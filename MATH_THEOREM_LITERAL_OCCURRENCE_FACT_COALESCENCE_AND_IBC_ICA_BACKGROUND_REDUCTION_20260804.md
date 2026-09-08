# Literal occurrence facts coalesce ordinary assignments with aligned `Ibc/Ica` sockets

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional semantic and matching reduction.  On the literal
OR-word capacity model, after one complete physical socket bundle has been
selected and its footprint charged once, an ordinary target assignment and
the bundle service which assert the same occurrence fact consume that
occurrence once, not twice.
For the audited aligned `Ibc/Ica` bank this removes the apparent collision
between its native ports/upper turns and their ordinary palette roles.  It
does not prove that the transported background has a matching on the
complement, that a terminal specification accepts the polarized product
type, or that all data occur in one regenerative global cap state.

## 0. Result

Fix one literal word `A` and one complete cap/guard/phase state `c`.  A
physical occurrence is an interval address `e`, with the unique fact

\[
                 \mathsf f(e)=(e,\operatorname{OR}_A(e),c).
\tag{0.1}
\]

An ordinary target assignment `Z -> e` and a service inside an already
charged complete socket bundle are **fact-coalescible** at `e` when

1. `Z=OR_A(e)`;
2. the socket asserts the same address, value, and state (0.1);
3. its type/polarity field is logical metadata: it adds no new literal
   membership, absence, guard, or endpoint requirement at `e`; and
4. neither role requires `e` to be unused by the other.

Then both roles may be recorded on one unit occurrence inside the same
compound record.  The maximal common cap and every literal target witness
are unchanged.  The other occurrences in the physical socket route remain
charged normally.  In particular, a background compiler matching need not
avoid such a socket occurrence merely because it supplies that occurrence's
own exact target fact.

This is sharp.  If the socket asks for another value or state, adds a
physical constraint, or carries an exclusive-unused condition, the two
roles are not coalescible.  In the single-role unit-node model they form two
demands behind one capacity-one vertex, so no relabelling or polarity bit
can make them simultaneous.

For the aligned `Ibc/Ica` bank, ticket `j`, `1<=j<d`, uses native port
`p_(j-1)` and upper turn `q_(j-1)`.  Their exact facts are already

\[
 \operatorname{OR}(p_{j-1})
 =K\cup V_L^\epsilon\cup
       (F\setminus\{f_{j-1},f_j\}),                 \tag{0.2}
\]

\[
 \operatorname{OR}(q_{j-1})
 =K\cup V_L^\epsilon\cup F,                         \tag{0.3}
\]

where `V_L^epsilon={infinity,c,x_epsilon}`.  The complete polarized socket
physically uses its native route, but at the port and terminal it asserts
precisely these same facts.  Therefore, conditional on typed acceptance and
selection of the complete bundles, the ordinary lower-q1 role of every
`p_(j-1)` and the ordinary upper-witness role of every `q_(j-1)` coalesce
with the already charged socket bank at zero **additional** occurrence
charge.

The exact remaining background condition is a forced-edge contraction: the
strict-lower target/cell graph, after removing the target rows already
certified by the complete bundles, their chosen occurrence cells, and every
other noncoalescible cell in the selected bundle footprint, must match all
remaining targets in the same state.  Requiring the transported background
to avoid a coalescible socket cell *before* this contraction is stronger
than literal OR semantics.

## 1. Occurrence capacity is not role capacity

Let `C(A)` be the set of interval addresses of `A`.  Each `e in C(A)` has
one Boolean value

\[
                         v(e)=\operatorname{OR}_A(e). \tag{1.1}
\]

An ordinary compiler assignment is a sound edge `(Z,e)` with `Z=v(e)`.
A matching uses different addresses for different target rows.  A complete
socket record may mention the same address together with a route role,
logical ticket, polarity, and terminal type.

The physical load of a selected record family is measured on **distinct
occurrence addresses**.  Repeating the equality `v(e)=Z` in two parts of a
certificate does not create a second interval in the word.  This is the
same distinction as the source-free interval-diamond theorem: Hasse labels
and semantic roles are not additional physical cells unless a stronger
model explicitly prices them.

### Definition 1.1 (logical-only role)

A role `rho` attached to `e` is logical-only over the fixed state `c` when
its complete record

\[
                         (\rho,e,v(e),c)              \tag{1.2}
\]

adds no constraint on the letters of `A` beyond the already asserted fact
`OR_A(e)=v(e)`, and does not require exclusive ownership of `e`.

The role may retain a ticket label, ray side, cut index, and polarity.  Those
fields can distinguish meanings without duplicating the address capacity.

### Theorem 1.2 (idempotent occurrence-fact coalescence)

Let `(Z,e)` be an ordinary target assignment and let `rho_1,...,rho_t` be
logical-only roles attached to the same exact fact `(e,Z,c)`.  Replacing the
assignment and all role records by the single compound record

\[
                   (e,Z,c;\ \text{assignment},
                           \rho_1,\ldots,\rho_t)       \tag{1.3}
\]

preserves

1. the ordinary target witness;
2. every role assertion;
3. the literal maximal-cap constraints; and
4. unit occurrence capacity.

The occurrence `e` is charged once.

#### Proof

Items 1 and 2 all use the same equality `OR_A(e)=Z`.  By Definition 1.1,
the role fields add no further condition on `A`.  In the maximal-cap
formulation, assigning `Z` to `e` constrains every letter in `e` to lie in
`Z` and requires traces whose union is `Z`.  Repeating the identical
constraint is idempotent, so the cap and its trace decoration do not change.
Finally, unit capacity is attached to the interval address `e`; (1.3) is one
complete conjunctive record on that address, not `t+1` independently
selectable records.  Hence its load is one. \(\square\)

### Corollary 1.3 (sound matching overlaps are automatically value-aligned)

In one fixed literal word, if two sound target/cell edges meet the same
cell, their target values agree.

#### Proof

Both target values equal the unique value `v(e)`. \(\square\)

Thus a literal background matching cannot use a socket address for a
different target.  Its only possible overlap with an ordinary role of the
socket is the exact fact to which Theorem 1.2 applies.

## 2. Exact compound-background reduction

Let `L` be a target family, `C` a physical occurrence bank, and `H` the
sound target/cell graph in one fixed literal state.  Let

\[
              E_* =\{(Z_a,e_a):a\in A_*\}\subseteq H \tag{2.1}
\]

be pairwise target- and cell-disjoint forced facts carried by complete
socket bundles.  Put

\[
 L_*=\{Z_a:a\in A_*\},\qquad C_*=\{e_a:a\in A_*\}. \tag{2.2}
\]

Assume the selected complete bundles are mutually feasible in the fixed
state.  Let `B_* subseteq C minus C_*` be the rest of their physical
occurrence footprint which is unavailable to an ordinary assignment after
all accepted compound facts have been coalesced.  Thus every selected
bundle cell outside `C_* union B_*` which remains in `H` is explicitly
admitted to coinstantiate its own exact ordinary target fact.

### Theorem 2.1 (forced-edge contraction with socket roles)

Assume every socket role on `e_a` is fact-coalescible with `(Z_a,e_a)`.
Then a literal compiler matching containing all facts `E_*` and coexisting
with all socket roles exists if and only if the residual graph

\[
                    H-(L_*\cup C_*\cup B_*)           \tag{2.3}
\]

has a matching saturating `L\setminus L_*`.

Equivalently, the exact residual condition is

\[
 |N_H(X)\setminus(C_*\cup B_*)|\ge |X|
       \qquad(X\subseteq L\setminus L_*).            \tag{2.4}
\]

No extra capacity term is charged for the socket roles.

#### Proof

If `M_0` saturates the residual target shore in (2.3), then

\[
                         M=M_0\cup E_*                 \tag{2.5}
\]

is a matching saturating `L`.  Theorem 1.2 compounds every edge of `E_*`
with its socket roles without changing the cap or cell load, and the
residual matching avoids `B_*` by construction.  Conversely, delete `E_*`
from any full matching containing it.  Coexistence with the selected
bundles forbids every noncoalescible cell in `B_*`, so what remains is a
matching of (2.3) saturating `L\setminus L_*`.  Equation (2.4) is Hall's
criterion for that residual matching. \(\square\)

### Corollary 2.2 (an already realized background causes no assignment
collision)

Suppose one literal compiler matching `M` already exists in the same state.
Any socket address used by `M` is assigned its own exact value by Corollary
1.3.  Hence every overlap with a logical-only socket role can be replaced by
one compound record.  Ordinary target assignment alone creates no socket
collision.

This corollary does **not** say that arbitrary background *routing paths*
are disjoint from socket routes.  Any additional path interiors remain
physical capacities and must be priced jointly.

### Frozen-background warning

Deleting all capacities of one named background realization before forming
the socket network treats a coalescible endpoint as unavailable and can
therefore be strictly stronger than (2.3).  The exact options are:

1. factor the coalesced background edge out first and put it in the complete
   socket bundle, then delete only the genuinely noncoalescible bundle and
   residual background capacities; or
2. use an adaptive/compound formulation which retains the joint record.

Ordinary gammoid contraction does not perform this identification
automatically.

## 3. Specialization to the aligned `Ibc/Ica` bundles

Fix phase `epsilon` in the audited ambient theorem.  For `1<=j<d`, put

\[
 r_j=p_{j-1}(s),\qquad t_j=o_{j-1}(s),\qquad
 u_j=q_{j-1}(s).                                    \tag{3.1}
\]

Write

\[
 V_L^\epsilon=\{\infty,c,x_\epsilon\}.              \tag{3.2}
\]

The native-diamond identities give

\[
\begin{aligned}
 R_j^\epsilon
 &=\operatorname{OR}(r_j)
   =K\cup V_L^\epsilon\cup
      (F\setminus\{f_{j-1},f_j\}),\\
 T_j^\epsilon
 &=\operatorname{OR}(t_j)
   =K\cup V_L^\epsilon\cup(F\setminus\{f_{j-1}\}),\\
 U^\epsilon
 &=\operatorname{OR}(u_j)
   =K\cup V_L^\epsilon\cup F.
\end{aligned}                                       \tag{3.3}
\]

The first two families are value-injective in `j`; the upper value
`U^epsilon` is independent of `j`.  The addresses `r_j,t_j,u_j` are
separately injective, and the complete bundle theorem proves that the
records for distinct `j` are pairwise disjoint in every finite occurrence
coordinate.

The exact upstream ray facts are

\[
 X_j^\epsilon=J\cup\{x_\epsilon\}\cup P_j,
 \qquad
 Y_j^\epsilon=J\cup\{y_\epsilon\}\cup S_j.          \tag{3.4}
\]

They occur at the pairwise distinct addresses displayed in the ambient
theorem.  Their values have smaller filler support than (3.3), so they are
distinct from the native port and upper facts; the prefix and suffix
families are also distinguished by the active labels `x_epsilon` and
`y_epsilon`.

### Theorem 3.1 (zero-charge palette/socket coalescence)

Assume the fixed terminal state accepts and selects the complete polarized
native bundle whose terminal code is

\[
               (R_j^\epsilon,\text{prefix polarity}),
               \qquad
               (U^\epsilon,\text{suffix polarity})   \tag{3.5}
\]

on `r_j,u_j`, with the complete upstream facts (3.4) retained and the
bundle footprint charged once.  Assume further that the ordinary service at
`r_j,u_j` adds no new literal or exclusivity condition.  Then all `d-1`
complete aligned bundles coexist with the
ordinary assignments

\[
                         R_j^\epsilon\longmapsto r_j
                         \quad(1\le j<d)              \tag{3.6}
\]

and with the ordinary upper-witness role of `U^epsilon`, at zero additional
occurrence charge beyond the already selected physical bundle bank.

One may assign the unique upper target `U^epsilon` to any one chosen
`u_j`.  The other `u_j` are distinct duplicate occurrences used only as
socket terminals.  No target is counted more than once, and every socket
terminal remains a distinct unit occurrence.

The same conclusion holds for the central owner fact at `t_j` whenever the
route retains it as transit: owner service and transit assert the same
occurrence fact.  Alternatively, the complete native-diamond bundle may
contract `t_j` as a declarative internal owner, exactly as in the
source-free dual-role router theorem.

#### Proof

Equations (3.3) identify the ordinary palette values with the native values
used in (3.5) at the same addresses and state.  Under the logical-only
acceptance premise, Theorem 1.2 coalesces (3.6) with the port roles and
coalesces one upper assignment with its selected `u_j`.  The remaining
upper-turn addresses are not ordinary assignments of additional copies of
`U^epsilon`; they are distinct socket capacities carrying the same Boolean
value.  Pairwise occurrence disjointness of the full bundle bank prevents
cross-ticket capacity collisions.  The owner assertion follows by the same
argument, or by the cited complete-bundle contraction. \(\square\)

### Corollary 3.2 (sharp residual background premise)

Let `D^epsilon` be the set of distinct ordinary targets certified inside
the complete bundle bank: the two ray families (3.4), the lower-q1 family
`{R_j^epsilon}`, and one copy of the upper target `U^epsilon` (with central
owners treated in the owner row rather than the strict-lower compiler).

After choosing their displayed occurrence witnesses, simultaneous
background coexistence reduces to one literal matching on the complementary
target shore and complementary occurrence bank in the same cap state.
There is no separate requirement that this background avoid a bundle cell
which it uses for that cell's own exact target fact.

## 4. Sharp no-go outside the coalescence face

### Proposition 4.1 (single-role unit cut)

Suppose a cap model represents the ordinary assignment at `e` and a socket
role at `e` as two independent demands, both required to traverse one
capacity-one occurrence vertex, and forbids role coinstantiation.  Then the
two demands cannot be simultaneous.

#### Proof

The cut consisting of the occurrence vertex `e` has capacity one and
separates two demands from their declared services.  Equivalently, two
vertex-disjoint paths cannot both contain `e`. \(\square\)

A polarity bit distinguishes logical meanings but does not increase the cut
capacity.  Therefore Theorem 3.1 cannot be obtained inside a single-role
model by relabelling alone; the exact compound record must be admitted.

### Proposition 4.2 (value/state/exclusivity sharpness)

Fact coalescence is not justified if any of the following occurs:

1. the two roles claim different Boolean values at the same address;
2. they refer to different physical addresses with equal value;
3. they live in different cap/guard/phase states;
4. one role imposes an additional literal membership or absence condition;
5. one role requires the occurrence to be unused by every other service; or
6. two different ticket labels try to share the same socket occurrence
   without an explicit within-ticket coalescence rule.

#### Proof

Case 1 contradicts uniqueness of `OR_A(e)`.  Case 2 concerns two capacities,
not one common fact.  Cases 3--5 violate Definition 1.1.  Case 6 leaves two
independent unit demands at one capacity and is Proposition 4.1. \(\square\)

The aligned bank avoids Case 6 because the `u_j` are occurrence-distinct,
even though their Boolean values agree.

## 5. Exact frontier after coalescence

The aligned `Ibc/Ica` theorem plus Theorem 3.1 closes the local **duplicate
capacity accounting** question:

\[
 \boxed{
 \text{charged complete socket + its ordinary service on the same fact}
 \text{ charges that occurrence once.}}
\tag{5.1}
\]

It removes neither of the following genuinely different rows.

1. **Typed acceptance.**  The cap must admit (3.5), with the same phase,
   flags, endpoints, guards, cut label, and product polarity.  The ordinary
   fact `OR(e)=Z` does not by itself prove that acceptance predicate.
2. **Complement background/common state.**  One ambient source word and cap
   state must realize the bundle facts and a compiler matching on the
   complement from Corollary 3.2.  Coalescence prevents double charging but
   does not create that matching or its guards.

If a transported background is a collection of longer routing paths rather
than only ordinary target/cell assignments, every noncoalesced interior
capacity must additionally avoid the socket bank or be included in a larger
complete compound record.

Thus the former phrase "the socket bank must be disjoint from the whole
background" can be sharpened to:

> after identical occurrence facts are contracted into their complete
> bundles, the remaining background paths and assignments must be disjoint
> and feasible in one accepted cap state.

This is the weakest proof-safe premise currently supported by the literal
semantics.

## 6. Dependencies

- `MATH_THEOREM_ALIGNED_IBC_ICA_AMBIENT_BIRAIL_AND_POLARIZED_BUNDLES_20260804.md`
- `MATH_AUDIT_ALIGNED_IBC_ICA_AMBIENT_BIRAIL_AND_POLARIZED_BUNDLES_INDEPENDENT_20260804.md`
- `MATH_THEOREM_FOLDED_C8_NESTED_TERMINAL_INVARIANT_AND_POLARIZED_SOCKET_20260804.md`
- `MATH_THEOREM_DIAGONAL_INTERVAL_DIAMOND_SOURCE_FREE_DUAL_ROLE_ROUTER_20260803.md`
- `MATH_THEOREM_TERMINAL_COMMON_CAP_TWO_CROSS_RAY_RADO_GAMMOID_V2_20260803.md`
- `MATH_THEOREM_R_COMMON_CAP_GUARD_PRUNING_ROBUST_HALL_LIFT_20260731.md`
