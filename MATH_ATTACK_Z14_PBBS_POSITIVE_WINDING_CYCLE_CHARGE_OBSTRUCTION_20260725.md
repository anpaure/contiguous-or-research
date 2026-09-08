# Positive-winding PBBS returns: exact shift clustering and a complete-colour cocycle obstruction

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Outcome and exact scope

Put

\[
 N=2m+1,\qquad B_m=\operatorname{Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed.  The accepted quotient gate is

\[
 \overline\nu_H=O_A(B_m/N).
 \tag{0.1}
\]

This report treats only the positive-winding first-dominant branch in
Section 8 of `PBBS_PRIMITIVE_RETURN_RECURSION_AUDIT_20260725.md`.
It proves the following.

1. There is an exact shift criterion for two returns of the same length
   and winding on one \(\tau\)-cycle.  Return starts are zeroes of a paired
   forward/reverse prefix-difference walk.

2. A genuine first-dominant boundary start is never followed immediately
   by another first-dominant start.  Thus the easiest adjacent-start
   clustering cannot be the missing argument; any useful clustering must
   use nontrivial lags.

3. Adding the two deficit ledgers gives exactly the old
   \(O(B_m/\sqrt m)\) estimate.  Raw higher deficit moments are weaker at
   the Gaussian scale.  The only known nonlinear charge that has the
   correct normalization is the two-parity product/correlation charge,
   whose required PBBS-specific bound remains unproved.

4. More decisively, there is an explicit formal block-cocycle system on
   long quotient cycles which satisfies all of the following at once:

   * positive odd block data and both exact Section 8 identities;
   * winding one and complete first-return chronology;
   * the scalar area telescope;
   * coprime quotient-lap voltage, hence the complete-colour condition in
     the physical lift;
   * the known first-moment, second-moment, and centered-variance scales;
   * quotient cycles much longer than \(H\); and
   * distinct aperiodic voltage itineraries, as required by the audited
     voltage-itinerary rigidity theorem; and
   * \(\Theta_A(B_m/\sqrt m)\) pairwise support-disjoint returns of
     residence at most \(H\).

   At every selected start, the four local numbers
   \((a,b,c,\widehat c)\) are individually realized by an explicit genuine
   first-dominant Dyck word.

The formal cycles are **not** asserted to be simultaneous orbits of the
Dyck block rotation.  Therefore this is not a PBBS or wreath
counterexample and does not disprove (0.1).  Its exact logical consequence
is a no-go:

\[
 \boxed{\text{the dual ledgers, their proved moment scales, area,
 complete colour, and local first-dominant fringe feasibility do not
 imply (0.1).}}
 \tag{0.2}
\]

The missing square root must use Dyck information absent from the formal
model: either a sharper exact one-state joint marginal/multiplicity theorem
for first-dominant blocks, or a genuinely multi-time correlation for

\[
 \tau(P1R0S)=S1P0R.
\]

No coefficient-one theorem is claimed.

## 1. The two exact ledgers

Let \(\phi\) be the one-step block map and \(\tau=\phi^2\).  Along one
\(\tau\)-cycle write

\[
 D_j=\tau^jD,
 \quad a_j=\delta(D_j),
 \quad b_j=\delta(\phi D_j),
 \quad c_j=d(D_j),
 \quad \widehat c_j=d(\phi D_j).
 \tag{1.1}
\]

The audited block identities are

\[
 c_j=N-a_j-b_j,
 \qquad
 \widehat c_j=N-b_j-a_{j+1},
 \tag{1.2}
\]

and hence

\[
 a_{j+1}-a_j=c_j-\widehat c_j.
 \tag{1.3}
\]

A return of step-two length \(s\) and winding \(w\) satisfies

\[
 \sum_{j=0}^{s-1}c_j=a_s+wN,
 \qquad
 \sum_{j=0}^{s-1}\widehat c_j=a_0+wN.
 \tag{1.4}
\]

At a first-loss boundary \(w\ge1\), and its positive residence is
\(s+1\).  The full quotient support, including insertion and removal,
has exactly \(s+2\) edges.  Thus the Gaussian cutoff is

\[
 s+1\le H.
 \tag{1.5}
\]

All off-by-one statements below use (1.5).

## 2. Exact shift and cluster identities

Indices in this section are cyclic, but the displayed intervals are
assumed nonwrapping after choosing a lift of the cycle.

### Theorem 2.1 (paired-prefix shift criterion)

Suppose \([t,t+s)\) is a return of winding \(w\):

\[
 \sum_{j=t}^{t+s-1}c_j=a_{t+s}+wN.
 \tag{2.1}
\]

For \(k\ge1\), the translated interval \([t+k,t+k+s)\) is a return of
the same winding \(w\) if and only if

\[
 \boxed{
 \sum_{i=0}^{k-1}c_{t+i}
 =
 \sum_{i=0}^{k-1}\widehat c_{t+s+i}.}
 \tag{2.2}
\]

More generally, if the translated interval has winding \(w'\), then

\[
 \sum_{i=0}^{k-1}c_{t+i}
 -
 \sum_{i=0}^{k-1}\widehat c_{t+s+i}
 =(w-w')N.
 \tag{2.3}
\]

In particular, adjacent same-winding starts obey

\[
 \boxed{c_t=\widehat c_{t+s}.}
 \tag{2.4}
\]

#### Proof

Subtract (2.1) from the return equation at \(t+k\).  The difference of
the two \(c\)-sums is

\[
 \sum_{i=0}^{k-1}(c_{t+s+i}-c_{t+i}).
\]

By (1.3), the endpoint difference is

\[
 a_{t+s+k}-a_{t+s}
 =\sum_{i=0}^{k-1}(c_{t+s+i}-\widehat c_{t+s+i}).
\]

Including the possible winding change \((w'-w)N\), cancelling the common
terminal \(c\)-sum, and rearranging gives (2.3).  Equation (2.2) is the
case \(w'=w\), and (2.4) is \(k=1\). \(\square\)

Thus fixed-\((s,w)\) return starts are controlled exactly by zeroes of
the cross-lag walk

\[
 Z_{t,s}(k)
 =\sum_{i=0}^{k-1}
   \bigl(c_{t+i}-\widehat c_{t+s+i}\bigr).
 \tag{2.5}
\]

This is the natural cycle-clustering statistic furnished by the two
ledgers.  No estimate of its zero set follows from the one-point deficit
moments.

### Lemma 2.2 (ordinary consecutive-run packing)

Fix a cycle, \(s\), and \(w\).  Let \(R\) be a set of starts of such
returns and let \(\kappa(R)\) be the number of cyclic components of \(R\)
under ordinary consecutive-start adjacency.  If \(\alpha(R)\) is the
maximum number of pairwise quotient-support-disjoint returns with starts
in \(R\), then

\[
 \alpha(R)
 \le \kappa(R)+{|R|\over s}.
 \tag{2.6}
\]

With the exact residence support convention one may replace \(s\) in the
denominator by \(s+2\).

#### Proof

A run of \(K\) consecutive starts contains at most
\(1+\lfloor(K-1)/s\rfloor\) disjoint ledger cores, and at most
\(1+\lfloor(K-1)/(s+2)\rfloor\) disjoint full residence supports.  Sum
over the \(\kappa(R)\) runs. \(\square\)

The bound exposes a limitation of the word “clustering”: a single cluster
of length \(L\) still packs \(\Theta(L/s)\) intervals.  To gain the
missing square root one needs both a rarity estimate for eligible starts
and a nontrivial multiplicity/overlap estimate.  A bound only on the
number of clusters is insufficient.

## 3. A genuine first-dominant separation lemma

Call a nonprimitive Dyck word \(D\) first-dominant when its first
primitive component \(V\) is the unique component of maximum height.
At the first-loss boundary write

\[
 D=VC,
 \qquad C\ne\varnothing,
 \qquad \operatorname{ht}(C)<\operatorname{ht}(V)=h.
 \tag{3.1}
\]

### Lemma 3.1 (no adjacent first-dominant phases)

Under (3.1), \(\tau D\) is not first-dominant.

#### Proof

The canonical first-maximum factorization has the form

\[
 D=P1R0C,
 \tag{3.2}
\]

because the first return to height zero after the marked maximum-attaining
up-step is the end of the first primitive component \(V\).  Therefore

\[
 \tau D=C1P0R.
 \tag{3.3}
\]

The first primitive component of \(\tau D\) is the first primitive
component of \(C\), and has height strictly below \(h\).  Later in the
word, the prefix \(1P\) reaches height \(h\).  Hence the first primitive
component of \(\tau D\) is not the unique tallest component. \(\square\)

Consequently, adjacent-start equality (2.4) cannot directly cluster the
first-dominant starts themselves.  A successful cycle argument must use
the full nonzero-lag identity (2.2).  Lemma 3.1 supplies only a constant
factor and is far from (0.1).

## 4. Additive and raw-moment charges cannot gain the square root

Let \(\mathcal J\) be a quotient-edge-disjoint family of positive-winding
intervals, each nonwrapping and edge-simple on a quotient cycle longer
than its full support.  This is the accepted long-cycle sector.  Put

\[
 M_p=\sum_{D\in\mathcal D_m}d(D)^p.
 \tag{4.1}
\]

Because \(\phi\) is a permutation commuting with \(\tau\), the
half-shifted supports \(\phi\mathcal J\) are also pairwise disjoint.
Applying (1.4) on the two parities gives

\[
 2(N+1)|\mathcal J|
 \le
 \sum_{I\in\mathcal J}\sum_{j<s(I)}(c_j+\widehat c_j)
 \le2M_1.
 \tag{4.2}
\]

The proved estimate \(M_1=\Theta(B_m\sqrt m)\) therefore gives only

\[
 |\mathcal J|=O(B_m/\sqrt m).
 \tag{4.3}
\]

For every real \(p\ge1\), Holder's inequality applied separately to the
two ledgers yields the exact bound

\[
 \sum_{I\in\mathcal J}
 { (a_{s(I)}+w_IN)^p+(a_0+w_IN)^p
   \over s(I)^{p-1}}
 \le2M_p.
 \tag{4.4}
\]

At \(s\asymp\sqrt N\), the proved scale
\(M_2=\Theta(B_mN^{3/2})\) gives only \(O(B_m)\).  Centering at the global
mean \(\mu\asymp\sqrt N\) does not give a uniform interval charge, because
the centered ledger is

\[
 N+a_s-\mu s,
 \tag{4.5}
\]

for which the known scale data give no uniform positive lower bound; its
cancellation scale is \(s\asymp N/\mu\asymp\sqrt N\).
The antisymmetric combination of the two ledgers is only the endpoint
telescope \(a_s-a_0\).

The exact nonlinear sufficient charge is obtained by multiplying the two
positive ledgers.  For each interval \(I=(D,s)\),

\[
 N^2
 \le
 \sum_{0\le j,k<s}
 c(\tau^jD)\widehat c(\tau^kD).
 \tag{4.6}
\]

After grouping by \(\ell=k-j\), edge disjointness makes each first root
occur at most once for each fixed lag.  Thus the PBBS-specific estimate

\[
 \sum_{|\ell|<H}
 \sum_{E\in\mathcal A^{\rm fd}_{H,\ell}}
 d(E)d(\phi\tau^\ell E)
 =O_A(NB_m)
 \tag{4.7}
\]

would imply the positive-winding part of (0.1).  Here
\(\mathcal A^{\rm fd}_{H,\ell}\) is the set of roots occurring at lag
\(\ell\) inside an eligible first-dominant positive-winding interval.
This is the universal, family-independent eligible-root set.
Equation (4.7) is **unproved**.  The next construction shows that it cannot
be deduced from the scalar data above.

## 5. A long-cycle, complete-colour formal cocycle at the bad scale

This section constructs an abstract exact block-data system.  Every
displayed identity is proved, but simultaneous Dyck-orbit realizability is
not asserted.

### 5.1 Parameters

Fix \(A>0\).  Let \(s\to\infty\) through

\[
 s\equiv6\pmod {12}.
 \tag{5.1}
\]

Put \(\Lambda_A=\max\{1,16/A^2\}\), and choose an odd integer \(k\),
not congruent to \(2\pmod3\), with

\[
 \Lambda_As\le k\le\Lambda_As+6,
 \tag{5.2}
\]

which is possible because the allowed residue classes are
\(1,3\pmod6\).

and define

\[
 N=k(2s+1),
 \qquad m={N-1\over2},
 \qquad a=k(s-1),
 \qquad c=3k.
 \tag{5.3}
\]

Then \(N=2m+1\), \(k=\Theta_A(s)\), and
\(N=\Theta_A(s^2)\).  Since \(m\ge ks\), (5.2) gives

\[
 A\sqrt m\ge4s,
\]

so in particular \(s+1\le H\) for all sufficiently large \(s\).
Moreover,

\[
 2a+c=N.
 \tag{5.4}
\]

Define

\[
 y={N+2-a\over2},
 \qquad R={N+2+a\over2}.
 \tag{5.5}
\]

Because \(s/2\) is odd, \(y\) is odd and \(R\) is even.  Choose positive
odd integers \(x,z\), differing by at most two, with

\[
 x+z=R.
 \tag{5.6}
\]

Then

\[
 x+y+z=N+2,
 \qquad a+y=x+z.
 \tag{5.7}
\]

For \(\epsilon\in\{0,1\}\), put

\[
 x_\epsilon=x+4\epsilon,
 \qquad z_\epsilon=z-4\epsilon.
 \tag{5.7a}
\]

For large \(s\), these are positive odd integers, and

\[
 x_\epsilon+y+z_\epsilon=N+2,
 \qquad a+y=x_\epsilon+z_\epsilon
 \quad(\epsilon=0,1).
 \tag{5.7b}
\]

For large \(s\), every adjacent sum in

\[
 a,a,\ldots,a,x_\epsilon,y,z_\epsilon,a
 \tag{5.8}
\]

is strictly below \(N\).  Indeed

\[
 2a=N-c<N,
\]

and, using \(x_\epsilon,z_\epsilon\le R/2+5\),

\[
 4(N-a-x_\epsilon)\ge3N-5a-22=k(s+8)-22>0,
 \tag{5.9}
\]

while

\[
 4(N-x_\epsilon-y)\ge N+a-26>0,
 \tag{5.10}
\]

with the same estimates for \(z_\epsilon+a\) and
\(y+z_\epsilon\).

### 5.2 The quotient cycles and exact block identities

Let

\[
 T=2s+4.
 \tag{5.11}
\]

For \(\epsilon\in\{0,1\}\), define the \(\delta\)-template

\[
 \mathcal T_\epsilon=
 \bigl(\underbrace{a,a,\ldots,a}_{2s+1\ \mathrm{terms}},
       x_\epsilon,y,z_\epsilon\bigr).
 \tag{5.12}
\]

Put \(M=N+1\).  Given a cyclic binary word
\(\boldsymbol\epsilon=(\epsilon_0,\ldots,\epsilon_{M-1})\), concatenate
\(\mathcal T_{\epsilon_0},\ldots,\mathcal T_{\epsilon_{M-1}}\) on one
formal \(\phi\)-cycle.  Its length is \(MT\), and each of its two
\(\tau=\phi^2\)
cycles has length

\[
 {MT\over2}=M(s+2)\gg H.
 \tag{5.13}
\]

If \(u_t\) is a state of the formal \(\phi\)-cycle, set

\[
 \delta(u_t)=\delta_t,
 \qquad
 d(u_t)=N-\delta_t-\delta_{t+1}.
 \tag{5.14}
\]

Equations (5.9)--(5.10) make every \(d(u_t)\) positive.  All \(\delta_t\)
are odd, so every \(d(u_t)\) is odd.  If
\(D_j=u_{2j}\), then (5.14) is exactly

\[
 c_j=N-a_j-b_j,
 \qquad
 \widehat c_j=N-b_j-a_{j+1}.
 \tag{5.15}
\]

Thus both Section 8 block identities hold globally, including at every
template boundary.

### 5.3 Area and complete colour

On the even \(\tau\)-cycle, the sum of the area increments
\(a_j-b_j\) over a template of either type is

\[
 (s+1)a+y-(sa+x_\epsilon+z_\epsilon)
 =a+y-x_\epsilon-z_\epsilon=0
 \tag{5.16}
\]

by (5.7b).  The corresponding odd-parity sum is its negative and is also
zero.  Hence an integral potential \(\operatorname{ar}\) exists on both
\(\tau\)-cycles with

\[
 \operatorname{ar}(\tau D)-\operatorname{ar}(D)
 =\delta(D)-\delta(\phi D).
 \tag{5.17}
\]

The scalar area telescope is therefore exact.

Under the audited omitted-label voltage convention, the voltage of one
template is

\[
 (2s+1)a+x_\epsilon+y+z_\epsilon
 =N(s-1)+N+2
 \equiv2\pmod N.
 \tag{5.18}
\]

The complete \(\phi\)-cycle has voltage

\[
 2M=2(N+1)\equiv2\pmod N.
 \tag{5.19}
\]

Since \(N\) is odd, this voltage is coprime to \(N\).  Its physical lift
therefore takes exactly \(N\) quotient laps.  At every fixed quotient
phase the omitted label runs through all \(N\) colours once.  Thus the
formal cycle satisfies the componentwise complete-colour condition.

There are also enough genuinely long, distinct voltage itineraries.  A
cyclic binary word of length \(M\) with a proper period has period at most
\(M/2\), so the number of such ordered words is at most

\[
 M2^{M/2}.
 \tag{5.19a}
\]

For large \(M\), there are consequently at least \(2^{M-1}/M\)
aperiodic binary necklaces.  All three separator entries are strictly
below \(a\) for large \(s\): indeed

\[
 2(a-y)=k(s-4)-2>0,
 \qquad
 4(a-x_\epsilon),4(a-z_\epsilon)
 \ge k(s-4)-22>0.
 \tag{5.19c}
\]

Hence the maximal runs of \(a\)'s identify the template boundaries.  An aperiodic
\(\boldsymbol\epsilon\) therefore gives a \(\delta\)-itinerary of minimal
cyclic period exactly \(MT\), and distinct binary necklaces give distinct
cyclic voltage itineraries.

Finally,

\[
 B_m\le4^m=2^{N-1}=2^{M-2}.
 \tag{5.19b}
\]

Thus there are more than enough distinct aperiodic necklaces to assign
one to every main cycle used below.  The main formal cycles respect the
necessary injectivity conclusion of voltage-itinerary rigidity; their
long periods are not obtained by literally repeating a shorter voltage
word.

### 5.4 First returns and winding

At the beginning of each template, the next \(2s+1\) one-step
displacements are all \(a\).  Now

\[
 \gcd(a,N)
 =k\gcd(s-1,2s+1)
 =k\gcd(s-1,3)
 =k,
 \tag{5.20}
\]

because (5.1) gives \(3\nmid(s-1)\).  Hence the additive order of \(a\)
modulo \(N\) is exactly \(2s+1\).  The omitted label therefore returns
for the first time after these \(2s+1\) steps; all intermediate labels
are distinct.

For the associated step-two return, every displayed block has

\[
 a_j=b_j=a,
 \qquad c_j=\widehat c_j=c
 \qquad(0\le j<s),
 \tag{5.21}
\]

and the terminal \(a_s\) is again \(a\).  From (5.3),

\[
 sc=3ks=N+a.
 \tag{5.22}
\]

Thus both exact ledgers have winding one.  This is a simple first return
of positive residence \(s+1\le H\).

Template starts are separated by \(T/2=s+2\) on the even
\(\tau\)-cycle.  Their full residence supports, each of size \(s+2\),
are therefore pairwise disjoint and in fact tile that parity cycle.
Each formal \(\phi\)-cycle supplies exactly \(M\) selected intervals.

Let \(Q_0=\lfloor B_m/(MT)\rfloor\).  Since \(s\equiv0\pmod3\), one
has \(T\equiv1\pmod3\), while the extra choice in (5.2) gives
\(M=N+1\not\equiv0\pmod3\).  Choose \(h\in\{0,1,2\}\) so that

\[
 Q=Q_0-h,
 \qquad R_0=B_m-QMT\equiv0\pmod3.
 \tag{5.23}
\]

Then \(0\le R_0<3MT=O_A(N^{3/2})\).  Take

distinct aperiodic binary necklaces from Section 5.3, and use their
itineraries on \(Q\) disjoint formal cycles.  These cycles use
\(B_m-O_A(N^{3/2})=(1-o(1))B_m\)
states and supply

\[
 |\mathcal J|=QM
 ={(1-o(1))B_m\over T}
 =\Theta_A(B_m/\sqrt m).
 \tag{5.24}
\]

Compared with \(B_m/N\), (5.24) is larger by
\(\Theta_A(\sqrt m)\).  The remaining \(R_0\) states can be padded without
duplicating a voltage itinerary.  Choose \(R_0/3\) distinct cyclic triples
of positive odd integers \((p,q,r)\) with

\[
 p,q\in[N/4,N/3],
 \qquad r=N+2-p-q.
 \tag{5.24a}
\]

There are \(\Theta(N^2)\) such cyclic triples, more than the required
\(O_A(N^{3/2})\).  Indeed \(r>N/3\ge p,q\), so the unique large entry
fixes the cyclic phase and distinct ordered pairs \((p,q)\) give distinct
cyclic itineraries.  The three deficits are exactly

\[
 r-2,\qquad p-2,\qquad q-2,
 \tag{5.24b}
\]

and hence are positive odd.  Every triple has lap voltage
\(p+q+r\equiv2\pmod N\), and a three-cycle has a closed area telescope
because \(\tau=\phi^2\) is again a three-cycle.  Defining each deficit by
the adjacent law (5.14) gives positive odd block data and a complete-colour
physical lift.  Choosing distinct triple necklaces also respects
voltage-itinerary injectivity.  Their total contribution to every fixed
moment is polynomial and hence negligible compared with the main
exponential mass.  No assertion is made that the padding, or the main
cycles, consists of actual Dyck roots.

### 5.5 Exact moment scales and product-charge saturation

Inside one template, the \(2s\) interior base deficits equal

\[
 N-2a=c=3k=\Theta_A(\sqrt N).
 \tag{5.25}
\]

The four boundary deficits

\[
 N-a-x_\epsilon,\quad N-x_\epsilon-y,\quad
 N-y-z_\epsilon,\quad N-z_\epsilon-a
 \tag{5.26}
\]

are all \(\Theta_A(N)\), by (5.9)--(5.10) and the balanced choice of
\(x,z\).  In fact, summing (5.14) cyclically over either template gives
the exact first moment

\[
 2s(3k)+\sum_{\mathrm{four\ boundary}}d
 =TN-2(Ns+2)=4(N-1).
 \tag{5.26a}
\]

Since there are \(\Theta(B_m/T)=\Theta(B_m/\sqrt N)\)
templates, the formal system has

\[
 \sum d=\Theta_A(B_m\sqrt N),
 \tag{5.27}
\]

\[
 \sum d^2=\Theta_A(B_mN^{3/2}),
 \tag{5.28}
\]

and centered variance

\[
 \sum(d-\overline d)^2=\Theta_A(B_mN^{3/2}).
 \tag{5.29}
\]

Indeed, each template contributes \(\Theta_A(N)\) to the first moment
and \(\Theta_A(N^2)\) to the second; the \(\Theta(N)\) boundary deficits
also give the lower bound in (5.29).  More generally, for every fixed
\(p>1\),

\[
 \sum d^p=\Theta_A(B_mN^{p-1/2}).
 \tag{5.30}
\]

Thus, at the level of asymptotic orders, no finite collection of raw
scalar moments distinguishes this model from the known heavy-tail deficit
mechanism.  No claim is made that the exact PBBS moment constants or full
marginal laws agree.

For every selected interval, the two-parity product charge is exactly

\[
 \left(\sum_{j<s}c_j\right)
 \left(\sum_{j<s}\widehat c_j\right)
 =(N+a)^2.
 \tag{5.31}
\]

Summing (5.31) over (5.24) gives

\[
 \Theta_A(B_mN^{3/2}),
 \tag{5.32}
\]

whereas the sufficient PBBS bound (4.7) is \(O_A(B_mN)\).  The formal
model therefore realizes exactly the missing coherent square-root excess.

## 6. The selected local quadruple is pointwise first-dominant-realizable

The preceding cycles are formal.  Nevertheless their selected local
quadruple is not pointwise excluded by first-dominant fringe geometry.
This section proves existence of one such word, not the required
multiplicity of distinct roots.

### Proposition 6.1 (literal local realization)

Let \(a,c\) be as in (5.3), put

\[
 u={c-1\over2},
 \qquad h=a-c+1=k(s-4)+1,
 \tag{6.1}
\]

and define the Dyck word

\[
 D=
 1^{h-1}(01)^u\,1\,(01)^u0^{h-1}\,0\,(10)^u.
 \tag{6.2}
\]

Then \(D\) is first-dominant with nonempty suffix, and

\[
 \boxed{
 \delta(D)=a,
 \quad \delta(\phi D)=a,
 \quad d(D)=c,
 \quad d(\phi D)=c.}
 \tag{6.3}
\]

#### Proof

Use the canonical factorization

\[
 P^-=1^{h-1},
 \qquad P^+=(01)^u,
 \qquad P=P^-P^+,
 \qquad R=(01)^u0^{h-1},
 \qquad C=(10)^u.
 \tag{6.4}
\]

The path first reaches height \(h-1\) at the end of \(P^-\), remains at
or below that height through \(P^+\), and the marked up-step is its first
step to height \(h\).  During \(R\) it never exceeds \(h\), then reaches
height one at the end of \(R\), and the marked zero returns to zero.
Thus \(P1R0\) is a primitive component of height \(h\).  The suffix
\(C=(10)^u\) has height one, so the first component is uniquely tallest
and \(D\) is first-dominant.

The lengths give

\[
 |P|+1=(h-1)+(c-1)+1=a,
\]

\[
 |R|+1=(c-1)+(h-1)+1=a,
 \qquad |C|+1=c.
\]

They also verify the ambient semilength exactly:

\[
 |D|=2h+6u,
 \qquad {|D|\over2}=h+3u
 =a+{c-1\over2}={2a+c-1\over2}=m.
 \tag{6.5}
\]

Finally, the exact first-dominant fringe identity gives

\[
 d(\phi D)=|P^+|+1=c.
\]

This proves (6.3). \(\square\)

Proposition 6.1 is deliberately local.  It does **not** prove that the
successive formal states in Section 5 can be chosen as the successive
actual rotations of these words.  That simultaneous orbit condition is
exactly what remains.  In fact, direct canonical factorization of this
particular witness gives

\[
 \delta(\tau D)=a,
 \qquad d(\tau D)=1,
 \qquad \delta(\phi\tau D)=N-a-1,
 \tag{6.6}
\]

Indeed, in \(\tau D=C1P0R\), the first maximum occurs after \(C1P^-\),
at position \((c-1)+1+(h-1)=a\), and the first subsequent return to zero
is the end of the word, so its terminal suffix is empty.  The last value
in (6.6) then follows from the block identity.  Thus this word leaves the homogeneous \(a\)-template after three one-step
voltages.  Proposition 6.1 is not being silently iterated.

## 7. Decisive no-go and the remaining theorem

The construction in Section 5 survives all scalar or one-time repairs of
the Section 8 argument:

* pairing the forward and reverse ledgers;
* every fixed raw deficit moment at the corresponding heavy-tail order
  of magnitude (not its exact PBBS constant or marginal law);
* the centered second moment;
* the area increment and its cycle telescope;
* complete first-return chronology and simple-return parity;
* the full \(s+2\)-edge support convention;
* long main quotient cycles carrying every selected return;
* coprime lap voltage and complete colour in the physical lift; and
* local literal first-dominant fringe realizability.

It also arranges the formally eligible starts at the maximally dangerous
spacing:
one start per \(s+2\) quotient edges.  Thus the scalar data neither force
return rarity beyond \(B_m/\sqrt m\) nor force additional overlap among
those surviving starts.

Accordingly, no cycle-clustering or higher-order-charge proof based only
on these scale data can gain the missing \(\sqrt m\).  A valid positive
theorem must add either an exact first-dominant marginal/multiplicity bound
that excludes the formal selected tuples at the required scale, or
simultaneous word-level orbit information.  One exact sufficient form of
the second route is the unproved correlation estimate (4.7).  A sufficient direct
cycle-language target is the quantitative bound

\[
 \#\{\text{support-separated genuine first-dominant positive-winding
 starts of residence at most }H\}=O_A(B_m/N).
 \tag{7.1a}
\]

Merely excluding saturation at \(\Theta(B_m/\sqrt m)\) is necessary but
not equivalent to (7.1a).

The precise proved/conditional boundary is therefore

\[
 \boxed{
 \begin{array}{l}
 \textbf{Proved: }\text{exact shift criterion, first-dominant
 nonadjacency, and the complete-colour}\cr
 \text{long-cycle scalar-cocycle obstruction at }
 \Theta_A(B_m/\sqrt m).\cr
 \textbf{Unproved: }\text{a sharp first-dominant marginal bound, the
 multi-time estimate (4.7),}\cr
 \text{or any equivalent PBBS theorem excluding the formal templates.}
 \end{array}}
 \tag{7.1}
\]

## 8. Internal audit of the decisive construction

The following checks are independent of the heuristic interpretation.

1. **Parity.**  Condition \(s\equiv6\pmod {12}\) makes
   \(a,c,x_\epsilon,y,z_\epsilon,N\) odd; hence every deficit in
   (5.14) is odd.

2. **Window.**  The relevant residence is \(s+1\), not \(s\), and the
   support is \(s+2\).  The margin in (5.2) proves \(s+1\le H\).

3. **First return.**  Equation (5.20), not merely the terminal ledger,
   proves that none of the first \(2s\) physical phases repeats the label.

4. **Area.**  The separator equations in (5.7b) make the even- and
   odd-parity area sums vanish separately; no illicit cross-parity
   cancellation is used.

5. **Complete colour.**  Using \(M=N+1\) templates gives
   lap voltage \(2\), not zero.  Since \(N\) is odd, the physical lift
   visits every colour.  The two separator variants have the same voltage.

6. **Voltage rigidity.**  Distinct aperiodic binary necklaces give
   distinct itineraries of minimal period \(MT\); the main cycles neither
   repeat a shorter itinerary nor duplicate one another.  The polynomial
   padding uses distinct length-three itineraries.

7. **Long cycles.**  Each main \(\tau\)-cycle carrying selected returns
   has length \(M(s+2)\), so the bad packing is not hidden in the
   discarded short-cycle sector.  Only the negligible padding cycles have
   length three.

8. **Moments.**  The four separator-boundary deficits are globally
   compatible through (5.14); they are not isolated high-deficit states
   pasted into an incompatible neighbouring cocycle.

9. **Scope.**  No step constructs a literal PBBS orbit.  Proposition 6.1
   verifies only the local first-dominant quadruple.  Therefore (0.2),
   rather than a counterexample to (0.1), is the strongest valid
   conclusion.
