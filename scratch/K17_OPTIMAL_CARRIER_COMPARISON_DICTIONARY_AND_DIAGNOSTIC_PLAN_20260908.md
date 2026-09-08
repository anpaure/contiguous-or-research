# The meaningful comparison between the optimal k17 carrier and PBBS

2026-09-09, continuing the 2026-09-08 audit. Pure-proof preparation by
`exact_equality_structure`.
No new mathematical execution is claimed in this note. The proposed
diagnostic compares two specified finite objects; it does not search for
a replacement factor.

## 1. What is and is not available

The [user's construction text](K17_OPTIMAL24313_USER_PROOF_20260908.md)
describes a global search followed by fourteen successor changes and a
lower-letter assignment. Its intermediate factor and original quotient
certificate are not present in that text. Thus the fourteen changes
must not be identified with fourteen changes to canonical PBBS.

The actual optimal literal word is available and independently verified.
[Its two-cycle certificate](K17_OPTIMAL24313_DIRECT_FORWARD_AND_TWO_CYCLE_SEAM_CERTIFICATE_20260908.md)
recovers `Q=A[:85]`, `R=A[86:-2]`; their cyclic triple and four-window
decks are bijections onto the eight- and nine-set layers. The later
[initialized18 certificate](K18_OPTIMAL_INITIALIZED_TWO_CYCLE_STRUCTURE_AND_BYTE_REGENERATION_20260908.md)
uses these same recovered cycles, so it supplies no missing intermediate
search state.

## 2. Recover an unambiguous middle-level factor from the actual letters

For any cyclic component `a_0,...,a_(v-1)`, set

    L_i = a_i union a_(i+1) union a_(i+2),
    U_i = L_i union a_(i+3).

The verified decks imply `|L_i|=8`, `|U_i|=9`, every lower and upper
label occurs once across the bank, and consecutive lower labels differ.
Moreover

    U_i = L_i union L_(i+1).

Thus the literal bank canonically determines two perfect matchings in
the middle inclusion graph:

    M_out(L_i)=U_i,       M_in(L_(i+1))=U_i.              (2.1)

Its lower successor is exactly

    sigma=M_in^(-1) composed with M_out.                 (2.2)

Comparing these functions at a named eight-set is independent of where
a cycle was cut or numbered. Reversing all cyclic words swaps the two
matchings after indexing by the same named lower labels. Therefore the
unordered pair `{M_out(L),M_in(L)}` at each `L` is the orientation-free
incidence comparison. Both orientations must be distinguished from
genuine changes of the underlying middle-level two-factor.

This dictionary is an existing construction language, not a new theorem
of middle-layer existence. See
[the transition-factor reduction](../MIDDLE_LEVELS_TRANSITION_FACTOR_Q1_REDUCTION_20260725.md),
Sections 1 and 3.

## 3. Canonical PBBS in exactly the same gauge

For a stored canonical lower-owner cycle `B_i`, write

    X_i=[17] minus B_i,       F_i=X_i intersect X_(i+1).

The PBBS identities give the two bijective middle decks. The lower
chronology is `F_i -> F_(i+1)`, and the upper vertex between them is
`X_(i+1)`. Hence the correctly aligned native matchings are

    N_out(F_i)=X_(i+1),       N_in(F_i)=X_i.              (3.1)

Using `X_i` as the outgoing upper at `F_i` would silently reverse the
native factor. Comparing literal position `i` in two arbitrarily phased
cycles would be meaningless. The proposed checker uses (3.1) and named
facet labels throughout.

## 4. The temporal and lower-compiler data are also recoverable

Write each actual transition as

    L_(i+1)=L_i minus {d_i} plus {b_i}.

Its entering and departing coordinates are determined by the two lower
labels; `U_i=L_i union {b_i}`. The user's two temporal exclusions are

    b_i != d_(i+1),       b_i != d_(i+2).                (4.1)

Together with the bijective upper deck they ensure that a newly inserted
coordinate stays present in at least four consecutive upper owners:
`U_i,U_(i+1),U_(i+2),U_(i+3)`. It cannot disappear on its own transition,
and (4.1) excludes its next two possible departures. Every nonconstant
positive coordinate run in `U` consequently has length at least four.

Define the maximal envelope

    E_i=U_(i-3) intersect U_(i-2) intersect U_(i-1) intersect U_i.

Coordinate-run erosion and dilation then yield six-element envelope
letters with pair/triple/four-window ranks 7/8/9. The exact identities
and the direction of the time indices must be checked against the
recovered literal word. Each actual `a_i` is automatically a subset of
`E_i`, since it belongs to those four upper windows. The independently
verifiable compiler condition is

    a_i union a_(i+1)=E_i union E_(i+1).                 (4.2)

Equation (4.2) preserves every cyclic interval of length at least two.
It does not follow merely from having a perfect matching in (2.1).
The old PBBS carrier contains short positive runs, so its aperture-three
envelope is not assumed to satisfy the same uniform rank-six model.

## 5. What an exact delta would expose

For any fixed pair of perfect matchings `M,N`, the permutation

    theta=N^(-1) composed with M

decomposes their difference into disjoint alternating cycles. On one
nontrivial theta-cycle, replacing all old `N` edges by the corresponding
`M` edges preserves the perfect-matching constraints exactly. This is
the standard alternating-cycle exchange; it preserves the relevant
middle layer, but by itself need not preserve distinct outgoing/incoming
edges, residence, any lower palette, or upper targets.

The diagnostic can therefore answer concrete questions without an
optimization run:

* Is either actual matching identical to either orientation of the
  canonical PBBS matching?
* How many underlying middle incidences genuinely change, and on which
  canonical height classes?
* Do the exact matching differences break into bounded common-core
  alternating circuits, or into long globally supported circuits?
* Are the recovered matching maps and lower cap assignment equivariant
  under the specified physical coordinate rotation? If so, what are
  their actual quotient rows and shifts?
* Which canonical short-residence transitions have changed, and does
  the actual carrier satisfy both temporal exclusions everywhere?

It is useful to compute both oriented comparisons and the unordered
incidence comparison. An orientation choice alone can produce a large
oriented difference despite leaving the middle two-factor unchanged.

## 6. Existing obstructions and the constructive boundary

[The native full-state obstruction](PBBS_NATIVE_RECENCY_ROUTING_OBSTRUCTION_COMPLETE_AUDIT_20260908.md)
and [its aperture-three version](PBBS_FULL_CAPPED_RECENCY_AND_MATCHING_GRAPH_OBSTRUCTION_20260908.md)
exclude fusion by permutation routing on those unchanged full recency
inventories. They do not exclude changing the middle incidence matchings
and then rebuilding the history.

The [unrestricted triple-cap formulation](PBBS_UNRESTRICTED_TRIPLE_CAPS_COMPLETE_CNF_AND_SPARSE_RUN_CLAUSES_20260908.md)
and its independently checked UNSAT certificate concern the old
canonical chronology, with height-one/two components frozen and every
old rank-eight triple retained. They do not forbid a lower compiler
after changing those triples' chronology.

The older
[chronology-first owner/flag theorem](../MATH_THEOREM_CHRONOLOGY_FIRST_OWNER_FLAG_HALL_AND_PROTECTED_EXCHANGE_20260801.md)
and [fixed-fibre exchange/Hall obstruction](../MATH_THEOREM_R_K17_CHRONOLOGY_FIRST_FLAG_EXCHANGE_AND_FIXED_BORBIT_HALL_OBSTRUCTION_20260801.md)
already explain why an ordinary static matching exchange does not solve
the joint temporal/lower-palette problem. A generic restatement of
alternating-cycle decomposition is therefore not a new all-dimension
construction.

There is also a genuinely positive but narrower existing comparison:
[the canonical mountain C6](PBBS_CANONICAL_MOUNTAIN_C6_ALL_UPPER_TRANSPORT_20260908.md)
replaces three actual lower-owner edges, preserves all local proper upper
support in that exact context, and changes cycles 17+221 into 135+103.
It does not reduce their number. Its
[full-recency star interpretation](PBBS_FULL_RECENCY_STAR_PORT_TRANSPORT_AND_OWNER_ONLY_GATE_20260908.md)
supplies a sufficient common-history transport identity, but not a claim
that every middle matching circuit has such a history. Neither theorem
identifies the supplied optimum's difference from canonical PBBS.

The warranted next step is one exact reconstruction-and-difference
census, with no trial switches. If it finds a uniformly described small
circuit family, those particular circuits can motivate a reusable
exchange lemma with explicit temporal and target-transport hypotheses.
If the difference is global, that fact prevents misrepresenting the
finite optimum as an already discovered local perturbation of PBBS.

No all-dimension exchange rule or construction is claimed at this stage.

## 7. Retained all-dimension constraint on the lower compiler

The successful17 pair-preserving lower assignment is not an all-odd
compiler theorem. If every pair retains rank `r-1` on `2r+1` coordinates,
then each target of rank at most `r-2` must be a literal letter. At19
this needs 94,183 distinct literal targets, more than either the
92,378-position cyclic bank or the 92,381-position exact linear budget.

This is an **existing** obstruction, already proved in
[the one-core normalization audit](../MATH_AUDIT_AD_ALL_ODD_COMPILER_ONECORE_NORMALIZATION_20260729.md),
Section5, and
[the three-level chainization audit](../MATH_AUDIT_K_K17_THREE_LEVEL_NORMAL_CHAINIZATION_20260802.md),
Section7. It is retained here to delimit the proposed comparison's use:
even a reusable middle-carrier exchange must be coupled to a
pair-changing lower compiler for a general exact construction.
