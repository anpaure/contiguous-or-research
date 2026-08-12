# K16 external-ready H38 plus the unique zero-debt donor: exact UNSAT

## Scope

Start from the authenticated 38-hole, external-ready length-12873 state of
SHA-256

`575f9e5b3453618636918cb410cff88390e12c2dd09fc4d635820b40e1bd4880`.

Its complete arbitrary-value causal support consists of positions

`[110,111,112,666,667,670,4299,4301,6522,6523,6526,9958]`.

An exhaustive one-edit provider atlas over all 12,860 outside positions proves
that position 6524 is the **unique** outside position admitting a zero-new-debt
provider move.  This audit therefore opens exactly that one additional donor
and asks whether arbitrary nonzero assignments on the resulting 13-position
support can make the word universal.

## Encoding

The exact dynamic-substitution instance has:

- 2,177 variables;
- 37,093 clauses;
- 94 repair targets;
- 1,956 exact interval-witness terms;
- no structurally impossible target before solving.

The source-centered polarity transform is equisatisfiable; its all-false
assignment is the 38-hole source state.

## Verdict

CaDiCaL returned `s UNSATISFIABLE`.  The retained DRAT proof was independently
checked by `drat-trim`, which returned `s VERIFIED` after 702.484 seconds:

- 36,736 of 37,093 input clauses in the proof core;
- 9,084,841 of 11,441,361 lemmas in the core;
- 586,081,681 resolution steps;
- zero RAT lemmas.

Remote frozen directory:
`/home/amodo/or15/work/root_k16_external_ready_h38_expanded13_20260730/`.

Hashes:

- original CNF:
  `73a426dcb8586ef70dc23902d52caad628a3b63190e411b24f53b144ded8b715`;
- phase-normalized CNF:
  `4fd869f73ddb6b19b1874875adcc8a5e801810d5c37f04b3fe5e2b96aae46bab`;
- DRAT proof:
  `35c7754ffe5c773c4b65d65b560bcb70f3f8e612730275c35c7d75bf18008d19`;
- proof-check transcript:
  `a68356b379f4f0f4121760492b90ae388709543628a9abfa530c798eeb27a4d3`.

## Consequence

The causal 12-cell repair support is insufficient, and even its unique
zero-debt outside donor is insufficient.  Any completion from this state must
use at least two outside donor positions, or a donor whose first move creates
temporary debt.  The next exact supports therefore add the best coherent
debt-bearing donor at position 668 or an adaptive donor such as position 81
selected from the authenticated 22-hole descendant.

This is consistent with a separate exact monotone sweep: all 46 zero-debt
first donor choices from that 22-hole descendant reach 21 holes, and every one
then has no further zero-debt provider.  A successful path must contain a
simultaneous multi-edit or a temporary-debt step.
