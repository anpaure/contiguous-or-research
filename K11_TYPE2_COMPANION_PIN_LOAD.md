# Companion pin load on the localized side of the `k=11` Type-II branch

## 1. Audited result

Assume a hypothetical zero-free universal word of length `465` is in the
Type-II two-component branch.  Orient the two rank-at-most-four components as

```text
C1 = the slack-one component,
C2 = the slack-two component.
```

For a coordinate `b`, write

```text
o1(b) = #{p in C1 : b in A[p]},
n1    = |C1|,
z     = the number of literal rank-five entries.
```

Then

```text
b notin OR(C2)  =>  o1(b) >= 176,                    (1.1)
b notin OR(C2)  =>  n1 + z >= 211.                   (1.2)
```

The first row is the immediate named-coordinate projection of the existing
literal-localization theorem.  The second is its rank-five companion.  Both
are strictly stronger than the numerical information currently retained by
`TypeIITwoComponentPinPlan`; `TypeIIReversePinLoadPlan` is dormant in this
orientation because `C1` is then coordinate-complete.

There is a stronger rank-resolved form.  Put

```text
o1,s(b) = #{p in C1 : b in A[p] and |A[p]|=s}.
```

For `1<=s<=4`,

```text
b notin OR(C2)  =>  o1,s(b) >= C(10,s-1).             (1.3)
```

Thus the four exact lower bounds are

```text
(o1,1(b),o1,2(b),o1,3(b),o1,4(b)) >= (1,10,45,120).  (1.4)
```

Summing (1.4) gives (1.1), but the converse fails even after the current
aggregate rank rows are imposed.  The full rank-resolved circuit is therefore
genuinely stronger, although it is much more expensive than (1.1).

The recommended first implementation is the compact pair (1.1)--(1.2).

## 2. Proof of the lower-rank load

The audited Type-II two-component theorem supplies the following facts.

* Every entry in `C1` and `C2` has rank at most four.
* Every position outside the two components is a distinct literal five-set.
* Every internal adjacent pair of `C1` is a selected rank-five witness.
  Hence every interval of `C1` of length at least two has rank at least five.
* At least one of `OR(C1),OR(C2)` is `[11]`.

Fix `b notin OR(C2)`.  There are

```text
sum_(s=1)^4 C(10,s-1) = 1+10+45+120 = 176            (2.1)
```

nonempty targets of rank at most four containing `b`.

Such a target cannot have a witness meeting a literal rank-five separator,
and it cannot have a witness in `C2`, whose union omits `b`.  Its witness must
therefore lie in `C1`.  But a rank-at-most-four witness in the slack-one
component is a singleton physical interval.  Consequently every one of the
176 target values occurs literally at a different position of `C1`.

Every one of those positions contains `b`, proving (1.1).  Restricting to
rank `s` gives `C(10,s-1)` different literal positions and proves (1.3).

This proof also shows why merely knowing that `C1` contains the coordinate is
far too weak: one physical occurrence cannot pin 176 different literal
target values.

## 3. Rank-five companion

There are

```text
C(10,4)=210                                           (3.1)
```

rank-five targets containing `b`.  Let `z_b` be the number of literal
rank-five entries containing `b`, so `z_b<=z`.

Every other one of these `210-z_b` targets is nonliteral.  A selected witness
for it cannot cross a literal rank-five separator: a rank-five literal inside
a rank-five union would have to equal the target.  Nor can the witness lie in
`C2`, which omits `b`.  It therefore lies in `C1`.

The slack-one component has exactly `n1-1` selected nonliteral rank-five
witnesses, namely its internal adjacent pairs.  Hence

```text
n1-1 >= 210-z_b,
n1+z_b >= 211,
n1+z >= 211.                                         (3.2)
```

This proves (1.2).

There is an exact edge-level refinement.  If

```text
e1(b) = #{internal adjacent pairs of C1 whose OR contains b},
```

then

```text
e1(b)+z >= 210.                                      (3.3)
```

The path bounds `e1(b)<=n1-1` and `e1(b)<=2o1(b)` project (3.3) to

```text
n1+z>=211,
2o1(b)+z>=210.                                       (3.4)
```

The second row of (3.4) is redundant after (1.1), since `2*176>210`.
The first is not redundant.  Thus (1.2), rather than another touched-cell
minimum, is the useful compact scalar projection of the rank-five family.

## 4. Adversarial checks

### 4.1 Orientation and witness-choice loopholes

If `C2` omits `b`, coordinate completeness of at least one low component
forces `OR(C1)=[11]`.  This makes every antecedent of the existing reverse
module false: that module is intentionally aimed at the opposite orientation,
where `C1` has the deficit.

The proof does not require a witness choice beyond the already encoded
canonical choice.  Literal five-set targets use their singleton occurrences;
every remaining five-set has one selected nonliteral witness.  The `{1,2}`
component slack identity and the selected slack-one certificate then make all
selected witnesses in `C1` precisely its adjacent pairs.

### 4.2 Multiplicity and overlap

Different target values require different literal positions.  Repeated
entries can only increase `o1(b)` and cannot invalidate (1.1) or (1.3).

If `C2` misses two coordinates, the two families overlap, but each
coordinatewise count remains valid.  A stronger two-coordinate projection is
available; for example, for missing `b,c`, at least

```text
sum_(s=2)^4 C(9,s-2)=1+9+36=46
```

positions of `C1` contain both.  Encoding all 55 pair counters is not compact
and is not recommended before the eleven one-coordinate rows have been
benchmarked.

### 4.3 Why the existing aggregate rank rows do not imply (1.1)

The current localization circuit conditionally enforces only

```text
(a1(C1),a2(C1),a3(C1),a4(C1)) >= (1,10,45,120).
```

Those positions are not required by that projection to contain the *named*
missing coordinate.  The exact entry bits and the full OR formula of course
semantically imply the theorem; the strictness statements below concern the
currently exposed structural projection, as is appropriate for a redundant
SAT strengthening.

## 5. Strict abstract separations

All three examples below use the valid global marginal profile from the
reverse-pin analysis:

```text
z=1,
y=(y0,y1,y2)=(1,364,97),
x=(x0,x1,x2,x3)=(0,4,364,94),
entry ranks (a1,a2,a3,a4,a5)=(11,45,110,298,1).
```

They are certificates against the retained projection, not proposed OR
arrays.

### 5.1 The named load is new

Take

```text
(q1,q2)=(252,209),  (n1,n2)=(253,211),
|OR(C1)|=11,        OR(C2)=[11]\{b},
C1 ranks=(1,10,45,197),
C2 ranks=(10,35,65,101).
```

Let only one `C1` position, the rank-one position, contain `b`.  All current
conditional rank totals hold, the component identities and width marginals
hold, and the reverse module is dormant because `C1` is complete.  But

```text
o1(b)=1<176.
```

Thus (1.1) is absent from both current modules.

### 5.2 The rank-five length row remains new after (1.1)

Take

```text
(q1,q2)=(175,286),  (n1,n2)=(176,288),
|OR(C1)|=11,        OR(C2)=[11]\{b},
C1 ranks=(1,10,45,120),
C2 ranks=(10,35,65,178),
o1(b)=176.
```

Allocate 175 of the `y1` pair witnesses to `C1`, and allocate the remaining
189 pairs and all 97 triples to `C2`.  This satisfies the component slacks,
the aggregate literal-localization rows, the existing named-cell lower bound
`q2>=95+z`, and the new row (1.1).  Nevertheless

```text
n1+z=177<211.                                        (5.1)
```

The failure is exactly that the projection has allowed 286 distinct
rank-five values inside a ten-coordinate component, where only 252 exist.
Row (1.2) exposes the relevant named-coordinate eligibility without
materializing rank-five target names.

### 5.3 Rank resolution is stronger than the total load

Return to `(n1,n2)=(253,211)` and use

```text
C1 ranks=(11,45,77,120),
C2 ranks=(0,0,33,178),
(o1,1(b),o1,2(b),o1,3(b),o1,4(b))=(11,45,77,43).
```

Then `o1(b)=176`, `n1+z>=211`, and all aggregate rank rows hold, but

```text
o1,4(b)=43<120.
```

So the rank-four member of (1.4), and hence the full rank-resolved package,
is not implied by the compact pair.

## 6. Cheapest exact CNF design

### 6.1 Reused literals and guards

`TypeIITwoComponentPinPlan` already retains exact literals

```text
in1[p]  <-> p in C1,
has2[b] <-> b in OR(C2),
rank1_count,...,rank4_count inside C1.
```

`TypeIIReversePinLoadPlan` already constructs, for its exact `C1` union,

```text
occ1[b,p] <-> (in1[p] and b in A[p]).                 (6.1)
```

The current source stores these occurrences in a local vector.  Retaining
them as

```text
array<vector<int>,K> slack_one_occurrence
```

is a zero-variable, zero-clause refactor.  The companion module should reuse
that bank.  If the reverse module is disabled, the 5,115 conjunctions in
(6.1) can instead be built locally.

Every substantive row uses the escape

```text
{-two_components, has2[b]}.
```

It is active exactly when the two-component branch holds and `C2` omits the
named coordinate.

### 6.2 Compact coordinate-load row

For each `b`, use the audited Wallace/ripple circuit to form the exact count

```text
o1[b] = sum_p occ1[b,p].
```

Then impose `176<=o1[b]` under the escape above.  A 465-input exact counter
costs `922` variables and `6,454` clauses.  Since binary `176` has three set
bits, its guarded direct comparator uses three clauses.  Across eleven
coordinates the exact incremental inventory is

```text
10,142 variables / 71,027 clauses.                   (6.2)
```

No extra occurrence gate is included in (6.2).

### 6.3 Nearly free rank-five length row

Do not recount `in1`.  Because `C1` consists only of ranks one through four,

```text
n1 = rank1_count+rank2_count+rank3_count+rank4_count.
```

The four retained counters are nine-bit exact vectors.  Two parallel
nine-bit additions, one ten-bit addition, and one eleven-bit addition of the
existing `z=n5_count` use

```text
78 variables / 546 clauses.
```

The guarded comparison `211<=n1+z` has five clauses per coordinate.  Thus
(1.2) adds only

```text
78 variables / 601 clauses.                          (6.3)
```

to the whole module; the arithmetic sum is shared by all eleven guards.

The recommended compact package (1.1)--(1.2) therefore costs exactly

```text
10,220 variables / 71,628 clauses                    (6.4)
```

when the existing `C1` occurrence gates are reused.  As a standalone module
without the reverse plan, add `5,115` variables and `15,345` clauses, for

```text
15,335 variables / 86,973 clauses.                   (6.5)
```

### 6.4 Rank-resolved optional tier

For every `b,s,p`, define

```text
g[b,s,p] <-> (occ1[b,p] and rank[p][s]).
```

Four banks require 20,460 exact conjunctions.  Counting all 44 banks and
imposing the four constants in (1.4) gives, with `occ1` reused,

```text
61,028 variables / 345,477 clauses.                  (6.6)
```

This tier is mathematically stronger but too large for the first portfolio.
A useful intermediate experiment is the rank-one existence row alone.  It
needs 5,115 conjunctions and one long guarded existence clause per
coordinate:

```text
5,115 variables / 15,356 clauses.                    (6.7)
```

It forces the literal `{b}` into `C1` rather than merely requiring 176
untyped occurrences.

### 6.5 Edge-level optional tier

The exact strengthening (3.3) can be encoded by one touched-edge gate per
coordinate and adjacent physical pair, eleven 464-input counters, and eleven
guarded additions with `z`.  With direct five-clause definitions of internal
`C1` touched edges, its incremental inventory is

```text
15,422 variables / 97,790 clauses.                   (6.8)
```

This is much more expensive than the scalar consequence (1.2).  It should be
considered only if a benchmark shows that the compact package leaves many
low-`z`, clustered-occurrence survivors.

## 7. Recommendation and scope

The recommended deployment order is:

1. retain the already-created `C1` occurrence gates;
2. add the exact eleven counts and (1.1);
3. add the shared 60-variable arithmetic for (1.2);
4. benchmark before adding rank-specific or edge-specific banks.

The compact package is globally WLOG in the exact Type-II two-component
branch.  It fixes neither a coordinate nor a component cut.  It does not
change the rigorous bracket for `nu(11)` and it is not a substitute for an
independently verified SAT model or proof trace.

The companion checker is

```text
python3 scratch/check_k11_type2_companion_pin_load.py
```

and verifies all constants, the three strictness profiles, the redundancy
claims, comparator truth tables, and every inventory above.
