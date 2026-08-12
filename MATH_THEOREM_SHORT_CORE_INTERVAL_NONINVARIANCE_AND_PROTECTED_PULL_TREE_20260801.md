# A cyclic common-basis block is not automatic; a bounded phase relay plus protected pulls is the exact replacement

Date: 2026-08-01  
Lane: short-core Middle Levels interval / SCD multi-funnel  
Status: exact `ML(7)` counterexample to cycle-blind contiguity, exact
protected-factor gluing theorem, and an authenticated three-hex
matching-changing seam at `ML(11)`.  Existence of a recursive phase relay in
every dimension remains open.

## 0. Outcome

Put

```text
|G|=2m-3,
D=binom(2m-3,m-2),
E=binom(2m-3,m-3),
c=D-E=Cat_(m-1).
```

The automatic-common-basis theorem in
`MATH_THEOREM_SHORT_CORE_MIDDLE_LEVELS_CYCLIC_INTERVAL_COMMON_BASIS_GATE_20260801.md`
proves that every perfect matching `M` between ranks `m-2,m-1` has a set
`Q subset M`, `|Q|=c`, whose complementary lower and upper endpoints both
extend by deletion.  What it does not prove is that `Q` is consecutive in a
Middle Levels Hamilton cycle containing `M`.

This note makes that qualification sharp.

1. There is a literal Hamilton cycle of `ML(7)` for which **none** of the
   `35 x 2=70` cyclic blocks of `14` matched edges is a simultaneous
   deletion basis.  Thus the desired interval is not automatic for an
   arbitrary Middle Levels Hamilton cycle, even in the second nontrivial
   dimension.  It is also not invariant under ordinary incidence-hexagon
   Hamilton-to-Hamilton switching.

2. Connectivity can nevertheless be separated completely from the block.
   Start from a spanning two-factor `F=M union N` in which a common basis
   `Q subset M` is already one block of one component.  If the components of
   `F` can be joined by matching-preserving alternating pulls whose supports
   avoid every matched edge of `Q`, then all pulls preserve both deletion
   bases and preserve the literal block.  Any such pull tree produces the
   required Hamilton cycle.

3. The canonical `ML(11)` factor supplies an exact escape from the
   fixed-matching obstruction.  Two incidence hexagons reset the matching
   phase and leave one `132`-edge common-basis component plus two complement
   components.  A third hexagon is matching-preserving, cuts each component
   once, and merges all three.  The basis component is opened exactly once,
   so its complete matching-edge set becomes one literal cyclic block.

The resulting all-dimensional target is strictly weaker than constructing
the Hamilton cycle in one shot:

```text
bounded phase relay creating one protected common-basis component
  + one block-transparent cross pull
  + complement-supported pull tree on the remaining components.
```

For the new four-row-SCD/tight-ear owner forest, every diagonal path or pivot
collar which must survive can be added to the protected bank.  The same proof
then permits all remaining Mütze/hexagon gluing to occur in the unprotected
complement.

## 1. Notation

Write a Middle Levels Hamilton cycle as

```text
S_0,L_0,S_1,L_1,...,S_(D-1),L_(D-1),
```

where

```text
|S_i|=m-2, |L_i|=m-1,
S_i subset L_i, S_(i+1) subset L_i.
```

Its two alternating perfect matchings are

```text
M^0={S_i L_i},
M^1={S_i L_(i-1)}.
```

For a cyclic interval `Q` of `c` matching edges put `P=M\Q`.  The block is a
simultaneous deletion basis when

```text
{S_e:e in P} matches bijectively down to binom(G,m-3),
{L_e:e in P} matches bijectively up   to binom(G,m).
```

Equivalently, `Q` is a common basis of the two pulled-back dual transversal
matroids.  The property depends only on `(M,Q)`.  Contiguity depends on the
other alternating matching and is a separate topology row.

## 2. A literal `ML(7)` cycle with no good block

Take `m=5`, so

```text
D=35, E=21, c=14.
```

In decimal bitmask notation, consider the alternating cycle

```text
7,15,13,45,44,108,76,78,14,46,42,106,98,99,67,83,82,86,
70,102,100,101,37,53,49,51,35,39,38,54,52,116,112,114,
50,58,26,30,22,23,19,27,11,43,41,57,56,60,28,92,84,85,
21,29,25,89,81,113,97,105,104,120,88,90,74,75,73,77,69,71.
```

### Theorem 2.1 (cycle-blind interval assertion is false)

The displayed word is a Hamilton cycle of `ML(7)`.  For matching parity
zero, exactly `13` of its `35` blocks pass the lower deletion matching and
exactly `3` pass the upper deletion matching, but the two sets of starts are
disjoint.  The same counts hold for matching parity one.  Consequently no
cyclic interval of `14` matched edges is a simultaneous deletion basis.

### Proof

The deterministic audit listed in Section 8 performs the following literal
checks.

* The 70 masks are distinct and are exactly all rank-three and rank-four
  masks on seven coordinates.
* Every consecutive pair is a containment edge, including the wrap edge.
* For each of the two matching parities and each of the 35 starts, it deletes
  the corresponding 14-edge block.
* On the 21 retained rank-three endpoints it computes a maximum matching to
  all rank-two masks; on the 21 retained rank-four endpoints it independently
  computes a maximum matching to all rank-five masks.

The reported profiles are

```text
matching 0: lower-good 13, upper-good 3, simultaneous-good 0;
matching 1: lower-good 13, upper-good 3, simultaneous-good 0.
```

Both shores individually attain matching size 21 somewhere, so this is not
a scalar shortage on either shore.  It is exactly failure of the correlated
cyclic block. `square`

### Corollary 2.2 (ordinary hex switching does not preserve the property)

The authenticated positive `ML(7)` cycle in the previous note is connected
to the displayed zero-block cycle by a deterministic sequence of 3,210
accepted incidence-hexagon switches.  Every accepted switch replaces one
alternating matching of an incidence `C_6` by the other and is retained only
when the result is again one 70-vertex cycle.  Therefore existence of a good
cyclic block is not invariant under the standard local Hamilton-cycle switch
relation.

The deterministic walk is not needed for Theorem 2.1; it only prevents a
stronger but false inference that every cycle in the natural hex-switch
component is good.

## 3. Matching-preserving pulls and protected support

Let `F=M union N` be a spanning two-factor of the Middle Levels graph, where
`M,N` are perfect matchings.  Contract the edges of `M`; every component of
`F` becomes a directed cycle on the matched-edge vertices.

An **`M`-preserving pull** is an alternating even cycle `Z` for which

```text
N' = N triangle E(Z)
```

is again a perfect matching.  It replaces only `N`-edges, so `M` is fixed.
Its **contracted support** is the set of `M`-edges incident with the vertices
of `Z`.

Fix `Q subset M` and put `P=M\Q`.  The pull is **`Q`-avoiding** (or
`P`-supported) when its contracted support is contained in `P`.

### Lemma 3.1 (one pull preserves the block literally)

Assume that `Q` is consecutive in one component of `F`.  Every
`Q`-avoiding `M`-preserving pull which leaves a two-factor has the following
properties.

1. `M` and the set `Q` are unchanged.
2. Every `N`-edge incident with a matched-edge vertex of `Q` is unchanged.
3. Hence the internal order of `Q` and its two boundary arcs are unchanged;
   `Q` is still one cyclic interval in its output component.
4. If `Q` was a simultaneous deletion basis before the pull, it remains one
   afterward.

### Proof

Only vertices in the contracted support can have their `N`-incidence
changed.  A `Q`-avoiding pull has no such vertex in `Q`, proving statements
1--3.  Both deletion matroids are pulled back through `M`, and their common
basis is the unchanged set `Q`; statement 4 follows. `square`

The preservation is stronger than palette equality or an average marginal:
the literal matching edges, the literal block order, and both literal block
boundaries survive.

## 4. The protected pull-tree theorem

The standard pull constructions use a family of noninterfering alternating
cycles.  Rather than impose one particular canonical family, state exactly
the property needed here.

### Theorem 4.1 (protected common-basis block gluing)

Let `F_0=M union N_0` be a spanning two-factor.  Suppose:

1. `Q subset M`, `|Q|=c`, is a simultaneous deletion basis;
2. `Q` is one cyclic interval in one component of `F_0`;
3. there is a sequence of `Q`-avoiding `M`-preserving pulls
   `Z_1,...,Z_t` such that after applying the first `j` pulls the result is a
   two-factor with exactly one fewer component than after the first `j-1`;
4. after `Z_t` the factor is connected.

Then the final factor is a Middle Levels Hamilton cycle containing `Q` as a
cyclic-interval simultaneous deletion basis.

### Proof

Induct on the pulls.  Lemma 3.1 preserves the block and both deletion bases
at every step.  Every step lowers the component count by one, and the last
factor is a connected spanning two-regular graph, hence a Hamilton cycle.
`square`

### Corollary 4.2 (auxiliary-tree form)

Suppose a pairwise noninterfering pull family has an auxiliary component
graph in which an edge records a `Q`-avoiding pull that merges its two factor
components.  If this auxiliary graph is connected, any spanning tree gives
the sequence in Theorem 4.1.

This is the exact form in which the Gregor--Mütze--Nummenpalo pull-tree
argument may be used.  The existing theorem that an arbitrary prescribed
forest of canonical pulls extends to a gluing tree applies only after the
following two facts have been proved for the chosen recursive factor:

```text
the desired common basis is already one block;
the canonical pull auxiliary graph remains connected after all pulls
touching that block are forbidden.
```

Theorem 2.1 shows that dropping the first line is invalid.  Theorem 4.1
shows that no further interaction with connectivity is necessary once both
lines hold.

### Corollary 4.3 (additional protected diagonal forests)

Let `K` be any named bank of matched-edge vertices and factor edges which
must survive, for example the pivot collar and the diagonal maps

```text
L -> V=S+(U-L),
S -> K=R+(L-S),
U -> B=L+(W-U)
```

in the four-row-SCD/tight-ear construction.  If every pull in Theorem 4.1
also avoids `K`, then `K` survives literally.  Thus a first-return recursion
may build the short-core block and these maps as path forests first, and use
only complement-supported pulls for the final Hamiltonization.

This corollary is a preservation theorem, not an existence theorem for the
three diagonal path forests.

## 5. Exact construction of the pre-Hamilton block factor

The protected-pull theorem deliberately assumes that the block already
exists.  That assumption has a strictly weaker exact formulation than the
fixed-matching Hamilton-path criterion in the earlier note.

Fix a perfect matching `M`.  Write its edges as

```text
e=(S_e,L_e),  S_e subset L_e,
```

and form the directed contraction graph

```text
H_M: e -> f  iff  S_e subset L_f.                    (5.1)
```

A second perfect matching is exactly a directed cycle cover of `H_M`.

Fix `Q subset M`, put `P=M\Q`, and suppose

```text
q_1 -> q_2 -> ... -> q_c                              (5.2)
```

is a directed Hamilton path in `H_M[Q]`.  Contract (5.2) to one symbol
`star`.  Define the residual bipartite directed graph `K(Q,q_1,q_c)` with
outgoing and incoming shores both `P union {star}` by

```text
p -> p'       iff p -> p' in H_M,
star -> p     iff q_c -> p in H_M,
p -> star     iff p -> q_1 in H_M,                    (5.3)
```

and omit the loop `star -> star`.

### Theorem 5.1 (block-factor criterion)

There is a spanning two-factor `F=M union N` in which `Q` is one nontrivial
cyclic block of one component, with internal order (5.2), if and only if
`K(Q,q_1,q_c)` has a perfect matching.

### Proof

A perfect matching of the two shores of `K` is a permutation cycle cover on
`P union {star}`.  Since the star loop is absent, the cycle containing
`star` also contains at least one member of `P`.  Expand `star` into the path
(5.2).  The two incidences at the star become the unique `P -> Q` and
`Q -> P` boundary arcs, while every other selected incidence lies in `P`.
Together with `M` these arcs are a spanning two-factor and `Q` is one block.

Conversely, contract the `Q` block in any such two-factor.  Its second
matching becomes a permutation cycle cover of `P union {star}` using exactly
the arcs (5.3), hence a perfect matching of `K`. `square`

This replaces the earlier requirement of a Hamilton path through all of
`P`.  The complement is allowed to remain an arbitrary collection of factor
cycles; Theorem 4.1 Hamiltonizes it later.

Equivalently, the pre-Hamilton object consists of

```text
Q: common basis of the two deletion matroids;
R_Q: c-1 arcs, spanning one directed path on Q;
K: one ordinary residual perfect matching;
pulls: a Q-avoiding component gluing tree.             (5.4)
```

The first two rows are a common-basis plus tail/head/graphic correlation.
The third row is ordinary Hall.  The fourth is the only remaining global
topology row.

### Corollary 5.2 (bounded controlled leave)

If `Q` occupies `b` cyclic blocks rather than one, contraction gives `b`
star vertices.  A final short-core path needs at least `b-1`
block-concatenating seams.  Thus a uniform `b=O(1)` controlled leave is an
adequate replacement for the additive-constant programme, provided those
seams carry complete damage tickets.  Exact coefficient-one use of the
short-core funnel still asks for `b=1` (or for `b-1` genuinely free seams).

The automatic common-basis theorem alone gives no bound on `b`.

## 6. What the canonical lexical factor actually supplies

Use the paper parameter `n=m-2`, so the canonical lexical factor lies in
`ML(2n+1)` and the target block size is

```text
c=Cat_(n+1).                                           (6.1)
```

An exact reconstruction from the defining Dyck-rotation map gives the
following component matched-edge sizes.

| `n` | component matched-edge sizes | `c` |
|---:|---|---:|
| 1 | `3` | 2 |
| 2 | `10` | 5 |
| 3 | `21,14` | 14 |
| 4 | `72,36,18` | 42 |
| 5 | `110,110,110,55,55,22` | 132 |
| 6 | `156` (nine times), `78` (three times), `52,26` | 429 |

### Theorem 6.1 (finite protected-block census)

For `n=1,2,3,4`, every cyclic block of length `c` which fits inside one
canonical factor component is a simultaneous deletion basis, for both
matching parities.  The exact good/eligible counts are respectively

```text
6/6, 20/20, 70/70, 144/144.                           (6.2)
```

At `n=5`, no component is long enough, but exactly four unions of whole
canonical components have order `132`, and all four are simultaneous
deletion bases:

```text
{0,5}, {1,5}, {2,5}, {3,4,5}.                        (6.3)
```

At `n=6`, no union of whole components can have order `429`: every canonical
component order is even.  Hence any canonical-factor induction must first
cut through a component at this parameter.

### Proof

The audit in Section 8 reconstructs every factor edge, traverses its literal
components, and tests each stated block or exact-size component union by two
independent maximum containment matchings.  The final `n=6` assertion also
follows immediately from the displayed parity. `square`

The data are strongly positive for first-return recursion: through `n=4`,
the long canonical cycles are *universally* good at the required window
length, and `n=5` has whole-component common bases.  But the simplest
canonical pull finish is false.

### Theorem 6.2 (canonical fixed-matching complement-pull obstruction)

At `n=5`, enumerate all 11,550 incidence hexagons of `ML(11)`.  Exactly 550
are factor-alternating in the canonical factor.  Of these, 176 are
component-reducing and coherent with some fixed alternating perfect matching
`M`.

For each of the four common component unions (6.3) and every one of the 64
componentwise phases of `M`, form the auxiliary hypergraph of
matching-preserving component-reducing hexagons.  The subhypergraph supported
entirely on `P=M\Q` is disconnected in every one of the 256 cases; in fact
its graphic rank is zero in the best row for each union.  Consequently the
canonical factor, a whole-component basis from (6.3), and a one-round
fixed-`M` incidence-hex bank do **not** satisfy Corollary 4.2.

For the three-component basis `{3,4,5}`, one phase does connect the entire
`Q` side (rank two) and has 66 cross-side pulls, but still has no internal
`P` connector.  Thus the missing move is sharply a block-transparent
cross-side/partial-component seam or a noncanonical factor rethread, not
ordinary complement-only canonical gluing.

The theorem does not exclude a matching-changing seam, an intermediate
neutral/split move, a longer compound pull, or a jointly rebuilt factor.

## 7. A bounded block-transparent phase relay

The preceding obstruction fixes the matching too early.  The successful
canonical rethread instead changes matching phase twice and protects the
block only after the terminal matching has been installed.

Contract the edges of a perfect matching `M`.  For a second perfect matching
`N` and `Q subset M`, define the exact boundary current

```text
partial_Q(N)=#{uv in N: exactly one of the two contracted M-vertices is in Q}.
                                                               (7.1)
```

### Lemma 7.1 (two-boundary characterization)

If `M union N` is connected and `Q` is nonempty and proper, then `Q` is one
cyclic interval of matched edges if and only if

```text
partial_Q(N)=2.                                             (7.2)
```

### Proof

Walk around the contracted cycle and write one on a vertex in `Q` and zero
otherwise.  The quantity (7.1) is exactly the number of changes in this
cyclic binary word.  A nonconstant cyclic word has one run of ones exactly
when it has two changes. `square`

For an `M`-preserving alternating pull `Z`, with old and new `N` phases
`Z^-` and `Z^+`, put

```text
Delta_Q(Z)=partial_Q(Z^+)-partial_Q(Z^-).                  (7.3)
```

### Theorem 7.2 (exact phase-relay criterion)

Let `Z_Q,Z_P,Z_X` be pairwise port-disjoint incidence hexagons.  Suppose:

1. toggling the two reset hexagons `Z_Q,Z_P` takes `F_0` to a two-factor
   `F_2=M_* union N_2` containing the named terminal matching `M_*`;
2. `Q subset M_*` is a simultaneous deletion basis;
3. `Z_X` is `M_*`-preserving and is a pure merger of the components it
   meets;
4. after `Z_X` and any subsequent `Q`-avoiding pull tree the factor is
   connected; and
5. the exact current equation holds:

```text
partial_Q(N_2)+Delta_Q(Z_X)=2.                             (7.4)
```

Then the final Hamilton cycle contains `Q` as a cyclic-interval
simultaneous deletion basis.

### Proof

Port disjointness makes the two resets commute and leaves `Z_X` available.
The pull `Z_X` fixes `M_*`, so (7.3) gives the boundary after it.  Every
later `Q`-avoiding pull has zero boundary change by Lemma 3.1.  The terminal
factor is connected by hypothesis 4 and has boundary two by (7.4), so Lemma
7.1 makes `Q` one block.  Its two deletion-basis properties depend only on
`(M_*,Q)` and survive. `square`

### Corollary 7.3 (one-cut component relay)

Suppose after the resets one component has matched-edge set exactly `Q`,
all other components are `Q`-free, and `Z_X` contains exactly one old edge
of the `Q` component.  Then equation (7.4) is automatic: before the pull the
boundary is zero, while the pull opens the `Q` cycle once and creates its two
exterior boundary edges.  This is the literal shape of the authenticated
`ML(11)` relay below.

The reset hexagons need not preserve a block or even the eventual matching:
protection starts only after they install `M_*`.

### The authenticated `ML(11)` relay

Use the canonical lexical factor with six plane-tree components, indexed in
the ECO witness order with matched-edge sizes

```text
22, 55, 55, 110, 110, 110.
```

The three pairwise port-disjoint incidence hexagons are:

| role | Dyck word | original component support |
|---|---|---|
| `Q_RESET` | `11010100` | `{0,5}` |
| `P_RESET` | `11001100` | `{1,3,4}` |
| `CROSS_PULL` | `11001010` | `{2,3,5}` |

Their literal stage profile is

```text
canonical factor:          6 components;
after Q_RESET:             5 components;
after P_RESET:             3 components of matched-edge sizes 132,275,55;
after CROSS_PULL:           1 component.
```

For the final parity-one perfect matching `M_*`, the `132`-edge component
after the two resets is exactly the endpoint bank of original components
`{0,5}`.  It is a simultaneous deletion basis.  The other two components
contain no edge of `Q`.  Relative to `M_*`, the final hexagon has all three
old and all three new edges in `N_*`; it is therefore `M_*`-preserving.  Its
old phase contains one edge from each of the three components, so it is the
pure ternary merger in Theorem 7.2 and Corollary 7.3.

The resulting Hamilton cycle has a much stronger interval census.  For each
matching parity, all `462` starts pass the lower deletion basis, `460` pass
the upper deletion basis, and hence `460` of `462` are simultaneous.  In
particular parity one, start `243`, is exactly the protected component union
`{0,5}` above.

### Next parameter and the scope of padding

The authenticated canonical ECO-path Hamilton cycle at `ML(13)` is again
overwhelmingly positive: for each matching parity, all `1716` blocks pass
the upper deletion basis and `1714` pass the lower deletion basis.  The only
bad starts are `8,9`.  Thus the first forced partial-component parameter has
no cyclic-interval obstruction.

The next authenticated path certificate remains positive at scale.  At
`ML(15)`, exactly `5484` of the `6435` starts are simultaneous for each
matching parity, including start zero.  For the much larger authenticated
certificates at `ML(17),ML(19),ML(21)`, the prescribed start-zero block was
checked exactly and is simultaneous in both parities.  Direct all-start
audits of the smaller ECO cycles give `19/35` simultaneous starts per parity
at `n=3` and `126/126` at `n=4`.  Therefore:

> **Finite selectable-family theorem.**  Every authenticated fixed-rotation
> ECO path certificate for `3<=n<=10` contains a cyclic-interval simultaneous
> deletion basis of order `Cat_(n+1)`.

This identifies the weakest currently viable selectable cycle family.  One
does not seek the property on every Middle Levels cycle.  It is enough to
strengthen the open all-`n` fixed-rotation ECO path conjecture by requiring
one common-basis block; the finite witnesses show no additional obstruction
through the entire audited range.

### Exact reduction inside the canonical ECO recursion

An ECO path certificate selects pairwise port-disjoint incidence hexagons,
so all selected toggles commute.  Fix one alternating perfect matching `M`
of the final Hamilton cycle.  Split the selected atoms into

```text
R = {Z: the new phase of Z contains an edge of M},
P = {Z: neither phase of Z contains an edge of M}.       (7.5)
```

Toggle every atom of `R` first.  Because the atoms are disjoint and the
terminal factor contains `M`, this installs all of `M`; every atom of `P`
is then an `M`-preserving pull.  Write the resulting factor as
`F_R=M union N_R`.

### Theorem 7.4 (weighted ECO relay reduction)

Let `Q subset M` be any simultaneous deletion basis.  The ECO path
certificate produces a Hamilton cycle with `Q` as one block if and only if

```text
partial_Q(N_R) + sum_(Z in P) Delta_Q(Z) = 2.            (7.6)
```

### Proof

The selected atoms commute, and every atom in `P` fixes `M`, so their signed
boundary changes telescope exactly.  The ECO certificate already proves
that the final factor is connected.  Apply Lemma 7.1. `square`

Thus the all-`n` fixed-rotation ECO path conjecture already supplies the
component topology, collision independence and literal Hamiltonization.
The **single additional recursive support condition** is the scalar
two-boundary equation (7.6), with `Q` selected from the automatic common-base
fibre.  No literal padding of one finite relay is required.

For an incidence `C_6`, this scalar has only three values.  Label its six
contracted terminal-matching vertices cyclically by zeros and ones according
to membership in `Q`.  The old and new phases are the two alternating
three-edge matchings.  Each phase has between zero and three crossing edges;
their sum is the number of bit changes around the six-cycle and is even.
Therefore

```text
Delta_Q(Z) in {-2,0,+2}.                                  (7.7)
```

If `p_-` and `p_+` denote the numbers of negative and positive preserving
pulls, (7.6) is the single integer balance

```text
p_- - p_+ = (partial_Q(N_R)-2)/2.                         (7.8)
```

Thus a recursive proof needs no large vector of block states: it must export
one common basis and enough component-merging negative-charge ECO supports
to pay the initial boundary current, with neutral supports free.

There is also an exact fixed-order formulation.  Prescribe `M,Q` and
contract every original vertex through `M`, whether or not the current
factor already contains `M`.  For a selected atom with old/new phases
`Z^-,Z^+`, give it the total weight

```text
w_(M,Q)(Z)=#((Z^+ - M) crossing Q)-#((Z^- - M) crossing Q). (7.9)
```

For every port-disjoint selected bank `S`, literal cancellation gives

```text
partial_Q(N_final)
 = #((F_0-M) crossing Q) + sum_(Z in S) w_(M,Q)(Z).       (7.10)
```

On a fixed ECO component order, binary atoms are one-step arcs and ternary
atoms are two-step arcs in the integral path-tiling DAG.  Therefore, after
restricting to certificates whose terminal factor contains `M`, the relay
row is exactly one prescribed-weight source--sink path condition in that
DAG.  It is decidable by ordinary dynamic programming.  The all-`n` proof
must show that the recursive faithful/collision-phase bank retains a path of
weight `2-#((F_0-M) crossing Q)`.  This is the promised single recursive
support condition; all topology and resource rows are those of the existing
ECO path conjecture.

The exact relay-signature audit confirms the reduction on the start-zero
bases at the first four nontrivial path witnesses:

| `n` | reset atoms | preserving pulls | components after resets | boundary current |
|---:|---:|---:|---:|---:|
| 5 | 2 | 1 | 3 | `4-2=2` |
| 6 | 7 | 1 | 3 | `4-2=2` |
| 7 | 25 | 1 | 3 | `4-2=2` |
| 8 | 43 | 18 | 37 | `14-12=2` |

At `n=8`, the eighteen preserving pulls are a literal pure-merger chain

```text
37,35,33,...,3,1;
```

six pulls have boundary charge `-2` and twelve have charge zero.  This is
the first finite example where the relay is genuinely reselected and
distributed rather than one padded three-hex gadget.  It is also why the
correct induction target is (7.6), not a constant list of Dyck words.

The literal symmetric zero-padding of the three `ML(11)` Dyck words is not
the recursion.  At `n=6,7,8` the three padded hexagons merely change the
component counts

```text
14 -> 13 -> 12 -> 11,
34 -> 33 -> 32 -> 31,
95 -> 94 -> 93 -> 92,
```

and the third pull is not coherent with one alternating terminal matching.
This refutes only the naive three-word padding, not a bounded recursive phase
relay with reselected hexagons.

## 8. Mechanical audit

The independent literal checker is

```text
scratch/audit_short_core_ml7_zero_interval.cpp
SHA256 4c56151a01248b4da71738127c04b6649e02e0a510ea9145603a38163b8187c0
```

It was compiled and run on `ssh h100` with

```text
g++ -std=c++20 -O3 -DNDEBUG
```

and produced

```text
scratch/short_core_ml7_zero_interval_20260801.audit.json
SHA256 8e4fc0da3d1ba7a70ed40cae4d8405f96fad0e33e98a3ab98dc8e3ec9a04b245
```

with status `PASS_LITERAL_ML7_ZERO_INTERVAL`.

The deterministic incidence-hex walk is

```text
scratch/audit_random_ml7_interval_basis.cpp
SHA256 7e77a675151d516082ba934e2265333dd21cd775efb4e70dad13831780fd13e9
```

and uses seed one.  It accepts 3,210 Hamilton-to-Hamilton toggles before
reaching the frozen cycle above.

The canonical protected-block census is

```text
scratch/audit_canonical_factor_protected_block_20260801.py
SHA256 8803a22cc8f0d4c4a39f1be2b0a9c879afd0de95772e09a32bf8bfa9d33e270e

scratch/canonical_factor_protected_block_20260801.audit.json
SHA256 4f0f8d126ebfac718c62501c74d8e9166a8a5eab4fc22628af2427fe9149c7cb
```

The full-hex protected-auxiliary census is

```text
scratch/audit_canonical_n5_fullhex_protected_auxiliary_20260801.py
SHA256 510459e9b278f9899851fbe4d680c089fd39b1b7859142ae249b6b45dac715a5

scratch/canonical_n5_fullhex_protected_auxiliary_20260801.audit.json
SHA256 60e832657b81c9a6f51f56b85718e68a0de5727949534edbbec4b58bc41e7a7b
```

Both were run on `ssh h100`; the block census uses exact augmenting-path
matchings, and the auxiliary census enumerates every incidence `C_6`, not
only the fixed-rotation ECO subfamily.

The exact three-hex relay is frozen by

```text
scratch/audit_canonical_n5_three_hex_phase_relay_20260801.py
SHA256 b074d9fab2bf539de5ea827a52b275f161d63d730551d248aee13f91ea86cb88

scratch/canonical_n5_three_hex_phase_relay_20260801.audit.json
SHA256 fadf40d6a6c88ab1a80d240e44c9c647a2c8936879accfba3368433ee9fbd190
```

with status `PASS_CANONICAL_N5_THREE_HEX_PHASE_RELAY`.  The extracted cycle
and its interval census are

```text
scratch/canonical_n5_eco_path_cycle_20260801.json
SHA256 878399c76821078c71926f0f4040a2ea7aeaa50bbf4219dd8c163369c2d1d16e

scratch/canonical_n5_eco_interval_20260801.audit.json
SHA256 0a612f23d9e0f9abed4aaf9cd32a109a66d61e14087bfdf4e86098611919ca13
```

The `ML(13)` reconstruction and exact all-start census are

```text
scratch/extract_canonical_n6_eco_path_cycle_20260801.py
SHA256 7943d6224c7a21fa581bd5a193865578ba3315d7b74c1615e8ad61a20afb5f6b

scratch/audit_short_core_canonical_n6_eco_cycle_20260801.cpp
SHA256 8f703ba0481a40f5d9b417ebb26864c441d62ff6e340859638977738ea8215cb

scratch/canonical_n6_eco_path_cycle_20260801.json
SHA256 97bb39f5ac061cd941ef0740dbc940a156a2a3df9b1a4fa441abf30e0c402322

scratch/canonical_n6_eco_interval_20260801.audit.json
SHA256 13dbc175a14dfd79269f959d989ab160a0c78a81734c69d6e282440d2504171f
```

The bounded-padding scout is

```text
scratch/audit_padded_three_hex_phase_relay_scout_20260801.py
SHA256 08b169378ed0ea6fd9da671b85217ae652a1cb69c8eaf9c7a9533a8290a01396

scratch/padded_three_hex_phase_relay_scout_20260801.audit.json
SHA256 c1c838c3e3f882ff43ba10fade7c2f80bd429913503e43dd7e03833a665cb896
```

The generic ECO-cycle extractor and sparse Hopcroft--Karp interval checker
are

```text
scratch/extract_canonical_eco_path_cycle_param_20260801.py
SHA256 fc974c745ffd513fc873da3a3e30063b5d79e0f6525b0552ea08a8fdd5a87ca3

scratch/audit_short_core_eco_cycle_fast_20260801.cpp
SHA256 7b6e1cc5fdab55272d2efed7f4ae700163b6ab3164fb3c9d54f304369dd36bc0
```

Their additional exact outputs are

```text
scratch/canonical_n3_eco_interval_20260801.audit.json
SHA256 ab8a7866da9821e9b07d460e7a7857c30f7286cdc25787b43c8e79d539233048

scratch/canonical_n4_eco_interval_20260801.audit.json
SHA256 07ed5c17987169a4b2b3526c81c54de1a4c0c7d24fd5856feec0dad79fcb08a3

scratch/canonical_n7_eco_interval_20260801.audit.json
SHA256 ed0f8dff7fdbc200d32d146fc3a43e39e9ba07c86e75842f4a1ace0209a1c15e

scratch/canonical_n8_eco_interval_start0_20260801.audit.json
SHA256 b52574039519ce9a38ddb4c1c54f343e4a66884a30615ccb6b7440eb6dd8f939

scratch/canonical_n9_eco_interval_start0_20260801.audit.json
SHA256 a438f67010d0f43008358cfe1b29828cbac22f197f7af06af3e27b03179e5d81

scratch/canonical_n10_eco_interval_start0_20260801.audit.json
SHA256 9ea868199de13664ad026fc1f2c72515337653e8f93c165a1a4c1b0556f31897
```

The reset/preserving split and exact boundary-current telescope are checked
by

```text
scratch/audit_eco_interval_relay_signature_20260801.py
SHA256 2a12386e1539d4024331d08481cda0371a1fade9904fefdcaf13744ec326a23a

scratch/eco_interval_relay_signature_20260801.audit.json
SHA256 7b016ed9ee5ee52e74564f379fae1aa76a8b5c900f382f371761164fe2fadf29
```

with status `PASS_ECO_INTERVAL_RELAY_SIGNATURE`.

Every construction and census in this section was run on `ssh h100`; the
all-start `ML(13),ML(15)` matching censuses and the prescribed-start checks
through `ML(21)` used the `-O3 -DNDEBUG` C++ checker.

## 9. Revised exact frontier

The short-core rows are now separated as follows.

```text
ordinary simultaneous deletion basis for every fixed M: automatic;
cyclic interval in an arbitrary ML Hamilton cycle:     false at ML(7);
invariance under ordinary incidence-hex switching:     false at ML(7);
block preservation under complement-supported pulls:   exact;
Hamiltonization from a protected pull tree:             exact;
pre-Hamilton block factor via path + residual Hall:      exact;
canonical block evidence through n=5:                    positive;
canonical fixed-M complement pull tree at n=5:           false;
bounded matching-changing phase relay at n=5:           exact;
canonical ECO interval bank at n=6:                     1714/1716 per parity;
selectable ECO interval through n=10:                   exact finite;
boundary-current relay reduction:                       exact;
literal zero-padding of the n=5 relay:                  false at n=6;
all-n weighted protected ECO relay:                     open.
```

Accordingly the weakest clean recursive target is:

> **Weighted protected ECO relay lemma.**  For every sufficiently large `m`,
> choose a fixed-rotation ECO path certificate, one of its terminal matching
> parities `M`, and a common deletion basis `Q`.  After toggling the reset
> atoms first, require the preserving atoms to satisfy the sole additional
> support equation
>
> ```text
> partial_Q(N_R)+sum Delta_Q(Z)=2.
> ```
>
> If the owner construction needs the SCD diagonal maps or a pivot collar,
> include them in the same protected resource bank.

Theorem 4.1 then supplies the required Hamilton cycle without ever asking an
arbitrary common basis to become intervalizable and without asking a generic
Hamilton-cycle switch to preserve the block.

The `n=5` relay proves that two matching resets followed by one protected
cross pull are sufficient in the smallest nontrivial state.  The `n=8`
signature proves that the same invariant can be distributed over a longer
reselected pure-merger chain.  What remains is an all-`n` recursion for the
weighted support equation, not a literal padding of three finite words.  It
should be audited against this boundary-current state, not against a
cycle-blind cyclic-interval conjecture and not against a whole-component
union forever.
