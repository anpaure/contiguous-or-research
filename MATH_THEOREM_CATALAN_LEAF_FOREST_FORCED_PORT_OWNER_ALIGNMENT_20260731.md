# Leaf-peelable forced ports are exactly owner-aligned

Date: 2026-07-31  
Status: exact dimension-uniform theorem on a fixed upper transversal; no
all-`m` coherent-tree supply claim

## 0. Verdict

Fix a middle-levels factor and an upper-turn transversal `I` containing all
prescribed upper ports.  Let `Gamma_I` be its bipartite graph between the
cyclic `I`-gaps and the lower-turn colours: a gap `g` is adjacent to a colour
`c` when an occurrence of `c` lies in `g`.

Assume `Gamma_I` is a forest with a perfect matching `M`.  For every
prescribed lower port `j`, let

\[
                 f_j=(g(j),\ell_j)\in E(\Gamma_I),              \tag{0.1}
\]

where `g(j)` is the unique `I`-gap containing `j` and `ell_j` is its lower
turn colour.  Assume, as required by the forced-port theorem, that these
edges have distinct gap and colour endpoints, and write `F={f_j}`.

Then

\[
 \boxed{
 \text{the prescribed ports extend to one joint alternating decoration}
 \quad\Longleftrightarrow\quad F\subseteq M .}                  \tag{0.2}
\]

Thus on the intended leaf-peelable face the residual gap--Hall row is not
an exponential family of inequalities.  It is the literal owner-alignment
test

\[
                 \operatorname{owner}_M(g(j))=\ell_j
                 \qquad(j\in P_B).                               \tag{0.3}
\]

For an all-six coherent hexagon this is three pointwise tests on its lower
ports.  Pairwise-disjoint owner triples automatically supply the required
gap and colour injectivity.

## 1. Forest rigidity

### Lemma 1.1

A forest has at most one perfect matching.

#### Proof

If `M` and `M'` were two distinct perfect matchings, every nontrivial
component of their symmetric difference would be an even cycle alternating
between `M` and `M'`.  A forest contains no cycle.  Hence `M=M'`.  \(\square\)

### Theorem 1.2 (forced-port owner alignment)

Under the hypotheses of Section 0, the residual forced-port graph has a
perfect matching if and only if `F subseteq M`.

#### Proof

If `F subseteq M`, delete the gap and colour endpoints of every edge in
`F`.  The remaining edges of `M` form a perfect matching of the residual
graph.  The forced-port gap--Hall theorem then supplies the required joint
alternating decoration.

Conversely, suppose the prescribed ports extend.  Equivalently, the full
gap graph has a perfect matching `M'` containing `F`.  By Lemma 1.1 the
perfect matching of `Gamma_I` is unique, so `M'=M`, and therefore
`F subseteq M`.  \(\square\)

The conclusion is pointwise.  Merely requiring the three forced colours of
a coherent hexagon to equal the set of three colours owned by its three
gaps is not enough on a forest: a nontrivial permutation would give a second
perfect matching on those six vertices and hence an alternating cycle.

## 2. Exact nonforest extension theorem

The forest theorem is the rigid endpoint of a more general matching
exchange statement.  Let `Gamma` be any balanced bipartite graph with a
perfect matching `M`, and let `F` be a matching of prescribed edges.  Then
`F` is contained in a perfect matching if and only if there is a
vertex-disjoint family of `M`-alternating cycles such that

* every edge of `F setminus M` occurs on the non-`M` half of one cycle; and
* no edge of `F cap M` occurs on the `M` half of a selected cycle.

Indeed, flipping such cycles gives the desired matching.  Conversely, for
any perfect matching `M'` containing `F`, the nontrivial components of
`M triangle M'` are precisely such cycles.

A useful sufficient specialization is the **zero-flux private-block
condition**.  For each coherent hexagon `t`, let `G_t` be its three forced
gaps, `C_t` its three forced lower colours, and `F_t` the three forced port
edges.  If

\[
 |G_t|=|C_t|=3,\qquad F_t:G_t\longrightarrow C_t\text{ is bijective},
 \qquad M(G_t)=C_t,                                  \tag{2.1}
\]

and these blocks are pairwise vertex-disjoint, then replace `M` inside each
block by `F_t`.  The result is a perfect matching containing every forced
port.  Inside a three-by-three block the symmetric difference consists only
of shared edges, alternating four-cycles and alternating six-cycles.

Condition (2.1) is weaker than singleton sockets but stronger than colour
disjointness.  On a forest it collapses back to the pointwise condition
`F_t subseteq M` by Lemma 1.1.

## 3. Smallest shifted-triple obstruction

Owner alignment cannot be replaced by disjoint forced gaps and colours,
interval-convex occurrence geometry, maximum degree two, or existence of an
unforced leaf-peelable decoration.

Take gaps `g_1,...,g_4`, colours `c_1,...,c_4`, and the path

\[
 c_1-g_1-c_2-g_2-c_3-g_3-c_4-g_4.                  \tag{3.1}
\]

Its unique perfect matching is

\[
                 M=\{g_i c_i:1\le i\le4\}.          \tag{3.2}
\]

Force the three distinct port edges

\[
                 F=\{g_1c_2,g_2c_3,g_3c_4\}.        \tag{3.3}
\]

After deleting their endpoints, the residual vertices are `g_4,c_1` and
there is no edge between them.  Thus the forced triple fails Hall.  The
failure is the one-unit matching flux at the two ends of the open
alternating path; there is no alternating cycle on which to close it.

This graph is literally realizable as a gap-occurrence instance by placing
the colour lists

\[
 (c_1,c_2),\quad(c_2,c_3),\quad(c_3,c_4),\quad(c_4) 
                                                               \tag{3.4}
\]

in the four consecutive gaps.  Hence even linear-interval support and a
leaf-peelable base matching do not make a shifted private triple safe.

## 4. Calibration and all-`m` target

The standard positive fixtures lie on the rigid face of Theorem 1.2.

* At `m=4`, the three old private sockets are singleton gaps owned by
  `18,20,24`; the three forced lower ports use those owners.
* In the repaired `m=5` state, the first standard glue has singleton matched
  sockets owned by `82,84,88`, and the second has singleton matched sockets
  owned by `50,52,56`.  The two triples are disjoint.

Therefore their residual Hall success is explained locally by owner
alignment; it is not a separate global coincidence.

The exact sufficient construction target for the leaf-peelable coherent
route is now:

1. choose one upper transversal `I` containing every forced upper port;
2. make `Gamma_I` a leaf-peelable forest; and
3. choose the coherent component tree so that every forced lower port is
   owned by its containing gap in the unique matching of `Gamma_I`.

Under these three conditions the joint SDR is automatic.  This theorem does
not prove that such an `I` and coherent component tree exist for every `m`.
It also does not identify colour/gap privacy with occurrence-router privacy:
the latter remains a separate resource condition unless a node-private
occurrence path to a dedicated sink is supplied.
