# K16 j3959: exact depth-three donor descent and residual absorber no-gos

Date: 2026-07-30  
Status: **exact constructive descent `12 -> 6 -> 3 -> 2`; bounded absorber
families closed; two-row residual remains open**

## 1. Source and scope

The starting chronology is the occurrence-conserving buffered compound path
of `MATH_THEOREM_K16_J3959_MINIMAL_SERVICE_BLOCKS_SIGNATURE_GRAPH_AND_DONOR_GAP_20260730.md`.
It has 12 reconstruction failures, no empty erosion cell, and unresolved
charge

\[
3e_{0001}+2e_{0100}+4e_{0010}+3e_{0200}.
\]

All searches below preserve the complete 12,873-row occurrence multiset and
use the exact variable-depth maximal-envelope replay.  They concern only the
specified contiguous-packet relocation families; they are not no-gos for an
arbitrary carrier or arbitrary braid.

## 2. Exact descent

Three physical donor moves give:

| stage | move | remaining bad rows |
|---|---|---:|
| baseline | — | 12 |
| 1 | move source row `p6395 = 4f31` to the `R2|R3` cut | 6 |
| 2 | move source row `p2830 = 5659` to the `R0|R1` cut | 3 |
| 3 | move the source block at `p2098`, `5e38 5f18 1f98 1fb0 1fe0 17f0`, immediately after `5659` | 2 |

The corresponding chronology hashes are

```text
12 -> 6  df730ba533dc6165faa4a609f3f489bac1bbb86dcdaf08e5181bb44530e9d13f
 6 -> 3  d73549903b175a5bee24c544958adb101cdb3e6b8ac4dbe6db42f9ecb3cc0811
 3 -> 2  4d944656a5c9809d81cedbcd921d26af8f86fe28e8060d0a176aedb4ccb86efc
```

The final two reconstruction deficits are exactly

| row | target | reconstruction | missing |
|---:|---:|---:|---:|
| 895 | `5e38` | `5e18` | `0020` |
| 3953 | `6a71` | `6a61` | `0010` |

All five service targets `ca79,ea79,eb79,4e79,6f79` retain literal interval
witnesses throughout.  The independent replay is

```text
scratch/audit_k16_j3959_depth3_donor_descent_20260730.py
SHA256 0b8dd1b227d6050fa888aa9fe88cff0fa0b44308c1528c0fd797cf1eac41b990

scratch/k16_j3959_depth3_donor_absorber_20260730/descent.independent.audit.json
SHA256 1afd965d7da43112bee8192cdde38b8ca644dc2e0aa5ddf2f051a179b5e56342
payload 037d2b0b7831918354ae4a74f46bb6cb148affab733858944cfb8adcc755a035
```

## 3. Exact finite censuses

### 3.1 First packet

Every contiguous pre-flat packet of length at most 6 was moved into each of
the three original defective cuts.

```text
generated 115587
flat-pass 115506
capacity-pass 115506
exact carriers 0
best bad rows 6
```

The best is the `4f31` move above.  Thus a single packet in this family
cannot absorb the full charge.

### 3.2 Second packet

Starting from the six-defect state, every contiguous pre-flat packet of
length at most 8 was moved into either remaining cut.

```text
generated 102728
flat-pass 102640
capacity-pass 102640
exact carriers 0
best bad rows 3
```

There are six recorded three-defect minima; the first is `p2830=5659`.

### 3.3 Third packet

Starting from that three-defect state, the same complete length-at-most-8
census has no exact carrier.  Its unique two-defect minimum is the six-row
packet displayed above.

### 3.4 One further contiguous packet

From the two-defect state, all packets of length at most 32 into either
residual cut were tested:

```text
generated 410144
flat-pass 409024
capacity-pass 409024
exact carriers 0
best bad rows 2
```

No such packet improves the state at all.

### 3.5 Physical singleton and two-packet faces

For each residual cut, a physical singleton domain was defined by requiring
the moved row to close the destination collar while retaining at most 12
global bad rows.  Both domains are empty.

For bounded multirow packets of length at most 8, the destination-closing
domains are nonempty:

```text
0x0020 cut: 190 packets
0x0010 cut: 135 packets
occurrence-disjoint cross-pairs: 25625
```

Every cross-pair was replayed exactly.  None improves the two-defect state;
there are zero exact carriers.  This is the smallest honest two-packet
absorber face after the descent, and it is closed.

## 4. Consequence

The 12-row obstruction is not monolithic: ten of its rows are eliminated by
three explicit occurrence-conserving donor moves.  The true residual is the
two-coordinate charge

\[
e_{0020}\text{ at }5e38 + e_{0010}\text{ at }6a71.
\]

However, this charge is not separable into two bounded physical packet
repairs.  A completion must do at least one of the following:

1. use a packet longer than 32 at one residual cut;
2. use a noncontiguous packet with internal rethreading;
3. revisit an earlier choice among the six three-defect minima so that the
   two source charges cross-cancel;
4. change the `6f79`/nested service atlas rather than repairing this branch.

The highest-value next exact search is therefore a joint search over the six
stage-two minima and two internally rethreaded residual packets, with state
equal to the two bit charges plus the five protected service tokens.  It is
strictly smaller than returning to the 5,166-by-port atlas or a free collar
SAT model.

## 5. Programs and remote result hashes

```text
scratch/census_k16_j3959_depth3_donor_absorbers_20260730.cpp
scratch/census_k16_j3959_second_donor_absorber_20260730.cpp
scratch/census_k16_j3959_final_two_singleton_absorber_20260730.cpp
scratch/census_k16_j3959_residual_two_packet_absorber_20260730.cpp
```

Remote result-table hashes, retained under
`/dev/shm/root_j3959_donor_absorber_20260730/`, are respectively

```text
result.tsv     8e2b20170939b00561c4921ac9bcb890859f47a4150c8ac93bb35d3e23b51e3b
result2.tsv    95074ac617b2dd9b15cef2c83260a1766c96e79852348ae6e63891754c061cb2
result3.tsv    5efc10d4a40703d4e90a1d29e60ac299a307908882400f685c349e5b683fc8e0
result4m32.tsv e1297e136b9ba4513bbe401651b88cb1dbb3038a812e086b26ab56177332cf7d
result5.tsv    8c19041e6ee61a207cbd98e84f5a2aaf0c9f05a1d3e8305b9ca19f6f93d1a3b7
result6.tsv    fb3bd3701efbb0b01873c76eb6610a884b129ac648d8bbc4cc4525eb6933b860
```

The mathematical counts are additionally pinned by the independently copied
candidate chronologies and the local replay in Section 2.
