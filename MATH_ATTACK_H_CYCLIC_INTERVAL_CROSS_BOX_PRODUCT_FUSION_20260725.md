# Cyclic-interval near-designs: automatic cross-box fusion, an exact
# alternating product sheet, and a dense-core factorisation obstruction

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad B=\frac Wn.
\]

This report does not prove the mesoscopic cyclic-interval near-design
theorem.  It settles the cross-box part of that route in three precise
ways.

1. **The fixed-box endpoint dual is not an additional obstruction.**
   Any cyclic near-design with \(W+o(W)\) pointed starts can be globally
   relabelled so that its already existing literal band flags supply
   \(\Theta_A(HW)\) cross-box endpoint incidences when
   \(H=A\sqrt m+O(1)\).  In particular, \(O_A(W/H)\) pointed starts carry
   \(\Omega_A(W)\) globally distinct targets in distinct product boxes.
   This is stronger than the \(\Theta_A(W)\) sharing forced by the audited
   fixed-box shoulder duals.

2. **There is an exact coefficient-one product primitive.**  Given cyclic
   orders on two disjoint even \(s\)-sets, \(s/2\) alternating phase
   interleavings cover every even product sheet exactly once.  At every
   odd sheet they cover exactly one parity half.  Taking the other phase
   parity fills the missing half but duplicates the whole even sheet.
   Thus the remaining product problem is an exact correlated parity/frame
   selection problem, not a local seam problem.

3. **A proposed owner-spread factorisation lemma is false.**  There is an
   owner-scale family of legal return-free fragments whose departure
   degrees are at most \(B\), whose starting owners are all distinct, and
   whose number is \((1+o(1))W/h\), but whose departure chromatic index is
   \((2-o(1))B\).  It is a product of disjoint \((2h-1)\)-coordinate
   dense cores.  Cross-core seam fusion is fully available, but every
   packet can use at most one fragment from each core.

Consequently, unrestricted cross-box endpoint sharing is quantitatively
ample.  The surviving coefficient-one gate is a common packet
factorisation and correlated cross-frame parity selection which preserves
the middle partition and covers the bounded-degree odd sheets.  Point
degrees, distinct starting owners, and local literal extendibility do not
imply that factorisation.

## 1. The exact near-design target

For an oriented cyclic order
\(\pi=(z_0,\ldots,z_{n-1})\), put

\[
 I_\pi(j,r)=\{z_j,z_{j+1},\ldots,z_{j+r-1}\},
 \qquad j\in\mathbb Z_n.
\tag{1.1}
\]

For an indexed family \(\mathcal P\) of cyclic orders, let
\(\mathcal I_r(\mathcal P)\) be the set of distinct length-\(r\)
intervals occurring in its members.  Put

\[
 N_q=\binom n{m-q}=\binom n{m+1+q},
\tag{1.2}
\]

\[
 M_q^-=N_q-|\mathcal I_{m-q}(\mathcal P)|,\qquad
 M_q^+=N_q-|\mathcal I_{m+1+q}(\mathcal P)|.
\tag{1.3}
\]

The mesoscopic cyclic-interval near-design statement is

\[
 |\mathcal P|=(1+o(1))B
\tag{1.4}
\]

and

\[
 \boxed{\sum_{q=0}^{H}(M_q^-+M_q^+)=o(W).}
\tag{1.5}
\]

The deficit in (1.5) is aggregate across all \(2H+2\) ranks.

For one packet, put

\[
 E_j=I_\pi(j,m-H).
\tag{1.6}
\]

The literal word

\[
 E_0,E_1,\ldots,E_{n-1},E_0,E_1,\ldots,E_{2H}
\tag{1.7}
\]

satisfies

\[
 \bigvee_{u=0}^{t-1}E_{j+u}
 =I_\pi(j,m-H+t-1),
 \qquad 1\le t\le2H+2.
\tag{1.8}
\]

Thus a near-design compiles literally at cost

\[
 (n+2H+1)|\mathcal P|+\sum_{q\le H}(M_q^-+M_q^+)
 =W+o(W)
\tag{1.9}
\]

whenever \(H=o(m)\).  The issue below is construction of
\(\mathcal P\), not literalization.

## 2. Automatic cross-box sharing after one relabelling

Fix a partition of \([n]\) into \(b\) coordinate blocks, where \(b\) is
fixed, and fix a symmetric-chain decomposition in each block.  Their
products partition the Boolean lattice into product boxes.

Let \(\mathcal P\) be any indexed packet family.  From every distinct band
target covered by \(\mathcal P\), choose exactly one witnessing occurrence.
This assignment is made before any relabelling.  Write

\[
 M=n|\mathcal P|
\tag{2.1}
\]

for the number of pointed starts and \(K\) for the number of assigned
targets.

For a pointed start \(x\), let \(k_x\) be the number of its assigned
targets.  After a coordinate relabelling \(\sigma\), let \(c_x(\sigma)\)
be the number of distinct product boxes containing these \(k_x\) nested
targets.

### Lemma 2.1 (same-box extension probability)

Let \(X\subset Y\) be two fixed assigned targets at one pointed start and
put

\[
 d=|Y|-|X|\ge1.
\]

For a uniform coordinate permutation \(\sigma\),

\[
 \boxed{
 \Pr(\sigma X,\sigma Y\text{ lie in one product box})
 \le
 \frac{\binom{d+b-1}{b-1}}
      {\binom{m+1-H}{d}}.}
\tag{2.2}
\]

#### Proof

Condition on \(\sigma X\).  The difference
\(\sigma Y\setminus\sigma X\) is uniform among the \(d\)-subsets of
\([n]\setminus\sigma X\).  Since \(|X|\le m+H\), there are at least

\[
 \binom{m+1-H}{d}
\]

possible extensions.

Inside one product box, an extension is determined by the rank increments
made in the \(b\) factor chains.  Their nonnegative increments sum to
\(d\), so there are at most

\[
 \binom{d+b-1}{b-1}
\]

possibilities.  Some weak compositions may violate a chain endpoint;
discarding them only strengthens the upper bound. \(\square\)

Let \(Q(\sigma)\) count unordered pairs of assigned targets which have a
common pointed start and lie in one product box after applying \(\sigma\).
There are at most \(2H+2-d\) pairs of band ranks with difference \(d\).
Lemma 2.1 gives

\[
 \mathbb E Q
 \le
 M\sum_{d=1}^{2H+1}
 (2H+2-d)
 \frac{\binom{d+b-1}{b-1}}
      {\binom{m+1-H}{d}}.
\tag{2.3}
\]

Put

\[
 a_d=
 \frac{\binom{d+b-1}{b-1}}
      {\binom{m+1-H}{d}}.
\]

Then

\[
 \frac{a_{d+1}}{a_d}
 =\frac{d+b}{m+1-H-d}.
\tag{2.4}
\]

If \(H=o(m)\), the ratio in (2.4) is \(o(1)\), uniformly for
\(d\le2H+1\).  Hence the \(d=1\) term dominates and

\[
 \boxed{\mathbb E Q=O_b(MH/m).}
\tag{2.5}
\]

### Theorem 2.2 (automatic literal cross-box fusion)

There is a coordinate relabelling \(\sigma\) for which

\[
 \boxed{
 \sum_x(c_x(\sigma)-1)_+
 \ge K-M-O_b(MH/m).}
\tag{2.6}
\]

Every unit on the left is a literal common-left-endpoint incidence between
two distinct product boxes in the word (1.7).

#### Proof

At start \(x\), write \(k_{x,\mathcal B}\) for the number of assigned
targets in box \(\mathcal B\).  Then

\[
 k_x-c_x
 =\sum_{\mathcal B:k_{x,\mathcal B}>0}
   (k_{x,\mathcal B}-1)
 \le
 \sum_{\mathcal B}\binom{k_{x,\mathcal B}}2.
\tag{2.7}
\]

After summing (2.7),

\[
 \sum_x(c_x-1)_+
 \ge K-M-Q.
\tag{2.8}
\]

Choose \(\sigma\) with \(Q(\sigma)\le\mathbb EQ\), and use (2.5).
All assigned targets at one pointed start are the unions in (1.8)
beginning at its one physical occurrence \(E_j\).  Thus the sharing in
(2.6) is literal. \(\square\)

The same proof works simultaneously for \(J\) fixed product partitions
provided

\[
 JH/m=o(1)
\tag{2.9}
\]

with their numbers of factors uniformly bounded: sum their same-box pair
counts before choosing \(\sigma\).

### Corollary 2.3 (a near-design overpays the fixed-box dual)

Assume

\[
 H=A\sqrt m+O(1),\qquad A>0\text{ fixed},
\tag{2.10}
\]

and that \(\mathcal P\) satisfies (1.4)--(1.5).  Then some relabelling
has

\[
 \boxed{
 \sum_x(c_x-1)_+=\Theta_A(HW).}
\tag{2.11}
\]

Moreover, \(O_A(W/H)\) pointed starts contain
\(\Omega_A(W)\) globally distinct assigned targets belonging to distinct
product boxes.

#### Proof

For \(0\le q\le A\sqrt m+O(1)\), the exact ratio

\[
 \frac{N_q}{W}
 =\prod_{j=0}^{q-1}\frac{m-j}{m+2+j}
\tag{2.12}
\]

is bounded below by a positive constant depending only on \(A\).
Indeed, taking logarithms and using
\(-\log(1-u)\le u+2u^2\) in the displayed range gives

\[
 \log(W/N_q)\le A^2+o_A(1).
\]

Consequently

\[
 K=2\sum_{q=0}^{H}N_q-o(W)=\Theta_A(HW).
\tag{2.13}
\]

Also \(M=n|\mathcal P|=W+o(W)\), and (2.5) is \(o(W)\).  Equations
(2.6) and (2.13) prove the lower bound in (2.11); the upper bound follows
from \(c_x\le2H+2\).

Order the values \((c_x-1)_+\) decreasingly and take the largest
\(\lceil W/H\rceil\).  Their average is at least the average over all
\(M=(1+o(1))W\) starts.  By (2.11), their sum is
\(\Omega_A(W)\).  The assigned targets were globally distinct, and
within each retained start one may keep one target from every represented
box. \(\square\)

More generally, if \(\mathcal D\) is any prescribed audited shoulder
family with

\[
 |\mathcal D|\ge\kappa HW,
\tag{2.14}
\]

then the same conclusion holds with constants depending on
\(\kappa\), after restricting the fixed global assignment to covered
members of \(\mathcal D\).  At most the total \(o(W)\) band holes lie in
\(\mathcal D\), while its same-box pair count is bounded by the global
quantity \(Q\).

The fixed-box endpoint dual asks for only \(\Theta(W)\) endpoint--box
sharing in every compact positive-mass sector.  Corollary 2.3 supplies
\(\Theta_A(HW)\).  Hence the dual rules out sparse or prealigned seams,
but it cannot obstruct a genuine cyclic near-design with unrestricted
cross-box sharing.

## 3. An exact alternating-child product sheet

Let

\[
 A=(a_0,\ldots,a_{s-1}),\qquad
 C=(c_0,\ldots,c_{s-1})
\]

be cyclic orders on disjoint \(s\)-sets, with \(s\) even.  For
\(\delta\in\mathbb Z_s\), define the alternating parent order

\[
 \tau_\delta=
 (a_0,c_\delta,a_1,c_{\delta+1},\ldots,
  a_{s-1},c_{\delta+s-1}).
\tag{3.1}
\]

All indices below are cyclic.

### Theorem 3.1 (alternating product fusion)

Fix \(\varepsilon\in\{0,1\}\) and retain the \(s/2\) orders with

\[
 \delta\equiv\varepsilon\pmod2.
\tag{3.2}
\]

For every

\[
 1\le q\le s-2,
\tag{3.2a}
\]

their length-\(2q\) intervals cover exactly once every
target

\[
 I_A(u,q)\cup I_C(v,q),
\qquad (u,v)\in\mathbb Z_s^2.
\tag{3.3}
\]

At length \(2q+1\), they cover exactly once

\[
 \begin{aligned}
 &I_A(u,q+1)\cup I_C(v,q)
 &&\text{when }v-u\equiv\varepsilon\pmod2,\\
 &I_A(u,q)\cup I_C(v,q+1)
 &&\text{when }v-u\equiv1-\varepsilon\pmod2,
 \end{aligned}
\tag{3.4}
\]

and no other targets of these two product types.

The displayed interval identities remain valid at the boundary values
\(q=0,s-1,s\), but the exact-once assertions do not: an empty or full
child interval is independent of its nominal starting phase.  The proper
interior range (3.2a) is the one used in product-box fusion.

#### Proof

A direct reading of (3.1) gives

\[
 I_{\tau_\delta}(2i,2q)
 =I_A(i,q)\cup I_C(i+\delta,q),
\tag{3.5}
\]

\[
 I_{\tau_\delta}(2i+1,2q)
 =I_A(i+1,q)\cup I_C(i+\delta,q).
\tag{3.6}
\]

For a prescribed pair \((u,v)\), put \(d=v-u\).  If
\(d\equiv\varepsilon\), it occurs uniquely in (3.5) with
\((i,\delta)=(u,d)\).  Otherwise it occurs uniquely in (3.6) with

\[
 (i,\delta)=(u-1,d+1).
\]

This proves (3.3).

Similarly,

\[
 I_{\tau_\delta}(2i,2q+1)
 =I_A(i,q+1)\cup I_C(i+\delta,q),
\tag{3.7}
\]

\[
 I_{\tau_\delta}(2i+1,2q+1)
 =I_A(i+1,q)\cup I_C(i+\delta,q+1).
\tag{3.8}
\]

The differences of the two starting indices are respectively
\(\delta\) and \(\delta-1\).  Equations (3.2), (3.7), and (3.8) prove
(3.4), including uniqueness. \(\square\)

The coefficient ledger is exact.  The retained orders have

\[
 \frac s2(2s)=s^2
\tag{3.9}
\]

pointed starts, exactly the size of the even sheet (3.3).  Compiling a
depth-\(H\) band adds

\[
 \frac s2(2H+1)=o(s^2)
\tag{3.10}
\]

letters when \(H=o(s)\).

Taking both values of \(\varepsilon\) fills the two odd product sheets,
but every target in (3.3) then occurs twice and the pointed-start count
becomes \(2s^2\).  Thus paying for both local phases loses a full leading
coefficient.  A multiscale iteration must choose one phase in every
parent while using other frames to cover the complementary odd targets.
This is the exact correlated phase gate.

## 4. A dense-core obstruction to owner-spread factorisation

The following theorem corrects the proposed abstract stability statement

\[
 |\mathcal F|\le(1+o(1))B\,\nu(\mathcal F)
\tag{4.1}
\]

under only point-degree and distinct-owner hypotheses.

Choose an integer \(h\) satisfying

\[
 \log n=o(h),\qquad h=o(m).
\tag{4.2}
\]

Choose an even \(z=O(\log n)\) minimally so that

\[
 \binom z{z/2}\ge\frac n{2h-1}.
\tag{4.3}
\]

Reserve a \(z\)-set \(Z\), and partition all but fewer than \(2h-1\) of
the other coordinates into

\[
 k=\left\lfloor\frac{n-z}{2h-1}\right\rfloor
 =(1+o(1))\frac n{2h}
\tag{4.4}
\]

disjoint cores \(U_1,\ldots,U_k\), each of size \(2h-1\).  Choose
distinct codes

\[
 C_i\in\binom Z{z/2}.
\tag{4.5}
\]

Put

\[
 d_0=\binom{2h-2}{h-1},\qquad
 t=\left\lfloor\frac B{d_0}\right\rfloor.
\tag{4.6}
\]

For every \(D\in\binom{U_i}h\), create \(t\) copies of the departure
block \(D\).

### Theorem 4.1 (owner-spread dense-core cut)

The resulting \(h\)-uniform departure multihypergraph
\(\mathcal D\) has

\[
 \boxed{\Delta(\mathcal D)=(1-o(1))B,}
\tag{4.7}
\]

\[
 \boxed{\nu(\mathcal D)=k,}
\tag{4.8}
\]

\[
 \boxed{
 \chi'(\mathcal D)
 =\left(2-\frac1h+o(1)\right)B,}
\tag{4.9}
\]

and

\[
 \boxed{
 |E(\mathcal D)|=(1+o(1))\frac Wh.}
\tag{4.10}
\]

Every edge copy can be assigned a distinct middle owner \(X\) containing
its departure block, and every assigned pair \((D,X)\) extends to a
literal return-free length-\(h\) cyclic segment.

#### Proof: degree, matching, and colouring

A coordinate of \(U_i\) belongs to exactly \(d_0\) members of
\(\binom{U_i}h\).  Its degree is therefore \(td_0\le B\).  Since

\[
 \log d_0=O(h)=o(m),\qquad \log B=\Theta(m),
\]

we have \(d_0=o(B)\) and hence \(td_0=(1-o(1))B\), proving (4.7).

Any two \(h\)-subsets of a \((2h-1)\)-set intersect.  Thus a matching
uses at most one edge from each core, while edges from different cores
are disjoint.  This proves (4.8).

The number of copies in one core is

\[
 t\binom{2h-1}h
 =td_0\frac{2h-1}{h}
 =\left(2-\frac1h+o(1)\right)B.
\tag{4.11}
\]

They form a clique in the line graph, so at least this many colours are
necessary.  Conversely, enumerate the copies in every core and give the
\(j\)-th copy in all cores colour \(j\).  Different cores have disjoint
coordinate supports.  This proves (4.9).

Finally, multiply (4.11) by (4.4) and use \(nB=W\).  This gives
(4.10).

#### Proof: distinct assigned owners

For \(D\in\binom{U_i}h\), use the owner pool

\[
 \mathcal X_{i,D}
 =
 \left\{
 X\in\binom{[n]}m:
 X\cap U_i=D,\quad X\cap Z=C_i
 \right\}.
\tag{4.12}
\]

The pools are pairwise disjoint: different cores have different
\(Z\)-codes, and different \(D\)'s in one core prescribe different
intersections with \(U_i\).

Put

\[
 r=m-h-\frac z2.
\]

The coordinates outside \(U_i\cup Z\) number \(2r+2\), so

\[
 |\mathcal X_{i,D}|=\binom{2r+2}r.
\tag{4.13}
\]

Stirling's formula, uniformly under (4.2), gives

\[
 \frac{|\mathcal X_{i,D}|}{t}
 \ge
 \frac{\binom{2r+2}r\,d_0}{B}
 =\Theta\left(\frac{m}{2^z\sqrt h}\right).
\tag{4.14}
\]

Minimality in (4.3), together with the central-binomial estimate, gives

\[
 2^z=O\left(\frac nh\sqrt z\right).
\tag{4.15}
\]

Equations (4.14)--(4.15) imply

\[
 \frac{|\mathcal X_{i,D}|}{t}
 =\Omega\left(\sqrt{\frac hz}\right)\longrightarrow\infty.
\tag{4.16}
\]

Thus every copy of every \(D\) receives a distinct owner
\(X\in\mathcal X_{i,D}\).

#### Proof: literal fragment

For an assigned pair \(D\subset X\), choose any \(h\)-set

\[
 A=\{a_0,\ldots,a_{h-1}\}\subseteq[n]\setminus X
\]

and order \(D=\{d_0,\ldots,d_{h-1}\}\).  Put

\[
 X_j=
 \left(X\setminus\{d_0,\ldots,d_{j-1}\}\right)
 \cup\{a_0,\ldots,a_{j-1}\}.
\tag{4.17}
\]

The \(X_j\)'s form a return-free Johnson geodesic.  If \(K=X\setminus D\)
and \(R=[n]\setminus(X\cup A)\), the cyclic order

\[
 (d_0,\ldots,d_{h-1},K,
  a_0,\ldots,a_{h-1},R)
\tag{4.18}
\]

has \(X_j\) as its length-\(m\) interval beginning at phase \(j\).
Hence every fragment is literal. \(\square\)

The construction uses \((1+o(1))W/h\) fragments and
\((1+o(1))W\) departure slots.  Almost every coordinate lies in a core
and has departure degree \((1-o(1))B\).  Nevertheless, even perfect
cross-core fusion needs \((2-o(1))B\) packets.

The scope is important.  The theorem gives distinct assigned starting
owners and legal individual fragments.  It does not prove that all
internal owner states of all fragments are mutually distinct, nor that
the family is an actual PBBS orbit.  It therefore refutes the abstract
owner-spread inequality (4.1), not a PBBS-specific theorem retaining its
complete chronology.

## 5. Exact remaining product lemma

Theorems 2.2 and 3.1 isolate the surviving constructive statement.

> **Correlated cross-frame phase resolution — UNPROVED.**  Build a
> multiscale atlas of alternating product sheets and choose one phase
> \(\varepsilon\) in every parent so that:
>
> 1. the even/middle sheets remain an exact or \(o(W)\)-defect partition;
> 2. the complementary odd sheets, across all frames and every controlled
>    rank, have aggregate miss \(o(W)\);
> 3. the same choices admit one common departure/arrival/ordered-slot
>    factorisation into \(B+o(B)\) literal cyclic packets.

Choosing both phases locally is coefficient-fatal by (3.9).  There is no
growing-redundancy argument at a fixed Gaussian depth: the average number
of packet occurrences per target is only

\[
 \frac W{N_q}=\exp(q^2/m+o(1))=O_A(1)
 \qquad(q\le A\sqrt m),
\]

In the idealized model in which the \(d_T\) representations of a target
\(T\) depend on distinct independent fair phase bits, its miss probability
is \(2^{-d_T}\).  Jensen's inequality gives

\[
 \frac1{N_q}\sum_T2^{-d_T}
 \ge
 2^{-\frac1{N_q}\sum_Td_T}
 =2^{-W/N_q}
 =\Omega_A(1).
\]

Thus independent half-sheet sampling leaves a positive-density residue in
that model.  This does not rule out a structured deterministic signing;
it shows why the missing cross-frame cover must use correlation rather
than an unbounded number of independent chances.

The dense-core theorem shows that item 3 cannot be replaced by point
balance plus distinct owner starts.  All matching cuts, or a
PBBS-specific chronological substitute which implies them, are essential.

## 6. Adversarial audit

1. The sharing theorem assigns every covered target only once.  Its
   \(\Theta(HW)\) count is not inflated by repeated target occurrences.
2. The random relabelling is chosen after the assignment.  The global
   assignment is transported with the packets, and any prescribed target
   family loses at most the total \(o(W)\) holes.
3. Same-box pairs are counted over all assigned targets, so restricting to
   a shoulder subfamily can only reduce the error term.
4. The literal endpoint in Theorem 2.2 is the actual occurrence \(E_j\)
   in (1.7), not an abstract product-box portal.
5. In Theorem 3.1, the two start parities are both used inside one retained
   parent order.  This is why one parity class of \(\delta\)'s covers the
   entire even sheet rather than half of it.
6. The owner pools in (4.12) are disjoint because both the core code and
   the exact core intersection are prescribed.  Counting only all
   supersets of \(D\) would not prove an injective assignment.
7. The dense-core obstruction does not claim mutually disjoint internal
   paths.  That unproved strengthening is exactly where actual PBBS
   chronology could still defeat the countermodel.
8. No constant-one conclusion is claimed.  Cross-box seam capacity is
   closed; correlated packet factorisation and odd-sheet coverage remain
   open.
