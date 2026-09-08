# Near-width saturated rectangle covers require unbounded overlap

Date: 2026-09-07. Research continuation toward `nu(k)=(1+o(1))W(k)`.

This note proves a quantitative restriction on a family of possible
extensions of master Appendix A.7. It does not give a lower bound on arbitrary
OR words. The full coefficient-one theorem remains open.

## 1. Model and finite theorem

Let a finite indexed collection of pairs cover the Boolean cube. One member
of each pair is

\[
 R=C\times D=\{X\cup Y:X\in C,\ Y\in D\},
\]

where `C,D` are saturated chains on complementary coordinate supports. The
other member is the family of full complements of the sets in `R`. Families
may overlap, including within a complementary pair. Put

\[
 M=\sum_R(a_R+b_R),\qquad V=2\sum_Ra_Rb_R,
 \qquad a_R=|C|,\quad b_R=|D|.
\]

Thus `M` is the principal bridge charge and `V/2^k` is the average designated
coverage multiplicity, counting every indexed occurrence. Write

\[
 W=\binom{k}{\lfloor k/2\rfloor},\qquad
 F_k(x)=\sum_{j=0}^k\binom kj(1-|x-j|)_+.
\]

For every real `t>0` define

\[
 B_t={2M-W-F_k(k/2+t)\over2}.
\]

Then `B_t>0` for a nonempty cube cover and

\[
 \boxed{V\ge {2t\over B_t}(W/2-B_t)_+^2.}                 \tag{1}
\]

There is a sharper useful version:

\[
 \boxed{0<B_t\le W/4\quad\Longrightarrow\quad
        V\ge {tW^2\over2B_t}.}                          \tag{2}
\]

These inequalities are exact in finite dimensions. They do not require
centered rectangles, a symmetric chain decomposition, or a uniform split.

## 2. Proof

Set `u=(a+b)/2`, `v=|a-b|/2`, and let `c` be the rank center of `R` relative
to `k/2`. Saturation makes the linearly interpolated rank profile of `R`
exactly

\[
 H_{c,u,v}(x)=(u-|x-c|)_+-(v-|x-c|)_+.
\]

One proof is to replace each consecutive chain rank by its unit interval
centered there: the two interval densities convolve to this trapezoid,
equivalently to the triangular interpolation of the integer rank counts.
Complementation changes `c` to `-c`. The complete occurrence profile is

\[
 G(x)=\sum_R\{H_{c,u,v}(x)+H_{c,u,v}(-x)\}
       \ge F_k(k/2+x).
\]

In particular `G(0)>=W`, also for odd `k`, because the two central binomial
coefficients coincide. Put

\[
 D_R=u-H_{c,u,v}(0)=\min\{u,\max(v,|c|)\}.
\]

The triangle function is 1-Lipschitz. If `|c|<=u`, discarding the subtracted
inner triangle and moving the outer triangle to zero costs at most `2|c|`.
If `|c|>u`, each profile is at most `u` and `D_R=u`. In both cases,

\[
 H_{c,u,v}(t)+H_{c,u,v}(-t)
       \le2(u-t)_++2D_R.
\]

Since `2 sum D_R=M-G(0)`, summing gives

\[
 2\sum_R\min(t,u_R)
 \le 2M-G(0)-G(t)
 \le 2M-W-F_k(k/2+t)=2B_t.                              \tag{3}
\]

Let `ell_R=u_R-v_R=min(a_R,b_R)`. We have

\[
 \sum_R\ell_R\ge W/2,\quad
 \sum_R\min(t,\ell_R)\le B_t,\quad
 V=2\sum_Ra_Rb_R\ge2\sum_R\ell_R^2.                    \tag{4}
\]

The first inequality follows from `G(0)<=2 sum ell_R`; the others follow
from (3) and `ab>=min(a,b)^2`. The lengths at most `t` sum to at most `B_t`.
There are at most `B_t/t` longer lengths, whose sum is at least
`(W/2-B_t)_+`. Cauchy--Schwarz proves (1).

For (2), set `S=W/2`, `B=B_t`, `lambda=2tS/B`, and `kappa=tS^2/B^2`.
Since `B<=S/2`, `kappa>=lambda`. For `0<=x<=t`,
`x^2-lambda*x+kappa*min(t,x)>=0`; for `x>=t` the same expression is
`(x-lambda/2)^2`, because `kappa*t=lambda^2/4`. Sum this inequality and
apply (4):

\[
 \sum_R\ell_R^2\ge\lambda S-\kappa B=tS^2/B.
\]

This proves (2). Positivity of `B_t` also follows from (3), since at least
one `u_R` is positive. No numerical experiment is a premise.

## 3. Gaussian form and the divergence theorem

For a sequence of covers with `M/W -> c>=1`, fix `s>0`, put `t=s sqrt(k)`,
and define

\[
 b_c(s)={2c-1-e^{-2s^2}\over2}.
\]

The elementary central-binomial product estimate gives, uniformly for `s`
in fixed compact intervals,

\[
 {F_k(k/2+s\sqrt k)\over W}\longrightarrow e^{-2s^2},\qquad
 {W\sqrt k\over2^k}\longrightarrow\sqrt{2/\pi}.
\]

Consequently, whenever `0<b_c(s)<1/4`, (2) yields

\[
 \boxed{\liminf {V\over2^k}
   \ge {\sqrt{2/\pi}\,s\over2b_c(s)}.}                \tag{5}
\]

In particular, if `M/W -> 1`, then **`V/2^k -> infinity`**. Indeed (5)
then applies at each fixed sufficiently small `s>0`, and its right side is

\[
 {\sqrt{2/\pi}\,s\over1-e^{-2s^2}}
       \sim {\sqrt{2/\pi}\over2s}\quad(s\downarrow0).
\]

This order of limits proves divergence without a local-limit estimate
uniform in a vanishing relative error.

There is a quantitative small-error statement. If `epsilon=epsilon_k -> 0`,
`epsilon*k -> infinity`, and `M <= (1+epsilon)W`, take
`s=sqrt(epsilon)`. Expanding adjacent binomial ratios over
`t=sqrt(epsilon*k)` steps gives

\[
 F_k(k/2+t)/W=1-2\epsilon+o(\epsilon),\qquad
 B_t/W\le2\epsilon+o(\epsilon).
\]

For clarity, the ratio logarithm is `-2t^2/k + O(t/k+t^3/k^2)`;
rounding/interpolation contributes `O((t+1)/k)`, all `o(epsilon)` under
the stated condition. Formula (2) therefore gives

\[
 \boxed{{V\over2^k}\ge
  {1+o(1)\over\sqrt{8\pi\epsilon}}.}                  \tag{6}
\]

The `o(1)` in (6) is a statement about the specified joint regime, not a
numerical finite-dimensional bound. Formula (2) supplies the finite bound.

## 4. Sharp order and constant for the centered balanced rank relaxation

There is a useful positive counterpart: rank counts alone permit the
coefficient to approach one once sufficiently large overlap is allowed.
It also identifies the required length scale.

For a cover all of whose rectangles have equal side lengths and rank center
`k/2`, we have `G(0)=M` and `ell_R=u_R`. The same proof replaces `B_t` by
`(M-F_k(k/2+t))/2` and `S` by `M/2`. Consequently

\[
 F_k(k/2+t)\ge M/2\quad\Longrightarrow\quad
 \boxed{V\ge {tM^2\over M-F_k(k/2+t)}}.                 \tag{7}
\]

The denominator is positive for `t>0`. In the regime
`M=(1+epsilon)W`, `epsilon -> 0`, `epsilon*k -> infinity`, take
`t=sqrt(epsilon*k/2)`. Then

\[
 \boxed{{V\over2^k}\ge {1+o(1)\over2\sqrt{\pi\epsilon}}.} \tag{8}
\]

The leading constant in (8) is sharp for the Gaussian rank-profile
relaxation, as follows. This is an explicit nonnegative mixture of rank
profiles, not a cover of the actual coordinate sets.

Fix `0<a<1/2`, and set

\[
 f(t)=e^{-2t^2},\quad C_a=(1+4a^2)e^{-2a^2},\quad
 \lambda_a=4ae^{-2a^2},\qquad
 g_a(t)=\max\{C_a-\lambda_a|t|,f(t)\}.
\]

On `[0,1/2]`, `f` is concave, so its tangent at `a` lies above it.
That tangent is exactly `C_a-lambda_a*t`. On `[1/2,infinity)`, both the
line and `f` are convex. Hence `g_a` is convex and nonincreasing on the
positive axis, equals the line near zero, and eventually equals `f`.
It dominates the required Gaussian at every rank.

Let `z_a>1/2` be the unique second intersection of the line and `f`.
Existence and uniqueness follow because their difference is strictly
convex beyond `1/2`, starts negative there, and becomes positive before
the line reaches zero. The positive measure on `(0,infinity)`

\[
 d\eta_a(u)=\{f'(z_a)+\lambda_a\}\,\delta_{z_a}(du)
                    +\mathbf1_{u>z_a}f''(u)\,du
\]

is the distributional second derivative of `g_a` on the positive axis.
The atom is nonnegative by the direction of the crossing. Integrating
twice from infinity gives

\[
 g_a(t)=\int_0^\infty(u-|t|)_+\,d\eta_a(u),\qquad
 \int u\,d\eta_a(u)=C_a.
\]

Use half this measure as the multiplicity of symmetric paired square
profiles. Its principal charge is therefore exactly `C_a`, while its
normalized designated occurrence volume is

\[
 \mathcal V_a=\sqrt{2/\pi}\int_{-\infty}^{\infty}g_a(t)\,dt.
\]

As `a -> 0`, put `epsilon_a=C_a-1=2a^2+O(a^4)`. The zero of the line
is `u_a=C_a/lambda_a~1/(4a)`, and `z_a/u_a -> 1`: first `z_a -> infinity`
by the crossing equation, and then
`1-z_a/u_a=f(z_a)/C_a -> 0`. The difference between the integral of
`g_a` and that of the triangle `(C_a-lambda_a|t|)_+` is bounded by
`2 integral_(z_a)^infinity f(t) dt=exp(-Omega(a^-2))`. Thus

\[
 \boxed{\mathcal V_a\sim
 \sqrt{2/\pi}{C_a^2\over\lambda_a}
 \sim {1\over2\sqrt{\pi\epsilon_a}}.}                 \tag{9}
\]

This matches (8). Its main square side length is of order
`sqrt(k/epsilon)` before normalization. A subsequent exact finite
symmetrization and discrete-majorant proof in
`SYMMETRIZED_CONVEX_PROFILE_FRACTIONAL_COVER_20260907.md` realizes this
profile on actual coordinate subsets **fractionally**, including a bounded
correction for within-pair duplicates. That upgrade does not produce an
integral selection. `CENTERED_SQUARE_BAND_COMPILER_20260907.md` supplies an
independent-block compiler for sufficiently long selected squares; the
remaining integral rounding problem is open.

## 5. Consequence for the live construction search

The archived moving-center argument only excluded partitions and covers
whose excess volume vanishes. Equations (1)--(6) extend that conclusion to
**every uniformly bounded average multiplicity**, and quantify the loss.

Thus enlarging an overlapping staircase design while keeping its average
designated multiplicity bounded cannot yield coefficient one through the
saturated paired-rectangle bridge ledger. A successful construction in this
class must allow average multiplicity to grow without bound while paying
nearly minimal chain boundary cost.

This changes the appropriate template search criterion: low overlap is not
an asymptotic objective in this class. Large repeated volume can be required
even when the principal cost is almost optimal. The finite q-ary gate must
therefore allow such repeated volume rather than impose a bounded-overlap
condition implicitly.

The proof uses saturated rank profiles and designated coverage. It does not
apply unchanged to nonsaturated terminal chains, to covers obtaining their
missing targets only from additional cross-boundary intervals, or to an
OR compiler whose leading cost is smaller than `sum(a+b)`. Those remain
possible ways to achieve the thread objective.
