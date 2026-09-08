# Audit of the `m=5` synchronized three-`C10` state

Date: 2026-07-31  
Status: exact finite compatibility audit; positive occurrence connector at
`h=1`; strict-run and fixed aligned-one-edge faces fail; no deeper-shadow or
compiler claim

## 1. Input and verdict

The authoritative finite certificate is

```text
scratch/catalan_standard_m5_three_c10_private_repair_20260731.audit.json
SHA-256 f43e39674c4a027fe46ed2f9918e8c3dcc218865816decad4a8e1f4b8052c7e1
payload  ca3c2ffe5bc7f7a93543f63be93a282f39c12eb08e8fdd9f2fefb4f132b0d1fe
```

The source changed while the first version of this audit was being frozen.
The final change is nonmaterial for every coordinate below: it enriches the
one-switch/BFS/necklace census, most recently by adding the forced-decoration
diamond-orbit ledger.  The exact certificate projection used here—circuits,
marks, ports, staircase, common core, private paths and four-state glue
cube—has canonical SHA-256

```text
b2288732faea01a07f358fb0a44eec66436d8145a9859a670c3702bd76309b1d.
```

Replaying the prior and current source produced byte-for-byte equal
compatibility coordinates after deleting only source provenance.  Thus the
drift is enriched metadata, not a changed packet or state verdict.

The independent replay gives the following fail-closed matrix.

| coordinate | exact verdict |
|---|---|
| lower/upper turn palettes | **PASS**, `84/84` on each shore |
| alternating occurrence matching | **PASS**, augmented rank `210/210`, with all twelve standard ports forced |
| root-to-final common-core linkage | **PASS**, common rank `197`, deficiency `13`, and thirteen disjoint augmenting paths |
| gap forest / leaf peeling | **PASS** on all four states of the two-glue cube; the perfect matching is unique |
| binary-trace forest | **PASS** on all four cube states |
| strict residence/run state | **FAIL** on all four cube states |
| private lower gap-owner paths and selected port marks | **PASS** |
| fixed aligned one-effective-edge catalogue on both labels | **FAIL** |
| physical diamond lift | **PASS**, a linear forest of `42` paths |
| occurrence-level socket closure | **PASS**, an explicit `42`-connector cycle |
| primitive voltage | **PASS only vacuously**, because this finite base has `h=1` |
| deeper shadows, erosion/residence controller, common cap, compiler | **NOT CERTIFIED** |

Thus the three-`C10` packet is a genuine finite repaired Catalan linear
matching base with a physical socket closure.  It is not the full
leaf--run--socket inductive state and is not an all-dimension packet theorem.

## 2. Palette and common-core linkage

The three displayed circuits are pairwise vertex-disjoint and replay the
exact staircase

\[
 (3,3,3)\to(2,2,2)\to(1,1,1)\to(0,0,0),
\]

where the entries are lower missing colours, upper missing colours, and
augmented matching deficiency.  In the final augmented occurrence graph a
perfect matching of order `210` exists after forcing all `168` selected turn
edges; in particular, all twelve ports of the two standard hexagons are
selected.  The frozen matching signature has SHA-256

```text
dd76898dd030536c2d412e4023cc035c4b41e9e6d43c3a5fdc337caddaaf9d27
```

Intersecting the source and repaired augmented graphs gives matching order
`197`.  A Kőnig cover of order `197` independently proves maximality.  The
symmetric difference with the final perfect matching consists of

```text
13 augmenting paths: vertex lengths 4^11, 6, 16
 4 alternating cycles: vertex lengths 4^4.
```

The full labelled linkage signature has SHA-256

```text
12bc2a08d69b400d0a9534ca0f84e0baa3fc57d72b777758e080b79dd116297d
```

This is the exact end-to-end common-core certificate.  It is not a prepared
sequential linkage table for arbitrary future repair packets.

## 3. Leaf peeling passes, strict runs do not

With the final decoration fixed, the two standard glue bits have component
orders

```text
(0,0): 120,132
(1,0): 252
(0,1): 252
(1,1): 252.
```

In every state the labelled gap--lower-colour graph is a forest and has
exactly one perfect matching.  Hence its matching is recovered by successive
leaf peeling.  The binary mark trace is also on the forest side in every
state.

This must not be confused with the stronger strict-run coordinate.  Every
state has many cyclic zero-runs of length two and odd one-runs, so the rule

\[
 \text{zero-run length}\ge4,
 \qquad \text{one-run length even}
\]

fails.  Moreover, in the preglue state one of the two physical components
has no protected `0^4` block.  After either standard glue the resulting
Hamilton component contains two such blocks.  Consequently:

* exact trace-forest acceptance is proved;
* a per-component protected-breaker invariant is not available at the
  preglue boundary; and
* the packet cannot be inserted unchanged into an induction which requires
  the strict run state.

## 4. Private gap-owner paths pass; the stronger aligned face does not

The two standard labels retain their exact private owner paths

```text
[82]-gap-[84]-gap-[88]
[50]-gap-[52]-gap-[56].
```

Their off-path owner triples are disjoint, their local selected palettes are
unchanged by their standard toggles, and all twelve physical standard ports
are protected selected occurrences.  This proves the finite private
gap-owner-path statement, not a named physical socket pairing.

It does **not** prove the fixed aligned one-effective-edge catalogue of the
generic gluing theorem.  Starting with two preglue components, either
singleton toggle gives one component, but selecting both toggles also gives
one component:

```text
components(empty, first, second, both) = (2,1,1,1).
```

Two labels selected together therefore are not a size-one spanning tree in
one fixed graphic edge image.  At least one label is context-dependent or
topologically neutral after the other.  The exact private cube is positive;
the stronger static aligned-label interpretation is false.

## 5. Physical forest and socket closure

The selected diamond matching has exactly

```text
84 A-turn diamonds + 84 B-turn diamonds + 42 residual cross diamonds.
```

Their `210` distinct Johnson edges on the middle layer of `B_10` form a
linear forest with `42` path components.  The endpoint-pair signature is

```text
2e5708f6c04d74ad9b96537d14fce6aea2920b84b8716d75adcd062e525835b2.
```

There are `297` legal unused endpoint-occurrence connector records; every
one of the `84` formal ports has degree at least four, and every path has at
least seven other path neighbours.  A compact `84`-state `AddCircuit` model
found an exact one-cycle choice of `42` connectors.  Its certificate is

```text
scratch/threadD_m5_three_c10_socket_cycle_20260731.json
SHA-256 9225ab90b4ffcdab8134ee2433a9f50615f5bec51669bfc706709a776acbf01f
```

The independent replay does not trust the solver status: it checks that the
component order is a permutation, every orientation is Boolean, every
selected seam is a literal Johnson edge from the occurrence catalogue, and
all `42` seam edges are distinct.  Since `h=1`, the voltage condition is
vacuous.  This proves a physical endpoint/socket closure for this finite
base, but supplies no nontrivial voltage actuator for a lifted recursive
state.

The successful remote run used one CPU, `5,038` branches, `2` conflicts,
`0.0345` solver seconds, and `88,472` KiB peak RSS.  An earlier `1` GiB
virtual-address cap failed during OpenBLAS import and is classified only as
resource-limited `UNKNOWN`, not as a mathematical result.

## 6. Exact boundary

Nothing in these artifacts records consecutive-union witnesses beyond the
immediate turn ranks, a residence/erosion controller, a physical compiler
word, or a common-cap Hall matching.  Therefore no deeper-shadow,
coefficient-one word, or all-`m` induction statement follows.

The proved finite implication is precisely

\[
\boxed{
\text{three synchronized }C_{10}\text{s}
\Rightarrow
\text{complete alternating decoration}
+\text{leaf-peelable gap graph}
+\text{private two-glue cube}
+\text{physical }h=1\text{ socket closure}.}
\]

The strict-run coordinate and the fixed aligned-label coordinate are exact
obstructions to treating this as an already closed recursive state.

## 7. Reproduction

Run the solver-free replay:

```text
python3 scratch/threadD_audit_m5_three_c10_state_compatibility_20260731.py
```

It writes

```text
scratch/threadD_m5_three_c10_state_compatibility_20260731.audit.json
```

with canonical payload SHA-256

```text
49474c9c07e0e07568cdf023ae68f8fd2108ca4d8ce72f22be5ddaf8089f0290.
```

This hash is now defined after JSON key normalization.  In particular,
parsing the file, deleting `payload_sha256`, and canonicalizing it reproduces
the displayed value exactly; integer-keyed in-memory histograms cannot change
key ordering across serialization.

The replay source and JSON file SHAs are frozen separately in the handoff.
