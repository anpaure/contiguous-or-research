# Coherent-cycle compiler boundary quotient: exact rank cuts and the minimal compositional state

Date: 2026-08-01  
Lane: R, coherent-birail / terminal compiler  
Status: unconditional finite theorem for a fixed physical chronology and its
legal complete cap states.  It is a terminal quotient theorem, not an
existence proof for a bounded-defect chronology.  For composition with a
later packet, cap records must retain their shared boundary/separator type;
an unlabeled set of rank records is not a universal compositional state.

## 0. Verdict

The coherent `C6/C8` state does not determine the terminal compiler deletion
number.  There is, however, a canonical occurrence-labelled enrichment which
does, and it is strictly smaller than the full target--cell incidence graph.

Fix a set `P` of physical packet cells containing every cell whose legal
target neighbourhood can change under the prepared coherent circuit.  For a
legal complete cap state `theta`, let

* `M_B^theta` be the transversal matroid supplied by all background cells;
* `M_P^theta` be the transversal matroid supplied by the packet cells; and
* for a packet-feasible target set `I`, put

\[
 \kappa_\theta(I)
   =|L\setminus I|-r_{M_B^\theta}(L\setminus I).
                                                               \tag{0.1}
\]

Then

\[
 \boxed{
 \lambda_d(T)=
   \min_{\theta\in\Theta(T)}
   \min_{I\in\mathcal I(M_P^\theta)}\kappa_\theta(I)
   =\min_{\theta\in\Theta(T)}
     \max_{X\subseteq L}
       \bigl(|X|-r_{M_B^\theta}(X)-r_{M_P^\theta}(X)\bigr).}
                                                               \tag{0.2}
\]

The inner maximum is nonnegative because `X=emptyset` is allowed.  It is the
exact Edmonds matroid-union cut, equivalently the Hall/min-cut deficiency of
the fixed-state compiler graph.

Because `kappa_theta` is antitone, the first inner minimum may be restricted
to the bases of `M_P^theta`.  Thus the smallest natural local interface is:

> the packet-basis family together with the background deletion deficiency
> on those bases, kept separately for every legal complete cap state.

This is the promised non-tautological **terminal** quotient.  It forgets the
identities and edges of all background cells and all background matchings.
It retains exactly their rank response to target sets which the fixed local
packet can remove.  If another packet is attached later, the compatibility
relation between background and packet cap states, or a separator label
which makes that relation Cartesian, must also be retained.

## 1. Exact fixed-state setup

Fix a physical chronology `T`, a depth `d`, and one **complete** legal cap
state `theta` in the sense of the corrected CBC theorem: every common-core,
pin, boundary, protected-witness, nonzero-source and shared cap choice has
already been made.  After contracting any prescribed target--cell pins, let

\[
                 H_\theta(T)=(L,C;E_\theta)                 \tag{1.1}
\]

be the residual literal compiler graph.  Its left vertices are the residual
strict-lower target obligations and its right vertices are occurrence-labelled
physical cells.  An absent incidence is a structural zero.

Choose any occurrence-labelled subset `P subseteq C` which contains all
cells declared local to the prepared packet bank, and put

\[
                         B=C\setminus P.                       \tag{1.2}
\]

No assumption that `P` is small is needed for the theorem.  The useful case
is that `P` is the union of the physical supports of one closed `C6/C8`
family.

Define two matroids on the common ground set `L`:

\[
\begin{aligned}
 I\in\mathcal I(M_B^\theta)
   &\Longleftrightarrow H_\theta[I,B]
       \text{ has a matching saturating }I,\\
 I\in\mathcal I(M_P^\theta)
   &\Longleftrightarrow H_\theta[I,P]
       \text{ has a matching saturating }I.
\end{aligned}                                                \tag{1.3}
\]

These are transversal matroids.  Occurrence labels matter: two cells with
the same OR value still have capacity two when they are different physical
occurrences, and capacity one when they are the same occurrence.

On the exact one-core decoder face, no adjacency list has to be stored.  A
position occurrence `p` is represented by its forced core and maximal cap

\[
                         (C_p^\theta,P_p^\theta),              \tag{1.4}
\]

and its residual neighbourhood is exactly

\[
 N_\theta(p)=
   \{S\in L:C_p^\theta\subseteq S\subseteq P_p^\theta\}.      \tag{1.5}
\]

On a guarded face, append to (1.4) only the exact occurrence guard bits that
delete incidences from (1.5).  Hence the minimal *physical* packet record is
the occurrence label plus its core/cap pair and guard-deletion mask.  The
matroid in (1.3) is the canonical lossless compression of those records for
terminal matching.  Merely recording a cap without its core, or an OR value
without the occurrence label, is not lossless.

## 2. Exact packet/background union theorem

### Theorem 2.1 (compiler rank is a matroid-union rank)

For every fixed complete cap state `theta`,

\[
             \nu(H_\theta(T))
                  =r_{M_B^\theta\vee M_P^\theta}(L).          \tag{2.1}
\]

Consequently its exact deletion deficiency is

\[
\begin{aligned}
 \delta_\theta(T)
  &=|L|-\nu(H_\theta(T))\\
  &=\max_{X\subseteq L}
       \bigl(|X|-r_{M_B^\theta}(X)-r_{M_P^\theta}(X)\bigr)\\
  &=\min_{I\in\mathcal I(M_P^\theta)}
       \bigl(|L\setminus I|-r_{M_B^\theta}(L\setminus I)\bigr).
                                                               \tag{2.2}
\end{aligned}
\]

#### Proof

Every matching in `H_theta` splits uniquely into its edges ending in `B`
and its edges ending in `P`.  Their target sets are disjoint independent
sets of `M_B^theta` and `M_P^theta`.  Conversely, match disjoint independent
sets into the two disjoint cell banks and take the union.  This proves
(2.1).

Edmonds' matroid-union rank theorem gives

\[
 r_{M_B^\theta\vee M_P^\theta}(L)
  =\min_{X\subseteq L}
       \bigl(|L\setminus X|+r_{M_B^\theta}(X)
                         +r_{M_P^\theta}(X)\bigr),             \tag{2.3}
\]

which is the second line of (2.2) after subtraction from `|L|`.

Alternatively fix the target set `I` to be served by packet cells.  It must
be independent in `M_P^theta`, and the background can then serve exactly
`r_(M_B^theta)(L\setminus I)` further targets.  Maximizing this total gives
the third line.  \(\square\)

### Corollary 2.2 (only packet bases are needed)

Let `B(M_P^theta)` denote the bases of the packet transversal matroid.  Then

\[
 \delta_\theta(T)
   =\min_{I\in\mathcal B(M_P^\theta)}\kappa_\theta(I).         \tag{2.4}
\]

#### Proof

Matroid nullity `|S|-r(S)` is monotone under inclusion.  Hence, if
`I subseteq J`,

\[
 \kappa_\theta(J)
  =|L\setminus J|-r_B(L\setminus J)
  \le |L\setminus I|-r_B(L\setminus I)
  =\kappa_\theta(I).                                          \tag{2.5}
\]

Extend any packet-independent set to a packet basis.  The objective cannot
increase.  \(\square\)

## 3. The compiler-boundary quotient

For a fixed declared packet-cell bank `P`, define the **compiler boundary
signature** of `T` by

\[
 \mathfrak B_P(T)=
 \left\{
   \left(
     \mathcal B(M_P^\theta),
     \bigl(\kappa_\theta(I)\bigr)_{I\in\mathcal B(M_P^\theta)}
   \right):
       \theta\in\Theta(T)
 \right\}.                                                    \tag{3.1}
\]

Repeated identical records may be deleted for terminal optimization.
Target identities and packet occurrence identities are retained.  Cap
states are not unioned.  If this record is to be composed with another
packet, records with different shared boundary types may not be identified.
If `Theta(T)` is empty, the signature is empty and every minimum over it is
defined to be `+infinity`, in agreement with the absence of a legal common
cap.

The smallest enriched coherent state used here is

\[
                    \widehat\phi_P(T)
                      =\bigl(\phi_{C6/C8}(T),\mathfrak B_P(T)\bigr).
                                                               \tag{3.2}
\]

### Theorem 3.1 (exact quotient and invariance criterion)

The terminal compiler deletion number factors through (3.2), and in fact
through its second coordinate alone:

\[
 \boxed{
 \lambda_d(T)
   =\min_{(\mathcal D,\kappa)\in\mathfrak B_P(T)}
      \min_{I\in\mathcal D}\kappa(I).}                        \tag{3.3}
\]

Therefore two physical chronologies with the same occurrence-labelled
compiler boundary signature have the same `lambda_d`, irrespective of their
different background compiler graphs or background maximum matchings.

#### Proof

For each legal complete cap state apply Corollary 2.2, then minimize over
cap states.  This is exactly the definition of terminal compiler deletion.
\(\square\)

### Corollary 3.2 (correct CBC factorization condition)

On a closed physical coherent-cycle class, `lambda_d` factors through the
bare `C6/C8` state `phi` if and only if the scalar on the right of (3.3) is
constant on every physical fibre of `phi`.  A sufficient, checkable stronger
condition is that `mathfrak B_P(T)` itself is a function of `phi(T)`.

Thus a CBC proof does not need to preserve a full compiler matching through
each circuit.  It is enough to preserve/regenerate the compiler boundary
signature.  Conversely, preserving only whole-chain token margins does not
establish this condition.

### Proposition 3.3 (compatibility-correct compositional form)

Suppose a boundary label `b` contains every shared cap/guard bit through
which a background state and a packet state interact, and conditional on
`b` the admissible pairs form a Cartesian product

\[
 \Theta_B(b)\times\Theta_P(b).
\]

Define

\[
 K_b(I)=\min_{\beta\in\Theta_B(b)}
   \bigl(|L\setminus I|-r_{M_B^\beta}(L\setminus I)\bigr).
                                                               \tag{3.4}
\]

Then the exact composed deficiency is

\[
 \boxed{
 \delta=\min_b\min_{\pi\in\Theta_P(b)}
       \min_{I\in\mathcal I(M_P^\pi)}K_b(I).}                 \tag{3.5}
\]

Without such a separator, replace the Cartesian product in (3.5) by the
literal compatibility relation between background and packet states.  In
particular, two equal pairs `(packet bases,kappa)` with different shared
boundary bits may react differently to a later packet and cannot be merged
in a universal compositional quotient.

#### Proof

For each compatible background--packet state pair apply Theorem 2.1 and
then minimize.  Under the Cartesian separator hypothesis the background
minimum may be taken first, giving (3.4)--(3.5).  The final warning follows
because equality of the numerical rank records does not imply equality of
the set of packet states with which they are compatible.  \(\square\)

## 4. Canonical fixed-state min-cut quotient

There is also a representation which does not choose a packet/background
split and gives a literal finite-capacity network.

For fixed `theta`, partition target vertices into twin classes
`A_1,...,A_s` having identical cell neighbourhoods, and partition cells into
twin classes `D_1,...,D_t` having identical target neighbourhoods.  Put

\[
                  a_i=|A_i|,\qquad b_j=|D_j|.                  \tag{4.1}
\]

Join quotient vertices `A_i,D_j` exactly when their bipartite rectangle is
present.  Build the network

```text
source --(a_i)--> A_i --(|L|)--> D_j --(b_j)--> sink.
```

### Theorem 4.1 (twin-capacity min cut)

The integral maximum flow in this quotient network equals
`nu(H_theta(T))`.  In particular

\[
 \delta_\theta(T)=
   \max_{J\subseteq[s]}
      \left(
       \sum_{i\in J}a_i
       -\sum_{j:N(D_j)\cap\{A_i:i\in J\}\ne\varnothing}b_j
      \right)_+.                                             \tag{4.2}
\]

#### Proof

Between any adjacent twin classes the original graph is complete bipartite.
An original matching therefore induces an integral type flow.  Conversely,
an integral type flow can be expanded class by class to distinct original
vertices because its row and column totals do not exceed `a_i,b_j`.
Integral max-flow/min-cut proves the claim.

For Hall deficiency it suffices to take whole target twin classes: after one
member of a twin class is selected, adding the remaining members increases
the left side without changing its neighbourhood.  This gives (4.2).
\(\square\)

The twin partition is the coarsest vertex partition on which adjacency is
well-defined blockwise.  It can be exponentially smaller than the literal
graph when many physical cells have the same interval core/cap type.  It is
not permitted to merge cells merely because they have the same coherent
token label: their literal target neighbourhoods must agree.

## 5. Why the boundary profile is the minimal compositional datum

The word "minimal" cannot mean the smallest arbitrary statistic determining
one number: the scalar `lambda_d` itself would win tautologically.  The
relevant notion in this section is the rank response needed after the
background state is fixed.  Universal composition additionally needs the
compatibility information in Proposition 3.3.

### Proposition 5.1 (universal necessity of the deletion-rank profile)

Let `M_B` be any background transversal matroid on `L`, and define

\[
                    \kappa_B(I)=|L\setminus I|-r_B(L\setminus I).
                                                               \tag{5.1}
\]

For every `I subseteq L`, attach a packet bank consisting of one private
cell for each target in `I`, with no other packet incidences.  The resulting
compiler deficiency is exactly `kappa_B(I)`.

Consequently any background summary which is required to compose correctly
with every private occurrence packet **inside that fixed cap state** must
determine every value `kappa_B(I)`.  For one fixed packet bank it need only
determine those values on the packet bases, as in (3.1).  This pointwise
necessity does not remove the independent boundary-compatibility datum.

#### Proof

The private packet matroid has independent sets precisely the subsets of
`I`.  Theorem 2.1 gives deficiency

\[
                         \min_{J\subseteq I}\kappa_B(J).
\]

By antitonicity (2.5), the minimum is `kappa_B(I)`.  \(\square\)

Thus (3.1) is not a disguised copy of the full incidence graph.  It is the
exact response vector that any local packet can query, and Proposition 5.1
shows why those queried entries cannot be discarded in a universal theorem.

## 6. Structural zeros and the cap-state warning

The structural-zero ledger has three distinct layers.

1. **Coherent-token zeros.**  The prepared three-label support is
   `K_(3,3)-I=C6`; the strict-rainbow twisted support is a chordless `C8`.
   These zeros govern which whole-chain Markov moves exist.
2. **Occurrence/compiler zeros.**  For fixed `theta`, an incidence is absent
   unless that exact physical cell can literally realize that exact target
   under the fixed core, cap, deadline, pins and protected rows.  These zeros
   define the two transversal matroids in (1.3).
3. **Cap-state disjunctions.**  Incidences belonging to different complete
   cap states are not simultaneous edges.  They must never be united before
   matching.

The last warning is indispensable.  With two targets `r_1,r_2`, two cells,
and two legal cap states, let state zero contain both incidences of `r_1`
and none of `r_2`, while state one contains both incidences of `r_2` and none
of `r_1`.  Every legal graph has deficiency one, but their edgewise union is
`K_(2,2)` and has deficiency zero.  Hence

\[
 \min_\theta\max_X f(\theta,X)
       \ne \max_X\min_\theta f(\theta,X)                       \tag{6.1}
\]

in general, and marginal target degrees or the union graph are unsound.

## 7. Consequence for the coherent `C6/C8` route

Let `P` be the union of the exact physical occurrence supports of a closed
whole-chain `C6` or `C8` atlas.  The corrected CBC implication can now be
strengthened as follows.

### Corollary 7.1 (boundary-state CBC)

Suppose every physical circuit stays in the safe chronology class and its
endpoint compiler boundary signature is computed exactly.  Then terminal
compiler optimization over the reachable Markov component is the finite
optimization

\[
 \min_{T\text{ reachable}}
 \min_{(\mathcal D,\kappa)\in\mathfrak B_P(T)}
 \min_{I\in\mathcal D}\kappa(I).                              \tag{7.1}
\]

At each candidate endpoint, (2.2) is an exact guarded rank-cut certificate:

* a positive value exhibits a violated target cut `X`;
* value zero supplies a packet/background matching decomposition; and
* expanding the two transversal matchings gives a literal target--cell
  matching in one common complete cap state.

No compiler matching must be carried along the Markov walk.  No claim that
the bare coherent state determines `lambda_d` is used.

### Corollary 7.2 (exact circuit-invariance test)

Let `T,T'` be the two endpoints of one physically closed coherent circuit,
and use the same occurrence-labelled declaration of packet cells.  If there
is a bijection between their legal cap-state records which preserves

\[
 \mathcal B(M_P^\theta)
 \quad\text{and}\quad
 \kappa_\theta(I)\ \ (I\in\mathcal B(M_P^\theta)),            \tag{7.2}
\]

then `lambda_d(T)=lambda_d(T')`.  If (7.2) fails, the exact terminal effect
is still given by subtracting the two values of (3.3); no monotonicity is
implied by the signed coherent-chain move alone.

This is the precise invariant which a proposed regenerative `C6/C8` atlas
must preserve.  It is weaker than preserving a named complete matching and
stronger than preserving target degrees or the marginal compiler graph.

## 8. Scope and remaining gate

Proved here:

1. the exact packet/background matroid-union identity;
2. the exact rank-cut and deletion-profile formulas;
3. the canonical twin-capacity min-cut compression;
4. a non-tautological occurrence-labelled quotient determining `lambda_d`;
5. its universal compositional minimality; and
6. the precise cap-state disjunction which must not be relaxed.

Not proved here:

1. that a prepared `C6/C8` physical orbit contains a state with bounded
   boundary deficiency;
2. that the set of legal complete cap states is bounded or regenerative;
3. any global host, upper-witness, residence or owner theorem; or
4. `nu(k)<=B(k)+O(1)`.

The exact remaining positive task is now sharply localizable: construct a
closed packet orbit for which the basis-indexed background response vectors
in (3.1) contain one entry bounded by an absolute constant.
