# Audit: K17 `h=1` full-q1 residence-2018 joint provider and terminal interface

**Date:** 2026-08-02  
**Status:** positive full-q1 provider/forest/residual scaffold; negative
residence, deeper-upper, source, and compiler control.  No word is claimed.

## 1. Authenticated carrier

The active incidence-only factor is

```text
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
  checkpoint_fullq1_escape_res2018/model
SHA-256 c8f961413aeea43cbad5036e801c08f854f84889eaef11c281aa83bea46c057d
```

All heavy replay ran with `-O3` C++ on H100 CPU in the isolated root

```text
/home/amodo/or15/work/ad_v5r_h1_open22_019fc04bf4d7_20260802
```

The predecessor residence-2169 checkpoint remains frozen as a monotonic
control.  It is not the active interface.

## 2. Base and immediate-upper replay

Deterministic `p` materialization gives a complete 1,093,878-variable base
assignment.  Independent DIMACS replay obtains

```text
variables = 1,093,878
clauses   = 7,163,170
literals  = 22,610,292
status    = PASS
```

The independent opening verifier also replays all 16,261 cumulative guards,
exact degrees, the protected `M-B` and `510-B` incidences, forced `D-B=false`,
one augmented component, and two ordinary owner paths.  Both licensed
openings and both cyclic chronologies have zero immediate rank-ten holes.
All 19,448 immediate uppers are supplied by selected ordinary `p` rows; no
exceptional `D` occurrence is needed as a provider.

## 3. Exact joint extension certificate

The deterministic materializer chooses the lowest selected ordinary
provider for each rank-ten upper and fills every canonical Sinz auxiliary.
For orientation 0 the complete certificate has SHA-256

```text
9c996b0c0d21bd3f6760501215d0a18345263137f218ceeca4425a206a0cb7ff
```

The standalone global-oracle verifier replays:

```text
total variables                         2,873,695
extension clauses                       6,112,317
extension literals                     16,537,210
marked providers                           19,448
marked ordinary providers                  19,448
marked D providers                              0
primary forest components                   4,862
ordinary primary forest components          4,862
residual p-minus-z edges                     4,860
residual contracted graphic rank             4,860
residual contracted components                   2
all extension clauses satisfied               true
```

Thus this factor is a positive full-q1 provider/forest/residual scaffold.
This certificate does not waive any literal or compiler precondition.

## 4. Terminal adapter hard stop

The independent literal replay and the adapter agree exactly:

| orientation | short runs `(length 1,length 2)` | total | holes ranks 10--17 |
|---:|---:|---:|---:|
| 0 | `(1277,741)` | 2018 | `(0,1518,278,4,0,0,0,0)` |
| 1 | `(1276,742)` | 2018 | `(0,1518,278,4,0,0,0,0)` |

The adapter terminates with

```text
LITERAL_OUTER_NOT_READY q1_holes=0,0 residence=2018,2018
                        upper_total=1800,1800 word=0
```

No source chronology, lower Hall--DM instance, common-cap CNF, compiler
output, or word is emitted.  The terminal interface consists only of the
two owner chronologies, two `q` paths, per-upper interval-provider tables,
and the fail-closed audit.

## 5. Smallest remaining literal coupling

The active passive bank is

```text
escape_s2_quench.passive.cuts.DO_NOT_ADD.cnfpart
SHA-256 9fdbbe1c1303a8823f47b824de0471f4920ff623cdf71f52ccd592392b31b650
```

Its canonical minimum residence obstruction is row 3.  The selected
ordinary edge is

```text
p242272 = (lower 5479; owners 5495,5991), model literal +242272.
```

In both orientations it is the coordinate-0 length-one run at
`q[5109]=5479`, bounded by `q[5108]=5990` and `q[5110]=5494`; both bounding
roots omit coordinate 0.  The surrounding owners are
`22374,5991,5495,5622`.

A concrete currently-false crossing literal in the same cut is

```text
p220745 = (lower 1399; owners 1527,5495), model literal -220745.
```

Owner 1527 currently retains the coordinate-0 edges `p218919` and
`p220483`.  Selecting `p220745` inside a balanced closure that retains either
would enlarge the deficient component to at least four owners.  This is the
smallest one-literal CEGAR coupling interface, not a legal standalone toggle:
root/owner degrees, the 16,261 guards, q1, and connectivity still require a
complete alternating-circuit closure.

## 6. Authenticated depth-three owner payload

The static lower payload is the explicit table

```text
/home/amodo/or15/work/root_k17_exact_depth3_owner_payload_table_20260802/
  k17_depth3_owner_payload.tsv
SHA-256 029d3be53e13186e7be4c5bd8b89de9d3610be05c3af15f8c9024e7fbf3396c1
```

It is the constructive payload attached to
`MATH_THEOREM_K17_THREE_LEVEL_NORMAL_CHAINIZATION_20260802.md`, whose
current SHA-256 is
`1f285da227549171997362454cf5039ae690cc3f8af5f82033cc2406e2e8d9a4`.
A separately written table replay checks:

```text
rows = distinct rank-eight roots = distinct rank-nine owners = 24,310
targets of ranks one through eight, exactly once             = 65,535
chain lengths (one,two,three)                    = (1748,3899,18663)
selected factor incidences                                    = 48,620
fixed phase matching                                          = 24,310
```

Every row is a strict chain of at most three lower targets ending at its
immutable rank-eight root.  Its fixed rank-nine owner is joined to that root
by a selected incidence in the residence-2018 factor.  This closes static
lower-target allocation only.

The exceptional phase rows are `M=383 -> 511` and `D=255 -> 33023`.  The
fixed `D` phase occurrence is the orientation-0 closing occurrence and the
orientation-1 internal occurrence; this opening label does not change the
static predecessor graph.

## 7. Exact binding to the joint primary and its complement

The compatibility auditor authenticates the full `h1` map, the complete
base assignment, the orientation-0 joint certificate, and the payload table
before reconstructing every selected incidence.  The table rows split as

| root role | rows |
|---|---:|
| marked primary `z` root | 19,448 |
| residual ordinary `p-z` root | 4,860 |
| exceptional `M,D` roots | 2 |

For every ordinary row, the table owner is exactly one endpoint of the
selected `p`; the other endpoint is the ordinary rank-ten support
occurrence.  The roles may overlap at one root: carrying its lower chain
does not require the row to lie outside the marked primary forest.

The whole selected factor therefore carries the table statically and has an
independent perfect selected-incidence phase of size 24,310.  In contrast,
the strict primary complement `p-z` cannot carry the root-indexed table:

```text
available residual roots                         4,860
missing immutable root anchors                  19,450
actual cells on residual rows                   12,655 / 65,535
actual non-top cells on residual rows            7,795 / 41,225
maximum three cells per residual root           14,580
maximum two non-top cells per residual root      9,720
```

Adding the exceptional root indices gives only 4,862 anchors and still
misses 19,448.  Thus imposing `payload_root <= 1-used_primary_root` would be
an invalid compiler restriction.  The correct interface permits the lower
payload and the rank-ten primary role to share a root.

The topology side remains positive and unchanged: the primary forest has
4,862 components, the ordinary residual has rank 4,860 and two contracted
components, and one licensed internal `D` occurrence joins them.  The
table's `D` phase incidence and the topological `D` occurrence are separate
roles; their coexistence is static, not a serialization proof.

## 8. Exact static-chain provider menu and Hall stop

For a row `C1 < ... < CL`, `L <= 3`, the auditor enumerates every placement
of its `L` cumulative sets into three ordered thresholds.  This gives

```text
3*1748 + 3*3899 + 18663 = 35,604
```

weak embedded states.  Write the disjoint blocks of one state as
`(A1,A2,A3)`.  A formal fixed-owner predecessor arc from tail state `j` to
head state `i` is emitted exactly when

```text
(A_j2,A_j3) = (A_i1,A_i2)
root_i union A_j1 = owner_i.
```

The resulting exhaustive candidate bank has:

```text
formal variant arcs                                      6,128
variant states with zero head degree                    34,160
variant states with zero tail degree                    33,876
chain rows with zero head degree                        22,866
chain rows with zero tail degree                        22,582
maximum matching in the union-over-embeddings graph      1,425 / 24,310
formal chain matching deficiency                        22,885
right-aligned arcs / matching                                 1; 1 / 24,310
all-four-letters-nonempty arcs / matching                     1; 1 / 24,310
```

The chain graph deliberately forgets which embedding a row uses on its
incoming and outgoing sides.  It is therefore a relaxation of joint state
selection.  Its Hall failure is decisive: the frozen table and owner phase
have no one-predecessor-per-row literal balance even after empty-block weak
placements are allowed.  Short rows are not legal four-nonempty-letter
rotors without an independently certified padding or hinge realization.

The exact next source interface is consequently an enriched
occurrence-labelled menu which adds at least 22,885 independent matching
links before the relaxed fixed-owner graph can be perfect; the present
strict nonempty menu has deficiency 24,309.  Such links must be realized by
controlled padding, hinge, seam, or alternating-circuit states and replayed
against owner phase, topology, guards, q1, and residence.  Merely permuting
the canonical increments cannot pass this gate.

The primary audit has SHA-256
`58e5ed0f538b63e69303148802ae307d2f77eb09d73f3681e2f9acf1b07d791b`.
It publishes every row binding, all 35,604 states, all 6,128 arcs, and the
strict-complement obstruction.  No globally consistent embedding
permutation is asserted.

A structurally independent implementation reconstructs the candidate graph
from only the public table schema and arc definition.  It compares all
35,604 emitted variant records and the complete 6,128-arc set, including
metadata, with exact order-independent equality.  Its canonical alternating
Hall shore in the collapsed chain graph is

```text
|S_left| = 23,958
|N(S)|   =  1,073
defect   = 22,885.
```

For the right-aligned and nonempty graphs it emits shores of size 24,309
with empty neighbourhood.  Their sole surviving arc is chain
`1783 -> 2623`, variants `2015 -> 2961`, with four-letter trace
`(512,8192,2405,4096)`.  The independent source, audit, and explicit
shore have SHA-256 values

```text
3632824aa0440bfcadf9727d4bcc1c8b0dbdf589fa131bd7a55baf357164821c
1dbad23bd72184e2f8f630d164798f75a9bd873f1e9f7d4dceab914d61d722a7
f30b628cdc4269e568aec4a46ecae375986dc6ed6043eae97fe02b5f082cca8d
```

## 9. Terminal Benders/source interface

The exact terminal classification is now

```text
STATIC_PAYLOAD_PHASE_ATTACHED                     true
STRICT_PRIMARY_COMPLEMENT_CARRIES_PAYLOAD         false
WEAK_FIXED_OWNER_SOURCE_BALANCE                   false
LITERAL_NONEMPTY_SOURCE_BALANCE                   false
RESIDENCE_ZERO                                    false
DEEPER_UPPER_COMPLETE                             false
COMPILER_ELIGIBLE                                 false
WORD                                               0
```

The static predecessor graph is the same under both licensed openings, so
its Hall obstruction can be instantiated under either opening guard.  It is
not an unguarded incidence cut and must not be added to the factor CNF as if
the present weak menu were complete: an enriched literal-state menu may add
new arcs.  Independently, the physical factor still has residence 2,018 and
rank-11--13 holes `(1518,278,4)` in both openings.  Either failure alone is a
hard stop before source, lower Hall--DM, common-cap, or compiler work.

## 10. Frozen packages and scope

The complete local package is

```text
scratch/ad_k17_h1_res2018_joint_scaffold_20260802/
```

The depth-three payload/provider interface is frozen separately at

```text
scratch/ad_k17_h1_res2018_depth3_payload_provider_interface_20260802/
```

The end-to-end replay classification is

```text
PASS_Q1_ZERO_JOINT_CERTIFIED_OUTER_NOT_READY
```

Proved for this factor: complete base assignment and formula, cumulative
guards, exact connected `h=1` topology, full opened q1 in both orientations,
one complete orientation-0 provider/primary-forest/residual certificate,
the exact static lower payload and selected phase, the impossibility of
placing that root-indexed payload solely on `p-z`, exhaustive weak
fixed-owner predecessor candidates and their relaxed Hall failure, literal
residence and rank-10--17 replay, and fail-closed adapter behavior.

Not proved: positive residence, ranks 11--13, a source antecedent, lower
Hall--DM, common-cap SAT, compiler publication, exhaustive word replay, a
K17 universal word, `nu(17)=24313`, or an all-k theorem.
