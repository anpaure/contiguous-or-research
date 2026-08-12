# Audit design: K17 augmented-quotient socket pricing and carrier-local Benders cuts

Date: 2026-08-02

## 1. Scope

This note fixes the proof boundary between the static augmented outer
matching and the one-short relaxed-nine common-state oracle.  It is an
interface and implementation audit, not a state-SAT, residence, upper,
source, common-cap, compiler, or word certificate.

The authoritative static outer normalization is the dummy-permutation
quotient of the square matching

\[
 (18{,}646\text{ real bottoms})+(1{,}748\text{ dummies})
 \longrightarrow F_{1748}\cup H_{18646}.
\]

A real bottom may enter an `F` or `H` destination only through the exact
containment edge in the authenticated outer map.  A dummy may enter only an
`H` destination.  Dummy names are pure symmetry.  The quotient variable
`S_h` says that `H` destination `h` is occupied by some dummy; no cut or
heuristic in this interface may mention a dummy identity.

The exact full outer has 2,531,237 real assignment variables
(401,754 `x` and 2,129,483 `p`), 18,646 `S` variables, and the three exact
matching row families:

1. one real assignment per real bottom token;
2. one real assignment into every `F` destination;
3. one real assignment or `S_h` at every `H` destination.

Consequently every feasible quotient point has exactly 1,748 selected `x`,
16,898 selected `p`, and 1,748 selected `S` variables.

## 2. Carrier-local potential long-mode bank

Fix one authenticated owner phase `phi`.  The unrecoupled skeleton has four
classes:

```text
F                 1,748 original length-one rows
P2                3,899 fixed length-two rows
H                18,646 hard original length-three rows
soft                 17 fixed rank-one-bottom length-three rows
```

Each real assignment `p_(u,h)` materializes the potential long state

\[
       (B_u,M_h,R_h;T_h^\phi),
\]

and the seventeen soft rows contribute their fixed long states.  If `S_h`
is selected, destination `h` materializes the short state

\[
                 (M_h,R_h;T_h^\phi).
\]

For this short state, the complete relaxed-nine potential socket bank
enumerates:

- all 2,129,483 carrier-legal `p` long modes plus the 17 soft modes;
- all four flags on each predecessor and successor long mode;
- all nine strict nested contiguous short addresses;
- every neutral/downward flag pair `beta <= alpha`;
- pairwise real-token and `H`-destination matching compatibility; and
- equality of predecessor/successor flags when both incidences use the same
  long role and mode, because that role has one shared address; and
- the exact common literal five-cell state by a 32-state, 17-coordinate
  nonempty-cell dynamic program enforcing both short cover equations.

The bank is deliberately a superset of modes extendable to a full outer
matching.  Therefore a positive count is only a heuristic promise, while a
zero count is globally sound for this phase: every complete matching uses a
subset of the enumerated modes.

For each `h` the pricer exports:

```text
exact_hyperarcs
distinct_mode_pairs
flag_pair_mask and its diversity
short_address_mask and its diversity
distinct predecessor/successor mode counts
```

`HARD_GLOBAL_RELAXED9_ZERO` means `exact_hyperarcs=0`.  Since the canonical
physical 3/2 menu is a subset of relaxed nine, such a zero is canonical-zero
as well.  The zero is phase-local unless the two independently bound phase
sets are identical.  Current instructions use this fact only to omit the
corresponding `S_h` edge from a seed heuristic; the exact outer master is
left byte-for-byte unpruned.

## 3. Exact seed objective

Let `D_h`, `M_h`, `F_h`, and `A_h` be respectively the exact hyperarc count,
distinct mode-pair count, flag-pair diversity, and short-address diversity.
Restrict the `H` ground set to non-HARD slots.  On this restriction the
selectable short sets are the rank-1,748 restriction of the dual of the real
assignment transversal matroid: a partial short set `Q` is independent iff
deleting `Q` leaves a full rank-18,646 real matching.

The seed objective is exactly

\[
 \mathop{\rm lexmax}_{|Q|=1748}
 \left(\sum_{h\in Q}D_h,
       \sum_{h\in Q}M_h,
       \sum_{h\in Q}F_h,
       \sum_{h\in Q}A_h\right),
\]

with smaller `h_index` as the final deterministic tie-break.  Descending
lexicographic matroid greedy with a full matching-extension oracle is exact
for this symbolic weight.  If the non-HARD restriction has rank below 1,748,
the seed fails closed and the unpruned master remains the next interface.

The materializer must independently replay all 65,535 lower targets, the
length histogram `(0,7395,16915)`, the fixed 3,899 `P2` rows, the 17 soft
long rows, and the phase-specific owner/root bijections.  A weighted seed is
not called state-positive until the complete fixed-table address/socket
oracle is regenerated and independently replayed.

## 4. Dummy-free Benders literals

Write `z_e` for a real `x` or `p` assignment atom.  For a complete quotient
assignment `Y`, its 18,646 selected real atoms determine all 1,748 short
occupancies.  Therefore the safe full-assignment state no-good for phase
`phi` is

\[
 \neg g_\phi\ \vee\!
       \bigvee_{e\in Y_{\rm real}}\neg z_e,             \tag{4.1}
\]

where `g_phi` is the authenticated carrier/owner-phase guard.  No `S_h` and
no dummy literal is needed in (4.1).  Under the real-token and destination
exact-one equations, retaining all 18,646 selected real atoms fixes the
entire quotient point.  Clause (4.1) is authorized only after the fixed-table
state UNSAT result and its binding to `Y` and `phi` are independently
verified.

If both licensed phases are exhausted for the same real assignment, the two
guarded clauses may be resolved to the payload-only no-good only when the
host master independently proves that the two phase guards are exhaustive.
Failure in one phase alone is never an unguarded payload cut.

## 5. Smallest exact support for one empty common-state row

For a short realization `sigma`, let `T(s,sigma)` be the exhaustive set of
potential exact five-cell sockets.  The realization guard is:

```text
fixed P2 short       true
F short              selected x_(u,F), which also fixes its bottom
H short              S_h
```

After conditioning on `sigma`, every potential socket `t` requires at most
two dynamic long atoms `p_(u,j),p_(v,i)`; a fixed soft long contributes no
outer atom.  The address literals are recourse choices and are exhaustively
projected over, not frozen in an outer cut.

For incumbent `Y`, define `B_Y(t)` to be the selected real/short-occupancy
atoms that conflict, through a token or destination exact-one row, with at
least one required outer atom of `t`.  If the row is empty, every `B_Y(t)` is
nonempty.  The smallest guard-conditioned dependency support is the exact
minimum hitting set

\[
 C^*\in\arg\min_C |C|,
 \qquad C\cap B_Y(t)\ne\varnothing
       \quad(t\in T(s,\sigma)).                         \tag{5.1}
\]

It yields the proof-safe carrier-local clause

\[
 \neg g_\phi\ \vee\ \neg\sigma\ \vee
       \bigvee_{c\in C^*}\neg c.                       \tag{5.2}
\]

For a fixed short the `not sigma` literal is absent.  If the complete
potential bank itself is empty, (5.2) reduces to `not g_phi or not S_h` for
an `H` short, to `not g_phi or not x_(u,F)` for an `F` realization, or to a
phase-scoped empty clause for a fixed short.  A numeric minimum in (5.1)
requires an exact hitting-set solve or a checked core; inclusion-minimality
alone is not a minimum proof.

This support construction is a projection of the exact row activation
formula.  A Hall shore from one already materialized table is not such a
formula and must not be reused as an outer cut.

## 6. Global state failures beyond an empty row

If every row is nonempty but the coupled address/cycle-cover state oracle is
UNSAT, the default is the full real-assignment clause (4.1).  A smaller core
is allowed only from a single parameterized state CNF in which every direct
arc and socket hyperarc is linked iff to all of its `x/p/S` mode guards, the
hard outer matching equations are present, and the UNSAT proof and projected
assumption core are independently checked.  Marginal union matching,
current-table socket degree, and disjoint relay-column scores are not valid
substitutes.

Any other real assignment differs through one or more alternating components
of the augmented matching; after quotienting dummy names, components may
move short occupancy between `H` slots.  The state oracle prices and no-goods
the terminal whole assignment.  Scores of separate relay increments are not
additive state certificates.

## 7. Current authenticated bindings and implementation

The current s7 inputs used by the implementation are:

```text
origin skeleton SHA-256  db960ce5b51e0fdea7b048d35d48ca737096b16ee73a20df873beb0517e5f185
outer edge map SHA-256   d39b58f679f4d9219b72209b06ea71387db64cdecac649a4f390c9f7ed13da25
outer independent audit b8baee46a30167e3844de42d43d8e3f224a88242460245cb6e8f65b146f3cc28
outer frozen manifest    09ea90ac43e2563b7a4a2b7219f0e8c3856cfab70d3e45f45236c620f02f5b2e
s7 phase 0 SHA-256       ac52c0f1a00c91848a0f65f04745aa9a5d5a76d63169ddf3351e44c524f02207
s7 phase 1 SHA-256       736fc30c014c7b535f036348380ed46f545c1ef9bf1e409f515660fff2229058
s7 carrier model         37a160f2b3f02839fcd9621dccb42cce43a0297016cdf050ded742baa6f84748
```

Implementations:

```text
scratch/ad_k17_c1_potential_socket_pricer_20260802.cpp
scratch/solve_ad_k17_weighted_potential_socket_outer_seed_20260802.cpp
scratch/run_ad_k17_s7_potential_socket_pricer_h100_20260802.sh
```

Heavy execution is restricted to O3 C++ on H100 CPU in the unique root

```text
/home/amodo/or15/work/ad_v5r_s7_potential_socket_pricer_eqflag_019fc04bf4d7_20260802
```

An earlier calibration root without the `eqflag` suffix allowed `alpha>beta`
when the same long mode appeared on both sides of one short.  Its zero rows
remain conservative but its positive degrees and diversity are invalid and
must not seed the outer matching.

The definitive metric counts, phase comparison, seed tables, independent
replays, and hashes are appended only after those jobs finish.  Until then,
no HARD deletion, seed success, Benders cut, or state verdict is frozen.
