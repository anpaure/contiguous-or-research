# Optimal words

The README’s [current table](../README.md#exact-results) records exact
`nu(k)=B(k)` for every dimension through 22. Each word is a whitespace-separated
list of nonzero integer masks. Bit 0 represents coordinate 1.

The original `k01.word` through `k16.word` remain here. The six newer optimal
certificates are:

| Dimension | File | SHA-256 |
|---:|---|---|
| 17 | [k17_optimal24313.word](k17_optimal24313.word) | `7d85f8494084c7eb3f4b196159f3a5b5b020a0170e26ad0e34c6087bda525ff9` |
| 18 | [k18_optimal48623.word](k18_optimal48623.word) | `6b191b447231c665bb1288cdc7ebdea5c73fd79502ef47015ee3d98fcf685be5` |
| 19 | [k19_optimal92381.word](k19_optimal92381.word) | `1d0e7595dc72c6f1b7590e9565d5c0d3c30d70138e993d074e7d90d778d4e414` |
| 20 | [k20_optimal184759.word](k20_optimal184759.word) | `047b990b9e9f7a4585ba5d8fadf9c3d191cd218c989c3ffacf6e351d91b88d02` |
| 21 | [k21_optimal352719.word](k21_optimal352719.word) | `eb44ff87a669ae0163bdf926283c22c5494e08322efb5c947994a676dc3af1d2` |
| 22 | [k22_optimal705435.word](k22_optimal705435.word) | `a32fe59af4511fcf1a0e032e3f57ae358a9b74492a3f6d56aa8f4564c77ba2dd` |

Their [finite proof and verification scope](../EXACT_FINITE_RESULTS.md) are
consolidated in one note, and [verification.json](verification.json) contains
the compact repeatable check. Run the single public verifier, for example:

```bash
python3 verify_word.py answers/k22_optimal705435.word --k 22
```

Older upper words that were already published are retained for provenance.
They are superseded by the exact values. Intermediate new upper words and
large witness dumps remain in the local research archive instead of this
publication branch.
