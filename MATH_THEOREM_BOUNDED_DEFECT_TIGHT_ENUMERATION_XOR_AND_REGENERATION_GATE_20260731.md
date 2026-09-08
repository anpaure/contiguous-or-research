# Bounded-defect central forests: tight enumerations, an XOR obstruction, and the regeneration gate

Date: 2026-07-31  
Status: exact central reductions and an infinite architecture-specific
obstruction; no all-dimension bounded-defect construction and no full-word
theorem are claimed

## 0. Verdict

For the additive-constant conjecture, exact Catalan Linear Matching is
stronger than necessary at the **terminal central** stage.  The correct
weaker object is a partial ordered four-transversal with the same number
`t` of missing lower and upper colours and whose physical lift is a spanning
linear forest with `Cat_m+t` components.  Uniformly bounded `t` costs only a
uniformly bounded terminal repair, provided the remaining residence,
provider, and common-cap state is regenerated rather than passively
transported.

Two unconditional constructions reduce this bounded central gate to one
integer statistic.

1. A lower-tight two-level enumeration has an upper turn-collision excess
   `delta`.  Keeping one occurrence of every upper turn colour and breaking
   the support cycle gives central defect

   ```text
   t = max(1, delta).
   ```

2. Any spanning `Cat_m`-path forest with exact upper palette, in particular
   the canonical Chung--Feller/MSW parent, has central defect equal to its
   lower collision excess: delete all but one occurrence of each repeated
   lower colour.

The first reduction has a new infinite parity obstruction.  For

```text
m = 2^a - 1  (a >= 2),
```

the turn-colour XOR differs from the XOR of the complete upper layer.
Consequently every lower-tight cyclic enumeration has `delta >= 2`.  At
`m=3` this is sharp: an explicit cycle below has `delta=2`.  Thus the
tight-enumeration subclass cannot prove exact Catalan Linear Matching even
in its first nontrivial case, while it remains a viable bounded-defect route.

The exact all-`m` central target exposed here is

```text
sup_m min_C max(1, delta(C)) < infinity,
```

where `C` ranges over lower-tight two-level enumerations.  The dual target
uses lower defects of upper-tight enumerations.  Neither follows from the
published existence theorem.

Finally, defects in disjoint Pascal/tag sectors add exactly.  Replacing `s`
atoms can decrease either palette defect by at most `s`.  Therefore a
recursion assembled from an unbounded number of defective terminal blocks
cannot be repaired by a bounded collar.  A proof of `B(k)+O(1)` must reset
or contract the central defect at child scale, in the same sense as the
bounded-defect regenerative-spine theorem; passive block transport is not
enough.

For the optional recursive `SatCycle::sat_2` realization this warning can
be made unconditional and quantitative.  Its exact defect recurrence is
additive on its two tagged children plus a four-entry boundary correction.
Every odd Middle-Levels leaf has a forced collision excess of at least
`Cat_(r+1)`.  Even allowing every splice to repair four defects, the root
deficiency is at least

```text
Cat_(m+1)-Cat_m-Cat_(m-1)
 - 4(sum_(s=0)^(m-1) Cat_s - 1),
```

which is positive from `m=7` and asymptotic to
`(17/12)Cat_m = Theta(W/m)`.  Thus that concrete recursive GMM
implementation cannot yield an `O(1)`-defect central state.  Complementing
or reversing either child does not change the bound.  This does not apply
to the existential Mütze--Su/GMM two-level cycle or to a recursion with a
growing repair interface.

## 1. Central notation and bounded defect

Fix `m>=2`, let `Omega=[2m]`, and put

```text
L = binom(Omega,m-1),   X = binom(Omega,m),
U = binom(Omega,m+1),
N = |L| = |U| = m Cat_m,
M = |X| = (m+1) Cat_m = N+Cat_m.
```

A **central defect-`t` forest** is a set `P` of `N-t` Boolean diamonds
`(L,U)` such that

1. its lower colours are distinct;
2. its upper colours are distinct; and
3. its Johnson lift is a spanning linear forest on `X`.

The lift then has exactly

```text
M-(N-t) = Cat_m+t
```

path components, including isolates.  Orienting every path makes its tail
and head maps injective, so this is precisely a partial ordered
four-transversal missing `t` entries on each of its two equal palette
shores.

The adjective `spanning` only means that unused middle vertices are retained
as isolated paths.  It does not assert a chronology, residence, a deeper
shadow, or a common-cap compiler.

## 2. Extraction from a lower-tight two-level enumeration

Let

```text
R_0,X_0,R_1,X_1,...,R_(N-1),X_(N-1),R_0
```

be a simple saturating cycle in the incidence graph between ranks `m-1`
and `m`.  Thus the `R_i` enumerate `L`, the `X_i` are distinct, and

```text
X_i = R_i union R_(i+1).
```

The opposite Johnson edge at `R_i` is `X_(i-1) X_i`; its upper turn colour
is

```text
T_i = X_(i-1) union X_i
    = R_(i-1) union R_i union R_(i+1).
```

Put

```text
delta(C) = N - |{T_i : i in Z_N}|.
```

### Theorem 2.1 (exact tight-cycle extraction)

Every such cycle contains a central defect-`t` forest with

```text
t = max(1,delta(C)).
```

If `delta(C)>0`, this value is exact for subfamilies of the displayed
opposite edges which retain no repeated upper colour.  If `delta(C)=0`,
one deletion is still necessary because all `N` displayed edges form a
cycle.

#### Proof

Every displayed edge has lower colour `R_i`, so all lower colours are
distinct.  For each upper colour of multiplicity `q`, retain one of its
occurrences and delete the other `q-1`.  This deletes exactly `delta(C)`
edges and leaves all retained upper colours distinct.  When `delta(C)>0`,
at least one edge is deleted from the one support cycle, so the remaining
graph is a forest.  The other `M-N=Cat_m` middle vertices were not on the
support cycle and are retained as isolates.  Its component count is
`Cat_m+delta(C)`.

If `delta(C)=0`, the whole displayed family is the support cycle, not a
forest.  Delete one arbitrary edge.  This leaves a path plus the `Cat_m`
isolates and misses one colour on each palette shore.

For `delta(C)>0`, any upper-injective subfamily must delete at least `q-1`
occurrences from every load-`q` colour, hence at least `delta(C)` edges.
This proves the stated exactness.  \(\square\)

This theorem explains why a cyclic tight enumeration is naturally an
additive-constant input but can never by itself be an exact central forest:
even a perfect turn rainbow retains one physical cycle.

### Corollary 2.2 (maximum-matching deficiency is exactly `delta`)

Form the lower-versus-upper turn occurrence graph with edges
`(R_i,T_i)`.  Every lower vertex has degree one.  Therefore its maximum
matching has size `|{T_i}|` and deficiency exactly `delta(C)`.

#### Proof

All edges incident with one upper colour compete for that one upper vertex,
so a matching uses at most one and has size at most the number of nonempty
upper fibres.  Choosing one edge independently from every nonempty fibre
attains that bound because their lower endpoints are all distinct.  \(\square\)

## 3. The turn-colour XOR invariant

Write

```text
R_(i+1) = R_i - alpha_i + beta_i.
```

The two exterior coordinates in the turn at `R_i` give

```text
T_i = R_i union {alpha_(i-1), beta_i}.
```

All symmetric differences below count multiplicity modulo two.

### Theorem 3.1 (cycle-independent XOR)

For every lower-tight saturating cycle,

```text
triangle_i T_i = triangle_(R in L) R.
```

Consequently

```text
triangle_i T_i = Omega
```

if `binom(2m-1,m-2)` is odd, and it is empty otherwise.

#### Proof

For each coordinate, cyclic membership balance says that the number of
times it is deleted equals the number of times it is inserted.  Hence the
multisets `(alpha_i)` and `(beta_i)` have the same parity vector.  They
cancel in the symmetric difference of the displayed formula for `T_i`,
leaving exactly the symmetric difference of all `R_i`.  The latter family
is the complete rank-`m-1` layer.  Each coordinate belongs to
`binom(2m-1,m-2)` of its members.  \(\square\)

The complete upper layer has the independent XOR

```text
triangle_(U in U) U = Omega
```

if `binom(2m-1,m)` is odd, and is empty otherwise.

### Lemma 3.2 (the parity mismatch dimensions)

For `m>=2`,

```text
binom(2m-1,m) is odd  iff  m is a power of two,
```

whereas

```text
binom(2m-1,m-2) is odd
iff m is a power of two or one less than a power of two.
```

Thus the two XORs differ exactly when

```text
m = 2^a-1,  a>=2.
```

#### Proof

Lucas' theorem says `binom(n,k)` is odd exactly when `k & (n-k)=0`.
The first claim is

```text
m & (m-1) = 0.
```

For the second it gives

```text
(m-2) & (m+1) = 0.
```

The elementary binary solutions of the latter equation are
`m=2^a` and `m=2^a-1`: equivalently, the two integers at distance three,
`m-2` and `m+1`, have disjoint one-bits only in the terminal patterns
`011...110` and `011...101`.  Comparing with the first claim proves the
last statement.  \(\square\)

### Theorem 3.3 (Mersenne two-defect obstruction)

If `m=2^a-1` with `a>=2`, then every lower-tight two-level saturating cycle
satisfies

```text
delta(C) >= 2.
```

#### Proof

Theorem 3.1 and Lemma 3.2 say that the occurrence multiset `(T_i)` and the
complete upper layer have XORs differing by `Omega`.

If `delta=0`, the two size-`N` multisets are identical, contradiction.
If `delta=1`, exactly one upper set `H` is absent and one distinct upper set
`D` occurs twice.  Their XOR difference is `H triangle D`, so it would have
to equal `Omega`.  But two `(m+1)`-sets in a `2m`-set intersect in at least
two points.  Therefore `|H triangle D|<=2m-2`, and it cannot equal `Omega`.
\(\square\)

This is an obstruction only to the lower-tight cyclic subclass.  Exact
Catalan linear forests exist in audited Mersenne cases by other
architectures.

### Corollary 3.4 (sharp universal constant floor for BDTE)

If BDTE holds, its constant must satisfy `C_0>=2`.  The `m=3` fixture in
the next section attains this floor.

Indeed the Mersenne dimensions occur infinitely often and Theorem 3.3
applies in every one of them.

### Lemma 3.5 (the signed defect packet is the minimal parity state)

For any size-`N` occurrence multiset on a size-`N` palette, let `H` be the
set of absent colours and let `D` contain `mu(U)-1` labelled extra copies of
every overloaded colour `U`.  Then

```text
|H|=|D|=delta,
```

and the XOR discrepancy from the complete palette is

```text
chi = triangle_(H in H) H triangle triangle_(D in D) D.
```

#### Proof

The equality of the two cardinalities is the total occurrence ledger.
Modulo two, deleting a missing palette occurrence and inserting every extra
occurrence gives exactly the displayed symmetric difference.  \(\square\)

Thus a bounded recursive central state must retain the actual signed
hole/extra packet (or information strong enough to reconstruct its XOR),
not merely the scalar `delta`.  In a Mersenne dimension every defect-two
state necessarily consists of two holes and two extra copies whose four
set masks XOR to `Omega`.  The `m=3` witness below realizes exactly this
pattern.

## 4. Sharpness at `m=3`

Use six coordinates numbered `0,...,5` and decimal bitmasks.  The cyclic
lower sequence

```text
3,5,9,17,18,6,12,36,33,34,48,20,24,40,10
```

lists all fifteen two-subsets exactly once.  Consecutive masks intersect in
one point, including the wrap edge.  Its fifteen middle edge colours are

```text
7,13,25,19,22,14,44,37,35,50,52,28,56,42,11,
```

all distinct.  Hence it is a valid two-level saturating cycle.  Its upper
turn word is

```text
15,15,29,27,23,30,46,45,39,51,54,60,60,58,43.
```

It has support thirteen: `15` and `60` occur twice, while `53` and `57`
are absent.  Therefore `delta=2`.  Theorem 3.3 proves optimality inside the
tight-enumeration subclass:

```text
min_C delta(C) = 2  at m=3.
```

The companion audit script reconstructs every displayed set and also runs
a symmetry-reduced exhaustive DFS excluding defect at most one.  The DFS is
redundant for the lower bound after Theorem 3.3, but provides an independent
finite check of the model.

## 5. Extraction from an exact-upper path forest

The cyclic support above is not needed if one already has a physical path
forest.

### Theorem 5.1 (one-parent collision extraction)

Let `F` be a spanning `Cat_m`-path forest with `N` edges whose upper colours
are all distinct.  Put

```text
delta_-(F) = N - |{lower colours of F}|.
```

Then `F` contains a central defect-`delta_-(F)` forest.

#### Proof

For every repeated lower colour retain one occurrence and delete all other
occurrences.  Exactly `delta_-(F)` edges are deleted.  Upper injectivity is
inherited, and deleting edges from a forest preserves acyclicity and the
degree cap.  Every deletion increases the component count by one, giving
`Cat_m+delta_-(F)` components.  \(\square\)

The canonical Chung--Feller/MSW parent meets the hypotheses before the
lower-palette test.  Thus its lower collision excess is the exact central
defect of this deletion route; a complementary second parent is unnecessary
for the bounded partial certificate.  The audited values are

```text
m                 2   3   4   5    6    7     8      9
delta_-(MSW_m)    0   2  12  54  222  883  3468  13555.
```

These finite values sharply disfavor the canonical one-parent state, but
they are not an all-`m` lower bound.  Arbitrary conjugate or multi-parent
functional-pseudoforest constructions remain open.

### Theorem 5.2 (exact catalogue linearization ledger)

Let `H` be any diamond catalogue, including a union of MSW/complement
parents.  Let `P` be a lower/upper matching in `H` of size `N-h`, and put

```text
kappa(P)=min{|D| : D subseteq P and Psi(P-D) is a linear forest}.
```

Then `P` contains a central defect-`t` forest with

```text
t=h+kappa(P),
```

and this value is exact among submatchings of `P`.

If `G=Psi(P)`, one elementary upper bound is

```text
kappa(P) <= sum_X(deg_G(X)-2)^+ + c_2,
```

where `c_2` is the number of cycle components after greedily deleting an
edge incident with a vertex of degree greater than two until the degree cap
holds.

#### Proof

Delete a minimum linearizing set `D`.  The retained lower and upper colours
remain distinct, its size is `N-h-|D|`, and its lift is a forest.  Hence its
defect is `h+|D|`.  Conversely every linear-forest submatching of `P` deletes
at least `kappa(P)` edges, proving exactness.

For the upper bound, while a vertex has degree above two delete one of its
incident edges.  Every deletion reduces the displayed overload sum by at
least one, so at most that many deletions are made.  The resulting graph has
maximum degree two; delete one edge from every cycle component.  What
remains is a linear forest.  \(\square\)

For a two-parent functional pseudoforest, forced leaf peeling followed by
independent residual cycle bits enumerates every palette-perfect matching.
The bounded-defect target is therefore not merely bounded Hall deficiency:
it is

```text
min_P (palette deficiency of P + kappa(P)) = O(1).
```

This distinction is already literal at `m=3`: some conjugates have palette
deficiency zero, but the audited perfect lift contains two cycles and hence
has `kappa=2`.  At `m=4` two exceptional coordinate conjugates have both
terms zero.  No all-`m` bounded-conjugate theorem is presently known.

## 6. Tagged-sector additivity and the bounded-collar barrier

Let a desired palette be a disjoint union `P=P_1 dotcup ... dotcup P_b`,
and suppose the occurrence multiset is likewise sector-preserving before a
final repair.  Define palette defect as total palette size minus support
size.

### Lemma 6.1 (exact sector additivity)

Before cross-sector changes,

```text
def(P) = sum_j def(P_j).
```

If `s` old occurrences are replaced by `s` new occurrences, the support of
any one palette can increase by at most `s`.  Hence

```text
def(new) >= sum_j def(P_j) - s.
```

#### Proof

Disjoint tags make supports disjoint, proving additivity.  Deleting an
occurrence never increases support, while inserting one occurrence can add
at most one new colour.  Sum over the `s` insertions.  \(\square\)

### Corollary 6.2 (replicated bad-base barrier)

If a recursive child contains `b` disjoint tagged copies of a base with
palette defect at least `q`, then a repair using `s` changed atoms leaves
defect at least

```text
bq-s
```

on that palette.  In particular, an unbounded number of copies of the
`m=3` tight-cycle base requires an unbounded number of actual palette-changing
atoms; a bounded terminal collar cannot hide the replicated XOR debt.

The statement does not obstruct recursive repair.  It says exactly that the
repair must be a child-scale reset/contraction, not a passive disjoint union
followed by `O(1)` final edits.

## 7. Exact recurrence and no-go for the binary `sat_2` recursion

This section concerns the optional recursive implementation
`SatCycle::sat_2`; it is not identified with the existential two-level cycle
in the published corollary.

At a noncentral state `(n,k)`, the recursion splices two child cycles
`(n-1,k)` and `(n-1,k-1)`.  One child omits the new coordinate `z`, the
other contains it.  Before replacing the connector entries, their turn
supports are therefore disjoint.

For a multiset `M`, write

```text
c(M)=|M|-|supp(M)|.
```

### Lemma 7.1 (one replacement, exact sign)

Suppose one occurrence `x` of `M` is replaced by `y`, and let
`M'=M-x+y`.  Then

```text
c(M')-c(M)
 = 1[multiplicity_M(x)=1]
   - 1[multiplicity_(M-x)(y)=0].
```

In particular one replacement changes collision excess by at most one.

#### Proof

Removing `x` decreases support by one exactly when that occurrence was the
last `x`.  Inserting `y` increases support by one exactly when `y` is absent
after the deletion.  The multiset cardinality is unchanged.  \(\square\)

### Theorem 7.2 (exact finite-state splice recurrence)

Let `c_(n,k)` be the turn collision excess of the recursive cycle.  At an
internal splice there are `s<=4` endpoint occurrences replaced.  If
`M_0` is the disjoint tagged union of the two child turn multisets and

```text
M_j=M_(j-1)-x_j+y_j,
```

then

```text
c_(n,k)=c_(n-1,k)+c_(n-1,k-1)+sum_(j=1)^s epsilon_j,
```

where

```text
epsilon_j = 1[mult_(M_(j-1))(x_j)=1]
            -1[mult_(M_(j-1)-x_j)(y_j)=0]
```

belongs to `{-1,0,1}`.

Thus the scalar recurrence is exact after retaining only the multiplicities,
clipped at two, of the finitely many deleted and inserted boundary values.
In particular

```text
c_(n,k) >= c_(n-1,k)+c_(n-1,k-1)-4.
```

#### Proof

Before connector changes, child values lie in disjoint `z`-sectors, so
their collision excesses add.  Apply Lemma 7.1 sequentially to the at most
four changed entries.  \(\square\)

This is the exact recurrence requested by the bounded-defect question; the
older absolute-error estimate is its projection after forgetting the
boundary multiplicity bits.

The recursion stops either at `k=0`, assigned defect zero, or at a
Middle-Levels state `(2r+1,r)`.  Let `beta_r` be the collision excess at
such a leaf.

### Lemma 7.3 (forced base excess)

For every choice of the Middle-Levels base cycle,

```text
beta_r >= Cat_(r+1).
```

#### Proof

The turn word has one occurrence per rank-`r` vertex, hence
`binom(2r+1,r)` occurrences.  Its values have rank `r+2`, and there are only
`binom(2r+1,r+2)=binom(2r+1,r-1)` possible values.  Therefore

```text
beta_r >= binom(2r+1,r)-binom(2r+1,r-1)
       = 2/(r+2) binom(2r+1,r)
       = Cat_(r+1).
```

\(\square\)

For the root call `(2m,m-1)`, leaves of type `(2r+1,r)` occur with
multiplicity `Cat_(m-r-1)`, and the total number of leaves, including the
`k=0` leaves, is

```text
L_m=sum_(s=0)^(m-1) Cat_s.
```

A full binary recursion tree has `L_m-1` internal splices.

### Theorem 7.4 (recursive-GMM bounded-defect no-go)

For the `sat_2` root cycle,

```text
c_(2m,m-1) >= Gamma_m,
```

where

```text
Gamma_m = Cat_(m+1)-Cat_m-Cat_(m-1)
          -4(sum_(s=0)^(m-1)Cat_s-1).
```

The right side is positive for every `m>=7`, and

```text
Gamma_m = (17/12+o(1)) Cat_m
        = Theta( binom(2m,m)/m ).
```

Hence this recursive implementation has unbounded maximum-matching
deficiency in its lower-versus-upper turn occurrence graph and cannot
supply BDTE.

#### Proof

Iterate the lower bound in Theorem 7.2 over the full recursion tree and use
Lemma 7.3.  This gives

```text
c_(2m,m-1)
 >= sum_(r=1)^(m-1) Cat_(m-r-1) Cat_(r+1)
    -4(L_m-1).
```

The Catalan convolution

```text
Cat_(m+1)=sum_(t=0)^m Cat_t Cat_(m-t)
```

turns the displayed leaf sum into
`Cat_(m+1)-Cat_m-Cat_(m-1)`, proving the formula.  Direct Catalan arithmetic
gives `Gamma_7=85`.  Moreover

```text
(Gamma_(m+1)-Gamma_m)/Cat_m
 = 4(m^2-4m-6)/((m+2)(m+3)) + (m+1)/(4m-2),
```

which is positive for `m>=6`; hence it stays positive.
Finally

```text
Cat_(m+1)/Cat_m -> 4,
Cat_(m-1)/Cat_m -> 1/4,
sum_(s<m)Cat_s/Cat_m -> 1/3,
```

giving `4-1-1/4-4/3=17/12`.  The turn occurrence graph is left-functional,
one edge per lower colour, so its maximum matching size is exactly its
number of distinct upper neighbours.  Its matching deficiency is therefore
`c_(2m,m-1)`.  \(\square\)

Complementation, coordinate permutation, and child reversal preserve
collision excess.  A complement-paired version with the same two disjoint
tag sectors and at most four changed boundary occurrences consequently
obeys the same lower bound.  Escaping Theorem 7.4 requires either a different
global two-level cycle, a boundary interface whose number of genuinely
changed turn occurrences grows with the recursion, or a non-sectorwise
rethreading which destroys the additive child decomposition.

There is a useful sharp constant-width calibration.  If the same binary
leaf decomposition is retained but every internal splice may replace at
most `q` turn occurrences, the identical proof gives

```text
c_root >= Cat_(m+1)-Cat_m-Cat_(m-1)
          -q(sum_(s=0)^(m-1)Cat_s-1)
        = (11/4-q/3+o(1))Cat_m.
```

### Corollary 7.5 (nine-entry threshold)

Every such sectorwise binary recursion with `q<=8` has
`c_root=Omega(Cat_m)` and cannot satisfy BDTE.  Therefore a bounded-defect
repair which keeps this leaf decomposition must change at least nine turn
occurrences per typical binary splice, or else use a genuinely
non-sectorwise operation not measured by occurrence replacement.

This is a necessary ledger threshold, not a sufficiency theorem for a
nine-entry collar.  It is also specific to the **stateless** `sat_2` leaf
expansion, which rebuilds the root from all growing Middle-Levels leaves.
A stateful dimension-to-dimension induction that takes an already repaired
defect-`C_0` child as its input has only `O(C_0)` old debt and is not subject
to the Catalan leaf sum.  This is precisely the distinction between a fresh
recursive enumeration and a regenerative sidecar.

## 8. Exact connection to the regenerative interface

Call the following statement **BDTE** (bounded-defect tight enumeration):

```text
There is an absolute C_0 such that, for every m, some lower-tight
two-level saturating cycle C_m has max(1,delta(C_m)) <= C_0.
```

Theorem 2.1 shows that BDTE supplies a terminal central forest with at most
`C_0` missing colours per palette and at most `C_0` extra path components.
Theorem 5.1 gives the alternative one-parent statement
`sup_m delta_-(F_m)<infinity` for any chosen exact-upper forest family.

This closes only the `x_cent` coordinate of a bounded-defect sidecar.  To
deduce `nu(k)<=B(k)+O(1)`, one still needs one compatible odd spine whose
terminal physicalizations have bounded repair charge and whose carried
state satisfies either a bounded invariant or a contraction

```text
Phi(g') <= rho Phi(g)+beta,   rho<1.
```

At that interface the central contribution can be charged by

```text
x_cent <= C_0,
```

and by at most `2C_0` exposed path sockets.  The terminal missing palette
members may be appended once; they must not be copied into the next sidecar.
Residence, all deeper upper providers, and the common-cap compiler must be
recomputed jointly on the selected physical chronology.  Lemma 6.1 shows
why merely tagging and transporting old defects cannot establish the
uniform bound.

Therefore the shortest honest bounded-state theorem is:

> **Bounded central reset + regenerative physicalization.**  Prove BDTE
> (or its exact-upper-forest dual), and prove that one choice of its extracted
> forest in every odd dimension admits odd/even physicalizations whose
> noncentral carried potential remains uniformly bounded and whose total
> terminal charge is `O(C_0+Phi)`.

Together with the already proved bounded-defect spine implication, this
gives `nu(k)<=B(k)+O(1)`.  BDTE alone does not.

## 9. Exact scope

What is proved here:

* the precise defect extracted from a two-level tight enumeration;
* the precise defect extracted from an exact-upper path forest;
* the all-`m` XOR invariant;
* the infinite `delta>=2` obstruction at `m=2^a-1`;
* sharpness `delta=2` at `m=3`; and
* exact additivity under tagged sector composition;
* an `Omega(Cat_m)=Omega(W/m)` defect lower bound for the concrete binary
  `sat_2` recursion, even with arbitrary Middle-Levels base cycles.

What is not proved:

* BDTE for all `m`;
* bounded lower defect of the canonical MSW parent (the finite data point in
  the opposite direction);
* a bounded-parent functional-pseudoforest construction;
* bounded defect for the existential Mütze--Su/GMM saturating cycle (which
  is not the `sat_2` implementation);
* regeneration of residence, deeper shadows, or the common cap; or
* `nu(k)<=B(k)+O(1)` unconditionally.

## 10. Reproducibility and interfaces

The finite checks are:

* `scratch/audit_bounded_defect_tight_enumeration_m3_20260731.py`;
* `scratch/bounded_defect_tight_enumeration_m3_20260731.audit.json`;
* `scratch/audit_bounded_defect_msw_lower_collision_20260731.py`; and
* `scratch/audit_recursive_gmm_bounded_defect_nogo_20260731.py`.

The literal `sat_2` splice and Catalan leaf multiplicities were previously
derived in
`MATH_AUDIT_GMM_COR2_SUCCESSOR_AND_TRIPLE_UNION_BOUNDARY_20260726.md`.
The terminal-versus-carried implication used in Section 8 is
`MATH_THEOREM_BOUNDED_DEFECT_REGENERATIVE_SPINE_AND_EXPLICIT_O1_CONSTANT_20260731.md`.
