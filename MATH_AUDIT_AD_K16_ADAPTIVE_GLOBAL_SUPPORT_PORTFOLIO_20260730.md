# K16 adaptive global-support portfolio beyond the closed joint fibres

Date: 2026-07-30  
Lane: AD  
Status: **two new fibres proof-closed UNSAT; bridge17 and S18 time-limited UNKNOWN; A21 exact and staged; no length-12873 word yet**

## 1. Frozen endpoint and scope

The authenticated universal word is

```text
answers/k16_upper12874.word
length 12874
SHA-256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e
```

The exact lower bound remains `nu(16) >= 12873`.  Thus a universal word of
length `12873` would close the problem at `k=16`.  Every model below fixes a
literal length-`12873` deletion source, names a finite set of zero-based
editable positions, permits an arbitrary nonzero 16-bit value at each named
position, and freezes every other position.  These are exact fibres but are
not WLOG over all length-`12873` words.

The closed joint13 model and the previously explored joint4/joint6 supports
are not repeated here.

## 2. Exact fixed-support compiler and monotonicity

For a word `A` and editable positions

```text
p_0 < ... < p_{s-1},
```

split `A` into its `s+1` fixed runs.  Targets already represented inside one
fixed run remain covered for every assignment.  Any other interval has a
unique first and last editable position `p_a,p_b`; its fixed contribution is
a suffix of the preceding run, all intervening fixed runs, and a prefix of
the following run.  For each attainable fixed base `B subseteq T`, the
interval has OR exactly `T` iff:

1. every editable value from `a` through `b` is a submask of `T`; and
2. their joint OR contains `T \ B`.

Introducing one witness variable for each dominance-minimal triple
`(a,b,T\B)` and taking the disjunction over witnesses is therefore an exact
CNF encoding of literal interval coverage.  Deleting a need which strictly
contains another attainable need for the same `(T,a,b)` is sound: every
assignment satisfying the larger need also satisfies the smaller one, whose
base supplies the remaining target bits.  The independent audit reconstructs
the complete clause multiset, not merely its row counts.

### Fibre monotonicity

If `P subseteq Q` are supports on the same source, then the `P` fibre embeds
in the `Q` fibre by assigning each cell in `Q\P` its incumbent nonzero value.
Consequently:

```text
UNSAT(Q) => UNSAT(P),       SAT(P) => SAT(Q).
```

The reverse implications do not hold.  This elementary fact is used below
to avoid solving nested smaller supports after a larger one is proof-closed.

## 3. Novel-H2 adaptive8 and adaptive10: verified UNSAT

The source

```text
scratch/k16_delete6440_novel_h2_20260730.word
SHA-256 a1c9ec8d4e2b22b2fa20af1d0c96a33591b273f730814e1011f7bcd159e928fe
holes {0x287d,0x546d}
```

has the exact phase axis at position `3`, where eight minimum-debt values
replace `0x546d` by `0x766d`.  Two topology-derived supersets were solved.

| fibre | editable positions | vars | clauses | result |
|---|---|---:|---:|---|
| adaptive8 | `{2,3,4,528,532,5934,6438,12872}` | 745 | 10,833 | verified UNSAT |
| adaptive10 | adaptive8 `union {5921,6441}` | 1,185 | 17,372 | verified UNSAT |

Position `5921` is a phase-stable `0x287d` portal with best debts
`{0x2939,0x293d}`.  Position `6441` is phase-coupled: it provides `0x546d`
in the parent and `0x766d` in every one of the eight phase children.  Thus
adaptive10 is a genuine topology extension of adaptive8, not a second seed
on the same support.

Authenticated proof bundle hashes are:

```text
adaptive8 CNF   97c682944ede7d6d19367bebbc3d2f42bb2c1e8c015bf36f5e9a1e36f3875ff1
adaptive8 DRAT  2fd63cd06aecb30fb0864bdf4643f581f090add54cde6d4d780f637813b1816e
adaptive8 LRAT  d0e434159d01502b06e7639ce73dce6947c75bf44fe8f9be03a497efcba58d56

adaptive10 CNF  ef9f2721063d0ed431844b23dbdcd195b471e92c76ffd873573ef20687515fc2
adaptive10 DRAT c6be3336b17cbe1875c78f23bd3dcf4aab67098b96ca7158708eca99cc0f17f3
adaptive10 LRAT 8f697c67757622e94861de096b3c90e0afef2c26dfafa8c066dcfe9936c6f0a7
```

For both bundles, `drat-trim` returned `s VERIFIED`, and `lrat-check` checked
the generated LRAT against the full original CNF and returned `c VERIFIED`.
The adaptive10 trimmed input core retains all 77 target-support clauses and
15,899 of 17,372 clauses.  It is therefore a valid dense scoped core, not a
small semantic obstruction; no minimality is claimed.

## 4. Deletion-6441 fork theorem

Delete zero-based cell `6441` from the authenticated upper word.  The result
is

```text
scratch/ad_k16_upper12874_lowhole_delete_sub1_20260730/basin_delete_p6441.word
SHA-256 387beaada1065208f2a7c49d4e1ed0132044c10f05b34d692cd652f9c615e79c
holes {0x946d,0xa86d,0xd46d}.
```

### Theorem 4.1 (exact one-cell H/L/C fork)

Among one-cell substitutions which install all three source holes, the only
physical sites are `2,3,6440`, and all such substitutions are exactly:

```text
p2:    0x8008 | s,  s subseteq 0x0065      (16 values),
p3:    0x8044 | s,  s subseteq 0x0029       (8 values),
p6440: 0x8044 | s,  s subseteq 0x0029       (8 values).
```

Their exact output hole sets are respectively

```text
p2    -> {0x246d,0x2c6d,0x346d,0x766d},
p3    -> {0x146d,0x246d,0x2c6d,0x346d,0x546d,0x766d},
p6440 -> {0x287d,0xa46d,0xb46d,0xf66d}.
```

Hence `{3,6440}` is the unique inclusion-minimal position support among the
exhausted one-cell full-provider families which exposes all three priority
modes `0x287d,0x546d,0x766d`.  Position `2` supplies an additional,
nonredundant output profile, but it is not needed merely to expose those
three masks.

#### Proof

Every newly installed source hole must have a witnessing interval crossing
the changed cell.  The new cell value is therefore a submask of each of the
three source holes, hence of their intersection `0x806d`.  The exact frozen
provider census
`scratch/k16_multiroot_deletion_portal_rank_20260730.tsv` (SHA-256
`fe51c4301cab3be93900a9f848082a8fd8a7336bf1d0f9016cb512df2f9a33d2`)
records three full-provider positions and 32 provider/value rows.  Literal
replay of all 63 nonzero submasks of `0x806d` at each of
`2,3,6440` produces exactly the displayed `16+8+8=32` rows and the displayed
hole sets.  Equality with both census counts proves exhaustion.  Only the
`p6440` family produces `0x287d`, only the `p3` family produces `0x546d`, and
the `p3` family also produces `0x766d`.  Therefore every position support
exposing all three modes must contain `3` and `6440`, while that pair already
exposes all three.  This proves the corrected unique scoped minimality claim.
It is not a WLOG theorem against multi-cell-only constructions.  QED.

The resulting nonlocal bridge17 support is

```text
{0,1,2,3,4,6,7,528,6438,6440,6441,6443,6444,
 11621,11624,11686,11689}.
```

Its exact model has 3,995 variables, 85,592 clauses, 200,704 literals, 107
repair targets, 3,706 witnesses and no impossible target.  The independent
clause-multiset reconstruction passes.  Its single H100 run ended with
Kissat status `s UNKNOWN` and exit code `0` after `1788.19` CPU seconds
(maximum RSS `110,264,320` bytes).  The exact classification is therefore
`UNKNOWN`, not SAT or UNSAT.  Kissat emitted an incomplete `2,054,352,194`-
byte proof stream with SHA-256
`5b31cc4b3e9af5e7359d4985f18789ae312e51fab0bdb2a4361a09189ad9a0b4`;
it is retained remotely for provenance but is not a proof certificate and
was not passed to DRAT/LRAT verification.

## 5. Two staged global escapes

### 5.1 Novel-H2 A21 collateral hull

The exact A21 support is

```text
{2,3,4,528,532,5921,5922,5923,5924,5934,
 6437,6438,6439,6440,6441,6442,6443,
 12869,12870,12871,12872}.
```

It closes the principal literal hulls

```text
[2,4]=0xa46d, [5921,5924]=0x293d,
[6437,6443]=0xfc6d, [12869,12872]=0xce63.
```

The emitted and independently reconstructed exact model has 6,804 variables,
173,781 clauses, 422,393 literals, 113 repair targets, 6,447 witnesses and no
impossible target.  CNF SHA-256:

```text
10f40c7bd93b9f094dc30dba0568fcdb15f78ffc691bfbd007323b3215628364
```

It is staged on `/home` but has not been launched.  Feasibility is `UNKNOWN`.
The optional A25 extension adds `{5930,5931,5932,5933}` and closes
`[5930,5934]=0x327d`; it would add exactly 16 repair obligations and is not yet
emitted.

### 5.2 Deletion-2 S18 third basin

Deleting zero-based cell `2` gives an independently replayed source

```text
scratch/ad_k16_delete2_s18_source_20260730.word
SHA-256 4004843c0f69bb673e603af44151a756776059bac3468fdff9d6c172f5d4b813
holes {0x246d,0x2c6d,0x346d,0x766d}.
```

The nonlocal S18 support is

```text
{1,2,3,166,169,170,172,527,530,531,533,
 5999,6001,6002,6003,6005,12871,12872}.
```

It contains the two complete provider sites `2,3`, authenticated partial
providers in three remote blocks, and the terminal context-opening pair.  Its exact
model independently matches the pre-emission calculation:

```text
variables 3858, clauses 68047, literals 150122,
repair targets 120, witnesses 3552, impossible targets 0,
CNF SHA-256 0dcc91c130a51991018ac11b5703f3abe0efcab7bebf2ddbde1ea8fcac897937.
```

It was run once on H100 and ended with Kissat status `s UNKNOWN` and exit
code `0` at the wall cap, after `1742.31` CPU seconds (maximum RSS
`125,206,528` bytes).  Its incomplete `2,385,197,439`-byte proof stream has
SHA-256
`2ef258f0aa7435a91de5d4f3583f113a47de6d641626f1e79686be9cc9d1f561`.
It is retained remotely for provenance but is not a certificate and was not
passed to DRAT/LRAT verification.  Feasibility remains exactly `UNKNOWN`.

## 6. Exact boundary

Proved here:

1. the adaptive8 and adaptive10 fixed-support fibres are UNSAT with checked
   DRAT and LRAT certificates;
2. the deletion-6441 full-provider fork theorem, including the unique minimal
   pair `{3,6440}` for the three stated modes;
3. exact, independently reconstructed bridge17, A21 and deletion-2 S18 CNFs;
4. exact fixed-support monotonicity and literal chronology semantics.

Not proved:

1. no listed support is WLOG for arbitrary length-12873 words;
2. bridge17 and S18 are time-limited `UNKNOWN`, while A21 is unlaunched
   `UNKNOWN`;
3. no universal length-12873 word has been found;
4. the exact bracket remains `12873 <= nu(16) <= 12874`.
