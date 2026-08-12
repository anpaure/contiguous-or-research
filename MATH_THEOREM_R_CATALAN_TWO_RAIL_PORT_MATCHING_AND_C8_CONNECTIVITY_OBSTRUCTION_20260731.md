# Catalan two-rail port matchings: exact C8 transport and a connectivity obstruction

Date: 2026-07-31  
Lane: R  
Status: unconditional fixed-fragment theorem and an explicit first-
nondegenerate counterexample.  The theorem preserves the exact lower palette
and the complete immediate-upper multiplicity vector.  Deeper shadows,
residence and the common-cap compiler remain separate literal conditions.
No all-dimensional equality claim is made.

## 0. Verdict

Assume the split-switch matching of
`MATH_THEOREM_CATALAN_TWO_RAIL_RAINBOW_SWITCH_REDUCTION_20260731.md`
exists, with `m>=2`.  The resulting two-rail factor has an exact and useful
connectivity normal form.

1. Freeze the `K` retained path fragments on each rail.  Their `4K`
   occurrence-labelled endpoint ports carry a fixed-point-free involution
   `P`, pairing the two ends of each fragment.
2. Form the bipartite **port containment graph** between marked and unmarked
   endpoint occurrences.  Every compatible perfect matching `M` gives a
   spanning degree-two factor with exactly the same lower-q1 palette and the
   same complete immediate-upper multiplicity vector as the split-switch
   factor.
3. Its factor components are exactly the alternating cycles of `P union M`.
   Hence fixed-fragment Hamiltonization is equivalent to one extra condition:

   \[
             \text{the port graph has a perfect matching }M
             \text{ for which }P\cup M\text{ is one cycle}.       \tag{0.1}
   \]

4. The symmetric difference of two port matchings is a bank of
   occurrence-labelled common-`z` alternating closed trails.  A component
   whose physical unmarked owners are distinct is a simple incidence
   circuit; in particular its length-eight components are common-`z`,
   q1-neutral C8 moves.  They become protected only after the blocker and
   residence conditions in Section 6 pass.  Thus C8 reachability is a restricted
   perfect-matching exchange problem, not a consequence of the existence of
   the first split-switch matching.

Condition (0.1) is not automatic.  At `m=2` there is an exact rainbow
two-rail factor whose port graph is a single C8 and hence has exactly two
perfect matchings; both give two factor cycles.  Its unique cross-rung C8
preserves every lower colour and every immediate-upper multiplicity but maps
two cycles to two cycles.  This also refutes the previously stated
length-only component-parity law.  The exact topology invariant is the
occurrence-port cycle count, not circuit length.

## 1. Ports left by the split switches

Use the notation of the source theorem:

\[
 M=\binom{2m}{m},\qquad N=\binom{2m}{m+1},\qquad
 K=M-N=\operatorname {Cat}_m .                          \tag{1.1}
\]

The `K` local switches cut `K` distinct edges on the unmarked `U`-rail and
`K` distinct edges on the marked `z+C` rail.  The unmarked cuts may be
adjacent, so endpoints are occurrences: two ports may represent the same
physical `U` owner when the intervening fragment is a singleton.

Let

\[
                 {\cal Q}={\cal E}\sqcup\{J_X:X\in{\cal E}\}.     \tag{1.2}
\]

The union is disjoint because `{\cal E}` consists of the middle sets omitted
from the original saturating cycle, while every `J_X` is one of its used
sets `C_i`; rainbow condition (2.2) makes the `J_X` pairwise distinct.
Thus `|Q|=2K`.

For each `L in Q`, the switched factor has one cross edge

\[
                         (z+L)-\psi(L),\qquad L\subset\psi(L),      \tag{1.3}
\]

where `psi(L)` is an unmarked rank-`m+1` owner.  Regard its marked endpoint
as a port `p_L`.  Regard the `2K` endpoint occurrences of the cut unmarked
rail as ports `q`; write `U(q)` for the physical owner represented by `q`.
The original cross edges give a perfect matching `M_0` from the marked ports
to the unmarked port occurrences.

Deleting the cross edges leaves exactly `2K` retained rail fragments.  Pair
the two endpoint occurrences of every fragment, including the two distinct
tokens of a singleton fragment.  The resulting perfect matching on all
`4K` ports is denoted by `P`.

## 2. The exact port-matching theorem

Define the occurrence-labelled bipartite graph

\[
 {\cal G}_{\rm port}=({\cal P}_{z},{\cal P}_{0};E),\qquad
 p_Lq\in E\quad\Longleftrightarrow\quad L\subset U(q).             \tag{2.1}
\]

Every edge in (2.1) represents the literal Johnson edge
`(z+L)-U(q)`.  A perfect matching is called simple if its token edges induce
distinct physical Johnson edges.  In the split-switch setting this is
automatic: the labels `L` and hence the marked owners `z+L` are distinct.

### Theorem 2.1 (fixed-fragment port equivalence)

For every perfect matching `M` of `G_port`, insert the cross edge
`(z+L)-U(q)` for each `p_Lq in M` and retain every internal edge of every
rail fragment.  Call the result `F_M`.  Then:

1. `F_M` is a spanning degree-two factor on the child middle level.
2. Its complete lower-q1 multiset is independent of `M`; in particular it
   is the exact palette certified by the rainbow split-switch theorem.
3. Its complete immediate-upper multiplicity vector is independent of `M`.
4. Its factor components are in canonical bijection with the cycles of
   `P union M`, on occurrence-labelled ports.

Consequently `F_M` is one Hamilton cycle if and only if `P union M` is one
cycle.

#### Proof

An internal vertex of a retained fragment keeps its two old incident edges.
An ordinary endpoint keeps one internal edge and receives one matching edge.
A singleton fragment has two endpoint tokens and receives two matching
edges.  Thus every physical owner has degree two.

The lower colour of `(z+L)-U(q)` is exactly `L`.  Every marked port `p_L`
is used once, so the cross lower-colour multiset is the fixed set `Q`, once
each.  All internal edges are unchanged.  This proves the lower statement.

The upper colour of the same cross edge is

\[
                           (z+L)\cup U(q)=z+U(q).        \tag{2.2}
\]

Every unmarked port occurrence `q` is used once.  Hence the cross-edge upper
multiset is the fixed occurrence multiset `{z+U(q):q in P_0}`, independent
of `M`.  Internal upper colours are unchanged.  This proves the entire
immediate-upper statement, not merely marked-target surjectivity.

After contracting each retained fragment, its two endpoint tokens are
joined by `P` and every cross edge is joined by `M`.  The contracted graph
is exactly the two-regular multigraph `P union M`; contraction preserves
component count.  This proves the last assertion. \(\square\)

### Corollary 2.2 (the precise extra matching condition)

The rainbow split-switch hypothesis supplies the perfect matching `M_0`.
It supplies a connected two-rail factor if and only if `P union M_0` is one
cycle.  It supplies a fixed-fragment rethread to a connected factor if and
only if (0.1) holds for some perfect matching of `G_port`.

Thus ordinary Hall for `G_port` is already satisfied and is irrelevant to
the remaining topology.  The missing property is a **Hamilton-compatible
perfect matching** relative to `P`.

## 3. Port exchanges are common-`z`, q1-neutral circuit candidates

Let `M,M'` be two perfect matchings of `G_port`.  Their symmetric difference
is a disjoint union of occurrence-labelled alternating even cycles.  On a
component write the old edges as

\[
                 (z+L_i)-U_i\qquad(0\le i<\ell)         \tag{3.1}
\]

and the new edges, after cyclic indexing, as

\[
                 (z+L_{i+1})-U_i .                     \tag{3.2}
\]

Containment in the port graph says `L_i,L_(i+1) subset U_i`.  In the
balanced inclusion factor, (3.1)--(3.2) toggle the alternating circuit

\[
 L_0-U_0-L_1-U_1-\cdots-L_{\ell-1}-U_{\ell-1}-L_0,     \tag{3.3}
\]

while the other selected owner at row `L_i` remains `z+L_i`.  Hence this is
exactly a common-exterior-`z` circuit.

If the physical values `U_i` are distinct, (3.3) is a simple incidence
`C_(2 ell)`.  Repeated unmarked endpoint occurrences give a closed
alternating trail; after cancelling common physical edges, its balanced
symmetric difference decomposes further into simple incidence circuits.
This occurrence distinction is essential
when two U-rail cuts are adjacent.

### Theorem 3.1 (exact shadow signature)

Every exchange component (3.3):

1. preserves every lower-q1 colour exactly;
2. preserves the complete immediate-upper multiplicity vector exactly; and
3. changes factor topology according to the exact port cycle counts before
   and after the exchange.

For `ell=4` with distinct `U_i`, it is a common-`z` alternating C8.  Delete
its four old rungs from the entire unchanged factor, and let `P_C` pair the
eight resulting boundary occurrences along the retained paths (equivalently,
through `P union (M\R_C)`).  If `R_C` and `B_C` are the old and new rung
pairings, then the affected old and new
component counts are precisely

\[
                     c(P_C\cup R_C),\qquad c(P_C\cup B_C).          \tag{3.4}
\]

There is no formula depending only on `ell`.  The C8 is merging exactly
when the second number is smaller, and it Hamiltonizes its affected support
exactly when the second number is one.  Four old rungs on four distinct
components give the valid clean sufficient case `4 -> 1`.

#### Proof

The first two claims are Theorem 2.1 applied to `M` and `M'`.  Removing the
old cross edges leaves retained paths pairing their occurrence ports by
`P_C`.  Reinstalling the old or new matching closes precisely the cycles of
the two superpositions in (3.4). \(\square\)

### Corollary 3.2 (C8-only reachability)

Build the exchange graph whose vertices are perfect matchings of `G_port`
and whose edges toggle one alternating port C8 with four distinct physical
unmarked owners.  C8s Hamiltonize the frozen two-rail factor if and only if
the component of `M_0` in this exchange graph contains some `M` for which
`P union M` is one cycle.  Neither the rainbow identity nor the existence of
one C8 implies this condition.

### Corollary 3.3 (clean-C8 bank obstruction)

If an architecture permits only C8s whose four old rungs lie on four
distinct current components, every move changes the component count by
`-3`.  Such a bank can reach one component only when the initial count is
congruent to one modulo three.  This is a restriction of the **clean-only**
architecture, not a universal C8 invariant: nonclean switches must instead
be evaluated by (3.4).

## 4. What the local switches force--and what they do not

Fix one inserted `X`, hosted in `U=phi(X)`, and let `J=J_X` be the endpoint
whose marked edge is cut.  Let `V` be the other unmarked endpoint of the
cut U-rail edge.  Then

\[
                 \psi(X)=U,\qquad \psi(J)=V,\qquad U\cap V=J.       \tag{4.1}
\]

Define the current socket digraph on the cross labels by

\[
             L\longrightarrow L'\quad\Longleftrightarrow\quad
             L'\subset\psi(L),\quad L'\ne L.            \tag{4.2}
\]

The local switch forces `X -> J`: both are facets of `U`.  It does not force
a return.  More strongly, `J -> X` is impossible.  Write

\[
 U=J+a,\qquad V=J+c,\qquad c\notin U.                    \tag{4.3}
\]

Since `X` is a facet of `U` different from `J`, there is `b in J` with

\[
                         X=(J-b)+a.                     \tag{4.4}
\]

The point `a` belongs to `X` but not to `V`, so `X` is not a subset of `V`.
This proves the strict one-way assertion.

Thus the `K` local switches provide `K` built-in one-way arcs.  Every
directed C4, or longer socket cycle, needs additional inter-block
containments.  Condition (2.2) constrains lower colours and cut collisions;
it contains no such containment or strong-connectivity hypothesis.

## 5. A literal `m=2` counterexample

Take old ground set `[4]` and write sets as digit strings.  Use

\[
 (U_0,U_1,U_2,U_3)=(123,124,134,234),                  \tag{5.1}
\]

with seam facets

\[
 (C_0,C_1,C_2,C_3)=(23,12,14,34).                      \tag{5.2}
\]

The omitted middle sets are `{13,24}`.  Host `13` in `U_0`, host `24` in
`U_1`, and retain `12` in both blocks.  Thus

\[
 R_{13}=R_{24}=12,\qquad J_{13}=23,\qquad J_{24}=14.     \tag{5.3}
\]

The unmatched blocks contribute lower colours `{4},{3}`, while the two
retained split colours are

\[
                  13\cap12=1,\qquad24\cap12=2.          \tag{5.4}
\]

Hence the disjoint union in (2.2) is exactly `{1,2,3,4}`, and the two `J`
values are distinct.  Every hypothesis of the rainbow switch theorem is
satisfied.

The resulting child factor has the two cycles

\[
\begin{split}
 {\cal C}_1&=(U_0,U_1,z24,z12,z13),\\
 {\cal C}_2&=(U_2,U_3,z23,z34,z14).                    \tag{5.5}
\end{split}
\]

Its port containment graph is exactly the chordless C8

\[
 p_{23}-U_0-p_{13}-U_2-p_{14}-U_1-p_{24}-U_3-p_{23}.   \tag{5.6}
\]

Indeed these are exactly the two **unmarked** rank-three endpoint owners
containing each displayed rank-two label (the third rank-three owner is the
marked owner `z+L` itself and is not a vertex on the unmarked side of the
port graph).  A chordless even cycle has exactly two perfect matchings.
The original one is

\[
 M_0=\{p_{23}U_3,p_{13}U_0,p_{14}U_2,p_{24}U_1\},      \tag{5.7}
\]

and the other is

\[
 M_1=\{p_{23}U_0,p_{13}U_2,p_{14}U_1,p_{24}U_3\}.      \tag{5.8}
\]

The fixed fragment involution pairs

\[
 (U_0,U_1),\quad(U_2,U_3),\quad(p_{13},p_{24}),
 \quad(p_{14},p_{23}).                                  \tag{5.9}
\]

Direct superposition shows that both `P union M_0` and `P union M_1` have
two cycles.  Equivalently, toggling the genuine common-`z` C8

\[
\begin{split}
 &z23-U_3, z13-U_0, z14-U_2, z24-U_1\\
 \longmapsto{}\;&z23-U_0, z13-U_2, z14-U_1, z24-U_3             \tag{5.10}
\end{split}
\]

produces the two cycles

\[
 (U_0,U_1,z14,z34,z23),\qquad
 (U_2,U_3,z24,z12,z13).                                 \tag{5.11}
\]

All ten lower colours remain exact.  Each of the four marked immediate-
upper targets `z+U_i` has load two before and after (5.10); the sole
unmarked rank-four target also retains load two.  Nevertheless
there is no perfect matching of the fixed port graph which connects the
factor.  Hence no fixed-fragment cross-rung C8, longer common-`z` circuit, or
composition of them can Hamiltonize this exact rainbow two-rail instance.

This counterexample is scoped to fixed fragments.  A switch which cuts an
internal rail edge changes `P` and lies outside Theorem 2.1.  Such a move
must separately pass its marked-upper signature, deeper witness ledger and
residence collars; the split-switch theorem supplies none of these facts.

## 6. Protected upper witnesses and residence

For fixed fragments, Theorem 2.1 completely closes immediate q1:
cross-rung rematching preserves both lower and upper multiplicities exactly.
It does not literally retain each old cross-rung occurrence; it hands the
target `z+U(q)` to the new marked endpoint matched to the same unmarked port
`q`.

For a deeper upper or lower target, a witness wholly internal to one retained
fragment survives every rematching, including reversal.  A seam-spanning
witness survives exactly when an old occurrence avoids the changed seams or
a new suffix/full-fragments/prefix interval realizes the same target.  This
is the blocker-clutter criterion from the protected-opening theorem.

Residence is likewise not a property of the abstract matching alone.  Each
oriented fragment must carry its exact run-state/DFA transition; every cycle
of `P union M` must have an accepting cyclic product.  Directed compiler
pins and a non-reversal-closed DFA require orientation-labelled ports.

Thus the protected fixed-fragment Hamiltonian gate is:

> find a compatible perfect matching `M` for which `P union M` is one cycle,
> every destroyed seam-spanning target has a literal replacement, and the
> oriented fragment product passes residence and the final common-cap
> compiler.

These predicates are joint.  Separate ordinary Hall, separate fragment
connectivity, or marked-q1 completeness does not imply them.

## 7. Correction to the earlier component-parity claim

The C8 (5.10) maps two components to two components.  It is a literal simple
alternating incidence C8.  Therefore the earlier assertion

\[
 c(F')-c(F)\equiv\ell-1\pmod2
\]

for every alternating `C_(2 ell)` is false.  The attempted proof used a
matching-sign ratio determined only by superposition cycle lengths; such a
ratio also depends on the labelled interlacing of the matching chords.

The correct universal statement is (3.4): after deleting the old circuit
half, retain the occurrence-port involution `P_C` and count the cycles after
superposing the old and new pairings.  No circuit-length-only parity rule
survives.

The clean merger statements remain valid.  If the `ell` deleted factor edges
lie on `ell` distinct components, the new circuit concatenates their `ell`
opened paths into one, changing the component count by `1-ell`.  In
particular a clean common-exterior C8 genuinely gives `4 -> 1`.  What is
withdrawn is the claim that every C8 flips parity, that every C6 preserves
parity, or that an even component count by itself forces a C8 absorber.

## 8. Exact remaining existence theorem

The split-switch theorem has reduced the fixed-fragment connectivity problem
to a concrete, source-specific statement:

> **Protected two-rail Hamilton-compatible matching lemma (open).**  Choose
> the Catalan injection and split sides so that (2.2) holds and the resulting
> port containment graph has a perfect matching `M` satisfying the one-cycle
> condition (0.1), the blocker-clutter upper ledger, the oriented residence
> DFA, and the common-cap compiler.

A sufficient circuit form is an evolving common-`z` socket cycle whose old
rungs meet each current factor component once and whose guard/DFA predicates
pass.  Its long-circuit toggle merges those components in one shot.  For a
C8-only theorem, the matching must additionally be reachable from `M_0` in
the alternating-C8 exchange graph.

The `m=2` factor proves that the rainbow split-switch matching alone cannot
imply either conclusion.  No claim that `nu(k)=B(k)` follows from the
two-rail construction is made here.
