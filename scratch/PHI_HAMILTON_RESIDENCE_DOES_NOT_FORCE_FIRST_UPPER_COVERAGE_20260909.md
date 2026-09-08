# Fixed Phi, Hamiltonicity and residence do not force higher-rank coverage

2026-09-09. A bounded exact diagnostic by `exact_b_finite_frontier`, with
complete source review by root and `exact_equality_structure` before its
one H100 execution. The first qualifying example was subsequently checked
by a full materialized replay inside that run. No further candidate family,
retry, random search, or modification of the supplied optimal words was used.

**Result.** On 19 coordinates there is a Hamilton cycle through the two
complete middle layers which retains EVERY canonical outgoing Phi edge
and satisfies BOTH lower residence exclusions, but misses a rank11
target in its entire cyclic upper-interval OR family. Thus those structural
hypotheses do not imply even the first higher-rank coverage condition.

The example differs from the verified 19 carrier at just three incoming
matching assignments. Three is the smallest possible nonzero number of
changes to an incoming perfect matching in the middle-level incidence
graph. No minimality in the dimension is asserted.

## 1. The explicit counterexample

Take the already verified user word
[k19_optimal92381.word](../answers/k19_optimal92381.word), with raw SHA256

    1d0e7595dc72c6f1b7590e9565d5c0d3c30d70138e993d074e7d90d778d4e414.

Let M=92,378, C be its first M masks, and use cyclic subscripts in

    R_i=C_i union C_(i+1) union C_(i+2),
    U_i=R_i union C_(i+3)=Phi(R_i).

The [completed literal reconstruction](K19_OPTIMAL_LITERAL_PHI_CARRIER_PAIR_CHANGING_COMPILER_AND_QUOTIENT_CERTIFICATE_20260909.md)
verifies every rank-nine and rank-ten set exactly once and both residence
exclusions. The separate [full-word and cyclic certificate](../K19_K20_OPTIMAL_AND_CYCLIC19_VERIFIED_20260909.md)
establishes the complete upper coverage of this ORIGINAL carrier.

Put a=7,898, b=53,069 and c=78,118. Reorder the lower cycle as

    R' = R[:a] + R[b:c] + R[a:b] + R[c:].               (1.1)

All slice indices in(1.1) are zero-based and right-exclusive. At every
new lower state keep its canonical outgoing upper U'=Phi(R'). The three
changed successor edges, expressed in ORIGINAL lower-state indices, are

    7,897 ->53,069,
    53,068->78,118,
    78,117-> 7,898.                                   (1.2)

The affected incoming lower labels are

    R_7898=44363,  R_53069=175433,  R_78118=109897.

These are one recorded three-cycle of the difference between the actual
and native incoming matchings: source circuit 201, deterministic family
index 100. Reverting only this cycle gives (1.2). Every other incoming
incidence stays as in the original verified carrier. Formula(1.1) also
shows directly that the result is one cycle, not three disconnected cycles.

The fully replayed result has:

* 92,378 distinct rank-nine lower states and 92,378 distinct rank-ten uppers;
* U'_i=Phi(R'_i) and R'_i union R'_(i+1)=U'_i for EVERY i;
* U'_(i-1) intersect U'_i=R'_i for EVERY i;
* single-coordinate lower insertions b_i and deletions d_i, with
  b_i!=d_(i+1) and b_i!=d_(i+2) for EVERY i;
* exactly 75,581 distinct rank11 adjacent-upper unions, one short of
  binom(19,11)=75,582.

The absent target is

    T=109931={1,2,4,6,7,9,11,12,14,16,17},             (1.3)

where the set uses one-based coordinates. No original optimal word is
being refuted: the newly reordered carrier deliberately loses this target.

The two literal cycle files are retained:

* [Lower cycle](k19_phi_upper_three_circuit_diagnostic_20260909/counterexample_lower_cycle.word),
  SHA256 `4037dd78d59f42f73867cc857bdeb5aa268872b204dff00b0dcb8ce5801db4b7`.
* [Upper cycle](k19_phi_upper_three_circuit_diagnostic_20260909/counterexample_upper_cycle.word),
  SHA256 `daeaf0e1d4d5caba98c95012f2fb13296625e733928342951461f32dc0a2cb88`.

## 2. Why the missing pair color is a missing interval target

In any middle-level cycle of this form, consecutive distinct uppers of
rank r+1 intersect in the intervening lower r-set. Their union therefore
has rank r+2. For a target T of rank r+2, the following are equivalent:

    T occurs as a cyclic interval union of upper owners;
    T occurs as a union of two consecutive upper owners.              (2.1)

A one-owner interval has too small a rank. An interval of at least two
owners whose union is T has two consecutive owners contained in T;
their union has rank r+2 and must equal T. The converse is immediate.
This also covers intervals longer than one period: they cannot avoid
the same consecutive-pair condition.

The full replay checks an even more explicit absence certificate. All 11
rank-ten subsets of(1.3) occur, since the upper layer is complete, but
every one is isolated among the upper owners contained in T. Their
positions in the EXPORTED counterexample upper cycle are

    4231,32946,39398,43849,45407,48207,
    51736,58607,65690,67812,78118.

At each position the preceding AND following upper masks contain a
coordinate outside T. The complete eleven-row certificate records those
outside masks explicitly. Thus there is no interval of two or more
owners entirely contained in T, and no interval of any length with OR T.
The conclusion is not inferred merely from an unexamined palette count.

Only three adjacent-upper colors change. Their multisets are

    before: 109931,241001,437579;
    after:  175467,241001,372043.

The baseline census includes every rank11 target. Applying the exact
three-edge count update loses 109931 and no other rank11 target; the
independent full replay reconstructs the new 75,581-color palette and
checks the explicit target absence. No statement about which still-higher
targets survive is needed or claimed.

## 3. Three incoming changes are minimal in this comparison

The middle incidence graph joins an r-set R to an(r+1)-set U containing
it. It has no four-cycle: two distinct r-sets that share an(r+1)-superset
must have union of size r+1, and that union is their ONLY such common
superset. Hence they cannot share two distinct upper neighbors.

The symmetric difference of two distinct perfect matchings is a disjoint
union of alternating even cycles. A nontrivial component therefore has
at least six edges, or three lower vertices. Thus changing one or two
incoming assignments cannot produce another perfect matching. The
counterexample changes exactly three. This is minimal modification size
relative to the baseline matching, not a minimum-dimension assertion or
a claim about the smallest counterexample among all mathematical models.

## 4. Exact diagnostic and independent replay scope

The tested family was fixed before execution: all 1,216 recorded
length-three incoming-matching difference circuits, ordered by their
stored lower-label triples. Each is reverted independently on the ORIGINAL
carrier. No trial uses the result of another trial.

One baseline upper-pair census is sufficient: a three-circuit changes
exactly the three successor edges in its support. The resulting rank11
counts are the old full counts minus those three old colors plus their
three replacements.

Topology is tested exactly by cutting at the three affected heads. The
three unmodified arcs partition the whole original cycle. Their new
connections form a permutation of these three arcs, whose cycle count
is precisely the new full component count. Adjacent cut heads still give
nonempty one-state arcs and cause no exceptional case.

The local residence test is also complete. A newly failing three-edge
test must encounter a changed successor edge. Its start is therefore
within two NEW predecessors of a changed tail. The code tests every such
start, plus the old predecessors as harmless redundancy. Every other
new test equals a previously verified baseline test.

The complete fixed-family outcome was:

|Condition|Candidates|
|---|---:|
|Tested|1,216|
|Hamiltonian|494|
|Both residence exclusions|969|
|Hamiltonian and both exclusions|361|
|Those also losing a rank11 target|19|

After ALL candidates were recorded, the first qualifying one was
materialized as a full successor permutation and traversed from original
state 0. The replay rechecks every lower and upper label, canonical Phi,
every incidence, every residence test and the entire new rank11 palette.
The eleven isolated containment positions then exclude every longer
upper interval as in Section2. This replay does not rely on the local
screening verdict or the abstract three-arc topology test.

The [standalone source](diagnose_k19_phi_upper_support_three_circuits_20260909.py)
has SHA256

    5b11d71a35ca70695daea0db915224f79e1c1e3053efd6ef7e4d2b720e449702.

Root and `exact_equality_structure` passed full source reviews before
execution. All four inputs were pinned: original word, native canonical
data, recorded circuits, and completed structural report. Their hashes
and byte lengths appear in the
[complete result](k19_phi_upper_three_circuit_diagnostic_20260909/complete_diagnostic_certificate.json).
The [full replay](k19_phi_upper_three_circuit_diagnostic_20260909/counterexample_full_replay.json)
and [every candidate outcome](k19_phi_upper_three_circuit_diagnostic_20260909/all_1216_candidate_outcomes.json)
are retained beside it, together with an executed source snapshot.

One h100/arboghast process ran with 60 CPU seconds, 90 wall seconds and
2 GiB address space, finishing in 0.743687366 CPU seconds and
0.7441049250774086 wall seconds. No limit was reached. All outputs and
the executed source were copied locally; no retry or expanded family ran.

## 5. Consequence for the all-dimension construction gate

The canonical corridor in
[PBBS Section21.2](../PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md)
proves particular g=f^2 arrows using both forward and reverse unmatched
marks. It cannot be transferred to an arbitrary incoming matching merely
because its outgoing Phi matching and residence remain intact. The
counterexample is a direct failure of that proposed stronger conclusion.

This carrier also has a nonempty four-window antecedent; lack of a source
is not the issue. A one-position zero gap in a lower-coordinate run would
make the two neighboring upper owners equal, contrary to their bijection.
Thus lower zero gaps have length at least two. The residence conditions
make every lower positive run have length at least three. Since
U'_i=R'_i union R'_(i+1), upper positive runs have length at least four.
Coordinatewise erosion and dilation therefore give, for

    E_i=U'_(i-3) intersect U'_(i-2) intersect U'_(i-1) intersect U'_i,

    E_i union ... union E_(i+3)=U'_i,
    E_i union E_(i+1) union E_(i+2)=U'_(i-1) intersect U'_i=R'_i.

Each E_i is nonempty: consecutive rank-ten uppers differ by one element,
so their fourfold intersection has size at least 10-3=7. These statements
are the elementary run-length proof, not another executed source census.

The obstruction persists through a lower-cap compiler that freezes this
flat middle chronology. If a cyclic source has every four-letter window
equal to the prescribed U'_i, every interval of length at least four
is exactly the union of its consecutive four-window owners. Every shorter
interval is contained in a four-window owner and has rank at most10.
Consequently the absent rank11 target T cannot be supplied by ANY cap
changes that preserve those four-window owners. A different source or
middle chronology can repair it; unrestricted optimality is not obstructed.

There is a concise exact way to retain the first-higher obligation in a
future incoming-matching formulation. An admissible incoming incidence
U->R, with R subset U and U!=Phi(R), has color

    color(U,R)=U union Phi(R), of rank r+2.            (5.1)

A selected incoming perfect matching covers the first higher rank exactly
when every(r+2)-set appears as at least one selected edge color. These
color-cover constraints must accompany the degree, component and residence
conditions; the counterexample shows they cannot simply be dropped.
This is an exact encoding observation, not a new integral Hall theorem.
An ordinary matching flow does not automatically enforce these additional
color requirements, and first-higher coverage alone has not been proved
to imply every still-higher rank.

The verified17 two-cycle bank and19 universal cycle remain valid positive
examples with separately checked higher support. The present finite counterexample
removes an invalid simplification of their all-dimensional existence gate;
it does not negate those examples or establish an impossibility of an
all-dimensional exact constructor.
