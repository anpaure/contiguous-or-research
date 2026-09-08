# Rank-histogram surplus cuts for the exact `k=11,n=465` onion branches

## Status

This note proves three new necessary cell-capacity cuts.  They strengthen the
aggregate rows in `K11_CORE_CELL_INCIDENCE_CUTS_20260724.md` by observing that
duplicate literal entries of one rank cannot all be used as singleton
witnesses: there are only `C(11,r)` distinct targets of rank `r`.

Let

```text
c1=11, c2=55, c3=165, c4=330,
nr = number of rank-r entries in the rank-at-most-four low core(s),
S  = n1+2*n2+3*n3+4*n4.
```

Define the unweighted and weighted singleton surpluses

```text
F = sum_(r=1)^4 max(nr-cr,0),
E = sum_(r=1)^4 r*max(nr-cr,0).                    (0.1)
```

The new Type-I rows are

```text
y2 >= 96+z+F,                                      (T1-H0)
3*S-E-5*y1 >= 1938,                                (T1-H1)
6*S-E+5*z >= 4254.                                 (T1-H2)
```

Here `z=n5` is the selected/physical literal rank-five count and `y1,y2`
are the selected rank-five pair/triple counts.

For corrected Type II, let `n5` be the physical rank-five count, `s` the
number of low components, and `tight` the exact corrected stability-tight
flag.  Thus `tight=1` exactly in the duplicate/one-component and
no-duplicate/two-component cases.  Under `tight`, the two short-core rows are

```text
y2 >= 95+n5+F,                                     (T2-H0)
3*S-E-5*y1 >= 1936+2*s.                            (T2-H1)
```

In all three corrected Type-II cases the three-cell row is

```text
6*S-E+5*n5 >= 4254+5*tight.                        (T2-H2)
```

The old rows are the `F=E=0` projections of these inequalities.  In
particular, `(T1-H1)` and `(T1-H2)` imply `(I2)` and `(I3)`, while `(T2-H2)`
implies `(II3)`.

These are redundant consequences of the exact OR formula, not an
infeasibility proof.  No production solver is edited here.

## 1. Exact branch geometry used

The proof uses only the already audited onion facts.

### Type I

After deleting the unique rank-six endpoint and the `z` distinct literal
rank-five entries, the unique low core has

```text
N=464-z,
q=462-z=N-2
```

positions and selected nonliteral rank-five witnesses.  Every lower target
has a singleton/pair witness.  The selected nonliteral rank-five witnesses
are `y1` internal pairs and `y2` internal triples, with

```text
y1+y2=q=462-z.                                     (1.1)
```

### Type II

Write

```text
delta=n5-z,
s=# low components.
```

The exact corrected alternatives are

```text
(delta,s) in {(0,1),(1,1),(0,2)}.                  (1.2)
```

The number of low positions and selected nonliteral rank-five targets is

```text
N=465-n5,
q=462-z=462-n5+delta.                              (1.3)
```

Every selected nonliteral rank-five witness is internal to one low
component and has length two or three.  In the two `tight` cases every lower
target has a singleton or internal-pair witness.  In the remaining
no-duplicate/one-component case it has a witness of length at most three.

In the two-component case the total slack is three, split as one and two.
In particular one component is nonempty and the other has length at least
two.

## 2. Singleton histogram capacity

For each `r=1,...,4`, a rank-`r` singleton cell has the value of its physical
entry.  Although there are `nr` such positions, at most `cr=C(11,r)` of
them can be used as distinct singleton witnesses for the `cr` rank-`r`
targets.  Therefore:

* at most `min(nr,cr)` singleton cells of rank `r` can belong to a chosen
  distinct lower-target witness family;
* at most

  ```text
  sum_r min(nr,cr) = N-F                            (2.1)
  ```

  singleton cells can be useful by count;
* their total OR-rank is at most

  ```text
  sum_r r*min(nr,cr) = S-E.                         (2.2)
  ```

No assumption is made about which target receives which singleton.  These
are upper bounds on every distinct assignment.

The complete lower ideal has

```text
sum_(r=1)^4 cr   = 561,
sum_(r=1)^4 r*cr = 1936.                            (2.3)
```

## 3. The short-cell count cut

Assume the lower witnesses are singleton/pair witnesses.

In Type I there are `N-1` internal pair cells.  The `y1` selected rank-five
pair witnesses consume distinct cells, unavailable to lower targets.  By
(1.1), the number of pair cells left for lower targets is at most

```text
(N-1)-y1=1+y2.                                     (3.1)
```

Together with (2.1), coverage of all 561 lower targets gives

```text
561 <= N-F+1+y2.
```

Substituting `N=464-z` proves

```text
y2>=96+z+F.                                        (3.2)
```

In either tight Type-II case there are `N-s` internal pair cells over the
low components.  Equations (1.2)--(1.3) give

```text
(N-s)-y1
 =465-n5-s-(462-n5+delta-y2)
 =3-s-delta+y2
 =1+y2.                                            (3.3)
```

Thus `561<=N-F+1+y2`, now with `N=465-n5`, proves

```text
y2>=95+n5+F.                                       (3.4)
```

This argument does not apply to the no-duplicate/one-component Type-II case,
where a lower target may require a triple.

## 4. The weighted pair-cell cut

Again assume the lower witnesses are singleton/pair witnesses.  In a path
component `C=(A1,...,At)` of rank sum `SC`,

```text
sum_(i=1)^(t-1) |Ai union A(i+1)|
 <= 2*SC-|A1|-|At|
 <= 2*SC-2.                                        (4.1)
```

The formula remains valid at `t=1`, where the two endpoint terms refer to
the same entry and both sides are zero.  Summing over `s` components gives
pair-cell OR-rank capacity at most

```text
2*S-2*s.                                           (4.2)
```

Choose one short witness for each lower target and retain the `y1` selected
rank-five pair witnesses.  All cells are distinct.  Their required total
OR-rank is `1936+5*y1`.  Their singleton part has capacity at most `S-E` by
(2.2), while their pair part has capacity at most (4.2).  Hence

```text
1936+5*y1 <= 3*S-E-2*s.                            (4.3)
```

For Type I, `s=1`, giving `(T1-H1)`.  For the two tight Type-II cases this
is exactly `(T2-H1)`.  Notice that this also supplies the previously absent
two-component aggregate correction `3*S-5*y1>=1940` when `E=0`.

## 5. The weighted pair/triple-cell cut

Now allow lower witnesses of lengths one, two, or three.  For one component,
the total rank capacity of all internal pair and triple cells is at most

```text
5*SC-B(C),                                          (5.1)
```

where

```text
B(C)>=5  when |C|=1,
B(C)>=8  when |C|>=2.                               (5.2)
```

This follows by replacing each union rank by the sum of its entry ranks.
The entry coefficients in the pair-plus-triple family are:

```text
length 1:  0,
length 2:  1,1,
length 3:  2,3,2,
length>=4: 2,4,5,...,5,4,2.
```

Relative to coefficient five, positive entry ranks give the deficits in
(5.2).  Thus a single nontrivial core has boundary defect at least eight.
Two components of slack one and two have lengths at least one and two, so
their combined defect is at least `5+8=13`.

Select all lower witnesses and all `q` selected nonliteral rank-five
witnesses.  They are distinct singleton/pair/triple cells.  The lower
targets require total OR-rank 1936; the rank-five targets require `5*q`.
Using (2.2), (5.1), and (5.2) gives

```text
1936+5*q <= 6*S-E-8                         (one component),
1936+5*q <= 6*S-E-13                        (two components). (5.3)
```

For Type I, `q=462-z`, and the first row of (5.3) is exactly

```text
6*S-E+5*z>=4254.                                    (5.4)
```

For Type II, substitute `q=462-n5+delta`.  If `two` is the exact
two-component flag, (5.3) becomes

```text
6*S-E+5*n5 >= 4254+5*(delta+two).                   (5.5)
```

The three corrected alternatives make `delta` and `two` mutually exclusive,
and `delta+two=tight`.  This proves `(T2-H2)` in all cases.

## 6. Exact relation to the previous aggregate rows

Dropping the nonnegative `F,E` terms gives the already proved rows:

```text
Type I:
  y2>=96+z,
  3*S-5*y1>=1938,
  6*S+5*z>=4254;

Type II tight:
  y2>=95+n5,
  3*S-5*y1>=1936+2*s;

Type II all cases:
  6*S+5*n5>=4254+5*tight.
```

The Type-I first row is the named-cell width row.  The next two are `(I2)`
and `(I3)`.  The last Type-II row is `(II3)`.

A particularly cheap partial strengthening uses only the forced fact
`n1>=11`: each of the eleven singleton targets needs a literal singleton
entry, and all such entries lie in the low core.  Since `E>=n1-11`, Type I
satisfies

```text
3*S-n1-5*y1>=1927,                                 (6.1)
6*S-n1+5*z>=4243.                                  (6.2)
```

These dominate `(I2)--(I3)` and are strict whenever a singleton value is
repeated.  The full `E` rows also charge surplus rank-two, rank-three, and
rank-four entries.

## 7. Arithmetic separation from the old aggregate ledger

The following are integer rank/endpoint profiles, not OR words.  They show
that the three surplus rows are not algebraic consequences of the old
aggregate rows or of one another.  In all three examples use the rank-six
profile

```text
x=(x0,x1,x2,x3)=(1,0,0,461),                       (7.1)
```

and rank-five maximal chain A.

### 7.1 `(T1-H0)` only

```text
(h1,...,h6)=(0,0,48,48,96,462),
(z,y1,y2)=(0,366,96),
(n1,n2,n3,n4)=(114,0,0,350).
```

Here

```text
N=464, S=1514, F=123, E=183,
3*S-5*y1=2712,
6*S+5*z=9084.
```

Both weighted surplus rows hold, but `(T1-H0)` requires `y2>=219` and
fails by 123.

### 7.2 `(T1-H1)` only

```text
(h1,...,h6)=(0,0,451,451,451,459),
(z,y1,y2)=(3,8,451),
(n1,n2,n3,n4)=(264,102,76,19).
```

Here

```text
N=461, S=772, F=300, E=347,
3*S-5*y1=2276,
6*S+5*z=4647.
```

The count-surplus and three-cell-surplus rows hold, but

```text
3*S-E-5*y1=1929<1938.
```

### 7.3 `(T1-H2)` only

```text
(h1,...,h6)=(0,0,459,459,459,459),
(z,y1,y2)=(3,0,459),
(n1,n2,n3,n4)=(309,53,63,36).
```

Here

```text
N=461, S=748, F=298, E=298,
3*S-5*y1=2244,
6*S+5*z=4503.
```

The first two surplus rows hold, but

```text
6*S-E+5*z=4205<4254.
```

All three profiles satisfy:

* `S>=649`, `(I2)`, and `(I3)`;
* `n1+2*n2>=110`;
* the Type-I core length/count identity and `z<=133`;
* the named-cell base row `y2>=96+z`;
* the current central fan, cumulative nesting, short-pool, total-width, and
  branch-one profile rows with (7.1);
* both scalar local-density PB rows (their five-/six-set left sides are,
  respectively, `26390/36079`, `66272/84054`, and `71361/88849`).

This is separation from the displayed scalar projection, not a claim that
the profiles extend to the full interval-OR CNF.

## 8. Compact PB/CNF realization

The cuts reuse the exact rank counts `n1,...,n4`, the proposed shared `S`
bank, the rank-five boundary counts, and the already materialized Type-II
`s,n5,tight` flags.

There are two small implementations.

### 8.1 Shared surplus bank

For each of the four nine-bit counters, materialize

```text
er=max(nr-cr,0).
```

Four constant comparisons, four ordinary constant subtractors guarded by
their comparison bits, and two short addition trees give

```text
F=e1+e2+e3+e4,
E=e1+2*e2+3*e3+4*e4.
```

The three final PB comparisons are tiny relative to the multi-million
variable base formula.  All carries must be retained, and every comparison
must be guarded by the exact branch/subcase flag described above.

### 8.2 Fifteen subset rows, with no max gate

For `R subseteq {1,2,3,4}`, including the empty set,

```text
F=max_R sum_(r in R)(nr-cr),
E=max_R sum_(r in R)r*(nr-cr).                      (8.1)
```

Thus each surplus inequality is equivalently the conjunction of sixteen
ordinary linear PB comparisons obtained by replacing `F` or `E` with the
corresponding subset sum.  The empty-set row is exactly the corresponding
old base inequality, so only fifteen additional rows are needed when that
base row is retained.  This is useful for an independent inventory audit
because it avoids conditional subtraction/multiplexing entirely.  Shared
subset sums should be retained across all three families.

The recommended order is:

1. benchmark the nearly free `n1` projections (6.1)--(6.2);
2. add the exact `F,E` bank behind a new opt-in guard;
3. independently compare it with the fifteen-row construction on exhaustive
   small counters;
4. run build-only inventory and clause-stream audits before any solver run.

## 9. Independent arithmetic audit

The lightweight checker

```text
scratch/check_k11_histogram_surplus_cuts.py
```

exhausts the subset-max identities on `[0,7]^4`, checks all three corrected
Type-II branch constant rearrangements, and verifies every old/new row in the
three separating profiles.  It reports

```text
PASS
subset-max identities: exhaustive on [0,7]^4
Type-II branch constants: PASS
H0 S/F/E= (1514, 123, 183) profile= (0, 366, 96) n= (114, 0, 0, 350)
H1 S/F/E= (772, 300, 347) profile= (3, 8, 451) n= (264, 102, 76, 19)
H2 S/F/E= (748, 298, 298) profile= (3, 0, 459) n= (309, 53, 63, 36)
```

An independent theorem audit also confirmed the cell capacities, all Type-I
and Type-II constants, the exact `short_mode=tight` guard for `(H0)--(H1)`,
the all-Type-II scope of `(H2)`, and all three separating examples.  Its one
implementation warning is already reflected above: the subset-max
representation includes the empty subset, or equivalently retains the old
base row plus fifteen additional nonempty-subset rows.
