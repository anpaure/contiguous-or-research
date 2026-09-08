# k=13 after extracting the transferable k=11 structure

Date: 2026-07-27

> **Superseding status, 2026-07-28.**  Both finite targets discussed in the
> chronological body are now exact:
>
> \[
> \nu(13)=1719=B(13),\qquad \nu(14)=3434=B(14).
> \]
>
> The authoritative certificates are
> `scratch/k13_res0_onehole_repair_history16x5.path_best.linear.word` and
> `scratch/k14_intersection_sixpiece_hallpass_004a.word`.  The k=14 six-piece
> braid and verification are recorded in
> `MATH_K14_EXACT_3434_CERTIFICATE_20260728.md`.  Statements below describing
> either case as unresolved are retained only as research history.

## 0. Settled source theorem at `k=11`

The transfer source is a proved optimum, not a heuristic seed:

```
nu(11)=465=B(11),    N(11)=466.
```

The authoritative word is

```
scratch/sigma_sat_k11_465.word
sha256 746b469af108558b14e7f6af0e3f76f9b6f39f70b3561e0258cc976650761850
```

Both `scratch/sigma_calibration_harness` (all 108,345 intervals) and the
independent suffix-state verifier `scratch/sigma_calibration_verify_or_suffix`
cover all 2,047 nonempty masks with zero misses.  The deadline lower bound is
465, so this proves optimality.  Full audit and reproduction record:

```
scratch/sigma_calibration_final_k11_audit.md
K11_EXACT_465_SEARCH_CERTIFICATE_20260727.md
```

## 1. Priority correction

The depth parameter is `d=3` at `k=13` and throughout the unresolved
`d=3` family through `k=22`, except for the genuinely different tight
case `k=14`, where `d=2`.  (`k=12` also has `d=2`, but is already solved.)
Consequently the active exact search remains `k=13`; `k=14` is frozen at
the certified interval already on record.

The useful information transferred from the exact `k=11` words is not a
one-coordinate marginal.  It is the joint normal form

```
resident lower-colour Hamilton cycle
+ nested lower rainbow
+ simple upper excess
+ compatible compiler ownership.
```

The run histogram and the upper-excess histogram can both be optimal while
the compiler is still impossible.  Their alignment with the nested edge
colours is therefore essential.

## 2. The all-shadow front

The certificate

```
scratch/k13_shadowneutral_res104.certificate.json
```

lifts to one physical cycle of length `1716` and independently covers every
lower and upper shadow at every possible depth `q=1,...,6`.  Its sole defect
is residence:

* `13` middle-coordinate runs have length two;
* `91` middle-coordinate runs have length three;
* equivalently there are eight translation orbits of short runs.

The upper immediate-shadow load is already at the exact integrality floor:
`858` targets have load one and `429` have load two.  Thus the seed is an
exact global rainbow object separated from compiler eligibility only by
`104` short runs.

The carrier audit makes this exact.  The cyclic maximal preimage misses `299`
middle-coordinate carrier incidences at `273` positions.  These empty
carrier clauses are precisely the `104` short runs.  No cut to a length
`W+3` open word repairs them: the best cut removes only six of the `299`
empty incidences.

## 3. The joint-compiler front

The direct quotient SAT model jointly chooses the central sigma map and the
depth-three compiler entries.  It has been calibrated by recovering a new
independently verified exact `k=11` word and by proving incompatible fixed
`k=13` seeds UNSAT.

Starting from the first joint `k=13` seed, the number of quotient vertices
whose `D^2` cell is not the complete outgoing lower colour has descended

```
25 -> 19 -> 12 -> 8 -> 7.
```

The current `B=7` certificate is

```
scratch/sigma_jointcompiler_k13_d2descent_b7_r2.certificate.json
```

and extracts to a word of length `1719` covering `7762/8191` masks.  Its
remaining misses are exactly

| rank | misses | translation orbits |
|---:|---:|---:|
| 2 | 13 | 1 |
| 3 | 13 | 1 |
| 6 | 91 | 7 |
| 8 | 221 | 17 |
| 9 | 91 | 7 |

The total is `429=C_7`, or `33=C_7/13` translation orbits.  This numerical
identity is recorded as a diagnostic, not yet asserted as a conservation
law.  With the middle cycle fixed, the compiler can cover both missing
rank-two/rank-three orbits in `1.72 s`.  The resulting word covers
`7788/8191`; only ranks `6,8,9` remain, with `7,17,7` missing orbits.

## 4. The two fronts are globally separated

The all-shadow and joint-compiler seeds are not two coordinate descriptions
of one nearby object.  Their quotient sigma maps differ on `128/132` raw
choices.  Exhausting all affine relabellings improves this only to `123/132`
different choices.  Even after affine relabelling, quotient rotation, and
reversal, at most one of the seven flat-`D^2` bad vertices aligns with a
residence collar in both mask and chronological position.

Thus a small interpolation between the two certificates is not available.
The all-shadow seed should be used to learn legal circuit types; the joint
seed is the closer exact-word search state.

## 5. Current exact searches

The active searches are now:

1. continue the flat-`D^2` descent from seven to zero;
2. from the `B=7` seed, impose compiler ranks `2,...,6` and the two missing
   upper shadows jointly;
3. from the all-shadow seed, impose residence while preserving all six
   shadow sides;
4. enumerate longer and non-simple shadow-neutral endpoint circuits obtained
   from the arity `32/39/41` overlays between exact `k=11` solutions.

No timeout is interpreted as UNSAT.  An exact claim will be made only after
extracting a length-`1719` word and passing the independent all-interval OR
verifier on all `8191` nonzero masks.

## 6. Bridge breakthrough

The smallest honest central bridge is SAT.  Starting from the all-shadow
seed and freeing only `60/132` quotient choices produced

```
scratch/root_k13_bridge_res104_f60.certificate.json
```

in `25.78 s`, with one quotient cycle of voltage seven, zero depth-three
residence defects, and complete central lower-`q=2` coverage.  It also has
both `q=3` shadows complete.  Only six upper-`q=1` and three upper-`q=2`
orbits are absent.

With this central cycle fixed, the exact flat-`D^2` compiler covers every
lower mask of ranks `1,...,6` in under three seconds.  The extracted
length-`1719` word covers `8074/8191`; its only misses are `78` rank-eight
and `39` rank-nine masks.

A k=11-style directed endpoint five-cycle then preserves residence,
lower-`q=2`, both `q=3` shadows, connectivity, and nonzero voltage while
reducing upper-`q=2` holes from three orbits to two.  Recompiling all lower
ranks gives

```
scratch/root_k13_bridge_q2h26_fixed_full_lower.certificate.json
```

whose best length-`1719` cut covers `8087/8191`.  The complete residual is
now exactly eight upper-shadow orbits: six at rank eight and two at rank
nine (`104` physical masks total).

Appending those `104` missing masks literally gives an independently
verified universal word of length `1823`:

```
scratch/k13_upper1823.word
sha256 d7c72e89679ca56a88d35324bf49ee8b168a17c7ddc3ad2596bbf3c2f71d9590
```

Consequently the certified numerical interval improves immediately to

\[
1719\le \nu(13)\le 1823.
\]

This fallback bound is not the active target; upper-shadow hole-budget
descent is running from `(H_1,H_2)=(6,2)` toward `(0,0)` while preserving
residence, the nested lower rainbow, and the complete lower compiler.

Two further exact endpoint circuits improve the upper residue.  A length-8
cycle changes `(6,2)` to `(5,2)`.  An anchored length-11 cycle then changes
`(5,2)` to `(5,1)`.  Both moves preserve residence, the complete lower
compiler interface, connectivity, and all audited deeper shadows.  The
latest compiled length-`1719` word is

```
scratch/k13_bridge_l11_q1h65_q2h13.compiled.word
```

and covers `8113/8191`, missing only `65` rank-eight and `13` rank-nine
masks.  Appending these gives the independently verified fallback

```
scratch/k13_upper1797.word
sha256 e53f2cfab173ad1256340ea5160e5cd5c259d50c2b933c980135b2e2565d6580
```

so the current certified interval is

\[
1719\le \nu(13)\le 1797.
\]

The `1797` completion is optimal for this fixed `1719` prefix.  Its `65`
missing rank-eight and `13` missing rank-nine masks form an inclusion
antichain: no missing rank-eight mask lies inside a missing rank-nine mask.
All new witnesses ending at one appended position form a chain, so at most
one of these 78 targets can be realized per new endpoint.  Hence every
append-only completion needs at least 78 entries, and the stored completion
meets this lower bound.

## 7. Both depth-two sides are simultaneously exact

The final upper-`q=2` hole is not a structural obstruction.  Starting from
the closest upper-exact near-certificate and freeing `60/132` quotient
choices produced

```
scratch/root_k13_nearB_q1free_exactq2_f60.certificate.json
```

in `18.94 s`.  It is one translation-equivariant quotient cycle of voltage
eight whose lift has length `1716`, with:

* zero depth-three residence violations;
* all `1287` lower-`q=2` masks;
* all `715` upper-`q=2` masks;
* all `286` upper-`q=3` masks; and
* `1079/1287` upper-`q=1` masks, hence exactly sixteen missing translation
  orbits.

Its lone central lower-`q=3` orbit hole is not part of the remaining gate.
With the central cycle fixed, the exact depth-three multirow compiler is SAT
in `0.065 s` and gives

```
scratch/k13_q1h16_exactq2.compiled.word
```

of length `1719`.  This word misses exactly the `208=16*13` upper-`q=1`
masks and nothing at any other rank.  Therefore the current central search
can impose only

```
residence 3 + exact lower q2 + exact upper q2
```

and minimize the upper-`q=1` quotient-hole count from `16` to zero.  The
lower compiler is already proved feasible at this endpoint; lower-`q=3`
need not be included in the expensive central SAT model.

## 8. The transferable k=11 distributions

The exact equivariant `k=11` central certificate has an `X`-run histogram

```
3^143, 4^132, 5^55, 6^44, 7^22, 8^11,
9^22, 10^11, 11^11, 13^11,
```

with mean five and minimum three.  Thus residence is attained sharply: 143
of the 462 coordinate runs have the minimum permitted length.  Its upper
depth-one load profile is the integrality-floor design

```
1^198, 2^132,
```

so all 330 targets occur and the 132 forced excess units are simple.  Each
coordinate lies in exactly 84 excess masks.

For comparison, the exact-`q=2` `k=13` bridge has `X`-run histogram

```
3^455, 4^260, 5^260, 6^169, 7^104, 8^91,
9^169, 10^65, 11^13, 12^26, 13^26, 14^39,
15^13, 16^26,
```

with mean six and the same minimum three, but its upper depth-one profile is

```
0^208, 1^533, 2^468, 3^65, 4^13.
```

The residence distribution is therefore already of the correct qualitative
type.  What remains is to turn `208` holes plus `208` avoidable overload
units into the target floor profile `1^858,2^429`.  The useful transferable
object is not either marginal histogram alone, but the alignment of the
simple excess design with the nested lower-`q=2` colours.

## 9. First upper-q1 descent with both q2 sides fixed

The sixteen-hole state is not frozen.  A native length-six endpoint circuit
first produced

```
scratch/k13_q1h15_exactq2.certificate.json
```

with fifteen upper-`q=1` orbit holes, zero residence defects, both `q=2`
sides exact, all shadows at depths `3,...,6` exact, and quotient voltage six.
Its exact lower compiler solves in `0.014 s`, yielding a length-`1719` word
whose only misses are `195=15*13` rank-eight sets.

An exhaustive length-`2,...,8` endpoint-circuit scan from the sixteen-hole
state then found the stronger

```
scratch/k13_q1h14_exactq2_l8.certificate.json
```

with fourteen upper-`q=1` orbit holes, residence zero, both `q=2` sides
exact, and quotient voltage eight.  Its only other central defect is the
single lower-`q=3` orbit represented by `337`; the compiler repairs it.  The
compiled word

```
scratch/k13_q1h14_exactq2_l8.compiled.word
```

has length `1719` and misses exactly `182=14*13` rank-eight masks.  Thus the
active central residual has now descended

```
16 -> 15 -> 14
```

without sacrificing either depth-two rainbow.  This does not yet improve
the certified universal upper bound `1797`, but it proves that upper-`q=1`
deficiency is mobile inside the exact-`q=2`, resident solution space.

The descent continued.  An alternate thirteen-hole geometry admits a
length-two circuit producing

```
scratch/k13_q1h12_exactq2_l2.certificate.json
```

with residence zero, quotient voltage ten, both `q=2` sides exact, and every
shadow at depths `3,...,6` exact.  Its load profile on the 99 upper-`q=1`
quotient targets is

```
0^12, 1^49, 2^32, 3^5, 4^1.
```

The fixed compiler is SAT and the resulting length-`1719` word misses
exactly `156=12*13` rank-eight masks.  Hence the authoritative compiled
descent is now `16 -> 15 -> 13 -> 12`.

A separate compiler-SAT near-face was obtained by a length-six circuit:

```
scratch/k13_q1h11_upperq2near_corefeasible_l6.certificate.json
```

It has eleven upper-`q=1` orbit holes, one upper-`q=2` orbit hole (representative
`1019`), exact lower `q=2`, residence zero, and one compiler-repairable lower
`q=3` hole.  Its compiled word misses `143` rank-eight and `13` rank-nine
masks.  Thus the two active local fronts are `(H_1,H_2)=(12,0)` and
`(11,1)`; repairing the latter's single upper-`q=2` orbit without increasing
`H_1` gives the next valid descent.

That repair is now complete.  The length-three endpoint circuit

```
429: [4,12] -> [4,11]
1333: [6,12] -> [6,7]
603: [7,11] -> [7,8]
```

closes upper-`q=2` representative `1019` while retaining eleven upper-`q=1`
orbit holes, residence zero, exact lower `q=2`, and nonzero quotient voltage.
The resulting certificate and compiled word are

```
scratch/k13_q1h11_exactq2_repaired_l3.certificate.json
scratch/k13_q1h11_exactq2_repaired_l3.compiled.word
```

The one lower-`q=3` orbit hole is compiler-repairable; the compiler is SAT in
`0.097 s`.  The word has length `1719` and misses exactly `143=11*13`
rank-eight masks.  Therefore the authoritative compiled descent is now

```
16 -> 15 -> 13 -> 12 -> 11.
```

This is the first successful two-stage move that temporarily opened a shadow
to improve upper `q=1` and then closed that shadow without returning the
gain.  It establishes a concrete mechanism for crossing local minima of the
exact-`q=2` face.

A further length-four endpoint circuit gives the current authoritative
compiled state

```
scratch/k13_q1h10_exactq2_l4.certificate.json
scratch/k13_q1h10_exactq2_l4.compiled.word
```

with residence zero, both `q=2` sides exact, quotient voltage three, and a
SAT lower compiler.  Its length-`1719` word misses exactly `130=10*13`
rank-eight masks.  On the 99 upper-`q=1` quotient targets its load profile is

```
0^10, 1^52, 2^33, 3^2, 4^2.
```

The exact floor profile is `1^66,2^33`: all 33 load-two targets are already
correct, and the ten avoidable units are concentrated in four donor orbits

```
1271^3, 1517^4, 1523^4, 1725^3.
```

The ten holes are represented by

```
503,893,927,957,1011,1463,1883,1965,2747,2775.
```

There are 126 direct donor-to-hole matchings satisfying the donor capacities,
but none has zero endpoint-incidence imbalance.  Their minimum imbalance has
`L1=28`; hence at least fourteen additional simple compensator arcs are
necessary even before residence and depth-two constraints.  Exact upper
balance is therefore not a ten-move local repair of this certificate.

A length-eight circuit reaches nine upper-`q=1` holes with residence and both
`q=2` sides exact, but opens lower-`q=3` representative `99`; its compiler is
UNSAT.  Exhaustive simple endpoint cycles of support at most seven and pairs
with total support at most eight cannot repair it while retaining nine holes.
The nine-hole state is a genuine nonlocal repair target, not yet a compiled
improvement.  Thus the certified compiled descent currently stops at ten.

There is also an eleven-hole candidate with both `q=2` sides exact, but it
opens three lower-`q=3` orbits and its fixed compiler is UNSAT.  This is an
important scope correction: lower-`q=3` central defects are sometimes, but
not always, repairable by the multirow compiler.  It is retained only as a
targeted repair state, not counted as progress toward an exact word.

## 10. July 27 late update: the canonical-core verdict was too strong

The nine-hole certificate above is not globally compiler-UNSAT.  Only the
fixed canonical cyclic core is UNSAT.  The unrestricted linear depth-three
compiler solves it in `0.24 s`:

```
scratch/k13_q1h9_exactq2_l8.certificate.json
scratch/k13_q1h9_exactq2_l8.linear.compiler.out
```

Its compiled word misses the expected `117=9*13` rank-eight masks plus one
linear-boundary rank-nine mask.  This reopened the exact-`q=2` descent.

## 11. Exact compiler Hall obstruction

Pointwise canonical-core reachability is not a joint compiler criterion.  On
an upper-perfect, residence-zero candidate, deletion shrinking reduces the
compiler conflict to the four physical masks

```
X       = 5410 = {1,5,8,10,12},
X+{2}   = 5414,
X+{3}   = 5418,
X+{4}   = 5426.
```

The three rank-six extensions each have one feasible depth-two carrier.  The
rank-five root has exactly those same three feasible carriers: its five other
raw windows are blocked by the last required occurrences of coordinates
`6,9,11,7,0`.  Thus four targets have only three cells.  Translation gives a
52-target/39-cell Hall witness of deficiency thirteen.  Reusable audits:

```
scratch/k13_corefeasible_l10_rank56_mus_individual.json
scratch/k13_corefeasible_l10_rank56_mus_orbits.json
scratch/k13_corefeasible_l10_rank56_hall.json
scratch/sigma_compiler_rank_hall.py
```

The related bad lower-`q=3` orbit `393` gives twelve disjoint Hall components,
each `10` targets versus `9` cells.  A lower-`q=3` central hole is compiler-
benign only when maximal erosion supplies a safe depth-zero representative.
The neutral repair below replaces bad orbit `393` by benign orbit `225` and
creates the missing depth-zero slot in every translate.

## 12. Authoritative compiler-valid descent to six holes

A two-edge switch first gives

```
scratch/k13_q1h8_exactq2_res0_l2.certificate.json
```

with residence zero, both depth-two shadows exact, Hall deficiency zero, and
a SAT unrestricted compiler.  A neutral six-edge change followed by a
seven-edge change reaches six holes but temporarily creates bad orbit `393`.
A second neutral six-edge switch repairs that Hall defect without losing any
upper gain.  The authoritative state is

```
scratch/k13_q1h6_neutralB_l6.certificate.json
scratch/k13_q1h6_neutralB_l6.linear.word
scratch/k13_q1h6_neutralB_l6.linear.compiler.out
```

Its exact invariants are:

```
upper q1 holes:      6 quotient orbits = 78 physical masks,
lower/upper q2:      exact,
residence defects:  0,
lower q3 hole:       benign orbit 225,
all-lower Hall:      deficiency 0,
linear compiler:     SAT.
```

The seam is solved as well.  There are 507 cuts whose omitted upper-`q=1`
and upper-`q=2` carriers remain represented.  Cut 7 produces a length-1719
word missing exactly the 78 rank-eight masks and nothing else:

```
scratch/k13_q1h6_neutralB_l6.cut7.word
scratch/k13_q1h6_neutralB_l6.cut7.certificate.json
scratch/k13_q1h6_neutralB_l6.cut7.hall.json
scratch/k13_q1h6_neutralB_l6.cut7.compiler.json
```

Consequently, after a safe cut, the finite residual is literally upper
`q=1`; neither the lower compiler nor the boundary contributes a hidden miss.

## 13. Current nonmonotone bridge at five holes

The six-hole upper-load profile is

```
0^6, 1^58, 2^32, 3^2, 4^1.
```

Direct donor-to-hole routing has minimum endpoint imbalance six.  Hence at
least three compensator arcs and at least nine changed rows are necessary,
which explains the exhaustive failure of direct exact-`q=2` circuits through
length ten.

A randomized alternating-cycle sampler found the correct nonmonotone move: a
three-edge switch reduces six upper-`q=1` holes to five while opening exactly
one upper-`q=2` orbit, representative `2991`.  It preserves residence zero,
exact lower `q=2`, Hall deficiency zero, and compiler SAT:

```
scratch/k13_q1h5_q2u1_res0_l3.certificate.json
```

The remaining upper-`q=1` holes are `503,893,927,1011,1965`.  At this stage
the active gate was to restore upper-`q=2` orbit `2991` without increasing
those five holes.  Before that repair, the rigorous numerical bound was

```
1719 <= nu(13) <= 1797.
```

## 14. Five-hole debt repaired exactly

The temporary-shadow bridge closes.  A Hamming-nine quotient repair, solved
in `110.1 s`, restores upper-`q=2` orbit `2991` while keeping all five upper
`q=1` gains:

```
scratch/k13_q1h5_repairu2_hamming9.certificate.json
```

The repaired chronology has one quotient cycle of voltage ten, residence
zero, both `q=2` sides exact, and the quotient upper-load profile

```
0^5, 1^60, 2^31, 3^2, 4^1.
```

Its all-lower Hall graph has deficiency zero and the unrestricted lower
compiler is SAT in `0.27 s`.  There are 468 jointly upper-safe cuts.  At cut
7 the exact length-1719 word misses precisely the five physical translation
orbits at rank eight—65 masks—and no boundary mask:

```
scratch/k13_q1h5_repairu2_hamming9.cut7.certificate.json
scratch/k13_q1h5_repairu2_hamming9.cut7.hall.json
scratch/k13_q1h5_repairu2_hamming9.cut7.compiler.json
scratch/k13_q1h5_repairu2_hamming9.cut7.word
```

This is a genuine missing-mass descent from 78 to 65; it is not merely a
trade between adjacent shadow ranks.

Appending the 65 missing masks literally gives an independently verified
universal word of length 1784:

```
scratch/k13_upper1784.word
scratch/k13_upper1784.report.json
scratch/k13_upper1784.verify1.out
scratch/k13_upper1784.verify2.out
sha256 f51311f657458f9daa440a421dbbc6d288051e00698c0fd237340f5d319d0b7f
```

Both the exact interval verifier and the independent suffix-state verifier
report all `8191/8191` nonzero masks.  Therefore the certified interval is
now

```
1719 <= nu(13) <= 1784.
```

## 15. The repeated nonmonotone mechanism at four holes

The same three-edge motif applied to the repaired five-hole state reduces
upper `q=1` from five holes to four while opening one lower-`q=2` orbit,
representative `233`:

```
scratch/k13_q1h4_q2l1_res0_l3.certificate.json
```

It preserves residence zero and exact upper `q=2`.  As predicted by the Hall
analysis, the missing lower orbit creates deficiency twelve and makes the
lower compiler UNSAT.  The active bounded-Hamming repair is therefore:

```
upper q1 holes <= 4,
upper/lower q2 exact,
residence defects = 0,
Hall deficiency = 0.
```

Local simple repairs through length eight are exhausted.  Hamming-nine and
direct Hamming-thirteen SAT repairs are running.  Until one passes all-lower
Hall, exact compilation, a safe cut, and the independent interval verifier,
the authoritative completed word remains the five-hole cut above and the
rigorous optimum interval remains `1719<=nu(13)<=1784`.

## 16. July 28: three-hole bridge, forced-star obstruction, and the first symmetry-breaking exclusion

A four-choice trade extracted from the exact `k=11` motif geometry improves the
connected quotient front from four upper-`q=1` hole orbits to three:

```
scratch/k13_q1h3_q2l233_res1_k11motif.certificate.json
scratch/k13_q1h3_q2l233_res1_k11motif.full_audit.json
scratch/k13_q1h3_q2l233_res1_k11motif.middle_cycle.txt
```

The lifted middle cycle has SHA-256
`b299e0fbd9ea3cd56d41c1edcbee984b5437bf70ee2aed04743db9676aad0783`.
It is connected with voltage four and has upper-`q=1` hole representatives
`503,893,1851`, exact upper `q=2`, the single lower-`q=2` hole `233`, and one
quotient residence defect at position 25/lower 669.  All depths at least four
are exact.  This is a nonmonotone search seed, not an exact word.

Imposing both `q=2` sides exactly and retaining the three-hole budget immediately
produces a shadow-perfect disconnected quotient model with component sizes
`81+51`:

```
scratch/k13_q1h3_repair_q2res_hamming17_fulllazy.round0.disconnected.json
```

Thus coverage has crossed the three-hole threshold; connectivity and residence
are the remaining gates in that model.

The all-lower compiler obstruction is now structural rather than branch-specific.
For a missing lower-`q=2` rank-five root `R`, every candidate compiler cell for
`R` is already among the unique forced depth-two cells of the rank-six targets
containing `R`.  Hence `R` together with those supersets gives one more Hall
target than available cells; a linear seam can rescue at most one physical
member.  The audited quotient stars are:

```
A: 233 with supersets 235,745                 deficiency 12,
B: 339 with supersets 467,851,1357            deficiency 13,
C: 121 with supersets 123,125,249,377,969     deficiency 12.
```

Consequently a lower-`q=2` hole cannot be compiled around: it must be eliminated.

Finally, physical symmetry breaking has been tested at the first possible
granularity.  On both the five-hole and three-hole lifted cycles, all
`1,469,754` pairs of physical cycle cuts were enumerated.  There are respectively
3,770 and 3,991 Johnson-valid two-opt reconnections, but zero reconnections
preserving the two removed lower intersection colours.  Exact reports:

```
scratch/k13_q1h5_physical_color_2opt.json
scratch/k13_q1h3_physical_color_2opt.json
```

Therefore any non-equivariant physical repair of either seed needs at least a
three-opt trade.  Three-opt enumeration and component-merging SAT are the two
active exact fronts.  None of these results changes the certified interval
`1719<=nu(13)<=1784` yet.

## 17. July 28 late update: connectivity is solved at three holes

The `81+51` shadow-perfect model is not trapped in two components.  Exhaustive
enumeration of 484 directed three-edge endpoint cycles found 325 touching both
components, 131 that merge them into one cycle, and five that simultaneously
retain three upper-`q=1` holes and exact lower/upper `q=2`.  The best explicit
merge is

```
lower 599: {5,7}   -> {7,10},
lower 921: {10,11} -> {10,12},
lower 615: {3,10}  -> {3,4}.
```

The resulting primary seed and exhaustive report are

```
scratch/k13_q1h3_exactq2_connected_l3merge.certificate.json
scratch/k13_q1h3_disconnected_merge_l3.json
```

Its lifted middle cycle has SHA-256
`5b5a25f95df7a8dc7369ac69aba31cefedbc1b7ff7307b9fd0aa1c1e7024c9da`.
It is one quotient cycle of voltage one, has upper-`q=1` hole representatives
`255,893,1851`, both `q=2` sides exact, and only lower-`q=3` hole representative
`195`.  Its remaining structural debt is seven quotient residence violations,
all at distance three (91 physical short runs).

This closes connectivity as the three-hole gate.  The active finite target is
now sharper:

```
repair seven residence windows,
retain upper q1 holes <= 3,
retain both q2 sides exact,
retain the compiler-benign lower-q3 orbit 195, then compile and cut.
```

The lower-`q=3` orbit `195` has now been audited against the maximal-erosion
compiler.  Every one of its 13 rotations has eleven feasible depth-one cells,
with no seam dependence (143 candidates total).  This is more buffered than
the already compiler-benign orbit `225`; it is not a `393`-type Hall
obstruction.  No additional lower-`q=3` constraint is needed during residence
descent.

Automaton SAT, native alternating-cycle repair, and compatible pairs of physical
three-opt trades are running from this exact-shadow connected seed.  The
certified numerical interval remains `1719<=nu(13)<=1784` until those remaining
steps pass the two independent full-word verifiers.

## 18. July 28: all shadows exact with four residence defects

Native endpoint-cycle descent first reached a connected zero-immediate-hole
cycle with both `q=2` sides exact and four quotient residence defects.  A final
three-edge move then restored its remaining lower/upper `q=3` orbits without
losing any other depth.  The dominant certificate is

```
scratch/k13_allshadows_exact_res4_upperfill_l3.certificate.json
scratch/k13_allshadows_exact_res4_upperfill_l3.full_audit.json
scratch/k13_allshadows_exact_res4_upperfill_l3.middle_cycle.txt
```

The lifted middle-cycle SHA-256 is
`c53acfeaf8c983ebe1c9a7b7bd25a949a6c9ed39d37e51ef26f8675054271595`.
Its exact invariant vector is

```
quotient components:       1,
quotient voltage:          10,
lower/upper shadow holes:  0 for every q=1,...,6,
quotient residence debt:   4, at residues 0,2,17,59,
physical residence debt:   52.
```

This is the first single carrier that solves the entire simultaneous shadow
problem at `k=13`; neither connectivity nor any rank of coverage remains open.
The sole unresolved carrier condition is depth-three residence/factorability.

The four-defect state arose by intersecting two independently useful fronts:
an all-shadows-exact/residence-seven cycle and a zero-immediate-hole,
exact-`q=2`/residence-four cycle.  Their compatibility shows that the earlier
coverage-versus-residence tradeoff is not rigid.  Hard-shadow automaton SAT,
paired quotient cycles, and physical three-opt symmetry breaking are now all
targeted at

```
all shadows exact + residence debt 4  --->  all shadows exact + residence 0.
```

Only after residence zero is obtained can the maximal preimage, Hall compiler,
safe cut, and two full OR verifiers certify `nu(13)=1719`.  Until then the
rigorous numerical interval remains `1719<=nu(13)<=1784`.

## 19. July 28: factorability solved and certified upper bound 1732

The temporary-debt beam from the all-shadow-exact/residence-one state reached a
connected, fully residence-safe carrier whose sole missing shadow is the one
upper-`q=1` orbit represented by `1499`:

```
scratch/k13_res0_onehole_round6.certificate.json
scratch/k13_res0_onehole_round6.full_audit.json
scratch/k13_res0_onehole_round6.middle_cycle.txt
```

It has voltage five, residence zero, exact lower `q=1`, and exact lower/upper
shadows for every `q=2,...,6`.  Its lifted middle-cycle SHA-256 is
`09d3ebfcf7be87a73ad114bae18426047a145c08eff70c1a42908898377d88ff`.

The exact all-lower Hall audit passes with matching `4095/4095` and deficiency
zero.  The unrestricted depth-three compiler is SAT, has no residence failure
and no lower target without a candidate, and yields a length-1719 word missing
exactly the 13 rank-eight masks in the final upper orbit:

```
scratch/k13_res0_onehole_round6.alllower_hall.json
scratch/k13_res0_onehole_round6.linear.word
scratch/k13_res0_onehole_round6.linear.compiler.out
```

Appending those 13 masks gives the independently verified universal word

```
scratch/k13_upper1732.word
sha256 ef4ee6ef96c48f847b57a0dfb4fd5293ca8030537db3ea992b538b6f3a16c7d4
```

Both full OR verifiers report `8191/8191`, so the certified interval is now

```
1719 <= nu(13) <= 1732.
```

The exact frontier is genuinely one unit wide in two complementary coordinates:
all shadows exact plus one quotient residence defect, versus residence exact
plus one missing upper-shadow orbit.  Compensation-beam, anchored-cycle, and
local SAT searches are continuing toward their intersection.  Equality is not
claimed until a length-1719 word passes both full verifiers.

## 20. July 28: exact optimum by a two-cut, one-seam Hamilton path

The last obstruction was an artifact of insisting that the middle carrier be
one Hamilton cycle.  The compiler only needs a Hamilton **path**.

The local history-repair SAT instance

```
scratch/k13_res0_onehole_repair_history16x5.round0.disconnected.json
```

produced an exact, depth-three-resident, all-shadow-perfect middle 2-factor
with two physical cycles of lengths `1547` and `169`.  Its complete independent
audit is

```
scratch/k13_res0_onehole_repair_history16x5.round0.disconnected.full_audit.json
```

An exact two-cut/one-seam census then did the following:

1. cut one edge in each physical cycle;
2. orient both resulting paths;
3. join them by one cross-component Johnson edge;
4. retain every upper shadow and the exact linear residence equation
   `D^3 P=T`;
5. pass the remaining lower targets to the flexible compiler.

The exhaustive census checked `6240` cross Johnson pairs and four orientation
choices, hence `24960` candidates.  Of these, `6032` retained every upper
shadow, and `1092` additionally retained exact depth-three residence.  The
best candidate lost only one native lower-q1 target.  Its full all-lower Hall
graph nevertheless has matching `4095/4095` and deficiency zero.

The selected seam is

```
2515 -> 2391
component 0: endpoint 3,  direction -1
component 1: endpoint 53, direction +1
```

Primary carrier artifacts:

```
scratch/k13_two_cycle_one_seam_paths.json
scratch/k13_two_cycle_one_seam_path_000.json
scratch/k13_two_cycle_one_seam_path_000.hall.json
```

The global linear depth-three compiler is SAT and emits

```
scratch/k13_two_cycle_one_seam_path_000.word.txt
```

with exact audit

```
length:                   1719
nonempty OR masks:        8191 / 8191
missing masks:            0
D^3 row length:           1716
distinct D^3 values:      1716 = binom(13,7)
D^3 rank histogram:       {7:1716}
row distinct counts:      [990,1491,1717,1716]
```

The independent verifier is

```
scratch/verify_k13_exact_1719.py
```

and the word SHA-256 is

```
8d202e793d3317d2c3db76fef51f9d20d0e4e09fa2899a9686285cc01f4577d0
```

The endpoint-blocker lower bound already gives `nu(13)>=B(13)=1719`.
Therefore the interval closes:

```
nu(13) = 1719,
N(13)  = 1720.
```

Full proof/certificate note:

```
MATH_K13_EXACT_1719_CERTIFICATE_20260728.md
```

The reusable structural conclusion is that a small exact 2-factor is enough:
componentwise exact carriers may be cut and joined into one Hamilton path.
The `W+1` cells in row `d-1` provide precisely the boundary freedom needed to
absorb the one lost lower-q1 colour.  This removes connectivity from the hard
SAT core and should be tested first in every remaining depth-three case.
