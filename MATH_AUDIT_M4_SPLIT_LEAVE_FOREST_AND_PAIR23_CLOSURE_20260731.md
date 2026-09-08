# The exact split-leave forest normal form and the fixed PAIR23 closure obstruction at \(m=4\)

Date: 2026-07-31  
Status: exact equivalence and complete fixed-forest obstruction; no general
\(m=4\) existence or nonexistence verdict

## 1. Exact normal form

Put

\[
 \mathcal L=\binom{[8]}3,\qquad
 \mathcal M=\binom{[8]}4,\qquad
 \mathcal U=\binom{[8]}5.
\]

Thus

\[
 |\mathcal L|=|\mathcal U|=56,\qquad |\mathcal M|=70,
 \qquad K=70-56=14.
\]

For a Johnson edge \(xy\) in \(\mathcal M\), call \(x\cap y\) its lower
colour and \(x\cup y\) its upper colour.

### Theorem 1.1 (split-leave linear-forest equivalence)

The following data are equivalent.

1. An oriented saturating cycle on 56 members of \(\mathcal M\), using every
   upper colour once, together with an injective host for each of its 14
   omitted facets, such that:

   * the base lower word has profile \(0^{14}1^{28}2^{14}\);
   * inserting every omitted facet in its host block and uniformly cutting
     the incoming split edge repairs the lower palette exactly; and
   * the 14 cut lower colours are distinct.

2. A spanning linear forest \(F\subset J(8,4)\) with 14 paths such that
   every member of \(\mathcal L\) is a lower edge colour once and every
   member of \(\mathcal U\) is an upper edge colour once, together with:

   * an orientation \(t_j\leadsto h_j\) of every path, with \(n_j\) the
     neighbour of its tail \(t_j\); and
   * a cyclic permutation \(\sigma\) of the 14 paths for which

     \[
       h_jt_{\sigma(j)}\in E(J(8,4)),\qquad
       h_j\cup t_{\sigma(j)}
        =t_{\sigma(j)}\cup n_{\sigma(j)}.                 \tag{1.1}
     \]

   Define

   \[
   \alpha_{\sigma(j)}=h_j\cap t_{\sigma(j)},\quad
   \beta_{\sigma(j)}=t_{\sigma(j)}\cap n_{\sigma(j)},\quad
   d_{\sigma(j)}=h_j\cap n_{\sigma(j)}.                  \tag{1.2}
   \]

   Then the \(\alpha_j\) are distinct, the \(d_j\) are distinct, and

   \[
                         \{d_j:j<14\}\cap
                         \{\beta_j:j<14\}=\varnothing.   \tag{1.3}
   \]

#### Proof

Start with the data in (1). Subdivide every hosted cycle edge through its
omitted facet. This gives a Hamilton cycle \(P\) on all 70 middle facets.
Delete the 14 incoming split edges. These edges are vertex-disjoint: their
omitted endpoints are distinct and their used-seam endpoints are distinct.
A cycle cut at this matching is therefore a 14-path spanning forest.
Between two consecutive cuts the path begins at the omitted endpoint of
the earlier cut and ends at the used-seam endpoint of the later cut. Hence
every path has exactly one omitted tail.

The directed repair identity says exactly that the retained lower colours
are \(\mathcal L\), once each. Host subdivision preserves upper colour
blockwise, so the retained upper colours are \(\mathcal U\), once each.
The deleted incoming edges close the oriented paths in one cycle and give
(1.1). Their lower colours are the \(\alpha_j\). The retained outgoing
colours are the \(\beta_j\). Suppressing the omitted tail replaces
\(\beta_j\) by \(d_j\).

The suppressed base word has 14 holes and 14 duplicates. There are exactly
14 replacements. Thus the removed colours \(\beta_j\) enumerate the 14
holes, while the inserted colours \(d_j\) enumerate the 14 duplicates.
They are individually distinct and disjoint. This proves (2).

Conversely, add the 14 closure edges in (1.1) to \(F\). The cyclic
permutation makes the result one 70-cycle. Suppress every tail \(t_j\).
Equation (1.1) says that its two neighbours are distinct facets of the same
5-set, so suppression replaces the two incident edges by one Johnson edge
of that upper colour. Because \(F\) was upper-rainbow, the resulting
56-cycle is upper-rainbow.

The lower palette of \(F\) is initially \(\mathcal L\). Suppression removes
the distinct colours \(\beta_j\) and inserts the distinct, disjoint colours
\(d_j\). Its base profile is therefore exactly \(0^{14}1^{28}2^{14}\).
Reinsert the tails and cut the incoming closure edges: this reverses those
14 replacements and restores \(\mathcal L\). The incoming colours are the
distinct \(\alpha_j\), completing (1). \(\square\)

The important orientation consequence is literal: **one omitted tail per
path is necessary**. A mere perfect matching of the 28 endpoints is not a
uniform directed repair if some path has zero or two designated tails.

## 2. Complete obstruction for the frozen PAIR23 complement-path factor

The fourteen five-vertex paths in
MATH_THEOREM_D4_PAIR23_PORT_FACTOR_20260726.md span all 70 middle facets,
use every upper colour once, and have lower profile

\[
                         0^{14}1^{28}2^{14}.             \tag{2.1}
\]

Thus they are a natural finite structural seed, although they are not the
two-sided-rainbow forest required in Theorem 1.1.

For each of their 28 endpoints \(x\), let \(x'\) be its sole path neighbour
and let \(U_x=x\cup x'\). Put a directed closure arc \(x\to y\) when

\[
       xy\in E(J(8,4)),\qquad x\cup y=U_x,               \tag{2.2}
\]

and \(x,y\) belong to different paths. The direction designates \(x\) as
the omitted tail: the new closure edge repeats the upper colour of its
first path edge.

### Theorem 2.1 (fixed PAIR23 no-go)

The literal graph (2.2) has:

\[
 \begin{array}{c|r}
 \text{directed arcs}&46\\
 \text{underlying edges}&46\\
 \text{perfect endpoint matchings}&185\\
 \text{matchings whose contracted path graph is connected}&30.
 \end{array}                                             \tag{2.3}
\]

No perfect matching designates exactly one tail on every path. Indeed the
number of paths with one tail has histogram

\[
 0^2,\quad2^{40},\quad4^{102},\quad6^{24},\quad8^{17}    \tag{2.4}
\]

over all 185 matchings. Among the 30 connected matchings it has histogram

\[
                  2^1,\quad4^{15},\quad6^{10},\quad8^4. \tag{2.5}
\]

Consequently this fixed forest has no coherent uniform-outgoing closure,
even before imposing the lower-colour, alpha-rainbow, or leaf-peeling
conditions.

#### Proof

The deterministic audit constructs all 46 literal arcs from (2.2). No
underlying edge is bidirectional. Minimum-residual-degree recursion then
enumerates every perfect matching of the 28 ports. For every matching it
counts designated tails path by path and independently tests connectivity
of the contracted 14-vertex path graph. The exhaustive counts are
(2.3)--(2.5), whose maximum one-tail count is eight. Theorem 1.1 requires
fourteen. \(\square\)

This is only a fixed-forest obstruction. It does not exclude another
two-sided-rainbow forest, another complement-path factor, or an unrestricted
saturating cycle.

## 3. Compact exact search model

There are only 560 Boolean diamonds \([R,U]\), with

\[
 R\in\mathcal L,\qquad U\in\mathcal U,\qquad R\subset U.
\]

Selecting a diamond selects the Johnson edge between its two middle
corners. Introduce one binary variable for each diamond and impose:

\[
 \sum_{U\supset R}x_{R,U}=1\quad(R\in\mathcal L),
 \qquad
 \sum_{R\subset U}x_{R,U}=1\quad(U\in\mathcal U),        \tag{3.1}
\]

and, for every \(X\in\mathcal M\),

\[
 1\le\sum_{R\subset X\subset U}x_{R,U}\le2.             \tag{3.2}
\]

Equations (3.1)--(3.2) have 560 variables and the pairwise/triple CNF used
by the probe has 44,422 clauses. Degree summation forces 28 degree-one and
42 degree-two middle vertices. Lazy clauses excluding each selected cycle
therefore leave exactly fourteen paths. The remaining gate is finite:
enumerate the \(2^{14}\) path orientations and solve the 14-vertex directed
Hamilton-cycle problem (1.1), propagating the colour conditions
(1.2)--(1.3).

The staged probe is

    scratch/laneL_search_m4_double_rainbow_forest_closure_20260731.py

A PASS is not accepted from solver variables alone. The probe reconstructs
the 70-cycle, suppresses the 14 tails, verifies all 56 upper colours,
verifies the literal \(0^{14}1^{28}2^{14}\) base profile, verifies the
exact retained lower and upper palettes, and constructs the full repair
hypergraph for a leaf-peeling diagnostic. The script is staged for bounded
proof discovery; no complete forest census is claimed here.

## 4. Exact recursive seed interface

The positive \(m=3\) repair core embeds literally after adjoining one new
coordinate \(a\):

\[
 X\mapsto X+a,\qquad d\mapsto d+a,\qquad h\mapsto h+a,
 \qquad (C_i,U_i,C_{i+1})\mapsto
 (C_i+a,U_i+a,C_{i+1}+a).                               \tag{4.1}
\]

Fixing the six old host blocks with indices

\[
                         \{1,2,3,7,9,13\}               \tag{4.2}
\]

preserves all seven viable hyperedges of the positive five-token core.
Since \(\operatorname{Cat}_4-\operatorname{Cat}_3=14-5=9\), the sharp
unitriangular lift target is nine new matching ears. If those nine ears
can be ordered so that each has a degree-one pivot when peeled, and deleting
their three shores and all incident edges leaves **exactly** the lifted
five-token core (not merely a supergraph containing it), Lemma 5.2 of
MATH_THEOREM_CATALAN_DIRECTED_REPAIR_HYPERGRAPH_FLOW_20260731.md proves
the whole \(m=4\) core leaf-peelable.

The 560-variable forest CNF does not currently accept this as a direct warm
start: the old host triples live in the suppressed saturating cycle and are
known only after the endpoint closure is chosen. The seed belongs naturally
in the integrated block/host model, where (4.1)--(4.2), the five old omitted
facets, and the five old duplicate/hole colours can be fixed before search.

## 5. Reproduction

Run

    python3 scratch/audit_m4_pair23_uniform_closure_obstruction_20260731.py

The canonical payload SHA-256 printed by the audit is

    56f697dd7df2e840b28c539214ace8447ccf71fd947b0cc7555ca8963fbd7f97

The complete scope is the literal 28-port closure graph of the displayed
PAIR23 forest. No heuristic edge deletion or colour prefilter occurs.
