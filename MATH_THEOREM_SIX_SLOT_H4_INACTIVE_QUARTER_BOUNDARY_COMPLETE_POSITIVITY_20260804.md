# Six-slot `h=4`: complete positivity of the inactive quarter boundary

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical sign theorem.  It proves the
literal correlated rectangle gate strictly positive on the complete
inactive boundary `u=P/4`.  Together with the active-`Gamma` theorem, the
whole quarter boundary is closed.  No search or sampled computation is
used.

Put

\[
 A={\sqrt\pi\over2},
 \qquad
 F_\tau(w)=\sum_{q\ge0}K(q\tau+w),
 \qquad
 C(\tau)=F_\tau(0),
\tag{0.1}
\]

and let `epsilon=1/20000`.  On the inactive side,

\[
                         \Gamma(\delta)=\varepsilon.
\tag{0.2}
\]

The frozen `u=0` theorem gives

\[
 \boxed{
 H_\tau(w):=C(\tau)+F_\tau(w)>{11\over20000}}
\tag{0.3}

for every residual period and every `2tau/3<=w<=A`.

## 1. Quarter-boundary geometry

On `u=P/4`, the competing ceiling `u<=A-P` gives

\[
                         P\le{4A\over5}.
\tag{1.1}
\]

Together with `P>=2tau/3`, this implies

\[
 \tau\le{6A\over5},
 \qquad
 {\tau\over6}\le u\le{A\over5},
 \qquad
 {5\tau\over6}\le5u=P+u\le A.
\tag{1.2}
\]

Both `P` and `P+u` therefore lie in the range of (0.3).

We retain the exact rational bounds

\[
 A>{4431\over5000},
 \qquad
 \delta_*>{1363\over20000}.
\tag{1.3}
\]

## 2. The low quarter train

### Lemma 2.1

For every point of the quarter boundary,

\[
                         \boxed{F_\tau(u)>{53\over1000}.}
\tag{2.1}
\]

#### Proof

For `1/6<=t<=1/5`, the compact derivative is negative.  Indeed

\[
 K'(At)<0
 \quad\Longleftrightarrow\quad
 2\operatorname{arctanh}(t)<\pi t,
\]

and `arctanh(t)<=4t/3` gives the result.  Thus

\[
                         K(u)\ge K(A/5).
\]

At the endpoint,

\[
 K(A/5)=1-e^{-4\pi/25}-e^{-9\pi/25}.
\]

The finite positive Taylor comparisons

\[
 e^{4\pi/25}>{200\over121},
 \qquad
 e^{9\pi/25}>{1000\over323}
\tag{2.2}
\]

give

\[
                         K(A/5)>{9\over125}.
\tag{2.3}
\]

For the period tail, its first argument satisfies

\[
 A+\tau+u\ge A+{7\tau\over6}
 \ge A+{7(A+\delta_*)\over6}
 >{239953\over120000}.
\]

Its square exceeds `1999/500`, whose exponential is greater than `54`.
Every successive squared-argument gap is at least `4\pi/3`, whose
exponential is greater than `60`.  Hence the complete adverse tail is
smaller than

\[
 {1/54\over1-1/60}={10\over531}<{19\over1000}.
\tag{2.4}
\]

Combining (2.3)--(2.4),

\[
 F_\tau(u)>{9\over125}-{19\over1000}
 ={53\over1000}.
\]

This proves (2.1). \(\square\)

## 3. The upper quarter train

### Lemma 3.1

For every point of the quarter boundary,

\[
                         \boxed{F_\tau(P+u)>-{53\over1000}.}
\tag{3.1}
\]

#### Proof

By (1.2) and `delta>=delta_*`,

\[
 {P+u\over A}\ge{5\tau\over6A}>{17\over20}.
\]

The authenticated upper compact-kernel bound from the `u=0` theorem
therefore gives

\[
                         K(P+u)>-{13\over250}.
\tag{3.2}
\]

The first period-tail argument satisfies

\[
 A+\tau+(P+u)
 \ge A+{11\tau\over6}
 \ge A+{11(A+\delta_*)\over6}
 >{316301\over120000}.
\]

Its square exceeds `6947/1000`, whose exponential is greater than `1030`.
Every successive exponent gap is at least `5\pi/3`, whose exponential is
greater than `100`.  Thus the complete tail is smaller than

\[
 {1/1030\over1-1/100}<{1\over1000}.
\tag{3.3}
\]

Equations (3.2)--(3.3) give

\[
 F_\tau(P+u)>-{13\over250}-{1\over1000}
 =-{53\over1000}.
\]

This proves (3.1). \(\square\)

### Corollary 3.2

On the quarter boundary,

\[
                         \boxed{F_\tau(u)+F_\tau(P+u)>0.}
\tag{3.4}
\]

## 4. Complete boundary sign

The gate is

\[
 \mathfrak R
 =C(\tau)+F_\tau(P)+F_\tau(P+u)
  +\min\{C(\tau),F_\tau(u)\}-\varepsilon.
\tag{4.1}
\]

### Theorem 4.1

On the complete inactive quarter boundary `u=P/4`,

\[
                         \boxed{\mathfrak R>{1\over2000}>0.}
\tag{4.2}
\]

#### Proof

If the low minimum is `C(tau)`, then both `P` and `P+u` are legal shifts
for (0.3), and

\[
 \mathfrak R
 =H_\tau(P)+H_\tau(P+u)-\varepsilon
 >{21\over20000}.
\tag{4.3}
\]

If the low minimum is `F_tau(u)`, then Corollary 3.2 gives

\[
\begin{aligned}
 \mathfrak R
 &=H_\tau(P)+\{F_\tau(u)+F_\tau(P+u)\}-\varepsilon\\
 &>{11\over20000}-{1\over20000}
 ={1\over2000}.
\end{aligned}
\tag{4.4}
\]

The two cases exhaust the minimum and prove (4.2). \(\square\)

The active side and its switch were already closed.  Hence the full
quarter boundary is positive.

## 5. Exact scope

This theorem closes `u=P/4`, including its junction with `u=A-P` at
`P=4A/5`.  It does not sign the moving boundary `P=2tau/3`, the low-branch
switch away from the closed faces, or the formal initial gate row.

## 6. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| inactive `u=0` theorem and compact upper bound | `MATH_THEOREM_SIX_SLOT_H4_INACTIVE_U0_BOUNDARY_COMPLETE_POSITIVITY_20260804.md` | `ba327b06397a9190de23c62c6a0ca0f985bbb75bff12188540518550e03ecd8f` |
| active-`Gamma` theorem | `MATH_THEOREM_SIX_SLOT_H4_ACTIVE_GAMMA_COMPLETE_POSITIVITY_AND_BOUNDARY_COLLAPSE_20260804.md` | `3259e9c0c8a3f74839f5ed1cf73646395b8bebb17ea871d1d7e95e74360e2953` |
| literal rectangle | `MATH_THEOREM_SIX_SLOT_H4_LITERAL_RECTANGLE_CORRELATED_GATE_20260804.md` | `533f194ed727b2c15d26ca2007131a3bfc22f08f401097f74d021d40cf5dd5cd` |
