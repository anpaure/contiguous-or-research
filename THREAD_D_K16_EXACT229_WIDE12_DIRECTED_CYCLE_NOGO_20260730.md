# Exact229 wide12 directed-cycle no-go: independent audit

**Date:** 2026-07-30.

## Certified statement

Fix the exact229 chronology and its (212/187) Hall shore.  Consider one
directed token cycle

\[
p_0\leftarrow p_1\leftarrow\cdots\leftarrow p_{r-1}\leftarrow p_0,
\qquad 2\le r\le 8,
\]

whose positions are pairwise separated by at least twelve and whose individual
baseline replacement arcs preserve the frozen flat ledger and exact maximal
envelope equations.  No such cycle increases the fixed shore neighbourhood by
the required (25) cells.  In fact, among every bound-relevant closure, the
maximum exact gain is only (4).

This closes precisely the single-cycle, support-at-most-eight, wide12 class.  It
does not close a union of disjoint cycles, a nonseparated exchange, or a cycle
with more than seven nonroot positions.

## Independent arc census

The independent program tested all (165701250) nontrivial ordered position
pairs.  It reconstructed local legality without mutating the chronology and
also compared every decision with the frozen helper; there were zero
disagreements.  The exact arc census is:

```text
legal arcs       165666
maximum added         4
maximum net           4

(added,lost,net) : multiplicity
(0,0, 0) : 157830
(0,1,-1) :   2843
(0,2,-2) :    251
(0,3,-3) :     14
(1,0, 1) :   3840
(1,1, 0) :     45
(1,2,-1) :      2
(2,0, 2) :    611
(2,1, 1) :      3
(3,0, 3) :    226
(4,0, 4) :      1
```

The independently emitted positive-arc table is byte-identical to the
production table, SHA-256
`8d45283cf170713af419ed2cc86d206d32e5200c5098c64353633eea73486268`.

## Canonical DFS lemma

Every directed cycle in scope has a unique rotation whose root (p_0) is its
minimum position.  Starting from that root, the DFS follows its unique directed
successor order: every later vertex is greater than the root, unused, and
separated from every earlier vertex.  The reversed order is the inverse
replacement and is correctly a separate directed cycle when its arcs exist
(for a two-cycle the two orientations coincide).

After (u=|\mathrm{path}|-1) scored arcs, at most (8-u) arcs remain, including
the eventual closure.  Since every arc has net at most (M=4),

\[
\mathrm{score}+4(8-u)
\]

is a valid completion upper bound.  The identical post-add bound is used before
descending an edge.  Thus a cycle of gain at least (25) cannot be pruned.
Finally, separation twelve makes the complete profile-start intervals
([p-5,p+6]) disjoint, so the arc nets add exactly.

The independent DFS reproduced all production counters:

```text
nodes                 100373
bound prunes          590071
reached closures         680
maximum pruned bound      24
```

Here “reached closures” means closures surviving the upper-bound pruning, not
all low-score legal cycles.  The production `cycles.tsv` contains none of them
because it logs only score-at-least-25 closures.

## Literal replay of all 680 reached closures

The audit materialized all 680 reached closures, independently recomputed their
full maximal-envelope geometry, arbitrary-width accumulated-union upper holes,
and actual fixed-shore current, and checked exact equality with the summed arc
score.  All 680 preserve exact geometry.  Ninety also preserve complete upper
coverage.  Their scores are:

```text
-3:1, -2:4, -1:18, 0:508, 1:116, 2:27, 3:5, 4:1
```

There are 544 two-cycles and 136 three-cycles among the bound-reached closures;
no longer prefix can remain competitive with threshold 25 under the exact
bound.  The closure ledger SHA-256 is
`2cc8534c9b65167b0ba41acc45897d749a60e754508606853e01f9f37a0d447d`.

## Reproducibility

The independent H100 run used one CPU, 21.55 seconds wall time, and 7112 KiB
maximum RSS under a 1 GiB address-space cap.

Principal artifacts:

```text
1a0276b284d47071f73016abf0ef7e013e6f4f22e5af986d6553c69e9c4e91bc  audit_threadD_k16_exact229_wide12_cycles_independent_20260730.cpp
406f4527dc52f7da2fb4ac35e0e5830d2d2ffbc5a75967ce11b6c2b8c4ed1541  independent.audit.json
2cc8534c9b65167b0ba41acc45897d749a60e754508606853e01f9f37a0d447d  independent_closures.tsv
4bfd5bf9141ba5d6bb797e2141039f7b102ab0962a437fec1864a88575057b59  audit_threadD_k16_exact229_wide12_compare_20260730.py
e7c3143806df2edd611b7cb1bfe3079335b88a6b90113a7e3cb4e865e0587766  comparison.audit.json
```

The comparison payload hash is
`83f343be6dea89fdd377fe99db0c95cde27068741cd478935166254008965c1e`.

One stale production comment calls the shore “pass1” and mentions 249 targets;
the executable input and result correctly use the exact229 (212/187) shore.
The pinned production binary/result are not altered.
