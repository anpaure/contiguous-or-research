# Exact-one port of the RF495 rehost-eight cut

Date: 2026-07-30  
Lane: AD  
Scope: the frozen repeat-free seed5/self `4/9/5` fibre only

## 1. Result

The audited raw-model rehost cut has a sound exact-one projection, but it is
not obtained by appending the raw clauses or by tagging every maximal
`(target,Q)` class that merely contains an incumbent row.

Let `W_T` be the audited set of raw incumbent physical-witness selectors for
a formerly covered residual target `T`.  There are seventy-five such rows on
sixty-seven targets.  For an exact-one maximal selector `y`, let `rho(y)` be
its recorded `original_witness`.  Define

```text
I_T = { y : rho(y) is in W_T }
```

and introduce

```text
r_T <=> every y in I_T is false.
```

The exact census is

```text
67 formerly covered targets;
75 raw incumbent rows;
71 distinct exact maximal incumbent representatives;
|I_T| histogram 1^64, 2^2, 3^1.
```

Then the frozen-fibre physical theorem implies

```text
sum_T r_T >= 8.
```

Appending this relation and an exact threshold counter to the already
audited exact-one CNF gives

```text
base:          10,018 variables, 175,462 clauses;
added:            679 variables,   2,359 clauses;
strengthened:  10,697 variables, 177,821 clauses.
```

The strengthened CNF was built and independently audited, but was not
launched.  The separately assigned solve of the unstrengthened exact-one CNF
remains the unique live execution.

## 2. Why a literal clause copy is invalid

The raw model has one selector for every physical interval witness.  Its first
142 appended clauses define, for each formerly covered target,

```text
r_T <=> none of that target's raw incumbent witness selectors is selected.
```

The other 2,221 appended clauses are independent of the base model: they are
an exact dynamic counter for threshold eight.

The exact-one model quotients each `(T,Q)` class to its unique greatest fixed
part.  Four raw incumbents disappear under this quotient:

| target | erased raw row | `Q` | erased `F` | maximal row | maximal `F` |
|---|---:|---:|---:|---:|---:|
| `0x3186` | 1571 | `0x8` | `0x0000` | 1644 | `0x3104` |
| `0x3986` | 1926 | `0xc` | `0x0000` | 1999 | `0x3104` |
| `0x39c6` | 2094 | `0xe` | `0x0000` | 2168 | `0x3104` |
| `0x39e6` | 2174 | `0xf` | `0x0000` | 2250 | `0x3104` |

Greatest-row feasibility does not imply feasibility of a dominated row.  For
example, free OR `0x0082` on the `0x3186,Q=0x8` class completes the maximal
fixed part `0x3104`, but it does not complete the erased fixed part zero.
Consequently, the statement “this maximal class contains a raw incumbent” is
not, in general, an exact incumbent-survival statement.

The safe rule is stricter: tag a maximal selector only when its own recorded
representative is an incumbent.  All four displayed maximal rows are
independently incumbent rows themselves, so every one of the sixty-seven
targets retains at least one tagged representative.  The erased identities
are nevertheless not promoted or claimed to survive.

## 3. Soundness theorem

### Theorem 3.1 (safe exact-representative projection)

Fix the authenticated seed5/self RF495 fibre and the authenticated exact-one
maximal-provider CNF.  For each formerly covered target `T`, define `I_T` and
`r_T` as above.  Every satisfying physical completion of the fibre admits an
exact-one selector extension satisfying

```text
sum_T r_T >= 8.
```

Indeed, every satisfying assignment of the authenticated exact-one CNF,
after the definitions of the `r_T` are appended, satisfies this inequality.

#### Proof

The independently audited cascade theorem says that every physical
completion loses all original incumbent hosts for at least eight of the
sixty-seven formerly covered targets.

Take one such target `T`.  Every `y` in `I_T` has an
`original_witness=rho(y)` that is itself an original incumbent physical row.
The exact-one provider clauses attached to `y` are exactly the forbidden-bit
and needed-bit conditions of that row: its fixed OR, free-position mask and
interval endpoints were all independently matched.  Since the physical row
is lost, those conditions cannot hold, and therefore `y` cannot be true in a
satisfying assignment.  Hence every member of `I_T` is false and `r_T` is
true.  This applies to at least eight targets, proving the inequality.

Omitting the four dominated raw identities cannot invalidate the implication:
only selectors whose own exact physical incumbent semantics were checked are
used.  It can only make the projected notion less informative than a model
that retained every raw selector.  QED.

### Scope warning

Syntactically, `r_T` records absence of selected tagged representatives.  It
is not asserted to be a reverse-implication indicator for every physically
available incumbent interval, because provider clauses are one-way and the
exact-one model chooses one provider per target.  The theorem uses only the
safe direction: a physically lost exact incumbent representative cannot be
selected.  The imported physical rehost floor supplies at least eight such
targets.

## 4. Exact CNF

For `I_T={y_1,...,y_s}`, the definition is

```text
(-r_T OR -y_i)                    for i=1,...,s;
( r_T OR  y_1 OR ... OR y_s).
```

These clauses are equivalent to `r_T = NOT OR(I_T)`.  Across the sixty-seven
targets they contribute seventy-one binary clauses and sixty-seven reverse
clauses, hence 138 clauses.

Allocate `s[i,j]` for `0<=i<=67` and `0<=j<=8`, with semantics

```text
s[i,j] <=> at least j of the first i rehost variables are true.
```

Pin `s[i,0]` true and `s[0,j]` false for `j>0`.  For the `i`th rehost variable
`x`, encode

```text
y <=> a OR (x AND b),
a=s[i-1,j], b=s[i-1,j-1], y=s[i,j]
```

by the four clauses

```text
(-a OR y)
(-x OR -b OR y)
(-y OR a OR x)
(-y OR a OR b).
```

Finally pin `s[67,8]` true.  This is the same independently audited 612-state,
2,221-clause threshold counter as in the raw package.  Together with the 138
rebuilt definition clauses it gives 2,359 appended clauses.

## 5. Independent audit

The independent auditor does not import the builder.  It:

1. pins and checks both the raw rehost audit and the exact-one base audit;
2. reconstructs all tagged rows from raw incumbent IDs and exact-one
   `original_witness` fields;
3. matches fixed OR, physical `Q`, and interval endpoints for all seventy-one
   tagged rows;
4. verifies the four deliberately erased identities;
5. parses both DIMACS files and verifies the entire 175,462-clause base as an
   unchanged prefix;
6. reconstructs all 2,359 appended clauses byte-semantically;
7. exhausts the rehost equivalence truth tables for multiplicities one, two
   and three;
8. exhausts the sixteen recurrence rows; and
9. calibrates the threshold on all 4,096 twelve-input patterns.

It returns `PASS`, payload

```text
50a85f8af287dd9c7805f56674b344b97a486920c9b039de981d3008316e3fcf
```

## 6. Frozen artifacts

Raw alternative strengthening:

```text
scratch/k16_triwindow_rf495_rehost8_cut_20260730/model.rehost8.cnf
  dc9d50f8ce811e0d08536c375f56766e172b3451b0dd7d4eace6d6fe9b6e0c58
scratch/k16_triwindow_rf495_rehost8_cut_20260730/rehost8.map.json
  5793bdd50e1527fbf7a2c91be6c57a653db38bf9dc48d6116c9d41c2c9bdc32f
scratch/k16_triwindow_rf495_rehost8_cut_20260730/rehost8.manifest.json
  5ec7f2210aff76c82605156237fa129e362db1eeed9e616be9e02c67af720c7e
scratch/k16_triwindow_rf495_rehost8_cut_20260730/rehost8.independent.audit.json
  62fd2380ebed1b91370b21536956c83116b3fbb0fb28dd70d39b457ed5854ec9
```

Exact-one projected strengthening:

```text
scratch/build_k16_rf495_exactone_rehost8_cut_20260730.py
  2d49d4dfa015726144c966cd3688ed6fb60829e11ceb00dabf3f8da3b2f1f7ae
scratch/audit_k16_rf495_exactone_rehost8_cut_20260730.py
  b02f004dfef35c9bdcf404e5d6011b53da3dda2e534788abb83dd1f75c02cf5c
scratch/k16_rf495_exactone_rehost8_cut_20260730/rf495_exactone_rehost8.cnf
  f65f697cd5d65b7af8b8a672f7d0d4d11a8cded7f8e6214b31692eae18dcf035
scratch/k16_rf495_exactone_rehost8_cut_20260730/rf495_exactone_rehost8.map.json
  997819aa0d6fb2346cc81df1b7324eb9a38cfa4193210483d676b9915f8b5b55
scratch/k16_rf495_exactone_rehost8_cut_20260730/rf495_exactone_rehost8.manifest.json
  ee1a16975095e3578826fdf5316b40ba645694d47c02e4c1612bb71ca7e5c980
scratch/k16_rf495_exactone_rehost8_cut_20260730/rf495_exactone_rehost8.independent.audit.json
  488c2b253be9e981328770eee65a9fb4c9338432a43a0d3aa8685743eca070e3
```

No solver was launched from this package.  SAT acceptance for either model
remains a nonzero word of exact length 12,873 followed by independent literal
replay of all 65,535 masks.  No middle-row equality gate is valid.
