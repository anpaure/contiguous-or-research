# The minimal `k=76` mark regrouping and a uniform seven-cycle actuator

Date: 2026-08-01

Status: the seven-cycle theorem is unconditional for every `r>=12` at
`d=5`.  The `k=76` minimality and uniqueness statements are exact finite
theorems over all two-row, one-mark transpositions of the systematic profile
multiset.  This repairs the age-composition/Strassen obstruction, not the
one-copy physical construction.

## 1. The obstruction being repaired

At `k=76,r=38,d=5`, the systematic profile

```text
P={2,3,4,6,37}
```

occurs 76 times and forces age type

```text
(1,31,2,1,1,2).
```

No age type reachable from this type contains any systematic profile.  Thus
no choice of *unmarked* suffix completions can repair the Strassen cut.  The
marked grouping itself must change.

## 2. The unique minimal regrouping

Use 76 occurrences of the donor profile

```text
H={1,2,3,5,7}.
```

For each paired occurrence, exchange marked deficits 6 and 5:

```text
P={2,3,4,6,37}   -> P'={2,3,4,5,37},
H={1,2,3,5,7}    -> H'={1,2,3,6,7}.             (2.1)
```

Across the two rows, every marked-deficit multiplicity is unchanged.  The
new forced age types are

```text
X=(1,32,1,1,1,2),
Y=(31,1,3,1,1,1).                               (2.2)
```

The exact modified law supports a stationary Strassen circulation.

### Minimality

A nontrivial count-neutral regrouping cannot change only one row: if one
marked incidence is removed, the same rank mark must be installed on a
different row.  Hence at least two rows and two relocated marks are necessary
per repaired occurrence.  Construction (2.1) attains both lower bounds.

Equivalently, per occurrence it changes two rows, removes two old row-mark
incidences, and adds two new ones.

### Exact uniqueness in the canonical completion face

The complete census considered every two-row, one-mark transposition between
`P` and a systematic donor profile with at least 76 occurrences.  The only
four-mark systematic profile is a subset of `P` and has no mark available for
a genuine transposition, so the five-mark donor census is complete.

The scan completes every unchanged underfull row with its canonical
leading-zero type.  In that fixed completion face there are 97 eligible
transpositions, and exactly one yields a stationary type law:

```text
donor H={1,2,3,5,7}, swap 6<->5.                 (2.3)
```

Thus (2.1) is unique in the canonical leading-zero completion face, up to
the choice of the 76 donor occurrences.  Arbitrary completion or splitting
of unchanged underfull rows was not quantified by this scan.

## 3. A parametric seven-cycle

The successful circulation is not peculiar to `r=38`.

### Theorem 3.1 (double-hole regrouping actuator)

Let `d=5` and `r>=12`.  Consider the two marked profiles

```text
P_r={2,3,4,6,r-1},
H={1,2,3,5,7}.
```

Apply the mark exchange `6<->5`, producing

```text
P'_r={2,3,4,5,r-1},
H'={1,2,3,6,7}.
```

Their forced types are

```text
X=(1,r-6,1,1,1,2),
Y=(r-7,1,3,1,1,1).
```

Define five reservoir types

```text
Z_1=(r-7,3,1,1,1,1),
Z_2=(r-6,2,1,1,1,1),
Z_3=(r-8,3,2,1,1,1),
Z_4=(r-9,4,1,2,1,1),
Z_5=(r-6,2,1,1,2,0).
```

Then

```text
X -> Y -> Z_1 -> Z_2 -> Z_3 -> Z_4 -> Z_5 -> X   (3.1)
```

is a legal age-type cycle.

Consequently, if a post-regrouping type law is

```text
pi = sigma + a(e_X+e_Y+e_(Z_1)+...+e_(Z_5)),      (3.2)
```

where `sigma` is stationary, then `pi` is stationary for every `a>=0`.
The regrouping changes no marked-rank marginal.

### Proof

The mark-neutrality is immediate: (2.1) merely exchanges the locations of
one 5-mark and one 6-mark.

For the cycle, check `Q(target)<=P(source)` on each edge.  The only
potentially nonunit inequalities are

```text
Y_2=3 <= X_1=r-6,
(Z_1)_1=3 <= Y_0=r-7,
(Z_3)_1=3 <= (Z_2)_0=r-6,
(Z_4)_1=4 <= (Z_3)_0=r-8,
X_1=r-6 = (Z_5)_0.
```

They hold for `r>=12`; every other inequality is `0,1`, or `2` against the
same or a larger entry.  All seven vectors sum to `r` and have positive
fresh class.  Hence (3.1) is legal.  Uniform mass on a directed cycle is
stationary, proving (3.2).  QED.

## 4. The reservoir is literal at `k=76`

The five reservoir types correspond to the systematic profiles

```text
Z_1 : {1,2,3,4,7},
Z_2 : {1,2,3,4,6},
Z_3 : {1,2,3,5,8},
Z_4 : {1,2,4,5,9},
Z_5 : {2,3,4,6} with one leading zero deficit.
```

Every one occurs with far more than 76 copies.  After applying (2.1), remove
76 copies of each of the seven cycle types.  The remaining type law has mass

```text
6,892,620,648,693,261,354,068
```

and an exact integral stationary coupling.  Thus the full modified law is
literally

```text
stationary residual + 76 copies of the seven-cycle.
```

This is stronger than merely rerunning max flow after the edit.

## 5. What “local” means

The regrouping is optimal in profile support: two rows and one exchanged mark
on each.  It is also local in the profile-exchange graph.

It is **not** local in the original numerical residue order.  The bad rows
occupy

```text
[6762138943837485613791,6762138943837485613867),
```

whereas occurrences of the donor profile span

```text
[2250339343120898743070,3564299976360417907900).
```

The reported gap is

```text
3,197,838,967,477,067,705,891.
```

This does not invalidate the quotient repair: residue labels are not yet the
physical owner chronology, and the Strassen coupling is free to reorder
rows.  It does rule out treating the repair as a bounded contiguous edit of
the canonical residue order.

## 6. Uniformity verdict

The answer is split.

*For this first double-hole obstruction*, a bounded local regrouping theorem
does hold uniformly: the same two-row mark exchange and the same seven-cycle
work for every ambient rank `r>=12` at depth five.

*For all depths and all terminal profiles*, no bounded library theorem is
proved.  The single-hole family from the preceding theorem and the present
double-hole family are two exact actuator schemas.  As `d` grows, the number
and positions of missing small deficits can grow, and the required reservoir
stock need not be present in an independently chosen marked-profile law.
The `k=76` obstruction already proves that completion-only libraries are
insufficient.

The next honest general target is therefore:

> choose the marked-profile grouping and the actuator reservoir jointly, so
> every forced terminal block belongs to a stocked bounded cycle family.

Subsequent work proves that the same `d+1<->d` mark exchange has a uniform
all-depth cycle for the entire double-hole family, and recurs uniquely at
`k=89`.  See
`MATH_THEOREM_DOUBLE_HOLE_MARK_REGROUPING_ACTUATOR_20260801.md`.  Profiles
with three or more small holes and joint reservoir stocking remain open.

## 7. Interface with a protected Catalan/pivot host

The seven-cycle has the correct *marginal* interface: it preserves every
marked rank count exactly.  A physical coupling still requires four joint
conditions.

1. **Occurrence reservation.**  Reserve owner occurrences realizing the two
   regrouped rows and all five reservoir types before the one-copy selector.
2. **Protected-bank separation.**  None may consume the pivot collar's named
   owner, upper-witness, or common-cap tickets.
3. **Labelled cycle lift.**  Use the biregular partition lift on every edge of
   (3.1), with the actual owner/target labels retained rather than only type
   counts.
4. **Rooted component joining.**  Merge the lifted seven-cycles into the
   Catalan chronology by payload-transparent component switches while
   retaining residence and the pivot endpoints.

There are 76 physical copies at `k=76`, so the protected actuator bank is
`Theta(k)`, not `O(d)`.  The earlier fixed-`O(d)` common-basis avoidance
corollary cannot simply avoid it after the fact.  The actuator rows and the
common Catalan basis must be selected jointly, or compressed as one symmetry
orbit before literal lifting.

This precisely locates the remaining correlation: the age/mark arithmetic is
now exact, while one-copy physical owner selection and protected topology are
still open.

## 8. Scope and artifacts

Proved:

* the unique minimum two-row regrouping at `k=76` within the canonical
  leading-zero completion face;
* the all-`r` seven-cycle identity for the same double-hole pattern;
* exact residual stationarity after removing 76 cycle copies.

Not proved:

* a bounded actuator library for arbitrary `d`;
* a contiguous-residue regrouping;
* a labelled one-copy lift into the protected Catalan/pivot host;
* any new bound on `nu(k)`.

```text
scratch/search_systematic_k76_two_row_mark_swap_20260801.cpp
a0f8f6c230e25bb49d2cd79a6e76294789e3a19d1190e3bbf6ad2a43fc714a77

scratch/systematic_k76_two_row_mark_swap_20260801.out
d9f5b218bf0ffdae02bdde15da3ca5c8da57b7ce31f02772b4c44f875bc1a574

scratch/systematic_k76_two_row_mark_swap_20260801.audit.json
13abd90fa4808c267743a7cfe7f28d0aefb25470b8b34cae0dd28332fb2b0d7d
```
