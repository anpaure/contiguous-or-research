# The two-coordinate anchor topology: exact pairing criterion, zipper construction, and guarded cycle transport

Date: 2026-07-31  
Lane: R, integral `a=1` balanced-subcube recursion  
Status: exact all-parameter topology theorem for the **isolated common-port
/ prefix-bank normal form**.  This closes the abstract coupling of two side
path forests once their anchor pairings may be chosen.  It does **not**
prove that Boolean containment matchings realize the required pairings.
For an arbitrary inherited-tail/head common basis, retained child segments
add a third partial matching between distinct left and right label copies;
that more general topology is treated in
`MATH_THEOREM_CATALAN_SIDE_ANCHOR_PAIRING_TOPOLOGY_DECOUPLING_20260731.md`.

## 0. Rebased scope

Let

\[
 K=\operatorname {Cat}_n,
 \qquad C=\operatorname {Cat}_{n+1},
 \qquad h=C-K.
\]

The automatic two-coordinate common-basis theorem closes synchronized
incidence.  In the prefix-bank specialization the chosen central port
vertices are isolated and the two seams through each port suppress to one
direct side-to-side attachment.  The remaining central `a=1` question is
physical.  On each
shore one needs a spanning path forest with exactly `h` components and
`C` distinct seam anchors, every anchor having side degree at most one.
The two shores are then coupled labelwise by the `C` common ports.

This note proves four exact statements.

1. Each side forest is completely summarized for coupling purposes by a
   partial matching on the `C` port labels.
2. The contracted attachment graph is a path forest if and only if the
   union of the two colored partial matchings is a forest.
3. Given only the two numbers of zero-anchor side components, an acyclic
   abstract coupling exists if and only if one sharp scalar inequality
   holds.  In particular, two minimum-charge side forests always admit an
   explicit alternating zipper.
4. If a supplied physical side forest has cycles in its anchor coupling,
   cycle removal is an alternating free-socket transport problem.  A
   guarded strict-gammoid/Rado inequality is an exact selection criterion
   for the serializable transport subclass.

Path ordering or reversal alone never changes the partial matching and
therefore cannot repair a bad coupling.

## 1. From side components to colored anchor matchings

Let `Q` be the common port-label set, `|Q|=C`.  For
`epsilon in {-,+}`, let `G^epsilon` be a spanning path forest with exactly
`h=C-K` components.  It has pairwise distinct anchor vertices

\[
                 b^\epsilon(q)\qquad(q\in Q),          \tag{1.1}
\]

each of degree at most one in `G^epsilon`.

A nontrivial path has only two vertices of degree at most one, and an
isolated component contains only one vertex.  Hence every component of
`G^epsilon` contains zero, one, or two anchors.  Define a partial matching
`A_epsilon` on `Q` by

\[
 qq'\in A_\epsilon
 \quad\Longleftrightarrow\quad
 b^\epsilon(q),b^\epsilon(q')
 \text{ lie in the same two-anchor component}.         \tag{1.2}
\]

Let `a_epsilon` be the number of zero-anchor components and let
`r_epsilon=|A_epsilon|`.

### Lemma 1.1 (exact charge)

For each shore,

\[
                  \boxed{r_\epsilon=K+a_\epsilon}.     \tag{1.3}
\]

In particular `r_epsilon<=floor(C/2)`.

#### Proof

If `s_epsilon` is the number of one-anchor components, then

\[
 a_\epsilon+s_\epsilon+r_\epsilon=h,
 \qquad s_\epsilon+2r_\epsilon=C.
\]

Subtracting gives
`r_epsilon-a_epsilon=C-h=K`.  The matching bound is immediate. `square`

Now contract every component of the two side forests and join the two
components containing `b^-(q)` and `b^+(q)` by an edge labelled `q`.
Call the resulting bipartite multigraph `J`.  Zero-anchor components are
isolated and may be retained or omitted.

Define the two-colored multigraph

\[
                  H=(Q,A_-\sqcup A_+),                 \tag{1.4}
\]

where a pair belonging to both matchings occurs twice, once in each color.

### Theorem 1.2 (line-graph normal form)

The following are equivalent.

1. `J` is a forest.
2. `J` is a path forest.
3. `H` is a forest.
4. There is no nonempty `S subseteq Q` on which both partial involutions
   `A_-` and `A_+` are everywhere defined and preserve `S`.
5. The labels can be ordered component by component so that the first label
   of each component has no earlier mate and every later label has exactly
   one earlier mate among its two colors.

#### Proof

Every vertex of `J` has degree at most two, because its side component has
at most two anchors.  Thus a forest `J` is automatically a path forest.

The vertices of the edge-line multigraph of `J` are its labels `q`.  Two
labels are adjacent through a minus component exactly when their pair is in
`A_-`, and similarly on the plus shore.  Consequently this line multigraph
is exactly `H`.  A maximum-degree-two multigraph contains a cycle if and
only if its line multigraph does; this includes a parallel pair, which is a
2-cycle on both sides.  Hence (1)--(3) are equivalent.

Every component of `H` is an alternating path or an alternating cycle.
An alternating cycle has a vertex set `S` of the kind in (4).  Conversely,
on a finite nonempty invariant `S`, every vertex has one edge of each
color, so `H[S]` contains an alternating cycle.  This proves (3)<->(4).

If `H` is a path forest, order the vertices of every path from an endpoint;
the asserted earlier-mate rule follows.  Conversely, the last vertex of
any cycle has two earlier mates, contradicting the rule.  Thus (3)<->(5).
`square`

Condition (4) is the sharp parity/closure obstruction.  Its smallest
instance has two labels `q,q'` paired together on both shores.  All local
degree and side-forest conditions pass, but `J` has two parallel edges and
the physical lift has a cycle.  Reversing either side path or permuting the
side components leaves (1.2) unchanged, so endpoint order alone cannot
remove this obstruction.

## 2. Exact numerical existence and the alternating zipper

Forget Boolean containment for this section and ask only whether two
partial matchings of prescribed sizes can be put on the common label set
so that their colored union is a forest.

### Theorem 2.1 (abstract anchor-pairing min--max)

Let `C>=1` and let `0<=r_-,r_+<=floor(C/2)`.  There exist matchings
`A_-,A_+` on a common `C`-set, of sizes `r_-,r_+`, for which
`A_- sqcup A_+` is a forest if and only if

\[
                         r_-+r_+\le C-1.               \tag{2.1}
\]

#### Proof

Necessity follows because the colored union is a multigraph on `C`
vertices with `r_-+r_+` edges.

For sufficiency suppose first that `r_->r_+`.  Put
`d=r_--r_+>=1` and distribute the `r_+` plus-colored edges arbitrarily as
nonnegative integers `t_1+...+t_d=r_+`.  For each `i`, make an alternating
path having `t_i+1` minus edges and `t_i` plus edges.  These paths use

\[
             \sum_i(2t_i+2)=2r_-\le C
\]

vertices.  Leave the remaining labels isolated.  The case `r_+>r_-` is
dual.

If `r_-=r_+=r>0`, make one alternating path with `r` edges of each color;
it uses `2r+1<=C` vertices by (2.1).  The zero case is empty. `square`

Combining (1.3) with Theorem 2.1 gives the exact scalar topology face.

### Corollary 2.2 (zero-component budget)

Two side forests with zero-anchor counts `a_-,a_+` admit *some* abstract
relabelled acyclic coupling if and only if their individual matching bounds
hold and

\[
              \boxed{a_-+a_+\le C-2K-1}.              \tag{2.2}
\]

If equality is violated by one, namely
`a_-+a_+=C-2K`, then every nonisolated contracted side component has degree
two and `J` is a disjoint union of cycles.  This is an unavoidable
topological obstruction, independent of label order.

#### Proof

Insert `r_epsilon=K+a_epsilon` in (2.1).  On the stated equality face the
number of nonisolated vertices of `J` equals its `C` edges.  Every such
vertex has degree at least one and at most two; the degree sum is `2C`, so
every degree is two. `square`

The best recursive face is `a_-=a_+=0`.  It is always abstractly feasible.

### Corollary 2.3 (symbolic alternating zipper)

For `n>=2`, two minimum-charge side forests (`a_-=a_+=0`) have
`r_-=r_+=K`, and the following common endpoint pattern is acyclic.  Choose
distinct labels

\[
                 q_0,q_1,\ldots,q_{2K}in Q
\]

and put

\[
\begin{aligned}
 A_-&=\{q_{2i}q_{2i+1}:0\le i<K\},\\
 A_+&=\{q_{2i+1}q_{2i+2}:0\le i<K\}.
\end{aligned}                                          \tag{2.3}
\]

Their union is the single path
`q_0-q_1-...-q_(2K)`; all other labels are unpaired on both shores.  Thus
they lie in one-anchor side components, not necessarily isolated physical
components.

#### Proof

The Catalan recurrence gives

\[
 C-2K={2(n-1)\over n+2}K\ge1.
\]

Thus the displayed `2K+1` labels exist.  Equation (2.3) is visibly an
alternating path. `square`

For the audited parameters `n=3,...,7`, the global zero-component budgets
`C-2K-1` are respectively

\[
                         3,13,47,164,571.              \tag{2.4}
\]

These large abstract margins do not prove that containment diagonals can
realize the zipper pairs.

## 3. A guarded alternating exchange criterion

Fix a minus pairing `alpha=A_-` and a physically realized plus pairing
`beta=A_+`.  Let `E^+` be a declared catalogue of plus-shore pairs that can
replace an existing plus pair while preserving the diagonal palettes,
physical degrees, and all non-topological guards.  The next lemma is purely
topological; physical validity is a hypothesis on `E^+`.

### Lemma 3.1 (one free socket opens one cycle)

Suppose `x` is unmatched by `beta`, `yz in beta` lies on an alternating
cycle of `alpha sqcup beta`, and `xy in E^+`.  If `x` lies outside that
cyclic component, then

\[
                    \beta'=\beta-yz+xy               \tag{3.1}
\]

is a matching of the same size and `alpha sqcup beta'` has one fewer
cyclic component and no new cycle.  The free plus socket moves from `x` to
`z`.

#### Proof

Deleting `yz` opens the old alternating cycle into a path with endpoints
`y,z`.  Since `x` is beta-free, it has degree at most one in
`alpha sqcup beta` and is an endpoint or isolate of a different path
component.  Adding `xy` joins the two paths.  It cannot close a cycle, all
degrees remain at most two, and `z` is the new beta-free endpoint. `square`

Iterating Lemma 3.1 transports a free socket along an alternating exchange
path and spends it to open a cycle.  For simultaneous, independently
installable exchanges, this has an exact Rado formulation.

Build a directed exchange network `D_beta` whose vertices are possible
locations of the beta-free label.  An arc `x -> z` carries a fixed
certificate `xy in E^+`, `yz in beta` for the replacement
`yz -> xy`.  Impose the following **serializability hypothesis** on the
catalogue:

* every simple directed path from the declared source bank is certified as
  a whole monotone cycle-opening route: before its terminal step it moves
  the free socket only through path components, touches none of the original
  cycles, and at the terminal step deletes an edge of its assigned cycle;
  all matching labels are distinct and every prefix passes the
  contracted-graphic test; and
* vertex-disjoint directed paths have disjoint physical supports and their
  replacements commute.

Thus guarding and monotonicity are part of the path-catalogue theorem,
rather than being inferred from abstract reachability.  For each current
alternating cycle `Z`, let `T_Z` be the terminal states of routes assigned
to `Z`.  Let `S` be a bank of beta-free labels in pairwise distinct private
path components.

### Theorem 3.2 (guarded Rado cycle-opening criterion)

Under the serializability hypothesis above, all current cycles
can be opened simultaneously by component-disjoint exchange paths if and
only if

\[
       r_{D_\beta,S}\!\left(\bigcup_{Z\in\mathcal Z'}T_Z\right)
                    \ge |\mathcal Z'|
       \qquad(\mathcal Z'\subseteq\mathcal Z),          \tag{3.2}
\]

where `r_(D_beta,S)(T)` is the maximum number of pairwise vertex-disjoint
directed paths from distinct sources in `S` to distinct vertices of `T`.
After the toggles, the anchor coupling is a path forest.

#### Proof

Reachable terminal sets in a directed graph with source bank `S` form the
strict gammoid on the terminal vertices.  Choosing one terminal from each
part `T_Z` is a Rado transversal in that gammoid.  Rado's theorem gives
exactly (3.2).  The paths are component-disjoint and guarded, so their
matching toggles commute.  Each terminal toggle deletes one edge of its
assigned cycle; Lemma 3.1 and the prefix graphic tests show that no new
cycle is created.  All original cyclic components are opened. `square`

Condition (3.2) is exact only for the declared serializable exchange
catalogue.  Failure is a genuine guarded rank cut for that catalogue, not a
no-go for larger side-forest rethreadings.  Without privacy/serializability,
the simultaneous choice contains three-resource matching/graphic
correlation and is not reduced here to ordinary matroid intersection.

## 4. Exact remaining all-parameter theorem

The automatic common-basis theorem supplies a common deletion basis and
both incidence matchings.  The all-parameter `a=1` recursion would now
follow from either of the following strictly physical statements.

* **Direct zipper realization.**  Realize the two diagonal containment
  bases as side forests whose two-anchor component pairings have the form
  (2.3), or more generally obey Theorem 1.2.
* **Guarded exchange realization.**  Produce any two side forests obeying
  the degree caps, together with a plus- or minus-shore exchange catalogue
  satisfying (3.2).

The numerical Catalan charge supplies ample abstract room, but it does not
force either physical statement.  The smallest surviving obstruction is
not Hall incidence: it is a closed alternating anchor set, beginning with
the two-label parallel-pair obstruction, for which no containment-valid
free-socket exchange leaves the side palettes and forest guards intact.
