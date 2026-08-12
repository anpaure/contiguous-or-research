# The next Type-I boundary-face hierarchy

## 1. Result

Assume the exact Type-I `k=11,n=465` branch.  After the unique literal
six-set endpoint `T=63` is removed, the suffix has the exact peel

```text
P_5 || C_4 || Q_5,                                      (1.1)
```

where every entry of `C_4` has rank at most four and `C_4` represents every
nonempty mask of rank at most four.  Every physical interval of length three
inside `C_4` contains a selected rank-five witness.

For any `Q subseteq [11]`, define

```text
s_Q = #{i in C_4 : A[i] is a nonempty proper subset of Q}.
```

The next two levels below the deployed four-set ridge theorem are

```text
|Q|=4:  s_Q >= 10,       (already deployed ridge row)
|Q|=3:  s_Q >=  5,       (new locally sharp pointwise row)
|Q|=2:  s_Q >=  2.       (locally sharp but atomwise redundant)       (1.2)
```

These statements hold for all `C(11,3)=165` triples and all `C(11,2)=55`
pairs; the compact endpoint specialization uses the twenty triples and
fifteen pairs contained in `T`.  The value five at dimension three is not
the value four obtained by merely
counting singleton and adjacent-pair cells.  Four positions can provide six
physical cells, but the Boolean OR labels of those cells cannot be the six
proper masks of a three-cube.  This is the first algebraic collision in the
strict face hierarchy.

There is also a much cheaper aggregate consequence.  Put

```text
c_j = #{i in C_4 : A[i] subseteq T and |A[i]|=j},  j=1,2.
```

Then

```text
c_1 >= 6,
c_1 + 2*c_2 >= 30.                                      (1.3)
```

Writing `n_j` for the total number of literal rank-`j` entries gives the
global companion

```text
n_1 + 2*n_2 >= 110.                                     (1.4)
```

Each displayed support/profile constant is locally sharp for its stated
isolated face or rank-one/rank-two subproblem.  Equation
(1.4) is the cheapest recommended first implementation: it is a `1,864`
variable / `13,053` clause propagation module.  The endpoint refinement
(1.3) costs `2,788/15,810`.  The full twenty-row three-face bank is
strictly stronger pointwise and costs `27,680` variables / `165,960`
clauses over retained ridge literals.

All these rows are consequences of the exact base interval-OR formula.
They remove no genuine Type-I solution; their SAT purpose is propagation.
They are, however, not consequences of the projected numerical rank, width,
nested-support, facet, and ridge ledger explicitly checked below.
Deterministic separating multisets certify that projected statement; they
are not claimed to extend to assignments of every auxiliary variable in the
complete CNF.

## 2. The common core fact

Write `|C_4|=q+2`, where the `q` nonliteral rank-five masks have selected
witnesses `I_1,...,I_q` wholly inside the core.  Ordered by left endpoint,
the standard endpoint-slack normal form gives

```text
I_i subseteq [i,i+2].                                   (2.1)
```

Consequently every core interval of length at least three contains a
selected rank-five witness.  If `Q` has rank at most four and we mark the
positions whose entries are proper subsets of `Q`, every marked run has
length at most two: a marked triple would have OR contained in `Q` while
containing a rank-five witness.

If `p` marked positions form `rho` runs, their singleton and adjacent-pair
capacity is

```text
2p-rho <= p+floor(p/2).                                 (2.2)
```

For a `d`-face there are `2^d-2` nonempty proper targets.  The crude capacity
inversion is therefore

| face rank `d` | proper targets | least `p` from (2.2) | locally sharp `s_Q` |
|---:|---:|---:|---:|
| 2 | 2 | 2 | 2 |
| 3 | 6 | 4 | **5** |
| 4 | 14 | 10 | 10 |

The four-face row is exactly the audited ridge theorem.  The two-face row is
immediate.  The only nontrivial new issue is why the apparent three-face
value four is impossible.

## 3. Sharp three-face theorem

### Theorem 1

For every three-set `Q subseteq [11]`,

```text
#{i in C_4 : A[i] proper-subset Q} >= 5.                (3.1)
```

Equivalently, if

```text
p_Q = #{i in C_4:A[i] subseteq Q},
m_Q = #{i in C_4:A[i]=Q},
```

then

```text
p_Q >= 5+m_Q.                                           (3.2)
```

This applies in particular to all twenty triples

```text
Q_bcd=T\{b,c,d},  0<=b<c<d<6.                           (3.3)
```

### Proof by strict rank profile

Let `a_Q` be the number of rank-one marked positions and `b_Q` the number of
rank-two marked positions.  Every singleton target in `Q` forces a literal
singleton occurrence, so

```text
a_Q >= 3.                                               (3.4)
```

Consider the three rank-two targets inside `Q`.  At most `b_Q` of them can
be paid for by literal rank-two occurrences.  Every remaining target must
use an adjacent pair of its two singleton atoms.  Such atom-pair witnesses
are physically disjoint.  Otherwise two adjacent pairs sharing a position
would create three consecutive singleton entries, contradicting the
length-three core fact of Section 2.  Hence at most `floor(a_Q/2)` rank-two
targets are paid for by atom pairs.  Therefore

```text
b_Q+floor(a_Q/2) >= 3,
```

or, equivalently for integers,

```text
a_Q+2*b_Q >= 6.                                         (3.5)
```

Minimizing `a_Q+b_Q` under (3.4)--(3.5) gives five.  Since strict support is
exactly `a_Q+b_Q`, this proves (3.1).

There is also a short direct proof of the exceptional `p=4` case.  Six
available cells force two separated two-position runs.  In each run the
three OR values are `X,Y,X union Y` and must be distinct.  A singleton can
only occur as `X` or `Y`.  One run must therefore contain two of the three
singletons and its union is their two-set.  The other run must contain the
remaining singleton and the two remaining two-sets.  Joining that singleton
to either remaining two-set either repeats the two-set or produces the top
three-set, never the other proper two-set.  This is impossible.

### Local sharpness

On `Q=7`, the five strict entries in the separated runs

```text
(1,2), (4,5), (6)                                       (3.6)
```

represent all six masks `1,...,6`.  Their rank profile is exactly
`(a_Q,b_Q)=(3,2)`.  If `Q` itself has no literal occurrence, the runs

```text
(1,2), (5,6), (4)                                       (3.7)
```

represent all seven masks `1,...,7`.  Thus neither nonliterality of `Q` nor
the complete local target family raises the five-position threshold using
only the face-label/run hypotheses.  These gadgets are not asserted to
extend to a complete Type-I word, so a stronger theorem using global core
interactions is not ruled out.

## 4. Two-faces and the compact pair-profile theorem

For a two-set `Q={a,b}`, witnesses for the singleton targets `{a}` and `{b}`
force one literal occurrence of each atom.  They are two distinct positions
and both are proper subsets of `Q`, proving `s_Q>=2`.  The adjacent word
`a,b` is sharp and also represents `Q` if `Q` is nonliteral elsewhere.

This pointwise row should **not** receive fifteen new counters.  The existing
rank-one target clauses already force the two individual atom occurrences,
which is strictly more informative than their pairwise sum.

The interaction with all fifteen rank-two targets does yield a useful compact
row.

### Theorem 2 (endpoint pair profile)

With `c_1,c_2` as in Section 1,

```text
c_1 >= 6,
c_2+floor(c_1/2) >= 15,                                 (4.1)
```

and hence exactly

```text
c_1+2*c_2 >= 30.                                        (4.2)
```

### Proof

The six singleton targets inside `T` give `c_1>=6`.  A rank-two target inside
`T` either has a literal rank-two occurrence, or its length-at-most-two
witness is an adjacent pair of its two atoms.  Literal occurrences pay for
at most `c_2` distinct targets.  Two atom-pair witnesses cannot overlap:
an overlap again gives three consecutive singleton entries and contradicts
Section 2.  Thus atom pairs pay for at most `floor(c_1/2)` targets.  There are
fifteen targets, proving (4.1).  The floor inequality is equivalent to (4.2)
because `c_1+2c_2` has the parity of `c_1`.  QED.

The theorem is sharp for the isolated rank-one/rank-two target system.  Use one occurrence of each of the six atoms, pair
them as `(0,1),(2,3),(4,5)`, and represent those three rank-two targets by
the adjacent atom pairs.  Supply the other twelve rank-two masks literally.
Then `(c_1,c_2)=(6,12)` and equality holds in (4.2).

Exactly the same argument over all eleven coordinates gives a still cheaper
global row.  All rank-one and rank-two entries lie in `C_4`.  Among the 55
rank-two targets, at most `n_2` have literal representatives and at most
`floor(n_1/2)` can use pairwise-disjoint adjacent atom witnesses.  Hence

```text
n_2+floor(n_1/2) >= 55,
n_1+2*n_2 >= 110.                                       (4.3)
```

This is locally sharp: take twelve atom occurrences and arrange them as six
disjoint adjacent pairs with distinct ORs, for example
`(0,1),(2,3),(4,5),(6,7),(8,9),(10,0)`, and supply the remaining 49 pair
targets literally.  Then `(n_1,n_2)=(12,49)` and equality holds.

Summing the twenty pointwise three-face rows would give only

```text
10*c_1+4*c_2 >= 100.                                    (4.4)
```

The compact pair profile is stronger in aggregate: (4.2) and `c_1>=6` give

```text
10*c_1+4*c_2 >= 108.                                    (4.5)
```

Therefore no separate aggregate encoding of the twenty three-face rows is
useful.  Their remaining value is their pointwise distribution among the
twenty named triples.

For comparison, summing all 165 global three-face rows yields only

```text
45*n_1+9*n_2 >= 825,  equivalently 5*n_1+n_2>=92.       (4.6)
```

Here the integer right side is 92, since the left side is integral after
division by nine.  This is already implied by the Type-I rank-filtration
rows `n_1>=11` and `n_1+n_2>=56`, whose combination gives
`5*n_1+n_2>=100`.  Thus the useful global aggregate is the pair-witness
interaction (4.3), not the sum of strict triple supports.

## 5. Relation to the present CNF

There are two different notions of redundancy.

### Logical redundancy relative to the base formula

The base CNF is an exact encoding of a universal array.  Its rank-one and
rank-two `DirectTarget` records, exact OR clauses, nonzero-entry clauses, and
the Type-I core geometry imply Theorems 1--2.  With the named-cell guard, the
chosen lower witnesses are additionally exposed as singleton or adjacent
physical cells.  Consequently every proposed face row is a redundant
propagation lemma, just like the facet and ridge modules; none narrows the
set of genuine arrays.

The two-face rows are particularly close to the existing syntax: each is
just the sum of two atom-existence consequences.  They add no worthwhile
interaction and should be omitted.

The three-face row is less local.  Deriving it requires combining six target
witnesses, excluding a four-position OR labeling, and using the common
length-three core obstruction.  No current auxiliary variable records this
five-position consequence.

### Nonredundancy relative to materialized summaries

The current pointwise support table gives only `p_Q>=4` at rank three, and
literal copies of `Q` may pay that total-support row.  The local-density PB
module materializes only aggregate entry-rank moments.  The facet and ridge
modules constrain five- and four-faces but allow their support to come from
entries outside a specified triple.  The selected-width, rank-seven-width,
subcube-credit, onion-component, and residual-lex summaries likewise contain
no three-face strict count or `T`-restricted rank-one/rank-two profile.

The checker constructs a deterministic Type-I-shaped multiset with

```text
entry ranks             (31,45,110,238,40,1),
rank-5 widths           (40,284,138),
rank-6 widths           (1,42,284,135),
rank-7 widths           (0,4,42,284),
pointwise support minima 1,2,4,10,20,37,67,117,192,308.
```

All six endpoint facets have load at least twenty, all fifteen ridges have
strict load at least ten, every current rank moment and six-subcube-credit
row passes, but

```text
s_{\{0,1,2\}}=4,
(c_1,c_2)=(6,1).
```

Thus it violates both new conclusions.  A second deterministic certificate
satisfies the compact profile with `(c_1,c_2)=(15,10)` while retaining
`s_{\{0,1,2\}}=4`; hence the pointwise bank remains strictly stronger than
the compact aggregate in the projected relaxation.  Neither certificate is
claimed to satisfy the base interval-OR formula.

A third actual multiset passes the same pointwise nested-support, facet,
ridge, moment, and Type-I rank-architecture summaries with

```text
(n_1,...,n_6)=(56,0,110,165,133,1),
pointwise support minima=5,10,15,20,27,42,66,110,182,293,
```

but has `n_1+2*n_2=56<110`.  Hence the global pair profile (4.3) is also
strictly outside the current projected ledger.

## 6. Exact implementation options

No production source is edited by this note.

### Option A: global pair profile (recommended first)

Reuse the 465 exact rank-one/rank-two flags and count them directly.  Add
`n_1` to the one-bit left shift of `n_2` and impose
`n_1+2*n_2>=110`.  The existing Type-I filtration already imposes
`n_1>=11`.

| component | variables | clauses |
|---|---:|---:|
| two exact 465-input counters | 1,844 | 12,908 |
| one ten-stage full ripple addition | 20 | 140 |
| direct comparison to 110 | 0 | 5 |
| **total** | **1,864** | **13,053** |

This is the smallest genuinely interactive row in the hierarchy and needs
only the Type-I filtration's exact rank flags.  It should be the first
microbenchmark.

### Option B: compact endpoint pair profile

Reuse the exact support literals for `T=63` and the exact rank-one/rank-two
flags.  For each suffix position define

```text
u_j[i] <-> support_T[i] AND rank_j[i],  j=1,2.
```

Count the two 464-input rows exactly, impose `c_1>=6`, add `c_1` to the
one-bit left shift of `c_2`, and impose `c_1+2*c_2>=30`.

| component | variables | clauses |
|---|---:|---:|
| 928 exact two-input gates | 928 | 2,784 |
| two exact 464-input counters | 1,840 | 12,880 |
| one ten-stage full ripple addition | 20 | 140 |
| direct comparisons to 6 and 30 | 0 | 6 |
| **total** | **2,788** | **15,810** |

This is only about one eighth of the ridge module.  It should be added behind
an independent guard and microbenchmarked before being made part of every
Type-I portfolio.  It is coordinate-sensitive and complementary to Option A;
the two compact modules together cost only `4,652/28,863`.

### Option C: all twenty pointwise three-face rows

Retain each existing ridge strict-support vector as zero-CNF bookkeeping.
For `b<c<d`, reuse the row for `T\{b,c}` and define

```text
w[b,c,d,i] <-> ridge_support[b,c,i]
                 AND !A[i,d] AND !rank3[i].              (6.1)
```

The first two conditions put the entry inside `T\{b,c,d}`.  The exact
`!rank3` literal excludes the only nonproper contained value.  Impose

```text
sum_i w[b,c,d,i] >= 5                                   (6.2)
```

for all twenty triples.

| component | variables | clauses |
|---|---:|---:|
| `20*464` exact three-input gates | 9,280 | 37,120 |
| twenty exact 464-input counters | 18,400 | 128,800 |
| direct comparisons to 5 | 0 | 40 |
| **total** | **27,680** | **165,960** |

The natural dependency is

```text
TYPE1_TRIPLE_PIN_LOAD -> TYPE1_RIDGE_PIN_LOAD.
```

This bank is still below one percent of the current full Type-I clause
inventory, but it is large enough that it should be an A/B portfolio branch,
not silently enabled everywhere.  The stronger profile
`a_Q>=3, a_Q+2b_Q>=6` is mathematically exact but would need separate
rank-one/rank-two counters for every triple; its extra cost is not justified
before the cheaper `s_Q>=5` bank is benchmarked.

### Option D: pointwise two-face rows (do not implement)

The fifteen thresholds `s_Q>=2` merely recombine the six already required
singleton values.  They add counters without exposing a new interaction.
Use Options A--B instead.

## 7. Verification and scope

Run

```text
python3 scratch/check_k11_type1_face_hierarchy_next.py
```

The checker verifies:

* the crude `2,4,10` run-cap inversion;
* exhaustive impossibility of a four-position three-face labeling;
* sharp five-position gadgets with and without a literal top;
* the exact strict rank-profile optimization;
* sharpness of the compact pair profile;
* three deterministic auxiliary-summary separation certificates;
* every displayed pointwise support minimum, facet/ridge row, width row,
  rank moment, and six-subcube credit in those certificates; and
* all three exact CNF inventories.

The result is a new compact propagation hierarchy inside the Type-I branch.
It proves neither SAT nor UNSAT, changes no bound on `nu(11)`, and supplies no
evidence from a solver run.  The implementation recommendation is therefore:

1. encode and microbenchmark the `1,864/13,053` global pair profile;
2. test the complementary `2,788/15,810` endpoint pair profile;
3. retain the twenty three-face rows as a separate stronger Type-I branch;
4. do not spend CNF on the pointwise two-face sums.
