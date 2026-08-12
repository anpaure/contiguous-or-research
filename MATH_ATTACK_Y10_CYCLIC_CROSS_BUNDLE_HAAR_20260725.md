# Lane Y10: genuine cyclic cross-bundle Haar exchanges and the remaining capacity gate

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, solver,
computer experiment, or long-running computation is used.

## 0. Verdict

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad B=\frac Wn=\operatorname{Cat}_m,
\]

and, for \(1\le q\le H\le m-2\), put

\[
N_q=\binom n{m-q},\qquad
c_q=\left\lfloor\frac W{N_q}\right\rfloor .
\]

For an exact wreath factor \(F\), write \(\mu_q^F\) for its
rank-\((m-q)\) cyclic-interval load and use the unhalved floor energy

\[
Q_q(F)=\sum_S
 (\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1),
\qquad
\mathcal Q_H(F)=\sum_{q\le H}\frac{Q_q(F)}{c_q}.
\tag{0.1}
\]

This report constructs a genuine positive cyclic cross-bundle exchange on
one fixed indexed row reservoir.  It is not a signed surrogate and does not
merely preserve middle incidence.

1. A universal two-wreath circuit \(g\) has exact shadow norms

   \[
   \|B_{m-1}g\|_2^2=4,
   \qquad
   \|B_{m-q}g\|_2^2=8\quad(2\le q\le m-2).
   \tag{0.2}
   \]

   An explicit transposition \(\rho\) interchanges its two signs and
   satisfies \(\rho g=-g\).

2. If \(g\) is applicable in \(F\) and \(F'=F+g\), then

   \[
   \boxed{
   F\uplus\rho F\longleftrightarrow F'\uplus\rho F'
   }
   \tag{0.3}
   \]

   is a literal two-colour reblocking of the same indexed wreath-row
   multiset.  At every depth its energy gain is exactly twice its
   cross-colour overlap gain.  No interaction with untouched rows is
   omitted.

3. When \(n\) is prime, one common conjugation develops (0.3) through all
   \(n\) coordinate translations with pairwise disjoint effect supports
   simultaneously for \(q\le A\sqrt m\).  The developed packet has exact
   norms

   \[
   4n\quad(q=1),\qquad 8n\quad(2\le q\le H),
   \tag{0.4}
   \]

   and hence has no \(q\)-dependent seam halo.  These \(n\) exchanges are
   genuine reblockings of one fixed \(2n\)-colour reservoir.

4. Two owner-disjoint binary cells give a stronger exact covariance
   circuit.  The two diagonal decompositions of their Boolean square are
   reblockings of one another, and their weighted energy difference is

   \[
   \boxed{2\langle u,v\rangle_H.}
   \tag{0.5}
   \]

   Thus square-diagonal moves are the positive integral realization of a
   cross-bundle Gram term.

5. These theorems construct genuine cyclic cross-bundle **capacity**, but
   they do not prove capacity saturation.  For one developed universal
   circuit, all \(n\) translated gains are equal.  Choosing an arbitrary
   subset merely produces relabelled copies of the same two endpoint
   factors, so packetization alone cannot create a low endpoint which the
   base circuit did not already have.

6. At depth one the saturating Johnson cycle does give exact capacity
   saturation in the positive integral **edge relaxation**: the complete
   coordinate orbit of its balanced Hamilton cycle is a reblocking of the
   same uniform Johnson-edge multigraph as the orbit of every exact factor.
   It is not a wreath reblocking.  Its doubled lower colours meet at a
   vertex, whereas every lower-colour class in a wreath factor is a
   matching, and it lacks componentwise chronology.

7. The best genuinely cyclic depth-one seed remains PBBS.  In prime
   dimensions its load-three and load-one rotation orbits admit an exact
   centered affine correction to the floor slab.  Nevertheless every
   explicit clean PBBS \(C_8\) has a nonzero first-shadow increment, and a
   full separated rotation packet has mutually disjoint translated
   supports.  One packet therefore cannot realize one high-orbit/low-orbit
   transfer.  Cross-cancellation between at least two distinct core bundles
   and nonzero negative residual charges inside every new wreath are
   compulsory.

Accordingly, the requested genuine cyclic cross-bundle cell is proved, with
all constants.  The statement

\[
\sum_{q\le H}\frac{X_q^{\max}-X_q}{c_q}=o(kW)
\tag{0.6}
\]

is not proved.  The exact missing theorem is now a **correlated common-
completion theorem**: place sufficiently many nonorthogonal cyclic Haar
cells in compatible exact fibres and choose their square diagonals so that
their cross-bundle Gram gain saturates (0.6).  Neither stationarity nor
ordinary zero-voltage packet matching supplies that theorem.

---

## 1. The universal two-for-two circuit

Fix four distinct labels \(\alpha,\beta,\gamma,\delta\).  Let \(E,O\)
be ordered lists partitioning the remaining labels, with

\[
|E|=m-1,\qquad |O|=m-2.
\]

The following four cyclic orders are regarded modulo rotation and reversal:

\[
\begin{aligned}
C&=(\delta,\gamma,E,\beta,\alpha,O),\\
D&=(\beta,\delta,E,\alpha,\gamma,O),\\
C'&=(\delta,\beta,E,\gamma,\alpha,O),\\
D'&=(\gamma,\delta,E,\alpha,\beta,O).
\end{aligned}
\tag{1.1}
\]

Put

\[
P_0=\{C,D\},\qquad P_1=\{C',D'\},\qquad
g=e_{C'}+e_{D'}-e_C-e_D.
\tag{1.2}
\]

For a cyclic order \(R\), let \(B_r e_R\) be the incidence vector of its
\(n\) cyclic intervals of size \(r\).  Thus \(B_m\) is the middle-owner
map and \(B_{m-q}\) is the depth-\(q\) shadow map.

For a set \(K\) avoiding \(\beta,\gamma\), write

\[
\partial K=e_{K\cup\{\gamma\}}-e_{K\cup\{\beta\}}.
\tag{1.3}
\]

### Theorem 1.1 — exact cut profile

Each sign of \(g\) is a two-row middle packing,

\[
B_mg=0,
\tag{1.4}
\]

and, for \(2\le r\le m-1\),

\[
\boxed{
B_rg=
 \partial\operatorname{suf}_{r-1}O
+\partial\operatorname{suf}_{r-1}E
-\partial\operatorname{pre}_{r-1}E
-\partial\operatorname{pre}_{r-1}O.}
\tag{1.5}
\]

Consequently

\[
\boxed{
\|B_{m-1}g\|_2^2=4,
\qquad
\|B_{m-q}g\|_2^2=8\quad(2\le q\le m-2).}
\tag{1.6}
\]

#### Proof

Cut the four words in (1.1) immediately before every displayed exceptional
letter.  An \(r\)-interval wholly inside \(E\) or \(O\) occurs with the
same signed multiplicity on both sides.  The same is true of a cut-crossing
interval containing both or neither of \(\beta,\gamma\).  The surviving
intervals contain exactly one of those labels.  At the four relevant cuts,
their common \((r-1)\)-cores are respectively

\[
\operatorname{suf}_{r-1}O,\quad
\operatorname{suf}_{r-1}E,\quad
\operatorname{pre}_{r-1}E,\quad
\operatorname{pre}_{r-1}O,
\]

with signs \(+,+,-,-\), proving (1.5).  The identical check at \(r=m\)
has no survivor and also shows that neither sign repeats a middle owner.
This proves (1.4).

For \(2\le r\le m-2\), the four ordered-list cores are distinct and
adjoining \(\beta\) or \(\gamma\) gives eight distinct coordinates of
coefficient \(\pm1\).  For \(r=m-1\), the two \(O\)-terms have the same
core and cancel, leaving four distinct unit coordinates.  This proves
(1.6).  \(\square\)

### Lemma 1.2 — the swapping involution

For

\[
\rho=(\beta\ \gamma),
\tag{1.7}
\]

one has

\[
\rho P_0=P_1,\qquad \rho P_1=P_0,
\qquad \rho g=-g.
\tag{1.8}
\]

#### Proof

Apply \(\rho\) to (1.1): it takes \(C\) to \(C'\), \(D\) to \(D'\),
and conversely.  Equation (1.8) follows.  \(\square\)

---

## 2. A genuine fixed-reservoir two-fibre exchange

Assume that the negative side \(P_0\) occurs in an exact factor.  Write

\[
F=K\mathbin{\dot\cup}P_0,
\qquad
F'=K\mathbin{\dot\cup}P_1=F+g.
\tag{2.1}
\]

Theorem 1.1 makes \(F'\) an exact factor.  By Lemma 1.2,

\[
\rho F=\rho K\mathbin{\dot\cup}P_1,
\qquad
\rho F'=\rho K\mathbin{\dot\cup}P_0.
\tag{2.2}
\]

### Theorem 2.1 — involutive cross-bundle coherence

The two decompositions

\[
\mathscr D_0=(F,\rho F),
\qquad
\mathscr D_1=(F',\rho F')
\tag{2.3}
\]

use exactly the same indexed row-copy multiset.  Explicitly,

\[
(K\uplus P_0)\uplus(\rho K\uplus P_1)
=
(K\uplus P_1)\uplus(\rho K\uplus P_0).
\tag{2.4}
\]

At every depth,

\[
\mu_q^F+\mu_q^{\rho F}
=
\mu_q^{F'}+\mu_q^{\rho F'}
\tag{2.5}
\]

targetwise.  If

\[
X_q(A,B)=\sum_S\mu_q^A(S)\mu_q^B(S),
\tag{2.6}
\]

then

\[
\boxed{
Q_q(F)+Q_q(\rho F)-Q_q(F')-Q_q(\rho F')
=2\bigl[X_q(F',\rho F')-X_q(F,\rho F)\bigr].}
\tag{2.7}
\]

Since relabelling preserves floor energy,

\[
\boxed{
X_q(F',\rho F')-X_q(F,\rho F)
=Q_q(F)-Q_q(F').}
\tag{2.8}
\]

#### Proof

Equation (2.4) proves fixed-reservoir positivity, not merely equality of
middle incidence.  Put \(v_q=B_{m-q}g\).  Then

\[
\mu_q^{F'}=\mu_q^F+v_q,
\qquad
\mu_q^{\rho F'}=\rho\mu_q^F-v_q,
\]

which proves (2.5).

For each target \(S\), the sum of the two colour loads is fixed.  The
quadratic part of (0.1) therefore obeys

\[
x_0^2+x_1^2=(x_0+x_1)^2-2x_0x_1,
\]

while all linear terms are fixed.  Subtracting the two decompositions and
summing over targets proves (2.7).  Finally

\[
Q_q(\rho F)=Q_q(F),\qquad Q_q(\rho F')=Q_q(F'),
\]

so division of (2.7) by two gives (2.8).  \(\square\)

This is the smallest literal cross-bundle restitution cell.  In particular,
the phrase “cross-bundle exchange” below always means row-reservoir
preservation as in (2.4), not a parallel collection of factor-to-factor
trades which changes the aggregate rows.

---

## 3. Generic cyclic development with constant Haar curvature

Assume in this section that \(n\) is prime and identify the coordinate set
with \(\mathbb Z_n\).  Let \(T_a\) denote translation by \(a\).

### Lemma 3.1 — exact conjugated-translation collision probability

Let \(X,Y\) be distinct \(r\)-sets with

\[
t=|X\setminus Y|=|Y\setminus X|,
\]

let \(a\ne0\), and choose \(\sigma\) uniformly in \(S_n\).  Then

\[
\boxed{
\Pr(\sigma Y=\sigma X+a)
=\frac{nt}{r(n-r)\binom nr}.}
\tag{3.1}
\]

#### Proof

Condition on \(A=\sigma X\).  The set \(\sigma Y\) is uniform among the

\[
\binom rt\binom{n-r}t
\]

sets meeting \(A\) in \(r-t\) points.  Equality with \(A+a\) requires the
binary word of \(A\) along the \(a\)-cycle to have exactly \(t\) runs of
ones.  Since \(n\) is prime, that translation is one \(n\)-cycle, and the
number of such \(A\) is

\[
\frac nt\binom{r-1}{t-1}\binom{n-r-1}{t-1}.
\]

Divide by \(\binom nr\binom rt\binom{n-r}t\), and use

\[
\frac{\binom{r-1}{t-1}}{\binom rt}=\frac tr,
\qquad
\frac{\binom{n-r-1}{t-1}}{\binom{n-r}t}=\frac t{n-r}.
\]

This gives (3.1).  \(\square\)

For \(r\le(n-1)/2\), (3.1) is at most \(2/\binom nr\).

### Theorem 3.2 — simultaneous collision-free development

Fix \(H\le m-2\).  If

\[
\frac{8n^3}{W}+\frac{112nH}{N_H}<1,
\tag{3.2a}
\]

then there is a conjugation \(\sigma\) for which:

1. all \(2n\) translated negative rows

   \[
   T_a\sigma C,\quad T_a\sigma D
   \qquad(a\in\mathbb Z_n)
   \]

   form a middle packing; and

2. for every \(q\le H\), the translations of all distinct coordinates in
   \(\operatorname{supp}(B_{m-q}\sigma g)\) are pairwise distinct.

The total failure probability for uniform \(\sigma\) is at most

\[
\boxed{
\frac{8n^3}{W}+\frac{112nH}{N_H}.}
\tag{3.2}
\]

For \(H=\lceil A\sqrt m\rceil\) and fixed \(A\), this tends to zero, so
the conjugation exists for all sufficiently large prime \(n\).

#### Proof

The two old rows contain \(2n\) distinct middle owners.  A collision
between two different translated owners gives an equality of the form in
Lemma 3.1.  There are fewer than \(4n^2\) ordered base pairs and fewer than
\(n\) relative translations.  The bound \(2/W\) gives the first term of
(3.2).  A translate of one fixed owner cannot collide with another
translate of itself: a nonzero translation is an \(n\)-cycle, and no
nonempty proper subset is invariant under it when \(n\) is prime.

At any controlled depth the support size is at most eight.  There are at
most \(28\) unordered support pairs and fewer than \(n\) nonzero relative
translations.  Lemma 3.1 gives a bound \(2/N_q\) for each.  The more
conservative bound \(112n/N_q\), summed over \(q\le H\) and using
\(N_q\ge N_H\), gives the second term.  A union bound proves (3.2).
Both denominators are exponential in \(m\) on a fixed Gaussian window,
whereas the numerators are polynomial.  \(\square\)

Define

\[
G=\sum_{a\in\mathbb Z_n}T_a\sigma g.
\tag{3.3}
\]

### Corollary 3.3 — exact cyclic Haar norms

The negative side of \(G\) consists of \(2n\) rows covering \(2n^2\)
distinct middle owners.  Its positive side is also a middle packing, and

\[
\boxed{
\|B_{m-1}G\|_2^2=4n,
\qquad
\|B_{m-q}G\|_2^2=8n\quad(2\le q\le H).}
\tag{3.4}
\]

If

\[
S_H=\sum_{q=1}^H\frac1{c_q},
\]

then

\[
\boxed{
\|G\|_H^2
:=\sum_{q\le H}\frac{\|B_{m-q}G\|_2^2}{c_q}
=4n(2S_H-1).}
\tag{3.5}
\]

#### Proof

The negative packing is Theorem 3.2.  Since \(B_mG=0\), its positive
middle incidence equals the same \(0/1\) vector, so the positive side is
also a packing.  At each lower depth, Theorem 3.2 makes translated effect
supports disjoint.  Squared norms therefore add, and (1.6) gives (3.4).
Since \(c_1=1\), summation gives (3.5).  \(\square\)

### Theorem 3.4 — a fixed-reservoir \(2n\)-colour packet

Let \(F'=F+g\), as in Section 2.  For every \(a\), put

\[
F_a=T_a\sigma F,
\qquad
F'_a=T_a\sigma F',
\]

and

\[
\rho_a=T_a\sigma\rho\sigma^{-1}T_{-a}.
\tag{3.6}
\]

Then each pair

\[
(F_a,\rho_aF_a)
\longleftrightarrow
(F'_a,\rho_aF'_a)
\tag{3.7}
\]

is a row-reservoir-preserving exchange.  The \(n\) pairs together form one
literal reblocking on a fixed \(2n\)-colour reservoir, and every subset of
the \(n\) pair exchanges is legal.  Their fixed-window effect supports are
disjoint.

#### Proof

Conjugate and translate Theorem 2.1.  Different values of \(a\) use
different factor colours, so their row ledgers are disjoint even before
Theorem 3.2 is invoked.  Theorem 3.2 supplies disjoint target effects.
Thus any subset is a product of independent two-colour reblockings.
\(\square\)

### Proposition 3.5 — exact no-amplification for one developed seed

For every subset \(J\subseteq\mathbb Z_n\), the endpoint of (3.7) has
\(2|J|\) factor colours relabelled from \(F'\) and
\(2(n-|J|)\) factor colours relabelled from \(F\).  Hence

\[
\frac1{2n}\sum_i\mathcal Q_H(F_i^{(J)})
=\left(1-\frac{|J|}{n}\right)\mathcal Q_H(F)
 +\frac{|J|}{n}\mathcal Q_H(F').
\tag{3.8}
\]

In particular,

\[
\boxed{
\min_J\frac1{2n}\sum_i\mathcal Q_H(F_i^{(J)})
=\min\{\mathcal Q_H(F),\mathcal Q_H(F')\}.}
\tag{3.9}
\]

Thus cyclic development creates constant-curvature exchange capacity but
cannot, by itself, lower the best one-factor endpoint.

#### Proof

Every exchanged pair consists of coordinate relabellings of \(F'\), and
every unexchanged pair consists of relabellings of \(F\).  Energy is
relabel-invariant, giving (3.8)--(3.9).  \(\square\)

This is the decisive audit of the developed packet.  It prevents the
incorrect inference “\(n\) disjoint translated gains imply a new factor
with \(n\) times the improvement.”

---

## 4. Square-diagonal exchange: the exact positive Gram circuit

The preceding packet has identical translated gains.  A nontrivial
cross-bundle mechanism must correlate different cells.  The following
identity is the exact local mechanism.

Let one exact factor contain two owner-disjoint binary trades.  Write their
two row states as \(A_0,A_1\) and \(D_0,D_1\), where each pair of states
covers the same middle-owner block.  Let \(K\) cover the complement of the
two blocks.  Then all four factors

\[
F_{ij}=K\mathbin{\dot\cup}A_i\mathbin{\dot\cup}D_j,
\qquad i,j\in\{0,1\},
\tag{4.1}
\]

are literal exact factors.  Put

\[
u_q=\mu_q^{F_{10}}-\mu_q^{F_{00}},
\qquad
v_q=\mu_q^{F_{01}}-\mu_q^{F_{00}},
\]

and

\[
\langle u,v\rangle_H
=\sum_{q\le H}\frac{\langle u_q,v_q\rangle}{c_q}.
\tag{4.2}
\]

### Theorem 4.1 — square-diagonal restitution

The two-colour stacks

\[
\mathscr D_{\rm coh}=(F_{00},F_{11}),
\qquad
\mathscr D_{\rm split}=(F_{10},F_{01})
\tag{4.3}
\]

use the same indexed row-copy multiset, and

\[
\boxed{
\bigl[\mathcal Q_H(F_{00})+\mathcal Q_H(F_{11})\bigr]
-\bigl[\mathcal Q_H(F_{10})+\mathcal Q_H(F_{01})\bigr]
=2\langle u,v\rangle_H.}
\tag{4.4}
\]

Equivalently, the coherent-to-split cross-overlap gain is

\[
\boxed{\langle u,v\rangle_H.}
\tag{4.5}
\]

Consequently the lower-energy diagonal gains

\[
2|\langle u,v\rangle_H|
\]

over the higher-energy diagonal whenever the inner product is nonzero.

#### Proof

Both diagonals contain two copies of \(K\), one copy of each \(A_i\), and
one copy of each \(D_j\).  Hence (4.3) is a row-reservoir reblocking.

At one depth, abbreviate \(\mu_q^{F_{00}}\) by \(x\).  The four loads are

\[
x,\quad x+u_q,\quad x+v_q,\quad x+u_q+v_q.
\]

The linear part of the floor polynomial cancels between the two diagonals,
and

\[
\|x\|_2^2+\|x+u_q+v_q\|_2^2
-\|x+u_q\|_2^2-\|x+v_q\|_2^2
=2\langle u_q,v_q\rangle.
\]

Weight and sum over \(q\).  This proves (4.4).  The two-colour instance of
Theorem 2.1's cross-overlap identity gives (4.5).  \(\square\)

Theorem 4.1 is the precise positive interpretation of the class-covariance
gate: a useful multicolour exchange must make many such inner products have
the correct sign.  Orthogonal cells have zero diagonal gain, regardless of
their number or stationarity.

### Corollary 4.2 — balanced multi-fibre rounding inside a completed cube

Suppose an exact factor contains a conflict-free family of \(d\) universal
circuits.  Take \(M\) indexed copies of this completed owner-block
decomposition, and fix the number of copies using each side of every
circuit.  Arbitrarily reassigning those sides among the \(M\) backgrounds
preserves the complete indexed row reservoir and exact factorhood.  The
elementary two-colour swaps are the diagonal moves of Theorem 4.1.

If the side assignments are randomized independently by circuit, with
one-side frequency \(t_j\), then some deterministic reblocking satisfies

\[
\boxed{
\frac1M\sum_{i=1}^M\mathcal Q_H(F_i)
\le
\widetilde{\mathcal Q}_H(x(t))
+\sum_{j=1}^d t_j(1-t_j)\|g_j\|_H^2.}
\tag{4.6}
\]

Here \(x(t)\) is the common fractional midpoint profile.  For universal
circuits,

\[
\|g_j\|_H^2=4+8\sum_{q=2}^H\frac1{c_q}=4(2S_H-1).
\tag{4.7}
\]

#### Proof

For each output colour the independently permuted side variables have the
prescribed Bernoulli marginals.  Expand the quadratic floor polynomial.
Centered cross terms vanish, leaving the fractional midpoint energy plus
the displayed variances.  Average over colours and assignments, then
choose one deterministic assignment no larger than the mean.  Every
assignment is physical because the owner blocks are disjoint.  \(\square\)

This corollary is a true positive reblocking theorem.  Its unresolved input
is not rounding: one must construct a completed cube whose fractional
midpoint already has \(O_A(HB)\) energy.  The support-closed holonomy model
in the previous Lane-Y report shows that arbitrary exact middle cubes need
not have such a midpoint.

### Proposition 4.3 — the canonical fixed-level MSW cube has no depth-one diagonal gain

For any fixed concatenation level \(p\), the certified MSW universal
circuits indexed by \((P,R)\) have pairwise disjoint first-shadow effect
supports.  Hence, for two distinct cells in that common exact cube,

\[
\langle u_1,v_1\rangle=0.
\tag{4.8}
\]

Consequently every square-diagonal exchange among copies of this fixed-
\(p\) cube has zero depth-one energy gain.  More generally, if the number
of copies using each side of every cell is fixed, the total depth-one energy
is invariant under all reassignments of those sides among identical
background copies.

#### Proof

The exact MSW pivot theorem recovers \((P,R)\) from either endpoint side of
its first-shadow square; for fixed \(p\), distinct cells therefore have
disjoint four-target supports.  This gives (4.8).  In the multi-copy
statement, each depth-one target is affected by at most one cell.  Its
multiset of loads across factor colours depends only on the fixed number of
copies using the two sides of that cell, not on which backgrounds receive
them.  Summing the targetwise floor polynomial proves invariance.
\(\square\)

Thus the already completed positive-density \(p=0\) MSW atlas does not
realize the desired covariance route at the decisive first shadow.  One
must correlate cells from different contexts, where common applicability
is not supplied, or use genuinely nonlocal cells with overlapping
first-shadow actions.

### Proposition 4.4 — the complete concatenation-local atlas cannot repair the MSW first shadow

Let \(\mathscr Z_m\) be the complete fixed canonical family of
concatenation-local universal circuits over every boundary level \(p\),
excluding coordinate conjugates and dynamically created context columns.
It has exactly

\[
|\mathscr Z_m|=\operatorname{Cat}_{m-1}
\tag{4.9}
\]

columns, and its total first-shadow support \(U_1\) satisfies

\[
|U_1|\le4\operatorname{Cat}_{m-1}.
\tag{4.10}
\]

Every integral or fractional endpoint whose per-colour difference from the
canonical MSW factor lies in \(\operatorname{span}\mathscr Z_m\) has
unchanged depth-one loads outside \(U_1\).  This includes blockwise
multi-copy reassignments of the complete two-row sides of these columns;
it does not include arbitrary row-level reblockings of the same reservoir.
Consequently every such integral endpoint has
at least

\[
\boxed{
(2m-3)\operatorname{Cat}_{m-2}
-\frac{2W}{m+2}
-4\operatorname{Cat}_{m-1}
=\left(\frac1{16}-o(1)\right)W}
\tag{4.11}
\]

first-shadow holes, and hence

\[
\boxed{Q_1\ge\left(\frac18-o(1)\right)W.}
\tag{4.12}
\]

#### Proof

Every universal column has four first-shadow coordinates, proving (4.10).
Every linear combination of the columns vanishes outside their union, so
those loads are frozen under all of the stated positive specializations and
blockwise side reassignments.  The independently audited marked-gap theorem gives the
canonical MSW lower bound

\[
M_1(F_m^{\rm MSW})
\ge(2m-3)\operatorname{Cat}_{m-2}-\frac{2W}{m+2}.
\]

At most \(|U_1|\) of those holes can change.  This proves (4.11).  In the
unhalved normalization with \(c_1=1\), every remaining hole contributes

\[
(0-1)(0-2)=2
\]

to \(Q_1\), proving (4.12).  \(\square\)

Thus even arbitrary cross-level algebraic use of every known local
universal circuit is too sparse by a factor of order \(m\).  A successful
cyclic atlas must introduce nonlocal cells or use conjugated local cells in
new common completions; the existing MSW fibre cannot be saturated by
reassigning its local circuit states.

---

## 5. Depth-one capacity saturation in the Johnson-edge relaxation

This section isolates exactly what the saturating-cycle theorem does and
does not contribute.

Let

\[
N_1=\binom n{m-1},
\qquad
r=W-N_1=\frac{2W}{m+2}=\operatorname{Cat}_{m+1}.
\tag{5.1}
\]

The accepted saturating-cycle theorem gives a simple \(N_1\)-cycle in
\(J(n,m)\) using every \((m-1)\)-intersection colour exactly once.  It
omits a family \(\mathcal U\) of \(r\) middle vertices.

### Theorem 5.1 — balanced Hamilton relaxation

For every \(m\ge6\), the saturating cycle extends to a simple Hamilton
cycle \(H\) on all \(W\) middle vertices such that every lower colour has
load one or two, with exactly \(r\) colours of load two.  Hence

\[
Q_1(H)=0
\tag{5.2}
\]

in the scalar Johnson-edge relaxation.

#### Proof

For \(\mathcal A\subseteq\mathcal U\), put \(|\mathcal A|=\binom xm\)
with real \(x\ge m\).  Since

\[
r\le\binom{2m-1}m
\qquad(m\ge6),
\]

one has \(x\le2m-1\).  The Lovasz form of Kruskal--Katona gives

\[
|\partial\mathcal A|
\ge\binom{x}{m-1}
=\binom xm\frac{m}{x-m+1}
\ge|\mathcal A|.
\]

Hall's theorem therefore assigns every omitted middle set \(U\) a distinct
facet \(g(U)\subset U\).  Subdivide the unique old cycle edge of colour
\(g(U)\) by \(U\).  Distinct representatives subdivide distinct edges.
An unmatched colour remains single; a matched colour loses one edge and
gains two.  This proves the theorem.  \(\square\)

### Theorem 5.2 — exact orbit-stack saturation at the edge level

Let \(J=J(n,m)\).  The full indexed \(S_n\)-orbit of every spanning
Johnson two-factor is the uniform edge multigraph in which each edge of
\(J\) occurs

\[
\boxed{L=\frac{2n!}{m(m+1)}}
\tag{5.3}
\]

times.  In particular, the full edge orbit of the step-two graph of any
exact wreath factor can be reblocked exactly into the \(n!\) conjugates of
the Hamilton cycle \(H\) from Theorem 5.1.  Every output colour then has
\(Q_1=0\).

#### Proof

The Johnson graph is edge-transitive, has \(W\) vertices and degree
\(m(m+1)\), hence has \(Wm(m+1)/2\) edges.  A spanning two-factor has
\(W\) edges.  Its \(n!\) labelled conjugates therefore give the common
edge multiplicity

\[
\frac{n!W}{Wm(m+1)/2}=\frac{2n!}{m(m+1)}.
\]

This depends only on being a spanning two-factor.  Apply it to \(H\) and
to the step-two graph of an exact factor.  \(\square\)

Theorem 5.2 is a complete positive multicolour capacity theorem in the
edge relaxation.  It is not a row reblocking of wreaths.

### Proposition 5.3 — the first physical obstruction

In every genuine wreath factor, the Johnson edges of any fixed lower
colour form a matching.  The Hamilton cycle in Theorem 5.1 violates this
at every inserted vertex: its two incident edges have the same assigned
colour.  Consequently every proper coloured Johnson two-factor differs
from that Hamilton cycle in at least \(r\) edges of \(H\) (equivalently,
at least \(r\) edge/colour incidences).

#### Proof

At a middle window of a cyclic order, the two incident lower intervals are
the two distinct facets obtained by deleting its two positional endpoints.
Since an exact factor assigns the middle window to one wreath, two edges of
one lower colour cannot meet there.

At an inserted vertex \(U\), both new edges arose by subdividing the old
edge of colour \(g(U)\), so they meet at \(U\) with the same colour.
Different inserted vertices use different subdivided old edges.  At least
one edge in each resulting two-edge wedge must therefore change.  \(\square\)

The lower bound \(r=O(B)\) is at the permitted scale.  The deeper problem
is chronology, not its cardinality.

### Theorem 5.4 — exact chronology criterion

Let

\[
X_0X_1\cdots X_{n-1}X_0
\]

be an oriented \(n\)-cycle in \(J(n,m)\), and put

\[
S_i=X_i\cap X_{i+1}.
\]

It is the middle-window cycle of a cyclic coordinate order if and only if

\[
\boxed{
\#\{i:x\in S_i\}=m-1
\quad\text{for every }x\in[n].}
\tag{5.4}
\]

#### Proof

Put

\[
s_x=\#\{i:x\in X_i\},
\qquad
d_x=\#\{i:x\in X_i\setminus X_{i+1}\}.
\]

Then the left side of (5.4) is \(s_x-d_x\).  If it is \(m-1\), the
cyclic membership word of \(x\) is neither constantly zero nor constantly
one.  Hence \(d_x\ge1\), and \(s_x\ge m\).  Since

\[
\sum_xs_x=nm,
\]

all inequalities are equalities: \(s_x=m\), \(d_x=1\).  Thus each
coordinate leaves exactly once.  If \(a_i\) is the coordinate leaving at
step \(i\), the \(a_i\)'s are a permutation and, after a cyclic shift or
reversal of the indices,

\[
X_i=\{a_i,a_{i+1},\ldots,a_{i+m-1}\}.
\]

This is a wreath.  The converse is immediate.  \(\square\)

Thus global lower-colour balance, even with exact point margins after
averaging, does not imply the componentwise condition (5.4).

### Proposition 5.5 — translation-orbit grouping yields only AP wreaths

Assume \(n\) is prime.  Let \(S\) be an \((m-1)\)-set.  Its full
translation orbit

\[
\{S+a:a\in\mathbb Z_n\}
\tag{5.5}
\]

is the lower-colour family of one wreath only if, for some nonzero step
\(d\),

\[
S=b+\{0,d,2d,\ldots,(m-2)d\}.
\tag{5.6}
\]

Conversely every set of the form (5.6) has that property.  Hence all such
translation-orbit wreath families together contain only \(O(n^2)\) lower
targets, which is negligible compared with \(N_1\).

#### Proof

The \(n\) lower windows of a wreath form an \(n\)-cycle when two windows
are joined exactly when their intersection has size \(m-2\).  No
nonconsecutive positional windows have that intersection size.  Translation
by one preserves (5.5) and therefore acts as an order-\(n\) automorphism of
this cycle.  Since the order-\(n\) subgroup of the dihedral automorphism
group consists of rotations, after reindexing there is a nonzero \(d\)
such that consecutive lower windows are \(S,S+d,S+2d,\ldots\).

Consecutiveness gives \(|S\setminus(S+d)|=1\).  In the binary word of
\(S\) around the \(d\)-cycle, this is exactly one run of ones.  Thus
\(S\) is the arithmetic-progression interval (5.6).  The converse is
immediate by taking the cyclic coordinate order of common difference
\(d\).  There are only polynomially many choices of step and translate.
\(\square\)

Thus the prime-dimensional orbit correction in Theorem 6.1 cannot be
lifted by simply grouping its target orbits one by one into wreaths.  A
successful lift must mix several target orbits inside every non-AP wreath.

---

## 6. PBBS: an exact affine target and a one-packet obstruction

Let \(P_m\) be the canonical PBBS spanning two-factor of the odd graph.
It is componentwise point-regular, but its components may have length
\(\ell n\), \(\ell>1\), so it is not an exact wreath factor.

Let \(\mu_P(K)\in\{1,2,3\}\) be its first-angle load at the
\((m-1)\)-core \(K\), and put

\[
a_j=\#\{K:\mu_P(K)=j\}.
\]

Then

\[
a_2+2a_3=r,
\qquad
a_1=\frac{m-2}{m+2}W+a_3,
\qquad
Q_1(P_m)=2a_3\le\frac{2W}{m+2}<4B,
\tag{6.1}
\]

where the last \(Q_1\) uses the unhalved normalization (0.1).

### Theorem 6.1 — prime-dimensional affine correction

Assume \(n>3\) is prime.  The load classes are unions of free translation
orbits.  Let \(\mathcal H\) be the load-three class.  Choose a union
\(\mathcal L\) of exactly \(a_3/n\) full translation orbits from the
load-one class, and put

\[
\mu^*=\mu_P-\mathbf1_{\mathcal H}+\mathbf1_{\mathcal L}.
\tag{6.2}
\]

Then

\[
\mu^*(K)\in\{1,2\}\quad\text{for every }K,
\qquad Q_1(\mu^*)=0,
\tag{6.3}
\]

and

\[
\boxed{
\sum_K(\mu^*(K)-\mu_P(K))\mathbf1_K=0.}
\tag{6.4}
\]

#### Proof

Translation acts freely on every nonempty proper subset of \(\mathbb Z_n\),
so \(n\mid a_j\).  Equation (6.1) gives enough load-one orbits to choose
\(\mathcal L\).  Formula (6.2) lowers every 3 to 2 and raises the chosen
1's to 2, proving (6.3).  Every full translation orbit of \((m-1)\)-sets
has incidence sum

\[
(m-1)\mathbf1.
\]

The two selected orbit families have the same number of orbits, proving
(6.4).  \(\square\)

Theorem 6.1 removes scalar balance, integrality, rotation symmetry, and
point margins from the list of possible depth-one obstructions.  It does
not realize \(\mu^*\) by positive factor switches.

### Theorem 6.2 — every explicit clean PBBS seed has nonzero first-shadow action

Let \(K\) be a load-one core, put \(T=[n]\setminus K\), and let

\[
u_0\to u_1\to u_2\to u_3\to u_0
\]

be its explicit clean directed \(C_4\) in the PBBS residual digraph.  Put

\[
A_i=K\cup\{u_i\},
\qquad
B_i=T\setminus\{u_i,u_{i+1}\}.
\]

Let \(w_i\) be the other out-neighbour of \(u_i\), and write the retained
neighbour of \(B_i\) as

\[
K\setminus\{c_i\}\cup\{u_i,u_{i+1}\},
\qquad c_i\in K.
\]

The exact first-shadow increment of the clean alternating \(C_8\) is

\[
\begin{aligned}
\delta_{K,1}
={}&\sum_{i\in\mathbb Z_4}
\left(
 e_{T\setminus\{u_{i-1},u_i,w_i\}}
-e_{T\setminus\{u_i,u_{i+1},w_i\}}
\right)\\
&+\sum_{i\in\mathbb Z_4}
\left(
 e_{K\setminus\{c_i\}\cup\{u_{i+1}\}}
-e_{K\setminus\{c_i\}\cup\{u_i\}}
\right).
\end{aligned}
\tag{6.5}
\]

The first line is supported on targets disjoint from \(K\), the second on
targets meeting \(K\) in \(m-2\) points.  In both possible load-one
cyclic types, the first line reduces to a nonzero four-colour rectangle

\[
e_{R_0}+e_{R_2}-e_{R_1}-e_{R_3},
\tag{6.6}
\]

whose four targets are distinct and satisfy

\[
\mathbf1_{R_0}+\mathbf1_{R_2}
=\mathbf1_{R_1}+\mathbf1_{R_3}.
\tag{6.7}
\]

Consequently

\[
\boxed{\delta_{K,1}\ne0,\qquad\|\delta_{K,1}\|_1\ge4.}
\tag{6.8}
\]

#### Proof

At \(A_i\), compare the angle made by the alternating edge with the
retained PBBS neighbour; this gives the first line of (6.5).  At \(B_i\),
the same comparison gives the second line.  The support intersection
counts show that the two lines are disjoint.

For the disjoint-mark cyclic type

\[
a_0,a_1,a_2,c_0,c_1,c_2,
\qquad
(u_0,u_1,u_2,u_3)=(a_2,a_1,c_0,c_1),
\]

the predecessor/successor law gives

\[
(w_0,w_1,w_2,w_3)=(u_2,a_0,u_0,c_2).
\]

the first line is

\[
\begin{aligned}
&+e_{T\setminus\{u_0,u_1,a_0\}}
+e_{T\setminus\{u_2,u_3,c_2\}}\\
&-e_{T\setminus\{u_1,u_2,a_0\}}
-e_{T\setminus\{u_3,u_0,c_2\}}.
\end{aligned}
\tag{6.9}
\]

For the shared-mark type, the same predecessor/successor calculation gives

\[
(w_0,w_1,w_2,w_3)=(u_2,x,u_0,x),
\]

and the same formula holds with both anchors \(a_0,c_2\) replaced by the
shared mark \(x\).  Direct comparison shows that the
four targets are distinct and proves (6.7).  Since the second line has
disjoint support, it cannot cancel (6.9).  This proves (6.8).  \(\square\)

### Lemma 6.3 — parity of every odd-factor first-shadow increment

For any spanning two-factor \(G\) of the odd graph, let \(e_G(x)\) count
its edges whose omitted label is \(x\).  Then

\[
\boxed{
\sum_S\mu_1^G(S)\mathbf1_S
=\sum_X\mathbf1_{X^c}-2e_G.}
\tag{6.10}
\]

Hence every switch increment \(\delta\) satisfies

\[
\sum_S\delta(S)\mathbf1_S\in(2\mathbb Z)^n.
\tag{6.11}
\]

In particular, no nonzero mass-zero first-shadow increment has
\(\ell^1\)-norm two.  If a norm-four increment has four distinct unit
coordinates

\[
\delta=e_A+e_B-e_C-e_D,
\]

then it necessarily obeys only the parity relation

\[
\mathbf1_A+\mathbf1_B
\equiv\mathbf1_C+\mathbf1_D\pmod2.
\tag{6.11a}
\]

This congruence does not imply equality over \(\mathbb Z\).  The exact
affine equality (6.7) is a stronger special property of the explicit PBBS
far rectangle.

#### Proof

At a middle vertex \(X\), let \(a,b\in X^c\) be the omitted labels of its
two incident factor edges.  Its angle is

\[
X^c\setminus\{a,b\}.
\]

Summing its incidence vector over all \(X\) gives the fixed complement
sum, minus one copy of each incident omitted label.  Every factor edge has
two endpoints, giving (6.10).  Subtract two factors to obtain (6.11).
If a mass-zero vector had norm two, it would be \(e_A-e_B\); (6.11) would
force \(\mathbf1_A-\mathbf1_B\) even, hence \(A=B\).  \(\square\)

For an \((m-1)\)-core \(K\), define its first-shadow support envelope

\[
\Sigma(K)=
\left\{S\in\binom{[n]}{m-1}:
|S\cap K|\in\{0,m-2\}\right\}.
\tag{6.11b}
\]

Formula (6.5) gives

\[
\operatorname{supp}(\delta_{K,1})\subseteq\Sigma(K).
\tag{6.11c}
\]

Call \(K\) **rotation-separated** when, for every nonzero
\(a\in\mathbb Z_n\),

\[
2\le|K\cap(K+a)|\le m-5.
\tag{6.11d}
\]

The envelopes obey the elementary separation law

\[
\Sigma(K)\cap\Sigma(K')\ne\varnothing
\quad\Longrightarrow\quad
|K\cap K'|\le1\ \text{ or }\ |K\cap K'|\ge m-4.
\tag{6.11e}
\]

Indeed, a common target disjoint from both cores forces their union into
an \((m+2)\)-set; a target meeting both in \(m-2\) points makes both cores
one-element modifications of it; and in the mixed case the two cores can
meet only in the unique core point outside that target.  Thus a
rotation-separated core has pairwise disjoint translated envelopes.

### Theorem 6.4 — one separated rotation packet cannot perform the affine transfer

Suppose \(K\) is rotation-separated, so the translated support envelopes
of its clean increments are pairwise disjoint.  Put

\[
\Delta_K=\sum_{j=0}^{n-1}T_j\delta_{K,1}.
\tag{6.12}
\]

Then

\[
\|\Delta_K\|_1=n\|\delta_{K,1}\|_1\ge4n,
\tag{6.13}
\]

and \(\Delta_K\) meets every translation orbit of targets in at most one
developed seed orbit.  Therefore

\[
\boxed{
\Delta_K\ne
\mathbf1_{\mathcal O(L)}-\mathbf1_{\mathcal O(H)}}
\tag{6.14}
\]

for every two target orbits \(\mathcal O(L),\mathcal O(H)\).

#### Proof

Disjoint translated supports make the \(\ell^1\)-norm additive, and
Theorem 6.2 gives (6.13).  A pure high-orbit/low-orbit transfer has
\(\ell^1\)-norm \(2n\).  Thus it cannot equal \(\Delta_K\).  Moreover,
if two base support targets lay in one translation orbit, the seed support
would meet a nontrivial translate of itself, contradicting (6.11d)--
(6.11e).  This proves the target-orbit assertion.  \(\square\)

The support-envelope calculation gives a quantitative cross-packet locus.
If packets based at \(K,K'\) can share a target orbit, then for some shift
\(a\),

\[
|K\cap(K'+a)|\le1
\quad\text{or}\quad
|K\cap(K'+a)|\ge m-4.
\tag{6.15}
\]

For a fixed core orbit, the number of possible neighbouring core orbits is
at most

\[
\boxed{
D_m=
\binom{m+2}{3}
+(m-1)\binom{m+2}{4}
+\sum_{s=0}^3\binom{m-1}{s}\binom{m+2}{s}
=O(m^6).}
\tag{6.16}
\]

Indeed, the first two terms count the far configurations and the final sum
counts symmetric differences of size at most six.  Thus cancellation is
not diffuse: it must be routed through a polynomial-degree near/far graph.

### Proposition 6.5 — componentwise positive-short-path barrier

Assume \(n\) is prime.  A balanced exact \(n\)-vertex output component
cannot contain a positive distinguished PBBS three-vertex residual path if
all its other residual pieces have zero centered charge.

#### Proof

If the component contains \(t\) distinguished paths with cores \(K_i\),
their charges give

\[
n\sum_{i=1}^t\mathbf1_{K_i}
=(m-1)t\mathbf1.
\]

Since \(\gcd(n,m-1)=1\), one has \(n\mid t\).  Disjoint three-vertex paths
inside an \(n\)-vertex component also give \(3t\le n\).  Hence \(t=0\).
\(\square\)

Therefore global cancellation of a full rotation orbit of centered charges
does not sew exact wreaths.  Every affected wreath must contain explicit
negative nonzero residual charge as well.

---

## 7. Why ordinary zero-voltage packet matching cannot finish

For prime \(n\), quotient masks by coordinate translation.  At depth
\(q\), the quotient target count is

\[
M_q=\frac{N_q}{n}.
\]

A translation-rainbow full packet uses \(n\) quotient targets at every
depth.  An ordinary matching which insists on using every quotient target
at most once can therefore select at most

\[
\frac{M_H}{n}=\frac{N_H}{n^2}
\tag{7.1}
\]

packets.  Covering the middle layer requires \(W/n^2\) packets.  Hence an
ordinary matching covers at most the fraction

\[
\boxed{
\frac{N_H}{W}
=\prod_{j=0}^{H-1}\frac{m-j}{m+2+j}
=e^{-A^2+o(1)}}
\tag{7.2}
\]

when \(H=A\sqrt m+O(1)\).

Thus ordinary disjoint packet matching loses a positive fraction for every
fixed \(A>0\).  The needed theorem is capacitated: quotient target loads
must be \(c_q\) or \(c_q+1\), not at most one.

For a translation-invariant packet selection with quotient loads
\(\ell_q(v)\), the exact energy is

\[
\boxed{
Q_q=n\sum_{v}
(\ell_q(v)-c_q)(\ell_q(v)-c_q-1).}
\tag{7.3}
\]

Consequently \(Q_q=O(B)\) requires floor/ceiling accuracy on all but
\(O(M_q/n)\) quotient cells, not merely an ordinary near matching.

The companion report
`MATH_ATTACK_Y9_ZERO_VOLTAGE_PACKET_HYPERGRAPH_AUDIT_20260725.md`
proves exact generic degrees and an \(O(1/m)\) relative pair-codegree bound
for the natural packet incidence multihypergraph.  Those facts do not imply
the required result: the edge uniformity is

\[
n(H+1)=\Theta_A(m^{3/2}),
\]

and low relative codegree alone is not a growing-uniformity matching
theorem.  More importantly, (7.2) shows that the wrong uncapacitated
matching objective is impossible even if such a theorem were available.

---

## 8. Conditional constant-one implication of a completed cyclic atlas

The positive theorem above composes quantitatively if the missing common
completion and correlation estimate are supplied.

### Theorem 8.1 — completed cyclic-Haar criterion

Fix \(A>0\), \(H=\lceil A\sqrt m\rceil\), and suppose one exact factor
contains \(d\) owner-disjoint universal circuits, with

\[
d\le B/2.
\]

If a point \(x\) in their real cube satisfies

\[
\widetilde{\mathcal Q}_H(x)=O_A(HB),
\tag{8.1}
\]

then some literal exact cube vertex satisfies

\[
\mathcal Q_H=O_A(HB)=O_A(W/\sqrt m)=o(W).
\tag{8.2}
\]

#### Proof

Independent Bernoulli rounding, or the row-preserving multi-fibre version
in Corollary 4.2, has toll at most

\[
\frac14d\left(4+8\sum_{q=2}^H\frac1{c_q}\right)
\le BS_H-\frac B2
\le HB.
\]

Add (8.1).  Since \(HB=H W/n=O_A(W/\sqrt m)\), this proves (8.2).
The already audited literal exact-factor transfer and slow diagonal then
give the coefficient-one contiguous-OR theorem.  \(\square\)

The theorem is deliberately conditional only at the actual missing gate.
The cyclic-Haar circuits, positivity, exact row reservoir, norms, and
rounding constants are proved.  The following are **not** proved:

1. a one-factor completion of one generic \(2n\)-row developed packet;
2. a positive-density family of such completed packets;
3. a midpoint satisfying (8.1);
4. a sign/diagonal theorem forcing the cross-bundle Gram gain in (4.4) to
   saturate (0.6);
5. an exact-wreath lift of the balanced Johnson Hamilton orbit;
6. a PBBS packet matching satisfying both the explicit first-shadow
   cancellation and componentwise negative-charge sewing conditions.

---

## 9. Independent audit of the decisive steps

The following checks were performed independently of the initial
derivations.

### 9.1 Reservoir audit

The all-forward developed trade

\[
\sum_a T_a\sigma g
\]

does **not** preserve an orbit-stack row reservoir.  It changes every old
pair to a new pair.  The fixed-reservoir statement is instead (2.4), which
uses the inverse trade in the \(\rho\)-partner fibre.  Every occurrence of
\(K,\rho K,P_0,P_1\) appears once on both sides.  This correction is
essential.

### 9.2 Norm audit

At \(q=1\), the two \(O\)-terms in (1.5) cancel and four unit coordinates
remain, giving norm squared four.  For \(2\le q\le H\le m-2\), all eight
signed target coordinates are distinct, giving norm squared eight.  Translation
separation makes these norms add exactly \(n\) times; there is no hidden
factor of two.  Thus (3.4), not \(8n,16n\), is correct.

### 9.3 Energy/cross-overlap audit

For two colour loads with fixed targetwise total,

\[
x_0^2+x_1^2=T^2-2x_0x_1.
\]

The floor-polynomial linear terms depend only on \(T\).  Hence old energy
minus new energy is exactly twice new cross overlap minus old cross
overlap.  Relabel symmetry then gives (2.8).  The same expansion on a
Boolean square gives exactly \(2\langle u,v\rangle\), confirming (4.4).

### 9.4 Translation union-bound audit

Lemma 3.1 counts conjugated equality for one ordered relative translation.
Using support size eight, fewer than \(28n\) unordered pair/shift tests, and
the bound \(2/N_q\) actually gives \(56n/N_q\).  The displayed
\(112n/N_q\) is a valid factor-two safety margin.  The middle bound
\(8n^3/W\) is likewise conservative.  Both remain \(o(1)\).

### 9.5 Scope audit

Theorem 5.2 reblocks Johnson **edge copies**, not wreath rows.  PBBS is a
point-regular spanning two-factor, not an exact wreath factor.  Theorem 6.1
is an affine target histogram, not a physical switch realization.  The
ordinary packet matching obstruction (7.2) does not rule out capacitated
floor/ceiling resolution.  Finally, Theorem 8.1 is conditional on a low
completed midpoint and is not asserted as a proof of constant one.

## 10. Final proved/conditional boundary

The lane now has the requested genuine cyclic cross-bundle coherence:

\[
\boxed{
\text{universal Haar cell}
+\text{swapping involution}
+\text{cyclic development}
\Longrightarrow
\text{literal fixed-reservoir }2n\text{-colour exchanges}.}
\]

Its exact multidepth action is constant per translated circuit, and
square-diagonal exchanges realize cross-bundle covariance with equality.

What remains is not a restitution identity, parity repair, stationary-law
calculation, or ordinary matching.  It is the following positive theorem.

> **Cyclic correlated completion gate.**  Construct, inside one orbit-stack
> row reservoir, a family of commonly completable cyclic Haar cells whose
> nonorthogonal square-diagonal inner products admit a positive assignment
> with
> \[
> \sum_{q\le A\sqrt m}\frac{X_q^{\max}-X_q}{c_q}=o(kW).
> \]

The PBBS calculation proves that one separated core orbit cannot be that
family; the zero-voltage calculation proves that an uncapacitated packet
matching cannot be that family.  A solution must correlate distinct
near/far core bundles or supply a new growing physical atom with a
low-energy completed midpoint.
