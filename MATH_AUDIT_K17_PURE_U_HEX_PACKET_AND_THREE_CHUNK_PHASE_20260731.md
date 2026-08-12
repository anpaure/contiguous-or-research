# A pure-`U` alternating hex gives an exact three-chunk phase switch in the frozen `K17` carrier

Date: 2026-07-31  
Status: exact cycle-only audit and reusable local packet lemma; no residence,
common-cap compiler, or all-dimension recurrence is claimed

## 0. Result

Start with the authenticated literal carrier

```text
scratch/k17_parent_induced_macro_port_cycle_20260731.cycle
SHA-256 39cc3abe6a8991dc101a585123989deab863030060c00d3e0a2a60cd73252de6
```

There is a minimal alternating packet involving only six pure old-coordinate
rank-nine `U` owners.  Toggling its three selected and three unselected
incidences:

1. leaves every macro incidence and physical macro path fixed;
2. reconnects the old Hamilton cycle as three chunks, with exactly one chunk
   reversed;
3. again gives all `24310` rank-nine owners and all `24310` rank-eight edge
   colours exactly once;
4. deletes three short coordinate runs and creates none;
5. adds two previously missing lower-`q2` targets and two previously missing
   rank-ten upper-`q2` targets, without losing an old target in either deck;
6. adds one rank-eleven upper target and leaves the target sets at ranks
   twelve through seventeen unchanged.

The resulting literal cycle is

```text
scratch/k17_pure_u_hex_packet_20260731.cycle
SHA-256 42da8471dffb39d56c3aa1faa6d3572d1638e98f799dbfcc68dcfeb83423736d
```

This is a rigorous local installation mechanism, not evidence from a
one-off heuristic.  The incidence toggle and its three-chunk chronology are
dimension-free; only the displayed packet and census are specific to this
carrier.

## 1. Port objects recovered from the literal cycle

Let `x=2^15` and `y=2^16`.  Every owner in the cycle is of one of four
types:

```text
U : old rank 9
X : old rank 8 plus x
Y : old rank 8 plus y
A : old rank 7 plus x+y
```

Without reading the parent factor or flow certificate, split the literal
cycle into singleton `U` objects and maximal sector words

```text
X+ A+ Y+    or    Y+ A+ X+.
```

An `X/Y` shore change separates consecutive macros.  This cycle-only parse
gives exactly

```text
5005 U objects + 1430 macro objects = 6435 port objects,
```

and sector counts

```text
U^5005 X^6435 Y^6435 A^6435.
```

The intersection across each object boundary is an old rank-eight port
colour.  The `6435` boundary colours are distinct and equal
`binom([15],8)`.  Thus the parsed objects and colours form the authenticated
port Hamilton cycle directly from the final witness.

## 2. The reusable local packet lemma

Let `B` be the incidence graph between old rank-nine `U` owners and their
old rank-eight facets `T`.  Fix a degree-exact selected subgraph.  Suppose
there are distinct owners `U0,U1,U2` and colours `T01,T12,T20` such that

```text
T20--U0, T01--U1, T12--U2 are selected,
U0--T01, U1--T12, U2--T20 are unselected.
```

These six incidences form the alternating hexagon

```text
U0--T01--U1--T12--U2--T20--U0.
```

### Lemma 2.1 (minimal alternating port packet)

Toggle selected and unselected incidences around this hexagon.  Then every
`U` and every `T` retains its degree.  If the resulting port two-factor is
connected, expanding the unchanged physical macros gives another literal
owner cycle with the same complete owner and immediate-lower-colour decks.

Moreover, this is the smallest possible nontrivial incidence packet: the
`U--T` layer-incidence graph contains no four-cycle.

#### Proof

At each of the six hexagon vertices the toggle deletes one incidence and
adds one incidence, so every degree is unchanged.  Macro incidences are not
among the toggled edges.  Hence all port colours remain vertices of degree
two, all `U` owners remain once, and every fixed macro retains its two ports
and its complete internal owner/colour path.  Connectivity makes the new
two-factor one cycle; macro expansion therefore preserves the two complete
Boolean layers.

For minimality, two distinct rank-nine owners contain at most one common
rank-eight facet.  Indeed, two distinct rank-eight common facets would have
rank-nine union, and that union would equal both owners.  Hence the
incidence graph has no \(K_{2,2}\) and therefore no four-cycle.  An alternating
hexagon is the first possible packet.  \(\square\)

The exact cycle has `7225` such directed alternating hexagons after quotient
by cyclic rotation.  Exactly `3625` toggles leave one connected port cycle.
These are exhaustive finite counts, not samples.

## 3. The exact pure-`U` hexagon

Use

```text
U0 = 0x0177a
U1 = 0x01f78
U2 = 0x01f72

T01 = 0x01778
T12 = 0x01f70
T20 = 0x01772.
```

Thus the alternating cycle is

```text
0x0177a -- 0x01778 -- 0x01f78 -- 0x01f70
          -- 0x01f72 -- 0x01772 -- 0x0177a.
```

The selected incidences removed by the toggle are

```text
0x0177a--0x01772,
0x01f78--0x01778,
0x01f72--0x01f70,
```

and the inserted incidences are

```text
0x0177a--0x01778,
0x01f78--0x01f70,
0x01f72--0x01772.
```

All three fixed objects on the other side of the affected colours are also
singleton `U` objects:

| port colour | removed packet owner | fixed owner | fixed object index |
|---|---|---|---:|
| `0x01778` | `0x01f78` | `0x05778` | 2858 |
| `0x01f70` | `0x01f72` | `0x01f74` | 1556 |
| `0x01772` | `0x0177a` | `0x01776` | 4845 |

This is the exact fixed-macro obstruction check: no affected incidence has a
macro as its fixed partner, no macro port pair changes, and no macro path is
rebuilt.  The global traversal does reverse some already valid macros because
one whole phase chunk reverses.  The traversal profile changes from

```text
751 X-to-Y + 679 Y-to-X
```

to

```text
723 X-to-Y + 707 Y-to-X.
```

Consequently the packet is valid for the authenticated unoriented macro
carrier.  It does not assert the optional globally coherent macro-orientation
strengthening.

## 4. Exact three-chunk chronology

All indices below are zero-based; edge `i` lies between owner `i` and owner
`i+1` cyclically.  The removed literal seams are

| old edge | old owner pair | colour |
|---:|---|---|
| 6506 | `0x01f74 -- 0x01f72` | `0x01f70` |
| 11714 | `0x05778 -- 0x01f78` | `0x01778` |
| 19209 | `0x0177a -- 0x01776` | `0x01772` |

They cut the base cycle into

```text
A = base[6507:11715],       length  5208,
B = base[11715:19210],      length  7495,
C = base[19210:] + base[:6507], length 11607.
```

Their exact port-object censuses are

| chunk | objects `U+M` | sectors `U,X,A,Y` | base macro directions `F+R` |
|---|---:|---:|---:|
| A | `992+310` | `992,1577,1373,1266` | `169+141` |
| B | `1523+463` | `1523,1797,2017,2158` | `249+214` |
| C | `2490+657` | `2490,3061,3045,3011` | `333+324` |

The switched cyclic chronology is exactly

```text
C B reverse(A).
```

With the authenticated linear origin retained, the candidate sequence is
the literal slice identity

```text
base[0:6507]
+ base[11715:19210]
+ reverse(base[6507:11715])
+ base[19210:24310].
```

The new seams occur at

| new edge | new owner pair | preserved colour |
|---:|---|---|
| 6506 | `0x01f74 -- 0x01f78` | `0x01f70` |
| 14001 | `0x0177a -- 0x05778` | `0x01778` |
| 19209 | `0x01f72 -- 0x01776` | `0x01772` |

This proves both connectivity and the exact phase action without relying on
a graph drawing or solver metadata.

## 5. Literal palette and residence deltas

The candidate independently replays as

```text
24310 distinct rank-nine owners = binom([17],9),
24310 distinct rank-eight intersections = binom([17],8).
```

### Lower decks

At lower `q2`, the distinct rank-seven count changes as

```text
17825 -> 17827,     missing 1623 -> 1621.
```

The two new targets are

```text
0x01378, 0x01d70,
```

and no old target is lost.

At lower `q3`, the distinct rank-six count remains `11363`.  The target
`0x01172` is replaced by `0x01570`.  The width-four occurrence profile
improves from

```text
rank 6^23247 rank 7^1063
```

to

```text
rank 6^23249 rank 7^1061.
```

### Upper decks

At rank ten, the distinct count changes as

```text
17557 -> 17559,     missing 1891 -> 1889.
```

The two new targets are

```text
0x01f7c, 0x0577a,
```

and no old target is lost.  Rank eleven gains `0x01f7e`, changing
`11466 -> 11467`.  The target sets at ranks twelve through seventeen are
identical before and after the switch.  The maximum first-full-set width
remains `283`.

### Short positive-coordinate runs

The short-run profile changes as

```text
length 2: 1063 -> 1061,
length 3: 1829 -> 1828.
```

Exactly three runs disappear:

```text
bit 3,  length 2: 0x1137a 0x0177a
bit 4,  length 3: 0x05b74 0x01f74 0x01f72
bit 11, length 2: 0x01f78 0x01d7a
```

No short run is created.  This is the requested simultaneous local effect:
one packet repairs lower `q2`, upper `q2`, and residence defects while
leaving the frozen owner/`q1` carrier intact.

## 6. Reproducibility and scope

Run

```text
python3 scratch/audit_k17_pure_u_hex_packet_20260731.py
```

The cycle-only audit script has SHA-256

```text
8ce2063ebf7514afda0ba740dbcedd31aec2d8042747fa06de498ffdb3221bde
```

and writes

```text
scratch/k17_pure_u_hex_packet_20260731.cycle
scratch/k17_pure_u_hex_packet_20260731.audit.json
```

The JSON SHA-256 is

```text
6b38cc956c128063498c3947c0273e40df0d2ec09c47c4d52a2c43587f75468d
```

The script reads no parent component, flow state, or construction metadata.
It reconstructs the port objects from sector tags in the literal base cycle,
enumerates all alternating hexagons, performs the exact toggle in the port
graph, independently constructs the same candidate from the displayed slice
formula, and compares the full Boolean layers and all reported decks.

This packet removes only three of the `2892` short runs and two of the `1623`
lower-`q2` holes.  It therefore proves a reusable local move and one exact
strictly improving installation, not completion of residence, all lower
shadows, or the common compiler.
