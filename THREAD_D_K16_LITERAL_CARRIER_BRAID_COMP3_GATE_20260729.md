# The exact `k=16` literal carrier-braid to `COMP_3` gate

Date: 2026-07-29

Status: exact theorem and fail-closed adapter.  It accepts either a connected
physical quotient carrier or a literal multi-component PBBS braid.  No current
`k=16` artifact passes the complete gate, and no `k=16` word is claimed.

## 1. Exact fixed-chronology theorem

Let

\[
 T=(T_0,\ldots,T_{W-1}),\qquad |T_i|=8,qquad W={16\choose8},
\]

be a linear chronology, and put

\[
 P_p=\bigcap_{\max(0,p-3)\le i\le\min(W-1,p)}T_i
 \quad(0\le p<W+3).
\tag{1.1}
\]

### Theorem 1.1 (base core)

There is a nonempty source word `A` with `D^3A=T` if and only if

\[
 D^3P=T\qquad\hbox{and}\qquad P_p\ne\varnothing\quad(0\le p<W+3).
\tag{1.2}
\]

Every antecedent has `A_p subseteq P_p`.  Conversely `A=P` proves
sufficiency.  Thus cyclic residence of an input factor is not authoritative:
after cuts, orientations and seams, the exact condition is the **linear**
identity (1.2).

### Theorem 1.2 (upper/lower separation)

For every antecedent satisfying `D^3A=T` and every source interval of length
at least four,

\[
 \bigcup_{p=a}^{b}A_p=\bigcup_{i=a}^{b-3}T_i.
\tag{1.3}
\]

Every interval of length at most three has rank at most eight.  Therefore:

* complete arbitrary-width interval-OR coverage by `T` at ranks `9,...,16`
  is necessary and sufficient for **all upper targets**;
* every lower target must be realized by one of the `3(W+3)-3` source cells
  of lengths one, two or three;
* the exact lower gate is simultaneous feasibility of those source-cell OR
  rows with the common carrier clauses.  No shadow census substitutes for
  this coupled Boolean problem.

Together with complete middle ownership, (1.2), unrestricted upper coverage,
and the exact lower model are necessary and sufficient for the flat-middle
`COMP_3` architecture.

## 2. What q1 and q2 do—and do not—prove

Assume now that `T` is a Johnson path.

### 2.1 Upper shadows

Upper q1 is exactly the adjacent-union palette.  Upper q2 is exactly the
three-consecutive-state union palette.  Indeed, at the first state where an
interval union reaches rank ten, its preceding union has rank nine; the last
two distinct adjacent rank-eight states already union to that rank-nine set.
The last three states therefore realize the rank-ten target.

This stops at q2.  With a fixed six-set `C`, the Johnson path

```text
C+01, C+02, C+03, C+23, C+24
```

has total union of rank eleven, while neither four-state subinterval has that
union.  Hence fixed upper q3 and deeper are diagnostics; the accumulated-union
oracle is mandatory.

### 2.2 Lower q1: the sharp two-boundary theorem

Let

\[
 {\cal C}_1(T)=\{T_i\cap T_{i+1}:0\le i<W-1\}.
\]

Any rank-seven target absent from `C_1(T)` must be witnessed by a source
interval using source position `0` or `W+2`.  Same-rank prefix unions are
nested, as are suffix unions, so at most one new colour can occur at each
end.  Universality therefore forces

\[
 {16\choose7}-|{\cal C}_1(T)|\le2.
\tag{2.1}
\]

Zero q1 holes is a useful route-specific condition, not the generic theorem.
For one or two holes the adapter creates automatic endpoint-cell rows and
couples them to the same source bits.  More than two returns exact UNSAT.

### 2.3 Lower q2 and static Hall

Canonical lower q1/q2 intersections are sufficient **individual** candidate
witnesses under (1.2), but they are neither necessary nor jointly sufficient.
The retained exact words demonstrate non-necessity:

| word | linear lower-q1 holes | fixed lower-q2 holes |
|:--|:--|:--|
| `k=11` | `155` | `154` |
| `k=13` | `2135` | none |
| `k=15` | `18033,18553` | none |

All three words pass exhaustive universality; the displayed targets occur in
boundary source cells.

Even an SDR for a family of individual target-to-cell candidate rows is not
sufficient.  Fix a five-set
`C` disjoint from `0,1,2,3` and take

\[
 T_0=C+012,\qquad T_1=C+013.
\]

Then the maximal envelope is

\[
 (T_0,C+01,C+01,C+01,T_1).
\]

The incomparable rank-seven targets `C+02` and `C+12` each have all three
prefix cells as individual candidates and admit a distinct-cell matching.
But prefix ORs are nested, so no one source word can realize both.  Static
candidate degree and static SDR are exact rejection screens only; integrated
source-bit coupling is indispensable.

## 3. Literal carrier-braid adapter

The machine-readable schema is

```text
threadD-k16-literal-carrier-braid-v1
scratch/threadD_k16_literal_carrier_braid_20260729.schema.json.
```

It deliberately accepts no embedded middle path.  Its inputs are:

1. literal cyclic physical components partitioning the rank-eight owners;
2. an arbitrary nonempty cut set in every component;
3. a permutation of all canonical segment IDs, with one orientation per
   segment; and
4. the exact directed seam list and reconstructed-middle digest.

A segment associated with cut edge `e` starts after `e` and ends at the next
cut edge in the same component.  Segment IDs are the cuts sorted by
`(component,edge_index)`.  This supports one cut in one connected quotient
cycle and arbitrarily many cuts in a PBBS component.

The adapter independently verifies:

* every component is a simple Johnson cycle and the complete component deck
  is the rank-eight layer;
* every cut is used once, every segment is used once, and the declared seams
  equal the derived nonfactor adjacencies;
* the reconstructed linear path is owner-exact and Johnson;
* the sharp q1 boundary capacity and necessary endpoint candidate-SDR screen;
* (1.2), unrestricted upper completeness, and a position whose envelope
  contains `32768`;
* optionally, every lower target has at least one exact individual short-cell
  candidate.

`READY_FOR_EXACT_COMP3_WITH_Z_PIN` is not PASS.

## 4. Exact solve wrapper

`solve-carrier-braid-comp3` recomputes the chronology and all preceding
gates, automatically adds every palette-absent lower-q1 target to the
boundary ledger, merges any external boundary obligations, and invokes the
complete lazy lower compiler.  Every k16 production solve and literal replay
automatically inserts

```text
required_source_masks=[32768].
```

Thus a caller cannot omit the actual singleton source letter `{z}`.  A final
PASS additionally requires exact `D^3`, the complete owner deck, all lower and
upper targets, expected-middle equality, and independent literal replay.
Certificate output is fresh-only and never overwrites an existing path.

Commands:

```sh
python3 scratch/threadD_comp3_postprocessor_20260729.py \
  audit-carrier-braid --candidate CARRIER.json --full-candidates \
  --output-middle k16.middle --output CARRIER.audit.json

PYTHONPATH=/dev/shm/orlib python3 \
  scratch/threadD_comp3_postprocessor_20260729.py \
  solve-carrier-braid-comp3 --candidate CARRIER.json \
  --boundary-json BOUNDARY.json --workers 1 \
  --output-word k16.word --output k16.solve.audit.json
```

Heavy SAT/CP execution belongs on the H100 CPU.  Reconstruction, shadow
audits and retained regressions are solver-free.

## 5. Exact retained regressions

The connected-mode regression closes the retained `k=11` middle chronology
with edge `159--219`, opens it once, and reconstructs the exact path.  It has
one missing lower-q1 colour `155`, endpoint SDR deficiency zero, and zero
individual-candidate holes.

The component-braid regression uses the literal two-component `k=15` PBBS
factor

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
    from3_markov_s7_merge.components.json
SHA-256 f765d52aa68810af0e4897c6881f46ecf016b86394341a97f894dc6b53058151
```

with cuts at component-edge indices `22` and `41`, segment orientations
forward/reverse, and seam `19065 -> 18041`.  It reconstructs the retained
`k=15` chronology exactly, has the two boundary colours `18033,18553`, and
literal word replay passes with the required top-coordinate singleton.

The retained `k=11,k=13,k=15` words all pass with their top-coordinate
singletons required explicitly.  The standalone verifier also has a permanent
negative regression: a universal-looking word whose `D^3` row repeats owners
can no longer return PASS.

## 6. Current `k=16` frontier

No existing quotient or PBBS artifact is compiler-ready.

* The canonical compiler preflight is now
  `k16_qfactor_q1_topresident_hamilton_20260729.json`: one physical Hamilton
  cycle, complete lower/upper q1 palettes and top biresidence.  Of its 12,870
  cuts, 585 preserve both linear q1 palettes.  The unique best q1-perfect cut
  orbit has 7,882 empty coordinate carriers and still violates `D^3P=T` in
  6,686 middle rows.  Thus its first non-q1 failure is the exact core, before
  the coupled Hall solve.  It also has 1,796 cyclic-unavoidable upper holes
  (`10:1433, 11:318, 12:45`).
* The formerly primary lower2 Hamilton
  `k16_connected_q1_lower2_hamilton_20260729.json` is a genuine one-cycle
  diagnostic factor, but its advertised two lower-q1 holes are **quotient
  orbits**, not literal colours.  Their representatives are `33371` (orbit
  size 15) and `38053` (orbit size 5), so the physical cyclic leave has 20
  rank-seven targets.  Across all 25,740 directed openings, the exact
  `(linear holes, endpoint-SDR matching)` census is
  `(20,0):5490`, `(20,1):150`, `(21,1):19530`, `(21,2):570`.
  The minimum deficiency is therefore 19, and the fixed Hamilton factor is
  exact lower-q1 UNSAT before a compiler solve.
* The named connected base delta
  `k16_even_q2f_connected_soft_20260729.json` is not self-contained and has
  lower/upper q1 holes `3/5`, arbitrary-upper orbit holes `131`, and `3465`
  short runs.  A separately frozen two-switch census improves only its q1
  ledger to `2/5`; it is still not a compiler-ready literal chronology.
* The self-contained `k16_even_q2f_cross2_seed7.json` factor records complete
  q1, lower-q2 and arbitrary-upper orbit support, but has `145` physical
  components and `1050` short runs; a literal residence-safe final braid is
  still missing.
* The current PBBS full macro factor has `39` components, upper-q1 holes
  `533`, lower/upper q2 holes `195/426`, and `971` residence violations.
* The `552`-cut PBBS certificate is a proved fixed-cut no-go, not an input
  chronology.

These failures are construction facts, not failures of the compiler.  The
adapter is now ready for the first literal connected cycle or complete PBBS
braid that survives them.

For the diagnostic lower2 scaffold, the independent non-q1 gates also fail.
There are 3,420 cyclic positive runs of lengths below four, so every opening
violates the exact maximal-envelope equation `D^3P=T`; the best opening still
has 7,866 empty coordinate carriers.  Cyclic arbitrary-width upper coverage
already misses 1,893 physical targets, with rank histogram
`10:1420, 11:438, 12:35`, hence no opening can repair it.  The 89 missing
lower-q2 orbits expand to 1,313 physical fixed-window holes but remain a
diagnostic, not the exact coupled lower gate.  The singleton `{z}` is not the
immediate issue: the stable cut has 4,218 envelope candidate positions.

Both compact quotient files are materialized fail-closed through their pinned
27,456-row catalogues before entering the literal adapter.  The canonical
compiler preflight comes first:

```text
scratch/materialize_threadD_k16_q1_topresident_hamilton_20260729.py
scratch/threadD_k16_q1_topresident_hamilton_comp3.audit.json
```

The lower2 diagnostic remains reproducible separately:

```text
scratch/materialize_threadD_k16_connected_q1_lower2_hamilton_20260729.py
scratch/threadD_k16_connected_q1_lower2_hamilton_comp3.audit.json
```
