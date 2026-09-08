# K16 delete-p1 collar594: trivial physical symmetry and endpoint-antichain CNF extension

Date: 2026-07-31  
Status: **PASS propagation-only; exact fibre now solver-free closed by immutable ghost**

## 1. Frozen scope

Fix the length-12,873 delete-p1 source

```text
scratch/k16_upper12874_delete_p1_optimal_onehole.word
SHA256 a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649
```

and permit arbitrary nonzero values only at

```text
[0,5) union [6435,6444) union [12869,12873).
```

The authenticated target-intersection normalization maps this unrestricted
18-cell fibre equisatisfiably to 245 nonzero closure-fixed values.  Its frozen
CNF has 5,338 variables, 76,653 clauses, 61 residual targets and 4,218 exact
witness variables.  This note does not add a change-count condition.

## 2. There is no natural physical symmetry to break

Coordinate permutations and editable-position interval automorphisms are the
natural physical symmetry group of this fixed-complement model.

The residual-target degrees of bits `0..15` are

```text
57,12,33,40,16,58,40,14,0,21,48,28,29,17,36,39.
```

The sole degree tie, bits 3 and 6, is already split by their rank-incidence
histograms (and independently by pair incidence).  Thus every coordinate bit
is fixed.

The 70 active editable supports are exactly the interval hypergraphs

```text
P5 disjoint-union P9 disjoint-union P4.
```

Component sizes force every support automorphism to preserve each path; the
only candidates are independent reversal of the three paths.  Exact witness-
ledger symmetric differences are

| reversed paths | symmetric difference |
|---|---:|
| none | 0 |
| right | 108 |
| middle | 672 |
| middle + right | 780 |
| left | 512 |
| left + right | 620 |
| left + middle | 1,184 |
| all | 1,292 |

Therefore the identity is the only natural physical automorphism.  A lex
leader based on a collar reversal would be unsound.

There is also no smaller positionwise unary closure domain: every one of the
61 residual targets has a retained term through every editable cell.  All 18
positionwise target families are the full residual family and all 18 domains
remain the same 245 values.

## 3. Exact physical endpoint domains

A retained witness row has the form

```text
w = (target T, editable block [a,b], need N).
```

Its fixed physical base is uniquely `B=T & ~N`.  Enumerating the monotone
suffix and prefix OR states gives every physical interval having editable
intersection `[a,b]` and fixed base `B`.

All 4,218 witnesses have a physical form.  Their endpoint-domain histograms
are

```text
left endpoints:   size1 -> 4210, size2 -> 8
right endpoints:  size1 -> 4218.
```

If two physical intervals have the same left endpoint, or the same right
endpoint, they are nested.  Their OR targets are therefore comparable by
inclusion.  Two distinct equal-rank targets are incomparable, so they cannot
both be realized by witnesses exposing the same endpoint.

## 4. Compact endpoint-antichain extension

For every nontrivial quadruple

```text
(side in {L,R}, target rank, physical endpoint, target T)
```

introduce an occupancy variable `y`.  For every exact witness `w` of `T`
whose physical endpoint domain contains that endpoint, add

```text
not w OR y.
```

At each fixed `(side,rank,endpoint)`, add pairwise at-most-one clauses among
the occupancy variables of distinct targets.

The complete exact extension has

```text
nontrivial endpoint groups       257
new occupancy variables         2025
witness-to-occupancy clauses    7764
occupancy AMO clauses          12663
Hall endpoint-pair clauses       171
total added clauses            20598

combined variables              7363
combined clauses               97251.
```

The base clause prefix is byte-semantically unchanged.  The extension is
substantially smaller than the equivalent 220,867 direct witness-pair clauses.

### The slack-one Hall core

The following 18 residual targets are a pairwise-incomparable antichain:

```text
287d,2c6d,346d,546d,562d,56a9,6879,8c62,946d,
a46d,a86d,a879,c671,c879,cc61,d42d,d629,d6b1.
```

Their complete left-endpoint union has only 19 members:

```text
0..4, 6434..6443, 12869..12872.
```

Every completion must give the 18 targets distinct left endpoints, so at
most one of these 19 endpoints can be unused.  For each of the 171 endpoint
pairs, the strengthened CNF adds the positive disjunction of all exact
witness variables whose physical left domain touches the pair.  Clause
lengths range from 36 to 270.  The three minimum clauses correspond to

```text
(4,6443), (4,12872), (6443,12872).
```

## 5. Equisatisfiability proof

Deleting the new variables and clauses maps every extended model to a base
model.

Conversely, take any base model and set each occupancy variable to the OR of
its linked exact witnesses.  If two distinct target occupancies violated an
AMO, there would be true witnesses for distinct equal-rank targets with a
common physical endpoint.  The corresponding intervals are nested, forcing
the two targets to be comparable; equal rank then forces equality, a
contradiction.  Hence every base model extends to the new CNF.

For the 171 positive Hall clauses, select one physical provider for every
target in the displayed antichain.  Common-left-endpoint intervals are
nested, while the targets are incomparable, so the selected endpoints are
distinct.  Eighteen of the 19 endpoints are used, and every endpoint pair is
therefore touched by at least one true exact witness.

Composing this equivalence with the authenticated 245-value normalization
proves that the new CNF is equisatisfiable with the full arbitrary-nonzero
18-cell fibre.

Static right-endpoint Hall matching is feasible at every rank (the rank-eight
case is `21/21`), and the antichain left core has matching `18/18` with slack
one.  Thus this is a conditional propagation strengthening, not a solver-free
UNSAT theorem.

## 6. Authentication

```text
scratch/build_k16_deletep1_collar594_endpoint_hall_cnf_20260731.py
  SHA256 38efa4772b5ce9061876c2e5c7c292d67ad7bb065b1741a15e4f10ac140930ea

scratch/audit_k16_deletep1_collar594_endpoint_hall_cnf_20260731.py
  SHA256 3da984d2cffce8b5dd6182f94cd15f502eafcead4da17527d657c49467ca13ba

scratch/k16_deletep1_collar594_endpoint_hall_20260731/model.cnf
  SHA256 986ab1ed32a424587cc2a2df03d978bfdb8bfc232d1c085606de3c5077aac8c0

scratch/k16_deletep1_collar594_endpoint_hall_20260731/endpoint_hall.map.tsv
  SHA256 ef4b2dd9741fed1b5f9a07e451ca46d75be063baa74838a14987cd0b06e90371

scratch/k16_deletep1_collar594_endpoint_hall_20260731/model.stats.json
  SHA256 dd35699a1b84b95e48a33ec8f64fa98c621de0d9c0380651724b82ec55392778
  payload e649fdc394895c418234061eb9b5282538ccba24faa8e9667be34976332f8755

scratch/k16_deletep1_collar594_endpoint_hall_20260731/hall_core.tsv
  SHA256 cd5a00dd7d6167545395b9171bd46b16040c28674b5c8e9f3d99e26a8c815ff9

scratch/k16_deletep1_collar594_endpoint_hall_20260731/independent.audit.json
  SHA256 b49f630760f8d06ef3d368103712ad59289ecd05eb4bf06934c5d2e584986d35
  payload dbdbe90a0e4aa65e80c651f238f1d198e1d7defb1f38491ad3b5777796da380e

scratch/audit_k16_deletep1_collar594_slack1_left_hall_20260731.py
  SHA256 f3d105f24754d6bd9a46cb29f2b3fc125cf1fd993b6b662e23a1c67ecbce4647

scratch/k16_deletep1_collar594_slack1_left_hall_20260731/audit.json
  SHA256 9d9c36e8582c20f1a471159f72fb5eff1822ca9e824c4514b6d0315276be8a6e
  payload 02dc4d6046b8cfe9639e370f1a071da42dbdbc6996030c9de8d6d840288bbd64
```

No solver was launched on the strengthened CNF.  A previously active
base-CNF CaDiCaL job was later terminated as theorem-redundant after the
independent immutable-`0xc279` audit passed.  That interrupted run is
`UNKNOWN`, not solver-UNSAT; its incomplete proof remains preserved.

## 7. Superseding fixed-fibre theorem

The endpoint extension remains an exact, reusable propagation theorem, but
it is no longer a decision procedure for this 18-cell fibre.  The two fixed
triples `[11726,11728]` and `[12826,12828]` first-deliver `0xc279` at distinct
deadlines and avoid all eighteen editable positions.  Hence every assignment
in this fibre has a ghost extra.  The architecture-free K16 equality
inequality forces `G=0` at length 12,873, so the complete fibre is
solver-free impossible.

The superseding result and independent replay are:

```text
MATH_THEOREM_R_EVEN_CLOSED_SPLICE_THREE_DELETION_AND_18CELL_COLLAR_20260731.md

scratch/audit_k16_c279_two_fibre_ghost_independent_20260731.py
scratch/k16_c279_two_fibre_ghost_independent_20260731.audit.json

scratch/k16_deletep1_collar594_theorem_redundant_termination_20260731/
  termination.audit.json
```

Accordingly, `model.cnf` in Section 6 is frozen as propagation-only and
must not be presented as a solver verdict or restarted as an 18-cell search.

This theorem is only about the fixed delete-p1 raw-splice fibre.  It has no
carrier-Hall consequence and makes no unrestricted K16 claim.
