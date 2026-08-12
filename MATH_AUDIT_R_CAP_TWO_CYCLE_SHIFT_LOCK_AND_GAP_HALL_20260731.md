# Audit of the cap-two cycle-shift obstruction and gap-Hall rebase

Date: 2026-07-31  
Verdict: PASS, with the scope boundaries below mandatory.

Audited files:

- MATH_THEOREM_R_CAP_TWO_CYCLE_SHIFT_LOCK_AND_GAP_HALL_20260731.md;
- MATH_THEOREM_CATALAN_LINEAR_MATCHING_EXACT_REDUCTIONS_20260731.md;
- MATH_THEOREM_CATALAN_MATCHING_SWITCH_RECTANGLES_AND_GK_EDIT_DISTANCE_20260731.md;
- MATH_THEOREM_CATALAN_MIDDLE_LEVELS_TRACE_DECORATION_EQUIVALENCE_20260731.md;
- MATH_THEOREM_CATALAN_ALTERNATING_TURN_SDR_HALL_AND_M4_COUNTEREXAMPLE_20260731.md;
- MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md; and
- MATH_THEOREM_CATALAN_FOUR_TRANSVERSAL_MATROID_AND_TURN_AUGMENTATION_20260731.md;
- MATH_THEOREM_CATALAN_TRACE_LONG_SWITCH_AUGMENTING_LINKAGE_20260731.md; and
- MATH_THEOREM_CATALAN_BOUNDARY_LINKAGE_GAMMOID_STATE_20260731.md.

## 1. Compound-switch identity

For \(F'=F_0+B\), contraction of the \(c(F_0)\) retained components gives

\[
\begin{aligned}
 \beta(F')
 &=|E(F_0)|+|B|-|V|+c(\Gamma)\\
 &=\beta(F_0)+|B|-c(F_0)+c(\Gamma)\\
 &=\beta(F_0)+\beta(\Gamma).
\end{aligned}
\]

This remains valid when \(F_0\) has old cycle components and when
\(\Gamma\) has loops or parallel edges. Thus contracted acyclicity means no
new cycle; full acyclicity additionally requires \(F_0\) itself to be a
forest. In a cap-two source, that is exactly the condition that the deleted
old half meet every old cycle component. The middle-degree identity is
literal, and a perfect matching preserves both typed palettes.

For simultaneous signed whole-cycle shifts, every deleted cycle vertex is
an isolated retained component and anchors one inserted edge. External
retained components have outdegree zero. In a digraph of outdegree at most
one, an undirected circuit forces every vertex on it to supply one outgoing
circuit edge and is therefore a directed circuit wholly among anchors. This
proves the capacity and graphic rows (3.5)--(3.6).

## 2. Literal \(m=3\) replay

The lower entries in (5.1) enumerate all fifteen pairs. Complementing the
upper entries gives

    56 46 36 26 45 15 13 34 35 25 16 24 12 23 14

which is also a permutation of all fifteen pairs. Every lower entry is
contained in its upper entry, so the table is a perfect diamond matching.

Its lift decomposes as

    cycle: 123-124-145-135-123
    paths: 245-246-126-136-356-256-125
           234-236
           134-346
           235-345-456-146
           156

These components partition all twenty triples. The cycle is the rectangle
with core \(1\), side coordinates \(3,4\) and \(2,5\). Its opposite corners
are \(125,134\), with retained edges \(125-256\) and \(134-346\).
Both forward and backward shifts add two incidences at each corner and give
degree three.

The square exchange

    (12,1234),(13,1235) -> (12,1235),(13,1234)

retains both shore permutations and changes the lifted edges to
\(123-125,123-134\). The five paths in (5.6) partition all twenty triples.
Thus the example is not a counterexample to arbitrary circuit repair.

At \(m=2\), identifying a rank-three upper set by its omitted coordinate
makes a perfect matching a derangement of four symbols. The 4-cycle type
lifts to two paths; the \(2+2\) type lifts to one physical \(C_4\) whose
opposite corners are isolated. Either sign opens the latter. The minimality
claim is valid.

## 3. Middle-levels scope

For a fixed upper turn SDR \(I\), alternation puts exactly one lower
representative in each cyclic \(I\)-gap. Lower bijectivity is exactly a
perfect matching between gaps and the lower colours occurring in them.
This proves (6.3), independently of topology.

The authoritative \({\rm ML}(7)\) example has both turn maps surjective but
three consecutive unique upper occurrences whose intervening lower turns
repeat one colour. Hence it fails gap Hall before the binary trace test. A
shifted matching which remains in the exact support of the same
middle-levels cycle is again a supported perfect matching and uniquely
reconstructs an alternating decoration. Outside that support no trace
conclusion follows.

The middle-levels-resolvable class is strictly smaller than the arbitrary
Catalan linear matching class: the companion \(m=3\) forest has forced
middle-levels support of degree three.

The positive hexagon theorem changes the failed \(m=4\) cycle rather than
solving its impossible fixed gap graph. Its local preservation criterion is
exact: only six port turn colours can change, and alternation inside each
retained fragment survives reversal, leaving precisely the two typed local
palette equalities and the new boundary checks. The displayed repairing
toggle gives a different \({\rm ML}(7)\) cycle with an explicit fourteen-path
decoration, but it is not itself transparent because the old cycle has no
decoration. From the positive cycle, six other Hamilton toggles have common
forest decorations and are transparent for those supplied states. Thus the
recursion must carry a joint decoration and dynamically transparent
boundary/palette state.

## 4. Fixed-cycle connectivity audit

Perfect matchings of the turn-augmentation graph are connected by toggling
the disjoint alternating circuits of their symmetric difference. Each
intermediate object remains a perfect matching of the same graph, so the
fixed-cycle decoration equivalence gives both palette bijections and the
binary-trace theorem gives a cap-two physical lift. No negative-association,
matroid-intersection, or primitive-hexagon claim is used.

The forest endpoint criterion is also exact. With
\(K=\operatorname {Cat}_m\), an alternating cyclic sequence of residual edge
types requires even \(K\), so odd \(K\) makes every decoration linear. For
even \(K\), a forest has two consecutive same-type residual edges. Removing
their endpoints and forbidding internal residual edges on their empty arc
gives the forced-pair graph \(H_C[p,q]\); conversely any perfect matching of
that graph restores the forced pair and supplies the required same-type
consecutive edges. Hence failure of all forced-pair Hall tests is the
complete fixed-support obstruction.

For a gluing sequence, local repairability is not a compositional existence
statement. The exact object is the layered relation of occurrence-labelled
forest matchings. For a tree, leaf-to-root pruning is necessary and
sufficient; merely knowing that each edge relation is nonempty can fail at a
branch whose incident relations support disjoint parent states. This checks
the quantifier in Corollary 6.4 and is why neither an arbitrary SDR nor an
arbitrary gluing tree is enough. A nontransparent Berge repair must also land
outside the physical cycle face; perfect matchability alone does not ensure
this.

## 5. Simultaneous-cube audit

For pairwise vertex-disjoint incidence hexagons, no position belongs to two
local turn updates, so the selected colour-multiset changes add over the
hexagons. Deleting all old hexagon matchings leaves the asserted path atoms.
The nonempty-atom guard is essential: it makes the inward first selected
marks at a seam the actual two consecutive marks; without it, alternation
could depend on a chain of several seam choices. With the guard, every old
seam is valid in the base decoration and every new seam is valid exactly
when its two recorded types differ. Testing singleton toggle sets proves
necessity, and arbitrary subsets prove sufficiency. Thus Theorem 6.5 is
literal.

On formal atom ports, both the atom traversal and the chosen seam set are
perfect matchings. Their alternating cycles are in bijection with factor
components, proving (6.8). The standard voltage development of one quotient
cycle of voltage \(V\) has \(\gcd(h,V)\) components, so (6.9) is exact.
Neither row follows from palette transparency. The common-decoration
intersection (6.10), including its explicit atom-mark guard, rather than
individual nonempty local faces, is therefore the exact static gate. The
affine binary tree interface is a valid sufficient specialization because a
tree has no XOR consistency cycle.

For Corollary 6.7, root the component--hexagon incidence tree at a component.
Every hexagon has one parent branch and two child branches. Processing from
the leaves leaves its own three old edges untouched and places them on three
distinct current cycles; the alternate incidence matching merges the three
opened paths into one cycle. Hence each of the \(s\) toggles lowers the
component count by two. The tree identity \(3s=(2s+1)+s-1\) gives initial
component count \(2s+1\) and final count one. A four-unmarked-position
breaker wholly inside an atom survives every toggle and excludes the final
binary cycle face. The corollary is therefore sufficient exactly as stated;
it says nothing about finding such a tree or common decoration.

## 6. Bounded-linkage audit

For an alternating \(2t\)-circuit, at most \(t\) old augmented edges of
each of the physical-incidence, upper-turn and lower-turn types disappear.
Restricting an old maximum matching of deficiency \(e\) therefore deletes
\(\ell\le3t\) matching edges and leaves a matching of deficiency
\(s=e+\ell\le e+3t\). The maximum matching of the common graph has
deficiency \(r\le s\). The directed-linkage equivalence used in Theorem 6.8
does not require the restricted matching to be maximum: symmetric difference
with a perfect matching gives exactly \(s\) disjoint augmenting paths.
Re-maximizing in the common graph gives the minimal width \(r\).

For the literal simple-circuit augmented graph, the sharper \(2t\) charge is
also valid. If \(a\) deleted physical-incidence edges belong to the old
matching, they occupy \(2a\) of the \(2t\) switched positions. Every selected
deleted turn-occurrence edge must use a distinct remaining position, giving
\(a+(2t-2a)\le2t\). Parallel occurrence labels do not affect the argument.
For abstract rewrites with extra deletions away from the switched positions,
only the frozen \(3t\) edge-count bound is asserted.

The family in Proposition 6.9 replays literally. In the common graph
\(H_n\), \(x_0\) and \(y_0\) are exposed and \(M_n\) is maximum of
deficiency one. The old edge \(x_0y_0\) gives one perfect graph. Replacing it
by \(x_ny_0\) gives another, whose unique augmenting path follows the entire
chain and has length \(2n+1\). This proves globality of the paths even for a
perfect parent and a one-edge replacement, without claiming a Catalan
embedding.

The bounded-adhesion composition is exact by restriction and gluing of
oriented path fragments. It certifies only the augmented matching. A
linkage can change the selected occurrence matching globally, so gap-forest
acyclicity, physical parity, atom marks, endpoint sockets and voltage must be
evaluated on the same repaired matching (6.16). This verifies that the
combined state in Corollary 6.10 has the correct simultaneous quantifier.
The behavioral boundary \(B=S\cup T\cup V(A)\) is information-complete:
restricting a global linkage to the common graph gives a member of
\({\cal L}_H(B)\), and adjoining the bounded new-edge set \(A\) reconstructs
the linkage. Pairwise reachability is not enough because it does not encode
vertex-disjointness. The numerical bounds \(2e+12t\) and \(2e+10t\) follow
respectively from \(r\le e+3t\), \(r\le e+2t\), and
\(|V(A)|\le2|A|\le6t\).
For an adhesion of geometric size \(b\), a safe endpoint-pattern parameter
is \(p=b+2r+2|A|\), or \(b+2r\) when every new edge is already internal to a
named block. The bound \(4^p p!\) safely counts all oriented partial
pairings. Tree composition is exact by enumeration of the realized
relation; the audit does not claim that every prescribed pairing profile is
produced by one ordinary max-flow call.

## 7. Final scope

Proved:

- exact capacity and contracted-graphic tests for any specified compound
  alternating switch;
- exact no-new-cycle versus full-acyclicity distinction;
- failure of universal canonical forward/backward descent at \(m=3\);
- the private-opposite-corner criterion for a rectangle cycle;
- exact gap Hall in the fixed middle-levels subclass;
- transparent-hexagon preservation and the positive \(m=4\) ordinary-hex
  repair;
- cap-two alternating-circuit connectivity inside one fixed
  turn-augmentation graph;
- the exact forced-pair Hall obstruction to forest reachability in that
  fixed support;
- simultaneous transparency for any guarded family of vertex-disjoint
  hexagons;
- the exact atom-transition component and quotient-voltage rows;
- the literal connected incidence-tree Hamilton gluing criterion;
- the exact \(e+3t\) linkage-width bound and its literal-circuit
  \(e+2t\) refinement; and
- exact bounded-adhesion composition of the oriented linkage signature.

Not proved:

- existence of a forest perfect matching for every \(m\);
- cap-two reconfiguration connectivity outside one fixed middle-levels
  support;
- an all-\(m\) accepting transparent-gluing state; or
- protected connectors, deeper shadows, residence, or compilation.

No \(W/2\) Greene--Kleitman linear-subforest bound is used. The only GK
quantity cited is the corrected \(\Delta_m\) theorem and its audited
asymptotic constant.
