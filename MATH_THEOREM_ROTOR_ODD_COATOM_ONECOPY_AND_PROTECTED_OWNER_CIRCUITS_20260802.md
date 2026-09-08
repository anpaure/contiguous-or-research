# Odd-central coatom one-copy rounding and protected owner circuits

**Date:** 2026-08-02  
**Status:** unconditional owner/declared-target rounding on the odd-central
coatom face, exact protected extension and exchange criteria, and a sharp
Boolean Hall obstruction outside that face.  This note does not construct
the integral triangular chain factor or a literal Euler chronology.

## 0. Outcome

Let

\[
                   k=2r-1,
 \qquad W={2r-1\choose r-1}={2r-1\choose r}.
\]

Assume `r>=2`.

Suppose an integral residual table has already selected `W` pairwise
target-disjoint nonempty chains, one role per eventual owner, and uses every
rank-`(r-1)` target exactly once.  This is exactly the top-row situation of
the odd-central triangular residual bank whenever the Ferrers boundary does
not consume rank `r-1`.

Then owner repetition is not an additional marginal obstruction:

* every role contains a unique rank-`(r-1)` maximum;
* the central containment graph has a perfect matching from those maxima to
  all rank-`r` owners;
* assigning owners along that matching uses every owner and every already
  selected lower target once; and
* all such assignments are connected by alternating even owner circuits.

Every one prescribed coatom--owner incidence extends.  For a larger
protected matching, the exact residual Hall-damage row is given below.

This result must be used **inside**, not after, chronology selection.  An
owner-circuit flip preserves the target chains but need not preserve literal
state boundary.  Section 4 gives the exact boundary-zero lift condition.
Thus the theorem removes the odd-central owner-colour projection from the
integral rotor gate; the integral bounded-chain factor and the common
predecessor/Euler matching remain load-bearing.

Outside the complete coatom face there is a literal Boolean obstruction.
At `(k,r)=(7,4)`, 21 distinct role maxima containing one fixed coordinate
compete for only 20 owners.  Hence distinct named payloads alone do not
imply one-copy owner rounding.

## 1. Exact coatom forcing in the role table

Let `I` be a set of `W` roles.  Role `i` carries a nonempty strict chain

\[
             C_i=(S_{i,1}\subsetneq\cdots\subsetneq S_{i,\ell_i})
             \quad(1\le \ell_i\le d),                 \tag{1.1}
\]

of proper lower targets, so `1<=|S_(i,j)|<r` for every entry.  The chains
are pairwise disjoint as sets of named targets.  Assume their union contains
every member of `binom([k],r-1)` exactly once.

### Lemma 1.1 (one coatom per role)

Every role contains exactly one rank-`(r-1)` target, and that target is the
maximum of its chain.  Consequently the map

\[
             i\longmapsto q_i:=C_i\cap { [k]\choose r-1}       \tag{1.2}
\]

is a bijection from `I` to `binom([k],r-1)`.

#### Proof

One strict chain contains at most one set of a fixed rank.  There are `W`
roles and exactly `W` rank-`(r-1)` targets.  Exact target use therefore
forces equality in every role.  Since every other member of the chain has
smaller rank, the coatom is its maximum.  \(\square\)

No saturation assumption `sum_i ell_i=dW` is needed.  Complete coatom use
alone forces (1.2).

## 2. The odd-central owner matching

Let `G_r=(L,R;E)` be the containment graph

\[
 L={ [2r-1]\choose r-1},\qquad
 R={ [2r-1]\choose r},\qquad
 qT\in E\Longleftrightarrow q\subset T.               \tag{2.1}
\]

Both shores have size `W`.  Every vertex has degree `r`.

### Theorem 2.1 (exact odd-central coatom owner assignment)

For every table in Lemma 1.1 there is a bijection

\[
                         M:I\longrightarrow R                 \tag{2.2}
\]

such that `q_i subset M(i)` for every role `i`.  Relabelling role `i` by
owner `M(i)` yields one copy of every rank-`r` owner and retains every
declared lower target literally.

#### Proof

For `X subseteq L`, all `r|X|` edges incident with `X` end in `N(X)`, whose
vertices have total degree `r|N(X)|`.  Thus `|N(X)|>=|X|`.  Hall gives a
perfect matching of (2.1).  Use the bijection (1.2) to transfer it to the
roles.  Every member of `C_i` is contained in its maximum `q_i`, hence in
the matched owner.  Role payloads never move between roles, so their exact
target partition is unchanged.  \(\square\)

This proof uses the equality of the two middle ranks.  It is not an
arbitrary-owner version of the fractional pull clock.

### Lemma 2.2 (strict proper-shore expansion)

The graph `G_r` is connected, and every nonempty proper `X subsetneq L`
satisfies

\[
                         |N(X)|\ge |X|+1.                     \tag{2.3}
\]

#### Proof

Johnson adjacency connects the `(r-1)`-sets: if `q,q'` differ by one
exchange, their union is a common rank-`r` neighbour.  Therefore the
bipartite incidence graph is connected.

If equality held in Hall for a nonempty proper `X`, then the `r|X|` edges
from `X` would exhaust all `r|N(X)|` incidences at `N(X)`.  Hence no vertex
of `N(X)` would meet `L-X`, disconnecting `G_r`.  This is impossible.
The strict integer inequality gives (2.3).  \(\square\)

### Corollary 2.3 (one protected incidence is automatic)

Every edge `q_0T_0` of `G_r` lies in a perfect matching.

#### Proof

Delete `q_0,T_0`.  For nonempty `X subseteq L-{q_0}`, Lemma 2.2 gives
`|N_G(X)|>=|X|+1`; deleting `T_0` leaves at least `|X|` neighbours.  Hall
applies.  \(\square\)

There is also a one-component statement at the **incidence** projection.

### Corollary 2.4 (one protected edge in a Hamilton incidence rotor)

For every edge `e` of `G_r`, there is a Hamilton cycle of `G_r` containing
`e`.  Its two alternating edge classes are perfect matchings.  Choosing the
class containing `e` gives an exact owner assignment, while their union is
one alternating coatom--owner cycle.

#### Proof

Middle Levels Hamiltonicity gives one Hamilton cycle in `G_r`.  The action
of the coordinate-symmetric group on `G_r` is edge-transitive, so a ground-
set permutation sends any chosen edge of that cycle to `e` and sends the
whole cycle to another Hamilton cycle.  A bipartite Hamilton cycle splits
into two perfect matchings.  \(\square\)

At depth one this is the moving-core Hamilton rail.  At depth at least two,
the incidence cycle does not by itself transport the lower flag histories;
it is not yet a literal trace Euler component.

For a protected matching `P`, with endpoint shores `L(P),R(P)`, extension
is exact rather than automatic.

### Theorem 2.5 (protected Hall-damage row)

A matching `P` extends to a perfect matching of `G_r` if and only if

\[
 |N_G(X)|-|X|
       \ \ge\ |N_G(X)\cap R(P)|
 \quad\text{for every }X\subseteq L-L(P).             \tag{2.4}
\]

#### Proof

After fixing `P`, the residual graph deletes `L(P)` and `R(P)`.  Its
neighbourhood of `X` has size

\[
 |N_G(X)-R(P)|=|N_G(X)|-|N_G(X)\cap R(P)|.
\]

Hall in the residual graph is exactly (2.4).  \(\square\)

Thus a bounded protected bank is governed by literal expansion damage, not
by the number of pins alone.

## 3. Exact owner-circuit connectivity

### Theorem 3.1 (protected alternating owner circuits)

Let `M` and `M'` be two perfect matchings of `G_r` which both contain a
protected matching `P`.  There is a sequence

\[
                         M=M_0,M_1,\ldots,M_t=M'              \tag{3.1}
\]

in which `M_(j+1)` is obtained from `M_j` by flipping one simple alternating
even circuit, and every circuit is disjoint from `P`.

Every intermediate matching gives an exact one-copy owner assignment to the
same role chains.

#### Proof

The symmetric difference `M triangle M'` is a vertex-disjoint union of
simple even circuits alternating between the two matchings.  No edge of
`P` occurs in the symmetric difference.  Flip the circuits one at a time.
Every flip remains a perfect matching and hence retains one owner per role
and one role per owner.  The target payload is attached to the role, so it
is unchanged.  \(\square\)

This is the exact cycle-space statement available at the owner projection.
It gives no chronology claim by itself.

## 4. Exact lift of an owner circuit to a trace circuit

For role `i` and an admissible owner `T superset q_i`, let `E_i(T)` be its
menu of literal trace arcs carrying the complete fixed chain payload `C_i`
and all protected data.  Suppose a selected one-copy table uses arcs
`e_i in E_i(M(i))`.

Let `Z` be one alternating owner circuit and let `M^Z` be the flipped owner
matching.  Only the roles incident with `Z` change owners.

### Theorem 4.1 (boundary-zero lifted-circuit criterion)

The owner flip on `Z` has a payload-preserving, state-balanced literal lift
with all arcs outside `Z` fixed if and only if there are choices

\[
                   e'_i\in E_i(M^Z(i))\qquad(i\in Z)           \tag{4.1}
\]

such that

\[
                       \sum_{i\in Z}\partial e'_i
                         =\sum_{i\in Z}\partial e_i.           \tag{4.2}
\]

When (4.1)--(4.2) hold, the replacement preserves every owner, every
declared target occurrence, every protected menu row encoded in `E_i`, and
global state balance.

#### Proof

Necessity follows by subtracting the unchanged outside boundary from the
two balanced selections.  Conversely, (4.2) preserves total state boundary;
the flipped matching preserves the owner partition; and membership in the
same role menus preserves every attached payload.  \(\square\)

Component fusion is a further literal condition on the old and new support.
For example, a transparent crossed-head rectangle on two different Euler
components decreases the component count by one.  Equation (4.2) does not
assert that such a rectangle exists.

This theorem explains why owner matching must be chosen jointly with the
age chronology.  Flipping a perfect owner matching after freezing trace
states is unsound unless (4.2) is checked.

## 5. A sharp Boolean Hall obstruction away from the coatom face

For arbitrary role cores `K_i` of rank at most `r-1`, the owner graph is

\[
               i\sim T\quad\Longleftrightarrow\quad K_i\subset T,
               \qquad T\in { [k]\choose r}.                   \tag{5.1}
\]

Its perfect matching condition is ordinary Hall.  Distinct cores do not
make Hall automatic.

### Proposition 5.1 (first coordinate-star obstruction)

At `(k,r)=(7,4)`, there are 21 roles with pairwise distinct nonempty cores
of rank at most three, all containing coordinate `1`, but their owner
neighbourhood has size only 20.

#### Proof

Take the core `{1}`, all six pairs `{1,i}` for `2<=i<=7`, and any fourteen
of the fifteen triples `{1,i,j}` with `2<=i<j<=7`.  These are 21 distinct
cores.  Every rank-four owner containing any of them contains coordinate
`1`, so their joint neighbourhood is contained in

\[
                    \{T\in{[7]\choose4}:1\in T\},
\]

which has size `binom(6,3)=20`.  Hall fails by one.  \(\square\)

Adding arbitrary further roles cannot repair this deficient subset.  The
example may be decorated by additional private lower targets inside each
core, so it is not a collision of named payloads.  It is not the canonical
odd triangular bank: that bank's complete coatom row invokes Theorem 2.1
and removes exactly this obstruction.

More generally, every fixed coordinate set `A` gives the necessary star
row

\[
 \bigl|\{i:A\subseteq K_i\}\bigr|
       \le {k-|A|\choose r-|A|}.                              \tag{5.2}
\]

The full Hall family can be stronger than these principal-star rows.

## 6. Consequence for integral rotor fusion

On the odd-central complete-coatom face, an integral target-chain table
automatically admits an exact one-copy owner assignment with zero added
roles.  Owner assignments have the complete protected alternating-circuit
language of Theorem 3.1.  Therefore a proof of `B(k)+O(1)` on this face
does not need another owner-marginal rounding theorem.

The genuine remaining lower rows are:

1. construct the sharp integral triangular chain table (or a serialized
   substitute) itself;
2. choose the coatom owner matching together with literal age states so the
   lifted boundary equations (4.2) admit a balanced selection;
3. obtain one or `O(1)` Euler components by payload-transparent lifted
   circuits; and
4. if several components remain, bound their exact overlap-reset sidecar,
   not merely their number.

The stationary rational pull clock proves none of items 1--3: it averages
over chain roles, owner labels, and literal states.  Theorem 2.1 removes
only the owner projection **after** item 1, while Theorem 4.1 states the
exact noncircular condition needed to transport that rounding through the
chronology.

Even `k` retains a Catalan-sized set of roles without rank-`(r-1)` maxima,
so the corresponding residual owner Hall system is separate.  No even-
dimension claim is made here.

## 7. Scope

Proved here:

* exact one-copy owner/target rounding from any odd-central complete-coatom
  chain table;
* automatic extension of one protected incidence and the exact general
  protected Hall row;
* protected alternating-circuit connectivity of the owner assignments;
* the exact boundary-zero condition for physically lifting one such
  circuit; and
* a smallest central Boolean star obstruction showing why arbitrary role
  cores do not enjoy the same theorem.

Not proved here:

* the sharp integral triangular chain factor;
* a common integral successor selection;
* bounded Euler components or sidecar;
* residence, upper interval decks, source binding, common-cap/compiler, or
  regeneration; or
* `nu(k)<=B(k)+O(1)`.
