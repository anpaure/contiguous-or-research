# R2 audit: K17 residence 1994 neutral C6 and activated star-C8 quench

**Date:** 2026-08-02  
**Status:** independent prefix replay PASS.  This is a full-q1 carrier escape
from literal residence 1994 to 1993, not a resident factor or a word.

## 1. Frozen input and producer witness

The input is the currently authenticated checkpoint

```text
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
  checkpoint_fullq1_escape_res1994/model
SHA-256 127f97f02d238215367a1d5291853e0dd7ecb6d2d227cfcfed1c365e68d5ebcd
```

Its current four-entry manifest has SHA-256
`0dc6f0fbba8b9d8e509811b329e02bd35ec6493d1b82c92cf28969bc26aef714`.
The historical seven-entry checkpoint binding is not used.

The producer emitted the ordered packet

| step | family | core | labels | old incidence variables | new incidence variables |
|---:|:---:|---:|:---|:---|:---|
| 0 | C6 | 7946 | 4,14,7 | 11156,42258,11437 | 11158,42261,11433 |
| 1 | star-C8 | 5914 | 11,14,15,13 | 11158,37889,68776,22443 | 11157,37887,68777,22445 |

Producer hashes are

```text
packet  415240ce187d0e2caadcbb3d5c7f43ce92914a19d08352444c579664d59b7538
model   a9f0d53bdee43fc5db770ecac57781899c4d0f4fbed3b83ca0ac8b6af00008dd
audit   e081853a125821c406804f6f6062fd2ddd328e928d9863b0365792b0bfd19d72
```

The producer sampled 24,484,930 schemas with seed 2026080219.  A sampled
search is not an exhaustion certificate; only the displayed witness is used
below.

## 2. Independent ordered materialization

The independent audit root is

```text
/home/amodo/or15/work/r2_k17_fullq1_res1994_bridge_quench_20260802
```

An independently compiled circuit materializer checked the C6/star-C8
formulas, phases, and literal applicability in order.  It emitted exactly two
prefix models and reported

```text
PASS_PACKET_MATERIALIZED length=2 root_applicable_singletons=1
```

Thus the bridge is a root-applicable singleton and the star-C8 is not: the
second primitive exists only after materializing the first.  The independently
materialized terminal model is byte-for-byte equal to the producer model.

For each prefix, a separate extension/decoder rebuilt every ordinary pair
variable from the selected incidences, checked all 16,261 frozen guards,
decoded the augmented lollipop, both topology-derived openings, all ordinary
providers, literal residence, and ranks 10--17.  A second independently
compiled single-model auditor checked degrees, the protected boundary, one
component, exact provider multiplicities, and agreement with the passive
decode.

The exact results are

| state | model SHA-256 | ordinary q1 | opened rank-10 holes `(o0,o1)` | components | opened residence `(o0,o1)` | deeper holes `(r11,r12,r13)` |
|:---|:---|---:|:---:|---:|:---:|:---:|
| root | `127f97f0...` | 19412/19412 | (0,0) | 1 | (1994,1994) | (1520,271,4) |
| neutral C6 | `a73b5fe36e4bd7944c275ffefed5181d502370e9d08ef059c834f39b9fa8142b` | 19412/19412 | (0,0) | 1 | (1994,1994) | (1520,271,4) |
| activated star-C8 | `a9f0d53b...` | 19412/19412 | (0,0) | 1 | (1993,1993) | (1521,271,4) |

The full literal histories independently reconstructed are

```text
root:      o0=(1267,727), o1=(1268,726)
prefix 1:  o0=(1268,726), o1=(1269,725)
prefix 2:  o0=(1268,725), o1=(1267,726)
```

Each ordered pair is `(number of length-1 runs, number of length-2 runs)`.
The ordinary short-component/seam counts are respectively

```text
prefix 1: [0,1268,724] and 12 seam components
prefix 2: [0,1267,724] and 12 seam components.
```

Independent hashes are

```text
materializer source 184c9db6911d99b4f821108ddfda4cf27531cb08c0289bb279fd4837fe02b49f
materializer binary d00771db6dfe02ee8481e108085472e3553718649592468f24aca178b96ef2db
model-audit source db51016a56f6f2dec6701fc123ea662a410bdbe64f140132e9192b22d4bd35fb
model-audit binary ddc2488428075bbad450e7c67d7a7adc34f9e77a1ff91c0ebfd2551e8e2aee01
prefix-1 audit 934dbf0d9ff2b908d9b783c10bf1999eb02a1ca82df434db1edd4891119bc4d7
prefix-1 passive 569ce1d005d7f714618ae894fcb506ff6a79a4ff7caf7fa98174ff9ed8b453be
prefix-2 audit eb54a9bd5a06e32878d8c9c3f7415c9ab97e5199848c653e7c8f4e3947ca6874
prefix-2 passive ba04d2df64a0d7087dbac0668fd7d3a9a5d8f359775ec168cb163a4694ee7dbb
endpoint-audit source 3132df75c945dffd63188ea3f0d82bc183a26f3210f9c520b98c9e4b7a141cea
endpoint-audit binary e1dd2b9fc5a15d00e0f865205dcb40329a300287bef05879bc237bf0d8940b12
prefix-1 endpoint audit 8fa3660db40639a0c1542a3f8f012d1c74cacc709b68d58ff0e22618fde6a1cb
prefix-2 endpoint audit 87b5b268bfe536310c618448c3e829626e35c8b2a36990eb2bb0414ceccfc2f4
INPUTS.sha256 4d09670bfe085fd33925bb67c09faa8c12e60ab7a7389bb66b41dee0dfb5b5ce
AUDIT_OUTPUTS.sha256 b4a84a2ba25e7b2795d07664e96b0cdb5963f4f3a53ba8f7385cfe1940cff2e3
```

The independent topology decoder also records the literal opening frames:

```text
prefix 1: (start,cap)=(33023,41215), (65791,73983)
prefix 2: (start,cap)=(8447,73983),  (33023,98559)
```

Thus topology and seam roles were regenerated, not inherited from the root.
At both prefixes the exact degree vector is `(M,D,ordinary)=(1,3,2)`, every
owner has degree two, and the protected-boundary truth vector is
`(M->B,D->B,(B-0)->B)=(1,0,1)`.

## 3. Exact pair-channel activation

The two circuits overlap at the ordinary root `L=7962`.  At the frozen root
its selected incidences are

```text
y11152 : 7962 -> 7963   (insert coordinate 0)
y11156 : 7962 -> 8090   (insert coordinate 7).
```

The neutral C6 changes the second slot from coordinate 7 to coordinate 14;
the activated star-C8 then changes that same slot from coordinate 14 to
coordinate 13:

```text
selected extension coordinates: {0,7} -> {0,14} -> {0,13}
rank-10 pair colours:             8091 -> 24347  -> 16155
pair variables:                p263326 -> p263328 -> p263327.
```

Consequently the layerwise exact pair currents are

\[
 \Delta p_b=-p_{263326}+p_{263328},\qquad
 \Delta p_q=-p_{263328}+p_{263327},
\]

and the endpoint current is

\[
                 \Delta p_{bq}=-p_{263326}+p_{263327}.        \tag{3.1}
\]

The intermediate channel `p263328` cannot be deleted from the proof: it is
the literal pair assignment on which the prefix guards and provider rows are
evaluated.  At incidence level the quench deletes `y11158`, which is absent
at the root and installed by the bridge.  Therefore the quench is not a
legal root singleton.  This is a state-relative activation, not a padded
direct improvement.

Equivalently, with bridge current `z_b` and quench current `z_q`, the exact
quadratic update

\[
p(y+z_b+z_q)-p(y)
=p(y+z_b)-p(y)+p(y+z_b+z_q)-p(y+z_b)
\]

contains the cross current
`z_b(u)z_q(v)+z_q(u)z_b(v)` at the shared root.  Recomputing `p` from each
materialized incidence state is the fail-closed implementation.

## 4. Sufficient bridge-quench condition

Let `X` be the hard face consisting of exact degrees and protected edges,
all rebuilt pair/guard rows, one connected lollipop, all 19,412 ordinary
providers, and all 19,448 opened targets in each orientation.  Let
`R(F)=(R_0(F),R_1(F))` be the two literal residence scores.

The following check is sufficient for a strict escape from a root `F`:

1. a positive circuit `b` is incidence-applicable at `F`;
2. `G=F+b` lies in `X` and `R(G)=R(F)`;
3. a circuit `q` is incidence-applicable at `G`, with a bridge-installed
   deletion `A_b intersection D_q` nonempty (or, more generally, a nonzero
   exact pair cross-current);
4. `H=G+q` lies in `X`; and
5. `min_o R_o(H) <= min_o R_o(F)-1`.  A convenient stronger test is
   `R_o(H)<=R_o(F)` for both orientations with one strict inequality; because
   the present root has `(1994,1994)`, either terminal orientation below 1994
   already suffices.  This witness is strict in both.

Then `min_o R_o(H)<min_o R_o(F)` by condition 5.  The proof is literal:
conditions 1--4 retain every hard claim at both prefixes, and condition 5 is
the decoded strict decrease.
No additivity of local residence or pair deltas is assumed.

## 5. Exact scope

This packet proves a carrier with full immediate q1 and residence 1993.  It
does **not** prove depth-3 residence, and rank 11 worsens by one hole.  It
does not supply source antecedents, exterior chronology, the lower compiler,
opening/joining beyond the encoded lollipop, regeneration, or a contiguous-OR
word.  This unique-root audit replayed the frozen 16,261-row hard bank but did
not replay a later monolithic round-5 CNF (`full_round5_cnf_replayed=false`);
the separate activated-pair audit freezes that stronger formula replay.  The
producer search is not an exhaustive no-go for any absent packet.

## 6. Disjoint depth-four continuation

R2 also ran one unique O3 CPU witness search in the same persistent H100 root.
It was deliberately disjoint from the completed total-depth-at-most-three
lane:

1. the first primitive had to preserve residence 1994 in **both** openings;
2. any target reached at depth 1, 2, or 3 was rejected;
3. the only accepting depth was exactly four;
4. every prefix rebuilt pairs, all guards, both q1 openings, topology, and
   residence; and
5. a target needed a nonzero exact bridge/quench quadratic pair cross-term,
   while no constituent could be a root face-safe target singleton.

The frozen source and binary hashes are

```text
source b4b1de0853fd3786b82658f4c8582929c6158f78439c8f935f2fa5e75615a59e
binary bb1c618fc1ef44d73a7f97fe870dae920ed1a9d0769280646c5f76389081375c
```

With seed `2026080227`, residence debt 4, deeper-hole debt 20, and complete
state-relative C6/star-C8/octahedral-C8 proposal formulas, all 100,000,000
random trials finished without an accepting exact-depth-four packet.  The
audit SHA-256 is

```text
aac0dfedeed18e0b737cd47cddef705a11892cec84774da0a59b65257f6f427d.
```

The exact counters include 46 shallow targets rejected, 3 padded targets
rejected, 36,943 nonneutral first prefixes rejected, and 4,321 resets.  The
terminal file is the unchanged root model because the run found no witness.
This is a **sampled miss**, not a depth-four no-go or an exhaustive closure
certificate.
