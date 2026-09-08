# Joint optimization of the 3,807 residence cuts and the endpoint seams

**Date:** 2026-08-01  
**Status:** exact selector/master reduction, exact local-exchange theorem,
and a rigorous distance lower bound.  A finite H100 search proves that the
canonical-incumbent defect is not invariant, but does not find a zero-defect
minimum transversal.  This note does not prove or disprove
`nu(17)=24313`.

## 0. Reconciliation of the two endpoint audits

The raw endpoint audit in

```text
MATH_THEOREM_K17_3807_CUT_REJOIN_COLORED_FUNCTIONAL_HALL_20260801.md
```

found 28,395 unoriented Boolean seams for the deterministic rightmost-greedy
protected-avoiding minimum residence transversal emitted by its audit.  It found no dead endpoint
slot, cut colour, or cut-killed rank-ten colour.

The later audit

```text
MATH_THEOREM_K17_H2_MINCUT_BLOCK_ENDPOINT_THREE_RESOURCE_NOGO_20260801.md
```

is strictly stronger.  It orients every block and applies a deliberately
relaxed **necessary** two-block residence predicate.  Of 56,790 oriented raw
atoms, only 13,174 survive.  The filtered atlas has

\[
 1289\text{ zero cut colours},\qquad
 368\text{ dead outgoing blocks},\qquad
 368\text{ dead incoming blocks}.                            \tag{0.1}
\]

There is no contradiction.  The raw theorem separated its endpoint system
from the product residence automaton.  Its raw census was an optimistic
projection, not a feasibility claim.  The filtered audit proves that the
canonical emitted atomic block partition cannot satisfy the full system even at
singleton Hall.

The correct next quantifier is therefore

\[
 \boxed{\text{choose an optimal residence transversal and its endpoint
 seams jointly}.}                                             \tag{0.2}
\]

## 1. Every optimal circular transversal is a shortest path

Consider one old owner cycle with allowed gap set `A` and circular short-run
intervals `I_1,...,I_m`.  Every interval has length three or four in the
present factor.  Let its protected-avoiding transversal number be `c`.

Fix an allowed anchor \(a\in I_1\).  Remove the intervals containing `a`, cut
the circle immediately after `a`, and write the remaining intervals as

\[
                    J_i=[l_i,r_i]\quad(1\le i\le s),           \tag{1.1}
\]

ordered by nondecreasing right endpoint.  For an allowed point
\(q\in J_i\), define

\[
 n(i,q)=\min\{j>i:l_j>q\},                                   \tag{1.2}
\]

with value `s+1` if the set is empty.  Since \(r_j\ge r_i\ge q\) for every
later interval, `J_j` contains `q` exactly when \(l_j\le q\).  In this
specific instance the left endpoints are nondecreasing as well: every
interval has length three or four, so increasing the integer right endpoint
cannot decrease the left endpoint; ties are ordered by increasing left
endpoint.  Hence the intervals hit by `q` are a consecutive block and
(1.2) is well-defined as the next unhit state.

Define

\[
 f(s+1)=0,\qquad
 f(i)=1+\min_{q\in A\cap J_i} f(n(i,q)).                      \tag{1.3}
\]

Here the minimum of an empty set is `+infinity`; such a state has no path to
the sink.

### Theorem 1.1 (minimum-transversal path network)

For fixed anchor `a`, the minimum number of additional cuts is `f(1)`.
Moreover, every minimum transversal containing `a` is represented by a path
in the acyclic network whose arcs are

\[
 i\stackrel q\longrightarrow n(i,q)
 \quad\text{whenever}\quad f(i)=1+f(n(i,q)).                  \tag{1.4}
\]

Taking the union over those anchors satisfying `1+f(1)=c` represents every
protected-avoiding minimum circular transversal.

#### Proof

At the first unhit interval `J_i`, a new cut must be chosen at some allowed
\(q\in J_i\).  Because right endpoints are ordered, that point hits precisely
the consecutive later intervals whose left endpoints are at most `q`; the
first remaining interval is (1.2).  This proves recurrence (1.3).

Processing any minimum hitting set by its first point in each first-unhit
interval traces arcs satisfying equality in (1.4).  Conversely, the labels
on any source-to-sink path hit every interval and use `f(1)` points.  Every
circular hitting set meets `I_1`, so choosing one of its points as `a`
places it in one of the anchor networks.  \(\square\)

### Consequence

For each fixed anchor the cut-only layer is an integral shortest-path/
min-cost-flow polytope.  The finite union over admissible anchors has an
integral disjunctive extended formulation; it is not being identified with
one bare network polytope.  The chosen cut labels occur in cyclic order, so
consecutive labels also specify every resulting owner block.

## 2. Exact one-cut exchange graph

Let `D` be any minimum transversal on one cycle and let \(g\in D\).  Put

\[
 \mathcal I_g=\{I:I\cap D=\{g\}\}.                            \tag{2.1}
\]

Minimum cardinality implies \(\mathcal I_g\) is nonempty.

### Lemma 2.1 (exact basis-exchange test)

For an allowed unselected gap `q`,

\[
              D-g+q\text{ is a minimum transversal}
 \quad\Longleftrightarrow\quad
              q\in\bigcap_{I\in\mathcal I_g}I.               \tag{2.2}
\]

#### Proof

After deleting `g`, precisely the intervals in \(\mathcal I_g\) become unhit.
One replacement point repairs the transversal exactly when it belongs to
all of them.  The cardinality is unchanged and already minimum. \(\square\)

This gives an exact local move graph on optimal transversals.  It is useful
for search, but connectivity of this exchange graph is not asserted.

## 3. The joint network--seam master

Augment the path network of Theorem 1.1 so a node records the previous cut.
Every selected network arc from cut `g` to the next cut `h` emits the literal
owner block

\[
                   B(g,h)=(T_{g+1},\ldots,T_h).               \tag{3.1}
\]

Let `w_B` say that block `B` is selected, and let

\[
                   z_{B,+}+z_{B,-}=w_B                       \tag{3.2}
\]

choose its orientation.  For every possible pair of option-labelled
oriented blocks emitted by the networks, create a seam atom only when:

1. the tail and head owners are distinct Johnson neighbours;
2. their intersection is the colour of a selected cut;
3. the relaxed necessary residence predicate holds.

Write `y_e` for selected seam atoms and `x_g` for selected cut gaps.  The
cyclic one-copy master contains

\[
\begin{aligned}
 &x,w &&\text{belong to one minimum-transversal path network per old cycle},
                                                                  &&\tag{3.3a}\\
 &\sum_{e:\operatorname{tail}(e)=B^\sigma}y_e=z_{B,\sigma},
 \quad
 \sum_{e:\operatorname{head}(e)=B^\sigma}y_e=z_{B,\sigma},       &&\tag{3.3b}\\
 &\sum_{e:\kappa(e)=\kappa(g)}y_e=x_g
                 &&\text{for every old gap }g,                  &&\tag{3.3c}\\
 &\text{directed subtour cuts on the selected blocks}.          &&\tag{3.3d}
\end{aligned}
\]

For a linear chronology, replace one incoming and one outgoing equality by
explicit source/sink degree equations and replace one colour equality by one
named lower-colour hole (equivalently add one dummy boundary node).  Rank-ten
restoration rows and the exact product residence automaton are then added as
in the endpoint theorem.

### Theorem 3.1 (exact joint master)

Generate the complete dynamic option-labelled segment-pair catalogue over
all path-network arcs; the `56,790` raw atoms for the deterministic cut are
not a catalogue for alternative cuts.  Augment the induced order by the
exact product residence automaton (the relaxed predicate may remain as a
valid presolve filter).  Then the **linear** version of (3.2)--(3.3), with
the explicit source/sink and omitted-colour equations just stated, the
subtour rows, rank-ten restoration rows, automaton acceptance rows, and typed
protected-state pins is necessary and sufficient for an atomic reassembly
of some 3,807-cut minimum transversal into one positive-run-resident owner
chronology with the required immediate palettes.

The proof is the direct two-way reading of a chronology into its old-cycle
blocks and new seams.  The path networks certify that every short old run is
cut with minimum cardinality; the other rows are exactly orientation,
degree, named-colour, connectivity, upper-cover, and residence.

Ranks eleven and higher, clipped source collars, literal `D^3` replay, and
the terminal compiler are not included in this immediate-palette theorem.

## 4. Why this is not plain Hall, 2-SAT, or ordinary matroid intersection

The selector network (3.3a) is totally unimodular by itself.  After a cut
family and orientations are frozen, residual predecessor completion has an
ordinary Hall oracle.

Before that conditioning, each seam simultaneously consumes:

* a tail endpoint slot;
* a head endpoint slot;
* one selected named lower colour;
* and one edge of the contracted graphic structure.

Thus the seam set is constrained by two endpoint partition rows, a colour
partition row, and the graphic matroid, plus orientation and upper-cover
rows.  Even the frozen-cut subsystem is the three-resource matching from
the endpoint no-go theorem.  The natural exact formulation is therefore a
network-flow master with colored matching and graphic separation, not a
2-SAT instance or a standard two-matroid intersection.

For the weaker singleton question—does every selected colour and physical
block have at least one relaxed seam?—one may drop seam capacities and use
the `y_e` only as witnesses:

\[
\begin{aligned}
 &\sum_{e:\kappa(e)=\kappa(g)}y_e\ge x_g,\tag{4.1a}\\
 &\sum_{e:\operatorname{tail}(e)=B^\sigma,\sigma}y_e\ge w_B,
 \quad
 
 \sum_{e:\operatorname{head}(e)=B^\sigma,\sigma}y_e\ge w_B. \tag{4.1b}
\end{aligned}
\]

These are necessary only.  They are the precise joint optimization tested
in Section 6.

## 5. A rigorous distance lower bound

Let `D_0` be the deterministic rightmost-greedy minimum transversal emitted
by the cited audit and let `Z_0` be its 1,289
zero colours in the relaxed necessary atlas.

### Theorem 5.1 (24-relocation lower bound)

Let `D'` be any other protected-avoiding 3,807-cut minimum transversal whose
relaxed atlas has no zero selected colour.  Then

\[
                         |D_0\setminus D'|\ge24.               \tag{5.1}
\]

#### Proof

Put \(q=|D_0\setminus D'|=|D'\setminus D_0|\).  Transform the old partition
to the new one by deleting the `q` old-only cuts and then inserting the `q`
new-only cuts.  Each deletion creates at most one merged block; each
insertion creates at most two split blocks.  Hence at most `3q` final blocks
can fail to be literally identical to old blocks.

At most `q` colours of `Z_0` disappear from the selected cut palette.  If a
remaining colour \(K\in Z_0\) acquires a relaxed seam under `D'`, at least one
endpoint block of that seam is a new literal block.  Otherwise the same two
oriented old blocks would already have supplied that seam under `D_0`,
contradicting \(K\in Z_0\).

A physical rank-nine block has two endpoint owners.  Across its two
orientations, every seam colour incident to it is a rank-eight facet of one
of those owners.  Each owner has nine facets, so one new block can account
for at most 18 colours of `Z_0`.  Therefore

\[
                  1289\le q+18(3q)=55q.                       \tag{5.2}
\]

Thus \(q\ge\lceil1289/55\rceil=24\). \(\square\)

### Corollary 5.2 (36-extra-cut lower bound)

If every old canonical emitted cut is retained and only `t` additional cuts are
made, eliminating all 1,289 old zero colours by ordinary atomic seams
requires

\[
                              t\ge36.                          \tag{5.3}
\]

Indeed, `t` insertions create at most `2t` nonold blocks, each incident to
at most 18 old zero colours, so \(1289\le36t\).

Both bounds hold for the relaxed necessary atlas and hence also for every
exact residence automaton.  They do not apply to a non-atomic socket gadget
which supplies a colour internally.

## 6. Exact minimum-cut exchange experiment

The diagnostic source

```text
scratch/search_k17_h2_min_cut_residence_endpoint_20260801.cpp
SHA256 9a0807139ef9cfaaa59171435d4ae87696e65b910382a973ca9b44a1ab3751f9
```

uses Lemma 2.1 for every move, so every visited cut family is an exact
protected-avoiding 3,807-cut transversal.  It rebuilds all literal blocks
and evaluates the same relaxed necessary residence predicate as the
authenticated no-go audit.  The finite search is heuristic; it is not an
exhaustive theorem.

The initial score is

```text
zero colours = 1289
dead outgoing blocks = 368
dead incoming blocks = 368
relaxed oriented seam atoms = 13174
```

Eight independent 1,000-move walks already reached 1,211 zero colours.
Eight independent 20,000-move walks reached:

```text
best zero colours = 984
dead outgoing blocks = 260
dead incoming blocks = 260
relaxed oriented seam atoms = 17474
changed cuts relative to D_0 = 2037
```

The retained best transcript is

```text
scratch/k17_h2_min_cut_residence_endpoint_search_seed9303.out
SHA256 63fdc32ec615f683e2f230ef022ae00f676890e461b728eb31c551da4cbe9940
```

and ends in

```text
PASS_K17_H2_MIN_CUT_RESIDENCE_ENDPOINT_SEARCH
```

This proves experimentally that the 1,289 count is not invariant under
minimum-transversal exchange.  It also gives no evidence that elementary
one-cut exchanges can reach zero: the best walk still has 984 singleton
colour obstructions after changing more than half the cuts.

## 7. Current proof-safe conclusion

The raw 28,395-seam theorem remains the correct Boolean outer reduction for
the deterministic rightmost-greedy cut, but its endpoint census is
superseded for feasibility purposes by the 13,174-seam necessary-residence
no-go.

Alternative minimum transversals can improve the no-go while retaining the
sharp cut count 3,807; the authenticated exchange walk reduces the singleton
zero count from 1,289 to 984.  Thus the lex count is not an invariant.  The
cut family has the exact integral disjunctive path-network formulation of
Section 1, and one-cut adjacency has the exact intersection test (2.2).
Nevertheless, the joint endpoint problem remains a network-flow/coloured-
matching/graphic/automaton master, not plain Hall.

The newer lex-plus-extra-cut union atlas closes the former singleton gate at
support two.  It has 20,477 viable split options and 3,194,008 cut-pair
supports.  Unary columns leave 110 old zero colours unsupported; pair
columns support all 110, so all 2,025 old singleton colour/tail/head demands
have at least one column.  This is only a prospective union-of-menus result.
Different demands may require incompatible split choices, and a unary
support may reference a base block destroyed by another selected split.
The selected cut set has since been rebuilt literally.  Its `7,612` pieces
and colours have no relaxed lower/physical-endpoint zero and have perfect
unoriented `TH`, `TC`, and `CH` projections.  No common orientation or three-resource
matching exists on that bank: exactly `187` pieces have incoming support
only in one orientation and outgoing support only in the opposite one, so
the q1 CNF is UNSAT by unit propagation.  Independently, the relaxed atlas
has exactly `78` rank-ten zero-provider rows.  Thus that fixed dense
refinement fails both shared orientation and upper completion.

The current literal cut-choice incumbent preserves the zero q1 rows and all
three perfect unoriented projections while reducing these selected-bank
counts to `94` and `28`.  This is a live descent, not closure or a final
search verdict.

A subsequent independently replayed bank reaches `0` common-orientation and
`0` rank-ten singleton rows, still with all three physical q1 projections
perfect (bank/audit SHA prefixes `5b4fe2d1`/`199ab886`).  Its exact
three-resource q1 formula is UNSAT: a verified 14-clause/five-lemma core
reduces to two required colour edges competing for one physical socket.  This
rejects that fixed bank only and makes cut CEGAR around the bow tie the first
unresolved row; no chronology or word follows.

The first global one-cut CEGAR move destroys that core without reintroducing
any singleton zero, but the resulting bank is again q1-UNSAT with a verified
`15`-clause/`7`-lemma core.  Hence small-core iteration is validated, not
proved convergent.

The exact next theorem is therefore **joint integral cut/seam selection**:
choose one compatible cut/split bank, its literal blocks and orientations,
endpoint-disjoint seams and deleted-colour services, then impose owner
degrees and one-path topology, solve the simultaneous tail/head/colour
matching after altering the fixed bank's bow-tie core, and impose all rank-ten and ordered
deeper-upper witnesses, the
exact residence product, and finally the common-cap compiler after physical
replay.  A negative theorem must give a Hall/DM/Benders cut valid across cut
choices.  Singleton nonemptiness is closed only in the lex-rooted support-two
union projection and is not a sufficiency certificate for any selected bank.
