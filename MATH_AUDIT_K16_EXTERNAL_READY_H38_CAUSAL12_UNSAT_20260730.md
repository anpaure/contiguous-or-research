# K16 external-ready H38 causal-12 repair: exact UNSAT

## Source state

The authenticated length-12873 word
`scratch/k16_Hfinal_externalblockers_v2_h38.word` has SHA-256

`575f9e5b3453618636918cb410cff88390e12c2dd09fc4d635820b40e1bd4880`.

It has exactly 38 missing masks, but contains genuine position-0-avoiding
singleton witnesses of the two finish blockers:

- `0x4879` at position 111;
- `0x6879` at position 6522.

An independent witness backtrace attributes every one of the 37 collateral
holes, besides the original `0x2c6d` hole, to the twelve-position support

`[110,111,112,666,667,670,4299,4301,6522,6523,6526,9958]`.

## Exact question

Keep all other 12,861 cells fixed and allow each of those twelve cells to be
an arbitrary nonzero 16-bit mask.  Does any assignment make the entire word
universal?

This scope is stronger than freezing the two planted singleton witnesses: the
values at positions 111 and 6522 may also change, so external witnesses are
allowed to spread over intervals inside the twelve-position support.

## Encoding and verdict

The exact dynamic-substitution CNF has:

- 1,853 variables;
- 29,824 clauses;
- 94 repair targets;
- 1,649 exact witness terms;
- no structurally impossible target before solving.

CaDiCaL returned `s UNSATISFIABLE`.  The retained DRAT proof was checked by
`drat-trim`, which returned `s VERIFIED` after 62.174 seconds.  The verified
core uses 28,961 of 29,824 input clauses and 1,272,085 of 1,618,536 lemmas.

Frozen artifacts are under
`scratch/k16_external_ready_h38_repair12_unsat_20260730/`:

- original CNF SHA-256
  `c71b7e94d6dabbd7326adb09c9e14dc2660564e424f3d8064caae23038b38bfa`;
- phase-normalized CNF SHA-256
  `9f5be815fd7a5f0f11bda9df592091b1cbb5c6387d9ece47d0e801486015fc70`;
- compressed DRAT proof SHA-256
  `53b207e7172271b1b15f5a5b7db0ad2e73cd9c4468557a89a50268d4010a740c`;
- decompressed DRAT content SHA-256
  `51790b463bd39b834465a1418965c694439da235636f9553eab62cbd78965726`;
- proof-check transcript SHA-256
  `9e38b71ca2f920a38060646b9afdd5b37380abb0596a9529aab41a33f419beb6`.

The deterministic phase transform was centered at the H38 source and its
all-false assignment violated exactly the 38 source-hole clauses.

## Consequence

The external witnesses are real, but the causal support of their collateral
damage is not a sufficient repair support.  Any completion from this state
must change at least one cell outside the twelve positions above.  In
particular, a valid construction needs a donor/reserve move, not merely local
repair where the holes' existing witnesses were destroyed.
