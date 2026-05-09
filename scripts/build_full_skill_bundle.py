#!/usr/bin/env python3
"""Build the single-file ReFusion scene skill brief for external agents."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SOURCES = [
    ("Skill Entry Point", "skills/refusion-skills/SKILL.md"),
    (
        "Native Motion Scene Author Rule",
        "skills/refusion-skills/rules/native-motion-scene-author.md",
    ),
    (
        "Native Scene Intelligence Rule",
        "skills/refusion-skills/rules/native-scene-intelligence.md",
    ),
    (
        "Scene Migration v1 To v2 Rule",
        "skills/refusion-skills/rules/migration-v1-to-v2.md",
    ),
    ("SpeedyGraph Rule", "skills/refusion-skills/rules/speedygraph.md"),
    (
        "Effects And Renderer Rule",
        "skills/refusion-skills/rules/effects-and-renderer.md",
    ),
    (
        "Modern Motion Design Rule",
        "skills/refusion-skills/rules/modern-motion-design.md",
    ),
    (
        "Remotion Principles For ReFusion Rule",
        "skills/refusion-skills/rules/remotion-principles-for-refusion.md",
    ),
    (
        "Open Design Adaptation Rule",
        "skills/refusion-skills/rules/open-design-adaptation.md",
    ),
    ("Scene Program JSON Rule", "skills/refusion-skills/rules/scene-program-json.md"),
    (
        "Professional Timing Contract Rule",
        "skills/refusion-skills/rules/professional-timing-contract.md",
    ),
    ("Choreography Rule", "skills/refusion-skills/rules/choreography.md"),
    ("Composition Workspace Rule", "skills/refusion-skills/rules/composition-workspace.md"),
    ("Transition Authoring Rule", "skills/refusion-skills/rules/transitions.md"),
    ("Capability Registry Rule", "skills/refusion-skills/rules/capability-registry.md"),
    ("Tutorial Intake Rule", "skills/refusion-skills/rules/tutorial-intake.md"),
    ("Validation Rule", "skills/refusion-skills/rules/validation.md"),
    (
        "Director Brief Authoring v5 Rule",
        "skills/refusion-skills/rules/director-brief-authoring-v5.md",
    ),
    (
        "Director Plan Validator v5 Rule",
        "skills/refusion-skills/rules/director-plan-validator-v5.md",
    ),
    (
        "Motion Recipe Library v2 Rule",
        "skills/refusion-skills/rules/motion-recipe-library-v2.md",
    ),
    (
        "Brand-Aware Motion v5 Rule",
        "skills/refusion-skills/rules/brand-aware-motion-v5.md",
    ),
    (
        "Brand Icon Usage v5 Rule",
        "skills/refusion-skills/rules/brand-icon-usage-v5.md",
    ),
    (
        "Brand Asset Legal Fallback v5 Rule",
        "skills/refusion-skills/rules/brand-asset-legal-fallback-v5.md",
    ),
    (
        "Component Internal Choreography v5 Rule",
        "skills/refusion-skills/rules/component-internal-choreography-v5.md",
    ),
    (
        "Inter-Component Choreography v5 Rule",
        "skills/refusion-skills/rules/inter-component-choreography-v5.md",
    ),
    (
        "Background Semantic Pairing v5 Rule",
        "skills/refusion-skills/rules/background-semantic-pairing-v5.md",
    ),
    ("Text Layout v5 Rule", "skills/refusion-skills/rules/text-layout-v5.md"),
    ("Scene Composition v5 Rule", "skills/refusion-skills/rules/scene-composition-v5.md"),
    (
        "Rhythm Density Principles v5 Rule",
        "skills/refusion-skills/rules/rhythm-density-principles-v5.md",
    ),
    (
        "Professional Taste Checklist v5 Rule",
        "skills/refusion-skills/rules/professional-taste-checklist-v5.md",
    ),
    (
        "Repair Loop Examples v5 Rule",
        "skills/refusion-skills/rules/repair-loop-examples-v5.md",
    ),
    ("VERSION 5 Examples Catalog", "skills/refusion-skills/examples/v5/README.md"),
    ("Scene Program Validator Script", "scripts/validate_scene_program.py"),
    (
        "Basic Typewriter Intro Example",
        "skills/refusion-skills/examples/basic-typewriter-intro.json",
    ),
    (
        "Premium App Promo Example",
        "skills/refusion-skills/examples/premium-app-promo-scene.json",
    ),
    (
        "Revival Premium App Demo 60s Example",
        "skills/refusion-skills/examples/revival-premium-app-demo-60s.json",
    ),
    (
        "v5 Good Example 01",
        "skills/refusion-skills/examples/v5/good/good-01-prompt-morph.json",
    ),
    (
        "v5 Good Example 02",
        "skills/refusion-skills/examples/v5/good/good-02-feature-grid-fast-voice-smart-image.json",
    ),
    (
        "v5 Good Example 03",
        "skills/refusion-skills/examples/v5/good/good-03-saas-feedback-wall.json",
    ),
    (
        "v5 Good Example 04",
        "skills/refusion-skills/examples/v5/good/good-04-audio-engineering-card.json",
    ),
    (
        "v5 Good Example 05",
        "skills/refusion-skills/examples/v5/good/good-05-kinetic-captions-card.json",
    ),
    (
        "v5 Good Example 06",
        "skills/refusion-skills/examples/v5/good/good-06-image-retouch-card.json",
    ),
    (
        "v5 Good Example 07",
        "skills/refusion-skills/examples/v5/good/good-07-multi-aspect-adaptation.json",
    ),
    (
        "v5 Good Example 08",
        "skills/refusion-skills/examples/v5/good/good-08-ai-features-cascade.json",
    ),
    (
        "v5 Good Example 09",
        "skills/refusion-skills/examples/v5/good/good-09-social-app-promo.json",
    ),
    (
        "v5 Good Example 10",
        "skills/refusion-skills/examples/v5/good/good-10-tech-brand-intro.json",
    ),
    (
        "v5 Bad Example 01",
        "skills/refusion-skills/examples/v5/bad/bad-01-vague-intent.json",
    ),
    (
        "v5 Bad Example 02",
        "skills/refusion-skills/examples/v5/bad/bad-02-raw-coordinates-overuse.json",
    ),
    (
        "v5 Bad Example 03",
        "skills/refusion-skills/examples/v5/bad/bad-03-fade-only-cards.json",
    ),
    (
        "v5 Bad Example 04",
        "skills/refusion-skills/examples/v5/bad/bad-04-brand-without-registry.json",
    ),
    (
        "v5 Bad Example 05",
        "skills/refusion-skills/examples/v5/bad/bad-05-text-cut-mid-phrase.json",
    ),
    (
        "v5 Bad Example 06",
        "skills/refusion-skills/examples/v5/bad/bad-06-overloaded-motion-density.json",
    ),
    (
        "v5 Bad Example 07",
        "skills/refusion-skills/examples/v5/bad/bad-07-missing-primary-focus.json",
    ),
    (
        "v5 Bad Example 08",
        "skills/refusion-skills/examples/v5/bad/bad-08-contradictory-mood.json",
    ),
    (
        "v5 Bad Example 09",
        "skills/refusion-skills/examples/v5/bad/bad-09-component-choreography-missing.json",
    ),
    (
        "v5 Bad Example 10",
        "skills/refusion-skills/examples/v5/bad/bad-10-safe-area-violation.json",
    ),
]


def main() -> None:
    output = ROOT / "REFUSION_SCENE_SKILL_FULL.md"
    lines = [
        "# ReFusion Scene Skill Full Agent Brief",
        "",
        "This file is generated from the official ReFusion skill pack.",
        "Use it when an AI agent cannot browse repository folders or follow",
        "relative links such as `skills/refusion-skills/rules/*.md`.",
        "",
        "Do not edit this file directly. Update the source files and run:",
        "",
        "```bash",
        "python3 scripts/build_full_skill_bundle.py",
        "```",
        "",
        "## Included Sources",
        "",
    ]
    for _, rel_path in SOURCES:
        lines.append(f"- `{rel_path}`")
    lines.append("")

    for title, rel_path in SOURCES:
        source_path = ROOT / rel_path
        body = source_path.read_text(encoding="utf-8").strip()
        lines.extend(
            [
                "---",
                "",
                f"# {title}",
                "",
                f"Source: `{rel_path}`",
                "",
                body,
                "",
            ],
        )

    output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
