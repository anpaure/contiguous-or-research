# K16 facet-colour augmentation: the middle ghost is removable

## 1. Scope and result

Let `P` be the selected first-middle chronology of the authenticated
length-`12873` one-hole word

```text
scratch/k16_upper12874_best_delete.word
```

It has `12870` rank-eight occurrences, contains `0xc279` twice, and omits
`0x2c6d`.  Its genuine Johnson edges cover every rank-nine mask.  This note
proves the following carrier-level statement.

> **Theorem 1 (exact facet augmentation).**  One occurrence of `0xc279` can
> be replaced by `0x2c6d` and eight carrier edges can be switched so that:
>
> 1. the result is one connected linear path through all
>    `binom(16,8)=12870` rank-eight masks exactly once;
> 2. every inserted edge has exactly the rank-nine colour of the edge it
>    replaces; hence the complete rank-nine colour **multiset** is unchanged;
> 3. in particular, all `binom(16,9)=11440` immediate upper colours remain
>    covered.

The theorem is stronger than an argument using surplus colours: it spends
none of them.

This does **not** yet give a physical length-`12873` universal word.  The
development below first finds an area-passing augmentation with sole upper
debt `0xef79`, then removes that debt by two q1-safe reversals.  The resulting
all-upper order is nevertheless closed by the later exact area/rank-seven-
chain Pareto theorem.  Thus the proved positive result is the carrier
augmentation; the current live gate is another order-changing rethread, not
the original middle ghost or a different schedule for the frozen order.

## 2. General alternating-trail criterion

Write `F=binom([k],r)` and `U=binom([k],r+1)`.  A genuine carrier edge
`xy` has colour

```text
col(xy)=x union y in U.
```

Suppose a carrier occurrence `d*` is to be deleted and a missing facet `h`
is to be inserted.  A **colour-preserving augmenting trail** is data

```text
y[0]=h,
(z[1],w[1]),...,(z[t],w[t]),  w[t]=d*,
```

such that, for every `i`,

```text
z[i]--w[i] is a used carrier edge,
y[i-1]--z[i] is unused,
y[i-1] union z[i] = z[i] union w[i] has rank r+1,
y[i]=w[i].
```

Delete every `z[i]--w[i]` and insert `y[i-1]--z[i]`.  The colour multiset is
unchanged term by term.  The start `h` gains one degree, the terminal `d*`
loses one, and every intermediate occurrence has one edge deleted and one
inserted.

Therefore two internally disjoint such trails, ending through the two
different incident edges of the same `d*`, give

```text
deg(h)=2, deg(d*)=0,
```

and leave every other degree unchanged.  If their symmetric difference is
connected after the isolated `d*` is discarded, it is a linear path on the
desired facet deck.  This connectivity test is the only global condition;
colour preservation is local and exact.

## 3. The two K16 augmenting trails

Use the second `0xc279` occurrence, occurrence index `12825`.  The following
table writes each step as

```text
loose + pivot  /  delete(pivot--landing)  [colour].
```

### Trail A

```text
2c6d + 6c6c / delete(6c6c--686d) [6c6d]
686d + 6a6c / delete(6a6c--6a69) [6a6d]
6a69 + 6a71 / delete(6a71--4a79) [6a79]
4a79 + ca71 / delete(ca71--c279) [ca79]
```

In occurrence indices, the four `(loose,pivot,landing,deleted-left-edge)`
rows are

```text
(H,3289,3288,3288)
(3288,3095,3096,3095)
(3096,6386,6387,6386)
(6387,12824,12825,12824).
```

### Trail B

```text
2c6d + 2e69 / delete(2e69--266d) [2e6d]
266d + 263d / delete(263d--2679) [267d]
2679 + 6639 / delete(6639--4679) [6679]
4679 + c639 / delete(c639--c279) [c679]
```

In occurrence indices:

```text
(H,4486,4487,4486)
(4487,3598,3597,3597)
(3597,6389,6388,6388)
(6388,12826,12825,12825).
```

The hexadecimal display is redundant: the audit recomputes every union
from the frozen occurrence labels.  The two trails are internally disjoint,
delete distinct edges, and insert distinct unused edges.  After switching,
the only degree-zero occurrence is the chosen second `0xc279`; the new
`0x2c6d` occurrence has degree two; all other internal vertices have degree
two; the old two endpoints retain degree one.  Direct traversal visits
exactly `12870` vertices and ends at the old right endpoint.  This proves
Theorem 1.

## 4. The apparent `1429` surplus

There are nominally

```text
12869 - 11440 = 1429
```

more consecutive pairs than rank-nine colours.  In this selected deadline
chronology, however, two pairs are compiler seams whose union ranks are ten
and eleven.  Thus there are `12867` genuine rank-nine edge occurrences and
the literal q1 surplus is

```text
12867 - 11440 = 1427.
```

The augmentation preserves the full q1 multiplicity histogram

```text
1^10113 2^1227 3^100,
```

so this distinction does not affect the construction.

## 5. Strongest unchanged-schedule lift

Assign the augmented targets, in their new path order, to exactly the source
chronology's selected start/deadline intervals.  At a physical position
`p`, the largest legal cell is the intersection of all targets whose
interval contains `p`.  These maximal cores give an exact test: the fixed
schedule is realizable iff their OR over every assigned row equals that
row's target.

An exhaustive census of all `37` connected pairs of shortest
colour-preserving trails has:

```text
minimum empty maximal cores = 0,
minimum failed scheduled rows = 6.
```

The witness in Section 3 attains the minimum.  Its failed rows are

| row | physical interval | target | maximal OR | missing bit |
|---:|---:|---:|---:|---:|
| 3287 | 3287..3290 | `4ae9` | `4ae1` | `0008` |
| 3288 | 3288..3291 | `6a69` | `6a61` | `0008` |
| 3289 | 3289..3292 | `6a71` | `6a61` | `0010` |
| 5189 | 5189..5192 | `263d` | `262d` | `0010` |
| 5190 | 5190..5193 | `263e` | `262e` | `0010` |
| 6077 | 6077..6080 | `2e69` | `2c69` | `0200` |

The affected failure cells are the fifteen positions

```text
3287..3292, 5189..5193, 6077..6080.
```

Consequently no choice of compiler letters inside the unchanged maximal
cores can realize this target order with the old deadlines.  A successful
physical lift must retime at least these local row-bit obligations (or use a
different connected trail pair).  This is much narrower than the original
`c279 -> 2c6d` problem, but it remains a real gate.

One other shortest connected orientation is upper-complete at every rank,
but has twenty-five fixed-schedule row failures.  Thus immediate upper
completeness and unchanged-deadline realizability are currently a Pareto
tradeoff, not the same condition.

### The exact three-hole DP changes the lead

The unchanged source staircase is unnecessarily restrictive.  Running the
complete three-start-hole/three-deadline-hole DP

```text
scratch/audit_three_hole_middle_schedule_dp_20260731.py
```

on all thirty-seven connected shortest trail pairs finds exactly two which
pass the necessary lower-capacity gate `>=26332`.

The stronger upper candidate uses shortest-path indices `(9,9)` and has

```text
maximum selected lower area       29283
unselected-start credit upper bound   9
lower-capacity upper bound         29292
required lower mass                26332
deadline holes                  331,332,5571
start holes                  11838,11839,11840
upper holes                         ef79 only (rank 12).
```

Its frozen target order is

```text
scratch/k16_facet_augmented_area29283_targets_20260731.word
SHA-256 7e47362fbe1535b758f566343b741ed379ae631b24a4b7c0cc73d83f3b477a71.
```

The other passing pair `(9,10)` has capacity upper bound `29458` and upper
holes `{ec79,ef79}`.  Passing this scalar capacity gate is not a lower Hall
certificate; it says only that the target order is no longer ruled out by
the exact schedule/capacity theorem.

The sole `ef79` debt has a particularly sharp anatomy.  Its old complete
facet run has split into

```text
positions 2695..2698:   8a79,ca71,ea61,eb60   (missing bit 0400)
positions 12824..12828: e469,c479,c639,e619,e718 (missing bit 0800).
```

Joining or bridging these two runs realizes `ef79`.  Their four exterior
q1 boundary colours are all unique, so a naive block 2-opt destroys q1.
The next exact target is therefore a second colour-preserving alternating
bridge which joins these two facet runs while retaining lower capacity.

### Two exact reversals close the whole upper tower

For the frozen `(9,9)` target order, the following two ordinary 2-opt
reversals preserve the complete q1 palette while transporting, and then
eliminating, the sole upper debt:

```text
reverse positions 5567..11365:  ef79 -> 6d3e
reverse positions   11..11268:  6d3e -> no upper debt
```

The resulting target order is

```text
scratch/k16_facet_augmented_uppercomplete_capacity27597_targets_20260731.word
SHA-256 63aababe9d5cbaeec4ce68a1ec32edc02d249caf3750bb20f6bc87c1ca1eac43.
```

It has every rank-eight mask exactly once, all `11440` q1 colours, and no
missing carrier interval at any rank nine through sixteen.  Its complete
three-hole schedule DP has

```text
maximum selected lower area       27588
unselected-start credit upper bound   9
lower-capacity upper bound         27597
required lower mass                26332
deadline holes                     10,12,13
start holes                     5722,10950,10951.
```

Thus all middle and upper carrier conditions coexist with a scalar lower
capacity margin of `1265`.  This remains only a necessary capacity result:
the fixed maximizing schedule has not supplied the integral lower compiler.

For calibration, the ordinary exact-prefix Hall graph of that fixed schedule
was also replayed after this note was first drafted.  It matches only
`24328/26332` lower targets (deficiency `2004`) and has `1478` targets with
no individually exact candidate in that schedule.  Consequently this
particular maximizing schedule cannot be the final physical compiler.  The
later theorem
`MATH_THEOREM_K16_UPPERCOMPLETE_FACET_PQ_AREA_CHAIN_PARETO_NOGO_20260731.md`
strengthens this to every three-hole schedule for the same target order: its
exact area/positive-chain Pareto frontier misses the simultaneous lower-cell
and rank-seven-chain thresholds.  A further carrier rethreading remains live;
merely choosing another P/Q schedule does not.

## 6. Reproducible artifacts

```text
scratch/audit_k16_facet_augmenting_path_20260731.py
scratch/k16_facet_augmenting_path_20260731.audit.json
scratch/k16_facet_augmented_middle_targets_20260731.word
scratch/k16_facet_augmented_area29283_targets_20260731.word
scratch/k16_facet_augmented_uppercomplete_capacity27597_targets_20260731.word
```

The audit independently reconstructs the source first-middle sequence,
checks every switched edge, traverses the output path, checks all rank-eight
vertices, compares the complete rank-nine multiplicity counters, audits all
deeper carrier intervals, and performs the unchanged-schedule maximal-core
test.  Its carrier target SHA-256 is

```text
9712d02ebfb97c4a773caa90c0933eea78f30834162c462f4dd50692186b6550.
```

The current audit payload SHA-256 is

```text
bfed4d9f7cae694cc561bb6debcc8e93b8a1434f1689d0645ab61f03caf70451.
```
