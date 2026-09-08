# Protected Catalan--pivot connectors: the history-aperture law and the first residence obstruction

**Date:** 2026-08-02  
**Lane:** K, protected Catalan--pivot connector / adversarial audit  
**Status:** unconditional source-length and residence theorems, exact
all-width witness-cut criterion, and a sharp separation from the existing
owner/`q1` connector theorem.  No all-dimensional protected Catalan host is
claimed.

## 0. Outcome

The owner-layer problem is already exact.  Relative to a perfect incidence
matching `M_0`, an upper-exact rooted Catalan forest `Q_0` has
`C=Cat_m` directed-path components, and exactly `C-1` compatible free-port
links must form a directed Hamilton path through them.  The split-core
pivot supplies a protected, doubly-`q1`-rainbow, depth-`d` resident path and
the monotone insertion supplies its two compiler rays without upper-deck
damage.

Those facts do **not** yet give a physical depth-`d` source.  A connector
between two owner components must also identify their ordered `d`-letter
source histories.  The exact accounting is as follows.

If component `i` has `n_i` intended owner cells and `g_i` internal
nonowner depth cells, its literal source fragment has length

\[
                         n_i+g_i+d.                    \tag{0.1}
\]

If consecutive fragments overlap in `o_i` equal source letters, their
glued depth row has

\[
 \sum_i n_i+
 \underbrace{\sum_i g_i+
       \sum_i(d-o_i)}_{\text{nonowner/aperture charge}}             \tag{0.2}
\]

cells.  Therefore a `B+1` architecture with `W` owners has the sharp law

\[
              \boxed{\sum_i g_i+\sum_i(d-o_i)=1.}       \tag{0.3}
\]

All but at most one of the Catalan-scale joins must consequently identify a
full ordered `d`-history.  If the unique surplus cell is already assigned
inside a component or at the global boundary, **every** component join must
identify a full `d`-history.  Moreover, in the direct Hamilton-path
architecture the surplus is the controlled global-boundary nonowner, so
every join must be full: an overlap-defect cell at an internal join would
interrupt the two owners which the abstract free-port edge claims are
consecutive.  A Johnson free-port edge does not imply full-history overlap.

There is an independent residence obstruction.  For every `d>=2` there is
an explicit chain of three simple Johnson path components such that

* both immediate palettes on the combined path are injective;
* every component is residence-clean when its endpoint runs are clipped;
* the component connector graph already is the required directed path; but
* the combined path has an internal coordinate run of length exactly `d`,
  and therefore is not depth-`d` resident.

Thus neither upper-tail Hall, Catalan-forest graphic independence, nor a
free-port component path can imply residence.  The exact missing positive
object is a **history-labelled protected connector path**: choose one
physical source realization of every component and one directed free-port
path so that (0.3), the coordinate-run automaton, and the upper-witness
clauses hold simultaneously.

For all-width upper preservation there is a clean sufficient face.  Cut an
already upper-complete source into the intended component fragments and
require every upper target to retain a witness wholly inside one fragment.
Whole-fragment reordering then preserves all those witnesses.  The exact
cut condition is that the cut set not hit every occurrence interval of any
target.  Upper exactness of `Q_0` supplies only width two and does not imply
this occurrence condition.

## 1. Literal depth-`d` fragments

Let

\[
                    A=(A_0,\ldots,A_{n+g+d-1})         \tag{1.1}
\]

be a nonempty set word.  Its depth-`d` row is

\[
 D^d(A)_j=\bigcup_{t=j}^{j+d}A_t,
             \qquad 0\le j<n+g.                       \tag{1.2}
\]

Assume that exactly `n` declared cells in (1.2) are the intended
rank-`r` owner path and the other `g` are declared nonowner or aperture
cells.  Define the ordered left and right histories

\[
 \partial^-_dA=(A_0,\ldots,A_{d-1}),\qquad
 \partial^+_dA=(A_{n+g},\ldots,A_{n+g+d-1}).           \tag{1.3}
\]

For a reversed fragment, reverse the source word before taking (1.3).  The
history consists of literal source letters, not only their total union or
the first/last owner.

Let `A` and `B` be two fragments.  An `o`-overlap, `0<=o<=d`, is legal
when the last `o` source letters of `A` equal the first `o` source letters
of `B` pointwise.  Glue by identifying those positions.  If the source
letters are variables under cap constraints, “equal” means that one common
nonempty `o`-tuple satisfies both occurrence-labelled boundary systems.

For a sequence of fragments, pairwise overlap legality is not the complete
physical condition.  Put `b_1=0` and, when fragment `i` has source length
`n_i+g_i+d`, put

\[
              b_{i+1}=b_i+n_i+g_i+d-o_i.              \tag{1.3a}
\]

Source position `u` of fragment `i` then has global address `b_i+u`.
Call the iterated overlap **globally consistent** when all source letters
assigned to one global address agree and satisfy their common caps, and
when every named occurrence/pin retains its declared global interval
address without an unintended collision.  This is stronger than checking
the two adjacent port records.  If an intervening fragment has
`n_i+g_i<d` (in particular, an uncharged isolate has `n_i=1`), the source
images of nonadjacent fragments overlap through it.  On the full-`d`
overlap face, the exact overlap of fragments `i` and `i+2` is

\[
                  \max\{0,d-(n_{i+1}+g_{i+1})\};       \tag{1.3b}
\]

an uncharged isolate therefore creates a `d-1`-position nonadjacent
overlap.

### Theorem 1.1 (history-overlap accounting)

Let `A^(1),...,A^(s)` be glued in that order with legal overlap lengths
`o_1,...,o_(s-1)` and a globally consistent address quotient.  If fragment
`i` has `n_i` owner cells and `g_i` declared nonowner cells, the glued source
has depth-row length

\[
 \boxed{
 |D^d(A^{(1)}\star\cdots\star A^{(s)})|
   =\sum_{i=1}^s(n_i+g_i)+
        \sum_{i=1}^{s-1}(d-o_i).}                     \tag{1.4}
\]

When every `o_i=d`, the depth row is the literal concatenation of the
fragment depth rows; there is no intervening owner or nonowner cell.
Conversely, a physical gluing of fixed fragments which introduces no new
depth cell at a join must identify all `d` boundary source positions.

#### Proof

Before gluing, the total source length is

\[
                   \sum_i(n_i+g_i+d).
\]

The identifications save `sum_i o_i` physical positions.  Applying `D^d`
subtracts `d` from the resulting source length, giving

\[
 \sum_i(n_i+g_i)+sd-\sum_i o_i-d
 =\sum_i(n_i+g_i)+\sum_i(d-o_i),
\]

which is (1.4).

If `o_i=d`, a window beginning in the first fragment remains one of its
old windows until its last owner; the next window is the first window of
the second fragment because their `d` histories are the same physical
positions.  Hence the rows concatenate exactly.

Conversely, two fixed source fragments of row lengths `a` and `b` have
source lengths `a+d` and `b+d`.  An overlap of `o` gives depth-row length
`a+b+d-o`.  Equality with `a+b` forces `o=d`.  The identified positions
must carry equal literal source letters.  \(\square\)

### Corollary 1.2 (the one-credit aperture law)

Suppose the components carry all `W` owners once and the final source has
`W+1` depth cells.  Then (0.3) holds.  In particular:

1. if `sum_i g_i=1`, every connector has `o_i=d`;
2. if every `g_i=0`, exactly one connector has `o_i=d-1` and every other
   connector has `o_i=d`; and
3. two distinct deficient joins, or one deficient join together with an
   already priced nonowner cell, cannot occur at length `B+1`.

The second case is only a row-length possibility.  A `d-1` overlap creates
one extra depth cell **between** the two component owner blocks.  It does
not realize their abstract free-port edge as a consecutive owner transition
unless an additional owner-preserving bypass theorem is supplied.  Thus the
standard direct certificate, with `W` consecutive owners and one boundary
nonowner, lies on the first case: `sum_i g_i=1` at the boundary and every
`o_i=d`.

This is an equality, not a seam-count heuristic.  It says that a
Catalan-scale connector needs a common ordered-history bank on all but at
most one join.  The unique monotone pivot credit cannot be spent once per
component.

## 2. The history-labelled component connector

Fix `M_0,Q_0`.  Each component of `lambda(Q_0)` is an oriented owner path
with one free incoming and one free outgoing incidence port.  For each
component `K`, let `F(K)` be the menu of literal source fragments whose
owner row is that path and which retain all declared local pivot, palette,
cap and witness pins.

Define the labelled connector relation

\[
 (K,A)\longrightarrow(K',B;o)                         \tag{2.1}
\]

when:

1. the unused outgoing incidence of `K` and incoming incidence of `K'`
   form a legal free-port owner connector;
2. `A in F(K)`, `B in F(K')`, and their boundary source words admit a
   literal `o`-overlap;
3. the new cross-boundary owner cells are precisely the declared aperture
   cells and have their declared ranks; and
4. the occurrence-labelled residence and upper-witness guards exported at
   the boundary are accepted.

Here residence refers to coordinate traces in the **owner/depth row**.  For
short components, pairwise clipped endpoint tests are not sufficient: one
run may pass through several all-one components.  The selected path must
propagate the aggregate capped run state, or equivalently replay the final
owner trace.

### Theorem 2.1 (exact source-compatible connector reduction)

A fixed rooted Catalan forest has a physical component order at depth `d`
with exactly one surplus cell if and only if one can select one fragment
`A_K in F(K)` for every component and a directed Hamilton path through the
selected states such that

\[
             \sum_K g(A_K)+\sum_{e\in E({\cal P})}(d-o(e))=1,       \tag{2.2}
\]

and the complete address quotient is globally consistent and passes the
declared aggregate owner-run, witness, and owner-sequence predicates.  The
last predicate requires every selected
free-port edge to occur between consecutive owner cells; hence any positive
`d-o(e)` needs a separately certified bypass.  On the direct boundary-
nonowner face it simply forces `o(e)=d` on every connector and places the
unique `g=1` cell at the global boundary.
The pivot component may be required first, with its fixed source fragment
and exported right history.

#### Proof

The forward implication restricts the physical source to its consecutive
component owner blocks.  Its unused incidence ports give the free-port
Hamilton order, while its shared source positions give the overlaps in
(2.1).  Theorem 1.1 gives (2.2); the physical word supplies every declared
predicate.

Conversely, glue the selected fragments in the Hamilton order.  Theorem
1.1 and (2.2) give exactly `W+1` depth cells.  The free-port clauses give
the intended owner transitions, and the remaining clauses are literal
tests on the constructed source.  \(\square\)

The theorem is not offered as an all-dimensional existence proof.  Its
point is the strict separation

\[
 \text{upper-exact rooted forest + owner free-port path}
 \not\Longrightarrow
 \text{physical depth-}d\text{ connector}.             \tag{2.3}
\]

The missing correlation already appears in the equality of ordered source
histories, before the terminal compiler is considered.

### Rooted versus unrooted endpoint scope

The reduction above starts with a perfect `M_0`.  If the final short-shore
path omits the rooted link `L->H`, where `H=M_0^{-1}(V)`, its owner
endpoints are `M_0(L)` and `V=M_0(H)`.  Hence the two endpoint containments

\[
                         L\subset M_0(L),\qquad H\subset V             \tag{2.4}
\]

are automatic.  This must not be imported into an unrooted owner-path
construction.  There, if `o` is the unique omitted lower root and `s,t`
the chosen owner endpoints, extension to a perfect predecessor/successor
phase requires

\[
                         o\subset s\quad\hbox{or}\quad o\subset t.     \tag{2.5}
\]

Without (2.5), the owner path can satisfy its degree, rainbow and graphic
rows while admitting no rooted matching phase.  The history/aperture law
does not imply this containment; it is a separate endpoint row on every
unrooted formulation.

## 3. A sharp residence obstruction for every depth

The following construction shows that even an already selected component
path with both immediate palettes injective need not be resident.

Fix `d>=2` and `r>=d`.  Choose a common core `K` of size `r-d`, three
private coordinates `x_1,x_2,x_3`, and four pairwise-disjoint ordered banks

\[
 H_i=(h_{i,1},\ldots,h_{i,d-1}),\qquad0\le i\le3,      \tag{3.1}
\]

all mutually disjoint and disjoint from `K` and the `x_i`.  For
`i=1,2,3` and `0<=j<d`, put

\[
 V_{i,j}=K\cup\{x_i\}\cup
          \{h_{i-1,j+1},\ldots,h_{i-1,d-1}\}\cup
          \{h_{i,1},\ldots,h_{i,j}\}.                 \tag{3.2}
\]

Empty ranges are omitted.

### Theorem 3.1 (three-component residence no-go)

The combined order

\[
 V_{1,0},\ldots,V_{1,d-1},
 V_{2,0},\ldots,V_{2,d-1},
 V_{3,0},\ldots,V_{3,d-1}                              \tag{3.3}
\]

is a simple rank-`r` Johnson path.  Its immediate lower colours are
pairwise distinct and its immediate upper colours are pairwise distinct.
Each of its three displayed component paths is residence-clean under the
usual convention that endpoint runs are clipped.  Nevertheless (3.3) is
not depth-`d` resident: coordinate `x_2` has one internal run of length
exactly `d<d+1`.

#### Proof

Each row of (3.2) has rank

\[
                         |K|+1+(d-1)=r.
\]

Inside component `i`, step `j -> j+1` deletes `h_(i-1,j+1)` and inserts
`h_(i,j+1)`.  At the connector between components `i` and `i+1`, the two
owners are

\[
                  K+x_i+H_i,\qquad K+x_{i+1}+H_i,
\]

so the connector deletes `x_i` and inserts `x_(i+1)`.  Thus (3.3) is a
Johnson path.  Disjoint banks and the private-coordinate signatures make
all owners distinct.

An internal lower colour contains the unique private coordinate `x_i`,
whereas a connector lower colour is `K+H_i` and contains no private
coordinate.  Different components or connector indices are separated by
the disjoint `H_i` banks.  The same argument applies to upper colours:
an internal upper contains one `x_i`, while a connector upper contains the
pair `{x_i,x_(i+1)}`.  Prefix/suffix indices distinguish colours within an
internal class.  Hence both palettes are injective.

Within one component, every `H_(i-1)` coordinate has a prefix run, every
`H_i` coordinate has a suffix run, `x_i` fills the whole component, and
`K` fills it as well.  Every run therefore touches a component endpoint;
the component is clipped-residence-clean.  In the full path, `x_2` occurs
on exactly the `d` owners of the middle component.  It is absent from the
owners immediately before and after that component, so this is an internal
maximal run of length `d`.  Residence requires length at least `d+1`, a
contradiction.  \(\square\)

The component connector is already the directed path `1 -> 2 -> 3` and no
owner/`q1` repair is missing.  The obstruction is solely the omitted
boundary-run state.  It persists if (3.3) is embedded as a protected
contiguous subpath of a larger owner chronology.

## 4. Exact all-width witness preservation under cuts

Let `A` be a cyclic or linear source word which covers a target family
`T`.  For `S in T`, let `W_A(S)` be the set of physical intervals of `A`
whose union is `S`.  Let `E` be a set of cut edges producing source
fragments, and let `int(I)` be the source edges strictly crossed by an
interval `I`.

### Theorem 4.1 (component-internal witness criterion)

The cuts retain an occurrence of `S` wholly inside one fragment if and only
if

\[
             \exists I\in W_A(S):\quad int(I)\cap E=\varnothing.       \tag{4.1}
\]

Consequently every whole-fragment permutation and reversal preserves the
entire target family `T` whenever (4.1) holds for every `S in T` (with the
literal reversal of the chosen interval inside its fragment).

#### Proof

An old interval lies wholly in one cut fragment exactly when it crosses no
cut edge.  Such a physical interval remains contiguous under every
whole-fragment permutation; reversal merely reverses its positions and
does not change its union.  Conversely, an old witness internal to one
fragment crosses no cut.  \(\square\)

Equivalently, `E` must not be a transversal of the occurrence family

\[
                    \{int(I): I\in W_A(S)\}            \tag{4.2}
\]

for any target `S`.  This is the exact protected-cut obstruction.  If it
fails, a new cross-fragment interval may still recreate `S`, but that is a
new repair row and not preservation of the old upper witness.

Immediate-upper exactness of `Q_0` certifies one target at width two for
each rank-`r+1` colour.  It gives no occurrence in (4.1) for a target at a
larger width.  Hence the all-width clause cannot be inferred from the
Catalan forest or its connector path.

## 5. The weakest clean positive hypothesis

The preceding theorems isolate a sufficient protected Catalan--pivot host
statement which is weaker than asking for a robust Hamilton theorem on an
unlabelled owner graph and stronger than the present marginal results.

### Protected history-and-witness connector hypothesis `PHWC(m,d)`

For the fixed split-core pivot collar there exist `M_0,Q_0` and literal
fragment menus such that:

1. `Q_0` is an upper-exact rooted Catalan forest containing the declared
   alternating half of the pivot collar;
2. every required all-width upper target has a designated occurrence
   internal to one selected component fragment;
3. the history-labelled free-port relation (2.1) contains a directed
   Hamilton path beginning with the pivot component, and its complete
   global-address quotient is consistent (including nonadjacent overlaps
   through short components);
4. every internal connector has full `d`-history overlap, the unique
   surplus cell is the declared global-boundary nonowner (or an explicit
   owner-preserving aperture bypass is supplied), and the aggregate final
   owner-coordinate traces have no internal positive run shorter than
   `d+1`; and
5. the sole surplus cell and the two pivot rays have the declared boundary
   and common-cap roles.

### Corollary 5.1 (conditional protected Catalan--pivot connector)

`PHWC(m,d)` yields one physical length-`B+1` depth chronology containing
the pivot-rich collar, all `W` owners, an exact immediate-upper palette,
the designated all-width upper witnesses, and depth-`d` residence.  The
monotone pivot's two local compiler rays and old-deck transport survive.

#### Proof

The rooted Catalan forest and the selected free-port Hamilton path give the
owner/`q1` chronology.  Theorem 2.1 glues the selected source fragments with
the exact one-credit row length.  Item 4 is the literal residence test.
Theorem 4.1 preserves every designated upper witness.  The split-core pivot
theorem supplies its internal owner, palette, residence and ray identities,
and item 5 assigns the remaining boundary/common-cap state.  \(\square\)

The hypothesis is deliberately occurrence-level.  The known fractional
pull-clock/age circulation addresses marginal trace balance, but it does
not supply the integral history-labelled Hamilton path, the cutwise witness
condition, or the common-cap endpoint state.

## 6. Exact remaining lemmas and scope

This audit leaves three, and only three, independent rows before the local
pivot can be promoted to the requested global host.

1. **Protected rooted forest:** choose `M_0,Q_0` jointly, not by separate
   upper-tail Hall, so heads are injective and the rooted links are acyclic.
2. **History-labelled connector expansion:** after the `O(d)` pivot bank is
   fixed, the component relation must have a directed Hamilton path with
   total aperture charge at most one, a globally consistent address
   quotient, and accepted aggregate owner-run state.  Ordinary free-port
   connectivity, pairwise port Hall, or LKK/Ore expansion does not imply
   this.
3. **Internal upper-witness ownership:** choose the forest cuts so that
   (4.1) holds for every required higher upper target, or supply an explicit
   cross-seam repair ledger for the exceptions.

The theorem does not claim a terminal global lower compiler, Pascal
regeneration, a `k=17` word, or `nu(k)<=B(k)+1`.  It proves that the naive
statement “upper-exact Catalan forest plus Catalan connector tree” is
insufficient even before those gates: the exact missing state is the
ordered `d`-history/aperture and occurrence-witness state.
