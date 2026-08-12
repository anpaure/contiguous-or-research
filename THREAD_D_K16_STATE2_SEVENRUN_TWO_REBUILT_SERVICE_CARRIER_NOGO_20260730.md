# Thread D: the state2 seven-run two-service class has no exact carrier

Date: 2026-07-30

Status: exact scoped no-go, with a structural reduction and an independently
replayed finite census.  The complete one-new-split, seven-full-run class
above the seven sharp deficiency-one roots contains 904 chronologies with
`G=0` and complete arbitrary-width upper coverage, but none passes the exact
capacity-plus-envelope carrier gate.  Hence no member reaches the static
lower atlas or generalized COMP3.  The K16 bracket remains

```text
12873 <= nu(16) <= 12874.
```

The initially reported 80,640-row menu omitted the exceptional root-3 split
`w=6387`.  That count and its first production result are superseded.  The
correct menu has 81,600 rows and is the only result stated as final here.

## 1. Frozen source, roots, and exact class

Let `Q=(Q_0,...,Q_12872)` be the rank-eight target chronology

```text
scratch/k16_resident_state2_upper2_targets.txt
SHA-256 77dd098d7e066cd81ed68846d554c5e5a7247e90ec764033394287f312c28464.
```

The seven roots are the rows of

```text
scratch/threadD_k16_state2_secondbridge_sixcut_20260730/def1.final.audit.json
SHA-256 fca25ab94da72f4728ee7c80ab6a631a2ce7098daefa0b76a59182c5e48c8db1.
```

Each root is a permutation of the source positions with six full maximal
signed source runs and one missing upper-q1 colour.  It has already rebuilt
two other q1 colours by two occurrence-labelled directed seams.

For a root `rho`, let `E_rho` be its five broken source edges.  The class in
this note is defined as follows.

1. Choose one further edge `w notin E_rho` and split the source path at
   `E_rho union {w}` into seven source atoms.
2. Arbitrarily order and orient those atoms, while retaining the root's two
   exact directed q1-repair occurrences.
3. Retain only words having exactly seven full maximal signed source runs.
   Thus no conceptual cut may be restored and no word with at most six runs
   has a duplicate representation.

These three items define the topology class.  The census then tests, in
order, literal `G=0`, complete upper interval-OR coverage, the exact
capacity-plus-envelope carrier gate, and (only when that gate passes) the
static lower-host condition.

Only the two q1 occurrences are frozen in this broad class.  The old
depth-labelled A/G/R collars may be rebuilt elsewhere; imposing those old
collars gives a strict subclass discussed in Section 7.

If `c_e=Q_e union Q_(e+1)` and `J(P)` is the set of six output seams, the
exact q1 count in a reassembly `P` is

```text
n_P(T) = n_Q(T)
         - sum_(e in E_rho union {w}) [c_e=T]
         + sum_((i,j) in J(P)) [Q_i union Q_j=T].       (1.1)
```

A rank-nine target is the union of a nontrivial consecutive middle interval
if and only if it is the union of one adjacent distinct rank-eight pair.
Consequently positivity of (1.1) for every rank-nine target is necessary and
sufficient; this is not a bounded-width proxy.

## 2. Structural four-root no-go

The source multiset has exactly three duplicated values, on source edges

```text
6432, 12869, 12871.
```

Exact `G=0` requires the two occurrences of each duplicated value to be
adjacent.  Roots 0,2,4,6 cut edge 6432, and one of their two frozen repair
seams consumes occurrence `Q_6432`.  Unless `w=6431`, its other neighbour is
the internal source neighbour `Q_6431`, so `Q_6433` cannot be adjacent.  If
`w=6431`, adjoining `Q_6433` to the now-singleton `Q_6432` restores source
edge 6432 in one orientation or the other.  The two atoms merge and the word
has at most six maximal runs.

### Lemma 2.1 (flat-split obstruction)

Roots 0,2,4,6 have no seven-full-run child preserving their two directed
repair occurrences and satisfying `G=0`.

The same argument allows every new split on a source flat to be discarded.
This is a structural theorem, not a census observation.

## 3. Exact q1 support, including the exceptional collar split

Only roots 1,3,5 remain.  To repair a sole q1 hole, two of its rank-eight
facets must be exposed at atom boundaries.

For roots 1 and 5, joining the two already exposed native facets restores an
old source cut and violates seven-run maximality.  Their exact alternate-
facet cut supports are

```text
A_1 = {616,617,1208,1209,1456,1457,1630,1631,
       2097,2098,4992,4993,5009,5010},

A_5 = {1711,1712,2323,2324,4309,4310,4377,4378,
       4503,4504,5460,5461,5969,5970}.
```

Root 3 has sole hole `0xc679`.  Its old facet `Q_6388` normally has internal
predecessor `Q_6387` and fixed outgoing repair `Q_6388->Q_5627`, so neither
incidence is free.  Cutting `w=6387` is a genuine additional topology: it
makes `Q_6388` a singleton, allowing

```text
Q_12827 -> Q_6388 -> Q_5627.                            (3.1)
```

The first seam repairs `0xc679`, while the second is the frozen repair.  This
is not a restored cut.  Together with alternate-facet cuts, the exact root-3
support is

```text
A_3 = {6387,6433,6434,7196,7197,9717,9718,10032,10033,
       10523,10524,11032,11033,11725,11726}.
```

Cut `w=12827` is ineffective: `Q_12827` was already exposed, splitting its
outgoing edge does not free the incoming side of `Q_6388`, and `Q_12828` is
not a `0xc679` facet.  The old-facet incident edges are thereby exhausted.

For each of the 42 ordinary supports, the two repairs form one directed
three-atom chain.  Contraction leaves five macro-objects and four free
orientations, hence `5!*2^4=1920` raw descriptors.  At exceptional
`(rho,w)=(3,6387)`, the repairs become two directed two-atom chains;
contraction leaves five macro-objects but only three free orientations,
hence `5!*2^3=960` descriptors.  Therefore the exact raw menu is

```text
42*1920 + 960 = 81600.                                  (3.2)
```

Equation (3.1) is forced on every q1 survivor of the exceptional fibre, so
only `4!*2^2=96` of its raw descriptors can survive q1.

Maximal signed-run endpoints recover the six source cuts, order, and signs.
The three anchored root families are disjoint.  Thus maximal-run
normalization is injective and does not count restored duplicate cuts.

## 4. Exact carrier criterion

Let `T` be a `G=0` chronology and let `d_i` be its remaining delivery depth,
starting at three and decreasing at each flat.  Define the coordinatewise
maximal envelope

```text
E_j = intersection { T_i : i <= j <= i+d_i }.          (4.1)
```

Any physical source chronology `A` satisfying `D^3 A=T` must have
`A_j subseteq E_j`.  Conversely, the maximal choice `A_j=E_j` realizes `T`
exactly if and only if

```text
0 <= i+d_i <= 12872                                    (4.2)
```

for every `i`, every `E_j` is nonempty, and

```text
T_i = union_(j=i)^(i+d_i) E_j                           (4.3)
```

for every row `i`.  Hence (4.1)--(4.3) are an exact `D^3`-realization test,
not a
relaxation.  Complete lower coverage additionally needs the proved scalar
capacity bound

```text
sum_i d_i >= 26332.                                     (4.4)
```

The production field `carrier` means the conjunction of the exact
realization test (4.1)--(4.3) and the necessary scalar gate (4.4).  It is a
necessary interface for complete lower coverage, not by itself a sufficient
static-host or COMP3 theorem.  Rows counted only by `capacity` satisfy (4.4)
but need not reconstruct.

Upper coverage is also evaluated exactly.  For every start, accumulated
unions are advanced through every strict OR change until `0xffff`; this
enumerates all interval widths because at most sixteen new coordinates can
enter.

## 5. Corrected census

The final exact counts are

| gate | root 1 | root 3 | root 5 | total |
|---|---:|---:|---:|---:|
| raw descriptors | 26,880 | 27,840 | 26,880 | 81,600 |
| maximal/canonical seven-run | 21,840 | 22,452 | 21,840 | 66,132 |
| has a seam for the root hole | 4,032 | 2,784 | 4,224 | 11,040 |
| exact q1 and `G=0` | 2,496 | 312 | 2,136 | 4,944 |
| scalar capacity (4.4) | 736 | 94 | 606 | 1,436 |
| complete arbitrary-width upper | 400 | 0 | 504 | 904 |
| exact carrier gate (4.1)--(4.4) | 0 | 0 | 0 | 0 |

Exactly 344 rows are simultaneously full-upper and scalar-capable: 148 from
root 1 and 196 from root 5.  None reconstructs its maximal envelope.  Thus
the obstruction is neither q1, `G=0`, upper coverage, nor scalar capacity;
it is the simultaneous chronology/envelope condition.

The exceptional `w=6387` fibre contributes

```text
960 raw -> 612 maximal -> 96 q1/G0 -> 24 capacity
        -> 0 full-upper -> 0 exact carrier.             (5.1)
```

### Theorem 5.1 (seven-run two-service carrier no-go)

No member of the class in Section 1 simultaneously has `G=0`, complete
upper coverage, and an exact lower carrier.  In particular no member has a
zero-free static lower atlas, and no generalized-COMP3 or literal-word solve
is warranted.

#### Proof

Lemma 2.1 removes four roots.  The facet inventory and occupied-port
argument of Section 3 are lossless q1 reductions for the other three roots,
including the exceptional split (3.1).  Component contraction enumerates
the exact 81,600-row menu, and maximal-run endpoints make its retained rows
injective.  Equation (1.1) is the exact q1 decision.  Literal replay gives
the counts in Section 5.  Equations (4.1)--(4.3) are exact for `D^3`
realization, and (4.4) is the additional necessary scalar lower-capacity
gate.  No row passes their conjunction, so none can reach the static lower
atlas.  \(\square\)

## 6. Independent correction replay

The corrected production result is

```text
scratch/threadD_k16_state2_sevenrun_2f59b19f_h100/result.json
SHA-256 b83a3dab0f46db60a059d4c4f7de0b51a68ec8e637c4740ff901aedcd86bdc2c,

scratch/threadD_k16_state2_sevenrun_2f59b19f_h100/output/q1_survivors.tsv
SHA-256 07f99de266e9377faf559a9a7699e9ef8093a38862e056af1d299f77076d5bd8.
```

A structurally separate Python audit had already regenerated and literally
replayed the original 80,640-row subcatalogue.  The final incremental audit
then independently generated all 960 exceptional descriptors, proved the
exact set identity

```text
final q1 set = old q1 set disjoint-union exceptional q1 set,
4944 = 4848 + 96,                                       (6.1)
```

and literally replayed every exceptional row.  It also recomputed the final
gate sums and the 344-row upper/capacity intersection.  Its verdict is

```text
scratch/threadD_k16_state2_sevenrun_incremental_dafe7661_h100/
  incremental.audit.json
SHA-256 0b1b78c9859dbf43679bb828b0b6edac9c9d83d5d99576e4babe1667f12d29fd,
payload 214f4922b715f060b662bbff0ce76d3854c42f415949ad48d93c5cbb272320d0,
status PASS_EXACT_INCREMENTAL_CORRECTION_REPLAY.
```

The final C++ production run used one H100 CPU, 7.12 CPU seconds, 21.57
seconds wall, and 4,096 KiB maximum RSS under a 512 MiB cap.  It exited one,
the documented exact no-candidate status.  The incremental independent run
used one H100 CPU, 4.14 CPU seconds, 12.74 seconds wall, and 34,376 KiB RSS
under a 256 MiB cap; it exited zero.

The superseded 80,640-row production directory is retained only to bind the
old independent certificate used in (6.1).  Its deferred-upper status must
not be cited as the final theorem.

## 7. Strict protected-collar corollary

If the old depth-labelled A/G/R collars are additionally frozen, the class
collapses further.  The newly admitted root-3 `w=6387` q1 rows force the
reversed tail atom immediately before `Q_6388->Q_5627`; their two tail flats
therefore occur before the G atom and give G delivery depth one, not three.
They all fail phase.  The only phase-compatible row remains root 5 with
`w=5969`; it is q1-complete and `G=0` but misses upper rank-11 target
`0x6f79`.  An independent boundary replay also finds that all 96 exceptional
rows miss `0x4f5b`, with 72 additionally missing `0x6f79`.  The corrected
strict-subclass audit is

```text
scratch/threadD_k16_state2_sevenrun_service_inventory_20260730.audit.json
SHA 348446e855caea8a8056c392703deecf37ced1178479db8b0b00403ac832d13a,
payload 38687a2471fba48dd9ac6b4efe34d90fd057bd6df240724d8c205edf7dd4c637.
```

This strict-subclass obstruction is not used in Theorem 5.1.

## 8. Sharp remaining topology gate

The result closes exactly one additional source split while retaining the
two advertised q1 occurrences.  A genuinely new state2 escape must do at
least one of the following:

1. move or rebuild one of those two q1 occurrences rather than freezing it;
2. use two further source splits, hence an eight-or-more-run normal form;
3. use a non-source atom/value edit or a different root family.

The existence of 904 full-upper rows shows that adding upper-shadow seams is
not the next bottleneck.  A useful larger topology must preserve the exact
envelope reconstruction (4.3) while routing its services.

## 9. Frozen artifacts

```text
scratch/threadD_k16_state2_sevenrun_topology_lemma_20260730.md
  SHA 9765fb2c23493d4a8da3510e119f88e6c135bdb7890ed4a278376aab9383d8c2

scratch/threadD_k16_state2_sevenrun_two_service_census_20260730.cpp
  SHA 2f59b19f8ee52e54db6adc15d530bf00ad55e56ba92e22234076057d378fa9d7

scratch/threadD_k16_state2_sevenrun_2f59b19f_h100/result.json
  SHA b83a3dab0f46db60a059d4c4f7de0b51a68ec8e637c4740ff901aedcd86bdc2c

scratch/threadD_k16_state2_sevenrun_2f59b19f_h100/output/q1_survivors.tsv
  SHA 07f99de266e9377faf559a9a7699e9ef8093a38862e056af1d299f77076d5bd8

scratch/audit_threadD_k16_state2_sevenrun_w6387_incremental_20260730.py
  SHA dafe7661b97fe8e0f6eb4b50c54fe3729f71ec42efec3ef9040c914b86e991a8

scratch/threadD_k16_state2_sevenrun_incremental_dafe7661_h100/
  incremental.audit.json
  SHA 0b1b78c9859dbf43679bb828b0b6edac9c9d83d5d99576e4babe1667f12d29fd
  payload 214f4922b715f060b662bbff0ce76d3854c42f415949ad48d93c5cbb272320d0

scratch/threadD_k16_state2_root3_boundary_support_20260730.audit.json
  SHA 385598259943815903550522674c4ae6e534bab7e35ab251d391d1a373b3d964
  payload 73dbdf36039a046692a3264032534688f508bd4a17dc4479f5a3e1a5a33374ea
```
