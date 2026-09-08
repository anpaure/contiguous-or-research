# Exact `COMP_3` postprocessor and the single-sector shared-tail no-go

Date: 2026-07-29

Status: exact theorem and executable postprocessor.  The direct depth-three
compiler is sound and complete for a fixed chronology and does **not** impose
`DA=DP`.  The proposed one-block `15 -> 16` shared-tail lift is now proved
impossible.  No `k=16` word is claimed.

## 1. Result

The reusable postprocessor is

```text
scratch/threadD_comp3_postprocessor_20260729.py.
```

It provides six proof-separated operations.

1. Audit arbitrary-width upper coverage of a proposed middle chronology.
2. Solve the full direct `COMP_3(T)` system lazily over every lower target.
3. Couple certified boundary targets to distinct **short interval cells** by
   an exact SDR inside the same source-bit model.
4. Audit the old shared-tail formula literally, while returning the general
   no-go certificate before any proposed `B` search.
5. Reconstruct a `k=16` chronology from the exact even equivariant `(c,t)`
   normal form and gate it through linear q1, unrestricted upper coverage,
   the direct compiler core, and the literal `{z}` source row.
6. Reconstruct a final linear chronology from literal connected-carrier or
   multi-cut PBBS components, cuts, oriented segments and seams, then invoke
   the same compiler with the sharp two-boundary q1 rows.

The main correction is that the compiler fibre is larger than the historical
one-core face.  The retained `k=11` and `k=13` words have respectively 5 and
209 cells at which `DA != DP`; both nevertheless pass the exact compiler.

## 2. The exact direct compiler

Let

```text
T=(T_0,...,T_(W-1)),  |T_i|=r,  L=W+3,
```

and define the maximal source envelope

\[
 P_p=\bigcap_{\max(0,p-3)\le i\le\min(W-1,p)}T_i.
\]

For every `x in P_p` introduce a source bit `a_(p,x)`.  The base model is

\[
 A_p\subseteq P_p,\qquad A_p\ne\varnothing,
\tag{2.1}
\]

and, for every `x in T_i`,

\[
 \bigvee_{p=i}^{i+3}[x\in A_p]=1.
\tag{2.2}
\]

Equations (2.1)--(2.2) are equivalent to `D^3A=T`.  Envelope containment
gives every negative coordinate of a four-window and (2.2) gives every
positive coordinate.  No first-derivative equality is used.

### 2.1 Rank decoupling

For every such source word and every interval of at least four letters,

\[
 \bigcup_{p=a}^{b}A_p
 =\bigcup_{i=a}^{b-3}T_i.
\tag{2.3}
\]

An interval of at most three letters is contained in a four-window and has
rank at most `r`.  Consequently:

* rank-greater-than-`r` coverage depends only on arbitrary-width intervals of
  `T`;
* every rank-less-than-`r` target must occur in one of exactly
  `3L-3` source cells of lengths one, two, or three.

The implementation enumerates arbitrary interval ORs by retaining the
distinct OR states of intervals ending at the current position.  There are at
most `k+1` such states, so the oracle is linear in `kL`, not quadratic in
`L`.

### 2.2 Exact candidate cells

For a short cell `J`, put

\[
 E_J=\bigcup_{p\in J}P_p.
\]

For each required middle incidence `(i,x)`, its possible carriers are

\[
 C_{i,x}=\{p\in[i,i+3]:x\in P_p\}.
\]

Let `M_J` contain every `x` for which some nonempty `C_(i,x)` is contained in
`J`.  Then a target `S` is individually realizable on `J` if and only if

\[
 S\subseteq E_J,qquad M_J\subseteq S,qquad
 P_p\cap S\ne\varnothing\quad(p\in J).
\tag{2.4}

Necessity is immediate.  For sufficiency set `A_p=P_p cap S` on `J` and
`A_p=P_p` elsewhere.  The three conditions respectively give all target
bits, retain every middle carrier, and keep every selected source letter
nonempty.

For a chosen cell, the model channels the selector to the exact equality

\[
 \bigcup_{p\in J}A_p=S.
\tag{2.5}
\]

It forbids every outside-`S` bit and requires every inside-`S` bit somewhere
in `J`.

### 2.3 Lazy completeness

The solver starts with (2.1)--(2.2), decodes a source word, and replays all
`3L-3` short cells.  For every missing target it adds the complete disjunction
of the cells passing (2.4).  Rows persist.

Every added row is necessary for every universal antecedent, and no possible
cell is sampled or capped.  Each unsuccessful round adds a previously absent
target.  Thus the loop is finite and has the following fail-closed statuses.

* A decoded word with no missing target is an independently replayed witness.
* `UNSAT` after exact rows is a proof for that fixed chronology and pins.
* A time limit or an incomplete target catalogue is only `UNKNOWN`.

This proves soundness and completeness of the fixed-chronology postprocessor.
The final literal PASS predicate separately requires that `D^3A` be the
complete middle owner deck.  This closes a former verifier-only gap in which
a universal-looking word with a repeated, overlong middle row could pass even
though the solver correctly rejected that chronology.

### 2.4 Exact literal source-mask rows

For an optional requested source mask `S`, the compiler creates a selector
for every position `p` with `S subseteq P_p`.  A selected position fixes every
envelope bit to its indicator in `S`; coordinates outside `P_p` are already
absent.  Requiring at least one selector is therefore exactly

\[
 \exists p\qquad A_p=S.
\tag{2.6}
\]

Conversely, any core word containing the literal letter `S` extends to these
selectors, so the row is complete.  Multiple distinct masks are conjoined;
repeated identical command-line flags have set semantics.

For `k=16`,

```text
--require-source-mask 32768
```

pins an actual singleton source letter `{z}` somewhere in the full
16-coordinate word.  It does **not** constrain its position, its neighbours,
or the length of the coordinate-`z` run.  In particular it replaces, rather
than supports, the earlier overstrong claim that an exactly-four `B`-run was
necessary.

At final completion this row is logically redundant: because all source
letters are nonempty, any interval whose union is `{z}` consists entirely of
literal `{z}` letters.  It is nevertheless a useful eager master constraint
and an explicit certificate field before all lazy lower rows have been added.
The literal verifier independently reports the positions realizing every
requested mask.  Mask `32768` belongs to full `k=16` geometry; it is not a
valid mask in projected 15-coordinate `B` space.

This mask is now automatic in every k16 `solve_comp3_lazy` call and every
k16 literal audit, even if a caller omits the optional flag.  The dedicated
`(c,t)` and carrier-braid wrappers also pass it explicitly.

## 3. Exact boundary SDR

A right vertex is a short interval `(start,length)`, not a source position.
For an advertised boundary target, the API permits all specified length-one,
length-two, and length-three cells lying wholly in an outer three-letter
halo.  The outer matching uses the exact individual condition (2.4).

Any literal compiler induces an injection from distinct targets to distinct
occurrence cells, because one interval has one OR.  Therefore a Hall
deficiency is an exact obstruction.  A perfect outer matching is only
necessary: overlapping selected cells can jointly erase the last carrier of
a middle bit.  The CP model therefore channels the SDR selectors into the
same source bits and middle clauses.  This integrated model is exact.

The `k=11` regression prevents the old position-only shortcut:

```text
target 155: length-three cells (0,3) and (462,3);
target 154: length-two cell (463,2).
```

The `k=13` target `2135` and the two `k=15` targets `18553,18033` happen to
use singleton endpoint cells, but that is not the generic interface.
The machine-readable request schema is
`scratch/threadD_comp3_boundary_sdr_20260729.schema.json`.

## 4. Calibration

All retained words pass direct literal replay.

| `k` | `W+3` | lower targets | short cells | `DA/DP` errors | status |
|---:|---:|---:|---:|---:|:---|
| 11 | 465 | 1,023 | 1,392 | 5 | PASS |
| 13 | 1,719 | 4,095 | 5,154 | 209 | PASS |
| 15 | 6,438 | 16,383 | 19,311 | 0 | PASS |

For a proposed `k=16` chronology, the exact dimensions are

```text
W=12870, L=12873, lower targets=26332, short cells=38616.
```

Under the resident staircase envelope the source model has 64,377 incidence
bits and 102,960 positive middle clauses before lazy target rows.

The endpoint-normalized parent regression is

```text
scratch/threadD_k15_endpoint_normalized_6438_20260729.word
SHA-256 2448967155c15c9a9f97347254c68f321d1c3a7dff1be365f414189c85ee92b3
tail (17473,608,16), union 18033 of rank seven.
```

It is still an exact universal `k=15` word with unchanged `D^3` chronology.

## 5. The shared-tail construction and its exact no-go

The strict shared-tail proposal takes old and projected-dual words of length
`W+d`, fixes

\[
 (B_0,\ldots,B_{d-1})=(A_W,\ldots,A_{W+d-1}),
\]

and appends the `W` letters `z union B_d,...,z union B_(W+d-1)`.  The old
coordinate projections of intervals meeting this appended sector are

\[
 \begin{aligned}
 \mathcal M(A,B)=
 &\{\bigcup_{j=s}^{t}B_j:d\le s\le t<W+d\}\\
 &\cup\{(\bigcup_{i=s}^{W+d-1}A_i)
          \cup(\bigcup_{j=d}^{t}B_j):0\le s<W+d,\ d\le t<W+d\}.
 \end{aligned}
\tag{5.1}
\]

The original exact criterion was `M(A,B)=2^[15]`.  The following lemma shows
that it can never hold when `D^dB` is a distinct equal-rank deck.

### Theorem 5.1 (distinct equicardinal dilation forces nonempty source)

Let

\[
 R_i=\bigcup_{j=0}^{d}B_{i+j}\qquad(0\le i<W)
\]

be distinct sets of one cardinality, and assume `W>=d+2`.  Then every
`B_p` is nonempty.

#### Proof

If `0<=p<=W-2` and `B_p=empty`, set

\[
 C=\bigcup_{j=p+1}^{p+d}B_j.
\]

Then `R_p=C subseteq C union B_(p+d+1)=R_(p+1)`.  Equal cardinality gives
`R_p=R_(p+1)`, contradicting distinctness.

If `d+1<=p<=W+d-1`, put `i=p-d-1`.  Now `B_(i+d+1)=empty`, so the same
calculation gives `R_(i+1) subseteq R_i`, again forcing equality.  The two
source-index ranges

\[
 [0,W-2]\quad\hbox{and}\quad[d+1,W+d-1]
\]

cover `[0,W+d-1]` because `W>=d+2`.  QED.

### Corollary 5.2 (single appended sector is impossible)

Every interval meeting the appended sector contains at least one projected
letter `B_p`.  By Theorem 5.1 its old-coordinate projection is nonempty.
It therefore cannot realize the target `{z}`, whose old-coordinate projection
is empty.  Equivalently `0 notin M(A,B)`.

Thus the strict one-block shared-tail template is impossible for `15 -> 16`,
independently of the parent compiler, the rank-seven chronology, component
cuts, orientations, ordering, or marked-cover optimization.

For the frozen proposed prefix

```text
B0..3=(17473,608,16,0),
```

the contradiction is already local: `B3=0` gives `R3 subseteq R4`; equal
rank forces `R3=R4`.  The normalized parent remains a useful exact regression,
but it cannot seed a one-sector dual deck.

The code command

```sh
python3 scratch/threadD_comp3_postprocessor_20260729.py \
  shared-tail-no-go --old-k 15
```

returns this index certificate without importing a solver.

## 6. MSW interface: secondary finite audit

The API decodes the frozen 429 coordinate-order rows into 429 disjoint
length-15 Johnson cycles and can materialize any component order, cyclic cut,
and orientation.  This remains a useful segmented-search input format.

As a secondary check, both

```text
scratch/m7_msw_fixed_slot_cube_best_base.txt
scratch/m7_msw_fixed_slot_cube_best.txt
```

have zero intact-cycle start states satisfying the corrected early pin

\[
 R_0=18033,\qquad R_1\supseteq624,\qquad R_2\supseteq16.
\]

That finite zero is scoped only to concatenations of those intact cycles.
Theorem 5.1/Corollary 5.2 is stronger and makes further one-sector search
unnecessary.

The former fixed-`R` and variable-MSW shared-tail solve commands have been
retired.  Only the literal refutation audit and theorem command remain.

## 7. Degree-two rail/rung handoff

The distributed route now has a fail-closed input schema

```text
threadD-degree2-rail-rung-chronology-v1.
```

It requires an explicit `middle_path`, the complete degree-two factor edge
ledger labelled `rail`/`rung`, and the nonfactor seam ledger.  The adapter
recomputes, rather than trusts, all of the following:

1. the path is the complete rank-eight deck with no duplicate owner;
2. the factor has exactly `W` simple edges and degree two at every owner;
3. its connected components are the advertised physical rails;
4. the path uses exactly one cut per component and exactly `c-1` declared
   seams;
5. every path adjacency is either a retained factor edge or a declared seam;
6. Johnson adjacency, when `edge_policy="johnson"`;
7. the direct `COMP_3` maximal-envelope/core gate; and
8. unrestricted upper coverage.

Its status `READY_FOR_COMP3` is deliberately not `PASS`; it only authorizes
the exact lazy compiler.  The optional full candidate census then checks all
26,332 lower targets against all 38,616 short cells.

The command is

```sh
python3 scratch/threadD_comp3_postprocessor_20260729.py audit-rail-rung \
  --candidate H_OR_R_OUTPUT.json --full-candidates
```

The current resident rank-seven MSW shore and its scoped `361/429` insertion
no-go are upstream construction facts, not compiler inputs.  This adapter
waits for H/R to emit the literal combined rank-eight path and edge ledger;
it does not infer that chronology from scalar shore statistics.

## 8. Exact even equivariant `(c,t)` handoff

The compact route of
`MATH_EVEN_EQUIVARIANT_CT_NORMAL_FORM_20260729.md` now has a separate,
fail-closed adapter.  For `k=16`, put

```text
n=15, r=8, W=12870, N=858, z=bit 15.
```

The only registered decoder reconstructs the cyclic chronology literally as

\[
 T_i=(\{z\}:t_{i\bmod858}=1)
     \cup\{x<15:c_{i-858x\bmod12870}=1\}.
\tag{8.1}
\]

The decoder contract has ID `threadD-even-unit-voltage-ct-v1` and digest

```text
1910ff534b869038b5099b999defbaf4dfbca31667a6c5346d25ead23d59b8c5.
```

An unknown ID or contract digest returns the structured status
`DECODER_UNAVAILABLE`; it is never interpreted through a nearby formula.
The same metadata/hash checks run again in the direct Python audit API, so
bypassing the JSON loader does not bypass the decoder contract.  Fixed
numeric metadata must be plain integers and `provenance` must be nonempty.

An input must declare both `linear_start` and `orientation`; the adapter never
silently removes a cyclic edge.  It does not accept an embedded middle path.
Instead it reconstructs all 12,870 masks and checks the declared digest after
linearization.

Before authorizing `COMP_3`, it independently replays:

1. binary lengths, class sums `sum_(a=j mod 858)c_a=8-t_j`, and the exact
   insertion/deletion transversality table;
2. 429 zeros and 429 ones in `t`, the two 429-orbit necklace bijections,
   cyclic Johnson adjacency, unit-voltage equivariance, and minimum cyclic
   one-run four in both `c` and `t`;
3. the complete rank-eight owner deck;
4. on the actual **linear** path, the adjacent-intersection ledger for all
   11,440 rank-seven targets; zero, one or two missing targets are accepted
   only when their exact boundary-cell SDR has zero deficiency, while three
   or more are an exact boundary-capacity obstruction;
5. the adjacent upper-q1 palette as an audit ledger, followed by the exact
   unrestricted arbitrary-width upper oracle at every rank 9 through 16;
6. the maximal-envelope `D^3` core and a nonzero envelope candidate count
   for literal mask `32768`.

The last count is only a necessary prefilter.  The solve command always calls
the compiler with `required_source_masks=[32768]`, and independent replay
must find an actual source letter equal to `{z}`.  Thus
`READY_FOR_COMP3_WITH_Z_PIN` is not a word certificate.

The machine-readable input schema is

```text
scratch/threadD_k16_even_ct_candidate_20260729.schema.json.
```

It accepts compact bit strings or dense binary arrays, but canonical hashes
are always taken after decoding to integer lists.  The commands are

```sh
python3 scratch/threadD_comp3_postprocessor_20260729.py audit-even-ct \
  --candidate CT.json --output-middle k16.middle --output CT.audit.json

PYTHONPATH=/dev/shm/orlib python3 \
  scratch/threadD_comp3_postprocessor_20260729.py solve-even-ct-comp3 \
  --candidate CT.json --boundary-json BOUNDARY.json \
  --output-word k16.word --output k16.solve.audit.json
```

The first command is solver-free.  The second refuses to instantiate OR-Tools
unless all preceding chronology gates pass.
It also refuses an already existing `--output-word` path; a failed run can
therefore never leave that named path looking like a newly emitted
certificate.

### Theorem 8.1 (adapter soundness and completeness)

Fix a schema-valid `(c,t,start,orientation)` record.  The chronology supplied
to the compiler is exactly the linearization of (8.1).  The status
`READY_FOR_COMP3_WITH_Z_PIN` holds exactly when the replayed normal-form,
owner, linear lower-q1 boundary-capacity/SDR, unrestricted upper, maximal-core, and nonempty
`{z}`-envelope preconditions listed above hold.  It makes no assertion that
the simultaneous lower compiler is feasible.

Conditional on that status and an optional external boundary ledger,
`solve-even-ct-comp3` automatically merges the missing lower-q1 targets with
the external requests and
returns `PASS` if and only if there is a nonempty source word `A` with
`D^3A=T`, every lower target represented by a length-at-most-three source
interval, every boundary request assigned to a distinct allowed boundary
cell, and some literal letter `A_p={z}`.  Indeed the `(c,t)` wrapper changes
none of the clauses proved exact in Sections 2--3; it only fixes `T`, supplies
the exact source-mask row (2.6), and replays the decoded word.  Arbitrary-width
upper completeness was already decided solely by `T`.  Therefore neither a
false positive nor a fixed-chronology false negative is introduced by the
adapter.  Time-limit status remains `UNKNOWN`.

## 9. Literal connected-carrier / PBBS-braid handoff

The second construction-neutral k16 schema is

```text
threadD-k16-literal-carrier-braid-v1
scratch/threadD_k16_literal_carrier_braid_20260729.schema.json.
```

It consumes literal cyclic physical components, arbitrary cut positions, a
permutation of all oriented canonical segments, and the directed seam list.
The middle path is reconstructed; an embedded chronology is neither needed
nor trusted.  One component/one cut is the connected-quotient mode.  The PBBS
mode permits arbitrarily many cuts in every component.

The exact q1 correction is important.  Zero lower-q1 holes is not necessary:
the retained universal `k=11,k=13,k=15` chronologies have respectively one,
one and two.  More than two is exact UNSAT.  For one or two, the wrapper adds
the missing colours to the integrated endpoint-cell SDR automatically.  Fixed
lower q2 is diagnostic only; fixed upper q1/q2 are exact for those ranks on a
Johnson path, while q3 and deeper use the unrestricted accumulated-union
oracle.

The full theorem, counterexamples, schema semantics and retained connected/
two-component regressions are in
`THREAD_D_K16_LITERAL_CARRIER_BRAID_COMP3_GATE_20260729.md`.

## 10. Redirected `k=16` API and the remaining lemma

The live route is the distributed multi-sector/segmented braid.  It should
materialize a literal rank-eight chronology `T` of all 12,870 owners and pass
that chronology to the generic commands

```sh
python3 scratch/threadD_comp3_postprocessor_20260729.py score-middle \
  --middle CANDIDATE.json --k 16 --rank 8

PYTHONPATH=/dev/shm/orlib python3 \
  scratch/threadD_comp3_postprocessor_20260729.py solve-comp3 \
  --middle CANDIDATE.json --k 16 --rank 8 \
  --boundary-json BOUNDARY.json --require-source-mask 32768 \
  --output-word k16.word
```

The exact minimal fixed-chronology lemma is:

> There is an ordering `T` of the complete rank-eight layer such that every
> upper target is an arbitrary-width interval union of `T` and `COMP_3(T)`
> is feasible.

This statement is necessary and sufficient for the direct depth-three
architecture.  Its witness is a length-12,873 word; an independently replayed
witness proves the optimal value.  When a rail/rung construction advertises
specific cut-colour obligations, their exact boundary SDR rows are additional
candidate-specific constraints, not part of the architecture-free lemma.  For
an all-dimension induction one must in addition prove that the segmented braid
produces such a `T`; the compiler itself no longer hides a rounding or
`DA=DP` assumption.

## 11. Executable audit

The solver-free regression is

```text
scratch/audit_threadD_comp3_postprocessor_20260729.py
scratch/threadD_comp3_postprocessor_20260729.audit.json.
```

Twenty-six local tests cover exact candidate cells, arbitrary-width interval
states, the long/short rank identity, boundary interval cells, all three
retained words, the normalized parent, MSW decoding, and an exhaustive small
check of Theorem 5.1, plus separation of the degree-two ledger and compiler
core gates, literal source-mask replay, the exact small even `(c,t)` decoder,
explicit cut/orientation semantics, linear q1 palettes, rejection of an
unregistered decoder, all 256 small `(c,t)` pairs at `k=4` (including the
`j=N-1` transition wrap), exclusive fresh certificate output, complete-middle
PASS enforcement, literal connected/multi-component braid reconstruction, and
fail-closed public carrier-loader digest/schema/seam parsing, and the exact
physical expansion of the frozen k16 Hamilton quotient's two missing q1
orbits into a 20-colour literal leave.
The primary k16 regression is the q1-perfect, top-biresident physical
Hamilton scaffold: its best q1-perfect cut reaches the exact core gate and is
rejected with 7,882 empty carriers, while the lower2 Hamilton remains a
diagnostic orbit-expansion regression only.
The retained `k=11,k=13,k=15` words are replayed with their top-coordinate
singletons required.  They run in under one second.

A one-worker H100 CPU smoke used the required `/dev/shm/orlib` runtime.  It
solved the source-mask-augmented tiny compiler (17 variables, 28 constraints)
to `OPTIMAL`.  A separate synthetic `k=16` equality regression used the same
`D^3` chronology for two fixed words: `(2,1,1,32768,4)` is `OPTIMAL` under
the literal-32768 row, while `(2,1,1,32769,4)` is feasible without the row
and `INFEASIBLE` with it.  No full `k=16` chronology solve was launched.

The H100 CPU was reachable but heavily saturated during this iteration, so no
refreshed job was launched and no solver was run locally.  The source-mask
normalization and `Comp3Cp` encoding
remain AST-identical to the retained H100 execution.  `solve_comp3_lazy` and
`full_word_audit` intentionally changed: they now insert mask `32768`
automatically at k16, and the literal verifier additionally requires the
complete middle deck.  Those guards and both new reconstruction front ends are
solver-free local-regression claims, not retroactive H100 execution claims.

Current frozen SHA-256 values are

```text
7f434a2fd6b7258355fbe50cb21c6e178af51561d06a5c468b398fb0c58931b8
    scratch/threadD_comp3_postprocessor_20260729.py
fd396e1d8174b62d170cfa33932eecaf70cb391a634d6d4f816782cb77790f65
    scratch/test_threadD_comp3_postprocessor_20260729.py
30c95c7eb05b70f1bb466a83eb7c57947e50b396c5bf2fcacbad3a4ffbc63d4d
    scratch/audit_threadD_comp3_postprocessor_20260729.py
56253e6706bf9d0c7cf53491f5a8e015dab4463c11bd47e98030961058ef1733
    scratch/threadD_comp3_postprocessor_20260729.audit.json
cbea914921d7b345ca585eedcccd833d00ffe20cbe61724bc41f225f658fecf5
    scratch/threadD_k16_even_ct_candidate_20260729.schema.json
8454c19c9d2f13fb7fe45d39df37336716a593fcafb1f1f74a980e5d1d328c2a
    scratch/threadD_k16_literal_carrier_braid_20260729.schema.json
71a0b55852c0733a5faf03aa9e744fbef0664a3623b0c5e83d7ec17d59895943
    scratch/materialize_threadD_k16_connected_q1_lower2_hamilton_20260729.py
c24c2e22f9b4c4bf288b6bac9995771278bcc5e6bd5b2bc326a8fb4cacca3ce4
    scratch/threadD_k16_connected_q1_lower2_hamilton_cut33.carrier.json
3273c32f9c6fe587af9170b0cc481339b5919ce6c209a8871691a912b577e976
    scratch/threadD_k16_connected_q1_lower2_hamilton_comp3.audit.json
76e234542f06e22d5a1ce8131a78c6c6f60b62ce1206cd10608ed4467ef94c20
    scratch/materialize_threadD_k16_q1_topresident_hamilton_20260729.py
3fdd156360f93dac4021131ae2dbe1bd47c5f2c7b15332277a8b34743a4fae10
    scratch/threadD_k16_q1_topresident_hamilton_bestq1.carrier.json
ac3a2c0526a0aa1f076a90368e48e4e01686d4d469244c1aab14e26aa67d757e
    scratch/threadD_k16_q1_topresident_hamilton_comp3.audit.json
```

The historical H100-executed module is separately identified by
`cb4692dacb88cbe42a5c2c174111adc91a666b41e996ddf69185b822e7841780`.
Its executed smoke-driver digest was
`43558b29a8ba7494f2edfa118aba70c42468c15153cd4b1590c7fec7b2d81100`;
that exact driver is not the current retained driver
(`f5327e14cc97103f4ae7dda889cd6d4d94f0e1db05c1976f0b46ba6860baa74e`),
so the JSON smoke record
and retained module, rather than the current driver text, are the historical
execution artifacts.  A later rerun may refresh driver-level provenance when
the H100 is no longer saturated.
