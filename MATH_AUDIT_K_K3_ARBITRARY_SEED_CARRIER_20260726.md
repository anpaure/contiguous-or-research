# Audit of the (k=3) and arbitrary-(k) signed Q2 carrier

Date: 2026-07-26

Audited file:
`MATH_ATTACK_K_ARBITRARY_K_SEED_COMMON_OWNER_CARRIER_20260726.md`.

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

The arbitrary-(k) construction is exact.  In particular, (k=3) gives
a literal eight-corner factor menu on one (112)-owner middle carrier.
Every corner contains (28) physical Q2 cells, every bit has lower drift

\[
                         16(e_0-e_1),                 \tag{0.1}
\]

and upper drift (16(e_1-e_2)), and all eight corners have one common
phase colouring.  The all-new corner has exact death density

\[
                              {3\over7}.              \tag{0.2}
\]

The general ledgers

\[
 L^-_\epsilon
 =16(k+|\epsilon|)f_0+16(k+1-|\epsilon|)f_1,         \tag{0.3}
\]

\[
 L^+_\epsilon
 =16(k+|\epsilon|)f_1+16(k+1-|\epsilon|)f_2          \tag{0.4}
\]

are correct.

The Gaussian tensor claim also survives audit, but it needs one explicit
phase-balanced cell lemma which is not stated in the original proof.
Direction transversality alone would not imply a binomial decrement,
because Hamming-cycle phase can correlate with local Q2 orientation.
Here the common reservoir offsets repair the issue exactly: for every
fixed local colour, precisely (4k) of the (4(2k+1)) all-new local
cells place a death owner at that colour.  Therefore, conditional on an
arbitrary Hamming orientation and phase, the independent local cell
catalogue still gives death probability (k/(2k+1)) in every touched
block.  This proves

\[
 D_q\sim\operatorname{Bin}\left(q,{k\over2k+1}\right)              \tag{0.5}
\]

exactly inside every complete product packet.  Canonical first-(r)
packet selection and arbitrary frozen exteriors do not change (0.5), so
it remains exact on the retained near-spanning factor.  It need not hold
after deleting cell types, choosing incomplete packet sectors, or making
state-dependent component selections.

Thus the local (k)-seed, common phase, growing-(k) packing, and leading
Gaussian type-law claims pass.  The result remains a type-law theorem,
not labelled target balance or coefficient one.

## 1. Exact component and owner census

There are (k+1) disjoint six-coordinate blocks (B_0,ldots,B_k), each
with three fixed base pairs.  The neutral state

\[
                         O_j=\{a_j,c_j,e_j\}          \tag{1.1}
\]

splits all three pairs.  Seed component (i\ge1) varies its (B_i)
restriction through four death states (D_i) and four buffer states
(Z_i), while every other block is frozen at (O_j).  The survivor
component varies (B_0) through its four death states and freezes the
other blocks neutrally.

If (i\ne j), component (j) restricts to (O_i) on (B_i), whereas
component (i) restricts to (D_i\cup Z_i), or to (D_0) when (i=0).
None of these states equals (O_i).  Hence the components are pairwise
disjoint.

After adjoining the four reservoir orientations, their owner counts are

\[
 |\mathcal S_i\times\mathcal Y|=8\cdot4=32
       \quad(i\ge1),
 \qquad
 |\mathcal S_0\times\mathcal Y|=4\cdot4=16.          \tag{1.2}
\]

Thus

\[
                         |\mathcal U_k|=32k+16
                         =16(2k+1).                   \tag{1.3}
\]

Every owner has rank

\[
                         3(k+1)+2=3k+5               \tag{1.4}
\]

on (6(k+1)+4=6k+10) coordinates, exactly the middle rank.

For (k=3), the carrier is therefore a family of (112) rank-(14)
owners on (28) coordinates, decomposed as

\[
                         16+32+32+32.                 \tag{1.5}
\]

## 2. Classification of the local Q2 resources

The construction uses only the following three cell resources.  Here
"source-high" means that the local special state contains one full base
pair, and the last column counts lower type-one edges.

\[
\begin{array}{c|c|c|c}
\text{cell resource}&\text{number of owners}&
 \text{source-high owners}&\text{type-one lower edges}\\ \hline
\text{death vertical }D_i\times Q_R&4&4&4\\
\text{buffer vertical }Z_i\times Q_R&4&0&0\\
\text{new special }Q_{i,t}\times\{Y\}&4&2&0\\
\text{survivor vertical }D_0\times Q_R&4&4&4.
\end{array}                                           \tag{2.1}
\]

The third row follows because

\[
 Q_{i,t}=(a_ib_it,b_ic_it,c_id_it,a_id_it)            \tag{2.2}
\]

alternates death and buffer states.  Its four lower special
intersections are

\[
                         b_it, c_it, d_it, a_it,    \tag{2.3}
\]

none of which is a base pair.

One seed component has four death-vertical and four buffer-vertical
cells on its old shore, so its old ledger is

\[
                         16f_0+16f_1.                 \tag{2.4}
\]

Its new shore has eight special cells of the third kind, giving

\[
                         32f_0.                       \tag{2.5}
\]

The survivor has four cells of the last kind and contributes (16f_1).
Summing proves (0.3).

For upper edges, a vertical reservoir edge fills one reservoir pair.
It therefore has type one over (Z_i) and type two over (D_i).  Every
special-square union in (2.2) contains exactly one local full pair.  Thus
the old and new seed ledgers are

\[
                         16f_1+16f_2,qquad32f_1,      \tag{2.6}
\]

while the survivor contributes (16f_2).  This proves (0.4) directly,
without a complement assumption.

For (k=3), if (w=|\epsilon|), the four possible lower ledgers are

\[
\begin{array}{c|c}
w&L^-_\epsilon\\ \hline
0&48f_0+64f_1\\
1&64f_0+48f_1\\
2&80f_0+32f_1\\
3&96f_0+16f_1.
\end{array}                                           \tag{2.7}
\]

The all-new decrement is (48/112=3/7), and the sixteen survivor-high
occurrences give the residual (1/7).

## 3. Exact factor cube and the absence of hidden multiplicity

The old seed shore consists of eight disjoint reservoir squares, one over
each state in (D_i\dot\cup Z_i).  The two special squares
(Q_{i,e_i},Q_{i,f_i}) partition the same eight special states; repeating
them at four reservoir orientations gives eight disjoint new-shore cells.
Thus each seed shore covers the same (32) owners once.

Different seed components and the survivor component are owner-disjoint by
Section 1.  Consequently choosing the old or new shore independently in
every seed gives one-copy owner multiplicity at all (2^k) corners.  The
factor contains

\[
                         8k+4=4(2k+1)                 \tag{3.1}
\]

physical Q2 cells.  For (k=3), this is (28) cells at each of eight
corners.

This is a direct-sum/tagged construction: different seed bits act on
disjoint owner components.  The common carrier and common reservoir make
the factor menu literal, but the theorem does not claim that one owner is
acted on by several bits.

## 4. Common phase

Give the four states of every displayed special square the colours
(0,1,2,3) in cyclic order.  Distinct squares and distinct seed components
have disjoint owner states, so this defines (g) without conflict.  Give
the survivor states arbitrary values and put

\[
                   c(S\cup y_j)=g(S)+j\pmod4.         \tag{4.1}
\]

Every vertical cell sees the four reservoir offsets consecutively, while
every special cell at fixed (y_j) sees its assigned cyclic colours shifted
by (j).  Hence the same colouring is phase-compatible with every cell in
every corner.

The standard coloured-square suspension therefore lifts all corners to
the same owner support, with (4(2k+1)) physical (C_{2h})'s per lifted
local carrier.  No extra phase constraint appears at (k=3).

## 5. The phase-balanced cell census

The exact binomial law needs more than the owner counts in the original
Section 5.  It follows from the following stronger cellwise identity.

### Lemma 5.1 (death count at every local colour)

Fix a colour (ell\in\mathbb Z_4) and consider all
(4(2k+1)) Q2 cells in the all-new local factor.  Exactly (4k) cells
have a death owner at their unique vertex of colour (ell); exactly four
have a survivor-high owner there; and exactly (4k) have a buffer-zero
owner there.

#### Proof

For one seed (i), its new cells are indexed by

\[
                         t\in\{e_i,f_i\},qquad j\in\mathbb Z_4.    \tag{5.1}
\]

There are eight.  In each special square the death states occupy the
opposite base colours (0,2), while the buffer states occupy (1,3).
After adding reservoir offset (j), the colour-(ell) vertex is a death
state exactly when

\[
                         j\equiv\ell\pmod2.           \tag{5.2}
\]

There are two such offsets for each of the two values of (t), hence four
death cells and four buffer cells per seed.  Summing over (k) seeds gives
(4k) of each kind.  Every one of the four survivor vertical cells has a
survivor-high owner at colour (ell). \(\square\)

The lemma shows why an arbitrary common phase would not suffice: the four
reservoir offsets balance each death square at every individual colour.

## 6. Exact tensor-sector binomial law

Take a complete product packet (mathcal U_k^r) and its all-new factor.
Every product Q2 cell tuple occurs once.  Identify every local Q2 cell with
the abstract four colours using the common phase from Section 4, and apply
the same abstract Hamming factor to every product cell.

Fix any Hamming start phase, any abstract orientation vector of its product
cell, and any depth-(q) transversal window touching a set (J) of (q)
distinct local blocks.  These data determine one local colour
(ell_i\) in every block (i\), but do not determine the local cell
identity.  As the complete product cell tuple ranges, its local identities
are independent and uniform over the (4(2k+1)) cells.  Lemma 5.1 gives

\[
 \Pr(\text{death in block }i\mid\ell_i)
 ={4k\over4(2k+1)}={k\over2k+1}.                     \tag{6.1}
\]

The events are independent over (i\in J).  Therefore, conditional on
the arbitrary Hamming phase and orientation,

\[
                         D_q\sim
 \operatorname{Bin}\left(q,{k\over2k+1}\right).      \tag{6.2}

Averaging the conditioning proves the same exact law over all starts in
the complete packet factor.  No independence property of the Hamming
syndrome phase fibres is needed.

The source contribution has the simultaneous phasewise categorical law

\[
 \Pr(\text{death-high})={k\over2k+1},\qquad
 \Pr(\text{survivor-high})={1\over2k+1},\qquad
 \Pr(\text{buffer-zero})={k\over2k+1}.                \tag{6.3}

Thus correlations between source type and decrement are also explicitly
controlled; their total contribution over (q=O(\sqrt m)) touched blocks
is (O(q)), negligible beside the ambient (Theta(m)) variance.

## 7. Passage through canonical packet selection

The first-(r)-eligible rule partitions every retained owner into a
complete packet (mathcal U_k^r) with a frozen exterior.  Section 6 is
exact in every such packet separately, and its law does not depend on the
exterior.  Hence (6.2) remains exact after summing all canonical packets.
The exceptional leave has the bound stated in Theorem 7.1 and is
(o(W)) in the proposed regime.

Accordingly the claim should be stated as follows:

\[
 \boxed{\begin{minipage}{0.86\linewidth}
 In the retained canonical packet factor, for the all-new local corner and
 a common phase-compatible product-transversal Hamming order, every
 depth-(q) decrement has the exact aggregate law
 \(\operatorname{Bin}(q,k/(2k+1))\).  The assertion uses every local cell
 identity in every complete product packet.
 \end{minipage}}                                      \tag{7.1}
\]

It is not a theorem for an arbitrary subfamily of product cells, an
incomplete tensor sector, a state-dependent component selection, or a
different phase assignment which loses Lemma 5.1.

## 8. Packing and Gaussian scope

The eligibility probability is

\[
 p_k={16(2k+1)\over2^{6k+10}}
     ={2k+1\over2^{6k+6}},                            \tag{8.1}
\]

and the number of available blocks is

\[
 B=\left\lfloor{2m\over6k+10}\right\rfloor.          \tag{8.2}
\]

Thus (Bp_k=\Theta(m/64^k)).  The half-mean Chernoff and central-rank
conditioning argument gives

\[
 {W-G\over W}
 \le2(m+1)e^{-Bp_k/8}.                                \tag{8.3}

If (64^k=o(m^{1/3})), one may select
(r=m^{2/3+o(1)}\), round (2r) to a power of two, and retain
(G=(1-o(1))W) owners.  The exact factor has (G/(4r)) components, so
the standard depth-(H=O(\sqrt m)) collar is

\[
                         O(HW/r)=o(W).                \tag{8.4}

By (6.2), its mean decrement is

\[
 {qk\over2k+1}={q\over2}-{q\over2(2k+1)},            \tag{8.5}

and its conditional variance is (O(q)).  For (k\to\infty) and
(q=A\sqrt m+O(1)), the centre error is (o(\sqrt m)), and every added
variance/covariance term from the (q) local categories is (O(q)=o(m)).
Hence the normalized output type has the same Gaussian centre and variance
as the uniform target law.

This conclusion does not give total-variation convergence of the complete
finite orbit law without a local limit argument.  It gives convergence of
the normalized pair-type statistic to the same Gaussian.  It also says
nothing by itself about labelled targets, simultaneous shadow collisions,
or all-depth carrier affinity.

## 9. Exact boundary

Proved and audited:

1. the literal (112)-owner, eight-corner (k=3) factor;
2. the arbitrary-(k) exact factor cube and ledgers;
3. one common phase and all-length suspension;
4. the phase-balanced cell census;
5. the exact tensor-sector and retained-packet binomial decrement;
6. near-spanning packing in the stated growing-(k) range; and
7. disappearance of the leading Gaussian pair-type mean/variance
   obstruction when (k\to\infty).

Not proved:

* exact finite matching of every target orbit mass;
* total-variation convergence of the full type histogram without an
  additional uniform local limit theorem;
* labelled lower/upper target balance;
* complete all-depth affine carrier vectors;
* collision control or odd-wreath leave completion; or
* coefficient one.
