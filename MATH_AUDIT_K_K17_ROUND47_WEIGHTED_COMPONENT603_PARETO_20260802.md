# Audit: K17 round47--weighted component 603 Pareto fixture

**Date:** 2026-08-02  
**Status:** PASS for the exact static bottom matching, target partition,
complete supplier projection, and indexed relaxed9 socket census stated below.
This is not a fixed-state `1S-ROTS` certificate and no SAT instance was run.

## 1. Inputs and candidate

The two authenticated complete real-bottom matchings are:

* round47, materialized table SHA-256
  `95dee6e9718f9067d4bd5c860f7763a45ee03785bdbb13b20b8d95540a7a2735`;
* the global weighted static seed, selection SHA-256
  `c880bcecb7c5ec95e812babe4afc7f1bc2ccb1df27a3708904cca94c7aa510e9`.

Their symmetric difference has a path component numbered `603` by the
frozen catalogue.  It has `22` real-bottom vertices, `23` right-host
vertices, and `44` coloured difference edges.  Its old unmatched hard host
is row `5022`, whose complete-menu degree is zero; its new unmatched hard
host is row `14492`, whose complete-menu degree is `90632`.

Flipping precisely that path gives

```text
scratch/k_rots_k17_joint_1s_20260802/component603_pareto_audit/
  component_603.table.tsv
```

with SHA-256

```text
54b8063b4f39afb8ffccabadb88f04b65edaa0a4321c343f84f15918d75f24f4.
```

The literal `22`-edge replacement ledger is
`component603.flip.tsv` in the same directory.

## 2. Why component flipping is exact

Let `P_0,P_1` be complete real-bottom matchings on the same left shore.
Both saturate every free host and exactly `16898` hard hosts.  In
`P_0 triangle P_1`, every real token and every free host has degree zero or
two.  A hard host has degree zero, one, or two; degree-one hard hosts are
exactly the symmetric difference of the two short sets.  Therefore every
nontrivial component is an alternating cycle or a path joining one old
short to one new short.

Flipping a whole component preserves degree one at every real token and at
every internally covered host.  A path only exchanges its two unmatched
hard endpoints.  Consequently any subset of the disjoint components is
again a complete real-bottom matching.  Because every real bottom is still
placed exactly once, all free hosts remain occupied, and every chosen edge
is a legal Boolean containment edge, materialization preserves the complete
lower-target partition and the histogram `(0,7395,16915)`.

For component 603, an independent comparison of the old, weighted, and
candidate maps found:

```text
real donors                         18646
old/new-different donors            18183
candidate donors taking new edge       22
candidate donors taking old edge    18161
neither-old-nor-new choices              0
right-host collisions                    0
changed physical rows                   23
```

Thus the candidate is literally one whole alternating path, not a partial
relay or an aggregate short-set exchange.

## 3. Independent static replay

An independent donor-path normal-form replay against original table SHA
`db960ce5b51e0fdea7b048d35d48ca737096b16ee73a20df873beb0517e5f185`
verified:

* every owner and root is unchanged;
* all moved bottoms satisfy their free-root or hard-middle containment;
* all `65535` targets occur exactly once;
* the length histogram is `(0,7395,16915)`;
* there are `1748` terminal donor paths, no donor cycle, and maximum path
  length `12` in the complete materialized table.

The audit JSON has SHA-256
`271546a95839f40425cbec66565e11c7d321780e9a3eef368848c403f629c503`;
its reconstructed real-bottom arcs have SHA-256
`87acb6d754c9c3fc05f6d61981a89ac40c4d262a7aa68c2e32526b1ca40e5564`.

## 4. Exact supplier projection

For a materialized table, let the left shore consist of all `24310` source
rows and the right shore of its `16898` hard heads.  An edge is present
exactly when at least one of the complete `6/9/4` source flags is compatible
with one of the four ordered head flags, with self-supply forbidden.

The incremental evaluator is exact for a component flip.  Its changed-row
set is the full right-host set of the component.  Hence it:

1. recomputes every changed source against every current hard head;
2. discards every old edge into a changed head;
3. recomputes every unchanged source against every changed head; and
4. retains only edges whose source row and head row are both unchanged.

These four classes partition the final projection graph.  A separate full
four-flag replay then verified

```text
hard heads                  16898
maximum supplier matching  16898
supplier deficiency            0
```

in `full_fourflag.audit.json`, SHA-256
`4ac8f356e7c4b6eb48b10f90210678981b097ba7db67756e8074d106c212dadb`.

## 5. Exact Pareto improvement and scope

The same indexed relaxed9 socket enumerator was run independently on
round47 and component 603:

| table | exact socket triples | zero socket roles |
|---|---:|---:|
| round47 | 2188 | 5969 |
| component 603 | 2207 | 5967 |

The component-603 audit and summary have SHA-256 values
`ee013ffb31fcc16fe24fda2332805bb13fc77f68bc3c120a12d585921288426c`
and
`6e99f47bc53e0bb9f06705ce5e2ab9448c4a78251eb99f9978a7f432e63b15df`.
The independent copies are byte-identical.  Therefore component 603 is the
first frozen table in this component face that strictly beats round47 in
zero roles while retaining supplier projection `16898/16898`; it also
improves the secondary triple count by `19`.

The `5967` zero roles remain fatal to launching a fixed-table `1S` SAT under
the stated workflow.  This audit proves no simultaneous socket choice,
degree/cycle/address one-hot, residence, upper deck, common cap, compiler,
or word.  After the separately proved private `1748`-short bank, this table
is a scoped Pareto fixture; the current downstream gate is the fixed/free
`5647`-role DNF together with residual long--long completion.

## 6. Evaluator hardening corrections

The mathematical result is proof-safe because the endpoint artifacts above
are independently authenticated.  The two component sources are not by
themselves self-authenticating:

1. `read_old` checks only injectivity and cardinality.  It does not prove
   that its arcs materialize the supplied round47 table or that every arc is
   a legal containment edge.
2. `read_new` checks the real-token image and counts `1748` declared `S`
   rows, but does not check that the `S` set is exactly the complement of the
   real-host image, nor that every `P/X` edge is legal.
3. the one-component `flip` calls the target-partition census, but its local
   validator does not recheck strict row containment.  Legality is inherited
   from the separately authenticated endpoint matching, not established by
   that call alone.

A hardened evaluator should bind hashes, reconstruct both endpoint tables
from the original row table, check every `P/X` containment edge, verify
`S=H\setminus image(P)`, and compare an incremental graph hash with a full
rebuild for every frozen winner.

## 7. Proof-safe Benders cut

Let `x` be the vector of component choices.  For a physical head row `h`,
let `H_h(x)` indicate that it is hard, and let `A_{uh}(x)` be the exact
compatibility truth table for source `u` and head `h`, set to zero when
`H_h(x)=0`.  Each row state belongs to at most one disjoint component, so
`A_{uh}` depends on at most the two component bits controlling `u` and `h`.

For every fixed physical head set `X`, define

\[
 q_{X,u}(x)=\bigvee_{h\in X} A_{uh}(x).
\]

The exact, assignment-independent supplier Hall row is

\[
 \boxed{
   \sum_u q_{X,u}(x)\ \ge\ \sum_{h\in X}H_h(x)
 }
 \tag{7.1}
\]

for every `X`.  A deficient candidate supplies `X` from its alternating DM
shore.  Encode the two-bit compatibility functions and the ORs exactly with
auxiliary Boolean variables; do not replace (7.1) by stale provider-degree
counts from the incumbent.  If the exact component hypercube has no
projection-perfect, lower-zero candidate on a declared admissible bank,
the violated rows (7.1), together with exact activation truth tables, are a
proof-safe global core for that face.  A fixed-table Hall shore alone is only
that assignment's no-good.

## 8. Bound sources

```text
catalogue source
  7400859a506490048df9fef119ca50b3910e1a6ba09a214780b518c9dfea0ed8
incremental evaluator source
  244dbf09cc2179518e17409f56c9b4e6b36fd7a555128dd60cfcd7f896de1bb8
independent donor-path audit source
  81783bfdb08dcf473450de160a2e12821535769de40c97bbfcce36f4b3c1a933
indexed socket audit source
  b8f73de61ca62e880d417faac43c96f305c9c9a36bf8b00f038c74a9abac92e1
```

