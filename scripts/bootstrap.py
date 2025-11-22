import json, pathlib, datetime

ROOT = pathlib.Path(".")
MANIFEST = json.load(open("manifest.json"))
TEMPLATES = ROOT / "templates"

def load_tmpl(name):
    return (TEMPLATES / name).read_text(encoding="utf-8")

def render(tmpl, vars):
    out = tmpl
    for k, v in vars.items():
        out = out.replace("{{"+k+"}}", str(v))
    return out

def write_file(path, content):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

def bullets_to_md(bullets):
    return "\n".join([f"- {b}" for b in bullets])

def main():
    ts = datetime.datetime.utcnow().isoformat() + "Z"

    # --- Core docs ---
    for item in MANIFEST.get("create", []):
        tmpl = load_tmpl(item["template"])
        vars = dict(item.get("vars", {}))
        vars.setdefault("GENERATED_AT", ts)
        write_file(item["path"], render(tmpl, vars))

    # --- Task lanes ---
    lane_tmpl = load_tmpl("lane.md.tmpl")
    for lane in MANIFEST.get("lanes", []):
        vars = {
            "TITLE": lane["title"],
            "GENERATED_AT": ts,
            "BULLETS": bullets_to_md(lane.get("bullets", []))
        }
        write_file(lane["file"], render(lane_tmpl, vars))

    # --- Entities ---
    entities = {
        "version": MANIFEST.get("version"),
        "generated_at": ts,
        "guardrails": {
            "defensive_only": True,
            "no_offensive_security": True,
            "require_logging": True,
            "short_lived_tokens": True
        },
        "entities": MANIFEST.get("entities", [])
    }
    write_file("entities/entities.omega.json", json.dumps(entities, indent=2))

    # --- Workflow generation ---
    wf_tmpl = load_tmpl("workflow.yml.tmpl")
    for wf in MANIFEST.get("workflows", []):
        vars = {
            "NAME": wf["name"],
            "COMMAND": wf["command"],
            "COMMIT_MSG": wf["commit_msg"]
        }
        write_file(wf["path"], render(wf_tmpl, vars))

    # --- Auto-create dirs ---
    for folder in ["docs/state","docs/legacy","docs/conversations","docs/diagrams","docs/tasks/lanes"]:
        (ROOT / folder).mkdir(parents=True, exist_ok=True)

    # --- Diagram placeholder ---
    if not (ROOT/"docs/diagrams/over_system.mmd").exists():
        write_file("docs/diagrams/over_system.mmd", "```mermaid\nflowchart TD\nA-->B\nB-->C\nC-->A\n```\n")

    print("✅ Bootstrap expansion complete.")

if __name__ == "__main__":
    main()
