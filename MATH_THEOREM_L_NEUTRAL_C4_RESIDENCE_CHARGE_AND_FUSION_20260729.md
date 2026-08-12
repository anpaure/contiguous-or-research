# Neutral Johnson C4 slides: residence charge, port monoid, and the exact fusion gate

Date: 2026-07-29  
Status: general theorems proved; the frozen `L57614` direct slide is
specialized exactly.  A second scalar-neutral slide is certified in the
companion marked-collar theorem.  No rebuilt overlay or residence descent is
claimed.

## 1. Setting

Let `F` be a simple spanning two-factor of the Johnson graph
`J(n,r)`.  For an edge `e=uv`, write

\[
 L(e)=u\cap v,\qquad U(e)=u\cup v.                    \tag{1.1}
\]

The factor is **q1-perfect** if every rank-`r-1` lower colour and every
rank-`r+1` upper colour occurs at least once.  A Johnson C4 switch has four
distinct vertices and the form

\[
 F'=F-\{AB,CD\}+\{AD,BC\},                              \tag{1.2}
\]

where the two new edges are unused Johnson edges.  It automatically
preserves every middle-vertex degree.

For a coordinate `x`, let `V_x={v:x in v}` and let

\[
 I_x(F)=(V_x,\{uv\in F:u,v\in V_x\})                    \tag{1.3}
\]

be the coordinate-internal graph.  It has maximum degree two.

## 2. Intrinsic residence charge

### Theorem 2.1 (small-component form of residence)

The maximal finite runs of coordinate `x` around the factor cycles are in
bijection with the path components of `I_x(F)`.  Run length equals component
order.  A cycle component of `I_x(F)` is precisely a whole factor component
on which `x` is always present and is not counted by the residence audit.
Consequently the exact residence-defect multiset is

\[
 \Gamma(F)=\{(x,C):C\text{ is a path component of }I_x(F),
                         1\le |C|\le3\},                  \tag{2.1}
\]

with multiplicity, and

\[
 D(F)=|\Gamma(F)|.                                       \tag{2.2}
\]

Write `D_x(F)` for the number of members of `Gamma(F)` with first coordinate
`x`, so that `D(F)=sum_x D_x(F)`.

For a charge `(x,C)`, its literal closure consists of the `|C|-1` internal
edges of `C` and the two factor edges from the path endpoints to
`V\setminus V_x` (both incident edges when `|C|=1`).

**Proof.** Intersect a factor cycle with `V_x`.  Each proper nonempty
intersection breaks uniquely into maximal consecutive vertex intervals.
The factor edges internal to each interval form a path, and different
intervals have no internal edge between them.  Conversely every path
component of (1.3) is such an interval.  If every vertex of a factor cycle
lies in `V_x`, its internal graph is that whole cycle.  The short-run audit
counts exactly the proper intervals of orders one, two, and three.  The
closure description is then immediate.  `square`

Thus `(x,C)` is the **intrinsic defect**.  The two zero-side boundary
neighbours are its movable **collar**.  These should not be conflated.

### Theorem 2.2 (exact all-coordinate run-count identity)

Let `R_x(F)` be the number of proper maximal `x`-runs of arbitrary positive
length, equivalently the number of path components of `I_x(F)`.  If
`partial_x F` denotes the factor edges with exactly one endpoint in `V_x`,
then

\[
 R_x(F)=|V_x|-|E(I_x(F))|={1\over2}|\partial_xF|.          \tag{2.3}
\]

Moreover every Johnson two-factor satisfies

\[
                         \boxed{\sum_xR_x(F)=\binom nr}.   \tag{2.4}
\]

In particular every C4 rethread conserves the total number of proper runs,
although it may fuse a run at one coordinate and fission one at another.
For an individual equal-size degree-preserving exchange `E^- -> E^+` whose
endpoint is again a spanning two-factor, the exact derivative is

\[
 \Delta R_x=
 |\{e\in E^-:e\subseteq V_x\}|-|\{e\in E^+:e\subseteq V_x\}|
 ={1\over2}\bigl(|\{e\in E^+:|e\cap V_x|=1\}|
                 -|\{e\in E^-:|e\cap V_x|=1\}|\bigr).    \tag{2.5}
\]

**Proof.** A maximum-degree-two graph has `|V|-|E|` path components; each
cycle component contributes zero to this Euler characteristic.  The two
factor incidences at every vertex of `V_x` give
`2|V_x|=2|E(I_x)|+|partial_x F|`, proving (2.3).  Summed over coordinates,
`sum_x |V_x|=r binom(n,r)`.  Every Johnson edge has intersection size `r-1`,
so it belongs to exactly `r-1` internal graphs.  A spanning two-factor has
`binom(n,r)` edges.  Subtraction proves (2.4).  Taking the difference of
either equality in (2.3) across the exchange proves (2.5). `square`

### Definition 2.3 (pure collar transport)

A switch is a pure transport for coordinate `x` if it leaves the edge set of
`I_x(F)` unchanged.  Equivalently, among the two deleted and two inserted
edges it changes no edge whose two endpoints contain `x`.  It is a strict
residence-charge transport if, in addition,

\[
                         \Gamma(F')=\Gamma(F).             \tag{2.6}
\]

### Corollary 2.4 (charge conservation)

A pure transport for `x` preserves the entire `x`-part of `Gamma`, including
the vertex set and order of every short run.

A chain of strict residence-charge transports preserves every intrinsic
charge `(x,C)`, not only their number.  In particular it cannot coalesce or
annihilate two defects.  A chain whose moves satisfy only

\[
                         D(F_{i+1})=D(F_i).                \tag{2.7}
\]

need not preserve `Gamma`, but it preserves its augmentation `|Gamma|`.
Hence it may erase two named defects only by creating two defect units
elsewhere (with the analogous one-unit statement for coalescence into one
short run).

The distinction is essential: **pure collar slide** is a structural move,
whereas **scalar-neutral slide** means only (2.7).

## 3. Exact finite port monoid

The effect of an arbitrary rethread on residence is local at its ports and
has a constant-state exact calculus.

For a finite binary path word `w`, put

* `A(w)=1` when `w` is all ones;
* `P(w),S(w) in {0,1,2,3,4}`, the initial and terminal one-run lengths,
  capped at four; and
* `I(w)`, the number of one-runs of lengths at most three touching neither
  end of the word.

Let `h(t)=1` for `1<=t<=3` and zero otherwise, and write
`a plus_4 b=min(4,a+b)`.

### Theorem 3.1 (threshold-four segment monoid)

The tuple

\[
                         M(w)=(A(w),P(w),S(w),I(w))         \tag{3.1}
\]

determines `M(uv)` from `M(u),M(v)`.  The boundary update is as follows.
The prefix continues through `u` exactly when `A(u)=1`, the suffix continues
through `v` exactly when `A(v)=1`, and the only possible new internal short
run is the join of `S(u)` and `P(v)`.  More explicitly:

* if `S(u)>0,P(v)=0`, add `h(S(u))` to `I` unless `A(u)=1`;
* if `S(u)=0,P(v)>0`, add `h(P(v))` unless `A(v)=1`;
* if both are positive, add `h(S(u) plus_4 P(v))` exactly when neither word
  is all ones; and
* otherwise add zero.

Together with `I(u)+I(v)` and the prefix/suffix rules, these formulae give
`M(uv)` exactly.  Reversal interchanges `P` and `S`.

For a non-all-one cyclic word, its short-run count is `I` plus

\[
 \begin{cases}
 h(P\mathbin{+_4}S),&P,S>0,\\
 h(P),&P>0=S,\\
 h(S),&S>0=P,\\
 0,&P=S=0.
 \end{cases}                                              \tag{3.2}
\]

For an all-one cyclic word it is zero.

**Proof.** Concatenation changes no run except the suffix run of the first
word and the prefix run of the second.  Whether their union remains an outer
run is exactly the all-one flag.  Lengths at least four are indistinguishable
for the short-run predicate, so capping at four loses no information.  This
gives the listed cases.  Closing the two outer ports gives (3.2). `square`

After cutting the two edges of a C4, summarize the two resulting path words
for each coordinate, reverse a summary when its path is reversed, and apply
the old and new port pairings.  Theorem 3.1 therefore gives the exact
all-coordinate residence derivative of a proposed C4 without scanning the
path interiors again.

When each cut path contains an `x`-zero, there is a simpler formula.  For a
port `p`, let `lambda_x(p)` be the inward consecutive-one length, capped at
four (zero when the port itself is zero).  If `P_0` and `P_1` are the old and
new pairings of the four ports, then

\[
 D_x(F')-D_x(F)=
 \sum_{\{p,q\}\in P_1}h(\lambda_x(p)+_4\lambda_x(q))-
 \sum_{\{p,q\}\in P_0}h(\lambda_x(p)+_4\lambda_x(q)).    \tag{3.3}
\]

Internal runs cancel, proving (3.3).  The monoid version covers the omitted
all-one-path case.

## 4. Q1 surplus is the second conserved ledger

For `sigma in {L,U}`, let `n_F^sigma(c)` be the load of colour `c` and

\[
                         s_F^\sigma(c)=n_F^\sigma(c)-1.     \tag{4.1}
\]

### Lemma 4.1 (exact local q1 test and surplus conservation)

For any equal-size edge exchange `E^- -> E^+`, set

\[
 \delta^\sigma(c)=
 |\{e\in E^+:\sigma(e)=c\}|-|\{e\in E^-:\sigma(e)=c\}|. \tag{4.2}
\]

The exchange is q1-perfect exactly when

\[
                         s_F^\sigma(c)+\delta^\sigma(c)\ge0
 \quad\text{for every }c\text{ and both palettes}.        \tag{4.3}
\]

Moreover

\[
                  \sum_c\delta^L(c)=\sum_c\delta^U(c)=0. \tag{4.4}
\]

Thus a q1-perfect slide transports surplus; it cannot create total surplus.
For every q1-perfect middle factor in `J(2r,r)`,

\[
 \sum_c s_F^L(c)=\sum_c s_F^U(c)
 =\binom{2r}{r}-\binom{2r}{r-1}
 ={1\over r+1}\binom{2r}{r}.                              \tag{4.5}
\]

At `k=16,r=8`, each total is exactly `12870/9=1430`.

**Proof.** Equation (4.3) is the definition of post-trade positive load.
Each deleted or inserted edge contributes once to each palette, proving
(4.4).  Summing `n_F^sigma(c)-1` and using the number of factor edges and
the two palette sizes gives (4.5). `square`

The q1 test therefore involves at most the colours of the two old and two new
edges, namely four old and four new palette-colour occurrences; no global
Hall inference is needed for one fixed C4.

## 5. The exact fusion square

Let `(x,P)` and `(x,Q)` be two distinct intrinsic defects of orders
`a,b<=3`.  Choose endpoints `p in P`, `q in Q` and their factor boundary
edges `pz,qw`, where `z,w` omit `x`.

### Theorem 5.1 (fusion and annihilation criterion)

Assume the four vertices are distinct and `pq,zw` are unused Johnson edges.
Then

\[
 F'=F-\{pz,qw\}+\{pq,zw\}                                \tag{5.1}
\]

is a simple spanning two-factor.  In `I_x`, it replaces the two path
components `P,Q` by the single path component `P union Q`.  Hence

\[
 \Delta_x D={\bf1}_{a+b\le3}-2.                           \tag{5.2}
\]

It coalesces the two defects into one when `a+b<=3`, and annihilates both
when `a+b>=4`.

At the level of runs this fusion always has `Delta_x R=-1`.  Therefore the
universal identity (2.4) forces

\[
                         \sum_{y\ne x}\Delta_yR=1.         \tag{5.3}
\]

Some other coordinate must fission.  Residence descent remains possible
even if that compulsory new run is short: an annihilation removes two defect
units, so one newly short run still leaves a strict net gain.

Conversely, a single C4 which joins two distinct `x`-path components while
deleting no `x`-internal edge must have the form (5.1): its two old edges are
`x`-crossing boundaries and its two new edges are one `11` edge and one
`00` edge.

The fusion is q1-perfect exactly when (4.3) holds.  Its exact global
residence derivative is

\[
 D(F')-D(F)=({\bf1}_{a+b\le3}-2)
             +\sum_{y\ne x}\Delta_yD.                    \tag{5.4}
\]

In particular, an annihilating fusion (`a+b>=4`) is a strict global descent
whenever

\[
                         \sum_{y\ne x}\Delta_yD\le1.       \tag{5.5}
\]

For a coalescing fusion (`a+b<=3`), strict global descent holds exactly when
`sum_(y ne x) Delta_y D <= 0`.

All quantities in (4.3) and (5.4) are literal local ledgers, with (3.1)--
(3.3) providing an exact finite-state computation of the latter.

**Proof.** Degrees are unchanged.  In the coordinate-internal graph, neither
deleted edge is present, `zw` is absent, and `pq` joins endpoints of the two
paths.  This proves the component statement and (5.2).  The converse follows
because joining the components requires a newly inserted `11` edge; with
exactly two `x`-present endpoints, the other new edge is `00` and both old
partners are crossing.  Equation (5.3) follows from Theorem 2.2, and
(4.3)--(5.5) follow from the two exact ledgers. `square`

Therefore neutral routing has a precise constructive role: it may move the
two collars and the q1 surplus until (5.1), (4.3), and the appropriate
descent inequality hold--(5.5) for annihilation, or
`sum_(y ne x) Delta_y D <= 0` for coalescence.  A fusion used as the final
descent must be nonneutral; a scalar-neutral fusion is only another routing
step.  Neutral slides alone cannot lower `D(F)`.

## 6. Alternating-circuit rethreading and cycles

### Theorem 6.1 (endpoint decomposition of every slide chain)

For any chain of two-factors `F_0,...,F_t`, let

\[
 B=F_0\setminus F_t,\qquad R=F_t\setminus F_0.             \tag{6.1}
\]

At every middle vertex,

\[
                         \deg_B(v)=\deg_R(v).              \tag{6.2}
\]

Consequently `B union R` decomposes into closed trails alternating between
old and new edges.  Also, if `chi_F` is the physical edge-incidence vector
and `partial S_i` the signed boundary of the `i`-th C4, then

\[
                 \chi_{F_t}-\chi_{F_0}=\sum_i\partial S_i.\tag{6.3}
\]

A closed walk in the slide-state graph gives an integral relation
`sum partial S_i=0`.  Conversely, an alternating-circuit endpoint exchange
is realizable by C4s only when it admits an ordering whose temporary
diagonals are legal unused Johnson edges and whose intermediate surplus and
residence ledgers meet the desired constraints.  No generic converse is
asserted.

**Proof.** Both endpoint factors have degree two, which gives (6.2).
Pair an old and a new half-edge at every visited vertex and follow the pairs
to obtain alternating closed trails.  Equation (6.3) telescopes. `square`

If every move in the chain is scalar-neutral and q1-perfect, then the scalar
residence objective and total q1 surplus are invariant, while (6.3) is the
exact telescoping edge ledger.  Only a closed state walk makes its right-hand
side zero.  If every move is strict charge transport, `Gamma` is also fixed.
Thus an arbitrarily long
macroscopic rethread assembled only from neutral slides can improve collar
location, component topology, or q1-surplus placement, but cannot improve
the residence objective.  It can only prepare a later nonneutral C4, such as
the fusion square, or a larger compound exchange with a negative aggregate
short-run ledger analogous to (5.4).

## 7. Exact specialization to the frozen L57614 direct slide

Write

\[
 A=56088,\quad B=64024,\quad C=64040,\quad D=64264.
\]

The audited switch deletes `AB,CD` and inserts `AD,BC`.  At coordinate five
(bit `32`) the endpoint bits `(A,B,C,D)` are `(0,0,1,0)`.  Hence no
coordinate-five internal edge changes.  The intrinsic defect is

\[
                         (5,\{64036,64040\}).              \tag{7.1}

Its old collar is

\[
 \{(64036,65028),(64040,64264)\},                         \tag{7.2}
\]

and its new collar is

\[
 \{(64036,65028),(64040,64024)\}.                         \tag{7.3}

Thus the same intrinsic length-two defect survives; only one zero-side
neighbour is transported.  The frozen motif census shows no other short-run
signature change.  Therefore

\[
             \Gamma(F')=\Gamma(F),\qquad D(F')=D(F)=2222.\tag{7.4}

The complete q1-surplus transport is

\[
\begin{array}{c|cc}
 &\text{surplus lost}&\text{surplus gained}\\ \hline
L&L_{55832}&L_{56072}\\
U&U_{64296}&U_{64056}.
\end{array}                                                \tag{7.5}
\]

Each lost colour had load two and each gained colour had load one, so (4.3)
holds with equality at the two donors.

For reference, the four-port bit types also contain a latent fusion/fission
pair: coordinate four has pattern `1100` (old `11+00`, new two crossings),
while coordinate eight has pattern `1001` (old two crossings, new `11+00`).
The exact run ledger is

\[
                         \Delta R_4=1,\qquad
                         \Delta R_8=-1,                    \tag{7.6}
\]

with every other `Delta R_x=0`.  The exact charge audit nevertheless gives
`Gamma(F')=Gamma(F)`: the compulsory fission and fusion concern long runs,
not short ones.  This demonstrates why endpoint bit type alone is
insufficient; the capped port lengths in Theorem 3.1 are decisive.

The direct slide is therefore a strict residence-charge transport and a
one-unit q1-surplus transport in each palette.  Any chain staying in this
strict class can move the collar of (7.1) and its provider currency, but the
intrinsic charge (7.1) itself is fixed and cannot be discharged.  A genuine
residence-descent step must be nonneutral.  Theorem 5.1 gives one exact
option; another C4 geometry or a compound exchange would need its own
negative aggregate short-run ledger.

The companion exact collar audit continues this move once more.  That second
move remains scalar-neutral but is not a strict all-coordinate charge
transport: it replaces a coordinate-four length-one charge by a
coordinate-ten length-three charge while preserving (7.1).  This is fully
consistent with Corollary 2.4 and illustrates why scalar neutrality cannot be
silently upgraded to conservation of `Gamma`.

## 8. Proved boundary

Proved here:

* residence defects are exactly the small path components (2.1);
* the threshold-four port monoid gives the exact local derivative;
* q1 surplus has the exact local test (4.3) and fixed k16 total `1430` per
  palette;
* strict collar transport preserves intrinsic charges, while scalar
  neutrality preserves only their total number;
* (5.1)--(5.5) are exact sufficient conditions for two-boundary fusion, and
  (5.1) is locally necessary for a C4 which joins two distinct
  `x`-components while deleting no `x`-internal edge; and
* every slide chain has the alternating-circuit endpoint decomposition.

False in general:

* a q1-perfect scalar-neutral C4 need not be a strict charge transport.  The
  frozen `S4 -> S10` slide in the companion audit is an explicit example: it
  replaces a coordinate-four singleton defect by a coordinate-ten
  length-three defect while leaving the total unchanged.

Not proved:

* the k16 factor has a second defect routable to (7.1) through legal neutral
  slides;
* a q1-perfect fusion satisfying (5.5) exists; or
* a neutral-slide macro rethread preserves deeper shadows or makes the fixed
  red/blue overlay feasible.

The k16 numerical and literal claims in Section 7 use only the frozen
provider/Farkas and C4 materialization audits:

```text
scratch/k16_motif820_l57614_active_colour_c4_20260729.audit.json
scratch/k16_l57614_motif820_c4_materialization_20260729.audit.json
scratch/k16_l57614_motif820_escape_direct_slide_20260729.json
scratch/audit_k16_l57614_direct_slide_charge_20260729.py
scratch/k16_l57614_direct_slide_charge_20260729.audit.json
scratch/audit_k16_l57614_neutral_collar_slide_graph_20260729.py
scratch/k16_l57614_neutral_collar_slide_graph_20260729.audit.json
```
