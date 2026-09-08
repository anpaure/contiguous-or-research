# Exact two-sided lift and its coupled recency-state compiler

Date: 2026-09-08. Pure proof by `exact_b_induction`.

Status: the complete finite criterion and explicit witness compiler below
are proved. No mathematical execution or finite search was performed.
This is a reusable extension of the exact one-seam criterion, not a new
attaining word. In particular, the already established transition bound
rules out this entire two-sided architecture for an optimal19 word.
Further exact19 work must allow extensively interleaved coordinates;
no one- or two-seam19 search is proposed here.

## 1. Construction and relation to earlier endpoint lifts

Let X be a nonempty alphabet, A a universal word on X of length m,
and z a new coordinate. Let L and R be arbitrary old-projection words,
possibly empty. Their individual letters may also be empty, since they
will be marked with z. Consider

    V=mark_z(L) || {z} || pi(A) || {z} || mark_z(R),       (1.1)

where pi is one permutation of X applied to the entire middle word and
mark_z adjoins z to every letter. Its length is

    m+2+|L|+|R|.                                        (1.2)

All z-free targets remain in the universal middle word. For an odd old
dimension, if m=W+t and |L|+|R|=W-2, its length is 2W+t. This budget
calculation is not an existence theorem for suitable tails or states.

`FINITE_LIFT_SLACK_THEOREMS_AUDIT_20260724.md`, Sections 2–3, already
proves the ordinary trimmed lift and its one-ended chain compression.
Section 4 proves a two-ended chain construction with one marked tail
possibly empty, and Section 11 gives the general tagged interval-cover
criterion. The result here removes endpoint-chain assumptions and gives
an exact coordinate-assignment criterion for BOTH seams of (1.1), while
retaining their coupling through the single pi.

## 2. The exact tagged target deck

Write Cov(L), Cov(R) for the nonempty ordinary interval ORs in the tails.
Every tagged interval either lies inside a tail, crosses one bridge,
or crosses both bridges. An interval crossing both contains all of pi(A)
and therefore has old projection X. Intervals crossing only the left
bridge have projection

    S union P,  S in Suf_0(L), P in Pref_0(pi(A)),

and those crossing only the right bridge have projection

    C union T,  C in Suf_0(pi(A)), T in Pref_0(R).

The subscript zero permits an empty suffix or prefix. The full target
X is already supplied by a full prefix or suffix of pi(A), so the exact
nonempty old projection deck is

    Cov(L) union Cov(R)
    union (Suf_0(L) vee Pref_0(pi(A)))
    union (Suf_0(pi(A)) vee Pref_0(R)),                   (2.1)

with the empty projection separately supplied by either pure bridge.
Here vee denotes all unions of one member from each family, and any
empty output in (2.1) can simply be ignored.

Define the defects

    Dcal=(2^X minus {empty}) minus (Cov(L) union Cov(R)).

For each D in Dcal, let T_L(D) be the union of the longest suffix of L
all of whose letters are subsets of D, and let T_R(D) be the union of
the analogous longest prefix of R. Put

    U_L(D)=D minus T_L(D),
    U_R(D)=D minus T_R(D).

Both U_L(D) and U_R(D) are nonempty for a genuine nonempty defect:
equality to the empty set would already give a suffix or prefix witness
inside its corresponding tail.

**Exact two-seam criterion.** V is universal if and only if every D in
Dcal satisfies at least one of

    there exists P in Pref_0(pi(A)) with U_L(D) subseteq P subseteq D;
    there exists C in Suf_0(pi(A)) with U_R(D) subseteq C subseteq D.
                                                               (2.2)

The proof is the same maximal-compatible-tail argument on each side:
in any left seam witness its tail suffix is contained in T_L(D), hence
the middle prefix must contain U_L(D), and conversely its union with
T_L(D) is D. The right side is identical under reversal. A full defect
D=X has no excluded coordinate and can use the full middle word. Empty
tails give T=empty and require an exact middle prefix or suffix.

A proper D cannot be repaired by combining pieces of BOTH seams: the
interval connecting them contains the whole universal middle word and
has old projection X. The disjunction in (2.2) is per TARGET, not per
coordinate of that target.

## 3. The precise coupling between the two coordinate orders

Let E_1,...,E_p be the nonempty increments of the distinct prefix-union
chain of A, in first-seen order. Let F_1,...,F_q be the nonempty increments
of its suffix-union chain, in most-recent-first order. Define the exact
joint incidence matrix

    h_(i,j)=|E_i intersect F_j|.                         (3.1)

Its row sums and column sums are the separate prefix and suffix size
profiles. Under a common permutation pi the whole matrix is unchanged.
Conversely, ordered partitions (P_1,...,P_p) and (Q_1,...,Q_q) of X arise
as (pi(E_i)) and (pi(F_j)) under some ONE pi if and only if

    |P_i intersect Q_j|=h_(i,j) for every i,j.            (3.2)

Necessity is immediate. For sufficiency, choose any bijection from each
source cell E_i intersect F_j to its equal-sized target cell P_i intersect
Q_j and combine these disjoint bijections. This explicitly constructs pi.

The two separate marginal profiles are not sufficient. For the universal
two-coordinate word ({a},{b}), the prefix blocks are ({a},{b}) and suffix
blocks ({b},{a}); the matrix is anti-diagonal. Assigning both target
orders to ({a},{b}) respects each separate size profile but cannot be
obtained by any single permutation of that word.

This is also the proper equivalence criterion for different endpoint-cap
representatives. Equal cap sizes suffice at one seam, as proved in
`scratch/EXACT_ONE_SEAM_LIFT_PRECEDENCE_AND_ENDPOINT_CAP_THEOREM_20260908.md`.
For two seams, the entire ordered matrix (3.1) must agree. Two caps of the
same size can interact differently with the opposite endpoint blocks,
so their marginal sizes alone do not justify collapsing them.

## 4. Complete disjunctive precedence theorem

For each D in Dcal choose one side, LEFT or RIGHT. For LEFT defects build
a graph G_L with arcs

    x -> y for every x in U_L(D), y in X minus D.

For RIGHT defects build G_R analogously using U_R(D). A coordinate's
prefix index refers to its block P_i, and its suffix index to Q_j.

**Theorem.** There exists a permutation pi making (1.1) universal if and
only if there exist such side choices and two ordered partitions P,Q
satisfying the exact joint counts (3.2), with

    prefix_index(x)<prefix_index(y) for every arc of G_L,
    suffix_index(x)<suffix_index(y) for every arc of G_R. (4.1)

**Proof.** For any fixed side, the corresponding alternative in (2.2)
holds exactly when all its required coordinates enter the relevant chain
strictly before every excluded coordinate. Choose the prefix ending at
the largest required index; it then contains the required set and avoids
all exclusions. Conversely any successful chain prefix supplies that
strict boundary. Ties between a required and an excluded coordinate are
not allowed. If D=X there are no exclusions and its constraint is vacuous.

Thus a successful pi gives a valid side choice for each defect and gives
the partitions in (4.1). Conversely the side choices and partitions
supply a pi by (3.2). For a LEFT target take the actual longest compatible
L-suffix, the first bridge, and the actual middle prefix whose union ends
at the largest required prefix index. Their union is D union {z}.
For RIGHT use the corresponding middle suffix, second bridge and R-prefix.
These are ordinary contiguous witnesses. Every nondefect is covered in
a marked tail, {z} is explicit, and every old target remains in pi(A).
This proves sufficiency with all witness types accounted for. QED.

The conjunction of all arcs for a given defect must be assigned to one
side together. Replacing this by a separate LEFT-or-RIGHT choice for each
individual arc would be an unsound relaxation.

## 5. A complete finite decision and literal compiler

The theorem gives the following finite complete procedure; no execution
of it is claimed here.

1. Enumerate whole-target side assignments and form their two graphs.
   A directed cycle in either chosen graph rules out that assignment.
2. Enumerate the ordered prefix partitions with row sizes sum_j h_(i,j),
   by taking each entire next block from the current G_L-minimal vertices.
   Remove the selected block simultaneously, as in the one-seam theorem.
3. For each such prefix partition, build the suffix blocks successively.
   At suffix step j choose from the current G_R-minimal vertices exactly
   h_(i,j) members lying in P_i for EVERY i. Remove their union as Q_j
   and recurse until every column has been assigned.
4. On success construct the cellwise pi from Section 3, then the literal
   word and the witnesses from Section 4.

Every valid pair of partitions follows one branch of this procedure:
its next block has no incoming arc from any remaining coordinate, and
its intersections have the prescribed counts. Conversely, every completed
branch has the strict graph inequalities and exact cell counts. This
proves completeness of both a success and an exhausted negative decision
within the specified tails and base matrix.

Unlike the special one-seam profile with an all-singleton remainder,
arbitrary adequate choices in Step 3 need not be safe. Later columns have
prescribed row capacities, so different choices can leave different future
feasibility. Backtracking over all permitted choices is required unless a
separate argument proves it unnecessary. Two separately feasible graphs
also do not suffice without the joint matrix constraints.

## 6. The already known obstruction for the next exact dimension

The new literal certificate establishes nu(18)=48623. The existing
entrance/exit theorem already used the lower bound B(18)=48623 to prove
that any universal19 word of length B(19)=92381 requires at least 541
entrances and 541 exits for EACH coordinate. This value was already
recorded in
`scratch/EXACT_B_ENTRANCE_EXIT_CAPACITY_AND_INDUCTION_OBSTRUCTION_20260908.md`,
Section 5; it is not a new consequence first made available by attainment.
The initialized-extension/interleaving proof is restated in
`scratch/INITIALIZED_RECENCY_EXTENSION_INTERLEAVING_AND_K18_LOWER_BOUND_AUDIT_20260908.md`.

For the new coordinate z, (1.1) has exactly one marked-to-unmarked
transition and one unmarked-to-marked transition, regardless of either
tail's size, either endpoint cap, or the permutation. Taking rank10 in
the earlier exit inequality yields

    binomial(18,9) <= (N-nu(18))+9,
    N >= 48620+48623-9=97234.                            (6.1)

Therefore NO word of the form (1.1), with any universal18 middle word
and arbitrary tails, can attain 92381. This is a scoped corollary of the
older transition theorem, not a new lower bound on unrestricted nu(19).

An all-marked appended extension is even constrained by
Ext_z(A)>=W(18), giving total length at least

    nu(18)+W(18)=97243.

The exact two-sided criterion remains useful in other dimensions or for
other length targets, but it cannot be presented as a surviving exact19
construction route. Any successful all-dimensional equality mechanism
must allow the required extensive interleaving; neither fixed arbitrary
tails nor a more flexible relabeling removes this chronology constraint.

## 7. Status

This note proves an exact finite constructive compiler conditioned on
explicitly satisfiable graph and cell-count constraints. It does not
claim those constraints are satisfiable for a new source, and it does
not authorize a broad search. Its contribution beyond the prior
endpoint-chain sufficient conditions is the complete whole-target
disjunction and the exact coupling matrix for the same relabeling at
both seams. The separate exact19 obstruction is attributed to the
already established entrance/exit theorem.
