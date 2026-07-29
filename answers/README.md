# Exact answers through `k=15`

Each `kNN.word` file is a whitespace-separated optimal nonzero word.  Every
contiguous-subarray OR is computed over ordinary integer bitmasks.

| `k` | `nu(k)` | SHA-256 |
|---:|---:|---|
| 1 | 1 | `4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865` |
| 2 | 2 | `f251ddc12234e0da8d3b778bd0f7463fb477f16f47757f5617dc8b4ff4d4f14a` |
| 3 | 4 | `aafa934d13be209cc39a9b5cb0b140af652fc0eebd127c42c6c982422964a790` |
| 4 | 7 | `efe145ebc697686a2e3bf53a36362b5025835f2eb0ba16a1a0e64e2abd4ec1ca` |
| 5 | 12 | `72195450d0361b37fbf58442203014eff475b3f59222c907fab99743106eee06` |
| 6 | 21 | `7d30e058f98e6c09d65515e3f3971ae8bd7637f711670fa06a8a1dc536852d6d` |
| 7 | 37 | `dda4b06c2e35bda3ea8a876a90807172adee166567d84b587ef5ae68cae9bec7` |
| 8 | 72 | `df6d76b468bd816fd014d9b6f5259ba60e5f1ea06e4c4313901fe6155c8780eb` |
| 9 | 128 | `c7e8cbfbe1a3531ffae4c9a01bd4b3b51dad0856b38486bacc56dbcaa73e3221` |
| 10 | 254 | `24b6fc4f4c054e46ef54553ca37eded126150542d51a61256a837d666e0c74fd` |
| 11 | 465 | `746b469af108558b14e7f6af0e3f76f9b6f39f70b3561e0258cc976650761850` |
| 12 | 926 | `6d598c62f5925d1d2dfce8279eea82069318bd93ff66d0b204c639cf06297851` |
| 13 | 1719 | `8d202e793d3317d2c3db76fef51f9d20d0e4e09fa2899a9686285cc01f4577d0` |
| 14 | 3434 | `7d94117099bbb46402e8f4edda718dae7eb10e2e5e34e9b588e08a198b43db17` |
| 15 | 6438 | `f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b` |

The empty word is optimal for the nonzero `k=0` problem, so no `k00.word`
file is needed.  Prepending `0` to any listed word gives an optimal word for
the version that also requires the zero mask.

Verify all files with:

```sh
for k in $(seq 1 15); do
  python3 verify_word.py --k "$k" "answers/k$(printf '%02d' "$k").word"
done
```

## Exact `k=15` certificate

The monotone-deadline lower bound and the retained word give

\[
                         \nu(15)=6438.
\]

The construction and independent exhaustive verification are recorded in
[`K15_OPTIMAL_6438_TWO_CYCLE_ARBITRARY_SEAM_CERTIFICATE_20260729.md`](../K15_OPTIMAL_6438_TWO_CYCLE_ARBITRARY_SEAM_CERTIFICATE_20260729.md).
