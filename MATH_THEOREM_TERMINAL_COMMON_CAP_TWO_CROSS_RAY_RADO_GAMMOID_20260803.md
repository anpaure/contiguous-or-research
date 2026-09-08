# FORMATTING-FAILED DRAFT — DO NOT CITE

This first draft lost TeX backslashes through the patch transport.  Its
mathematical replacement is
`MATH_THEOREM_TERMINAL_COMMON_CAP_TWO_CROSS_RAY_RADO_GAMMOID_V2_20260803.md`.
The draft is retained only as lineage and is not an authenticated theorem.

# Terminal common-cap linkage for two cross-ray systems and transported background

**Date:** 2026-08-03  
**Status:** unconditional abstract strict-gammoid/Rado theorem, exact
all-subset and all-cut formula, and an (O(1))-deficiency corollary under an
occurrence-labelled cross-ray lifting hypothesis.  The physical lifting
hypothesis is explicit and is not inferred from value-level ray matchings.

## 0. Outcome

Fix one complete terminal common-cap state.  After an authenticated
background linkage has been transported, the admissible physical
occurrences for each terminal ticket induce one Rado matroid for each of the
two canonical cross-ray systems.  The tickets simultaneously realizable in
both systems are the common independent sets of those two matroids.

If (I) is the common ticket set, its exact deficiency is

\[
\boxed{
 \delta=
 \max_{\substack{J_0,J_1\subseteq I\\J_0\cap J_1=\varnothing}}
 \left[
 |J_0|-r_{N_0}(A_0(J_0))+
 |J_1|-r_{N_1}(A_1(J_1))
 \right].}
\tag{0.1}
\]

Here (A_p(J)) is the union of the literal occurrence-labelled entry menus
of tickets in (J), and (N_p) is the phase/system-(p) gammoid after
protecting the transported background.  Menger turns (0.1) into an exact
pair of all-cut inequalities.

Let (Z) be the tickets which are loops in at least one of the two Rado
matroids.  Then

\[
                 \boxed{\delta_I=|Z|+\delta_{I\setminus Z}.}
\tag{0.2}
\]

Consequently, if (|Z|\le z) and the two residual Rado systems have
all-subset deficiencies at most (k_0,k_1), then

\[
                       \boxed{\delta\le z+k_0+k_1.}
\tag{0.3}
\]

Thus two occurrence-exact canonical cross-ray linkages plus a transported
background give terminal common-cap deficiency (O(1)) whenever their
joint exceptional label set and residual cut defects are (O(1)).  Exact
private side-cell cross matchings and exact background transport give the
special case (delta=0).

The qualification “occurrence-exact” is load-bearing.  Two abstract ray
matchings, two marginal phase matchings, or a matching on target values do
not imply (0.3).

## 1. Fixed state and occurrence-expanded data

Let ({\cal C}) be the family of complete terminal cap/guard states.  A
state (c\in{\cal C}) fixes every shared source letter, declared row state,
flag, deadline, endpoint guard, occurrence capacity, and structural zero
used below.  All matroids in this note are formed only after (c) is fixed.

Let (I) be the finite set of terminal **ticket labels**.  A label includes
its common declared state.  If common state is still a choice, first fix a
common state assignment; optimizing over such assignments is an outer
operation, not part of the matroid rank below.

For (p\in\{0,1\}), let

\[
 A_{p,i}^c\subseteq V(D_p^c)
\]

be the complete menu of entry ports for the physical occurrence of ticket
(i) in canonical system (p).  A port record contains at least

\[
 (i,c,p,\hbox{ray},\hbox{role},\hbox{physical row/cell},
  \hbox{flag},\hbox{endpoint},\hbox{guard footprint}).
\tag{1.1}
\]

Equal target masks at different addresses remain different ports.  Two
records sharing one physical capacity pass through the same capacity-one
vertex.  Two different physical rows with the same value remain two
vertices.

The directed graph (D_p^c) is unit-vertex-split and contains every shared
capacity gadget and every terminal sink in (T_p^c).  Its linkable vertex
sets form the strict gammoid

\[
                    M_p^c=L(D_p^c,T_p^c).
\tag{1.2}
\]

### Transported background

Let (B_p^c) be an independent occurrence-labelled background set of size
(b_p).  There are two exact interpretations.

* If its named transported routes are frozen and private, remove their used
  capacities and terminal slots before defining the residual network.
* If background recourse is allowed, protect only its service by contracting
  it in the gammoid:

  \[
   N_p^c=M_p^c/B_p^c,
   \qquad
   r_{N_p^c}(X)=lambda_p^c(B_p^c\cup X,T_p^c)-b_p,
  \tag{1.3}
  \]

  where (lambda_p^c) is maximum vertex-disjoint linkage size.

The second form may reroute the background; it does not freeze a named
matching.  When full-block transport gives private background paths, the two
forms agree on the residual ray bank.

The menus (A_{p,i}^c) are static in the one fully materialized terminal
state.  Candidate-created hosts which appear only when other tickets are
selected are not unconditionally present ports.

## 2. Rado matroids on ticket labels

For (J\subseteq I), put

\[
                    A_p^c(J)=\bigcup_{i\in J}A_{p,i}^c.
\tag{2.1}
\]

A ticket set (S\subseteq I) is system-(p) feasible if it admits distinct
representatives (a_i\in A_{p,i}^c) whose representative set is independent
in (N_p^c).  Rado's theorem says that these sets form a matroid (R_p^c)
on (I), with rank

\[
 \boxed{
 \rho_p^c(S)=
 \min_{J\subseteq S}
 \left(|S\setminus J|+r_{N_p^c}(A_p^c(J))\right).}
\tag{2.2}
\]

Every ticket selected by a common-cap compiler must be feasible in both
systems under the same fixed state (c).  Conversely, if the two system
networks use separate physical capacity copies after all genuinely shared
capacities have been placed into the state/gadget, a set independent in both
(R_0^c,R_1^c) has the required two occurrence linkages.

### Theorem 2.1 (exact common-label min--max)

Let

\[
 \nu(c)=\max\{|S|:S\in R_0^c\cap R_1^c\},
 \qquad \delta(c)=|I|-\nu(c).
\tag{2.3}
\]

Then

\[
 \nu(c)=\min_{U\subseteq I}
 \left(\rho_0^c(U)+\rho_1^c(I\setminus U)\right),
\tag{2.4}
\]

and (0.1) holds with (N_p=N_p^c,A_p=A_p^c).

#### Proof

Equation (2.4) is Edmonds' two-matroid intersection theorem.  Substitute
(2.2).  For (J_0\subseteq U) and
(J_1\subseteq I\setminus U),

\[
\begin{aligned}
 &|U\setminus J_0|+r_{N_0}(A_0(J_0))
  +|(I\setminus U)\setminus J_1|+r_{N_1}(A_1(J_1))\\
 &=|I|-\left[
 |J_0|-r_{N_0}(A_0(J_0))
 +|J_1|-r_{N_1}(A_1(J_1))\right].
\end{aligned}
\]

As (U) varies, the possible pairs (J_0,J_1) are exactly the disjoint
pairs of subsets of (I).  Taking the minimum and subtracting from (|I|)
gives (0.1).  \(\square\)

The disjointness of (J_0,J_1) shares one omission budget between the two
systems.  Adding two independently computed full-set deficiencies is a
valid upper bound, but need not be exact.

## 3. Exact all-cut form

In the unit-split graph, let

\[
 \gamma_{p,C}^c(X)
\]

denote the capacity of a source--sink cut (C) in the network whose source
bank is the occurrence-labelled set (Xcup B_p^c).  Infinite
claim-to-entry arcs are not cuttable.  Menger and (1.3) give

\[
 r_{N_p^c}(X)=min_C\gamma_{p,C}^c(X\cup B_p^c)-b_p.
\tag{3.1}
\]

### Theorem 3.1 (all-subset/all-cut common-cap criterion)

For an integer (K\ge0), the fixed state (c) has common deficiency at
most (K) if and only if, for every disjoint (J_0,J_1\subseteq I) and
every pair of cuts (C_0,C_1),

\[
\boxed{
 \gamma_{0,C_0}^c(B_0^c\cup A_0^c(J_0))
 +\gamma_{1,C_1}^c(B_1^c\cup A_1^c(J_1))
 \ge b_0+b_1+|J_0|+|J_1|-K.}
\tag{3.2}
\]

#### Proof

Insert (3.1) into (0.1).  The negative of a minimum cut is a maximum over
cuts, independently in the two systems.  Therefore

\[
\begin{aligned}
\delta(c)=
\max_{\substack{J_0\cap J_1=\varnothing\\C_0,C_1}}
 \{&|J_0|+|J_1|+b_0+b_1\\
   &-\gamma_{0,C_0}^c(B_0^c\cup A_0^c(J_0))
    -\gamma_{1,C_1}^c(B_1^c\cup A_1^c(J_1))\}.
\end{aligned}
\tag{3.3}
\]

Inequality (3.2) is exactly the assertion that the right side is at most
(K).  \(\square\)

A linkage rank of the full union (A_p(I)) is not a replacement for
(3.2).  Rado requires every ticket subset: a large union rank can be carried
by ports belonging to one ticket while many other tickets share a single
port.

## 4. Structural zeros

Define the genuine fixed-state structural-zero set

\[
 Z(c)=\{i\in I:\rho_0^c(\{i\})=0
                 \text{ or }\rho_1^c(\{i\})=0\}.
\tag{4.1}
\]

An empty raw menu is sufficient but not necessary: a nonempty menu whose
ports are all loops after background contraction is also structural zero.
The zero-threshold shores in the abstract birail calculation are not
structural zeros; their purpose is precisely to be served by the opposite
positive shore.

### Lemma 4.1 (exact zero separation)

Equation (0.2) holds.

#### Proof

Every element of (Z(c)) is a loop in at least one of the two matroids and
belongs to no common independent set.  Deleting all of (Z(c)) therefore
does not change the maximum common independent-set size.  Subtract that
unchanged value first from (|I\setminus Z|) and then from (|I|).  \(\square\)

Arbitrary absent incidences outside (Z(c)) do not receive an additive
charge.  They remain inside the ranks and cuts of Sections 2--3.  For
example, (m) nonzero tickets can all have the same sole capacity-one port;
there are no structural-zero tickets, yet the deficiency is (m-1).

## 5. The (O(1)) theorem

### Theorem 5.1 (bounded terminal common-cap deficiency)

Fix (c\) and put (I'=I\setminus Z(c)).  Suppose

\[
 |Z(c)|\le z
\tag{5.1}
\]

and, for (p=0,1),

\[
 r_{N_p^c}(A_p^c(J))\ge |J|-k_p
 \qquad(J\subseteq I').
\tag{5.2}
\]

Then

\[
                        \boxed{\delta(c)\le z+k_0+k_1.}
\tag{5.3}
\]

If a separately transported background target bank omits at most (eta)
targets outside (I), the total terminal compiler deficiency is at most

\[
                         \boxed{\beta+z+k_0+k_1.}
\tag{5.4}
\]

#### Proof

Equation (5.2) and Rado's rank formula give
(ho_p^c(S)\ge |S|-k_p) for every (S\subseteq I').  Apply (2.4):

\[
 \nu_{I'}(c)\ge
 \min_{U\subseteq I'}
 \left(|U|-k_0+|I'\setminus U|-k_1\right)
 =|I'|-k_0-k_1.
\]

Lemma 4.1 proves (5.3).  The independently omitted background targets add
at most (eta), proving (5.4).  \(\square\)

The all-subset hypotheses in (5.2) may be certified by an explicit
near-spanning occurrence-labelled linkage.  If system (p) has
vertex-disjoint, correctly typed routes for every ticket outside an
exceptional set (E_p), then matroid nullity monotonicity gives (5.2) with
(k_p\le|E_p|).  Equivalently, each sink-avoiding cut traps at most its
capacity plus (|E_p|) ticket labels.

### Corollary 5.2 (two canonical cross-ray matchings plus background)

Assume, in one common state (c), that:

1. the transported background is an occurrence-labelled linkage omitting
   at most (eta=O(1)) background targets;
2. every abstract edge of each canonical cross-ray matching is expanded to
   all of its required physical occurrences;
3. after removing (Z(c)cup E_p), those occurrence routes are pairwise
   vertex-disjoint in system (p), correctly typed at their terminals, and
   simultaneously disjoint from the protected background;
4. (|Z(c)|,|E_0|,|E_1|=O(1)); and
5. folding/unfolding preserves ticket, common state, occurrence address and
   every capacity used by the routes.

Then

\[
 \boxed{\operatorname{def}_{\rm terminal}
       \le\beta+|Z(c)|+|E_0|+|E_1|=O(1).}
\tag{5.5}
\]

If the background is exact, the cross-ray side cells are private from its
image, all required cross edges survive, and (Z(c)=\varnothing), their
literal union is already a complete common compiler matching and the
deficiency is zero.

This corollary is the rigorous form of “two cross matchings plus transported
background.”  An abstract matching edge is not counted until every physical
occurrence it represents is present.

## 6. Required occurrence-labelled lifting lemma

For Corollary 5.2, a folded cross-ray path must satisfy all of the following.

1. Every legal physical full block maps to a folded path.
2. Every folded path unfolds to a legal physical full block.
3. Vertex-disjoint folded paths are equivalent to simultaneous physical
   feasibility, with every shared capacity represented once.
4. Path switching preserves ticket label, common declared state, phase,
   occurrence row/cell, role, endpoint class and prescribed terminal type;
   alternatively, every switch has an explicit legal normalization with the
   same complete data.
5. The lift commutes with protecting or contracting the transported
   background.
6. No selected ticket receives a provider/host which exists only after a
   different, not-yet-selected ticket is installed.

If one abstract cross ticket consumes two physical cells, both cells appear
as separate capacity vertices.  Serving all occurrence atoms serves the
ticket.  If at most (K) occurrence atoms are unserved, at most (K)
logical tickets are incomplete.  Ordinary Rado does not, however, optimize
an arbitrary choice of two-cell bundles: without the fixed canonical lift,
that is a matroid-parity or more general set-packing problem.

Terminal sinks may be treated as interchangeable only within a complete
occurrence type for which every path permutation is physically legal.
Otherwise terminal identity must be encoded in the state/gadget; aggregate
source-to-sink linkage can silently swap two prescribed occurrence labels.

## 7. Choosing the common cap

For the cap family ({\cal C}), the actual optimum is

\[
 \max_{c\in{\cal C}}\nu(c)
 =\max_{c\in{\cal C}}\min_{U\subseteq I}
   \left(\rho_0^c(U)+\rho_1^c(I\setminus U)\right).
\tag{7.1}
\]

Thus a target bound (K) requires the quantifier order

\[
 \boxed{
 \exists c\in{\cal C}\ \forall U\subseteq I:\quad
 \rho_0^c(U)+\rho_1^c(I\setminus U)\ge |I|-K.}
\tag{7.2}
\]

The weaker statement (orall U\,\exists c) is invalid, as is choosing
one cap independently in each system.  A usable proof must exhibit one cap,
prove the bound uniformly for every cap in a nonempty family, or supply a
genuine intersection theorem for the good-cap sets.

Phase 1 may be a transported background theorem input.  Transport alone
does not authenticate it as a private/native phase.

## 8. Sharp obstructions

The following show why the hypotheses cannot be dropped.

1. **Common-state mismatch.**  One ticket has only state (a) in system 0
   and only state (b\ne a) in system 1.  Both marginal Rado ranks equal
   one, but the true common-state rank is zero.
2. **Shared bottleneck.**  (m) ticket menus all contain the same sole
   capacity-one occurrence.  Every singleton is nonzero, but deficiency is
   (m-1).
3. **Correlated two-ray choices.**  Let one ticket allow ((a,c)) or
   ((b,d)), and another allow ((a,d)) or ((b,c)).  Each ray projection
   has a perfect matching, but no two full pairs are coordinate-disjoint.
4. **Dynamic support.**  If ticket (i) exists only using a host created by
   (j), and (j) exists only using a host created by (i), the pair may
   be feasible while neither singleton is.  Feasibility is not hereditary,
   so no fixed Rado matroid represents it.
5. **Unlabelled terminal swap.**  An aggregate two-source/two-sink linkage
   may connect each source to the wrong prescribed sink.  Menger's ordinary
   cut theorem permits the permutation unless the occurrence type makes it
   legal or the identity is retained in the network.
6. **Accumulating local defect.**  A sequence of layers can kill a different
   coordinate at every step.  Per-layer deficiency one does not imply
   terminal (O(1)); a global layered-gammoid cut or one fixed (O(1))
   exceptional set is required.

## 9. Scope

Theorems 2.1, 3.1 and 5.1 are exact abstract matroid/linkage theorems.
Corollary 5.2 is conditional on the occurrence-labelled physical lifting
lemma of Section 6 and one fixed compatible cap state.  This note does not
prove that a particular folded-C8 carrier supplies that lift, does not solve
owner, residence, chronology, upper-shadow or compiler regeneration, and
does not prove an all-dimensional source bank or a final OR word.
