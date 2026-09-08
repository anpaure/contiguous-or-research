# Audit of the arbitrary-k common-owner Q2 carrier

Date: 2026-07-26

Audited file:
MATH_ATTACK_K_ARBITRARY_K_SEED_COMMON_OWNER_CARRIER_20260726.md.

Method: pure mathematics only.

## Verdict

**PASS.**  Sections 1--6 give a literal arbitrary-\(k\) carrier with exact
one-copy ownership, correct lower and upper affine ledgers, pointwise
disjoint death bits of density \(1/(2k+1)\), and one common phase-compatible
all-length suspension.  No integrality or rank defect is present.

The later packing and phase-balanced tensor operator also pass the checks
needed for the Gaussian implication.  One wording correction is useful:
the menu contains \(kr\) signed bits across \(r\) blocks, but any one
all-new product row changes at most one local pair frame per block and hence
has matching-switch radius at most \(r\), not \(kr\).  Since
\(r\gg\sqrt m\), the intended escape from the old
\(O(\sqrt m)\)-radius ceiling remains valid.

## 1. Common support and exact factors

Each block \(B_j\) has six coordinates and neutral state
\[
                         O_j=\{a_j,c_j,e_j\},
\]
which splits its three base pairs.  In seed block \(i\), the four states
\(D_i\) have one full pair, the four states \(Z_i\) split all three pairs,
and none equals \(O_i\).

In component \(\mathcal S_i\), every other block is frozen at its neutral
state.  Therefore distinct components disagree in at least one block
between \(O_i\) and \(D_i\cup Z_i\) or \(D_0\), proving literal
disjointness.

Every special state has rank \(3(k+1)\) on \(6(k+1)\) coordinates.  After
adjoining a split reservoir orientation, every carrier owner has rank
\[
                         3(k+1)+2=3k+5
\]
on \(6k+10\) coordinates, exactly the middle rank.

The special-state count is \(4+8k\); multiplying by four reservoir
orientations gives
\[
                         |\mathcal U_k|=16(2k+1).
\]

On one seed component, the old shore consists of eight vertical reservoir
squares.  The new shore consists, for \(t=e_i,f_i\), of the two local
squares
\[
 (a_ib_it,b_ic_it,c_id_it,a_id_it)
\]
at each of four reservoir orientations.  Their directions are
\(\{a_i,c_i\}\) and \(\{b_i,d_i\}\), which are disjoint.  The two squares
partition \(D_i\dot\cup Z_i\), so both shores cover the same 32 owners
exactly once.

The survivor contributes four vertical cells.  Hence every Boolean corner
has
\[
                         4+8k=4(2k+1)
\]
physical \(Q_2\)'s and covers the same carrier once.

## 2. Lower and upper ledgers

All neutral contexts split their base pairs.

On an old vertical seed shore, the \(D_i\) cells contribute \(16f_1\) and
the \(Z_i\) cells contribute \(16f_0\).  Every new special lower edge has
local intersection
\[
                         b_it,\ c_it,\ d_it,\ a_it,
\]
none of which is a base pair, so the new shore contributes \(32f_0\).
The fixed survivor contributes \(16f_1\).  Summing gives
\[
 L^-_\epsilon
 =16(k+|\epsilon|)f_0+
  16(k+1-|\epsilon|)f_1.
\]

Every old vertical upper edge fills one reservoir pair, giving type one
over \(Z_i\) and type two over \(D_i\).  Every new special upper union
contains exactly one of \(a_ib_i,c_id_i\) and leaves the reservoir
orientation split.  Thus
\[
 L^+_\epsilon
 =16(k+|\epsilon|)f_1+
  16(k+1-|\epsilon|)f_2.
\]

Each bit consequently has exact signed difference
\[
                         16(e_0-e_1)
\]
below and \(16(e_1-e_2)\) above, unchanged by any frozen exterior core.

## 3. Pointwise operator and \(k=3\)

Each seed death class has \(4\cdot4=16\) owners.  Different death classes
lie in disjoint tagged components.  The survivor-high class has 16 owners,
and the union of all buffer-zero classes has \(16k\).  Therefore
\[
\begin{array}{c|c}
\text{source zero}&k/(2k+1)\\
\text{death}&k/(2k+1)\\
\text{survivor high}&1/(2k+1).
\end{array}
\]

At the all-new corner the decrement is exactly
\[
                         \operatorname{Bernoulli}
                         \left({k\over2k+1}\right).
\]

For \(k=3\), the carrier has
\[
                         16\cdot7=112
\]
owners, every corner has \(4\cdot7=28\) physical \(Q_2\)'s, and the eight
corners have lower ledgers
\[
                         16(3+|\epsilon|)f_0+
                         16(4-|\epsilon|)f_1.
\]
The all-new ledger is \(96f_0+16f_1\), obtained from
\(48f_0+64f_1\) by 48 pointwise deaths, giving density \(3/7\).

This is a simpler exact \(k=3\) construction than the Catalan
\(\binom{[8]}4\)-carrier candidate: neutral contexts trade carrier density
for completely disjoint Boolean ownership.

## 4. Common phase and suspension

The two special squares in a seed component are disjoint, different seed
components are disjoint, and the survivor is disjoint from all of them.
Assigning \(0,1,2,3\) cyclically on every displayed special square is
therefore globally consistent.  On vertical cells,
\[
                         c(S\cup y_j)=g(S)+j
\]
runs cyclically through the reservoir square.  On special cells at fixed
\(y_j\), it is the assigned cyclic colouring shifted by \(j\).

Thus one owner colouring is compatible with every cell of every Boolean
corner.  The standard coloured-square suspension gives
\[
                         4(2k+1)
\]
pairwise disjoint \(C_{2h}\)'s on one identical lifted support for every
\(h\ge2\).

Common phase compatibility proves local all-length exactness.  It does not
by itself imply phase-independent death after an arbitrary Hamming tensor;
the balanced charts of Section 8 are separately necessary for that claim.

## 5. Abstract capacity and Gaussian threshold

For an abstract \(k\)-seed carrier with disjoint equal death bits of density
\(1/(2k+1)\), \(L\) independent product-transversal visible blocks give
\[
 D_L\sim\operatorname{Bin}\left(L,{k\over2k+1}\right).
\]
The exact conditional-sector target displacement is
\[
 \Delta_{\varepsilon,q}
 ={q(2m-2\varepsilon-q-1)\over2(2m-1)}.
\]
For fixed \(k\), matching the mean would require
\[
 L^*_{k,\varepsilon,q}
 ={2k+1\over k}\Delta_{\varepsilon,q}
 =\left(1+{1\over2k}\right)q+O_A(1).
\]
The direct \(L=q\) tensor has exact centre gap
\[
 \Delta_{\varepsilon,q}-{kq\over2k+1}
 =
 {q[\,2m-(2k+1)(2\varepsilon+q)-1\,]
  \over2(2m-1)(2k+1)}
 ={q\over2(2k+1)}+O_A(1).
\]
At \(q=A\sqrt m+o(\sqrt m)\), its product-normal total-variation gap is
\[
                         2\Phi\left({A\over2k+1}\right)-1.
\]

Letting \(k\to\infty\) removes this Gaussian gap without requiring more
than \(q\) touched blocks.  The centred decrement variance remains
\(O(q)=O(\sqrt m)\), negligible relative to the ambient
\(\Theta(m)\) pair-type variance.

## 6. Packing and tensor phase

The block eligibility probability is
\[
 p_k={16(2k+1)\over2^{6k+10}}
 ={2k+1\over2^{6k+6}},
\]
and with \(B=\lfloor2m/(6k+10)\rfloor\),
\[
                         Bp_k=\Theta(m/64^k).
\]
Thus \(64^k=o(m^{1/3})\) leaves enough inventory to select
\(r=m^{2/3+o(1)}\) blocks, with exponentially small conditioned leave.
The exact component count is \(G/(4r)\), giving standard collar
\(O(HW/r)=o(W)\) through \(H=O(\sqrt m)\).

The parity-balanced local charts in Section 8 are correct: for every fixed
abstract \(Q_2\) vertex, four of the eight cells in each seed component
declare it a death vertex, while the four survivor cells never do.  Hence
the conditional death probability is exactly \(k/(2k+1)\), independently
of Hamming phase.  The order
\[
 \alpha_1,\ldots,\alpha_r,\beta_1,\ldots,\beta_r
\]
repeated twice touches every local block at most once in a window
\(q\le r\).  The exact conditional decrement is therefore binomial.

The upper action is its pointwise complement.  A seed buffer vertex
creates one full pair, a seed death vertex creates none, and every
survivor vertex creates its reservoir pair.  Hence, for the same window,

\[
 B_q=q-D_q\sim
 \operatorname{Bin}\left(q,{k+1\over2k+1}\right).
\]

Its centre has the opposite error of the same magnitude and its centred
fluctuation is again \(O_p(m^{1/4})\).  Thus the lower and upper leading
Gaussian type laws are simultaneous, although exact finite orbit and
labelled balance remain open.

More precisely, the phasewise buffer/death/survivor multiplicities are
\(4k,4k,4\), with source/lower/upper types

\[
                         (0,0,1),\quad(1,0,1),\quad(1,1,2).
\]

Thus the report's exact joint generating polynomial

\[
                         {kz+kxz+xyz^2\over2k+1}
\]

passes term by term.  Its consequence \(\mathcal P_+(u)=u^q\mathcal
P_-(u)\) is a real finite-law rigidity, not a claim that the full uniform
lower and upper target laws have already been reached.

The menu has \(kr\) Boolean bits, but a fixed product row lies in one local
cell per block and changes at most one pair frame there.  Its matching
radius is at most \(r\), which is still \(m^{2/3+o(1)}\gg\sqrt m\).
This correction does not affect the action or collar conclusions.
