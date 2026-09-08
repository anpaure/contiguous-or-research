# P3 audit: proof-scoped minimum-hitting-set residence masters for `k=17`

Date: 2026-08-02

Status: exact selector-master construction and directly replayed legacy cores.
Every solver verdict in this note is scoped to its explicitly hashed
compact-v3 seed face.  No global `k=17` UNSAT, upper-completeness, source,
compiler, or word claim is made.

## 1. The core-opening theorem

Let `B` be the immutable compact-Horn-v3 body plus a chosen sound residence
blocker bank, with no incumbent freeze-unit tail.  Let `p_f` be the option
selected by an anchor factor on optional facet `f`.  Suppose a directly
DRAT-verified extracted core is

```text
K union { p_f : f in C },   K subset B,   C nonempty.
```

Then `B and AND_{f in C} p_f` is UNSAT.  Equivalently,

```text
B entails OR_{f in C} not p_f.                         (1.1)
```

The exact-one facet rows make (1.1) physical: every `B` model changes at
least one facet in `C`.  Thus a possibly satisfiable expansion must **open at
least one** facet in each certified core.  It is not necessary to open every
facet in a core.

The inherited expander did the latter: it removed every positive option unit
retained by `drat-trim`.  That is sound but deliberately over-expansive.
P3 instead preserves every core as a separate hyperedge, deduplicates equal
edges, removes only strict supersets, and solves the resulting hitting-set
master exactly.

This theorem is portable to a stronger bank only after two checks:

1. the core CNF/core DRAT pair is replayed directly; and
2. every non-option-unit core clause occurs in the new hashed body.

Both checks are fail-closed in the P3 builder/replay pipeline.  A core from a
different anchor becomes a selector row only when every one of its option
units is still the selected, frozen option of the new anchor.  If an option
has already changed, or its facet is already editable through the current
short-run support, that old core is already discharged and adds no new
opening requirement.

`drat-trim -c` yields a sufficient UNSAT core, not automatically an MUS.
Accordingly this note calls the stored rows verified cores.  A future
assumption shrink may be called subset-minimal only after the reduced hard-
unit CNF has its own verified proof and each one-deletion remainder has a
replayed SAT witness.

## 2. Exact selector formulation

For every initially frozen anchor facet introduce `o_f`, where

```text
o_f = 0  forces the anchor option p_f,
o_f = 1  permits the facet to change.
```

The guard is

```text
o_f OR p_f.                                             (2.1)
```

Opening does not force `not p_f`; it only removes the freeze.  For each
unresolved certified core add

```text
OR_{f in C_i} o_f.                                      (2.2)
```

The proof-derived physical clause `OR not p_f` is also appended as redundant
propagation after structural portability has been checked.  An exact Sinz
counter imposes

```text
SUM o_f <= h,                                           (2.3)
```

where `h` is the exact hitting number of the known unresolved cores.  A
disjoint-core packing of size `h` and a hitting witness of size `h` form a
short independently checkable optimality certificate.  Consequently
(2.2)--(2.3) search all minimum-opening masks at once; they do not commit to
one arbitrary hitting witness.

On a verified UNSAT at budget `h`, the next safe expansion is budget `h+1`.
It excludes only the union of faces represented by that anchor, bank, current
support, and budget.  On SAT, the complete CNF assignment must be replayed,
then the physical factor, residence, topology, and voltage decoded
fail-closed before handoff.

## 3. Frozen legacy proof input

Two independently promoted chains contribute 26 cores through round 12:

```text
union609 sizes: 16,4,21,22,13,24,4,77,78,4,91,18,264
union612 sizes: 16,4,21,22,13,24,48,74,4,101,20,12,165
```

The manifest is

```text
scratch/p3_k17_verified_core_manifest_20260802.tsv
```

P3 directly replays every `core.cnf/core.drat` pair.  It does not infer proof
validity from a solver exit or from the old expansion list.  The new builder
then finds all 24,156 distinct non-assumption core clauses in each promoted
body before emitting any learned blocker or selector row.

## 4. C18 residence-1,615 / raw-union694 anchor

Authenticated anchor:

```text
model SHA256  fb8e8aa64e092fdf532c0d166f5b3c413818c327788c75353515e966c991f3ff
factor SHA256 5c8e864807c641109b6f430a21064c219417c912000a0d2c9a8cc6317e67c955
residence     1,615 = 731 length-two + 884 length-three physical runs
upper orbits rank11/rank12 missing = 86/14
```

The raw cumulative bank has 694 serialized rows and SHA256
`d718f3536cce182209782ea2ac3daa312ad26b6357bb8df1969bed746716c542`.
Literal-set and row-set canonicalization removes 76 permutation duplicates,
leaving 618 logical clauses with SHA256
`8ea108a81b6bd741a9544aa439532a13c9131ed4f9ab9d80b606fe36805f0496`.
This is a representation change only; the master is bound to both hashes.

The 95 current blocker rows touch 262 optional facets, leaving 936 guarded
frozen facets.  Relative to this anchor, 11 old cores are prehit by a changed
option and three by initial editable support.  Twelve raw unresolved rows
deduplicate to eight hyperedges.  Their exact hitting number is six:

```text
minimum witness facets = {759,2003,2805,2809,3027,5835}
seed option variables  = {454,3014,4467,4496,5342,12048}
disjoint-core packing  = 6
```

The minimum-budget master has

```text
321,197 variables
1,847,501 clauses
CNF SHA256 96956355da118293bb83bb84a69d21b52c0c1c254370a7b49e4d56b5e10fba7c
```

Remote frozen root:

```text
/home/amodo/or15/work/p3_k17_res1615_c18_union694_minhs_selector_20260802
```

Budget 6 is independently solver-UNSAT under Kissat and CaDiCaL.  The local
`drat-trim` revision prints exact `c trivial UNSAT` and `s VERIFIED` but exits
1 on an input-level contradiction because `sts` remains initialized to
`ERROR` in that source branch.  P3 does **not** accept exit 1 generically.  It
accepts only this exact transcript with no contrary status and reproduces it
using a newly empty proof; all other exit-1 cases fail closed.  The original
Kissat proof is retained.  The same fail-closed replay certifies every budget
from 7 through 16.  Budget 17 reached the enforced 1,800-second Kissat cap and
is recorded only as `UNKNOWN_124`; its retained 944 MB partial DRAT is not a
proof and supports no exclusion.  Thus the certified C18/union694 selector
frontier is exactly `b <= 16`, scoped only to the hashed faces in this root.

## 5. Residence-1,581 / raw-union698 anchor

Authenticated anchor:

```text
model SHA256  178a91fc4979f359448704085a6ae92f41caff9bf8cb23ab5713a4475af98cfe
factor SHA256 14903257c9dd4082ef571a82aefea753a5cda958807d90958f5e43454d2c9497
residence     1,581 = 748 length-two + 833 length-three physical runs
upper orbits rank11/rank12 missing = 86/15
```

The raw union698 bank has SHA256
`c9bad1bd9a4a4069ebfca7edab2a8bdb890b447099c9fb4c30e75b3d7e83ad37`.
Independent set canonicalization maps 698 serialized rows to 622 distinct
logical clauses, SHA256
`524fdc5898a416d721713b4af4a0ff2e7babd94c2e4aa84f124e49b1b9f76a16`.
It contains the canonical union618 bank plus four new logical rows.

The 93 current blockers touch 254 facets, leaving 944 guarded frozen facets.
Eleven legacy cores are prehit by seed changes; none is prehit merely by
current support.  Fifteen unresolved rows deduplicate to ten hyperedges.
Their exact hitting number is eight:

```text
minimum witness facets = {759,863,2003,2287,2805,2809,3027,5835}
disjoint-core packing  = 8
```

The minimum-budget master has

```text
323,139 variables
1,851,387 clauses
CNF SHA256 131472f17711a170f99aea91ccab9c262015c1cf6ab6cd28dfe88a579238d72c
```

Remote frozen root:

```text
/home/amodo/or15/work/p3_k17_res1581_union698_minhs_selector_20260802
```

After the preceding C18/union694 loop terminated, this unchanged master ran
from its exact minimum budget 8.  Budgets 8 through 15 are independently
proof-verified face-scoped UNSAT.  Budget 16 reached the exact 1,800-second
cap with no solver status, checker artifact, or verified manifest and is only
`UNKNOWN_124`; no budget 17 or later face ran.  Thus the certified union698
frontier is exactly `b <= 15` in this root.

The auto-master CNF and its selector/core/audit companions were rebuilt after
replay paths were bound exactly to the manifest and remained byte-identical.
The earlier prebuild manifest retained the pre-path-binding source digest; it
is preserved as `PREBUILD_SHA256SUMS.pre_pathbind_stale_20260802`.  The current
`PREBUILD_SHA256SUMS` has SHA256
`9f8570d6ed691b75cd801c755540224105e0835f5b9f577dcab9a54507201c33`
and directly rechecks the raw bank, canonical bank, normalization audit, and
the exact builder source that produced the frozen auto master.

## 6. Superseding union706 comparison and staged anchor

The next raw bank is union706, SHA256
`549c9aed6dc3306a580129800251f3b47316e29c4a6d777c60d086628d06c14a`.
After both ordered lanes terminated, P3 canonicalized it as literal and row
sets: 706 serialized rows become 630 logical clauses, SHA256
`748c0842315fff0ae03102619668d5e8c2de52243b328ec398a250a9951dd188`.
It then evaluated two authenticated anchors under those identical bytes:

```text
residence-1,547 leader:
  model  fb1c96c33964006ad3eec1f71550a7d033724c3508dbec54c7f3dc8bb9961ef5
  factor 165664c5e27cf1c3e67c387fa8e08e2576bd64ea06c13340c18a16db8de9eee0

balanced residence-1,564 anchor:
  model  35b8f9dd4287c336584ab54b8341e7a3cd1e394086fb0848cb405d6089827c9d
  factor a56ea34a57c05f2993c6999ad2b1f9fde79089dfd8bd94b08e0e4b784329ad7a
  residence 1,564 = 714 length-two + 850 length-three runs
  rank-11/rank-12 orbit deficits 86/14; physical holes 1,462/238
```

Both anchors have 15 raw unresolved legacy cores, ten compressed edges, the
same exact hitting number eight, the same eight-edge disjoint packing, and the
same hitting witness
`{759,863,2003,2287,2805,2809,3027,5835}`.  The requested proof metrics are
therefore tied.  P3 stages balanced residence-1,564 as the deterministic
schedule tie-break: it has 947 rather than 951 guarded selectors and its
master is 36 variables and 72 clauses smaller, while its authenticated upper
deficits are better.  This is not semantic dominance: residence-1,547 is 17
lower, the faces have different initial support, and any future verdict is
scoped to only the chosen hashed face.

```text
balanced union706 minimum master:
  variables/clauses 323,166 / 1,851,449
  CNF SHA256         646bf2e262aaaff6636059fe619b991320788582a4fa6148c825d83ced29af7f
  scope              res1564_union706_raw_canonical_set630, selector budget 8

comparison root:
  /home/amodo/or15/work/p3_k17_union706_anchor_comparison_20260802

staged winner root:
  /home/amodo/or15/work/p3_k17_res1564_union706_minhs_selector_20260802
```

The earlier raw-union701 request is retained as provenance only and is not an
active construction target.  No union706 SAT solver has been launched.

## 7. Scope boundary

The compact-v3 body is exact for positive depth-three residence only on its
exact lower-facet/owner-degree-two face.  It does not encode quotient or
physical connectivity, nonzero voltage, ranks 11--17, source binding, the
lower compiler, or a literal contiguous-OR word.  Therefore:

* a verified selector-master UNSAT excludes only the stated hashed face and
  opening budget;
* a SAT assignment is only a candidate until complete CNF replay and physical
  residence/topology/voltage decoding pass; and
* neither result changes the certified global `k=17` bounds by itself.
