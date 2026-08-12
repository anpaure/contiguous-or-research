# Buffered occurrence donors at the exact `j=3959` RF-halo carrier

Date: 2026-07-30

Status: **PASS_EXACT_CONDITIONAL_COMPILER; PASS_LOCAL_TWO-UNIT ATOM;
PASS_UNIQUE UPPER RAY; ONE PHYSICAL DONOR-RETURN GATE OPEN**.

This note works only with the frozen rank-eight chronology

```text
scratch/k16_rf_halo_j_family_20260730/rank1_j3959.targets
SHA-256 edc3a3770f90140259f5e1d82c055bac634f49973aeaaff8cb06e42b18c581ee.
```

It does not claim a K16 universal word.  It proves four exact statements:

1. a compound coordinate involution simultaneously aligns three lower Hall
   ports with the five missing upper masks;
2. a literal depth-two collar creates two of the three missing lower
   neighbours;
3. a unique 112-row intact ray closes the complete upper spectrum in a
   precisely stated buffered architecture; and
4. the source vacancy of that ray cannot be closed by a singleton return.

The only unproved step is a common physical chronology realization of the
lower ports and the upper ray with a non-singleton return.

## 1. Exact Hall core

Put

```text
C = 0665,   P = 2665,   Q = 8000.
```

The exact deficient shore is

```text
X = {0665,066d,0675,06e5,0765,1665,2665,8000,8665},
Y = {803,2939,4349,9215,19070,27225}.
```

The six right cells are:

| cell | interval | allowed | mandatory | targets in `X` |
|---:|:---|:---|:---|:---|
| 803 | `[267,270)` | `0765` | `0465` | `0665,0765` |
| 2939 | `[979,982)` | `0675` | `0461` | `0665,0675` |
| 4349 | `[1449,1452)` | `066d` | `0464` | `0665,066d` |
| 9215 | `[3071,3074)` | `1665` | `0265` | `0665,1665` |
| 19070 | `[6356,6359)` | `06e5` | `0661` | `0665,06e5` |
| 27225 | `[10395,10397)` | `8665` | `0660` | `0665,8665` |

Thus `X-Y` is the disjoint union of a `7/6` extension star and the two
isolated vertices `P,Q`.  The deterministic matching used in the audit has
unmatched roots

```text
1665,2665,8000.
```

Only `2665,8000` are canonical roots; `1665` is the matching-relative root
of the star.

### Lemma 1.1 (protected Hall escape)

Let `G'` be a modified incidence graph on the same lower targets.  If all six
old cells and their old incidences are retained, then repairing this shore
requires at least three distinct new right cells.  Equality holds precisely
when the new cells have an SDR for the three roles

```text
S = one extra star neighbour,   P = a 2665 neighbour,
Q = an 8000 neighbour.
```

More generally, without monotonicity every repair of this fixed shore obeys

\[
 |N_{G'}(X)\setminus Y|-|Y\setminus N_{G'}(X)|\ge 3.                 \tag{1.1}
\]

#### Proof

The displayed table gives `|X|=9`, `|Y|=6`, so Hall gives (1.1).  Under the
retention hypothesis the second term vanishes.  One new cell has matching
capacity one, hence three distinct cells are necessary.  The old six cells
match all six star arms, so an SDR for `S,P,Q` is also sufficient.  Conversely
any perfect matching assigns one new cell to each isolated vertex and one
new cell to the unmatched star unit, giving that SDR.  ∎

This is the three-unit descendant of the 20-port occurrence graph in item
2038A.  The next construction deliberately leaves its Johnson-distance-one
face: two of its useful donor pairs have Johnson distance two.

## 2. Exact compound involution and conditional full compiler

Let

\[
 \pi=(0\ 1)(6\ 15)
\]

act on coordinate masks.  Direct calculation gives

```text
lower:
  9626 -> 1665,    a626 -> 2665,    0040 -> 8000;

upper:
  ce3a -> 4e79,    ef3a -> 6f79,
  ca7a -> ca79,    ea7a -> ea79,    eb7a -> eb79.
```

The first two lower pairs have symmetric difference `8043`, hence Johnson
distance two; the singleton pair has distance one.  They are therefore a
genuine compound escape from the restricted distance-one donor graph.

The exact lower donor occurrences used below are

| donor to receiver | spent cell | reserve occurrence |
|:---|---:|---:|
| `9626 -> 1665` | 24899, `[9232,9234)` | 24807, `[9186,9188)` |
| `a626 -> 2665` | 22239, `[7902,7904)` | 20377, `[6971,6973)` |
| `0040 -> 8000` | 9378, `[3126,3127)` | 190 other occurrences |

The exact upper donor intervals are

```text
ce3a: [8564,8566)
ef3a: [8563,8567), [8563,8568)
ca7a: [7226,7228)
ea7a: [6578,6581), [7226,7229)
eb7a: [6578,6582), [7814,7818).
```

### Theorem 2.1 (conditional all-gates compiler)

Let `M` be the deterministic size-26,329 matching frozen by the audit.
Suppose a physical modification of the chronology has the following
properties.

1. Cells `24899,22239,9378` acquire respectively the `pi`-image incidences
   to `1665,2665,8000`.
2. Every `M`-edge survives except possibly the four overwritten edges whose
   left endpoints are `0626,0202,a226,a024`.
3. Every incidence in the following reroutes exists:

```text
1665 -> 24899,  0626 -> 1596,  0202 -> 6141;
2665 -> 22239,  a226 -> 23338, a024 -> 26126;
8000 -> 9378.
```

Then the complete lower graph has a matching of size `26332`, so its Hall
deficiency is zero.  If the five displayed upper donor intervals are also
transported by the same coordinate action, all five upper holes are filled.

#### Proof

Before the modification the matched owners of

```text
24899,1596,6141 are 0626,0202,free,
22239,23338,26126 are a226,a024,free,
9378 is free.
```

Consequently the three displayed alternating reroutes are vertex-disjoint
and augment the old matching three times.  The resulting 26,332 right cells
are distinct.  For the upper assertion, coordinate permutations commute
with union, so every donor interval has the stated image.  ∎

The theorem is exact but conditional: it is an incidence certificate, not a
claim that a local coordinate relabelling preserves the middle deck or every
edge of `M`.

### Theorem 2.2 (sharp within the prescribed six-position mask grid)

In the common-anchor cumulative-OR architecture with two strict left
increments, one anchor, and three strict right increments, six nonempty
positions are necessary and sufficient to transport both upper chains and a
singleton `8000` port.  A witness is

```text
source: 2100 0400 ca3a 0040 2000 0100
target: 2100 0400 4a79 8000 2000 0100.
```

The half-open intervals

```text
[1,3), [0,3), [2,4), [2,5), [2,6)
```

have source ORs

```text
ce3a,ef3a,ca7a,ea7a,eb7a
```

and target ORs

```text
4e79,6f79,ca79,ea79,eb79.
```

The singleton `[3,4)` is `0040 -> 8000`.

#### Proof

The identities are direct OR calculations and the second row is the
coordinatewise `pi` image of the first.  For necessity, two strict left
chain increments require two distinct nonempty positions before the anchor;
three strict right increments require three distinct nonempty positions
after it.  Together with the anchor this is at least `2+1+3=6`.  ∎

Sharpness is only at mask-grid level.  The six masks are not asserted to be
a valid rank-eight chronology.

## 3. A literal two-unit lower Hall atom

The five unique source rows

```text
2ce5@6388, 2e65@6389, 6665@3955, 46e5@3954, 4ec5@3953
```

occur in this order at output positions `8849..8853` of the frozen
hard-motif rethread:

```text
2ce5,2e65,6665,46e5,4ec5.
```

Every row in `8842..8860` has depth two and exact local maximal-envelope
replay.  Around the atom the target/envelope ledger is

```text
21dd/019d, 29d5/2195, 28f5/20d5,
2ce5/28c5, 2e65/2865, 6665/2465,
46e5/0665, 4ec5/4645, 5e85/4685,
5c95/4c85, 5995/5885,
```

where every target is the OR of its three consecutive envelopes.

### Theorem 3.1 (local `9/6 -> 9/8` atom)

This collar creates the two distinct proper-prefix cells

| cell | interval | allowed | mandatory | service |
|---:|:---|:---|:---|:---|
| 18391 | `[8851,8853)` | `2665` | `2620` | `2665` |
| 18392 | `[8852,8853)` | `0665` | `0220` | excess star unit |

Thus, in any embedding which retains the old six shore cells, the local
matching number rises from six to eight and only `8000` remains.

#### Proof

For a proper-prefix cell `J`, a target `T` is feasible exactly when

\[
 M(J)\subseteq T\subseteq U(J),\qquad
 E_p\cap T\ne\varnothing\quad(p\in J).                              \tag{3.1}
\]

The displayed envelope ledger gives the two allowed and mandatory masks.
Substitution into (3.1) proves the two incidences.  The intervals, hence the
right vertices, are distinct.  Lemma 1.1 then gives the matching claim.  ∎

This is a physical *local* atom, not a completed chronology.  Its materialized
whole path preserves the complete target multiset but has the single remote
middle error

```text
row 12806: target 346d, replay 146d
```

and upper holes `6a79,6f3b`.  Also, every one of its five central rows has a
bit outside each of the original five upper holes.  Hence no interval
witnessing one of those five masks can pass through the collar; this is
neutrality to the named holes only, not arbitrary-upper preservation.

## 4. The unique intact upper ray and its return floor

Let `A=4a79@3959`.  Consider the following **buffered-ray architecture**:

1. keep residual row order;
2. retain the forward tail ray `eb60,ea61,ca71` at source positions
   `12823..12825`;
3. move `A` immediately after `ca71`;
4. follow it by one intact oriented source interval beginning at a physical
   rank-eight facet of `4e79`;
5. keep that interval inside one constant-depth sector and disjoint from the
   protected flats and service rows; and
6. require exact local maximal-envelope replay at its source closure and at
   the complete destination entry/exit cluster.

There are 18 oriented facet starts.  Exact boundary parsing leaves 30
locally compatible rays.

### Theorem 4.1 (unique upper-complete ray)

Exactly one of those 30 rays is arbitrary-upper-complete.  It is

\[
 B=Q[281:393]=(4e78,\ldots,6d70)
\]

in forward orientation, of length 112.  The materialized chronology has

```text
flats       6320,12869,12871
capacity    32063
upper holes none.
```

The five new witnesses, with inclusive output endpoints, are

```text
ca79 [12712,12713]     ea79 [12711,12713]
eb79 [12710,12713]     4e79 [12713,12714]
6f79 [12825,12826].
```

Its only middle-replay residue is

| row | target | replay | missing bits |
|---:|:---|:---|:---|
| 3844 | `2c6d` | `2c65` | `0008` |
| 3845 | `287d` | `2865` | `0018` |
| 3846 | `6879` | `6861` | `0018` |
| 3847 | `6a71` | `6a61` | `0010` |

#### Proof

The two seams incident with `A` give `ca71|A=ca79` and
`A|4e78=4e79`; extending left through `ea61,eb60` gives `ea79,eb79`.
The exit gives `6d70|4679=6f79`.  Complete contiguous-union replay proves
there are no other upper holes.

For the scoped uniqueness statement, the 18 oriented starts and every
allowed length are determined by the fixed source word.  The frozen auditor
first applies the two exact constant-depth boundary equations, producing 30
rows, and then performs full arbitrary-width upper replay on each row.  The
single surviving row is the one displayed.  Full maximal-envelope replay of
that materialization gives exactly the four-row table.  ∎

This is a finite exact theorem for the declared architecture, not a claim
that every buffered repair needs 112 rows.

### Lemma 4.2 (no singleton return)

Keep the depth-three source collars fixed and insert one rank-eight row `Z`
into

```text
...6665,2c6d,287d,6879 | Z | 6a71,6b61,7b60...
```

The local maximal-envelope equations hold if and only if

```text
Z in {4a79,6879,6a39}.
```

Each of `4a79,6879,6a39` has a unique source occurrence, at positions
`3959,3958,4513`, respectively.  Returning `4a79` removes the service pivot.
The formal filler `6879` is unavailable while the left collar is fixed: its
only occurrence is the protected left neighbour, so moving it into the
filler slot does not realize the duplicated configuration and leaves the
vacancy chronology unchanged.  The only admissible distinct singleton donor
is `6a39@4513`; moving it produces six bad middle rows and the upper holes
`6a3b,6b39`.  Therefore no target-multiset-preserving singleton return
completes the 112-ray architecture.  At least one further non-singleton
occurrence-labelled return segment is necessary.

#### Proof

At constant depth three,

\[
 E_p=T_{p-3}\cap T_{p-2}\cap T_{p-1}\cap T_p,
 \qquad T_i=E_i\cup E_{i+1}\cup E_{i+2}\cup E_{i+3}.                 \tag{4.1}
\]

Apply (4.1) to the seven affected rows.  Coordinatewise, the equations force

```text
one-bits  4839,
zero-bits 9586,
free bits 2240 = 0040 | 0200 | 2000.
```

The forced-one mask has rank six, so a rank-eight `Z` chooses exactly two of
the three free bits.  The three results are precisely
`4a79,6879,6a39`.  The unique-occurrence and service-pivot arguments exclude
`4a79` and `6879`; direct full replay of the only admissible distinct
transfer, `6a39@4513`, gives the six bad rows and holes stated above.  ∎

For comparison, the direct `8000` first-flat collar is also not a one-row
problem.  Among the 330 eligible no-top masks and their 331 physical
occurrences, deleting one occurrence and inserting it immediately after
`a879` yields zero structurally exact chronologies.  Thus at least two moved
rows are necessary in that narrower source-relative relocation class.  This
statement does not add to Lemma 4.2, because one compound segment could
serve both duties.

## 5. Exact proved/conditional boundary

The results above do **not** compose into a universal word yet.

What is unconditional:

- the `9/6` Hall core and its three-role escape criterion;
- the complete matching reroute conditional on the three named incidence
  retypings, survival of every unaffected edge of the frozen matching `M`,
  and the displayed reroute incidences;
- the `pi` lower/upper maps and the sharp six-position mask skeleton;
- the literal depth-two two-unit lower atom;
- the unique upper-complete 112-row intact ray in the stated architecture;
  and
- the impossibility of a singleton return for that ray.

The minimum remaining physical hypothesis is the following.

> **Buffered donor-return gate `BDR_3959`.**  There is a
> target-multiset-preserving compound segment exchange which replaces the
> `4a79` source vacancy by a non-singleton return, has exact G0/maximal-
> envelope middle replay, is arbitrary-upper-complete, and whose recomputed
> lower incidence graph satisfies one of the following exact certificates:
> (i) an explicit full SDR; (ii) Theorem 2.1's `M`-retention hypothesis and
> its three `pi`-labelled incidences; or (iii) retention of the whole old
> matching and six shore cells together with an SDR for the three roles
> `S,P,Q`, for example the two-unit atom plus an `8000` port.

By Theorem 2.1 and Lemma 1.1, `BDR_3959` gives a complete lower compiler and
all upper masks for this carrier.  Neither ordinary O4 nor singleton/block
co-location can prove it; those faces are already closed.  A valid next move
must be a genuine occurrence-labelled donor-return braid.

## 6. Reproducibility

Hall/involution auditor:

```text
scratch/threadA_k16_rf_halo_j3959_buffer_20260730/
  audit_j3959_hall_buffer.py
    SHA 3fdac825c704fb3389ce5db33b084533b65fae6a3397f3d0b5aae887d5a20cc5
  j3959_hall_buffer.audit.json
    SHA 3908783e72b216756c193e17cf824665505f61c07e0537bbaff636bcfe7fa498
    payload dae27ab410a96bf09aa5fde19085f7d551faaff2c6bdc74e61eddfde2e34a476
```

Upper-ray auditor and materialized near atom:

```text
  audit_j3959_upper_buffer.py
    SHA 124eaa6bf22c67c5d8ca8d68cc2632cb3119edd5cd26c0406a4abadfe933568f
  j3959.upper_buffer_112.targets
    SHA 7bbb357ca2ff6bb9d1c917107561d9aac1de4de5a2ee453036a83f8b0bab09c8
  j3959.upper_buffer_112.audit.json
    SHA 51901406fc90c72435ff991ec8727ffa072bea31b486135c302509d1bed91c46
    payload 29701866b1c7fbf4085b38d1f10e3651f1728fb06d424a10cb1baa0790d7d268
```

Local lower atom:

```text
  audit_j3959_lower_two_unit_atom.py
    SHA e0def4a94ad3bdf82ddf797849ba1f72b77e1937a6c3c22831c16ec5874eaf6f
  j3959.lower_two_unit_atom.audit.json
    SHA 3aa255146a0c5bee8db5b0646a72dd870d4d8144c75fbc6a85cdc63681911ece
    payload 947123e472edb7be4e88a3de6d64a5c0541341a1c6199b71afd2cf3e79998475
```

Direct one-row top-collar reproducer:

```text
scratch/enumerate_k16_j3959_top_collar_relocations_20260730.cpp
SHA 301d717c24dc75018c3ec77a34d88eee5d2cf622a40670bb4ffe5a8c90d8b3b7

output:
eligible=330 relocation_trials=331 structural_survivors=0
```
