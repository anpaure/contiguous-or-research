# Adjacent necklaces: the terminal-normal core has an exact internal path-product reduction

**Date:** 2026-08-05  
**Method:** canonical terminal pairing and the odd-group Cartesian
path-product theorem; no computation  
**Status:** unconditional second stage after the terminal-fracture cube
partition. It is vertex-disjoint from that first stage. It perfectly
matches every residual fibre except one explicit shifted-quiet necklace
when all local path lengths are odd.

## 1. Input from the terminal-fracture theorem

Fix an odd coordinate length \(q\). First match every nontrivial fibre of
the terminal normal form

\[
       (P,n-1,1,0^g)\longleftrightarrow(P,n,0^{g+1}).
                                                        \tag{1.1}
\]

The exact residual \(t=0\) necklaces have only the following positive
macroblocks.

* A **unit block** is

\[
                            (1,0^g),\qquad g\ge1.       \tag{1.2}
\]

* A **long block** is

\[
              (a_1,\ldots,a_\ell,0),\qquad
              \ell\ge2,\quad a_i\ge1,\quad a_\ell\ge2.
                                                        \tag{1.3}
\]

Indeed a zero gap of length at least two can follow only a singleton one,
while every nonsingleton positive run has zero gap exactly one and terminal
value greater than one.

## 2. Canonical pairs inside a long block

Pair the positive coordinates of (1.3) backwards from its terminal end:

\[
 (a_{\ell-1},a_\ell),\
 (a_{\ell-3},a_{\ell-2}),\ldots .                    \tag{2.1}
\]

If \(\ell\) is odd, leave \(a_1\) unpaired. The first pair in (2.1) is
called the **terminal pair**; all others are **ordinary pairs**.

For the terminal pair fix its sum \(n\). Because its second coordinate must
remain at least two, its complete allowed allocation set is

\[
                  (n-b,b),\qquad 2\le b\le n-1.      \tag{2.2}
\]

It induces the path \(P_{n-2}\).

For an ordinary pair fix its sum \(m\). Its complete positive allocation
set is

\[
                  (m-b,b),\qquad 1\le b\le m-1,      \tag{2.3}
\]

and induces the path \(P_{m-1}\).

Changing \(b\) by one is one literal adjacent chip transfer. Every state in
(2.2)--(2.3) retains the same positive-run length and zero skeleton.
Moreover the terminal value stays at least two and its following zero gap
stays one. Hence every such edge remains inside the \(t=0\) core.

## 3. Exact collision-free fibres

Fix the following cyclic data:

1. the sequence of unit and long macroblocks and all macroblock lengths;
2. every zero-gap length;
3. every free first coordinate in an odd-length long block;
4. the sum of every pair in (2.1); and
5. the distinction between terminal and ordinary pair roles.

Let the resulting path lengths be \(r_1,\ldots,r_s\), where

\[
 r_i=
 \begin{cases}
  n_i-2,&i\text{ is terminal},\\
  m_i-1,&i\text{ is ordinary}.
 \end{cases}                                        \tag{3.1}
\]

### Lemma 3.1 (literal fibre)

Before taking rotations, the states with the fixed data above form exactly

\[
                         P_{r_1}\square\cdots\square P_{r_s}.
                                                        \tag{3.2}
\]

Distinct fixed data give disjoint fibres, and their union is the complete
\(t=0\) core.

#### Proof

The positive-run and zero-gap skeleton is intrinsic in every \(t=0\) state.
Pairing backwards from a terminal coordinate is therefore canonical.
The free coordinates and pair sums are then read uniquely from the state.
Conversely, arbitrary choices from (2.2) and (2.3) reconstruct one and
only one state with those data. All choices are independent because the
pairs are disjoint. This proves (3.2), disjointness, and exhaustion.
\(\square\)

Let \(H\le C_q\) be the rotational stabilizer of the fixed cyclic data. It
permutes equal path factors of equal role and size. Since \(q\) is odd,
\(|H|\) is odd.

### Lemma 3.2 (necklace fibre)

The corresponding necklace fibre is exactly

\[
                (P_{r_1}\square\cdots\square P_{r_s})/H.
                                                        \tag{3.3}
\]

#### Proof

If two labelled states with the fixed data are rotations of one another,
that rotation stabilizes the data and hence lies in \(H\). The converse is
immediate. Every product-path edge is a literal adjacent transfer by
Section 2. \(\square\)

## 4. Matching and the exact critical state

The odd-group Cartesian-path-quotient theorem applied to (3.3) gives a
matching of deficiency at most one. Here its critical state can be made
fully explicit.

Orient each odd terminal path so that its isolated endpoint is \(b=2\).
Orient each odd ordinary path so that its isolated endpoint is \(b=1\).
Pair the remaining consecutive allocations in each path. The graded
tensor Dirac operator for these local pairings has:

* zero kernel if some \(r_i\) is even;
* a one-dimensional kernel, supported on the tensor of the displayed
  isolated endpoints, if every \(r_i\) is odd.

The critical tensor is fixed by \(H\). On the invariant orbit space its
complementary block remains nonsingular, since the inverse commutes with
\(H\). A Pfaffian term therefore matches every other orbit.

### Theorem 4.1 (exact second-stage reduction)

Every \(t=0\) fixed-data necklace fibre containing at least one long block
is perfectly matched unless both of the following hold:

1. every terminal pair sum \(n_i\) is odd;
2. every ordinary pair sum \(m_i\) is even.

In that exceptional case there is a matching missing exactly the one
necklace in which

\[
\begin{array}{ll}
\text{each terminal pair is}&(n_i-2,2)
                              =(\text{odd},2),\\[1mm]
\text{each ordinary pair is}&(m_i-1,1)
                              =(\text{odd},1).
\end{array}                                           \tag{4.1}
\]

If there are no long blocks, the fibre is the singleton all-unit
necklace built only from \((1,0^g)\) macroblocks.

#### Proof

A terminal factor has odd order precisely when \(n_i-2\) is odd,
equivalently when \(n_i\) is odd. An ordinary factor has odd order
precisely when \(m_i-1\) is odd, equivalently when \(m_i\) is even. If any
factor order is even, the path-product quotient theorem gives a perfect
matching.

When all are odd, the preceding tensor construction isolates exactly the
state (4.1) and is nonsingular on its complement, including after taking
\(H\)-invariants. Its Pfaffian gives the claimed matching. The number of
orbit vertices is odd because both the product order and every \(H\)-orbit
size are odd, so one unmatched vertex is also necessary. With no path
factors at all, Lemma 3.1 gives the stated singleton. \(\square\)

## 5. Shifted-quiet critical runs

The exceptional long blocks have a rigid form. Pairing them backwards
from the terminal end, every ordinary pair is \((\text{odd},1)\) and the
terminal pair is \((\text{odd},2)\). Thus an even-length critical run is

\[
       (o_1,1,o_2,1,\ldots,o_{h-1},1,o_h,2),
       \qquad o_i\text{ odd},                         \tag{5.1}
\]

while an odd-length critical run has one arbitrary free coordinate before
the same pattern:

\[
       (a,o_1,1,\ldots,o_{h-1},1,o_h,2).              \tag{5.2}
\]

Each is all-quiet except for the single terminal value two. Its following
zero is isolated. The literal exit

\[
                    (\text{odd},2,0)
              \longleftrightarrow
                    (\text{odd},1,1)                 \tag{5.3}
\]

removes that zero and repairs the local quiet pair, but merges two
macroblocks. Applying (5.3) independently is not yet justified: distinct
merged-run fibres can overlap, exactly as in the naive full-fracture
counterexample. A final alternating-rail or contour theorem must correlate
these exits.

Consequently, after the two disjoint matching stages, the complete
unmatched candidate set consists exactly of:

1. all-unit necklaces, already identified with a strictly smaller
   odd-slot adjacent-necklace graph by the macroblock complement reduction;
   and
2. shifted-quiet necklaces whose every long block has form (5.1) or (5.2).

No general long-run receiver companion remains.

## 6. Scope

Proved:

1. a genuinely disjoint next-stage fibre decomposition inside the
   terminal-normal \(t=0\) core;
2. exact path-product quotient matching in every such fibre;
3. perfect matching whenever one local allocation path has even order;
4. one explicit critical necklace otherwise; and
5. reduction of every long block to one terminal-two defect.

Not proved:

1. collision-free consolidation of the exits (5.3);
2. protected radial socket compatibility of that consolidation;
3. PBBS owner/q2-halo compatibility; or
4. any universal-word upper bound.
