# Frozen occ296+C6: regenerated closed-packet expansion

Date: 2026-07-31  
Lane: A, probabilistic expansion / closed packets  
Status: exact source-relative theorem; no K17 completion and no all-dimensional theorem

## 1. Frozen state and exact guard sets

The base object is the authenticated K17 owner cycle

    scratch/k17_opt28_occ296_c6_localmin_verified_20260731.owner_cycle.word
    SHA256 a47aa9d7c8b86ca3912c8c82262969332727d27bf427ee8783ccb1a8ce664b49

with transparent residual state

    scratch/k17_opt28_occ296_c6_localmin_state_20260731.txt
    SHA256 df816a09b5d0f1b2336e611ace3595298286116f3664c11556dbe25efd6d1321

It has one physical owner cycle, every rank-nine owner and every lower-q1
colour exactly once, and a frozen marked bank of 4108 owners. Its literal
two-bank row \(Z=(Z_i)_{i=0}^{24310}\) has

\[
 |\mathcal R|=776,\qquad |\mathcal S_2|=503,\qquad
 |\mathcal S_3|=503,\qquad
 (|\mathcal H_{10}|,|\mathcal H_{11}|,|\mathcal H_{12}|)
 =(1585,824,116).
\]

For \(0\le j\le24312\), define the clipped envelope

\[
 E_j=\bigcap_{\max(0,j-2)\le i\le\min(j,24310)} Z_i,
 \qquad (DZ)_i=Z_i\cup Z_{i+1}.
\]

The implementation initializes a boundary intersection to the full
seventeen-coordinate mask before intersecting the available \(Z_i\)'s. The
defect sets are:

* \(\mathcal R=\{(Z_i,b):b\in
  Z_i\setminus(E_i\cup E_{i+1}\cup E_{i+2})\}\);
* \(\mathcal S_2\), the internal coordinate runs of length below three in
  \(Z\), labelled by coordinate and by their physical \(Z\)-cells;
* \(\mathcal S_3\), the internal coordinate runs of length below four in
  \(DZ\), labelled by coordinate and by their adjacent-\(Z\) occurrence
  pairs;
* \(\mathcal H_r\), the missing rank-\(r\) contiguous interval unions of
  \(Z\).

A packet is **setwise guarded** for a bank \(\mathcal B\) when its final
defect set is contained in its base defect set. Its service set is
\(\mathcal B_{\rm base}\setminus\mathcal B_{\rm final}\). This is strictly
stronger than preserving only the size of a defect bank.

All upper claims below stop at ranks 10--12. The base has no holes at ranks
13--17, but this note does not certify those ranks for every compound packet.
Named survivor anchors, common-cap compatibility, and prepins are also outside
the declared guard state.

## 2. Minimum residual-U incidence circuits

### Lemma 2.1 (girth six)

In the inclusion graph between rank-eight lower ports and rank-nine owners,
there is no four-cycle. Hence every nonzero alternating incidence circuit has
at least six incidences.

#### Proof

Two distinct rank-eight sets have at most one common rank-nine superset: if
their symmetric difference has size two, their union is the unique one, and
otherwise they have none. A four-cycle would give two distinct common
rank-nine supersets. ∎

Thus the minimum circuits are incidence hexes. Let \(K\) be a rank-seven mask
on the old fifteen coordinates and let \(a,b,c\notin K\) be distinct. The
hex rotates the selected incidences of

\[
 K+ab,\qquad K+bc,\qquad K+ca
\]

among \(K+a,K+b,K+c\), in either orientation. Applicability means all three
residual singleton objects select their deleted port and do not already
select their added port. Algebraically this preserves every owner degree and
the lower-colour multiset. It is physically admissible only when its three
new edges reconnect the four cut fragments into one path.

### Theorem 2.2 (complete D3-inclusive C6 census)

On the frozen state, the complete old-coordinate residual-U incidence-C6
catalogue has

\[
\begin{array}{c|r}
\text{class}&\text{number}\\ \hline
\text{applicable incidence hexes}&6561\\
\text{one-cycle hexes}&3260\\
\mathcal R,\mathcal S_2,\mathcal S_3\text{-setwise guarded}&248\\
\text{also }\mathcal H_{10},\mathcal H_{11},\mathcal H_{12}
  \text{-setwise guarded}&14.
\end{array}
\]

Every one of the 14 fully declared-bank-guarded packets is neutral on all six
defect banks. Therefore every one of the

\[
 776+503+503+1585+824+116
\]

obligations has an empty service list. The 14 packets use 84 distinct
incidence resources, so their incidence-overlap graph has zero edges and
maximum degree zero.

In particular, there is no monotone one-C6 repair of even one declared
obligation. An anchored LLL or nibble fails before its numerical inequality:
the true minimum candidate-list size is \(L=0\).

#### Proof

The generator iterates over every rank-seven \(K\), every three-subset of its
eight outside old coordinates, and both orientations. Its selected/deleted
versus unselected/added incidence test is exactly applicability, so it
enumerates every incidence C6 in this fibre once. There are 6561.

For every move, literal traversal starts at the fixed marked-bank exit,
visits every residual object once, and must return at the fixed entrance.
Exactly 3260 pass. The resulting \(Z\)-row is materialized, and its sorted
cell multiset is checked against the base. Replay tokens, \(Z\)-run tokens,
\(DZ\)-run tokens, and rank-10/11/12 hole sets are recomputed literally.
Exact set inclusion gives 248 and then 14. Direct set differences give zero
service for all 14. Comparing the six incidence resources of each packet
gives 84 distinct resources and no overlap.

A separately implemented parser, C6 enumerator, path traversal, envelope
builder, occurrence-token evaluator, and upper-hole evaluator independently
reproduces 6561/3260/248/14 and every zero service bank. ∎

### Signed, not guarded, C6 supply

If upper losses are permitted while
\(\mathcal R,\mathcal S_2,\mathcal S_3\) remain setwise guarded, the 248
packets have the following singleton gain lists:

\[
\begin{array}{c|c|c|c|c}
r&|\mathcal H_r|&\text{holes with a gain packet}&\text{zero-list holes}
 &\text{positive list-size range}\\ \hline
10&1585&53&1532&1\text{--}2\\
11&824&82&742&1\text{--}3\\
12&116&27&89&1\text{--}5.
\end{array}
\]

Their exact incidence-resource overlap graph has 24 edges and maximum degree
two. These are not guarded service lists: each of the 234 nonneutral packets
creates at least one new upper hole in ranks 10--12. Disjoint incidence
footprints also do not prove that two packets compose to a single path or
that their losses cancel. The small overlap degree is therefore not an LLL
dependency degree.

The earlier count 249 is retracted: it omitted occurrence-labelled
\(DZ\)-run guarding. The exact D3 guard removes one packet.

## 3. Complete P2 and support-two P3 shells

A primitive same-colour exchange replaces one selected edge by another edge
of the same lower colour. If the two edges share one owner, its owner-degree
delta is \(-e_u+e_v\); call it support two. If they are disjoint, its delta
has support four. In the frozen complement path there are exactly

\[
 545721=239266+306455
\]

primitive columns, with 239266 of support two and 306455 of support four.
Every full primitive degree-delta vector is distinct.

### Theorem 3.1 (P2 exhaustion and complete support-two P3 census)

1. No two distinct primitive columns in this frozen catalogue form a balanced
   pair.
2. The complete support-two, three-column, distinct-colour, one-path packet
   bank has 13871 packets.
3. Exactly 423 of those packets are simultaneously setwise guarded for
   \(\mathcal R,\mathcal S_2,\mathcal S_3\) and
   \(\mathcal H_{10},\mathcal H_{11},\mathcal H_{12}\). Their singleton
   upper service lists are:

\[
\begin{array}{c|c|c|c|c}
r&|\mathcal H_r|&\text{positive lists}&\text{zero lists}&
  \text{list-size histogram}\\ \hline
10&1585&69&1516&1^{66}2^3\\
11&824&85&739&1^{77}2^8\\
12&116&36&80&1^{30}2^4 3^2.
\end{array}
\]

The declared algebraic resource-overlap graph on the 423 packets uses 3739
colour/incidence resources, has 42 edges, and has maximum packet degree
three. There are 209 target--packet service copies. The values zero to three
attached to those copies in the audit JSON are the degrees of their **parent
packets** in the 423-packet graph; they are not degrees in the expanded copy
graph. The overlap graph omits simultaneous topology, joint replay/D2/D3
interactions, upper-witness interactions, ranks 13--17, and common-cap
conflicts. It is not a physical LLL dependency graph.

#### Proof

Two primitive columns balance only when their nonzero degree-delta vectors
are opposites. Exhaustion of the 545721 distinct vectors finds no opposite
pair, proving (1).

For support-two columns, a balanced triple

\[
 (-e_u+e_v)+(-e_v+e_w)+(-e_w+e_u)=0
\]

is exactly a directed triangle on owner labels; the absence of an opposite
pair excludes a two-cycle plus a zero column. Conversely every such directed
triangle is balanced. Enumerating each triangle at its least owner gives
28114 directed triangles. No row repeats a lower colour. The exact
four-fragment tree test rejects 14243 disconnected rethreads and retains
13871, proving (2).

Every retained packet is replayed literally. Of the 13871, 4512 do not
increase any of the three upper-hole counts, but only 2868 preserve all three
upper hole sets. Because hole-set inclusion implies count nonincrease, the
scalar prefilter cannot discard a fully guarded packet. Intersecting exact
replay-, \(Z\)-run-, and \(DZ\)-run-set inclusion leaves exactly 423.
Direct set differences give the service table. Declaring a shared lower
colour or a shared deleted/added colour-owner incidence to be a resource
overlap gives the exact 3739-resource, 42-edge, maximum-degree-three packet
graph and 209 service copies. This proves (3) for the six declared banks. ∎

### Atomic rank-ten Hall obstruction

Even after discarding all residence and upper-loss guards, the 13871
support-two P3 singleton gain lists reach only 1462 of the 1585 rank-ten
holes. The atomic target--packet graph has matching rank 1459. An exact Hall
witness has 129 targets and only three packet neighbours, hence deficiency
126: 123 targets have empty lists, and the remaining six form a
three-neighbour core. The loss-free positive subbank reaches 892 targets and
has matching rank 873.

Therefore the **one-packet atomic provider relation** cannot support a
distinct-packet rank-ten transversal. This audit does not exclude a jointly
replayed compound of several P3 packets; no additivity theorem for singleton
gain lists under such composition is asserted here.

The scalar evaluator illustrates the need for setwise guards. Its best
independently replayed count-nonworsening packet changes

\[
 (1585,824,116)\longmapsto(1582,822,117),
\]

improving ranks ten and eleven while exporting a new rank-twelve hole.

## 4. Consequence for expansion

The old-base figures 5433, list range 2--34, and their conflict statistics do
not apply to the occ296+C6 fibre. After regeneration:

* the complete declared-bank-setwise-guarded incidence-C6 lists have \(L=0\);
* the complete declared-bank-setwise-guarded support-two P3 lists have
  1516/739/80 zero rows;
* the small packet overlap degrees zero and three are irrelevant to an
  anchored LLL and are not full physical dependency degrees.

Thus the anchored-LLL/nibble hypothesis is false in the first two
declared-bank-guarded packet shells. This is a source-relative support
obstruction, not a global K17 impossibility.

## 5. Exact remaining boundary

The smallest uncensused ways around the obstruction are:

1. a jointly replayed pair of support-two P3 packets, including the narrower
   two-C6 case;
2. a balanced P3 containing at least one of the 306455 support-four primitive
   columns;
3. a P4 or longer alternating circuit;
4. an occurrence-changing or forest-first ear outside the fixed residual-U
   fibre.

Every compound must be judged after joint materialization. A physical packet
signature must include deleted/added incidences, final fragment permutation,
signed replay/D2/D3 and upper-witness sets, marked-bank anchors, and eventual
common-cap recourse. Pairwise incidence disjointness alone does not imply
one-path topology, witness survival, or rank-three cap compatibility.

No common-cap matching is instantiated at this checkpoint because replay and
residence still fail. Nothing here proves a K17 word,
\(\nu(17)=B(17)\), \(B(k)+O(1)\), or an RSB transition.

## 6. Frozen artifacts and audit boundary

Minimum-C6 producer, result, and independent replay:

    scratch/audit_threadA_k17_occ296_c6_closed_packet_expansion_20260731.cpp
    SHA256 efd79a1cddbeddb13625cf1f43159f84aa2dffd16365ae332783a834122b0b5b

    scratch/threadA_k17_occ296_c6_closed_packet_expansion_20260731.raw.json
    SHA256 9a8db5c0119aa99104a41d38ce60a67caf00564b2dca8e635da76e817465e0fe

    scratch/audit_threadA_k17_occ296_c6_closed_packet_expansion_independent_20260731.py
    SHA256 98e23de3eac140d7a50e03e5d5476b2cecb6a78c7298eb80fdc51052c6586649

    scratch/threadA_k17_occ296_c6_closed_packet_expansion_20260731.audit.json
    SHA256 ab3382d123412cca7ef50ed47ac6acf87274a1e880943a7f9f8a97c613bc0713
    payload aad0a83e93815e2abde1dc504d352a246f8161eceb94a0ae0e4e3ae08513bb7f

P2/P3 catalogue and independent algebra/rank-ten audit:

    scratch/k17_opt28_occ296_c6_balanced_p2_20260731.meta.json
    SHA256 1d35eea0f8607c50020308841e4cb1e01d9811f117992af5a5c0c627733391d2

    scratch/k17_opt28_occ296_c6_balanced_p3s2_20260731.meta.json
    SHA256 2a07e8d11aa9e9aadf5696e8173658ade4bc89d68f8c0fa3735ae6595dd3fcf9

    scratch/k17_occ296c6_balanced_p2_p3_rank10_independent_20260731.audit.json
    SHA256 de1e812ce472954a9875b787ecec00dc6117af77a3dca02aeeb4804c2098ff2e
    payload 90032a0f866342de886421528c7d607e29e14bc97ad44391ca9df8f4464141f6

P3 literal guard evaluator and result:

    scratch/evaluate_k17_opt28_balanced_p3_packets_20260731.cpp
    SHA256 fed76211e43b94e16b9ee217cea4fe8722067e27537fdb4ca56e4e3897c35e61

    scratch/audit_threadA_k17_occ296_p3s2_holeset_guard_20260731.cpp
    SHA256 bd97d1632c60f1af5b66b170b6dcc0c98c35c10fe3e6f5292399611d4c32f309

    scratch/threadA_k17_occ296_p3s2_holeset_guard_20260731.audit.json
    SHA256 c1abd3af2fb29c25285555b01c8314a9f26b0719dc0a0e824f535da7cc62f5c1

Lineage and summary wrapper:

    scratch/audit_threadA_k17_occ296_c6_packet_lineage_20260731.py
    SHA256 16eb6386cc483bee13ad75c9a123b7dd2a19df77b86c8d3fbc5cd586e81408cc

    scratch/threadA_k17_occ296_c6_packet_lineage_20260731.audit.json
    SHA256 094fc9c891afed679f33b7c8fd34eb0d5511b857cc4d76aa38971de7037f3e3c
    payload d68661c415e460daee0f37949a6dda3c2b1a25baeaf7c9d56a38261772c74a4f

Scalar P3 checkpoint and independent literal replay:

    scratch/k17_opt28_occ296_c6_balanced_p3_exact_20260731.result.json
    SHA256 39cd6be297803a0ecfbbdcac4903413f952d8288f45531c4a3660f32e43ce7fc

    scratch/k17_opt28_occ296_c6_balanced_p3_exact_20260731.owner_cycle.word
    SHA256 c522020c4f7cdee2719d654b6d6b9a0c9228fd80f27d877102997c0db0e3ab30

    scratch/k17_opt28_occ296_c6_balanced_p3_exact_20260731.independent.audit.json
    SHA256 641cf08a1557e11f8a5792ace7362beefd1f11085f0f9ebb745180c8d3dbccb0
    payload 18956dd3879040a37a56ca9955dff3273dc99eed757f3e3344d8d682a318a7c8

The C6 census has a genuinely independent literal replay. The 423-packet P3
guard result is producer-exact. The separate lineage audit binds the intended
evaluator, packet binary, carrier, and current result bytes, but does not
replace an independent literal replay or prove an embedded command lineage.
Physical pair compatibility remains outside scope.
