# Independent audit of the named-cell family encoding

> **Superseded/retracted B/C width-row verdict (2026-07-23).**  The old
> source substituted the chain-A formula for `y0` on all three chains.  Its
> chain-B/C named-cell comparisons omitted the internal width-zero blocks
> `22`/`11`.  The target theorem and length caps survive, but the old
> production projection was incomplete.  Corrected rows and an independent
> source audit are recorded in `K11_RANK5_SINGLETON_BOUNDARY_REPAIR.md` and
> `K11_RANK5_SINGLETON_BOUNDARY_REPAIR_IMPLEMENTATION_AUDIT.md`.

## Verdict

**PASS.**  The guarded selected-witness caps are sound and projection-exact
in every audited Type-I/Type-II filtration subcase.  The exact Type-II
duplicate flag and all three selected-width comparisons are also correct.

## 1. Family localization

For Type I, every rank-at-most-four target has a suffix witness of length at
most two.  The direct and generic witness variables are existential and can
select that witness WLOG.  `Inside(0)=false` and the distance-two clauses
encode precisely this restriction.  Crossed shadow candidates already have
physical length at most two; a candidate touching the literal rank-six
entry cannot have the exact lower target value.

For Type II, the three exact cases are `(delta,s)=(0,1),(1,1),(0,2)`.
Only `(0,1)` has slack three.  The other cases receive the conditional
length-two cap.  In `(0,2)`, the existing exact slack-one-pair clauses force
every internal pair of that component to be a selected rank-five witness,
so an exact rank-at-most-four pair is necessarily in the slack-two component.
Literal rank-five separators prohibit crossing pairs.  This recovers the
full named family, rather than only its cardinality inequality.

## 2. Duplicate flag

The compared counters are full-width exact sums.  Their equality means

```text
n5-y0+s=2.
```

Among the three valid cases this is true for `(1,1)` and `(0,2)`.
Conjoining equality with `not two_components` therefore identifies exactly
`(1,1)`.  The bit-equality CNF, global conjunction, and final AND-NOT gate
are all bidirectional.  The extension costs exactly 13 variables and 59
clauses and is absent when the named-cell guard is off.

## 3. Width rows

For chain A, `y2=(h3-h2)+(h5-h4)`; for B, `y2=h3-h2`; for C,
`y2=h5-h4`.  Substituting `z=y0=h1+462-h6` gives exactly the three encoded
comparisons.  Type I uses the chain selector as guard.  Type II uses exact
conjunctions `(duplicate AND chain)` at offset 96 and
`(two_components AND chain)` at offset 95.  Inactive guarded arithmetic
cannot impose a comparison.

## 4. Verification

The finite checker `scratch/check_k11_named_cell_family.py` independently
exhausts all Boolean subcase gates, short interval caps, and small analogue
boundary schedules.  It reproduces the exact incremental inventories:

```text
Type I   241 variables   37,851 clauses
Type II  489 variables   39,453 clauses
```

Both production branches compile cleanly and reproduce the build-only
fingerprints recorded in `K11_NAMED_CELL_FAMILY_ENCODING.md`.

This audit certifies the reduction and its implementation, not SAT or UNSAT
of the underlying `k=11,n=465` instance.
