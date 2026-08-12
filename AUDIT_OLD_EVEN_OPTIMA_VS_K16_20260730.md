# Audit: how the exact even cases were actually obtained, and why `k=16` is different

Date: 2026-07-30

This note reconstructs the provenance of the exact `k=10`, `k=12`, and
`k=14` words from the retained search logs, source programs, certificates,
and literal replays.  The main conclusion is simple:

> The older even optima were not outputs of one automatic odd-to-even lift.
> `k=10` was found directly; `k=12` began from a lift but required substantial
> carrier repair; and `k=14` used a specially ported six-piece braid whose
> success depends on the favorable depth drop `3 -> 2`.  At `15 -> 16` that
> depth drop disappears.

All three retained answer files were replayed independently in this audit:

| case | length | covered | SHA-256 |
|---|---:|---:|---|
| `answers/k10.word` | 254 | 1023/1023 | `24b6fc4f4c054e46ef54553ca37eded126150542d51a61256a837d666e0c74fd` |
| `answers/k12.word` | 926 | 4095/4095 | `6d598c62f5925d1d2dfce8279eea82069318bd93ff66d0b204c639cf06297851` |
| `answers/k14.word` | 3434 | 16383/16383 | `7d94117099bbb46402e8f4edda718dae7eb10e2e5e34e9b588e08a198b43db17` |

## 1. The arithmetic regimes

For the flat carrier ansatz, put

\[
 r=\lceil k/2\rceil,\quad W=\binom{k}{r},\quad
 \Lambda=\sum_{s=1}^{r-1}\binom{k}{s},
\]

and let `d` be the minimum depth with

\[
 dW+\binom{d+1}{2}\geq\Lambda.
\]

The relevant values are:

| `k` | `W` | `d` | `B(k)=W+d` | scalar lower-capacity slack |
|---:|---:|---:|---:|---:|
| 10 | 252 | 2 | 254 | 122 |
| 12 | 924 | 2 | 926 | 266 |
| 14 | 3432 | 2 | 3434 | 392 |
| 16 | 12870 | 3 | 12873 | 12284 |

Here the last column is
`dW+binom(d+1,2)-Lambda`.  In particular, the sometimes quoted value 210
for the `k=14` scalar slack is not this quantity; the exact monotone-deadline
slack is 392.

The decisive depth sequence is

```text
d(9)=2, d(10)=2;
d(11)=3, d(12)=2;
d(13)=3, d(14)=2;
d(15)=3, d(16)=3.
```

Adjacent-intersection lifting shortens each internal coordinate run by one.
Thus the `11 -> 12` and `13 -> 14` lifts receive one free unit of residence;
the `9 -> 10` and `15 -> 16` lifts do not.

## 2. `k=10`: direct search, not a successful lift

The obvious `k=9 -> 10` construction was tried.  It interleaves the `k=9`
lower-shadow row and its lifted copy and does give a 252-vertex Hamilton path
through all five-sets.  The retained handoff explicitly records that this
path is **not factorable** at depth two or three: the new coordinate
alternates, creating internal runs of length one.

The exact `k=10` carrier was instead found in the unrestricted factorable
component by `central_path_plateau.cpp`.  The search operation was a reversal
of a contiguous path segment whose two new boundary edges remained Johnson
edges; every candidate with nonzero run deficit was rejected.  Starting from
a carrier covering 966 of the 968 required two-sided shadow colors, the
retained logs show

```text
966/968 -> 967/968 -> 968/968
```

within seven such factor-preserving moves.  The final middle row has:

* all 252 rank-five sets exactly once;
* all 210 rank-four and all 120 rank-three consecutive intersections;
* all upper ranks six through ten through consecutive unions.

Only after the carrier was complete was the lower word solved exactly.  The
retained CNF has 192,665 witness selectors, 195,205 variables, and 2,552,701
clauses.  SAT produced the 254-letter word.

Therefore the reusable part of `k=10` is the carrier/compiler separation and
the factor-preserving segment-reversal move.  Its actual chronology is a
search-specific certificate.  It is not evidence that an odd optimum lifts
automatically to the next even optimum.

## 3. `k=12`: a lift supplied a near seed, not the answer

### 3.1 Original construction history

The original `k=12` search used the lower-preserving intersection lift from a
then-available `k=11` carrier.  This is the favorable depth-drop case
`3 -> 2`, so the intersection sector inherits adequate residence almost
automatically.  Nevertheless the initial lifted path still had:

* 28 missing upper masks; and
* one unit of run deficit at the concatenation boundary.

A three-move beam repair removed the run deficit.  Neutral moves improved the
upper palette.  The lower compiler then exposed constraints that shadow
scores alone had hidden:

1. the singleton-position matching was only `11/12`;
2. after fixing that, an eight-target Hall family had only seven clean cells;
3. after fixing that, the exact factor-label SAT was positive;
4. the resulting word still had upper holes, eventually reduced to one
   rank-seven mask and then repaired by a label-preserving path move.

The final carrier has 924 middle owners, exact depth-two residence, and all
lower and upper shadows.  The final exact factor model retained 1,466,918
selectors and 1,478,030 variables.

So the historical `k=12` result was a lift **plus dimension-specific beam
search, targeted Hall repair, and exact SAT**.  The lift was valuable because
it placed the search close to the right component, not because it proved the
case.

### 3.2 Post-hoc six-piece reconstruction

After the `k=14` braid was understood, a distinct `k=12` optimum was rebuilt
from the exact `k=11` source with the same six-piece motif.  Its exact data are

```text
A cuts: 66, 459
B ear: length 3 beginning at 409
piece order: A1R B1F A2R B2R A3F B3R
```

The resulting carrier compiles in 0.0306 seconds using 42,753 selectors and
46,463 variables.  Its word
`scratch/k12_intersection_sixpiece_hallpass_001.word` has SHA-256
`a29517e67dd3c9db5f773f5332b3e3e44197cfe79d3d8014ea0770c9bedeb482`
and independently covers all 4095 nonempty masks.

This later certificate confirms the braid mechanism, but also shows its
scope: the raw braided middle path still has two lower-q1 holes and one
lower-q2 hole.  The unrestricted lower compiler absorbs them.  The success is
not a pointwise shadow identity at every lower depth.

## 4. `k=14`: a finite port identity in a six-piece braid

This is the one older even optimum genuinely produced by the now-familiar
odd-to-even braid.

The exact `k=13` carrier family supplies two 1716-vertex sectors:

* `A`, all rank-seven sets avoiding the new coordinate; and
* `B`, the new coordinate joined to an adjacent-intersection row of a
  (possibly different) `k=13` source.

A contiguous `A||B` chronology has the middle partition and can have perfect
upper shadows and depth-two residence, but it cannot realize the singleton
of the new coordinate.  The forced-core theorem says that the new coordinate
needs an internal middle run of exactly `d+1=3`, or a suitable boundary flag.

Extracting a three-vertex `B` ear creates the needed run, but deletes two
first-upper colors.  A five-piece braid has only one independently usable `A`
port and cannot restore both unique colors.  The exact winning move uses two
`A` cuts:

```text
A cuts: after 418 and 1445
B ear: three vertices beginning at 966
piece order: A1F B2R A3F B1F A2R B3F
```

The two lost `B` colors determine the two `A` cut locations up to side
choices: each lost color is itself an `A` vertex, and a seam from that vertex
to a containing `B` endpoint restores the corresponding upper color.  This
is why the successful search was finite and sharply targeted rather than a
generic anneal.

Quantitatively:

* 100 calibrated strict source carriers were retained;
* 35 admit a valid six-piece braid;
* for the exact source, the parameterized search checked only 159
  endpoint-valid templates, 29 residence-valid templates, and one
  upper/Hall-perfect template;
* the braid search took about 0.06 seconds;
* the final lower compiler took 0.79 seconds, with 323,113 selectors and
  340,289 variables.

This separates the reusable theorem from the certificate-specific data.
The reusable theorem is: a length-`d+1` `B` ear plus two lost-color-addressed
`A` cuts reduces the seam search to `O(W)` times a fixed template catalogue.
The numbers `418,1445,966`, orientations, and source permutation are finite
certificate data.

## 5. Why `k=16` does not inherit the easy part

There are three distinct notions of “lift” that were being conflated.

### 5.1 The unconditional trimmed lift is easy but nonoptimal

Any word of length `n` lifts to the next dimension at length `2n`.  From the
exact `k=15` word this gives 12,876 letters.  It proves an upper bound, not
the target 12,873.  Subsequent collar work has improved the verified bound to
12,874, leaving

\[
12873\leq\nu(16)\leq12874.
\]

Thus even now the generic lift works; what is hard is saving its final three
letters, and especially the last one.

### 5.2 The six-piece intersection lift loses one unit of residence

At `11 -> 12` and `13 -> 14`, the target depth is one below the odd source
depth.  At `15 -> 16`, both depths are three.  The `B` sector is an
adjacent-intersection row, so it loses one from every internal run.  A clean
source condition is therefore depth-four residence in the `B` source (runs
of at least five), not merely the depth-three residence already needed for
the `k=15` optimum.

The retained exact audit of the present `k=15` sources found 1020 depth-four
residence violations on eight physical cycles; even a greedy cut cover needs
533 cuts.  A six-piece braid alters only bounded collars around five seams.
It cannot repair hundreds of defects inside the pieces.  This is the precise
reason the old braid does not scale directly.

The finite calibration confirms the law:

| lift | depth change | six-piece outcome |
|---|---|---|
| `7 -> 8` | `2 -> 2` | zero resident braids |
| `9 -> 10` | `2 -> 2` | zero resident braids |
| `11 -> 12` | `3 -> 2` | exact optimum |
| `13 -> 14` | `3 -> 2` | exact optimum |
| `15 -> 16` | `3 -> 3` | source-residence gate open |

So `k=10` itself is already a counterexample to the memory that “the same
lift always solved evens”: its unchanged-depth lift failed, and direct search
was needed.

### 5.3 The current one-letter gap is local but globally coupled

The verified 12,874 word is not a flat exact-middle carrier of the old type.
Deleting one letter gives a 12,873-letter partial word; the current search has
reorganized it down to two uncovered masks.  Exact local audits have ruled
out the smallest provider paths and show that the remaining improvement must
leave the known two-state portal basin or make a larger temporary excursion.

The large scalar slack 12,284 at `k=16` therefore does not make the final
step automatic.  The obstruction is pointwise compatibility of witnesses
under one chronology, not total lower-cell capacity.  This is directly
analogous to the old `k=14` fact that aggregate slack existed but two specific
unique upper colors still required two specifically addressed ports—only the
remaining `k=16` circuit is no longer bounded to six pieces.

## 6. Bottom line

The old even record is consistent, not paradoxical:

* `k=10`: direct factorable-carrier search; the natural lift failed.
* `k=12`: favorable-depth lift followed by substantial targeted repair; a
  clean six-piece reconstruction was found only later.
* `k=14`: favorable-depth six-piece braid with an exact two-port upper-color
  identity.
* `k=16`: no depth drop, so the intersection sector needs a stronger odd
  source; the generic trimmed lift reaches `B+3`, collar work reaches `B+1`,
  and the remaining `B` step needs a genuinely larger correlated rethread.

The phrase “odd-to-even lift” described a source of good starting states in
several different regimes.  It was never one theorem saying an optimal odd
word automatically yields an optimal even word.

## 7. Primary evidence

* `MATHEMATICAL_HANDOFF.md`, Sections 10c, 13, 32, and 333.
* `MATH_ODD_EVEN_SIX_PIECE_LIFT_20260728.md`.
* `MATH_K14_EXACT_3434_CERTIFICATE_20260728.md`.
* `K14_INTERSECTION_LIFT_RANK1_OBSTRUCTION_20260728.md`.
* `central_path_plateau.cpp` and `central_path_plateau*.log`.
* `k10_factor_full.cnf.log`, `k12_optimal_factor.log`.
* `scratch/k06_k12_k14_six_piece_shadow_braid_motif_audit.json`.
* `AUDIT_CLAUDE_TWO_RAIL_K10_K16_SKELETONS_20260730.md`.

