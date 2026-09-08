# Rainbow matching cycle breaking is a four-matroid gate

Date: 2026-08-01  
Lane: Thread D, upper representatives / rooted-link forest  
Status: exact alternating-packet characterization, exact smallest projection
counterexample, and exact tractable sufficient faces.  No all-dimensional
Catalan-forest existence claim is made.

## 0. Verdict

Let `D=(V,E)` be a directed labelled multigraph.  Each arc `e` has a tail
`t(e)`, a head `h(e)`, and an upper colour `c(e)` in a set `C` of size `U`.
Assume that a set `F` of `U` arcs already exists such that

* `c:F->C` is a bijection;
* the tails of `F` are distinct; and
* the heads of `F` are distinct.

Thus `F` is a colour-saturating head/tail rainbow matching.  This does not
imply that its rooted links are a forest.  The arcs of `F` form a directed
partial permutation, so every component is a directed path or a directed
cycle.  Graphic independence is exactly the absence of the cycle
components, including a two-cycle made from opposite parallel links.

The exact selection problem is a common independent set of size `U` in
four matroids on `E`:

\[
  M_C\quad\text{(upper colours)},\qquad
  M_T\quad\text{(tails)},\qquad
  M_H\quad\text{(heads)},\qquad
  M_G\quad\text{(rooted graphic)}.                      \tag{0.1}
\]

Consequently neither ordinary matching, Rado's rainbow-forest theorem, nor
two-matroid intersection closes the gate.  The two-colour example in
Section 4 has both a full head/tail rainbow matching and a full
colour-rainbow forest, but no set satisfying both.

There is nevertheless an exact exchange theorem.  Relative to any initial
rainbow matching `F`, delete a set `R` meeting every directed cycle and put
`F_0=F-R`.  The deleted colours can be restored without losing matching or
acyclicity exactly when the four matroids in (0.1), contracted by `F_0` and
restricted to those colours, have a common independent set of size `|R|`.
This gives both the exact obstruction and the minimum exchange radius.  A
one-edge-per-cycle packet is valid precisely when this condition holds for
some `R` of size equal to the number of cycles.

For the middle-levels rooted-link problem, a successful output has `U`
edges on `W` vertices and therefore exactly

\[
                         W-U=\operatorname{Cat}_m       \tag{0.2}
\]

directed path components.  Only after this cycle-breaking gate is closed do
the free component ports exist.  On an acyclic connector reservoir, the
remaining rooted-link completion is the already proved one-defect Hall row.

## 1. Four exact matroids

Let `M_C,M_T,M_H` be the partition matroids whose parts are respectively
the colour, tail and head fibres.  Let `M_G` be the cycle matroid of the
underlying labelled multigraph obtained from `D` by forgetting arc
orientation.  Opposite arcs between the same two vertices remain parallel
labelled edges.

### Theorem 1.1 (rooted rainbow-forest equivalence)

There is a colour-saturating head/tail matching whose rooted links are a
forest if and only if

\[
       \max\{|I|:I\in M_C\cap M_T\cap M_H\cap M_G\}=U. \tag{1.1}
\]

#### Proof

Independence in the first three matroids says at most one arc of each
colour, tail and head.  At size `U`, colour independence saturates all `U`
colour parts.  Independence in `M_G` is exactly rooted-link acyclicity.
\(\square\)

If `I` is independent in the first three matroids, every vertex has
indegree and outdegree at most one.  Hence an undirected cycle in `I` is
coherently directed, apart from the allowed length-two opposite-arc case,
which is still a directed two-cycle.  Therefore

\[
             r_G(I)=|I|-z(I),                            \tag{1.2}
\]

where `z(I)` is the number of directed cycle components.

The exact integer formulation of (1.1) is

\[
\begin{aligned}
 x_e&\in\{0,1\},\\
 \sum_{c(e)=a}x_e&=1 &&(a\in C),\\
 \sum_{t(e)=v}x_e&\le1,
 &\sum_{h(e)=v}x_e&\le1 &&(v\in V),\\
 \sum_{e\in E[S]}x_e&\le |S|-1
             &&(\varnothing\ne S\subseteq V).
\end{aligned}                                           \tag{1.3}
\]

The last row includes parallel two-cycles.  It is the precise rooted-link
forest condition, not a later topological preference.

## 2. Exact alternating-packet theorem

Fix a full rainbow matching `F`, and optionally fix a protected set
`P subseteq F` which must remain literal.  For `R subseteq F-P`, put

\[
                         F_0=F-R.                       \tag{2.1}
\]

Call `R` a **cycle cut** when it meets every directed cycle component of
`F`; equivalently, `F_0` is a forest.  Let

\[
        E_R=\{e\in E:c(e)\in c(R)\}.                    \tag{2.2}
\]

Contract `F_0` in all four matroids and restrict them to `E_R`.  Loops in a
contracted tail or head partition are precisely arcs using an already
occupied port; loops in the contracted graphic matroid are precisely arcs
whose endpoints already lie in one `F_0` component.

### Theorem 2.1 (balanced exchange criterion)

There is a full colour-saturating head/tail rainbow forest `F'` containing
`P` if and only if there are a cycle cut `R subseteq F-P` and a set
`A subseteq E_R` of size `|R|` which is independent in

\[
 M_C/F_0,qquad M_T/F_0,qquad M_H/F_0,qquad M_G/F_0.   \tag{2.3}
\]

Then

\[
                         F'=F_0\cup A.                  \tag{2.4}
\]

#### Proof

If (2.3) holds, colour independence at size `|R|` uses every colour of
`R` once.  Tail and head independence preserve the matching, and graphic
independence makes (2.4) a forest.  Its colour set is the complete set `C`,
and it retains `P`.

Conversely, given `F'`, take

\[
                  R=F-F',\qquad A=F'-F.                \tag{2.5}
\]

Both full sets use every colour once, so `c(A)=c(R)` and `|A|=|R|`.
Their common part `F_0=F\cap F'` is a subforest of `F'`, hence `R` meets
every cycle of `F`.  The four independence statements follow by
contracting this common part.  \(\square\)

Define

\[
 \nu_F(R)=\max\{|A|:A\subseteq E_R\text{ is independent in all four
                    contractions in (2.3)}\}.           \tag{2.6}
\]

The exact obstruction functional is

\[
 \Delta_P(F)=
   \min_{\substack{R\subseteq F-P\\F-R\text{ a forest}}}
          \bigl(|R|-\nu_F(R)\bigr).                    \tag{2.7}
\]

A protected rainbow forest exists exactly when `Delta_P(F)=0`.  The minimum
exchange radius is the least `|R|` among the zero-defect terms.  If `F` has
`z(F)` cycles, every cycle cut has size at least `z(F)`.  Thus a minimal
three-/four-/long-circuit search should first enumerate one edge per cycle
and test (2.3); enlarging `R` is necessary only after every such term has
positive defect.

The formula is exact, but `nu_F(R)` is a four-matroid common-independence
number.  It is not supplied by a rank-sum min--max theorem.

### Immediate protected obstruction

If one directed cycle of `F` is contained entirely in `P`, no cycle cut
`R subseteq F-P` exists.  Hence no forest retaining all of `P` exists.  More
generally, every protected solution must leave at least one removable edge
on every current cycle.

## 3. Legal one-edge descent and compound exchanges

Let `Z` be a directed cycle of a rainbow matching `F`, let `e in Z-P`, and
let `f` have the same colour as `e`.  Removing `e` turns `Z` into a directed
path and frees one outgoing and one incoming port.

### Lemma 3.1 (one-edge cycle breaker)

The swap

\[
                       F-e+f                            \tag{3.1}
\]

is a rainbow matching with one fewer cycle if and only if

1. the tail of `f` is unused in `F-e`;
2. the head of `f` is unused in `F-e`; and
3. those two endpoints lie in distinct components of the underlying
   forest part of `F-e`.

#### Proof

The first two conditions are exactly the tail/head matching rows.  Under
them, adding `f` creates an undirected cycle precisely when its endpoints
already lie in one path component.  If they lie in different components,
no new cycle is created, while removing `e` destroyed `Z`.  The colour row
is preserved because `c(e)=c(f)`.  \(\square\)

Thus ordinary matching-alternating cycles are not sufficient: they may
change the colour multiset.  A legal compound packet must be balanced in
three partitions.  If it removes `R` and inserts `A`, then exactly

\[
\begin{aligned}
 c(A)&=c(R)\quad\text{as multisets},\\
 t(A)&\text{ and }h(A)\text{ are injective and avoid the ports of }F-R,\\
 \bar\lambda(A)&\text{ is a forest after contracting }F-R             
\end{aligned}                                           \tag{3.2}
\]

are required.  These are the literal alternating-exchange equations behind
(2.3).  The exchange object is a three-partite hypercircuit on
colour/tail/head incidences with an additional graphic row, not merely an
alternating cycle in the tail--head bipartite graph.

An iterative descent theorem follows immediately: if every nonforest
rainbow matching containing `P` has a legal swap from Lemma 3.1, repeated
swaps terminate at a forest because the nonnegative integer `z(F)` drops at
every step.  The hypothesis is substantive and is false in general.

## 4. Smallest separation of the two easy projections

Take vertices `1,2,3`, colours `red,blue`, and arcs

\[
 e:1\to2\ (\mathrm{red}),\qquad
 f:2\to1\ (\mathrm{blue}),\qquad
 g:1\to3\ (\mathrm{blue}).                             \tag{4.1}
\]

Then

\[
                         F=\{e,f\}                      \tag{4.2}
\]

is a full colour-saturating head/tail rainbow matching, but its rooted links
form a two-cycle.  On the other hand

\[
                         G=\{e,g\}                      \tag{4.3}
\]

is a full colour-rainbow graphic forest, but it repeats tail `1`.  These are
the only two ways to choose one edge of each colour.  Hence no full common
independent set exists.

This proves sharply that the conjunction

\[
\boxed{
 \text{full head/tail rainbow matching exists}
 \quad+\quad
 \text{full Rado rainbow forest exists}}
                                                               \tag{4.4}
\]

does not imply the desired joint object.  The example is properly coloured
as a bipartite tail--head graph: the two blue edges are disjoint.  Therefore
proper-colour/Latin-transversal structure alone does not remove the
obstruction.

For the starting matching (4.2), removing `f` exposes the blue alternatives
`f,g`: `f` fails the graphic contraction and `g` fails the tail contraction.
Removing both edges does not help.  Thus (2.7) has positive defect for every
cycle cut.

## 5. What two-matroid min--max and Brualdi--Ryser do prove

If the tail/head rows are discarded, Rado--Edmonds gives the exact
colour--graphic value

\[
 \max_{I\in M_C\cap M_G}|I|
   =\min_{X\subseteq E}
       \bigl(r_C(X)+r_G(E-X)\bigr).                     \tag{5.1}
\]

Thus one edge of every upper colour can be chosen acyclically exactly when
the right side is at least `U`; equivalently, every colour subfamily has
enough graphic rank in its available union.

If colour and graphic rows are discarded, tail--head selection is ordinary
bipartite matching and has the Hall/Konig min--max theorem.  Similar
rank-sum formulas hold for every chosen pair among the four matroids.
Example (4.1) shows that simultaneous equality in these projections does
not imply equality in (1.1).

A colour-saturating head/tail matching is a transversal in a properly
edge-coloured bipartite graph.  Brualdi--Ryser-type Latin-transversal
theorems concern this projection, usually in a complete Latin-square host
and sometimes only up to a one-cell deficit.  They neither apply to an
arbitrary sparse rooted-link graph nor impose (or even see) the graphic
matroid.  In the present task their conclusion has already been assumed,
and (4.1) shows that this strongest possible projection still does not break
cycles.

Generic common independence of three partition matroids already contains
three-dimensional matching.  Adding `M_G` cannot acquire an Edmonds-style
rank min--max without additional structure.  Therefore a claimed proof must
exhibit one of the tractable structures below, rather than invoke ordinary
matroid intersection or a Latin transversal theorem.

## 6. Exact tractable faces

### 6.1 Support-first directed linear forest

Suppose a directed linear forest `R subseteq E` covers every colour, and a
protected subforest `P subseteq R` has distinct colours.  Choose the
prescribed edge of every colour used by `P` and any carrying edge of `R` for
each remaining colour.  The chosen set is a subset of `R`, so tails, heads
and graphic independence are automatic.  It is the required rooted Catalan
forest.  This is the cleanest exact positive reduction.

### 6.2 Acyclic replacement support with automatic ports

Fix a cycle cut `R_0` of an initial matching and put `F_0=F-R_0`.  If all
candidate replacements lie in one directed linear forest relative to
`F_0`—that is, their union with `F_0` already has injective ports and is
graphic-independent—then (2.3) reduces to the ordinary colour-cover row.
One carrying edge per missing colour suffices.

If only graphic acyclicity is automatic, a colour-saturating head/tail
rainbow matching is still required.  There is no Hall theorem for that
three-partite problem in general.  If the tail assigned to every missing
colour is fixed and distinct, it reduces to an ordinary colour-to-head
matching, and Hall becomes exact.

### 6.3 Acyclic connector reservoir after the forest exists

Once a rooted Catalan forest `Q_0` exists, it has `C=Cat_m` directed path
components and one free incoming/outgoing port per component.  If the
admissible component connector digraph is acyclic, a matching of size
`C-1` is automatically one directed Hamilton path.  Hence its exact
criterion is

\[
                     |N(X)|\ge |X|-1                   \tag{6.1}
\]

for every set of outgoing component ports (after contracting any protected
connector paths).  This one-defect Hall theorem is downstream of, and does
not replace, the cycle-breaking problem in Sections 1--5.

## 7. Rooted middle-levels specialization

Fix a perfect incidence matching `M_0`.  For an incidence `e=LV` outside
`M_0`, the rooted arc and its upper colour are

\[
 \lambda(e):L\longrightarrow M_0^{-1}(V),\qquad
 \operatorname{up}(e)=M_0(L)\cup V.                    \tag{7.1}
\]

Put `V=binom([2m-1],m-1)` and let the colours be the rank-`m+1` sets.  A
head/tail rainbow matching saturating all `U` upper colours is a directed
partial permutation with `U` arcs on `W` vertices.  If it has `z` cycle
components, then its total number of rooted components is

\[
                     W-U+z=\operatorname{Cat}_m+z.      \tag{7.2}
\]

It is a rooted Catalan forest exactly when `z=0`; then it has precisely
`Cat_m` directed path components.  A cycle has no free head or tail port,
so it cannot be postponed to the Catalan connector stage.  At least one
colour representative on that cycle must participate in a balanced packet
from Theorem 2.1.

For a protected pivot path chosen in the correlated predecessor phase, the
protected arcs are already a directed subforest.  The exact remaining gate
is therefore (1.1) after contracting that path.  If an initial full rainbow
matching is available, (2.7) is the sharp cycle-breaking diagnostic.  Once
it reaches zero, the rooted-link forest condition and the component count
are automatic, and the only topology row left is the downstream
one-defect connector Hall condition (6.1).

## 8. Precise surviving theorem

The assumption in the task closes only the three partition rows.  To finish
the rooted Catalan stage one must prove at least one of:

1. every cycle-bearing full rainbow matching has a legal one-edge descent
   from Lemma 3.1;
2. for some cycle cut `R`, the exact four-contraction deficit in (2.7)
   vanishes;
3. a support-first directed linear forest covering every upper colour
   exists; or
4. a special structural theorem reduces the replacement candidates to a
   fixed-tail Hall instance.

Without such structure, Brualdi--Ryser and ordinary matroid intersection
are projection theorems only.  The two-colour instance (4.1) is the smallest
exact obstruction.
