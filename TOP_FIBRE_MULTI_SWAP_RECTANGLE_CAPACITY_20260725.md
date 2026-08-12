# Multi-swap complementary rectangles: macroscopic mass, restricted freedom

Date: 2026-07-25

Pure mathematics only.

## 0. Outcome

The complementary-segment construction can carry a macroscopic **batch**
of rank-isolating rectangles at one top while paying only (O(Q))
duplicated phases.

Take two blocks of disjoint adjacent swaps, each of size

\[
 L\asymp\sqrt M,
\]

with their boundary blocks separated by about (m). Their four-order
mixed difference decomposes into

\[
 \Theta(L^2)=\Theta(M)
\]

elementary rectangles, all supported on hard ranks
(m\pm O(L)\subseteq m\pm[0,Q]). The complementary phase overlap remains
(O(Q)), and each two-segment system retains (M-O(L)) distinct owners.

This does **not** give (Theta(M)) independently selectable rectangle
bits. One four-order trade selects a Cartesian-product batch. With two
segment orders its independent choice dimension is only (O(L)), and a
fixed rank receives only (O(L)) elementary rectangles. More generally,
an overlap of size (R) supports at most (O(R)) elementary
rank-isolating anchors at any one fixed rank.

Thus the mechanism has macroscopic aggregate absorber mass but only
sublinear per-rank capacity. It can eliminate a Catalan/sublinear residual;
it cannot repair a linear hole density concentrated in one shallow rank.

## 1. Two commuting swap blocks

Fix a cyclic order (pi) of a top (U), with phase positions in
(mathbb Z_M). Let

\[
 A_1,\ldots,A_s
\]

be pairwise disjoint adjacent transpositions whose boundaries lie in one
cyclic position interval (I_A) of length (L). Let

\[
 B_1,\ldots,B_t
\]

be pairwise disjoint adjacent transpositions with boundaries in a second
interval (I_B) of length (L). Assume the two position intervals are
disjoint, so all (A_i,B_j) commute. Put

\[
 \alpha=A_1\cdots A_s,
 \qquad
 \beta=B_1\cdots B_t.
 \tag{1.1}
\]

Use the four orders

\[
 \pi_{00}=\pi,quad
 \pi_{10}=\alpha\pi,quad
 \pi_{01}=\beta\pi,quad
 \pi_{11}=\alpha\beta\pi.
 \tag{1.2}
\]

Choose (I_B) to lie at cyclic displacement (m+O(L)) from (I_A).
Then every boundary separation

\[
 r_{ij}=\operatorname{dist}(\partial A_i,\partial B_j)
 \tag{1.3}
\]

belongs to (m+[-O(L),O(L)]).

## 2. One (O(Q))-overlap serves the whole block

For a swap boundary at phase (p), the sensitive starts at hard interval
lengths (m\pm q), (0\le q\le Q), are

\[
 p+1,qquad p+H+1\pm q.
 \tag{2.1}
\]

As (p) ranges over (I_A), their union lies in two cyclic position
intervals of total length

\[
 O(L+Q)=O(Q)
 \tag{2.2}
\]

provided (L\le Q). As in the two-swap construction, choose two cyclic
phase segments (P_0,P_1) covering the phase circle whose intersection
contains (2.2) and has size (O(Q)).

Define

\[
 \mathscr A_0=\pi|_{P_0}\sqcup\alpha\beta\pi|_{P_1},
 \tag{2.3}
\]

and

\[
 \mathscr A_1=\alpha\pi|_{P_0}\sqcup\beta\pi|_{P_1}.
 \tag{2.4}
\]

Every phase sensitive to (alpha) on a hard row lies in both segments.
Therefore the hard-row load difference between (2.3) and (2.4) equals the
full four-order mixed difference

\[
 v(\pi)+v(\alpha\beta\pi)-v(\alpha\pi)-v(\beta\pi).
 \tag{2.5}
\]

## 3. Exact telescoping into elementary rectangles

Write

\[
 \alpha_{<i}=A_1\cdots A_{i-1},
 \qquad
 \beta_{<j}=B_1\cdots B_{j-1}.
\]

### Theorem 3.1 (multi-swap rectangle expansion)

As an identity of interval-incidence vectors,

\[
 \boxed{
 (1-\alpha)(1-\beta)v
 =\sum_{i=1}^s\sum_{j=1}^t
 \alpha_{<i}\beta_{<j}
 (1-A_i)(1-B_j)v.}
 \tag{3.1}
\]

Every summand is an elementary four-order rectangle. Its only exceptional
interval lengths are

\[
 r_{ij},\qquad M-r_{ij}.
 \tag{3.2}
\]

#### Proof

The telescoping identities

\[
 1-\alpha=\sum_i\alpha_{<i}(1-A_i),
 \qquad
 1-\beta=\sum_j\beta_{<j}(1-B_j)
\]

hold without approximation. The two swap blocks commute, so multiplying
the identities gives (3.1). The elementary rank-isolation theorem applied
after the prefix relabeling
(alpha_{<i}\beta_{<j}) gives (3.2). \(\square\)

If (I_B-I_A=m+[-L,L]), then all (r_{ij}) lie in

\[
 m+[-2L,2L].
\]

For (2L\le Q), every first exceptional length is a hard lower or upper
rank, while its complement is outside the central hard band.

Taking alternating boundaries inside blocks of length (L) gives

\[
 s,t=\Theta(L),
 \qquad st=\Theta(L^2).
 \tag{3.3}
\]

With (L\asymp\sqrt M), (3.3) is (Theta(M)).

## 4. Owner and word cost

The products (alpha,eta) use (s+t=O(L)) disjoint adjacent swaps.
At owner length (m), each swap changes only two phase intervals.
Consequently each principal one-owner-per-phase family in (2.3) or (2.4)
differs from the full base packet at only (O(L)) phases. It therefore
contains at least

\[
 M-O(L)
 \tag{4.1}
\]

distinct owners.

The two phase segments have total length

\[
 M+O(Q),
\]

so the duplicated-position toll remains (O(Q)), independent of the
(Theta(L^2)) elementary summands in (3.1). Across all (N_H) tops,

\[
 QN_H=O(QW/m)=o(W),
\]

and two resets per top still cost (O(HN_H)=o(W)).

Thus the multi-swap batch is physically asymptotically lossless.

## 5. Why the summands are not independent choices

For subsets (I\subseteq[s]), (J\subseteq[t]), replacing
(alpha,eta) by

\[
 \alpha_I=\prod_{i\in I}A_i,
 \qquad
 \beta_J=\prod_{j\in J}B_j
\]

selects the Cartesian-product collection (I\times J) of elementary
interactions, with the appropriate prefix relabelings. It does not select
an arbitrary subset of the (st) pairs.

Equivalently, the elementary interaction coefficient matrix supplied by
one four-order system has Boolean rank one. A sum of (p) independent
four-order systems has interaction matrix rank at most (p). An arbitrary
(s\times t) correction can require

\[
 p\ge\min(s,t)=\Theta(L)
 \tag{5.1}
\]

systems. Paying separate resets for that many systems at every top would
cost at least

\[
 \Theta(LHN_H),
\]

which is not (o(W)) when (L\asymp\sqrt m) and
(H\asymp\sqrt{m\log m}).

Thus (3.1) proves macroscopic correction **mass**, but not macroscopic
independent binary freedom.

## 6. Sharp fixed-rank capacity bound

Let (Omega=P_0\cap P_1), with (|\Omega|=R). Consider elementary
rectangle switches whose restricted two-segment implementation uses the
first swap as the duplicated-sensitivity anchor.

For an anchor boundary (p), the length-independent sensitive phase
(p+1) belongs to (Omega). Hence there are at most (R) possible anchor
boundaries. At one prescribed exceptional length (r), the second
boundary is then uniquely (p+r) modulo (M).

### Proposition 6.1

At a fixed isolated rank, a two-segment system with overlap (R) supports
at most

\[
 \boxed{R}
 \tag{6.1}
\]

elementary anchor rectangles, up to reversal of their orientation.

In particular, (R=O(Q)) gives only (O(Q)) elementary correction units
per top at one rank.

This matches the multi-swap grid: for a fixed boundary separation, its
pairs lie on one diagonal of the (s\times t) grid and number only
(O(L)).

Across all tops, the fixed-rank elementary capacity is at most

\[
 O(QN_H)=O(WQ/m)=o(W).
 \tag{6.2}
\]

Therefore complementary-segment rectangles cannot repair a
(Theta(W)) hole density concentrated at depth one or any other single
rank. A primary construction must already leave (o(W)) defect in every
rank. The rectangles can then serve as a sublinear final absorber.

## 7. Exact calibrated conclusion

One top can carry (Theta(M)) elementary rank-isolating rectangle mass at
(O(Q)) duplicated-state cost, by a two-block multi-swap trade. It cannot
carry (Theta(M)) freely and independently selectable rectangle choices
within the same two-segment architecture.

The remaining alternatives are:

1. prove that the residual correction matrices arising from the primary
   near-transversal have bounded/low Boolean rank, so the correlated
   batches in (3.1) suffice;
2. fuse many four-order systems dynamically inside one common-top path,
   avoiding separate resets; or
3. construct genuinely multi-top circuits whose interaction matrices add
   to the required residual while keeping owner collisions (o(W)).

Without one of these additional inputs, the rectangle mechanism is a
macroscopic aggregate absorber but only a sublinear per-rank absorber.

