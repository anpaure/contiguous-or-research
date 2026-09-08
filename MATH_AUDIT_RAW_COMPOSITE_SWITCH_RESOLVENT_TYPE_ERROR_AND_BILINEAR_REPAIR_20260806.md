# Audit of the raw composite switch: resolvent type error and bilinear repair

**Date:** 2026-08-06  
**Method:** operator-type check against `(5.25)--(5.28)` and the Bellman
counterterm; no computation or search  
**Verdict:** Sections 3--7 of
`MATH_THEOREM_RAW_COMPOSITE_SWITCH_COEFFICIENT_IDENTITY_AND_FULL_CHANGE_GATE_20260806.md`
are invalid.  Section 2 may be retained only as a scalar coefficient
identity.  It does not identify the Bellman boundary.  The proposed
private-order switches close the pristine generator identity, but do not
yet close the stopped bilinear boundary.

## 1. The type error

For a resource type `T`, the Johnson resolvent

\[
 R_T=L_T^\dagger B_T
\]

acts on the resource Hilbert space

\[
 \mathcal H_T=\ell^2_0(\Omega_T).
\]

For a composite row `A`, by contrast,

\[
 u=(K_Tf)(A)=\sum_{x\in U_A^\circ\cap T}f_x
\]

is a scalar.  The expressions `||u||_R`, `||u-v||_R`, and the vector
polarization in equation `(3.2)` of the raw-switch note are therefore
undefined.  No canonical embedding of this scalar into `H_T` is specified,
and choosing one would change the claimed estimate.

The vectors on which `R_T` legitimately acts are:

1. the actual resource profile `f_{T,i}`;
2. a resource innovation `delta f_{T,i}` in the carre-du-champ; or
3. a signed Johnson-edge incidence `b_{xy}=e_x-e_y`.

The scalar `K_Tf(A)` is none of these.

## 2. Incidence-vector form does not rescue `(FSW)`

Let

\[
 z_A=\sum_{x\in U_A^\circ\cap T}e_x,
 \qquad K_Tf(A)=\langle z_A,f\rangle.
\]

If a private switch replaces exactly one occurrence `x` by `y`, then

\[
 z_A-z_{A'}=e_x-e_y.
\]

This is a valid resource vector.  But the covariance boundary is

\[
 \begin{aligned}
 (K_Tf(A))^2-(K_Tf(A'))^2
  &=(f_x-f_y)
    \bigl(2\langle z_{A\cap A'},f\rangle+f_x+f_y\bigr).
 \end{aligned}
\tag{2.1}
\]

It is not `||e_x-e_y||_R^2`, and it is not controlled by that resistance
without an additional estimate on the common word sum.  Thus the fact that
the changed set has one occurrence does not by itself pay the stopped
covariance boundary by `(ROc)`.

## 3. The actual Bellman identity

Write the current covariance operator as

\[
 B_{T,i}=K_{T,i}^*M_iK_{T,i},
 \qquad
 \langle f,B_{T,i}f\rangle
   =\sum_A\mu_i(A)(K_Tf(A))^2.
\tag{3.1}
\]

Let `L_{T,i}` be the current linearized resource-removal operator, with the
normalizations of `(5.25)--(5.28)` in the joint-Lyapunov note.  The valid
counterterm is

\[
 \widetilde C_i
   =\sum_T\beta_T(i)\langle f_{T,i},R_Tf_{T,i}\rangle.
\tag{3.2}
\]

Its linear drift contains the bilinear form

\[
 \langle f,R_TL_{T,i}f\rangle
\]

(with the symmetric real part when the stopped operator is not
self-adjoint), while its noise term contains

\[
 \mathbb E_i\langle\delta f,R_T\delta f\rangle.
\]

On the pristine orbit the cancellation is the well-typed identity

\[
 \boxed{
 \langle f,R_TL_Tf\rangle=\langle f,B_Tf\rangle.}
\tag{3.3}
\]

After stopping, the operator residue is the net bilinear form

\[
 \boxed{
 \langle f,(B_{T,i}-B_T)f\rangle
 +\operatorname {Re}\langle f,
        R_T(L_T-L_{T,i})f\rangle,}
\tag{3.4}
\]

together with the non-isotropic noise and predictable coefficient terms
already listed in `(5.35)` and `(JRES)`.  In the one-sided formulation it
must be controlled only after being combined in the Bellman supersolution
`(4.5)`/`(JBEL)`.  Equation `(3.4)`, not `(FSW)`, is the stopped row.

For a missing Johnson generator edge `xy` of weight `w`, the symmetrized
second term is explicitly

\[
 {w\over2}\langle f,
   (R_Tb_{xy}b_{xy}^*+b_{xy}b_{xy}^*R_T)f\rangle
 =w(f_x-f_y)\bigl((R_Tf)_x-(R_Tf)_y\bigr).
\tag{3.5}
\]

This is sign-indefinite and is not the resistance
`<b_xy,R_T b_xy>`.  The latter appears in the quadratic variation of a
literal edge innovation, not in the linear stopped-generator boundary.

## 4. What the private-order generator really proves

The component-local private order involution remains useful if its static
host claims pass audit.  Averaging it over the complete coordinate orbit
gives

\[
 \sum_{xy}w_{xy}(f_x-f_y)^2
   =\alpha_T\langle f,L_Tf\rangle.
\tag{4.1}
\]

Consequently

\[
 \langle f,R_T(\alpha_TL_T)f\rangle
   =\alpha_T\langle f,B_Tf\rangle.
\tag{4.2}
\]

This is exactly the pristine cancellation already required by `(5.28)`.
At a stopped boundary, however, one must compare the covariance-row loss
in `(2.1)` with the generator boundary `(3.5)` plus the future-relation
counterterm.  A one-occurrence switch makes this comparison local, but does
not make it automatic.

## 5. Status of the coefficient calculation

The first-kill fugacity calculation in Section 2 of the raw-switch note may
correctly identify the scalar weight of a killed composite row.  Even if
so, it only weights the first term of `(3.4)`.  The Bellman boundary is a
coupled covariance/generator/noise expression, so equality of killed-row
coefficients does not prove its sign or dominate it.

In particular, the four companion-incidence cases in Section 4 of the
private-order note are not currently proved to be `(ROc)`/`(FE3)` terms.
The cited equations `(5.3)--(5.5)` define the rooted intersection variance
polynomial; they are not an identity for the coefficient difference of a
local composite switch.

## 6. Correct remaining lemma

A proof-safe local target is:

> **Private-switch Bellman boundary lemma.**  Sum the net expression
> `(3.4)`, its adjoint-gradient analogue, non-isotropic noise, and changing
> future coefficients over the earliest-blocker partition of the private
> one-occurrence generator.  Its positive part, after the exact pristine
> cancellation `(4.2)`, is bounded by the existing future selected-relation
> potential and the literal `(ROc)`/`(FE3)` injections at total scale
> `O(M/d^4)`.

The lemma must keep the covariance term `(2.1)` and the generator term
`(3.5)` together.  Proving the two separately by absolute values would
recreate the stronger unresolved `(JRES)` row and can lose a slow Johnson
factor.

Until this lemma is proved, neither `(FSW)` nor the current private-order
note closes `(JVAL)` or the raw cleanup estimate.

