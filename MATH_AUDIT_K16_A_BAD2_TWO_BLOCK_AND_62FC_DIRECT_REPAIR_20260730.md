# K16 Lane A: two detached blocks close geometry, and a direct `62fc` move closes the upper tower

Date: 2026-07-30  
Status: **exact constructive carrier result; lower Hall remains deficient**

## Two-block census

Start with the arbitrary-upper-complete Lane-A chronology of SHA

```text
dc336b93f981d09bbba9f44969bef46da51c6feeab595b05c2fd6b26b340638d
```

whose only maximal-envelope failures are the adjacent rows `287d,6879`,
both missing `0010`.

Enumerate two occurrence-disjoint, independently source-closable contiguous
pre-flat blocks of lengths 1 through 64.  Orient each block independently
and place the two blocks and the two defective occurrences in all 24 relative
orders.  The exact census is

```text
oriented source blocks       1,562
occurrence-disjoint pairs    1,183,916
relative arrangements       28,413,984
local run/erosion passes             4
full replays                         4
geometry-exact candidates            4
arbitrary-upper-complete             0
```

The four exact candidates have respectively `6,3,1,4` arbitrary-upper
holes.  The best uses

```text
source 2003 length 35 forward,
source 4330 length 46 forward,
piece order 0132,
```

and has sole upper hole `62fc`.  Its chronology SHA is

```text
2d549ce428e327b4958974d91346476d5e1f020e658b5da724d92c845ac5b01e.
```

This independently reproduces AD's frozen split-pair carrier.

## Direct repair of `62fc`

The nine rank-eight facets of `62fc` occur once each.  The complete direct
quotient therefore consists of 216 distinct one-segment reversals and
one-row relocations which install an adjacent facet pair.

Exact replay gives

```text
unique candidates                 216
geometry-exact                       2
arbitrary-upper-complete              4
simultaneously exact and complete     1
```

The simultaneous carrier reverses rows `[4376,5884]` inclusive in the
one-hole chronology.  It has

```text
length             12,873
capacity            32,063
flats               6320,12869,12871
zero envelopes      0
replay defects      0
arbitrary-upper holes 0
SHA 4bd6be21b216009b854c6b2da72500a07e4c61efcef431533bc42e4ae7429f4d.
```

Thus the upper and carrier-geometry gates are simultaneously satisfiable in
this basin.  This is not yet a universal word: the exact generalized lower
Hall graph has matching `26300/26332`, deficiency 32.  Its 15 zero-degree
targets are

```text
2665 28e9 29a9 32f0 4879 48e9 4e70 5b60
60f8 62cc 685c 6989 6a29 6c70 8000.
```

For comparison, the original exact j3959 chronology has Hall deficiency 3
and only zeroes `2665,8000`, while root's detached-cycle pass1 has deficiency
34 and 19 zeroes.  The direct carrier is a real improvement over pass1 but
does not discharge the compiler.

## Scope and consequence

The two-block census is complete only for two independently source-closable
same-phase physical blocks of length at most 64.  The direct quotient is
complete only for one reversal/relocation that directly installs `62fc`.
Neither is a global no-go.

The positive conclusion is structural: the earlier `bad=2` seam is not a
carrier obstruction.  Two detached blocks pay both geometry charges, and one
additional direct move pays the last upper charge.  The remaining obstruction
is purely lower-Hall compatibility.

## Artifacts

```text
scratch/search_k16_a_bad2_two_detached_blocks_20260730.cpp
SHA256 a6288e3eccb37673f202d38c5780049430d5d2e86da23234519bdd5993afba68

scratch/search_k16_exact_one_upper_hole_direct_moves_20260730.py
SHA256 87f3c5665473a11043b0556a1c692359c0a218f762511f8d204257f6159a5be7

scratch/k16_a_two_block_then_direct62fc_20260730/
  two_block_result.tsv
  pre_direct_one_hole.targets
  direct62fc.audit.json
  exact_upper_complete.targets
  hall.audit.json
```
