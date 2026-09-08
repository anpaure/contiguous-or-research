# K16 j3959: the three minimum service states have the same bounded rethreading obstruction

Date: 2026-07-30  
Status: **exact finite theorem; scoped to two internally rethreaded physical packets of length at most eight**

## Statement

After the exact `12 -> 6 -> 3 -> 2` donor descent, the 5,166-block
service atlas has exactly three minimum representatives:

```text
V0 = ab61, e361, eb60,
V1 = ea61,
V2 = ca71.
```

Every representative has the same two reconstruction equations:

```text
5e38 -> 5e18, missing 0020,
6a71 -> 6a61, missing 0010.
```

For each representative and each residual cut, enumerate every physical
contiguous pre-flat source interval of length 2 through 8.  Internally
rethread its occurrences with an exact run-state DFS whose state is the last
four masks.  A transition is retained exactly when it

1. closes every positive coordinate run with length at least four;
2. leaves every four-row erosion nonempty; and
3. passes the full variable-depth carrier replay after insertion.

Quotient by the exact full-word deficit signature.  For every one of the
three representatives, the two local domains are identical:

```text
first residual cut: 15 signature representatives,
second residual cut: 7 signature representatives.
```

All `15 * 7 = 105` occurrence-disjoint cross-pairs are replayed.  For every
representative:

```text
exact carriers: 0,
minimum bad rows: 2,
unique minimum-geometry pair: source 3541 length 8 and source 5676 length 8.
```

Thus internally rethreading bounded physical packets does not pay either
residual charge.  The complete bad-row histogram, identical for all three
representatives, is

```text
2:1, 3:2, 4:4, 5:7, 6:9, 7:12,
8:20, 9:20, 10:14, 11:10, 12:6.
```

## Arbitrary-upper destroyed-witness ledger

Every one of the 105 pairs is additionally replayed against all arbitrary
upper targets.  The minimum upper-hole counts are

```text
V0=ab61: 23,
V0=e361: 23,
V0=eb60: 20.
```

The unique minimum-geometry pair is not the minimum-upper pair.  It destroys
25 upper targets for `ab61` and `e361`, and 22 for `eb60`.  In the latter
case the destroyed set is

```text
46eb 4779 477b 4f33 56d9 5753 6373 6a79 6b79 7373 8f3c
8f3e 8f7c 8f7e cf45 cf75 da56 db56 df45 e566 f566 f766.
```

The minimum-upper histogram for `eb60` is

```text
20:12, 21:21, 22:21, 23:25, 24:12, 25:7, 26:6, 28:1.
```

For `ab61` and `e361` it is the same histogram shifted by three:

```text
23:12, 24:21, 25:21, 26:25, 27:12, 28:7, 29:6, 31:1.
```

Hence this face is not merely unable to improve the two-row geometry: all of
its choices also incur substantial arbitrary-upper collateral damage.

## Scope

This proves an exact no-go only for the following family:

- one physical contiguous pre-flat packet of length at most eight is assigned
  to each of the two residual cuts;
- each packet may be internally rethreaded in any run-state-legal order;
- the two source intervals are occurrence-disjoint.

It is not a no-go for noncontiguous packets, longer packets, a different
service architecture, or an unrestricted K16 carrier.  Since all three
minimum outer-service representatives have now been exhausted with the same
geometry profile, the bounded residual-packet lane should be retired.  The
positive continuation is a global embedding or a different upper-complete
near-carrier, not a larger atlas sweep.

## Artifacts

```text
scratch/dp_k16_j3959_rethreaded_packet_domains_20260730.cpp
SHA256 cbaa434f79c7e342304afb8c6dc27859d167ad7e48981fbd07e75bec3badc19f

scratch/build_k16_j3959_three_minimal_v0_bases_20260730.py
SHA256 5e0d9785fec736e4e3e06292adf3124c5a5a914a3409a8b21c557d1c6be9fa49

scratch/audit_k16_j3959_three_v0_rethreaded_packet_nogo_20260730.py
SHA256 3bd2894f165b691d23fe066b300499f7d4aa931c75f4d9b7822579c03c15c010

scratch/k16_j3959_rethreaded_packet_domains_20260730/
  three_v0_m8.independent.audit.json
SHA256 870c035f256d403579ec19a2bc8f29b08c914856adc2d796c1fdeceb0f2f9752
payload 3a4c16d301d0bd903448188de8a811982b644c30e75c0b73ec2efd027fc96cd1
```
