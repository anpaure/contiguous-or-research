# A prospective upper-exact forest has an exact endpoint common-basis lift,
# while pair-bank allocation alone does not make it physical

Date: 2026-08-01  
Lane: K / support-first Catalan owner selector / prospective coloured tree  
Status: unconditional one-sided pair-bank allocation, unconditional
prospective endpoint/common-basis and rooted-connector theorems, exact
small counterexamples to the missing physical implication.  Existence of
the required physical forest in every dimension remains open.

## 0. Outcome

Work on the rank-`m` Johnson graph on `[2m-1]`.  The exact support-first
target is a spanning linear forest `F` with

* every rank-`m+1` edge union used exactly once;
* every rank-`m-1` edge intersection used at most once; and
* the protected tight-pivot path contained with its prescribed orientation.

This note proves two positive statements and one sharp separation.

1. Every upper colour can be assigned integrally to a coordinate-pair
   endpoint bank, even after deleting an arbitrary protected colour family,
   so that every bank is independent in its one-sided dual transversal
   matroid.  This is an exact all-`m` matroid-union theorem.
2. Once the physical forest `F` exists, choosing its component orientations
   and constructing the correlated perfect matching `M_0` is only an
   ordinary two-matroid common-basis problem.  The exact free-port graph is
   then explicit, and a DAG subreservoir with rooted Hall joins the forest
   into one rooted path.
3. The first statement does not imply the hypothesis of the second.  There
   is a complete `m=3` pair-bank allocation, with all lower colours distinct,
   whose physical support contains a four-cycle.  At `m=4`, three locally
   legal bank atoms already force degree three at one owner.  Product
   rounding has positive-density branching and lower-colour collisions.

Thus the prospective construction has been reduced to one genuinely
correlated row:

\[
 \boxed{\text{upper-exact/lower-injective physical linear forest}}
 \quad+\quad
 \boxed{\text{endpoint common basis}}
 \quad+\quad
 \boxed{\text{rooted acyclic Hall reservoir}}.       \tag{0.1}
\]

Only the first box is still an all-dimensional existence problem.  This is
strictly prospective: no fixed `M_0`, no Greene--Kleitman pruning, and no
post-hoc repair of a prescribed upper selector is used.

The canonical lexical GMN pull family is separately obstructed for
`m>=12`; the independent audit is recorded in
`MATH_AUDIT_K_R_LEXICAL_GMN_UPPER_OBSTRUCTION_20260801.md`.  That no-go is
construction-specific and is not used to prove (0.1).

## 1. The exact physical support system

Put

\[
 \Omega=[2m-1],\qquad
 \mathcal O={\Omega\choose m},\qquad
 \mathcal L={\Omega\choose m-1},\qquad
 \mathcal U={\Omega\choose m+1}.                    \tag{1.1}
\]

Write

\[
 W=|\mathcal O|=|\mathcal L|,
 \qquad U=|\mathcal U|={m-1\over m+1}W,
 \qquad C=W-U=\operatorname {Cat}_m.                 \tag{1.2}
\]

For a Johnson edge `e=XY`, put

\[
                 \lambda(e)=X\cap Y,\qquad
                 \upsilon(e)=X\cup Y.               \tag{1.3}
\]

Let `P` be the prescribed tight-pivot edge path.  Binary edge variables
`x_e` describe the desired support exactly by

\[
\begin{aligned}
 \sum_{e:\upsilon(e)=R}x_e&=1 &&(R\in\mathcal U),\\
 \sum_{e:\lambda(e)=L}x_e&\le1&&(L\in\mathcal L),\\
 \sum_{e\ni X}x_e&\le2&&(X\in\mathcal O),\\
 \sum_{e\in E(S)}x_e&\le |S|-1
       &&(\varnothing\ne S\subseteq\mathcal O),\\
 x_e&=1&&(e\in P),\\
 x_e&\in\{0,1\}.                                    \tag{1.4}
\end{aligned}
\]

The first row is upper surjectivity and exactness; the next two are lower
injectivity and physical degree two; the fourth is the graphic row.  Hence
(1.4) is necessary and sufficient for a spanning upper-exact,
lower-injective Johnson linear forest containing `P`.  Such a forest has
exactly `U` edges and therefore exactly `C` components, isolates included.

This is the prospective physical row.  The fixed-`M_0` four-matroid
formulation is recovered only after one chooses a root matching.  Section 5
shows that it is advantageous to postpone that choice until after (1.4).

## 2. An all-pair one-sided endpoint allocation

Fix a coordinate pair \(a\in{\Omega\choose2}\), and put

\[
 X_a={\Omega\setminus a\choose m-1},\qquad
 Y_a={\Omega\setminus a\choose m}.                  \tag{2.1}
\]

Let `T_a` be the transversal matroid on `X_a` represented by containment
into `Y_a`: a family of residual `(m-1)`-sets is independent if its members
can be assigned distinct containing members of `Y_a`.  Put

\[
                         N_a=T_a^*.                  \tag{2.2}
\]

An SCD of \(2^{\Omega\setminus a}\) saturates `Y_a`, so, with

\[
 D={2m-3\choose m-1},\qquad E={2m-3\choose m},       \tag{2.3}
\]

we have

\[
 r(T_a)=E,\qquad
 r(N_a)=D-E={2D\over m}=\operatorname {Cat}_{m-1}.   \tag{2.4}
\]

The upper colours containing `a` are in bijection with `X_a` by

\[
                         R\longmapsto R\setminus a.  \tag{2.5}
\]

Pull `N_a` back along (2.5), and make every upper colour not containing
`a` a loop.

### Theorem 2.1 (prospective all-pair endpoint colouring)

For every `m>=2` and every protected family
\(\mathcal P\subseteq\mathcal U\), there is a partition

\[
        \mathcal U\setminus\mathcal P
             =\mathop{\dot\bigcup}_{a\in{\Omega\choose2}} I_a  \tag{2.6}
\]

such that

\[
 R\in I_a\Longrightarrow a\subset R,                \tag{2.7}
\]

and

\[
             \{R\setminus a:R\in I_a\}
                 \quad\hbox{is independent in }N_a. \tag{2.8}
\]

#### Proof

The symmetric group on `Omega-a` acts transitively on `X_a` and preserves
`N_a`.  Averaging the orbit of any basis gives

\[
                 {r(N_a)\over D}{\bf1}_{X_a}
                    ={2\over m}{\bf1}_{X_a}
                    \in B(N_a).                     \tag{2.9}
\]

Consequently, for every \(A\subseteq X_a\),

\[
                         r_{N_a}(A)\ge {2\over m}|A|. \tag{2.10}
\]

Put

\[
 q={m+1\choose2},\qquad
 z^a_R=\begin{cases}
              1/q,&a\subset R,\\
              0,&a\not\subset R.
             \end{cases}                            \tag{2.11}
\]

Because

\[
                     {1\over q}={2\over m(m+1)}
                         \le {2\over m},             \tag{2.12}
\]

the vector `z^a` belongs to the independent-set polytope of the pulled-back
`N_a`: the matroid independent polytope is downward closed and contains
the segment from zero to (2.9).  Every upper colour contains exactly `q`
coordinate pairs, so

\[
                         \sum_a z^a_R=1.             \tag{2.13}
\]

For every \(A\subseteq\mathcal U\setminus\mathcal P\),
(2.10)--(2.13) give

\[
                         |A|\le\sum_a r_{N_a}(A).    \tag{2.14}
\]

Edmonds' matroid-union criterion says precisely that the whole restricted
ground set can be partitioned into independent sets of the pulled-back
matroids.  This is (2.6)--(2.8).  \(\square\)

For each `a`, the set in (2.8) extends to a basis `B_a` of `N_a`.
Equivalently, \(X_a\setminus B_a\) matches bijectively into all of `Y_a`.
This
is the exact one-sided short-top or deletion-bank interpretation.

Deleting \(\mathcal P\) before applying the theorem protects the pivot's upper
colours, but not its physical owners, lower colours, heads, or connector
ports.  Those resources are not represented in `N_a` and must not be
silently inferred from (2.6).

## 3. How many fixed-pair funnels are even possible?

Let `A` be a collection of `t` coordinate pairs and regard it as the edge
set of a graph `G` on `Omega`.  If every upper colour is to be assigned to
one of these pairs, then every `(m+1)`-set must contain an edge of `G`, or
equivalently

\[
                              \alpha(G)\le m.         \tag{3.1}
\]

### Proposition 3.1 (hitting lower bound)

Every such fixed-pair family has

\[
                              t\ge m-1.              \tag{3.2}
\]

At the support-hitting level this is sharp.

#### Proof

Choosing one endpoint of every edge gives a vertex cover of order at most
`t`.  Its complement is independent and has order at least `2m-1-t`.  If
`t<=m-2`, it contains an independent `(m+1)`-set, contradicting (3.1).

For sharpness, take `m-1` disjoint pairs and one unmatched coordinate.  Its
independence number is `m`, so every `(m+1)`-set contains a chosen pair.
\(\square\)

One one-sided pair bank has rank at most `Cat_(m-1)`.  Hence palette
capacity gives the stronger necessary condition

\[
 t\ge
 \left\lceil{U\over\operatorname {Cat}_{m-1}}\right\rceil
 =\left\lceil{(2m-1)(m-1)\over m+1}\right\rceil.     \tag{3.3}
\]

For `m>=5`, the right side is `2m-4`.  The earlier scalar observation that
four fixed-pair SCD funnels have enough order to supply `Cat_m` **connector
ports** concerns a different bank.  Four funnels cannot cover the full
upper palette in the present support-first problem.

## 4. Pair-bank independence does not imply a physical forest

An assignment of an upper colour `R` to the pair `a={i,j} subset R`
forces the physical Johnson edge

\[
                     R-i\quad--\quad R-j             \tag{4.1}
\]

and forces its lower colour to be `R-a`.  Therefore a complete assignment
is a solution of (1.4) exactly when

1. the residuals `R-a` are distinct;
2. every rank-`m` owner has forced degree at most two; and
3. the forced owner graph is acyclic.

The local matroids `N_a` impose none of the cross-bank degree or graphic
rows.

### Proposition 4.1 (complete `m=3` graphic counterexample)

On `[5]`, use

\[
\begin{array}{c|c|c}
R&a&R-a\\ \hline
1234&34&12\\
1245&25&14\\
1345&34&15\\
1235&25&13\\
2345&23&45.
\end{array}                                           \tag{4.2}
\]

The `34`- and `25`-banks are bases of their local rank-two endpoint
matroids `U_(2,3)`; the `23`-bank is an independent singleton; and the five
lower residuals are distinct.  Nevertheless (4.1) is

\[
       123-124-145-135-123
       \qquad\mathbin{\dot\cup}\qquad245-345.         \tag{4.3}
\]

Thus the complete upper palette and every one-sided endpoint row pass while
the graphic row fails.

### Proposition 4.2 (`m=4` branching counterexample)

The locally legal atoms

\[
 (12345,15),\qquad(12346,26),\qquad(12347,37)         \tag{4.4}
\]

have distinct lower residuals `234,134,124`, but all three forced edges
meet the owner `1234`.  Hence local independence and lower injectivity do
not imply the degree-two row either.

### Proposition 4.3 (the uniform point has every scalar and cut margin)

Give every edge in the `(m+1)`-clique of each upper colour weight

\[
                              1/q,\qquad q={m+1\choose2}.           \tag{4.5}
\]

Then every upper row has weight one, every lower row has weight

\[
                    {{m\choose2}\over q}={m-1\over m+1}<1,          \tag{4.6}
\]

and every owner has weighted degree

\[
                    {m(m-1)\over q}={2(m-1)\over m+1}<2.            \tag{4.7}
\]

It also satisfies every graphic inequality.  Indeed, for an owner set `S`
of order `s`, its internal weight is at most

\[
 \min\left\{{s\choose2}/q, {m-1\over m+1}s\right\}.                \tag{4.8}
\]

The first term is at most `s-1` for `s<=2q`, and the second is at most
`s-1` for `s>(2q)`.  Thus the obstruction is integral correlation, not a
fractional palette, degree, or graphic cut.

Independent per-colour rounding of (4.5) makes the degree of a fixed owner

\[
       \operatorname {Bin}\left(m-1,{2\over m+1}\right),            \tag{4.9}
\]

so the probability of degree at least three tends to

\[
                              1-5e^{-2}>0.                           \tag{4.10}
\]

A fixed lower colour has load

\[
       \operatorname {Bin}\left({m\choose2},{1\over q}\right),     \tag{4.11}
\]

whose collision probability tends to `1-2/e>0`.  Hence any product or
purely local rounding produces `Theta(W)` branching and lower collisions.
This is the prospective analogue of the positive-density GK branching
barrier.

## 5. Prospective construction of `M_0` from a physical forest

Assume now that `F` is a solution of (1.4).  Let

\[
 \mathcal A=\mathcal L\setminus\{\lambda(e):e\in F\}.               \tag{5.1}
\]

Then \(|\mathcal A|=C\).  Give every component `K` one of its possible path
orientations.  Write `h_K` for its initial owner and `b_K` for its terminal
owner.  An isolated owner has one state with `h_K=b_K`.

Let `Sigma` be the set of allowed component-orientation states.  On `Sigma`
define

* the partition matroid `P_comp`, allowing at most one state per component;
* the transversal matroid `T_A`, in which a state `(K,h_K,b_K)` is adjacent
  to \(a\in\mathcal A\) exactly when \(a\subset b_K\).

If the tight-pivot component and direction are prescribed, delete its
incompatible orientation state before forming these matroids.

### Theorem 5.1 (endpoint common-basis lift)

The forest orientations admit a prospective perfect matching `M_0`
compatible with all oriented forest edges if and only if `P_comp` and
`T_A` have a common basis of order `C`.  Equivalently,

\[
 r_{P_{\rm comp}}(Z)+r_{T_{\mathcal A}}(\Sigma\setminus Z)\ge C
                     \qquad(Z\subseteq\Sigma).        \tag{5.2}
\]

Given such a basis and a matching

\[
                         K\longmapsto a_K\in\mathcal A,
                         \qquad a_K\subset b_K,       \tag{5.3}
\]

define

\[
 \begin{aligned}
 M_0(X\cap Y)&=X&&\text{for every oriented edge }X\to Y\text{ of }F,\\
 M_0(a_K)&=b_K&&\text{for every component }K.         \tag{5.4}
 \end{aligned}
\]

Then \(M_0:\mathcal L\to\mathcal O\) is a perfect incidence matching, and the
successor incidences of `F` contract to an upper-exact directed linear
forest.  On a protected pivot

\[
                         V_0\to V_1\to\cdots\to V_t,
\]

equation (5.4) gives

\[
                         M_0(V_i\cap V_{i+1})=V_i,    \tag{5.5}
\]

which is precisely the correlated predecessor phase.

#### Proof

A common basis chooses exactly one orientation of every component and can
be matched to all `C` members of \(\mathcal A\); this is exactly (5.3).
Conversely any such oriented assignment is independent of order `C` in both
matroids and hence is a common basis.  Edmonds' two-matroid min--max theorem
gives (5.2).

On a component with `v` owner vertices, (5.4) maps its `v-1` internal
intersection colours bijectively to its nonterminal owners.  Equation (5.3)
maps one unused lower colour to its terminal.  Across components, the
internal colours and \(\mathcal A\) partition \(\mathcal L\), while
nonterminals and terminals partition \(\mathcal O\).  All maps are
containment incidences,
so `M_0` is perfect.

For consecutive oriented edges \(X\to Y\to Z\), the lower colour
\(X\cap Y\) has its successor incidence to `Y`, whose `M_0`-preimage is
\(Y\cap Z\).
At the last edge the preimage of the terminal is `a_K`.  Thus every physical
component contracts to one directed rooted path and (5.5) holds.  Upper
labels are unchanged edge unions, hence remain exact. \(\square\)

This theorem is the promised prospective simplification.  Once the
physical forest is born inside the upper-exact fibre, the choice of `M_0`
is not a four-matroid intersection: it is one ordinary matroid intersection
on component orientations.

## 6. The exact rooted connector theorem

Under Theorem 5.1, the free outgoing rooted port of component `K` is `a_K`,
and the first owner of component `K'` is `h_(K')`.  Hence the complete
free-port component digraph has the literal rule

\[
 \boxed{K\longrightarrow K'
       \iff K\ne K'\ \text{ and }\ a_K\subset h_{K'}.}              \tag{6.1}
\]

Let `K_*` be the component required to contain the initial tight-pivot
path.

### Theorem 6.1 (rooted acyclic Hall completion)

Let `D` be any DAG subgraph of (6.1).  There is a set of `C-1` connector
arcs which joins the components into one directed Hamilton path starting at
`K_*` if and only if

\[
 |N_D^-(Y)|\ge |Y|
       \qquad\bigl(Y\subseteq\operatorname {Comp}(F)\setminus\{K_*\}\bigr).
                                                               \tag{6.2}
\]

#### Proof

Apply Hall to the bipartite graph with outgoing component copies on the
left and incoming copies of every component except `K_*` on the right.
Condition (6.2) gives a matching saturating all `C-1` right copies.
Thus the selected arcs have distinct tails and heads, every nonroot has
indegree one, and the root has indegree zero.  The DAG hypothesis excludes
a directed cycle.  With `C` vertices and `C-1` edges the selected graph is
therefore one directed path, necessarily starting at `K_*`.  The converse
is immediate. \(\square\)

Only one acyclic Hall-passing subreservoir is needed.  The full admissible
port graph may contain cycles.

### Corollary 6.2 (direct component-chain certificate)

It is sufficient to orient and order the components

\[
                         K_*=K_1,K_2,\ldots,K_C       \tag{6.3}
\]

so that, for `i<C`, the terminal `b_i` and next start `h_(i+1)` are Johnson
adjacent and

\[
       a_i=b_i\cap h_{i+1}\in\mathcal A              \tag{6.4}
\]

are distinct and exhaust all but one member `a_C` of \(\mathcal A\), with

\[
                              a_C\subset b_C.         \tag{6.5}
\]

Then set `M_0(a_i)=b_i`.  The seams `K_i->K_(i+1)` themselves are the
required DAG reservoir and Hamilton path.

This is the sharp prospective coloured auxiliary-tree target: the
"auxiliary tree" may be taken to be a path, with its connector colours
drawn from the missing lower bank.

## 7. First-dimensional positive calibration

At `m=3`, take the physical forest

\[
 135-123-124-145,\qquad134-345,\qquad235-234,
 \qquad125,\qquad245.                               \tag{7.1}
\]

Its five edge unions are all five rank-four colours and its lower colours
are

\[
                              13,12,14,34,23.         \tag{7.2}
\]

Thus

\[
                              \mathcal A=\{15,24,25,35,45\}.          \tag{7.3}
\]

Orient and order the components as

\[
 134\to345;\quad235\to234;\quad245;\quad
 145\to124\to123\to135;\quad125.                   \tag{7.4}
\]

The four consecutive seams have lower colours

\[
                              35,24,45,15,            \tag{7.5}
\]

and the final terminal `125` contains the remaining colour `25`.  Hence
Corollary 6.2 gives the literal owner Hamilton path

\[
 134,345,235,234,245,145,124,123,135,125.             \tag{7.6}
\]

This verifies all statements of the prospective lift at the first
nontrivial dimension.  It is not evidence for the general existence row.

## 8. The three-primary quotient cannot be an `O(1)` sidecar

Suppose `m=3r+2`.  In the maximal three-free cyclic quotient, the residual
order-three action has exactly `Cat_r` fixed row orbits and no fixed column
or symbol.  Therefore every equivariant row-saturating selector must break
symmetry on all `Cat_r` of those orbits.

### Proposition 8.1 (deferring orientation does not absorb a three-stabilizer)

The same obstruction holds for an equivariant **undirected** exact-one
physical support, even if every component is to be oriented only later.

#### Proof

Above a fixed quotient row, an exact physical edge is an unordered
column--symbol endpoint pair `{B,A}`.  The order-three stabilizer would act
setwise on this pair, giving a homomorphism

\[
                              C_3\longrightarrow S_2. \tag{8.1}
\]

That homomorphism is trivial.  Hence both endpoints would be fixed
individually, whereas the three-primary quotient theorem says there is no
fixed column and no fixed symbol.  This is impossible. \(\square\)

The obstruction says that a **fully equivariant choice** is impossible.  It
does not say that the fixed rows are hard to select after symmetry is
deliberately broken.  In fact they have a canonical protected form.

### Theorem 8.2 (the fixed-row bank is automatically an isolated matching)

Let `K` be the order-three coordinate subgroup.  For every `K`-fixed row

\[
                              C=\bigcup_{j=1}^r O_j                  \tag{8.2}
\]

and every legal chosen column `B=C+{b}`, let

\[
                         A=C+\{\alpha(B)\}                          \tag{8.3}
\]

be its symbol for a perfect incidence matching `mu`.  Choose one such cell
for every fixed row `C`.  Then all chosen tails `B`, all chosen symbols `A`,
and indeed all endpoints across both roles are pairwise distinct.  The
selected directed edges `B->A` are therefore a matching of isolated edges.

#### Proof

For any set of the form `X=C+{x}`, with `C` a union of `K`-orbits and
`x notin C`, define

\[
                    \kappa(X)=X\cap kX\cap k^2X.                    \tag{8.4}
\]

The three points in the `K`-orbit of `x` are distinct and outside `C`, so

\[
                              \kappa(X)=C.                          \tag{8.5}
\]

Both `B` and `A` have this form: incidence legality gives
`alpha(B) notin B`, hence `alpha(B) notin C`.  Thus either endpoint uniquely
recovers its row core `C`.  Endpoints belonging to different rows cannot
coincide.  For one row, `A!=B` because `alpha(B) notin B` while `b in B`.
Therefore no endpoint occurs in two selected edges. \(\square\)

In the maximal clean quotient this gives `(s/3)Cat_r` literal protected
edges, arranged into `Cat_r` residual orbits.  Thus it is naturally a
`Cat_r`-state orbit bank.  Choosing its phases is the necessary symmetry
breaking from Proposition 8.1, but no Hall, degree, or graphic obstruction
remains inside the bank itself.

Contract this protected bank exactly as follows:

1. delete its fixed row constraints;
2. contract its chosen tails in the column partition matroid;
3. contract its chosen symbols in the symbol partition matroid; and
4. contract its pairwise-disjoint directed edges in the graphic matroid.

The opposite port roles remain available: a protected tail may still receive
one residual incoming edge, and a protected symbol may still emit one
residual outgoing edge.  This is ordinary directed-path contraction, not
deletion of the whole endpoint pair.

After all `K`-fixed rows are removed, the residual action on rows is free.
Indeed, the residual group is cyclic of three-power order, and every
nontrivial stabilizer contains its order-three subgroup.  Columns and
symbols had no order-three fixed vertices already.  Thus the prospective
quantifier order can be sharpened to

\[
 \boxed{\text{protected fixed-row matching}}
 \longrightarrow
 \boxed{\text{free-action residual forest}}
 \longrightarrow
 \boxed{\text{endpoint/common-basis and rooted Hall}}.             \tag{8.6}
\]

The first box is now unconditional.  Freeness of the residual action does
not itself supply the second box, and the selected phase bank need not leave
an invariant residual resource set.

The endpoint orientation in Theorem 5.1 occurs only **after** the physical
row/edge selector `F` has been constructed.  It changes component directions
and assigns unused lower colours to terminals; it does not create a missing
fixed column or symbol for a fixed row.  Consequently it cannot reduce the
exception count:

\[
                       \text{exceptional quotient rows}
                         \ge\operatorname {Cat}_r.    \tag{8.7}
\]

In particular, no prospective construction based on the maximal clean
quotient plus `O(1)` exceptional rows can satisfy (1.4).  Theorem 8.2 now
supplies those rows as a protected matching rather than leaving them as an
unstructured braid debt.  The remaining free-action selector must extend
this contraction; the endpoint common-basis theorem acts only after that
residual physical forest exists.

An invariant redundant support can postpone the decision but cannot remove
it.  Over a fixed row its cells occur in orbits of order three, so the
smallest invariant menu has three cells and costs two redundant cells.
There are `(s/3)Cat_r` fixed quotient rows when the residual group has
order `s`, so this costs at least

\[
                         {2s\over3}\operatorname {Cat}_r             \tag{8.8}
\]

redundant quotient cells before orbit identification.
Choosing one representative from that menu still breaks symmetry on each of
the `Cat_r` residual row orbits.  A single recursive rule may correlate all
these choices; the theorem lower-bounds the number of affected orbits, not
the description length of the rule.

Thus the three-primary obstruction rules out bounded-exception residual
lifts, not non-equivariant or Catalan-recursive prospective constructions.

## 9. Generic rainbow theorems do not close the physical row

For fixed `M_0`, every upper-colour class has size `m+1` and the occurrence
graph has maximum degree `m-1`.  The generic bounded-degree full-rainbow
threshold for graphs is above `2 Delta`; sharp abstract examples exist at
`2 Delta-1`.  Since

\[
                              m+1<2(m-1)\qquad(m\ge4), \tag{9.1}
\]

no theorem using only class size and maximum degree can prove the required
rainbow forest.  The local pair-bank theorem likewise cannot replace the
missing correlation, by Propositions 4.1--4.3.

Any positive proof must therefore use Boolean structure while selecting the
physical support, not after fixing a generic `M_0` or after independently
rounding upper colours.

## 10. Exact remaining theorem and scope

The strongest sufficient all-`m` statement isolated here is:

> **Prospective protected forest theorem.**  For every sufficiently large
> `m` and every planted tight-pivot path in the proved protected range,
> system (1.4) has a solution `F` for which the endpoint-orientation
> matroids of Section 5 have a common basis and the resulting port graph
> contains a DAG satisfying rooted Hall (6.2).

Theorems 5.1 and 6.1 prove that this statement produces exactly the desired
upper-surjective directed linear forest `R` containing the pivot and its
acyclic connector reservoir.  Theorem 2.1 proves that its one-sided upper
endpoint allocation always exists.  Propositions 4.1--4.3 prove why the
remaining physical correlation cannot be omitted.

Nothing in this note proves residence, deeper shadows, the lower common-cap
compiler, or `nu(k)=B(k)`.  Those remain downstream guarded states.  The
result is an exact central owner-layer construction interface, not the full
contiguous-OR theorem.
