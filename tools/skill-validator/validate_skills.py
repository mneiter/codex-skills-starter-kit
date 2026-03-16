#!/usr/bin/env python3

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple


BASE_LAYERS = ("atomic", "guardrails", "orchestration")
BASE_REQUIRED_SECTIONS = (
    "Purpose",
    "When To Use",
    "Inputs",
    "Process",
    "Outputs",
    "Guardrails",
    "Verification",
    "Escalation",
)
SKILL_NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n(.*)\Z", re.DOTALL)
TOP_LEVEL_HEADING_RE = re.compile(r"^# (.+?)\s*$")
MARKDOWN_HEADING_RE = re.compile(r"^#{2,6}\s+([A-Za-z0-9-]+)\s*$")


@dataclass
class Issue:
    severity: str
    message: str
    path: Optional[Path] = None


@dataclass
class PackRoot:
    kind: str
    name: str
    root: Path
    readme_path: Path
    manifest_path: Path
    index_path: Path


@dataclass
class SolutionGroup:
    name: str
    root: Path
    readme_path: Path
    leaf_packs: List[PackRoot]


def add_issue(issues: List[Issue], severity: str, message: str, path: Optional[Path] = None) -> None:
    issues.append(Issue(severity=severity, message=message, path=path))


def relpath(path: Optional[Path], root: Path) -> str:
    if path is None:
        return ""
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def clean_item(line: str) -> str:
    line = line.strip()
    line = re.sub(r"^[-*]\s+", "", line)
    line = re.sub(r"^\d+\.\s+", "", line)
    return line.strip()


def split_lines(block: str) -> List[str]:
    items: List[str] = []
    for raw_line in block.splitlines():
        cleaned = clean_item(raw_line)
        if cleaned:
            items.append(cleaned)
    return items


def extract_frontmatter(text: str, path: Path, issues: List[Issue]) -> Tuple[Dict[str, str], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        add_issue(issues, "ERROR", "Missing or malformed frontmatter.", path)
        return {}, text

    frontmatter_text, body = match.groups()
    frontmatter: Dict[str, str] = {}
    for line in frontmatter_text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        parsed = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", stripped)
        if not parsed:
            add_issue(issues, "ERROR", f"Unsupported frontmatter line: {line}", path)
            continue
        key, value = parsed.groups()
        frontmatter[key] = value.strip()
    return frontmatter, body


def extract_sections(body: str) -> Dict[str, str]:
    sections: Dict[str, List[str]] = {}
    current_heading: Optional[str] = None
    for line in body.splitlines():
        heading = TOP_LEVEL_HEADING_RE.match(line)
        if heading:
            current_heading = heading.group(1).strip()
            sections[current_heading] = []
            continue
        if current_heading is not None:
            sections[current_heading].append(line)
    return {key: "\n".join(value).strip() for key, value in sections.items()}


def extract_dependencies(inputs: List[str]) -> List[str]:
    for item in inputs:
        lowered = item.lower()
        if lowered.startswith("dependencies:") or lowered.startswith("dependency:"):
            raw_value = item.split(":", 1)[1].strip()
            if raw_value.lower() in ("", "none", "n/a", "na"):
                return []
            return [part.strip() for part in re.split(r"[;,]", raw_value) if part.strip()]
    return []


def parse_manifest(path: Path, issues: List[Issue]) -> List[Dict[str, str]]:
    if not path.exists():
        add_issue(issues, "ERROR", "Missing manifest.", path)
        return []

    rows: List[Dict[str, str]] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    header: Optional[List[str]] = None
    in_table = False
    for index, line in enumerate(lines):
        if not line.startswith("|"):
            if in_table:
                break
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if header is None:
            header = cells
            continue
        if not in_table:
            in_table = True
            continue
        if len(cells) != len(header):
            add_issue(issues, "ERROR", f"Malformed manifest row at line {index + 1}.", path)
            continue
        row = {header[i]: cells[i] for i in range(len(header))}
        if any(value for value in row.values()):
            rows.append(row)
    if header is None:
        add_issue(issues, "ERROR", "Manifest table header not found.", path)
    return rows


def parse_index(path: Path, issues: List[Issue]) -> List[str]:
    if not path.exists():
        add_issue(issues, "ERROR", "Missing index.", path)
        return []
    names: List[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = MARKDOWN_HEADING_RE.match(line)
        if not match:
            continue
        heading = match.group(1).strip()
        if SKILL_NAME_RE.match(heading):
            names.append(heading)
    return names


def manifest_path_value(value: str) -> str:
    return value.strip().strip("`")


def build_metadata(name: str, description: str, sections: Dict[str, str], layer: str) -> Dict[str, object]:
    when_to_use = split_lines(sections.get("When To Use", ""))
    inputs = split_lines(sections.get("Inputs", ""))
    outputs = split_lines(sections.get("Outputs", ""))
    verification = split_lines(sections.get("Verification", ""))

    purpose = ""
    for line in sections.get("Purpose", "").splitlines():
        if line.strip():
            purpose = line.strip()
            break

    triggers: List[str] = []
    if description.strip():
        triggers.append(description.strip())
    triggers.extend(item for item in when_to_use if item not in triggers)

    return {
        "name": name,
        "layer": layer,
        "purpose": purpose,
        "triggers": triggers,
        "inputs": inputs,
        "outputs": outputs,
        "dependencies": extract_dependencies(inputs),
        "verification": verification,
    }


def validate_metadata(metadata: Dict[str, object], schema: Dict[str, object], issues: List[Issue], path: Path) -> None:
    required = schema.get("required", [])
    properties = schema.get("properties", {})

    for field in required:
        if field not in metadata:
            add_issue(issues, "ERROR", f"Missing normalized metadata field '{field}'.", path)
            continue

        value = metadata[field]
        field_schema = properties.get(field, {})
        field_type = field_schema.get("type")

        if field_type == "string":
            if not isinstance(value, str) or not value.strip():
                add_issue(issues, "ERROR", f"Metadata field '{field}' must be a non-empty string.", path)
        elif field_type == "array":
            if not isinstance(value, list):
                add_issue(issues, "ERROR", f"Metadata field '{field}' must be a list.", path)
                continue
            min_items = field_schema.get("minItems", 0)
            if len(value) < min_items:
                add_issue(
                    issues,
                    "ERROR",
                    f"Metadata field '{field}' must contain at least {min_items} item(s).",
                    path,
                )
            for item in value:
                if not isinstance(item, str) or not item.strip():
                    add_issue(
                        issues,
                        "ERROR",
                        f"Metadata field '{field}' must contain only non-empty strings.",
                        path,
                    )

    layer_enum = properties.get("layer", {}).get("enum", [])
    layer = metadata.get("layer")
    if layer and layer not in layer_enum:
        add_issue(issues, "ERROR", f"Invalid layer value '{layer}'.", path)


def load_skill(path: Path, layer: str, schema: Dict[str, object], issues: List[Issue]) -> Optional[Tuple[str, Dict[str, object]]]:
    text = path.read_text(encoding="utf-8")
    frontmatter, body = extract_frontmatter(text, path, issues)

    name = frontmatter.get("name", "").strip()
    description = frontmatter.get("description", "").strip()
    if not name:
        add_issue(issues, "ERROR", "Missing frontmatter field 'name'.", path)
        return None
    if not description:
        add_issue(issues, "ERROR", "Missing frontmatter field 'description'.", path)
        return None
    if not SKILL_NAME_RE.match(name):
        add_issue(issues, "ERROR", f"Invalid skill name '{name}'.", path)

    sections = extract_sections(body)
    for section in BASE_REQUIRED_SECTIONS:
        if section not in sections or not sections[section].strip():
            add_issue(issues, "ERROR", f"Missing or empty section '{section}'.", path)

    metadata = build_metadata(name=name, description=description, sections=sections, layer=layer)
    validate_metadata(metadata=metadata, schema=schema, issues=issues, path=path)
    return name, metadata


def validate_manifest_rows(
    discovered: Dict[str, Path],
    rows: List[Dict[str, str]],
    manifest_path: Path,
    scope_name: str,
    issues: List[Issue],
) -> Dict[str, Dict[str, str]]:
    row_map: Dict[str, Dict[str, str]] = {}
    names_from_manifest: List[str] = []
    for row in rows:
        skill_name = row.get("Skill", "")
        if not skill_name:
            continue
        names_from_manifest.append(skill_name)
        row_map[skill_name] = row

    if sorted(discovered.keys()) != sorted(names_from_manifest):
        add_issue(
            issues,
            "ERROR",
            f"{scope_name} manifest entries do not match discovered skill folders.",
            manifest_path,
        )

    for name, relative_path in discovered.items():
        row = row_map.get(name)
        if row is None:
            continue
        if manifest_path_value(row.get("Path", "")) != str(relative_path):
            add_issue(
                issues,
                "ERROR",
                f"Manifest path for '{name}' does not match the real skill path.",
                manifest_path,
            )
    return row_map


def validate_index_names(
    discovered: Dict[str, Path],
    index_names: List[str],
    index_path: Path,
    scope_name: str,
    issues: List[Issue],
) -> None:
    if sorted(discovered.keys()) != sorted(index_names):
        add_issue(
            issues,
            "ERROR",
            f"{scope_name} index headings do not match discovered skill folders.",
            index_path,
        )


def discover_base(repo_root: Path, issues: List[Issue]) -> Dict[str, Tuple[Path, str]]:
    base_root = repo_root / ".codex" / "skills"
    discovered: Dict[str, Tuple[Path, str]] = {}
    if not base_root.exists():
        add_issue(issues, "ERROR", "Missing .codex/skills directory.", base_root)
        return discovered

    for layer in BASE_LAYERS:
        layer_root = base_root / layer
        if not layer_root.exists():
            add_issue(issues, "ERROR", f"Missing canonical layer directory '{layer}'.", layer_root)
            continue
        for child in sorted(layer_root.iterdir()):
            if not child.is_dir():
                continue
            skill_file = child / "SKILL.md"
            if not skill_file.exists():
                add_issue(issues, "ERROR", "Skill folder is missing SKILL.md.", child)
                continue
            discovered[child.name] = (skill_file, layer)
    return discovered


def discover_pack_layout(repo_root: Path, issues: List[Issue]) -> Tuple[List[PackRoot], List[SolutionGroup]]:
    packs_root = repo_root / "packs"
    direct_packs: List[PackRoot] = []
    solution_groups: List[SolutionGroup] = []
    if not packs_root.exists():
        return direct_packs, solution_groups

    for child in sorted(packs_root.iterdir()):
        if not child.is_dir():
            continue

        readme_path = child / "README.md"
        manifest_path = child / "skills-manifest.md"
        index_path = child / "skills-index.md"
        child_dirs = [entry for entry in sorted(child.iterdir()) if entry.is_dir()]
        extra_files = [entry for entry in child.iterdir() if entry.is_file() and entry.name != "README.md"]
        nested_pack_roots = [
            entry
            for entry in child_dirs
            if (entry / "skills-manifest.md").exists() or (entry / "skills-index.md").exists()
        ]

        if manifest_path.exists() or index_path.exists():
            if nested_pack_roots:
                add_issue(
                    issues,
                    "ERROR",
                    f"Top-level packs entry '{child.name}' mixes direct pack and solution group signals.",
                    child,
                )
            direct_packs.append(
                PackRoot(
                    kind="direct pack",
                    name=child.name,
                    root=child,
                    readme_path=readme_path,
                    manifest_path=manifest_path,
                    index_path=index_path,
                )
            )
            continue

        if not readme_path.exists():
            add_issue(
                issues,
                "ERROR",
                f"Top-level packs entry '{child.name}' must be a direct pack or a solution group with README.md.",
                child,
            )
            continue

        if extra_files:
            add_issue(
                issues,
                "ERROR",
                f"Solution group '{child.name}' must contain only README.md at its root.",
                child,
            )

        leaf_packs: List[PackRoot] = []
        for subdir in child_dirs:
            leaf_packs.append(
                PackRoot(
                    kind="leaf pack",
                    name=f"{child.name}/{subdir.name}",
                    root=subdir,
                    readme_path=subdir / "README.md",
                    manifest_path=subdir / "skills-manifest.md",
                    index_path=subdir / "skills-index.md",
                )
            )
        solution_groups.append(
            SolutionGroup(
                name=child.name,
                root=child,
                readme_path=readme_path,
                leaf_packs=leaf_packs,
            )
        )

    return direct_packs, solution_groups


def discover_pack_skills(pack_root: PackRoot, repo_root: Path, issues: List[Issue]) -> Dict[str, Path]:
    discovered: Dict[str, Path] = {}
    skills_dir = pack_root.root / "skills"
    if not skills_dir.exists():
        return discovered

    for child in sorted(skills_dir.iterdir()):
        if not child.is_dir():
            continue
        skill_file = child / "SKILL.md"
        if not skill_file.exists():
            add_issue(issues, "ERROR", "Skill folder is missing SKILL.md.", child)
            continue
        discovered[child.name] = skill_file.relative_to(repo_root)
    return discovered


def validate_pack_root(
    pack_root: PackRoot,
    repo_root: Path,
    schema: Dict[str, object],
    seen_skill_names: Dict[str, Path],
    issues: List[Issue],
) -> int:
    if not pack_root.readme_path.exists():
        add_issue(issues, "ERROR", f"Missing README.md for {pack_root.kind} '{pack_root.name}'.", pack_root.root)

    rows = parse_manifest(pack_root.manifest_path, issues)
    index_names = parse_index(pack_root.index_path, issues)
    discovered_pack = discover_pack_skills(pack_root, repo_root, issues)

    row_map = validate_manifest_rows(
        discovered=discovered_pack,
        rows=rows,
        manifest_path=pack_root.manifest_path,
        scope_name=f"{pack_root.kind.title()} '{pack_root.name}'",
        issues=issues,
    )
    validate_index_names(
        discovered=discovered_pack,
        index_names=index_names,
        index_path=pack_root.index_path,
        scope_name=f"{pack_root.kind.title()} '{pack_root.name}'",
        issues=issues,
    )

    count = 0
    for folder_name, relative_path in discovered_pack.items():
        row = row_map.get(folder_name)
        layer = row.get("Layer", "") if row else ""
        if row and row.get("Layer") not in BASE_LAYERS:
            add_issue(
                issues,
                "ERROR",
                f"{pack_root.kind.title()} manifest for '{folder_name}' uses an invalid layer token.",
                pack_root.manifest_path,
            )
        loaded = load_skill(repo_root / relative_path, layer, schema, issues)
        if loaded is None:
            continue
        name, _metadata = loaded
        if name in seen_skill_names:
            add_issue(issues, "ERROR", f"Duplicate skill name '{name}'.", repo_root / relative_path)
        seen_skill_names[name] = repo_root / relative_path
        count += 1
        if folder_name != name:
            add_issue(
                issues,
                "WARN",
                f"Folder name '{folder_name}' does not match skill name '{name}'.",
                repo_root / relative_path,
            )
    return count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate skill repository structure.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Repository root to validate.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = args.root.resolve()
    issues: List[Issue] = []
    info_lines: List[str] = []
    schema_path = repo_root / "tools" / "skill-validator" / "skill-metadata-schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))

    total_skills = 0
    seen_skill_names: Dict[str, Path] = {}

    base_manifest_path = repo_root / ".codex" / "skills" / "skills-manifest.md"
    base_index_path = repo_root / ".codex" / "skills" / "skills-index.md"
    base_rows = parse_manifest(base_manifest_path, issues)
    base_index_names = parse_index(base_index_path, issues)
    base_skills = discover_base(repo_root, issues)
    base_paths = {name: path.relative_to(repo_root) for name, (path, _layer) in base_skills.items()}
    base_row_map = validate_manifest_rows(base_paths, base_rows, base_manifest_path, "Base skills", issues)
    validate_index_names(base_paths, base_index_names, base_index_path, "Base skills", issues)

    base_count = 0
    for folder_name, (skill_path, layer) in base_skills.items():
        loaded = load_skill(skill_path, layer, schema, issues)
        if loaded is None:
            continue
        name, _metadata = loaded
        row = base_row_map.get(name)
        if row and row.get("Layer") != layer:
            add_issue(
                issues,
                "ERROR",
                f"Manifest layer for '{name}' does not match its canonical path.",
                base_manifest_path,
            )
        if name in seen_skill_names:
            add_issue(issues, "ERROR", f"Duplicate skill name '{name}'.", skill_path)
        seen_skill_names[name] = skill_path
        base_count += 1
        total_skills += 1
        if folder_name != name:
            add_issue(issues, "WARN", f"Folder name '{folder_name}' does not match skill name '{name}'.", skill_path)

    direct_packs, solution_groups = discover_pack_layout(repo_root, issues)

    for direct_pack in direct_packs:
        count = validate_pack_root(direct_pack, repo_root, schema, seen_skill_names, issues)
        total_skills += count
        if count == 0:
            info_lines.append(f"INFO: direct pack {direct_pack.name} has no skills yet")
        else:
            info_lines.append(f"INFO: validated {count} skills in direct pack {direct_pack.name}")

    for solution_group in solution_groups:
        info_lines.append(f"INFO: discovered solution group {solution_group.name}")
        if not solution_group.leaf_packs:
            info_lines.append(f"INFO: solution group {solution_group.name} has no leaf packs yet")
            continue
        for leaf_pack in solution_group.leaf_packs:
            count = validate_pack_root(leaf_pack, repo_root, schema, seen_skill_names, issues)
            total_skills += count
            if count == 0:
                info_lines.append(f"INFO: leaf pack {leaf_pack.name} has no skills yet")
            else:
                info_lines.append(f"INFO: validated {count} skills in leaf pack {leaf_pack.name}")

    errors = [issue for issue in issues if issue.severity == "ERROR"]
    warnings = [issue for issue in issues if issue.severity == "WARN"]

    print(f"INFO: discovered {base_count} canonical base skills")
    for line in info_lines:
        print(line)
    for issue in warnings + errors:
        suffix = f" ({relpath(issue.path, repo_root)})" if issue.path else ""
        print(f"{issue.severity}: {issue.message}{suffix}")

    if errors:
        print(
            f"INFO: validation failed with {total_skills} skills checked, {len(errors)} errors, {len(warnings)} warnings"
        )
        return 1

    print(f"INFO: validation passed with {total_skills} skills checked, 0 errors, {len(warnings)} warnings")
    return 0


if __name__ == "__main__":
    sys.exit(main())
