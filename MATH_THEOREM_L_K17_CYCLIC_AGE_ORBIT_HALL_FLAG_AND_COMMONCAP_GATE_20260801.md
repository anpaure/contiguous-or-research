# `k=17` cyclic age orbits: exact quotient Hall, the flag-correlation gate, and common-cap scope

Date: 2026-08-01  
Lane: L, occurrence-labelled terminal compiler  
Status: unconditional orbit-matching theorem, exact Hall cuts, automatic
unguarded rank-eight-root/current-owner contraction, and a sharp rank-count
counterexample; no decorated owner cycle or `k=17` universal word is claimed

## 0. Outcome

For `k=17`, every nonempty proper subset has a free orbit under cyclic
coordinate rotation.  The exact age-ST certificate has denominator

\[
                1430={1\over17}\binom{17}{9}=\operatorname{Cat}_8, \tag{0.1}
\]

so its integer type masses can indeed label one type per rank-nine owner
orbit.  Every required rank-`s` mass

\[
                         n_s={1\over17}\binom{17}{s}   \tag{0.2}
\]

is also an integer.

This arithmetic removes the denominator obstruction, but it does not
restore the stabilizer averaging used in the fractional proof.  The exact
conclusions are:

1. For any **fixed** invariant target-to-cell occurrence bank, physical
   matching is equivalent to ordinary Hall on the orbit quotient.  If that
   bank is trace guarded, the same quotient matching is a common-cap
   compiler.
2. The unrestricted quotient containment graph at each rank is biregular
   and always has a target-saturating matching.  Thus there is no
   single-rank obstruction when the supporting owner orbits are chosen
   prospectively.
3. Certificate rank counts alone are not Hall.  At rank seven, all neighbours
   of one target orbit fit inside the 286 owner orbits whose types do not
   support rank seven; the capacity table still passes while that target has
   degree zero.  The same literal obstruction works at ranks four, five, and
   six.
4. In the unguarded static problem, one can avoid assigning types to owners
   first.  Partition the lower targets into nested packets with distinct
   rank-eight roots.  The regular rank-eight/rank-nine quotient incidence
   multigraph then matches those roots to current owners automatically.
5. The remaining simultaneous object is not seven independent matchings.
   It is a rooted short-chain exact cover, followed by a coloured flag cycle
   satisfying the changing-owner survivor relation and twisted voltage.  An
   authenticated GKS surgery already solves the ranks six/seven/eight part;
   only the ranks two--five low/head attachment remains statically.
6. Cyclic equivariance supplies no automatic common cap for an **external
   carrier**.  A direct transition-compatible age source needs no separate
   lower cap; an external carrier still needs trace guards or literal
   maximal-cap replay.

Thus the denominator-1430 observation yields a genuine finite one-copy
route, but the missing theorem is an orbit-flag/transition transversal, not
a scalar rounding of the age masses.

## 1. Free cyclic orbits and the certified type patterns

Let `Gamma=Z_17` act by coordinate rotation.  Since 17 is prime, a subset
fixed by a nonidentity rotation is either empty or all of `Z_17`.  Hence all
target and owner orbits used below have size 17.

Use the following shorthand for the nine certified age types:

| name | type `c` | multiplicity | proper suffix ranks `R(c)` |
|---|---|---:|---|
| `A` | `(1,5,2,1)` | 139 | `{1,6,8}` |
| `B` | `(1,6,1,1)` | 297 | `{1,7,8}` |
| `C` | `(2,5,1,1)` | 8 | `{2,7,8}` |
| `D` | `(3,3,2,1)` | 20 | `{3,6,8}` |
| `E` | `(3,4,1,1)` | 20 | `{3,7,8}` |
| `F` | `(4,3,1,1)` | 140 | `{4,7,8}` |
| `G` | `(5,1,2,1)` | 127 | `{5,6,8}` |
| `H` | `(5,2,1,1)` | 237 | `{5,7,8}` |
| `I` | `(6,1,1,1)` | 442 | `{6,7,8}` |

The resulting supporting-owner counts are

\[
 (|A_s|)_{s=1}^8=(436,8,40,140,364,728,1144,1430),  \tag{1.1}
\]

while the target-orbit demands are

\[
                    (n_s)_{s=1}^8=(1,8,40,140,364,728,1144,1430). \tag{1.2}
\]

Thus ranks two through eight are tight and rank one has slack 435.

## 2. Exact free-cyclic occurrence matching theorem

Let `L` be a union of proper target orbits and `C` a union of physical cell
orbits, all free under `Gamma`.  Let

\[
                             H\subseteq L\times C      \tag{2.1}
\]

be an invariant candidate incidence graph.  Write `Hbar` for its quotient
support graph on target and cell orbits.

### Theorem 2.1 (free-orbit Hall lift)

The following are equivalent.

1. `H` has a matching saturating every physical target in `L`.
2. `Hbar` has a matching saturating every target-orbit node.
3. Every target-orbit family `X` satisfies

   \[
                          |N_{\overline H}(X)|\geq|X|. \tag{2.2}
   \]

If, in addition, `H` is one complete trace-guarded common-cap bank, every
matching obtained this way is a literal common-cap compiler.

#### Proof

For a quotient edge joining free orbits `O_L,O_C`, choose basepoints and
identify both with `Z_17`.  Invariance makes its nonempty physical block a
union of shifts

\[
                         i\longmapsto i+\delta.        \tag{2.3}
\]

Any one allowed shift is a perfect matching of the two 17-vertex orbits.
A quotient matching therefore lifts block by block to a physical matching.

Conversely, average any physical matching over `Gamma` and sum its weights
on orbit blocks.  Divide by 17.  This gives a fractional matching in
`Hbar` with unit demand and unit capacity at every quotient node.  Bipartite
integrality gives a quotient matching.  The equivalence with (2.2) is Hall.
Finally, complete trace guards make every physical matching in `H` maximal-
cap exact. \(\square\)

The theorem is exact, but its input is an occurrence graph.  Type masses do
not construct that graph or its guards.

## 3. The full quotient containment graph is Hall-positive

For `1<=s<=8`, let `G_s` be the quotient **multigraph** whose left vertices
are rank-`s` target orbits and whose right vertices are rank-nine owner
orbits.  An edge is an aligned containment `S subset T`, modulo simultaneous
rotation.  Multiple alignments between the same orbit pair are retained.

### Proposition 3.1 (biregular orbit containment)

The two degrees of `G_s` are

\[
           a_s=\binom{17-s}{9-s},
           \qquad b_s=\binom9s.                       \tag{3.1}
\]

Consequently its simple support graph has a matching saturating all `n_s`
target-orbit vertices.

#### Proof

Fix a target representative `S`.  Its aligned rank-nine supersets number
`a_s`.  Fix an owner representative `T`; its rank-`s` subsets number `b_s`.
Freeness makes these the quotient multidegrees, and double counting gives

\[
                         n_sa_s=1430b_s.              \tag{3.2}
\]

For a target-orbit set `X`, all `a_s|X|` incident multiedges end in
`N(X)`, while each owner node receives at most `b_s` of them.  Hence

\[
        |N(X)|\geq{a_s\over b_s}|X|
                 ={1430\over n_s}|X|\geq|X|.          \tag{3.3}
\]

Hall proves the claim. \(\square\)

Thus for each rank separately one may first choose a saturating matching and
then declare its `n_s` image owners to be the supporting owners.  The
remaining difficulty is choosing these images with the common certified
type pattern and one compatible flag per owner.

## 4. Exact Hall cuts after a type placement

Let

\[
             \theta:\{\text{owner orbits}\}\longrightarrow
                      \{A,\ldots,I\}                  \tag{4.1}
\]

have the certified multiplicities, and put

\[
             A_s(\theta)=\{U:s\in R(\theta(U))\}.     \tag{4.2}
\]

Let `G_s^phys` be any declared orbit occurrence catalogue; at the weakest
local level it is a subgraph of the containment support in Section 3, and
after a quotient chronology is fixed it must also enforce the outgoing
deleted label, suffix width, transition state, and every guard.

### Theorem 4.1 (exact rank-`s` orbit cut)

For a fixed type placement and fixed occurrence catalogue, the rank-`s`
physical targets have an equivariant SDR if and only if

\[
 \boxed{
 |N_{G_s^{\rm phys}}(X)\cap A_s(\theta)|\geq|X|
 \qquad\text{for every target-orbit set }X.}          \tag{4.3}
\]

At ranks two through eight the two shores have equal size, so this is a
perfect-matching condition.

This is Theorem 2.1 applied after deleting the owner tickets whose types do
not support `s`.

### Proposition 4.2 (rank counts are sharply insufficient)

The certified type multiplicities can satisfy every scalar capacity while
the rank-seven Hall graph has a zero-degree target.

#### Proof

Fix a rank-seven target orbit `O`.  A representative has only

\[
                         \binom{10}{2}=45             \tag{4.4}
\]

aligned rank-nine supersets, so `O` has at most 45 neighbouring owner
orbits even in the unrestricted containment graph.

Exactly

\[
                  139+20+127=286                      \tag{4.5}
\]

owners receive the three types `A,D,G` which do not support rank seven.
Assign every neighbour of `O` one of these ineligible types, and fill their
remaining 241 positions arbitrarily with the same three prescribed bin
sizes.  Assign the six rank-seven types to the other 1144 owners.  All type
and rank counts remain exact, but (4.3) fails for `X={O}` with empty
neighbourhood. \(\square\)

The identical singleton-cut argument applies at ranks four, five, and six:

\[
\begin{array}{c|c|c}
s&\text{ineligible owner count}&\text{aligned-superset upper bound}\\ \hline
4&1290&\binom{13}{5}=1287\\
5&1066&\binom{12}{4}=495\\
6&702&\binom{11}{3}=165.
\end{array}                                            \tag{4.6}
\]

This is a logical counterexample to automatic rounding from the type counts;
it is not a no-go for a prospectively chosen decorated quotient cycle.

As a useful opposite calibration, the rank-two support graph is complete:
for every cyclic distance `a=1,...,8`, the graph with edges
`x--(x+a)` is a 17-cycle and has independence number eight.  Every
rank-nine owner therefore contains a pair of every cyclic distance, so any
eight rank-two-supporting owners can serve all eight rank-two target orbits.

## 5. Owner-first simultaneous bases and the root-first contraction

Let `U` be the 1430 owner-orbit ground set.  For each rank `s`, reverse the
containment graph and let `M_s` be the transversal matroid on `U`: an owner
set is independent when it can be matched to distinct rank-`s` target
orbits.  Proposition 3.1 says `rank(M_s)=n_s`.

For a type placement with bins `B_A,...,B_I`, the separate rank SDRs exist
exactly when

\[
              A_s=\bigcup_{\alpha:s\in R(\alpha)}B_\alpha
              \quad\text{is a basis of }M_s
              \qquad(2\leq s\leq8).                  \tag{5.1}
\]

The bins must also partition `U` and have the nine certified sizes.  This is
an exact finite formulation of the prospective type-placement gate.  It is
an intersection of several pulled-back transversal-base constraints and
partition constraints, not ordinary two-matroid intersection.  Standard
Edmonds integrality for one or two matroids therefore does not close it.

Even (5.1) is only the **separate-rank** relaxation.  It does not ensure that
the targets assigned to one owner are nested parts of one age partition.

The owner-first formulation is not the smallest unguarded static model.
Suppose instead that one first partitions all target orbits of ranks two
through eight into 1430 prescribed nested packets, with every packet rooted
at a different rank-eight orbit `Q`.  Let `G_(8,9)` be the quotient
multigraph of aligned containments `Q subset T`.  Both shores have 1430
vertices and every vertex has multidegree nine.  Thus, for every root family
`X`,

\[
                         9|X|\leq9|N(X)|,             \tag{5.2}
\]

so the simple support satisfies Hall.  Bipartite edge colouring in fact
decomposes `G_(8,9)` into nine perfect matchings.  Choosing one aligned edge
for each packet and rotating its whole flag gives literal `Q subset T`, and

\[
                         C_3=T\setminus Q             \tag{5.3}
\]

is the required oldest singleton.  Therefore packet-to-current-owner Hall
is automatic once the rooted packetization exists.

This contraction removes the simultaneous bases (5.1) from the **unguarded
one-endpoint static** problem.  It does not choose the successor owner,
enforce `Q=T intersection T'`, or preserve a preassigned phase, transition,
or trace guard.  The exact contracted packet model and its mixed-rank Hall
cuts are given in
`MATH_THEOREM_L_GKS_K17_CHAIN_SPLITTING_AND_RESIDUAL_FLAG_HALL_GATE_20260801.md`.
The independently frozen 286-edge surgery in
`MATH_THEOREM_A_K17_GKS_RANK678_CONTROLLED_SURGERY_AND_LOW_FLAG_GATE_20260801.md`
constructs its complete central layer with shape counts

\[
                 442\ (6<7<8),\quad286\ (6<8),\quad702\ (7<8). \tag{5.4}
\]

Consequently the live unguarded static rows are just the four coupled
rank-two--five low-to-head Hall systems.

## 6. The true one-copy object is a transition-compatible flag exact cover

Every certified type has `c_3=1`.  On a changing-owner Johnson edge, the
oldest class is the deleted label `alpha`, and a local state supplies the
nested flag

\[
 C_0\subset C_0\cup C_1\subset
 C_0\cup C_1\cup C_2=T-\{\alpha\}\subset T.          \tag{6.1}
\]

The first three ranks in (6.1) are exactly `R(c)`.  For a fixed quotient
owner cycle and fixed type word, choose representatives `T_i` and let
`v_i in Z_17` be the edge voltage, so the literal next owner is the chosen
representative `T_(i+1)` rotated by `v_i`.  Let `F_i` be the finite menu of
labelled age partitions at owner position `i` consistent with its outgoing
deleted label.  Write

\[
                         f\leadsto_{v_i}f'             \tag{6.2}
\]

when the survivor inclusions of the changing-owner age lemma hold from `f`
to the rotated state `rho^(v_i)f'` across `i->i+1`.  On an unfolded
fundamental path, the final state is therefore `rho^v f_0`, where
`v=sum_i v_i`; it need not equal `f_0`.  Let `ell_s(f)` be the target orbit
emitted by the rank-`s` suffix of `f`.

### Theorem 6.1 (exact orbit flag-cycle system)

The lower occurrence part of a certificate-decorated quotient cycle exists
if and only if there are binary variables `x_(i,f)`, `y_(i,f,f')`, and
binary rank-one mark variables `m_(i,f)`, with `y` supported on (6.2),
satisfying

\[
 \sum_{f\in F_i}x_{i,f}=1,                            \tag{6.3}
\]

\[
 \sum_{f'}y_{i,f,f'}=x_{i,f},
 \qquad
 \sum_fy_{i,f,f'}=x_{i+1,f'},                        \tag{6.4}
\]

with cyclic indices, together with

\[
 \sum_{i,f:\ s\in R(\operatorname{type}(f)),\ \ell_s(f)=O}x_{i,f}=1
 \quad
 \left(2\leq s\leq8, O\in\binom{\mathbb Z_{17}}s/\mathbb Z_{17}\right), \tag{6.5}
\]

and

\[
 0\leq m_{i,f}\leq
 x_{i,f}\mathbf1_{1\in R(\operatorname{type}(f))},
 \qquad \sum_{i,f}m_{i,f}=1.                         \tag{6.6}
\]

Type labels and their multiplicities are fixed in the menus.  Every other
rank-one suffix occurrence is physically present but unmarked.

#### Proof

A selected decorated quotient cycle gives the variables by recording its
local states and transitions.  Tightness of every rank two through eight
makes distinctness equivalent to (6.5).

Conversely, (6.3)--(6.4), with the voltage-twisted relation (6.2), select one
compatible labelled age partition at every owner of the unfolded quotient
cycle and close it at the prescribed rotation.  The changing-owner lemma
spells the source letters.  Equation (6.5), followed by the free cyclic
lift, covers every physical lower target at those ranks exactly once; (6.6)
designates one occurrence orbit which covers all 17 singletons. \(\square\)

The system is a coloured flag exact cover with a cyclic automaton.  Separate
Hall conditions (4.3) are necessary projections, not sufficient conditions
for (6.3)--(6.5).

## 7. Common-cap interpretation

There are two different uses of the word "compiler" here.

1. **Direct age source.**  A solution of Theorem 6.1 literally chooses the
   final source letters `C'_0`.  Its marked suffixes are already physical;
   there is no additional lower common-cap rounding.  Upper witnesses,
   opening, and one connected owner chronology remain separate.
2. **Cap inside an external carrier.**  If the same target orbits are to be
   placed in a pre-existing envelope chronology, that chronology and its
   physical cells must themselves carry the free diagonal `Z_17` action.
   Form the resulting invariant target-to-cell bank `H`.  Theorem 2.1 then
   reduces its matching row to quotient Hall, but common-cap exactness follows
   only if `H` is trace guarded (or if the selected orbit shifts pass a
   literal maximal-cap replay).

More explicitly, if `M` is the selected occurrence-labelled target/cell
family and `Ebar_p` is the external carrier envelope at physical position
`p`, its maximal cap is

\[
 A_p(M)=\overline E_p\cap
        \bigcap_{(S,C)\in M:\ p\in C}S.              \tag{7.1}
\]

The exact external-carrier gate is that every `A_p(M)` is nonempty and that
these caps reproduce every protected owner/upper row and every selected
lower cell.  Rotation copies these equations; it does not prove them.

The age type remembers only the sizes of its classes.  It does not remember
which absolute cells overlap or which bits survive the intersections of all
selected caps.  In this particular certificate every `c_i` is positive, so
its three suffix ranks are strictly increasing and every available rank has
a unique suffix width.  Thus the general repeated-width ambiguity is absent
at `k=17`; the literal target, phase, transition, and cap data are still
lost.
Moreover,

\[
                 \operatorname{Stab}_{\mathbb Z_{17}}(T)=1 \tag{7.2}
\]

for every owner.  Thus cyclic symmetry supplies no within-owner transitivity
to replace the `Sym(T)` averaging in the fractional lift.  Equivariance is
enough to lift a proved quotient matching; it does not prove its edges or
its guards.

## 8. Connected type-word audit

The original age arc table has a 140-fold isolated self-loop at
`F=(4,3,1,1)`.  The minimal balanced repair is

\[
\begin{array}{rcl}
F\to F&:&140\mapsto139,\\
I\to I&:&125\mapsto124,\\
F\to I&:&0\mapsto1,\\
I\to F&:&0\mapsto1,
\end{array}                                            \tag{8.1}
\]

where `I=(6,1,1,1)`.  Both new arcs satisfy the age inequalities.  All type
marginals and rank capacities are unchanged, and the positive support is
now connected Eulerian.  The current certificate and decorated-cycle
reduction incorporate this repair.  Hence a 1430-position cyclic **type
word** exists; assigning it to a Johnson owner cycle and solving the flag
system remains open.

## 9. Exact frontier

At `k=17`, the occurrence/compiler hierarchy is now

\[
\boxed{
\begin{array}{c}
\text{integer type counts and connected type word}\quad\text{(proved)}\\
\Downarrow\\
\text{GKS central rank-six/seven/eight packetization}\quad\text{(proved)}\\
\Downarrow\\
\text{rank-two--five low/head packetization}\quad\text{(open)}\\
\Downarrow\\
\text{static current-owner assignment}\quad\text{(automatic)}\\
\Downarrow\\
\text{transition-compatible nested flag exact cover}\quad\text{(open)}\\
\Downarrow\\
\text{one nonzero-voltage quotient owner cycle and upper-safe opening}
   \quad\text{(open)}\\
\Downarrow\\
\text{direct literal source, or guarded orbit common cap}.
\end{array}}
\]

The owner-first cuts are (4.3); after root-first contraction the exact
static cuts are the mixed head/root and low/head Hall rows in the companion
GKS note.  The exact first positive theorem is the free-orbit Hall lift.
What cyclic equivariance does **not** do is turn the rank capacity table into
the correlated flag/transition solution.

## 10. Authenticated inputs

The scope above is rebased on:

* `MATH_THEOREM_K17_EXACT_AGE_COMPOSITION_FRACTIONAL_ST_CERTIFICATE_20260801.md`,
  SHA-256
  `985941d5806b7c22d40afaddcb69a0152764051d550ec52d44d08c123af59131`;
* `MATH_REDUCTION_K17_CATALAN_ORBIT_AGE_DECORATED_RAINBOW_CYCLE_20260801.md`,
  SHA-256
  `cdebb8b6ef75461e65f04ed5d8a79d210cc30876ecc1392119555d6ddbc6f646`;
* `MATH_THEOREM_AGE_COMPOSITION_STRASSEN_CIRCULATION_CUTS_20260801.md`,
  SHA-256
  `8a3084c9f546707c2b031de472d9b1d2191fbccf9fcbacb5cd30d7fec57922fa`.

The first two files already contain the connected `F<->I` repair in
(8.1).  The orbit-Hall, type-placement counterexample, transversal-base
formulation, and flag-cycle system in this note were independently derived
from their literal type and orbit data; no finite search was used.
