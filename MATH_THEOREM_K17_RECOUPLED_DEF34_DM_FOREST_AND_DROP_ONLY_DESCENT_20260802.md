# K17 recoupled deficiency-34 DM forest and drop-only descent

**Date:** 2026-08-02  
**Status:** exact static supplier theorem and authenticated drop-only
improvement on the strict-def84 recoupled parent.  This is not an occurrence
state, chronology, residence proof, compiler, K17 word, or proof of
`nu(17)=24313`.

## 1. Authoritative parent

The strict-Pareto `b268` transfer selection was recoupled through the exact
root/common-basis completion.  Its compressed and overlaid tables are

```text
bf5b946f9e1cd5165ba323c894208e9370e7a2b671578ef2a6231535c2ba3241
  compressed.tsv
9dafc568f9b93151822053618fe4574b2b50452e944b7fb98a093c47dda9e2f3
  final.tsv
```

The load-bearing overlaid parent is the SHA-bound file

```text
scratch/k17_b268_common_parent_selector_20260802/
  root_k17_b268_common_parent_selector_def85_019fc35b_20260802/
  out/def84_force_mutable_zero_roots/final.tsv
```

It must **not** be substituted by the later staging file
`/home/amodo/or15/work/def34_release_math_20260802/final.tsv`: that path was
subsequently overwritten, now has SHA `e359e821...`, and differs in 108 rows.
The chain below reconstructs from `bf5b946f...` plus the authenticated
drop-001 selection with edge `32928` restored, yielding `9dafc568...` before
the first drop.

The final table has exact complete `6/9/4` supplier projection

```text
edges          74982
matching       16864/16898
deficiency     34
zero heads     20
Hall shore     51/17
graph FNV64    a3d6b556f77db3fa
```

Every statement below uses this parent.  Results for the earlier recoupling
of a different deficiency-94 transfer selection are sibling evidence only.

## 2. Exact DM-forest decomposition

The alternating Hall shore decomposes into 32 connected components.  Every
component is a bipartite tree.  Twenty components are isolated zero heads.
The remaining twelve components have the following `(heads,suppliers)`
types:

```text
3/2  2/1  2/1  2/1  3/2  2/1
4/2  2/1  2/1  3/1  2/1  4/3
```

Thus thirty components have deficiency one and two have deficiency two,
giving

```text
30*1 + 2*2 = 34.
```

The component and member ledgers have hashes

```text
d5ecd42fde312e7a6aa656466a4d513dbe0af33d9dccf479978d3aed55e5158e
  strict_def34_dm.components.tsv
e3b948447d9ab3c271350982393ad11a73ddeb09c78852e2c45af63af96aa7f5
  strict_def34_dm.members.tsv
1b9b7a4308472cba84d3b171eea73e2d5ced33a0e46c3190557bc2c6154b2bbc
  strict_def34_dm.audit.json
```

This proves that the remaining deficiency is not one opaque 51-by-17 Hall
core.  It is a direct sum of 32 small tree deficits.  In particular, adding
one external supplier to one component can pay one unit, provided the table
change does not create an equal defect elsewhere.

## 3. A genuine drop-only improvement

Old protected transfer edge `32928` has endpoints and payload

```text
LR row       13007: compressed [66638,66782]
LMR row      13925: compressed [66626,70770,70898]
```

In the overlaid table these are respectively

```text
13007: [66626,66638,66782]
13925: [70770,70898].
```

Dropping the transfer therefore does not invent a new row state: it restores
both rows byte-for-byte to the exact recoupled compressed parent.  The
compressed parent already has the exact target partition and the exact
root/common-basis completion.  Hence the drop preserves those two properties.
The endpoints are outside the union of the 7,213 protected ticket rows, so
all protected row bytes also survive.

The restored LR supplier `13007` becomes adjacent to formerly isolated head
`13914`.  Exact maximum matching and Hall replay gives

```text
matching       16865/16898
deficiency     33
zero heads     19
Hall shore     50/17
edges          74985
graph FNV64    c7f210f0df68f832
```

The Hall certificate is a literal one-head peel:

```text
Q_33 = Q_34 - {13914},
B_33 = B_34.
```

The exact evidence is

```text
9e5fcd90a90c4020ce50e18f5df597b2c5c3e51b45c2deef5cf31d32962a24f0
  release32928.table.tsv
d666ca731c6b20f28fec5d35505ecd11b4247ceb9bb7be29053fe681dcb78c56
  release32928.matching.tsv
bd0a4f4974d7fe3561e0d57d89eb44cbeb8e3a98092e141ff86ba7d901e53ccc
  release32928.hall.tsv
651032d331a42a1ca522c96381afe0616ef7baa727f1926b7627ec818731444c
  release32928.projection.audit.json
```

No compensating addition is mathematically required by the target
partition, root completion, or supplier graph.  The overlaid subtype census
changes from 438 to 437 LLR modes, while the chain-length histogram remains
exactly `[0,7395,16915]`.

## 4. Marginal socket neutrality

Repricing the complete fixed table in each declared owner phase gives the
same four marginal socket counts before and after the drop:

```text
(phase0,phase1,both,either) = (3099,2260,1838,3521).
```

The released-table price hashes are

```text
a00a5305cbdfa25429b67e8048052823e15951c55ecacd2afa276c8bacc96d1a
  release32928.dnf.phase0.tsv
8873729fe1bd07bb62101b1f0012e1790675631553f0e8003505a4fadbe5c207
  release32928.dnf.phase1.tsv
7781f58c08679a5ef270ec863ecd46370d482727447ecd99589dd626ce963b37
  release32928.dnf.phase0.audit.txt
86b643821e2c031741f5c63e69349067930535eb05ac3dede1c652868d3c617a
  release32928.dnf.phase1.audit.txt
```

This is exact marginal DNF neutrality.  It is not a claim that one common
occurrence-labelled packing has been transported.

## 5. Why zero activation is not the descent criterion

Dropping selected edge `63200` restores supplier `19283`, which becomes
adjacent to isolated head `6352`; the new supplier is already exposed in the
declared matching.  Nevertheless exact replay remains at deficiency 34:

```text
matching       16864/16898
zero heads     19
Hall shore     52/18
graph FNV64    1a47468943592d2b
```

The old isolated component `{6352}` disappears, but the successor shore
gains heads `{3564,10352}` and supplier `{10617}`.  In other words, the drop
replaces a `1/0` deficient tree by a new `2/1` deficient tree.  The zero count
falls, but the total deficiency does not.

This is an exact counterexample to the cheap rule

```text
activate an isolated head + reach an exposed supplier => strict descent.
```

The head-role swap and all invalidated matching incidences must be charged.

## 6. Correct exact criterion

Let `M` be a maximum matching before a drop or exchange.  In the successor
graph retain every pair of `M` whose head is still active and whose literal
compatibility remains true; call the surviving matching `M°`.  Put

```text
ell   = |M| - |M°|,
alpha = maximum number of augmentations from M° in the successor graph.
```

Then, because the active hard-head census is invariant,

```text
delta_successor = delta_parent + ell - alpha.
```

Therefore strict descent is equivalent to `alpha > ell`.  A final matching
of size `|M|+1` and a final Hall shore of excess `delta_parent-1` are a short
exact certificate.  The DM forest supplies a cheap necessary filter: a
candidate which neither introduces an external supplier into an old
deficient component nor removes a head from it leaves that component's Hall
debt intact.  But only the complete successor matching/Hall replay accounts
for newly born deficient trees such as the `63200` example.

For a one-for-one exchange forced by an external application, this same test
must be applied after the compensating addition.  The addition is safe
exactly when it does not consume the drop's one-unit exchange surplus.

## 7. Zero-transfer comparison

Transfer count is not monotone with supplier quality.  The strict compressed
parent with zero overlays has

```text
matching       16846/16898
deficiency     52
zero heads     43
Hall shore     60/8
edges          74517
graph FNV64    19d242e29ec964a4
```

Thus the selected overlay bank pays 18 supplier units overall even though
at least one individual selected transfer is now harmful and can be dropped.
The right finite problem is subset descent, not all-or-none transfer removal.

Its exact marginal socket tuple is

```text
(phase0,phase1,both,either) = (2687,1898,1422,3163).
```

In particular, the zero-transfer parent fails the required common-positive
floor `both >= 1748` by 326.  This proves that transfer cardinality is free
but the transfer bank itself is not disposable.  Drop-only descent must
retain enough overlays to keep the common socket floor.

The zero-transfer projection hashes are

```text
a2b9b1d21775c6e278e019e306f1c227877bae3a5fc110fc38a6e3140a4bd628
  zero_transfer.projection.audit.json
9e84e7619683006956b6ab2ce035d7bd9717f14032cae7a0ecd369a8d142e4fa
  zero_transfer.matching.tsv
5b243016a55dc339ae2f56f517d08bd53c7fa811af1ef9b45bf1a11e57564dee
  zero_transfer.hall.tsv
2b3fc5f6b8d3a824fad99067981c08e339c7ef2eb566d30dcd52980f7c6293ab
  zero_transfer.dnf.phase0.tsv
0bd651f97d3c083d2cee38b4b68850e25f50a147d0740c8a0e107e225ecb6383
  zero_transfer.dnf.phase1.tsv
d8f440b38f07b2bebcc72aca61ae09b59da3bf2ddd2066ea52d847fbaf170ce2
  zero_transfer.dnf.phase0.audit.txt
40118d4fe91f6c3529e7f2b6f38aa99ac426f757d9961824e6dd2320095a8321
  zero_transfer.dnf.phase1.audit.txt
```

## 8. Scope and next exact target

### Lemma 8.1 (overlay count is not a target-count invariant)

One overlay acts on two parent chains as

```text
[u<q] + [ell<m<r]  ->  [ell<u<q] + [m<r].
```

It preserves both chain roots, both owners, the multiset of chain lengths
`{2,3}`, and the union of occurrence-labelled targets.  Dropping the overlay
is the inverse identity.  Consequently, if the parent table is an exact
target partition, every subset of pairwise row-disjoint overlays is also an
exact target partition.  There is no scalar or target-count equation forcing
exactly 438 overlays.

This lemma does not say that every subset preserves supplier rank or sockets;
the zero-transfer counterexample proves otherwise.

### The six-drop chain

Starting with the strict 438-overlay recoupled table, exact greedy drop-only
descent accepts

```text
32928, 11715, 12615, 32713, 49993, 68076.
```

Every accepted pair of endpoints lies outside the protected 7,213-row union
and is restored byte-for-byte from the same compressed parent.  Fresh
maximum matching, Hall, and full two-phase fixed-table DNF replays give:

| drops | last edge | selected | supplier deficiency | zero | Hall | `(p0,p1,both,either)` |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | - | 438 | 34 | 20 | 51/17 | 3099/2260/1838/3521 |
| 1 | 32928 | 437 | 33 | 19 | 50/17 | 3099/2260/1838/3521 |
| 2 | 11715 | 436 | 32 | 19 | 49/17 | 3098/2259/1837/3520 |
| 3 | 12615 | 435 | 31 | 19 | 46/15 | 3097/2258/1836/3519 |
| 4 | 32713 | 434 | 30 | 19 | 43/13 | 3096/2257/1835/3518 |
| 5 | 49993 | 433 | 29 | 19 | 41/12 | 3095/2256/1834/3517 |
| 6 | 68076 | 432 | 28 | 19 | 37/9 | 3094/2255/1833/3516 |

Thus six supplier units are gained while the common-positive socket bank
loses only five records and remains 85 above the required 1,748 floor.

At the successive pre-drop states the exact improving-drop banks were

```text
def33: 11715 12615 32713 49993 68076 79337 79511 79582
def32:       12615 32713 49993 68076 79337 79511 79582
def31:             32713 49993 68076 79337 79511 79582
def30:                   49993 68076 79337 79511 79582
def29:                         68076 79337 79511 79582
```

The three final alternatives are not further independent of `68076`: after
dropping `68076`, none remains improving.

### The exhaustive deficiency-28 plateau

Let `(Q,B)` be the exact 37/9 Hall shore at the final state.  For each
remaining selected drop, restore its two parent rows and evaluate the fixed
old-shore witness after removing any head made inactive by the drop.  If

```text
|Q'| - |N_successor(Q')| >= 28,
```

Hall's theorem proves immediately that the successor cannot improve.  This
filter is exact as a rejection rule; it makes no assertion about candidates
which lower the old-shore excess.

Of all 432 remaining drops:

* 430 retain old-shore excess at least 28 and are solver-free Hall no-gos;
* only edges `5619` and `63200` lower that fixed witness to 27;
* fresh complete maximum matching replay on each gives matching `16870`,
  deficiency 28, so neither improves.

Hence the endpoint is a complete single-drop plateau in the exact supplier
projection subject to the fixed compressed parent and current selected set.
The two survivor candidates are additional instances of successor birth
debt: repairing the old shore alone is not sufficient.

### Frozen chain hashes

The load-bearing table / selection / projection / outgoing-scan hashes are:

```text
drop001 def33
9e5fcd90a90c4020ce50e18f5df597b2c5c3e51b45c2deef5cf31d32962a24f0 table
bbab0f1dff55b5f36ec23d8bdeb2358c9e301a18a7e4b977ba78b366117d7121 selection
651032d331a42a1ca522c96381afe0616ef7baa727f1926b7627ec818731444c projection
7b5c1bb2ad45a0f42e9644f70ff5d7a695ac2cc21c93576faa8cc878ee3a2770 scan

drop002 def32
4aab8c6d861f354d3349ba199bf5f12995d50bab9540f089f16fee50ac7ac20c table
147eb633b646b21ebb34e54234fe90e93815386581addb77d71e51b0dbfd3b51 selection
1856ec82e12b43c00413554dfafd595d5aff20b5692d4285918b4528e2949d1d projection
d7f877410334cb1ff6c2149858a31c8484679aa8b0b56456d78487e81a426bd2 scan

drop003 def31
0164db1ec7c2851b94c8d30a418b33f000117af8cda09582f38cd1886cf45510 table
50bec1dd02c4ac8cd7e81aebc3936271005371f6ebf0f4064a66098846d23fc9 selection
e4d38ef7c2503e90fac8598e20cb07d49a14138c99c4d1cdfe7b2b923a048fca projection
e93673fbf00424e12f26dcdbce00571921e49aec3d18176f6e15b045394c1d22 scan

drop004 def30
0a6f73c0b91524b5daa2776ce13dcabcf95ba873ef27c7bf7de023f2642c4207 table
eac9668d39c3a330eaa69e0bfa8ec9592d578de4f34612f7f00a2ab296d0d6c9 selection
a7ee0c038896830a681ac56c1cfc37d8a409bc6452a43cd6813fb68af85970f4 projection
3f11966cc2390efb0d119fad7a17762c767edab1d7b436a3b989652ca4597be5 scan

drop005 def29
df408f84f24d593ecdfe55ebe562bc18d63622ffd09ffa52e2ea12bbdbf72924 table
d5ed1265f0bab789acc5eeed9df21536f67d5ce246822ce61e4c501728f8ad03 selection
effca66b6c2862ae924e57c58f4c4d6b6c78939cffb816d50bf5831872c4d141 projection
a3a02b4edb9d5822b215605fb9e49f7402c2bad8dea3e13a461c9cdd7b5c4ffa scan

drop006 def28 plateau
18044fb4f7e4174c483e3cd8f6c4d91b0b9a9aa1a26ef45952312a310e5244c2 table
7c46719dae10194709f2c9928aecf1f4f88410a0cbe07461c21bc2ad7debde04 selection
1397b7362888ab0c20d54a01742a8c1810b1af6915af2b6019228feae9a8d5a1 projection
80f77baf5f20e016216060f2d26c9b9610317fba0e73b13ea864a4291806891c plateau scan
```

The final matching and Hall hashes are respectively

```text
37a7ffa45c2806bf1badfb60de4e5544b2c953e8434f269bf5fa52671bc34e03
8d1393b4af3ff7dd7184bb064fb0a88088e6966fa25f3de95bc76ead40fcfd81
```

and its phase-0/phase-1 DNF ledgers and audits are

```text
2bc327f774f473cdad2c237979ff73b906360435b77f418a003b5f9fe1e48673
df731a0df69913d41a3b114bc943f843191e9a8d0c5e42997cedc36538a171d2
6206161453556f23d1cac83a5e60b3b642995072362f5b1c22ee5ad1e36f0207
7490c6c2bebe6ade23814fe029b2af6e57ee4158a285064d3c2e25bdd84423e5
```

## 9. Scope and next exact target

The authenticated static incumbent is now the 432-overlay deficiency-28
table.  Every accepted drop satisfies all of:

1. exact target partition and root table by restoration to the compressed
   parent;
2. no changed protected row;
3. exact supplier rank increase by a fresh maximum matching/Hall replay;
4. the four fixed-table marginal socket counts remain at least 1,748.

The terminal scan proves no selected drop passes.  This is an exact
radius-one **drop-only** plateau, not a no-go for one-for-one exchanges,
multiple drops, a different choice among the final four alternatives, fresh
root recoupling, or K17 equality.

All finite outputs are under

```text
scratch/def34_release_math_20260802/
/home/amodo/or15/work/def34_release_math_20260802/
```

The second directory is a staging/evidence directory only.  Its unqualified
`final.tsv` is not the authoritative deficiency-34 parent; use the explicit
SHA and path in Section 1.  The SHA-bound drop-001 through drop-006 artifacts
remain the evidence for the descent itself.
