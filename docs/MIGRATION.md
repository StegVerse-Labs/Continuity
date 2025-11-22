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
