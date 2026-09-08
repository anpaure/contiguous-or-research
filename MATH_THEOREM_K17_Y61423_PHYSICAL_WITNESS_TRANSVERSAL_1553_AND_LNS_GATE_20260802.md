# K17 Y=61423 physical witness transversal 1553 and guided-LNS gate

Date: 2026-08-02  
Status: exact solver-free theorem on one authenticated physical incumbent and
its literal witness supports; independently certificate-checked.  The
all-support radius-zero face and the canonical-transversal radii zero, one,
and two are additionally DRAT-verified UNSAT.  An exact non-radius packing-
excess model further proves a resource-strengthened global distance of at
least 1,561 facets.  No unrestricted
protected-completion, resident K17 carrier, or word is claimed.

## 0. Result

Let `F0` be the authenticated clean1666 physical factor and let `Y=61423`.
It is one owner-once exact-facet Hamilton cycle, covers every rank-ten cap,
contains the 90-edge singleton-hole bank, and has

```text
833 positive runs of length 2
833 positive runs of length 3
 12 maximal Y-clean blocks with union Y.
```

For each of these 1,678 forbidden witnesses, take its complete physical edge
support: the entering edge, all internal edges, and the leaving edge.  Project
the support to its rank-eight facet colours.  The resulting 1,678-edge
hypergraph on 5,724 facet vertices has

\[
                         \boxed{\tau=1553}.              \tag{0.1}
\]

The equality is literal, not an LP estimate.  A frozen certificate contains

* 1,553 pairwise facet-disjoint witness supports, proving `tau>=1553`; and
* 1,553 named facets meeting every witness support, proving `tau<=1553`.

Separately,

```text
residence witnesses: 1666 cuts / 5627 facets / tau=1547
full-Y witnesses:       12 cuts /  114 facets / tau=12
combined:             1678 cuts / 5724 facets / tau=1553.
```

The maximum number of combined incumbent witnesses containing one facet is
three; on the residence-only subfamily it is two.  The 1,553 packed supports
contain 5,444 distinct facets.

Consequently, every physical factor which avoids all of these authenticated
incumbent witnesses differs from `F0` at at least 1,553 facet choices.  In
particular, every depth-three-resident factor containing the bank and making
`Y` missing must differ from `F0` on at least 1,553 facets.

After imposing the exact facet, owner, rank-ten-cap, and protected-bank rows,
the lower bound strengthens to

\[
                    \boxed{\operatorname{dist}(F,F_0)\ge1561}. \tag{0.2}
\]

This second statement is DRAT-certified rather than solver-free; its exact
non-radius encoding is given in Section 3.3.

This is a distance from the named incumbent `F0`, not a lower bound on the
distance between arbitrary carriers and not a global K17 impossibility
theorem.

## 1. Why facet hitting is necessary

Every physical edge in an exact lower-rainbow factor owns its intersection
facet.  Because each rank-eight facet is used exactly once, changing the
selected edge on a witness support is equivalent to changing at least one of
the support's facet choices.

For a positive run of length `l<=3`, its support consists of the entering
edge, its `l-1` internal edges, and the leaving edge.  If all those edges
remain selected, the intermediate positive owners are degree-saturated and
the two boundary owners remain zero in that coordinate, so exactly the same
short run survives.

For a maximal `Y`-clean block, the same argument applies.  Keeping the
entering edge, all internal edges, and the leaving edge degree-saturates the
clean owners and preserves dirty owners at both boundaries.  Its owner union
therefore remains `Y`.

Thus every acceptable completion must hit every recorded support.  If
`H=(V,E)` is the facet-support hypergraph, its changed-facet set is a
transversal of `H`.

## 2. Exact certificate of equality

The deterministic constructor repeatedly chooses a facet meeting the maximum
number of still-live cuts, breaking ties by mask.  It terminates after 1,553
facets and directly verifies that every one of the 1,678 cuts is hit.

Independently, order the cuts by support size and ID and greedily accept a cut
whose facets are disjoint from all previously accepted supports.  This yields
1,553 pairwise disjoint cuts.  Any transversal needs a different facet for
each member of this packing, so it has size at least 1,553.  The two
certificate halves prove (0.1).

The compact certificate is

```text
/home/amodo/or15/work/longrun_k17_y61423_physical_completion_20260802/
  seed1666.hitting.tsv
SHA256 f6cf27afac6748ebd276686e4b99d24937ea2bfde30d48113f86b634efabf10a
```

An independent verifier reparses all physical edges, recomputes their
intersection facets, checks every hit, and checks pairwise disjointness of
the packed supports.  Its output is

```text
PASS_K17_Y61423_PHYSICAL_WITNESS_TRANSVERSAL_CERTIFICATE
cuts=1678 hitting=1553 packing=1553 packed_facets=5444
```

## 3. Consequence for local search

This exact metric explains why small edit or annealing neighbourhoods around
`F0` cannot solve the protected-completion problem.  Before satisfying owner
degree, cap, topology, or any newly created witness, a candidate must already
change at least 6.39 percent of all 24,310 facet choices.

Two exact radius-zero calibrations were materialized on the bank-only physical
resource master.

### 3.1 All-witness support shell

Keep all 5,724 facets occurring in some incumbent witness mutable and freeze
the other 18,586 facets to `F0`.  The resulting

```text
5,178,030 variables / 11,149,472 clauses
```

formula is UNSAT by input unit propagation.  `drat-trim` verifies a
556-input-clause core and 556 resolution steps.  This says that repairing the
witnesses requires resource propagation beyond their literal supports.

### 3.2 Canonical transversal shell

Keep only the 1,553 certificate facets mutable and freeze the other 22,757.
This stronger scoped face is also UNSAT by input propagation.  Its trimmed
core has only four input clauses and four resolution steps.  Therefore the
particular canonical minimum transversal does not extend while every other
facet is frozen.

Neither radius-zero result proves that every size-1,553 transversal fails,
nor that a valid completion needs more than 1,553 changes.  The exact guided
shell calculation has now also released the canonical transversal's first
and second factor-line-graph neighbourhoods.  Both are UNSAT with retained
proofs: radius one trims to a four-input-clause unit core, while radius two
trims to a 1,441-input-clause core.  Thus every completion in this particular
guided ball must leave the radius-two shell.  This remains a statement about
one canonical transversal and one incumbent-derived shell, not all hitting
sets of the same size.

The active guided shell sizes are

```text
radius 0:  1553 mutable / 22757 frozen  (VERIFIED UNSAT)
radius 1:  4630 mutable / 19680 frozen  (VERIFIED UNSAT)
radius 2:  7456 mutable / 16854 frozen  (VERIFIED UNSAT)
radius 3:  9892 mutable / 14418 frozen  (TIMEOUT UNKNOWN)
radius 4: 11951 mutable / 12359 frozen  (TIMEOUT UNKNOWN).
```

Radii three and four each reached the 900-second cap with exit 124.  They are
exactly `UNKNOWN`, not negative evidence promoted to UNSAT.

### 3.3 Exact non-radius packing-excess balls

The disjoint packing permits a global Hamming test which neither fixes the
greedy transversal nor privileges a cyclic neighbourhood.  For a packed
support `S`, let `c(S)` be the number of its facets changed from `F0`.  Every
recorded packed support is itself a witness no-good, so `c(S)>=1`.  Since the
1,553 supports are facet-disjoint, define

\[
 E=\sum_S(c(S)-1)+\#\{\hbox{changed facets outside the packing}\}. \tag{3.1}
\]

Every changed facet lies either in exactly one packed support or outside all
of them.  Hence, identically,

\[
                   \#\mathrm{changed}=1553+E.             \tag{3.2}
\]

The overlay introduces a threshold literal for each event `c(S)>=t`,
`2<=t<=|S|`, and charges every outside baseline-primary directly.  Exhaustive
subset implications make the threshold charges exact for an upper bound; a
Sinz counter imposes `E<=b`.  Thus its SAT models are exactly the accumulated
physical master inside global facet distance `1553+b`.

The first eight budgets `b=0,1,2,3,4,5,6,7` are UNSAT:

```text
b=0: distance <=1553, 5,181,921 vars / 11,171,918 clauses,
     UNSAT in 1.87 s; 858-clause trimmed core; VERIFIED.
b=1: distance <=1554, 5,204,677 vars / 11,217,428 clauses,
     UNSAT in 4.14 s; 7,378-clause trimmed core; VERIFIED.
b=2: distance <=1555, 5,227,433 vars / 11,262,938 clauses,
     UNSAT in 6m42s; 40,277-clause trimmed core; VERIFIED.
b=3: distance <=1556, 5,250,189 vars / 11,308,448 clauses,
     UNSAT in 6m38s; 60,700-clause trimmed core; VERIFIED.
b=4: distance <=1557, 5,272,945 vars / 11,353,958 clauses,
     UNSAT in 6m53s; 157,424-clause trimmed core; VERIFIED.
b=5: distance <=1558, 5,295,701 vars / 11,399,468 clauses,
     UNSAT in 7m29s; 207,705-clause trimmed core; VERIFIED.
b=6: distance <=1559, 5,318,457 vars / 11,444,978 clauses,
     UNSAT in 9m54s; 268,967-clause trimmed core; VERIFIED.
b=7: distance <=1560, 5,341,213 vars / 11,490,488 clauses,
     UNSAT in 10m33s; direct backward DRAT replay; VERIFIED.
```

Therefore every exact physical resource factor containing the 90-edge bank
and destroying all 1,678 named witnesses has distance at least 1,561.  This
quantifies recourse over *all* hitting patterns.  It still does not say that a
factor at distance 1,561 exists, nor that the unrestricted bank is
incompletable.

### 3.4 Exterior-donor separator

The proof cores for `b=0,1,2` contain no packed-support threshold variable.
This suggested, and a separate exact model confirms, a stronger physical
statement.  Leave all 5,444 facets in the disjoint packed supports completely
unrestricted and bound only changes among the other 18,866 facets.  Exterior
budgets zero, one and two are all DRAT-verified UNSAT.  Therefore

\[
 \boxed{\text{every accepted resource factor changes at least three facets
 outside the packed witness supports}.}                       \tag{3.3}
\]

This is the first recurring separator extracted from the distance ladder:
arbitrary extra rethreading inside the named witness supports cannot replace
three exterior donor facets.

The trimmed physical cores are not one fixed mask shore.  For packing-excess
budgets zero through four, an independent option replay gives

```text
budget                   0      1      2      3       4       5
primary facets          59     36    365    900    4399    5351
exact-one facet rows     1      2      3      4      21      27
rank-ten cap rows        1      0      8     11     110     129
```

The tempting `b+1` facet-row pattern holds only through budget three.  At
budget four the core closes over thousands of physical facets and more than
one hundred cap rows.  Several earlier masks recur, but there is no fixed
mask-level shore.  The stable proof-safe object is an augmenting exterior-
donor hierarchy; a uniform symbolic description of its expanding closure
remains open.

## 4. Artifact ledger

Authenticated inputs:

```text
ff75194a4c071eb1d3c82269e482a9d0175e0356b0f6ad177daa9d7a9b5f8009  clean1666 factor.tsv
89a9121c97e4258ce947d39ef2554bd342d4f9c2dcdaead7738949aed9572350  bank.tsv
cdcef370d03478d1739a84280848df5e68035362531bd70ba6f182a8136f7e4a  seed1666.cuts.tsv
```

Sources and outputs:

```text
2d21ea50fb24c90754d7fccb1e12ed06a54982f25969e186d4d932e9f76b2131  physical witness separator source
e70f774704db804ff7948bb886a6fe21222d5fc8b91c459c05d217aa9c0671ab  transversal constructor/audit source
2a8e99d30b20337f8e26d8da18f689dcd0a95e0db830bf6884a10b23974f3a10  transversal audit binary
e6efb1b71fe6e9e5f223611bcff43e2e9a18035037c145dd9ce2a4b4c1f90d47  transversal audit output
426718de1faf2e54ac90d7e35b3a30dfd634e0a50fc6159c271abc861613edc3  independent verifier source
78935cfd46bfae2212dbc8423d0dd962ef7f68e874132f3f0557aefb1c740cf8  independent verifier binary
47214b6f99f6577dcdbed7e53e40328f9e8593fa5c1f0770b8eb62cd5cd195be  independent verifier output
7e327346f3b33368c2f0885369387b62deaaead09dbfeeb8ce7c459909d36e6f  shell-builder source
914e504adf3d15a5f7bb21c33daec71c0b23af0aaacbbdb8b6c2a25e48750711  shell-builder binary
```

DRAT calibrations:

```text
92cd341370a0f656ac82d703b3d064930a6bd307648c91d901c22a085393d5e8  all-support shell0 CNF
b543a867556870a6b62ac52e8d21ea1fc990791bad253086e66739ada978ee3e  all-support shell0 DRAT
bd6cf8704694a4c1d685ffedcc6fd1e1a07a1c58afab9f80961991efdb189938  all-support shell0 core CNF
09a24a48073b8950fb70fa70fb20e6c967f2f0dffea915705f142293ec3a0968  all-support shell0 LRAT
8891869b3e58d239fef4f72abde7b75a3c4aee079707c1243132ada4f674cfe8  all-support shell0 drat-trim output
43cba03182aaadf3d47f6468689e02522f6b693d46c689f8a67c36fe09d2c085  transversal shell0 CNF
cb17eae02ebf911ae1000adbb340d25f54b2da95f27a7b9811417ee2fecdd38a  transversal shell0 DRAT
432384b9d3f273095d30c324ca437e1844bf9fd859546327029ae019f30a3700  transversal shell0 core CNF
23283ec35b99ac5a2e4670790a0473281dca21aaeaca0abdeb75f46f3a30846f  transversal shell0 LRAT
cc8b2eef37be9c7d02536450809a2128f9a420332b2086be171fc148bd284a64  transversal shell0 drat-trim output
da2fa78179c2d866b62b7709d6f6e5a4117c34562d42709015f87cf043c48b3e  transversal shell1 CNF
e4c7ebf89892d986bcdc975e1f30582ea2836780e27231aa5d02f3261f6b2219  transversal shell1 DRAT
1fe09288842dd1cef4974ed6a52c926ddc2116cfe9d80f6e450bec5ebef55db3  transversal shell1 LRAT
7e13d6cefaf7c9c8df4cf1a8ec19a605ab71a2fd932d6754c38b3e583f2072d7  transversal shell1 drat-trim output
9bfececd12632e0cc0a6fb6d9ddf2eb65d9e4e06e5131e8917e5753aebd61255  transversal shell2 CNF
b31ab3b64f8fbb826d422eafd4276ce2ce7264fd1dcafa1f63fddedbcbad427d  transversal shell2 DRAT
e9797cbc52cda3eef12810fea5f78262b36d6145c92a33643f21e015a0aed642  transversal shell2 core CNF
7cc7c7ad6b404f0379f2f057fccbdc8a686f9c197dbf583653d430d622f5b9cd  transversal shell2 LRAT
d0bec3e80eb9a0f8f8a6423332de78867655f88610d5fe0aa1881fde6807a510  transversal shell2 drat-trim output
65037e75b751aca6d47c98219dbaad78f212e097ce34e63316e4dbd8038f0523  packing-excess builder source
29d5ba905921e91978759e467d3c66e0b6531c00d5d2cbe301ddbaa5072ff280  packing-excess b0 CNF
e4fc1a26517b31682fc2160934e5432ae5f0cb3c879b17c965319479ed12c2a5  packing-excess b0 DRAT
e341817bd5a3b9c76a2b1fa4ee7ac25bf826aae40cd6ae448223c2849ba21487  packing-excess b0 core CNF
0b9d11bb50e68cde8eb015bf9302daf4a5d1abfc0673ea6bdc7f3517befa97b9  packing-excess b0 LRAT
5ef70d5e2f35cd943806b4060e0abff98de0cbe51d7c98bfcdf2e585af81b6c8  packing-excess b0 drat-trim output
3f93cafdb78ffa342b6ff0fe376c6bc87ac2f8be56d7d426075b6e938ba9da03  packing-excess b1 CNF
dc7c994d38c42834bd396d1abc1a6d54b1d01f7ed0b2c9765b2757e3769ab697  packing-excess b1 DRAT
27d152e0da4ffe20e08ad57666a284b1ce6d031e46d9701ca6ce121d2f797d9b  packing-excess b1 core CNF
d3ab9a2b4525cf0d14d99c7b25cf5714b86f062a8a925284e74f1979c971994a  packing-excess b1 LRAT
14c2da3e8110e6ba50db1cb10fb28046b43b532dc32a5371fcd0f52b56346e70  packing-excess b1 drat-trim output
38a5d52b973a86432ff1b356e14fca5577e5c54d3e01411e1fd4d0a60fd49660  packing-excess b2 CNF
cf8619c074c850d188f9455568d97773c1795da02350120e7b25c1ff62315403  packing-excess b2 DRAT
0be2c8a5b9107c63ac00aeee237b2995fde9b1e18b41a1080d479e91f1e9f428  packing-excess b2 core CNF
61012e5380b49a4dd802d70cbc109495cff275b6eb6e336dc0267ad8687cb757  packing-excess b2 LRAT
faf82894360a7b27356fe81b1d7d4273fbb527215d2b8716d66a736f58de493f  packing-excess b2 drat-trim output
650db426720a23175066825f5b968e76951540d6001705c1874712deb70368ed  packing-excess b3 CNF
71062884e1f4a411ac4080182a3851eb922ff44fe8545a8b877e9eeb512a31c2  packing-excess b3 DRAT
46adc9fe5b54ac96ac652e270ecec2999da63d64c2c1ed4f5bea666d7040874f  packing-excess b3 core CNF
7df7ec65fea23a6ec07ee448aba34dcaaf528c23f13d6f78a07553ca7a4c5267  packing-excess b3 LRAT
06e4c92546f3af2f57943e098666dc875d917ca859d1cb2d612c498ba3b4ca72  packing-excess b3 drat-trim output
f28edbdc75bcfb2ceb0dde18153c30de011f6ec0a9e470a7acd3897d0edfa0df  packing-excess b4 CNF
165d5807394ae00a1354587bb692a1bd199a22a072f7074474e481f2f8d027af  packing-excess b4 DRAT
f3796b8f78452fff2c4cfb8763ec69c20ef4e51df1afb73454f114de8481b2ef  packing-excess b4 core CNF
797dd4cb1df0c095bef28617788ae71bfc8ec289a0e6580152fbd03cbcd17bf7  packing-excess b4 LRAT
5ebe3b0b7f2a1d046681d742fc2fb81ac5437960c7ba2e6a7426762f9f86e15e  packing-excess b4 drat-trim output
d6e04b9eefee41e84bc1a6bb9baa9fc6443bd62351bf39a272f2196a726b526c  packing-excess b5 CNF
dd4f719e6328b190877934afd3a771646d7640814f00af4ff01a8865947127fd  packing-excess b5 DRAT
3981c49eb46710fb8c14ff028b7cf4ab6454fe2b5d7fb35d17f90308c57897d4  packing-excess b5 core CNF
6e3f2a74b7a329e2afe00500e52acfeb3394949f1db3e80404abf64293b300f9  packing-excess b5 LRAT
e33f667fc2e9c1535db5395652b6f1954d6c16ed4f56ad995cc6948a82ae48f2  packing-excess b5 drat-trim output
dfbcf46d564295bf03b33a98113e90571d7711ec86c9254f76f39fc79f98b9d9  packing-excess b6 CNF
d73e771c1c81a9fc66cac6214604d0e23c0df0b832d8081ae15e89436cc72306  packing-excess b6 DRAT
5058164f0baf68277ef623a21ecc36e667ee0b4fbbb8aa56703fb74ae422d167  packing-excess b6 core CNF
83f5a1c49e5a974792f8c0717763bd8a682f1225a78ba709168c520216a013a9  packing-excess b6 LRAT
9d69ad667172c5fc61e41518debc74ce7e7d4392379bbea0e1be48eb1f5f67f8  packing-excess b6 drat-trim output
9c369ba99e8206e9317883acaf91b4d439e61f8c521d628b57c308a426eb2d70  packing-excess b7 CNF
d5109e74cec83de1ac42d46ab394c6a4f1ffb5004635902a1d9b4f587feb71d2  packing-excess b7 DRAT
6caab73b909135314073b963b7e5405a5187780df177d12368ed8eff760c23e0  packing-excess b7 direct proof replay
90884486628effeac5431569997eb0db2370464ec689a46f6f066d6f31a9e0c6  exterior-budget builder source
3315fb8972ab7150d21b7c71e57148b3e357f4d161d624f189e9cc92f9988ef3  exterior b0 CNF
1ef8d94c134da305a3e7aeefbcdf59b19d5930ae872308688f933ade2e2109b3  exterior b0 DRAT
275f9db78ccbc118412de0d382d2049b3e9b0c6b82329be55ce130518b86aeae  exterior b1 CNF
8b07e212195489902aa750f9b54f0377f305d1a01a48f77e36012e74b48a9a95  exterior b1 DRAT
7a81597a01d45e02e06e3b635954275df3e2f9805d5d1ba041908628d10920d5  exterior b2 CNF
bfd679031f62e633f22440cdd12bb4de1be87cc91d671c6cd8f9fc2c7e74dc66  exterior b2 DRAT
6948285afdeccb31db6bf67ef7686f3bbefc7fcc5ba2eeead6a21597b04af3aa  exterior b2 LRAT
a4a9c25fa1a47ef9385de0e357c951cb7294febd030a1765197ad8ef36ded442  exterior b2 drat-trim output
602aec565d4f59040c8fb4efa93093db4094dbba8fed6f903af3bda327a70707  physical core-audit source
3a6d6dc21720efc8633b64aa5d35667d23d1a3dad5b40c595101b75ad90516c8  budget0 core audit
0687e70876fd5e9a5b4aefa70ccda0d0a745f405f5d69b6fa48514b34f50ee46  budget1 core audit
6928234a66bbca5edbb15d71fbcce70e86d244c74a803a596c241c947d7b496b  budget2 core audit
8e475c262d2de07f4e8e02b93026a459fe3fa2488dc140de1f5ad109d386f39c  budget3 core audit
728b413892f3f4d7d339e394c92317196c849fe67c0110598cbe491f5f8ea1bb  budget4 core audit
026b3f95bcdc1f633c65af76171973b1f05517768c61c44665f0ce25b6d81de0  budget5 core audit
```

The compact machine-readable ledger is
`scratch/k17_y61423_physical_witness_transversal_1553_20260802.audit.json`.

## 5. Exact scope

Proved:

> Relative to the authenticated clean1666 factor, every exact-resource
> physical factor containing the protected bank and destroying all 1,666
> named short runs and all twelve named full-`Y` blocks changes at least
> 1,561 rank-eight facet choices.  The witness hypergraph alone has exact
> transversal number 1,553.

Not proved:

* that the unrestricted 90-edge bank has no resident completion;
* that 1,561 changes suffice once topology and newly created witness rows are
  enforced;
* that another starting factor has the same distance;
* that later CEGAR rounds create no new witnesses; or
* any statement about `nu(17)` or the all-k conjecture.

The theorem upgrades “local search seems stuck” to an exact incumbent-relative
reason: the first legal repair is necessarily a globally distributed
rethread, and every hitting pattern needs at least eight units beyond the raw
minimum transversal once the exact physical resource rows are imposed.
