# Thread D: exact protected split-B true-five-cut obstruction

Date: 2026-07-30

Status: exact scoped no-go.  The complete phase-compatible split-`B`
true-five-cut fibre has 27,439 representations.  None is complete even at
upper depth one.  In particular there is no candidate for the later
G0/envelope/capacity/arbitrary-upper/static-lower filters, and no COMP3 solve
or word claim is warranted.

This closes a strict enlargement of both the 1,200-row fixed refinement and
the fixed-three-plus-one four-cut fibre.  It does not cover a sixth cut, a
second independent bridge, or a moved/rebuilt protected collar.

## 1. Frozen source and the boundary correction

Let `Q=(Q_0,...,Q_12872)` be

```text
scratch/k16_resident_state2_upper2_targets.txt
SHA-256 77dd098d7e066cd81ed68846d554c5e5a7247e90ec764033394287f312c28464.
```

Its first flat is `Q_6432=Q_6433`.  The protected source neighborhoods are

```text
0x4c71: Q[3276..3281],
0x4c39: Q[5723..5728].
```

The exact directed-seam catalogue leaves the two advertised starts

```text
C=Q_12826=0x4a79 -> Q_4243=0x5879,
C=Q_12826=0x4a79 -> Q_5336=0x4979,
```

and both intersections equal `0x4879`.

There is a critical off-by-one.  Put `b0=Q_6388=0x4679` and
`Z=Q_6389=0x6639`.  The core relevant to the question is

```text
K_s = Q[:s] | Q[6389:12827] | Q[s:6389] | Q[12827:],
      s in {4243,5336}.                                  (1.1)
```

Exact replay gives three and only three failed middle rows, beginning at
output position `s`; each loses precisely bit `0x0400`.  Its upper holes are

```text
s=4243: {0x4e79,0x58f9,0x5af9},
s=5336: {0x497b,0x4e79,0x697b}.                          (1.2)
```

Replacing boundary `6389` by `6388` is a different row: it has no
`0x0400` carrier defect and five upper holes, including `0xc679` and
`0x6f79`.  The production engine asserts (1.1)--(1.2), so that wrong parent
cannot silently enter the census.

## 2. Complete phase-compatible quantifier

Conceptually retain the four cut edges

```text
3279, s-1, 6388, 12826
```

and add one cut at `t`.  Require:

1. the two displayed source neighborhoods remain literal, forward, and at
   depth three;
2. the directed join `Q_12826 -> Q_s` remains present; and
3. the outer prefix and suffix remain forward.

### Lemma 2.1 (two-class classification)

Exactly two classes satisfy these conditions.

The `B`-tail class is

```text
BT(s,t) = Q[:s] | Q[t+1:12827] | Q[s:t+1] | Q[12827:],
s in {4243,5336},  s <= t <= 5722.                       (2.1)
```

It has `1480+387=1867` representations.

The missing arbitrary-bridge class cuts the `C` head after the full first
flat and moves that head behind the protected `B` block:

```text
CH(s,t,epsilon)
 = Q[:s] | Q[t+1:12827] | Q[s:6389]
   | Q[6389:t+1]^epsilon | Q[12827:],                    (2.2)

s in {4243,5336}, 6433 <= t <= 12825,
epsilon in {forward,reverse}.
```

It has

```text
2 * 6393 * 2 = 25572
```

representations.  Thus the exact total is

```text
1867 + 25572 = 27439.                                    (2.3)
```

#### Proof

The `0x4c71` neighborhood fixes the initial protected block forward.  The
service condition fixes the block ending in `C=Q_12826` immediately before
the block beginning in `Q_s`.  The `0x4c39` neighborhood lies before the
source first flat, so it must remain before that flat after the braid.

With only one additional cut there are two ways to reverse the bad relative
order.  One may split the `B` block before its protected neighborhood and
move its forward tail before `C`, giving (2.1).  Or one may split the `C`
block after the complete flat and move the flat-containing head after `B`,
in either orientation, giving (2.2).  A cut in the initial block, through a
protected neighborhood or through the flat, or either other placement puts
the `0x4c39` neighborhood after the first flat or destroys its literal
forward order.  This proves completeness.  Direct origin-index replay in the
engine independently verifies the service join and both literal intervals
for every one of the 27,439 descriptors.  \(\square\)

Class `CH` is the strict new part.  Its cut range and both orientations are
absent from the 1,200-row refinement and from either fixed-three-plus-one
fibre.

## 3. Exact rank-nine obstruction

### Lemma 3.1 (rank-nine edge criterion)

For a sequence of rank-eight masks, a rank-nine mask `S` is the union of a
nontrivial consecutive interval if and only if some adjacent pair in that
interval has union `S`.

#### Proof

The reverse implication is immediate.  For the forward implication, every
row of the interval is a rank-eight subset of `S`.  Since their union is
`S`, at least two rows differ.  At the first adjacent change, the two
distinct rank-eight subsets of the same nine-set omit different elements,
and hence have union `S`.  \(\square\)

Therefore a block braid changes the complete q1 ledger only at its removed
and added boundary edges.  Reversing a block does not change its internal
undirected edge colours.

The source q1 holes are

```text
H0=0x4e79, H1=0xc679.                                    (3.1)
```

For `BT`, the removed edges are

```text
(s-1,s), (t,t+1), (12826,12827),
```

and the added edges are

```text
(s-1,t+1), (12826,s), (t,12827).                         (3.2)
```

The exact edge-count update leaves both masks in (3.1) uncovered in every
row.  Its q1-deficiency histogram is

```text
3^813 4^1054.                                             (3.3)
```

For `CH`, the removed edges are

```text
(s-1,s), (t,t+1), (6388,6389), (12826,12827).             (3.4)
```

The added edges in the forward orientation are

```text
(s-1,t+1), (12826,s), (6388,6389), (t,12827),             (3.5)
```

and in the reverse orientation they are

```text
(s-1,t+1), (12826,s), (6388,t), (6389,12827).             (3.6)
```

Let

```text
J_4243 = Q_4242 union Q_4243 = 0x58f9,
J_5336 = Q_5335 union Q_5336 = 0x497b.                    (3.7)
```

For each fixed start `s`, `J_s` is absent from every `CH` row.  In the
forward orientation `0x4e79` is absent as well.  In the reverse orientation
the variable edge `(6388,t)` can repair one relevant colour, but never both
the inherited and local debts.  The exact histograms, aggregated over both
starts, are

```text
CH forward: 2^2 3^28 4^12756,
CH reverse: 2^2 3^20 4^12764.                            (3.8)
```

Thus the minimum q1 deficiency is two and no row is q1-complete.

### Theorem 3.2 (protected split-B true-five-cut no-go)

None of the 27,439 phase-compatible representations is upper-complete.
Consequently none can pass the requested G0/envelope/capacity/all-upper/
static-lower chain.

#### Proof

Lemma 2.1 exhausts the topology.  Equations (3.2)--(3.8) are the exact
rank-nine edge ledger, and Lemma 3.1 makes this ledger equivalent to q1
interval coverage.  Both classes have positive q1 deficiency.  Since q1 is
a necessary part of arbitrary-upper completeness, every descriptor is
rejected before the later filters.  \(\square\)

This is a logical early stop, not an unevaluated search timeout.  The engine
is fail-closed: every hypothetical q1 survivor would be materialized and
checked for G0, exact depth-three collars, maximal-envelope reconstruction,
capacity, all three named hosts, arbitrary-width upper coverage, and the
complete lower static atlas.  There are no such survivors.

## 4. Reproducibility

The production source is

```text
scratch/threadD_k16_state2_splitB_true5cut_complete_census_20260730.cpp
SHA-256 1c56662c720b530fa1a09c8c25c30f03192c6561ec25d5a5e55f680b6870f8ec.
```

Its exact H100 `/home` run used one CPU, 0.43 seconds wall time, 0.22 seconds
user time, and 4,096 KiB maximum RSS.  Exit code one is the engine's
documented no-candidate status.  It is not `UNKNOWN` or a resource failure.

```text
scratch/threadD_k16_state2_splitB_true5cut_20260730/result.json
  SHA f5678d6499a8c10c581308c698525a5b56c539200df29458a082d6ac88563eb7

scratch/threadD_k16_state2_splitB_true5cut_20260730/stdout.log
  SHA c45bc4d2f07dcc0189a36021c51334510e50f58e44fa011d023c83e8da375963

scratch/threadD_k16_state2_splitB_true5cut_20260730/stderr.log
  SHA 08d627eae294cfd3fa8378213fc1da54bb605d3fd0412ad527d1f3ef22974580

scratch/threadD_k16_state2_splitB_true5cut_20260730/q1_directed_seams.tsv
  SHA cf1c32f8af2bd2b669a01cc499017b2cbc8f13cabc7c8bccd64ce163ed27aac9
```

A structurally separate Python replay reconstructs the complete rank-nine
edge census directly from (3.2), (3.4)--(3.6), agrees on all 27,439 rows,
and records the histograms (3.3), (3.8):

```text
scratch/audit_threadD_k16_state2_splitB_true5cut_q1_20260730.py
  SHA 857ab2726050533fdd82d8ae710d3df427721450dbb196f47b2af26c599c042a

scratch/threadD_k16_state2_splitB_true5cut_20260730/independent_q1.audit.json
  SHA aa376b56ddee493d11bcc10399a481a88ef3a9690c55da689d8e4a212cad00ff
  payload 200f8873be1ce1a5c3edad1b07cd66454d7168a833a8ed95092ebb78a53245b1.
```

The global bracket remains

```text
12873 <= nu(16) <= 12874.
```

The exact next topology must use a sixth cut/second independent bridge, or
move and reconstruct at least one protected collar.  Merely changing the
single bridge endpoint or reversing its `C` head cannot succeed.
