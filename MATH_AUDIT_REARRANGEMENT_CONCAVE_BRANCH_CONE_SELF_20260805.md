# Self-audit: rearrangement concave-branch cone

**Date:** 2026-08-05  
**Audited file:**
`MATH_THEOREM_REARRANGEMENT_CONCAVE_BRANCH_CONE_AND_SCALAR_APERTURE_20260805.md`  
**Verdict:** **GO** as an abstract conditional theorem.  It does not place
the Rayleigh orbit in the cone.

## 1. Differential orientations

At negative depth `s`,

\[
 H(L(s))=H(R(s))=-s
\]

gives `L'=1/g>0` and `R'=-1/f<0`.  Therefore the component length
decreases with depth.  As physical length increases, `L` moves left and
`R` moves right.  Left concavity makes `g=-H'` nondecreasing in the
spatial variable, so it decreases under that left motion.  Right
concavity makes `f=H'` nonincreasing, so it decreases under the right
motion.  Their parallel sum therefore decreases.  Thus `-C'` decreases,
`C'` increases, and `C` is convex.  All signs agree.

## 2. Shape propagation

On the old positive support, `RH=H-C`; both summands are concave because
`H` is concave and `-C` is concave.  After the old zero, `RH=-C`, which is
increasing and concave.  If `H(0)>q`, its value at zero is positive while
its value at the old zero is negative.  Concavity then permits exactly one
crossing and puts the new minimum at the old zero.  The new origin and
depth are exactly

\[
 P-q,\qquad C(a).
\]

Therefore another cone step requires the separately stated scalar
`P-q>C(a)`.

## 3. Counterexample arithmetic

For the exact kernel in Section 5 of the theorem:

* the linear branch reaches zero at `a=1` and `-3/4` at `b=19/16`;
* positive area is `3/4+1/8=7/8`;
* negative left area is `9/128`;
* with `lambda=96/103`, negative right area is `103/128`;
* total negative area is `112/128=7/8`;
* at depth `s=1/4`, the component length is

  \[
  {1\over8}+{103\over96}\log3>1.
  \]

Since component length decreases with depth, `C(1)>1/4=P-q`.  Thus zero
area, continuity, concave branches, and `P>q` genuinely do not imply the
next aperture.

## 4. Rayleigh scope

The imported exact inequality `g_2'(b-)<0` gives
`(RK)''(b-)>0`.  Hence `RK` fails the cone hypothesis on its full left
branch.  No statement in the theorem or this audit treats the missing
concavity of `R^2K` as proved.
