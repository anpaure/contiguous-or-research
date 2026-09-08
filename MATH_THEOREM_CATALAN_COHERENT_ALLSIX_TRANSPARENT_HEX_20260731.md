# Coherent external labels characterize all-six transparent hexagons

Date: 2026-07-31  
Status: exact all-dimension local theorem; independently replayed on every
all-six transparent row of the frozen positive `ML(7)` fixture; no spanning
catalogue or all-`m` joint-decoration existence claim

## 0. Verdict

Let `Z=(H;a,b,c)` be an alternating Boolean-incidence hexagon in a
middle-levels factor.  Suppose the factor uses one alternating matching of
the hexagon and one additional, nonhexagon edge at every port.  At the lower
ports write

\[
 L_x=H+x,qquad L_x+d_x\text{ is its nonhexagon neighbour}
 \quad(x\in\{a,b,c\}),                              \tag{0.1}
\]

and at the upper ports write

\[
 U_{xy}=H+x+y,qquad U_{xy}-e_{xy}\text{ is its nonhexagon neighbour}.
                                                               \tag{0.2}
\]

Necessarily

\[
 d_x\notin H\cup\{a,b,c\},qquad e_{xy}\in H.       \tag{0.3}
\]

If one joint decoration marks all six ports, then toggling the hexagon
preserves that decoration if and only if

\[
 \boxed{
 d_a=d_b=d_c,qquad e_{ab}=e_{bc}=e_{ca}.}           \tag{0.4}
\]

The boundary-alternation row is automatic on this all-six face.  Thus
fixed-decoration transparency is independent of all other representative
choices once the six ports are selected: it is exactly two local equality
tests.

Call such a hexagon **coherent**.

## 1. Lower-shore palette

Orient the old matching as

\[
 L_aU_{ab},\qquad L_bU_{bc},\qquad L_cU_{ca}.        \tag{1.1}
\]

The selected lower-port turn colours before the toggle are

\[
 H+a+b+d_a,qquad H+b+c+d_b,qquad H+c+a+d_c,        \tag{1.2}
\]

and afterwards they are

\[
 H+c+a+d_a,qquad H+a+b+d_b,qquad H+b+c+d_c.        \tag{1.3}
\]

If the three `d` labels agree, the two multisets are visibly the same.
Conversely, every `d_x` lies outside `H union {a,b,c}`.  If all three are
different, the unique outside label identifies each term in any multiset
equality, forcing two different pairs among `ab,bc,ca` to agree.  If exactly
two `d` labels agree, the term with the unique third label must match itself,
again forcing two different pairs to agree.  Both are impossible.  Hence
the lower palette is preserved exactly when

\[
                         d_a=d_b=d_c.                \tag{1.4}
\]

## 2. Upper-shore palette

Because a nonhexagon neighbour of `U_xy` is obtained by deleting an element
of `H`, its old and new selected turn colours are `H-e_xy` plus one of the
two letters `x,y`.  With orientation (1.1), the three old colours are

\[
 H-e_{ab}+a,qquad H-e_{bc}+b,qquad H-e_{ca}+c,     \tag{2.1}
\]

and the three new colours cyclically replace `a,b,c` by `b,c,a` at those
ports.  The same unique-label argument, now inside `H`, proves that these
multisets agree exactly when

\[
                       e_{ab}=e_{bc}=e_{ca}.          \tag{2.2}
\]

Equations (1.4) and (2.2) are precisely the two shore-palette conditions of
the transparent-hexagon theorem.

### Corollary 2.1 (the private triples are forced faces)

For a coherent hexagon with common labels `d` and `e`, its three selected
upper-turn colours are

\[
 H+d+a+b,qquad H+d+b+c,qquad H+d+c+a,               \tag{2.3}
\]

and its three selected lower-turn colours are

\[
 H-e+a,qquad H-e+b,qquad H-e+c.                    \tag{2.4}
\]

Thus the recurring “private triples” in the finite `m=4,5` constructions
are not an additional empirical ansatz.  They are exactly a rank-two face
and a rank-one face of the same three-cube, forced by coherence.  A family
of coherent hexagons whose two displayed colour triples are pairwise
disjoint automatically passes forced-port colour injectivity; the remaining
representative gate is precisely the residual forced-port gap--Hall test.

## 3. Boundary alternation

Deleting the old hexagon matching leaves retained path fragments whose six
boundary vertices are exactly the six marked ports.  Every new seam joins a
lower port to an upper port.  Therefore the last selected type on one side
of every seam and the first selected type on the other are opposite.  The
fragment-boundary condition is automatic.

Combining this observation with Sections 1--2 proves (0.4).  The same proof
works componentwise when the toggle merges or splits factor cycles.

## 4. Recursive use and exact scope

On the all-six face the gluing catalogue can be generated without resolving
the full decoration at every candidate: retain exactly the coherent
hexagons.  The remaining correlated requirements are:

1. one joint alternating SDR marks all six ports of every selected coherent
   hexagon;
2. the gap-forest attachment test remains acyclic;
3. the coherent component graph and linkage router satisfy the exact
   resilience inequality `c(K_Y)<=|Y|+1`; and
4. protected physical-linearity, socket/voltage, residence, deeper-shadow
   and compiler rows survive.

This theorem removes the local palette-transfer ambiguity.  It does not
prove that enough coherent hexagons exist, that their port-mark constraints
have a joint decoration, or that a component-spanning selection passes the
other rows.

## 5. Frozen `m=4` calibration

The four all-six-marked transparent Hamilton rethreadings in the repaired
`ML(7)` fixture have common external labels

\[
                         (d,e)=(5,1),(6,5),(2,1),(3,6),                \tag{5.1}
\]

respectively.  The independent audit reconstructs the factor adjacency,
derives every external label from the literal six ports, and checks both
turn-colour multiset equalities before and after the toggle.
