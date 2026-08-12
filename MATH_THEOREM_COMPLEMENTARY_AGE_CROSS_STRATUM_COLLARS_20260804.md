# Complementary-age cross-stratum collars

**Date:** 2026-08-04  
**Status:** unconditional local residence theorems.  This note sharpens the
collar part of
`MATH_THEOREM_RUN_TRANSPARENT_PAIR_CELL_SQUARES_AND_EXCEPTIONAL_PORT_GATE_20260804.md`.
It does not prove that the required balanced collars occur in a spanning
pair-cell factor, and it makes no palette or compiler claim.

## 1. Transition-slot ages

Open an `L`-resident cube cycle at one transition edge.  At either endpoint,
number the retained transition edges going inward by

\[
                       1,2,\ldots,L-1.                 \tag{1.1}
\]

The number in (1.1) is the **transition-slot age**.  Thus, if one common
direction occurs at age `i` on one side of a new seam and at age `j` on the
other side, the two occurrences have transition-slot separation exactly

\[
                              i+j.                     \tag{1.2}
\]

Consequently the repeated direction is safe across that seam if and only if

\[
                              i+j\ge L.                 \tag{1.3}
\]

This is the off-by-one point hidden by the stronger disjoint-collar
condition: two collars may share directions, provided their ages are
complementary.

Every one-sided `(L-1)`-collar contains `L-1` distinct directions.  Also, the
deleted cut direction is absent from both endpoint collars.  Both statements
follow immediately from `L`-residence.

## 2. One seam at the critical dimension

Consider the cross-stratum adjacency

\[
 (D,E,S)\longleftrightarrow(D-\{p\},E-\{q\},S\cup\{p,q\}),
 \qquad |S|=m,                                         \tag{2.1}
\]

and delete a common-direction edge from each cube.  At one proposed seam,
write the small-side collar directions in increasing age as

\[
 a_1,a_2,\ldots,a_{L-1}
\]

and the large-side collar directions as

\[
 b_1,b_2,\ldots,b_{L-1}.
\]

Assume that the two exceptional large-cube directions `p,q` are absent from
this large-side collar.

### Theorem 2.1 (complementary-age one-seam relabelling)

If

\[
                              m\ge L,                   \tag{2.2}
\]

then the common cube directions can be relabelled so that the cut direction
is fixed and the seam is `L`-safe.  Explicitly, set

\[
                     a_i\longmapsto b_{L-i}
                     \qquad(1\le i<L),                 \tag{2.3}
\]

fix the common cut direction, and extend arbitrarily to a bijection of the
remaining common directions.

#### Proof

The collar directions are distinct, and the cut direction belongs to neither
collar.  Thus (2.2) gives room for the `L-1` assignments (2.3) and the fixed
cut direction.  Every repeated collar direction then has ages `i` and
`L-i`, whose sum is exactly `L`; by (1.3) it is safe.  Any common direction
not paired by (2.3) is absent from at least one of the two collars and creates
no cross-seam short repetition.  The exceptional directions `p,q` are absent
by hypothesis.  Hence this seam satisfies the complete transition-spacing
condition. \(\square\)

The theorem is deliberately one-seam local.  A square switch has two seams,
and both must use one common relabelling.  The next section gives the exact
compatibility test.

## 3. Exact two-seam criterion

Let `U,V` be the two sets of `m` common abstract directions in the small and
large cubes.  Let `s_U,s_V` be their deleted cut directions.  For endpoint
`epsilon in {0,1}`, define

\[
 \alpha_\epsilon:U\longrightarrow\{1,\ldots,L-1,L\},\qquad
 \beta_\epsilon:V\longrightarrow\{1,\ldots,L-1,L\},   \tag{3.1}
\]

where a finite value is the transition-slot age and the value `L` means
"absent from this collar."  In particular,

\[
 \alpha_\epsilon(s_U)=\beta_\epsilon(s_V)=L.           \tag{3.2}
\]

The value `L` is only a capped infinity: it is convenient because an absent
direction is automatically safe in every inequality below.

One may pair endpoint `epsilon` of the small path with endpoint
`sigma(epsilon)` of the large path, where `sigma` is either the identity or
the transposition.  Define a bipartite graph `G_sigma` on

\[
                  U-\{s_U\}\quad\text{and}\quad V-\{s_V\}       \tag{3.3}
\]

by declaring `uv` legal when

\[
 \alpha_\epsilon(u)+\beta_{\sigma(\epsilon)}(v)\ge L
 \qquad(\epsilon=0,1).                                \tag{3.4}
\]

### Theorem 3.1 (simultaneous complementary-age criterion)

Assume:

1. both old cube cycles are `L`-resident;
2. both opened arcs have at least `L` edges;
3. `p,q` are absent from both large endpoint collars.

Then the cross-stratum square admits an `L`-resident common-direction
relabeling if and only if, for at least one endpoint pairing `sigma`, the
graph `G_sigma` has a perfect matching.

Equivalently, the exact remaining condition is

\[
 |N_{G_\sigma}(X)|\ge |X|
 \qquad\text{for every }X\subseteq U-\{s_U\}.           \tag{3.5}
\]

#### Proof

Any relabelling fixes the two copies of the deleted common cut direction and
restricts to a bijection in (3.3).  At seam `epsilon`, a common direction
repeated at the two finite ages is safe exactly when (3.4) holds, by (1.2).
Thus every resident relabelling gives a perfect matching of `G_sigma`.

Conversely, a perfect matching of `G_sigma`, together with
`s_U -> s_V`, is a bijection of all common directions.  Condition (3.4)
protects every common direction across both seams.  Hypothesis 3 protects the
two seam coordinates `p,q`; hypothesis 2 separates their two seam
occurrences; and old internal repetitions are protected by hypothesis 1.
These are all coordinate classes, so the switched cycle is `L`-resident.
Hall's theorem gives (3.5). \(\square\)

This replaces the old set-disjointness requirement by an exact, ordinary
bipartite matching problem on age histories.

## 4. Two useful corollaries

### Corollary 4.1 (balanced collars close the critical case)

Suppose, in each opened cube, the two endpoint collars use the same support
of `L-1` directions.  In the large cube suppose additionally that `p,q` are
outside that common support.  If `m>=L`, then `G_sigma` has a perfect
matching, and the square switch is `L`-resident.

#### Proof

On either cube, every supported direction occurs once in each endpoint
collar.  Old residence gives

\[
                 \alpha_0(u)+\alpha_1(u)\ge L.          \tag{4.1}
\]

Summing (4.1) over the `L-1` supported directions gives equality, because
each endpoint age multiset is exactly `{1,...,L-1}`:

\[
 \sum_u(\alpha_0(u)+\alpha_1(u))=L(L-1).
\]

Hence every inequality in (4.1) is an equality.  The same holds for the
large cube.

Match the unique small direction of age `i` at endpoint zero to the unique
large direction of age `L-i` there.  At endpoint one their ages are
respectively `L-i` and `i`, so both seam sums equal `L`.  Match the
directions outside the common collar supports arbitrarily, fixing the cut
direction.  This is possible because `m>=L`.  Theorem 3.1 applies. \(\square\)

Thus the critical scale `m=L+O(log r)` has no numerical collar obstruction:
one phase-coherent local pattern--equal support at the two ends--already
closes it.  What remains is to plant or regenerate that pattern in the cube
factor.

### Corollary 4.2 (automatic two-seam range improves from `4L` to `2L`)

If `p,q` have already been chosen outside both large endpoint collars, then

\[
                              m\ge2L-3                  \tag{4.2}
\]

guarantees a perfect matching in every `G_sigma`.  Without a pre-existing
choice of `p,q`, the worst-case sufficient bound is

\[
                              m\ge2L-1.                  \tag{4.3}
\]

#### Proof

Fix a small direction `u`.  If it occurs at ages `i_0,i_1` in both endpoint
collars, old residence gives `i_0+i_1>=L`.  At endpoint `epsilon`, it is
incompatible with at most `L-i_epsilon-1` large collar directions.  Hence
its total forbidden degree is at most

\[
 (L-i_0-1)+(L-i_1-1)\le L-2.                           \tag{4.4}
\]

If it occurs in only one collar, the same bound is immediate.  The symmetric
argument gives forbidden degree at most `L-2` on the large shore.

After fixing the cut direction, `G_sigma` has `n=m-1` vertices on each
shore and minimum degree at least `n-(L-2)`.  Under (4.2) this is at least
`n/2`.  A balanced bipartite graph with minimum degree at least half its
shore size has a perfect matching: if `|X|<=n/2`, any one vertex of `X` has
at least `n/2>=|X|` neighbours; if `|X|>n/2` and some right vertex lay
outside `N(X)`, all its at least `n/2` neighbours would lie in a complement
of size `<n/2`, a contradiction.

Finally, the union of the two large collars has size at most `2L-2`.  The
large cube has `m+2` abstract directions, and its cut direction is already
outside that union.  To choose two further directions `p,q` outside it in
the worst case requires `m+2-(2L-2)>=3`, which is (4.3). \(\square\)

## 5. Revised residence frontier

The former `m>=4L` bound was an artefact of forbidding every collar overlap.
The exact picture is now:

* one seam is always solvable at `m>=L` by complementary ages;
* two seams are governed exactly by the Hall graph (3.4);
* arbitrary endpoint histories are automatically solvable by `m>=2L-1`;
* at the critical scale `m=L+O(log r)`, balanced two-end collar support is a
  complete phase-coherent certificate.

The remaining residence theorem is therefore not a counting theorem.  It is
the construction of cube cuts whose two endpoint collars have the balanced
support property, or more generally satisfy the Hall condition (3.5), while
the global component splice is assembled.  The exceptional `Q_0,Q_1` ear
problem also remains: complementary-age relabelling removes no triangle
pulse inside a genuinely two-edge ear.
