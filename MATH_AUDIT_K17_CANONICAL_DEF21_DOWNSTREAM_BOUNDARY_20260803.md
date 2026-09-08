# K17 canonical deficiency-21 parent: downstream-gate boundary and transparent-mode tickets

**Date:** 2026-08-03  
**Status:** exact static-chain-factor and parent-local transparency audit.  This
note does **not** claim a physical chronology, residence, upper coverage,
common-cap compilation, a length-24313 word, or `nu(17)=B(17)`.

## 1. Authoritative input

All computations read the frozen H100 producer

```text
/home/amodo/or15/work/k17_drop12_canonical_consumer_catalogue_20260803
```

and write only to the separate audit root

```text
/home/amodo/or15/work/root_k17_def21_downstream_audit_20260803
```

The relevant input hashes are

```text
compressed chain table  e878bf19654d8478b4552451a3b5c9a54716e1383d2513c59d680091e10b5ffb
final ten-mode table     fa49188250bf194c8218d8afb5bf5f9220e4a73fd1267824bc7ed0b2868bbb7c
owner phase 0            b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
owner phase 1            736fc30c014c7b535f036348380ed46f545c1ef9bf1e409f515660fff2229058
supplier Hall ledger     1836380f40fae8bd67927e293930b293203df4f05ea67d699a2d10cde6771f08
structural catalogue     790fae940cd80c05e35656027dcb57139180b54c77f567c9b5333ab5d4581434
pin-disjoint common bank a687337fb4bd00527c0bdc8d472e5338663c76f8d7757c7f11ddb47f090eef37
materialization audit    787e3d3f92f321c89ef75e0e92bdbe9cb284051595c2145c68f2d2118e56f6d2
occurrence audit         2be9f9cdf671a683d217ac9cf8fda49313fd85d751e2408bfca4e2c9c8c95783
DNF intersection audit   3948555eb617676ceefbf72401d99734cf03bb7792fd44900ba2c5f6bf94b65f
supplier replay          25926071dfa2c2873c90a24c05c579bd384d1e33bbd62ac87c2b80f7e796f278
```

The complete supplier projection remains

```text
edges 74935; matching 16877/16898; deficiency 21;
19 zero heads; maximum Hall shore 23 heads / 2 suppliers.
```

## 2. What the canonical table actually is

The table is a complete **static lower-ideal chain factor**, not an ordered
middle-layer carrier.

An independent C++ replay proves:

* the 24,310 rows have contiguous IDs;
* their owner masks are precisely the 24,310 distinct rank-nine subsets;
* their roots are precisely the 24,310 distinct rank-eight subsets;
* each root is contained in its owner and is the last target of the row;
* every row is a strict inclusion chain of length two or three;
* there are 7,395 length-two rows and 16,915 length-three rows;
* the target multiset has 65,535 occurrences and 65,535 distinct masks;
* its rank histogram is

```text
rank 1:    17      rank 2:   136      rank 3:   680      rank 4:  2380
rank 5:  6188      rank 6: 12376      rank 7: 19448      rank 8: 24310.
```

Thus every nonempty target of rank at most eight occurs exactly once, in a
chain assigned to a containing rank-nine owner.  This is an exact ideal
chain assignment at depth three.

The ten final LLR transfers change 20 target lists relative to the compressed
parent, but change **zero** owner masks and **zero** root masks.  The target
partition and the 7,395/16,915 length histogram remain exact.

## 3. No physical owner graph is bound by this package

The canonical authority contains no global owner-edge, successor,
predecessor, component, opening, or cut ledger.  Neither `chain_id` nor equal
row IDs between the two owner-phase tables is declared to be such a ledger.

Two fail-closed diagnostics independently show why neither convention may be
invented.

1. In `chain_id` order only 5,876 of the 24,309 consecutive owner pairs are
   Johnson adjacent.  Hence this row order is not a middle-layer path.
2. Pairing phase-0 and phase-1 owners by equal row ID gives 12,051 degenerate
   equal-owner pairs, only 12,259 Johnson pairs, only 10,661 distinct rank-ten
   unions out of 19,448, and a permutation with 12,057 cycle components.  Its
   component-size census is

```text
12051 components of size 1; two of size 3; and one each of
sizes 394, 2033, 3080, and 6746.
```

This second object is a useful diagnostic union of two incidence matchings;
it is not the missing physical carrier.

Consequently the following quantities are **undefined**, not merely bad:

* path/component topology and opening endpoints;
* coordinate run lengths and residence defects;
* the immediate upper palette of adjacent owners;
* arbitrary-width interval-union coverage.

They remain undefined even if the current supplier deficiency later reaches
zero, unless an owner chronology/edge ledger is supplied separately.

## 4. Exact transparent action of an LLR mode

A canonical structural mode takes two rows

```text
host  LR:  {u,q}
donor LMR: {l,m,r},     with l strictly contained in u,
```

and replaces them by

```text
host  LLR: {l,u,q}
donor MR:  {m,r}.
```

### Transparency lemma

Every such mode preserves:

1. every row owner and root;
2. the global target multiset;
3. the number of length-two and length-three rows;
4. strict chain containment and target-to-owner containment.

It changes only the assignment of the one lower target `l`: `l` moves from
the donor owner to the host owner.

The proof is literal from the displayed transformation.  The old and new
two-row target multisets are both `{l,m,r,u,q}`.  The catalogue conditions
give `l subset u subset q` and `l subset m subset r`, while each root remains
inside its unchanged owner.  One row changes `2 -> 3` and the other `3 -> 2`.

Therefore any row-disjoint simultaneous LLR selection is transparent to
every future gate depending only on the owner/root state.  It cannot repair
or damage a separately supplied owner chronology, residence trace, or upper
deck.  It **can** change the lower compiler because it moves named target
`l` between owner slots; that move must remain occurrence-labelled.

## 5. Frozen downstream-transparency ticket bank

The audit emits one record for every pin-disjoint exact-common mode.  Each
record contains

* endpoint and state IDs;
* phase-specific predecessor/successor occurrence rows;
* the coalesced physical row set and its size;
* the moved target, its rank, source owner, and destination owner;
* old and new endpoint chains;
* static-transparency flags;
* current Hall-head, zero-head, and supplier-neighbor touch flags.

The census is

```text
pin-disjoint exact-common modes          3494
strict identical phase tuple             2813
coalesced row cost 2 / 3 / 4       2813 / 666 / 15
moved target rank 1 / 2 / 3 / 4 / 5
                         1198 / 585 / 451 / 852 / 408
```

All 3,494 records pass the four static transparency checks.  Eleven use an
endpoint changed by the fixed ten-mode overlay and are not additional modes
on that literal final table.  The fixed-final helper census is

```text
applicable exact-common helpers           3483
strict 2-row helpers                       2807
coalesced row cost 2 / 3 / 4       2807 / 662 / 14.
```

The ledger SHA is

```text
051f119e82ac99f9bc3d9b729e812948adf7a9dea021b01a1414a52b7e8749c2
```

## 6. Cheap exact filter from the current Hall shore

Among all 3,494 pin-disjoint exact-common modes:

* no endpoint is one of the current 23 Hall heads;
* no endpoint is one of the 19 zero heads;
* no phase predecessor/successor row is a current Hall or zero head;
* 3,493 avoid both current supplier rows `12973` and `14851`;
* the sole exception is strict mode `52847`, whose LR endpoint is current
  supplier row `14851`.

The shore itself is 19 isolated zero heads together with the two incidence
paths

```text
13148 -- 12973 -- 12948
15103 -- 14851 -- 1490.
```

The middle vertices are the two physical supplier identities.  Edge 52847
destroys both incidence edges carried by row 14851, which costs one distinct
supplier credit.

Hence, on the fixed canonical parent and fixed root action set, a one-mode
child from this bank cannot improve deficiency by retiring or changing a
current Hall-shore head.  To reach deficiency 20 it must create at least one
new distinct supplier for that shore.  Exact one-mode accounting for mode
52847 loses the present service from row 14851, so it must create at least
two new identities: one replacement and one net gain.  Exact endpoint
incidence replay proves that none of the 3,483 incumbent-disjoint literal
common modes creates any new shore supplier.  Ordinary common modes therefore
have credit zero, while edge 52847 has credit minus one.  Every common
singleton is rejected by this Hall shore.

This is only a necessary filter.  Supplier credit is by physical row
identity, and every surviving candidate still requires simultaneous
materialization plus a complete supplier replay.

For multiple modes the exact cheap prefilter is:

1. distinct endpoint rows;
2. joint capacity of all coalesced phase witness rows together with the fixed
   23-row occurrence union;
3. no protected-row collision;
4. exact common declared state per mode;
5. preservation of at least one net new distinct neighbor of the current
   23-head shore after charging every lost row (or an explicitly broader root
   rematerialization that changes a shore head).

The 3,483 records left after 11 incumbent-endpoint conflicts, including the
strict 2-row records, form an exact individually-common helper/control face.
They are **not** the complete pair domain.  The current structural supplier
screen has 468 exact deficiency-20 one-mode sources, and every one has
`raw_common_state=0` even after admitting its new LLR host as an occurrence
witness.  Thus none is an occurrence-common singleton, but a second mode can
create a new long state and thereby create a common state for the source.
The complete pair lane must contain at least one of those 468 structural
source modes and enumerate a second structural mode capable of mutual
occurrence support.  Restricting both coordinates to the 3,483 helper records
would exclude every known supplier-improving source.

The exact score, occurrence-result, and occurrence-audit SHAs are

```text
84a4475d2d3d445ff8acc827cbf22ce56b539294208ab482ebe4e8e6f4308cb7
21ab1c4f987c54d835306394c86a7aef0b96ead2caeaf31153b9513889a91050
8997ff1d63ba7fe9607f148d79a06c9f554a0461f055642f8769af9f6bc98acc.
```

The resource-disjoint common/common face is also exactly dead:

```text
credit  0       5,219,031 pairs
credit -1           2,287 pairs
positive credit         0 pairs
total            5,221,318 pairs
```

The minus-one rows are exactly the compatible pairs containing edge 52847.
No common/common pair moves a shore head or creates a new shore supplier, so
none can satisfy the target-20 cut.  This face should be skipped/frozen, not
submitted to the supplier solver.

The independent Hall-geometry package is frozen under

```text
/home/amodo/or15/work/k17_def21_hall_geometry_20260803
```

with manifest SHA
`a1cb60e9e91b8acc9814e48671de39d8af168b32227e0d368ac506484f8e47b0`;
its common-mode effect ledger and pair audit have SHAs
`f528ed3a5e593a955328d167a2a0ca619ad88501e5f431d41da789361ff04a68`
and `d8759707dd51263959aa12b2756320047ef51ec096d0736bfb5b0ea324725fb9`.

The exact singleton obstruction is at the state-key level, not merely at the
selected-witness level: native-phase-0 and transported-phase-1 supported key
sets are disjoint for all 468 sources.  Alternative physical witnesses inside
one key therefore cannot repair a singleton.  This fact does not transport to
a pair, because both key supports must be rebuilt after the two modes are
materialized together.

There is no preliminary row-capacity scarcity.  Pair each of the 468 sources
with the 3,483 fixed-final common helpers and reject a helper whenever either
source endpoint occurs among its two endpoints or four selected phase-witness
rows.  Every source retains

```text
2802..2807 strict 2-row helpers,
3477..3483 total common helpers.
```

There are 1,313,339 strict ordered seeds and 1,629,622 total ordered seeds;
no source has zero helpers.  The exact count ledger and transcript have SHAs

```text
pair_helper_counts.tsv        a36111f198176bd64b084060119f275fcb7a9955cd9e7cf869cdc819d33e29c0
pair_helper_counts.audit.txt  4baae119b15ce0d3fef4c4aba863c992844ba95271b8944b023a141558c650d6.
```

These are resource-safe seeds, not occurrence-positive pairs.  The exact
changed-long-state rescue predicate is the following.  For mode `e`, let
`h_e` be its old LR host and `d_e` its old LMR donor.  After selecting
`{e,f}`, in phase `p` form `B^p(e,f)` by removing both donor long states and
installing all four flag states of both new LLR hosts.  For the new MR short
of `e` and state `k=(q,alpha,beta)`, let `W^p_e(f,k)` be the literal
predecessor/successor pairs in `B^p(e,f)` satisfying the exact incoming,
outgoing, five-cell, and same-row flag predicates.  Define

```text
C_e(f) iff some k has one tuple in W^0_e(f,k) and one in W^1_e(f,k)
             whose shared physical rows receive equal flags.
```

A pair is occurrence-valid exactly when `C_e(f)` and `C_f(e)` hold with one
joint row-capacity/flag assignment.  Since every deficiency-20 source has no
common state alone, every witness of `C_e(f)` must use the newly installed
helper host `h_f` in at least one phase; deleting `d_f` cannot create a state.
This is the exact directed rescue arc `f -> e`.  A pair is consequently a
mutual rescue, or a one-way rescue in which `f` retains a pre-certified common
ticket avoiding both source endpoints.  The 3,483 common helpers are a useful
sufficient face, but the complete incidence search must allow every
fixed-final-applicable structural helper because two individually noncommon
modes may rescue one another.

## 7. Compiler and common-cap boundary

Three different objects must not be conflated.

1. The chain table is an exact ideal assignment of all 65,535 lower targets
   to nested owner slots.
2. The 29,256/29,256 augmented residual b-matching certifies the frozen outer
   representation used to materialize this table.
3. The 16,877/16,898 supplier matching is a necessary complete 6/9/4
   row-pair projection.

None is a target-to-physical-interval-cell common-cap matching.  The package
contains no global physical cell ledger and no common-cap incidence graph.
The 10+10 phase tickets and their 23-row union certify only the fixed local
occurrence face.  Thus the full compiler remains undefined, not deficiency
21.  Supplier zero would close one necessary projection but would not by
itself prove a compiler or a word.

## 8. Gate ledger

The machine-readable gate ledger is

```text
scratch/audit_k17_def21_downstream_20260803/downstream_gate_status.tsv
```

with SHA

```text
c79f0c85099442af4f1fdddc5f1c28e045818d7a40096cd6585e4e8cccb91ef3
```

The static audit and its source have SHAs

```text
static_chain_factor.audit.tsv   fd29ebe9a55f46012ca713fa18b1a26834f0df9514b35dc1cc4b8159d565b995
audit_static_chain_factor.cpp   4ea935f1b1d6a2bb4b1d5b70c76ea393e8dd696d5cd2dabfaed6b9313cdbe9a5
```

The transparency-ticket generator has SHA

```text
f6157146c4e0f3450a46d53187533df71a682adb06bf772da7e4bf29690c6a8d
```

and its compact census transcript has SHA

```text
59aa17ce12541ada6ceccb4eec0ff3216bed6c4cb1b1df6793a5cb6b8e1b83c7.
```

## 9. Proof-safe conclusion

The canonical deficiency-21 parent already solves the static lower-chain
partition exactly, and every active LLR mode preserves that achievement and
the complete owner/root state.  The next descent target is supplier
deficiency 20 (with deficiency zero still the ultimate supplier goal).  The
individually-common singleton and common/common pair faces cannot deliver
that first step: their Hall credit is never positive.  The live pair lane is
therefore a 468-source/occurrence-helper search with exact mutual-state and
joint-capacity semantics.

No component, opening, residence, immediate-upper, deep-upper, or common-cap
claim is available from this package.  Those gates require an independently
bound physical owner chronology and physical interval-cell incidence after
the supplier stage.
