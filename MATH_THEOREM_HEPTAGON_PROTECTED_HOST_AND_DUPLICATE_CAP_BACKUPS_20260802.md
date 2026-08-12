# Protected heptagon hosts and duplicate-cap backup planting

**Date:** 2026-08-02  
**Status:** unconditional static terminal owner/q1 host with local cap backups;
global upper decoration, bounded components, residence completion, source, and
compiler remain open.

## 1. Setting

Let `ML_m` be the containment graph between ranks `m-1` and `m` of
`[2m-1]`.  A projected Johnson edge

\[
 A-F-B,qquad F=A\cap B,                                  \tag{1.1}
\]

is a two-edge path in `ML_m`.  Its immediate-upper colour is

\[
                            U=A\cup B,                    \tag{1.2}
\]

of rank `m+1`.

The small protected-factor theorem available in the repository is:

> Every 2-bounded subgraph `P subset ML_m` with `|E(P)|<=m-2` is contained
> in a spanning two-factor of `ML_m`.

The theorem below applies it to the terminal plus state of the heptagonal
packet.  It does not try to embed the old and new states simultaneously.

## 2. The terminal heptagon is a legal protected bank

A terminal heptagon has seven rows

\[
                         x_{i+1}-f_i-y_i.                 \tag{2.1}
\]

When the packet anchors are private, the seven facets, seven moving owners,
and seven retained owners are distinct.  Therefore its incidence lift has
exactly 14 edges and maximum degree two.  A bank of `H` vertex-disjoint
terminal heptagons has

\[
                         14H                              \tag{2.2}
\]

incidence edges and remains 2-bounded.

More generally, let `P` contain this terminal bank together with any
specified compatible incidence collars.  Assume

\[
 \Delta(P)\le2,qquad |E(P)|=L.                           \tag{2.3}
\]

Every owner/facet occurrence and every history interval wholly contained in
these collars survives any two-factor completion literally.

## 3. Exact duplicate-cap provider geometry

Fix a rank-`m+1` cap `U`.  Its rank-`m` owners are

\[
                         U\setminus\{a\},qquad a\in U.  \tag{3.1}
\]

Every unordered pair `a,b in U` gives one provider

\[
 U\setminus\{a\}
   -U\setminus\{a,b\}
   -U\setminus\{b\}.                                    \tag{3.2}
\]

Thus the provider graph is a complete graph `K_(m+1)` on the owner
vertices, and its edges have pairwise-distinct facet labels.  In particular
there are exactly

\[
                         {m+1\choose2}                    \tag{3.3}
\]

literal providers for `U`.

Suppose a protected bank forbids `a_U` of the owner vertices in (3.1) and
`b_U` of the provider facets in (3.2).

### Lemma 3.1 (sharp one-cap availability cut)

An allowed provider exists iff the forbidden facet set does not contain
every edge of the complete graph induced by the unblocked owner vertices.
In particular, the scalar condition

\[
                   {m+1-a_U\choose2}>b_U                \tag{3.4}
\]

guarantees an allowed provider, and is sharp given only `a_U,b_U`.

#### Proof

A provider is legal exactly when both of its owner endpoints and its unique
facet edge are unblocked.  After deleting the `a_U` owner vertices, all
remaining providers are the edges of `K_(m+1-a_U)`.  They are all destroyed
exactly when the forbidden facets cover this entire edge set. \(\square\)

## 4. Simultaneous fixed-bank backups

Let `Q={U_1,...,U_q}` be the old cap values which require explicit backup in
the terminal state.  We ask for a deliberately strong solution: the chosen
provider paths are vertex-disjoint from `P` and from one another.

Write `v_O(P)` and `v_F(P)` for the number of owner and facet vertices met by
`P`.

### Theorem 4.1 (greedy duplicate-cap backup planting)

If

\[
 {m+1-v_O(P)-2q\choose2}>v_F(P)+q,                       \tag{4.1}
\]

then one can select one provider for every cap in `Q`, with all selected
provider paths mutually vertex-disjoint and disjoint from `P`.

#### Proof

Choose the caps sequentially.  Before step `j`, at most `v_O(P)+2(j-1)`
owner vertices and `v_F(P)+(j-1)` facet vertices are forbidden.  Condition
(4.1) is the worst-case form of (3.4), so a provider remains.  Add its two
owners and one facet to the forbidden bank and continue. \(\square\)

The condition is intentionally simple and worst-case.  It does not assume
that the caps are distinct, although repeated requests for one cap can be
handled more economically by a matching in its provider clique.

## 5. Unconditional static protected-host theorem

### Theorem 5.1 (terminal heptagon plus local upper backups)

Let `P` be a compatible 2-bounded terminal heptagon/collar bank satisfying
(2.3), and let `Q` be its required old-cap backup list.  If (4.1) holds and

\[
                         L+2q\le m-2,                    \tag{5.1}
\]

then there is a spanning two-factor of `ML_m` which contains:

1. every terminal heptagon row in `P`;
2. every protected collar/history incidence in `P`; and
3. one additional provider of every cap in `Q`.

Consequently the projected factor has every rank-`m-1` facet exactly once,
every rank-`m` owner of degree two, every new packet cap, and every named old
packet cap.

#### Proof

Apply Theorem 4.1.  Each selected provider contributes a disjoint two-edge
incidence path, so the enlarged bank `P*` is 2-bounded and has `L+2q` edges.
Condition (5.1) allows the small protected-factor theorem to extend `P*` to
a spanning two-factor.  Projection gives the owner and lower-palette rows.
The packet rows supply their new caps and the selected providers supply all
members of `Q`. \(\square\)

### Corollary 5.2 (fixed-`H` asymptotic host)

For fixed `H`, suppose the complete terminal collar bank has

\[
                         L=O(Hd),\qquad q\le7H,           \tag{5.2}
\]

where `d=Theta(sqrt(m))`.  Then (4.1) and (5.1) hold for all sufficiently
large `m`.  Hence any fixed compatible bank of terminal heptagons, their
literal `O(d)` collars, and all locally displaced cap values embeds in an
exact owner/q1 two-factor.

This closes the static owner/facet/local-cap collision row for fixed `H`.

The same proof is not limited to a constant number of caps.  If

\[
 L=o(m),\qquad q=o(m),                                    \tag{5.3}
\]

then (4.1) holds asymptotically; if additionally `L+2q<=m-2`, Theorem 5.1
applies.  In particular an `O(d)` protected bank and `O(d)` named cap
backups are unconditionally plantable when `d=Theta(sqrt(m))`.  What cannot
be handled this way is a Catalan- or width-scale global upper deficit.

At the authenticated `k=17` floor 2,567, the complete cap-load histogram is

```text
load 1: 16,762
load 2:  1,581
load 3:    102
load 4:    935
load 5:     68
```

The 19,448 cap values carry 24,310 edges, as required.  Thus there are 2,686
duplicated cap colours and 4,862 spare cap units, but they are highly
nonuniform.  Aggregate duplicate mass is ample for a fixed packet bank; the
provider theorem is needed because the relevant old cap values must receive
the backups at the correct literal owner/facet resources.

## 6. What “protected history” means here

The completion preserves every specified owner and incidence in `P`.
Therefore it preserves:

* every residence run whose two boundaries lie inside a protected collar;
* every interval-OR witness wholly contained in that collar; and
* the endpoint transfer state explicitly determined by the protected part.

It does **not** determine the unprotected continuation of a collar.  In
particular, an external run may enter a collar with an unknown age, and an
arbitrary completion may pair packet ports in the wrong global order.  A
full bi-resident reset collar for all coordinates generally needs linear,
not `O(d)`, support: every coordinate absent at a seam would need a nearby
one to reset its zero-gap state, and every present coordinate would need a
nearby zero to reset its positive-run state.

Thus Theorem 5.1 protects a declared finite boundary history; it does not
prove that the history is accepting independently of the exterior.  The
heptagon host-spread lemma must still produce an accepting exterior pairing
or a bounded accepting return.

### 6.1 Exact coupling once complete history tickets are available

The cap-backup layer does not have to be selected in the same probabilistic
or Hall product as the history tickets.  This gives a useful exact separation.

For task `i`, let `G_i` be a family of **complete terminal tickets**.  A ticket
is required to contain all of the following literal data, not just an
algebraic heptagon label:

* both authenticated phase rows and their exterior-history replay;
* its source/compiler incidences and protected upper witnesses;
* its topology ports and residence boundary state; and
* its terminal plus-phase protected incidence bank `P(g)`.

Assume `P(g)` is 2-bounded and has at most `ell_d` incidence edges, and that
the ticket names at most seven old cap colours which need duplicate providers.
Put an edge between tickets from different task families precisely when their
literal data cannot coexist.  This includes owner/facet degree violations,
occurrence-resource collisions, source/compiler collisions, incompatible
exterior histories, topology-port collisions, or loss of a protected witness.

**Complete-ticket transversal theorem.**  Suppose the tasks are ordered and,
for every `i<j`, each ticket in `G_i` conflicts with at most `D_ij` tickets in
`G_j`.  If

\[
 |G_j|>\sum_{i<j}D_{ij}\qquad(1\le j\le H),             \tag{6.1}
\]

then one can choose pairwise compatible tickets, one from every `G_j`.

**Proof.**  Choose greedily in the displayed order.  After the first `j-1`
choices, at most `sum_{i<j} D_ij` candidates of `G_j` are forbidden, so (6.1)
leaves a candidate.  The definition of conflict makes the resulting union a
literal compatible protected bank.  `square`

In particular, if every cross-family conflict bound is at most `D_0`, it is
enough that

\[
 |G_j|>(H-1)D_0.                                       \tag{6.2}
\]

For the previously audited separated one-ear geometry, a selected centre
excludes at most `6d-3` candidate centres in another list.  If the remaining
literal-resource exclusions have maximum load `Delta_phys`, then

\[
 D_0=6d-3+\Delta_{\rm phys}                            \tag{6.3}
\]

is valid.  Equation (6.3) must not be applied to a generic heptagon macro:
it is available only when the complete ticket really has the audited
one-ear support and all additional physical conflicts are included in
`Delta_phys`.

Let `g_1,...,g_H` be tickets selected by (6.1), and put

\[
 P=\bigcup_i P(g_i),\qquad L=|E(P)|\le H\ell_d,
 \qquad q\le7H.                                        \tag{6.4}
\]

Duplicate-cap providers can now be chosen *after* the tickets.  Theorem 4.1
and the crude bounds `v_O(P),v_F(P)<=L` show that it is sufficient that

\[
 {m+1-H\ell_d-14H\choose2}>H\ell_d+7H.                \tag{6.5}
\]

The providers may then be chosen greedily, pairwise vertex-disjoint and
disjoint from `P`.  If also

\[
 H\ell_d+14H\le m-2,                                  \tag{6.6}
\]

the small protected-factor theorem extends the resulting bank to a spanning
owner/facet two-factor.  Thus the local cap backups create no additional
phase/history matching problem once the complete tickets have been selected.

If `ell_d=Ad+B`, (6.5)--(6.6) hold for every fixed `H` and all sufficiently
large `m`, since `d=Theta(sqrt(m))`.  More generally they allow
`H=O(m/d)` with a sufficiently small constant depending on `A`; they do not
allow a Catalan-scale task bank.

There are two standard alternatives to the elementary greedy condition, but
neither supplies the missing ticket families.  If the complete-ticket
conflict graph has maximum degree `Delta`, Haxell's independent-transversal
theorem gives a transversal when every part has size at least `2 Delta`.
For equal part size `K`, independently choosing one ticket per task and using
the conflict pairs as bad events gives the symmetric local-lemma condition

\[
 e\,{2K\Delta+1\over K^2}<1,                           \tag{6.7}
\]

for example `K>=4e Delta` when `Delta>=1`.  If only a per-pair bound `D_0`
is known, then `Delta` may be `(H-1)D_0`, so (6.7) gives no asymptotic gain
over (6.2).

Most importantly, the prospective `Theta(k^7)` rooted-heptagon count is not
`|G_i|`.  A fixed old chronology can collapse a prospective atlas to one
literal phase, and the source, compiler, exterior-history, and residence
tests can reject every algebraic label.  The unconditional result is
therefore exactly this:

> complete history tickets with the spread bound (6.1) can be coupled, and
> their `O(H)` named cap backups can subsequently be planted and extended.

The remaining host-history theorem must prove positive supply and spread for
the **complete** ticket families.  Raw heptagon abundance, one-point
marginals, or aggregate duplicate-cap slack do not imply it.

## 7. The global adjacent-upper gate remains integral

Theorem 5.1 covers all packet-affected caps, but its arbitrary two-factor
completion need not cover every other rank-`m+1` cap.  The global selector
has one variable for every Johnson edge and constraints

\[
\begin{array}{ll}
\text{each rank-}(m-1)\text{ facet:}&=1,\\
\text{each rank-}m\text{ owner:}&=2,\\
\text{each rank-}(m+1)\text{ cap:}&\ge1,\\
\text{protected rows:}&=1.
\end{array}                                               \tag{7.1}
\]

There is no unprotected fractional obstruction.  Give every Johnson edge
weight `1/binom(m,2)`.  A fixed facet supports `binom(m,2)` edges, a fixed
owner has degree `m(m-1)`, and a fixed cap supports `binom(m+1,2)` edges.
Consequently

\[
 \sum_{e:f(e)=f}x_e=1,
 \qquad
 \sum_{e\ni v}x_e=2,
 \qquad
 \sum_{e:U(e)=U}x_e=\frac{m+1}{m-1}>1.                  \tag{7.2}
\]

Thus the uniform point satisfies both equality rows exactly and every cap
row with strict slack `2/(m-1)`.

Separate Hall cuts likewise have strict surplus.  For every cap family
`A`, incidence counting gives

\[
 |N_{owners}(A)|\ge\frac{m+1}{m-1}|A|,
 \qquad
 |N_{facets}(A)|\ge\frac{m+1}{m-1}|A|.                  \tag{7.4}
\]

The obstruction is correlated integral rounding: one must choose the same
provider edge for its cap, two owner capacities, and its facet row.  The
degree-two edge system is not a matroid, so ordinary Rado or two-matroid
intersection does not apply.  This is precisely the ordered Boolean-diamond
correlation already isolated elsewhere in the repository.

The protected bank consumes only `O(Hd)` resources.  The uniform cap slack
is only `Theta(1/m)` per cap, while the facet and owner rows are exact, so a
naïve perturbation does not absorb a fixed integral row automatically.  A
protected upper-decorated completion requires an absorber or a conflict-free
exact matching theorem, not another aggregate count.

### 7.1 Exact fractional Farkas cut after a protected bank

Assume for this paragraph that the protected bank is a union of complete
projected Johnson rows.  Delete its fixed variables and put

\[
 b_f=1-d_P(f),\qquad b_v=2-d_P(v),\qquad
 c_U=(1-M_P(U))_+.                                      \tag{7.5}
\]

For every remaining allowed edge `e`, write `f(e)` for its facet,
`u(e),v(e)` for its owner endpoints, and `U(e)` for its cap.  The residual
fractional selector is feasible iff the following implication holds for
every choice of free real numbers `alpha_f,beta_v` and nonnegative
`gamma_U`:

\[
 \alpha_{f(e)}+\beta_{u(e)}+\beta_{v(e)}+\gamma_{U(e)}
 \le0\quad\text{for all allowed }e                       \tag{7.6}
\]

implies

\[
 \sum_f b_f\alpha_f+
 \sum_v b_v\beta_v+
 \sum_U c_U\gamma_U\le0.                                \tag{7.7}
\]

#### Proof

This is Farkas' lemma for the system consisting of the facet and owner
equalities, the cap lower bounds, and nonnegative edge variables.  Directly,
multiply the equalities by `alpha,beta` and the cap inequalities by
`gamma>=0`.  Under (7.6), every nonnegative variable has nonpositive total
coefficient, forcing (7.7).  The converse is the separating-hyperplane form
of Farkas' lemma. \(\square\)

Thus a violated `(alpha,beta,gamma)` is a sharp fractional protected-host
certificate.  Separate owner Hall, facet Hall, and cap counts are merely
special projections of this cut.  Even when every such fractional cut
passes, an integral selector can still fail because the owner-degree-two
edge family is not a matroid and the four named resources must be rounded
on the same edge occurrences.

### 7.2 Exact topology row

For an integral solution of (7.1), connectedness is equivalent to the
subtour inequalities

\[
                     x(\delta(S))\ge2                    \tag{7.8}
\]

for every nonempty proper owner set `S`.  Degree two makes every disconnected
component violate (7.8), while a connected two-regular graph is one cycle.

Thus the protected upper-decorated Hamilton host is exactly the integer
system (7.1), (7.8).  The fixed-`z` heptagon lies in the integer kernel of
the owner, facet, and cap-multiset rows; Theorem 2.2 of the heptagon note
shows that on a seven-component support it strictly repairs the subtour
structure.  This identifies a concrete two-stage route:

1. round the protected upper selector to any integral two-factor; then
2. prove that its cap-exact heptagon connector hypergraph crosses every
   remaining component partition.

The second statement is not implied by ordinary Johnson expansion, because
all seven old rows must already be selected and must share one coherent
heptagon label pattern.

## 8. Boundary of the theorem

The strongest unconditional conclusion is

\[
\boxed{
 \text{fixed terminal heptagons + compatible collars + local cap backups}
 \Longrightarrow
 \text{one exact owner/q1 two-factor containing them}.}
\]

Still open, and explicitly not inferred, are:

1. global rank-`m+1` upper surjectivity;
2. one component or `O(H)` components;
3. accepting exterior residence histories and arbitrary-width uppers;
4. a depth-`d` literal source antecedent; and
5. the integral lower compiler/common cap.

The next genuine theorem is a **protected upper-decorated completion** of
(7.1), preferably with bounded component count.  The local duplicate-cap
bank itself is no longer an obstruction for fixed `H`.
