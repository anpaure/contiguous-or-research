# `k=17` prefix coloured inventory and middle-levels split

Date: 2026-07-31  
Status: exact finite certificate for the coloured low-block inventory and
exact reformulation of the rank-eight/rank-nine gate.  No prefix ordering,
tail completion, upper tower, or length-24313 word is claimed.

## 1. The coloured inventory exists

The proposed prefix needs `2328` two-letter low blocks of types

\[
 680(3,5;\cap=0),\qquad972(4,5;|\cap|=1),\qquad
 676(4,4;\cap=0).
\]

A literal certificate has now been constructed and independently replayed.
It uses every rank-three target, `2324` distinct rank-four targets and
`1652` distinct rank-five targets, leaving exactly `56` rank-four
singletons.  In addition to low-target disjointness, all `2328` internal
block unions are distinct rank-eight sets.  Thus the coloured inventory
strengthening missing from the original Hall/EKR proof is true for `k=17`.

This does not order the blocks or choose the `2536` rank-seven separators.
The local separator graphs are nevertheless very dense.  The unoriented
block graph has `2537` vertices, `3,215,112` edges, density `0.999439`,
minimum degree `2433`, one component and diameter at most two.  On `4865`
oriented block-port states, the directed graph has `23,135,220` arcs,
minimum outdegree `3649`, one strongly connected component and directed
diameter at most two.  Bare separator compatibility is therefore not the
observed bottleneck; the global separator, rank-eight and rank-nine rainbow
resources remain coupled.

## 2. Exact corrected prefix trace

Write the prefix as `q_0,...,q_7400` and define

\[
 C_i=q_i\cup q_{i+1}\qquad(0\le i<7400).
\]

The one-pivot schedule has length-three owners on starts `0,...,7400`, not
length-four owners.  For `0<=i<7399`,

\[
 O_i=q_i\cup q_{i+1}\cup q_{i+2}=C_i\cup C_{i+1}.
\]

Hence the internal prefix gate is exactly a vertex-simple path

\[
 C_0,C_1,\ldots,C_{7399}
\]

in `J(17,8)` with distinct rank-nine edge-union colours.  Whenever the
central physical letter is a rank-seven separator,

\[
 q_{i+1}=C_i\cap C_{i+1}
\]

is forced.  Two seam-crossing triples provide the last two prefix owner
colours.

## 3. Middle-levels formulation

Let `V_0,...,V_16909` be the tail rank-eight triple cells after a successful
tail completion.  The exact rank-eight/rank-nine atlas consists of two
alternating paths in the middle-levels graph `M_17`:

\[
 C_0-O_0-C_1-\cdots-O_{7398}-C_{7399},
\]

and

\[
 V_0-O_{7401}-V_1-\cdots-O_{24309}-V_{16909}.
\]

Together these use all `24310` rank-eight vertices and `24308` rank-nine
vertices.  The two exceptional seam owners `O_7399,O_7400` are precisely
the two missing rank-nine vertices.  They complete a Hamilton path or cycle
exactly when their incidence with the four path endpoints has the required
two-connector pattern.  This is a small endpoint gate, not an automatic
consequence of the two paths.

Thus the palette problem is equivalently:

> construct two physically factorable alternating middle-levels paths of
> the prescribed sizes, then attach them through two exceptional upper
> vertices.

## 4. Upper ranks remain independent

Even exact rainbows through rank nine do not force rank ten.  The six
rank-six letters

```text
012345, 123456, 234567, 345678, 456789, 056789
```

have distinct pair, triple and quadruple unions of ranks seven, eight and
nine, while their two five-letter unions coincide.  Ranks `10,...,16`
therefore require an explicit facet-run or protected-witness condition.

## 5. Reproducibility

```text
scratch/build_k17_prefix_colored_inventory_20260731.py
  SHA 47d1e9183d2e9047dd4a23e417636559cfb40de2c117722b4bc2bf1a64c8beb6
scratch/k17_prefix_colored_inventory_20260731.json
  SHA dbb4b85bbc5ba86378b212e235f3f833694e9f09f2c931b2196922dc19c58de5
scratch/audit_k17_prefix_colored_inventory_20260731.py
  SHA 125c1a9daa157f7dbf6c4cae09822b5a630b1fba089f6eabac8c5459f1e163b2
scratch/audit_k17_prefix_ordering_graph_20260731.py
  SHA 15e8877c4b27e3a59183d7cef21924b75cf8ed6e63c3c97a639686617b143acf
```

The coloured-inventory canonical payload SHA is
`2977ee1396f00abd8d92bcca109be987c66415a59ff3a7fbd9e24ea097cfa8a6`.
