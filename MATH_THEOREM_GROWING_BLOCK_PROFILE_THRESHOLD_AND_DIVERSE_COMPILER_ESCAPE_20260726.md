# Growing block profiles: the sharp Hall threshold and the diverse-compiler scale

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Outcome

This note extends the full-block Farkas obstruction from fixed block size to
a block size \(b=b(m)\).  There are three different thresholds.

* **One-depth threshold.**  At one fixed Gaussian depth, the full-block
  obstruction has linear size if \(b=O(1)\), while every \(b\to\infty\)
  makes that one-depth deficit \(o(W)\).
* **All-depth coefficient-one threshold.**  Put
  \(\Lambda_b=2^b/b\).  The sum of the profile deficits through
  \(H=A\sqrt m\) is
  \[
       \left({2\over3\sqrt\pi}+o(1)\right)
       {W\sqrt m\over\Lambda_b^{3/2}}
  \]
  throughout the transition range.  Consequently the sharp escape from
  this dual simultaneously for all \(q\le H\) is
  \[
                         {2^b\over b}\gg m^{1/3}.
  \]
  Equivalently,
  \[
     b>{1\over3}\log_2m+\log_2\log_2m+\omega(1).
  \]
* **Existence threshold for a deficient profile.**  Put
  \(q=A\sqrt m+O(1)\), \(A>0\), and
  
  \[
                  \gamma_m={2^b\over\sqrt m}.
  \]
  
  If \(\gamma_m\to\gamma<2/A\), deficient full-block strata still exist,
  although their total mass is \(o(W)\) when \(b\to\infty\).  If
  \(\gamma_m\to\gamma>2/A\), every full-block stratum has at least as many
  middle owners as lower targets, so the profile dual is exactly empty for
  all sufficiently large (m).  The transition is therefore
  
  \[
          b={1\over2}\log _2m+\log _2(2/A)+O(1).
  \]

In the genuinely moderate regime \(b\to\infty\) and
\(2^b=o(\sqrt m)\), the complete depth-\(A\sqrt m\) profile deficit
\(\Delta_{m,b}(A)\)
satisfies the logarithmically sharp estimate

\[
 \boxed{
 {\Delta_{m,b}(A)\over \binom{2m}{m-q}}
 =\exp\left[-\left({A^2\over4}+o(1)\right){2^b\over b}\right]. }
\tag{0.1}
\]

Consequently a factor which is allowed to cross the prescribed blocks
must have at least \(\Delta_{m,b}(A)\) actual depth-\(q\) window
occurrences containing a cross-block move, up to the number of targets it
is willing to leave uncovered.  For fixed \(b\) this is
\(\Omega_{A,b}(W)\); for \(b\to\infty\) it is \(o(W)\) at that one
depth.  A cross transition belongs to at most \(q\) cyclic depth-\(q\)
windows, so the corresponding necessary transition count is at least
\(\Delta_{m,b}(A)/q\).

For the rank-twisted diverse compiler, (R\asymp\sqrt{mH}\asymp m^{3/4})
when (H=A\sqrt m), but (R) is **not** the block size seen by this dual.
The union of all rank-dependent physical frames inside one macroblock is
(K_{d,d}); its connected components are the macroblocks of size
(b=2d).  The compiler merely permutes the (R) abstract directions and
does not add physical edges between macroblocks.  Thus the correct
substitution is \(b=2d\), not \(b=R\).  The one-depth deficit is \(o(W)\)
as soon as \(d\to\infty\), but the all-depth sum is \(o(W)\) precisely
when
\[
                    {2^{2d}\over2d}\gg m^{1/3}.
\]
Thus it is enough that
\[
       d>{1\over6}\log_2m+{1\over2}\log_2\log_2m+\omega(1).
\]
The usual choice \(d=10\log_2m\) has enormous slack.  The old
bounded-quartet dual is paid by the fact that every selected axis crosses
the quartet refinement.

This removes only the full-block-profile obstruction.  It does not prove
the cross-packet Hall/covariance theorem: a selector localized in a carrier
of size (\Theta(R)) still has the independent capacity loss
(\exp(-\Theta(q^2/R))=\exp(-\Theta(m^{1/4}))).

## 1. Exact profile deficit

Assume first that (b\mid2m), put (n=2m/b), and partition the physical
coordinates into (n) labelled (b)-sets.  Let

\[
 h_b(z)=(1+z)^b-z^b.
\]

For (0\le r\le2m), let (A_{r,k}) be the number of rank-(r) sets
containing exactly (k) whole blocks.  Exactly

\[
 A_{r,k}=\binom nk[z^{r-bk}]h_b(z)^{n-k}.
\tag{1.1}
\]

At lower depth (q), write

\[
 X_k=A_{m,k},\qquad T_k=A_{m-q,k},\qquad
 N_q=\binom{2m}{m-q}.
\tag{1.2}
\]

The largest one-sided deficit which can be certified by a nonnegative
weight depending only on the full-block profile is

\[
 \Delta_{m,b}(A)=\sum_k(T_k-X_k)_+.
\tag{1.3}
\]

Indeed the maximizing (0/1) weight is the indicator of
(\{k:T_k>X_k\}).  If every physical move remains inside one block, a
lower target has the same full blocks as its middle owner, so (1.3) is an
exact Farkas deficit.  Complementation gives the identical empty-block
deficit on the upper side.

Blocks of unequal bounded remainder may be frozen.  All estimates below
are unchanged after multiplication by (1+o(1)), provided (b=o(m)).

## 2. Monotone likelihood ratio

The deficient profile set is always an initial interval.  This fact is
needed to turn one saddle calculation into a global statement.

### Lemma 2.1

For (r<s), the ratio

\[
                         {A_{s,k}\over A_{r,k}}
\tag{2.1}
\]

is nondecreasing in (k) wherever it is defined.

#### Proof

For one block, let (R) be its rank and (I={\bf1}_{\{R=b\}}).  Its
unnormalized array is

\[
 K(j,0)=\binom bj\quad(0\le j<b),\qquad
 K(b,1)=1,
\]

with all other entries zero.  Every ordered (2\times2) minor of (K)
is nonnegative: the only minor using the second column which can be
nonzero has lower row (b), and its determinant is (\binom bj\ge0).
Thus (K) is totally positive of order two.

Convolution of two TP2 arrays is TP2.  To see this directly, expand a
minor of the convolution and group the summands with the two first
coordinates in increasing order; each grouped term is a product of one
minor of the first array and one minor of the second.  Every such product
is nonnegative.  Induction therefore shows that the joint count array of

\[
             \left(\sum_{j=1}^nR_j,\sum_{j=1}^nI_j\right)
\]

is TP2.  This joint array is precisely (A_{r,k}).  Hence

\[
 A_{r,k}A_{s,k+1}\ge A_{r,k+1}A_{s,k},
\]

which is equivalent to (2.1). \(\square\)

In particular (X_k/T_k) is nondecreasing, and

\[
              \{k:T_k>X_k\}=\{0,1,\ldots,k_c\}
\tag{2.2}
\]

for some \(k_c\), with the convention that the set may be empty.

## 3. A triangular local limit ratio

Put (p=2^{-b}), and let (J) have the rank of a uniformly chosen proper
subset of one block:

\[
 \Pr(J=j)={\binom bj\over2^b-1},\qquad0\le j<b.
\]

Write

\[
 a_b=b-\mathbb EJ={b2^{b-1}\over2^b-1},\qquad
 v_b={2(1-p)\over b}\operatorname {Var}J.
\tag{3.1}
\]

Then

\[
                  a_b={b\over2}(1+o(1)),\qquad
                  v_b={1\over2}+o(1)
\tag{3.2}
\]

when (b\to\infty).

### Lemma 3.1 (uniform ratio)

Suppose (b=o(\sqrt m)).  Uniformly for (x) in a fixed compact set and
integers

\[
 k={m\over b2^{b-1}}+{x\sqrt m\over a_b}+O(1),
\tag{3.3}
\]

one has

\[
 \boxed{
 \log {X_k\over T_k}
 ={A^2+2Ax\over2v_b}+o(1). }
\tag{3.4}
\]

#### Proof

Put (d=n-k).  The common factor (\binom nk(2^b-1)^d) cancels from
(X_k/T_k).  Since

\[
 m-bk-(\mathbb EJ)d={m\over2^b-1}-a_bk,
\]

the source coefficient in (1.1) is at displacement
(-x\sqrt m+O(b)) from the mean of a sum of (d) copies of (J), and
the target coefficient is at displacement
(-(A+x)\sqrt m+O(b)).  Moreover

\[
        d\operatorname {Var}J=v_bm+O(\sqrt m+b^2)=v_bm(1+o(1)).
\]

The triangular lattice local limit theorem therefore gives the ratio of
the two Gaussian densities, which is (3.4).

For completeness, its uniformity here does not require a black-box
fixed-distribution hypothesis.  Put \(L_m=(m/b)^{1/12}\).  On
\(|t|\le L_m/\sqrt m\), Taylor's formula for
\(\log\mathbb Ee^{it(J-\mathbb EJ)}\) has total third-order
remainder

\[
 O\!\left(d\,\mathbb E|J-\mathbb EJ|^3|t|^3\right)
 =O((b/m)^{1/4})=o(1).
\]

On the complementary Fourier range, starting at \(L_m/\sqrt m\), use

\[
 \left|\mathbb Ee^{itJ}\right|
 \le{ |(1+e^{it})/2|^b+p\over1-p};
\]

the part away from multiples of \(2\pi\) is at most
\(\exp(-cmt^2)+\exp(-cdb)\) after raising to the power \(d\), and is
therefore \(o(m^{-1/2})\) after integration; the neighborhoods of the
multiples of \(2\pi\) reduce to the preceding Taylor estimate.  Fourier
inversion gives the relative local limit uniformly for displacements
\(O(\sqrt m)\). \(\square\)

The crossing point in (3.4) is

\[
                         x=-{A\over2}.
\tag{3.5}
\]

At (k=0), the corresponding value of (x) is exactly

\[
 x_0=-{\sqrt m\over2^b-1}=-{1+o(1)\over\gamma_m}.
\tag{3.6}
\]

Together with Lemma 2.1, equations (3.5)--(3.6) already prove the sharp
existence transition: if (\gamma_m\to\gamma>2/A), then
(X_0/T_0>1), hence (X_k\ge T_k) for every (k); if
(\gamma_m\to\gamma<2/A), then (X_0/T_0<1), so a deficient stratum
exists.

The assertion for \(\gamma>2/A\) covers the transition scale and every
\(b=o(\sqrt m)\) above it.  In the remaining range, where \(b\) is not
\(o(\sqrt m)\), the same conclusion follows without a local limit.  A
uniform middle set contains a prescribed \(b\)-block with probability

\[
 { (m)_b\over(2m)_b}\le2^{-b}.
\]

Thus, whenever (b\gg\log m), the probability that it contains any whole
block is at most ((2m/b)2^{-b}=o(1)).  Hence
(X_0=(1-o(1))W>N_q\ge T_0); Lemma 2.1 again gives (X_k\ge T_k) for all
(k).  The two arguments overlap, so there is no uncovered range of
(b=o(m)).

## 4. Size of the surviving deficit

We record the conditional deviation estimate used below.

### Lemma 4.1 (conditional rare-block deviation)

Let (F) be the number of whole (b)-blocks in a uniform
rank-((m-q)) set, where (b\to\infty), (b=o(\sqrt m)), and
(2^b=o(\sqrt m)).  If (c>0) is fixed, then

\[
 \log\Pr\left(
 F\le {2m\over b2^b}-{c\sqrt m\over b}+o(\sqrt m/b)
 \right)
 =-\left({c^2\over4}+o(1)\right){2^b\over b}.
\tag{4.1}
\]

#### Proof

Under independent fair choices inside the (n=2m/b) blocks, let
(R_j) be block rank and (I_j={\bf1}_{\{R_j=b\}}).  Conditioning
(\sum R_j=m-q) gives the uniform target layer.  At density one half,

\[
 \operatorname {Var}R_j={b\over4},\quad
 \operatorname {Cov}(R_j,I_j)={bp\over2},\quad
 \operatorname {Var}I_j=p(1-p).
\]

Therefore the variance of (I_j) after orthogonal projection off the
rank coordinate is

\[
 \tau_b^2=p\bigl(1-(b+1)p\bigr)=p(1+o(1)).
\tag{4.2}
\]

The conditional mean of (F) is

\[
 {2m\over b}p-2pq+O(bp+b^2p)
 ={2m\over b2^b}+o(\sqrt m/b).
\tag{4.3}
\]

Put (s=c\sqrt m/b).  Then

\[
 {s\over n\tau_b^2}={c\over2}{2^b\over\sqrt m}=o(1),
 \qquad
 {s^2\over2n\tau_b^2}
 =\left({c^2\over4}+o(1)\right){2^b\over b}.
\tag{4.4}
\]

Apply exponential tilting to the two-dimensional sum
(\sum(R_j,I_j)), choosing the second tilt to make the (I)-mean fall by
(s) and the first tilt to keep the (R)-sum fixed.  The second tilt is
(-s/(n\tau_b^2)(1+o(1))); the first is its covariance-cancelling
projection.  Taylor expansion of the joint cumulant gives the quadratic
cost in (4.4).  Its third and higher terms are smaller by the factor
(s/(n\tau_b^2)=o(1)).  Under the tilted law, the two-dimensional local
central limit theorem gives a polynomial, hence
(\exp(o(2^b/b))), cost for imposing the two exact lattice sums.  This
proves the matching lower bound.  Chernoff's inequality with the same tilt
gives the upper bound. \(\square\)

### Theorem 4.2 (moderate growing-block deficit)

If (b\to\infty) and (2^b=o(\sqrt m)), then (0.1) holds.

#### Proof

Choose (\varepsilon_b\downarrow0) so slowly that
(\log(1/\varepsilon_b)=o(2^b/b)).  Lemma 3.1 at
(x=-A/2+\varepsilon_b), followed by Lemma 2.1, confines every deficient
profile to

\[
 F\le {2m\over b2^b}-{(A-o(1))\sqrt m\over b}.
\]

Lemma 4.1 with (c=A-o(1)) proves the upper bound in (0.1).

At (x=-A/2-\varepsilon_b), Lemma 3.1 gives
(X_k/T_k\le1-c_A\varepsilon_b) on a neighboring interval whose target
mass has, by the tilted local form of Lemma 4.1, logarithm

\[
 -\left({A^2\over4}+o(1)\right){2^b\over b}.
\]

Multiplication by (c_A\varepsilon_b=exp(o(2^b/b))) does not change the
logarithmic rate.  This is the lower bound. \(\square\)

There is also a closed form on the critical scale.  Suppose

\[
             {2^b\over\sqrt m}\longrightarrow
             \gamma\in(0,2/A).
\]

Put

\[
 \lambda={2m\over b2^b}={2\sqrt m\over b\gamma}(1+o(1)),
 \qquad u=1-{A\gamma\over2},
 \qquad h(u)=1-u+u\log u.
\]

The same two-dimensional exponential tilt, now with a bounded rather than
vanishing (I)-tilt, gives

\[
 \boxed{
 \log {\Delta_{m,b}(A)\over N_q}
 =-\lambda h(u)+o(\lambda). }
\tag{4.5}
\]

Indeed the conditional log moment generating function of (F), uniformly
for bounded tilt, is

\[
 \lambda(e^t-1)+o(\lambda);
\]

the rank-compensating tilt is \(O(m^{-1/2})=o(1)\), so Legendre duality
gives the Poisson rate (h).  Lemmas 2.1 and 3.1 place the likelihood
crossing at (u\lambda+o(\lambda)), and tilting just to either side of the
crossing supplies the two bounds in (4.5).  At
(\gamma=2/A), a deficient stratum, if lower-order arithmetic leaves one,
has total mass at most

\[
                         \exp(-(1+o(1))\lambda)N_q.
\tag{4.6}
\]

Equations (0.1), (4.5), and (4.6), together with the empty-profile result
above the transition, prove

\[
 \boxed{
 b\to\infty\quad\Longrightarrow\quad
 \Delta_{m,b}(A)=o(W). }
\tag{4.7}

For fixed (b), the fixed-block local limit theorem instead gives
(\Delta_{m,b}(A)=\Theta_{A,b}(W)).  Thus bounded versus unbounded (b)
is the sharp threshold at one prescribed Gaussian depth.

## 4A. The simultaneous all-depth threshold

The preceding conclusion cannot simply be summed over the
\(\Theta(\sqrt m)\) protected depths.  The largest aggregate contribution
comes from depths much smaller than \(H\).

For an arbitrary \(q\), define

\[
 \Delta_{m,b}(q)=\sum_k(A_{m-q,k}-A_{m,k})_+,
 \qquad
 \mathfrak D_{m,b}(A)
 ={1\over W}\sum_{1\le q\le A\sqrt m}\Delta_{m,b}(q),
\tag{4A.1}
\]

and put

\[
                         \Lambda_b={2^b\over b}.
\tag{4A.2}
\]

### Theorem 4A.1 (all-depth profile mass)

Suppose \(b\to\infty\), \(\Lambda_b\to\infty\), and
\(b^2\Lambda_b=o(m)\).  Then, for every fixed \(A>0\),

\[
 \boxed{
 \mathfrak D_{m,b}(A)
 =\left({2\over3\sqrt\pi}+o(1)\right)
       {\sqrt m\over\Lambda_b^{3/2}}.}
\tag{4A.3}
\]

If \(b^2\Lambda_b\not=o(m)\), then
\(\mathfrak D_{m,b}(A)=o(1)\).  Consequently, over all growing \(b\),

\[
 \boxed{
 \sum_{q\le A\sqrt m}\Delta_{m,b}(q)=o(W)
 \quad\Longleftrightarrow\quad
 {\Lambda_b\over m^{1/3}}\longrightarrow\infty.}
\tag{4A.4}
\]

At the critical scale \(\Lambda_b\sim c\,m^{1/3}\),

\[
 {1\over W}\sum_{q\le A\sqrt m}\Delta_{m,b}(q)
 \longrightarrow {2\over3\sqrt\pi}\,c^{-3/2}.
\tag{4A.5}
\]

The upper sign has the identical mass.  Thus the sum over both signed
ledgers has twice the constant in (4A.3), although one physical crossing
transition may serve windows of both signs.

#### Proof

Let \(p=2^{-b}\), and let \(\mu_0\) be the source-layer mean of the
full-block count.  The exact hypergeometric formula gives

\[
 \mu_0={2m\over b}{(m)_b\over(2m)_b}
       ={2m\over b}p(1+O(b^2/m)).
\]

On the target layer, the conditional mean and variance are

\[
 \mu_q=\mu_0-2pq\{1+O(bq/m+b^2/m)\},\qquad
 \sigma_b^2={2m\over b}p(1+o(1))
            ={2m\over b^2\Lambda_b}(1+o(1)).
\tag{4A.6}
\]

Thus the source mean exceeds the target mean by

\[
                         d_q=2pq(1+o(1)).
\tag{4A.7}
\]

Take

\[
                 q=y\sqrt{m/\Lambda_b},\qquad
                 z={k-\mu_q\over\sigma_b}.
\tag{4A.8}
\]

Uniformly for \(y\) in a fixed compact subset of \((0,\infty)\), the
two-dimensional local central limit theorem for
\(\sum(R_j,I_j)\), with the rank coordinate conditioned, gives

\[
 {A_{m,k}\over A_{m-q,k}}
 =\exp\left\{
 {y^2\over\Lambda_b}
 +{\sqrt2\,y\over\Lambda_b}z
 +O(\Lambda_b^{-2})+o(\Lambda_b^{-1})
 \right\}.
\tag{4A.9}
\]

Here the first term is
\(\log(W/N_q)=q^2/m+o(\Lambda_b^{-1})\), while

\[
 {d_q\over\sigma_b}
 ={\sqrt2\,y\over\Lambda_b}(1+o(1))
\tag{4A.10}
\]

is the slope of the normal likelihood ratio.  The likelihood crossing is
therefore at

\[
                         z=-{y\over\sqrt2}+o(1).
\tag{4A.11}
\]

The error in the likelihood ratio (4A.9) is uniform on compact
\(y,z\)-sets.  Expand the exact coefficient saddle.  The unconditioned
binomial rank has zero third cumulant, deletion of the all-one atom
contributes \(O(pb^3)\) per block, and the difference of all fourth and
higher saddle terms at two coefficient indices separated by \(q\) is
\(o(\Lambda_b^{-1})\) at the scale (4A.8).  This proves the required
ratio estimate directly, rather than by subtracting two local-limit
approximations.  Separately, \(b^2\Lambda_b=o(m)\) gives
\(\sigma_b^2\to\infty\), so the target standardized profile converges to
the normal law with \(o(1)\) distributional error.  Since the integrand
in the deficit is \(O(\Lambda_b^{-1})\), that \(o(1)\) error contributes
only \(o(\Lambda_b^{-1})\) to (4A.12).

Let \(\phi,\Phi\) be the standard normal density and distribution
function.  Integrating \(1-A_{m,k}/A_{m-q,k}\) below the crossing in
(4A.11) gives

\[
 {\Delta_{m,b}(q)\over W}
 ={g(y)+o(1)\over\Lambda_b},
\tag{4A.12}
\]

where

\[
 g(y)=\sqrt2\,y
 \left[
   \phi\!\left({y\over\sqrt2}\right)
   -{y\over\sqrt2}\Phi\!\left(-{y\over\sqrt2}\right)
 \right].
\tag{4A.13}
\]

For clarity, (4A.13) is just

\[
 \sqrt2\,y\int_{-\infty}^{-y/\sqrt2}
              \left(-z-{y\over\sqrt2}\right)\phi(z)\,dz.
\]

The same exponential tilt used in Lemma 4.1 gives the summable uniform
bound

\[
 {\Delta_{m,b}(q)\over W}
 \le {C_A\over\Lambda_b}(1+y)^3e^{-c_Ay^2}
\tag{4A.14}
\]

for \(1\le q\le A\sqrt m\).  Hence (4A.12) may be summed as a Riemann
sum, whose mesh is \(\sqrt{\Lambda_b/m}\):

\[
 \mathfrak D_{m,b}(A)
 ={ \sqrt m\over\Lambda_b^{3/2}}
   \left(\int_0^\infty g(y)\,dy+o(1)\right).
\tag{4A.15}
\]

Writing \(u=y/\sqrt2\) and using Fubini,

\[
\begin{aligned}
 \int_0^\infty g(y)\,dy
 &=2\sqrt2\int_0^\infty
       u\{\phi(u)-u\Phi(-u)\}\,du\\
 &=2\sqrt2\left\{
      {1\over\sqrt{2\pi}}
      -{1\over3}\int_0^\infty t^3\phi(t)\,dt
    \right\}\\
 &=2\sqrt2\left\{
      {1\over\sqrt{2\pi}}
      -{2\over3\sqrt{2\pi}}
    \right\}
 ={2\over3\sqrt\pi}.
\end{aligned}
\tag{4A.16}
\]

This proves (4A.3).

It remains to cover the range where the conditional full-block variance
does not diverge.  Couple a uniform rank-\((m-q)\) target \(T\) to a
uniform middle set \(X\supset T\).  Then

\[
 {\Delta_{m,b}(q)\over N_q}
 \le d_{\rm TV}(F_b(T),F_b(X))
 \le\Pr(F_b(T)\ne F_b(X))
 \le Cq2^{-b}.
\tag{4A.17}
\]

The final inequality follows by summing over blocks: a block must be full
in \(X\), which has probability at most \(2^{-b}\), and one of its
coordinates must be among the \(q\) deleted coordinates.  The
monotone-likelihood calculation at \(k=0\), uniformly in
\(q\le A\sqrt m\), also shows that deficient profiles can occur only for

\[
                         q\le C{m\over2^b}
                         =C{m\over b\Lambda_b}.
\tag{4A.18}
\]

Summing (4A.17) only through (4A.18) gives

\[
 \mathfrak D_{m,b}(A)
 \le C{m^2\over b^3\Lambda_b^3}.
\tag{4A.19}
\]

If \(b^2\Lambda_b\ge c m\) and \(b=o(m^{1/3})\), the right side is
\(O(b^3/m)=o(1)\).  If \(b\ge m^{1/3}\), the probability that a middle
set contains any whole block is at most
\((2m/b)2^{-b}=o(1)\), and Lemma 2.1 makes every profile nondeficient
eventually.  Thus the complementary range also has \(o(1)\) aggregate
deficit.

Finally, the transition \(\Lambda_b\asymp m^{1/3}\) lies inside the
local-limit range \(b^2\Lambda_b=o(m)\).  Equations (4A.3) and (4A.19)
therefore prove (4A.4)--(4A.5). \(\square\)

## 5. Requested scales

All logarithms in the examples below are base two.

1. If (b=c\log_2m) with (0<c<1/2), then
   
   \[
   {\Delta_{m,b}(A)\over W}
   =\exp\left[-\left({A^2\over4c}+o(1)\right)
                    {m^c\over\log_2m}\right].
   \tag{5.1}
   \]
2. If (b=(1/2)\log_2m+O(1)), write
   (2^b/\sqrt m\to\gamma).  For (\gamma<2/A), equation (4.5)
   applies and the deficit is
   (\exp(-\Theta_A(\sqrt m/\log m))W).  For (\gamma>2/A), it is
   exactly zero eventually.
3. If (b=c\log_2m) with (c>1/2), in particular if
   (b\asymp\log m), the deficit is exactly zero eventually.
4. If \(b=m^\alpha\) for any fixed \(0<\alpha<1\), then a middle set has a
   whole block with probability at most
   
   \[
                   {2m\over b}2^{-b}
                   =\exp(-\Theta(m^\alpha)),
   \]
   
   and the monotone likelihood lemma gives
   (\Delta_{m,b}(A)=0) eventually.
5. A hypothetical disjoint block system with
   (b=R\asymp\sqrt{mH}\asymp m^{3/4}) is therefore far beyond the
   disappearance threshold.  In the actual compiler construction the
   packet supports are not a coordinate partition, so this hypothetical
   substitution is not the relevant one.

As a slower example, (b=\log_2\log m) gives

\[
 {\Delta_{m,b}(A)\over W}
 =\exp\left[-\left({A^2\over4}+o(1)\right)
                 {\log m\over\log_2\log m}\right],
\]

already (o(1)), although deficient strata still exist.

That last statement is only one-depth.  The all-depth conclusions from
Theorem 4A.1 are as follows.

* For \(b=c\log_2m\),
  \[
   \mathfrak D_{m,b}(A)
   =\left({2\over3\sqrt\pi}+o(1)\right)
     (c\log_2m)^{3/2}m^{(1-3c)/2}.
  \tag{5.2}
  \]
  Hence \(c>1/3\) succeeds, \(c<1/3\) fails, and the bare choice
  \(c=1/3\) still fails by a factor \((\log m)^{3/2}\).
* Writing
  \[
      b={1\over3}\log_2m+\log_2\log_2m+s_m,
  \]
  gives
  \[
       {\Lambda_b\over m^{1/3}}=(3+o(1))2^{s_m}.
  \tag{5.3}
  \]
  Thus \(s_m\to+\infty\) is the sharp all-depth escape, bounded \(s_m\)
  leaves a nonzero limiting obstruction, and \(s_m\to-\infty\) fails.
* For \(b=\log_2\log m\), the one-depth deficit displayed above is tiny,
  but
  \[
    \mathfrak D_{m,b}(A)
    =\left({2\over3\sqrt\pi}+o(1)\right)
       {\sqrt m\,(\log_2\log m)^{3/2}\over(\log_2m)^{3/2}},
  \]
  which diverges.  This is the cleanest illustration of why
  \(b\to\infty\) alone is not enough for a common all-depth ledger.

## 6. Transverse moves and the exact crossing charge

Return now to a factor which may use cross-block moves.  For a selected
lower depth-(q) window (\omega), let (c(\omega)) be the number of its
Johnson transitions whose endpoints lie in different prescribed blocks.
If (X(\omega)) is its middle owner and (T(\omega)) its lower
intersection, then

\[
       0\le F_b(X(\omega))-F_b(T(\omega))\le c(\omega).
\tag{6.1}

The first inequality holds because (T\subseteq X).  An internal move
cannot destroy a full block.  A cross-block move removes one coordinate
from only one current block and can therefore destroy at most one block
which was full in the starting owner.  Charging each first destruction to
the transition which causes it proves (6.1).  Complementation gives the
upper analogue.

Let \(E_q^-\) be the number of lower depth-\(q\) owner occurrences with
\(c(\omega)>0\), and let \(M_q^-\) be the number of lower targets which
are permitted to remain uncovered.  Use the weight which is one on all
deficient profiles in (1.3).  Every occurrence not counted by \(E_q^-\)
is still profile preserving.  Therefore

\[
 \boxed{
                         E_q^-+M_q^-\ge\Delta_{m,b}(q). }
\tag{6.2}
\]

The same inequality holds for the upper sign.  It is outcome-wise and
does not assume independent packet choices.  In particular, if the final
floor energy is \(o(W)\), then \(M_q^\pm=o(W)\), and a fixed-\(b\)
construction must have \(E_q^\pm=\Omega_{A,b}(W)\) at
\(q=A\sqrt m+O(1)\).

On a cyclic factor, one physical cross transition lies in at most \(q\)
directed length-\(q\) windows.  If \(C\) is the number of cross
transitions, then \(E_q^\pm\le qC\), and hence

\[
                         C\ge {\Delta_{m,b}(q)-M_q^\pm\over q}.
\tag{6.3}
\]

Thus the exact necessary depth-(q) crossing-window density is

\[
 {\Delta_{m,b}(A)\over W}=
 \begin{cases}
   \Theta_{A,b}(1),&b=O(1),\\[2mm]
   \exp[-(A^2/4+o(1))2^b/b],
       &b\to\infty, 2^b=o(\sqrt m),\\[2mm]
   0,&2^b>(2/A+o(1))\sqrt m.
 \end{cases}
\tag{6.4}

Summing (6.2) through \(H=A\sqrt m\) gives, separately for each sign,

\[
 \boxed{
 \sum_{q\le H}(E_q^\pm+M_q^\pm)
 \ge\sum_{q\le H}\Delta_{m,b}(q).}
\tag{6.5}
\]

One physical cross transition lies in at most
\(\sum_{q\le H}q=H(H+1)/2\) signed window occurrences, so also

\[
 C\ge {2\over H(H+1)}
 \left\{\sum_{q\le H}\Delta_{m,b}(q)
       -\sum_{q\le H}M_q^\pm\right\}.
\tag{6.6}
\]

In the growing transition regime, combine (6.5) with Theorem 4A.1.  If
the total signed hole budget is \(o(W)\), then

\[
 {1\over W}\sum_{q\le H}E_q^\pm
 \ge\left({2\over3\sqrt\pi}+o(1)\right)
       {\sqrt m\over\Lambda_b^{3/2}}-o(1).
\tag{6.7}
\]

There is also a useful physical-transition charge.  Put
\(q_*=\lfloor\sqrt{m/\Lambda_b}\rfloor\).  The function \(g\) in
(4A.13) has a positive minimum on \(1\le y\le2\).  Hence every
\(q\in[q_*,2q_*]\) satisfies

\[
 {E_q^\pm+M_q^\pm\over W}\ge {c_0+o(1)\over\Lambda_b}
\tag{6.8}
\]

for an absolute \(c_0>0\).  If

\[
 C=o\!\left({W\over\sqrt{m\Lambda_b}}\right),
\]

then \(E_q^\pm\le qC=o(W/\Lambda_b)\) throughout that interval.
Summing (6.8) would force

\[
 \sum_{q\le H}M_q^\pm
 \ge(c_0+o(1)){W\sqrt m\over\Lambda_b^{3/2}}.
\]

Therefore, whenever \(\Lambda_b=O(m^{1/3})\) and the total hole budget is
\(o(W)\),

\[
 \boxed{
 {C\over W}=\Omega\!\left({1\over\sqrt{m\Lambda_b}}\right).}
\tag{6.9}
\]

At the all-depth critical scale \(\Lambda_b\asymp m^{1/3}\), this means
\(\Omega(W)\) total exceptional window occurrences and
\(\Omega(W/m^{2/3})\) cross transitions.

This is the requested quantitative boundary.  A no-go uniform over every
\(b=o(m)\) is false, but the common all-depth escape is sharper than the
one-depth escape: without transverse windows it requires
\(2^b/b\gg m^{1/3}\).  Beyond the half-logarithmic threshold there is not
even a deficient depth-\(H\) full-block stratum.

## 7. Application to the diverse compiler

In the rank-twisted construction one macroblock is

\[
                         B_j=A_j\mathbin{\dot\cup}C_j,
                         \qquad |A_j|=|C_j|=d.
\]

At local rank (k), the frame is a perfect matching (M_{j,k}) from
(A_j) to (C_j).  For the cyclic rank twist, the union over all (k)
is exactly (K_{d,d}).  Hence the coordinate-union graph has connected
components

\[
                         B_j,\qquad b=|B_j|=2d.
\tag{7.1}
\]

A retained (Q_R) packet chooses (R) split edges from many such
components.  Its active physical support has at most (2R) coordinates,
but owner-disjoint packets are not coordinate-disjoint, and their supports
cannot be used as blocks in (1.1).  Conversely, the compiler conjugate is
only a bijection between abstract directions and the already selected
physical edges.  It creates no edge between two (B_j)'s.  Therefore
(7.1) is the exact block system for the full-block dual.

If \(d\to\infty\), equation (4.7) gives the one-depth statement

\[
                     \Delta_{m,2d}(A)=o(W).
\tag{7.2}
\]

For the common all-depth ledger, Theorem 4A.1 instead gives the exact
condition

\[
 \boxed{
             {2^{2d}\over2d}\gg m^{1/3}.}
\tag{7.3}
\]

Equivalently,

\[
 d>{1\over6}\log_2m+{1\over2}\log_2\log_2m+\omega(1).
\tag{7.4}
\]

If \(d=C\log_2m\), the all-depth profile obstruction disappears for
\(C>1/6\).  The stronger assertion that the depth-\(H\) deficient set is
exactly empty holds for \(C>1/4\).  The concrete customary choice
\(d=10\log_2m\) satisfies both conditions with enormous slack.

At the same time every rank-twisted axis joins \(A_j\) to \(C_j\).  If
the old bounded quartet partition refines the two halves,
every such axis crosses its quartet block, so every nonempty compiler
window is exceptional for that bounded profile.  This is precisely how the
construction pays (6.2) at bounded scale while needing no crossing at the
growing macroblock scale.

When (H=A\sqrt m),

\[
                         R\asymp\sqrt{mH}\asymp m^{3/4}.
\]

This scale supplies long trace-injective compiler components and an
(o(W/H)) cycle count.  It does not improve (7.2), because (R) does not
change the coordinate-union components.  Nor does (7.2) imply target Hall:
if the (R) selected axes are localized in a carrier (E) of size
(\Theta(R)), the exact fibre ratio is at most

\[
              \exp(-c q^2/R)=\exp(-\Theta(m^{1/4}))=o(1).
\]

Thus the diverse compiler genuinely escapes the bounded internal-gadget
profile dual, but still requires the dispersed selected-axis Hall theorem
and the common all-depth integral covariance theorem.

## 8. Proved boundary

The following are proved here.

1. The fixed-(b) Gaussian Hall obstruction extends uniformly to growing
   (b), with the sharp logarithmic deficit (0.1).
2. The existence of any deficient full-block stratum has its sharp
   transition at (2^b=2\sqrt m/A).
3. At one prescribed Gaussian depth, linear obstruction is equivalent,
   for this profile, to bounded block size.  Across the entire protected
   band the sharp threshold is \(2^b/b\gg m^{1/3}\), with the exact
   transition constant \(2/(3\sqrt\pi)\) per sign.
4. Cross-block moves obey the exact one-depth and aggregate occurrence
   and transition charges (6.2)--(6.6).
5. At the diverse-compiler scale the correct invariant component size is
   \(2d\), not \(R\).  Rank-twisted macroblocks escape the full all-depth
   dual exactly when \(2^{2d}/(2d)\gg m^{1/3}\); the standard
   \(d=10\log_2m\) choice does.

Not proved here are the dispersed arbitrary-weight Hall inequality, the
negative floor-covariance selection, or coefficient one.  The surviving
constructive gate is therefore not further growth of (R), but a selected
axis system which avoids the independent carrier cuts while admitting one
integral all-depth, both-sign compiler choice.
