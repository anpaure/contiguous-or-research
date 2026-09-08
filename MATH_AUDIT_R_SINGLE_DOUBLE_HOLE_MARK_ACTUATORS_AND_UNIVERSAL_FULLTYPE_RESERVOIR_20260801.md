# Audit of the single/double-hole marked actuators and a universal full-type reservoir

Date: 2026-08-01  
Lane: R / age-composition marked regrouping  
Status: independent symbolic audit, one finite-scope correction, and a new
exact age-quotient reservoir lemma.  Nothing here supplies a one-copy
protected Catalan embedding.

## 1. Verdict

The algebraic actuator theorems in handoff items `2498MR` and `2500DH` are
valid:

1. every displayed vector is a composition of `r` with positive fresh class;
2. every displayed directed edge satisfies the literal age inequality
   `c'_(i+1)<=c_i`;
3. the advertised profiles are exactly the positive suffix-deficit sets of
   their types;
4. the two-row exchanges preserve every marked-deficit multiplicity; and
5. equal mass on the displayed closed walks is a stationary type measure.

There is one important correction to the finite uniqueness statements.  The
97-case `k=76` and 101-case `k=89` programs construct the unchanged law with
`zero_type(profile,r,d)`.  Consequently they prove uniqueness **inside the
canonical leading-zero completion face**.  They do not quantify over all
possible completions or type-splittings of every unchanged underfull profile.
The successful swaps and their explicit cycles remain exact.  The word
“unique” should retain this completion-face qualifier unless a separate
option-flow enumeration is supplied.

The audit also gives a general pattern beyond two holes.  Every positive age
type lies on an explicit directed cycle of length `d+1` through the all-one
positive-age hub.  Hence any marked profile, including a terminal profile
with arbitrarily many holes, has an exact stationary packet using one marked
occurrence and `d` recyclable unmarked reservoir occurrences.  This closes
the age-quotient algebra under a strong stock hypothesis, but it does not
remove the physical problem: the standard labelled lift of such a cycle is
inside one fixed owner and therefore repeats that owner.

## 2. Audit of the uniform double-hole identities

Fix

```text
d>=3, r>=d+4, 1<=m<=d-1,
j=d-m+1, L=r-d-1.
```

The old and new profiles are

```text
A =({1,...,d+1}\{m,d}) union {r-1},
H ={1,...,d-2,d,d+2},
A'=({1,...,d}\{m}) union {r-1},
H'={1,...,d-2,d+1,d+2}.
```

Each has exactly `d` distinct marks.  The bound `r>=d+4` guarantees that
`d+2<r-1`, so no displayed union has an accidental collision.  Exchanging
`d+1` and `d` changes the two row-mark incidences

```text
(A,d+1),(H,d)  to  (A',d),(H',d+1),
```

and therefore preserves the complete marked-deficit multiplicity vector.
Under the rank convention `s=r-t`, it equivalently preserves every marked
rank multiplicity.

For a full profile `t_1<...<t_d`, the forced type is

```text
c_d=t_1,
c_(d-i)=t_(i+1)-t_i  (1<=i<d),
c_0=r-t_d.
```

Applying this identity gives exactly

```text
X_0=1, X_1=L, X_j=2, X_i=1 otherwise,
Y=(L-1,1,3,1,...,1).
```

For `1<=p<=j-1`, let `R_p` have fresh class `L`, all positive-age
coordinates one, and coordinate `p` raised to two.  Its suffix deficits are

```text
K_p={1,...,d+1}\{d-p+1}.
```

Indeed, the cumulative sums are `1,...,d-p`, then jump by two and continue
through `d+1`.

### Proposition 2.1 (edge audit)

The closed walk

```text
X -> Y -> R_1 -> ... -> R_(j-1) -> X
```

is legal and has `j+1<=d+1` vertices.

### Proof

For `X->Y`, the only nonunit inequality is `Y_2=3<=X_1=L`.
For `Y->R_1`, it is `(R_1)_1=2<=Y_0=L-1`.  Both hold because `L>=3`.
On `R_p->R_(p+1)`, the unique two in the target is bounded with equality by
the source two one coordinate to its left.  Finally

```text
X_1=L=(R_(j-1))_0,
X_j=2=(R_(j-1))_(j-1),
```

and all remaining target positive-age coordinates are one.  This checks all
`d` transition inequalities.  The coordinate sums are `r`; the fresh
classes are `1`, `L-1`, or `L`, hence positive.  QED.

Thus Theorem 3.1 of the double-hole note is correct with its stated
decomposition hypothesis

```text
pi=sigma+a(e_X+e_Y+sum_p e_(R_p)).
```

That hypothesis is substantive: numerical presence of the types is not by
itself a proof that their removal leaves a stationary residual.

The phrase “the full double-hole family” means precisely this normalized
terminal family, with holes `{m,d}` in `{1,...,d+1}`.  It is not a theorem
for an arbitrary pair of missing positions in an arbitrarily longer small
deficit interval.

## 3. Audit of the `d=5` seven-cycle

For `d=5`, after the `6<->5` exchange the two forced types are

```text
X=(1,r-6,1,1,1,2),
Y=(r-7,1,3,1,1,1).
```

The five displayed reservoir vectors all sum to `r`.  Their positive suffix
profiles are, respectively,

```text
{1,2,3,4,7},
{1,2,3,4,6},
{1,2,3,5,8},
{1,2,4,5,9},
{2,3,4,6};
```

the last vector has one retained zero cumulative suffix, which is not a
positive mark.

The only sharp lower-bound check in the seven-cycle is

```text
4 <= r-8
```

on the edge

```text
(r-8,3,2,1,1,1) -> (r-9,4,1,2,1,1).
```

Thus `r>=12` is exactly sufficient for the displayed parametric proof.  A
direct coordinate check verifies the other six edges.

At `k=76`, the raw transcript gives a complete circulation of the modified
law.  The seven cycle edges each carry at least 76 units.  Subtracting 76
units on those edges leaves a nonnegative circulation of mass

```text
6892620648693261354600 - 7*76
 = 6892620648693261354068.
```

This independently explains the residual-stationarity claim; it is not just
a scalar max-flow status.  The five reservoir node counts in the transcript
are all strictly greater than 76.

## 4. Exact scope of the finite minimality statements

The absolute combinatorial lower bound is valid.  A nontrivial regrouping
that preserves every mark count cannot alter only one row.  With two rows,
the least possible nonzero incidence change removes one mark from each row
and installs the two marks crosswise.  The `6<->5` exchange attains this
two-row/four-incidence symmetric-difference bound.

The stronger uniqueness statement has narrower scope.  In

```text
scratch/search_systematic_k76_two_row_mark_swap_20260801.cpp
```

the line constructing `base` applies `zero_type` to every profile, and every
trial modifies that fixed histogram.  The same convention is used in the
range probe underlying the `k=89` result.  Therefore the exact conclusions
are:

* among the 97 eligible `k=76` two-row one-mark transpositions, exactly one
  makes the canonical leading-zero type histogram stationary;
* among the 101 eligible `k=89` transpositions, exactly one does so;
* the successful swaps are the instances stated in items `2498MR/2500DH`.

They do **not** prove that every other swap fails after arbitrary completion
and splitting of unchanged underfull profile mass.  This does not affect the
completion-independent *pre-swap* `k=76` obstruction, nor either symbolic
actuator theorem.

At `k=76` the only underfull systematic profile is `{2,3,4,6}`, a subset of
the bad profile, so it supplies no genuine crosswise mark value.  This makes
the donor list complete, but it does not make that row's post-swap completion
canonical.  A global uniqueness claim would still need the corresponding
option-flow quantifier.

## 5. A universal full-positive age cycle

The following exact lemma is the clean pattern toward three or more holes.

### Theorem 5.1 (universal full-type reset cycle)

Let `r>=d+1`, and let

```text
c=(c_0,...,c_d),  c_i>=1,  sum_i c_i=r.
```

Put

```text
D=(r-d,1,...,1).
```

For `0<=t<=d`, define `V_t(c)` by

```text
(V_t)_i = c_(d-t+i)  for 1<=i<=t,
(V_t)_i = 1          for t<i<=d,
(V_t)_0 = r-sum_(i=d-t+1)^d c_i-(d-t).
```

Then `V_0=D`, `V_d=c`, every coordinate of every `V_t` is positive, and

```text
D=V_0 -> V_1 -> ... -> V_d=c -> D                 (5.1)
```

is a legal age closed walk of length `d+1`.

### Proof

Using `sum_i c_i=r`,

```text
(V_t)_0=c_0+sum_(i=1)^(d-t)(c_i-1)>=1.
```

For `V_(t-1)->V_t`, coordinates `2,...,t` are exact shifts of the launched
tail coordinates, and coordinates `t+1,...,d` are ones bounded by source
ones.  The only remaining inequality is the new first positive-age entry:

```text
(V_t)_1=c_(d-t+1)
 <= c_0+sum_(i=1)^(d-t+1)(c_i-1)
 =(V_(t-1))_0.
```

After subtracting `c_(d-t+1)`, the left-over difference is

```text
c_0-1+sum_(i=1)^(d-t)(c_i-1)>=0.
```

Finally `D_(i+1)=1<=c_i` for `0<=i<d`, so `c->D` is legal.  QED.

Every `V_t` has exactly `d` distinct positive suffix deficits.  Explicitly,

```text
K_t(c)={1,...,d-t}
       union {d-t+sum_(i=u)^d c_i : d-t+1<=u<=d}.  (5.2)
```

The two parts in (5.2) are strictly ordered, so these are genuine full
profiles.

### Corollary 5.2 (strong-stock marked packet)

Let `A` be any marked deficit profile with `|A|<=d`.  Extend it to a
`d`-subset `S` of `{1,...,r-1}` and let `c(S)` be the positive type forced by
`S`.  On the closed walk (5.1), mark the occurrence `c(S)` by `A` and leave
the other `d` occurrences unmarked.  The result is a stationary marked
packet of `d+1` occurrences whose complete marked marginal is exactly one
copy of `A`.

Consequently a bank of `M` arbitrary exceptional profiles can be absorbed at
the age-quotient level whenever `dM` recyclable unmarked reservoir
occurrences are supplied.  Terminal profiles with three or more holes create
no additional algebraic obstruction under this stock hypothesis.

### Corollary 5.3 (arbitrary count-neutral regrouping)

Suppose two old full profiles are exchanged count-neutrally into two new full
profiles.  If the host supplies two reset-cycle packets before and after the
exchange, with all nondistinguished vertices unmarked, replacing the old two
packets by the new two packets preserves:

* the number `2(d+1)` of occurrences;
* every marked-deficit marginal; and
* stationarity of the age-type law.

This is independent of the number and locations of holes in the four central
profiles.

## 6. Why Theorem 5.1 is not yet the requested protected stock theorem

The universal packet deliberately exposes the missing quantifier rather than
hiding it.

1. It uses `d` unmarked reservoir occurrences per marked task occurrence.
   A block of multiplicity `a` therefore consumes `ad` reservoir
   occurrences, even though it uses only `O(d)` parametric type schemas.
2. In a near-saturated triangular marked law, the existence of this many
   rows which may be left unmarked is not automatic.
3. The standard literal lift of one age cycle keeps the owner `T` fixed.
   Hence its `d+1` windows repeat the same middle owner and are not an exact
   one-copy Catalan factor.
4. Choosing distinct owners for the vertices independently does not repair
   this: the fixed-owner partition lift supplies the age edge, whereas an
   owner-moving edge needs an additional protected Catalan braid.
5. Nothing in the age state records upper witnesses, common-cap addresses,
   residence collars, or component-splice ports.

Thus the exact remaining physical theorem can be stated sharply:

> Construct an owner-moving realization of the reset cycles (5.1), or of a
> denser multiplexing of them, in which the `ad` reservoir roles are carried
> by existing protected Catalan occurrences, all owners remain one-copy,
> and upper/common-cap/residence tickets survive.  Equivalently, prove that
> the protected host contains a cycle-stock factor for the required marked
> packet multiset, not merely the separate fixed-owner age cycles.

This is the point at which a genuine bounded reservoir-stock theorem is
needed.  The single- and double-hole notes correctly do not claim it.

## 7. Independent audit of the arbitrary-hole two-cycle schema

The universal reset cycle above uses unmarked reservoirs.  A sharper proposed
construction keeps every central row full and compresses all donor changes
into one sweep.  Its algebra is also valid.

Fix an integer `h>=1` and put

```text
B=d+h-1<=r-2.
```

Let `H` be an `h`-subset of `[B-1]`, and consider the full terminal profile

```text
A=([B]\H) union {r-1}.                           (7.1)
```

Set

```text
L=H intersect [d],
U=[d+1,B]\H.
```

Since `[d+1,B]` has `h-1` elements and `B` is not in `H`, direct counting
gives

```text
|U|=|L|-1.                                       (7.2)
```

In particular `L` is nonempty.  Choose a residual hole `m` as follows: if
`d` lies in `L`, take `m=d`; otherwise take any `m` in `L`.  Bijection-pair
the elements `a` of `L\{m}` with the elements `u` of `U`.  For each pair,
exchange `u` from row `A` with `a` from a donor row `[d]`.  All exchanges are
collision-free.  Collectively they produce

```text
X-profile = ([d]\{m}) union {r-1},
Y_(a,u)-profile = ([d]\{a}) union {u}.           (7.3)
```

Equation (7.3) proves exact count neutrality rank by rank.

Put `M=r-d`.  Use

```text
D=(M,1,...,1),
R_p=(M-1,1,...,1), with coordinate p raised to2.
```

Because of the choice of `m`, every exchanged `a` satisfies `a<=d-1`.
Writing

```text
p=d-a+1,
```

we have `2<=p<=d`, and the type forced by the second profile in (7.3) is

```text
Y_(a,u)=(r-u,u-d,1,...,1), with coordinate p raised to2.  (7.4)
```

There is no double assignment at coordinate one; excluding `a=d` is
essential for the literal formula (7.4).

### Proposition 7.1 (individual donor and terminal cycles)

For every pair `(a,u)`,

```text
D -> R_1 -> ... -> R_(p-1) -> Y_(a,u) -> D       (7.5)
```

is a legal age cycle.  The `X` type has the usual single-hole cycle

```text
X -> D -> R_1 -> ... -> R_(j-1) -> X,
j=d-m+1,                                         (7.6)
```

when `m<d`; when `m=d`, (7.6) reduces to the two-cycle `X<->D`.

### Proof

The only nonunit entry entering `Y_(a,u)` from `R_(p-1)` is its first
positive-age coordinate:

```text
u-d <= r-d-1=M-1,
```

because `u<=B<=r-2`.  Its age-`p` two is supplied with equality by the
age-`p-1` two of `R_(p-1)`.  All coordinates of `Y_(a,u)` are positive, so
`Y_(a,u)->D` is automatic.  The proof of (7.6) is the same right-moving-two
check as Proposition 2.1; for `m=d`, the forced `X` has
`X=(1,M,1,...,1)`, which gives both directions with `D`.  QED.

Thus arbitrary `h` is already covered by `O(d)` **distinct parametric
types**, although using (7.5) separately may require quadratic reservoir
multiplicity.

### Proposition 7.2 (compressed donor sweep)

Index positions by `p=1,...,d`.  Put `S_p=Y_(a,u)` when the pair assigned to
`a=d-p+1` exists, and put `S_p=R_p` otherwise.  Then `S_1=R_1`, and

```text
D -> S_1 -> S_2 -> ... -> S_d -> D              (7.7)
```

is legal if and only if every two consecutive `Y` positions, carrying high
labels `u,v`, satisfy

```text
u+v<=r+d.                                        (7.8)
```

### Proof

There is no `Y` at position one because `a=d` is either absent from `L` or
is the chosen residual hole.  Hence the first edge is `D->R_1`.  Across a
general edge `S_p->S_(p+1)`, the age-two token shifts with equality from
coordinate `p` to `p+1`.  All unit coordinates are automatic.  If the target
is a `Y` with label `v`, its first positive-age entry imposes

```text
v-d <= (S_p)_0.
```

For `S_p=R_p` this follows from `v<=r-2`.  For a source `Y` labelled `u`, it
is precisely `v-d<=r-u`, which is (7.8).  Finally `S_d->D` is automatic
because the target positive-age entries are all one.  This proves both
necessity and sufficiency.  QED.

Since adjacent labels are distinct elements of `U`,

```text
u+v<=B+(B-1)=2d+2h-3.
```

Therefore the uniform inequality

```text
r>=d+2h-3                                       (7.9)
```

implies (7.8) for every bijection and every adjacency.  Under (7.9), one
terminal cycle (7.6) plus the donor sweep (7.7) contains all modified rows
and uses only `O(d)` occurrence roles, not merely `O(d)` distinct types.
The proposed bound `r>=d+2h-2` is also sufficient, but is one unit weaker
than this distinct-label estimate.

The conclusion is again conditional on a stationary-residual decomposition
and on physical stock.  In particular, (7.7) is not by itself an
owner-simple Catalan path: its direct partition lift remains in one owner.

## 8. Corrected implication ledger

Proved unconditionally:

* the `d=5`, `r>=12` seven-cycle identity;
* the normalized all-depth double-hole cycle;
* the arbitrary-hole individual cycles (7.5)--(7.6);
* the compressed arbitrary-hole sweep under the exact adjacent-label
  criterion (7.8), in particular under (7.9);
* exact mark neutrality of both exchanges;
* the universal full-positive reset cycle (5.1);
* the strong-stock quotient absorption of arbitrary hole patterns.

Proved in a finite fixed-completion face:

* uniqueness among 97 `k=76` and 101 `k=89` minimum transpositions.

Still open:

* uniqueness under arbitrary completion/type splitting;
* bounded-density reservoir stock in the actual triangular law;
* an owner-moving one-copy lift of the packets;
* protected upper/residence/common-cap compatibility;
* any consequence for `nu(k)`.
