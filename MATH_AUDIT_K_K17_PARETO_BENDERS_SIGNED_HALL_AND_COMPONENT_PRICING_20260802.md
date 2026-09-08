# Independent proof audit: K17 signed-Hall Pareto Benders and component pricing

**Date:** 2026-08-02  
**Audited theorem:**
`MATH_THEOREM_K17_PARETO_BENDERS_SIGNED_SUPPLIER_HALL_AND_MSHORT_COMPONENT_PRICING_20260802.md`

## Verdict

**PASS for the stated outer/Benders scope.**  The theorem gives an exact
supplier-Hall separator and an exact matching-component/fundamental-circuit
candidate language.  The phase-zero component-603 Pareto candidate and the
protected private H-short bank are independently frozen.  Neither object by
itself is a common-state cycle cover.

## 1. Matching-component audit

For two outer matchings, every real token and every free host is saturated
twice, so its symmetric-difference degree is zero or two.  Only hard hosts
can have degree one.  Hence all open components are alternating paths with
hard endpoints; all other components are alternating even cycles.

Flipping one component preserves all real-token and free-host degree-one
rows and hard-host capacity.  A path exchanges exactly one occupied and one
unoccupied hard host, so its short sets differ by one basis exchange in
`M_short`.  A cycle changes no hard-host occupancy and is correctly called
a same-basis fibre circuit.  No sequential-relay provenance follows.

The theorem correctly warns that supplier/socket records may couple rows
from different matching components, so objective deltas are not additive
without an extra disjoint-support proof.

## 2. Hall algebra audit

For fixed phase `p` and `Q subseteq H`, the demanded heads are `Q-S`, so
their count is

\[
                         \sum_{v\in Q}(1-s_v).
\]

The bidirectional OR `n^p_(Q,u)` counts supplier identity `u` once.
Therefore

\[
 \sum_{v\in Q}(1-s_v)-\sum_u n^p_{Q,u}\le0
\]

is literally Hall's inequality.  At an incumbent `*`, its left side is
`d_(p,Q)^*`.  Subtraction gives

\[
 \sum_{v\in Q}(s_v-s_v^*)+
 \sum_u(n^p_{Q,u}-n_{Q,u}^{p,*})\ge d_{p,Q}^*.
\]

All four signs are correct.  In particular a lost last supplier has charge
`-1`; counting records instead of distinct supplier identities would be
unsound.  A candidate can expose a new deficient shore, so fresh
matching/min-cut separation remains necessary.

The activation equivalences are also correctly scoped.  A supplier record
must be an exact conjunction of selected payload modes, and both directions
of every record/edge/neighborhood OR are required.  An ordinary phase-0
catalogue cannot certify generalized relay-created modes.

## 3. Fundamental-circuit audit

Deleting the matched real edge at a currently occupied hard host `e` exposes
one real token.  Alternating reachability to a currently short host `f`
gives exactly the primal rematching whose dual short basis is `S-f+e`.
Thus the reachable endpoints are
`C_(M_short)(e,S)-e`.

The theorem correctly does not assign one modular price to this endpoint
exchange: different alternating paths can move different internal bottoms,
and distinct-neighbor Hall plus socket counts are nonlinear.  Literal replay
of the chosen path/packet is load-bearing.

## 4. All-role catalogue objective audit

With exact phase-`p` ticket activations `b_g^p`, the OR `c_w^p` is one
exactly when short role `w` has at least one ticket.  Splitting the short
roles into fixed `3899`, free `1748`, and hard-dummy `1748` gives

\[
 Z_p=\sum_{w\in W_{\rm fixed}}(1-c_w^p)
     +\sum_{F\in W_F}(1-c_F^p)
     +\sum_{v\in H}(s_v-c_v^p),
 \qquad \Omega_p=\sum_gb_g^p.
\]

The split is exact.  A free role is always short, but its selected `x_(u,F)`
fixes its lower payload and must occur in every ticket DNF.  Fixed roles
depend on the real placement edges at their predecessor/successor endpoint
modes.  Therefore H-only dummy pricing sees only the last summand and cannot
be an exact objective for the dominant `5,647` fixed/free roles.

These remain catalogue metrics; neither chooses one compatible ticket per
short nor enforces the address/degree cycle cover.  The signed zero-budget
cut and ticket-count cut in (5.4)--(5.5) follow by direct subtraction, with
all first-ticket gains and last-ticket losses retained.

## 5. Bound inputs and finite calibration

The independently replayed projection-perfect endpoint is bound by

```text
round-47 table
95dee6e9718f9067d4bd5c860f7763a45ee03785bdbb13b20b8d95540a7a2735

independent projection audit
2b79c35507d07be6c1fbb1503ceff0701ebf11184230b030bc3bfec8f761361a
```

The independently reproduced weighted materialized table is

```text
3886de626d55d4393d3f71f51fa9799488608f26eb977a8ff60e7be39cfac7cd
```

Its static admissible-bank Hall reproduction has audit SHA

```text
d8d7f5aa451d6ac8c3fb6b08b2cb06f3bf5b8ca8fe7ce7031ccc985998a5d92f
```

and exact bank sizes/slacks

```text
A=10167, Z=8479, Hall slacks=(0,0).
```

The full two-phase autopsy supersedes the earlier H-only tuple.  Its zero
splits `(fixed,free,hard)` are

```text
phase0  3170 / 1535 / 788
phase1  3193 / 1542 / 762
```

and its supplier defects are `121/131`.  These values explain why hard-slot
pricing alone was pointed at the wrong score.  They are calibration only
until the full autopsy hashes are frozen.

The phase-0 component product has produced candidate `603` with independently
replayed

```text
supplier matching 16898, zeros 5967, tickets 2207.
```

The load-bearing hashes are

```text
component table       54b8063b4f39afb8ffccabadb88f04b65edaa0a4321c343f84f15918d75f24f4
full audit            4ac8f356e7c4b6eb48b10f90210678981b097ba7db67756e8074d106c212dadb
coordinate-DP audit   cb8364c67dd8f486aadd2986231f579cb758fe02e2ffc7de522ab3293606c57b
flip ledger           ea6ef70c52a7f077d4443d5b406d23febf752784c5d2b590d5f28f0029f8426b
```

The separate clean-room audit note has SHA-256
`14b1c3410a83fac781261ef01a6cbaf9d2579cfc4457e4e46f000f86bebbb4e4`;
its package manifest has SHA-256
`b9d1139767ea86c0c4a52e6602afa47128c768eac2298cefd386587171d1ae03`.

No phase-1 inference is permitted.

Finally, the protected H-short bank is independently frozen:

```text
bank theorem audit
dfaa7a5682861945f2de680076e86ce70fac2be5f35b3fe9783916c3903eec92

selected 1748 tickets
d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1

complete outer matching
179270d1d01f6c14a7b47b5eb390e634aca33ac16e5ec82d54a93b589b8d850e
```

It proves `3496` cross-disjoint endpoint hosts, `3495` forced dynamic token
edges plus one fixed-soft endpoint, and an outer extension.  It is a
sufficient retained-witness bank, not a complete global ticket theorem.

Materializing that outer extension gives the independently replayed
protected-face Pareto start

```text
table SHA              b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
full audit SHA         5c14e0834829ab3c27c83be817259d8bc9e2395ab1e9a94b84713d740d4cb29f
supplier               16796/16898 (deficiency 102)
socket triples         3878
zero split             fixed 3187 / F 1521 / H 0
```

All `1748` protected H tickets are present.  This is one fixed residual
completion and its supplier score is the union/menu projection, not a
selected common-state factor.  It is nevertheless the correct starting
tuple for the protected-face Benders search: the H layer is closed, while
all `5647` fixed/free roles remain in the exact-one DNF master.

## 6. Exact remaining finite task

The exact reduced master may protect
the whole H-short bank and solve:

1. one exact ticket for each of the `3899+1748=5647` fixed/free roles;
2. residual long-flag/direct-arc degrees on all `16915` long roles;
3. hard exact supplier matching `16898/16898` by fresh signed Hall
   separation.

The protected tickets consume `1748` incoming and outgoing stubs.  Together
with the residual `5647` sockets, the exact degree sum leaves `9520` direct
long--long arcs.  Cross-disjointness makes the protected stub indicators
binary and conflict-free.  The theorem's equations (8.2)--(8.4) are then
necessary and sufficient for a relaxed-nine phase-0 **cycle cover** in the
declared protected face.  They do not force one common cycle.

Failure of that residual master is a scoped no-go only.  No fixed-table SAT
call or atomic-relay assumption belongs in this audit.

## 7. Typed-bank and cycle-fibre audit

The theorem now makes a load-bearing distinction which the ordinary
nonzero-bank Hall test does not provide.  A set `S subset A_0` can be both
locally nonzero and an `M_short` basis while its occurrence tickets compete
for the same endpoint host or bottom token.  The frozen bank instead gives
typed protected data `(B,tau,E_B;mu_B)`: one literal ticket per short,
cross-disjoint endpoint hosts, and the `3,495` injective forced endpoint
edges `E_B`.  The complete matching `mu_B` proves that these data extend; its
unforced residual edges are not protected.  The reduced master is valid only
after `(B,tau,E_B)` is protected, not merely the abstract basis `B`.

The residual catalogue must be generated on the contracted long set
`(H-S_H) dotcup L_soft`; otherwise a protected short can be illegally reused
as a long endpoint.  Likewise every protected endpoint fixes its literal
long flag even on the opposite directed port.  The contraction filter and
flag units (8.2a) are therefore necessary, not implementation details.  The
remaining fixed/free ticket layer is a typed three-partite hypermatching;
only after branching on flags and predecessor choices does it reduce to a
bipartite successor flow.

For a declared family of vertex-disjoint alternating cycles of the residual
outer matching, each primitive availability is exactly an AND of cycle and
flag literals.  Hence (9.1)--(9.3) are exact role-activation rows.  After
selected tickets consume ports, (9.4)--(9.5) construct exactly the remaining
long--long eligibility graph.  For every fixed long-role shore `X`,

\[
 \sum_{h\in X}o_h\le\sum_k n_{X,k}
\]

is Hall on `X` intersected with the currently unused outgoing shore.  The
appearance of both endpoint-availability bits in `eta_c` is necessary; it
prevents an already consumed port from being counted as a neighbour.

Equation (9.6) retains the selected direct edges because the supplier row
depends on which perfect matching is chosen.  Thus (9.7) may be used as the
exact projection separator for long--long feasibility, but one may not solve
that Hall system independently and then count supplier edges from all
eligible transitions.  Equations (9.8)--(9.10) correctly activate only
supplier occurrences whose parent ticket or direct edge is actually
selected.  They are ordinary Hall on the fixed active-head shore
`H-S_H`.  The supplier universe must contain one clone for every possible
owning outgoing primitive and compatible head state; otherwise the
selected-parent equivalence can silently omit a newly materialized edge.

The protected baseline's alternating shore has `109` heads and `7`
union/menu supplier identities.  Because the short set is fixed, its first
selected-state cut is exactly `sum_u n_(Q*,u)>=109`; subtracting the seven
baseline activations gives net gain at least `102`, with no short-head
charge.  The head-file SHA is
`5b0afdc17d4be1e05bc51f459e8c2fe299959dbfdc279f13a409557ba0712255`.
This cut is valid even though the baseline is not itself a selected-state
cycle factor: its absolute form is ordinary Hall on a fixed physical shore.
The analogous residual-role aggregate has `939` baseline-supported roles,
so full support requires net first-ticket gain at least `4708`; the
individual DNFs remain stronger and prevent a large-degree role from
substituting for an unsupported one.

Therefore Theorem 9.1 is an exact phase-zero **cycle-factor** formulation in
the declared residual cycle fibre.  It is not global over all residual
matchings and contains no subtour, phase-one, residence, upper-shadow,
physical-replay, common-cap, compiler, or word conclusion.

## 8. Correlated rank-seven C6-column audit

### 8.1 Literal positive column

The three-row move

```text
rows 16269,16267,16271
old  81416-81417 ; 73216-81409-81413 ; 81408-81412-81420
new  81409-81417 ; 73216-81412-81413 ; 81408-81416-81420
```

was replayed from the raw inputs by two independent C++ programs.  The first
checks the complete named target deck, row roots/owners and length histogram,
all `1748` private tickets, all `18646` protected outer edges, and one exact
new-P2 socket in each owner phase.  The witnesses are

```text
phase 0  (q,a,b)=(8,2,2), modes 70822,1584370
phase 1  (q,a,b)=(7,0,0), modes 86138,414573
```

and neither witness uses one of the two changed `H` destinations.  The
second program changes the three rows in the raw round-47 supplier table and
replays the selected perfect matching.  It remains `16898/16898`; the three
affected selected masks change as

```text
16269->15428  1073741892 -> 68
19298->16271   536870963 -> 1073741892
22299->16267   268435506 -> 68.
```

The load-bearing hashes are

```text
structural replay source  f00230aca24fc80e11cdeb8ecbe1f893eed037444079737c8076d93fa10dbea1
structural replay output  fc65985e3a8f29fa62c2d1787cbff0ca41ffbb31a1d7d1998e0181c04ea59f32
preservation source       82e1c98f67fba9bc041fca45e61a36dc2df076e5094b72d8f9f2c8f46df081c1
preservation output       698e9865bae2cde1c663d62dcee78e3759ccd2f8e54a1dab174ce556817d7829
```

This proves one protected-bank-compatible local column.  It does not prove
that its socket witness, private ticket bank, and raw supplier matching are
one common selected-state factor.

### 8.2 Complete fixed-table row-shadow census

The unique-closure reconstruction in Lemma 10.1 was independently rerun.
It reproduced byte-for-byte:

```text
rank-seven union-zero roles        623
raw structural columns             364, covering 290 roles
bottom-legal columns                180, covering 168 roles
protected-row-clean columns         118, covering 116 roles
maximum raw columns per role          3
row conflicts among clean columns      2
maximum row-disjoint clean packing    116
```

The hashes are

```text
audit source       7da1f9ab6e6b0013eac30fde0370bcb36361ed9b95effe2faadcc199209dd979
candidate table    cb93bfc7b785eff4e9d6d01bc6ec6f46e3e2025879b3b1abeff85ba9757fefe0
audit JSON         77d3ada0ea96b95044830c216d62e4826a16c027212563773cf048975d608e48
packing source     1e72385a99d7063b9f27111d1fdd77b639a2f2ac47159ad7a2f5f0aca0cc3752
packing selection  f3b1251a5b592a165dc08eef8c87623660146186fb64ec4b05166985249fbb5d
packing audit      df546cdb2c6a6a70a47aa2dd1482460afa332b037fc7c5fb08d097d0d2fe2216
```

The `118/116` row-clean layer is only a necessary prefilter.  It does not
replay forced outer edges, phase sockets, selected-state supplier, or
inter-column conflicts.  Conversely the census is tied to the fixed table;
it cannot rule out columns created after an earlier C6.  Thus the correct
conclusion is a one-shot coverage obstruction, not a serial-C6 no-go.

An independent fixed-root SCC audit also reproduces

```text
rank-seven slots             19448
nonidentity containment arcs 136136
SCCs / largest SCC           421 / 18953
old bad roles movable/stuck  461 / 162
```

under the generous relaxation which deletes every lower-bottom constraint.
The independently implemented source, complete slot table, and JSON hashes
are

```text
source  14cd04785aefcc1dd524f272b11c861d8a942c2717cc58e3595b62e1bfe6fcd2
table   879b76e36129c3437cb90bf5ce9f794f2cf9c79732019bc6246a8e9109238980
JSON    65904e7e33fe1f6df3004077fea1800ac2f9ec05aee1253467b99cf2c2608b85
```

A singleton SCC forbids moving that rank-seven target while the receiver
root bank is fixed.  It does not freeze the role's socket DNF: rethreading a
different H middle can create a new endpoint mode incident to the unchanged
role.  Hence this is an exact no-go for “one target-moving circuit per bad
role,” not for every fixed-root socket-repair strategy.  Any broader no-go
requires an additional DNF-locality/invariance lemma which is not known.

### 8.3 Why the master must regenerate every nonlinear row

For pairwise row/resource-disjoint columns, the row-state equations (10.8)
give one literal final table.  Containment is then a Boolean function of the
selected row states, giving (10.9).  Ticket, direct, and supplier records
also depend on the selected row states and must be cloned as in (10.10).
After that regeneration, the exact-one ticket, degree, and Hall proofs from
Sections 8--9 remain valid.

It is unsound to attach a scalar benefit to each C6 and retain the old
catalogue: a changed `H` middle simultaneously changes outer containment,
fixed/free role DNFs, direct port eligibility, and supplier masks.  It is
also unsound to add overlapping C6 deltas.  Theorem 10.2 is exact only on
the declared row/resource-disjoint face; an overlapping packet must be one
larger simultaneous table-state column.

### 8.4 Exact separation from the 693-exchange route

An independent literal comparison of the abstract outer-zero route endpoint
with this private bank gives

```text
private hard-short rows          1748
route hard-short rows            1748
intersection                      311
private-only / route-only        1437 / 1437
forced dynamic placements        3495
retained / violated               557 / 2938
```

Its source and frozen output have hashes

```text
comparison source  85287bab6574cf34bdfe23c5a427073a05ee3c5072fbb93cf3e30e855c1bd067
comparison output  16eed67939d8df11b363dd6c68d9dfd7136e5f95a89621c64b097b1437fe42ce
```

Therefore that exact 693-exchange endpoint is not a simultaneous endpoint
for this exact protected bank.  The conclusion is strictly scoped: it does
not reject another exchange route, another private bank, or a joint route
whose outer and role-moving columns are selected together.

## 9. Global chain/root branch-flow audit

The undecorated rows (11.1) are exactly the node-edge incidence rows of one
bipartite graph with shores `L_out dotcup M_out` and
`M_in dotcup R_in`; equality/capacity changes do not alter total
unimodularity.  The marginal short-positivity row is genuinely outside that
proof.  On rows `(E_m,A_l,C_r)` and columns
`(y_lm,y_lr,x_mr)` its coefficient matrix is

\[
 \begin{pmatrix}1&0&1\\1&1&0\\0&1&1\end{pmatrix},
\]

whose determinant is `2`.  Multiplying the inequality row by `-1` changes
only its sign, so no standard-form convention removes the obstruction.

The two conditional reductions are exact:

1. for fixed `x`, the right shore available to `y` is
   `V_x=M dotcup R_x`, not all of `M dotcup R`; every unused root and every
   middle whose selected root edge is nonpositive is mandatory.  Adding
   `|V_x|-|L|` dummy left vertices complete to the optional right shore
   converts simultaneous real-left/mandatory-right saturation to one
   ordinary perfect matching.  At K17, `|V_x|=24310`, `|L|=21777`, so the
   number of dummies is exactly `2533`;
2. for fixed `y`, a compatible completion requires its unused-root shore to
   have the same cardinality as `M`; this cardinality check is included in
   the perfect-matching condition.  The short middles are exactly those
   without a lower predecessor.  Restricting only those middle rows to
   positive root edges gives one ordinary perfect matching.  Equivalently
   the number of selected lower-to-middle edges must be `16915`.

Thus alternating exact Hall separation is valid, while joint TU is not.
This statement concerns marginal constants `p_mr`.  In the selected-state
master each constant is replaced by the OR of complete occurrence-labelled
DNFs on the final table, outer matching, flags, and addresses, but that OR is
only availability.  A ticket-selection bit is tied simultaneously to the
shortness of `m`, the selected `x_mr`, and an active DNF, with exactly one
ticket per short middle.  Those selected bits carry all shared endpoint/
resource and selected-parent supplier rows.  Therefore the marginal fixed-x/
fixed-y Hall flows remain exact projections, while the selected-state master
retains the ticket hypermatching whenever menus share resources.  The private
bank may be pinned only while its exhibited short/root rows, `1748` tickets,
`3495` forced dynamic placements, and fixed soft endpoint remain literal.

There is currently no complete post-role-move catalogue for the `5647`
fixed/free DNFs.  Consequently Section 11 is an exact branch-flow reduction,
not a finite PASS or UNSAT result.  The known protected baseline starts at
supplier `16796/16898`, selected-state Hall shore `109->7`, and fixed/free
zeros `4708`; none of these is repaired merely by the marginal b-matching.

### 9.1 Two-matroid static closure and literal fixture

The stronger common-basis formulation was checked independently.  On ground
`E=M dotcup R`, let `M_L` be the low-target transversal matroid and
`N=M_7^* direct-sum U_(16915,M)`.  A common basis has exactly `16915`
middle receivers and `4862` direct roots; complementing the latter in `R`
gives an `M_7` basis.  The two matching witnesses therefore give exactly the
three-level table, and the converse reads the same common basis from any
table.  Both matroids have rank `21777`, so ordinary weighted matroid
intersection closes the undecorated static allocation.

Only receiver-element weights are covered by this reduction.  Witness-edge,
socket, and occurrence-state costs are not ground-set weights.  The fixed-y
oracle must also require `|R-C_R|=|M|` and a perfect matching on both shores;
an `M`-saturating matching alone would leave root degrees open.  These scope
corrections are incorporated in the current theorem.

The literal protected baseline fixture was rebuilt independently and
reproduced byte-for-byte:

```text
L/M/R                    21777 / 19448 / 24310
C_M/C_R                  16915 / 4862
M7 complement basis      19448
chain histogram          0 / 7395 / 16915
```

The independent source and JSON hashes are

```text
60911fa22a41d33a8eda3975ab51e36e6fc071eb10fd692c38831763700f4bfe
cb2f3403d054a7110b58c41c5daa487836bcf10291d8dec54952a15c4d064cc4
```

The corrected theorem is
`MATH_THEOREM_K17_THREE_LEVEL_COMMON_BASIS_AND_SOCKET_NON_TU_BRANCH_FLOW_20260802.md`.
It closes static allocation only; the complete `5647`-role regenerated DNF
catalogue remains absent.
