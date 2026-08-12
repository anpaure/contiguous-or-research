# Signed palette-neutral packets: exact composition and positive-density packing

Date: 2026-08-01

## 1. Two graphs, two different signs

There are two logically separate objects.

1. The **static/common-live graph** is a bipartite graph
   (H=(L,R;E)).  A matching chooses mutually distinct live attachment
   resources.  Its sign is matching gain.
2. The **chronology graph** is a selected physical graph (P) on owner or
   attachment states.  Its components are actual paths/cycles.  Its sign is
   graphic-rank gain, equivalently component reduction.

A static rooted factor supplies (H), but it does not supply (P).  Thus a
positive Dulmage--Mendelsohn sign is not a chronology merge theorem.

The definitions below deliberately carry both witnesses.

## 2. Whole signed packets

Fix a bipartite graph (H_0=(L,R;E_0)) and a matching (M\subseteq E_0).
A **palette-neutral circuit packet** (x) contains:

* a literal factor replacement with zero signed palette/resource delta;
* a set (D_H(x)\subseteq E_0) of common-live incidences it invalidates;
* a set (A_H(x)) of common-live incidences it creates;
* a tuple (mathcal Q(x)) of explicitly listed (M)-augmenting paths in
  
  \[
  H_x=(H_0\setminus D_H(x))\cup A_H(x);
  \]
* a complete footprint listing every state, incidence, selected chronology
  edge, provider, and guard which the replacement can invalidate.

When a chronology graph (P) is also fixed, a **topologically signed packet**
additionally contains:

* selected old chronology edges (D_P(x)\subseteq E(P)) which are removed;
* selected new chronology edges (A_P(x));
* an explicitly designated independent link set (B_P(x)\subseteq A_P(x))
  after the retained graph has been contracted.

The packet is **(M)-stable** if (D_H(x)\cap M=\varnothing).

Two packet realizations conflict if any of the following holds:

* their literal root supports overlap;
* their augmenting witnesses share a vertex;
* one deletes an edge used by the other's witness;
* their physical footprints collide;
* their provider or guard tickets are incompatible;
* their selected chronology links cannot coexist.

This conflict definition is intentionally stronger than root-disjointness.
The (k=17) audit shows why: two changed roots can alter live status at other
roots through incoming/outgoing transition support.

## 3. Exact matching-composition theorem

For a graph (G\supseteq M), let (a_M(G)) be the maximum number of
pairwise vertex-disjoint (M)-augmenting paths in (G).

### Theorem 3.1 (augmenting-path packing identity)

If (M\subseteq E(G)), then

\[
\boxed{\nu(G)-|M|=a_M(G).}
\tag{3.1}
\]

### Proof

Toggling (M) along (t) vertex-disjoint (M)-augmenting paths gives a
matching of size (|M|+t).  Hence (a_M(G)\le\nu(G)-|M|).

Conversely, let (M^\star) be a maximum matching chosen to maximize

\(|M\cap M^\star|\).  Every component of (M\mathbin\triangle M^\star) is
an alternating cycle or path.  No component can have one more (M)-edge than
(M^\star)-edge, since toggling that component would augment the maximum
matching (M^\star).  The components having one more (M^\star)-edge are
pairwise vertex-disjoint (M)-augmenting paths, and their number is exactly
(|M^\star|-|M|).  Thus the reverse inequality holds.  ∎

Now let (S) be a packet family and put

\[
H_S=
\left(H_0\setminus\bigcup_{x\in S}D_H(x)\right)
\cup\bigcup_{x\in S}A_H(x).
\]

### Theorem 3.2 (stable signed composition)

Suppose:

1. every packet in (S) is (M)-stable;
2. the listed path tuples (mathcal Q(x)), (x\in S), are mutually
   vertex-disjoint;
3. every listed path survives every other packet's deletion footprint.

If (g_x=|\mathcal Q(x)|), then

\[
\boxed{\nu(H_S)\ge |M|+\sum_{x\in S}g_x.}
\tag{3.2}
\]

Equality holds if and only if, after toggling all listed paths, the resulting
matching has no augmenting path in (H_S).

### Proof

The hypotheses say that the union of the listed tuples is a collection of
(sum g_x) vertex-disjoint (M)-augmenting paths in (H_S).  Toggle them
simultaneously to obtain (3.2).  By Berge's lemma, the resulting matching is
maximum exactly when it has no augmenting path.  ∎

### Necessary-and-sufficient formulation

For prescribed gains (g_x), a packet family has matching gain at least
(sum g_x) if and only if (H_S) contains (sum g_x) vertex-disjoint
(M)-augmenting paths.  It has gain exactly (sum g_x) if and only if the
maximum such packing has that cardinality.

Thus explicit compatible packet witnesses are a sufficient certificate, and
Theorem 3.1 shows that existence of a witness packing is also necessary.  A
particular packetwise attribution of those paths need not be necessary because
augmenting paths may reroute across packet footprints.

## 4. A strong separability criterion

The residual no-augmenting-path test is exact but global.  The following
stronger hypothesis makes exact additivity local.

### Corollary 4.1 (separable packets)

Suppose the affected vertices split into disjoint sets (V_x), (x\in S),
such that:

* packet (x) changes only incidences induced by (V_x);
* every (M)-augmenting path using a changed incidence lies wholly in one
  (V_x);
* the local changed graph on (V_x) has gain exactly (g_x).

Then

\[
\nu(H_S)-|M|=\sum_{x\in S}g_x.
\]

This condition is sufficient, not necessary.  It explains exactly what the
bare phrase “root-disjoint packets compose” omits: root disjointness must be
upgraded to separation of the entire alternating-path footprint.

## 5. Exact graphic-rank composition

Now fix an actual chronology graph (P) on vertex set (V).  For a packet
family (S), put

\[
D_S=\bigcup_{x\in S}D_P(x),\qquad
A_S=\bigcup_{x\in S}A_P(x),\qquad
R_S=P\setminus D_S.
\]

Let (r_G(F)) be graphic rank and define the deletion toll

\[
\ell(S)=r(P)-r(R_S).
\]

### Theorem 5.1 (exact chronology sign)

The component reduction is

\[
\boxed{
c(P)-c(R_S\cup A_S)=r_{R_S}(A_S)-\ell(S).
}
\tag{5.1}
\]

### Proof

Since (c(G)=|V|-r(G)),

\[
c(P)-c(R_S\cup A_S)=r(R_S\cup A_S)-r(P).
\]

Use

\[
r(R_S\cup A_S)=r(R_S)+r_{R_S}(A_S)
\]

and the definition of (ell(S)).  ∎

### Theorem 5.2 (additive signed graphic composition)

Suppose each packet (x) is assigned integers (ell_x,h_x\ge0) and a link
set (B_P(x)\subseteq A_P(x)) such that:

1. deletion tolls add:
   
   \[
   \ell(S)=\sum_{x\in S}\ell_x;
   \]
2. each (B_P(x)) has size (ell_x+h_x);
3. the union (igcup_x B_P(x)) is independent in the graphic matroid after
   (R_S) is contracted.

Then

\[
\boxed{c(P)-c(R_S\cup A_S)\ge\sum_{x\in S}h_x.}
\tag{5.2}
\]

Equality holds exactly when

\[
r_{R_S}(A_S)=\sum_x(\ell_x+h_x).
\]

### Proof

Graphic independence gives

\[
r_{R_S}(A_S)\ge\left|\bigcup_xB_P(x)\right|
=\sum_x(\ell_x+h_x).
\]

Substitute the additive deletion toll into (5.1).  The equality statement is
immediate.  ∎

When (P) is a forest and the deleted edges are distinct, the deletion toll
is simply (|D_S|).  Theorem 5.2 then says that selected new links must form a
forest after the retained pieces are contracted and must outnumber the cuts
by the desired component gain.

## 6. Whole signed composition

### Corollary 6.1

Let (S) be a palette-neutral packet family satisfying Theorem 3.2 with
matching gains (g_x), and Theorem 5.2 with chronology gains (h_x).  Then
all packets may be applied simultaneously while:

* preserving every named static palette exactly;
* increasing common-live matching by at least (sum g_x);
* reducing chronology components by at least (sum h_x).

No implication is asserted between the two gains.  Both certificates must be
carried by the same literal packet realizations.

This is the signed composition theorem suggested by the (k=17) audit.

## 7. Matroid selection of topology links

Assume packets have been normalized so that their internal replacement pays
their deletion toll and each exports one additional candidate connector edge.
For task (i), let (mathcal E_i) be its menu of exported edges in the
contracted component graph.

### Theorem 7.1 (Rado connector transversal)

There is a choice (e_i\in\mathcal E_i) whose union is a forest if and only if

\[
\boxed{
r_{\rm gr}\!\left(\bigcup_{i\in J}\mathcal E_i\right)\ge |J|
\quad\text{for every task set }J.
}
\tag{7.1}
\]

### Proof

This is Rado's independent-transversal theorem applied to the graphic
matroid.  ∎

Equation (7.1), not the number of raw circuits, is the exact topology-side
Hall condition.

## 8. LLL selection of literal augmenting witnesses

Fix one independent connector (e_i) for each task using Theorem 7.1.  Let
(mathcal L_i(e_i)) be the literal packet realizations exporting that edge
and carrying a stable (M)-augmenting witness.

### Theorem 8.1 (conflict-free witness transversal)

Suppose every list has at least (L) realizations and every realization
conflicts with at most (Delta) realizations in other lists, where conflict
includes the complete matching and chronology footprints.  If

\[
\boxed{L>3e\Delta,}
\tag{8.1}
\]

then one can choose one realization from every list with no conflicts.

### Proof

Discard options so every list has size exactly (L), and choose independently
and uniformly.  For every conflicting pair of options, let the bad event be
that both are chosen.  Its probability is (L^{-2}).

A bad event involves two task lists.  At most (L\Delta) conflict events
involve either one, so its dependency degree is less than (2L\Delta).  The
symmetric Lovász local lemma applies when

\[
eL^{-2}(2L\Delta+1)<1,
\]

which follows from (8.1).  ∎

Because conflicts include shared witness vertices and cross-deletions, the
selected augmenting paths survive and are vertex-disjoint.  Because their
exported links were chosen by Rado, the topology links remain independent.

## 9. Positive-density signed-bank corollary

### Corollary 9.1

Suppose a construction exposes (h\ge\alpha N) normalized packet tasks for
some fixed (alpha>0), and:

1. the connector menus satisfy the Rado inequalities (7.1);
2. after fixing the Rado connectors, every task retains at least (L) whole
   literal realizations;
3. each realization conflicts with at most (Delta) others;
4. (L>3e\Delta).

Then there is a palette-neutral packet bank of size (h=\Theta(N)) with
additive common-matching gain (h) and additive chronology component
reduction (h).

### Proof

Rado first chooses independent exported topology links.  The local lemma then
chooses mutually compatible literal packets carrying those links and
vertex-disjoint stable augmenting witnesses.  Apply Corollary 6.1.  ∎

The asymptotic estimates proposed for buffered hexagons,

\[
L=\Omega(m^2),\qquad \Delta=O(md),\qquad d=O(\sqrt m),
\]

give (L/\Delta=\Omega(\sqrt m)), so the LLL row would eventually hold.
The genuinely unresolved row is then the Rado rank condition together with
production of whole stable witnesses—not raw packet abundance.

## 10. Why three-matroid language alone is insufficient

One may view the constraints as:

* a partition constraint choosing at most one realization per task;
* a disjoint-augmenting-path or gammoid constraint;
* a graphic-matroid constraint on chronology links.

There is no general integral theorem for the common independent sets of three
arbitrary matroids.  The two-stage Rado-plus-LLL statement avoids claiming
one: topology is selected by an exact matroid theorem, and all remaining
literal interactions are absorbed into a bounded-degree conflict system.

## 11. Relation to the finite (k=17) bank

The five Pareto circuits found in the (k=17) audit show that simultaneous
static/common gain is possible, but that audit did not export their actual
(M)-augmenting paths or any chronology forest.  Therefore they are evidence
for the packet definition, not certified instances of Corollary 6.1.

The next finite artifact should augment each selected circuit row with:

1. the incumbent matching-edge list it promises to preserve;
2. one explicit augmenting path;
3. the selected chronology cuts and replacement links;
4. the contracted-component IDs certifying relative graphic rank.

Only then does “component-reducing circuit” have a literal, compositional
meaning.

