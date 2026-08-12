# `k=17`: the zero-singleton dense bank has a four-seam q1 bow-tie obstruction

Date: 2026-08-01  
Status: exact human-readable obstruction plus DRAT-verified UNSAT core for the
orientation-coupled q1 matching of the current 7,612-piece dense bank.  This
rejects that fixed bank, not the protected factor family or `nu(17)=24313`.

## 1. The apparently perfect incumbent

The cut-choice incumbent

```text
scratch/k17_dense_refinement_zerozero_bank_20260801.tsv
```

was continued until its literal rebuild reached

```text
COMMON_ORIENTATION_ZERO relaxed=0
RANK10_ZERO relaxed=0
zero_colours=0 zero_tail_states=0 zero_head_states=0
match_piece_TH=7612 match_piece_TC=7612 match_piece_CH=7612
```

Its retained bank SHA-256 is

```text
5b4fe2d1a0125ea25f6fbb4b9259a6d2ee2007cd4ba55ac0aa4a6f23aa6bad8f
```

Thus every local orientation row and every pairwise physical projection is
perfect.  The next exact question is whether one can choose 7,612 seams which
simultaneously use every tail piece, head piece, selected rank-eight colour,
and one common orientation of every physical piece.

## 2. Exact q1 formula and verdict

For every physical piece `P`, introduce two orientation variables and choose
exactly one.  For every relaxed-resident atomic seam `e`, introduce a seam
variable.  Impose:

1. one outgoing seam from the chosen orientation of every piece;
2. one incoming seam to that same orientation;
3. exactly one seam of every selected rank-eight colour.

The formula has

\[
 891,633\text{ variables},\qquad
 2,416,757\text{ clauses},\qquad
 228,730\text{ physical seam variables}.
\]

Kissat reports UNSAT.  A retained text DRAT proof verifies independently:

```text
c 14 of 2416757 clauses in core
c 5 of 15729 lemmas in core using 21 resolution steps
c 0 RAT lemmas in core
s VERIFIED
```

The proof therefore does not hide a large combinatorial failure.  Its core is
one four-seam bow tie.

## 3. Decoded physical core

Write

```text
A = piece 1330
B = piece 7017
C = piece 2538
c = colour 984, lower mask 18782
d = colour 999, lower mask 19038
```

The only core seams are

| name | tail | head | colour | upper mask |
|---|---|---|---|---:|
| `x` | `A+` | `B+` | `c` | 19326 |
| `y` | `C-` | `B+` | `d` | 19326 |
| `z` | `B-` | `A-` | `c` | 19326 |
| `w` | `B-` | `C+` | `d` | 19326 |

Here `+/-` denotes the two orientations of a physical piece.  Both colours
have degree exactly two inside the complete q1 atlas relevant to the core.

### Theorem 3.1 (bow-tie obstruction)

No orientation-consistent coloured cycle cover contains exactly one seam of
each selected colour.

#### Proof

Colour `c` requires `x` or `z`; colour `d` requires `y` or `w`.

If `x` is chosen, `y` cannot be chosen because both enter the single incoming
socket of `B+`.  Hence `d` must use `w`.  But `x` requires orientation `B+`
while `w` requires `B-`, contradicting the one-orientation rule for `B`.

If `z` is chosen, `w` cannot be chosen because both leave the single outgoing
socket of `B-`.  Hence `d` must use `y`.  Now `z` requires `B-` while `y`
requires `B+`, the same contradiction.

These cases exhaust colour `c`.  Therefore no cover exists.  \(\square\)

In the undirected physical-socket quotient, `x,z` are the two directed views
of one edge labelled `c`, and `y,w` are the two directed views of one edge
labelled `d`.  Both physical edges meet the same socket of `B`.  Thus the
14-clause core is exactly a two-colour/one-socket Hall obstruction: colour
exactness requires both edges while socket degree one permits at most one.
The orientation proof above is its unquotiented four-seam form.

All four seams happen to have the same rank-ten upper mask.  Rank-ten
singleton completeness therefore does not detect the obstruction.

## 4. What this changes

The fixed dense bank is conclusively rejected at q1 despite:

* zero lower-colour singleton rows;
* zero physical endpoint rows;
* zero common-orientation singleton rows;
* zero rank-ten provider rows;
* three perfect physical two-shore matchings.

This is a concrete instance of the general functional three-resource parity
warning.  It also makes the next finite repair extremely small: a cut change
must add an alternative seam for colour `c` or `d`, change the relevant
orientation incidence at `B`, or replace one of the selected colours.  After
that change the exact q1 formula can be resolved and any next core returned.
This is a natural finite CEGAR loop on cut choices.

Connectivity, exact global residence, ranks 11--17, and the terminal compiler
remain downstream even after q1 becomes SAT.

### 4.1 Direct core-piece substitutions do not suffice

The three core pieces arise from base pieces 665, 3509 and 1269, using cuts
3558, 18893 and 6753.  Their complete internal alternatives give

\[
                    6\cdot4\cdot10=240
\]

cut combinations.  Literal replay finds 20 combinations preserving zero q1
singleton rows, zero common-orientation rows and zero rank-ten rows.  The
exact q1 formula is UNSAT for all 20.  Thus changing only the three visible
core split points does not close the carrier; a provider outside the core is
needed.

### 4.2 One global provider change breaks the first core, exposing a second

An exact single-cut pricing oracle examines 16,667 replacements of the full
bank.  Of these, 13,027 preserve all local zero rows and 21 add a provider for
one of the bow-tie colours.  The strongest move changes base piece 1268 from
cut 6744 to 6751 and raises mask 19038's seam degree from two to ten.

The resulting bank

```text
scratch/k17_dense_bowtie1_repair_bank_20260801.tsv
SHA-256 423a759cd9d180a23f221d8ebc6ea388112394bb2c7b028f12fd1668f425803b
```

retains every local zero row and destroys the first bow tie.  Its exact q1
formula is nevertheless UNSAT.  The verified second core has 15 original
clauses and seven lemmas and decodes as follows:

```text
pieces: 2263, 2264, 3516
single colour: 839, lower mask 15635
seams:
  2263+ -> 3516+
  2264- -> 3516+
  3516- -> 2263-
  3516- -> 2264+
```

Each of pieces 2263 and 2264 must choose an orientation, and either
orientation forces one of these four seams.  Therefore two seams of the same
colour are required.  Trying to redirect one through the opposite side of
piece 3516 instead forces both orientations of that central piece.  This is
another constant-size functional-Hall obstruction.

The CEGAR mechanism is therefore validated but not finished: a cut change
can kill one exact core while preserving all local rows, and the next core is
again tiny and explicitly priceable.

## 5. Artifacts

Remote retained root:

```text
/home/amodo/or15/work/root_k17_dense_zero265_q1_matching_20260801
```

```text
q1.cnf
  SHA-256 545d3d00d9b13df0943f5454757bfe493920652dc1690be363c3ea3949185269
q1.drat
  SHA-256 ed1f221870d3f11db20e12a84c3f7685255975bcffc33482f19e5ad4ada5d590
scratch/k17_dense_zero265_q1_core_20260801.cnf
  SHA-256 428296575b753910f48c76a0e74c726592da0509f32f4f226206f6812ba18aca
scratch/k17_dense_zero265_q1_core_20260801.drat
  SHA-256 abfc7aa2436570adfc88fa5d5a606768c428cd6d84f69aa49a98a84232b8f1b4
scratch/k17_dense_zero265_q1_dratcheck_20260801.out
  SHA-256 6c8c891a1dddab4832c3a3d55efc021ddc8e8a7f9c935c505d9aea6cd1515880
scratch/k17_dense_refinement_zerozero_bank_20260801.tsv
  SHA-256 5b4fe2d1a0125ea25f6fbb4b9259a6d2ee2007cd4ba55ac0aa4a6f23aa6bad8f
scratch/k17_dense_refinement_zerozero_literal_audit_20260801.out
  SHA-256 2a5966273d09664752457a007ab1fc4a6625ee5006f7487ac17f9dbfcfa7f2e1
scratch/k17_dense_refinement_zerozero_search_audit_20260801.out
  SHA-256 199ab8864d35586dd7e7c97f5131562165c63bdeb47d36b0d23e45f2b8695cef
scratch/k17_dense_bowtie1_second_core_20260801.cnf
  SHA-256 23a2dc891d06e9b842c79f53d2854bd6b4e581702bc2dbcf7b9efcdabbb51107
scratch/k17_dense_bowtie1_second_corecheck_20260801.out
  SHA-256 1d97d08835771aceaddb27d570075f69424d28a22f19816f177b4a9fb402f65f
```
