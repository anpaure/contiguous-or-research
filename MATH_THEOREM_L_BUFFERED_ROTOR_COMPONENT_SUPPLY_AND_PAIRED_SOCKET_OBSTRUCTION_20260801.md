# Buffered rotor component supply and the paired-socket obstruction

Date: 2026-08-01  
Lane: L, integral sequel to aggregate rotor-semigroup rounding  
Status: unconditional package anatomy, positive-core necklace-supply theorem,
bounded-multiplicity no-go, and smallest paired-buffer/named-load
counterexamples.  A positive min-cut theorem is proved on the private
payload-zero face.  No labelled compiler or new bound on `nu(k)` is claimed.

## 0. Verdict

The two canonical role coordinates

\[
                         \ell_-=d-1,\qquad \ell_+=d+1             \tag{0.1}
\]

close the aggregate semigroup equations in
`MATH_THEOREM_AGGREGATE_MONOTONE_ROTOR_SEMIGROUP_AND_BUFFER_ROUNDING_20260801.md`.
They do not by themselves close integral rotor fusion.

There are three distinct facts.

1. A rotor package with positive permanent core has a connected
   **necklace-level** supply of legal two-edge switches.  The switches retain
   every type occurrence and hence preserve the coarse marked-rank vector.
2. Simultaneous physical fusion must choose paired low/high sockets, live
   ports, and zero net named-target payload.  Two separate buffer Hall rows
   do not compose.  A literal `2x2` paired-socket instance passes both
   marginal Hall systems but has no joint selection; an independent private
   payload example preserves every rank total but cannot preserve named
   loads.
3. Even at unlabelled type level, satisfying the exact **two-buffer**
   rounding theorem does not imply fusion.  For every `d>=3`, an explicit
   `r=2d+2` semigroup vector satisfies both canonical buffer hypotheses but
   forces the all-two age composition to be a singleton successor loop.
   The four-buffer conductor has the same obstruction as a larger subface.

Thus the bounded-buffer theorem is false without a **joint pair-labelled
connector expansion** hypothesis.  On the stronger face where connector
macros are resource-private, payload-zero and serial-safe, the exact theorem
is positive and is only one component min-cut: the contracted merge graph
must be connected.

## 1. Literal anatomy of a uniform rotor package

For a generator `g_(a,b)`, where `0<=a<d<b<r`, put

\[
 D=d-a,\qquad B=b-a+1,\qquad K=r-b-1.                            \tag{1.1}
\]

Its positive mobile compositions and age types are

\[
 \mathcal A_{B,D+1}
   =\{x=(x_0,\ldots,x_D)\in\mathbb Z_{>0}^{D+1}:\sum_i x_i=B\}, \tag{1.2}
\]

\[
 c_{a,b}(x)=(K+x_0,x_1,\ldots,x_D,
                         \underbrace{1,\ldots,1}_{a}).           \tag{1.3}
\]

The raw package successor rotates `x`.  Hence its number of raw type
necklaces is

\[
 \kappa(B,D+1)={1\over D+1}
  \sum_{q\mid\gcd(B,D+1)}\varphi(q)
       \binom{B/q-1}{(D+1)/q-1}.                                \tag{1.4}
\]

The two aggregate buffers have very different raw topology.

### Proposition 1.1 (canonical buffer anatomy)

For every `a<d`, the high-buffer package `g_(a,d+1)` has one raw type
necklace.  For every `b>d`, the low-buffer package `g_(d-1,b)` has

\[
                         \left\lfloor{b-d+2\over2}\right\rfloor \tag{1.5}
\]

raw type necklaces.

#### Proof

For `b=d+1`, (1.1) gives `B=D+2`.  Every positive composition of `B`
into `D+1` parts has one part equal to two and all others equal to one;
rotation is transitive.

For `a=d-1`, one has `D+1=2` and `B=b-d+2`.  Rotation exchanges the two
positive parts, so the orbits are the unordered positive pairs of sum `B`,
whose number is `floor(B/2)`. \(\square\)

In particular, buffer abundance is not raw connectedness.  When `d<r-1`,
every nontrivial package which supplies the top role `b=r-1` has `K=0`.
Since the canonical Ferrers demand has positive top-role multiplicity, the
positive-core result below cannot by itself finish that decomposition.  If
`d=r-1`, the top role is instead the short unit `e_d`.

## 2. Positive core gives connected necklace-level switch supply

The split-rotor formula from
`MATH_THEOREM_L_MONOTONE_ROTOR_FRACTIONAL_SCOPE_AND_INTEGRAL_FUSION_GATE_20260801.md`
says that every arc selected by a full successor permutation has mobile
form

\[
 x\longmapsto(x_0+x_D-t,t,x_1,\ldots,x_{D-1}),
 \quad1\le t\le\min\{x_0+x_D-1,K+x_0\}.                         \tag{2.1}
\]

### Theorem 2.1 (positive-core necklace 2-section is connected)

If `K>=1`, contract the raw rotation necklaces of `A_(B,D+1)`.  Join two
necklaces when two of their baseline rotation arcs admit a legal crossed
two-edge switch.  The resulting necklace graph is connected.

Each such switch changes only successor arcs.  Therefore it preserves the
complete multiset of type occurrences and every marked-rank payload attached
to those occurrences.

#### Proof

On positive compositions, allow a unit transfer between cyclically adjacent
parts, keeping every part positive.  This graph is connected: subtract one
unit successively from every nonzero excess `x_i-1` and move it around the
cycle to coordinate zero.  Every composition reaches

\[
                         (B-D,1,\ldots,1).                        \tag{2.2}
\]

Quotienting a connected graph by rotation leaves a connected graph on its
rotation orbits.

It remains to realize one unit-transfer edge by a legal switch.  Rotate the
two compositions so that the changed adjacent parts are coordinates `D`
and zero.  Write them as `x,y`, with

\[
 y_i=x_i\ (1\le i<D),\qquad |y_0-x_0|=|y_D-x_D|=1.              \tag{2.3}
\]

Cross the baseline arcs `x->R(x)` and `y->R(y)`.  In the first crossed arc,
the shifted mobile rows are equalities, the mobile/fixed-tail row is
`1<=x_D` (or `1<=y_D`), and all later singleton rows are equalities.  Its
first demand is `y_0<=K+x_0`; the reverse crossed arc needs
`x_0<=K+y_0`.  Both hold because `K>=1` and (2.3).  Equivalently, the crossed
split parameters are `t=y_0` and `t=x_0`, using
`x_0+x_D=y_0+y_D`.  If the compositions are in distinct rotation orbits,
the switch merges their directed cycles.  Thus every unit-transfer quotient
edge is legal, proving connectedness.  The type occurrences and their
occurrence-attached rank marks were never changed. \(\square\)

This theorem proves **supply**, not simultaneous fusion.  A spanning tree
of quotient edges can reuse the same baseline rotation arc at several
incident edges, and its crossed literal states may fail owner, palette,
upper, or common-cap compatibility.  A port-disjoint serializable spanning
tree is an additional integral selection theorem.

## 3. A bounded number of buffer occurrences cannot repair core-free fusion

The aggregate theorem has very large canonical buffer multiplicities.  It
must not be confused with a theorem using only `O(1)` extra buffer
occurrences.

### Theorem 3.1 (core-free added-buffer lower bound)

Let `V` contain one occurrence of every positive `(d+1)`-part composition
of `r`, and let `kappa` be its rotation-necklace count.  Add `t` arbitrary
age-type occurrences of total size `r`.  If the resulting occurrence
multiset has one legal successor cycle and `kappa>1`, then

\[
             \boxed{t\ge\left\lceil{\kappa\over r+1}\right\rceil.} \tag{3.1}
\]

Consequently no bounded number of buffer occurrences fuses the core-free
rotor as `kappa` grows.

#### Proof

Let `M_i` be the sum of age coordinate `i` over all occurrences.  Summing
the successor inequalities gives

\[
 D_i=M_i-M_{i+1}\ge0,
 \qquad S=\sum_{i=0}^{d-1}D_i=M_0-M_d.                           \tag{3.2}
\]

The original coordinate-symmetric set `V` contributes zero to `M_0-M_d`.
Each added age type contributes at most `r`, so `S<=rt`.  An arc leaving an
original composition has zero total slack only when its head is its block
rotation.  At most `t` original necklaces contain the type of an added
occurrence; every other one needs a positive-slack exit in a single global
cycle.  Hence

\[
                         \kappa-t\le S\le rt,
\]

which is (3.1).  The excluded case `kappa=1,t=0` is the one raw necklace
and needs no fusion. \(\square\)

If occurrences are replaced rather than added, the sharper bound
`t>=ceil(kappa/[2(r-d)])` from the preceding integral-fusion theorem
applies for `kappa>1`, with the same trivial one-necklace exception.  These
are occurrence bounds.  They become named-target lower bounds only under
private anchors or an explicit no-cancellation rule.

### Theorem 3.2 (all aggregate conductor buffers can still force a loop)

For every `d>=4`, set

\[
                         r=2d+2,\qquad Q=Q_{r,d},\qquad
                         N=\left\lceil{Q+1\over d}\right\rceil. \tag{3.3}
\]

Take the occurrence multiset consisting of:

1. one complete core-free long package `g_(0,r-1)`, namely every positive
   `(d+1)`-composition of `r` once;
2. `N` complete high-buffer packages `g_(0,d+1)`; and
3. `Q+1` unit short packages at each of the three role coordinates
   `d-3,d-2,d-1`.

Its aggregate role vector belongs to the uniform rotor semigroup and obeys

\[
 \min\{A_{d-3},A_{d-2},A_{d-1},A_{d+1}\}\ge Q+1,               \tag{3.4}
\]

so it satisfies the full conductor hypothesis of the aggregate theorem.
Nevertheless no legal successor permutation on these occurrences is one
cycle.

#### Proof

Membership in the semigroup is by the displayed package decomposition.
Each short unit contributes once to its named low role.  Since

\[
             g_{0,d+1}=e_0+d e_{d+1},                            \tag{3.5}
\]

the high role has multiplicity `dN>=Q+1`; hence (3.4).

Now inspect age types.  The core-free package is the coordinate-symmetric
set of positive compositions of `2d+2`.  A high-buffer package has types

\[
             (d+x_0,x_1,\ldots,x_d),qquad
             x_i>0,\quad\sum_i x_i=d+2,                          \tag{3.6}
\]

so exactly one of the `x_i` is two and all others are one.  Every short unit
may use the standard self-loop type

\[
                         (d+2,1,\ldots,1).                        \tag{3.7}
\]

Consequently the total coordinate marginals satisfy

\[
                         M_i=M_{i+1}\qquad(1\le i<d).             \tag{3.8}
\]

For any legal successor permutation `F`, each difference
`c_i-F(c)_(i+1)` is nonnegative.  Summing and using (3.8) forces

\[
                         F(c)_{i+1}=c_i\qquad(1\le i<d)          \tag{3.9}
\]

on every selected edge.

The only source occurrences with

\[
                         (c_1,\ldots,c_{d-1})=(2,\ldots,2)
\]

are the three core-free types

\[
                         s_i=(i,2^{d-1},4-i),\qquad i=1,2,3.     \tag{3.10}
\]

The only target occurrences with

\[
                         (c_2,\ldots,c_d)=(2,\ldots,2)
\]

are

\[
                         t_j=(4-j,j,2^{d-1}),\qquad j=1,2,3.     \tag{3.11}
\]

Here `2^(d-1)` denotes a string of `d-1` twos.  The buffer types (3.6)--
(3.7) have at most one nonunit coordinate after coordinate zero, so none
enters these lists when `d>=4`.

Equation (3.9) forces a bijection from the three sources (3.10) to the three
targets (3.11).  The remaining first transition inequality is exactly

\[
                              j\le i.                            \tag{3.12}
\]

The `3x3` triangular bipartite graph (3.12) has the unique perfect matching
`i=j`.  In particular

\[
                         (2,2,\ldots,2)\longmapsto(2,2,\ldots,2) \tag{3.13}
\]

is a forced singleton loop.  Since the occurrence multiset has other
vertices, it cannot be one successor cycle. \(\square\)

The counterexample is already at `d=4,r=10`.  It is stronger than a socket
shortage: unlimited copies of the actual high-buffer package and all low
conductor coordinates leave the tight internal overlap block (3.12)
unchanged.  It also precedes owner and named-target assignment, so no choice
of those labels repairs it while retaining this occurrence multiset.

For the smallest case, `Q_(10,4)=784` and `N=197`.  One exact aggregate
vector is

\[
 A_0=267,\quad A_1=A_2=A_3=785,\quad A_5=788,
 \quad A_9=56,\quad \sum_\ell A_\ell=3466.                       \tag{3.14}
\]

### Theorem 3.3 (the exact internal-word Ferrers cuts)

Let `Omega` be any occurrence multiset satisfying

\[
                         M_i=M_{i+1}\qquad(1\le i<d).             \tag{3.15}
\]

For an internal word `w=(w_1,...,w_(d-1))`, define

\[
\begin{aligned}
 S_w&=\{c\in\Omega:(c_1,\ldots,c_{d-1})=w\},\\
 T_w&=\{c'\in\Omega:(c'_2,\ldots,c'_d)=w\}.
\end{aligned}                                                    \tag{3.16}
\]

There is an **unlabelled age-type occurrence** legal successor perfect
assignment if and only if, for every
`w`,

\[
 |S_w|=|T_w|,
 \qquad
 |\{c'\in T_w:c'_1>t\}|
   \le |\{c\in S_w:c_0>t\}|\quad\text{for every integer }t.     \tag{3.17}
\]

After such a perfect assignment is chosen, one successor cycle additionally
requires the ordinary proper-subset directed connectivity cuts.

#### Proof

As in (3.8)--(3.9), every legal selected edge is tight in coordinates
`1,...,d-1`.  Hence it lies in one block `S_w x T_w`, and within that block
the only remaining type inequality is

\[
                              c'_1\le c_0.                        \tag{3.18}
\]

This is a Ferrers bipartite graph.  Its exact Hall family consists of the
upper threshold sets in (3.17), together with equality of the two shores.
The blocks are disjoint, so their perfect matchings compose.  Finally, a
perfect successor assignment is a cycle cover; it is one cycle exactly when
every nonempty proper occurrence subset has an outgoing selected edge.
\(\square\)

For `w=2^(d-1)` in Theorem 3.2, the source capacities and target demands are
both `{1,2,3}`.  Every threshold cut is tight, so the Ferrers matching is
uniquely `i->i` and forces (3.13).  This identifies the precise missing
expansion: a buffer bank must enter every tight internal-word block or create
slack in at least one of coordinates `1,...,d-1`; aggregate role totals do
not see these cuts.

### Theorem 3.4 (the exact two-buffer theorem can still force a loop)

For every `d>=3`, put

\[
                         r=2d+2,qquad N\ge Q^\circ_{r,d}.       \tag{3.19}
\]

Take one complete core-free package `g_(0,r-1)` and `N` copies of the
canonical pair package `g_(d-1,d+1)`.  Its aggregate vector is

\[
\begin{aligned}
 A_0&=\binom{r-2}{d},& A_{r-1}&=\binom{r-2}{d-1},\\
 A_{d-1}&=N,& A_{d+1}&=N,
\end{aligned}                                                     \tag{3.20}
\]

with all other coordinates zero.  It is a literal sum of rotor generators,
has `L=H`, and satisfies both exact balanced-rounding hypotheses

\[
                         A_{d-1},A_{d+1}\ge Q^\circ_{r,d}.       \tag{3.21}
\]

Nevertheless no legal successor permutation on these occurrences is one
cycle.

#### Proof

Membership is the displayed package decomposition.  The identity

\[
 d\binom{2d}{d}=(d+1)\binom{2d}{d-1}                            \tag{3.22}
\]

balances the core-free package, and each pair package contributes one unit
to each resource shore.

The pair package has exactly two age types,

\[
 p=(d+1,2,1^{d-1}),\qquad h=(d+2,1^d).                           \tag{3.23}
\]

The core-free package is the coordinate-symmetric set of all positive
`(d+1)`-compositions of `2d+2`.  Thus the total coordinate marginals obey

\[
                         M_i=M_{i+1}\qquad(2\le i<d).             \tag{3.24}
\]

Every legal selected edge is consequently tight in these coordinates:

\[
                         F(c)_{i+1}=c_i\qquad(2\le i<d).          \tag{3.25}
\]

Restrict to sources with `c_2=...=c_(d-1)=2`.  Neither buffer type (3.23)
lies in this fibre.  The core-free sources are parametrized by

\[
 P=\{(x_0,x_1)\in\mathbb Z_{>0}^2:x_0+x_1\le5\},                \tag{3.26}
\]

with terminal coordinate `6-x_0-x_1`.  Targets with
`c'_3=...=c'_d=2` are parametrized by the identical set
`(y_1,y_2) in P`, with fresh coordinate `6-y_1-y_2`.  Equation (3.25)
leaves exactly

\[
                         y_1\le x_0,qquad y_2\le x_1.           \tag{3.27}
\]

Any bijection from `P` to itself dominated coordinatewise is the identity:
sum both coordinates over every matched pair, and the total nonnegative
slack is zero.  In particular the unique occurrence

\[
                         u=(2,2,\ldots,2)                         \tag{3.28}
\]

must map to itself.  This forced singleton loop excludes one global cycle.
\(\square\)

The smallest instance is `d=3,r=8`, where `Q^circ=140`, `N=140`, and

\[
                         A=(20,0,140,0,140,0,0,15),
                         \qquad\sum_\ell A_\ell=315.             \tag{3.29}
\]

The obstruction precedes owner and named-target labelling, so relabelling
cannot repair it while retaining this occurrence multiset and payload.

### Theorem 3.5 (general tight-word product-order Hall cuts)

Let `1<=h<d` and let `Omega` be any occurrence multiset satisfying

\[
                         M_i=M_{i+1}\qquad(h\le i<d).             \tag{3.30}
\]

For a word `w` of length `d-h`, define

\[
\begin{aligned}
 S_w&=\{c\in\Omega:(c_h,\ldots,c_{d-1})=w\},\\
 T_w&=\{c'\in\Omega:(c'_{h+1},\ldots,c'_d)=w\},\\
 x(c)&=(c_0,\ldots,c_{h-1}),\\
 y(c')&=(c'_1,\ldots,c'_h).
\end{aligned}                                                     \tag{3.31}
\]

There is an **unlabelled age-type occurrence** legal successor perfect
assignment if and only if, for every `w`, the two shores have equal size and

\[
 |\{c'\in T_w:y(c')\in\mathcal U\}|
   \le |\{c\in S_w:x(c)\in\mathcal U\}|                         \tag{3.32}
\]

for every upward-closed set `U` in the coordinatewise order on
`Z_(>=0)^h`.  A one-cycle assignment additionally requires every ordinary
proper-subset directed connectivity cut.

#### Proof

Equation (3.30) makes every selected edge termwise tight in coordinates
`h,...,d-1`.  Edges therefore decompose into the disjoint blocks
`S_w x T_w`, where their remaining condition is exactly

\[
                              y(c')\le x(c)                       \tag{3.33}
\]

coordinatewise.  Finite-poset Strassen, equivalently Hall in this dominance
graph, is precisely (3.32) plus equality of shore sizes.  The block
matchings compose.  They form a cycle cover, and the usual directed cuts are
exactly the condition that this cover has one cycle.  This statement does
not impose fixed labelled owners, labelled partitions, or guarded physical
arcs; those are separate lift constraints. \(\square\)

Theorem 3.4 is the case `h=2`, `w=2^(d-2)`.  Both prefix multisets equal
`P`, every product-order Hall cut is tight in aggregate, and domination
forces the identity matching.  The exact missing expansion is therefore
word/fibre-level: a buffer must enter each tight block or create slack in
one of the frozen age coordinates.  The two aggregate buffer totals do not
see these cuts.

### Theorem 3.6 (canonical-catalogue decomposition-independent no-go)

For every `d>=4`, put

\[
\begin{gathered}
 r=2d+2,\qquad N=Q^\circ_{r,d},\\
 q_0=\binom{2d}{d},\qquad p_0=\binom{2d}{d-1},\qquad
 T=\left\lfloor{N\over(d+1)p_0}\right\rfloor+1.                 \tag{3.34}
\end{gathered}
\]

Define the aggregate vector

\[
 A_0=q_0T,qquad A_{r-1}=p_0T,qquad
 A_{d-1}=A_{d+1}=N,                                             \tag{3.35}
\]

with all other coordinates zero.  It is balanced, belongs to the rotor
semigroup, and satisfies the exact two-buffer threshold.  Nevertheless
**every** decomposition of this same vector into the canonical uniform
rotor packages and canonical unit self-loops has no one-cycle legal
successor ordering.

#### Proof

The displayed vector is realized by `T` copies of `g_(0,r-1)` and `N`
copies of `g_(d-1,d+1)`, so it belongs to the semigroup; (3.22) proves
balance and the two buffer coordinates equal `Q^circ`.

In any other decomposition, a nontrivial generator can use only a nonzero
low coordinate `a in {0,d-1}` and a nonzero high coordinate
`b in {d+1,r-1}`.  Suppose it used no `g_(0,r-1)`.  Then all `p_0T` copies
of the top role would have to come from `g_(d-1,r-1)`.  Each such copy
consumes `d+1` occurrences of the low buffer, so this would require

\[
                         (d+1)p_0T>N,                            \tag{3.36}
\]

contrary to (3.35).  Thus every decomposition contains at least one
complete core-free `g_(0,r-1)` package.

Consider again the word `w=2^(d-2)` in coordinates `2,...,d-1`.  The other
possible nontrivial packages are `g_(0,d+1)`, `g_(d-1,d+1)`, and
`g_(d-1,r-1)`.  Their types have this word all one, or have at most one
coordinate equal to two; unit packages also have the all-one word.  Since
`d>=4`, none enters the `w` fibre.  That fibre therefore consists of `z>=1`
identical copies of the core-free prefix downset `P` from (3.26) on both
shores.

All four possible nontrivial packages, and the canonical unit self-loops,
have equal total age marginals in coordinates `2,...,d`.  Hence Theorem 3.5
with `h=2` applies to every such decomposition.

Every dominated perfect matching between these identical multisets has
zero total coordinate slack and hence is the identity on prefix-pair values,
equivalently raw rotation on the full age types.  In particular, the `z`
occurrences of `u=(2,...,2)` map only among themselves.  They form a
nonempty closed successor block, so no decomposition admits one global
cycle. \(\square\)

The smallest instance is

\[
 d=4,\quad r=10,\quad N=775,\quad T=3,
 \qquad(A_0,A_3,A_5,A_9)=(210,775,775,168),                     \tag{3.37}
\]

with total owner mass `1928`.  Thus the failure is not an artefact of a bad
choice among canonical package decompositions; it is invisible to the two
aggregate buffer coordinates themselves.  A noncanonical unmarked `e_0`
connector realization is outside this no-go and would itself be an
additional physical fusion construction, not a consequence of the
semigroup equations.

## 4. Exact paired-buffer fusion system

Fix a package decomposition and contract its `C` raw rotor necklaces.  Let
`E` be a catalogue of certified merge macros.  A macro `e` has:

* a component pair in the contracted graph;
* one low socket `lambda(e)` and one high socket `eta(e)`;
* a set `R_e` of other unit resources; and
* a signed named-target load vector `Delta_e`.

The payload vectors are assumed context-independent and additive in every
allowed serial order.  If a payload depends on the current boundary, that
boundary state must be included in the macro catalogue before using the
linear equation below.

Assume a selected set is **serial-safe** precisely when it has a rooted leaf
order in which every deleted baseline arc remains live, all physical ports
are distinct, and every switch merges two current components without
splitting either.

### Theorem 4.1 (exact serial-safe bounded-buffer system)

Within this macro semantics, zero-defect fusion exists if and only if there
are binary variables `z_e` satisfying

\[
\begin{aligned}
 z(E)&=C-1,                                                        \tag{4.1}\\
 z(E[X])&\le |X|-1 &&(\varnothing\ne X\subseteq[C]),              \tag{4.2}\\
 \sum_{e:\lambda(e)=\lambda}z_e&\le1 &&(\text{each low socket }\lambda),\tag{4.3}\\
 \sum_{e:\eta(e)=\eta}z_e&\le1 &&(\text{each high socket }\eta),\tag{4.4}\\
 \sum_{e:\rho\in R_e}z_e&\le1 &&(\text{each other unit resource }\rho),\tag{4.5}\\
 \sum_e\Delta_e(t)z_e&=0 &&(\text{each named target }t),          \tag{4.6}
\end{aligned}
\]

and the selected macro set is serial-safe.  Equations (4.1)--(4.2) say
exactly that the component edges form a spanning tree; equivalently they may
be separated by the component cuts `z(delta(X))>=1` together with the edge
count.

#### Proof

A serial-safe spanning tree merges one leaf component at a time and ends in
one component.  Equations (4.3)--(4.5) are precisely resource injectivity,
and (4.6) is exact named-load preservation.  Conversely, a serial-safe
fusion starts with `C` components and every selected macro reduces the
current component count by exactly one.  It therefore uses exactly `C-1`
macros; their component edges are a spanning tree, and projection gives
every displayed row. \(\square\)

This is not an ordinary min-cut problem in general: it is a graphic row,
two paired partition systems, other resources, and a load lattice.  The two
aggregate buffer inequalities remember only the marginals of
(4.3)--(4.4).

## 5. The smallest paired-socket and named-load counterexamples

### Proposition 5.1 (the `2x2` paired-buffer obstruction)

Take three component vertices on a path, so its two component edges are
forced merge tasks `T_1,T_2`.  There are two low sockets `L_1,L_2` and two
high sockets `H_1,H_2`.  Give the tasks these options:

\[
\begin{array}{c|c}
T_1&(L_1,H_1),(L_2,H_2)\\
T_2&(L_1,H_2),(L_2,H_1).
\end{array}                                                     \tag{5.1}
\]

Both the low and high projected task--socket graphs are `K_(2,2)` and pass
every marginal Hall cut.  Nevertheless no choice of one option per task is
jointly resource-disjoint.

#### Proof

Choosing `(L_1,H_1)` for `T_1` conflicts with the first option for `T_2` at
`L_1` and with its second at `H_1`.  Choosing `(L_2,H_2)` conflicts with the
two options at `H_2` and `L_2`, respectively. \(\square\)

This is minimal: one task has no pairing obstruction, and one socket on
either shore cannot have two separately feasible marginal matchings.

### Proposition 5.2 (aggregate ranks do not imply named loads)

Let every available crossing macro `e` have a source target `S_e` and
destination target `T_e` of the same rank, with all `S_e,T_e` pairwise
distinct across the entire catalogue, and put

\[
                         \Delta_e={\bf1}_{T_e}-{\bf1}_{S_e}.      \tag{5.2}
\]

Then every macro preserves the aggregate rank histogram.  But no nonempty
selection satisfies (4.6), because its private coordinates cannot cancel.
In particular, every spanning fusion changes at least `C-1` named loads.

Thus even perfect component expansion and unlimited scalar buffer counts do
not imply named-load preservation.

## 6. The exact positive min-cut face

### Corollary 6.1 (private payload-zero fusion)

Assume `C>=2`.  Suppose every candidate merge macro is payload-zero, its low/high sockets
and all other resources are private to that macro, and every spanning tree
of candidate component edges is serial-safe.  Then zero-defect fusion exists
if and only if the contracted merge graph is connected, equivalently

\[
             \min_{\varnothing\ne X\subsetneq[C]}|\delta_E(X)|\ge1. \tag{6.1}
\]

#### Proof

Necessity is immediate.  If (6.1) holds, choose any spanning tree.  Resource
and load rows are automatic and serial safety lets Theorem 4.1 apply.
\(\square\)

On the same otherwise private, payload-zero face, with only one nonprivate
buffer shore, the graphic and partition rows form an ordinary two-matroid
intersection.  With both paired shores and named loads, Proposition 5.1
shows why separate Hall/min-cut checks are unsound.

## 7. Consequence for the canonical semigroup theorem

The aggregate theorem supplies enough **counts** in coordinates `d-1` and
`d+1`; it supplies neither the pair-labelled options (5.1) nor the
zero-payload equation (4.6).  Positive core guarantees connected quotient
switch supply by Theorem 2.1, but simultaneous live ports remain open, and
the unavoidable top-role packages have core zero.  At the exact zero-defect
level, the next theorem would be:

> construct a serial-safe, pair-labelled low/high connector atlas whose
> component graph spans every core-free and positive-core necklace, whose
> socket projections are jointly integral, and whose literal named-target
> payload is zero, while retaining the upper/common-cap guards.

The weaker and now preferred first target is recorded in
`MATH_THEOREM_L_NRFC_BOUNDED_DEBT_INCIDENCE_CIRCUIT_FUSION_20260801.md`:
replace payload zero by a merge-tree component cocycle with `O(1)` root
debt, or by only `O(1)` unmatched chronological port chains, and repair the
bounded terminal palette debt afterward.  The counterexamples above still
show that aggregate buffers and marginal Hall alone do not imply that
weaker cancellation law.

No strengthening of the scalar buffer inequalities alone can prove this;
Propositions 5.1--5.2 are literal finite obstructions to that implication.
