# Independent audit: order-free two-corridor contraction and LKK scope

**Date:** 2026-08-02  
**Audited root theorem:**
`MATH_THEOREM_ROOT_ORDER_FREE_TWO_CORRIDOR_HAMILTON_CONTRACTION_20260802.md`
at SHA `7231f74bf433c75d81e117d21861e9763862ccba62ca3ee6accbd6c13c6ea9e6`  
**Verdict:** PASS.  The residual LKK branches do not imply the resulting
partition-Hamilton row.

## 1. Contraction replay

The protected composite path has literal order

\[
 A_b\to F\xrightarrow{P_3}E\to D_c.
\]

Deleting it from a valid cycle leaves an incoming role at `A_b` and an
outgoing role at `D_c`; hence directional contraction correctly retains arcs
entering `A_b` and leaving `D_c`.  The same check for
`C_bc->B_bc` retains arcs entering `C_bc` and leaving `B_bc`.

Deleting both marked arcs from one cycle creates roots `D_c,B_bc` and sinks
`C_bc,A_b`.  The only pairing compatible with one original cycle is

\[
 D_c\leadsto C_{bc},
 \qquad B_{bc}\leadsto A_b.
\]

The crossed pairing would restore two cycles.  Conversely the displayed
pair concatenates with the marked arcs to one cycle.  Thus both directions
of the root reduction are exact.

The corrected state-fibre scope is load-bearing and sound: internal `P_3`
fragments are removed, `g_2` carries their cumulative ledger, exactly one
state is selected per remaining physical-fragment fibre, and every shared
capacity is global.  An ordinary Hamilton cycle through all state copies
would not be equivalent.

## 2. Exact partition subtour check

For state variables `y_v` and arc variables `x_e`, exact-one fibre selection
and

\[
 x(\delta^+(v))=x(\delta^-(v))=y_v
\]

give a directed cycle cover on exactly one state per physical fibre.  If
`V_J` is the union of the state fibres in a nonempty proper physical set
`J`, one cycle component is isolated exactly when its physical fibre set has

\[
                         x(\delta^+(V_J))=0.
\]

Therefore the full family

\[
                         x(\delta^+(V_J))\ge1
\]

is necessary and sufficient for one partition-Hamilton cycle.  This also
checks the equivalent internal-arc inequality
`x(A[V_J])<=|J|-1`.

## 3. LKK nonimplication

The two LKK branches in the residual Ore proof constrain only the projected
rank-`(m-1)`/rank-`m` capacity-two incidence table.  They are unchanged if
literal fragment histories partition a valid projected two-factor into
closed state classes.  Put both marked arcs in one class and take the
physical fibres of another as `J`; then the complete state union `V_J` has
no accepted incoming or outgoing join, while all projected Ore/LKK rows are
unchanged.

Thus LKK does not imply even static strong connectivity of the contracted
state graph, much less partition-Hamiltonicity.  The exact first obstruction
is a nonempty proper fibre set whose state union is forced closed in the
global partition-assignment face.  Absence of one such cut is not sufficient:
subtour rows may conflict, so the full partition master or a genuinely
state-preserving robust-expansion/merger theorem is still required.

## 4. Scope

The fixed-order tight suffixes are not a global no-go: a successful cycle
chooses its own two orders.  The audit proves only that the owner/lower LKK
margin cannot supply the missing order-free topology.  Integer charge,
histories/capacities, deeper upper shadows, residence beyond the encoded
state and compiler feasibility remain separate global rows.
