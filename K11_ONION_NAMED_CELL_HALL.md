# Named-cell Hall localization in the `k=11` onion branches

## 1. Result

The rank-filtration architectures force a branch-specific restriction that is
not visible to any target-length blocker or nested scalar Hall inequality.
After literal active-rank entries are removed, every lower target must occur
in a **named physical cell** of a small diagonal band inside the resulting
low components.  The permitted band width is the component's own rank-witness
slack, not the global short-window bound.

For the two exact `k=11` branches this gives:

* **Type I.** Every mask of rank at most four is either one entry of the
  unique rank-at-most-four core or the OR of one adjacent pair inside that
  core.
* **Type II, two low components.** Every mask of rank at most four is either
  one low entry or the OR of an adjacent pair in the uniquely designated
  slack-two component.  No pair in the slack-one component can serve a lower
  target.
* **Type II, one low component with one duplicate rank-five occurrence.**
  Every mask of rank at most four is an entry or an adjacent-pair OR in that
  component.
* **Type II, one low component and no rank-five duplicate.** Every mask of
  rank at most four is the OR of a window of length at most three in that
  component.

The corresponding inequalities retain actual short-window OR ranks.  In the
two-component Type-II branch, if `z` is the number of literal rank-five
values and `E_4` is the number of internal adjacent pairs of the slack-two
component whose OR has rank at most four, then

```text
E_4 >= 96+z,                         (1.1)
length(slack-two component) >= 97+z. (1.2)
```

In Type I the analogous lower bound is `E_4>=97+z`.  These are necessary
conditions for a length-465 word; they do not prove existence or
nonexistence.

The cell rows also force new joint selected-endpoint width cuts.  If `y_2`
denotes the number of selected rank-five witnesses of physical length three
(width two), then

```text
Type I:                         y_2 >= 96+z,       (1.3)
Type II, two low components:   y_2 >= 95+z,       (1.4)
Type II, one component, delta=1:
                                y_2 >= 96+z.       (1.5)
```

For comparison, the previous joint scalar width row gives only
`y_2>=91+z` in Type I and `y_2>=87+z` in the two-component Type-II branch.

## 2. Named-cell confinement lemma

Let a segment `J` have length `q+t`, and suppose it contains selected
witnesses for `q` distinct rank-`r` masks.  Assume those witnesses are wholly
inside `J`.

### Lemma 2.1

Every interval `K subseteq J` of length at least `t+1` contains one of the
selected rank-`r` witnesses.  Consequently, if `|U(K)|<r`, then

```text
|K|<=t.                                             (2.1)
```

### Proof

Re-index `J` as `1,...,q+t`.  Order the selected intervals by left endpoint,

```text
I_i=[a_i,b_i],  a_1<...<a_q.
```

Equal-rank targets are incomparable, so no selected interval contains
another; hence `b_1<...<b_q`.  There are `q` distinct left endpoints and `q`
distinct right endpoints among `q+t` positions, giving

```text
i<=a_i,b_i<=i+t,
I_i subseteq [i,i+t].                              (2.2)
```

Write `K=[a,b]` and suppose `|K|>=t+1`.  Since `b<=q+t`, necessarily `a<=q`.
Also `b>=a+t`, so

```text
I_a subseteq [a,a+t] subseteq K.
```

The OR of `K` contains the selected rank-`r` value `U(I_a)`, proving (2.1).
The statement is vacuous and still valid when `q=0`.  ∎

This is stronger than the usual segment-capacity count.  It identifies every
physical cell that can still carry a lower target.

## 3. General component Hall law

Suppose literal rank-`r` entries are deleted from a word.  Let the remaining
rank-below-`r` components be `C_1,...,C_s`.  Write

```text
n_j=|C_j|,
q_j=# selected nonliteral rank-r witnesses assigned to C_j,
t_j=n_j-q_j.
```

Every target `S` of rank below `r` has a witness in one component: a witness
for `S` cannot contain a literal rank-`r` entry.  Lemma 2.1 says that its
witness in `C_j` has length at most `t_j`.

For `u<r`, define the named candidate family

```text
N_u(C_j,t_j)
  ={I subseteq C_j : 1<=|I|<=t_j and |U(I)|<=u}.
```

Distinct target masks require distinct physical intervals.  Therefore:

### Theorem 3.1 (named-cell Hall inequality)

For every `1<=u<r`,

```text
Lambda_u(k):=sum_(a=1)^u C(k,a)
   <= sum_(j=1)^s |N_u(C_j,t_j)|.                 (3.1)
```

More strongly, the actual OR values obey the family inclusion

```text
{S subseteq [k]:1<=|S|<=u}
  subseteq union_j {U(I):I in N_u(C_j,t_j)}.      (3.2)
```

Unlike a scalar containment cap, (3.1) remembers the component, both physical
endpoints, and the actual OR rank of every candidate cell.

## 4. Type I

Type I has one literal six-set at an endpoint.  Deleting it leaves the exact
rank-five equality word of length

```text
464=beta_5(11)=C(11,5)+2.
```

Let `z` be the number of literal rank-five entries in that suffix.  They are
distinct and occupy its two boundary blocks.  The unique low core `C` has

```text
|C|=464-z.
```

The other `462-z` five-sets have selected witnesses inside `C`, so its slack
is exactly

```text
t=|C|-(462-z)=2.                                  (4.1)
```

For `1<=u<=4`, let

```text
V_u=#{i in C:|A_i|<=u},
E_u=#{i,i+1 in C:|A_i union A_(i+1)|<=u}.
```

Theorem 3.1 becomes the branch-specific row

```text
Lambda_u(11)<=V_u+E_u.                            (4.2)
```

At `u=4`, every entry of `C` has rank at most four, so

```text
V_4=464-z,
Lambda_4(11)=11+55+165+330=561.
```

Hence

```text
E_4>=561-(464-z)=97+z.                            (4.3)
```

There are `|C|-1` adjacent-pair cells.  At least `E_4` of them have rank at
most four and therefore cannot be selected rank-five witnesses.  The core
contains

```text
q=462-z=|C|-2
```

selected nonliteral rank-five witnesses, all of physical length two or three.
If `y_2` is the number of length-three witnesses, then

```text
q-y_2 <= (|C|-1)-E_4,
y_2 >= E_4-1 >= 96+z.                             (4.4)
```

This couples a named physical-cell deficit to the left/right width profile of
the selected rank-five endpoint schedule.

The full set-valued consequence is that all 561 masks in ranks one through
four occur among the `464-z` entries and the adjacent-pair ORs of this one
named core.  No triple window can be their only witness.

## 5. Type II

Let

```text
h=# literal rank-five occurrences,
z=# distinct literal rank-five values,
delta=h-z.
```

After deleting all `h` literal positions, the low components contain
`462-z` selected nonliteral rank-five witnesses.  Their total slack is

```text
sum_j t_j=(465-h)-(462-z)=3-delta.                (5.1)
```

Rank-filtration stability gives `delta+s<=2`.  Since the lower ideal is
nonempty, the only possibilities are:

```text
(delta,s,component slacks)
  (0,1,{3}),
  (1,1,{2}),
  (0,2,{1,2}).                                   (5.2)
```

### 5.1 One component, no duplicate

Here the sole component has slack three.  Define `V_u,E_u,F_u` as the
numbers of its singleton, adjacent-pair, and consecutive-triple cells whose
OR rank is at most `u`.  Then

```text
Lambda_u(11)<=V_u+E_u+F_u,  1<=u<=4.             (5.3)
```

At `u=4`, `V_4=465-z`, so

```text
E_4+F_4>=96+z.                                   (5.4)
```

### 5.2 One component, one duplicate

Here the component has slack two and `h=z+1`.  Thus

```text
Lambda_u(11)<=V_u+E_u,                            (5.5)
E_4>=561-(464-z)=97+z.                            (5.6)
```

Exactly as in (4.4), its `462-z=|C|-2` selected nonliteral five-set witnesses
have length two or three.  Hence

```text
y_2>=E_4-1>=96+z.                                 (5.6a)
```

### 5.3 Two components

Here `delta=0`, the two slacks are `{1,2}`, and `h=z`.  Designate the
slack-one component `C^(1)` and the slack-two component `C^(2)`.  A lower
target in `C^(1)` must be a singleton; in `C^(2)` it is a singleton or an
adjacent-pair OR.  Therefore, writing `V_u` for all low singleton candidates
and `E_u^(2)` for the qualifying adjacent pairs internal to `C^(2)`,

```text
Lambda_u(11)<=V_u+E_u^(2).                        (5.7)
```

At rank four,

```text
V_4=465-z,
E_4^(2)>=96+z.                                    (5.8)
```

If `b=|C^(2)|`, then `E_4^(2)<=b-1`, so

```text
b>=97+z.                                          (5.9)
```

The slack-two component contains `b-2` selected rank-five witnesses.  At most
`b-1-E_4^(2)` of them can be adjacent pairs, so its number of selected triple
witnesses is at least

```text
(b-2)-(b-1-E_4^(2))=E_4^(2)-1>=95+z.             (5.10)
```

Every selected witness in the slack-one component is a pair, and every
literal selected witness is a singleton.  Thus the triples in (5.10) are
exactly contributions to the global rank-five width-two count `y_2`, proving
(1.4).

This is a direct restriction on the position of the unique component cut and
on the actual adjacent OR values.  The existing coordinate-transversal
theorem may independently designate either component as coordinate-complete;
(5.7) does not assume which one.

## 6. Why blocker/Hall cannot imply these rows

At `k=11,n=465`, every scalar endpoint-blocker hierarchy already passes.  Its
strongest central cap merely says that lower masks may use physical windows
of length at most three anywhere in the 465-position word.  It does not know
which positions are literal separators, which low component has slack one or
two, or the actual rank of a named short-window OR.

By contrast:

* Type I deletes every triple cell and every cell outside one specified core
  from the rank-at-most-four candidate pool;
* Type-II `{1,2}` deletes all nonsingleton cells of the slack-one component
  and all triple cells of the slack-two component;
* every surviving cell is counted only when its actual OR rank is at most
  the tested cutoff.

For a concrete separation, take the Type-I rank architecture with no literal
five-set and alternate two rank-four entries whose union has rank eight.  It
satisfies all purely numerical blocker/Hall rows at length 465, but has
`E_4=0` and violates (4.3).  Universality plus named joint endpoint geometry,
not a stronger scalar target-length cap, rules it out.

## 7. Search consequence

The inequalities can be encoded without target identities:

1. use the existing exact onion component flags;
2. materialize actual OR-rank-at-most-`u` flags for only the permitted pairs
   (and, in the slack-three subcase, triples);
3. impose (4.2), (5.3), (5.5), or (5.7) for `u=1,2,3,4`.

The stronger set-valued version (3.2) can replace direct lower-target witness
slots branchwise.  Either encoding retains the exact unrestricted problem
inside the chosen onion branch.
