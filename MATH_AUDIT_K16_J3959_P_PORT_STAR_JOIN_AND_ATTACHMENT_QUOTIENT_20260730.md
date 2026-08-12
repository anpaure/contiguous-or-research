# `j=3959` alternative `2665`/star join: exact boundary quotient and loss-charged Hall audit

Date: 2026-07-30

Status: **PASS exact local audit; all five named upper services; 57,216
loss-robust nine-shore survivors; global embedding, arbitrary-upper replay
and full lower Hall remain open**.

This note independently audits the frozen `j=3959` local-collar catalogue.
It is source-relative to the authenticated rank-eight chronology with SHA256
`edc3a377...`.  It makes no unrestricted K16 claim.

## 1. The boundary cascade is `130 -> 30 -> 15 -> 3`

Let `P=2665`, `Q=8000` and let the seven star targets be

```text
0665,066d,0675,06e5,0765,1665,8665.
```

The frozen chronology contains nine rank-eight masks `P+x`.  Its thirteen
oriented left ports and thirteen oriented right ports give exactly 130
occurrence-disjoint minimal nonflat `P` joins; 60 avoid all six old star
halos.

Requiring exact depth-two reconstruction of all six rows of the joined port,
using the native two-row right continuation, leaves 30 joins.  Requiring two
distinct proper-prefix cells, one for `P` and one for a star target, leaves
15.  Finally, coupling the port to the service-block suffix

```text
4a79,4e39,4d39
```

and requiring exact reconstruction of the terminal row `4d39` leaves exactly
three.  All three have the forced left half

```text
source 3753,3752,3751: 0779,2771,2765
```

and the following right halves and native buffers:

| branch | right triple | native buffer | old private cell touched |
|---:|:---|:---|:---|
| 0 | `6665,46e5,4ec5` | `5e85,5c95` | none |
| 1 | `26e5,06f5,42f5` | `60f5,70f4` | `06e5` |
| 2 | `a665,c665,c6c5` | `ce85,dc85` | `8665` |

Thus the three hard-coded right branches in the production catalogue are
complete, but only after the terminal-`4d39` equation is included.  A
port-only audit sees twelve additional `P`/star joins which cannot follow
that service suffix.

## 2. Necessary-and-sufficient depth-two attachment law

For one coordinate, the depth-two maximal envelope at position `p` is the
AND of the three rows ending at `p`.  A fixed row containing the coordinate
is reconstructed exactly if and only if its containing 1-run has length at
least three.

Consequently, for either end of a fixed exact collar, let `r` be the length
of a boundary 1-run:

```text
r >= 3: no exterior bit is required,
r = 2 : the near exterior row must contain the bit,
r = 1 : both the near and far exterior rows must contain the bit.
```

Taking these requirements coordinatewise gives four masks

```text
(left far, left near, right near, right far).                 (2.1)
```

Containment of the four masks in the four exterior rows is necessary and
sufficient for reconstruction of every fixed collar row.  This is a literal
run proof, not a solver condition.

Across all 57,396 production collars there are exactly 124 incoming
`(far,near)` states and three outgoing `(near,far)` states:

```text
(1010,0010), (3000,1000), (1800,1000).
```

All `124*3=372` products occur.  The frozen attachment TSV records the exact
multiplicity of every state.

## 3. Independent replay of the 57,396 local collars

The audit reconstructs rather than imports the envelope and candidate-cell
logic.  For every catalogue row it verifies:

1. all nineteen source occurrences are distinct and their literal values
   agree with the frozen chronology;
2. the service block belongs to the authenticated 2,250-member depth-three
   projection;
3. every row having complete two-row context reconstructs exactly at depth
   two;
4. only proper-prefix lengths one and two are used;
5. the block literally supplies `4e79,ca79,ea79,eb79`;
6. the consecutive collar rows `4d39,0779,2771` have OR `6f79`, so every
   collar supplies all five named upper services; and
7. the source occurrences `2a79@913`, `6a39@4513`, `4f19@1633`, whose OR is
   `6f79`, are untouched.

The reserved source triple is therefore redundant for the five named local
identities.  Their presence does not prove arbitrary-upper completeness in a
materialized chronology.

## 4. Charging destroyed old Hall cells

The simple three-role test assumes all six old star cells survive.  Physical
source relocation need not preserve that assumption.  The audit therefore
charges as unavailable every old Hall vertex whose depth-three source halo
intersects one of the nineteen selected occurrences, adds all literal new
collar incidences, and recomputes the matching on the canonical nine-target
shore.  This is a conservative lossless-splice test: it does not credit any
new cell which a future source-return braid might create at an opened gap.

The exact histogram is

```text
matching number 9 (loss-robust):       57,216
matching number 8 (return-dependent):     180
```

Each of the three right branches contributes `19,072` passes and 60 failures,
and every one of the 2,250 service blocks occurs in the passing set of every
branch.

All 180 failures have the single predecessor occurrence sequence

```text
273,272,271,270,269.
```

Charging that deletion destroys the old `0765` private shore cell.  After
`P` and `Q` are paid, the collar exposes only one net new star vertex, leaving
matching number eight.  The reverse predecessor `265,266,267,268,269` also
touches the same old halo but creates an additional literal `0765` cell and
therefore passes.  This explains why a halo-intersection test alone would
incorrectly discard 180 further valid local collars.

The matching-eight rows are not a physical no-go.  A materialized
source-return braid could reconstruct the touched old cell or create another
replacement.  They are precisely the rows not certified by a lossless local
splice.

## 5. Exact remaining gate

The 57,216 loss-robust rows are local, not physical compiler assignments.  The TSV
does not specify how the nineteen removed occurrences are returned to their
source gaps, where the collar is placed relative to the three phase drops,
or how its source gaps are repaired.  Without a materialized
occurrence-conserving variable-depth chronology, arbitrary-upper replay and a
full 26,332-target lower
matching cannot be replayed: new collar cells may have outside owners and
source-gap changes may alter cells far beyond the canonical shore.

Therefore the sharp conclusion is:

```text
three exact endpoint-trace branches,
372 exact exterior attachment states,
five named upper services in every local collar,
57,216 loss-robust local Hall survivors,
180 additional source-return-dependent rows,
full physical arbitrary-upper/lower-Hall embedding still open.
```

## Frozen artifacts

```text
scratch/audit_k16_j3959_p_port_star_join_semantics_20260730.py
scratch/k16_j3959_p_port_star_join_semantics_20260730.audit.json
scratch/k16_j3959_p_port_star_endpoint_quotient_20260730.tsv
scratch/k16_j3959_p_port_star_attachment_states_20260730.tsv
```
