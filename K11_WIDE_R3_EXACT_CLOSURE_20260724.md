# Certified exact closure of the new `k=11` wide-LNS radius-three branches

Date: 2026-07-24

## Result

Four distinct frozen length-476 words from the live wide-LNS portfolio each
cover 2,046 of the 2,047 nonzero 11-bit masks and miss only mask `1884`.
For every word, 24 selected triples of editable positions have exact untouched
repair-family size four and unique-witness load three.

The audited fixed-edit CNF encoding was generated for all 24 triples of each
word.  It quantifies all `2047^3` assignments of arbitrary nonzero replacement
values for a selected triple.  CaDiCaL returned UNSAT on the three distinct
formulas, and every proof was independently accepted by `drat-trim` with

```text
s VERIFIED
```

The fourth formula was regenerated from its own frozen word and is byte-for-
byte identical to the third formula, including its variable map.  Therefore
all 96 named fixed-position cases are certified impossible.  Equivalently,
the certificate excludes

```text
823,426,351,008
```

seed/case/value tuples.  This is a local exact-neighborhood result only; it
does not change `465 <= nu(11) <= 477`.

## Inputs

The frozen word hashes are:

```text
90fdda5bcdb17286ea91741ef770665a40ff843c43d6d651dcdd7285af018935  wide1701
95b41b72bcfa69dc0cbed6d2a0c21ec11672712c0b59012b0e41180f64034e41  wide1702
d6ab7f82036a1fdede77ca735a1e4634163bfdf43607e4d2fc8f55050fe8a207  wide1703
396b3c018b52158c00ddff9e384f1ece9c76447e1a69d073e4dab74bc2000a1d  wide1704
```

The first, third, and fourth words use the same 24 position triples; the
second uses its separately frozen 24-case list.  Exact branch construction
and the live-state diagnostic are in
`K11_WIDE1701_1704_DIAGNOSTIC_20260724.md`.

## Formula inventory

```text
run       cases  variables  clauses  literals  CNF SHA-256
wide1701     24       1243     5629     13260  a47b186e...633467
wide1702     24       1219     5172     12126  36268aac...a874
wide1703     24       1243     5629     13260  91929998...e490
wide1704     24       1243     5629     13260  91929998...e490
```

`wide1703.top24.cnf` and `wide1704.top24.cnf` compare equal byte-for-byte;
their map files also compare equal and have SHA-256
`b827eff10d21a2009aa0c43b4e6e31f81429270f10b8d7395b3854cc97b30c79`.

## Proof certificates

```text
wide1701 proof  f7dc9ba13dd1aecfa6d5d95480cbaec265ac452da5a4f043112458abb1a1064e
wide1702 proof  cc33bf44786f42ea0ce3d844b4dfe2aa827394ce9ef28d8f81822739818f5026
wide1703 proof  14b57081822dd325b7aba9486146b54d0bf6aeabb3e6017e597bb95c2c855a0c
```

The checker logs have respective hashes

```text
bbd10566706b70cb0fe1db8b1def281acc385bfc098a3c314c5520a11f6f013b
f7315c9a588aba4e160033b79d32217017b83a1c3a4096bfee87053e2bef5f0d
e6bad0853f79e600372dbcbaed6de498048976929eeb42717585b7c49244428a
```

and report verification times below 0.11 seconds because the formulas are
small.  The frozen remote executable hashes were:

```text
CaDiCaL   28ac31c3ded66d398692fd390086e5db669520bf31346a5b3780bf6ea67a1590
drat-trim be9a20191731a6a6a82e509d959d5c5c9f69f1a92765bf3209685622c0384498
generator eeafff309e47c3069d9b10372dc12658eadf99195eb3a76239c968afce142afd
```

The complete local proof bundle is
`scratch/k11_wide_r3_certified_20260724/`; its manifest has SHA-256

```text
bab00c847bd0ef8073317ce97b7ee9df0d6fa63efc43c2538091c3cad4ea10d8
```

## Semantics and limits

The fixed-edit formula is satisfiable iff at least one listed position triple
admits arbitrary nonzero replacement values making its complete 476-entry
word universal.  This equivalence and the independent decoder are audited in
`K11_FIXED_EDIT_NEIGHBORHOOD_SAT_20260724.md`.

UNSAT therefore closes exactly the listed triples.  It does not close all
radius-three triples around any seed, the complete arbitrary-two-replacement
neighborhoods of the four seeds, or unrestricted length 476.
