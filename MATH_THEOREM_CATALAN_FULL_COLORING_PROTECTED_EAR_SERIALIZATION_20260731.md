# Full-colouring cover-down: protected gain-one ears, exact prefix circuits, and Kempe locks

Date: 2026-07-31  
Status: exact conditional zero-defect cover-down theorem and sharp finite
exchange obstructions.  No all-`n` Boolean ear-supply theorem is claimed.

## 0. Outcome and exact boundary

Fix an arbitrary synchronized common basis `Q` and its four-uniform
capacity-slot hypergraph `H_Q`.  The Delcourt--Postle theorem now supplies a
full conflict-free colouring of `E(H_Q)`, and one colour gives a
`P-o(P)` capped physical forest.  The complete colouring is useful, but it
does not by itself imply exact cover-down.

This note proves the exact positive statement available from it.

1. Against one donor colour, the largest possible increase of a partial
   target class is the Hall deficiency

   \[
      \delta(C\mid M,Z)=
       \max_{A\subseteq C^Z}\bigl(|A|-|N_M(A)|\bigr).             \tag{0.1}
   \]

   Here `Z` is the protected old bank and `C^Z` contains the donor atoms
   disjoint from it.  Every inclusion-minimal positive set is a genuine
   **gain-one ear**.
2. For a family of possibly multicolour ears, matching and slot capacities
   serialize under explicit privacy.  Physical-forest serialization has an
   exact circuit-deadline criterion.  If `a(K)` and `r(K)` are the packets
   adding and removing edges of a physical circuit `K`, an order with packet
   times `tau_i` is valid exactly when

   \[
        \min_{j\in r(K)}\tau_j
          \le \max_{i\in a(K)}\tau_i                              \tag{0.2}
   \]

   for every circuit.  Every packet order works exactly when

   \[
                         a(K)\cap r(K)\ne\varnothing               \tag{0.3}
   \]

   for every circuit.  This is the **self-breaking circuit row**.
3. `P-|M|` private gain-one ears satisfying (0.2), avoiding the protected
   seams, give a literal size-`P` capped physical forest.  If all selected
   compiler incidences lie in one trace-guarded bank, the final matching is
   also maximal-common-cap exact.  Thus this face is a rigorous zero-defect
   protected cover-down.
4. Two finite obstructions delimit the claim.  A three-atom `K_(1,2)` shows
   that all single-donor deficiencies may vanish while one correlated
   two-donor packet gains one.  More sharply, a literal six-atom `n=4`
   slot fixture has a matching of size three, whereas every colouring
   reachable from its three size-two classes by arbitrary pairwise Kempe
   flips still has every class of size two.  Exhaustive replay finds no such
   coloured-graph Kempe lock on at most five atoms.

Consequently the full Delcourt--Postle colouring is a distributed exchange
reservoir, not an automatic exact absorber.  The missing Boolean theorem is
the supply of a protected self-breaking ear family (or a larger correlated
packet family) inside `H_Q`, together with one common trace-guarded compiler
face.  This result is separate from the residual exact-cover search.

## 1. The protected two-colour deficiency formula

Let `H` be any hypergraph and let `M` and `C` be disjoint matchings in `H`.  Think of
`M` as the current target colour and `C` as one donor colour.  Two atoms
conflict when they meet in a hypergraph resource.  Fix a protected bank
`Z subseteq M` and put

\[
 C^Z=\{e\in C:e\text{ conflicts with no }z\in Z\}.                \tag{1.1}
\]

For `A subseteq C^Z`, define its complete old conflict neighbourhood

\[
 N_M(A)=\{m\in M\setminus Z:
                 m\text{ conflicts with some }a\in A\}.          \tag{1.2}
\]

Because `C` is a matching,

\[
                  M[A]=(M\setminus N_M(A))\sqcup A                \tag{1.3}
\]

is a matching retaining every atom of `Z`.

### Theorem 1.1 (exact one-donor Hall deficiency)

The maximum order of a matching contained in `M union C` and containing
`Z` is

\[
\boxed{
  |M|+\delta(C\mid M,Z),\qquad
  \delta(C\mid M,Z)=
     \max_{A\subseteq C^Z}(|A|-|N_M(A)|).}                         \tag{1.4}
\]

Equivalently, if `nu(B_(M,C^Z))` is the maximum matching order in the
bipartite conflict graph with shores `M setminus Z` and `C^Z`, then

\[
 \boxed{
       \delta(C\mid M,Z)=|C^Z|-\nu(B_(M,C^Z)).}                   \tag{1.4a}
\]

In particular, one donor colour has a gain-one cover-down ear if and only
if its conflict graph against `M` violates Hall on the donor shore.

#### Proof

Equation (1.3) has order

\[
                     |M|+|A|-|N_M(A)|,                            \tag{1.5}
\]

so the right side of (1.4) is attainable.  Conversely, let `X` be any
matching in `M union C` containing `Z`, and put `A=X cap C`.  Every old
atom compatible with all of `A` may be added to `X` without losing
feasibility.  Therefore an optimal `X` contains all of
`M setminus N_M(A)`, and its order is at most (1.5).  Maximizing over `A`
proves (1.4).  The deficient form of Hall's theorem on the donor shore says
that this maximum deficiency is the donor-shore order minus the maximum
bipartite matching order, proving (1.4a).  `square`

### Lemma 1.2 (minimal positive sets are connected unit ears)

If `A subseteq C^Z` is inclusion-minimal with

\[
                         |A|>|N_M(A)|,                             \tag{1.6}
\]

then

\[
                         |A|=|N_M(A)|+1,                           \tag{1.7}
\]

and the bipartite conflict graph induced by `A union N_M(A)` is connected.

#### Proof

For every `a in A`, minimality gives

\[
 |A|-1\le |N_M(A\setminus\{a\})|\le |N_M(A)|.
\]

Together with (1.6), this proves (1.7).  If the induced conflict graph had
more than one component, its donor and old orders would sum to the two
sides of (1.6).  Some component would have positive donor surplus, giving a
proper positive subset of `A`, contrary to minimality.  `square`

This is a genuine gain-one statement; it is not an equal-size
perfect-matching circuit.  A minimal ear may branch in the conflict graph,
because one four-uniform atom can meet up to four old atoms.  It need not be
an alternating path.

If the whole induced component is a connected component of the two-colour
conflict graph on `M union C`, swapping its two shores is an ordinary Kempe
move and changes the target-class order by the component imbalance.  A
general Hall ear from Lemma 1.2 may be only part of such a component; it is
then a consumptive extraction move rather than a full-colouring Kempe move.

## 2. Private multicolour ears and matching serialization

Let the current target matching be `M`, with protected bank `Z`.  A declared
packet `i` consists of a matching `A_i` of new atoms, possibly drawn from
several colour classes, and its complete old neighbourhood

\[
                         R_i=N_M(A_i).                              \tag{2.1}
\]

Call it a **protected unit ear** when

\[
             R_i\cap Z=\varnothing,
             \qquad |A_i|=|R_i|+1.                                \tag{2.2}
\]

The packet family is resource-private when

1. `A=union_i A_i` is a matching of the host hypergraph; and
2. the old sets `R_i` are pairwise disjoint.

The second condition also prevents an atom of `A_i` from conflicting with
an old atom in `R_j`, `j != i`: such an atom would belong to both complete
neighbourhoods.

For `S subseteq I`, put

\[
 M_S=\left(M\setminus\bigcup_{i\in S}R_i\right)
          \sqcup\bigcup_{i\in S}A_i.                              \tag{2.3}
\]

### Lemma 2.1 (matching and capacity prefixes)

For every `S subseteq I`, `M_S` is a hypergraph matching, contains `Z`, and
has order

\[
                   |M_S|=|M|+\sum_{i\in S}(|A_i|-|R_i|).          \tag{2.4}
\]

In `H_Q`, every `M_S` therefore obeys ordinary physical degree at most two
and seam-anchor degree at most one.

#### Proof

Atoms within the added bank are disjoint by privacy.  An added atom from
`A_i` conflicts with an old atom only in `R_i`, all of which are removed
when `i in S`.  The old matching remains a matching, and (2.2) retains
`Z`.  This proves feasibility and (2.4).  The last assertion is exactly the
capacity-slot equivalence for `H_Q`.  `square`

The full colouring supplies internal matching for every monochromatic
subset automatically.  It does **not** supply cross-colour privacy for a
multicolour `A_i`; that is an additional audited row.

### Theorem 2.2 (binary self-breaking clutter lemma)

The preceding matching argument is one instance of a general exact
serialization law.  Let

\[
 X_S=X_0\sqcup\bigsqcup_{i\notin S}R_i
             \sqcup\bigsqcup_{i\in S}A_i                            \tag{2.5}
\]

be a binary packet system with pairwise-disjoint fixed, off, and on banks,
and let `cal B` be any clutter of forbidden subsets of their union.  For a
packet-supported blocker `B in cal B`, put

\[
 a(B)=\{i:B\cap A_i\ne\varnothing\},\qquad
 r(B)=\{i:B\cap R_i\ne\varnothing\}.                              \tag{2.6}
\]

Here *packet-supported* only excludes a formal bad event using an exterior
atom which occurs in neither phase of the declared binary system; it does
not mean that the blocker already appears in some state.

Then every subset state `X_S` avoids every blocker if and only if

\[
 \boxed{a(B)\cap r(B)\ne\varnothing
                 \quad\text{for every packet-supported }B.}       \tag{2.7}
\]

For one packet order with distinct times `tau_i`, every prefix is safe if
and only if

\[
 \boxed{
  \min_{j\in r(B)}\tau_j
       \le\max_{i\in a(B)}\tau_i
       \quad\text{for every packet-supported }B.}                  \tag{2.8}
\]

#### Proof

A blocker `B` is contained in `X_S` exactly when

\[
                         a(B)\subseteq S,qquad
                         r(B)\cap S=\varnothing.                   \tag{2.9}
\]

Some subset `S` satisfies (2.9) exactly when the two index sets in (2.6)
are disjoint; choosing `S=a(B)` proves the reverse direction.  Along an
order, (2.9) holds at some prefix exactly when

\[
       \max_{i\in a(B)}\tau_i
          <\min_{j\in r(B)}\tau_j,
\]

which is the strict reverse of (2.8).  `square`

This one lemma applies simultaneously to the union of the following
forbidden clutters.

* **Host collisions:** the two-atom sets sharing one lower, upper, or slot
  resource.  Resource privacy makes every packet-supported such pair
  self-breaking in its own packet.
* **Physical topology:** the occurrence-labelled edge sets of projected
  graphic circuits, including parallel two-circuits.
* **Delcourt--Postle transparency:** the monochromatic short-cycle
  configurations which must remain forbidden if donor colours are retained.
* **Downstream common cap:** the pulled-back inclusion-minimal empty-position,
  protected-row-bit, and selected-lower-bit blockers after unary closure.

Thus a single binary self-breaking certificate can protect matching,
forest, short-cycle, and compiler rows at every prefix.  Requiring
`R_i cap Z` empty additionally freezes the named seams or anchors.  The
trace-guarded face used below is a simpler sufficient way to make the last
clutter empty on every matching-compatible selection; it is not the only
possible application of (2.7).

## 3. Exact physical prefix criterion

Let `F` be the fixed physical forest consisting of the retained central
scaffold, all inherited seams, and the projection of `M`.  Write
`partial A_i` and `partial R_i` for the projected physical edges of the two
packet shores.  Projection is simple on a host matching: the intersection
and union colours recover the physical owner pair.

For `S subseteq I`, the physical prefix is

\[
              F_S=F-\bigcup_{i\in S}\partial R_i
                       +\bigcup_{i\in S}\partial A_i.             \tag{3.1}
\]

Consider every graphic circuit `K` in

\[
                         F\cup\partial A,
 \qquad \partial A=\bigcup_i\partial A_i.                         \tag{3.2}
\]

Parallel edges count as a two-circuit.  Since `F` is a forest, every such
`K` contains an added edge.  Define

\[
\begin{aligned}
 a(K)&=\{i:K\cap\partial A_i\ne\varnothing\},\\
 r(K)&=\{i:K\cap\partial R_i\ne\varnothing\}.                   \tag{3.3}
\end{aligned}
\]

### Theorem 3.1 (circuit-deadline serialization)

Let `tau_i in {1,...,|I|}` be distinct packet times and let `S_t` be the
first `t` packets.  Every physical prefix `F_(S_t)` is a forest if and only
if

\[
 \boxed{
    \min_{j\in r(K)}\tau_j
        \le \max_{i\in a(K)}\tau_i
       \quad\text{for every circuit }K\subseteq F\cup\partial A.} \tag{3.4}
\]

The minimum of an empty set is `+infinity`.  Hence (3.4) also detects a
circuit surviving in the final state.

#### Proof

A circuit `K` is present at prefix `t` exactly when every packet adding one
of its new edges has fired, and no packet removing one of its old edges has
fired.  Equivalently,

\[
       \max_{i\in a(K)}\tau_i\le t
          <\min_{j\in r(K)}\tau_j.                                \tag{3.5}
\]

Some integer `t` satisfies (3.5) exactly when the strict reverse of (3.4)
holds.  Excluding this for every circuit is equivalent to every prefix
being acyclic.  `square`

### Corollary 3.2 (arbitrary-order self-breaking criterion)

Every subset state `F_S`, and hence every packet order, is a forest if and
only if

\[
 \boxed{
                a(K)\cap r(K)\ne\varnothing
                \quad\text{for every circuit }K.}                 \tag{3.6}
\]

#### Proof

If packet `i` belongs to both sets in (3.3), then whenever all additions of
`K` are active, packet `i` has also deleted an old edge of `K`.  Thus `K`
never occurs.  Conversely, if the two sets are disjoint, take
`S=a(K)`.  All added edges of `K` are present and none of its old removal
edges is gone, so `F_S` contains `K`.  `square`

Condition (3.6) is stronger than final acyclicity.  Final acyclicity asks
only that `r(K)` be nonempty; serializing arbitrary ear choices requires a
packet which both participates in and breaks every possible circuit.  For a
chosen order, (3.4) is the weaker exact disjunctive-deadline row.  It is not
in general reducible to pairwise packet conflicts.

The theorem works at the declared packet granularity.  If the atoms inside
one packet must themselves be exposed sequentially, refine that packet into
micro-packets and reapply (3.4); an atomic packet certificate alone does not
assert internal serializability.

## 4. Zero-defect protected cover-down on the serializable face

Let `P` be the order of each outer resource bank of `H_Q`.

### Theorem 4.1 (protected gain-one ear cover-down)

Assume:

1. `M` is a matching of `H_Q`, and the fixed scaffold plus its physical
   projection is a forest;
2. `Z subseteq M` contains every old atom whose occurrence is protected;
3. there are exactly `h=P-|M|` resource-private protected unit ears;
4. their packet times satisfy (3.4); and
5. the final selected target--cell incidences belong to one trace-guarded
   compiler bank in the sense of
   `MATH_THEOREM_GUARDED_CONVEX_LAMINAR_COMMON_CAP_COMPILER_20260731.md`.

Then toggling the ears in the certified order has the following literal
properties.

* Every prefix is a host matching and a capped physical forest.
* Every protected atom and every inherited seam remains present.
* The final matching has order `P`, so it uses every lower and every upper
  outer resource exactly once.
* The final maximal common cap is nonempty and realizes every protected row
  and every selected lower cell.  Thus the cover-down has zero marginal,
  topological, anchor, and common-cap defect.

#### Proof

Lemma 2.1 gives a matching at every prefix and increases its order by one
per ear.  Theorem 3.1 gives the physical-forest row at every prefix.  Slot
equivalence gives both physical degree caps, while `R_i cap Z` empty keeps
the protected bank.  The final order is

\[
                           |M|+h=P.                                \tag{4.1}
\]

A matching of order `P` meets all `P` lower resources and all `P` upper
resources, so both palettes are exact.  Finally, every saturated matching
inside a trace-guarded bank is common-cap exact by the complete trace-guard
lemma.  `square`

The immediate Boolean cap `V=D union x union y` is already encoded by each
slot atom and is automatic after outer saturation.  Hypothesis 5 concerns
the **downstream word-compiler maximal common cap** (positions, protected
rows, and selected lower trace rows), which is a distinct object.  No extra
row is being imposed on the Boolean diamond itself.

The trace-guard row is a sufficient face, not something produced by the
Delcourt--Postle colouring.  The two-position `K_(2,2)` example in the
guarded-common-cap theorem has perfect marginal matchings and a permanent
owner bit but no integral common-cap compiler.  Therefore marginal
colouring plus physical acyclicity cannot replace hypothesis 5.

### Full-colouring transparency

Theorem 4.1 is consumptive: it extracts one exact target matching and need
not leave all donor colours conflict-free.  If the whole colouring must be
preserved as a future reservoir, add two independent requirements.

1. Each binary packet is a union of connected components of the current
   two-colour conflict graph; swapping those components preserves proper
   resource colouring.
2. On both affected colours, every prefix avoids the Delcourt--Postle
   forbidden configuration hypergraph.  For the short-cycle conflict
   system this means that neither mixed old/new shore creates a projected
   cycle of length at most the declared cutoff.

The first row is ordinary Kempe legality.  The second is a genuine
**transparent-switch** row and is not implied by proper colouring.  Target
physical-forest preservation in (3.4) does not certify the donor colour.

### Theorem 4.2 (exact two-colour terminal-phase criterion)

There is a useful exact limit on what two close colour classes can do.
Let `F_0,F_1` be two host matchings and form their complete four-resource
exchange incidence graph `Xi(F_0,F_1)`: atoms are vertices, a resource used
in both phases joins its two atoms, and a resource used in only one phase is
a terminal half-edge at that atom.  A **component-phase hybrid** chooses,
independently for every connected component of `Xi`, either all phase-zero
atoms or all phase-one atoms in that component.

Such a hybrid saturates every lower and every upper outer resource if and
only if both conditions hold.

1. No outer resource is absent from both `F_0` and `F_1`.
2. No exchange component contains a phase-zero outer terminal and a
   phase-one outer terminal.

Every component with terminals on exactly one phase is forced to that
phase; a component with no outer terminal is free.

#### Proof

An outer resource used in both matchings is an ordinary exchange edge, so
either phase of its component covers it exactly once.  A resource used in
only phase `i` is a terminal and is covered exactly when its component is
put in phase `i`.  An absent resource cannot be supplied, while opposite
terminal phases in one component impose contradictory phase choices.
These are the only cases.  `square`

The few-terminal theorem proves that two Delcourt--Postle classes may be
chosen with only `o(P)` resource terminals, but it does not force either
condition here.  Common holes are absent from the exchange graph entirely,
and all opposite-phase terminals may lie in one component.  Therefore two
close `P-o(P)` classes still do not provide exact cover-down; third-colour
ears or a theorem splitting the terminal core are necessary.

## 5. The correlated `K_(1,2)` gate

The one-donor formula cannot be applied to all colours independently and
then maximized.  At `n=4`, take the literal side diamonds on `[8]`

\[
\begin{array}{c|c|c}
 &D&V\\ \hline
 r&0123&012345\\
 a&0123&012367\\
 b&2345&012345.
\end{array}                                                     \tag{5.1}
\]

Use slot index one on their two intermediate rank-five sets.  The three
atoms have conflict graph

\[
                              a-r-b,                               \tag{5.2}
\]

because `a` shares only the lower resource of `r`, `b` shares only its
upper resource, and `a,b` are resource-disjoint.  Put them in three
singleton colours with target `M={r}`.  Each donor separately has

\[
                         \delta(C_j\mid M,\varnothing)=0,          \tag{5.3}
\]

but the correlated two-donor packet

\[
                         \{r\}\longrightarrow\{a,b\}              \tag{5.4}
\]

has gain one and its two physical edges are disjoint.

This is the smallest static obstruction: a gain requires at least one old
and two new atoms, and putting both new atoms in one donor would itself give
a positive one-donor Hall set.  It does **not** obstruct neutral
reconfiguration: swap `r` with `a`, after which `b` is free.  Its exact
lesson is that a proof based only on positive initial one-donor deficiencies
misses serializable neutral ears.

The literal replay is

```text
scratch/audit_catalan_three_colour_kempe_unit_ear_obstruction_20260731.py
scratch/catalan_three_colour_kempe_unit_ear_obstruction_20260731.audit.json
```

and is scoped to fixed `Q` for which the two displayed lower resources
survive the puncture.

## 6. A true six-atom Kempe lock

There is also an obstruction to **arbitrary sequences** of pairwise Kempe
flips.  Let the conflict graph have high vertices `h0,h2,h4` spanning a
triangle and low vertices `l1,l3,l5`, where `l1` is adjacent to `h2,h4`,
`l3` to `h0,h4`, and `l5` to `h0,h2`.  There are no other edges.  Colour

\[
              \{h0,l1\},\qquad\{h2,l3\},\qquad\{h4,l5\}.          \tag{6.1}
\]

Each pair of colours induces one connected path `P4`, with two vertices on
each shore.  Therefore its only Kempe flip exchanges the two colour names
on that whole path.  After such a flip the same statement remains true.
The Kempe closure consists of the six global permutations of (6.1), and
every colour always has order two.  Nevertheless

\[
                          \{l1,l3,l5\}                              \tag{6.2}
\]

is an independent set of order three.

### Proposition 6.1 (pairwise Kempe cover-down is incomplete)

There is a properly three-coloured four-uniform capacity-slot conflict
system with a matching larger than every colour class, but no sequence of
pairwise Kempe component flips increases any colour class.

#### Proof

The preceding `P4` argument proves Kempe closure and the order-two
invariant.  The low vertices prove that the host matching number is at
least three.  A literal typed four-resource realization is obtained by
using three shared resources `a,b,c`: `h0` uses `b,c`, `h2` uses `a,c`,
`h4` uses `a,b`, while `l1,l3,l5` use `a,b,c`, respectively; private
resources pad every atom to order four.  The frozen audit further realizes
these six atoms as actual `n=4` Boolean side diamonds.  `square`

In the Boolean realization, the common rank-five set `01234` uses slot two
on `h0,h2,l5` and slot one on `h4`; hence the fixture requires that owner to
be nonanchor.  It also requires four displayed lower resources to survive
`Q`.  It is not claimed to embed for every fixed common basis, nor to remain
closed after adding the exterior atoms of the full `H_Q` colouring.

The independent exhaustive audit covers every properly coloured graph on
at most five vertices, every number of nonempty colours, every ordered
colour-size composition, and every compatible cross-edge set.  Among
`4,594` cases, `4,150` have a larger independent set than target colour
zero, but none is Kempe-locked.  Thus six vertices are minimal at the
abstract coloured-conflict-graph level.

```text
scratch/audit_catalan_six_atom_kempe_coverdown_lock_20260731.py
scratch/catalan_six_atom_kempe_coverdown_lock_20260731.audit.json
```

## 7. Exact all-`n` theorem still required

The arbitrary-`Q` Delcourt--Postle colouring closes the asymptotic
`P-o(P)` physical row.  To turn the full colouring into coefficient one,
one still needs one of the following Boolean statements.

1. **Protected self-breaking ear supply.**  After selecting a near-forest
   colour, the leave admits `P-|M|` resource-private unit ears satisfying
   (3.4), with all choices inside one trace-guarded common-cap bank.
2. **Correlated packet supply.**  A bounded-width multicolour packet system
   routes the `K_(1,2)` and six-atom Kempe locks, and its packet-level
   physical circuits satisfy the same deadline inequalities.

Neither follows from the number or average size of colour classes.  A
single colour gives no exchange correlation, and pairwise Kempe components
can be balanced forever.  Conversely, Theorem 4.1 shows that once the
protected ear supply and common guard face are present, no further
topological or marginal cover-down theorem is needed.

## 8. Audit record

The two local fixtures were replayed deterministically by the scripts in
Sections 5--6.  They check literal Boolean containment, capacity-slot
resources, conflict graphs, physical forests, Kempe closure, matching
number, and the stated finite minimality census.  No SAT solver, H100 job,
handoff edit, or research-index edit was used.
