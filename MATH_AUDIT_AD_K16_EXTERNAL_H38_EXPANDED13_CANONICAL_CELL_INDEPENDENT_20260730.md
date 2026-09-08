# Independent audit: K16 external-H38 expanded13 canonical-cell strengthening

Date: 2026-07-30  
Lane: AD independent audit  
Status: **PASS; solver-free; no SAT/UNSAT claim**

## 1. Verdict and exact scope

The 208-row canonical-cell derivative of the frozen expanded13 model is an
exact equisatisfiable strengthening **for this `budget=-1` instance**.  An
independent implementation reproduced:

1. the 94 physical repair targets and all 1,956 interval terms from the word
   and 13 editable positions;
2. all 37,093 parent clauses, in exact normalized emitter order;
3. all 208 appended clauses, in exact order;
4. the 2,177-variable, 37,301-clause, 105,688-literal output; and
5. the output SHA-256
   `7ef805b9b6665e2c87bed3e18bb573ece33dc07f64e40716f2dd8c09fa85e294`.

The old 216-family conflict catalogue does not transfer verbatim.  It is the
minimal empty-intersection catalogue of a different 57-target occupancy
projection.  The expanded13 instance has 94 targets and explicit cell bits;
its exact transferable normalization is the 208 reverse cell-bit rows.

No solver was run.  This audit proves only encoding correctness and
equisatisfiability, not feasibility, infeasibility, or a new bound on
`nu(16)`.

## 2. Frozen provenance

The audited bundle is

```text
scratch/ad_k16_external_h38_expanded13_blocker_strengthening_20260730/
```

with:

| object | SHA-256 |
|---|---|
| `model.cnf` | `73a426dcb8586ef70dc23902d52caad628a3b63190e411b24f53b144ded8b715` |
| `model.map` | `6afae83ab5e574a5b975cf4b9a64494dadf29afdf53f7965ab1d7f906be2a6c3` |
| `model.canonical.cnf` | `7ef805b9b6665e2c87bed3e18bb573ece33dc07f64e40716f2dd8c09fa85e294` |
| source word | `575f9e5b3453618636918cb410cff88390e12c2dd09fc4d635820b40e1bd4880` |
| positions | `6298916f9ed2f5415f7f4ec72db90cb996b8fe18efc473c959821a17a7e7624c` |
| C++ emitter | `5d40fc37e1b1caea5992049887204a8224589b48f91ab7b5c6d7531efdc503a1` |
| strengthener | `b7ac8c8f315c54f1294c56a67d68df0156b5cacc52d83f4abb0f63d53a181927` |

The editable zero-based positions are exactly

```text
110,111,112,666,667,670,4299,4301,6522,6523,6524,6526,9958.
```

The map metadata is exactly `bits=16`, `length=12873`, `budget=-1`,
`editable_count=13`, `index_base=0`.

## 3. Independent physical and parent replay

The audit did not trust the target or witness counts in the map.  Starting
from the frozen word and positions, it independently:

* split the word into the 14 fixed runs and marked every OR realized wholly
  inside a fixed run;
* recovered 65,441 fixed-only targets and therefore the complementary 94
  repair targets;
* recomputed the distinct fixed suffix/prefix ORs around each editable block;
* recovered 481 changed-interval bases, with maximum 40 for one block;
* applied the exact minimal-residual-need reduction and recovered all 1,956
  witness terms, with maximum 23 for one target; and
* matched every target and every ordered `(first,last,need)` term against the
  frozen map.

It then rebuilt the parent clauses independently from the map:

* 13 cell-nonzero clauses;
* the complete equivalence between each change variable and deviation of its
  16-bit cell from the incumbent;
* every witness forbidden-bit implication;
* every witness residual-need clause; and
* every target at-least-one-witness clause.

The rebuilt sequence equals the parsed parent sequence clause for clause:

```text
variables  2177
clauses   37093
literals  82744
```

This also establishes a fact used in the normalization proof: with
`budget=-1`, change variables occur only in their local equivalence rows.
There is no cardinality counter or other consumer of a change variable.

## 4. Equisatisfiability theorem

For cell `i` and coordinate `q`, let `x[i,q]` be the cell bit.  For a witness
`w=(T,[a,b],need)`, write `w through i` when `a <= i <= b`.  The appended row
is

```text
x[i,q] OR OR{ w : w is through i and q is not in T }.
```

### Theorem 4.1

Adding these 13 times 16 rows preserves satisfiability of the frozen
expanded13 parent.

### Proof

Take any parent model and keep every witness value fixed.  For each editable
cell define

```text
X'_i = intersection{ T : some true T-witness is through i },
```

using the full 16-coordinate set when the family is empty.

Every true witness already implies `X_i` is a subset of its target.  Hence
`X_i` is a subset of `X'_i`; this transformation only adds bits.  In
particular, the parent cell-nonzero clause remains true.

Fix a true witness `w=(T,[a,b],need)`.  For every `i` in its interval, `T`
is one of the sets intersected in the definition of `X'_i`; thus
`X'_i` is a subset of `T`.  No forbidden bit is introduced.  Every residual
need bit that was supplied by an old cell remains supplied because each cell
only expanded.  Therefore every old true witness remains a valid literal
interval witness, and every target at-least-one row remains satisfied.

For each `(i,q)`, either `q` lies in `X'_i`, making the cell-bit literal true,
or some true through-witness target omits `q`, making the right side of the
new row true.  Thus all 208 rows hold.

Reset each change variable to the truth of `X'_i != incumbent_i`.  The local
change equivalences then hold.  Because the budget is `-1`, there is no
change-cardinality row to disturb.  Finally, each of the other 65,441 targets
has an interval wholly within a fixed run, so this normalization cannot erase
its witness.

This maps every parent model to a strengthened model.  The converse follows
because the strengthened formula contains all parent clauses.  Hence the two
formulas are equisatisfiable.  QED.

The proof is not valid for a prescribed finite edit count: cell expansion can
change which cells differ from their incumbents.

## 5. Exact appended-row replay

For every `(i,q)`, the audit scanned all mapped witnesses and independently
formed the right side from precisely those terms whose interval contains `i`
and whose target omits `q`.  Every right side is nonempty.  The exact totals
are:

```text
rows                         208
right-side witness incidences 22736
minimum right-side size        22
maximum right-side size       302
```

All 208 rows are distinct and non-tautological.  The derivative CNF consists
of the exact 37,093-clause parent prefix followed by this exact 208-clause
suffix.

## 6. Why the 216-family does not transfer

The number 216 is not a dimension-only constant.  It decomposes as 18
minimal pairs, 46 minimal triples, and 152 minimal quadruples for the
specific 57-target profile family.  Expanded13 has a different 94-target
family.  Its independently reproduced low-order intersection census is

```text
15 disjoint target pairs
5741 inclusion-minimal empty target triples.
```

Thus copying the old target-labelled clauses would be semantically wrong.
Generating all new minimal conflicts would also miss the compact structure
already present: if true witness terms through one cell have empty target
intersection, their forbidden-bit implications contradict that cell's
nonzero clause.  Therefore every-order empty-intersection conflict is already
encoded through the 16 explicit cell bits.

What transfers is the canonical reverse direction.  The 208 rows make each
cell bit equal, after normalization, to membership in the intersection of
its true through-witness targets.  They are equisatisfiable strengthening
rows, not formula-level implicates in the original `(x,w)` variable space.

## 7. Payload replay

The claimed audit file itself has SHA-256

```text
33d18cd67612eff8f3c2ad409fa9c31b0baf43833c600d59717479574aa278d3
```

and records payload

```text
982ddb7e9ea5d4186c6818c13c73f31abb8f090208abf80c73dd564fc43b9516.
```

Removing the `payload_sha256` field from the parsed JSON and applying the
documented sorted-key compact serialization reproduces that payload exactly.
The histogram keys are serialized as strings before hashing, so the current
audit is round-trip stable.

## 8. Independent artifacts

```text
scratch/audit_ad_k16_external_h38_expanded13_canonical_cells_independent_20260730.py
SHA-256 acd8630d6f04f3a225bf94d79fc729b015dce930681e62dff6754cf711497dfd

scratch/ad_k16_external_h38_expanded13_blocker_strengthening_20260730/
  model.canonical.independent_audit.json
SHA-256 1f75b0ebb1a7a73220cdc05bae05ff7c2059fca22112789cf91d105002d97e8f
payload SHA-256 d71a9c086f1bb867fbf02072a7a9d794b35fa0b4ba0442755b788d4fdbc45807
```
