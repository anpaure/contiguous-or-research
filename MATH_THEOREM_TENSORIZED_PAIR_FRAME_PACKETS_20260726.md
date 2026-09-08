# Tensorized pair-frame packets and the coarse-capacity audit

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

The bounded 8-coordinate pair-frame associator tensorizes without loss.
For every \(r\ge1\), each resolution vector
\(\varepsilon\in\{0,1\}^r\) partitions the same support

\[
                         \mathcal V^{\,r}
\tag{0.1}
\]

into \(6^r\) disjoint copies of \(Q_{2r}\).  If \(h=2r\) is a power of
two, applying the resolvable Hamming factor inside every cube gives an
exact \(C_{4r}\)-factor of the common support.  Thus one packet carries
\(2^r\) exact middle resolutions.

There is a canonical global partition into these packets: in a middle set
take its first \(r\) eligible 8-blocks.  If \(r=o(m)\), the family with
fewer than \(r\) eligible blocks has size

\[
                         e^{-\Omega(m)}W.
\tag{0.2}
\]

Hence all but an exponentially small fraction of the middle layer is
partitioned into tensor packets.

The visible two-directions-per-block restriction does not force an
\(\Omega(W)\) target deficit at \(q=\Theta(\sqrt m)\).  Uniform targets
have linearly many eligible blocks, whereas the construction requests
only \(r-q=o(m)\).  In fact the local frame admits two connected
partitions into three \(Q_3\)'s.  After adjoining one spectator pair these
become two partitions into three \(Q_4\)'s, and tensor powers feed directly
into the power-of-two Hamming factor.

The remaining gate is therefore fine, not coarse:

\[
\boxed{\text{consecutive direction order and cross-packet shadow
collisions, not 8-block weight capacity.}}
\tag{0.3}
\]

## 1. The local datum

On one labelled 8-block

\[
                 B=\{a,b,c,d,u,v,w,x\},
\]

put

\[
 \mathcal V=
 \left\{
 X\cup Y:
 X\in\binom{\{a,b,c,d\}}2,\ 
 Y\in\{uw,ux,vw,vx\}
 \right\}.
\tag{1.1}
\]

Thus \(|\mathcal V|=24\), and every member has size four.  The two local
pair-frame resolutions from the bounded associator theorem are denoted

\[
 \mathscr R^0=\{K^0_1,\ldots,K^0_6\},
 \qquad
 \mathscr R^1=\{K^1_1,\ldots,K^1_6\}.
\tag{1.2}
\]

Each \(K^\eta_j\) is an isometric \(Q_2\), the six cells in each
resolution are disjoint, and

\[
 \mathcal V=\mathop{\dot\bigcup}_{j=1}^6K^0_j
           =\mathop{\dot\bigcup}_{j=1}^6K^1_j.
\tag{1.3}
\]

The ownership overlap of the two resolutions is connected.

## 2. Exact tensorization

Take \(r\) disjoint labelled copies \(B_1,\ldots,B_r\) of the block in
Section 1 and write

\[
 \mathcal V^{\,r}
 =
 \left\{
 S\subseteq\bigcup_{i=1}^rB_i:
 S\cap B_i\in\mathcal V_i\ \text{for every }i
 \right\}.
\tag{2.1}
\]

Every member has size \(4r\), and \(|\mathcal V^{\,r}|=24^r\).

### Theorem 2.1 (the \(2^r\) exact cube resolutions)

For every
\(\varepsilon=(\varepsilon_1,\ldots,\varepsilon_r)\in\{0,1\}^r\),

\[
 \boxed{
 \mathcal V^{\,r}
 =
 \mathop{\dot\bigcup}_{(j_1,\ldots,j_r)\in[6]^r}
 \left(
 K^{\varepsilon_1}_{j_1}\square\cdots\square
 K^{\varepsilon_r}_{j_r}
 \right).}
\tag{2.2}
\]

Every cell in (2.2) is an isometric \(Q_{2r}\).  Hence (2.2) consists of
exactly \(6^r\) cubes.

#### Proof

The Cartesian product of \(r\) copies of \(Q_2\) is \(Q_{2r}\).  For a
fixed \(\varepsilon_i\), the six cells \(K^{\varepsilon_i}_{j_i}\)
partition \(\mathcal V_i\).  Taking Cartesian products of these disjoint
partitions proves both disjointness and exhaustion in (2.2). \(\square\)

### Corollary 2.2 (exact \(C_{4r}\)-factors)

Assume

\[
                         h=2r=2^t.
\tag{2.3}
\]

Fix any one resolution class of the Hamming
\(C_{2h}=C_{4r}\)-factor of \(Q_h\).  Applying it inside every cell of
(2.2) gives, for every \(\varepsilon\), an exact factor

\[
 \mathscr C_\varepsilon
 \quad\text{of }\mathcal V^{\,r}
\tag{2.4}
\]

into

\[
 6^r\frac{2^{2r}}{4r}
 =\frac{24^r}{4r}
\tag{2.5}
\]

isometric \(C_{4r}\)'s.  Consequently any two choices
\(\varepsilon,\varepsilon'\) give an exact integral trade on the same
middle support.

The assertion is support-exact.  It does not assert that the ownership
overlap after the Hamming refinement is one component; component
connectivity is not needed for the exact replacement.

## 3. Canonical global packet partition

Let \(n=2m+1\), and choose

\[
                         B=\lfloor m/4\rfloor
\tag{3.1}
\]

disjoint labelled 8-blocks among \(2m\) of the coordinates.  Call a block
\(i\) eligible for a middle set \(S\in\binom{[n]}m\) when

\[
                         S\cap B_i\in\mathcal V_i.
\tag{3.2}
\]

For a set having at least \(r\) eligible blocks, let \(I(S)\) be the
indices of its first \(r\) eligible blocks.  Define its packet by

\[
 \mathscr P(S)=
 \left\{
 S':
 \begin{array}{l}
 S'\cap B_i\in\mathcal V_i\quad(i\in I(S)),\\
 S'\cap B_i=S\cap B_i\quad(i\notin I(S)),\\
 S'\text{ agrees with }S\text{ off the }8\text{-blocks}
 \end{array}
 \right\}.
\tag{3.3}
\]

Every varied block still contributes exactly four points, so
\(\mathscr P(S)\subseteq\binom{[n]}m\).

### Lemma 3.1 (the first-\(r\) rule is stable)

If \(S'\in\mathscr P(S)\), then \(I(S')=I(S)\).  Consequently two packets
defined by (3.3) are either equal or disjoint, and each packet is
canonically isomorphic to \(\mathcal V^{\,r}\).

#### Proof

Every selected block remains eligible under variation in \(\mathcal V\).
Every unselected block is frozen, so its eligibility status does not
change.  Therefore the ordered list of the first \(r\) eligible blocks is
constant throughout the packet.  The remaining assertions follow
immediately. \(\square\)

### Theorem 3.2 (exponentially small middle leave)

If \(r=o(m)\), then

\[
 \#\left\{
 S\in\binom{[n]}m:
 S\text{ has fewer than }r\text{ eligible blocks}
 \right\}
 \le e^{-c m}W
\tag{3.4}
\]

for some absolute \(c>0\) and all sufficiently large \(m\).

#### Proof

Generate the coordinates independently with probability
\(p=m/(2m+1)\), then condition on total size \(m\).  Before conditioning,
the block indicators are independent and their common success
probability is

\[
 24p^4(1-p)^4=\frac3{32}+O(m^{-2}).
\tag{3.5}
\]

Thus the number \(Z\) of eligible blocks is binomial with

\[
 \mathbb EZ=\left(\frac3{128}+o(1)\right)m.
\tag{3.6}
\]

Since \(r=o(m)\), eventually \(r\le\mathbb EZ/2\), and Chernoff gives
\(\Pr(Z<r)\le e^{-c_1m}\).  The conditioning event has probability
\(\Theta(m^{-1/2})\) by Stirling, so conditioning multiplies this bound by
at most \(O(\sqrt m)\).  Absorbing the polynomial factor into the
exponential proves (3.4). \(\square\)

Combining Lemma 3.1, Theorem 3.2, and Corollary 2.2 gives:

### Corollary 3.3 (global tensor packet factor)

If \(2r\) is a power of two and \(r=o(m)\), all but
\(e^{-\Omega(m)}W\) middle sets are partitioned into canonical packets,
and every packet independently admits \(2^r\) exact
\(C_{4r}\)-factor resolutions.

## 4. A three-direction local refinement

The local frame is not intrinsically two-dimensional.  Define three
cells by their special two-set supports

\[
 \{ab,ac\},\qquad \{ad,bd\},\qquad \{bc,cd\},
\tag{4.1}
\]

and in each cell allow all four reservoir orientations.  These are three
disjoint \(Q_3\)'s, with active pairs respectively

\[
 (bc,uv,wx),\qquad (ab,uv,wx),\qquad (bd,uv,wx),
\tag{4.2}
\]

and fixed special points \(a,d,c\).  They partition \(\mathcal V\).

A second partition is given by special supports

\[
 \{ab,ad\},\qquad \{ac,bc\},\qquad \{bd,cd\},
\tag{4.3}
\]

with active special pairs \(bd,ab,bc\) and fixed special points \(a,c,d\).
After suppressing the four parallel reservoir phases, the ownership
overlap of (4.1) and (4.3) is the 6-cycle

\[
 ab-ac-bc-cd-bd-ad-ab.
\tag{4.4}
\]

Hence:

### Theorem 4.1 (connected three-\(Q_3\) associator)

The same 24-state frame has two exact partitions into three isometric
\(Q_3\)'s, and their ownership overlap is connected.

The divisibility condition \(2d\mid2^d\) prevents a uniform
\(C_{2d}\)-factor when \(d=3r\).  One spectator pair removes this issue.
On ten coordinates put

\[
                  \widetilde{\mathcal V}=\mathcal V\square Q_1.
\tag{4.5}
\]

Each of the two \(Q_3\)-partitions becomes a partition of
\(\widetilde{\mathcal V}\) into three \(Q_4\)'s.  Therefore

\[
 \widetilde{\mathcal V}^{\,r}
 =\mathop{\dot\bigcup}_{3^r\text{ cells}}Q_{4r}
\tag{4.6}
\]

in either resolution.  If \(r\) is a power of two, then \(h=4r\) is a
power of two and the Hamming construction gives an exact
\(C_{8r}\)-factor in every resolution.

The global first-\(r\) packet construction and exponential-leave proof
apply verbatim to disjoint 10-blocks: now the local success probability is

\[
                         \frac{48}{2^{10}}=\frac3{64},
\tag{4.7}
\]

still a fixed positive constant.  Thus the three-direction refinement is
globally packable up to an exponentially small middle leave.

The depth-one signed ledger can in fact be audited exactly, and it exposes
a limitation.

### Proposition 4.2 (the padded \(Q_3\) move has zero aggregate type drift)

Measure full-pair type relative to

\[
                         ab\mid cd\mid uv\mid wx\mid yz.
\tag{4.8}
\]

In either of the two \(Q_4\)-resolutions of
\(\widetilde{\mathcal V}\), one Hamming resolution class has lower and
upper type ledgers

\[
 \boxed{
 \mathscr S^-:36f_0+12f_1,
 \qquad
 \mathscr S^+:36f_1+12f_2.}
\tag{4.9}
\]

In particular, switching the two three-\(Q_4\) resolutions changes fine
shadow identities but has zero aggregate depth-one fixed-pair drift.

#### Proof

Every local \(Q_4\) cell has one special direction and three
reservoir/spectator directions.  A Hamming \(C_8\)-factor of \(Q_4\)
contains two cycles; each direction occurs twice in each cycle, hence
four times in the factor.  The two occurrences of a direction within one
cycle are antipodal, so along a nonspecial direction the two special
two-set states occur equally often.

Two cells in either partition contain exactly one of the full special
pairs \(ab,cd\), while the third contains neither.  A cell of the first
kind contributes

\[
 10f_0+6f_1\quad\text{below},\qquad
 10f_1+6f_2\quad\text{above}.
\tag{4.10}
\]

Indeed, the four special-direction lower faces have no full pair, while
each of the three other directions contributes two faces with the full
special pair and two without it.  Union rather than intersection shifts
every displayed type by one.  A cell containing no full special pair
contributes \(16f_0\) below and \(16f_1\) above.  Summing two cells of the
first kind and one of the second proves (4.9). \(\square\)

Thus the \(Q_3/Q_4\) refinement solves support dimension and divisibility,
but it cannot replace the original \(Q_2\) associator as the signed
depth-one correction.  A global construction must either mix the two
mechanisms or exploit the fine, rather than aggregate-type, difference
between the \(Q_4\) resolutions.

## 5. Exact coarse target-capacity audit

Consider first the \(Q_2\)-tensor packet.  A lower \(q\)-window of an
isometric \(C_{4r}\), \(q<2r\), uses \(q\) distinct directions.  If \(d_i\)
of them belong to selected block \(i\), then

\[
 d_i\in\{0,1,2\},\qquad
 \sum_i d_i=q,\qquad
 |R\cap B_i|=4-d_i.
\tag{5.1}
\]

In particular, every untouched selected block is still literally in
\(\mathcal V\).  Writing

\[
 Z(R)=\#\{i:R\cap B_i\in\mathcal V_i\},
\tag{5.2}
\]

every produced target satisfies

\[
                         Z(R)\ge r-q.
\tag{5.3}
\]

For a uniform \(R\in\binom{[n]}{m-q}\), the same conditioned-binomial
calculation as in Section 3 gives

\[
 \mathbb EZ(R)=\left(\frac3{128}+o(1)\right)m
\tag{5.4}
\]

uniformly for \(q=o(m)\).  Hence, if \(r=o(m)\),

\[
 \Pr\{Z(R)<r-q\}\le e^{-\Omega(m)}.
\tag{5.5}
\]

Even the canonical first-\(r\) rule causes no macroscopic loss.  If
\(q=o(r)\), use \(q\) early blocks having the exact local target pattern

\[
                         \{c,u,w\},
\tag{5.6}
\]

and complete each by adding \(a\), producing
\(acuw\in\mathcal V\).  Under the Bernoulli model a labelled block has
pattern (5.6) with probability \(1/256+o(1)\).  Among the first
\(\lfloor r/4\rfloor\) blocks there are at least \(q\) such patterns
outside an \(e^{-\Omega(r)}\) event.  All completed blocks lie among the
source's first \(r\) eligible blocks.  Consequently, uniformly for
\(1\le q\le Q=o(r)\),

\[
 \#\{\text{targets with no canonical coarse completion at depth }q\}
 \le
 \left(e^{-c r}+e^{-c'm}\right)\binom n{m-q}.
\tag{5.7}
\]

Therefore

\[
 \sum_{q\le Q}
 \#\{\text{coarsely excluded targets at depth }q\}
 \le
 Q\left(e^{-cr}+e^{-c'm}\right)W=o(W).
\tag{5.8}
\]

This is a target-capacity statement, not merely an average occurrence
calculation.

## 6. The apparent triple-deletion deficit

There is nevertheless a real incidence warning.  Group \(m\) idealized
deletion directions into \(m/4\) macroblocks of four, and choose a uniform
\(q\)-subset.  For \(q=O(\sqrt m)\), the probability that some block
receives at least three directions is

\[
 \left(1+o(1)\right)\frac{q^3}{m^2}.
\tag{6.1}
\]

Indeed, the expected number of such blocks is

\[
 \frac m4
 \frac{
 4\binom{m-4}{q-3}+\binom{m-4}{q-4}
 }{\binom mq}
 =
 \left(1+o(1)\right)\frac{q^3}{m^2},
\tag{6.2}
\]

and simultaneous events in two blocks have lower order.  Since
\(\binom n{m-q}/W\asymp e^{-q^2/m}\), summing (6.1) over the Gaussian
window gives

\[
 \sum_{q\le A\sqrt m}
 \binom n{m-q}\Pr(\text{a triple block})
 =
 \left(
 \int_0^A t^3e^{-t^2}\,dt+o(1)
 \right)W.
\tag{6.3}
\]

Thus the pure \(Q_2\) realization misses a \(\Theta(W)\) portion of the
*uniform deletion-incidence benchmark*.  Equation (6.3) alone is not a
missing-target theorem: a target has many middle extensions and can
choose a completion with its additions spread across distinct blocks.
The explicit completion bound (5.8) proves that the benchmark loss does
not become a coarse target-capacity loss.

The \(Q_3\) refinement removes even this incidence warning.  Its first
forbidden event is four directions in one block, whose total Gaussian
mass is

\[
 \sum_{q\le A\sqrt m}
 \binom n{m-q}\,
 O\!\left(\frac{q^4}{m^3}\right)
 =
 O\!\left(\frac W{\sqrt m}\right)=o(W).
\tag{6.4}
\]

This is the precise reason local dimension three is the natural safe
threshold for the Gaussian window.

## 7. Final theorem and remaining gate

The tensorized associator supplies exponentially many local resolution
choices while preserving exact middle ownership packet by packet:

\[
 \text{\(2^r\) resolutions on \(\mathcal V^r\), or two connected
 resolutions on \(\widetilde{\mathcal V}^{\,r}\).}
\tag{7.1}
\]

All but \(e^{-\Omega(m)}W\) middle sets lie in canonical packets whenever
\(r=o(m)\).  Neither the 8-block weight invariant nor the
three-deletion issue forces an \(\Omega(W)\) target deficit; the padded
\(Q_3\) refinement eliminates the latter even at the incidence level.

What is not proved is the needed shadow theorem.  A successful global
choice of packet resolutions must still show that:

1. the prescribed local directions occur as consecutive windows in the
   selected Hamming cycles;
2. fine targets produced by distinct middle packets collide only \(o(W)\)
   times in aggregate;
3. the resolution choices have the required signed action on the full
   fixed-pair type ledger at all depths.

These are now the exact remaining gates.  No coarse block-capacity
obstruction survives.
