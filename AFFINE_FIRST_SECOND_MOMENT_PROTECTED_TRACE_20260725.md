# First- and second-moment hashes of an affine geodesic trace

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

One affine coordinate hash supplies more structure than the usual scalar
subset-sum colour.  On every protected signed row, the first subset moment
is affine in phase and the second subset moment is quadratic.  Distinct
moment curves have at most two common colour pairs.

This gives a zero-extra-entropy candidate for dispersing the remaining
cross-slice pair-square term: both moments use the same coordinate labels.
It is not yet a physical-target dispersal theorem.  Distinct physical
targets may share both moment colours, and identical quadratic traces must
be treated separately.

## 1. Affine coordinate strings

Work over a prime field `F_p`, with `p>g+2Q`.  Along one return-free
geodesic write the departure and arrival coordinates as

\[
 a_t,\ b_t\qquad(0\le t<g)
\]

and impose

\[
 h(a_t)=A+\alpha t,
 \qquad
 h(b_t)=B+\alpha t,
 \qquad \alpha\ne0.
 \tag{1.1}
\]

Put `delta=B-A`.  For a Boolean target `S`, define

\[
 \chi_1(S)=\sum_{x\in S}h(x),
 \qquad
 \chi_2(S)=\sum_{x\in S}h(x)^2.
 \tag{1.2}
\]

Let `X_t` be the middle owner, so

\[
 X_{t+1}=X_t-a_t+b_t.
 \tag{1.3}
\]

For signed depth `d in [-Q,Q]`, use `F_d(t)` for the lower flag when
`d<0`, the owner when `d=0`, and the upper flag when `d>0`.

## 2. Exact one-step formulas

### Proposition 2.1 (signed replacement rule)

Put

\[
 \lambda_d=\delta+\alpha d.
 \tag{2.1}
\]

Then consecutive signed-depth flags satisfy

\[
 \boxed{
 \chi_1(F_d(t+1))-\chi_1(F_d(t))=\lambda_d,}
 \tag{2.2}
\]

and

\[
 \boxed{
 \chi_2(F_d(t+1))-\chi_2(F_d(t))
 =\lambda_d\bigl(A+B-\alpha d+2\alpha t\bigr).}
 \tag{2.3}
\]

#### Proof

For `d=-q<0`, the lower flags obey

\[
 F_{-q}(t+1)=F_{-q}(t)-a_{t+q}+b_t.
 \tag{2.4}
\]

The first-moment increment is

\[
 (B+\alpha t)-(A+\alpha(t+q))
 =\delta-\alpha q=\lambda_{-q}.
\]

The difference of squares is the difference times the sum,

\[
 \lambda_{-q}(A+B+\alpha q+2\alpha t),
\]

which is (2.3).  For `d=q>0`, consecutive upper flags replace
`a_{t-q}` by `b_t`; the same calculation gives
`lambda_q=delta+alpha q` and the factor
`A+B-alpha q+2alpha t`.  The case `d=0` is (1.3).  \(\square\)

The usual simultaneous row-rainbow condition is

\[
 \lambda_d\ne0\qquad(|d|\le Q).
 \tag{2.5}
\]

It is enough to choose `delta/alpha` outside `[-Q,Q]` in `F_p`.

## 3. Quadratic moment traces

Summing (2.2)--(2.3) gives constants `c_{1,d},c_{2,d}` such that

\[
 \boxed{
 \chi_1(F_d(t))=c_{1,d}+\lambda_dt,}
 \tag{3.1}
\]

and

\[
 \boxed{
 \chi_2(F_d(t))
 =c_{2,d}+\lambda_d
 \left[t(A+B-\alpha d)+\alpha t(t-1)\right].}
 \tag{3.2}
\]

When (2.5) holds, eliminate `t=(chi_1-c_{1,d})/lambda_d`.
The protected row lies on a quadratic graph

\[
 \chi_2=P_d(\chi_1),
 \tag{3.3}
\]

whose leading coefficient is `alpha/lambda_d`.

### Corollary 3.1 (bounded colour-curve coincidence)

Two protected moment traces whose quadratic polynomials in (3.3) are
different have at most two common pairs `(chi_1,chi_2)` in `F_p^2`.
If their leading coefficients agree, but the polynomials are not
identical, they have at most one common pair.

#### Proof

Common pairs are roots of the difference of two polynomials of degree at
most two.  If the quadratic coefficients cancel, the difference has
degree at most one.  \(\square\)

## 4. Exact residual gate

No second independent coordinate hash was imposed in deriving
(3.1)--(3.3).  Thus the affine-subcatalogue entropy cost is exactly the
same as for the first-moment row colouring already audited.

To turn Corollary 3.1 into the needed four-walk estimate, two additional
statements are required.

1. **Identical-trace multiplicity.**  The total current priority weight of
   different slices inducing the same polynomial `P_d` must be bounded by
   the calibrated target degree, with an `o(1)` collision excess.
2. **Moment-fibre dispersion.**  Within one moment-colour pair, physical
   target-pair labels must not acquire a later-time concentration larger
   than the ideal `z^{-2}` pair-square inflation.

The first is a finite parameter-collision problem in
`(A,B,alpha,c_{1,d},c_{2,d})`.  The second is still a physical membership-
atom statement; moment colours alone cannot imply it, because two distinct
Boolean sets can have identical first and second hash moments.

Thus the quadratic trace is a new exact algebraic input, not a completed
coefficient-one proof.
