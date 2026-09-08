# A sparse recency C6 with explicit flat four-window ports

Date: 2026-09-08. Independent pure-proof audit of the root agent's corrected construction. No computation or search was used.

Status: the local transition gadget, exact width-one-through-four transfer, literal predecessor/successor strips, and conditional three-component fusion are proved. The ports have not been embedded into the current PBBS bank. No current source was modified and no exact-length universal word is claimed.

## 1. Corrected states and sparse transition graph

Partition [17] into disjoint sets U,V,W,Z,A,G of sizes 3,3,1,1,3,6. Write A={a,b,c} and F=U union V union W, so |F|=7. A recency state lists nonempty last-occurrence classes from newest to oldest.

For each i in A, choose an order (j_i,l_i) of A minus {i}, and set

    P_i=(U | V | W union {i} | Z | {j_i} | {l_i} | G).

For each unordered pair {i,j} in A, with remaining arm l, set

    X_ij={i,j},
    Q_ij=(X_ij | U | V | W | Z | {l} | G).

The exact recency update prepends the new letter and deletes its coordinates from every previous block, dropping empty blocks. Therefore

    T_(X_ij)(P_i)=T_(X_ij)(P_j)=Q_ij.

In P_i it removes i from W union {i}, leaving W, and removes j from whichever singleton block contains it. The other singleton remains after Z. Its previous order is immaterial once one singleton is removed. The same calculation applies to P_j.

The third source P_l does not map to Q_ij: its block W union {l} survives as a two-element block. Thus the source/destination compatibility graph consists exactly of the six edges

    P_a--Q_ab--P_b--Q_bc--P_c--Q_ac--P_a.

It is a six-cycle, not a complete coherent class. In particular it has no two distinct sources with two distinct common destinations, so the coherent-class common-facet lemma does not apply.

## 2. Middle owners, facets, and exact suffix transfer

The source prefix ranks are 3,6,8,9,10,11,17. The destination prefix ranks are 2,5,8,9,10,11,17. Their rank-nine prefix targets are

    T_i=F union {i} union Z,
    R_ij=F union {i,j}.

All six are distinct: sources contain Z and one arm, while destinations contain no Z and two arms. Within each family the arm labels distinguish them.

Suppose a source occurrence is realized as a flat four-window endpoint, meaning its last four literal letters have union T_i. Since the unique rank-nine prefix is its fourth recency block, those four blocks must be the four consecutive last-occurrence times. Thus its suffix unions of widths one through four are

    S(P_i)=(U, U union V, F union {i}, F union {i} union Z).

Appending X_ij updates suffix unions by S'_1=X_ij and S'_h=X_ij union S_(h-1) for 2<=h<=4. It gives exactly

    S(Q_ij)=(X_ij, X_ij union U,
             X_ij union U union V, F union {i,j}),

independently of whether the source is P_i or P_j. These are the destination's first four recency-prefix unions.

Hence a permitted reroute preserves the whole width-one-through-four suffix vector at its destination, not only its rank-nine owner. Subsequent unchanged letters update this vector deterministically by the same recurrence. Every later four-window union, triple union, pair union, and letter is therefore transported until the next rerouted edge, where the same argument applies again.

The three source last-three facets are F union {i}; the three destination last-three facets are U union V union {i,j}. They are six distinct rank-eight sets. The source family contains W, whereas the destination family does not. Every graft edge P_i to Q_ij has actual adjacent-owner intersection

    T_i intersect R_ij=F union {i}.

Thus its middle adjacency is Johnson, and choosing one outgoing edge per source uses each of these three outgoing colors once. This avoids both the common-facet repetition obstruction and a non-Johnson seam charge.

## 3. Concrete literal predecessor and successor strips

Fix any U_0 subset U and V_0 subset V of size two. The same choices can be used at every port. For source i and either incident destination {i,j}, consider the literal word segment

    G, {l_i}, {j_i}, Z, W union {i}, V union U_0,
    U, {i,j}, Z union V_0.

After the letter U, its exact recency state is P_i: the earlier U_0 is overwritten by U, leaving V as the second block, and the other displayed blocks retain their stated order. After appending {i,j}, the state is exactly Q_ij.

The four consecutive four-letter windows ending at V union U_0, U, {i,j}, and Z union V_0 have unions

    T_i^- = U_0 union V union W union Z union {i,j_i},
    T_i   = U union V union W union Z union {i},
    R_ij  = U union V union W union {i,j},
    R_ij^+= U union V union Z union {i,j}.

Each has rank nine, and they are pairwise distinct. T_i^- differs from T_i by replacing the missing coordinate of U with j_i; it contains Z whereas R_ij does not, and W whereas R_ij^+ does not. The other three are distinguished by their W,Z and arm membership.

Their three adjacent intersections are respectively

    U_0 union V union W union Z union {i},
    F union {i},
    U union V union {i,j},

all of rank eight and mutually distinct. Their actual last-three literal unions are, respectively,

    U_0 union V union W union Z union {i},
    F union {i},
    U union V union {i,j},
    U union V_0 union Z union {i,j},

all of rank eight. Thus the strip has the required literal four-window replay and triple facets, including a genuine Johnson predecessor to P_i and successor to Q_ij.

The source history through U does not depend on which incident destination is selected. The next letter Z union V_0 can likewise be the same for every destination. At the endpoint after it the prefix ranks are 3,5,8,9,10,11,17, so this continuation creates no immediate missing-rank-ten obstruction.

For an additional distinctness check, choose (j_a,j_b,j_c)=(b,c,a). The three predecessor owners T_i^-, the three source owners T_i, the three destinations R_ij, and the three successor owners R_ij^+ are all twelve distinct rank-nine sets. Their four groups are distinguished by W,Z membership and by the missing coordinate of U; the arm or arm-pair distinguishes members within a group. The corresponding twelve last-three rank-eight sets are also distinct, using the four W,Z membership patterns and the arm labels.

These are local strip certificates. Their earlier initialization windows are not asserted to form part of an optimal middle chronology, and the three separately displayed strips are not claimed to be one global path.

## 4. Conditional three-to-one fusion

Suppose an existing legal occurrence routing has one directed path and two directed cycles, containing respectively the three source occurrences, with old edges

    P_a -> Q_ab,
    P_b -> Q_bc,
    P_c -> Q_ac.

All six named occurrences are distinct, and the three old edges lie in the three distinct routing components. Replace them by

    P_a -> Q_ac,
    P_c -> Q_bc,
    P_b -> Q_ab.

All new transitions are legal by Section 1. Cutting each old edge opens its component at its named destination. The new route follows the path prefix through P_a, the opened P_c component from Q_ac through P_c, the opened P_b component from Q_bc through P_b, and the old path suffix from Q_ab. It is one path with the same initial and terminal occurrences. Thus three components become one.

Every recency-state occurrence is retained, and the incoming-letter multiset {X_ab,X_bc,X_ac} is merely permuted. All recency-prefix target labels are preserved. If the old routing also carries the flat suffix vectors in Section 2, every width-one-through-four suffix target is preserved as well. In particular, its rank-nine four-window and rank-eight triple inventories are transported exactly.

This statement requires one path and two cycles. Applying the same permutation to three disjoint paths generally leaves three paths, so the local strip examples alone do not supply the global routing premise.

## 5. Why the singleton split is necessary for these ports

The earlier unsplit source used A minus {i} as one two-element block. Its prefix menu was 3,6,8,9,11,17, omitting rank ten.

Under a consecutive-start selected chronology, a flat four-window owner with a predecessor has union with that predecessor equal to the last-five-letter interval ending at its source endpoint. Distinct rank-nine owners make that union larger than nine. The unsplit source menu forces it to be at least eleven, making the incoming owner intersection at most seven. Three such flat source occurrences therefore force at least three non-Johnson incoming edges, violating the one-pivot allowance b+e<=2.

Splitting the two old arm labels into singleton blocks restores the rank-ten prefix. The explicit strip in Section 3 verifies that this is a real repair of that particular obstruction: the source now has a literal Johnson predecessor while all sparse C6 transitions remain valid.

## 6. The actual embedding boundary

These corrected ports pass the middle/facet and local flat-continuation interfaces, but they do not occur unchanged in the currently verified good depth-three source bank. Their pair suffixes have ranks six at P_i and five at Q_ij; the current good bank has rank seven at every pair. Their latest letters also have sizes three and two, rather than the current six-element envelopes.

A construction that preserves every existing pair union cannot introduce these states. Embedding them requires a certified alteration of the lower rows and retention or reassignment of all affected targets. This is a separate obligation from the graft: once an existing routing already has the stated ports, the graft itself preserves its width-one-through-four suffix inventory by Section 2.

No embedding, all-lower reassignment, safe global opening, or exact B(17)-length word is supplied here. The current 1513 PBBS bank is unchanged. The result is a concrete conditional connector with verified literal local continuations, not an unrestricted existence theorem.
