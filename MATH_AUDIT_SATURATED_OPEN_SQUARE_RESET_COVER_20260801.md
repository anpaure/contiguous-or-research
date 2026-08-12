# Audit of the saturated open-square reset cover

Date: 2026-08-01

Audited theorem:
`MATH_THEOREM_SATURATED_OPEN_SQUARE_RESET_COVER_20260801.md`.

Verdict: **GO as a conditional reset-host theorem**.  The combinatorial
coordinate-cover and square-supply conclusions are unconditional.  The
bounded dead-block hypothesis is not proved and must not be reported as a
Boolean construction or as `nu(k)<=B(k)+O(1)`.

## 1. Source-parameter replay

The Chapter-9 source uses

\[
 q=\lceil2H\log H\rceil,
 \qquad s_0=q(q+1)+1,
\]

and produces maps `f_0,g_0:[H]^{s_0}->[H]^{s_0}` with one of the two
coordinate equalities for every word pair.  The theorem copies these maps
on `R=b+1` disjoint coordinate blocks.  Applying the source lemma inside
each block gives `R` distinct raw witness coordinates.  Therefore `b`
dead blocks leave at least one live block.  No independence or probability
claim is used in this step.

The proof remains valid if both equalities hold at one coordinate: either
orientation may be selected.  It also remains valid when a block contains
many raw witnesses: liveness means at least one has an eligible literal
menu.

## 2. Bundling audit

The alphabet is the product of the attachment, two predecessor, phase and
guard states.  Hence one invocation of the coordinate cover chooses one
coordinate and one sign for the entire three-return state.

If the product bundling is removed and the cover is invoked separately on
the three return types, the conclusion is invalid: the three invocations
may choose different blocks, coordinates, and signs.  The theorem does not
make that inference.

## 3. Open-square replay

For

\[
 E=L+x,quad F=L+y,quad U=L+x+y,quad
 E'=L-p+x+z,quad F'=L-p+y+z,
\]

the forward path is `E,E',F',F` and the reverse path is
`F,F',E',E`.  Their three intersections are

\[
 L-p+x,quad L-p+z,quad L-p+y,
\]

and their three unions are

\[
 L+x+z,quad L-p+x+y+z,quad L+y+z.
\]

Thus both orientations use the same simple immediate palettes.  The
head--owner projection is one alternating `E`--`F` path, and the
tail--head projection is the two crossed parity paths.  This matches the
opened-reset signature in the cited support-four square theorem.

The direct seam resources `L,U` are omitted in both phases.  Therefore the
square shares the seam internally rather than attempting to clone three
private direct returns.

## 4. Candidate-count replay

There are `a=|L|=r-1` choices of `p` and
`c=k-r-1` choices of `z`, giving exactly `ac` cores.

For a fixed typed lower resource:

* the `L-p+x` or `L-p+y` families determine `p`, leaving `c` choices;
* the `L-p+z` family determines both `p,z`.

For a fixed typed owner resource:

* the `L+x+z` or `L+y+z` families determine `z`, leaving `a` choices;
* the `L-p+x+y+z` family determines both `p,z`.

The membership patterns in `x,y` make these displayed families disjoint.
The internal roots determine `(p,z)` and their `x/y` patterns separate the
two root families.  Hence one nonseam typed forbidden unit kills at most
`max(a,c)` cores.  A union bound gives the stated
`ac-|B|max(a,c)` supply.

This is a prospective alternative count.  It does not say all alternatives
can be embedded simultaneously in a fixed owner factor.

## 5. Guard nonimplications

The theorem correctly keeps the following outside the raw coordinate
equality.

1. Internal q1 simplicity does not prevent collision with an incumbent
   exterior occurrence.
2. Equality of immediate owner palettes does not preserve wider interval
   unions crossing the module.
3. A three-edge square read consecutively can violate the depth residence
   floor; an occurrence lift or resident collar is additional data.
4. Abstractly private return labels do not imply compiler safety.  The
   sharp `U_(2,3)` deletion obstruction survives.
5. Separate phasewise Rado certificates do not imply one common residual
   minor; the three-label Borromean obstruction survives.
6. Abstract palette labels require a literal palette-realization map.

Therefore the eligible-menu definition is not circular as a theorem
statement: it isolates exactly which physical data have to be proved for a
raw coordinate.  But it is conditional and supplies no existence proof for
those data.

## 6. Exact scope label

The safe status string is

```text
PASS_ROBUST_COORDINATE_COVER_AND_SQUARE_Q1_SUPPLY;
CONDITIONAL_BOUNDED_DEAD_BLOCK_LITERAL_LIFT;
NO_ALLK_OR_O1_CLAIM
```

No computation is required for this audit.
