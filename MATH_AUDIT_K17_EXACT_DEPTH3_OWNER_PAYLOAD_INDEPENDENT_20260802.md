# K17 exact depth-3 owner-payload table: independent audit

**Date:** 2026-08-02  
**Verdict:** PASS for the literal table, chain partition, and selected
rank-eight--rank-nine owner phase.  This is not a source, residence, upper-deck,
compiler, or universal-word certificate.

## 1. Frozen inputs

The audited payload is

```text
/home/amodo/or15/work/root_k17_exact_depth3_owner_payload_table_20260802/
  k17_depth3_owner_payload.tsv
SHA256 029d3be53e13186e7be4c5bd8b89de9d3610be05c3af15f8c9024e7fbf3396c1
```

The producer-side report and generator source were frozen, but neither was
used as executable audit logic:

```text
k17_depth3_owner_payload.audit.json
SHA256 6e508cb8521e2c263c32b3f08e546693d50e90f858b8f6157a3f55e7ef7c758c

build_k17_exact_depth3_owner_payload_table_20260802.cpp
SHA256 410a617e3e724e005b8cce73bee50067ee8256363ae723621e18910748c929b1
```

The incidence map and authenticated primary factor were

```text
/home/amodo/or15/work/root_k17_h1_global_outer_20260802/lazy10/
  basec4.map.tsv
SHA256 80980012d7b1449c8ce3932e77ee7e5e47f5d6eb6f18d219687358cbd024355a

/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
  checkpoint_fullq1_escape_res2018/model
SHA256 c8f961413aeea43cbad5036e801c08f854f84889eaef11c281aa83bea46c057d
```

## 2. Independent implementation

The audit implementation is a fresh strict parser and replay.  It neither
includes the generator nor copies its matching implementation:

```text
scratch/audit_k17_fullq1_floor_replay_20260802/
  audit_depth3_owner_payload_independent.cpp
SHA256 e198b4870f6832a5168aae596686478de38ceed525f7555eca157df0ac6a9aeb

  depth3_owner_payload.independent.audit.json
SHA256 bb2fc1f7eb54e0379af2797b179efdb25b7eb677a826bb0732198134b4cf001f

  DEPTH3_MANIFEST.sha256
SHA256 434ea4d3f0c8270487873517e05263911f7d6dd79e4b0d60dc9bf450e6b5de8d
```

It independently parses the complete SAT assignment, the complete
`218,790`-row incidence map, and every TSV field.  It then checks:

1. chain IDs are exactly `0,...,24309`;
2. every listed mask is nonzero and has rank at most eight;
3. masks in a chain are strict successive inclusions and the last mask is
   exactly the row's rank-eight root;
4. target masks are globally unique and exhaust every nonempty mask of ranks
   one through eight;
5. roots exhaust the rank-eight layer once each and owners exhaust the
   rank-nine layer once each;
6. every root is contained in its row's owner; and
7. the map variable for every displayed root--owner incidence is selected in
   the authenticated primary model.

As a separate replay of the carrier, it reconstructs all selected incidence
edges, the exceptional root degrees, all owner degrees, and connectedness.

## 3. Exact results

The parser obtains

```text
chains                                      24,310
length histogram (1,2,3)                  (1,748, 3,899, 18,663)
targets                                     65,535
duplicate or missing targets                     0
rank-eight roots, unique/exhaustive          24,310
rank-nine owners, unique/exhaustive           24,310
selected root--owner phase incidences         24,310
unselected displayed phase incidences              0
```

The two checksum identities close:

```text
1,748 + 3,899 + 18,663 = 24,310,
1,748 + 2(3,899) + 3(18,663) = 65,535.
```

The exact target-rank histogram is

```text
rank                 1    2    3     4     5      6      7      8
payload count       17  136  680  2380  6188  12376  19448  24310
```

This is exactly `binom(17,r)` in every rank `r=1,...,8`.  Hence uniqueness
plus the histogram is also an independent exhaustiveness check.  The table
contains `65,535-24,310=41,225` strict chain links.

The independently reconstructed selected factor has

```text
selected incidence edges                    48,620
connected components                             1
root degrees (M,D,ordinary)                  (1,3,2)
owner degree                                      2
```

Thus the displayed `24,310` root--owner rows form a perfect selected phase:
each rank-eight root and each rank-nine owner occurs once, and every one of
those incidences is literally selected in model `c8f96141...`.

For an implementation-independent cross-check, a separate strict `gawk`
scan of the model, map, and table reproduced the same chain, rank, uniqueness,
exhaustiveness, phase, and degree counts with every error counter zero.

## 4. Scope boundary

This audit authenticates a static inclusion-chain payload table and one
selected rank-eight--rank-nine matching phase on one fixed factor.  It does
not establish literal source balance, depth-three residence, any upper deck,
a common cap, lower-compiler feasibility, a length-`24,313` word, or
`nu(17)=B(17)`.  It also does not certify the producer's particular
Hopcroft--Karp execution: the emitted table is checked directly, so its
generation history is unnecessary for the finite certificate verified here.
