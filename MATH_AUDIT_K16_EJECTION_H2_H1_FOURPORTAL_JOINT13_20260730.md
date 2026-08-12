# Audit: K16 ejection H2/H1 frontier and the four-portal joint13 fibre

Date: 2026-07-30

## Verdict summary

The authenticated ejection frontier is reproduced exactly.

- The H2 word has length 12873 and exactly the holes `0x4879,0x6879`.
- Its one-cell transition at position 0 gives the H1 word with sole hole
  `0x2c6d`.
- The H1 provider atlas has four and only four minimum-debt position fibres,
  totalling 153 assignments.  Every one leaves exactly two holes.
- A newly frozen H100 rerun exhausts the 284 H2 provider-first intermediates
  with at most seven holes and finds no completing second substitution.
- The independently frozen non-provider joint-support theorem closes every
  two-edit completion whose two final endpoint assignments both fail to
  provide an original H2 hole.  Combining the results leaves only a
  provider-first excursion through at least eight holes.
- The 13-cell union of the four literal witness hulls has an exact
  arbitrary-nonzero-value CNF, independently reconstructed clause for clause.
  A smaller occupancy projection is independently proved equisatisfiable.

The two CNF solver runs and their final disposition are recorded in the
dedicated solver section below.  Every negative conclusion is restricted to
its named rooted state or frozen-complement fibre.  Nothing here proves an
unrestricted length-12873 or K16 no-go.

## Authenticated states

| state | SHA-256 | exact holes |
|---|---|---|
| `scratch/k16_ejection_lns_h2_p110_20260730.word` | `5234b77101ac1f22ec1802b4e1f5eccb6f0fc6f540efff9bbd0dc92da8c09fe7` | `0x4879,0x6879` |
| `scratch/k16_h2_to_h1_p0.h1.word` | `ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a` | `0x2c6d` |

Both contain 12873 nonzero masks.  Independent start-by-start OR replay gives
the displayed hole sets.

The words differ only at zero-based position 0:

```text
H2: p0 = 0x2c61
H1: p0 = 0x4879
```

This assignment installs both H2 holes and creates the single H1 debt
`0x2c6d`.  It is a net `2 -> 1` transition, not a zero-debt move.  The retained
transition audit has SHA-256
`fa880e45d86e36858a6c3051a65d3c8e8b93cc7a36fedfd199541e32131f8011`.

The H2 exact provider atlas has SHA-256
`cd0a200e42013c43146369986ca946c3277cd2440c38219d2c45dd7305475754`.
It evaluates 44,421 unique provider moves.  The H1 atlas-v2 has SHA-256
`b216a9da50abe571969049cc5c60b4dff534c6eebba286de1612ef9c124d3c68`
and evaluates 28,805 unique provider assignments for `0x2c6d`.

## Four exact H1 portal fibres

No H1 provider move is zero-debt.  The minimum final hole count is two, and
exactly 153 assignments attain it:

| position | exact value fibre | count | exact resulting holes |
|---:|---|---:|---|
| 0 | `0x0800 OR s`, `s subseteq 0x246d` | 128 | `0x4879,0x6879` |
| 4489 | `0x0024 OR s`, `s subseteq 0x2041` | 8 | `0x2669,0x2e69` |
| 6440 | `0x0440 OR s`, `s subseteq 0x002d` | 16 | `0x806d,0xa86d` |
| 12872 | `0x2c6d` | 1 | `0xce61,0xce63` |

Thus “four portals” means four position/debt fibres, not four literal
assignments.  A one-substitution completion would necessarily be a provider,
so the atlas also excludes a one-cell finish of H1.

The solver-free geometry audit
`scratch/ad_k16_h1_four_portal_geometry_20260730.audit.json`, SHA-256
`3263ab64f540e5552f810f2dbf919d6b18da89310162ff8746c0f099e9b4a9d0`,
derives their exact source-witness hull union:

```text
[0,2) U [4486,4490) U [6438,6441) U [12869,12873).
```

## Authenticated provider-first two-edit barrier

The earlier H2 sweep audit was initially unusable as a promoted certificate
because its mutable source had been overwritten.  The exact retained source,
included provider engine, seed, binary, and rerun now coexist under

```text
scratch/k16_h2_provider_first_floor8_frozen_20260730/
```

The H100 replay used every position, no first-move truncation, two threads,
and these exact filters:

1. the first replacement installs at least one original H2 hole and leaves at
   most seven total holes;
2. the second replacement installs at least one current hole and leaves zero
   holes.

Every successful second substitution must satisfy condition 2.  The provider
value generator is exhaustive for every interval through the edited cell.
The run finds 284 qualifying first moves and zero completing seconds.  Hence:

> Every ordered two-substitution completion from this H2 word either starts
> with an edit that installs neither original hole, or has at least eight
> holes after its first edit.

By itself this rerun is an ordered two-edit dichotomy for one rooted H2 word;
it does not exclude non-provider-first synergy, an eight-or-more-hole
excursion, or depth three and above.  The separate theorem below closes the
first of those branches.

The separately authenticated theorem
`MATH_THEOREM_K16_H2_NONPROVIDER_EJECTION_CLOSURE_AND_EXCLUSIVE_SUPPLY_20260730.md`,
SHA-256
`79b9fe8e6926350536d71c44c5a119a83dc5fcbbe028cdf51b062f3fb7c0add7`,
exhausts the genuinely non-provider two-endpoint branch and finds no
completion.  Its primary and independent audits have hashes
`bb9ff7812d69d7e9b95de51badb29f59b87a3ec012c7f7d8514c574608bcf2b8`
and
`5d11ff16a66d638448a8e85b4a3ac1ea61134336a3f74bbfb748bf116a8482ef`.
Together with the authenticated rerun above, this sharpens the current H2
two-edit frontier:

> Any still-possible two-substitution completion has a provider-first
> orientation whose endpoint assignment is a source-hole provider when
> applied alone to the frozen H2 word, and whose intermediate word has at
> least eight total holes.

The later exact mixed-face theorem
`MATH_THEOREM_K16_H2_NONPROVIDER_FIRST_MIXED_FACE_CLOSURE_20260730.md`,
SHA-256
`ec0c5d43b8a2ff6b5558c3d9c64b0beaecd0a7be78ba656219d3ecb5f8fe733e`,
also closes every chronology with one source-provider and one
source-nonprovider final endpoint.  Its twelve surviving high-debt rows all
have the same exclusive-supply contradiction
`L & ~U = 0x8000`, independently replayed occurrence by occurrence.  Thus the
newest exact two-edit frontier is sharper:

> Any still-possible two-substitution completion uses two source-provider
> endpoints, and both provider-first orientations pass through at least eight
> total holes.

That provider/provider high-debt face remains open.  The combined statement
is still rooted at the single H2 word and says nothing about depth three or an
unrelated basin.  The mixed theorem's frozen manifest has SHA-256
`6cc6f8292dd474332b3ec362561b0f65ac1df3e7d2df9e44e4b5936d99379caa`.

Independence caveat: the non-provider theorem's second verifier consumes the
primary manifest's 330 retained support rows.  It independently reconstructs
the fixed/affected interval labels and directly verifies an obstruction for
every listed row, but does not independently re-enumerate the earlier
`13102 -> 335 -> 330` corridor reduction.  Completeness of that reduction
rests on the nested-hole proof plus the primary enumerator; every retained
pair is independently replayed.

Key retained hashes are:

| artifact | SHA-256 |
|---|---|
| frozen sweep source | `2626bc0c68902817155c3b94e7bfc8248aec91f8f62a08b2d46c9fa43b33dfd8` |
| included provider engine | `d68273a4c77a3aa41a25a53539a78b7d4030f0b002afcb153cde8c4ee3db1068` |
| H100 binary | `4dfb6d7a0b87d959a5f091471a4e8ffa3e134441f8287ca00d3ae3c3d029674b` |
| replay audit | `92c86bafea6e50630efa370e0cf048c69ecfcbb79178cda58bd1f343493d0225` |
| resource transcript | `e32c4b39a756dfeb8788e8effefb97ccbc9f7ff093b9a2bc9fa8377e029cbe50` |
| consolidated manifest | `14015af20b855a9b10901b3793d9dd8c88fd2ceec60a6166794f35521ba50344` |

The regenerated audit is byte-identical to the earlier audit, closing the
lineage gap without strengthening its scope.

## Exact joint13 raw CNF

The editable positions are

```text
0,1,4486,4487,4488,4489,6438,6439,6440,12869,12870,12871,12872.
```

Every listed cell may take any nonzero 16-bit mask, including its incumbent;
there is no cardinality constraint, and every other position is frozen.  The
raw affected-witness formula has:

```text
55 residual targets
341 changed-interval bases
1595 dominance-minimal witness terms
1816 variables
35208 clauses
81990 literals.
```

Its hashes are:

| artifact | SHA-256 |
|---|---|
| `model.cnf` | `0fc8ab9880a5016cbc404810f74f1b04c54e93903f6b2b7e1ff47e7dc12f8cb7` |
| `model.map` | `cefb607c2b16278aeafedc865fd74ec86f77bf5dc35b83a2a3fd347c8cdc47e9` |
| `model.stats.json` | `390efe8ac875a660fb34fa530be844011c12f7378262e92978790c39e0415318` |
| emitter source | `5d40fc37e1b1caea5992049887204a8224589b48f91ab7b5c6d7531efdc503a1` |
| included frozen core | `c660cae1f5915f23a783fc371177cbe90f0206830d2fb83be92bd0c17a964cb8` |
| positions | `2113ceb9471adb07407e57898ea0f451b7f38d926f3e034ac6cd2d3c2261e153` |

A fresh source compilation reproduces the CNF, map, and statistics
byte-for-byte.  The independent audit rebuilds the fixed-run target partition,
every affected interval base, every minimal need term, and the complete DIMACS
clause multiset.  It returns GO:

| artifact | SHA-256 |
|---|---|
| audit driver | `d9595223f3ffb02bb7aaac6e7e3fa00a6d01281a010c23154b0c5582b5c3876e` |
| audit JSON | `8b4e73c42771f7c3ce35fba4121db1274fd38f3711864380e3c71c000da9d3ad` |
| audit payload | `15f6c9463bc0fdadd4cd6f0abfed78d2e46e14cd572887a7d718d6fd03a7818e` |
| fail-closed raw SAT decoder | `37bbd13953c1f2f43531d7588925b30d1845f6cf849fdbf00c17690231908c85` |

After existential projection of auxiliary variables, the raw CNF is
satisfiable exactly for universal physical words in this frozen 13-cell fibre.

## Exact compact occupancy projection

The independently audited canonical occupancy formula is equisatisfiable
with the raw unbounded-cardinality formula.  It has 1,130 variables, 17,558
clauses, and 67,482 literals.  Its CNF and map hashes are

```text
504677bee9bdf8a9eed475f284bcae489a2cf78db6dbc2a2b696c9bc7a632887
486b5a2f3fa3fd05432190e62bba5fdf7594739b9cd71b058212e8e60a346330
```

An independent builder produces the same normalized clause sequence.  The
equivalence proof and complete lineage are in
`MATH_AUDIT_K16_REORGANIZED_H1_FOURPORTAL_JOINT13_OCCUPANCY_EQUIVALENCE_20260730.md`,
SHA-256
`ac9b3e248baa7fac1efa0195fe0744c596b72ac37ed30b749729443b0c561687`.

Canonicalization may change physical masks and the number of changed cells.
It is therefore exact here only because the parent budget is unbounded.  It
must not be combined with an exact-change-count row without a new proof.

## Solver disposition

Two nonduplicate H100 lanes were run under one-core, 1,800-second, 8 GiB
address-space caps.  Every proof and log was written under a unique
`/home/amodo/or15/work/root_k16_*` directory; `/dev/shm` was used only to read
pre-existing solver binaries.

| encoding / solver | result | terminal evidence |
|---|---|---|
| raw 1,816/35,208 CNF, Kissat seed 731, core 31 | `UNKNOWN` | SIGTERM at 1,799.62 process seconds; no explicit SAT/UNSAT line |
| occupancy 1,130/17,558 CNF, CaDiCaL 3.0.1 seed 941, core 41 | `UNKNOWN` | SIGTERM at 1,799.99 real seconds; no explicit SAT/UNSAT line |

The raw run reached 36,225,520 conflicts and at most 96 MiB RSS.  Its retained
partial DRAT has 2,814,377,984 bytes and SHA-256
`0512202facfdce230922afb10c033777d57317efa6a40e67946cdfb3240f8764`.
The occupancy run reached 24,504,855 conflicts and 81 MiB RSS.  Its retained
partial DRAT has 1,927,220,337 bytes and SHA-256
`1dbb616e430ff021e0344467db4ebfeb8483e05b4a11777370e4e04b243d1f8b`.

Neither partial stream ends in an UNSAT derivation, and neither is a
certificate.  No proof verification was attempted because neither solver
reported UNSAT.  No candidate was emitted.  The exact frozen thirteen-cell
fibre therefore remains unresolved.

The frozen local solver audit is
`scratch/k16_reorganized_h1_fourportal_joint13_20260730/solver_portfolio.audit.json`,
SHA-256
`cb82d2f15d97b66c5e8624fafa449a6bd053c5a376812be7476dca381e85a129`.
Its local raw and occupancy logs have hashes
`231a874a278ed9bbf4c70573a7c7e5504b4a6fbb17403fcbd2450ccfe1d590ae`
and
`8d8899686c47ba36fabf1be30e72c022b9acf704525642c8d429840afaf0952c`.

A separately owned 1,790-variable explicit-witness encoding remained active
after these lanes closed.  It is not duplicated here, and no status is
inferred from its running process.  Its incumbent-derived structural phase is
now independently audited: exactly one of 55,852 clauses fails,
`(-467 OR 1621)`, the bit-11 availability row for a singleton `0x2c6d`
near-witness.  Availability elimination yields 36 direct bit-11 conflicts
and 62 full-singleton binary conflicts across 31 targets.  The exact core and
scope are recorded in
`MATH_AUDIT_K16_H1_FOURPORTAL_STRUCTURAL_PHASE_ONE_CLAUSE_CORE_20260730.md`.

## Depth-three/four normal form

`MATH_THEOREM_K16_ATOMIC_PORTAL_PACKET_NORMAL_FORM_20260730.md` proves the
complete fixed-support search reduction needed beyond the two-edit barrier.
For a chosen current hole, an exhaustive branch object is a simultaneous
witness-installing packet, possibly nonconsecutive and of size greater than
one.  Chronological non-provider edits outside its witness may be deferred.
The companion interval-piercing theorem gives exact support protection bounds.

This validates a depth-three/four recursion only when intermediate hole and
debt caps are removed.  It also exposes why raw witness multiplicity and the
previous `0x082a` reserve test are insufficient: a true reserve must contain a
witness disjoint from the contemplated future packet, or have piercing number
larger than the residual budget.

## Claim boundary

A decoded SAT assignment for either exact CNF would be a universal
length-12873 word and would close the global one-cell gap constructively.  A
verified UNSAT proof excludes only arbitrary values on the thirteen displayed
positions with the complement frozen.  It does not exclude:

- edits outside this support;
- a different length-12873 basin;
- insertions, deletions, relocation, or reordering; or
- unrestricted K16.

The global bracket remains

```text
12873 <= nu(16) <= 12874.
```
