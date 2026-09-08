# Hinge rectangles: integral coloured rotor flow and rooted Euler fusion

Date: 2026-08-02  
Status: unconditional literal rectangle theorem, exact integral-flow
rounding on that face, and exact label-preserving fusion/sidecar criteria.
The existence of a canonical triangular chain table satisfying the displayed
hinge-flow and topology hypotheses remains open.

## 0. Outcome

The corrected pull clock proves a rational stationary trace circulation with
the optimal residual rank marginals.  It does not itself choose one trace per
owner or one occurrence of every named residual target.  Generic rounding is
false: the owner/state matrix has determinant-two minors, literal Boolean
parity examples exist, and the marked-age semigroup is not normal.

There is nevertheless a substantial exact integral face.  First choose an
exact table

\[
       \mathcal F=\{(T,C_T):T\in\tbinom{[k]}r\},          \tag{0.1}
\]

where the `C_T` are pairwise disjoint strict chains of named lower targets,
each has length at most `d`, every member of `C_T` is a proper subset of
`T`, and the chains partition the required residual target bank.

For every owner-chain `(T,C_T)`, this note constructs a literal Cartesian
tail/head rectangle of depth-`d` trace arcs.  Every arc in that rectangle has
owner `T` and marks exactly the same named chain `C_T`.  Consequently:

* if the root-conditioned fractional state-balance equations are feasible
  inside these rectangles, network total unimodularity selects one trace per
  owner **integrally** while covering every target in (0.1) exactly once;
* on any fixed-head flag table, balance is exactly capacitated Hall, and
  connected balance is exactly a distinct-role spanning-tree skeleton whose
  deletion leaves the residual Hall demands feasible;
* mutually admissible crossed-head switches merge Euler components while
  preserving every owner and every declared lower-target label; and
* if switching stops at a bounded list of components, the exact de Bruijn
  overlap distance gives the necessary sidecar budget.

Thus the owner/target integer rounding is automatic on the hinge face.  The
minimal remaining canonical lemma is to choose `(0.1)` and its hinges so
that one root-conditioned fractional hinge flow exists and its component
exchange graph is spanning, or has universal `O(1)` reset cost.

The rectangle is transparent only for the declared lower chain and owner.
Its free endpoint letters can change unmarked suffixes, exterior upper
windows, residence, guard data, or compiler cells.  Those must be added as
explicit restrictions before applying the theorem downstream.

## 1. Trace and chain notation

A depth-`d` trace is a word of nonempty letters

\[
                         e=(B_0,B_1,\ldots,B_d).          \tag{1.1}
\]

It is the de Bruijn arc

\[
 (B_0,\ldots,B_{d-1})\longrightarrow(B_1,\ldots,B_d).   \tag{1.2}
\]

Its owner is `union_(i=0)^d B_i`.  Let

\[
 C=(S_1\subsetneq\cdots\subsetneq S_\ell),\qquad
 0\le\ell\le d,\qquad S_\ell\subsetneq T               \tag{1.3}
\]

be a chain to be marked by proper suffix unions.  For `ell=0`, (1.3) is
empty.

## 2. The literal hinge rectangle

### Theorem 2.1 (payload-transparent owner-chain rectangle)

For every `(T,C)` in (1.3), the trace menu `Tr_d(T,C)` contains a Cartesian
rectangle

\[
                         \mathcal A_{T,C}\times
                         \mathcal H_{T,C}.               \tag{2.1}
\]

Every pair in (2.1) is a literal trace with owner `T` and the same declared
marked payload `C`.

If `1<=ell<=d-1`, the rectangle can be chosen with

\[
 |\mathcal A_{T,C}|=2^{|S_\ell|},\qquad
 |\mathcal H_{T,C}|=2^{|S_1|}-1.                         \tag{2.2}
\]

If `ell=d`, it has

\[
 |\mathcal A_{T,C}|=2^{|S_d|},\qquad
 |\mathcal H_{T,C}|=1.                                  \tag{2.3}
\]

The empty-chain case also has a nonempty rectangle.

#### Proof

Assume first `1<=ell<=d-1`, put `S_0=emptyset`, and choose `x in S_1`.
For arbitrary

\[
                         A\subseteq S_\ell,\qquad
                         \varnothing\ne B\subseteq S_1,  \tag{2.4}
\]

set

\[
 B_0=(T\setminus S_\ell)\cup A,\qquad B_d=B.             \tag{2.5}
\]

The fixed middle spine `M=(B_1,...,B_(d-1))` is

\[
\begin{aligned}
 B_i&=\{x\} &&(1\le i\le d-\ell-1),\\
 B_{d-j}&=S_j\setminus S_{j-1} &&(2\le j\le\ell),\\
 B_{d-1}&=S_1.
\end{aligned}                                             \tag{2.6}
\]

The index ranges in (2.6) are disjoint and cover the middle positions.
Every letter is nonempty.  For `1<=j<=ell`, the suffix

\[
                         B_{d-j},\ldots,B_d               \tag{2.7}
\]

has union `S_j`; the variable last letter is contained in `S_1`.  The union
of the fixed middle and last letter is `S_ell`, while (2.5) supplies its
nonempty complement in `T`.  Hence the full union is `T`.

The tail state is `(B_0,M)` and depends only on `A`; the head state is
`(M,B)` and depends only on `B`.  Every cross-pair has the same literal word
form and the same proof above.  This gives (2.1)--(2.2).

For `ell=d`, set

\[
 B_{d-j+1}=S_j\setminus S_{j-1}\quad(1\le j\le d),
 \qquad B_0=(T\setminus S_d)\cup A,\quad A\subseteq S_d. \tag{2.8}
\]

Now the suffix of length `j` is `S_j`; the head is fixed and the tail has
the `2^{|S_d|}` choices in (2.3).

If `ell=0`, choose `x in T`, put `B_0=T`, set every middle letter to
`{x}`, and allow `B_d` to be any nonempty subset of `T`.  There is no marked
payload to change. \(\square\)

### Scope warning

For `ell<=d-1`, changing `B_d` changes the unmarked length-one suffix, and
changing `B_0` can change exterior prefix/crossing data.  The theorem says
that the owner and the declared marked chain are transparent.  It does not
silently include upper, residence, pin, guard, or compiler payloads.

## 3. Root-conditioned integral coloured flow

Let `P` be a fixed rooted trace path using distinct owners and distinct
declared target occurrences.  Remove those resources from (0.1), and let

\[
                         \eta=\partial P                  \tag{3.1}
\]

be its integral state boundary.  For every remaining owner `T`, choose one
hinge rectangle `E_T=\mathcal A_T\times\mathcal H_T` from Theorem 2.1,
possibly restricted to a smaller nonempty subrectangle after imposing
literal guards.

### Theorem 3.1 (hinge-flow integrality)

Suppose there are rational nonnegative arc weights `x_e` supported on the
hinge rectangles such that

\[
 \sum_{e\in E_T}x_e=1\quad(T\text{ free}),\qquad
 \partial x=-\eta.                                      \tag{3.2}
\]

Then there is an integral selector `z` satisfying (3.2).  It chooses exactly
one trace for every free owner and, together with `P`, uses every declared
residual named lower target exactly once.

#### Proof

For each free owner introduce nodes `T^-`,`T^+` and one fixed-unit arc
`T^- -> T^+` whose lower and upper capacities are both one.  For each tail
`u in \mathcal A_T` add `u -> T^-`; for each
head `v in \mathcal H_T` add `T^+ -> v`.  Impose the state boundary `-eta`
and flow conservation at the owner nodes.  The tail and head marginals of
the rational vector in (3.2) give a feasible network flow.  Node-arc
incidence is totally unimodular and all capacities and supplies are
integral, so an integral flow exists.

One unit crosses every owner arc and therefore chooses one tail and one
head.  Cartesianity makes their pair a literal trace in `E_T`.  Theorem 2.1
makes the marked payload constant over `E_T`, so the chain partition (0.1)
proves exact named-target use. \(\square\)

The theorem does not follow from the original pull-clock circulation unless
that fractional circulation, or an integrally traded replacement, is shown
to lie in the rectangles of one exact table (0.1).

### Corollary 3.2 (saturated-chain predecessor normal form)

Suppose every chain in (0.1) has length exactly `d`, and first take the
zero-boundary face `P=emptyset`.  Write its difference
blocks as

\[
 D_{T,j}=S_{T,j}\setminus S_{T,j-1},\qquad S_{T,0}=\varnothing,
\]

and let

\[
 h_T=(D_{T,d},D_{T,d-1},\ldots,D_{T,1})                 \tag{3.3}
\]

be its fixed head state.  Distinct target chains give distinct states
`h_T`.  Define the predecessor digraph `Gamma_F` on the owners by

\[
                         R\longrightarrow T
       \quad\Longleftrightarrow\quad h_R\in\mathcal A_T. \tag{3.4}
\]

Then owner/target-exact balanced selectors are exactly directed cycle covers
of `Gamma_F`.  Equivalently, one exists if and only if the bipartite graph
with left vertices `R`, right vertices `T`, and edges (3.4) has a perfect
matching.  This is exactly Hall's condition.  A zero-sidecar connected
selector is exactly a directed Hamilton cycle of `Gamma_F`.

#### Proof

At chain length `d`, Theorem 2.1 fixes the head of owner `T` to `h_T` and
allows only its tail to vary in `\mathcal A_T`.  State balance requires every
distinct `h_R` to be used exactly once as a tail, while every `h_T` already
appears exactly once as a head.  Thus the selected arcs are a permutation of
the `h_T`, supported precisely on (3.4).  Its permutation cycles are the
Euler components. \(\square\)

Root arcs which themselves form a path of predecessor edges in (3.4) may be
pinned and that prescribed path contracted before applying Hall or
Hamiltonicity.  An arbitrary root path with states outside the `h_T` bank
returns to the general boundary-flow formulation (3.2).  If a cycle cover
contains edges `R->T` and `S->U` in different cycles, and both cross edges
`S->T`,`R->U` exist, swapping the two tails merges those cycles while
preserving owners and target chains.  Hence a rectangle-crossing condition
on `Gamma_F` is an exact constructive substitute for assuming Hamiltonicity
outright.

### Theorem 3.3 (fixed-head connected rounding criterion)

More generally, let `I` be a finite set of occurrence roles.  Role `i` has
a fixed owner and named-target payload, a fixed head state `h_i`, and a
nonempty set `A_i` of legal tail states.  Put

\[
 a_v=|\{i\in I:h_i=v\}|,\qquad
 V_F=\{v:a_v>0\}.                                      \tag{3.5}
\]

Tail choices outside `V_F` may be deleted: no balanced selector can use
one.  A balanced one-copy selection exists if and only if the bipartite
role--tail graph has an exact capacitated matching with tail demand `a_v`.
Equivalently,

\[
 |J|\le \sum_{v\in N(J)}a_v\qquad(J\subseteq I).       \tag{3.6}
\]

A weakly connected balanced selection exists if and only if there are
distinct roles `R\subseteq I` and legal choices `t_i\in A_i` for `i\in R`
such that

1. the undirected edges `\{t_i,h_i\}` for `i\in R` form a spanning tree
   on `V_F`;
2. their tail-use vector
   `b_R(v)=|\{i\in R:t_i=v\}|` satisfies `b_R(v)\le a_v`; and
3. after deleting the roles in `R`, the residual role--tail graph has an
   exact capacitated matching with demands `a_v-b_R(v)`.

#### Proof

Balance says exactly that state `v` is chosen as a tail as many times as it
occurs as a fixed head, namely `a_v`.  This is the capacitated matching
problem, and (3.6) is its cloned-vertex Hall criterion.

If a balanced selector is connected, choose a spanning tree from its
underlying undirected support and let `R` be the distinct occurrence roles
carrying those tree edges.  Their tail uses are bounded by the full demand;
the remaining selected roles give the residual matching in item 3.
Conversely, the tree choices together with that residual matching use every
role once and every tail state `v` exactly `a_v` times.  They are balanced,
and the selected support contains the spanning tree, hence is connected.
\(\square\)

Fixed root or pin roles `P` are preassigned first.  Retain the original
all-role head vector `a`, remove the roles in `P`, and replace the tail
demand by `a-b_P`, where `b_P` is the literal pinned tail-use vector.  A
negative entry certifies impossibility.  Otherwise the same matching proof
applies to the unpinned roles, with the fixed rooted block (or each fixed
connected block) contracted in the spanning-tree condition.  Any upper,
exterior, residence, or compiler datum depending on the variable tail must
already be encoded in the legal lists `A_i`.

## 4. Label-preserving cycle exchanges

Let `z` be an integral selector from Theorem 3.1.  Its union with `P` is
balanced and hence is a disjoint union of rooted/unrooted Euler components.
Keep every arc of `P` protected.

Take two unprotected selected arcs in distinct components,

\[
                         e_T:u\to v,\qquad e_R:x\to y.   \tag{4.1}
\]

Call them **mutually head-compatible** when

\[
                         y\in\mathcal H_T,qquad
                         v\in\mathcal H_R.               \tag{4.2}
\]

Because their tails are unchanged, (4.2) makes the crossed arcs

\[
                         e'_T:u\to y,\qquad e'_R:x\to v  \tag{4.3}
\]

members of the same owner rectangles.

### Theorem 4.1 (transparent component transposition)

Replacing (4.1) by (4.3) preserves:

1. one trace for every owner;
2. every declared named lower-target occurrence;
3. every state indegree and outdegree; and
4. every protected root arc.

It decreases the number of weak components by one.

#### Proof

Owner identities are unchanged, and payload transparency in Theorem 2.1
preserves the target chains.  The two heads are merely transposed, so state
balance is unchanged.  No protected arc was selected.

Every edge of a balanced weak component lies on a directed circuit, hence
is not a bridge in the underlying multigraph.  Removing one selected arc
from each old component leaves both weakly connected.  Both crossed arcs
join the two old components, so their union is one component. \(\square\)

### Corollary 4.2 (zero-sidecar rooted fusion)

If every selector reachable from `z` by the switches above has, whenever it
has more than one component, a mutually head-compatible pair in different
components, repeated switches produce one connected balanced selector.
It has one Euler circuit containing `P`; choosing the prescribed root in
that circuit gives one rooted chronology with zero sidecar.

A simple sufficient special case is a common admissible head pool
`H_* \subseteq \bigcap_T \mathcal H_T`, with every selected free head in
`H_*` and at least one unprotected free arc in the root component.  Distinct
components cannot share a state, so any two component arcs have distinct
heads in `H_*` and can be transposed.

## 5. Exact bounded-sidecar alternative

If transparent exchanges stop with Euler components `K_1,...,K_s`, open
each component at a chosen state `v_i`.  Let

\[
 \operatorname{dist}(u,v)=d-\operatorname{ov}(u,v)       \tag{5.1}
\]

be the exact de Bruijn reset distance.  For any ordering beginning with the
root component, the components serialize into one rooted open Euler trail
after adding

\[
                  \sum_{i=1}^{s-1}
                    \operatorname{dist}(v_i,v_{i+1})     \tag{5.2}
\]

uncoloured sidecar arcs.  Hence a universal additive constant follows from
an ordering and opening states for which (5.2) is `O(1)`.

Neither `s=O(1)` alone nor fractional connected support implies this: a
generic reset costs `d`, and literal Boolean owner menus have parity families
with unbounded sidecar outside the canonical central profile.

## 6. Exact minimal remaining lemma

The preceding theorems reduce the canonical lower-side problem to one
Boolean-specific statement.

> **Rooted hinge-fusion lemma.**  For the triangular residual target bank,
> choose one exact owner-chain table (0.1), one admissible rooted path `P`,
> and guarded subrectangles of the hinges in Theorem 2.1 such that:
>
> 1. the root-conditioned rational balance equations (3.2) are feasible;
> 2. an integral selector supplied by Theorem 3.1 is connected under the
>    protected transpositions of Theorem 4.1, or its terminal components
>    admit an ordering with universally bounded cost (5.2).

This is strictly weaker than a direct integral coloured rotor-fusion
theorem: after item 1, owner and named-target integrality are automatic.
It is also stronger than the two known marginal results.  The pull clock
does not select one exact table (0.1), while the SCD selector does not prove
fractional balance in its hinge rectangles.

On the saturated residual face with exactly `dW` targets, any partition into
`W` chains of length at most `d` has every chain of length `d`.  There the
lemma reduces further to constructing the pinned predecessor graph
`Gamma_F` of Corollary 3.2 with Hall and a Hamilton cycle, or with a
rectangle-connected cycle-cover fibre.  No general three-matroid rounding
remains on that face.

Equivalently, before using the distinct-head simplification, Theorem 3.3
asks for one Hall-safe spanning-tree skeleton: reserve distinct literal
roles whose state edges span, and require exact capacitated Hall with demand
`a-b_R` on the unreserved roles.  This is the sharp finite lower-side
condition, not a heuristic expansion requirement.

The canonical `k=10` denominator obstruction shows that item 1 must permit
integral trades away from the displayed symmetric pull-block histogram.
The determinant-two, saturated-age, and parity examples show why a generic
fractional-to-integral theorem outside the hinge face is false.

## 7. Scope and dependencies

This note closes the integral owner/declared-lower-target rounding and the
subsequent fusion **under the rooted hinge-fusion lemma**.  It does not prove
that lemma, nor residence, arbitrary upper shadows, a fixed comparator, or
the terminal common-cap compiler.  Any such guard that varies with `B_0` or
`B_d` must be included by restricting the rectangles before (3.2).

The fractional input is
`MATH_THEOREM_CORRECTED_PULL_CLOCK_PACKING_AND_FRACTIONAL_TRACE_CIRCULATION_20260801.md`.
The exact chain-table input is supplied marginally by the protected SCD
selector.  The generic integral obstructions are in
`MATH_THEOREM_INTEGRAL_AGE_CIRCULATION_NORMALITY_AND_LATTICE_OBSTRUCTIONS_20260801.md`
and
`MATH_THEOREM_THREAD_D_TPC_ONE_COPY_COLOURED_EULER_ROUNDING_20260801.md`.
The reset metric is
`MATH_THEOREM_BOUNDED_CHAIN_TRACE_EULER_SERIALIZATION_AND_SIDECAR_DISTANCE_20260801.md`.
