# Independent audit of the K17 drop-12 bilateral-source triple oracle

**Date:** 2026-08-03  
**Audited theorem:**
`MATH_THEOREM_K17_DROP12_IRREDUCIBLE_BILATERAL_SOURCE_TRIPLE_ORACLE_20260803.md`,
SHA-256
`30c08e08e18fd5d75e011a053da5207e24184ad56c0dce17a5ab9729ca1e283d`.

## Verdict

**PASS.**  On the canonical drop-12 parent, the exact unary, directed-pair,
and ordered-triple no-go chain implies that every occurrence-valid triple
containing an authenticated source must give that source a two-phase option
using both other installed helper hosts.  The `B/G1/G2` factorization, its
nine phase-class pairs, the 21 source templates, the 645 full host-incidence
matrices, and the structural multiplicity formulas are correct.

During review, two implementation ambiguities were found and corrected in
the audited snapshot: a `G1` generator must test the activated helper state
against itself when `alpha=beta`, and its other-state bank is the complete
unary-`e` bank, including `H_e` and admissible incumbent LLR hosts, rather
than a parent-only base bank.

## Exact support reduction

For a source option `o_e`, classify its use of `h_f,h_g`.

* Support zero restricts unchanged to the unary `e` child: neither inserted
  helper state is used, while the absent donor rows `d_f,d_g` cannot occur in
  its footprint.  This contradicts exact unary zero on all 468 sources.
* With support `{f}`, the same source option restricts to the directed
  `e+f` child.  This asserts a source option, not a complete pair packing.
  Losslessness of the `52,664,349 -> 94` source-rescue screen retains that
  prefix.  The triple is consequently in the complete `10,536,324` ordered
  extension domain; losslessness of its phasewise upper and the independent
  complete replay `70 -> 0` exclude it.  Support `{g}` is symmetric.

Thus every surviving source role has support `{f,g}`.  If a physical triple
contains several members of the 468-source bank, the argument applies to
each retained source label separately.

The frozen evidence is consistent with this use: unary common positives are
`0/468`; the 94 exact pair rows have 94 source anchors and zero pair
packings; and the 70 exact triple rows have zero packings, zero unanchored
source options, and zero native-phase-0 third-role tuples.  Phase 1 remains
transported-owner evidence.

## Factorization and finite templates

In one phase, a source ticket contains neither helper (`B`), only `h_f`
(`G1_f`), only `h_g` (`G1_g`), or both (`G2`).  The classes are disjoint and
complete.  `B` must survive both donor deletions; `G1_f` is built in the
`e+f` child and must survive deletion of `d_g` (and symmetrically for
`G1_g`); `G2` is built after both deletions.  These casualty tests apply in
both phases and to every provider kind.

The ordered phase-class pairs whose union contains both helpers are exactly

```text
(B,G2)       (G2,B)
(G1_f,G1_g)  (G1_g,G1_f)
(G1_f,G2)    (G2,G1_f)
(G1_g,G2)    (G2,G1_g)
(G2,G2)
```

There are nine: seven pairs incident with `G2`, plus the two opposite
`G1_f/G1_g` pairs.

For the source alone, a phase footprint is one of the seven subsets of
`{h_e,h_f,h_g}` of size at most two.  Inclusion-exclusion gives

```text
7^2 - 2*4^2 + 2^2 = 21.
```

For all three roles, a phase assigns each selected host to unused or one of
three roles.  Removing the three all-to-one-role assignments leaves 61.
Forbidding `h_f` from the source leaves `4*3*4-2=46`; forbidding both helpers
leaves `4*3*3-2=34`.  Hence the exact host-incidence cover is

```text
61^2 - 2*46^2 + 34^2 = 645.
```

These are template counts only; keys, directions, flags, literal rows,
donor casualties, and cross-phase coalescing remain exact join fields.

The provider semantics used by the proof agree with the frozen replay:
7,213 private rows are unavailable; reservations are 20 rows per phase,
with intersection 17 and union 23; an opposite-phase-only row is admitted
only at its incumbent flag; and current incumbent LLR hosts remain eligible
when the phase rule permits them.  Same-phase sharing is forbidden, while
opposite-phase sharing is allowed only at one common flag.

## Structural census and source-label symmetry

Both reviewed counters implement the same endpoint-matching algebra:

* producer-style multigraph counter, source SHA
  `a0dbd04c7becc59c18ce41f295a715255598b0fce40447e3326550454556491d`;
* independently structured bipartite counter, source SHA
  `f63793159ae15d1383a92a737b7e4fb5be46b7b06eb9ba0c702d99b7b4f7f05b`.

The first uses degree inclusion-exclusion with the parallel-edge correction
in the theorem.  The second independently verifies that the actual `U`
graph has disjoint host/donor shores and 112,621 unique endpoint pairs, then
counts size-three matchings.  Its frozen audit SHA is
`738cfee3a4965bb42c2fb3768a73d29bbd42a71e0a4ca382e19958317fa678ba`.
The resulting structural census is

```text
U modes                                      112,621
source modes                                     468
M3(U)                                235,111,811,861,040
M3(U minus S)                        232,171,812,852,413
unique triples containing a source    2,939,999,008,627
  exactly one source                   2,929,210,805,021
  exactly two sources                     10,776,672,353
  exactly three sources                       11,531,253
source-anchored unordered records      2,950,798,743,486
source-anchored ordered-helper rows     5,901,597,486,972
```

The identities are

```text
A = T1 + 2*T2 + 3*T3,
B = T2 + 3*T3,
C = 3*T3,
T = T1 + T2 + T3 = A - B + T3.
```

Therefore a source-anchored enumeration duplicates a two-source child twice
and a three-source child three times.  Helper sorting removes only helper
order.  It is proof-safe to collapse to one sorted physical triple only
after retaining the complete set of bilaterally viable source labels; G2
predecessor/successor orientations and literal option alternatives remain
distinct.

## Scope

No broad support-two search was run in this audit.  The theorem proves a
lossless remaining domain and exact checker contract, not that the domain is
empty.  Every retained child still needs complete helper-role menus, exact
three-option packing, simultaneous literal materialization with protected-row
replay, and a fresh complete supplier matching.  The 645 matrices are not
physical triples or supplier positives.
