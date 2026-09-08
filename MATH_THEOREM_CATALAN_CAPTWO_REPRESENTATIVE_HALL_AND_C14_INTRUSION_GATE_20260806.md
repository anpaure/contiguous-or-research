# Cap-two Catalan representatives and the C14 connector intrusion gate

## Status

This note is purely mathematical.  It uses no finite search.

For a fixed upper-surjective cap-two middle-level factor, the selection of
an upper-exact rooted Catalan forest collapses to one ordinary Hall system:
factor cycles must be assigned distinct duplicated upper colours occurring
on them.  A particularly simple sufficient condition is that every factor
cycle contain two deletable duplicated-colour occurrences.

The new linear-size Boolean `C14` reservoir does not, by itself, finish the
connector stage.  A pairwise resource-disjoint bank of `C14` switches which
is confined to the `C` nonrepresentative connector edges leaves at least
`ceil(C/7)` components in the componentwise-closed starting state.  More
generally, reducing `C` components to `b` by disjoint `C14` switches forces
at least

\[
             7\left\lceil {C-b\over6}\right\rceil-C
             \ge {C-7b\over6}                         \tag{0.1}
\]

distinct old representative edges into the switch bank.  Thus an
`O(1)`-component construction using the anonymous linear `C14` bank must
transport `Theta(C)` named upper representatives; it cannot keep the
rooted Catalan forest frozen.

After that transport is included in each mode, the remaining connector
statement is again an exact Hall condition, now from factor cycles to
hereditarily accessible upper-safe `C14` buffers.  This is the sharp
all-cut obstruction left by the cap-two/Catalan route.

## 1. Rooted factor notation and the Catalan excess

Put

\[
 \mathcal L={ [2m-1]\choose m-1},\qquad
 \mathcal O={ [2m-1]\choose m},\qquad
 \mathcal U={ [2m-1]\choose m+1},                    \tag{1.1}
\]

and

\[
 W=|\mathcal L|=|\mathcal O|,qquad
 U=|\mathcal U|,qquad
 C=W-U={2W\over m+1}=\operatorname {Cat}_m.          \tag{1.2}
\]

Fix two edge-disjoint perfect incidence matchings `M_0,M_1` between
`mathcal L` and `mathcal O`.  Relative to `M_0`, every edge `e=LV` of
`M_1` has rooted arc

\[
       \lambda(e):L\longrightarrow M_0^{-1}(V)       \tag{1.3}
\]

and immediate-upper colour

\[
       u(e)=M_0(L)\cup V\in\mathcal U.                \tag{1.4}
\]

The arcs of `M_1` form a directed cycle cover on the `W` rooted vertices.
Let `mathcal K` be its factor-cycle set.

Assume the upper palette is **cap two and complete**:

\[
             1\le\mu_R:=|\{e\in M_1:u(e)=R\}|\le2
             \qquad(R\in\mathcal U).                  \tag{1.5}
\]

Since `sum_R mu_R=W=U+C`, exactly `C` colours occur twice.  Denote their
set by

\[
             \mathcal D=\{R:\mu_R=2\},\qquad
             |\mathcal D|=C.                          \tag{1.6}
\]

This is the cap-two specialization of upper-defect conservation.  The
`C` deletions needed to retain one occurrence of every upper colour are
exactly one deletion from each class `E_R=u^{-1}(R)`, `R in mathcal D`.

Let `P subseteq M_1` be a protected occurrence bank which may not be
deleted.  Make the bipartite **cycle--duplicate graph**

\[
 H_P=(\mathcal K,\mathcal D;E),                         \tag{1.7}
\]

where `K R` is an edge precisely when cycle `K` contains an occurrence

\[
             e\in E_R-P.                               \tag{1.8}
\]

Equal upper masks at different occurrences remain distinct physical
edges; the colour vertex records only the one deletion quota for that
duplicated class.

## 2. Exact representative-forest Hall theorem

### Theorem 2.1 (cycle--duplicate Hall equivalence)

There is a set `Q_0 subseteq M_1` such that

1. `P subseteq Q_0`;
2. `Q_0` contains exactly one occurrence of every `R in mathcal U`; and
3. the rooted graph `lambda(Q_0)` is a forest,

if and only if

\[
             |N_{H_P}(\mathcal A)|\ge|\mathcal A|
             \qquad(\mathcal A\subseteq\mathcal K).  \tag{2.1}
\]

Whenever it exists, `Q_0` has `U=W-C` edges and exactly `C` rooted path
components.  If the Hall deficiency is

\[
 \delta_P=
 \max_{\mathcal A\subseteq\mathcal K}
       (|\mathcal A|-|N_{H_P}(\mathcal A)|),           \tag{2.2}
\]

then the least possible number of old factor cycles left completely
inside an upper-exact protected representative set is exactly `delta_P`.

#### Proof

Choosing one representative of every upper colour is equivalent to choosing
one deletion from each duplicated class `E_R`, `R in mathcal D`, and no
deletion from a unique class.  Because `M_1` is a directed cycle cover, the
kept set is a forest exactly when the deletion set meets every factor
cycle.  Protected occurrences are retained exactly when all deletions lie
outside `P`.

Thus a representative forest gives, by assigning to each factor cycle one
of the distinct duplicated colours whose deleted occurrence lies on it, a
matching of `H_P` saturating `mathcal K`.  Conversely, a matching saturating
`mathcal K` chooses one allowed deletion of a distinct duplicated colour on
every cycle.  Choose an arbitrary allowed occurrence for the deletion quota
of every still-unassigned duplicated colour.  Different colour classes are
disjoint, so these extra choices do not collide.  The resulting `C`-edge
deletion set avoids `P`, deletes exactly one occurrence of every duplicated
colour, and meets every factor cycle.  Its complement is therefore the
required upper-exact forest.

The kept forest has `W` vertices and `U=W-C` edges, hence `C` components.
The deficiency statement is the defect form of Hall: at most
`|mathcal K|-delta_P` old cycles can receive distinct deletion colours, and
the construction above breaks every assigned cycle.  `square`

Theorem 2.1 is also the Edmonds common-base condition for the upper-colour
partition matroid and the rooted graphic matroid, specialized to a cycle
cover.  Upper-defect conservation turns the abstract rank inequalities into
the concrete Hall cuts (2.1).

### Corollary 2.2 (two available repeats per cycle suffice)

If every factor cycle contains at least two occurrences outside `P` whose
upper colours lie in `mathcal D`, then (2.1) holds and a protected rooted
Catalan forest exists.

#### Proof

For `mathcal A subseteq mathcal K`, count available duplicated-colour
occurrences on its cycles.  There are at least `2|mathcal A|`.  One
duplicated colour has exactly two occurrences in the entire factor, so it
contributes at most two to this count.  Therefore

\[
                         |N_{H_P}(\mathcal A)|
                         \ge |\mathcal A|.             \tag{2.3}
\]

Apply Theorem 2.1.  `square`

This condition is close to the exact scalar limit: the entire factor has
only `2C` duplicated-colour occurrences.  In particular it also implies
`|mathcal K|<=C`.

### Theorem 2.3 (abstract two-repeat target is always attainable)

Assume

\[
                         |\mathcal K|\le C,           \tag{2.4}
\]

every factor cycle has at least two row occurrences outside `P`, the
colours on `P` are distinct, and

\[
                         |u(P)|<{m-1\over2}.          \tag{2.5}
\]

Then there is a cap-two complete target palette on the same `W` labelled
factor rows such that

1. every row of `P` keeps its old upper colour;
2. the target has the exact coordinate current of `M_0 union M_1`; and
3. every factor cycle contains at least two unprotected occurrences of
   duplicated target colours.

Moreover the old and target palette matrices are connected by ordinary
`2x2` row-coordinate switches which never use a row of `P`.

#### Proof

By the protected simple Catalan target theorem, choose a simple regular
family

\[
                         \mathcal D^*\subseteq\mathcal U,
                         \qquad|\mathcal D^*|=C,       \tag{2.6}
\]

disjoint from `u(P)`, such that the row multiset

\[
                         1+\mathbf1_{\mathcal D^*}    \tag{2.7}
\]

has exactly the coordinate current of two edge-disjoint perfect
middle-level matchings.

Choose two unprotected row labels from every factor cycle.  This uses at
most `2C` labels by (2.4).  Add arbitrary unprotected labels until exactly
`2C` labels have been chosen.  There are enough such labels: for `m=3`,
(2.5) forces `P=emptyset` and `W=2C`; for `m>=4`,

\[
 W-2C={m-3\over m+1}W\ge {m-1\over2}>|P|.            \tag{2.8}
\]

Assign the two copies of every colour in
`mathcal D^*` bijectively to these labels, making sure that the first two
chosen labels on each cycle receive duplicated-colour copies.  Assign the
single copy of every other target colour to the remaining labels, retaining
the already fixed protected rows.  This is possible because
`mathcal D^* cap u(P)=emptyset` and the protected colours are distinct.

All rows have the same rank, and the old and target matrices have the same
coordinate column sums.  They agree on every protected row.  The row-fixed
Ryser theorem therefore connects them by `2x2` interchanges avoiding `P`.
`square`

Theorem 2.3 proves that cycle dispersion of the Catalan duplicate bank has
no abstract current or row-matrix obstruction.  Its unproved step is
literal: a row-coordinate Ryser interchange need not be an installed
Boolean matching switch, and a sequence of abstract interchanges need not
preserve the rooted factor or its source chronology.  The `C14` bank is a
candidate physical lift of this exact abstract transport.

## 3. What the residual Catalan bank does

Let `D=M_1-Q_0`.  Then

\[
                         |D|=C.                       \tag{3.1}
\]

Every component of `Q_0` has one free outgoing and one free incoming port,
and `D` is a perfect matching between those port shores.  Thus, after
contracting the `C` paths of `Q_0`, the full factor is a permutation on `C`
component vertices.  If it has `q` cycles, deleting one edge of `D` from
each such cycle gives a protected upper-surjective `q`-path forest; every
deleted edge is a nonrepresentative occurrence, so no upper colour is lost.

This is the exact Catalan forest/connector decomposition.  The issue is not
the number of connector edges: the residual bank already has exactly `C`.
The issue is changing its component permutation while preserving the named
upper representatives and the literal lower flags.

## 4. A sharp limitation of disjoint connector-only C14 switches

An alternating switch on a Boolean incidence `C_(2s)` replaces `s` old
matching edges by `s` new matching edges.  On the rooted permutation it
composes one side with an `s`-cycle.  Since an `s`-cycle is a product of
`s-1` transpositions, one switch changes the number of permutation cycles
by at most `s-1`.

For a `C14`, `s=7`.

### Theorem 4.1 (connector-only noncontraction)

Start from the componentwise closure of `Q_0`, so the residual matching
`D` closes each of the `C` Catalan paths separately and the full rooted
factor has `C` cycles.  Let `t` Boolean `C14` switches have pairwise
resource-disjoint old phases, and suppose every old edge used by every
switch belongs to `D`.  Then

\[
                  t\le\left\lfloor {C\over7}\right\rfloor,
 \qquad
 c_{\rm final}\ge C-6t
                  \ge\left\lceil {C\over7}\right\rceil. \tag{4.1}
\]

In particular, a one-shot resource-disjoint `C14` bank confined to the
nonrepresentative Catalan connectors cannot give `O(1)` components.

#### Proof

Every old phase contains seven distinct matching edges.  Resource
disjointness and `|D|=C` give the first inequality.  One toggle lowers the
cycle count by at most six, so the total decrease is at most `6t`.  Writing
`C=7a+b`, `0<=b<7`, gives

\[
 C-6\lfloor C/7\rfloor=a+b\ge\lceil C/7\rceil.       \tag{4.2}
\]

`square`

### Theorem 4.2 (representative-intrusion lower bound)

Under the same componentwise-closed start, suppose a pairwise
resource-disjoint family of `C14` switches reduces the factor to at most
`b` cycles.  The number `a` of distinct old edges of `Q_0` used by the
switches satisfies

\[
 \boxed{
 a\ge
 7\left\lceil {C-b\over6}\right\rceil-C
 \ge {C-7b\over6}.}                                    \tag{4.3}
\]

Hence for fixed `b`, at least `C/6-O(1)` selected upper representatives
must participate in the switch bank.

#### Proof

If there are `t` switches, the cycle-count bound gives

\[
                         6t\ge C-b.                    \tag{4.4}
\]

Their disjoint old phases contain `7t` distinct matching edges.  At most
the `C` edges of `D` are nonrepresentatives, so at least `7t-C` of them
belong to `Q_0`.  Substitute the least integral value of `t` allowed by
(4.4).  The second inequality follows by deleting the ceiling.  `square`

Theorem 4.2 is the precise interaction between the linear `C14` reservoir
and upper-defect conservation.  The anonymous ambient bank has enough
physical resources for `Theta(C)` switches, because `C=Theta(W/m)` while
the bank has `Omega(W)` members.  But any disjoint bank strong enough to
Hamiltonize the componentwise Catalan closure necessarily enters
`Theta(C)` representative edges.  Its modes must therefore carry a
simultaneous occurrence-level upper transport.  Lower-flag preservation by
itself is insufficient.

Sequential reuse of a bounded anchor bank lies outside Theorems 4.1--4.2;
so does a construction whose residual matching is already an
`O(1)`-cycle permutation.  These are exactly the two ways to evade the
count.

For the explicit anonymous lower bound `W/98`, scalar capacity already
exceeds the information-theoretic switch count for all sufficiently large
`m`:

\[
 {W\over98}\ge {C\over6}={W\over3(m+1)}
                         \qquad(m\ge32).               \tag{4.5}
\]

Thus the intrusion theorem is not another cardinality obstruction.  It
says exactly that the available ambient capacity must be bound to named
upper transport on a Catalan-scale subset of representative occurrences.

## 5. Exact C14 cycle-to-buffer Hall theorem

The preceding lower bound does not say that the required transport is
impossible.  It identifies what a complete buffer mode must include.

Let `F` be a protected upper-surjective cap-two factor.  Delete one
nonprotected duplicated-colour occurrence to open one factor cycle into a
directed anchor path.  Call the remaining directed factor cycles
`mathcal Z`.

Let `mathcal B` be a pairwise resource-disjoint installed bank of Boolean
`C14` buffers.  A **whole accepting mode** from `Z in mathcal Z` to
`B in mathcal B` consists of a fixed phase change such that

1. the old phase is literally present in the current factor;
2. the main square imports `Z` into the anchor path and creates no new
   directed cycle;
3. every deleted immediate-upper representative is retained elsewhere or
   recreated by the new phase, so the complete upper palette survives;
4. every attached lower flag, protected occurrence, residence ticket, and
   declared exterior state is retained or explicitly transported; and
5. modes fixed for distinct buffers are hereditarily compatible: after any
   subset is applied, every unused fixed mode remains present and its path
   anchors remain in the required directed order.

Make the bipartite graph

\[
             G=(\mathcal Z,\mathcal B;E_G),            \tag{5.1}
\]

where `ZB in E_G` when one such whole accepting mode has been fixed.

### Theorem 5.1 (exact installed-buffer deficiency)

Within this declared mode bank, the minimum number of unabsorbed factor
cycles is

\[
 \boxed{
 \delta(G)=
 \max_{\mathcal A\subseteq\mathcal Z}
       (|\mathcal A|-|N_G(\mathcal A)|).}              \tag{5.2}
\]

In particular, all cycles are absorbed if and only if

\[
             |N_G(\mathcal A)|\ge|\mathcal A|
             \qquad(\mathcal A\subseteq\mathcal Z).   \tag{5.3}
\]

#### Proof

Hall deficiency is the number of cycle vertices left unmatched by a
maximum matching of `G`.  Apply the fixed mode assigned to each matched
cycle--buffer pair.  Resource disjointness and hereditary compatibility
allow the modes to be applied in any order.  Every application imports
exactly its assigned cycle into the anchor path, preserves the full upper
palette and all declared guards, and leaves every unmatched cycle
unchanged.  Thus precisely the unmatched cycles remain.  Conversely one
buffer has one phase bit and can process at most one assigned cycle in this
construction class, so every absorbed-cycle set gives a matching in `G`.
`square`

A convenient sufficient condition is

\[
 \min_{Z\in\mathcal Z}d_G(Z)\ge\lambda,qquad
 \max_{B\in\mathcal B}d_G(B)\le\mu,qquad
                         \lambda\ge\mu.               \tag{5.4}
\]

Indeed, double counting incidences between any
`mathcal A subseteq mathcal Z` and `N_G(mathcal A)` gives

\[
             \lambda|\mathcal A|
             \le\mu|N_G(\mathcal A)|.                 \tag{5.5}
\]

The same calculation with `lambda/mu=1-epsilon` gives the exact
`epsilon`-fractional all-cut bound required by a contracting defect
recurrence.

## 6. Consequences for recursion and matroid/base exchange

The cap-two Catalan route now has two exact combinatorial cuts.

1. **Representative cut.**  Equation (2.1) is necessary and sufficient to
   extract the upper-exact rooted Catalan forest from a fixed cap-two
   factor.  It is an ordinary Hall theorem, equivalently the specialized
   partition/graphic common-base min--max.
2. **Connector-buffer cut.**  Equation (5.3), or bounded deficiency in
   (5.2), is necessary and sufficient inside a prepared upper-safe `C14`
   mode bank.

The linear anonymous `C14` theorem proves only

\[
                         |\mathcal B|=\Omega(W).       \tag{6.1}
\]

It proves neither one edge of `G` nor the upper transport forced by
Theorem 4.2.  In particular, raw buffer capacity cannot be substituted for
(5.3).

Likewise, a recursive construction which produces only a cap-two palette
and a two-factor does not imply (2.1): duplicated occurrences may be
concentrated on too few factor cycles.  Corollary 2.2 identifies a sharp
local invariant which is sufficient and uses exactly the correct Catalan
scale.

Therefore either of the following would give an `O(1)`-defect owner/q1
construction:

* recursively maintain two available duplicate occurrences per factor
  cycle and a whole accepting `C14` linkage graph with `delta(G)=O(1)`; or
* construct the rooted Catalan forest directly, choose a residual connector
  permutation with `O(1)` cycles, and avoid the `C14` intrusion altogether.

The first route is a genuine occurrence-addressed recursion theorem, not a
matroid consequence.  The second is the original protected
Catalan-connector theorem.  The new sharp obstruction is that no
resource-disjoint bounded-support exchange proof can interpolate between
them while freezing the selected upper representatives: it must transport
`Theta(C)` named upper occurrences or reuse a regenerative anchor.

## 7. Remaining scope

This note closes the abstract representative selection and identifies the
exact terminal linkage cut.  It does not construct

* the cap-two protected factor;
* the two-repeat-per-cycle invariant;
* the whole accepting edges of `G`;
* a regenerative anchor permitting sequential resource reuse;
* arbitrary-width upper witnesses, source residence, or the common cap.

Consequently it is a strict reduction of the owner/immediate-upper topology
gate, not a proof of `nu(k)<=B(k)+O(1)`.
