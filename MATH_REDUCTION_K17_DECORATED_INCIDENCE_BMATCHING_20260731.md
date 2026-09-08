# K17 decorated residual factor: exact incidence reduction

Date: 2026-07-31.  Scope: the fixed tripleflow core
`scratch/k17_pbbs_u_yaux_tripleflow_bridge_20260731.fragments`, SHA-256
`0f6267a487916ff2ee2aa04b3656d4a2b24aa7a72a057e87c39b381cfddfa25d`.

This note concerns only the carrier residual-factor search.  It does **not**
claim staircase, opening, envelope, compiler, or universal-word feasibility.

## 1. Exact b-matching normal form

Let `c` be a residual rank-eight colour, and let `O(c)` be its rank-nine
supersets having positive residual owner demand.  The direct-pair model chooses
one unordered pair `{a,b} subset O(c)`.  Introduce instead an incidence bit

```
y[c,a] = 1 iff owner a is an endpoint of c's chosen edge.
```

Then the complete lower master is exactly

```
sum(a in O(c)) y[c,a] = 2                         for every colour c,
sum(c subset a) y[c,a] = residual_degree(a)       for every owner a.
```

Because the incidence bits are Boolean, the two selected owners at a colour
are distinct and determine its unique physical edge.  Conversely every
direct-pair selection gives exactly these two incidences.  Thus this is a
bijection, not a relaxation.  The residual lower master is a bipartite
`b`-matching / integral network-flow fibre.

For the authenticated K17 core the exact counts are:

| object | count |
|---|---:|
| residual colours | 16,445 |
| positive-demand owners | 17,875 |
| admissible colour-owner incidences | **139,144** |
| direct pair options | **524,642** |

## 2. Sound lazy upper witnesses

A rank-ten target `T` is supplied by colour `c subset T` precisely when the
two intermediate rank-nine owners `a,b` between `c` and `T` both satisfy
`y[c,a]=y[c,b]=1`.  For a target that is currently missing, introduce a
witness `z[c,a,b]` with only

```
z[c,a,b] -> y[c,a],
z[c,a,b] -> y[c,b],
OR(all providers z[c,a,b] of T).
```

Reverse channeling is unnecessary: any valid decorated factor can extend the
model by setting one actual provider witness true, while every satisfying
witness certifies an actually selected pair.  The same witness construction
gives sound higher-upper induced-component cuts and component-shore cuts.

For a disconnected incumbent component `S`, a connected degree-two factor
must choose at least two physical edges crossing `S`; hence

```
sum(z[e] : candidate pair edge e crosses S) >= 2
```

is exact and sound.  Optional legacy `010/0110` cuts are kept separate: they
describe only a restricted local face and are not the opening-dependent K17
staircase condition.

## 3. Measured compact master

The independently audited 730-hole hint is

`scratch/k17_pbbs_u_tripleflow_upperq1_switch_greedy730_20260731.components`,
SHA-256
`d9272e95297c48bf2113b956d86adda26731938203dbed0aa67f37d6b4d3332e`.

Seeding witness rows only for its 730 missing rank-ten targets gives:

| variable class | count |
|---|---:|
| incidence variables | 139,144 |
| initial target witnesses | 20,119 |
| **compact first master** | **159,263** |
| eager direct-pair master | 524,642 |

This is a 365,379-variable (69.6%) reduction at the first exact solve.  The
preflight is frozen in
`scratch/k17_pbbs_u_decorated_incidence_preflight730_20260731.audit.json`,
SHA-256
`eea6ff42fac0eec8f0bf96484501d4f5da36688252829be20af4ae6fb75afb12`.
The stronger model is
`scratch/solve_k17_pbbs_u_decorated_incidence_cegar_20260731.py`, SHA-256
`b193f69708090256da7b9f5c48ce54c6f5805563e806f1df267d6d1e944aebab`.
It has been syntax-checked locally and preflighted with OR-Tools 9.15 on the
EPYC, but has deliberately not been launched against the live direct-pair
lane.

Immediately afterward, a neutral alternating-cycle walk (the Markov moves of
§5) reduced the same exact factor from 730 holes to **one**: only target
`0x17a78` remains, and it has five admissible providers.  The frozen factor is
`scratch/k17_pbbs_u_tripleflow_upperq1_switch_plateau1_20260731.components`,
SHA-256
`62c4626d1588c7e33d6c58cb480a23d97d2f329c44103b6f020f93e88ffdf696`.
On this hint the compact exact master starts with only

| variable class | count |
|---|---:|
| incidence variables | 139,144 |
| witness variables for `0x17a78` | 5 |
| **compact first master** | **139,149** |

That is a 385,493-variable (73.5%) reduction from the eager pair master.  The
preflight is
`scratch/k17_pbbs_u_decorated_incidence_preflight_plateau1_20260731.audit.json`,
SHA-256
`97a44d23be64c0a9c6e9861aeac4c9c74973a911ac1104c5f1979edaeb6be8d7`.

The same neutral-chain walk then closed the last target.  The fully double-
rainbow factor is
`scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_20260731.components`,
SHA-256
`6b24e8ab4c77e3e5711cacab233db29733e1b27c74b735a8fb84c9a1c3643702`:
all 24,310 lower colours and all 19,448 rank-ten upper targets occur.  It has
21 cyclic components.  With this as the hint, the compact continuation starts
with **exactly 139,144 variables and no upper-q1 witness variables**.  Frozen
preflight:
`scratch/k17_pbbs_u_decorated_incidence_preflight_q1complete_20260731.audit.json`,
SHA-256
`181f3d87c8b7759bfcfc1e4707b72556c2597c8d64e15fa7d62e2b7227ee7d4c`.

This closes the immediate upper-q1 gate without SAT.  It does not close the
remaining 21-to-1 component merge, higher upper decks, or the exact linear
staircase/opening.

## 3.1 The exact dual: lower q2 lives on owner nodes

The same incidence graph expresses the next lower deck without chronology
variables.  At a rank-nine owner `S`, its two incident lower colours `c1,c2`
(fixed or residual) satisfy

```
left_neighbour ∩ S ∩ right_neighbour = c1 ∩ c2.
```

Thus upper q1 is the pair decoration on colour nodes (`owner1 ∪ owner2`),
whereas lower q2 is the dual pair decoration on owner nodes
(`colour1 ∩ colour2`).  For a missing rank-seven target `Q`, a provider owner
has form `S=Q+{a,b}` and needs precisely incidences `(Q+a,S)` and `(Q+b,S)`.
If one is a fixed-core incidence the provider is one existing `y` literal; if
both are residual, one dual witness implies both `y` literals.  An OR of all
such providers is exact by the same extension argument as upper q1.

On the double-rainbow hint, 15,095 of 19,448 q2 targets occur and 4,353 are
missing.  Every missing target has a provider.  Their exact initial encoding
uses 5,917 single-incidence providers and 124,026 dual witnesses, for

| variable class | count |
|---|---:|
| incidence variables | 139,144 |
| dual q2 witnesses | 124,026 |
| **simultaneous q1+q2 master** | **263,170** |

This remains almost exactly half the 524,642-variable direct-pair q1 master,
while enforcing a strictly stronger deck.  Frozen preflight:
`scratch/k17_pbbs_u_decorated_incidence_preflight_q1q2_20260731.audit.json`,
SHA-256
`5633e069213a6f442f9182e1fc68b804892cc642a40971b7c6823fa703add655`.

## 4. What elementary presolve does *not* find

Three independent negative diagnostics delimit the remaining difficulty.

1. Exact equality/ALO unit propagation fixes **zero** of the 524,642 pair
   options.  Failed-literal propagation on all 872 options belonging to the
   101 upper rows of provider count at most ten also fixes zero.  Audit:
   `scratch/k17_pbbs_u_decorated_low_provider_probe_20260731.audit.json`.
2. The target-colour upper projection has a matching saturating all 13,541
   missing targets.  Alternating reachability from the 2,904 surplus colours
   reaches every target and every colour, so there is no Hall-tight DM core.
   Audit: `scratch/k17_pbbs_u_decorated_upper_hall_20260731.audit.json`.
3. In the exact lower b-matching fibre, orient unused incidences
   colour-to-owner and used incidences owner-to-colour.  The resulting graph
   is one SCC on all 34,320 vertices.  Therefore every one of the 139,144
   incidences belongs to some exact lower b-matching; SCC presolve deletes
   none.  Audit:
   `scratch/k17_pbbs_u_decorated_bfactor_scc_20260731.audit.json`.

These are useful negative theorems: the fixed core is not stuck on a local
degree or Hall obstruction.  The genuine coupling is upper decoration,
connectivity, and the later opening/staircase gate.

## 5. General-construction connection

The incidence normal form also supplies the exact Markov basis used in the
general protected-factor program.  The symmetric difference of two feasible
lower masters is an Eulerian bipartite graph and decomposes into alternating
cycles.  Toggling any such cycle preserves every colour degree (two) and every
owner residual degree.  Conversely every two feasible lower factors are
connected by these toggles.

Thus the current K17 carrier search and the general UPMBC/(E1) problem have
the same algebraic move space: lower-rainbow exactness is a network-flow fibre;
only the protected face (upper decks, opening-compatible residence, and low
component count) remains non-linear.  The 730-hole hint being a strict local
minimum under primitive alternating-6 switches does not contradict this
connectivity—it proves that longer or neutral alternating-cycle chains are
needed.
