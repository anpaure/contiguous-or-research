# `k=17`: source audit and fail-closed static filter for atomic aligned `3+1` incidence-`C8`s

**Date:** 2026-08-02  
**Status:** proof-safe prelaunch audit.  No `C8` enumeration, SAT solve, or
heavy local computation is performed here.  The present sources contain an
exact physical factor replay and a complete **star** generator, but they do
not yet contain the octahedral generator or the immutable manifests needed
to certify a literal aligned role-relocating `3+1` packet.  Missing manifest
data must return `UNKNOWN`, never `PASS` or a no-go.

## 1. Scope correction

The frozen round-02 object is the dual fan whose two owner masks are

\[
        s=115442,\qquad t=115186.
\]

The labels `3669,3670` are legacy piece numbers, not immutable socket keys.
The exact source already recovers their current pieces from the owner masks,
which is the correct convention.

The existing Lane-L single-move census proves only that no move in its
declared face creates a new provider of lower colour `114930` while retaining
its other filters.  It does **not** exclude a socket escape which leaves the
degree of `114930` unchanged, moves a forced endpoint role, or changes a
joint tail--head--colour atom.  Consequently no statement that a higher-order
move is necessary is licensed until the separate one-cut socket-escape audit
is complete.  The atomic `C8` face below is nevertheless a valid, incomparable
correlated face.

## 2. Audited source inventory

The relevant frozen sources and their SHA-256 digests are:

| source | SHA-256 | exact content | missing content |
|---|---|---|---|
| `scratch/audit_k17_dense_refinement_c6_single_20260801.cpp` | `542c5fe23d681d3f9fdd852931753f20d6b0cc7712b5717e83059fc0e0082e75` | authenticated selected factor, protected incidences, component reconstruction, changed-path replay, degree at most two, owner partition, internal `D3` run test, relaxed q1 atom rebuild | literal age/predecessor state and protected-successor recurrence |
| `scratch/census_k17_zerozero_bowtie_c6c8_20260801.cpp` | `9718b8a48aed0eaeacd333265713593b420a3ddc760aeac265f349fa955e9f86` | `TargetMove`, affected-piece rebuild, exact old/new atom deltas, rank-10 delta, matching projections, complete star `C8` generator | octahedral `C8`, directed `3+1`, immutable roles, joint dependency manifests |
| `scratch/census_k17_round02_socket_rank_c6c8_exact_20260802.cpp` | `cb2f1dc5ca86db3d04d3841e9e26202c26acc2bc547f217deed618c5e4add21f` | current-mask dual-fan locator; exact direct/rainbow/endpoint classification after physical replay | octahedral `C8`; generic role relocation; literal directed `3+1`; age successors |
| `scratch/threadD_k17_round02_dualfan_c6c8_20260801.cpp` | `1f0e3a9aa9e4389aa4ad689bd67c78b0c10e96066511000773abf0f5b9fd3e5a` | targeted star/C6 dependency prefilter | joint `C8` cone; immutable role and successor manifests |

Two source-level distinctions are essential.

1. `score_target` is an exact replay of the declared selected incidence
   toggle and is strong enough for the owner/degree part of the static
   filter.  Its `path_d3_resident` predicate is only an internal positive-run
   test; it is not the literal age recurrence required by the `C8` launch
   theorem.
2. `endpoint_role_relocation` in the round-02 source means that one of the
   two owner masks ceases to be an endpoint or the two endpoint paths merge.
   This is a useful dual-fan event, but it is not the generic immutable
   forced-role predicate in the `3+1` specification.

No file in the current round-02 catalogue is an authenticated
`age_successor_manifest` or a complete immutable `role_manifest`.  Thus a
current-source row cannot yet be labelled a **literal** role-relocating
`3+1` `C8`.

## 3. Exact two-family `C8` normal form

Let indices be in `Z/4Z`, and let `a_0,a_1,a_2,a_3` be distinct coordinates.
There are exactly two Boolean incidence-`C8` families.

### 3.1 Star family

For a rank-seven core `S`, put

\[
 L_i=S\cup\{a_i\},\qquad
 O_i=S\cup\{a_i,a_{i+1}\}.
\tag{3.1}
\]

Then `L_i` is incident with `O_i` and `O_{i-1}`.

### 3.2 Octahedral family

For a rank-six core `S`, put

\[
 L_i=S\cup\{a_i,a_{i+1}\},\qquad
 O_i=S\cup\{a_i,a_{i+1},a_{i+2}\}.
\tag{3.2}
\]

Again `L_i` is incident with exactly `O_i` and `O_{i-1}` inside the
octagon.  Thus both families use the same alternating toggle:

\[
 \begin{array}{c|cc}
 \epsilon&\text{removed at }L_i&\text{inserted at }L_i\\ \hline
 0&O_i&O_{i-1}\\
 1&O_{i-1}&O_i.
 \end{array}
\tag{3.3}
\]

The core and petal four-set are uniquely recoverable within each family.
There are three cyclic petal orders modulo reversal and two phases, hence

\[
 {17\choose7}{10\choose4}\,3\,2
 ={17\choose6}{11\choose4}\,3\,2
 =24,504,480
\tag{3.4}
\]

keys in each family and `49,008,960` total.  A numeric id is therefore
unambiguous only together with the family tag.  The existing `make_c8`
implements (3.1) only.

## 4. The exact static filter

Fix an authenticated occurrence-labelled selected factor `F`.  For every
selected incidence retain the immutable key

\[
      e=(\text{lower mask},\text{owner mask}),                 \tag{4.1}
\]

its component-cycle occurrence, directed position, endpoint side, and every
declared role/successor/dependency label.  For a family/order/phase key `Q`,
construct the four removed keys `e_i^-` and four opposite inserted keys
`e_i^+` from (3.1)--(3.3).  The proof-safe filter consists of the following
six gates.

### G1. Active opposite matching

Every `e_i^-` is selected in `F`, no `e_i^+` is selected, and no `e_i^-` is
protected against removal.  The eight immutable incidence keys are written
to the output row.  Mask membership alone is insufficient.

### G2. Degree and owner preservation

Apply all four changes atomically.  Each `L_i` and each `O_i` loses one and
gains one incidence algebraically; the exact physical replay must additionally
verify no duplicated incidence, degree at most two, the same owner set once
each, and the declared path/cycle class.  Intermediate one-, two-, or
three-edge subsets are irrelevant and must not be screened.

### G3. Literal directed `3+1`

Locate the four removed **incidence occurrences** in the old factor.  Their
component multiplicities must be `[3,1]`.  On the repeated component, record
the three immutable incidence keys in its authenticated direction and compare
their cyclic index word with the declared aligned word for the family,
phase, and role orientation.

The current theorem notes do not define a phase-only global direction for a
factor cycle.  Therefore the safe implementation stores the expected word in
an authenticated alignment manifest and tests equality there.  Sorting the
three positions, accepting either direction, or comparing numeric component
ids would enlarge the class and is not a certificate for the declared
directed face.

### G4. Immutable role relocation

Let a forced role be keyed by its occurrence/endpoint fingerprint, including
the load-bearing incidence, endpoint side and any other slots participating
in the role atom.  Rebuild the new factor and compare the old and new role
keys.  Acceptance requires the declared role to change or become internal in
the exact sense specified by the role manifest.  A changed component number,
an affected piece, or disappearance of an unrelated endpoint is insufficient.

For the particular round-02 dual fan, the current endpoint-mask test is a
sound **sufficient** event only for the explicitly declared socket role; it
does not replace this generic gate.

### G5. Literal age and protected successors

Replay all four new turns against an authenticated age/predecessor manifest.
Each turn must satisfy the literal age recurrence, and every protected
successor incidence touched by the packet must remain present in its required
state.  The internal run predicate and the boolean `protected` field on old
incidences do not imply this gate.

### G6. Complete dependency cone

For every stored core `K`, its cone `D(K)` must include load-bearing
occurrences, provider footprints, capacities, guards, blockers, role atoms,
protected successors, and all joint endpoint--endpoint,
endpoint--colour, and tail--head--colour hyperedges.  Compute the before/after
truth value of each declared datum under the atomic packet.  A packet may be
rejected by persistence only when a complete stored trace is literally
unchanged.  `affected_pieces` is a safe broad prefilter but is not the joint
reverse cone.

### Proposition 4.1 (static-filter exactness)

Assume the selected-factor, alignment, role, age-successor, and complete
dependency manifests are authenticated and complete for the declared face.
Then gates G1--G5 accept exactly the atomic aligned role-relocating literal
`3+1` simple `C8`s in that face; G6 gives exactly the trace-persistence
rejections relative to the declared core library.

#### Proof

Equations (3.1)--(3.3) classify every simple Boolean incidence `C8` and give
its unique opposite matching.  G1 and G2 are precisely physical activity and
atomic factor preservation.  G3 is the definition of the aligned directed
`3+1` subface on immutable occurrences.  G4 and G5 are respectively the
declared role and literal-successor predicates.  Completeness of `D(K)` makes
the contrapositive persistence test in G6 exact: if no datum in the cone
changes, the stored trace remains; if a declared trace datum changes, its
before/after row records the witness.  No inference about q1 feasibility is
made.  \(\square\)

## 5. Required output and fail-closed statuses

Every generated row should contain at least:

* family, core, cyclic petal order, phase, and a family-tagged id;
* all four removed and four inserted immutable incidence keys;
* the four old component fingerprints, the repeated component fingerprint,
  its three directed positions, observed order, and expected aligned order;
* old/new immutable role keys and the exact relocation witness;
* the four age-recurrence rows and every protected-successor before/after row;
* every changed entry of every intersected `D(K)` with its joint context; and
* exact physical rebuild statistics.

The only proof-safe terminal statuses at this stage are:

* `REJECT_Gj`, accompanied by a replayable witness for failed gate `Gj`;
* `PASS_STATIC_FILTER`, only when all six manifests are present, authenticated,
  and every gate passes; or
* `UNKNOWN_MISSING_MANIFEST` / `UNKNOWN_MANIFEST_DRIFT` when a needed declared
  datum is absent or does not authenticate.

After a complete library scan, a statically passing packet may be labelled
`CAUSAL_OPEN_NOT_Q1_VERDICT` or `LIBRARY_OPEN_NOT_Q1_VERDICT`.  Syntactic
`OPEN_MANIFEST` is not semantic q1 feasibility.

## 6. Sharp surviving gate

The existing source is reusable rather than obsolete:

* `make_c8` plus the physical factor replay already proves G1 and the main
  part of G2 for the star family;
* the octahedral formula (3.2) is a direct second generator using the same
  atomic replay; and
* the dual-fan endpoint classifier is a useful target-specific downstream
  row.

What is **not** yet proved is the complete static catalogue of literal
aligned role-relocating `3+1` `C8`s.  The exact missing inputs are the
octahedral generator, the directed-alignment manifest, the immutable role
manifest, the literal age/protected-successor manifest, and the complete
joint dependency cones.  Until these exist, the strongest correct result is
a formal incidence/owner replay with `UNKNOWN` at the missing literal gates.
This leaves the one-cut non-`114930` socket escape and the atomic `C8` lane
both live; it does not justify calling a higher-order move necessary.
