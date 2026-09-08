# Audit of the PBBS height-distance obstruction to arbitrary named grafts

**Date:** 2026-08-05  
**Method:** independent line-by-line invariant replay; no computation  
**Audited file:**
`MATH_OBSTRUCTION_NAMED_RELATIVE_C8_GRAFT_HEIGHT_DISTANCE_20260805.md`
**Audited SHA-256:**
`07c98569c2b3a0f844ccddeeabe5722bd1b7017544e1733f796682b39d6e59ea`

## 0. Verdict

**PASS with the stated relative-support quantifier.**  The obstruction
rules out an `O(d)` graft to an arbitrary preassigned PBBS body component.
It does not rule out selecting nearby bodies after the collar is planted,
nor a linear-support graft.

## 1. Height replay

Complementing a rank-`m` owner gives a deficit-one rank-`(m-1)` PBBS
state.  Its Dyck height equals the maximum weight of a cyclic interval,
with members weighted `+1` and nonmembers `-1`.  Swapping one owner
coordinate swaps one zero and one one in that state, so every cyclic
interval weight changes by `0`, `+2`, or `-2`.  This proves the constant
two in Lemma 1.1.

The largest soliton part is invariant under PBBS evolution, so every old
PBBS component has one well-defined height.  A new Middle-Levels incidence
joins two old matching owners which contain the same facet; those owners
are equal or Johnson adjacent.  Therefore every new incidence crosses at
most two height levels.

## 2. Low-height shield replay

For the shield (2.2), its complement chooses exactly one coordinate from
every consecutive pair `(x_i,y_i)`.  Each pair contributes either `10` or
`01`, of net prefix increment zero, and the extra `kappa` is the unique
deficit zero.  The cyclic amplitude is at most two.  Hence every shield
owner lies in a PBBS component of height at most two.

Every attached collar/screen owner is at Johnson distance `O(d)` from a
shield endpoint.  Repeated use of Lemma 1.1 gives height `O(d)` throughout
the protected attachment bank.  The proof does not assert this for an
arbitrary coordinate labelling; it supplies the explicit paired labelling
(2.1), which is sufficient for a counterexample to a universal lemma.

## 3. Contraction replay

After old PBBS components are contracted, unchanged factor edges are
loops.  Only genuinely new incidences can move between contracted
components.  A final component meeting both the protected bank and the
named body therefore projects to a walk with at most `q` new edges.
Height changes by at most two per edge, giving

\[
                         q\ge(H(C)-H_0)/2.
\]

Deleted edges cannot shorten this requirement.  Arbitrarily long travel
inside a PBBS component is already contracted and keeps height fixed.
Counting two newly coloured incidences per switched matching-pair unit
gives the safe denominator four in the alternate support convention.

## 4. Extreme body and scope

The fully nested Dyck word has height `m-1`, while the protected bank has
height `O(d)`.  Therefore the required relative support is `Omega(m)`.
Since `d=Theta(sqrt(m))`, it is not `O(d)`.

This owner/q1 obstruction is present before endpoint-state or upper-backup
requirements are imposed.  Those requirements cannot rescue an infeasible
unconstrained graft.  The negative result is therefore compatible with,
and independent of, the isolated upper-backup packing theorem.

The exact surviving positive problem is body **co-selection** in a local
PBBS height/contact neighbourhood.  Height locality alone is only a
necessary condition; the two-colour alternating-return and typed endpoint
conditions remain open there.
