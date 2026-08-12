# Audit: the rank-bound constant and the fixed-width Gaussian tail

## Verdict

The two main conclusions in the submitted calculation are correct after one
notation repair:

\[
 B(k)=W(k)+\sqrt{\frac{\pi k}{8}}+O(1),
 \qquad W(k)=\binom{k}{\lfloor k/2\rfloor},
\]

and, for the exact truncated chain-product tail word at half-width
`h=floor(c sqrt(m))`,

\[
 \frac{L_m(m-h)}{W(2m)}\longrightarrow T(c).
\]

The decimal `0.626657...` is `sqrt(pi/8)`, not `sqrt(8/pi)`.
The latter is approximately `1.59577`.  The rendered formulas in the source
are ambiguous, but the derivation itself uses the former, correct constant.

This does not improve the current upper bound by itself.  It gives a useful
quantitative sufficient target: a central-band word through depth
`2 sqrt(m)` with asymptotic coefficient below `1.0843809493` would improve
the global `sqrt(2)` constant.

## 1. Rank-count asymptotic

For rank `r`, write

\[
 M_r=\binom kr,\qquad L_r=\sum_{s<r}\binom ks,
\]

and let `tau_r` be the least `t` satisfying

\[
 L_r\le tM_r+\binom{t+1}{2}.
\]

Taking `u=ceil(2^((k+1)/2))` makes the triangular term alone at least
`2^k>L_r`.  Hence `tau_r<=u` uniformly and

\[
 W(k)\le B(k)\le W(k)+O(2^{k/2}).
\]

The gap from the central binomial coefficient to the next layer is
`W/(m+1)` for `k=2m` and `2W/(m+2)` for `k=2m+1`.  This is exponentially
larger than the uniform slack bound, so for all sufficiently large `k` the
maximizer is central (upper-central in odd dimension).

At that rank, `L/W=Theta(sqrt(k))`, while
`binom(t+1,2)/W=o(1)`.  Therefore

\[
 \tau=\frac LW+O(1).
\]

For `k=2m`,

\[
 L=2^{2m-1}-\frac12\binom{2m}{m}-1,
\]

and for `k=2m+1` at rank `m+1`, `L=2^{2m}-1`.  Stirling's formula gives in
both cases

\[
 \frac LW=\sqrt{\frac{\pi k}{8}}+O(1).
\]

Thus the claimed asymptotic for `B(k)` follows.  The finite check through
`k=11`, combined with the uniform bound for `k>=12`, also correctly proves
`B(k)<sqrt(2)W(k)` for every `k>=1`.

## 2. Fixed-`c` tail limit

Use the exact shorter product construction from `TRUNCATED_IDEAL_PRODUCT.md`:

\[
 L_m(r)=2\sum_a N_m(a)w_m(a)C_m(r-a),
\]

where

\[
 N_m(a)=\binom ma-\binom m{a-1},\qquad
 w_m(0)=m,\quad w_m(a)=m-2a+1\ (a>0).
\]

Put `r=m-floor(c sqrt(m))` and
`x=(m-2a)/sqrt(m)`.  The mesh is `2/sqrt(m)`, and uniformly on compact
`x`-ranges,

\[
 \frac{N_m(a)w_m(a)}{W(m)}\to 2x^2e^{-x^2/2},
\]

while

\[
 \frac{C_m(r-a)}{W(m)}\to
 \begin{cases}
 e^{-(2c-x)^2/2},&0\le x<2c,\\
 1,&x\ge2c.
 \end{cases}
\]

Together with `W(m)^2/W(2m)~2/sqrt(pi m)`, Riemann summation yields

\[
 T(c)=\frac4{\sqrt\pi}\left[
 \int_0^{2c}x^2e^{-[x^2+(2c-x)^2]/2}\,dx+
 \int_{2c}^{\infty}x^2e^{-x^2/2}\,dx\right].
\]

Standard central-binomial Gaussian bounds supply an integrable dominating
function; the exceptional `a=0` term is negligible.  Evaluating the two
integrals gives

\[
 T(c)=4\left(c^2+\frac12\right)e^{-c^2}\operatorname{erf}(c)
 +\frac{4c}{\sqrt\pi}e^{-2c^2}
 +2\sqrt2\operatorname{erfc}(\sqrt2c).
\]

Its derivative is

\[
 T'(c)=4c(1-2c^2)e^{-c^2}\operatorname{erf}(c)
       -\frac{8c^2}{\sqrt\pi}e^{-2c^2},
\]

so it is strictly decreasing for `c>=1/sqrt(2)`.  Direct high-precision
evaluation confirms

\[
 c_*=1.924707427123100\ldots,
 \quad T(c_*)=\sqrt2-1,
 \quad T(2)=0.3298326130736817\ldots.
\]

Exact finite sums at `m=50,100,200,500,1000` converge to these limits for
`c=1,1.5,2`; this is an independent numerical check, not part of the proof.

## 3. Correct quantitative reduction

Let `nu_band(2m,h)` cover only ranks `m-h,...,m+h`, and define

\[
 \Gamma(c)=\limsup_{m\to\infty}
 \frac{\nu_{\rm band}(2m,\lfloor c\sqrt m\rfloor)}{W(2m)}.
\]

Concatenating the band word with the two-tail word is valid and gives

\[
 \limsup\frac{\nu(2m)}{W(2m)}\le\Gamma(c)+T(c).
\]

Therefore at `c=2`,

\[
 \Gamma(2)<\sqrt2-T(2)=1.084380949299413\ldots
\]

is sufficient to beat `sqrt(2)`.  The stronger near-width conclusion
`Gamma(2)<=1` would give the explicit constant

\[
 1+T(2)=1.329832613073682\ldots.
\]

The standard doubling lift preserves any even-dimensional leading constant
in the adjacent odd dimensions.  This is a genuine intermediate target,
but no construction currently establishes the needed bound on `Gamma(2)`.

## Scope

The asymptotic formula concerns the proved lower bound `B(k)`, not the unknown
optimum `nu(k)`.  It confirms that the rank-count lower constant is one.  It
does not prove `nu(k)=(1+o(1))W(k)` or improve the upper constant until the
central-band theorem above is supplied.
