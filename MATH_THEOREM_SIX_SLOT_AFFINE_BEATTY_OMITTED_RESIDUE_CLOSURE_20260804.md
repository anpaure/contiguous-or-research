# Six-slot affine Beatty clock: closure by the omitted residue classes

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves the explicit
headless size-five/subthreshold-period gate produced by the affine
setup-cost no-descent family at grid six strictly positive.  The proof is
one exact residue-complement identity and one degree-seventeen rational
Taylor certificate.  It uses no numerical sampling or search.

Put

\[
 A={\sqrt\pi\over2},\qquad d={A\over10},
\]

and let

\[
 C(d)=\sum_{m\ge0}K(md)>0
\tag{0.1}
\]

be the proved arithmetic all-ceiling clock.

The affine setup-cost table

\[
 {A\over10}(0,1,3,5,7,9,10)
\tag{0.2}
\]

has the exact Bellman functional

\[
\begin{aligned}
 \Phi_6=\sum_{q\ge0}\bigl(&K((9q)d)+K((9q+1)d)
 +K((9q+3)d)\\
 &+K((9q+5)d)+K((9q+7)d)\bigr).
\end{aligned}
\tag{0.3}

## 1. Residue complement

Define the omitted-residue train

\[
 \Omega=
 \sum_{q\ge0}\bigl(
 K((9q+2)d)+K((9q+4)d)+K((9q+6)d)+K((9q+8)d)
 \bigr).
\tag{1.1}
\]

The selected residues `{0,1,3,5,7}` and omitted residues `{2,4,6,8}`
partition `Z/9Z`.  Therefore

\[
                         \boxed{C(d)=\Phi_6+\Omega.}
\tag{1.2}
\]

It is enough to prove `Omega<0`.

## 2. Twelve retained Gaussians

For the four compact omitted arguments `rd`, `r in {2,4,6,8}`, write
`u=r/10`.  Since `0<u<1`,

\[
 K(Au)=1-e^{-\pi(1-u)^2/4}-e^{-\pi(1+u)^2/4}.
\tag{2.1}
\]

The first tail row, `q=1`, is

\[
 K((9+r)d)=-e^{-\pi(1+(9+r)/10)^2/4}.
\tag{2.2}
\]

Every row with `q>=2` is strictly negative.  Hence, with

\[
\begin{aligned}
 \mathcal T=\{&1/5,2/5,3/5,4/5,
 6/5,7/5,8/5,9/5,\\
 &21/10,23/10,5/2,27/10\},
\end{aligned}
\tag{2.3}

one has the strict upper bound

\[
                         \Omega
 <4-\sum_{t\in\mathcal T}e^{-\pi t^2/4}.
\tag{2.4}

## 3. Exact degree-seventeen certificate

Define the odd Taylor polynomial

\[
                         Q_{17}(x)=
 \sum_{j=0}^{17}{(-x)^j\over j!}.
\tag{3.1}

Taylor's theorem with Lagrange remainder gives

\[
                         e^{-x}>Q_{17}(x)
                         \qquad(x>0),
\tag{3.2}

because the degree-eighteen remainder has positive sign.  Also
`pi<22/7`, so

\[
 e^{-\pi t^2/4}
 >e^{-11t^2/14}
 >Q_{17}(11t^2/14).
\tag{3.3}

The following is one exact rational inequality.  Expanding (3.1) at the
twelve rational arguments in (2.3), collecting over a common positive
denominator, and subtracting `401/100` gives

\[
\begin{aligned}
 &\sum_{t\in\mathcal T}Q_{17}(11t^2/14)-{401\over100}\\
 &\quad=
 {1107521168275515646975339594998344921314175828988640776532351139
  \over
  2464861067577089663016747663360000000000000000000000000000000000000}
 >0.
\end{aligned}
\tag{3.4}

This is a finite integer comparison, not a decimal estimate.  Equations
(3.3)--(3.4) prove

\[
                         \sum_{t\in\mathcal T}e^{-\pi t^2/4}
                         >{401\over100}.
\tag{3.5}

Substitution in (2.4) yields

\[
                         \boxed{\Omega<-{1\over100}.}
\tag{3.6}

## 4. Closure of the six-slot affine gate

Combining (0.1), (1.2), and (3.6),

\[
 \boxed{
 \Phi_6=C(A/10)-\Omega
 >C(A/10)+{1\over100}>{1\over100}>0.
 }
\tag{4.1}

Thus the explicit grid-six triple-inert-junction clock is not a Bellman
separator.  Its positivity comes from the negativity of the four omitted
residue classes, not from first-crossing size descent.

## 5. General omitted-residue sign gate

The same residue identity isolates the exact analytic question for the
balanced affine family in every grid.  Let `h>=2`, put

\[
 d_h={A\over2h},\qquad L_h=2h-1,
\]

and define the selected and omitted residues modulo `L_h` by

\[
 S_h=\{0,1,3,\ldots,2h-3\},
 \qquad
 E_h=\{2,4,\ldots,2h-2\}.
\tag{5.1}

Let

\[
 \Phi_h=\sum_{q\ge0}\sum_{r\in S_h}K((qL_h+r)d_h),
\]

and

\[
 \Omega_h=\sum_{q\ge0}\sum_{r\in E_h}K((qL_h+r)d_h).
\tag{5.2}

Since `S_h` and `E_h` partition `Z/L_hZ`, one has the exact identity

\[
                         \boxed{C(d_h)=\Phi_h+\Omega_h.}
\tag{5.3}

Consequently the sign statement

\[
                         \boxed{\Omega_h<0}
\tag{5.4}

is sufficient to close the balanced affine setup-cost clock at grid
`n=h+1`, because then `Phi_h>C(d_h)>0`.

The present theorem proves (5.4) for `h=5`, with the stronger margin
`Omega_5<-1/100`.  It does not prove (5.4) uniformly in `h`, does not
close every grid-six efficiency branch, and does not prove the all-grid
Bellman inequality.

## 6. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| affine setup-cost clock and exact five-coset form | `MATH_THEOREM_AFFINE_SETUP_COST_FIRST_CROSSING_AND_APERY_NO_DESCENT_20260804.md` | `408aacd10f2e20bf26364f6464d06a7d0fb9c4d179e93e21b8a26482ce7405ce` |
| strict arithmetic all-ceiling margin | `MATH_THEOREM_SMOOTH_BINOMIAL_CONFIGURATION_DUAL_AND_CEILING_PRICE_CLASSES_20260804.md` | `c3a2c1858f59fa32e61d2f9a9252085ad7fb01f3521ab5cb46998705123e103d` |
