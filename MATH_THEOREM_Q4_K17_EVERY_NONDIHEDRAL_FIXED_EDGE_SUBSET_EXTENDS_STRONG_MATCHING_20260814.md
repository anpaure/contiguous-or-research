# Every subset of the eight q4 k17 nondihedral fixed edges extends to a strong perfect matching

**Date:** 2026-08-14

**Status:** Exact finite theorem in the 70-row fixed-owner projection.  This
does not assert a cover of the 680 nonfixed owner bracelets, an exact lower
ledger, or a full pure-rail factor.

## 0. Result

Normalize a reflection-fixed rank-nine owner necklace on `Z_17` as

```text
                 {0} union (+-A),       A in binom([8],4).       (0.1)
```

Thus the fixed-owner vertex set is `binom([8],4)` and has size 70.  The
strong globally lifted self columns project to the graph

```text
 G_2:  A--B  iff  |A intersect B|=2.                         (0.2)
```

It is 36-regular and has 1,260 edges.  The complete quotient-self,
fixed-lower catalogue frozen in commit `3a6f1768` supplies the following
eight additional, pairwise vertex-disjoint edges in the stable indexing of
`owner_orbits()`:

```text
e0=(22,31)       e1=(246,1391)   e2=(341,1290)   e3=(497,1301)
e4=(509,1362)    e5=(704,832)    e6=(799,1347)   e7=(899,1145). (0.3)
```

Every edge in `(0.3)` joins two four-subsets with intersection three, so it
is outside `G_2`.

> **Theorem 0.1 (all 256 mixed fixed faces close).**  For every subset
> `I subset {0,...,7}`, delete from `G_2` the two endpoints of every `e_i`
> with `i in I`.  The residual graph has a perfect matching.  Equivalently,
> the selected nondihedral edges together with strong distance-two edges
> extend to a perfect 35-edge matching of all 70 fixed owner bracelets.

In particular, this holds simultaneously for all `2^8=256` choices; it is
not only the previously frozen all-eight completion.

## 1. Exact census

Put `k=|I|`.  The residual graph has `70-2k` vertices, and every one of its
maximum matchings has the forced perfect size `35-k`.  The exhaustive edge
and matching-size histograms are:

| `k` | subsets | residual vertices | residual edge count: multiplicity | residual minimum degree: multiplicity | matching size: multiplicity |
|---:|---:|---:|:---|:---|:---|
| 0 | 1 | 70 | `1260:1` | `36:1` | `35:1` |
| 1 | 8 | 68 | `1188:8` | `34:8` | `34:8` |
| 2 | 28 | 66 | `1118:16, 1119:8, 1120:4` | `32:28` | `33:28` |
| 3 | 56 | 64 | `1050:8, 1051:16, 1052:16, 1053:16` | `30:8, 31:48` | `32:56` |
| 4 | 70 | 62 | `985:8, 987:24, 988:34, 990:4` | `29:32, 30:38` | `31:70` |
| 5 | 56 | 60 | `924:8, 925:16, 926:16, 927:16` | `28:40, 29:16` | `30:56` |
| 6 | 28 | 58 | `866:16, 867:8, 868:4` | `27:16, 28:12` | `29:28` |
| 7 | 8 | 56 | `810:8` | `27:8` | `28:8` |
| 8 | 1 | 54 | `756:1` | `26:1` | `27:1` |

The subset counts sum to 256.  The edge-count variation from `k=2` onward
shows that subset size alone does not determine the residual isomorphism
type.

## 2. Certificates and proof

The primary H100 output

```text
scratch/verify_q4_k17_nondihedral_edges_extend_strong_matching_all_subsets_20260814.h100.out
```

contains a literal perfect-matching certificate for every subset mask
`0,...,255` under `all_subset_certificates`.  In addition, the field

```text
by_subset_size[str(k)]["one_certificate"]                  (2.1)
```

gives one human-addressable certificate for every `k=0,...,8`.  These are
the nested masks

```text
k                    0   1   2   3    4    5    6     7     8
subset mask           0   1   3   7   15   31   63   127   255
strong edges         35  34  33  32   31   30   29    28    27. (2.2)
```

Each entry in `(2.1)` literally lists the selected edges from `(0.3)` and
the indexed strong completion; no reconstruction from an optimizer state is
needed.

For completeness, the computation first independently reconstructs the 70
vertices from their unique centred necklace representatives.  It joins two
vertices exactly when their normalized four-pair sets intersect in two,
recovering 1,260 edges.  For each of the 256 masks it deletes the chosen
endpoints and obtains a maximum-cardinality matching.  The asserted size is
then strengthened to an explicit certificate.

The independent audit does not invoke a matching algorithm.  It rebuilds
`G_2` directly, checks every listed completion edge against `(0.2)`, and
checks that the completion vertices are exactly the `70-2k` undeleted
vertices with no repetition.  A matching with `(70-2k)/2=35-k` edges is
perfect, which proves Theorem 0.1.  The same audit recomputes every row of
the table from the literal graph.

There is a useful structural explanation for why the finite instances are
dense.  Pairing each `A` with its complement identifies `G_2` as the
two-vertex independent blow-up of an 18-regular folded graph on 35
complement classes.  This observation is not used as an unproved general
extendability theorem: the exact claim above rests on the 256 checked
certificates.

## 3. Frozen provenance

The eight-edge input is the exact catalogue from commit `3a6f1768`:

```text
MATH_OBSTRUCTION_Q4_K17_QUOTIENT_SELF_FIXED_LOWER_CATALOGUE_HAS_MATCHING_EIGHT_20260814.md
sha256 911702a6e5e70700fd8d8abc9c85061d0b8643c94cdbf3497e3c1e3552c17b38

scratch/audit_q4_k17_nondihedral_self_fixed_lower_20260814.py
sha256 c9d27c4a99ed2eabe47759f14fa0bd3838333a51146baabbb7f9efa843b4321e

scratch/audit_q4_k17_nondihedral_self_fixed_lower_20260814.h100.out
sha256 324bf271234eefede36081908c38e73e72272925e2a6b4df656cae1189fc5426
```

The new verifier and independent literal-certificate audit are:

```text
scratch/verify_q4_k17_nondihedral_edges_extend_strong_matching_all_subsets_20260814.py
sha256 9e62b14740fd4090105e82bf878b7fb2773f7382b2bba0a302dc6b80031333fb

scratch/verify_q4_k17_nondihedral_edges_extend_strong_matching_all_subsets_20260814.h100.out
sha256 e95583677aaab4c5cc0714304dea9a0ebbad3e2710abaeaea7a85a51a9f53c1b

scratch/audit_q4_k17_nondihedral_edges_extend_strong_matching_all_subsets_20260814.py
sha256 896df29e8816d41e39d11159e42435585c6b3fea65588f37ff18f1d6dac78c19

scratch/audit_q4_k17_nondihedral_edges_extend_strong_matching_all_subsets_20260814.h100.out
sha256 c1011399ab7582afca41de1b30368d8ab17afe5d2e73c6447994ec7cf58f052e
```

Both H100 runs report `PASS`, check all 256 masks, and agree on every
histogram.  The audit output explicitly records that it validated every
perfect matching without calling a matching routine.

## 4. Scope boundary

The theorem closes exactly the fixed-owner matching projection for any
choice of the eight new quotient-self edges.  It does not choose one of the
two lower-deck realizations above a new owner deck, cover the 680 nonfixed
owner rows, repair the 70 fixed-lower parities, or solve the global
owner/lower pure-rail factor.  Those remain separate semigroup and exact-
cover gates.
