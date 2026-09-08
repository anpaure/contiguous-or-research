# Adversarial audit of the Type-II reverse pin-load theorem

## Verdict

**PASS, with one additional redundancy conclusion and a frozen compact
encoding design.**  The canonical witness choice, the touched-cell envelope,
the interaction of the 176 lower targets with the 210 rank-five targets, and
all four displayed inequalities in `K11_TYPE2_REVERSE_PIN_LOAD.md` are
correct.

The useful new projection is exactly

```text
b notin OR(C1) => o2(b)>=59,
b notin OR(C1) => 3*o2(b)+z+y2>=386.                  (0.1)
```

The note already identifies `n2+o2>=177` as redundant.  In fact the fourth
row

```text
n2+o2+z+y2>=387                                       (0.2)
```

is also redundant after the existing two-component eligibility row,
`y2>=95+z`, and (0.1) are retained.  This is not a correctness defect: all
four rows remain exact projections of the touched-cell theorem.  It means a
first production module should encode only (0.1).

No production source was edited by this audit.

## 1. Canonical witness dependence

The theorem is conditional on the same globally WLOG selected rank-five row
already used by the Type-II component encoding.  In the two-component branch:

1. all `z` literal rank-five entries have different values;
2. all of them are selected as singleton witnesses;
3. an exact-one selector chooses `C1`, every internal adjacent pair of which
   is forced into the selected rank-five row;
4. the other component is `C2`.

If `n_i=|C_i|` and `q_i` selected nonliteral rank-five witnesses lie in
`C_i`, then

```text
n1=q1+1,       n2=q2+2,       q1+q2=462-z.             (1.1)
```

The `n1-1` internal pairs of `C1` are distinct rank-five values.  No selected
rank-five interval of length three can lie in `C1`, because it would contain
one of those selected pairs; two nested equal-rank intervals must have the
same value, contradicting the one-target-per-slot selection.  A nonliteral
rank-five witness cannot cross a literal rank-five separator either.
Consequently every selected triple is in `C2`, and `y2` is a valid global
upper bound on the number of triples from any specified target subfamily.

This is an existential canonicalization, not a statement that every possible
witness choice gives the same component slacks.  It is sufficient for a SAT
cut because the existing Type-II schedule and slack-one selector encode this
very choice.  Given a genuine word, reselecting all literal singletons and all
`C1` pairs, then retaining arbitrary witnesses for the remaining targets,
produces the required schedule.

## 2. Why all relevant witnesses lie in `C2`

Fix `b notin OR(C1)`.

There are

```text
sum_(s=1)^4 C(10,s-1)=176                              (2.1)
```

nonempty rank-at-most-four masks containing `b`.  A lower witness cannot
contain a literal rank-five separator.  It also cannot lie in `C1`, whose
entries all omit `b`.  Therefore it lies in `C2`.

The local slack of `C2` is two: its `q2=n2-2` selected rank-five witnesses
fit in `n2` positions.  The ordered-antichain segment lemma consequently
places those witnesses in windows of length at most three and makes every
interval of length at least three contain one.  A rank-at-most-four witness
inside `C2` therefore has length at most two.  Hence the 176 lower targets
use 176 different singleton/adjacent-pair cells touched by `b`.

There are

```text
C(10,4)=210                                             (2.2)
```

rank-five masks containing `b`.  Let `z_b` be the number occurring as
literal separators.  The other `210-z_b` targets are nonliteral.  They cannot
be represented in `C1` or across a separator, so their selected witnesses are
in `C2`.  At most `y2` of them are triples.  Every remaining target therefore
uses a distinct adjacent pair touched by `b`.

The lower cells and rank-five pair cells are mutually distinct: one physical
interval has one OR value, and the two families have different target ranks.
Thus

```text
G2(n2,o2(b)) >= 176 + max(0,210-z_b-y2).               (2.3)
```

Since `z_b<=z`, (2.3) implies

```text
G2(n2,o2(b)) >= max(176,386-z-y2).                     (2.4)
```

Using global `z,y2` loses information but is safe.  A future, larger module
could count `z_b` and the coordinate-specific triple population instead.

## 3. Exact touched-cell envelope

For a path of length `n` with `o` marked vertices, the touched singleton and
edge cells number

```text
o + (# path edges incident with a marked vertex).
```

The edge term is at most both `2o` and `n-1`.  If `2o<=n-1`, separated
internal marked vertices attain `2o`; otherwise a path vertex cover of size
at most `o` touches all `n-1` edges.  Therefore

```text
G2(n,o)=o+min(n-1,2o)=min(3o,n+o-1).                  (3.1)
```

Combining (2.4) and (3.1) says that both arguments of the left minimum exceed
both arguments of the right maximum.  This is exactly the quartet

```text
3o2>=176,
n2+o2>=177,
3o2+z+y2>=386,
n2+o2+z+y2>=387.                                      (3.2)
```

There is no missing endpoint correction: `n2-1` is precisely the number of
internal adjacent pairs of the contiguous component.

The supplied checker exhausts the envelope through path length 14 and checks
the algebraic equivalence of (2.4) and (3.2) over the full real parameter
ranges.  It passes.  The finite exhaustion is a regression check; the proof
above establishes arbitrary `n`.

## 4. Redundancy of the two `n2+o2` rows

If `C1` omits `b`, its `q1` selected rank-five values avoid `b`.  Hence

```text
q1<=C(10,5)=252,
n2=q2+2>=212-z.                                        (4.1)
```

The already audited named-cell capacity gives

```text
q2>=95+z,
n2>=97+z.                                              (4.2)
```

Thus `n2>=max(212-z,97+z)>=155`; together with `o2>=59`, this proves
`n2+o2>=214`, so the second row of (3.2) is redundant with margin 37.

The fourth row is redundant as well once the current selected-width row

```text
y2>=95+z                                               (4.3)
```

and the two useful rows (0.1) are present.  For `z<=57`, put `s=z+y2`.
Then `s>=95+2z`, `n2>=212-z`, and

```text
o2>=ceil((386-s)/3).
```

The function `s+ceil((386-s)/3)` is nondecreasing, so

```text
n2+o2+s
 >= 307+z+ceil((291-2z)/3)
 >= 405.                                               (4.4)
```

For `z>=58`, equations (4.2)--(4.3) and `o2>=59` give

```text
n2+o2+s >= (97+z)+59+(95+2z)=251+3z>=425.             (4.5)
```

Therefore (0.2) is never the active new propagation target once the current
named-cell width row is enabled.  Without (4.3), all four rows remain the
exact touched-envelope projection and the full quartet encoding below is
available.

## 5. Strictness and exact rank-five accounting

The note's profile is internally consistent at the rank-five/component
level:

```text
z=1,
(q1,q2)=(252,209),
(n1,n2)=(253,211),
y=(1,364,97).
```

All 252 targets avoiding `b` can occupy the `C1` adjacent pairs.  The 210
targets containing `b` split exactly into

```text
one literal singleton + 112 C2 pairs + 97 C2 triples.  (5.1)
```

Indeed `364-252=112` and `112+97=q2=209`.  With only `o2=59` occurrences,

```text
G2(211,59)=177,
176+112=288,                                           (5.2)
```

so the exact touched demand fails even though all old component, selected
width, rank-seven width, entry-rank, and six-subcube marginals pass.  This
proves strictness of the joint row.  Taking `o2=58` also violates the lower
family row.

For independence between the two useful new rows, one may instead take

```text
z=1, (q1,q2)=(250,211), (n1,n2)=(251,213),
y=(1,250,211), x=(0,4,249,209).
```

Then `3*58+z+y2=386`, so the joint row holds at `o2=58`, while `o2>=59`
fails.  These are relaxation certificates, not proposed OR arrays.

## 6. Compact exact SAT design

The recommended module should require the existing Type-II two-component
pin-localization and named-cell guards.  Reuse:

* `slack_one_membership[465]` and `slack_two_membership[465]`;
* `slack_two_has[11]`;
* the 5,115 already allocated exact occurrence gates
  `slack_two_membership[i] AND A[i,b]`;
* the exact `z=n5` counter and rank-five state row.

The existing occurrence gates are currently local temporaries.  Retaining
them as a field changes no variable or clause count.

Add the following.

1. Build the exact eleven `C1` coordinate-OR bits.  Each bit uses 465 exact
   occurrence gates, their implications to one `has` flag, and one reverse
   OR clause: `5,126 variables / 20,471 clauses`.
2. Count the retained 465 `C2` occurrence gates separately for each
   coordinate.  Eleven exact Wallace/ripple counters use
   `10,142 / 70,994`.
3. For each of the 462 rank-five slots, define an exact flag for state `02`
   or `13`, then count these flags to materialize `y2`.  This uses
   `1,374 / 7,770`.
4. For each coordinate, exactly sum `3o2+z+y2`.  A weighted Wallace count
   uses 29 full adders, hence `638 / 4,466` over eleven coordinates.
5. Guard the comparisons `o2>=59` and `3o2+z+y2>=386` by
   `two_components AND !C1_has[b]`.  Direct first-difference comparisons use
   `88` clauses and no variables.

The exact recommended incremental inventory is therefore

```text
17,280 variables / 103,789 clauses.                    (6.1)
```

All substantive clauses contain the two-component escape; outside that
branch the exact component memberships and occurrence counts are zero.

If the existing `C2` occurrence gates are not retained, rebuilding them adds
`5,115 / 15,345`, giving `22,395 / 119,134`.  Retention is therefore the
natural compact implementation.

### Full quartet variant

To encode all four rows of (3.2), additionally:

* count `n2=sum_i slack_two_membership[i]`: `922 / 6,454`;
* form eleven exact `n2+o2` sums and compare to 177:
  `198 / (1,386+44)`;
* form eleven exact `n2+o2+z+y2` sums and compare to 387:
  `594 / (4,158+44)`.

This gives the exact full-envelope inventory

```text
18,994 variables / 115,875 clauses.                    (6.2)
```

The smaller (6.1) is recommended because the omitted rows are proved
redundant in Section 4.

## 7. Independent checks and scope

The original checker

```text
python3 scratch/check_k11_type2_reverse_pin_load.py
```

passes.  It verifies the touched envelope, constants, four-row equivalence,
the second-row redundancy, and the principal strictness profile.  The audit
supplement

```text
python3 scratch/audit_k11_type2_reverse_pin_load.py
```

additionally checks canonical target accounting, fourth-row redundancy,
independence of the two useful rows, and both exact circuit inventories.

The theorem applies only to the two-component Type-II subcase and proves no
SAT/UNSAT result or changed bound for `nu(11)`.
