# Audit: literal age-window flow and corrected facet-module spread

Date: 2026-08-02  
Lane: K, independent proof/scope audit

## 1. Verdict

Both submitted notes are mathematically sound after the local scope repairs
recorded below.  They close two exact marginal layers:

1. fixed-matching, fixed-root, single-depth age-label allocation is a
   capacitated bipartite flow and hence totally unimodular; and
2. completely labelled facet blocks have an exact weighted greedy packing
   theorem at scale $W/(18q^3)$.

Neither result rounds the correlated common chronology or gives an
additive-constant construction.

## 2. Literal age-window contraction

Let $k=2m+1$, let $M$ be a perfect incidence matching from rank $m$
to rank $m+1$, and put

\[
 q\longrightarrow M(q)-\{a\},\qquad a\in q.
\]

The labelled contraction is $m$-regular in both directions.  A selected
length-$d$ resident window records distinct old departures
$a_0,\ldots,a_{d-2}$, and its depth-$j$ intersection is exactly

\[
              q_0-\{a_0,\ldots,a_{j-1}\}.
\]

Consequently the role/root exact flow equations plus one predecessor and
one successor per selected window are equivalent to a literal all-high
cycle cover.  The usual root cuts are exactly the additional one-component
condition.  This is a fixed-$M$, all-high statement; mixed ages and a
choice of $M$ require a larger joint system.

### 2.1 Coordinate law and cap

On every cyclic component, coordinate-$x$ arrivals equal departures.
Root exactness therefore gives

\[
 D_x=B_x(M):=|\{q:M(q)-q=\{x\}\}|.
\]

The incidence word of \(x\) has positive runs of length at least \(d\).
Across all roots it has \(\binom{2m}{m-1}\) positive positions, so

\[
 D_x\le\left\lfloor{\binom{2m}{m-1}\over d}\right\rfloor.
\]

A fixed-depth prescribed jump $S+\{x\}\supset S$ consumes a distinct
$x$-departure.  Jumps at different offsets cannot simply be added, since
one physical departure occurs in several overlapping windows.

### 2.2 Balanced matching and the TU face

Cyclic parenthesis cancellation has one unmatched zero on every rank-$m$
word.  Adding it is an incidence bijection, equivariant under the free
$\mathbb Z_{2m+1}$-action.  Thus every coordinate is added exactly

\[
 {1\over2m+1}\binom{2m+1}{m}=\operatorname{Cat}_m
\]

times.  This matching meets every coordinate cap for $d\le m$ and extends
to an SCD, but it need not have a Hamilton contraction or a feasible common
age flow.

After this matching, a concrete chain-to-root assignment and one deck
offset are fixed, allowed departures form the network

\[
             s\longrightarrow q\longrightarrow x\longrightarrow t.
\]

The exact feasibility criterion is

\[
 |R|\le\sum_{x\in\bigcup_{q\in R}A_j(q)}c_x
 \qquad(R\text{ a free-root family}),
\]

and the node--arc matrix is TU.  Automatic feasibility is proved only for
the unforced lists and for a *concrete* rotation-equivariant nonempty list
system.  A rotation-symmetric fractional average of Ferrers factors does not
supply such a system.

### 2.3 Exact non-TU boundary

For $m\ge3,d\ge3$, take three rooted flags with target/root incidence
matrix

\[
 \begin{array}{c|ccc}
       &f_1&f_2&f_3\\ \hline
 S     &1&0&1\\
 T     &1&1&0\\
 q     &0&1&1
 \end{array}.
\]

Its determinant is two.  Thus identifying two proper depth layers into one
rooted-window column already destroys network TU.  The head-bijection rows,
resident overlap and subtour cuts are additional, separate couplings; none
is used in this minor.  At $d=2$ the displayed two-depth minor is absent,
so it must not be advertised as an absolute first non-TU row in that case.

The coordinate-overload construction is a genuine integral obstruction for
arbitrary prescribed static chains.  The $J(5,2)$ argument is also sound,
but only for the all-high depth-two resident Hamilton/rainbow-upper face.  It
does not refute mixed-age or fractional traces.

## 3. Corrected facet-module ledger

Use $d\ge2$, $q=d+2\ge4$, $c=r-d-1\ge1$.  In the separated Ferrers
range (safely $c-1>d$), a length-$q$ module consumes one
$e_{d+1}$, $q-1$ copies of $e_{d-1}$, $d$ units of $L-H$, $q$
owners, one target at ranks $c,c+1$, and $q$ targets at every rank
$c+2,\ldots,r-1$.  A length-$(q+1)$ module adds one unit to every latter
row.  Hence an inventory with $t$ modules, $B$ of the longer type,
necessarily satisfies

\[
\begin{aligned}
 t&\le A_{d+1},\\
 (q-1)t+B&\le A_{d-1},\\
 dt+B&\le E=L-H,\\
 qt+B&\le n_{c+2}.
\end{aligned}
\]

Here \(n_{c+2}\) is the available target inventory; it is
\(\binom{k}{c+2}\) only in the unreserved full-deck face.

The exact binomial ratios give

\[
 {A_{d-1}\over A_{d+1}}\to1,
 \qquad
 {qA_{d+1}\over\binom{k}{c+2}}\to{\pi\over2}>1,
 \qquad
 {q^2A_{d-1}\over(q-1)W}\to{\pi\over2}e^{-\pi/4}.
\]

Thus $t=A_{d+1}$ is impossible for a buffered target-simple inventory,
and the buffer-coordinate ceiling is $O(W/q^2)$.  Other ledger rows can
make the available count smaller, even zero.

### 3.1 Exact joint greedy theorem

For the completely labelled candidate family, transitivity gives the exact
conflict load

\[
 \Gamma={q^2\over W}+{1\over K_c}+{1\over K_{c+1}}
       +\sum_{j=2}^{q-2}{q^2\over K_{c+j}}.
\]

The union-bound greedy proof is exact: every integer $t$ with
$(t-1)\Gamma<1$ has pairwise owner/named-target-disjoint labelled
candidates.  With a preused bank the sufficient row is
$\Psi+(t-1)\Gamma<1$.  Canonically

\[
 \Gamma\sim1.33703\,{q^3\over W},\qquad
 \Gamma\le17{q^3\over W}
\]

eventually, so every $t\le\lfloor W/(18q^3)\rfloor$ is selected.

This theorem co-selects the owner block, cyclic order and target labels.  It
does **not** allocate the primitive or short-buffer source occurrences and
does not discharge $dt+B\le E$.  Physical use remains conditional on the
complete ledger.

### 3.2 Growing-uniformity boundary

After stripping independent labels, the natural object is a labelled
multihypergraph; reversing a cyclic order duplicates a resource edge.
Quotienting that uniform multiplicity leaves the degree ratios unchanged.
For $q\ge5$ and nested high targets $P\subset Q$ of ranks $r-2,r-1$,

\[
 {\deg(P,Q)\over\deg(Q)}={2\over r-1},\qquad
 {\deg(P,Q)\over\deg(P)}={2\over k-r+2}.
\]

The $q\ge5$ condition is necessary: for $q=4$, rank $r-2=c+1$ is a
low target omitted from this high-target hypergraph.  If
$R=q(q-2)$ is the edge size and $D=X_0q/K_{c+2}$ the maximum degree,
then

\[
 {R\Delta_2\over D}
 \ge {2q(q-2)\over r-1}{K_{c+2}\over K_{r-1}}
 \longrightarrow {\pi\over2}e^{-\pi/4}>0.
\]

Therefore a growing-uniformity theorem requiring
$R\Delta_2/D=o(1)$ cannot be imported from pair codegree alone, although
$\Delta_2/D=\Theta(q^{-2})\to0$.  This is not an obstruction to a
specialized interval-chain nibble or absorber.

## 4. Accepted combined boundary

The exact remaining age row is a correlated choice of central matching,
chain/root assignment, common resident windows, head bijection and subtour
connectivity.  The exact remaining facet row is actual buffer allocation
plus joint interval-chain block/order/label selection up to the required
inventory size.  OFHT chronology, mixed residence, upper decks, protected
interfaces and the compiler remain downstream.

Neither theorem implies $B(k)+O(1)$, coefficient one, or any $O(1)$
defect bound.

## 5. Hashes

| note | submitted SHA-256 | corrected SHA-256 |
|---|---|---|
| `MATH_THEOREM_LITERAL_AGE_WINDOW_CONTRACTION_FLOW_AND_COORDINATE_CAP_20260802.md` | `b3f87adaeef3310f47376e243328f56f6ee4af7991f4132d97ff507e0b2193b1` | `f7a987063e8e5eac3be8db85bf21d98316db15156446d4fc77aac56507ebe63a` |
| `MATH_THEOREM_FACET_MODULE_LEDGER_AND_WEIGHTED_JOINT_GREEDY_SPREAD_20260802.md` | `b7f7fbd9895b503785735a3b407d9fd120f0e02a0fcd8cb9e865c8bd0f197f87` | `3656e91e24372624f420e17c011c3a69944d0c0d490f9aeb3040159cf7f9d2f0` |

The corrected hashes above are the hashes immediately after the scope
repairs.  They must be refreshed if either source note is edited again.
