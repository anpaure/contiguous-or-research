# The growing-block full-profile obstruction: uniform saddle, exact monotonicity, and the sharp threshold

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web input
is used.

## 0. Statement and interpretation

Let (q=A\sqrt m+O(1)), where (A>0) is fixed.  Partition the (2m)
physical coordinates into

\[
                         n={2m\over b}
\tag{0.1}
\]

blocks of size (b=b(m)), initially assuming (b\mid2m).  For a set
(Y), write (F_b(Y)) for the number of full blocks.  Put

\[
\begin{aligned}
 X_{m,k}&=\#\{X\in\tbinom{[2m]}m:F_b(X)=k\},\\
 T_{m-q,k}&=\#\{T\in\tbinom{[2m]}{m-q}:F_b(T)=k\},\\
 D_{m,b,q}&=\sum_{k\ge0}(T_{m-q,k}-X_{m,k})_+,
 \qquad N_q=\binom{2m}{m-q}.
\end{aligned}
\tag{0.2}
\]

Thus \(D_{m,b,q}\) is the strongest deficit obtainable by a profile
weight \(0\le w_k\le1\), because
\[
 \max_{0\le w_k\le1}\sum_k w_k(T_{m-q,k}-X_{m,k})=D_{m,b,q}.
\]
It is also the exact number
of crossings or holes which any construction must supply before the
(F_b)-Farkas witness can disappear.

### Theorem 0.1 (sharp growing-(b) boundary)

Assume (b=o(m)).

1.  The ratio

    \[
                         {X_{m,k}\over T_{m-q,k}}
    \tag{0.3}
    \]

    is nondecreasing in (k), exactly, for every (m,b,q).  Consequently
    the deficit profiles form an initial interval of integers.

2.  Define the real crossing index

    \[
    \kappa_{m,b,q}
      ={m/(2^b-1)-q/2\over b2^{b-1}/(2^b-1)}
      ={m\over b2^{b-1}}-{q(2^b-1)\over b2^b}.
    \tag{0.4}
    \]

    Whenever \(b=O(\log m)\) and \(\kappa_{m,b,q}\) is separated from
    zero by (\gg\sqrt m/b), the last deficit profile is

    \[
                         \kappa_{m,b,q}+o(\sqrt m/b).
    \tag{0.5}
    \]

3.  Suppose (b\to\infty) and (2^b=o(\sqrt m)).  Then

    \[
    \boxed{
    \log {D_{m,b,q}\over N_q}
       =-\left({A^2\over4}+o(1)\right){2^b\over b}.}
    \tag{0.6}
    \]

    In particular (D_{m,b,q}=o(W)), where (W=\binom{2m}m).  Thus the
    linear Gaussian Hall obstruction from a fixed block size vanishes for
    *every* sequence (b(m)\to\infty), however slowly.

4.  Suppose

    \[
                         {2^b\over\sqrt m}\longrightarrow c\in(0,\infty).
    \tag{0.7}
    \]

    If (c<2/A), put (I(x)=1-x+x\log x).  Then

    \[
    \boxed{
    \log {D_{m,b,q}\over N_q}
      =-\left({2\over c}I(1-Ac/2)+o(1)\right){\sqrt m\over b}.}
    \tag{0.8}
    \]

    If (c>2/A), then (D_{m,b,q}=0) for all sufficiently large (m).
    At (c=2/A), one has at least the sharp conclusion

    \[
                         D_{m,b,q}=o(N_q),
    \tag{0.9}
    \]

    and any possible deficit is confined to (k=0) up to a vanishing
    boundary ambiguity.

5.  If (2^b/\sqrt m\to\infty), then

    \[
                         D_{m,b,q}=0
    \tag{0.10}
    \]

    for all sufficiently large (m).  This includes (b\sim\beta\log_2m)
    with (\beta>1/2), every (b\asymp\log m) with coefficient exceeding
    (1/2), every (b=m^\alpha), (0<\alpha<1), and the compiler scale
    (b\asymp R\asymp\sqrt{mH}=m^{3/4}) when (H\asymp\sqrt m).

The theorem distinguishes two thresholds which should not be conflated.
The normalized linear deficit disappears as soon as (b\to\infty).  The
deficit profiles themselves disappear only at

\[
                         2^b\sim {2\over A}\sqrt m,
\tag{0.11}
\]

or (b=(1/2)\log_2m+\log_2(2/A)+o(1)).

At the finer coefficient-one repair scale (W/H), (0.6) says, away from
the boundary constants,

\[
\begin{array}{ll}
 D_{m,b,q}\gg W/H,
 &\displaystyle {A^2 2^b\over4b}< (1-o(1))\log H,\\[6pt]
 D_{m,b,q}\ll W/H,
 &\displaystyle {A^2 2^b\over4b}> (1+o(1))\log H.
\end{array}
\tag{0.12}
\]

For (H\asymp\sqrt m), this transition is

\[
                         {2^b\over b}\sim {2\over A^2}\log m,
\tag{0.13}
\]

namely (b=\log_2\log m+\log_2\log\log m+O_A(1)).  Thus a block size
only doubly logarithmic in the ambient scale already makes the old
profile toll smaller than the admissible (W/H) ledger.

## 1. Exact coefficients

Put

\[
 h_b(z)=(1+z)^b-z^b,
 \qquad D_b=2^b-1.
\tag{1.1}
\]

Choosing the full blocks first gives the exact identities

\[
\begin{aligned}
 X_{m,k}&=\binom nk[z^{m-bk}]h_b(z)^{n-k},\\
 T_{m-q,k}&=\binom nk[z^{m-q-bk}]h_b(z)^{n-k}.
\end{aligned}
\tag{1.2}
\]

Let (J_b) have distribution

\[
 \Pr(J_b=j)={\binom bj\over D_b},\qquad0\le j<b.
\tag{1.3}
\]

Writing (p_b=2^{-b}), direct calculation gives

\[
\begin{aligned}
 \mu_b&={b(2^{b-1}-1)\over D_b},\\
 a_b:=b-\mu_b&={b\over2(1-p_b)},\\
 \sigma_b^2&={b(1-(b+1)p_b)\over4(1-p_b)^2}.
\end{aligned}
\tag{1.4}
\]

For (d=n-k), the source coefficient index has displacement

\[
 \delta_{b,k}:=m-bk-\mu_bd
               ={m\over D_b}-a_bk
\tag{1.5}
\]

from the mean of (J_1+\cdots+J_d).  The target displacement is
(\delta_{b,k}-q).  Formula (0.4) is exactly the solution of

\[
                         \delta_{b,k}=q/2.
\tag{1.6}
\]

## 2. An exact monotone-likelihood theorem

For (0\le r\le2m), let

\[
                         A(r,k)=
 \#\{Y\in\tbinom{[2m]}r:F_b(Y)=k\}.
\tag{2.1}
\]

### Lemma 2.1 (TP\(_2\))

The array (A(r,k)) is totally positive of order two:

\[
 A(r_1,k_1)A(r_2,k_2)
 \ge A(r_1,k_2)A(r_2,k_1)
\tag{2.2}
\]

whenever (r_1\le r_2) and (k_1\le k_2).

#### Proof

For one block, form the two-column array

\[
 c_b(r,0)=\binom br\quad(0\le r<b),
 \qquad c_b(b,1)=1,
\tag{2.3}
\]

with all other entries zero.  Every nontrivial (2\times2) minor has its
first factor in column zero at a row below (b) and its second factor in
column one at row (b); it is therefore nonnegative.  Thus (c_b) is
TP\(_2\).

The convolution of two nonnegative TP\(_2\) arrays is TP\(_2\).  This is
the two-dimensional convolution form of the four-functions inequality.
Apply that inequality to the four translates of the two factors at the
corners \((r_i,k_j)\), \(i,j\in\{1,2\}\).  Their pointwise TP\(_2\)
inequalities give, after summing over the convolution indices,
\[
 (f*g)(r_1,k_1)(f*g)(r_2,k_2)
 \ge(f*g)(r_1,k_2)(f*g)(r_2,k_1).
\]
For completeness, the four-functions inequality follows by pairing each
unordered pair of indices with its coordinatewise meet and join.  Iterating
this closure property through the \(n\) blocks proves (2.2), because
\(A=c_b^{*n}\).
\(\square\)

Taking (r_1=m-q), (r_2=m), (k_1<k_2) in (2.2) gives

\[
 {X_{m,k_1}\over T_{m-q,k_1}}
 \le {X_{m,k_2}\over T_{m-q,k_2}}
\tag{2.4}
\]

whenever the denominators are nonzero.  This proves Theorem 0.1(1).  It
also shows that no disconnected collection of exceptional profile islands
is hidden outside the saddle calculation.

## 3. A triangular local limit uniform in (b=o(m))

We record precisely the local estimate used below.

### Lemma 3.1 (uniform central coefficient ratio)

Let (b=o(m)), let (d=(2m/b)(1+o(1))), and put
(V_{b,d}=d\sigma_b^2\).  Uniformly for lattice displacements
(|x|\le C\sqrt m), with fixed (C),

\[
 [z^{\mu_bd+x}]h_b(z)^d
 ={D_b^d\over\sqrt{2\pi V_{b,d}}}
   \exp\!\left(-{x^2\over2V_{b,d}}\right)(1+o(1)).
\tag{3.1}
\]

Consequently, whenever both (\delta_{b,k}) and
(\delta_{b,k}-q) are (O(\sqrt m)),

\[
 \log{X_{m,k}\over T_{m-q,k}}
 ={q^2-2q\delta_{b,k}\over2V_{b,n-k}}+o(1).
\tag{3.2}
\]

#### Proof

The characteristic function of (J_b) is explicitly

\[
 \phi_b(t)=
 {2^b e^{ibt/2}\cos(t/2)^b-e^{ibt}\over D_b}.
\tag{3.3}
\]

On (|t|\le b^{-1/2}o(1)), Taylor expansion of its logarithm gives

\[
 \log\mathbb E e^{it(J_b-\mu_b)}
 =-{\sigma_b^2t^2\over2}
   +O\bigl((b^{3/2}+b^3p_b)|t|^3\bigr).
\tag{3.4}
\]

Since (d\asymp m/b), the aggregate standardized third-moment error is

\[
 O\!\left(\sqrt{b/m}+{b^2p_b\over\sqrt m}\right)=o(1).
\tag{3.5}
\]

Outside a shrinking neighbourhood of zero, (3.3) gives

\[
 |\phi_b(t)|\le
 {2^b|\cos(t/2)|^b+1\over D_b}.
\tag{3.6}
\]

Splitting the Fourier integral into
(|t|\le L/\sqrt m), (L/\sqrt m<|t|\le b^{-1/2}), and the complement,
then taking (L\to\infty) slowly, (3.4)--(3.6) show respectively a
Gaussian main term, an (o(m^{-1/2})) Gaussian tail, and an
(o(m^{-1/2})) aperiodic tail.  This proves (3.1), uniformly on bounded
standardized displacements.  Dividing the two instances (x=\delta_{b,k})
and (x=\delta_{b,k}-q) proves (3.2). \(\square\)

At (k=\kappa_{m,b,q}+u\sqrt m/b), with bounded (u), (1.5), (3.2),
(a_b/b\to1/2), and (V_{b,n-k}/m\to1/2) give

\[
 \log{X_{m,k}\over T_{m-q,k}}=Au+o(1).
\tag{3.7}
\]

Together with exact monotonicity, this proves (0.5).

For (k=0), whenever (2^b\asymp\sqrt m), the same calculation uses
(V_{b,n}/m\to1/2) and gives

\[
 \log{X_{m,0}\over T_{m-q,0}}
 =A^2-{2A\sqrt m\over2^b-1}+o(1).
\tag{3.8}
\]

This is negative for (2^b/\sqrt m\to c<2/A) and positive for
(c>2/A).  Exact monotonicity then proves the asserted existence or
nonexistence of every deficit profile in the critical window.

## 4. The subcritical deficit mass

Assume henceforth that (b\to\infty) and (2^b=o(\sqrt m)).  If (K)
denotes the number of full blocks in a uniformly random rank-((m-q))
set, then

\[
 \lambda_b:=\mathbb EK
 ={2m\over b}\,{(m-q)_b\over(2m)_b}
 ={2m\over b2^b}
   -{2A\sqrt m\over2^b}
   +O\!\left({b\over2^b}+{1\over\sqrt m}\right).
\tag{4.1}
\]

Here ((x)_b=x(x-1)\cdots(x-b+1)).  Since the present assumption forces
(b=O(\log m)), expansion of the logarithm of the product defining
((m-q)_b/(2m)_b) is uniform and proves (4.1).

Equations (0.4) and (4.1) yield

\[
 \lambda_b-\kappa_{m,b,q}
 ={A\sqrt m\over b}(1+o(1))=:t_b.
\tag{4.2}
\]

Moreover

\[
 \operatorname {Var}K={2m\over b2^b}(1+o(1))=:v_b^K,
 \qquad {t_b\over v_b^K}= {A2^{b-1}\over\sqrt m}(1+o(1))=o(1),
\tag{4.3}
\]

and

\[
                         {t_b^2\over v_b^K}
 ={A^2 2^{b-1}\over b}(1+o(1))\longrightarrow\infty.
\tag{4.4}
\]

### Lemma 4.1 (conditional rare-block moderate deviation)

Under the assumptions above,

\[
 \log\Pr(K\le\lambda_b-t_b(1+o(1)))
 =-(1+o(1)){t_b^2\over2v_b^K}.
\tag{4.5}
\]

#### Proof

Introduce a mark (u) for a full block.  The joint rank/full-block
generating function is

\[
 G(z,u)=\bigl((1+z)^b+(u-1)z^b\bigr)^n.
\tag{4.6}
\]

Conditioning its (z^{m-q})-coefficient and putting (u=e^\theta), a
two-variable saddle expansion at the rank saddle gives, uniformly for

\[
                         |\theta|=O(t_b/v_b^K)=o(1),
\tag{4.7}
\]

the conditional cumulant identity

\[
 \log\mathbb E e^{\theta(K-\lambda_b)}
 ={v_b^K\theta^2\over2}
  +O\bigl(v_b^K|\theta|^3+v_b^K b2^{-b}\theta^2+o(1)\bigr).
\tag{4.8}
\]

For clarity, (4.8) can be obtained without suppressing a dependence
assumption: differentiate the logarithm of (4.6), adjust the (z)-saddle
to keep the rank coefficient fixed, and use
(z^b/(1+z)^b=2^{-b}(1+O(b/\sqrt m))).  The second derivative is the
Schur complement of the rank/full-block covariance matrix and equals
(v_b^K(1+o(1))); every (j\)-th derivative for (j\ge3) is
(O_j(v_b^K)).  The saddle displacement is (O(b2^{-b}\theta)), giving
the displayed uniform remainder.

The Chernoff bound with (\theta=-t_b/v_b^K) gives the upper half of
(4.5).  Under the corresponding exponential tilt, the mean is
(\lambda_b-t_b+o(t_b)), the variance remains (v_b^K(1+o(1))), and
the Fourier argument of Lemma 3.1 gives a central interval of tilted
probability bounded below by a negative power of (v_b^K).  Its logarithm
is (o(t_b^2/v_b^K)), proving the matching lower bound. \(\square\)

By (3.7) and monotonicity, the support of
((T_{m-q,k}-X_{m,k})_+) ends at
(\kappa_{m,b,q}+o(\sqrt m/b)).  Lemma 4.1 therefore gives the upper
bound in (0.6).  For the lower bound, choose
(\epsilon_m\downarrow0) sufficiently slowly and restrict to

\[
 k\le\kappa_{m,b,q}-\epsilon_m\sqrt m/b.
\tag{4.9}
\]

Equation (3.7) gives (1-X_{m,k}/T_{m-q,k}\ge
1-e^{-A\epsilon_m/2}), while choosing
(|\log\epsilon_m|=o(2^b/b)) makes this factor invisible on the
logarithmic scale in (4.5).  The displacement in (4.9) is
(t_b(1+o(1))).  Thus

\[
 \log {D_{m,b,q}\over N_q}
 =-{t_b^2\over2v_b^K}(1+o(1))
 =-\left({A^2\over4}+o(1)\right){2^b\over b},
\tag{4.10}
\]

which proves (0.6).

## 5. The half-logarithmic critical window

Suppose (2^b/\sqrt m\to c\in(0,2/A)).  Then

\[
 \lambda_b=\left({2\over c}+o(1)\right){\sqrt m\over b},
 \qquad
 {\kappa_{m,b,q}\over\lambda_b}\longrightarrow1-{Ac\over2}.
\tag{5.1}
\]

For every fixed (\theta), the same marked saddle (4.6), now without
expanding in (\theta), gives

\[
 {1\over\lambda_b}\log\mathbb E e^{\theta K}
                         \longrightarrow e^\theta-1.
\tag{5.2}
\]

Indeed a full block has conditional probability (2^{-b}(1+o(1))), and
every joint cumulant of fixed order is (\lambda_b(1+o(1))); the fixed-rank
corrections are smaller by (O(b2^{-b})=o(1)).  Exponential tilting of
(5.2) yields, uniformly for fixed (x\in(0,1)),

\[
 \log\Pr(K\le x\lambda_b)
                         =-\lambda_b I(x)+o(\lambda_b),
 \qquad I(x)=1-x+x\log x.
\tag{5.3}
\]

Using (x=1-Ac/2), and repeating the negligible likelihood-factor
sandwich from Section 4, proves (0.8).

If (c>2/A), (3.8) is bounded positively away from zero.  Hence
(X_{m,0}>T_{m-q,0}), and exact monotonicity (2.4) gives
(X_{m,k}>T_{m-q,k}) for every (k).  Thus (D_{m,b,q}=0).
At (c=2/A), (3.8) is (o(1)), while the only possible deficit lies at
the extreme Poisson tail (k=0+o(\lambda_b)); (5.3) with (x\downarrow0)
gives (0.9), and in fact an exponential upper bound

\[
 {D_{m,b,q}\over N_q}
 \le\exp\!\left(-(A+o(1)){\sqrt m\over b}\right).
\tag{5.4}
\]

## 6. Blocks larger than the critical scale

For (2^b/\sqrt m\to\infty) with (b=O(\log m)), Lemma 3.1 at (k=0)
gives

\[
 \log{X_{m,0}\over T_{m-q,0}}=A^2+o(1)>0.
\tag{6.1}
\]

Exact monotonicity again implies (D_{m,b,q}=0).

If (b/\log m\to\infty), a uniformly random rank-(r) set, for either
(r=m) or (r=m-q), contains a full block with probability at most

\[
 {2m\over b}{(r)_b\over(2m)_b}
 \le {2m\over b}2^{-b}=o(1).
\tag{6.2}
\]

For (b=o(m)), the right side is still (o(1)): if (b\le\sqrt m\), the
displayed exponent is (o(b)), while if (b>\sqrt m\), the exact product
has logarithm at most (-c b) for an absolute (c>0).  Therefore

\[
 X_{m,0}=W(1-o(1)),\qquad
 T_{m-q,0}=N_q(1-o(1)),
\tag{6.3}
\]

and

\[
 {X_{m,0}\over T_{m-q,0}}=e^{A^2+o(1)}>1.
\tag{6.4}
\]

Monotonicity completes (0.10) throughout (b=o(m)).

## 7. The simultaneous all-depth ledger

The pointwise \(q=A\sqrt m\) calculation does not by itself determine the
sum over every \(q\le H\).  The dominant depths for that sum are smaller.
They admit a local asymptotic-normal, or LAN, calculation with an exact
constant.

Put

\[
 \varepsilon_b={2b\over2^b},\qquad
 z_q={q\over\sqrt{\varepsilon_bm}}
     =q\sqrt{{2^b\over2bm}},
\qquad
 \phi(z)={e^{-z^2/2}\over\sqrt{2\pi}}.
\tag{7.1}
\]

### Theorem 7.1 (uniform profile LAN and the all-depth sum)

Assume

\[
 b\longrightarrow\infty,\qquad
 2^b=o(\sqrt{bm}).
\tag{7.2}
\]

Uniformly when \(z_q\) stays in a fixed compact subset of
\([0,\infty)\),

\[
 \boxed{
 {D_{m,b,q}\over W}
  =\varepsilon_b z_q
       \{\phi(z_q)-z_q\Phi(-z_q)\}+o(\varepsilon_b).}
\tag{7.3}
\]

If \(H=A\sqrt m+O(1)\), then

\[
\boxed{
 {1\over W}\sum_{q=1}^{H}D_{m,b,q}
 =\left({1\over3\sqrt{2\pi}}+o(1)\right)
       \sqrt m\,\varepsilon_b^{3/2}
 =\left({2\over3\sqrt\pi}+o(1)\right)
       \sqrt m\left({b\over2^b}\right)^{3/2}.}
\tag{7.4}
\]

Consequently the aggregate full-profile toll has its sharp transition at

\[
                         {2^b\over b}\asymp m^{1/3}.
\tag{7.5}
\]

More exactly, if \(2^b/b\sim C m^{1/3}\), then the left side of (7.4)
converges to

\[
                         {2\over3\sqrt\pi}\,C^{-3/2}.
\tag{7.6}
\]

Thus \(2^b/b\gg m^{1/3}\) makes the complete \(q\le A\sqrt m\) profile
toll \(o(W)\), whereas \(2^b/b\ll m^{1/3}\) makes that aggregate toll
\(\omega(W)\).  This is the relevant threshold when the same construction
must pay every protected depth, even though the pointwise
\(q=A\sqrt m\) deficit had already become \(o(W)\) for every
\(b\to\infty\).

#### Proof

Let \(K\) be the full-block count under a uniformly random target of rank
\(m-q\).  In the range \(z_q=O(1)\), one has

\[
 q=z_q\sqrt{\varepsilon_bm}=o(\sqrt m),\qquad
 \lambda_b:=\operatorname {Var}K
             ={2m\over b2^b}(1+o(1)).
\tag{7.7}
\]

The constants in (7.7) can be read directly from the unconditioned
Bernoulli-\(1/2\) block model.  If \(R\) is total rank, \(I\) is one
block's full indicator, and \(p=2^{-b}\), then

\[
\begin{aligned}
 \operatorname {Var}R&={m\over2},&
 \operatorname {Cov}(R,K)&=mp,&
 \operatorname {Var}K&={2mp(1-p)\over b}.
\end{aligned}
\tag{7.7a}
\]

Consequently the conditional regression coefficient is \(2p\), and the
Schur-complement variance is

\[
 {2mp\over b}\{1-(b+1)p\}
 ={2m\over b2^b}(1+o(1)).
\tag{7.7b}
\]

Tilting the rank from \(m\) to \(m-q\) changes these quantities by
\(1+o(1)\) in the present range.

The source full-block mean exceeds the target mean by

\[
 \Delta_q={2q\over2^b}(1+o(1)).
\tag{7.8}
\]

Its standardized value is

\[
 d_q={\Delta_q\over\sqrt{\lambda_b}}
     =\varepsilon_bz_q(1+o(1)).
\tag{7.9}
\]

Also Stirling's formula gives

\[
 \log {W\over N_q}={q^2\over m}+o(\varepsilon_b)
                  =\varepsilon_bz_q^2+o(\varepsilon_b).
\tag{7.10}
\]

The marked saddle (4.6), expanded jointly in the rank displacement and
the full-block mark, gives the following LAN identity.  If

\[
                         x={k-\mathbb E_{m-q}K\over\sqrt{\lambda_b}}
\tag{7.11}
\]

stays bounded, then

\[
 \log {X_{m,k}\over T_{m-q,k}}
 =\varepsilon_bz_q(z_q+x)+o(\varepsilon_b),
\tag{7.12}
\]

uniformly for bounded \(x,z_q\).  Here the \(-d_q^2/2\) term in the
likelihood ratio is \(O(\varepsilon_b^2)\), and is absorbed by the
remainder.

For exact error accounting, differentiate the logarithm of (4.6) at its
rank saddle.  The full-block variance is \(\lambda_b(1+o(1))\), the
rank/full-block covariance produces (7.8), and every third mixed
cumulant contributes

\[
 O(\varepsilon_b^2(1+|x|+z_q)^3)
   +O\!\left({b\over m}\right).
\tag{7.13}
\]

Under (7.2), \(b/m=o(\varepsilon_b)\).  The one-dimensional local saddle
error after taking the ratio of the two neighbouring rank coefficients is
also \(O(\sqrt{b/m}\,\varepsilon_b)=o(\varepsilon_b)\); the un-differenced
local-limit errors cancel.  This proves (7.12), rather than merely an
\(o(1)\) version of it.

The local central limit theorem for \(K\), on the same saddle, says that
\(x\) has standard-normal lattice density.  Since the exact TP\(_2\)
theorem makes the negative-likelihood set an initial interval, (7.12)
gives

\[
\begin{aligned}
 {D_{m,b,q}\over N_q}
 &=\mathbb E_{m-q}
   \left[\left(1-
     {X_{m,K}\over T_{m-q,K}}\right)_+\right]\\
 &=\varepsilon_bz_q
   \int_{-\infty}^{-z_q}(-z_q-x)\phi(x)\,dx
   +o(\varepsilon_b)\\
 &=\varepsilon_bz_q
   \{\phi(z_q)-z_q\Phi(-z_q)\}+o(\varepsilon_b).
\end{aligned}
\tag{7.14}
\]

Because \(N_q/W=\exp(-\varepsilon_bz_q^2+o(\varepsilon_b))=1+o(1)\),
this proves (7.3).

The same Chernoff tilt used in Lemma 4.1 supplies an integrable uniform
envelope for (7.14): for absolute \(C,c>0\),

\[
 {D_{m,b,q}\over W}
 \le C\varepsilon_b z_q(1+z_q)e^{-c z_q^2}
\tag{7.15}
\]

until the right side is already exponentially negligible; beyond that
point the large-deviation estimate is stronger.  The mesh of the
\(z_q\)-lattice is

\[
                         \Delta z={1\over\sqrt{\varepsilon_bm}}=o(1),
\tag{7.16}
\]

while \(z_H=A/\sqrt{\varepsilon_b}\to\infty\).  Dominated Riemann
summation in (7.3) therefore yields

\[
 {1\over W}\sum_{q\le H}D_{m,b,q}
 =(1+o(1))\sqrt{\varepsilon_bm}\,\varepsilon_b
 \int_0^\infty z\{\phi(z)-z\Phi(-z)\}\,dz.
\tag{7.17}
\]

Finally,

\[
\begin{aligned}
 \int_0^\infty z\phi(z)\,dz&={1\over\sqrt{2\pi}},\\
 \int_0^\infty z^2\Phi(-z)\,dz
 &= {1\over3}\int_0^\infty t^3\phi(t)\,dt
  ={2\over3\sqrt{2\pi}},
\end{aligned}
\tag{7.18}
\]

so the integral in (7.17) is \(1/(3\sqrt{2\pi})\).  This proves
(7.4)--(7.6). \(\square\)

## 8. Explicit named regimes

Let (b=\beta\log_2m+o(\log m)).

* If (0<\beta<1/2), (0.6) becomes

  \[
  \log {D_{m,b,q}\over N_q}
  =-\left({A^2\over4\beta}+o(1)\right)
     {m^\beta\over\log_2m}.
  \tag{7.1}
  \]

* If (\beta>1/2), then (D_{m,b,q}=0) eventually.

* If (b=(1/2)\log_2m+\gamma+o(1)), put (c=2^\gamma).
  Formula (0.8) applies for (2^\gamma<2/A), while the deficit vanishes
  for (2^\gamma>2/A).

If (b=m^\alpha), (0<\alpha<1), or if
(b\asymp\sqrt{mH}=m^{3/4}) at (H\asymp\sqrt m), (0.10) applies:
there is no full-block profile deficit at any (k).

## 9. What this does and does not obstruct

If every selected physical move stays within the (b)-blocks, then
(F_b) is preserved and (D_{m,b,q}) is an exact crossing-or-hole toll.
The preceding theorem proves:

* fixed (b): the old toll is (\Theta_{A,b}(W));
* (b\to\infty): the toll is (o(W)), with the sharp logarithmic size
  (0.6) below the half-logarithmic window;
* (b\gtrsim(1/2)\log_2m): the toll disappears completely once the
  constant in (0.11) is crossed; and
* at the compiler scale (R\asymp m^{3/4}), this invariant supplies no
  obstruction at all.

Thus there is no extension of the bounded-gadget \(\Omega(W)\) no-go to
all (b=o(m)).  A growing block genuinely escapes it.  Conversely, below
the threshold (0.13), any proposed transverse construction must either
leave at least (D_{m,b,q}) target holes or use at least that many
Gaussian-depth occurrences which change (F_b).  The present theorem
does not assert that such crossings suffice: it identifies their exact
profile demand and removes the old invariant once the demand is paid.

The theorem was stated on the divisibility subsequence \(b\mid2m\), the
exact equal-block tensor model.  In the only nontrivial threshold range
\(b=O(\log m)\), a residual block of size \(<b\) perturbs the rank saddle
by \(O(b)=o(\sqrt m)\); conditioning on its rank and summing its \(b+1\)
sectors gives the same estimates.  For larger \(b\), the no-deficit
conclusion follows from the termwise union bound (6.2).  No
coefficient-one conclusion is claimed.
