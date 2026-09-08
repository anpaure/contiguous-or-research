# Self-audit: rainbow-forest blocker, CSP, and matroid min--max

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_BPLUS1_RAINBOW_FOREST_BLOCKER_CSP_AND_MATROID_MINMAX_20260804.md`  
**Theorem SHA-256:**
`e9d32b46c907ef85bf1fb791de57d6d6918fb26746521f91ef876b4d919e4c2e`  
**Method:** independent symbolic recheck against the four input files.  No
finite search, solver, or candidate computation is used.

## 0. Verdict

**GO at the fixed occurrence-labelled factor and retained-old-witness
scope.**

The deletion, occurrence-section, fixed-selector matroid-intersection, and
component-omission formulations are equivalent.  The join-tree theorem is
correct under its explicit running-intersection hypothesis.  The reserve
Hall and component-profile statements are one-way criteria with the stated
directions.  The note does not establish any of their hypotheses for the
full Boolean all-parameter instance.

## 1. Occurrence and quota audit

The ground set is the physical edge-occurrence set of `F`; equal colours do
not identify occurrences.  Exact upper representation leaves one member of
each colour class `E_R`, so its deletion complement has exactly
`b_R=mu_R-1` members of that class.  A rainbow protected bank removes at
most one occurrence from deletion availability and therefore always leaves
at least `b_R` available occurrences.

Since `F` is a directed cycle cover, a subset is a forest if and only if it
omits at least one edge of every old cycle.  Thus the three structural rows
of `mathfrak D(F,P)` are respectively upper exactness, pivot survival, and
component omission.  No tail/head or occurrence multiplicity is silently
quotiented.

## 2. Blocker and forced-core audit

A target survives through the old channel exactly when one witness edge set
is disjoint from the deletion set.  Its failure sets are therefore exactly
the transversals of its witness family.  This family is upward closed, so
avoiding every failure set is equivalent to avoiding containment of every
minimal transversal.  Taking complements gives Theorem 2.1 in both
directions.

For a singleton deletion `{e}`, transversality says that `e` lies in every
witness.  This is exactly membership in the forced-cut core.  The theorem
therefore preserves the earlier safe-opening result and correctly explains
why forced cores are incomplete for a forest: two or more cuts can jointly
hit witness intervals whose total intersection is empty.

Every admissible deletion has size `sum_R b_R=W-U=Cat_m`.  Hence transversal
number at least `Cat_m+1` is the exact unstructured guarantee against all
deletion sets of that cardinality.  The theorem labels it stronger than the
quota-aware condition and does not infer it from witness counts.

## 3. Occurrence-section CSP audit

A section chooses one labelled occurrence in every colour domain.  A pivot
edge makes its domain a singleton, so the section contains the pivot
literally.  The target relation is a union of cylinders: one cylinder fixes
exactly the occurrence coordinates used by one witness.  A witness using
two distinct occurrences of the same colour gives inconsistent coordinate
equalities and contributes no tuple.  Reuse of the same occurrence by
different targets is represented by equality of one shared coordinate and
is allowed.

The component relation forbids precisely the tuple selecting every edge of
that component.  If a component repeats one colour, no section can select
both occurrences and the component relation is automatically full, as it
should be.  The natural join therefore gives exactly one protected
upper-exact set, all target witnesses, and all component omissions.  This
proves Theorem 3.1 without an integrality assumption.

For Theorem 3.2, running intersection makes `S_i cap S_j` the complete set
of variables shared across the two sides of tree edge `ij`.  The recursive
message is consequently the exact projection of assignments extendible
over one side.  Leaf induction proves necessity; choosing a root tuple and
back-substituting compatible subtree tuples proves sufficiency.  Laminar
scopes admit such an inclusion tree.  The theorem does not say the actual
target and component scopes are laminar.

## 4. Rainbow-selector and nonmatroid audit

After individually nonrainbow or pivot-conflicting witnesses are removed,
a family of tokens fails to be rainbow exactly when two of its tokens use
different occurrences of one colour.  Pairwise conflict edges therefore
capture the full obstruction, and one token per target is exactly an
independent transversal.

In the displayed augmentation example, `{alpha}` uses occurrences
`r_0,s_0`; `{beta,gamma}` uses `r_1,t,s_1` and is rainbow because the shared
edge `t` is one occurrence, not two.  Adding `beta` to `{alpha}` conflicts
on `R`, and adding `gamma` conflicts on `S`.  Thus a smaller compatible set
cannot be augmented from a larger one, so the token independence system is
not a matroid.  Since gammoids are matroids, this rules out only a direct
gammoid on these tokens.  The theorem explicitly leaves auxiliary gadget
reductions open.

The cited `2 Delta` independent-transversal criterion is Haxell's standard
theorem.  It is offered only as a conditional corollary; no Boolean menu
size or conflict-degree estimate is asserted.

## 5. Matroid-intersection and Hall audit

For a fixed bank `H_sigma` independent in the colour partition and graphic
matroids, contraction is legitimate.  A common independent extension of
size `U-|H_sigma|` gives a total size-`U` colour-independent set, hence one
representative of every one of the `U` nonempty colour classes.  Graphic
independence is exactly the forest condition.  Edmonds' standard min--max
therefore gives (5.2) with the two complementary rank arguments in the
correct order.

On the deletion side, each component needs one designated deletion and
colour `R` has capacity `b_R`.  Its adjacency to component `K` is exactly
the presence of an `R` occurrence outside the bank in `K`.  Capacitated
Hall yields (5.4), while Hall deficiency is the number of components that
cannot receive a designation.  Any designation extends to the exact colour
quotas because unused deletions need no component upper capacity.  Conversely
one may designate one edge in every component met by a quota deletion set.
This checks the exact deficiency interpretation.

If a rainbow bank contains an entire factor cycle, all its cycle edges have
distinct colours and no one is deletable there.  The singleton component
set then has deficiency one, so the Hall form also detects graphic
dependence before contraction.  The outer minimum in (5.6) is therefore an
exact obstruction.  It is not evaluated or exchanged with the inner
maximum.

## 6. Reserve and profile audit

When a component contains two occurrences of colour `R`, a rainbow bank can
consume at most one of them.  The component remains adjacent to `R` in
every residual omission graph.  Hence `N_R^(2) subseteq N_R^sigma`, and Hall
on these immune incidences implies Hall for every selector.  The menu form
is equally direct: an occurrence outside the entire menu envelope cannot be
used by the selected bank and is an immutable deletion reserve.  Both
criteria are sufficient only.

An `ell`-edge directed path contains exactly `(ell-q+1)_+` directed
`q`-edge intervals.  One interval has one owner union and cannot represent
two distinct rank-`m+q` targets.  Summing over the `Cat_m` components proves
the profile inequality.  The width-two identity subtracts the number of
nontrivial path components, and the top proper layer has `2m-1` targets.
The statement is correctly restricted to `m>=4` for these specializations
and to witnesses lying already in `Q_0`.

## 7. Downstream and global-scope audit

An ordered connector adds edges without deleting `Q_0`, so all selected
old witnesses survive.  A switch that deletes old edges is still governed
by the earlier retained-or-redelivered criterion and is not licensed by the
new theorem.  The monotone pivot remains a downstream transport theorem,
not evidence for the joint occurrence section.

The theorem does not construct or prove:

* a protected all-parameter upper-surjective factor `F`;
* a rainbow independent transversal for the Boolean witness menus;
* running-intersection scopes;
* the multiplicity-two or immutable-reserve Hall inequalities;
* ordered component ports or protected octagon accessibility;
* a depth source antecedent, residence, lower flags, or common cap; or
* `nu(k)<=B(k)+1`.

## 8. Input SHA audit

The hashes copied into the theorem match the exact inputs read:

* `MATH_THEOREM_BPLUS1_ALLWIDTH_RAINBOW_WITNESS_BANK_AND_SAFE_OPENING_20260803.md`  
  `f44ff6af870e6ef188444193e7c1755bb1441832f3a477a11bc0bda0505d5958`
* `MATH_THEOREM_PROTECTED_UPPER_EXACT_CATALAN_FOREST_FORWARD_ATLAS_PULL_ABSORBER_20260803.md`  
  `b2b3c1dcfdcab1338aaffb2783f8a5edc26b8e21a1358e2604696fedaa8333d1`
* `MATH_THEOREM_BPLUS1_PROTECTED_COMPONENT_PORT_HALL_AND_OCTAGON_HAMILTONIZATION_20260803.md`  
  `401aa24568e869909e332c61d222e72d6a0310c585168484e0b30267d6739392`
* `MATH_THEOREM_BPLUS1_CATALAN_HAMILTON_PATH_CERTIFICATE_20260801.md`  
  `a6329c0f3e5f1c7dc5e5ab76338ff52a955f874901e282dc1a17fffae4d7a503`

The theorem SHA at the top of this audit was recomputed only after the
theorem text was frozen.
