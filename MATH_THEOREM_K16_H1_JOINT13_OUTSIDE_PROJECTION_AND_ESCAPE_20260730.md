# K16 H1 joint13: exact outside-edit projection and escape theorem

Date: 2026-07-30  
Status: **proved normalization theorem with a sharp scope boundary**

## 1. Frozen instance

Let `x` be the authenticated length-12,873 H1 word

```text
scratch/k16_h2_to_h1_p0.h1.word
SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a
```

whose sole hole is

```text
H = 0x2c6d.
```

Put

```text
S = {0,1,4486,4487,4488,4489,6438,6439,6440,
     12869,12870,12871,12872}.
```

The four consecutive blocks of `S` have widths `2,4,3,4`.  For an arbitrary
nonzero-mask word `y` of the same length define its source-reset projection

```text
pi_S(y)[i] = y[i]  if i is in S,
             x[i]  otherwise.
```

This projection changes neither length nor order.  It may change arbitrarily
many values and is not change-count preserving.

## 2. Exact projection criterion

Let `R=R_S(x)` be the set of targets having no `x`-witness interval disjoint
from `S`.  Exact independent interval-OR enumeration gives

```text
|R| = 55,
```

with exactly the residual list in the frozen joint13 geometry.  Every one of
the other 65,480 nonzero masks has a literal `x`-witness contained in one of

```text
[2,4485], [4490,6437], [6441,12868].
```

### Theorem 2.1 (source-reset projection)

For every word `y`, the following are equivalent.

1. `pi_S(y)` is universal.
2. `pi_S(y)` covers every target in `R`.
3. For every `T in R` there is an interval `I` such that

   ```text
   OR(y[i] : i in I intersect S)
       OR OR(x[i] : i in I minus S) = T.               (2.1)
   ```

Consequently, for a universal `y`, all outside-support edits can be erased
simultaneously without losing universality **if and only if** the 55 hybrid
conditions (2.1) hold.

#### Proof

Conditions 2 and 3 are the definition of interval coverage in `pi_S(y)`.
Condition 1 implies 2.  Conversely, every `T` outside `R` has a fixed source
witness disjoint from `S`; `pi_S(y)` agrees with `x` throughout that witness.
Thus those 65,480 targets are automatic, while condition 2 supplies the
remaining 55.  This proves all equivalences.

## 3. Identification with the frozen joint13 fibre

The ORs of the three complete fixed gaps are

```text
[2,4485]     : 0x7fff, whose supersets are 0x7fff and 0xffff;
[4490,6437]  : 0xffff;
[6441,12868] : 0xffff.
```

None of these possible crossing targets belongs to `R`, and `0x7fff` and
`0xffff` have fixed-only witnesses.  Hence a witness of a residual target in
`pi_S(y)` cannot meet two editable blocks.  It cannot avoid `S`, by the
definition of `R`.  It therefore meets exactly one block, and its trace on
that block is a nonempty consecutive interval.  The number of possible
traces per target is exactly

```text
2*3/2 + 4*5/2 + 3*4/2 + 4*5/2 = 29.
```

The already independently audited fixed prefix/suffix bases turn these
traces into exactly the 29 joint13 charts.  Therefore condition 2 of Theorem
2.1 is precisely feasibility of the frozen arbitrary-value joint13 fibre,
not a relaxation.

This gives the promised lifting rule:

> Any exact obstruction to the joint13 fibre automatically excludes every
> universal same-length word whose source-reset projection satisfies (2.1),
> even if that word has arbitrarily many, arbitrarily valued edits outside
> `S`.

No outside-support solver run is needed for this implication.

## 4. A checkable wider class and the escape alternative

For a word `y`, let

```text
E = {i outside S : y[i] != x[i]}.
```

### Corollary 4.1 (residual-witness-separated normalization)

Suppose `y` is universal and, for every `T in R`, some `y`-witness interval
for `T` avoids all of `E`.  Then `pi_S(y)` is universal.

Indeed, on an `E`-avoiding interval, `y` and `pi_S(y)` agree at every cell:
they agree by definition on `S`, and an outside cell not in `E` still has its
source value.  The selected 55 witnesses survive, so Theorem 2.1 applies.

The companion solver-independent guard-ladder theorem now authenticates that
full joint13 obstruction.  Hence any universal word outside that fibre must
satisfy the following exact escape alternative:

```text
there exists T in R such that every y-witness for T meets E.       (4.1)
```

In other words, the outside edits must be a collective transversal of the
entire witness-interval family of at least one residual target.  This is a
strict extension beyond fixed support: `E` may have any size and occur at any
positions.  The theorem only demands that no residual target depend
collectively on it.

Condition (4.1) is necessary to escape a joint13 obstruction, not sufficient
for a universal word.  It also does not bound the size of `E` without an
additional interval-piercing argument for the particular final word.

## 5. Why the obvious stronger normalization fails

There is no nonempty position-only region outside `S` that is uniformly
erasable merely because it lies in a source safe gap.  Since `x` misses `H`,
no source cell equals `H`.  For any outside position `p`, changing only
`x[p]` to `H` creates the singleton witness `[p,p]`; every `H`-witness in the
new word must meet `p`, because a witness avoiding `p` would already have
been an `x`-witness.  Resetting `p` therefore removes all `H`-witnesses.

Individual redundancy is not compositional either.  At the concrete outside
positions `p=2,q=3`, whose source values are `0x0045,0x0424`, set both values
to `H`.  Resetting either one alone retains the other singleton `H`-witness,
whereas resetting both returns `x` and loses `H`.  The audit replays the four
words exactly.  This example is not universal and is used only to refute a
coordinatewise witness-erasure rule.

The safe-gap OR argument localizes witnesses only **after** the complement is
reset.  It does not make arbitrary changes inside a gap semantically inert.
Likewise, target-intersection normalization changes values on a fixed chart
incidence pattern; it does not relocate an outside witness into `S`.
Arbitrary value transfer or relocation remains unproved.

## 6. Independent audit and scope

The solver-free audit reconstructs all source interval ORs and all interval
ORs contained in the three fixed-complement segments by an endpoint DP with
at most 17 distinct OR states per endpoint.  It directly replays every
retained witness, independently recovers the sole source hole, the 65,480/55
fixed/residual partition, all three gap ORs and crossing palettes, and the
29-trace count.  It also replays the coordinatewise counterexample.

```text
scratch/audit_k16_h1_joint13_outside_projection_normalization_20260730.py

scratch/k16_h1_joint13_outside_projection_normalization_20260730.audit.json
```

This theorem supplies the projection/escape transfer, while
`MATH_THEOREM_K16_H1_JOINT13_RQC_GUARD_LADDER_UNSAT_20260730.md` supplies the
support-restricted obstruction.  It does not normalize a word satisfying the
escape alternative (4.1), and the pair gives no unrestricted length-12,873 or
K16 no-go.  The global bracket remains

```text
12873 <= nu(16) <= 12874.
```
