# Self-audit: PBBS single-soliton forced-cycle obstruction

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_PBBS_SINGLE_SOLITON_FORCED_CYCLE_OBSTRUCTION_20260805.md`  
**Method:** independent symbolic replay of every parenthesis cancellation;
no computation or search  
**Verdict:** **PASS**, within the explicit fixed-centered-PBBS scope.

## 1. Orbit replay

For `D=1^m0^m`, the marked first-maximum up-step is the final one, so the
rooted update is

\[
 \phi(D)=\overline{0^m}\,0\,\overline{1^{m-1}}
        =1^m0^m.
\]

Its physical displacement is `m`.  Since `gcd(m,2m+1)=1`, the `f`-period
is exactly `n=2m+1`.  It is odd, so squaring does not split the cycle.

The forward distinguished deletion in the two-step formula is the final
up-step of the mountain.  Removing it leaves one run of `m-1` ones and one
run of `m+2` zeros.  Rotation of this word has full period `n`, because a
binary cyclic word with exactly one nonempty run of each symbol cannot be
fixed by a nonzero proper rotation.  Hence the `n` q1 colours on the
component are distinct.

## 2. Multiplicity replay

For

\[
 K=1^{m-1}z_0z_1\cdots z_{m+1},
\]

forward cancellation pairs the old ones with
`z_0,...,z_(m-2)` and leaves

\[
 U_+(K)=\{z_{m-1},z_m,z_{m+1}\}.
\]

Reverse cancellation across the cyclic boundary pairs the old ones with
`z_(m+1),...,z_3` and leaves

\[
 U_-(K)=\{z_0,z_1,z_2\}.
\]

The exact angle-occurrence theorem says a fixed point `u` of
`beta_K alpha_K` must lie in `U_-(K)`.  For `m>=3`, replay the three
possibilities.

* `u=z_0`: after the flip the word is `1^m0^(m+1)`, whose forward survivor
  is `z_(m+1)`.
* `u=z_1`: cancel the new `1` with `z_2`, the last old `1` with `z_0`, and
  the remaining old ones successively; the survivor is `z_(m+1)`.
* `u=z_2`: cancel the new `1` with `z_3`, the last two old `1`s with
  `z_0,z_1`, and the remaining old ones successively; the survivor is
  `z_(m+1)`.  This is exactly where `m>=3` is used.

After flipping `z_(m+1)`, reverse cancellation first pairs the new terminal
one with `z_m`, then pairs the old one-run cyclically with
`z_(m-1),...,z_1`, leaving `z_0`.  Therefore

\[
 \beta_K\alpha_K(z_a)=z_0\qquad(a=0,1,2),
\]

and only `z_0` is fixed.  Thus `mu(K)=1`.  PBBS commutes with coordinate
rotation, so all `n` component colours have multiplicity one.

## 3. Max-height and Hall replay

The deficit-three decomposition of `K` has two empty blocks and the single
block `1^(m-1)0^(m-1)`.  The max-height rule is therefore forced to retain
the unique occurrence above.  More strongly, multiplicity one forces every
q1 section to retain it.

For the one-cycle Hall cut, every incident colour has capacity
`q_R=mu_R-1=0`, so the exact capacitated right side is zero while the cycle
demand is one.  This is a genuine minimal Hall obstruction, not a mere
failure of the particular representative rule.

## 4. Boundary and scope

For the rectangular extension, direct complementation verifies

\[
 \phi((1^u0^u)^b)
 =1^u(0^u1^u)^{b-1}0^u=(1^u0^u)^b.
\]

After deleting the final up-step of the first mountain, the first modified
mountain contributes the block `1^(u-1)0^(u-1)`, the next unmatched zero
is immediately followed by another unmatched zero, and the remaining
`b-1` mountains form the third block.  The height triple is therefore
`(u-1,0,u)` for `b>=2`, making the current occurrence nonmaximal and a
different maximum-block occurrence available.  For `b=1`, it is
`(m-1,0,0)`, recovering the rigid cycle.  This proves the stated
rectangular classification without claiming anything about nonrectangular
action sectors.

At `m=2`, the third candidate lacks two old ones to absorb both preceding
zeros; a second fixed point survives.  The theorem correctly isolates
`m>=3` and states only that the max-height section is cyclic at `m=2`.

The proof does not exclude changing the ambient Johnson carrier, adding a
Pascal cross edge, or applying a palette-preserving local factor surgery.
It excludes only representative selection within the fixed centered PBBS
occurrence factor.  The stated scope is therefore exact.
