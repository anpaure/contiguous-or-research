# Audit of named-hook one-or-two-rail propagation

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_PBBS_NAMED_HOOK_CHAIN_TWO_RAIL_PROPAGATION_20260805.md`  
**Method:** independent component-orbit and cut-topology audit; no search  
**Verdict:** **PASS**, subject exactly to the theorem's stated
all-sufficiently-large-`m` range and named-block scope.

## 1. Defect in the withdrawn formulation

The old two-rail proof silently treated the two rotated `J_b` edges as
lying on one physical component.  Rotation fixes the action profile but can
permute several action-angle components.  This is a real defect: for
example, the displayed near-hook shape at `h=6,b=3` has voltage `9` modulo
`21`, hence a rotation orbit of size `3`.

The corrected theorem does not assume this orbit is trivial.

## 2. Orbit dichotomy

If the displayed near-hook component has orbit size `a_b`, orbit-stabilizer
in the cyclic group `Z_n` gives

\[
 a_b\mid n,\qquad
 J_b(x)=J_b(y)\Longleftrightarrow x\equiv y\pmod {a_b}.
\]

Since `n` is odd, either `a_b=1` or `a_b>=3`.  In an interval of `M`
consecutive rotation indices, one residue class modulo nontrivial `a_b`
occupies at most `ceil(M/a_b)<=M/3+1` places.  The support ledger removes
at most `3B^2` further choices after the first placement.  The theorem's
choice `M>10B^2+10` therefore leaves a placement on a different near-hook
component whenever `a_b>1`.

When `a_b=1`, the centered-interval placement retains the previously
audited antipodal separation on the next voltage-one hook component.  The
rotation multiplier is `m+1` for every named hook, so no change of cyclic
order is hidden between consecutive stages.

## 3. Topology audit

Before a paired stage, write the cycles as `R_0,R_1,A,D_0,D_1`, identifying
equal symbols.  The first clean switch merges `R_0,A,D_0` to `M`.

- If `D_1=D_0`, the second switch cuts once on `R_1` and twice on `M`.
  There are three directed paths.  The clean reconnection is an even
  3-cycle, hence preserves cycle-count parity.  A positive even number no
  larger than three is exactly two.  The already-audited local cut
  permutation splits both `A` and `D_0` material across the outputs.

- If `D_1\ne D_0`, the second switch has one old edge on each of the three
  distinct cycles `R_1,M,D_1`; it therefore merges them to one cycle.

Thus the formerly missing case is not a failure.  It is a strict
improvement from two rails to one.

## 4. Induction audit

The initial connector `G_1` is the explicit rotation-rigid triple.  Its
near-hook voltage is `2`, which is coprime to odd `n`; hence its two copies
necessarily share the same near-hook component and establish the separated
two-rail invariant.

At a later two-rail stage:

- `a_b=1` invokes the same-donor branch and reproduces the separated
  two-rail invariant on `H_(b+1)`;
- `a_b>1` invokes the different-donor branch and enters the absorbing
  one-rail state.

In the one-rail state, one later connector has its hook edge on the current
cycle and its other two edges on fresh action profiles, so it merges three
cycles to one.  The state is invariant to the terminal stage.  Only
neighboring connector types can share action profiles, so accumulated old
supports do not create an unbounded exclusion count.

## 5. Palette and scope audit

All switches are individually selected and q2-neutral.  Protected supports
are disjoint, so the q1/q2 multiset identities compose literally.  The
named block ends with one or two cycles and therefore costs at most two
graphic punctures, or four q2/owner sidecar occurrences.

The theorem does **not** establish a bounded component count for the whole
PBBS factor: the unnamed action-angle components remain.  It also makes no
q3, residence, arbitrary-upper, or common-cap assertion.  No such claim is
used in the proof.
