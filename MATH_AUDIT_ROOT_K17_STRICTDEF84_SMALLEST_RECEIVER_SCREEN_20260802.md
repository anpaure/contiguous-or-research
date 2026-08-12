# Strict-def84 recoupled smallest-receiver screen

**Date:** 2026-08-02  
**Status:** complete, SHA-bound exhaustive no-go for C4, C6 and support-four
`(2,2)` on the `9dafc568...` parent.

## 1. Authenticated parent and frozen scope

The receiver search is based on the strongest strict-def84 root-recoupled
carrier and its materialized 438-mode table:

```text
compressed carrier
  bf5b946f9e1cd5165ba323c894208e9370e7a2b671578ef2a6231535c2ba3241
final table
  9dafc568f9b93151822053618fe4574b2b50452e944b7fb98a093c47dda9e2f3
literal b268 / native phase-0 owner table
  b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
transported phase-1 owner table
  736fc30c014c7b535f036348380ed46f545c1ef9bf1e409f515660fff2229058
```

The final table's generalized supplier projection has 74,982 edges and
matching rank `16,864/16,898`, hence deficiency 34, with 20 zero heads.  The
authenticated alternating deficient Hall witness has 51 heads and exactly 17
supplier neighbors.  This is the fixed 51/17 shore used below.  The source
audit does not by itself assert that a complete Dulmage--Mendelsohn
decomposition has been materialized.

The selected ticket ledger has SHA
`d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1`
and names 1,748 tickets with 7,213 distinct protected physical rows.  All
7,213 rows are byte-identical between literal b268 and the recoupled final
table.

The regenerated structural catalogue from task
`019fc363-103a-7ad0-83fc-037646c7aff5` is now frozen:

```text
fresh.complete.edges.tsv       e51b1688e977c11fb7dee80338f4bcc7e86b83c232c416f48bd774ac6f4d9746
fresh.complete.edges.audit     f86ff3e8045f2eac24bb8e856df1360f3f3eb33091382b6bc93827cf819f0f38
structural matching            62fef5ff936603a39302edcc490b8ec0dac6f3c155a85ad7b4907afdda4d52e4
state-support audit            0d8a3510b14f7a055f020774ca469012ded0372dc8951d3ad9231e0a27e315dd
```

It contains 115,086 freshly rederived structural edges and has structural
matching rank 3,420.  The producer semantically replays every catalogue row
against the compressed parent and rejects protected endpoints; no old b268
edge number or payload is transported into this search.

The catalogue's single-transfer marginal ledgers contain 16,095 native-p0
positives, 18,225 transported-p1 positives, 5,228 same-declared-state edges
and 3,171 exact six-tuple-common edges.  These are not a replacement
selected-parent table and are not reused as receiver-arc prices: the producer
recomputes every receiver menu on `9dafc568...`.

## 2. Exact receiver classes

Write a current short row as `(B_r,R_r)`.  A receiver move permutes the
bottom masks among distinct current short rows while retaining every target
row's literal row id, owner, root and length.  The assigned bottom must remain
a strict subset of the target root.  The open classes are exactly:

```text
C4    support 2, cycle type (2)
C6    support 3, directed cycle type (3)
P22   support 4, cycle type (2,2)
```

The two orientations of a C6 are distinct when both are legal.  P22 is
canonicalized under exchange of its two transpositions.  The support-four
single cycle `(4)` is the old C8 lane and is not reopened here, as requested.

All support rows and every dynamic predecessor/successor row must avoid the
exact 7,213-row ticket footprint.  The final-table target partition and every
protected row are independently replayed by the light auditor.

## 3. Exact fixed-shore screen

Let `Q` be the 51 shore heads and `N(Q)` their 17 final-table supplier
neighbors.  If `S` is the changed supplier-row set, only incidences of rows in
`S` can change, so the new fixed-shore neighborhood is exactly

```text
N'(Q) = (N(Q) minus changed rows losing all Q incidences)
        union
        (changed rows having a new Q incidence).
```

Every incidence is tested by the complete generalized 6/9/4 flag-pair
compatibility predicate.  A receiver circuit is retained only if

1. a changed supplier outside old `N(Q)` is compatible with some `q in Q`;
   and
2. `|N'(Q)| >= 18`.

The second condition excludes an outside supplier that merely compensates
for a lost old neighbor.  This is an exact screen against the incumbent Hall
witness, not a fresh maximum supplier matching.

## 4. Phase-common occurrence screen

For each receiver role `(target_row,new_bottom,root)`, the producer evaluates
the full relaxed-nine family and exact five-cell DP under:

```text
phase 0: literal b268 owners;
phase 1: root-aligned round047.s7 transported owners.
```

The candidate's structural row is used in both phases.  Each phase-specific
occurrence is a literal tuple

```text
(short_row, q, alpha, beta, predecessor_row, successor_row),
```

with `beta <= alpha`; one physical long row may occupy both endpoints only
when `alpha == beta`.  Protected long rows are forbidden.

Two scopes were exhaustively enumerated:

1. **State-common necessary supergraph:** `(short_row,q,alpha,beta)` is common
   while the phase-specific literal predecessor/successor rows may differ.
2. **Exact literal-common graph:** the complete six-tuple, including both
   physical endpoint rows, is identical in both phases.

For either scope, the projected joint endpoint rule permits at most one
predecessor and one successor use per physical long row and requires one
consistent flag across all its uses.  A row may bridge the successor of one
role to the predecessor of another.  This is still a necessary occurrence
projection: internal five-cell witnesses, chronology, demands and literal
cyclic cells are not thereby composed.

Phase 1 remains explicitly transported-only.  No native phase-1 or carrier
authentication is claimed.

## 5. Exhaustive census and verdict

The independent receiver graph contains 377,500 protected-safe fitting arcs
on 5,647 safe short rows.  A complete structural replay gives:

| class | all protected-safe structures | structures enlarging 51/17 shore |
|---|---:|---:|
| C4 | 13,413 | 75 |
| C6 | 256,159 | 2,622 |
| P22 | 89,778,372 | 1,001,038 |

Only the 29,219 arcs belonging to at least one shore-enlarging structure were
occurrence-priced.  This is completeness-preserving for the conjunction being
tested.  Their occurrence census is:

```text
state-common positive arcs / declared states   837 / 927
exact-common positive arcs / literal tuples    733 / 884
state/exact mutual C4 components                 13 / 10
```

An independent SHA-bound parser reconstructed every arc and relevance bit,
replayed the first stored exact witness for all 733 exact-positive arcs in
both phases, and enumerated the positive graphs:

| occurrence scope | all-role-positive C4 | all-role-positive C6 | all-role-positive P22 |
|---|---:|---:|---:|
| state-common supergraph | 13 | 0 | 76 |
| exact literal-common | 10 | 0 | 44 |

None of those circuits with every role individually occurrence-supported
enlarges the fixed shore.  The conjunctive census is therefore:

| occurrence scope | C4 passing occurrence + shore | C6 | P22 |
|---|---:|---:|---:|
| state-common supergraph | 0 | 0 | 0 |
| exact literal-common | 0 | 0 | 0 |

Thus the intersection already becomes empty before joint endpoint selection.
Both endpoint-rejection counts and accepted counts are consequently zero.
The exact and state-common candidate ledgers contain headers only.

This is a sharp no-go for the three declared classes on this SHA-bound
parent: none can simultaneously preserve the ticket footprint, strictly
enlarge the fixed 51/17 shore with an external supplier, and provide all
required phase-common occurrence roles.  It is not a global support floor.
In particular, the scope-closed C8 `(4)` class, support at least five,
chain-length-changing moves, non-permutation packets and richer occurrence
couplings remain outside this result.

## 6. Downstream composability scope

There is no screen-positive row to promote.  Therefore no candidate was
claimed to pass, or submitted to, the required downstream gates:

1. a fresh complete supplier matching and dual replay on the materialized
   candidate;
2. residual outer matching and selected-parent supplier projection;
3. complete endpoint state and cross-role demand-disjointness;
4. literal cyclic-cell replay and its residence/upper/compiler consumers.

The result is an early-gate impossibility for C4/C6/P22, not a downstream
composability certificate.

## 7. SHA-bound artifacts and execution

The frozen package is

```text
scratch/root_k17_strictdef84_small_receiver_screen_20260802/
```

Principal artifacts:

```text
exhaustive producer source     8e59296dd5235a9bbea57ee41273a9dfa3c28986b84c03a0b34bdee7e3e418b4
independent structural source  5603ca60e0ea2c4980e9d2d9563984a0cc037ade345a6d5881bff244f1fb1dfd
independent graph-audit source  9d406f9b20c3531e8eeddafe0bc745e184b03a530acf0ea232924a5962b26db4
fail-closed light auditor      6ef2db4d9b5ce610b0a042904c2ce223cf345f52ee865be99ff927ea30a2fadc
producer audit                 191445d6310705945008c99d9ba6408cea3c49df07e85bb0240bf605ec48b8a9
receiver arc-price ledger      469efc8f8c4e72b21e84b16078521df766c485d169be697fee39a3f14928dc0b
candidate census               76081cd7bb64f5bae73390f0225974b4913737e938730281f9c6a399a047c929
exact/state candidate headers  0d0845c7776ef0143c26a00f00bc7f53e380b225102ad65297f159b0e91a43d6
independent structural audit   b9d036a4151b06e72b40300c912de1961161cea4be1874f7923f0580ea0ffd94
independent graph audit        2d8b663e68a70b04c0475b49ab9df807a14feadc7eb2c9d8ec8dfc8577901340
exact light audit              deb372e048d42d2da984b20e0adeb0f534dd17c540e04a85a916cd7b108f99cc
state-common light audit       cfee7ecdf2ab0770431934fe2ccfc83e825ad06aa0785c5059933f338c5ec468
```

`BASE_INPUTS.sha256`, `CATALOGUE_BINDING.sha256` and
`FROZEN_RESULTS.sha256` verify from the local package root.
`REMOTE_INPUTS.sha256` binds the copied `input/` and `src/` layout and was
verified in the unique H100 execution root.  The current frozen-results
manifest has SHA
`16a07d701822571728cf480881c281e49993c9bd7307402735720ddf6c003060`.

The exhaustive occurrence pricing ran CPU-only on H100 in the unique root

```text
/home/amodo/or15/work/root_k17_strictdef84_small_receiver_019fc35b_20260802
```

with eight pinned cores (52--59) and a 16 GiB virtual-memory cap.  No root
radius/controller path was read for output or written, and no duplicate
radius search was launched.
