# Exact two-deletion plus 13-append screen at length 476

## Scope and result

Start with the fixed 465-entry word in
`k11_upper549_natural_array.txt`.  Delete two entries, keep all remaining
entries in their original order, and append thirteen nonzero 11-bit masks.
The completed length would be

\[
 465-2+13=476.
\]

All

\[
 \binom{465}{2}=107{,}880
\]

deletion pairs have now been rigorously eliminated:

* 107,861 pairs violate the missing-poset width theorem;
* the remaining 19 exact formulas have independently verified binary DRAT
  proofs.

Therefore there is no universal length-476 word in this complete
fixed-prefix two-deletion-and-append-13 neighborhood.  This is not an
unrestricted proof that `nu(11)>476`.

## 1. Structural width screen

If `q` positions are appended to a fixed prefix, every target missing from
the prefix must choose one of the `q` new right endpoints.  The suffix ORs at
one endpoint form an inclusion chain.  Thus the missing-mask poset has width
at most `q`.

For `q=13`, independent exhaustive scans give the complete distribution

| Missing-poset width | Pairs |
|---:|---:|
| 13 | 19 |
| 14 | 370 |
| 15 | 2,981 |
| 16 | 11,429 |
| 17 | 25,283 |
| 18 | 33,221 |
| 19 | 25,247 |
| 20 | 9,096 |
| 21 | 233 |
| 22 | 1 |

The exact scanner is
`scratch/screen_append_deletion_pairs.cpp`, SHA-256

```text
f098c02fccf10e20f51755a9c450b3aee00380b76a9b374ae39cb885c63858fe
```

and is run by

```sh
g++ -O3 -std=c++20 -pthread \
    scratch/screen_append_deletion_pairs.cpp \
    -o /tmp/screen_append_deletion_pairs
/tmp/screen_append_deletion_pairs 11 13 8 \
    < k11_upper549_natural_array.txt
```

A separately written scanner and direct quadratic interval enumeration both
reproduced the distribution and every survivor profile.

## 2. The nineteen width-tight pairs

Every survivor contains deletion 102, whose value is 24:

| Deleted indices | Missing masks | Width |
|---:|---:|---:|
| 0, 102 | 19 | 13 |
| 102, 462 | 20 | 13 |
| 102, 464 | 21 | 13 |
| 102, 272 | 22 | 13 |
| 102, 150 | 23 | 13 |
| 102, 180 | 23 | 13 |
| 102, 223 | 23 | 13 |
| 102, 260 | 23 | 13 |
| 102, 404 | 23 | 13 |
| 102, 438 | 23 | 13 |
| 102, 444 | 23 | 13 |
| 102, 178 | 24 | 13 |
| 102, 267 | 24 | 13 |
| 102, 394 | 24 | 13 |
| 102, 432 | 24 | 13 |
| 9, 102 | 25 | 13 |
| 49, 102 | 25 | 13 |
| 102, 263 | 25 | 13 |
| 102, 238 | 27 | 13 |

The global minimum number of missing targets is eighteen, attained by pairs
`(0,1)` and `(0,462)`, but both have width fourteen and are structurally
impossible.  Hence `(0,102)` is the strongest width-feasible repair pair.

## 3. Endpoint-chain exact formulas

The audited source `append_completion_sat.cpp` has SHA-256

```text
7e49ea13cd92b42a9a7c2bc7c3116e3b9dd6ca80719111b62d9163fef60368e3
```

and the deployed binary has SHA-256

```text
bae9f7e45172c16e0981c0d9d8ef990591dc46e4015fbdd77bec3b4ab5f2e9b5
```

In addition to enumerating every appended-only and seam-crossing witness,
the formula materializes the exact new right endpoint selected by every
missing target.  It imposes:

* at most one incomparable target at every endpoint, including cross-rank
  pairs;
* when the missing-poset width equals `q`, one member of a fixed maximum
  antichain at every endpoint.

These clauses are exact consequences of the suffix-chain theorem and remove
no completion.  Independent static audit, 20,000 random-family width tests,
and a real CaDiCaL regression all pass.

The original no-deletion append remains SAT at

```text
1338 variables / 71164 clauses.
```

A fresh 477-entry model passed both independent OR verifiers.

## 4. Complete proof certification

Every one of the nineteen width-tight formulas returned UNSAT and emitted a
binary DRAT proof.  Each CNF/proof pair was independently checked with

```sh
drat-trim formula.cnf proof.dratb -i -w
```

and all nineteen logs end in

```text
s VERIFIED
```

The proofs use between approximately 1.65 million and 4.64 million checked
resolution steps.  The complete archive is

```text
scratch/k11_length476_two_deletion_proofs_20260723.tar.gz
```

with SHA-256

```text
828e3eda371978508fdcd0e4589c4770499eb4bef506210c573a4a804d835f36
```

Its internal 57-file SHA-256 manifest has hash

```text
bc5bd4278593eb9189f378c9ffa784b1be147d4fbe8ace4be57bccac7369bca2
```

The archive contains every CNF, binary proof, verifier log, solve log, and
status file.  The archive was re-extracted locally; every manifest entry
passed `sha256sum -c`, and all nineteen verifier logs were independently
counted.

## 5. Exact boundary of the conclusion

The one-deletion and two-deletion repair neighborhoods are now completely
closed at length 476.  This proves that a successful 476-entry construction
cannot be obtained from the current 465-entry partial word by preserving the
order of all but one or two entries and appending the corresponding number
of repairs.

It does not exclude:

* three or more deletions followed by a longer append;
* insertions or replacements in the interior;
* a different ordering of the 465-entry prefix; or
* an unrelated universal word of length 476 or 465.
