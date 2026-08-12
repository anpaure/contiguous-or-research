# Rayleigh coagulation as interval flow: exact dual closedness and a renewal obstruction

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional exact equivalence, closedness theorem, and sharp
boundary obstruction.  This note does **not** construct the Rayleigh
coagulation kernel and does not prove the all-grid Bellman inequality.

## 0. Outcome

Put

\[
 A={\sqrt\pi\over2},\qquad p=e^{-A^2},
\]

and let the job and socket measures be

\[
 \mu(dx)=j(x)\,dx,
 \quad j(x)=2(A+x)e^{-(A+x)^2}\quad(x>0),
\tag{0.1}
\]

and

\[
 \nu(dy)=s(y)\,dy,
 \quad s(y)=2(A-y)e^{-(A-y)^2}\quad(0<y<A).
\tag{0.2}
\]

Thus

\[
 \mu(0,\infty)=p,
 \qquad \nu(0,A)=1-p,
 \qquad \int x\,d\mu=\int y\,d\nu.
\tag{0.3}
\]

The exact finite coagulation problem is equivalent to one linear interval
placement problem.  There must be a finite measure `eta` on

\[
 \mathcal E=\{(a,y):a\ge0,\ 0<y<A\}
\tag{0.4}
\]

such that

\[
 (\operatorname{length})_\#\eta=\nu
\tag{0.5}
\]

and

\[
 \boxed{
 \int_{\mathcal E}{\bf1}_{\{a\le t<a+y\}}\,d\eta(a,y)
 =g(t):=e^{-(A+t)^2}
 \quad\text{for a.e. }t\ge0.}
\tag{0.6}
\]

The intervals are the consecutive socket pieces of all jobs.  Conversely,
every measure satisfying (0.5)--(0.6) decomposes into finite directed paths
from zero, and those paths are the required socket groups.

This equivalence gives two further conclusions.

1. The exact configuration cone is closed in the ordinary narrow
   topology.  Consequently the covering-price inequalities are not only
   necessary: they are sufficient.  This closes the analytic
   Hahn--Banach/tightness caveat left open in the first Rayleigh
   coagulation note.
2. A successful interval flow must be strongly state-dependent.  If
   `kappa` is its first-piece marginal, then

   \[
   \kappa(0,t]\ge\mu(0,t]
   \tag{0.7}
   \]

   for every `t`.  Hence the aggregate marginal of nonfirst sockets obeys

   \[
   (\nu-\kappa)(0,t]
   \le p(\pi-2)t^2+O(t^4).
   \tag{0.8}
   \]

   In particular an iid/start-independent renewal kernel is impossible:
   its forced internal-start density is negative at the origin.

The remaining continuum theorem is therefore sharply located: construct a
**state-dependent** interval-length kernel satisfying (0.5)--(0.6), or
prove the equivalent family of nonnegative monotone-subadditive price
inequalities.

## 1. Exact interval-flow equivalence

For a finite measure `eta` on `mathcal E`, define its occupation measure by

\[
 \mathsf O_\eta(B)
 =\int_{\mathcal E}|B\cap[a,a+y)|\,d\eta(a,y)
 \qquad(B\subseteq[0,\infty)\text{ Borel}).
\tag{1.1}
\]

Let `sigma_0` and `sigma_1` be its start and end marginals:

\[
 \sigma_0=(a)_\#\eta,
 \qquad
 \sigma_1=(a+y)_\#\eta.
\tag{1.2}
\]

### Theorem 1.1 (coagulations are exactly Rayleigh interval flows)

The following are equivalent.

1. There is a finite positive measure `rho` on finite configurations

   \[
   (x;y_1,\ldots,y_N),
   \qquad x>0,\quad0<y_i<A,\quad\sum_i y_i=x,
   \tag{1.3}
   \]

   whose job marginal is `mu` and whose aggregate piece marginal is `nu`.
2. There is a finite positive measure `eta` on `mathcal E` satisfying
   (0.5) and

   \[
   \mathsf O_\eta(dt)=g(t)\,dt.
   \tag{1.4}
   \]

Moreover, in either direction one may preserve the complete occurrence
measure of every socket length.

#### Proof

Assume first that `rho` is given.  Choose a measurable ordering of every
finite multiset, for example nondecreasing order with a fixed tie rule.  Put

\[
 a_1=0,
 \qquad
 a_i=y_1+\cdots+y_{i-1}\quad(i\ge2),
\tag{1.5}
\]

and place the interval `[a_i,a_i+y_i)`.  Aggregate these intervals over
`rho` to obtain `eta`.  Its length marginal is exactly `nu`.  Within a job
of size `x`, the intervals partition `[0,x)`.  Therefore its occupation at
`t` is `1_{t<x}`, and

\[
 {d\mathsf O_\eta\over dt}(t)
 =\mu((t,\infty))
 =e^{-(A+t)^2}=g(t).
\tag{1.6}
\]

Conversely suppose `eta` is given.  For every compactly supported
continuously differentiable `f`, Fubini gives

\[
 \int f\,d(\sigma_1-\sigma_0)
 =\int_{\mathcal E}\bigl(f(a+y)-f(a)\bigr)\,d\eta
 =\int_0^\infty f'(t)g(t)\,dt.
\tag{1.7}
\]

Since `g(0)=p` and `g'(t)=-j(t)`, integration by parts yields

\[
 \boxed{\sigma_1-\sigma_0=\mu-p\delta_0.}
\tag{1.8}
\]

An interval endpoint is strictly positive, so `sigma_1` has no atom at
zero.  Taking the atom at zero in (1.8) consequently gives

\[
 \sigma_0(\{0\})=p.
\tag{1.9}
\]

Thus, with

\[
 \tau=\sigma_0-p\delta_0,
\tag{1.10}
\]

equation (1.8) is the exact flow balance

\[
 \boxed{
 \sigma_0=p\delta_0+\tau,
 \qquad
 \sigma_1=\mu+\tau.}
\tag{1.11}
\]

Disintegrate `eta` over both endpoint marginals.  At a positive location
`x`, split the incoming edge kernel in the Radon--Nikodym proportions

\[
 {d\tau\over d(\mu+\tau)}(x),
 \qquad
 {d\mu\over d(\mu+\tau)}(x).
\tag{1.12}
\]

The first part is paired with the outgoing edge kernel, whose base measure
is exactly `tau`; the second part is declared terminal.  Iterating from the
source mass `p delta_0` constructs a measure on finite or countably infinite
directed paths and a generated edge submeasure `eta_gen<=eta`.  Every edge
strictly increases its location.  The unused edge measure
`zeta=eta-eta_gen`, if nonzero, has equal start and end marginals: all source
mass has been inserted, and the continuation pairing exhausts the same
`tau` on its incoming and outgoing sides.

If `zeta` were such a residual flow, its occupation density `h_zeta` would have distributional
derivative zero by (1.7).  Hence `h_zeta` would be constant almost
everywhere.  But

\[
 \int_0^\infty h_\zeta(t)\,dt
 =\int_{\mathcal E}y\,d\zeta(a,y)<\infty,
\]

so that constant is zero.  Since every edge has positive length,
`zeta=0`.  Thus the generated paths exhaust all of `eta`.

No positive mass can then escape along an infinite path.  The aggregate
number of traversed edges is

\[
 \eta(\mathcal E)=\nu(0,A)=1-p<\infty.
\tag{1.13}
\]

The source mass is `p`; hence the mean number of edges on a source path is
`(1-p)/p<\infty`.  The number of edges is therefore finite almost surely.
Every path begins at zero, ends with marginal `mu`, and its consecutive
edge lengths sum to its endpoint.  Sending each path to the configuration
of its edge lengths gives `rho`.  Its aggregate length marginal remains
the length marginal of `eta`, namely `nu`.  This proves the equivalence.
`square`

### Remark 1.2 (the exact boundary measures)

Equation (1.11) is the concise start/end form requested by the interval
picture:

\[
 \boxed{
 \text{starts}=p\delta_0+\tau,
 \qquad
 \text{ends}=j(x)\,dx+\tau.}
\tag{1.14}
\]

The occupation profile is not an additional independent constraint once
these boundary measures and vanishing occupation at infinity are known;
it is their integrated divergence.

## 2. Closedness and exact sufficiency of configuration prices

For a nonnegative socket price `a` define its physical covering closure

\[
 a^\star(x)=
 \inf\left\{
   \sum_{i=1}^N a(y_i):
   N\ge1,\quad0<y_i<A,\quad\sum_i y_i\ge x
 \right\}.
\tag{2.1}
\]

### Theorem 2.1 (the price inequalities are an iff theorem)

For the Rayleigh measures `mu,nu`, an exact coagulation exists if and only
if

\[
 \boxed{
 \int_0^\infty a^\star(x)\,d\mu(x)
 \le
 \int_0^A a(y)\,d\nu(y)}
\tag{2.2}
\]

for every nonnegative bounded continuous price `a`.

#### Proof

Necessity follows by applying (2.1) to every configuration and integrating.
We prove the closedness needed for sufficiency.

It is convenient first to allow an aggregate used-capacity marginal
`lambda<=b`, where `b` is an available-capacity measure.  A job of size
`x` may use capacities whose sum is at least `x`; this is precisely the
physical trimming relaxation.  Let `mathcal F` be the set of all available
measures `b` for which such a kernel with job marginal `mu` exists.
This set is convex and upward closed.

Put the ordinary narrow topology on finite positive measures on `(0,A)`;
equivalently, test against `C_b((0,A))`.  We claim that `mathcal F` is
closed in this topology.  Indeed, let `b_n in mathcal F` converge narrowly
to `b`, and choose witnessing kernels `rho_n` with used marginals
`lambda_n<=b_n`.  Their expected piece counts are uniformly bounded:

\[
 \int N\,d\rho_n=\lambda_n(0,A)
 \le\sup_n b_n(0,A)<\infty.
\tag{2.3}
\]

Hence the configuration masses with `N>R` are `O(1/R)`.  For bounded `N`,
tightness of the fixed job marginal and compactness of `[0,A]` give
tightness on the configuration compactification which permits boundary
piece sizes.  Narrow convergence of `b_n` makes that family uniformly tight
inside `(0,A)`; because `lambda_n<=b_n`, no positive aggregate piece mass
can appear at either boundary.  A weakly convergent subsequence `rho_n ->
rho` therefore exists.  The covering inequality is closed and the job
marginal remains `mu`.

For `f in C_c((0,A))`, `f>=0`, the configuration functional

\[
 \Phi_f(x;y_1,\ldots,y_N)=\sum_{i=1}^N f(y_i)
\tag{2.3a}
\]

is nonnegative and lower semicontinuous on the disjoint-union
compactification.  Portmanteau and `lambda_n<=b_n` give

\[
 \int\Phi_f\,d\rho
 \le\liminf_n\int\Phi_f\,d\rho_n
 \le\lim_n\int f\,db_n
 =\int f\,db.
\tag{2.3b}
\]

Thus the aggregate positive-piece marginal of `rho` is at most `b`.
Any zero pieces may be deleted; a configuration containing no positive
piece has `x=0` and hence zero `rho`-mass.  Therefore `b in mathcal F`.
Since narrow convergence on a bounded-mass subset of this Polish measure
space is metrizable, this sequential argument proves the closedness needed
below.  (The same conclusion can also be derived from Theorem 1.1 by
tightness of interval occupation measures.)

If no admissible kernel existed, `nu` would lie outside the closed convex
upward set `mathcal F`.  Strong separation gives a continuous socket price
`a`.  Upward closure forces `a>=0`.  Minimizing its value over
`mathcal F` separates independently over the jobs, and therefore gives

\[
 \inf_{b\in\mathcal F}\int a\,db
 =\int a^\star(x)\,d\mu(x).
\]

This equality does not hide a finite-piece integrability assumption.  For
`M>=1`, first restrict (2.1) to pieces bounded away from zero and from `A`.
After redundant pieces are deleted, a near-minimizing cover uses
`O_M(1+x)` pieces, which is integrable against `mu`.  Standard measurable
selection therefore gives a witnessing kernel for the restricted
pointwise infimum.  As the two cutoffs tend to the endpoints, these
restricted infima decrease pointwise to `a^star`.  A cover using one fixed
socket length has integrable cost `O(1+x)`, so dominated convergence gives
the displayed equality.

The strict separating inequality would be the reverse of (2.2), a
contradiction.  This proves sufficiency.

Finally every admissible relaxed kernel has zero trimming and uses every
socket.  If its configuration capacities are `y_i`, then

\[
 0\le
 \int\left(\sum_i y_i-x\right)d\rho
 +\int y\,d(\nu-\lambda)
 =\int y\,d\nu-\int x\,d\mu=0.
\tag{2.4}
\]

Both nonnegative terms vanish.  Thus `sum_i y_i=x` almost everywhere and,
because `y>0`, `lambda=nu`.  The relaxed closed problem and the exact
coagulation problem coincide. `square`

### Scope of Theorem 2.1

The theorem closes only the analytic duality caveat.  It does not prove
the inequalities (2.2).  Every `a^star` is nonnegative, nondecreasing,
subadditive, and idempotent under covering closure.  Replacing `a` on the
socket interval by `a^star` preserves the left side and can only decrease
the right side.  Thus (2.2) is exactly the covering-closed
nondecreasing-subadditive/all-grid Bellman gate already isolated in the
discrete and Gaussian notes.

One endpoint subtlety is worth recording.  A literal covering closure need
not be lower semicontinuous because pieces satisfy the strict bound `y<A`:
for the constant socket price one, `a^star` jumps upward at every positive
multiple of `A`.  It may be replaced by its lower-semicontinuous left-limit
representative inside the two atomless integrals, but that representative
is not the literal pointwise covering cost at the jumps.  No
lower-semicontinuity equivalence is used in Theorem 2.1.

## 3. A sharp first-piece boundary law

Let `rho` be any exact coagulation, choose any measurable ordering of the
pieces in every group, and let `kappa` be the marginal of the first piece.

### Theorem 3.1 (prefix Hall and quadratic internal aperture)

For every `t>=0`,

\[
 \boxed{\kappa(0,t]\ge\mu(0,t].}
\tag{3.1}
\]

Consequently

\[
 \boxed{
 (\nu-\kappa)(0,t]
 \le
 e^{-(A-t)^2}+e^{-(A+t)^2}-2e^{-A^2}}
 \qquad(0\le t\le A),
\tag{3.2}
\]

and, as `t downarrow 0`,

\[
 \boxed{
 (\nu-\kappa)(0,t]
 \le p(\pi-2)t^2+O(t^4).}
\tag{3.3}
\]

The right side of (3.2) is strictly positive for `0<t<=A`, so the first
prefix Hall row itself does not obstruct the Rayleigh measures.

#### Proof

Every job of size at most `t` has every positive piece, and in particular
its first piece, of size at most `t`.  Counting those jobs proves (3.1).
Since `kappa<=nu`, subtracting (3.1) from the socket cumulative gives

\[
 (\nu-\kappa)(0,t]
 \le\nu(0,t]-\mu(0,t].
\tag{3.4}
\]

The two explicit cumulative distributions turn the right side into

\[
 e^{-(A-t)^2}+e^{-(A+t)^2}-2p
 =2p\left(e^{-t^2}\cosh(2At)-1\right),
\tag{3.5}
\]

which proves (3.2).  Since `A^2=pi/4`, its Taylor expansion is

\[
 2p(2A^2-1)t^2+O(t^4)
 =p(\pi-2)t^2+O(t^4),
\]

proving (3.3).

To see strict positivity on the full interval, put

\[
 S(t)=e^{-(A-t)^2}+e^{-(A+t)^2}.
\]

Its logarithmic derivative has the sign of
`A tanh(2At)-t`, which is positive and then negative exactly once.  Thus
`S` first increases and then decreases.  Also

\[
 S(0)=2p,
 \qquad
 S(A)=1+e^{-\pi}>2p,
\]

the last inequality following already from `p<1/2`.  Hence
`S(t)>S(0)` for `0<t<=A`. `square`

### Interpretation

The socket density at zero and the job density at zero agree.  Equation
(3.3) is the stronger integrated statement: to first order, **all** very
short sockets must be first pieces.  Only a quadratic amount of short
socket mass is available for later positions in a group.

## 4. Start-independent renewal is impossible

A natural attempt is to choose every interval length independently of its
start.  The preceding boundary law rules this out, and the sign failure is
literal.

### Theorem 4.1 (iid renewal no-go)

There is no interval flow of the product form

\[
                         \eta(da,dy)=\alpha(da)k(dy).
\tag{4.1}
\]

Here the immaterial product scaling is normalized by requiring `k` to be
a probability measure.

Equivalently, no construction in which every initial and internal state
uses the same start-independent socket-length distribution can solve the
Rayleigh coagulation problem.

#### Proof

The total interval mass is `1-p`, so (0.5) forces

\[
 k(dy)={\nu(dy)\over1-p}.
\tag{4.2}
\]

The start marginal is `alpha`.  By (1.11), write

\[
 \alpha=p\delta_0+\tau.
\tag{4.3}
\]

The end marginal of the product flow is `alpha*k`; hence flow balance is

\[
 \tau=pk+\tau*k-\mu.
\tag{4.4}
\]

The right side is absolutely continuous on `(0,\infty)`, so `tau` has a
density `r`.  Because `tau` has no atom at zero,

\[
 (\tau*k)(x)\longrightarrow0\qquad(x\downarrow0).
\tag{4.5}
\]

Taking the right limit in (4.4) gives

\[
 \begin{aligned}
 r(0+)
 &=p\,{s(0)\over1-p}-j(0)\\
 &=2Ap\left({p\over1-p}-1\right)\\
 &=2Ap\,{2p-1\over1-p}<0.
 \end{aligned}
\tag{4.6}
\]

Here `p<1/2` because `pi/4>log 2`.  A positive measure cannot have a
strictly negative density on a right neighborhood of zero.  Contradiction.
`square`

The obstruction is local, not a failure of the scalar ledgers.  A
successful renewal description must correlate the next socket length with
the current partial sum or residual job size.

## 5. A one-piece cancellation face and the separated residual problem

The two densities have one nonzero crossing.  Let `c in (0,A)` be its
location.  Assigning the common density directly to one-piece jobs gives a
useful sufficient construction face for the remaining adaptive problem.

### Proposition 5.1 (unique diagonal crossing)

There is a unique `c in (0,A)` such that

\[
                         j(c)=s(c).
\tag{5.1}
\]

Writing `c=Atheta`, it is characterized by

\[
 \boxed{\operatorname{arctanh}\theta={\pi\over2}\theta,
 \qquad0<\theta<1.}
\tag{5.2}
\]

Moreover `s>j` on `(0,c)` and `j>s` on `(c,A)`.

#### Proof

The density equality is

\[
 {A+c\over A-c}=e^{4Ac}.
\]

After putting `c=Atheta` and `A^2=pi/4`, taking logarithms gives
(5.2).  The function
`atanh(theta)/theta` is strictly increasing from one to infinity, whereas
`pi/2>1`, so there is exactly one positive solution.  The endpoint signs
give the final assertion. `square`

### Corollary 5.2 (separated residual construction face)

Match the common density

\[
 h(y)=\min\{j(y),s(y)\}\qquad(0<y<A)
\tag{5.3}
\]

as one-piece jobs.  The remaining socket and job measures are

\[
 \nu_{\rm res}(dy)=(s(y)-j(y))\mathbf1_{(0,c)}(y)\,dy,
\tag{5.4}
\]

and

\[
 \mu_{\rm res}(dx)
 =(j(x)-s(x))\mathbf1_{(c,A)}(x)\,dx
  +j(x)\mathbf1_{[A,\infty)}(x)\,dx.
\tag{5.5}
\]

They have equal first moments, and their supports are strictly separated:

\[
 \operatorname{supp}\nu_{\rm res}\subset(0,c),
 \qquad
 \operatorname{supp}\mu_{\rm res}\subset(c,\infty).
\tag{5.6}
\]

Their count difference remains

\[
 \nu_{\rm res}(0,c)-\mu_{\rm res}(c,\infty)
 =1-2p>0.
\tag{5.7}
\]

#### Proof

Removing the same measure `h(y)dy` from the job and socket marginals
preserves equality of first moments and preserves their count difference.
The support assertion follows from Proposition 5.1. `square`

Thus one may construct the full solution by assigning all literal
one-piece overlap first and solving the displayed separated residual pair.
The remaining question on this face is a reverse subtraction flow:
repeatedly assign a residual socket `y<c` to a current residual endpoint
`x>y`, replace the endpoint by `x-y`, and terminate exactly when the
residual reaches zero.  Theorem 4.1 shows that the choice of `y` cannot be
independent of the current residual.

This corollary is stated in the proof-safe direction: a solution of the
residual pair plus the diagonal one-piece configurations solves the full
problem.  No cancellation theorem asserting that every pre-existing full
kernel can be rearranged onto this face is used.

## 6. Exact remaining gate

The anonymous Gaussian rank-only problem is equivalent to items 1 and 3
below.  Item 2 is a strictly more structured sufficient construction.

1. There is a state-dependent interval kernel with length marginal `nu`
   and occupation profile `g`.
2. The separated residual pair (5.4)--(5.5) admits an adaptive reverse
   subtraction flow using every residual socket once; this implies item 1.
3. Every nonnegative nondecreasing subadditive covering price satisfies
   the Rayleigh configuration inequality (2.2).

By Theorem 2.1, item 3 has no remaining analytic closedness qualification.
By Theorem 4.1, it cannot be proved by writing the flow as an ordinary iid
renewal process.  The next constructive target is a residual-dependent
monotone coupling whose subtraction step preserves the prefix Hall order
and whose active mass tends to zero.

Even a solution of this continuum gate would still require discrete
rounding/absorption, named Boolean containment, literal run serialization,
and the upper/residence host.  No claim about those later gates is made
here.
