# Quarantined four-level tight enumerations are generalized Pascal braids

Date: 2026-07-29

Status: exact equivalence theorem.  It identifies a single classical-looking
global object whose contraction is the generalized odd Pascal braid.  Its
existence with the required quarantine and decorations remains open.  The
published GMM theorem does not force quarantine: the exact rank-transition
simplex and explicit `m=2` listings below realize low--low, low--high, and
high--high defect steps separately.  In the odd-middle-layer dimensions it
also identifies complement-coherent lower `q=2` with upper `q=1` and derives
the exact strict-trace NAND law; neither identity supplies coverage by
itself.

## 1. Four consecutive levels

Assume `m>=2`.  Let `Omega=[2m]`, and write

\[
 A=\binom\Omega m,\quad B=\binom\Omega{m+1},\quad
 L=\binom\Omega{m-1},\quad H=\binom\Omega{m+2}.
\]

Put

\[
 W=|A|=(m+1)C,\quad |L|=|B|=N=mC,\quad
 |H|=N_2=\frac{m(m-1)}{m+2}C,
\]

where `C=Cat_m`.  In the four-level cube graph induced by
`L union A union B union H`, one parity shore is `L union B`, and the other
is `A union H`.  Their imbalance is

\[
 t=2N-(W+N_2)
  =\frac{2(m-1)}{m+2}C.                               \tag{1.1}
\]

This is exactly the `B`-merge count in the generalized Pascal braid.

## 2. Quarantine

A tight cyclic enumeration of the four levels has total flip length twice
the larger shore.  The standard parity count therefore forces:

1. every opposite-shore step has Hamming distance one;
2. exactly `t` same-shore steps occur; and
3. every same-shore step has Hamming distance two and lies in `L union B`.

Call such an enumeration **B-quarantined** when every one of those `t`
distance-two steps joins two rank-`m+1` vertices in `B`.  Thus no distance-two
step touches `L`.

### Theorem 2.1 (exact rank-type simplex)

For an arbitrary tight enumeration, let

```text
u = number of distance-two L--L steps,
v = number of distance-two L--B steps,
w = number of distance-two B--B steps.
```

Then

\[
                         u+v+w=t,                    \tag{2.1}
\]

and the counts of one-bit transitions between consecutive ranks are

\[
\begin{aligned}
 e_{L,A}&=2N-2u-v,\\
 e_{A,B}&=2C+2u+v,\\
 e_{B,H}&=2N_2.
\end{aligned}                                        \tag{2.2}
\]

Consequently B-quarantine is exactly the corner

\[
 u=v=0,\quad w=t,
 \qquad\Longleftrightarrow\qquad e_{L,A}=2N.          \tag{2.3}
\]

This corner is consistent with every rank, parity, and degree equation, but
none of those equations forces it.

#### Proof

Let `p` be the number of opposite-parity transitions and let `x,y` count
same-parity transitions on `A union H` and `L union B`, respectively.
Cyclic incidence counting gives

\[
 p+2x=2(W+N_2),\qquad p+2y=4N.
\]

The metric lower bound for the flip length is `p+2x+2y=4N+2x`, whereas
tightness gives length `4N`.  Hence `x=0`, `y=t`, every cross transition is
one-bit, and every same-shore transition is two-bit.  This proves (2.1).
Every `H` vertex must then have two `B` neighbours, giving
`e_(B,H)=2N_2`.  Counting incidences at `L` and then at `A` gives (2.2).
Finally `2N-e_(L,A)=2u+v`, proving (2.3).  \(\square\)

### Source audit and sharp scope

GMM Corollary 2 asserts a tight enumeration for every interval of
consecutive levels.  In the noncentral case its proof delegates to the
earlier trimming-and-gluing theorem.  The GMM statement and proof do not
carry a parameter locating the `t` same-shore steps among `L` and `B`.
Therefore the published GMM theorem gives (2.1), not the extra equality
(2.3).  Whether the delegated construction can be strengthened to force
(2.3) for every `m` is an additional constrained-enumeration problem.

Already for `m=2`, all three extreme locations occur.  The following cyclic
listings each enumerate all fifteen nonempty subsets of `[4]` and have
fourteen cube edges plus one two-flip edge:

```text
L--L (final edge 1--4):
4,34,3,23,234,24,2,12,124,1234,123,13,134,14,1,(4)

L--B (final edge 123--1):
1,14,134,34,4,24,2,12,124,1234,234,23,3,13,123,(1)

B--B (final edge 124--123):
123,13,3,23,234,34,4,24,2,12,1,14,134,1234,124,(123)
```

Their flip length is `16`, the tight value.  Thus bare tightness cannot
quarantine the defect, while the last listing proves that there is no
universal rank-count obstruction to quarantine.

## 3. Contraction theorem

### Theorem 3.1

Suppress every vertex of `L union H` from a B-quarantined tight enumeration.
The result is a Hamilton cycle on `A union B` with exactly

\[
 AA=N,\qquad BB_{\rm protected}=N_2,\qquad
 BB_{\rm merge}=t,\qquad AB=2C.                       \tag{3.1}
\]

Moreover:

1. the `AA` intersections are every member of `L` exactly once;
2. the protected `BB` unions are every member of `H` exactly once;
3. every contracted edge is a legal Johnson edge inside a shore or a
   containment edge between shores.

#### Proof

No same-shore step touches a vertex of `L`.  Hence each `R in L` is flanked
by two distinct rank-`m` neighbours.  Suppressing `R` produces the Johnson
edge between them, of intersection colour `R`.  This gives `N` exact `AA`
edges.

Every `Y in H` lies in the smaller parity shore, so both of its neighbours
are rank-`m+1` sets.  Suppressing it produces one protected `BB` edge of
union colour `Y`, giving `N_2` such edges.  The `t` quarantined direct steps
are additional Johnson `BB` edges.  All remaining steps are direct cube
edges from `A` to `B` and hence are containment edges.

Suppressing vertices from a cyclic listing leaves one cyclic listing of all
`W+N` middle owners.  Therefore the remaining cross count is

\[
 W+N-N-N_2-t=W-N_2-t=2C,
\]

using (1.1) and `W=N+C`.  This proves (3.1) and every label assertion.
\(\square\)

After adjoining a new coordinate `z` to every owner in `A`, Theorem 3.1 is
exactly the channel skeleton of an odd generalized Pascal braid.

## 4. Expansion theorem

### Theorem 4.1

Conversely, suppose a Hamilton cycle on `A union B` has the channel counts
(3.1), its `AA` intersection colours are exactly `L`, and a distinguished
set of `N_2` `BB` edges has union colours exactly `H`.  Expand every `AA`
edge through its intersection vertex in `L`, and every distinguished `BB`
edge through its union vertex in `H`.  Leave the `t` remaining `BB` edges and
the `2C` cross edges unexpanded.

The result is a B-quarantined tight enumeration of all four levels.

#### Proof

Exactness of the two colour maps makes every vertex of `L union H` appear
once, and the Hamilton middle cycle makes every vertex of `A union B` appear
once.  Expanded edges become two cube edges; cross edges are already cube
edges; the remaining `BB` edges are distance-two steps wholly inside `B`.
Thus the only same-parity steps are precisely the `t` quarantined ones.

The total flip length is

\[
 2N+2N_2+2t+2C
 =2(N+N_2+t+C)=4N,                                    \tag{4.1}
\]

because `t=N-N_2-C`.  The larger parity shore has size `2N`, so (4.1) is
the tight value.  \(\square\)

### Corollary 4.2 (exact equivalence)

The generalized Pascal `q=1` channel skeleton and a B-quarantined four-level
tight enumeration are the same object before opposite-colour decorations.
The two-forest port construction is obtained by cutting this single global
enumeration into its `AA` and protected-`BB` subforests.

## 5. Decorations not supplied by tightness

The equivalence deliberately does not claim the coefficient-one theorem.
For the contracted cycle one still needs:

1. pairwise distinct no-`z` lower colours across cross, protected `BB`, and
   merge `BB` edges;
2. coverage of every `z`-upper colour by `AA` unions and cross endpoints;
3. every `AA` component to have at least `d+1` vertices, which is residence
   of `z`;
4. old-coordinate residence and all deeper intersection/union shadows;
5. an exact one-core, compiler Hall, safe cut, and literal word verification.

Nor does the published existence of an arbitrary tight enumeration imply
B-quarantine.  A same-shore distance-two step may lie inside `L` or join a
vertex of `L` to one of `B`.  Such a step destroys the clean contraction:
it can isolate a lower colour or produce a noncontainment middle transition.

Thus the sharp new all-`m` target is:

> construct a decorated B-quarantined tight enumeration of the four consecutive
> levels.

This is stronger than the classical tight-enumeration theorem but packages
chronology, both path forests, all component counts, and all port usage in one
global object.  It is the natural single-object formulation of the remaining
generalized-braid induction.

### Theorem 5.1 (exact opposite-colour interface)

Adjoin `z` to the rank-`m` owners.  For `T in A` and `U in B`, define

\[
\begin{aligned}
 d_\times^A(T)&=\#\{(z+T)--U\text{ cross edges}\},\\
 \mu_B(T)&=\#\{UV\text{ BB edges}:U\cap V=T\},\\
 \lambda_U&=\#\{TT'\text{ AA edges}:T\cup T'=U\},\\
 d_\times^B(U)&=\#\{(z+T)--U\text{ cross edges}\}.
\end{aligned}                                        \tag{5.1}
\]

The contracted quarantined cycle has both lower `q=1` decks exact and both
upper `q=1` decks complete if and only if

\[
 d_\times^A(T)+\mu_B(T)=1\qquad(T\in A),             \tag{5.2}
\]

and

\[
 \lambda_U+d_\times^B(U)\ge1\qquad(U\in B).          \tag{5.3}
\]

The marked `AA` intersections already give every `z`-lower colour, and the
protected `BB` unions already give every no-`z` upper colour.  Thus (5.2)
is exactly the opposite no-`z` lower deck and (5.3) exactly the `z`-upper
cover.  Equation (5.2) forces \(d_\times^A(T)\le1\); consequently the `AA`
forest has no singleton, its `2C` cross labels are its distinct endpoint
set, and the `BB` intersections biject the complementary rank-`m` colours.

For a fixed quarantined chronology satisfying (5.2), its `AA` endpoints are
distinct and its existing cross edges witness endpoint Hall and connected
monodromy.  Before (5.2), the seams still fill endpoint occurrences, but an
`AA` isolate contributes two copies of one lower label and is not represented
by a distinct-label endpoint set.  If two `C`-path sector forests already
satisfying the opposite-lower condition are cut apart and re-paired, let
`E_A` be the endpoint set of the `AA` forest and let

\[
                         b_U=2-\deg_{P_B}(U).
\]

Capacitated containment Hall

\[
 |X|\le\sum_{U\in N(X)}b_U\qquad(X\subseteq E_A)      \tag{5.4}
\]

where `N(X)` is the rank-`m+1` containment neighbourhood, is necessary and
sufficient for an owner-exact cross matching.  Together with upper-hole
exposure `lambda_U+b_U>=1`, it is necessary and sufficient for the re-paired
factor to retain the complete `z`-upper deck.  To recover one Hamilton
chronology, rather than a two-factor, the contracted component
graph must also be connected; equivalently the selected cross matching
\(M_\times\) must obey

\[
 |\delta_{M_\times}(\mathscr S)|\ge2                 \tag{5.5}
\]

for every nonempty proper family of contracted path components.

For an integer `1<=h<=m`, orient each `AA` path
`P=(T_0,...,T_(L(P)-1))` and put

\[
 \omega_d(S)=
 \sum_P\#\left\{0\le i<L(P)-d:
             \bigcap_{j=0}^{d}T_{i+j}=S\right\}.     \tag{5.6}
\]

Under local depth-`h` residence and `L(P)>=h+1`, the complete
`z`-protected tower is exactly

\[
 \omega_d(S)\ge1
 \quad\left(1\le d\le h,
             S\in\binom{[2m]}{m-d}\right).           \tag{5.7}
\]

The single four-level chronology therefore removes Hall and subtour as
*selection* problems only if its actual cross edges are kept.  It does not
make (5.2)--(5.3) or (5.7) automatic, and it supplies no other-coordinate
residence, no-`z` deeper shadows, core closure, or common-`Q` compiler Hall.

### Corollary 5.2 (global `q=1` perfection discharges the port gates)

Let `F` be a Hamilton cycle on all rank-`m+1` subsets of
`Omega union {z}`.  Suppose its edge intersections are every rank-`m`
target exactly once and its adjacent edge unions cover every rank-`m+2`
target.  Relative to `z`, its edge-type counts are forced:

\[
 |E_{AA}|=mC=N,\qquad |E_\times|=2C,\qquad
 |E_{BB}|=(m-1)C=N-C.                                \tag{5.8}
\]

Every no-`z` rank-`m+2` target is the union of a `BB` edge.  Selecting one
such edge for each target gives `N_2` distinct protected edges and leaves

\[
                     (m-1)C-N_2=t                    \tag{5.9}
\]

merge edges.  Expanding all `AA` edges by their old-coordinate intersections
(deleting `z`) and these protected `BB` edges by their unions produces a
`q=1`-decorated
B-quarantined tight enumeration contracting back to `F`.

#### Proof

Only `AA` intersections contain `z`, so exact lower ownership gives exactly
the `N` `AA` edges and their complete marked deck.  Degree two at the `W`
A-owners gives \(2W=2|E_{AA}|+|E_\times|\), hence
\(|E_\times|=2C\); subtracting from the `W+N` cycle edges gives the `BB`
count in (5.8).

Only `BB` unions omit `z`.  Upper `q=1` coverage therefore gives a nonempty
`BB` fibre over every no-`z` target.  Fibres of different targets are
disjoint because an edge has one union, so a transversal uses `N_2`
distinct edges.  Equation (5.9) follows, and Theorem 4.1 performs the
expansion.  \(\square\)

At this first upper rank, adjacent-union coverage is equivalent to coverage
by arbitrary nontrivial carrier intervals.  Indeed, if such an interval has
union `S` of rank `m+2`, every adjacent Johnson pair in it has a rank-`m+2`
union contained in `S`, and hence equal to `S`.  The argument does not extend
to targets of rank at least `m+3`, which may require genuinely wider
intervals.

The original cross edges now simultaneously certify (5.2), (5.3), endpoint
Hall, and connected monodromy.  Fixed-port deletion quotas, exposure, and
Hall are separate only when the two forests are selected independently.
There is no multiedge ambiguity: a Hamilton cycle in the simple Johnson graph
uses each physical edge once, and the union fibres used above are disjoint.

This corollary is strictly a `q=1` statement.  “Adjacent unions” means unions
of two consecutive owners.  Exact lower `q=1` already gives the depth-one
protected deck and forbids `AA` isolates (equivalently singleton `z`-runs).
It supplies no rank-correct union of three or more consecutive owners, no
deeper upper-shadow cover, no residence or protected-window conclusion at
depth at least two, and no core or compiler conclusion.

## 6. Small exact calibration

Suppressing ranks `1` and `4` from the quarantined `m=2` listing above gives

```text
B123,A13,A23,B234,A34,A24,A12,A14,B134,B124,(B123).
```

Its four cross lower labels are `13,23,34,14`, while its protected and merge
`BB` intersections are `14,12`.  Thus it repeats `14` and misses `24`, so
quarantine does not imply (5.2).  Its `AA` path lengths are `2,4`, so it also
fails the depth-two hypothesis in (5.7), even though its `AA` lower deck is
exact.  This is a literal counterexample to both automatic-decoration
shortcuts.

## 7. `m=7` calibration

For the `14 -> 15` step,

\[
(W,N,N_2,C,t,2C)=(3432,3003,2002,429,572,858).
\]

These are exactly the sector counts of the solved full-`q=1` generalized
factor.  That finite factor has nine middle cycles and many residence
defects, so it is not yet the Hamilton/decorated tight enumeration demanded
above.  It confirms the channel arithmetic, not the missing theorem.

## 8. Complement coherence identifies lower `q=2` with upper `q=1`

Put

\[
 k=2m+1,\qquad r=m+1,\qquad
 \widehat W=\binom{k}{r}=W+N=(2m+1)C.                \tag{8.1}
\]

Let

\[
 T=(T_i)_{i\in\mathbb Z_{\widehat W}}
\]

be a Hamilton cycle of `J(k,r)` whose lower `q=1` intersections are exact,
and define

\[
                         X_i=T_i\cap T_{i+1}.         \tag{8.2}
\]

Then

\[
 T_0,X_0,T_1,X_1,\ldots,T_{\widehat W-1},X_{\widehat W-1},T_0
                                                               \tag{8.3}
\]

is a Middle Levels Hamilton cycle.  Conversely, suppressing the rank-`m`
shore of any Middle Levels Hamilton cycle gives such a lower-exact Johnson
cycle.  The identities are

\[
 X_i=T_i\cap T_{i+1},\qquad
 T_i=X_{i-1}\cup X_i.                                 \tag{8.4}
\]

The second identity holds because `X_(i-1)` and `X_i` are distinct rank-`m`
facets of `T_i`.

### Theorem 8.1 (complement half-turn deck duality)

Assume the Middle Levels cycle (8.3) is invariant under set complementation,
meaning that complementation preserves its selected cycle-edge set.
Then `widehat W` is odd.  Writing

\[
                         \widehat W=2s+1,             \tag{8.5}
\]

the alternating indexing may be fixed as in (8.3), and complementation acts
by the half-turn

\[
 \overline{T_i}=X_{i+s},\qquad
 \overline{X_i}=T_{i+s+1}.                            \tag{8.6}
\]

Consequently

\[
 \overline{X_i\cap X_{i+1}}
       =T_{i+s+1}\cup T_{i+s+2}.                      \tag{8.7}
\]

Thus the lower-`q=2` deck of `T` and its upper-`q=1` adjacent-union deck are
pointwise complements, up to the cyclic shift `s+1`.  Their complete load
multisets agree.  In particular, one deck covers its entire expected rank if
and only if the other does.

More generally, for every `q>=0`,

\[
 \overline{\bigcup_{j=0}^{q}T_{i+j}}
     =\bigcap_{j=0}^{q+1}T_{i+s+j}.                  \tag{8.7a}
\]

This is an unconditional set/multiset identity.  Expected-rank shadow
language at larger depth still requires the corresponding residence or rank
condition.

#### Proof

Exact lower `q=1` makes the `X_i` pairwise distinct and exhaustive, so
(8.3)--(8.4) are immediate.  Complementation acts on the abstract cycle
`C_(2 widehat W)` as an involutory dihedral automorphism and swaps its two
rank shores.  A vertex-axis reflection would fix a set, impossible under
complementation.  An edge-axis reflection would fix an edge setwise and
swap its endpoints, forcing a Middle Levels edge `S--overline S`; but a set
is disjoint from, and hence not incident with, its complement for `m>=1`.
Thus reflection is impossible.  The only remaining nontrivial involutory
rotation is the half-turn.  It swaps the alternating shores only when
`widehat W` is odd, and position addition by `widehat W=2s+1` gives (8.6).
Taking complements of `X_i cap X_(i+1)` proves (8.7).  Intersecting
`overline(T_(i+j))=X_(i+s+j)` over `0<=j<=q` and using (8.2) proves
(8.7a).  \(\square\)

By Lucas' theorem, `widehat W` is odd exactly when

\[
                         m=2^a-1.                    \tag{8.8}
\]

Hence this collapse is available at `k=15` (`m=7`), but not in arbitrary
odd dimension.  Even in the admissible dimensions it does not prove either
deck complete; it proves that lower `q=2` and upper `q=1` are one and the
same coverage gate.  Combining Theorem 8.1 with Corollary 5.2, a
complement-coherent carrier that passes lower `q=2` automatically supplies
the upper-`q=1` hypothesis needed for the quarantined lift.

## 9. The strict `c`-space NAND law

Assume in addition that the carrier is voltage-one equivariant.  Identify
coordinates with `Z_k`, put

\[
                         \widehat N=\widehat W/k=C,
\]

and write its binary trace normal form as

\[
 T_i(c)=\{x\in\mathbb Z_k:c_{i-x\widehat N}=1\},
 \qquad c\in\{0,1\}^{\mathbb Z_{\widehat W}}.         \tag{9.1}
\]

### Corollary 9.1 (complement coherence is a scalar NAND subshift)

Under (8.5), the complement half-turn (8.6) is equivalent to

\[
                    1-c_p=c_{p+s}c_{p+s+1}
                    \qquad(p\in\mathbb Z_{\widehat W}).       \tag{9.2}
\]

Put

\[
             \tau=s+1=2^{-1}\pmod{\widehat W},\qquad
             d_i=c_{\tau i}.                          \tag{9.3}
\]

Then (9.2) is equivalent to

\[
             d_{i+1}=\operatorname{NAND}(d_i,d_{i+2})
             =1-d_id_{i+2}                            \tag{9.4}
\]

for every cyclic index `i`.  Equivalently, the cyclic word `d` has neither
`00` nor `111` as a contiguous factor.

#### Proof

For every position `i` and coordinate `x`, the first identity in (8.6)
gives

\[
 1-c_{i-x\widehat N}
   =c_{i+s-x\widehat N}\,c_{i+s+1-x\widehat N}.
\]

As `p=i-x widehat N` ranges over `Z_(widehat W)`, this is exactly (9.2),
and the same membership calculation proves the converse.  Since
`widehat W=2s+1`, one has `2(s+1)=1 mod widehat W`.  Substitute
`p=tau(i+1)` into (9.2); using `s=tau-1` gives

\[
                         1-d_{i+1}=d_id_{i+2},
\]

which is (9.4).  Its allowed length-three factors are precisely

```text
010, 011, 101, 110.
```

These are exactly the binary triples avoiding `00` and `111`, proving the
last equivalence.  \(\square\)

The trace class sums give `(m+1)C` ones and `mC` zeros.  Since the zeros of
`d` are isolated, `d` has `mC` one-runs.  If `a` of them have length two,
then

\[
 mC+a=(m+1)C,
\]

and therefore

\[
 \#(11\text{-runs of }d)=C,\qquad
 \#(1\text{-runs of }d)=(m-1)C.                     \tag{9.4a}
\]

Also `c_p=d_(2p)`.  A physical transition `c_p=1,c_(p+1)=0` is therefore
the step-two pattern `110` in `d`, occurring once at the end of every
length-two `d`-run.  Hence

\[
                       \#(1\text{-runs of }c)=C.     \tag{9.4b}
\]

For `k=15`,

\[
 \widehat W=6435=2\cdot3217+1,\qquad
 \widehat N=429,\qquad \tau=3218.                    \tag{9.5}
\]

Thus `d` has 3,003 isolated zeros, 429 length-two one-runs, and 2,574
singleton one-runs, while the physical trace `c` has 429 one-runs.  The
short runs in the permuted `d` order are not residence defects; residence is
measured in the original `c` order.

The NAND law is an exact complement-coherence filter, not a carrier
construction.  The trace must still satisfy its residue-class rank sums,
Johnson transitions, Hamilton orbit separation, exact lower `q=1`, and
lower-`q=2` coverage.  It supplies no upper-depth coverage by itself;
(8.7a) merely identifies each upper-depth test with the next lower-depth
test.  It gives no compiler conclusion.
