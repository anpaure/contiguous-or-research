# Audit: factorial-collision transfer, facet braid, and signed-cube duality

## Verdict

The three main results are mathematically valid:

1. a two-sided-rainbow Johnson linear forest has the stated literal
   facet-braid word;
2. the Poissonized signed-subcube functional has the displayed entropy
   dual and gives a deterministic repair upper bound;
3. the factorial-collision theorem and its wreath/reservoir transfer have
   the stated constants and asymptotics.

None of them constructs the growing-depth exact factor required for the
constant-one theorem.  The unconditional global coefficient therefore does
not change.

## 1. Facet-braid literalization

For a path `T_0,...,T_l`, put `S_i=T_(i-1) cap T_i` and choose endpoint
facets `S_0` and `S_(l+1)` different from their adjacent selected facets.
Then

\[
 S_i\cup S_{i+1}=T_i,
 \qquad
 S_{i-1}\cup S_i\cup S_{i+1}=T_{i-1}\cup T_i.
\]

The first identity uses lower-rainbow injectivity for internal vertices and
the explicit endpoint choices at the two ends.  Thus a nontrivial path with
`v_j` vertices costs exactly `v_j+1`; an isolated vertex costs one.  The
total pre-repair length is exactly `v+c_+`, and literal completion gives

\[
 N_0+c_++N_-+N_+-2e.
\]

Upper-rainbow injectivity is needed only for the count of distinct selected
upper colours, not for the local OR identities.  The even three-rank and odd
trimmed-lift asymptotics are correct, assuming the later conflict-free
near-spanning **linear** forest recorded in the handoff (not the branching
Greene--Kleitman forest).

## 2. Signed-subcube entropy duality

For the finite incidence matrix `A` of holes versus opposite signed
subcubes, the functional is

\[
 \Psi=\inf_{\lambda\ge0}
 \left(c^T\lambda+2\sum_S e^{-(A\lambda)_S}\right).
\]

The identity

\[
 2e^{-x}=\sup_{y\ge0}
 \left[y\left(1+\log\frac2y\right)-xy\right]
\]

and finite-dimensional Fenchel duality give exactly

\[
 \max\left\{
 \sum_S y_S\left(1+\log\frac2{y_S}\right):
 0\le y_S\le2,\ A^Ty\le c
 \right\}.
\]

Strong duality is justified because the exponential term is finite and
continuous everywhere and the nonnegative orthant has a nonempty domain.
The upper restriction `y<=2` is harmless: the scalar entropy term is
maximal at 2, and lowering a coordinate above 2 only relaxes the packing
constraints.

The deterministic upper bound is also valid.  Bernoulli selection with
probability `1-exp(-lambda)` has expected block cost at most `c lambda` and
leaves a hole with probability `exp(-(A lambda)_S)`.  Equivalently, a
Poisson multiset interpretation makes the linear block-cost term exact.
Thus the dual is exact for the defined Poissonized surrogate; it is not a
claim that `Psi` equals the minimum deterministic repair length or the
minimum Bernoulli expected ledger.

The per-rank dual certificate `y_S=1` is feasible.  For free dimension
`s>=1`, a block meets a fixed rank in at most two slices, hence at most
`2W(s)<=2nu(s)<=c(P,N)` points.  The proof should treat `s=0` separately:
then the opposite subcubes contain at most two singleton sets and the anchor
indicators pay exactly the required one or two entries.  This is a proof
presentation correction, not a counterexample.

## 3. Factorial collision theorem

Write `T=cN+rho`.  Balancing minimizes the `r`th factorial moment at

\[
 \Phi_r=(N-\rho){c\choose r}+\rho{c+1\choose r}.
\]

When an initially empty coordinate is raised successively from `t=0` to
`c`, a donor of load at least `c+1` must exist, and the factorial moment
decreases by at least

\[
 \sum_{t=0}^{c-1}
 \left({c\choose r-1}-{t\choose r-1}\right)
 =(r-1){c+1\choose r}.
\]

This proves, with the exact constant,

\[
 F_r-\Phi_r\ge
 M(r-1){c+1\choose r},
 \qquad 2\le r\le c+1.
\]

The donor argument remains valid after earlier holes have been filled: if
the current marked coordinate has load below `c` and every other coordinate
has load at most `c`, total mass is below `cN`, contradicting
`T>=cN`.  Subsequent ordinary balancing only decreases the moment.

For `r=2`, the factorial excess is exactly half the previously defined
floor-corrected quadratic energy:

\[
 2\Delta_{q,2}
 =\sum_S(\mu_q(S)-\lambda_q)^2-\eta_q.
\]

Hence the denominator `{c_q+1 choose 2}` and all factors of two in the
hole bound are correct.

At the first shadow (`c_1=1`) the exact identity is

\[
 \Delta_{1,2}=M_1+
 \sum_{S:\,\mu_1(S)>0}{\mu_1(S)-1\choose2}.
\]

The positivity restriction is needed unless a special zero convention is
declared.  Writing the sum over all `S` makes `{ -1 choose 2}` undefined
(or equal to 1 under generalized-binomial conventions), so the unrestricted
sum in the submitted statement is a minor notation error.

## 4. Wreath transfer and asymptotics

The exact block length is `n+2H+1`, and it exposes interval lengths from
`m-H` through `m+H+1`.  Complementation pairs every lower hole with exactly
one upper hole.  The common `R`-order reservoir therefore leaves expected
lower defect at most

\[
 \sum_{q=h+1}^{H}N_q(1-n/N_q)^R,
\]

and the factor 2 for complementary repairs is correct.  The literal tail
count `2 sum_(s=0)^(m-H-1) binom(n,s)-1` is also correct.

With

\[
 h^2=m(\log\log m+\gamma),\qquad
 R=\left\lceil e^{-\gamma/2}W/n\right\rceil,
\]

one has

\[
 Rn/N_h\ge \log m\,e^{\gamma/2-o(1)},
\]

so the reservoir residual and traversal cost are `o(W)`.  The stated
Hoeffding tail exponent for
`H=(1/2+epsilon)sqrt(n log n)` is correct.

Finally, uniformly in this range,

\[
 \lambda_q=W/N_q
 =\exp(q(q+1)/m+o(1)),
\]

and `c_q=floor(lambda_q)>=lambda_q/2`, giving

\[
 {c_q+1\choose2}\ge\lambda_q^2/8.
\]

Thus the Gaussian pair-energy condition with weight
`exp(-2q(q+1)/m)` really does imply the normalized factorial condition.

## 5. Remaining gate

The advances reduce the needed construction but do not supply it.  One
still needs exact middle wreath factors for which, through
`h=(1+o(1))sqrt(m log log m)`, either the hybrid certificates sum to `o(W)`
or, more concretely,

\[
 \sum_{q\le h}
 \frac{\Delta_{q,2}}{{c_q+1\choose2}}=o(W).
\]

Separate per-depth load vectors, fractional factors, or the retracted
high-uniformity economical-cover rounding do not establish this integral,
common-factor condition.
