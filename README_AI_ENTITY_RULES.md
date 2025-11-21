# AI Entity Governance — Continuity v2

AI entities must operate under strict, documented constraints.

---

# 🛡 Allowed
- Read repo state  
- Generate reports  
- Emit tasks  
- Normalize READMEs  
- Map org drift  
- Graph repo relationships  
- Suggest improvements  
- Maintain STATUS.md  
- Repair workflows (SCW Mesh)  
- Add new entities into `entities.max.json`  

---

# ❌ Forbidden
- Editing secrets  
- Creating long-lived tokens  
- Deleting files  
- Overwriting `/docs/legacy/`  
- Removing historical evidence  
- Making irreversible structural changes  
- Acting outside declared scopes  

---

# 🔐 Safety
- Every action must produce a log  
- Every write must be commit-tracked  
- Every suggestion must be attached to a task  
- DriftScan cannot alter repos (read-only)  
- VaultGuard must never elevate itself  

---

# 📘 Vision
Entities work *in parallel* but *under governance*.

Continuity v2 is capable of growth  
but not chaos.
