# Independent audit of the fixed-phase odd-diamond augmenter and
# multi-funnel splice

Date: 2026-08-01  
Audited files:

* `MATH_THEOREM_ODD_DIAMOND_TIGHT_ONE_TO_TWO_AUGMENTER_20260801.md`;
* `MATH_THEOREM_OWNER_LAYER_ONE_TO_TWO_AUGMENTER_AND_MULTIFUNNEL_SPLICE_20260801.md`.

Verdict: **PASS with the fixed-`M_0`, private-linkage, simultaneous-versus-
serial, and provider-versus-connector scopes stated in the companion
theorem.**

## 1. Local set and phase audit

The ranks in the augmenter are correct: `L,L'` have rank `m-1`;
`A,B,C,D` have rank `m`; and `R,S` have rank `m+1`.  The four owners are
pairwise distinct.  Direct substitution gives

\[
 A\cup C=S,\qquad A\cup B=R,\qquad C\cup D=S.                       \tag{1.1}
\]

The old and target diamonds share only owner `A`.  Therefore a single first
matching can orient both with the retained occurrence only when
`M_0(L)=A`.  The rerouted diamond has owners `C,D`, so exactly two rows are
possible:

\[
 M_0(L')=C=L'+x
 \quad\hbox{or}\quad
 M_0(L')=D=L'+a.                                                    \tag{1.2}
\]

Writing `P=M_0^{-1}(B)`, `H=M_0^{-1}(C)` and
`Q_D=M_0^{-1}(D)` gives exactly

\[
\begin{array}{c|c}
 C\text{-phase}&L\to L'\ \mapsto\ L\to P,\ L'\to Q_D,\\
 D\text{-phase}&L\to H\ \mapsto\ L\to P,\ L'\to H.
\end{array}                                                        \tag{1.3}
\]

No arbitrary owner-slot choice implies either row in (1.2); this is an
extra correlation with the fixed first matching.

## 2. Port and endpoint audit

In the D-phase, deleting `L->H` and inserting the two new arcs restores the
old outgoing port at `L` and incoming port at `H`.  Exactly the free
incoming port at `P` and free outgoing port at `L'` are consumed.  Hence

\[
 \operatorname {Src}(Q^+)=\operatorname {Src}(Q)-\{P\},\qquad
 \operatorname {Term}(Q^+)=\operatorname {Term}(Q)-\{L'\}.         \tag{2.1}
\]

Under `M_0`, these are physical source owner `B` and terminal owner `D`.

In the C-phase, `L'` is the head of the deleted edge and must also have a
free outgoing port.  Thus the deleted edge is terminal.  Deletion creates
source `L'`; the two new incoming ports consume sources `P,Q_D`; and the
new outgoing port consumes terminal `L'`.  This verifies the companion
ledger.  The C-phase is legal but is strictly less root-friendly.

## 3. Graphic and component audit

After deleting `AC`, the two physical additions are `AB,DC`.  Each is safe
exactly when its endpoints are in different current union--find classes.
In the original post-deletion forest, the equivalent static condition is
that the two component pairs are nonloops and not the same unordered pair.
The directed role rows give degree at most two, so acyclicity gives a linear
forest.  One edge is deleted and two are added, proving

\[
                  |E^+|=|E|+1,\qquad \kappa^+=\kappa-1.            \tag{3.1}
\]

Final graphic independence does not by itself serialize several moves.
The companion theorem correctly retains dynamic union--find and
future-provider avoidance as additional serial guards.

## 4. Prospective phase planting

Each labelled move prescribes exactly two first-matching rows.  If these
rows and a protected predecessor matching form a partial matching of total
size at most `m-1`, the established protected small-matching extension
theorem applies.  This proves only the first matching.  It does not select
the auxiliary upper providers or establish free ports, residual Hall, or
topology.  The theorem's bounded prospective scope is therefore exact.

## 5. Alternating-forest exchange audit

Let the dependency forest have `n` nodes and `d` roots.  It has `n-d`
parent--child edges, so the blocker family has that size.  The simultaneous
exchange removes

\[
                         n+(n-d)=2n-d
\]

old edges and inserts `2n`, gaining exactly `d`.

The word **entire** in the theorem's blocker definition is load-bearing:
`H` contains every residual selected edge meeting a genuinely new resource,
`H` avoids the protected bank, and every new edge is role/slot-disjoint from
all of `Q-(F union H)`.  Otherwise (5.2) need not be a matching or preserve
the protected bank.

The upper-colour partition is literal.  Every rerouted `g` restores the
colour of its deleted auxiliary provider.  Every nonroot target `e`
restores the colour of its unique blocker because this equality is imposed
on every parent--child dependency, while the `d` root targets add
the `d` missing colours.  Because the auxiliary and blocker families are
disjoint subsets of an upper matching, these colour classes are disjoint.
The explicit role/resource and graphic hypotheses therefore prove an
upper-exact protected forest.  Its component count follows from Euler and
`W-U=Cat_m`.

The least-fixed-point closure is the exact uncapacitated AND-tree test:
height induction proves sufficiency, and the complement of the closure is
the stated trap.  On the private at-most-one-blocker face, dependencies are
paths.  Capacity-one resource splitting makes their joint choice exactly a
vertex-disjoint linkage, so strict-gammoid rank/Menger separation is both
necessary and sufficient.  Without privacy, paths can splice through a
shared resource bundle and this reduction is unsound.

Finally, if `n_j` nodes have `j` children, forest edge counting gives

\[
 \sum_j jn_j=n-d,
 \qquad
 n_0=d+\sum_{j\ge2}(j-1)n_j.                                      \tag{5.1}
\]

This verifies the extra leaf debt for two- and three-blocker nodes and the
failure of ordinary marginal Hall beyond the private path face.

## 6. Multi-funnel and reserve scope

The deleted `f` is the selected provider of its auxiliary upper colour,
not a duplicate-colour SCD connector.  In the D-phase, a component starting
at `P` and one ending at `L'` can be spliced into the two pieces exposed by
deleting `f`, subject to the literal port and union--find tests.  The
interiors are preserved; the source `P` and terminal `L'` are not.

A frozen three-primary reserve edge cannot simultaneously be deleted and
claimed protected.  It may instead expose a free port, or its replacement
must be chosen before the reserve is frozen.  One local move also breaks
clean cyclic equivariance unless its whole orbit is developed and audited.
These qualifications preserve the earlier `Cat_r` reserve lower bound.

The raw labelled menu is not an availability theorem: occupying both slots
of every facet `R-a` blocks the target owner resource `B=R-a` for every
direct candidate through `R`.  Hence polynomial supply cannot replace the
fixed-phase, occupancy, packing and topology rows.

The augmenter installs one missing upper colour and supplies one component
merger.  It is unavailable after upper exactness and therefore cannot
replace the final `Cat_m-1` duplicate-colour connector braid.  The companion
theorem states this separation correctly.

No computation or asymptotic heuristic is used in this audit.
