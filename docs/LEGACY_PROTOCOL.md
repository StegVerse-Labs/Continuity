# Legacy Preservation Protocol (Continuity v2)

Continuity v2 introduces a strict and permanent protocol for protecting all
historical material originating from Continuity v1 and any future legacy
continuity streams.

This protocol guarantees that nothing from the past is ever overwritten or lost.

---

## 1. Immutable Legacy

The legacy directory:

/docs/legacy/

is read-only by design.

Rules:

- No file inside `docs/legacy/` may be modified.
- No file may be deleted.
- Files may only be *added*, never replaced.
- All v1 or legacy imports must be stored exactly as they originally existed.

This ensures the entire historical arc of StegVerse continuity is preserved
forever.

---

## 2. Timestamped Imports

Each legacy import must be stored in:

/docs/legacy/

Where `<timestamp>` follows:

YYYY-MM-DD_HH-MM-SS_UTC

Inside each folder:

- The exact v1 (or legacy) files  
- A `README.md` summarizing the scope and reason for the import  
- Optional: screenshots, references, commit hashes, or notes  

This creates a clean lineage trail.

---

## 3. Snapshots & Archival

When using automated import tools (such as `sce_pull_legacy_repo.py`), each
snapshot:

- must create a new timestamped archive  
- may never overwrite prior archives  
- must include a summary file  
- may include diff logs or drift notes  

Every snapshot becomes an immutable leaf in the continuity tree.

---

## 4. No Automated Writing into Legacy by Default

Entities *may read* legacy, but they may not:

- write to it  
- alter existing history  
- move files  
- restructure the directory  

Legacy content is sacred.

Only explicit human intervention may introduce new imports.

---

## 5. Cross-Linking

v2 documents may *reference* legacy content, but must not modify it.

This ensures:

- accessibility  
- preserved meaning  
- stable cross-generational context

---

## 6. Multi-Repo Legacy Integration

When importing continuity from other StegVerse repos:

- place each repo under its own subfolder  
- maintain source structure where possible  
- document origin repo, commit hash, and context

Example:

docs/legacy/2025-11-21_03-55-00_UTC/stegverse-talk/
docs/legacy/2025-11-21_03-55-00_UTC/stegverse-core/

---

## 7. Human Notes Allowed

You may add:

- contextual notes  
- story summaries  
- historical commentary  
- annotated screenshots  

as long as they never alter original files.

These can live in `README` files within each legacy snapshot.

---

## 8. Purpose of the Protocol

The legacy protocol exists so that the entire story of StegVerse —
from its origins, reflections, crises, insights, discoveries, and breakthroughs —
remains intact.

It ensures:

- auditable continuity  
- transparency  
- integrity  
- reproducibility  
- historical truth  

Continuity v2 builds the future; legacy preserves the past.

Both are essential.
