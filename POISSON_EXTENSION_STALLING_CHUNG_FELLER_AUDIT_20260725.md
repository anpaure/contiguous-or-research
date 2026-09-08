# Audit: extension clustering, product-survival stalling, and Chung--Feller phase classes

Date: 2026-07-25

Method: pure mathematics only.

## 0. Verdict

Three scope corrections are required.

1. The proposed Poisson law for `ext_q` uses the wrong mean.  The
   extension count is identically divisible by `q+1`; one displayed lower
   interval contributes all `q+1` of its middle extensions in one cluster.
   The natural Poisson variable is the wreath-occurrence multiplicity
   `mu_q`, of mean `W/N_q`, not `ext_q`, of mean `(q+1)W/N_q`.  Therefore
   no theorem concentrates the obstruction at `q=O(1)`.
2. `M z^K` is an exact first moment only for an independently thinned
   resource universe (with a common survival density `z`).  It is a useful
   no-go for a product-survival trajectory of one hard augmented orbit,
   but it is not a no-go for the actual catalogue under an aligned or
   factor-preserving residual.  It also gives an upper survival scale, not
   by itself a matching lower scale.
3. The Chung--Feller flaw parameter `e` does not produce `m` or `m+1`
   different exact factors.  The classes `D_{2m}^e` are different
   transversals of the same Catalan family of MSW cycles.  Changing `e`
   merely changes the chosen starting state (hence the phase/orientation
   presentation) of each existing cycle.  It gives no new physical wreath
   support and no shadow averaging.

## 1. Exact clustering of the extension count

Let `n=2m+1`, let `F` be one exact middle wreath factor, and fix

\[
 R\in\binom{[n]}{m-q}.
\]

Write

\[
 \mu_{F,q}(R)
 =\#\{\pi\in F:R\text{ is a cyclic }(m-q)\text{-interval of }\pi\}.
 \tag{1.1}
\]

Let `ext_q(R)` count middle sets `X superset R` whose unique owning wreath
in `F` displays `R` as a cyclic interval.

### Proposition 1.1 (extension clustering identity)

For every `R`,

\[
 \boxed{\operatorname{ext}_q(R)=(q+1)\mu_{F,q}(R).}
 \tag{1.2}
\]

Consequently

\[
 \boxed{
 \sum_R\mu_{F,q}(R)=W,
 \qquad
 \sum_R\operatorname{ext}_q(R)=(q+1)W.}
 \tag{1.3}
\]

#### Proof

A fixed cyclic interval of length `m-q` lies in exactly `q+1` cyclic
intervals of length `m`: extend it by `a` coordinates on the left and
`q-a` on the right, for `a=0,...,q`.  All of those middle intervals belong
to the same wreath and hence are owned by that wreath in the exact factor.
Conversely, every extension counted by `ext_q(R)` arises in this way.
This proves (1.2).  Every wreath has exactly `n` cyclic intervals of length
`m-q`, and `|F|=W/n`, which gives (1.3). \(\square\)

In particular, `ext_q(R)` takes values only in

\[
 0,q+1,2(q+1),\ldots .
\]

It cannot be approximately Poisson with its own mean
`(q+1)W/N_q` when `q` grows.  Under an independent-wreath-occurrence
heuristic, the plausible law is instead

\[
 \mu_{F,q}(R)\approx\operatorname{Poisson}(\lambda_q),
 \qquad \lambda_q={W\over N_q},
 \tag{1.4}
\]

and therefore

\[
 \Pr(\operatorname{ext}_q(R)=0)
 =\Pr(\mu_{F,q}(R)=0)
 \approx e^{-\lambda_q},
 \tag{1.5}
\]

not `exp(-(q+1)lambda_q)`.

For `q=o(m^{2/3})`,

\[
 \log\lambda_q
 ={q(q+1)\over m}
 +O\!\left({q^3\over m^2}+{q\over m}\right).
 \tag{1.6}
\]

Thus:

* if `q=o(sqrt(m))`, then `lambda_q=1+o(1)` and the Poisson hole
  probability stays near `e^{-1}`;
* if `q=A sqrt(m)` for fixed `A`, it stays at the positive constant
  `exp(-exp(A^2))`;
* substantial automatic Poisson decay begins only once `q/sqrt(m)` tends
  to infinity (for example around the familiar
  `sqrt(m log log m)` reservoir scale).

Even (1.5) is only a model prediction.  Equation (1.3) alone is a first
moment and gives no upper bound on the number of zeros.  An exact factor
may be strongly sub-Poisson or strongly clustered.  A structural tail
reduction still needs an anticoncentration/extension-spread theorem.

## 2. Exact scope of the `M z^K` calculation

Let `O` be a finite edge catalogue with `M=|O|`, every edge using `K`
distinct resource vertices.  Retain every resource independently with
probability `z`.  Then, without any assumption on edge overlaps,

\[
 \boxed{
 \mathbb E|O_{\rm live}|=Mz^K,
 \qquad
 \Pr(O_{\rm live}\ne\varnothing)\le Mz^K.}
 \tag{2.1}
\]

More generally, if an edge uses `k_i` resources in stratum `i`, retained
independently at density `z_i`, then

\[
 \boxed{
 \mathbb E|O_{\rm live}|
 =M\prod_i z_i^{k_i}.}
 \tag{2.2}
\]

The single power `z^K` is justified only when all relevant strata have the
same product survival density.

For one simple `S_n`-orbit of a template, `M<=n!`.  For the full
floor-calibrated odd template,

\[
 K=n+2\sum_{q\le Q}
 \left\lfloor{nN_q\over W}\right\rfloor
 =(1+o(1))n\sqrt{\pi m}
 \tag{2.3}
\]

when `Q/sqrt(m)->infinity`.  Hence

\[
 {\log M\over K}
 \le(1+o(1)){\log n\over\sqrt{\pi m}}.
 \tag{2.4}
\]

If an independent residual consumes a fraction

\[
 (1+\varepsilon){\log n\over\sqrt{\pi m}}
\]

of every stratum, then (2.1) tends to zero superpolynomially and the orbit
has no live edge with high probability.  This is a genuine product-model
ceiling.

It is not an actual-catalogue no-go for four separate reasons.

1. A matching residual is the complement of previously selected whole
   edges and is highly correlated with the catalogue; its edge-survival
   probability need not be `z^K`.
2. An aligned residual can deliberately preserve many complete edges even
   at a density far below the product threshold.
3. A union of template types, formal-copy or priority orbits, or a larger
   genuine group action can have far more indexed edges than one simple
   coordinate orbit.  Its actual `M` must be recomputed.
4. From `Mz^K>>1` one cannot infer the existence of a live edge without a
   second-moment or structural argument.  Thus (2.4) gives an upper
   survival scale; the word `Theta` requires an additional lower-side
   theorem.

The correct conclusion is therefore:

\[
 \boxed{
 \text{one giant hard edge cannot follow an independent product
 trajectory deep enough, but correlated integral alignment is not ruled
 out.}}
 \tag{2.5}
\]

The same qualification applies to fixed-size random thinning.  Its exact
edge survival is hypergeometric rather than `z^K`; at the present
exponential stratum sizes it is asymptotic to the product expression, but
it is still an exogenous random-residual theorem, not an endogenous
matching theorem.

## 3. The Chung--Feller parameter does not give new factors

Let

\[
 \mathcal D_{2m}^e
\]

be the balanced paths with exactly `e` flaws.  The MSW maps give
bijections

\[
 f:\mathcal D_{2m}^e\longrightarrow\mathcal D_{2m}^{e+1}.
 \tag{3.1}
\]

For `x in D_{2m}^0`, put

\[
 x_e=f^e(x)
\]

(with the usual interleaved `g`-states in the odd cycle).  The resulting
MSW cycle contains exactly one `x_e` from every flaw class.  Since every
map `x mapsto x_e` is a bijection, every fixed flaw class is a transversal
of the same Catalan set of cycles.

Therefore starting the construction from class `e` merely chooses the
`e`-th representative on each already existing cycle.  As an unoriented
cycle factor,

\[
 \boxed{F^{(e)}=F^{(0)}\qquad(0\le e\le m).}
 \tag{3.2}
\]

Depending on conventions, the displayed vertex list or omitted-label word
may be cyclically shifted or reversed.  Neither operation changes the
physical wreath support or any cyclic-interval multiplicity.  In
particular, averaging the alleged `m` phase factors cannot reduce a lower
shadow defect: it averages identical physical factors.

To obtain genuinely different exact factors one must alter the MSW
pairing/flip rule, conjugate by a coordinate permutation not stabilizing
the factor, or perform a legal factor trade.  The flaw index `e` alone does
none of these.

## 4. Corrected frontier

The three audited observations leave the following valid conclusions.

* Extension clustering destroys the proposed `q+1` Poisson exponent; the
  shallow obstruction is not proved to be concentrated at bounded depth.
* The hard augmented-orbit calculation is a clean warning against
  independent product survival, not a theorem against correlated
  near-factors or dynamically aligned residuals.
* The canonical Chung--Feller construction supplies one exact physical
  wreath factor, presented through `m+1` flaw-class transversals, not
  `m+1` distinct factors.

None of these claims proves or disproves coefficient one.  They prevent
three attractive but invalid shortcuts from being used in its proof.
