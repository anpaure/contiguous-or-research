# K16 S4 specialized provider-domain search (2026-07-30)

**Final disposition:** the whole frozen S4 fibre is impossible by the later
solver-free fixed-deadline theorem.  The specialized searches below remain
useful explanations of the local provider geometry, but all unrestricted S4
enumeration has been retired.

## Frozen input

The search uses only the self-contained atlas
`scratch/k16_triwindow_s4_495_lead_20260730/frozen_atlas/`:

- 18 free cells in independent windows of lengths `4,9,5`;
- 69 residual targets not already covered by the fixed body;
- 5,867 complete semantic interval-provider rows;
- incumbent holes `0x31ce` and `0x7bce`, with
  `0x31ce subset 0x7bce`;
- the three scarce lower facets `0x4c71,0x4879,0x4c39` have fixed-body
  witnesses and therefore cannot be destroyed by any collar assignment.

The atlas's independent interval replay reports zero omitted and zero extra
semantic providers.

## Maximal-domain lemma

Choose one semantic provider `P_t` for every residual target `t`.  Write
`Q(P_t)` for its participating free cells and `F(P_t)` for the OR of its fixed
cells.  Define

```
D_c = intersection { t : c in Q(P_t) },
```

using `0xffff` when no selected provider contains `c`.

The selected provider system is realizable by nonzero collar cells if and
only if:

1. every `D_c` is nonzero; and
2. for every selected provider,

```
F(P_t) OR OR_{c in Q(P_t)} D_c = t.
```

Necessity follows because every realizing cell value is a nonzero subset of
`D_c`.  For sufficiency, assign cell `c` the maximal value `D_c` itself.

An even stronger monotone search follows.  It is unnecessary to remember the
selected providers.  Maintain only the 18 maximal domains.  If a target is
currently uncovered, branch over one of its providers and intersect every
participating editable domain with that target.  A valid completion must make
one such branch, while a branch that does not realize its own provider can be
discarded.  Domains only shrink, so memoizing the 18-mask vector gives an
exact finite branch-and-bound search with no Boolean cell variables and no
generic SAT solver.

Implementation:
`scratch/search_k16_s4_nested_provider_exact_20260730.cpp`.

Every reported score-zero assignment is assembled into the full length-12873
word and independently replayed inside the program against all 65,535 nonzero
masks before it can be written.

## Exact first-level no-go results

### Positional-qset-nested pairs

All 774 compatible pairs in which the `0x31ce` provider's free-cell set is a
subset of the `0x7bce` provider's free-cell set were checked.  If editable
cells are confined to the union of those two provider intervals, every case
is impossible.  The specialized search visited 1,844 distinct maximal-domain
states.

### Every compatible pair

Removing positional nesting gives the frozen atlas's 5,692 compatible raw
provider pairs.  Exact cap-state deduplication leaves 3,540 distinct roots.
Again, when editable cells are confined to the union of the two provider
intervals, every root is impossible.  The specialized search visited 6,204
maximal-domain states.

Thus a valid S4 completion, if one exists, requires at least one genuinely
external compensating cell.  This is a local support theorem only: it does
not rule out one or more compensator runs, two-window compensation, or the
unrestricted 18-cell collar.

## Retired stronger searches

The same exact engine began checking:

1. pair union plus one inclusion-maximal disjoint compensator interval;
2. the complete physical window(s) containing the provider pair;
3. subsequently, two-window and unrestricted 18-cell support.

The bounded pair-plus-one and physical-window runs ended `UNKNOWN`; no claim
was drawn from their timeouts.  The unrestricted and size-seven runs were
stopped once the fixed-deadline theorem closed the complete eighteen-cell
fibre.  No remote process from this lane remains active.

## Pair collateral and the five-rehost floor

`scratch/analyze_k16_s4_nested_pair_minimal_collateral_20260730.py` computes
the exact minimum-Hamming assignment for each of the 774 nested pairs.  Once
all allowed incumbent 1-bits are retained, the remaining optimization is an
exact set cover: an added `(cell,bit)` literal can satisfy its cell's nonzero
clause and at most the two selected-provider bit clauses.  The catalogue is

```
scratch/k16_s4_specialized_provider_domain_20260730/
  nested_pair_minimal_collateral.tsv
  nested_pair_minimal_collateral.audit.json
```

The best canonical pair is `(small_shape,large_shape)=(67,68)`.  Its exact
minimum uses nine bit flips on tail cells 16 and 17 and leaves only four
collateral holes:

```
0x3cc8, 0x3ce8, 0xb6a8, 0xb6ac.
```

Every canonical nested-pair assignment leaves at least four residual holes;
the next collateral level is six.  For pair 67/68, all 26,707 distinct unions
of one external provider support for each of the four debts were generated.
Every support using at most six external physical cells is impossible:
the size-at-most-four strata contribute 2,516 supports and 150,379
maximal-domain states, while the size-five stratum contributes 3,311 supports
and 1,550,392 states, and the size-six stratum contributes 4,374 supports and
16,643,405 states.  Thus 10,201 canonical support unions are closed; size
seven is the first live stratum.  This is a
provider-support statement, not a claim that six cell *values* must change:
an exact provider interval may contain an incumbent-valued physical cell.

This agrees in scale with, but is logically separate from, the exact sharp
pair theorem in
`MATH_AUDIT_K16_S4_SHARP_PAIR_FIVE_REHOST_FLOOR_20260730.md`.  For the nine
sharp pairs `{36,68,69} x {2,3,133}`, exhaustive optimization over all 216
incumbent-Q choices proves that their three immediately displaced rows force
two further rehosts, uniquely `{0x31cc,0x33cc}`.  Hence those nine pairs have
a five-nonincumbent-rehost floor.  The sharpened v2 audit additionally proves
that the exact five-rehost fibre is empty when every other target retains
incumbent provenance: all 24 valid shape-36 base states leave four relaxed
rows individually unhostable, while all 36 shape-68/69 base states leave all
five unhostable.  A sharp-pair completion therefore needs a sixth protected
rehost or a more global abandonment of incumbent provenance.  The frozen audit is
`scratch/k16_s4_sharp_pair_five_rehost_floor_20260730.audit.json` (SHA-256
`85deda18dbd83f6be1662e75181152504c99a689952535ae24d3fe84f879255c`).

## Complete frozen-fibre no-go

The two fixed bodies contain two first rank-eight deliveries of `0xbcc2` at
distinct deadlines:

```text
[6481,6483] -> 0xbcc2, deadline 6483;
[7581,7583] -> 0xbcc2, deadline 7583.
```

Both intervals are wholly fixed.  Therefore this duplicate survives every
assignment of arbitrary nonzero values to all eighteen collar cells.  The
architecture-free deadline inequality

```text
Lambda <= (e-G)(L+G)
```

at `L=12873,e=3,Lambda=26332` is already contradicted by `G=1`, because the
right side is `25748`.  Hence no universal word exists anywhere in this
frozen seed-4/self `4/9/5` fibre.

A second independent checker reads only the physical fixed layout, enumerates
all fixed first-middle deliveries, and reconstructs the duplicate without
reading the parent word, provider atlas, or Lane-R reproducer:

```text
scratch/audit_k16_s4_fixed_deadline_duplicate_independent_20260730.py
scratch/k16_triwindow_s4_495_lead_20260730/frozen_atlas/
  fixed_deadline_duplicate.second_independent.audit.json
```

The conclusion is scoped to this frozen seed-4 layout.  It does not decide a
repeat-free parent opening or `nu(16)` globally.
