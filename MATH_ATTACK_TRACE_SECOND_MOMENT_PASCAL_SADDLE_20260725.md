# PBBS Pascal-saddle passages: the exact trace second moment and a sharp tensorization obstruction

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, solver, or
web search is used.

## 0. Outcome

Put

\[
 N=2r+1,\qquad B_r=\operatorname{Cat}_r,
 \qquad H=\lceil A\sqrt r\rceil,
 \qquad G=2H-1,
\]

where \(A>0\) is fixed.  Let a first peak-deletion core have rank \(d\)
and \(k\) peaks, and put

\[
 p=2d+1,\qquad y=r-d-k,\qquad M=y+2d=r+d-k.
\]

The complete inverse fibre has size

\[
 F_r(d,k)=\binom M{2d}.
\]

For a normalized core \(E\), let \(\kappa_t(E)\in\mathbb Z_p\) be its
selected-particle itinerary, with \(\kappa_0=0\), and define the local time
of the immediate predecessor in the Gaussian window by

\[
 V_G(E)=\#\{1\le t\le G:\kappa_t(E)=-1\}.
\]

The exact peak-spacing theorem implies the following identity.  If
\(W_G(E)\) is the number of inverse roots above \(E\) whose returned
physical label reappears by time \(G\), then, with

\[
 s_E=\min\left\{y,\left\lfloor{V_G(E)\over2}\right\rfloor-1\right\},
\]

\[
 \boxed{
 W_G(E)=
 \begin{cases}
 0,&V_G(E)<2,\\[2mm]
 \displaystyle F_r(d,k)-\binom{M-s_E-1}{2d},&V_G(E)\ge2.
 \end{cases}}
 \tag{0.1}
\]

In the full Pascal saddle tube

\[
 |d-r/2|+|k-r/6|\le2\sqrt{r\log r},
 \tag{0.2}
\]

one consequently has, uniformly for all cores,

\[
 \boxed{
 \left({3\over4}-o(1)\right)F_r(d,k)\mathbf1_{\{V_G\ge2\}}
 \le W_G(E)
 \le F_r(d,k)\mathbf1_{\{V_G\ge2\}}
 \le F_r(d,k)\binom{V_G(E)}2.}
 \tag{0.3}
\]

Thus the Pascal weight does not blur the chronology: up to absolute
constants, a dangerous saddle core is exactly a core for which the
predecessor is selected twice in the window.

Expanding the last term in (0.3) produces a genuine three-point trace
energy.  If

\[
 \mathsf N(d,k)={1\over d}\binom dk\binom d{k-1}
\]

and

\[
 T_{u,v}(d,k)=
 \#\{E\in\mathcal D_d:\operatorname{pk}(E)=k,
                  \ \kappa_u(E)=\kappa_v(E)=-1\},
 \tag{0.4}
\]

then

\[
 \boxed{
 \sum_{\substack{E\in\mathcal D_d\\\operatorname{pk}(E)=k}}
       \binom{V_G(E)}2
 =\sum_{1\le u<v\le G}T_{u,v}(d,k).}
 \tag{0.5}
\]

The uniform-label contribution to the right side is exactly

\[
 {\binom G2\over p^2}\mathsf N(d,k).
\]

After multiplication by the exact inverse-fibre weight and summation over
(0.2), this baseline is

\[
 \boxed{
 \sum_{(d,k)\text{ in }(0.2)}
 F_r(d,k){\binom G2\over p^2}\mathsf N(d,k)
 \le (2A^2+o_A(1)){B_r\over r}.}
 \tag{0.6}
\]

Hence an \(O_A(B_r/r)\) bound for the nonuniform three-point excess proves
the desired new, linear-seam quotient estimate

\[
 \overline\nu_H=O_A(B_r/r).
\]

This is a precise positive reduction, but the excess bound is not a
consequence of the audited one-point trace facts.  Two sharp obstructions
are proved below.

1. A marginal fan factor \(1/H\) and an interval edge factor \(1/H\) do
   not tensorize.  An exact fibre-over-cycle incidence model has row density
   \(1/H\), interval length \(H\), and an edge-disjoint packing of size
   \(LF/H\), not \(LF/H^2\).

2. There is an explicit balanced long-cycle itinerary with one legitimate
   \(z=0\) predecessor passage per \(\Theta(H)\) quotient phases.  After
   exact Pascal lifting it has packing \(\Theta(\mathsf M_r(d,k)/H)\) in
   every abstract saddle cell while satisfying particle homomesy and all
   one-level fibre capacities.

The second construction is deliberately an abstract trace model, not a
Dyck/PBBS realization.  Its role is exact: homomesy, the predecessor
criterion, long period, and the Pascal capacities cannot prove (0.6)'s
excess bound.  The surviving statement is a PBBS-specific three-point
trace anticorrelation theorem.  No claim of \(RP_A\) or coefficient one is
made here.

## 1. Exact Pascal mass as a local-time threshold

For a fixed core \(E\), the terminal root-slot occupancy \(z\) has exact
fibre size

\[
 K_z(d,k)=\binom{M-z-1}{2d-1},\qquad 0\le z\le y.
 \tag{1.1}
\]

The peak-spacing theorem says that this lift returns by time \(G\) if and
only if the \((2z+2)\)-nd occurrence of the predecessor is at most \(G\).
Equivalently,

\[
 V_G(E)\ge2z+2.
 \tag{1.2}
\]

Therefore

\[
 W_G(E)=
 \sum_{z=0}^{y}K_z(d,k)
       \mathbf1_{\{V_G(E)\ge2z+2\}}.
 \tag{1.3}
\]

If \(V_G(E)<2\), this sum is empty.  Otherwise its last allowed index is
\(s_E\), and the hockey-stick identity gives

\[
 \begin{aligned}
 \sum_{z=0}^{s_E}\binom{M-z-1}{2d-1}
 &=\binom M{2d}-\binom{M-s_E-1}{2d}.
 \end{aligned}
\]

This proves (0.1).

The first allowed occupancy already has mass

\[
 {K_0(d,k)\over F_r(d,k)}
 ={\binom{M-1}{2d-1}\over\binom M{2d}}
 ={2d\over M}.
 \tag{1.4}
\]

Uniformly in (0.2),

\[
 {2d\over M}
 ={2d\over r+d-k}
 ={3\over4}+O\!\left(\sqrt{\log r\over r}\right).
 \tag{1.5}
\]

Thus \(W_G(E)\ge K_0(d,k)\) whenever \(V_G(E)\ge2\), while trivially
\(W_G(E)\le F_r(d,k)\).  Finally

\[
 \mathbf1_{\{V_G\ge2\}}\le\binom{V_G}2.
\]

Equations (1.4)--(1.5) prove (0.3), with every floor retained.

There is also an exact thresholded second moment

\[
 \mathcal C_G(d,k)
 =\sum_{\substack{E\in\mathcal D_d\\\operatorname{pk}(E)=k}}
  \min\left\{1,\binom{V_G(E)}2\right\}
 =\#\{E:V_G(E)\ge2\}.
 \tag{1.6}
\]

Equations (0.3) and (1.6) show that direct saddle start mass is comparable
to \(F_r(d,k)\mathcal C_G(d,k)\).  The uncapped factorial moment in (0.5)
is a sufficient, but potentially stronger, energy because a single bursty
core can contribute \(\Theta(G^2)\).

## 2. The exact Fourier excess and its coefficient

Equation (0.5) is immediate from

\[
 \binom{V_G(E)}2
 =\sum_{1\le u<v\le G}
   \mathbf1_{\{\kappa_u(E)=-1\}}
   \mathbf1_{\{\kappa_v(E)=-1\}}.
\]

Let \(\zeta=e^{2\pi i/p}\).  Character orthogonality gives

\[
 \mathbf1_{\{x=-1\}}
 ={1\over p}\sum_{a=0}^{p-1}\zeta^{a(x+1)}.
\]

Consequently

\[
 T_{u,v}(d,k)
 ={\mathsf N(d,k)\over p^2}
 +{1\over p^2}
  \sum_{\substack{a,b\in\mathbb Z_p\\(a,b)\ne(0,0)}}
  \sum_{\substack{E\in\mathcal D_d\\\operatorname{pk}(E)=k}}
  \zeta^{a(\kappa_u(E)+1)+b(\kappa_v(E)+1)}.
 \tag{2.1}
\]

Define the real three-point excess by

\[
 \begin{aligned}
 \mathfrak X_G(d,k)
 ={1\over p^2}
 \sum_{1\le u<v\le G}
  \sum_{\substack{a,b\in\mathbb Z_p\\(a,b)\ne(0,0)}}
  \sum_{\substack{E\in\mathcal D_d\\\operatorname{pk}(E)=k}}
  \zeta^{a(\kappa_u(E)+1)+b(\kappa_v(E)+1)}.
 \end{aligned}
 \tag{2.2}
\]

The expression is real because it equals a difference of the two real
quantities in

\[
 \boxed{
 \sum_E\binom{V_G(E)}2
 ={\binom G2\over p^2}\mathsf N(d,k)
  +\mathfrak X_G(d,k).}
 \tag{2.3}
\]

There is an equivalent positive-semidefinite Gram decomposition which
separates one-point bias from coherent two-time energy.  On the finite set
of peak-\(k\) cores, with counting inner product, put

\[
 f_t(E)=\mathbf1_{\{\kappa_t(E)=-1\}},
 \qquad h_t=f_t-{1\over p}\mathbf1,
 \qquad \mu_t=\langle h_t,\mathbf1\rangle.
 \tag{2.3a}
\]

Then

\[
 T_{u,v}={\mathsf N(d,k)\over p^2}
 +{\mu_u+\mu_v\over p}+\langle h_u,h_v\rangle,
\]

and hence

\[
 \boxed{
 \mathfrak X_G(d,k)
 ={G-1\over p}\sum_{t=1}^G\mu_t
 +{1\over2}\left\|\sum_{t=1}^Gh_t\right\|_2^2
 -{1\over2}\sum_{t=1}^G\|h_t\|_2^2.}
 \tag{2.3b}
\]

Thus even exact one-time uniformity \(\mu_t=0\) would leave the coherent
Gram term.  The missing estimate is precisely a bound on the alignment of
the centered predecessor indicators across the first \(G\) times, within
each fixed peak cell.  Componentwise homomesy controls full-cycle row and
column sums, but it does not bound the norm in (2.3b).

The complete outer mass of the cell is

\[
 \mathsf M_r(d,k)=F_r(d,k)\mathsf N(d,k).
 \tag{2.4}
\]

In (0.2), \(p=r+O(\sqrt{r\log r})\), whereas
\(G=2A\sqrt r+O_A(1)\).  Hence

\[
 {\binom G2\over p^2}
 \le {2A^2+o_A(1)\over r}.
 \tag{2.5}
\]

Summing (2.5) against (2.4), and using that the Pascal cells partition the
outer Catalan roots, proves (0.6).

### Theorem 2.1 (three-point trace criterion for the linear-seam target)

For every quotient-edge-disjoint family whose starts lie in (0.2), one has
the unconditional energy inequality

\[
 \boxed{
 |\mathcal P|
 \le {2A^2+o_A(1)\over r}B_r
 +\sum_{(d,k)\text{ in }(0.2)}
   F_r(d,k)\,\mathfrak X_G(d,k).}
 \tag{2.5a}
\]

Suppose

\[
 \boxed{
 \sum_{(d,k)\text{ in }(0.2)}
 F_r(d,k)\,\mathfrak X_G(d,k)
 =O_A(B_r/r).}
 \tag{2.6}
\]

Then the number of outer quotient roots in the tube which start a return of
gap at most \(G\) is \(O_A(B_r/r)\).  Consequently, after the audited
moderate-deviation deletion outside (0.2),

\[
 \boxed{\overline\nu_H=O_A(B_r/r).}
 \tag{2.7}
\]

#### Proof

Sum the upper bound in (0.3) over the cores in each cell, then sum over the
tube.  Equations (2.3), (0.6), and (2.6) bound the resulting number of
return starts by \(O_A(B_r/r)\).  A quotient-edge-disjoint family cannot
contain more intervals than there are starts.  The audited saddle-tail
estimate removes all cells outside (0.2) with \(o(B_r/N)=o(B_r/r)\) total
mass.  This proves (2.7).  \(\square\)

A stronger but sign-free sufficient hypothesis replaces the left side of
(2.6) by the sum of the absolute values of the nontrivial character sums
in (2.2).  The coefficient in (2.5) shows that no extra power of \(r\) is
hidden: the independent/uniform trace baseline is exactly the desired
scale.

### Theorem 2.2 (bounded killed-trace energy)

The factorial energy in Theorem 2.1 is not necessary: it can overcharge a
single core by order \(G^2\).  There is an exact bounded replacement.  For
\(0<\theta<1\) and an integer \(v\ge0\), put

\[
 \psi_\theta(v)
 =1-(1-\theta)^v-v\theta(1-\theta)^{v-1},
 \tag{2.8}
\]

where the last term is understood as zero when \(v=0\).  Then

\[
 \boxed{
 \theta^2\mathbf1_{\{v\ge2\}}
 \le \psi_\theta(v)
 \le \min\left\{\mathbf1_{\{v\ge2\}},
                 \theta^2\binom v2\right\}.}
 \tag{2.9}
\]

For the fixed choice \(\theta=1/2\), define

\[
 \mathcal S_G(d,k)
 =\sum_{\substack{E\in\mathcal D_d\\\operatorname{pk}(E)=k}}
   \psi_{1/2}(V_G(E)),
 \tag{2.10}
\]

and let

\[
 \beta_{p,G}
 =1-\left(1-{1\over2p}\right)^G
   -{G\over2p}\left(1-{1\over2p}\right)^{G-1}.
 \tag{2.11}
\]

Write the killed-trace excess as

\[
 \mathfrak S_G(d,k)
 =\mathcal S_G(d,k)-\beta_{p,G}\mathsf N(d,k).
 \tag{2.12}
\]

Then every quotient-edge-disjoint family whose starts lie in the saddle
tube satisfies

\[
 \boxed{
 |\mathcal P|
 \le (2A^2+o_A(1)){B_r\over r}
 +4\sum_{(d,k)\text{ in }(0.2)}
 F_r(d,k)\mathfrak S_G(d,k).}
 \tag{2.13}
\]

Consequently

\[
 \sum_{(d,k)\text{ in }(0.2)}
 F_r(d,k)\mathfrak S_G(d,k)=O_A(B_r/r)
 \tag{2.14}
\]

is a sufficient condition for \(\overline\nu_H=O_A(B_r/r)\).  It is no
stronger than the factorial-excess criterion (2.6), up to an
\(O_A(B_r/r^{3/2})\) baseline error.

#### Proof

The quantity \(\psi_\theta(v)\) is the probability that independent
\(\theta\)-thinning of \(v\) marked times retains at least two.  It
vanishes at \(v=0,1\), equals \(\theta^2\) at \(v=2\), and

\[
 \psi_\theta(v+1)-\psi_\theta(v)
 =v\theta^2(1-\theta)^{v-1}\ge0.
\]

This proves the lower bound in (2.9).  The union bound over the
\(\binom v2\) retained pairs proves the upper bound.

By (0.3) and (2.9) with \(\theta=1/2\),

\[
 |\mathcal P|
 \le4\sum_{(d,k)\text{ in }(0.2)}F_r(d,k)\mathcal S_G(d,k).
 \tag{2.15}
\]

Under independent uniform labels, thinning changes the hit probability
from \(1/p\) to \(1/(2p)\); hence (2.11) is exactly the probability of at
least two retained hits in \(G\) trials.  Since \(G/p=o_A(1)\),

\[
 4\beta_{p,G}
 ={\binom G2\over p^2}+O_A(G^3/p^3)
 ={2A^2+o_A(1)\over r}
 \tag{2.16}
\]

uniformly in (0.2).  Summing the error against the cell masses gives
\(O_A(B_r/r^{3/2})\).  Substitution of (2.12) into (2.15) proves
(2.13)--(2.14).

Finally, the upper bound in (2.9) gives

\[
 4\mathcal S_G(d,k)
 \le\sum_E\binom{V_G(E)}2.
\]

Subtracting the two independent baselines gives the exact one-sided
comparison

\[
 4\mathfrak S_G(d,k)
 \le \mathfrak X_G(d,k)
 +\left({\binom G2\over p^2}-4\beta_{p,G}\right)
   \mathsf N(d,k),                                  \tag{2.16a}
\]

where the parenthesized difference is nonnegative and
\(O_A(G^3/p^3)\).  After multiplication by \(F_r(d,k)\) and summation,
its contribution is \(O_A(B_r/r^{3/2})\).  There is no hidden lower-tail
condition: since \(\mathcal S_G\ge0\),

\[
 \sum_{(d,k)}F_r(d,k)\mathfrak S_G(d,k)
 \ge-\sum_{(d,k)}F_r(d,k)\beta_{p,G}\mathsf N(d,k)
 =-O_A(B_r/r).                                     \tag{2.16b}
\]

Thus the usual two-sided big-oh hypothesis (2.6) implies (2.14).  This
proves the last assertion.  \(\square\)

There is an exact chronology expansion behind (2.8).  With
\(f_t(E)=\mathbf1_{\{\kappa_t(E)=-1\}}\),

\[
 \psi_\theta(V_G)
 =1-\prod_{t=1}^G(1-\theta f_t)
  -\sum_{u=1}^G\theta f_u
       \prod_{\substack{1\le t\le G\\t\ne u}}(1-\theta f_t).
 \tag{2.17}
\]

Equivalently,

\[
 \psi_\theta(V_G)
 =\sum_{j=2}^G(-1)^j(j-1)\theta^j
   \sum_{1\le t_1<\cdots<t_j\le G}
   f_{t_1}\cdots f_{t_j}.
 \tag{2.18}
\]

Thus (2.14) is a bounded, signed, all-order first-passage trace estimate.
It keeps the exact chronology and cannot be inflated by a bursty core.

The big-oh scale is sharp for any argument which bounds all starts.  The
independently audited overlap-one construction in
MATH_ATTACK_K_ZERO_WINDING_TRACE_COMPLETION_OBSTRUCTION_20260725.md
gives absolute \(0<a<b\), \(c>0\), and infinitely many \(r\) for which
at least

\[
 c\,{B_r\over N}
 \tag{2.19}
\]

actual zero-winding starts have duration in
\([a\sqrt r,b\sqrt r]\).  Fix \(A>b+1\).  The saddle complement has
\(o(B_r/N)\) total mass, so (2.19) remains of order \(B_r/r\) inside
(0.2).  Equations (0.3) and (2.9) give explicitly

\[
 \sum_{(d,k)\text{ in }(0.2)}F_r(d,k)\mathcal S_G(d,k)
 \ge {1\over4}\sum_{(d,k)\text{ in }(0.2)}
       F_r(d,k)
       \sum_{\substack{E\in\mathcal D_d\\\operatorname{pk}(E)=k}}
       \mathbf1_{\{V_G(E)\ge2\}}
 \ge {1\over4}\sum_EW_G(E)
 =\Omega(B_r/r).
\]

Thus neither the all-start count nor this bounded
energy admits a universal little-oh improvement.  This does not give a
packing lower bound: those actual intervals may still cluster on their
quotient cycles.

## 3. Why the two known \(1/H\) factors do not tensorize

The next lemma is an exact capacitated interval model.  It shows that a
one-phase fan-capacity factor and an interval-length factor combine by a
minimum, not a product, unless cross-phase incidence is controlled.

### Lemma 3.1 (residue-class saturation)

Let \(H\mid L\) and \(H\mid F\).  Consider the product edge set

\[
 \mathbb Z_L\times[F],
\]

where the second coordinate is transported identically around the base
cycle.  Partition the \(F\) fibre labels into equal classes
\(C_0,\ldots,C_{H-1}\), each of size \(F/H\).  Declare a start
\((i,v)\) eligible exactly when

\[
 v\in C_{i\bmod H}.
 \tag{3.1}
\]

Attach to it the length-\(H\) interval

\[
 [i,i+H)\times\{v\}.
\]

Then:

1. every base phase has exactly \(F/H\) eligible fibre starts;
2. for each fibre label, its eligible intervals are pairwise edge-disjoint;
3. all eligible intervals, over all phases and fibres, are pairwise
   edge-disjoint; and
4. their total number is

   \[
    \boxed{LF/H.}
    \tag{3.2}
   \]

#### Proof

The first assertion is the definition.  A fixed label \(v\in C_a\) is
eligible exactly at the phases congruent to \(a\pmod H\).  The corresponding
half-open length-\(H\) intervals partition the base cycle.  Hence they are
edge-disjoint.  Intervals carrying different fibre labels lie on disjoint
product edges.  There are \(L/H\) intervals for each of the \(F\) labels,
which proves (3.2).  \(\square\)

The total product edge budget is \(LF\), so (3.2) also saturates the
universal length bound.  Yet the eligible fraction at each phase is
\(1/H\).  Multiplying this marginal fraction by the length factor would
predict \(LF/H^2\), wrong by the full factor \(H\).

The harmonic Pascal fan has pointwise profile factor

\[
 Q_H\sim e/H.
\]

Lemma 3.1 fits underneath that allowance: add unused eligible vectors if a
row of size \(eF/H\) is desired.  Thus the proved fan-capacity upper bound
and the proved interval edge budget, by themselves, cannot yield their
product.

The obstruction is exactly a cross-phase second moment.  If
\(x_{i,v}\) is the eligibility indicator in Lemma 3.1, then

\[
 \sum_{i,v}x_{i,v}={LF\over H},
 \qquad
 \boxed{
 \sum_{i,v}x_{i,v}x_{i+H,v}={LF\over H}.}
 \tag{3.3}
\]

The second quantity would be \(LF/H^2\) at independent density \(1/H\).
Hence precisely the missing factor is the exclusion of residue-class
trace concentration such as (3.3).

This is a logical no-go for marginal tensorization, not a PBBS
counterexample.  Actual fan eligibility comes from dynamically transported
zero slots; a successful proof may still show that those slots cannot form
the residue pattern (3.1).

## 4. Homomesy and one-level chronology also permit the bad scale

We now give a second abstract model which retains the exact predecessor
chronology, rather than only the two marginal capacities.

Fix odd \(G\ge7\), put \(q_0=2(G+1)\), and choose integers
\(R\ge1\) and \(Q=Rq_0\).  In the Gaussian application take

\[
 R=\left\lceil{r\over q_0}\right\rceil,
 \qquad r\le Q<r+q_0,
 \tag{4.0}
\]

and \(p=2d+1=r+O(\sqrt{r\log r})\).  For
\(0\le m<R\), write \(b_m=mq_0\).  Choose offsets
\(c_0,\ldots,c_{Q-1}\in\mathbb Z_p\) satisfying

\[
 c_{b_m}=c_{b_m+5}=0,
 \qquad c_{b_m+2}=c_{b_m+G}=-1,
 \tag{4.1}
\]

and

\[
 c_{b_m+t}\notin\{0,-1\}
 \quad(1\le t<G,\ t\notin\{2,5\}),
 \qquad 0\le m<R.
 \tag{4.2}
\]

Choose the still unspecified values so that there are no
\(1\le s<Q\) and \(a\in\mathbb Z_p\) for which

\[
 c_{(t+s)\bmod Q}
 +\left\lfloor{t+s\over Q}\right\rfloor
 \equiv c_t+a\pmod p
 \quad(0\le t<Q).
 \tag{4.2a}
\]

Such choices exist for all sufficiently large \(r\) in (4.0).  Indeed,
the number of choices satisfying (4.1)--(4.2) is

\[
 (p-2)^{(G-3)R}p^{Q-(G+1)R}
 \ge c_Ap^{Q-4R},
 \tag{4.2b}
\]

because \((G-3)R/p=O_A(1)\).  For fixed \((s,a)\), the equations excluded
in (4.2a) determine all coordinates from at most
\(\gcd(s,Q)\le Q/2\) initial coordinates, so at most \(p^{Q/2}\) offset
words are bad for that pair.  The total number of bad words is at most
\(Qp^{Q/2+1}\).  Since

\[
 Q-4R-(Q/2+1)=R(G-3)-1\longrightarrow\infty,
\]

the lower bound in (4.2b) eventually exceeds the bad count.  This proves
the assertion.  Define a cyclic label word of length \(pQ\) by

\[
 \boxed{
 \kappa_{Qj+t}=j+c_t\pmod p,
 \qquad j\in\mathbb Z_p,\quad0\le t<Q.}
 \tag{4.3}
\]

### Lemma 4.1 (balanced long-cycle passage word)

The word (4.3) has the following properties.

1. Every label occurs exactly \(Q\) times.
2. At each special origin \(Qj+b_m\), the root label \(j\) first reappears at
   time five.
3. Its immediate predecessor \(j-1\) occurs exactly once before time
   \(G\), at time two, and occurs next at time \(G\).
4. After quotienting global label rotation and passing to step two, the
   displayed pattern has a cycle of length \(Q/2=\Theta(r)\).  It has
   \(R\) special origins, separated by \(G+1\) step-two phases, and every
   return trace has \((G+3)/2\) edges.  Hence those traces are nonwrapping
   and pairwise disjoint.

#### Proof

For every fixed offset \(t\), the map \(j\mapsto j+c_t\) is a bijection of
\(\mathbb Z_p\).  Thus each label occurs once at each of the \(Q\)
offsets, proving the first assertion.  Assertions two and three are exactly
(4.1)--(4.2).

Shifting by \(Q\) positions adds one to every label.  It is therefore one
global label rotation.  A smaller normalized time period would give
exactly the equations forbidden in (4.2a).  Hence the normalized one-step
period is \(Q\).  Since \(Q\) is even, the normalized step-two period is
\(Q/2\).  Every \(b_m=mq_0\) is even, and consecutive special origins are
\(q_0/2=G+1\) step-two phases apart.  The return gap is \(G\), so its
quotient trace has \((G+3)/2\) edges.  For \(G\ge7\),

\[
 {G+3\over2}<G+1.
\]

Thus the trace is nonwrapping.  \(\square\)

At every special origin, the exact predecessor criterion has

\[
 h=5<G,\qquad n_{-1}(G)=1,\qquad z=0.
 \tag{4.4}
\]

Thus (4.3) satisfies the complete one-level chronology used by the Pascal
kernel.  Its balance also implies all componentwise lag-matrix identities:
for every lag, the corresponding matrix has equal row and column sums, and
the sum over lags has the correct square total.

Now place this abstract itinerary on cycles in one saddle cell.  Let
\(\mathsf N=\mathsf N(d,k)\), discard fewer than \(Q\) roots if needed,
and partition the rest into normalized one-step cycles of length \(Q\).
Each such cycle splits into two step-two cycles of length \(Q/2\), and all
\(R\) special phases lie on one of them.  Above every special phase take all

\[
 K_0(d,k)=\binom{M-1}{2d-1}
\]

terminal-zero fibre vectors.  Transport is bijective, so distinct vectors
remain distinct at every projected edge.  For one fixed vector, consecutive
special starts are \(G+1\) quotient phases apart, whereas a trace has only
\((G+3)/2\) edges.  Thus its \(R\) intervals are pairwise edge-disjoint.
Different vectors use different lifted edges.  Hence all chosen intervals
are pairwise edge-disjoint and every reduced-edge load is at most
\(F_r(d,k)\).

In this abstract system choose the fibre-transport bijections between
successive special phases so that the terminal-zero subfibre maps to itself.
This is consistent with the audited one-level axiom, which requires
bijective transport and the pointwise load ceiling.  It is not asserted
that genuine PBBS slot transport has this extra periodicity; excluding it
is part of the missing cross-phase theorem.

The resulting abstract packing has size

\[
 \begin{aligned}
 \left\lfloor{\mathsf N\over Q}\right\rfloor R K_0(d,k)
 &=\left({3\over4}+o(1)\right)
   {\mathsf M_r(d,k)\over2(G+1)}
   -O_A(F_r(d,k)\sqrt r)\\
 &=\Theta_A\!\left({\mathsf M_r(d,k)\over\sqrt r}\right)
 \end{aligned}
 \tag{4.5}
\]

whenever the cell contains many cycles.  Equivalently, its dangerous-core
density is \(1/[2(G+1)]=\Theta_A(r^{-1/2})\), whereas the random three-point
baseline in (2.5) is \(\Theta_A(r^{-1})\).

At every special core \(V_G=2\), so
\(\binom{V_G}{2}=1\).  The excess in this model is therefore not caused by
rare high-local-time bursts: it survives unchanged in the capped energy
\(\mathcal C_G\) from (1.6).

In every cell in (0.2), Stirling's formula gives

\[
 \log\mathsf N(d,k)
 =2d\,h(k/d)+O(\sqrt{r\log r})
 =r\,h(1/3)+O(\sqrt{r\log r}),
 \tag{4.6}
\]

where \(h(x)=-x\log x-(1-x)\log(1-x)>0\).  Thus
\(\mathsf N/Q\to\infty\) exponentially, and the
\(O_A(F_r(d,k)\sqrt r)\) rounding
term in (4.5) is indeed
\(o_A(\mathsf M_r(d,k)/\sqrt r)\).

Moreover (4.2b) supplies

\[
 \log\bigl(\#\{\text{admissible offset words}\}\bigr)
 \ge (Q-4R)\log p+O_A(1)
 =\Theta(r\log r),
 \tag{4.7}
\]

whereas (4.6) is only \(\Theta(r)\).  Thus every abstract cycle may be
given a different selected-label itinerary.  Numerically this does not
conflict with the audited voltage-itinerary ceiling: at period
\(Q=\Theta(r)\), that ceiling permits
\(Qp^Q=\exp(\Theta(r\log r))\) quotient states, far more than the
\(\exp(\Theta(r))\) saddle cores used here.  This remains a consistency
check, not a claim that the displayed selected-label words are realized by
PBBS voltage words.

The rounding term in (4.5) is irrelevant to the logical construction; one
may take any number of complete abstract cycles, or replicate the cell.

This model is not asserted to be the itinerary of a rank-\(d\), peak-\(k\)
Dyck core.  Indeed, proving that saddle PBBS cores cannot realize this
kind of trace concentration is exactly the missing theorem.  What (4.5)
proves is that none of the following audited facts implies that theorem:

* componentwise particle homomesy;
* bistochastic two-point lag matrices;
* the exact \(0\cdots0\cdots(-1)\) predecessor order;
* logarithmic, or even zero, prescribed terminal occupancy;
* long nonwrapping quotient period; and
* all one-level Pascal fibre and transported-edge capacities.

## 5. Exact proved and conditional boundary

The following statements are proved here.

1. The saddle passage mass is the exact local-time threshold (0.1), and is
   uniformly comparable to \(F_r(d,k)\mathbf1_{\{V_G\ge2\}}\).
2. Its raw second-moment majorant is the three-point trace sum (0.5).
3. The uniform-label part of that energy has the exact required order
   \(O_A(B_r/r)\), with coefficient at most \(2A^2+o_A(1)\).
4. The weighted excess estimate (2.6) implies the linear-seam target
   \(\overline\nu_H=O_A(B_r/r)\).
5. Separate fan and interval factors cannot be multiplied: Lemma 3.1 is a
   sharp integral capacity obstruction.
6. One-point homomesy and the exact one-level chronology do not control the
   excess: Lemma 4.1 and (4.5) realize the larger \(1/\sqrt r\) scale in an
   abstract long-cycle Pascal system.
7. The bounded killed-trace energy (2.8)--(2.18) is pointwise equivalent,
   up to the factor four, to the exact dangerous-core indicator and has the
   same independent baseline as the factorial energy.  It is therefore the
   sharper sufficient trace gate when high local-time bursts are present.

Accordingly, the energy lane has not proved \(CP_A\) (and hence has not
proved the stronger \(RP_A\)).  It has isolated coefficient-correct
statements which would prove the newly requested \(O_A(B_r/r)\) quotient
bound.  The raw three-point form is

\[
 \boxed{
 \sum_{(d,k)\text{ in the Pascal saddle}}
 F_r(d,k)\sum_{1\le u<v\le2H-1}
 \left(
 T_{u,v}(d,k)-{\mathsf N(d,k)\over(2d+1)^2}
 \right)
 =O_A(B_r/r).}
 \tag{5.1}
\]

and the weaker burst-robust form is (2.14).

Because the sum on the left can have cancellations, a bound for its
positive part or for the absolute Fourier excess is a stronger sufficient
form.  The abstract models show that (5.1) must use a genuinely PBBS- and
peak-sensitive restriction on realizable three-point traces.  It cannot be
replaced by marginal Pascal capacity, interval length, phase homomesy, or
bounded-slot information.

No consequence of the retracted primitive-sector converse is used.

## 6. Exact composition with the accepted linear seam

This section records the normalization, since the new target is the
big-oh statement \(CP_A\), not the former little-oh statement \(RP_A\).
Let

\[
 N=2r+1,\qquad W_r=\binom Nr=NB_r.
\]

After deleting quotient cycles of length at most \(H+1\), the audited deck
sandwich is

\[
 \nu_H(P_r)\le2N\overline\nu_H+NZ_H,
 \qquad
 Z_H\le(2H+2)N^{2H+2}.
 \tag{6.1}
\]

For fixed \(A\) and \(H=\lceil A\sqrt r\rceil\),

\[
 \log(NZ_H)=O_A(\sqrt r\log r)=o(r),
 \qquad
 B_r=\exp(r\log4-O(\log r)).
 \tag{6.2}
\]

Thus \(NZ_H=o_A(B_r)\).  Either (2.6) or the weaker (2.14) therefore gives

\[
 \overline\nu_H\le K_A{B_r\over r}
 \quad\Longrightarrow\quad
 \boxed{\nu_H(P_r)\le(4K_A+o_A(1))B_r.}
 \tag{6.3}
\]

This is exactly \(CP_A\), because \(B_r/r\) and \(B_r/N\) differ by the
factor \(N/r=2+1/r\).

The dominance-staircase seam gives the central word ledger

\[
 L_H\le W_r+2HB_r+2(5H-1)\nu_H(P_r).
 \tag{6.4}
\]

Substituting (6.3) and dividing by \(W_r=NB_r\) yields, for fixed \(A\),

\[
 {L_H\over W_r}
 \le1+
 {2H+2(5H-1)(4K_A+o_A(1))\over N}
 =1+O_A\!\left({1\over\sqrt r}\right).
 \tag{6.5}
\]

Finally choose integers \(A_j=j\to\infty\).  If \(K_j\) is the constant
in (6.3), choose thresholds \(R_j\) increasing so rapidly that, whenever
\(r\ge R_j\),

\[
 {j(1+K_j)\over\sqrt r}\le {1\over j},
 \qquad {j^2\over r}\le {1\over j},
 \tag{6.6}
\]

and the already proved product-SCD tail outside the
\(\lceil j\sqrt r\rceil\) band has normalized cost at most \(1/j\).
Put \(A(r)=j\) on \(R_j\le r<R_{j+1}\).  Then \(A(r)\to\infty\),
\(H=o(r)\), the central excess in (6.5) is \(o(1)\), and the outer-tail
cost is \(o(1)\).  The accepted parity lift then gives the
constant-one theorem.

This last paragraph is conditional only on (2.6), or on the strictly
weaker killed-trace estimate (2.14), for every fixed \(A\).  Neither
estimate is proved here.
