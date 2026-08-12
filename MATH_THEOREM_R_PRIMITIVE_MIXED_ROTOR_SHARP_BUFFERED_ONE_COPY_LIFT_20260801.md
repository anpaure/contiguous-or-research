# Primitive mixed rotor: sharp buffered one-copy lift

Date: 2026-08-01  
Lane: R, named rotor flag-colouring (NRFC)  
Status: unconditional local theorem.  The smallest canonical mixed rotor
has no one-copy labelled lift by itself, but one copy plus exactly `d`
short low-buffer occurrences has an owner-simple literal cycle with an
injective occurrence-labelled lower flag deck.  The number `d` is sharp
even if arbitrary extra occurrence types are allowed.  This is a local
module, not a global Ferrers target-colouring or physical-factor theorem.

## 1. The primitive canonical buffer pair

Fix

```text
k >= r+1,       r>d>=2,       s=r-d>=2.
```

The primitive mixed generator between the two adjacent buffer coordinates
is

```text
g_(d-1,d+1)=e_(d-1)+e_(d+1).
```

Its two positive age types are

```text
P=(s-1,2,1,...,1),       H=(s,1,...,1),              (1.1)
```

where both vectors have `d+1` coordinates.  The type `H` is also the
standard short self-loop type.  One occurrence of `H`, marked only at its
top `d-1` offered ranks, realizes one unit `e_(d-1)`.

The primitive two-state type cycle `P<->H` has no literal labelled
two-cycle.  Indeed, equality of the singleton survivor rows around the
cycle identifies two distinct nonempty age cells in the `P` state.  The
argument below gives the stronger sharp owner-simple lower bound.

## 2. A universal cycle-length lower bound

### Lemma 2.1 (short owner-simple cycles are trivial)

Let a literal cyclic word have period `L`, trace depth `d`, and suppose
each of its `L` owner occurrences must receive a distinct rank-`r` owner.
Then no component has `2<=L<=d+1`.  A component with `L=1` is possible
only when its single source letter already has size `r`.  Consequently, a
component containing an occurrence whose source has size less than `r`
must have

```text
L >= d+2.                                               (2.1)
```

#### Proof

If `2<=L<=d+1`, every cyclic interval of `d+1` source letters contains
every one of the `L` period letters.  Hence all `d+1`-window unions are the
same owner, contradicting owner injectivity.  If `L=1`, its owner is just
the single repeated source letter, so that source must itself have rank
`r`.  The final assertion follows.  QED.

### Corollary 2.2 (sharp occurrence floor for one primitive package)

Any owner-simple literal cycle cover containing the two occurrences of one
primitive package (1.1) needs at least `d` additional occurrences, even if
their types are unrestricted.

#### Proof

Both primitive source sizes, `s-1` and `s`, are less than `r`.  If fewer
than `d` occurrences are added, the entire cover has fewer than `d+2`
occurrences.  Every component then violates Lemma 2.1.  QED.

This is an occurrence/chronology obstruction.  It precedes owner symmetry:
having arbitrarily many available names for owners cannot shorten a
cyclic window below `d+2`.

## 3. Common-core source words and exact multiplicity

The construction is clearest in a slightly more general form.  Let a
cyclic word in the two symbols `P,H` have length `L>d+1`, contain no
adjacent `P` symbols, and give every position `t` a private tag `z_t`.
Choose a fixed set `G` of size `s-2` and a point `b` outside it, and use

```text
S_t=G union {z_t}             at a P position,
S_t=G union {b,z_t}           at an H position.       (3.1)
```

The literal age partition of these sources has type `P` at every `P`
position and type `H` at every `H` position.  Indeed, at a `P` position
the immediately preceding `H` source contributes `{b,z_(t-1)}` to age
one, while every older source contributes only its private tag.  At an `H`
position, the current source refreshes `G,b`, so every older source
contributes only its private tag.  Every owner is

```text
G union {b} union {the d+1 private tags in its window}. (3.2)
```

Since `L>d+1`, these cyclic tag intervals, and hence the owners, are
distinct.  The same argument makes all fixed-length prefix intervals
distinct.

### Theorem 3.1 (exact multiplicity of the unbuffered primitive)

Put

```text
m_0=ceil((d+2)/2).
```

If the ground set has at least

```text
(s-2)+1+2m_0=s-1+2m_0                         (3.3)
```

points, then `m_0` copies of `g_(d-1,d+1)` have a literal owner-simple
one-cycle lift with an injective marked lower deck.  No smaller positive
multiple has any owner-simple literal cycle cover.

#### Proof

Use the alternating type word `(PH)^m_0` in the common-core construction.
Its length `2m_0` is at least `d+2`, and there are no adjacent `P`
positions.  Mark every offered rank on every occurrence.  At rank `s-1`,
the marked prefixes are the `m_0` distinct `P` sources; at rank `s`, they
are the `m_0` distinct `H` sources.  At every larger offered rank, both
types use the same prefix length between two and `d`, so distinct cyclic
tag intervals give distinct targets.  This realizes exactly `m_0` copies
of the primitive signature.

Conversely, `m` primitive copies have only `2m` occurrences, all with
source size less than `r`.  Corollary 2.2's cycle-length argument gives
`2m>=d+2`, hence `m>=m_0`.  QED.

Thus denominator clearing for this primitive has exact factor
`ceil((d+2)/2)`, not a dimension-independent factor.  The obstruction is
chronological, not a shortage of owner names.

## 4. The sharp one-primitive buffered construction

### Theorem 4.1 (primitive rotor plus `d` low-buffer units)

The aggregate packet

```text
g_(d-1,d+1) + d e_(d-1)                               (4.1)
```

has a literal one-copy lift consisting of one owner-simple directed cycle
of length `d+2`.  Its owners are distinct rank-`r` sets, and all marked
nested prefixes of any fixed rank are pairwise distinct.

#### Construction

Choose pairwise disjoint symbols

```text
G, b, w, v_1,...,v_(d+1),       |G|=s-2,             (4.2)
```

inside `[k]`.  Put `L=d+2` and take the following cyclic source letters:

```text
S_0 = G union {w},
S_i = G union {b,v_i},       1<=i<=d+1.              (4.3)
```

For time `t` modulo `L`, define the age cells directly from the literal
word:

```text
C_(t,0)=S_t,
C_(t,j)=S_(t-j) - union_(h=0)^(j-1) S_(t-h),
                                      1<=j<=d.        (4.4)
```

Then, literally and without a type-only relaxation,

```text
C_(t+1,j+1)=C_(t,j)-C_(t+1,0),       0<=j<d.         (4.5)
```

At `t=0`, (4.4) has sizes

```text
(s-1,2,1,...,1)=P:
C_(0,0)=G union {w},
C_(0,1)={b,v_(d+1)},
```

and every later cell is a singleton `v_i`.  At every `t!=0`, the current
source has size `s`; every preceding source contributes only its private
tag `w` or `v_i`, because `G` and, for the other large sources, `b`, were
already refreshed.  Thus all these `d+1` states have type `H`.

Let

```text
Z=G union {b,w,v_1,...,v_(d+1)}.
```

It has size `r+1`.  Each owner is the union of `d+1` consecutive source
letters among the `d+2` letters in (4.3), hence is

```text
T_t=Z-{the private tag of the one omitted source}.    (4.6)
```

The `d+2` owners are therefore distinct rank-`r` facets of `Z`.

Attach the primitive marks to the unique `P` occurrence and any one of the
`H` occurrences, marking every rank that they offer.  Attach one short
`e_(d-1)` mark pattern to each remaining `d` occurrences of `H`, namely
mark only ranks

```text
s+1,s+2,...,r-1.                                    (4.7)
```

This is exactly the aggregate signature (4.1): rank `s-1` is marked once,
rank `s` once, and every rank `s+1,...,r-1` exactly `d+2` times.

Finally, the prefix at a state through age `j-1` is exactly the union of
the `j` consecutive source letters ending at that state.  Rank `s-1`
occurs only at the `P` source, and rank `s` only at the distinguished
primitive `H` source.  At each rank at least `s+1`, all marked prefixes use
the same interval length `2<=j<=d<L`; their sets of private tags are
distinct cyclic intervals.  Hence the occurrence-labelled targets are
pairwise distinct at every rank.  This proves the theorem.  QED.

## 5. Smallest instance and exact interpretation

For `(r,d)=(4,2)`, take `G` empty.  The source cycle is

```text
{w}, {b,v_1}, {b,v_2}, {b,v_3}.                     (5.1)
```

It gives one state of type `(1,2,1)` and three of type `(2,1,1)`, on four
distinct owners (four facets of a five-set).  One `(2,1,1)` occurrence is
the high half of `g_(1,3)` and the other two are the two short low-buffer
units.  Thus the primitive `(1,2,1)<->(2,1,1)` obstruction is repaired at
one copy by **two extra low-buffer occurrences**.  One extra occurrence is
impossible by Corollary 2.2.

Across dimensions this gives a sharp infinite counterfamily to any literal
"two added occurrences suffice" interpretation: for every `d>=3`, one
primitive package plus only two extra buffer occurrences has total length
four, strictly below `d+2`, and cannot be owner-simple.  The exact cost is
`d` extra low units, or alternatively
`ceil((d+2)/2)` copies of the primitive package itself.

The wording matters.  Merely possessing the low/high role pair
`e_(d-1)+e_(d+1)` does not repair its labelled two-cycle; that role pair is
the obstructed primitive itself.  What repairs it is a length-`d+2`
chronology funded by `d` additional low-buffer units.  Consequently no
dimension-independent `O(1)` conversion follows from the two aggregate
buffer inequalities.  Conversely, the required local overhead is exactly
linear in `d`, and the Ferrers conductor has vastly more low-buffer mass;
using that mass globally remains a joint decomposition and target-colouring
problem.

## 6. Precise remaining scope

Theorem 4.1 closes the owner and lower-target rows for this one local
packet, with one literal occurrence of every displayed role.  It does not
show that the canonical Ferrers target families contain a disjoint union of
these facet modules, nor that the aggregate semigroup decomposition can
reserve `d` low units per primitive without changing its other role counts.
It also does not prove upper/deep shadows, source-letter residence,
Ore--Ryser completion, connectivity between modules, or common-cap/compiler
compatibility.

The exact global NRFC remainder can therefore be sharpened as follows:

> Select a decomposition and group every primitive low/high package with a
> length-`d+2` owner/target-simple chronology (the explicit facet module is
> one option), while assigning all other rotor occurrences so that named
> owner and nested-target resources are globally disjoint.  The only
> obstruction left at this layer is this global packing/colouring problem,
> not the primitive two-cycle itself.
