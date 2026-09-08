# `k=17` R2 audit: marker-58 lower-rainbow two-factor extension

**Date:** 2026-08-02  
**Verdict:** `PASS` for the exact rank-9 owner/rank-8 lower-q1 factor and
opening-type-3 protected paths; `FAIL` for rank-10 completeness.  No
chronology or universal-word claim is made.

## 1. Frozen inputs and provenance

The audited factor is
`scratch/k17_marker58_q1_extension_20260802/marker58_q1_factor.tsv`,
SHA-256
`0eab1f3cb25d0704e86e614850b95dec7a14e5b3c12b69254e2a90b2af0bf09e`.
It is paired with the frozen 96-row marker witness, SHA-256
`88fe38dc68ca3345318e142386a389fe7ea3eb56794ede1ed4e01494c7b88403`;
the selection rule is literally its first 58 rows and opening type `3`.
The header plus those 58 rows has SHA-256
`903c04215e817fd0f499df998d6b9ca4a43460fb1fb56c5ca7c5ea6ad4cf6866`.

The announced verifier prefix `4a729a...` is not present in the checkout or
producer root.  The current producer verifier instead hashes to
`9c79af0ea259b055c8defa443c872c170383907ff225cf4805114431514007c0`.
It has a nonbinary-flag validation bug and a permissive witness parser, so it
was not used as the independent proof certificate.  The audit used the
separately written strict replay
`scratch/audit_ad_k17_marker58_q1_extension_20260802.cpp`, SHA-256
`cbd643dac784fa309ba3b20a292ca426fff8eaad4f2752f8583a1ad7551a2297`.

At the producer root, a fresh read-only stream from builder source
`3503bc5cf00c3da1bf1fb2fa8971720cbdf9abe6cea59ed50c298fb8e465d22d`
and binary
`1974f588248fe29f7057870cafaec3ae749027eec9d0206a15709c6c56378112`
with arguments `(witness,58,3)` reproduced the factor byte-for-byte.  The
authoritative updated producer audit and log have hashes
`9a9c2c4082924bc0593381d1ead6c14855d950f0bd74e6b10c7a68db54b5c9d0`
and
`160630ac07aebe8b32d3dd9a3634c09cc55af7da9af936ff780ec67e175040ec`.
The older local producer copies are stale and are not authoritative.

## 2. Independent H100 replay

The strict verifier was compiled only on H100 with
`g++ 13.3.0 -O3 -std=c++20 -DNDEBUG -Wall -Wextra -Wpedantic -Werror`
and run at

```text
/home/amodo/or15/work/r2_k17_marker58_q1_replay_20260802
```

The executable SHA-256 is
`b7f2f089690293c5e96f488e6c7ca4c504de74022b9e37ccf4d2b824106338db`.
The regenerated JSON has SHA-256
`518a96832053a78595ae8284d4b27b2a90e266876968ff18e07b5247e3491b5d`
and is byte-identical to the separately retained independent audit.

For every factor row `(colour,a,b,protected)`, the replay required a literal
binary flag, ranks `(8,9,9)`, `a!=b`, `a intersect b=colour`, rank-10 union,
and a previously unused lower colour.  It instantiated the complete rank-9
layer and required degree two at every owner.

## 3. Exact certified census

The resulting factor has:

| row | exact value |
|---|---:|
| factor edges | `24,310` |
| distinct rank-9 owners / degree-two owners | `24,310 / 24,310` |
| distinct rank-8 lower colours | `24,310` (the complete layer) |
| developed protected paths | `58*17 = 986` |
| protected path owners | `4,930` |
| protected path edges/colours | `3,944` |
| components | `1,179` |
| largest component | `16,643` |
| distinct rank-10 caps | `13,307 / 19,448` |
| missing rank-10 caps | `6,141` |
| rank-10 repeat units / maximum load | `11,003 / 6` |
| protected distinct caps / repeats / maximum load | `986 / 2,958 / 4` |

The complete component-size histogram is
`{3:1005, 4:23, 5:44, 6:41, 7:12, 8:7, 9:1, 10:6, 11:10, 12:15,
14:10, 15:3, 3410:1, 16643:1}`.  The global rank-10 cap-load histogram is
`{1:6317, 2:4162, 3:1711, 4:1050, 5:66, 6:1}`; the protected-only histogram
is exactly `{4:986}`.  These distributions are frozen in
`scratch/r2_k17_marker58_q1_replay_20260802/component_and_cap_histogram.tsv`.

The protected set was reconstructed from geometry, not trusted from the
flag column.  For each first-58 base mask and each of 17 shifts, the checker
formed the five rank-9 facets of its rank-10 support, opened the cycle at
type `3` in order `4,0,1,2,3`, and rebuilt the four Johnson edges.  It proved
the 986 paths have disjoint owner sets and required equality of the expected
and flagged edge sets, protected owner sets, and protected owner-degree
maps.  Thus there are no missing, extra, colliding, or differently oriented
protected edges.

Each opened marker path's four edges have the same rank-10 union.  Hence the
3,944 protected edges already contain 2,958 protected repeat units and only
986 distinct caps.  This makes the upper-q1 limitation structural in the
present binding, not a bookkeeping omission.

## 4. Exact scope

This is a simple spanning two-factor of `J(17,9)` with a perfect rank-8
rainbow and exact containment of the 986 opened marker paths.  It is not
connected: the component count is 1,179.  It is not rank-10 complete: the
deficit is exactly 6,141.

The protected binding covers only each module's five rank-9 owners and four
retained rank-8 q1 edges.  It does not bind the omitted fifth q1 edge, the
marker theorem's rank-5--7 targets, or its source/buffer occurrence labels.
Therefore it proves no source chronology, physical buffer placement,
residence, ranks 10--17 completion, component joining/opening, exterior
windows, or compiler/common-cap matching.
