# Independent audit of the k17 all-opening primary Benders bridge

## Verdict

`PASS` for the stated source-stage and primary-cut scope.

The executable bridge does **not** claim that upper, Hall/DM, common-cap, or
word recourse has been executed.  Those rows are a fail-closed downstream
schema.  It does prove and export exact source-stage cuts for the frozen
`final2397` control.

## Authenticated inputs

```text
factor   eba52226952cda38d74e98fc7463f54640b0b59736ff88fc2949c8f0c02de1eb
model    9aa9c8137b4b90508aa255536a6f683bfa448b60de497b498f7119e432eb24ec
map      7b88292585cee9bb8e72a0017734f466f12aa7cb12c4507bec69b40484eb81f3
witness  88fe38dc68ca3345318e142386a389fe7ea3eb56794ede1ed4e01494c7b88403
```

The calibration model is the explicitly scoped sparse positive-primary
model.  Production `full-model` mode separately requires a complete model
and replays every clause of its supplied combined-master CNF.

## Independent determinant replay

All 35,713 option-map rows were checked for:

- rank-8 declared facet;
- two rank-9 physical endpoints;
- literal intersection and rank-10 union;
- canonical owner and cap orbit representatives;
- exact signed voltage.

The first 58 frozen marker bases with opening type 3 reconstruct all 232
fixed quotient rows and all 3,944 protected physical edges.  The sparse
model selects exactly 1,198 primaries, whose developments are exactly 20,366
unprotected physical edges.  The factor binding accounts for all 24,310
edges with no collision or omission.

Independent factor checks pass:

```text
rank-8 facets       exact 24310/24310
rank-9 degree       exactly two at all 24310 owners
rank-10 caps        complete 19448/19448
physical topology   one 24310-cycle
```

No counter, dart, history, or rank-11 auxiliary appears in an emitted
primary cut.

## All-opening replay

The independent verifier reconstructs the canonical owner cycle without
using the quotient map, witness, or SAT model.  It obtains

```text
length-2 positive runs     1292
length-3 positive runs     1105
total short runs           2397
directed openings tested   48620
source-valid openings      0
minimum residual runs      2395
```

Direction-one rows swap the cut endpoints.  The stable root key is the
directed physical endpoint pair; the factor-row edge ID remains diagnostic
only.  All 48,620 rooted source guards were replayed against an actual
unclipped short run.

## Two-run structural core

The bridge and a separate reconstruction find the same two coordinate-zero
paths:

```text
101166 - 101165 - 102157 - 109837 - 109838
128112 -  62577 -  62569 -  64553 -  64808
```

Both traces are `0,1,1,1,0`.  Their bracket edge IDs are respectively

```text
{19965,19978,20091,21754}
{12598,12615,12619,12838}
```

and are disjoint.  Two bracket edges are fixed protected developments.  The
remaining six translate exactly as follows:

```text
primary 15783, shift  8 : 101165--102157
primary 15802, shift  8 : 102157--109837
primary  7604, shift  4 :  62577--128112
primary 10293, shift 10 :  64553--64808
primary 10514, shift 10 :  62569--64553
primary 13179, shift  5 :  62569--62577
```

All six primaries are positive in the frozen model.  Degree two makes both
four-edge paths persistent whenever these activators remain selected.
Because one physical opening has only one cut edge, it cannot meet both
disjoint bracket sets.  The exact primary clause is therefore

```text
-7604 -10293 -10514 -13179 -15783 -15802 0
```

The source-core TSV and CNF hashes are

```text
9a352f5534cb3659e993f32a32522f7f24beaf8efaa3d299d85733b5305d0db3
029bc73fe0f277690a0ab62227e0cad8e3a90dd6748e1a86c617b128fd309209
```

The clause is valid on the fixed-bank, degree-two, single-cycle/one-cut
target face.  It is not an independently-opened multicomponent-forest cut.

## Fallback no-goods

The 1,198-negative-literal selected-factor no-good has SHA-256

```text
a551203a1df126ca3ac497e065e82b6f90b6b5435cf2181dde15d22500e6c1b0
```

On the authenticated exact-facet face it fixes the whole incumbent factor.
The complete signed 35,713-literal assignment no-good has SHA-256

```text
3b31e9015c08fee00c7fbc82b97fc8bf2626ab8d2a57cd10540e4affe5bea7ff
```

and is the fallback if constant selected cardinality is not reauthenticated.
Both clauses have exact sign and unique-variable censuses.

## Positive pass-through calibration

The k15 positive is inherited from the accepted generic fail-closed
source/compiler package, not run through the hardcoded marker58 bridge.  Its
explicit pass-through ledger is bundled and records:

```text
Hall                         16383/16383
dual exhaustive coverage    32767/32767
Benders verdict              PASS_WORD_DUAL_VERIFIED
cut emitted                  no
```

## Frozen package

```text
scratch/ad_k17_opening_benders_primary_interface_v4_20260802/
```

Manifest SHA-256:

```text
feabd0d4b7e254a28815179ccce9661cc0662d9cf3a0cbe683a162c7ed01415d
```

Principal implementation and independent verifier sources:

```text
63e43380a14c970249ee73890e3b620a6cf0af5dfd71247d8f6954a53059d4e7
3d25b015cb5f2a97ec0c6ceb9f1011478dc31b710f65ed5a45efc67e608ddbdd
```

Audit JSONs:

```text
5928b87d1f5d13ea494e5ef809848d44962c4f0577f94c5479070bb0250ec5ab
5401bbbba132892c178683d0c7eec4c532ce8078913c6f9c77c7818aa0c4538d
```

All files listed by the manifest verify.  Both O3 builds have empty warning
logs.

## Remaining exact boundary

The v4 executable closes determinant provenance, every-opening source
classification, rooted source-guard export, and the global source/factor
fallback clauses.  Its `deep_oracle_schema.tsv` is a contract, not an eager
implementation of upper or DM rows.  For a future resident candidate:

- a missing upper target needs an exact path/DFA witness formulation or a
  guarded full opening cube;
- a DM shore needs exact `P/U/M/nonempty` candidate activations before its
  deficit becomes a guarded row;
- common-cap UNSAT needs an independently verified proof/core;
- any unknown opening forbids a global incumbent no-good;
- SAT must still pass clause replay, exact derivative replay, and both
  exhaustive `2^17-1` scans before word emission.
