# Colored Euler lifts and the exact linear chronology gate

Date: 2026-07-28

Status: unconditional reduction.  It proves that arbitrary separately
feasible hypersimplex completions do **not** lift, gives the exact
adjacent-rank obstruction, and gives a necessary-and-sufficient integral
flow formulation for one simultaneous linear chronology.  It does not
construct the missing `k=15` chronology.

## 0. Outcome

The hypersimplex theorem solves the marginal problem at each rank, but
there are two further coupling layers:

1. adjacent rows must be the vertex and intersection-colour multisets of
   one Johnson Euler trail; and
2. those adjacent Euler trails must be the successive projections of one
   common safe chronology.

The first layer has an exact coloured-multigraph formulation and a
capacitated Hall relaxation.  In particular, every nonempty family
`C` of proposed intersection colours must satisfy the chronological
subtour inequality

\[
 \sum_{R\in C}c_R
 \le
 \sum_{A\in N(C)}m_A-1.                         \tag{0.1}
\]

This inequality is invisible to total multiplicity and point degrees.
There is a six-coordinate counterexample in which both rows are hole-free,
the excess vector is an integer point of the relevant hypersimplex, all
coordinate run counts are positive, but (0.1) fails.

The second layer is exactly one integer flow in a boundary-capped safe
de Bruijn graph.  The variables are local windows, not complete
chronologies; flow balance plus connected support invokes Euler's theorem
to recover the chronology.  Thus the remaining gate is no longer the
informal phrase “synchronize the rankwise trades”.  It is one explicit
integer flow with linear middle-owner and all-depth colour projections,
plus the standard connected-support inequalities.

## 1. Adjacent rows as a coloured Euler trail

Fix `1<=s<=k`.  Let

\[
 \mathcal A=\binom{[k]}s,
 \qquad
 \mathcal R=\binom{[k]}{s-1}.
\]

Suppose `m_A` is a nonnegative desired multiplicity on `mathcal A` and
`c_R` a nonnegative desired multiplicity on `mathcal R`, with

\[
 n:=\sum_A m_A,
 \qquad
 \sum_Rc_R=n-1.                                  \tag{1.1}
\]

For `R in mathcal R`, its extensions are the `s`-sets `A superset R`.
An edge between two distinct extensions `A,B` is a Johnson edge and has
intersection colour `R=A cap B`.

### Theorem 1.1 (exact coloured-Euler criterion)

Assume `n>=2`.  There is a Johnson walk

\[
 A_0,A_1,\ldots,A_{n-1}                           \tag{1.2}
\]

whose vertex-type multiplicities are `m` and whose intersection-colour
multiplicities are `c` if and only if there are:

* endpoint numbers `e_A in {0,1,2}` with
  `sum_A e_A=2` and `e_A<=2m_A`; and
* nonnegative integers

\[
 y_{R;A,B}=y_{R;B,A}
\]

for `A ne B`, `A cap B=R`, satisfying

\[
 \sum_{\{A,B\}:A\cap B=R}y_{R;A,B}=c_R
 \qquad(R\in\mathcal R),                         \tag{1.3}
\]

\[
 \sum_{R\subset A}\ \sum_{B\ne A}y_{R;A,B}
   =2m_A-e_A
 \qquad(A\in\mathcal A),                         \tag{1.4}
\]

and the multigraph on the positive-multiplicity members of `mathcal A`
with these edge multiplicities is connected.  Equivalently, connectivity
can be imposed linearly by

\[
 \sum_{\substack{A\in U,\ B\notin U\\R=A\cap B}}
       y_{R;A,B}\ge1                              \tag{1.5}
\]

for every nonempty proper subset `U` of the positive-multiplicity support.

#### Proof

Given (1.2), put one multigraph edge between the types of every consecutive
pair and give it their intersection colour.  Equations (1.3) and (1.4)
follow, where `e_A` counts how many of the two ends of the walk have type
`A`.  The traversed multigraph is connected.

Conversely, (1.4) says that the odd-degree vertices are exactly the two
distinct types with `e_A=1`, unless one type has `e_A=2`, in which case all
degrees are even and the desired trail starts and ends at that type.
Connectedness and Euler's theorem give a trail using every selected edge.
The number of occurrences of type `A` in its vertex list is

\[
 {\deg(A)+e_A\over2}=m_A.
\]

Equation (1.3) gives the prescribed colour multiset.  \(\square\)

This theorem is exact, but contains the Hamilton-path problem as a special
case and is not claimed to be an easy algorithm.  The next projection is a
genuine polynomial-time cut test.

## 2. The capacitated Hall projection

For a putative solution of Theorem 1.1 define the colour half-edge loads

\[
 h_{R,A}:=\sum_{B\ne A}y_{R;A,B}.
\]

They satisfy

\[
 \sum_{A\supset R}h_{R,A}=2c_R,                  \tag{2.1}
\]

\[
 \sum_{R\subset A}h_{R,A}=2m_A-e_A,             \tag{2.2}
\]

\[
 0\le h_{R,A}\le c_R.                            \tag{2.3}
\]

The last inequality holds because a loopless multigraph with `c_R` edges
has degree at most `c_R` at one vertex.

### Lemma 2.1 (half-edge realization)

Every integral solution of (2.1)--(2.3) can be paired, separately for each
`R`, into a loopless multigraph with `c_R` edges and degrees `h_(R,A)`.

#### Proof

For a fixed `R`, the degrees sum to `2c_R` and the maximum is at most
`c_R`.  Pair two positive stubs belonging to distinct extensions, always
using a current maximum-degree extension.  After one pair is removed the
new maximum is at most `c_R-1`; induction gives the required loopless
multigraph.  Parallel edges are allowed, as they are for repeated
occurrences in a trace row.  \(\square\)

Thus (2.1)--(2.3) are necessary and sufficient for a union of one Euler
trail and zero or more Euler circuits with the prescribed marginals.
Connectedness is the only condition lost in this projection, and it has an
exact support formulation.

For a feasible half-edge flow `h`, let `B_h` be the bipartite graph on the
positive colour types and positive vertex types, with

\[
                         RA\in E(B_h)\iff h_{R,A}>0. \tag{2.3a}
\]

### Theorem 2.2 (support-connected flow is exactly the Euler lift)

A feasible integral half-edge flow `h` has a connected coloured-multigraph
realization if and only if `B_h` is connected.

#### Proof

If a coloured realization `G` is connected, replace every edge `AB` of
colour `R` by the two-edge path `A-R-B`.  The resulting graph is a spanning
subgraph of `B_h`, so `B_h` is connected.

Conversely, start with any per-colour pairing supplied by Lemma 2.1.  Its
coloured multigraph has one component containing the two odd endpoints (or
the distinguished cut point when `e_A=2`) and zero or more Eulerian
components.  If it is disconnected while `B_h` is connected, some colour
`R` has one paired edge `ab` in one component and another paired edge `cd`
in a different component.  Replace them by

\[
                         ac,\qquad bd,             \tag{2.3b}
\]

both still coloured `R`.  The four endpoint types are distinct across the
two old components, so these are legal loopless `R`-edges.

If both old components are Eulerian, neither deleted edge is a bridge and
the cross-pairing joins them.  If one is the unique open-trail component,
deleting its edge gives one or two trails, deleting an edge of the Eulerian
component gives one trail, and the two cross edges join all pieces into one
open-trail component.  Thus the number of components decreases by one.
The half-edge loads, vertex degrees, and colour counts do not change.
Iterating produces a connected realization.  \(\square\)

### Corollary 2.3 (spanning-tree plus max-flow criterion)

The adjacent-row lift exists if and only if there are an endpoint vector
`e` and a spanning tree `tau` of the allowed containment graph such that
the capacitated flow (2.1)--(2.3) remains feasible after imposing

\[
                         h_{R,A}\ge1\qquad(RA\in\tau). \tag{2.3c}
\]

For a fixed `tau`, this is one ordinary integral max-flow after subtracting
one unit from the supplies, demands, and tree-edge capacities.  Hence all
non-network content at one adjacent pair is the choice of a support tree;
pairing its half-edges is free by Theorem 2.2.

#### Proof

Every connected support contains a spanning tree.  Conversely (2.3c)
makes the support connected, and Theorem 2.2 applies.  Lower bounds of one
are removed in the standard way, leaving the stated residual flow.
\(\square\)

The system is a capacitated bipartite flow.  Its exact max-flow/min-cut
criterion is the following.  Put

\[
 p_R=2c_R,
 \qquad
 d_A=2m_A-e_A.
\]

Then (2.1)--(2.3) are feasible if and only if totals agree and, for every
`U subseteq mathcal R` and `V subseteq mathcal A`,

\[
 \boxed{
 \sum_{R\in U}p_R-\sum_{A\in V}d_A
 \le
 \sum_{\substack{R\in U,\ A\notin V\\R\subset A}}c_R.}
                                                               \tag{2.4}
\]

This follows by taking the cut with `U` and `V` on the source side in the
network

\[
 s\longrightarrow R\longrightarrow A\longrightarrow t
\]

with capacities `p_R,c_R,d_A`.  Network integrality makes fractional and
integral feasibility identical at this projected stage.

## 3. The chronological subtour inequalities

For a family `C subseteq mathcal R`, put

\[
 N(C)=\{A\in\mathcal A:\text{ some }R\in C\text{ is contained in }A\}.
\]

### Theorem 3.1 (chronological cut)

Every Johnson walk with marginals `(m,c)` satisfies, for every nonempty
`C`,

\[
 \boxed{
 \sum_{R\in C}c_R
 \le
 \sum_{A\in N(C)}m_A-1.}                         \tag{3.1}
\]

#### Proof

Mark the positions of the walk whose vertex type belongs to `N(C)`.  A
transition coloured by a member of `C` has both endpoints marked.  If the
marked positions form `b>=1` runs, the total number of transitions with
both endpoints marked is

\[
 \sum_{j=1}^b(\text{run length}_j-1)
 =\sum_{A\in N(C)}m_A-b
 \le\sum_{A\in N(C)}m_A-1.
\]

The `C`-coloured transitions are a subset of these.  \(\square\)

These are subtour-elimination cuts: they say that colour mass supported on
a proper cluster of vertex types cannot close a cycle inside that cluster
and still belong to one global chronology.

### Proposition 3.2 (separate hypersimplex feasibility does not lift)

Let `k=6` and `s=3`.  Take the upper multiset to be every member of
`binom([6],3)` exactly once.  Take the lower multiset to be every member of
`binom([6],2)` exactly once, together with three additional copies of
`{1,2}` and one additional copy of `{3,4}`.

Both rows are hole-free and have the correct consecutive sizes

\[
 20,qquad19.
\]

The lower excess point-degree vector is

\[
 (3,3,1,1,0,0),                                  \tag{3.2}
\]

which lies in `4 Delta(6,2)`: its coordinates lie in `[0,4]` and sum to
`2*4`.  Hence it is exactly a valid hypersimplex completion.  Including
the complete rank-two layer, the lower point degrees are

\[
 (8,8,6,6,5,5).                                   \tag{3.3}
\]

Since the upper point degrees are all `10`, even the candidate coordinate
run counts

\[
 (2,2,4,4,5,5)                                    \tag{3.4}
\]

are positive.

Nevertheless no chronology exists.  The colour `{1,2}` has load four,
whereas its neighbourhood consists of the four triples containing
`{1,2}`, each available once.  Theorem 3.1 gives the impossible inequality

\[
 4\le4-1.
\]

Thus total size, no holes, point degrees, and hypersimplex decomposability
do not imply even a two-row chronological lift.  In particular there can
be no theorem lifting *arbitrary* separate completions from the preceding
hypersimplex note.

## 4. One exact all-depth linear flow

The adjacent-row theorem still does not synchronize the trails at
different depths.  The exact synchronization is a boundary-corrected
de Bruijn flow.

Fix `d>=1`.  A **two-sided `d`-safe window** is a Johnson word

\[
 e=(A_0,A_1,\ldots,A_d)                            \tag{4.1}
\]

such that every subword of `q<=d` transitions has intersection rank
`r-q` and union rank `r+q`.  Equivalently, within each such subword all
deleted and inserted labels are distinct and no label is used in both
directions.

Let `D_d(k,r)` be the de Bruijn digraph whose vertices are two-sided safe
words of `d` vertices and whose arcs are the windows (4.1), directed from
their length-`d` prefix to their length-`d` suffix.  For an arc put

\[
 \lambda_q(e)=\bigcap_{h=0}^qA_h
 \qquad(0\le q\le d).                              \tag{4.2}
\]

For a terminal state `v=(B_0,...,B_(d-1))`, define its suffix correction

\[
 \sigma_{q,S}(v)=
 \#\left\{0\le j<d-q:
       \bigcap_{h=0}^qB_{j+h}=S\right\}.           \tag{4.3}
\]

At `q=0`, this simply counts the entries of `v` equal to `S`.

### Theorem 4.1 (linear safe-chronology flow)

Let `mu_q` be prescribed multiplicities on rank `r-q` for `1<=q<=d`.
There exists a two-sided depth-`d` safe Hamilton chronology

\[
 T_0,T_1,\ldots,T_{W-1},
 \qquad W=\binom kr,                               \tag{4.4}
\]

whose depth-`q` lower trace has multiplicity `mu_q` if and only if there
are two states `u,v` and a nonnegative integral arc vector `z` on
`D_d(k,r)` satisfying all of the following.

**Boundary flow:**

\[
 \sum_{e\in\delta^+(w)}z_e-
 \sum_{e\in\delta^-(w)}z_e
 =\mathbf1_{w=u}-\mathbf1_{w=v}                   \tag{4.5}
\]

for every state `w`.

**One copy of every middle owner:**

\[
 \sum_{e:A_0=S}z_e+\sigma_{0,S}(v)=1
 \qquad\left(S\in\binom{[k]}r\right).             \tag{4.6}
\]

**All prescribed lower rows:**

\[
 \sum_{e:\lambda_q(e)=S}z_e+\sigma_{q,S}(v)
 =\mu_q(S)                                         \tag{4.7}
\]

for `1<=q<=d` and `S in binom([k],r-q)`.

**One Euler component:** all states incident with a positive `z`-arc,
together with `u,v`, lie in one weak component.  Equivalently one may add
the standard directed-support cut inequalities.

#### Proof

Given (4.4), take one de Bruijn arc for every full `d`-transition window,
starting at positions `0,...,W-d-1`.  Consecutive windows overlap, giving
(4.5).  Their first entries account for positions `0,...,W-d-1`; the
terminal state accounts for the final `d` positions, proving (4.6).
Likewise, the arc labels in (4.2) account for all depth-`q` windows whose
start is at most `W-d-1`, while (4.3) accounts for the remaining `d-q`
suffix windows.  This proves (4.7).  The used arcs form one trail.

Conversely, (4.5) and connected support give an Euler trail from `u` to
`v` using each arc with multiplicity `z_e`.  Consecutive de Bruijn arcs
overlap in `d` owners, so the trail spells one two-sided safe Johnson word.
Equation (4.6) says that its `W` positions enumerate the entire middle
layer exactly once.  Equation (4.7), with the suffix correction, gives the
prescribed trace multiplicities at every depth.  \(\square\)

Upper-union multiplicities are included without changing the theorem: add
the analogous arc labels

\[
 \upsilon_q(e)=\bigcup_{h=0}^qA_h
\]

and their terminal corrections to (4.7).

### Corollary 4.2 (exact lift lattice around a fixed chronology)

Fix the two endpoint states and a base chronology with arc vector `z_0`.
A family of signed lower- and upper-row changes is linearly liftable with
those endpoints if and only if it is the image, under the corresponding
trace-label maps, of an integer circulation `eta` satisfying

\[
 \partial\eta=0,
 \qquad
 C_0\eta=0,                                        \tag{4.8}
\]

where `C_0` is the middle-owner projection.  It is realized by an actual
chronology precisely when additionally

\[
 z_0+\eta\ge0                                     \tag{4.9}
\]

and the resulting support is one Euler component.

Rankwise symmetric two-block exchanges only prove that each proposed row
change lies in the kernel of point incidence.  Proposition 3.2 proves that
this is strictly weaker than membership in the image lattice (4.8).

## 5. Nested endpoints and the sharpened remaining gate

The endpoint types in Theorem 1.1 are not independently selectable across
depths.  In one chronology they are two nested flags:

\[
 P_q=\bigcap_{h=0}^qT_h,
 \qquad
 Q_q=\bigcap_{h=W-q-1}^{W-1}T_h,                  \tag{5.1}
\]

with

\[
 P_{q+1}\subset P_q,
 \qquad
 Q_{q+1}\subset Q_q,
 \qquad
 |P_q|=|Q_q|=r-q.                                 \tag{5.2}
\]

Thus the chronology gate now has three exact stages.

1. **Marginal completion:** choose hole-free `mu_q` with the prescribed
   point degrees.  This is solved by the hypersimplex theorem.
2. **Adjacent Euler feasibility:** for every adjacent pair
   `(mu_q,mu_(q+1))`, choose endpoints belonging to the two flags (5.1)
   and satisfy Theorem 1.1.  The capacitated Hall cuts (2.4) and the
   chronological cuts (3.1) are immediate certificates against a bad
   choice of hypersimplex decomposition.
3. **Common chronology:** satisfy the single boundary-capped flow of
   Theorem 4.1.  Pairwise Euler feasibility is necessary but not sufficient,
   because the Euler order at row `q+1` must literally be the edge-colour
   order induced at row `q`.

For the frozen `k=15` Hall-29 carrier, the earlier theorem proves stage 1
at depths two and three with wide coordinate margins.  It does **not** yet
prove stage 2 for a selected pair of zero-hole completions, and therefore
does not prove stage 3.  The mathematically clean next test is now:

* construct the zero-hole excess designs;
* run the integral half-edge flow (2.1)--(2.3), extracting an explicit
  cut (2.4) if it fails;
* add the subtour constraints if the flow passes; and only then
* solve or prove the common `D_3(15,8)` flow.

The trace-two theorem sharpens the last sentence further.  There is no
independent matching layer once the controller trace word is fixed; the
controller trace word must instead be built into the same chronology.  The
exact combined formulation is recorded next.

## 6. Trace two adds colours to the Euler graph, not another Hall problem

Let a controller skeleton produce a nonempty trace `Q_p` at every source
position.  For a physical cell `c` with source interval `I_c`, put

\[
 \rho_Q(c)=\bigcup_{p\in I_c}Q_p.                 \tag{6.1}
\]

The fixed-skeleton right-degree-one theorem says that a residual target
`S` can use `c` if and only if all base/footprint conditions hold and

\[
                         \rho_Q(c)=S.              \tag{6.2}
\]

In particular two distinct subset targets never compete for one cell.
Consequently, after `Q` is fixed, residual Hall is equivalent to the
singleton coverage conditions

\[
 \#\{c:\ c\text{ is eligible and }\rho_Q(c)=S\}\ge1
 \qquad(S\text{ residual}).                       \tag{6.3}
\]

This observation can be incorporated directly into Theorem 4.1.  Suppose
all physical cell intervals and all controller footprints have span at most
`h`.  Enlarge the de Bruijn state so that, in addition to the safe Johnson
history, it records:

1. the last `h` traces `Q_p`;
2. the at-most-two active controllers generating each of them; and
3. the remaining lifetime of every active controller footprint.

Call the resulting finite digraph `D_(d,h)^dec`.  Delete every local arc
which violates nonemptiness, controller generation, base eligibility, or a
fixed protected equality.  Label every surviving arc by

* its middle owner and all lower/upper flag targets, as in Theorem 4.1; and
* every interval union (6.1) of a physical cell which becomes complete on
  that arc.

### Theorem 6.1 (single decorated-Euler formulation)

For bounded cell span `h`, a two-sided safe chronology together with a
trace-two residual compiler exists if and only if there is a nonnegative
integral boundary flow on `D_(d,h)^dec` such that

1. its positive support is one Euler component;
2. every middle owner has total load one;
3. the required lower and upper flag-colour equations hold; and
4. for every residual target `S`, the total number of eligible completed
   cell labels equal to `S` is at least one.

#### Proof

Any compiled chronology gives its consecutive decorated windows and hence
the stated flow.  Conditions 1--3 are exactly Theorem 4.1 with the local
controller data appended.  Condition 4 is (6.3).

Conversely, Euler's theorem spells the integral flow as one decorated word.
The retained local arcs make its controller skeleton admissible.  Conditions
2--3 give the middle and flag requirements.  Condition 4 gives one eligible
cell for every residual target; cells chosen for distinct targets are
automatically distinct by (6.2).  The fixed-skeleton theorem therefore
supplies the trace-two residual extension without any further Hall choice.
\(\square\)

Thus the final coupling is one ordered `Q`-word/flag-tower construction.
The hierarchy is now:

\[
 \text{hypersimplex marginals}
 \;\longrightarrow\;
 \text{adjacent coloured-Euler cuts}
 \;\longrightarrow\;
 \boxed{\text{one decorated Euler trail}}.
\]

The old owner matching is not a fourth stage.  Its apparent competition
collapses after the trace word is selected.  For the frozen `k=15` H29
instance this also explains the exact `29`-cell tax: the old six cells can
display at most six distinct skeleton-union values, so a successful
decorated chronology must create at least 29 new eligible interval-union
occurrences.

## 7. Reproducible `k=15` adjacent-flow audit

The program

```text
k15_adjacent_euler_flow.cpp
```

implements Lemma 1.1 of the hypersimplex note, then uses symmetric
two-block exchanges to drive each excess design to its floor/ceiling load
profile, and finally runs the exact capacitated flow (2.1)--(2.3).  It reads
the frozen carrier

```text
scratch/k15_doubletrans_05_213_hall29.json
```

and preserves its actual two nested endpoint flags.  Compiled with
`-O3 -DNDEBUG`, deterministic seed zero gives

```text
depth 2:  load 1^3577 2^1428
          hash 5428802374913097295
depth 3:  load 2^2577 3^426
          hash 10140450685199794027

q1 -> q2 half-edge flow: 12866 / 12866
q2 -> q3 half-edge flow: 12864 / 12864

q1 -> q2 support components: 897 -> 1
q2 -> q3 support components: 1150 -> 1

q1 -> q2 verified Euler-trail hash: 7347369576099631482
q2 -> q3 verified Euler-trail hash: 17642377625863709212
```

Thus one explicit pair of hole-free completions clears **every**
capacitated Hall cut (2.4) at both adjacent stages.  The initial max-flows
have respectively 897 and 1150 support components.  Integral residual-cycle
pivots preserve every supply, demand, and capacity while reducing those
counts to one.  Theorem 2.2 then pairs the half-edges, and an independent
Euler traversal verifies the displayed hashes and all vertex/colour
multiplicities.

This is therefore an exact computational certificate for the **full
adjacent coloured-Euler stage**, not merely its fractional or half-edge
projection.  It is still not a proof of the common chronology theorem: the
two Euler trails order the shared depth-two occurrence multiset
independently, whereas one flag tower requires those two orders to be
identical (up to the common boundary convention).

The audited `k=15` frontier is consequently sharper:

* marginal zero-hole feasibility: proved;
* adjacent connected coloured-Euler realizations for one balanced choice:
  certified at both pairs;
* one common decorated Euler trail: open.

## 8. The missing upper colours form one diamond table

The adjacent theorem records intersection colours only.  For the exact
carrier, consecutive row-`q` sets also have prescribed union colours in row
`q-1`.  Both colours are encoded by one Boolean diamond.

Keep the notation of Section 1 and put

\[
 \mathcal U=\binom{[k]}{s+1}.
\]

Every Johnson edge `AB` has

\[
 R=A\cap B\in\mathcal R,
 \qquad
 U=A\cup B\in\mathcal U,                          \tag{8.1}
\]

and is uniquely determined by the flag `R subset U`, `|U-R|=2`: its two
endpoints are the two intermediate `s`-sets.

### Theorem 8.1 (two-sided diamond-Euler criterion)

Let `m_A`, `c_R^-`, and `c_U^+` be prescribed vertex, intersection-colour,
and union-colour multiplicities, with totals `n,n-1,n-1`.  There is a
Johnson walk realizing all three multisets if and only if there are endpoint
numbers `e_A` as in Theorem 1.1 and nonnegative integers

\[
                         y_{R,U}\qquad(R\subset U, |U-R|=2) \tag{8.2}
\]

such that

\[
 \sum_{U\supset R}y_{R,U}=c_R^-,                 \tag{8.3}
\]

\[
 \sum_{R\subset U}y_{R,U}=c_U^+,                 \tag{8.4}
\]

\[
 \sum_{R\subset A\subset U}y_{R,U}=2m_A-e_A,    \tag{8.5}
\]

and the multigraph on the intermediate `s`-sets, containing `y_(R,U)`
copies of the edge determined by the diamond `[R,U]`, is connected.

#### Proof

A walk gives one diamond for every consecutive pair.  Counting its lower
colour, upper colour, and endpoint incidences gives (8.3)--(8.5), and its
edge multigraph is connected.

Conversely, the graph in the statement has exactly the prescribed degrees
and exactly zero or two odd vertices according to `e`.  Euler's theorem
gives a trail.  The unique lower and upper colours of every diamond edge
give (8.3)--(8.4), and the usual degree/end calculation gives vertex
multiplicity `m_A`.  \(\square\)

For `k=15`, apply this theorem first at `s=7`:

* `m_A` is the depth-one multiplicity;
* `c_R^-` is the chosen hole-free depth-two multiplicity; and
* `c_U^+` is one copy of every rank-eight middle owner except the two
  prescribed top endpoints.

Only after this **two-sided** graph is found may one apply the depth-three
transition-system theorem: pair its incident edge copies at each rank-seven
owner so that the intersections of consecutive rank-six edge colours have
the prescribed depth-three loads and the transition graph is one path.
Pair--pair switches in that transition system preserve the graph and hence
all top union colours.

This qualification matters numerically.  The explicit connected
`q1 -> q2` Euler trail of Section 7, built without (8.4), misses 1905 of the
required internal rank-eight owner occurrences and creates 1905 excess
occurrences.  The explicit `q2 -> q3` trail similarly has a 2333-unit
deficit in its required rank-seven union multiset.  These are neither lower
bounds nor obstructions; they demonstrate that the two one-sided Euler
certificates do not accidentally synchronize the upper tower.

The exact finite carrier gate through depth three is therefore:

1. a connected two-sided diamond table (8.2)--(8.5) at depth one;
2. a support-complete local transition system on its edge copies with the
   prescribed depth-three labels; and
3. the controller-trace decoration of Theorem 6.1.

All three are parts of one decorated Euler trail; none is an independent
matching problem.
