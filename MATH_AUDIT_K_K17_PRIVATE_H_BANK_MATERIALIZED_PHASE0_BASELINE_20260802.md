# Audit: K17 private H-bank materialized phase-zero baseline

**Date:** 2026-08-02  
**Status:** PASS for exact outer materialization, the lower target partition,
the complete phase-zero supplier projection, and the fixed-table relaxed-nine
socket census.  No fixed-table SAT was run.

## 1. Bound protected inputs

The protected private bank is the independently verified certificate in

```text
scratch/k17_phase0_retained_witness_private_basis_20260802/
```

Its load-bearing files are

```text
original table             db960ce5b51e0fdea7b048d35d48ca737096b16ee73a20df873beb0517e5f185
selected H tickets         d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1
complete outer matching    179270d1d01f6c14a7b47b5eb390e634aca33ac16e5ec82d54a93b589b8d850e
private-bank audit         dfaa7a5682861945f2de680076e86ce70fac2be5f35b3fe9783916c3903eec92
```

The bank has `1748` selected hard shorts, `3496` pairwise-distinct endpoint
hosts, `3495` forced movable host-token placements, and one fixed soft
endpoint.

## 2. Literal materialization

The independent materializer reads the original table and the complete
outer matching.  For a free receiver it writes `(B,R_F)`; for an occupied
hard receiver it writes `(B,M_H,R_H)`; and for an unoccupied hard receiver
it writes `(M_H,R_H)`.  It checks every token/receiver identity, strict
containment, unique token and receiver use, the exact `1748/16898` receiver
census, all `3495` forced flags, and the final histogram.

```text
materializer source
  scratch/materialize_k17_private_h_outer_matching_20260802.cpp
  SHA-256 532780dca891c8841f68fbdad8f8ef68cf5787a0ba973bd7ecdee78a76538499

materialized table
  scratch/k17_phase0_retained_witness_private_basis_20260802/
    private_h_outer_materialized.tsv
  SHA-256 b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
```

The table has `24310` rows and histogram `(0,7395,16915)`.  The independent
private-bank verifier already proves that its matching uses all `65535`
lower targets exactly through the bottom-token partition theorem; the state
census below reparses the materialized rows independently.

## 3. Complete fixed-table state replay

One nice-15 H100 CPU, capped at 8 GiB, ran the independently frozen
four-flag census.  The executable and source hashes were

```text
census executable  e9b1c75c0775ba5cbd8314d8dd7f5b3ee6c4c325485198990f26cd9e2a185300
census source      b3bed193dbbed859b8f24f9bd82d56a716f2493dba616e8a2d606d89de03505e
```

Peak RSS was `27448 KiB`; elapsed time was `149.06 s`; exit status was zero.
The exact result is

```text
hard heads                         16898
supplier matching                  16796
supplier deficiency                  102
supplier Hall shore heads/neighbours 109/7
exact relaxed-nine socket triples   3878
zero short roles                    4708
```

The zero/triple split by original row class is

| class | roles | zeros | live roles | triples |
|---|---:|---:|---:|---:|
| original singleton/free `F` | 1748 | 1521 | 227 | 330 |
| original fixed length-two `P2` | 3899 | 3187 | 712 | 1025 |
| selected hard short `H` | 1748 | **0** | 1748 | 2523 |

All `1748` protected occurrence-labelled tickets occur literally in the
reconstructed `short_reset_triples.tsv`.  Thus the H row is typed support,
not merely membership in the optimistic outer nonzero bank.

Principal output hashes are

```text
full audit JSON       5c14e0834829ab3c27c83be817259d8bc9e2395ab1e9a94b84713d740d4cb29f
socket summary        bc7415c669ee58213934405de696d23411359450d59bbdbb2705e4fbf3c4df67
socket triples        6e4f41c30b8aa9d9cbb599343d055d1ff14387137d3e0575b3f01ad5ea7d2217
supplier Hall shore   5b0afdc17d4be1e05bc51f459e8c2fe299959dbfdc279f13a409557ba0712255
```

## 4. Exact Pareto interpretation

Against the projection-perfect round-47 table, this arbitrary protected
completion changes

\[
 (\text{supplier deficiency},Z,\Omega):
 (0,5969,2188)\longrightarrow(102,4708,3878).         \tag{4.1}
\]

Against the weighted abstract-nonzero basis it changes

\[
 (29,5949,2407)\longrightarrow(102,4708,3878).       \tag{4.2}
\]

The typed private bank therefore removes all H zeros and substantially
improves the literal state census, but its arbitrary residual outer
completion loses `102` supplier units.  The next selector must retain the
protected H tickets and their forced placements while moving the residual
outer matching, fixed/free tickets, flags, and direct long--long edges until
the supplier rank is `16898`.

This is precisely the residual branch-flow interface in
`MATH_THEOREM_K17_PROTECTED_H_SHORT_PRIVATE_BANK_AND_FIXEDFREE_BRANCHFLOW_GATE_20260802.md`.
The open typed rows are the `5647` fixed/free roles; a current fixed-table
zero is not a global no-go and no fixed-table SAT should be launched.

## 5. Scope

This audit proves no simultaneous fixed/free ticket selection, one common
cycle, phase one, residence, upper shadow, common-cap/compiler feasibility,
or word.  It is the exact phase-zero Pareto baseline for the protected
private-bank branch-flow master.
