# AI Entity Governance Rules (Continuity v2)

Continuity v2 introduces structured AI entities that may read, analyze,
synthesize, and emit continuity tasks across the StegVerse ecosystem.  
These rules define what entities *can* and *cannot* do.

These rules apply universally across all entities in v2, v2-MAX, and v2-OMEGA.

---

## Core Principles

### **1. Defensive-Only Behavior**
Entities may:
- scan for drift
- repair documentation
- generate tasks
- update state
- map topology
- validate links and workflows

Entities may *not*:
- perform offensive actions
- attack systems
- exploit vulnerabilities
- attempt privilege escalation
- engage in unauthorized access outside the repo environment

---

## 2. No Secret Creation Without Policy

Entities may:
- read secrets metadata (scope names, existence)
- validate rotation schedules
- confirm drift in token usage

Entities may *not*:
- create new PATs
- modify token values
- perform direct secret injection
- alter GitHub org-level secrets

All secret rotation must be human-approved or follow a specific vault policy.

---

## 3. All Actions Must Produce Clear Outputs

Every entity must write its outputs to a file in `docs/state/` or a lane file.

Examples:
- `ghost_findings.md`
- `drift_report.md`
- `heal_report.md`
- `deps.md`
- `linkproof.md`
- `benchmarks.md`

This ensures:
- reproducibility  
- traceability  
- auditability  

No silent actions.

---

## 4. Entities Do Not Modify Legacy Content

Entities may read legacy content but cannot modify anything in:
