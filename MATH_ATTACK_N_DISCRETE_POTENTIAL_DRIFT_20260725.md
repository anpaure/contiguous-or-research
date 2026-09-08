# New line N: positive discrete potentials and exact component drift

## 0. Verdict

Assume \(m\ge3\), as throughout the asymptotic exact-factor problem.

There is a positive separable discrete-convex potential that is strictly
more robust than quadratic collision energy and treats \(q=1\) without an
exception.

For an integer floor \(c\ge1\), define the capped factorial-entropy slope

\[
\sigma_c(t)
=
\operatorname{clip}_{[-1,1]}
\left(
\log\frac{t+1}{c+1}
\right),
\qquad t\in\mathbb Z_{\ge0},
\tag{0.1}
\]

and define \(\eta_c\) by

\[
\eta_c(c)=0,
\qquad
\eta_c(t+1)-\eta_c(t)=\sigma_c(t).
\tag{0.2}
\]

Then

\[
\eta_c(c)=\eta_c(c+1)=0,
\qquad
\eta_c(t)>0
\quad(t\notin\{c,c+1\}),
\]

and \(\eta_c\) is discretely convex and \(1\)-Lipschitz. If

\[
D_c(t)=\operatorname{dist}(t,\{c,c+1\}),
\qquad
Q_c(t)=(t-c)(t-c-1)=D_c(t)(D_c(t)+1),
\]

then, with

\[
\alpha_c=\log\frac{c+2}{c+1},
\]

\[
\boxed{
\alpha_cD_c(t)
\le
\eta_c(t)
\le
D_c(t),
\qquad
\eta_c(t)
\le
h_c(t)
\le
\frac{\log2}{2}Q_c(t).
}
\tag{0.3}
\]

where

\[
h_c(t)
=
\log(t!)
-\log(c!)
-(t-c)\log(c+1)
\tag{0.4}
\]

is the uncapped factorial-entropy chord defect.

For a fixed Gaussian window \(H_A=\lceil A\sqrt m\rceil\), the floors
\(c_q\) are bounded by a constant \(M_A\). Hence

\[
\alpha_A
:=
\log\frac{M_A+2}{M_A+1}
>0
\]

and the exact-factor potential

\[
\boxed{
\mathcal E_{H_A}(F)
=
\sum_{q=1}^{H_A}\frac1{c_q}
\sum_S\eta_{c_q}(\mu_q^F(S))
}
\tag{0.5}
\]

satisfies

\[
\boxed{
\alpha_A\mathcal C_{H_A}(F)
\le
\mathcal E_{H_A}(F)
\le
\mathcal C_{H_A}(F)
\le
2\mathcal O_{H_A}(F),
}
\tag{0.6}
\]

and

\[
\boxed{
\mathcal E_{H_A}(F)
\le
(\log2)\Psi_{H_A}(F),
}
\tag{0.7}
\]

where \(\mathcal C_H\) is the free-quota corridor,
\(\mathcal O_H\) the mobile overload, and \(\Psi_H\) the half
floor-collision energy. Thus \(\mathcal E_H\) is factorwise equivalent to
the unlabelled overload target on every fixed window, but has bounded
linear tails and curvature at most \(\log2\), rather than quadratic tails
and curvature \(1\) or \(2\).

At the troublesome first shadow,

\[
c_1=1,\qquad \theta_1=\frac2m,
\]

and

\[
\boxed{
\eta_1(0)=\log2,\quad
\eta_1(1)=\eta_1(2)=0,\quad
\eta_1(3)=\log\frac32,\quad
\eta_1(4)=\log3.
}
\tag{0.8}
\]

Holes and the first upper collision are both charged positively; no
\(q=1\) term is discarded.

There is also a genuine restricted one-component drift theorem. Let
\(F,G\) be exact factors, let
\(\mathcal K(F,G)=\{K_1,\ldots,K_k\}\) be their complete middle-ownership
overlay components oriented from \(F\) toward \(G\), and put

\[
g=\mathcal E_H(F)-\mathcal E_H(G)>0.
\]

For every retained load coordinate \(a=(q,S)\), let

\[
P_a=\sum_i(v_i(a))_+,
\qquad
N_a=\sum_i(-v_i(a))_+,
\]

where \(v_i\) is the load effect of switching \(K_i\). Define

\[
\boxed{
\overline{\mathfrak R}_H(F,G)
=
(\log2)
\sum_{q\le H}\frac1{c_q}\sum_S P_{q,S}N_{q,S}.
}
\tag{0.9}
\]

If

\[
g>\overline{\mathfrak R}_H(F,G),
\]

then some single complete ownership component is a legal integral switch
with

\[
\boxed{
\mathcal E_H(F)-\mathcal E_H(F_{K_i})
\ge
\frac{
g-\overline{\mathfrak R}_H(F,G)
}{k}
\ge
\frac{
g-\overline{\mathfrak R}_H(F,G)
}{\operatorname{Cat}_m}.
}
\tag{0.10}
\]

If the component effects are coordinatewise sign-coherent, then
\(\overline{\mathfrak R}_H=0\), so a single component improves by at
least \(g/k\). This condition includes every \(q\le H\), literally
including \(q=1\). It persists while original components are switched
toward \(G\); in at most \(k\) single-component moves one reaches \(G\),
a factor no worse than \(G\), or, in the general curvature regime, a
factor within the initial residue of \(G\).

This restricted theorem cannot be made into an unconditional fair
transposition drift theorem by convexity alone. For every coordinate
transposition \(\tau\),

\[
\mathcal E_H(\tau F)=\mathcal E_H(F).
\]

On the intrinsic \(\tau\)-cell, the potential is antipodally even in the
component signs. Every state-independent fair packet law has zero
cell-average drift, and every finite switch class contains a potential
minimum with no deterministic decreasing switch. These statements already
hold for the \(q=1\) potential alone.

Thus the new positive result is exact but restricted:

> A bounded-curvature entropy-Huber potential converts a better
> low-cancellation exact comparator into provable one-complete-component
> descent. The missing theorem is the construction of such a comparator,
> or an \(o(\mathcal E_H(F)-\mathcal E_H(G))\) cancellation residue.
> Convexity, entropy, and exact floor subtraction do not provide that
> structure automatically.

## 1. Exact-factor notation

Put

\[
n=2m+1,\qquad
W=\binom nm,\qquad
B=\frac Wn=\operatorname{Cat}_m.
\]

Throughout the report \(m\ge3\).

Let \(\mathfrak F_m\) be the finite set of exact middle wreath factors.
At depth \(q\), write

\[
r_q=m-q,\qquad
N_q=\binom n{r_q},
\qquad
\frac W{N_q}=c_q+\theta_q,
\tag{1.1}
\]

where

\[
c_q=\left\lfloor\frac W{N_q}\right\rfloor\ge1,
\qquad
0\le\theta_q<1.
\]

For \(F\in\mathfrak F_m\), let \(\mu_q^F(S)\) be its rank-\(r_q\)
interval load. Then

\[
\sum_S\mu_q^F(S)=W.
\tag{1.2}
\]

Put

\[
y_q^F(S)=\mu_q^F(S)-c_q.
\]

The two unconstrained integer-floor values are

\[
y_q^F(S)\in\{0,1\},
\quad\text{equivalently}\quad
\mu_q^F(S)\in\{c_q,c_q+1\}.
\]

Define the rankwise corridor and overload

\[
C_q(F)
=
\sum_S
\operatorname{dist}(\mu_q^F(S),\{c_q,c_q+1\}),
\tag{1.3}
\]

\[
O_q(F)
=
\max\left\{
\sum_S(c_q-\mu_q^F(S))_+,
\sum_S(\mu_q^F(S)-c_q-1)_+
\right\}.
\tag{1.4}
\]

Their weighted sums are

\[
\mathcal C_H(F)=\sum_{q\le H}\frac{C_q(F)}{c_q},
\qquad
\mathcal O_H(F)=\sum_{q\le H}\frac{O_q(F)}{c_q}.
\tag{1.5}
\]

The exact conservation identity gives

\[
\boxed{
\mathcal O_H(F)\le\mathcal C_H(F)\le2\mathcal O_H(F).
}
\tag{1.6}
\]

The half floor-collision energy is

\[
\boxed{
\Psi_H(F)
=
\frac12
\sum_{q\le H}\frac1{c_q}
\sum_S
(\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1).
}
\tag{1.7}
\]

It is nonnegative on integer loads and vanishes exactly on the two floor
values.

## 2. Full factorial entropy

For integers \(c,t\ge0\), define

\[
\boxed{
h_c(t)
=
\log\Gamma(t+1)
-\log\Gamma(c+1)
-(t-c)\log(c+1).
}
\tag{2.1}
\]

On integers this is (0.4). The affine slope \(\log(c+1)\) is uniquely
forced by the requirement

\[
h_c(c)=h_c(c+1)=0.
\]

### Lemma 2.1 — exact convexity and floor subtraction

\[
\boxed{
\Delta h_c(t)
:=
h_c(t+1)-h_c(t)
=
\log\frac{t+1}{c+1},
}
\tag{2.2}
\]

and

\[
\boxed{
\Delta^2h_c(t)
=
\log\frac{t+2}{t+1}>0.
}
\tag{2.3}
\]

Therefore \(h_c\) is strictly discretely convex on
\(\mathbb Z_{\ge0}\), has exactly the two zeros \(c,c+1\), and is positive
elsewhere.

#### Proof

Use

\[
\Gamma(t+2)=(t+1)\Gamma(t+1)
\]

in (2.1). The first difference is (2.2), and differencing once more gives
(2.3). Thus \(h_c\) decreases strictly until \(c\), is flat from \(c\) to
\(c+1\), and increases strictly thereafter. \(\square\)

For \(d\ge1\),

\[
\boxed{
h_c(c+1+d)
=
\sum_{j=1}^{d}
\log\left(1+\frac j{c+1}\right),
}
\tag{2.4}
\]

and, for \(1\le d\le c\),

\[
\boxed{
h_c(c-d)
=
\sum_{j=1}^{d}
\log\frac{c+1}{c+1-j}.
}
\tag{2.5}
\]

The first upper wall is

\[
h_c(c+2)=\log\frac{c+2}{c+1},
\tag{2.6}
\]

When \(c\ge1\), the first lower wall is

\[
h_c(c-1)=\log\frac{c+1}{c},
\tag{2.6a}
\]

which is larger than the upper wall.

### Theorem 2.2 — exact corridor and quadratic comparisons

Let

\[
D=D_c(t)=\operatorname{dist}(t,\{c,c+1\}),
\qquad
Q=Q_c(t)=(t-c)(t-c-1)=D(D+1),
\]

and

\[
\alpha_c=\log\frac{c+2}{c+1}.
\]

Then

\[
\boxed{
h_c(t)\ge\alpha_cD
}
\tag{2.7}
\]

for every \(t\ge0\), with equality at \(t=c+2\), and

\[
\boxed{
h_c(t)\le\frac{\log2}{2}Q
}
\tag{2.8}
\]

for every \(c,t\ge0\). The constant \(\log2/2\) is sharp, attained at
\((c,t)=(1,0)\) and also at \((0,2)\).

There is no positive constant \(\beta_c\) for which

\[
h_c(t)\ge\beta_cQ_c(t)
\]

holds for all \(t\): on the upper tail the ratio is
\(\asymp(\log t)/t\).

#### Proof

Every upper increment in (2.4) is at least \(\alpha_c\). When \(c\ge1\),
every lower increment in (2.5) is at least

\[
\log\frac{c+1}{c}>\alpha_c,
\]

which proves (2.7). For \(c=0\) there is no feasible lower side.

For the upper side, put

\[
a_j=\log\left(1+\frac j{c+1}\right).
\]

Since \(a_j/j\) decreases in \(j\),

\[
a_j\le ja_1\le j\log2.
\]

For the lower side,

\[
\log\frac{c+1}{c+1-j}
\le
\log(1+j)
\le
j\log2.
\]

Summing either side gives

\[
h_c(t)\le(\log2)\frac{D(D+1)}2.
\]

The equality and tail statements follow directly from (2.4)--(2.5).
\(\square\)

The exact reciprocal bracket

\[
\boxed{
c+1\le\alpha_c^{-1}\le c+2
}
\tag{2.9}
\]

follows from

\[
\frac1{c+2}
\le
\log\left(1+\frac1{c+1}\right)
\le
\frac1{c+1}.
\]

## 3. Capped factorial entropy

The full entropy still has \(t\log t\) upper tails. Cap its marginal cost,
not its value.

Define

\[
\boxed{
\sigma_c(t)
=
\max\left\{
-1,\,
\min\left\{
1,\log\frac{t+1}{c+1}
\right\}
\right\},
}
\tag{3.1}
\]

and let \(\eta_c\) be the unique integer function satisfying

\[
\eta_c(c)=0,
\qquad
\eta_c(t+1)-\eta_c(t)=\sigma_c(t).
\tag{3.2}
\]

### Theorem 3.1 — positive bounded-curvature floor potential

For every \(c\ge1\):

1. \(\eta_c(c)=\eta_c(c+1)=0\), and these are its only zeros;
2. \(\eta_c(t)>0\) at every other nonnegative integer;
3. \(\eta_c\) is discretely convex and \(1\)-Lipschitz;
4. its curvature obeys

   \[
   \boxed{
   0\le\Delta^2\eta_c(t)\le\log2;
   }
   \tag{3.3}
   \]

5. pointwise,

   \[
   \boxed{
   \alpha_cD_c(t)
   \le
   \eta_c(t)
   \le
   D_c(t),
   \qquad
   \eta_c(t)
   \le
   h_c(t)
   \le
   \frac{\log2}{2}Q_c(t).
   }
   \tag{3.4}
   \]

#### Proof

The uncapped slopes in (3.1) are strictly increasing in \(t\). Clipping
to an interval preserves monotonicity, proving discrete convexity, while
\(|\sigma_c|\le1\) proves Lipschitzness. Also

\[
\sigma_c(c)=0,
\]

all earlier slopes are negative, and all later slopes are positive. This
proves the zero and positivity statements.

The clipping map is \(1\)-Lipschitz, so

\[
\begin{aligned}
\Delta^2\eta_c(t)
&=\sigma_c(t+1)-\sigma_c(t)\\
&\le
\log\frac{t+2}{t+1}
\le\log2,
\end{aligned}
\]

which proves (3.3).

Every outward upper slope has magnitude at least
\(\alpha_c<1\). The closest lower slope has magnitude

\[
\log\frac{c+1}{c}>\alpha_c,
\]

and all farther lower slopes are larger in magnitude. Clipping at one
therefore leaves every outward marginal cost at least \(\alpha_c\), which
gives the lower bound in (3.4). Since \(|\sigma_c|\le1\) and the potential
vanishes at both floor points, summing outward slopes gives
\(\eta_c\le D_c\). Clipping can only reduce the magnitude of the outward
entropy increments, so \(\eta_c\le h_c\). The last inequality is
Theorem 2.2. \(\square\)

The cap one is not essential. It is chosen because it gives a universal
unit Lipschitz constant while leaving the first \(q=1\) walls unchanged.

## 4. Fixed-window exact-factor potential

Fix \(A>0\) and put

\[
H_A=\min\{m-1,\lceil A\sqrt m\rceil\}.
\]

For \(q\le H_A\),

\[
\frac W{N_q}
=
\prod_{j=0}^{q-1}
\left(1+\frac{2(j+1)}{m-j}\right).
\tag{4.1}
\]

Hence

\[
\log\frac W{N_q}
\le
\frac{q(q+1)}{m-q}.
\tag{4.2}
\]

For all sufficiently large \(m\), one may take, for example,

\[
\boxed{
M_A=\left\lceil e^{3(A+2)^2}\right\rceil
}
\tag{4.3}
\]

so that

\[
1\le c_q\le M_A
\qquad(q\le H_A).
\tag{4.4}
\]

Put

\[
\alpha_A=\log\frac{M_A+2}{M_A+1}>0
\tag{4.5}
\]

and define

\[
\boxed{
\mathcal E_{H_A}(F)
=
\sum_{q=1}^{H_A}\frac1{c_q}
\sum_S\eta_{c_q}(\mu_q^F(S)).
}
\tag{4.6}
\]

### Theorem 4.1 — robustness versus overload and collision

For every exact factor \(F\),

\[
\boxed{
\alpha_A\mathcal C_{H_A}(F)
\le
\mathcal E_{H_A}(F)
\le
\mathcal C_{H_A}(F),
}
\tag{4.7}
\]

\[
\boxed{
\alpha_A\mathcal O_{H_A}(F)
\le
\mathcal E_{H_A}(F)
\le
2\mathcal O_{H_A}(F),
}
\tag{4.8}
\]

and

\[
\boxed{
\mathcal E_{H_A}(F)
\le
(\log2)\Psi_{H_A}(F).
}
\tag{4.9}
\]

Consequently,

\[
\boxed{
\mathcal E_{H_A}(F)=o(W)
\iff
\mathcal O_{H_A}(F)=o(W).
}
\tag{4.10}
\]

Thus \(\mathcal E_H\) is an overload-equivalent replacement target with
bounded slope and curvature, while quadratic collision energy can
overcharge a single spike quadratically.

#### Proof

Equation (4.7) follows from the first pair of inequalities in (3.4),
(4.4), and the monotonic decrease of \(\alpha_c\) in \(c\). Combine it
with (1.6) to obtain (4.8).
Equation (4.9) follows by summing the last inequality in (3.4), noting the
factor \(1/2\) in (1.7). Equation (4.10) follows from (4.8). \(\square\)

### 4.1 The \(q=1\) mode

Exactly,

\[
N_1=\binom n{m-1},
\qquad
\frac W{N_1}=\frac{m+2}{m}=1+\frac2m.
\]

Thus

\[
c_1=1,\qquad\theta_1=\frac2m.
\tag{4.11}
\]

The slopes through \(t=3\) have magnitude below one, so the capped and
full entropy agree there. Directly,

\[
\boxed{
\eta_1(0)=\log2,\qquad
\eta_1(1)=\eta_1(2)=0,\qquad
\eta_1(3)=\log\frac32,\qquad
\eta_1(4)=\log3.
}
\tag{4.12}
\]

At \(q=1\), a hole \(\mu_1=0\) and a first upper collision
\(\mu_1=3\) each have corridor distance one and receive positive costs
\(\log2\) and \(\log(3/2)\), respectively.

## 5. Exact component-switch calculus

Let \(F,G\in\mathfrak F_m\). Cancel their common wreaths and let

\[
\mathcal K(F,G)=\{K_1,\ldots,K_k\}
\]

be the connected components of their complete middle-ownership overlay.
Orient each component from \(F\) toward \(G\). Let \(z_i\) be its
wreath-incidence effect and

\[
v_i=B_Hz_i
\]

its stacked retained load effect.

For every \(J\subseteq[k]\),

\[
F_J=F+\sum_{i\in J}z_i
\tag{5.1}
\]

is a genuine integral exact factor, and

\[
k\le|F\setminus G|\le B.
\tag{5.2}
\]

For a general separable potential

\[
\Theta_H(F)
=
\sum_{q\le H}w_q\sum_S\phi_q(\mu_q^F(S)),
\qquad
w_q>0,
\tag{5.3}
\]

put

\[
\Delta_i
=
\Theta_H(F_{\{i\}})-\Theta_H(F),
\qquad
g=\Theta_H(F)-\Theta_H(G).
\tag{5.4}
\]

At a load coordinate \(a=(q,S)\), define

\[
P_a=\sum_i(v_i(a))_+,
\qquad
N_a=\sum_i(-v_i(a))_+.
\tag{5.5}
\]

### Lemma 5.1 — exact curvature rectangle

Let \(\phi\) be discretely convex and let \(x,x-N,x+P\) be feasible
integer loads. Define

\[
\boxed{
\mathfrak R_\phi(x;P,N)
=
\phi(x+P)+\phi(x-N)-\phi(x)-\phi(x+P-N).
}
\tag{5.6}
\]

Then

\[
\boxed{
\mathfrak R_\phi(x;P,N)
=
\sum_{r=0}^{P-1}\sum_{s=1}^{N}
\Delta^2\phi(x+r-s)
\ge0,
}
\tag{5.7}
\]

with value zero if \(PN=0\).

#### Proof

For \(P,N>0\), telescope first in the positive direction and then in the
negative direction:

\[
\begin{aligned}
\mathfrak R_\phi(x;P,N)
&=
\sum_{r=0}^{P-1}
\left[
\Delta\phi(x+r)-\Delta\phi(x+r-N)
\right]\\
&=
\sum_{r=0}^{P-1}\sum_{s=1}^{N}
\Delta^2\phi(x+r-s).
\end{aligned}
\]

Discrete convexity proves nonnegativity. The boundary cases are immediate.
\(\square\)

Define the exact total rectangle

\[
\mathfrak R_\Theta(F,G)
=
\sum_{q,S}w_q
\mathfrak R_{\phi_q}
\left(
\mu_q^F(S);P_{q,S},N_{q,S}
\right).
\tag{5.8}
\]

### Theorem 5.2 — exact singleton ledger

For every separable discrete-convex \(\Theta_H\),

\[
\boxed{
\sum_{i=1}^k\Delta_i
\le
-g+\mathfrak R_\Theta(F,G).
}
\tag{5.9}
\]

Consequently, if

\[
g>\mathfrak R_\Theta(F,G),
\]

some single complete ownership component is a legal exact-factor switch
with

\[
\boxed{
\Theta_H(F)-\Theta_H(F_{\{i\}})
\ge
\frac{g-\mathfrak R_\Theta(F,G)}k.
}
\tag{5.10}
\]

#### Proof

At one coordinate, group all positive effects and all negative effects.
Same-sign superadditivity for a discrete-convex scalar function gives

\[
\sum_i[\phi(x+v_i)-\phi(x)]
\le
[\phi(x+P)-\phi(x)]
+
[\phi(x-N)-\phi(x)].
\]

By (5.6), the right side equals

\[
\phi(x+P-N)-\phi(x)+\mathfrak R_\phi(x;P,N).
\]

Sum over all coordinates with weights \(w_q\). The net endpoint is \(G\),
so its change is \(-g\), which proves (5.9). Averaging proves (5.10).
\(\square\)

The raw nonadditivity

\[
\operatorname{Can}_{\rm raw}(F,G)
:=
\sum_i\Delta_i-[\Theta_H(G)-\Theta_H(F)]
\tag{5.11}
\]

may be negative because same-sign curvature can be favorable. The exact
theorem is

\[
\operatorname{Can}_{\rm raw}(F,G)
\le
\mathfrak R_\Theta(F,G);
\]

the rectangle is a certified upper bound on harmful opposite-sign
cancellation, not always the exact loss.

### 5.1 Capped-entropy specialization

For \(\phi_q=\eta_{c_q}\), Theorem 3.1 gives

\[
0\le\Delta^2\phi_q\le\log2.
\]

With \(w_q=1/c_q\), define

\[
\boxed{
\overline{\mathfrak R}_H(F,G)
=
(\log2)
\sum_{q\le H}\frac1{c_q}
\sum_S P_{q,S}N_{q,S}.
}
\tag{5.12}
\]

Then

\[
\mathfrak R_{\mathcal E}(F,G)
\le
\overline{\mathfrak R}_H(F,G).
\tag{5.13}
\]

Combining (5.10), (5.13), and \(k\le B\) proves (0.10).

The literal \(q=1\) contribution is

\[
(\log2)
\sum_{S\in\binom{[n]}{m-1}}
P_{1,S}N_{1,S},
\tag{5.14}
\]

because \(c_1=1\). It is present with a positive coefficient.

For comparison, the full floor polynomial

\[
\phi_q(t)=(t-c_q)(t-c_q-1)
\]

has \(\Delta^2\phi_q=2\), while the half floor polynomial has curvature
one. Their corresponding rectangle ceilings are respectively

\[
2\sum_{q,S}\frac{P_{q,S}N_{q,S}}{c_q},
\qquad
\sum_{q,S}\frac{P_{q,S}N_{q,S}}{c_q}.
\tag{5.15}
\]

The capped entropy has the smaller universal curvature coefficient
\(\log2\).

## 6. Restricted fixed-window drift theorems

### Theorem 6.1 — sign-coherent one-component descent

Assume \(G\) improves \(F\) for a separable discrete-convex potential
\(\Theta_H\) by \(g>0\), and assume the component effects are
coordinatewise sign-coherent:

\[
\boxed{
v_i(q,S)v_j(q,S)\ge0
\quad
\text{for every }i,j,q,S.
}
\tag{6.1}
\]

Then some single complete ownership component satisfies

\[
\boxed{
\Theta_H(F)-\Theta_H(F_{\{i\}})
\ge
\frac gk
\ge
\frac gB.
}
\tag{6.2}
\]

This theorem includes every retained depth simultaneously, including
\(q=1\).

#### Proof

Condition (6.1) implies \(P_{q,S}N_{q,S}=0\) at every coordinate, so the
curvature rectangle vanishes. Apply Theorem 5.2. \(\square\)

If the component load supports are pairwise disjoint, the stronger exact
additivity

\[
\Theta_H(G)-\Theta_H(F)=\sum_i\Delta_i
\tag{6.3}
\]

holds. If \(G\) is a global minimizer, every \(\Delta_i\le0\): otherwise
switching precisely all negative-\(\Delta_i\) components would produce a
factor below the global minimum. Hence all strict components may be
switched in arbitrary order, and after they are exhausted the current
factor is already globally minimizing.

### Theorem 6.2 — persistent residue descent

Fix a comparator \(G\), and let

\[
\overline{\mathfrak R}_0
=
\sum_{q,S}w_qL_qP_{0,q,S}N_{0,q,S},
\tag{6.4}
\]

where

\[
0\le\Delta^2\phi_q\le L_q
\]

on every integer interval between the extremal partial loads
\(x_t-N_t\) and \(x_t+P_t\) encountered in the comparison.

Starting from \(F_0=F\), repeatedly switch one original
\(F/G\)-component supplied by Theorem 5.2 toward \(G\) whenever the current
gap

\[
g_t=\Theta_H(F_t)-\Theta_H(G)
\]

exceeds \(\overline{\mathfrak R}_0\). Then:

1. every step is a strict legal single-component descent;
2. at most \(k\) steps occur;
3. the terminal factor \(F_*\) satisfies

   \[
   \boxed{
   \Theta_H(F_*)
   \le
   \Theta_H(G)+\overline{\mathfrak R}_0.
   }
   \tag{6.5}
   \]

For the capped entropy, take

\[
L_q=\log2,
\qquad
w_q=\frac1{c_q},
\]

so (6.4) is exactly (5.12).

#### Proof

After switching an original component toward \(G\), it agrees with \(G\)
and cancels from the overlay. Every unswitched original component remains
a complete component with the same oriented load effect. Thus every
positive total \(P_{t,q,S}\) and negative total \(N_{t,q,S}\) is
nonincreasing, so the current rectangle envelope is at most
\(\overline{\mathfrak R}_0\).

If \(g_t>\overline{\mathfrak R}_0\), Theorem 5.2 supplies a strict
single-component descent. Each step removes at least one original
component, so at most \(k\) occur. If all components are switched, the
state is \(G\); otherwise the stopping condition gives (6.5). \(\square\)

In the sign-coherent case \(\overline{\mathfrak R}_0=0\), so a global
minimizer comparator is reached, or another global minimizer is reached
earlier, in at most \(k\le B\) single-component strict descents.

The substantive restricted-regime gate exposed by Theorem 6.2 is:

\[
\boxed{
\text{construct a better exact comparator }G
\text{ with }
\overline{\mathfrak R}_H(F,G)
=o\!\left(\mathcal E_H(F)-\mathcal E_H(G)\right).
}
\tag{6.6}
\]

Neither convexity nor exact floor subtraction proves this cancellation
condition.

## 7. Exact no-go for unrestricted transposition drift

The preceding theorems use an arbitrary better exact comparator. Intrinsic
coordinate-transposition cells have an additional symmetry that blocks
automatic drift.

Fix a coordinate transposition \(\tau\). Since the potential is
coordinate-invariant within each rank,

\[
\boxed{
\mathcal E_H(\tau F)=\mathcal E_H(F).
}
\tag{7.1}
\]

Thus switching all components from \(F\) to \(\tau F\) is a nontrivial
legal zero-drift packet whenever the cell is nontrivial.

Write an intrinsic cell as

\[
\mu(\varepsilon)
=
\bar\mu+\frac12\sum_{i=1}^k\varepsilon_i d_i,
\qquad
\varepsilon_i\in\{-1,+1\}.
\tag{7.2}
\]

Relabelling by \(\tau\) sends \(\varepsilon\) to \(-\varepsilon\).
Therefore

\[
\boxed{
V(\varepsilon)
:=
\mathcal E_H(F_\varepsilon)
\quad\text{satisfies}\quad
V(-\varepsilon)=V(\varepsilon).
}
\tag{7.3}
\]

Every Walsh coefficient on an odd component set vanishes. This evenness
uses only coordinate invariance; it applies to entropy and need not be
polynomial.

### Theorem 7.1 — fair-cell drift no-go

Let \(p\) be a state-independent probability law on component packets
\(J\subseteq[k]\), and define

\[
\mathfrak D_pV(\varepsilon)
=
\sum_Jp(J)[V(\varepsilon^J)-V(\varepsilon)].
\tag{7.4}
\]

Then

\[
\boxed{
2^{-k}\sum_\varepsilon\mathfrak D_pV(\varepsilon)=0.
}
\tag{7.5}
\]

If the supported flips generate the cube, \(V\) is nonconstant, and
\(\mathfrak D_pV\le0\) at every vertex, then a contradiction results.
Equivalently, a nonconstant cell has both favorable and unfavorable fair
drift vertices.

#### Proof

For every fixed packet \(J\), the map
\(\varepsilon\mapsto\varepsilon^J\) permutes the cube, so

\[
\sum_\varepsilon V(\varepsilon^J)
=
\sum_\varepsilon V(\varepsilon).
\]

Average over \(J\) to obtain (7.5). If every drift were nonpositive, it
would vanish everywhere. The finite maximum principle for the generating
flip graph would then force \(V\) to be constant. \(\square\)

The same obstruction holds globally. Any symmetric legal proposal kernel
is reversible with the uniform law on each finite communicating class.
More generally, for every reversible stationary law \(\pi\),

\[
\boxed{
\sum_F\pi(F)
\mathbb E[\mathcal E_H(F')-\mathcal E_H(F)\mid F]
=0.
}
\tag{7.6}
\]

Therefore no inequality of the form

\[
\mathbb E[\Delta\mathcal E_H\mid F]\le-a(F),
\qquad a(F)>0,
\]

can hold throughout a closed class.

Every communicating class also has a deterministic
\(\mathcal E_H\)-minimum with no decreasing legal switch. Proving that all
such minima have \(o(W)\) potential is the absolute class-selection theorem
one was trying to obtain, not a consequence of convexity.

### 7.1 Why \(q=1\) does not escape the no-go

The rank-\(m-1\) potential

\[
\mathcal E_1(F)
=
\sum_{S\in\binom{[n]}{m-1}}\eta_1(\mu_1^F(S))
\]

is itself coordinate-relabeling invariant. Hence (7.1)--(7.6) hold with
the retained depth set equal to \(\{1\}\). No cancellation from deeper
ranks is used.

Unconstrained convex minimization at \(q=1\) prefers exactly the loads

\[
\mu_1(S)\in\{1,2\},
\]

because their mean is \(1+2/m\). Whether the image of the exact-factor
fibre contains such a load vector is precisely the positive integral
balancing issue. Symmetry and local convex drift do not prove it.

## 8. Implication scope and surviving theorem

Unconditionally proved:

1. the full factorial-entropy floor defect, positivity, and exact
   comparisons (2.1)--(2.9);
2. the capped entropy-Huber potential with exact floor zero, bounded slope,
   and curvature at most \(\log2\) (3.1)--(3.4);
3. fixed-window equivalence with mobile overload and domination by
   quadratic collision energy (4.7)--(4.10);
4. exact positive charging of the \(q=1\) hole and first upper collision
   (4.11)--(4.12);
5. the curvature-rectangle singleton ledger (5.6)--(5.13);
6. one-complete-component descent in sign-coherent or small-residue
   comparator regimes (6.2)--(6.5); and
7. the exact intrinsic-cell, fair-chain, and \(q=1\) drift no-go
   (7.1)--(7.6).

Not proved:

1. existence of a better sign-coherent or low-residue comparator from an
   arbitrary exact factor;
2. \(\min_F\mathcal E_{H_A}(F)=o(W)\);
3. a low-\(\mathcal E_H\) minimum in every intrinsic switch class;
4. a universal favorable fair or deterministic transposition drift;
5. a bounded-size cancellation-connected macro-packet;
6. MWB, labelled common-owner synchronization, or a literal contiguous-OR
   word.

The strongest honest remaining gate in this lane is the low-residue
comparator statement (6.6), together with an absolute upper bound on the
comparator's potential. The new entropy-Huber potential reduces harmful
opposite-sign curvature from the quadratic coefficient \(1\) to at most
\(\log2\), keeps the exact integer floor and the \(q=1\) mode, and has
linear rather than quadratic tails. It does not manufacture the missing
comparator.

## 9. Independent audit checklist

The decisive constants and scopes were independently audited.

1. **Entropy algebra.** The forced chord slope, first and second
   differences, exact \(q=1\) values, sharp lower corridor coefficient
   \(\alpha_c\), and uniform upper coefficient \(\log2/2\) were checked
   separately.

2. **Capped curvature.** Clipping preserves monotonicity and cannot
   increase adjacent slope differences, giving
   \(0\le\Delta^2\eta_c\le\log2\). The fixed-window floor bound makes
   \(\alpha_A>0\), so no \(m\)-dependent comparison constant is hidden.

3. **Component ledger.** The rectangle indexing in (5.7), inequality
   direction in (5.9), divisor \(k\le\operatorname{Cat}_m\), literal
   \(q=1\) coefficient, and persistence after deleting switched components
   were checked independently.

4. **Scope.** Arbitrary-comparator ownership components were kept distinct
   from intrinsic transposition cells. Every asserted endpoint is an
   integral exact factor. The fair-drift no-go is not used against biased
   comparator-directed moves.

No finite or computational search, web input, or fractional-factor
surrogate is used.
