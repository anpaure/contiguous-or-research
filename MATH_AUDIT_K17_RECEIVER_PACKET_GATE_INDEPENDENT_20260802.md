# Independent K17 receiver-packet gate audit

**Date:** 2026-08-02  
**Lane:** independent receiver-bank C4/C6 and positive-calibration replay  
**Status:** PASS for the scoped finite claims below; no receiver-bank-changing
packet is promoted as socket-complete or composable.

## 1. Verdict

The corrected frontier separates cleanly into four different objects.

| object | structural | common-phase socket | supplier/private | chronology/composable |
|---|---:|---:|---:|---:|
| round-47 receiver-changing C4 | `304`, covering `150/162` | `0/304` full | not a packet certificate | no |
| round-47 residual receiver-changing C6 | `208` | `0/208` full | four all-P2 cases: private `4/4`, supplier `3/4` | no |
| private-b268 receiver-changing C4 | `256`, covering `128/162` | not completely priced in that table state | candidate-by-candidate phase-0 outer/ticket lift `256/256` | no |
| prefix C4 `565,649` | PASS | PASS | PASS in the declared frozen ledgers | positive calibration only |
| fixed-bank C6 `16269,16267,16271` | PASS | PASS | PASS in the declared frozen ledgers | positive calibration only |

The two positive calibrations do not contradict the receiver-bank no-go.
The prefix C4 moves two rank-six bottoms and therefore does not change the
rank-seven receiver bank.  The fixed-bank C6 cyclically reassigns three
rank-seven targets among the same three rank-eight receiver roots, so its
receiver set is unchanged.

## 2. Path-independent structural replay

A new C++ parser/enumerator was compiled with `g++ -std=c++20 -O3 -DNDEBUG`
and run on H100 under

```text
/home/amodo/or15/work/audit_k17_receiver_packet_gate_agent_20260802
```

It independently parsed both phase metrics, the 623-role fixed-root SCC
table, the complete 24,310-row target tables, the protected tickets and the
complete outer matching.  It reconstructed the 162 singleton-SCC rank-seven
zero roles rather than accepting the candidate files as input.

On the transported round-47 table it recovered exactly:

```text
receiver-changing C4 edges      304
covered singleton roles         150
uncovered singleton roles        12
maximum degree                    5
```

with uncovered IDs

```text
23021 23042 23046 23070 23336 23340
23471 23850 23955 23987 24051 24055.
```

The independently generated pair set equals `receiver_c4_edges.tsv`
exactly.  Enumerating every directed length-two C6 through those twelve
roles gave exactly 208 cycles, equal row-for-row to
`receiver_c6_cycles.tsv`.  Every cycle uses two nonreceiver roles.  The
classification is

```text
all-original-P2       4
one original F       60
two original F      144.
```

## 3. Exact socket-catalogue gate

A second independent parser checked every one of the 304 C4 output files.
For each file it reconstructed the old and crossed roles from the immutable
table, checked the row IDs and masks, and required each existence bit to
agree with its exact-hyperarc count.  The result is

```text
first crossed role common-phase positive   143 / 304
rank7-on-nonreceiver common-phase positive   0 / 304
both crossed roles common-phase positive     0 / 304.
```

It also checked all 72 distinct rank7-on-F output files used by the 204
F-containing C6s.  Every role has phase-0 count zero and phase-1 count zero.
The remaining four all-original-P2 C6s were checked against their exact
per-role ledger; every one contains a zero changed role.  Thus all 208
receiver-changing support-three cycles fail full common-phase completion.

As a raw-oracle calibration, the eight selected C6s in
`aligned_c6_sockets.tsv` were rebuilt and repriced from the 2,129,500-mode
potential union.  Their exact counts reproduced byte-for-byte and the
accepted count was zero.  The catalogue zeros use the exhaustive
relaxed-nine, four-flag, pairwise-compatible, exact five-cell-DP oracle.
This audit independently checks all frozen outputs and the exhaustive source
scope; it does not claim a theorem for a richer socket grammar.

For the four all-P2 receiver C6s, full supplier replay gives three survivors
and one exact casualty:

```text
16810 -> 3407 : 50 -> 0.
```

All four are footprint-disjoint from the 1,748 protected tickets and the
frozen private outer matching.  These resource ledgers remain separate from
the socket ledger; because every cycle is socket-zero, none is composable.

## 4. Private-b268 outer-ticket lift: sound but narrower

The private materialization is not the round-47 target table.  Relative to
round 47 it changes 15,449 target chains and 11,889 owners, while preserving
the root skeleton.  Independent enumeration on that table gives

```text
private C4 edges        256
covered roles           128
uncovered roles          34
F receivers used        204.
```

The outer replay checked all 18,646 selected edges as a bijection
(`16,898 H + 1,748 F`), all token bottoms and H/F receiver payloads, and all
3,495 ticket-forced incidences.  For every private C4 candidate, the old F
edge is unforced, the promoted row is unused on the right shore, and neither
changed row occurs in the protected ticket footprint.  Therefore the
delete-`L->Q`, insert-`L->R` update is a sound **candidate-by-candidate
phase-0 outer extension** for all 256 edges.

It is not a socket or supplier certificate.  Only 88 row-ID pairs overlap
the round-47 C4 catalogue, and only four have identical two-role
socket/owner signatures.  Conversely, exactly seven round-47 edges retain
the same private F lower; their dedicated ledger has `0/7` full socket
passes.  The remaining private-table candidates must not inherit the
round-47 zero theorem or be promoted as full packets without a table-bound
two-phase socket and supplier replay.

## 5. Positive controls

### Prefix C4 `565,649`

Independent exact replay verifies

```text
old  (4423,4943) + (4427,5455)
new  (4427,4943) + (4423,5455)
```

with the 65,535-target deck, roots, owners and row lengths preserved.  Exact
two-phase hyperarc counts reproduce as

```text
row 565: phase0 1829, phase1 1829
row 649: phase0 7377, phase1 1682.
```

The four frozen witnesses independently pass the five-cell DP.  The warm-47
supplier matching remains `16898/16898`; all 1,748 protected tickets and the
complete `16898 H + 1748 F` outer matching are untouched.  Both moved
bottoms have rank six, so this is a valid lower-rank packet calibration, not
a receiver-bank change.

### Fixed-bank P2-H-H C6 `16269,16267,16271`

Independent exact replay verifies

```text
old  81416-81417 ; 73216-81409-81413 ; 81408-81412-81420
new  81409-81417 ; 73216-81412-81413 ; 81408-81416-81420.
```

The target deck, owners, roots and row lengths are unchanged.  The new P2
role has exactly 3,899 phase-0 and 3,584 phase-1 hyperarcs, and independent
frozen witnesses pass in both phases.  Supplier replay remains
`16898/16898`; all 1,748 tickets and the complete outer matching survive,
including rechecks of both changed H receivers.  The three old and new
rank-seven receiver roots form the same set.  This is therefore a valid
fixed-bank correlated-column seed, not a singleton-SCC receiver-bank escape.

Neither positive control certifies one common selected occurrence,
chronology, history/guard clones, topology, residence, upper/source closure,
compiler feasibility, or a word.

## 6. Frozen bindings

Key independent source/output hashes are

```text
bc09625ad3168b45523f3be1db8856afb377b13c8451e2a59cd659c3ab5cbfc7  audit_receiver_structural_outer_independent.cpp
c2f48bd7c44c5440f9d1d2fa4a12c2dab4db8484ed1160c70b8b5fe57135a433  audit_receiver_socket_certificates_independent.cpp
cdf49cd0d1b8a2eeee79c46d9b7cad1fc4e4aeafcbee18c2d756f79bfcad6079  structural_outer.audit.json
d8c530bf2bea450789ef0d77e38fbcece4d32da91e498433bdebd28d1eaf3d89  socket_certificates.audit.json
310a62b95fab0caefb11de9d114f577f13b0a306a429aa653d80589738115187  prefix_c4.count_replay.txt
26dcae9f9a44a13a7340e3b591111c4333f8133df1c216c22f18bd81b98aad9d  prefix_c4.independent.audit.txt
7797ac71336cc1799c1756166489db38571380c7c2a6cd774817072323ba291f  prefix_c4.supplier_private.audit.tsv
5d02a34f0eabea6a39d16b07058744af387af0fde04af06de454d62bffd9d0c8  fixedbank_c6.count_replay.txt
fc65985e3a8f29fa62c2d1787cbff0ca41ffbb31a1d7d1998e0181c04ea59f32  fixedbank_c6.independent.audit.txt
698e9865bae2cde1c663d62dcee78e3759ccd2f8e54a1dab174ce556817d7829  fixedbank_c6.supplier_private.audit.tsv
```

The complete frozen tree, including all 304 C4 and 72 rank7-on-F output
files, is bound by `FINAL_MANIFEST.sha256` in the H100 audit root.  A local
copy of the scoped note and manifest is retained under
`scratch/audit_k17_receiver_packet_gate_agent_20260802/`.
