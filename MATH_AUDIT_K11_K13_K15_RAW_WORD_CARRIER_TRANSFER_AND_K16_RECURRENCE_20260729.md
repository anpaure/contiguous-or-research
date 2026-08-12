# Raw optimal words at `k=11,13,15`: exact carrier invariants and a `k=16` recurrence target

Date: 2026-07-29

Status: exact audit of the three retained optimal words and their reconstructed
central carriers; exact audit of the `k=15` Markov reduction chain; conditional
recurrence and explicitly labelled conjectures.  No `k=16` construction is
claimed.

## 0. Main conclusions

The common structure is now precise.

1. All three words have depth three.  Their third OR derivatives are Johnson
   Hamilton paths on the complete middle layer, and every internal positive
   coordinate run has length at least four.
2. The raw paths canonically recover rotation-equivariant cyclic factors.  At
   `k=11` the factor has one physical component.  At `k=13` and `k=15` it has
   two.  In both two-component cases the raw path is obtained by deleting one
   edge from each component and inserting one cross-component Johnson edge.
3. The exact seam arithmetic is

   ```text
   k=11: one cut, no seam, one missing q1 colour;
   k=13: two cuts, one lower-colour-recycling seam, one missing q1 colour;
   k=15: two cuts, one upper-colour-recycling seam, two missing q1 colours.
   ```

   The two `k=15` holes are installed literally at the two word endpoints.
   Thus lower-colour recycling is not the invariant.  The invariant is the
   hole/duplicate identity `H=E+1` together with a two-endpoint SDR.
4. The `k=15` compiler is substantially cleaner than the raw `k=11,k=13`
   compilers: it is a genuine one-core, `DA=DP`, where `P` is the maximal
   depth-three envelope.  All 2,657 deleted coordinate occurrences are
   isolated.  This isolates an exact matching-plus-independent-set compiler
   suitable for recurrence.
5. The `k=15` factor was reduced from nine components to two by three
   shadow-null alternating circuits of supports `4,6,4`.  Physical component
   count, not quotient component count alone, is the right topological
   potential because a quotient cycle of voltage `v` has `gcd(k,v)` lifts.
6. The direct `k=15 -> 16` incidence-dual lift has a sharp residence
   obstruction.  The final `k=15` factor has exactly 1,425 positive runs of
   length four.  Passing to its facet row shortens every such run to length
   three.  But `d(16)=3`, so a direct unchanged facet shore would need length
   at least four.  A `k=16` recurrence therefore needs a genuinely global
   run-raising dual or an independent resident rank-seven shore; bounded seam
   repair is not enough.

## 1. Frozen inputs

The canonical words and SHA-256 values are

```text
746b469af108558b14e7f6af0e3f76f9b6f39f70b3561e0258cc976650761850
    answers/k11.word

8d202e793d3317d2c3db76fef51f9d20d0e4e09fa2899a9686285cc01f4577d0
    answers/k13.word

f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b
    answers/k15.word
```

Their common raw-word census is

```text
74ff4c31f722d73055524ca8d4569ed4319ad6246b92823c4cd921cd190437e3
    scratch/raw_optimal_words_k11_k15_20260729.json.
```

The exact `k=15` component-reduction chain and compiler audits are

```text
cdd8bd2539e0bd5428e0762cecff9fe705e277db7c64588009de6fb03bbb8bec
    scratch/k15_fixed_matching_pbbs_resident_20260729/
        pbbs_component_reduction_chain.audit.json

5eeb04a61d8a085e89b05db9ca1075cfd64e5f95a9a35bcbb80711617579d125
    scratch/k15_fixed_matching_pbbs_resident_20260729/
        arbitrary_seams_compile.audit.json.
```

All three canonical words pass the literal exhaustive verifier and attain
their deadline lower bounds.

## 2. Basic depth-three data

Put

```text
r=(k+1)/2,  W=binom(k,r),  L=W+d,  h=r-d.
```

For the three odd cases:

| `k` | `r` | `W` | `d` | `h` | `L` |
|---:|---:|---:|---:|---:|---:|
| 11 | 6 | 462 | 3 | 3 | 465 |
| 13 | 7 | 1716 | 3 | 4 | 1719 |
| 15 | 8 | 6435 | 3 | 5 | 6438 |

Writing `D` for adjacent union and `T=D^3A`, each `T` is a permutation of
all rank-`r` masks and every one of its `W-1` transitions is a Johnson edge.

## 3. The maximal-envelope law

For a rank-`r` path `T=(T_i)` define its maximal depth-`d` preimage

\[
 P_p=\bigcap_{i=\max(0,p-d)}^{\min(p,W-1)}T_i,
 \qquad 0\le p<W+d.                                      \tag{3.1}
\]

### Lemma 3.1 (boundary staircase)

Suppose every internal positive coordinate run of `T` has length at least
`d+1`.  Then

\[
 |P_p|=
 \begin{cases}
 r-p,&0\le p<d,\\
 r-d,&d\le p<W,\\
 r-(W+d-1-p),&W\le p<W+d.
 \end{cases}                                             \tag{3.2}
\]

Consequently the rank histogram of `P` is

\[
 (r-d)^{W-d}(r-d+1)^2\cdots(r-1)^2r^2.                  \tag{3.3}
\]

#### Proof

Across a window of at most `d` Johnson transitions, residence prevents an
inserted coordinate from being deleted again.  Hence the deleted coordinates
are distinct, and the intersection loses exactly one coordinate per
transition.  The three ranges in (3.2) have window lengths `p+1`, `d+1`, and
`W+d-p`, respectively.  This proves both assertions.

The raw words give exactly:

| `k` | maximal-envelope ranks | word ranks | equal `A_p=P_p` |
|---:|:---|:---|---:|
| 11 | `3^459 4^2 5^2 6^2` | `1^11 2^55 3^399` | 395/465 |
| 13 | `4^1713 5^2 6^2 7^2` | `1^17 2^196 3^677 4^826 5^2 6^1` | 826/1719 |
| 15 | `5^6432 6^2 7^2 8^2` | `1^15 2^105 3^455 4^1365 5^4495 6^1 7^2` | 4493/6438 |

The pointwise envelope-minus-word gap histograms are

```text
k=11: 0^395 1^56  2^10  3^3   4^1
k=13: 0^826 1^678 2^196 3^18  4^1
k=15: 0^4493 1^1368 2^457 3^105 4^15.
```

These are containment gaps, not Hamming distances between masks.

## 4. Run distributions

### 4.1 Exact cyclic positive-run histograms

After restoring the hidden factor closures, the physical positive-run
histograms are

```text
k=11:
  4^143 5^132 6^55 7^44 8^22 9^11 10^22 11^11 12^11 14^11

k=13:
  4^429 5^299 6^208 7^221 8^117 9^130 10^104 11^13
  12^13 13^104 14^26 15^13 16^26 18^13

k=15:
  4^1425 5^1110 6^780 7^570 8^495 9^405 10^285 11^210
  12^270 13^150 14^165 15^75 16^90 17^45 18^45 19^60
  20^30 21^45 22^45 23^15 24^45 26^15 27^15 28^45.
```

All minima are exactly four; residence has no spare unit at the bottom.

For a strict rotation-spiral cycle factor with no coordinate constant on a
component, the number of positive runs is exactly the number `W` of Johnson
edges and their total mass is `rW`.  Thus their mean is exactly `r`.
Likewise the zero runs number `W`, have mass `(k-r)W`, and mean `k-r`.
This identity holds at every stage of the `k=15` Markov chain.

### 4.2 Linear boundary runs

In all three opened paths the positive runs of lengths below four are

```text
1^2 2^2 3^2,
```

and every internal positive run has length at least four.  This is not an
accident.  At the left boundary the first three distinct deletions terminate
one prefix run of each length `1,2,3`; dually, the final three insertions begin
one suffix run of each length.  Residence makes those six coordinates
distinct within each collar.

### 4.3 Facet erosion

For a cyclic rank-`r` row put `X_i=T_i intersection T_(i+1)`.  On each
coordinate, a positive run of length `ell` in `T` becomes a positive run of
length `ell-1` in `X`.  There is no coalescence.  Hence the lower-facet row
has minimum run three and the same multiplicities shifted down by one.

For the final `k=15` factor this creates exactly

```text
1425
```

facet runs of length three.

## 5. Hidden factors and exact seam arithmetic

The natural cyclic edge-orbit reconstruction gives:

| `k` | quotient component lengths | physical components | cut orbits | seam orbits |
|---:|:---|:---|---:|---:|
| 11 | `42` | `462` | 1 | 0 |
| 13 | `119,13` | `1547,169` | 2 | 1 |
| 15 | `426,3` | `6390,45` | 2 | 1 |

Every displayed quotient voltage is coprime to `k` (up to the orientation
and generator convention), so each quotient component has one physical lift.

The exact cut/seam colours are:

| `k` | edge | lower intersection | upper union | role |
|---:|:---|---:|---:|:---|
| 11 | `159--219` | 155 | 223 | cut |
| 13 | `2515--2395` | 2387 | 2523 | cut |
| 13 | `2167--2391` | 2135 | 2423 | cut |
| 13 | `2515--2391` | 2387 | 2519 | seam; recycles lower 2387 |
| 15 | `19065--26745` | 18553 | 27257 | cut |
| 15 | `18041--20081` | 18033 | 20089 | cut |
| 15 | `19065--18041` | 17017 | 20089 | seam; recycles upper 20089 |

Thus the decisive `k=15` seam deliberately duplicates a retained lower
colour: lower mask `17017` has load two.  Its upper colour `20089` has load
one in the linear path and is indispensable.  Every deeper crossing target
has another witness; the seam's only unique expected-rank crossing witness is
this upper-q1 colour.

### Lemma 5.1 (hole/duplicate balance)

Open `c` cycles of an exact lower-rainbow factor and add `c-1` Johnson seams.
Let `H` be the number of missing lower-q1 colours and

\[
 E=\sum_x(\lambda_x-1)^+
\]

the duplicate excess of their path loads.  Then

\[
                         H=E+1.                  \tag{5.1}
\]

#### Proof

There are `W` colours and `W-1` path transitions.  The `W-H` occupied
colours use one occurrence each and the excess uses `E` further occurrences.
Thus `W-1=(W-H)+E`.

The three cases are

```text
k=11: H=1, E=0
k=13: H=1, E=0
k=15: H=2, E=1.
```

In the two-endpoint compiler normalization, at most two missing cut colours
can be installed at the global endpoints.  Therefore the sharp q1 target is
not “every seam recycles”; it is `H<=2`, equivalently `E<=1`, together with
endpoint containment and the common one-core constraints.

## 6. Boundary target positions

The missing central lower targets are paid as follows:

| `k` | missing target | rank/depth | exact payment |
|---:|---:|:---|:---|
| 11 | 155 | q1/rank5 | `D^2A[0]=D^2A[462]=155` |
| 11 | 154 | q2/rank4 | `DA[463]=154` |
| 13 | 2135 | q1/rank6 | `A[1718]=2135` |
| 15 | 18553 | q1/rank7 | `A[0]=18553` |
| 15 | 18033 | q1/rank7 | `A[6437]=18033` |

For `k=15` these form two literal endpoint flags

\[
 18553\subset26745=T_0,
 \qquad
 18033\subset20081=T_{6434},                     \tag{6.1}
\]

each with one-coordinate difference.  More generally, a removed cut colour
is automatically contained in both endpoints of its cut edge.  After two
cycles are oriented into a path, the two unrecycled cut colours are therefore
eligible at the two outer maximal-envelope cells.  Eligibility is automatic;
simultaneous one-core feasibility is not.

The endpoint derivative flags make the contrast visible:

```text
k=11 left : 137 < 153 < 155 < 219
     right: 152 < 154 < 155 < 159

k=13 right: 2135 < 2167, with D A and D^2 A already equal to 2167

k=15 left : 18553 < 26745, and D A=D^2 A=D^3 A=26745 there
     right: 18033 < 20081, and D A=D^2 A=D^3 A=20081 there.
```

Here `<` denotes strict set containment at the corresponding boundary
position, not numerical order.

## 7. Shadow-load histograms of the opened carriers

Support, rather than load balance, is the stable invariant.  The exact first
three depth profiles are:

```text
lower q1
  k=11: 0^1 1^461
  k=13: 0^1 1^1715
  k=15: 0^2 1^6432 2^1

upper q1
  k=11: 1^199 2^131
  k=13: 1^937 2^272 3^78
  k=15: 1^3676 2^1229 3^100

lower q2
  k=11: 0^1 1^209 2^109 3^11
  k=13: 1^860 2^427
  k=15: 1^3632 2^1318 3^55

lower q3
  k=11: 1^12 2^55 3^55 4^43
  k=13: 1^156 2^222 3^235 4^102
  k=15: 1^902 2^1109 3^719 4^225 5^33 6^15

upper q2
  k=11: 1^33 2^45 3^55 4^32
  k=13: 1^224 2^219 3^181 4^65 5^25 6^1
  k=15: 1^1140 2^975 3^601 4^239 5^33 6^15

upper q3
  k=11: 3^1 5^21 6^22 7^11
  k=13: 1^14 2^51 3^53 4^64 5^52 6^13 7^26 11^1 12^12
  k=15: 1^59 2^332 3^255 4^239 5^270 6^106 7^74 8^30.
```

Except for the explicitly listed lower holes, every target is present.  In
particular the increasingly nonuniform upper loads do not obstruct exact
optimal words.

## 8. The `k=15` Markov switch chain

The all-depth resident source factor was compressed by three exact
alternating circuits:

| stage | quotient `(length,voltage)` rows | physical lengths | support | tight length-4 runs |
|:---|:---|:---|---:|---:|
| `F0` | `(258,10),(126,4),(37,1),(5,11),(3,4)` | `774^5,1890,555,75,45` | - | 1395 |
| `F1` | `(381,11),(40,4),(5,11),(3,4)` | `5715,600,75,45` | 4 | 1410 |
| `F2` | `(386,7),(40,4),(3,4)` | `5790,600,45` | 6 | 1425 |
| `F3` | `(426,11),(3,4)` | `6390,45` | 4 | 1425 |

Voltages are orientation-dependent; only their gcd with 15 and the displayed
lift counts are invariant.

The exact alternating circuits are

```text
support 4, rows 2,39,145,85:
  remove variables 18,274,1018,599
  add    variables 17,277,1016,597

support 6, rows 89,311,148,144,178,113:
  remove variables 626,2181,1041,1010,1248,795
  add    variables 628,2184,1038,1012,1249,793

support 4, rows 7,50,175,105:
  remove variables 53,351,1227,739
  add    variables 52,354,1226,736.
```

For every circuit:

1. the selected lower-owner deck and degree-two equations remain exact;
2. the `lower-q2` and `upper-q1` colour deltas are empty;
3. every lower and upper support remains complete at every depth;
4. minimum cyclic positive run remains four; and
5. collision-floor excess remains nine.

The first support-four circuit has disproportionate topological leverage.  It
rethreads quotient mass `258+126+37` into `381+40` and changes a voltage-10
cycle with five physical lifts into coprime-voltage cycles.  Hence physical
components fall from nine to four.  This proves that a component objective
must be evaluated after voltage lifting.

The tight-run count is not monotone under component descent.  These are
topology moves, not residence-slack moves.  Exhaustion through support eight
found 11,518 deck-safe circuits at the final two-component factor and every
one was topology-rejected.  The correct endpoint was therefore two cycles
plus one seam, not a forced Hamilton cycle.

## 9. Exact compiler anatomy

Let `Z_p=P_p-A_p`.  If `A_p subset P_p`, then

\[
 DA=DP                                                    \tag{9.1}
\]

is exactly the coordinatewise condition that no union edge loses a coordinate
present in `P_p union P_(p+1)`.  In the interior this says that the deletion
positions of each coordinate form an independent set; at a one-sided
boundary occurrence there is also a unary protection constraint.  If (9.1)
holds, then

\[
 D^3A=D^2(DA)=D^2(DP)=D^3P=T.                            \tag{9.2}
\]

The raw compiler error and deleted-run data are

| `k` | error cells at depths `0,1,2,3` | deleted-coordinate run histogram | maximum deleted run |
|---:|:---|:---|---:|
| 11 | `70,5,2,0` | `1^73 2^5 3^2` | 3 |
| 13 | `893,209,1,0` | `1^676 2^223 3^2` | 3 |
| 15 | `1945,0,0,0` | `1^2657` | 1 |

Thus only the canonical `k=15` word is literally a one-core relative to its
maximal envelope.

### 9.1 Exact `k=15` assignment decomposition

The generalized compiler assigns exactly 4,945 distinct targets:

```text
rank 1:   15
rank 2:  105
rank 3:  455
rank 4: 1365
rank 5: 3003
rank 7:    2 boundary residuals.
```

The first five rows comprise every nonempty mask of rank at most five:

\[
 \sum_{j=1}^5\binom{15}{j}=4943.                         \tag{9.3}
\]

A canonical assignment extracted from the retained word has envelope-rank
profile

```text
target rank 1: 15 positions of envelope rank 5
target rank 2: 105 positions of envelope rank 5
target rank 3: 455 positions of envelope rank 5
target rank 4: 1365 positions of envelope rank 5
target rank 5: 3000 positions of envelope rank 5,
               one of envelope rank 6, two of envelope rank 7
target rank 7: two endpoint positions of envelope rank 8.
```

The 1,493 unused positions are 1,492 repeated rank-five maximal cells and one
rank-six maximal cell.  Rank-five word values have multiplicity profile

```text
1^1896 2^780 3^277 4^43 5^6 6^1.
```

All ranks one through four occur exactly once.  The 2,657 deleted coordinate
occurrences by coordinate are

```text
157,163,186,165,156,160,185,156,188,190,176,179,196,209,191.
```

They are not point-balanced, yet (9.1) holds exactly.  Transitivity or point
balance is therefore not necessary for the finite compiler.

There are at least two distinct exact compiler points over the same carrier.
The canonical word and

```text
scratch/k15_from3_two_cycle_broad_seam_20260729/threadH_broad_seam.word
```

differ at 2,059 source positions, but their first, second, and third
derivatives are identical.  This is direct evidence that the one-core fibre
has substantial internal mobility after the carrier and boundary flags are
fixed.

## 10. The exact `k=16` obstruction and target

For `k=16`, the middle rank and width are

\[
 r=8,\qquad W=\binom{16}{8}=12870.                       \tag{10.1}
\]

The number of nonempty masks below rank eight is

\[
 \sum_{j=1}^7\binom{16}{j}=26332.                        \tag{10.2}
\]

Depth two supplies only

\[
 2W+\binom32=25743<26332,                                \tag{10.3}
\]

whereas depth three supplies `3W+6=38616`.  Hence

\[
 d(16)=3,\qquad h=5,\qquad B(16)=12873.                  \tag{10.4}
\]

### Proposition 10.1 (direct incidence-dual shore fails residence)

Take the final `k=15` factor `F3` and form its facet row

\[
 X_i=T_i\cap T_{i+1}.                                    \tag{10.5}
\]

Use `z+X_i` as the `z`-containing shore of a proposed rank-eight `k=16`
carrier, without rethreading the `X` chronology.  Then that shore contains
exactly 1,425 positive old-coordinate runs of length three.  Therefore it
does not satisfy depth-three residence.

#### Proof

Section 4.3 shortens each positive source run by exactly one.  The final
factor has exactly 1,425 source runs of length four.  Equation (10.4) requires
every internal positive carrier run to have length at least four.

This is a no-go only for the unchanged facet chronology.  A global braid may
cut, extend, merge, or externalize these runs.  It does prove that a bounded
collar correction cannot be the whole `k=16` recurrence: all 1,425 defects
must be changed or moved out of the internal chronology.

### 10.2 Exact two-shore interface for `k=16`

With a new coordinate `z`, the rank-eight layer splits evenly as

\[
 {cal A}=\binom{[15]}8,
 \qquad
 {cal B}=z+\binom{[15]}7,
 \qquad |{cal A}|=|{cal B}|=6435.                     \tag{10.6}
\]

If the `A` shore is cut into `a` paths and the `B` shore into `b` paths, a
single alternating block path has forced channel counts

\[
 AA=6435-a,\quad BB=6435-b,\quad AB+BA=a+b-1.            \tag{10.7}
\]

This identity is automatic.  The missing existence theorem is not the count;
it is a simultaneous choice of

1. an all-depth resident rank-eight `A` forest;
2. an all-depth resident rank-seven `B` forest with minimum positive run four;
3. cross incidences joining all blocks while preserving the two shadow
   towers and keeping every internal `z`-block long enough; and
4. an endpoint-compatible one-core compiler.

For such a depth-three `k=16` path, the maximal envelope would have profile

```text
5^12867 6^2 7^2 8^2.
```

The base one-core target family has

\[
 \sum_{j=1}^5\binom{16}{j}=6884                         \tag{10.8}
\]

members, plus the explicitly missing rank-six/rank-seven boundary targets.
If the first-shadow seam arithmetic leaves at most two holes, the exact
compiler target count is at most 6,886 in 12,873 positions.

## 11. Concrete recurrence conjectures

Everything in this section is conjectural unless explicitly called an
interface theorem.

### Conjecture 11.1 (odd two-component Catalan normal form)

For every odd `k=2m+1`, there is a rotation-equivariant lower-rainbow factor
on the upper middle layer such that

1. every quotient voltage is coprime to `k`;
2. there are at most two quotient components;
3. cyclic positive residence is at least `d(k)+1`;
4. every lower and upper fixed-window shadow required by the compiler is
   complete; and
5. the factor is reachable from a PBBS/Catalan selector by integral
   alternating circuits which preserve those four gates.

The `k=11,13,15` factors prove the conclusion at semilengths `5,6,7`; only
the `k=15` case currently has an audited shadow-null circuit chain.

### Conjecture 11.2 (two-boundary opening)

Every factor in Conjecture 11.1 admits one cut per component and at most one
cross seam such that

1. all upper targets survive;
2. internal residence survives;
3. lower-q1 hole count is at most two; and
4. the missing cut colours have an SDR into the two global endpoint cells.

The correct seam objective is lexicographic: preserve irreplaceable upper
witnesses first, then minimize lower `H=E+1`.  The `k=15` seam proves that
forcing lower-colour recycling can delete the optimum.

### Conjecture 11.3 (endpoint one-core Hall)

For the opened Catalan carriers of Conjecture 11.2, the exact assignment
system

\[
 S\subseteq P_p,qquad DA=DP,                            \tag{11.1}
\]

has an integral matching of all base targets of ranks at most `h=r-d`
together with the at most two boundary residual flags.

This is a concrete matching problem with adjacent omission conflicts.  It is
strictly stronger than ordinary Hall.  It holds for the retained `k=15`
carrier; the raw `k=11,k=13` words do not themselves prove this normal form.

### Conjecture 11.4 (run-raised incidence dual for even successors)

For an odd normal-form factor `F`, there is a global integral transform
`R(D(F))` which

1. preserves the incidence-dual lower/upper flag identities;
2. raises every required positive run to at least `d(k+1)+1`;
3. has at most two coprime-voltage components; and
4. admits the cross-shore braid (10.7).

When `d(k+1)=d(k)-1`, ordinary facet erosion already supplies the required
run length; this is exactly why the audited `k=13 -> 14` six-sector braid is
compatible.  At `15 -> 16`, the depths are equal and the 1,425 length-three
runs are the exact additional gate.

## 12. Proved versus open boundary

Proved:

- every numerical table and artifact identity in Sections 1--9;
- the boundary-staircase, endpoint-run, facet-erosion, and hole/duplicate
  identities;
- the three exact `k=15` Markov trades and their full protected signatures;
- `d(16)=3`, the 1,425-run direct-dual obstruction, and the exact `k=16`
  sector/compiler counts.

Not proved:

- a semilength-raising Catalan selector rule;
- availability of shadow-null component-reducing circuits for every odd
  `k`;
- a universal upper-safe two-boundary opening;
- the endpoint one-core Hall conjecture beyond the retained `k=15` carrier;
- a run-raised dual or complete `k=16` word.

The strongest transferable architecture is therefore

```text
odd Catalan all-depth factor
  -> shadow-null voltage-aware compression to at most two cycles
  -> upper-first seam with H<=2
  -> endpoint one-core compiler
  -> exact odd word,

and, for the even successor,

odd factor + run-raised incidence dual
  -> resident two-shore braid
  -> the same endpoint one-core compiler.
```
