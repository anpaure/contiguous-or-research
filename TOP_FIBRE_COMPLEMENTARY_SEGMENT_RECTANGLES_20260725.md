# Complementary-segment rectangles in growing top fibres

Date: 2026-07-25

Pure mathematics only. No computation, search, solver, or external
rounding theorem is used.

## 0. Verdict

Let

\[
 M=m+H,
 \qquad H\sim\sqrt{m\log m},
 \qquad Q=o(H),
\]

and consider the hard interval lengths

\[
 \mathcal L_Q=\{m-q,m+q:0\le q\le Q\}.
 \tag{0.1}
\]

The naive four-order rectangle cannot be deployed by putting two full
diagonal packets on half of the tops and zero packets on the rest. The two
diagonal orders differ by only two adjacent swaps, so their owner sets
have intersection at least (M-4). Such a (0/2) deployment covers at
most

\[
 \frac{M+4}{2}N_H=(1/2+o(1))W
\]

distinct middle owners.

There is, however, a valid low-overlap deployment.

* At every top use two cyclic promotion segments rather than two full
  packets.
* Their phase sets cover the whole phase circle and overlap only in two
  neighborhoods of total size (O(Q)).
* Put the two diagonal orders on these complementary segments.

The resulting two paths have (M+O(Q)) positions, cover at least (M-4)
distinct owners, and admit an exact rank-isolating rectangle switch on the
whole hard band. The switch preserves the middle-owner multiplicity vector
exactly and changes only one chosen lower or upper rank.

The attainable rank-(r) rectangle vectors generate the full integral
kernel of the point-incidence map. Thus there is no parity or finite-index
lattice obstruction: total coordinate marginals are the only linear
invariants at one rank.

What remains is positivity and abundance. The rectangle theorem is a
final-absorber mechanism after a near-transversal has already been built.
It does not by itself construct that near-transversal or show that a
bounded number of available top rectangles realizes every small residual.

## 1. The full-packet diagonal is unusable

Fix a top (U) and a cyclic order (\pi_{00}). Let (\pi_{10}) be
obtained by one adjacent swap, (\pi_{01}) by a disjoint adjacent swap,
and (\pi_{11}) by both swaps.

At any fixed proper interval length, one adjacent swap changes exactly two
members of the interval family. In particular, at owner length (m),

\[
 |\mathcal P(U,\pi_{00})\cap\mathcal P(U,\pi_{11})|
 \ge M-4.
 \tag{1.1}
\]

Therefore the two diagonal packets together contain at most (M+4)
distinct owners. If only (N_H/2) tops are doubled, their total distinct
owner capacity is at most

\[
 (M+4)N_H/2=(1/2+o(1))W.
 \tag{1.2}
\]

Allowing missing top tags does not repair this loss. Full diagonal packets
are useful only as a formal signed trade, not as a primary (0/2)
selection.

## 2. Exact four-order interval rectangle

Write one cyclic order as

\[
 x_0,x_1,\ldots,x_r,x_{r+1},\ldots,x_{M-1},
\]

and swap the disjoint adjacent pairs

\[
 (a,b)=(x_0,x_1),
 \qquad(c,d)=(x_r,x_{r+1}),
 \tag{2.1}
\]

where (2\le r\le M-2). Let (v_\ell(\pi)) be the integer incidence
vector of the cyclic length-(\ell) interval family of (\pi), and put

\[
 \Delta_\ell
 =v_\ell(\pi_{00})+v_\ell(\pi_{11})
  -v_\ell(\pi_{10})-v_\ell(\pi_{01}).
 \tag{2.2}
\]

### Theorem 2.1 (rank isolation)

One has

\[
 \boxed{\Delta_\ell=0
 \quad\text{unless}\quad
 \ell\in\{r,M-r\}.}
 \tag{2.3}
\]

Put

\[
 C=\{x_2,\ldots,x_{r-1}\},
 \qquad
 D=\{x_{r+2},\ldots,x_{M-1}\}.
\]

At the two exceptional lengths,

\[
 \boxed{
 \Delta_r
 =e_{Cbc}+e_{Cad}-e_{Cac}-e_{Cbd},}
 \tag{2.4}
\]

and

\[
 \boxed{
 \Delta_{M-r}
 =e_{Dad}+e_{Dbc}-e_{Dbd}-e_{Dac}.}
 \tag{2.5}
\]

Here concatenation denotes adjoining the displayed labels to the common
core.

#### Proof

For one interval to be sensitive to the first swap, exactly one of
(x_0,x_1) must lie in it. Thus one interval boundary is the cut between
those two positions. Sensitivity to the second swap similarly forces the
other interval boundary to be the cut between (x_r,x_{r+1}). The two
arcs between these cuts have lengths (r) and (M-r), proving (2.3).

On the first arc, the four orders give respectively

\[
 Cbc,\quad Cac,\quad Cbd,\quad Cad,
\]

with signs in (2.2), proving (2.4). The complementary arc gives (2.5).
\(\square\)

For (r=m-q), the complementary length is (H+q); for (r=m+q), it
is (H-q). When (q\le Q=o(H)), neither complementary length belongs to
the central hard band (0.1). Hence (2.4) isolates lower depth (q), and
the choice (r=m+q) isolates upper depth (q).

## 3. Phase support of one adjacent swap

Index packet phases by their interval starting positions. For the first
swap (x_0\leftrightarrow x_1), a length-(\ell) interval changes only at
the two starts

\[
 1,qquad 1-\ell\pmod M.
 \tag{3.1}
\]

As (\ell) ranges over (0.1), all sensitive phases lie in

\[
 \mathcal S_A
 =\{1\}
 \cup[H+1-Q,H+1+Q]pmod M.
 \tag{3.2}
\]

Thus (\mathcal S_A) is the union of two cyclic neighborhoods with total
size at most (2Q+2).

### Lemma 3.1 (two complementary cyclic segments)

There are two cyclic intervals of phases (P_0,P_1\subseteq\mathbb Z_M)
such that

\[
 P_0\cup P_1=\mathbb Z_M,
 \qquad
 \mathcal S_A\subseteq P_0\cap P_1,
 \qquad
 |P_0\cap P_1|=O(Q).
 \tag{3.3}
\]

#### Proof

Take disjoint short cyclic arcs around the two components in (3.2). The
complement consists of two open arcs. Let (P_0) join the short arcs
through the first complementary arc and let (P_1) join them through the
second. Both are cyclic intervals, their union is the circle, and their
intersection is exactly the two chosen short arcs. \(\square\)

Every (P_i) is a contiguous phase segment, hence gives one legal
promotion path.

## 4. The exact complementary-segment trade

Define the initial two-path system at (U) by

\[
 \mathscr A_0
 =\pi_{00}|_{P_0}\ \sqcup\ \pi_{11}|_{P_1},
 \tag{4.1}
\]

and the switched system by

\[
 \mathscr A_1
 =\pi_{10}|_{P_0}\ \sqcup\ \pi_{01}|_{P_1}.
 \tag{4.2}
\]

### Theorem 4.1 (restricted segments recover the full rectangle)

For every hard length (\ell\in\mathcal L_Q), the interval-load
difference between (4.1) and (4.2) is exactly (\Delta_\ell) from
(2.2). Consequently:

1. choosing (r=m-q) changes only the lower depth-(q) load vector;
2. choosing (r=m+q) changes only the upper depth-(q) load vector;
3. for every (q\ge1), the middle-owner load vector is preserved exactly;
4. all other hard lower and upper rows are preserved exactly.

#### Proof

The difference is

\[
 [v_{\ell,P_0}(\pi_{00})-v_{\ell,P_0}(\pi_{10})]
 +[v_{\ell,P_1}(\pi_{11})-v_{\ell,P_1}(\pi_{01})].
 \tag{4.3}
\]

Both brackets are changes under the first adjacent swap, without and with
the second swap respectively. Every phase sensitive to the first swap at
a hard length lies in (P_0\cap P_1) by (3.2)--(3.3). Hence restricting
to (P_0,P_1) deletes no nonzero term from either bracket. Equation
(4.3) is therefore the full mixed difference (2.2).

The conclusions follow from Theorem 2.1 and the fact that, for (q\ge1),
neither (m) nor any other hard length equals (r) or (M-r).
\(\square\)

## 5. Owner capacity and reset cost

Each two-path system has

\[
 |P_0|+|P_1|=M+O(Q)
 \tag{5.1}
\]

state positions. It also contains at least (M-4) distinct middle owners.
Indeed, choose one path's owner at every phase in
(P_0\cup P_1=\mathbb Z_M). Relative to the full packet of
(\pi_{00}), the resulting one-owner-per-phase family differs only at the
at most four phases sensitive to the two adjacent swaps at length (m).
All other (M-4) owners remain distinct.

Using such a system at every top gives

\[
 MN_H+O(QN_H)=W+o(W)
 \tag{5.2}
\]

positions, because (QN_H=O(QW/m)=o(W)). Two path initializations per top
cost

\[
 O(HN_H)=o(W).
 \tag{5.3}
\]

Thus the complementary-segment rectangle has no analogue of the fatal
half-capacity loss in (1.2). Cross-top owner collisions are still a
separate near-transversal problem, but the local deployment itself is
asymptotically lossless.

## 6. Exact rectangle lattice and parity audit

For (2\le r\le n-2), let

\[
 A_r:\mathbb Z^{\binom{[n]}r}\longrightarrow\mathbb Z^n,
 \qquad A_re_S=\mathbf1_S,
 \tag{6.1}
\]

be the point-incidence map. Let (L_{n,r}) be generated by all rectangle
vectors

\[
 \rho(C;a,b,c,d)
 =e_{Cac}+e_{Cbd}-e_{Cad}-e_{Cbc},
 \tag{6.2}
\]

where (|C|=r-2) and (a,b,c,d) are distinct outside (C).

### Theorem 6.1 (no hidden lattice obstruction)

\[
 \boxed{L_{n,r}=\ker_{\mathbb Z}A_r.}
 \tag{6.3}
\]

In particular there is no parity or finite-index obstruction beyond the
coordinate marginals.

#### Proof

The inclusion (L_{n,r}\subseteq\ker A_r) is immediate. We prove the
reverse inclusion by induction on (n), for fixed (r).

At (n=r+1), the columns are the complements of the singletons. Their
incidence matrix is (J-I), which is nonsingular, so the kernel is zero.

Let (n\ge r+2), and split (z\in\ker A_r) according to whether a block
contains (n). Identify the containing-(n) part with an integer vector
(z_1) on the ((r-1))-subsets of ([n-1]). The coordinate-(n)
equation says

\[
 \sum_Pz_1(P)=0.
 \tag{6.4}
\]

The Johnson graph on these ((r-1))-sets is connected, so (z_1) is an
integer sum of edge differences

\[
 e_{C+y}-e_{C+z},
 \qquad |C|=r-2.
 \tag{6.5}
\]

For every such difference choose

\[
 x\in[n-1]\setminus(C\cup\{y,z\}),
\]

which is possible because (n\ge r+2). The rectangle with core (C)
and labels (n,x,y,z) has containing-(n) part exactly (6.5), up to
sign. Subtracting integer combinations of these rectangles kills (z_1).

The remaining vector is supported on the (r)-sets of ([n-1]) and is
still in the point-incidence kernel. By induction it belongs to
(L_{n-1,r}\subseteq L_{n,r}). This proves (6.3). \(\square\)

For every hard interval rank (r=m\pm q), (q\le Q), every generator
(6.2) is realizable by Theorem 2.1: choose a filler set of size

\[
 M-r-2\ge0
\]

and arrange the four special labels at the two boundaries separated by
(r). Since (Q=o(H)), this filler size is positive for all sufficiently
large (m).

Thus the complementary-segment switches generate exactly every signed
rank-(r) correction which preserves point marginals.

## 7. What remains: positivity and multi-rank availability

Theorem 6.1 is a signed lattice theorem, not an absorber theorem. Three
issues remain.

1. A desired load correction must have the same coordinate marginals as
   the current load. Rectangle switches cannot change those marginals.
2. An integer representation by rectangles need not admit an ordering in
   which every intermediate two-segment system remains selected with
   nonnegative multiplicity.
3. A bounded supply of tops must realize the rectangles simultaneously at
   all hard ranks. The induction in Theorem 6.1 gives no useful bound on
   the number of generators or on top reuse.

Accordingly, the proved role of these rectangles is as a final absorber:
after a primary construction leaves a point-compatible residual of total
size (o(W)), use rank-isolating complementary-segment switches to remove
it without reopening the middle or the other controlled ranks.

To make this effective at Catalan scale, one needs a quantitative positive
version, for example:

> every point-balanced rank-(r) residual of total variation
> (O(N_H)) is realizable by (O(N_H)) available complementary-segment
> rectangles, with bounded top reuse, while preserving the
> near-transversal owner property.

No such positive bounded-generation theorem is proved here. The exact
advances are the asymptotically lossless segment deployment, perfect
rank isolation on the hard band, and the absence of any parity/lattice
obstruction.

