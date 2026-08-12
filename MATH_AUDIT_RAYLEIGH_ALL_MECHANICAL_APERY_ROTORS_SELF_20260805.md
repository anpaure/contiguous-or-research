# Self-audit of all mechanical Apéry rotor positivity

**Date:** 2026-08-05  
**Method:** independent symbolic replay; pure mathematics; no computation,
search, or solver  
**Audited source:**
`MATH_THEOREM_RAYLEIGH_ALL_MECHANICAL_APERY_ROTORS_POSITIVE_20260805.md`  
**Verdict:** **PASS.**  The floor-clock identity, Euclidean multiplicities,
Beatty support indexing, exact discrepancy moments, Parseval factors, and
final square comparison all check.

## 1. Mechanical clock and fundamental period

For `m=qg+r`,

\[
 qh+\left\lfloor{rh\over g}\right\rfloor
 =\left\lfloor{mh\over g}\right\rfloor,
\]

so the formal clock is exactly the displayed floor sequence.  Floor
superadditivity gives both ordinary and carry inequalities.  A proper
density tie occurs precisely when `g|rh`; hence primitivity is equivalent
to `gcd(g,h)=1`, and division by the gcd leaves the infinite clock
termwise unchanged.

## 2. Multiplicity and Beatty indexing

The integer solutions of

\[
 n\le {mh\over g}<n+1
\]

are counted by

\[
 c_n=\left\lceil{(n+1)g\over h}\right\rceil
     -\left\lceil{ng\over h}\right\rceil.
\]

For `g=ah+b`, this is `a+delta_n`.  When `0<b<h`, the interval

\[
 [nb/h,(n+1)b/h)
\]

has length below one, and contains the integer `ell` exactly for

\[
 n=\lfloor \ell h/b\rfloor.
\]

Coprimality handles every nonzero endpoint; `ell=0,n=0` is included by
the left-closed convention.  Therefore

\[
 \Phi_{g,h}=aC(\eta)+R_{h,b}
\]

is exact, with neither an omitted head term nor an extra multiplicity.

## 3. Sparse Beatty discrepancy moments

For the sparse clock `U_ell=eta floor(ell p/b)`, one has

\[
 U_{\ell+b}=U_\ell+p\eta,
\]

so the counting discrepancy is genuinely `P=peta` periodic.  On the cell
`x=eta(n+u)`,

\[
 H(x)=\left\lceil{b(n+1)\over p}\right\rceil
\]

and hence

\[
 D(x)=A_n+{b\over p}(1-u).
\]

Multiplication by `b` permutes the nonzero residues modulo `p`, so `A_n`
is uniform on `{0,1/p,...,(p-1)/p}`.  The exact moments are

\[
 \mathbb ED={1+b/p-1/p\over2},
\]

and

\[
 \operatorname {Var}(D)
 ={p^2-1\over12p^2}+{b^2\over12p^2}
 ={1+\rho^2-t^2\over12}.
\]

This validates both (3.6) and (3.7).

## 4. Fourier constants

For real periodic `D`, Parseval gives

\[
 \sum_{n\ge1}|\widehat D_n|^2
 ={1\over2}\operatorname {Var}(D)
 ={1+\rho^2-t^2\over24}.
\]

Pairing signs and applying the transform bound gives

\[
 |N|
 <{BP^2\over2\pi^2}
   \sum_{n\ge1}{|\widehat D_n|\over n^2}.
\]

Cauchy--Schwarz and `zeta(4)=pi^4/90` yield

\[
 |N|
 \le {BP^2\over2\sqrt{90}}
      \sqrt{{1+\rho^2-t^2\over24}}
 ={BP^2\over24\sqrt{15}}
      \sqrt{1+\rho^2-t^2}.
\]

Thus the source has the correct factors of two, `P`, and `pi`.

## 5. Final strict dominance

The previously audited all-period theorem gives

\[
 BP^2<12\sqrt{15}M.
\]

Therefore

\[
 |N|<{M\over2}\sqrt{1+\rho^2-t^2}.
\]

The zeroth mode is `(M/2)(1+rho-t)`, and

\[
 (1+\rho-t)^2-(1+\rho^2-t^2)
 =2(\rho-t)(1-t)\ge0.
\]

All quantities being nonnegative, taking square roots is legitimate.
When `b=1`, the last inequality is equality, but the preceding coefficient
bound is strict, so the final phase value remains strictly positive.

## 6. Scope

The theorem signs every rational lower mechanical rotor, including all
primitive Christoffel words, and handles nonprimitive ones after exact
gcd collapse.  It does not prove that all cyclic-block cone extremes are
mechanical, nor that a nonlinear phase minimum occurs at an extreme ray.
It also does not price finite shoulders.

**Final verdict: PASS.**
