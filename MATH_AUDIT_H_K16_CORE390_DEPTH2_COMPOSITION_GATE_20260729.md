# Lane H audit: the detector-zero core390 depth-two composition gate

Date: 2026-07-29

## 1. Frozen objects

Let (Q_0) be the physical q1-exact factor in

```text
scratch/k16_q1_endpoint_resume1_failedlit0_20260729.json
SHA-256 17bd05a0bb0da228e580d65bdec27ce04589072baecb8575e0623fc4ea4343b8
```

and let (P) be the fixed resident factor with SHA-256

```text
d28491b708d5a83e8abcde20fda8ad523cd58f9c662f46ae2d9c2507ba73e951.
```

The deletion-minimal guarded core is

```text
scratch/k16_failedlit0_guarded_q1_motif_core_20260729.json
SHA-256 2f8031fff879faf42b80a169aee2f0a0f5a2484987c5fe625c20fc5bf945c238.
```

It has eight lower-q1 rows, thirteen upper-q1 rows, and the single motif
row 390.  Its physical closure is

\[
C=\{(57902,57998),(57902,61994),(57998,58250)\}.
\]

## 2. Exact fixed-core detector

For a q1-exact middle-level 2-factor (Q), define the core390 detector as
follows.  If (C\not\subseteq Q), set \(\Delta_{390}(Q)=0\).  Otherwise put

\[
B=Q\setminus P,\qquad R=P\setminus Q,
\]

and introduce removal variables (x_b), (b\in B), and addition variables
(y_r), (r\in R).  Impose

\[
\sum_{r\ni v}y_r=\sum_{b\ni v}x_b \quad\text{for every vertex }v,
\]

all physical lower- and upper-q1 coverage inequalities computed from (Q),
and

\[
\sum_{c\in C}x_c\ge 1.
\]

Set \(\Delta_{390}(Q)=0\) when this system is feasible and set it to one
when it is proved infeasible.  An unresolved finite solve is neither value.

**Theorem 2.1 (detector equivalence).**  If (C\subseteq Q), then
\(\Delta_{390}(Q)=0\) if and only if there is a q1-complete 2-factor in
(P\cup Q), with every edge of (P\cap Q) frozen, that omits at least one
edge of (C).

**Proof.**  Starting from the degree-two factor (Q), replacing the selected
blue edges by the selected red edges preserves degree two exactly when the
displayed vertex equalities hold.  The lower and upper inequalities say
exactly that every physical q1 colour remains represented.  The last row says
that at least one closure edge is removed.  Conversely, subtracting (Q)
from any such factor gives the variables and all three families of rows.
Edges common to (P) and (Q) have no variable and are therefore frozen.
\(\square\)

The three closure edges form the physical path

\[
61994-57902-57998-58250.
\]

Coordinate 2 has values (0,1,1,0) on these four vertices, so all three
edges present is exactly the fixed length-two short-run obstruction.  The
artifact

```text
scratch/k16_failedlit0_motif390_only_core_20260729.json
```

proves \(\Delta_{390}(Q_0)=1\): degree, every q1 row, and this one motif row
are already infeasible.

This detector is deliberately local to the fixed (P\cup Q) circulation.
Detector zero does not prove all-motif residence, connectivity, compiler
readiness, or feasibility after allowing arbitrary Johnson edges.

## 3. The complete row carrier

Every rank-seven lower colour (L) has exactly

\[
\binom{9}{2}=36
\]

middle-level Johnson providers, namely

\[
\{L\cup\{a\},L\cup\{b\}\},\qquad
\{a,b\}\in\binom{[16]\setminus L}{2}.
\]

Every rank-nine upper colour (U) similarly has the 36 providers

\[
\{U\setminus\{a\},U\setminus\{b\}\},\qquad
\{a,b\}\in\binom{U}{2}.
\]

A Johnson edge has a unique intersection and a unique union, so it occurs in
at most one selected lower fibre and at most one selected upper fibre.  For
the eight lower and thirteen upper core colours there are 756 incidences.
Exactly 24 edges lie in both a selected lower and a selected upper fibre.
Consequently the complete physical row carrier contains

\[
756-24=732
\]

distinct edges.  Relative to (Q_0), 21 are present deletion edges and 711
are absent addition edges.  The closure (C) is a subset of the present 21.
This census is frozen in

```text
scratch/k16_failedlit0_complete_core_q1_provider_catalogue_20260729.json.
```

Thus a signed packet ((D,A)) hits a guarded q1 row exactly when

\[
(D\cap F_{21})\cup(A\cap F_{711})\ne\varnothing.
\]

The separate 8,224-edge one-star catalogue is an optional enlargement;
edges outside the 732-provider set do not themselves hit one of the 21 q1
rows.

## 4. Exact local reduction to 61 deletion and 276 addition anchors

The core artifact serializes 33 current/resident provider edges on 41
vertices (V).  Let (S) be the set of all Johnson edges incident with
(V).  Direct counting gives

\[
|S\cap Q_0|=61.
\]

Among the 711 absent row providers, exactly 276 have both endpoints outside
(V).  These 276, together with the 61 current edges, form a complete signed
anchor family.

**Theorem 4.1 (local carrier reduction).**  Every degree-balanced packet
that hits one of the 732 row-provider edges, or its one-vertex degree halo,
either deletes one of the 61 current anchors or adds one of the 276 remote
anchors.

**Proof.**  A deleted present provider is incident with (V), hence belongs
to (S\cap Q_0).  An added provider disjoint from (V) is one of the 276
remote anchors.  If an added edge meets (v\in V), degree balance at (v)
forces at least one deleted (Q_0)-edge incident with (v); that edge lies in
the 61-set.  The same argument covers every added edge in the one-vertex
degree halo.  \(\square\)

The exact digests of the sorted compact edge lists are

```text
delete61 80424591c9cf2128af029ccdd8113383353095268182b1a5a577550f463ed6b8
add276   4cbb1c92ef77dedb84f2d3686c28ec2ffacd8b5164159bfdda5bedfc5e21de2a
union337 77960e3827d41f96a23a9ef50f8642a238bc8dc07dafe4952c26860a7b6738fd
```

## 5. Nonduplication theorem and current launch verdict

The newly landed Lane-R source

```text
scratch/search_k16_q0_core22_radius4_halo_20260729.py
```

uses the same (Q_0), the same 61+276 signed carrier, radii 2,3,4, and exact
q1 filtering.  Therefore regenerating a first packet in Lane H would exactly
duplicate R's single-halo job.

The admissible depth-two architecture is consequently:

1. import a hash-frozen, scope-complete R candidate union as depth one;
2. perform only new detector replay and two-packet composition;
3. preserve q1 literally after composition;
4. accept a final state only if its physical digest is absent from R's full
   one-packet digest union.

At the time of this audit no completed Q0 R report exists.  Moreover, the
available PLAN_ONLY file was generated from an older revision of the R
source.  Hence neither complete candidate coverage nor the final digest
exclusion can presently be certified.

**Corollary 5.1 (fail-closed launch decision).**  A detector-zero depth-two
process launched before a self-consistent complete R report is available
would violate the requested nonduplication condition.  No such process may
be launched from the present artifacts.

No heavy local enumeration, SAT call, or H100 process was run for this audit.

## 6. Bounded composition driver

The fail-closed implementation is

```text
scratch/search_k16_core390_rbank_depth2_composition_beam_20260729.py
SHA-256 82b74700c8b6bf22a3cad9b18bf15cb63ac1de72a9898009237a8c645b978776
```

with plan

```text
scratch/k16_core390_rbank_depth2_composition_beam_20260729.plan.json
SHA-256 dab125558bb819e817ccc6e210d8e2fc4e9aa610f9cd065a284ca403987ae8f3.
```

It accepts only provenance-matching complete R local shards, independently
replays Johnson incidence, degree balance and both q1 ledgers, and imports
their deduplicated packets without regenerating depth one.  A deterministic
target-diverse prefilter keeps at most 1,024 packets; exact core390 replay
retains at most 96; and the second layer examines at most

\[
\binom{96}{2}=4560
\]

unordered compatible pairs.  Hence at most 5,584 detector calls are made.
At two CPU-seconds per call the declared solver budget is at most 11,168
CPU-seconds.  `UNKNOWN` is not detector zero.  A final witness must pass an
independent q1 audit and be absent by both signed packet signature and
physical factor digest from the entire imported R union.

The independent driver audit passes at the displayed hash, conditional only
on the R input gate.  The enumeration-free size/overlap audit is

```text
scratch/k16_core390_depth2_size_overlap_audit_20260729.json
SHA-256 165f227a861f9796f1c326e11f31009d435cad3e8f3e30941ad7b6d700541aad
status WAITING_FOR_COMPLETE_R_REPORTS_DO_NOT_LAUNCH.
```

Its prospective envelope is one process, one worker, no GPU, a 16-GiB
address-space ceiling, an 8-GiB file-size ceiling, and six CPU-hours.  Since
the exact R inputs do not yet exist, no immutable launch package was built
and no remote process was started.
