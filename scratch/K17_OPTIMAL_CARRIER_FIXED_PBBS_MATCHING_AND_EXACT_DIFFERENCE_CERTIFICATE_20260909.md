# The optimal k17 carrier preserves one PBBS matching exactly

2026-09-09. Independent reconstruction, proof, and one bounded exact
comparison by `exact_equality_structure`. Root read the entire diagnostic
before authorizing the single execution. **PASS.**

The supplied optimum does not replace both middle-layer matchings.
Its outgoing eight-set/nine-set matching is exactly canonical PBBS on
all 24,310 physical labels. Only its incoming matching changes.
This identifies a strictly smaller concrete construction space for
further work: retain the PBBS root-addition matching and change the
complementary perfect matching, then rebuild and compile the resulting
history. It does not prove that such a construction succeeds in all
dimensions.

## 1. Sources and phase-independent definitions

The exact source word is
[k17_optimal24313.word](../answers/k17_optimal24313.word), SHA-256

`7d85f8494084c7eb3f4b196159f3a5b5b020a0170e26ad0e34c6087bda525ff9`.

Recover `Q=A[:85]` and `R=A[86:-2]`, of periods 85 and 24,225.
The [independent literal certificate](K17_OPTIMAL24313_DIRECT_FORWARD_AND_TWO_CYCLE_SEAM_CERTIFICATE_20260908.md)
establishes their full cyclic coverage and their middle-layer bijections.
The later [exact18 reconstruction](K18_OPTIMAL_INITIALIZED_TWO_CYCLE_STRUCTURE_AND_BYTE_REGENERATION_20260908.md)
uses these same recovered cycles.

For either cyclic literal word `a`, define

    L_i=OR(a_i,a_(i+1),a_(i+2)),
    U_i=OR(a_i,a_(i+1),a_(i+2),a_(i+3)).                 (1.1)

Every `L_i` is an eight-set, every `U_i` a nine-set, and each layer is
enumerated once across both cycles. Moreover `U_i=L_i union L_(i+1)`.
Thus two perfect inclusion matchings and the successor are recovered:

    M_out(L_i)=U_i,
    M_in(L_(i+1))=U_i,
    sigma=M_in^(-1) composed with M_out.                 (1.2)

The comparison uses the physical eight-set mask as its key. It is
unaffected by the chosen cut position or component numbering.

The canonical input is
[height_adaptive_canonical_cycles.json](k17_height_adaptive_20260908/height_adaptive_canonical_cycles.json),
SHA-256

`fed20c313c639740b089428c1d2b8b572fc7138de4c11c2203be554e4acfa2a3`.

For its stored lower-owner cycle `B_i`, put `X_i=[17] minus B_i` and
`F_i=X_i intersect X_(i+1)`. Its matchings in the same forward gauge are

    N_out(F_i)=X_(i+1),       N_in(F_i)=X_i.              (1.3)

The explicit gauge derivation and earlier obstructions are recorded in
[the comparison plan](K17_OPTIMAL_CARRIER_COMPARISON_DICTIONARY_AND_DIAGNOSTIC_PLAN_20260908.md).

## 2. Exact fixed-matching result

The full named-label comparison establishes

    M_out(L)=N_out(L)   for every eight-set L.            (2.1)

For the other matching,

    number of unchanged incoming rows = 6732,
    number of changed incoming rows   = 17578.          (2.2)

At all 6,732 unchanged rows both unordered middle incidences agree;
at every other row exactly one incidence agrees. No lower vertex loses
both of its old incidences. There are exactly 31,042 common undirected
middle incidences in the two factors. The successor agrees with the
native forward successor at 6,732 lower labels as well.

The changed incoming rows, grouped by their original PBBS component
height, are:

| Native height | Changed physical lower labels |
|---:|---:|
| 1 | 17 |
| 2 | 1241 |
| 3 | 5831 |
| 4 | 6018 |
| 5 | 3247 |
| 6 | 1003 |
| 7 | 204 |
| 8 | 17 |

These are changes in the given physical coordinate labeling. No search
over coordinate permutations or alternative PBBS conventions was made.

## 3. What the fixed matching means constructively in any odd dimension

For `n=2r+1`, let `f` be the canonical PBBS step and `u(L)` the cyclic
unmatched zero of an r-set `L`. Then

    f(L)=L^c minus {u(L)},
    Phi(L)=f(L)^c=L union {u(L)}.                        (3.1)

In (1.3), `F_i=f(B_i)` and the next lower owner is `f^2(B_i)`.
Therefore `N_out(F_i)=f(F_i)^c=Phi(F_i)`.
The actual optimum's fixed matching in (2.1) is precisely this
canonical root-addition matching.

Once `Phi` is fixed, an admissible middle carrier is specified by a
permutation `sigma` of the r-sets satisfying

    sigma(L)=Phi(L) minus {d(L)},       d(L) in L.        (3.2)

The deletion restriction excludes `sigma(L)=L`. It guarantees that
the lower sets and the upper colors `Phi(L)` are each used once.
Conversely every loop-free middle factor containing `Phi` and oriented
along it has this form.

The candidate bipartite successor graph in (3.2) is r-regular on both
shores: it is the middle inclusion graph with the perfect matching
`Phi` removed, after identifying each upper vertex with its unique
`Phi`-preimage. Thus selecting one complementary perfect matching
always gives a legitimate middle two-factor. **The existence of such
a perfect matching alone says nothing about its temporal or all-rank
coverage properties.**

This fixed-matching language is already present in earlier work. The
new finite finding is that the supplied successful carrier lies in
this restricted family exactly, rather than requiring both matchings
to vary. Accordingly a search for an all-dimensional mechanism need
not first generalize the root-addition matching itself.

## 4. The actual incoming difference, without hypothetical switch trials

Let

    theta=N_in^(-1) composed with M_in.

Its nontrivial cycles are the exact disjoint alternating circuits
between the two incoming perfect matchings. Their complete census is:

| Number of lower vertices in a circuit | Number of circuits | Common-core rank | Active-coordinate count |
|---:|---:|---:|---:|
| 3 | 289 | 7 | 3 |
| 5 | 68 | 6 | 5 |
| 34 | 1 | 0 | 17 |
| 170 | 1 | 0 | 17 |
| 16167 | 1 | 0 | 17 |

There are 360 nontrivial circuits, involving 17,578 lower vertices.
Every circuit's complete ordered lower masks and old/new upper masks
are saved. The common core is the intersection of its lower masks;
active coordinates are the union of its upper masks outside that core.

The 289 three-vertex circuits have exactly the usual common-core
triangle geometry: three lower sets `C+a_i` with `|C|=7`, and upper
sets `C+{a_i,a_j}`. Switching their incoming edges is a middle-level
C6 flip. The 68 five-vertex circuits are middle-level C10 flips on
a six-coordinate common core and five active coordinates. No stronger
classification of their ordering is asserted from these counts.

Switching all edges on any one alternating circuit preserves the
incoming perfect matching and, with `Phi` fixed, preserves the degree
and owner-count equations. The diagnostic did **not** test such an
intermediate factor for loops, temporal exclusions, lower coverage,
or upper coverage. Those properties cannot be inferred from static
matching conservation.

In particular the successful factor is not shown to arise by 357
independent safe local exchanges: its exact difference also contains
the three large circuits above. This does not prove that the large
circuits cannot be factored through other intermediate matchings using
smaller moves. Such a factorization and its coverage transport have
not been provided or tested.

The user's fourteen successor changes were relative to an unspecified
intermediate result of a global search. They are not a count of the
changes from canonical PBBS measured here.

### 4.1 Exact quotient difference, derived without another run

Both incoming matchings commute with the verified 17-coordinate rotation
`rho`, so `theta` commutes with it as well. Rotation therefore permutes
the theta-cycles, preserving their lengths. The action of `rho` on every
proper nonempty physical target is free of order17.

A theta-cycle of length three or five cannot be invariant under this
free order17 action. Such cycles consequently occur in full rotation
orbits of17: the 289 triangles give17 quotient triangles, and the68
five-cycles give4 quotient five-cycles. Each of the physical lengths34,
170 and16,167 occurs only once, so its cycle is rotation-invariant and
projects to one quotient cycle of respectively2,10 and951 vertices.
The6,732 fixed physical rows give396 fixed quotient rows.

Thus on the recovered1,430 quotient rows the exact difference has

    fixed rows:       396;
    nontrivial cycles:17 of length3, 4 of length5,
                      1 each of lengths2,10,951.         (4.3)

There are1,034 changed quotient rows. This is a direct group-action
consequence of the executed physical census and verified equivariance;
it was not an additional computational experiment. In particular the
large physical circuit corresponds to a951-row quotient circuit, rather
than many independent small circuits already present in this difference.

## 5. Temporal exclusions, exact lower envelopes, and recovered quotient

For `L -> sigma(L)`, record insertion `b(L)=sigma(L) minus L` and
deletion `d(L)=L minus sigma(L)`, both singletons. The actual carrier
satisfies both exclusions everywhere:

    b(L) != d(sigma(L)),
    b(L) != d(sigma^2(L)).                              (5.1)

The exact native comparison has 119 violating lower labels, all
assigned native height two by the source inventory. These are counts
of (5.1), not a census of every short coordinate run of every source
representation. The actual violation count is zero.

At each actual cyclic literal position, the checker reconstructs

    E_i=intersection(U_(i-3),...,U_i).

All 24,310 envelopes have rank six and collectively represent every
one of the 12,376 six-sets. The actual letter is contained in its
envelope, and every actual adjacent pair has exactly the envelope
pair's union. The mandatory pair-preserving pin

    Pin_i=(E_i minus E_(i-1)) union (E_i minus E_(i+1))

is contained in the actual letter at every position. There are 4,998
singleton pins and 19,312 two-coordinate pins. The actual cyclic
letters contain 21,777 distinct targets, the complete rank-one-through-six
family verified in the earlier literal census.

The native matching maps are rotation-equivariant, and the actual
successor, both matchings, envelope, pins, and refined literal letters
are all rotation-equivariant as well. Consequently the recovered
1,430 rows based on minimum-mask rotation representatives, with explicit
successor shifts, determine the complete actual middle carrier and
lower assignment. This reconstructs a valid quotient description from
the literal data, but does not identify the row numbering of the
unprovided original construction certificate.

## 6. Scope of the constructive advance

The completed native and aperture-three full-recency routing obstructions
do not apply to this new chronological inventory. The old unrestricted
triple-preserving cap UNSAT result also fixed the old chronology.
Here a complementary middle matching changes first; only afterward
are the envelope and lower letters reconstructed.

The exact preserved PBBS matching and the recovered quotient rows
provide a concrete smaller starting point for an all-dimension
construction: a complementary successor matching with explicit temporal
and coverage conditions. The missing proof is no longer accurately
described as requiring two entirely new middle matchings.

The lower compiler must still be generalized. The known one-core
capacity obstruction already excludes preserving every rank-eight pair
while filling all lower ranks in an exact19 word: it would require
94,183 distinct literal targets in at most 92,381 positions. This is
the earlier theorem in
[the one-core normalization audit](../MATH_AUDIT_AD_ALL_ODD_COMPILER_ONECORE_NORMALIZATION_20260729.md),
Section5, and
[the dimension-dependence audit](../MATH_AUDIT_K_K17_THREE_LEVEL_NORMAL_CHAINIZATION_20260802.md),
Section7. Therefore the fixed-matching simplification must ultimately
be coupled to a pair-changing lower compiler, rather than an unqualified
extension of the successful17 literal assignment.

No dimension-uniform safe local exchange or all-dimension exact word
has been established by this diagnostic.

## 7. Reproduction and full artifacts

The reviewed standalone checker is
[compare_k17_optimal_carrier_to_canonical_pbbs_20260909.py](compare_k17_optimal_carrier_to_canonical_pbbs_20260909.py).
One pinned-input run on `h100`, hostname `arboghast`, returned PASS in
0.530 seconds under 30 CPU seconds, 45 wall seconds and 1 GiB address
space. No optimization, trial switch, random choice, extra census,
or local mathematical execution occurred.

The local bundle is
[k17_optimal_carrier_comparison_20260909](k17_optimal_carrier_comparison_20260909/).
It includes:

* [Complete comparison certificate](k17_optimal_carrier_comparison_20260909/optimal_vs_pbbs_carrier_comparison_certificate.json).
* Full actual and canonical named middle-carrier rows.
* Every named incidence difference and every native temporal violation.
* All four fixed oriented alternating-circuit decompositions, including
  [the changed incoming matching](k17_optimal_carrier_comparison_20260909/alternating_circuits_native_incoming_actual_incoming.json).
* [The recovered 1,430 rotation-quotient rows](k17_optimal_carrier_comparison_20260909/recovered_1430_canonical_rotation_rows.json).

Remote directory:
`/home/amodo/exact-b-k17-optimal-carrier-comparison-20260909/artifacts/`.
