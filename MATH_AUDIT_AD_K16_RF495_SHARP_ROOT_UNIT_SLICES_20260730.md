# AD audit: corrected RF495 sharp-root unit slices

Date: 2026-07-30  
Scope: the frozen seed5/self RF495 `4/9/5` fibre only.

## 1. Namespace correction

The first three columns of
`distinguished_hole_root_atlas.sharp.tsv` are zero-based option offsets in
each target's file order in `residual_maximal_provider_incidence.tsv`.  They
are not the maximal solver's numerically sorted-`Q` identifiers.  The table
now names them explicitly as
`file_option_index_h0`, `file_option_index_h1`, and
`file_option_index_h2`.

Consequently the equality-surviving rows `(68,3,20)` and `(69,3,20)` decode
as follows.

| witness | target | fixed OR | free `Q` | representative | file index | sorted-`Q` id |
|---:|---:|---:|---:|---|---:|---:|
| 673 | `0x18e7` | `0x0000` | `0x30000` | `12871..12872` | 68 | 66 |
| 674 | `0x18e7` | `0x0000` | `0x20000` | `12872..12872` | 69 | 65 |
| 2464 | `0x3de7` | `0x3104` | `0x0000f` | `0..4` | 3 | 9 |
| 4307 | `0x9e20` | `0x0000` | `0x00060` | `6435..6436` | 20 | 14 |

Every row is authenticated against the original map and raw incidence and
survives exact same-`(target,Q)` dominance.  Witness 2464 is the unique
greatest member of its two-row class and dominates witness 2388; the other
three classes are singletons.

Thus the two physical sharp roots are

```text
{673,2464,4307}
{674,2464,4307}.
```

The discarded translation `{668,2392,4327}` / `{664,2392,4327}` came from
reading file offsets as sorted-`Q` ids.  Those roots are compatible but
directly displace 24 and 35 incumbent targets, respectively, and are not
sharp.  No CNF or solve was launched from that translation.

## 2. Exact root and cascade ledger

For either corrected root, integral maximal-core replay gives direct
displacement exactly

```text
{0x1e20,0x1e64,0x1e74,0x39e6,0x9c63}.
```

The equality-face census has 96 retained-incumbent choices and no feasible
base after allowing zero, one, or two further rehosts.  The unique
three-target relaxation is

```text
{0x18e6,0x19e6,0x8000},
```

and it leaves exactly eight feasible retained bases for each root.  Hence the
exact equality-face floor is eight rehosted targets, with union

```text
{0x18e6,0x19e6,0x1e20,0x1e64,0x1e74,0x39e6,0x8000,0x9c63}.
```

This is a root/equality-bank theorem.  It does not itself choose providers
for the eight rehosted targets or complete the word.

The subsequent domain audit closes both roots through total rehost budget
ten.  Across the sixteen root/base pairs at budget eight, every one of the
eight relaxed targets has zero maximal-provider domain.  All 118 possible
one-more-target relaxations at budget nine fail.  At budget ten, every pair
face but one already has a zero domain.  The unique survivor is the
`Q0=0x20000` root with additional relaxed targets
`{0x9b54,0x9b56}`; its domain sizes give exactly 24 joint combinations, and
all 24 fail.  Thus neither sharp root completes with at most ten rehosts.

## 3. Exact CNF slices

Let `F` be the authenticated original RF495 CNF, with 6,369 variables and
205,557 clauses, SHA-256
`2fc9333bc069a60ad85d39a409f35725e1941b66765407cf9b3276ffeff31e7a`.
The two individual slices are exactly

```text
F AND 673 AND 2464 AND 4307,
F AND 674 AND 2464 AND 4307.
```

Their DIMACS files retain every source clause byte-for-byte, change the
header clause count to 205,560, and append only the three displayed positive
units.  Their hashes are respectively

```text
fee4b52ae5bf8def929a58316656e69b5cc1c0472ea061d9ada177c27c557790
e3c52c19ca7dcf8eddaa9aa8bea338ca129a7639037ab045895739bbddb5cd50.
```

The exact union of these branches is

```text
F AND 2464 AND 4307 AND (673 OR 674).
```

This follows by distributivity and needs two positive units plus the binary
clause `673 674 0`.  No at-most-one clause is sound or needed: assignments
realizing both witnesses belong to the union.  The union CNF has SHA-256

```text
7de39a2fb2d3243d35c7cb17abc3be2e8b5614332e62856d74968c50421c6e82.
```

An UNSAT proof for one individual CNF excludes that branch only.  An UNSAT
proof for the union excludes exactly both sharp branches, but not the full
unconditioned RF495 fibre.

## 4. Literal acceptance and execution status

SAT acceptance remains the corrected RF495 gate: materialize 18 nonzero
collar cells into a word of length 12,873 and independently replay all 65,535
nonempty masks as literal contiguous ORs.  A `D^3` middle-row condition is not
permitted.

No equivalent sharp-slice job was found on H100, and no new solve was
launched: the resource audit showed only 0.31% CPU idle, swap fully used, and
many active solver workers.  In view of the exact budget-ten structural
closure, the sharp CNFs are now proof-calibration artifacts only and should
not consume a scarce core.  Computational priority passes to the unrestricted
exact-one 4,900-choice CNF and restrictive-first nonsharp branches.  The
natural `{606,2464,4307}` slice remains only a sound nonsharp calibration.

## 5. Frozen artifacts

The deterministic builder and structurally separate byte/semantic verifier
are

```text
scratch/build_k16_rf495_sharp_hole_root_unit_slices_20260730.py
scratch/audit_k16_rf495_sharp_hole_root_unit_slices_20260730.py
```

The builder audit payload is
`25941733f254a7423aeccfe1428d5b2066c6067010df5570ab1742ac0f8063dc`.
The independent audit reports `PASS` with payload
`65574bfa51ba516a4b8f13c15655997dd3ef3a77b5305bda6301ee8ccfd9bffa`.

The budget-ten closure inputs have hashes

```text
sharp8_nogo.independent.audit.json   a9e32c01601fe8cebb1e40e87b1c5f30963110f78795d26af35eb71df3778903
sharp_pair_blocker.cpp.audit.json    6e37050e6bda8b2bb42a5efe940afe4f87b9dd167162a9d373fd31b7d7e7b5e4
sharp_pair_blocker.candidates.tsv    4a2e612d7417ad289406391daed8486466b36fd21848787790f8da552f095f71
```
