# Thread D: Boolean suffix rectangularization and the `k=17` MMM run-four cut

Date: 2026-08-01  
Status: exact local rectangularization, a genuine TU coloured-completion
face, saturation of the independent-layer colour lattice, and a
solver-free obstruction for the frozen shift-one MMM owner cycle.  The
obstruction does not apply to every rotational middle-levels cycle or to a
different age certificate.  No `k=17` word is claimed.

## 0. Outcome

Rebase on the exact one-copy quotient reduction in
`MATH_THEOREM_THREAD_D_K17_AGE_ORBIT_ONECOPY_QUOTIENT_LIFT_20260801.md`.
There are six tight suffix rows, at ranks `2,...,7`, after rank eight is
identified with the lower Johnson colour.

Four facts sharpen that gate.

1. With the two neighbouring age partitions fixed, the complete menu of an
   intermediate state is exactly a Cartesian product of two uniform-matroid
   base intervals.  One factor changes only the first suffix; the other
   changes the first and second suffix by the same Boolean exchange.
2. On cyclically nonadjacent layers, the first factor gives an exact
   bipartite Hall problem and hence a TU integral completion face.  It can
   repair first-suffix ranks `2,...,6`.  It cannot change any rank-seven
   colour: all 1144 rank-seven slots are second suffixes.
   In fact rank seven is completely determined by the owner cycle: its
   colour is the intersection of three consecutive owners.
3. Before path reachability is imposed, the complete flag-signature lattice
   is saturated.  There is no parity or finite Smith obstruction hidden in
   the six colour marginals themselves.  Only component totals, equivalently
   ordinary Hall/equality cuts, survive at that relaxation.
4. The canonical frozen shift-one MMM cycle cannot carry the certified age
   multiset at all.  Its 1430 quotient coordinate runs contain only 132 runs
   of length exactly four, whereas the 436 occurrences with `c_0=1` each
   force a distinct length-four run.  The deficit is 304 before any coloured
   suffix row is considered.  For the particular frozen Euler order, every
   relative cyclic alignment fails at least 372 of the 436 equations in the
   forward orientation and at least 381 in the reverse orientation.
   Independently, its native triple-owner bank contains only 1001 of the
   1144 required rank-seven target orbits.

Thus a Boolean-specific TU face exists, and the abstract colour lattice is
benign, but the canonical MMM/type input is obstructed one level earlier.
The live route must jointly change the lower-rainbow owner cycle (or the age
certificate) and then solve a genuinely colour-transferring second-shore
path problem.

## 1. Literal age notation

Let three consecutive rank-nine owner states carry age partitions

\[
 A=(A_0,A_1,A_2,A_3),\qquad
 Q=(Q_0,Q_1,Q_2,Q_3),\qquad
 D=(D_0,D_1,D_2,D_3).                               \tag{1.1}
\]

The first Johnson edge deletes the singleton `A_3` and inserts `beta`; the
second deletes the fixed singleton

\[
                         Q_3=\{\alpha\}.             \tag{1.2}
\]

Write the prescribed type of `Q` as

\[
                         c=(c_0,c_1,c_2,1).           \tag{1.3}
\]

Literal compatibility is

\[
 Q_{j+1}\subseteq A_j,\qquad
 D_{j+1}\subseteq Q_j\qquad(0\le j<3),              \tag{1.4}
\]

together with the newborn identity

\[
 Q_0=\{\beta\}\mathbin{\dot\cup}
       (A_0-Q_1)\mathbin{\dot\cup}
       (A_1-Q_2)\mathbin{\dot\cup}
       (A_2-Q_3).                                    \tag{1.5}
\]

Its proper suffixes are

\[
 S_1(Q)=Q_0,\qquad S_2(Q)=Q_0\cup Q_1,\qquad
 S_3(Q)=Q_0\cup Q_1\cup Q_2.                        \tag{1.6}
\]

For the certified types, `|S_2|` is six or seven and `|S_3|=8`.

## 2. Exact fixed-neighbour rectangle

Assume the fixed data in Section 1 admit at least one intermediate state.
Define

\[
 \begin{split}
 \mathcal B_1&=\{X:D_2\subseteq X\subseteq A_0-D_1,
                         \ |X|=c_1\},\\
 \mathcal B_2&=\{Y:D_3\subseteq Y\subseteq A_1-D_1,
                         \ |Y|=c_2\}.
 \end{split}                                        \tag{2.1}
\]

### Theorem 2.1 (uniform-base product)

The map `Q -> (Q_1,Q_2)` is a bijection from the complete fixed-neighbour
fibre onto

\[
                         \mathcal B_1\times\mathcal B_2. \tag{2.2}
\]

For `(X,Y)` in (2.2), the inverse is

\[
 \begin{split}
 Q_1&=X,\qquad Q_2=Y,\qquad Q_3=\{\alpha\},\\
 Q_0&=\{\beta\}\mathbin{\dot\cup}(A_0-X)
          \mathbin{\dot\cup}(A_1-Y)
          \mathbin{\dot\cup}(A_2-\{\alpha\}).
 \end{split}                                        \tag{2.3}
\]

#### Proof

The first half of (1.4) gives `Q_1 subset A_0`, `Q_2 subset A_1` and
`Q_3 subset A_2`.  The second half gives `D_2 subset Q_1` and
`D_3 subset Q_2`.  Since `D_1 subset Q_0` and the four `Q` classes are
disjoint, neither `Q_1` nor `Q_2` may meet `D_1`.  Hence every intermediate
state maps into (2.1).

Conversely, (2.3) is the literal update from `A`; the fixed feasibility
assumption handles the conditions involving `D_1`, `beta` and `Q_3` which
do not depend on `X,Y`.  The two lower containments in (2.1) give
`D_2 subset Q_1` and `D_3 subset Q_2`, and the exclusions by `D_1` give
`D_1 subset Q_0`.  Thus (1.4) holds in both directions.  The sizes in
(2.1), together with the legal type transitions, make `|Q_0|=c_0`.
The constructions are inverse.  `square`

Each `mathcal B_j` is the base family of a uniform matroid after a fixed
lower set is contracted and a fixed forbidden set deleted.  Its
one-element-exchange graph is connected.

### Corollary 2.2 (triangular colour action)

On the fibre (2.2),

\[
 \begin{split}
 S_1(Q)&=Q_0,\\
 S_2(Q)&=\{\beta\}\cup A_0\cup(A_1-Q_2)
                           \cup(A_2-Q_3),\\
 S_3(Q)&=T_i-\{\alpha\}.
 \end{split}                                        \tag{2.4}
\]

Consequently:

* a one-element exchange in `Q_1` changes only `S_1`;
* a one-element exchange in `Q_2` changes `S_1` and `S_2` by the same
  exchanged pair; and
* `S_3`, the owner, the type and the age-three residence state are fixed.

This is the exact triangular local actuator.  It is stronger than a scalar
degree statement and weaker than a palette-transparent trade.

## 3. A genuine TU coloured-completion face

Fix a cyclic compatible partition path `P`.  Let `I` be a set of layers no
two of which are adjacent cyclically, and suppose none is a protected pin.
At every `i in I`, fix the two neighbouring states and fix `Q_2,Q_3`, but
allow `Q_1` to range over its family `mathcal B_1` in Theorem 2.1.  Since
the active layers are nonadjacent, these choices are independent and every
choice remains one literal partition path.

For a rank `s`, delete the target orbits already occupied by inactive
rank-`s` first suffixes.  Make a bipartite graph whose left vertices are the
active layers with `c_0=s`, whose right vertices are the residual rank-`s`
target orbits, and whose edges are the orbits obtainable by a `Q_1` choice.

### Theorem 3.1 (separated first-shore Hall theorem)

Assume the inactive first-suffix orbits are pairwise distinct and the two
shores above have equal size at each rank.  The separated face completes
all active first-suffix colours exactly if and only if

\[
                         |N(X)|\ge |X|                \tag{3.1}
\]

for every set `X` of active layers, rank by rank.

Moreover, the completion polytope is integral: its matrix is the direct sum
of bipartite assignment matrices.

#### Proof

Corollary 2.2 says the active choice at one layer changes only its first
suffix, and nonadjacency says it changes no other active fibre.  Hence the
global feasible set is exactly the product of the displayed bipartite
matching systems.  Hall gives (3.1), and bipartite matching matrices are
TU.  `square`

The exact scope by rank is important:

\[
\begin{array}{c|c|c}
\text{rank}&\text{first-suffix slots}&\text{second-suffix slots}\\ \hline
2&8&0\\
3&40&0\\
4&140&0\\
5&364&0\\
6&442&286\\
7&0&1144.
\end{array}                                         \tag{3.2}
\]

Thus the theorem supplies a real integral face for every rank-two through
rank-five slot and for the 442 first-shore rank-six slots whenever a
suitable nonadjacent active family is available.  It does not solve the 286
second-shore rank-six slots or any rank-seven slot.

### Proposition 3.2 (rank seven is a native owner-cycle row)

At every rank-seven slot, `c_2=1`.  The next deletion label satisfies

\[
                         \{\alpha_{i+1}\}\subseteq Q_{i,2}. \tag{3.3}
\]

Both sides are singletons, and therefore

\[
 \begin{split}
 S_2(Q_i)
   &=S_3(Q_i)-\{\alpha_{i+1}\}\\
   &=T_i\cap T_{i+1}\cap T_{i+2}.                  \tag{3.4}
 \end{split}
\]

Hence no partition-state choice changes a rank-seven suffix.  A necessary
condition for any placement of the certified types on a fixed owner cycle
is that its three-consecutive-owner intersections contain all 1144
rank-seven target necklaces.  For a fixed type word, the 1144 positions
carrying rank-seven types must themselves give the bijection.

#### Proof

The survivor rule puts the next state's oldest singleton inside the current
age-two class.  Every type whose second suffix has rank seven has age-two
class size one, proving equality in (3.3).  Since `S_3` is the intersection
of the first two owners and the next Johnson edge deletes
`alpha_(i+1)`, (3.4) follows.  `square`

If `Q_1` is fixed and `Q_2` varies, the choice generally has both an inner
and an outer colour and is a three-partite matching, not a network matrix.
It reduces to Theorem 3.1 only under an additional checked alignment: the
map from every outer option `S_2` to its inner option `S_1` must be one
common injection `theta`, and the required inner residual set must be the
`theta`-image of the required outer residual set.  Without that hypothesis,
no TU conclusion is valid.

## 4. The independent-layer colour lattice is saturated

Fix an eight-set `L` and integers `1<=a<b<8`.  Let

\[
 \mathcal F_{a,b}(L)=\{(X,Y):X\subset Y\subset L,
                            |X|=a,\ |Y|=b\}.         \tag{4.1}
\]

Associate the signature `e_X+e_Y` to a flag.  Let
`A(Omega)` denote the zero-sum root lattice on a finite set `Omega`.

### Theorem 4.1 (saturated two-shore flag lattice)

The lattice generated by all differences of signatures in (4.1) is

\[
 A\!\left({L\choose a}\right)\oplus
 A\!\left({L\choose b}\right).                     \tag{4.2}
\]

After the rank-one shore is discarded, the same statement holds with only
the second summand when `a=1`.

#### Proof

Every signature difference has coordinate sum zero on both shores, proving
containment in the right side.  If adjacent `a`-sets `X,X'` differ by one
element, then `|X union X'|=a+1<=b`; choose a `b`-set `Y` containing their
union.  The two flags `(X,Y),(X',Y)` generate `e_X-e_X'`.  The Johnson graph
on `a`-sets is connected, so these vectors generate the first root lattice.

If adjacent `b`-sets `Y,Y'` differ by one element, their intersection has
size `b-1>=a`; choose `X subset Y intersection Y'`.  The two flags generate
`e_Y-e_Y'`, and connectivity of the `b`-set Johnson graph gives the second
root lattice.  The two families of generators are shore-pure, proving the
direct sum.  `square`

All certified pairs

\[
 (1,6),(1,7),(2,7),(3,6),(3,7),(4,7),
 (5,6),(5,7),(6,7)                                  \tag{4.3}
\]

satisfy the hypotheses.  After projection to `Z_17` necklaces, define the
co-occurrence graph using the actually projected adjacent-exchange
generators.  Its incidence lattice is the zero-sum lattice on each connected
component and is saturated.  Therefore no nonunit Smith invariant exists
in the independent-layer relaxation.  Its only additive obstructions are
component totals; positivity turns these into the usual Hall/equality cuts.

This does not prove saturation after path reachability.  For a fixed root,
let `B` be the node--arc incidence matrix of the pruned layered automaton,
let `C` map arcs to the six colour vectors, and fix one root path `p_0`.
The exact path-difference lattice is

\[
                         C(\ker_{\mathbb Z} B).       \tag{4.4}
\]

The Smith form of a fundamental-cycle/diamond generator matrix for (4.4)
is the correct finite modular test.  It may acquire torsion even though
(4.2) is saturated.

## 5. Separate Hall does not imply a common path

The obstruction is present even in the smallest nested Boolean flag model.
Let `L={1,...,8}` and put

\[
 \begin{array}{ll}
 A_0=\{1,2,3\},&A_1=\{1,2,4\},\\
 B_0=\{1,2,3,4,5,6\},&B_1=\{1,2,3,4,5,7\}.
 \end{array}                                         \tag{5.1}
\]

Every `A_i` is contained in every `B_j`.  Adding the common top `L` and one
owner element makes each pair `(A_i,B_j)` a legitimate nested type
`(3,3,2,1)` flag.  Give the first layer states

\[
                         a=(A_0,B_0),\quad b=(A_0,B_1)
\]

and the second layer states

\[
                         c=(A_1,B_0),\quad d=(A_1,B_1),
\]

but retain only transitions `a->c` and `b->d`.

### Proposition 5.1 (nested Hall/path separation)

Both rank graphs have perfect matchings, and the two layers have a static
common nested-flag transversal.  Nevertheless no legal path is rainbow at
both ranks.

#### Proof

The rank-three colours are forced to be `A_0,A_1` and are distinct.  At
rank six, each layer offers both `B_0,B_1`, so Hall is exact.  The static
choices `(a,d)` and `(b,c)` are common nested transversals.  They are not
paths.  The only paths are `(a,c)`, which repeats `B_0`, and `(b,d)`, which
repeats `B_1`.  `square`

The two legal path bases `{a,c}` and `{b,d}` fail basis exchange.  Thus full
state paths are not the bases of a matroid or gammoid; in prefix form they
have the weaker path-greedoid structure.  Concatenating private copies with
complete inter-copy connectors and block-private colours gives linear
rank-six defect while every separate Hall system and every static nested
flag system remains feasible.

This example is an abstract transition subrelation on genuine Boolean
flags.  It is not asserted to be a subautomaton of the frozen MMM instance.
Its exact conclusion is that nestedness, separate Hall and the Catalan count
alone cannot imply a common-path theorem or even bounded defect.  A positive
result must use an MMM-specific path-switch property.

There is one taut positive limit.  If every layer menu is a Cartesian
product over the six rows and every transition is independent of those row
coordinates, then six separate Hall matchings combine coordinatewise into a
legal path.  The actual age flags do not meet this hypothesis: their rows
are nested and Proposition 6.1 below shows that the complete payload is
state-injective.

## 6. There is no payload-transparent state rectangle

### Proposition 6.1 (payload injectivity)

Fix the owner `T`, deleted label `alpha`, incoming label `beta`, and the age
type.  The rank-`2,...,8` suffix payload determines the entire partition
state.

#### Proof

If `c_0>=2`, both `S_1` and `S_2` are among the recorded tight rows, and

\[
 Q_0=S_1,\quad Q_1=S_2-S_1,\quad
 Q_2=S_3-S_2,\quad Q_3=T-S_3.                        \tag{6.1}
\]

If `c_0=1`, literal updating forces `Q_0={beta}` because the incoming new
coordinate consumes the sole age-zero position.  Then `S_2,S_3` and `beta`
give the same reconstruction.  `square`

Hence two distinct states at one layer cannot have the same complete
coloured payload.  The rectangularization of Section 2 necessarily
transfers colours; there is no nontrivial payload-transparent tail--head
rectangle to which ordinary network rounding could be applied wholesale.

## 7. A run-four supply cut for every owner cycle

Let an equivariant quotient Johnson cycle have physical owners `T_i`, with
edge `i` deleting `alpha_i` and inserting `beta_i`.

### Theorem 7.1 (singleton-age run-four injection)

In any literal age lift using the certified types, every position `j` with
`c_0(j)=1` satisfies

\[
                         \beta_{j-1}=\alpha_{j+3}.    \tag{7.1}
\]

The corresponding coordinate has one-run exactly

\[
                         T_j,T_{j+1},T_{j+2},T_{j+3}. \tag{7.2}
\]

Distinct such positions give distinct run starts.  Consequently an
equivariant quotient owner cycle carrying a type multiset with `h`
occurrences of `c_0=1` must have at least `h` quotient coordinate-run orbits
of length exactly four.

#### Proof

The incoming inserted coordinate `beta_(j-1)` belongs to `C_(j,0)`.  If
that class has size one, it is the entire class.  The survivor chain

\[
 C_{j+3,3}\subseteq C_{j+2,2}subseteq
 C_{j+1,1}\subseteq C_{j,0}                         \tag{7.3}
\]

consists of nonempty classes, so all four sets are that singleton.  The last
set is `{alpha_(j+3)}`, proving (7.1).  The coordinate is absent before its
insertion, survives unrefreshed for the next three transitions, and leaves
on edge `j+3`, proving exact length four.  Run starts are indexed by their
insertion edges, so the map is injective.  `square`

For the frozen certificate,

\[
                         h=139+297=436.               \tag{7.4}
\]

This is an owner-cycle capacity cut independent of all six suffix colours.

## 8. Exact obstruction on the canonical shift-one MMM cycle

Freeze the published shift-one MMM upper projection as

`scratch/k17_mmm_shift1_upper_cycle_20260801.word`.

It has 24310 distinct rank-nine owners, Johnson adjacency, all 24310 lower
rank-eight colours once, strict quotient period1430 and voltage one.  Its
physical coordinate-run histogram begins

\[
 2^{5695},3^{1598},4^{2244},5^{357},6^{1071},
 7^{119},8^{1071},                                      \tag{8.1}
\]

and every count is divisible by17.  Hence it has only

\[
                         2244/17=132                  \tag{8.2}
\]

quotient run orbits of length four.  Combining (7.4) and (8.2) gives the
solver-free cut

\[
                         132<436,                     \tag{8.3}
\]

with deficit304.  Therefore this owner cycle admits no literal lift of the
certified type multiset, for any cyclic type ordering and either orientation.

There is also a direct coloured obstruction.  The native rank-seven bank
from Proposition 3.2 has only

\[
                         1001<1144                  \tag{8.4}
\]

distinct target necklaces; it misses143.  Thus even an independently
repaired age chronology on this same owner order could not satisfy the
rank-seven row.

For the particular frozen type word

`scratch/k17_age_type_euler_word_20260801.tsv`,

the complete cyclic correlation audit is sharper:

\[
\begin{array}{c|c|c|c}
\text{orientation}&|\{j:\beta_{j-1}=\alpha_{j+3}\}|&
 \max\text{ matched forced positions}&\min\text{ violations}\\ \hline
\text{forward}&132&64&372\\
\text{reverse}&132&55&381.
\end{array}                                          \tag{8.5}
\]

On the rank-seven row, the best frozen-word alignments still leave240 holes
forward and242 holes in reverse.  All 1430 relative cyclic shifts were
checked in each orientation.  Equations (8.3) and (8.4), not search
exhaustion, are the stronger ordering-independent obstructions.

## 9. Exact surviving gate

The frozen type word is a valid connected age-type circulation, but the
canonical MMM cycle is not its literal owner host.  The next positive input
must be one of:

1. a different unit-voltage lower-rainbow owner cycle with at least436
   exact-length-four run orbits, all1144 native rank-seven lower-`q2`
   target orbits, and a nonempty uncoloured partition automaton;
2. a different exact age certificate with smaller `c_0=1` demand; or
3. a joint owner-cycle/type construction rather than post-colouring a fixed
   MMM cycle.

After such an input is found, the proof-safe order is:

1. fix a root and prune the literal layered automaton;
2. apply the separated first-shore Hall theorem where possible;
3. compute the Smith form of the path lattice (4.4);
4. solve the remaining correlated second-shore rank-six/rank-seven path
   transversal; and only then
5. test upper-safe opening and the literal compiler.

The present results do not claim that the six-row gate is impossible in a
different host.  They show exactly where ordinary TU applies, why a
payload-transparent reduction cannot finish it, and why the most canonical
MMM host must be replaced.

## 10. Executable audits

The local fixed-neighbour audit

`scratch/audit_threadD_age_suffix_rectangularization_20260801.py`

checks all 25 type triples occurring in the frozen word.  On one canonical
geodesic two-edge Johnson geometry per triple, it enumerates the full
intermediate fibre, verifies the Cartesian product (2.2), both parts of the
triangular suffix action (2.4), exchange connectivity and payload
injectivity.  Johnson-triangle geometries and other neighbour choices are
not exhaustively replayed; the symbolic proof of Theorem 2.1 is independent
of that fixture.  Its
payload

`scratch/threadD_age_suffix_rectangularization_20260801.audit.json`

has status

`PASS_AGE_SUFFIX_FIXED_NEIGHBOUR_RECTANGULARIZATION`.

The independent MMM audit

`scratch/audit_threadD_k17_mmm_fixed_type_lag4_20260801.py`

verifies the complete frozen owner word, lower rainbow, strict spiral,
coordinate-run histogram, run-four supply cut and every relative frozen-word
alignment in both orientations.  Its payload

`scratch/threadD_k17_mmm_fixed_type_lag4_20260801.audit.json`

has status

`PASS_SCOPED_NO_FIXED_TYPE_LAG4_ALIGNMENT`.

The frozen owner word was obtained without optimization by

`scratch/fetch_k17_mmm_shift1_upper_cycle_20260801.py`

from the published `combos.org` shift-one construction, then replayed
entirely from the local frozen artifact.  No local SAT or heavy search was
used.
