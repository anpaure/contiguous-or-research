# Thread D: exact one-copy age-orbit rounding at `k=17`

Date: 2026-08-01  
Status: exact quotient arithmetic, exact connected type assignment, and an
exact TU reduction for the literal age-partition lift after a quotient owner
cycle is fixed.  The rank-2 through rank-7 coloured suffix constraints remain
a coupled path-transversal gate.  No `k=17` word is claimed.

## 0. Outcome

For

\[
 k=17,\qquad r=9,\qquad d=3,\qquad
 W={17\choose9}=17\cdot1430,                         \tag{0.1}
\]

the denominator `1430` of the exact age-composition certificate is exactly
the number of free rank-nine owner necklaces.  Hence one certificate unit
can be assigned to one owner necklace, and its 17 translates select exactly
one trace for each of the 24310 literal owners.

There are three logically different conclusions.

1. The displayed pre-splice 14-entry type-arc ledger in the certificate note
   does **not** form one cyclic type word.  Type `(4,3,1,1)` is an isolated
   140-loop component.  It does form an abstract two-component successor
   permutation.  This 14-entry ledger is reconstructed by undoing the frozen
   splice; it is not a separately frozen TSV artifact.
2. The frozen word
   `scratch/k17_age_type_euler_word_20260801.tsv` replaces one loop at
   `(4,3,1,1)` and one loop at `(6,1,1,1)` by the two cross-arcs.  Its
   16 positive arc types are legal, balanced and strongly connected.  It is
   one Euler word of length 1430 with the exact nine stationary type counts.
3. Merino--Mička--Mütze supply a unit-voltage 1430-cycle of rank-nine owner
   necklaces whose physical lift is a lower-rainbow Johnson Hamilton cycle.
   The frozen type word can therefore be written around an actual quotient
   owner factor with no divisibility, type-count or type-Euler obstruction.

The remaining literal-age problem is not another integer-rounding problem.
After the owner cycle, type word and one root partition are fixed, compatible
age partitions are exactly a unit path in a layered directed network.  Its
matrix is a network matrix and is integral.  The genuinely non-TU rows are
the simultaneous all-different suffix-target necklaces at ranks 2 through 7.
Rank 8 is already the lower Johnson colour and is automatic on the MMM
factor.

## 1. Free owner orbits and the certificate scale

Let `rho` be coordinate rotation on `Z_17`.

### Lemma 1.1 (free action)

Every nonempty proper subset of `Z_17` has a free `Z_17` orbit.

#### Proof

A nonidentity rotation is a 17-cycle.  An invariant subset is a union of its
ground orbits, hence is empty or all of `Z_17`.  `square`

Consequently there are

\[
 {1\over17}{17\choose9}=1430                         \tag{1.1}
\]

owner necklaces, and `binom(17,s)/17` target necklaces at every rank
`1<=s<=16`.

Use the nine certified types

\[
\begin{array}{c|c|r}
i&c_i&n_i\\\hline
0&(1,5,2,1)&139\\
1&(1,6,1,1)&297\\
2&(2,5,1,1)&8\\
3&(3,3,2,1)&20\\
4&(3,4,1,1)&20\\
5&(4,3,1,1)&140\\
6&(5,1,2,1)&127\\
7&(5,2,1,1)&237\\
8&(6,1,1,1)&442 .
\end{array}                                           \tag{1.2}
\]

Their total is 1430.  All have final age class one.  A decorated object has
no smaller orbit, since its stabilizer would stabilize its owner.

## 2. Exact type-Euler ledger

An age transition `c->c'` is legal when

\[
                         c'_{j+1}\le c_j
                         \quad(0\le j<3).             \tag{2.1}
\]

Undoing the authoritative TSV splice gives the displayed pre-splice ledger
with 14 positive ordered type pairs.  Its exact cut is

\[
 a_{55}=140,\qquad a_{5j}=a_{j5}=0\quad(j\ne5).       \tag{2.2}
\]

Thus `{c_5}` and the other eight types are two support components.  Equal
row and column sums give a successor permutation, but no single cyclic
successor word.

The authoritative frozen word uses the loop splice

\[
\begin{aligned}
 &(c_5,c_5),(c_8,c_8)\\
 &\hspace{20mm}\longmapsto(c_5,c_8),(c_8,c_5) .       \tag{2.3}
\end{aligned}
\]

Both cross-arcs are legal:

\[
 (1,1,1)\le(4,3,1),\qquad
 (3,1,1)\le(6,1,1).                                  \tag{2.4}
\]

The switch preserves every row sum and column sum.  It joins the isolated
type to the former eight-type component, so the repaired multigraph is
strongly connected and Eulerian.

### Theorem 2.1 (type word on any owner cycle)

Let `O_0,...,O_(1429)` be any cyclic ordering of the 1430 owner necklaces.
Assign to `O_i` the type on row `i` of the frozen word.  Then:

* every type occurs exactly `n_i` times;
* every consecutive ordered type pair has its repaired prescribed count;
* every consecutive type transition is legal; and
* the cyclic word has one component.

#### Proof

The TSV is a Hierholzer ordering of the repaired integer multigraph.
Reading its successive arc tails around any prescribed cycle gives the
claim.  This is also the standard fact that a connected balanced directed
multigraph has an Euler circuit. `square`

This theorem is about colouring positions of an owner cycle.  It does not
yet choose compatible literal age partitions.

## 3. The quotient owner factor is unconditional

The rotational middle-levels theorem, in the exact projected form recorded
in
`MATH_MERINO_MICKA_MUTZE_STRICT_SPIRAL_PROJECTION_20260729.md`,
gives a quotient Johnson cycle

\[
                         O_0,O_1,\ldots,O_{1429}       \tag{3.1}
\]

with a prescribed unit voltage `v in Z_17`.  Its lift visits every rank-nine
owner once, and the adjacent intersections are every rank-eight set once.

Choose gauge representatives `T_i in O_i` so that

\[
 T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\}
 \quad(0\le i<1430),\qquad
 T_{1430}=\rho^vT_0.                                 \tag{3.2}
\]

Apply Theorem 2.1 to (3.1).  This proves:

### Corollary 3.1 (abstract coloured owner-factor realization)

The repaired certificate counts are realized exactly on a unit-voltage,
lower-rainbow quotient owner cycle.  There is one certified age type per
owner necklace and one legal certified type transition per quotient Johnson
edge.

The reconstructed pre-splice 14-entry matrix cannot be used on this one
cycle because of (2.2).  It is realizable only as a disconnected type
successor permutation.  The frozen TSV uses exactly the `c_5`--`c_8` switch
(2.3); a different legal repair recorded elsewhere is not used here.

## 4. Exact literal partition-state automaton

Write the frozen type at position `i` as

\[
                         c_i=(c_{i,0},c_{i,1},c_{i,2},1).
\]

Define layer `P_i` to consist of ordered partitions

\[
 P=(C_0,C_1,C_2,C_3),\qquad
 T_i=C_0\mathbin{\dot\cup}C_1\mathbin{\dot\cup}C_2
             \mathbin{\dot\cup}C_3,                 \tag{4.1}
\]

with `|C_j|=c_(i,j)` and

\[
                         C_3=\{\alpha_i\}.            \tag{4.2}
\]

For `P in P_i` and `P' in P_(i+1)`, put `P=>P'` exactly when

\[
                         C'_{j+1}\subseteq C_j
                         \quad(0\le j<3).             \tag{4.3}
\]

The wrap layer is interpreted equivariantly:

\[
                         P_{1430}=\rho^vP_0.          \tag{4.4}
\]

Condition (4.3), the two owner sets in (3.2), and (4.2) imply the exact
newborn-class identity

\[
 C'_0=\{\beta_i\}\cup
       \bigcup_{j=0}^2(C_j-C'_{j+1}).                \tag{4.5}
\]

Thus no extra local source equation is missing.

### Theorem 4.1 (partition-path equivalence)

The type-coloured quotient owner cycle has an equivariant literal
one-trace-per-owner age lift if and only if there are

\[
                         P_i\in\mathcal P_i
                         \quad(0\le i<1430)           \tag{4.6}
\]

such that `P_i=>P_(i+1)` at every layer and the equivariant closure (4.4)
holds.

When (4.6) exists, developing it under `rho` gives:

1. exactly one literal trace for every rank-nine owner;
2. exact order-three de Bruijn state balance;
3. one connected physical trace cycle, because `v` is a unit modulo 17; and
4. cyclic coordinate residence at least four.

#### Proof

A literal trace window determines its last-occurrence partition.  Shifting
the window moves every survivor of age `j` into age `j+1`, deletes the
unique age-three element `alpha_i`, and places `beta_i` and every refreshed
survivor into age zero.  These are precisely (4.2)--(4.5), proving
necessity.

Conversely, (4.3)--(4.5) spell one legal nonempty next source letter.
Consecutive windows have identical overlapping order-three state.  Equation
(4.4) allows the 17 translates to concatenate, and unit voltage makes their
lift one cycle.  A newborn coordinate starts in `C_0` and can reach the
deleted class `C_3` only after three further transitions; refreshes delay
rather than shorten this time.  Hence every positive run has length at
least four. `square`

### Corollary 4.2 (TU after fixing the root)

Fix `P_0 in P_0`.  Make the time-expanded digraph with the layers
`P_0,...,P_1430`, the arcs (4.3), source `P_0` and sink `rho^vP_0`.
Existence of the literal lift is a unit source--sink flow.  The matrix is a
directed node--arc incidence matrix, so every feasible fractional flow has
an integral path.

Allowing several boundary roots is a finite disjoint union of these
networks.  Comparator/root pins may delete allowed sources, sinks or
transitions without changing integrality.  An adjacent same-guard
comparator passage still needs its separately declared boundary sidecar;
the age quotient does not repair its two-traces-one-owner obstruction.

The layer sizes are small and exact:

\[
 |\mathcal P_i|
 ={8!\over c_{i,0}!\,c_{i,1}!\,c_{i,2}!}\le560.       \tag{4.7}
\]

For the frozen word the total number of layer states is 183232.  Hence the
uncoloured partition lift is a polynomial-size reachability problem, not a
large integer programme.

## 5. The exact suffix-colour rows

For `P_i=(C^i_0,C^i_1,C^i_2,C^i_3)`, its available marked suffix values are

\[
 S_{i,j}=C^i_0\cup\cdots\cup C^i_{j-1}
 \quad(1\le j\le3),                                  \tag{5.1}
\]

whenever their ranks are below nine.  The frozen type counts give:

\[
\begin{array}{c|rrrrrrrr}
s&1&2&3&4&5&6&7&8\\\hline
\text{available slots}&436&8&40&140&364&728&1144&1430\\
\text{target necklaces}&1&8&40&140&364&728&1144&1430 .
\end{array}                                           \tag{5.2}
\]

Thus every available slot at ranks `2,...,8` is forced to be used.  Exact
coverage at one of these ranks is equivalent simply to pairwise
distinctness of the corresponding target necklaces.

At rank eight,

\[
 S_{i,3}=T_i-C^i_3=T_i-\{\alpha_i\}
                    =T_i\cap T_{i+1}.                \tag{5.3}
\]

The MMM owner factor is lower-rainbow, so the 1430 rank-eight target
necklaces are automatically distinct.  At rank one, any one of the 436
available singleton slots covers the unique singleton necklace.

The exact unsolved colour condition is therefore

\[
 \boxed{\text{the selected partition path makes every }S_{i,j}
        \text{ at ranks }2,\ldots,7\text{ orbit-distinct}.}      \tag{5.4}
\]

These rows couple choices in different layers and different ranks.  They
are not part of the network matrix in Corollary 4.2.

## 6. Coloured quotient master and its lattice

Before the owner cycle and type word are fixed, a decorated packet orbit
`p` has the signature

\[
 \sigma(p)=
 \bigl(
 {\bf1}_{o(p)},\
 {\bf1}_{a(p)},\
 {\bf1}_{h(p)}-{\bf1}_{t(p)},\
 ({\bf1}_{S_s(p)})_{s=1}^8,\
 \omega(p)
 \bigr).                                             \tag{6.1}
\]

The coordinates record owner necklace, certified type-arc class, quotient
state boundary, actual target necklaces, and voltage.  The exact
one-copy equations are

\[
\begin{aligned}
 &x(\mathcal E_o)=1 &&(o\text{ an owner necklace}),\\
 &x(\mathcal E_a)=m_a &&(a\text{ a certified type arc}),\\
 &\partial x=0,\\
 &x(\mathcal E_{s,Q})=1 &&(2\le s\le8,\ Q\text{ a target necklace}),\\
 &x\in\{0,1\}^{\mathcal E},
\end{aligned}                                        \tag{6.2}
\]

plus connected support and nonzero total voltage.  Rank one needs one
selected available slot, not 436 distinct colours.

Equations (6.1)--(6.2) give the exact additive/lattice gate:
the required vector must belong to the degree-one Minkowski sum of packet
signature sets, and every finite character of the corresponding difference
lattice is a proof-safe modular obstruction.  The type count projection has
no remaining obstruction after (2.3).  Fixing the MMM cycle and the type
word turns the state part into the TU path network of Section 4.  What
remains is precisely the coloured path-transversal (5.4).

A cheap necessary separator follows by deleting the transition arcs.  For a
rank `s` and a set `I` of eligible positions, let `N_s(I)` be the target
necklaces obtainable from partition states which survive forward/backward
reachability pruning.  Then

\[
                         |N_s(I)|\ge|I|               \tag{6.3}
\]

is necessary.  These rankwise Hall cuts are not sufficient: one partition
choice simultaneously fixes up to three ranks and must lie on one common
path.

## 7. Exact verdict and next finite gate

The denominator bridge is real and useful.

* **Closed:** owner-orbit divisibility and stabilizers.
* **Closed:** exact stationary type counts.
* **Closed after the frozen switch:** one connected 1430-position type word.
* **Closed unconditionally:** a unit-voltage, lower-rainbow quotient owner
  cycle on which that word can be placed.
* **Integral once the root is fixed:** the uncoloured literal
  partition-state lift.
* **Automatic:** rank-eight target necklaces, owner exactness, trace-state
  balance, connected lift and depth-three residence, conditional on a
  partition path.
* **Open:** existence of a partition path satisfying the simultaneous
  rank-2 through rank-7 orbit-distinct rows, followed by an upper-safe
  opening and the literal terminal compiler.

Accordingly, the next proof-safe computation is not a generic owner SAT.
It is:

1. materialize one MMM quotient owner cycle with its edge voltages;
2. build the 183232-state layered automaton for the frozen type word;
3. prune it by forward/backward reachability;
4. separate the six rankwise Hall systems; and
5. solve the remaining common coloured path, retaining one root and the
   unit-voltage closure.

Any failure before Step 4 is an exact network reachability obstruction.
Any failure at Step 4 is an exact target-orbit Hall cut.  Resource or time
exhaustion is only `UNKNOWN`.

## 8. Independent audit

The lightweight checker

`scratch/audit_threadD_k17_age_orbit_quotient_lattice_20260801.py`

independently parses the frozen 1430-row type word and verifies:

* all type and transition counts;
* legality of every transition;
* the reconstructed pre-splice 14-entry two-component cut;
* the repaired 16-entry strong connectivity;
* the complete rank-capacity/target-orbit table; and
* the exact layer-state counts, including the maximum 560.

Its payload is

`scratch/threadD_k17_age_orbit_quotient_lattice_20260801.audit.json`,

with status

`PASS_K17_AGE_ORBIT_TYPE_EULER_AND_LATTICE_AUDIT`.

No heavy local computation was used.
