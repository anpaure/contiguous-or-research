# Short-core Middle Levels intervals: the common basis is automatic, contiguity is not

Date: 2026-08-01  
Lane: replace the standard-GK short core by a block cut from a Middle Levels Hamilton cycle  
Status: exact all-`m` common-basis theorem, exact fixed-matching rethread criterion,
an explicit physical obstruction to arbitrary-basis rethreading, and exact positive
audits through `ML(9)`.  No all-`m` cyclic-interval theorem is claimed.

## 0. Verdict

Put

```text
|G|=2m-3,
D=binom(2m-3,m-2),
E=binom(2m-3,m-3),
c=D-E=Cat_(m-1).
```

Take a Hamilton cycle in the Middle Levels incidence graph between ranks
`m-2` and `m-1` of `G`, and choose either one of its two alternating perfect
matchings.  This note proves the following.

1. For **every** chosen perfect matching there is automatically a set `Q` of
   `c` matched edges such that the `D-c=E` complementary lower endpoints
   match bijectively down to rank `m-3`, while the complementary upper
   endpoints match bijectively up to rank `m`.  In matroid language, `Q` is a
   common basis of two dual transversal matroids.  There is even a balanced
   distribution on these common bases with marginal `c/D=2/m`.

2. If `Q` is a cyclic interval of matched edges in the Hamilton order, its
   complement supplies all long chains `R<S<L<U`, while `Q` supplies the
   `c` short chains `S<L`.  Reversing the interval order gives exactly the
   short-core quotient Hamilton path required by the SCD-funnel braid.

3. The automatic common-basis theorem does **not** imply that a common basis
   is a cyclic interval.  Both the balanced common-basis distribution and the
   average of all cyclic intervals have the same uniform barycentre, but two
   integral families can share that barycentre and have no common vertex.

4. Cycle switches which retain the chosen perfect matching have an exact
   scope.  After contracting that matching, a common basis `Q` can be made
   consecutive iff both induced shores admit directed Hamilton paths with
   the two required cross arcs.  Already in `ML(5)` there is a literal common
   deletion basis whose induced quotient has two sinks, so no Hamilton cycle
   retaining the matching can make it consecutive.

5. The desired interval nevertheless exists in every authenticated finite
   fixture tested.  Exhaustively, all 24 unoriented `ML(5)` Hamilton cycles
   have all ten starts good for both matching parities.  The authenticated
   `ML(7)` cycle has `5` and `6` good starts; the authenticated `ML(9)` cycle
   has `39` and `39`.

Thus the short-core proposal is genuinely positive and removes the standard
GK quotient obstruction in the tested cases.  The exact missing theorem is
now a **cyclic-interval common-basis theorem**, not ordinary Hall and not
unqualified Middle Levels cycle switching.

## 1. Hamilton-cycle notation

Write a Middle Levels Hamilton cycle as

```text
S_0,L_0,S_1,L_1,...,S_(D-1),L_(D-1),
```

with indices modulo `D`, where

```text
|S_i|=m-2,     |L_i|=m-1,
S_i subset L_i,     S_(i+1) subset L_i.              (1.1)
```

Its two alternating perfect matchings are

```text
M^0={S_i L_i:i in Z_D},
M^1={S_(i+1) L_i:i in Z_D}.                           (1.2)
```

Fix either matching and index its edges in their cyclic order.  Let `Q` be a
cyclic interval of `c` matched edges and put

```text
P=M\Q,       |P|=E.                                  (1.3)
```

Call `Q` a **simultaneous deletion basis** when

```text
{S_e:e in P} matches bijectively down to binom(G,m-3),
{L_e:e in P} matches bijectively up to   binom(G,m).  (1.4)
```

The word *deletion* refers to deleting `Q`: equivalently, `Q` is a basis in
each of the two dual transversal matroids defined below.

## 2. Exact equivalence with the SCD-funnel short core

### Theorem 2.1 (interval deletion-basis lift)

If `Q` is a cyclic-interval simultaneous deletion basis, then the four
central ranks of `2^G` have a chain partition consisting of

```text
E long chains R_e<S_e<L_e<U_e,       e in P,
c short chains       S_e<L_e,         e in Q.         (2.1)
```

Every rank-`m-3` and rank-`m` set occurs exactly once.  Moreover the short
chains have the quotient Hamilton ordering required in the three-block
SCD-funnel construction.

### Proof

Choose the two bijective matchings in (1.4).  For each `e in P`, let `R_e`
be the distinct matched `(m-3)`-subset of `S_e`, and let `U_e` be the
distinct matched `m`-superset of `L_e`.  The matching `M` itself partitions
both central shores, so (2.1) covers each of the four displayed ranks once.

For `M^0`, consecutive matched edges obey

```text
S_(i+1) subset L_i.                                  (2.2)
```

Read the cyclic block `Q` in reverse order.  Then every current short-chain
lower set lies in the next short-chain upper set:

```text
S_current subset L_next.                             (2.3)
```

This is exactly the arc relation used in the short-chain quotient of
`MATH_THEOREM_OWNER_LAYER_SCD_MULTIFUNNEL_RECURRENCE_AND_THREE_PRIMARY_GATE_20260801.md`.
For `M^1`, use the opposite orientation.  Hence the interval itself is the
required quotient Hamilton path. `square`

This theorem is deliberately scoped to the short core.  It does not by
itself install the exterior upper-exact owner forest, residence, or the
global OR compiler.

## 3. The common deletion basis is automatic

Let

```text
X=binom(G,m-2),       Y=binom(G,m-3).
```

Let `T` be the transversal matroid on `X`: a family of `(m-2)`-sets is
independent when it can be matched to distinct contained members of `Y`.
Its rank is `E`.

### Lemma 3.1 (uniform base point)

The constant vector

```text
b_X=E/D=(m-2)/m                                      (3.1)
```

lies in the base polytope of `T`.  Consequently the constant vector

```text
q_X=1-b_X=c/D=2/m                                    (3.2)
```

lies in the base polytope of `T^*`.

### Proof

In the Boolean incidence graph `Y--X`, give every incidence edge weight
`1/m`.  Every `Y`-vertex has exactly `m` upper neighbours, so its load is
one.  Every `X`-vertex has exactly `m-2` lower neighbours, so its load is
`(m-2)/m`.

The bipartite matching polytope is integral.  The displayed fractional
matching is therefore a convex combination of matchings saturating `Y`.
Their used `X`-sets are bases of `T`, and their marginal vector is (3.1).
The standard identity

```text
B(T^*)={1-x:x in B(T)}
```

gives (3.2). `square`

### Theorem 3.2 (automatic simultaneous deletion basis)

For every perfect matching `M` between ranks `m-2` and `m-1` of `G`, there
exists `Q subset M`, `|Q|=c`, satisfying (1.4).

There is also a probability distribution on such `Q` for which

```text
Pr(e in Q)=c/D=2/m             for every e in M.      (3.3)
```

### Proof

For `e=(S_e,L_e) in M`, define two bijections from `M` to `X` by

```text
tau(e)=S_e,       eta(e)=G\L_e.                       (3.4)
```

Pull `T^*` back along `tau` and `eta`.  Lemma 3.1 puts the same constant
vector (3.2) in both base polytopes.  Equivalently, for every `A subset M`,
both pulled-back ranks are at least `(c/D)|A|`.  Edmonds' matroid-
intersection min--max theorem gives

```text
r_tau(A)+r_eta(M\A)
 >= (c/D)|A|+(c/D)(D-|A|)=c.                         (3.5)
```

Hence there is a common independent set of order `c`, necessarily a basis
of both matroids.  Its complement is a basis of each primal transversal
matroid.  Under complementation, a downward matching from `G\L_e` to rank
`m-3` is exactly an upward matching from `L_e` to rank `m`, proving (1.4).

Finally, the common-base polytope is integral.  Decomposing the shared
constant point (3.2) into common bases gives (3.3). `square`

This is the odd-ground, one-step analogue of the automatic common-basis
theorem in
`MATH_THEOREM_CATALAN_TWO_COORDINATE_COMMON_BASIS_AUTOMATIC_20260731.md`.
It removes all ordinary containment-Hall uncertainty from the short-core
lane.

## 4. Why the balanced theorem does not give a cyclic interval

Let `I_a` be the `D` cyclic intervals of length `c` in the matched-edge
order.  Their average incidence vector is also

```text
(1/D) sum_a 1_(I_a)=(c/D)1.                           (4.1)
```

Thus the common-base polytope and the cyclic-interval polytope both contain
the same uniform point.  This does not imply that they share a vertex.

### Example 4.1 (smallest abstract obstruction)

On cyclic ground order `1,2,3,4`, let `c=2`.  Let `N_1,N_2` be rank-two
partition matroids with blocks

```text
N_1: {1,2}|{3,4},
N_2: {1,4}|{2,3}.                                    (4.2)
```

Their common bases are exactly

```text
{1,3}, {2,4},                                        (4.3)
```

while the cyclic two-intervals are

```text
{1,2}, {2,3}, {3,4}, {4,1}.                          (4.4)
```

There is no common vertex, although both convex hulls contain
`(1/2,1/2,1/2,1/2)`.  Therefore the automatic common-basis theorem plus
uniform-marginal averaging cannot prove contiguity, even for partition
matroids.

The Boolean matroids have much more structure than (4.2), so this is not a
counterexample to the desired short-core theorem.  It is an exact
counterexample to the proposed proof shortcut.

## 5. Exact scope of cycle switches retaining one matching

Fix a perfect matching `M`.  Contract its matched incidence edges.  The
result is the directed graph `H_M` whose vertices are the edges of `M`, with

```text
e -> f    iff    e!=f and S_e subset L_f.             (5.1)
```

A second perfect matching is a directed cycle cover in `H_M`; its union
with `M` is one Middle Levels Hamilton cycle exactly when the cover is one
directed Hamilton cycle.

### Theorem 5.1 (fixed-matching interval criterion)

Let `Q subset M` and `P=M\Q`.  A Middle Levels Hamilton cycle containing
`M` can traverse `Q` consecutively iff there are directed Hamilton paths

```text
q_start -> ... -> q_end      in H_M[Q],
p_start -> ... -> p_end      in H_M[P],               (5.2)
```

together with the two cross arcs

```text
q_end -> p_start,       p_end -> q_start.              (5.3)
```

### Proof

Contract `M` in such a Hamilton cycle.  Cutting its directed Hamilton cycle
at the two boundaries of `Q` gives (5.2)--(5.3).  Conversely, concatenating
the two paths with the two cross arcs gives a directed Hamilton cycle in
`H_M`, which uncontracts to a Middle Levels Hamilton cycle containing `M`.
`square`

Consequently, alternating-cycle switches which preserve `M` cannot make an
arbitrary common basis consecutive.  The induced Hamilton-path condition is
an independent topology row.

### Example 5.2 (literal `ML(5)` fixed-matching obstruction)

On `G={0,1,2,3,4}`, the rank-three Johnson order

```text
7,21,25,13,14,11,19,26,28,22                        (5.4)
```

and its consecutive rank-two intersections form a Middle Levels Hamilton
cycle.  Choose the matching

```text
M=Q disjoint_union P,

Q={(6,7),(5,21),(17,25),(9,13),(10,11)},
P={(12,14),(3,19),(18,26),(24,28),(20,22)}.          (5.5)
```

Each pair is `(S_e,L_e)` in decimal mask notation.  The complement `P`
matches downward to all singletons by

```text
12->8,   3->1,   18->2,   24->16,   20->4,           (5.6)
```

and upward to all rank-four sets by choosing targets whose omitted
coordinates are respectively

```text
4,2,0,1,3.                                           (5.7)
```

Thus `Q` is a simultaneous deletion basis.

But in `H_M[Q]`, both `(6,7)` and `(10,11)` have outdegree zero.  Their lower
sets `{1,2}` and `{1,3}` are contained in no other upper endpoint displayed
in `Q`.  A directed Hamilton path has only one terminal vertex, so
`H_M[Q]` has no directed Hamilton path.  By Theorem 5.1, no Hamilton cycle
retaining `M` can make this common basis consecutive.

Switches which change `M` also change both pulled-back deletion matroids.
They may still prove the desired existence theorem, but the common basis
must then be selected jointly with the switch sequence; it is not an
invariant supplied in advance.

## 6. Exact finite audit

The exact checker is

```text
scratch/audit_short_core_interval_basis.cpp
SHA256 1610ca7ca0eaf01109d0f0c765632299b19d9cf9f18d0dfbb37f4e4addcbeab4
```

It was compiled and run on `ssh h100` with

```text
g++ -std=c++20 -O3 -DNDEBUG
```

under

```text
/home/amodo/or15/work/short_core_interval_audit_20260801.
```

The retained compact audit is

```text
scratch/short_core_interval_basis_20260801.audit.json
SHA256 577cfae18969dd4413200986622d8e6970092506998d3b5c55a588ece4af4720
```

The remote complete output has SHA256

```text
cfb7457c7ec4854d0b9d7ec327590d9481415abf5e064814881ec73aad5c4b0e.
```

The results are:

| cycle | `m` | `D` | `c` | good starts, parity 0 | good starts, parity 1 |
|---|---:|---:|---:|---:|---:|
| authenticated `ML(5)` | 4 | 10 | 5 | 10 | 10 |
| authenticated `ML(7)` | 5 | 35 | 14 | 5 | 6 |
| authenticated `ML(9)` | 6 | 126 | 42 | 39 | 39 |

The `ML(5)` enumeration is exhaustive up to orientation and rotation:
there are 24 Hamilton cycles, and every one has exactly ten good starts for
each matching parity.

For the fixed matching in (5.5), there are 197 common deletion bases, but
only 10 are intervalizable in **any** Hamilton cycle retaining that matching.
For the other matching parity there are 192 common bases and 40 are
intervalizable.  This independently quantifies the fixed-matching topology
gate: common bases are abundant, but most are outside the intervalizable
orbit.

The `ML(9)` source certificate is

```text
scratch/catalan_m5_three_c10_endpoint_socket_20260731.audit.json
SHA256 3af1f9d4e2875b5896d8db355d6ed8f7d72f592f57e634f9d25125f5413b53a4.
```

These are finite positive results, not an induction.

## 7. The exact remaining theorem

The shortest sufficient statement for this lane is now the following.

### Cyclic-Interval Common-Basis Lemma

For every sufficiently large `m`, there exists a Middle Levels Hamilton
cycle on ranks `m-2,m-1` of `[2m-3]`, a choice of matching parity, and a
cyclic interval `Q` of `Cat_(m-1)` matched edges such that `Q` is a common
basis of the two dual deletion matroids in Theorem 3.2.

By Theorem 2.1, this immediately supplies the non-GK short-core quotient
Hamilton path and all long-chain deletion extensions.

A stronger fixed-matching switch theorem would instead prove that, for some
chosen `M`, at least one common basis `Q` satisfies Theorem 5.1.  Theorem 3.2
alone cannot choose such a `Q`; Example 5.2 shows why.

The remaining global owner-layer construction must still reconcile this
short core with the rooted upper-exact Catalan forest, connector tree,
pivot collar, residence, and deeper upper witnesses.  The present theorem
removes the short-core containment matching and identifies contiguity as the
only new local row.

## 8. Proof-safe conclusion

The proposed Middle Levels route is substantially better than the standard
GK short-core quotient:

```text
ordinary two-sided deletion Hall:                 automatic;
short/long central chain counts:                  exact;
short-core quotient Hamilton order from a block: automatic;
cyclic block with both deletion bases:            finite positive, open all-m;
arbitrary common basis -> block by fixed-M switch:false.
```

Therefore the automatic common-basis theorem plus generic cycle switching
does **not** yet prove the construction.  The precise obstruction is the
induced directed Hamilton-path gate in Theorem 5.1.  The precise positive
target is the Cyclic-Interval Common-Basis Lemma above.
