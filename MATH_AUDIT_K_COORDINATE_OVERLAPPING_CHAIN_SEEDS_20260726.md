# Audit of the coordinate-overlapping chain (Q_2) carrier

Date: 2026-07-26

Audited file:
`MATH_ATTACK_K_COORDINATE_OVERLAPPING_CHAIN_SEEDS_20260726.md`.

Method: pure mathematics only.  No finite search, computation, solver, or
web input was used.

## Verdict

**PASS.**  The adjacent-chain construction is a literal common-support
(2^k)-factor cube.  The coordinate overlap introduces neither an owner
collision nor an (X/Y)-ledger collision: different seed sectors have
different complete tag restrictions, while every cell preserves its tag
restriction.  The middle-rank calculation, owner count, lower and upper
ledgers, common phase, phasewise birth--death law, eligibility, and packing
constants all check exactly.

The main scope caveat in the report is also correct.  This is coordinate
overlap without repeated owner action.  Each owner lies in exactly one
tagged seed sector (or in the survivor sector), so the construction improves
the physical inventory from (64^{-k}) scale to (k^{-2}4^{-k}) scale but
does not itself implement a dependent multihit operator.

There are only typographical TeX defects in the source: `arbitrary-(k\)`,
the commas in the exponents in (0.6), `quad` in (4.1), `left\lfloor` in
(6.4), and the commas in the denominators in (6.7).  None changes a
mathematical assertion.

## 1. Support, ranks, and one-copy ownership

There are

\[
 (k+1)+1+t+2=k+t+4
\]

matched coordinate pairs: the chain pairs (P_0,ldots,P_k), the splitter
(S), the (t) tag pairs, and the two reservoir pairs.  Thus the ambient
block has

\[
 n_k=2(k+t+4)=2k+2t+8
\]

coordinates.

In a seed sector, the active local state has rank three on
(P_{i-1}\cup P_i\cup S).  The (k-1) inactive chain pairs and the (t)
tag pairs each contribute one coordinate.  Hence its nonreservoir rank is

\[
 3+(k-1)+t=k+t+2.
\]

Every reservoir orientation contributes two more coordinates, so every
carrier owner has rank (k+t+4=n_k/2).  The carrier is literally in the
middle layer.

For (i\ne j), every state in sector (i) restricts to (G_i) on the tag
coordinates, whereas every state in sector (j) restricts to (G_j).
Since (G_i\ne G_j), the sectors are disjoint even when their untagged
chain restrictions overlap.  The survivor sector is separated in the same
way.  Consequently

\[
 |\mathcal U_k^{\rm ch}|=4(4+8k)=16(2k+1).
\]

For fixed (i) and (eta), the displayed four local states form the
cycle

\[
 a_{i-1}b_{i-1}s_\eta,quad
 b_{i-1}a_i s_\eta,quad
 a_i b_i s_\eta,quad
 a_{i-1}b_i s_\eta.
\]

Successive edges use alternately the disjoint swaps
(a_{i-1}\leftrightarrow a_i) and
(b_{i-1}\leftrightarrow b_i).  The two splitter values partition
(D_i\dot\cup Z_i).  Therefore the eight old vertical reservoir cells and
the eight new special cells are two exact partitions of the same 32-owner
seed sector.  Together with the four fixed survivor cells, every Boolean
corner partitions the common carrier into exactly

\[
 8k+4=4(2k+1)
\]

physical (Q_2)'s.

No hidden shadow collision is created by the coordinate reuse.  A lower or
upper edge of a cell retains the full tag word (G_i); hence edges in
different sectors remain distinct.  Within one sector, the four reservoir
intersections/unions are distinct on an old cell, and the four active
intersections/unions are distinct on a new cell.  Thus the stated literal
ledgers do not rely merely on a multiplicity count.

## 2. Exact lower and upper ledgers

On a new active square, the four lower intersections are

\[
 b_{i-1}s_\eta,quad a_i s_\eta,quad
 b_i s_\eta,quad a_{i-1}s_\eta.
\]

All split the fixed matching.  Its four upper unions contain exactly one
full pair, alternately (P_{i-1}) and (P_i).  On an old vertical cell,
the lower edge preserves the active state and the upper edge additionally
fills exactly one reservoir pair.  Hence the old and new seed ledgers are

\[
\begin{array}{c|cc}
 &L^-&L^+\\ \hline
\text{old}&16f_0+16f_1&16f_1+16f_2\\
\text{new}&32f_0&32f_1.
\end{array}
\]

The survivor contributes (16f_1) below and (16f_2) above.  A corner
(\epsilon\) of weight (s) therefore has exactly

\[
 L^-_\epsilon
 =16(k+s)f_0+16(k+1-s)f_1,
\]

\[
 L^+_\epsilon
 =16(k+s)f_1+16(k+1-s)f_2.
\]

Each seed bit has the background-independent signed drifts

\[
 16(e_0-e_1)\quad\hbox{below},\qquad
 16(e_1-e_2)\quad\hbox{above}.
\]

The death owner class in seed (i) consists of its four (D_i)-states
times four reservoir orientations, hence has size 16.  These (k) classes
are tag-disjoint.  The buffer classes have total size (16k), and the
survivor-high class has size 16, proving the all-new owner proportions

\[
 \Pr(\text{buffer})={k\over2k+1},\qquad
 \Pr(\text{death})={k\over2k+1},\qquad
 \Pr(\text{survivor})={1\over2k+1}.
\]

## 3. Common phase and the exact joint operator

The special squares are mutually owner-disjoint, so their cyclic
(\mathbb Z_4)-colourings can be chosen independently.  With

\[
 c(X\cup y_j)=g(X)+j\pmod4,
\]

the colour is cyclic around every old vertical cell and every new special
cell.  Thus one colouring works for all (2^k) factors and supplies the
claimed common all-length suspension.

Fix an abstract (Q_2)-vertex.  In a new seed sector, the four reservoir
orientations expose each local square position once.  Across the two
splitter squares this gives four (D_i)-owners and four (Z_i)-owners at
that abstract vertex.  In an old seed sector no owner dies, while all eight
owners birth one pair; the survivor contributes four further birth owners.
Consequently a corner of weight (s) has the exact conditional rates

\[
 p_s^-={s\over2k+1},\qquad
 p_s^+=1-p_s^-={2k+1-s\over2k+1}.
\]

The complementarity is pointwise, not merely in expectation:

\[
\begin{array}{c|ccc}
 &\text{source}&\text{lower}&\text{upper}\\ \hline
\text{new buffer}&0&0&1\\
\text{new death}&1&0&1\\
\text{survivor}&1&1&2.
\end{array}
\]

At the all-new corner the phasewise multiplicities are (4k,4k,4).
Therefore the joint source/lower/upper probability-generating polynomial
is exactly

\[
 \Xi_k(x,y,z)={kz+kxz+xyz^2\over2k+1}.
\]

For a product-transversal window touching (q\) different blocks, local
cell identities are independent and uniform.  Hence

\[
 D_q\sim\operatorname{Bin}\left(q,{k\over2k+1}\right),
 \qquad B_q=q-D_q
 \sim\operatorname{Bin}\left(q,{k+1\over2k+1}\right),
\]

and the full conditional joint law is (\Xi_k^q).  The stated Hamming
direction word repeats the block indices (1,\ldots,r); every cyclic
window of length at most (r) therefore touches each block at most once.
This justifies the binomial law without a hidden phase-independence
assumption.

## 4. Eligibility and constants

Under unbiased independent coordinates, the exact eligibility probability
is

\[
 p_k^{\rm ch}
 ={16(2k+1)\over2^{2k+2t+8}}
 ={2k+1\over2^{2k+2t+4}}.
\]

Because (t=\lceil\log_2(k+1)\rceil),

\[
 (k+1)^2\le2^{2t}<4(k+1)^2,
\]

and hence

\[
 {2k+1\over64\,4^k(k+1)^2}
 <p_k^{\rm ch}
 \le {2k+1\over16\,4^k(k+1)^2}.
\]

For

\[
 B=\left\lfloor{m\over k+t+4}\right\rfloor
\]

and (m\ge2(k+t+4)), multiplication by
(m/[2(k+t+4)]\le B\le m/(k+t+4)) gives exactly (6.6).

The coarse constants in (6.7) are valid uniformly for every (k\ge1).
Indeed (1\le t\le k), and the lower estimate reduces to

\[
 12k^2(2k+1)>(k+t+4)(k+1)^2.
\]

Using (t\le k), its right side is at most
(2(k+2)(k+1)^2); the difference from the left side is at least

\[
 22k^3+4k^2-10k-4>0.
\]

For the upper estimate it is enough to note

\[
 k^2(2k+1)le3(k+t+4)(k+1)^2.
\]

Thus, with the source's typographical commas removed,

\[
 \boxed{
 {m\over1536k^2 4^k}<Bp_k^{\rm ch}
 \le {3m\over16k^2 4^k}.}
\]

If (k^24^k=o(m^{1/3})), this gives
(Bp_k^{\rm ch}=\omega(m^{2/3})).  Choosing (r) as the largest power of
two not exceeding (m^{2/3}) yields

\[
 \tfrac12m^{2/3}<r\le m^{2/3},
\]

and (2r) is also a power of two.  Eventually (r\le Bp_k^{\rm ch}/2).
The first-(r)-eligible selector, conditioned half-mean Chernoff bound,
and common Hamming factor therefore give the claimed leave,
(G/(4r)) components, and common collar

\[
 O(HW/r)=o(W)\qquad(H=O_A(\sqrt m)).
\]

## 5. Exact implication boundary

The report proves a strict inventory improvement and preserves the exact
finite birth--death operator.  It does **not** prove that one owner is
recoupled by several seed involutions: tags make the seed supports
disjoint.  It consequently does not supply dependent multidepth mixing,
exact orbit quotas, labelled balance, or coefficient one.  All Gaussian
claims in the report are leading pair-type statements with the certified
collar removed; the report correctly leaves occurrence-resolved all-depth
collision control open.
