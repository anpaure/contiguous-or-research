# Thread D: A29 successor-zeta precomputer and CP-SAT payload

Date: 2026-07-28

> **Superseded indexing notice.**  This first implementation record used the
> wrong synthesized bit swap `(0,11)` while labeling it `tau(1,12)`.  Its
> payload and descendants are quarantined under
> `scratch/threadD_quarantine_wrong_tau_0_11/` and must not be used.  The
> corrected implementation reads `scratch/k15_transposition_parent_winner.json`,
> whose transposition is zero-based `[1,12]` (one-based `(2,13)`).  The
> authoritative replacement is
> `MATH_THREADD_A29_LANEI_EXACT_BENDERS_CORRECTED_20260728.md`.

## Audited outcome

The concrete four-parent catalogue is

1. `scratch/k15_doubletrans_05_213_hall29.json` (H29),
2. `scratch/k15_outer2_p1_h30_bridge.json` (H30),
3. `scratch/k15_terminal_palette_h31_outer1.json` (H31), and
4. the coordinate relabeling `tau(1,12)H29`, with coordinates numbered
   from one (bits 0 and 11 are exchanged).

The union has 6,435 vertices, 18,814 distinct directed arcs, maximum
indegree four, and maximum outdegree four.  A29 is the 1,524-target
Dulmage--Mendelsohn witness in
`scratch/k15_doubletrans_05_213_hall29.dm_witness.json`.

The native precomputer builds the complete `3^15=14,348,907` entry
interval-zeta table, using 28,697,814 bytes.  On H29 it obtained

```text
direct exact neighborhood       1495
successor/local zeta neighborhood 1495
expected DM witness cells       1495
left boundary hits                 0
right boundary hits                0
```

Both computed cell-index lists agree exactly with the authoritative
`witness_cells` array.  Thus all 36 exact A29 boundary indicators are false
on H29.  This is stronger than checking only the scalar 1495 and shows that
the projected `+36` boundary allowance has no literal support for this cut.

The same regression passed locally and on the requested H100 CPU.

## Files

- `scratch/threadD_A29_successor_zeta.cpp`: standalone native precomputer.
- `scratch/threadD_A29_cpsat.py`: exact CP-SAT payload builder.
- `scratch/threadD_A29_4parent_payload.json`: concrete graph, four parent
  orders, A29, and constraint metadata.
- `scratch/threadD_A29_zeta.u16`: native little-endian zeta ROM.
- `scratch/threadD_A29_h29_regression.json`: all 36 boundary bits and the
  exact H29 regression totals.
- `scratch/threadD_A29_cpsat_audit.json`: construction-size audit.

Every new artifact has the requested `threadD_` prefix, except this dated
theorem/implementation note.

## Exact CP-SAT constraint

Let `ord[0],...,ord[6434]` be a permutation of the vertex identifiers.
A single deterministic automaton has a super-source transition to every
first vertex and the transition

```text
state u -- label v --> state v
```

for each of the 18,814 union arcs `u -> v`.  Together with `AllDifferent`,
this is exactly a directed Hamilton chronology in the four-parent union.
There are 25,249 automaton transitions, stored once.

For each chronology position, one element constraint obtains its 15-bit
middle mask.  The model shares the exact global erosion bits

```text
p[i,x] = AND(w[j,x] : max(0,i-3) <= j <= min(i,6434)).
```

It also imposes the literal carrier-existence condition for every middle
occurrence.  All 19,311 compiler cells, including the 36 endpoint cells,
are then treated uniformly.

For a cell `C`, `claim[C]` selects one A29 target `T_C` and implies the
literal conditions

```text
T_C subset E_C,
M_C subset T_C,
T_C intersects p_i for every i in C.
```

The mandatory-carrier implication is encoded without a carrier auxiliary.
For every possible inside carrier position `p`, its clause is

```text
not claim[C] OR T_C[x] OR not p[p,x]
             OR OR(p[q,x] : q is outside C in the same four-position carrier).
```

Finally the model adds

```text
sum_C claim[C] >= 1524.
```

This one-way witness encoding is exactly equivalent to
`|N(A29)| >= 1524`: every claimed cell has a literal fitting target, while
any 1,524 actual neighbor cells can choose such targets and set their claims.
The unused reverse implication `Fit => claim` is unnecessary.  Consequently
there is no 1,524-way target OR and no directed-motif leaf enumeration.

## Construction audit

The payload builder gives the following exact high-level census:

```text
vertices                         6,435
union arcs                      18,814
automaton transitions           25,249
compiler cells                  19,311 = 6438+6437+6436
logical variables            1,132,863
high-level constraints       4,723,795
mandatory-carrier clauses    2,316,450
row-meet auxiliaries           579,300
vertex element constants    41,409,225
target element constants    29,429,964
enumerated motif leaves              0
old full leaves             213,501,726
```

On H100, `PYTHONPATH=/dev/shm/orlib` successfully loaded the supplied
OR-Tools and reproduced this audit.  A full fixed-H29 model construction
reached the post-construction reporting line; it then encountered an OR-Tools
wrapper difference (`CpModelProto.ByteSize` is absent) before solving.  The
local builder now uses `CpModel.ExportToFile` instead.  Per instruction, no
second build/solve was started.  Thus the native regression and construction
audit are complete, while no CP-SAT feasibility result is claimed.

## Reproduction

Native:

```bash
c++ -O3 -march=native -std=c++20 \
  -o scratch/threadD_A29_successor_zeta \
  scratch/threadD_A29_successor_zeta.cpp

scratch/threadD_A29_successor_zeta \
  --h29 scratch/k15_doubletrans_05_213_hall29.json \
  --h30 scratch/k15_outer2_p1_h30_bridge.json \
  --h31 scratch/k15_terminal_palette_h31_outer1.json \
  --witness scratch/k15_doubletrans_05_213_hall29.dm_witness.json \
  --payload scratch/threadD_A29_4parent_payload.json \
  --zeta scratch/threadD_A29_zeta.u16 \
  --report scratch/threadD_A29_h29_regression.json
```

H100 construction audit:

```bash
PYTHONPATH=/dev/shm/orlib python3 scratch/threadD_A29_cpsat.py \
  scratch/threadD_A29_4parent_payload.json \
  --audit-out scratch/threadD_A29_cpsat_audit.json
```

The optional `--build-model` flag constructs the exact model.  `--fix-parent
H29 --threshold 1524` is the intended negative fixed-path regression; it was
not rerun after the reporting compatibility fix.
