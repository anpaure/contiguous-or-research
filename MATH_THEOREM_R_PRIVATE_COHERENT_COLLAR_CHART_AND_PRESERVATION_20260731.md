# Private coherent collars: owner-masked charts, automatic closure, and preservation

Date: 2026-07-31  
Status: exact dimension-uniform conditional theorem and sharp orthogonality
obstructions; no all-\(m\) private-collar supply

## 0. Verdict

On the leaf-peelable prepared face, the common Hall and router gates are no
longer abstract optimization problems.

Fix one occurrence-labelled joint decoration \(D\), with upper transversal
\(I\), leaf-forest gap graph \(\Gamma_I\), and unique matching \(M\).
For every coherent transition chart \((H,d,e)\):

* retain a chart vertex \(x\) exactly when the rank-\((m-1)\) upper-turn
  occurrence \(H+x\) belongs to \(I\); and
* retain an arc \(x\to y\) exactly when the forced lower-turn edge at the
  rank-\(m\) occurrence \(H+x+y\) is the literal \(M\)-owner edge of its
  \(I\)-gap.

Then directed triangles in this **owner-masked chart** are exactly coherent
all-six hexagons whose six ports already belong to \(D\).  In one chart
these triangles are port-disjoint and their forced owner edges are disjoint,
so forced Hall is automatic.

The remaining topology/resource filter is literal.  Keep only triangles
whose component effect is a nonloop merge edge and whose occurrence source
has a node-private route.  If these private coherent collars form a
component-spanning tree, their zero-flux owner blocks close forced Hall,
their private paths close router resilience, and every tree order is an
accepted fixed-\(D\) transparent gluing list.

Colour/gap privacy and occurrence-route privacy are orthogonal.  A shifted
owner triple can fail Hall despite a private route, while two owner-aligned
tree edges can fail resilience by sharing one router vertex.  Thus the exact
remaining all-\(m\) problem is supply of one joint private coherent collar
tree, not another Hall or router theorem.

## 1. Coherent transition charts

Let \(\Omega=[2m-1]\), \(m\ge3\), and let \(F\) be a simple spanning
two-factor of the middle-levels graph.  For

\[
 H\in{\Omega\choose m-2},\qquad e\in H,\qquad d\in\Omega\setminus H,
\]

let \({\cal T}_{H,d,e}\) be the loopless digraph on
\(\Omega\setminus(H\cup\{d\})\) with

\[
 x\longrightarrow y
 \quad\Longleftrightarrow\quad
 (H+x+d)-(H+x)-(H+x+y)-((H-e)+x+y)
 \text{ is a factor path}.                          \tag{1.1}
\]

The chart is partial-functional and has no directed two-cycle.  Its directed
three-cycles are exactly the coherent all-six incidence hexagons with common
external-add label \(d\), common external-delete label \(e\), and core
\(H\).

Across all charts the exact arc ledger is

\[
 \sum_{H,d,e}|E({\cal T}_{H,d,e})|
 =2{2m-1\choose m-1}(m-2)
 =(m+1)(m-2)\operatorname {Cat}_m.                  \tag{1.2}
\]

The average is only \(2/(m-1)\) arcs per chart.  Same-chart directed
triangles are vertex-disjoint and have disjoint physical ports and forced
colour faces.  These facts are proved in
MATH_THEOREM_R_DECORATION_CONDITIONED_COHERENT_ROUTER_AND_RETHREAD_MERGE_SEPARATION_20260731.md.

## 2. The owner-masked chart

Now fix a joint alternating decoration \(D\) of \(F\).  Let \(I\) be its
selected upper-turn occurrences.  Assume the associated
**occurrence-labelled** gap--lower-colour multigraph \(\Gamma_I\) is a
forest, and let \(M\) be its unique occurrence-labelled perfect matching.

For a chart vertex \(x\), let

\[
                         p_x=H+x                    \tag{2.1}
\]

be its named rank-\((m-1)\) upper-turn occurrence.  Retain \(x\) exactly
when \(p_x\in I\).

For a chart arc \(x\to y\), let

\[
 q_{xy}=H+x+y,
 \qquad
 f_{xy}=\bigl(g(q_{xy}),(H-e)+x;q_{xy}\bigr),       \tag{2.2}
\]

where \(g(q_{xy})\) is the cyclic \(I\)-gap containing the named
rank-\(m\) occurrence \(q_{xy}\).  The second expression is the literal
occurrence-labelled forced lower-turn edge.  Retain the arc exactly when
both endpoint vertices survive and \(f_{xy}\in M\).  The occurrence label
is essential when one lower colour occurs more than once in one gap; a
collapsed gap--colour edge does not identify the physical port.  Denote the
resulting digraph by
\({\cal T}^{D}_{H,d,e}\).

### Theorem 2.1 (owner-masked triangle equivalence)

Directed three-cycles of \({\cal T}^{D}_{H,d,e}\) are in bijection with
coherent all-six hexagons in chart \((H,d,e)\) whose six forced port
occurrences all belong to the same decoration \(D\).

Moreover, all directed triangles in one owner-masked chart may be selected
simultaneously: their six-port sets are disjoint and the union of all their
forced lower-port edges is a subset of \(M\).

#### Proof

By the chart theorem, a directed cycle

\[
                         a\to b\to c\to a
\]

is exactly one coherent all-six hexagon.  Its three upper-turn occurrences
are \(p_a,p_b,p_c\), which belong to \(I\) precisely because the three
vertices survived the mask.  Its three lower forced edges are
\(f_{ab},f_{bc},f_{ca}\), which belong to \(M\) precisely because the three
arcs survived.  The leaf-forest owner-alignment theorem says that these are
exactly the conditions for all six prescribed ports to extend through the
fixed decoration.

Conversely, if all six ports of a coherent chart hexagon belong to \(D\),
its rank-\((m-1)\) upper-turn occurrences lie in \(I\).  Since
\(\Gamma_I\) is a forest with unique matching and the forced lower ports
are selected by \(D\), each literal forced edge at the three rank-\(m\)
occurrences lies in \(M\).  Thus all three cycle vertices and arcs survive.

Distinct directed cycles of a partial functional chart are vertex-disjoint.
The chart theorem makes their ports and forced colours distinct.  Since
\(M\) is a matching, their owner edges also have distinct gap endpoints.
Their union is therefore a subset of \(M\), proving simultaneous
installation. \(\square\)

This theorem collapses forced-port Hall to a local triangle mask.  It does
not say that the triangle is a merge, that enough triangles exist, or that
their occurrence routes are private.

## 3. Private coherent collars

A **private coherent collar** relative to \((F,D,M)\) is a directed triangle
\(t\) of an owner-masked chart together with:

1. a genuine nonloop effective edge \(c_t\) between two current factor
   components;
2. its zero-flux owner block

   \[
   G_t=\{g(q_{ab}),g(q_{bc}),g(q_{ca})\},\quad
   C_t=\{(H-e)+a,(H-e)+b,(H-e)+c\},
   \quad F_t=\{f_{ab},f_{bc},f_{ca}\}\subseteq M;   \tag{3.1}
   \]

3. one occurrence-router source \(s_t\) and a named path \(P_t\) from
   \(s_t\) to a dedicated sink;
4. its complete correlated signature for the prepared collective cube.

For collars from different charts, require their port and owner blocks to be
vertex-disjoint.  On one owner-masked chart this disjointness is automatic.

### Theorem 3.1 (automatic private coherent-tree closure)

Let \({\cal B}\) be a bank of private coherent collars such that:

1. its component multigraph is connected;
2. all forced owner blocks are pairwise disjoint;
3. all named occurrence paths \(P_t\) are pairwise vertex-disjoint, end at
   distinct sinks, and avoid every private block router; and
4. the entire bank, not merely each singleton collar, satisfies H0--H5 on
   every component-forest subset; in particular its physical resources are
   disjoint or explicitly capacity-checked and its prefix reachability is
   the prepared redundant row.

Then every component spanning tree \(T\subseteq{\cal B}\), in every edge
order, is an executable fixed-\(D\) transparent component-spanning list.

#### Proof

Coherence and Theorem 2.1 make all selected collars simultaneously
\(D\)-transparent.  Since each \(F_t\subseteq M\) and the blocks are
disjoint, deleting their matched endpoints leaves the restriction of \(M\)
as a perfect residual matching.  Forced Hall is therefore automatic.

For a router deletion \(Y\), pairwise path disjointness lets \(Y\) kill at
most \(|Y|\) of the tree routes.  Deleting that many edges from a tree
creates at most \(|Y|+1\) components.  Hence

\[
                         c(K^D_Y)\le |Y|+1.          \tag{3.2}
\]

The private-tree router theorem gives the same conclusion blockwise, and
the ordered fixed-decoration theorem makes every tree order executable.
\(\square\)

The theorem remains valid off the leaf-forest face when every block obeys
the more general zero-flux identity

\[
                         M(G_t)=C_t                 \tag{3.3}
\]

and the blocks are disjoint.  More generally, one may supply the exact
vertex-disjoint \(M\)-alternating-cycle packing which inserts all
\(F_t\setminus M\) and deletes none of \(F_t\cap M\).

## 4. Preservation through a preliminary rethread

The ML(7) calibration shows that transparent rethreading and component
merging are separate.  A preliminary rethread may nevertheless preserve a
later private coherent tree under an exact exported signature.

### Theorem 4.1 (private-collar preservation)

Let \(R:F\to F'\) be a component-neutral fixed-\(D\) transparent rethread.
Let \({\cal B}\) be a named private coherent-collar bank for \(F\).
Suppose:

1. \(D\) remains leaf-peelable on \(F'\): its new gap graph
   \(\Gamma'_I\) is a forest with unique matching \(M'\);
2. every named collar remains an alternating coherent hexagon with the same
   six selected port occurrences, remains a nonloop effective component
   edge, and passes the prepared H0--H5 state;
3. every forced lower port of every collar is still selected by \(D\);
4. the named occurrence routes, their distinct sinks, owner-block
   disjointness and all private physical resources survive.

Then the same named bank is a private coherent-collar bank relative to
\((F',D,M')\), and Theorem 3.1 applies unchanged.

#### Proof

Fixed-\(D\) transparency preserves every selected port occurrence.  In the
new leaf forest, \(D\)'s selected lower occurrences form a perfect matching.
Uniqueness forces that matching to be \(M'\), so every forced lower-port
edge is owner-aligned automatically.  Hypothesis 2 preserves coherence and
nonloop topology, while hypothesis 4 preserves the private router damage
budget and all remaining prepared resources. \(\square\)

A convenient stronger sufficient condition is literal equality of the
exported collar signature

\[
 (H,d,e;\hbox{ six named ports};c_t;
  \hbox{ owner block};P_t,\hbox{ sink};
  \hbox{ prepared physical state}).                 \tag{4.1}
\]

Fixed-\(D\) transparency by itself is not enough.  A rethread can preserve
the decoration while changing a leaf forest into a cyclic gap graph or
changing the later external port edges.  In that case owner alignment and
coherence must be recomputed, using alternating-cycle packing off the forest
face.

## 5. The two private resources are orthogonal

### Proposition 5.1 (owner alignment does not imply router privacy)

Take three factor components joined by two coherent collar edges in a path.
Let their forced owner blocks be disjoint subsets of one leaf-forest
matching \(M\).  If both occurrence sources must traverse one unit router
vertex \(v\), deleting \(v\) kills both tree edges and leaves three
components:

\[
                         3>|\{v\}|+1=2.
\]

Forced Hall passes, but router resilience fails.

### Proposition 5.2 (router privacy does not imply owner alignment)

Let the leaf gap graph be the path

\[
 c_1-g_1-c_2-g_2-c_3-g_3-c_4-g_4
\]

with unique matching \(M=\{g_ic_i:1\le i\le4\}\).  Force the disjoint edges

\[
                         g_1c_2,\quad g_2c_3,\quad g_3c_4.       \tag{5.1}
\]

Give the collar a completely private occurrence route.  The route row
passes, but the forced edges form an open alternating path with one unit of
flux.  Deleting their endpoints leaves unmatched \(g_4,c_1\), so forced
Hall fails.

These are exact independent obstructions.  No theorem from colour/gap
privacy to occurrence-route privacy, or conversely, is available.

## 6. Quantitative supply boundary

The unmasked chart theorem gives at most

\[
 { (m+1)(m-2)\operatorname {Cat}_m\over3}
\]

coherent triangles globally and a port-conflict neighbourhood at most
\(12m-29\).  These estimates remain only prefilters.  Owner masking may
delete every triangle, surviving triangles may all be component-neutral
rethreads, and their router paths may share a small cut.

Within one owner-masked chart, however, every surviving directed triangle
is already gap/colour private relative to every other surviving triangle.
Thus the remaining selection there is exactly:

1. filter for genuine nonloop component effects;
2. choose a connected component-edge subbank; and
3. assign node-private occurrence routes.

If the whole filtered bank has globally pairwise-disjoint routes and a
connected component graph, any spanning tree closes by Theorem 3.1.

## 7. Exact finite scope and remaining lemma

The repaired \(ML(7)\) cycle has six fixed-decoration transparent Hamilton
rethreads, exactly four of which are all-six coherent.  Its 15 splitting
toggles have no common componentwise decoration.  It supplies no private
coherent merge edge.

Item 2171 separately supplies the positive \(m=4\) owner-aligned merge path

\[
                         [18]-g-[20]-g-[24],
\]

and the repaired \(m=5\) standard sockets use the disjoint owner triples
\(\{82,84,88\}\) and \(\{50,52,56\}\).  These calibrate the owner-aligned
and zero-flux faces only; absent a separate router certificate, they do not
certify node-private occurrence paths or recursive supply.

The exact all-\(m\) target is now:

> construct or preserve one leaf-peelable decoration whose owner-masked
> coherent charts contain enough genuine nonloop triangles to connect all
> factor components, with pairwise-disjoint zero-flux owner blocks and a
> node-private occurrence route for every selected tree edge.

A preliminary rethread is allowed only with Theorem 4.1's exported
signature or a complete recomputation.  Residence, deeper shadows,
socket/primitive voltage, Pascal reachability and the common-\(Q\) compiler
remain downstream.  No coefficient-one theorem is claimed.

## 8. Authoritative dependencies

* MATH_THEOREM_CATALAN_LEAF_FOREST_FORCED_PORT_OWNER_ALIGNMENT_20260731.md
* MATH_THEOREM_CATALAN_PRIVATE_TREE_AUTOMATIC_HALL_AND_ROUTER_20260731.md
* MATH_THEOREM_CATALAN_COHERENT_ALLSIX_TRANSPARENT_HEX_20260731.md
* MATH_THEOREM_CATALAN_TRANSPARENT_ROUTER_RESILIENCE_CRITERION_20260731.md
* MATH_THEOREM_CATALAN_ORDERED_FIXED_D_TRANSPARENT_GLUING_AFTER_ROUTER_20260731.md
