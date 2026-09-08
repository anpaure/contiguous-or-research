# The fixed capped bank has no directed rank-six-context fusion cycle

2026-09-08. One bounded exact census by root, executed only on h100.
The conditional fusion theorem is
[the directed-port lemma](PBBS_CAPPED_EQUAL_CONTEXT_DIRECTED_PORT_FUSION_LEMMA_20260908.md).
Root read that entire proof and checked its owner indices and scope.

Use the canonical146-component bank, with H=min(h,3). For every H=3
adjacent source pair, remove one shared unpinned coordinate a from both
letters, obtaining an ordered common-context candidate (E,F), with
|E|=|F|=5 and |E union F|=6. Compute the unchanged left and right
rank-eight triples as K+a+u and K+a+v. Group by (E,F,u), and record
the directed edge a->v. A directed cycle of length at least3 in distinct
components would permit the theorem's middle-layer-preserving fusion.

The exhaustive fixed-source result is:

* 74,562 eligible ports;
* 298,248 direct literal triple replays under their two-position caps;
* 29,240 ordered context groups;
* zero directed cycles of length at least3, even before imposing distinct
  component labels.

Every group has at most one edge from each coordinate, by uniqueness
of its native rank-eight left flank. The program traverses each entire
functional directed graph, not a sampled set of proposed cycles. A loop
is impossible because v lies outside the original pair, while a would
be inside it. A directed two-cycle would repeat a globally unique right
rank-eight triple. Thus the specified criterion has no realization in
this bank.

No fusion, search over cuts, alternate context, or word modification was
performed after this negative decision. This is not a no-go theorem for
all caps or all possible joining operations. In particular, more general
contexts, simultaneous state changes, different owner inventories, and
different cap patterns remain outside this census.

Artifacts:

* [Standalone census](census_k17_rank6_context_c6_ports_20260908.py).
* [Exact report](k17_rank6_context_ports_20260908/rank6_context_port_census.json).
* [Complete directed-cycle list, empty](k17_rank6_context_ports_20260908/all_directed_port_cycles.json).

Input is the exact factorized source menu with SHA-256
bf55d2ef90e32f7eac6148e1e889d87a4a0214e651adb62df543c2e7af04c642.
Remote directory: /home/amodo/exact-b-k17-rank6-context-ports-20260908/.
The run took0.621seconds under120CPU/150wall/2GiB limits and exited.
