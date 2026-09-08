# K16 WIDTH45 provider/path and special-cycle theorem: the Sep5 seam floor is 98

Date: 2026-07-30  
Lane: R  
Status: proved for the frozen source-relative WIDTH45 one-seam service model
under global five-position cut separation.  No WIDTH45 carrier, compiler
solution, or `K=16` word is claimed.

## 1. Exact scope and frozen objects

The source factor is

```text
scratch/k16_asymmetric_len8_orbit_repair_20260730.json
SHA-256 6bea170e55a52a6f345382efac6bf898dcb11f18ce0f4c3dd392b9a59cd8d204
```

The compact q<=3 physical seam ledger is

```text
scratch/k16_len8_source_seam_ledger_20260730.bin
SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657
```

It has 12,870 transition ports and 211,604 directed, nonold,
positive-collar-safe Johnson seams.  The defect bank consists of 45 lower-q2
targets and 48 upper rank-eleven targets.

For a seam `a`, let `H_45(a)` be the set of distinct defects supplied by its
isolated crossing windows: lower-q2 uses the natural three-owner window, and
upper rank eleven uses four- or five-owner windows.  A seam is a WIDTH45
provider when `H_45(a)` is nonempty.

The constructive hypothesis is the explicit cyclic Sep5 condition

```text
for every source-cycle position p,
    c_p+c_(p+1)+c_(p+2)+c_(p+3)+c_(p+4) <= 1.          (1.1)
```

This is not the retracted four-separated WIDTH45 draft.  The later
authoritative separated-port theorem observed that, in its source-position
indexing, a width-five occurrence can meet two cuts at source distance four.
Thus the isolated width-five signatures are credited constructively only
under (1.1), or through exact occurrence activators as described in Section
7.

Endpoint balance makes every selected seam set a disjoint union of directed
cycles on transition ports.  All lower bounds below relax mutual Sep5
conflicts and many other physical constraints after retaining the isolated
WIDTH45 service premise.  Such relaxations can only lower the computed costs.

## 2. Exact WIDTH45 reclassification

### Proposition 2.1

The provider census changes from

```text
fixed upper width four / q<=3 providers       5,425
combined upper widths four and five           5,575
new width-five-only providers                    150
```

All 150 new providers are singleton upper providers.  No old provider gains a
new distinct defect, so the 193 double-provider seams, 119 distinct defect
pairs, matching number 37, and exact provider-only floor 56 are unchanged.

The new per-target incidence histogram is

```text
2^14 3^17 4^14 5^3,
```

and every one of the 48 upper targets gains at least two providers.  Each of
the three targets `46811,56173,60854` gains five.

#### Proof/certificate

The WIDTH45 checker rebuilds every four- and five-owner split from the frozen
source, compares each combined hit set with its width-four hit set, and checks
all 211,604 columns.  It returns hit-cardinality histogram

```text
0^206029 1^5382 2^193.
```

The 150 difference columns have empty old hit set and one upper hit.  QED.

### Catalogue-ID correction

Frozen-source seam IDs are not compact-binary seam IDs.  Of the 150 new
records, 142 have different numerical IDs in the two catalogues.  The physical
directed endpoint pair `(left transition,right transition)` is the invariant
identifier.

The special-cycle checker therefore maps all 150 records by endpoint pair,
checks that every pair occurs exactly once in the binary catalogue, and checks
that its binary q<=3 hit set is empty.  The complete 150-row conversion table
is persisted in the primary audit.  Its canonical JSON SHA-256 is

```text
ac5d17239b647679d90c02f52f556dc4b2f7bd66875ea5934215666f89a2b6e1.
```

No theorem in this report identifies seams across those catalogues by their
local integer ID.

## 3. The WIDTH45 provider-path dual

Let `D_45` be the directed graph of all 5,575 providers.  Delete the `z`
selected nonproviders from a balanced selected port permutation.  What
remains is a union of provider cycles and at most `z` nonempty provider paths.

The exact WIDTH45 SCC replay gives

```text
strong components                         12,804
nontrivial strong components                   9
largest strong component                      45
internal provider arcs                         75
targets serviceable on provider cycles         45
cycle-unserviceable targets                     48
condensation ordered pairs                   5,500
exact union states created                  28,203
active nondominated states                  24,928
global maximal path masks                    1,094
```

The same 33-target half-weight set from the q<=3 theorem remains valid:

```text
33609 34069 34450 35370 35461 36132 36969 37389 37972 38154 39496
41170 41285 41633 42010 42115 43089 43176 43540 46224 46811 49572
49802 50498 51252 51462 53410 53584 53825 54312 56173 59680 60854
```

Every maximal WIDTH45 path mask meets this set in at most two targets.  Hence
the exact rational dual with denominator two has numerator 33 and proves

```text
number of provider paths >= ceil(33/2) = 17.              (3.1)
```

Conversely, the authenticated old 17-mask cover projects onto the WIDTH45
cycle-unserviceable bank.  Every nonempty projection is contained in a
regenerated WIDTH45 maximal mask, and the seventeen projections cover all 48
targets.  Therefore the permissive SCC-free-router path-cover number is
exactly

```text
tau_45 = 17.                                               (3.2)
```

Together with the provider floor 56, this preserves the old path-decomposition
floor 73.  It does **not** construct seventeen vertex-disjoint physical paths,
connectors, or a Sep5 port permutation.

## 4. Reoptimized WIDTH45 port potential

Use the positive integer target weights from the authenticated scale-20 base
certificate.  Their total is

```text
sum_t w_t = 1899,
```

their minimum is 11, and exactly the three targets

```text
S = {46811,56173,60854}                                    (4.1)
```

have weight 23.

The old port potential does not transfer verbatim: fifteen new WIDTH45
providers, one rotation orbit, have reduced cost `-3`.  All fifteen are
individually Sep5-compatible.

However, the same target weights admit a new exact integer potential
`phi_45` on all 12,870 ports.  Longest-difference closure terminates in five
passes after 1,320 improvements and gives

```text
0 <= phi_45(v) <= 20,

w(H_45(a)) <= 20+phi_45(head(a))-phi_45(tail(a))            (4.2)
```

for every WIDTH45 provider.  Its vector SHA-256 is

```text
5eb2f287aaa3880ff9b04f411911b27625e367ab8f9f2dd23c51ef06c57f898a.
```

For every seam define

```text
rho_45(a)=20+phi_45(head(a))-phi_45(tail(a))-w(H_45(a)).    (4.3)
```

For a nonprovider the last term is zero.  Thus every seam has nonnegative
cost.  If a balanced service selection has `C` seams and target multiplicity
`m_t`, telescoping the potential around its selected directed cycles gives

```text
20 C = sum_t m_t w_t + sum_selected rho_45(a).             (4.4)
```

Coverage alone gives `20C>=1899`, hence `C>=95`.  At equality 95 the cost
budget is one.  The cost-at-most-one graph has fifteen nontrivial SCCs, all of
size five; only 90 arcs are internal, of which 60 are providers.  Those
providers serve 30 targets and miss 63.  Therefore equality 95 is impossible
and

```text
C >= 96.                                                   (4.5)
```

Section 5 strengthens this to 98.

## 5. Exact special-cycle costs under `phi_45`

Every member of `S` has exactly 65 WIDTH45 providers.  Every such provider
hits that one target and no other defect, and the three 65-seam banks are
pairwise disjoint.  Their individual reduced-cost histogram, identically for
each target, is

```text
0^50 1^5 3^5 15^5.                                        (5.1)
```

For one specified service seam `a:u->v`, any selected cycle containing it has
cost at least

```text
rho_45(a) + dist_rho45(v,u),                               (5.2)
```

where the distance is the exact nonnegative shortest-path distance in the
directed seam graph.  Enumerating all service seams and cyclic orders gives

```text
minimum closed-walk cost containing target 46811             17
minimum closed-walk cost containing target 56173             17
minimum closed-walk cost containing target 60854             17

minimum closed-walk cost containing any specified pair       36
minimum closed-walk cost containing all three                 51.  (5.3)
```

The all-211,604-arc graph and the individually Sep5-compatible graph are in
fact identical for this catalogue, so both independent replays return (5.3).
Global mutual Sep5 conflicts are still omitted.

The pair and triple routes are genuinely cheaper than in the base q<=3
potential, where their costs were 39 and 55.  They do not lower the decisive
partition minimum:

```text
three singleton cycles              17+17+17 = 51
one pair cycle plus one singleton      36+17 = 53
one triple cycle                              51.           (5.4)
```

The primary audit persists the minimizing service seams and every connector's
seam-ID/vertex path, and replays every displayed total exactly.

## 6. The WIDTH45 floor-98 theorem

### Theorem 6.1

Every balanced selected port permutation in the frozen WIDTH45 isolated-seam
service system which satisfies global Sep5 and covers all 93 defects has at
least 98 selected seams and cuts.

#### Proof

Choose one selected provider occurrence for each target in `S`.  The selected
directed cycles partition those three marked occurrences.  For a singleton,
pair, or triple block of that partition, the containing physical cycle is a
closed walk in the relaxed graph used in Section 5.  Hence (5.3)--(5.4) imply

```text
sum_selected rho_45(a) >= 51.                              (6.1)
```

Repeated target service only increases the first term of (4.4), because all
weights are positive.  Combining (4.4), coverage, and (6.1) gives

```text
20 C >= 1899+51 = 1950.
```

Therefore

```text
C >= ceil(1950/20) = 98.                                   (6.2)
```

QED.

This is the strongest solver-free WIDTH45 cut floor proved here.  It does not
assert that 98 is attainable.  The newer scale-140 base-catalogue floor 101
has not been transplanted to WIDTH45 and is not inferred here.

## 7. Occurrence and physical boundary

Under Sep5, isolated width-four/five loss and gain signatures are additive.
If Sep5 is weakened, a one-seam width-five occurrence for seam variable `y_a`
and split `r` may be credited only with an activator `z_(a,r)` satisfying

```text
z_(a,r) <= y_a,
z_(a,r)+c_j <= 1                 for each of the three collateral cuts j,
z_(a,r) >= y_a-sum_j c_j.                                 (7.1)
```

Equation (7.1) is exact for that emitted one-seam occurrence but incomplete
for a window crossing two selected seams.  A complete close-cut model must
enumerate those compound occurrences; this report does not.

The theorem also does not cover arbitrary upper widths six and above, another
carrier, open-boundary rethreads, non-row-power compound trades absent from the
isolated seam catalogue, connectivity, reverse-edge conflicts, q1 ledgers,
survivor rows, or the literal compiler.  Shortest connector walks may repeat
ports or arcs and different marked cycles may intersect.  Those are deliberate
relaxations, so they preserve the lower-bound implication but provide no
physical construction.

## 8. Finish-chain readiness

Any future SAT carrier can be passed to the already patched even-K finish
chain.  Its pinned hashes remain

```text
ct_handoff.py ff85c33f19901db576670a6485814d0986e4640062bff313853217502176e831
cutscan16.py  fa44126112fd9c604e15541435ae6f6d9dececf0581bf0dd96f6ce375d2b72b9
sandwich2.py 126173c22262c51f90c3e6740b31484d635fb9b9c6f94f60e7d46e3a2ad6b098
comp3.py     27299d722bc78b4bf14f62ceb50d210e9e762f6b71f2270bd8b4c5ff1ba55bb0
```

The interface fixes the exact cut orientation, treats every upper loss as
hard, and sends at most two lower-q1 losses into the exact boundary-SDR/common
COMP3 solve.  A positive compiler result still requires fresh literal word
materialization and exhaustive verification.

## 9. Audited artifacts

### WIDTH45 provider/path/potential certificate

```text
scratch/audit_k16_width45_provider_path_dual_20260730.py
SHA-256 1a36e5915ad73c17acb3cd38fbe133918cea8787e593b16400938945fd84cbf8

scratch/k16_width45_provider_path_dual_20260730.audit.json
SHA-256 115ce4dfbcfdbd652c0696f21c6f44b5ed58737f16752fa1e5bd203477c12f4a
payload 9f6efacc29ad54e4917ff82c28d4d58fe9068493d131713a56ba9d5b436f1ef2

scratch/k16_width45_provider_path_dual_20260730.resource.txt
SHA-256 61e2f7ff299b264491f5037aadd850d06e17c55e31174b9477e91f1bace398e7

scratch/k16_width45_provider_path_dual_20260730.stdout.txt
SHA-256 12d4f07df5a84ec300889ce4921c73f7685e3f8a6df4562e471b119f46984c70
```

The final payload hash is reload-stable.  An earlier certificate whose file
SHA was sound but whose payload hash depended on pre-JSON integer-key ordering
was retained only as a recoverable pre-fix artifact and is not authoritative.

### Primary WIDTH45 special-cycle replay

```text
scratch/audit_k16_width45_special_cycle_cost_20260730.py
SHA-256 3a7b9f59a77de9e34a8afcd355c08feb1c017f1e220e00a9a07db9a67e4e4ba4

scratch/k16_width45_special_cycle_cost_20260730.audit.json
SHA-256 5aeca148d519b6c6b48677c825de0dc812e319003e7d6210b40394d7b68ddae6
payload 885deb403002a654bdd1b57c8a7a0b8e12c1252c8f0f649e89547121b060c834

scratch/k16_width45_special_cycle_cost_20260730.resource.txt
SHA-256 e942e3701f2be6dfb43a447f0020e0f34dd916d20d91e8794c024720b0672345

scratch/k16_width45_special_cycle_cost_20260730.stdout.txt
SHA-256 c4ea88dcd1f0769d25e739b26e554140a0d29276f759d9e8ee098203cb9fa517
```

This replay used one H100 CPU, a 2 GiB address-space cap, 12.85 seconds wall
time, and 93,192 KiB maximum RSS.

### Independent implementation

```text
scratch/audit_r_k16_width45_special_cycle_cost_20260730.py
SHA-256 4c6c7baf0b018530169ea4b88e7b61b772a249992b5b66051fdb0b8e9c95b9a0

scratch/k16_width45_special_cycle_cost_independent_20260730.audit.json
SHA-256 354f62a056c10b26ddd74f8870dc02d400d5ca1bf19d909876daebc7d06c04f4
payload fd8c779c165a7c539b651eb2f972700354bdb42b729b88d541d11e28b97b9654

scratch/k16_width45_special_cycle_cost_independent_20260730.resource.txt
SHA-256 c25fbbb3e63352e0a6bc72198d799ee9810cf2e157d33d8a000c2739e5489a3b

scratch/k16_width45_special_cycle_cost_independent_20260730.stdout.txt
SHA-256 e8325fdb158384873527efc152bbe5314518995eac50d80d16599047b0ab97c5
```

The independent implementation uses the existing compact-ledger parser rather
than the primary raw parser, reconstructs the same endpoint-pair augmentation,
and independently returns singleton `17`, pair `36`, triple `51`, partition
floor `51`, and cut floor `98`.
