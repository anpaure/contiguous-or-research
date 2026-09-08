# The GK depth-two root graph is regular and connected, but its free orientation has Catalan-many sinks

**Date:** 2026-08-07  
**Status:** unconditional graph theorem and exact scope audit.  The result
removes abstract root connectivity as an obstruction.  It does **not** give
a rainbow physical Hamilton path: the simplest connectivity paths reuse a
lower colour, and the free orientation has a Catalan path-cover lower bound.

## 1. The graph and its tree move

Let `D_m` be the Dyck words of semilength `m`.  For `U in D_m`, let its
first primitive component have semilength `n_1(U)`.  A **depth-two flip**
chooses

* an upstep `b` from height one to height two in that first primitive; and
* a downstep `x` in the excursion opened by `b`, including its closing
  downstep,

and changes `b` to a downstep and `x` to an upstep.  The resulting word is
again Dyck.  Write `U -> V` for this orientation and let `H_m` be the
underlying simple graph.

In the rooted-plane-tree interpretation, the first primitive is the subtree
at the first child `v` of the root.  The position `b` is an edge from `v` to
one of its children, and `x` is the return traversal of an arbitrary edge in
that child's subtree.  Thus the move is a root-child contour transposition.
There is one outgoing arc for every non-root edge of the first-child
subtree:

\[
                    d^+(U)=n_1(U)-1.                  \tag{1.1}
\]

The flip strictly decreases the usual `1`-before-`0` inversion statistic by
`x-b`.  In particular, the depth-two orientation is acyclic.

## 2. Exact arc duality and regularity

## Theorem 2.1

For every `U in D_m`,

\[
                    d^- (U)=m-n_1(U),                 \tag{2.1}
\]

and consequently

\[
                    \boxed{d_{H_m}(U)=m-1}.           \tag{2.2}
\]

### Proof

Let `y` be the downstep closing the first primitive of `U`.  Every incoming
depth-two arc is obtained uniquely as follows.  Choose an upstep `q` in a
later top-level primitive, change `y` to an upstep and `q` to a downstep.
Call the resulting word `W`.  Before `q`, the extra opening at `y` raises
the path by two; from `q` onward the two changes cancel.  Hence `W` is
Dyck.  In `W`, the old `y` is a depth-two opener and the old `q` is a
downstep in its excursion, so the depth-two flip `W -> U` is legal.

Conversely, reversing any depth-two arc into `U` must turn the first closing
downstep `y` upward and one later upstep downward.  Thus the construction is
bijective.  There are exactly `m-n_1(U)` upsteps after the first primitive,
proving (2.1).

Outgoing and incoming arcs cannot be the same, because the inversion
statistic strictly falls on every outgoing arc.  Equations (1.1) and (2.1)
therefore give (2.2). \(\square\)

This also reproves

\[
                  |E(H_m)|={m-1\over2}\operatorname{Cat}_m. \tag{2.3}
\]

## 3. Explicit connectivity

Call a word of the form `10 A`, with `A in D_{m-1}`, a **sink word**.  These
are exactly the sinks of the depth-two orientation, and there are
`Cat_{m-1}` of them.

## Theorem 3.1

`H_m` is connected for every `m>=2`.  More precisely, every vertex is
joined to

\[
                         Z_m=(10)^m                  \tag{3.1}
\]

by an explicit sequence of depth-two edges.

### Proof

If `U` is not a sink, then it begins with `11`.  Choose `b` to be its second
position and choose for `x` the closing downstep matched to `b`.  The
depth-two flip at `(b,x)` produces a sink `10 A`.

It remains to connect every sink to `Z_m`.  Suppose `A` is not
`(10)^{m-1}`.  Then `A` has an upstep `q` beginning at positive height.
Let `x` be the downstep matched to `q`, and define

\[
             A'=A-q+x,\qquad
             W=11\,(A\text{ with }q\text{ changed to }0).   \tag{3.2}
\]

Here `A-q+x` means that `q` is changed from `1` to `0` and `x` from `0`
to `1`.  Because `q` begins at positive height, lowering the subexcursion
between `q` and `x` by two never makes it negative.  Thus `A'` is Dyck.
Likewise `W` is Dyck: before `q` its height is two above that of `A`, and
after `q` it equals the height of `A`.

The word `W` has two legal depth-two arcs, both using its second position:

\[
                         10A \leftarrow W \to 10A'.  \tag{3.3}
\]

The inversion statistic of `A'` is smaller than that of `A` by `x-q`.
Iteration therefore terminates.  A Dyck word with no upstep beginning at
positive height has only singleton top-level primitives, so the terminal
word is `(10)^{m-1}`.  This proves connectivity. \(\square\)

The proof gives a path of length at most
`1+2*binom(m-1,2)` from each vertex to `Z_m`, and hence the coarse
diameter bound

\[
                    \operatorname {diam}(H_m)
                    \le 4{m-1\choose2}+2.             \tag{3.4}
\]

No optimization of this bound is claimed.

## 4. Why connectivity is not yet a physical fusion theorem

For an arc `U -> V` with active opener `b`, the GK hinge colour is

\[
                         a(U,b)=U-\{1,b\}.             \tag{4.1}
\]

The two arcs in the sink bridge (3.3) use the same source `W` and the same
opener `b=2`.  They therefore have the same `a` colour.  Consequently the
connectivity proof is not a rainbow path construction: using both arms of
one bridge repeats a required lower colour.

There is a second exact limitation.  A directed path cover using only the
free orientation must end every path at a sink.  Hence it has at least

\[
                  \boxed{\operatorname {Cat}_{m-1}}   \tag{4.2}
\]

components.  Since

\[
 {\operatorname {Cat}_{m-1}\over\operatorname {Cat}_m}
 ={m+1\over 2(2m-1)}\longrightarrow {1\over4},        \tag{4.3}
\]

no `O(1)`-path cover can be obtained from the acyclic orientation while
requiring at most one outgoing free hinge at each root.  Reverse traversal,
multiple distinct openers at a root, or an additional rethread is necessary
for stronger contraction.

On the other hand, the existing extremal-family Hall theorem is already a
genuinely capacity-faithful positive contraction.  For

\[
                  \mathcal F_m=\{11E00:E\in D_{m-2}\},
\]

it selects one depth-two arc per root with injective targets and private
`a` and `B_y` banks.  Acyclicity then makes the selected arcs a directed
path forest with exactly `Cat_{m-2}` edges.  Thus the currently proved
fully controlled depth-two contraction removes the positive fraction

\[
 {\operatorname {Cat}_{m-2}\over\operatorname {Cat}_m}
 ={m(m+1)\over4(2m-1)(2m-3)}\longrightarrow {1\over16} \tag{4.4}
\]

of root components in one pass.

## 5. Exact audit of external Gray-code shortcuts

The known Catalan Gray codes cannot be imported merely from their
transposition or leaf-move descriptions.

1. **Binary-tree rotations.**  The depth-two graph is not the
   associahedron: `H_4` has no four-cycle, whereas the associahedron has a
   commuting-rotation square.

2. **Greedy homogeneous Dyck transpositions.**  Reverse the bit convention
   of the Vajnovszki--Wong listing to the present `1=up` convention.  At
   semilength four it contains the consecutive transition

   \[
                    10101100\longleftrightarrow10111000. \tag{5.1}
   \]

   Both words begin with `10`, hence both are sinks of the depth-two
   orientation.  No two sinks are adjacent in `H_4`.  Thus that published
   Hamilton path is not a spanning subgraph of `H_m` from `m=4` onward.

3. **Literal star transpositions.**  Every Dyck word starts in `1`, and
   every depth-two flip fixes that first coordinate.  A nontrivial literal
   star transposition at the first coordinate therefore is not an edge of
   `H_m`.  Quotienting or rotating representatives would require a new
   edge-by-edge proof.

4. **Delete-and-append leaf moves.**  This move class is also strictly
   larger.  At `m=3`, the two ordered trees encoded by `101010` and
   `101100` differ by moving one root leaf to become a child of the second
   root child, but both words are depth-two sinks and hence are not
   adjacent in `H_3`.  Nakano's leaf-move theorem therefore supplies no
   automatic `H_m` Hamilton path.

## 6. Exact frontier

At the uncoloured graph level there is no component obstruction:

\[
                         \boxed{H_m\text{ is connected and }(m-1)
                         \text{-regular}.}
\]

The obstruction is now specifically physical and coloured.  One needs a
degree-two selector of depth-two arcs that simultaneously

* avoids repeated `a` colours;
* uses each target facet `X_V` at most once;
* controls the unused endpoint bank; and
* beats the Catalan sink barrier by a certified rethread or by using
  multiple distinct openers at selected roots.

Without that extra selector, graph Hamiltonicity alone would still not
finish the root fusion.
