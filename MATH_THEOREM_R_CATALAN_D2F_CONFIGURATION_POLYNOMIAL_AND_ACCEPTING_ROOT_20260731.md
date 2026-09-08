# D2F configuration polynomials and the exact accepting-root induction

Date: 2026-07-31  
Status: exact all-dimension relational theorem for the corrected decorated
2-factor target; exact comparison with transparent hex transfer; no proof
that the accepting root is nonempty for every dimension

## 0. Verdict

The corrected decorated-2-factor target admits an exact componentwise
induction.  No Hamilton order or component-merging state is needed.

For each factor component, enumerate its locally forest-safe marked
configurations and its two unmarked cross phases.  Record only the upper and
lower turn-colour sets consumed.  Multiplication over components, with
squarefree colour variables, composes these local choices exactly.  The
coefficient of the monomial containing every upper and every lower colour
once is positive if and only if the factor supports an accepting decoration
whose induced lift is a Catalan path forest.

This gives a literal accepting-root relation, not an existence proof.  The
remaining all-dimension lemma is positivity of that one coefficient for one
explicit recursively generated factor family.

## 1. Local accepting configurations

Fix `m>=2`, `Omega=[2m-1]`, and a spanning 2-factor `F` of `ML(2m-1)`.
Write

\[
 \mathcal U=\binom\Omega{m+1},\qquad
 \mathcal L=\binom\Omega{m-2},\qquad
 P=|\mathcal U|=|\mathcal L|.                       \tag{1.1}
\]

For one factor component `C`, a **local accepting configuration** is one of
the following.

1. An unmarked configuration: no turn occurrence is selected, and one of
   the two alternating residual factor-edge phases is chosen.
2. A marked configuration: positive, equal numbers of selected `A`- and
   `B`-occurrences alternate cyclically by shore, including across the
   wrap-around; their selected upper colours are pairwise distinct, their
   selected lower colours are pairwise distinct, at least one occurrence of
   `C` is unmarked, and the mixed binary trace is off the exceptional cycle
   face.  In particular a singleton mark is not a cyclic alternation.

For a configuration `sigma`, let

\[
 U(\sigma)\subseteq\mathcal U,qquad
 L(\sigma)\subseteq\mathcal L                       \tag{1.2}
\]

be its consumed turn-colour sets.  Cyclic alternation gives

\[
                         |U(\sigma)|=|L(\sigma)|.     \tag{1.3}
\]

Both unmarked phases have `U=L=empty` and differ only in their literal cross
edges.

## 2. The exact configuration polynomial

Introduce commuting variables `x_U` for `U in mathcal U` and `y_L` for
`L in mathcal L`.  Define

\[
 P_C(\mathbf x,\mathbf y)=
   \sum_{\sigma\in\mathscr A(C)}
       \prod_{U\in U(\sigma)}x_U
       \prod_{L\in L(\sigma)}y_L,                   \tag{2.1}
\]

where `mathscr A(C)` is the local accepting set.  The constant coefficient
is two, one for each unmarked phase.  Put

\[
                       P_F=\prod_{C\in\operatorname{comp}(F)}P_C. \tag{2.2}
\]

Finally let

\[
              \mathfrak m_*=prod_{U\in\mathcal U}x_U
                              \prod_{L\in\mathcal L}y_L.          \tag{2.3}
\]

### Theorem 2.1 (target-coefficient equivalence)

The factor `F` supports a corrected componentwise Catalan decoration whose
physical lift is a `Cat_m`-path forest if and only if

\[
                           [\mathfrak m_*]P_F>0.       \tag{2.4}
\]

The coefficient counts the accepting componentwise decorations, including
the independent unmarked residual phases.

#### Proof

Expanding (2.2) chooses one local accepting configuration on every factor
component.  A contribution to the squarefree monomial (2.3) uses every
upper and lower colour exactly once: omission misses a variable, while a
repeat creates exponent at least two.  Thus a contributing term is exactly
a globally bijective pair of turn transversals with componentwise
alternation, no wholly marked component, and no exceptional partial trace.

Conversely, every corrected componentwise decoration restricts to one term
of every `P_C`; global colour bijectivity makes their product exactly
`mathfrak m_*`.  The corrected decorated-2-factor theorem then gives the
`Cat_m`-path forest.  Literal phase choices are distinct constant terms, so
the ordinary integer coefficient counts them.  \(\square\)

For existence alone one may evaluate coefficients in the Boolean semiring,
replacing positive coefficients by `1`, while retaining ordinary monomial
exponents.  The variables themselves must not be made idempotent:
`x_U^2` must remain distinguishable from `x_U`, or a repeated colour would
be accepted unsoundly.  With that convention the equivalence is unchanged.

## 3. Exact relation and accepting-root recurrence

Let the factor components be the leaves of any rooted binary composition
tree.  At a node `v`, define

\[
 \mathcal R_v\subseteq2^{\mathcal U}\times2^{\mathcal L} \tag{3.1}
\]

to consist of the colour pairs consumed by some accepting choice on all
leaves below `v`, with no colour repeated.  At a component leaf,

\[
 \mathcal R_C=\{(U(\sigma),L(\sigma)):
                         \sigma\in\mathscr A(C)\}.    \tag{3.2}
\]

For children `a,b`, use the disjoint-union join

\[
 \mathcal R_v=
 \left\{(U_a\mathbin{\dot\cup}U_b,
          L_a\mathbin{\dot\cup}L_b):
 \begin{array}{l}
 (U_a,L_a)\in\mathcal R_a, (U_b,L_b)\in\mathcal R_b,\cr
 U_a\cap U_b=L_a\cap L_b=\varnothing
 \end{array}\right\}.                               \tag{3.3}
\]

### Theorem 3.1 (exact accepting-root induction)

The recurrence (3.2)--(3.3) is independent of the binary bracketing, and

\[
             (\mathcal U,\mathcal L)\in\mathcal R_{\rm root} \tag{3.4}
\]

if and only if `F` supports an accepting decorated 2-factor certificate.

#### Proof

The join is simply multiplication of squarefree monomial supports in (2.2).
Disjoint union is associative and commutative, so bracketing is irrelevant.
The root pair in (3.4) is precisely the target monomial (2.3), and Theorem
2.1 applies.  \(\square\)

This is the exact relational induction requested by the weaker central
target.  Its state can be exponentially large; no bounded-adhesion claim is
hidden in the theorem.

It is also a fixed-factor, fixed-component-partition relation.  It forgets
the occurrence identities, residual phases and physical ports after a leaf
is summarized by `(U,L)`.  Therefore it does not by itself transport a
common decoration through a glue, compare factors with different component
partitions, or constitute a dimension-recursive Pascal theorem.  Such a
transfer needs the richer occurrence-labelled relation; terminal existence
over a factor family is handled separately in Section 6.

## 4. Gap-Hall realization inside one leaf

The local set `mathscr A(C)` need not be enumerated blindly.  Choose a set
`I_C` of upper-turn occurrences on `C`.  If it is nonempty, make the cyclic
gaps between consecutive members of `I_C` and connect each gap to every
lower colour occurrence lying in it.  A perfect matching from these gaps to
distinct lower colours chooses exactly one `B` mark per gap and is
equivalent to alternating shore types on `C`.  Retain the occurrence label
of a matching edge, because it fixes the binary trace.

The configuration is locally accepting exactly when:

1. the selected upper colours are distinct;
2. the occurrence-labelled gap graph has a matching saturating every gap;
3. the selected lower colours are distinct; and
4. the resulting trace has at least one zero and is off the mixed cycle
   face.

When `I_C` is empty, the only configurations are the two unmarked phases.
Thus the leaf relation has an exact ordinary matching oracle plus a finite
cyclic trace test.

Globally, fixing one upper occurrence for every `U in mathcal U` produces
the single occurrence-labelled gap--lower-colour graph across all marked
components from
`MATH_THEOREM_R_CATALAN_DECORATED_TWO_FACTOR_GAP_HALL_AND_CYCLE_BUDGET_20260731.md`.
A perfect matching there fixes the marked occurrences before the trace
filter.  If `u` components remain unmarked, it has `2^u` literal
root-configuration lifts, one for each independent residual phase.  The
projected existence relation records only that at least one lift exists.

## 5. Why scalar or separate-rainbow induction is insufficient

Projecting `mathcal R_v` to cardinalities loses the colour correlations.
Even retaining separate upper and lower coverage is insufficient: the
audited `ML(7)` gap-Hall counterexample has both turn maps surjective but no
joint alternating representatives.  In the component-balance flow of the
companion theorem, that one-component example passes automatically and then
fails at the cyclic gap relation.

Likewise, requiring one decoration to survive every gluing hex is stronger
than (3.4).  For the frozen positive `ML(7)` cycle, the exact
Hamilton-output census is

\[
 31\text{ alternating hexes},\quad16\text{ Hamilton outputs},\quad
 10\text{ of those Hamilton outputs decorable},\quad
 6\text{ sharing a forest decoration with the source}.          \tag{5.1}
\]

Those ten Hamilton-output factors have a nonempty accepting fibre.  The
number six has a different meaning: only six source/output pairs share one
**literal occurrence-labelled forest decoration**.  It is not an
intersection count for the colour-set relations (3.1), because every factor
relation contains `(empty,empty)` and every accepting root uses the same
full-palette pair.  The cited census does not classify the remaining split
outputs for the weaker componentwise D2F target.

Thus the relation (3.1) is exact for terminal existence on one fixed factor
partition, but it is too coarse to transport a common decoration across a
switch.  Fixed-decoration transparency requires an occurrence/phase-labelled
relation together with the two-shore local turn-multiset equality and
retained-fragment boundary alternation.  The minimal D2F target permits
complete representative reoptimization at the terminal factor and does not
require the terminal factor to be Hamiltonian.

## 6. Factor-family and circuit extension

For a family `mathscr F` of allowed terminal 2-factors, put

\[
                         P_{\mathscr F}=\sum_{F\in\mathscr F}P_F. \tag{6.1}
\]

Then `[mathfrak m_*]P_mathscr F>0` if and only if some factor in the family
is accepting.  Since any two spanning 2-factors differ by unrestricted
alternating circuits, taking `mathscr F` to be all spanning 2-factors removes
the starting factor and component-merging order from the existential gate.

This does not make a strict ECO family connected, and it does not preserve
residence, deep shadows, RSB, seam chronology, voltage, or compiler state.

## 7. Sharp remaining theorem

The direct all-dimension route is now exactly:

> Construct an explicit recursively described family `mathscr F_m` of
> spanning `ML(2m-1)` 2-factors and prove
> `[mathfrak m_*]P_mathscr F_m>0` for every `m>=2`.

Equivalently, prove that the relation recurrence has the full-palette pair
at its root.  Theorems 2.1 and 3.1 prove the implication and exact
composition; they do not prove this nonemptiness statement.

If such a theorem is proved, it gives central Catalan Linear Matching only.
The full equality `nu(k)=B(k)` still requires residence, all deeper shadows,
RSB and the common lower compiler on one literal chronology.
