# K17 candidate1911: one-side second-circuit no-go through support ten

Date: 2026-08-01  
Lane: H2 exact local connector catalogue  
Status: **candidate factor authenticated; exhaustive one-simple-one-side
support-at-most-ten repair catalogue empty; mixed packets remain open**

## 1. Frozen connected factor

The support source is

```text
scratch/h2_k17_dev5_candidate1911.factor.tsv
SHA-256 c082621d6444dc2283675882557d0240babb989f2d31847eb198fbe8b4612587
```

Independent literal replay gives:

```text
D/H incidence rows:              1430 / 1430, perfect and edge-disjoint
quotient owner topology:          one 1430-cycle
voltage:                          9 mod 17
physical lift:                    one 24310-owner cycle
rank-8 edge colours:              1430 / 1430
upper rank-10 turn colours:       1144 / 1144
lower rank-7 turn colours:        1142 / 1144
lower holes:                      0x00e0f, 0x01547
positive runs shorter than four: 4352 = 1173 of length 2 + 3179 of length 3
```

Thus candidate1911 solves quotient/physical connectivity, rank 8 and upper
q1, but it is neither lower-q1 complete nor resident.

The independent base replay is frozen as

```text
scratch/audit_h2_k17_candidate1911_connected_factor_20260801.py
  SHA 1def852a7baa644a5da1a52f92ac63f4ab08e7e0cbb405872261608658aa8c69
scratch/h2_k17_candidate1911_connected_factor_20260801.audit.json
  SHA 906eca150fed88d5f5562de4e22f2a38143ec7c3666a24858b20ee036097d822
  payload 749e76afa52aaabc6b42c222ff1199ec051dc1265ecff83916f7d7cec38ebe56
```

## 2. Why the old closure obstruction does not apply automatically

Fix one matching shore `M` in `{D,H}` and hold the opposite matching fixed.
For an owner `u` and a literal incidence `e=(u,f)`, let `v` be the unique
owner whose current `M` edge occupies facet `f`.  The assignment arc is

\[
                              u\mathrel{\mathop{\longrightarrow}^{e}}v.       \tag{2.1}
\]

A simple directed circuit of these arcs cyclically reassigns exactly its old
facet set.  Hence `M'` remains owner-perfect and facet-perfect.  The opposite
matching remains perfect as well, so owner heads and the rank-8 facet palette
are already balanced.  Candidate1911 therefore has valid owner/rank-8 closure
circuits; the earlier fixed-J7 empty-closure theorem is not inherited by this
factor.

The remaining exact rows are:

1. exclude a new incidence equal to the fixed opposite-matching edge;
2. replay every changed rank-7 and rank-10 turn with its stored phase;
3. require positive final load for all 1,144 targets on both shores;
4. traverse `H'^{-1}D'` and require one quotient cycle; and
5. require nonzero total voltage for one physical lift.

The frozen census deliberately allows every voltage and first filters only
quotient connectivity and the two complete palettes.  Its empty result is
therefore stronger than a voltage-nine-only no-go.

## 3. Completeness of the targeted support-ten catalogue

Each missing lower colour has exactly ten raw provider assignment arcs on
each shore:

```text
                    0x00e0f providers   0x01547 providers
D side                       10                  10
H side                       10                  10
```

Any final repair must introduce each absent colour at a changed lower-turn
center, so it contains at least one of these forty provider arcs.  The DFS
roots at every provider arc, follows every displaced-owner assignment arc,
retains parallel phase incidences, and closes every simple circuit with at
most ten owners.  It rejects only a repeated owner, an opposite-edge
collision during literal replay, or the support cap.  Cyclic duplicates are
removed by the complete owner/incidence assignment map.  Consequently every
single simple `D`-only or `H`-only assignment circuit of support at most ten
that could repair candidate1911 is enumerated.

The exact combined-shore census is:

| support | assignment circuits | upper-palette safe | connected and upper-safe |
|---:|---:|---:|---:|
| 2 | 1 | 0 | 0 |
| 3 | 3 | 0 | 0 |
| 4 | 18 | 1 | 0 |
| 5 | 90 | 2 | 0 |
| 6 | 528 | 8 | 0 |
| 7 | 3,383 | 21 | 6 |
| 8 | 22,512 | 81 | 0 |
| 9 | 154,929 | 260 | 36 |
| 10 | 1,062,432 | 900 | 0 |

All 1,243,896 emitted assignment maps replay as valid matching circuits.
There are **zero** connected, upper-complete circuits whose lower palette is
complete.  In particular, no one-simple-one-side circuit through support ten
repairs both named holes while retaining the already solved topology and
upper q1.

Even supports have no connected survivor, agreeing with the independent sign
law: composing a 1,430-cycle with an even-support assignment cycle reverses
the required permutation sign.  This parity check is diagnostic; the exact
literal traversal is the acceptance test.

## 4. Best debt transport, not repair

The best connected upper-safe row is a D-side support-nine circuit:

```text
owners:     426,425,230,602,636,396,125,406,428
new edges:  3838,3832,2076,5422,5724,3564,1128,3657,3855
upper holes: none
lower holes: 0x00755,0x01547
physical components: 1
short positive runs: 4471
```

It transports one lower debt and leaves total debt two; it also worsens the
residence count from 4,352 to 4,471.  It is not a candidate construction.

## 5. H100 run and fail-closed status

The exact run used one H100 CPU core (`taskset -c 47`, `nice 19`), an O3
native binary, a 4 GiB virtual-memory cap and a 1,860-second external cap.
It exited zero and wrote `PASS_EXACT_COMPLETED`; no cap fired.  A cap or
abnormal exit would have been recorded as `UNKNOWN`/fail-closed rather than
as an empty catalogue.

Remote run directory:

```text
/home/amodo/or15/work/h2_k17_candidate1911_secondcycle_l10_b9c5f579
```

Local frozen bundle:

```text
scratch/h2_k17_candidate1911_second_cycle_l10_20260801/
```

Key SHA-256 values:

```text
frozen C++ source  b9c5f5797eee3d62628f66a51da49c568401ddff0136ed37adfa7485086562f6
H100 binary        e9439e2f7e662a517577020108ea4027448310a0c58977902d38447f447b40aa
factor TSV         c082621d6444dc2283675882557d0240babb989f2d31847eb198fbe8b4612587
audit JSON         95bfc5f866c20c3067c6b2c7923a5cc49869d033d34790e48ca04d64639cb1b4
candidate table    836f72ae8aa84689f1911460761764f6c77f524fa3ffbef09177a5241a18294a
run stderr         4eb76ad8bc6b0b69d431a74460999bc5d86d7665bdb4a4605091f34c44c2c6ee
exit file          9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
wrapper status     4e6fdc6b62d9769f6ca65022140ad72bcbbfbdc44db9122640d4cc81ae5d788e
```

The only compiler warning is a brace/indentation warning in JSON emission;
the independently reviewed statement sequence is unconditional as intended
and does not affect enumeration.

Independent fail-closed audit:

```text
scratch/audit_h2_k17_candidate1911_second_cycle_l10_20260801.py
  SHA b0a8d95ff6c17e9ac897928dc6c7ecf378226544d0e0c6aab9dd87b90d8d5b1
scratch/h2_k17_candidate1911_second_cycle_l10_20260801.audit.json
  SHA 921a1b89ed7ea2bc84784d7b9f61c21dc674451906000e106fdfaf12b633d84b
  payload 37471bdba5e5a79fed8d4df99ff2eb8f27659004ed877a40e6062002bf089932
```

The producer's `full_hits` predicate requires both palettes and one quotient
component but deliberately does not require one physical component or
residence.  Zero hits under this relaxation is proof-safe for the stronger
requested target; a positive hit would have required those extra checks.

## 6. Smallest compound control

The smallest packet not represented by one simple one-side circuit is two
assignment rectangles.  A direct-terminal census reconstructs the final
`D',H'` pair before evaluating any turn, so overlapping mixed rectangles and
removal of an old opposite-shore edge are handled correctly.  It finds 19 D
rectangles and 20 H rectangles.  Here a same-shore pair means two rectangles
defined relative to the frozen factor with disjoint owner pairs; a mixed
pair may overlap arbitrarily.  The exact packet counts are

```text
DD: 164 compatible / 147 terminal-disjoint; gains neither old hole
HH: 183 compatible / 165 terminal-disjoint; 18 gain only 0x00e0f
DH: 380 raw / 336 terminal-disjoint;       18 gain only 0x00e0f
```

No frozen-relative packet gains `0x01547`.  A sequential same-shore second
rectangle sharing one owner reduces to a simple three-owner assignment
circuit and is already included in the support-ten census above.  A return
on the same owner pair has 17 legal D terminal maps and 18 legal H terminal
maps; an independent replay finds that none gains either named hole.  Thus
the combined audits close every two-rectangle packet of union owner support
at most four, with the generator scopes kept explicit.

The independently frozen control is

```text
MATH_AUDIT_H2_K17_CANDIDATE1911_MIXED_TWO_RECTANGLE_SUPPORT4_NOGO_20260801.md
scratch/audit_h2_k17_candidate1911_mixed_two_rectangle_packets_20260801.py
scratch/h2_k17_candidate1911_mixed_two_rectangle_packets_20260801.audit.json
MATH_AUDIT_K17_CANDIDATE1911_MIXED_TWO_RECTANGLE_INDEPENDENT_20260801.md
scratch/audit_k17_candidate1911_mixed_two_rectangles_independent_20260801.py
scratch/k17_candidate1911_mixed_two_rectangles_independent_20260801.audit.json
```

Its theorem/script/JSON hashes are respectively
`6364389b27fd05943465ce224d24ec53604fcf40ede9fe63fcf8acee3c5831eb`,
`1b055add6d243275969eb668466683903d9e4428add5b8a4d14c998509e4ea84`,
and `f123097c85f5c4e7e7c91b946d28f6f8d43d5a9b58efd7f7047e055e663654ed`
(payload `9540edf7a503b4e4818c18858071acc281635c798da6f50c091716b7c8ab0dab`).
The independent note/script/JSON hashes are respectively
`d3e3f62ffe2986f9a57663f4acd21c808957e890953c36095a449ad21496b0f2`,
`1b664fff03b6c35414a9283a46f78aa75e0a53d2f3840dafe66cb7a7f62b43af`,
and `b6c003f3a2dc0dc8817d573d1aa5d747fbc1488ebe46f7e9bc15a59490d7b746`
(payload `07fb81b94772b30e6f12e84de0d3cb86e47dba99338b5d8efe63147d3c357709`,
status `PASS_FROZEN_RELATIVE_TWO_RECTANGLE_SCOPE`).

## 7. Precise open class

An exact marginal reduction was also run for the first genuinely compound
gate.  The two holes have respectively 86 and 90 canonical service atoms,
so there are 7,740 raw two-hole atom pairs before terminal interaction.  The
same-shore direct-provider menus contain 100 budget-feasible D pairs (46 of
even total support parity) and 95 H pairs (62 of even parity); the mixed
direct menu contains 200 pairs, of which 102 pass the support-ten budget and
parity.  This is **not** a Hall obstruction: marginal service exists.
Moreover, mixed service cannot soundly be reduced to the direct 10-by-10
menus.  For `0x00e0f`, 66 of 70 mixed service atoms are genuinely joint-only;
for `0x01547`, all 70 are joint-only.

The exact terminal laws for two assignment circuits are

\[
 H'=H\beta_1\beta_2,\qquad
 \pi'=(\beta_1\beta_2)^{-1}\pi,
\]

\[
 D'=D\alpha_1\alpha_2,\qquad
 \pi'=\pi\alpha_1\alpha_2,
\]

and, for one circuit on each shore,

\[
 D'=D\alpha,\qquad H'=H\beta,\qquad
 \pi'=\beta^{-1}\pi\alpha.                                      \tag{7.1}
\]

Hamilton parity requires even total assignment support.  All final turn
loads, topology and voltage must be replayed from `(D',H')`; isolated circuit
deltas cannot be added.  The frozen marginal reduction is

```text
scratch/audit_h2_k17_candidate1911_two_circuit_service_pairs_20260801.py
  SHA c36a42de2229cfba5fc448d9874b1dfe4ff807e3b4071a9443615f0ff5b73188
scratch/h2_k17_candidate1911_two_circuit_service_pairs_20260801.audit.json
  SHA 5f0d0be13529bddc0e639d0d8c26c78110afb86aa6e03fefa6bb83c074bcedfb
  status PASS_EXACT_SERVICE_ATOM_REDUCTION
```

It is a provider/menu reduction, not a two-circuit no-go.  The 7,740 pairs
still require a terminal-compatible circuit realization and joint literal
palette/topology/voltage replay.

This theorem closes exactly **one simple assignment circuit on one matching
shore with support at most ten**.  It does not close:

* two or more assignment circuits of total support at most ten, except for
  the two-rectangle support-four class just closed;
* a genuinely mixed `D/H` exchange larger than that rectangle class;
* a joint successor exchange not representable by one one-side circuit;
* one-side support at least eleven; or
* residence, ranks 11 and above, source/deep-shadow witnesses, opening, or
  common-cap/compiler compatibility.

The smallest live repair is therefore a three-or-more-rectangle packet, a
larger mixed exchange, or a two-cycle packet whose rank-7 gains cover
`0x00e0f,0x01547` and whose signed upper/lower losses, topology and voltage
are replayed jointly.  Independently, item2524D closes the single-one-side
class through support eleven, so its first open odd support is thirteen; it
does not close the compound classes above.  No global K17 conclusion
follows.
