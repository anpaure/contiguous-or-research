# Independent audit: literal occurrence coalescence and the aligned `Ibc/Ica` reduction

**Date:** 2026-08-04  
**Method:** independent pure-mathematical audit; no computation, search, or
solver  
**Audited theorem:**
`MATH_THEOREM_LITERAL_OCCURRENCE_FACT_COALESCENCE_AND_IBC_ICA_BACKGROUND_REDUCTION_20260804.md`  
**Audited SHA-256:**
`8476036e42ff39e2d4abb1d24b39eeda89a45d01e4808fa96bcea0a3d5b95b0c`  
**Verdict:** `GO`.  The theorem now incorporates the complete-bundle
semantic correction and explicitly deletes the remaining noncoalescible
bundle footprint in the forced-edge contraction.  The fixed-state
compound-record principle, corrected matching reduction, and conditional
aligned `Ibc/Ica` specialization are exact.  No common terminal cap,
transported background, or two-phase common matching follows.

## 1. The underlying OR-word semantics

For a fixed literal word `A`, an interval address `e` has one value

\[
                         v(e)=\operatorname{OR}_A(e).
\]

The universal-word definition does not create one capacity for each
semantic use of `e`.  It creates one interval occurrence.  Consequently,
if a complete certificate already uses `e` and certifies the fact
`v(e)=Z`, then recording that same occurrence as the ordinary witness of
target `Z` does not create a second interval address.

This applies to all three native roles occurring in the aligned bundle:

1. a lower target assignment can share its exact port occurrence;
2. a central owner witness can share its exact owner occurrence; and
3. an upper target witness can share its exact terminal occurrence.

There is no hidden exclusivity in the definition of a universal OR word.
Distinctness is required between different rows of the lower-target
matching, not between every semantic label attached to one already
materialized interval.  Likewise, an upper target only needs an occurrence;
it does not reserve that occurrence against another compatible role.

An auxiliary model may impose the stronger rule that a route endpoint, an
owner transit vertex, or a terminal sink must be unused by every other
service.  In that stronger model coalescence is unavailable unless a
compound-record rule is added explicitly.  Such exclusivity is a property
of the auxiliary model, not of literal OR-word semantics.

## 2. Necessary correction to “logical-only socket role”

Theorem 1.2 is correct exactly as a statement about records which add no
new occurrence resource or literal constraint.  However, the complete
`Ibc/Ica` socket from the aligned ambient theorem is not, in its entirety,
a logical-only label.  Its native route physically uses the port, owner
(unless declaratively contracted), and q1 terminal occurrences.

The valid order of construction is therefore:

1. select one complete polarized bundle and charge each occurrence in its
   physical footprint once;
2. require the bundle to retain the exact address, value, phase, guards,
   endpoints, terminal type, and cap state;
3. attach the ordinary target/owner/upper-witness service to the already
   charged occurrence when that service asserts the identical fact; and
4. keep every further type or route requirement inside the same compound
   record.

Under this interpretation, the **additional ordinary service** is
logical-only relative to the complete bundle, and coalescence is exact.
It would be misleading to infer instead that the whole socket route is
logical-only or consumes no occurrence capacity.

Equivalently, a proof-safe replacement for the relevant premise is:

> there exists one accepted complete canonical record whose capacity
> footprint contains `e` once and whose conjunctive services include both
> the physical socket role and the ordinary fact `(Z,e)`.

This is precisely the kind of complete-record premise used in the folded
polarized-socket theorem and in the source-free dual-role router theorem.
It is not supplied merely by equality of Boolean values.

## 3. Exact forced-edge contraction

Let `H subseteq L times C` be the target/cell graph after one literal word
and one complete cap/guard/phase state have been fixed.  Let

\[
 E_*=\{(Z_a,e_a):a\in A_*\}
\]

be pairwise target- and cell-disjoint forced edges, and put
`L_*={Z_a}` and `C_*={e_a}`.  Let `B_*` be every other occurrence in the
mutually feasible selected bundle footprint which remains unavailable to
an ordinary assignment after all admitted compound facts have been
coalesced.  A matching saturating `L`, containing `E_*`, and coexisting
with the bundles exists if and only if

\[
                  H-(L_*\cup C_*\cup B_*)
\]

has a matching saturating `L minus L_*`.  The exact Hall form is

\[
 \boxed{
 |N_H(X)\setminus(C_*\cup B_*)|\ge |X|
 \qquad(X\subseteq L\setminus L_*).}
\tag{3.1}
\]

Formula (3.1) is the unambiguous forced-edge contraction.  Omitting `B_*`
would be false in general: a bundle can coalesce at its forced cell while
also reserving a different route cell needed by the only residual matching
edge.  The patched theorem now prices exactly that possibility.

The proof is the standard exact bijection

\[
                 M_0\longleftrightarrow M_0\cup E_*.
\]

No capacity is double-counted when the socket services are part of the
same compound records as `E_*`; no unavailable residual capacity is
silently reused because `B_*` has been deleted.

### Scope of this contraction

The reduction is exact for the ordinary target/cell matching in a fixed
realized state.  It is not an automatic common-cap theorem for a candidate
graph assembled before the word or trace guards are fixed.  In that earlier
setting, individually sound edges can still fail simultaneous cap/trace
compatibility.  Formula (3.1) prices the selected socket bundle footprint,
not arbitrary noncoalesced interiors of transported background routes.
Those further capacities must likewise be deleted, contracted under a
proved adaptive-recourse equality, or included in a larger compound
record.

## 4. Audit of the aligned `Ibc/Ica` specialization

Fix one phase `epsilon` and the exact antecedent `A^epsilon` from
`MATH_THEOREM_ALIGNED_IBC_ICA_AMBIENT_BIRAIL_AND_POLARIZED_BUNDLES_20260804.md`.
For `1<=j<d`, its displayed native cells satisfy

\[
\begin{aligned}
 \operatorname{OR}(p_{j-1})
  &=K\cup V_L^\epsilon\cup
       (F\setminus\{f_{j-1},f_j\})=:R_j^\epsilon,\\
 \operatorname{OR}(o_{j-1})
  &=K\cup V_L^\epsilon\cup(F\setminus\{f_{j-1}\}),\\
 \operatorname{OR}(q_{j-1})
  &=K\cup V_L^\epsilon\cup F=:U^\epsilon.
\end{aligned}
\tag{4.1}
\]

The port values `R_j^epsilon` are pairwise distinct.  The port addresses,
owner addresses, and q1 terminal addresses are separately injective in
`j`; interval length separates different roles.  The upstream prefix and
suffix ray addresses are also pairwise distinct and carry the exact
phase-specific birail targets.  These facts were independently audited in
the aligned ambient theorem.

Therefore, **if one accepted complete polarized bundle is selected for
every `j` in the same state**, then:

* assign each distinct strict-lower target `R_j^epsilon` to its own port
  `p_(j-1)`;
* retain the central owner fact at `o_(j-1)` while using or declaratively
  contracting that owner inside the same complete route;
* use one chosen `q_(j-1)` as the ordinary witness of the single upper
  target `U^epsilon`; and
* use the remaining, occurrence-distinct `q_(j-1)` cells only as socket
  terminals.

Every selected interval is charged once.  Thus the apparent collision
between palette service and native socket service is not a literal
capacity obstruction.

### What is not proved by the specialization

1. **Typed acceptance remains open.**  The logical polarity bit does not
   prove that the terminal cap accepts the complete product type.
2. **The two phases remain separate.**  The same address generally has a
   different Boolean value in phases `P` and `Q`.  Coalescence in
   `A^0` and coalescence in `A^1` do not produce one common background
   matching or one common terminal cap.  The pointwise union of the two
   antecedents is only a containment cap, not an exact antecedent.
3. **Background interiors remain priced.**  Forced-edge contraction removes
   assignment collisions only.  A transported path that traverses a bundle
   cell in an incompatible role, or shares a different unit resource, must
   still be handled jointly.
4. **The upper duplicate is one target, not `d-1` targets.**  All
   `q_(j-1)` values equal `U^epsilon`; only one is needed as the ordinary
   upper witness.  Their multiplicity remains useful solely as distinct
   socket capacity.
5. **No global regeneration follows.**  The argument is local to the
   displayed exact antecedent and complete bundle bank.

With these qualifications, Theorem 3.1 and Corollary 3.2 of the audited
document are sound.  The phrase “the socket attaches only a logical role”
should always be read as “after the complete socket bundle has been charged,
the additional ordinary service is a coalescible logical role.”

## 5. Final verdict

The exact gain is real:

\[
\boxed{
\text{one complete occurrence may simultaneously serve its own target,
owner/upper role, and accepted socket role, and is charged once.}}
\]

The exact remaining global condition is correspondingly smaller: contract
every accepted compound bundle fact first, then solve the residual literal
matching and all noncoalesced route capacities in one common state.

This does **not** establish that the requisite compound terminal type is
accepted, that the residual matching exists, or that phase `P` and phase
`Q` coexist in one regenerative cap.  Those remain the substantive cap and
regeneration gates.

## 6. Dependencies checked

- `MATH_THEOREM_ALIGNED_IBC_ICA_AMBIENT_BIRAIL_AND_POLARIZED_BUNDLES_20260804.md`
  at SHA-256
  `7906b08d7d7953b2d8a22730fa6cd79f637f2f2e732890696155e3e1b0d3770e`;
- `MATH_THEOREM_FOLDED_C8_NESTED_TERMINAL_INVARIANT_AND_POLARIZED_SOCKET_20260804.md`
  at SHA-256
  `a6dba7ab6eab0e14e47552ab52ce00a2962969a6168f08972946720c6224fe53`;
- `MATH_THEOREM_DIAGONAL_INTERVAL_DIAMOND_SOURCE_FREE_DUAL_ROLE_ROUTER_20260803.md`
  at SHA-256
  `2e71b1f3a7c26c23accf9e3cee9a23ba01ef17658f959b73ac69c622ce2a2802`;
- `MATH_THEOREM_TERMINAL_COMMON_CAP_TWO_CROSS_RAY_RADO_GAMMOID_V2_20260803.md`;
- `MATH_THEOREM_R_COMMON_CAP_GUARD_PRUNING_ROBUST_HALL_LIFT_20260731.md`.
