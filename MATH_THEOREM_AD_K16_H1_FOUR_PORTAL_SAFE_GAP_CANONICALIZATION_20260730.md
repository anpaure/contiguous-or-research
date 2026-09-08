# K16 H1 four-portal safe-gap and canonical-intersection theorem

Date: 2026-07-30  
Lane: AD, independent solver-free audit  
Status: **proved on the named source and support; completion remains UNKNOWN**

## 1. Frozen source and scope

The source is

```text
scratch/k16_h2_to_h1_p0.h1.word
SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a
```

It has length 12,873 and its sole missing nonzero contiguous-OR colour is

```text
H = 11373 = 0x2c6d.
```

The provider atlas is

```text
scratch/k16_reorganized_h1_exact_provider_atlas.audit.json
SHA-256 59cbc69665c5f21c8f9575e997765da478e947322d926669172cb71a04ddbbb7
```

The statements below concern arbitrary nonzero replacements only on the
explicit thirteen-cell support in Section 4.  They do **not** say that every
length-12,873 completion is equivalent to one on that support, and no SAT or
UNSAT result is claimed.

## 2. Independent reconstruction of all minimum-debt moves

For a position `p`, let `L_p` and `R_p` be the compressed lists of distinct OR
states of intervals ending immediately before `p` and starting immediately
after `p`, including the empty state.  A replacement `x` can create `H` iff
for some `l in L_p`, `r in R_p`,

```text
(l OR r) subset H,
x = (H \ (l OR r)) OR s,   s subset H intersect (l OR r).
```

This enumerates every possible one-cell `H` provider: every `H`-witness
through `p` has precisely one such pair of side states, and the displayed
condition is necessary and sufficient.

Rebuilding all interval multiplicities gives exactly 28,805 distinct
position/value providers.  Their exact debt histogram agrees entry-for-entry
with the frozen atlas.  The minimum debt is two, attained by exactly 153
moves, and those moves are precisely the following four cubes.

| position | old value | minimum-debt replacement cube | count | common new `H` witness | exact debts |
|---:|---:|---|---:|---|---|
| 0 | `0x4879` | `0x0800 OR s`, `s subset 0x246d` | 128 | `[0,3]` | `0x4879,0x6879` |
| 4489 | `0x2261` | `0x0024 OR s`, `s subset 0x2041` | 8 | `[4486,4489]` | `0x2669,0x2e69` |
| 6440 | `0x806d` | `0x0440 OR s`, `s subset 0x002d` | 16 | `[6438,6440]` | `0x806d,0xa86d` |
| 12872 | `0xce60` | `0x2c6d` | 1 | `[12872,12872]` | `0xce61,0xce63` |

The counts are `2^7,2^3,2^4,1`, hence total 153.  This is an exhaustive
classification, not merely a list of examples.  Notice that the full
provider menus at positions 4489 and 6440 each have 128 values; respectively
only 8 and 16 of them attain debt two.

## 3. Exact destroyed witnesses

The source occurrence lists of the eight debt colours are:

| debt | every source witness |
|---:|---|
| `0x4879` | `[0,0]` |
| `0x6879` | `[0,1]` |
| `0x2669` | `[4487,4489]` |
| `0x2e69` | `[4486,4489]` |
| `0x806d` | `[6440,6440]` |
| `0xa86d` | `[6438,6440]` |
| `0xce61` | `[12871,12872]` |
| `0xce63` | `[12869,12872]`, `[12870,12872]` |

Thus the word has one source witness for every listed debt except `0xce63`,
which has exactly two.  Every listed witness contains the corresponding
portal.  Direct replacement-delta evaluation proves that every value in each
cube destroys all witnesses in its row and no other colour loses its last
witness.

## 4. The precise minimality that is proved

For one portal family, define its **source-witness hull** to be the smallest
integer interval containing the portal and every position of every source
witness of its two debts.  The four hulls are

```text
B0 = [0,1],
B1 = [4486,4489],
B2 = [6438,6440],
B3 = [12869,12872].
```

Their union `S` has thirteen cells.  These intervals are uniquely minimal in
the source-witness-hull sense by their definition and the occurrence table in
Section 3.  This does **not** prove that all thirteen positions must change,
that no smaller arbitrary support can complete the word, or that `S` is WLOG
for the global problem.

The first `H` provider uses the fixed suffix positions 2 and 3.  Therefore
`[0,3]` is its common provider interval, while only `[0,1]` belongs to the
editable source-witness hull.  Conflating those two notions would overstate
the minimal support by two cells.

## 5. Safe-gap decomposition

The fixed gaps between these four blocks are

```text
G0 = [2,4485],       OR(G0) = 0x7fff,
G1 = [4490,6437],    OR(G1) = 0xffff,
G2 = [6441,12868],   OR(G2) = 0xffff.
```

The first identity is important: the first gap is not fully saturated.
Nevertheless it is coverage-safe.  Any interval meeting blocks on both sides
of `G0` contains `G0`, so its colour is either `0x7fff` or `0xffff`.  Both are
already witnessed without meeting `S`, for example by `[2,18]` and
`[4490,6436]`.  An interval crossing either later gap has colour `0xffff`,
again fixed-only covered.

### Theorem 5.1 (exact block localization)

Let `y` agree with the source outside `S`.  Every interval of `y` meeting two
distinct blocks has a colour that already has a source witness disjoint from
`S`.  Consequently every colour not fixed-only witnessed can be covered, or
fail to be covered, entirely within one block and its adjacent fixed context.

**Proof.** An interval meeting two ordered blocks contains every fixed cell
of an intervening gap.  Its OR therefore contains the gap OR.  The only
16-bit supersets of `0x7fff` are `0x7fff` and `0xffff`; the only superset of
`0xffff` is itself.  The explicit fixed-only intervals above witness those
colours independently of all cells in `S`.  Therefore a non-fixed-only target
cannot use a cross-block interval. QED.

## 6. Residual targets and exact local forms

Deleting all intervals that meet `S` leaves three fixed segments:

```text
[2,4485], [4490,6437], [6441,12868].
```

Exact interval enumeration in those segments leaves 55 residual targets:

```text
8805,8813,8933,8941,8949,9325,9833,9837,9965,9981,
10349,10361,10365,10441,10997,11369,11373,11465,11497,
11881,11885,13421,14537,14793,15561,15593,15817,15849,
18553,26745,30317,31177,32877,35938,35943,36070,36071,
37997,40166,42093,43117,43129,43133,44141,46189,48367,
52321,52323,52327,52455,52833,52835,54381,59513,63085.
```

This list contains the missing target `H`; the other 54 are source-covered
but have no witness disjoint from `S`.

Fix a residual target `T`, a block `B_i`, and a nonempty consecutive subblock
`J subset B_i`.  Starting from `J`, extend left through adjacent fixed cells
when `J` touches the left end of `B_i`, and extend right analogously, stopping
immediately before the first fixed cell that contains a bit outside `T` or
before the next editable block.  Call the resulting interval `I(T,i,J)` and
let

```text
C(T,i,J) = OR of its fixed cells.
```

There are

```text
C(2+1,2)+C(4+1,2)+C(3+1,2)+C(4+1,2)
= 3+10+6+10 = 29
```

such forms per target, hence exactly `55*29=1595` forms.

### Lemma 6.1 (maximal contexts are complete)

For any word agreeing with the source outside `S`, every witness of a
residual target can be replaced by one of the 1595 maximal-context forms
without changing any editable value.

**Proof.** By Theorem 5.1 the witness meets exactly one editable block.  Its
intersection with that block is a nonempty consecutive subblock `J`.  Extend
through each adjacent fixed cell whose value is a submask of `T`.  Each
extension keeps the interval OR equal to `T`, because the old interval
already had OR `T`.  The process stops exactly at `I(T,i,J)`.  It cannot reach
a second editable block: that would make `T` one of the fixed-only safe-gap
colours, contrary to residuality. QED.

## 7. Canonical-intersection theorem

Choose at least one form `f=(T,i,J)` for every residual target `T`.  For each
editable position `p`, define

```text
A_p = intersection of all targets T_f of chosen forms with p in J_f,
```

with `A_p=0xffff` if no chosen form uses `p`.

### Theorem 7.1 (exact selected-form feasibility)

The chosen forms can be realized simultaneously by nonzero editable values
if and only if both conditions hold:

1. `A_p != 0` for every `p in S`;
2. for every chosen form `f` and every bit
   `q in T_f \ C_f`, there exists `p in J_f` with `q in A_p`.

When the conditions hold, the canonical assignment `y_p=A_p` realizes every
chosen form.  Hence a completion supported on `S` exists if and only if there
is a choice of at least one of the 29 forms for each of the 55 targets that
satisfies (1)--(2).

**Proof, necessity.** Suppose values `x_p` realize the chosen forms.  If
`p in J_f`, then `x_p subset T_f`, otherwise the interval for `f` would
contain a bit outside its target.  Thus nonzero `x_p subset A_p`, proving
`A_p != 0`.  Every required bit outside the fixed context must be supplied by
some editable cell of `J_f`; that bit then belongs to every selected target
using that cell, hence to `A_p`.

**Proof, sufficiency.** Put `y_p=A_p`.  For a chosen form `f`, every editable
value on `J_f` is a submask of `T_f`, and its fixed context is also a submask
of `T_f`.  Condition (2) supplies every bit of `T_f` absent from the context,
so the OR of `I_f` is exactly `T_f`.  Condition (1) keeps every word cell
nonzero.  Fixed-only colours retain their witnesses outside `S`, and every
residual target has a selected realized form. QED.

This theorem is an integral literal-interval statement.  It is not a
fractional relaxation and does not identify target occurrence with a merely
marginal condition.

## 8. Direct exact CNF consequence

Introduce one selector for each of the 1595 forms and sixteen bit variables
for each of the thirteen editable cells.  Use:

1. one at-least-one-form row per residual target;
2. `not f OR not x[p,q]` whenever `p in J_f` and `q notin T_f`;
3. `not f OR OR_{p in J_f} x[p,q]` for each `q in T_f\C_f`;
4. one nonzero row per editable cell;
5. the reverse canonical row

   ```text
   x[p,q] OR OR{f: p in J_f and q notin T_f}.
   ```

Theorem 7.1 proves this formula equisatisfiable with literal completion on
the named support.  Exact reconstruction gives

```text
1595 selector variables + 208 cell-bit variables = 1803 variables,
35195 clauses,
104727 literals.
```

The occupancy projection may compress this further; the dimensions above
are for the direct canonical-cell formulation and are included as an
independently checkable baseline.

## 9. Reproducible audit artifacts

```text
scratch/audit_ad_k16_h1_four_portal_geometry_20260730.py
SHA-256 145c9d16c1b626f8613940bd38d53350e7652b5ee9584df14cf5a13e533d2f28

scratch/ad_k16_h1_four_portal_geometry_20260730.audit.json
SHA-256 3263ab64f540e5552f810f2dbf919d6b18da89310162ff8746c0f099e9b4a9d0
```

The JSON contains all 153 minimum-debt moves, every source debt occurrence,
all 1595 maximal local forms, the safe-gap palettes, the 55 residual targets,
and the exact direct-CNF ledger.  Its verbose local-form payload hash is

```text
28faab15c382314aa1b3c68b871b632ae7a1345b473d64580978ee2456271b64.
```

The script performs no SAT call and no completion search.  Its final status
is `PASS` for reconstruction and `UNKNOWN_NOT_SOLVED` for completion.
