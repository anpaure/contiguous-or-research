# Audit of the `K17` OPTIMAL28 fixed-skeleton static provider no-go

Date: 2026-07-31  
Status: exact upper-`q1` fixed-skeleton no-go; exact canonical width-three
lower-`q2` census; no full lower-`q2` no-go is claimed

## 1. Verdict

Fix the six-swap macro forest and the `133` singleton packet objects selected
by the OPTIMAL28 marked path.  Allow every one of the remaining `4872`
pure-`U` owners to choose any two capacity-positive incident ports.  Relax
owner degree coupling, port degree coupling, connectivity, residence, deeper
shadows, and the common compiler.

Even in this relaxation, the union of all possible upper-`q1` providers
misses exactly `218` of the `19448` rank-ten colours.  This is a genuine
fixed-skeleton literal obstruction: an interval of rank-nine owners whose
union has rank ten necessarily contains an adjacent pair with that same
union.  Consequently no reconnection of the residual `U` objects can make
this fixed object skeleton upper-`q1` complete.

The analogous canonical width-three lower-`q2` support misses `165` rank-seven
colours.  This second number is exact for intersections of three consecutive
owners, but it is **not asserted here** as a full literal lower-`q2`
obstruction.  The static master does not enumerate longer compiler intervals,
and this audit imports no theorem identifying all literal lower witnesses with
the canonical width-three row.  Any use of `165` as a global lower-hole count
would therefore be unsound without that additional theorem.

The two independent enumerations agree on the decisive dimensions

```text
residual pure-U owners                                4872
capacity-positive rank-eight ports                    5744
residual owner-pair z columns                       141255
demand-two same-port upper y columns                  80449
upper-q1 unsupported colours                            218
canonical width-three lower-q2 unsupported colours      165.
```

Thus the OPTIMAL28 complement/socket problem cannot be closed by residual
pairing alone.  At least one fixed macro/packet occurrence, an object interior,
or the literal compiler chronology must change.

## 2. Fixed object model

Let

\[
 \mathcal T={ [15]\choose 8},\qquad
 \mathcal U={ [15]\choose 9}.
\]

The fixed bank consists of `1430` macro paths and `133` singleton packet
objects.  Every object endpoint is incident with a port
\(T\in\mathcal T\).
For a port `T`, let `f(T)` be the number of fixed incidences and put

\[
                         d(T)=2-f(T).                 \tag{2.1}
\]

The exact demand profile is

\[
                    d(T):\qquad 0^{691}1^{1744}2^{4000}.       \tag{2.2}
\]

The packet uses `133` distinct members of \(\mathcal U\); the residual owner
bank \(R\) therefore has `5005-133=4872` members.  For
\(T\in\mathcal T\), write

\[
                  R_T=\{U\in R:T\subset U\}.          \tag{2.3}
\]

An admissible residual singleton `U` chooses two distinct ports among its
capacity-positive facets.  Ignoring global consistency gives one owner-pair
column

\[
                       z_{U,\{S,T\}}                  \tag{2.4}
\]

for every such pair.  The exact total is

\[
 \sum_{U\in R}{|\{T\subset U:d(T)>0\}|\choose2}=141255.        \tag{2.5}
\]

The number of columns per residual owner has profile

\[
 6^9,\ 10^{31},\ 15^{235},\ 21^{842},\ 28^{1937},\ 36^{1818}. \tag{2.6}
\]

## 3. Exhaustive upper-`q1` provider classification

Every adjacent owner pair occurs either inside a fixed macro or at one port.
The internal pairs are fixed.  At a port there are exactly three cases.

1. \(d(T)=0\): two fixed endpoint owners meet; their union is fixed.
2. \(d(T)=1\): one fixed endpoint owner \(A_T\) meets one selected residual
   \(U\in R_T\); the provider colour is \(A_T\cup U\).
3. \(d(T)=2\): two distinct selected residual owners \(U,V\in R_T\) meet;
   the provider colour is \(U\cup V\).

The third case is represented by

\[
                         y_{T,\{U,V\}},               \tag{3.1}
\]

and its unrestricted catalogue size is exactly

\[
                \sum_{T:d(T)=2}{|R_T|\choose2}=80449.          \tag{3.2}
\]

Independently, the residual-degree profile on the `4000` demand-two ports is

\[
                   |R_T|:\qquad4^3,5^{34},6^{522},7^{3441},   \tag{3.3}
\]

so (3.2) replays arithmetically as

\[
 3{4\choose2}+34{5\choose2}+522{6\choose2}+3441{7\choose2}
 =18+340+7830+72261=80449.                                   \tag{3.4}
\]

This classification is exhaustive because every port has final degree two,
and the only unfixed objects are residual singletons.  It is deliberately a
relaxation: the same residual owner may be used inconsistently in different
listed providers and endpoint capacities need not be respected.  Hence a
colour absent even from this union is impossible in every genuine residual
completion.

### Lemma 3.1 (adjacent-pair reduction)

Let \(A_0,\ldots,A_{\ell-1}\) be a nontrivial contiguous interval of
distinct rank-nine owners in a Johnson chronology.  If

\[
                         |\bigcup_i A_i|=10,          \tag{3.3}
\]

then every adjacent pair in the interval has rank-ten union equal to the
whole interval union.

#### Proof

Adjacent rank-nine Johnson vertices intersect in rank eight, so their union
has rank ten.  This union is contained in the rank-ten set in (3.3), hence is
equal to it.  The same argument applies to each adjacent pair.  \(\square\)

Singleton intervals have rank nine and cannot witness a rank-ten target.
Thus absence from the adjacent-pair provider union is absence from every
literal owner interval, including cyclic wrap.

### Theorem 3.2 (fixed-skeleton upper-`q1` no-go)

For the authenticated OPTIMAL28 macro/packet skeleton, the provider union of
the fixed internal pairs and all cases in Section 3 contains `19230` of the
`19448` rank-ten targets and omits exactly `218`.

Therefore no residual `U` pairing on this fixed skeleton is upper-`q1`
complete, even before degree, connectivity, residence, deeper-shadow, or
common-cap constraints are imposed.

#### Proof

The exact enumeration gives

```text
fixed distinct upper colours       14729
targets needing a variable provider 4719
all possible distinct colours      19230
unsupported colours                  218.
```

The unsupported set splits as `116` `x`-only targets and `102` `y`-only
targets; there are no untagged or `xy` targets in it.  Its canonical sorted
list has SHA-256

```text
cda1d49d62b377782acbc82764bfd19fb0aee65121bbe91189d3833d7d6a29de
```

The provider classification is exhaustive for adjacent pairs, and Lemma 3.1
is exhaustive for all literal rank-ten intervals.  \(\square\)

## 4. Exact canonical width-three lower classification

Every three-owner window is centred in exactly one of three object types.

### 4.1 Macro centre or macro endpoint

Windows wholly internal to a macro are fixed.  At its left endpoint let the
first two macro owners be `A_0,A_1`, let `B` be any legal external neighbour,
and let the exposed port be

\[
                          T=A_0\cap B.                \tag{4.1}
\]

Then

\[
                    B\cap A_0\cap A_1=T\cap A_1.     \tag{4.2}
\]

Thus the endpoint-centred lower colour is fixed by the macro and its exposed
port; it does not depend on which residual owner supplies `B`.  The right
endpoint is identical after reversal.  This verifies the endpoint-centred
formula that is easiest to omit from a pair-column model.

### 4.2 Singleton centre

Let a singleton owner `U` use ports `S,T`, and let its neighbouring owners be
`L,R`.  Legality says

\[
                         L\cap U=S,\qquad U\cap R=T.  \tag{4.3}
\]

Consequently

\[
                         L\cap U\cap R=S\cap T.       \tag{4.4}
\]

For one of the `133` packet singletons this colour is fixed.  For a residual
singleton it depends only on the owner-pair column (2.4), not on the selected
neighbour identities.  Equations (4.2) and (4.4), together with internal
macro triples, exhaust all width-three windows.

The exact census is

```text
fixed distinct width-three lower colours       15551
targets needing a variable z provider           3897
all possible distinct width-three colours       19283
unsupported width-three colours                   165.
```

### Proposition 4.1 (scope of the lower count)

The `165` unsupported rows are impossible as intersections of three
consecutive owners in any residual completion of the fixed skeleton.  No
claim is made for intersections of four or more consecutive owners.

#### Proof

The first sentence follows from the exhaustive centre classification above.
The second is a model-scope statement: the enumerated provider catalogue has
no variables for longer compiler intervals, and this audit proves no
lower-witness compression theorem analogous to Lemma 3.1.  Therefore its
enumeration cannot certify absence of those unmodelled witnesses.
\(\square\)

## 5. Independent audit

Two independently structured scripts reproduce the decisive census.

1. `scratch/audit_ad_k17_opt28_static_shadow_provider_master_20260731.py`
   enumerates the fixed support and the relaxed `z/y` columns directly over
   all rank-ten and rank-seven targets.
2. `scratch/audit_ad_k17_opt28_depth2_local_provider_state_20260731.py`
   starts from the literal connected owner cycle, reconstructs every fixed
   object, and independently enumerates port turns, macro-boundary windows,
   and singleton-centred turns.  It serializes all `218` upper zero rows and
   all `165` canonical lower zero rows.  It additionally checks that every
   current upper-`q2` hole has at least one enumerated local turn provider;
   that is only a local-support statement.

The second audit has fail-closed assertions for all frozen dimensions.  Its
larger enumeration contains `2,738,470` residual singleton turn templates,
so agreement is not a consequence of merely copying the compact formulas.

Authenticated inputs are

```text
six-swap macro forest       4e3129d2604d3e41c226efa3bea71a203180538710dd97272cc734e23412441b
packet catalogue            b803899bbf07b3cbc82e995c9fd1f6231e6eba679d6a60e4a447cb36c08e71f2
OPTIMAL28 marked path        b60341b5cee0de1884d3af6561d8247722bad879d7b5322ca21d94f60472e351
connected residual b-flow   b3cbb0663409463cb24a2ed78db154cc88a042b633e979cba3506ba74e610ef6
literal connected cycle     5a1dbc412daec65babbcc17c8fe30ad62c13fcf8d4606d2c22bfa839b6654c24
```

The independently frozen local-provider audit is

```text
script SHA-256   b6a5e4091ac661e577586ca49df289279e17cf9700981ed933c06ce086111e9a
JSON SHA-256     bcaa076f8844787093b4b5aad98db0186289f5cea66ebc83e45ce20f2eadbbc0
payload SHA-256  fe9bcb8ae361e02be1782d37ff89244bea3779f60b8ee055b568233684229418
lower-zero list  5fbdc42b715f7367bd6b739efa513ca196c7f0acda0c681863324f09264da3f5
```

All histogram/profile keys in this independent JSON are serialized as
strings before hashing, and the emitter checks the payload again after a JSON
round trip.  This avoids the integer-key/string-key ambiguity present in
intermediate concurrent snapshots of the compact master audit.

## 6. Exact remaining boundary

The fixed-skeleton residual-pairing lane is closed already by the `218`
upper colours.  The result does **not** rule out:

* changing the occurrence transversal or any macro/packet interior;
* replacing one or more fixed packet objects;
* a nonflat literal compiler that changes the exported owner chronology;
* a broader construction in which the present rank-nine owner blocks are not
  kept as the same fixed objects.

The `165` lower rows should be used as a canonical-width-three diagnostic,
not as an additional global impossibility theorem.  The actionable next gate
is therefore a skeleton-changing upper-service rethread that is coupled to
residence and to the complementary common-cap interface.
