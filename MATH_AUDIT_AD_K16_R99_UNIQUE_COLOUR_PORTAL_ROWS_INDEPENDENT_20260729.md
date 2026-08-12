# Independent audit: k16 r99 unique-colour portal rows

Date: 2026-07-29

Status: **PASS in the stated loopless, degree-balanced, binary cut scope.**
No solver or H100 process was used.  No counterexample was found.

## 1. The portal implication

Let `e=uv` be the sole selected source provider of a lower or upper q1
colour, and let `Q` be the union of the endpoints outside `{u,v}` of all
loopless off-source providers of that colour.  If no off-source provider is
parallel to `e`, then every replacement provider has an endpoint in `Q`.
When `e` is cut, q1 coverage therefore creates positive added degree at a
node of `Q`.  Exact nodewise degree restoration forces positive cut degree
at that node.  Since source-cut variables are Boolean,

```text
sum_{h in source: ends(h) intersects Q} cut[h] >= cut[e]
```

is valid.  The source was independently reconstructed as 858 loopless edges
on 858 quotient nodes with degree histogram `{2:858}`.  Thus the degree
balance used in this argument is exact, not an inferred average condition.

The parallel-provider exception is necessary for this local implication and
is implemented correctly.  All addable providers are loopless, so the test
that their endpoint set is a subset of `{u,v}` is exactly the test for the
same unordered quotient-node pair.  There are 20 skipped colour rows: eight
lower and twelve upper; 16 have one parallel alternative and four have two.
Skipping the whole row is conservative; no claim is needed about whether
some skipped row might follow from additional global q1 constraints.

There is one coefficient qualification.  The stored coefficient `1` on
every incident source edge is an integer/Boolean hitting consequence.  In 52
of the 1,328 rows, a source support edge joins two nodes of `Q` (50 rows have
one such edge and two rows have two), so this unit row is not literally the
unrounded fractional sum of the degree equations.  The direct fractional
row would count such an edge twice.  This does not affect validity in the
binary CP/Benders master.  It should nevertheless be described as an
integer portal cut rather than an ordinary LP consequence.

## 2. Critical colour `(0,1849)`

Independent reconstruction of the lower-colour provider fibre gives:

```text
sole source provider: 4529
source endpoints:      {88,316}
loopless alternatives: 35
parallel alternatives: 0
alternate nodes Q:     {89,99,109,263,288,355,613}
source support:
  {3299,4560,4598,4936,5049,5463,7892,
   9827,11485,12197,12207,14126,17805,22581}
```

Fourteen alternatives have one endpoint in `Q` and 21 have both endpoints
in `Q`.  None of the 14 source support edges has both endpoints in `Q`.
Consequently the displayed critical row is also a direct fractional
consequence of q1 coverage and the summed degree equations; it does not rely
on the integer-coefficient qualification above.

## 3. The 29 canonical Pareto witnesses

The corrected scope file has SHA-256
`b1b069fe61a871fea0c6929cd44dc88bbde0d5f68de77a6b1a7d22a82c6c642e`.
Its delete component 5 explicitly has `required_edge_ids=[22511]`.
Regenerating the Pareto witnesses locally from that scope produced a
byte-identical file with SHA-256
`4c1f0826b036f515cfe6ab70a9bdda1e0d8c6a8a59fcb35bb75753292f39608a`:
14 retain witnesses and 15 delete/replace witnesses.

All 29 are distinct 99-edge source subsets, hit all 147 frozen motifs, have
the recorded unique-loss pair and cut digest, and obey the branch lock.  In
every case

```text
4529 is cut, and no edge of the 14-edge critical support is cut.
```

Hence every stored canonical witness violates the lower `(0,1849)` portal
row.  The full recomputation also matches the recorded violation histogram

```text
{17:9, 18:4, 19:4, 20:2, 21:3, 22:1, 23:6}.
```

The exact conclusion is that these 29 canonical representatives have no
loopless degree-balanced q1 completion.  It is not a pure q1-only no-go, and
it does not exclude other cuts realizing the same Pareto loss pairs; the
JSON already states the latter limitation correctly.

## 4. Artifact-hardening observation

The frozen portal checker pins the witness bytes and checks the 29 critical
violations, but does not itself recheck motif coverage, stored loss weights,
cut digests, or correspondence to the corrected Pareto frontier.  All of
those checks passed independently here.  Adding them to the permanent
checker would improve provenance against a future repinned witness file; it
is not a defect in the current frozen result.
