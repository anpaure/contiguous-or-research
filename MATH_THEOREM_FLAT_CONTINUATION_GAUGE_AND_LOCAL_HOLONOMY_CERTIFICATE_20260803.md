# Flat continuation gauges and local holonomy certificates

**Date:** 2026-08-03  
**Status:** unconditional finite-state theorem.  It reduces the complete
continuation-holonomy row of a fixed completed rotor to a spanning-tree
certificate, and in a prepared cell complex to local face relations.  It
does not prove that the current OR-word packet system has such a gauge.

## 0. Outcome

The completed bilateral-rotor theorem leaves one nonadditive obstruction:
an Euler-balanced packet bank may return every named current and still act
nontrivially on the complete continuation state.  This note gives an exact
criterion under which that obstruction disappears.

Let \(\Gamma=(V,E)\) be a connected finite geometric multigraph of edge
occurrences, with one chosen orientation for every geometric edge.  At a vertex
\(v\), let \(\Omega_v\) be the complete continuation-state fibre, including
every address, history, reset, residence, frame and authenticated parent
datum used by the next transition.  Every oriented macro edge
\(e:u\to v\) carries a bijection

\[
                         R_e:\Omega_u\longrightarrow\Omega_v.       \tag{0.1}
\]

The reverse orientation is a formal dart labelled by \(R_e^{-1}\), whether
or not the reverse packet is physically executable.  Parallel physical
records remain distinct geometric edges.  For a walk \(W\) in this
geometric multigraph, write \(R_W\) for the composition of its edge maps,
in traversal order.

The following are equivalent.

1. Every closed macro walk has identity continuation holonomy.
2. The fundamental closed walks determined by one spanning tree have
   identity holonomy.
3. There are fibre gauges \(g_v:\Omega_v\to\Omega_*\) into one reference
   set such that

   \[
                            R_e=g_v^{-1}g_u                 \tag{0.2}
   \]

   for every edge \(e:u\to v\).

Under these conditions every rooted block-Euler circuit has identity full
continuation holonomy, independently of its order.  Thus the stronger
certificate of \(|E|-|V|+1\) exact fundamental-cycle checks can avoid an
Euler-order search; \(|E|\) counts geometric edges, not both oriented
darts.  Flatness is sufficient, not necessary, for the existence of a
closing Euler order.

If the macro graph is the one-skeleton of a simply connected prepared
2-complex and every face boundary has identity continuation action, then
the gauge exists automatically.  More generally it is enough that the
chosen face boundaries normally generate the fundamental group.  Thus a
packet system built from a Cayley complex needs only its local involution,
commutation and braid relations checked on the **complete** continuation
state.

This criterion is deliberately full-state.  Additive lower-current
cancellation, equality of projected flags, or flatness after forgetting
addresses does not imply (0.2).

For the present OR-word packets, bijectivity is itself an open lifting
condition.  A bare residence-age update is generally noninvertible: a
refresh merges several old ages into age zero, while a nonrefresh at the
deadline is only partially defined.  It becomes eligible for this theorem
only after restricting to a fully scheduled singleton fibre or enlarging
the state by enough discarded provenance to make every transition
bijective.  The same warning applies to partial address transports.

## 1. Walk holonomy

For a walk

\[
 W=(v_0\xrightarrow{e_1}v_1\xrightarrow{e_2}\cdots
          \xrightarrow{e_t}v_t),
\]

put

\[
                    R_W:=R_{e_t}\circ\cdots\circ R_{e_1}.          \tag{1.1}
\]

Backtracking cancels because the reverse edge carries the inverse map.
Consequently \(R_W\) depends only on the reduced edge path and gives a
groupoid representation of the fundamental groupoid of \(\Gamma\).

Fix a root \(o\), a spanning tree \(T\), and for each vertex \(v\) let
\(P_v\) be the unique tree path from \(o\) to \(v\).  For a chord
\(e:u\to v\), define the rooted fundamental loop

\[
                      C_e=P_u\,e\,P_v^{-1}.                         \tag{1.2}
\]

There is one such loop for every unoriented chord; these loops freely
generate \(\pi_1(\Gamma,o)\).

## 2. The flat-gauge theorem

### Theorem 2.1 (flat continuation gauge)

For a connected macro graph with bijective edge transports, the following
are equivalent.

* **(F1)** \(R_W=\mathrm{id}_{\Omega_v}\) for every closed walk based at
  every \(v\).
* **(F2)** \(R_{C_e}=\mathrm{id}_{\Omega_o}\) for every chord \(e\notin T\).
* **(F3)** There is a reference fibre \(\Omega_*\) and bijections
  \(g_v:\Omega_v\to\Omega_*\) satisfying (0.2) on every oriented edge.

When they hold, the transport along any walk from \(u\) to \(v\) is

\[
                               R_W=g_v^{-1}g_u.                     \tag{2.1}
\]

#### Proof

Clearly (F1) implies (F2).

Assume (F2), take \(\Omega_*=\Omega_o\), and define

\[
                              g_v:=R_{P_v}^{-1}.                    \tag{2.2}
\]

For a tree edge, (0.2) follows immediately from the definitions, with the
orientation handled by inversion.  For a chord \(e:u\to v\), the identity
on \(C_e\) says

\[
 R_{P_v}^{-1}R_eR_{P_u}=\mathrm{id}_{\Omega_o},
\]

so

\[
 R_e=R_{P_v}R_{P_u}^{-1}=g_v^{-1}g_u.
\]

Thus (F3) holds.

Finally, under (F3), a walk telescopes:

\[
 (g_{v_t}^{-1}g_{v_{t-1}})\cdots
 (g_{v_1}^{-1}g_{v_0})=g_{v_t}^{-1}g_{v_0}.
\]

This is (2.1), and it is the identity for a closed walk.  Hence (F3)
implies (F1). \(\square\)

### Corollary 2.2 (Euler-order independence)

Suppose a completed rotor has a weakly connected balanced macro support,
so block-Euler circuits exist, and suppose its complete continuation maps
satisfy Theorem 2.1.  Then every rooted block-Euler circuit returns its
initial complete continuation state.  No Euler-order search and no terminal
continuation sidecar are required.

#### Proof

Every Euler circuit is a closed macro walk.  Apply (F1). \(\square\)

The conclusion concerns continuation holonomy only.  A simultaneous global
physical packing is still required.  It is absorbed into this certificate
only through the common-\(\pi\), label-preserving construction of Section 4,
or through a separately proved coherent-lifting alternative.

## 3. Local face certificates

Let \(X\) be a connected 2-dimensional CW complex whose one-skeleton is
\(\Gamma\).  Give every oriented edge the transport (0.1).  For an oriented
2-cell \(f\), let \(\partial f\) be its boundary walk.

### Theorem 3.1 (local flatness)

Suppose

\[
                              R_{\partial f}=\mathrm{id}            \tag{3.1}
\]

for every 2-cell.  If \(X\) is simply connected, then the equivalent
conditions of Theorem 2.1 hold.

More generally, they hold whenever the conjugates of the face boundaries
normally generate \(\pi_1(\Gamma,o)\).

#### Proof

The edge transports define a homomorphism

\[
 \rho:\pi_1(\Gamma,o)\longrightarrow\operatorname{Sym}(\Omega_o).
\]

Condition (3.1) places every face boundary in \(\ker\rho\), and therefore
places their normal closure in \(\ker\rho\).  Under the stated hypothesis
that normal closure is all of \(\pi_1(\Gamma,o)\).  Hence \(\rho\) is
trivial, which is (F1). \(\square\)

### Corollary 3.2 (presentation certificate)

Suppose a prepared macro bank is the Cayley one-skeleton of a finite group
presentation

\[
                         \langle s_1,\ldots,s_t\mid\mathcal R\rangle,
\]

and its continuation transports are bijections.  If every **translated
defining-relator face** in \(\mathcal R\) acts trivially on its complete
continuation fibre, then the continuation gauge is flat.

In a Coxeter-type bank, the required local checks are the translated
involution and all defining braid faces (including every required braid
length); for example

\[
                 s_i^2=1,\qquad s_is_j=s_js_i,
                 \qquad s_is_js_i=s_js_is_j.                         \tag{3.2}
\]

The statement is not valid for a general Schreier graph without also
checking generators of the vertex stabilizer: a closed Schreier walk may
represent a nonidentity stabilizer element even when all presentation
relators act trivially.

## 4. Joint-capacity version

The exact regenerated-rotor criterion couples continuation states to one
global physical assignment.  The flat-gauge theorem can absorb this
coupling, but only by enlarging the state honestly.

Fix a nonempty set \(\Pi_0\) of complete, capacity-faithful,
occurrence-labelled packings of the entire packet bank, and put

\[
 \widehat\Omega_v=
 \coprod_{\pi\in\Pi_0}\Omega_v(\pi),                \tag{4.1}
\]

where every slice is nonempty.  Suppose every edge record preserves the
same global packing label and induces bijections

\[
 R_{e,\pi}:\Omega_u(\pi)\longrightarrow\Omega_v(\pi)
 \qquad(\pi\in\Pi_0).                                \tag{4.2}
\]

### Corollary 4.1 (capacity-faithful flat gauge)

If the fundamental-cycle or local-face certificate holds for the resulting
disjoint-union maps \(\widehat R_e\), then every block-Euler circuit has a compatible
capacity-faithful continuation chain and returns its enlarged initial
state.

#### Proof

Apply Theorem 2.1 to the enlarged fibres. \(\square\)

This is a strong sufficient condition, not a free rectangularization
theorem.  Locally extendible packing restrictions modulo a compositional
quotient need not arise from one global packing.  If a quotient is retained
instead of the disjoint union above, one additionally needs a coherent
path-lifting or amalgamation theorem and trivial kernel holonomy.  If an
edge relation is partial or many-to-many, replacing it by a nonempty
projected relation also loses the conclusion: nonempty relations need not
compose, and different local relations may require incompatible global
packings.

## 5. Sharp scope boundaries

### 5.1 Additive cancellation is insufficient

Take one macro vertex with one loop whose complete continuation action is a
transposition of two addresses.  Give the loop zero owner, lower, upper and
compiler current.  All additive signatures vanish, but the continuation
holonomy is nontrivial.  Theorem 2.1 detects the loop as a failed
fundamental-cycle check.

### 5.2 Projected flatness is insufficient

Let the complete fibre be \(\{0,1\}\times\{a,b\}\), project away the second
coordinate, and let one loop swap \(a,b\) while fixing \(0,1\).  The
projected gauge is flat and the full gauge is not.

### 5.3 Cycle-space checks are insufficient in the nonabelian case

Checking only a basis of the binary cycle space is not, by itself, a
nonabelian holonomy certificate.  One must check fundamental loops, or face
boundaries whose **normal closure** is the full fundamental group.  The
spanning-tree certificate of Theorem 2.1 is always safe.

### 5.4 A Schreier bank needs stabilizer checks

Local presentation relators identify words representing the same group
element.  In a Schreier graph, a nonidentity stabilizer element is still a
closed walk.  Its continuation action must also be checked.  A Cayley bank
has trivial stabilizers and avoids this extra row.

## 6. Consequence for the regenerating-bank programme

The current completed-rotor theorem asks for some rooted block-Euler order
whose complete continuation relation closes.  The present theorem gives a
stronger, order-independent sufficient route through either of two exact
tasks:

1. choose a spanning tree of the fixed macro support and verify identity on
   every fundamental loop; or
2. construct the support as a simply connected packet complex and verify a
   finite family of local face relations on the complete state.

In particular, a prospectively prepared Coxeter packet bank does not need a
separate global holonomy search if its local involution/commutation/braid
relations hold after including addresses, histories, residence flags,
reset data and every authenticated packing coordinate.

Flatness does not characterize the weaker Euler-order existential.  For
example, on one macro vertex take two distinct loop occurrences whose maps
are the same nonidentity transposition \(\tau\).  Either two-edge Euler word
has product \(\tau^2=I\), although each fundamental loop is nonflat.

Together with the rotor-router and value-fibre theorems, the remaining
all-dimensional target can be stated as follows.

> **Flat completed physical rotor-router.**  Construct one fixed child in
> which the packet macro support is connected and balanced; its complete
> continuation transports admit the flat certificate above; its
> claim-to-port router has bounded Hall defect; its suffix-port gammoid has
> bounded corank; and its changed physical cells form a literal value
> coboundary in one common final cap state.

The router-corank theorem then closes supplier rank up to the two bounded
coranks, the value-fibre theorem closes the lower compiler, and the present
theorem closes continuation holonomy.  What remains is geometric existence
of this one common child and the bounded exterior/ray interface.  No
unconditional \(B(k)+O(1)\) conclusion is claimed here.
