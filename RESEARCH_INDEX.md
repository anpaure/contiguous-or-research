# Research index

## Full chronological log

[`MATHEMATICAL_HANDOFF.md`](MATHEMATICAL_HANDOFF.md) is the complete working
log.  It intentionally preserves failed routes and superseded claims.  Always
read its opening current-status block first.

## General lower bound and synthesis

- [`MONOTONE_DEADLINE_LOWER_BOUND_AND_EQUALITY_AUDIT_20260727.md`](MONOTONE_DEADLINE_LOWER_BOUND_AND_EQUALITY_AUDIT_20260727.md)
- [`EXACT_OR_FORMULA_SYSTEMATIZED_UNDERSTANDING_20260728.md`](EXACT_OR_FORMULA_SYSTEMATIZED_UNDERSTANDING_20260728.md)

## Exact finite results

- [`answers/`](answers/) contains normalized optimal words for `1<=k<=14`.
- [`K11_EXACT_465_SEARCH_CERTIFICATE_20260727.md`](K11_EXACT_465_SEARCH_CERTIFICATE_20260727.md)
- [`MATH_K13_EXACT_1719_CERTIFICATE_20260728.md`](MATH_K13_EXACT_1719_CERTIFICATE_20260728.md)
- [`MATH_K14_EXACT_3434_CERTIFICATE_20260728.md`](MATH_K14_EXACT_3434_CERTIFICATE_20260728.md)
- [`scratch/`](scratch/) contains the selected compact machine certificates,
  independent verifiers, and reproduction scripts cited by those notes.

## Current `k=15` frontier

The target is `B(15)=6438`.  The best frozen carrier has exact compiler Hall
deficiency 29, so the conjectured optimum is not yet constructed.

- [`K15_CPSAT_BENDERS_EXHAUSTION_20260728.md`](K15_CPSAT_BENDERS_EXHAUSTION_20260728.md)
- [`K15_NATIVE_SEARCH_PORT_AUDIT_20260728.md`](K15_NATIVE_SEARCH_PORT_AUDIT_20260728.md)
- [`K15_RELABEL_INDEX_AUDIT_AGENT_20260728.md`](K15_RELABEL_INDEX_AUDIT_AGENT_20260728.md)
- [`MATH_K15_FIVE_FACE_MINIMAL_PARENT_COVER_DECOMPOSITION_20260728.md`](MATH_K15_FIVE_FACE_MINIMAL_PARENT_COVER_DECOMPOSITION_20260728.md)
- [`MATH_THREEWAY_K15_MINIMAL_MULTIPARENT_EXCHANGE_20260728.md`](MATH_THREEWAY_K15_MINIMAL_MULTIPARENT_EXCHANGE_20260728.md)
- [`MATH_LANE_C_K15_GLOBAL_FIVE_PARENT_MOVING_DM_SEPARATOR_20260728.md`](MATH_LANE_C_K15_GLOBAL_FIVE_PARENT_MOVING_DM_SEPARATOR_20260728.md)

Selected machine evidence includes:

- `scratch/k15_doubletrans_05_213_hall29.json` and its summary;
- `scratch/h29cube_exact_benders8.json`;
- `scratch/k15_exact_pair_nogos_20260728/`;
- the five frozen parent paths;
- compact exact support-3-through-7 transfer audits;
- the native Hall engine and proof-safe global five-parent CP-SAT source.

## Reproducibility boundary

Generated CNFs, temporary solver portfolios, compiled executables, and stale
search outputs are omitted.  This is deliberate: they exceeded 50 GiB and
were not authoritative certificates.  Retained source plus compact inputs can
regenerate them when a historical branch genuinely needs to be replayed.
