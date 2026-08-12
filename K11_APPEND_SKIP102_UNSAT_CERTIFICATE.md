# Certified UNSAT for the fixed skip-102, twelve-append branch

## Scope

This certificate concerns one restricted attempt to shorten the verified
477-entry `k=11` word:

1. start from `k11_upper549_natural_array.txt`;
2. delete its zero-based position 102;
3. append exactly twelve arbitrary nonzero 11-bit masks.

The exact formula is UNSAT.  Therefore no word in this fixed-prefix branch
has length 476.  This does **not** rule out other 476-entry words and does not
change the global bounds on `nu(11)`.

## Exact instance

After deletion, the 464-entry prefix misses seventeen masks, with rank
profile

```text
rank 5: 2
rank 6: 2
rank 7: 12
rank 8: 1
```

The twelve rank-seven targets saturate the twelve new right endpoints.  The
audited fixed-prefix append encoding includes every appended-only witness and
one representative of every cross-seam fixed-suffix OR.  It is sound and
complete for arbitrary twelve-entry nonzero extensions.

The certified CNF has

```text
variables=1494
clauses=90762
candidates=1362
```

and SHA-256

```text
2270fd363c941db026ca38cd5b71acbeb2266a2bf9d9aaf20f2290639612b443
  skip102_q12.cnf
```

This CNF predates the later redundant explicit endpoint-flag bank.  The
absence of that bank does not affect completeness; equal-rank endpoint
distinctness was already a semantic consequence of the exact OR clauses.

## Proof and independent verification

CaDiCaL emitted a binary DRAT proof:

```text
00fed3a7ed55e474f83abba0403090c6b8f328edad1781dd12b008c1318c1b45
  skip102_q12_unsat.dratb
```

Independent verification used

```text
drat-trim skip102_q12.cnf skip102_q12_unsat.dratb -i -w
```

and returned exit zero with

```text
s VERIFIED
73479 of 90762 clauses in core
168102 of 318640 lemmas in core
25858633 resolution steps
```

The verifier log SHA-256 is

```text
2a27fd4b0ae8185f72cdfdb0aa701892a82dfff813682fa0c9a87291589762e8
  skip102_q12_drat_trim.log
```

All three artifacts are retained under
`scratch/k11_append_delete_proofs/`.

## Evidentiary conclusion

The exact conclusion is only

```text
no twelve-entry append completes the prefix obtained by deleting position 102.
```

It is one certified branch elimination in the broader search for a
476-entry word.  Deletions 7, 89, and 196 remain the most permissive
single-deletion append branches because their shortened prefixes miss only
eleven rank-seven masks.
