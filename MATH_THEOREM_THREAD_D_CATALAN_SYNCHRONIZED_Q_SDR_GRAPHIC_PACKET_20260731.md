# Synchronized common-`Q` exchanges, two direct SDRs, and the rooted-graphic packet test

Date: 2026-07-31  
Status: exact packet language and exact local motif criterion; exact
fixed-filler obstruction in the two-parent normal form;
occurrence-conditional bounded actuator.  No
all-parameter regenerative construction is claimed.

## 0. Verdict

Fix an oriented structural Catalan path forest `F` and an independently
chosen Catalan filler forest `G` on the same old ground set.  The exact
two-parent strict recursive state is

\[
                         (F,G,Q,M^-,M^+,{\cal H}),              \tag{0.1}
\]

where `F` supplies the common inherited-port bank and both direct
occurrence systems, `G` supplies the isolated translated `c`-rail,
`M^-`,`M^+` are the two direct occurrence SDRs, and `H` is the complete
capped physical support.  There is an exact simultaneous exchange
language in the structural `F` fibre, while the `c+G` summand may be chosen
independently.

* Changing `Q` from `Q` to `Q'` forces, on each shore, alternating paths
  whose endpoints are exactly the old and new exposed port owners.
  Alternating cycles may be added independently.  This condition is both
  necessary and sufficient for the two palette rows.
* After including every changed seam, representative and auxiliary root
  edge, physical acyclicity is exactly a binary fundamental-cycle minor,
  or equivalently a loopless-forest test after contraction.  Degree and
  anchor caps remain literal rows.
* A unit exchange `Q-q+r` has a genuinely bounded realization when both
  shores contain the two-edge alternating paths

  \[
       \partial_\sigma q-y_\sigma-\partial_\sigma r,
       \qquad \sigma\in\{-,+\}.                         \tag{0.2}
  \]

  Its existence and its graphic safety are occurrence hypotheses, not
  consequences of the automatic common-basis theorem.
* Forbidden `0110` motifs have an exact seam-local ledger.  Every motif
  wholly inside a retained path fragment survives; only three-edge windows
  crossing a removed or added edge need to be checked.

There is a decisive but sharply scoped limitation.  The translated filler
sector `c+G` is a direct summand independent of `F,Q,M^-,M^+`.  Therefore a
filler motif

\[
                         b_{i-1}=a_{i+1}                         \tag{0.3}
\]

survives **every** exchange in the fixed-`G` structural selection fibre,
bounded or unbounded.  In the old one-parent specialization `G=F`, the
frozen child parameters `n=3,4,5` contain respectively `5,17,44` such
fixed-filler motifs.  The independent-filler theorem permits replacing
`G` by a guarded `G'` without changing `Q` or either SDR.  Thus this is an
obstruction to a fixed filler, not to the two-parent strict recursion.

Thus the packet theorem below is exact and reusable, but its role is to
repair motifs in the structural three-sector support and to certify an
`F`-changing regeneration tuple **after** a labelled correspondence between
the old and regenerated occurrence catalogues has been supplied.  The
alternating-path theorem itself is a fixed-`F` theorem.  Filler residence is the separate
right-total supply problem `G -> G'`.  Neither result alone is a residence
induction.

## 1. Direct SDRs as matchings with synchronized exposed sets

For `sigma in {-,+}`, let

\[
 B^\sigma=({\cal O}^\sigma,X^\sigma;{\cal E}^\sigma)              \tag{1.1}
\]

be the strict direct occurrence graph.  The left shore
`O^sigma` is the relevant outer palette.  The right shore `X^sigma` is the
middle palette on that side.  Consistent orientation of every child path
makes the endpoint maps

\[
 \partial_-q=t_q,\qquad \partial_+q=h_q\qquad(q\in E(F))          \tag{1.2}
\]

injective.  The direct SDR `M^sigma` is a matching which saturates every
left vertex and every right vertex except

\[
                    \partial_\sigma Q
       =\{\partial_\sigma q:q\in Q\}.                              \tag{1.3}
\]

This is just the set form of the two exact direct-SDR equations: the
omitted middle colours are the inherited tail bank on one shore and the
inherited head bank on the other.

### Theorem 1.1 (unmatched-set alternating-path normal form)

Let `M^sigma` and `N^sigma` be direct SDRs belonging to port banks `Q` and
`Q'`, respectively.  Their symmetric difference is a disjoint union of

1. even alternating cycles; and
2. even alternating paths, each joining one member of

   \[
       \partial_\sigma(Q\setminus Q')
       \quad\hbox{to one member of}\quad
       \partial_\sigma(Q'\setminus Q).                \tag{1.4}
   \]

Every vertex in (1.4) is used once and there are no other open paths.

Conversely, start from `M^sigma`.  Let `A subseteq Q` and
`E subseteq E(F)-Q`, with `|A|=|E|`.  If a vertex-disjoint family of
`M^sigma`-alternating paths pairs `partial_sigma A` with
`partial_sigma E`, and a vertex-disjoint family of alternating cycles is
also toggled, then the resulting matching is a direct SDR exposing exactly

\[
                 \partial_\sigma(Q-A+E).              \tag{1.5}
\]

#### Proof

At a left vertex, both matchings have degree one, so the symmetric
difference has degree zero or two.  At a right vertex matched by both or
neither it likewise has degree zero or two.  Its degree is one precisely
when the vertex is exposed by exactly one matching, namely at the vertices
in (1.4).  Hence every nontrivial component is an alternating cycle or an
alternating path with endpoints in (1.4).  Alternation forces the two ends
of a path to have opposite old/new exposure status.  This proves the first
claim.

Conversely, toggling an alternating cycle changes no matching degree.
Toggling a path matches its formerly exposed endpoint and exposes its
formerly matched endpoint.  Vertex-disjointness makes the toggles commute,
and (1.5) follows.  `square`

### Corollary 1.2 (exact synchronized common-basis packet)

Put `Q'=Q-A+E`.  There are direct SDRs for `Q'` on both shores if and only
if there are path/cycle families of Theorem 1.1 simultaneously for
`sigma=-,+`, with the **same** sets `A,E`.

In particular this condition itself certifies that `Q'` is a common basis
of the two pulled-back direct transversal matroids.  It is stronger than
separate rank or one-sided Hall inequalities because it displays both
integral representative systems.

### Corollary 1.3 (unit synchronized packet)

Let `q in Q` and `r notin Q`.  Suppose that, for each shore, there is an
outer colour `y_sigma` such that

\[
 y_\sigma\partial_\sigma r\in M^\sigma,
 \qquad
 y_\sigma\partial_\sigma q\in {\cal E}^\sigma.        \tag{1.6}
\]

Then replacing the first edge in (1.6) by the second on both shores and
putting `Q'=Q-q+r` preserves both direct palettes exactly.  These are the
shortest possible nontrivial alternating paths, each of length two.

After parallel occurrence labels are collapsed to their literal physical
edges, its complete nonroot physical ledger is a `5 -> 5` exchange.  Indeed, at
`q` it replaces the two selected-port seams by the punctured central edge;
at `r` it replaces the punctured central edge by the two selected-port
seams.  This is a `3 -> 3` exchange, and the one representative replacement
on each shore adds two further old and two further new edges.  After common
edges are cancelled, write these sets as

\[
                         A_{q,r}^{\rm unit},
                         E_{q,r}^{\rm unit},
              \qquad |A_{q,r}^{\rm unit}|=
                     |E_{q,r}^{\rm unit}|=5.           \tag{1.7}
\]

Thus, when the auxiliary rooted edges can be retained, the unit packet's
graphic test is exactly the `5 x 5` instance of (2.2).  If changing the
anchor bank forces auxiliary root-edge changes, those root exchanges must
be appended to (1.7), and the larger full minor—not the bare `5 x 5`
minor—is authoritative.  In either form the literal owner and anchor caps
must still be checked.

## 2. Exact rooted-graphic and capacity test

Augment the current physical forest by the auxiliary root edges used in
the rooted-side formulation, obtaining a graphic base `T` on a fixed
vertex set.  A proposed synchronized packet changes every affected direct
representative and seam, and may also change its auxiliary root choices.
After cancelling common edges, write its complete graphic exchange as

\[
                       T'=T-A_G+E_G,
             \qquad |A_G|=|E_G|=s.                    \tag{2.1}
\]

For `e in E_G`, let `C_T(e)` be the fundamental cycle of `e` with respect
to `T`, and put

\[
 X_{A_G,E_G}(a,e)=\mathbf 1[a\in C_T(e)]
       \quad(a\in A_G,e\in E_G).                      \tag{2.2}
\]

### Theorem 2.1 (complete packet certificate)

The synchronized packet gives another strict common-`Q`/two-SDR rooted
graphic state if and only if all of the following hold.

1. The two shore path/cycle families satisfy Theorem 1.1 with the same
   `A,E`.
2. Every literal owner, role, ordinary-degree and seam-anchor capacity row
   holds after the exchange.
3. The binary matrix (2.2) is nonsingular:

   \[
                         \det_{\mathbf F_2}X_{A_G,E_G}=1.          \tag{2.3}
   \]

If the state is stored as a forest rather than a rooted base, take
`A_G,E_G` here to mean only the nonroot physical edges.  Condition 3 is
equivalently: delete `A_G`, contract every remaining component, and
require the multigraph induced by `E_G` to be loopless and acyclic, with
the prescribed final edge count.

#### Proof

Item 1 is Corollary 1.2.  Item 2 is exactly the nonmatroidal physical
capacity row.  Represent the graphic matroid over `F_2` and row-reduce the
columns of `T` to the identity.  The coordinate column of a nonbasis edge
`e` is the incidence vector of `C_T(e)`.  Replacing the basis columns
indexed by `A_G` by those indexed by `E_G` gives a basis exactly when the
minor (2.2) is nonsingular.  This proves (2.3).  The contraction statement
is the usual expansion/contraction characterization of cycles in a
forest.  `square`

This criterion includes simultaneous-depth topology: one must put the
complete physical support into `A_G,E_G`.  Testing the two shore forests
separately and then assuming their common-port coupling is acyclic is not
sound.

## 3. Exact motif locality

Orient a physical path as

\[
                    v_{i+1}=v_i-a_i+b_i.              \tag{3.1}
\]

A positive coordinate run has length two on
`v_i,v_(i+1)` precisely when the four-vertex trace is `0110`, equivalently

\[
                         b_{i-1}=a_{i+1}.              \tag{3.2}
\]

The property is invariant under reversal of the whole path.

Delete the old physical edges `A_G` of a legal packet, ignoring auxiliary
root edges, and call the resulting maximal physical path pieces the
**retained fragments**.

### Lemma 3.1 (seam-local motif ledger)

Every forbidden motif whose three edges lie in one retained fragment is
present after the packet, possibly in reverse order.  Every motif which is
destroyed crosses a deleted physical edge, and every newly created motif
crosses an added physical edge.  Consequently, if the packet removes and
adds `s` physical edges, its exact motif change is determined by at most
`3s` old and `3s` new three-edge seam windows.

In particular, a packet eliminates one specified motif and creates none if

1. at least one of its three edges is deleted;
2. no other old motif crosses a deleted edge; and
3. every new three-edge window crossing an added edge avoids (3.2).

#### Proof

Inside a retained fragment, the vertex and edge order is unchanged up to
reversal, and `0110` is palindromic.  Thus all internal motifs survive.
Only a three-edge window meeting a cut can disappear, and only a window
meeting a new seam can appear.  A fixed edge occupies one of three
positions in a three-edge window, giving the stated bound.  The final
criterion is immediate.  `square`

The lemma is stronger and safer than a scalar run-count objective: it says
exactly which local collars require replay and proves that all other motif
claims are inherited.

## 4. The smallest useful physical cores

### Lemma 4.1 (two-edge run-transfer core is not palette-neutral)

Let `x` be absent from `A` and present in `B,U,V`.  Suppose `AB` is an
`x`-boundary Johnson edge and `UV` is an internal `x`-edge.  Consider the
degree-preserving path splice

\[
             \{AB,UV\}\longrightarrow\{AU,BV\}.       \tag{4.1}
\]

If the old and new lower turn-colour multisets are equal, then `B=U` and
(4.1) is the trivial exchange.  The crossed alternative
`{AV,BU}` is likewise trivial.

#### Proof

Among the old lower colours, `A cap B` is the unique one omitting `x`,
whereas `U cap V` contains `x`.  Among the new lower colours,
`A cap U` is the unique one omitting `x`, whereas `B cap V` contains `x`.
Palette equality forces

\[
                         A\cap B=A\cap U.              \tag{4.2}
\]

Both `B` and `U` are Johnson neighbours of `A` obtained by inserting `x`.
Their intersections with `A` identify the deleted coordinate, so (4.2)
implies `B=U`.  The other crossing is identical.  `square`

Thus the tempting two-column splice which transfers a short run into a
long run cannot itself preserve even the lower palette.  It needs a third
palette column, a `Q` exchange, or a larger compensating circuit.

### Lemma 4.2 (standard incidence hexagon)

Let `K` have size `r-2`, and let `a,b,c,d` be distinct outside `K`.  Put

\[
\begin{array}{lll}
 L_a=K+a,&L_b=K+b,&L_c=K+c,\\
 U_{ab}=K+a+b+d,&U_{bc}=K+b+c+d,&U_{ca}=K+c+a+d.
\end{array}                                                        \tag{4.3}
\]

The exchange

\[
\begin{aligned}
 &(L_a,U_{ab}),\ (L_b,U_{bc}),\ (L_c,U_{ca})\\
 &\hspace{18mm}\longleftrightarrow
 (L_b,U_{ab}),\ (L_c,U_{bc}),\ (L_a,U_{ca})             \tag{4.4}
\end{aligned}
\]

is an alternating `C6`.  It preserves both palette multisets and the
complete physical degree vector.  Its six physical vertices are

\[
 K+ab,\ K+ad,\ K+bc,\ K+bd,\ K+ac,\ K+cd,               \tag{4.5}
\]

and each is incident with one old and one new edge.

Therefore a selected old half of (4.4) may be toggled without any new
degree violation.  It preserves a physical forest exactly when its three
new edges pass Theorem 2.1, and it eliminates a forbidden motif exactly
when the seam-local test of Lemma 3.1 passes.

#### Proof

The containments in (4.4) are immediate.  Every `L` and every `U` occurs
once on each side, proving both palette claims.  Expanding each incidence
to its two intermediate rank-`r` sets gives (4.5); direct inspection shows
one old and one new incidence at every listed vertex.  The remaining
claims are Theorem 2.1 and Lemma 3.1.  `square`

The algebraic `C6` identity is unconditional.  Its applicability is not:
the strict occurrence catalogue must contain the six incidences, its old
half must be selected, all role and anchor rows must survive, and its
contracted new half must be acyclic.  The theorem does not assert that a
useful hexagon exists near every motif.

## 5. No bounded theorem follows from the matroid rows alone

For every `L`, let one shore occurrence graph have right vertices
`r_0,...,r_L`, left vertices `y_1,...,y_L`, and only the edges

\[
                  y_ir_i,\qquad y_ir_{i-1}\quad(1\le i\le L).      \tag{5.1}
\]

The matching `{y_i r_i}` exposes `r_0`; the only matching exposing `r_L`
is `{y_i r_(i-1)}`.  Their symmetric difference is the unique alternating
path

\[
              r_0-y_1-r_1-y_2-\cdots-y_L-r_L,          \tag{5.2}
\]

of length `2L`.  Use identical copies on the two shores and map all
physical edges into private branches of a rooted tree.  Then every palette,
capacity and graphic row is harmless, but moving the synchronized exposed
port requires changing all `L` representatives on both shores.

Hence neither two transversal matroids nor their addition to a graphic
base implies a dimension-independent circuit bound.  A bounded packet
theorem must assume a bounded literal occurrence corridor such as (1.6),
or prove such corridors from Boolean geometry.

This example is an abstract sharpness construction.  It is not asserted to
be an induced strict Boolean occurrence graph.

## 6. The independent filler and the exact fixed-fibre obstruction

The complete two-parent strict lift is a disjoint union

\[
        {\cal H}(F,G,Q,M^-,M^+)
          =(c+G)\ \dot\cup\ {\cal H}_3(F,Q,M^-,M^+),               \tag{6.1}
\]

where `H_3` is the punctured-`z` rail, the two pure sides and the two seam
families.  No seam or side edge is incident with `c+G`.  This is the exact
independent-filler theorem; the equality `G=F` is optional.  Replacing `G`
may require a new auxiliary root augmentation of the full disjoint union,
but it leaves the structural rooted row on `H_3` unchanged.

### Theorem 6.1 (fixed-filler residence invariance)

If three consecutive edges of `G` contain (3.2), their translated copies
in `c+G` contain the same forbidden motif for every choice of structural
forest `F`, common basis `Q`, and direct SDRs `M^-,M^+`.  This remains true
under an arbitrary simultaneous packet of Theorem 2.1 while `G` is fixed.

Conversely, replacing `G` by any other Catalan linear forest `G'` changes
no palette, port, SDR or rooted-graphic row in `H_3`; the full support is a
linear forest exactly when `G'` and `H_3` are linear forests.

#### Proof

Adjoining the constant coordinate `c` changes none of the old-coordinate
traces.  The direct-sum identity (6.1) says a structural common-`Q`/SDR
packet never cuts `c+G`, so Lemma 3.1 preserves every motif there.  The
converse assertions are the palette and topology direct sums: every
Catalan filler uses the same two `c`-tagged palette banks, and no other
sector touches its vertices.  `square`

### Corollary 6.2 (smallest noncircular two-parent regenerative state)

A strict recursive residence induction must export the tuple

\[
                         (F,G,Q,M^-,M^+).             \tag{6.2}
\]

Its two independent obligations are:

1. choose a guarded filler `G` (or replace `G` by a guarded `G'`) for the
   isolated `c`-rail; and
2. for any forbidden motif in `H_3`, use a packet which actually cuts that
   motif.  If this requires `F -> F'`, regenerate `Q'` and both direct SDRs
   in the occurrence graphs belonging to `F'`, then pass Theorem 2.1.

The alternating paths after an `F` change live in regenerated graphs; they
are not circuits in the old fixed occurrence graphs.  On the other hand a
pure filler replacement needs no common-basis or SDR exchange at all.

This is the strict recursion gate `common Q + two direct SDRs + rooted
graphic support`, with the structural and filler quantifiers correctly
separated.

## 7. Exact `n=3,4,5` test

The solver-free audit

```text
scratch/audit_threadD_catalan_derf_local_motif_exchanges_n3_n5_20260731.py
```

reconstructs the authenticated chained witnesses in their historical
one-parent specialization `G=F` and obtains

\[
\begin{array}{c|r|r|r}
\text{child }n&\text{all motifs}&\text{fixed filler }c+G&
\text{variable/boundary}\\ \hline
3&17&5&12\\
4&44&17&27\\
5&144&44&100.
\end{array}                                                        \tag{7.1}
\]

It also exhausts every fixed-`Q`, one-shore occurrence circuit of order at
most three.  The numbers of graphic-feasible packets and motif descents are

\[
\begin{array}{c|c|r|r}
n&\text{shore}&\text{graphic-feasible}&\text{motif descents}\\ \hline
3&-&2&0\\
3&+&2&0\\
4&-&12&0\\
4&+&12&0\\
5&-&39&0\\
5&+&33&0.
\end{array}                                                        \tag{7.2}
\]

The shore signs in (7.2) only name the two source arrays; the source audit
records the corresponding `upper/lower` labels explicitly.  Every feasible
packet in this finite class is physically trace-identical.

The synchronized packet is different.  A second solver-free audit exhausts
every one-element `Q` exchange for which each shore is transported by a
simple alternating path of at most three arcs.  It obtains

\[
\begin{array}{c|r|r|r|r}
n&\text{labelled packets}&\text{full physical forests}&
\text{strict descents}&\text{pure eliminators}\\ \hline
3&5&1&1&0\\
4&72&16&3&0\\
5&589&39&3&1.
\end{array}                                                        \tag{7.3}
\]

The pure `n=5` packet is already the unit move of Corollary 1.3:

```text
q_out=188, q_in=67,
upper new occurrence=(65,3), lower new occurrence=(67,8).
```

It deletes the coordinate-eight motif on ambient vertices
`(3682,3906,3850,3722)` and creates none.  Since that motif lies in the
structural three-sector support, the packet remains valid after replacing
the disjoint filler `G` by any other Catalan forest.  This is an exact
finite positive actuator, not an all-parameter supply theorem.

Restricting the same audit to the support-minimal length-two paths of
Corollary 1.3, and collapsing parallel labels to physical packets, gives
the sharper unit ledger

\[
\begin{array}{c|r|r|r|r|r|r|r}
n&\text{direct pairs}&\text{graphic}&\text{physical}&
 \text{root/profile}&\text{improving}&\text{best }\Delta&
 \text{pure}\\ \hline
3&2&1&1&1&1&-2&0\\
4&9&9&9&8&2&-1&0\\
5&20&19&9&9&2&-1&1.
\end{array}                                                        \tag{7.4}
\]

Here `physical` is the conjunction of the degree and graphic rows;
`root/profile` additionally retains the exact anchor/root profile.  The
pure row in (7.4) is the displayed `188 -> 67` packet.  Thus the exact
five-edge theorem is nonvacuous at every tested parameter, while a pure
one-motif deletion first occurs in the frozen chain at `n=5`.

The `c+G` column diagnoses the copied-filler choice only.  By Theorem 6.1
it is immutable while that filler is fixed, but the independent-filler
theorem permits a different `G` without disturbing the structural state.

The all-parameter statements are Theorems 1.1, 2.1 and 6.1, not either
finite census.  Table (7.2) shows that fixed-`Q` one-shore circuits do not
move the frozen chronology, while (7.3) proves that synchronizing the `Q`
exchange with both SDR paths can move it and, at `n=5`, can do so
monotonically.  Neither census excludes longer packets or a
structural-forest-changing regeneration circuit.

## 8. Exact surviving theorem target

The first reusable positive target is now:

> **Bounded two-parent regeneration lemma.**  Every accepted state `(F,G)`
> with one designated forbidden motif in its structural three-sector
> support admits one of the following bounded repairs:
>
> 1. a fixed-`F` synchronized `Q`/two-SDR packet of Theorem 2.1 which cuts
>    the motif, creates none, and exports the same reserve state; or
> 2. a structural-forest packet `F -> F'` which cuts the motif, followed in
>    the regenerated occurrence graphs by synchronized alternating paths
>    producing `Q',M'^-,M'^+` and a complete physical exchange satisfying
>    the new rooted minor and every capacity row.
>
> Independently, the accepted filler relation is right-total: some guarded
> `G'` exists for the next isolated `c`-rail.

Theorem 2.1 gives a proof-producing verifier for alternative 1, and the
same unmatched-set and graphic arguments verify alternative 2 after a
labelled regenerated catalogue is supplied.  Lemma 3.1 reduces the
residence audit to bounded collars.  Existence of the two uniform repair
supplies and the filler supply is open.  The automatic common-basis theorem alone does not
provide the bounded alternating paths.  Theorem 6.1 only rules out
repairing a bad **fixed filler** by structural selection; it does not rule
out another filler and does not rule out an `F`-changing packet on the
three-sector support.

## 9. Quantifier audit and provenance

The following statements are exact theorems with no occurrence-supply
assumption:

* the alternating-path/cycle normal form of Theorem 1.1;
* the synchronized common-basis equivalence of Corollary 1.2;
* the rooted fundamental-minor/contraction test of Theorem 2.1;
* the seam-local motif ledger of Lemma 3.1;
* the two-edge palette obstruction and the `C6` identity of Section 4;
* the absence of a matroid-only bounded-length conclusion in Section 5;
  and
* the independent-filler/fixed-filler split of Theorem 6.1.

The following are occurrence-conditional and remain open uniformly:

* existence of the two length-two paths (1.6), or of uniformly bounded
  replacements for them, in the strict Boolean occurrence graphs;
* simultaneous satisfaction of the literal caps and the full rooted minor;
* a `C6` or compound packet whose seam collar has negative motif delta;
* a bounded `F -> F'` regeneration relation carrying a new synchronized
  common basis and both SDRs; and
* a right-total guarded filler bank.

The exact source reductions and finite replay used here are

```text
MATH_THEOREM_CATALAN_DIRECT_EDGEWISE_SIDE_LIFT_RECURSION_20260731.md
MATH_THEOREM_H2_CATALAN_ROOTED_SIDE_TREE_AND_COMMON_CAP_SCD_GATE_20260731.md
MATH_THEOREM_CATALAN_INDEPENDENT_C_RAIL_FILLER_20260731.md
MATH_AUDIT_THREAD_D_CATALAN_DIRECT_RECURSION_MOTIF_EXCHANGE_N3_N5_20260731.md
scratch/audit_threadD_catalan_derf_local_motif_exchanges_n3_n5_20260731.py
scratch/threadD_catalan_derf_local_motif_exchanges_n3_n5_20260731.audit.json
scratch/audit_threadD_catalan_synchronized_q_packets_n3_n5_20260731.py
scratch/threadD_catalan_synchronized_q_packets_n3_n5_20260731.audit.json
MATH_THEOREM_THREAD_D_CATALAN_STRICT_FIVE_EDGE_PACKET_AND_MOTIF_DESCENT_20260731.md
scratch/audit_threadD_catalan_strict_five_edge_packet_n3_n5_20260731.py
scratch/threadD_catalan_strict_five_edge_packet_n3_n5_20260731.audit.json
```

The first finite audit is complete only for fixed-`Q`, one-shore occurrence
circuits of orders at most three on the frozen `n=3,4,5` rows.  Its finite
zero-descent result is explicitly superseded for synchronized moves by
(7.3)--(7.4), and must not be promoted to a no-go for longer circuits,
another filler, or structural regeneration.
The synchronized audit is complete only for one `Q` exchange and simple
alternating paths of at most three arcs per shore; its `n=5` witness is a
literal positive packet, not a uniform supply theorem.
The final audit is complete for the support-minimal five-edge subfamily;
its physical-packet counts are (7.4).
