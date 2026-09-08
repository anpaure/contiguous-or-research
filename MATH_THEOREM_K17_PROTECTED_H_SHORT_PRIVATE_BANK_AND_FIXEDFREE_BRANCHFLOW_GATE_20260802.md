# K17 protected H-short private bank and the exact fixed/free branch-flow gate

**Date:** 2026-08-02  
**Status:** the private H-short bank and its outer extension are independently
replayed.  The residual formulation below is an exact equivalence, not a
claim that the residual instance has already been solved.

## 1. Frozen protected bank

Start from the authenticated three-level K17 target table.  Its recoupled
form has

\[
 |F|=1748,\qquad |H|=18646,
\]

where `F` is the family of original singleton rows and `H` is both the real
bottom-token family and the family of eligible hard receivers.

The protected phase is bound to `original.res1972.tsv`, SHA-256
`db960ce5b51e0fdea7b048d35d48ca737096b16ee73a20df873beb0517e5f185`.
All residual ticket catalogues in this note must use that same owner/root
phase.  A fixed/free union census produced for an `s7` owner phase is a
different instance and cannot supply positive or negative rows here.

The independently replayed private bank selects a set

\[
 S_H\subset H,\qquad |S_H|=1748,                         \tag{1.1}
\]

and one exact phase-zero common-state ticket for every member of `S_H`.
Writing `P_H` and `Q_H` for the predecessor- and successor-host sets of
those tickets, the certificate has

\[
 |P_H|=|Q_H|=1748,qquad P_H\cap Q_H=\varnothing.         \tag{1.2}
\]

Thus all `3496` protected long endpoint hosts are distinct.  Their selected
bottom tokens are also distinct.  Exactly `3495` endpoints use a movable
hard bottom token and one uses a fixed soft-long endpoint.

The `3495` movable endpoint assignments extend to a complete outer bottom
matching with short set exactly `S_H`: every one of the `18646` real tokens
is used, all `1748` free receivers are filled, and exactly `16898` hard
receivers are filled.  In particular `S_H` is a basis of

\[
                 M_{\rm short}=(M/F)^*.                \tag{1.3}
\]

The frozen independent audit is

```text
scratch/k17_phase0_retained_witness_private_basis_20260802/
```

with the following load-bearing SHA-256 values:

```text
selected_tickets.tsv       d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1
complete_outer_matching    179270d1d01f6c14a7b47b5eb390e634aca33ac16e5ec82d54a93b589b8d850e
independent audit JSON     dfaa7a5682861945f2de680076e86ce70fac2be5f35b3fe9783916c3903eec92
independent verifier       16868a9a716933cc14b723ac3e94c07ec636bad9f8dd1b47332aee9eca7ccdd8
package manifest           80e1c40c74d4e3f14b738d22ef6c0a1f90926c765da30bde0669ecf2d29f25ba
```

The protected tickets are occurrence-labelled: each carries its short
address, predecessor and successor flags, endpoint hosts, and endpoint
bottom tokens.  This closes the variable H-short/socket-intersection row on
this phase-zero face.

This conclusion uses the full typed certificate, not merely abstract
membership in the `10,167`-element local nonzero bank `A`.  A set
`S subset A` can be an `M_short` basis while its individually legal tickets
collide on endpoint hosts or bottom tokens.  The protected object here is
`(S_H,tau,E_B;mu_B)`: the basis, one simultaneously composable
occurrence-labelled ticket per basis element, its `3495` forced movable
endpoint assignments `E_B`, and a complete outer matching `mu_B` witnessing
that these protected data extend.  Only `(S_H,tau,E_B)` and the fixed soft
endpoint are protected; the unforced residual edges of `mu_B` remain open.

### Corollary 1.1 (typed, not merely outer, H support)

Every residual outer completion which retains the `3495` forced placements
retains all `1748` selected H tickets literally.  Hence on this protected
face

\[
 Z_{\rm outer,H}=Z_{\rm typed,H}=0,
 \qquad \Omega_{\rm typed,H}\ge1748.                 \tag{1.4}
\]

In particular any remaining zero-role count is supported entirely on the
`5647` fixed/free roles.  This is strictly stronger than choosing a short
basis inside the aggregate nonempty-slot bank `A`: membership in `A` says
only that each H short has some local witness under some completion, while
(1.4) pins one mutually private witness for every selected H short in the
same outer completion.

Here `alpha` is the predecessor-long flag and `beta` is the
successor-long flag.  The retained catalogue uses the address-drift
orientation `beta<=alpha`.  The independent ticket replay has no
cross-side repeated host and has exactly one soft endpoint, so these flag
roles are literal rather than inferred from an undirected endpoint pair.
The separate canonical five-cell replay verifies that every selected ticket
is physical: `1365` use address `q7=inner12/outer123` and `383` use
`q8=inner23/outer123`.  Its flag-pair census is

\[
 (0,0)^{424},(1,0)^{498},(1,1)^{443},
 (2,2)^{150},(3,2)^{104},(3,3)^{129}.
\]

The physical verifier and audit have SHA-256 values
`7947c32afc8609cd4da7de9759f79cd3aaf1c15b8d629f407a66971add5d9287`
and
`1dd0d9d1c4e6a9690bc84bf00b0bd938403335c5ec659cde7a1acca814389b48`.

### Corollary 1.2 (exact protected-face Pareto start)

Materializing the exhibited outer extension gives table SHA-256
`b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc`.
Its independent relaxed-nine audit has SHA-256
`5c14e0834829ab3c27c83be817259d8bc9e2395ab1e9a94b84713d740d4cb29f`
and exact tuple

\[
 (P_0,Z_0,\Omega_0)=(16796,4708,3878),               \tag{1.5}
\]

where `P_0` has deficiency `102` and

\[
 Z_0=3187\ (\mathrm{fixed})+1521\ (F)+0\ (H).
\]

Thus the private bank closes the entire typed H-short zero layer in this
completion.  The live exact-one ticket layer still consists of all `5647`
fixed/free roles.  This tuple is a fixed-completion union/menu projection,
not a common-state cycle factor.

## 2. Exact residual outer matching

Do not freeze the arbitrary residual edges of the exhibited complete
matching.  Freeze only

1. the short set `S_H`;
2. the `3495` movable endpoint host-token assignments; and
3. the one fixed-soft endpoint.

There remain

\[
 18646-3495=15151                                      \tag{2.1}
\]

unused real bottom tokens.  The available receiver shore consists of all
`1748` free receivers and

\[
 16898-3495=13403
\]

unforced occupied hard receivers, again totalling `15151`.  Therefore the
residual outer row is an ordinary square containment matching.  The frozen
certificate proves this square graph has a perfect matching, but later
fixed/free socket choices may require a different one.

This distinction is load-bearing.  Pinning the whole exhibited completion
would create a fixed-table fibre; retaining the square matching variables
preserves every compound alternating cycle available around the protected
bank.

### Lemma 2.1 (complete residual cycle-circuit language)

The symmetric difference of any two residual outer completions extending
the protected bank is a disjoint union of alternating even cycles in the
`15151`-by-`15151` residual containment graph.  Flipping any one cycle
preserves the protected H short set, all protected endpoint placements, and
the exact target partition.  Conversely the union of these cycle flips
transforms one completion into the other.

#### Proof

Every residual token and every residual receiver is saturated in both
completions, so its symmetric-difference degree is zero or two.  Hence all
components are alternating cycles.  Alternating one component preserves
degree one and uses only legal containment edges.  Flipping all components
gives the second completion. \(\square\)

Thus the complete outer move language after protection is the ordinary
matching-fibre cycle language.  Fundamental `M_short` paths were needed to
choose the H bank; they are not needed to traverse its residual outer
fibre.

## 3. The 5,647 exact role DNFs

The remaining short roles are

\[
 \mathcal W_0=\mathcal W_{P2}\mathbin{\dot\cup}\mathcal W_F,
 \qquad |\mathcal W_{P2}|=3899,quad |\mathcal W_F|=1748. \tag{3.1}
\]

After contracting the protected short bank, the physical long-role set is

\[
 \mathcal L=(H\setminus S_H)\mathbin{\dot\cup}\mathcal L_{\rm soft},
 \qquad |\mathcal L|=16898+17=16915.               \tag{3.1a}
\]

For each `w in W_0`, let `G_w` be the complete phase-zero catalogue of
literal common-state tickets **on this protected materialization**.  Thus
both endpoint hosts lie in `L`; an original hard row in `S_H` may not
reappear as a long endpoint.  Equivalently, regenerate the catalogue after
contraction, or filter the original occurrence catalogue by the protected
short and fixed host--token rows.  A ticket `g` records

* the predecessor and successor long hosts;
* their bottom-placement modes;
* their common long flags;
* the short address; and
* for a free role, the real token placed at that free receiver.

Let `A_g(z,f)` be the conjunction of its required outer-matching literals
`z` and long-state literals `f`.  Then the exact support row is

\[
 \boxed{\qquad
   \bigvee_{g\in\mathcal G_w} A_g(z,f)=1
   \quad(w\in\mathcal W_0).\qquad}                  \tag{3.2}
\]

In a 0--1 master introduce `y_g` and impose

\[
 y_g\le \ell\quad(\ell\hbox{ a positive literal of }A_g),
 \qquad
 y_g\le1-\ell\quad(\ell\hbox{ a negative literal}),       \tag{3.3}
\]

together with

\[
                         \sum_{g\in\mathcal G_w}y_g=1.      \tag{3.4}
\]

Only the upper implications in (3.3) are needed for existential ticket
selection: (3.4) forces one genuinely active conjunction.  If all active
tickets rather than one selected ticket are to be counted, add the reverse
AND implication and the bidirectional role OR.

The endpoint rows are directed.  Every long host may be predecessor of at
most one short and successor of at most one short.  The protected bank has
already occupied the predecessor ports in `P_H` and successor ports in
`Q_H`.  A host may still use its opposite port, but every use must share its
single selected long flag.  Hence the residual exact rows are

\[
\begin{aligned}
 \sum_{g:\operatorname{pred}(g)=v}y_g
   &\le 1-\mathbf1_{v\in P_H},\\
 \sum_{g:\operatorname{succ}(g)=v}y_g
   &\le 1-\mathbf1_{v\in Q_H},                         \tag{3.5}\\
 y_g&\le f_{\operatorname{pred}(g),\alpha(g)},\qquad
 y_g\le f_{\operatorname{succ}(g),\beta(g)},\\
 f_{v,a_H(v)}&=1\qquad(v\in P_H\cup Q_H),\\
 \sum_a f_{v,a}&=1.
\end{aligned}
\]

Here `a_H(v)` is the predecessor flag of the unique protected ticket when
`v in P_H`, and the successor flag when `v in Q_H`.  It is well-defined
because the two protected endpoint shores are disjoint.  These units are
load-bearing: a protected host may use its opposite directed port later,
but that use must carry the already selected physical long flag.

Because the protected bank is cross-disjoint, its fixed flags never collide
with one another.  Any later collision is exposed literally by (3.5), not
hidden in a per-role degree score.

## 4. Residual long--long completion

After all `7395=1748+5647` short tickets have been chosen, precisely `7395`
long outgoing ports and `7395` long incoming ports are consumed.  The table
has `16915` long roles.  Consequently the residual directed long--long row
has the forced size

\[
                 16915-7395=9520.                    \tag{4.1}
\]

Let `L^+` and `L^-` be the unconsumed outgoing and incoming ports of the
contracted long-role set `L`, and
let `E_LL(z,f)` be the exact phase-zero compatible long--long transition
graph under the selected bottom modes and flags.  A residual degree
completion exists if and only if `E_LL(z,f)[L^+,L^-]` has a perfect
matching.  Equivalently,

\[
 \boxed{
 |N_{LL}(X)|\ge |X|\quad\text{for every }X\subseteq L^+.}  \tag{4.2}
\]

This is an ordinary Hall separator after the ticket and state literals have
been fixed.  With exact transition DNFs, (4.2) is also a proof-safe lazy
Benders family in the outer master.  The resulting directed object is a
cycle factor; connectedness is a separate subtour/merge row.

## 5. Projection-perfect row

Let `E_sup(z,f,y,e)` be the complete occurrence-labelled supplier graph
created by the protected tickets, selected fixed/free tickets, and selected
long--long edges.  It must saturate all `16898` active hard heads.  For a
head shore `X`, define `n_(X,u)` to be the bidirectional OR saying that
physical supplier identity `u` has at least one active edge into `X`.  The
exact row is

\[
 \boxed{
                 \sum_u n_{X,u}\ge |X|
                 \quad(X\subseteq H\setminus S_H).}          \tag{5.1}
\]

Maximum matching and alternating reachability separate (5.1).  Every
activation OR must be linked to the complete signed placement/state DNF in
both directions.  Counting occurrence records, or retaining a provider
after one of its placement literals disappears, is unsound.

## 6. Exact equivalence

### Theorem 6.1 (protected-H residual branch-flow equivalence)

Within the authenticated ordinary phase-zero mode catalogue, the protected
H bank extends to a target-exact one-state cycle factor with all short roles
supported and a perfect hard-head supplier projection if and only if there
exist variables satisfying:

1. the residual `15151`-by-`15151` outer containment matching;
2. the complete protected-contracted fixed/free ticket DNFs (3.2)--(3.4);
3. endpoint capacity, protected-flag units, and common-flag rows (3.5);
4. the `9520`-edge long--long perfect matching (4.2); and
5. the supplier Hall family (5.1).

#### Proof

Given a physical factor, read its residual bottom assignments, its ticket at
each fixed/free short, its unique long state, and its long--long edges.  The
five rows follow directly.

Conversely, the protected tickets give one predecessor and successor edge
at every H short.  Equations (3.2)--(3.5) do the same for every fixed/free
short without endpoint or state collisions; the contracted definition of
`G_w` prevents a protected short from being reused as a long host.  Equation
(4.2) fills every
remaining long in/out port exactly once.  Thus every physical role has
indegree and outdegree one and all selected transitions are literal
catalogue transitions.  The outer matching preserves the exact lower
target partition, while (5.1) gives the required supplier matching by
Hall's theorem.  This is precisely the claimed target-exact cycle factor.
\(\square\)

The equivalence does not turn the joint ticket layer into one polynomial
flow.  Before branching, (3.2)--(3.5) is exactly the typed three-partite
hypermatching of the R3 theorem.  After fixing the long-state branch and an
injective predecessor assignment, R3 reduces the successor choices to one
bipartite Hall flow; after all short tickets are fixed, (4.2) is the
separate residual long--long flow.  No total-unimodularity or polynomial
joint-rounding claim is made here.

## 7. Scope and next finite row

The private H-short bank removes the former `M_short`/socket intersection
from the open problem.  Fundamental `M_short` paths are no longer the main
move language after the bank is protected: residual bottom placements with
the same short set differ by alternating matching cycles, while ticket and
long--long choices live in the branch-flow rows above.

Still open are:

* completion of the full `5647`-role DNF catalogue, especially free-role
  payload dependence;
* solving the coupled residual rows (3.2)--(5.1);
* component merging/one chronology;
* phase one, residence, upper shadows, common-cap/compiler feasibility, and
  the final word.

The next proof-safe implementation should protect the selected ticket and
forced-edge files, enumerate the complete fixed/free DNFs, and alternate
literal branch-flow solves with long--long and supplier Hall separation.  A
fixed-table SAT call while any mandatory role has an empty current DNF is
strictly weaker and is not part of this reduction.

For a residual matching represented by independent alternating-cycle bits,
the exact activation and separation rows are Theorem 9.1 of
`MATH_THEOREM_K17_PARETO_BENDERS_SIGNED_SUPPLIER_HALL_AND_MSHORT_COMPONENT_PRICING_20260802.md`:
primitive availability is a bidirectional AND of cycle/flag literals,
fixed/free roles use literal DNF exact-one rows, residual long ports use the
availability-aware Hall cuts (9.7), and supplier records are activated only
through their selected parent ticket or direct edge before applying (9.10).
Those rows still produce a cycle factor, not one common cycle.
