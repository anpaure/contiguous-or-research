# Ordered two-corridor zero surplus and the history-star gate

**Date:** 2026-08-02  
**Lane:** A, the live common-history table after item 2649A  
**Status:** Sections 1--6 give the audited zero-surplus/history-state results.
The appended Sections 7--8 are a superseded draft and must not be cited; the
correct partition-Hamilton formulation is in
`MATH_THEOREM_A_ORDER_FREE_PARTITION_HAMILTON_AND_PULL_TREE_GATE_20260802.md`.

## 0. Verdict

The proposed proof order

\[
 \text{fix two forward orders}
 \longrightarrow
 \text{prove robust Hall surplus}
 \longrightarrow
 \text{delete history/bank options}                  \tag{0.1}
\]

cannot work.  Every raw-Hall-feasible fixed nontrivial forward corridor has
raw Hall surplus zero on a nested family of suffix shores.  More strongly,
its perfect
matching is forced at the endpoint-pair level: it uses every consecutive
pair in the chosen order.  Thus common history is not a small perturbation
of a robust ordered matching.  It is the predicate which decides whether
the proposed order is a legal path at all.

For two corridors the endpoint-pair criterion is consequently cellwise.  If
`C_(a,i)` is the parallel literal option cell between consecutive fragments
`v_(a,i),v_(a,i+1)`, then the filtered endpoint projection is feasible if
and only if

\[
                         C_{a,i}\setminus F\ne\varnothing
                         \quad\hbox{for all }a,i.       \tag{0.2}
\]

No aggregate option-load inequality which still permits one completely dead
cell can replace (0.2).  (A sufficiently strong total-loss bound can of
course imply every cell survives.)  Complete occurrence and charge rows add
one residual product-selection constraint across these cells; individual
nonemptiness is sufficient only on a cell-separable compiled face.

Kruskal--Katona and the new residual Ore--Ryser curvature theorem do give a
genuine robust theorem on the **marginal adjacent-rank owner/facet graph**.
They do not apply to the ordered fragment table: contraction, endpoint-state
selection, two role blocks, and forward orders have already changed its
shores and made every suffix tight.

The correct positive object is therefore chosen in the reverse order:

\[
 \text{find two owner-transversal paths in the accepted bi-history graph}
 \longrightarrow
 \text{read their two orders}.                         \tag{0.3}
\]

Section 6 proves that the full coherent bi-history state graph is regular of
degree `(m-d)(m-d-1)`.  The remaining correlation is selecting exactly one
state per physical owner, together with exact palettes and the protected
endpoints.

## 1. Forward ordered blocks

Fix one role block

\[
 V=(v_1\prec v_2\prec\cdots\prec v_s),               \tag{1.1}
\]

with root `v_1` and sink `v_s`.  Its left shore is

\[
 L=\{v_1^{\rm tail},\ldots,v_{s-1}^{\rm tail}\},
\]

and its right shore is

\[
 R=\{v_2^{\rm head},\ldots,v_s^{\rm head}\}.
\]

The raw table may have parallel literal options, but an endpoint pair
`v_i^tail v_j^head` occurs only when `i<j`.

### Theorem 1.1 (triangular rigidity)

Every perfect matching of the raw forward table projects to the consecutive
endpoint pairs

\[
                        v_i\longrightarrow v_{i+1}
                        \qquad(1\le i<s).              \tag{1.2}
\]

For every suffix shore

\[
 S_i=\{v_i^{\rm tail},\ldots,v_{s-1}^{\rm tail}\},   \tag{1.3}
\]

raw Hall, if true, forces

\[
 N_0(S_i)=\{v_{i+1}^{\rm head},\ldots,v_s^{\rm head}\},
 \qquad
 \kappa_0(S_i)=|N_0(S_i)|-|S_i|=0.                   \tag{1.4}
\]

#### Proof

Index the head `v_(j+1)` by column `j`.  Every allowed endpoint cell in row
`i` satisfies `j>=i`.  A perfect matching gives a permutation `pi` with
`pi(i)>=i` for every `i`.  Since

\[
                         \sum_i\pi(i)=\sum_i i,
\]

equality holds coordinatewise, proving (1.2).  Forwardness gives

\[
 N_0(S_i)\subseteq
       \{v_{i+1}^{\rm head},\ldots,v_s^{\rm head}\}.
\]

The two sets have the same cardinality.  Hall forces equality and hence
(1.4). \(\square\)

The two-root/two-sink table of item 2649A is block diagonal, so its endpoint
matching is the Cartesian product of the two forced matchings in (1.2).

## 2. Exact filtered criterion

Let

\[
 C_{a,i}=E_0(v_{a,i}^{\rm tail},v_{a,i+1}^{\rm head}) 
                                                               \tag{2.1}
\]

be the parallel literal options in the forced consecutive cell of block
`a in {1,2}`.  Let `F` contain every option rejected by a common endpoint
history or by a zero-residual occurrence resource.

### Theorem 2.1 (cellwise endpoint criterion and exact product master)

The filtered endpoint-pair table has a perfect matching if and only if

\[
                  C_{a,i}\setminus F\ne\varnothing
                  \qquad(a\in\{1,2\},\ 1\le i<s_a).   \tag{2.2}
\]

Let `P` be the Cartesian product of the surviving cells in (2.2).  The full
literal corridor exists if and only if `P` contains a selection
`(e_(a,i))` satisfying every shared occurrence and charge row.  In
particular (2.2) is sufficient for the full corridor only when those
cross-cell rows have already been compiled into a **cell-separable** face on
which every member of `P` is legal.

#### Proof

Necessity follows from Theorem 1.1.  For sufficiency, choose one surviving
literal option from each forced cell.  These cells have pairwise distinct
tail and head roles and hence form the endpoint perfect matching.  The same
forced-pair theorem shows that any full literal solution is exactly one such
product selection.  Intersecting the product with the resource/charge master
proves the remaining assertions. \(\square\)

Write `m_(a,i)=|C_(a,i)|`, let `H_(a,i)` count the options rejected by the
common histories, and let `Lambda_(a,i)(q)` count the options killed by a
zero-residual occurrence `q`.  The sharp union-bound sufficient row for the
endpoint projection is

\[
       H_{a,i}+\sum_q\Lambda_{a,i}(q)<m_{a,i}
       \qquad\hbox{for every }a,i.                    \tag{2.3}
\]

If one whole cell dies, the head `v_(a,i+1)` is completely destroyed from
the suffix shore `S_(a,i)`, while that shore has zero raw slack by (1.4).
This proves that an averaged row which permits one complete cell loss cannot
replace (2.3).  Aggregate bounds remain useful only when they imply the
worst-cell inequalities themselves.

## 3. Minimal physical Boolean obstruction

Let `K` have rank `m-1` and take adjacent rank-`m` owners

\[
                     A=K+x,\qquad B=K+y.              \tag{3.1}
\]

The two-fragment order `A prec B` has one physical seam, with lower colour
`K` and immediate-upper colour `K+x+y`.  Reserving that occurrence, or
choosing incompatible endpoint histories, deletes the sole consecutive
cell.  The last-tail singleton shore has raw slack zero and fails Hall.

Thus an `O(1)` protected bank can kill a prescribed order even though the
unconditioned Johnson owner graph has quadratic degree.  Local atlas
abundance and marginal resource load do not imply (2.2).

## 4. What Boolean shadow expansion really proves

Let `I_m` be the balanced `m`-regular inclusion graph between

\[
 {\cal O}=\binom{[2m-1]}m,
 \qquad
 {\cal F}=\binom{[2m-1]}{m-1}.
\]

For `S subseteq O` and `R in N_0(S)`, let `D(S)` denote **all** heads of
`N_0(S)` with no surviving incidence from `S`, and put

\[
 c_S(R)=|\{T\in S:R\subset T\}|.                      \tag{4.1}
\]

### Lemma 4.1 (exact marginal surplus identity)

\[
 m\bigl(|N_0(S)|-|S|\bigr)
    =\sum_{R\in N_0(S)}(m-c_S(R)).                    \tag{4.2}
\]

Then marginal Hall after filtering is equivalent to

\[
 \sum_{R\in D(S)}c_S(R)
 \le
 \sum_{R\in N_0(S)\setminus D(S)}(m-c_S(R)).         \tag{4.3}
\]

#### Proof

Count the `m|S|` owner--facet incidences by their facet endpoint.  Subtract
the result from `m|N_0(S)|` to get (4.2).  Removing `D(S)` gives Hall exactly
when

\[
 |N_0(S)|-|D(S)|\ge|S|.
\]

Multiply by `m` and use (4.2); after splitting the sum between destroyed and
surviving heads, this is (4.3). \(\square\)

For nonempty `S`, let `x in [m,2m-1]` be the unique real number with
`|S|=binom(x,m)`.  The Lovasz--Kruskal--Katona bound gives

\[
 |N_0(S)|-|S|
 \ge {x\choose m-1}-{x\choose m}.                    \tag{4.4}
\]

This is an explicit raw marginal surplus, not a bound on the ordered table.
The stronger pump-anchored residual theorem
`MATH_THEOREM_K_TWISTED_C6_RESIDUAL_ORE_CURVATURE_AND_POLYNOMIAL_CORE_20260802.md`
extends the developed pump plus the opened `O(d)` bank under its explicit
arithmetic conditions for `d=O(sqrt(m))` and sufficiently large `m`.

There is also a quantitative small-shore deletion range.  Suppose at most
`p` facet heads are protected, the positive-history projection kills at most
`d` owner--facet incidences at each owner, and `q(S)` further literal
incidences from `S` are killed.

### Lemma 4.2 (marginal protected-history range)

For nonempty `S` and its real parameter `x` above, the filtered marginal
shore satisfies Hall whenever

\[
 {x\choose m-1}-{x\choose m}
       \ge p+d|S|+q(S).                               \tag{4.5}
\]

With `p=q(S)=0`, this includes

\[
                         x\le m+{m\over d+1}-1.        \tag{4.6}
\]

#### Proof

Protecting `p` heads reduces the raw surplus (4.4) by at most `p`.  A
completely destroyed head consumes at least one killed incidence, while at
most `d|S|+q(S)` incidences are killed.  Hence the number of destroyed heads
is at most that quantity, and (4.5) implies the Hall-damage inequality.
Finally

\[
 {x\choose m-1}-{x\choose m}
   =|S|{2m-x-1\over x-m+1};                           \tag{4.7}
\]

solving `((2m-x-1)/(x-m+1))>=d` gives (4.6).
\(\square\)

Neither result proves (2.2).  The live shores are contracted fragment
endpoint occurrences, not the adjacent Boolean ranks, and forward ordering
has already collapsed every raw-Hall-feasible suffix surplus to zero.

## 5. A sharp history-star obstruction before ordering

Even the marginal graph has no uniform history-deletion theorem without a
global chronology-coherence hypothesis.  Fix `K subseteq [2m-1]` of size
`t<=d` and put

\[
                  S_K=\{T\in{\cal O}:K\subseteq T\}.  \tag{5.1}
\]

Give every owner in `S_K` a past insertion history containing `K`.  This
rejects every incidence `T -> T-x` with `x in K`.  Put

\[
 A_t={2m-1-t\choose m-t},
 \qquad
 B_t={2m-1-t\choose m-1-t}={m-t\over m}A_t.          \tag{5.2}
\]

### Theorem 5.1 (history-star deficiency)

The filtered neighborhood of `S_K` is contained in the facets containing
`K`.  Hence its Hall deficiency is at least

\[
                       A_t-B_t={t\over m}A_t.          \tag{5.3}
\]

The completely destroyed boundary contains at least `tA_t` facet heads,
while the raw Hall surplus is exactly

\[
                       {t(m-1)\over m}A_t.             \tag{5.4}
\]

If `d=t` and the insertion-history entries are exactly the members of `K`,
all three assertions are equalities: the filtered neighborhood has size
`B_t`, the boundary has size `tA_t`, and the deficiency is (5.3).  Already
the depth-one case gives deficiency `Cat_(m-1)`; for every larger depth,
taking `t=1` and padding the history can only increase this lower bound.

#### Proof

There are `A_t` owners containing `K`.  Any surviving deletion removes a
coordinate outside `K`, so its facet still contains `K`; there are only
`B_t` such facets.  This proves the lower bound (5.3).  A boundary facet
obtained by deleting `x in K` omits exactly that one member of `K`; it
recovers both `x` and its unique owner `T`.  Hence the `tA_t` boundary heads
are distinct and destroyed.  Before filtering, the full neighborhood is the
disjoint union of these boundary heads and the `B_t` internal heads, giving
(5.4).  When the history consists exactly of `K`, no deletion outside `K` is
rejected, so every internal facet survives and all bounds are equalities.
\(\square\)

If `a_K` is the number of surviving cross incidences `(T,x)` with
`T superset K,x in K`, while every internal facet containing `K` survives,
then Hall on `S_K` is equivalent to the exact anti-star exposure row

\[
                           a_K\ge {t\over m}A_t.       \tag{5.5}
\]

This is a fixed endpoint-state obstruction, not a proof that the adverse
states arise from one globally coherent chronology.  It proves that history
depth and per-owner deletion degree alone cannot replace coherence.

There is a direct two-corridor version.  Let `V_res` be the residual owner
bank and put

\[
             W_z=V_{\rm res}\cap\{T:z\in T\}.         \tag{5.6}
\]

Assume explicitly that the fixed residual state assignment **seals** `z` in
both directions: no accepted transition has exactly one endpoint in `W_z`.
Let `ell_z` be the number of designated sink tails in `W_z` and `r_z` the
number of designated root heads there.  Any two-path cover then requires

\[
                              \ell_z=r_z.              \tag{5.7}
\]

Indeed, internal edge conservation matches
`|W_z|-ell_z` tail roles to `|W_z|-r_z` head roles.  Thus root/sink placement
must be balanced across every history-closed residual class.  This is a
fixed-state necessary condition, not a claim that an adverse sealed class is
forced by every coherent chronology.

## 6. The coherent bi-history state graph

The adverse assignments in Section 5 motivate using chronology states as
vertices rather than deleting edges after the fact.  Let `Omega` have size
`2m-1`.  A two-sided depth-`d` state is

\[
                         (T;I,D),                      \tag{6.1}
\]

where `|T|=m`, `I=(i_1,...,i_d)` is an ordered tuple of distinct members of
`T`, and `D=(d_1,...,d_d)` is an ordered tuple of distinct members of
`Omega-T`.  They are the last `d` insertions and deletions.

A directed transition chooses

\[
             a\in T\setminus I,
 \qquad
             b\in(\Omega\setminus T)\setminus D,      \tag{6.2}
\]

and sends (6.1) to

\[
\left(T-a+b; (b,i_1,\ldots,i_{d-1}),
                 (a,d_1,\ldots,d_{d-1})\right).       \tag{6.3}
\]

At `d=0`, both tuples and both shifted tuples in (6.3) are empty.

### Theorem 6.1 (exact coherent-history supply)

For `0<=d<=m-2`, this directed graph is vertex-transitive and has equal
in- and out-degree

\[
                         q_d=(m-d)(m-d-1).             \tag{6.4}
\]

Every directed walk in it is biresident at depth `d`.  Conversely every
depth-`d` biresident owner chronology, together with its initial two history
tuples, lifts uniquely to a directed walk in this graph.

#### Proof

There are `m-d` choices for `a` and `m-1-d` choices for `b`, proving the
out-degree.  When `d=0`, this is the ordinary symmetric directed Johnson
graph, whose in- and out-degree are both `m(m-1)`.  Now assume `d>=1`.
At a target state, the newest deletion and insertion determine
`a,b` and hence the predecessor owner.  The dropped oldest insertion can be
chosen in `m-d` ways and the dropped oldest deletion in `m-d-1` ways, proving
the in-degree.

The symmetric group on `Omega` acts transitively on the ordered `I,D`
positions and on the two unmarked coordinate classes, proving vertex
transitivity.  Conditions (6.2) say exactly that no coordinate is deleted or
reinserted within `d` steps; the shift in (6.3) is the exact history update.
This proves both chronology assertions. \(\square\)

Each physical owner has

\[
                            (m)_d(m-1)_d              \tag{6.5}
\]

state copies.  Therefore (6.4) is genuine accepted local supply, but it is
not yet a physical owner table: one must select exactly one state copy of
each owner.  That owner-fibre transversal is precisely the correlation which
the arbitrary history-star assignment destroys and which marginal
Ore--Ryser does not see.

The local typed resource multiplicities are exact and give an explicit
worst-case union bound.  For a fixed state, the next owner `T-a+b` determines
`(a,b)` uniquely.  Thus all `q_d` next owners are distinct.  A fixed lower
facet `T-a` occurs for at most `m-d-1` allowed insertions `b`, while a fixed
upper cap `T+b` occurs for at most `m-d` allowed deletions `a`.

### Corollary 6.2 (literal outgoing survival after protection)

Fix an unprotected current owner/tail `T`.  If a protected bank contains at
most `f` lower facets, `u` immediate-upper caps, `h` forbidden **next/head**
owners, and `e` additional transition-specific seam occurrences, then every
coherent history state at `T` has at least

\[
 q_d-f(m-d-1)-u(m-d)-h-e                            \tag{6.6}
\]

surviving outgoing transitions.  In particular an `O(d)` bank with bounded
typed loads leaves positive local **outdegree** for `d=O(sqrt(m))` and
sufficiently large `m`.

#### Proof

Use the preceding multiplicities and the union bound.  One protected owner
or one literal seam occurrence removes at most one of the distinct next-owner
options. \(\square\)

For `d>=1` there is no analogous fixed-state incoming resource bound.  At a
target state, the newest insertion and deletion labels already determine the
unique predecessor owner and physical seam; the `q_d` incoming state edges
differ only in the two dropped oldest history labels.  One forbidden
predecessor owner or seam can therefore delete all of them.  At `d=0`, the
ordinary Johnson in-neighbours are distinct.  This is another reason that
complete positive-depth endpoint states must be chosen jointly with the
path, rather than frozen before an expansion argument.

This is genuine local robustness, but it does not contradict Theorem 1.1:
a Hamilton order can fail because one **chosen consecutive** cell is absent
even when both of its endpoints have many other accepted neighbours.

## 7. Order-free partition-Hamilton contraction

**Superseded draft.**  This section incorrectly treats every state copy as a
physical vertex.  The corrected theorem uses one state per physical fibre
and fibre-union subtour cuts; see the replacement note named in the status.

Let `G_acc` be the accepted literal fragment/state digraph before any total
order is chosen.  Put

\[
 r_1=D_c,\quad s_1=C_{bc},\qquad
 r_2=B_{bc},\quad s_2=A_b.                            \tag{7.1}
\]

Add the two protected formal arcs

\[
              g_1:s_1\to r_2,qquad g_2:s_2\to r_1,  \tag{7.2}
\]

where `g_1` is the fixed new-phase edge and `g_2` is the contracted protected
pump composite.  These arcs carry their complete literal endpoint states and
resource ledgers.

### Theorem 7.1 (order-free equivalence and exact master)

The following are equivalent.

1. `G_acc` contains two vertex-disjoint directed paths

   \[
        Q_1:r_1\leadsto s_1,qquad Q_2:r_2\leadsto s_2
   \]

   whose vertices partition the residual fragment bank.
2. `G_acc+{g_1,g_2}` has a directed Hamilton cycle containing both protected
   arcs.
3. There is a binary arc vector `x` satisfying

   \[
   \begin{aligned}
    x_{g_1}=x_{g_2}&=1,\\
    x(\delta^+(v))=x(\delta^-(v))&=1 &&(v\in V),\\
    x(\delta^+(U))&\ge1
       &&(\varnothing\ne U\subsetneq V),              \tag{7.3}
   \end{aligned}
   \]

   together with every uncompiled occurrence and charge row.

#### Proof

Concatenating `g_2,Q_1,g_1,Q_2` proves `1=>2`; deleting `g_1,g_2` proves the
converse and fixes the endpoint pairing.  The degree rows in (7.3) make the
selected arcs a directed cycle cover.  The proper-set outgoing cuts say that
this cover has only one component, proving `2<=>3`. \(\square\)

If `g:u->v` is contracted, the marked supervertex retains only arcs entering
`u` and arcs leaving `v`; arcs entering `v` or leaving `u` are discarded.
This forced-arc contraction is bijective on Hamilton cycles containing `g`.
Ordinary untyped contraction would create false cycles.

Dropping the last line of (7.3) leaves the exact two-path-plus-cycle-cover
projection.  It is a bipartite matching between tail roles
`V-{s_1,s_2}` and head roles `V-{r_1,r_2}`, and hence is feasible exactly
when

\[
 |N^+_{G_{\rm acc}}(X)\cap(V-\{r_1,r_2\})|\ge |X|
 \quad\bigl(X\subseteq V-\{s_1,s_2\}\bigr).          \tag{7.4}
\]

Equation (7.4) is the sharp order-free Hall threshold for a degree-feasible
cover.  The subtour rows in (7.3), not extra frozen-order slack, are the
remaining topology condition.

### Proposition 7.2 (general semidegree calibration and sharp sparse cut)

After forced-arc contraction, a general sufficient Hamiltonicity threshold
is minimum in- and out-degree at least half the contracted vertex count; this
is the directed Dirac--Ghouila-Houri theorem.  Without additional structure
the half threshold is sharp up to rounding, as two disjoint complete
bidirected blocks show.

The coherent-history graph of Section 6 is far below this dense threshold:
its degree is polynomial in `m`, while its state count is exponential in
`m`.  Thus any positive theorem here must use Boolean sparse expansion or an
explicit construction.

There is already a sharp sparse obstruction.  If a nonempty proper residual
class `W` has no accepted transition crossing its boundary, then the
augmented graph fails the corresponding cut in (7.3), unless the protected
arcs themselves cross in the unique way needed to join it.  Before adding
the protected arcs, degree feasibility also forces the exact root/sink
balance

\[
 |W\cap\{r_1,r_2\}|=|W\cap\{s_1,s_2\}|.              \tag{7.5}
\]

The sealed-coordinate classes of Section 5 realize this obstruction.  Hence
the regular degree (6.4), or any scalar minimum-semidegree bound of the same
order, cannot by itself prove protected Hamiltonicity.

## 8. Exact surviving gate

The robust-surplus programme is now replaced by a sharper constructive
target.

> Select one coherent state `(T;I_T,D_T)` for every unprotected owner and
> partition those selected states into the two directed paths with endpoints
> `D_c -> C_bc` and `B_bc -> A_b`, while meeting the exact lower,
> immediate-upper, protected occurrence, and charge rows.

After such paths are selected, their vertex orders make every consecutive
cell in (2.2) nonempty automatically.  Before they are selected, fixing an
order has no robustness to exploit.

This theorem separates the gates exactly:

1. the pump plus `O(d)` owner/lower marginal factor is already covered by the
   residual Ore--Ryser curvature theorem;
2. common history has the uniform local state supply (6.4);
3. the open integral problem is the **owner-fibre transversal plus two-path
   topology and palette correlation**.

No deterministic construction of that transversal is claimed here.  The
zero-surplus theorem proves that such a construction, rather than another
ordered-Hall expansion estimate, is logically necessary.
