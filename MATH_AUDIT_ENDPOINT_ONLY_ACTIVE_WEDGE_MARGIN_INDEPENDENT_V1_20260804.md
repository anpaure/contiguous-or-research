# Independent audit V1: endpoint-only active-wedge margin

**Date:** 2026-08-04  
**Verdict:** **GO** at the endpoint-factorized fixed-state scope.  No
computation, search, or solver output is used.

Audited theorem:
`MATH_THEOREM_ENDPOINT_ONLY_ACTIVE_WEDGE_MARGIN_20260804.md`,
SHA-256
`1c443748c354042951c485cf52289b7db5bf349c3b75151ef73b8978d1e13093`.

Author audit:
`MATH_AUDIT_ENDPOINT_ONLY_ACTIVE_WEDGE_MARGIN_20260804.md`,
SHA-256
`4c0cfd02b7afaf771ee1272a3403522dde0e81f954cd8d04810fb6f8add80a0e`.

## 1. Exact active-menu count

A full wedge at one lower turn is an edge of `K_m` on the extension
coordinates.  It has no star-active side exactly when both endpoints lie
outside `A_i`, giving

\[
 {m-a_i\choose2}
\]

unsupported wedges.  Every other edge has at least one active side.  The
definition of `t_i` counts exactly the forbidden terminal pairs among this
supported edge set, not unsupported pairs.  Hence

\[
 |W_i^c|
 ={m\choose2}-{m-a_i\choose2}-t_i
 =B_{a_i}(m)-t_i.
\]

No double counting occurs when both orientations of one wedge are active,
because the menu is indexed by the unordered q1 terminal pair.

## 2. Packing and private routing

The exact protected-wedge packing theorem requires the strict menu floor

\[
 |W_i^c|>B_{p-1}(m).
\]

The displayed count is therefore sufficient.  Every selected menu element
has at least one active side and a nonforbidden terminal; choosing such a
side gives its typed direct branch.  The completion-stable occurrence and
no-hidden-capacity hypotheses are precisely those needed by the automatic
private-routing theorem, so the selected routes coexist.

The selected bank has two incidences per lower turn and distinct owner
values.  Under degree compatibility and the stated total edge budget, the
small protected-factor theorem applies exactly.

## 3. Simple endpoint floor

For `1<=p<=m-1`,

\[
 B_p(m)-B_{p-1}(m)=m-p.
\]

If `a_i>=p`, monotonicity gives `B_(a_i)>=B_p`.  If additionally
`t_i<=m-p-1`, then

\[
 |W_i^c|
 \ge B_p-(m-p-1)
 =B_{p-1}+1.
\]

Thus the strict packing threshold is met with exactly one candidate of
integer margin.

## 4. Sharpness

With `a_i=p-1` and no forbidden terminals, the menu has exactly
`B_(p-1)(m)` elements.  The attained prefix-conflict construction from the
menu theorem can block every one, so the owner-side floor cannot be lowered
in a cardinality-only implication.

With `a_i=p`, the additional edges beyond the first `p-1` active stars are
exactly the `m-p` edges from the new active coordinate to the still-inactive
coordinates.  Forbidding precisely these q1 terminals leaves

\[
 B_p-(m-p)=B_{p-1}.
\]

The same sharp prefix can block the retained menu.  Therefore the strict
terminal row `t_i<=m-p-1` is also optimal at the minimal owner-side floor.

This sharpness is correctly scoped to a uniform endpoint-count proof; extra
structure or more than `p` active sides can provide additional margin.

## 5. Scope

The theorem assumes universal direct fan activity from every declared active
side except for the explicitly enumerated terminal holes, all in one fixed
completion-stable cap state.  Ordinary gammoid rank, nonloop counts, or
activation obtained in different states do not imply that premise.

The independent V1 verdict is **GO** at the hashes listed above.
