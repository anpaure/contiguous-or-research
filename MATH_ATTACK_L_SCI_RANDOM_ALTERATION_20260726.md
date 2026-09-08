# SCI exact dual, strip codegrees, and randomized alteration

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, or web input is
used.

## 0. Verdict

For the physical \(h\)-strip catalogue and the central window
\(0\le q\le H\), uniform independent selection followed by singleton repair
fails much more strongly than by a constant factor.

Write

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 r_q=\frac{N_q}{W},\qquad
 \alpha=1+\frac Hh.
\]

If every strip is selected independently with probability \(p\), and
\(\lambda=pD_0\), then the expected strip-block plus singleton cost, divided
by \(W\), is exactly

\[
 \Phi_m(\lambda)
 =\alpha\lambda+
   \left(1-\frac{\lambda}{D_0}\right)^{D_0}
   +2\sum_{q=1}^{H}r_q
      \left(1-\frac{\lambda}{D_0}\right)^{D_0/r_q}.
                                                        \tag{0.1}
\]

At expected strip-block cost \(W+o(W)\), so that \(\lambda=1+o(1)\),
the expected singleton leave is

\[
 (\kappa+o(1))\sqrt m\,W,
 \qquad
 \kappa=2\int_0^\infty
  \exp\{-x^2-e^{x^2}\}\,dx>0.                         \tag{0.2}
\]

After optimizing \(p\) without a strip-cost restriction, the unique optimum
satisfies

\[
 \lambda_*
 =\frac12\log m-\frac12\log\log m
   +\frac12\log(2\pi)+o(1),                           \tag{0.3}
\]

and

\[
 \min_p\frac{\mathbb E[\text{cost}]}W
 =\frac12\log m-\frac12\log\log m
   +\frac12\log(2\pi)+1+o(1).                        \tag{0.4}
\]

Thus independent alteration cannot prove SCI.

The obstruction is not orbit symmetry alone. A random conjugate of an
integral middle near-factor is orbit-symmetric and can have exponentially
small middle leave at the same one-fold marginal load. Its cycle indicators
are strongly dependent. Uniform fixed-size sampling without replacement,
on the other hand, has the same asymptotic loss as independent sampling.

More generally, every independent Bernoulli scheme whose column
probabilities are bounded by \(1-\varepsilon\), for fixed
\(\varepsilon>0\), has optimized expected cost

\[
 \Omega_\varepsilon(W\log m).                         \tag{0.5}
\]

Hence any successful independent scheme must develop near-deterministic
columns; arbitrary nonuniform independent selection already contains the
unknown integral problem as its \(0/1\) endpoint.

Finally, the fractional strip-cover optimum can be sharpened exactly:

\[
 \boxed{
 \tau^*_{m,H,h}
 =W+\frac Hh\binom{2m}{m-1}
 =W\left(1+\frac Hh\frac m{m+1}\right).}             \tag{0.6}
\]

Consequently neither the ordinary weighted dual nor any argument using only
per-rank target counts can yield an \(\Omega(W)\) integrality-gap
obstruction. Such an obstruction would have to use genuinely intersecting,
labelled whole-cycle constraints.

## 1. Exact incidence notation

Let \(\mathscr C=\mathscr C_{m,h}\), let \(M=|\mathscr C|\), and let
\(D_q\) be the number of catalogue cycles containing a fixed target in one
signed layer at depth \(q\). The catalogue identities are

\[
 M(2h)=WD_0=N_qD_q.                                  \tag{1.1}
\]

Therefore

\[
 r_q=\frac{N_q}{W}=\frac{D_0}{D_q},
 \qquad D_q=\frac{D_0}{r_q},                         \tag{1.2}
\]

and

\[
 r_q=\prod_{j=1}^q\frac{m-j+1}{m+j},qquad
 1=r_0>r_1>\cdots>r_H>0.                             \tag{1.3}
\]

The literal cost of one selected strip is

\[
 c=2h+2H=2h\alpha.                                   \tag{1.4}
\]

## 2. Uniform Bernoulli selection: exact rank ledger

Select every \(C\in\mathscr C\) independently with probability \(p\), and
append a singleton for every target not lying on a selected cycle. A fixed
depth-\(q\) target is uncovered with probability

\[
 u_q(p)=(1-p)^{D_q}.                                 \tag{2.1}
\]

There is one middle layer and two signed layers for each \(q\ge1\). Hence

\[
 \mathbb E[\text{cost}]
 =cMp+W(1-p)^{D_0}
   +2\sum_{q=1}^HN_q(1-p)^{D_q}.                    \tag{2.2}
\]

Put

\[
 \lambda=pD_0\in[0,D_0].                            \tag{2.3}
\]

Using (1.1)--(1.4), equation (2.2) is exactly (0.1).

The function \(\Phi_m\) is strictly convex on \([0,D_0)\). Indeed,

\[
 \Phi_m'(\lambda)
 =\alpha-\left(1-\frac\lambda{D_0}\right)^{D_0-1}
 -2\sum_{q=1}^H
  \left(1-\frac\lambda{D_0}\right)^{D_q-1},         \tag{2.4}
\]

and every term obtained by differentiating the negative powers in (2.4) is
positive. Since \(H\ge1\), \(H<h\),

\[
 \Phi_m'(0)=\alpha-(2H+1)<0,
 \qquad
 \lim_{\lambda\uparrow D_0}\Phi_m'(\lambda)=\alpha>0.
\]

Thus there is a unique optimizer \(\lambda_*\), characterized exactly by

\[
 \boxed{
 \left(1-\frac{\lambda_*}{D_0}\right)^{D_0-1}
 +2\sum_{q=1}^H
  \left(1-\frac{\lambda_*}{D_0}\right)^{D_q-1}
 =\alpha.}                                           \tag{2.5}
\]

## 3. A one-fold strip budget leaves \(\Theta(\sqrt m W)\) holes

Use the synthesis scales

\[
 H=\left\lceil\sqrt{m\log m}\right\rceil,
 \qquad
 h=2^{\lceil(3/4)\log_2m\rceil}.                    \tag{3.1}
\]

For every fixed \(x\ge0\), (1.3) gives

\[
 r_{\lfloor x\sqrt m\rfloor}\longrightarrow e^{-x^2}.
                                                               \tag{3.2}
\]

Also \(D_0\) grows faster than every power of \(m\). Consequently, if
\(\lambda\to\lambda_0\in(0,\infty)\),

\[
 \left(1-\frac\lambda{D_0}\right)^{D_q}
 =\exp\left(-\frac\lambda{r_q}+o(1)\right)           \tag{3.3}
\]

uniformly on every range \(q\le B\sqrt m\), with fixed \(B\).
The elementary bound

\[
 r_q\le \exp\left(-\frac{q^2}{m+q}\right)           \tag{3.4}
\]

supplies an integrable tail after (3.3). Since \(H/\sqrt m\to\infty\), a
Riemann sum gives

\[
 \frac1{\sqrt m}\left[
  r_0\left(1-\frac\lambda{D_0}\right)^{D_0}
  +2\sum_{q=1}^Hr_q
   \left(1-\frac\lambda{D_0}\right)^{D_q}
 \right]
 \longrightarrow
 2\int_0^\infty e^{-x^2-\lambda_0e^{x^2}}\,dx.       \tag{3.5}
\]

If the expected selected-block cost is \(W+o(W)\), then

\[
 \alpha\lambda W=W+o(W).
\]

Here \(\alpha\to1\), so \(\lambda\to1\). Equations (3.5) and (2.2)
prove (0.2). In particular, retaining only the middle layer gives the weaker
but sometimes useful bound

\[
 W(1-p)^{D_0}=(e^{-1}+o(1))W.                        \tag{3.6}
\]

The full Gaussian window strengthens (3.6) by a factor of order \(\sqrt m\).

## 4. Optimizing the uniform sampling rate

The optimizer lies at logarithmic load. The elementary expansion of (1.3),
uniformly for \(q=o(m^{2/3})\), is

\[
 \log r_q
 =-\frac{q^2}{m}
  +O\left(\frac{q^2}{m^2}+\frac{q^4}{m^3}\right).   \tag{4.1}
\]

For

\[
 \lambda=\frac12\log m+O(\log\log m),               \tag{4.2}
\]

the effective terms in (2.5) have
\(q=O(\sqrt{m/\lambda})\). On that scale, (4.1) and the fact that
\(D_0\) is superpolynomial give

\[
 \left(1-\frac\lambda{D_0}\right)^{D_q-1}
 =e^{-\lambda}e^{-\lambda q^2/m}(1+o(1)).            \tag{4.3}
\]

The estimate is uniform on a growing Gaussian core; (3.4) makes the
complement negligible. The standard integral comparison for the Gaussian
lattice sum gives

\[
 1+2\sum_{q=1}^H e^{-\lambda q^2/m}
 =\sqrt{\frac{\pi m}{\lambda}}\,(1+o(1)).            \tag{4.4}
\]

It follows from (2.5) that

\[
 e^{-\lambda_*}\sqrt{\frac{\pi m}{\lambda_*}}
 =\alpha(1+o(1)).                                    \tag{4.5}
\]

Equivalently,

\[
 \lambda_*+\frac12\log\lambda_*
 =\frac12\log(\pi m)-\log\alpha+o(1).              \tag{4.6}
\]

Solving (4.6) yields the slightly more general form

\[
 \lambda_*
 =\frac12\log m-\frac12\log\log m
  +\frac12\log(2\pi)-\log\alpha+o(1).              \tag{4.7}
\]

For (3.1), \(\log\alpha=o(1)\), proving (0.3).

At the same Gaussian scale, \(r_q=1+O(1/\lambda_*)\) in weighted average.
Therefore (2.5) implies that the normalized expected singleton leave at the
optimum is

\[
 \left(1-\frac{\lambda_*}{D_0}\right)^{D_0}
 +2\sum_{q=1}^Hr_q
  \left(1-\frac{\lambda_*}{D_0}\right)^{D_q}
 =\alpha+o(1).                                       \tag{4.8}
\]

Moreover

\[
 (\alpha-1)\lambda_*
 =O\left(m^{-1/4}(\log m)^{3/2}\right)=o(1).         \tag{4.9}
\]

Combining (4.7)--(4.9) proves (0.4).

## 5. Poisson, mixtures, and fixed-size sampling

### 5.1 Arbitrary nonuniform Poisson intensities

Give cycle \(C\) an independent Poisson multiplicity of mean \(\mu_C\), and
charge every occurrence. Put

\[
 \lambda=\frac{2h}{W}\sum_C\mu_C.                  \tag{5.1}
\]

For a target \(S\), its hole probability is

\[
 \exp\left(-\sum_{C\ni S}\mu_C\right).             \tag{5.2}
\]

On either signed depth-\(q\) layer, the average of the exponent load is

\[
 \frac1{N_q}\sum_S\sum_{C\ni S}\mu_C
 =\frac{2h\sum_C\mu_C}{N_q}
 =\frac\lambda{r_q}.                                 \tag{5.3}
\]

Convexity of \(e^{-x}\) and Jensen's inequality show that the expected
number of holes in that layer is at least

\[
 N_qe^{-\lambda/r_q}.                                \tag{5.4}
\]

Equality holds for uniform intensity. Thus, among all independent Poisson
schemes with a fixed total intensity, the uniform scheme is optimal. Its
normalized objective is exactly

\[
 \alpha\lambda+e^{-\lambda}
 +2\sum_{q=1}^Hr_qe^{-\lambda/r_q}.                  \tag{5.5}
\]

Equations (0.2)--(0.4) apply to (5.5), with no Bernoulli error. If repeated
copies are collapsed and only distinct cycles are charged, the presence
probabilities are \(p_C=1-e^{-\mu_C}\), so the model is simply nonuniform
Bernoulli selection instead.

### 5.2 Mixtures of uniform Bernoulli rates

Let \(P\) be random and, conditional on \(P=p\), select all cycles
independently at the common rate \(p\). For every integer \(D\ge2\), the
function \(p\mapsto(1-p)^D\) is convex. Hence

\[
 \mathbb E(1-P)^{D_q}
 \ge (1-\mathbb EP)^{D_q}.                           \tag{5.6}
\]

The selected-block cost is linear in \(P\). Thus mixing the global sampling
rate never improves on the deterministic rate \(p=\mathbb EP\).

### 5.3 Uniform sampling without replacement

Select exactly \(k\) distinct cycles uniformly from the \(M\) catalogue
cycles. The exact hole probability of a depth-\(q\) target is

\[
 u_{q,k}
 =\frac{\binom{M-D_q}{k}}{\binom Mk},                \tag{5.7}
\]

with the numerator interpreted as zero if \(k>M-D_q\). Put

\[
 \lambda=\frac{kD_0}{M}=\frac{2hk}{W}.              \tag{5.8}
\]

For \(\lambda=O(\log m)\), catalogue sparsity gives, uniformly on every
rank range contributing non-negligibly to the sum,

\[
 u_{q,k}=\exp\left(-\frac\lambda{r_q}+o(1)\right).   \tag{5.9}
\]

Indeed, \(k/M=\lambda/D_0=o(1)\) and
\(D_q/M=2h/N_q=o(1)\), while the quadratic errors in the logarithm of
(5.7) are negligible. Therefore fixed-size sampling has the same
one-fold-budget loss (0.2) and the same optimized loss (0.4). Merely fixing
the total number of cycles does not create the owner-level dependence that
SCI needs.

## 6. A no-go for diffuse nonuniform Bernoulli selection

Let the cycle indicators be independent with arbitrary probabilities
\(p_C\), but assume

\[
 0\le p_C\le\delta<1\quad(C\in\mathscr C).           \tag{6.1}
\]

Define the normalized expected middle incidence

\[
 \lambda=\frac{2h}{W}\sum_Cp_C.                    \tag{6.2}
\]

For a target \(S\), put \(a_S=\sum_{C\ni S}p_C\). Since

\[
 \log(1-x)\ge-\frac{x}{1-\delta}
 \qquad(0\le x\le\delta),                           \tag{6.3}
\]

its hole probability obeys

\[
 \prod_{C\ni S}(1-p_C)
 \ge\exp\left(-\frac{a_S}{1-\delta}\right).         \tag{6.4}
\]

The average of \(a_S\) on a signed depth-\(q\) layer is \(\lambda/r_q\).
Applying Jensen to (6.4) gives the exact lower bound

\[
 \boxed{
 \frac{\mathbb E[\text{cost}]}W
 \ge\alpha\lambda+
 e^{-\lambda/(1-\delta)}
 +2\sum_{q=1}^Hr_q
   e^{-\lambda/((1-\delta)r_q)}.}                   \tag{6.5}
\]

Fix \(\varepsilon>0\) and suppose \(\delta\le1-\varepsilon\). Put
\(t=\lambda/(1-\delta)\) and

\[
 a=\alpha(1-\delta)\ge\alpha\varepsilon.           \tag{6.6}
\]

The right side of (6.5) becomes

\[
 at+e^{-t}+2\sum_{q=1}^Hr_qe^{-t/r_q}.              \tag{6.7}
\]

The same Laplace calculation as in Section 4, now with the stationarity
condition

\[
 e^{-t}\sqrt{\frac{\pi m}{t}}=a(1+o(1)),            \tag{6.8}
\]

shows, uniformly when \(\varepsilon\) is fixed, that the minimum of (6.7)
is

\[
 a\left[
  \frac12\log m-\frac12\log\log m
  +\frac12\log(2\pi)-\log a+1
 \right]+o(1).                                      \tag{6.9}
\]

This proves (0.5), with leading constant at least
\(\varepsilon/2+o(1)\).

In particular, a sequence of diffuse independent schemes with
\(\max_Cp_C=o(1)\) has the same leading
\((\tfrac12+o(1))W\log m\) barrier as uniform independent sampling.
Conversely, (6.5) cannot obstruct probabilities tending to one. This is
unavoidable: allowing \(p_C\in\{0,1\}\) includes every deterministic
integer strip family, and proving an \(\Omega(W)\) loss for all such choices
would disprove SCI itself.

### 6.1 Stability: every successful product measure has an integral backbone

There is a precise converse to the diffuse no-go. Suppose an arbitrary
Bernoulli product measure, followed by singleton repair, has

\[
 \mathbb E[\text{cost}]=W+o(W).                      \tag{6.10}
\]

Let \(U_q\) denote its expected number of holes in one signed depth-\(q\)
layer, and retain \(\lambda\) from (6.2). The union bound at each target,
summed over a rank, gives

\[
 U_0\ge W(1-\lambda)_+,
 \qquad
 U_q\ge W(r_q-\lambda)_+.                           \tag{6.11}
\]

The block cost is \(\alpha\lambda W\). From (6.10), (6.11), and the two
signed depth-one layers, one obtains

\[
 \lambda=1+o(1),
 \qquad
 \sum_{q=-H}^H U_{|q|}=o(W).                         \tag{6.12}
\]

Indeed, the block-cost bound gives \(\limsup\lambda\le1\). If
\(\lambda\le1-\epsilon\) along a subsequence, then \(r_1\to1\), and the
block, middle-hole, and two depth-one-hole terms in (6.11) sum to at least
\((1+2\epsilon-o(1))W\), contradicting (6.10). Thus \(\lambda\to1\), the
block cost itself is \(W+o(W)\), and all singleton costs together are
\(o(W)\).

For a middle target \(X\), define

\[
 a_X=\sum_{C\ni X}p_C,qquad
 u_X=\prod_{C\ni X}(1-p_C),qquad
 w_X=a_X-(1-u_X)\ge0.                                \tag{6.13}
\]

Here \(w_X\) is the expected repeated-incidence waste at \(X\). Equations
(6.12)--(6.13) give

\[
 \sum_Xu_X=o(W),qquad
 \sum_Xw_X
 =\lambda W-W+\sum_Xu_X=o(W).                       \tag{6.14}
\]

There is a sequence \(\eta_m\downarrow0\) such that the deterministic
high-probability backbone

\[
 \mathcal F_m=\{C:p_C\ge1-\eta_m\}                  \tag{6.15}
\]

has all of the following properties:

\[
 \left|\binom\Omega m\setminus
       \bigcup_{C\in\mathcal F_m}M(C)\right|=o(W),   \tag{6.16}
\]

\[
 \left|\left\{X:
  |\{C\in\mathcal F_m:X\in M(C)\}|\ge2\right\}
 \right|=o(W),                                      \tag{6.17}
\]

\[
 |\mathcal F_m|=(1+o(1))\frac{W}{2h},               \tag{6.18}
\]

and

\[
 \frac{2h}{W}\sum_{C\notin\mathcal F_m}p_C=o(1).   \tag{6.19}
\]

To prove this, first fix \(0<\eta<1/4\). If no cycle through \(X\) has
probability at least \(1-\eta\), then one of the following holds:

* \(a_X\le1-\eta/2\), in which case \(u_X\ge1-a_X\ge\eta/2\);
* \(a_X\ge1+\eta/2\), in which case \(w_X\ge\eta/2\); or
* \(|a_X-1|<\eta/2\), in which case (6.3), with
  \(\delta=1-\eta\), gives
  \(u_X\ge\exp[-(1+\eta/2)/\eta]\).

Thus the number of middle targets missed by the fixed-\(\eta\) backbone is
at most

\[
 \frac{\sum_X(u_X+w_X)}
 {\min\{\eta/2,\exp[-(1+\eta/2)/\eta]\}}=o(W).       \tag{6.20}
\]

If two backbone cycles pass through \(X\), then
\(w_X\ge1-2\eta\ge1/2\), proving (6.17) for fixed \(\eta\). A diagonal
choice \(\eta=\eta_m\downarrow0\), slow enough that the right side of
(6.20) remains \(o(W)\), proves (6.16)--(6.17). The union bound
\(2h|\mathcal F_m|\ge W-o(W)\), together with

\[
 (1-\eta_m)|\mathcal F_m|
 \le\sum_Cp_C=(1+o(1))\frac{W}{2h},
\]

proves (6.18), and the same inequalities prove (6.19).

This stability theorem does not itself prove SCI. At each fixed signed rank,
if \(B_q\) is the number of targets missed by \(\mathcal F_m\), then union
bounding the residual low-probability cycles gives

\[
 B_q\le U_q+2h\sum_{C\notin\mathcal F_m}p_C=o(W).    \tag{6.21}
\]

But summing (6.21) over \(2H+1\) ranks loses a factor \(H\); (6.19) gives
only \(o(1)\), not \(o(1/H)\), normalized residual mass. Thus a hypothetical
successful product measure necessarily consists of an almost integral
middle near-factor plus a vanishing-cost residual whose shadows perform the
remaining all-depth repair. Constructing or excluding precisely that
residual is still an SCI-level problem.

## 7. Why general dependence is genuinely different

Let \(\mathcal F\) be an integral owner-disjoint middle near-factor with
middle leave \(L=o(W)\), and choose a uniformly random coordinate conjugate
of \(\mathcal F\). The resulting law is orbit-symmetric. Every catalogue
cycle has the same inclusion marginal

\[
 p=\frac{|\mathcal F|}{M}
 =\frac{W-L}{2hM}
 =\frac{1-L/W}{D_0}.                                 \tag{7.1}
\]

Thus its normalized marginal load is \(pD_0=1-L/W\), the same one-fold load
at which independent sampling leaves approximately \(e^{-1}W\) middle
targets. Nevertheless the conjugated near-factor leaves exactly \(L=o(W)\)
middle targets in every outcome. For the explicit fixed-pair Stage-A family,
\(L/W\) is exponentially small.

Therefore no lower bound based only on orbit-symmetric one-cycle marginals
can prove a loss. The necessary distinction is local correlation: the
near-factor suppresses repeated ownership and forces almost one selected
cycle at every middle target. Whether one can preserve enough of this
correlation while dispersing all signed shadows is precisely the remaining
integral issue.

## 8. Exact fractional optimum and the failure of rank-only obstructions

The fractional optimum in the synthesis admits an exact evaluation. Average
any fractional solution over coordinate permutations. The cycle variable
becomes a common value \(x\). Put \(\lambda=D_0x\). Minimal singleton values
at the middle and at signed depth \(q\) are respectively

\[
 (1-\lambda)_+,
 \qquad
 \left(1-\frac\lambda{r_q}\right)_+.
\]

Hence the normalized fractional objective is

\[
 g(\lambda)
 =\alpha\lambda+(1-\lambda)_+
  +2\sum_{q=1}^H(r_q-\lambda)_+.                    \tag{8.1}
\]

On \([r_1,1]\),

\[
 g(\lambda)=1+(\alpha-1)\lambda
\]

is increasing. Below \(r_1\), at least the two signed depth-one terms are
active, and every linear piece has slope at most

\[
 \alpha-1-2<0.
\]

Above \(1\), \(g(\lambda)=\alpha\lambda\) initially and cannot improve the
value at \(r_1\). Thus the unique minimizer is

\[
 \lambda=r_1=\frac m{m+1}.                           \tag{8.2}
\]

This proves (0.6). An explicit primal optimum is

\[
 x_C=\frac1{D_1}\quad(C\in\mathscr C),
 \qquad
 z_X=\frac1{m+1}\quad\left(X\in\binom\Omega m\right),
\]

with every nonmiddle singleton variable zero. An explicit dual optimum puts
weight \(1\) on every middle target, weight \(H/(2h)\) on every target in
each of the two signed depth-one layers, and weight zero elsewhere. Every
cycle constraint is tight because

\[
 2h+2(2h)\frac{H}{2h}=2h+2H.                        \tag{8.3}
\]

For completeness, suppose an integral family contains \(n\) cycles. At any
one signed rank it covers at most \(2hn\) distinct targets. Therefore every
integral solution obeys the rank-cardinality lower bound

\[
 \tau_{m,H,h}\ge
 \min_{n\in\mathbb Z_{\ge0}}
 \left[
  (2h+2H)n+(W-2hn)_+
  +2\sum_{q=1}^H(N_q-2hn)_+
 \right].                                           \tag{8.4}
\]

After setting \(\lambda=2hn/W\), the bracket divided by \(W\) is exactly
\(g(\lambda)\) on a grid of mesh \(2h/W\). Its minimum differs from
\(\tau^*\) by at most \(O(Hh)=o(W)\). Thus every obstruction using only the
number of selected cycles and the cardinality of each rank is asymptotically
incapable of separating \(\tau\) from \(\tau^*\) by \(\Omega(W)\).

## 9. Random-alteration boundary

The following statements are proved here.

1. Uniform independent Bernoulli selection, arbitrary nonuniform charged
   Poisson selection, mixtures of uniform Bernoulli rates, and uniform
   fixed-size sampling all fail SCI quantitatively.
2. Every Bernoulli product measure bounded a fixed distance below
   deterministic columns has an \(\Omega(W\log m)\) optimized alteration
   cost.
3. Orbit symmetry by itself gives no obstruction: structured dependent
   middle near-factors defeat the middle-layer loss at the same marginals.
4. The ordinary cover LP has the exact value (0.6), and rank-only counting
   cannot prove an additive \(\Omega(W)\) integer gap.

What remains unproved is whether a highly correlated whole-strip selection,
with owner recycling permitted and literal singleton alteration, can attain
\(\tau=\tau^*+o(W)\). The random-selection calculations do not supply an
integrality-gap obstruction. They show instead that any positive SCI proof
must use near-deterministic local exclusion/reconfiguration, not diffuse
rounding.

## 10. Exact dual and complementary slackness

For clarity, the fractional primal is

\[
 \min\quad
 (2h+2H)\sum_Cx_C+\sum_{S\in\mathcal B_{m,H}}z_S
 \tag{10.1}
\]

subject to

\[
 z_S+\sum_{C:S\in\mathcal T_H(C)}x_C\ge1,
 \qquad x_C,z_S\ge0.                                \tag{10.2}
\]

### Theorem 10.1 (exact SCI dual)

The dual is

\[
 \max\sum_{S\in\mathcal B_{m,H}}y_S                 \tag{10.3}
\]

subject to

\[
 \sum_{S\in\mathcal T_H(C)}y_S\le2h+2H
 \quad(C\in\mathscr C_{m,h}),                       \tag{10.4}
\]

\[
 0\le y_S\le1
 \quad(S\in\mathcal B_{m,H}).                       \tag{10.5}
\]

The upper bound in (10.5) is exactly the constraint supplied by the
singleton-repair column \(z_S\).

Every dual optimum may be averaged over the full coordinate group without
changing feasibility or objective. Hence an optimum exists with values
\(a_0\) on the middle layer and \(a_q^-,a_q^+\) on the signed
depth-\(q\) layers. All strip constraints then become

\[
 a_0+\sum_{q=1}^H(a_q^-+a_q^+)
 \le1+\frac Hh,                                     \tag{10.6}
\]

and the objective becomes

\[
 Wa_0+\sum_{q=1}^HN_q(a_q^-+a_q^+).                \tag{10.7}
\]

Since \(W>N_1>N_2>\cdots\) and \(0<H/h<1\), (10.6)--(10.7) are solved by

\[
 a_0=1,\qquad
 a_1^-+a_1^+=\frac Hh,\qquad
 a_q^\pm=0\quad(q\ge2).                             \tag{10.8}
\]

Thus (0.6) is the global dual optimum, not merely the invariant optimum.
The complement-symmetric choice is

\[
 a_1^-=a_1^+=\frac H{2h}.                           \tag{10.9}
\]

The primal solution from Section 8 and the dual solution (10.8) satisfy
complementary slackness exactly:

1. every positive strip variable meets a tight strip constraint;
2. every positive middle repair meets \(y_X=1\);
3. the middle and signed depth-one coverage rows are tight; and
4. all deeper coverage rows are slack and carry zero dual weight.

Consequently no nonsymmetric weighted dual can improve (0.6).

## 11. Exact integer collision decomposition

Let \(\mathcal F\) be any integral family of \(n\) strips and put

\[
 I=2hn.                                              \tag{11.1}
\]

Every signed rank receives exactly \(I\) target incidences. For
\(d\in[-H,H]\), let \(\ell_d(T)\) be the load of \(T\in\binom\Omega{m+d}\),
and put

\[
 U_d=|\{T:\ell_d(T)>0\}|,\qquad
 E_d=\min(I,N_{|d|})-U_d.                            \tag{11.2}
\]

### Lemma 11.1 (fine-defect identity)

The minimum block-plus-singleton cost obtained from \(\mathcal F\) by
repairing exactly its holes is

\[
 \boxed{
 F(I)+\sum_{d=-H}^{H}E_d,}                           \tag{11.3}
\]

where

\[
 F(I)=\left(1+\frac Hh\right)I
 +(W-I)_+
 +2\sum_{q=1}^H(N_q-I)_+.                           \tag{11.4}
\]

Indeed,

\[
 N_{|d|}-U_d=(N_{|d|}-I)_++E_d.                    \tag{11.5}
\]

The continuous minimum of \(F\) is attained uniquely at \(I=N_1\) and is
equal to \(\tau^*\). Restricting \(I\) to \(2h\mathbb Z\) changes the
minimum by at most

\[
 O(Hh)=o(W),                                        \tag{11.6}
\]

because the grid mesh is \(2h\) and every slope has magnitude at most
\(2H+2\).

Thus all unresolved integrality lies in

\[
 \sum_dE_d.                                         \tag{11.7}
\]

In particular, no obstruction using only the number of selected strips and
the cardinalities of the signed ranks can give an additive
\(\Omega(W)\) gap.

There is an equivalent overload identity. If

\[
 O_d=\sum_T(\ell_d(T)-1)_+,\qquad
 H_d=N_{|d|}-U_d,
\]

then

\[
 \boxed{O_d-H_d=I-N_{|d|}.}                         \tag{11.8}
\]

Formally evaluating the rank envelope at \(I=W\), holes are exactly overload
above the unavoidable baseline \(W-N_{|d|}\), and

\[
 F(W)-\tau^*=\frac Hh(W-N_1)=o(W),                  \tag{11.9}
\]

In general \(2h\nmid W\), so an actual family need not have \(I=W\). Instead
put

\[
 I_+=2h\left\lceil\frac W{2h}\right\rceil=W+O(h).
 \tag{11.10}
\]

The slope bound used in (11.6) gives

\[
 F(I_+)-\tau^*=o(W).                                \tag{11.11}
\]

Thus a family with incidence total \(I_+\) is fully compatible with SCI if
its aggregate fine defect (11.7) is \(o(W)\).

## 12. Exact strip-pair codegrees

Let

\[
 V_d=\binom{\Omega}{m+d},\qquad |d|\le H,
\]

and let \(\lambda(S,T)\) be the number of strips containing two distinct
targets \(S\in V_d,T\in V_e\). In this section put

\[
 D_d:=D_{|d|}
 =\frac{(m+d)!(m-d)!}{2(m-h)!^2}.                   \tag{12.0}
\]

Also put

\[
 p=|S\cap T|-(m-h),                                  \tag{12.1}
\]

\[
 u=h+d-p=|S\setminus T|,\qquad
 v=h+e-p=|T\setminus S|,                             \tag{12.2}
\]

\[
 L_{d,e}=\max(0,d+e),\qquad
 U_{d,e}=h+\min(d,e),                                \tag{12.3}
\]

and

\[
 n_{d,e}(p)=
 \begin{cases}
  |d-e|+1,&p=U_{d,e},\\
  |d+e|+1,&p=L_{d,e},\\
  2,&L_{d,e}<p<U_{d,e},\\
  0,&\text{otherwise}.
 \end{cases}                                        \tag{12.4}
\]

### Theorem 12.1 (exact pair-codegree formula)

One has \(\lambda(S,T)>0\) if and only if

\[
 L_{d,e}\le p\le U_{d,e}.                            \tag{12.5}
\]

In that range,

\[
 \boxed{
 \lambda(S,T)
 =D_d\,
 \frac{n_{d,e}(p)}
 {\binom{m+d}{u}\binom{m-d}{v}}.}                   \tag{12.6}
\]

Equivalently,

\[
 \lambda(S,T)=
 \frac{
 n_{d,e}(p)u!v!(m-h+p)!(m-h+p-d-e)!
 }{2(m-h)!^2}.                                      \tag{12.7}
\]

#### Proof

Fix \(S\). In every incident strip, \(S\setminus K\) is a circular interval
of length \(h+d\) in a \(2h\)-cycle. A rank-\(m+e\) target is an interval of
length \(h+e\). The overlap of two such circular intervals ranges from
\(\max(0,d+e)\) to \(h+\min(d,e)\). The shorter interval has
\(|d-e|+1\) contained phases at maximum overlap; there are
\(|d+e|+1\) minimum-overlap phases; and every interior overlap has two
phases.

For fixed \(S\), the number of rank-\(m+e\) targets with difference
parameters \(u,v\) is

\[
 \binom{m+d}{u}\binom{m-d}{v}.
\]

The stabilizer of \(S\) is transitive on them. Double counting their
incidences with the \(D_d\) strips through \(S\) proves (12.6), and (12.7)
follows from the degree formula. \(\square\)

For \(S,T\in V_d\), put \(\delta=|S\setminus T|\). Then

\[
 \frac{\lambda(S,T)}{D_d}
 =
 \begin{cases}
 \displaystyle
 \frac2{\binom{m+d}{\delta}\binom{m-d}{\delta}},
 &1\le\delta<h-|d|,\\[3mm]
 \displaystyle
 \frac{2|d|+1}
 {\binom{m+d}{h-|d|}\binom{m-d}{h-|d|}},
 &\delta=h-|d|.
 \end{cases}                                        \tag{12.8}
\]

In particular,

\[
 \max_{\substack{S\ne T\\S,T\in V_0}}
 \frac{\lambda(S,T)}{D_0}=\frac2{m^2}.              \tag{12.9}
\]

If \(d<e\), \(r=e-d\), and \(S\subset T\), then

\[
 \frac{\lambda(S,T)}{D_d}
 =\frac{r+1}{\binom{m-d}{r}},\qquad
 \frac{\lambda(S,T)}{D_e}
 =\frac{r+1}{\binom{m+e}{r}}.                       \tag{12.10}
\]

Thus adjacent nested ranks have normalized codegree \(2/(m-d)\).

### Corollary 12.2 (sharp band maximum)

For \(H=o(m)\),

\[
 \boxed{
 \max_{S\ne T}
 \frac{\lambda(S,T)}
 {\min(\deg S,\deg T)}
 =\frac2{m-H+1}.}                                   \tag{12.11}
\]

The maximum is attained by adjacent nested targets in ranks \(H-1,H\), and
symmetrically in ranks \(-H,-H+1\). Nonnested pairs satisfy

\[
 \frac{\lambda(S,T)}
 {\min(\deg S,\deg T)}
 \le\frac{2H+1}{m^2-H^2}.                           \tag{12.12}
\]

This follows directly from (12.6): for a nested gap \(r\), the normalized
quantity is at most

\[
 \frac{r+1}{\binom{m-H+r}{r}},
\]

which decreases from \(2/(m-H+1)\); for a nonnested pair, both binomial
factors in (12.6) are nontrivial and their product is at least
\(m^2-H^2\).

There is also an exact adjacent-rank chronology identity:

\[
 \sum_{\substack{T\in V_{d+1}\\S\subset T}}
 \frac{\lambda(S,T)}{D_d}=2.                        \tag{12.13}
\]

Every occurrence of \(S\) in a strip has exactly two containing targets in
the next rank. This two-endpoint coupling is invisible to separate
rankwise rounding.

## 13. Corrected cutoff and generic-nibble obstructions

The degree ratio has the expansion

\[
 \log(D_q/D_0)=q^2/m+o(1)                           \tag{13.1}
\]

uniformly for \(q=O(\sqrt{m\log m})\).

At the original cutoff \(H^2/m=\log m+o(1)\),

\[
 D_H=(1+o(1))mD_0,
\]

and an adjacent nested pair in ranks \(H-1,H\) has codegree

\[
 \frac{2D_{H-1}}{m-H+1}=(2+o(1))D_0.                \tag{13.2}
\]

Thus a full-band assumption \(\Delta_2=o(D_{\min})\) fails.

### Proposition 13.1 (parameter repair)

Fix \(\beta\in(1/2,1)\), and set

\[
 H=\left\lceil\sqrt{\beta m\log m}\right\rceil.      \tag{13.3}
\]

Then

\[
 R_{m,H}/W=O(m^{1/2-\beta})=o(1),                   \tag{13.4}
\]

\[
 D_H/D_0=(1+o(1))m^\beta,                           \tag{13.5}
\]

\[
 \Delta_2/D_0=(2+o(1))m^{\beta-1}=o(1).             \tag{13.6}
\]

#### Proof

Hoeffding gives \(R_{m,H}\le2\,4^me^{-H^2/m}\), while
\(W=\Theta(4^m/\sqrt m)\), proving (13.4). Equation (13.1) proves
(13.5), and (13.2) supplies the lower bound in (13.6). For the matching
upper bound, Corollary 12.2 gives

\[
 \frac{2D_{H-1}}{m-H+1}
 \le\Delta_2
 \le\frac{2D_H}{m-H+1}.                             \tag{13.6a}
\]

Since \(D_{H-1}/D_H=1+o(1)\), this proves (13.6). More explicitly,
gap-one nested pairs are maximized in ranks \(H-1,H\); nested gaps
\(r\ge2\) have codegree at most

\[
 D_H\,\frac3{\binom{m-H+2}{2}}
 =o(m^{\beta-1}D_0),
\]

while nonnested pairs have codegree at most

\[
 D_H\,\frac{2H+1}{m^2-H^2}
 =o(m^{\beta-1}D_0).
\]

Thus the adjacent nested pair supplies the global asymptotic maximum, proving
(13.6). \(\square\)

The correction preserves every compiler estimate and every random-alteration
asymptotic, because \(H/\sqrt m\to\infty\), \(H=o(m^{2/3})\), and the same
dyadic \(h=m^{3/4+o(1)}\) has \(H/h=o(1)\).

Pair codegrees are nevertheless insufficient. The whole strip edge has

\[
 R_{\rm edge}=2h(2H+1)                              \tag{13.7}
\]

vertices. From (12.11),

\[
 R_{\rm edge}
 \max_{S\ne T}\frac{\lambda(S,T)}
 {\min(\deg S,\deg T)}
 \asymp\frac{hH}{m}.                                \tag{13.8}
\]

Whenever the Boolean tail is \(o(W)\) and \(h/H\to\infty\), the right side
of (13.8) diverges. Thus even a growing-rank criterion requiring edge rank
times normalized pair codegree to vanish would not apply.

There is a higher-codegree obstruction as well. Fix
\(1\le s\le H\) and one strip phase \(t\). For \(0\le a,b\le s\), put

\[
 G_{a,b}=K\cup I_z(t+a,h+b-a).                      \tag{13.9}
\]

These \((s+1)^2\) distinct sets all belong to the strip column, at signed
depth \(b-a\). Let \(J_s\) be their family.

### Proposition 13.2 (crossing-grid codegree)

\[
 \lambda(J_s)\ge
 \frac{(m-s)_{\underline{h-s}}^2}{4h}.              \tag{13.10}
\]

Consequently

\[
 \frac{D_H}{\lambda(J_s)}
 \le2h\,\frac{D_H}{D_0}(m)_{\underline s}^{\,2}.    \tag{13.11}
\]

For \(s=\lceil\log m\rceil\),

\[
 \boxed{
 \left(\frac{D_H}{\lambda(J_s)}\right)^{
 1/((s+1)^2-1)}
 \le e^{2+o(1)}.}                                   \tag{13.12}
\]

#### Proof

The grid differences reveal \(s\) ordered active coordinates at each end.
Its smallest set has size \(m-s\) and its largest has size \(m+s\). Choose
and order the remaining \(h-s\) active coordinates inside the smallest set,
and independently choose and order the remaining \(h-s\) active coordinates
outside the largest set. This gives
\((m-s)_{\underline{h-s}}^2\) oriented extensions. One unoriented strip has
at most \(4h\) phase/orientation descriptions, proving (13.10).

Finally,

\[
 D_0=\frac{(m)_{\underline h}^{\,2}}2,\qquad
 \frac{(m)_{\underline h}}
 {(m-s)_{\underline{h-s}}}=(m)_{\underline s},
\]

which proves (13.11). For \(s=\lceil\log m\rceil\), the logarithm of its
right side is \(2s\log m+O(\log m)\), while
\((s+1)^2-1=s^2+2s\), proving (13.12). \(\square\)

Thus the usual full-codegree roots do not diverge. This does not prove an
integral gap—the grids are highly structured pieces of the desired
chronology—but it blocks a generic growing-rank full-codegree black box.

## 14. Why an ordinary matching theorem is the wrong target

Every strip contains \(2h\) targets in the smallest outer layer \(V_H\).
A matching in the full band hypergraph has at most

\[
 N_H/(2h)
\]

edges and therefore covers at most \(N_H=o(W)\) middle targets. SCI needs
about \(W/(2h)\) strips and necessarily permits multiplicity in the smaller
layers.

The object is capacity-regular rather than degree-regular. At the formal
one-fold incidence total \(W\), every layer has desired mean load

\[
 \mu_d=W/N_{|d|},
\]

and

\[
 D_d/\mu_d=D_0                                      \tag{14.1}
\]

is exactly constant. At rank one,

\[
 \mu_1=(m+1)/m,
\]

so an exact floor/ceiling quota vector of total \(W\) has quota two on
exactly

\[
 W-N_1=W/(m+1)
\]

targets and quota one on every other target. The same whole strips must
realize these quotas at every rank and around both adjacent-rank endpoints.

For one rank alone, the incidence hypergraph is regular and its same-rank
codegrees are small. In the middle projection,

\[
 \Delta_2/D_0=2/m^2,\qquad
 (2h)^2\Delta_2/D_0=o(1)
\]

for \(h=m^{3/4+o(1)}\). A middle-only near-matching is plausible and is
already supplied explicitly by Stage A. Separate rankwise nibbles, however,
choose different strip families and cannot be intersected after the fact.

The rigorous conclusion is therefore:

\[
 \boxed{\text{ordinary matching nibble, independent-cover alteration, and
 pair-codegree-only covering do not presently compose to SCI.}}   \tag{14.2}
\]

This is a statement about the verified hypotheses and exact losses above. It
does not assert that every orbit-specific, strongly dependent Rödl-style
capacity process must fail.

## 15. A precise sufficient successor

Let \(I\) be the least multiple of \(2h\) which is not smaller than \(W\).
Then

\[
 I=W+O(h)=W+o(W).                                   \tag{15.0}
\]

For each signed rank \(d\), choose
integer quotas

\[
 b_d(T)\in
 \left\{\left\lfloor I/N_{|d|}\right\rfloor,
       \left\lceil I/N_{|d|}\right\rceil\right\},
\qquad
 \sum_{T\in V_d}b_d(T)=I.                           \tag{15.1}
\]

All quotas are at least one.

### Proposition 15.1 (capacity-nibble sufficient condition)

If there is a family \(\mathcal F\) of \(I/(2h)\) whole strips such that

\[
 \sum_{d=-H}^{H}\sum_{T\in V_d}
 |\ell_d(T)-b_d(T)|=o(W),                            \tag{15.2}
\]

then SCI holds.

#### Proof

Every hole has load zero and quota at least one, so the total holes are at
most the left side of (15.2). The block cost is

\[
 (1+H/h)I=W+o(W).
\]

Singleton alteration gives an integral solution of cost \(W+o(W)\). Since
\(\tau^*=W+o(W)\), its additive integrality gap is \(o(W)\). \(\square\)

Condition (15.2) is stronger than SCI, but it is one precise sufficient
aggregate target for a capacity-respecting nibble. Such a theorem would have
to preserve simultaneously:

1. lower quota one at every labelled target;
2. floor/ceiling overload dictated by \(I/N_d\);
3. both signs and all depths;
4. the two-endpoint chronology (12.13);
5. one common cyclic strip choice; and
6. aggregate \(o(W)\) error, not merely rankwise \(o(W)\).

The corrected cutoff (13.3) removes the avoidable absolute pair-codegree
failure. The crossing grids and growing edge rank show why an orbit-specific
capacity process, rather than a generic matching theorem, is still required.

## 16. Final proved/conditional boundary

### Proved

1. The exact dual is (10.3)--(10.5), and its optimum is (0.6).
2. The exact integer collision defect is (11.3).
3. Diffuse independent alteration has the losses in Sections 3--6.
4. The exact pair codegrees are (12.6)--(12.7).
5. The original cutoff has \(\Delta_2=(2+o(1))D_0\).
6. The corrected cutoff
   \(H^2/m=\beta\log m\), \(1/2<\beta<1\), keeps the Boolean tail
   \(o(W)\) and gives \(\Delta_2=o(D_0)\).
7. The crossing grids have bounded full-codegree roots.
8. Rank-only lower bounds differ from \(\tau^*\) by only \(o(W)\), so no
   ordinary weighted dual or layer-cardinality cut gives an
   \(\Omega(W)\) integrality gap.

### Unproved

1. SCI.
2. A genuine labelled cross-rank integrality-gap obstruction.
3. A chronology-preserving capacity process satisfying (15.2).
4. A lift from separate rankwise Hall/TU solutions to one strip family.

The attack therefore closes the diffuse alteration schemes and the standard
matching/codegree criteria tested here, sharpens the fractional optimum
exactly, and singles out a viable probabilistic successor: a strongly
dependent, orbit-specific capacity process, preferably at the corrected cutoff
\(H^2/m=\beta\log m\) with \(1/2<\beta<1\).
