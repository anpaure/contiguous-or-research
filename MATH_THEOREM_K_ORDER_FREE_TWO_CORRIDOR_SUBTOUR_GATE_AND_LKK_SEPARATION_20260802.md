# Order-free two-corridor topology: the partition-subtour gate and why residual LKK does not imply it

**Date:** 2026-08-02  
**Lane:** K, prospective direct-new-phase topology  
**Status:** exact audit of the protected-arc contraction, exact
partition-assignment/subtour formulation, and a sharp projection obstruction.
The residual owner/lower Ore theorem does not imply partition-Hamiltonicity
of the accepted history-state graph.

## 0. Verdict

The corrected contraction in
`MATH_THEOREM_ROOT_ORDER_FREE_TWO_CORRIDOR_HAMILTON_CONTRACTION_20260802.md`
is exact.  Contracting

\[
 A_b\longrightarrow F\xrightarrow{P_3}E\longrightarrow D_c
\]

and the fixed arc `C_bc -> B_bc` turns the two residual corridors into one
**partition-Hamilton** problem.  Every internal physical fragment of `P_3`
is removed, the marked `g_2` state carries its complete cumulative ledger,
and exactly one state must be selected from every remaining physical-fragment
fibre.  Shared capacities are global.

This order-free target avoids the artificial tight suffix shores of one
frozen forward order.  It does **not** follow from the two
Lovasz--Kruskal--Katona branches used to close residual Ore--Ryser.  Those
branches concern capacity-two incidence after histories and state fibres have
been projected away.  A history refinement can preserve every projected
owner/lower row while producing a nonempty endpoint-free closed fibre class.

The first exact new row is the fibre-subtour family

\[
       x(\delta^+(V_J))\ge1
       \qquad(\varnothing\ne J\subsetneq {\cal P}),    \tag{0.1}
\]

where `cal P` is the physical-fragment set and `V_J` is the union of the
state fibres indexed by `J`.  Together with exact-one state selection and
one-in/one-out assignment, (0.1) is necessary and sufficient for one
partition-Hamilton cycle.  It is absent from the residual Ore theorem.

## 1. Audit of the protected-arc contraction

Let

\[
 g_2:A_b\to D_c
\]

denote the directional contraction of the fixed composite pump path, and let

\[
 g_1:C_{bc}\to B_{bc}
\]

be the other prescribed new-phase arc.  Their four endpoints are distinct
and avoid the interior of `P_3`.

### Theorem 1.1 (partition contraction is exact)

A literal chronology selects exactly one state of every physical residual
fragment and contains `g_1,g_2` in one cycle if and only if deleting those
arcs gives

\[
 D_c\leadsto C_{bc},
 \qquad B_{bc}\leadsto A_b.                            \tag{1.1}
\]

For a forced arc `u->v`, directional contraction retains only joins entering
`u` and joins leaving `v`.  The marked replacement fibre carries both
endpoint ledgers and the arc contribution exactly once.  For `g_2`, it also
carries every internal fragment/resource/history/charge contribution of
`P_3`, whose internal fragment fibres are deleted.

#### Proof

Using the selected state of each physical fragment, concatenate

\[
 A_b\xrightarrow{g_2}D_c\leadsto C_{bc}
 \xrightarrow{g_1}B_{bc}\leadsto A_b.
\]

Conversely, deleting the two arcs from a partition-Hamilton cycle creates
roots `D_c,B_bc` and sinks `C_bc,A_b`.  A crossed pairing would close a
proper cycle containing one protected arc before the other, so (1.1) is
forced.  At `u->v`, the selected arc has consumed the outgoing role of `u`
and incoming role of `v`; only the incoming role of `u` and outgoing role of
`v` remain.  Expansion is therefore unique.  \(\square\)

An untyped owner contraction, retaining the internal `P_3` fragments, or
filtering a shared capacity independently at each state copy would invalidate
the converse.

## 2. Exact order-free partition formulation

Let `D=(V,A)` be the contracted accepted directed multigraph.  Let

\[
               {\cal P}=\{P_1,\ldots,P_M\}
\]

be its physical-fragment fibres, with admissible state set `V(P)`.  The two
marked contractions are their fixed replacement fibres.  Parallel literal
arcs remain distinct.  Use `y_v in {0,1}` for state vertices and
`x_e in {0,1}` for arcs.

### Theorem 2.1 (partition assignment plus fibre subtours)

`D` has a directed partition-Hamilton cycle if and only if

\[
\begin{aligned}
 \sum_{v\in V(P)}y_v&=1 &&(P\in{\cal P}),\\
 x(\delta^+(v))&=y_v &&(v\in V),\\
 x(\delta^-(v))&=y_v &&(v\in V),                      \tag{2.1}\\
 x(\delta^+(V_J))&\ge1
       &&(\varnothing\ne J\subsetneq{\cal P}).       \tag{2.2}
\end{aligned}
\]

The marked states have `y=1`.  Every occurrence, palette, history,
upper-ticket or common-cap row must be imposed on these same global
variables.  For a solution of (2.1), outgoing and incoming cut values agree,
and for `|J|=j`, (2.2) is equivalent to

\[
                         x(A[V_J])\le j-1.             \tag{2.3}
\]

#### Proof

Equations (2.1) select one state from every physical fibre and make the
selected arcs a disjoint directed cycle cover on the `M` selected states.
Summing selected outdegree minus indegree over `V_J` equates its outgoing and
incoming cuts.  A proper selected cycle component visits a proper nonempty
fibre set `J` and has no selected arc leaving `V_J`; conversely any
multi-cycle cover has such a component.  Hence (2.2) is equivalent to one
cycle.  Exactly `j` selected states lie in `V_J`, yielding (2.3).
\(\square\)

This is the exact order-free replacement for guessing two total orders.
After finding the cycle, deleting the marked arcs supplies those two orders.
An ordinary Hamilton cycle visiting every admissible state copy is the wrong
object, and one partition assignment without (2.2) proves only a cycle cover.

## 3. What the residual LKK proof controls

The residual Ore theorem acts in the rank-`(m-1)`/rank-`m` containment graph.
For a lower shore `S` it controls

\[
 \sum_Y\min\{2,d(Y,S)\}-2|S|.                         \tag{3.1}
\]

Its opposite LKK branches occur only after a hypothetical capacity failure
has been localized to one polynomial-size full shore.  They prove that the
owner/lower `b`-factor polytope is nonempty.  They do not imply

* a lower bound on `|N_D^+(V_J)|` after state filtering;
* a selected arc crossing every fibre shore;
* strong connectivity after the two marked contractions; or
* absence of a proper cycle component.

Even before history filtering, the unconditional Tanner estimate used by the
Ore proof is only

\[
 |N(S)|-|S|\ge {2m-1\over2m^2}
                   \min\{|S|,N-|S|\},                 \tag{3.2}
\]

which is relative expansion `1+Theta(1/m)` on middle shores, not the
factor-two neighbourhood expansion used by elementary sparse Hamilton
rotation arguments.  More decisively, the projection producing (3.1)--(3.2)
forgets the state fibres and their global shared-capacity coupling.

## 4. Sharp projection obstruction

### Proposition 4.1 (endpoint-free closed fibre class)

All residual Ore/LKK inequalities may hold while even the first contracted
partition cut (2.2) fails.

#### Proof

Take an owner/lower-exact residual two-factor supplied by Ore with at least
two directed components.  Give every physical fragment an admissible state
labelled by its component and accept joins only when they preserve that
label.  Extra alternative state copies may be added, provided they preserve
the same physical-component partition.  The owner/facet incidence projection,
degrees, codegrees, protected demands and both LKK calculations are unchanged.

Put both marked arcs in one component and let `J` be the physical-fragment
set of a different component.  Then

\[
 J\ne\varnothing,
 \qquad J\ne{\cal P},
 \qquad \delta_D^+(V_J)=\delta_D^-(V_J)=\varnothing. \tag{4.1}
\]

Every exact-one state assignment closes a cycle inside `J`, violating
(2.2).  No partition-Hamilton cycle through the marked states exists.
\(\square\)

This is a separation theorem, not a claim that the intended Boolean history
table realizes the worst case.  It proves that projected LKK inequalities
alone contain no information capable of excluding it.

### Corollary 4.2 (minimal static and assignment-face cuts)

A nonempty proper fibre set `J` with no accepted outgoing arc from its full
state union `V_J` is a complete static no-go.  More generally, if every
solution of the global partition assignment/capacity face satisfies

\[
                         x(\delta^+(V_J))=0,           \tag{4.2}
\]

then `J` is a complete subtour obstruction even when raw crossing arcs exist.
This is the state-expanded analogue of a DM shore.  It must be computed in
the literal global face; absence of one forced-closed shore is not by itself
a Hamilton theorem because several subtour rows can conflict.

## 5. Consequence for the live construction

The fixed-order tight suffix is not an invariant no-go: a successful
partition-Hamilton cycle supplies its own two orders.  The opposite LKK
branches nevertheless do not bypass it.  A proof must add one genuinely
directed ingredient to the now-closed residual factor row:

1. solve (2.1)--(2.2) with the global history/capacity states;
2. prove Boolean-specific robust directed expansion which survives the
   one-state-per-fibre selection and the `O(d)` protected bank; or
3. construct a partition cycle cover plus marked-state-preserving alternating
   mergers for every proper component.

The weakest exact exported topology state is the contracted marked partition
assignment face together with its live fibre-subtour shores.  Integer charge,
deeper uppers, residence beyond the encoded histories and terminal compiler
feasibility remain separate.
