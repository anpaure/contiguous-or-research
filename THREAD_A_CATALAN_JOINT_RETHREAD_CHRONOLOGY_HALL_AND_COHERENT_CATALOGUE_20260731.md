# Joint rethread--chronology Hall and the quantifier-correct coherent catalogue

Date: 2026-07-31  
Status: exact all-dimension reductions and one exact `m=5` counterexample;
no all-`m` catalogue construction and no coefficient-one conclusion

## 0. Verdict

There are two exact but logically different selection problems.

1. For a proposed Hamilton chronology of the middle layer, the existence of
   one exact two-palette Catalan forest is **exactly** a perfect-matching
   problem in its lower--upper occurrence-colour graph.  The associated
   Hall cuts are the missing min--max rows in a joint rethread/chronology
   model.
2. After a repaired fixed decoration has been prepared, item 2192 reduces
   transparent component gluing to coherent merge-edge supply, one
   forced-port residual Hall matching, and router resilience.  These three
   requirements must have one common decoration/tree quantifier.

The common quantifier is load-bearing.  Router resilience for a catalogue
and forced-port feasibility for an unrelated tree do not compose.

The canonical optimal `K10` chronology supplies a sharp finite warning.  It
is a Hamilton path, has both immediate palettes separately, has the complete
minimal all-depth flag tower, has internal positive runs of length at least
three, and admits `COMP_2`.  Nevertheless its occurrence-colour graph has
matching number `186` rather than `210`; an explicit Hall shore has size
`50` and only `26` neighbours.  Thus the common matching row is independent
of the other listed marginal/chronology rows.

The exact remaining all-`m` supply lemma is stated in Section 7.  The six
shared-decoration rows of the repaired `ML(7)` cycle are Hamilton
**rethreads**, not component merges.  Its fifteen splitting toggles have no
common decoration.  Item 2171 is the separate positive `m=4` merge fixture.

## 1. The occurrence-colour graph

Fix `m>=1`, and put

\[
 \mathcal X={ [2m]\choose m},\qquad
 \mathcal L={ [2m]\choose {m-1}},\qquad
 \mathcal U={ [2m]\choose {m+1}}.
\]

Write

\[
 M=|\mathcal X|={2m\choose m},\qquad
 N=|\mathcal L|=|\mathcal U|={2m\choose {m-1}},
 \qquad K=M-N=\operatorname {Cat}_m.                 \tag{1.1}
\]

Let

\[
 T=(X_0,X_1,\ldots ,X_{M-1})                         \tag{1.2}
\]

be a Hamilton path of `J(2m,m)`.  For its adjacency occurrence `e_i` put

\[
 \ell(e_i)=X_i\cap X_{i+1}\in\mathcal L,
 \qquad
 u(e_i)=X_i\cup X_{i+1}\in\mathcal U.               \tag{1.3}
\]

The **occurrence-colour graph** `G_T` is the bipartite multigraph on
`mathcal L dotcup mathcal U` with one occurrence edge
`(ell(e_i),u(e_i))` for every chronology adjacency.  Occurrences, rather
than only unordered colour pairs, are retained.

### Theorem 1.1 (exact chronology--decoration equivalence)

The following are equivalent.

1. `G_T` has a perfect matching.
2. There is a set `F subseteq E(T)` which uses every lower colour and every
   upper colour exactly once.
3. The chronology `T` contains, on its own edges, an exact two-palette
   Catalan linear forest.

When these conditions hold, `F` has `N` edges, spans all `M` middle
vertices, and has exactly `K` path components, isolated vertices included.
The `K-1` chronology edges outside `F` are exactly the ordered physical
seams between those components.

#### Proof

A perfect matching in `G_T` selects one occurrence incident with every
vertex of `mathcal L dotcup mathcal U`; the corresponding chronology edges
give item 2.  Conversely, item 2 is precisely a perfect matching of the
occurrence graph.

Every subset of the edge set of a path is a spanning linear forest.  It has
`N` edges, so its component number is

\[
                         M-N=K.                      \tag{1.4}
\]

Deleting `N` selected edges from the `M-1` chronology adjacencies leaves
`K-1` breaks.  Since the selected components are consecutive intervals of
`T`, every break joins two consecutive components and their contraction is
a path.  This proves item 3 and the seam statement.  The converse from item
3 to item 2 is its exact palette definition.  QED.

The support clause is essential.  The theorem does not say that an
arbitrary Catalan linear matching, using Johnson edges outside `T`, can be
embedded into this chronology.

## 2. Exact Hall projection

Let `y_e` be the indicator that Johnson edge occurrence `e` belongs to the
chosen chronology and let `f_e` be its decoration flow.  Conditional on an
integral Hamilton path `y`, impose

\[
 0\le f_e\le y_e,\qquad
 \sum_{\ell(e)=L}f_e=1\quad(L\in\mathcal L),\qquad
 \sum_{u(e)=U}f_e=1\quad(U\in\mathcal U).            \tag{2.1}
\]

### Theorem 2.1 (exact Benders cuts)

System (2.1) is feasible if and only if, for every
`S subseteq mathcal L` and `Q subseteq mathcal U`,

\[
 \boxed{
 \sum_{\substack{\ell(e)\in S\\u(e)\notin Q}}y_e
       \ge |S|-|Q|.}                                 \tag{2.2}
\]

For integral `y`, a feasible `f` may be chosen integral.

#### Proof

Use the usual unit-capacity network

\[
 s\longrightarrow\mathcal L\longrightarrow\mathcal U
 \longrightarrow t,
\]

giving the occurrence arc associated with `e` capacity `y_e`.  A cut whose
source side contains exactly `S` on the lower shore and `Q` on the upper
shore has capacity

\[
 N-|S|+|Q|+
 \sum_{\substack{\ell(e)\in S\\u(e)\notin Q}}y_e.    \tag{2.3}
\]

All cuts have capacity at least `N` exactly when (2.2) holds.  Max-flow/
min-cut gives (2.1), and bipartite-flow integrality gives an integral
perfect matching when `y` is integral.  QED.

For fractional `y`, (2.2) proves only the existence of a fractional `f`;
it is not an integrality theorem for the joint chronology polytope.

If full diamond occurrences are protected in advance, they must themselves
form a matching.  Delete their lower and upper endpoints and apply (2.2) to
the residual graph.  This ordinary protected-edge statement must not be
confused with item 2192's forced **one-shore port** problem; the latter has
the additional cyclic-gap constraint of Section 6.

## 3. Exact residence cuts on an integral chronology

For a coordinate `x` and bit `epsilon in {0,1}`, let

\[
 V_{x,\epsilon}=\{X\in\mathcal X:1_{x\in X}=\epsilon\}. \tag{3.1}
\]

Thus `epsilon=1` controls positive runs and `epsilon=0` controls gaps.

### Theorem 3.1 (short internally bounded run cut)

Let `y` be an integral Hamilton path on `mathcal X`.  It has no internally
bounded `epsilon`-run of coordinate `x` of length at most `d` if and only if
for every nonempty `S subseteq V_(x,epsilon)` with `|S|<=d`,

\[
 \boxed{
 3y(E(S))+y(E(S,\mathcal X\setminus V_{x,\epsilon}))
       \le 3|S|-2.}                                  \tag{3.2}
\]

Endpoint runs are intentionally exempt.

#### Proof

Let the selected graph induced by `S` have `c` nonempty components, `i`
internal edges, and `t` selected edges from `S` to the opposite bit shore.
Since the selected graph is a path,

\[
                  i\le |S|-c,\qquad t\le2c.          \tag{3.3}
\]

Consequently

\[
                       3i+t\le3|S|-c.                \tag{3.4}
\]

Violation of (3.2) forces `c=1`, `i=|S|-1`, and `t=2`.  The two free ends
of the induced path are then both used by opposite-bit edges, so there is
no selected edge from `S` to another vertex of `V_(x,epsilon)`.  Hence `S`
is one complete internally bounded run.  Conversely, such a run has
`i=|S|-1,t=2`, and its left side is `3|S|-1`, violating (3.2) by one.  QED.

The theorem is for an integral maximum-degree-two acyclic chronology.  It
does not assert anything about fractional `y`.  Biresidence requires both
values of `epsilon`.

## 4. The exact joint integral gate

The preceding two families can be placed in one exact integral object.
Choose an **ordered** Hamilton path `T`, not merely an undirected edge set,
because the compiler and pinned ports use positions.  Then require:

1. the occurrence matching (2.1), equivalently all cuts (2.2);
2. the desired positive- and zero-run families (3.2);
3. the declared deeper flag witnesses; and
4. the full common compiler `COMP_d(T)`.

For a minimal `q`-window flag architecture, one may introduce a binary
variable `w_P` for every `q`-edge Johnson path `P`, impose

\[
                         w_P\le y_e\quad(e\in P),    \tag{4.1}
\]

and require at least one selected `P` with the prescribed intersection or
union for every target.  Because integral `y` is one Hamilton path, every
selected connected `P` is a consecutive chronology window.  These rows are
exact for the minimal-window architecture.  They are in general stronger
than arbitrary-width upper completeness and are not claimed necessary for
every universal word.

For the compiler, write `T=(T_0,...,T_(M-1))` and put

\[
 P_j=\bigcap_{\max(0,j-d)\le i\le\min(M-1,j)}T_i
 \qquad(0\le j<M+d).                                \tag{4.2}
\]

`COMP_d(T)` asks for nonempty source letters `A_j subseteq P_j` such that

\[
             \bigcup_{j=i}^{i+d}A_j=T_i
             \quad(0\le i<M),                       \tag{4.3}
\]

and every nonempty target below rank `m` is the union of a source interval
of length at most `d`.  Equations (4.2)--(4.3) are exactly `D^dA=T`, with
the clipped endpoint envelopes included.  This is the full common compiler,
not a collection of independent rankwise Hall assignments.

### The `m=5,d=2` specialization

Here `M=252`, `N=210`, and `K=42`.  Thus a joint occurrence matching
selects a `210`-edge/`42`-path Catalan forest and its containing Hamilton
chronology has exactly `41` physical seams.  This count follows from
Theorem 1.1; it does not identify those seams with transparent factor
toggles.

The item 2188 residence-clean fixed matching begins with `21` minimal-depth
debts.  Under a variable rethread or chronology those `21` targets are not
an invariant complete constraint set.  If `c_(q,S)` is the source witness
count and a proposed move removes `r_(q,S)` old witnesses and adds
`a_(q,S)` new witnesses, exact survival is

\[
               c_{q,S}-r_{q,S}+a_{q,S}\ge1           \tag{4.4}
\]

for **every** protected target.  The initial `21` are precisely the rows
with `c_(q,S)=0`; old uniquely covered targets create additional casualty
rows.  Therefore an unrestricted joint model must impose the global flag/
upper rows, or the complete ledger (4.4), rather than service only the
initial debt bank.

The compiler variables act on the final ordered `T`; they do not act on the
selected `210`-edge forest alone.

## 5. Coherent all-six labels

Consider an incidence hexagon with core `H` and three varying letters
`a,b,c`.  At its lower ports write the external insertion labels as
`d_a,d_b,d_c`, and at the upper ports write the external deletion labels as
`e_ab,e_bc,e_ca`.

### Lemma 5.1 (item 2192 coherence test)

Assume one joint decoration marks all six actual port occurrences.  The
hexagon is fixed-decoration transparent if and only if

\[
             d_a=d_b=d_c,qquad e_{ab}=e_{bc}=e_{ca}. \tag{5.1}
\]

The retained-fragment boundary marks then alternate automatically.

#### Proof

The three lower selected colours before and after the toggle are, up to
cyclic order,

\[
 \{H+ab+d_a,H+bc+d_b,H+ca+d_c\},
 \quad
 \{H+ca+d_a,H+ab+d_b,H+bc+d_c\}.                    \tag{5.2}
\]

Every `d` lies outside `H union {a,b,c}`.  If one has unique multiplicity,
it identifies a term in both multisets and would force two distinct pairs
among `ab,bc,ca` to agree.  Hence multiset equality forces all three `d`'s
equal; equality is visibly sufficient.  The identical unique-label
argument inside `H` gives equality of the three `e`'s on the upper shore.
Every reconnected hex edge joins opposite shore types, so boundary
alternation is automatic.  QED.

Such a label is called **coherent**.  Coherence proves only local palette
transparency.  It does not prove component merging, gap-forest acyclicity,
router linkage, residence, deep support, or compiler compatibility.

## 6. Quantifier-correct postrepair catalogue theorem

Work on the exact prepared face H0--H5 of
`MATH_THEOREM_CATALAN_ORDERED_FIXED_D_TRANSPARENT_GLUING_AFTER_ROUTER_20260731.md`:
literal subset superposition, one fixed occurrence-labelled decoration,
component-faithful effects, private/aligned gap effects, one fixed linkage
router, and prefix-closed boundary reachability.

For one joint decoration `D`, let `mathcal C_D` contain exactly the labels
which

1. are genuine component **merges** (their component effects are nonloop
   edges);
2. are coherent in the sense of Lemma 5.1;
3. have all six forced ports selected by `D`; and
4. satisfy the frozen H0--H5 correlated signature relative to this same
   `D`.

Let `K_D` be their labelled component multigraph.  Let `mathcal N` be the
fixed unit vertex-capacitated router with sink bank `Z`.  For a router vertex
set `Y`, retain the labels whose sources still reach `Z` in
`mathcal N-Y`, and call the resulting component graph `K_(D,Y)`.

### Theorem 6.1 (shared-decoration catalogue criterion)

On the prepared face, an ordered component-spanning transparent list exists
if and only if there is one joint decoration `D` such that

\[
 \boxed{
                c(K_{D,Y})\le |Y|+1
                \quad\hbox{for every }Y.}            \tag{6.1}
\]

Here isolated component vertices count in `c(K_(D,Y))`.

#### Proof

For a label set `S`, the linkage-gammoid rank is the exact vertex-Menger
minimum

\[
 r_L(S)=\min_Y\bigl(|Y|+|S\cap T_Y|\bigr),           \tag{6.2}
\]

where `T_Y` is the set of sources still connected to the sink bank after
deleting `Y`.  The graphic--gammoid spanning-tree theorem says that a common
spanning tree exists exactly when, for every partition `Pi` of the
component vertices,

\[
                  r_L(\delta_{K_D}(\Pi))\ge|\Pi|-1.  \tag{6.3}
\]

Substitution of (6.2) turns this into

\[
 |Y|+|\delta_{K_{D,Y}}(\Pi)|\ge|\Pi|-1.              \tag{6.4}
\]

For every graph `G` and `p`-block partition,

\[
                       |\delta_G(\Pi)|\ge p-c(G).    \tag{6.5}
\]

Thus (6.1) implies every row (6.4).  Conversely, take `Pi` to be the
component partition of `K_(D,Y)`; its crossing set is empty, and (6.4)
gives (6.1).  Hence (6.1) is equivalent to a common graphic--gammoid
spanning tree.  H0--H5 make every ordering of that tree an executable
fixed-`D` transparent component-spanning list.  Conversely every executable
list is such a common tree and therefore implies (6.1).  QED.

### Forced-port realization of `D`

For one factor cycle, prescribed ports extend to a joint alternating SDR
exactly when:

1. their forced colours are distinct on each shore;
2. some upper-turn transversal contains every forced upper port;
3. every cyclic gap of that transversal contains at most one forced lower
   port; and
4. after deleting forced gaps and forced lower colours, the residual
   gap--colour graph has a perfect matching.

Necessity follows because alternation chooses exactly one lower occurrence
in every upper-transversal gap.  Conversely, choose every forced lower port
and use the residual matching to fill the remaining gaps.  For a
disconnected factor, take gaps cyclically inside each component, require the
upper transversal to meet every component, and match the union of residual
gaps globally to the residual lower colours.  The same proof applies.

Consequently Theorem 6.1 may equivalently be searched in either of two
forms:

* choose `D` first by forced-port Hall, restrict to `mathcal C_D`, then test
  (6.1); or
* choose one set `S` which is simultaneously a component spanning tree,
  router-linkable, and whose forced ports extend to one decoration `D` by
  the residual gap-Hall test.

It is **not** sufficient that the full catalogue satisfy (6.1) while some
different tree passes forced-port Hall.  For example, on a component
triangle let every router basis contain edge `a`, while forced-port Hall
admits only the tree `{b,c}`.  Each existential statement holds separately,
but no common executable tree exists.

Residual gap Hall supplies the joint SDR.  Private/aligned leaf peelability
and the other H0--H5 rows remain prepared hypotheses; they do not follow
from Hall.

## 7. The precise all-`m` target and the three distinct move classes

The minimal postrepair catalogue lemma is now:

> **Coherent supply lemma.**  Construct one joint decoration `D` for which
> the `D`-admissible catalogue of genuine coherent component-merging labels
> is router-resilient in the sense of (6.1).

For a full carrier theorem the same construction must preserve, or exactly
replace, the physical chronology, run, all-depth flag, endpoint/socket,
voltage, and `COMP_d` state.  Item 2192 proves selection and ordering only
after those correlated hypotheses have been prepared.

Three certificates must remain separate.

1. **Hamilton rethread.**  A toggle changes a Hamilton factor to another
   Hamilton factor; its component effect is a loop and it supplies no edge
   of `K_D`.
2. **Component merge.**  A genuine nonloop component edge belongs to the
   catalogue tested by (6.1).
3. **Physical Johnson seam.**  In Theorem 1.1 the `K-1` unselected edges of
   the final Hamilton chronology join the selected Catalan paths.  This is
   a property of the final ordered carrier, not automatically the same as a
   factor-toggle certificate.

The repaired `ML(7)` cycle has six shared-decoration Hamilton rethreads.
All fifteen component-splitting toggles have zero common componentwise
decoration, already failing the palette row.  They supply no positive merge
edge.  Item 2171's separate standard-factor fixture is the genuine positive
`m=4` component-merge base.

## 8. Exact `m=5` chronology-first obstruction

Let `A` be `answers/k10.word`, whose SHA-256 is

`24b6fc4f4c054e46ef54553ca37eded126150542d51a61256a837d666e0c74fd`.

It has length `254`.  Define

\[
                         T_i=A_i\cup A_{i+1}\cup A_{i+2}
                         \quad(0\le i<252).           \tag{8.1}
\]

### Proposition 8.1

Exact replay proves all of the following.

1. `A` is universal on ten coordinates.
2. `T` lists every rank-five target exactly once and consecutive entries
   are Johnson adjacent, so `T` is a Hamilton path of `J(10,5)`.
3. Every rank-`5-q` intersection and rank-`5+q` union occurs in a minimal
   `(q+1)`-vertex window for `1<=q<=5`.
4. Every internally bounded positive coordinate run has length at least
   three.  This is not biresidence: there are `65` internal zero-runs of
   length one or two.
5. `D^2A=T`, and every nonempty target below rank five is a union of one or
   two consecutive source letters.  Thus `COMP_2(T)` is feasible.
6. Both immediate palettes occur separately, but

\[
                         \nu(G_T)=186<210.            \tag{8.2}
\]

An exact Hall shore is the following `50` lower colours (hexadecimal):

```text
017 01b 03c 04d 053 05a 05c 063 06a 09c
0ac 0b2 0b4 0cc 0e2 12c 134 146 14a 164
168 18a 192 194 198 20b 21c 226 22a 22c
231 232 234 246 24a 251 264 268 270 28a
291 2b0 2e0 303 309 311 321 330 384 388
```

Its complete neighbour set consists of the following `26` upper colours:

```text
07b 0be 0de 0f3 176 17a 19b 1bc 23e 25b
25e 26d 27a 27c 29d 2f1 317 31d 32d 366
36c 371 3b2 3b4 3ca 3cc
```

No chronology occurrence crosses from the displayed lower shore to an
upper colour outside the displayed neighbour set.  The deficiency is
therefore `50-26=24`.  A matching of size `186` and a vertex cover of size
`186` certify equality in (8.2).

The lower degree histogram is

\[
                       1^{170}2^{39}3^1,              \tag{8.3}
\]

and the upper degree histogram is

\[
                       1^{171}2^{37}3^2.              \tag{8.4}
\]

### Corollary 8.2 (scoped edit floor)

Any Hamilton chronology on the same middle layer whose occurrence graph has
a perfect matching must add at least `24` supports absent from `G_T`.  Its
Johnson-edge support symmetric difference from `T` is at least `48`.  Any
sequence of standard incidence-hex toggles needs at least eight toggles.

#### Proof

The displayed lower shore needs at least `50` distinct upper neighbours.
Only `26` are present, so at least `24` new crossing supports are necessary.
A Johnson edge is uniquely determined by its intersection/union pair: if
`U\R={a,b}`, its endpoints are `R+a,R+b`.  Both Hamilton paths have `251`
edges, so adding `24` new supports also removes at least `24`, giving
symmetric difference at least `48`.  A standard incidence hex replaces at
most three chronology supports, so at least `ceil(24/3)=8` are required.
QED.

This is a chronology-specific lower bound, not a no-go for every `m=5`
joint chronology and not a claim that eight toggles suffice.

## 9. Audit and scope

The finite replay is frozen in

* `scratch/audit_thread_a_k10_joint_decoration_hall_counterexample_20260731.py`,
  SHA-256
  `984d30d8b3adcbba6859a5f23ae5a5c7716627b2d938addc6756fab73d91e386`;
* `scratch/thread_a_k10_joint_decoration_hall_counterexample_20260731.audit.json`,
  SHA-256
  `b00d94a2a95d452c656a5663fac4eac991adbb7ae3ce4b76f1b8c581324d4835`;
* canonical payload SHA-256
  `a32ee22340bedc906e91255a46c1d295f048b033c941e50c419548b459cd9503`.

The direct occurrence theorem, cut projection, and residence inequality are
dimension-uniform.  The coherent/router theorem is dimension-uniform only
on the prepared H0--H5 fixed-decoration face.  No theorem here constructs
the required all-`m` coherent catalogue, proves the final physical flag/
compiler rows, or proves `nu(k)=B(k)`.
