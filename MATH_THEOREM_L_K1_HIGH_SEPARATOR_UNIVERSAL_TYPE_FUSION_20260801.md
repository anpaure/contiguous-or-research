# Lane L: the `K=1` high-separator class universally fuses the core-free rotor at type level

Date: 2026-08-01  
Status: exact unlabelled age-type theorem.  One complete copy of the
canonical long package `g_(0,r-2)` joins all raw necklaces of one complete
core-free package `g_(0,r-1)` into one legal successor cycle by serial
same-source-type switches.  This is not a one-copy labelled-owner theorem,
a named-target absorber, or a proof that the canonical Ferrers inventory
contains the required extra package.

## 0. Outcome and exact scope

Fix

```text
d >= 1,                 r >= d+3,
L=d+1.
```

The complete core-free long package has one occurrence for every positive
`L`-part composition of `r`.  Its raw successor rotates the parts.  Add
one complete copy of the nearest positive-core long package

```text
g_(0,r-2),              K=r-(r-2)-1=1.
```

The latter has one occurrence for every positive `L`-part composition of
`r-1`; its age type is obtained by adding one to the first part.  The
bipartite graph between the raw necklaces of the two packages, with an
edge when the two necklaces contain occurrences of the same age type, is
connected.  Along a spanning tree, swapping the outgoing heads of two
same-type occurrences serially merges all raw cycles.  Thus the union of
the two package occurrence multisets has a one-cycle legal **type-level**
successor permutation.

All occurrence-attached marks and role labels are untouched.  However,
same age type does not make two particular labelled age partitions have
the same live successor list.  Therefore the switch is not automatically
literal, and arc-attached q1/upper/provider payloads are not protected.
The missing lift is precisely a labelled cross-rectangle/owner--flag Hall
theorem together with its named-provider closure rows.

In particular, the deep-word obstruction for the two-buffer-only face
cannot be promoted to a no-go against an arbitrary single high-separator
class: `g_(0,r-2)` already destroys it at unlabelled type level.

## 1. The two canonical occurrence banks

For `n>=L`, put

```text
A_n={x=(x_0,...,x_d) in Z_(>0)^L : sum_i x_i=n}.
```

Let `R` denote cyclic right rotation,

```text
R(x_0,...,x_d)=(x_d,x_0,...,x_(d-1)).              (1.1)
```

### Core-free bank

The package `g_(0,r-1)` has permanent core zero.  Its occurrence set is

```text
V={v_x:x in A_r},             type(v_x)=x,            (1.2)
```

and its raw successor is

```text
v_x -> v_(R x).                                      (1.3)
```

This is legal with equality in every age-transition row.  Its cardinality
is

```text
|V|=|A_r|=C(r-1,d).                                  (1.4)
```

### `K=1` high-separator bank

The package `g_(0,r-2)` has mobile sum `r-1` and permanent current core
one.  Define

```text
iota(y)=(1+y_0,y_1,...,y_d),       y in A_(r-1).      (1.5)
```

Its occurrence set and raw successor are

```text
H={h_y:y in A_(r-1)},       type(h_y)=iota(y),
h_y -> h_(R y).                                      (1.6)
```

Indeed the head type is

```text
iota(Ry)=(1+y_d,y_0,...,y_(d-1)).                    (1.7)
```

For the transition inequalities `c'_(i+1)<=c_i`, the row `i=0` is
`y_0<=1+y_0`, and every later row is equality.  Thus (1.6) is legal.
The map `iota` is injective and

```text
|H|=|A_(r-1)|=C(r-2,d).                              (1.8)
```

These are exactly the occurrence counts of one canonical package copy:

```text
g_(0,r-1)
 = C(r-2,d)e_0 + C(r-2,d-1)e_(r-1),

g_(0,r-2)
 = C(r-3,d)e_0 + C(r-3,d-1)e_(r-2),                 (1.9)
```

and Pascal gives the masses (1.4) and (1.8).  No composition in either
bank is duplicated internally.  A type `c in A_r` occurs once in each
bank exactly when `c_0>=2`: in the second bank it is `h_(c-e_0)`.

The condition `r>=d+3` is exact for this canonical nontrivial class,
because its high role `r-2` must satisfy `r-2>d`.  At `r=d+2`, the symbol
`g_(0,r-2)` is not a long/mixed rotor generator.

## 2. The necklace-incidence graph

Let

```text
N_r=A_r/<R>,               N_(r-1)=A_(r-1)/<R>       (2.1)
```

be the raw rotation-necklace sets.  Define a bipartite graph `Gamma` on
`N_r disjoint_union N_(r-1)` as follows.  Join `O in N_r` to
`P in N_(r-1)` when there are `x in O`, `y in P`, and a coordinate `j`
such that

```text
x=y+e_j.                                             (2.2)
```

Equivalently, rotate both compositions so that `j` becomes zero.  Then

```text
sigma x=sigma y+e_0=iota(sigma y),                   (2.3)
```

so the two raw cycles contain occurrences with exactly the same age type.

### Lemma 2.1 (connected necklace incidence)

The graph `Gamma` is connected.

#### Proof

Consider the graph on `A_r` in which

```text
x ~ x-e_i+e_j              whenever x_i>=2.          (2.4)
```

It is connected.  From any positive composition, repeatedly move every
unit above one into coordinate zero; this reaches

```text
(r-d,1,...,1),                                      (2.5)
```

and all intermediate compositions remain positive.

If `x' = x-e_i+e_j`, put `y=x-e_i=x'-e_j`.  Then
`y in A_(r-1)`, and in `Gamma` the rotation orbits of `x` and `x'` are
joined by the length-two path

```text
[x] -- [y] -- [x'].                                  (2.6)
```

Thus all vertices of `N_r` lie in one component of `Gamma`.  Every
`[y] in N_(r-1)` is adjacent to `[y+e_0] in N_r`, so no vertex on the
other shore is omitted.  Hence `Gamma` is connected.  QED.

The proof uses one full copy of `A_(r-1)`: exactly one occurrence for each
positive composition `y`.  It does not assert that this full bank is
minimal.  A smaller rotation-stable separator bank would suffice whenever
its corresponding necklace-incidence graph remains connected.

## 3. Serial same-type cycle switches

The following elementary point is the reason the connected quotient graph
is already enough at unlabelled type level.

### Lemma 3.1 (same-source-type switch)

Let `u,u'` be occurrences of the same age type in two distinct directed
cycles of a legal type-level successor permutation.  Write their current
arcs as

```text
u -> v,                  u' -> v'.                   (3.1)
```

Then replacing them by

```text
u -> v',                 u' -> v                    (3.2)
```

is legal, preserves every in/out degree, and merges the two cycles into
one.

#### Proof

Type-level legality of an arc depends only on the source type and the head
type through `type(head)_(i+1)<=type(source)_i`.  Since `u,u'` have equal
source type, both current head types are legal from both sources.  The
crossing preserves the indegree of `v,v'` and the outdegree of `u,u'`.
Deleting one arc from each of two directed cycles gives two directed
paths; the crossed arcs concatenate the paths into one directed cycle.
QED.

The same source occurrence may be used again later.  Its current outgoing
head remains legal from that source type, so a later same-type crossing is
still valid.  Thus no edge-private port hypothesis is needed at this
unlabelled level.

### Theorem 3.2 (one-class universal type fusion)

On the occurrence multiset `V disjoint_union H`, there is a legal
type-level successor permutation consisting of one directed cycle.
It is obtained from the raw rotation cover (1.3), (1.6) by exactly

```text
|N_r|+|N_(r-1)|-1                                  (3.3)
```

serial same-type switches along any spanning tree of `Gamma`.

#### Proof

Initially there is one directed cycle for each vertex of `Gamma`: the raw
rotation cycle of that necklace.  Root a spanning tree of `Gamma` and
process its edges from the root outward.  For a parent--child tree edge,
choose the equal-type occurrence pair supplied by (2.3).  At that moment,
the parent occurrence belongs to the already fused root-subtree cycle,
while the child occurrence belongs to a not-yet-fused raw cycle.  Lemma
3.1 merges those two cycles legally.  Continue through all tree edges.

After `|V(Gamma)|-1` switches, every original raw cycle lies in one cycle,
which proves (3.3) and the theorem.  Reuse of a parent-side occurrence is
safe by the observation after Lemma 3.1.  QED.

### Corollary 3.3 (zero occurrence-attached payload boundary)

Attach any fixed vector of abstract role/rank marks to each occurrence in
`V disjoint_union H`.  The construction of Theorem 3.2 changes only
successor arcs.  Therefore the occurrence multiset and the sum of every
occurrence-attached payload are preserved exactly.  In the bounded-debt
merge-tree language, such payload has zero root-minus-leaf boundary and
zero exceptional error.

This includes the aggregate rank signature assigned to the two canonical
package copies.  It does **not** include payload defined by the selected
source--head pair.

## 4. Why this does not yet give a literal named-target absorber

For labelled age states `X,X'` of the same type, a current literal head
`Y` of `X` need not be a literal head of `X'`.  The exact recurrence is

```text
Y_(i+1)=X_i-Y_0,                                    (4.1)
```

not merely the type inequality.  Consequently equal source type does not
make the two live labelled successor menus a rectangle.  Lemma 3.1 can be
lifted only after proving, for every selected tree edge, a literal crossed
pair

```text
X -> Y,       X' -> Y',       X -> Y',       X' -> Y. (4.2)
```

The full-orbit biregular fractional lift proves average supply of labelled
arcs but does not select these correlated rectangles at one copy.

Likewise, lower q1 intersections, upper unions, arbitrary-width interval
witnesses, and compiler-cap cells can depend on the selected arc or on its
literal context.  Their signed provider payload must be replayed on (4.2).
Theorem 3.2 does not show that it vanishes or telescopes.

Thus the strongest proof-safe implication is

```text
one complete K=1 high-separator package
   => unconditional core-free fusion at unlabelled type level,

literal zero/O(1)-debt fusion
   => still needs a one-copy owner--flag cross-rectangle selector
      plus exact signed provider-closure cuts.                 (4.3)
```

Finally, adding `g_(0,r-2)` changes the aggregate role vector by (1.9) and
uses `C(r-2,d)` owner slots.  The theorem neither proves that these slots
can be removed from other packages while retaining the prescribed Ferrers
signature nor that the required named flags exist.  It only proves that a
one-extra-class **word/type** lower bound is impossible.

## 5. Residual sharp capacity row for one literal provider class

The protected `PH` bank of
`MATH_THEOREM_L_NRFC_PROVIDER_CLOSURE_CUT_AND_TWO_BUFFER_DEEP_FIBRE_NOGO_20260801.md`
has `C(d-1)` missing old rank-`(r-1)` q1 colours after arbitrary one-cycle
source reassembly, before outside providers are counted.  Let an added
literal provider class have `B` selected occurrences capable of supplying
an old q1 colour outside the pure retained-source `d`-windows.  Since one
age occurrence offers rank `r-1` at most once, it contributes at most one
such provider incidence.  The exact closure bound remains

```text
h >= C * (d-1)-B.                                   (5.1)
```

For `z` complete copies of a canonical long package `g_(0,b)`, the number
of occurrences whose final mobile cell is one, and hence which can offer
rank `r-1`, is

```text
B <= z C(b-1,d-1).                                  (5.2)
```

Indeed there are `C(b,d)` positive `(d+1)`-part compositions of `b+1`,
and fixing the last part to one leaves `C(b-1,d-1)` compositions.  The
usable fraction is exactly

```text
C(b-1,d-1)/C(b,d)=d/b.                              (5.3)
```

Equations (5.1)--(5.3) are only a terminal provider-capacity lower bound;
they are not a no-go when the class has the required linear stock.  In
particular, the fractional monotone-rotor distribution cannot count one
high-separator occurrence more than once at terminal time, but a sufficiently
large literal class might clear this scalar row.  Its owner--flag matching,
cross-rectangle supply, and all other closure cuts remain the exact gates.

Equivalently, bounded terminal debt in this protected family requires

```text
z >= (C * (d-1)-O(1))/C(b-1,d-1).                   (5.4)
```

For the universal `K=1` class `b=r-2`, one package copy has at most
`C(r-3,d-1)` usable old-q1 providers.  Thus the same class which completely
removes the unlabelled word/topology obstruction can still be forced to
have arbitrarily large literal named debt by taking

```text
C * (d-1) > C(r-3,d-1)+H                            (5.5)
```

protected modules (and enlarging the ambient ground set as required by the
private-tag construction).  This is a scoped one-copy-package lower bound,
not a counterexample when the canonical inventory supplies a growing number
of `K=1` package copies.
