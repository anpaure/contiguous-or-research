# Protected wedges and static pull hosts: the exact cut condition and quantifier obstruction

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical composition theorem, exact
fixed-host cut characterization, and sharp menu-to-host obstruction.  No
search or computational construction is used.  The theorem reduces
Hamiltonization of a protected wedge bank to one named transparent-pull cut
condition.  It does not prove that the arbitrary two-factor supplied by the
small protected-factor theorem has such a host.

## 0. Main result

Let `D` be the `2p`-edge bank of `p` full wedges selected by the protected
wedge-packing theorem, and let `F` be a spanning Middle-Levels two-factor
containing `D`.

Fix a static tree-compatible family of strict two-component pull circuits
for `F`, with auxiliary multigraph `H` on the components of `F`.  Delete
from `H` every pull whose old phase contains an edge of `D`, and call the
remaining graph `H_D`.

Then, relative to this fixed pull family,

\[
 \boxed{
 \text{there is a pull-tree Hamiltonization preserving every wedge}
 \iff H_D\text{ is connected}.}
\tag{0.1}
\]

Equivalently, every nontrivial component cut of `H` contains a pull whose
deleted factor edges avoid `D`.

If each factor edge belongs to at most `lambda` pull old-phases, then at
most `2p lambda` host edges are forbidden.  Hence host edge-connectivity

\[
                         \kappa(H)>2p\lambda
\tag{0.2}
\]

is a sufficient quantitative condition.  In the canonical GMN pull family
`lambda=1`, but its standard auxiliary host has edge-connectivity one, so
this numerical route gives no protection even for one wedge.  A wedge
meeting the old phase of its unique bridge disconnects the transparent
host.

There is also a sharp quantifier obstruction: in any fixed base factor,
each lower turn has exactly one factor-supported full wedge.  A menu of size
`binom(m,2)-1` can omit that wedge entirely.  Thus no menu-size theorem,
including the wedge-packing theorem, can lift its choices into a pull host
fixed before the wedges are chosen.  The factor and its static host must be
selected jointly with the wedge bank, or the resulting factor must be shown
to satisfy (0.1).

## 1. Static pull-host setup

Let `F` be a spanning two-factor of `ML_m`, with component set

\[
                         \mathcal C=\operatorname{Comp}(F).
\]

For every labelled edge `e` of a multigraph `H` on `mathcal C`, let `Z_e`
be an alternating circuit with old and new phases

\[
                         O_e\subseteq F,
 \qquad N_e\cap F=\varnothing.
\tag{1.1}
\]

Assume the family is **tree-compatible**:

1. for every graphic forest `T subseteq E(H)`, the switches
   `O_e -> N_e`, `e in T`, are simultaneously legal; and
2. their effect on factor components is exactly contraction of the edges
   of `T`.

Thus a spanning tree of `H` turns `F` into one spanning cycle.  This is the
static compatibility supplied by the canonical pull family and assumed in
the general preselected-switch theorem.

Let `D subseteq F` be a protected edge bank.  In the wedge application,
`D` is the union of both incidence edges at each selected lower turn.
Define

\[
 B_D=\{e\in E(H):O_e\cap D\ne\varnothing\},
 \qquad
 H_D=H-B_D.
\tag{1.2}
\]

## 2. Exact support transparency

### Lemma 2.1

A pull `e` preserves every protected edge in `D` if and only if

\[
                         O_e\cap D=\varnothing.
\tag{2.1}
\]

When `D` contains both factor incidences at a lower turn `L`, every pull
satisfying (2.1) preserves the complete turn and its q1 upper value.

#### Proof

The switched factor is `(F-O_e) union N_e`, with the two phases disjoint.
An edge of `D subseteq F` survives exactly when it is not deleted, proving
(2.1).

If both incidences at `L` survive, they already give degree two at `L` in
the switched two-factor.  They remain its two factor neighbours, so their
intersection root and their owner union are unchanged.  The q1 upper value
selected by that full wedge is therefore unchanged. \(\square\)

This is **support transparency**.  A pull which preserves the two wedge
edges may still alter an unnamed residence witness, compiler cell, external
history, or cap resource.  Those stronger notions require enlarging `D` to
the complete protected resource state and redefining `B_D` accordingly.

## 3. The protected pull cut theorem

### Theorem 3.1 (exact fixed-host criterion)

Assume `H` is connected and the pull family is tree-compatible.  There is a
spanning pull tree whose switches preserve `D` if and only if `H_D` is
connected.

Equivalently,

\[
 \boxed{
 \delta_H(X)\nsubseteq B_D
 \quad\text{for every }
 \varnothing\ne X\subsetneq\mathcal C.}
\tag{3.1}
\]

When these conditions hold, applying the pull tree gives one spanning
Middle-Levels Hamilton cycle containing every edge of `D`, hence every
selected full wedge and its q1 terminal value.

#### Proof

Any pull tree preserving `D` uses only labels outside `B_D`, so it is a
spanning tree of `H_D`; necessity follows.

If `H_D` is connected, choose an ordinary labelled spanning tree
`T subseteq E(H_D)`.  Tree compatibility makes all its switches legal and
contracts every component of `F` to one.  Lemma 2.1 says every switch
preserves `D`.  Thus the final factor is one spanning cycle containing
`D`.  The cut formulation is the standard characterization of graph
connectivity. \(\square\)

### Corollary 3.2 (preselected pull portals)

Suppose a task construction additionally prescribes a labelled pull set
`A subseteq E(H_D)`.  A `D`-transparent spanning pull tree containing every
edge of `A` exists if and only if

\[
                         H_D\text{ is connected}
 \quad\text{and}\quad
                         A\text{ is a graphic forest in }H_D.
\tag{3.2}
\]

#### Proof

Necessity is immediate.  For sufficiency, graphic basis extension enlarges
the forest `A` to a spanning tree of the connected graph `H_D`, then apply
Theorem 3.1. \(\square\)

Thus a portal-to-pull lift must prove two logically separate rows:

1. each attached portal label is an actual `D`-transparent host edge and the
   selected labels form a forest; and
2. the residual transparent host satisfies the cut condition (3.1).

Raw Johnson adjacency or a forest before quotienting does not imply either
row.

## 4. Exact load bound and its limit

For a factor edge `d in F`, put

\[
 \lambda(d)=|\{e\in E(H):d\in O_e\}|,
 \qquad
 \lambda=\max_{d\in F}\lambda(d).
\tag{4.1}
\]

### Proposition 4.1

If `|D|=2p`, then

\[
                         |B_D|\le2p\lambda.
\tag{4.2}
\]

Consequently (0.2) implies the cut condition (3.1).

#### Proof

Count incidences `(d,e)` with `d in D cap O_e`.  Every forbidden pull has
at least one such incidence, while each protected edge contributes at most
`lambda` incidences.  This gives (4.2).

Deleting fewer than `kappa(H)` edges cannot disconnect an
`kappa(H)`-edge-connected multigraph.  Equations (4.2) and (0.2) therefore
make `H_D` connected. \(\square\)

In the canonical GMN family, pull circuits are pairwise edge-disjoint, so

\[
                         \lambda=1,
 \qquad |B_D|\le2p.
\tag{4.3}
\]

This bound is exact as a load statement but does not imply connectivity:
the standard labelled plane-tree host has a bridge.  If a selected wedge
edge belongs to the old phase of that bridge pull, then the bridge lies in
`B_D` and `H_D` is disconnected.  Thus a single protected edge can destroy
all transparent pull trees even though the total forbidden load is one.

## 5. Composition with protected wedge packing

The wedge-packing theorem selects `p` full wedges with pairwise distinct
lower turns, owners, and q1 terminal values.  Under its factor-compatibility
and edge-count rows, the small protected-factor theorem supplies at least
one spanning two-factor `F` containing their `2p`-edge union `D`.

### Corollary 5.1 (wedge packing plus the protected pull cut)

If one such completion `F` admits a connected tree-compatible pull host `H`
whose `D`-transparent subhost satisfies (3.1), then `ML_m` has a Hamilton
cycle containing all selected wedges.  If prescribed task-pull labels are
also required, add exactly the forest condition (3.2).

No further topology hypothesis is needed.

#### Proof

The wedge theorem and small protected-factor theorem give `D subseteq F`.
Apply Theorem 3.1, or Corollary 3.2 when task pulls are prescribed. \(\square\)

This is the shortest unconditional implication currently available.  Its
remaining premise is one named graph condition on the factor completion:

### Protected Pull Cut `PPC(F,D,H)`

\[
 \boxed{
 \text{for every nontrivial component cut of }F,
 \text{ some strict compatible pull crosses it and deletes no edge of }D.}
\tag{5.1}
\]

`PPC` is necessary and sufficient for Hamiltonization **inside the fixed
static host `H`**.  It is not claimed necessary for a different pull family
or an arbitrary Hamilton cycle containing `D`.

## 6. Sharp static-host quantifier obstruction

Fix any base factor `F`.  At a lower turn `L`, degree two gives exactly two
factor owners, hence exactly one factor-supported full wedge; call it
`w_F(L)`.

### Theorem 6.1 (abundance cannot lift into a pre-fixed host)

For every `m>=3` and every fixed factor `F`, the menu

\[
 \mathcal W_F^-(L)
 =\binom{[2m-1]\setminus L}{2}\setminus\{w_F(L)\}
\tag{6.1}
\]

has size

\[
                         {m\choose2}-1,
\tag{6.2}
\]

yet contains no wedge supported by `F`.

Consequently, even menus of asymptotically full size do not imply that a
selected wedge is present in a factor and pull host fixed independently of
the menu selection.

#### Proof

Every wedge supported by `F` at `L` must use the two factor incidences at
`L`; their unordered owner pair is unique.  Removing that one pair removes
every factor-supported wedge while leaving (6.2) candidates. \(\square\)

The same construction at any collection of distinct lower turns gives
large menus with no transversal embeddable in the pre-fixed factor.  Thus
the valid quantifier order is

\[
 \boxed{
 \text{choose wedges and factor/host jointly, or choose wedges first and
 prove `PPC` for an adaptive completion}.}
\tag{6.3}
\]

It is invalid to choose a canonical pull host first and infer a
wedge-to-host lift only from menu size and pairwise conflict bounds.

## 7. Exact frontier

The topology bridge created by wedge packing is now reduced to one exact
cut row:

\[
 \text{protected wedge packing}
 \Longrightarrow
 \text{some two-factor }F\supseteq D
 \xRightarrow{\operatorname{PPC}(F,D,H)}
 \text{Hamilton factor containing }D.
\]

What is proved unconditionally:

* support transparency is exactly avoidance of the two protected incidence
  edges of each wedge;
* relative to a static tree-compatible host, `PPC` is necessary and
  sufficient;
* forbidden-pull load is at most `2p lambda`; and
* abundance alone cannot lift wedges into a host chosen beforehand.

What remains open:

1. construct, jointly with the selected wedges, a factor completion with a
   tree-compatible host satisfying `PPC`;
2. or build a noncanonical redundant host with enough protected cut
   expansion;
3. if task pulls themselves are prescribed, lift them to a forest in that
   same host; and
4. preserve the full residence, upper-witness, and compiler state, for which
   edge support transparency alone is insufficient.

Thus the obstruction is no longer “component scattering.”  It is the
initial static-host cut

\[
                         H-B_D\text{ connected},
\]

together with the joint factor/host quantifier forced by Theorem 6.1.

## 8. Dependencies

| role | file |
|---|---|
| protected wedge packing and two-factor completion | `MATH_THEOREM_PROTECTED_TURN_DIAMOND_WEDGE_PACKING_20260804.md` |
| graphic basis extension and preselected switch completion | `MATH_THEOREM_PRESELECTED_PORTAL_FOREST_EXTENSION_AND_PULL_HOST_LIFT_GATE_20260801.md` |
| protected static-switch composition | `MATH_THEOREM_K_PROTECTED_SAFE_SWITCH_TREE_AND_HYPERTREE_COMPOSITION_20260802.md` |
| canonical pull edge-disjointness and host obstruction | `MATH_THEOREM_R_CANONICAL_MUTZE_PULL_COATOM_AND_RESIDENT_COLLAR_EMBEDDING_20260801.md` |

