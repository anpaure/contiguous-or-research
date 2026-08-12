# `k=17`: complete lower-flag attachment on the controlled GKS central skeleton

Date: 2026-08-01  
Lane: A, exact Catalan-orbit age flags  
Status: unconditional literal static rank-`2,...,8` flag factor on the
authenticated GKS surgery; changing-owner chronology, voltage and the
upper-safe opening remain open

## 0. Result

Fix the authenticated GKS rank-`6,7,8` skeleton from
`MATH_THEOREM_A_K17_GKS_RANK678_CONTROLLED_SURGERY_AND_LOW_FLAG_GATE_20260801.md`:

\[
 442\ (6<7<8),\qquad286\ (6<8),\qquad702\ (7<8).     \tag{0.1}
\]

There is a literal assignment of all lower target necklaces at ranks two
through five to this skeleton with quotas

\[
\begin{array}{c|rrrr}
 &2&3&4&5\\ \hline
(6<8)&0&20&0&127\\
(7<8)&8&20&140&237.
\end{array}                                           \tag{0.2}
\]

Together with the 436 unused rank-one slots, this gives exactly the nine
certified age-type masses

\[
                 (139,297,8,20,20,140,127,237,442). \tag{0.3}
\]

More strongly, for every one of the 1430 rank-nine owner orbits the
certificate gives an actual disjoint partition

\[
                 T=C_0\mathbin{\dot\cup}C_1
                     \mathbin{\dot\cup}C_2
                     \mathbin{\dot\cup}C_3           \tag{0.4}
\]

of its declared type.  The three suffixes

\[
                  C_0,qquad C_0\cup C_1,qquad
                  C_0\cup C_1\cup C_2               \tag{0.5}
\]

cover every necklace orbit exactly once at each tight rank `2,...,8`.
Thus the full **static** GKS age-flag gate is closed, not merely its rank
marginals.

## 1. The four Hall systems and their coupling

Let `K_-` be the 286 skip packets `(6<8)` and `K_+` the 702 pair packets
`(7<8)` of the fixed skeleton.  Each packet has a fixed aligned physical
base `B_K` of rank six or seven inside its rank-eight and rank-nine sets.

For `s=2,3,4,5`, join a rank-`s` target necklace `O` to packet `K` when
some rotation of its fixed representative is contained in `B_K`.  Once the
type bins are fixed, the four required Hall systems are

\[
\begin{array}{c|c}
s&\text{eligible packets}\\ \hline
2&C\subset K_+,\quad |C|=8,\\
3&D\subset K_-,\ |D|=20;\quad E\subset K_+,\ |E|=20,\\
4&F\subset K_+,\quad |F|=140,\\
5&G\subset K_-,\ |G|=127;\quad H\subset K_+,\ |H|=237.
\end{array}                                           \tag{1.1}
\]

For a fixed subdivision, rank `s` is feasible exactly when

\[
                  |N_s(X)|\ge |X|                   \tag{1.2}
\]

for every family `X` of rank-`s` target orbits.  The subtlety is that the
subdivision itself must be selected while no packet is reused.  Four
separately feasible marginal systems would not establish that coupling.

The frozen certificate solves the coupled problem directly: it chooses the
type bin of every packet and one aligned target in its unique low slot.
After that choice, the selected edges are explicit perfect matchings in all
four graphs (1.2), and hence certify every Hall cut.

## 2. Exact construction

For a selected target representative `S` and recorded shift `a`, put

\[
                         C_0=\rho^aS.                \tag{2.1}
\]

If `K` is a skip packet with rank-six base `B`, define

\[
 C_1=B-C_0,qquad C_2=Q_8-B,qquad C_3=T_9-Q_8.      \tag{2.2}
\]

If `K` is a pair packet with rank-seven base `B`, use the same formula.
For an intact triple use

\[
 C_0=Q_6,qquad C_1=Q_7-Q_6,qquad
 C_2=Q_8-Q_7,qquad C_3=T_9-Q_8.                    \tag{2.3}
\]

The aligned containment test makes all differences in (2.2)--(2.3)
literal.  They are disjoint and have the following sizes:

\[
\begin{array}{c|c}
\text{packet/low rank}&(|C_0|,|C_1|,|C_2|,|C_3|)\\ \hline
(6<8),1&(1,5,2,1)=A\\
(7<8),1&(1,6,1,1)=B\\
(7<8),2&(2,5,1,1)=C\\
(6<8),3&(3,3,2,1)=D\\
(7<8),3&(3,4,1,1)=E\\
(7<8),4&(4,3,1,1)=F\\
(6<8),5&(5,1,2,1)=G\\
(7<8),5&(5,2,1,1)=H\\
(6<7<8)&(6,1,1,1)=I.
\end{array}                                           \tag{2.4}
\]

The exact matching occupies 147 skip packets and 405 pair packets.  The
remaining `286-147=139` skip packets receive type `A`, and the remaining
`702-405=297` pair packets receive type `B`; choose any singleton of their
base for `C_0`.  All rank-one suffixes lie in the unique singleton
necklace orbit, so any one of these 436 occurrences can be marked.

This proves (0.3) at the level of literal partitions rather than type
labels alone.

## 3. Independent all-rank replay

The independent verifier does not trust the matcher's quota report.  For
all 1430 rows it checks:

1. the owner, skeleton kind, base, rank-seven and rank-eight sets against
   the frozen central skeleton;
2. pairwise disjointness and union (0.4);
3. the four cardinalities against the declared one of the nine types;
4. the recorded rotation identity `rho^a S=C_0`;
5. literal suffix identities (0.5);
6. exact type masses and exact skip/pair quotas; and
7. pairwise distinct necklace orbits at every rank `2,...,8`.

It returns

```text
PASS_K17_GKS_FULL_STATIC_AGE_FLAGS
suffix_orbit_counts_rank2_to8 = 8,40,140,364,728,1144,1430
skip_rank2_to5 = 0,20,0,127
pair_rank2_to5 = 8,20,140,237
type_masses = 139,297,8,20,20,140,127,237,442
```

The construction program was compiled with `g++ -O3 -std=c++20` and run
on the H100 CPU under a 4 GiB address-space cap.  Its deterministic seed
found the frozen solution at trial 6978.  Randomization is not part of the
proof: the TSV and the independent verifier are the certificate.

## 4. Exact scope

This result closes the static necklace-chain surgery completely.  It also
answers the compatibility question affirmatively: the lower attachments
are simultaneously compatible with one exact type on every owner and with
all nine global masses, not merely with separate rank capacities.

It does **not** order these owners.  The connected type word of SHA
`e55bea5534c80560755dbc34a1f40e5cb9e67bca23e82d72caf902d2a1fd39f8`
still requires:

* a voltage-twisted changing-owner transition between consecutive literal
  partitions;
* the 436 forced lag-four return identities;
* one nonzero-voltage connected quotient lift; and
* an upper-safe physical opening.

The owner-cycle SAT lane is therefore neither duplicated nor bypassed.  Its
static flag input is now an explicit controlled GKS certificate.

## 5. Frozen artifacts

```text
scratch/threadA_k17_gks_rank678_skeleton_20260801.tsv
scratch/build_threadA_k17_gks_lowflag_matcher_20260801.cpp
scratch/threadA_k17_gks_full_static_flags_20260801.tsv
scratch/threadA_k17_gks_lowflag_matcher_20260801.audit.txt
scratch/verify_threadA_k17_gks_full_static_flags_20260801.py
scratch/threadA_k17_gks_full_static_flags_20260801.audit.json
```

Frozen SHA-256 values are

```text
rank678 skeleton TSV       6367d80702243cc08cdb952ad34632f45680b3ba3587a3b779c6d3e3ba68005f
O3 matcher source          a46ca6cf7ba1d091b3b175a1de47e2eee3e0c1d4c34ef2d38d43fc24d71bbb5e
H100 matcher binary        8b08f0fdc4b733fefcfcf1c1fa0db5bdf7892242dce069626e186b8450bc8af5
full static flags TSV      5fc20be6e76a5ca0336ce9bc51e252d2d597f2ec2ea9ff96a54264eb050cf886
matcher audit text         1b500507e413b8cebf33ce83dfe2efe0907f81d2b7dad06039341341486ec93e
independent verifier       d4ffe1166f82685d8baeeb905c5ae0e2a2ce985c5b92a24db04b66fa291f791d
independent audit JSON     f41e4bb870a4f2e81ecb9483461a7d41b04629594fe885a117f560feb737191d
```
