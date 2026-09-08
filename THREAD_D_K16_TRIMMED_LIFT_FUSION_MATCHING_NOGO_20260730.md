# K16 trimmed-lift fusion matching no-go

**Date:** 2026-07-30  
**Scope:** the literal word
\[
L=A\mid(\{z\})\mid zA[:-1],\qquad A=\texttt{answers/k15.word},
\]
and shortening operations obtained solely by replacing adjacent letters by
their union.  Letter deletions and arbitrary rewrites are not covered.

## 1. Result

The verified trimmed lift has length
\[
|L|=12876=B(16)+3
\]
and covers all `65535` nonempty masks.  Nevertheless:

> **Theorem.** Every one of the `12875` adjacent boundaries of `L` is
> individually fatal under union-contraction.  Hence no nonempty simultaneous
> family of adjacent fusions preserves universality.  In particular the three
> excess letters cannot be removed by three fusions.

This is stronger than an order-three census.  It is witnessed by two explicit
saturating target matchings plus the singleton-`z` seam guard.

## 2. Exact provider graph

Contract a set `F` of original adjacent boundaries.  Each letter of the new
word is the union of one consecutive block of original letters.  Therefore
every interval in the contracted word is an original interval `[l,r]` whose
two exterior boundaries avoid `F`.

For a target `T`, define its provider hypergraph `G_T` as follows.  For every
original interval `[l,r]` with union `T`, insert the set of its eligible
exterior boundaries:
\[
e(l,r)=\{l-1,r\}\cap D,
\]
where `D` is the boundary family being audited.  Endpoint intervals give
singleton edges, and a provider with neither eligible exterior boundary gives
the empty edge.  Then, exactly,
\[
T\text{ survives }F
\iff
\exists e\in G_T:\ e\cap F=\varnothing.                 \tag{2.1}
\]
Thus one boundary `b` destroys `T` precisely when `b` belongs to every edge of
`G_T`.

The audit enumerates every endpoint occurrence, including all plateaux where
several starts have the same interval union.  It deduplicates only identical
`(target, exterior-edge-set)` records.

## 3. The three boundary families

Write `n=|A|=6438`.

### 3.1 First copy of `A`

An unmarked target can only be witnessed wholly inside the first `A` block.
On its `6437` internal boundaries the common-provider incidence graph is
\[
b\sim S
\iff
b\in\bigcap_{e\in G_S}e.
\]
Every boundary has between `2` and `12` neighbours.  The frozen audit gives a
matching saturating all `6437` boundaries by distinct unmarked targets.  Its
target-rank histogram is
\[
1^{14},2^{99},3^{427},4^{1243},5^{1670},6^{1356},7^{1480},8^{148}.
\]

### 3.2 Appended copy `zA[:-1]`

For a marked target `z|S`, all providers have one of three old-coordinate
projections:

1. an interval of `A[:-1]`;
2. a suffix of `A` ending at the singleton `z`; or
3. a suffix of `A`, possibly empty, followed by a prefix of `A[:-1]`.

For an internal appended interval `[l,r]`, its provider edge is
\[
\{l-1:l>0\}\cup\{r:r<6436\}.
\]
A cross-seam suffix-prefix provider contributes the singleton `{r}`; a suffix
ending at the singleton `z` contributes the empty edge.  These are all marked
providers, not a fixed-width surrogate.

There are `6436` internal appended boundaries.  Again every boundary has
between `2` and `12` common-provider targets, and the audit gives a matching
saturating all of them by distinct marked targets.  The old-mask target-rank
histogram is
\[
1^{14},2^{99},3^{427},4^{1243},5^{1670},6^{1356},7^{1479},8^{148}.
\]

The internal scan has `115593` proper interval occurrences; the cross-seam
scan reaches the full prefix at index `20`.  The complete nonimmune marked ledger has `113193`
distinct provider edges after immune-target removal.

### 3.3 The two singleton seams

The remaining two boundaries are
\[
A[-1]\mid z,\qquad z\mid zA[0].
\]
The displayed `z` is the unique letter with zero old-coordinate projection.
Contracting either incident boundary removes the only interval with union
exactly `{z}`.  Hence both boundaries are fatal.

## 4. Matching consequence

Take any nonempty fusion set `F`.

* If `F` meets the first long block, choose one such boundary `b`.  Its matched
  unmarked target has every provider incident with `b`, so (2.1) says it is
  lost.
* If `F` meets the appended long block, the same argument uses its matched
  marked target.
* If `F` consists only of seam boundaries, `{z}` is lost.

Additional contractions cannot restore a target: they only impose more
alignment restrictions on original interval endpoints.  This proves the
theorem.  The matchings also show that `s` fusions confined to either long
block lose at least `s` distinct targets.

## 5. Exact remaining gate

This result must **not** be promoted to a deletion no-go.  Deleting a letter
can make the letters on its two sides adjacent, producing the union of a
punctured original interval.  Such a witness need not occur as an interval of
`L`, so monotonicity (2.1) fails.  A simultaneous three-deletion audit must
model punctured providers directly; requiring every intermediate one-deletion
word to remain universal would be an unsound restriction.

## 6. Reproducible certificate

* Source: `scratch/audit_threadD_k16_trimmed_lift_fusion_matching_20260730.py`
* Audit: `scratch/threadD_k16_trimmed_lift_fusion_matching_20260730.audit.json`
* Canonical `A` SHA-256:
  `f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b`
* Constructed lift SHA-256:
  `9d0214f6c7cea45a1f26d031687ecada9ac34500e925dcfc127bdf1514b624c8`
* Stable payload SHA-256:
  `7b830d8f892ea51bb5a0db6b1adbdb040a386221b0adebb904e83242f343000b`

The audit is standard-library only, uses no solver, stores both full matching
tables, and rechecks every matched incidence against the reconstructed
provider graph.  A local replay takes about one second.
