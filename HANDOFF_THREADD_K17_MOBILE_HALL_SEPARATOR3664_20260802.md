# Handoff: mobile fan / Hall separator for exact3664

Adopt `/home/amodo/or15/work/threadD_k17_mobile_hall3664_20260802/output`.

- Remove the 61 `MOBILE_FAN_UNSAT` rows in `output/certificates.tsv` from any not-yet-started q1 queue.  They are all 30 anchor-6 residuals and all 31 anchor-8 residuals.
- Keep the other 3,603 rows on the exact q1 path.  `UNDECIDED` is not evidence of feasibility.
- No `HALL3_UNSAT` row was found.
- Do not build one common exact exterior language for this family: its union interface already contains 6,892 of 7,612 outgoing/incoming/orientation resources and 4,925 of 7,612 colours.

Independent replay:

```bash
cd /home/amodo/or15/work/threadD_k17_mobile_hall3664_20260802
python3 tools/verify_threadD_k17_mobile_hall61_20260802.py \
  output/certificates.tsv output/providers.tsv output/blockers.tsv \
  input/cases.tsv exact_crosscheck/results exact_crosscheck/certs \
  output/independent_replay.tsv output/independent_replay.audit.json
```

Expected final line:

```text
PASS_INDEPENDENT_MOBILE_HALL61_REPLAY unsat=61 blockers=1952 exact=61
```

The generator can be replayed CPU-only on a single disjoint core.  It does not emit or solve CNF.  Its exact scope and the exterior-language no-go are recorded in `MATH_THREADD_K17_MOBILE_HALL_SEPARATOR3664_20260802.md`.
