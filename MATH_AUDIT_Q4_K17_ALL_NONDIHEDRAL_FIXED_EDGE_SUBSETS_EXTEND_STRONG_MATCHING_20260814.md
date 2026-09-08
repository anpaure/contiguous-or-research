# Hostile audit: all q4 k17 nondihedral fixed-edge subsets extend strongly

**Date:** 2026-08-14

**Verdict:** **PASS**, at the exact finite fixed-owner-projection scope stated
in the source theorem.

## 1. Audited source

```text
MATH_THEOREM_Q4_K17_EVERY_NONDIHEDRAL_FIXED_EDGE_SUBSET_EXTENDS_STRONG_MATCHING_20260814.md
sha256 1076b1f4195ffdf2340122343aaedf2afb3be171ef3d1ed0af033a6a34fb1e9e
```

The eight-edge input is bound to commit `3a6f1768` and to the frozen
catalogue output SHA recorded in the theorem.

## 2. Hostile checks

### 2.1 Vertex and edge normalization

The independent audit reconstructs, rather than imports, the normalization
of a fixed rank-nine necklace.  A unique centred representative is exactly
`{0}` together with four of the eight nonzero reflection pairs.  It finds
exactly 70 such owner-orbit indices.

For two normalized four-pair sets, the strong edge predicate is literal
intersection size two.  Direct enumeration gives 1,260 edges and degree 36.
Each of the eight frozen quotient-self edges instead has intersection size
three, none is a strong edge, and their sixteen endpoints are distinct.
Thus deletion by a `k`-subset really leaves `70-2k` vertices.

### 2.2 All-subset completeness

The primary verifier iterates integer masks `0,...,255`, so no subset orbit
reduction or symmetry assumption can omit a case.  It stores the complete
strong matching found for every mask.  It separately records the first
certificate at each subset size, which occurs at masks

```text
                         0,1,3,7,15,31,63,127,255.
```

The independent audit reads all 256 literal certificates and does **not**
call NetworkX or any other matching algorithm.  For every mask it checks:

1. the selected new-edge indices equal the set bits of the mask;
2. every completion pair is one of the 1,260 reconstructed strong edges;
3. no completion vertex is repeated;
4. the completion vertex set is exactly the undeleted vertex set; and
5. the completion has `35-k` edges.

These conditions alone prove perfectness.  Consequently the theorem does
not depend on trusting maximum-matching optimality or solver status.

### 2.3 Histogram replay

The audit independently filters the 1,260 strong edges after each deletion,
recomputes the residual degree sequence, and aggregates the 256 cases by
`k`.  Its recomputed residual-vertex, residual-edge, minimum-degree, and
matching-size histograms agree exactly with every entry in the theorem's
table.  The subset multiplicities are `binom(8,k)` and sum to 256.

### 2.4 Scope

The conclusion is only a perfect matching of the 70 reflection-fixed owner
bracelets.  It does not select physical strong lifts, solve the 680
nonfixed-row residual cover, choose lower realizations, or evade the frozen
fixed-lower parity obstruction.  The source states all four boundaries and
does not promote the finite projection result to a global factor theorem.

The complement-pair blow-up paragraph is explanatory only.  No general
factor-criticality or extendability theorem is invoked.

## 3. H100 replay

```text
scratch/verify_q4_k17_nondihedral_edges_extend_strong_matching_all_subsets_20260814.py
sha256 9e62b14740fd4090105e82bf878b7fb2773f7382b2bba0a302dc6b80031333fb

scratch/verify_q4_k17_nondihedral_edges_extend_strong_matching_all_subsets_20260814.h100.out
sha256 e95583677aaab4c5cc0714304dea9a0ebbad3e2710abaeaea7a85a51a9f53c1b
status PASS; subsets_checked 256

scratch/audit_q4_k17_nondihedral_edges_extend_strong_matching_all_subsets_20260814.py
sha256 896df29e8816d41e39d11159e42435585c6b3fea65588f37ff18f1d6dac78c19

scratch/audit_q4_k17_nondihedral_edges_extend_strong_matching_all_subsets_20260814.h100.out
sha256 c1011399ab7582afca41de1b30368d8ab17afe5d2e73c6447994ec7cf58f052e
status PASS; subsets_checked 256;
all_certificates_cover_every_vertex_exactly_once true;
reported_histograms_recomputed_exactly true
```

All compilation, enumeration, matching, certificate checking, and hashing
were performed on H100.
