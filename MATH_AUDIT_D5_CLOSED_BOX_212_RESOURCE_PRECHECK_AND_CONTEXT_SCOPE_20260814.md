# The 212 closed-box resource precheck has empty sampled menus through lift four

**Date:** 2026-08-14  
**Status:** exact finite-menu H100 audit, negative only in its declared
closed-box scope.  This is not an UNSAT result for a cut-open D5 compiler.

## 0. Outcome

For each of the 212 frozen D5 terminal triples, the audit generated 400
cell-preserving relabelings of the complete 36-owner closed splice package.
It tested the literal rank-11/ground-23 bank and common-core lifts by `t=1,2,4`
fresh common-one/common-zero pairs.  Every one of the 84,800 candidates at
each lift collided with the protected radius-two D5 owner/q1 halo before a
q2 test was reached.

```text
t   rank/ground   accepted menus   owner rejects   lower-q1   upper-q1
0     11/23          0/212             50694          24014      10092
1     12/25          0/212             43836          26335      14629
2     13/27          0/212             38625          27545      18630
4     15/31          0/212             30488          28017      26295
```

For each finite menu the exact CP-SAT conflict hypergraph is therefore
UNSAT with a provably smallest singleton core: row `0`, source row `1`, hard
distance-two type, has no accepted candidate.  The hypergraph itself has no
candidate nodes or pairwise resource constraints because protected-bank
filtering empties every row first.

## 1. What the precheck means

The result is strong evidence that two complete private exterior C6 cycles
are the wrong global object.  Adding common-core freedom shifts collisions
from owner labels toward q1 labels but does not produce one admissible closed
box in this menu.

It is not an architecture-free obstruction.  A physical D5 substitution
must use cut-open context strands, identify only the prescribed boundary
occurrences, refill the q1 incidences removed from those strands, and audit
the mixed q2 windows.  The closed-box model instead asks all 34 nonmarked
owners and every closed exterior q1/q2 resource to avoid the context halo.
That deliberately overprotects resources which a true boundary compiler
must replace or reuse in a controlled way.

Consequently:

* `FINITE_MENU_UNSAT` means exact UNSAT of the sampled finite menu only;
* the singleton core is minimum for that menu because its row has zero
  candidate nodes;
* no claim is made about all cell-preserving permutations at any `t`; and
* no claim is made about the overlap-one cut-open graft or the 226-router
  serial atlas.

## 2. Exact conflict-hypergraph model

Each candidate is a cell-preserving bijection from one of the adjacent/hard
rank-seven package templates to the lifted terminal triple.  The protected
filter keeps typed banks separate and rejects any nonterminal package owner,
lower-q1, upper-q1, lower-q2 or upper-q2 value meeting the corresponding
radius-two old/new D5 socket halo.

After filtering, a Boolean variable represents every surviving candidate.
Each row requires exactly one variable and each typed resource permits at
most one selected variable.  Row activation literals expose an exact CP-SAT
infeasibility core.  Since all menus are empty in the four runs above, the
returned one-row core is trivially cardinality-minimum; no broader core
minimality algorithm is being claimed.

## 3. H100 provenance

Frozen D5 selection:

```text
94deb656dac1d8955b20d851e92600156d703842d6de169d4b6bea356fa3ec32
```

Solver:

```text
cb04892ba86065f94545fad3731b1e4c65ea1cd12210c8184a5bf4870afe5f96
  scratch/solve_d5_212_complete_splice_package_bank_20260814.py
```

H100 outputs:

```text
7973d8d2e15952b2d7bdb3f26ecf68eb91f5e310f6e6e4458a3b937ad58813f3
  scratch/solve_d5_212_complete_splice_package_bank_t0_20260814.h100.out
79c5b54c5191e2ad3f2b7929483cf4afd21a38343406f3e43d257bd7677442ba
  scratch/solve_d5_212_complete_splice_package_bank_t1_20260814.h100.out
a229255d85e9ac81b27310ddd0335c56d43dc779e11270fba3994b8c2b26bf53
  scratch/solve_d5_212_complete_splice_package_bank_t2_20260814.h100.out
46d2e05b3cadb18107f6c33bfba59684334fdbc843a44ef12607a4d65df62ac8
  scratch/solve_d5_212_complete_splice_package_bank_t4_20260814.h100.out
```

All candidate generation, protected-bank construction, CP-SAT solving and
hashing ran on H100.
