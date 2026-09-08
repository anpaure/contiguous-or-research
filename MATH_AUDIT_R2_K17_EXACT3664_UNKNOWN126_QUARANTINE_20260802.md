# R2 k=17 exact3664 UNKNOWN:126 quarantine audit

Date: 2026-08-02

## Result

Cases `0273`, `0274`, and `0275` are exact functional-q1 UNSAT cases.  Their
main-portfolio `UNKNOWN:126` labels were wrapper failures, not solver-unknown
verdicts.

The isolated quarantine at

```text
/home/amodo/or15/work/threadD_k17_exact3664_q1_quarantine273_275_independent_20260802
```

reconstructed each two-cut bank from the frozen baseline, rebuilt the
`Q1_ONLY` CNF, reran Kissat, extracted a core, checked that core against the
full CNF, and verified both the full and reduced DRAT proofs.  Every recorded
return code is `0`, except the expected Kissat UNSAT code `20`.

The quarantine summary is
[`quarantine.summary.tsv`](scratch/r2_k17_exact3664_anomaly273_275_20260802/quarantine.summary.tsv),
SHA-256
`e177efd6b92dc7fed753b341e98fc5d2441c663eb7162088cd52b801015dfeac`.
Its 76-entry artifact manifest has SHA-256
`fe893ed92af7ddf9bed8c68c73f3547aa8941ecae776fee9783aeb98c7370113`;
the recorded status is `overall=0`.

## Exact certificates

| case | bank SHA-256 | CNF SHA-256 | proof SHA-256 | core SHA-256 | core-lemmas SHA-256 |
|---:|---|---|---|---|---|
| 273 | `a1837ad75aade78851d5a1fbe8e3a285814b80745e31bb3e1ce8409993e53ed8` | `8483620b43b7b5317b5d7564c52d2c72ef41d401028d8520e275f9e90fa37d71` | `a4adcf61b8f63f54bba192963c2bd76610dc55f301af38f3f001b80164874344` | `a70b7296e96fdbcd8e61a4da913acf971113bd6207162d8fc6f24ef1ee905ccb` | `10aa4ad87fbc0286b3704ba7f0341a897eae0954c71f7e62eda77ad4b7aefc44` |
| 274 | `aecef96e7d9d49afaf8c375bb56ed498dbbb83f586d24547c1593311331b016a` | `2a6ce810399707e3b051ca2493711058297bc3179a04044499eb1fab4bcb9a5b` | `4230123b7774c19b11f69e31d00548f2daca29d7e25f74e1451f001a6f505b95` | `83b2247ba5f353f9fc23f8ac5780f028e4b43c34821877fc8ac2532a097009bc` | `2692d39eda56f0a2e1d17f69e5e1e2f3450c04653519ab33826474064e2e5481` |
| 275 | `f5c63966c8ef7b4dd4e5aeea458f38a182925c77b72f1034b8ff306f13eaaffa` | `423064de07f4937a0b137b08e9e0556c3c4bb97f1279320ad6103cf80196b778` | `9e3e9341dbfc953236f44b741df1f8ebfe24b16ea63e63a2966963c79b93f2ba` | `fc62e92d9f64b5e4d111dcc8ec545e00a0cb17c9be66fb9c3622caf415f57d84` | `85766af49eed1790e46086d079f49445bf46a868c3ff9a4143739eb6d7f0ff41` |

The dimensions are respectively:

```text
273  900328 variables  2449260 clauses  58 core clauses  73 core lemmas
274  900368 variables  2449370 clauses  58 core clauses  73 core lemmas
275  900160 variables  2448798 clauses  53 core clauses  61 core lemmas
```

## Independent proof replay

The quarantine manifest was replayed in full.  A separate verifier then bound
the three quarantine rows to the main `UNKNOWN:126` rows and independently
reran, for every case:

1. full-CNF/full-proof DRAT verification;
2. literal core-subset verification; and
3. reduced-core/core-lemmas DRAT verification.

All nine checks passed.  The exact recheck hashes are in
[`summary.tsv`](scratch/r2_k17_exact3664_anomaly273_275_20260802/summary.tsv),
SHA-256
`019f2b29870de39ed8fe591a62c3e1659672e86562813c4c6c628235d7013235`.
The independent theorem payload has SHA-256
`33cecb716278ed75a6c6be37e6a58c913fec5f3026fb0036a6114c79682262a7`,
and its artifact manifest has SHA-256
`ac2124b818f6a1d2702b34713f2b87fa8ea48e25b05940b41742d8a86e49be1c`.

The recheck performed no solver rerun and did not touch any other exact3664
case.  It used idle H100 CPUs `28`, `29`, and `33` for the proof checkers.

## Wrapper diagnosis

The main worker was rewritten in place from SHA-256 prefix `97cfbdd5` to
`cc41a02a` while the eight-way `xargs` launch was live.  The patch timestamp
`20:04:17.100Z` straddles these three cases.  Their original Kissat logs each
contain `s UNSATISFIABLE` and `c exit 20`, but the shell subsequently attempted
to execute its own `kissat.out`, producing permission-denied exit `126`.
Contemporaneous launcher errors also include an unmatched quote and unbound
`SUBSET` references.  No DRAT stage ran in the original three workers.

Therefore the main rows alone are nonfinal; any combined 3,664-case manifest
must explicitly replace cases `273..275` with the quarantine rows and record
their origin.

## Scope

The CNFs have `rank10_rows_encoded=false`.  This audit proves UNSAT only for
the three exact cyclic relaxed-residence functional-q1 formulas.  It makes no
rank10-selection, topology, ranks 11--17, rooted-state, residence, or compiler
claim.
