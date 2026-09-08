# Rayleigh long-wrap clocks: an exact continuum duty-cycle dichotomy

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional exact asymptotic reduction.  The primitive
long-wrap Apéry family converges, after its natural scaling, to one explicit
periodic duty-cycle all-price functional.  If that scalar functional is
negative at one point, it produces honest negative formal Apéry clocks for
all sufficiently large periods.  If it is positive, the same family has a
linear positive reserve for all sufficiently large periods.  The scalar is
not signed here.

## 1. The long-wrap family

Fix

\[
 0<P\le\zeta,
 \qquad 0<\alpha\le P,
\tag{1.1}
\]

and an integer `g>=1`.  Put

\[
 a_g={\alpha\over g},
\tag{1.2}

and define the shift table

\[
 s_r=r a_g\quad(0\le r<g),
 \qquad s_g=P.
\tag{1.3}

Its internal gaps are all `a_g`; its wrap gap is

\[
 P-(g-1)a_g=P-\alpha+{\alpha\over g}\ge a_g.
\tag{1.4}

### Lemma 1.1

The table (1.3) is nonnegative and cyclically superadditive.  Its endpoint
has maximum density `lambda=P/g`.  If `alpha<P`, the endpoint is uniquely
maximum-density and the table is a primitive Apéry table.

#### Proof

For `i+j<=g`, ordinary superadditivity is equality:

\[
 s_{i+j}=s_i+s_j.
\]

For `i+j>=g`,

\[
 P+s_{i+j-g}-(s_i+s_j)=P-g a_g=P-\alpha\ge0.
\]

For every proper `r`,

\[
 {s_r\over r}=a_g={\alpha\over g}\le{P\over g};
\]

the inequality is strict exactly when `alpha<P`.  The exact Apéry-clock
claim follows from the cyclic-superadditive tail theorem. \(\square\)

Write

\[
 F_P(x)=\sum_{q\ge0}K(qP+x),
\tag{1.5}

so the complete formal functional is

\[
 \boxed{
 \Phi_g(P,\alpha)
 =\sum_{r=0}^{g-1}F_P\left({r\alpha\over g}\right).}
\tag{1.6}

Equivalently, its literal clock is

\[
 U_{qg+r}=qP+{r\alpha\over g}
 ={\alpha\over g}(qg+r)+(P-\alpha)q.
\tag{1.7}

Thus this is the period-dilated arithmetic clock: every completed period
receives the long-wrap bonus `P-alpha`.

## 2. The continuum obstruction

Define

\[
 \boxed{
 J_P(\alpha)=\int_0^\alpha F_P(x)\,dx
 =\sum_{q\ge0}\int_{qP}^{qP+\alpha}K(t)\,dt.}
\tag{2.1}

### Theorem 2.1 (exact Riemann limit and finite error)

For every fixed `(P,alpha)` as in (1.1),

\[
 \boxed{
 \lim_{g\to\infty}{\alpha\over g}\Phi_g(P,\alpha)
 =J_P(\alpha).}
\tag{2.2}

More precisely,

\[
 \boxed{
 \left|
 \Phi_g(P,\alpha)-{g\over\alpha}J_P(\alpha)
 \right|
 \le \operatorname {Var}_{[0,\alpha]}(F_P).}
\tag{2.3}

The sharper endpoint expansion is

\[
 \boxed{
 \Phi_g(P,\alpha)
 ={g\over\alpha}J_P(\alpha)
 +{F_P(0)-F_P(\alpha)\over2}
 +O_{P,\alpha}(g^{-1}).}
\tag{2.4}

#### Proof

Put `h=alpha/g`.  On each interval `[rh,(r+1)h]`,

\[
 \left|hF_P(rh)-\int_{rh}^{(r+1)h}F_P(x)dx\right|
 \le h\operatorname {Var}_{[rh,(r+1)h]}(F_P).
\]

Sum over `r=0,...,g-1` and divide by `h`; this proves (2.3), hence (2.2).

The Rayleigh kernel is piecewise smooth with integrable second derivative,
and its matching-point singularities are finite jumps of higher
derivatives only.  Gaussian summability therefore makes `F_P'` of bounded
variation on `[0,alpha]`.  The composite trapezoidal estimate gives

\[
 h\left({F_P(0)+F_P(\alpha)\over2}
   +\sum_{r=1}^{g-1}F_P(rh)\right)
 =J_P(\alpha)+O_{P,\alpha}(h^2).
\]

Converting the trapezoidal sum to the left sum and dividing by `h` proves
(2.4). \(\square\)

### Corollary 2.2 (counterexample-or-reserve dichotomy)

1. If `J_P(alpha)<0`, then

   \[
   \Phi_g(P,\alpha)<0
   \]

   for every sufficiently large `g`.  Hence one negative duty-cycle value
   gives an explicit infinite family of primitive formal Apéry
   counterclocks.

2. If `J_P(alpha)>0`, then for every sufficiently large `g`,

   \[
   \Phi_g(P,\alpha)
   \ge {g\over2\alpha}J_P(\alpha)>0.
   \]

Thus the sign of `J_P(alpha)` is the exact leading-order sign of the
long-wrap family.

## 3. The duty-cycle price is itself subadditive

For `x>=0`, write

\[
 x=qP+r,
 \qquad q=\lfloor x/P\rfloor,
 \qquad0\le r<P,
\]

and define

\[
 \boxed{
 H_{P,\alpha}(x)=q\alpha+\min\{r,\alpha\}.}
\tag{3.1}

Equivalently,

\[
 H_{P,\alpha}(x)
 =\int_0^x {\bf1}_{\{t\bmod P<\alpha\}}dt.
\tag{3.2}

### Theorem 3.1

The function `H_(P,alpha)` is nonnegative, nondecreasing, and subadditive,
with `H(0)=0`.  If

\[
 X=(A-R)_+,
 \qquad Y=(R-A)_+
\tag{3.3}

are the Rayleigh socket and job deviations, then

\[
 \boxed{
 J_P(\alpha)
 =\mathbb E H_{P,\alpha}(X)
  -\mathbb E H_{P,\alpha}(Y).}
\tag{3.4}

#### Proof

Only subadditivity needs care.  Write two residues as `r,s in[0,P)`.
Without a carry, it is the elementary inequality

\[
 \min\{r+s,\alpha\}
 \le\min\{r,\alpha\}+\min\{s,\alpha\}.
\tag{3.5}

With a carry `r+s>=P`, the required residue inequality is

\[
 \alpha+\min\{r+s-P,\alpha\}
 \le\min\{r,\alpha\}+\min\{s,\alpha\}.
\tag{3.6}

Assume `r<=s`.  If `r>=alpha`, both terms on the right equal `alpha`, so
(3.6) is immediate.  If `r<alpha<=s`, then
`r+s-P<=r`, and (3.6) follows.  If `s<alpha`, then the left side is
`alpha+r+s-P` (because `r+s-P<alpha`), which is at most `r+s` since
`alpha<=P`.  This proves subadditivity.

The derivative in (3.2) exists almost everywhere.  Tail integration for a
nonnegative absolutely continuous price gives

\[
 \mathbb EH(X)-\mathbb EH(Y)
 =\int_0^\infty H'(t)K(t)dt.
\]

Use (3.2), split into `P`-blocks, and apply Gaussian absolute convergence;
the result is exactly (2.1). \(\square\)

Therefore a negative `J_P(alpha)` would not be an artifact of the
periodization: it would be a literal bounded-slope nondecreasing
subadditive Rayleigh price separator.

## 4. Exact endpoint data

The equal-work identity gives

\[
 \boxed{J_P(0)=J_P(P)=0.}
\tag{4.1}

Moreover

\[
 J_P'(\alpha)=F_P(\alpha),
\tag{4.2}

so

\[
 \boxed{J_P'(0)=C(P)>c_*.}
\tag{4.3}

At the other endpoint,

\[
 F_P(P)=C(P)-M.
\tag{4.4}

The all-large-socket tail-capacity theorem proves

\[
 M-C(P)>c_*
 \qquad(0<P<A).
\tag{4.5}

Since `P<=zeta<A`,

\[
 \boxed{J_P'(P)<-c_*.}
\tag{4.6}

Thus `J_P(alpha)>0` in nonempty collars of both endpoints.  Any negative
duty-cycle obstruction must be a genuinely interior excursion returning to
zero at `alpha=P`; it cannot escape through either arithmetic boundary.

At `alpha=P`, expansion (2.4) gives

\[
 \Phi_g(P,P)={M\over2}+O_P(g^{-1}),
\tag{4.7}

in agreement with the small-mesh arithmetic comb
`Phi_g(P,P)=C(P/g)`.

## 5. Exact surviving scalar gate

The simplest primitive multi-kink formal family is now governed by one
compact two-variable inequality:

\[
 \boxed{
 J_P(\alpha)\ge0
 \qquad(0<P\le\zeta,\ 0\le\alpha\le P).}
\tag{5.1}

Proving (5.1) would close every sufficiently large-period long-wrap clock;
a strict interior failure would refute formal Apéry positivity outright by
Corollary 2.2.  Equation (3.4) identifies (5.1) as a concrete periodic
duty-cycle subcone of the Rayleigh all-price problem, not as a centered-
covariance estimate.

The theorem does not assert (5.1), does not control finite `g` from a zero
continuum value, and does not handle general primitive multi-kink profiles
or finite shoulders.

## 6. Dependencies

1. `MATH_THEOREM_RAYLEIGH_APERY_FUNDAMENTAL_PERIOD_COLLAPSE_AND_ONE_KINK_COMB_RESERVE_20260805.md`;
2. `MATH_THEOREM_RAYLEIGH_APERY_DEFECT_QUEUE_AND_ZEROTH_MODE_RESERVE_20260805.md`;
3. `MATH_COROLLARY_RAYLEIGH_ALL_LARGE_SOCKET_TAIL_CAPACITY_20260805.md`;
4. `MATH_THEOREM_RAYLEIGH_ARITHMETIC_COMB_CENTERED_PHASE_IDENTITY_20260805.md`.
