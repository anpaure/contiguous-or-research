# General q: two-order Phi connectors with balanced padding

Date: 2026-09-09. Pure constructive proof and independent audit of root's proposed generalization. No mathematical execution.

For q>=3, a parent factor with residence at least q supplies a complete local bank of q-edge connectors after adding 2q-4 fixed coordinates. The two final deletion orders always include a legal choice at a strict incoming boundary. This preserves the parent residence bound; it does not amplify it. The added dimension is 2q-4, so only the q=3 case is a two-coordinate extension.

## 1. Parent, padding and port shape

Let r>=2. The specified parent is a complete strict canonical-Phi factor on 2r+1 sites, with lower rank r and positive-coordinate residence at least q. Embed each parent state P as

    0^(q−2) P 1^(q−2).                                (1.1)

The child has 2r+2q-3 coordinates and lower rank r+q-2. Every parent height is shifted by -(q-2). Its minimum is at most -(q-1), below every initial fixed-prefix height. The final fixed ones rise from the end-parent height -(q-1) to -1 and cannot introduce an earlier lower minimum. Thus canonical Phi commutes with the embedding. Parent-coordinate ages are unchanged; the q-2 trailing fixed ones are permanently present.

For a fixed parent port P=00D1, with D Dyck of semilength r-1, the child source is

    A=0^q D 1^(q−1).

Write D=1R; let d denote that first D-one, and a the final parent one, which is the leftmost one in the displayed trailing block. The other q-2 trailing ones are fixed padding. Let alpha and gamma be the actual ages of a and d at A.

## 2. The first q−2 edges

For j=0,...,q-2 define

    S_j=0^(q−j) 1^j D 1^(q−1−j) 0^j.                 (2.1)

Here S_0=A. For j=0,...,q-3, the edge S_j->S_(j+1) inserts the last leading zero and deletes the rightmost remaining fixed one. It never deletes a during these edges.

At S_j the last leading zero first reaches height -q+j, which is at most -2 for all j<=q-2. The following j ones reach height -q+2j; the Dyck section never falls below that height. The trailing ones rise to j-1, and the final j zeros descend only to -1. Consequently the first global minimum is precisely that last leading zero. Every claimed insertion is therefore canonical, including the next insertion at S_(q-2).

All q-2 initial deletions remove fixed coordinates of infinite age under the embedded parent history. At the final S_(q-2),

    S_(q−2)=00 1^(q−2) D 1 0^(q−2),                  (2.2)

the active ages of a,d have increased to alpha+q-2 and gamma+q-2.

## 3. The two final orders

The next canonical insertion changes the second remaining leading zero to one. There are two possible penultimate states:

    T_I =0 1^(q−1) D 0^(q−1),       deleting a first;
    T_II=0 1^(q−1) 0R 1 0^(q−2),    deleting d first. (3.1)

Both have canonical Phi insert the first coordinate u. For T_I, the initial zero reaches -1 and the following ones and Dyck section remain above it; the final zeros only return to -1. For T_II, after the initial 0·1^(q-1)·0 the height is q-3. Every prefix of R has height at least -1, so the following heights are at least q-4>=-1. Its final active one and zeros end at -1 without going lower. In both cases the FIRST global minimum remains the initial zero.

Deleting the other coordinate then reaches the common endpoint

    E=1^q 0R 0^(q−1).                                (3.2)

The final two deletion ages are exactly

    order I (a,d):  alpha+q−2, gamma+q−1;
    order II(d,a):  gamma+q−2, alpha+q−1.              (3.3)

Therefore order I is legal precisely when alpha>=2, and order II precisely when gamma>=2. Both alpha and gamma are positive. Since the embedded incoming edge is strict Johnson, it inserts only one coordinate; the distinct present coordinates a,d cannot both have age1. At least one order is always legal. Choose order I unless alpha=1, in which case choose order II. In the latter case a closes a run of exactly q states.

At E the q newly inserted leading coordinates have ages 1,2,...,q in physical order on either route. Every surviving D-coordinate has its original age plus q. All trailing coordinates and d are absent. Thus the route choice gives the same output state and the same ages for every surviving coordinate.

The q>=3 restriction is used in q-4>=-1 for the swapped penultimate state. The r>=2 restriction supplies the nonempty D and distinct coordinate d. No smaller-parameter construction is implicit.

## 4. Mixed-bank disjointness and exact counts

Select any h of the complete fixed ports, including possibly all Cat_(r-1) of them. All states S_j with j>=1 have the last fixed coordinate zero, outside the complete embedded inventory where it is one. Their numbers q-j of initial zeros distinguish the stage banks. Both penultimate banks have one initial zero and are separated from each other by a: it is absent in T_I and present in T_II. The endpoint has no initial zero. Every map from D into a stage is injective, including the states involving 0R, from which D=1R is recovered. Thus all new lower states in the mixed bank are distinct.

For j=0,...,q-2, the outgoing upper of S_j is

    0^(q−j−1) 1^(j+1) D 1^(q−1−j) 0^j.              (4.1)

The j=0 upper is the embedded parent port's original outgoing upper and is reused once. All later upper banks have last fixed bit zero. Their different initial-zero counts distinguish them. The final consumed upper is either

    1^q D 0^(q−1),       or       1^q 0R 1 0^(q−2).  (4.2)

These have no initial zero, are separated from each other by a, and are injectively indexed by D. Thus the new consumed uppers are pairwise distinct and outside the embedded upper inventory. This also proves cross-port disjointness when different final orders are used.

If the parent has M=binom(2r+1,r) lower states, removing h old port edges and adding qh connector edges gives

    used lower states = M+qh,
    assigned edges / consumed uppers = M+(q−1)h.       (4.3)

The result is h directed paths plus any parent components without a selected cut. The missing incoming heads are the embedded sigma(00D1), and the free outgoing ends are the indexed E. This is a path bank, not a full child factor.

## 5. Remaining boundary and dimension gates

The free outgoing upper at E is 1^q0R0^(q-2)1: all earlier nonempty heights are positive or zero until the final first minimum, so Phi adds the last fixed coordinate. Every missing incoming head has at least q-1 initial zeros: the padding supplies q-2, and the first parent coordinate remains zero in every facet of Phi(00D1)=01D1. A facet of the free upper can delete only one of its initial ones. Since q-1>=2, direct matching of these free ends to the listed missing heads cannot close the paths.

A global completion must provide unused incidences and restore genuine parent-age boundary certificates at the cut heads. It must also accommodate the q distinct young output ages. No matching, topology, coverage, or exact-length word claim follows from the degree ledger alone.

The hypothesis is a parent factor already having residence q. Balanced padding leaves all its active-coordinate runs unchanged and hence supplies no residence amplification. Applied to the verified nineteen-coordinate residence-three carrier, this theorem is the q=3 local bank already established; it does not by itself turn that carrier into a higher-residence input. For q>3 it adds 2q-4 coordinates, rather than two.

Root proposed the general S_j family and two final orders. The induction agent independently checked every first-minimum calculation, exact age inequality, stage/bank distinction, output ages and ledger. The q=3 specialization is exactly [the two-order 0P1 connector](TWO_ORDER_CANONICAL_PHI_CONNECTOR_AND_COMPLETE_0P1_PORT_BANK_20260909.md). The result is a positive parameterized local construction with explicit limitations, not a completed all-dimensional induction. No mathematical execution occurred.
