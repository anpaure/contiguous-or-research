# Candidate1911 short-run span obstruction and complete paired-C8 census

Date: 2026-08-02  
Lane: L, disjoint candidate1911 route  
Status: **exact baseline ledger; solver-free residence lower bound; complete
negative H-C8 x D-C8 census**

## 1. Exact scope

Fix the authenticated candidate1911 factor

```text
scratch/ad_k17_complement_dual_trim3_splice_20260801/candidate1911.factor.tsv
SHA256 c082621d6444dc2283675882557d0240babb989f2d31847eb198fbe8b4612587
```

in its frozen orientation-0 chronology.  It is one quotient cycle of voltage
9 and one primitive 24,310-owner physical cycle.  Its upper rank-10 q1
palette is complete and its lower rank-7 q1 holes are

\[
                 H_7=\{\texttt{0x00e0f},\texttt{0x01547}\}.
\]

This note considers exactly one non-loop simple support-four assignment
cycle on `H` and one on `D`, applied simultaneously.  Parallel incidence
phases and atoms which individually select an opposite-base edge are retained;
only the simultaneous terminal `D/H` factor is tested.  Non-simple cycles,
loops, other supports, more than one cycle per shore, arbitrary compound
exchanges, other factors and occurrence/nonflat compiler moves are outside the
census.

There is no K17 word claim.  Source cells, occurrence ages, ranks above the
reported trim ledger, exterior intervals and the terminal compiler remain
separate gates.

## 2. Exact short-run and protected-ticket ledger

The frozen ledger source reconstructs the authenticated physical chronology
and emits every positive run of length below four.  It gives

```text
length 1       0
length 2    1173 = 69 * 17
length 3    3179 = 187 * 17
total       4352 = 256 * 17
```

The quotient key is `(quotient_start,length,bit-owner_phase)`.  Every key has
exact multiplicity 17.  The literal q1 occurrence table independently gives

```text
lower load histogram  1^874 2^249 3^18 4^1, holes 0x00e0f,0x01547
upper load histogram  1^878 2^247 3^18 4^1, no holes
```

and marks every load-one row as protected.  The sparse root-zero source-trim3
upper ledger lists every missing or unique-witness target.  Its exact hole
vector at ranks 10 through 16 is

\[
                     (0,1666,323,0,0,0,0),
\]

and its unique-witness vector is

\[
                     (14927,3214,731,0,0,0,0).
\]

The interval convention is exactly `[start,endpoint)`; trim three is applied
once, not twice.  This is a protected baseline casualty ledger.  Since the
paired-C8 census below has no q1-hole-monotone member and no all-69 member,
there is no qualified terminal factor on which to run a rank-11/12 casualty
comparison.  In particular the baseline numbers are not presented as a
deeper-upper verdict for any invalid max-hit row.

## 3. Outgoing-transition span lemma

For a physical length-two positive run beginning at quotient position `s`,
the four consecutive owner states have bit pattern

\[
                          0,1,1,0.
\]

Call

\[
                          I_s=\{s-1,s,s+1\}
\tag{3.1}
\]

its outgoing-transition span, with positions modulo 1430.  An old quotient
transition here means both its successor owner and its signed phase increment;
a same-head rephasing is a changed transition.

### Lemma 3.1 (span persistence)

If a terminal degree-two factor retains all three old transitions in `I_s`,
then the corresponding old length-two run orbit survives.

#### Proof

The three retained transitions keep the four old owners as one path.  Any
terminal traversal uses that path in its old order or its reverse order, and
both orders have bit pattern `0,1,1,0`.  The `Z_17` translate gives the same
statement for all 17 physical copies.  Hence destroying the orbit requires
changing at least one transition in (3.1).  ∎

The 69 length-two rows contain the following 67 starts:

```text
9,32,42,52,86,101,104,112,116,171,208,245,310,327,336,353,
367,372,386,390,406,462,487,492,511,528,551,558,619,631,667,
672,712,770,790,796,816,835,843,849,853,897,919,922,941,950,
966,1024,1055,1058,1076,1082,1085,1104,1139,1155,1192,1198,
1210,1229,1241,1285,1295,1343,1358,1363,1417.
```

Their spans `I_s` are pairwise disjoint.  The complete certificate is
`length2_disjoint_spans.tsv`; the two omitted starts are exactly 559 and 851.
Thus any rethread of this fixed factor which raises the minimum positive run
from two to at least three changes at least **67 old quotient transitions**.
This conclusion is independent of q1 and of the finite C8 census.

### Corollary 3.2 (bounded paired-C8 no-go)

A support-four `D` assignment cycle deletes old outgoing transitions only at
its four owner tails.  A support-four `H` cycle deletes old outgoing
transitions only at the four base predecessors of its changed `H` incidences.
Simultaneous overlap can reduce, but cannot increase, their union beyond
eight.  Since `8<67`, an H-C8 x D-C8 exchange cannot remove every old
length-two run orbit.  It cannot attain minimum run three, hence cannot attain
the required minimum run four.

A single one-shore C8 is also topology-impossible from the one-cycle base:
its assignment 4-cycle is odd, so multiplication changes the sign of the
owner successor permutation, while every 1430-cycle has the base sign.  The
paired 4+4 shell is the smallest two-C8 shell not excluded by sign alone.

## 4. Exact q1 predicates

For a terminal factor write `mu'_10,mu'_7` for its q1 occurrence loads.  The
census distinguishes:

1. **coefficientwise neutral:** `mu'_10=mu_10` and `mu'_7=mu_7`;
2. **coverage neutral:** the terminal hole sets are exactly `empty,H_7`;
3. **hole monotone:** the upper hole set is empty and the lower hole set is a
   subset of `H_7`.

The third is weakest.  Every changed lower turn is recomputed on the union of
affected owners and every changed upper turn on the union of affected facets.
No isolated H and D marginal vectors are added on overlaps.

## 5. Complete H-C8 x D-C8 census

For one shore, the raw assignment graph has an arc `u -> v` for every literal
nonselected incidence from owner `u` to the facet occupied by owner `v` in the
old shore matching.  Loops are omitted but parallel phases are distinct.  A
DFS enumerates every simple directed 4-cycle, roots it at its least incidence
id and deduplicates by its complete sorted `(tail,new incidence)` map.  This is
complete for the stated atom class.

The exact banks are

```text
H raw arcs     11440       H-C8 atoms  1386
D raw arcs     11439       D-C8 atoms  1383
Cartesian pairs                         1916838
```

Every pair is first tested for terminal edge-disjointness.  For every
terminal-valid pair the evaluator reconstructs the simultaneous affected
turns, the contracted component permutation and signed voltage.  It does not
assume that either atom is legal in isolation.  The exact result is:

| row | count |
|---|---:|
| terminal-valid pairs | 650,509 |
| pair-rescued terminal pairs | 2,741 |
| connected pairs | 156,627 |
| connected, nonzero-voltage pairs | 150,826 |
| upper-q1-complete pairs | 2,215 |
| no-new-lower-hole pairs | 2,225 |
| hole-monotone pairs | **0** |
| coverage-neutral pairs | **0** |
| coefficientwise q1-neutral pairs | **0** |

Thus the two individual weak q1 projections are disjoint: no terminal-valid
pair is even hole-monotone, before imposing topology or residence.

Independently, the exact 69-orbit hit histogram over all 1,916,838 pairs is

```text
hits  0       1       2       3       4      5    6   7
rows  611494  755681  402492  120566  23101  3153 334 17
```

The maximum is only seven.  The 17 maximizing rows are frozen in
`paired_c8.max_hit.tsv`; six are terminal-valid and three are connected.
None of the six terminal-valid maximizing rows is q1 coefficientwise neutral.
There is no all-69 row and there is no hole-monotone row, so both the mandatory
all-69 replay branch and the deterministic running-maximum sample branch are
empty.  No best factor is emitted.  This is a negative theorem, not an
unevaluated candidate.

## 6. H100 execution and independent audit

The finite census ran only on one H100 CPU core in

```text
/home/amodo/or15/work/laneL_candidate1911_residence_20260802
```

with GCC C++20, `-O3 -DNDEBUG -Wall -Wextra -Wpedantic` and the two inherited
library-only diagnostics suppressed (`-Wno-range-loop-construct` and
`-Wno-unused-function`).  The run was pinned to core 30, used 7,168 KiB peak
RSS, took 4.38 seconds wall time, and exited zero.  No local finite search was
run.

The independent audit checked atom completeness, terminal recomputation, q1
deltas, topology/voltage signs, the H/D transition-tail map, all arithmetic,
the 67-span certificate and the 17-row maximum-hit ledger.  The JSON is a
result payload rather than a self-hashing manifest, so the binding hashes are
listed here explicitly:

```text
canonical factor
  c082621d6444dc2283675882557d0240babb989f2d31847eb198fbe8b4612587

baseline ledger source
  df5700e3d1c3e7868994b8265b400adf4767b8332efd3f3d54cf6a069b94973a
baseline audit JSON
  e693686da5ca69857cdce9a10ddd399f09d19e3299a44b872d279ea660ad062a
physical short-run table
  924388ac63d40dc50a20cc2c836dc7735ebd937479c599bc1745edcb37cfaede
short-run orbit table
  daa152692a0278528a7f935fc46ffedf256f6757a419d19b6801fd3b818ce89b
q1 protected ledger
  ffc97cb59410344e50e49ffba74b452c3ec92e4d143a0293ea26eed4b6f75852
root-zero protected upper ledger
  3d9b889bbb115c8cc5b5e954c5d04c0d2dac06a1a05526a1d9e307d1f8993a3f
67-span certificate
  eb8c935a48b2ffbca9a3b250cc019c1b9f62b027ab01d02975b350728f1c387e

paired-C8 main source
  dbe3b300b0c93ce14568d7aba5fc86d3ec5cb87f1c5b6f185bb1e8a877d67ac2
included independent core
  dbf074561eaa31c8fb463eb210bdcb3682b294787dc270c992b51225964443d0
frozen atlas source
  f3599e0a83f1aa2f51d99a914222be6c154a9bbb48bbdd46961dabc2d3cea939
H100 binary
  9cd61ca4aefa56be39addc17e6474fe270f243086cfc4f3414cd5ef32fb8d554
paired-C8 audit JSON
  5e175c4b7ff21d27e314e363142c8cea0d4cc7795f69a76705a72c2c80182cdb
maximum-hit ledger
  7febc7e471b9a4c924e8cc4fd999e448a8b50dc03d3fd67fb8008f92f07080b8
stdout / time ledger
  db51803641a4235895ed5bab600cbecd96932b10a0920edeeaf99f3de1f32061
  2134633c6c6cce556a7bee3561a23d7337d9dced0f4b94f8da65e8d6d056a332
```

## 7. Consequence and remaining route

The paired C8/`3+1` route is closed twice: by the solver-free 67-transition
residence obstruction and by the complete zero-count q1 intersection.  A
residence repair inside the fixed candidate1911 owner factor must therefore
be a genuinely large correlated rethread changing at least 67 old quotient
transitions, or must leave this flat factor model through an occurrence-level
or nonflat compiler actuator.  No conclusion is drawn about those larger
classes.
