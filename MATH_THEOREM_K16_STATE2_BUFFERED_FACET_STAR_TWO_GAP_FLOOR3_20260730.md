# K16 state2 buffered facet-star two-gap no-go and gap floor three

Date: 2026-07-30

## 1. Exact two-gap class

Fix either authenticated nonlocal5opt state2 source from the one-gap theorem:

| case | source SHA-256 | blocker |
|---:|---|---:|
| 0 | `762a6361c571f4e182aa03340399d3a1c07f25755c689362da173f04bd1cc407` | `0x1639` |
| 1 | `1e75cfb4c8e610a4ea2bf1095e44d3236f655aabc3efe65e8532912b7c0572a8` | `0x1879` |

Choose three distinct rank-eight cofacet centres of the blocker and delete
their three complete radius-three source collars.  Keep every remaining row
in source order; this gives a core \(C\) of length

\[
 12873-3\cdot7=12852.
\]

Take the twenty-one unchanged deleted rows in an arbitrary order, split them
into two nonempty ordered blocks \(A,B\), and choose two distinct core gaps
\(0\le g_0<g_1\le12852\).  The final word is

\[
 C[:g_0]\;A\;C[g_0:g_1]\;B\;C[g_1:].                         \tag{1}
\]

Gap order canonically names the left and right blocks.  Reversing an input
description and swapping its two gaps gives the same canonical form.  Equal
gaps merely concatenate \(A,B\) and reduce to the proved one-gap class.

This class is deliberately wider than the layer-interleaved weave: block
orders and the split point are arbitrary.  It is disjoint from the active
directed-donor lane because no target value changes, and from long-segment
3-opt because no residual-core row moves, reverses, or changes order.

**Theorem.** No word of the form (1) is a tail-fixed G0 carrier.  More
generally, within this unchanged-value, source-ordered, three-collar class,
an exact carrier requires at least three distinct insertion gaps.

The lower bound is necessary, not sufficient: no three-gap construction is
claimed.

## 2. The directed closure witnesses

Deleting a collar centred at \(p\) creates the residual-core edge

\[
 (p-4)\longrightarrow(p+4).
\]

The exact six-by-six port graph from the one-gap theorem contains the two
phase edges at each of the eighteen possible centres.  Its signatures are

```text
case 0: 00 at all nine centres;
case 1: 10 at centre 617 and 00 at the other eight.
```

The apparent depth-two edge at 617 is unavailable in a G0 transformation of
the present kind; Section 3 proves that the source flat phase is preserved.
Thus every selected collar has an explicit failed actual-phase carrier row.

For each such failure, let \(P_p\) be the exact set of residual-core gaps at
which inserting a block could alter its dependency interval.  The literal
catalogue gives \(|P_p|\in\{4,6\}\).  For every one of the 168 instances
`(source, unordered centre triple)`, the three sets satisfy

\[
 P_{p_0}\cap P_{p_1}
 =P_{p_0}\cap P_{p_2}
 =P_{p_1}\cap P_{p_2}=\varnothing.                              \tag{2}
\]

The minimum compacted closure separations are 59 and 374 in cases 0 and 1;
the exact repair-gap separation is stronger than needed for (2).

If no insertion gap lies in \(P_p\), the complete mask/depth neighbourhood
of the canonical failed row is unchanged.  Inserting an arbitrarily long
block at another core gap only shifts this neighbourhood; it does not change
its ordered masks.  Hence the same lost-bit carrier inequality persists.

## 3. Flat-phase rigidity with two blocks

The following literal facts hold in both sources:

1. every row in every possible moved collar is unique within its source;
2. no collar intersects a source flat pair; and
3. every removal-closure endpoint pair has unequal masks.

Therefore neither removal nor any internal/external join of either inserted
block can create a flat.  If an insertion gap splits an old flat pair, the
word has fewer than three flats and fails G0.  Otherwise all three old flat
pairs survive, with the same order relative to every unpatched closure.
Every G0 candidate in (1) consequently uses each closure's authenticated
actual phase.  In particular, moving centre 617 to the relaxed depth-two
edge is impossible without first failing the flat ledger.

## 4. Three-set stabbing certificate

An exact carrier must alter all three canonical failed closure equations.
By locality, its insertion-gap set \(G\) must satisfy

\[
 G\cap P_{p_i}\ne\varnothing\qquad(i=0,1,2).                   \tag{3}
\]

Equation (2) says that one gap belongs to at most one demanded repair set.
Thus the exact transversal number is

\[
 \tau\bigl(\{P_{p_0},P_{p_1},P_{p_2}\}\bigr)=3.              \tag{4}
\]

For the two-gap class, \(|G|=2<3\), so at least one literal carrier failure
is untouched.  This proves the theorem before the contents, orientations,
or split of \(A,B\) are examined.  It also proves the stated insertion-gap
floor three for any number and order of unchanged rows placed at each gap.

## 5. Exact canonical gap-pair census

The residual core has 12,853 gaps, hence each unordered centre triple has

\[
 \binom{12853}{2}=82,593,378
\]

canonical distinct gap pairs.  Both roots have the same repair-size
histogram:

| repair-set sizes | centre triples per root |
|---|---:|
| `(4,4,4)` | 35 |
| `(6,4,4)` | 42 |
| `(6,6,4)` | 7 |

Across all 84 unordered centre triples of either root, the exact relaxed
pair partition is

| number of closure failures whose repair set is hit | gap pairs |
|---:|---:|
| 0 | 6,923,456,484 |
| 1 | 14,382,312 |
| 2 | 4,956 |
| 3 | **0** |
| total | 6,937,843,752 |

Pairs that split a source flat are retained in these totals, so this is an
over-approximation of G0-feasible gap pairs.  Even the relaxed system has no
three-hit pair.  Ordered centre labels and arbitrary block partitions only
multiply already rejected descriptions; they cannot change the zero in the
three-hit row.

## 6. Audit and exact boundary

The byte-reproducible audit

`scratch/audit_k16_state2_buffered_star_two_gap_floor3_20260730.py`

has SHA-256
`0327b7b7e848ab9f445b4f1539c0c97dc2049100307f9352f4f62b55026e1f00`.

It authenticates both sources; rechecks moved-row uniqueness, collar/flat
disjointness, and unequal closure endpoints; binds and verifies the 36-edge
phase graph and actual-phase repair catalogue; reconstructs the core flats
for all 168 triples; proves all repair sets disjoint; and independently
partitions all canonical gap pairs by the number of repair sets hit.

Its outputs are

- `scratch/k16_state2_buffered_star_two_gap_floor3_20260730.audit.json`,
  SHA-256 `93c2c0f5915957fa3bbc4a531a2f567399ce77253b665531336625dd2acabb5c`,
  payload SHA-256
  `72f92e9fed54d15d91c01a6d3a9f7d8a62b771e2025efe340b8b5522a3acc534`;
- `scratch/k16_state2_buffered_star_two_gap_floor3_20260730.tsv`,
  SHA-256 `561185fe92ab2c432c3ec0a02675c38fe781e5ea7e846a7967324498f2660a2a`.

A structurally separate implementation rebuilds all 168 triples without
importing the frozen one-gap code, includes endpoint and adjacent-gap cases,
and independently obtains the same stabbing floor:

- `MATH_THEOREM_K16_STATE2_TWO_GAP_BUFFERED_STAR_STABBING_FLOOR3_20260730.md`,
  SHA-256 `f5771c745c67d9f3711cc9e1386bdc92dfe8e762bd3ab650e4b70a5fc39a3f22`;
- `scratch/k16_state2_two_gap_closure_port_lower3_20260730/audit_k16_state2_two_gap_closure_port_lower3_20260730.py`,
  SHA-256 `c62fa80de149dd680e5ed4474f824251b5176b764f8c9ff2175bdf6aedce76cd`;
- `scratch/k16_state2_two_gap_closure_port_lower3_20260730/independent.audit.json`,
  SHA-256 `34512210a1a32412b6a4079120ff4dbdae062b6f20fce46317cd4da7c2ec73bf`,
  payload SHA-256
  `0ffcf093c5cb884a36b8dadd14eee7065ef024db5b45642c8fbed99226b78582`;
- `scratch/k16_state2_two_gap_closure_port_lower3_20260730/two_gap_triple_catalogue.tsv`,
  SHA-256 `a7abb3523197a6b3ffccc502834b2dbd764d38d2631fa9afd1e244af328009cc`.

An adversarial six-port replay independently checks canonicalization, exact
flat rigidity, the apparent centre-617 counterphase, and all gap-membership
quotients:

- `scratch/k16_state2_buffered_star_graph_independent_20260730/TWO_GAP_FLOOR3_ADVERSARIAL_AUDIT.md`,
  SHA-256 `80b09d5008d52309ec9d35122cf6d885002820b098b9aefeb5d5be5b85b0a4a2`;
- `scratch/k16_state2_buffered_star_graph_independent_20260730/audit_two_gap_floor3.py`,
  SHA-256 `6fb18f51ef89c284633d4f578ff8edd5bbc867f5cac0e32de83d40e30619515a`;
- `scratch/k16_state2_buffered_star_graph_independent_20260730/two_gap_floor3.audit.json`,
  SHA-256 `326944becd0ed18e2cbf095f848714c0014870cc2039e9aa60c91d703ec5f595`,
  payload SHA-256
  `326b0732576a1d5b6ba76eb577941742a5fba85e89734a4ef6dad4c0fd9d7f97`.

No H100 computation or solver is used: the exact port prefilter empties the
two-gap carrier face before physical block enumeration.

This is only a source-relative obstruction for unchanged radius-three
collars, a source-ordered residual core, and at most two insertion gaps.  It
does not cover changed values, directed donor transfer, moved core segments,
wider atoms, other sources, or unrestricted K16.  The K16 bracket remains

\[
 12873\le\nu(16)\le12874.
\]
