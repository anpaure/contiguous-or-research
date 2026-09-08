# Thread K: exact Catalan-leave correction flow, chronology SDR, and minimal obstructions

Date: 2026-07-29

## 0. Verdict

The correction problem has an exact finite necessary-and-sufficient
flow/representative formulation.  Its fixed-data core is totally unimodular,
but the simultaneous Catalan choices are not a flow.

The positive theorem is this.  In the physical child Boolean incidence
graph, fix one protected path occurrence for every required lower `q=2,3`
target and, at every required upper depth `q`, one protected **`q`-edge**
occurrence for every upper target.  If the union `F` of their incidence arcs
has degree at most two, then it extends to a literal lower-rainbow child factor
if and only if one explicit family of residual cap-two cut inequalities holds.
The completion is an integral max-flow.  Relative to an activated four-sector
baseline, every such completion decomposes into literal alternating factor
switches.

Residence and compiler ports remain separate, exact finite conditions:

* residence is acceptance by a positive-run automaton, equivalently exclusion
  of every selected bracketed path `0 1^ell 0` with `1<=ell<=d`;
* for the final maximal erosion `P`, simultaneous choice of a one-core and a
  saturating port matching is exactly a nearest-neighbour constrained SDR.

The forced Catalan leave has an even earlier activation gate.  Choosing one
upper occurrence and its two `Z`-ports for each old upper target is a
capacitated colored pair-SDR, equivalently a 3-uniform exact matching.  Fixed
occurrences give the audited cap-two network, but occurrence choice and port
choice together are not TU.  A four-color/four-resource instance is perfectly
regular, has a fractionally exact solution and maximal ordinary resource
neighbourhoods, yet has no integral pair-SDR.  This is minimal in the
two-port abstraction.  Hence biregularity or ordinary expansion alone cannot
prove the missing Catalan theorem.

The literal Johnson hierarchy is also sharp.

1. For `r>=4`, a three-row common/private-cofacet motif is the first possible
   fixed-`I` cap-two Hall failure after singleton degree checks.
2. A forced Boolean incidence `C6` passes every cap-two cut but its contracted
   `A`-cycle has trace `110`, so old-coordinate residence fails.
3. A different alternating `C6` is the smallest literal degree-preserving
   switch atom and, when embedded in one common full factor completion, can
   polarize lower and upper `q=2,3` witnesses onto opposite shores.
4. Two adjacent compiler assignments omitting one required envelope
   coordinate are the smallest joint one-core/port obstruction, even when
   the static target-position graph passes Hall.

These are scoped obstructions to generic composition.  None is asserted to
occur in every Catalan atlas, and no counterexample to the desired recursion
is claimed.  The exact remaining theorem is to exploit the actual
Catalan/Johnson geometry to choose one common pair-SDR, residence-safe
chronology, all-shadow witness section, and port SDR.

No search, SAT solver, or long computation was used.

## 1. Physical incidence dictionary

Let the old coordinate set have size `2r-1`, and put

\[
 \Omega^+=\Omega\cup\{x,y\},\qquad |\Omega^+|=2r+1.
\]

The child lower and upper middle layers are

\[
 \mathcal L=\binom{\Omega^+}{r},\qquad
 \mathcal U=\binom{\Omega^+}{r+1}.
\]

Let

\[
 \mathcal B=(\mathcal L,\mathcal U;E),\qquad
 E=\{(R,Q):R\subset Q\}.                              \tag{1.1}
\]

Both shores have the same cardinality, and `B` is `(r+1)`-regular.

### Lemma 1.1 (incidence-factor dictionary)

An arc-simple set \(X\subseteq E\) defines a lower-rainbow spanning Johnson
2-factor on `U` if and only if

\[
 \deg_X(R)=2\quad(R\in\mathcal L),\qquad
 \deg_X(Q)=2\quad(Q\in\mathcal U).                    \tag{1.2}
\]

#### Proof

The two selected upper neighbours of a lower row `R` are distinct
rank-`r+1` supersets of `R`; they differ in exactly one coordinate and hence
form a Johnson edge with intersection color `R`.  Every lower row is used
once.  Conversely, each lower-rainbow Johnson edge supplies its two incidence
arcs, and upper factor degree two is exactly the right equation in (1.2).
\(\square\)

Thus the Catalan-leave factor of the preceding report is a literal point of
the bipartite 2-factor polytope.  Working physically avoids quotient phase
and short-orbit ambiguities.  A symmetric quotient version must restore
actual orbit weights and phases afterwards.

Once an activated baseline `X^0` has been chosen, fix an allowed correction
atlas

\[
                       \mathcal A\subseteq E,          \tag{1.3}
\]

containing it.  Equivalently, one may fix a universal `A` first and require
the later activation choice to satisfy (X^0(\kappa)\subseteq\mathcal A).
Taking `A=E` allows every physical factor; a restricted atlas records the
intended switch library or locality budget.

## 2. The exact occurrence-transversal/cap-two gate

Return temporarily to the old factor notation of the preceding report:

\[
 C_i=T_i\cap T_{i+1},\qquad V_i=T_i\cup T_{i+1}.
\]

Let

\[
 \mathcal V=\binom{\Omega}{r+1},\qquad
 \mathcal Z=\binom{\Omega}{r-2},
\]

and let

\[
 \mathcal O(V)=\{i:V_i=V\}                            \tag{2.1}
\]

be the occurrence fibre of the old upper target `V`.

For every `V`, define its pair-port family

\[
 \mathscr E_V=
 \left\{
 (i,\{Z,Z'\}):
 i\in\mathcal O(V),\ Z\ne Z',\ Z,Z'\subset C_i
 \right\}.                                            \tag{2.2}
\]

### Theorem 2.1 (pair-SDR equivalence)

There exists an upper occurrence transversal `I`, together with a simple
cap-two factor `K` in the graph `P_I` of the preceding report, if and only if
one can choose one representative

\[
                     \kappa(V)\in\mathscr E_V          \tag{2.3}
\]

for every \(V\in\mathcal V\) so that every resource
\(Z\in\mathcal Z\) belongs to exactly two chosen pairs.

#### Proof

Given `(I,K)`, the selected occurrence over `V` is the unique member
\(i\in I\cap\mathcal O(V)\), and its two `K`-neighbours give the pair in
(2.3).
Conversely, take the occurrence named by each representative into `I` and
join it to its named pair.  Every selected occurrence has degree two, every
`Z` has degree two, and distinctness of the pair makes the graph simple.
\(\square\)

Equivalently, use binary variables `p_(i,{Z,Z'})` with the colour equations

\[
 \sum_{(i,P)\in\mathscr E_V}p_{i,P}=1
 \quad(V\in\mathcal V),                              \tag{2.4a}
\]

and the resource equations

\[
 \sum_{V}\sum_{(i,P)\in\mathscr E_V:\ Z\in P}p_{i,P}=2
 \quad(Z\in\mathcal Z).                               \tag{2.4b}
\]

Each column of this system meets one colour equation and two resource
equations.  It is a capacitated pair-SDR, or a 3-uniform exact matching, not
a bipartite network matrix.

### Theorem 2.2 (fixed-transversal cap-two flow)

For fixed `I`, a simple `K` exists if and only if, for every
\(A\subseteq\mathcal Z\),

\[
 \boxed{
 \sum_{i\in I}\min(2,\deg_A(i))\ge2|A|.}              \tag{2.5}
\]

This is the integral network

\[
 s\longrightarrow Z\ [2],\qquad
 Z\longrightarrow i\ [1],\qquad
 i\longrightarrow t\ [2].                            \tag{2.6}
\]

This repeats the exact fixed-`I` theorem only to locate the new boundary:
`I` alone is a partition choice and `K` for fixed `I` is TU, but their joint
choice is Theorem 2.1.

There is one useful positive sufficient condition.  Every selected right
column `C_i` has degree `r-1`, and the two shores have equal size.  If
`r>=3` and every left `Z` has degree at least `r-1`, then all left degrees
equal `r-1`; the graph is biregular and two edge-disjoint perfect matchings
give `K`.

Before choosing `I`, (2.5) gives the necessary cut

\[
 M(A):=
 \sum_{V\in\mathcal V}
 \max_{i\in\mathcal O(V)}\min(2,\deg_A(i))
 \ge2|A|.                                              \tag{2.7}
\]

It is not sufficient: the maximizing occurrence may depend on `A`, whereas
one common transversal must pass every cut.

### Proposition 2.3 (first literal fixed-`I` flow defect)

Assume `r>=4` and every left vertex has degree at least two.  No cap-two cut
on one or two left vertices can fail.  The first possible failure has three
left vertices and, in Boolean containment geometry, is uniquely of the
following form:

\[
 Z_j=C^*\setminus\{a_j\},\qquad
 N_I(Z_j)=\{C^*,C_j\}\quad(j=1,2,3),                  \tag{2.8}
\]

where the `C_j` are private cofacets.  Its defect is exactly one:

\[
 \sum_C\min(2,\deg_{\{Z_1,Z_2,Z_3\}}C)
 =2+1+1+1=5<6.                                        \tag{2.9}
\]

#### Proof

For at most two left vertices, every right degree within the set is at most
two, so truncation in (2.5) loses nothing; minimum left degree two supplies
the demand.  For three Boolean `(r-2)`-sets, two distinct sets have at most
one common `(r-1)`-cofacet.  With total incidence at least six, truncated
capacity can fall below six only when total incidence is exactly six and one
cofacet contains all three.  The other three incidences must then be private,
giving (2.8)--(2.9).  The converse is immediate. \(\square\)

This is the smallest actual Boolean cap-flow obstruction.  For `r=3`, a
rank-`r-1` cofacet has only two such facets, so truncation never loses
capacity and minimum left degree two passes every cut.  Realization of the
displayed fixed `I` by the occurrence fibres is a separate question.

## 3. Biregularity does not solve the activated gate

### Theorem 3.1 (minimal regular non-TU pair-SDR)

Take four colours `A,B,C,D` and four resources `1,2,3,4`, each of capacity
two, with port lists

\[
\begin{array}{c|c}
A&12,34\\
B&13,24\\
C&14,23\\
D&12,34.
\end{array}                                           \tag{3.1}
\]

Every colour has two ports, every resource lies in four ports, every
nonempty colour family has resource neighbourhood all four, and weight
`1/2` on every port is fractionally exact.  No integral representative
system exists.

#### Proof

If `A,D` choose the same pair, its two resources are already saturated;
every port of `B` and every port of `C` meets one of them, causing an
overload.  If `A,D` choose different pairs, all four resources have current
degree one.  The chosen `B` and `C` ports must therefore be disjoint
complements.  Neither `13` nor `24` is complementary to `14` or `23`.
Thus no integral choice exists.

For minimality, with two resources only the pair `12` exists.  With three
resources, resource degree two forces the aggregate selected multiplicities
of `12,13,23` all to be one.  The remaining choice is an ordinary perfect
matching between three colours and the three pair types, so fractional
feasibility plus bipartite Hall is integral. \(\square\)

The example is not claimed to embed in the unfiltered Catalan occurrence
atlas.  It proves the exact negative statement needed here: even perfect
capacity ratios and maximal ordinary endpoint expansion do not imply the
joint transversal/cap-two theorem.  A positive result must exploit additional
Johnson containment or chronological structure.

## 4. The leave is a partition-constrained vertex cover

Fix an integer `d>=1`.  Let `G_d` be the conflict pseudograph on parent
edge positions.  It joins two
distinct positions on the same component when their cyclic distance is less
than `d`, and it has a loop at every position of a component of length less
than `d`.  A vertex cover must cover a loop by containing its endpoint, and
an independent set contains no looped vertex.  Put

\[
 \alpha_i=\mathbf1_{\{i\in I\}},\qquad J=I^c.
\]

### Theorem 4.1 (exact new-label residence gate)

The new coordinates `x,y` in the **uncorrected** four-sector factor are
depth-`d` resident if and only if

\[
 \sum_{i\in\mathcal O(V)}\alpha_i=1
 \quad(V\in\mathcal V),                               \tag{4.1}
\]

and

\[
 \alpha_i+\alpha_j\ge1
 \quad(ij\in E(G_d)).                                 \tag{4.2}
\]

Equivalently, `I` is a one-per-fibre vertex cover of `G_d`, or `J` is an
independent set having the exact colour quotas

\[
 |J\cap\mathcal O(V)|=|\mathcal O(V)|-1.              \tag{4.3}
\]

In particular, every component of length less than `d` has empty leave.

#### Proof

The preceding report proved that a gap `g` between consecutive leave
positions creates one `x`-run and one `y`-run of length `g+1`.  Residence
requires `g>=d`.  With at least two leave positions this is exactly pairwise
independence in the distance-`<d` graph.  With one leave position its sole
cyclic gap is the component length, and the added loops exclude precisely
the short case.  The occurrence-transversal equations give (4.1) and hence
(4.3). \(\square\)

On components of lengths `L_c`, the scalar necessary bound is

\[
 |J|\le\sum_c\left\lfloor\frac{L_c}{d}\right\rfloor. \tag{4.4}
\]

Without fibre quotas it is also sufficient.  On one Hamilton component it
is `W>=d Cat_r`.  With (4.1), scalar capacity is not sufficient.

There is a literal local Johnson obstruction.  Fix an `(r+1)`-set `V` and
cycle through

\[
 T_j=V\setminus\{v_j\}\qquad(0\le j\le r).            \tag{4.5}
\]

All `r+1` edges have upper union `V`, while their lower colours are distinct.
Every coordinate has a positive run of length `r`, so this component is
depth-`d` resident when `r>=d+1`.  Nevertheless (4.1) chooses at most one of
these edges into `I` and forces at least `r` consecutive positions into `J`, violating
(4.2) for every `d>=2`.  This is conditional on embedding the component in
a global passing parent; no such global obstruction is asserted.

### Proposition 4.2 (exact forced-interface census)

On a parent component with nonempty leave, let `g_1,...,g_s` be the positive
cyclic distances between successive leave positions and put

\[
 h_t(J)=\sum_{j=1}^s\min(t,g_j);                       \tag{4.6}
\]

set `h_t=0` on a component with empty leave, and sum over components.  Then
`h_t(J)` is exactly the number of `t`-index blocks meeting `J`.  Hence

\[
 h_t(J)\le t|J|,                                      \tag{4.7}
\]

with equality exactly when every leave gap is at least `t`.

In the four-sector child the exact pure-start counts are

\[
 \begin{array}{c|c}
 \text{sector}&\text{pure }q\text{-edge starts}\\ \hline
 X&W-h_q\\
 Y&W-h_q\\
 U&W-h_{q+1}.
 \end{array}                                          \tag{4.8}
\]

Thus the pure-sector start loss is

\[
 2h_q+h_{q+1},                                        \tag{4.9}
\]

at most `7b` for `q=2` and `10b` for `q=3`, where
`b=Cat_r`.  These are window starts, not distinct target holes; duplicates
may survive, and pure-`U` lower windows are not old consecutive lower
windows.

The exact edge census is

\[
 \begin{array}{c|cccccc}
 \text{edge type}&AA&XX&YY&UU&AX&AY\\ \hline
 \text{count}&W-b&W-b&W-b&W-h_2&b&b,
 \end{array}                                          \tag{4.10}
\]

with `h_2` further cross-sector edges from the `T` family.  Hence the number
of sector-interface edges is

\[
 S=2b+h_2,                                             \tag{4.11}
\]

equal to `4b` under depth `d>=2` new-label residence.  The `A/K` cycles
contribute `W-b` pure-`A` starts and are bulk new chronology, not a seam
halo.

At depth `q`, at most `qS` window starts meet a sector-interface edge; the
exact count is the cyclic `q`-neighbourhood sumset of the interface-edge set.
This is again a count of starts, not of distinct holes.

#### Proof

Assign every block start to the next leave position.  Among the `g_j` starts
preceding that leave, exactly `min(t,g_j)` have a `t`-block reaching it,
proving (4.6).  The sector formulas follow directly from the explicit edge
formulas of the preceding report. \(\square\)

## 5. Protected witnesses leave an exact residual flow

Fix a forced incidence set

\[
                         F\subseteq\mathcal A.         \tag{5.1}
\]

Put

\[
 b(v)=2-\deg_F(v),\qquad E_f=\mathcal A\setminus F,   \tag{5.2}
\]

and, for \(X\subseteq\mathcal L\), define

\[
 d_X(Q)=
 |\{(R,Q)\in E_f:R\in X\}|.                          \tag{5.3}
\]

### Theorem 5.1 (protected residual-flow criterion)

There is a child factor `X` satisfying

\[
                         F\subseteq X\subseteq\mathcal A
\]

if and only if

\[
                  \deg_F(v)\le2                       \tag{5.4}
\]

for every incidence vertex and, for every \(X\subseteq\mathcal L\),

\[
 \boxed{
 \sum_{R\in X}b(R)
 \le
 \sum_{Q\in\mathcal U}\min(b(Q),d_X(Q)).}             \tag{CF}
\]

The criterion is integral.  An inclusion-minimal family with positive defect

\[
 \Delta_F(X)=
 \sum_{R\in X}b(R)
 -\sum_Q\min(b(Q),d_X(Q))>0                           \tag{5.5}
\]

is a complete finite obstruction certificate.

#### Proof

Use the residual network

\[
 s\longrightarrow R\ [b(R)],\qquad
 R\longrightarrow Q\ [1]\ ((R,Q)\in E_f),\qquad
 Q\longrightarrow t\ [b(Q)].                         \tag{5.6}
\]

The total demands on the shores agree because `|L|=|U|` and every forced
arc contributes once to each shore.  For fixed source-side `X`, minimizing a
cut independently at `Q` contributes `min(b(Q),d_X(Q))`.  Max-flow/min-cut
gives (CF).  Integral capacities give an integral residual flow, whose union
with `F` has degree two on both shores.  Conversely, restricting any
completion to `E_f` gives such a flow. \(\square\)

Give baseline incidences cost zero and other allowed incidences cost one.
Minimum correction is then an integral min-cost flow.  If `F` already
contains nonbaseline incidences, add the fixed constant
\(|F\setminus X^0|\) to the residual optimum (equivalently, minimize cost on
the full final incidence vector).  The result is the number of added
incidences, and the incidence symmetric difference has twice that size
because both factors have the same number of arcs.

### Corollary 5.2 (literal alternating switches)

Let `X^0` and `X` be two incidence factors.  Orient every incidence in
`X\setminus X^0` from `L` to `U` and every incidence in `X^0\setminus X`
from `U` to `L`.  The resulting digraph is balanced at every vertex and
decomposes into directed alternating cycles.  Toggling these cycles gives a
sequence of literal exact-factor switches from `X^0` to `X`.

This also identifies an important scope boundary.  If `A=E`, no witness is
protected, and correction cost is unbounded, then every child factor is
reachable from the Catalan baseline.  Such a theorem has erased the
recursion: it is equivalent to constructing a passing child from scratch.
A meaningful lift must protect occurrences, restrict the atlas, or bound the
switch cost.

## 6. Exact shadow representatives

A simple alternating owner path is written

\[
 \pi=(Q_0,R_1,Q_1,\ldots,R_\ell,Q_\ell),              \tag{6.1}
\]

and `E(pi)` denotes its `2ell` incidence arcs.

For a lower target

\[
 S\in\binom{\Omega^+}{r+1-q},\qquad q\in\{2,3\},
\]

let `W^-_(q,S)` be the finite family of allowed simple `q`-edge paths with

\[
                         \bigcap_{j=0}^qQ_j=S.         \tag{6.2}
\]

For every required upper depth `q` and target

\[
 U\in\binom{\Omega^+}{r+1+q},
\]

let `W^+_(q,U)` be the finite family of allowed simple **`q`-edge** paths
with

\[
                         \bigcup_{j=0}^q Q_j=U.        \tag{6.3}
\]

This fixed-depth family is the upper-tower semantics used in the passing
interface below.  There is also a strictly weaker unrestricted-interval
variant: let `W^+(U)` contain allowed **simple** paths of arbitrary length
whose owner union is `U`.  This family is finite.  Any unrestricted interval
witness with repeated traversal can be truncated to at most one simple
traversal of that factor component without changing the accumulated union.

### Theorem 6.1 (protected-shadow section plus flow)

There is a factor inside `A` covering every required lower `q=2,3` target
and every target at every required fixed upper depth if and only if one can
choose one witness

\[
 \sigma(q,-,S)\in\mathscr W^-_{q,S},\qquad
 \sigma(q,+,U)\in\mathscr W^+_{q,U}                  \tag{6.4}
\]

for every target so that the union

\[
 F_\sigma=\bigcup\{E(\sigma(t)):t\text{ required}\}   \tag{6.5}
\]

has degree at most two and satisfies (CF).

#### Proof

From a shadow-complete factor choose one actual occurrence of every target.
The union of their incidence arcs has degree at most two, and the remaining
factor incidences are a residual flow.  Conversely, Theorem 5.1 supplies a
factor containing `F_sigma`.  In a degree-two factor, selecting every edge
of a simple path forces it to be a literal consecutive component segment:
the two path edges consume both degrees at every internal owner.  Hence all
chosen shadows survive. \(\square\)

For fixed sign and depth, different target labels automatically use distinct
path occurrences, but witnesses at different depths may overlap and should
be allowed to do so.  Thus the outer object is a compatible representative
section/path-hypergraph cover, not an ordinary capacity matching.  Fixed
representatives reduce exactly to the TU flow of Theorem 5.1.

Equivalently introduce binary witness variables and impose

\[
 w_{T,\pi}\le x_e\quad(e\in E(\pi)),\qquad
 \sum_{\pi\in\mathscr W(T)}w_{T,\pi}\ge1.             \tag{6.6}
\]

The same proof gives the weaker unrestricted-interval variant after replacing
`W^+_(q,U)` by `W^+(U)`.  In that variant, (6.6) can instead be separated by
a finite accumulated-union reachability automaton.  Its states are `(Q,A)`
with `Q subseteq U` the current owner and `A subseteq U` the accumulated
union; acceptance is `A=U`.  For a fixed selected factor this is an ordinary
unit flow.  Sharing the factor variables across every target is the non-TU
master coupling.

## 7. Residence is a positive-run automaton, not an edge filter

On an oriented factor component write

\[
 Q_{i+1}=Q_i-\{\alpha_i\}+\{\beta_i\}.                \tag{7.1}
\]

Depth-`d` residence is exactly

\[
 \boxed{\beta_i\ne\alpha_{i+t}\quad(1\le t\le d)}.   \tag{7.2}
\]

Indeed `beta_i` is present until transition `i+t`; equality would create a
positive run of length `t<=d`.  Constant all-one components are allowed.

For one coordinate the exact cyclic DFA has states

\[
                 0,1_1,1_2,\ldots,1_d,1_\infty.       \tag{7.3}
\]

Reading a zero stays at `0`, except that `1_infty` may return to `0`.
Reading the first one enters `1_1`; successive ones advance through
`1_d` and then `1_infty`.  A return to zero from `1_j`, `j<=d`, is
forbidden.  The all-one cycle uses `1_infty` throughout.  It accepts exactly
the traces whose nonconstant positive runs have length at least `d+1`.

Equivalently, enumerate every minimal allowed-atlas factor path whose
coordinate trace is

\[
                         0\,1^\ell\,0,
 \qquad 1\le\ell\le d.                               \tag{7.4}
\]

If `E(B)` is its incidence set, residence is the finite family

\[
 \boxed{
 \sum_{e\in E(B)}x_e\le|E(B)|-1.}                    \tag{R}
\]

The endpoints may coincide when the bad run wraps a short factor component.

### Proposition 7.1 (cap-two flow does not imply residence)

Let `|Q|=r-3` and choose distinct `a,b,c`.  In the rank-`r-2`/rank-`r-1`
containment graph put

\[
 Z_a=Q\cup\{a\},\quad Z_b=Q\cup\{b\},\quad
 Z_c=Q\cup\{c\},                                     \tag{7.5}
\]

and

\[
 C_{ab}=Q\cup\{a,b\},\quad
 C_{ac}=Q\cup\{a,c\},\quad
 C_{bc}=Q\cup\{b,c\}.                               \tag{7.6}
\]

The six containments form a 2-regular `C6`, so every cap-two cut passes at
equality.  Contracting the `Z` shore gives the `A`-cycle

\[
 C_{ab},C_{bc},C_{ac}.                                \tag{7.7}
\]

Coordinate `a` has cyclic trace `1,0,1`, one positive run of length two.
Thus the component fails every depth `d>=2` residence test.

This is a literal Boolean/Johnson atom.  It is a no-existence obstruction
only when the displayed component is forced by the occurrence choices;
otherwise the pair-SDR may route around it.

Within the four-sector architecture, `K` affects only the all-`A` cycles on
`I`.  Once `kappa` is chosen, every `Z` joins its two selected occurrences;
contracting `Z` gives a 2-regular graph `H_kappa` on `I`.  For an old
coordinate `z`, label `i` by \(\mathbf1_{\{z\in C_i\}}\).  The `A`-sector residence
condition is exactly exclusion of the bracketed paths (7.4) in `H_kappa`.
The mixed-sector old-coordinate traces are determined by `I` and the parent
order.  Neither condition is an edge capacity.

## 8. One-core and Hall eliminate to one chronology-constrained SDR

Fix the **final** factor chronology, let `P=(P_i)` be its maximal depth-`d`
erosion on the disjoint union of cyclic components, and let `T_0` be the
family of low targets which must be placed literally.  Assume these targets
and the idle `P_i` are nonempty when a nonempty source word is required.

### Theorem 8.1 (core-elimination theorem)

The following are equivalent.

1. There is a one-core `C`,

   \[
   C_i\subseteq P_i,\qquad
   C_i\cup C_{i+1}=P_i\cup P_{i+1},                  \tag{8.1}
   \]

   and an injection `mu:T_0 -> positions` satisfying

   \[
                    C_{\mu(S)}\subseteq S\subseteq P_{\mu(S)}.
                                                                    \tag{8.2}
   \]

2. There is an injection `mu` with \(S\subseteq P_{\mu(S)}\) such that, after
   putting

   \[
   L_i=\begin{cases}
       S,&i=\mu(S),\\
       P_i,&i\text{ is unused},
       \end{cases}                                    \tag{8.3}
   \]

   one has

   \[
                 L_i\cup L_{i+1}=P_i\cup P_{i+1}      \tag{8.4}
   \]

   on every cyclic adjacency.

#### Proof

From (1), \(C\subseteq L\subseteq P\); applying adjacent union gives

\[
                 DP=DC\subseteq DL\subseteq DP,
\]

so (8.4) holds.  Conversely, take `C=L`.  At a used position
`C_i=S`, so (8.2) holds, and (8.4) is the one-core equation. \(\square\)

Thus variable-core Hall is not “take the union of all possible port graphs
and match.”  It is an SDR with nearest-neighbour OR constraints.

An exact binary formulation uses assignment variables `m_(S,i)`:

\[
 \sum_i m_{S,i}=1,\qquad
 \sum_Sm_{S,i}\le1,\qquad
 m_{S,i}=0\text{ unless }S\subseteq P_i,              \tag{8.5}
\]

and, for every coordinate `a in P_i union P_(i+1)`, requires that `a` occur
in at least one of the two endpoint labels selected by (8.3).  These are the
literal coordinate form of (8.4).

For a fixed one-core `C`, (8.2) reduces to ordinary bipartite Hall:

\[
 S\sim i\quad\Longleftrightarrow\quad
 C_i\subseteq S\subseteq P_i.                         \tag{8.6}
\]

The matching is TU only after `C` and the final chronology are fixed.

### Corollary 8.2 (independent-reserve positive case)

Restrict all assignments to a pairwise nonadjacent position set `R_0` and
put

\[
 M_i=(P_i\setminus P_{i-1})\cup(P_i\setminus P_{i+1}).\tag{8.7}
\]

Then a compiler supported on `R_0` exists if and only if the ordinary graph

\[
                 S\sim i\quad\Longleftrightarrow\quad
                 M_i\subseteq S\subseteq P_i          \tag{8.8}
\]

has a saturating matching.  No edge sees two replacements, so the OR
constraints decouple.  This is useful for a residual correction bank but
cannot place more than `|R_0|` targets.

### Proposition 8.3 (smallest joint port obstruction)

Let a coordinate `z` have envelope trace `1,1,1,1` on consecutive positions
`0,1,2,3` and be zero just outside.  The core equation forces

\[
 C_0(z)=C_3(z)=1,\qquad C_1(z)\vee C_2(z)=1.          \tag{8.9}
\]

Give two required targets unique admissible positions `1,2`, both omitting
`z` (other coordinates may be padded to keep every label nonempty).  Each
assignment alone extends to a core, and the static target-position graph has
its perfect matching.  Together they force `C_1(z)=C_2(z)=0`, contradicting
(8.9).  One forced zero is extendable; two adjacent forced zeros are the
first possible failure.

Finally, if residence makes every `P_i` have rank `h=R-d` and `T_0` contains
all nonempty targets of rank at most `h`, a saturating port SDR already
forces complete lower depth `d`: every rank-`h` target `S` is matched under
\(S\subseteq P_i\), and equal ranks give `S=P_i`.  At the depth-three
`k=11 -> 13` interface, final port success therefore implies lower `q=3`;
lower `q=2` remains a separate shadow condition.

## 9. The exact passing-correction theorem

### Theorem 9.1 (finite correction-interface equivalence)

Fix a parent factor, an integer depth `d>=1`, the literal four-sector
construction, a
universal allowed physical correction atlas `A`, the requested lower
`q=2,3` targets, every target at every requested fixed upper depth, and the
low compiler target family `T_0`.

Here “the Catalan-leave architecture corrects inside `A`” means that the
certificate includes an activated four-sector baseline
\(X^0(\kappa)\subseteq\mathcal A\) and a final factor reachable from it by
allowed alternating
switches.  The baseline itself need not be resident; residence is imposed on
the final factor.  Under this definition, the architecture corrects to a
child satisfying the listed interface if and only if there exist,
simultaneously:

**F0. Activated Catalan pair-SDR.**  Representatives `kappa(V)` satisfying
Theorem 2.1.  These data produce the literal four-sector baseline `X^0`, and
one requires \(X^0(\kappa)\subseteq\mathcal A\).  In the stricter subclass
where the **initial baseline** must already be new-label resident, add the
leave vertex-cover equation (4.2); equation (4.1) is already part of the
occurrence transversal.

**F1. Protected shadow section.**  One fixed-depth path from every family in
Section 6, with forced union `F_sigma` of degree at most two.

**F2. Integral correction flow.**  A residual solution of (CF) in `A`.
Together with `F_sigma` it gives the final incidence factor `X`; if a switch
budget is imposed, use the integral min-cost version relative to `X^0`.

**F3. Final residence.**  The completed factor satisfies every positive-run
clause (R), on all coordinates and all final components.  If later
same-dimensional cuts and joins are used, the clauses are evaluated after
those joins.

**F4. Final compiler SDR.**  On the maximal erosion `P_d(X)`, an injection
`mu` satisfies (8.3)--(8.4).

If a strict quotient or one physical Hamilton cycle is required, add the
exact phase, component-splice and voltage conditions to `F2`; those are
orthogonal to the physical coverage theorem.

#### Proof

Necessity is extraction from the complete correction certificate.  Its
chosen activated baseline supplies the upper-occurrence and `K`-port data in
`F0`; these need not be recoverable from the final child.  The final child
supplies one actual occurrence of every shadow target, the remaining factor
incidences, its accepted coordinate traces, and its actual one-core matching.
Theorems 2.1, 5.1, 6.1 and 8.1 give `F0`--`F4`.

Conversely, `F0` invokes the explicit four-sector theorem and supplies a
legal lower-rainbow baseline.  `F1`--`F2` and Theorem 6.1 supply a legal
factor with every requested shadow.  `F3` is exactly the residence condition.
`F4` and Theorem 8.1 supply a one-core and a saturating compiler assignment,
so the graded source word exists.  All claims refer to the same final factor
and chronology. \(\square\)

The theorem is finite but not polynomially small in its raw form: fixed-depth
path families and Hall cuts may be exponentially many.  The fixed-depth
families have finite layered-path separation, while the weaker unrestricted
upper variant has accumulated-union reachability separation; the residual
cuts have max-flow separation.  Finiteness and exact separation, not
compactness, are the theorem here.

The algebraic classification is now exact:

\[
\begin{array}{c|c}
\text{layer}&\text{exact mathematical type}\\ \hline
I\text{ only}&\text{partition representative choice}\\
K\text{ for fixed }I&\text{cap-two network flow}\\
(I,K)\text{ jointly}&\text{colored pair-SDR / 3-uniform exact matching}\\
\text{fixed shadow representatives}&\text{residual TU flow}\\
\text{representative choice}&\text{path-hypergraph section}\\
\text{residence}&\text{shared positive-run DFA clauses}\\
\text{fixed core ports}&\text{ordinary Hall matching}\\
\text{variable core ports}&\text{nearest-neighbour constrained SDR}.
\end{array}                                           \tag{9.1}
\]

Separate feasibility of the rows of (9.1) does not compose, because they
share the same occurrence, incidence and chronology variables.

## 10. The smallest literal shadow-collision switch

The Boolean incidence graph between consecutive ranks has no `C4`: two
distinct rank-`h-1` sets lie in at most one common rank-`h` set.  Therefore
an alternating `C6` is the smallest nontrivial degree-preserving switch atom.

Assume `h>=5` in the physical middle-level universe of size `2h-1`.  Let
`|R|=h-2`, choose distinct `a,b,c,e,d_a,d_b` outside `R`, and choose
`r_0 in R`.  Put

\[
 P_a=R\cup\{a\},\quad P_b=R\cup\{b\},\quad
 P_c=R\cup\{c\},                                     \tag{10.1}
\]

and

\[
 V_{ab}=R\cup\{a,b\},\quad
 V_{bc}=R\cup\{b,c\},\quad
 V_{ca}=R\cup\{c,a\}.                               \tag{10.2}
\]

These six vertices form the incidence `C6`.  Give every `P_t` one fixed
other endpoint

\[
 Q_a=R\cup\{a,d_a\},\qquad
 Q_b=R\cup\{b,d_b\},\qquad
 Q_c=R\cup\{c,e\},                                  \tag{10.3}
\]

and give every `V` and `Q` one fixed external incidence.  Conditional on
one common **full incidence-factor completion** containing all the displayed
fixed incidences, toggling the two alternating matchings of
(10.1)--(10.2) preserves every row and owner degree and hence is a literal
exact-factor switch.  This paragraph does not assert that an arbitrary
surrounding atlas supplies that full completion.

Take the fixed predecessor

\[
 A=(R\setminus\{r_0\})\cup\{a,b,e\}.                 \tag{10.4}
\]

At `V_ab`, the two shores continue to `Q_a` or `Q_b`.  Their exact depth-two
outputs are

\[
\begin{array}{c|cc}
 &a\text{-shore}&b\text{-shore}\\ \hline
L_2&(R\setminus\{r_0\})\cup\{a\}&
    (R\setminus\{r_0\})\cup\{b\}\\
U_2&R\cup\{a,b,e,d_a\}&R\cup\{a,b,e,d_b\}.
\end{array}                                           \tag{10.5}
\]

Choose another `r_1 in R` and prepend

\[
 B=(R\setminus\{r_0,r_1\})\cup\{a,b,e,c\}.           \tag{10.6}
\]

Then the depth-three outputs are

\[
\begin{array}{c|cc}
 &a\text{-shore}&b\text{-shore}\\ \hline
L_3&(R\setminus\{r_0,r_1\})\cup\{a\}&
    (R\setminus\{r_0,r_1\})\cup\{b\}\\
U_3&R\cup\{a,b,c,e,d_a\}&R\cup\{a,b,c,e,d_b\}.
\end{array}                                           \tag{10.7}
\]

All consecutive owners have rank `h`; the displayed lower ranks are
`h-2,h-3` and upper ranks `h+2,h+3`, exactly as required.

Consequently, within any such common completion, if the only remaining lower
witness is on the `a`-shore and the only remaining upper witness is on the
`b`-shore, each marginal shadow ledger has a legal exact-factor switch but
the common correction does not.  The same polarity holds simultaneously at
`q=2` and `q=3`.

Every coordinate trace inside either four-owner word `B,A,V_ab,Q_t` is
monotone.  Thus the atom creates no internally bracketed short positive run;
residence compatibility depends only on its external collars.  The atom is
still local: witness uniqueness, global residence, and one-core completion
are additional hypotheses.  It is not a counterexample to the Catalan
recursion.  It proves that marginal lower and upper witness flows cannot be
combined after forgetting their common shore bit.

## 11. Seam charges after the correction

The forced sector-interface ledger of Proposition 4.2 is intrinsic to the
Catalan lift.  A later same-dimensional segment correction has an additional,
separate budget.

If `R_s` old factor edges are cut and `R_s` new joins are made, then at every
fixed depth `q` and on each tower:

\[
 \begin{aligned}
 \#\text{old windows removed}&\le qR_s,\\
 \#\text{new windows created}&\le qR_s,\\
 \|\lambda'_q-\lambda_q\|_1&\le2qR_s.
 \end{aligned}                                        \tag{11.1}
\]

If the old support was complete, at most `qR_s` holes can be created.  Every
new depth-`d` residence defect meets a join: at most `dR_s` depth-`d` windows
and `2dR_s` positions require checking.  Direct transported-envelope
one-core gluing promotes at most `2R_s` columns; recomputing maximal erosion
and adding the two outer guards promotes at most `(d+2)R_s`.

These charges must be added to, not substituted for, the `h_t(J)` sector
ledger.  Conditions `F1`--`F4` are imposed on the final post-join chronology.

## 12. Audited `k=11 -> 13` boundary and implication scope

The audited raw boundary proves that the requested child interface exists by
an independently constructed `k=13` carrier.  It does not provide the
pair-SDR or the common protected representative section required here.

The exact discrepancies between the audited raw `k=13` child and the natural
inheritance map remain:

\[
 \begin{array}{c|c}
 \text{audit}&\text{value}\\ \hline
\text{all-leaf child rows needing a mark change}&115/132\\
\text{minimum individual natural mark replacements}&133\\
\text{ECO-projected moved endpoints in the raw child}&225\\
\text{canonical singleton port degree}&6\to1.
 \end{array}                                          \tag{12.1}
\]

These values show that the **audited raw child** is globally reselected and
that those literal natural-inheritance classes fail.  They do not show that
every possible successful child must move as much.  They neither prove nor
refute the actual Catalan pair-SDR, residence-safe flow, or
chronology-constrained port system.

There are two useful logical dependencies.

1. For fixed protected witnesses, (CF) is the complete algebraic degree
   theorem; no additional integrality obstruction remains.
2. At depth three, a final saturating graded port SDR already forces complete
   lower `q=3`.  The lower `q=2` and every upper support condition remain
   independent.

The theorem guarantees exactly the listed lower `q=2,3` interface.  If the
definition of a passing carrier requires additional lower depths, their
fixed-depth path families must also be inserted into `F1`; Theorem 6.1 and
the proof of Theorem 9.1 then apply verbatim.  Residence and every upper
depth are always evaluated on the final child after all cuts and joins.

No coefficient-one or all-odd conclusion follows from this report.

## 13. Exact remaining theorem

The sole positive existence target in this architecture is now:

> **Catalan simultaneous correction lemma.**  For every passing parent,
> exploit its actual Catalan/Johnson occurrence geometry to choose a
> pair-SDR `kappa` (and, in the initially resident-baseline subclass, whose
> occurrence positions cover the looped distance graph `G_d`), and choose one
> common all-shadow representative section such that
> the residual defects (5.5) all vanish, an integral completion avoids every
> residence clause (R), and its final maximal erosion admits the constrained
> port SDR (8.3)--(8.4), with the intended admissible correction-cost and
> voltage bounds.

Biregularity and ordinary expansion cannot prove this statement: Theorem 3.1
is the minimal abstract obstruction, Proposition 2.3 is the first literal
fixed-transversal flow defect, Proposition 7.1 is the first forced
chronology defect, Section 10 is the smallest literal shadow-polarity switch
atom conditional on a common full factor completion, and Proposition 8.3 is
the smallest joint port defect.

Conversely, the simultaneous lemma and Theorem 9.1 give the desired passing
`k+2` carrier.  This is the precise proved/conditional boundary.

## 14. Sources and proof-audit scope

This report builds on

```text
THREAD_K_SEMILENGTH_RAISING_CATALAN_LEAVE_LIFT_AND_ECO_OBSTRUCTION_20260729.md
MATH_THEOREM_EQUIVARIANT_GRADED_COMPILER_QUOTIENT_HALL_20260729.md
THREAD_D_EXACT_Q1_CYCLE_COVER_SPLICE_AND_UNRESTRICTED_SHADOW_CUTS_20260729.md
MATH_CODE_AUDIT_AD_SHADOW_TOKEN_AND_FLOW_COMPRESSION_20260729.md
```

Three independent mathematical lanes audited the residual cut, pair-SDR,
positive-run, shadow-path, and core-elimination formulations.  No finite
carrier fitting was used.  The literal `C6` polarity formulas were checked
independently at both `q=2` and `q=3`; their global scope caveats are retained
in Section 10.
