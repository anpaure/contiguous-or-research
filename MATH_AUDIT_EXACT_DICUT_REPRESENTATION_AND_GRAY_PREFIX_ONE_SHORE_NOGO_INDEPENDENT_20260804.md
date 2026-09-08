# Independent audit of the exact dicut and one-shore no-go theorem

**Date:** 2026-08-04  
**Verdict:** **PASS after scope and exposition repairs.**  The nested
measurable-difference, exact-extension, zero--zero incidence, and one-way
dicut formulations are equivalent.  The contained-cell isolation theorem
is correct, and it implies the stated connected cyclic-interval obstruction.
The valuation and residence arguments close the exceptional power-of-two
case under the repaired hypotheses `M>s_2(r)`, `D>=3`, and `s_2(r)<D`.

No internet search, H100 computation, solver, or finite search was used.
This is a proof-level audit.

## 1. Audited sources

| role | file | SHA-256 |
|---|---|---|
| target before audit | `MATH_THEOREM_EXACT_DICUT_REPRESENTATION_AND_GRAY_PREFIX_ONE_SHORE_NOGO_20260804.md` | `382b535c180f1177b19c55d3432fe03cf71328e9532724fda729a2aee1291703` |
| target after audit | same file | `87ffe4d7e5d76f91676bfb9848d3f641b0586ce87049bfc1044b79043e164df1` |
| parent puncture theorem | `MATH_THEOREM_RESIDUE_CARRYING_PUNCTURES_AND_BILATERAL_COMPONENT_SEPARATOR_20260804.md` | `bd0f567bcd91f09e6c40216d08c0463e7abbe495756392095e5839ea8d690fbd` |
| independent parent audit | `MATH_AUDIT_RESIDUE_CARRYING_PUNCTURES_AND_BILATERAL_COMPONENT_SEPARATOR_INDEPENDENT_20260804.md` | `8d1cad8e99ddefb7a9dd73e7bf56cd30fc3e00242383b1ff2c4ce5f0598e37f1` |

The hash of this audit note is reported outside the note to avoid a
self-reference.

## 2. Repairs made to the target

The mathematical core required no reversal, but five scope/exposition
repairs were applied.

1. The meaning of an exact extension is now explicit: added blocks are
   pairwise disjoint, disjoint from the preselected owner set `U`, and cover
   its complement.
2. Corollary 1.2 now includes both directions of the zero--zero label proof.
3. Theorem 2.2 now explicitly justifies that a contained `Q`-cell is a
   connected subcube of the ambient `R`-cell.  Edge isolation alone would
   not logically identify connected components without this observation.
4. Corollary 3.2 now declares the residue-compatible length `b` positive,
   and Lemma 3.3 states the linear transition-index convention for internal
   path residence.
5. Corollary 3.4 now explicitly assumes `M>s_2(r)` and spells out
   `|U| congruent to W_r modulo 2^M`.  The previous phrase
   “residue-compatible” inherited this from Corollary 3.2, but the displayed
   corollary was not self-contained without it.

The last item is a genuine hypothesis repair.  Without `M>s_2(r)`, congruence
modulo `2^M` need not preserve the exact valuation `s_2(r)`.

## 3. Exact extension, nested difference, and dicut

Let the block-intersection multigraph have one edge labelled `v` from the
`P`-block `P(v)` to the `Q`-block `Q(v)`.

Given an exact extension, let `A` be the union of its selected `P`-blocks
and `Y` the union of its selected `Q`-blocks.  Exactness gives

\[
 A\cap Y=\varnothing,
 \qquad A\mathbin{\dot\cup}Y=V\setminus U.
\]

For `B=V-Y`, the set `B` is `Q`-measurable, `A subseteq B`, and
`B-A=U`.  Conversely, from `A subseteq B` and `U=B-A`, selecting the
`P`-blocks in `A` and the `Q`-blocks in `V-B` gives two disjoint measurable
sets whose union is `V-U`.  This verifies `(1)<->(2)` including the cases
`U=emptyset` and `U=V`.

For `(2)->(3)`, take `S` to contain the `P`-blocks outside `A` and the
`Q`-blocks outside `B`.  An entering edge would have its owner in `A-B`,
which is empty.  A leaving edge has its owner in `B-A=U`.  Parallel edges
cause no issue because equality is between labelled owner-edge sets.

For `(3)->(2)`, let `A` be the union of `P`-blocks outside `S` and `B` the
union of `Q`-blocks outside `S`.  An owner in `A-B` would label an entering
edge, so `A subseteq B`; the leaving edges are exactly the owners in `B-A`.
Thus all three formulations are exactly equivalent.

This is consistent with the parent puncture theorem.  In the all-available
case, touched blocks are unusable by an extension, including when a touched
block disappears entirely after deletion.  The full-graph dicut form
retains those zero-degree/swallowed cases automatically and is therefore an
exact sharpening, not an illicit use of the parent's survival-only multicut
corollary.

## 4. Zero--zero incidence form

Label a block `1` precisely when it is selected.  Every owner in `U` then
has labels `(0,0)`, while every owner outside `U` has exactly one selected
incident block and hence labels summing to one.  Conversely, equations

\[
 v\in U\Longrightarrow (x_{P(v)},y_{Q(v)})=(0,0),
 \qquad
 v\notin U\Longrightarrow x_{P(v)}+y_{Q(v)}=1
\]

make selected blocks disjoint from `U`, prohibit every selected--selected
incidence, and cover each owner outside `U` once.  Hence they give an exact
extension.  In particular, `U` is the **entire** zero--zero edge class and
the one--one edge class is empty.  The claim is stronger than endpoint
separation or an arbitrary multicut and is correct.

## 5. Contained pair cells

If a singleton `Q`-pair `{p,q}` is not an `R`-pair, its two choices lie in
different `R`-pairs.  Flipping `p` to `q` changes both corresponding
`R`-occupancies, so a `Q`-cell containing both choices cannot lie in one
fixed `R`-cell.  Lemma 2.1 follows.

Now consider an `R`-cube edge in direction `{p,q}`.

* If `{p,q}` is also a `Q`-pair, the flip preserves the complete
  `Q`-occupancy record, so both endpoints lie in the same `Q`-cell.
* Otherwise, if `p'` is the `Q`-partner of `p`, the occupancy of
  `{p,p'}` changes by one.  Of two adjacent values in `{0,1,2}`, at least
  one equals one.  That endpoint's `Q`-cell has a singleton on a nonshared
  pair and therefore cannot be contained in `C` by Lemma 2.1.

Thus no ambient cube edge joins two distinct contained `Q`-cells.  Every
contained `Q`-cell is nevertheless connected: all of its singleton
directions are shared `R,Q` pairs, hence are actual directions of the
ambient cube.  The contained cells are consequently exactly the connected
components of their union.  Theorem 2.2 and its connected-union consequence
are valid, including dimension-zero cells.

## 6. Cyclic interval and valuation consequences

A nonempty proper cyclic interval in a Hamilton cycle contains all path
edges between its consecutive vertices, so its vertex set is connected in
the ambient cube.  If it is a union of whole contained `Q`-cells, Theorem
2.2 forces it to be one cell.  A dimension-`a` pair cell has `2^a` owners,
which proves Corollary 3.1.  The particular Hamilton cycle need not be a
reflected Gray cycle and need not be resident for this step.

Write

\[
 W_r=2^s u,
 \qquad s=s_2(r),
 \qquad u\text{ odd}.
\]

If `M>s` and positive `b` satisfies `b congruent to W_r modulo 2^M`, then

\[
 b=2^s\bigl(u+2^{M-s}t\bigr),
\]

whose parenthesized factor is odd.  Hence `nu_2(b)=s`.  If also `b=2^a`,
then `a=s` and `b=2^s`.  This proves Corollary 3.2 for every positive
residue-compatible length, not only for the least positive residue.

The binary-reflected Gray-prefix observation is also correctly scoped: the
binary expansion decomposes a prefix into consecutive affine subcubes, but
their union is connected by the prefix path.  Therefore such a one-shore
realization would contradict Theorem 2.2 unless only one subcube occurs.

## 7. Residence no-go and boundary cases

Let a Hamilton path of `Q_a` have transition length `L=2^a-1`, and require
equal directions to have linear index gap at least `D`.

* If `L<D`, any repeated direction would have gap at most `L-1<D`, so all
  `L` transitions are distinct.  This would require `L<=a`, false for
  `a>=2`.
* If `L>=D`, the first `D` transitions are pairwise distinct, requiring
  at least `D` directions.  This contradicts `a<D`.

Thus Lemma 3.3 is exact for `2<=a<D`.

In Corollary 3.4, Corollaries 3.1--3.2 force the interval to be one
dimension-`a` contained cell with `a=s_2(r)<D`.  Every consecutive ambient
edge with both endpoints in that cell uses a shared `R,Q` direction, by the
nonshared case in Theorem 2.2.  The interval traversal is therefore a
Hamilton path of that `a`-cube.

The remaining boundary cases are correct:

* if `a=0`, the block has one vertex;
* if `a=1`, it has two vertices;
* under `D>=3`, both have fewer than the required `D` macro vertices;
* if `2<=a<D`, Lemma 3.3 excludes internal residence.

The assumption `D>=3` is necessary for the stated all-case conclusion:
when `D=2` and `a=1`, a two-vertex one-edge path meets the size threshold and
is internally resident vacuously.  The theorem correctly excludes this
boundary by hypothesis.

## 8. Exact scope of the result

The audited theorem rules out only the **one-shore contained-cell** route:
a connected residue interval cannot be assembled from several whole cells
of one other pairing, and its sole power-of-two exception fails at the
stated residence scale.  It does not rule out the exact positive object
identified by Theorem 1.1,

\[
 U=B\setminus A,
 \qquad A\text{ `P`-measurable},
 \quad B\text{ `Q`-measurable},
 \quad A\subseteq B,
\]

which genuinely uses both shores.  It also proves no existence of such a
resident nested difference, no good-dimension selector, no macro Hall, no
collar holonomy, no palette, and no compiler.  The theorem's final open
target is therefore proof-safe.

