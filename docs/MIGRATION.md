# Continuity v1 → v2 Migration Guide

This document describes how the StegVerse continuity system transitions from the
original, manually maintained v1 structure into the autonomous and parallelized
Continuity v2 architecture.

---

## Why Migrate?

Continuity v1 served as the historical foundation of StegVerse.  
It captured conversations, reflections, decisions, and design evolution.

However, v1 had limitations:

- No autonomous generation
- No task lanes or worker entities
- No cross-repo drift detection
- No long-term scalability framework
- No structured preservation of legacy artifacts

Continuity v2 addresses all of these.

---

## Migration Principles

1. **Do not overwrite v1.**  
   All v1 content must be preserved exactly as it existed.

2. **Import v1 into `/docs/legacy/`.**  
   Each import is placed under a timestamped directory.

3. **v2 becomes authoritative moving forward.**  
   All new continuity tasks, workers, entities, and workflows operate under v2.

4. **v1 becomes read-only.**  
   Even if additional v1 content is imported later, it must be preserved verbatim.

---

## Migration Steps

### **Step 1 — Create the v2 Repository**
Initialize the repo with the seed v2 files (the ones you're currently uploading).

### **Step 2 — Import v1 Files**
Place all historical continuity content into:

/docs/legacy/

Each import folder must include:

- `README` summarizing the import
- All v1 content as-is

### **Step 3 — Add v2 Expansion Tools**
The v2 bootstrap or OMEGA expansion can generate:

- task lanes  
- workflows  
- entity definitions  
- diagrams  
- status files  
- and more  

This turns v2 into a living engine.

### **Step 4 — Run Drift Detection (Optional)**
Actions such as `sce_drift_scan` or `sce_snapshot` can validate repo health,
naming consistency, and cross-repo coherence.

### **Step 5 — Begin Using v2 as the Active Layer**
From this point on:

- All new updates go into `docs/*`, not legacy.
- All workflows operate under v2 rules.
- v1 serves as an immutable historical record.

---

## Outcome of Migration

After migration:

- v1 is frozen and safely preserved.  
- v2 becomes fully operational.  
- The StegVerse continuity layer supports autonomous growth, parallel tasks,
  and multi-repo awareness.

This file explains the correct and safe process for transitioning from v1 → v2.
