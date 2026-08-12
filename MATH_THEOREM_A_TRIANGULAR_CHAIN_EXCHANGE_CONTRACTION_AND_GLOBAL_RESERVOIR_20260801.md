# Triangular owner-chain contraction has an exact alternating-flow theorem and a global Boolean edit barrier

Date: 2026-08-01  
Lane: A, integral triangular owner-chain rounding  
Status: unconditional contraction/min--max theorems, an exact pairwise
exchange calculus, an abstract fractional-to-integral obstruction, and sharp
Boolean SCD edit lower bounds.  No unconditional integral triangular factor
for the complete Boolean ideal is claimed.

## 0. Outcome

Put

\[
 r=\left\lceil {k\over2}\right\rceil,\qquad
 W=\binom kr,\qquad
 P=\{S\subseteq[k]:1\le |S|<r\},\qquad
 \Lambda=|P|,
\]

and let \(d\) be least with

\[
                  dW+\binom{d+1}{2}\ge\Lambda.          \tag{0.1}
\]

The exact integral target has \(W\) owner resources of capacity \(d\) and
boundary resources \(\partial_i\) of capacities \(i\), \(1\le i\le d\).
This is weaker than a \(W\)-owner depth-\(D\) factor and is the correct
lower-cell profile at length \(B(k)\).

This note proves the following.

1. The overload

   \[
                  \Phi=\sum_v(\ell_v-c_v)_+             \tag{0.2}
   \]

   is an exact scalar Lyapunov function.  Under a stable, unit-saturated
   alternating exchange bank, it contracts to zero if and only if every
   overloaded resource cut has enough outgoing exchange capacity.
2. For two chains, every legal repartition is obtained by flipping connected
   components of their bipartite incomparability graph.  The attainable load
   changes are exact subset sums of the component imbalances.  Hence the
   first integral obstruction is a real subset-sum/lattice obstruction, not
   a fractional-capacity issue.
3. Once a global clock \(\tau:P\to[d]\) is fixed, triangular chainization is
   exactly a bipartite matching problem.  Hall is necessary and sufficient,
   and ordinary alternating augmentations give a contracting construction.
4. Rank symmetry, an \(O(d)\)-depth integral start, scalar capacity and even
   an exact fractional triangular factor do not imply integral contraction
   for an arbitrary containment poset.  A family of incomparable
   \((d+1)\)-chains gives an explicit obstruction.
5. On a saturated Boolean symmetric-chain decomposition, every triangular
   contraction must delete

   \[
      R_{k,d}=\sum_{\substack{j\ge1\\jd\le r-2}}
                  \binom{k}{r-jd-1}
      =\left({1\over2}+2\sum_{j\ge1}e^{-4\pi j^2}+o(1)\right)W   \tag{0.3}
   \]

   old successor edges and introduce asymptotically the same number of new
   ones.  It must also change a positive fraction
   \(\operatorname{erfc}(\sqrt\pi/2)+o(1)\) of all old target-owner
   incidences.  The \(d\) boundary chains are negligible on these scales.

Thus a bounded/local absorber cannot transform a classical SCD or a
worst-case \(O(d)\)-factor.  The surviving Boolean theorem is:

> construct one clock satisfying every chronology-Hall cut, or construct a
> hereditarily realizable unit-ear bank satisfying every overloaded exchange
> cut.

Either theorem gives the integral triangular factor.  Sliding-OR
serialization remains a later gate.

## 1. Exact triangular overload ledger

Let

\[
 {\cal V}=\binom{[k]}r\ \dot\cup\
          \{\partial_1,\ldots,\partial_d\},             \tag{1.1}
\]

with capacities

\[
                         c_T=d,\qquad c_{\partial_i}=i. \tag{1.2}
\]

Start with any anchored owner-chain factor, for example Tomon's
rank-symmetric \(O(d)\)-factor, and append \(d\) empty boundary chains.
Write \(\ell_v\) for the load of resource \(v\), and put

\[
 \sigma=\sum_vc_v-\Lambda
       =dW+\binom{d+1}{2}-\Lambda\ge0.                  \tag{1.3}
\]

Define

\[
 E=\sum_v(\ell_v-c_v)_+,\qquad
 U=\sum_v(c_v-\ell_v)_+.                               \tag{1.4}
\]

### Proposition 1.1 (exact overload identity)

\[
                  U=E+\sigma,\qquad
                  E={\|\ell-c\|_1-\sigma\over2}.        \tag{1.5}
\]

Consequently \(E=0\) if and only if every owner and boundary capacity is
satisfied.  Scalar balancing requires exactly \(E\) unit transfers.

#### Proof

Since the chains partition \(P\), \(\sum_v\ell_v=\Lambda\).  Therefore

\[
 \sum_v(c_v-\ell_v)=\sigma=U-E.
\]

Also \(\|\ell-c\|_1=E+U=2E+\sigma\).  This proves (1.5).
\(\square\)

For the initial factor, the boundary chains are empty.  If

\[
 E_{\rm own}=\sum_T(|C_T|-d)_+,\qquad
 U_{\rm own}=\sum_T(d-|C_T|)_+,
\]

then

\[
 U_{\rm own}+\binom{d+1}{2}=E_{\rm own}+\sigma.        \tag{1.6}
\]

Any feasible terminal factor moves at least \(E_{\rm own}\) targets out of
their original overloaded owner bins.  At most \(\binom{d+1}{2}\) can finish
in boundary bins, so at least

\[
             \left(E_{\rm own}-\binom{d+1}{2}\right)_+ \tag{1.7}
\]

must finish at different owners.

If the starting maximum load is \(H\le Ad\), then

\[
 E_{\rm own}\le\left(1-{d\over H}\right)\Lambda
              \le\left(1-{1\over A}\right)\Lambda.     \tag{1.8}
\]

Indeed, \((x-d)_+\le(1-d/H)x\) for \(0\le x\le H\).
Tomon's eventual bound \(H\le11d\) therefore gives
\(E_{\rm own}\le10\Lambda/11\).  This is only an upper bound: Tomon's
maximum-depth theorem alone gives no small-overload estimate.

## 2. A stable alternating bank gives exact contraction

A directed exchange atom \(a:u\to v\) is a physical chain repartition which
preserves every target, every unaffected chain and every owner label, and
changes only the two loads by

\[
                            \Delta_a=-e_u+e_v.          \tag{2.1}
\]

Let \(G\) be a directed bank of such atoms with integral arc capacities
\(\kappa\).

Call the bank **hereditarily path-realizable** when every integral
capacity-respecting collection of directed paths can be implemented by
compound alternating chain exchanges, and after any such implementation
the unused residual bank has the same property.  This is a physical
hypothesis, not a consequence of the load graph.

### Theorem 2.1 (exchange-bank max-flow/min-cut)

For a hereditarily path-realizable unit bank, the current factor contracts
to the triangular capacity box if and only if

\[
        \boxed{\quad
        \ell(X)-c(X)\le\kappa(\delta^+X)
                     \qquad(X\subseteq{\cal V}).\quad} \tag{2.2}
\]

An integral augmenting-path algorithm reaches the box in exactly
\(E\) unit transports, and every path lowers the potential (0.2) by one.

#### Proof

Put \(e_v=(\ell_v-c_v)_+\) and \(s_v=(c_v-\ell_v)_+\).
Make a flow network with source arcs of capacity \(e_v\), exchange arcs of
capacity \(\kappa\), and sink arcs of capacity \(s_v\).  All excess can be
routed if and only if every resource cut \(X\) satisfies

\[
                     e(X)\le s(X)+\kappa(\delta^+X).    \tag{2.3}
\]

Because \(e(X)-s(X)=\ell(X)-c(X)\), (2.3) is (2.2).  Integral max flow
decomposes into directed unit paths from overloaded to slack resources.
Hereditary realizability implements the paths successively.  One path
removes one unit of overload and creates none, so it lowers \(E\) by one.
After \(E\) paths all loads lie in the box.  The converse follows from the
same cut conservation. \(\square\)

A positive closed cut \(X\) with \(\ell(X)>c(X)\) is therefore an exact
obstruction for the declared exchange bank.

### Lattice qualification

Theorem 2.1 cannot be applied to an unsaturated move lattice.  If the legal
load vectors are \(\Delta_\gamma\), every reachable load lies in

\[
             \ell+\operatorname{span}_{\mathbb Z}
                         \{\Delta_\gamma\}.             \tag{2.4}
\]

For example, loads \((2,0)\), capacities \((1,1)\), and the sole move
\((-2,2)\) satisfy the scalar fractional balance but never reach
\((1,1)\).  A \(t\)-unit splice may be replaced by \(t\) unit arcs only
when graded intermediate splices really exist.  Unit-lattice saturation and
hereditary physical realization are load-bearing hypotheses.

## 3. Exact two-chain alternating exchanges

Let \(C,D\) be two inclusion chains.  Make the bipartite incomparability
graph \(I(C,D)\) on \(C\dot\cup D\); its edges join incomparable elements.
There are no edges inside either current chain.

### Theorem 3.1 (component-flip classification)

Every repartition of \(C\cup D\) into two inclusion chains is obtained by
independently flipping the two bipartition classes on connected components
of \(I(C,D)\).  Conversely every such collection of flips is a two-chain
repartition.

If \(C,D\) are anchored at owners \(T,U\), a component \(K\) may be flipped
without changing the owner labels if and only if

\[
       D\cap K\subseteq{\cal P}(T),\qquad
       C\cap K\subseteq{\cal P}(U).                    \tag{3.1}
\]

Here a boundary owner is interpreted as the universal set \([k]\).

#### Proof

A partition into two chains is exactly a proper two-colouring of the
incomparability graph.  On each connected bipartite component its
two-colouring is unique up to exchanging the colours.  This proves the
classification.  Condition (3.1) is precisely the requirement that every
transferred target remain below its new owner. \(\square\)

For an eligible component put

\[
                         \delta_K=|C\cap K|-|D\cap K|.  \tag{3.2}
\]

Flipping a family \({\cal J}\) transfers
\(\sum_{K\in{\cal J}}\delta_K\) load units from \(C\) to \(D\).
Therefore, if \(C\) has excess \(e_C\) and \(D\) slack \(s_D\), the exact
best pairwise contraction amount is

\[
 g_{CD}=\max\left\{
       \sum_{K\in{\cal J}}\delta_K:
       1\le\sum_{K\in{\cal J}}\delta_K\le\min(e_C,s_D)
                         \right\},                    \tag{3.3}
\]

with value zero when the set is empty.

For vertex-disjoint source--destination pairs these component flips commute.
Hence the maximum one-round decrease of \(E\) among disjoint two-bin
repartitions is exactly the maximum-weight matching in the overloaded/slack
bipartite graph with weights \(g_{CD}\).  Its standard integral
vertex-cover dual is

\[
 \min\left\{\sum_C\alpha_C+\sum_D\beta_D:
              \alpha_C+\beta_D\ge g_{CD},\
              \alpha,\beta\ge0\right\}.                \tag{3.4}
\]

If the maximum matching has positive weight in every reachable nonterminal
state, iteration terminates.  If it is always at least \(\varepsilon E\),
only \(O(\varepsilon^{-1}\log E)\) parallel rounds are needed.  Load-zero
component flips generate the natural Kempe orbit in which to seek a positive
move.

### Proposition 3.2 (the pairwise quantum obstruction is real)

At \(k=9,r=5,d=2\), take

\[
 C:\{1\}\subset\{1,2\}\subset\{1,2,3\},\qquad
 D:\{4\},                                                \tag{3.5}
\]

and distinct rank-five owners both containing \(\{1,2,3,4\}\).
The graph \(I(C,D)\) is connected \(K_{3,1}\), with imbalance two.
The only two-chain load vectors are \((3,1)\) and \((1,3)\).  Although the
scalar overload and slack at cap two are both one, no pairwise alternating
exchange reaches \((2,2)\).

Thus a third-chain circuit, a zero-load rerouting which changes later
component profiles, or a genuinely unit-saturated ear is sometimes
necessary even in the Boolean lattice.  This is a local pair obstruction,
not a \(k=9\) triangular-factor no-go.

## 4. A fixed clock makes the problem bipartite

Fix a function

\[
                              \tau:P\longrightarrow[d]. \tag{4.1}
\]

Make a bipartite graph \(B_\tau^\triangle\).  Its left shore is a copy
\(P_L\).  Its right shore is

\[
 P_R\ \dot\cup\ \binom{[k]}r\
     \dot\cup\{b_1,\ldots,b_d\}.                       \tag{4.2}
\]

Put edges

\[
\begin{aligned}
 S_L&\longrightarrow S'_R
    &&\text{if }S\subset S'\text{ and }\tau(S)<\tau(S'),\\
 S_L&\longrightarrow T
    &&\text{if }S\subset T,\quad |T|=r,\\
 S_L&\longrightarrow b_i
    &&\text{if }\tau(S)\le i.
\end{aligned}                                           \tag{4.3}
\]

### Theorem 4.1 (fixed-clock Hall equivalence)

There is an integral triangular chain factor compatible with \(\tau\) if
and only if \(B_\tau^\triangle\) has a matching saturating \(P_L\).
Equivalently, for every nonempty \(A\subseteq P\),

\[
 \boxed{\quad
 |A|\le |N_\tau^P(A)|+|N_O(A)|
             +d-\min_{S\in A}\tau(S)+1.\quad}          \tag{4.4}
\]

Here \(N_\tau^P(A)\) is the higher-time strict-superset neighbourhood and
\(N_O(A)\) is the rank-\(r\) owner neighbourhood.

#### Proof

Given a triangular factor, number positions in every chain from one upward.
Owner chains have at most \(d\) positions.  Boundary chain \(b_i\) has at
most \(i\), so its terminal time is at most \(i\).  Match every nonterminal
target to its successor and every terminal target to its owner or boundary
address.  This saturates \(P_L\).

Conversely, orient every matched target--target edge toward its right
endpoint.  Every target has outdegree one, target indegree at most one, and
every terminal resource indegree at most one.  Strict inclusion and strict
increase of \(\tau\) forbid cycles.  The components are target paths ending
at distinct terminals.  An owner path has at most \(d\) targets because its
times are distinct in \([d]\).  A path ending at \(b_i\) has increasing
positive times whose last value is at most \(i\), hence length at most
\(i\).  Transitivity puts every owner path below its terminal owner.

Hall proves the equivalence.  The boundary neighbours of a nonempty
\(A\) are exactly \(b_i\) with \(i\ge\min_A\tau\), giving the last term in
(4.4). \(\square\)

The existential problem is therefore

\[
 \boxed{\quad
 \min_{\tau:P\to[d]}
 \max_{\varnothing\ne A\subseteq P}
 \left(
 |A|-|N_\tau^P(A)|-|N_O(A)|
       -d+\min_A\tau-1
 \right)_+=0.\quad}                                    \tag{4.5}
\]

For fixed \(\tau\), all saturating matchings are connected by ordinary
symmetric-difference alternating cycles and paths.  There is no residual
parity, TU, or matching-exchange connectivity obstruction after a feasible
clock is supplied.

### Corollary 4.2 (augmenting contraction)

Split any starting chain factor into \(\tau\)-increasing pieces of length at
most \(d\), and retain their internal successor edges as a partial matching
in \(B_\tau^\triangle\).  If (4.4) holds, Berge augmentations extend this
partial matching to a saturating one.  Each augmentation lowers by one the
number of unmatched left endpoints.  At termination the resulting paths
are an exact integral triangular factor.

Thus (4.4) is an actual global alternating-exchange theorem, not merely an
existence encoding.

## 5. Fractional triangular capacity still need not round abstractly

Fix \(d\ge2\) and \(W\ge d+2\) with

\[
                         (d-1)W\ge2(d+1),              \tag{5.1}
\]

and put

\[
                         q=\left\lfloor{W+d\over2}\right\rfloor+1. \tag{5.2}
\]

Let \(P^\star\) be the disjoint union of \(q\) total chains
\({\cal C}_1,\ldots,{\cal C}_q\), each of length \(L=d+1\), with targets in
different components incomparable.  Give the system \(W\) distinct
equal-rank universal owners, and boundary capacities \(1,\ldots,d\).

### Theorem 5.1 (triangular fractional/integral separation)

This instance has:

1. an anchored integral starting factor of depth \(d+1\);
2. an exact fractional triangular chain factor, even when every resource
   is required to select a nonempty chain; and
3. no integral triangular chain factor.

#### Proof

Since \(q\le W\), assign each whole component to a distinct owner, proving
item 1.

List the resource capacities as \(c_a\): \(W\) copies of \(d\) and
\(1,2,\ldots,d\).  Their total is

\[
                         K=dW+{d(d+1)\over2}.           \tag{5.3}
\]

The assumptions imply

\[
 W+d\le q(d+1)\le K.                                   \tag{5.4}
\]

Choose real \(\theta_a\in[1,c_a]\) with
\(\sum_a\theta_a=q(d+1)\).  At resource \(a\), choose an integer
\(L_a\in\{1,\ldots,c_a\}\) with expectation \(\theta_a\), choose one of the
\(q\) components uniformly, and then choose a uniform \(L_a\)-element
subchain of that component.

A fixed target has probability

\[
 {1\over q}\,\mathbb E{L_a\over d+1}
             ={\theta_a\over q(d+1)}                  \tag{5.5}
\]

of being selected at resource \(a\).  Summing over resources gives one.
All owner containments are automatic, proving item 2.

Integrally, no chain can meet two components.  Each component has length
\(d+1\), whereas every resource has capacity at most \(d\), so each
component needs at least two resource addresses.  But

\[
                         2q>W+d.                       \tag{5.6}
\]

There are too few resources. \(\square\)

This is a literal set-containment instance: use disjoint
\(X_i=\{x_{i,1},\ldots,x_{i,d+1}\}\), targets
\(S_{i,t}=\{x_{i,1},\ldots,x_{i,t}\}\), and equal-rank owners
\((\bigcup_iX_i)\cup\{y_j\}\).  It is not the complete Boolean ideal.
It proves that scalar overload, rank-symmetric-looking component chains,
an \(O(d)\) integral start and the exact fractional triangular theorem do
not constitute a contraction proof.  Boolean cross-component containment
must be used.

For every clock \(\tau:P^\star\to[d]\), each component needs at least two
\(\tau\)-increasing paths.  Thus target successors have matching rank at
most \(|P^\star|-2q\); adding the \(W+d\) terminals leaves deficiency at
least \(2q-(W+d)>0\).  This is a clock-independent Hall certificate for
(5.6).

## 6. The contraction is necessarily global on a saturated Boolean SCD

This section concerns a classical **saturated symmetric-chain
decomposition**.  Its exact binomial evaluations do not automatically apply
to Tomon's possibly rank-gapped decomposition.

For a saturated SCD chain \(C\), let \(\ell(C)\) be its number of nonempty
members below rank \(r\).

### Proposition 6.1 (owner-incidence change)

If the SCD chains keep their middle-owner labels, every terminal triangular
factor changes at least

\[
 E_{k,d}=\sum_C(\ell(C)-d)_+
        =\sum_{t=d+1}^{r-1}\binom{k}{r-t}              \tag{6.1}
\]

old target-owner incidences.

#### Proof

The terminal chain at the same owner retains at most \(d\) targets from its
old SCD chain.  Every other old target changes owner or enters a boundary
chain.  This proves the first expression.  In a saturated SCD,

\[
              \#\{C:\ell(C)\ge t\}=\binom{k}{r-t},     \tag{6.2}
\]

because such chains meet rank \(r-t\), and every set of that rank lies in
one chain.  Summing the layer-cake identity proves (6.1). \(\square\)

With

\[
                    {d\over\sqrt k}\longrightarrow
                    c=\sqrt{\pi\over8},
\]

the local central limit theorem and dominated Riemann convergence give

\[
 {E_{k,d}\over W\sqrt k}\longrightarrow
       \int_c^\infty e^{-2x^2}\,dx,
\qquad
 {E_{k,d}\over\Lambda}\longrightarrow
       \operatorname{erfc}\!\left({\sqrt\pi\over2}\right)
       \approx0.2101.                                  \tag{6.3}
\]

The triangular boundary capacity is \(O(d^2)=O(k)=o(\Lambda)\), so this
positive-density owner reassignment cannot be a bounded leave absorber.

### Proposition 6.2 (successor-edge cut floor)

Every terminal factor whose chain capacities are at most \(d\) deletes at
least

\[
 R_{k,d}=\sum_C\left\lfloor{\ell(C)-1\over d}\right\rfloor
        =\sum_{\substack{j\ge1\\jd\le r-2}}
                    \binom{k}{r-jd-1}                  \tag{6.4}
\]

old SCD successor edges.

#### Proof

Retained old successor edges on one SCD chain form runs of at most \(d\)
vertices.  Partitioning a path of \(\ell\) vertices into such runs deletes
at least \(\lfloor(\ell-1)/d\rfloor\) edges.  This number is
\(\sum_{j\ge1}\mathbf1_{\{\ell\ge jd+1\}}\).  Apply (6.2) with
\(t=jd+1\).  Rank zero is excluded, giving \(jd\le r-2\).
\(\square\)

For each fixed \(j\),

\[
 {1\over W}\binom{k}{r-jd-1}\longrightarrow
                         e^{-\pi j^2/4}.               \tag{6.5}
\]

A central-binomial product bound supplies a summable
\(e^{-c_0j^2}\) majorant, so dominated convergence gives

\[
 {R_{k,d}\over W}\longrightarrow
 \kappa:=\sum_{j\ge1}e^{-\pi j^2/4}
 ={1\over2}+2\sum_{j\ge1}e^{-4\pi j^2}
 =0.500006974\ldots.                                   \tag{6.6}
\]

The middle equality is Jacobi inversion for the theta series.

Let \(n_0\) be the number of nonempty lower SCD paths.  Initially there are
\(\Lambda-n_0\) old successor edges.  A terminal factor with \(c\le W+d\)
nonempty chains has \(\Lambda-c\) successor edges.  If \(A\) old edges are
deleted, the number of new edges is exactly

\[
                         B=n_0+A-c.                    \tag{6.7}
\]

For odd \(k=2m+1\), \(n_0=W\), so \(B\ge R_{k,d}-d\).
For even \(k=2m\),

\[
 n_0=\binom{2m}{m-1}=W-{W\over m+1},
\]

so \(B\ge R_{k,d}-W/(m+1)-d\).  In either parity,

\[
                         {B\over W}\ge\kappa-o(1).      \tag{6.8}
\]

Therefore a successful contraction changes at least
\((2\kappa-o(1))W\) successor incidences.  The \(d\) extra boundary chains
remove only \(o(W)\) of the splice debt.  This is a global
\(\Theta(W)\)-exchange theorem, not the retracted projection-\(W/2\)
argument.

## 7. Boundary absorption needs Ferrers shape

Suppose a residual family is already partitioned into chains of decreasing
lengths

\[
                         a_1\ge\cdots\ge a_s.           \tag{7.1}
\]

### Proposition 7.1 (exact triangular absorber criterion)

These chains fit the boundary capacities \(1,\ldots,d\) if and only if

\[
                         s\le d,\qquad
                         a_j\le d-j+1\quad(1\le j\le s).\tag{7.2}
\]

In particular every residual family of at most \(d\) targets is absorbed
as singleton chains.  An antichain of \(d+1\) targets is not absorbable,
although its cardinality is far below \(\binom{d+1}{2}\).

#### Proof

Sort the boundary capacities decreasingly as
\(d,d-1,\ldots,1\).  The largest residual chain must use the largest
capacity, the second largest the second largest, and so on.  This gives
(7.2), and the same assignment proves sufficiency.  An antichain needs one
resource per target. \(\square\)

Thus a rounded leave must be Ferrers/width controlled; an \(O(d^2)\)
cardinality bound or rankwise marginal bound does not suffice.

## 8. The smallest remaining Boolean lemma

There are two equivalent constructive targets.

### Clock form

Construct \(\tau:P\to[d]\) satisfying every cut (4.4).  Then Theorem 4.1
and Corollary 4.2 give the integral triangular factor by ordinary
augmenting paths.

### Stable-ear form

Starting from one anchored \(O(d)\)-factor, construct a matching-closed,
hereditarily realizable exchange bank whose move lattice contains the unit
differences on every relevant component and whose cuts satisfy (2.2).
Then Theorem 2.1 contracts the exact overload.

For a monotone prefix-graft subbank, the first obstruction is already
visible.  If \({\cal A}\subseteq\binom{[k]}s\) is the family of overloaded
bottoms and \({\cal B}\subseteq\binom{[k]}t\), \(s<t\), is the family of
slack host ceilings, a graft edge is \(A\subset B\).  If there is no such
edge, normalized matching gives

\[
 {|\mathcal A|\over\binom ks}
 +{|\mathcal B|\over\binom kt}\le1.                    \tag{8.1}
\]

#### Proof

The rank-\(t\) upper shadow of \({\cal A}\) has normalized size at least
\(|{\cal A}|/\binom ks\).  It is disjoint from \({\cal B}\). \(\square\)

Full Boolean levels therefore have the needed expansion, but dynamically
selected bottom and ceiling subfamilies can form a nearly tight cross-free
cut.  Rank symmetry and scalar overload do not exclude it.

The exact open statement is not “many possible exchanges.”  It is either

\[
       |N(X)|\ge|X|\quad\text{for every excess-token family }X, \tag{8.2}
\]

inside one stable physical ear bank, or the chronology-Hall system (4.4)
for one common clock.  The abstract obstruction in Section 5 proves that
some additional Boolean correlation is indispensable.

Even after (8.2), one must still construct the sliding-OR cocycle and upper
interval language.  No exact \(B(k)\) claim follows from this note alone.

## 9. Audit

The proof was independently audited with the following scope corrections.

* The binomial evaluations (6.1), (6.4) and their constants apply to a
  saturated classical SCD.  For an arbitrary Tomon factor only the literal
  load expressions \(\sum_T(\ell_T-d)_+\) and
  \(\sum_T\lfloor(\ell_T-1)/d\rfloor\) are automatic.
* A multiunit exchange is not a bank of unit moves without an actual graded
  refinement; the lattice condition (2.4) is essential.
* Pairwise component flips need not realize a one-unit correction, as
  Proposition 3.2 shows.
* Fractional triangular feasibility and total boundary capacity do not
  imply a Ferrers-shaped integral leave.
* Fixed-clock matching integrality solves only chain selection.  It does not
  serialize the chains into one contiguous-OR word.

No computation or finite search was used.

