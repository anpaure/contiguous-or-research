# Exact full Greene--Kleitman root-hinge catalogue and its linear worst-case menu

**Date:** 2026-08-07  
**Status:** unconditional characterization and exact worst-case list size.
It disproves a uniform quadratic-menu premise for the full GK-compatible
hinge family.  It does not settle the global resource transversal.

## 1. Setup

Let `U` be a Dyck word of semilength `m`, and let `H(t)` be its height after
position `t`.  Choose two upsteps `u,b` of `U` and a downstep `x`.  Put

\[
 X=U-u,qquad B_x=U-u-b+x.                              \tag{1.1}
\]

Let `t` be the standard Greene--Kleitman successor: it changes the
rightmost unmatched zero to one.  We seek exactly the triples `(u,b,x)` for
which

\[
 t(X)=X+y,qquad t(B_x)=B_x+b.                          \tag{1.2}
\]

The first equation determines `y` uniquely.

## 2. Height-record characterization

## Theorem 2.1 (full literal catalogue)

Equations (1.2) hold if and only if all the following conditions hold.

1. `u<b<x`.
2. The upstep `b` ends at height one or two.
3. If `b` ends at height one, it opens a nonfirst top-level primitive
   component, and `u` is any upstep in an earlier top-level component.
4. If `b` ends at height two, it opens a child subtree of a top-level root,
   and `u` is the top-level root opener or any upstep in an earlier sibling
   subtree of `b`.
5. The position `x` is any downstep in the subtree opened by `b`, including
   its closing downstep.

In both cases, `y` is the closing downstep of the top-level primitive
component containing `u`.

### Proof

Changing `u,b` from upsteps to downsteps and `x` from a downstep to an
upstep gives

\[
 H_{B_x}(t)=H(t)-2{\bf1}_{t\ge u}-2{\bf1}_{t\ge b}
                  +2{\bf1}_{t\ge x}.                  \tag{2.1}
\]

If `b` is the rightmost unmatched zero, its step creates the last new
record low.  In particular its height is no larger than the final height
`-2`.  Inspecting the possible orders of `u,b,x` in (2.1) shows that the
only possible order is `u<b<x`.  If the original upstep `b` ends at height
`h`, then

\[
                              H_{B_x}(b)=h-4.           \tag{2.2}
\]

Since no later height may fall below this record and the final height is
`-2`, equation (2.2) forces `h<=2`.

Suppose first that `h=2`.  Before `b`, only the change at `u` is active.
For `b` to create the new record `-2`, the original path may not return to
height zero between `u` and `b`.  Hence `u` and `b` lie in the same
top-level primitive component, and `u` occurs in the root opener or an
earlier root-child subtree.  Conversely this condition keeps the modified
height at least `-1` before `b`.

If `h=1`, equation (2.2) gives the new record `-3`.  This happens exactly
when `b` opens a later top-level component; any earlier upstep `u` is
allowed, because before `b` the modified path is bounded below by `-2`.

Between `b` and `x`, the displacement in (2.1) is `-4`.  The record at `b`
survives precisely while the original path stays at height at least `h`.
Therefore `x` must be a downstep in the excursion opened by `b`, and every
such downstep works.  At and after `x`, the displacement becomes `-2`.
The original Dyck path is nonnegative, so no later lower record is created
when `h=2`, and all later heights are strictly above the record when
`h=1`.

Finally, in `X=U-u` the displacement is `-2` after `u`.  Its last new
record zero is reached when the top-level primitive component containing
`u` first closes.  This is the asserted position `y`.  All conditions are
therefore necessary and sufficient. \(\square\)

## 3. Exact menu formula

Write the top-level primitive components of `U` as ordered rooted plane
trees `T_1,...,T_k`, with edge counts

\[
                         n_1+\cdots+n_k=m.             \tag{3.1}
\]

For the root children of `T_j`, let their subtree edge counts be

\[
                         s_{j1},...,s_{jd_j},qquad
                         \sum_{q=1}^{d_j}s_{jq}=n_j-1. \tag{3.2}
\]

Then Theorem 2.1 gives exactly

\[
\boxed{
 |L_U|=
 \sum_{1\le i<j\le k}n_i n_j
 +\sum_{j=1}^k\left[(n_j-1)+
             \sum_{1\le p<q\le d_j}s_{jp}s_{jq}\right].}
                                                               \tag{3.3}
\]

Indeed, a later top-level opener in `T_j` has
`n_1+...+n_{j-1}` choices for `u` and `n_j` choices for `x`.  A root child
of size `s_{jq}` has

\[
                         1+\sum_{p<q}s_{jp}
\]

choices for `u` and `s_{jq}` choices for `x`.  Summing gives (3.3).

Using `sum_q s_{jq}=n_j-1`, formula (3.3) simplifies to

\[
\boxed{
 |L_U|={1\over2}\left(m^2-k-
             \sum_{j=1}^k\sum_{q=1}^{d_j}s_{jq}^2\right).}     \tag{3.4}
\]

## Corollary 3.1 (exact worst-root scale)

For every Dyck root,

\[
                              |L_U|\ge m-1.             \tag{3.5}
\]

The bound is sharp: for the mountain word `1^m0^m`,

\[
                              |L_U|=m-1.                \tag{3.6}
\]

### Proof

Discarding the nonnegative sibling products in (3.3) gives

\[
 |L_U|\ge {k\choose2}+m-k\ge m-1.
\]

For the mountain there is one top-level tree and its root has one child of
size `m-1`; formula (3.3) gives exactly `m-1`. \(\square\)

Thus no theorem asserting `|L_U|=Omega(m^2)` uniformly over all roots can
hold for this catalogue.  Moreover, the extremal family is exponentially
large.  Every word

\[
                              U=11E00,                  \tag{3.7}
\]

with `E` an arbitrary Dyck word of semilength `m-2`, has one top-level
component whose root has one child of size `m-1`.  Hence it attains
`|L_U|=m-1`.  There are `Cat_{m-2}` such roots, and

\[
 {\operatorname {Cat}_{m-2}\over\operatorname {Cat}_m}
 ={m(m+1)\over4(2m-1)(2m-3)}\longrightarrow {1\over16}. \tag{3.8}
\]

Therefore the linear-menu roots are not a polynomial or `o(Cat_m)`
exceptional bank; they form a positive asymptotic proportion.

## 4. Coarse resource-load boundary

The characterization gives immediate polynomial, but not linear, load
bounds.  A fixed rank-`(m-2)` colour `a` has at most

\[
                         m(m+1)(m+2)                   \tag{4.1}
\]

preimages `(U,u,b,x)`: choose the ordered pair `u,b` from the `m+2`
coordinates outside `a`, then choose `x` from the remaining coordinates.
Likewise a fixed rank-`(m-1)` resource occurs as `B_x` in at most
`O(m^3)` catalogue entries.  The immediate counting bound for its `B_y`
load is `O(m^4)`: after choosing the deleted element `y`, the ordered pair
`u,b`, and hence `U`, there may still be `O(m)` legal choices for `x`.

These are only upper bounds; the Dyck and record constraints reduce them.
However, together with the sharp minimum list `m-1`, they show that a
quadratic-list-versus-linear-load greedy argument is not presently
available.  Any exact transversal must exploit the ordered-tree structure,
use a second matching phase, or tolerate/fuse controlled overlaps.

## 5. Exact Hall routing for the extremal linear-menu family

The positive-density extremal family in (3.7) nevertheless has a rigid
useful structure.  Put

\[
                         \mathcal F_m=\{11E00:E\in D_{m-2}\}.
\]

For `U in F_m`, the only possible pair `(u,b)` is the first two upsteps.
The colour

\[
                         a_U=U-\{1,2\}
\]

and the resource

\[
                         B_{y,U}=a_U+\{2m\}             \tag{5.1}
\]

are injective in `U`.  Moreover every `B_{y,U}` contains the final
coordinate, whereas no fixed root facet `X_V subset V` does.  Hence this
entire `B_y` bank is disjoint from the fixed `X` bank.

For every downstep `x` in the unique child subtree, put

\[
                         V_x=U-\{2\}+\{x\}.             \tag{5.2}
\]

Before `x`, changing the child opener at position `2` downward lowers the
Dyck height by two; the path stays nonnegative because `x` lies in that
child subtree.  At `x`, changing the downstep upward restores the original
height.  Thus `V_x` is Dyck.  Also

\[
                         B_x(U,x)=a_U+\{x\}=X_{V_x}.    \tag{5.3}
\]

Let `J_m` be the bipartite graph from `F_m` to all Dyck roots in which
`U V_x` is an edge.  Every left vertex has degree exactly `m-1`.  A fixed
right root `V` has degree at most `m-1`: a preimage is recovered by choosing
the deleted position `x in V` and setting `U=V-x+\{2\}`, and position `1`
cannot be chosen.

For every `S subset F_m`, edge counting therefore gives

\[
             (m-1)|S|=e(S,N(S))\le(m-1)|N(S)|.
\]

Hall's theorem proves:

## Theorem 5.1 (linear-family controlled-overlap routing)

There is an injection `phi:F_m -> D_m` such that every extremal root `U`
has a valid hinge with

\[
                         B_{x,U}=X_{\phi(U)}.            \tag{5.4}
\]

Simultaneously, all its `a_U` and `B_{y,U}` resources are private, and the
`B_y` bank avoids every fixed root facet.

This is a controlled-overlap theorem, not a private-hinge theorem: the
selected `B_x` values intentionally lie in the fixed `X` bank.  A global
degree-two circuit still has to route those overlaps.
