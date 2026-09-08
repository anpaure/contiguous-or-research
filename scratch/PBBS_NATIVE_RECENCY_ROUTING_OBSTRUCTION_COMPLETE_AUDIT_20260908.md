# Complete audit of the native PBBS recency-routing obstruction at k=17

2026-09-08. Independent proof and one bounded exact h100 census by
`exact_equality_structure`.

**PASS.** The unchanged native D^h bank has 24,310 distinct periodic
recency states in 146 components. The complete graph of legal neutral
(same-height) transitions has precisely the native edges, self-loops,
and 17 additional edges from canonical cycle 83 to canonical cycle 103.
These components have height three and periods 153 and 85, respectively.
There is no reverse edge and no additional same-component edge.

Every legal permutation routing on this fixed state inventory stays
within the original components. Its minimum component count is 146,
and the native routing is the unique routing with no self-loops.
This is an obstruction to rerouting these unchanged states, not a
lower bound excluding a shorter word with different recency states.

The submission being checked is transcribed in
[ROTATION_PERIOD_ADVANCE_USER_CLAIMS_20260908.md](ROTATION_PERIOD_ADVANCE_USER_CLAIMS_20260908.md),
last section. This audit does not certify that submission's separate
translated-return, period-formula, or partition-census claims.

## 1. Exact state and source conventions

At an endpoint the recency state is the ordered partition

    P=(B_0|B_1|...|B_t),

of the seen physical coordinates by last occurrence, most recent first.
Its prefix unions are exactly the distinct suffix ORs at that endpoint.
Appending a nonempty physical letter F gives

    T_F(P)=(F|B_0 minus F|B_1 minus F|...|B_t minus F),   (1.1)

with empty blocks removed. This is the exact theorem in
[MASTER_HANDOFF.md](../MASTER_HANDOFF.md), Section 1.2. In particular
an edge into a specified destination state Q must append its first
block F=Q_0. There is no alternative letter to test for that edge.

Use each original canonical g=f^2 cycle A_i of lower owners, its
complementary upper owners X_i, and its actual invariant height h.
The native literal word is

    D_i^h=intersection_(j=0)^h X_(i+j).                  (1.2)

Here h is NOT replaced by min(h,3). Source identities, residence, and
cyclic reconstruction are proved in
[the height-adaptive finite-word audit](PBBS_HEIGHT_ADAPTIVE_FINITE_WORD_AND_RANGE_BOUND_INDEPENDENT_AUDIT_20260908.md),
Sections 1–3, and
[the aperture/rank interface](PBBS_CAPPED_APERTURE_EXACT_MIDDLE_AND_LOWER_PIN_INTERFACE_20260908.md).

The input is the original
[canonical cycle data](k17_height_adaptive_20260908/height_adaptive_canonical_cycles.json),
with SHA-256

    fed20c313c639740b089428c1d2b8b572fc7138de4c11c2203be554e4acfa2a3.

No source cut, coordinate, orientation, period, or owner was changed.
The exact census independently reconstructs (1.2) from these owners
and checks it against every stored source letter.

## 2. Native states have unique middle labels and a fixed initial shape

At endpoint i of a native height-h period, the suffix windows of
lengths 1,...,h+1 have ranks

    9-h, 10-h, ..., 8, 9.

They therefore give the initial recency block sizes

    9-h, 1, 1, ..., 1,                                  (2.1)

where h singletons follow the first block through rank nine. In
particular the number b_9 of prefix targets strictly below rank nine
is h. It is a count of distinct recency prefixes, not a claim about
all intervals of a given length.

The rank-nine prefix at this endpoint is X_i, and the rank-eight
prefix is

    X_i intersect X_(i+1)=f(A_i).                        (2.2)

The g cycles partition the lower middle layer, complementation
bijects it to the upper middle layer, and f is a bijection. Hence
every rank-nine prefix and every rank-eight prefix appears exactly
once in the full native inventory. These facts also imply that the
recency states themselves are distinct.

The finite checker verifies the full shape (2.1), both identities
(2.2), and both 24,310-element prefix bijections directly from the
periodic words. It uses a full period to initialize all last
occurrences before storing any states, so empty-start transient
states are not mistaken for native periodic states. A separate
physical last-occurrence calculation replays every recorded state.

## 3. Height cannot increase along an edge to a different native state

The following argument is elementary and does not assume a general
rank-potential theorem.

Let P,Q be different states in the native inventory. Write
d_P=9-h_P and d_Q=9-h_Q for their first-block sizes, and let F=Q_0
be the uniquely possible appended letter. Assume T_F(P)=Q.

First observe that if F is contained in P's rank-nine prefix M_P,
then M_P is still a recency prefix after the update. Indeed F is
moved to the front, and the remaining parts of the original blocks
through M_P follow it before any coordinate outside M_P. Their union
is exactly M_P. Uniqueness of the rank-nine label in the inventory
would then imply Q=P. Thus for an edge between different states,

    F is not a subset of M_P.                           (3.1)

Suppose h_Q>h_P, equivalently d_Q<d_P. The old first block P_0 has
a nonempty remainder P_0 minus F, and this is the first block after
F in T_F(P). By (2.1), that destination block must be a singleton.
If d_Q<=d_P-2 its remainder has size at least two, contradiction.
If d_Q=d_P-1, the singleton remainder forces F to consist of all
but one coordinate of P_0; in particular F subset P_0 subset M_P,
contradicting (3.1). Consequently

    h_Q<=h_P for every edge between different native states.   (3.2)

Self-loops trivially preserve height. Every directed cycle therefore
has constant height: a finite closed nonincreasing height sequence
cannot contain a strict decrease. This excludes all cross-height
edges from every cyclic permutation of the inventory. Their complete
enumeration is unnecessary and is not claimed by the census.

There is also a more general prefix-count proof, independently supplied
by the root audit. List P's prefixes strictly below rank nine as
U_1,...,U_h and its next prefix as U_(h+1)=M_P. Include U_0=empty.
Every prefix after appending F is one of F union U_j, after duplicates
are removed. If the destination's rank-nine prefix M_Q differs from
M_P, its least such index j satisfies j<=h: for j>=h+1 it would contain
M_P and hence equal it. Before that prefix there are at most j distinct
small prefixes, represented by F union U_0,...,F union U_(j-1).
Thus b_9(Q)<=j<=b_9(P). In the neutral case equality forces j=h,
so U_h is contained in M_Q. On the native inventory U_h has rank eight.
This proves both monotonicity and the next section's containment
without needing the native first-block sizes. Uniqueness of the
rank-nine state label makes every non-self edge a different-label edge.

## 4. The nine-subset neutral predecessor test is exhaustive

Suppose now h_Q=h_P=h, and again first take P!=Q. The equal sizes
|F|=|P_0|=9-h imply that F=P_0 would give the self-loop P. Hence
P_0 minus F is nonempty. As above, it must be the singleton second
block of Q. Therefore F replaces exactly one coordinate of P_0 by
exactly one new coordinate z. By (3.1),

    z is outside M_P.                                   (4.1)

Let R_P be P's rank-eight prefix. It consists of P_0 and the next
h-1 singleton blocks. Since z is outside M_P, it removes none of
these singletons. In the updated state the prefix through rank nine
is exactly

    M_Q = F union R_P.                                  (4.2)

The old first-block remainder contributes one coordinate and the
next h-1 singleton blocks contribute the others, so its rank is
nine. Equation (4.2) proves

    R_P is an eight-subset of M_Q.                      (4.3)

For P=Q the containment (4.3) already holds. Thus every neutral
predecessor, INCLUDING the self-loop, occurs among the nine states
whose rank-eight prefixes are the nine eight-subsets of M_Q.
The rank-eight bijection supplies exactly one state for each such
subset. Discarding candidates of different height and testing (1.1)
with F=Q_0 is therefore a complete decision, not a restricted search.

Containment is only a necessary filter. The census tests equality of
the ENTIRE updated ordered partition to Q; matching one or both
middle prefixes alone is not accepted as a legal edge.

The proofs in Sections 3–4 also apply abstractly to any finite
inventory with unique rank-s labels and initial block sizes s-h
followed by h singletons: replace 9 and 8 by s and s-1. They do not
rely on a k=17 numerical coincidence.

## 5. One complete bounded reconstruction and edge census

The standalone checker is
[audit_k17_native_recency_neutral_graph_20260908.py](audit_k17_native_recency_neutral_graph_20260908.py).
It was run once on h100 (`arboghast`), with hard limits of 120 CPU
seconds, 150 wall seconds, and 2 GiB address space. It returned PASS
in approximately 1.94 seconds. No mathematical program ran locally.

It performs these logically separate checks:

1. Reconstruct every native D^h letter from the unchanged owners and
   check the stored source period.
2. Reconstruct all cyclic steady recency states by exact updates,
   and independently replay them from coordinate last-occurrence
   times. Check shape, owner/facet identities, distinctness, and
   every original successor edge.
3. Generate every candidate in Section 4. For each same-height
   candidate, compare the literal move-to-front result with an
   independent implementation that groups each physical coordinate
   by its new recency class. Test the whole destination state.
4. Classify every accepted edge as a self-loop, native edge,
   additional internal edge, or cross-component edge. Construct the
   component quotient and an explicit topological ordering.

The exact result is:

| Quantity | Count |
|---|---:|
| Original components | 146 |
| Periodic recency states | 24,310 |
| All nine-subset candidates | 218,790 |
| Candidates with unequal height, discarded | 131,818 |
| Complete neutral candidates tested | 86,972 |
| Rejected neutral candidates | 38,335 |
| Legal neutral edges | 48,637 |
| Native edges | 24,310 |
| Self-loops | 24,310 |
| Additional same-component edges | 0 |
| Cross-component edges | 17 |

All 17 cross-component edges have source cycle 83 and destination
cycle 103 in the original zero-based canonical numbering. Both
heights are three; their periods are respectively 153 and 85. There
are no other edges in the neutral component quotient. Its explicit
state-level edge list and topological order are saved below.

## 6. Complete cyclic-routing obstruction

A legal cyclic permutation assigns every inventory state exactly
one legal successor and exactly one predecessor. Its components
are directed cycles, possibly self-loops. By Section 3 each such
cycle has constant height. On contracting the original PBBS
components, its nontrivial steps would give a closed directed walk
in the neutral component quotient. The saved quotient is acyclic,
so no routing cycle can cross between original components.

Within one original component v_0,...,v_(m-1), the complete census
leaves only

    v_i -> v_i,       or       v_i -> v_(i+1 mod m).     (6.1)

In a permutation these choices cannot be mixed. If v_i takes its
self-loop, v_(i-1) cannot use its native edge into the already
occupied vertex and must also loop; this propagates around the
component. Equivalently, if any native edge is selected, the
indegree condition forces every edge of that original cycle.

Thus each original component is either its one native cycle or
all of its vertices are individual self-loops. There are 146
original components and every period is at least 17. The minimum
routing-component count is exactly 146, attained by keeping every
native cycle. If self-loops are forbidden, that routing is unique.

This proves the submitted obstruction in full for the fixed k=17
inventory. It rules out zero-extra cyclic fusion that preserves all
these recency states. It does not rule out changed letters/states,
a different owner chronology, caps, added transient states, or a
separately proved linear splice. No new shorter literal word is
claimed here. No analogous census at k=7,9,...,19 was rerun.

## 7. Complete reproducibility artifacts

Local directory:
[k17_native_recency_graph_20260908](k17_native_recency_graph_20260908/).

* [Full certificate](k17_native_recency_graph_20260908/native_recency_routing_certificate.json).
* [Every native periodic state](k17_native_recency_graph_20260908/native_periodic_states.json).
* [Every same-height candidate, including rejected candidates](k17_native_recency_graph_20260908/complete_neutral_candidates.csv).
* [Every legal neutral edge](k17_native_recency_graph_20260908/complete_neutral_legal_edges.csv).
* [Complete neutral component quotient and all 17 extra edges](k17_native_recency_graph_20260908/native_neutral_component_quotient.json).

The candidate CSV has SHA-256

    0d9e77022ef32e31e406d76d70670f0cf33c8e52896ed649e5f7d5ca962bd559,

and the legal-edge CSV has SHA-256

    df84d767f06043608dc2b1b962358033465b4100e6a8fcb92095747e372e6478.

The report records hashes and byte counts for all exported large
artifacts. Remote source and output remain at

    h100:/home/amodo/exact-b-k17-native-recency-20260908/

The complete same-height graph is explicitly exported. The absence
of cross-height edges from cyclic routings is a mathematical
consequence of Section 3; it is not being inferred from an
unperformed all-pairs edge scan.
