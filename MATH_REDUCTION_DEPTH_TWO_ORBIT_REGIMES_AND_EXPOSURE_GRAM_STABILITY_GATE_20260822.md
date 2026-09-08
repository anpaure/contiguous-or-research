# Depth-two orbit regimes and the remaining exposure-Gram stability gate

**Date:** 2026-08-22

**Status:** rigorous shallow-fixed and top-fixed-defect asymptotics for the
explicit orbit factor, an exact finite regime scan, and a perturbative
exposure-histogram interface.  A uniform bulk exposure-angle bound is not
proved.

## 1. Exact orbit factor

Put

\[
 b=2r+1,\qquad k=r-2,\qquad N={b\choose k},\qquad p={b\over N}.
                                                               \tag{1.1}
\]

For `2<=j<=k`, let `theta_(r,j)` be the squared Fisher singular value of
the unconstrained full cyclic rank-`k` deck on `V_(b-j,j)`, and put

\[
 F_{r,j}=N\theta_{r,j},qquad
 \Theta_{r,j}={\theta_{r,j}\over p^2}
              ={N\over b^2}F_{r,j}.               \tag{1.2}
\]

The exact Hahn sum is

\[
 F_{r,j}=b\sum_{h=0}^{k}w_hP_{r,j}(h),             \tag{1.3}
\]

where `w_0=6`, `w_k=1`, and `w_h=2` otherwise, and

\[
 P_{r,j}(h)=
 {1\over(k)_j(r+3)_j}
 \sum_{a=0}^{j}(-1)^{j-a}{j\choose a}
 (h)_a(h+5)_a(k-h)_{j-a}^2.                       \tag{1.4}
\]

Here `(z)_m=z(z-1)...(z-m+1)`.  Formula (1.4) follows from the
intersection-shell expression by the two identities

\[
 {{k-j\choose h-a}\over{k\choose h}}
 ={(h)_a(k-h)_{j-a}\over(k)_j},
\quad
 {{r+3-j\choose k-j-h+a}\over{r+3\choose k-h}}
 ={(k-h)_{j-a}(h+5)_a\over(r+3)_j}.               \tag{1.5}
\]

Thus every statement below concerns a completely explicit scalar; rooted
exposure has not yet entered.

## 2. Fixed shallow modules

### Theorem 2.1

For each fixed `j>=2`, as `r` tends to infinity,

\[
 F_{r,j}=\begin{cases}
 \displaystyle {4\over j+1}r^2+O_j(r),&j\text{ even},\\[2mm]
 25(j-1)+O_j(r^{-1}),&j\text{ odd}.
 \end{cases}                                                   \tag{2.1}
\]

Consequently

\[
 \boxed{
 \Theta_{r,j}=\begin{cases}
 \displaystyle {N\over j+1}(1+O_j(r^{-1})),&j\text{ even},\\[2mm]
 \displaystyle {25(j-1)N\over4r^2}(1+O_j(r^{-1})),
       &j\text{ odd}.
 \end{cases}}                                                 \tag{2.2}
\]

#### Proof

For fixed `j`, (1.4) is a degree-`2j` polynomial in `h` divided by a
degree-`2j` polynomial in `r`.  Put `h=kx`.  Expanding falling factorials
coefficientwise gives, uniformly as a polynomial on `[0,1]`,

\[
 P_{r,j}(kx)=(2x-1)^j+r^{-1}Q_j(x)+r^{-2}R_j(x)+O_j(r^{-3}),  \tag{2.3}
\]

for explicit polynomials `Q_j,R_j`.  Euler--Maclaurin is exact here up to
the corresponding finite Bernoulli remainder because all degrees are
fixed.

If `j` is even,

\[
 \sum_{h=0}^{k}P_{r,j}(h)
 ={r\over j+1}+O_j(1),                              \tag{2.4}
\]

since `integral_0^1(2x-1)^j dx=1/(j+1)`.  The two endpoint changes from
weight two to weights six and one contribute only `O_j(1)`.  Multiplying
by `b` proves the first line of (2.1).

For odd `j`, the leading integral and its endpoint half-sum vanish.  Direct
substitution of the coefficients obtained from

\[
 (z)_m=z^m\left(1-{m(m-1)\over2z}
 +{m(m-1)(3m^2-7m+2)\over24z^2}+O_m(z^{-3})\right) \tag{2.5}
\]

into (2.3), followed by the elementary beta integrals of its monomials,
gives

\[
 2\sum_{h=0}^{k}P_{r,j}(h)
 +4P_{r,j}(0)-P_{r,j}(k)
 ={25(j-1)\over2r}+O_j(r^{-2}).                    \tag{2.6}
\]

For auditability, the endpoint values used here are exactly

\[
 P_{r,j}(0)=(-1)^j{(k)_j\over(r+3)_j},
 \qquad P_{r,j}(k)=1.                              \tag{2.7}
\]

The coefficient in (2.6) is obtained after cancellation of the two
finite sums
`sum_a (-1)^(j-a) binom(j,a)a^u`, `0<=u<j`; at `u=j` the sum is `j!`.
This is the standard `j`-th finite-difference identity and leaves
`25(j-1)`.  Multiplication by `b=2r+1` proves the odd line.  Equation
(2.2) follows from (1.2). `square`

The first two nontrivial cases have particularly compact exact forms:

\[
 F_{r,2}={4r^4+20r^3-73r^2-5r+18
             \over3(r+2)(r+3)},                    \tag{2.8}
\]

\[
 \boxed{
 F_{r,3}={50r^3-155r^2+40r+65
             \over(r+1)(r+2)(r+3)}.}               \tag{2.9}
\]

For `r>=5`,

\[
 7\operatorname {num}(F_{r,3})
 -55\operatorname {den}(F_{r,3})
 =5(r-5)(59r^2+12r-5)\ge0,                         \tag{2.10}
\]

so

\[
 \boxed{\Theta_{r,3}\ge {55N\over7(2r+1)^2}
                         \ge {55N\over63r^2}.}      \tag{2.11}
\]

Among fixed shallow modules, `j=3` is therefore the asymptotic bottleneck:
even levels have orbit factor of order `N`, while fixed odd `j>=5` have a
larger leading constant than `j=3` at order `N/r^2`.

## 3. Fixed defect from the top

### Theorem 3.1

For each fixed `d>=0`, with `j=k-d`,

\[
 F_{r,k-d}=2r+O_d(1),
 \qquad
 \boxed{\Theta_{r,k-d}={N\over2r}(1+O_d(r^{-1})).}            \tag{3.1}
\]

#### Proof

Substitute `j=k-d` in the original binomial form of the Hahn shell.  The
factor `{k-j choose h-a}={d choose h-a}` restricts each inner sum to at
most `d+1` terms.  Reindex by `t=k-h` and then by `u=j-a`.  The `t=0`
term is exactly one.  For every fixed `d`, the terms with `t>=1` are a
finite linear combination, with coefficients depending polynomially on
`d`, of reciprocal-binomial terms

\[
 {1\over{r+3\choose t}},\qquad
 {1\over{r-2\choose t}},                            \tag{3.2}
\]

and their first `d` adjacent ratios.  The `t=1` contribution is `O_d(1/r)`;
using

\[
 \sum_{t=2}^{r-2}{1\over{r+3\choose t}}=O(r^{-2})             \tag{3.3}
\]

and the identical adjacent-ratio bound for the shifted terms makes the
remaining sum `O_d(r^-2)`.  Hence the bracket in (1.3) is
`1+O_d(1/r)`, proving (3.1). `square`

At the literal top `d=0` no reduction is hidden:

\[
 F_{r,k}=b\sum_{t=0}^{k}
 {w_{k-t}(-1)^t\over{r+3\choose t}}
          =2r-3+O(r^{-1}).                          \tag{3.4}
\]

For clarity, the finite expression used in the fixed-defect proof is

\[
 P_{r,k-d}(k-t)=
 {\displaystyle\sum_u(-1)^u{k-d\choose u}
       {d\choose d+u-t}{d+5\choose t-u}
  \over {k\choose t}{k+5\choose t}},               \tag{3.5}
\]

where at most `d+1` summands are nonzero.  This follows by substituting
`a=k-d-u` into the original intersection-shell formula and makes the
reciprocal-binomial tail estimate literal.

Thus the top regime has an orbit factor larger than the shallow `j=3`
factor by a factor of order `r`.

## 4. Bulk evidence and its exact limitation

For the concrete bulk interval `r/10<=j<=9r/10`, the exact checker finds

\[
                         F_{r,j}\ge r/2                \tag{4.1}
\]

for every tested `20<=r<=60`, with substantial parity oscillation.  It
also finds that the minimum of `F_(r,j)` over all `2<=j<=r-2` occurs at
the top for `7<=r<=14` and at `j=3` for every `15<=r<=60`.

These are exact finite computations, not an asymptotic proof.  A uniform
steepest-descent or positive integral representation for the Hahn sum
(1.3) in the bulk remains open.  In particular this note does not promote
(4.1) to a theorem.

## 5. Exact exposure-to-avoidance decomposition

The rooted-exposure vectors admit a sharper exact form.  Let `d_s` be the
complete-catalogue degree of a rank-`s` target and put

\[
 N_{0,s}(S)=|\{F:S\in F_s,\ F\cap E_0=\varnothing\}|.          \tag{5.1}
\]

### Theorem 5.1

For `s in {r,r-1}`,

\[
 \boxed{
 e_s(S)=\sum_{T\in E_0}\deg(S,T)-d_s+N_{0,s}(S).}             \tag{5.2}
\]

On every nontrivial module `V_(b-j,j)`,

\[
 \boxed{
 \operatorname {span}\{c_r,c_{r-1},e_r,e_{r-1}\}
 =\operatorname {span}\{c_r,c_{r-1},N_{0,r},N_{0,r-1}\}.}    \tag{5.3}
\]

#### Proof

For `t_F=|F cap E_0|`, the integer identity

\[
                         (t_F-1)_+=t_F-1+\mathbf1_{\{t_F=0\}} \tag{5.4}
\]

gives (5.2) after summing over `F` through `S` and swapping the sum in
`sum_F t_F`.  The term `-d_s` is constant and hence vanishes on every
`j>=1` module.  For each pair of shores, the map

\[
 c_\tau\longmapsto
 \left(S\mapsto\sum_{T\in X_\tau}c_\tau(T)\deg(S,T)\right)  \tag{5.5}
\]

is `S_b`-equivariant.  The subset modules are multiplicity-free, so its
`j`-th component is a scalar map between the unique two-row copies.
Consequently the first term of (5.2) lies in
`span{c_r,c_(r-1)}` on every fixed `j`.  Replacing `e_r,e_(r-1)` by
`N_(0,r),N_(0,r-1)` therefore leaves the four-vector span unchanged.
`square`

This identifies the genuinely nonlinear exposure data: it is precisely the
conditional zero-hit, or avoidance, profile.  The explicit pair-codegree
sum and the degree constant create no new compensated direction.

A boundary-polymer or transfer-matrix attack may now target `N_0` directly.
For high `j`, the natural conjecture is that its two harmonic directions
have negligible correlation with the shallow deck after the central
directions are removed, so `alpha_(r,j)` stays bounded away from zero.
That statement is not implied by the existing unsigned second and third
overlap moments and is not proved here.

## 6. What the orbit split says—and does not say—about exposure

The compensated relative eigenvalue is

\[
                         \widehat\sigma_{r,j}^2
                         =\alpha_{r,j}\Theta_{r,j}.            \tag{6.1}
\]

Sections 2--3 show that neither the shallow-fixed nor top-fixed-defect
orbit factor is polynomially small: it is exponentially large because
`N=exp(Theta(r))`.  The known standard-output exponential obstruction is
entirely removed by relative-density normalization.  A true exponential
obstruction in these regimes can therefore occur only if the exposure
angle `alpha` cancels essentially the whole `N` factor.

The exact histogram theorem writes the normalized `5 by 5` Gram matrix as
weighted exposure-intersection histograms.  Here is a robust sufficient
interface for their asymptotics.

### Lemma 6.1 (Gram stability)

Let `G^0` and `G` be normalized `5 by 5` Gram matrices with final diagonal
one, let their leading blocks be `B^0,B`, and suppose

\[
 \|G-G^0\|_{\rm op}\le\epsilon,qquad
 \lambda_{\min}(B^0)\ge\mu,qquad
 \alpha(G^0)\ge a.                                  \tag{6.2}
\]

If

\[
                         \epsilon\le {a\mu^2\over32},         \tag{6.3}
\]

then `B` is nonsingular and

\[
                         \boxed{\alpha(G)\ge a/2.}            \tag{6.4}
\]

#### Proof

Condition (6.3) implies `epsilon<=mu/2` because `a,mu<=1`.  The resolvent
identity gives

\[
 \|B^{-1}-(B^0)^{-1}\|\le {2\epsilon\over\mu^2}.              \tag{6.5}
\]

Writing the last columns as `g,g^0`, normalized Gram positivity gives
`||g||,||g^0||<=2`, while `||g-g^0||<=epsilon`.  Expanding
`g^T B^-1 g-(g^0)^T(B^0)^-1g^0` and applying (6.5) bounds its absolute
value by `16epsilon/mu^2<=a/2`.  Since
`alpha=1-g^T B^-1g`, (6.4) follows. `square`

Thus a regime-specific reference histogram calculation with polynomial
`a,mu` and operator error satisfying (6.3) would prove a polynomial angle,
and hence much more than needed after multiplication by (2.2) or (3.1).

The currently proved aggregate second and third duplicate moments do not
supply (5.2): they control unsigned totals, whereas the harmonic Gram
entries contain signed cross-shore cancellations.  This is the exact
remaining gap in all three regimes.  The finite values at `r=4,5` show
positive constants but do not identify the asymptotic worst regime of the
full product (6.1).

## 7. Exact verifiers

Run

```text
python3 scratch/verify_depth_two_orbit_regimes_20260822.py
```

The standard-library checker verifies the Hahn and shell formulas against
each other, proves the rational identities (2.8)--(2.9) on enough points to
fix their degrees and then on an independent range, checks (2.10)--(2.11)
and the explicit top formula, and performs the exact all-module scan through
`r=60`.  The bulk scan is recorded as evidence only.

The exact avoidance decomposition is independently replayed at `r=4` by

```text
python3 scratch/verify_exposure_zero_avoidance_decomposition_20260822.py
```

It checks (5.2) target by target and verifies that replacing exposure by
the zero-hit vectors leaves the exact compensated angle unchanged.
