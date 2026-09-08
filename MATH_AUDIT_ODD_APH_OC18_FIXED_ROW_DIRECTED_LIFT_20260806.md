# Audit: the OC18 origin code has the fixed-row directed lift

**Date:** 2026-08-06  
**Primary theorem:**
`MATH_THEOREM_ODD_APH_OC18_ORIGIN_APERTURE_AND_MOBILE_CART_REDUCTION_20260806.md`  
**Lift theorem:** Theorem 4.1 of
`MATH_AUDIT_ODD_COMPLEMENT_ONE_SOCKET_INDEPENDENT_20260806.md`  
**Method:** literal support and generator audit; no computation or search  
**Verdict:** **GO.** Every OC18 code edge and every reflected-support edge
used to prepare the code is a bounded word in the authenticated fixed-row
work generators. There is no missing directed generator.

## 1. The authenticated generator

Fix the selected nonquiet row on `p_1`, and let the scan prefix end there.
For every physical unit-transfer edge

\[
                         e:z\longleftrightarrow z'
\]

whose support is disjoint from that prefix, the shadow-clock theorem gives
the directed two-arc generator

\[
             \widehat z\longrightarrow \widetilde {z'}
                         \longrightarrow \widehat {z'} .       \tag{1.1}
\]

The first arc is the physical transfer. The second is the uniquely selected
`p_1` matching edge. The unordered selected row on `p_1` is unchanged, and
the endpoint is again on the majority shore. Consequently any work walk

\[
                         z_0,z_1,\ldots,z_t                 \tag{1.2}
\]

lifts by concatenating the generators (1.1). The theorem applies in either
orientation of every undirected work edge; reversal of a local code path is
therefore covered as well.

This is the only directed generator needed below.

## 2. Support audit

The first connector meeting `p_1` and the two terminal-collar blocks are
removed before the ordinary atom is selected. The atom, its aperture, both
temporary heads, and every block moved while preparing the aperture all lie
in the reserved work suffix. In particular:

1. an internal move inside one two-coordinate work block is disjoint from
   the scan prefix through `p_1`;
2. a move across the boundary of two adjacent work blocks is also disjoint
   from that prefix;
3. moving an aperture block through `H|H` changes values on work
   coordinates, but does not change the coordinate support; and
4. reflecting such a bounded local path merely reflects its list of
   physical work edges. It does not move an edge into `p_1`.

Thus semantic values `H`, `M`, `A`, `B`, and `C` do not create a new edge
type. Every nonzero microstep in the origin-aperture preparation belongs to
the token graph `G_work` of the shadow-clock theorem. A zero-length reparse
of a run of identical `H` blocks contributes no graph edge and needs no
lift.

## 3. The OC18 tables are literal work walks

Every consecutive pair in the displayed code tables is one adjacent unit
transfer. For example,

\[
 0020\to0011\to0002,
 \qquad
 0022\to0112\to1012,
 \qquad
 2022\to1122\to0222                         \tag{3.1}
\]

are respectively two products of generators (1.1), and the remaining rows
are identical in form.

For an `M`-containing aperture the theorem chooses a simple path in the
fixed-mass four-coordinate layer `V_j`. By definition, every edge of `V_j`
is one adjacent physical transfer. Moreover

\[
       |V_j|\le |V_4|=19,
       \qquad |V_4-\{0202\}|=18.             \tag{3.2}
\]

Hence a chosen simple code path is a word of at most eighteen authenticated
generators, or at most seventeen in the punctured mass-four layer. No
connectivity assertion is being used as a substitute for a directed lift:
connectivity chooses the undirected work path, and (1.1) lifts each of its
literal edges.

The block transpositions used to bring the two aperture blocks to one side
of the stationary cart have the same form. Each is a simple path in a
four-coordinate fixed-mass layer and is therefore a product of at most
eighteen generators. Lemma 2.1 of the primary theorem uses only an absolute
bounded number of these transpositions. Thus the entire reflected support
preparation is a bounded word in (1.1).

## 4. Why reflection causes no phase gap

It would be invalid to obtain the directed reflected path by conjugating a
phase-zero path: reflected complement need not be an automorphism of the
fixed directed contraction. The present argument does not do that.

Write the reflected local path as its literal physical work edges

\[
                  \rho e_1,\rho e_2,\ldots,\rho e_t .          \tag{4.1}
\]

Each `rho e_i` is itself an edge of `G_work`, so apply (1.1) directly to
`rho e_i`. The same selected `p_1` row clocks every edge. Therefore the
reflected bounded support straddling the semantic atom heads is no different
from an ordinary work path for directed-lift purposes.

This is precisely the distinction made in the independent complement audit:
macroscopic directed conjugacy is false, while edgewise shadow-clock
compilation is true.

## 5. Collision and composition audit

The shadow-clock theorem also states that vertex-disjoint work walks have
vertex-disjoint directed lifts. The OC18 proof supplies the work-level
decoder:

* the persistent origin code fixes the atom address and collar-order class;
* the early register fixes atom type, orientation, and transport phase;
* one literal head or the returned cart fixes the active local window; and
* simplicity fixes the microstep.

Hence two distinct source-labelled OC18 work paths cannot meet at a majority
work state. Their lifts cannot meet at a minority state either, because a
minority state is the unique selected-row mate of its following majority
state. Concatenating setup, code writing, cart work, code restoration, and
atom retirement therefore introduces no new collision.

If different sources use different selected nonquiet `p_1` rows, the rows
are disjoint matching edges and already distinguish their lifted states. If
they use the same row, the preceding work-state argument applies.

## 6. Verdict

Every nonzero move required by the OC18 origin-code construction is either

1. a physical unit transfer wholly in the work suffix, hence one generator
   (1.1); or
2. a bounded simple fixed-mass work path, hence a bounded product of those
   generators.

The reflected-support case is covered edge-by-edge and requires no new
phase-one row, no directed conjugacy, and no additional protected generator.
Therefore the final directed-lift qualifier in the primary theorem is
discharged.

This audit is limited to the directed-lift row. It does not independently
reaudit the origin-aperture selection or the work-level occurrence decoder;
it shows that their already stated literal paths compile into the fixed-row
directed contraction exactly as required.
