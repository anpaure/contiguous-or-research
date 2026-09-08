# Hostile audit: monotone `q`-owner path packing and the one-seam palette gate

**Date:** 2026-08-13  
**Verdict:** **PASS AS PATCHED.**  The original source had one false residence
description and one missing global palette premise.  The erosion indices and the
one-ticket count were correct.  The patched source repairs both issues, proves order
rigidity, adds exact owner degrees and pair codegrees, and freezes the smallest exact
owner/lower packing-plus-fusion target.  
**Method:** direct Johnson-distance, coordinate-run, erosion, and incidence counting.
The finite degree/codegree replay ran only on `h100`.

## 1. Frozen sources

Original source:

`MATH_REDUCTION_MONOTONE_QOWNER_PATH_PACKING_AND_ONE_SEAM_PALETTE_GATE_20260813.md`

Original SHA-256:

`d895f4adc2a6f7669bb31360d3cc60b69789a37fc198b3b5cd51eb06780afec1`

Patched source SHA-256:

`5bb8716916ca5afdc42bc5f17a9f7c213bcf1e9b49213693e4de9be399e52e59`

## 2. First concrete failure in the original wording

The original status line said that an open monotone block is automatically
`q`-biresident.  This is false; the local statement is only boundary-clipped.

For the smallest example, take

\[
 q=2,\qquad A=\{1,2,3\},\qquad x_1=1,\qquad y_1=4.       \tag{2.1}
\]

The block is

\[
                         123,\ 234.                       \tag{2.2}
\]

On these two owners, coordinate `1` has word `10` and coordinate `4` has word `01`.
Thus their nonconstant runs reach the boundary, exactly as the local theorem says,
but their eventual lengths depend entirely on the adjoining blocks.  If the two-owner
trace is closed by itself, the same transition support `{1,4}` occurs on both cyclic
edges and both coordinates have positive and zero runs of length one, violating
`2`-biresidence.

Therefore no open block is resident by itself.  The patched status and proof now claim
only that no nonconstant run has both endpoints inside the block.  Global residence is
deduced later from all transition windows meeting the seams.

## 3. Local path rigidity

For `i<j`, direct subtraction in the displayed construction gives

\[
                         d_J(T_i,T_j)=j-i.                 \tag{3.1}
\]

Hence two support owners are Johnson adjacent exactly when their indices are
consecutive.  The induced Johnson graph on one support is exactly `P_q`.  This proves
three facts which the original hypergraph paragraph used but did not justify:

1. the unordered support determines the monotone order up to reversal;
2. there are exactly two orientations, not a larger occurrence multiplicity; and
3. the internal edge set and internal lower-colour set are determined by the support.

The support hypergraph formulation is therefore sound.  A perfect support matching
really is a partition into monotone path supports; after it is selected, only one of
two orientations per block remains to be chosen.

## 4. Erosion index audit

Use the ambient maximal antecedent

\[
                         P_t=\bigcap_{v=0}^{q-1}T_{t-v}.  \tag{4.1}
\]

For a consecutive interval `0<=a<=b<=q-1`, the exact identity is

\[
 \boxed{
 \bigcap_{j=a}^{b}T_j=\bigcup_{u=b}^{a+q-1}P_u.}         \tag{4.2}
\]

The original notation

\[
 \bigcup_{v=b-a}^{q-1}P_{a+v}                            \tag{4.3}
\]

is algebraically the same range; it was not an off-by-one error.  The patch rewrites
it as (4.2) and supplies the missing proof.

Indeed, for each `u in [b,a+q-1]`, the erosion window `[u-q+1,u]` contains `[a,b]`,
so the right side is contained in the left.  Conversely, if a coordinate is present
through `[a,b]`, global `q`-positive residence puts `[a,b]` inside a positive run of
length at least `q`.  That run contains some `q`-window covering `[a,b]`, whose right
endpoint necessarily lies in `[b,a+q-1]`.  This proves the reverse containment.

Only positive residence is needed for (4.2).  Zero residence is needed elsewhere for
the literal owner clock and splice safety, not for this erosion equality.

## 5. Exact lower ledger and the missing premise

Suppose `b=W/q` blocks partition the owners.  They have exactly

\[
                         b(q-1)=W-b                       \tag{5.1}

internal transitions and `b` seams.  For odd `k=2R-1`,

\[
 {k\choose R-1}={k\choose R}=W.                          \tag{5.2}

Thus, **provided the internal lower values are globally distinct**, their set
`\mathcal I` has size `W-b` and the seams must be exactly its `b`-element complement.
This proves the one-ticket-per-block ledger with coefficient one.

The emphasized premise was present in Proposition 2.1 but was dropped in the original
seam proposition.  Merely asking for `b` distinct seam colours outside `\mathcal I`
does not repair an internal collision: if two internal occurrences have the same
value, then

\[
                         |\mathcal I|\le W-b-1            \tag{5.3}
\]

and its complement has at least `b+1` colours.  The `b` seams can be distinct and
unused while still leaving a lower colour uncovered.  The original converse therefore
did not follow.

The patch explicitly carries global internal distinctness into Proposition 3.1 and,
more usefully, makes every internal lower colour a host resource in `\mathcal G_q`.
An owner-perfect matching in that augmented host enforces the premise automatically.

## 6. Residence and exact seam collars

Write `E_i=T_i triangle T_(i+1)` for a transition support.  A coordinate changes
exactly on the edges whose supports contain it.  Its cyclic positive and zero run
lengths are the separations between consecutive such edges.  Hence

\[
 \boxed{\text{the trace is `q`-biresident}
 \iff\text{ every `q` consecutive supports are coordinate-disjoint}.} \tag{6.1}
\]

Inside a monotone block the `q-1` supports are pairwise disjoint, because all
`x_i,y_i` are distinct.  Every `q`-edge window therefore meets a seam.  Since seams
are spaced by exactly `q` edges in the pure block decomposition, every such window
meets exactly one seam.  Recording the entire ordered `q-1` transition word on both
sides of a seam is sufficient and necessary to check all windows meeting it.

This verifies the patched Proposition 3.1.  The original phrase “internal residence
follows” was too strong: local monotonicity supplies only the disjoint internal collar;
the seam tests jointly supply global residence.

## 7. Exact support-hypergraph census

Let `ell=q-1`.  The patch proves

\[
 D_q={q\over2}(R)_{\underline\ell}(R-1)_{\underline\ell} \tag{7.1}
\]

for the owner degree.  To audit it, fix an owner and its position in the oriented
path.  Across the earlier and later exchanges, choose one ordered list of `ell`
distinct coordinates inside the owner and one outside it.  This gives
`(R)_ell(R-1)_ell` paths per position, `q` positions, and a factor `1/2` because each
support has the two recovered orientations.

For owners at Johnson distance `d<=ell`, orient the unique path direction so the first
owner precedes the second.  There are `q-d` possible positions, `(d!)^2` orders for the
forced central exchanges, and

\[
 (R-d)_{\underline{\ell-d}}
 (R-1-d)_{\underline{\ell-d}}                            \tag{7.2}
\]

choices for all exchanges outside their interval.  Thus

\[
 \lambda_{q,d}=(q-d)(d!)^2
 (R-d)_{\underline{\ell-d}}
 (R-1-d)_{\underline{\ell-d}},                           \tag{7.3}
\]

and the codegree is zero for `d>ell`.  Division by (7.1) gives the source formula.
For `q<=(R+1)/2`, consecutive ratios are below one and

\[
                         {\Delta_2\over D_q}
 ={2(q-1)\over qR(R-1)}.                                 \tag{7.4}
\]

Exact enumeration on `h100` replayed all supports for `3<=R<=5` and
`2<=q<=min(R,4)`.  Representative rows were

\[
\begin{array}{c|c|c|c}
R&q&D_q&(\lambda_{q,1},\lambda_{q,2},\lambda_{q,3})\\ \hline
3&3&18&(4,4,0)\\
4&3&108&(12,4,0)\\
4&4&288&(36,16,36)\\
5&3&360&(24,4,0)\\
5&4&2880&(216,48,36).
\end{array}                                               \tag{7.5}
\]

Every exact value matched (7.1)--(7.3).  The computation is only a replay; the proof
is the direct count above.

## 8. Smallest exact global target

The augmented `(2q-1)`-uniform host `\mathcal G_q` has the owner shore
`\mathcal O`, lower shore `\mathcal L`, and one edge consisting of a path's `q`
owners together with its `q-1` internal lower colours.  It has exact shore degrees

\[
 d_{\mathcal O}=D_q,\qquad
 d_{\mathcal L}={q-1\over q}D_q.                         \tag{8.1}
\]

An `\mathcal O`-perfect matching has `W/q` blocks, makes every internal colour
distinct, and leaves exactly `W/q` lower colours.  After that matching is chosen, the
remaining task is exactly:

* choose one of two orientations for each selected block; and
* find a directed Hamilton cycle through the blocks whose seam arcs pass the collar
  test and whose distinct labels are the unused lower colours.

Because the number of arcs equals the number of missing colours, “distinct labels in
the missing set” is equivalent to “use every missing colour exactly once.”  This proves
both directions of patched Theorem 4.2 and is the smallest exact packing/fusion target
currently justified by the monotone-path construction.

It remains a matching-plus-rainbow-Hamilton theorem, not a consequence of the owner
support matching alone.  Mixed `q,q+1` sizes can remove the scalar `q|W` obstruction
only when their sizes represent `W`; they do not prove the mixed packing or remove
other incidence-lattice constraints.

## 9. Final scope verdict

After patching, the following statements are exact:

* local monotone paths have boundary-clipped coordinate runs and rigid order;
* conditional erosion identity (4.2);
* the one-seam lower deficit under global internal distinctness;
* the transition-collar equivalence for global `q`-biresidence;
* exact owner degrees and pair codegrees; and
* the augmented-host plus rainbow-Hamilton equivalence.

No owner-perfect augmented matching, rainbow seam cycle, upper palette, low-rank
compiler, mixed-size absorber, or one-cycle terminal cap is proved.  Subject to those
scope limits, the patched reduction passes.
