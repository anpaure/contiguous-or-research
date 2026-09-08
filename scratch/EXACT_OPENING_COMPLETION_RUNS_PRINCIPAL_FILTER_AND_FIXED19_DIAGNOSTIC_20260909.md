# Exact opening from completion runs and one principal upper filter

2026-09-09. Pure proof and one completed fixed-phase diagnostic by
`exact_equality_structure`. The root-authorized single run passed;
complete results and provenance are in Section7.

The ordinary and truncated witness-core theorems already exist. This
note makes their coordinate/run data explicit and reduces the supplied
nineteen-coordinate opening to 255 specified targets. It does not infer
a safe opening from Phi, middle-layer counts, or witness multiplicities.

## 1. Prior results and the correct general scope

Read before deriving this record:

* MASTER_HANDOFF Section3.8, especially (3.37) and (3.40);
* `MATH_THEOREM_CYCLIC_RECUT_WITNESS_CORE_AND_BPLUS1_BOUNDARY_GATE_20260801.md`,
  Sections1–4: the complete witness-interior core and its scope;
* `MATH_THEOREM_BPLUS1_ALLWIDTH_RAINBOW_WITNESS_BANK_AND_SAFE_OPENING_20260803.md`,
  Sections1–2: maximal compatible blocks, cores, and retained-witness
  selection without assuming uniqueness;
* `MATH_THEOREM_L_RESET_OPEN_PATH_EXTERIOR_SAFE_CUT_BLOCKER_MINMAX_20260801.md`,
  Sections1–3: exact blocker loads, multiple suppliers, and limitations
  of average multiplicity statements;
* `MATH_THEOREM_PBBS_SOURCE_OPENING_PENETRATION_AND_HEIGHT_STAIRCASE_20260805.md`,
  Sections1–3: exact source/owner overhang, truncated cores and staircase;
* `scratch/UNIFORM_CYCLIC_MIDDLE_WINDOW_CAPACITY_AND_OPENING_OBSTRUCTION_20260909.md`:
  short-target capacity and the remaining longer-upper opening gate.

Uniform middle-window length is AUTOMATIC for a universal cyclic word
of exact width, by MASTER (3.40); it is not an extra freely imposed
architecture assumption. For odd n=2r+1, its rank-r windows have one
length q and its rank-(r+1) windows have length q+1. The latter follows
because every endpoint must serve rank r+1, so its first window longer
than q cannot skip that rank. The counting condition forces q to grow
with r. A fixed triple compiler is therefore not an all-dimensional
family merely because the instances17 and19 succeed.

The general linearization (3.37) appends disjoint first-occurrence blocks
outside a largest final letter. It preserves all cyclic targets using
at most n-max|C_i|-1 extra positions. The principal-filter size below is
a number of TESTS for a shorter prefix-copy opening, not a proposal to
repair each test with one extra letter. For the supplied19 period with
largest letter rank seven, that old unconditional repair costs at most
eleven positions; the successful prefix opening costs three.

## 2. Complete compatible runs and all minimal witnesses

Let B=(B_0,...,B_(m-1)) be any cyclic word whose total union is the ground
set. Fix a proper target T with at least one cyclic interval witness.
Call a maximal consecutive run of letters contained in T a T-compatible
run. These are exactly the components remaining after removing every
position carrying a coordinate outside T. A compatible run is COMPLETE
if the union of all its letters is T.

Every T-witness lies in a complete compatible run, and every complete
run is itself a witness. An inclusion-minimal witness has neither a
redundant first letter nor a redundant last letter. Every witness
contains one, by successively deleting redundant endpoints. Thus only
these minimal intervals are needed for any retained-witness test.

For a fixed linear complete run [a,b], define for each x in T

    first(x)=its first occurrence in that run,
    last(x)=its last occurrence in that run,
    f=max_(x in T) first(x),
    l=min_(x in T) last(x).                                  (2.1)

Then f is the earliest possible right endpoint of a T-witness, and l
is the latest possible left endpoint. Indeed [a,f] and [l,b] cover T;
ending earlier misses a coordinate attaining f, and starting later
misses a coordinate attaining l.

Consequently the intersection of the internal entering-edge sets of
ALL witnesses in this run is exactly

    {l+1,...,f}, if l<f; otherwise empty.                    (2.2)

One does not need a unique witness. Formula (2.2) follows because every
witness starts at most l and ends at least f, while the two extremal
witnesses above attain those bounds. The same extrema are attained
among inclusion-minimal witnesses.

If two distinct compatible runs are complete, their witness interiors
are disjoint and the target's global core is empty. If exactly one run
is complete, (2.2) is its global core. These cases make the old compatible-
block core theorem explicit in coordinate first/last data.

### Complete minimal-witness enumeration

At each right endpoint in one compatible run, keep the LATEST start
whose interval covers T. This is done by advancing the left endpoint
while all coordinates in its letter still have another occurrence in
the current interval. The resulting interval is minimal at its left
end. It is also minimal at its right end exactly when this latest start
strictly exceeds the previous endpoint's latest T-covering start, or
when it is the first covering endpoint.

For if the latest start is unchanged, the previous ending interval
already covers T, so the last letter is redundant. If the start has
increased, the previous endpoint has no T-covering suffix at that new
start or later, so the last letter is indispensable. Every minimal
witness must have this unique latest start at its endpoint. This gives
ALL minimal witnesses, not merely one shortest witness per target.

## 3. Literal prefix collars: an exact erosion of the core

Open B at the edge entering index c and append the next q periodic
letters, where 0<=q<m. A proper cyclic witness fails to occur in the
opened word precisely when its interior includes the WHOLE directed
edge arc

    K_q(c)={the edges entering c,c+1,...,c+q}.                (3.1)

To see this at c=0, a failed witness must wrap and finish at index at
least q of the next copy. It then traverses all q+1 edges in (3.1).
Conversely those edges force exactly that unsupported overhang.

Therefore a target is lost precisely when K_q(c) lies in the intersection
of all its witness interiors. For a sole complete compatible run with
coordinates (2.1), the fatal opening positions are exactly

    c in {l+1,...,f-q},                                 (3.2)

in the run's unwrapped chart. Empty intervals give no fatal cut. If
there are two complete runs, every opening is safe for this target.
The full-ground target is always supplied by the full original period.

This is the source-level form of the already proved truncated-core
calculus. It is not a new union-of-bad-cuts theorem. Its useful point
here is that the whole targetwise obstruction can be recovered from
complete runs and two coordinate occurrence extrema.

## 4. A q-letter opening reduces to one owner edge and its upset

Let C be a universal cyclic word of exact width M on n=2r+1, and let q
be its automatic rank-r witness length. Set

    U_i=OR(C_i,...,C_(i+q)).                              (4.1)

The U_i enumerate the rank-(r+1) layer once. The proposed opening

    A=C_0,...,C_(M-1),C_0,...,C_(q-1)                    (4.2)

contains exactly the ordinary owner line U_0,...,U_(M-1).
All targets of rank at most r+1 already retain their short witnesses.
Every higher source witness is a union of consecutive U owners, by
associativity, so its opening problem is exactly the zero-collar
opening of this owner cycle at U_(M-1) -> U_0.

Put

    V=U_(M-1) union U_0.                                 (4.3)

Every higher target lost at this opening must contain V: every lost
owner witness crosses that edge and contains both endpoint owners.
The adjacent owner intersection is the rank-r window at index0, so
|V|=r+2. Thus only

    T with V subseteq T proper subset of [n]              (4.4)

need examination. There are 2^(r-1)-1 such targets. This test count
is independent of M; it does not claim those targets are lost or charge
an individual repair for each.

The precise sufficient-and-necessary edge-local condition is:
for every T in (4.4), either the compatible owner run crossing the cut
is incomplete, another complete run exists, or the sole complete
crossing run has f before the cut or l on/after the cut. Equivalently,
one of its two extremal one-sided witnesses survives.

If the condition fails, there are coordinates x,y in T such that x
occurs only after the cut and y only before it within that unique
complete run. This is a named coordinate-separation obstruction,
not merely a low total witness count. Conversely a sole complete
crossing run whose two sides both miss some coordinate is fatal.

The condition allows arbitrary witness multiplicities and does not
require preserving a designated long witness. It can be passed to an
induction as a port obligation on the one principal filter (4.4).
Its satisfiability is additional to the prescribed matching and the
middle-window conditions.

## 5. A genuinely sufficient pair-cover property, with its limitation

Here is one alternative structural sufficient condition. For each
proper T in the relevant principal filter, suppose either:

* T has at least two complete compatible owner runs; or
* within its sole complete run, every coordinate pair {x,y} subseteq T
  occurs together in at least one owner of that run.

Then every opening edge is safe for each such T, in particular the
specified edge. In the second case a nonempty core would give a cut
between l and f, and coordinates x,y lying entirely on opposite sides
of that cut in the run. No one owner could contain both, contradicting
the pair-cover hypothesis.

This asks for a two-coordinate shadow property inside complete runs,
not uniqueness or transport of every upper witness. It is sufficient
but not necessary. For example repeated singleton letters can give two
disjoint witnesses for a two-coordinate target inside one compatible
run although no individual letter contains that pair.

The full middle layer supplies every rank-(r+1) subset of T somewhere,
but those occurrences need not lie in a COMPLETE T-run. Therefore the
pair-cover hypothesis does not follow from middle-layer bijectivity.
The definition of Phi specifies one incident matching and likewise
does not supply this placement statement. No automatic safe-opening
theorem from Phi plus the already universal cyclic core has been proved
here. A separate diagnostic showing that Phi, residence and middle
coverage can fail upper coverage concerns the weaker premises and does
not settle this question for already universal cores.

## 6. Reviewed inspection of the one supplied19 cut

For the supplied19 literal, q=3 and M=92378. The V in (4.3) has rank11,
so exactly255 proper targets (4.4) are relevant. The reviewed source
is

    scratch/inspect_k19_single_supplied_cut_255_upper_targets_20260909.py.

It pins the literal SHA, keeps the original phase throughout, and for
each of those255 targets enumerates every maximal compatible owner run
and every inclusion-minimal witness. It independently compares the
minimal-witness extrema with (2.1), classifies the actual reason for
survival, and replays one surviving ordinary witness both in the owner
line and in the actual source word C+C[:3]. The complete run and minimal-
witness records are saved even when many witnesses serve the same target.

The cap is60 CPU seconds,90 wall seconds,2 GiB and256 MiB per output
file. Root and frontier independently read the complete source and
passed it before root authorized execution. Induction subsequently also
passed its complete minimal-witness/run/extrema source review. No other
cut, word edit, generator, or optimization is inspected. The existing
actual19 safe opening was already verified by its literal full-word
certificate. This diagnostic identifies its run-based mechanism rather
than inferring safe opening from counts.

## 7. Actual supplied-cut certificate and one unsafe-phase consequence

The single h100/arboghast run completed PASS in4.022899 seconds. The
one fixed removed-edge color was

    V=384086, of rank11.

All255 proper targets containing V survived for the following exact
reasons:

| Fixed-cut survival reason | Targets |
|---|---:|
| The compatible run crossing the cut is incomplete | 229 |
| The crossing run is complete, but another complete run supplies T | 25 |
| The sole complete crossing run has a surviving left extremal witness | 1 |

Across those255 targets the checker reconstructed436,900 maximal
COMPATIBLE runs, of which12,840 were COMPLETE. These are different
counts. It enumerated all20,827 inclusion-minimal witnesses;20,807
are retained at the supplied cut. Each target received one directly
replayed ordinary owner witness and its actual source witness.

The unique target in the last row is

    T=515158, of rank12.

It has53 compatible runs and exactly one complete run. In the unwrapped
owner chart this sole complete run is [92375,92378] inclusive. Its two
minimal owner witnesses are

    [92375,92377] and [92376,92378] inclusive.

The independently computed coordinate extrema are

    f=92377,  l=92376,
    forced entering-edge core={92377}.

The supplied cut is at92378 congruent to0, so it retains the first
witness. Its zero-based, right-exclusive actual source interval is

    [92375,92381),

the last six letters of the supplied linear word. The other minimal
witness crosses the supplied cut.

There is a useful PURE CONSEQUENCE of this already computed core: the
three-letter prefix opening of the same cyclic source at phase92377
would lose T. Every owner witness of T traverses the entering edge92377.
No second cut was searched, evaluated, or replayed; the conclusion is
the exact core theorem applied to the saved complete witness family.
Thus this actual universal Phi-containing core is not safe at every
phase, even though its supplied phase is safe. This does not refute
existence of some safe phase for a general universal cyclic width core.

Complete local artifacts are in
[`scratch/k19_fixed_cut_255_20260909/`](k19_fixed_cut_255_20260909/).
All copied JSON/JSONL files passed the remote SHA-256 manifest locally.
The executed source and execution log are retained.

* Source snapshot `checker.py` SHA-256:
  `ac22b980ff3f3b1d079324159e8d1a0acc3514ec3265f568474a4cd87ca11af6`.
* [Full certificate](k19_fixed_cut_255_20260909/single_cut_255_target_certificate.json)
  SHA-256:
  `c5e6ae8fa557e80ccdfb27ec454da40f79bfc31bd357614170c59bc7c739e032`.
* [Every run and minimal witness](k19_fixed_cut_255_20260909/all_255_run_and_minimal_witness_records.jsonl)
  SHA-256:
  `b98a58eb955533ad2634f035efc6ca224b6df3de28f0c024b31df2c45bac2754`.

The immutable input literal SHA-256 was
`1d0e7595dc72c6f1b7590e9565d5c0d3c30d70138e993d074e7d90d778d4e414`.
No limit was reached, no retry ran, and no mathematical process remains
live. These data certify the stated cut-specific mechanism; they do
not supply an all-dimensional safe-port existence theorem.
