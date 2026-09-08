# Exact pair-union replacement with binary host choices

Date: 2026-09-08.
Status: proved finite constructive specialization; no new value of nu(k), and no all-dimension host supply is claimed.

## 1. Why this is a different finite gate

Master Handoff 3.10 fixes a word of envelopes E and first fixes a smaller core C with DC=DE. It then uses a matching to choose letters between C and E. Fixing C in advance makes all choices compatible, but can unnecessarily remove potential hosts. The theorem below instead permits simultaneous adjacent replacements and tests their compatibility exactly. It pays zero extra letters. If every demanded target has at most two allowed host positions, the remaining selection problem is 2-SAT, rather than the general higher-order common-cap problem.

This is only a tractable special case of the compiler. In particular, it does not assert that suitable hosts exist in the unresolved k=17 carrier.

## 2. Setup and complete host definition

Let E=(E_1,...,E_n) be a linear word of nonempty subsets of a finite universe. For 1<=i<n set U_i=E_i union E_{i+1}. Let L be a family of distinct nonempty target sets. A position i is a legal host for S in L when

1. S is a subset of E_i;
2. if i>1, E_{i-1} union S = U_{i-1}; and
3. if i<n, S union E_{i+1} = U_i.

Thus installing S at i, with every other letter left unchanged, preserves every adjacent pair union. For a cyclic word, require the analogous two equations at every position, with indices modulo n. The cyclic version below is stated for n>=3; a period-one or period-two word can be checked separately.

For each S choose a nonempty subdomain D(S) of its legal hosts, with |D(S)|<=2. This domain is supplied data. The theorem is exact for the supplied domains; restricting a larger domain to two choices can discard valid solutions.

A selected option is a pair (S,i), i in D(S). Two selected options belonging to distinct targets are incompatible precisely in either of the following situations:

- they name the same position;
- they name adjacent positions i,j, and S union T differs from E_i union E_j.

All those conflicts are pair conflicts. Options belonging to one target are handled by its exactly-one choice.

## 3. Exact theorem

There exists an injective assignment f:L -> {1,...,n}, with f(S) in D(S), such that replacing E_{f(S)} by S preserves every adjacent pair union, if and only if there is a choice of one option per target containing no incompatible pair.

With at most two options per target, this is a 2-SAT instance. One Boolean variable chooses the host of each target having two hosts. A one-host target has a fixed option. Every incompatible option pair gives the clause forbidding their simultaneous selection. A conflict with a fixed option becomes a unit clause; two incompatible fixed options give immediate infeasibility. Therefore this finite compiler can be decided and constructed by strongly connected components of its implication graph.

### Proof

Necessity is direct. Distinct target labels cannot be installed at the same position. Two adjacent installed labels must have the required original pair union.

For sufficiency, define A_i to be its assigned target if i was selected, and E_i otherwise. All letters are nonempty, and every target in L is witnessed by its selected one-letter interval.

Consider any adjacent pair. If neither position is selected, the pair is unchanged. If exactly one position is selected, the legal-host condition preserves its pair union. If both positions are selected, absence of the corresponding incompatible pair preserves it. These cases exhaust all pairs, so DA=DE.

For any linear interval [a,b] with a<b,

    union_{j=a}^b A_j = union_{j=a}^{b-1} (A_j union A_{j+1})
                       = union_{j=a}^{b-1} (E_j union E_{j+1})
                       = union_{j=a}^b E_j.

Thus every interval with at least two letters has exactly its original union. The same identity holds for a cyclic interval of length between two and the period, using its consecutive cyclic edges. This proves the claimed physical realization.

For the 2-SAT assertion, one option for a two-host target is the positive literal of its variable and the other is the negative literal. Forbidding simultaneous options l and l' gives (not l OR not l'). The preceding equivalence proves that satisfying assignments are exactly the desired physical replacements. The standard implication-graph criterion is constructive: a formula is satisfiable exactly when no variable and its negation lie in the same strongly connected component; ordering the acyclic component quotient supplies a satisfying assignment. No marginal matching or fractional relaxation is used. QED.

## 4. Exact all-target corollary and length charge

Suppose every required target outside L already has a witness of length at least two in E. If the 2-SAT instance is satisfiable, A is universal on the requested target family and has exactly n letters. In particular, if the requested family is every nonempty subset of [k], n=B(k), and the independent monotone-deadline lower bound is available, then

    nu(k)=B(k).

The premise includes every target outside L. A target witnessed only as an original single letter is not protected merely by DA=DE. Such a target must either be added to L or supplied with a separate preserved witness. This is particularly important for the envelope-rank targets in Master 3.10.

For k=17, a possible use with rank-six envelopes would take L to contain all nonempty targets of rank at most six, and require E already to realize every rank-seven-or-higher target in a multi-letter interval. An optimal-length linear E would have n=24313. A satisfying binary-host instance would then give an actual 24313-letter word, with no joining, repair, or asymptotic charge. None of these source/existence premises is supplied by the present lemma.

The cyclic version only gives a cyclic word. It does not pay for a linear opening. Any use for nu(k) must charge or prove a safe opening independently.

## 5. Simultaneous freedom, and a sharp limitation

The lemma permits adjacent proper shrinkages. For example, with two original letters both {a,b,c,d}, installing {a,b} and {c,d} preserves their pair union. A rule allowing only isolated modified positions would reject this valid move.

Ordinary Hall alone still does not suffice. Take two positions, both originally {a,b,x}, and demand the two distinct letters {a},{b}, each with both positions as legal hosts. Every individual installation preserves the one protected pair, and the host graph is K_{2,2}. Any injective simultaneous installation loses x from that pair. The 2-SAT formula is unsatisfiable. This is an obstruction to this supplied finite source, not to unrestricted OR words.

The binary-domain condition is substantive. With three or more choices per target, the option-conflict description remains exact, but exactly-one target clauses need not have width two. No polynomial general compiler follows.

Nor does this repair the all-k problem by itself: preserving all pair unions forces every target smaller than every U_i to be a single letter. At most n such distinct targets can then be covered. A source whose required lower ideal has more than n elements must allow some pair unions to change, use longer lower witness cells, or otherwise change its architecture.

## 6. Current constructive frontier and the correct recursive input

The exact k16 result is documented in:

- MATH_CERTIFICATE_K16_OPTIMAL_12873_TRUEFF_COMMONCAP_20260731.md;
- MATH_THEOREM_MASTER_STAIRCASE_PINNED_COMMON_CAP_COMPILER_20260731.md; and
- MATH_THEOREM_GUARDED_CONVEX_LAMINAR_COMMON_CAP_COMPILER_20260731.md.

It uses an endpoint-rerooted four-filter carrier, a legal variable staircase and singleton pin, and one simultaneous common-cap assignment. The final word, rather than solver statistics, is the positive certificate.

The useful all-dimension recursive interface is in:

- MATH_THEOREM_DIMENSION_UNIFORM_PASCAL_SHADOW_BRAID_INDUCTION_20260731.md; and
- MATH_THEOREM_ZERO_DEFECT_PASCAL_PARTICLE_BRAID_INDUCTION_20260731.md.

A parent optimal word alone is not the recursive invariant. The child must regenerate one common occurrence-labelled object having exact middle ownership, complete all-width upper witnesses, valid coordinate residence and nonempty envelopes at its optimum-length schedule, and simultaneous lower-target realization. The existing Pascal arithmetic and component-neutral insertion ledger do not supply this joint object.

A concrete k17 owner-connected source is documented in MATH_THEOREM_K17_OPT28_CONNECTED_OWNER_FACTOR_AND_NONFLAT_RESIDUAL_20260731.md and its independent audit. That source has a complete immediate lower palette, but its nonflat row has 2392 strict short-run defects, 3568 maximal-envelope replay mismatches, and upper holes of counts 1900,911,128 at ranks 10,11,12. A downstream cap solver cannot restore those missing protected bits or upper witnesses. It would be premature to feed that source directly to this lemma or to the general common-cap compiler.

These observations identify two separate constructive tasks: first construct a source that already meets its protected-row and upper-coverage premises; then solve its physically coupled lower compiler. The present theorem gives an exact small-domain method for a special case of the second task. It does not settle the first task or the all-dimension supply theorem.
