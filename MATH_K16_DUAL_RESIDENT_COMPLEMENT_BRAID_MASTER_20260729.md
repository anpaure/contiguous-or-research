# Exact complement-rail master for the `15 -> 16` lift

Date: 2026-07-29

Status: conditional reduction and exact q1 formulation.  It assumes the
input factor stated in Section 1.  No such bi-resident input factor and no
`k=16` word are claimed here.

## 1. Input and the two Pascal rails

Put

\[
 X=[15],\qquad z=16,\qquad V_8={X\choose8},\qquad W=|V_8|=6435.
\]

Let `F` be a spanning 2-factor of `J(15,8)`.  For an edge
`e={P,Q}` write

\[
 \lambda(e)=P\cap Q\in{X\choose7},\qquad
 \upsilon(e)=P\cup Q\in{X\choose9}.
\tag{1.1}
\]

The conditional input needed below is:

1. `lambda:E(F)->binom(X,7)` is a bijection;
2. every member of `binom(X,9)` occurs among the `upsilon(e)`;
3. on every component, every cyclic one-run and every cyclic zero-run of
   every old coordinate has length at least four.

Condition 2 is equivalently q1 completeness of the lower palette of the
complementary rank-seven factor.  Condition 3 is bi-residence at depth
three.  Q1 completeness alone says nothing about the deeper upper targets;
that gate remains explicit below.

The child middle layer splits into two rails

\[
 A_P=P\quad(P\in V_8),\qquad
 B_R=\{z\}\cup R\quad(R\in{X\choose7}).
\tag{1.2}
\]

The A rail is `F`.  Complementing the vertices of `F` gives the B rail:
the copy of `P` on that rail is `B_(bar P)`.  A cross edge is possible
exactly when

\[
 A_P\sim B_R\quad\Longleftrightarrow\quad R\subset P.
\tag{1.3}
\]

Thus the rung graph is the ordinary incidence graph between ranks seven
and eight.  It is 8-regular on both shores and has exactly

\[
 8W=51480
\tag{1.4}
\]

rungs.  The two rails contain all `2W=12870` child middle vertices exactly
once.

## 2. The complete edge-colour table

For `e={P,Q}` in `F`, let its complementary B edge have endpoints
`R=bar P,S=bar Q`.  Every possible retained edge has the following q1
colours:

\[
\begin{array}{c|c|c}
\text{edge}&\text{intersection}&\text{union}\\ \hline
A_PA_Q&\lambda(e)&\upsilon(e)\\
B_RB_S&\{z\}\cup\overline{\upsilon(e)}
       &\{z\}\cup\overline{\lambda(e)}\\
A_PB_R\ (R\subset P)&R&\{z\}\cup P.
\end{array}
\tag{2.1}
\]

This table is an identity, not a heuristic.  It shows why the rungs are the
right repair objects:

* a rung incident with `B_R` repairs precisely the tight old lower colour
  `R`;
* a rung incident with `A_P` repairs precisely the tight upper colour
  `{z}+P`.

The other two palettes, old upper rank nine and `z`-lower rank seven, have
the duplicate capacity `W-C(15,9)=1430`.

## 3. Exact cut and rung accounting

For each factor edge `e`, let `c^A_e,c^B_e` say that its A or B copy is
cut.  Let `y_(P,R)` select the rung `A_PB_R`, and let `h^A_P,h^B_R` mark the
two global endpoints.  Define

\[
 a=\sum_e c^A_e,\qquad b=\sum_e c^B_e.
\]

At every vertex, Hamilton-path degree is equivalent to

\[
\begin{aligned}
 \sum_{R\subset P}y_{P,R}
   &=\sum_{e\ni P}c^A_e-h^A_P,\\
 \sum_{P\supset R}y_{P,R}
   &=\sum_{e\ni\bar R}c^B_e-h^B_R,
\end{aligned}
\tag{3.1}
\]

with

\[
 \sum_Ph^A_P+\sum_Rh^B_R=2.
\tag{3.2}
\]

Summing (3.1) on both shores gives the exact identities

\[
 |Y|=a+b-1,qquad |a-b|\le1.
\tag{3.3}
\]

If `F` has `c` physical components, connectivity also forces

\[
 a\ge c,\qquad b\ge c.
\tag{3.4}
\]

Conversely, (3.1)--(3.2), one cut in every old rail cycle, and connectedness
of the selected graph give one Hamilton path.  No ordering variables are
needed: after the degree equations the only possible connected object is a
spanning path.

### 3.1 Minimum cost of a marked four-state B run

An internal z-run is exactly a B segment.  If no old B component has length
four, producing a four-state B segment needs two B cuts in one component,
so `b>=c+1`.  Equations (3.3)--(3.4) then give the sharp scalar minimum

\[
 (a,b,|Y|)=(c,c+1,2c).
\tag{3.5}
\]

The marked segment must have two rungs, rather than be a global end, if one
wants an internal run.  If `c=1`, (3.5) puts both B ends at the global
ends, so an internal marked segment instead needs at least `(a,b)=(2,2)`.
If a four-cycle is already a component, a single cut opens it as a
four-state segment and `(a,b)=(c,c)` is arithmetically possible.

For an internal B segment flanked by legal rungs, four states are in fact
enough to make `{z}` an exact individually realizable compiler cell.  The
local proof is in Section 6.2.  Simultaneous feasibility with every other
lower target remains the full `COMP_3` gate.

## 4. Q1 is a linear system

For a rank-nine set `U`, write

\[
 E_U=\{e\in E(F):\upsilon(e)=U\}.
\]

The complete four-palette q1 condition is exactly

\[
\begin{aligned}
 c^A_e&\le \sum_{P\supset\lambda(e)}y_{P,\lambda(e)}
                 &&(e\in E(F)),\\
 c^B_e&\le \sum_{R\subset\overline{\lambda(e)}}
                     y_{\overline{\lambda(e)},R}
                 &&(e\in E(F)),\\
 \sum_{e\in E_U}(1-c^A_e)&\ge1
                 &&(U\in{X\choose9}),\\
 \sum_{e\in E_U}(1-c^B_e)&\ge1
                 &&(U\in{X\choose9}).
\end{aligned}
\tag{4.1}

The first row says that cutting the unique AA occurrence of
`lambda(e)` exposes and uses a rung at `B_(lambda(e))`.  The second says
that cutting the unique BB occurrence of `{z}+bar(lambda(e))` exposes and
uses a rung at `A_(bar(lambda(e)))`.  The last two rows preserve the two
slack palettes.  Formula (2.1) proves both necessity and sufficiency.

Summing the last two per-colour capacities gives the sharp scalar
consequences

\[
 a\le1430,\qquad b\le1430
\tag{4.2}
\]

for exact q1.  If at most two z-containing lower colours are delegated to
the compiler, only the second bound relaxes, to `b<=1432`; the A bound is an
upper-rank condition and remains 1,430.  The per-colour rows in (4.1) are
strictly stronger than these scalar consequences.

If the compiler is permitted at most two missing **lower** q1 colours,
introduce slacks only in the first and fourth rows and require their sum to
be at most two.  The second and third rows are upper-rank conditions and
must remain exact unless a separate longer-interval witness is exhibited.
This distinction prevents a lower compiler allowance from being spent on
an upper hole.

An equivalent cut-only exposure form follows from (3.1):

\[
 c^A_e\le \deg_{C_B}(\lambda(e))-h^B_{\lambda(e)},
 \qquad
 c^B_e\le \deg_{C_A}(\overline{\lambda(e)})
                         -h^A_{\overline{\lambda(e)}},
\tag{4.3}

before the actual incidence-rung b-matching is chosen.

## 5. A sound sparse Hamilton master

The exact q1/topology master uses the following Boolean variables:

\[
 2W\text{ rail cuts}
 +8W\text{ rungs}
 +2W\text{ endpoint flags}
 =77220
\tag{5.1}

before optional witness variables.  Add (3.1)--(3.2), (4.1), and one marked
four-state B segment.  Connectedness is imposed fail-closed by adjoining a
dummy vertex to the two endpoint flags.  The selected graph is then
2-regular.  Whenever it has more than one cycle, add the ordinary subtour
row

\[
 \sum_{e\in\delta(S)}x_e\ge2
\tag{5.2}

for a component `S` not containing the dummy.  Iteration terminates with
one dummy cycle, equivalently one physical Hamilton path.

For a four-consecutive-vertex B interval, a mark variable implies:

* the two boundary B edges are cut;
* its three internal B edges are retained;
* both endpoint dummy flags are zero; and
* both endpoint rung degrees are one.

At least one mark is required.  There are only `W` possible marks.

This is a sparse SAT/0-1-flow model: 51,480 is the dominant static edge
count, rather than a quadratic graph on 12,870 owners.

For fixed cuts and endpoint flags, the rung layer is exactly a bipartite
`b`-matching and needs no integer-programming relaxation theorem.  Give
`A_P` demand

\[
 d_A(P)=\deg_{C_A}(P)-h^A_P
\]

and `B_R` demand `d_B(R)=deg_(C_B)(R)-h^B_R`.  In the network

```text
source -> A_P -> B_R -> sink,       R subset P,
```

use endpoint capacities `d_A,d_B` and unit incidence arcs.  An integral
maximum flow of value `a+b-1` is equivalent to (3.1).  Thus cut feasibility
plus q1 is a 0-1 cut master followed by an ordinary integral flow.  The
subtour rows (5.2) are the only global topological addition; without them a
perfect port flow may close several macro cycles.

Equivalently, after equality of the two total demands, the exact port Hall
system is

\[
 \sum_{P\in S}d_A(P)
 \le
 \sum_{R\in N(S)}d_B(R)
 \qquad(S\subseteq V_8),
\tag{5.3}
\]

where `N(S)` is taken in the rank-seven/rank-eight incidence graph.  A
failed flow therefore returns a literal deficient cut, not a heuristic
spectral diagnosis.

### 5.1 Exact residence by lazy motif rows

Decode the unique path.  If coordinate `x` has an internal positive run of
length `ell<=3`, let `M` be the `ell+1` selected path edges from the state
immediately before the run through the state immediately after it.  Add

\[
 \sum_{e\in M}x_e\le |M|-1.
\tag{5.4}

This row is sound because any Hamilton path retaining all of `M` retains
the same forbidden run, in either orientation.  Repeating (5.4) is an exact
residence CEGAR.  Bi-residence of the input implies that every initial
violation row contains at least one rung; no untouched rail interior can
be rejected.

A pairwise terminal-run compatibility table is a useful sufficient
prefilter, but it is not exact when a coordinate is constant across three
or more consecutive fragments.  The motif row (5.4), or an equivalent
four-state automaton on the macro path, avoids that hidden gap.

## 6. Upper coverage and the exact compiler interface

Q1 completeness does not imply arbitrary-width upper completeness.  Two
additional exact gates remain.

### 6.1 Protected native witnesses

If the input factor comes with a catalogue of native all-depth witnesses,
introduce a variable `w_(S,I)` for an A- or B-rail interval `I` whose union
is the child upper target `S`, and impose

\[
 w_{S,I}\le1-c_e\quad(e\text{ internal to }I),
 \qquad
 \sum_Iw_{S,I}\ge1.
\tag{6.1}

For A intervals these are upper shadows of `F`; for B intervals they are
complements of lower shadows of `F`, with `z` adjoined.  At depths one
through seven there are exactly

\[
 2\cdot7W=90090
\]

cyclic native occurrences before identical witnesses are merged.  They
cover 9,949 no-z targets and 16,383 z-targets; the full 16-set is the union
of the whole final path automatically.  Formula (6.1) is therefore a sound
sparse monotone protection theorem for an all-depth input factor.  Cross-created witnesses may be
accepted by the final literal audit, but they are not silently counted in
(6.1).

Without such an all-depth catalogue, arbitrary-width upper coverage must be
audited on the decoded path.  A missing target is not repaired merely by
passing (4.1).

### 6.2 Direct `COMP_3`

For the decoded chronology `T_0,...,T_(2W-1)`, run the unrestricted direct
compiler

```text
scratch/threadD_comp3_postprocessor_20260729.py
```

with maximal envelopes

\[
 P_p=\bigcap_{\max(0,p-3)\le i\le\min(2W-1,p)}T_i.
\]

The marked B run has a unique erosion position `p`.  The exact
candidate-cell test is

\[
 \{z\}\subseteq P_p,
 \qquad M_{\{p\}}\subseteq\{z\},
\tag{6.2}

and the common compiler remains feasible with `A_p={z}`.

The coordinate fact used here is elementary and exact at every depth.  If a
positive middle run is `[a,b]`, its legal source positions are the erosion
interval `[a+d,b]`.  A source position in this interval is the sole possible
carrier of some middle incidence if and only if it is one of the two
endpoints.  The left endpoint is forced by middle position `a`, the right by
position `b`; at an interior source position, any incidence using it can use
the preceding or following erosion position as well.

For the marked internal segment in Section 5, (6.2) is automatic.  Write
the relevant middle collar as

\[
 A_L,B_{R_0},B_{R_1},B_{R_2},B_{R_3},A_R.
\tag{6.3}
\]

The legal rungs give `R_0 subset A_L` and `R_3 subset A_R`.  Hence every
old coordinate in the four-state core

\[
 C=R_0\cap R_1\cap R_2\cap R_3
\]

also occurs in both flanking A states.  In the depth-three erosion, a source
position is mandatory for an old coordinate exactly when it is the first or
last erosion position of that coordinate's positive run.  The two flanking
occurrences show that the unique z position is neither.  Thus
`M_{\{p\}} subseteq {z}`.  Setting `A_p={z}` and every other source letter
to its maximal envelope is a valid base antecedent.  This proves:

> **Four-ear lemma.**  Every internal four-vertex B segment flanked by legal
> incidence rungs supplies an individually legal singleton source letter
> `{z}`.

The lemma settles the singleton channel, but not simultaneous coverage of
all 26,332 lower targets; that is why unrestricted `COMP_3` remains.

The complete fail-closed pipeline is therefore:

1. solve (3.1)--(5.2) and the q1 rows;
2. add residence rows (5.4) until clean;
3. check arbitrary-width upper coverage, or enforce (6.1);
4. invoke exact `COMP_3`, pinning one valid singleton cell;
5. exhaustively replay all `65535` nonempty masks.

Only step 5 is an exact `k=16` certificate.  A q1-feasible braid, a marked
four-state B segment, or a compiler-feasible chronology in isolation is not
one.

## 7. Square-switch specialization

The colour-aware square in
`MATH_K16_DUAL_RAIL_SQUARE_SWITCH_REDUCTION_20260729.md` is the special
case that cuts one AA and one BB edge and uses two rungs which automatically
repair their tight colours.  If `F` has `c` components on each rail, merging
the initial `2c` cycles into one child cycle takes at least `2c-1` such
component-reducing squares.  Cutting one final selected edge opens the
cycle.

This square model is smaller and palette-safe by construction, but it is a
strict subclass of (3.1)--(5.2).  In particular, a negative square-packet
search is not a negative theorem for the general segmented braid.

There is an exact way to see its component limitation.  Since `lambda` is
a bijection, put

\[
 \phi(e)=\overline{\lambda(e)}\in V_8.
\]

For an oriented AA incidence `(e,X)` with `X` an endpoint of `e`, the only
possible colour-aware BB edge is

\[
 f=\lambda^{-1}(\bar X).
\tag{7.1}
\]

The square exists if and only if `phi(e)` is an endpoint of `f`.  It then
joins the A component of `e` to the B copy of the F component of `f`.
Thus the complete component-pair graph is computed without enumerating any
rungs.

For the centered complementary PBBS factor, the corrected undirected
catalogue has 12,870 such squares: every A edge has the two B partners
through its two endpoint roles.  Every square is diagonal at component
level: `e` and `f` belong to the same one of the 73 physical PBBS
components.  The fixed square catalogue can therefore merge the initial
146 rails only to 73 paired components.
This is a scoped obstruction to the centered-PBBS square-only model, not to
the general incidence-rung master.  It also identifies the required repair:
rethread the factor so that (7.1) has a connected component-pair graph, or
use non-square rungs.

The general centered-factor proof, the correction from 6,435 to 12,870,
and the unrelated-factor component census are in
`MATH_ATTACK_R_K16_DUAL_RAIL_SQUARE_DIAGONAL_AND_EQUIVARIANT_CT_20260729.md`.

## 8. Exact scope

The reduction proves:

* the two-rail and q1 identities;
* the sharp cut/rung count and minimum four-run arithmetic;
* a 77,220-variable sparse Hamilton master;
* exact lazy residence rows; and
* a sound upper/compiler handoff.

It does not prove existence of the assumed dual-resident factor, feasibility
of the braid master, arbitrary-width upper completeness, or `COMP_3`.
Those are genuinely separate finite gates.
