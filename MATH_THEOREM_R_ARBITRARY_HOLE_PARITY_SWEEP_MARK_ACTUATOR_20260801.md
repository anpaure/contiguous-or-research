# Arbitrary terminal holes admit a two-parity marked-regrouping actuator

Date: 2026-08-01  
Lane: R / age-composition circulation / protected Catalan interface

Status: unconditional at the marked-profile/age-circulation level.  Every
normalized terminal profile with any number of small holes can be regrouped,
rank by rank neutrally, into a stationary packet supported on at most
`2d+1` age types and at most `3d+3` occurrence roles.  The packet uses two
parity sweeps of the age-token path.  It does **not** by itself choose
one-copy owner occurrences, preserve upper/common-cap tickets, or splice the
packet into a literal contiguous-OR factor.

## 1. Age notation

Fix a depth `d>=2` and an owner rank `r`.  An age type is

```text
c=(c_0,...,c_d),  c_0>=1, c_i>=0, sum_i c_i=r.
```

Its positive marked-deficit set is

```text
Def(c)={c_d,c_d+c_(d-1),...,c_d+...+c_1},
```

with repetitions and zero deleted when they occur.  Write

```text
P(c)=(c_0,...,c_(d-1)),  Q(c)=(c_1,...,c_d).
```

The directed age edge `c->c'` is legal exactly when

```text
Q(c')<=P(c)
```

coordinatewise.

Throughout, `[s]={1,...,s}`.

## 2. The normalized arbitrary-hole terminal row

Fix `h>=1` and put

```text
B=d+h-1.
```

Assume

```text
r>=B+2.                                                   (2.1)
```

Let `H` be an `h`-subset of `[B-1]`, and consider the full `d`-mark
terminal profile

```text
A=([B]\H) union {r-1}.                                   (2.2)
```

The condition `H subset [B-1]` is only a normalization: `B` is the largest
retained small mark.  It also makes (2.2) a `d`-set, while (2.1) keeps its
top mark `r-1` separate from the small block.

Split the holes and the retained high small marks as

```text
L=H intersect [d],
U=[d+1,B]\H.                                              (2.3)
```

Then

```text
|L|=|U|+1.                                                (2.4)
```

Indeed, `[d+1,B]` has `h-1` elements and contains `h-|L|`
holes, so it retains `|L|-1` elements.  In particular `L` is nonempty.

Choose the one low hole which will remain by the rule

```text
m=d,             if d is in L;
m any element L, if d is not in L.                        (2.5)
```

Choose an arbitrary bijection

```text
phi:L\{m} -> U,
u_a=phi(a).                                               (2.6)
```

For every `a in L\{m}`, take one donor row with profile `[d]` and
exchange the two marks

```text
u_a in A  <->  a in [d].                                 (2.7)
```

After all exchanges, the terminal row and donor rows have profiles

```text
A*=([d]\{m}) union {r-1},
Yprof_(a,u_a)=([d]\{a}) union {u_a}.                      (2.8)
```

The choice (2.5) ensures that every exchanged `a` is at most `d-1`.

### Lemma 2.1 (exact mark neutrality)

As incidence vectors on the deficit ranks,

```text
1_A + sum_(a in L\{m}) 1_[d]
 = 1_(A*) + sum_(a in L\{m}) 1_(Yprof_(a,u_a)).           (2.9)
```

#### Proof

The terminal row loses every element of `U` and gains every element of
`L\{m}`.  Since (2.4) and (2.6) pair those sets bijectively, its small
profile becomes exactly `[d]\{m}`.  Donor `a` loses `a` and gains `u_a`.
Thus every removed rank mark is reinserted once and every inserted rank mark
was removed once.  The top mark `r-1` is unchanged.  This proves (2.9).
QED.

## 3. The explicit age types

Put

```text
M=r-d.
```

By (2.1), `M>=2`.  Define the canonical type

```text
D=(M,1,...,1).                                            (3.1)
```

For `1<=p<=d`, define

```text
R_p=(M-1,1,...,1), with coordinate p raised from 1 to 2. (3.2)
```

Here and below `p` is a positive-age coordinate, so `1<=p<=d`.
Their exact profiles are

```text
Def(D)=[d],
Def(R_p)=[d+1]\{d-p+1}.                                  (3.3)
```

For an exchanged pair `(a,u)`, put

```text
p(a)=d-a+1.                                               (3.4)
```

By (2.5), `2<=p(a)<=d`.  Define

```text
Y_(a,u):
  y_0=r-u,
  y_1=u-d,
  y_(p(a))=2,
  y_i=1 for 2<=i<=d, i!=p(a).                            (3.5)
```

Because `d<u<=B<=r-2`, all its entries are positive and sum to `r`.
Directly reading its reversed gaps gives

```text
Def(Y_(a,u))=([d]\{a}) union {u}.                        (3.6)
```

Finally define the type `X_m` carried by `A*`.

If `m<d`, put `j=d-m+1` and

```text
(X_m)_0=1,
(X_m)_1=M-1,
(X_m)_j=2,
(X_m)_i=1 for 2<=i<=d, i!=j.                             (3.7)
```

If `m=d`, put

```text
X_d=(1,M,1,...,1).                                        (3.8)
```

In both cases

```text
Def(X_m)=([d]\{m}) union {r-1}.                          (3.9)
```

Thus every type has the literal marked profile claimed in (2.8) or (3.3);
none is merely an unlabelled capacity vector.

## 4. The base terminal cycle

### Lemma 4.1

If `m<d` and `j=d-m+1`, then

```text
X_m -> D -> R_1 -> R_2 -> ... -> R_(j-1) -> X_m          (4.1)
```

is a legal directed age cycle.  If `m=d`, then

```text
X_d -> D -> X_d                                           (4.2)
```

is a legal directed age cycle.

#### Proof

For `X_m->D`, every coordinate of `Q(D)` equals one, while every
coordinate of `P(X_m)` is at least one.  The edge `D->R_1` uses only

```text
(R_1)_1=2<=D_0=M.
```

Each edge `R_p->R_(p+1)` moves the unique excess unit one age to the
right; its only nonunit comparison is

```text
(R_(p+1))_(p+1)=2=(R_p)_p.
```

For the last edge in (4.1),

```text
(X_m)_1=M-1=(R_(j-1))_0,
(X_m)_j=2=(R_(j-1))_(j-1),
```

and all remaining comparisons are `1<=1` or `1<=2`.

For (4.2), `Q(D)=(1,...,1)<=P(X_d)`, while

```text
Q(X_d)=(M,1,...,1)=P(D).
```

This proves both claims.  QED.

## 5. Two parity sweeps close every donor simultaneously

Let

```text
E={p(a) mod 2 : a in L\{m}} subseteq {0,1}.               (5.1)
```

For each used parity `epsilon in E` and each `1<=p<=d`, define

```text
S_p^epsilon = Y_(a,u_a),
  if p=p(a) and p mod 2=epsilon for some a;
S_p^epsilon = R_p,
  otherwise.                                              (5.2)
```

The map `a->p(a)` is injective.  Every donor type occurs in exactly one
parity sweep.  Also `S_1^epsilon=R_1`, because (2.5) excluded `a=d`.

### Lemma 5.1 (parity-sweep lemma)

For every `epsilon in E`,

```text
D -> S_1^epsilon -> S_2^epsilon -> ... -> S_d^epsilon -> D (5.3)
```

is a legal directed age cycle.

#### Proof

The first edge is `D->R_1`, already checked in Lemma 4.1.

Fix `1<=p<d`.  Both `S_p^epsilon` and `S_(p+1)^epsilon`
have their unique small excess at their displayed indices `p` and `p+1`.
Thus the target excess comparison is always

```text
(S_(p+1)^epsilon)_(p+1)=2
 <= (S_p^epsilon)_p=2.                                   (5.4)
```

All other target positive-age coordinates except coordinate one equal one.
It remains only to check target coordinate one against source coordinate
zero.

Two adjacent indices have opposite parity, so (5.2) never places donor
types at both ends of the same edge.  There are therefore only three cases.

1. For `R_p->R_(p+1)`, the comparison is `1<=M-1`.
2. For `Y_(a,u)->R_(p+1)`, it is
   `1<=r-u`, true because `u<=r-2`.
3. For `R_p->Y_(a,u)`, it is

   ```text
   u-d <= r-d-2 = M-2 < M-1=(R_p)_0.                     (5.5)
   ```

Every remaining comparison is between positive entries and one.  Finally,
`Q(D)=(1,...,1)<=P(S_d^epsilon)`, because every coordinate of
`P(S_d^epsilon)` is positive.  This proves (5.3).  QED.

### Remark 5.2 (when one sweep suffices)

If all donor types are placed in a single sweep, the only new possible
failure is a consecutive pair

```text
Y_(a,u) -> Y_(a-1,v).
```

It is legal exactly when

```text
v-d <= r-u,
equivalently u+v<=r+d.                                    (5.6)
```

Thus a one-sweep compression is possible exactly when the high labels can
be assigned to the filled-hole path so that (5.6) holds on every adjacent
filled pair.  Since distinct labels satisfy `u+v<=2B-1`, the coarse
sufficient condition

```text
r>=d+2h-3                                                (5.7)
```

makes every bijection work.  The two-parity construction does not need
(5.6) or (5.7).

## 6. Uniform arbitrary-hole actuator

### Theorem 6.1

Under the assumptions of Section 2, perform the mark exchanges (2.7).
Take one copy of the base cycle from Lemma 4.1 and one copy of each used
parity cycle (5.3).  The resulting post-regrouping type multiset is a
stationary integral age circulation with exactly the same marked-rank
marginals as the input packet.

Equivalently, distinguish the repeated `D` occurrences and cross their
outgoing edges pairwise.  Since every tail still has type `D`, these legal
two-edge switches concatenate the constituent cycles into one directed
closed age walk without identifying or deleting an occurrence.  This
closed walk has

```text
at most 2d+1 distinct age types,
at most 3d+3 occurrence roles.                            (6.1)
```

At the marked-row level, the input has one terminal occurrence
`(c(A),A)`, where `c(A)` is the positive type forced by the full profile
`A`, and one donor occurrence `(D,[d])` for every exchanged pair.  The
regrouping **retimes** these distinguished occurrences as

```text
(c(A),A)       -> (X_m,A*),
(D,[d])        -> (Y_(a,u_a),Yprof_(a,u_a)).               (6.2)
```

All reservoir occurrences `(D,[d])` and `(R_p,Def(R_p))` are unchanged.
No stationarity is asserted for the pre-regrouping type multiset; the
theorem asserts exact mark-marginal equality and stationarity of the
post-regrouping packet.

#### Proof

By Lemmas 4.1 and 5.1, every constituent is a legal directed age cycle.
The sum of their integral edge-incidence circulations is stationary.  Each
`Y_(a,u_a)` appears in exactly one parity cycle, `X_m` appears in the
base cycle, and every other occurrence is a `D` or `R_p` reservoir.
Equations (3.3), (3.6), and (3.9) identify all their marked profiles.
Lemma 2.1 proves exact marked-rank neutrality between the input and output
packets.  The type changes in (6.2) are essential: changing profile labels
while falsely retaining the old forced types would not be a valid operation.

Let `t=|U|<=d-1` and let `c=|E|<=2`.  If `m<d`, the base cycle has
`j+1<=d+1` vertex occurrences and each parity cycle has `d+1`; hence

```text
(j+1)+c(d+1)<=3d+3.                                      (6.3)
```

If `m=d`, the base cycle has two occurrences, so the stronger bound
`2+2(d+1)=2d+4` holds.  The union of type supports is contained in

```text
{D,X_m} union {R_1,...,R_d}
  union {Y_(a,u_a):a in L\{m}},                           (6.4)
```

whose size is at most `2+d+t<=2d+1`.  Crossing outgoing edges at
occurrence-distinguished copies of `D` preserves all type incidences and
stationarity.  QED.

### Corollary 6.2 (multiplicity)

For `q` identical terminal rows, multiplying every occurrence in Theorem
6.1 by `q` gives an exact integral stationary circulation and retains every
rank-mark count.  The *type library* remains of size at most `2d+1`, while
the required labelled occurrence stock scales as `O(qd)`.

## 7. Relation to the single- and double-hole actuators

For `h=1`, no donor is needed and Lemma 4.1 is the terminal-gap cycle.

For `h=2`, one high mark is exchanged with one low hole.  Theorem 6.1 gives
an alternative all-depth double-hole repair using the canonical donor
profile `[d]`.  This does not supersede the `k=76` uniqueness theorem:
the canonical systematic `k=76` profile law does not stock `[d]`, whereas
its unique minimum repair uses donor `{1,2,3,5,7}`.  The present theorem is
a joint marked-grouping/reservoir construction, not a claim about the frozen
systematic donor catalogue.

For `h>=3`, the parity split is the new point.  It prevents two donor types
with potentially incompatible fresh/age-one loads from ever being adjacent;
the intervening `R_p` simultaneously advances the excess token and resets
the fresh-class capacity.

## 8. Exact protected-host interface and nonclaims

Theorem 6.1 is an integral quotient packet.  It proves that arbitrary-hole
marked regrouping has no further age-circulation or rank-marginal
obstruction, provided the displayed occurrence roles are stocked.  It also
shows that only `O(d)` roles per repaired terminal occurrence are needed;
there is no algebraic need for an unbounded family indexed by the hole set.

It is **not** yet a literal owner-moving packet in one exact factor.  A
protected Catalan/pivot host must still supply all of the following jointly:

1. distinct occurrence-labelled rows for every repeated `D`, `R_p`, and
   donor role in the closed walk;
2. actual set-partition transitions lifting every displayed age edge, with
   one-copy middle owners;
3. separation from the pivot, upper-witness, residence, and common-cap
   ticket banks, or a proof that the packet transports those tickets;
4. payload-transparent component switches which splice the lifted closed
   walk into the rooted physical chronology.

If those rows are selected from an existing host, the actuator adds no word
positions: it only regroups marks and reassigns existing age transitions.
The theorem does not prove that such a protected stock exists.  In
particular, for a terminal block of multiplicity `q`, the physical bank has
`Theta(qd)` labelled occurrences even though it uses only `O(d)` age types;
fixed-post-hoc `O(d)` common-basis avoidance is therefore insufficient when
`q` grows.  A joint owner/common-basis selector or an orbit-compressed lift
remains necessary.

No upper-shadow theorem, compiler theorem, contiguous-OR word, or bound on
`nu(k)` is claimed here.

## 9. Audit status

Every profile identity and every age edge above has been independently
checked symbolically.  An independent proof of the underlying single-cycle
construction, including the exact one-sweep criterion (5.6), is recorded in

```text
MATH_AUDIT_R_SINGLE_DOUBLE_HOLE_MARK_ACTUATORS_AND_UNIVERSAL_FULLTYPE_RESERVOIR_20260801.md
```

The two-parity decomposition is a graph-theoretic refinement: the donor
positions form a subgraph of the path on positive-age indices, whose two
parity classes contain no adjacent vertices.  It uses no finite search.
