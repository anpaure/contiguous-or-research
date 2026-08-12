# `k=17`: exact common-live DM obstruction and minimal unary escape from the `e28a8e...` table

Date: 2026-08-01  
Lane: independent rooted-flag decoder / serial support-two repair  
Status: exact finite audit; no full common state transversal or cycle cover

## 1. Verdict

The frozen `d44b6061...` reverse packet has final rooted table

```text
scratch/threadA_k17_rooted_global_support2_shuffle201_h100_20260801/
  shuffle201_reverse.candidate.tsv
SHA256 e28a8ee5825564baf0d75720d8f3c1a53a911e9c53956aff49ed2460fd08c8dd
```

For each of its 12,870 root-owner attachment states, independently rebuild
all loop-free literal transitions.  Call a state **both-live** when it has at
least one incoming and at least one outgoing state arc.  In the bipartite
graph from the 1,430 roots to the 1,430 owners, retain exactly the incidences
whose state is both-live.

The exact maximum matching in this common graph is only `718`.  The
deterministic alternating-reachability min cut is

```text
tails X                    770
heads N(X)                  58
deficiency                 712
SHA256(sorted tail IDs)    980087d9fa6dbd3fc87a8c5ba90179a31aa727f71db5aaffdbbde6395dcd4773
SHA256(sorted head IDs)    87a3c7dfbcb139dfe64c5f6994f063599247ae18c3f9e1a74820288ac36e25dd
```

Thus there is no common 1,430-state root-owner transversal, even before
requiring that its selected states possess a transition cycle cover.  An
induced cycle-cover component profile is consequently undefined.  The same
literal replay gives

```text
packet matching / zero-out / zero-in       954 / 234 / 445
state zero-out / zero-in                  2803 / 11140
owner zero-out / zero-in                     0 / 351
root-owner in/out/both matching            890 / 1196 / 718.
```

## 2. Exact smallest-support escape

The authenticated `d44b6061...` packet changes 856 roots, leaving 574 roots
available for an additional root-disjoint circuit.  Independently enumerate
all 1,904 literal flags at each available root and retain every nonincumbent
zero-resource-delta option.  There are exactly `220` such unary circuits.

All 220 were applied one at a time to the complete `e28a8e...` table, after
which every rooted transition, state arc, liveness bit, common incidence,
Hopcroft--Karp matching, and Hall shore was rebuilt.  Five options add an edge
from the old Hall tail shore to an owner outside its old neighbourhood; exactly
one increases the common matching:

```text
root                       1080
option_id                  2056402
old (type,C0,C1,C2)        (0,1024,10564,9)
new (type,C0,C1,C2)        (0,64,11524,9)
```

This is a literal singleton-phase pivot.  The type and `C2` are unchanged,
and

```text
old C0 union C1 = new C0 union C1 = 11588,
canonical outer target = 2897.
```

Both inner sets have rank one and therefore carry no tight resource.  Hence
the resource difference is exactly zero relative to `d44b6061...`; root 1080
was untouched by the old packet, so it is also exactly zero relative to
`e28a8e...`.  The same row is simultaneously

1. an arity-one root-disjoint extension of the 449-circuit `d44b` packet; and
2. an arity-one primitive circuit in the fresh `e28` fibre.

Since a nonidentity circuit cannot have support zero, arity one is the
smallest possible resource-circuit augmentation.  Within the complete set of
eligible root-disjoint unary extensions, this is the unique matching gainer.

## 3. Fully recomputed effect

The pivot changes the loop-free root graph by

```text
removed  1080 -> 175
removed  1080 -> 176
added    1080 -> 937.
```

At the common both-live root-owner level, it makes the exact one-for-one
replacement

```text
removed  (root 175, owner 712)
added    (root 937, owner 781).
```

Root 937 belongs to the old 770-tail Hall shore, while owner 781 is outside
the old 58-head neighbourhood.  This is the desired escaping DM incidence.
Fresh matching/min-cut replay gives

```text
common matching                 718 -> 719
Hall deficiency                 712 -> 711
new Hall tails / heads          767 / 56
new tail ID SHA256              9e192e1442a7d77c75fe8bfe318699ad57654b0d306dc9eeb248f99ef8eff11b
new head ID SHA256              419de8e39db23389f28efc2a3b8042a5c1e477bd30d677a079cfa33e12099e26
```

The packet projection stays `matching/zero-out/zero-in = 954/234/445`.
Owner zero-out stays zero; owner zero-in changes `351 -> 352`.  State zeros
change from `2803/11140` to `2804/11140`.  The augmentation is therefore an
exact common-matching improvement, not a monotone improvement of every
relaxation.

The four other unary Hall escapes do not raise the common matching:

| root | option | escape edges | common matching | in-live matching | packet matching | owner zero-in |
|---:|---:|---:|---:|---:|---:|---:|
| 654 | 1245392 | 1 | 718 | 891 | 953 | 349 |
| 747 | 1422338 | 1 | 718 | 891 | 953 | 351 |
| 907 | 1727090 | 1 | 718 | 890 | 954 | 351 |
| 502 | 955997 | 1 | 717 | 889 | 953 | 352 |

This demonstrates why an escaping edge is a useful DM filter but a fresh
maximum-matching replay is still necessary.

## 4. Relation to serial round 1

The later serial table is

```text
scratch/laneK_k17_rooted_flag_catalogue_bind_20260801/
  e28_round1_reverse.candidate.tsv
SHA256 449713150e945977420638c65ab411b2f26e188b9bd48d4949f2f64a46a9d207
```

It **does not retain** the unary pivot.  Serial step 219 uses a binary circuit
on roots 1058 and 1080, and the final row 1080 is

```text
(type,C0,C1,C2) = (1,64,11525,8),
```

not the unary row `(0,64,11524,9)`.  Thus the unary was superseded, rather
than silently incorporated.  The serial table is nevertheless much stronger:

```text
packet matching / zero-out / zero-in       1110 / 134 / 307
state zero-out / zero-in                   1918 / 10928
owner zero-out / zero-in                      0 / 282
root-owner in/out/both matching             980 / 1296 / 867
```

Its common-live Hall cut has `684` tails, `121` heads, and deficiency `563`,
with tail/head hashes

```text
48f6ed9429429831306782eb06ae2fee81e2124cd9e00b4b1092a3b870178ec7
f0f3387add3791fc498cff2730f242682414509b85a544fa91c0b4ac07b81bd2.
```

It too has no full common transversal, so its quotient component profile is
undefined.

## 5. Frozen artifacts

Independent verifier and original `e28` common Hall audit:

```text
scratch/verify_k17_disjoint_support2_selector_20260801.cpp
  SHA256 0d0f68bc3524579b940f8797a7dacc2dd531d7417f132c92ffbf09ee906e7d23
scratch/laneK_k17_rooted_flag_catalogue_bind_20260801/
  shuffle201_reverse.selector.independent.audit.json
  SHA256 a5ada1febde2daaa621bac54b0722a7429672d03b56c8aa4de20900b26d681e2
```

Exhaustive unary scan and summary:

```text
scratch/search_k17_e28_dm_unary_augmentation_20260801.cpp
  SHA256 6d6cc906c47958eca3316a3426250fa718e581a1c3095534c894cb9e5547ec88
scratch/k17_e28_dm_augmentation_20260801/unary_scan.audit.json
  SHA256 9b0fda0403fe2cbb868518b0fd752c0d8f55eb57333704254186534ec549b33f
scratch/k17_e28_dm_augmentation_20260801/unary_scan.unary_hits.tsv
  SHA256 db0b0551bef7c8c6e44f01f0f7828a8af8a249938711604505c2f2accee4716b
```

Augmented table, d44-packet extension, and fresh-e28 primitive replay:

```text
scratch/k17_e28_dm_augmentation_20260801/unary_scan.best_unary.candidate.tsv
  SHA256 a3aa2fb148c3b4fdfc92e6069c0b97578dd18b5e34e66469b7899804555d9036
scratch/k17_e28_dm_augmentation_20260801/
  unary_scan.best_unary.d44b_extension.selected_circuits.tsv
  SHA256 b8a2d8d7e63909d45ce0fca6b291f558cbe7783397d06fb8da3247b413c0b24c
  unary_scan.best_unary.d44b_extension.manifest.json
  SHA256 845ac6e05570a8de5765efc515196e5f284504ba6617c3f2c94bb027f9128d66
  unary_scan.best_unary.d44b_extension.independent.audit.json
  SHA256 a5e88c84506134a6d9f07b0ddc36580b44a87549df5143c4d20251d5e19a7737
  unary_scan.best_unary.e28_primitive.selected_circuits.tsv
  SHA256 6143d1e2825445d859473452249e453eaae3b1e17fa2bedaf196c3b7e6d4408a
  unary_scan.best_unary.e28_primitive.manifest.json
  SHA256 cb858861021e9bf2347093f48a1b6aa561408ec6e43ad1a0fd1f2030d0d3eaaf
  unary_scan.best_unary.e28_primitive.independent.audit.json
  SHA256 e118768a9a5f2e32aaa4c18f48d1ffcd94e7f50309fa4e4029bcf9e15a520a9a
```

Serial-round independent audits:

```text
scratch/laneK_k17_rooted_flag_catalogue_bind_20260801/
  e28_round1_reverse.owner_demand.audit.json
  SHA256 046230a87c16c950ea2cd563e4e0f2d537998426979343bf7331022295bdf4c1
  e28_round1_reverse.common_live_dm.audit.json
  SHA256 76330efa102b4b08066420ee80bc5a2ab760998cdeca1757e9f5412a7ef08c36
```

All selector-side catalogue hashes in these manifests are declared
provenance for in-memory catalogue enumeration.  The independent claims above
do not rely on catalogue IDs: they replay literal rows, exact resources, the
complete transition graphs, maximum matchings, and Hall witnesses directly.
