# R2 audit: K17 full-q1 escape packet and exact 2018-defect catalogue

**Date:** 2026-08-02  
**Status:** PASS for the promoted incidence factor, its literal four-move
packet, the frozen guards, full immediate rank-ten palette, connected
lollipop topology, both licensed seam orientations, and the exact terminal
coordinate-defect catalogue.  The factor is not resident: each opened
orientation still has 2,018 short positive runs.  No rank-11-plus completion,
source, compiler, exterior-window, regeneration, or word claim is made.

## 1. Frozen inputs and independent root

Promoted checkpoint:

```text
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
  checkpoint_fullq1_escape_res2018

model SHA-256       c8f961413aeea43cbad5036e801c08f854f84889eaef11c281aa83bea46c057d
passive audit       ea24de7b229b572ad2f25a3a03f96230b29266daf56c2daf5ce92435b2f331ec
independent audit   885f62c5b7689ada00970688a9771a5bcaa543657e3fae3d065aed3d1f41cb9d
promoted manifest   224499fd6c3df28d7f0c656a4a53dd73a7fc9b9467418e01f2c3adaef6880957
```

`sha256sum -c` passes for every row of the promoted manifest.  The new
read-only replay root is

```text
/home/amodo/or15/work/r2_k17_escape2018_auth_20260802
```

Its 19-row immutable-input manifest and 68-row output manifest both pass
literal `sha256sum -c` replay:

```text
audit.inputs.sha256   3c526b599b45b2c02aad6df30be87a0557460a5ea158fe377b8008d336904789
audit.outputs.sha256  f9c4d722d659038b8b40ced832bb39cfd536da4db16bb682f972923dabe0aba3
```

No move search or SAT solver was launched.  The O3 verifiers ran on one H100
CPU.

## 2. Literal four-move packet

The independently checked model trajectory is

```text
base model    5499b2fb492a6307e531bf33f20341a3e1c89c44cd45e0ee88ae6a8556c5e4fa
prefix model  748bc5cfe639028fd6642f044249740f333e5849556c9684af551e4f7356ef64
terminal      c8f961413aeea43cbad5036e801c08f854f84889eaef11c281aa83bea46c057d
```

The base-to-prefix literal difference is exactly the three old and three new
incidences of bridge C6 row 2508.  The prefix-to-terminal difference is
exactly the twelve old and twelve new incidences of the three stated C8
rows.  The three quench moves are root-disjoint.  Across the two stages the
bridge roots `16152` and `15672` are deliberately reused.

| ordinal | stage/id | core; labels | saved local data | roots | old incidence variables | new incidence variables |
|---:|---|---|---|---|---|---|
| 1 | bridge 2508, C6 | `15640; 5,7,9` | q1 score 0; opened 0; residence delta 0; connected alone | `15672,15768,16152` | `25943,26169,26860` | `26167,26862,25944` |
| 2 | quench 2446, C8 | `15128; 0,10,1,15` | q1 score 0; opened 0; residence delta -2; connected alone | `15129,16152,15130,47896` | `24702,26858,24713,87553` | `26857,24711,87554,24704` |
| 3 | quench 12688, C8 | `104194; 4,13,5,14` | q1 score 0; individual opened sentinel; residence delta -4; disconnected alone | `104210,112386,104226,120578` | `186038,199229,186075,210811` | `199228,186074,210812,186039` |
| 4 | quench 2243, C8 | `13624; 0,1,11,16` | q1 score 0; individual opened sentinel; residence delta -1; disconnected alone | `13625,13626,15672,79160` | `21223,25940,142666,21222` | `21214,21228,25947,142660` |

The last two rows are not admissible connected factors when applied singly
to the immediate post-bridge state.  In the promoted order
`2446 -> 12688 -> 2243`, however, the independent promoted-chain replay
checks guards, connectivity, positive ordinary q1 load, and both opened q1
frames after every prefix.  Thus the witness is a strict ordered synergistic
packet (and its endpoint also passes the weaker simultaneous terminal-batch
contract), not four independently feasible descent moves.

Frozen packet evidence:

```text
packet verifier source  bab51c2af4b4e65581819ad6850afd90d2ea4f35af53618bd1437aeffbffcd89
packet verifier binary  83472d635ff2bb6ce4d6d4ae800a9167bc8c2603ede6f9a01b645660b51f3bc9
packet.moves.tsv        862e90b734137c9160d6d12c9881179e61c21e0c14f3123713a831480aa23af4
packet.audit.json       460a086ad7823fa838f205ae6732be13bf49fc556a0791f93118f28b59e2574f
promoted-chain source   46e0ddaa3ccca27bc853d8ab27d9094614f900c81cf071cd09c0953978d8a22e
promoted-chain TSV      8ae21b56cec03e04386b3c2f8aad441ec1421e5c9f3387d3da744a4aaf9d2488
promoted-chain audit    4d0cac9a426125da2cbb5a3134b9b4b64f64cccbdd01f4907e7829c2575d3063
```

## 3. Endpoint semantic replay

Base, prefix, and terminal independently pass all of the following:

```text
selected rank8--rank9 incidences     48,620
frozen guards                   16,261 / 16,261
augmented incidence components            1
ordinary immediate targets       19,448 / 19,448
non-D immediate targets           19,412 / 19,412
D-superset immediate targets           36 / 36
opened palette, both orientations 19,448 / 19,448
cyclic palette, both orientations 19,448 / 19,448
```

The literal chronology changes as follows:

| state | ordinary short owner components `(1,2,3)` | seam-short components | opened short runs `(orientation 0,1)` | deeper holes per orientation |
|---|---:|---:|---:|---:|
| base | `(0,1280,743)` | 12 | `(2025,2025)` | `(1804,1804)` |
| prefix | `(0,1280,743)` | 12 | `(2025,2025)` | `(1803,1803)` |
| terminal | `(0,1276,740)` | 12 | `(2018,2018)` | `(1800,1800)` |

At the terminal, the per-orientation upper-hole vector for ranks 10 through
17 is

```text
[0,1518,278,4,0,0,0,0].
```

This explicitly refutes residence and arbitrary-width upper completion.

The terminal full-q1 replay has SHA-256
`e53c287c03bc870207ec3b6ae0d2864d111684e652d1d8973dfa4bf6a4d7c3ca`;
the self-contained q1/chronology replay has SHA-256
`f27bb8d4241aa304f1c4213edf3641ac5b06f7d9a23b832637d6a2c4f6106b51`.

## 4. Exact seam roles and defect TSV

The protected `D` owner bank remains

```text
[8447,33023,65791].
```

The packet changes the derived tail role from owner `8447` to owner `65791`.
The terminal tail contains 27,869 bipartite vertices.  The two exact seam
orientations are

| orientation | start owner | return owner | internal colour | closing colour |
|---:|---:|---:|---:|---:|
| 0 | 8447 | 33023 | 73983 | 33279 |
| 1 | 33023 | 8447 | 98559 | 8703 |

Each internal and closing colour has ordinary multiplicity one, and each
opened/cyclic palette is still complete.

The exact terminal TSV is

```text
/home/amodo/or15/work/r2_k17_escape2018_auth_20260802/terminal.defects.tsv
SHA-256 1e0ead134db6f82813b6f36e25f26b1b21574803fc9d6ba5ea966ebf49fd59ce
```

It has one header plus 4,036 data rows.  Fields are
`orientation, coordinate, begin, end, length`; path indices are zero-based
and both endpoints are inclusive.  Each orientation has exactly 2,018
maximal internal positive runs of length one or two:

```text
orientation 0: length1=1277, length2=741
orientation 1: length1=1276, length2=742
per-coordinate totals, either orientation:
[114,103,129,111,118,119,120,126,108,114,113,121,120,122,114,137,129]
```

The oriented defect row sets are not identical: their intersection has
1,146 rows and each orientation has 872 additional rows.  The terminal
coordinate audit SHA-256 is
`e85ff798540dafb61d57bf8f6862708b33d46a49fe74b85033e2bec31c52fab4`.

## 5. Fail-closed corrections and scope

The first packet verifier rejected the evidence because it assumed catalogue
edge order matched root order position by position.  Inspection of the saved
C6/C8 convention showed that only the two lower-root multisets are ordered
invariantly.  The corrected verifier checks both old and new lower-root
multisets, then checks the complete literal model differences.  The failed
log remains frozen as `packet.v0.err`.

An older promoted independent binary also ignored the requested
self-contained root sentinel and attempted to open `-/passive.audit.json`.
The already-frozen newer source, SHA-256
`13270117bb3c0a3f3d8cb26ed94dbef8e4268c63e23bc5f93c2716bc82e7f704`,
was compiled independently and used for the endpoint replays.  The failed
version-skew log remains frozen as `base.selfcontained.v0.err`.

The audited object is a nonresident connected incidence carrier with full
immediate q1.  It does not supply positive depth-3 residence, complete ranks
11--17, a lower/source antecedent, a terminal compiler, exterior opening
windows, regeneration, a universal word, or the contiguous-OR theorem.
