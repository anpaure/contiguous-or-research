# K16 annealing audit: why the C105 seed stalled, and the C106 normal form

Date: 2026-07-30

## Scope

This note concerns only the frozen K16 length-eight source and its 211,604
direction-coherent seam catalogue.  It is not a lower bound for another K16
carrier or for a non-separated transformation.  The cycle statements below
are exact audits of named search incumbents, not existence or nonexistence
claims.  The authenticated source-relative lower bound `C>=106` is proved
separately by the five-lock automaton.

## 1. Exact decomposition of the eleven-missing C105 incumbent

The frozen incumbent

```text
scratch/k16_c105_anneal_seed_m11_20260730.json
SHA-256 524d28548088ddd31bed5007d395c1d6ffacf2165dbe17651cd2ba04abe46b07
```

is an exact endpoint-balanced, port-capacity-one selection of 105 seams.  Its
active directed graph is the disjoint union of nine cycles of lengths

```text
2,2,2,2,2,15,15,20,45.
```

Its eleven missing targets all have direct-dual weight four, so its missing
weight is 44.  It repeats all fifteen weight-one targets and sixteen
weight-two targets once, for repeat weight 47; its total seam slack is zero.
This is exactly the identity

```text
repeat_weight - missing_weight + slack = 47 - 44 + 0 = 3
                                                 = 2*105 - 207.
```

The length-45 cycle has no *globally unique occurrence*: its 60 service
occurrences consist of two occurrences of each of 30 targets.  This does not
make the cycle simply removable.  Collectively it is the sole twofold
provider of those 30 targets; deleting it loses all 30 at once.  The
length-20 cycle supplies sixteen globally unique targets but also contains
the weight-two repeat that traps the result in the now-excluded C105
slack-one/repeat-two face if the other 60 seams are frozen.

The two length-15 cycles jointly supply 30 distinct weight-two targets exactly
once.  Freezing only these 30 clean seams leaves a 75-seam residual problem:

- cover the other 63 targets;
- avoid all 30 frozen targets, since repeating weight two is impossible on
  the surviving equality faces;
- at C105, either exact service with slack three, or one repeated weight-one
  target with slack two.

The authenticated five-lock theorem now proves both residual alternatives,
and in fact every C105 equality branch, impossible even after omitting port
capacity.  Consequently the observed eleven-missing plateau was not merely a
weak neighborhood: there is no C105 service solution anywhere in this frozen
catalogue.

The solver-free cycle audit is

```text
scratch/k16_c105_anneal_seed_m11_cycles_20260730.audit.json
SHA-256 84aca46eeb37147f04ddc3cbcedb79241cfb87c927ce70920ab270c2489b69a5
```

## 2. Exact C106 equality arithmetic

At `C=106`, complete service gives

```text
Q + R = 2*106 - 207 = 5,
```

where `Q` is total repeated target weight and `R` is total seam slack.  Let
the five authenticated lock triples be

```text
{35044,36935,40066}, {37320,41102,47364},
{33906,36417,51235}, {33337,50976,58385},
{41872,49436,61960}.
```

All fifteen members have target weight one.  For total slack `R<=3`, the
authenticated closed-walk automaton says that the attainable five-bit lock
syndromes are exactly the masks of parity `R mod 2` and Hamming weight at most
`R`.  Comparing this with the odd baseline syndrome `11111` gives:

- `R=3,Q=2`: repeat one weight-one target from each of two distinct triples;
- `R=2,Q=3`: repeat one weight-one target from each of three distinct triples;
- `R=1,Q=4`: repeat one weight-one target from each of four distinct triples;
- `R=0,Q=5`: repeat one weight-one target from every triple.

Weight-two or weight-four repeats do not toggle a lock bit and are therefore
impossible in these faces.  Repeating twice in one lock group also fails to
provide the required distinct toggles.  The two remaining arithmetic faces
are forced without the automaton:

- `R=5,Q=0`: exact service;
- `R=4,Q=1`: one repeated weight-one target.

Thus every C106 equality ledger lies in a compact `4^5=1024` atlas: for each
lock group choose either its one unit of slack or one of its three targets to
repeat.  This is the correct branch space for C106 fractional seeds, integer
search, and structured annealing.

## 3. Search consequence

The C105 annealer should not be tuned further.  The constructive next step is
to obtain a capacity-one fractional C106 basis in one of the 1,024 normal-form
faces, exactify it in cycle coordinates, and round/rethread only inside that
face.  In particular, objective functions should charge direct-dual weighted
deficiency rather than the number of holes: the C105 incumbent's eleven holes
were all weight four, while its repeat mass lived entirely at weights one and
two.

For this fractional seed step, all nonnegative-row-slack seams must be kept.
Filtering to `row_slack <= R` is WLOG for a binary seam selection but is not
WLOG for continuous seam mass: a higher-slack seam can carry a fraction at
most `R/row_slack`.  The correction and the exact seam-slack census are in
`MATH_CORRECTION_K16_C106_CONTINUOUS_ROW_SLACK_TRUNCATION_20260730.md`.
