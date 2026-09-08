# Audit: K17 h1 joint global q1 oracle and compiler gate

Date: 2026-08-02

## 1. Verdict

PASS for the claimed finite interface and deterministic replay scope.

The model-independent extension was built on the H100 host CPU, its complete
map and 6,112,317 clauses were independently enumerated, and the authenticated
71-hole and 26-hole factors were replayed as regressions.  A late factor with
zero missing colours in the earlier necessary non-D q1 census was also bound
and replayed.  It remains negative for the actual linear-opening gate, with
22 holes in each orientation, and fails residence and deeper uppers.  No
common-cap instance and no word were emitted.

The audit does not claim SAT or UNSAT for the merged central-plus-extension
formula.  No q1, residence, or compiler search was launched by this task.

## 2. Execution environment

All O3 compilation and all nontrivial C++ replays ran on the H100 host CPU:

```text
host:  arboghast
root:  /home/amodo/or15/work/ad_v5r_h1_joint_global_019fc04bf4d7_20260802
flags: -std=c++20 -O3 -DNDEBUG -Wall -Wextra -pedantic
GPU:   unused
```

The final builder, verifier, adapter, and control warning logs are all zero
bytes.  Representative peak RSS values were 209,380 KiB for the builder
compile, 261,432 KiB for the verifier compile, 114,792 KiB for the complete
26-hole verifier replay, and 66,552 KiB for the adapter replay.

The H100 filesystem briefly reached 100% while pre-existing q1 portfolios
wrote proof streams.  No file was deleted, truncated, or cleaned.  After
space became available externally, the existing audit root was atomically
renamed into the required `ad_v5r_*` namespace and all final work stayed
inside that unique root.

## 3. Source and binary binding

Final source hashes are:

```text
c6fc2bffb1c7ef745117943b7d59c4831f02c79a855097ab171f381c6cc0ea75  build_ad_k17_h1_joint_global_oracle_20260802.cpp
580057b6e87200f9126ff11d89e00ed3181addd3a6e552400b5a718e19a8a405  verify_ad_k17_h1_joint_global_oracle_20260802.cpp
c959b84cdcf11defc45661a844d03d2b089429f9788a753089bcbdbf8ec1f0e6  audit_ad_k17_h1_q1zero_compiler_adapter_20260802.cpp
ac432241c3baf8651080efb609c6f4d7dec64b6d10761cd175b651e1dae36605  audit_ad_h1_joint_global_oracle_controls_20260802.cpp
7f404855d3abb50a07e7fe13d1d9daf92fca00f878ca33913db1b7958e8945ba  build_ad_exact_source_compiler_pipeline_20260802.cpp
```

Final H100 binary hashes are:

```text
ad3cacb94891da184a5b0d42e83ed9e60e763601cce3c544fc993163907a0d29  h1_joint_builder
29f4da4f332fea3a70ff04eafc09ca4d1662040d69b8893059e9a22ac70d0436  h1_joint_verifier.final
06bb1676d9dcfeff516bfbd1a291c9cade96b5b647a88cc9cad5485758e96dd0  h1_compiler_adapter.final
6bc0f1d08befe85f3686bd5ce0c2ac961629bfc609ff5d0a85ad0a4f3565cb00  h1_joint_controls.final
```

## 4. Authenticated inputs

The exact base map and principal factor inputs are:

```text
d90eda6666629aad49a52247b07068d24d3e8da265f587dae55e864dca223d63  h1.map.tsv

645de2d68cb0b012bbea2d7f7027b7f62f86e9d4e43b9b70fceb22c60dc00a4a  h26.incidence.model
08c8794960d02c8c1b091206c551b80d1a6e0f07ec21dbc32d5e6d3a6efe9bf2  h26.extended.model
80af20fb0c5ae04a0335f7eee3e4da55efb166a5072152d24eafc2e40d0877da  h26.factor.audit.json
70ed7ac6cd23f5830639cc898224e34887982057e7614372d037ac2363897dbc  h26.q1.cuts.cnfpart
32edaf0fa9b8d771c4f6a71f96825192e31cbcc859248310102d50fe885cf36d  h26.passive.audit.json

0debc7f6aabfb30b9f69e13da39e3ca355f29206d7dec3e5592cc5544f7c4f63  h71.extended.model
5c4b9a9a3cb6fe2a0d4a17b02475a6aa092456dc356db8ab1edab085a1825b0f  h71.q1.cuts.cnfpart
ae9d9d7771dd1f11bdaf905bc5af96d4104d178333c6ab2cc9d2f084c3dae6e3  h71.passive.audit.json

addfb4b286268a574e64f91af1dccedfe9590f2c02dda438868343decf30f993  k7.conn.decode
```

The late ordinary-q1-zero factor is independently bound by:

```text
b1fc0d9ca69c8411aad96557f5a47fe031616c88644f5d5691bec705b2b61a31  q1zero.incidence.model
f544cbc2a6c3bf9f9d7500202b4a60cb06660c3b5a1cdd382daec4d8dd4bbb90  q1zero.extended.model
ef9859055fd91d3179ee4e9f22b18124b4227d674f4d3fb2f4e141b60be13a8e  q1zero.factor.audit.json
b7d78582ca8f0aaeddbbb0413f00a95b569f2ba7c577dedcd94e57997684f0c2  q1zero.passive.audit.json
5de9fd0c869cbb69ac2d8861dcc0dee24f31c51198596bcd3c9380e499dbb251  q1zero.literal.independent.audit.json
```

The independent sparse and complete copies are byte-identical across the two
external replay directories.  The exact necessary q1 cut is empty, with the
SHA-256 of the empty file, and its replay reports `19,412/19,412`.

## 5. Extension build

The builder independently regenerated all 218,790 base `y` rows and 875,088
base `p` rows before emitting anything.  Its terminal line was:

```text
PASS_AD_K17_H1_JOINT_GLOBAL_ORACLE_BUILD
  variables=2873695 extension_clauses=6112317
  targets=19448 ordinary_z=875088 exceptional_zd=160 used_roots=24308
```

The generated payloads are:

```text
1e0d1662230a51c294c829aae2be6b03531d84ab19666c531554affcc7adebee  h1_joint.extension.cnf
5217046c68f46ef680e3f986626a1f10573dc277089fb38f10880a7ee95d5715  h1_joint.variables.tsv
fd3aa57611b79456a0e151dffe36071a5b0d521122ac630f05e79abfa9dee9fd  h1_joint.builder.audit.json
```

The CNF has 6,112,317 body clauses, 16,537,210 literals, and no empty clause.
The variable map has 1,779,817 extension rows.  The builder audit was
published last, after both payloads were flushed, fsynced, hashed, and
installed without replacement.

## 6. Independent K17 replays

The verifier does not trust the builder's declared counts.  It reconstructs
the complete extension map universe, replays every CNF clause, rebuilds the
base factor from `y`/`p`, derives both D orientations, and directly compares
rank-ten interval unions with the physical occurrence census.

Without a total merged extension assignment, the exact status is

```text
PASS_K17_H1_JOINT_ORACLE_DETERMINISTIC_NEGATIVE_Q1_AUDIT
```

and both `q1_zero_claimed` and `word_claimed` are false.

### 6.1 Supplied 26-hole incumbent

The signed-y input and the independently extended full model agree:

```text
ordinary necessary non-D holes: 26
opened-literal holes:            48 / 48
physical-cycle holes:            47 / 47
extension clauses replayed:      6,112,317
```

Audit hashes are:

```text
3523dbe81b68588fdf6444bfc8d0d5fde943cffeb16c7767b8d4a13d52622e2a  h26 sparse verifier audit
c9e277616ff80b63df5bd8ab16c7c3ce6af1c2af1c771e102e473038c3129a56  h26 complete verifier audit
719b723ae65f81ee1d36275eb3692469001cc544ad5db5562a318ffd74f3f195  h26 compiler-adapter audit
```

The adapter exactly reproduces:

```text
orientation 0: short=5574, upper=(48,1534,288,7,0,0,0,0)
orientation 1: short=5574, upper=(48,1535,288,7,0,0,0,0)
status=Q1_NOT_ZERO, word=0.
```

### 6.2 71-hole regression

The regression remains distinct:

```text
ordinary necessary non-D holes: 71
opened-literal holes:            93 / 93
physical-cycle holes:            92 / 92
orientation 0: short=5576, upper=(93,1547,288,7,0,0,0,0)
orientation 1: short=5577, upper=(93,1547,288,7,0,0,0,0).
```

Its verifier and adapter audit hashes are:

```text
8fbd2bd612bc3fc283b4489c01290197895ae66c792e8e808819293198794d90
7dc8d7619efeca47602bee8f98194a4247d46009244bce3d04a894b91b578152
```

### 6.3 Late necessary-q1-zero factor

The earlier necessary non-D q1 replay is exact at `19,412/19,412`, but the
new literal/global replay gives:

```text
ordinary necessary non-D holes: 0
opened-literal holes:            22 / 22
physical-cycle holes:            21 / 21
orientation 0: short=5586, upper=(22,1533,286,7,0,0,0,0)
orientation 1: short=5587, upper=(22,1534,286,7,0,0,0,0)
status=Q1_NOT_ZERO, common-cap CNF=0, word=0.
```

This closes the requested integration test without overloading the old q1
metric.  Sparse/full verifier and adapter hashes are:

```text
a9cfafd326c2d2e098b8e36b6b17b63b7f96734bd118ed2f65a0b7d854b42102
ef94e5e2182fc01eed6302d69b315e3674efba7c9200dd72273ec46138bc0578
98855514fff36c61b1430cba79ed1672a79ee640eae5d71da83773ba6172e639
```

## 7. K7 global controls

Two independent executables consumed the authenticated 70-incidence line.
The verifier reports zero opened and cyclic holes in both orientations.  The
stronger control reports:

```text
augmented components=1, ordinary paths=2, q1=21/21
primary edges=21, primary components=14
residual edges=12, contracted rank=12, final components=2
I=4, J=10, c=15, forest 25>22, Benders 22>19, flow 25/28
73 legal replacements, 49 local-row improvements
best local row 20>19, best global flow 26/28.
```

Final audit hashes are:

```text
6318ecd6a16acc909927fe8011765b994aab15365b69ebe8d67d1bebda4b7e4a  independent K7 verifier
af7207f8865e210992c99f0100f23701e8366bef5aef248496d26d868497c189  joint K7 controls
```

The second row is the required finite countercontrol: improving one minimum
shore is not a global residual-completion oracle.

## 8. Downstream fail-closed review

The compiler adapter evaluates the two licensed chronologies separately and
in this order:

```text
opened literal q1 and short-run residence
all nonwrapping upper ranks 10..17
exact maximal source
complete lower P/U/M graph and Hall--DM
common-cap CNF/model
provider semantics, derivative, and two exhaustive 131071 scans.
```

The present K17 inputs all stop at the first line.  Thus no lower graph or
common-cap CNF is emitted for them.  `PENDING` and pathname-only
`UNSAT_PROOF` both become `COMMONCAP_UNKNOWN`.  The only word-writing path
requires a total SAT model, every regenerated clause, selected-provider
semantics, exact derivative, and both exhaustive scans, followed by an
atomic no-replace install.

The previously frozen all-opening v5 package continues to calibrate the
48,620 marker58 opening selectors, final2397 source-negative branch, K13
Hall--DM branch, and authenticated K15 common-cap SAT publication branch.
Those controls are not reinterpreted as `h=1` results.

## 9. External solver state

At the final integration snapshot one pre-existing CaDiCaL q1 portfolio
process remained live under
`root_k17_q1_targeted_static_20260802/exact_core`.  This task did not launch,
duplicate, modify, stop, or clean it.  External solver state is not a member
of the frozen package.

## 10. Nonclaims

This audit does not claim:

- a total satisfying assignment of the merged global extension;
- an authoritative common-cap UNSAT proof;
- literal residence for any current K17 factor;
- complete ranks 11 through 13 for any current K17 factor;
- source, lower Hall--DM, or common-cap success at K17;
- a K17 universal word;
- any value of `nu(17)`.
