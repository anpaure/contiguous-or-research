# Bottom companion selector after stopped-hazard cancellation

**Date:** 2026-08-06  
**Method:** synthesis of exact orbit counts, first-hit competing risks, and
the fresh-block hotspot obstruction; no computation or search  
**Status:** the probability/cylinder part of iterative integral rounding is
closed conditionally on one hereditary residual premise.  The remaining
premise is strictly weaker than residual regularity but is not supplied by
the current fresh-path packing theorem.

## 1. What is now unconditional

For the complete fresh `h=2,3` macro orbit, after normalizing carrier load
to one, the exact local rows have scales

\[
 \eta_*={1\over r(d+1)}={H\over Wr},\qquad
 \delta_*=O(d^{-3}),\qquad
 \kappa_*=exp[-\Theta(d\log d)].                         \tag{1.1}
\]

Here `eta_*` is the one-mark root intensity, `delta_*` is the relative
carrier-pair codegree, and `kappa_*` is the additional cost of prescribing
a companion in the same macro.  Pre-reserved banks delete only an
`O(1/d)` fraction of every prospective companion orbit.

Independent proposal rain cannot turn these rows into a near-perfect
selector at unit intensity: it leaves an `e^{-1+o(1)}` fraction of resources
unproposed.  Raising the intensity to cover down to `1/d` costs `Theta(log
d)` per root, which is forbidden.  The one-round isolated nibble preserves
the local cylinder, but summing its stopped one-point envelopes over rounds
does not prove the multi-root cylinder.

The exponential-clock theorem removes both losses.  At every reachable
residual state choose any nonnegative macro rates `x`.  If

\[
 d_x(v,w)\le\delta\min\{d_x(v),d_x(w)\},                  \tag{1.2}
\]

and for every compatible marked cluster `A` of size at most three,

\[
 d_x(A)\le\theta\kappa^{|A|-1}d_x(v(A)),                 \tag{1.3}
\]

then sequential exponential-clock acceptance gives, for every exact
prescribed macro partition `pi` of `m` marked occurrences,

\[
 \Pr(\Pi=\pi)
 \le
 \left[\prod_{j=1}^{|\pi|}
       {1\over1-(j-1)\delta/2}\right]
 \theta^{|\pi|}\kappa^{m-|\pi|}.                        \tag{1.4}
\]

The proof waits for the first accepted macro meeting the live prescribed
root carriers.  Macros missing those carriers may be accepted and the rate
vector may be recomputed arbitrarily.  Bonferroni gives the first-hit
denominator; after summing over the possible first block, unequal root loads
cancel exactly.  Thus there is no sum over rounds or acceptance-time
assignments.

## 2. The amount of residual regularity actually needed

The bottom Haxell step accepts any fixed factor per prescribed root.  Hence
it is enough that, through tested order `q<=K d`,

\[
 \theta\le C_1\eta_*                                      \tag{2.1}
\]

for an absolute `C_1`, and

\[
 \delta\le{\gamma\over d},\qquad K\gamma<2.              \tag{2.2}
\]

Indeed the product in (1.4) is then at most

\[
 \left(1-K\gamma/2\right)^{-q},                           \tag{2.3}
\]

another fixed factor per root.  Carrier degrees themselves may be
arbitrarily unequal.  In an absolute normalization it is enough that live
carrier degrees stay between `1-epsilon_0` and `1`, for any fixed
`epsilon_0<1`; this only rescales the constants.

Thus ordinary pair-codegree is no longer the delicate row.  It may degrade
from `d^{-3}` almost to `d^{-1}`.  The binding invariant is the **relative
marked-cluster ratio** (2.1), especially the singleton row saying that no
live carrier has concentrated onto one marked role.

## 3. Why the existing integral lower packing does not imply it

There is a near-complete packing of the rank-`t` layer by fresh `d`-paths,
with leave `O(M/d)`.  It may nevertheless contain a hotspot: for one fixed
marked owner `(T,z)`, there are

\[
 \Theta\!\left({1\over d^2}{r-1\choose d-2}\right)        \tag{3.1}
\]

pairwise lower-vertex-disjoint packed paths for which `(T,z)` is a legal
companion.  Uniform local tail selection then hits `(T,z)` with probability
`Theta(d^{-2})`, whereas (2.1) requires `Theta(d^{-3})` up to a fixed
factor.  Random pre-reserved banks do not remove the hotspot.

Consequently none of the following is sufficient by itself:

* a maximal or near-perfect fresh lower-path packing;
* uniform local companion selection after that packing;
* complete-orbit pair-codegrees;
* one-round nibble concentration;
* product-residual degree concentration.

The block packing and owner/companion choice must be correlated, or the
packing theorem must be strengthened by a marked-load condition.

## 4. Exact remaining selector lemma

The bottom companion-spread row is reduced to the following statement.

> **Marked-ratio regenerative extension.**  There is a state-dependent
> macro-selection policy which continues until only `O(1/d)` of the
> intended resources remain and such that, before every accepted macro,
> the residual instance admits positive rates on every still-required task
> satisfying (1.2)--(1.3), with (2.1)--(2.2) and
> `kappa=O(kappa_*)`.

This lemma immediately implies `(CE)` by (1.4), then the shared-mark theorem
implies the bank-conditioned two-mark cylinder `(C2)`, and the fixed-factor
bottom theorem completes the Haxell step.

The lemma is weaker than a hereditary fractional factor: no common carrier
degree is required, no `1+o(1)` cylinder constant is required, and the pair
row may lose almost two powers of `d`.  It is stronger than mere positive
extendability because a residual carrier supported on one companion star
violates (2.1).

## 5. Smallest next target

A sufficient deterministic form is a **marked-ratio separator lemma**:
after every partial matching in the chosen policy, move at most `O(W/d)`
carriers in total to the separator so that the remaining macro cone contains
a positive rate vector satisfying

\[
 {d_x(A)\over d_x(v(A))}
 \le C_1\eta_*\kappa_*^{|A|-1}                            \tag{5.1}
\]

for `|A|<=3`, together with the weak pair row (2.2).  Proving (5.1) by a
joint block--owner nibble, an entropy-maximizing residual factor, or a
hotspot-deletion/min-cut theorem would close the companion selector.  No
additional stopped-time or high-order cylinder argument is needed.

## 6. Dependencies

The exact stopped-hazard theorem is
`MATH_THEOREM_EXPONENTIAL_CLOCK_REGENERATIVE_MACRO_ROUNDING_CE_20260806.md`.
Its scope audit is
`MATH_AUDIT_EXPONENTIAL_CLOCK_REGENERATIVE_MACRO_CE_20260806.md`.
The fixed-factor bottom reduction is
`MATH_THEOREM_ANY_FIXED_FACTOR_COMPANION_CYLINDER_SUFFICES_FOR_BOTTOM_HAXELL_20260805.md`.
The hotspot is
`MATH_OBSTRUCTION_FRESH_BLOCK_HOTSPOT_DEFEATS_LOCAL_COMPANION_SAMPLING_20260805.md`.

