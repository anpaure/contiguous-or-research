# The exact nine-cycle coloured-seam master and cut-kernel reduction

## 0. Current endpoint and claim boundary

Fix the independently audited `k=15` factor

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/u2u3l3_s801.engine.json
SHA-256 886877094a3eaba8950136728d131782141a4b6f882d570ecb3791827da98f83
```

It is a lower-`q1`-rainbow Johnson `2`-factor on all `W=6435` rank-eight
owners, with nine physical cycles of lengths

```text
1890, 774, 774, 774, 774, 774, 555, 75, 45.
```

It has minimum coordinate residence four and complete audited lower and
upper trace decks through every required depth.  The only factor-level gate
is connectivity.  Opening one edge in each cycle and adding eight seams
would give a spanning path, but only if the eight seams

* recycle eight of the nine deleted lower-`q1` colours;
* introduce no residence defect;
* do not destroy the last occurrence of any required lower or upper target.

This note gives a necessary-and-sufficient finite master for precisely that
problem.  Its fixed-width version is a literal zero-one flow/common-base
system.  An extended occurrence version is exact for unrestricted interval
semantics as well.  The lower compiler/Hall condition remains a separate
set of rows and is not implied here.

## 1. Ports, cut colours, and seam donors

Let `G=J(15,8)`.  A Johnson edge `AB` has lower colour

\[
 \kappa(AB)=A\cap B\in\binom{[15]}7.                 \tag{1.1}
\]

Every edge of colour `S` is

\[
 \{S+a,S+b\},\qquad a,b\notin S,\quad a\ne b.        \tag{1.2}
\]

Write the nine factor cycles as `C_0,...,C_8`.  A **port state** `p` on
`C_i` consists of a cut edge `e(p)` and an orientation of `C_i-e(p)`.  Write
the resulting path as

\[
 P(p)=(h(p),\ldots,t(p)),                             \tag{1.3}
\]

where `h(p)` and `t(p)` are its head and tail ports, and put

\[
 \lambda(p)=\kappa(e(p)).                             \tag{1.4}
\]

Both ports contain `lambda(p)`.  Reversal exchanges the ports and preserves
the cut colour.  Since the original factor is lower-rainbow, cut edges on
different cycles always have different colours.

For states `p` on `C_i` and `q` on `C_j`, `i\ne j`, a directed seam

\[
 \alpha:p\longrightarrow q                           \tag{1.5}
\]

exists when `t(p)h(q)` is a Johnson edge.  Its seam colour is

\[
 \mu(\alpha)=t(p)\cap h(q).                           \tag{1.6}
\]

A selected cut state `d` is a **donor** for `alpha` when

\[
 \lambda(d)=\mu(\alpha).                              \tag{1.7}
\]

The donor need not be the source or target state.  Two useful local
subfamilies are

\[
\begin{array}{lll}
\text{source-pays:}&\mu(\alpha)=\lambda(p),
 &\lambda(p)\subset h(q),\\
\text{child-pays:}&\mu(\alpha)=\lambda(q),
 &\lambda(q)\subset t(p).
\end{array}                                           \tag{1.8}
\]

The containments in (1.8) are equivalent to the colour equalities because
the two seam endpoints are distinct rank-eight sets.

## 2. Why a pairwise exact two-switch cannot work

### Theorem 2.1 (two-edge lower-palette rigidity)

Take one edge of lower colour `S` from one factor cycle and one edge of
lower colour `T` from a vertex-disjoint factor cycle.  There is no
nontrivial `2`-switch on their four endpoints whose two new Johnson edges
have lower-colour multiset `{S,T}`.

#### Proof

Let the old edges be `x_0x_1` of colour `S` and `y_0y_1` of colour `T`.
The four vertices are distinct, and `S\ne T` by lower rainbowness.  In a
nontrivial cross matching, relabel so that `x_0y_0` has colour `S` and
`x_1y_1` has colour `T`.

Then `y_0` contains `S` because the new edge has intersection `S`, and it
contains `T` because it was an endpoint of the old `T`-edge.  Similarly
`x_1` contains both `S` and `T`.  Distinct `(r-1)`-sets contained in an
`r`-set have union of size exactly `r`; hence

\[
 y_0=S\cup T=x_1,
\]

contrary to vertex-disjointness.  The other cross pairing is the same after
renaming.  \(\square\)

Thus eight individually palette-neutral cycle-fusing `2`-switches are
intrinsically impossible.  The viable architecture cuts all nine cycles,
adds only eight connectors, and deliberately leaves one cut colour absent
at the boundary of the final path.

## 3. The exact topology and donor master

For each cycle `C_i`, let `mathcal P_i` be any finite catalogue of permitted
port states.  It may already exclude states failing terminal pins or a
chosen cut-protection test.  Let `mathcal A` be the finite catalogue of
directed Johnson seams between states on different cycles.

Use binary variables

\[
 z_p\quad(p\in\mathcal P_i),\qquad
 x_\alpha\quad(\alpha\in\mathcal A),                 \tag{3.1}
\]

and donor variables

\[
 d_{\alpha p}\quad
 (\alpha\in\mathcal A, p\in\cup_i\mathcal P_i,
   \ \mu(\alpha)=\lambda(p)).                         \tag{3.2}
\]

The **nine-cycle seam master** consists first of the following rows.

### State and incidence rows

\[
 \sum_{p\in\mathcal P_i}z_p=1\qquad(i=0,\ldots,8),   \tag{3.3}
\]

and, for every arc `alpha:p -> q`,

\[
 x_\alpha\le z_p,\qquad x_\alpha\le z_q.             \tag{3.4}
\]

At every selected state there is at most one incoming and one outgoing
seam:

\[
 \sum_{\alpha:\,\operatorname{head}(\alpha)=p}x_\alpha\le z_p,
 \qquad
 \sum_{\alpha:\,\operatorname{tail}(\alpha)=p}x_\alpha\le z_p. \tag{3.5}
\]

There are exactly eight seams,

\[
 \sum_{\alpha\in\mathcal A}x_\alpha=8,               \tag{3.6}
\]

and their component projection is acyclic:

\[
 \sum_{\substack{\alpha:i\to j\\i,j\in Q}}x_\alpha
 \le |Q|-1
 \qquad(\varnothing\ne Q\subseteq\{0,\ldots,8\}).  \tag{3.7}
\]

### Donor/SDR rows

Every selected seam receives one selected donor,

\[
 \sum_{p:\lambda(p)=\mu(\alpha)}d_{\alpha p}=x_\alpha, \tag{3.8}
\]

and no selected cut state is donated twice:

\[
 \sum_\alpha d_{\alpha p}\le z_p,
 \qquad d_{\alpha p}\le z_p.                         \tag{3.9}
\]

Since there are nine selected cut states and eight seams, these rows leave
exactly one selected cut colour unused.

It is useful to expose that colour by the binary identity

\[
 u_p=z_p-\sum_\alpha d_{\alpha p}.                    \tag{3.10}
\]

Exactly one `u_p` equals one.  This is the missing boundary lower colour;
it is not enough merely to know that some colour is missing.

### Theorem 3.1 (topology and palette equivalence)

Rows (3.3)--(3.9) are feasible if and only if one can choose and orient one
cut per physical cycle and concatenate the nine resulting paths by eight
Johnson seams into one spanning path whose lower colours are precisely all
old lower colours except one.

#### Proof

Suppose the rows are feasible.  By (3.6)--(3.7), the component projection
is a forest with eight edges on nine vertices, hence a spanning tree.
Rows (3.4)--(3.5) give indegree and outdegree at most one at every component
and force both incident seams of an internal component to use its same
selected state.  Therefore the tree has maximum undirected degree two and
is consistently oriented: it is a directed Hamilton path through the nine
oriented component segments.

Cutting deletes nine pairwise distinct lower colours.  By (3.8), every seam
uses a selected cut colour.  By (3.9), the eight seam colours are distinct.
Thus eight deleted colours are restored and exactly one is absent.

Conversely, a palette-exact concatenation selects one state per component
and eight seams forming a directed spanning path, giving (3.3)--(3.7).
Match every seam to the unique selected cut edge having its lower colour.
This is an injective donor assignment and gives (3.8)--(3.9).  \(\square\)

### Corollary 3.2 (boundary-port SDR)

Let

\[
 \rho_q=z_q-\sum_{\alpha:\operatorname{head}(\alpha)=q}x_\alpha,
 \qquad
 \tau_q=z_q-\sum_{\alpha:\operatorname{tail}(\alpha)=q}x_\alpha           \tag{3.11}
\]

mark the initial and terminal states of the component path.  For the usual
rank-seven boundary port, an unused donor `p` is left-eligible at initial
state `q` when

\[
 \lambda(p)\subset h(q),                              \tag{3.12}
\]

and right-eligible at terminal state `q` when

\[
 \lambda(p)\subset t(q).                              \tag{3.13}
\]

Introduce boundary assignment variables `b^L_(pq),b^R_(pq)` only for
eligible pairs, and impose

\[
\begin{aligned}
 &\sum_{p,q}(b^L_{pq}+b^R_{pq})=1,\\
 &b^L_{pq}\le u_p,\quad b^L_{pq}\le\rho_q,\\
 &b^R_{pq}\le u_p,\quad b^R_{pq}\le\tau_q.           \tag{3.14}
\end{aligned}
\]

Rows (3.14) are necessary and sufficient for the one missing lower colour
to have a literal boundary port.  They are the one-item instance of the
general boundary SDR: with several special cells, join each cell to its
eligible endpoint occurrence and impose the usual matching/Hall rows.

More explicitly, the eight recycled colours already occupy eight distinct
seam cells.  Only the unused colour `R` has no seam cell.  Necessity of
boundary eligibility is immediate.  If `R` is eligible at either global
boundary, assign it there; the other boundary is spare, so this extends the
forced eight seam assignments to the complete special-cell SDR.  Hence, in
the exact eight-distinct-donor setting, the full rank-seven special-cell
Hall test reduces to this single endpoint-containment test.

This condition is strictly stronger than a lower-rank or unconditioned Hall
score.  A path can recycle eight colours perfectly and have base Hall
deficiency zero while its unique unused colour is contained in neither
endpoint.

### Corollary 3.3 (fixed-port common-matroid form)

After fixing one state on each cycle, restrict the seam ground set to seams
whose colours lie among the nine cut colours.  Define:

* the graphic matroid on the underlying component pairs;
* the tail partition matroid, capacity one at each component;
* the head partition matroid, capacity one at each component;
* the colour partition matroid, capacity one at each cut colour.

A palette-exact spanning path exists exactly when these four matroids have a
common independent set of size eight.

This is a common-base characterization, not ordinary two-matroid
intersection.  Tail, head, colour, and connectivity cannot in general be
certified by one scalar Hall inequality.

### Corollary 3.4 (child-pays flow form)

Restrict to seams `p -> q` satisfying

\[
 \mu(p\to q)=\lambda(q).                              \tag{3.15}
\]

Then every noninitial component automatically donates its own cut colour,
so the donor rows are redundant.  For fixed states and a prescribed initial
component `r`, feasibility is exactly the zero-one system

\[
\begin{aligned}
 &\sum_i x_{ij}=1 &&(j\ne r),\\
 &\sum_i x_{ir}=0,\\
 &\sum_j x_{ij}\le1 &&(i=0,\ldots,8),                \tag{3.16}\\
 &\sum_{i,j\in Q}x_{ij}\le |Q|-1
   &&(\varnothing\ne Q\subseteq[9]\setminus\{r\}).
\end{aligned}
\]

The first three lines alone are a bipartite predecessor matching; Hall's
condition is necessary and sufficient for that relaxation.  It can leave a
rooted path plus disjoint directed cycles.  The last line is the exact
subtour/arborescence condition which turns it into a Hamilton path.  Thus
the child-pays restriction is the cleanest finite flow submodel, but it is
only sufficient for the unrestricted donor problem.

### Corollary 3.5 (source/target donor phase law)

Fix an ordered path of selected states

\[
 p_1\longrightarrow p_2\longrightarrow\cdots
 \longrightarrow p_9,                               \tag{3.17}
\]

and suppose every seam colour is required to equal the cut colour of one
of its two endpoint states.  Then the eight seams recycle eight distinct
cut colours if and only if there is a unique `r\in\{1,\ldots,9\}` such that

\[
\begin{cases}
 \mu(p_i\to p_{i+1})=\lambda(p_i),&i<r,\\
 \mu(p_i\to p_{i+1})=\lambda(p_{i+1}),&i\ge r.
\end{cases}                                           \tag{3.18}
\]

The unique unused cut colour is `lambda(p_r)`.  Thus every exact
source-or-target donor word is a block of source payments followed by a
block of target payments; a target-to-source reversal is impossible.

#### Proof

View seam `i` as an edge of the ordinary nine-vertex path and assign it to
the endpoint whose cut colour it uses.  Exact recycling is a matching of
the eight path edges to eight of the nine path vertices.  Let `p_r` be the
unmatched vertex.

Starting at the left endpoint, seam one must be assigned to `p_1` unless
`r=1`.  Inductively, every seam strictly left of `r` must be assigned to its
left/source endpoint, since its right endpoint must remain available for
the next seam.  Starting at the right endpoint gives the dual conclusion:
every seam at or right of `r` must be assigned to its right/target endpoint.
This proves necessity and uniqueness.  The pattern in (3.18) visibly uses
every cut colour except `lambda(p_r)` exactly once, proving sufficiency.
\(\square\)

The all-target child-pays model is the case `r=1`; the all-source model is
the case `r=9`.  Hence the full source-or-target library enlarges the child
model by only eight possible phase locations once the component/state order
is fixed.

## 4. Exact residence rows

For an oriented Johnson step `e:A -> B`, write

\[
 \operatorname{ins}(e)=B\setminus A,
 \qquad
 \operatorname{del}(e)=A\setminus B.                 \tag{4.1}
\]

At a seam let `e_0` be the connector, let `e_{-3},e_{-2},e_{-1}` be the
last three old steps on its left, and let `e_1,e_2,e_3` be the first three
old steps on its right.  Because every old cyclic run has length at least
four, the seam creates a short positive run if and only if

\[
 \operatorname{ins}(e_i)=\operatorname{del}(e_j)     \tag{4.2}
\]

for one of

\[
 (-3,0),(-2,0),(-2,1),(-1,0),(-1,1),(-1,2),
 (0,1),(0,2),(0,3).                                  \tag{4.3}
\]

Indeed an insertion at `e_i` followed by deletion at `e_j` creates a
one-run of length `j-i`; (4.3) is exactly the set of newly created pairs
with `1<=j-i<=3` and with the new seam between them.

Consequently the exact internal residence constraint is simply

\[
 x_\alpha=0                                           \tag{4.4}
\]

for every seam candidate violating one of the nine tests (4.2).  Reversing
a component is harmless in its interior and is handled by recomputing
`ins,del` on its oriented collar.  Initial and terminal port states require
the corresponding one-sided boundary test under the boundary convention of
the compiler; introduce root/terminal indicators

\[
 \rho_p=z_p-\sum_{\alpha:\operatorname{head}(\alpha)=p}x_\alpha,
 \qquad
 \tau_p=z_p-\sum_{\alpha:\operatorname{tail}(\alpha)=p}x_\alpha           \tag{4.5}
\]

and forbid `rho_p=1` or `tau_p=1` at an ineligible terminal state.  With
those boundary rows, (4.4) is necessary and sufficient for residence four
of the final path.

## 5. Exact fixed-window shadow rows

For a sign `epsilon in {-,+}` and depth `q`, define the trace of a
`q`-edge, `q+1`-owner window by

\[
 \Phi_q^-(T_0,\ldots,T_q)=\bigcap_{h=0}^qT_h,
 \qquad
 \Phi_q^+(T_0,\ldots,T_q)=\bigcup_{h=0}^qT_h.         \tag{5.1}
\]

For each physical target `Z`, let

* `L_{epsilon,q,Z}` be its load in the old nine-cycle factor;
* `D_{p,epsilon,q,Z}` be the number of old cyclic `q`-windows for `Z`
  destroyed by choosing cut state `p`;
* `G_{alpha,epsilon,q,Z}` be the number of new `q`-windows for `Z` crossing
  seam `alpha`.

Every component has at least `45` owners and `q<=7`.  Hence no such window
crosses two new seams.  The new load is exactly

\[
 L'_{\epsilon,q,Z}
 =L_{\epsilon,q,Z}
  -\sum_pD_{p,\epsilon,q,Z}z_p
  +\sum_\alpha G_{\alpha,\epsilon,q,Z}x_\alpha.       \tag{5.2}
\]

### Theorem 5.1 (last-witness preservation)

For the fixed-width trace semantics, rows

\[
 L_{\epsilon,q,Z}
 -\sum_pD_{p,\epsilon,q,Z}z_p
 +\sum_\alpha G_{\alpha,\epsilon,q,Z}x_\alpha
 \ge1                                                 \tag{5.3}
\]

for every required physical target are necessary and sufficient for the
spliced path to preserve the complete deck.

#### Proof

Every old window either avoids its selected cut and remains verbatim in one
component segment, or crosses that cut and disappears.  Every new window
not of the first kind crosses one unique selected seam.  These three
classes are disjoint and exhaustive, giving (5.2).  Coverage is exactly
positivity of every resulting load.  \(\square\)

This is the precise meaning of "lost last witnesses versus new seam
windows."  A cut is harmless when other old occurrences leave the first
two terms positive.  A seam need pay only rows driven to zero by the chosen
cut set; there is no requirement to preserve the complete load histogram.

## 6. Cut kernels and the exact row reduction

For a target `Z` and a factor cycle `C`, let `mathcal W_C^q(Z)` be all its
old fixed `q`-windows witnessing `Z`.  Define the cut kernel

\[
 K_C^q(Z)=\bigcap_{W\in\mathcal W_C^q(Z)}E(W)          \tag{6.1}
\]

when the support family is nonempty.

### Lemma 6.1 (cut-kernel criterion)

A specified one-cut-per-cycle selection destroys every old fixed-`q`
witness of `Z` if and only if, for every cycle `C` supporting `Z`, its cut
edge lies in `K_C^q(Z)`.  In particular, `Z` survives every nine-cut
selection if at least one supporting cycle has empty cut kernel.

#### Proof

The cut on `C` destroys every supporting window there exactly when that one
edge belongs to every member of `mathcal W_C^q(Z)`, which is precisely
membership in (6.1).  All global witnesses are destroyed exactly when this
happens on every supporting cycle.  \(\square\)

Thus only targets with nonempty kernels on all their supporting cycles need
active restoration rows.  The exact physical census for the retained
factor, written `robust / potentially killable`, is

\[
\begin{array}{c|rrrrrrrrrrrrrr}
 &L1&U1&L2&U2&L3&U3&L4&U4&L5&U5&L6&U6&L7&U7\\ \hline
\text{robust}
 &0&460&265&573&723&600&780&395&425&105&105&15&15&1\\
\text{killable}
 &6435&4545&4740&2430&2280&765&585&60&30&0&0&0&0&0.
\end{array}                                           \tag{6.2}
\]

In particular, no upper row at depth at least five and no row on either
shore at depth at least six can become a hole merely by one cut in each
cycle.  Lower fixed windows through depth four are genuine geodesic windows
under residence four; at depth five the source has `5040` valid lower
windows, so that rank is the first lower filter requiring separate care.

## 7. Unrestricted-interval exactness

For upper depths `q>=3`, the literal graded evaluator may accept a longer
interval whose union is the target, not only a geodesic `q`-edge window.
Therefore (5.3) is an exact necessary-and-sufficient theorem for the stated
fixed-window deck and a sufficient preservation theorem for unrestricted
coverage, but it is not by itself necessary for the latter.

There is nevertheless an exact finite extension.  Enumerate every possible
new interval by

* its initial state and offset;
* the directed chain of seam arcs it traverses;
* its terminal state and offset.

For such an interval `I`, introduce `h_I` and impose the standard AND rows

\[
 h_I\le x_\alpha\quad(\alpha\in I),
 \qquad
 h_I\ge 1-|A(I)|+\sum_{\alpha\in A(I)}x_\alpha.       \tag{7.1}
\]

State links are added at the two ends when the interval contains no seam.
Its union/intersection is known from the literal owner sequence.  For every
target, sum the surviving old-interval indicators and all new `h_I` having
that trace, and require the sum to be at least one.  These rows are finite
and are necessary and sufficient for the unrestricted interval semantics.

Because there are only nine components, this extension has bounded chain
depth eight.  It may be large, but it contains no logical relaxation.  A
search using only (5.3) is a proof-safe stronger subproblem; a negative
result for that subproblem is not a no-go for unrestricted upper coverage.

## 8. Complete theorem and remaining gate

### Theorem 8.1 (nine-cut/eight-seam equivalence)

The retained nine-cycle factor admits a literal spanning path which

1. uses every middle owner once;
2. is Johnson-adjacent at all eight seams;
3. has the complete lower-`q1` palette minus one boundary colour;
4. has residence at least four, under the declared boundary convention;
5. preserves every required fixed-width lower and upper target;

if and only if the binary system (3.3)--(3.9), the residence rows
(4.4)--(4.5), and the last-witness rows (5.3) is feasible.

Replacing (5.3) by the full interval rows of Section 7 gives the analogous
necessary-and-sufficient statement for unrestricted trace semantics.
Adding (3.14) is necessary and sufficient for the unique absent lower
colour to occupy an eligible left or right boundary port.  This still does
not replace the remaining multi-rank/common-`Q` compiler Hall rows.

#### Proof

Theorem 3.1 is necessary and sufficient for the physical path and exact
lower palette.  Section 4 is the exact local residence characterization,
because reversal preserves each segment interior and every new bad run must
meet one seam or a final endpoint.  Theorem 5.1 gives exact fixed-window
coverage.  The three ledgers concern the same selected states and seams, so
their conjunction is both necessary and sufficient.  Section 7 supplies
the same occurrence partition for the unrestricted semantics.  \(\square\)

The remaining finite question is therefore not generic connectivity.  It
is feasibility of one common state/seam selection simultaneously satisfying

```text
graphic path + tail/head ports + lower-colour donor SDR
+ residence collars + last-witness rows
+ the separate lower compiler/Hall rows.
```

The child-pays flow (3.15)--(3.16) is the clean first exact submodel.  Failure
there would not exclude source-pays, third-component donors, or the full
unrestricted-interval master.

## 9. Exact finite calibration and the current obstruction

The frozen physical catalogue for the retained factor has

```text
oriented cut states                              12,870
raw source-donor seam arcs                      129,720
raw quotient-loop rows                              30
residence-safe source-donor arcs                 48,075
residence-safe quotient-loop rows                    15
residence-safe source-or-target donor library    96,150.
```

Here **source-donor** means that the new seam intersection equals the
source/tail state's cut colour; it is the `source-pays` case of (1.8).

An independently replayed eight-seam chain uses the ordered port states

```text
(component, cut, reverse)
(7,34,0), (3,128,1), (8,20,1), (0,412,1), (5,281,1),
(6,145,1), (2,531,1), (1,395,0), (4,376,0).
```

Its middle path has SHA-256

```text
7290ed7b5404c062a3c147dbbd9e8144754a7b19d6001a2398cc5375694f0a07.
```

The literal replay proves:

* all `6,435` middle owners are distinct and all eight seams are Johnson
  edges;
* residence has zero violations;
* upper `q1,q2`, lower `q3,...,q7`, and upper `q4,...,q7` remain complete;
* the only nonboundary shadow holes are lower-`q2` mask `5516` and
  upper-`q3` mask `15326`; the latter is missing under both fixed-width and
  unrestricted-interval audits;
* the eight seam colours recycle eight distinct cuts, leaving cut colour
  `13708` unused.

Its donor word is one source payment followed by seven target payments, so
Corollary 3.5 forces the unused colour to be the second state's cut colour,
namely `13708`.  The D-round-001 chain is the all-target phase `r=1`.

However, the global endpoints are `7628` and `10062`, and

\[
 13708\not\subset 7628,
 \qquad
 13708\not\subset 10062.                              \tag{9.1}
\]

Thus Corollary 3.2 gives rank-seven special-cell SDR deficiency exactly
one.  The lower-rank diagnostic matching is `4943/4943`, but that statistic
does not override the endpoint-conditioned failure.  This chain is a
resident near-all-depth path, not a compiler-ready chronology.

For comparison, the independently retained D-round-001 chain leaves cut
colour `7498`, which is left-boundary eligible and therefore passes the
rank-seven special-cell SDR, but its fixed-window ledger has lower hole
counts `(1,6,0,0,0,0,0)` and upper hole counts `(1,1,1,0,0,0,0)` over
depths one through seven.  The two examples isolate the live simultaneous
gate: boundary eligibility and last-witness preservation have each been
achieved, but not yet in the same eight-seam path.

Frozen independent replay:

```text
scratch/audit_k15_u2u3l3_eight_seam_chain_20260729.py
  SHA-256 d0a161bab9a6c0df162daed0c40440b7f4ce7a5d7ccbe18a6f9636fc37f70b45
scratch/k15_u2u3l3_eight_seam_chain_7290ed_20260729.audit.json
  SHA-256 5e9a0e189d7a736af2d17c47b317af2afa3e15515e2ff8218030ada90fd440bf
scratch/k15_fixed_matching_pbbs_resident_20260729/
  u2u3l3_endgame.audit.round001.chronology.json
  SHA-256 dc39bfd9377a2d806d50c84f941b0e943f0dc2742000864dec9659713085c3e1
```

These are positive certificates for their stated rows and exact
counterexamples to any claim that unconditioned Hall or near-complete
shadow counts alone imply compiler readiness.  They are not a global
nonexistence result for the master of Theorem 8.1.
