# Adversarial audit: k=16 residence-motif / q1-palette coupling

Date: 2026-07-29

Verdict: **the palette-safe deletion model is infeasible by a two-edge,
solver-free certificate.**  The supplied 148-edge witness also checks exactly:
it hits all 226 old residence motifs and destroys 88 lower plus 92 upper q1
quotient rows.  The claim that 180 is the minimum number of destroyed rows,
with 148 the removal tie-break, is supported by the retained CP-SAT
`OPTIMAL` status and equal bound `180148`, but not by an independently
checkable proof log.  It must remain solver-transcript scope.

The replayable audit is
`scratch/audit_ad_k16_residence_palette_coupling_20260729.py`; its retained
output is
`scratch/ad_k16_residence_palette_coupling_20260729.audit.json`.

## 1. Source and carrier scope

Both deletion payloads name
`k16_qfactor_q1_topresident_hamilton_20260729.json` and pin SHA-256

```text
f76ab4e5c30c3269da87788c275777a3b40deea96f4fbf892cd5c6027280a7a5
```

That digest matches the top-resident source bytes exactly.  It does not match
the promoted lower-q1-two-hole Hamilton carrier.  The two selected quotient
edge sets are also materially different: each contains 858 orbits, their
intersection has size 783, and each has 75 private orbits.  Thus none of the
226/148/88/92/180 claims may be transferred to
`k16_connected_q1_lower2_hamilton_20260729.json`.

At the time of this audit the promoted comparator file has SHA-256
`16fc3739...`; retained earlier artifacts cite the relabelled byte version
`abde6319...`.  Its selected-edge set is unchanged.  This byte drift does not
affect the conclusion above because the deletion payloads pin the distinct
`f76ab4e...` source.

## 2. Motif completeness and compression

The audit independently materializes all 858 selected edge orbits over the
15 old-coordinate rotations.  It obtains one degree-two physical component
of length 12,870.  Direct cyclic-run enumeration gives:

| Physical short positive-run length | Count |
|---:|---:|
| 1 | 330 |
| 2 | 1,620 |
| 3 | 1,440 |
| **Total** | **3,390** |

There is no short positive run in the distinguished top coordinate.  For
each old-coordinate short run, the entering edge, internal edges, and exiting
edge form its forcing path.  Mapping those physical edges back to quotient
edge IDs and deduplicating produces exactly 226 motifs, with size histogram

```text
2: 22, 3: 108, 4: 96; total incidences: 752.
```

Every quotient motif occurs exactly 15 times among the 3,390 physical runs.
This proves that the compression is precisely the old-coordinate rotation
compression, rather than an accidental set deduplication.  The independently
reconstructed motif list agrees byte-for-byte after canonicalization with
`residence_motif_edge_sets`; its canonical SHA-256 is
`a0e83acf...`.

Keeping every edge of one motif keeps the corresponding local physical path,
and degree two then keeps that old short run.  Therefore every equivariant
rethread must delete at least one current quotient edge from every old motif.
This is only a necessary condition: additions can create new runs, and the
deletion model does not impose the repaired factor constraints.

The motifs are cyclic intervals along the 858-edge quotient cycle.  Cutting
at an uncovered cycle edge and applying earliest-finish greedy yields both
147 pairwise edge-disjoint motifs and a 147-edge transversal.  Hence the
unconstrained old-motif transversal number is solver-free and exactly 147.

## 3. Palette-provider constraints and solver-free infeasibility

The source covers all 764 lower and all 764 upper q1 quotient rows.  For a
current row with provider set `P`, palette-safe mode encodes

```text
sum(remove[e] for e in P) <= |P|-1,
```

which is exactly “retain at least one current provider.”  An edge is therefore
individually removable only when both its lower and upper current provider
multiplicities are at least two.  There are only 36 such selected edges, and
186 of the 226 motifs contain none.

One explicit obstruction suffices.  Sorted motif 1 is

```text
{1091, 1406}.
```

- Edge 1091 is the sole selected provider of upper row `(0,1915)`.
- Edge 1406 is the sole selected provider of upper row `(0,3005)`.
- Their shared lower row `(0,445)` has exactly the two providers
  `{1091,1406}`.

Hitting the motif removes 1091 or 1406, and either choice loses a currently
covered upper row.  Thus palette-safe motif hitting is infeasible without any
solver assumption.  The CP-SAT `INFEASIBLE` record is consistent but
unnecessary for this implication.

## 4. The 180/148 witness and the lexicographic model

In min-holes mode the Boolean row variable satisfies

```text
h[P] >= sum(remove[e] for e in P) - (|P|-1).
```

Because every `h[P]` has positive objective weight, it is zero unless all
current providers are removed and is forced to one when they are.  The
objective is

```text
1000 * (lower holes + upper holes) + removals.
```

There are only 858 removal variables, so `1000 > 858` makes this a valid
lexicographic objective: one fewer row hole dominates every possible change
in removal count.

Independent evaluation of the retained 148-edge set gives:

- all 226 motifs hit (214 once and 12 twice);
- 88 lower q1 quotient rows lost;
- 92 upper q1 quotient rows lost;
- objective `1000*(88+92)+148 = 180148`.

Of the 180 lost rows, 179 had one current provider.  The only nonsingleton
loss is lower row `(1,1611)`, whose two current providers are
`{21303,22078}`.  The output's equal best bound `180148.0` and status
`OPTIMAL` support the claimed primary optimum 180 and conditional removal
tie-break 148, but the JSON has no DRAT, branch certificate, dual, or other
independently replayable lower-bound proof.  I did not launch a heavy solve.

The field `minimum_removed_edges: 148` must be read conditionally.  It is the
minimum removal count among the reported minimum-hole solutions; the
unconstrained motif hitting minimum is 147.

## 5. Quotient rows are not literal colours

The counts 88, 92, and 180 are quotient palette rows/rotation orbits.  Direct
orbit expansion gives:

| Side | Missing quotient rows | Missing literal q1 colours |
|---|---:|---:|
| Lower | 88 | 1,320 |
| Upper | 92 | 1,370 |
| **Total** | **180** | **2,690** |

One missing upper row has rotation-orbit size five; the other 179 missing rows
have size 15.  Accordingly, “180 literal colours” would be false.  The exact
statement is “180 q1 quotient rows, representing 2,690 literal q1 colours.”

## 6. Hashes and provenance limitations

The `payload_sha256_before_hash` values in the palette-safe, min-holes,
147-edge, and interval-certificate JSON files all recompute exactly.  The
catalogue digest also recomputes as
`e5ffa02199834c476f45b314b2eacfbaa1866a74895cc0aa4e12744c8d157ff3`.

Those payloads do not embed a solver-script SHA, a motif-list SHA, or a solver
proof log.  During this audit the solver script acquired an optional
`--forbid-cross-removals` mode and now emits an extra
`forbid_cross_removals` field that is absent from the retained result JSONs.
The default-false mathematical model audited above is unchanged, but the
current script cannot byte-reproduce the old payloads.  The new audit JSON
therefore records current generator hashes and an independent canonical motif
hash; it does not claim historical byte-level generator provenance.

## 7. Exact implication for the search

What is proved is a coupling obstruction for deletion-only edits of the 858
current top-resident quotient edge orbits: no deletion set can hit all old
residence motifs while retaining a current provider of every current lower
and upper q1 row.

What is not proved is nonexistence of a resident, q1-complete Hamilton factor.
The model omits replacement edges and replacement palette providers, degree
two after edits, connectivity, voltage, and newly created residence motifs.
Therefore residence repair and q1 restoration must be treated as a joint
global rethread; the certificate does not rule such a rethread out.
