#!/usr/bin/env python3
"""Validate ReFusion Scene Program JSON before pasting it into the app."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


SCENE_SCHEMA = "refusion.scene-program/v1"
DIRECTOR_SCHEMA = "refusion.motion-director/v1"
BLOCKED_KEYS = {
    "code",
    "script",
    "function",
    "eval",
    "imports",
    "remoteImports",
    "shaderSource",
    "html",
    "css",
    "jsx",
    "react",
    "gsap",
}
LAYER_KINDS = {"shape", "text", "image", "video", "group"}
ELEMENT_KINDS = {"shape", "solid", "text", "image", "icon", "mask"}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Preflight a ReFusion DirectorPlan + SceneProgram JSON file.",
    )
    parser.add_argument("path", help="Path to a .json scene file")
    args = parser.parse_args()
    path = Path(args.path)
    errors: list[str] = []
    warnings: list[str] = []

    try:
        source = path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"ERROR: could not read {path}: {exc}", file=sys.stderr)
        return 2

    text = source.strip()
    if not text:
        errors.append("file is empty")
    if text.startswith("```") or text.endswith("```"):
        errors.append("remove Markdown fences; paste JSON only")
    if text.startswith("{") and not text.endswith("}"):
        errors.append("JSON appears incomplete: copy from the first `{` through the final `}`")

    try:
        payload = json.loads(text)
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}")
        payload = None

    if isinstance(payload, dict):
        check_blocked_keys(payload, errors)
        director = payload.get("directorPlan")
        scene = payload.get("sceneProgram")
        if scene is None and payload.get("schemaVersion") == SCENE_SCHEMA:
            scene = payload
        if director is None:
            warnings.append("missing directorPlan; agents should include one for professional planning")
        elif isinstance(director, dict):
            validate_director_plan(director, errors, warnings)
        else:
            errors.append("directorPlan must be an object")
        if isinstance(scene, dict):
            validate_scene_program(scene, errors, warnings)
        else:
            errors.append("missing sceneProgram object with schemaVersion refusion.scene-program/v1")
    elif payload is not None:
        errors.append("JSON root must be an object")

    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"OK: {path} is complete ReFusion Scene Program JSON")
    return 0


def check_blocked_keys(value: Any, errors: list[str], path: str = "") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}" if path else str(key)
            if key in BLOCKED_KEYS:
                errors.append(f"blocked executable/web key `{key}` at {child_path}")
            check_blocked_keys(child, errors, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            check_blocked_keys(child, errors, f"{path}[{index}]")


def validate_director_plan(
    plan: dict[str, Any],
    errors: list[str],
    warnings: list[str],
) -> None:
    if plan.get("schemaVersion") != DIRECTOR_SCHEMA:
        errors.append(f"directorPlan.schemaVersion must be {DIRECTOR_SCHEMA}")
    require_positive_number(plan, "durationMs", errors, "directorPlan.durationMs")
    require_positive_number(plan, "frameRate", errors, "directorPlan.frameRate")
    for key in ("beats", "components", "primitives"):
        if not isinstance(plan.get(key), list):
            errors.append(f"directorPlan.{key} must be a list")
    component_ids = {item.get("id") for item in plan.get("components", []) if isinstance(item, dict)}
    beat_ids = {item.get("id") for item in plan.get("beats", []) if isinstance(item, dict)}
    for index, primitive in enumerate(plan.get("primitives", [])):
        if not isinstance(primitive, dict):
            errors.append(f"directorPlan.primitives[{index}] must be an object")
            continue
        if primitive.get("beatId") not in beat_ids:
            warnings.append(f"primitive {primitive.get('id', index)} references unknown beatId")
        if primitive.get("targetComponentId") not in component_ids:
            warnings.append(f"primitive {primitive.get('id', index)} references unknown targetComponentId")


def validate_scene_program(
    scene: dict[str, Any],
    errors: list[str],
    warnings: list[str],
) -> None:
    if scene.get("schemaVersion") != SCENE_SCHEMA:
        errors.append(f"sceneProgram.schemaVersion must be {SCENE_SCHEMA}")
    duration = require_positive_number(scene, "durationMs", errors, "sceneProgram.durationMs")
    require_positive_number(scene, "frameRate", errors, "sceneProgram.frameRate")
    layers = scene.get("layers")
    if not isinstance(layers, list) or not layers:
        errors.append("sceneProgram.layers must be a non-empty list")
        return
    layer_ids: set[str] = set()
    for index, layer in enumerate(layers):
        layer_path = f"sceneProgram.layers[{index}]"
        if not isinstance(layer, dict):
            errors.append(f"{layer_path} must be an object")
            continue
        layer_id = require_string(layer, "id", errors, f"{layer_path}.id")
        require_string(layer, "name", errors, f"{layer_path}.name")
        kind = require_string(layer, "kind", errors, f"{layer_path}.kind")
        if kind and kind not in LAYER_KINDS:
            errors.append(f"{layer_path}.kind `{kind}` is unsupported")
        if layer_id in layer_ids:
            errors.append(f"duplicate layer id `{layer_id}`")
        layer_ids.add(layer_id)
        start = require_non_negative_number(layer, "startMs", errors, f"{layer_path}.startMs")
        layer_duration = require_positive_number(layer, "durationMs", errors, f"{layer_path}.durationMs")
        if duration is not None and start is not None and layer_duration is not None:
            if start + layer_duration > duration:
                warnings.append(f"{layer_path} extends beyond scene duration")
        elements = layer.get("elements")
        if not isinstance(elements, list) or not elements:
            errors.append(f"{layer_path}.elements must be a non-empty list")
            continue
        validate_elements(elements, errors, warnings, layer_path, layer_duration)
        validate_channels(layer.get("channels"), errors, f"{layer_path}.channels", layer_duration, allow_missing=True)


def validate_elements(
    elements: list[Any],
    errors: list[str],
    warnings: list[str],
    layer_path: str,
    layer_duration: float | None,
) -> None:
    ids: set[str] = set()
    for index, element in enumerate(elements):
        path = f"{layer_path}.elements[{index}]"
        if not isinstance(element, dict):
            errors.append(f"{path} must be an object")
            continue
        element_id = require_string(element, "id", errors, f"{path}.id")
        kind = require_string(element, "kind", errors, f"{path}.kind")
        if kind and kind not in ELEMENT_KINDS:
            errors.append(f"{path}.kind `{kind}` is unsupported")
        if element_id in ids:
            errors.append(f"duplicate element id `{element_id}` in {layer_path}")
        ids.add(element_id)
        if not isinstance(element.get("properties", {}), dict):
            errors.append(f"{path}.properties must be an object")
        validate_channels(element.get("channels"), errors, f"{path}.channels", layer_duration, allow_missing=True)
        if kind == "text" and not element.get("text"):
            warnings.append(f"{path} is text but has no text string")


def validate_channels(
    channels: Any,
    errors: list[str],
    path: str,
    owner_duration: float | None,
    *,
    allow_missing: bool,
) -> None:
    if channels is None:
        if not allow_missing:
            errors.append(f"{path} must be a list")
        return
    if not isinstance(channels, list):
        errors.append(f"{path} must be a list")
        return
    for index, channel in enumerate(channels):
        channel_path = f"{path}[{index}]"
        if not isinstance(channel, dict):
            errors.append(f"{channel_path} must be an object")
            continue
        require_string(channel, "property", errors, f"{channel_path}.property")
        keyframes = channel.get("keyframes")
        if not isinstance(keyframes, list) or not keyframes:
            errors.append(f"{channel_path}.keyframes must be a non-empty list")
            continue
        last_time = -1.0
        for keyframe_index, keyframe in enumerate(keyframes):
            keyframe_path = f"{channel_path}.keyframes[{keyframe_index}]"
            if not isinstance(keyframe, dict):
                errors.append(f"{keyframe_path} must be an object")
                continue
            time_ms = require_non_negative_number(keyframe, "timeMs", errors, f"{keyframe_path}.timeMs")
            if time_ms is not None:
                if time_ms < last_time:
                    errors.append(f"{keyframe_path}.timeMs must be sorted")
                last_time = time_ms
                if owner_duration is not None and time_ms > owner_duration:
                    errors.append(f"{keyframe_path}.timeMs exceeds owning layer duration")
            if "value" not in keyframe:
                errors.append(f"{keyframe_path}.value is required")


def require_string(data: dict[str, Any], key: str, errors: list[str], path: str) -> str | None:
    value = data.get(key)
    if isinstance(value, str) and value.strip():
        return value
    errors.append(f"{path} is required")
    return None


def require_positive_number(
    data: dict[str, Any],
    key: str,
    errors: list[str],
    path: str,
) -> float | None:
    value = data.get(key)
    if isinstance(value, (int, float)) and value > 0:
        return float(value)
    errors.append(f"{path} must be a positive number")
    return None


def require_non_negative_number(
    data: dict[str, Any],
    key: str,
    errors: list[str],
    path: str,
) -> float | None:
    value = data.get(key)
    if isinstance(value, (int, float)) and value >= 0:
        return float(value)
    errors.append(f"{path} must be a non-negative number")
    return None


if __name__ == "__main__":
    raise SystemExit(main())
