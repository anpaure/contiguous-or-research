# K16 nested-portal normal form and the interacting-12 no-go

Date: 2026-07-30

## 1. Scope and source basin

The source is

```text
scratch/k16_h2_to_h1_p0.h1.word
```

of length `12873`, with sole missing mask

```text
H = 0x2c6d = 11373.
```

Its exhaustive one-cell provider atlas has exactly four minimum-debt portal
positions.  At each portal, every exact portal value considered below serves
`H` and deletes exactly the displayed two-element Boolean chain:

| portal `p` | `P` | `Q` | exact portal values |
|---:|---:|---:|---:|
| 0 | `0x4879` | `0x6879` | 128 |
| 4489 | `0x2669` | `0x2e69` | 8 |
| 6440 | `0x806d` | `0xa86d` | 16 |
| 12872 | `0xce61` | `0xce63` | 1 |

In every row, `P` is a proper subset of `Q`.

This note classifies and audits a precise family of genuinely cooperative
three-cell ejection circuits.  It is not a no-go for arbitrary supports of
size three or more.

## 2. Two-blocker laminar normal form

Let `A=(a_0,...,a_{L-1})` be the source word.  Fix one portal `p` and its
chain `P < Q`.  Consider a final three-edit assignment on positions
`{p,u,v}`, `u<v`, with the following properties:

1. the edit at `p` is an exact portal edit from the table;
2. the final word has a `P`-witness interval `I_P` and a nested `Q`-witness
   interval `I_Q`, with

   ```text
   {u,v} subset I_P subset I_Q,    p notin I_Q;
   ```

3. both repair positions are genuine blockers for `P` in the source:

   ```text
   a_u not subset P,    a_v not subset P.
   ```

The third condition is what makes the repair an AND-type cooperative repair:
neither source value can be left unchanged inside a `P` witness.

### Lemma 2.1 (consecutive-blocker normal form)

`u,v` are consecutive in the ordered set

```text
B_P = {i : a_i not subset P}.
```

Let `C_P(u,v)` be the maximal interval around `u,v` containing no other
member of `B_P`, and let

```text
c_P = OR {a_i : i in C_P(u,v) \ {u,v}}.
```

Then legal repair values `x,y` must satisfy, and are sufficient to make
`C_P(u,v)` a `P` witness exactly when,

```text
0 < x subset P,  0 < y subset P,  c_P OR x OR y = P.       (2.1)
```

After treating `u,v` as editable, let `C_Q(u,v)` be the maximal interval
around them whose remaining fixed cells are all submasks of `Q`, and put

```text
c_Q = OR {a_i : i in C_Q(u,v) \ {u,v}}.
```

A nested `Q` witness exists exactly when

```text
c_Q OR P = Q.                                                (2.2)
```

#### Proof

Every cell in an interval whose OR is `P` is a submask of `P`.  Thus every
source `P`-blocker inside `I_P` must be edited.  There are only two repair
edits, so no third blocker can lie between `u` and `v`; they are consecutive
in `B_P`.  Extending `I_P` through adjacent fixed `P`-submasks changes no OR
once `P` has been reached, proving (2.1) for the maximal collar.

The same argument at `Q` shows that every fixed cell of a nested `Q` witness
is a `Q`-submask.  Extending to the maximal `Q` collar changes no OR once `Q`
has been reached.  Because the inner collar has OR `P`, the outer collar has
OR `Q` exactly when its fixed core supplies `Q\P`, which is (2.2).  Conversely,
(2.1)--(2.2) visibly construct the two nested witnesses.  QED.

This is a finite support normal form, not a heuristic candidate generator.

## 3. Separator absorption

The portal cluster `{p}` and repair cluster `{u,v}` are separated by a fixed
interval.  Let `R` be the OR of that open separator.

### Lemma 3.1 (absorbed clusters decouple)

If every old and new value at `p,u,v` is a submask of `R`, then every interval
meeting both clusters has unchanged OR.  Hence the exact coverage delta of
the three edits is the sum of the one-cell portal delta and the two-cell
repair delta.

#### Proof

Every interval meeting both clusters contains the entire separator, hence
already has OR containing `R`.  OR-ing any old or new edited value changes
nothing.  Intervals meeting only one cluster form disjoint classes and give
the two separate deltas.  QED.

All portal values are submasks of `H`, and all values in (2.1) are submasks of
`P`.  Therefore the support-level sufficient test is

```text
a_p OR a_u OR a_v OR H OR P  subset  R.                      (3.1)
```

`R=0xffff` is only the strongest special case; (3.1) finds 550 additional
decoupled supports.

## 4. Exact census

Applying Lemma 2.1 to the four portal chains gives:

| portal | all laminar two-blocker supports | `R=0xffff` | additionally absorbed | genuinely interacting |
|---:|---:|---:|---:|---:|
| 0 | 300 | 13 | 285 | 2 |
| 4489 | 313 | 41 | 265 | 7 |
| 6440 | 181 | 180 | 0 | 1 |
| 12872 | 547 | 545 | 0 | 2 |
| **total** | **1341** | **779** | **550** | **12** |

An independent 0.3-second Python verifier rederives the source hole, all four
census rows, and the exact twelve-row TSV:

```text
scratch/audit_k16_nested_portal_support_census_20260730.py
  1d4f40f55bbca8ad8d5cc14bcfcd85839f44826f3825f0ca8eb5fdbd07769c3b

scratch/k16_nested_portal_support_census_20260730.audit.json
  087661aeb11b1fb9eb22bc89c6a031a1d4389cf3f180bb0e6aca9300a5856d09
```

The exact full-separator audit enumerated every exact portal value and every
ordered nonempty pair `x,y` satisfying (2.1):

```text
structural supports: 779
value assignments:   11,096,982
status:              NO_PASS
best residual holes: 8
literal crosschecks: 35
```

Artifacts:

```text
scratch/audit_k16_nested_portal_adjacent_split_20260730.cpp
scratch/k16_nested_portal_two_blocker_20260730.audit.json
```

The full-or-absorbed audit result is recorded in Section 7.

## 5. The genuinely interacting 12

The only supports not covered by Lemma 3.1 are listed exactly in

```text
scratch/k16_nested_portal_interacting12_20260730.tsv
```

Their `(portal;u,v)` triples are:

```text
(0;2,3)              (0;6434,6436)
(4489;4484,4485)     (4489;4496,4497)
(4489;4498,4499)     (4489;4499,4500)
(4489;4501,4502)     (4489;4502,4503)
(4489;6436,6437)     (6440;6435,6437)
(12872;12867,12868)  (12872;12868,12869)
```

For each support we emitted the exact dynamic substitution CNF with all three
cells independently ranging over **every nonzero 16-bit value**, with no
cardinality bound.  This is strictly stronger than testing only the laminar
values in (2.1).  All twelve formulas are UNSAT, and all twelve DRAT proofs
were independently checked by `drat-trim` (`s VERIFIED`).

The formulas are tiny: 106--187 variables and 781--2192 clauses.  The result
is therefore an exact support theorem, not a timeout or optimization claim.

Artifacts:

```text
scratch/k16_nested_portal_interacting12_exact_20260730/
scratch/k16_nested_portal_interacting12_exact_20260730/campaign.status
scratch/k16_nested_portal_interacting12_exact_20260730/MANIFEST.sha256

generic semantic CNF emitter
scratch/k16_dynamic_unbounded_substitution_cnf_20260730.cpp
SHA-256 5d40fc37e1b1caea5992049887204a8224589b48f91ab7b5c6d7531efdc503a1

campaign script
scratch/run_k16_nested_portal_interacting12_remote_20260730.sh
SHA-256 ec47ed65a845127f33565637ed95c8985ea1eaadd2ba76de7c3ad7b1c398331f
```

The retained bundle contains each CNF and checked DRAT proof, but not the
remote emitter binary.  Its semantic lineage is therefore the frozen generic
emitter source above together with the independently audited dynamic-
substitution encoding; the manifest authenticates the syntactic proof bundle.

Authentication:

```text
support TSV:    673b89ed517b3203e8216f8f72e13f908c0aed9210d37fe5ba36c1742005ab62
campaign:       5d4a8aecd57c8f9edbb6d7b44206912e2036b1e8123e313c7ed2d1a9216a380f
manifest:       dbcb785cbe8a61b87ef79c5670bc5565d899f7169c0c8f0a279780d6afcaced6
```

## 6. Consequence and exact scope

The twelve interacting supports cannot contain a universal `12873`-word,
even if the intended portal/laminar semantics are discarded and the three
cells are assigned arbitrarily.

Together with the full-or-absorbed separator audit, this closes **all 1,341
supports** in the two-blocker laminar three-edit normal form around the four
minimum-debt portals.

It does **not** exclude:

1. a portal which temporarily creates more than the minimum nested pair;
2. a final `P` witness using one old `P`-blocker plus a second edited
   `P`-compatible supplier;
3. non-laminar or separate final witnesses for `P` and `Q`;
4. four or more edited cells;
5. a route not beginning with one of the four minimum-debt portals.

Thus the next mathematically distinct finite family is not another
provider-first depth-two sweep.  It is either the **one-blocker/one-supplier
family** or the **crossed-witness family**, followed by genuine four-cell
ejection circuits if those fail.

## 7. Full-or-absorbed exact audit

The same exact delta enumerator was rerun with Lemma 3.1 enabled.  It exhausts
all 779 full-separator supports plus all 550 absorbed-separator supports:

```text
structural supports: 1,329
value assignments:   119,532,950
status:              NO_PASS
best residual holes: 6
literal crosschecks: 38
wall time:           3:06.40 on one EPYC CPU core
maximum RSS:         13,824 KiB
```

The best point occurs in the `p=4489` geometry with repair positions
`3520,3521`; it still misses

```text
0x22cd, 0x2a65, 0x2a6d, 0x2ac5, 0x2acd, 0x2ae5.
```

Artifacts and hashes:

```text
scratch/k16_nested_portal_absorbed_separable_20260730.audit.json
  28afff6bd13cfd65f6b1e5e7eb38e53aec5135e8c34c5ba4fae2e944a552127d

scratch/k16_nested_portal_absorbed_separable_20260730.resource.txt
  584694c0eaf4f63c38a1d000796058d3b6a55506308e4ea8be47eae85870c55a

scratch/audit_k16_nested_portal_adjacent_split_20260730.cpp
  826528492d968b740ea0e0db067cf5524de1d4e2cde1d1e9fb743a46e1bf66c2

scratch/k16_nested_portal_two_blocker_20260730.audit.json
  34685ac10d680aaa0aa864c41b5c2ceba1406818e9ccbe3937b5f4840bca6654
```

The 1,329 separable supports and 12 unrestricted DRAT-UNSAT interacting
supports partition the full 1,341-support census.  Therefore:

> **Theorem.** No universal length-12,873 word is obtained from the
> reorganized one-hole basin by an exact minimum-debt portal edit followed by
> two genuine `P`-blocker edits whose final `P,Q` witnesses are laminar and
> use both repair cells.

This is the precise statewise no-go; the exclusions in Section 6 remain
essential.
