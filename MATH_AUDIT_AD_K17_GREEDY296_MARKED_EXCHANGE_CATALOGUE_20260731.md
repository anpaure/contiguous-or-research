# AD audit: greedy296 marked-preserving exchange catalogue

Date: 2026-07-31

## Scope

This note independently rebuilds the lower-rainbow exchange master for the
greedy296 OPTIMAL28 checkpoint.  It does **not** reuse the old 545,721-column
edge list.  The marked path is frozen.  Endpoint balance, one-cycle
connectivity, residence, rank-11/rank-12 chronology and common-cap feasibility
remain separate constraints.

## Theorem 1 (exact checkpoint split)

The files

- `scratch/k17_opt28_occurrence_greedy296_verified_20260731.flow.json`,
- `scratch/k17_opt28_occurrence_greedy296_connected_bflow_20260731.json`, and
- `scratch/k17_opt28_occurrence_greedy296_connected_full_20260731.owner_cycle.word`

reconstruct exactly one 24,310-owner Johnson cycle.  Its 6,435 objects split
cyclically into one marked interval of 304 objects/4,108 owners and one
complement interval of 6,131 objects/20,202 owners.  The marked interval has
171 macro objects and 133 U-owner objects.  Its 4,107 internal lower colours,
the complement's 20,201 internal lower colours, and the two cross colours are
pairwise distinct and partition all 24,310 rank-eight colours.

The two cross edges in the saved owner order are exactly

| position | direction | owners | lower colour |
|---:|---|---|---:|
| 1128 | marked to complement | 83766, 18358 | 18230 |
| 21330 | complement to marked | 7418, 71930 | 6394 |

**Proof.**  Reconstruct all 1,430 macro blocks from their physical occurrence
nodes, add the 133 fixed and 4,872 residual U objects, and traverse the resulting
degree-two port graph from its least port.  The resulting owner list agrees
term-for-term with the saved word.  Marking the stated macro and fixed-U
objects gives exactly two cyclic status changes.  A literal scan gives the
three edge counts above and 24,310 distinct intersections.  The independent
verifier reconstructs the marked interval solely from the two oriented cross
edges and repeats the count.  ∎

## Theorem 2 (complete compact exchange universe)

For each complement-internal lower colour `c`, let `e_c={a_c,b_c}` be its
current edge and let

`V_c = {v : |v|=9, c subset v, and v is outside the marked owner set}`.

Every marked-preserving same-colour replacement of `e_c` is uniquely an
unordered pair `{u,v}` from `V_c`, other than `{a_c,b_c}`.  Conversely, every
such pair is a legal Johnson edge with intersection `c`.  Hence the exact
column count for the group is `binom(|V_c|,2)-1`.

For greedy296 there are exactly 20,201 groups and 545,721 implicit columns.
The profile of `|V_c|` is

| `|V_c|` | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| groups | 15 | 129 | 454 | 1,601 | 3,836 | 6,748 | 7,418 |

**Proof.**  Two distinct rank-nine supersets of a fixed rank-eight `c` differ
only in their respective added coordinates, so their intersection is exactly
`c`.  Conversely, any rank-nine Johnson edge of colour `c` consists of two
such supersets.  Freezing the marked path and both cross edges makes precisely
the 20,201 complement-internal colours eligible.  Direct enumeration from the
new marked set gives the profile and sum.  No old column is imported.  ∎

The compact JSON stores each group as `(c,e_c,V_c)`; a C++ evaluator expands
the columns by `i<j`, excluding the stored old-pair indices.

## Theorem 3 (exact rank-ten provider census and signed relaxation)

The greedy296 linear nonflat Z row has exactly 1,908 missing rank-ten targets.
Its rank-ten hole set is exactly the hole set of current owner-edge unions.
Across the new exchange catalogue these holes have 66,606 provider incidences
using 16,445 distinct lower-colour groups.  Every hole has support, with
minimum 10 and maximum 45.

Every selected column has the exact signed rank-ten delta

`+1[new union] - 1[old union]`.

Therefore every completion needs at least 1,908 selected columns.  This bound
is tight in the degree/connectivity/residence-free signed-row relaxation: the
catalogue contains an explicit 1,908-column seed using distinct groups; each
deleted old union is used no more often than its initial surplus, and literal
replay leaves all 19,448 rank-ten rows positive.  The seed SHA-256 is
`4d5d070af3cddd34c4d6f6aa1cb807ad47ba100522c8f4442a2c2700f84f87ae`.

**Proof.**  The rank-ten hole identity is checked by two independent scans:
all changing intervals of the 24,311-cell Z row, and all adjacent unions of the
owner cycle.  Provider enumeration tests every pair inside the exact `V_c`.
For the relaxation, connect each old rank-ten colour to its groups with
capacity equal to its load minus one, each group with capacity one, and each
hole with demand one.  Exact integral max flow has value 1,908.  Replaying the
exported integral witness verifies every signed row directly.  ∎

This theorem is deliberately not a physical rethread theorem: the seed need
not balance owner degrees, form one cycle, or satisfy residence/deeper rows.
Indeed its raw endpoint-degree delta is nonzero at 4,195 owners, has
`L1=4,536`, and maximum absolute imbalance 3.  It is an exact rank-ten seed,
not a factor.

## Comparison with the old static 218-hole set

The old static set is reconstructed from the old macro forest rather than read
from a truncated sample.  Its sorted-set hash is
`cda1d49d62b377782acbc82764bfd19fb0aee65121bbe91189d3833d7d6a29de`.

- 186 of the old 218 are holes of the current linear Z row.
- The old catalogue had 6,419 provider incidences on these 218 targets.
- The newly rebuilt catalogue has 6,385: all 218 still have support 10--45.
- At semantic-column level, 4,866 survive, 1,553 disappear, and 1,519 are new.

Thus reusing the 6,419 old columns would be unsound even though the aggregate
support changes only by 34.

The greedy296 fixed residual-pair fibre itself has 177 static rank-ten holes
(set hash `b383958488c70ea67ecf5678f84677c68e666cbf5eb4a1f98b7ecd48bee3f778`),
of which 137 lie in the old static set.  All 177 are current linear-Z holes and
have 4,973 exchange incidences, support 10--44.  Hence greedy296 improves the
static no-go from 218 to 177 but does not revive the fixed-pair fibre.

## Exact remaining boundary

The compact master is the correct starting universe for a physical repair.
One must still select columns so that:

1. every complement owner has zero signed degree imbalance;
2. the resulting complement factor, together with the frozen marked path and
   two cross edges, is one cycle;
3. rank-ten signed rows remain positive;
4. the chosen chronology satisfies strict D2/D3 residence and rank-11/rank-12
   interval rows; and
5. its nonflat erosion envelopes admit the common-cap compiler Hall matching.

Ranks 11 and 12 cannot be assigned a context-free one-edge delta: their
interval witnesses depend on the final edge chronology.  The catalogue exports
literal endpoints for exact post-selection replay rather than asserting such a
delta.

## Frozen artefacts

- Generator/audit:
  `scratch/audit_ad_k17_greedy296_exchange_catalogue_20260731.py`
  SHA-256 `00c6e0dd210ee60cbb0b2543d65c8ea1aa7e26d8079f14eb030a160782d31da4`.
- Compact catalogue:
  `scratch/ad_k17_greedy296_marked_exchange_catalogue_20260731.json`
  SHA-256 `c31071269fb709d28887e5d3590be15d5af727560809c8476dd2981ef546ea2a`,
  payload `6e6c82c14246792da7848e71a3665657c30063936d18a5801471b395a970a266`.
- Generator audit:
  `scratch/ad_k17_greedy296_marked_exchange_catalogue_20260731.audit.json`
  SHA-256 `ded898e2123548ba7361e96ca06f8638cd8a0a795511ea51b7d6f24db4d18580`,
  payload `f2d40ca09eefb22d4cf5b28108809fb15d784b065c1260f101213e764f0b4881`.
- Independent verifier:
  `scratch/verify_ad_k17_greedy296_exchange_catalogue_20260731.py`
  SHA-256 `618e244035c1183e0e8ec6479c706858fe123a76014b36439135b985ef056aff`.
- Independent audit:
  `scratch/ad_k17_greedy296_marked_exchange_catalogue_20260731.independent.audit.json`
  SHA-256 `c2046b761fc5644ffcfbc711f3e0bc2db0a5c62e19fb1e83a0340ce6cac59fb8`,
  payload `ee072bcacde1d75a8ba753b8b98e71147f39408d00298b64c54b5618d42e4afe`.
