# The all-mesh comb theorem gives a global Apéry stability tube

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation or search  
**Status:** unconditional corollary.  Every first-minimum-normalized formal
Apéry clock lies at a mesh no larger than the Rayleigh minimum.  The
all-mesh arithmetic-comb theorem therefore upgrades the former
small-mesh-only stability ball to one uniform tube covering every possible
normalized mesh.  A nonpositive clock must have either fixed relative
residue displacement or fixed adverse finite-shoulder debt.  Converting
either defect into physical Boolean reserve remains open.

## 1. Uniform arithmetic margin

Let

\[
 c_*={377\over108000}.                           \tag{1.1}
\]

The centered-phase theorem proves

\[
                         C(h)=\sum_{m\ge0}K(mh)>c_*
 \qquad(h>0).                                    \tag{1.2}
\]

Put

\[
 B_A=\|K'\|_1+A\operatorname {Var}(K'),
\tag{1.3}
\]

and

\[
 \varepsilon_*=min\left\{{1\over2},{c_*\over2B_A}\right\}>0.
\tag{1.4}
\]

## 2. Every normalized maximum density is in range

Let a saturated first-`zeta` table have size `N`, endpoint
`T in[zeta,2zeta)`, and maximum density

\[
                         \lambda=\max_{1\le j\le N}{a_j\over j}.
\tag{2.1}
\]

### Lemma 2.1

\[
                         0<\lambda\le\zeta<A.    \tag{2.2}
\]

### Proof

For `j<N`, first crossing gives `a_j<zeta`, and hence
`a_j/j<zeta`.  If `N>=2`, then

\[
 {T\over N}<{2\zeta\over N}\le\zeta.
\]

If `N=1`, saturation gives `T=zeta`, so `T/N=zeta`.  Taking the maximum
proves (2.2). `square`

## 3. Global stability and dichotomy

Let the formal Apéry clock be

\[
 U_m=\lambda m+\beta_{m\bmod g},
 \qquad\beta_0=0,
 \qquad\beta_r\le0,
\tag{3.1}
\]

and put

\[
 \Delta=\max_r(-\beta_r).                       \tag{3.2}
\]

Let `V` be the exact finite-availability Bellman clock and let

\[
 \mathscr S^-=
 \sum_{m<L}\bigl(K(U_m)-K(V_m)\bigr)_+          \tag{3.3}
\]

be its adverse shoulder debt.

### Theorem 3.1 (global formal-clock stability tube)

If

\[
                         \Delta\le\varepsilon_*\lambda,
\tag{3.4}
\]

then

\[
                         \boxed{\Phi(U)>c_*/2.} \tag{3.5}
\]

Consequently, if `Phi(V)<=0`, then at least one of

\[
                         \boxed{\Delta>\varepsilon_*\lambda} \tag{3.6}
\]

or

\[
                         \boxed{\mathscr S^-\ge c_*/2}       \tag{3.7}
\]

holds.

### Proof

The bounded-variation sampling theorem gives, when
`Delta<=lambda/2`,

\[
 \Phi(U)\ge C(\lambda)
 -{\Delta\over\lambda}
  \bigl(\|K'\|_1+\lambda\operatorname {Var}(K')\bigr).
\tag{3.8}
\]

Lemma 2.1 gives `lambda<A`, so the parenthesis is at most `B_A`.
Equations (1.2), (1.4), and (3.4) imply

\[
 \Phi(U)>c_*-\varepsilon_*B_A\ge c_*/2,
\]

which proves (3.5).

The exact shoulder identity gives

\[
                         \Phi(V)\ge\Phi(U)-\mathscr S^-.
\]

If (3.6) fails, (3.5) holds; then `Phi(V)<=0` forces (3.7). `square`

## 4. Exact gain and limitation

The earlier stability theorem required an unspecified sufficiently small
mesh `lambda<=h_0`.  Lemma 2.1 and the all-mesh comb theorem remove that
restriction completely: every normalized formal Apéry clock lies in the
same uniform arithmetic tube.

This does not prove all-price positivity.  A putative counterclock may
still have the displacement (3.6) or the shoulder debt (3.7).  The result
does prove that **mesh size is no longer a third escape mechanism**.  The
remaining conversion theorem has only the two named defects, with fixed
dimension-free thresholds.

## 5. Dependencies

1. `MATH_THEOREM_RAYLEIGH_ARITHMETIC_COMB_CENTERED_PHASE_IDENTITY_20260805.md`;
2. `MATH_THEOREM_RAYLEIGH_APERY_ARITHMETIC_STABILITY_AND_SHOULDER_DEBT_DICHOTOMY_20260805.md`;
3. `MATH_THEOREM_RAYLEIGH_FIRST_MINIMUM_CROSSING_AND_COMPACT_PERIOD_APERTURE_20260805.md`.
