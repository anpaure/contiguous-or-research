# Protected upper-exact Hamilton paths and robust rooted-tail extension

Date: 2026-08-01  
Lane: protected Catalan connector / additive-one owner layer  
Status: exact equivalence and exact protected Hall extension.  Simultaneous
head injectivity and graphic connectivity remain open.

## 0. Outcome

Put

\[
 W={2m-1\choose m},\qquad
 U={2m-1\choose m+1},\qquad
 C=W-U={2W\over m+1}=\operatorname {Cat}_m .          \tag{0.1}
\]

Fix a perfect matching `M0` in the middle-levels incidence graph `ML_m`
between ranks `m-1` and `m` of `[2m-1]`.  For an incidence `e=LV` outside
`M0`, retain the rooted labels

\[
 \operatorname{up}(e)=M_0(L)\cup V,
 \qquad
 \lambda(e)=L\longrightarrow M_0^{-1}(V).             \tag{0.2}
\]

The additive-one owner-layer target has an exact simpler form.  It does not
need a residual closure.

> A matching `Q subset ML_m-M0` is the short shore of a spanning
> alternating Hamilton path exactly when `|Q|=W-1` and its rooted links
> form a spanning tree.  Requiring its adjacent-upper colours to be
> surjective adds only `up(Q)=binom([2m-1],m+1)`.

Equivalently, select one occurrence of every upper colour to obtain a rooted
Catalan forest `Q0`, and then select exactly `C-1` connector incidences whose
links form a **directed free-port Hamilton path** after the `C` components of
`Q0` are contracted.  Equivalently, they form a spanning tree together with
the tail/head matching constraints.  There is no final residual matching
and no protected closure edge.

There is also an unconditional protected extension theorem for the first
half of this object.  Relative to any fixed `M0`, any at most `m` prescribed
distinct upper-colour/root-tail tickets extend to a complete injection of
all rank-`m+1` upper colours into distinct rooted tails.  The proof is one
Kruskal--Katona shadow inequality plus Hall.  Therefore a fixed bank of
`3Hh` pivot-path transitions whose upper colours are **globally distinct
across the whole bank** creates no upper-palette/root-tail obstruction
whenever `3Hh<=m`; in particular the numerical bound is automatic under the
already proved planting hypothesis `6Hh<=m-2`.  Owner/lower-colour resource
disjointness alone does not imply this cross-packet upper-colour condition.

The extension is a **semimatching**, not yet the desired `Q0`: two lifted
incidences may have the same head, and their rooted links may branch or
cycle.  The exact remaining central gate is thus

\[
 \boxed{\text{head injectivity + a directed free-port spanning link path,
 jointly with the protected rooted-tail transversal}.} \tag{0.3}
\]

## 1. Rooted Hamilton-path equivalence

The matching property of `Q` implies that every lower vertex is the tail of
at most one rooted link and every lower vertex is the head of at most one
rooted link.  Hence `lambda(Q)` is a directed partial permutation; its
underlying graph has maximum degree at most two.

### Theorem 1.1 (rooted upper-exact Hamilton path)

For `Q subset ML_m-M0`, the following are equivalent.

1. `Q` is a matching of size `W-1` and `lambda(Q)` is
   graphic-independent.
2. `M0 union Q` is a spanning alternating Hamilton path in `ML_m`, with
   endpoints on opposite shores.

Under either condition, the path is adjacent-upper-surjective exactly when

\[
             \operatorname{up}(Q)
                 ={[2m-1]\choose m+1}.                 \tag{1.1}
\]

Conversely, in every spanning alternating Hamilton path the larger of its
two alternating edge classes is a perfect matching `M0`; its other edge
class is a matching `Q` satisfying items 1--2.  Thus (1.1), for that rooted
decomposition, is also necessary for an upper-decorated Hamilton path.

#### Proof

Assume item 1.  The rooted link graph has `W` vertices and `W-1` independent
graphic edges.  It is therefore a spanning tree.  Since `Q` is a matching,
the link tree has indegree and outdegree at most one and consequently
maximum undirected degree at most two.  A tree of maximum degree two is one
spanning path.

Contract every edge of `M0` in `M0 union Q`.  This turns an incidence edge
`e in Q` into exactly its rooted link `lambda(e)`.  Hence the contracted
graph is the spanning link path.  Expanding the pairwise disjoint `M0`
edges yields one spanning alternating path in `ML_m`.  Exactly one lower
vertex is not a `Q` tail and exactly one middle vertex is not a `Q` head, so
these are its opposite-shore endpoints.  This proves item 2.

Conversely, colour the edges of a spanning alternating path by parity.  It
has `2W-1` edges, so the larger colour class has `W` edges and meets every
vertex once; call it `M0`.  The other class `Q` is a matching of size
`W-1`.  Contracting `M0` in the path gives the rooted link path, which is
graphic-independent.  This proves item 1 and the converse statement.

At a lower vertex `L` used by `Q`, its two incident owners in the expanded
path are `M0(L)` and the endpoint `V` of its `Q` edge.  Their union is
literally `up(LV)`.  These are all adjacent-owner turns of the projected
path, so their surjectivity is exactly (1.1).  \(\square\)

### Theorem 1.2 (Catalan forest plus connector tree, no residue)

The following are equivalent.

1. `Q` satisfies Theorem 1.1 and (1.1).
2. There is a disjoint decomposition `Q=Q0 dotunion Q1` such that
   * `Q0` is a rooted Catalan forest: it is a matching, `up` is a
     bijection from `Q0` to the `U` upper colours, and `lambda(Q0)` is a
     forest;
   * `|Q1|=C-1`;
   * `Q0 union Q1` is a matching; and
   * after contracting the `C` components of `lambda(Q0)`, the labelled
     links of `Q1` form a directed Hamilton path through the components,
     using the unique free outgoing port of one component and the unique
     free incoming port of the next.  Equivalently, under the matching
     hypothesis, the contracted links form a spanning tree.

#### Proof

Assume item 1.  Choose one edge of `Q` carrying each upper colour, and call
the resulting `U`-edge set `Q0`.  Every subset of the link path is a forest,
so `Q0` is a rooted Catalan forest.  It has

\[
                     W-U=C                                      \tag{1.2}
\]

components.  Put `Q1=Q-Q0`.  Then

\[
                     |Q_1|=(W-1)-U=C-1.                         \tag{1.3}
\]

Because the full link graph is a spanning tree, contracting the `Q0`
forest turns `Q1` into a spanning tree on its `C` components.  Every
component of `lambda(Q0)` is a coherently directed path: tail and head
injectivity give indegree and outdegree at most one.  The matching condition
on `Q0 union Q1` permits a connector to use only a free outgoing port and a
free incoming port and leaves component indegree and outdegree at most one.
The contracted spanning tree is therefore one directed Hamilton path.

Conversely, expanding such a free-port path on the components of a forest
gives a forest;
the edge count is

\[
                    U+(C-1)=W-1.                                \tag{1.4}
\]

It is therefore a spanning tree.  The matching condition makes it a rooted
link path as in Theorem 1.1, and `Q0` already supplies (1.1).  \(\square\)

### Protected version

Let `P=P0 dotunion P1` be a protected alternating incidence-path bank,
properly coloured so that `P0 subset M0` and `P1` is required on the short
shore.  Conditional on a certificate `Q` containing `P1`, if the upper
labels on `P1` are globally distinct, then in Theorem 1.2 one may require
`P1 subset Q0`: choose the protected occurrence for each of its upper labels
and choose occurrences from `Q` for the other labels.  This decomposes an
existing protected certificate; it is not an existence proof for one.

For the collared pivot geodesic, one packet has `3h` Johnson transitions,
and hence `3h` protected incidences in each alternating shore.  Its upper
labels are pairwise distinct within that packet.  Thus `H` packets prescribe
`3Hh` rooted upper-tail tickets in `Q0` only when their upper labels are also
distinct across different packets.  Disjoint owner and lower-colour
resources do not by themselves guarantee this extra condition.

The protected statement is an equivalence, not an existence assertion.  It
shows exactly that the additive-one topology asks for a protected Catalan
forest plus `C-1` connectors and nothing afterward.

## 2. A sharp-enough rooted upper-tail expansion

We first isolate the numerical shadow fact used by Hall.

### Lemma 2.1 (one-step central shadow surplus)

Let `X` be a nonempty family of `(m+1)`-subsets of `[2m-1]`, and let
`partial X` be its rank-`m` lower shadow.  Then

\[
                         |\partial X|\ge |X|+m.          \tag{2.1}
\]

#### Proof

Put `k=m+1` and `x=|X|`.  Kruskal--Katona says that `|partial X|` is at
least the numerical lower shadow `partial_k(x)` of the first `x` rank-`k`
sets in colex order.  Here

\[
             1\le x\le {2m-1\choose m+1}
                         ={2k-3\choose k}.              \tag{2.2}
\]

Write the first term of the canonical binomial expansion as

\[
                 x={s\choose k}+b,qquad
                 k\le s\le2k-3,qquad
                 0\le b<{s\choose k-1}.                \tag{2.3}
\]

The remainder colex family of rank `k-1` is supported on at most `s`
points.  Since `s<=2k-3`, its lower shadow has size at least its own size;
this follows directly by double-counting incidences at or above the middle
rank, or by the normalized matching property.  Therefore

\[
                      \partial_{k-1}(b)\ge b.            \tag{2.4}
\]

The Kruskal--Katona formula gives

\[
 \partial_k(x)-x
  =\left[{s\choose k-1}-{s\choose k}\right]
    +\left[\partial_{k-1}(b)-b\right].                  \tag{2.5}
\]

Write `D_s=binom(s,k-1)-binom(s,k)`.  At `s=k`, `D_s=k-1`, and

\[
             D_{s+1}-D_s={s\choose k-2}-{s\choose k-1}\ge0
                 \qquad(k\le s\le2k-3).                \tag{2.6}
\]

Thus (2.5) is at least `k-1=m`, proving (2.1).  \(\square\)

### Theorem 2.2 (protected rooted upper-tail extension)

Fix any perfect incidence matching `M0`.  Let `P` be a family of `t<=m`
prescribed pairs

\[
                  (R,T),\qquad
 R\in{[2m-1]\choose m+1},\quad
 T\in{[2m-1]\choose m},\quad T\subset R,              \tag{2.7}
\]

with all `R` distinct and all `T` distinct.  Then `P` extends to an
injection

\[
 \psi:{[2m-1]\choose m+1}\longrightarrow
                         {[2m-1]\choose m},qquad
                         \psi(R)\subset R.              \tag{2.8}
\]

Equivalently, all upper colours can be assigned to distinct rooted tails
of `M0`, retaining every prescribed ticket.

#### Proof

Delete the `t` prescribed upper vertices and the `t` prescribed rank-`m`
vertices from the containment graph between ranks `m+1` and `m`.  For any
nonempty family `X` of remaining upper vertices, Lemma 2.1 gives

\[
 |N(X)\setminus V(P)|
       \ge |N(X)|-t
       \ge |X|+m-t
       \ge |X|.                                         \tag{2.9}
\]

The empty family is harmless.  Hall's theorem gives a matching saturating
all remaining upper vertices; adjoining `P` gives (2.8).  \(\square\)

### Incidence interpretation and exact scope

For a chosen pair `(R,T)` in (2.8), let

\[
                  L=M_0^{-1}(T),qquad R=T+\{b\}.       \tag{2.10}
\]

Since `L subset T`, write `T=L+{a}`.  Then

\[
                  V=L+\{b\}                            \tag{2.11}
\]

is the unique other middle corner of the diamond `[L,R]`, and

\[
                  e=LV,qquad \operatorname{up}(e)=R.   \tag{2.12}
\]

Distinct `T` give distinct rooted tails `L`.  Hence Theorem 2.2 constructs
an upper-exact rooted-tail **semimatching** containing all protected tickets.

It does not say that the heads `V` in (2.11) are distinct.  If two heads
coincide, the incidences (2.12) are not a matching.  Even when all heads are
distinct, the link graph may contain several components or cycles.  Thus
Theorem 2.2 proves exactly two of the four correlated rows

\[
 \begin{array}{c|c}
 \text{resource}&\text{status}\ \hline
 \text{upper colours}&\text{exact}\cr
 \text{rooted tails}&\text{injective}\cr
 \text{heads}&\text{open}\cr
 \text{graphic spanning tree}&\text{open}.
 \end{array}                                             \tag{2.13}
\]

This scope is essential.  Treating (2.8) as a rooted Catalan forest would
silently assume the head partition row and the graphic matroid row.

## 3. Consequence for the pivot bank

One collared pivot packet contains `3h` Johnson transitions.  After choosing
the alternating root shore, they give `3h` distinct pairs `(R,T)` of the
form (2.7): distinctness of the upper colours and of the rooted owner
occurrences holds within one protected path.  For `H` packets the prescribed
size is `t=3Hh` provided the copies have distinct rooted owners and globally
distinct upper colours.  The small protected-factor theorem can first
supply a compatible alternating perfect class `M0`; it does not create
cross-packet upper distinctness.

Therefore Theorem 2.2 applies whenever

\[
                              3Hh\le m.                 \tag{3.1}
\]

The existing small protected-factor theorem uses the stronger hypothesis

\[
                              6Hh\le m-2,               \tag{3.2}
\]

so every protected bank already in its range and satisfying the global
upper-distinctness hypothesis automatically passes the complete upper-
palette/root-tail Hall row.

Combining Theorems 1.2 and 2.2 gives the sharpened owner-layer frontier:

> Starting from the protected exact upper-tail semimatching, reselect or
> augment it so that the forced other middle corners are also injective and
> the resulting `W-1` rooted links form one spanning path.  Equivalently,
> produce a protected rooted Catalan forest and connect its `C` components
> by exactly `C-1` compatible free-port incidences forming a directed path.

There is no residual closure at additive one, and no further ordinary Hall
row after those connectors.  This does not prove their existence; it removes
the upper-palette/tail matching and final residual-matching rows from the
protected global theorem.

## 4. Relation to the full OR-word problem

The theorem is entirely at the owner/q1/immediate-upper layer.  The pivot
packet itself already supplies its local residence, old-deck transparency,
and exact two-ray compiler.  A global word still has to preserve exterior
residence, arbitrary-width upper witnesses, one terminal common cap, and a
bounded regenerative endpoint state.

Accordingly, the implication proved here is

\[
 \begin{array}{c}
 \text{protected pivot paths}\cr
 \Downarrow\quad\text{(Theorem 2.2)}\cr
 \text{upper-exact rooted-tail semimatching}\cr
 \Downarrow\quad\text{(open head/tree correlation)}\cr
 \text{upper-decorated spanning Hamilton path}\cr
 \Downarrow\quad\text{(separate guarded rows)}\cr
 \text{a length-}B(k)+1\text{ universal word}.
 \end{array}                                             \tag{4.1}
\]

The first arrow is unconditional.  The second and third are not claimed.
