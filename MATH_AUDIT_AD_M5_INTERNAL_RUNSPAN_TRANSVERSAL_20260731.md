# Exact internal-run span transversal for the item2183 (m=5) carrier

## 1. Scope and frozen inputs

This note audits only the immutable internal coordinate runs of the literal
42-path (J(10,5)) forest in item2183.  The reconstruction is independent of
any choice of endpoint sockets or path orientations.

Frozen inputs:

- `scratch/audit_thread_a_m5_three_c10_downstream_state_20260731.py`, SHA-256
  `f97eaa7d8457f619e06fa91a501142a5b9fb0af0818fc0b31ae10ef318778041`;
- `scratch/thread_a_m5_three_c10_downstream_state_20260731.audit.json`, SHA-256
  `91201d7281bde581ef01a58778b6e8edbea8dcb7da37d185c76f1771b91b2a5e`.

The exact replay written for this note is
`scratch/audit_ad_m5_internal_runspan_transversal_20260731.py`; its output is
`scratch/ad_m5_internal_runspan_transversal_20260731.audit.json`.

## 2. Closed-span lemma

Let

\[
P=(v_0,v_1,\ldots ,v_{L-1})
\]

be one source path and fix a coordinate (c).  Suppose

\[
(1_c(v_{a}),1_c(v_{a+1}),1_c(v_{a+2}),1_c(v_{a+3}))=(0,1,1,0).
\]

Call the three source edges with indices

\[
I=[a,a+2]=\{v_av_{a+1},v_{a+1}v_{a+2},v_{a+2}v_{a+3}\}
\]

the closed span of this bad run.

**Lemma 2.1 (immutable closed span).**  Let a new literal path or cycle be
obtained by deleting some source-path edges, retaining every undeleted
source fragment intact up to reversal, and reconnecting the fragments.  If
none of the three edges in (I) is deleted, then the new chronology still
contains an internal length-two positive run of coordinate (c).

**Proof.**  The four vertices stay consecutive inside one retained fragment.
In the original orientation their word is (0110); in the reversed
orientation it is again (0110).  Both boundary zeroes remain adjacent to
the two ones.  Hence reconnection outside the closed span cannot change that
internal run.  (square)

Thus the deleted source seams of every successful interior rethread form a
transversal of the 31 closed three-edge intervals.

## 3. Exact interval transversal

The 31 bad runs occur on exactly 18 of the 42 paths.  In the following table
an interval ([i,j]) means the source edges with indices (i,ldots,j).

| path | length | bad spans | pathwise minimum |
|---:|---:|:---|---:|
| 1 | 11 | [1,3], [4,6] | 2 |
| 3 | 29 | [6,8], [10,12], [15,17], [19,21], [22,24], [25,27] | 6 |
| 5 | 13 | [3,5], [7,9] | 2 |
| 6 | 4 | [0,2] | 1 |
| 7 | 7 | [1,3] | 1 |
| 8 | 5 | [0,2] | 1 |
| 9 | 12 | [2,4], [6,8] | 2 |
| 11 | 13 | [2,4], [8,10] | 2 |
| 12 | 8 | [1,3], [4,6] | 2 |
| 13 | 7 | [1,3] | 1 |
| 14 | 8 | [3,5] | 1 |
| 15 | 16 | [1,3], [9,11], [11,13] | 2 |
| 16 | 9 | [4,6] | 1 |
| 17 | 8 | [3,5] | 1 |
| 20 | 7 | [0,2] | 1 |
| 22 | 6 | [0,2] | 1 |
| 25 | 7 | [1,3] | 1 |
| 26 | 9 | [1,3], [2,4] | 1 |

All unlisted paths have no internal length-two positive run.

**Theorem 3.1 (sharp 29-seam obstruction).**  Every fragment rethread that
removes all 31 old internal length-two runs deletes at least 29 original
forest seams.  This is sharp as an interval-transversal statement.

**Proof.**  On a line, the minimum number of integer points meeting a family
of intervals equals the maximum number of pairwise disjoint intervals.  The
standard proof chooses the right endpoint of the first interval in
increasing right-end order; the intervals that cause a new choice are
pairwise disjoint, while the chosen endpoints hit every interval.  Applying
this independently on the edge line of each source path gives the last
column of the table.  Different source paths have disjoint edge sets, so the
values add to

\[
2+6+2+1+1+1+2+2+2+1+1+2+1+1+1+1+1+1=29.
\]

The audit JSON records both a 29-point hitting set and 29 pairwise disjoint
intervals, so the primal and dual certificates agree.  (square)

There are only two overlaps that save a cut relative to the raw count 31:

1. on path 15, spans ([9,11]) and ([11,13]) force source edge 11;
2. on path 26, spans ([1,3]) and ([2,4]) may be hit by either source edge
   2 or source edge 3.

Every other bad span is edge-disjoint from every other bad span on its path.
Consequently edge ((15,11)) is the sole globally forced path-edge choice.
The exact number of minimum transversals is

\[
2\cdot 3^{27}=15,251,194,969,974.
\]

One canonical greedy minimum, written as `(path, edge-index)`, is

```text
(1,3) (1,6)
(3,8) (3,12) (3,17) (3,21) (3,24) (3,27)
(5,5) (5,9)
(6,2) (7,3) (8,2)
(9,4) (9,8)
(11,4) (11,10)
(12,3) (12,6)
(13,3) (14,5)
(15,3) (15,11)
(16,6) (17,5) (20,2) (22,2) (25,3) (26,3)
```

The audit JSON gives the corresponding physical mask pairs and all 31 runs
with path index, coordinate, four vertices, and three physical span edges.

## 4. Exact consequences for a minimum-support rethread

Let (s) be the number of deleted old seams.  Theorem 3.1 proves (s\ge29),
without using Johnson legality.  If equality holds, the deletion set has the
normal form above: the path-15 edge 11 is forced, path 26 contributes edge 2
or 3, and every other disjoint span contributes exactly one of its three
edges.

For a literal equality-support replacement with (s=29), the exact
fixed-window delta theorem gives the following *upper bounds on the affected
boundary ledger*, not preservation:

- at depth (q), at most (29q) old and (29q) new seam-crossing windows;
- at (q=2), at most 58 old and 58 new boundary occurrences, hence total
  occurrence variation at most 116;
- for the depth-two maximal erosion envelope, at most 58 source columns can
  change;
- for one erosion-letter cell whose dependency window has (h+1) owner
  seams, at most (29(h+1)) start positions can change (provided the window
  is shorter than the chronology).

These bounds locate the exact finite regeneration ledger.  They do **not**
show that any of the minimum transversals has a Johnson-legal reconnection,
that the new seams create no new short runs, that every lost flag has a new
provider, or that the compiler Hall inequalities survive.  Those are the
remaining regeneration conditions.

### 4.1 The depth-one palette gate is feasible at support 29

For a chosen minimum transversal (D), preserving the two exact depth-one
palettes means the following.  Give each deleted edge (e) its lower colour
(L_e) and upper colour (U_e).  A replacement using (L_e) and (U_f)
exists precisely when

\[
L_e\subset U_f,\qquad |U_f\setminus L_e|=2;
\]

the physical Johnson edge is then uniquely determined.  Because every
deleted seam must genuinely change, the required permutation (e\mapsto f)
must have no fixed point.  Thus the exact depth-one gate is a loopless
directed cycle cover of the selected lower-to-upper incidence graph.

This gate is **not** an additional obstruction at 29.  The audit records an
explicit minimum transversal, in the 29 equality groups, with selected edge
indices

```text
1,5,6,10,15,19,22,25,3,7,0,1,0,2,6,2,8,1,6,1,4,1,11,4,4,1,0,1,2
```

and the following successor permutation:

```text
5,28,7,12,17,6,24,0,20,14,11,18,10,23,25,9,8,13,1,21,15,3,27,22,26,2,19,16,4.
```

It is the single 29-cycle

```text
0,5,6,24,26,19,21,3,12,10,11,18,1,28,4,17,13,23,22,27,
16,8,20,15,9,14,25,2,7.
```

Direct replay verifies 29 distinct inserted Johnson edges, disjoint from the
29 deleted edges, with exactly the same lower-colour multiset and exactly the
same upper-colour multiset.

This is deliberately only a palette certificate.  Its owner-degree delta is
nonzero on 70 middle owners: 35 have delta (-1) and 35 have delta (+1).
Direct physical replay gives degree histogram

\[
                         0^4 1^{94}2^{136}3^{18},
\]

and one 71-vertex/71-edge cyclic component, so this witness is not a
physical path-forest exchange.  Exact restoration of every old owner degree
would be one sufficient subclass, but it is not necessary.  The exact next
gate is only degree at most two plus acyclicity (followed by new-run,
higher-flag, and compiler checks).

### 4.2 Exact support-29 physical no-go

The degree-at-most-two gate already fails for **every** minimum
transversal and every loopless palette cycle cover.  Let (F) be the frozen
210-edge forest.  For a middle owner (v), let (b_v=d_F(v)), let (D_v)
be the selected deleted source edges incident with (v), and let (I_v)
be the selected inserted palette-cross edges incident with (v).  The exact
physical capacity row is

\[
       b_v-\sum_{e\in D_v}x_e+\sum_{a\in I_v}y_a\le2.       \tag{4.1}
\]

This is maximum new degree at most two.  It does **not** require restoration
of the old owner degree.

**Theorem 4.1 (support-29 decorated-forest impossibility).**  There is no
choice of one deleted edge from each of the 29 equality run-span groups and
no loopless lower-to-upper palette cycle cover satisfying (4.1) at all 252
middle owners.  Consequently every two-palette-exact literal linear-forest
rethread that removes all 31 old length-two runs has support at least 30.
The new lower-to-upper pairing may differ from the source pairing.

**Proof certificate.**  The exact quotient has 84 candidate deleted edges
and 427 loopless palette arcs.  Its CNF has 511 variables and 15,154 clauses:

\[
111\text{ group exactly-one}
+3100\text{ cycle-cover}
+11943\text{ physical degree clauses}.
\]

For completeness, the degree encoding can be checked without a solver.  Fix
an owner and an exact truth set (T\subseteq D_v).  Put

\[
c_v=2-b_v.
\]

For every (S\subseteq I_v) with

\[
|S|=c_v+|T|+1,
\]

the CNF contains

\[
 \bigvee_{e\in T}\neg x_e
 \ \vee\!
 \bigvee_{e\in D_v\setminus T}x_e
 \ \vee\!
 \bigvee_{a\in S}\neg y_a.                         \tag{4.2}
\]

When the deletion truth set is exactly (T), the first two blocks are
false, and (4.2) says that no (c_v+|T|+1) inserted incidences are all true.
Thus all such clauses are equivalent to

\[
|I_v|\le c_v+|T|,
\]

which is exactly (4.1).  Conversely, every violation of (4.1) contains such
an (S) and falsifies (4.2).

Kissat returned UNSAT in 0.03 seconds.  The 420 KiB DRAT proof independently
verifies.  `drat-trim` extracted a 1,076-clause core with 1,319 core lemmas
plus the final empty clause; the extracted core and proof independently
verify again (917 active clauses and 997 active lemmas on the second pass).  Since acyclicity
was not encoded, the result is an UNSAT certificate for a relaxation of the
physical forest problem and therefore proves the theorem.

The support-30 feasibility problem is not decided here.  Combining this
lower bound with the independently replayed residence-clean perfect diamond
matching of item2188 gives the current exact internal-rethread bracket

\[
                   30\le s_{\min}\le119.
\]

The upper endpoint is a 210-edge, 42-path, two-palette-exact forest with no
internal positive run shorter than three.  It still has 21 deeper-shadow
debts and unresolved endpoint/compiler chronology, so this bracket concerns
the central residence/palette/forest subsystem only.

## 5. Reproducibility

The replay reports

```text
status = PASS_EXACT_ITEM2183_INTERNAL_RUNSPAN_TRANSVERSAL
bad runs = 31
paths with bad runs = 18
exact minimum deleted seams = 29
minimum transversals = 15251194969974
payload SHA-256 = 43b39a185d71991d3e40538defd1e325e0f7436f63a41113f0fc0a14ccc2340f
```

Artifact hashes after deterministic replay:

- run-span script: `9440727eedbfd364ab183ce25f64a75f1ae24228afb96c432d5f1613eae8f370`;
- run-span JSON: `22fb3d9fc344ba0f1656319f304f26df4961853fd9b31bbb68dc893f98f9789d`;
- degree-two CNF: `eb542e3ee0f3c3a8829c5c278c71c2df159585e2740b11cbf62f4f67ecfa2c1c`;
- full DRAT proof: `65dd5aaca70ffdcd0e1ef0693a8276f235b65774c0f936fd92ad74bfc2c9c129`;
- extracted core CNF: `3e04d1ad5ee40eb8b1552db0c7279d952d38e2f0443626099414852c6688bb19`;
- extracted core proof: `17cbc0a758f4023eead77508abc7b278806e0414cba7818192a81c3ebe0d666f`;
- independent semantic/DRAT audit JSON:
  `049ad277705f73783ab901d811f07b4e59d26d51645dfaf746e60c4cae616303`,
  payload
  `b8e37ab4daa6aa44339edbb0ebea8f75d875177db2ad42bc01ca9894cde6cc8a`.
