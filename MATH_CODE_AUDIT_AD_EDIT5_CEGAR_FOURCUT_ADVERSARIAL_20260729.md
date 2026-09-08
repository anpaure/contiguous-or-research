# Adversarial audit: four-closure shell and edit-five connectivity CEGAR

Date: 2026-07-29  
Lane: AD, independent audit  
Scope: exact mathematics and lightweight, solver-free source audit only

No CP-SAT solve, exhaustive heavy job, or new H100 worker was launched.  The
only executions were `py_compile`, `--help`, and the finite \(900\cdot48\)
block-route audit, both normally and under `python -O`.

## 1. Frozen sources audited

```text
803593f675ac7c7c575ae4674bb3a60e5921498cad431a147b4c1355442f6e79
  scratch/solve_k15_pascal_edit5_connectivity_cegar_ad_20260729.py

f9b5ca96d8b7e4b3f249a7ca36b8147cf4eaa1bdaf69d63cdfc8f070959a40f6
  scratch/solve_k15_pascal_fourcut_shell_ad_20260729.py

13e1a8b9f35d1a1a9c4f51cb8e0e5158935ccfd2116f9857d6f7a771295eaff9
  scratch/audit_k15_pascal_fourcut_empty_shell_ad_20260729.py
```

The parent path used by the audit has SHA-256

```text
eeccbd6be6edeba88a5d953a1f543c8f77895bbbec0e6ab0fd4eadb9e05af546.
```

All three sources compile successfully with and without optimization.  The
independent audit and the catalogue generator also produced byte-identical
stdout under normal Python and `python -O`.

## 2. Correct four-closure theorem, including new colour occurrences

Write the frozen rank-seven path as

\[
 P=(T_0,\ldots,T_{N-1}),\qquad N=\binom{14}{7}=3432,
\]

and its old edge at position (i) as (e_i=T_iT_{i+1}).  For a Johnson
edge (uv), call (u\cap v) its lower colour.

### Theorem 2.1 (four closures survive arbitrary added occurrences)

Let (P') be any Hamilton path on the same rank-seven deck with the same two
endpoints as (P).  Let (A\subseteq E(P')) satisfy:

1. exactly one edge of (A) has each rank-six lower colour;
2. every rank-seven vertex has (A)-degree one or two; and
3. every component of the spanning graph ((V(P'),A)) has at least four
   vertices.

Then (P') deletes at least one old edge from each of the following four
pairwise disjoint sets:

\[
\begin{aligned}
G_1={}&\{708,709,710,711\},\\
G_2={}&\{1940,1941,1942\},\\
G_3={}&\{2219,2220,2221,2521,2522\},\\
G_4={}&\{179,180,181,1364,1365,1773,1774,1775,\\
     &\hspace{23mm}1836,1837,1838,2723,2724,2725,2726\}.
\end{aligned}
\]

This remains true when new seams of (P') create extra occurrences of any
of the lower colours used in the proof.

#### Proof

Call an edge of (P') a cut when it is not in (A).  Conditions 2 and 3
imply that no two cuts can occur within path-edge distance three: two such
cuts contain a consecutive pair of cuts at distance at most three, and the
intervening (A)-component then has at most three vertices.  In particular,
adjacent cuts are impossible.

Whenever two consecutive surviving old edges have the same colour, exactly
one of them must be selected.  They cannot both be selected by exactness of
the lower colour, and they cannot both be cuts by the degree-one lower bound.
Consequently a newly added occurrence of that colour cannot be selected to
evade this local conclusion.  This observation is the point that closes the
added-occurrence loophole.

For (G_1), the complete old fibres are

\[
F_{14374}=\{708,709\},\qquad F_{12390}=\{710,711\}.
\]

If all four old edges survive, each adjacent pair has exactly one cut.
The two cuts are at distance two or three (the only distance-one choice is
itself forbidden), contradicting condition 3.

For (G_2), the complete old fibre is

\[
F_{10318}=\{1940,1941,1942\}.
\]

If these three consecutive old edges survive, exactness plus nonadjacent
cuts forces the centre edge to be selected and the two outer edges to be
cuts.  Their distance is two.  Selecting a new occurrence would leave
adjacent old cuts, so it does not help.

For (G_3), the complete old fibres are

\[
F_{5149}=\{2219,2220\},\qquad
F_{5273}=\{2221,2521,2522\}.
\]

The surviving adjacent pair (2521,2522) forces one of those two edges to
be the unique selected occurrence of colour (5273); hence (2221) is a
cut.  The surviving adjacent pair (2219,2220) forces exactly one cut, and
it cannot be (2220), adjacent to the cut at (2221).  Thus (2219) and
(2221) are cuts at distance two.  Again, any selected new occurrence
would leave an adjacent old pair unselected.

For (G_4), the complete relevant old fibres are

\[
\begin{array}{c|c}
7697&179,1775\\
3858&181,1838\\
16128&1364,1365,1773\\
3792&1836,2723\\
2761&2725,2726.
\end{array}
\]

The connector positions (180,1774,1837,2724) in (G_4) are essential:
their survival preserves the displayed distance-two/three local blocks.
The adjacent pair (1364,1365) forces its unique colour-(16128)
selection to lie in that pair, so (1773) is a cut.  The adjacent pair
(2725,2726) supplies one cut.  If there were no short component, colour
(3792) could not cut at (2723), so it would cut at (1836).  Then
colour (3858) could not cut at (1838), so it would cut at (181).
Then colour (7697) could not cut at (179), so it would cut at (1775),
which is distance two from the forced cut at (1773).  Choosing a newly
added occurrence in any of the three nonlocal double fibres leaves both old
occurrences cut and therefore includes the very cut excluded at the
corresponding implication step; it cannot evade the chain.

Thus survival of every edge of any (G_i) contradicts condition 3.  The
four sets are disjoint, proving the theorem.  \(\square\)

### Scope correction

The conclusion printed at lines 187--189 of the independent audit says
"exact-lower chronology".  Exact lower-colour multiplicities alone are not
the stated hypothesis.  The exact theorem also needs the spanning
(A)-degree-one-or-two condition (or the full generalized-Pascal owner
equations that imply it) and hard residence.  The edit-five CP model does
enforce all of these conditions, so this wording issue does not change its
feasible set.

## 3. Exact four-cut route classification

The four groups have sizes (4,3,5,15), are pairwise disjoint, and hence
give exactly

\[
 4\cdot3\cdot5\cdot15=900
\]

possible deletion quadruples when the edit distance is four.  Once four old
edges are deleted, the old path splits into five nonempty intervals.  Any
same-endpoint Hamilton path retaining every other old edge is obtained by:

1. keeping the interval containing (T_0) first and forward;
2. keeping the interval containing (T_{N-1}) last and forward; and
3. permuting and orienting the three internal intervals.

Thus the (3!2^3=48) cases tested per deletion tuple are exhaustive.  The
independent DFS in the audit source is genuinely separate from the
Cartesian-product generator in the shell source.

The reproduced result is:

```text
cut quadruples                  900
Johnson-compatible assemblies  900
profile                         [(new joins, distinct joins)=(0,4)] x 900
exact-distance-four assemblies 0
ledger SHA-256                  ceedb84102052749d902cc3ff3fb72905a0c10add812d9af9861da70f72b1801
```

More precisely, the 900 compatible assemblies are 900 presentations of the
same unedited parent path, one for each artificial four-cut decomposition;
they are not 900 distinct physical routes.  In every case the block order is
(0,1,2,3,4), all orientations are forward, and the joins restore the four
deleted base edges.  Therefore there is no same-endpoint exact-distance-four
path satisfying the necessary four closures.  Together with Theorem 2.1:

\[
 \boxed{|E(P')\setminus E(P)|=|E(P)\setminus E(P')|\ge5}
\]

for every path/controller solution under the theorem's hypotheses.

The route generator independently returned catalogue SHA-256

```text
ffc29a2d5cc667136b5bd332190f90fd59bfa57c0463e718369316283b68c463
```

with `new0_distinct4: 900`, zero retained exact-distance-four routes, and
zero distinct added edges.  The off-live-palette and in-live-palette pieces
are respectively (540) and (360), and both are also empty.

## 4. Postpatch independent closure certificate

The current independent executable now certifies the finite content of
Theorem 2.1 rather than merely checking the fibre literals.  For each colour,
its selector domain is every verified old occurrence together with `None`,
where `None` represents selection of an arbitrary newly added occurrence.
This is exhaustive for the old-edge cut pattern even if there are many new
occurrences: exact lower multiplicity permits precisely one selected
occurrence, so either one old occurrence or no old occurrence is selected.

For every assignment the checker makes every other old fibre occurrence a
cut and tests all pairs of cuts in the fully preserved connector blocks.
A pair at edge-position distance at most three already forces a short
component; ignoring cuts on newly added or irrelevant connector-colour edges
is a safe relaxation.  It also verifies that the unions of the literal
connector intervals are exactly the four closure sets, including positions
180, 1774, 1837 and 2724.

The exact assignment censuses for G1, G2, G3 and G4 are respectively 9, 4,
12 and 324, and the number without a forced short component is zero in every
gadget.  The truth-table formulation and its `None` case are sound and
complete for the closure implication.  The patched conclusion also states
the necessary degree-one-or-two spanning hypothesis explicitly.  No new bug
was found in these checks.

## 5. Exact edit/connectivity equivalence in the edit-five model

The graph model at lines 205--224 is exact for its declared support radius.
Let (h_e\in\{0,1\}) denote selected Johnson edges.  The endpoint degrees
are one and all other degrees are two, so the selected graph has

\[
 \frac{2(N-2)+2}{2}=N-1
\]

edges and consists of one source--sink path plus zero or more disjoint
cycles.  If five selected edges are nonbase, then exactly five of the
(N-1) base edges are absent.  Hence the model's linear edit equation is
equivalent to half-symmetric-difference five; no separate deletion equation
is missing.

For an endpoint-free shore (S), every connected source--sink path crosses
\(\delta(S)\) at least twice.  Therefore each CEGAR inequality

\[
 \sum_{e\in\delta(S)}h_e\ge2
\]

is valid.  Every disconnected incumbent has a unique component containing
both odd-degree endpoints and all other components are cycles, so the loop
adds a valid cut for every cycle.  Repeated separation is finite.  A
connected incumbent with the degree equations is exactly one Hamilton path
on the full deck.  An `INFEASIBLE` result after any finite collection of
these cuts therefore rules out every connected solution, although it remains
a solver-reported result rather than an independently checkable proof.

Resume rows are also sound: the loader canonicalizes them, rejects empty or
full shores, rejects foreign vertices and both endpoints, and rejects
duplicates.  Such a row is a universally valid source--sink connectivity
cut even if it was not originally produced by this CEGAR instance.

## 6. Compact hard-residence constraints

The hard-residence compression is exact once connectivity has produced a
Hamilton path.

The lower-rainbow equations select (3003\) AA edges.  The equations

\[
 d_A(v)=1+t_v,\qquad t_v\in\{0,1\},
\]

make every AA component a spanning subpath of the selected Hamilton path.
The inequality

\[
 a_{uv}\le t_u+t_v
\]

forbids a two-vertex AA component.  An internal witness can be one only when
(a_{uv}=t_u=t_v=1), and every (t_v=1) vertex must see such a witness.
This excludes precisely a three-vertex component: its unique degree-two
vertex has no AA neighbour of degree two.  Conversely every path component
of at least four vertices has a degree-two--degree-two edge incident with
each of its degree-two vertices (the single central edge suffices for four
vertices), so witnesses exist.  The exact-AND implementation in the
four-cut source and the subset-witness implementation in the edit-five source
therefore define the same hard-residence property on a final path.

During an intermediate disconnected CEGAR solve, an AA cycle may satisfy
the compact constraints.  This is a harmless relaxation: every such path
cycle is subsequently separated, and on every connected final graph the
formulation is exact.  It neither loses a genuine Hamilton solution nor
invalidates an eventual infeasibility result.

## 7. Both controller sectors

The controller equations are complete and correctly coupled to the same AA
choice.  For every rank-seven middle owner (T),

\[
 d_{AA}(T)+d_{\rm cross}(T)=2,
 \qquad d_{\rm cross}(T)+d_{BB,\rm lower}(T)=1.
\]

For every rank-eight no-(z) child (U),

\[
 d_{\rm cross}(U)+d_{BB}(U)=2.
\]

The first upper sector is enforced by

\[
 \sum_{AA:\,u\cup v=U}a_{uv}
 +\sum_{{\rm cross}:\,\text{upper}=U}c\ge1
 \quad(U\in\tbinom{[14]}8),
\]

and the second by at least one selected BB pair with each rank-nine union.
The decoder reconstructs all three physical edge types, checks the total
(6435)-edge census and absence of duplicates, checks degree two at every
rank-eight child, audits the exact lower deck and the full upper deck, and
then separately checks both (z)-upper and no-(z)-upper sets.  No sector is
silently omitted.

## 8. Fail-closed and provenance corrections: postpatch disposition

### 8.1 Empty-shell mutation window: resolved

The early empty-catalogue branch now recomputes and compares the source,
helper, path and hint hashes immediately before emitting its result.  A
mutation leaves only the noncertificate `BUILDING` sentinel and raises.  The
TOCTOU defect is closed.

### 8.2 Independent-audit claim scope: resolved

The independent audit now states the exact lower-colour, degree-one-or-two
spanning, and minimum-component-size hypotheses.  It also embeds the four
truth tables described in Section 4.

### 8.3 Route-shell versus closure certificate: resolved

The shell result now uses
`VERIFIED_EMPTY_ROUTE_SHELL_CONDITIONAL_ON_CLOSURES`; its `scope` remains the
exact conditional route statement.  The separate independent executable
supplies the closure truth-table certificate.  Consumers must retain both
artifacts for the combined edit-distance-five lower bound.

### 8.4 Negative CP-SAT provenance: substantially resolved

The edit-five source now serializes `argv`, all resolved paths, raw integer
status, the last `ResponseStats()`, total elapsed time, and a per-iteration
ledger containing the requested limit, solver and process wall times, cut
count, and incumbent component sizes.  These fields are JSON-safe and are
updated consistently at every solved iteration.  The final model-proto hash
is still correctly taken after all CEGAR cuts.  No implementation bug was
found in the added ledger.

The unavoidable boundary remains explicit: source/model provenance plus a
CP-SAT `INFEASIBLE` status is not an independently checkable UNSAT proof.
`certificate_status` remains null and downstream prose must still say
`solver-reported INFEASIBLE in the declared scope` unless a separate proof
is exported.

### 8.5 Catalogue-hash domain: resolved

The catalogue now includes the domain string before hashing and defines the
hash as canonical sorted compact JSON excluding only `catalogue_sha256`.
The recomputed all-shell hash is the value in Section 3.

## 9. Final audited boundary

The mathematical four-closure implication is valid, including arbitrary
new occurrences of its colours.  The two independent route enumerators agree
that all 900 four-cut decompositions have only the restored parent assembly,
so edit distance four is rigorously empty and five is the first support
radius not ruled out.

The edit-five full-Johnson model is exact for same-endpoint connected paths,
its compact hard-residence constraints are exact on those paths, both
physical `q1` controller sectors are present, and its connectivity CEGAR
uses only valid cuts.  No feasible-set error was found.  The first audit's
executable-coverage, wording, empty-branch, hash-domain and provenance issues
have all been patched and re-audited.  The only remaining qualification is
the explicitly disclosed absence of an independently checkable CP-SAT
infeasibility proof.  No result of the edit-five model has been run or
claimed in this audit.
