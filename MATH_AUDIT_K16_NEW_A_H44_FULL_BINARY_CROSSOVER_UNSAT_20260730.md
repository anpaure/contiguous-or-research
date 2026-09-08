# K16 new-A / canonical-H full binary crossover: exact UNSAT

## Scope

Let `H` be the authenticated length-12873 word obtained by deleting position
1 from the verified length-12874 certificate.  Its sole missing mask is
`0x2c6d`.  Let `A` be the independently replayed length-12873 compound
reverse/provider word of SHA-256

`a92509fd4f60490588973e7a70d457b369e4b0192a65f3de7adef105727e33fa`,

whose sole missing mask is `0xa86d`.  The two words differ at exactly 44
positions.

This audit asks the complete binary-crossover question: keep every other cell
equal to `H`, and at each of the 44 differing positions choose independently
either the `H` value or the `A` value.  Thus all `2^44` literal crossovers are
covered.  This does **not** quantify over arbitrary third values at those
positions or edits outside the 44-position support.

## Encoding

The exact dynamic-substitution CNF for the 44-position support has 23,863
variables and 361,396 clauses before parent restriction.  One selector was
added per position and every mapped value bit was equated to the corresponding
cell of exactly one parent.  The resulting DIMACS instance has:

- 23,907 variables;
- 362,147 clauses;
- 751 appended parent-domain clauses.

The parent-domain transformer is
`scratch/restrict_dynamic_cnf_to_two_parents_20260730.py`.  The 44 positions
are recorded in `scratch/k16_newA_vs_H_44_positions_20260730.txt`.

## Verdict and proof

Kissat returned `s UNSATISFIABLE`.  The retained DRAT proof was independently
checked by `drat-trim`, which returned `s VERIFIED`; verification took 0.302
seconds.  The checker reduced the proof to 139 input clauses and one core
lemma.

Frozen artifacts are under
`scratch/k16_newA_H44_binary_crossover_20260730/`:

- `binary_parents.cnf`, SHA-256
  `9c3f7340c4452ee8c778cbee0be04a532ae808f1b03cd5aca545a87cc34d9bf3`;
- `binary_parents.drat`, SHA-256
  `abd1069f3df06c52f35abe13b93fc7b75f6135f14dda5eb71271c5fbb1680d50`;
- `binary_parents.dratcheck`, SHA-256
  `cce05f663ea66c7a31dfae702d1afcdd27552a938dac81d22a5cbd02f5a7a1e1`;
- `binary_parents.out`, SHA-256
  `b022e7184efcb8e36d4ee2f5f56df927e044b4ed0275e19ec0a8651125938333`;
- `binary_parents.selectors`, SHA-256
  `fe2dadee932cc77d3ed1b36ea51c42e1493b7341280af6997190fe93ff7f82dd`.

## Consequence

The new 44-edit basin is structurally distinct, but literal cellwise mixing
with the canonical deletion basin cannot close the coefficient-one gap.  Any
successful use of this support must assign at least one cell a value occurring
in neither parent, or must edit outside this support.  The separate unbounded
44-position CNF tests the first alternative exactly and remains logically
stronger than this crossover theorem.
