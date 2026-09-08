# Depth two: second-order Johnson walks and two exact integral projections

Date: 2026-08-01  
Status: unconditional exact normal form and two integral projection theorems.
At depth two, an owner-exact literal chronology is exactly a second-order
walk on the rank-`(m-1)` layer.  The named-lower/root-cap projection and the
named-lower/owner-injection projection both round integrally for every
`m`.  Their common selection, acyclicity, and the Catalan connector bank
remain open.  No all-dimensional one-copy theorem is claimed.

## 1. Literal depth-two chronology

Put

```text
n=2m+1,
L=C([n],m-1),       R=C([n],m),       O=C([n],m+1),
ell=|L|,            W=|R|=|O|.
```

A depth-two flag at a root `Q in R` is a pair

```text
(Q;a),       a in Q,
```

and it offers the lower target `S=Q-{a}`.  A literal turn from `(Q;a)` to
`(Q';a')` exists exactly when

```text
Q'=Q-{a}+{b}       for some b notin Q,
a' in Q-{a}.
```

Its owner is `Q union Q'`.

## 2. Second-order walk theorem

### Theorem 2.1

A connected owner-exact depth-two chronology is equivalent to a cyclic
word

```text
S_0,S_1,...,S_(W-1)       in L
```

such that, with indices modulo `W`,

```text
Q_i=S_(i-1) union S_i                         (2.1)
O_i=S_(i-1) union S_i union S_(i+1),          (2.2)
```

the following hold:

1. consecutive `S` values are distinct Johnson neighbours;
2. the `Q_i` are all distinct, hence enumerate `R`;
3. every `O_i` has rank `m+1`, and the `O_i` are all distinct, hence
   enumerate `O`.

Every named lower target is markable exactly once if and only if every
member of `L` occurs at least once in the cyclic word.

### Proof

Start with a literal chronology.  At root `Q_i`, let `a_i` be its deletion
and put

```text
S_i=Q_i-{a_i}.
```

Write `Q_(i+1)=Q_i-{a_i}+{b_i}`.  Legality says
`a_(i+1) in S_i`, so

```text
S_(i+1)=S_i-{a_(i+1)}+{b_i}.
```

Thus consecutive lower values are Johnson neighbours.  Moreover

```text
Q_i=S_(i-1) union S_i,
```

because `a_i` is exactly the coordinate removed from `S_(i-1)` on the
step to `S_i`.  Taking the union of consecutive roots gives (2.2).
Root and owner exactness give items 2--3.

Conversely, from such a lower word define `Q_i` by (2.1), and let

```text
a_i=Q_i-S_i=S_(i-1)-S_i.
```

The step `Q_i -> Q_(i+1)` removes `a_i` and inserts the unique coordinate
of `S_(i+1)-S_i`.  The next deletion `a_(i+1)=S_i-S_(i+1)` lies in `S_i`,
so the literal depth-two transition law holds.  Equations (2.1)--(2.2)
give exact roots and owners.  Finally, marking is occurrence-local: one may
mark one occurrence of each lower value independently.  QED.

For a cycle cover rather than one connected chronology, Theorem 2.1 holds
componentwise, with the `W` root and owner values partitioned across the
cyclic words.

## 3. Exact Catalan seam ledger

The number of repeat occurrences in any lower-covering word is forced:

```text
Delta=W-ell
     =2W/(m+2)
     =Cat_(m+1).                                      (3.1)
```

Choose and mark one occurrence of every lower target in a connected word,
and delete its other `Delta` transition edges.  What remains is a spanning
linear forest on the root vertices:

* it has exactly one edge of each lower colour;
* it has `ell=W-Delta` edges;
* it has exactly `Delta` path components, including isolated vertices.

Conversely, suppose a spanning linear forest on `R` has one edge of each
lower colour, all its edge-owner colours are distinct, and its `Delta`
components can be cyclically joined by `Delta` further Johnson edges using
the unused owner colours, with the two incident lower edge-colours distinct
at every joined endpoint.  Orient the resulting cycle.  Theorem 2.1 gives
a connected owner-exact depth-two chronology covering every lower target.

Thus the exact depth-two object splits into

```text
lower-rainbow Catalan linear forest
        + Delta owner-injective connector edges.       (3.2)
```

The count in (3.1) is not an approximation: it is exactly the number of
seams/connectors available after one occurrence of every lower colour has
been retained.

## 4. First integral projection: exact lower colours and root cap two

For every `S in L`, its rank-`m` supersets form a set `N(S)` of size
`m+2`.  We seek two distinct members of `N(S)` and allow every root to be
used at most twice.

### Theorem 4.1 (two-incidence b-matching)

There is a simple incidence set `I subseteq L x R` such that

```text
deg_I(S)=2       for every S in L,
deg_I(Q)<=2      for every Q in R.                  (4.1)
```

Consequently, joining the two roots assigned to `S` gives a graph `F` on
`R` with one edge of every lower colour and maximum degree at most two.

### Proof

Use the bipartite containment graph `L--R`, with edge capacity one, demand
two at every left vertex, and capacity two at every right vertex.  The
standard capacitated Hall condition is

```text
2|X| <= sum_(Q in R) min(2,deg_X(Q))              (4.2)
```

for every `X subseteq L`.  A root contains exactly `m` lower facets, so
`0<=deg_X(Q)<=m` and

```text
min(2,deg_X(Q)) >= (2/m)deg_X(Q).
```

The incidence graph has left degree `m+2`; hence

```text
sum_Q min(2,deg_X(Q))
 >=(2/m)sum_Q deg_X(Q)
 =(2(m+2)/m)|X|
 >=2|X|.
```

Thus every cut passes.  Integral max flow gives (4.1), and edge capacity
one makes the two assigned roots distinct.  QED.

Orient every path and cycle of `F`.  Internal roots then have one incoming
and one outgoing marked transition.  If `n_1` is the number of degree-one
roots, the deficit identity

```text
2W-2ell=2Delta=2n_0+n_1
```

shows `n_1<=2Delta`.  Thus the exact named-lower row has an integral partial
literal flow whose entire state imbalance is confined to a Catalan-sized
endpoint bank.  The theorem does not make `F` acyclic or its owner colours
distinct.

## 5. Second integral projection: exact lower colours and owner injection

Make the distance-two containment graph between `L` and `O`, joining
`S` to `U` when `S subset U`.  Its degrees are

```text
deg_L=C(m+2,2),       deg_O=C(m+1,2).               (5.1)
```

### Theorem 5.1 (upper-owner SDR)

There is an injection

```text
phi:L -> O,          S subset phi(S).                (5.2)
```

For each `S`, the two middle facets of `phi(S)` containing `S` form a
Johnson edge of lower colour `S`.  These `ell` edges therefore use every
lower colour once and have pairwise distinct owner colours.

### Proof

For every `X subseteq L`, double count its incidences with its upper
neighbourhood:

```text
C(m+2,2)|X| <= C(m+1,2)|N(X)|.
```

Hence

```text
|N(X)| >= ((m+2)/m)|X| >= |X|.
```

Hall gives (5.2).  The two coordinates of `phi(S)-S` give the asserted
middle facets.  QED.

This theorem does not control middle-root degrees or topology.

## 6. The exact correlation left after the two projections

An ordered diamond is

```text
(S,U,T,H),
S in L, U in O, S subset T,H subset U,
T!=H.
```

Selecting one ordered diamond for every `S`, with `U`, `T`, and `H` all
injective, simultaneously strengthens Theorems 4.1 and 5.1.  Its directed
middle graph has maximum indegree and outdegree one; forbidding directed
cycles makes it the marked Catalan linear forest in (3.2).

The two projection proofs cannot simply be intersected:

* Theorem 4.1 is a bipartite b-matching on `L--R`.
* Theorem 5.1 is a different bipartite matching on `L--O`.
* One diamond column touches one owner and two middle resources.  The
  middle-capacity rows overlap rather than form a partition matroid.

The raw diamond matrix already contains the unsigned triangle minor

```text
[1 1 0]
[1 0 1]
[0 1 1]
```

of determinant two.  Thus neither max-flow proof implies a common integral
selection.  This is the first exact correlation not removed by Boolean
shadow expansion.

The second-order walk theorem shows why the correlation is load-bearing:
root degree two is literal state balance, owner injection is owner
one-copy, and acyclicity leaves exactly the `Delta=Cat_(m+1)` connector
slots.  Solving these three rows jointly is already the complete depth-two
one-copy core; deeper pull-clock rows can only add constraints.

## 7. Proof-safe consequence

At depth two, ordinary containment Hall is completely solved on both sides:

```text
named lower targets + cap-two roots: exact integral;
named lower targets + injective owners: exact integral.
```

Therefore a future one-copy rounding proof should not spend effort on
another marginal Hall estimate.  It must correlate the two exact
projections into a linear forest and then use the forced Catalan connector
bank.  This is a strictly smaller target than the full trace master, but it
is not implied by stationary pull-clock feasibility or by Birkhoff
rounding.
