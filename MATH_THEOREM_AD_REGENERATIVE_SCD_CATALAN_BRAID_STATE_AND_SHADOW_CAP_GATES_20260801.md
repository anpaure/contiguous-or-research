# Regenerative SCD Catalan braid state and the exact shadow/common-cap gates

Date: 2026-08-01  
Lane: AD, same-parity `k-2 -> k` renewal  
Status: exact owner-state equivalence; independently replayed finite
`m=4,...,8` forests; exact conditional braid/source renewal theorem; and a
sharp growing-interface obstruction.  No all-`m` detachment selector,
protected selector, component Hamilton braid, deep-shadow renewal, common
cap, or `nu(k)<=B(k)+1` theorem is claimed.

## 0. Verdict

Put

\[
 k=2m-1,\qquad
 \mathcal L_m={ [2m-1]\choose m-1},\quad
 \mathcal O_m={ [2m-1]\choose m},\quad
 \mathcal U_m={ [2m-1]\choose m+1},                 \tag{0.1}
\]

and

\[
 W_m=|\mathcal L_m|=|\mathcal O_m|,\qquad
 U_m=|\mathcal U_m|,\qquad
 C_m=W_m-U_m=\operatorname {Cat}_m.                 \tag{0.2}
\]

The finite flexible-SCD certificates have a smaller exact description than
their packet grammar suggests.  Their complete owner layer is just

\[
                         \boxed{(M_0,\pi)},           \tag{0.3}
\]

where `M_0` is a perfect root--owner incidence matching and `pi` is an
acyclic partial injection on the roots.  The upper palette, used lower
palette, Catalan leave, component sources, component terminals, physical
edges, and component pairing are all derived.  In particular, the omitted
lower colours are already the terminal ports; there is no additional
leave-to-terminal Hall problem.

For `m=4,...,8`, independently replayed SAT witnesses give exact spanning
forests with `C_m` directed path components.  This proves a finite central
owner row, not a literal recurrence.  The child forest is selected afresh
from a canonical SCD of the whole old-coordinate ground; it is not obtained
by transporting the previous selected forest or its source chronology.

The correct regenerative architecture has three successive layers.

1. Select a fresh protected pair `(M_0,pi)` and then join its `C_m`
   components by `C_m-1` free-port arcs into one directed owner path.
2. Realize that path as the depth-`h` row of one source word, with the
   refreshed pivot packet as a prefix and one terminal nonowner cell.
3. On that same source, select every deep target occurrence and pass the
   maximal common-cap equations.

Layer 1 is finite-positive only without the protected packet.  Layers 2--3
remain open.  The exported interface has a bounded **number of structured
fields**, but it is not a dimension-independent finite state: the current
refresh halo has `O(h)` letters and `Theta(h^2)` derived interval addresses,
and universal crossing coverage requires its compressed prefix/suffix OR
decks (with complete ordered signatures needed for addresswise reuse).

## 1. Exact central normal form

Let

\[
 M_0:\mathcal L_m\longrightarrow\mathcal O_m          \tag{1.1}
\]

be a bijection with `x subset M_0(x)` for every root `x`.  Let

\[
 \pi:\mathcal L_m\rightharpoonup\mathcal L_m          \tag{1.2}
\]

be a partial injection.  For `x in dom(pi)`, define the physical edge and
its upper colour by

\[
 e_x=\{M_0(x),M_0(\pi x)\},\qquad
 u_x=M_0(x)\cup M_0(\pi x).                           \tag{1.3}
\]

### Theorem 1.1 (root-permutation equivalence)

Call an oriented physical forest **`M_0`-coherent** when every edge of
lower colour `x` is directed from `M_0(x)` to its other owner and the
induced root arcs have indegree and outdegree at most one.  This directed
condition is stronger than physical maximum degree two.

The following are equivalent.

1. The physical edges form a spanning upper-exact `M_0`-coherent directed
   Catalan linear forest, oriented from `M_0(x)` to `M_0(pi x)`.
2. The partial injection `pi` satisfies

   \[
   M_0(x)\cap M_0(\pi x)=x\quad(x\in\operatorname{dom}\pi),       \tag{1.4}
   \]

   its directed graph has no cycle, and

   \[
   x\longmapsto u_x
   \quad\hbox{bijects }\operatorname{dom}\pi
          \hbox{ onto }\mathcal U_m.                 \tag{1.5}
   \]

Under these conditions:

\[
 |\operatorname{dom}\pi|=U_m,\qquad
 \#\operatorname{components}=W_m-U_m=C_m,            \tag{1.6}
\]

the exact used lower-`q1` palette is `dom(pi)`, and

\[
 T_m:=\mathcal L_m\setminus\operatorname{dom}\pi,qquad
 S_m:=\mathcal L_m\setminus\operatorname{im}\pi      \tag{1.7}
\]

are respectively the terminal-root and source-root banks, one of each per
component.

#### Proof

Equation (1.4) says that `e_x` is a Johnson edge whose lower colour is
exactly `x`; (1.5) says that all immediate-upper colours occur exactly once.
Because `pi` is a partial injection, every root has outdegree and indegree
at most one.  Acyclicity therefore makes its directed graph a disjoint union
of paths.  It has `W_m` vertices and `U_m` edges, giving (1.6).  A root is a
terminal exactly when it has no outgoing arc, and is a source exactly when
it has no incoming arc, proving (1.7).

Conversely, contract every `M_0` incidence edge of an `M_0`-coherent rooted
upper-exact Catalan forest.  Each physical edge has a unique lower root `x`
and a unique head root `y=M_0^{-1}(V)`.  Coherence makes `x -> y` a partial
injection, physical acyclicity makes it acyclic, and palette exactness gives
(1.4)--(1.5).  This reconstructs `pi`.  \(\square\)

The coherence qualifier is load-bearing.  A physical path `A-B-C` can be
root-oriented as `A->B<-C`; it has physical maximum degree two but root
indegree two and therefore is not represented by a partial injection.

### Corollary 1.2 (automatic leave--port alignment)

Both banks in (1.7) have order `C_m`.  The total physical degree deficit is
`2C_m`.  Every omitted lower colour is the terminal root of exactly one
component, and every component has exactly one available incoming source
root.  Thus terminal leave, endpoint slots, and component endpoint pairing
are derived from `(M_0,pi)` and are not independent matching rows.

This is the irreducible owner-layer state.  Cached source/terminal labels,
component ids, endpoint mates, and sector types are useful algorithmically,
but contain no additional mathematical choice.

## 2. The finite flexible-SCD theorem

Let

\[
 D_m={2m-3\choose m-2},\qquad
 s_m={2m-3\choose m}+{2m-3\choose m+1}=2D_m-C_m.      \tag{2.1}
\]

The isolated SCD seed has `2D_m` components.  Every selected one-to-two
detachment replaces one seed edge by two edges, so it adds one net edge and,
on an acyclic support, reduces the component count by one.  Selecting the
`s_m` missing-sector services therefore leaves exactly

\[
                         2D_m-s_m=C_m                \tag{2.2}
\]

components.

Indeed, with `g=2m-3`, two applications of Pascal and
`binom(g,m-1)=binom(g,m-2)=D_m` give

\[
\begin{aligned}
 W_m&={g\choose m}+3D_m,\\
 U_m&={g\choose m+1}+2{g\choose m}+D_m,
\end{aligned}
\]

and hence `C_m=W_m-U_m=2D_m-s_m`.

### Theorem 2.1 (authenticated finite owner forests)

For every `m=4,...,8`, there is a canonical SCD root matching `M_0` and a
partial injection `pi` satisfying Theorem 1.1.  The exact replay is:

\[
\begin{array}{c|r|r|r|r|rrrrr}
m&W_m&U_m&C_m&s_m&aC&aD_{\rm long}&aD_{\rm short}&zA&zR\\ \hline
4&35&21&14&6&0&4&1&0&1\\
5&126&84&42&28&0&14&7&0&7\\
6&462&330&132&120&23&37&24&19&17\\
7&1716&1287&429&495&108&132&90&45&120\\
8&6435&5005&1430&2002&473&498&316&137&578
\end{array}                                                       \tag{2.3}
\]

Every row has maximum rooted indegree/outdegree one, maximum physical degree
two, exact upper and used-lower palettes of size `U_m`, no directed or
undirected cycle, and exactly `C_m` components.

#### Audit scope

The SAT model enforces the target/provider/head/tail phase selection.  Its
saved satisfying assignments are not by themselves forest certificates:
acyclicity is absent from the CNF, and exhaustive `m=4` replay contains
seven encoded cyclic selections.  Independent reconstruction of the five
saved assignments verifies Johnson legality, both palettes, all capacities,
acyclicity, and component counts.  Therefore (2.3) is an exact finite
existence theorem, while automatic acyclicity of the option grammar is
false.

The smaller restricted catalogue is solved only for `m=4,5`; its larger
runs are `UNKNOWN`, not `UNSAT`.  No phase formula, symmetry rule, or
all-`m` selector follows from (2.3).

### Theorem 2.2 (conditional protected atom closure)

Let the current refreshed bank `P_h` be its two directed paths with `2t`
diamonds.  Relative to the fixed SCD matching `M_0`, suppose every protected
diamond is either an old seed edge or one edge of a legal two-edge
detachment atom, with the forced `M_0` orientation.  Whenever one edge of an
atom is forced, force its partner as well.  The resulting closure
`widehat P_h` has

\[
                  |\widehat P_h|\le4t,
   \qquad\hbox{at most }16t=O(h)\hbox{ typed resources}.          \tag{2.4}
\]

If a phase-detachment selector contains this closure, satisfies all
provider/head/tail/release rows, and its rooted support is acyclic, then it
produces a forest of Theorem 1.1 containing the current refreshed bank.

If, in addition, the two protected paths occur contiguously in at most two
forest components and the component maximal-source test extends their fixed
letters, their literal collars use at most

\[
                         2t+2(h+1)+O(1)=O(h)          \tag{2.5}
\]

source positions.  Every interval wholly inside either halo then retains
its OR automatically; the `Theta(h^2)` internal addresses are derived from
these `O(h)` letters rather than separately protected tickets.

#### Proof

Each forced protected edge adds at most the one partner in its atom, giving
`|widehat P_h|<=2|P_h|=4t`.  A diamond uses one lower, one upper and two
labelled owner-slot resources, proving the second bound.  The detachment
palette ledger is unchanged by forcing complete atoms; rooted capacities
and acyclicity then give Theorem 1.1.  A depth-`h` path with `e` edges uses
`e+h+1` source positions.  Summing over two paths with `2t` total edges
gives (2.5).  Fixing those ordered letters fixes every internal interval OR.
\(\square\)

This is a conditional integration theorem, not an all-`m` protected
selector.  The transient proof state includes the selected atom ids and the
at most two marked components.  Once the forest is sealed, its owner output
again contracts to `(M_0,pi)`.

## 3. Exact component-braid completion

For one central state `(M_0,pi)`, contract each directed path component.
For `t in T_m` and `s in S_m`, declare a legal port arc

\[
                         t\longrightarrow s           \tag{3.1}
\]

when

\[
                         s\ne t,\qquad t\subset M_0(s),             \tag{3.1a}
\]

and the two roots lie in distinct contracted components.  This is the
literal incidence edge from lower root `t` to owner `M_0(s)`; in the owner
projection it joins `M_0(t)` to `M_0(s)` and has lower colour `t`.  The
equality case is the already used `M_0` edge, not a port arc.

This port graph is owner-level.  Source chronology, mixed crossing rows,
residence and common-cap compatibility are generally not edge-local and are
imposed jointly on the selected path in Section 4.

### Theorem 3.1 (free-port Hamilton braid)

The central forest extends to one rooted owner Hamilton path with exact
lower-`q1` palette except for one terminal colour `a` if and only if one can
select `C_m-1` legal port arcs whose contracted component graph is a
directed Hamilton path.

The unique component source not entered is the global root.  The unique
terminal `a in T_m` not used by a connector is the global terminal lower
colour.  The complete owner path then has

\[
                    U_m+(C_m-1)=W_m-1               \tag{3.2}
\]

Johnson edges and uses every lower colour except `a`.  Its immediate-upper
palette remains complete because the central `U_m` edges already supply it;
connector upper colours may repeat.

#### Proof

Each central component is a directed path with one free outgoing terminal
and one free incoming source.  Hence selected port arcs have contracted
indegree and outdegree at most one.  They connect all components without a
cycle exactly when they form one directed Hamilton path, necessarily using
`C_m-1` arcs.  Expanding the components gives one owner Hamilton path.  The
converse follows by deleting from any completion the `C_m-1` edges outside
the central forest.  \(\square\)

For the pivot-prefix architecture, one further requires the one or two
contiguous refreshed paths of Theorem 2.2 to occur first in their prescribed
order, with the first root globally unentered.  When two components are
used, the first selected port arc is their declared literal socket.  This is
a forced-edge/root/socket condition, not a new scalar row.

The finite witnesses in Section 2 do not certify Theorem 3.1 and were not
selected around the pivot packet.  For the project deadline values at
`m=4,...,8`, even the packet's disjoint-label supply condition
`3h<=m-1` fails, so these fixtures cannot serve as literal protected-packet
tests.

## 4. The regenerative same-parity state

The same-parity transition adjoins two coordinates to the old ground.  The
SCD construction uses a fresh canonical SCD on the entire old-coordinate
set and outputs a fresh `(M_0,pi)`.  It does not need the previous selected
forest.  This is the precise regenerative gain.

Let the local pivot-rich and rolling-refresh theorem be taken as frozen.
Set `h=d(2m-1)` and `B(2m-1)=W_m+h`.  Write `P_h` for its current
protected packet and `a` for the terminal lower cell.  An exact regenerative
child state consists of the following six layers.

1. **Central renewal.**  An atom-closed selector from Theorem 2.2 whose
   output `(M_0,pi)` satisfies Theorem 1.1 and contains the two refreshed
   paths contiguously in at most two rooted components.
2. **Component braid.**  A port Hamilton path from Theorem 3.1, beginning
   with those protected component(s) in their prescribed order and
   terminating at lower colour `a`.
3. **Ordered source/cap skeleton.**  Take `W_m+h+1` post-insertion source
   positions, a declared pivot position, and the preword obtained by
   deleting it.  Freeze the exact split-core pre/post letters on the
   protected prefix.  At every other position declare a point cap `C_p` and
   mandatory subset `D_p`.  Declare the depth-`h` intervals intended to be

   \[
        D^hA_m^+=(O_0,O_1,\ldots,O_{W_m-1},a),        \tag{4.1}
   \]

   every native lower-`q1` cell, the ordered overlap at every component
   seam, and every signed residence row.  All these desired equalities are
   hard rows of the cap system; source letters are not chosen yet.

4. **All-depth occurrence renewal.**  Give an explicit injective interval-
   address map from every retained parent occurrence to a contiguous child
   interval.  It must preserve the target id and literal OR under the word
   constructed in Layer 5.  Release every selected occurrence meeting a
   changed halo, a moved component boundary, or an address not covered by
   this map.  The transported ids together with the released and newborn
   ids partition **all nonempty child targets**.  Rematch the latter ids to
   pairwise-distinct residual child intervals.  A fixed-slot replacement
   may use a proved prefix/suffix deck inclusion or equality; component
   permutation is never inferred from a local signature.  Every chosen
   replacement address must separately pass its typed deadline, grade and
   guard; deck inclusion certifies OR coverage only.
5. **One common word.**  Let `M` be the union of the transported and new
   occurrence assignments.  Include the exact packet letters, owner rows,
   native cells, seam rows and residence guards among the hard/fixed rows.
   At each free position set `A^+_{m,p}=K_p(M)`, where `K_p(M)` is the
   maximal cap of Section 7; use the declared fixed letter at a fixed
   position.  Require (7.2)--(7.3) for every hard and selected row.  For
   each component seam, now computed in this same word, let `O` be the old
   owner, `S` the union of the retained ordered overlap, `U` the next owner
   and `E` the entering nonempty letter.  Check

   `S⊆O∩U`, `U-S⊆E⊆U`, `E∩(O-S)=∅`, and `|O△U|=2`,

   together with the exact native-cell and signed-run checks.  Define
   `A_m^-` by deleting the pivot; its protected prefix is required to be the
   frozen split-core preword.
6. **Recursive closure.**  The right terminal socket, ordered overlap,
   capped age vector, prefix/suffix deck state and refresh birth ledger
   emitted by `A_m^+` satisfy the declared input predicate of the next
   same-parity state.

At the open right boundary export the terminal owner/lower pair, the ordered
`h` overlap letters, capped signed residence ages, the compressed prefix and
suffix OR decks (or the stronger ordered signatures when addresswise
transport is used), and the current packet/refresh phase.  Since the packet
is placed first, no left interface is exported.

### Theorem 4.1 (conditional one-step and regenerative transition)

If Layers 1--5 exist at parameter `m`, then the word `A_m^+` constructed in
Layer 5 has length `B(2m-1)+1`, its depth-`h` row is the literal owner-simple
chronology (4.1), its immediate palettes are complete, it is globally
resident, and it covers every nonempty target.  If Layer 6 also holds, this
one-step certificate is a regenerative transition and exports an accepted
right boundary state for the next same-parity step.

#### Proof

Theorem 1.1 supplies the upper-exact `C_m`-component forest and its exact
used lower palette.  Theorem 3.1 adds precisely the other `C_m-1` lower
colours and orders every owner once, leaving only `a`.  The maximal-cap
criterion constructs one word, not a second post-hoc realization: all
owner, native-cell, packet, seam and residence equations were inserted as
hard rows before `K_p(M)` was evaluated.  Layer 4 partitions every nonempty
target id and assigns it a distinct exact interval of this same word.  The
joint seam and signed-age tests make the abstract component braid a literal
resident chronology.  The frozen pivot theorem identifies its declared
pre/post prefix.  When assumed, Layer 6 is exactly the next-state acceptance
assertion.  No marginal Hall or cross-word cap step is hidden in the
argument.  \(\square\)

This theorem is conditional.  In particular, a fresh owner forest does not
transport the old source word: the SCD roots remember the old ground set,
not the old chronology or its target occurrences.

## 5. What is and is not bounded

The owner **boundary debt** is bounded in arity.  Once the child is built,
all `C_m` internal components and connectors are sealed.  The exported
owner data are only a distinguished root, a terminal lower/owner pair, one
packet phase, and one right source boundary.

The literal boundary is larger:

\[
\begin{array}{c|c}
\text{object}&\text{current size}\\ \hline
\text{protected rolling-refresh forest bank}&O(h)\\
\text{ordered right overlap/source halo}&O(h)\\
\text{derived upper addresses in the two halos}&\Theta(h^2)\\
\text{signed endpoint run vector}&O(m)\text{ labelled entries}.
\end{array}                                                     \tag{5.1}
\]

The protected forest bank is `o(m)` in the triangular regime.  Conditional
on the protected all-`m` selector, it can be reselected from scratch rather
than accumulated historically.  This does **not** prove renewal of the
source halo, age ledger, shadow occurrences, or common cap.  What is proved
is a constant schema and an `O(h)` current local bank, not a
constant-information automaton.

### Proposition 5.1 (no unrestricted finite crossing state)

For a block `B`, let `P(B)` and `S(B)` be the sets of distinct OR values of
its prefixes and suffixes.  In a fixed exterior slot, replacement
`B_old -> B_new` preserves every old crossing OR whenever the total OR is
unchanged and

\[
                 P(B_{\rm old})\subseteq P(B_{\rm new}),\qquad
                 S(B_{\rm old})\subseteq S(B_{\rm new}).          \tag{5.2}
\]

For two-way universal crossing equivalence these inclusions become
equalities.  Addresswise preservation at the same prefix/suffix lengths is
the stronger condition of equal ordered signatures.

If the ground has at least `ell` distinct labels and `ell>=3`, there are at
least `(ell-2)!` two-way crossing-equivalence classes even among blocks
having the same first letter, last letter and total OR.  Hence an
unrestricted exact equivalence interface needs at least

\[
                         \log_2((\ell-2)!)            \tag{5.3}
\]

bits; no dimension-independent finite state can be universally correct.

#### Proof

For a crossing at the left boundary, the exterior suffix is fixed and only
the prefix OR of the inserted block varies; (5.2) therefore supplies the
same old union value.  The right boundary is dual, and intervals crossing
both boundaries use the equal total OR.  This proves the one-way statement;
apply it in both directions for equivalence.

For the lower bound, fix the first and last singleton letters and permute
`ell-2` distinct internal singleton letters.  All resulting blocks have the
same endpoints and total OR.  Their prefix decks are pairwise different:
the unique prefix value of each cardinality recovers the next label in the
permutation.  Hence no two are two-way crossing-equivalent.  \(\square\)

This does not refute a structured recurrence.  For nested flags

\[
 L_1\supseteq\cdots\supseteq L_p,qquad
 Q_1\subseteq\cdots\subseteq Q_q,                    \tag{5.4}
\]

the `p+q-1` Ferrers rail

\[
 L_1Q_1,\ldots,L_pQ_1,L_pQ_2,\ldots,L_pQ_q           \tag{5.5}
\]

realizes all `pq` unions.  Thus an `O(h)` structured shadow state remains a
live possibility; cap-legal embedding of that rail is not proved.

## 6. Exact deep-shadow renewal gate

For every source word and every valid `q>=0`, the owner chronology obeys

\[
 D^{h+q}A_s=\bigcup_{j=0}^{q}(D^hA)_{s+j}.            \tag{6.1}
\]

Therefore a fixed braided owner order determines all upper interval values.
It does not imply that every required target has a surviving occurrence.
The finite SCD certificates verify only the immediate (`q=1`) upper and
lower palettes.

Equivalently, for `q>=1` and consecutive physical forest edges `e_j=A_jB_j`, put
`lambda(e_j)=A_j union B_j`.  A rank-`(m+q)` target `X` has a width-`q`
owner witness exactly when some `q` consecutive edges satisfy

\[
 \lambda(e_j)\subseteq X\quad(1\le j\le q),\qquad
 \bigcup_{j=1}^{q}\lambda(e_j)=X.                    \tag{6.2}
\]

This is a checkable forest-level deep-upper gate, not a consequence of
upper-`q1` bijectivity.

An exact same-parity renewal must provide one occurrence assignment with:

1. injective transport of every untouched parent target occurrence into
   its child Pascal sector;
2. complete release of every selected occurrence meeting a changed refresh
   halo or component seam;
3. a cell-disjoint rematching of the released targets and all newborn
   targets at every depth; and
4. an explicit mapped occurrence, the one-way compressed deck inclusions
   of Proposition 5.1 for a fixed-slot replacement, or explicit release of
   every crossing witness.  Ordered signature equality is the stronger
   addresswise sufficient form.

The current two refresh halos contain `Theta(h^2)` derived upper addresses.
Under Theorem 2.2's two-component contiguous source lift, their internal
values are automatic consequences of `O(h)` fixed letters and need no
separate tickets.  What remains is the exterior/crossing occurrence map and
its common cap.  Without contiguity, an `O(h)` abstract atom closure may
fragment over `Theta(h)` components and naive literal collars again cost
`Theta(h^2)`.  Likewise, abstract intersections of consecutive owners do
not certify literal lower compiler cells; those depend on the actual source
letters and selected interval addresses.

## 7. Exact common-cap gate

Fix a candidate occurrence matching `M`.  At a free source position `p`,
let `C_p` be its point cap and `D_p` its mandatory subset.  Intersect `C_p`
with every hard-row target and every target selected by `M` whose interval
contains `p`.  For each hard or selected row `R`, let `I_R` be its free
position set, `S_R` its required OR value, and `B_R` the union of its frozen
exterior letters.  Then

\[
 K_p(M)=C_p
  \cap\!\bigcap_{R:p\in I_R}S_R
  \cap\!\bigcap_{(T,c)\in M:p\in I_c}T.              \tag{7.1}
\]

### Theorem 7.1 (maximal common word)

One nonempty source word realizes all frozen, hard, and selected rows if and
only if

\[
 D_p\subseteq K_p(M)\ne\varnothing                   \tag{7.2}
\]

at every free position, every fixed position passes the analogous cap and
row intersections, and every hard and selected row reconstructs exactly:

\[
                B_R\cup\bigcup_{p\in I_R}K_p(M)=S_R. \tag{7.3}
\]

#### Proof

Every feasible source letter `A_p` must lie in each set intersected in
(7.1), so `D_p⊆A_p⊆K_p(M)`.  For any feasible row,

\[
 S_R=B_R\cup\bigcup_{p\in I_R}A_p
   \subseteq B_R\cup\bigcup_{p\in I_R}K_p(M)
   \subseteq S_R,
\]

which proves the necessary reconstruction equality.  Conversely choose the
maximal letter `K_p(M)` at every free position.  Equations (7.2)--(7.3),
together with the fixed-position checks, then realize every row and keep
every source letter nonempty.  \(\square\)

Occurrence Hall does not imply this theorem.  With two positions capped by
`{z,a}` and `{z,b}`, select singleton rows `{a}` and `{b}` and require their
two-position union to be `{z,a,b}`.  The occurrence matching is perfect,
but the maximal letters are `{a}` and `{b}`, whose union loses `z`.
Therefore deep occurrence matching, component-braid selection, graphic
independence, and common cap must be imposed for the same source state.

## 8. Sharp remaining theorem boundary

The same-parity program is reduced to the following three correlated
existence statements.

1. **Protected all-`m` SCD detachment.**  Extend the flexible option grammar
   to every `m`, force the current atom closure, retain provider/head/tail
   uniqueness plus acyclicity, and place the two refreshed paths contiguously
   in at most two components.  The finite witnesses have empty protected
   bank and do not prove this.
2. **Rooted component braid.**  In the resulting port digraph, find a
   directed Hamilton path beginning with the packet component and ending at
   the prescribed terminal lower colour.  Automatic leave alignment removes
   one former Hall row but does not imply this path.
3. **Shadow/cap renewal.**  Realize that owner path by one source chronology,
   transport/rematch every all-depth target occurrence with explicit
   address maps or sufficient boundary-deck inclusions, and satisfy
   (7.1)--(7.3) for that same matching.

The central owner choice is regenerative and nonaccumulating **conditional
on Gate 1**.  The precise unproved bridge is the third statement, together
with protected selection and port ordering.  Local pivot and rolling
residence geometry are solved; their source/deep/common-cap integration is
part of Gate 3 and is not solved.

## 9. Provenance

The finite selector source is

```text
scratch/search_scd_global_seed_detachment_sat_20260801.cpp
```

with SHA-256
`16faf809cdb88942df4702874165d9f276e0e6ca182ceada33009ff229931911`.
The five saved model hashes are

```text
m=4  182bf5e4690f0c8b625992bbcb98fe01b96edca24cc719ccee4c3c301fe54aff
m=5  82e2e70ebf892c07682ec1525a18cc9c125e6bdc7f7c1b955bd150c5f9c0c273
m=6  a5d1e7f624cb9f31e9fe6677df58f015390240e866e13f8e47a5ca515bf74e75
m=7  031a9755e912a0221035fa549ea9f5241bfef6e0ca1f618b84590fbfd3c93af1
m=8  4a6a1fd1e93ec7a56401a9294924207132ac5144a41faebbc24d8eb50ce2aa00
```

Independent forest replay is frozen in

```text
scratch/h2_scd_phase_detachment_20260801/
  independent_acyclicity_refresh.audit.json
```

with file SHA-256
`b1cd2cc6920b66e110426ed0b33373fe3dd1cbec8bf1979bae5d929739c56417`,
payload SHA-256
`d28ff48d48c2e8c43efbb7242e91e7cdecf65333fddb31a9dc079455b649c088`,
and status
`PASS_FOREST_WITNESSES_M4_M8_BUT_AUTOMATIC_ACYCLICITY_FALSE_M4`.
