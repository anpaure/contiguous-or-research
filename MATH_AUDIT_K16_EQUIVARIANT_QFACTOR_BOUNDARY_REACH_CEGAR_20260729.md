# Audit of the strict equivariant `k=16` quotient-factor boundary/reach model

Date: 2026-07-29  
Status: connected-model theorem **PASS**, with the disconnected boundary and
CEGAR-output qualifications in Sections 3--4; the connected/unit solve with
seed `16301` ended `UNKNOWN` and proves neither existence nor nonexistence.

Audited H100 source:

```text
/dev/shm/k15_rotation/scratch/k16_even_necklace_q1_factor_topres_20260729.py
SHA-256 24cdfa70cad22287bfaf371f5f65b843c37f334b0cf0fc7b0df93ffdf10faa6c
```

Its exact quotient catalogue has SHA-256

```text
e5ffa02199834c476f45b314b2eacfbaa1866a74895cc0aa4e12744c8d157ff3.
```

## 1. Quotient factor theorem

Let `G` be the middle-level graph on rank-eight subsets of `[16]`, and let
`rho` rotate the old coordinates `Z_15` while fixing the sixteenth coordinate
`z`.  The action is free on both old rank-eight owners and `z` plus old
rank-seven owners.  Hence the quotient has `429+429=858` vertices.

There are exactly `27456` undirected Johnson edge orbits: `12012` AA,
`12012` BB and `3432` cross.  Exactly 28 are quotient loops, 14 on each
same-shore sector.  A loop has two incidences at its quotient vertex.  Thus
the equations

\[
 \sum_{e\ni v}x_e=2
\]

with a loop counted twice are exactly the equivariant physical degree-two
condition.  The 764 lower and 764 upper first-shadow orbit rows are exact:
429/335 lower orbits occur without/with `z`, and 335/429 upper orbits occur
without/with `z`.  The two short old-rank-six/nine orbits have 12 quotient
providers; the other 762 colours have 36.  Selecting one provider of a short
orbit still covers all five physical targets, each three times.

## 2. Connected circuit and voltage

For every nonloop edge orbit `e={u,v}`, the model has two directed literals
`f_e,r_e` and imposes

\[
 f_e+r_e=x_e.
\]

All quotient loops are set to zero.  `AddCircuit` receives no self-loop
exclusion literal, so every one of the 858 quotient vertices lies on its one
selected directed circuit.  Parallel voltage-labelled arcs are legitimate.
Consequently the selected undirected edges form one spanning quotient cycle.

If the stored physical representative of `e` has endpoint phases `a,b`, its
forward voltage is `b-a mod 15`, and its reverse voltage is the negative.
Summing these directed increments is the exact monodromy of the quotient
cycle.  The physical lift has `gcd(15,v)` components.  Therefore the allowed
row

\[
 v\in\{1,2,4,7,8,11,13,14\}
\]

is necessary and sufficient for one physical cycle.  The option called
`unit_voltage` correctly means a unit modulo 15, not literally voltage one;
these are conjugate by an old-coordinate relabelling.

## 3. Exact top boundary/reach lemma

Write `b_v` for the Boolean boundary variable at quotient vertex `v`.  The
model imposes

\[
 b_v=\sum_{e\ni v,\ e\text{ cross}}x_e.                 \tag{3.1}
\]

Since `b_v` is Boolean, (3.1) both identifies a shore boundary and excludes
cross-degree two.  Thus a selected shore run cannot have one vertex.

For every same-shore incidence `(v,e=vu)`, introduce `r_(v,e)` with only the
lower implication

\[
 r_{v,e}\ge x_e+b_u-1,                                  \tag{3.2}
\]

and impose

\[
 b_v+\sum_{e\ni v,\ e\text{ same}}r_{v,e}\le1.          \tag{3.3}
\]

### Lemma 3.1 (correct connected scope)

On a loopless quotient 2-factor, (3.1)--(3.3) hold if and only if every
**proper** shore run (a run in a component containing both shore labels) has
length at least four.  In particular, on one spanning quotient cycle they
hold if and only if every cyclic run of each shore label has length at least
four.  They impose no condition on a monochromatic quotient component.

### Proof

A one-vertex run gives cross-degree two and violates (3.1).  A two-vertex
run has adjacent boundary vertices `v,u` joined by a selected same-shore
edge.  Then (3.2) forces `r_(v,e)=1`, while `b_v=1`, contradicting (3.3).
A three-vertex run has an interior vertex adjacent along its two selected
same-shore edges to two boundary vertices; both reach variables are forced
to one, again contradicting (3.3).

Conversely, suppose every proper shore run has length at least four.  Set a reach
variable to one exactly when its edge is selected and its opposite endpoint
is a boundary, and set every other reach variable to zero.  A boundary
vertex then has no boundary same-shore neighbour, and an interior vertex has
at most one boundary neighbour.  Hence (3.2)--(3.3) hold.  This proves both
necessity and sufficiency for proper runs.  A monochromatic component has
`b_v=0` throughout and admits all reach variables zero, regardless of its
length.  On a spanning quotient cycle both shore labels occur (there are 429
vertices of each type), so every run is proper.  The argument is cyclic and
includes the voltage closing seam.  ∎

The connected hypothesis is essential.  In this exact catalogue, the AA
triangle on quotient nodes `(0,1,8)` with edge orbits `(0,69,8)` has voltage
zero, and the BB triangle on nodes `(429,430,436)` with edge orbits
`(15444,15504,15451)` has voltage zero.  Each triangle satisfies
(3.1)--(3.3) locally with all boundary and reach variables zero, but lifts to
15 monochromatic physical 3-cycles.  The AA example violates the zero-run
condition for `z`, and the BB example violates the one-run condition.  Thus
the rows must not be advertised as an exact top-biresidence encoding for an
arbitrary disconnected warm-start factor.

On the connected `AddCircuit` model, the option named `top_biresidence`
therefore enforces both the one-runs and zero-runs of the fixed coordinate
`z`; this is stronger than merely requiring positive `z`-residence.  In the
disconnected 2-factor model it enforces the same statement only on
nonmonochromatic components.  The independent output audit currently
reports positive `z` runs but not zero-run minima.  Thus a future accepted
artifact must either be quotient-connected (when the proof above supplies
the zero-run assertion) or explicitly replay the zero runs before claiming
the named stronger property.

The independently rebuilt connected/unit/top-biresident model has

```text
131164 variables, 78725 constraints.
```

## 4. Exact component CEGAR

Drop `AddCircuit`, retain the quotient degree-two, q1 and boundary/reach
rows, and solve for a 2-factor.  These rows already enforce length at least
four on every proper shore run, but, by Lemma 3.1, a disconnected warm start
is not yet certified top-biresident.  For every proper current quotient
component with vertex set `S`, add

\[
 \sum_{e\in\delta(S)}x_e\ge2.                           \tag{4.1}
\]

Every connected 2-factor must cross a proper cut a positive even number of
times, so (4.1) is necessary.  If the quotient has become one cycle but its
voltage is nonunit, add only the exact factor no-good

\[
 \sum_{e\in F}x_e\le857.                               \tag{4.2}
\]

Reversing an undirected quotient cycle negates its voltage and does not
change its gcd with 15, so (4.2) loses no usable orientation.  Persistent
rows (4.1)--(4.2) therefore define an exact component CEGAR: a factor
returned with final status `PHYSICAL_HAMILTON` or
`PHYSICAL_HAMILTON_RESIDENT` is connected and unit-voltage; `UNKNOWN` proves
nothing.  Once the quotient is connected, Lemma 3.1 also upgrades the
boundary/reach rows to exact two-sided top residence.  Before that point,
monochromatic short components are harmless warm-start artifacts: component
cuts remove them.  If positive residence CEGAR is enabled, its literal motif
cuts additionally remove a monochromatic BB 3-cycle; the AA zero-run case is
still removed by its component cut.

There is one implementation-level fail-closed caveat in the audited source.
After a feasible round, the variable `selected` retains that round's factor.
If the next round is `UNKNOWN` or `INFEASIBLE`, or if `max_rounds` is reached,
the JSON still contains those stale non-null `selected_edge_ids`, even though
the factor has just been cut off, and `main` returns exit code zero solely
because the field is non-null.  Therefore neither a non-null field nor the
process exit code certifies CEGAR success.  A consumer must require one of
the two explicit success statuses above and then run a fresh literal audit.

## 5. Lazy old-coordinate residence motifs

Lift a returned factor literally.  A positive run of length `ell<4` is
fixed by its left boundary edge, its internal edges and its right boundary
edge.  Let `E(I)` be the set of quotient edge orbits underlying that physical
chain.  The row

\[
 \sum_{e\in E(I)}x_e\le |E(I)|-1                        \tag{5.1}
\]

is necessary: retaining all those orbit edges retains the same physical
`0,1^ell,0` chain.  This remains true if a very short quotient component
causes an orbit edge to occur more than once; the set row merely says that
at least one forcing orbit must change.  Adding all current motifs together
with the component rows is a sound exact CEGAR for positive residence.
Acceptance requires a fresh literal lift with zero short positive runs in
all 16 coordinates; two-sided top residence then follows from quotient
connectedness and Lemma 3.1 (or may be replayed directly as an independent
check).

## 6. Current computational boundary

The strict run

```text
/dev/shm/k16_qfactor_connected_unit_topres_seed16301.json
```

ended `UNKNOWN` after 1801.483777 solver seconds, 376236 branches and 15
conflicts; `selected_edge_ids` is null.  It is not an obstruction.  The next
sound stage is a q1-complete quotient 2-factor satisfying the boundary/reach
rows, used only as a hint for the component CEGAR of Section 4.  It becomes
exactly top-biresident when the CEGAR makes it quotient-connected; an earlier
disconnected factor needs the monochromatic-component qualification above.
Old-coordinate motif rows from Section 5 are added only after (or together
with) this topology stage.  No `k=16` word is claimed without deeper shadows,
a safe opening, the unrestricted compiler, and literal target replay.

## 7. Explicit top-biresident 2-factor warm start

The complementary centered-PBBS scaffold has complete lower/upper `q1`, 118
quotient components and 146 physical components.  Although its quotient
factor contains monochromatic components, its literal physical cycle lengths
are at least 15, so both values of the top coordinate have residence at least
four on every component.

The solver-free cross-switch census tested 157609 eligible AA/BB old-edge
pairs and 1771 voltage-labelled cross packets.  Exactly 226 packets preserve
all 764 lower and 764 upper target orbits while opening components of quotient
length at least four.  The retained packet is

\[
 \{8734,24187\}\longmapsto\{8745,13244\}.               \tag{7.1}
\]

It opens two quotient cycles of length 21 and produces one mixed quotient
cycle of length 42 and voltage 10.  Its lift has five mixed physical cycles
of length 126, each with alternating top one/zero run lengths 21.  Every
unchanged monochromatic physical component still has length at least 15.
Thus (7.1), unlike an arbitrary boundary/reach-compliant disconnected point,
is literally top-biresident.

The independently lifted ledger is

```text
lower q1 support       764/764
upper q1 support       764/764
quotient components    117
physical components    145
old-coordinate shorts  1020 = 90 of length 2 + 930 of length 3
```

An independent literal two-sided audit gives identical top one/zero run
histograms

```text
15:5, 21:15, 45:9, 75:21, 105:23, 135:11, 165:1,
```

so both minima are exactly 15.  Its artifact is

```text
scratch/k16_pbbs_topres_safe_cross_switch.top_biresidence.audit.json
SHA-256 1e75033873fe6a3183c2f7eeac442abbbb417189b6c8d162afec806535efe9cc.
```

The warm-start artifact and full safe-packet census are

```text
/dev/shm/k16_pbbs_topres_safe_cross_switch.json
SHA-256 9030bd92d54297e8dff82cf5509046f1b6f0b972805bad6f2506672acd42d4a2

/dev/shm/k16_pbbs_topres_safe_cross_switch.all.json
SHA-256 2d61c689688dbcece14811bd0597668c43360331736e01e511cbe5bd84636326
```

and the deterministic census source is

```text
scratch/search_k16_pbbs_topres_safe_cross_switch_20260729.py
SHA-256 15c07b6cef14f310790bc2aa1693ddc1bba5b79bbf92d61fee9dc4c25f7485dc.
```

This is a genuine exact warm start, not a connected or resident final
carrier.  It is now supplied only as a branching hint to the persistent
component CEGAR; all topology and later residence claims are re-audited from
the selected edge set.
