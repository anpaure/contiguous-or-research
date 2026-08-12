# Independent audit: `k=17` shuffle201 synchronized circulation

Date: 2026-08-01  
Lane: R / chronology-first OFHT  
Audited theorem: `MATH_THEOREM_R_K17_SHUFFLE201_SYNCHRONIZED_FLAG_TRANSITION_CIRCULATION_20260801.md`  
Verdict: **PASS after the scope corrections recorded below.**

## 1. Frozen source and finite replays

The source certificate is

```text
scratch/k17_rank8_rooted_static_shuffle201_20260801.certificate.tsv
SHA256 d44b60611a3c9e4ba1533a774762fce825d327dcc7536cdcd9c10522404b1ad3
```

The independent direct-row replay reconstructs the exact type and tight
lower-target ledger and gives

```text
legal packet turns / labelled state arcs         970 / 7760
packet matching / zero-out / zero-in             556 / 723 / 826.
```

The fixed-outer-face C++ replay, its literal edge list, and an independent
comparison program reproduce

```text
menus / packet arcs / loops                       16925 / 7462 / 2
zero-out / zero-in                                      21 / 80
maximum matching                                         1335
Hall tail / neighbourhood                            1169 / 1074
old Hall tail's neighbourhood in the new graph              1322.
```

Thus the old `1206/1080` shore is crossed but a new deficiency-95 shore is
present.  This validates the theorem's conclusion that one frozen shore is
not a monotone potential.

The independently reconstructed reverse-tie circuit selection contains
449 pairwise root-disjoint circuits on 856 roots, comprising 42 unary and
407 binary circuits.  It reproduces the final row table byte-for-byte and
gives

```text
turns / packet matching / zero-out / zero-in
970 / 556 / 723 / 826  ->  1855 / 954 / 234 / 445.
```

Every type multiplicity and every tight common `A/B` target resource is
unchanged.  The common root--owner both-live projection has matching only
`718/1430`; hence the factor is not an occurrence-owner chronology.

## 2. Mathematical audit

### 2.1 Static Rado decomposition

PASS.  Once one outer shell `(type,B)` is fixed at every root, completion of
the exact lower ledger is equivalent to five labelled bipartite perfect
matchings for `|A|=2,...,6`, plus local rank-one choices.  The rank-six
right shore must be recomputed as all rank-six targets minus the selected
rank-six `B` targets.  Treating rank-six `A` and `B` occurrences as separate
resources would be wrong; the theorem uses the required common resource.

### 2.2 Collapsed versus occurrence-state circulation

PASS after correction.  Flow balance on a complete row flag is exact only
for the collapsed packet-root cycle-cover relaxation: an entering and a
leaving arc can use different attachment states.  Literal occurrence-owner
exactness requires the separate state

```text
(root, complete row flag, attachment-owner orbit, phase)
```

and statewise balance there, together with exact root, owner, and resource
rows.  Under the established arc convention, an arc's `H` incidence pairs
its tail root with the attachment-owner orbit of its head state; state
balance and the owner transversal consequently make both owner shores
exact.  No connectivity conclusion follows.

For a deficient intermediate, circulation is too strong.  The exact score
uses independent in/out capacities bounded by the selected flag or selected
attachment-state variable.  Only at score 1430 do these capacities saturate
to the corresponding circulation.

### 2.3 Hall/min-cut formulation

PASS.  For any selected collapsed flag set `x`, Hall gives precisely

\[
 x(X)\le x(\Gamma^+(X))
\]

for every flag family `X`, and the exact partial score is

\[
1430-\max_X\bigl(x(X)-x(\Gamma^+(X))\bigr)_+.
\]

Alternating reachability in a maximum matching is therefore an exact
min-cut separation oracle.  This is a resource-constrained Boolean master,
not a total-unimodularity claim.

### 2.4 Fixed-face lower bounds

PASS.  A perfect matching must send 95 tails of the new Hall shore outside
its old neighbourhood.  If `R` is the set of rows changing outer `B` orbit
or type and `K` is the set receiving a target migrated from the old `B`
stage to the new `A` stage, exact target use injects `K` into `R`.  Each
escaping edge charges at most its changed tail and changed head, so

\[
95\le 2|R\cup K|\le4|R|.
\]

Hence `|R|>=24`; without stage migration, `|R|>=48`.  In every case at
least 48 complete row flags change.  The location-weighted cut and the
intermediate bounds `M<=1335+4|R|`, respectively `M<=1335+2|R|` without
migration, follow by the same tail/head charging.  A root-disjoint circuit
of support at most two has cut coefficient at most four, giving the stated
24-column floor.

## 3. Scope

The audited positive factor is an exact static lower-resource factor with a
strictly improved collapsed packet transition matching.  It does **not**
certify one common attachment-state transversal, a connected/voltage-valid
physical cycle, upper shadows, an opening, residence beyond the rooted age
recurrence, or a common-cap compiler.  A collapsed matching of 1430 would
close only the packet-root support gate; the full attachment-state
circulation would still have to be solved.

## 4. Replayed artifact hashes

```text
scratch/audit_r_k17_shuffle201_fixed_Borbit_global_A_union_20260801.cpp
  e2baecbf0cf7a201526c7f04d8be3ee2665025f61aeb5ce86cee93f93f984630
scratch/k17_shuffle201_fixed_Borbit_global_A_union_20260801.audit.json
  7881c5c5b07b908d25346821ffb79481eb3d6323b65ed875b3d08483279c9046
scratch/k17_shuffle201_fixed_Borbit_global_A_union_20260801.edges.tsv
  73d58a2b132a5edfdf1bb4a6a754c23091c365ec0ff054100bd8ea8dd7b8cf3e
scratch/k17_shuffle201_fixed_Borbit_comparison_20260801.audit.json
  e2b88f58c8c3ec39afa485e2b0746ed0eeee86b569fbca3e82780cde9f79ce8c

scratch/threadA_k17_rooted_global_support2_shuffle201_h100_20260801/
  shuffle201_reverse.candidate.tsv
    e28a8ee5825564baf0d75720d8f3c1a53a911e9c53956aff49ed2460fd08c8dd
  shuffle201_reverse.independent.audit.json
    264ba804b98b96a216b9087a948f5e74c305f13f3be2d07270ccdd3d94e752a0
  reverse.owner.audit.json
    b332ccc08662e3931d7e6afe59f945ce8e49df32f95311c7315b1b0c64b80e3d

scratch/laneK_k17_rooted_flag_catalogue_bind_20260801/
  shuffle201_reverse.selector.independent.audit.json
    a5ada1febde2daaa621bac54b0722a7429672d03b56c8aa4de20900b26d681e2
  shuffle201_reverse.owner_demand.independent.audit.json
    c87add18cfe9da003fa63e222946bf71366e81fdcd7ccf35d34cb3539c0399fe
```

