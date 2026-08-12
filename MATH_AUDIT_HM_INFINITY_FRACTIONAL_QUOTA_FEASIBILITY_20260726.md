# Fractional \(H_m\)-orbit quota feasibility with the distinguished infinity coordinate

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Let

\[
\Omega=\{\infty\}\sqcup([m]\times\{0,1\}),\qquad
n=2m+1,
\]

and let

\[
H_m=C_2^m\rtimes S_m
\]

fix \(\infty\), permute the \(m\) coordinate pairs, and swap coordinates
inside pairs. For lower depth \(q\), put

\[
k=m-q,\qquad
W=\binom{n}{m},\qquad
N_q=\binom{n}{k},\qquad
\lambda_q=\frac{W}{N_q}=c_q+\theta_q,
\]

\[
c_q=\lfloor\lambda_q\rfloor,\qquad
\rho_q=W-c_qN_q=\theta_qN_q.
\]

The exact conclusions are:

1. Pure \(H_m\)-symmetry has no fractional quota obstruction, even after
   imposing the exact point margins of a wreath factor. The constant
   high density \(\theta_q\) on every target orbit is feasible.

2. The feasibility is simultaneous and nested at the fractional owner
   level: a uniform random deletion order inside every middle owner gives
   every rank-\(k\) target load exactly \(W/N_q\) for every \(q\).

3. An \(H_m\)-fixed integral balanced quota is a separate subset-sum
   problem. For an arbitrary balanced quota, symmetry need be broken in
   at most one orbit. If one also enforces the two necessary infinity-class
   totals, symmetry need be broken in at most one orbit in each stratum.
   Their combined size is \(O_A(W/\sqrt m)\) for \(q\leq A\sqrt m\).
   Exact ordinary-coordinate point regularity of those partial orbits is
   an additional integral design condition and is not proved here.

4. For prescribed orbit masses, the exact half-\(\ell^1\) projection is
   \(\max(D^-,D^+)\) if only total mass is imposed. With the two exact
   infinity-class totals imposed, it is the sum of this maximum over the
   two strata. Requiring integral ordinary-coordinate point regularity can
   only increase this relaxed distance.

5. None of these fractional statements constructs a literal completed
   wreath factor, a two-sided \(X/Y\) chronology, or contiguous-OR rows.
   Any integral orbit congruence or native pair-geodesic obstruction is
   therefore compatible with this fractional feasibility theorem.

6. For the native one-frame pair-face transition, the source state
   \((\epsilon,f)\) is preserved. Its exact Gaussian likelihood ratio
   yields an \(\Omega_\gamma(W)\) under-floor deficit whenever
   \(q/\sqrt m\to\gamma>0\). Thus the fixed-state architecture is closed,
   even though unrestricted \(H_m\)-fractional transport is feasible.

## 1. Complete target-orbit classification

For \(S\subseteq\Omega\), put

\[
\epsilon(S)=\mathbf1_{\{\infty\in S\}},
\]

and let \(f,h,e\) be the numbers of full, split, and empty coordinate
pairs. Then

\[
f+h+e=m,\qquad |S|=2f+h+\epsilon.
\]

Two targets are in the same \(H_m\)-orbit if and only if their quadruples
\((\epsilon,f,h,e)\) agree. Hence a rank-\(k=m-q\) orbit is indexed by
\((\epsilon,f)\), with

\[
h=m-q-\epsilon-2f,\qquad
e=f+q+\epsilon,
\]

and exact size

\[
\boxed{
T_{q,\epsilon,f}
=2^{m-q-\epsilon-2f}
\frac{m!}
 {f!(m-q-\epsilon-2f)!(f+q+\epsilon)!}.}
\tag{1.1}
\]

The range is

\[
0\leq f\leq
\left\lfloor\frac{m-q-\epsilon}{2}\right\rfloor.
\]

The orbit sizes satisfy

\[
\sum_{\epsilon,f}T_{q,\epsilon,f}=N_q.
\tag{1.2}
\]

Write

\[
N_{q,1}=\sum_fT_{q,1,f}=\binom{2m}{k-1},
\qquad
N_{q,0}=\sum_fT_{q,0,f}=\binom{2m}{k}.
\tag{1.3}
\]

Then

\[
\frac{N_{q,1}}{N_q}=\frac{k}{n},
\qquad
\frac{N_{q,0}}{N_q}=\frac{n-k}{n}.
\tag{1.4}
\]

## 2. Exact factor margins and the fractional orbit polytope

Put

\[
B=\frac{W}{n}=\operatorname{Cat}_m.
\]

Every exact wreath-factor rank-\(k\) histogram has total mass \(W\) and
point degree \(kB\) at each coordinate. In particular, its two infinity
class totals are

\[
L_1=kB,\qquad L_0=(n-k)B.
\tag{2.1}
\]

For a balanced quota

\[
b(S)=c_q+\mathbf1_{\mathcal H}(S),
\]

the high-family counts forced in the two strata are

\[
\boxed{
\rho_{q,1}=kB-c_qN_{q,1}=\frac{k\rho_q}{n},}
\tag{2.2}
\]

\[
\boxed{
\rho_{q,0}=(n-k)B-c_qN_{q,0}
=\frac{(n-k)\rho_q}{n}.}
\tag{2.3}
\]

These are integers because the left sides are integers.

Let \(x_{\epsilon,f}\in[0,1]\) be the fractional high density in orbit
\((\epsilon,f)\). The exact factor-compatible fractional quota polytope is

\[
\boxed{
\sum_fT_{q,1,f}x_{1,f}=\rho_{q,1},\qquad
\sum_fT_{q,0,f}x_{0,f}=\rho_{q,0}.}
\tag{2.4}
\]

It is nonempty. Indeed,

\[
\boxed{x_{\epsilon,f}=\theta_q=\rho_q/N_q}
\tag{2.5}
\]

for every \((\epsilon,f)\) satisfies (2.4), by (1.4).

There is no further one-point equation. Inside one orbit, ordinary
coordinates are transitive and each target contains \(k-\epsilon\) of
them. Thus the high incidence at each ordinary coordinate is

\[
\frac1{2m}\sum_{\epsilon,f}
(k-\epsilon)T_{q,\epsilon,f}x_{\epsilon,f}.
\tag{2.6}
\]

Using (2.4), this equals

\[
\frac{k\rho_q-\rho_{q,1}}{2m}
=\frac{k\rho_q}{n},
\tag{2.7}
\]

the same high incidence as at \(\infty\). Hence (2.4) is precisely the
fractional total-and-point-margin system.

## 3. A simultaneous nested fractional selector

For every middle \(m\)-set \(X\), choose a uniformly random ordering of
the elements of \(X\). For all \(q\), let

\[
P_q(X)=X\setminus\{\text{the first \(q\) elements of the order}\}.
\tag{3.1}
\]

The family \(P_q(X)\) is nested in \(q\), and its law is
\(H_m\)-equivariant.

Fix \(S\in\binom{\Omega}{m-q}\). There are

\[
\binom{m+1+q}{q}
\]

middle supersets \(X\supseteq S\), and for each such \(X\), the first
\(q\) elements form any prescribed \(q\)-subset of \(X\) with probability
\(\binom mq^{-1}\). Therefore

\[
\sum_{X\supseteq S}\Pr(P_q(X)=S)
=\frac{\binom{m+1+q}{q}}{\binom mq}
=\frac{\binom{2m+1}{m}}{\binom{2m+1}{m-q}}
=\boxed{\lambda_q.}
\tag{3.2}
\]

Thus every target receives the same proportional fractional load,
simultaneously at every depth. Splitting

\[
\lambda_q=c_q+\theta_q
\]

recovers (2.5) exactly. This is a finite barycentric identity, not an
entropy argument.

The selector supplies only lower nested owner flags. Applying the same
construction to complements supplies an upper fractional selector.
This does not couple the two selectors into one literal wreath path.

## 4. Integral symmetry and the exceptional-orbit bound

A pointwise \(H_m\)-fixed integral balanced quota has binary orbit choices
\(z_{\epsilon,f}\in\{0,1\}\). With exact factor point margins, the exact
arithmetic condition is

\[
\boxed{
\sum_fT_{q,1,f}z_{1,f}=\rho_{q,1},\qquad
\sum_fT_{q,0,f}z_{0,f}=\rho_{q,0}.}
\tag{4.1}
\]

Without the point-margin requirement, only the sum of these two equations
is required. These are exact subset-sum conditions.

For \(q\leq A\sqrt m\),

\[
\max_{\epsilon,f}T_{q,\epsilon,f}
=O_A(N_q/\sqrt m)
=O_A(W/\sqrt m).
\tag{4.2}
\]

This follows from the adjacent ratio

\[
\frac{T_{q,\epsilon,f+1}}{T_{q,\epsilon,f}}
=\frac{(m-q-\epsilon-2f)(m-q-\epsilon-2f-1)}
       {4(f+1)(f+q+\epsilon+1)},
\tag{4.3}
\]

which gives a log-concave sequence of width \(\Theta_A(\sqrt m)\) in
each nonempty infinity stratum.

Consequently:

* ignoring point margins, greedily take whole target orbits up to
  \(\rho_q\), then take a partial subset of one more orbit;
* imposing the necessary infinity-class totals, do the same separately in
  the \(\epsilon=0\) and \(\epsilon=1\) strata, using (2.2)--(2.3).

Thus pure integral orbit granularity can always be confined to one
exceptional orbit without point margins, or to at most two exceptional
orbits while enforcing the two infinity-class totals. In either case its
total support is \(O_A(W/\sqrt m)=o(W)\).

The partial orbit need not itself be point-regular. The second bullet
does not automatically give equal degrees among the ordinary coordinates.
The fractional construction of Section 2 does give exact ordinary point
margins; an integral point-regular completion is a separate question.

## 5. Exact projection of prescribed orbit masses

Let \(M_{\epsilon,f}\) be prescribed nonnegative integral target-orbit
masses. First impose only

\[
\sum_{\epsilon,f}M_{\epsilon,f}=W.
\tag{5.1}
\]

Define

\[
D^-=\sum_{\epsilon,f}
(c_qT_{q,\epsilon,f}-M_{\epsilon,f})_+,
\]

\[
D^+=\sum_{\epsilon,f}
(M_{\epsilon,f}-(c_q+1)T_{q,\epsilon,f})_+.
\tag{5.2}
\]

The clipping proof gives the exact orbit-relaxed formula

\[
\boxed{
\min_b\frac12\|\mu-b\|_1=\max\{D^-,D^+\}.}
\tag{5.3}
\]

Now impose the exact factor stratum totals

\[
\sum_fM_{1,f}=L_1,\qquad
\sum_fM_{0,f}=L_0.
\tag{5.4}
\]

Put

\[
D_\epsilon^-=\sum_f
(c_qT_{q,\epsilon,f}-M_{\epsilon,f})_+,
\]

\[
D_\epsilon^+=\sum_f
(M_{\epsilon,f}-(c_q+1)T_{q,\epsilon,f})_+.
\tag{5.5}
\]

Because the two required high counts are fixed separately by
(2.2)--(2.3), the two clipping problems decouple. Hence

\[
\boxed{
\min_{\substack{b\ \mathrm{balanced}\\
\mathrm{with\ exact\ stratum\ totals}}}
\frac12\|\mu-b\|_1
=\sum_{\epsilon=0}^1
\max\{D_\epsilon^-,D_\epsilon^+\}.}
\tag{5.6}
\]

The minimum is over orbit-relaxed histograms with the prescribed masses.
It is attained by the same clipping-and-redistribution argument within
each stratum. For a fixed literal histogram it remains a lower bound.

In particular, prescribed orbit masses are fractionally compatible with
balanced quotas and the exact factor stratum totals exactly when

\[
c_qT_{q,\epsilon,f}
\leq M_{\epsilon,f}
\leq(c_q+1)T_{q,\epsilon,f}
\tag{5.7}
\]

for every orbit, together with (5.4).

## 6. The native one-frame transition is nevertheless obstructed

The preceding feasibility uses all deletion types. A native pair-face
geodesic is much more restrictive: it deletes only selected elements from
split pairs. It therefore preserves both \(\epsilon\) and \(f\).

The number of middle owners in source state \((\epsilon,f)\) is

\[
\boxed{
V_{\epsilon,f}=T_{0,\epsilon,f}
=2^{m-\epsilon-2f}
\frac{m!}
 {f!(m-\epsilon-2f)!(f+\epsilon)!}.}
\tag{6.1}
\]

A valid depth-\(q\) pair-face start from this state lands in target orbit
\((q,\epsilon,f)\). Hence \(V_{\epsilon,f}\) is an upper capacity for its
load. The exact capacity ratio is

\[
\boxed{
R_{\epsilon,f,q}:=
\frac{V_{\epsilon,f}}{T_{q,\epsilon,f}}
=2^q
\frac{(f+q+\epsilon)!}{(f+\epsilon)!}
\frac{(m-\epsilon-2f-q)!}{(m-\epsilon-2f)!}.}
\tag{6.2}
\]

It is strictly increasing in \(f\), because

\[
\frac{R_{\epsilon,f+1,q}}{R_{\epsilon,f,q}}
=
\frac{f+q+\epsilon+1}{f+\epsilon+1}
\frac{(m-\epsilon-2f)(m-\epsilon-2f-1)}
 {(m-\epsilon-2f-q)(m-\epsilon-2f-q-1)}
>1.
\tag{6.3}
\]

There is already a coarse infinity-stratum mismatch. The source mass with
\(\epsilon=1\) is \(mB\), while the exact rank-\((m-q)\) quota mass in
that stratum is \((m-q)B\). Thus a state-preserving assignment has

\[
qB=q\operatorname{Cat}_m
\tag{6.4}
\]

too many \(\epsilon=1\) starts. At \(q=\Theta(\sqrt m)\), (6.4) is only
\(\Theta(W/\sqrt m)\), so the refinement by \(f\) is essential.

Let

\[
\frac{q}{\sqrt m}\longrightarrow\gamma>0,\qquad
z_{\epsilon,f}
=\frac{4(f-m/4+q/2)}{\sqrt m}.
\tag{6.5}
\]

The fixed \(\epsilon\) changes only \(O(m^{-1/2})\) terms in the following
local limits. Uniformly for bounded \(z_{\epsilon,f}\),

\[
\sqrt m\frac{T_{q,\epsilon,f}}{N_q}
\longrightarrow
\sqrt{\frac2\pi}e^{-z_{\epsilon,f}^2/2},
\tag{6.6}
\]

\[
\sqrt m\frac{V_{\epsilon,f}}{W}
\longrightarrow
\sqrt{\frac2\pi}e^{-(z_{\epsilon,f}-2\gamma)^2/2},
\tag{6.7}
\]

\[
\lambda_q=\frac{W}{N_q}\longrightarrow e^{\gamma^2}.
\tag{6.8}
\]

The factor \(\sqrt{2/\pi}\), rather than \(\sqrt{8/\pi}\), occurs because
each fixed-\(\epsilon\) stratum has asymptotic mass \(1/2\). The two
strata together give a standard normal law in the \(z\)-coordinate.
Equations (6.6)--(6.8) follow directly from the factorial formulas and
the two-sided Stirling inequalities.

Consequently

\[
\boxed{
R_{\epsilon,f,q}
\longrightarrow e^{-\gamma^2+2\gamma z_{\epsilon,f}}.}
\tag{6.9}
\]

Along a subsequence on which \(c_q=c\) is constant, put

\[
z_c=\frac{\log c+\gamma^2}{2\gamma}.
\tag{6.10}
\]

The under-floor states are asymptotically \(z<z_c\). Therefore, writing
\(\Phi\) for the standard normal distribution function,

\[
\boxed{
\frac1W
\sum_{\epsilon,f}
(cT_{q,\epsilon,f}-V_{\epsilon,f})_+
\longrightarrow
c e^{-\gamma^2}\Phi(z_c)
-\Phi(z_c-2\gamma).}
\tag{6.11}
\]

This limit is strictly positive. It is the difference of the target and
source Gaussian masses on the region where their exact likelihood ratio
is below \(c\). If \(e^{\gamma^2}\) is an integer \(L\), the only possible
eventual floor values are \(L-1\) and \(L\); applying (6.11) on each
subsequence still gives a positive lower bound.

Thus, for every fixed \(\gamma>0\),

\[
\sum_{\epsilon,f}
(c_qT_{q,\epsilon,f}-V_{\epsilon,f})_+
=\Omega_\gamma(W).
\tag{6.12}
\]

This is an unavoidable aggregate underload for any construction confined
to one pair frame. If total target mass remains \(W\), it forces the same
amount of positive overload elsewhere. If starts may be discarded, then

\[
\text{discarded mass}+\text{positive overload}
=\Omega_\gamma(W).
\tag{6.13}
\]

Hence every window \(q\leq A\sqrt m\) with a fixed positive limiting
ratio \(q/\sqrt m\) gives a coefficient-one obstruction for the native
\((\epsilon,f)\)-preserving architecture. This does not contradict the
fractional selector of Section 3, which freely crosses the \(f\)-states.

## 7. Implication boundary

The preceding proves a complete absence of fractional obstruction from
the \(H_m\)-target orbit capacities. It does not prove:

* an integral \(H_m\)-fixed factor state;
* a deterministic equivariant selector;
* a joint lower/upper \(X/Y\) owner path;
* exact middle-wreath completion;
* low run count or literal contiguous-OR realization.

In particular, native fixed-pair geodesics preserve a finer source type
and may have a linear state-capacity deficit even though the unrestricted
fractional kernel (3.1) is perfectly balanced. Such a deficit comes from
the allowed transition matrix, not from target-orbit capacity or
wreath-product symmetry alone.
