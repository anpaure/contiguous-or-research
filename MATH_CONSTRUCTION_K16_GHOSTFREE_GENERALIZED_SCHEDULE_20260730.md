# K16 ghost-free generalized middle schedule (2026-07-30)

## Scope

This note records a solver-free construction and audit at the conjectured
optimal length

\[
L=B(16)=12873.
\]

It does **not** yet give a universal word.  It gives an exact generalized
middle-delivery schedule with no repeated middle target (the former
``ghost''), together with a legal six-hole realization.  The remaining gate
is a finite compiler problem inside the schedule envelopes.

## Construction

Start from the verified universal word
`answers/k16_upper12874.word`.  Its first-middle delivery ledger has one
repeated target, `0xc279`, delivered at starts 11729 and 12829.

Delete physical cell/start position 12827 (zero-based), thereby deleting the
second delivery of `0xc279`.  Transport every surviving delivery interval
through this deletion and extend the transported deadlines of original
starts 12825 and 12826 by one position.

The resulting length-12873 schedule has:

- all 12870 rank-8 targets exactly once;
- three additional same-deadline flat deliveries, `0x4e71`, `0xcc63`, and
  `0xce61`;
- no repeated middle target, no stall, and no jump;
- all consecutive scheduled-target unions except exactly
  `0xc679`, `0xca79`, `0xea79`, and `0xeb79`.

For each physical position `j`, define its generalized envelope by

\[
P_j=\bigcap\{T:(s,e,T)\text{ is a scheduled row and }s\le j\le e\}.
\]

The envelope-rank census is

| rank | cells |
|---:|---:|
| 5 | 6434 |
| 6 | 6434 |
| 7 | 3 |
| 8 | 2 |

and the total envelope bit mass is 70811.

## Six-hole legal realization

Delete position 12827 from the 12874-word, then (in the new indexing) clear
bit `0x10` at position 12827 and bit `0x08` at position 12828.

Every cell is a nonempty submask of its envelope and every scheduled middle
OR is realized.  Exhaustive literal replay leaves exactly six holes:

| mask | decimal | rank |
|---:|---:|---:|
| `0x8231` | 33329 | 5 |
| `0xc219` | 49689 | 6 |
| `0xc679` | 50809 | 9 |
| `0xca79` | 51833 | 9 |
| `0xea79` | 60025 | 10 |
| `0xeb79` | 60281 | 11 |

Thus the repeated-middle wrinkle is not intrinsic: at the exact conjectured
length there is a ghost-free schedule, and its current literal defect is six
targets.

## Reproducible artifacts

- `scratch/audit_k16_ghostfree_p12827_schedule_20260730.py`
  - SHA-256 `b5752cb953d37657f87c6760476451c76a07430b685d51b7ab81a949b807fbfb`
- `scratch/k16_ghostfree_p12827_schedule_20260730.audit.json`
  - SHA-256 `cefa500933ddcc67c1ee553265164127598d39217d433ca59638e3c1762a14ee`
  - payload SHA-256 `e6d8b80b71ee85009d291f607649a7451b7c2f676eefe1c7ee5cdd5c43661c3f`
- `scratch/k16_ghostfree_p12827_schedule_seed6.word`
  - SHA-256 `1a01b1c8afed2807e5eb763d281ce0863a581e395a869975bedab57623702153`
- `scratch/solve_k16_ghostfree_p12827_collar_cpsat_20260730.py`
  - SHA-256 `7fdab2c7758aa76e84a190b17e9d06d6bcce26cc149ac6e615c45eb9e2f9f99f`

The audit script reconstructs the schedule from the 12874-word, verifies the
envelope system, constructs the six-hole realization, and independently
enumerates all interval ORs.

## Exact suffix-46 compiler: refuted

The compiler freezes positions `[0,12827)` of the six-hole realization.  Its
46-cell suffix is allowed to range over arbitrary nonempty submasks of the
exact generalized envelopes.  It imposes:

1. every affected scheduled middle OR; and
2. every target with no occurrence wholly inside the frozen prefix.

This model is infeasible.  CP-SAT found the contradiction in presolve, and an
assumption-guarded replay reduced the core to the single target `0xc219`.

The no-go also has a solver-free audit.  Under the exact envelopes there are
741 physically distinct suffix-crossing intervals which could supply all bits
of `0xc219`.  Every one suppresses a mandatory outside-`0xc219` bit whose only
available host in an affected schedule row lies inside that candidate
interval.  There are 28 distinct primary blocking schedule requirements.

Artifacts:

- `scratch/k16_ghostfree_p12827_collar_20260730.result.json`
  - SHA-256 `5acaa9805f0042ba0fea81c4ff1ad458c835216bbcf3da615dd46f82617a859e`
- `scratch/audit_k16_ghostfree_suffix46_xc219_blockers_20260730.py`
  - SHA-256 `0b0d4aed2d0d7d1085965fee6d2670645470e4f6d1a2717ff0bae51774aa4ad9`
- `scratch/k16_ghostfree_suffix46_xc219_blockers_20260730.audit.json`
  - SHA-256 `71a20c6fc07d3dd3809e3f4dc4caa8eaad6bf1950138490f6e151d800ea2836a`
  - payload SHA-256 `08f5ee3bb4da3f60ca8a52a466a6541f7ad521fa45ecbd3adf9975b774650191`

The obstruction is therefore not to the ghost-free schedule itself.  It says
only that its final 46 cells cannot repair the lower hole `0xc219` while the
entire prefix is frozen.  The exact singleton envelope providers for this
target occur globally at positions 7200 and 12592, so the next compiler must
use nonterminal support.

## Stronger global envelope no-go

The four upper masks are, however, intrinsic to this exact schedule.  Even if
all 12873 cells are allowed to vary over arbitrary nonempty submasks of their
generalized envelopes, no interval can realize any of

`0xc679`, `0xca79`, `0xea79`, `0xeb79`

while retaining every scheduled middle OR.

For a fixed target `U` and start `s`, take the earliest endpoint `e` at which
the allowed contributions `P_i & U` can union to `U`.  If `[s,e]` suppresses
the last possible host of a scheduled bit outside `U`, every longer interval
from `s` remains blocked.  Exhausting these earliest endpoints gives:

| target | compatible starts | schedule-feasible starts |
|---:|---:|---:|
| `0xc679` | 6446 | 0 |
| `0xca79` | 6447 | 0 |
| `0xea79` | 6447 | 0 |
| `0xeb79` | 8780 | 0 |

Artifacts:

- `scratch/audit_k16_ghostfree_schedule_forced_upper_nogo_20260730.py`
  - SHA-256 `a8179978f8dff78423a6f429971673a4a94799da7af939fe8d0430f154b785a0`
- `scratch/k16_ghostfree_schedule_forced_upper_nogo_20260730.audit.json`
  - SHA-256 `ad51e658059be6af7d3b4b7b9a34488b843fbe7bcfd7f6cf08b50b0e47aadb9b`
  - payload SHA-256 `031e32fa7eee68b7b8f96c56c37db0cc43f8860335a720d476b4bc1a8945b4c2`

Consequently, the next move is schedule-level rethreading: changing the
deleted ghost copy and/or the neighboring deadlines.  No envelope compiler,
global or local, can finish this particular schedule.

## Structural consequence

The old 12874 witness paid four excess delivery units: three legitimate
same-deadline flats and one repeated middle target.  This construction removes
the repeated target while retaining the three flats.  Hence the proposed
`2^(d-1)` waste law is not forced by the middle-delivery arithmetic at `d=3`;
the lower-bound budget of three is schedule-feasible.  What remains is literal
short/upper-target compatibility, not a forced fourth middle unit.
