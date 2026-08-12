# `k=17` round-02: independent authentication and physical classification of the 12 promoted escape cores

Date: 2026-08-02  
Lane: R2, read-only verifier  
Status: independently authenticated for the exact files and scoped claims below

This audit concerns only the promoted files at

```text
/home/amodo/or15/work/root_k17_round02_dualfan_socket_escape_20260801/q1_tests
```

No search, pricing, SAT solve, or remote write was performed.  The audit does
not assert that a second recut exists or that breaking one named core closes
q1, rank ten, topology, residence, deeper upper rows, or the compiler.

## 1. Canonical identities

The hashes of the three root tables are

```text
core_summary.tsv  d1336ed1131393f5bdfe10556718af7a5ddf838a1880ad36029ab643689998e3
summary.tsv       9793e3e7ba97f62112161258bef73ab04b60e359e631987977a0f2422a207554
drat_summary.tsv  39a4f41f4d2ecae4ad6273f86eed6de92d95dc6639e0f0355738265f3368f9c0
```

For a compact identity of the promoted bundle, run the following from the
directory above.  These are hashes of the sorted `sha256sum` listings, so
both the basenames and the individual file hashes enter the digest.

```text
sha256sum escape*.core.* | LC_ALL=C sort | sha256sum
  b1ce92ae40bd3a1d526f1ec9a5a6258f80ae33c5960ab5c75ebe865a56716159  -

sha256sum escape*.core.cnf escape*.core.lemmas | LC_ALL=C sort | sha256sum
  1270b854567cb9e74453412a189ebb92022142de730699c12c4f97d515d83a53  -

sha256sum escape*.core.lower_masks escape*.core.orientations.tsv \
          escape*.core.seams.tsv | LC_ALL=C sort | sha256sum
  f64e3ab36476195e5a6685bfc985cc98893a1468a47bb3e9540bd6b69704dedd  -
```

An independent local copy produced the same three listing digests.  Direct
read-only hashing also showed that all 12 actual bank, q1 CNF, and proof
files equal the hashes in `summary.tsv` and `drat_summary.tsv`, and every
corresponding root proof-check transcript contains `s VERIFIED`.

The promoted core formula identities are:

| child | clauses | retained proof lines | core CNF SHA-256 | retained proof SHA-256 |
|:---:|---:|---:|:---|:---|
| `e00` | 22 | 54 | `3ac26da7e6c011cb0a79afca71ad2876bf739bd69fa438f770f2e0b20529c493` | `44b2c109d7fe233e86ab821c9e2f265c9ba2d860aaf55fb69b3762d07c4fce09` |
| `e01` | 148 | 174 | `f8f6709d20ab158fd72135cf3d72f0faad1947cb61dca1f4350f5c14891b5325` | `ea961dfb3f8401d6f1b7e874cd3e844c21f859090091286a82dcceb0525af2d0` |
| `e02` | 148 | 174 | `0d22eb5d186bb33ee819584ebfaa495d3d017011adc97e41ffaea9306e288037` | `83fda54653deb34ef83411a2e5a241763c9a712d43c3b0c4ca4f734e59b3875f` |
| `e03` | 148 | 174 | `b41f5e3e84070fed4a08b20a995eb137558f88e7f679e5e7ea238766889989a9` | `8a0639af9c45c6a37db2567e81498aeb518294d453681481655a5b80f356b260` |
| `e04` | 148 | 174 | `9ae6b04ff811230a91ceb362467cab26db30982f223248ae248ba52e38d35891` | `e35588a077e6f0f73fa788ea3ebe95a41290fba0840872865e99b9fa740e683a` |
| `e05` | 175 | 182 | `b3e13736fa6e6fc36f0d43b2f3aa2192299093750e4a8203514f7d224556dc2c` | `1a6a9830024df01493eb2db991fe7020dc7a28d05a9710a7508b18541cff836f` |
| `e06` | 26 | 67 | `06c9649675b08936484aef1eb844ca0396eec0c712e3f743bb9288cc2bd14225` | `861a46b91e6436df388a70bdd3c91d9eca74e6362dc66af040b553d5ab7128dc` |
| `e07` | 168 | 197 | `3a84fdb2e08ea677174db885537e1466f01b90705da7ef9fd8f3bf9f0e2fb6f3` | `92b79d0d4c4b8944cf745435204913d1853e5bcd0eae8093990d81f4be63fce3` |
| `e08` | 156 | 155 | `4b69bb1c7cf6c263f0969e5172f40df4e8c5ee335ff21e44d70a6d4c30559883` | `da6763b8007a30f9ac07eb4f9804dc20bb3f6f26231315df5d2e3f00048a4e8e` |
| `e09` | 148 | 174 | `0dd94be3df57b64b795763a1cba48353d9182085c99cebb892ffb67d02905e3c` | `837f728ec264fc7de4f127fbedd3054cdff189a516afa980d672fef73756ced7` |
| `e10` | 148 | 174 | `f004f566727699bb0fac65ba8dbd44d0b6292e3c223c3bc337026704e0e44a0e` | `9268d522caa5421fc4a1f02dff703137585efa0065668415e7faf324b25a53cd` |
| `e11` | 182 | 124 | `469aebc98c42ee799813cc95c6e5d220d9e5d2000f19ee6c0b5b4b0faf9cb466` | `c9ba6bef4040478df6239976127bf6fab3025776411d3967d074d225060410a6` |

## 2. Independent proof and projection checks

The independent read-only H100 checker was
`/home/amodo/or15/drat-trim/drat-trim`, SHA-256
`92f0aa9575ed519d66a99b8b1b3dde6ece4618ae4c202a3a4b200265dda0aa7a`.
Each of the 12 pairs

```text
escapeXX.core.cnf  escapeXX.core.lemmas
```

independently returned `s VERIFIED`.  The checker reported

```text
e00 22/22/49     e01 143/38/1607   e02 143/38/1607
e03 143/38/1607 e04 143/38/1607   e05 142/41/1680
e06 26/26/66    e07 165/44/1650   e08 156/41/1765
e09 143/38/1607 e10 143/38/1607   e11 179/32/1825
```

where each tuple is retained original clauses / retained lemmas / resolution
steps.  Every replay used zero RAT lemmas and reported zero redundant
literals in the retained proof lemmas.  Separately, every retained core clause
was checked, as an unordered set of signed literals, to occur in the
corresponding full `escapeXX.q1.cnf`.  Every real retained seam and
orientation map row was also checked byte-for-byte against the corresponding
full q1 map.  Hence the tiny verified formulas are genuine unsatisfiable
subformulas of the authenticated full formulas; this conclusion does not
depend on rerunning a SAT solver.

There is one extraction defect.  The first row of every
`escapeXX.core.orientations.tsv` is a spurious parse of the DIMACS header.
Its alleged variable is respectively

```text
22,148,148,148,148,175,26,168,156,148,148,182
```

for `e00` through `e11`; each has zero occurrences in the corresponding
core body.  Dropping exactly this row leaves true orientation-row counts

```text
6,10,10,10,10,10,6,10,8,10,10,12.
```

No physical conclusion below uses the spurious rows or the similarly noisy
header tokens in `core.vars`.

## 3. Physical decoding

For a retained seam with rank-eight lower mask `c` and rank-ten upper mask
`u`, write `u-c={a,b}`.  Its unordered owner-mask endpoints are exactly

\[
                         c\cup\{a\},\qquad c\cup\{b\}.
\]

The directed state rows then distinguish physical endpoint occurrences.
This matters because a singleton or repeated-endpoint piece can contribute
two distinct socket resources carrying the same owner mask.

The complete classification is:

| children | primary colour | forced shore | exact physical graph | owner-mask quotient |
|:---|---:|:---|:---|:---|
| `e00` | `118996` | `R(1507)=127188`, `L(2078)=119028` | path `119508--127188--119004--119028` | same path |
| `e06` | `14820` | `R(3505)=14821`, `R(3789)=14828` | path `15844--14821--15332--14828` | same path |
| `e01,e02,e03,e04,e07,e08,e09,e10` | `115308` | `L(3924)=115310`, `L(7179)=119404` | `K_{2,7}` | `K_{2,5}` |
| `e05` | `115308` | same | same `K_{2,7}`, plus one pendant | `K_{2,5}` plus pendant |
| `e11` | `87145` | `L(1790)=87147`, `R(6616)=119913` | `K_{2,9}` | `K_{2,6}` |

For the `115308` class, the seven physical leaf occurrences are

```text
R(704)=115436;
L(3923)=R(3923)=116332 as two distinct resources;
L(4066)=117356;
R(6223)=115309;
L(6972)=R(6972)=123500 as two distinct resources.
```

For `e11`, the nine leaf occurrences are

```text
R(640)=87657;
L(2714)=R(2714)=95337 as two resources;
L(2949)=89193;
L(3950)=R(3950)=87161 as two resources;
L(3952)=R(3952)=87273 as two resources;
R(6124)=87149.
```

The `e05` extra retained seam has lower colour `117348` and joins
`L(4066)=117356` to `R(1262)=125540`.  It misses both forced shore sockets,
so it does not enlarge their colour neighbourhood.

In every row, the two shore resources are forced, no retained seam joins
them directly, and every retained seam incident with either shore resource
has the single primary colour.  Thus, for the displayed shore `Y`,

\[
                       |\Gamma(Y)|+\nu(E[Y])=1<2=|Y|.
\]

All 12 promoted cores therefore contain a one-colour **dual fan**.  None is
a primal fan.  In particular, the older core labels for `e06,e07,e08,e11`
must not be reused for this later root extraction.

The row-by-row frozen classification is
`scratch/r2_k17_round02_root_12_escape_core_classification_20260802.tsv`,
SHA-256
`917c98a35e7b0b7a9523764eb10138926566765cef0fa85447a02ecc9990370a`.

## 4. Exact second-recut promotion test

For a literal two-cut rebuild `D`, retain the same forced shore `Y={s,t}`
unless the rebuilt clauses prove a genuine role relocation.  Let an active
arm record its outside physical socket occurrence and selected lower colour.
The named dual-fan certificate is broken exactly when one of the following
holds:

1. a resident, resource-available direct seam joins `s` to `t`;
2. there are arms `s--x` and `t--y` with distinct lower colours and exact
   outside-resource compatibility: either different outside pieces, or two
   endpoint occurrences and opposite in/out slots of the same piece under
   one common path orientation; or
3. a literal forced-role replay relocates or internalizes one of the old
   shore resources.

This is the two-socket rainbow matching rank condition `rho_D(Y)=2`, with
role relocation handled as a change of the certificate's premise.  A safe
scan must rebuild the final bank before testing it: same-base alternatives
are incompatible, counterpart-split unary supports may disappear, palette
membership and geometry may be supplied by different recuts, and owner-mask
equality cannot replace physical socket-occurrence equality.

Only children passing all five scoped zero-265 ledgers and this exact local
rank test may be promoted to full q1 proof/model replay.  Passing is not a
q1 feasibility claim; failing with unchanged roles is an exact retained-core
UNSAT certificate.
