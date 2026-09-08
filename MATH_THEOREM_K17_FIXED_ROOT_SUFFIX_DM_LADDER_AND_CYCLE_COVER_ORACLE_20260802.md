# K17 fixed-root suffix DM ladder and exact cycle-cover oracle

Date: 2026-08-02

Status: proof-safe target-assignment theorem.  This note was derived by
read-only inspection of the local ladder source and ledgers; no solver or
remote action was used.

## 1. Verdict

On a fixed rank-eight receiver-root bank, suffix rethreading is exactly an
allowed-edge perfect-matching problem relative to the current rank-seven/root
matching.  Contracting the current matching gives a directed exchange graph.
Its strongly connected components are the Dulmage--Mendelsohn elementary
blocks:

* every supported permutation and every suffix circuit stays inside the SCC
  blocks;
* a singleton SCC is forced identity in every supported permutation;
* membership in a nontrivial SCC is necessary and sufficient for
  **individual** target movability; and
* simultaneous movement of any prescribed role set is decided exactly by a
  bipartite perfect matching, equivalently a Hall/min-cut oracle, inside the
  SCC blocks.

The four locally frozen faces split the 623 rank-seven phase-union-zero P2
roles as

\[
 138/485,\quad194/429,\quad220/403,\quad461/162
\]

into individually cycle-live/forced-identity roles.  In the maximally
relaxed fixed-bank face, 162 named labels are forced to keep their current
rank-eight receivers under every support length and every packing of suffix
circuits.  A C6 is one directed 3-cycle, so C6 columns can harvest existing
SCC mobility but cannot unlock a singleton or cross an SCC boundary.

This is a target-movement theorem, not an absolute socket-repair no-go.  It
forces a receiver-bank change only for an architecture that requires every
named defect to be repaired by moving its own rank-seven label (or after a
separate invariance theorem proves that an unchanged label remains zero).

## 2. Exchange digraph

Let `V` be the 19,448 current slots containing a rank-seven target.  Write
`S_u` for the current rank-seven label in slot `u` and `R_v` for the fixed
rank-eight root of slot `v`.  For a face `F`, the loopless exchange digraph
`D_F=(V,A_F)` has

\[
 u\longrightarrow v
 \quad\Longleftrightarrow\quad
 u\ne v,quad S_u\subset R_v,quad
 \text{and the receiver conditions of }F\text{ hold}.       \tag{2.1}
\]

Identity loops are implicit but are excluded from every reported arc count.
On a fixed-bottom face, a current long-H receiver `v` additionally requires

\[
                         B_v\subset S_u.             \tag{2.2}
\]

The four nested faces are:

1. old rank-seven P2 receivers plus unprotected current-long H receivers,
   with (2.2); all 3,496 endpoint hosts of the 1,748 private tickets are
   excluded from the nonidentity H receiver shore;
2. all current-long H receivers, with (2.2);
3. all current-long and all 1,748 current-short H receivers, with (2.2) on
   long receivers; and
4. every current rank-seven receiver, with all lower-bottom conditions
   deleted.

The vertex deck remains all 19,448 slots in every face; a receiver disabled
by a face retains only its implicit identity assignment.

## 3. Exact SCC/DM theorem

### Theorem 3.1 (SCC factorization)

Add the implicit identity loops to `D_F`.  If `pi` is any supported
permutation of the rank-seven labels over the fixed roots, then every selected
edge `u -> pi(u)` has both ends in one SCC of the loopless graph `D_F`.
Consequently:

1. `pi` preserves every SCC setwise;
2. every singleton SCC is forced identity;
3. after deleting every cross-SCC arc, the supported-assignment polytope is
   the direct product of the per-SCC assignment polytopes; and
4. a vertex is individually movable if and only if its SCC has size at least
   two.

#### Proof

Every permutation decomposes into disjoint directed cycles.  A selected
nonidentity edge lies on its permutation cycle, so its head reaches its tail
and its endpoints are in the same SCC.  This proves 1--3.  A singleton has no
usable nonidentity cycle and is forced to its identity loop.  Conversely,
every vertex of a nontrivial strongly connected digraph lies on a directed
cycle; use that cycle and use identity loops elsewhere.  This proves 4.
\(\square\)

The last statement is only individual.  Different cycle-live vertices need
not admit one common disjoint cycle packing.

### Theorem 3.2 (simultaneous movement and min--max)

For a prescribed set `K subset V`, form a bipartite graph `G_F(K)` with left
and right copies of `V`.  Retain every exchange arc as a left-to-right edge
and every identity edge except `u-u` for `u in K`.  Then a supported fixed-bank
permutation moving every member of `K` exists if and only if `G_F(K)` has a
perfect matching.

Equivalently,

\[
 \delta_F(K)=\max_{X\subseteq V}\bigl(|X|-|N_{G_F(K)}(X)|\bigr)=0. \tag{3.1}
\]

A deficient Hall shore is an exact proof-safe obstruction and is returned by
one matching min-cut.  By Theorem 3.1 this test factors over SCCs; singleton
members of `K` fail immediately.  Thus SCC membership is the correct
preprocessing, while the internal matching is the exact simultaneous-packing
oracle.

## 4. Exact four-face ladder

The frozen local summary is:

| face | vertices | nonidentity arcs | SCCs | largest SCC | cycle-live | forced identity |
|---|---:|---:|---:|---:|---:|---:|
| protected fixed-bottom H | 19,448 | 27,357 | 17,512 | 1,259 | 138 | 485 |
| all current-long H | 19,448 | 32,171 | 14,284 | 4,077 | 194 | 429 |
| add all current-short H | 19,448 | 44,407 | 7,728 | 10,683 | 220 | 403 |
| fixed receiver bank, delete all bottoms | 19,448 | 136,136 | 421 | 18,953 | 461 | 162 |

The final face is an assignment supergraph of the first three.  Any extra
socket, state, supplier, protected-resource, or chronology condition which
retains the same label/root bank can only shrink the feasible permutation
set; it cannot make one of its singleton labels assignment-movable.

The C6 rethread on one P2 and two H rows contracts to a directed 3-cycle.
Compositions and row-disjoint packings of such C6s remain within the SCC
blocks.  Hence the authenticated positive C6 is a local harvest column, not a
complete generator for the fixed bank.

## 5. Relation to root-basis exchange

Let `M_7` be the transversal matroid on the rank-eight roots presented by
rank-seven/rank-eight containment.  The current 19,448-root receiver set `B`
is an `M_7` basis.  Alternative matchings on the same basis differ by closed
alternating cycles; after contraction these are exactly the directed circuits
described above.

If an outside root `r` is admitted and a current root `b` is retired, a legal
single basis exchange

\[
                         B-b+r                       \tag{5.1}
\]

is witnessed by an open fundamental alternating path.  Thus changing root
type is an ordinary matroid basis move, not an arbitrary chronology move.
When the low layer is also fixed, (5.1) must pass a second low-receiver
alternating-path test; the full correlated object is the two-matroid common
basis treated in
`MATH_THEOREM_K17_THREE_LEVEL_COMMON_BASIS_AND_SOCKET_NON_TU_BRANCH_FLOW_20260802.md`.

The 162 singleton pairs do not imply 162 bank exchanges.  One open exchange
path can alter several assignments.  They prove only that no fixed-`B`
permutation can move all 623 named labels, and therefore that at least one
operation must leave the fixed-bank cycle face if moving every label is the
repair requirement.

## 6. Scope that must not be strengthened

The audited bad set is the phase union `Z_0 union Z_1`.  It is not a
phase-resolved count of singleton common zeros.  If the two phases are
alternatives rather than simultaneous obligations, the union count alone is
not a phase-independent no-go.

More importantly, keeping a singleton label/root pair fixed does not prove
that its socket predicate remains zero after other rows change.  A fixed-bank
construction can still leave this graph by:

* changing which rank-seven slots receive lower predecessors, so a former
  short P2-type role becomes long;
* regenerating endpoint modes after other H middles move;
* changing owner/root-carrier incidence;
* choosing a different permitted phase; or
* enlarging the endpoint/state grammar or planting a new endpoint module.

Therefore `root-bank recoupling is necessary for every K17 solution` is not
a consequence of the SCC ledger.  The proof-safe conclusion is the exact
fixed-bank target-movement obstruction above.

## 7. Frozen local evidence and evidence tier

```text
scratch/k17_global_chain_recoupling_20260802/
  audit_k17_rank7_suffix_scc_ladder_20260802.cpp
    f44d20ca0d10f352610132dfa4a430772a4c863d4a378810dd864fa53d0774a2
  rank7_suffix_scc_ladder.summary.tsv
    a68f1b2a8b40a95bd68a42a38f73ed5aae48a43aaba21b920129d453b4246ee4
  rank7_suffix_scc_ladder.protected_fixed_bottom_H.roles.tsv
    9ae757b709067a29b21ede0f65af6b16c0d320db493a346a772eeaf5ea278e45
  rank7_suffix_scc_ladder.all_current_long_H.roles.tsv
    6bc27fbbd7198c05bbcb6182ecff85c6c314d467183871f18ab350e024d59c5f
  rank7_suffix_scc_ladder.add_all_short_H.roles.tsv
    fab2a870fd377588264b2800a05afe233a50cac51d0c3bd489ce03c91804f874
  rank7_suffix_scc_ladder.fixed_root_bank_no_bottom_constraints.roles.tsv
    80d53fa5ab4d0c356bbf9be55099f103a6b77c15265e05161c0aa7de77117581
```

The source verifies the 785 old rank-seven P2 receivers, all 16,915
current-long rank-seven H receivers including the 17 soft rows, all 1,748
current-short H receivers, and the 1,748-ticket/3,496-distinct-host protected
bank.  The protected ticket input was previously frozen at SHA-256
`d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1`.

The four-rung directory does not yet contain an argv/input manifest or a
separately implemented replay.  This note therefore freezes the displayed
local source/output hashes and the mathematical implication of those ledgers;
it does not upgrade the first 138/485 row to independently replayed
provenance.  The last three rows and, separately, the maximally relaxed row
have stronger independent replay bindings in
`MATH_THEOREM_ROOT_K17_RANK7_FIXED_ROOT_BANK_SCC_OBSTRUCTION_20260802.md`.

What remains is the simultaneous internal matching census for any chosen
repair set, phase-resolved and regenerative socket replay, and then the
common endpoint/state, protected bank, supplier Hall, long-state,
chronology, residence, upper/source/compiler, and word gates.
