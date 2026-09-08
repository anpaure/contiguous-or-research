# K17 `h=1` static C6/C8 chain, one-hole checkpoint, and q1-zero model: independent audit

## Verdict

Three narrowly scoped claims are independently authenticated.

1. The saved `census0`--`census22` static chain is a literal sequence of
   guarded, connected, degree-preserving C6/star-C8 moves.  It raises the
   number of covered necessary non-`D` rank-ten colours monotonically from

   \[
   19341\quad\text{to}\quad19386,
   \]

   hence reduces that q1 hole count from `71` to `26`.  Exactly 45 formerly
   missing colours are installed and no previously covered colour is lost.

2. The later model

   ```text
   /home/amodo/or15/work/root_k17_q1_targeted_static_20260802/
     transport3_2.best.model
   ```

   SHA

   ```text
   be00a9d0b2470cd334a0b51476185c2ef61c99d28ce61b12f2ff32c26bcac213
   ```

   is a connected augmented `h=1` lollipop satisfying the complete frozen
   guard bank and covering `19,411/19,412` necessary non-`D` q1 colours.
   Its unique missing colour is decimal mask

   \[
   32058=\mathtt{0x7d3a}.
   \]

3. The successor `q1zero.independent.model`, SHA

   ```text
   b1fc0d9ca69c8411aad96557f5a47fe031616c88644f5d5691bec705b2b61a31
   ```

   is independently authenticated as a connected, degree-exact,
   guard-valid augmented factor covering all `19,412/19,412` necessary
   non-`D` q1 colours.  Thus the ordinary necessary q1 gate is closed.

None of these statements is a residence, complete-upper, source, lower-compiler,
or universal-word result.  In particular, this is **not** a K17 solution.

## Independent implementation

The audit source is

```text
scratch/audit_k17_h1_q1_targeted_static_chain_independent_20260802.cpp
SHA db51016a56f6f2dec6701fc123ea662a410bdbe64f140132e9192b22d4bd35fb
```

It does not include or invoke the targeted-search source.  Starting from the
raw incidence and pair-variable maps, it reconstructs:

- all `218,790` rank-eight/rank-nine incidence variables;
- all ordinary two-owner pair variables;
- the `16,261` frozen guarded clauses;
- the augmented-lollipop degree row (`M` degree one, `D` degree three,
  every other root degree two, every owner degree two);
- connectedness by a fresh BFS;
- the exact provider multiplicity of each of the `19,412` necessary
  non-`D` rank-ten colours;
- both literal linearizations of the lollipop and their residence/upper
  metrics.

The two machine-readable results are

```text
scratch/k17_h1_q1_targeted_static_chain_independent_20260802.audit.json
SHA 7f0d8ff9321fedb6a14671fa7a4d75f818af5f196b180da71fdae63407de61e9

scratch/k17_h1_q1_onehole_transport3_2_independent_20260802.audit.json
SHA b4401058201ed6cb40c0f3a16640d737da8ddd684ecc980f2e475ea6e2957f95

scratch/k17_h1_q1_zero_second_independent_20260802.audit.json
SHA 5de9fd0c869cbb69ac2d8861dcc0dee24f31c51198596bcd3c9380e499dbb251
```

## Complete static-circuit reconstruction

For each of the 23 saved pre-move states, the audit independently enumerates
the complete claimed geometry classes.

### Hexagons

A hexagon is determined by a rank-seven core and three of its ten exterior
labels.  Hence the complete number of geometries is

\[
\binom{17}{7}\binom{10}{3}=2,333,760.
\]

Both alternating parities are reconstructed directly from the incidence
map.  A move is retained only if exactly one parity is currently selected,
neither protected boundary edge is removed, neither exceptional root is
touched, and the complete frozen clause bank remains satisfied after the
literal toggle.

### Rank-seven-core star octagons

Choose a rank-seven core, four exterior labels, and one of the three
unoriented cyclic orders on those labels.  Thus the complete claimed star-C8
class has

\[
3\binom{17}{7}\binom{10}{4}=12,252,240
\]

geometries per state.  The same literal parity, boundary, exceptional-root,
and guarded-clause tests are replayed.

This is complete for the stated rank-seven-core four-petal star-C8 class.  It
is not a claim that every C8 in the whole incidence graph has this form.

For every round, every independently reconstructed retained-catalogue row
agrees byte-for-byte with the saved TSV row.  The JSON records an independent
FNV64 digest of each complete catalogue.

## Why the two-move replay is sound

The saved two-move steps require disjoint rank-eight root sets.  In these
incidence circuits, root disjointness implies disjoint changed incidence
variables and disjoint changed ordinary-pair variables.  It does not by
itself prove that two moves compose safely, so the audit still applies them
sequentially, checks every jointly affected guarded clause, and recomputes
connectedness on the final factor.

At every state the audit also reconstructs every eligible single and every
eligible root-disjoint pair and confirms the saved best score in that
restricted family.  The literal difference between consecutive saved models
has a unique decomposition into the recorded one or two catalogue moves.

The independently replayed covered-colour sequence is

```text
19341, 19343, 19345, 19347, 19349, 19351,
19353, 19355, 19357, 19359, 19361, 19363,
19365, 19367, 19369, 19371, 19373, 19375,
19377, 19379, 19381, 19383, 19384, 19386.
```

Equivalently, the hole sequence is

```text
71, 69, 67, 65, 63, 61, 59, 57, 55, 53, 51, 49,
47, 45, 43, 41, 39, 37, 35, 33, 31, 29, 28, 26.
```

There are two moves in every round except `census21`, which has one.  Every
move installs one new q1 colour and the union of covered q1 colours grows at
every step.

## Independent one-hole replay

The one-hole model has exactly `48,620` selected incidence edges and the
required complete degree row.  It is connected, keeps the fixed boundary,
and satisfies all `16,261` guarded clauses after reconstructing every
ordinary-pair channel from its two selected incidences.

Its provider histogram over the `19,412` necessary q1 colours is

```text
provider multiplicity: 0      1       2     3   4  5
number of colours:     1  15077    3833   466  32  3
```

The sole multiplicity-zero target is `32058`.  A fresh exact-q1 cut replay
reports

```text
required=19412 covered=19411 missing=1 cut_literals=45.
```

The 45 literals are the expected candidate root/provider choices for one
rank-ten target; their existence is not a proof that one can be selected
while retaining the other gates.

## Fresh extend/cut/passive pipeline

A fresh audit directory was created at

```text
/home/amodo/or15/work/root_k17_q1_targeted_static_20260802/
  audit_transport3_2_independent_20260802/
```

The no-anneal component/guard replay returned the input model byte-for-byte:

```text
replay.model
SHA be00a9d0b2470cd334a0b51476185c2ef61c99d28ce61b12f2ff32c26bcac213

replay.audit.json
SHA d48cc6fc8db79ca7824db22ad2251b90c1082eddcc7694bfe238a504d1903c26
```

The independently regenerated downstream artifacts are

```text
extended.model
SHA 7e9ff1a6702de4cb6712e3155c4fbba92bfec89a1963a8ceba56fc79da48c92d

q1.cuts.cnfpart
SHA f8e989dba147cb17f43dd540e005cf6ab45317cf1678f8458975ea05f484cace

passive.audit.json
SHA ae4516c45f7f0e613e9adc2bc1e9ec4fe5c8eca3863349b2bc307d81c3b44ca8

passive.cuts.DO_NOT_ADD.cnfpart
SHA 6a82f7282dcf6e51696b4c8a793f539f7c8cfd2dfa2d19feb5405859a1f72a34
```

The two literal linear orientations have respectively

```text
short positive q-runs: 2976+2608 = 5584
                       2977+2608 = 5585

upper holes ranks 10..17:
  [23,1532,286,7,0,0,0,0]
  [23,1533,286,7,0,0,0,0].
```

Thus the best orientation still has `5,584` short positive runs and `1,848`
upper holes.  The zero vector in the passive JSON field
`ordinary_upper_holes_10_17` is not an upper-completeness statement: in
`exacth1` replay mode that optional ordinary-component census is deliberately
skipped.  The literal orientation arrays above are the relevant evidence.

## Second independent q1-zero replay

The final q1-zero model was replayed under a second fresh prefix:

```text
/home/amodo/or15/work/root_k17_q1_targeted_static_20260802/
  audit_q1zero_second_independent_20260802/
```

The no-anneal connectivity/guard replay returned the input model
byte-for-byte.  The regenerated exact-q1 cut is empty:

```text
required=19412 covered=19412 missing=0 cut_literals=0.
```

The authoritative second-replay hashes are

```text
replay.model
SHA b1fc0d9ca69c8411aad96557f5a47fe031616c88644f5d5691bec705b2b61a31

extended.model
SHA f544cbc2a6c3bf9f9d7500202b4a60cb06660c3b5a1cdd382daec4d8dd4bbb90

q1.cuts.cnfpart (empty)
SHA e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

passive.audit.json
SHA b7d78582ca8f0aaeddbbb0413f00a95b569f2ba7c577dedcd94e57997684f0c2

literal independent audit
SHA 5de9fd0c869cbb69ac2d8861dcc0dee24f31c51198596bcd3c9380e499dbb251
```

The q1 provider histogram is

```text
provider multiplicity: 0      1       2     3   4  5
number of colours:     0  15079    3832   466  32  3.
```

The q1-zero repair does not close the other gates.  Its best literal
orientation has `5,586` short positive q-runs and upper holes

```text
[22,1533,286,7,0,0,0,0]
```

at ranks 10 through 17, totalling `1,848`.  Here the 22 remaining rank-ten
holes are among the 36 exceptional `D`-containing colours outside the
ordinary-q1 gate.

## Exact scope boundary

What is proved:

- complete reconstruction of the saved C6/star-C8 static catalogues;
- exact guarded and connected replay of the monotone `71 -> 26` q1 chain;
- exact factor/guard/connectivity/q1 authentication of the one-hole model;
- a second exact authentication of the succeeding q1-zero model;
- exact passive literal metrics for that model.

What is not proved:

- depth-three residence;
- complete arbitrary-width upper coverage;
- a depth-three source antecedent;
- any lower compiler matching;
- a universal word of length `24,313`;
- `nu(17)=B(17)`.

The correct finite conclusion is therefore: the necessary non-`D` q1 gate
is now complete inside this particular connected guarded `h=1` factor,
while the residence and deeper-upper gates remain far open.
