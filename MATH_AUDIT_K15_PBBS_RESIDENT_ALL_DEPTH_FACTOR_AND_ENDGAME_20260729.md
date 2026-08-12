# Independent audit of the `k=15` PBBS resident all-depth factor

Date: 2026-07-29

## 0. Verdict

The artifact

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/u2u3l3_s801.engine.json
```

passes independent literal replay.  It is an exact non-loop, residence-four,
all-depth-complete factor on the physical rank-eight layer.  It has nine
physical cycles, so it is not yet one linear carrier and is not a literal OR
word.

The exact remaining obligations are:

1. open and concatenate the nine physical cycles into one Johnson path while
   retaining linear residence and every upper target;
2. solve the exact common lower compiler for that one chronology; and
3. retain and independently verify a nonzero 6,438-letter word.

Neither a seam path alone nor a Hall number alone proves the word.

## 1. Artifact identities

```text
886877094a3eaba8950136728d131782141a4b6f882d570ecb3791827da98f83
    u2u3l3_s801.engine.json

f2ab5b997199e788c1f18d2de2579020751020a35d8ef1394cb0b06a40494bd7
    u2u3l3_s801.audit.json

d086844ce1c48d3f6f7c9e6ff4bdba109763343e532e747b0aec16565f0f055b
    u2u3l3_s801.independent.factor.audit.json

5e7256393313f7695d028e97ac2de1014d3d24cc4cd1f25047512b1a4581084c
    u2u3l3_s801.components.json

4156ee55fdc47f297a5fd260d5af8d7e5ed4d5c01b3daab87082ef6c6f45b76f
    u2u3l3_s801.seam_catalogue.audit.json
```

The stable quotient choice-table digest is

```text
8d09676a3c073c5bb688c6ea61d8561087f560ebcc1fac775b9a97d33b1cf08a.
```

The selected-choice ID digest is

```text
f69024ab9f58a807c4d340e2d87322def1dde851311539fffeebc7ba9411592a,
```

and the expanded physical-cycle digest is

```text
bc033cd5da8c2c1d9876ffc3a1f725dd03f52319324ecf94cb0f92617c69cd30.
```

## 2. Independent replay routes

Three logically separate replays were run.

1. `audit_sigma_factor_candidate_20260729.py` reconstructs the quotient
   voltage graph and its physical lifts directly from the 429 literal
   `[lower,a,b]` choices.  Its fresh output byte-matches
   `u2u3l3_s801.independent.factor.audit.json`.

2. `audit_k15_global_rainbow_factor_candidate_20260729.py` rebuilds the
   repository quotient catalogue, expands every physical component, and
   reruns the graded shadow and residence oracles.  It agrees numerically
   with `u2u3l3_s801.audit.json`.  The current output schema additionally
   records the optional component-export path, so byte identity is not
   claimed for that expanded output.

3. `threadD_seed0_component_seam_endgame_20260729.py audit` independently
   enumerates every literal cyclic `(q+1)`-window on all nine physical
   cycles.  This checks both lower intersections and upper unions at every
   depth, not merely the three witness families imposed in the SAT model.

No solver status is used in the conclusions below.

## 3. Exact physical factor

The 429 quotient choices expand to all

```text
binom(15,8) = 6435
```

physical rank-eight states, each exactly once and with degree two.  Every
physical transition is a Johnson edge.  There are no quotient loops.

The quotient and lift topology is:

| quotient start | quotient length | oriented voltage | sign class | physical lifts | lift length |
|---:|---:|---:|---:|---:|---:|
| 255 | 258 | 5 | `{5,10}` | 5 | 774 |
| 447 | 126 | 4 | `{4,11}` | 1 | 1890 |
| 503 | 37 | 1 | `{1,14}` | 1 | 555 |
| 1907 | 5 | 4 | `{4,11}` | 1 | 75 |
| 3303 | 3 | 11 | `{4,11}` | 1 | 45 |

Thus there are five quotient components and nine physical cycles, with
length multiset

```text
1890, 774^5, 555, 75, 45.
```

The minimum cyclic coordinate-one run is four.  There are zero residence
bad runs and zero residence shortfall at depth three.

## 4. Literal all-depth shadow table

For every `q=1,...,7`, direct physical enumeration of consecutive
`(q+1)`-state windows gives:

| q | lower rank | lower support | upper rank | upper support |
|---:|---:|---:|---:|---:|
| 1 | 7 | 6435/6435 | 9 | 5005/5005 |
| 2 | 6 | 5005/5005 | 10 | 3003/3003 |
| 3 | 5 | 3003/3003 | 11 | 1365/1365 |
| 4 | 4 | 1365/1365 | 12 | 455/455 |
| 5 | 3 | 455/455 | 13 | 105/105 |
| 6 | 2 | 105/105 | 14 | 15/15 |
| 7 | 1 | 15/15 | 15 | 1/1 |

Hence every lower and upper target has a literal minimum-width cyclic
witness.  The unrestricted upper-interval oracle also returns no hole.  The
complete missing-set digest is

```text
61af099366fa42b9dbabc5323f67e28e9a9d04e4013e4e79ce43a7733015bc22.
```

The immediate-shadow collision data are

```text
upper-q1 pair collisions    100
lower-q2 pair collisions     97
collision-floor excess        9.
```

These multiplicities are not needed for the support verdict.

## 5. What cutting can destroy

Cyclic completeness is not inherited automatically by an arbitrary opening.
An old witness may cross the deleted closing edge of its source cycle.  A new
seam may also create a short coordinate run or fail to replace the lost
witness.  Therefore each proposed linear chronology must be replayed after
all cuts, orientations, and seams are fixed.

The solver-free seam catalogue contains

```text
12,870  oriented cut states,
96,150  residence-safe Johnson seam arcs.
```

Every one of the 72 ordered pairs of distinct source components has at least
one seam arc.  This rules out a coarse component-digraph obstruction, but it
does not prove that eight mutually compatible arcs form a valid chronology.

There is an explicit warning example.  The state chain

```text
11812, 12766, 12828, 7314, 4009, 5663, 3349, 11119, 9049
```

uses the component order

```text
6,7,8,3,1,2,0,5,4,
```

cuts

```text
146,68,24,219,114,167,1674,573,312,
```

and orientations

```text
0,0,0,0,1,1,1,1,1.
```

It has eight Johnson seams, eight distinct recycled cut colours, no linear
residence violation, and exact structural identity for the maximal erosion.
Nevertheless literal replay gives

```text
upper holes by depth    (1,3,1,0,0,0,0),
lower holes by depth    (1,3,2,0,0,0,0).
```

Its middle-path digest is

```text
95b359b2022ee63d75cad73e2695369cee93ad667cf6cef1c20e53e1b155238d.
```

Thus topology, residence, and the lower-q1 recycling count do not imply cut
survival.  Upper and lower chronology remain genuine constraints.

## 6. Exact minimal word interface

Let `T=(T_0,...,T_(W-1))`, `W=6435`, be a linear ordering obtained from the
nine physical cycles.  For a word

```text
A=(A_0,...,A_(W+2)),
```

write

```text
(D^3 A)_i = A_i union A_(i+1) union A_(i+2) union A_(i+3).
```

The following is an exact sufficient interface.

### Proposition 6.1

Assume:

1. `T` contains every rank-eight subset of `[15]` exactly once;
2. every rank-nine through rank-fifteen subset is the union of a nonempty
   contiguous interval of `T`;
3. every `A_p` is nonempty and `D^3 A=T`; and
4. every rank-one through rank-seven subset is the union of a nonempty
   contiguous interval of `A`.

Then `A` is a literal contiguous-OR word containing every nonempty subset of
`[15]` and has length

```text
W+3 = 6438.
```

#### Proof

Ranks one through seven occur by hypothesis 4.  Every rank-eight target is
some `T_i`, hence is the four-letter union

```text
A_i union A_(i+1) union A_(i+2) union A_(i+3).
```

If an upper target is

```text
T_i union T_(i+1) union ... union T_j,
```

then it is exactly

```text
A_i union A_(i+1) union ... union A_(j+3).
```

Thus every nonempty target is a literal interval OR of `A`.  The word has
`6435+3=6438` nonempty letters.  QED.

Consequently a verified output satisfying Proposition 6.1, together with the
already proved lower bound `nu(15)>=6438`, proves `nu(15)=6438`.

## 7. Remaining obligations, with scopes separated

### 7.1 Linear topology and chronology

Choose one cut and orientation in each physical cycle and eight Johnson seams
forming one path through all nine components.  Recheck:

1. all 6,435 distinct middle states;
2. every seam is Johnson;
3. zero linear residence violations;
4. the maximal erosion has length 6,438, is pointwise nonempty, and derives
   back to the chosen middle path; and
5. every upper target survives under an unrestricted linear interval audit.

The current direct-opening model adds the useful sufficient normalization
that each seam recycles exactly one endpoint cut lower-q1 colour and no cut
colour is recycled twice.  Nine removed colours and eight seams then leave
exactly one adjacent lower-q1 colour for the compiler.  This normalization is
not itself a logically necessary part of Proposition 6.1.

### 7.2 Exact common lower compiler

For the one fixed chronology, find one common nonzero word `A`, not separate
rankwise rows, satisfying `D^3 A=T` and covering every lower target.  The
compiler must enforce its full Hall and omission constraints simultaneously.
A matching size, marginal balance, or one-hole lower palette alone is not a
word certificate.

### 7.3 Literal final verification

Retain the 6,438 integers and run

```text
python3 scratch/verify_exact_or_word.py WORD --k 15 --require-middle-row
```

The verifier must check nonzero letters, exact middle reconstruction, and all
`2^15-1` nonempty target masks.  Only this final PASS supports the equality
claim.

## 8. Precise proved boundary

Proved now:

* a non-loop exact middle factor exists;
* it is cyclically resident at depth three;
* both lower and upper cyclic shadow towers are complete at every depth;
* its quotient and physical component ledgers are exact; and
* the coarse residence-safe seam graph has no ordered-component obstruction.

Not proved:

* a shadow-safe eight-seam linearization;
* a satisfying exact common lower compiler on any such linearization;
* a retained 6,438-letter word; or
* `nu(15)=6438`.

