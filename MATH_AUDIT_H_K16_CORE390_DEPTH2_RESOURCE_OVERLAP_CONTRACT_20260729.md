# Core390 depth-two beam: exact resource and overlap contract

## 1. Frozen input

Let

* `Q0` be `scratch/k16_q1_endpoint_resume1_failedlit0_20260729.json`,
  SHA-256
  `17bd05a0bb0da228e580d65bdec27ce04589072baecb8575e0623fc4ea4343b8`;
* `K390` be
  `scratch/k16_failedlit0_guarded_q1_motif_core_20260729.json`,
  SHA-256
  `2f8031fff879faf42b80a169aee2f0a0f5a2484987c5fe625c20fc5bf945c238`.

The frozen endpoint is a 12,870-edge spanning Johnson 2-factor and has zero
lower- and upper-`q1` holes.  The exact guarded infeasible core has twenty-two
rows: eight lower-`q1` rows, thirteen upper-`q1` rows, and motif row 390.
The motif closure is

\[
 (57902,57998),\quad (57902,61994),\quad (57998,58250).
\]

The twenty-one `q1` rows contain twenty-one distinct blue-provider indices
and thirteen red-provider occurrences with twelve distinct red-provider
indices.  The three motif indices are exactly

\[
 11795,11796,11821,
\]

and all three already occur among the twenty-one blue-provider indices.
Consequently the serialized fixed-overlay support contains exactly

\[
             21+12=33                                      \tag{1}
\]

distinct terms, not thirty-six.  Here a blue term is hit by deleting that
edge and a red term is hit by adding that edge.  Equation (1) is only an
overlay sub-census; it is not the complete row-hit halo required here.

The authoritative physical row catalogue is
`scratch/k16_failedlit0_complete_core_q1_provider_catalogue_20260729.json`,
SHA-256
`9ba223ea58e00cd2f9619c5ce7f309ff45c62b5d90beabb7cea3b30aa254df70`.
Every lower or upper colour has 36 Johnson provider edges.  The twenty-one
rows have 756 row-edge incidences, with multiplicity histogram 708 edges
used once and 24 edges used twice.  Therefore their union has

\[
                 708+24=732.                              \tag{2}
\]

Exactly 21 of these edges lie in `Q0` and are deletion targets; the other
711 are addition targets.  The three motif-closure edges lie in the same
732-edge carrier, so adjoining them does not enlarge it.  The mandatory
direct row-hit scope is thus `21+711=732` signed terms.  The separate
8,224-edge one-star catalogue is only an optional enlargement.

## 2. Enumeration-free branching bound

The Johnson graph on rank-eight subsets of `[16]` has degree
`8*8=64`.  Fix one signed focus edge and a radius `r` in `{2,3,4}`.  After
choosing one of its two orientations, each of the remaining `r-1`
alternating pairs has at most 64 choices for a new Johnson edge and at most
two choices for the following old factor edge.  Hence the number of terminal
walks before closure, simplicity, `q1`, and duplicate rejection is at most

\[
             2(2\cdot64)^{r-1}.
\]

Thus the exact displayed upper bounds are

\[
 r=2:256,\qquad r=3:32768,\qquad r=4:4194304.             \tag{3}
\]

Summing (3) over the 732 signed provider terms gives

\[
 732(256+32768+4194304)=3094404096                       \tag{4}
\]

terminal walks for the first parent.  This deliberately overcounts packets
meeting several rows and both endpoints of a row.  If the second step is
again restricted to at most 732 rebuilt signed provider terms, its symbolic
bound is `N1*3094404096`, where `N1` is the number of retained first states.
If the second step uses another focus rule, its plan must state and audit the
corresponding finite focus count; (4) must not be silently reused.

This is a time/streaming warning, not an in-memory state count and not a
completion forecast.

Lane R uses an exact smaller enumeration transversal called `local`: the 61
current `Q0` edges incident with an overlay-active provider endpoint, together
with the 276 absent palette providers whose two endpoints avoid all active
endpoints.  Its 337 targets have terminal-walk envelope

\[
 337(256+32768+4194304)=1424609536.                       \tag{5}
\]

This reduction loses no direct row-hit packet.  If a packet deletes a present
core provider, that deletion is among the 61.  If it adds an absent core
provider with two remote endpoints, that addition is among the 276.  If the
added provider has an active endpoint, degree balance forces deletion of a
current `Q0` edge at that endpoint, again among the 61.  Thus `local` covers
every packet hitting the 732-edge row carrier, while admitting some additional
degree-neighbourhood packets.

## 3. Exact boundary with Lane R

For a factor `Q`, write a packet as the signed pair `(D,A)`, where `D` is
deleted from `Q` and `A` is added.  Its canonical signature is the sorted
pair of sorted physical edge sets.  Let `R1` be Lane R's *completed* frozen
single-halo catalogue: all exact-`q1`, connected, edge-simple, balanced
alternating packets of radii two, three, or four hitting the exact reduced
337-target `local` carrier above.  Its enumerator is
`scratch/search_k16_q0_core22_radius4_halo_20260729.py`; the launch package
must bind the exact source hash recorded by every completed R report.  No
completed R report exists at this audit, and the source changed while this
static audit was assembled, so an earlier plan hash is deliberately not a
launch binding.

The proposed first layer is not new: every admissible first packet belongs to
`R1`.  A nonduplicate depth-two job must therefore obey all of the following.

1. It hash-validates R's endpoint, resident factor, catalogue, radii, focus
   digest, completion status, and complete candidate-signature list.
2. It imports those candidates as routing states and independently replays
   degree and both `q1` ledgers.  It does not enumerate that first layer
   again.
3. It rebuilds the exact guarded-core/detector data after the first packet
   before choosing or scoring the second packet.
4. A reported winner has a canonical **net** signature outside `R1` (or
   fails an equivalent, hash-frozen structural coverage predicate for R's
   exact declared scope).

For sharded R output, `PASS_SELECTED_CORE_HALO_COMPLETE` certifies only the
selected shard.  A complete merge must require `target_classes=[local]`,
the same frozen input and code hashes and radii in every report, every delete
shard index and every add shard index for their declared shard counts, and
exact coverage of all 61 local deletions plus 276 remote additions.  Candidate
signatures and target metadata must be unioned and deduplicated across
shards; the per-shard field `q1_exact_distinct_selected_scope` certifies only
that selected shard and is not a merged-global count.

If R's reports cover only a strict subset of (2), the package must spell out
the exact complement and may enumerate only that complement in addition to
importing R's results.  If the completed R reports or their exact coverage
predicate are unavailable, nonduplication is unproved and launch must fail
closed.

Notice that merely using two packets is not enough: cancellation can reduce
their net symmetric difference to a single packet already in `R1`.

The audited finite beam cap is as follows.  Read and hash the complete merged
R catalogue, retain its full signature/digest union for the novelty test, and
apply a deterministic diversity prefilter to at most 1,024 candidates.  Run the
exact single-worker detector once on each prefiltered state and retain at most
`K=96`.  Test every unordered pair of distinct retained packets, at most

\[
                 {96\choose2}=4560,                       \tag{6}
\]

rebuilding the physical factor and both `q1` ledgers before detector scoring.
Thus there are at most `1024+4560=5584` exact detector calls.  With a hard
two-CPU-second per-call budget, their aggregate solver budget is at most
11,168 CPU-seconds.  An `UNKNOWN` call is not a success.  The second layer
does not rescan the full R union.  This is a bounded top-96 composition beam,
not a complete census of all depth-two pairs.

## 4. Memory theorem and its limit

A deliberately conservative allowance for one materialized CPython factor
is

\[
 2^{20}+12870(112+64)=3313696\text{ bytes}.               \tag{7}
\]

The two integer objects plus their tuple are charged 112 bytes per edge, and
64 further bytes per edge are reserved for hash-table slack.  A 16-GiB
address-space ceiling contains 5,184 copies of (7).  This does **not** prove
that 7,776 simultaneous scored states fit: constraint rows, implication
proofs, traversal stacks, SQLite pages, and allocator fragmentation can
dominate (7).

Accordingly the only proof-safe `<=24 GiB` claim is a fail-stop one.  The
driver must stream candidates, retain only a fixed-width compact frontier,
use a bounded packet cache, score in the same process, and impose
`RLIMIT_AS=16 GiB`, strictly below the requested 24-GiB ceiling.  Exceeding
the cap is permitted to terminate the job; it
must not spawn another worker or silently lift the cap.

## 5. Immutable launch package

A launchable package must contain only hash-manifested files and satisfy:

* exact hashes for `Q0`, `K390`, the resident factor, base, B certificate,
  A cycles, the 732-edge provider catalogue, edge catalogue, R enumerator,
  driver, static audit, every R shard report, and the merged R report;
* a plan-only replay that validates the twenty-two-row census, the fixed
  closure, the `21/711/732` provider counts, and zero initial `q1` holes;
* one Python process and `workers=1`; no process pool or solver subprocess;
* host gate `hostname -s == arboghast` and explicit
  `H100_HEADROOM_CONFIRMED=YES`;
* `ulimit -v 16777216`, `ulimit -t 21600`, and `ulimit -c 0`, plus a bounded
  output/checkpoint file size (preferably an internal byte-exact
  `RLIMIT_FSIZE` of 8 GiB);
* `CUDA_VISIBLE_DEVICES` empty and all numerical-library thread counts one;
* a package-unique nonblocking lock, so a second core390 beam refuses to
  start;
* `sha256sum -c SHA256SUMS` before either the audit or driver runs;
* an on-disk checkpoint and atomic final JSON.  No result file means no
  theorem or detector-zero claim.

The wrapper is allowed to run only after a fresh H100 headroom check.  The
16-GiB ceiling is an immutable safety property, not evidence that the search
will finish within its six-hour CPU budget.

## 6. Proved and conditional boundary

Unconditionally proved here are the serialized `21/12/33` sub-census, the
authoritative `21/711/732` complete row-carrier census, the branching bounds
(3)--(5), the top-96 call bound (6), the factor-footprint allowance (7), and
the exact logical form of
the R-overlap test.  A core390 depth-two launch is conditional on receipt and
hash-validation of R's complete single-halo reports and on a driver satisfying
the streaming/fail-stop contract above.  No R result exists at the time of
this audit; no search was run and no new endpoint is claimed.
