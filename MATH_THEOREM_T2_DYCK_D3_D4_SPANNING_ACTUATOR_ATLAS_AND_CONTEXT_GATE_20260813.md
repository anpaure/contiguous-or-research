# The `T2` suffix actuator spans `D_3` and `D_4`, but no insertion-closed template is yet proved

**Date:** 2026-08-13
**Status:** unconditional exact finite theorem at suffix semilengths three
and four, with an independently verified q2-safe spanning actuator on all
fourteen `D_4` roots.  All shortest-length claims are explicitly restricted
to alternating circuits whose owners are internal (degree two) in the
post-`T2` factor, the class needed by the proposed source lift.  The selected
circuits are incidence-vertex-disjoint and their simultaneous toggle merges
every touched lifted component into one.  Every selected circuit fails
undilated `2`-residence on at least one shore.  Right Dyck-tail concatenation
remains a valid context operation; left insertion and primitive wrapping are
not automatic.  An all-semilength context-generated family is therefore
still open.

## 0. Outcome

Apply the two frozen `T2` packets at every suffix root, as in
`MATH_THEOREM_T2_TWO_SUFFIX_C16_Q2_SAFE_SWITCH_AND_C8_C10_OBSTRUCTION_20260813.md`.
Let `G_s` be the graph on `D_s` in which two Dyck suffixes are adjacent
when their up-step sets differ by one `1/0` transposition.

The aligned switch `1100W <-> 1010W` is only a matching in `G_s`.  It does
not span once `s>=3`.  The escape is real but needs a richer finite atlas.

1. At `s=3`, there is an explicit four-edge suffix tree.  Its actuators
   have exact all-six-prefix internal-owner minima `16,16,18,16`, are
   pairwise owner- and
   colour-disjoint, preserve aggregate q2 support, and merge exactly `27`
   post-`T2` components into one component with `893` owners on either
   middle-level shore.
2. At `s=4`, **every one of the 47 edges of `G_4` admits a q2-safe
   internal-owner alternating actuator**.  Its exact shortest safe length
   over all six `T2` prefix channels, within that class, belongs to

   \[
                            \{14,16,18,20,22,24\}.             \tag{0.1}
   \]

   The complete histogram is

   \[
        C_{14}:3,\quad C_{16}:15,\quad C_{18}:11,\quad
        C_{20}:9,\quad C_{22}:8,\quad C_{24}:1.                \tag{0.2}
   \]
3. A SAT-selected thirteen-edge suffix arborescence uses only
   `C14/C16/C18/C20` actuators.  The thirteen circuits are pairwise owner-
   and colour-disjoint.  Their simultaneous toggle loses no old q2 target
   and merges `82` post-`T2` components into one component with `2898`
   owners on either shore.
4. The standard Proskurowski--Ruskey path is not itself a compatible
   shortest-class shortcut.  All thirteen of its edges individually have
   q2-safe internal-owner actuators, but the enumerated shortest-safe
   candidate classes in the two productive prefix channels have no pairwise
   vertex-disjoint transversal.
5. None of the finite spanning actuators is directly resident.  The `s=4`
   simultaneous output has `51` bad upper `2`-collars and `40` bad lower
   `2`-collars, and the minimum new-seam gap is one on both projections.

Thus the topology/spanning part is no longer obstructed at `s=3,4`; the
remaining theorem is genuinely recursive:

\[
 \boxed{\text{derive a finite context-insertion grammar whose selected
 circuits remain q2-safe, resource-disjoint, component-connecting, and
 residence-liftable in every }D_s.}                         \tag{0.3}
\]

## 1. Search object and exact q2 test

Fix a suffix edge `V--W` and one of the six changed `T2` prefix owners
`P`.  In the exact post-`T2` owner--q1 incidence factor, let

\[
                         A=PV,\qquad B=PW.                    \tag{1.1}
\]

A directed exchange step is

\[
 O\mathrel{\mathop\longrightarrow^Q}O'
 \quad\Longleftrightarrow\quad
 (O,Q)\notin F, (O',Q)\in F.                               \tag{1.2}
\]

Two internally vertex- and colour-disjoint paths `A -> B` and `B -> A`
give a simple alternating incidence circuit.  The **admissible class** in
this note additionally requires every owner on both paths to have degree two
in the post-`T2` factor.  This makes the untouched mate below defined at
every row and is exactly the internal-owner class needed for the proposed
common-history/source lift.  Endpoint-using circuits outside this class are
not included in any minimality claim.  At a toggled owner `O`, let
`M` be its unchanged selected q1 mate.  The exact q2 current is

\[
                          [M\cup Q^+]-[M\cup Q^-].             \tag{1.3}
\]

All length claims below are therefore exact finite statements **inside this
admissible class**: breadth-first directed distances give the lower bound,
every smaller path-length split is exhausted, label simplicity is checked,
and `(1.3)` is evaluated against the complete old load ledger.

## 2. A complete `D_3` actuator tree

The five suffix roots are

```text
111000, 110100, 110010, 101100, 101010.
```

Select the following tree and prefix instances:

| suffix edge | witness prefix owner | exact all-prefix internal-owner minimum |
|---|---|---:|
| `111000--101100` | `101001010101` | `C16` |
| `111000--101010` | `101001001101` | `C16` |
| `110100--110010` | `101001010101` | `C18` |
| `110100--101100` | `101001001101` | `C16` |

### Theorem 2.1 (`D_3` simultaneous actuator)

The four displayed circuits have pairwise disjoint owner sets and
pairwise disjoint q1-colour sets.  Each circuit separately loses no old q2
support value, and their aggregate current loses none.  Their simultaneous
toggle meets `27` post-`T2` lifted components and produces one component,
so the exact component reduction is `26`.  The output component has

\[
                         47(2m+1)=47\cdot19=893              \tag{2.1}
\]

owners on each shore.

The four component arities are all eight; however, their component--trade
incidence graph is not a tree.  Component overlaps create two independent
hypercycles, but the actual endpoint permutation still has one orbit.
This is why direct traversal, rather than the sufficient hypertree theorem
alone, is needed for the finite certificate.

#### Proof

The frozen circuit rows are listed in the verifier named in Section 7.
It independently rebuilds the post-`T2` factor, checks every old/new
incidence and every q2 current, verifies owner/colour disjointness, and
traverses the complete lifted result.  The suffix edge set is a connected
four-edge graph on five vertices and hence a tree.  A separate all-prefix
audit exhausts every shorter admissible circuit in all six `T2` channels;
none is q2-safe.  Hence the displayed `C16,C16,C18,C16` lengths are the exact
admissible minima for these four templates. \(\square\)

### Residence and common intersections at `s=3`

The individual upper common-intersection ranks are all `7`; the lower
projection common-intersection ranks are `2,3,2,3`.  The original-owner
lower palettes have respectively `7,6,8,5` lost and equally many born
occurrences.  Every circuit has a bad `2`-collar on both shores.  The
simultaneous state retains `18` bad upper collars and `14` bad lower
collars, with minimum seam gap one.

Thus the upper/q1 projection has ample prospective common-history rank for
fixed source depth, but the frozen chronology is not resident.  The lower
projection has both a small common core and a nonzero palette current.

## 3. Complete edge atlas at `s=4`

There are `14` Dyck roots and `47` transposition edges in `G_4`.

### Theorem 3.1 (every `D_4` suffix edge is actuated)

Every edge of `G_4` admits a q2-support-safe simple internal-owner
alternating incidence circuit through corresponding `T2` owners.  Across
all six prefix channels, the exact admissible shortest-safe length histogram
is `(0.2)`.

Within the two productive channels used to build the spanning selection,
37 of the 47 suffix edges have a q2-safe label-simple circuit already at
the directed-distance lower bound.  The remaining ten require two
additional incidences.  Across those ten edges the search exhausts `28`
shorter label-simple circuits; all fail q2 support or fail to realize a
simple combined circuit.  A second audit exhausts all admissible circuits
in the other four prefix channels strictly below these incumbents and finds
no improvement.  The maximum all-six-prefix admissible minimum is the
unique `C24` class.

#### Proof

For each suffix edge and each of the two productive prefix owners

```text
101001010101, 101001001101,
```

the H100 enumerator computes both directed distances, enumerates all path
splits from the lower bound upward, rejects owner/colour repetitions, and
evaluates `(1.3)`.  The 47 exact rows, lower bounds, witness counts, and
shorter-cycle counts are frozen in the certificate of Section 7.  The
all-prefix audit then repeats the strict-below-incumbent exhaustion for each
of the remaining four prefix channels.  It reports no improvement and the
same histogram `(0.2)`. \(\square\)

This is the first evidence that the local actuator vocabulary may be
bounded: at `s=4` no **internal-owner** circuit longer than `24` is needed.
It is not yet an all-`s` theorem, a statement about endpoint-using circuits,
or a proof that the six numerical lengths correspond to a finite symbolic
grammar.

## 4. An exact spanning actuator on all fourteen `D_4` roots

The selected suffix-tree edges, written parent-to-child, are:

```text
11110000 -> 10111000     C18
11110000 -> 10110010     C16
11101000 -> 10101100     C16
10101010 -> 11101000     C16
11100100 -> 11100010     C18
10101100 -> 11100100     C16
11011000 -> 11001100     C18
10111000 -> 11011000     C16
11010100 -> 11010010     C18
10110100 -> 11010100     C16
11010010 -> 11001010     C18
11001010 -> 10101010     C14
10110010 -> 10110100     C20.
```

This is an arborescence rooted at `11110000`.

### Theorem 4.1 (`D_4` simultaneous spanning actuator)

The thirteen frozen circuits have the following exact properties.

1. Their owner sets are pairwise disjoint, and their q1-colour sets are
   pairwise disjoint.  Thus all toggles commute.
2. The length histogram is

   \[
                          C_{14}:1,\quad C_{16}:6,\quad
                          C_{18}:5,\quad C_{20}:1.             \tag{4.1}
   \]
3. Their aggregate q2 current removes `88` loaded occurrences, but every
   old target retains load at least one.
4. Their old incidences meet `82` distinct post-`T2` lifted components.
   The actual simultaneous endpoint permutation has one orbit, so the
   output component has

   \[
                     138(2m+1)=138\cdot21=2898                \tag{4.2}
   \]

   owners on either shore.  The global component reduction is `81`.
5. Seventeen earlier SAT models passed suffix-tree and resource-
   disjointness constraints but failed either aggregate q2 support or the
   one-orbit component test.  Blocking those models yields the displayed
   certificate.

#### Proof

The SAT encoding gives every nonroot suffix one incoming selected arc and
assigns one-hot depths; every selected arc points from smaller to larger
depth.  This is exactly a rooted spanning arborescence.  Owner and colour
resources have at-most-one constraints.  After decoding, the enumerator
recomputes aggregate `(1.3)` and traverses the full lifted graph.  The
independent verifier reconstructs all incidences and repeats each listed
claim without rerunning the search. \(\square\)

The component--trade incidence graph need not be a hypertree.  The
certificate proves the stronger desired conclusion—one actual output
component—directly.  Thus the hypertree condition remains a useful
symbolic sufficient condition, not a necessary condition for these
longer component-overlapping actuators.

The distinction is literal in the frozen selection.  Twelve circuits merge
all of their individually touched components into one, with shore-owner
lengths `336`, `357`, or `378` according to arity.  The selected `C14` on

```text
11001010--10101010
```

meets six old components but produces two individual outputs of shore-owner
lengths `146` and `148`; its component reduction is four, not five, and its
two named suffix representatives are not individually joined.  Interactions
with the other twelve commuting toggles merge these two pieces into the
certified simultaneous output.  Consequently “suffix arborescence” always
means the selected graph on suffix **labels**, never an assertion that each
edge is a binary component connector or that the component incidence graph
is a hypertree.

### Individual common-history/residence boundary

The exact per-circuit audit gives upper common-intersection ranks `7` or `8`
and lower common-intersection ranks between `2` and `6`.  Every lower
original-owner palette is nonneutral, with `5`--`8` lost occurrences.  Twelve
circuits have a bad lower `2`-collar; the circuit on
`11010100--10110100` has none on the lower shore but has three bad upper
collars.  Every other circuit also has at least one bad upper collar.  Thus
no selected circuit is directly two-shore `2`-resident, even though the
upper common cores are large enough for a prospective fixed-depth planting.

## 5. The standard recursive path is individually safe but globally incompatible

Let `P_4` be the Proskurowski--Ruskey transposition Hamilton path on
`D_4`.  Exhaustive H100 enumeration in the internal-owner class and the two
productive prefix channels gives q2-safe circuits on all thirteen path
edges.  Their minimum incidence lengths in that enumerated class, in path
order, are

```text
20,18,18,22,18,24,18,22,14,22,20,22,20.
```

For these shortest-safe classes the candidate counts are

```text
32,16,60,416,4,564,12,68,8,176,192,84,56.
```

Nevertheless the exact resource-selection CNF is unsatisfiable: one
cannot choose one circuit from these shortest-safe classes per PR edge
while keeping all owner and colour vertices disjoint.  Pairwise arc
consistency does not see the obstruction—all candidate domains remain
nonempty and unchanged—so the failure is genuinely global.

This does not obstruct a PR-based solution using another prefix channel,
longer circuits, controlled overlap, or a different branch order.  It proves
that “take one actuator from each enumerated shortest PR class” is not the
desired recursive grammar.

## 6. Context insertion and exact remaining obstruction

### 6.1 Right Dyck-tail concatenation is valid

If a frozen circuit is supported before coordinate `2s` and `W` is any
Dyck word appended on the right, the MSW concatenation identities

\[
 I(XW)=I(X)\Vert(2s+I(W)),\qquad
 D(XW)=D(X)\Vert(2s+D(W))                              \tag{6.1}
\]

preserve every selected/unselected incidence.  Every q2 backup tensors by
the common up-step set `U(W)`, and distinct tails separate supports.
Therefore the complete `D_3` and `D_4` certificates generate valid actuator
families under arbitrary **right** Dyck contexts.  This is a genuine
context-closure statement, but it produces disjoint aligned copies indexed
by the right tail; it does not connect different tail blocks and hence is
not by itself a spanning Catalan suffix-tree recursion.

### 6.2 Left insertion and primitive wrapping are not automatic

The Catalan recursion also needs transformations such as

\[
                         X\mapsto 10X,qquad X\mapsto1X0.       \tag{6.2}
\]

These alter the MSW prefix phase.  Literal coordinate insertion into a
valid circuit need not preserve its old selected incidences.  Thus `(6.1)`
does not give an insertion-closed grammar for `(6.2)`.

The finite results make the exact missing theorem sharp:

> **Context-generated suffix-tree actuator theorem.**  Find finitely many
> symbolic circuit schemas and context transition rules which recursively
> cover the PR `flip/insert` seams (or another Catalan spanning-tree
> recursion), while allowing a resource-disjoint selection whose aggregate
> q2 current is support-monotone and whose component endpoint permutation
> is one orbit.

Even that theorem would not finish residence.  The verified `D_4` output
has

\[
              51\text{ bad upper 2-collars},qquad
              40\text{ bad lower 2-collars},                 \tag{6.3}
\]

and minimum seam gap one on both shores.  Hence the residence lift must
use a phase clock, dwell, or prospectively planted cut-separated common
histories.  At source width `d+3`, it must be turn-faithful to both endpoint
mates.  If the original-owner lower palette is required, its aggregate
current must also be audited or repaired.

## 7. H100 certificates and independent verification

All substantive enumeration, SAT solving, verification, and hashes were
run on `ssh h100` in

```text
/dev/shm/t2_suffix_wave1b_20260813
```

The complete `D_4` enumerator/SAT search is

```text
scratch/search_t2_suffix_d4_spanning_actuator_sat_20260813.py
SHA256 8913f0a93ec247b9d1aecce99650731c2d650de51673ee0c4972bea94a82ded5
```

Its exact H100 output is

```text
scratch/search_t2_suffix_d4_spanning_actuator_sat_20260813.h100.out
SHA256 7545a319867dd3c7f32a13158dad41d2860d7e69a356858bbf1dd96e5160db06
```

The run used Kissat `4.0.4`, took `415.56` seconds, and had reported peak
RSS `843544` KiB.  Candidate retention is capped at `160` witnesses only
after the first safe length has been found; the cap therefore affects the
SAT menu but not the minimum-length proof.

The other-four-channel strict-improvement audit is

```text
scratch/audit_t2_suffix_d4_allprefix_minima_20260814.py
SHA256 314613957c054542bab7dbfaa5c54a90690a65c92c90934405c396c56ab26970
```

with H100 output

```text
scratch/audit_t2_suffix_d4_allprefix_minima_20260814.h100.out
SHA256 eb3b5c4880563d74b153e4eda7ca25a9e4c9da9135e4029a9c202ad43abd50b2
```

It took `281.58` seconds, had peak RSS `331488` KiB, found no improvement,
and reproduced `(0.2)`.  Together with the two-channel exhaustive search,
this proves the all-six-prefix internal-owner minima.  The independent
frozen-selection verifier is

```text
scratch/verify_t2_suffix_d4_spanning_actuator_certificate_20260813.py
SHA256 cae054de206c52c459b9dfc0fdb7ec4a37bbee8c64aadbb85f76b21f2990c24a
```

with H100 output

```text
scratch/verify_t2_suffix_d4_spanning_actuator_certificate_20260813.h100.out
SHA256 1655832f4bf249696433b4939a1f2ab936939142429507aac3083a4eea5b7aa0
```

It reconstructs the frozen selection, component action, exact common
intersections, lower-palette current, and both collar projections without
rerunning candidate enumeration.  It reports `PASS` and took `111.26`
seconds with peak RSS `742364` KiB.

The `D_3` verifier is

```text
scratch/verify_t2_suffix_s3_actuator_catalogue_20260813.py
SHA256 1bdf72f85dbcf690f6d358bca446e30405373031eef17975e8105e0e81da3327
```

with H100 output

```text
scratch/verify_t2_suffix_s3_actuator_catalogue_20260813.h100.out
SHA256 f00cf5209b15f66e69d771dc26d7077ce1559174f4ed89fce270537383a9f93f
```

The all-six-prefix strict-shorter audit for the four selected `D_3` edges is

```text
scratch/audit_t2_suffix_s3_selected_allprefix_minima_20260814.py
SHA256 bcb56e14223ce7c11a3c3fefcd64ce55f5586c5784c2f7951098f776f464b2c4
```

with H100 output

```text
scratch/audit_t2_suffix_s3_selected_allprefix_minima_20260814.h100.out
SHA256 d0d6fa5f3ba703e667ed5632dc072508cfe14255fde543a508fe0e9e3db7c0a6
```

and status `PASS` (`5.62` seconds, peak RSS `59444` KiB).

The PR-path compatibility audit is

```text
scratch/search_t2_suffix_pr_s4_compatible_selection_20260813.py
SHA256 40650474bf7e3910d7612259798ef5aded17aad2a9ba964f03a4300be8e200f2
```

and its H100 output has SHA-256

```text
41484ba09bc59f1056578af3a631eccd94a7b22369f3f108a1f04e2068a3dee0.
```

## 8. Sharp remaining gate

The aligned matching obstruction has been escaped finitely and
substantially: all suffix roots can be joined at `s=3,4`, with exact q2
support and actual one-component topology.  What remains is no longer
“find another local circuit.”  It is the two-part theorem

\[
 \boxed{\begin{array}{c}
 \text{prove a finite insertion-closed recursive actuator grammar for all }s,\\
 \text{then realize its selected seams in a residence-dilated,
 cut-separated, turn-faithful source host.}
 \end{array}}                                             \tag{8.1}
\]

The first line is forced by the nonfunctoriality of `(6.2)` and the PR
shortest-selection UNSAT result.  The second is forced by `(6.3)`.
