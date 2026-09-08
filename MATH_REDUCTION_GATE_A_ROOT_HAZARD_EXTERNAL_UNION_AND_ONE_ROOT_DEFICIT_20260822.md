# Gate A: root hazard, external-union exposure, and the one-root deficit

**Date:** 2026-08-22  
**Status:** exact infinitesimal theorem and a punctured-residual conditional
bound; the cumulative Gate-A comparison is not proved

This note isolates the sign-indefinite part of the scalar Palm recursion.
For an infinitesimal isolated-edge bite, the average hazard of an ordered
twelve-carrier rooted at (v) is exactly

\[
 d(v)+12E_v-\overline D_{12}(v).
\]

The covariance of the first term with the increasing carrier tail is always
favourable.  The positive part of the duplicate term is bounded by the
existing sixth row-defect.  Hence the only unbounded signed term left in the
survival-selection tangent is the following one-root question:

> can a high-tail root have substantially smaller marginal external
> conflict exposure (E_v) than a Palm-typical root?

This is a strict compression of the twelve-carrier covariance.  It does not
control the finite exact-size bite, the erosion relative to the uniform
slice, or the cumulative stopped history, so it does not close Gate A.

## 1. Definitions

Let (H) be a finite simple hypergraph with edge set (mathcal E), and let
(V_\star) be one prescribed root shore.  Put (Z=|\mathcal E|).  For an
edge (F), a root (v), and an external edge (G), write

\[
 \Gamma(F)=\{G\in\mathcal E:G\cap F\ne\varnothing\},\qquad
 \mathcal S_v=\{F\in\mathcal E:v\in F\},\qquad d_v=|\mathcal S_v|,
                                                               \tag{1.1}
\]

\[
 C_F=|\Gamma(F)|,\qquad
 a_G(v)=|\{F\in\mathcal S_v:F\cap G\ne\varnothing\}|.       \tag{1.2}
\]

Thus (a_G(v)=d_v) when (v\in G).  For (d_v>0), define the marginal
external exposure

\[
 E_v={1\over d_v}\sum_{F\in\mathcal S_v}(C_F-d_v)
     ={1\over d_v}\sum_{G\not\ni v}a_G(v).                  \tag{1.3}
\]

The second identity follows by swapping (F) and (G).

Fix an integer (m\ge2).  An ordered (m)-carrier rooted at (v) is
(\gamma=(v;F_1,\ldots,F_m)), where the (F_i\in\mathcal S_v) are
distinct.  Put

\[
 N_i=\Gamma(F_i)\setminus\mathcal S_v,\qquad
 U(\gamma)=\left|\bigcup_{i=1}^mN_i\right|,\qquad
 D(\gamma)=\sum_{i=1}^m|N_i|-U(\gamma).                       \tag{1.4}
\]

Let (\overline U_m(v)) and (\overline D_m(v)) denote the averages of
these two quantities over the ((d_v)_m) ordered carriers at (v), with
both values set to zero when (d_v<m).  The carrier-Palm root law is

\[
 T_m=\sum_{v\in V_\star}(d_v)_m,\qquad
 \widehat P(v)={(d_v)_m\over T_m}.                            \tag{1.5}
\]

When a carrier-dependent variable is present, the same symbol denotes the
joint law which assigns mass \(1/T_m\) to every ordered carrier
\((v;F_1,\ldots,F_m)\) with distinct \(F_i\in\mathcal S_v\).  Its root
marginal is exactly (1.5).

Fix a real (c\ge m-1), and put

\[
 f_c(d)=(d-c)_+^m,qquad
 \varphi_c(d)=
 \begin{cases}f_c(d)/(d)_m,&d\ge m,\\0,&d<m,\end{cases}
 \qquad A_c={\sum_{v\in V_\star}f_c(d_v)\over T_m}
            =\mathbb E_{\widehat P}\varphi_c(d_v).           \tag{1.6}
\]

Only the case (m=12) is used for Gate A, but no extra work is needed for
the general identity.

## 2. Exact conditional union formula

### Lemma 2.1

For every root with (d_v\ge m),

\[
 \boxed{\overline U_m(v)=mE_v-\overline D_m(v).}              \tag{2.1}
\]

Moreover, with (a=a_G(v)),

\[
 \boxed{
 \overline D_m(v)=\sum_{G\not\ni v}
 \left\{{ma\over d_v}-1+{(d_v-a)_m\over(d_v)_m}\right\}.}   \tag{2.2}
\]

In particular, if

\[
 Q_{2,v}=\sum_{G\not\ni v}(a_G(v))_2,
\]

then

\[
 \boxed{
 0\le\overline D_m(v)
 \le {\binom m2\over(d_v)_2}Q_{2,v}.}                        \tag{2.3}
\]

#### Proof

Averaging the first sum in (1.4) over the ordered carrier chooses every
member of (\mathcal S_v) equally often.  Its mean is therefore (mE_v),
which proves (2.1).

For fixed (G\not\ni v), let (X_G) be the number of the (m) sampled
star edges which meet (G).  It has the hypergeometric law with population
(d_v) and (a_G(v)) successes.  The contribution of (G) to (D) is
((X_G-1)_+).  Since

\[
 \mathbb E(X_G-1)_+=\mathbb EX_G-\Pr(X_G\ge1)
 ={ma_G(v)\over d_v}-1+{(d_v-a_G(v))_m\over(d_v)_m},
\]

summing proves (2.2).  Finally
((x-1)_+\le\binom x2), and the probability that a fixed pair of carrier
positions both meet (G) is ((a_G(v))_2/(d_v)_2).  Summation over the
(\binom m2) pairs and then over (G) proves (2.3).  \(\square\)

## 3. Exact isolated-bite tangent

Independently mark every edge of (H) with probability (p), accept a
marked edge exactly when it has no other marked conflict neighbour, delete
the vertices of every accepted edge, and take the induced residual (H_p).
Define the unnormalised terminal scalar

\[
 A_c(p)={\mathbb E\sum_{v\in V_\star}f_c(d_{H_p}(v))
              \over
              \mathbb E\sum_{v\in V_\star}(d_{H_p}(v))_m}.   \tag{3.1}
\]

The expectations include roots which were deleted, with degree zero.  This
is exactly the scalar obtained by applying the Palm construction to the
unnormalised residual law.

For a current carrier (\gamma), a singleton marked edge kills it precisely
when that edge belongs to

\[
 \bigcup_i\Gamma(F_i)=\mathcal S_v\mathbin{\dot\cup}
                         \bigcup_iN_i.
\]

Thus its singleton hazard is (d_v+U(\gamma)).  If a singleton (G) is
outside that union, the carrier survives and the root degree falls from
(d_v) to (d_v-a_G(v)).  Define the nonnegative averaged erosion

\[
 \mathcal R_{m,c}={1\over T_m}\sum_{v\in V_\star}\sum_{G\not\ni v}
 (d_v-a_G(v))_m
 \{\varphi_c(d_v)-\varphi_c(d_v-a_G(v))\}.                    \tag{3.2}
\]

### Theorem 3.1 (root-hazard/external-union decomposition)

If (T_m>0) and (A_c>0), then the derivative at (p=0) exists and

\[
 \boxed{
 A_c'(0)=
 -\operatorname {Cov}_{\widehat P}(d_v,\varphi_c(d_v))
 -m\operatorname {Cov}_{\widehat P}(E_v,\varphi_c(d_v))
 +\operatorname {Cov}_{\widehat P}(\overline D_m(v),
                                      \varphi_c(d_v))
 -\mathcal R_{m,c}.}                                         \tag{3.3}
\]

The first and fourth terms are nonpositive.  Consequently

\[
 \boxed{
 (A_c'(0))_+
 \le m\,\mathbb E_{\widehat P}
       [ (\overline E-E_v)_+\varphi_c(d_v)]
     +\mathbb E_{\widehat P}
       [\overline D_m(v)\varphi_c(d_v)],}                     \tag{3.4}
\]

where (\overline E=\mathbb E_{\widehat P}E_v).  Equivalently, the
positive logarithmic tangent is at most the right side of (3.4) divided by
(A_c).

#### Proof

For a fixed finite hypergraph, only the no-mark case and singleton mark
sets contribute to the derivative at zero; every singleton is isolated.
The exact Palm one-step quotient therefore gives

\[
 A_c'(0)=-\operatorname {Cov}_{\widehat P}
       (|\cup_i\Gamma(F_i)|,\varphi_c(d_v))-\mathcal R_{m,c}. \tag{3.5}
\]

This can also be checked without probability notation: for any function
(h) with (h(0)=0), the derivative of
(\mathbb E\sum_vh(d_{H_p}(v))) at zero is

\[
 -\sum_{G\in\mathcal E}\sum_{v\in V_\star}
       \{h(d_v)-h(d_v-a_G(v))\}.                              \tag{3.6}
\]

Apply (3.6) to (h=f_c) and (h(d)=(d)_m), differentiate their quotient,
and group surviving carriers; this is (3.5), including (3.2).

Conditional on (v), the mean union hazard is, by Lemma 2.1,

\[
 \mathbb E[|\cup_i\Gamma(F_i)|\mid v]
 =d_v+\overline U_m(v)=d_v+mE_v-\overline D_m(v).              \tag{3.7}
\]

Since (\varphi_c(d_v)) depends only on (v), substituting (3.7) in
(3.5) proves (3.3).

The function (\varphi_c) is nondecreasing.  Indeed, when (d>c),

\[
 {\varphi_c(d+1)\over\varphi_c(d)}
 =\left(1+{1\over d-c}\right)^m{d-m+1\over d+1}\ge1,         \tag{3.8}
\]

because Bernoulli's inequality and (c\ge m-1) make the first factor at
least (1+m/(d-m+1)=(d+1)/(d-m+1)).  The remaining integer transitions
are immediate.  Hence
(\operatorname {Cov}_{\widehat P}(d_v,\varphi_c(d_v))\ge0).
Also (\mathcal R_{m,c}\ge0) term by term.

Finally,

\[
 -\operatorname {Cov}(E_v,\varphi_c)
 =\mathbb E[(\overline E-E_v)\varphi_c]
 \le\mathbb E[(\overline E-E_v)_+\varphi_c],                  \tag{3.9}
\]

and nonnegativity gives
(\operatorname {Cov}(\overline D_m,\varphi_c)
 \le\mathbb E[\overline D_m\varphi_c]).  Equations
(3.3) and (3.9) prove (3.4).  \(\square\)

The decomposition is exact, not a first-order independence heuristic.
The derivative at zero is the literal tangent of the isolated-edge process;
isolation changes only terms of order at least two in (p).  A uniform
finite-bite remainder still has to be proved separately before summing the
tangent along the actual schedule.

## 4. Sixth-defect control of the duplicate term

We now specialize to (m=12).  This subsection is a conditional theorem
for every current residual, including every induced punctured residual; it
does not assert that the hypotheses persist along the punctured process.

Let (n=|V_\star|), choose (z>0), and suppose, for fixed
(\delta,K,a_0>0),

\[
 c\ge11,\qquad c\ge(1+\delta)z,\qquad z\ge8/\delta,\qquad
 d_v\le Kz,qquad T_{12}\ge a_0nz^{12}.                       \tag{4.1}
\]

For integers \(0\le a\le d\), put

\[
 \Phi_z(d,a)=a\{(d-z)^6-(d-z-1)^6\}
              -\{(d-z)^6-(d-z-a)^6\},                        \tag{4.2}
\]

and define the external sixth row-defect

\[
 \mathfrak D_z=\sum_{v\in V_\star}\sum_{G\not\ni v}
                         \Phi_z(d_v,a_G(v)).                   \tag{4.3}
\]

### Lemma 4.1

Under (4.1),

\[
 \boxed{
 \mathbb E_{\widehat P}
 [\overline D_{12}(v)\varphi_c(d_v)]
 \le C_{\delta,K,a_0}{\mathfrak D_z\over nz^6}.}              \tag{4.4}
\]

#### Proof

Twice differencing the sixth power gives the exact nonnegative expansion

\[
 \Phi_z(d,a)=\sum_{s=0}^{a-2}(a-1-s)
 \{30(d-z-s-1)^4+30(d-z-s-1)^2+2\}.                           \tag{4.5}
\]

If (d-z\ge\delta z), (4.1) and a two-case split imply

\[
 \Phi_z(d,a)\ge c_{\delta,K}z^4(a)_2.                         \tag{4.6}
\]

For completeness, if (a\le(d-z)/2), every summand up to a harmless
endpoint adjustment has fourth-power factor
(\Omega_\delta(z^4)), and the triangular weights sum to ((a)_2/2).
If (a>(d-z)/2), retain the first
(\lfloor(d-z)/4\rfloor) summands.  There are
(\Omega_\delta(z)) of them, each has fourth-power factor
(\Omega_\delta(z^4)) and weight (\Omega(a)); the result is
(\Omega(az^5)\), which is at least
(c_{\delta,K}z^4a^2) because (a\le d\le Kz).  The lower bound
(z\ge8/\delta) absorbs all endpoints.

On the support of (\varphi_c), one has
(d_v-z\ge\delta z).  Equation (2.3) and (4.6) therefore give

\[
 (d_v)_{12}\overline D_{12}(v)
 \le {12\choose2}(d_v-2)_{10}Q_{2,v}
 \le C_{\delta,K}z^6
       \sum_{G\not\ni v}\Phi_z(d_v,a_G(v)).                  \tag{4.7}
\]

Also (0\le\varphi_c\le1): for (c\ge11), each of the twelve factors
of ((d)_{12}) is at least (d-c).  Multiply (4.7) by
\(\varphi_c(d_v)/T_{12}\), sum over \(v\), and use
\(T_{12}\ge a_0nz^{12}\).  This proves (4.4).  \(\square\)

Combining Theorem 3.1 and Lemma 4.1 yields the punctured-residual
conditional inequality

\[
 \boxed{
 (A_c'(0))_+
 \le12\,\mathbb E_{\widehat P}
       [(\overline E-E_v)_+\varphi_c(d_v)]
 +C_{\delta,K,a_0}{\mathfrak D_z\over nz^6}.}                 \tag{4.8}
\]

The exact signed normalized external-exposure statistic per unit of the
carrier size is

\[
 \mathcal Y_c(H)=
 {\mathbb E_{\widehat P}
       [(\overline E-E_v)\varphi_c(d_v)]
  \over\mathbb E_{\widehat P}\varphi_c(d_v)}.
\]

The actual logarithmic tangent contains \(m\mathcal Y_c(H)\).  After the
duplicate defect is charged, the following nonnegative one-root statistic
is a sufficient upper bound per unit of carrier size:

\[
 \boxed{
 \mathcal X_c(H)=
 {\mathbb E_{\widehat P}
       [(\overline E-E_v)_+\varphi_c(d_v)]
  \over\mathbb E_{\widehat P}\varphi_c(d_v)}.}                \tag{4.9}
\]

Indeed \(m\mathcal Y_c(H)\le m\mathcal X_c(H)\).  The latter is a one-root
lower-tail statistic for marginal external exposure.  It
contains no ordered-carrier label and no conditional residual environment.
For the punctured catalogue, a proof may control the signed integral of
\(\mathcal Y_c\), or more strongly its upper bound \(\mathcal X_c\), while
also aligning the nonnegative erosion and the uniform-slice drift and
controlling the separately required finite-bite remainder.  Neither a
maximum-degree cap nor the full-catalogue pair profile currently proves
those requirements.

## 5. Exact audit and finite evidence

The verifier

`scratch/audit_gate_a_external_union_decomposition_20260822.py`

checks (2.1)--(2.3) and (3.3) over exact rational arithmetic on several
selected generic hypergraphs.  It also builds the directed punctured
catalogue at (r=3),
deletes the targets of the identity configuration, and checks the
(m=12,c=132) tangent by two independent calculations: direct singleton
deletion and the four terms of (3.3).

For that finite punctured residual the total tangent is negative.  The
external-exposure covariance itself has the adverse sign, but it is offset
by the duplicate covariance, the favourable root hazard, and erosion.  This
is useful diagnostic evidence for the signed decomposition, not an
asymptotic theorem and not evidence that each term separately has the right
sign.
