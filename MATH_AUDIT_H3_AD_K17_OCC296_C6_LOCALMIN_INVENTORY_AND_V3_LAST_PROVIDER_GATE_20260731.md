# K17 occ296+C6 inventory and v3 last-provider gate

Date: 2026-07-31  
Lane: H3 independent audit for AD  
Verdict: **checkpoint PASS; literal v3 and protected-last-provider reuse require a format/row-semantics extension**

I did not edit the root producer.  No nonempty exchange repair, compiler,
common-cap matching, or K17 word is claimed.

## 1. Frozen construction chain

Search and export sources:

```text
scratch/search_k17_opt28_connected_circuit_lns_20260731.cpp
SHA-256 a185ef768d73809e8231bf2cd7b70b574663e615eec111e6aae25ae94c1040b2

scratch/export_k17_opt28_connected_search_state_20260731.py
SHA-256 a5a28fe721941a25abeeb9652a32e07c1d1d087fa71de638a4a42f7974d0e8d9
```

Input and final state:

```text
scratch/k17_opt28_occ296_c6_search_state_20260731.txt
SHA-256 a973d3bff87a4ae751f100c9548df4b5fb4bd8b786d20ecb2c970f5622f54097

scratch/k17_opt28_occ296_c6_localmin_state_20260731.txt
SHA-256 df816a09b5d0f1b2336e611ace3595298286116f3664c11556dbe25efd6d1321

scratch/k17_opt28_occ296_c6_localmin_candidate_20260731.json
SHA-256 960ca8df23e7c4ea28c6381e6642b4ec1ab86288a57329115d72182e56be949c
```

The candidate records `1160` accepted C6 moves and `4872` final residual-U
assignment rows.  The filename `localmin` is a search-checkpoint label.  No
complete enumeration of its entire legal exchange neighbourhood is frozen,
so this audit does **not** promote that label to a theorem of local
optimality.

Occurrence base and residuals:

```text
scratch/k17_opt28_occurrence_greedy296_verified_20260731.flow.json
SHA-256 079f5cd96f713ef2d72dd43acff10f84416acdb670aeff96f61a3cb97f29c25f

scratch/k17_opt28_occurrence_greedy296_connected_bflow_v2_20260731.json
SHA-256 63b49db80ad983bcd440aba3ac4b449888e30dea2d3c83e140e15b07082f69d0

scratch/k17_opt28_occ296_c6_localmin_verified_20260731.residual.json
SHA-256 6fcc91d45b2090b26b612020340a21088a2367c5c0bccd10d3d3614042c60fe4
payload c92b72db852a8362a2f99c8091dec072ef42af831e1ef83af5381375d6d2a6e4
assignment payload bcf4d6f9b543df3a1d5e8936f29ef3d85924d1ec7e24b960ceae78e0fb58bc82
```

The final residual pins the exact occurrence-flow SHA.  Its rows equal the
candidate rows.  Independently, they partition the `4872` nonpacket U owners,
fill all `9744` conditioned port incidences exactly, and together with the
`1430` macro edges and `133` packet-U edges form one connected degree-two
graph on all `6435` old ports.

Literal root artifacts:

```text
scratch/k17_opt28_occ296_c6_localmin_verified_20260731.owner_cycle.word
SHA-256 a47aa9d7c8b86ca3912c8c82262969332727d27bf427ee8783ccb1a8ce664b49

scratch/k17_opt28_occ296_c6_localmin_verified_20260731.materialization.audit.json
SHA-256 b12bb2feb207f3f88266aecf2f380dd072f0f9f66edcd7fe435f6eaf75b2177a
payload 101150d59e8a1c6852c666420e3a0dc9595ae9c5b0b0d351a9bfc7de9b0b5acf

scratch/k17_opt28_occ296_c6_localmin_verified_20260731.independent.json
SHA-256 b3625410b21b85c7b0794687ed6b79d37c1b801f051afaa82f567e7f9e1745c1
payload abd6dc3ad4823970c9bdda132774a4f3ca4047603303675e42e54f744498a433
```

Two further independent replays authenticate the same physical owner order
and Z row:

```text
scratch/h2_independent_audit_k17_opt28_occ296_c6_localmin_20260731.py
SHA-256 04e0148f4005f96c64df3f88d80628ffc8172e3c7fce67bf8f60e3c3fb1a1b29
scratch/h2_k17_opt28_occ296_c6_localmin_independent_20260731.audit.json
SHA-256 fc6716d285f774c246e22b7cbfd9a29f69391ace9f7d8089061d2fed57f38be7

scratch/h4_independent_audit_k17_opt28_occ296_c6_localmin_20260731.py
SHA-256 0be596135bffc24bafcbfb8363559670c67965976e27acf0f8901b4ee7371218
scratch/h4_k17_opt28_occ296_c6_localmin_independent_20260731.audit.json
SHA-256 0bca08d71f42db8fc97ff599328fd725c32abb0de2c30396ce72bf70374d32a4
```

## 2. Exact marked set and oriented cross edges

I reconstructed the marked set from the occurrence flow, the fixed packet,
the `106` mandatory components, and the `28` optional components.  It has
exactly `4108` owners and is one cyclic interval in the frozen owner cycle.
Its start in the saved order is position `21331`.

Authentication hashes:

```text
sorted marked set, decimal-newline SHA
1000abca19494ea85fc1c73fa6ed56a3e690266ffb10f1c5e6768b25fe232cd3

marked path order, little-endian uint32 SHA
4e260c9bb867fe177a14aa5a143da1a5a55d07b98cb56c751bb176b44a85e8ff

sorted complement set, decimal-newline SHA
70bbdacf9082480573e9d99cd8fed41cde37c4d56524c11f2b3c3692a142b2a6
```

After rotating marked-first, the two frozen directed cross edges are

```text
left:  marked 83766 -> complement 18358
       intersection 18230, union 83894

right: complement 7418 -> marked 71930  (linear closing owner edge)
       intersection 6394, union 72954
```

Both are Johnson edges.  There are exactly two cyclic bank transitions.  The
`4107` marked internal turns plus the two cross facets and `20201` complement
facets partition the entire rank-eight layer.

## 3. Literal Z replay

The exact two-bank row has `4108` marked rank-nine cells followed by `20203`
distinct rank-eight facet cells, so its length is `24311`.

Independent exact metrics:

```text
strict D2 bad                       503 = 230 length one + 273 length two
strict D3 bad                       503 = 230 length two + 273 length three
empty maximal envelopes              0
maximal-envelope volume          150224
minimum envelope size                 6
replay mismatch rows                748
replay missing bits                 776
host redundancy                  252803
upper holes rank 10 / 11 / 12  1585 / 824 / 116
upper holes rank 13..17               0
extensions through rank-12 stop  134403
```

These values agree with the root, H2, and H4 replays.  In particular this
checkpoint is strictly stronger than occurrence-only for residence and
replay, and unlike occurrence-only it has no rank-thirteen hole.

## 4. Exact rank-ten load and last-provider bank

For the linear owner chronology, excluding the final-to-first owner wrap as
required by the literal word, the rank-ten load profile is

```text
load        1      2    3   4  5
targets 12196   4948  662  54  3.
```

Thus there are `12196` current last-provider targets.  Their sorted
decimal-newline SHA is

```text
2f507b63c02f041bb1020b9ef178ff6ee8095c463e80ccfea5593d158c7fc051
```

Of these, `2826` are supplied on frozen marked/cross edges.  The remaining
`9370` have their unique provider on an exchange-eligible complement edge;
their sorted decimal-newline SHA is

```text
62d99663affa309cea7fc7fabf1857c279fac452df74f1eaf5ba713ce77432c5
```

The complete marked-preserving exchange bank still has exactly `545721`
columns.  Its projections at this checkpoint are

```text
current holes:       1585 targets,  54307 additive refs, support 10..45
all last providers: 12196 targets, 328399 additive refs
vulnerable last:     9370 targets, 289011 additive refs
```

Exactly one vulnerable target, `0x1c0df = 114911`, has no alternative
additive provider in the complement exchange bank.  Its incumbent provider
must therefore remain unless a move outside this marked-preserving bank is
introduced.

## 5. What the present evaluator can accept

The frozen generic evaluator is

```text
scratch/evaluate_ad_k17_opt28_marked_exchange_20260731.cpp
SHA-256 037ad2f0a4ec332b7ccbfdfba05730a10f1ed1f86091905f45a3c8bef35cbc60
```

### 5.1 C6 hole bank: yes, as version two

No evaluator semantic change is needed to evaluate exchange selections on
this C6 carrier when the seed target list contains the `1585` **currently
missing** rank-ten targets.  The exact v2 expectation trailer is

```text
(54307, 10, 45, 503, 503, 0, 748, 1585, 824, 116).
```

I generated an ephemeral v2 compatibility seed without touching the root
producer.  Its size was `3310` bytes, SHA
`cdcbb96057049e4f4906db343ac73810be9ff8ed4ab49f4f620efbcb6490e3d9`.
The frozen evaluator accepted the empty incumbent and reproduced the full
baseline; its JSON SHA was
`65655e7e2383020c6575bbfaf6cbe59fa1baeaa9af96531aae85a83f3a10a31e`.

Therefore a new producer may emit a C6-specific **v2 hole seed** immediately.

### 5.2 Literal version three: no, not currently

The parser explicitly accepts only versions one and two.  Changing the
otherwise valid C6 hole seed's version field to three gives fail-closed

```text
ERROR bad seed version
```

Thus the current executable cannot literally accept a v3 file without at
least a parser/layout extension.

### 5.3 Last-provider list in the existing single service bank: no

More importantly, this is not just a version-number issue.  The present seed
has one target-bank semantics:

* targets are assumed to be baseline holes needing a new gaining edge;
* support counts enumerate new-edge unions; and
* if every target is covered, the one-gain floor enforces
  `selected columns >= target count`.

Last-provider targets are already covered at baseline.  Reusing the single
target list for the `12196` last-provider rows makes the empty incumbent cover
every row with zero selected columns and then fail the one-gain floor.  An
ephemeral correctly hashed v2 seed for this experiment had SHA
`b9c7dab092820ff0024664011d394722b7bd8f545798ee80ea81b98ead0fc75a`;
the evaluator rejected it with

```text
ERROR one-gain-per-service-row floor failed
```

This rejection is correct for the current *hole-bank contract* but wrong for
a *protected-provider contract*.  Therefore a true v3 last-provider seed
cannot be accepted without semantic changes.

## 6. Minimal v3 extension

The physical factor, degree/connectivity, literal Z, residence, envelope, and
rank-ten-through-twelve scanning code can remain unchanged.  The seed and
service-row layer must distinguish at least two banks:

1. **gain rows**: currently absent targets; additive new-edge references and
   the one-gain cardinality floor apply;
2. **protected-loss rows**: currently covered targets whose last incumbent
   provider may be deleted; coverage must survive, but no selected-column
   lower bound follows.

For a solver-facing sidecar, protected rows should also name their incumbent
provider group and the columns that restore the target after its loss.  The
target `0x1c0df` becomes an exact keep-old-edge row inside this exchange
fibre.  Only the gain-bank cardinality may appear in the generic floor.

With that split, the current exact candidate chronology scan can evaluate
both banks without further geometric changes.  Without it, merely relabelling
the present list “v3 last providers” is not sound.

## 7. Independent audit artifact

```text
scratch/audit_h3_ad_k17_occ296_c6_localmin_inventory_v3_gate_20260731.py
SHA-256 639100dc5674606b8f2b1440d3341fba0c4559103572afda9e72858675672792

scratch/h3_ad_k17_occ296_c6_localmin_inventory_v3_gate_20260731.audit.json
SHA-256 50114eeea47a66d82d8f1d6b61f6efff61e9e7a7905dcbc41aeda71f73407170
payload 1ce938c103de78d4f58c361da8eaab55f9a809eee0999c2cd0cad8fdf895da83
```
