# Independent audit of the AD (k=16), radius-99 dynamic-top stage

Date: 2026-07-29  
Audited driver: `scratch/search_ad_k16_recenter_r99_scope_complete_20260729.py`  
Audited SHA-256: `be0aef35b977e7539620101ff284ae7ed490408d8bfded9ca333c2576ae1148f`

## Verdict

The dynamic-top formulation is exact on its stated loopless degree-two
scope.  The boundary/reach rows exclude exactly the nonmonochromatic top-1
and top-0 runs of lengths (1,2,3).  The literal CEGAR rows then exclude the
remaining short monochromatic physical components.  Every lazy row is a
valid edge-orbit nogood, so it cannot remove a top-biresident factor.

Consequently:

1. `TOP_BIRESIDENT_Q1_FACTOR` is a sound positive certificate after literal
   replay.
2. `INFEASIBLE_CP_SAT_TRANSCRIPT` in one locked branch is scoped only to that
   branch; global infeasibility requires both branches.
3. A round-limited `UNKNOWN`, `MAX_ROUNDS`, or retained
   `FEASIBLE_Q1_TOP_DEFECT` is not an impossibility certificate.

There are no mathematical defects in the top formulation.  There are two
provenance/durability caveats: `--hint-result` is not fully fail-closed, and
the atomic writer does not `fsync` the containing directory.

## 1. Exact local boundary theorem

### Theorem 1.1

Let (F) be a loopless degree-two factor in the physical lift of the
quotient catalogue.  Give each physical middle vertex its fixed top label
(z\in\{0,1\}).  Project the driver's boundary/reach system to (F):

\[
B_v=\sum_{e\ni v,\ e\text{ cross}}x_e,
\]

and, for every same-shore incidence (vu),

\[
R_{v,vu}\ge x_{vu}+B_u-1,
\qquad
B_v+\sum_{vu\text{ same}}R_{v,vu}\le1.
\]

Here (B,R,x) are Boolean.  This system is feasible if and only if every
nonmonochromatic cyclic (z)-run in (F) has length at least four.

### Proof

Every quotient vertex orbit is free under the old-coordinate rotation.  A
selected nonloop edge orbit therefore contributes exactly one physical
incidence at every phase of each endpoint orbit.  Thus the quotient cross
degree is the literal cross degree at every lifted phase.

Since (B_v) is Boolean, the first equality simultaneously says:

* cross degree two is impossible;
* (B_v=1) exactly when (v) has cross degree one.

A length-one run is exactly a vertex of cross degree two, so these and only
these length-one runs are excluded.

The reach variables are only lower-defined.  After existentially eliminating
them, the second pair of rows is precisely

\[
B_v+#\{u:vu\in F,\ z(u)=z(v),\ B_u=1\}\le1.
\]

A length-two run has two adjacent boundary vertices, so the row fails at
either endpoint.  A length-three run has a nonboundary middle vertex with
two boundary neighbours, so the row fails at the middle.  Conversely, if a
row fails, then either (B_v=1) and a same-shore neighbour is also a
boundary, giving a length-two run, or (B_v=0) and both same-shore
neighbours are boundaries, giving a length-three run.  This argument is
label-symmetric and therefore covers top-1 and top-0 runs simultaneously.
Together with the cross-degree-two case it proves the claim.  ∎

The local rows intentionally accept a monochromatic component: every one of
its boundary flags is zero.  Such a component is defective only when its
physical cycle length is at most three, and that is the exact residual case
handled by CEGAR.

## 2. Literal CEGAR theorem

### Theorem 2.1

Let (C=(v_0,e_0,v_1,e_1,\ldots)) be a physical cycle of a selected
equivariant degree-two factor.  Suppose (v_s,\ldots,v_{s+\ell-1}) is a
top-1 or top-0 run of length (1\le\ell\le3).  Define

\[
P=\{e_{s-1},e_s,\ldots,e_{s+\ell-1}\}
\]

as a set of quotient edge-orbit IDs, collapsing repetitions.  If the whole
cycle is monochromatic, take (P) to be all its edge-orbit IDs.  Then every
loopless degree-two factor selecting every orbit in (P) contains the same
literal short run.  Hence

\[
\sum_{e\in P}x_e\le |P|-1
\]

is valid for every top-biresident factor.

### Proof

Selecting an edge orbit selects every physical rotation of its representative
edge.  Thus selecting all orbits in (P) selects every displayed physical
edge, even if one orbit occurs more than once in the displayed segment.  At
each run vertex the two displayed incidences are selected.  Degree two then
saturates that vertex, so no other selected edge can alter the segment.  The
top label is a fixed vertex label, hence the same short run remains.  In the
monochromatic case all vertices of the short component are saturated by the
selected cycle edges.  ∎

The implementation uses exactly the entering edge, all internal edges, and
the leaving edge: `edge_ids[(run_start-1+offset) % length]` for
(0\le\text{offset}\le\ell).  It repeats the construction after complementing
the top bits, so zero-runs are not omitted.

### Corollary 2.2 (finite exact CEGAR)

Every defective incumbent contributes a fresh valid nogood.  Indeed, if all
of its current short-run orbit sets had already been added, that incumbent
would violate an existing row.  Therefore an unbounded-round run over the
finite factor space terminates with either a literal top-biresident factor or
branch-scoped infeasibility.  The driver's finite `--rounds` cap changes only
termination status, not soundness.

## 3. Independent solver-free replay

The audit script
`scratch/audit_ad_k16_r99_dynamic_top_stage_20260729.py` has SHA-256
`845529055d0e324623c901ced422c693ee99bbefa5075eacaaaf9580fd945f52`.
It performed the following checks without invoking CP-SAT:

* all 131,064 binary cyclic words of lengths 3 through 16 were checked;
  131,036 were nonmonochromatic, and Theorem 1.1 held in every case;
* the driver's literal motif extractor was independently reconstructed on
  the frozen source and on a pinned defective factor;
* on the defective factor there were 45 literal short top-1 occurrences
  collapsing to 3 orbit nogoods and 60 short top-0 occurrences collapsing to
  4 orbit nogoods; the two independent extractors agreed exactly;
* every extracted motif was nonempty and contained only selected edge
  orbits;
* the source plus all 26,570 additions was checked to equal the full loopless
  catalogue edge universe;
* two successive calls to the atomic JSON helper were replayed and left the
  complete second generation with no temporary file.

The generated audit JSON is
`scratch/ad_k16_r99_dynamic_top_stage_20260729.audit.json`, SHA-256
`7b9179abe76c9365465ca788a5e0b68dc996762540377dee86ab909f4ed7684e`,
embedded payload SHA-256
`debb79f7337a573bb992a6622a450d56866570d6f486ed3675ed04f03edfbf17`.

## 4. Branch locking and exact scope

The equality

```text
cut[22511] == int(locked_branch == "delete")
```

fixes the distinguished cut exactly: `retain` means zero and `delete` means
one.  The two values partition all radius-99 cut sets.

Projection exactness of the conditioned core banks is independently covered
by `scratch/k16_r99_two_branch_core_scope_independent_20260729.audit.json`
(SHA-256
`2d1cf63759cd936478030aedfb88be13853071d6f15179114d06ed865639d490`):
566 cores cover the retain branch and 973 cover the delete branch.  The top
rows and lazy rows introduce no new branch asymmetry.

Connectivity and unit voltage are not imposed.  They remain post-audit
properties.  This is accurately declared in the result scope.

## 5. Hint ingestion audit

Hints do not change the feasible set: every imported bit is passed only to
`add_hint`.  A valid same-source, same-branch radius-99 factor is therefore a
sound warm start, and the auxiliary boundary/reach variables need not be
hinted.

However, ingestion is not fail-closed as provenance validation.  It checks
only that the selected-ID set has 858 distinct entries and differs from the
source by 99 removals and 99 additions.  It does **not** explicitly check:

* catalogue membership of every selected ID;
* exclusion of quotient loops;
* degree two, q1 support, or current-motif hitting;
* agreement of edge 22511 with `--locked-branch`;
* an input artifact SHA or payload digest.

Unknown/off-universe additions are silently absent from variable hints.
An opposite-branch hint may either conflict harmlessly with the fixed bit or
fail the subsequent `contained` core-hint assertion.  These behaviours cannot
make a false factor feasible, but they can make warm-start provenance
ambiguous or abort a run.  A hardened launcher should literal-audit the hint
and require its branch before invoking the driver.

## 6. Incumbent persistence audit

For every callback, the driver first writes a uniquely named raw-incumbent
archive and then replaces the rolling checkpoint.  Each JSON write uses a
temporary file in the destination directory, flushes and `fsync`s it, and
calls `os.replace`.  Thus each visible target is atomic on the same
filesystem, and a failure during the rolling-checkpoint write leaves the
unique archive already written.  The payload digest detects content changes.

Exact limitations:

* the parent directory is not `fsync`ed, so rename durability across a power
  loss or filesystem crash is not proved;
* callback artifacts are correctly labelled
  `RAW_MODEL_INCUMBENT_UNAUDITED`; only the post-solve `lift_and_audit` result
  certifies q1 and top biresidence;
* an audited round checkpoint is not separately archived before the next raw
  callback overwrites the rolling path, although every raw incumbent has a
  unique archive and can be replayed;
* on branch-scoped infeasibility, the artifact is explicitly a CP-SAT
  transcript rather than a standalone proof log.

One metadata detail is harmless but worth preserving in downstream reports:
the round field named `positive_short_runs` is the total positive short-run
count over all coordinates, not the top-only defect count.  Final top status
uses `top_biresidence_ok`, which checks both top-1 and top-0 histograms and is
the correct predicate.

## Final proved boundary

The exact top-stage theorem is proved for all loopless, equivariant,
degree-two radius-99 factors in either declared 22511 branch that satisfy the
base motif and both-q1 rows.  A positive terminal artifact remains subject
only to the explicitly separate connectivity/unit-voltage audit.  No global
negative conclusion is available unless both locked branches terminate
infeasible after all dynamically added valid rows; a timeout or round cap is
only unknown.
