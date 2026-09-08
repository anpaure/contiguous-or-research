# The `B+1` occurrence section:
# a sharp interval obstruction, the dual join tree, reserve Hall, and a blocker LLL

**Date:** 2026-08-04  
**Scope:** pure fixed occurrence-labelled factor mathematics  
**Status:** one sharp abstract no-go, exact dual-CSP and acyclic-join
criteria, and two conditional sufficient existence theorems.  No finite
search, solver, random experiment, Boolean host construction, or `B+1`
upper bound is claimed.

## 0. Outcome

Let `F` be a directed cycle cover, let `u(e)` be the immediate-upper colour
of the labelled occurrence `e`, and let `P` be a rainbow protected bank.
The objective is to keep one occurrence of every colour, keep `P`, omit an
edge of every old cycle, and keep one old interval witness of every proper
higher target.

There is no universal fixed-factor theorem at this abstract interface.
Already one directed four-cycle with colour word

\[
                              R,A,R,B
\]

and two unique, disjoint two-edge interval witnesses can force the two
different `R` occurrences.  Each target is individually feasible, and every
occurrence section automatically breaks the old cycle, but the two targets
cannot coexist.  This is an inclusion-minimal forced-literal obstruction.
It is not asserted to be the occurrence table of a Boolean rooted factor.

Three positive statements survive this obstruction.

1. There is an exact **dual CSP** whose variables are targets and whose
   values are witness choices.  One relation per q1 colour requires all
   chosen witnesses using that colour to use the same physical occurrence.
   This dual join is nonempty exactly when a protected rainbow witness bank
   exists.

2. If the colour-relation scopes have a running-intersection tree, repeated
   semijoin pruning is exact: the dual join is nonempty if and only if its
   arc-consistency core is nonempty.  Laminar colour footprints are a
   special case.  Running intersection alone is not enough; the four-cycle
   obstruction has laminar dual scopes but an empty colour relation.

3. Let `A` contain the pivot and every occurrence in the restricted witness
   menus.  If the occurrences outside `A` satisfy the capacitated
   component--colour Hall inequalities, then **every** compatible witness
   choice extends to an upper-exact forest.  This immutable reserve condition
   decouples cycle omission from target selection.

There is also a direct probabilistic criterion.  Sample one occurrence of
each colour independently.  Target failure is a blocker-transversal event,
and failure to break a component is a second bad event.  An asymmetric
Lovasz local lemma on their literal colour scopes gives a joint occurrence
section.  Under immutable reserve Hall, the component bad events may be
removed from the lemma entirely.

These are exact or sufficient host properties, not a proof that the Boolean
all-width witness menus have a dual join tree, a nonempty semijoin core,
enough immutable reserves, or the required local-lemma parameters.

## 1. Fixed ground and admissible menus

Use the notation

\[
 E=E(F),\qquad E_R=u^{-1}(R),\qquad
 \mu_R=|E_R|,\qquad b_R=\mu_R-1,                    \tag{1.1}
\]

and let `mathcal K` be the component set of `F`.  Assume

\[
                         |P\cap E_R|\le1             \tag{1.2}
\]

for every colour.  Its protected occurrence domain is

\[
 \Omega_R=
 \begin{cases}
  \{p\},&P\cap E_R=\{p\},\\
  E_R,&P\cap E_R=\varnothing.
 \end{cases}                                        \tag{1.3}
\]

For every required proper higher target `X`, let `mathcal W_X` be its old
path- or cyclic-interval witness family, with internal occurrence set
`J(I)`.

A witness `I` is **admissible** when

* `J(I)` contains at most one occurrence of each colour; and
* whenever \(P\cap E_R=\{p\}\) and `J(I)` uses colour `R`, its `R`
  occurrence is `p`.

Equivalently, `P union J(I)` is rainbow.  Fix a nonempty restricted menu

\[
                         \mathcal M_X\subseteq\mathcal W_X              \tag{1.4}
\]

of admissible witnesses for every target.  All positive theorems below are
relative to these declared menus.  For `I in mathcal M_X`, define the
partial occurrence map

\[
 \rho_I(R)=e\quad\Longleftrightarrow\quad J(I)\cap E_R=\{e\};            \tag{1.5}
\]

leave `rho_I(R)` undefined when `I` does not use `R`, and put

\[
 A=P\cup\bigcup_X\bigcup_{I\in\mathcal M_X}J(I).       \tag{1.6}
\]

An occurrence section is a tuple

\[
                   a=(a_R)_R\in\prod_R\Omega_R,        \tag{1.7}
\]

with selected edge set `Q(a)={a_R:R}`.  It realizes `I` when
`a_R=rho_I(R)` for every colour used by `I`.

## 2. Universal fixed-factor existence is false

Say that a menu `mathcal M_X` **forces** the literal `(R,e)` when every
`I in mathcal M_X` uses colour `R` and has `rho_I(R)=e`.

### Proposition 2.1 (forced-literal obstruction)

If two required targets force `(R,e)` and `(R,f)` with \(e\ne f\), then no
occurrence section realizes a menu witness for both targets.

#### Proof

The first target requires `a_R=e`, while the second requires `a_R=f`.
One section has only one `R` coordinate.  \(\square\)

This is only a sufficient obstruction in general: inconsistency may require
several alternative witnesses and contain no forced literal.

### Proposition 2.2 (sharp one-cycle two-interval no-go)

There is an abstract fixed factor satisfying all of the following.

1. `F` is one directed four-cycle and \(P=\varnothing\).
2. There are two targets, each with one individually admissible two-edge
   cyclic-interval witness.
3. Each target separately has an upper-exact forest section.
4. Every occurrence section is a forest.
5. No occurrence section realizes both targets.

#### Proof

Write the four labelled cycle edges in cyclic order as

\[
                              e,a,f,b                 \tag{2.1}
\]

and give them colours

\[
                 u(e)=u(f)=R,\qquad u(a)=A,\qquad u(b)=B.             \tag{2.2}
\]

Give target `X` the unique witness `J(I_X)={e,a}` and target `Y` the
unique witness `J(I_Y)={f,b}`.  Both are two-edge cyclic intervals and are
individually rainbow.

Here

\[
                         b_R=1,\qquad b_A=b_B=0.       \tag{2.3}
\]

Every section keeps `a,b` and exactly one of `e,f`; it therefore omits one
edge of the unique old cycle.  Keeping `e` realizes `X`, and keeping `f`
realizes `Y`, so either singleton target family is feasible.  Realizing both
would keep both `R` occurrences, which a section cannot do.  \(\square\)

The obstruction is inclusion-minimal with respect to its target relations:
deleting either relation makes the instance feasible.  Among instances in
which every target is individually admissible, at least two target
relations and at least two occurrences of one colour are needed for this
kind of cross-target contradiction.  This is the claimed sharpness.  It is
an obstruction at the occurrence-interval interface only; no Boolean
realizability is inferred.

In deletion language, the exact quota forces `D={e}` or `D={f}`.  Target
`X` requires `D={f}`, while target `Y` requires `D={e}`.  Thus the example
is simultaneously a section obstruction and a two-blocker obstruction.

## 3. The dual target-choice CSP

For a colour `R`, let

\[
 T_R=\{X:\rho_I(R)\text{ is defined for some }I\in\mathcal M_X\}.       \tag{3.1}
\]

Define a relation on witness-choice variables by

\[
 \mathcal C_R=
 \left\{(I_X)_{X\in T_R}\in\prod_{X\in T_R}\mathcal M_X:
   \left|\{\rho_{I_X}(R):\rho_{I_X}(R)\text{ defined}\}\right|\le1
 \right\}.                                             \tag{3.2}
\]

Also include the unary domain relation

\[
                              \mathcal D_X=\mathcal M_X.                \tag{3.3}
\]

Undefined values in (3.2) impose no condition: a chosen witness which does
not use `R` does not reserve an `R` occurrence.

### Theorem 3.1 (exact dual-join equivalence)

A protected rainbow witness selector from the restricted menus exists if
and only if

\[
                 \left(\Join_R\mathcal C_R\right)
                    \Join\left(\Join_X\mathcal D_X\right)              \tag{3.4}
\]

is nonempty.  The variables in this join are the targets `X`, and the value
of variable `X` is its chosen witness `I_X`.

#### Proof

Choose one menu witness for every target.  Because every chosen witness is
individually admissible, their union with `P` is rainbow exactly when, for
each colour `R`, every chosen witness which uses `R` uses the same labelled
occurrence.  That condition is precisely membership in `mathcal C_R`.
The unary relations impose the declared domains.  Intersecting the
conditions over all colours proves both directions.  \(\square\)

This is dual to the occurrence-section CSP: there the variables are colours
and target survival is a relation; here the variables are targets and
physical-occurrence agreement is one relation per colour.

### Theorem 3.2 (dual running intersection and exact semijoin core)

Index the relations in (3.4) by `i in mathcal I`, write their scopes as
`S_i`, and suppose there is a tree `T` on `mathcal I` such that, for every
target variable `X`,

\[
                         \{i:X\in S_i\}               \tag{3.5}
\]

induces a connected subtree.

Start with the relations `B_i=mathcal A_i`, where `mathcal A_i` denotes
the corresponding `mathcal C_R` or `mathcal D_X`.  Repeatedly delete a
tuple `z in B_i` whenever some neighbour `j` of `i` has no tuple
`w in B_j` with

\[
                       z|_{S_i\cap S_j}=w|_{S_i\cap S_j}.               \tag{3.6}
\]

Continue until no deletion is possible, and call the resulting relations
`B_i^*`.  Then the dual join (3.4) is nonempty if and only if

\[
                              B_i^*\ne\varnothing
                       \qquad(i\in\mathcal I).         \tag{3.7}
\]

Indeed, every tuple of every nonempty `B_i^*` extends to a global witness
selector.

#### Proof

The restriction of a global join tuple is never deleted: at every adjacent
relation its other restriction supplies the support required in (3.6).
Thus a nonempty join implies (3.7).

Conversely, root `T` at any relation and choose any root tuple in its
nonempty core.  For each child, (3.6) supplies a core tuple agreeing with
the already chosen parent tuple on the separator.  Continue recursively.
The running-intersection property says that every target variable shared by
two tree regions occurs on the whole path between them.  Adjacent agreement
therefore glues all chosen relation tuples to one global assignment.  The
same recursion can begin with any prescribed core tuple.  \(\square\)

### Corollary 3.3 (laminar and separator-surjective hosts)

If the nonempty scopes among `T_R` and `{X}` form a laminar family, they
admit a running-intersection tree, so Theorem 3.2 applies.  In particular,
if every relation is nonempty and, on every edge `ij` of such a tree,

\[
        \pi_{S_i\cap S_j}(\mathcal A_i)
          =\pi_{S_i\cap S_j}(\mathcal A_j),           \tag{3.8}
\]

then a protected rainbow selector exists.

#### Proof

Connect each laminar set to a minimal strict superset, join disjoint roots
arbitrarily, and attach duplicate or singleton scopes inside their
containment chain.  Sets containing one target form a connected chain, so
this is a join tree.  Under (3.8), every tuple on either endpoint of a tree
edge has a compatible tuple at the other endpoint.  Hence semijoin pruning
deletes nothing, and Theorem 3.2 applies.  \(\square\)

The nonempty-core condition, not laminarity alone, is the exact weakest
compatibility condition **within this fixed dual join-tree class**.  The
four-cycle of Proposition 2.2 has laminar dual scopes

\[
                    T_R=\{X,Y\},\qquad T_A=\{X\},\qquad T_B=\{Y\},       \tag{3.9}
\]

but \(\mathcal C_R=\varnothing\).

Literal interval geometry also does not force a join tree after colours are
identified.  On one six-cycle, take three pairwise disjoint two-edge
intervals with colour pairs

\[
                           RS,\qquad ST,\qquad RT.     \tag{3.10}
\]

Their support intervals are disjoint, but their target scopes are
`{R,S},{S,T},{R,T}`.  A join tree on these three scopes would have to make
all three pairs adjacent, because each colour belongs to exactly two of the
scopes.  No three-vertex tree does so.  Thus repeated colour fibres can
destroy the laminarity visible in the literal interval supports.

## 4. Deterministic immutable-reserve Hall

For a colour `R`, define the component set with a menu-immutable deletion
reserve by

\[
 N_R^{\rm res}(A)=
 \{K\in\mathcal K:(E(K)\cap E_R)-A\ne\varnothing\}.                   \tag{4.1}
\]

### Theorem 4.1 (dual selector plus reserve Hall)

Assume the restricted menus have a protected rainbow witness selector.  If

\[
 |Y|\le
 \sum_{R:N_R^{\rm res}(A)\cap Y\ne\varnothing} b_R
                     \qquad(Y\subseteq\mathcal K),                   \tag{4.2}
\]

then there is an occurrence section `Q_0` which

* contains `P` and the selected witness of every target;
* contains exactly one occurrence of every q1 colour; and
* omits an edge of every old cycle, hence is a directed path forest.

Equivalently, its deletion complement `D=E-Q_0` avoids `P`, has
\(|D\cap E_R|=b_R\), meets every old cycle, and is not a transversal of any
target's complete witness family.

#### Proof

Let

\[
                       H=P\cup\bigcup_XJ(I_X).         \tag{4.3}
\]

The selector makes `H` rainbow and \(H\subseteq A\).  Inequality (4.2) is
capacitated Hall from old components to colours: component `K` may be
assigned colour `R` when it has an `R` occurrence outside `A`, and colour
`R` has capacity `b_R`.  Choose such an assignment covering all components
and designate one corresponding reserve occurrence in each component.
These designated occurrences lie outside `A`, hence outside `H`.

For each colour `R`, at most `b_R` designated occurrences have that colour.
Fill its deletion set arbitrarily to exactly `b_R` occurrences while
avoiding `H`.  This is possible because a rainbow `H` uses at most one of
the `mu_R` occurrences.  The complement contains `H`, has exactly one edge
of every colour, and omits the designated edge of every old cycle.  Every
selected old witness therefore survives.  \(\square\)

Condition (4.2) is exact for the construction class in which every cycle is
assigned a designated breaking edge outside the full menu envelope `A`.
It is only sufficient for unrestricted forest extension: when (4.2) fails,
an edge in `A-H` may still be available for deletion after the actual
selector is known.

### Corollary 4.2 (dual-laminar reserve theorem)

Suppose the dual relation scopes have a running-intersection tree, their
semijoin core is nonempty, and (4.2) holds.  Then the desired protected
upper-exact all-width forest exists.

#### Proof

Theorem 3.2 supplies the rainbow selector, and Theorem 4.1 extends it.
\(\square\)

### Corollary 4.3 (coherent-menu host)

Suppose every menu is nonempty and

\[
                              |A\cap E_R|\le1          \tag{4.4}
\]

for every colour `R`.  If (4.2) holds, the desired forest exists.

#### Proof

Choose an arbitrary witness from every menu.  By (4.4), their union with
`P` is rainbow.  Apply Theorem 4.1.  \(\square\)

This is the simplest deterministic reserve certificate.  The dual
join-tree theorem permits many colours to have several active occurrences,
provided the witness choices retain a nonempty consistency core.

## 5. A product-measure blocker local lemma

For every colour independently sample

\[
                         a_R\sim\pi_R                 \tag{5.1}
\]

from a probability distribution `pi_R` on `Omega_R`.  Thus every protected
colour is deterministic.  For an admissible witness `I`, put

\[
 S(I)=u(J(I)),\qquad
 w(I)=\prod_{e\in J(I)}\pi_{u(e)}(e).                 \tag{5.2}
\]

For every target choose a sub-menu

\[
                         \mathcal L_X\subseteq\mathcal M_X             \tag{5.3}
\]

such that the colour scopes `S(I)`, `I in mathcal L_X`, are pairwise
disjoint.  Let `B_X` be the event that the random section realizes no
witness in `mathcal L_X`.  Independence inside this one target gives

\[
 \Pr(B_X)=p_X:=\prod_{I\in\mathcal L_X}(1-w(I)),
 \qquad
 S(B_X)=\bigcup_{I\in\mathcal L_X}S(I).               \tag{5.4}
\]

In deletion language, `B_X` says that `D(a)=E-Q(a)` meets every witness in
the restricted menu: it is exactly the restricted blocker-transversal bad
event.

For a component `K`, let `C_K` be the event that the section selects every
edge of `K`.  If `u` is not injective on `E(K)`, this event is impossible.
Otherwise put

\[
 c_K=\Pr(C_K)=\prod_{e\in E(K)}\pi_{u(e)}(e),
 \qquad S(C_K)=u(E(K)),                               \tag{5.5}
\]

where a factor with \(e\notin\Omega_{u(e)}\) is interpreted as zero.  Omit
all zero-probability component events.

Make the dependency graph `Gamma` on the bad events

\[
                 \{B_X\}_X\cup\{C_K:c_K>0\}          \tag{5.6}

by joining two events exactly when their displayed colour scopes intersect.

### Theorem 5.1 (asymmetric blocker--component LLL)

Write `q_Z=p_X` when `Z=B_X` and `q_Z=c_K` when `Z=C_K`.  If there are
numbers `x_Z in (0,1)` such that

\[
 q_Z\le x_Z\prod_{Z'\in N_\Gamma(Z)}(1-x_{Z'})
                           \qquad(Z\in V(\Gamma)),    \tag{5.7}
\]

then there is an occurrence section which contains `P`, realizes one
witness of every target, and omits an edge of every factor component.
Consequently its complement is an admissible deletion set and the selected
section is the required upper-exact rooted forest.

#### Proof

Every bad event is determined by the independent colour variables in its
displayed scope.  Events with disjoint scopes are independent, so `Gamma`
is a valid dependency graph.  Equation (5.4) is exact because the selected
witness events inside `mathcal L_X` use disjoint sets of colour variables.
Equation (5.5) is exact when the component colours are distinct; with a
repeated colour, selecting two different occurrences by one coordinate is
impossible.

The asymmetric Lovasz local lemma applied to (5.7) gives positive
probability that none of the bad events occurs.  Avoiding every `B_X`
retains a declared witness of every target.  Avoiding every `C_K` makes the
section omit at least one edge of every old cycle.  The product domains
force `P`, and there is exactly one selected occurrence per colour by
construction.  \(\square\)

### Corollary 5.2 (symmetric form)

If every bad event in (5.6) has probability at most `p`, every bad event has
at most `Delta` neighbours, and

\[
                             e\,p(\Delta+1)\le1,       \tag{5.8}
\]

then the conclusion of Theorem 5.1 holds.

This is a literal colour-dependency bound.  The number of geometric
intervals which overlap one witness is not a substitute for `Delta` when a
repeated q1 colour couples far-apart intervals.

### Corollary 5.3 (reserve-decoupled blocker LLL)

Let

\[
 A_{\mathcal L}=P\cup
       \bigcup_X\bigcup_{I\in\mathcal L_X}J(I).       \tag{5.9}
\]

Assume the reserve Hall inequalities (4.2) hold with \(A_{\mathcal L}\) in
place of `A`.  Form the dependency graph using only the target events
`B_X`.  If the asymmetric condition (5.7), or the symmetric condition
(5.8), holds for this target-only graph, then the required forest exists.

#### Proof

The local lemma first supplies one occurrence section realizing at least
one witness in every `mathcal L_X`; no component event is imposed.  Choose
one realized witness per target.  Their union with `P` is rainbow because
it is a subset of one occurrence section and lies in \(A_{\mathcal L}\).
Theorem 4.1, applied to these restricted menus, then supplies a possibly
different occurrence section which contains the chosen bank and breaks
every old cycle.  \(\square\)

The reserve-decoupled form is often the cleaner target: component scopes do
not enter the local-lemma dependency degree at all.

## 6. Exact frontier

The occurrence-section problem now has two additional exact faces and two
conditional existence certificates.

* The four-cycle construction proves that individual target feasibility,
  one-cycle omission, and literal interval witnesses do not imply a joint
  section.
* The dual join (3.4) is an exact witness-selector formulation.  On a
  running-intersection host, nonempty semijoin core is necessary and
  sufficient; laminar scopes without relation consistency are insufficient.
* Immutable reserve Hall makes the cycle row independent of which compatible
  witness selector is returned.
* The blocker LLL handles nonacyclic scope systems when restricted target
  menus have enough product-measure success and sufficiently small literal
  colour dependency.

No theorem here proves that a Boolean owner factor has any of these host
properties.  In particular, it does not prove

1. a protected all-parameter upper-surjective factor;
2. nonempty admissible all-width menus;
3. dual laminarity or a nonempty semijoin core;
4. reserve Hall outside the complete witness envelope;
5. an LLL probability or dependency estimate;
6. ordered component-port Hall, switch safety, or a source chronology; or
7. `nu(k)<=B(k)+1`.

The weakest statement established is deliberately scoped: for a fixed
dual join tree the semijoin core is the exact compatibility test, and for
the immutable-reserve construction (4.2) is the exact capacitated
designation test.  No globally weakest Boolean host property is claimed.

## 7. Input ledger

The following files were read in full.  SHA-256 values refer to the exact
workspace bytes used.

* `MATH_THEOREM_BPLUS1_RAINBOW_FOREST_BLOCKER_CSP_AND_MATROID_MINMAX_20260804.md`  
  `e9d32b46c907ef85bf1fb791de57d6d6918fb26746521f91ef876b4d919e4c2e`
* `MATH_AUDIT_BPLUS1_RAINBOW_FOREST_BLOCKER_CSP_AND_MATROID_MINMAX_20260804.md`  
  `818d1155e7391236f266791e0892dc98b520cf81a6399e6f5e8054ddcc1d0530`
* `MATH_THEOREM_BPLUS1_ALLWIDTH_RAINBOW_WITNESS_BANK_AND_SAFE_OPENING_20260803.md`  
  `f44ff6af870e6ef188444193e7c1755bb1441832f3a477a11bc0bda0505d5958`
* `MATH_AUDIT_BPLUS1_ALLWIDTH_RAINBOW_WITNESS_BANK_AND_SAFE_OPENING_20260803.md`  
  `cee21191163d10e46452d3a8eee72ed52b6743321f97630d771e4347808c05b9`
* `MATH_THEOREM_PROTECTED_UPPER_EXACT_CATALAN_FOREST_FORWARD_ATLAS_PULL_ABSORBER_20260803.md`  
  `b2b3c1dcfdcab1338aaffb2783f8a5edc26b8e21a1358e2604696fedaa8333d1`
* `MATH_THEOREM_BPLUS1_PROTECTED_COMPONENT_PORT_HALL_AND_OCTAGON_HAMILTONIZATION_20260803.md`  
  `401aa24568e869909e332c61d222e72d6a0310c585168484e0b30267d6739392`
* `MATH_THEOREM_BPLUS1_CATALAN_HAMILTON_PATH_CERTIFICATE_20260801.md`  
  `a6329c0f3e5f1c7dc5e5ab76338ff52a955f874901e282dc1a17fffae4d7a503`

No finite search, solver, enumeration, or random experiment is used.
