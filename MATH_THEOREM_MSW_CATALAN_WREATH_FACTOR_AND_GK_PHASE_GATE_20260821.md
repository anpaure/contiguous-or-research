# The MSW Catalan factor is an exact wreath bank, but not a canonical GK phase bank

## 1. Outcome and scope

Put
\[
        b=2m+1,
        \qquad N=\binom bm,
        \qquad C_m={1\over m+1}\binom{2m}{m}={N\over b}.       \tag{1.1}
\]
The base cycle factor used in the Mütze--Standke--Wiechert
Chung--Feller construction, and subsequently in the
Mütze--Nummenpalo--Walczak odd-graph Hamilton construction, is exactly a
partition of \(\binom{[b]}m\) into \(C_m\) cyclic-interval wreaths.
There is no approximate central packing gate.

Taking independent copies of this bank on the two local coordinate
shores gives an exact product partition of every central source pair into
\(C_m^2\) disjoint \(b\times b\) wreath grids.  This is an unconditional
positive central-order bank.

However, under the canonical coordinate identification with the
alternating Greene--Kleitman order
\(A_0,B_0,A_1,B_1,\ldots,A_{b-1},B_{b-1}\), almost every antidiagonal
phase of those grids mixes the two GK orientations, and an even smaller
family is monochromatic and survives two upper steps.  Exact enumeration
through \(b=13\) shows that no product block supplies the phase capacity
needed even at \(H=2\), including after an optimistically independent
choice of reversal for every *pair* of wreaths.

Thus the MSW factor closes central source/target packing, but it does not
by itself coinstantiate the already-proved longest-top GK retirement
selection.  Global conjugation of the whole MSW banks, trades between
wreaths, and assignments which split and recombine antidiagonals remain
open; the finite phase census below does not rule them out.

## 2. Every minimum odd cycle is a wreath

Let
\[
        S_0,S_1,\ldots,S_{b-1},S_b=S_0                   \tag{2.1}
\]
be a \(b\)-cycle in \(KG(b,m)\).  Label its \(i\)-th edge by the unique
omitted coordinate
\[
        q_i=[b]\setminus(S_i\cup S_{i+1}).                    \tag{2.2}
\]
For a coordinate \(q\), let \(t_q\) be its multiplicity in the word
\((q_0,\ldots,q_{b-1})\).  At every edge not labelled \(q\), membership
of \(q\) toggles; at an edge labelled \(q\), both endpoints omit it.
Returning to the initial incidence bit around an odd cycle gives
\[
        b-t_q\equiv0\pmod2.                                   \tag{2.3}
\]
Hence every nonzero \(t_q\) is odd.  Since there are \(b\) coordinates
and \(\sum_qt_q=b\), every coordinate occurs exactly once.

The recurrence
\[
        S_{i+1}=[b]\setminus(S_i\cup\{q_i\})                  \tag{2.4}
\]
now has the cyclic solution
\[
        S_i=\{q_{i+1},q_{i+3},\ldots,q_{i+2m-1}\}.            \tag{2.5}
\]
Because multiplication by two permutes \(\mathbb Z_b\), the sets in
(2.5) are precisely the \(m\)-windows of the cyclic order
\[
        (q_0,q_2,q_4,\ldots)                                  \tag{2.6}
\]
with subscripts modulo \(b\).  Conversely, the windows of any cyclic
order satisfy (2.4) and form a \(b\)-cycle in the odd graph.  Therefore
minimum odd cycles and wreaths are the same objects.

## 3. The MSW omitted-label word

For a Dyck word \(x\) of semilength \(m\), the MSW path uses balanced
states \(x_i\), one-step upper states \(y_i=g(x_i)\), and
\(x_{i+1}=h(y_i)\).  Let \(a_i\) be the bit inserted by \(g\) and
\(b_i\) the bit deleted by \(h\).  With the extra coordinate denoted
\(\infty\), the associated odd-graph cycle is
\[
 (x_0,\widetilde y_0,x_1,\widetilde y_1,ldots,
       x_{m-1},\widetilde y_{m-1},x_m),                        \tag{3.1}
\]
where
\(\widetilde y_i=([2m]\setminus y_i)\cup\{\infty\}\) and
\(x_m=[2m]\setminus x_0\).

The two edges around \(\widetilde y_i\) omit \(a_i\) and \(b_i\),
respectively, while the closing edge omits \(\infty\).  Thus its omitted
word is exactly
\[
 q(x)=(a_0,b_0,a_1,b_1,\ldots,a_{m-1},b_{m-1},\infty)
      =(\pi(x),\infty).                                       \tag{3.2}
\]
By Section 2, a cyclic wreath order for this cycle is obtained by reading
the even positions of (3.2).  The equivalent implementation used by the
checker reads \(q_{-1},q_{-3},q_{-5},\ldots\); this differs only by a
cyclic shift and reversal.

The MSW paths indexed by the \(C_m\) Dyck words are vertex-disjoint and
cover the odd graph.  Equations (1.1)--(3.2) therefore prove:

**Theorem 3.1 (exact Catalan wreath factor).**  The orders
\(R_x\), one for each Dyck word \(x\), have pairwise disjoint
\(m\)-window decks and
\[
        \bigsqcup_{x\in D_{2m}^0}{\cal I}_m(R_x)
          =\binom{[b]}m.                                      \tag{3.3}
\]

This is the precise equivalence between the MSW/MNW base factor and an
exact central wreath decomposition.

## 4. Exact central product bank

The complement of an \(m\)-window in a \((2m+1)\)-cycle is an
\((m+1)\)-window of the same unoriented circle.  Complementing (3.3)
therefore also gives a partition of \(\binom{[b]}{m+1}\).

Take one copy of the factor on coordinates \(A\) and one on coordinates
\(B\).  For \(x,z\in D_{2m}^0\), write
\[
 X_i={\cal I}_m(R_x;i),\qquad
 Y_j={\cal I}_{m+1}(R_z;j).                                  \tag{4.1}
\]
Then the grids
\[
        \{(X_i,Y_j):i,j\in\mathbb Z_b\},
        \qquad (x,z)\in(D_{2m}^0)^2,                          \tag{4.2}
\]
partition all
\(N^2\) middle sources of split \((m,m+1)\).  Within a grid, the
antidiagonals
\[
        \Phi_p(x,z)=\{(X_i,Y_{p-i}):i\in\mathbb Z_b\},
        \qquad p\in\mathbb Z_b,                               \tag{4.3}
\]
partition its \(b^2\) cells.  All source and central-target collisions are
therefore absent before any upper-chain interpretation is imposed.

## 5. The exact GK phase test

For a cell \((X,Y)\) of (4.2), read its balanced binary word in the
interleaved coordinate order
\[
        A_0,B_0,A_1,B_1,\ldots,A_{b-1},B_{b-1}.                \tag{5.1}
\]
Give a present coordinate step \(+1\) and an absent coordinate step
\(-1\).  If \(h_t\) is the prefix height, put
\[
        k(X,Y)=-\min_t h_t.                                   \tag{5.2}
\]
This is exactly the top excess of the Greene--Kleitman chain containing
\((X,Y)\).  Its first upper step is on the \(A\)-side exactly when
\(k(X,Y)\) is odd.

Consequently a whole phase (4.3) can serve as a persistent height-\(H\)
GK packet only if

1. all \(b\) values \(k(X_i,Y_{p-i})\) have the same parity; and
2. their minimum is at least \(H\).

Matching the phase parity to the half-step type word is an additional
restriction.  The checker first counts phases satisfying only conditions
1--2, so its persistent counts are upper bounds for correctly typed
physical phases.

At the central split \(|2m-b|=1\), the affine capacity used by the
integral GK theorem requires
\[
 n_m=\left\lfloor{b-H+1\over2}\right\rfloor                  \tag{5.3}
\]
phases of each orientation, hence \(2n_m\) phases in each complete
product block if it is to be used without splitting.

## 6. Exact finite phase census

For \(H=2\), the canonical MSW labels give the following exact counts.
`mono` counts all orientation-monochromatic phases, even those retiring
before height two.  `persistent` imposes both conditions in Section 5.
The last two columns allow each *pair* of wreaths to choose its two
reversal bits independently and hence form an optimistic upper bound on
what any globally consistent reversal assignment can achieve.

\[
\begin{array}{c|c|r|r|r|r|r|r|r}
m&b&C_m^2&\sum\!\mathrm{mono}&\sum\!\mathrm{persistent}
 &\max\mathrm{persistent}&2n_m
 &\sum\!\mathrm{persistent}_{\rm rev}
 &\max\mathrm{persistent}_{\rm rev}\\ \hline
2&5&4&2&0&0&4&0&0\\
3&7&25&9&0&0&6&0&0\\
4&9&196&57&3&1&8&5&1\\
5&11&1764&399&41&2&10&67&2\\
6&13&17424&3068&380&2&12&666&2
\end{array}                                                    \tag{6.1}
\]

In every row of (6.1), **zero** product blocks have the \(2n_m\)
persistent phases required by (5.3), even under the pairwise-reversal
upper bound.  For example, at \(b=13\) the canonical factor has only 380
persistent phases across all 17,424 blocks, versus
\(12\cdot17{,}424\) required by the unsplit block compiler.  Correct
half-step colours can only reduce that supply.

The finite statement is exact, but it is deliberately scoped.  Rotating
a wreath only shifts phase names and does not alter these counts; reversal
is already upper-bounded.  The checker does not optimize arbitrary global
coordinate conjugations of the two entire factor banks, nor does it allow
cells from different antidiagonals or different product blocks to be
recombined.  Thus (6.1) refutes only the canonical, whole-antidiagonal
coinstantiation—not the existence of some traded or globally conjugated
MSW compiler.

## 7. Consequence for the proof architecture

The correct separation is now
\[
 \boxed{\text{MSW central wreath factor: exact}}
 \quad\longrightarrow\quad
 \boxed{\text{GK chain-to-whole-phase coinstantiation: open}}.
                                                                    \tag{7.1}
\]
The first box may be used unconditionally, including as a collision-free
central product bank.  The second box cannot be obtained by simply taking
the canonical Dyck orders and the globally longest GK chains phase by
phase.  Any completion must use additional conjugation, wreath trades, or
a reassignment which preserves the exact central bank while changing the
upper-chain phase geometry.
