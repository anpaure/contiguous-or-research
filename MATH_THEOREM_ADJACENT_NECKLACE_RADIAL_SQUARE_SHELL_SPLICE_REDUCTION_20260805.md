# Adjacent necklaces: the universal radial square and shell-splice reduction

**Date:** 2026-08-05  
**Method:** minimum-coordinate shells and four explicit adjacent transfers;
no computation  
**Status:** unconditional reduction.  It gives the exact cross-shell splice
for every number of slots.  It does **not** prove the protected Hamilton or
near-perfect matching statement inside a higher-dimensional boundary shell.

## 1. Minimum-coordinate shells

For integers `q>=3,b>=1`, write

\[
 \mathcal N_{q,b}
 =\{x\in\mathbb Z_{\ge0}^q:\sum_i x_i=b\}/C_q
\]

and join two necklaces when one unit is moved between cyclically adjacent
coordinates.  Put

\[
 \partial\mathcal N_{q,s}
 =\{[x]\in\mathcal N_{q,s}:\min_i x_i=0\}.
\tag{1.1}
\]

For `0<=m<=floor(b/q)`, let `s_m=b-mq`.  Subtracting `m` from every
coordinate gives a bijection

\[
 \{[x]\in\mathcal N_{q,b}:\min_i x_i=m\}
 \longleftrightarrow
 \partial\mathcal N_{q,s_m}.
\tag{1.2}
\]

Thus the vertex set is the disjoint union of its minimum-coordinate shells.
An edge either stays in one shell or joins two consecutive shells: one move
can increase the minimum only when it fills the unique zero and leaves every
other residual coordinate positive.

## 2. The universal radial square

Assume `s>=q+2`.  In the outer boundary shell define

\[
\begin{aligned}
 A_s&=[0,\underbrace{1,\ldots,1}_{q-2},s-q+2],\\
 B_s&=[0,\underbrace{1,\ldots,1}_{q-3},2,s-q+1].
\end{aligned}
\tag{2.1}
\]

In the next inner boundary shell, of mass `s-q`, define

\[
\begin{aligned}
 C_{s-q}&=[\underbrace{0,\ldots,0}_{q-1},s-q],\\
 D_{s-q}&=[\underbrace{0,\ldots,0}_{q-2},1,s-q-1].
\end{aligned}
\tag{2.2}
\]

All four displayed classes are distinct in the stated range.

### Theorem 2.1 (radial square)

For every shell offset `m`, the four vertices

\[
 m\mathbf1+A_s,\quad m\mathbf1+B_s,\quad
 (m+1)\mathbf1+C_{s-q},\quad (m+1)\mathbf1+D_{s-q}
\]

span the cycle

\[
 A_s-B_s-D_{s-q}-C_{s-q}-A_s,
\tag{2.3}
\]

where the first and third edges lie within their respective shells and the
other two are radial edges between consecutive shells.

#### Proof

The edge `A_s B_s` moves one unit from the last coordinate to the preceding
coordinate.  The edge `C_(s-q) D_(s-q)` does the same in the inner shell.

Moving one unit from the last coordinate of `A_s` into its zero gives

\[
 (1,1,\ldots,1,s-q+1)
 =\mathbf1+(0,\ldots,0,s-q),
\]

which is the radial edge `A_s C_(s-q)`.  The same move applied to `B_s`
gives

\[
 (1,1,\ldots,1,2,s-q)
 =\mathbf1+(0,\ldots,0,1,s-q-1),
\]

which is `B_s D_(s-q)`.  Adding the common shell offset `m` changes none of
these unit-transfer identities.  `square`

The cases `s-q=1` and `s-q=2` have the familiar terminal degeneracies: in
the first case the two inner endpoints coincide, while in the second they
form the terminal boundary edge.  They are handled by a one-vertex or
one-edge path insertion, exactly as in the proved three-slot construction.

## 3. Cycle splice

### Theorem 3.1 (protected-shell cycle reduction)

Fix `q`.  Suppose that, for every residual mass `s` occurring in the shell
sequence and satisfying `s>=q+2`, the boundary graph
`\partial\mathcal N_{q,s}` has a Hamilton cycle containing the two protected edges

\[
 A_sB_s
 \quad\hbox{and}\quad
 C_sD_s,                                           \tag{3.1}
\]

where `C_s=[0^(q-1),s]` and `D_s=[0^(q-2),1,s-1]`.  Require the two edges
to be distinct except in the explicitly handled terminal shells.

Suppose also that the finitely many terminal boundary shells admit the
corresponding one-vertex/one-edge protected path insertion.  Then
`G_(q,b)` has a Hamilton cycle whenever it has at least three vertices.

#### Proof

Start with the innermost shell.  Inductively assume all shells below the
current outer shell have already been spliced into one cycle containing
the protected entry edge `C_(s-q)D_(s-q)` of its current outermost shell.

Delete the outer edge `A_sB_s` and the inner edge
`C_(s-q)D_(s-q)`, and insert the two radial edges from Theorem 2.1.  This is
the standard two-edge splice of two disjoint cycles into one cycle.  Repeat
outward through all minimum shells.  The new outer shell's entry edge
`C_sD_s` was not used and remains available for the next stage.  The
terminal degeneracies are inserted as paths instead of cycles.  Every
vertex lies in exactly one shell by (1.2), so the final cycle is spanning.
`square`

The theorem is deliberately stated as a reduction: for `q=3` the boundary
shell is the explicit cycle proved in the three-slot theorem, so it recovers
that construction.  For `q>=4`, the protected higher-dimensional boundary
cycle is the unresolved statement.

## 4. Matching-only version

Hamilton cycles are stronger than the PBBS application needs.  The same
radial square gives the exact weaker interface.

Write `A,B` for the two inner-facing sockets and `C,D` for the two
outer-facing sockets of one shell, with radial pairs `A_new--C_old` and
`B_new--D_old`.  Call the shell **radially flexible** when the following
perfect matchings exist.

* If the shell order is even: the shell itself, and each of

\[
 H-\{A,C\},\quad H-\{A,D\},\quad
 H-\{B,C\},\quad H-\{B,D\}                         \tag{4.1}
\]

has a perfect matching.
* If the shell order is odd: each of

\[
 H-A,\quad H-B,\quad H-C,\quad H-D                 \tag{4.2}
\]

has a perfect matching.

Here deleting an outer-facing socket exports a monomer to the next shell;
deleting an inner-facing socket means that it was consumed by the radial
edge from the preceding shell.

### Corollary 4.1 (parity-socket propagation)

If every boundary shell is radially flexible, then the union of all
shells has a matching of deficiency at most one.  The unmatched vertex, if
forced by global parity, may be prescribed at the outermost surviving
socket.

#### Proof

Process the shells from inside out, maintaining the invariant that an even
accumulated block is perfectly matched, while an odd accumulated block has
exactly one exported monomer, at either one of its two outer-facing
sockets.

With no incoming monomer, use the shell matching itself when its order is
even, and use `H-C` or `H-D` when its order is odd.  With an incoming
monomer at `C_inner` (respectively `D_inner`), consume it by the radial edge
to `A` (respectively `B`).  If the new shell is odd, use `H-A` or `H-B` and
close the accumulated block.  If the new shell is even, use one of the
two-vertex deletions in (4.1), thereby exporting exactly one of `C,D`.
These are all four parity cases.  Hence the invariant persists and no
second monomer is ever created.  `square`

This formulation separates the two genuine requirements:

1. parity-optimal matching inside one boundary shell;
2. entry/exit flexibility at the four explicitly named radial sockets.

An unrooted assertion that a shell merely has *some* near-perfect matching
is not enough for the induction.

## 5. Independent shell matching has unbounded aggregate defect

Let

\[
 N_q(s)=|\mathcal N_{q,s}|,
 \qquad
 L_q(s)=|\partial\mathcal N_{q,s}|.
\]

Deleting one unit from every coordinate gives

\[
                         L_q(s)=N_q(s)-N_q(s-q),       \tag{5.1}
\]

with the second term zero for `s<q`.  When `q` is odd, Burnside parity
gives

\[
 N_q(s)\equiv {q+s-1\choose s}\pmod2.                \tag{5.2}
\]

Along one shell sequence put `p_m=N_q(b-mq) mod 2` and set `p_(M+1)=0`
after the terminal shell.  Equation (5.1) becomes the exact telescoping
law

\[
 |\partial\mathcal N_{q,b-mq}|
 \equiv p_m+p_{m+1}\pmod2.                           \tag{5.3}
\]

Thus odd shell sockets are precisely the transition points of one binary
parity word.  They occur in consecutive pairs, apart from the single
endpoint forced by the total parity.  Radial flexibility is the physical
statement that transports a monomer through the intervening even shells
and cancels each such pair.

Already for `q=3`, Lucas' theorem says that `N_3(s)` is odd exactly when
`s=0` or `1 mod 4`.  Equation (5.1) consequently gives, for `s>=3`,

\[
                         L_3(s)\equiv s\pmod2.         \tag{5.4}
\]

The shell sequence `b,b-3,b-6,...` alternates parity.  Hence among its
first `M+1=floor(b/3)+1` shells, at least `floor((M+1)/2)` have odd order.
Any matching constrained to stay inside individual shells therefore leaves
an unbounded number of monomers, even though the full three-slot graph has
a Hamilton cycle.

Thus the radial splice is not optional bookkeeping.  A theorem giving one
near-perfect matching independently in every shell does **not** imply a
global bounded defect; the unmatched sockets must be correlated through
the radial edges.

## 6. Complement duality and exact open shell

Under the binary encoding, `\partial\mathcal N_{q,s}` is the set of fixed-content
binary necklaces containing an adjacent separator pair `00`.  Binary
complementation carries it to the subset of `G_(s,q)` containing an
adjacent `11`.  Thus complement duality preserves the protected-shell
nature of the problem but does not turn the boundary shell into a full
lower-dimensional necklace graph.

The exact remaining theorem is therefore:

> **Protected adjacent-necklace shell theorem.**  For odd `q`, every
> boundary shell `\partial\mathcal N_{q,s}` is radially flexible at the two
> protected entry/exit edges in (3.1), or admits an equivalent bounded
> protected interface that composes through the radial square.

This is strictly sharper than asking for an arbitrary near-perfect matching
of the whole graph, and it is exactly what a subtractive-Euclidean
shell/splice proof must establish.

## 7. Scope

Proved:

1. the exact minimum-shell decomposition;
2. a literal radial square between every two consecutive nonterminal
   shells;
3. Hamilton and near-perfect splice implications from protected shell
   interfaces.

Not proved:

1. protected matching flexibility of every higher-dimensional boundary
   shell;
2. the full adjacent-necklace near-perfect theorem;
3. simultaneous marked-port/q2-halo separation in the PBBS lift;
4. any global `nu(k)<=B(k)+O(1)` consequence.
