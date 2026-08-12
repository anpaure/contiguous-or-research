# Independent audit of the K16 P0 fixed/variable append CNF–DRAT bundle

Date: 2026-07-30

## Verdict

**PASS, with one scope-count correction.**  Both retained formulas are exact
literal interval encodings of their named finite templates, and their retained
binary DRAT proofs verify UNSAT.  An independent reconstruction matched every
CNF clause in order, not merely the headers or aggregate counts.

The inclusive P0 basin ranges

```text
6439-6441,12868-12872
```

contain **eight** editable basin positions, not six.  The builders and maps use
the correct eight-position list.  Only prose that calls this a six-position
scope is wrong.

## Exact negative scopes

Let (P) be the authenticated length-12,873 basin with SHA-256

```text
0a70a67eced48a82883a698c6fd25688a27c52faf19e3fa11bbbd9a78581bea6.
```

The fixed formula allows arbitrary nonzero values at exactly

```text
6439,6440,6441,12868,12869,12870,12871,12872
```

and appends the fixed cell `0x287d`.  Its verified UNSAT result has only that
scope.

The variable formula allows arbitrary nonzero values at those same eight
basin positions and also makes the appended cell at position `12873` an
arbitrary nonzero 16-bit value.  Its verified UNSAT result therefore closes
arbitrary append **within this P0 basin-edit template**, but it is not an
unrestricted length-12,874 no-go.  Positions outside the displayed P0 set are
frozen.

## Encoding audit

Intervals avoiding every editable position lie wholly in one fixed run and
are replayed before formula construction.  Every other interval meets one
consecutive block of editable positions.  Its variable-dependent part is
determined by the first and last editable indices, while its fixed part is the
OR of:

1. a suffix of the fixed run before the first editable cell;
2. every complete fixed gap between editable cells; and
3. a prefix of the fixed run after the last editable cell.

For a residual target (t), a witness variable for pattern
((i,j,F)) implies:

* every zero bit of (t) is absent from all editable cells (i,ldots,j);
* every one bit of (t) absent from (F) occurs in at least one of those
  editable cells; and
* patterns with a forbidden fixed bit, (F\mathbin{\&}\neg t\ne0), do not
  receive a witness.

An at-least-one clause over these exact patterns is added for every residual
target.  Each editable cell has a nonzero clause.  These conditions are
necessary and sufficient for literal contiguous-OR universality within the
named template; witness equivalence is unnecessary because every target ALO
forces one implication-valid exact witness.

The variable-append builder uses a placeholder at position `12873`, but that
position is itself editable and hence excluded from all fixed runs.  The
placeholder cannot affect the formula.  The appended singleton and all
cross-boundary intervals appear in the consecutive-block catalogue.

## Independently reconstructed counts

| model | editable 16-bit cells | residual targets | patterns | bit vars | witness vars | total vars |
|---|---:|---:|---:|---:|---:|---:|
| fixed `0x287d` append | 8 | 30 | 165 | 128 | 791 | 919 |
| arbitrary append | 9 | 31 | 176 | 144 | 1014 | 1158 |

The fixed clause ledger is

\[
8+30+5857+12594=18489,
\]

and the variable-append ledger is

\[
9+31+7674+18420=26134.
\]

The four terms are respectively cell-nonzero, target-ALO, positive-bit
witness, and zero-bit exclusion clauses.  The independent checker regenerated
the entire ordered clause sequences and found exact equality with the retained
DIMACS files.

## Proof audit

The retained checker outputs state:

```text
fixed:    919 variables, 18489 clauses, 3034211 proof bytes, s VERIFIED
variable: 1158 variables, 26134 clauses, 17273929 proof bytes, s VERIFIED
```

These values match the actual CNFs, maps, and proof file sizes.  The 2.9 MiB
fixed proof was also rerun locally with the frozen `drat-trim` binary and
returned `s VERIFIED` in 0.956 seconds.  The 16 MiB variable proof was not
rerun locally because the operating system refused the requested hard
address-space ceiling; its retained verification output and all input/proof
hashes were instead audited.  No heavy local solve was run.

The fixed CP-SAT audit independently reports `INFEASIBLE` in the same
eight-position/fixed-append scope.  The DRAT proof, rather than the CP-SAT
status, is the proof-producing certificate.

## Frozen primary bundle

```text
fixed emitter
  2a2ffca7a27511e32ab4539e8ad0e34417ccba2da805bc00f406bf5ca0af7be0
variable emitter
  f07d94cd855747fc20f830473d8d22df3c365dca41e16579486b2fe2ace49e68
template driver
  820bc726f4a9edafb69081e36f24712a0dfe2196ea33271bc661d690056b0cfb

p0_append287d.cnf
  ef88e6e7eb76323254f9d0ea7385a1a8044a01d164d6a336c489115d08271497
p0_append287d.cnf.map.json
  9e2d92cd46eada2c07a7042fe653e2487cdb6c018054d6b2547af89189a26a66
p0_append287d.drat
  84b54a054e8a6a5be4c7d252b5ffb90696e51d68ff92d8ab0a3f0667a5bdd78c
p0_append287d.dratcheck.out
  80f16bf7c96d5b4ba21b838ac028449c985bc67184fb31c4a737735f839b2373

p0_variable_append.cnf
  ed5c08f4fe03e0d89b669d3700be35068a835c14f6d789514818530d1f922c0e
p0_variable_append.cnf.map.json
  6c08325aa11150c8d8ccdd16786f18753089e176e0adfaa076496a1125ffb542
p0_variable_append.drat
  10bc3e923fc3fc57fa88f7193b7307600fcc0fe0f65ae28cace8394778cfa045
p0_variable_append.dratcheck.out
  ed778e19fd002427fc236e7f0cdc6002087d3de0bd8500f661dbb68b3dbc6efd

drat-trim binary
  ebf53476748574a057367ff7c199002ce0d54e457a37044118d545495c641f54
```

## Independent replay artifacts

```text
scratch/audit_ad_k16_12874_append_template_bundle_independent_20260730.py
SHA-256 7157b269f7c7cc66b9cdf70c594a007544d180f2843df231ed3707d6be303f67

scratch/ad_k16_12874_append_template_bundle_independent_20260730.audit.json
file SHA-256    845066242bf0750945a2a35c10a4a7ddf8eef83482624a41f91e44f4ce892438
payload SHA-256 121bab02ae3abd54f5b74ed96a8071c9cbc8784e4785110c7ef0f498f4106970
```

The JSON report freezes all primary file hashes, exact reconstructed target
and clause counts, proof-byte/log agreement, the corrected eight-position
scope, and the clause-for-clause comparison result.
