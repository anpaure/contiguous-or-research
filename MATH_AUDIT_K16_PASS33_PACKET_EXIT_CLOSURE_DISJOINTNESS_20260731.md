# K16 pass33 packet/positive-cut exit closure audit

Date: 2026-07-31  
Status: **PASS_SCOPED_DISJOINTNESS.** The complete frozen pass33 packet atlas
does not realize any of the three `4e70` positive-cut exits. This is not an
unrestricted Hall or K16 no-go.

## 1. Frozen lineage

The parent is the exact/all-upper Hall-24 pass33 carrier

```text
scratch/threadD_k16_exact229_braid24_support3_shell_20260730/pass_33.targets
SHA-256 2dbb84bc6467047d99019e58b6a33072cbca8f0bc6e62c451954603611fcf2ec
```

The packet lane is the authenticated depth-seven occurrence-cycle table

```text
scratch/k16_pass33_compatibility_cycles_20260731/depth7_match_fast.tsv
SHA-256 ca25a947847baf3a8ecab733e68cfcae3557143163d6c9f6b1f867c64532c57b
```

with frozen matching

```text
scratch/k16_pass33_compatibility_cycles_20260731/pass33.matching.tsv
SHA-256 edce435b180a85f79874bf5d1be92cd152d763f31177347a221a3b9c4d4767e6
```

The newest local matching audit used here is

```text
scratch/threadA_k16_pass33_matching_packet_closure_20260731.audit.json
SHA-256 02a1f88fe856fca5434eb979c76a3ee3aaa09fd56c4dcd297c6332edb8ff92be
```

and the three positive-cut ports are independently frozen in

```text
scratch/k16_exact229_nested_four_third_overlap_gate_20260730.audit.json
SHA-256 59fdeccb1b6225d10f7b41dc88efebf074e04921f11dd3b8d2cce30b77c3fc2d
```

No search was launched for this audit. The complete finite work below takes
about three seconds locally.

## 2. Exact dependency closures

For a maximal-envelope position `p`, let `I(p)` be its incoming row set. For
a cell `J`, let `R(J)` be the union of `I(p)` over `p in J`. The exact
two-step row dependency used by the packet engine is

\[
 D(J)=R(J)\mathbin\cup
 \bigcup_{r\in R(J)}\ \bigcup_{p=r}^{r+d(r)} I(p).
\]

It contains every row value needed both to form the cell profile and to
replay the affected carrier rows. Direct reconstruction gives

| exit | cell | paired targets that must survive | exact `D(J)` |
|---|---|---|---|
| A | `J19536=[6607,6609)` | `{4e70,ce40}` | `[6603,6610]` (8 rows) |
| B | `J19538=[6608,6610)` | `{4e70,ce30}` | `[6604,6611]` (8 rows) |
| C | `J31749=[12714,12715)` | `{4e70,4a70}` | `[12710,12716]` (7 rows) |

The paired target is essential only to the displayed frozen augmenting path:
the cell is already used by that stored matching.  A later full-rematch audit
proves that these old-mate incidences are noncore, so final acceptance must
use the forced rematch criterion rather than require the old mate itself.

## 3. Exact intersection theorem for the packet atlas

Each packet table row is an occurrence-labelled permutation cycle. Its
source positions and destination positions are the same set, hence that set
is exactly the physical edit support. Parsing all 2,732 authenticated rows
against the closures above gives

```text
support disjoint from A,B,C       2658
support meets only C                74
support meets A                      0
support meets B                      0
support meets multiple closures      0
```

Every one of the 74 C contacts meets `D(C)` at exactly one physical row,
`12713`. None touches `12712`. Their values transported into row `12713` are

```text
4679:35, 8e71:14, c279:9, ca59:8,
c659:4, 0e79:3, 8e59:1.
```

This proves disjointness from all three exits:

* A and B are unchanged because no packet support meets either dependency
  closure.
* At C the envelope is the intersection of rows `12712,12713,12714`.
  Initially rows `12712=ca71` and `12713=4a79` both lack bit `0400`.
  Changing row `12713` alone cannot introduce `0400` into the intersection,
  so none of the 74 contacts creates the `4e70` edge.

None of the 74 right-contact packets is all-upper; their minimum frozen
matching loss is 33. The only three all-upper packets are table rows
422/461/463. Their exact supports are disjoint from all three exit closures,
and their frozen matching losses are 44/43/44 respectively.

Consequently, composing an all-upper packet with only an abstract retained-
graph exit edge cannot certify Hall 23: one new edge raises matching by at
most one. This last sentence is intentionally narrow. A new interacting
kernel can change many incidences and must be fully rematched.

## 4. Smallest local occurrence gates

Before exactness or occurrence constraints, the missing-bit blockers are

| exit | envelope position | rows lacking required bit |
|---|---:|---|
| A, bit `0010` | 6607 | `{6605,6606}` |
| A, bit `0010` | 6608 | `{6606}` |
| B, bit `0040` | 6608 | `{6608}` |
| B, bit `0040` | 6609 | `{6608,6609}` |
| C, bit `0400` | 12714 | `{12712,12713}` |

Thus a one-row A installer is forced to edit row 6606, a one-row B installer
is forced to edit row 6608, and C must edit both 12712 and 12713.

Using exactly Lane A's occurrence-source conditions—distance greater than six
from the destination and from protected sites
`{6320,12869,12871,12720}`—gives the following complete direct census:

* A has 12,824 eligible source occurrences. Seventeen transported values are
  individually middle-exact at row 6606, but zero realizes both
  `4e70--J19536` and `ce40--J19536`.
* B has 12,824 eligible source occurrences. Twelve transported values are
  individually middle-exact at row 6608, but zero realizes both
  `4e70--J19538` and `ce30--J19538`.
* C's two forced rows must each receive a rank-eight superset of `4e70`. The
  complete safe occurrence list is

  ```text
  280:4e72, 913:6e70, 1000:4f70, 4172:4ef0,
  4349:4e74, 5332:5e70, 6607:ce70.
  ```

  All 42 ordered distinct source pairs were replayed at rows 12712/12713;
  zero is simultaneously locally exact and realizes both paired edges.

There is also no hidden closure-only rearrangement. Every nonidentity
permutation of the occurrences already present in a closure preserves the
fixed depth pattern, but none is middle-exact:

```text
A: 8!-1 = 40319 tested, exact 0
B: 8!-1 = 40319 tested, exact 0
C: 7!-1 =  5039 tested, exact 0
```

Therefore any genuine exit chronology must import at least one remote
occurrence.  The paired-old-mate subclass needs the local compensators stated
above, but that is not a lower bound for unrestricted rematching.

## 5. Paired-path templates and the rematch correction

The following 19 templates are the smallest family only under the historical
extra requirement that the old mate of the port cell survive.  They remain a
valid scoped paired-path family, but they are not the final rematch-aware
acceptance gate.

The smallest focused next family has only 19 local destination templates:

\[
\begin{aligned}
K_A(t)&=\{6606,t\},&t&\in D(A)\setminus\{6606\} &&(7\text{ templates}),\\
K_B(t)&=\{6608,t\},&t&\in D(B)\setminus\{6608\} &&(7\text{ templates}),\\
K_C(t)&=\{12712,12713,t\},&t&\in D(C)\setminus\{12712,12713\}
&&(5\text{ templates}).
\end{aligned}
\]

For each template, enumerate occurrence-labelled imports into the local
destinations, not marginal mask values. Retain a local root exactly when:

1. the fixed depth pattern and every affected middle row replay exactly;
2. the appropriate paired cell predicate holds;
3. every source occurrence is distinct and at least one lies outside the
   closure;
4. the unique protected upper witnesses `ce2e`, `8a5f`, and `ca5f`, and the
   independent `8000` path, are unchanged or explicitly rehosted.

Only after a local root survives should its displaced occurrence labels be
closed through the already-defined single-row compatibility relation. Remote
closure vertices may remain dependency-disjoint, but the old forced halo arc
`3846->4653` is not a root requirement and packet cycles with no local root
are never revisited. This makes the family structurally disjoint from Lane
A's broad halo-first packet enumeration.

The subsequent forced-basis audit gives the corrected smallest relaxed root:

```text
4e72@280 -> row6606
```

It is middle-exact, creates `4e70--J19536`, loses old mate
`ce40--J19536`, preserves the five-edge forced core and `8000`, and fully
rematches to26309.  It is not occurrence-integral and owes upper masks
`ce6a,ce6b`; its displaced value is `ce62`.  Thus the sharp next family is
the occurrence cycle closing this root, not the 19 paired-path templates.

Final acceptance is literal: occurrence bijection, all middle rows, all
65,535 upper masks, retained `8000`, and a fresh full Hall matching of at
least 26,309.  A stored old matched cell edge is not separately required.

## 6. Scope

The theorem is complete only for the frozen pass33 depth-seven packet table,
the three stated dependency closures, the paired-path minimal-import tests,
and closure-internal permutations.  The rematch-aware one-row replay is
recorded separately.  It does not exclude the exit-rooted occurrence cycle,
another Hall-24 parent, a changed flat schedule, or a nonzero-target DM exit.
No K16 word and no global lower bound is claimed.

## 7. Reproducer

```text
scratch/audit_k16_pass33_packet_exit_closure_overlap_20260731.py
scratch/k16_pass33_packet_exit_closure_overlap_20260731.audit.json
```

The exact script, JSON, and payload hashes are recorded after the final
replay in the handoff/index entry.
