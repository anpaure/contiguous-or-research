# `k=17`: residence factor Benders master, exact residual collars, and the unit-37 DM verdict

Date: 2026-08-02  
Status: exact theorem/model interface with frozen projection, residual-collar,
transition-gap, cumulative round-five and directed-history audits.
The rank-eight factor, rank-ten coverage, topology and depth-three residence
must be selected jointly.  The frozen round-one CNF is only the first lazy
separation round.  Its proof-producing Kissat and CaDiCaL runs, and both
auxiliary Kissat variants, each exited `124` at 1,800 seconds: the result is
UNKNOWN, not UNSAT.  Deeper upper and compiler recourse are not activated
because no resident master solution is yet frozen.

## 1. Frozen rebase and exact scope

The round-one quotient CNF is

```text
c6638107ba4d1241403f914b5893614d9660a48cde7e43bef495b5fe28ebed52
  scratch/k17_marker58_residence_round1_20260802/marker58_residence_round1.cnf
7b88292585cee9bb8e72a0017734f466f12aa7cb12c4507bec69b40484eb81f3
  scratch/k17_marker58_residence_round1_20260802/marker58_residence_round1.map.tsv
9948bd6152774219b93adf7f5476929ad6e1a8a4338b9ddd38504ce47eaf3e51
  scratch/k17_marker58_residence_round1_20260802/c68b.double_fusion.residence_blocks.cnf
```

It has 204,167 variables and

\[
 439145+2+316=439463                                      \tag{1.1}
\]

clauses: the exact base resource CNF, two incumbent component cuts, and 316
short-run blockers extracted from the connected `double_fusion` factor.  It
has no voltage constraint.  Its residence clauses have arities

```text
unit 37, binary 15, ternary 149, quaternary 115.
```

These clauses are sound necessary rows in the connected
`Z_17`-equivariant protected catalogue, but they are not a complete static
residence encoding.  Every later incumbent must be separated again.

The current 4,199-run factor has exact census

\[
 N_2=2312,\qquad N_3=1887,\qquad N_{<4}=4199=247\cdot17.  \tag{1.2}
\]

A complete single-move census contains 1,888 directed endpoint-retaining
C6 circuits and 6,259 corresponding C8 circuits.  Among the cap-safe,
physically connected candidates, none reduces (1.2).  Thus 4,199 is an
exact floor only for that one-circuit neighbourhood.  It is not a global
lower bound, a support lower bound, or even a certified two-circuit floor.
The bound state is frozen by

```text
5c806564935f8eed1eadd4e592e4888859a75a9ab08190a9e36b7dcec89a03b2
  round048.model
b1343737cb0e3d99dec503e526e566521504478af1c5792c9a7949b6a5796616
  c68b.greedy48.factor.tsv
bc993e33368002b873ea484328ecf3931c58105a8e59f9ab96025d300f7ff8a7
  round048.audit.json
```

## 2. Exact resource master

Work first on the quotient catalogue.  Let `P` be the 232 fixed protected
edge orbits and let `x_e` select a residual option.  Write `f(e)` for its
rank-eight facet orbit, `m_o(e) in {0,1,2}` for its endpoint multiplicity at
owner orbit `o`, and `u(e)` for its rank-ten cap orbit.  Put
`d_P(o)=deg_P(o)` and let
`p_P(u)=1` exactly when at least one protected edge covers `u`.
The exact resource rows are

\[
 \sum_{e:f(e)=f}x_e=1                                      \tag{2.1}
\]

for every residual facet orbit,

\[
 d_P(o)+\sum_e m_o(e)x_e=2                                 \tag{2.2}
\]

for every owner orbit, and

\[
 p_P(u)+\sum_{e:u(e)=u}x_e\ge1                            \tag{2.3}
\]

for every cap orbit.  Quotient loops count twice in (2.2).  The existing
CNF writes (2.2) as an at-most row, but the total residual endpoint ledger
is `2*1198`, so (2.1) forces equality.

Equations (2.1)--(2.3), with the fixed protected rows, are in bijection with
`Z_17`-equivariant rank-eight-rainbow, rank-nine-degree-two factors covering
every rank-ten cap.  They make no connectivity or residence assertion.

## 3. Quotient connectivity and physical voltage

For every nonempty proper quotient-owner shore `S`, impose

\[
 |P\cap\delta(S)|+\sum_{e\in\delta(S)}x_e\ge2.             \tag{3.1}
\]

On the integral degree-two face, (3.1) is equivalent to one quotient cycle.
An integral separator returns the vertex set of any component.  Fractional
separation is the global minimum cut with fixed and selected edge capacities.

One quotient cycle need not lift to one physical cycle.  Give every oriented
quotient edge dart `a=(v,w)` its signed voltage `delta_a in Z_17`, with the
two darts of a quotient loop kept distinct.  Use oriented selection variables
`y_a`, with one incoming and one outgoing arc at every owner, and impose

\[
 y_a+y_{\bar a}=x_e\quad(e\notin P),\qquad
 y_a+y_{\bar a}=1\quad(e\in P).                            \tag{3.2}
\]

Choose one selected auxiliary gauge dart with `g_a<=y_a` and
`sum_a g_a=1`.  For binary `p_a`, impose the exact equality
`p_a=y_a-g_a`.  Give every quotient owner one one-hot potential `R_(v,r)`,
`r in Z_17`.  On every selected nongauge arc require

\[
 R_{v,r}+p_a\le1+R_{w,r+\delta_a}
       \qquad(r\in\mathbb Z_{17}),                         \tag{3.3}
\]

and on the gauge arc impose

\[
 R_{v,r}+R_{w,r+\delta_a}+g_a\le2
       \qquad(r\in\mathbb Z_{17}).                         \tag{3.4}
\]

Fix one arbitrary potential to remove the additive gauge.  Removing the
gauge arc turns the directed quotient cycle into a path, so (3.3) propagates
the unique relative potentials.  Equation (3.4) says that closing the path
has nonzero voltage.  Since 17 is prime, (3.1)--(3.4) are equivalent to a
single 24,310-owner physical lift.

The auxiliary quotient gauge arc represents an orbit of 17 physical edges.
It is not the one literal edge at which a physical chronology is opened.

## 4. Exact residence master for arbitrary physical factors

For an arbitrary, not necessarily equivariant, physical factor use one
binary edge variable `X_e` per allowed physical Johnson edge.  Equations
(2.1)--(2.3) are replaced by their literal rank-eight, owner and rank-ten
versions, and physical connectivity uses (3.1) on all 24,310 owners.
Choose one literal opening seam

\[
 h_e\le X_e,\qquad \sum_e h_e=1.                           \tag{4.1}
\]

A singleton positive coordinate run is already impossible: if
`0,1,0` occurs at three consecutive owners, the two adjacent rank-eight
intersections are the same.  Thus only runs of lengths two and three remain.

Let `B` be a geometrically possible coordinate-labelled bracket path

\[
                    0,1^\ell,0,\qquad \ell\in\{2,3\},      \tag{4.2}
\]

including its entering, internal and leaving edges.  It has three edges for
`ell=2` and four for `ell=3`.  Impose

\[
 \boxed{
 \sum_{e\in B}(1-X_e)+\sum_{e\in B}h_e\ge1.}               \tag{4.3}
\]

### Theorem 4.1 — exact physical separation

On the connected degree-two factor face, (4.3) for every bracket `B` is
necessary and sufficient for a depth-three-resident linear opening.

#### Proof

If every edge of `B` is selected, its internal owners already use both of
their degree-two incidences, so the displayed segment is forced up to
reversal.  It remains an internal short run unless the unique seam lies on
one of its three or four edges.  This proves necessity.

Conversely, any internal positive run of length two or three supplies its
own fully selected bracket whose seam term is zero, contradicting (4.3).
Length one was excluded above, so every internal positive run has length at
least four.  Coordinatewise maximal depth-three erosion then reconstructs
the owner chronology.  Its source envelopes are nonempty because four
consecutive rank-nine Johnson owners have intersection rank at least six.
This proves sufficiency.  `square`

For an integral incumbent, separation consists only of traversing the cycle
and emitting the rows for its `0,11,0` and `0,111,0` windows.  For a
fractional incumbent, minimize

\[
 w(B)=\sum_{e\in B}(1-X_e)+\sum_{e\in B}h_e                \tag{4.4}
\]

over the finite depth-three/four motif catalogue; exactly the motifs with
`w(B)<1` are violated.  Hence lazy separation is complete.

## 5. Exact residence reduction in the connected equivariant class

The physical seam terms in (4.3) cannot be discarded for an arbitrary
factor.  They can be discarded in the target quotient subclass.

### Theorem 5.1 — translate-window theorem

A connected `Z_17`-equivariant factor has a resident linear opening if and
only if it has no cyclic positive run of length below four.

#### Proof

The coordinate generator acts freely on the 24,310-owner Hamilton cycle.
An automorphism of order 17 cannot be a reflection, so it is a nontrivial
cycle rotation.  Every edge orbit consists of 17 edges spaced
1,430 positions apart.  A short coordinate run therefore has 17 translated
bracket windows.  Each window has at most four edges, so the translated
windows are disjoint.  One physical seam can meet at most one of them and
cannot make the other 16 boundary runs.  Thus no resident opening exists.
The converse is immediate: with no cyclic short run, every opening is
resident.  `square`

Consequently the exact quotient lazy row is

\[
 \boxed{
 \sum_{e\in\operatorname{supp}(B)}(1-x_e)\ge1,}            \tag{5.1}
\]

where fixed protected edges are omitted and equal option variables are
deduplicated.  The 316 round-one clauses are precisely the first incumbent's
rows (5.1).  An all-fixed empty support would certify immediate
infeasibility; none occurs in round one.

### Theorem 5.2 — exact transition-label oracle

Orient a physical Middle Levels lift and write the two flips on projected
owner edge `i` as

\[
 T_i\xrightarrow{p_i}X_{i+1}\xrightarrow{q_i}T_{i+1},
 \qquad p_i\text{ deleted},\quad q_i\text{ inserted}.
\]

If `q_i=a` and `p_j=a` is the next deletion of the same coordinate in the
cyclic flip sequence, then its positive owner run has length

\[
 j-i={\operatorname{dist}(q_i,p_j)+1\over2}.               \tag{5.2}
\]

Thus depth-three positive residence is exactly

\[
 \operatorname{dist}(q_i,p_j)\ge7                          \tag{5.3}
\]

for every insertion and its next same-label deletion.  At an integral
incumbent the independent separator merely scans the cyclic flip labels.  A
violation with `1<=j-i<=3` emits (4.3) on owner edges `i,...,j` in the
arbitrary physical model, or the deduplicated row (5.1) in the connected
equivariant model.  The `j-i=1` row is redundant once rank-eight facets are
rainbow, but retaining it makes the transition-label replay independent.

The quotient test does not require physical development.  Normalize a dart
`a:v->w` so that at tail fibre `g` its deletion and insertion labels are
`g+pi_a` and `g+chi_a`, and its head fibre is `g+delta_a`.  A dart path
`a_0,...,a_t`, `t in {1,2,3}`, whose propagated endpoint label is not flipped
on an intermediate dart is a forbidden motif exactly when

\[
 \chi_{a_0}\equiv
 \pi_{a_t}+\sum_{s=0}^{t-1}\delta_{a_s}\pmod {17}.          \tag{5.4}
\]

This congruence is independent of `g`: either all 17 developed paths are
short motifs or none are.  Operationally, scan forward and stop at the first
same-label deletion; composite paths spanning a deletion and reinsertion are
not separate occurrence rows.  The test is therefore a compact exact pricing
oracle for (5.1), after quotient connectivity and nonzero voltage have been
certified.

No deletion-to-next-insertion spacing is imposed.  Requiring a symmetric
gap between every two consecutive flips of a label is a stronger
sufficient-only condition for positive residence, not an exact master row.
The exact negative-run condition is a separate deletion-to-insertion gap of
at least nine and is outside the positive-residence gate used here.

## 6. Equivalent turn/age interface

For downstream source and compiler coupling, retain an orientation of the
physical selected cycle: on its two darts impose
`y_a+y_{\bar a}=X_e`, with one selected incoming and one selected outgoing
dart at every owner.  For every owner `v` and coordinate `j`, choose exactly
one state

\[
 q\in Q=\{0,1,2,3,4,L1,L2,L3,L4\}.                        \tag{6.1}
\]

State zero means that `j` is absent.  Ordinary states one, two and three are
exact positive-run ages and state four is the saturated age at least four.
The `L` states describe the positive prefix clipped by the left boundary:
`L1,L2,L3` are exact prefix ages and `L4` is saturated.  State zero is
compatible only with bit zero; every other state is compatible only with bit
one.

On a selected directed nonseam dart, the permitted transitions are

```text
ordinary, head bit 1: 0->1, 1->2, 2->3, 3->4, 4->4
ordinary, head bit 0: 0->0, 4->0
left prefix, bit 1:   L1->L2, L2->L3, L3->L4, L4->L4
left prefix, bit 0:   Lt->0 for every t in {1,2,3,4}
```

Lift the physical seam to its selected orientation by

\[
 h_a\le y_a,\qquad \sum_a h_a=1,\qquad
 h_e=h_a+h_{\bar a}.
\]

For every incompatible state pair on dart `a=(v,w)`, impose

\[
 s_{v,j,q}+s_{w,j,q'}+y_a-h_a\le2.                         \tag{6.2}
\]

The seam deletes its transition.  It also initializes its head: for every
seam dart `a=(v,w)` and coordinate `j`, impose

\[
 h_a\le s_{w,j,0}\quad(j\notin w),\qquad
 h_a\le s_{w,j,L1}\quad(j\in w).                           \tag{6.3}
\]

The `L` chain permits an arbitrarily short clipped left prefix.  Ordinary
terminal states one through three permit an arbitrarily short clipped right
suffix, while every positive run that closes away from the seam must first
reach state four.  Hence (6.1)--(6.3) are equivalent to the complete physical
motif family (4.3).  Unlike a five-state sentinel encoding, this formulation
exports exact boundary ages through depth three (and a saturated fourth
state).  The lazy formulation is smaller for factor search; this age
formulation is the fail-closed interface for collars, source positions and
compiler cells.

### 6.1 Static eager quotient-age formulation

The nine-state physical formulation above is strictly broader than the
orbit-tied search, but it is not instantiated in the frozen CNF.  On the
connected nonzero-voltage `Z_17`-equivariant face, an eager quotient model
can instead use five cyclic states.  This is equivalent to the lazy rows
(5.1), but exports ages for later coupling.

Put `n=1430`, let the catalogue have `m=35713` residual option orbits and
`232` fixed protected edge orbits, and choose a fixed nonloop protected dart

\[
                 a_*=(t_*,r_*).                           \tag{6.4}
\]

Fixing its direction loses no factor/topology/residence solution: reverse
the whole eventual quotient cycle if necessary.  It need not be a legal
source seam, so a source-restricted opening must keep its physical seam
choice separate.

For each undirected orbit `e` use one orientation bit `o_e`.  If `e` is
variable, the forward and reverse selected-dart expressions are `o_e` and
`x_e-o_e`, with `0<=o_e<=x_e`; for a fixed edge they are `o_e` and
`1-o_e`.  Write either expression as `Y_a`.  Impose one selected incoming
and one selected outgoing dart at every quotient owner and fix `Y_(a_*)=1`.
Give each owner a bounded continuous order `0<=T_v<=n-1`, set `T_(r_*)=0`,
and, for every dart `a=(v,w)` other than `a_*`, impose

\[
\begin{split}
 T_w&\ge T_v+1-n(1-Y_a),\\
 T_w&\le T_v+1+n(1-Y_a).                                  \tag{6.5}
\end{split}
\]

The selected darts form a cycle cover.  Removing `a_*`, any extra directed
cycle contradicts the strict increment in (6.5); hence the remaining darts
form one Hamilton path from `r_*` to `t_*`.  Along that path the bounds force
the `T` values to be exactly `0,...,n-1`, even though they were declared
continuous.  Thus (6.5) eagerly replaces all quotient subtour cuts.

For the smallest ILP, voltage potentials are unnecessary after (6.5).
Choose signed representatives for the dart voltages and impose

\[
 V=\sum_a\delta_aY_a=17z+\rho,
 \qquad z\in\mathbb Z,\quad 1\le\rho\le16,\quad\rho\in\mathbb Z. \tag{6.6}
\]

This says exactly that the one quotient cycle has nonzero total voltage.
Since 17 is prime, its physical lift is one cycle.  If explicit fibre
potentials are required downstream, the one-hot variables `R_(v,s)` and
path propagation (3.3)--(3.4) are an equivalent, larger interface.

For residence, index a physical coordinate at owner fibre `(v,g)` by its
relative phase `c=j-g in Z_17`.  At a quotient representative `v`, absent
phases have the constant state zero.  For each of its nine present phases
use a one-hot state

\[
                  Q_{v,c,q},\qquad q\in\{1,2,3,4\}.        \tag{6.7}
\]

On a selected dart of voltage `delta`, phase `c` maps to `c-delta` at its
head.  The inserted phase is forced to head state one, the deleted phase is
forced to tail state four, and each of the eight common phases obeys

\[
 Q_{v,c,q}+Y_a\le 1+Q_{w,c-\delta,\min(q+1,4)}
       \qquad(q=1,2,3,4).                                  \tag{6.8}
\]

These transitions are enforced on `a_*` as well.  Deleting them there would
open all 17 developed copies of the quotient dart and would model 17 seams,
not one physical opening.  Equations (6.7)--(6.8) say exactly that every
cyclic positive run has length at least four.  By Theorem 5.1 this is
equivalent to existence of a depth-three-resident literal opening.  A
literal seam is one fibre lift of `a_*` (or of another permitted dart),
selected separately by a phase in `Z_17`; clipped boundary collar ages are
then reconstructed locally.  The quotient gauge is never the physical seam.

The optimized static ILP adds, beyond the exact resource rows,

```text
35,945 orientation binaries
 1,430 continuous order variables
51,480 sparse age binaries       (=1430*9*4)
     2 bounded voltage integers
```

and therefore uses 123,138 structural binaries including the 35,713
resource primaries.  The more transparent dense one-hot voltage/age version
uses 217,518 binaries plus 1,430 order variables.  Starting from the frozen
204,167-variable resource CNF, sparse bit-blasting has about 331,632 Boolean
variables before reified-order auxiliaries.  There are about 2.45 million
age implications and 1.22 million one-hot voltage implications in the dense
potential version; with order adders and cardinalities the static CNF is
roughly 7--10 million clauses.  This is an estimate, not a frozen build.

Consequently the current lazy quotient Benders master already subsumes the
same feasibility condition after separation, and the physical nine-state
master logically subsumes it after literal expansion, but no existing
frozen CNF contains this eager compressed age layer.  A width-1430 Waksman
router can replace (6.5) using `Theta(n log n)` controls, but it must also
route owner labels and certify every consecutive selected catalogue edge;
it duplicates the factor successor relation and is not smaller unless many
downstream rows require absolute quotient positions.  The eager quotient
model also remains strictly narrower than the arbitrary physical master.

### 6.2 Authenticated directed-history snapshot

The implemented eager residence layer uses a smaller equivalent state than
(6.7).  Its source is

```text
82a20aeec38a0ebce6467c2558a1b604a32fbed26b2818d7d2575a82af75dc4a
  scratch/build_k17_marker58_directed_history_master_20260802.cpp
```

and the generated snapshot is

```text
c7bd1ac496a7f6303a334aafd1531ec086faa2fd97a30cd82686bbb1fb7050b6
  marker58_directed_history.cnf
7827cb0c8b7925d5fca73f37d0cd6cbc8567eff51f6609ecca8b6681bf29a7fb
  marker58_directed_history.map.tsv
```

over the exact 204,167-variable, 439,463-clause round-one base.  For a
selected dart `a:u->v`, let `delta_a` be its fibre increment, let `pi_a` be
the deleted coordinate in the tail frame, and let `chi_a` be the inserted
coordinate in that frame.  The builder gives each owner three one-hot
relative-coordinate histories and enforces

\[
 h_0(v)=\chi_a-\delta_a,
 \qquad h_j(v)=h_{j-1}(u)-\delta_a\quad(j=1,2),            \tag{6.9}
\]

together with `h_j(u) != pi_a` for `j=0,1,2`.  The signs are forced by the
normalization `x=rot(rep(x),fibre(x))`: the head fibre is the tail fibre plus
`delta_a`, so a fixed absolute label loses `delta_a` in the head frame.
Along a dart path the forbidden equality is exactly (5.4).  Therefore (6.9)
forbids precisely insertion-to-next-deletion distances one, two and three;
it imposes no stronger deletion-to-insertion or symmetric gap.

The fixed marker rows are reconstructed from the first 58 frozen base
orbits and opening type three by the same literal five-cycle formula as the
rank-ten factor builder.  Every reconstructed row is checked against the
map's facet, two owner orbits, cap and voltage.  Each nonloop option receives
two dart variables with `forward+reverse=x_e`; every fixed edge receives
exactly one direction.  The eight quotient-loop options are killed.  The
base has owner degree two, and the added clauses require at least one
incoming and at least one outgoing selected dart.  Since their sum is two,
both directed degrees are exactly one; no missing at-most row is being
assumed.  The loop ban is lossless for the final connected target: a selected
quotient loop consumes both degrees of its owner and isolates that orbit.

There are 35,937 nonloop edge orbits, hence 71,874 dart variables, and
`1430*3*17=72,930` history variables.  Thus

\[
 204167+71874+72930=348971.                               \tag{6.10}
\]

The added clauses split exactly as

```text
143,292  orientation/self-loop rows
  2,860  incoming/outgoing rows
587,730  history exactly-one rows
2,731,212 dart/history rows              (=71874*38)
---------
3,465,094 added rows
```

and `439463+3465094=3904557` total clauses.  An independent literal parser
finds exactly that many terminated clauses, maximum variable 348,971, no
out-of-range literal, 71,874 contiguous arc-map rows and the declared history
base 276,042.  Two independent source audits agree on the rotation
convention, marker reconstruction, degree implication and history induction.

The frozen input hashes are part of the proof boundary.  The builder checks
every supplied map row but does not regenerate the complete option catalogue
from first principles, and its generic integer parser should range-check
before narrowing in a future fail-closed revision.  Neither issue changes
the authenticated finite instance above; it prevents transporting the audit
to an un-hashed map or witness.

The remote generation directory presently has no SHA manifest, saved
invocation or nonempty builder transcript.  Therefore the hashes above bind
an authenticated stable snapshot, not a self-contained frozen generation
root.  The local independent audit record binds this exact limitation.

This CNF is an eager residence master that is exact on the final connected,
nonzero-voltage quotient face.  Before those gates it describes an oriented
cycle cover with sound three-step histories; a tiny zero-voltage component
whose coordinate is constantly present is outside the claimed equivalence.
The CNF does not contain an eager Hamilton-path/order layer, nonzero-voltage
layer, literal physical seam or boundary collar.  Those remain fail-closed
decoding/separation gates.  Consequently a SAT result still requires
component and voltage replay, while a proofless solver termination cannot
establish UNSAT.  The exploratory Kissat run is outside this theorem until a
complete model or checked proof is frozen.

## 7. What round one and the 4,199 floor prove

The round-one formula contains only two component cuts.  Those cuts eliminate
one old three-component incumbent; they do not instantiate all shores (3.1).
The formula also has no version of (3.2)--(3.4).  Therefore SAT would still
require an independent topology/voltage/residence replay, and UNSAT would be
scoped only to the frozen orbit-tied catalogue and its sound first-round
rows.  The four 1,800-second solver exits are all `124`, so presently neither
conclusion is available.

The 4,199 census proves that no single endpoint-retaining directed C6 or C8
in the enumerated cap-safe connected neighbourhood improves the positive
short-run objective.  It does not justify freezing the factor variables.
In particular, multi-circuit, longer-support and nonlocal rethreading remain
live master moves.

## 8. The 37 units are not a Hall/DM obstruction

Each round-one unit clause fixes one residual primary to zero because the
other edges of its incumbent short-run bracket are protected.  The 37 units
hit 37 distinct facets, 37 distinct caps and 74 distinct owner endpoints.
They are valid lazy rows in the frozen protected quotient catalogue, not
globally forbidden geometric edge types.

Define the facet--owner support graph by joining `(f,o)` when some live option
on facet `f` uses owner `o`.  Define the missing-cap--facet graph by joining
`(u,f)` when some live option on `f` covers missing cap `u`.

### Theorem 8.1 — exact projection verdict

Deleting all 37 unit options creates no new Hall/DM obstruction in the
facet--owner support projection.  In the missing-cap--facet projection it
leaves zero Hall deficiency and no left-deficient DM component, with the
missing caps taken as the left shore.

#### Proof

An independent O3 C++ reconstruction finds that every deleted option's two
facet--owner incidences have alternative live options.  Hence the support
graph is literally unchanged, with 9,750 arcs before and after.  Therefore
all its Hall shores and its DM decomposition are unchanged; the unit rows
cannot create a new obstruction in this projection.  This statement does
not promote the projection audit into a new joint facet--owner matching
certificate.

The unit deletions remove 36 distinct facet--cap arcs, from 35,497 to 35,461,
but the minimum cap degree remains four.  Exact Hopcroft--Karp matching
saturates all 1,086 missing caps into the 1,198 residual facets both before
and after deletion.  Thus Hall deficiency and the number of unmatched left
DM vertices are zero.  `square`

This theorem does not solve the joint factor.  A primary option atomically
couples two owner endpoints, one facet and one cap; weighted owner degree,
connectivity, voltage and all later residence rows remain correlated.  Any
remaining obstruction may still lie in the unchanged facet--owner
projection or, decisively, in the correlations retained only by the joint
master.  What is proved here is that the 37 deletions create no new
facet--owner projection obstruction and leave the cap--facet projection
zero-deficient.

## 9. Variable-staircase no-go for the fixed connected order

Changing only the opening or monotone depth/deadline particles cannot rescue
the original connected `double_fusion` cycle of length `W=24310`.  For a cut, let
`a_0<...<a_m` be the relative internal starts of its length-two positive
runs and define

\[
 G_2=\max\{a_0+2,\ \max_i(a_{i+1}-a_i+2),\ W-a_m\}.         \tag{9.1}
\]

The exact all-cut audit checks both orientations and all 24,310 cuts.  Every
cut has

\[
                              G_2=36.                        \tag{9.2}
\]

The two-gap staircase theorem gives

\[
 \operatorname{Loss}\ge2W-2G_2=48548>7401.                \tag{9.3}
\]

Consequently, loss at most the scalar budget 7,401 would require

\[
 G_2\ge\left\lceil{2W-7401\over2}\right\rceil=20610.       \tag{9.4}
\]

Thus the fixed order fails by orders of magnitude.  This covers every
monotone three-particle arbitrary-start/deadline staircase in the audited
class, in both orientations.  It does not rule out rethreading the factor or
leaving that staircase class.

### Corollary 9.1

The common master must leave the factor selection and chronology variables
free.  Cut and age variables cannot repair its flat depth-three residence.
Within the audited monotone three-particle staircase/common-master face,
cut, start, deadline and compiler choices cannot repair the frozen connected
order.  The certified alternatives are to rethread the factor or leave that
staircase class.

## 10. Exact residual closure at the `10+33` incumbent

Let `I` be the independently replayed Pareto state with model SHA-256

```text
39a2be5af7e396cb5114b95c7d16ae4456caea0f114a74dbe53922295fac8f55
```

It selects one live option on every residual facet, selects no unit-banned
primary, satisfies all 316 frozen blocker rows and both recorded component
cuts, but has ten bad owners and 33 missing caps.  Its owner loads are exactly
five of degree one and five of degree three, so its squared owner penalty is
ten.  In particular `I` is not a two-factor: it has no unique chronology, and
connectivity, voltage and transition-label residence are not yet meaningful
for it.

The reported owner-exact, blocker-exact comparison point with 83 cap holes is
the opposite Pareto endpoint, not a completion and not a closure certificate.
No argument below infers feasibility from either marginal projection or from
interpolating between these two debt vectors.

### 10.1 Signed switch master

For each residual facet `f`, let `e_f^0` be its choice in `I`.  A switch atom
`a=(f,e_f^0->e)` has variable `z_a`; impose at most one switch per facet and
interpret no switch as retaining `e_f^0`.  Define the exact signed deltas

\[
 \Delta_o(a)=m_o(e)-m_o(e_f^0),\qquad
 \Delta_c(a)={\bf1}_{u(e)=c}-{\bf1}_{u(e_f^0)=c},          \tag{10.1}
\]

and define `Delta_B(a)` and `Delta_S(a)` analogously for blocker load and
shore-crossing load.  If `b_o=d_I(o)-2`, `L_c^I` is the incumbent cap load,
`q_B^I` is its blocker load and `chi_S^I` its shore load, the exact residual
rows are

\[
 b_o+\sum_a\Delta_o(a)z_a=0,\qquad
 L_c^I+\sum_a\Delta_c(a)z_a\ge1,                          \tag{10.2}
\]

\[
 q_B^I+\sum_a\Delta_B(a)z_a\le |B|-1,qquad
 \chi_S^I+\sum_a\Delta_S(a)z_a\ge2.                      \tag{10.3}
\]

Every option's two owner endpoints remain one atomic column.  The red/blue
symmetric difference of an owner-exact repair consists of alternating trails
joining the five deficit tokens to the five excess tokens, plus balanced
alternating circuits.  The 33 missing caps seed provider trails or circuits,
but a balanced circuit may still be forced by cap survival, a topology shore,
voltage or residence.  It is therefore unsound to retain only marginal
owner--facet or cap--facet matching edges.

Only after (10.2) makes every owner degree two may the min-cut, voltage and
transition-label oracles run.  A component supplies (3.1), zero voltage is
excluded by (3.2)--(3.4) or an exact full-choice no-good, and a short run
supplies (5.1) using the congruence (5.4).  Each new row is translated back
to signed switch form and retained.

### 10.2 Closure and the two different proof obligations

The complete switch-constraint hypergraph has one row node for every facet,
owner, cap that can gain or lose a provider, blocker, topology shore,
zero-voltage escape support, and possible transition-label motif.  Join an
atom to every row on which its signed delta is nonzero.  Seed the ten violated
owner rows and 33 missing caps, and later seed every separated topology,
voltage or residence row.  Alternating row-to-atom and atom-to-row expansion
is the unique least separator-closed repair collar.  It may be the entire
catalogue; a finite implementation that has not priced every omitted row is
only an increasing under-approximation.

Let `F` denote the full master after complete lazy separation and let `K` be
a proposed editable facet collar.  Put

\[
 F_K=F\ \wedge\ \bigwedge_{f\notin K}(x_{e_f^0}=1).       \tag{10.4}
\]

There are two opposite certificates:

* If `F_K` is UNSAT, every repair must escape the collar, giving the exact
  Benders row

\[
 \sum_{f\notin K}(1-x_{e_f^0})\ge1.                       \tag{10.5}
\]

* The exterior may be frozen as containing **every** repair only after the
  escape formula

\[
 F\ \wedge\left[\sum_{f\notin K}(1-x_{e_f^0})\ge1\right] \tag{10.6}
\]

  is itself proof-UNSAT.  Equivalently, every exterior incumbent choice is a
  proved backbone of `F`.

A contraction certificate and a completeness certificate are different.
Frozen edges may be contracted into maximal paths only when every internal
owner has both incidences frozen and every unfrozen incidence is an explicit
portal; each path must export its endpoints, signed voltage and exact
depth-three DFA transfer.  This evaluates a chosen exterior exactly, but it
does not prove (10.6).  Without (10.6), residual SAT is a valid witness while
residual UNSAT is scoped and can yield only an escape row such as (10.5).

### 10.3 Frozen shell-zero cut and active shell one

The exact shell-zero restriction keeps 53 facets and 1,715 live options,
pinning 33,998 exterior primaries.  It is the literal 439,463-clause
round-one CNF plus those pins, for 473,461 clauses.  Byte/semantic replay
passes, and DRAT-trim verifies UNSAT.  This proves only `F_round1,K0` UNSAT,
but that is already enough for the globally valid escape row (10.5), because
the eventual full master is a strengthening of `F_round1`.

The retained 32-clause core contains four base clauses and 28 negative
primary assumptions.  Hence the following much sharper Benders row is valid
for every round-one completion:

\[
 \sum_{v\in V_0}x_v\ge1,                                  \tag{10.7}
\]

where

```text
V0 = {11594,11904,11931,11952,20856,20857,21720,22330,
      24775,25195,25663,25960,26027,26414,26431,26487,
      26515,26991,26995,29112,30094,33729,33730,33764,
      33765,34009,34873,35279}.
```

Primary 25195 is already unit-banned; retaining it makes the literal core
replay exact and it may be deleted when simplifying (10.7).
Indeed, setting every variable in `V0` false makes the two long core clauses
force primaries 4706 and 4707.  The remaining base clauses
`40258 or not 4706` and `not 40258 or not 4707` then contradict.  This direct
resolution proves (10.7) independently of the retained `core_replay.out`,
which replays the full collar CNF rather than the extracted 32-clause file.
Geometrically, the pinned boundary leaves caps 23227 and 23229 dependent on
the two incompatible choices 4706 and 4707 of the same facet 2903.

Shell one is the current exact boundary: 1,016 editable facets, 30,733
editable options and 4,980 exterior pins, for 444,443 clauses.  Its build and
literal prefix/pin replay pass, but its solver is active and has no result.
Therefore shell zero is a proved no-go, shell one is UNKNOWN, and neither
proves that the shell-one exterior contains every repair.  No global
feasibility or infeasibility follows.

### 10.4 Coordination with the compound chronologies and round two

The independently frozen compound seed has model SHA
`7cc0345dda66052154102843a82daa3e38d7b58828127f5ebab8d99c40d82aa9`
and residence-audit SHA
`5813f5b3385c2784572a91bc9aa9875131abb2e6929c33a5693ee6d1a0718abb`.
It is owner/rank-eight/rank-ten exact, connected with nonzero voltage, and has
`2210+1870=4080` positive runs of lengths two and three.  It still selects
old unit-banned primaries and has not passed the 316 round-one rows.  It is
therefore a literal chronology/pricing seed for compound rethreading, not a
round-one-feasible incumbent and not an exterior that may be merged with
`I` without re-evaluating every row.

The promoted `paired_escape005` chronology is stronger.  Its model and factor
hashes are

```text
452d47edb23ca9f31ad7885546c8d22e3d7222d0bb572e171190ac5ee7570bb0
  paired_escape005.model
19bb99264cd592db409c9b3dcb5cd6d59309e54bc64067780b2e426471381aa8
  paired_escape005.factor.tsv
```

Literal replay gives one connected nonzero-voltage factor with exact
rank-eight owners and all rank-ten caps.  Its positive-run census is

\[
 N_2=2176,\qquad N_3=1853,\qquad N_{<4}=4029=237\cdot17.   \tag{10.8}
\]

Extraction gives 237 exact quotient motif orbits, all with 17 physical
translates and no all-fixed obstruction.  Of these, 168 were already among
round one's 316 rows and 69 are novel, so the cumulative active bank has

\[
 316+237-168=385                                         \tag{10.9}
\]

rows.  The 69 new clause arities are `3/1/33/32` at arities one through four;
their
new unit primaries are `4726,25040,25229`.  The byte-preserved cumulative CNF
has 204,167 variables and 439,532 clauses, SHA-256

```text
272d0f23bedd0b22c830c4bc08883ad9bf7883de61ce1f448e648df9752f2e93
```

with merge-audit SHA
`c61fc031dadecba244b182a693b7a837f529c9f2db5a3652aef5e500ec1e0925`.
These 69 rows are mandatory new Benders constraints and potential closure
seeds.  A row becomes a seed for the `10+33` collar only if `I`, or a later
separated incumbent, violates it; no `I`-against-69 replay is claimed here.
The round-one shell-zero UNSAT and its cuts remain valid under this
strengthening, but shell one was built from the weaker 316-row CNF and cannot
certify a round-two SAT witness without replaying all 69 new rows.

The independent flip-gap validator has source SHA
`e6d2c4bffb727a685acccdc116818ae128424372e67fe68d31b2f4588bd297ec`.
Its insertion-to-next-deletion scan agrees exactly with direct run scanning:
5,372 on `c68b.double_fusion` and 4,029 on `paired_escape005`.  The audit
hashes are respectively
`e16edb0a11373096e54a3ed376a1348e9505aed7b639f3c2abb3b13c42ade772`
and
`2c685ce8e876aa37e7ded871ab361e4185ed5d44e4b370db2376fec4ff5c7ab4`.
This independently validates the separator semantics in Theorem 5.2; it does
not make the finite 385-row bank complete.

### 10.5 Exact partial-MaxSAT/Benders ladder

Let `H_2` be the exact resource/protected CNF and the two recorded component
cuts, but not the 385 residence clauses.  During Benders separation, let `H`
be `H_2` strengthened by every accumulated hard topology/voltage cut.

For the positive budget, a key `c` is a genuine `Z_17` orbit of a coordinate
and an undirected bracket path, modulo global reversal.  Store one oriented
representative for the transition-label replay, but do not charge its reverse
as a second defect.  Distinct coordinate/bracket orbits that happen to have
the same primary support retain distinct bits, or one exactly weighted bit.
Let `mathcal C` be this ledger.  With negative support clause `C_c`, introduce
relaxation bit `y_c` and impose

\[
 H,\qquad C_c\vee y_c\quad(c\in\mathcal C),\qquad
 \sum_{c\in\mathcal C}y_c\le B.                           \tag{10.10}
\]

The counter is an ordinary incremental cardinality network or sequential
counter of size `O(|mathcal C|B)`.  It becomes `O(385B)` only if the occurrence
merge verifies that the 168 support overlaps are the same canonical motif
orbits.  With `H=H_2`, budget `B=0` needs only clause supports and is exactly
the cumulative hard round-two model; later hard Benders rows only strengthen
it.  The frozen 385 merge deduplicates clause supports, not labelled
occurrences, so it is not by itself an authenticated positive-budget ledger.
Before claiming an exact `B>0` result, merge the old and current occurrence
tables by the canonical key above and replay every multiplicity.

Independently of that pending ledger merge, the connected
`paired_escape005` factor is an exact witness with 237 quotient short-run
orbits, hence 4,029 physical runs.  Thus it supplies the rigorous upper bound
`B<=237` for the occurrence objective, and testing `B=200,150,...` can seek
nonlocal factor jumps without presuming that the monolithic zero budget is
easy or feasible.  In the equivariant master `B` counts quotient orbits and
the physical count is `17B`; in an arbitrary physical master it counts literal
brackets.

For an arbitrary linear physical master, relax the seam-aware row (4.3); for
the connected equivariant master, relax the 17-translate row (5.1).  The
oriented representative must satisfy the insertion-to-next-deletion test, and
no symmetric deletion-to-insertion gap is charged.

Every integral owner-exact candidate is decoded before acceptance.  A new
component shore or zero-voltage certificate is added hard.  The exact
transition-gap scan adds every missing occurrence-labelled motif with a fresh
relaxation bit and extends the same cardinality counter.  Therefore a SAT
result at budget `B` is certified only after topology, voltage and motif
separation reach a fixed point.  A proof-UNSAT result over the full option
catalogue is already valid at that budget even before motif pricing closes,
because every omitted sound row can only strengthen the formula.  UNSAT over
a pinned collar remains scoped unless the exterior has the completeness
certificate (10.6).  This ladder is a search interface, not a global result,
and no duplicate global solve is launched here.

### 10.6 Round-four C10 control and exact canonical reconciliation

The clean-C14 expansion first produced the canonical bank

\[
 385+220-192=413.                                         \tag{10.11}
\]

Thus its novel count is 28; the earlier phrase "25 novel" referred instead
to the raw-C14 increment `222-197`.  The 413-row bank has SHA-256

```text
29773f2946d1a00fc7743176d84c9b2e4e9c4e2ea929cd5dd501e412adf66145
```

and arities `45/17/196/155`.  The exact old-bank positive control proves
`B385=192`, but the same clean factor has `B413=220`.

The new C10 factor is the active control.  Its model and factor hashes are

```text
4e49661a975e3768eb931b51109e5c2e7856234cea9485d053d4a0b99ab4a540
  c68b.floor3502.model
33d6719dbd6f5bc49e3b7c31f0350385c9ac2de035e767a82680ca137e5cf7be
  c68b.floor3502.factor.tsv
```

Literal replay gives all 1,430 quotient facet/owner edge orbits, every
rank-eight colour, all 19,448 rank-ten caps, all 3,944 protected edges, one
quotient component, nonzero voltage and one 24,310-owner physical cycle.
The exact transition-gap census is

\[
             1938+1564=3502=206\cdot17.                  \tag{10.12}
\]

Hence C10 is not resident.  It violates only 198 rows of the old bank, so it
constructively crosses the restricted target `B413<=200` with slack two,
but its fully priced count is 206 quotient motif orbits.  True `B<=200`
therefore remains six motif orbits, or 102 physical short runs, away.

Canonical sort/unique reconciliation gives

\[
       |C_{413}|=413,\qquad |C_{10}|=206,\qquad
       |C_{413}\cap C_{10}|=198,\qquad
       |C_{413}\cup C_{10}|=421.                          \tag{10.13}
\]

The authoritative 421-row union has SHA-256

```text
8caaf19d74b161146e312a99e6e25d46d8e2e67b9e20785a4382bd066dc28106
```

and its merge audit has SHA-256
`ea8f828a525bfafa234a3f6af78bd47fb0fc72385022bf761a424857eee36bbc`.
Its arities are `45/17/201/158`.  The eight new clauses have arities five
ternary and three quaternary; no new unit row is created.  The provisional
raw-text union of size 585 and the early `novel_vs413` text difference are
rejected: opposite literal orders made them noncanonical.  Only the
sort/unique literal-vector union 421 may be used.

```text
-34901 -32071 -14544 -11678 0
-32418 -27557 -9194 -8831 0
-22900 -12851 -5223 0
-19024 -2712 -2193 0
-18679 -18659 -18174 0
-18103 -3969 -545 0
-18058 -8758 -952 0
-15156 -14597 -9518 -4293 0
```

The exact Pareto ledger is now:

| factor | known score | true motifs | runs | `(H11,H12,H13)` |
|---|---:|---:|---:|---:|
| raw C14 | `B385=197` | 222 | 3,774 | `(1836,374,34)` |
| clean C14 | `B413=220` | 220 | 3,740 | `(1836,408,34)` |
| C16 | `B413=213` | 216 | 3,672 | `(1836,408,17)` |
| C10 | `B413=198`, `B421=206` | 206 | 3,502 | `(1802,425,17)` |

All listed upper values are passive exact cyclic-union diagnostics.  C10 is
the residence/rank-11 lead, C16 has fewer rank-12 holes, and raw C14 remains
the rank-12 lead.  None of those marginal upper advantages can be
transplanted to another factor.  For a compound move use exact set deltas

\[
 \Delta B=|M'\setminus M|-|M\setminus M'|,
 \qquad
 \Delta H_r=|H'_r\setminus H_r|-|H_r\setminus H'_r|.       \tag{10.14}
\]

These deltas are additive only when the affected target sets are disjoint
and exact baseline/final provider loads certify that no unchanged alternate
provider masks a loss.  Disjoint provider occurrences alone are not enough.

For an upper-provider occurrence `p`, let `R_p` be all required surviving
edge/turn literals and let `q_l` be the truth value of required literal `l`.
Its exact availability bit satisfies

\[
 a_p\le q_l\ (l\in R_p),\qquad
 a_p\ge1-|R_p|+\sum_{l\in R_p}q_l.                        \tag{10.15}
\]

For existential deck coverage put `v_t=OR_(p in Prov(t)) a_p`; for optional
or capacitated providers first select `lambda_p<=a_p`, impose the matching or
capacity rows, and put `v_t=OR lambda_p`.  In either case impose

\[
 v_t\ge\lambda_p\ (p\in\operatorname{Prov}(t)),\qquad
 v_t\le\sum_p\lambda_p,\qquad u_t+v_t=1,
 \qquad H_r=\sum_{\operatorname{rank}(t)=r}u_t,            \tag{10.16}
\]

with `a_p` substituted for `lambda_p` in the existential case.  This is an
exact exported hole census.  The lone covering inequality
`sum(lambda_p)+u_t>=1` would be exact only at a minimizing optimum.

The proof-safe priority is a dynamically priced true motif bound `B<=200`,
then sequential minimization of `(H11,H12,H13)`.  The achieved `B413<=200`
was only a restricted-bank generator.  Even `B421<=200` for a new factor is
not terminal: decode it, price every current motif, append every new row and
accept only at a CEGAR fixed point.  A different lexicographic order must be
declared and proved, not hidden in a scalar score.

### 10.7 Dominant rank-13-complete `final2754` Pareto rebase

The new upper/source control is the exact factor

```text
edc937949e741382fbf53cb80f1d32aa9c7d7f008f60894682ecac0b1e7747a7
  round000.model
fac9ad6c29f39a89c9cdce4e88f231e5f73725535e6e1aea47aeb3f43aaaddc7
  final2754.factor.tsv
```

It passes every facet, owner, rank-eight, rank-ten-cap, protected-path,
quotient-connectivity and nonzero-voltage gate and develops to one physical
cycle.  Its exact positive-run census is

\[
             1377+1377=2754=162\cdot17,                  \tag{10.17}
\]

so it is not resident.  Literal evaluation of the supplied 445-row bank
gives `B445=142`; the audit has SHA-256
`e154178466f17d528d7b2605329a0bcd749c8fcdbae273f8b81ed09c00c4df79`.
The exact current motif count 162 is already below 200, so this factor crosses
the fully current-priced partial-MaxSAT threshold, not merely the old-bank
projection.  The difference `162-142=20` must still be canonically joined
against the bank before promoting a next-round support file; it is not by
itself a claim of 20 distinct novel clauses.  Residence requires score zero,
not merely at most 200.

The exact cyclic upper leave is

\[
                  (H_{11},H_{12},H_{13})=(1853,357,0),    \tag{10.18}
\]

with ranks 14--17 complete.  The upper audit SHA-256 is
`8f490dc5740feff1e0c130b4d1177de171910af9ce9ab48a82c8c2cf1194bf03`.
It strictly improves `final2992` in residence, rank 11 and rank 12 while
retaining rank-13 completeness, so `final2992` is no longer an active Pareto
root.  It is also the best rank-12 and residence point in the displayed
ledger.  C10, C16 and raw C14 still have fewer rank-11 holes, so their exact
provider columns are not discarded.

Any upper/source coupling rooted at `final2754` must use the exact
availability/coverage rows (10.15)--(10.16) and replay shared target loads.
Rank-13 completeness is a real new boundary condition, but it does not bind
the 1,853 rank-11 holes, 357 rank-12 holes, the 2,754 residence defects, a
literal source atlas, exterior intervals or compiler cells.  In particular
this factor is neither a resident host nor a word.

## 11. Fail-closed Benders order and downstream interface

A complete solve must iterate:

1. enforce (2.1)--(2.3) and all protected rows;
2. in a residual solve, enforce (10.2)--(10.3), retain every proof-derived
   escape row, and do not freeze an exterior without (10.6);
3. separate quotient or physical shores by (3.1);
4. enforce nonzero quotient voltage by (3.2)--(3.4), or reject a zero-voltage
   integral incumbent by an exact scoped no-good;
5. separate every short physical motif by (4.3), or every quotient motif by
   (5.1) and (5.4) in the connected equivariant subclass; attach the exact
   occurrence relaxation bit only when running (10.10); alternatively use
   the eager directed histories (6.9), while retaining the separate
   component and voltage gates;
6. materialize and replay the one physical chronology, seam and age states;
7. stop only when no resource, exterior-column, topology, voltage or residence separator
   fires.

The successful master certificate must export the exact selected edge set,
oriented successor relation, physical seam, fibre potentials and all
coordinate age states.  Deeper rank-11--13 interval-union witnesses, the 986
joint five-state source-atlas entries and the terminal compiler live graph
must be conditioned on that exported tuple.  Their Hall/max-closure and
maximal-common-cap replay cannot be compiled from marginal factor counts.

No such master certificate is currently frozen: the global round-one solves
timed out UNKNOWN and every frozen chronology seed still violates residence.
Therefore this lane does not claim or launch deeper-upper/compiler closure.

## 12. Frozen artifacts and exclusions

The theorem/audit package is frozen under

```text
/home/amodo/or15/work/r2_k17_residence_master_round1_20260802
scratch/r2_k17_residence_master_round1_20260802
```

The package manifest `FROZEN_SHA256SUMS` has SHA-256

```text
4357dcba192558b84d2e2eb7849651d32f8f21d8cd481f6832ecbffe5154e1ed
```

and passes `sha256sum -c`.  Its new projection artifacts include

```text
e0f1f784dc027ba558263d25af5b3123b0e3aeba2684fbc7e3ad7cda8a0a7a92
  audit_k17_round1_unit37_hall_dm_projections_20260802.cpp
23920a684929f5a67758cedcc3ea409ccd5303d4c0a9697ff39cec3f03ff7f9c
  unit37_hall_dm.audit.json
```

The variable-staircase audit is bound by

```text
0c85b7a1903c71eff20b0eea47c6f63d7fac4edd509875c582d5a644d0af99ef
  audit_v_k17_marker58_deadline_particles_20260802.cpp
b54ab366b43f892bac94b6b1972ddbfbee8c0407cebb7804914e43f3be23a8d8
  marker58.deadline.audit.json
```

The exact transition reduction is independently frozen as

```text
07c18bb9ff3b7e3a7cfb69a4abe4ee9ac0bc6ee81a10992fb3bfcf7d91cc7c67
  MATH_THEOREM_LONG_RUN_MIDDLE_LEVELS_RESIDENCE_REDUCTION_20260802.md
```

The package also binds the `10+33` independent debt replay, shell-zero CNF,
DRAT and checker transcript, immutable shell-one pre-solve boundary, the
385/413/421 blocker lineage, raw/clean C14 and C16 controls, the C10 factor
and canonical round-four merge, the rank-13-complete `final2992` comparator
and dominant `final2754` control,
both independent flip-gap outputs, and the directed-history source-semantics
snapshot audit.  No broad factor or SAT search was launched by this lane.
The external exploratory directed-history Kissat run is not included in any
verdict.

The exact open object is the joint master above.  Source binding, ranks
11--17, exterior windows, compiler/common-cap matching, regeneration and a
universal word remain outside the proved scope.
