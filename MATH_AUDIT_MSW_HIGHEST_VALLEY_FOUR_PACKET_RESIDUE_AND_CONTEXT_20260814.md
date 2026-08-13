# Hostile audit of the MSW highest-valley context and residue proof

**Date:** 2026-08-14

**Verdict:** PASS after one local repair. The theorem in
`MATH_THEOREM_MSW_HIGHEST_VALLEY_FOUR_PACKET_MONOTONE_CONNECTIVITY_20260813.md`
is proof-complete for the stated connectivity conclusion. The audit found
no counterexample to context transport, any packet permutation, the
both-pyramid cyclic ordering, the wrap gap, or the crossed exceptional
cuts.

The one repaired defect was in the third subcase of the one-pyramid
residue proof. The earlier text called

    L+d+2  and  L+O+d+3

consecutive and assigned them gap O+1. For L<d an old point lies between
them. The current proof correctly uses the genuinely consecutive pair

    L+d+2  and  T+L+3,

whose gap is T-d+1 >= d+1. This changes neither the theorem nor its
threshold.

## 1. Context transport

The recursion

    rho(1u0v)=(c,c-rho(mu u),1,c+rho(v))

has the following exact functorial effect on an old-to-new position
permutation supported inside one child.

1. In a right child, the child permutation is translated and the enclosing
   pair plus the left child contribute fixed positions.
2. In a left child, the identity

       rho(mu u)=|u|+1-rev rho(u)

   reverses and translates the child permutation; the enclosing pair and
   right child are fixed.
3. Cutting the cyclic position circle immediately before the active block,
   those newly fixed positions adjoin the two linear ends. They extend one
   complementary cyclic interval and never split it. Reversal exchanges
   the two ends.

Induction along the binary-tree address therefore gives a dihedral
conjugate of the canonical active permutation with 2O additional fixed
positions in one exterior gap. With the sentinel, the full fixed exterior
interval has length 2O+1. This proves that the position calculation depends
only on L,Q,O; ambient shape only permutes labels inside a pointwise-fixed
block.

An independent H100 reconstruction of rho from its g/h dynamics checked
every highest-valley packet in all Dyck roots through m=10:

    context_packet_checks=71627

Every global permutation was dihedrally conjugate to the corresponding
canonical formula. Both translation and reversal cases occurred for all
four packet types, so the test was not confined to one address parity.

## 2. Packet permutations and tight-position conversion

The independent audit constructed the canonical words

    M_(L+1) M_(Q+1) M_O

and each legal transposed mate, reconstructed both flip words by g/h, and
formed the literal permutation pi[new flip position]=old flip position.
For all 0<=L,Q,O<=10 it obtained the four displayed theorem formulas
exactly:

    canonical_formula_checks=4851.

It separately checked that each formula is a permutation and that the
displayed nonfixed flip-position supports are exact in every local case in
which the packet is available.

The map from flip position z to tight position is multiplication by
2^(-1)=m+1 modulo n. Hence a direct same-start cut is safe precisely when
its d starts avoid

    C_pi union (C_pi-(s-1)).

On a cyclic circle, a d-term interval avoids this set if and only if two
consecutive bad points have cyclic distance at least d+1. The off-by-one
in this criterion is therefore correct.

## 3. Residue ordering and both-pyramid gaps

The H100 audit scanned all four sufficient rows through

    1<=d<=30,  0<=L,Q,O<=30.

It checked 455,925 applicable residue rows. The direct 0011 packet failed
exactly at

    (L,Q,O)=(d,d,d-1),

once for every tested d, and nowhere else.

For the delicate both-pyramid proof, a separate audit scanned 6,661,200
states through d,L,Q<=60 and 0<=O<=60. It verified literally:

1. when Q+O<=d-2, the translated point d-Q-O-1 is immediately before L;
2. in the remaining no-gap branch, 0 and L are consecutive;
3. reversal gives Q<=d as claimed;
4. L+Q+d+2 is immediately followed by T+L+3;
5. T+L+d+4 is the last bad point and its next point is zero across the
   cyclic wrap; and
6. the two resulting gap bounds are

       L+O<=2d-1,  Q+O<=2d-1.

Adding gives L+Q+2O<=4d-2, equivalently T+O<=4d-2. Combining this with
T>=3d-1 gives O<=d-1. Together with the earlier O>=d-1, this forces
O=d-1; L,Q<=d and T>=3d-1 then force L=Q=d. The contradiction algebra is
sound.

The wording “lies in the final segment before the cyclic wrap” is the
correct ordering assertion; no equality of a translated point with the
wrap endpoint is being assumed.

## 4. Exceptional crossed cuts

At (L,Q,O)=(d,d,d-1), the audit converted each explicit flip permutation
to its tight-position map q_r and checked the theorem's cuts for every
1<=d<=100. It verified the stronger ordered crossed identities, not just
unordered pair equality:

    q_(b+s-1+j)=a+j,
    q_(b+j)=a+s-1+j,

for every 0<=j<d. There were 10,100 ordered endpoint-pair checks and no
failure. The formulas printed in the theorem are therefore sufficient to
recover the crossed rails without relying on the finite graph census.

## 5. Independent and targeted H100 replays

The dependency-free hostile verifier is

`scratch/audit_msw_highest_valley_four_packet_residue_context_20260814.py`.

Its frozen H100 summary is:

    host=arboghast
    canonical_formula_checks=4851
    context_packet_checks=71627
    residue_row_checks=455925
    ordering_states=6661200
    exceptional_ordered_pair_checks=10100
    PASS

The repository's targeted verifier was independently rebuilt and rerun on
H100 at m=14. Its current-byte summary includes

    roots=2674440
    nonmountain=2674439
    packet_good=2674439
    packet_bad=0
    high_left_good=2674439
    high_right_good=2674439
    high_left_same_start_good=2674439
    high_right_same_start_good=2674439.

Thus the fresh output actually exercises the current highest-valley code
path; it is not the stale output mismatch identified in the earlier audit.

## 6. Frozen SHA-256 ledger

All hashes below were computed on H100 after the final theorem bytes were
copied there:

| artifact | SHA-256 |
|---|---|
| final theorem | `18b19df227235e5121bfa017e9520f7df82dd0a3323c6fe4ea3b505ab9bc12fc` |
| hostile verifier | `13644755ad553ff23edcff4da89ed70bc639648cf307a8757caa4eaf04ddcd67` |
| hostile verifier output | `0369363a7de47816961a406e05bcf166b48708941f214078cbbf5ac5a7fabe2d` |
| targeted verifier source | `957bb91c1c41c355ec33a43faeddcb32b74a8fb6e93724bfd47ff6bf2d68e58f` |
| targeted verifier binary | `c50e9a2a816358b0dbf1542b67d28f4f50e02b0fb6f319fc46f5877006a30399` |
| fresh m=14 targeted output | `0a05d58e284bf27ca5b946361c17722d4c3017d8f7d438c9adf940d3ef8e68ae` |

## 7. Exact scope

The audit freezes monotone same-forced connectivity. It does not prove a
simultaneous separated-port assignment, bounded tree child load in all
parameters, source fusion, occurrence-disjoint de-Bruijn switching, or the
long upper-deck actuator. Those remain independent gates.
