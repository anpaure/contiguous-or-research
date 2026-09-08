# Pascal closing ports: rectangle calculus, regenerative boxes, and the exact rail obstruction

**Date:** 2026-08-02
**Status:** unconditional occurrence-level composition theorem and exact
Boolean normal form.  The note proves a regenerative fixed-box induction
and a two-copy correction reset under explicit protected-port hypotheses.
It also proves that neither port multiplicity, stationary pull-clock type,
nor a correction bank made only from ordinary same-rail splices can replace
those hypotheses.  Construction of the protected ports inside a canonical
owner/target-exact Hamilton table remains open.  No upper-shadow,
residence, exterior-window, or common-cap/compiler assertion is made.

## 0. Outcome

The closing-port problem has an exact small algebra.

Fix an ordered rail word `w`.  Make a bipartite graph `B_w` whose left
vertices are predecessor-token occurrences ending in `w`, whose right
vertices are roles beginning with `w`, and whose edges are literal legal
predecessor assignments.  A closing port is an edge of `B_w`.

Two child ports splice precisely when they are opposite edges of a
`K_(2,2)` in `B_w`.  The two possible parent ports are the other two edges.
Consequently:

1. an ordinary freeze-after-rectangle splice never changes the ordered
   rail;
2. every sequence of such splices remains in one edge component generated
   by `4`-cycles;
3. a binary hierarchy can finish at rail `w` only if every participating
   leaf exports `w`; and
4. a bounded correction bank of the same kind cannot convert disjoint rail
   languages.

There is also a genuine regenerative positive state.  Suppose a table
exports every port in a complete rectangle `L x R` of `B_w`.  If two child
boxes have sizes `(ell_0,r_0)` and `(ell_1,r_1)`, their splice exports the
two crossed boxes

\[
                   L_0\mathbin\times R_1,
             \qquad L_1\mathbin\times R_0.                 \tag{0.1}
\]

Thus identical boxes reproduce themselves at every binary level.  More
generally, two disjoint copies of a target correction box reset both sides
of an arbitrary compatible box.  One copy can reset only one side.  This is
an exact bounded correction-bank recurrence, not a marginal count.

For Boolean flags the rectangle condition simplifies further.  Let the
common rail have union `W`, let `z_i` be the terminal block of role `i`, and
let `c_i` be the leading block of its selected predecessor.  Delete `W`
from these blocks.  Two ports cross exactly when

\[
 (c_0\setminus W)\mathbin\triangle(c_1\setminus W)
       \subseteq (z_0\setminus W)\cap(z_1\setminus W).       \tag{0.2}
\]

In words, every changed leading coordinate must be hidden in both terminal
blocks.  This gives explicit terminal-cube port boxes in every depth.

There is a sharp target-support cost.  Put `Q_i=W union c_i`.  Compatible
ports with distinct rank-`r` owners satisfy

\[
                         Q_0\cup Q_1\subseteq T_0\cap T_1. \tag{0.2a}
\]

Hence two full rank-`(r-1)` supports must coincide.  A strict globally
q1-simple portal pair is impossible; the positive box must quarantine the
repeated portal support unmarked, or use at least one boundary-deficient
support.  This is why the protected SCD quantifier is load-bearing.

The remaining recursive lemma is no longer a cap-comparison mystery.  It
is the following protected routing statement:

> choose the canonical owner/target-exact child tables so that their
> private-rooted Hamilton certificates expose one common rail and one
> common terminal-cube box (or expose ports connected to that box by a
> uniformly bounded bank of occurrence-distinct `4`-cycle catalysts).

The protected SCD theorem pays no named-target sidecar for a bounded
prescribed portal bank.  It does not put those portals on a Hamilton path,
so the displayed routing assertion remains open.

## 1. The occurrence-labelled port graph

Fix a depth `d>=1`.  A role `i` has fixed head

\[
                 h_i=(A_{i,1},\ldots,A_{i,d}),          \tag{1.1}
\]

owner `T_i`, fixed marked payload, and literal legal predecessor-token
occurrences.  Put

\[
 \lambda_i=(A_{i,1},\ldots,A_{i,d-1}),\qquad
 P_i=T_i\setminus\bigcup_{s=1}^d A_{i,s}.              \tag{1.2}
\]

For a head-token occurrence `j`, write

\[
 h_j=(c_j,\ldots),\qquad
 \rho_j=(\text{last }d-1\text{ blocks of }h_j).         \tag{1.3}
\]

The literal predecessor identity is

\[
 j\longrightarrow i
 \quad\Longleftrightarrow\quad
 \rho_j=\lambda_i,qquad P_i\subseteq c_j\subseteq T_i.
                                                               \tag{1.4}
\]

Occurrences, rather than unlabelled set values, are the vertices.  This is
essential when two unmarked portal occurrences carry the same physical
state.

For a rail word `w`, define the bipartite graph

\[
 X_w=\{j:\rho_j=w\},\qquad
 Y_w=\{i:\lambda_i=w\},                                \tag{1.5}
\]

with edge set given by (1.4); call it `B_w`.  For a fixed table `F`, let
`P_F(w)` be the edges which occur as the distinguished closing edge in at
least one private-rooted Hamilton certificate on the same fixed role
payload.

The phrase "on the same payload" means that alternative certificates may
change predecessor assignments and the postselection frozen support, but
not owners or declared marked targets.

## 2. Exact rectangle calculus

Let two occurrence-disjoint child tables expose ports

\[
                       e_0=j_0i_0,qquad e_1=j_1i_1,     \tag{2.1}
\]

in their common parent alphabet.

### Theorem 2.1 (port splice equals a bipartite square)

The two ports admit the freeze-after-rectangle splice if and only if they
lie on the same rail `w` and

\[
                       j_0i_1,qquad j_1i_0             \tag{2.2}
\]

are edges of `B_w`.  Equivalently, (2.1) are one diagonal of an
occurrence-labelled `K_(2,2)`.  After the splice, the parent can export
either edge in (2.2), according to which crossed role is left unfrozen.

Every owner and every declared marked target is unchanged.

#### Proof

The two old ports are selected closing assignments.  The
freeze-after-rectangle theorem says exactly that both crossed assignments
in (2.2) must be literal.  Formula (1.4) makes this possible only in one
rail fibre and is also sufficient.  Crossing the two closing arcs merges
the two child cycles.  Freezing one crossed role leaves the other crossed
edge as the parent port.  Role payloads are fixed independently of the
chosen predecessor, so all owners and marked targets persist. \(\square\)

### Corollary 2.2 (rail intersection is hereditary)

For every ordinary binary splice,

\[
 \operatorname{Rail}(F_0\star F_1)
       \subseteq
 \operatorname{Rail}(F_0)\cap\operatorname{Rail}(F_1). \tag{2.3}
\]

More generally, if a binary hierarchy made only from Theorem 2.1 exports
rail `w` at its root, every leaf used by that hierarchy exported `w`.
Adding any number of ordinary correction leaves cannot bridge two principal
children with disjoint rail languages.

#### Proof

Theorem 2.1 requires the two input rails to equal `w`, and each output edge
still belongs to `B_w`.  Induct up or down the binary hierarchy. \(\square\)

Thus a correction macro which truly changes a rail must be a new nonlocal
operation.  It cannot be assembled from same-rail rectangles while hiding
the intermediate rail state.

### Definition 2.3 (the `C4` edge complex)

Let `Q_w` be the hypergraph whose vertices are the edges of `B_w` and whose
four-element hyperedges are the edge sets of its occurrence-labelled
`K_(2,2)` subgraphs.  Call its connected components the **rectangle
components** of `B_w`.  Here `B_w` is the complete fixed ambient graph for
the Pascal node under consideration; passing to a larger ambient table can
add squares and must be audited afresh.

### Proposition 2.4 (correction-bank component invariant)

Every port produced from an active port by ordinary rectangle splices lies
in the same rectangle component of `Q_w`.

#### Proof

A splice replaces one diagonal of a square by the other, so all four old
and new edges lie in one hyperedge of `Q_w`.  This proves invariance.
\(\square\)

The converse is false without a stronger lineage hypothesis.  A static
walk in `Q_w` may ask to reuse a token or role already consumed inside the
parent, whereas the next binary splice can access only the currently
exported edge and a fresh child port.  Thus rectangle-component membership
is necessary, not sufficient.  A proof-grade correction bank must list the
fresh occurrence-disjoint catalyst at every step and replay the actual
crossed output.  The rectangular-box recurrence below is one sufficient
way to do so.  Reusing one physical set value does not provide two catalyst
occurrences.

## 3. Regenerative rectangular boxes

### Definition 3.1 (box-ported table)

Let `L subseteq X_w` and `R subseteq Y_w`, with `L x R` complete in
`B_w`.  A table `F` is **`(w;L,R)`-ported** when

\[
                         L\times R\subseteq P_F(w).     \tag{3.1}
\]

Thus every edge of the box is the closing port of some private-rooted
certificate on the same payload.  The definition is stronger than merely
having all those legal edges.

### Lemma 3.1a (sandwich-box equivalence)

For nonempty `L subseteq X_w` and `R subseteq Y_w`, put

\[
 P_R^\vee=\bigcup_{i\in R}P_i,\qquad
 T_R^\wedge=\bigcap_{i\in R}T_i,\qquad
 C_L^\wedge=\bigcap_{j\in L}c_j,\qquad
 C_L^\vee=\bigcup_{j\in L}c_j.                         \tag{3.1a}
\]

Then `L x R` is complete in `B_w` if and only if

\[
                 P_R^\vee\subseteq C_L^\wedge,
        \qquad  C_L^\vee\subseteq T_R^\wedge.          \tag{3.1b}
\]

#### Proof

Completeness says `P_i subseteq c_j subseteq T_i` for every pair
`(j,i)`.  Intersecting the first family over `j` and then uniting over `i`
gives the first sandwich; uniting the second over `j` and intersecting over
`i` gives the second.  Both operations reverse directly. \(\square\)

Thus box verification is four aggregate set operations, not a quadratic
pair audit.  This is an exact equivalence only after the literal common
rail has been fixed.

### Theorem 3.2 (cross-product recurrence)

Let `F_0,F_1` be occurrence-disjoint box-ported tables with boxes
`L_0 x R_0` and `L_1 x R_1` on the same rail.  Suppose the ambient parent
graph is complete on

\[
 (L_0\cup L_1)\times(R_0\cup R_1).                    \tag{3.2}
\]

Then their splice exports both boxes

\[
                         L_0\times R_1,qquad
                         L_1\times R_0.                \tag{3.3}
\]

If their sizes are `(ell_0,r_0)` and `(ell_1,r_1)`, the parent therefore
exports a regenerative box of size at least

\[
                 \max\{\ell_0r_1,\ell_1r_0\}.          \tag{3.4}
\]

It has all child owners and targets exactly once whenever those payloads
were disjoint and exact.

#### Proof

Fix `j_0 in L_0` and `i_1 in R_1`.  Choose any `i_0 in R_0` and
`j_1 in L_1`.  The child tables have private-rooted certificates closing at
`j_0i_0` and `j_1i_1`.  Completeness (3.2) supplies the crossed edges, and
Theorem 2.1, freezing the `R_0` crossed role, leaves `j_0i_1` as the parent
port.  This gives the first box; reverse the frozen side for the second.
Payload exactness is inherited role by role. \(\square\)

### Corollary 3.3 (infinite fixed-box family)

If both children at every node export occurrence-disjoint copies of one
nonempty box type `(w;L,R)`, and the parent embeddings identify either
crossed box in (3.3) as a fresh copy of that same literal incidence type,
then every level exports the type again.  Arbitrarily many children fuse
into one private-rooted Hamilton table with no lower sidecar.

This is a genuine infinite composition theorem.  Its hypothesis is a
literal protected-box hypothesis, not a stationary-type or marginal-degree
hypothesis.

### Theorem 3.4 (two-copy correction reset)

Let an active table export `L x R`, and let two occurrence-disjoint
correction tables each export a target box `L_* x R_*`, all on one rail.
Assume every cross incidence used below is present.  Then two successive
splices export `L_* x R_*`:

\[
 (L\times R)\star(L_*\times R_*)
       \supseteq L\times R_*;qquad
 (L\times R_*)\star(L_*\times R_*)
       \supseteq L_*\times R_*.                       \tag{3.5}
\]

In the nondegenerate disjoint-bank setting, one correction copy cannot in
general reset both coordinates: every output edge takes its left endpoint
from one input table and its right endpoint from the other.

#### Proof

Both inclusions are Theorem 3.2 with the indicated choice of crossed box.
For the last statement, a single splice outputs only the two mixed boxes in
(3.3), never the old unmixed correction box. \(\square\)

Hence a two-copy box is a literal bounded correction bank.  Regeneration
requires two fresh copies at the next level, or a parent construction which
recreates them as part of its payload partition.

## 4. Exact Boolean terminal normal form

Fix a rail

\[
                         w=(A_1,\ldots,A_{d-1}),qquad
                         W=\bigcup_{s=1}^{d-1}A_s.      \tag{4.1}
\]

Let a role `i` have terminal block `z_i=A_(i,d)` and selected predecessor
leading block `c_i`.  Since its selected full trace has owner `T_i`,

\[
                         T_i=W\cup z_i\cup c_i,qquad
                         P_i=(c_i\setminus W)\setminus z_i. \tag{4.2}
\]

Write

\[
                         \bar c=c\setminus W,qquad
                         \bar z_i=z_i\setminus W.       \tag{4.3}
\]

### Lemma 4.1 (one-role terminal cube)

A predecessor occurrence ending in `w` and having leading block `c` is
legal for role `i` if and only if

\[
                         \bar c\mathbin\triangle\bar c_i
                              \subseteq\bar z_i.        \tag{4.4}
\]

#### Proof

By (1.4), legality is

\[
 \bar c_i\setminus\bar z_i\subseteq\bar c
       \subseteq\bar c_i\cup\bar z_i.                 \tag{4.5}
\]

The left inclusion says `bar c_i - bar c subseteq bar z_i`; the right says
`bar c - bar c_i subseteq bar z_i`.  Together they are (4.4). \(\square\)

### Theorem 4.2 (two-port hidden-difference criterion)

Two selected ports with common rail cross if and only if

\[
 (\bar c_0\mathbin\triangle\bar c_1)
                         \subseteq\bar z_0\cap\bar z_1. \tag{4.6}
\]

#### Proof

The first crossed assignment is legal exactly when the symmetric
difference is contained in `bar z_0`, by Lemma 4.1.  The other is legal
exactly when it is contained in `bar z_1`. \(\square\)

This is the literal cap equation sought by the two-child recursion.  The
terminal blocks, rather than marginal interval sizes, carry the changed
leading coordinates.

### Corollary 4.3 (terminal-cube boxes)

Fix a leading block `c`, a set `H`, and a family of roles `R` with common
rail, selected leading block `c`, and

\[
                         H\subseteq\bigcap_{i\in R}(z_i\setminus W).
                                                               \tag{4.7}
\]

For every `D subseteq H`, suppose there is a predecessor-token occurrence
ending in `w` whose leading block `c_D` satisfies

\[
                         c_D\setminus W=(c\setminus W)\triangle D. \tag{4.8}
\]

Then these tokens and roles form a complete box in `B_w`.  Restricting to
any rank-legal subfamily of the `c_D` remains complete.  The role owners

\[
                         T_i=W\cup c\cup z_i             \tag{4.9}
\]

are pairwise distinct whenever the sets on the right of (4.9) are.

In particular one common hidden coordinate gives a `K_(2,|R|)` box in
every depth, and a common fixed `(w,c)` socket gives a one-port
regenerative state with automatic mutual cap containment.

#### Proof

Equations (4.7)--(4.8) make (4.4) true for every token-role pair.  Equation
(4.9) is (4.2), and its last assertion is immediate. \(\square\)

The construction is not a claim that all these token occurrences and roles
already lie on private-rooted Hamilton certificates.  It closes the local
Boolean incidence problem exactly.

### Theorem 4.4 (cap-aperture law)

Let `R` be a nonempty family of roles on one rail, with selected anchor
leading blocks `c_i`, and put

\[
                         H_R=\bigcap_{i\in R}(z_i\setminus W). \tag{4.10}
\]

A nonempty token family `L` forms a complete box `L x R` if and only if
there is one base token `j_* in L` such that

\[
 \overline c_{j_*}\triangle\overline c_i
          \subseteq\overline z_i\quad(i\in R),          \tag{4.11}
\]

and every `j in L` satisfies

\[
 \overline c_j\triangle\overline c_{j_*}
          \subseteq H_R.                                \tag{4.12}
\]

Consequently all leading labels in one complete box lie in a single
Boolean aperture of dimension at most `|H_R|`; in particular

\[
 \bigl|\{c_j\setminus W:j\in L\}\bigr|\le 2^{|H_R|}.   \tag{4.13}
\]

#### Proof

If the box is complete, Lemma 4.1 gives (4.11).  For any `j in L` and any
role `i`, both `bar c_j` and `bar c_(j_*)` differ from `bar c_i` only inside
`bar z_i`.  Their symmetric difference is therefore contained in every
`bar z_i`, proving (4.12).

Conversely, (4.11)--(4.12) imply, for every `i,j`,

\[
 \overline c_j\triangle\overline c_i
 \subseteq
 (\overline c_j\triangle\overline c_{j_*})
 \cup
 (\overline c_{j_*}\triangle\overline c_i)
 \subseteq\overline z_i.
\]

Lemma 4.1 makes every token-role pair legal.  Bound (4.13) is the size of
the Boolean cube on `H_R`. \(\square\)

The aperture theorem is sharp: Corollary 4.3 realizes the whole cube when
the corresponding token occurrences exist.  It also quantifies the
precise terminal diversity a regenerative correction box must retain.

### Theorem 4.5 (owner/q1 terminal-aperture law)

For two selected compatible ports, define their predecessor support values

\[
                         Q_\epsilon=W\cup c_\epsilon
                         \qquad(\epsilon=0,1).          \tag{4.14}
\]

Then

\[
                         Q_0\cup Q_1\subseteq T_0\cap T_1. \tag{4.15}
\]

Suppose `T_0,T_1` are distinct rank-`r` owners and
`|Q_epsilon|<=r-1`.  Put

\[
                         e_\epsilon=(r-1)-|Q_\epsilon|. \tag{4.16}
\]

The exact support difference obeys

\[
                         |Q_0\triangle Q_1|
                                \le e_0+e_1.            \tag{4.17}
\]

In particular, if both supports have rank `r-1`, then

\[
                         Q_0=Q_1=T_0\cap T_1.           \tag{4.18}
\]

Thus two distinct, globally one-copy q1 labels cannot be the two strict
ports of a nondegenerate splice.  Distinct support values require total
defect at least one, and this lower bound is sharp.

#### Proof

The common rail union `W` is contained in both role heads and hence in both
owners.  Old legality puts `c_epsilon` in `T_epsilon`; crossed legality puts
`c_(1-epsilon)` in `T_epsilon`.  Therefore both owners contain
`W union c_0 union c_1`, proving (4.15).

Distinct rank-`r` sets intersect in at most `r-1` points.  Hence

\[
 \begin{aligned}
 |Q_0\triangle Q_1|
 &=2|Q_0\cup Q_1|-|Q_0|-|Q_1|\\
 &\le2(r-1)-[(r-1-e_0)+(r-1-e_1)]\\
 &=e_0+e_1.
 \end{aligned}                                          \tag{4.19}
\]

When both defects vanish, two rank-`(r-1)` sets have union of size at most
`r-1`, so they coincide; (4.15) then forces (4.18).

For sharpness, take `|W|=r-3`, choose distinct points `a,b,x,y` outside
`W`, and put

\[
 \begin{array}{c|c|c|c}
 &c_\epsilon&z_\epsilon&T_\epsilon\\ \hline
 0&\{b\}&\{a,x\}&W\cup\{a,b,x\}\\
 1&\{a,b\}&\{a,y\}&W\cup\{a,b,y\}.
 \end{array}                                            \tag{4.20}
\]

Both mandatory parts equal `{b}`, so both crossed assignments are legal.
Here `Q_0=W+b` has defect one, `Q_1=W+a+b` has defect zero, and their
symmetric difference has size one. \(\square\)

Theorem 4.5 does not invalidate the terminal-cube box.  It says that a box
with repeated full q1 support cannot mark every portal occurrence as a new
one-copy q1 target.  The protected SCD construction uses precisely the
allowed escape: keep the bounded portal suffixes unmarked and route those
named targets through unprotected roots.  Alternatively, (4.20) supplies
the smallest boundary-deficient aperture.

## 5. What the SCD and long-run inputs do and do not supply

The protected SCD theorem accepts arbitrary prescribed flags at at most
`m+1` distinct roots while routing every named high target through the
unprotected roots.  Therefore a bounded terminal-cube bank can be planted
at the **static** owner/target layer with its suffixes unmarked.  If some
portal targets are marked instead, their occurrence labels must be
injective, exactly as in the protected SCD theorem.

This does not imply that the prescribed token-role incidences occur on one
Hamilton selector.  In the notation above, the still-missing assertion is

\[
                 L\times R\subseteq P_F(w),             \tag{5.1}
\]

not merely `L x R subseteq E(B_w)`.  The known arbitrary-protected-owner
counterexample prevents replacing (5.1) by a post-hoc extension claim.

Likewise, the long-run Middle Levels flip-gap theorem controls distances
between repeated coordinate flips.  It proves residence once a Hamilton
cycle has been chosen.  It does not force equality of two literal ordered
rails, and it does not force the hidden-difference condition (4.6).  Thus a
long-run cycle is compatible with the present theorem only after one proves
that the protected terminal-cube ports lie on that cycle, or after a
bounded rethread preserving its flip-gap guards.

## 6. Sharp count-only obstruction

No number of same-type ports on a common rail forces even one compatible
pair.

### Proposition 6.1 (arbitrarily large incompatible families)

For every `s>=1` and every `d>=2`, there are two families of `s` literal
Boolean ports such that

1. all `2s` ports have the same ordered rail and the same block-size type;
2. their predecessor tokens, role heads, and owners are pairwise distinct;
3. every port is individually legal; and
4. no port in the first family crosses a port in the second.

#### Construction and proof

Take a nonempty common rail with union `W`, and choose distinct coordinates

\[
 x,y,u_i,a_i,v_i,b_i\qquad(1\le i\le s)               \tag{6.1}
\]

outside `W`.  In the first family put

\[
 c_i=\{x,u_i\},\qquad z_i=\{u_i,a_i\},qquad
 T_i=W\cup\{x,u_i,a_i\}.                              \tag{6.2}
\]

In the second put

\[
 c'_i=\{y,v_i\},\qquad z'_i=\{v_i,b_i\},\qquad
 T'_i=W\cup\{y,v_i,b_i\}.                            \tag{6.3}
\]

The mandatory parts are `P_i={x}` and `P'_i={y}`, so every displayed old
port is legal.  But no `c'_j` contains `x`, and no `c_i` contains `y`.
Hence neither crossed assignment exists.  The private coordinates make all
tokens, heads, and owners distinct, while the displayed block sizes agree.
\(\square\)

This rules out a regenerative theorem based only on port count, cell-rank
type, stationary pull-clock mass, or unordered Boolean degree.  It also
shows why a bounded correction bank must be certified in the rectangle
complex rather than counted abstractly.

At the strict `(k,d)=(5,2)` all-high boundary, owner exactness freezes every
realized predecessor list and gives two directed `5`-cycles.  In the present
language the available closing edges have no payload-preserving rectangle
route which merges those cycles.  The terminal-cube construction escapes
that boundary only by using protected unmarked/non-all-high portal roles or
a contracted macro, exactly as required by the earlier audit.

## 7. Exact recursive interface

The smallest proof-safe same-parity lemma is now one of the following
equivalent-strength constructive interfaces.

> **Protected terminal-box host lemma `PTBH(d)`.**  At every sufficiently
> large same-parity Pascal node there is a static one-copy owner/target
> table and a bounded occurrence bank `(w;L,R)` such that
>
> 1. `L x R` satisfies the sandwich equations (3.1b), with its Boolean
>    aperture certified by (4.11)--(4.12);
> 2. every edge of `L x R` is the closing port of a private-rooted Hamilton
>    certificate on the same payload, i.e.
>    `L x R subseteq P_F(w)`;
> 3. the two Pascal child embeddings make all cross incidences in (3.2)
>    literal and payload-transparent; and
> 4. one crossed output box is a fresh copy of the same state in the next
>    dimension, or reaches it through a uniformly bounded bank of fresh
>    catalysts in one rectangle component.

Theorem 3.2 proves that `PTBH(d)` is closed under the lower
owner/target/topology composition.  Conversely, within the ordinary
freeze-after-rectangle architecture, Corollary 2.2 and Proposition 2.4
show that items 1--4 cannot be replaced by a port-count hypothesis: a
successful recursion must preserve a common rail and a reachable rectangle
component.

### Fixed-box form

For every sufficiently large child, construct an owner/target-exact static
table and a private-rooted Hamilton selector which is `(w;L,R)`-ported for
one literal box preserved by the two Pascal embeddings.  Corollary 3.3 then
gives an infinite same-parity induction.

### Bounded-reset form

Construct one port in a fixed rectangle component and at most `b`
occurrence-distinct protected catalysts, uniformly in the dimension, whose
literal serial replay reaches a regenerated box.  Rectangle-component
membership is only a necessary filter.  The case `b=2` is supplied by
Theorem 3.4 once two copies of a complete correction box are physically
routed.

### Terminal-cube form

Use Corollary 4.3 to plant a common rail and hidden terminal cube, then prove
that its prescribed incidences extend to the required private-rooted
Hamilton certificates.  The static named-target cost of a bounded bank is
already removed by protected SCD selection.  The unresolved correlation is
the protected Hamilton/path extension, not local Boolean cap feasibility.

These interfaces retain one copy of every owner and declared target because
all rectangle operations change only predecessor assignments.  They do not
assert any of the following additional rows:

1. arbitrary-width upper interval-union coverage;
2. residence or preservation of flip gaps after protected rethreading;
3. exterior opening, quotient voltage, or one-component ambient topology
   beyond the lower predecessor selector; or
4. terminal common-cap/compiler feasibility.

## 8. Internal proof audit

The arguments above use only the literal predecessor identity (1.4) and the
freeze-after-rectangle splice.  The following checks are independent of
any finite census.

1. **Square direction.**  Old diagonal `j_0i_0,j_1i_1` is replaced by
   `j_0i_1,j_1i_0`; no old edge is silently retained as the new closing
   edge.
2. **Rail scope.**  Equality is of ordered set-valued words, not their rank
   profiles or new-coordinate signatures.
3. **Terminal algebra.**  Removing `W` from
   `P_i subseteq c subseteq T_i` gives (4.5), whose two set differences are
   exactly the symmetric difference in (4.4).
4. **Payload scope.**  Owners and marks belong to roles, so predecessor
   switches preserve them.  A correction table still consumes its own
   disjoint owner payload; it is not a free extra occurrence.
5. **Privacy scope.**  Box edges are legal physical options.  Singleton-tail
   privacy is imposed only after a particular crossed selection is made,
   exactly as in the freeze-after-rectangle theorem.
6. **No marginal inference.**  Proposition 6.1 has arbitrary port
   multiplicity and identical size profiles but no cross edge.

Accordingly the theorem is an exact lower owner/target/topology interface,
not a full source-word construction.
