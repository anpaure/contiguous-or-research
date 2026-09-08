# Hall 19 neutral compression: root 9104, the split 8216 forest, and literal readiness

Date: 2026-07-28

Status: exact neutral-beam census, two priority-state theorems, complete
one-braid negative scans from both priority states, and exact common-`Q`
readiness audits.  The negative physical theorem is scoped to deletion-only
one-occurrence rebases of native children; it is not an obstruction to an
arbitrary later segment braid.

## 1. Frozen Hall-19 base and neutral census

The base is the certified Hall-19 carrier

```text
scratch/k15_h20_h19_root8216_chain/final/candidate_0000.json
SHA-256 86dcb9f16739b0a75eca8cde6bc9c824876453ab3b8fc70f01144da517dd4c0b
```

Its direct three-cut scan contains no Hall-18 state among move descriptions
with lower-q1 holes at most four; descriptions outside that cap were not
Hall-evaluated.  Emitting the Hall-19/zero-six stratum and quotienting equal
middle paths gives exactly 689
nonidentity neutral states.  Every materialized state is Hall 19 with zero
count six.  The exact raw DM census reports

```text
states                                      689
states changing a fixed component profile  188
states saturating a fixed component          24
states with root-changing migration           2
states with a root-changing diamond            2
```

Its output and compact-ranking SHA-256 digests are

```text
3c9571a60228793bc41702386be3916aa36a45410851ff991e1beab634d987ad
  h19_raw_dm_component_census.jsonl
74549c7030407d5e08b250dedd8ab108ac2283714f5c4a3baa19da9f9f5655a1
  h19_raw_dm_component_ranking.json
```

The independently richer complete-profile census gives the DM-left
histogram

\[
\begin{array}{c|rrrrrrrr}
|L|&380&484&485&514&515&516&517&524\\ \hline
\#&1&1&1&3&9&635&37&2.
\end{array}                                                     \tag{1.1}
\]

Thus the unique strongest raw compression is not a Hall gain; it is a
neutral migration to a much smaller critical component.

## 2. Priority router c0440

Define

\[
 X_{19}\xrightarrow{\operatorname{FR}(3814,4556,5539)}X_{0440}. \tag{2.1}
\]

The frozen state is

```text
scratch/k15_h19_neutral_c0440_fr3814_4556_5539.json
SHA-256 a51f8631a9b2394405b8304c949bf9606d3b43f897f51ad9474de725df34584a
middle_path SHA-256 014c9f5a870f819c0b22045e9e98ddbdfc6adb839f2354d387528e7cdbb6dd38
```

Here and below the path digest is the SHA-256 of the comma-separated decimal
mask sequence without a terminal newline.

### Theorem 2.1 (exact neutral root compression)

`X_0440` is a permutation of all 6435 rank-eight masks, is a Johnson path,
is depth-three resident, and is complete in every upper layer `q=1,...,7`.
Its lower-hole vector is

\[
                         (4,18,13,1,0,0,0).                   \tag{2.2}
\]

It has Hall deficiency 19, matching rank 16364, zero count six, and positive
DM shore `380/361`.

The move replaces the old component

\[
                         C_{960}:161/160
\]

by

\[
                         C_{9104}:25/24.                      \tag{2.3}
\]

The two target sets meet only in `13264`; hence 160 old targets leave, 24 new
targets enter, and the exact compression is 136.  The root-8216 `321/319`
component is unchanged.

On the *fixed old* root-960 target shore, however, the new physical bank has
161 neighbours and matching rank 161.  Complete-profile cancellation shows
an added copy of the star profile

\[
                              \{960,9152\},                   \tag{2.4}
\]

whose two depth-zero physical occurrences are cells `4800` and `6053`.

#### Proof

Literal materialization of `FR(3814,4556,5539)` agrees with the stored path.
Direct deck, Johnson, residence, and layer enumeration gives (2.2) and the
upper assertion.  Exact matching and DM decomposition gives `380/361` and
(2.3).  Canonical component comparison gives the unique bridge target
`13264`.  Finally, restricting every occurrence profile to the old 161-set
gives rank and neighbourhood size 161, with (2.4) as the only added copy of
an already present native profile.  All comparisons retain physical
multiplicity.  \(\square\)

### Theorem 2.2 (q1-cap-four direct-neighbourhood no-go)

The full one-braid description scan from `X_0440` has no Hall-18 state among
the Hall-evaluated descriptions with lower-q1 holes at most four.  It counted
549329 Johnson, 12021 resident, and 9202 upper-safe descriptions; 7301 passed
the q1 cap and were Hall-evaluated.  Its score distribution begins with 7124
Hall-19/zero-six and one Hall-19/zero-seven description; the best evaluated
deficiency is 19.  The frozen hashes are

```text
4ed7e47eedb13cd56c1e1f562df7bc0808f89d7e79685bbaf5d38b24dfd09f0d
  scan.out
b24f60b64fe9963aac60edf10830f53ab5304764de52b42d1913131f084b17dd
  scan.err
6e3a2ee0a1b807730cbb9c8cef0d17d922623b8aa3f07b341b0a9d6d7e86dace
  result.json
```

This closes every single three-cut splitter after the c0440 router only within
the required lower-q1-hole cap four.  It does not close a further neutral
router followed by a third braid or descriptions outside that cap.

## 3. Literal common-`Q` result on the former shore

The incidence saturation in (2.4) is literal, not merely a matching fact.
The maximal controller has value `9152` at both cells `4800` and `6053`.
At either cell one may make the single deletion

\[
                         9152\longmapsto960,                  \tag{3.1}
\]

whose deleted mask is `8192`.  The other cell retains the native `9152`
pin.  Direct interval verification shows that (3.1) preserves all 6435
central windows and one reserved native pin for each of the 497 formerly
natively covered targets.  Adding the exceptional root pin therefore gives

\[
                            497+1=498                         \tag{3.2}
\]

simultaneous pins on the former 516-target Hall-19 shore, leaving precisely
the other 18 exposed targets.

The two common-word digests and companion cells are

```text
split cell 4800, companion 6053:
  d4a366e3037bb702f02b369af41acf3da160935a9a9421c1fa94722b0780855c
split cell 6053, companion 4800:
  746bf0bd9048dac284793196585e734e55b90f8e1354c630402a4547b919d590
```

The permanent verifier is

```text
scratch/audit_k15_h19_c0440_root960_common_q.py
SHA-256 29ef829f1615c6be26acb4329e7a64437d6e079f185e364453454247bb4308f6
```

and its frozen certificate has SHA-256

```text
a7a5ca6fac7fd2056604ea22f6489baccfb729587a636045c07842f02af482c6
  scratch/k15_h19_c0440_root960_common_q_certificate.json
```

The scope of (3.2) is exactly the former 516-target shore.  It is not a
16364-pin global common-word compiler.  It also explains why saturating the
old root does not lower Hall deficiency: the unit defect has migrated to the
new root-9104 component.

A second audit reserves the child state's entire 361-pin final DM basis and
the 160 nonroot pins of the old root-960 component simultaneously.  These
banks share the pin `(cell,target)=(13326,13264)`.  After identifying that
copy and adding root `960`, either word realizes

\[
                         361+160-1+1=521                      \tag{3.3}
\]

distinct target/cell pins.  Thus the same shrink is compatible with both the
old focal component and the complete new critical reserve; its exact scope
is this 521-pin union, still not the full compiler.

## 4. Physical-readiness theorem and the c0440 obstruction

For a positive DM component `C=(L,R)`, let the native trace of a physical cell
be the union of its maximal-controller letters.  Call `C` a native basis when
these traces are distinct members of `L` and their complement

\[
                              E(C)=L\setminus n(R)             \tag{4.1}
\]

has size `|L|-|R|`.  The members of `E(C)` are its exposed roots.  This
definition permits the `321/319` component: its intersection is `8216`, not
a target, while

\[
                              E(C)=\{8217,8218\}.              \tag{4.2}
\]

A one-occurrence deletion rebase to \(e\in E(C)\) must use an extra physical
occurrence of some native child \(t\) with \(e\subseteq t\).  On the chosen cell
interval `I`, every new controller letter must lie in `e`; hence the
coordinatewise largest possible deletion word is forced:

\[
 Q'_j=Q_j\cap e\quad(j\in I),\qquad Q'_j=Q_j\quad(j\notin I). \tag{4.3}
\]

If (4.3) fails a central window, a reserved native pin, nonemptiness, or the
new root interval, every smaller deletion word also fails.  Thus direct
testing of (4.3) is complete for a fixed child occurrence.  For a gap-two
component the pair test enumerates two distinct cells and verifies the
combined maximal word, distinguishing partial gap-two-to-gap-one discharge
from full discharge.

### Theorem 4.1

All 18 final c0440 DM components are native bases in the sense above.
Seventeen have one exposed root; the root-8216 component has the two roots in
(4.2).  Across the complete physical bank there is no extra native-child
occurrence for any of these components.  Consequently there is no
one-occurrence deletion rebase at all.  In particular, the root-8216
component admits neither partial nor full discharge by this mechanism.

The exact scorer and c0440 outputs are

```text
4148fb930860e3ff0385d7caab3b6f2ea085e310546c51c676bf70b7f2911835
  index_k15_h19_physical_readiness_beam.py
e95c252f672d62be8d9fa652a2666bcbbf04ab8ed7100e569de3421b15e58db0
  c0440.physical.jsonl
b64c42b07cb0c40f420637ff1c657187e132035619cdffc6fda313245bd5a53f
  c0440.physical.ranking.json
```

The independent state-specific audit package is

```text
2a8e7dfd7cbe0d29232e2c9d1559284ca3e1874d53168e22de2f72b5fa77451a
  THREAD_K_K15_H19_C0440_ROOT9104_EXACT_AUDIT_20260728.md
3d34423a5a6f12e41c91e82d24d14bd8f510d19f4db0c827738ab3031b12f4bb
  scratch/audit_k15_h19_c0440_root9104.py
fd1ee165a73299d161a3ac82c10e1f6b7d783662be7227102ebce92b8fbea74e
  scratch/k15_h19_profile_20260728/audit_k15_h19_c0440_root9104.json
```

This is a statewise obstruction to the duplicate-native shrink primitive,
not to nonnative profile refinements, square splits, or another neutral braid.

The obstruction is specifically child-pin conservation, not chronology.
For root `9104`, 12 raw sockets are central-window-safe if their unique child
pin is released; seven delete one of coordinates `1,2,3,6,12,13,15`.  For
the root-8216 component there are 74 sockets for each exposed root.  After
releasing the occupied children, 147 of the 148 single sockets work and 5355
two-root cell pairs preserve all central windows and all other native pins.
With every child pin reserved, however, both the partial and full counts are
zero because no child has a companion occurrence.

### Theorem 4.2 (beam-wide deletion-readiness obstruction)

The conclusion is not peculiar to c0440.  In all 689 Hall-19/zero-six
neutral states, every final positive-DM component is an exposed-target native
basis.  Across the entire occurrence bank of every state there are

\[
 \boxed{\text{zero extra occurrences of every final-component native child}.}
                                                                    \tag{4.4}
\]

Consequently all 689 states have zero one-root deletion rebases, zero
unit-component full discharges, and zero gap-two partial or full discharges.
The exact root-8216 `321/319` component occurs in 661 states; none admits even
one of its two exposed roots by this mechanism.

The all-component census and compact ranking have SHA-256 digests

```text
3c663d3fbf8005c2c4622f4b2a43609d8b68a20abb7241f1f7db466603cb3058
  h19_physical_readiness_census.jsonl
0a747f03dd4583f72131ae0dc72bef2312364c238781e65e6cf01a62f05fff47
  h19_physical_readiness_ranking.json
```

A separate anchored-root audit, which permits a prospective root split to
consume one native child and measures the resulting loss, gives minimum
defect exactly one in all 689 states and no ready state.  Its output digest is

```text
24fbceea139c8e1d8325878f77b0f823e9dc80bcbe8f9bfd2597b74b5731861d
```

Thus the missing datum is literal: many ports are exactly one duplicate
native occurrence away from readiness, but the entire neutral beam contains
no such duplicate on a final component.

## 5. Secondary router c0520

The second structurally distinct state is

\[
 X_{19}\xrightarrow{\operatorname{RF}(688,2636,2650)}X_{0520}. \tag{5.1}
\]

Its frozen SHA-256 and ordered path digest are

```text
897ab99092552874c0b66203bc4bbe1a4e4b68e349d58521b53ebf21dd126c39
42b69885e5bb2de8ff81bfc6904209cd4a814eaf298b13c66ded0dd963878efd
```

It is deck-exact, Johnson, resident, upper-complete, Hall 19/zero six, and
has lower-hole vector

\[
                         (4,18,11,1,0,0,0).                   \tag{5.2}
\]

Its DM shore is `485/466`.  It replaces the root-8216 `321/319` component by

\[
               C_{8217}:129/128,
               \qquad C_{8218}:161/160.                      \tag{5.3}
\]

The exact migration removes 36 old targets, adds five, and therefore
compresses total left mass by 31.  All 19 final components have unit defect
and are native bases.  None has an extra native-child occurrence, so no
one-occurrence deletion rebase is available.

The direct scan from `X_0520` also contains no Hall-18 state among descriptions
with lower-q1 holes at most four; upper-safe descriptions outside that cap
were not Hall-evaluated.  It counted 548467 Johnson, 11956 resident, and 9165
upper-safe descriptions.  Its frozen output hashes are

```text
4a2fb01cef8d8263589721e5581c9f1ebd8e18d8f9002a18a70d72a7ff8208cf
  scan.out
e892cae65f330948997532e8a89f35d41c63aa010a7e73b33ecc8102ba2bf5b4
  scan.err
0444b44c55e37ce05db896a76fb5faa3b844ba18e00a2bb9fd784a2154f7cdd5
  result.json
```

The c0520 physical outputs are

```text
831a72923bf41e8c56f97e826c097c1dceb8bd99a063df6ad17142c7bf8db88f
  c0520.physical.jsonl
1e6d7176660e33a2f4f4941a459c7cc6b7f0a677e2a9f04a5406320406dbe281
  c0520.physical.ranking.json
```

Thus component splitting and literal duplicate readiness are independent:
c0520 removes the gap-two component abstractly but creates no shrink port.

## 6. Selected second-neighbourhood exhaustion and scope

The union of the first 16 states selected by fixed-rank, forest,
profile-router, migration, and compression rankings has been scanned across
all one-braid descriptions.  None has a Hall-18 neighbour within the enforced
lower-q1-hole cap four; descriptions outside that cap were not Hall-evaluated.
The aggregate runner hashes are

```text
19ac5f039806f639e463de0bfed7542a3f03a9783f4ba5b7e218a71aad264a76
  h18_first16.out
6162e409863cd1eea23895c3b8493b3bab33615c24221e846059bdde4bc77d41
  h18_first16.err
```

This proves an exact scoped absence theorem for those 16 full one-braid
neighbourhoods.  It does not cover all 689 neutral parents.

The formerly proposed packet-15 double-compression branch is independently
closed: the only noninverse second packet moves preserve the focal `129/128`
component exactly, while the inverse moves restore `161/160`.  See
`THREAD_K_K15_H20_PACKET15_DOUBLE_COMPRESSION_AUDIT_20260728.md`, SHA-256
`e6057260ccf13819add5d169b260d846e3ba1f0cb5e83e6be460ef36b95670a4`.

The remaining branch is genuinely third-order.  The neutral neighbourhood of
c0440 was emitted and again deduplicated to 689 states.  Its complete-profile
and all-component physical censuses both pass; every state is Hall 19/zero
six, every final component is a native basis, and none has a duplicate native
child.  The leading forest/compression state is the commuting square in the
next section.  Neither raw component size nor fixed-shore saturation is by
itself a literal readiness certificate; the all-component physical score must
precede those abstract rankings.

## 7. Exact commuting double compression

Let

\[
 A=\operatorname{FR}(3814,4556,5539),\qquad
 B=\operatorname{RF}(688,2636,2650).
\]

Their inclusive physical supports are disjoint, with 1163 untouched
positions between them.  Therefore they commute as literal block maps, and
direct materialization verifies

\[
                         B(A(X))=A(B(X))                      \tag{7.1}
\]

entry for entry.  The four path digests are

```text
X       97429bb3f25ccf921e794c1d20ed361684116823d0a14787634dc22af820e441
A(X)    014c9f5a870f819c0b22045e9e98ddbdfc6adb839f2354d387528e7cdbb6dd38
B(X)    42b69885e5bb2de8ff81bfc6904209cd4a814eaf298b13c66ded0dd963878efd
AB(X)   43c8029e981235210896a47b3d8161b3e96112fcd68912eed645b8753ab01742
```

The composite carrier file has SHA-256

```text
79a4d1dbf5b8c40fea6086d1cd7820f74ccd058518b53f35a2e6d830fa163451
```

All four corners are exact decks, Johnson paths, resident, upper-complete,
Hall 19/zero six.  Their DM shores are

\[
       516/497,\qquad380/361,\qquad485/466,\qquad349/330.      \tag{7.2}
\]

Move `A` replaces root `960` type `161/160` by root `9104` type
`25/24`; move `B` replaces root `8216` type `321/319` by roots `8217`
and `8218` of types `129/128` and `161/160`.  Every shared component and
every full restricted-profile Counter is unchanged on the opposite edge.
Thus the two compressions are componentwise additive, not merely equal in
their scalar shore sizes.  Their signed shadow currents are likewise
order-independent at every depth.  The final lower-hole vector is
`(4,18,13,1,0,0,0)` and all upper supports remain complete.

The 19 final components give a 330-pin native basis, but no selected child
has a second occurrence.  The root-960 star shrink survives and gives two
490-pin common-`Q` words; every final-component rebase remains blocked by its
unique child pin.

The direct scan from `AB(X)` again has no Hall-18 state among descriptions with
lower-q1 holes at most four; descriptions outside that cap were not
Hall-evaluated.  It counted 549476 Johnson, 12021 resident, and 9203 upper-safe
descriptions.  Its hashes are

```text
25f795d3fcc2e8f6f27620715c094f2dd1870d986b467de906a76d0506d672b2
  scan.out
2e05802f5c6a030b4fdbf839e5cd8c71012ac6b81ad6f370b89bb6089b6b9bc1
  scan.err
```

The independent square audit package is

```text
5120d4771a750bcf58204c0d81804ef24f865ae1f2e21231542c0d2a8c577439
  THREAD_K_K15_H19_C0530_COMMUTING_DM_COMPRESSION_SQUARE_AUDIT_20260729.md
49686d28b64b9f86822643902ba568def51f3a701cfacd176d1ca2477c951daf
  scratch/audit_k15_h19_commuting_square_c0530.py
9024d8c61b8ffc6d3b7c50d439cdb3709ce278606a0183b58c04ad09fdc4e27e
  scratch/k15_h19_commuting_square_20260729/audit_k15_h19_commuting_square_c0530.json
```

## 8. Root-defect relay has a certified inverse and unique c0668 closure

The next profile-ranked braid is

\[
 c0440\xrightarrow{\operatorname{RF}(3176,4522,5948)}c0668.
\]

It replaces the root-9104 target component `25/24` by the disjoint root-952
target component `6/5`, changing the total DM shore from `380/361` to
`361/342` without changing deficiency 19.  All shared target shores, types,
and native-trace multisets persist, but several physical right-cell sets are
re-addressed.  The fixed old shore is saturated and the fixed new shore loses
one unit of rank, so this is an exact defect relocation, not a Hall
improvement.

The complete c0668 neutral census starts from 7130 emitted Hall-19/zero-six,
lower-q1-hole-four move descriptions and has 695 deduplicated passing states.
Exactly one saturates the fixed root-952 shore or canonically migrates its
target component, including same-root target-shore migrations:

```text
candidate_0450  FR(3176,4603,5948)
648ad9d3112908dbfff22ba9a95c81b7db3591154bc9594a09874a4e0030f608
```

Its middle path is entrywise equal to c0440.  Thus the relay has the certified
inverse cycle

\[
  9104:25/24\ \rightleftarrows\ 952:6/5.
\]

Every one of the 695 states remains Hall 19/zero six; every final component
has a native basis, but there are no surplus native child occurrences and no
exact reserve-preserving single or within-component full rebases under the
canonical native reserve.  This does not cover nonnative pins or simultaneous
ears across components.  The physical census is

```text
bee279b28f3aa7ca88758025ce2998f59c781e2cad6f7bcdd91b6cabf325794c
```

The independent root-8216 compression-plus-split commutes literally with this
relay.  It gives `c0526`, DM `330/311`, with target-component types `952:6/5`,
`8217:129/128`, and `8218:161/160`, but re-addresses the root-952 physical
cells and again yields no native duplicate readiness.  Direct scans from
c0668 and c0526 find no Hall 18 among descriptions satisfying the enforced
lower-q1 hole cap four; upper-safe descriptions outside that cap were not
Hall-evaluated.

The exact theorem, audit, artifacts, and scope caveat are in
`THREAD_K_K15_H19_ROOT_DEFECT_RELAY_CYCLE_20260729.md`.  What is closed is the
one-step canonical target-shore closure from c0668, not outgoing relays from
c0440, pure physical readdressings, or higher-order braids.  A successful
continuation must create a surplus native occurrence, certify a nonnative
common-`Q` assignment, coordinate components, or first alter the occurrence
geometry by a longer coupled route.
