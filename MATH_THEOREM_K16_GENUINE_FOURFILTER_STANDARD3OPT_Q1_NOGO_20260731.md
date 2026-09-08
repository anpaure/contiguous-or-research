# Genuine four-filter K16: standard three-opt cannot close q1

**Date:** 2026-07-31  
**Status:** exhaustive for the stated endpoint-preserving standard three-opt
family; no claim about four-opt, ladder braids, or K16 globally

## 1. Authenticated source

The source target chronology is

```text
scratch/k16_genuine_fourfilter_natural_targets_20260731.word
SHA-256 0f6d64e9311ef634169964350baa8f817b17b9d1619970c881f87e7346550a5c
```

It is the complete rank-eight layer generated from the genuine four-filter
K15 seed `51f57125...` by

\[
 \operatorname{rev}(2^{15}\!\cup D^2A[0:6390])
 \;\Vert\;D^3A\;\Vert\;
 \operatorname{rev}(2^{15}\!\cup D^2A[6391:6436]).
\]

Its adjacent rank-nine palette has exactly the two holes

```text
b3cc  d3cc.
```

## 2. Quantified move family

Choose three path edges `c0<c1<c2`.  They split the chronology into four
segments `A,B,C,D`.  Keep the global endpoints fixed, put `B,C` in either
order, and orient each independently.  Thus each cut triple has exactly

\[
  2\cdot2\cdot2=8
\]

standard endpoint-preserving reconnections.  Internal edge colours are
unchanged; only the three cut colours are removed and the three new seam
colours are added.

## 3. Exact cut reduction

For a missing rank-nine colour `H`, every new edge of colour `H` joins two
rank-eight facets of `H`.  In a standard three-opt, every endpoint of a new
seam is adjacent to one of the three cuts.  Therefore, if a reconnection adds
both missing colours, at least two of its cuts are immediately before or
after a facet occurrence of `b3cc` or `d3cc`.

There are 31 distinct such special cut positions.  Consequently it is
complete to choose two special cuts and let the third range over every path
edge, then deduplicate sorted triples.  This gives exactly

```text
5,974,165 cut triples
47,793,320 reconnections.
```

The reduction does not assume that the third new seam is rank nine and does
not assume either missing colour occupies a prescribed seam.

## 4. Exhaustive result

For every reconnection, the audit updates the exact multiplicity of every
affected rank-nine colour: the three deleted colours, three inserted colours,
and the two pre-existing holes.  It finds

```text
q1-complete reconnections: 0.
```

Hence no member of this entire standard three-opt family can even pass the
q1 gate.  P/Q capacity, arbitrary upper coverage, and lower Hall matching
need not be considered for this family.

This is stronger than the previous single-reversal observation, but it is
not a no-go for:

- a four-or-more-cut rethread;
- a general permutation/orientation of all four segments that moves global
  endpoints;
- the natural insertion-cut family;
- a multi-seam Hamilton braid in the `D2/D3` containment ladder; or
- a non-P/Q equality architecture.

## 5. Frozen artifacts

```text
scratch/search_k16_genuine_fourfilter_3opt_area_20260731.cpp
  SHA-256 e6bf0df755365090c4043552c133b7358d8c38f0537576dd1007f0dd7413a93f

scratch/k16_genuine_fourfilter_3opt_20260731.stdout
  SHA-256 fd7cb027714f92d6f92a973f37e53de66dd3c5662ecdbe8708f56e21dc895552

scratch/k16_genuine_fourfilter_3opt_20260731.stderr
  SHA-256 856e7cd2c7fc0a8802ab5743a91b0276bda779ed5c378a1b7454a29152aedba4
```

The optimized local replay took 6.25 wall seconds and 6.17 user seconds.
An independent audit is requested separately; until it lands, the primary
enumeration and the proof above are the evidence for this scoped theorem.
