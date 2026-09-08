# K15-to-K17 diamond U-sector: a two-target opposite-choice no-go

Date: 2026-07-31  
Status: solver-free finite theorem with independent literal replay  
Scope: the `answers/k15.word` depth-three carrier and its occurrence-ordered old-rank-nine U-sector

## 0. Statement

Let \(A\) be the verified optimal K15 word `answers/k15.word`, and form its
flat middle carrier

\[
T_i=A_i\cup A_{i+1}\cup A_{i+2}\cup A_{i+3},
\qquad 0\le i<6435.
\tag{0.1}
\]

The \(T_i\) are exactly the 6435 rank-eight masks of \([15]\).  Put

\[
c_i=T_i\cup T_{i+1},qquad 0\le i<6434.
\tag{0.2}
\]

Every rank-nine mask occurs as some \(c_i\).  The proposed unmarked
\(U\)-sector of the K15-to-K17 diamond chooses one occurrence of every
rank-nine colour and orders the 5005 colours by the chosen physical
positions.

### Theorem 0.1

No such occurrence selection makes the resulting U-sector internally cover
all old-coordinate masks of ranks at least ten.

The obstruction consists of two targets and one repeated colour:

\[
c=0x1b7a,qquad O(c)=\{3837,4003\},
\tag{0.3}
\]

\[
0x1b7b\text{ forces }x_c=3837,
\qquad
0x1f7a\text{ forces }x_c=4003.
\tag{0.4}
\]

This is the K15 analogue of the independent opposite-choice core found in
the K16 carrier.

## 1. General opposite-choice certificate

Use the occurrence-selection notation and exact physical-interval criterion
from

`MATH_THEOREM_K17_PASCAL_OCCURRENCE_INTERVAL_AND_OPPOSITE_CHOICE_NOGO_20260731.md`.

### Lemma 1.1 (opposite-choice certificate)

Suppose a colour \(c\) has occurrence domain \(O(c)\), and two targets
\(S,S'\) have the following property:

- every exact feasible interval for \(S\) forces \(x_c\in P\);
- every exact feasible interval for \(S'\) forces \(x_c\in P'\); and
- \(P\cap P'=\varnothing\).

Then no occurrence selection covers both targets.

#### Proof

Any selection covering \(S\) has \(x_c\in P\), while any selection covering
\(S'\) has \(x_c\in P'\).  The two requirements are inconsistent. \(\square\)

The lemma is elementary, but its value is that exact interval enumeration
can certify its hypotheses without solving the full selection CSP.

## 2. Literal K15 carrier data

The carrier derived by (0.1) has SHA256

```text
bb453b77d4eb8d9b8199a3db9bec6d873367b23e9e1a8beb6a87b16a5ded4eb6
```

and the edge-colour occurrence histogram is

\[
1^{3676}\,2^{1229}\,3^{100}.
\tag{2.1}
\]

Thus there are 5005 distinct colours and 2758 nontrivial occurrence atoms.
Selecting the first occurrence of each colour gives 216 old upper holes.
Both targets in (0.4) are among those holes.

Around the first pivot occurrence the literal edges are

\[
\begin{array}{c|c}
i&c_i\\ \hline
3836&0x1b5e\\
3837&0x1b7a\\
3838&0x1b6b\\
3839&0x2b6b.
\end{array}
\tag{2.2}
\]

Around the second pivot occurrence they are

\[
\begin{array}{c|c}
i&c_i\\ \hline
4001&0x1f66\\
4002&0x1f72\\
4003&0x1b7a\\
4004&0x5b3a.
\end{array}
\tag{2.3}
\]

Here `0x1f72` is a multiplicity-one colour, while `0x1b7a` occurs exactly
at the two positions in (0.3).

## 3. The two forced targets

### Lemma 3.1

Every occurrence selection which covers

\[
S_-=0x1b7b
\]

chooses the pivot occurrence at position 3837.

#### Proof

Enumerate physical intervals using the exact individual-feasibility
criterion: unique blocker colours must lie outside, every repeated blocker
must retain an outside occurrence, and available good colours must cover the
target.

After shrinking endpoints which are unselected repeated blockers, the only
canonical good-endpoint interval is

\[
[3837,3838].
\tag{3.1}
\]

The two physical colours are `0x1b7a` and `0x1b6b`, whose union is
`0x1b7b`.  More strongly, retaining all redundant blocker endpoints gives
five exact interval signatures, and in every one target bit 4 has the sole
provider

\[
(0x1b7a,\text{ occurrence }3837).
\tag{3.2}
\]

Hence every witness forces \(x_c=3837\). \(\square\)

### Lemma 3.2

Every occurrence selection which covers

\[
S_+=0x1f7a
\]

chooses the pivot occurrence at position 4003.

#### Proof

The only canonical good-endpoint interval is

\[
[4002,4003].
\tag{3.3}

Its colours are the fixed `0x1f72` and the pivot `0x1b7a`, whose union is
`0x1f7a`.  Retaining redundant blocker endpoints gives twelve exact
interval signatures.  In every signature target bit 3 has the sole
provider

\[
(0x1b7a,\text{ occurrence }4003).
\tag{3.4}

Therefore every witness forces \(x_c=4003\). \(\square\)

Theorem 0.1 follows from Lemmas 1.1, 3.1, and 3.2.

## 4. The five-clause SAT core

The generalized fixed-blocker-gap model for the 216 first-selection holes
has

```text
2758 base occurrence atoms
296 interval guards
3054 total variables
4202 clauses
```

Its entire contradiction already appears in the following five input
clauses.  In that generated instance:

- atom 226 means selecting colour `0x1b7a` at 3837;
- atom 227 means selecting it at 4003;
- guard 2773 is target `0x1b7b`, interval `[3837,3838]`;
- guard 2785 is target `0x1f7a`, interval `[4002,4003]`.

The core is

\[
\begin{aligned}
&\neg226\vee\neg227,\\
&2773,\qquad \neg2773\vee226,\\
&2785,\qquad \neg2785\vee227.
\end{aligned}
\tag{4.1}
\]

Unit propagation derives both 226 and 227, contradicting the first clause.
Equation (4.1) is only a machine-coordinate rendering of the solver-free
proof in Section 3.

## 5. Independent replay

Run

```text
python3 scratch/audit_k15_to_k17_u_sector_opposite_choice_nogo_20260731.py
```

The script:

1. derives \(T=D^3A\) directly from `answers/k15.word`;
2. verifies the complete rank-eight carrier and all 5005 q1 colours;
3. verifies (2.1), the 216-hole first-selection baseline, and (0.3);
4. enumerates every exact feasible physical interval for both targets;
5. verifies the unique canonical intervals and the forced-provider claims;
6. returns `PASS_SOLVER_FREE_OPPOSITE_CHOICE_NOGO`.

The source word SHA256 is

```text
f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b
```

## 6. Exact scope for the diamond construction

For a two-coordinate Pascal/diamond lift from K15 to K17, the rank-nine
middle layer includes an unmarked shore

\[
U={ [15]\choose 9}.
\]

The theorem rules out the following sufficient architecture:

1. derive the K15 rank-eight carrier by (0.1);
2. represent every old rank-nine mask by one existing q1 edge occurrence;
3. order the U-sector by those selected physical positions; and
4. require that U-sector itself supply every old-coordinate upper target.

It does **not** rule out:

- a different optimal K15 source word or carrier;
- rethreading or switching the carrier before selecting occurrences;
- an arbitrary ordering of the old rank-nine masks not inherited from q1
  positions;
- a multi-component U-sector with additional old-only seam witnesses;
- a diamond braid whose old-only targets are supplied by another unmarked
  component; or
- the equality \(\nu(17)=B(17)\).

## 7. Consequence

The K15 and K16 occurrence decks independently exhibit the same failure
mode: every upper target is locally plausible, but a repeated q1 colour is
the unique provider in two distant windows which demand opposite
occurrences.  Therefore “choose one occurrence of every q1 colour” is not a
uniform Pascal induction theorem, even on solved optimal parents.

The next constructive filter should explicitly eliminate opposite forced
literals before running Hall, LLL, or SAT.  For this K15 source, any repair
must alter at least one neighborhood in (2.2)--(2.3), change the pivot
multiplicity, or abandon physical occurrence ordering for the U-sector.

