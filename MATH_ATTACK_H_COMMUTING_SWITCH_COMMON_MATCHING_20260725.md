# Commuting-switch common matching: exact links and the surviving gate

Date: 2026-07-25

Method: pure mathematics only.

## 0. Verdict

This report does not prove coefficient one. It establishes:

1. exact owner, same-rank, mixed, and higher link formulae for the
   commuting-switch trajectory catalogue;
2. a rigorous first grouped nibble bite;
3. a polynomial obstruction to every product-quasirandom iteration of that
   bite;
4. exact Boolean-switch and mesoscopic block absorbers; and
5. a relaxed unmatched-tag threshold
   \[
     e=o(Nm^{-1/3})=o(W/m^{4/3})
   \]
   for recalibrated quotas followed by separate literal repair.

Write

\[
 n=2m,\quad M=m+H,\quad
 W=\binom{2m}{m},\quad N=\binom{2m}{M},
\]

where \(H\) is the first crossing with \(W/N\ge M\). Thus

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 N=(1+o(1))W/m,\qquad MN=W-O(WH/m).
\]

Let \(Q=o(H)\) be the audited tail-killing truncation and put

\[
 R_q=\binom{2m}{m-q}=\binom{2m}{m+q},
\qquad
 c_0=M,\qquad
 c_q=\min\!\left\{M,\left\lfloor\frac{R_q}{N}\right\rfloor\right\}.
\tag{0.1}
\]

## 1. One-bit localization

Pair the phase indices \((0,1),(2,3),\ldots\), independently transpose
each pair, and let \(\beta=\lfloor M/2\rfloor\). The decorated tag degree is

\[
 A=2^\beta(M!)^2,
\tag{1.1}
\]

including all coordinate labellings and common priorities.

If \(\eta_t\) is the switch bit affecting phase \(t\), extended by zero at
the other phases, then

\[
 B_t=[t-H,t-1]-\eta_t\{t-H\}+\eta_t\{t-H-1\},
\tag{1.2}
\]

\[
 U\setminus L_q(t)
 =[t-H,t+q-1]-\eta_t\{t-H\}+\eta_t\{t-H-1\},
\tag{1.3}
\]

\[
 U\setminus U_q(t)
 =[t-H,t-q-1]-\eta_t\{t-H\}+\eta_t\{t-H-1\}.
\tag{1.4}
\]

These follow by substituting the rotor identities

\[
 L_q(t)=X_t-\{u_t,\ldots,u_{t+q-1}\},\qquad
 U_q(t)=X_t+\{u_{t-1},\ldots,u_{t-q}\}.
\]

Thus a complete vertical stack depends on one bit. Constraints at distinct
switch phases factor exactly: if \(J\) is the constrained phase set and
\(E_z\subseteq\{0,1\}\) is the allowed bit set at \(z\), then the number
of compatible switch vectors is

\[
 2^{\beta-|J|}\prod_{z\in J}|E_z|.
\tag{1.5}
\]

## 2. Exact same-type links

For a defected interval of length \(h<M/2\), let \(p_{h,j}\) be the mean
number of other phases at Johnson distance \(j\). Direct endpoint
comparison gives

\[
 p_{h,j}=
 \begin{cases}
 2,&1\le j\le h-2,\\
 2+\beta/M,&j=h-1,\\
 M-2h+1-\beta/M,&j=h.
 \end{cases}
\tag{2.1}
\]

Indeed the ordinary interval spectrum changes only at separations
\(h\) and \(M-h\); each boundary switch has mean \(\beta/(2M)\). The
check \(\sum_jp_{h,j}=M-1\) is exact.

The target degrees are

\[
 D_0=A\frac{MN}{W},\qquad
 D_q=A\frac{c_qN}{R_q}.
\tag{2.2}
\]

If middle owners \(X,Y\) have Johnson distance \(j\), then

\[
 \boxed{\frac{\deg(X,Y)}{D_0}
 =\frac{p_{H,j}}{\binom mj^2}.}
\tag{2.3}
\]

Consequently the maximum distinct-owner normalized link is exactly
\(2/m^2\).

If same-rank targets \(S,T\), of rank \(r=m\pm q\), have Johnson distance
\(j\), and \(h=M-r\), then

\[
 \boxed{
 \frac{\deg(S,T)}{D_q}
 =\frac{c_q-1}{M-1}
  \frac{p_{h,j}}{\binom rj\binom{2m-r}j}.}
\tag{2.4}
\]

The maximum is

\[
 \frac{2(c_q-1)}{(M-1)(m-q)(m+q)}
 =\frac{2+o(1)}{m^2}.
\tag{2.5}
\]

For (2.3), label the four membership atoms of two hole templates; their
sizes are \(H-j,j,j,m-j\). For (2.4), the local partner count is
\(\binom rj\binom hj\), the common-priority correction is
\((c_q-1)/(M-1)\), and the ratio of common-carrier counts is
\(\binom hj/\binom{2m-r}j\). These factors give the displayed formulae.

## 3. Mixed and higher links

For an owner \(X\) and signed depth-\(q\) target \(S\), put

\[
 a=|X\setminus S|,\qquad b=|S\setminus X|.
\]

Let \(\kappa_q^\pm(a,b)\) be \(1/(2^\beta M)\) times the number of
switch-vector/ordered-phase triples having this oriented profile. Then

\[
 \boxed{
 \frac{\deg(X,S)}{D_0}
 =\frac{c_q}{M}
  \frac{\kappa_q^\pm(a,b)}{\binom ma\binom mb}.}
\tag{3.1}
\]

Every lower \(q\)-flag lies in exactly
\(X_t,X_{t+1},\ldots,X_{t+q}\); dually every upper \(q\)-flag contains
exactly \(X_t,X_{t-1},\ldots,X_{t-q}\). Hence a nested pair has

\[
 \boxed{
 \frac{\deg(X,S)}{D_0}
 =\frac{c_q}{M}\frac{q+1}{\binom mq}.}
\tag{3.2}
\]

At \(q=1\) this is \((2+o(1))/m\), not \(1/m\): the unpointed edge
contains two adjacent owner phases. Every deeper nested or nonnested mixed
link is \(O(m^{-2})\).

There is also an exact master formula. For typed targets
\(S_1,\ldots,S_k\), prescribe every nonzero membership-atom size \(n_J\).
A compatible phase tuple contributes the labelling and carrier factors

\[
 (M-|\cup_iS_i|)!\prod_{\varnothing\ne J\subseteq[k]}n_J!,
\qquad
 \binom{2m-|\cup_iS_i|}{M-|\cup_iS_i|}.
\tag{3.3}
\]

If the distinct constrained phases have sorted priority thresholds
\(d_1\le\cdots\le d_\ell\), the priority factor is

\[
 (M-\ell)!\prod_{i=1}^{\ell}(d_i-i+1).
\tag{3.4}
\]

Multiplying (3.3)--(3.4), applying the bit factor (1.5), and summing over
compatible phase tuples is the exact mixed higher codegree.

For independent trajectories on fixed tags \(U,V\), with
\(s=|U\cap V|\), the common-target count \(Z_r\) in rank \(r=m\pm q\)
satisfies

\[
 \mathbb EZ_r=\binom sr
 \left(\frac{c_q}{\binom Mr}\right)^2,
\tag{3.5}
\]

\[
\begin{aligned}
 \mathbb E(Z_r)_2
 =\sum_{j=1}^{M-r}
 &\binom sr\binom rj\binom{s-r}j\\
 &\cdot
 \left[
 \frac{c_q}{\binom Mr}
 \frac{c_q-1}{M-1}
 \frac{p_{M-r,j}}{\binom rj\binom{M-r}j}
 \right]^2.
\end{aligned}
\tag{3.6}
\]

## 4. First bite and exact nibble obstruction

Let \(K=M+2\sum_{q=1}^Qc_q=(\sqrt\pi+o(1))m^{3/2}\) be the claimed
target count per trajectory.

### Theorem 4.1 (grouped first bite)

For \(0<\theta\le1\), there is a target-disjoint selection on at least

\[
 \left(\theta-\frac{\theta^2}{2}\right)\frac NK
\tag{4.1}
\]

tags.

#### Proof

Let \(p_{Ux}\) be the probability that a uniform column above \(U\)
contains \(x\). The exact fractional matching gives
\(\sum_Up_{Ux}\le1\), while \(\sum_xp_{Ux}=K\). Activate each tag with
probability \(\theta/K\), choose one column, and join colliding choices.
The expected number of collision-graph edges is at most

\[
 \frac{\theta^2}{2K^2}
 \sum_x\left(\sum_Up_{Ux}\right)^2
 \le\frac{\theta^2N}{2K}.
\]

The expected active count is \(\theta N/K\). Delete one endpoint per
collision edge. \(\square\)

This bite cannot be iterated by a product-quasirandom argument. Let
\(\lambda_q=Nc_q/R_q=1-o(1)\) uniformly. Every edge contains \(c_q\)
same-anchor adjacent-rank flag pairs for each sign, and the codegree of
each such pair divided by \(A\) is exactly

\[
 \frac{\lambda_q}{m+q}.
\tag{4.2}
\]

For

\[
 \Psi_j(P)=\frac1A
 \sum_{\operatorname{tag}(F)\ne\operatorname{tag}(P)}
 \binom{|P\cap F|}{j},
\]

it follows that

\[
 \boxed{\Psi_2(P)\ge(\sqrt\pi+o(1))\sqrt m.}
\tag{4.3}
\]

Under independent target retention of density \(z\), the nonlinear
conditioning term contains

\[
 \sum_{j\ge2}\Psi_j(P)(z^{-1}-1)^j.
\]

At \(z=m^{-1/3}\), (4.3) alone makes this at least
\(m^{7/6+o(1)}\). Moreover every block-permutation catalogue has
\(A\le(M!)^3\), so the expected residual degree of one tag is at most

\[
 (M!)^3z^K.
\tag{4.4}
\]

At \(z=m^{-1/3}\), its logarithm is

\[
 -(\sqrt\pi/3+o(1))m^{3/2}\log m.
\tag{4.5}
\]

Thus a successful process must preserve correlated whole columns; pair
codegree and product residuals are provably insufficient.

## 5. Exact local absorbers

For fixed switch cells, form the multigraph whose vertices are available
owners and whose edges are the two owner alternatives of each cell.
Choosing distinct owners is exactly an edge-to-endpoint SDR.

### Theorem 5.1 (switch SDR)

With no pinned one-option cells, an SDR exists exactly when every component
is a tree or unicyclic. With pins, the exact possibilities are a tree with
at most one pin, or a unicyclic component with no pin.

Orient a tree away from its root and a unicyclic component cyclically with
attached trees directed away from the cycle. Necessity is the component
Hall inequality. An unbiased distribution, giving every edge each endpoint
with probability \(1/2\), exists exactly for paths and bare cycles.

Three parallel switch cells on the same adjacent owner pair are realizable
on three genuine carriers and have no SDR. Thus the unrestricted Boolean
absorber is false.

Permuting arrivals in blocks of length \(L\le H-Q\) gives a stronger local
object. At internal level \(j\), the returned set is a uniform
\(j\)-subset \(R_j\) of the block and

\[
 \varnothing=R_0\subset R_1\subset\cdots\subset R_{L-1}
\]

runs through all maximal Boolean chains. Hence forbidden families
\(\mathcal F_j\subseteq\binom{[L]}j\) can be avoided whenever

\[
 \sum_{j=1}^{L-1}
 \frac{|\mathcal F_j|}{\binom Lj}<1.
\tag{5.1}
\]

There are only \(\lceil M/L\rceil\) immutable boundary stacks per carrier,
so their total charge is

\[
 N\left\lceil\frac ML\right\rceil(2Q+1)
 \le W(2Q+1)\left(\frac1L+\frac1M\right).
\tag{5.2}
\]

Taking \(L\asymp H\) makes this \(o(W)\). Global trace-fibre
factorization and cross-fibre disjointness remain unproved.

## 6. Adaptive unmatched-tag leave

Let \(N'=N-e\) and recalibrate

\[
 d_0(e)=M,\qquad
 d_q(e)=\min\!\left\{M,\left\lfloor\frac{R_q}{N'}\right\rfloor\right\}.
\tag{6.1}
\]

### Theorem 6.1

Suppose trajectories on \(N-e\) tags realize these common nested quotas
with all claimed targets disjoint. If

\[
 \boxed{e=o(Nm^{-1/3}),}
\tag{6.2}
\]

then separate literal repair, followed by the audited outer reservoir and
tails, has total length \(W+o(W)\).

#### Proof

Put

\[
 \Delta=W-MN',\qquad\delta=\Delta/W.
\]

Then

\[
 \delta=O(H/m)+O(e/N)=o(m^{-1/3}).
\tag{6.3}
\]

The middle positions and their literal holes cancel exactly:

\[
 MN'+(W-MN')=W.
\tag{6.4}
\]

At an uncapped positive depth, the deficit is less than \(N'\), so all
uncapped rows cost \(O(QN)=o(W)\). At a capped depth,
\(R_q\ge MN'=W(1-\delta)\), while

\[
 \frac{R_q}{W}
 \le\exp\!\left(-\frac{q^2}{m+q}\right).
\]

Thus \(q\le2\sqrt{m\delta}\), and each capped deficit is at most
\(W\delta\). Their total is

\[
 O(W\delta+W\sqrt m\,\delta^{3/2})=o(W).
\]

\(\square\)

This exponent is sharp for separate literal charging. Indeed

\[
 1-\frac{R_q}{W}\le\frac{q^2}{m},
\]

so every \(q\le\sqrt{m\delta/2}\) has at least \(W\delta/2\) holes after
only \(MN'\) distinct occurrences. Their total is
\(\Omega(W\sqrt m\,\delta^{3/2})\).

The surviving clean gate is therefore a block-permutation common matching
on \(N-o(Nm^{-1/3})\) tags, after deleting the \(o(W)\) boundary stacks.
No such global matching is proved here.

