# Gaussian-annulus multi-seed overlays: exact floor reservoirs, cross-Gram contraction, and orbit-mass obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or external
input is used.

## 0. Verdict

Let

\[
 n=2m+1,
 \qquad
 W=\binom{n}{m},
 \qquad
 I_m=\{q:\lceil a\sqrt m\rceil\le q\le
                 \lfloor b\sqrt m\rfloor\},
 \tag{0.1}
\]

where \(0\le a<b<\infty\) are fixed.  The following facts hold for
literal exact middle-wreath factors.

1.  Any finite collection of exact factors has a canonical
    owner-hypergraph overlay.  In each connected component one may choose
    the complete row shore of any one seed.  Every simultaneous component
    choice is again a literal exact factor.

2.  For an arbitrary probability law on those physical choices, the
    expected floor-corrected annular energy is exactly

    \[
      \boxed{
      \mathbb E\mathcal Q_I
       =\|\bar f\|_I^2-B_I+
        \mathbb E\|f-\bar f\|_I^2.}
      \tag{0.2}
    \]

    There is no omitted floor, component, or integrality term.

3.  For \(r\) seeds and independent uniform component shores, put

    \[
    A_r={1\over r^2}\sum_{i<j}\|f^i-f^j\|_I^2,
    \qquad
    V_r={1\over r^2}\sum_K\sum_{i<j}
                 \|u_{K,i}-u_{K,j}\|_I^2.
    \tag{0.3}
    \]

    Then

    \[
      \boxed{
      \mathbb E\mathcal Q_I(F_{\boldsymbol i})
       ={1\over r}\sum_{i=1}^r\mathcal Q_I(F^i)
        -(A_r-V_r).}
      \tag{0.4}
    \]

    Moreover \(A_r-V_r\) is exactly the total off-component Gram
    coherence.  Thus (0.4), rather than a one-seed spectral gap, is the
    exact multi-seed contraction criterion.

4.  Formula (0.2) has a termwise nonnegative floor decomposition.  If
    \(X_T\) is the random integral load at a target, \(p_T=\mathbb EX_T\),
    and

    \[
      \ell_\lambda(p)=(p-\lambda)^2+\{p\}(1-\{p\}),
      \tag{0.5}
    \]

    then, at each depth,

    \[
      \boxed{
      \mathbb E Q_q
       =\underbrace{\sum_T\ell_{\lambda_q}(p_T)
           -N_q\ell_{\lambda_q}(\lambda_q)}_{\mathcal R_q^{\rm mean}\ge0}
        +\underbrace{\sum_T
          \left(\operatorname {Var}X_T-
             \{p_T\}(1-\{p_T\})\right)}_{
             \mathcal R_q^{\rm round}\ge0}.}
      \tag{0.6}
    \]

    In a fair binary component overlay, if
    \(d_K(T)=u_{K,1}(T)-u_{K,0}(T)\in\mathbb Z\), then the rounding
    reservoir at \(T\) is exactly

    \[
      \boxed{
      {1\over4}\left(
          \sum_Kd_K(T)^2-
          \mathbf1_{\{\sum_Kd_K(T)\ {\rm odd}\}}
      \right).}
      \tag{0.7}
    \]

    It is zero precisely when every \(d_K(T)=0\), or exactly one of them
    is \(1\) or \(-1\).  Every other pattern costs at least \(1/2\).
    Hence a fair binary overlay can have expected annular deficiency
    \(o(W)\) only if all but \(o(W)\) target-depth cells have this
    single-unit geometry.  This is a sharp obstruction to diffuse
    independent component heat.

5.  For any partition of each target layer into target orbits, the exact
    floor energy splits into an orbit-total penalty and a within-orbit
    penalty.  In particular, if every component shore preserves every
    orbit total and the resulting orbit-total penalty is \(\Omega(W)\),
    then every physical child has deficiency \(\Omega(W)\).  More
    generally, an overlay can escape such a cut only by transporting a
    matching \(\Omega(W)\) amount of orbit mass.  This is the precise
    sense in which unrelated seeds can evade the old diagonal-relabeling
    obstruction.

6.  The Gaussian integer baseline is not \(O(W)\).  If
    \(c_q=\lfloor\lambda_q\rfloor\),
    \(\theta_q=\lambda_q-c_q\), and the depth weight has bounded
    Riemann limit \(\omega(x)\), then

    \[
      \boxed{
      B_I=W\sqrt m\left[
       \int_a^b\omega(x)e^{-x^2}
       \vartheta(x)(1-\vartheta(x))\,dx+o_{a,b}(1)
      \right],}
      \tag{0.8}
    \]

    where \(\vartheta(x)=\{e^{x^2}\}\).  For positive standard weights
    the integral is positive.  Thus the target \(\mathcal Q_I=o(W)\)
    asks for cancellation to additive accuracy \(o(W)\) around a
    baseline of order \(W\sqrt m\).

The two-seed identity in
`MATH_THEOREM_TWO_SEED_COMPONENT_MIXING_20260726.md` is correct.  In the
notation of that report, the quantities in (0.3) are \(A_2=A/4\) and
\(V_2=V/4\), so (0.4) is exactly its equation (3.7).  The genuinely new
information here is the multi-seed physical overlay theorem, the two
nonnegative reservoirs (0.6), the rigidity formula (0.7), the exact
orbit-total decomposition, and the annular baseline (0.8).

This theorem does not construct seeds satisfying the near-saturated Gram
condition.  It proves the exact condition and a statewise no-go for every
overlay whose orbit-mass transport is too small.

---

## 1. Floor-corrected energy on a fixed annulus

At lower depth \(q\), let

\[
 \mathcal X_q=\binom{[n]}{m-q},
 \qquad
 N_q=|\mathcal X_q|,
 \qquad
 \lambda_q={W\over N_q}=c_q+\theta_q,
 \tag{1.1}
\]

where \(c_q\in\mathbb Z_{\ge1}\) and \(0\le\theta_q<1\).  An exact
factor \(F\) has an integral load vector

\[
 \mu_q^F\in\mathbb Z_{\ge0}^{\mathcal X_q},
 \qquad
 \sum_{T\in\mathcal X_q}\mu_q^F(T)=W.
 \tag{1.2}
\]

Put

\[
 f_q^F=\mu_q^F-\lambda_q\mathbf1.
 \tag{1.3}
\]

Let \(w_q>0\) be prescribed weights.  Throughout a fixed Gaussian
annulus the standard choices

\[
 w_q=1,
 \qquad w_q={1\over c_q},
 \qquad w_q={1\over c_q(c_q+1)}
 \tag{1.4}
\]

are bounded above and below by positive constants depending only on
\(a,b\).  Define

\[
 \|z\|_I^2=\sum_{q\in I_m}w_q\|z_q\|_2^2,
 \tag{1.5}
\]

\[
 B_I=\sum_{q\in I_m}w_qN_q\theta_q(1-\theta_q),
 \tag{1.6}
\]

and

\[
 \mathcal Q_I(F)=\|f^F\|_I^2-B_I.
 \tag{1.7}
\]

The upper shadows may be included by taking a second isomorphic copy of
each \(\mathcal X_q\).  Every identity below then holds after summing over
the two signs; with equal weights the right side of (1.6) and the constant
in (0.8) are simply doubled.

### Lemma 1.1 (exact scalar floor identity)

For every integral load vector satisfying (1.2),

\[
 \boxed{
 \|f_q^F\|_2^2-N_q\theta_q(1-\theta_q)
 =Q_q(F):=\sum_{T\in\mathcal X_q}
  (\mu_q^F(T)-c_q)(\mu_q^F(T)-c_q-1).}
 \tag{1.8}
\]

Every summand on the right is a nonnegative even integer.  It vanishes
exactly at loads \(c_q,c_q+1\).  Consequently

\[
 \boxed{
 \mathcal Q_I(F)=\sum_{q\in I_m}w_qQ_q(F)\ge0.}
 \tag{1.9}
\]

#### Proof

Writing \(\lambda=c+\theta\), direct expansion and
\(\sum_T\mu(T)=N\lambda\) give

\[
\begin{aligned}
 \sum_T(\mu(T)-\lambda)^2-N\theta(1-\theta)
 &=\sum_T\mu(T)^2-(2c+1)\sum_T\mu(T)+Nc(c+1)\\
 &=\sum_T(\mu(T)-c)(\mu(T)-c-1).
\end{aligned}
\]

The product of two consecutive integers is nonnegative and even.  Its
only integer zeros are \(c,c+1\).  Summing with weights proves (1.9).
\(\square\)

In particular, if the weights are bounded below by \(w_*>0\), then

\[
 \#\{(q,T):\mu_q^F(T)\notin\{c_q,c_q+1\}\}
 \le {\mathcal Q_I(F)\over2w_*}.
 \tag{1.10}
\]

Thus \(\mathcal Q_I=o(W)\) means that only \(o(W)\) cells are outside
their floor pair, even though the annulus contains \(\Theta(W\sqrt m)\)
target-depth cells.

---

## 2. Exact Gaussian accounting

### Lemma 2.1 (uniform load asymptotic)

Uniformly for \(0\le q\le b\sqrt m+1\),

\[
 \lambda_q=\prod_{j=0}^{q-1}{m+2+j\over m-j},
 \tag{2.1}
\]

and

\[
 \boxed{
 \log\lambda_q={q(q+1)\over m}+O_b(m^{-1}).}
 \tag{2.2}
\]

Consequently, with \(x_q=q/\sqrt m\),

\[
 \boxed{
 \lambda_q=e^{x_q^2}\left(1+{x_q\over\sqrt m}
                    +O_b(m^{-1})\right),
 \qquad
 {N_q\over W}=e^{-x_q^2}(1+O_b(m^{-1/2})).}
 \tag{2.3}
\]

#### Proof

The ratio formula for binomial coefficients gives (2.1).  For
\(j\le b\sqrt m+1\), expand to third order:

\[
\begin{aligned}
 \log\left(1+{j+2\over m}\right)
 -\log\left(1-{j\over m}\right)
 ={}&{2j+2\over m}-{2j+2\over m^2}\\
 &+{(j+2)^3+j^3\over3m^3}
   +O_b\left({(j+2)^4\over m^4}\right).
\end{aligned}
\tag{2.4}
\]

The first terms sum to \(q(q+1)/m\).  The remaining displayed sums are
respectively \(O_b(m^{-1})\), \(O_b(m^{-1})\), and
\(O_b(m^{-3/2})\).  This proves (2.2).  Since
\(q(q+1)/m=x_q^2+x_q/\sqrt m\), exponentiation gives (2.3).
\(\square\)

Put

\[
 \vartheta(x)=e^{x^2}-\lfloor e^{x^2}\rfloor.
 \tag{2.5}
\]

There are only finitely many threshold points
\(\sqrt{\log k}\in[a,b]\).  Away from them,

\[
 c_q\longrightarrow\lfloor e^{x^2}\rfloor,
 \qquad
 \theta_q\longrightarrow\vartheta(x)
 \quad\hbox{when }q/\sqrt m\to x.
 \tag{2.6}
\]

The \(O(1)\) lattice points near each threshold do not affect a normalized
Riemann sum.

### Theorem 2.2 (Gaussian floor baseline)

Suppose \(w_q\) is uniformly bounded and, away from the finitely many
thresholds,

\[
 w_q\longrightarrow\omega(x)
 \quad\hbox{whenever }q/\sqrt m\to x,
 \tag{2.7}
\]

where \(\omega\) is Riemann integrable.  Then

\[
 \boxed{
 {B_I\over W\sqrt m}
 \longrightarrow
 \beta_{a,b}(\omega)
 :=\int_a^b\omega(x)e^{-x^2}
          \vartheta(x)(1-\vartheta(x))\,dx.}
 \tag{2.8}
\]

Also

\[
 \boxed{
 {1\over W\sqrt m}\sum_{q\in I_m}N_q
 \longrightarrow\int_a^be^{-x^2}\,dx.}
 \tag{2.9}
\]

For the three weights in (1.4), respectively,

\[
 \omega(x)=1,
 \quad
 {1\over\lfloor e^{x^2}\rfloor},
 \quad
 {1\over\lfloor e^{x^2}\rfloor
          (\lfloor e^{x^2}\rfloor+1)}.
 \tag{2.10}
\]

If \(\omega\) is positive almost everywhere, then
\(\beta_{a,b}(\omega)>0\).

#### Proof

Divide (1.6) by \(W\), use (2.3), and apply bounded Riemann-sum
convergence.  The integrand in (2.8) tends to zero on both sides of every
integer threshold, so the floor jumps cause no difficulty.  Formula
(2.9) is the same argument without the floor factor.  The fractional part
\(\vartheta(x)\) is strictly between zero and one except at finitely many
points, proving positivity. \(\square\)

It follows that a proof of \(\mathcal Q_I=o(W)\) must match a centered
energy of order \(W\sqrt m\) to its exact integer baseline with additive
error \(o(W)\).  A fixed-factor multiplicative estimate which leaves a
constant fraction of the baseline cannot suffice.

---

## 3. The physical \(r\)-seed owner overlay

Let \(F^1,\ldots,F^r\) be arbitrary literal exact middle-wreath factors
on the same coordinate set.  In seed \(i\), let \(R_i(X)\) denote the
unique wreath row owning the middle set \(X\in\binom{[n]}m\).

Form an \(r\)-partite hypergraph \(\mathfrak H\).  Its vertices are all
rows of all seeds, with the seed as the part label.  For every middle set
\(X\), put one hyperedge

\[
 \{R_1(X),\ldots,R_r(X)\}.
 \tag{3.1}
\]

Let \(\mathcal K\) be its connected components.  If \(K\in\mathcal K\),
write \(R_{K,i}\) for its rows on shore \(i\), and \(\Omega_K\) for its
middle-set hyperedges.

### Theorem 3.1 (literal multi-seed component choices)

For every component \(K\) and every seed shore \(i\),

\[
 \boxed{n|R_{K,i}|=|\Omega_K|.}
 \tag{3.2}
\]

For every choice map \(\iota:\mathcal K\to[r]\),

\[
 F_{\iota}=\bigcup_{K\in\mathcal K}R_{K,\iota(K)}
 \tag{3.3}
\]

is a literal exact middle-wreath factor.

#### Proof

Every row in an exact factor owns exactly \(n\) middle sets.  If a row
belongs to a component, all incident hyperedges belong to that component.
Conversely every hyperedge of \(\Omega_K\) has exactly one endpoint on
shore \(i\).  Double counting the incidences between \(R_{K,i}\) and
\(\Omega_K\) proves (3.2).

Fix \(X\in\Omega_K\).  Its unique owner on shore \(\iota(K)\) belongs to
the union (3.3), while no row chosen from another component owns \(X\).
Thus every middle set is owned exactly once.  All selected objects are
complete original wreath rows, so (3.3) is a literal exact factor.
\(\square\)

At depth \(q\), let \(u_{K,i,q}\) be the target-load vector contributed
by \(R_{K,i}\).  Then

\[
 \mu_q^{F^i}=\sum_Ku_{K,i,q}.
 \tag{3.4}
\]

Each shore of \(K\) has the same number of rows.  Hence

\[
 \sum_Tu_{K,i,q}(T)=n|R_{K,i}|
 \tag{3.5}
\]

is independent of \(i\).  Moreover every cyclic row has exactly
\(m-q\) depth-\(q\) intervals containing a fixed coordinate.  Therefore
the point margins of \(u_{K,i,q}\) are also independent of \(i\).  Every
component difference

\[
 u_{K,i,q}-u_{K,j,q}
 \tag{3.6}
\]

has zero total and zero point margins; in Johnson language it lies in
\(\bigoplus_{d\ge2}U_d\).  This is a physical fact, not a relabeling
assumption.

---

## 4. Exact Gram and covariance identities

Choose a random shore \(I_K\in[r]\) in every component, under an
arbitrary joint law.  Put

\[
 Y_K=u_{K,I_K},
 \qquad
 \bar u_K=\mathbb EY_K,
 \qquad
 \bar f=\sum_K\bar u_K-\lambda\mathbf1,
 \tag{4.1}
\]

where all depths in the annulus are stacked in the Hilbert space (1.5).

### Theorem 4.1 (general physical overlay identity)

\[
 \boxed{
 \mathbb E\mathcal Q_I(F_{\boldsymbol I})
  =\|\bar f\|_I^2-B_I+
    \sum_{K,L}\mathbb E
       \langle Y_K-\bar u_K,Y_L-\bar u_L\rangle_I.}
 \tag{4.2}
\]

The double sum is

\[
 \mathbb E\left\|\sum_K(Y_K-\bar u_K)\right\|_I^2\ge0.
 \tag{4.3}
\]

If the component choices are independent, every off-diagonal term
vanishes and

\[
 \boxed{
 \mathbb E\mathcal Q_I(F_{\boldsymbol I})
  =\|\bar f\|_I^2-B_I+
    \sum_K\mathbb E\|Y_K-\bar u_K\|_I^2.}
 \tag{4.4}
\]

#### Proof

Every outcome is exact by Theorem 3.1, and its centered load is

\[
 f=\bar f+\sum_K(Y_K-\bar u_K).
\]

Expand its squared norm and take expectations.  The linear term vanishes.
Subtract the deterministic baseline \(B_I\).  Independence kills every
off-diagonal covariance, proving (4.4). \(\square\)

Now take uniform one-seed marginals:

\[
 \Pr(I_K=i)={1\over r}
 \quad(K\in\mathcal K,\ i\in[r]).
 \tag{4.5}
\]

Set

\[
 \bar u_K={1\over r}\sum_i u_{K,i},
 \qquad
 \delta_{K,i}=u_{K,i}-\bar u_K,
 \tag{4.6}
\]

\[
 \bar f={1\over r}\sum_i f^i,
 \tag{4.7}
\]

and define

\[
 A_r={1\over r}\sum_i
        \left\|\sum_K\delta_{K,i}\right\|_I^2,
 \qquad
 V_r={1\over r}\sum_{K,i}\|\delta_{K,i}\|_I^2.
 \tag{4.8}
\]

The standard vector-variance identity gives both pairwise forms in (0.3).

### Corollary 4.2 (multi-seed heat and cross-Gram identity)

For independent uniform shores,

\[
 \boxed{
 \mathbb E\mathcal Q_I(F_{\boldsymbol I})
 ={1\over r}\sum_i\mathcal Q_I(F^i)-(A_r-V_r).}
 \tag{4.9}
\]

Furthermore

\[
 \boxed{
 A_r-V_r={2\over r}
  \sum_{K<L}\sum_{i=1}^r
       \langle\delta_{K,i},\delta_{L,i}\rangle_I.}
 \tag{4.10}
\]

Thus independent component heat contracts the mean seed deficiency by
exactly the positive coherent cross-component Gram mass.  Negative or
zero total cross-Gram gives no contraction.

If the shores have uniform marginals but are correlated, let

\[
 C_r=\sum_{K\ne L}\mathbb E
       \langle\delta_{K,I_K},\delta_{L,I_L}\rangle_I.
 \tag{4.11}
\]

Then the exact extension is

\[
 \boxed{
 \mathbb E\mathcal Q_I(F_{\boldsymbol I})
 ={1\over r}\sum_i\mathcal Q_I(F^i)-A_r+V_r+C_r.}
 \tag{4.12}
\]

Negative cross-component covariance is therefore a genuine escape from
independent-shore variance.

#### Proof

The average seed centered energy is

\[
 {1\over r}\sum_i\|f^i\|_I^2=\|\bar f\|_I^2+A_r.
 \tag{4.13}
\]

For independent shores the covariance term in (4.4) is \(V_r\).  Subtract
the same \(B_I\) from (4.13) and (4.4), proving (4.9).  Expanding the
squared sums in \(A_r\) proves (4.10).  Keeping the off-diagonal terms in
(4.2) proves (4.12). \(\square\)

At Gaussian scale, the exact independent-shore target is therefore

\[
 \boxed{
 A_r-V_r={1\over r}\sum_i\mathcal Q_I(F^i)-o(W).}
 \tag{4.14}
\]

A mere inequality \(A_r\ge(1+\eta)V_r\) is not enough unless it also
supplies the near-saturation (4.14).  For correlated uniform marginals,
replace the left side by \(A_r-V_r-C_r\).

---

## 5. The convex-envelope floor reservoirs

The global Gram formula conceals two separately nonnegative terms.  We
now expose them.

### Lemma 5.1 (minimum variance of an integer random variable)

If \(X\) is integer-valued and \(p=\mathbb EX\), then

\[
 \boxed{
 \operatorname {Var}X\ge\{p\}(1-\{p\}).}
 \tag{5.1}
\]

Equality holds exactly when

\[
 X\in\{\lfloor p\rfloor,\lceil p\rceil\}
 \quad\hbox{almost surely}. 
 \tag{5.2}
\]

#### Proof

Put \(a=\lfloor p\rfloor\).  The integer polynomial
\((X-a)(X-a-1)\) is nonnegative.  Taking expectations and using
\(p=a+\{p\}\) gives

\[
 \mathbb E(X-p)^2-\{p\}(1-\{p\})
 =\mathbb E[(X-a)(X-a-1)]\ge0.
\]

Equality in the nonnegative integer polynomial occurs exactly at
\(X=a,a+1\). \(\square\)

The function

\[
 \ell_\lambda(p)=(p-\lambda)^2+\{p\}(1-\{p\})
 \tag{5.3}
\]

is the lower convex envelope, on the integer lattice, of
\(x\mapsto(x-\lambda)^2\).  On every interval \([j,j+1]\) it is affine,
and its slopes increase by two at successive integers.  Hence it is
convex.

### Theorem 5.2 (exact mean and rounding reservoirs)

Fix a depth \(q\).  For any random exact factor arising from any overlay
law, let

\[
 X_T=\mu_q(T),
 \qquad
 p_T=\mathbb EX_T.
 \tag{5.4}
\]

Then (0.6) holds, and its two displayed terms are nonnegative.

If \(0<\theta_q<1\), then

\[
 \mathcal R_q^{\rm mean}=0
 \quad\Longleftrightarrow\quad
 p_T\in[c_q,c_q+1]quad\hbox{for every }T.
 \tag{5.5}
\]

If \(\theta_q=0\), equality holds exactly when \(p_T=c_q\) for every
target.  Moreover

\[
 \mathcal R_q^{\rm round}=0
 \quad\Longleftrightarrow\quad
 X_T\in\{\lfloor p_T\rfloor,\lceil p_T\rceil\}
 \quad\hbox{a.s. for every }T.
 \tag{5.6}
\]

#### Proof

For one target,

\[
 \mathbb E(X_T-\lambda_q)^2
  =(p_T-\lambda_q)^2+\operatorname {Var}X_T.
 \tag{5.7}
\]

Every outcome has total load \(W\), so
\(\sum_Tp_T=N_q\lambda_q\).  Summing (5.7), subtracting the floor
baseline, and adding and subtracting
\(\{p_T\}(1-\{p_T\})\) proves (0.6).

The rounding term is nonnegative by Lemma 5.1.  Jensen's inequality gives

\[
 {1\over N_q}\sum_T\ell_{\lambda_q}(p_T)
 \ge\ell_{\lambda_q}\left({1\over N_q}\sum_Tp_T\right)
 =\ell_{\lambda_q}(\lambda_q)
 =\theta_q(1-\theta_q),
\]

so the mean term is nonnegative.  If \(0<\theta_q<1\), the maximal affine
interval of \(\ell_{\lambda_q}\) containing \(\lambda_q\) is
\([c_q,c_q+1]\), giving (5.5).  At an integer \(\lambda_q=c_q\), the
function has a strict corner, and equality forces every \(p_T=c_q\).
Lemma 5.1 gives (5.6). \(\square\)

Combining Theorems 4.1 and 5.2 gives the exact identity

\[
 \boxed{
 \|\bar f\|_I^2-B_I+
 \mathbb E\|f-\bar f\|_I^2
 =\sum_{q\in I_m}w_q
   (\mathcal R_q^{\rm mean}+\mathcal R_q^{\rm round}).}
 \tag{5.8}
\]

Thus a probability law supported on physical overlay children has
expected deficiency \(o(W)\) if and only if both aggregate reservoirs in
(5.8) are \(o(W)\).  If this holds, at least one literal exact child has
\(\mathcal Q_I=o(W)\).

### Corollary 5.3 (exact fair-binary rigidity)

Consider two seeds, and choose every component shore independently and
fairly.  At a target-depth cell put

\[
 d_K=u_{K,1}(T)-u_{K,0}(T)\in\mathbb Z.
 \tag{5.9}
\]

Then (0.7) is the exact contribution of this cell to
\(\mathcal R_q^{\rm round}\).  It is zero exactly for the following two
patterns:

\[
 d_K=0\quad\hbox{for every }K,
 \tag{5.10}
\]

or

\[
 d_{K_0}=1\hbox{ or }-1\quad\hbox{for one }K_0,
 \qquad d_K=0\quad(K\ne K_0).
 \tag{5.11}
\]

Every other pattern contributes at least \(1/2\).

#### Proof

The random load is

\[
 X=p+{1\over2}\sum_K\varepsilon_Kd_K,
 \qquad
 p={1\over2}\sum_K(u_{K,0}(T)+u_{K,1}(T)),
 \tag{5.12}
\]

with independent fair signs.  Hence

\[
 \operatorname {Var}X={1\over4}\sum_Kd_K^2.
 \tag{5.13}
\]

The parity of \(2p\) is the parity of \(\sum_Kd_K\).  Therefore

\[
 \{p\}(1-\{p\})
 ={1\over4}\mathbf1_{\{\sum_Kd_K\ {\rm odd}\}},
\]

which proves (0.7).  If the expression is nonzero, its numerator is a
positive even integer: modulo two,
\(\sum_Kd_K^2\equiv\sum_Kd_K\).  Its minimum is therefore two, giving
the lower bound \(1/2\).  Equality zero requires sum of squares zero, or
sum of squares one with odd total, exactly (5.10)--(5.11). \(\square\)

If \(w_*=\min_{q\in I_m}w_q>0\), define a cell to be **complex** when it
does not have one of the forms (5.10)--(5.11).  Then

\[
 \boxed{
 \mathbb E\mathcal Q_I
 \ge {w_*\over2}\,#\{\hbox{complex target-depth cells}\}.}
 \tag{5.14}
\]

Consequently an overlay having \(\Omega(W)\) complex cells cannot prove
expected deficiency \(o(W)\) by independent fair switching.  This is not
the refuted single-relabeling heat argument: it applies to arbitrary
unrelated exact seeds and follows solely from integer component effects.
It does not obstruct correlated shore laws, for which the independent
variance (5.13) is replaced by the full covariance in (4.2).

More generally, if independent integer component variables sum to a
random variable supported on two consecutive integers, then all but at
most one component variable are deterministic, and the remaining one is
supported on two consecutive integers.  Indeed, the diameter of the
support of a Minkowski sum is the sum of the support diameters.  This is
the multi-shore equality form of the same rounding reservoir.

---

## 6. Exact orbit-total and within-orbit decomposition

For each depth \(q\), fix an arbitrary partition
\(\mathscr O_q\) of \(\mathcal X_q\).  The intended examples are the
target orbits of a finite-order coordinate permutation or a finite
coordinate group, but no symmetry is needed.

Let \(O\in\mathscr O_q\), put \(d=|O|\), and for an integral load vector
\(\mu\) define

\[
 T_O=\sum_{S\in O}\mu(S),
 \qquad
 a_O=\left\lfloor{T_O\over d}\right\rfloor,
 \qquad
 b_O=T_O-da_O.
 \tag{6.1}
\]

Define the orbit-total floor penalty

\[
\begin{aligned}
 \Psi_{c,d}(T)
 &:=(d-b)(a-c)(a-c-1)
      +b(a+1-c)(a-c)\\
 &=d(a-c)(a-c-1)+2b(a-c),
\end{aligned}
 \tag{6.2}
\]

where \(a=\lfloor T/d\rfloor\) and \(b=T-da\).

### Theorem 6.1 (orbit-mass floor decomposition)

For every integral target load,

\[
 \boxed{
 Q_q(\mu)=
 \sum_{O\in\mathscr O_q}\Psi_{c_q,|O|}(T_O)
 +\sum_{O\in\mathscr O_q}\sum_{S\in O}
      (\mu(S)-a_O)(\mu(S)-a_O-1).}
 \tag{6.3}
\]

Both terms on the right are nonnegative.  The first is the exact minimum
of \(Q_q\) among all nonnegative integral vectors with the prescribed
orbit totals.  Hence

\[
 \boxed{
 Q_q(\mu)=0
 \quad\Longleftrightarrow\quad
 \begin{cases}
 c_q|O|\le T_O\le(c_q+1)|O|&\text{for every }O,\\
 \mu(S)\in\{a_O,a_O+1\}&\text{inside every }O.
 \end{cases}}
 \tag{6.4}
\]

#### Proof

For fixed \(T\), the sum of squares of \(d\) integers is minimized when
they differ by at most one, namely at \(d-b\) copies of \(a\) and \(b\)
copies of \(a+1\).  Evaluating
\((x-c)(x-c-1)\) there gives (6.2).

More directly, subtract the value in (6.2) from
\(\sum_{S\in O}(\mu(S)-c)(\mu(S)-c-1)\).  The linear terms cancel because
\(\sum_{S\in O}\mu(S)=T\), and the result is exactly

\[
 \sum_{S\in O}(\mu(S)-a)(\mu(S)-a-1).
\]

This proves (6.3) and nonnegativity.  The zero characterization follows
from the integer zeros of the two consecutive-factor polynomials.
\(\square\)

For the physical overlay of Section 3, put

\[
 t_{K,i}(O)=\sum_{S\in O}u_{K,i,q}(S).
 \tag{6.5}
\]

The orbit total of the child \(F_\iota\) is exactly

\[
 \boxed{T_O(F_\iota)=\sum_Kt_{K,\iota(K)}(O).}
 \tag{6.6}
\]

Thus the nonlinear first term of (6.3) is an explicit finite
orbit-mass scheduling problem on the same component variables.

### Corollary 6.2 (statewise invariant-orbit obstruction)

Suppose

\[
 t_{K,i}(O)\quad\hbox{is independent of }i
 \tag{6.7}
\]

for every \(q,O,K\).  Then every physical child has the same orbit totals.
If

\[
 \sum_{q\in I_m}w_q\sum_{O\in\mathscr O_q}
       \Psi_{c_q,|O|}(T_O)\ge\gamma W
 \tag{6.8}
\]

for some fixed \(\gamma>0\), then

\[
 \boxed{\mathcal Q_I(F_\iota)\ge\gamma W}
 \tag{6.9}
\]

for every component choice \(\iota\), independent or correlated.

This recovers the finite-order diagonal-relabeling floor: a shore and its
coordinate-permuted shore have the same mass on every orbit of that
permutation.  Unrelated seeds evade this conclusion only when (6.7)
fails.

There is a quantitative transport version.  Put

\[
 J_{c,d}=[cd,(c+1)d]
 \tag{6.10}
\]

and note from (6.2), or from its successive discrete slopes, that

\[
 \boxed{
 \Psi_{c,d}(T)\ge2\operatorname {dist}(T,J_{c,d}).}
 \tag{6.11}
\]

Fix reference orbit totals \(T_O^0\), and define

\[
 D_0=\sum_{q\in I_m}w_q\sum_O
       \operatorname {dist}(T_O^0,J_{c_q,|O|}),
 \tag{6.12}
\]

\[
 R=\max_\iota\sum_{q\in I_m}w_q\sum_O
       |T_O(F_\iota)-T_O^0|.
 \tag{6.13}
\]

Since distance to an interval is one-Lipschitz, every child obeys

\[
 \boxed{
 \mathcal Q_I(F_\iota)\ge2(D_0-R).}
 \tag{6.14}
\]

Therefore a reference linear orbit imbalance \(D_0=\Omega(W)\) cannot be
repaired by a multi-seed overlay with orbit-mass transport \(R=o(W)\).
This is an exact statewise obstruction, with no heat-bath or averaging
hypothesis.

---

## 7. Orbit projection of the cross-Gram

The orbit-mass condition also has a linear Hilbert-space shadow.  Let
\(P_{\mathscr O}\) average a vector on every orbit.  Then

\[
 \boxed{
 \|P_{\mathscr O}z\|_I^2
 =\sum_{q\in I_m}w_q\sum_{O\in\mathscr O_q}
     {1\over|O|}\left(\sum_{S\in O}z_q(S)\right)^2.}
 \tag{7.1}
\]

For the uniform \(r\)-seed overlay, set

\[
 \bar t_K(O)={1\over r}\sum_i t_{K,i}(O),
 \qquad
 d_{K,i}(O)=t_{K,i}(O)-\bar t_K(O).
 \tag{7.2}
\]

The orbit-sector contribution to the cross-Gram (4.10) is exactly

\[
 \boxed{
 (A_r-V_r)_{\rm orb}
 ={2\over r}\sum_{K<L}\sum_i\sum_{q,O}
   {w_q\over|O|}d_{K,i}(O)d_{L,i}(O).}
 \tag{7.3}
\]

The complementary within-orbit sector has the identical formula with
\(I-P_{\mathscr O}\), and the two add orthogonally.  Condition (6.7) is
equivalent to \(d_{K,i}(O)=0\) throughout, in which case the overlay has
zero Gram action on every orbit-constant direction.  Merely changing
orbit masses is not enough: (7.3) shows that independent heat needs those
changes to have positive coherent cross-component sign.  Conversely,
large positive (7.3) does not by itself settle the nonlinear floor;
Theorem 6.1 requires the attained totals to enter their exact intervals
\(J_{c_q,|O|}\).

Combining Sections 4--7 gives the promised necessary-and-sufficient
formulation for a prescribed overlay law:

\[
\boxed{
\begin{aligned}
 \mathbb E\mathcal Q_I=o(W)
 \quad\Longleftrightarrow\quad&
 \|\bar f\|_I^2+\mathbb E\|f-\bar f\|_I^2
       =B_I+o(W)\\
 \quad\Longleftrightarrow\quad&
 \sum_qw_q(\mathcal R_q^{\rm mean}
             +\mathcal R_q^{\rm round})=o(W)\\
 \quad\Longleftrightarrow\quad&
 \mathbb E\sum_{q,O}w_q\left[
      \Psi_{c_q,|O|}(T_O)+Q_{a_O}(\mu|_O)
                              \right]=o(W).
\end{aligned}}
\tag{7.4}
\]

All terms in the second and third lines are nonnegative.  Hence no
cancellation is hidden in either equivalence.

---

## 8. Audit of the earlier two-seed theorem

Take \(r=2\), let the two component shores be \(u_K,v_K\), and put
\(\Delta_K=v_K-u_K\).  The notation of
`MATH_THEOREM_TWO_SEED_COMPONENT_MIXING_20260726.md` is

\[
 A=\left\|\sum_K\Delta_K\right\|_I^2,
 \qquad
 V=\sum_K\|\Delta_K\|_I^2.
 \tag{8.1}
\]

Our normalized quantities are

\[
 A_2={A\over4},
 \qquad
 V_2={V\over4}.
 \tag{8.2}
\]

Substitution in (4.9) gives

\[
 \boxed{
 \mathbb E\mathcal Q_I(F_{\boldsymbol\varepsilon})
 ={\mathcal Q_I(F)+\mathcal Q_I(G)\over2}
  -{A-V\over4}.}
 \tag{8.3}
\]

This is exactly equation (3.7) of the earlier report.  The floor baseline
is seed-independent and was subtracted with the correct coefficient.  Its
midpoint form

\[
 \mathbb E\mathcal Q_I
 =\left\|{f^F+f^G\over2}\right\|_I^2
   +{V\over4}-B_I
 \tag{8.4}
\]

is also correct.

The additional audit furnished by Theorem 5.2 is

\[
 {\mathcal Q_I(F)+\mathcal Q_I(G)\over2}
  -{A-V\over4}
 =\sum_{q\in I_m}w_q
   (\mathcal R_q^{\rm mean}+\mathcal R_q^{\rm round}),
 \tag{8.5}
\]

and Corollary 5.3 evaluates the second reservoir exactly.  Therefore the
two-seed theorem is not missing a coefficient, but its abstract
\(A-V\) criterion hides the stringent physical equality case required on
a Gaussian annulus.

---

## 9. Proved boundary

The following is now rigorous.

* Multi-seed connected owner components give legal integral exact-factor
  choices; there is no ownership relaxation in the theorem.
* Equations (4.2), (4.9), and (4.12) are the exact baseline-corrected
  drift laws for arbitrary, independent, and correlated shore laws.
* The expected floor defect is the sum of two nonnegative reservoirs.
  In a fair binary overlay, any target affected nontrivially by two
  components pays at least \(1/2\), unless all but one effects cancel by
  being literally zero; algebraic cancellation of their signed sum does
  not remove this variance charge.
* Orbit-total preservation gives the statewise obstruction (6.9), and
  insufficient orbit transport gives (6.14).
* The exact Gaussian floor baseline is (2.8), of order \(W\sqrt m\).

What is not proved is the existence of a physical family of unrelated
seeds for which (4.14), or its correlated form, holds.  A successful
construction must do both of the following through all
\(q\in[a\sqrt m,b\sqrt m]\):

1. transport any obstructing orbit totals into the intervals
   \([c_q|O|,(c_q+1)|O|]\) with only \(o(W)\) aggregate residual; and
2. realize floor-compatible target means with essentially
   one-residual-component rounding, or supply correlated component choices
   whose negative covariance replaces that rigidity.

This is the exact surviving physical overlay lemma.  It neither reuses nor
assumes the false single-relabeling heat-bath principle.
