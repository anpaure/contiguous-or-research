# K17 compact age projection and fixed-D coloured-Hall decomposition

Date: 2026-08-01

## 1. Scope

This note concerns the loopless `Z_17`-equivariant fixed-MASS age-bimatching
necessary skeleton used in the age-first K17 programme.  It proves an exact
projection of the staged rank-7 plus eager rank-10 round-0 formula and an
exact fixed-`D` decomposition of upper-q1 completion.

The following are still outside unless explicitly stated otherwise:

- lower suffix ranks 2 through 6;
- quotient connectivity and nonzero voltage, except when checked lazily;
- upper ranks 11 through 16 and upper-safe opening;
- opened lower-q1 restitution;
- generalized lower compiler, common cap, and literal OR-word realization.

Thus no statement below is a proof of the K17 optimum or of unrestricted
carrier existence.

## 2. The compact projection theorem

Let `X` be the common semantic variables consisting of the owner type, the
four age classes on every owner coordinate, the facet-survivor availability
bits, and the two owner-facet incidence matchings `D,H`.

### Theorem 2.1

The frozen round-0 staged-rank7/ordered-root CNF and the compact CNF defined
in Sections 3--5 have exactly the same satisfiable projection onto `X`.

The compact CNF has exactly

```text
613656 variables
3240006 clauses
```

versus round 0's `2964627 / 13706998`.

### Proof overview

The proof is the composition of four bidirectional extension lemmas:

1. exact binary count circuits replace the old local histogram clauses and
   global unary counters;
2. deterministic rank-7 witnesses replace suffix-selector exact-one rows;
3. implication-only rank-10 provider witnesses replace exact conjunction
   variables at this existential stage;
4. the normalized root and its distinct provider are extension-only before
   root-sensitive opening constraints.

Each lemma is proved below.  All auxiliary variables in either encoding can
then be reconstructed from a common semantic assignment.

## 3. Exact compact count circuits

### 3.1 Gates

For Boolean inputs `a,b`, a half adder has outputs

```text
s = a xor b,
c = a and b.
```

The xor is encoded by its four falsifying-assignment clauses and the and by
three standard equivalence clauses, for seven clauses total.

For inputs `a,b,c`, a full adder has

```text
s = a xor b xor c,
d = majority(a,b,c).
```

Eight input-assignment clauses force parity and six clauses force majority,
for fourteen clauses total.  Direct truth-table inspection proves both gate
relations in both directions.

Adding two little-endian `ell`-bit numbers uses one half adder at bit zero and
`ell-1` full adders.  It has `2ell` new variables and `14ell-7` clauses.  A
balanced tree on a power-of-two number of padded inputs therefore computes
the exact integer sum, not merely a relaxation.

### 3.2 Global type masses

For each of types 0 through 7, pad the 1,430 owner type bits by 618 unit-zero
variables to 2,048 and use the balanced adder tree.  Fix all twelve output
bits to the required mass

```text
(139,297,8,20,20,140,127,237).
```

Per type this costs 8,784 variables and 43,463 clauses; over eight types,

```text
70272 variables, 347704 clauses.
```

Type 8 is omitted from the global counter.  Once every owner has exactly one
type, its count is

```text
1430-(139+297+8+20+20+140+127+237)=442.
```

### 3.3 Local age histograms

Retain exact-one among ages 0,1,2,3 at every owner coordinate.  For each owner
count only ages 0 and 1, padding nine inputs to sixteen.  A local counter has
59 variables and 266 circuit/padding clauses; its low four result bits are
conditioned on the selected type, adding 36 clauses.  Two counters cost
`118 / 604` per owner.  Add exact-one among the nine age-3 bits, costing
`8 / 24` per owner.

The nine pairs of required `(age0,age1)` counts are

```text
(1,5),(1,6),(2,5),(3,3),(3,4),(4,3),(5,1),(5,2),(6,1).
```

They are pairwise distinct.  Hence a type ALO already implies type AMO:
selecting two types would force some counter bit to both signs.  Coordinate
exact-one and `age3=1` then give

```text
age2 = 9-age0-age1-age3 = 8-age0-age1,
```

which is exactly the omitted profile coordinate.  Thus the local circuit is
equivalent to the old four histogram rows.  Over all owners its complete
local block, including coordinate exact-one and type ALO, costs

```text
218790 variables, 1015300 clauses.
```

Together with the fixed semantic allocation, matching exact-one rows,
same-owner loop exclusions, and the age bridge, the compact age/D/H core is

```text
459232 variables, 2465550 clauses.
```

## 4. Deterministic rank-7 projection

For owner `o`, let

```text
L(o) = {owner coordinates having age 0 or 1}.
```

Every allowed type has `|L(o)|` equal to 6 or 7.  Introduce a witness
`w(o,S)` only for each seven-subset `S` of the nine owner coordinates.  The
eleven implications are:

- for each of the seven elements of `S`, `w -> (age0 or age1)`;
- for each excluded element, `w -> not age0` and `w -> not age1`.

Thus at most one witness can be true for a fixed owner, and a true witness
has `S=L(o)`.  The six types with `|L(o)|=7` have total mass

```text
297+8+20+140+237+442 = 1144.
```

There are also exactly 1,144 rank-7 rotation-orbit targets.  One ALO per
target therefore forces at least 1,144 true witnesses; only 1,144 owners can
supply one, so the witnesses form a bijection between eligible owners and
targets.  Every omitted owner AMO, target AMO, and size-six selector is
therefore implied after projection.

Conversely, from a satisfying semantic assignment set each old owner suffix
selector to the unique set `L(o)` (of size six or seven).  This reconstructs
the old staged-rank7 layer.  The compact rank-7 block costs

```text
51480 variables, 567424 clauses.
```

The compact base is consequently

```text
510712 variables, 3032974 clauses.
```

## 5. Rank-10 and root projection

At each quotient facet, exact `D,H` matching rows and the same-owner loop
exclusions determine one actual nonloop ordered turn.  Hence every semantic
solution has exactly 1,430 actual turns.

For each allowed ordered turn `a=(d,h)`, introduce an implication-only
provider `p_a` with

```text
p_a -> D_d,
p_a -> H_h.
```

Add one provider ALO for each of the 1,144 rank-10 colour orbits.  Any true
provider is an actual turn, so compact satisfaction implies that every
rank-10 orbit is actually covered.  Conversely, for an actually complete
factor select one actual provider in every orbit.  The projection is exact;
false provider variables must never be interpreted as absent turns.

This block costs

```text
102944 variables, 207032 clauses.
```

Since 1,430 actual turns cover 1,144 nonempty colour groups, some colour has
load at least two.  Choose either actual turn in a repeated group as the old
unique normalized root and another as its distinct provider.  Set every old
exact conjunction variable to `D_d and H_h` and extend the Sinz root prefix
canonically.  Therefore all 205,887 old root/root-aux variables and 514,717
root clauses are extension-only before root-sensitive opening cuts.

This completes the proof of Theorem 2.1.

## 6. Exact replay rule

A compact SAT witness is accepted only after:

1. complete assignment and all-clause replay of the compact CNF;
2. reconstruction of all actual turns from `D/H`, ignoring false provider
   bits;
3. verification of all 1,144 actual and certified rank-10 orbit loads;
4. export of every actual turn in a load-at-least-two orbit as a root
   candidate, with a distinct actual mate;
5. literal age/rank-7 replay;
6. quotient connectivity/nonzero-voltage separation.

Only after these checks may an existential root oracle test trim-3 upper
ranks 11 through 16.  The old ordered-layer separator cannot consume compact
provider bits as though they were exact conjunctions.

## 7. Exact fixed-D coloured-Hall fallback

Fix `D` and a literal age state.  Form the bipartite multigraph `G(D,a)` from
facets to head owners.  Its edges are precisely nonloop `H` incidences that
satisfy the endpoint-age and survivor bridge constraints against the fixed
`D` supply.  Label an edge by its resulting rank-10 colour orbit.  Parallel
incidence IDs are retained.

### Theorem 7.1

There exists a rank-10-complete perfect matching `H` in `G(D,a)` if and only
if there exists a matching `P` such that:

1. `P` contains exactly one edge of every one of the 1,144 colours; and
2. `G(D,a)-V(P)` has a perfect matching, necessarily of size 286.

### Proof

If `H` exists, select one `H` edge of each colour.  These 1,144 edges form
`P` because `H` is a matching; the remaining 286 `H` edges are the residual
perfect matching.  Conversely, the union of `P` and a residual perfect
matching is a perfect matching covering every colour.  ∎

For consumed-facet indicators `x_f` and consumed-owner indicators `y_o`,
residual Hall is equivalent to the unit-coefficient family

```text
sum_{o in N(S)} y_o
  <= |N(S)|-|S| + sum_{f in S} x_f
```

for every facet set `S`.  Indeed, a residual perfect matching injects the
`|S|-x(S)` unconsumed facets of `S` into the `|N(S)|-y(N(S))` unconsumed
owners of `N(S)`, proving necessity.  Conversely, a residual Hall-deficient
set can be chosen entirely among unconsumed facets, where the same row is
exactly the failed Hall inequality.  Alternating reachability after a failed
maximum matching returns such a violated set `S`, with violation equal to
the matching deficiency.  In representative-edge variables `p_e`, the row
is equivalently

```text
sum_{e: facet(e) in S} p_e - sum_{e: owner(e) in N(S)} p_e
  >= |S|-|N(S)|.
```

This is an exact Benders fallback, not a fixed-width heuristic.  It is exact
only after both `D` and the age state are fixed; fixing `D` alone does not
remove age-dependent edge availability.  Topology, voltage, higher shadows,
and compiler gates remain subsequent stages.

### Theorem 7.2 (fixed-`D`, variable-age q1 projection)

Let `B` be the already-generated compact rank-7 base CNF, before the
root-free q1 provider layer.  Fix only one literal perfect matching `D_0` by
its 1,430 positive incidence literals; leave every age and `H` variable in
`B` free.  At each facet, `D_0` fixes the physical tail and hence assigns a
fixed upper-q1 colour to every nonloop `H` incidence there.  Add one clause

```text
OR { H_e : colour(D_0,e)=c }
```

for every one of the 1,144 rank-10 colour orbits `c`.

The resulting formula is satisfiable if and only if `D_0` extends, through
some age state and some legal perfect matching `H`, to the compact pre-
topology rank-7/q1 skeleton.  With the `D_0` assumptions emitted as unit
clauses it has exactly

```text
510712 variables
3032974 + 1430 + 1144 = 3035548 clauses.
```

#### Proof

The base CNF already enforces all age profiles and masses, the direct rank-7
rows, both perfect matchings, the selected-`D` availability equations, every
`H` age-consumption implication, and the same-owner loop exclusions.  Once
`D_0` is fixed, the union colour of an actual turn depends only on its
selected `H` incidence, so the 1,144 added ALOs are exactly upper-q1
surjectivity.  Conversely, from any solution of the compact provider formula
with `D=D_0`, forget the provider variables; its base assignment satisfies
these ALOs.  Given a solution of the fixed-`D` formula, choose one selected
`H` edge from every colour ALO and set precisely the corresponding provider
bits.  This reconstructs the compact formula.  ∎

A proof-verified UNSAT result for this face gives the canonical outer
Benders clause

```text
OR_{d in D_0} not D_d,
```

which has 1,430 literals and excludes `D_0` for every age state.  A timeout
gives no clause.  This is the preferred lighter staged face after a compact-
base incumbent; it is strictly broader than freezing that incumbent's ages.

### Theorem 7.3 (complete two-shore residual-flow cuts)

Fix `D`, an age state `a`, and a matching `P` containing one representative
of every q1 colour.  Put `x_f=1` and `y_o=1` on the 1,144 facets and owners
consumed by `P`.  For a facet-owner pair `(f,o)`, let `w_fo(a)=1` precisely
when at least one parallel `H` incidence from `f` to `o` is genuinely legal
for `a` and the fixed `D` tail.  Then the remaining 286 edges exist if and
only if, for every `S` of facets and `T` of owners,

```text
sum_{f in S, o notin T} w_fo + x(S)-y(T) >= |S|-|T|.       (7.1)
```

#### Proof

Use the network with capacities

```text
source -> f : 1-x_f
f -> o      : w_fo
o -> sink   : 1-y_o.
```

The required flow is `1430-1144=286`.  The cut whose source side contains
facet set `S` and owner set `T` has capacity

```text
286-|S|+x(S)+sum_{f in S,o notin T}w_fo+|T|-y(T).
```

Thus all cuts have capacity at least 286 exactly when (7.1) holds.  Integral
max flow gives the residual matching, and every residual matching satisfies
the same cut count.  This proves both directions.  Taking `T=N(S)` recovers
the coefficient-one Hall row in Theorem 7.1.  Parallel incidences must be
compressed by the Boolean OR `w_fo`; their sum is a weaker relaxation.  ∎

### Theorem 7.4 (fixed-`(D,H)` age face and core cuts)

Let `H_0` be a q1-complete static matching for `D_0`.  The formula

```text
B AND {D_d : d in D_0} AND {H_h : h in H_0}
```

has exactly

```text
510712 variables
3032974+1430+1430 = 3035834 clauses,
```

and is satisfiable exactly when `(D_0,H_0)` has an age/direct-rank7
extension.  If a verified UNSAT core retains subsets `D'` and `H'` of its
positive units, then

```text
OR_{d in D'} not D_d OR OR_{h in H'} not H_h                (7.2)
```

is valid in the unrestricted joint master.  Under the standing condition
`D=D_0`, its shorter local form is simply

```text
OR_{h in H'} not H_h.                                      (7.3)
```

Neither (7.3) nor the full 1,430-edge `H_0` no-good excludes `D_0` by
itself.  The `D_0` no-good is justified only after the entire static-H master,
augmented by sound local cuts, is proof-verified UNSAT.  Full proof and
fail-closed core extraction are formalized separately in
`MATH_THEOREM_AD_K17_FIXED_DH_CORE_BENDERS_LOOP_20260801.md`.

### Theorem 7.5 (pure outer-`D` colour-capacity cuts)

For a q1-colour set `T`, facet set `A`, and owner set `C`, suppose

```text
delta = |T|-|A|-|C| > 0.
```

Let `Q(T,A,C)` be the set of `D` incidences at facets outside `A` for which
some nonloop `H` incidence has owner outside `C` and its turn colour lies in
`T`.  Every q1-extendable `D` satisfies

```text
sum_{d in Q(T,A,C)} D_d >= delta.                            (7.4)
```

Indeed, at most `|A|` of the `|T|` pairwise-disjoint colour representatives
use facets in `A`, and at most `|C|` further representatives use owners in
`C`.  Every remaining representative requires a distinct selected `D`
incidence in `Q`.  A minimum vertex cover of a deficient union-provider
graph gives a directly violated instance.  These rows are not complete:
on `K_2,2`, diagonal edges of one colour and antidiagonal edges of another
pass every union-shore matching test but admit no rainbow two-edge matching.
Thus an integral representative master remains necessary.

No compact-base incumbent is actually required to start this decomposition.
The quotient owner--facet incidence multigraph is 9-regular on two shores of
size 1,430.  For every owner set `S`, its `9|S|` incident edges end in
`N(S)`, which receives at most `9|N(S)|` edges; hence `|N(S)|>=|S|`.
Hall therefore supplies a perfect matching `D_0`.  A deterministic
augmenting-path algorithm gives one literal outer-master incumbent.  Solve
the fixed-`D_0` face above; on verified UNSAT append its 1,430-literal cut to
the bipartite matching master and choose another `D`.  This logic-Benders
enumeration is exact, although the full-face no-good alone need not be an
efficient convergence theorem.

### Theorem 7.3 (exact 11,440-variable fixed-incumbent face)

Fix a literal age state and `D`.  For every incidence `e` that is a legal
`H` edge against this fixed pair, introduce one Boolean `h_e`.  Its upper-q1
colour is now a fixed label: it is the orbit of the union of the fixed
`D`-tail at `e`'s facet with `e`'s head owner.  Impose:

1. exactly one `h_e` at each quotient facet;
2. exactly one `h_e` at each quotient head owner;
3. at least one `h_e` of every one of the 1,144 upper-q1 colours.

Call the resulting formula `Q(D,a)`.  Then `Q(D,a)` is satisfiable if and
only if `(D,a)` extends to an age-legal, loopless, upper-q1-complete perfect
matching `H`.

It has at most 11,440 variables: at each fixed-`D` facet, at least one
incidence having the same owner as the selected `D` edge is forbidden
(there may be a parallel same-owner family in the quotient multigraph).
Facet degree is therefore at most eight and owner degree at most nine.
Pairwise exact-one
encoding gives at most

```text
1430*(1+binom(8,2)) + 1430*(1+binom(9,2)) + 1144 = 95524
```

clauses, with no ordered-turn conjunction or provider variables.

#### Proof

Every selected legal incidence supplies one edge of `H`.  The first two row
families say exactly that these edges form a perfect facet-to-owner matching;
the third says exactly that its fixed turn-colour image is surjective.  This
is precisely the desired extension.  Conversely, the incidence indicators
of any desired `H` satisfy all three row families.  The size bound follows
from the 12,870 incidence census, the forced same-owner exclusion at every
facet, and the incidence degree bounds.  ∎

The already-generated compact base (`510712 / 3032974`) also gives a
proof-safe lighter first stage: solve it, retain only its age and `D`
semantics, discard its provisional `H`, and solve `Q(D,a)`.  Iterating this
logic-based Benders split over base incumbents is complete for the same
pre-topology rank-7/q1 projection; one arbitrary base incumbent followed by
`Q(D,a)` UNSAT excludes only that fixed face.  A satisfying
`Q(D,a)` assignment replaces the provisional `H`; choosing one selected
edge of each q1 colour reconstructs all implication-only provider bits, so
the full compact CNF can and must be replayed literally.

If `Q(D,a)` is unsatisfiable, its proof excludes only that fixed age/`D`
incumbent.  A reusable logic-based Benders row requires either:

- a sufficient assumption core over the fixed age/`D` literals, whose
  negated conjunction is appended to the base master; or
- the coloured representative formulation of Theorem 7.1 and an exact
  residual Hall shore returned by alternating reachability.

Even without core minimization there is a canonical sound face no-good.
Because the base has exact-one `D` at every facet and exact-one age at every
owner coordinate, the 1,430 selected `D` literals and 12,870 selected age
literals determine the whole semantic face.  Therefore `Q(D,a)` UNSAT
justifies the 14,300-literal master clause

```text
OR_{selected D_e} not D_e
  OR OR_{selected age(o,b,j)} not age(o,b,j).
```

An assumption core may only shorten this clause; it is not needed for
soundness.  The UNSAT proof for `Q(D,a)` and the exact semantic binding must
both be retained.  In particular, solver `UNKNOWN` justifies no no-good.

A mere timeout supplies neither row.  Within a fixed age/`D` face, existing
topology and cyclic higher-shadow rows also contract exactly from ordered
turn atoms to the corresponding `h_e` variables, because the `D` tail at
each facet is fixed.  Root-sensitive opening rows still need an explicit
existential root choice and are not included in `Q(D,a)`.

## 8. Artifacts

```text
scratch/build_ad_k17_incidence_bimatching_age_direct_rank7_20260801.cpp
  SHA 929df90315748d640db90c23eb501487c6ce83ab222100208f9636e1cc8fdd46

scratch/build_ad_k17_age_bimatching_rootfree_rank10_layer_20260801.cpp
  SHA 5d4e717d5cfa813388d1860daa5ac8a94793911f109cdfa510822588147e59ca

scratch/verify_ad_k17_direct_rank7_rootfree_rank10_semantics_20260801.cpp
  SHA 828bcfeed9c85810f4cc8db0aae82f7fd61d29332a3aad5d7dd2b6a988dba3c7

scratch/build_ad_k17_fixed_D_variable_age_rank10_layer_20260801.cpp
  SHA 6b4a10577717a26886bc6529df136490794bc6459c49612e8ad748a6799a7b6e

scratch/build_ad_k17_fixed_age_D_rank10_H_subproblem_20260801.cpp
  SHA 8d5a7166e9ac690501f69be5b7893e54064309d91171d4e570e24285b9767beb

scratch/lift_ad_k17_fixed_D_sat_to_compact_model_20260801.cpp
  SHA ec3657344e7e6a6a7e5a975dbefbacbbcf885af29ca43f5743cef913a82c0e8d

scratch/build_ad_k17_fixed_D_outer_nogood_20260801.cpp
  SHA f60b2fabcb8dca407352eabaf952dbec64718211a8b11d9cdc9ec91c105e012e
```

Generated H100 package:

```text
/home/amodo/or15/work/ad_k17_age_compact_929df903_5d4e717d_20260801
```

The composed CNF has SHA
`9c431267864a819d1a58079ee50aea557279a17bda61dbfd97aecbb680a9c719`.

Map hashes:

```text
9255e0a94e0a278a9e92990b8534ee4d7ee7a96eebbe56631df1205adef31950  base.direct.map.tsv
6f77724052a0dad8571a5bc5b3177bc4c74077be9e698e2a44e38e74eba63dd1  rootfree.rank10.layer.map.tsv
```

Both staged builders are scoped to the authenticated frozen base

```text
fc6dbf2469502e2e02be7818074e18ebcecd65403268e713917820515688c4f7  base.direct.cnf
9255e0a94e0a278a9e92990b8534ee4d7ee7a96eebbe56631df1205adef31950  base.direct.map.tsv
0ea1eb78aed578eddaada54b6e472ecd4f2bd4d16646c2c0ef966e1f54967415  base.direct.stats.json
```

Their source-level deterministic variable-ID checks do not replace these
artifact hashes.  A runner must hash-bind the inputs before generation and
must independently parse/hash every completed output before treating it as a
solver instance or certificate.
