# A bulk first-derivative compiler and a second exact `k=11` word

Date: 2026-07-27

## 1. Result

> **Scope.**  This is an exact and substantially simpler compiler for the
> final `k=11` certificate, but it is not a uniform asymptotic reduction.
> It places every mask of rank at most `s=r-d` literally, which requires
> `sum_{j<=s} binom(k,j) <= W+d`.  This already fails at `k=9` (`129>128`)
> and eventually fails by a factor `Theta(sqrt(k))`.  The row-graded general
> replacement and the exact good-cut rigidity theorem are in
> `MATH_GOOD_CUT_PCSH_20260727.md`.

The selected-pin compiler can be replaced, for the final `k=11` middle
cycle, by a simpler cyclic construction:

1. take the cyclic depth-3 erosion `P` of the middle cycle;
2. choose a canonical coordinate core `C subseteq P` satisfying `DC=DP`;
3. solve one sandwich matching for the masks of ranks at most 3;
4. cut at an exterior-safe edge and append the first three entries.

The resulting word has length 465 and covers all 2,047 nonempty masks.  Its
SHA-256 is

```text
bda651d3e40d0920d3e6ed12e6a2091e477695d8ad7f6bd186b831f087cf136a
```

and the file is

```text
scratch/sigma_calibration_bulk_k11_465.word
```

The construction works because preserving the **first** Boolean derivative
preserves every later derivative automatically.  This collapses the entire
intermediate-pin hierarchy.

## 2. First-derivative collapse

For a cyclic word of sets `A=(A_j)`, write

\[
(DA)_j=A_j\cup A_{j+1},
\]

with cyclic indices.

### Theorem 1 (first-derivative sandwich)

Let `C,A,P` be cyclic words of the same length such that

\[
C_j\subseteq A_j\subseteq P_j\quad\text{for every }j,
\qquad DC=DP.
\tag{2.1}
\]

Then

\[
DA=DP,
\qquad
D^tA=D^tP\quad\text{for every }t\ge1.
\tag{2.2}
\]

#### Proof

Monotonicity of union gives

\[
DC\subseteq DA\subseteq DP.
\]

The two outside words are equal by hypothesis, proving `DA=DP`.  Applying
`D` repeatedly proves the second assertion.  □

Thus no particular occurrence of an intermediate mask has to be pinned.  It
is enough to preserve the entire first derivative of the erosion word.

## 3. A canonical core with `DC=DP`

Fix one coordinate `x`.  Its support in the cyclic word `P` is a union of
cyclic runs.  For each proper run

\[
[a,b]=a,a+1,\ldots,b,
\]

put `x` in `C` at

\[
a,a+2,a+4,\ldots,
\]

and also at `b` if it was not already selected.  Do this independently for
every coordinate.

### Lemma 2 (run-alternating core)

The resulting word satisfies

\[
C_j\subseteq P_j,
\qquad DC=DP.
\tag{3.1}
\]

#### Proof

Again work coordinatewise.  An edge with neither endpoint in the support of
`x` contributes `x` to neither derivative.  At each boundary edge of a run,
the unique supported endpoint is selected.  On the internal path of a run,
the alternating set, with the final endpoint added, is a vertex cover.
Therefore every cyclic edge having `x` in at least one endpoint has `x` in a
selected endpoint.  This is exactly `DC=DP`.  □

If a group acts on coordinates and acts on the oriented position cycle by
rotations, this construction is equivariant: run starts, parity from the
start, and run ends are all preserved by the action.

## 4. Exact surplus Hall after eliminating the deepest rank

Suppose every `P_j` has rank `s` and every `s`-set occurs.  For an `s`-set
`Q`, put

\[
R_Q=\{j:P_j=Q\},
\qquad \mu(Q)=|R_Q|\ge1.
\]

Let

\[
\mathcal L_{<s}=\{S:1\le |S|<s\}.
\]

Join `S in mathcal L_{<s}` to position `j` when

\[
C_j\subseteq S\subseteq P_j.
\tag{4.1}
\]

### Theorem 3 (surplus-Hall criterion)

There is a sandwich matching for **all** targets of ranks at most `s` if and
only if, for every `mathcal A subseteq mathcal L_{<s}`,

\[
|\mathcal A|
\le
F(\mathcal A)
:=
\sum_{Q\in\binom{[k]}s}
\min\big\{\mu(Q)-1,\ |N(\mathcal A)\cap R_Q|\big\}.
\tag{4.2}
\]

#### Proof

Every rank-`s` target `Q` can use only a position in its own block `R_Q`, and
the blocks are disjoint.  Consequently the lower-rank targets must be
matched while using at most `mu(Q)-1` positions of each block; the remaining
position is then assigned to `Q`.

Conversely, any matching of the lower targets respecting these block
capacities leaves a position for every `Q`, so it extends to all ranks.
The capacitated Hall theorem, or equivalently max-flow/min-cut with block
capacity `mu(Q)-1`, says that such a lower matching exists exactly when
(4.2) holds.  □

An equivalent and sometimes more transparent form is

\[
F(\mathcal A)
=|N(\mathcal A)|
-\#\{Q:N(\mathcal A)\cap R_Q=R_Q\}.
\tag{4.3}
\]

The correction term is the price of reserving one position for each deepest
target.

## 5. Symmetric witnesses reduce to the quotient

The function `F` in (4.2) is monotone and submodular: each summand is the
rank of a uniform matroid of rank `mu(Q)-1` evaluated on a neighbourhood
union.  Hence

\[
\delta(\mathcal A)=|\mathcal A|-F(\mathcal A)
\]

is supermodular.

If a finite group acts by automorphisms preserving `P`, `C`, and the blocks,
the minimal-deficient-set uncrossing proof in
`MATH_SYMMETRIC_HALL_UNCROSSING_20260727.md` applies verbatim: any failure of
(4.2) has a group-invariant witness.  For a free `Z_p` action, it is therefore
enough to check unions of target orbits, and every inequality divides by
`p`.

For `k=11`, `s=3`, the lower targets consist of one singleton orbit and five
pair-distance orbits.  There are only

\[
2^6-1=63
\]

nonempty quotient inequalities.

## 6. Universal-word corollary

Let `T` be a cyclic middle word and let `P` be its depth-`d` cyclic erosion.
If every coordinate run of `T` has length at least `d+1`, then the erosion
identity gives

\[
D^dP=T.
\tag{6.1}
\]

Assume:

1. the derivative rows `P,DP,...,D^dP` cover all required lower ranks;
2. the middle word and its higher derivatives cover all required upper
   ranks cyclically;
3. the surplus-Hall inequalities (4.2) hold for the run-alternating core;
4. there is an exterior-safe cut, meaning the upper windows deleted by the
   cut are not unique occurrences.

Use the matching from Theorem 3 to replace matched entries of `P` by their
target sets and leave unmatched entries equal to `P`.  Call the resulting
cyclic word `A`.  Theorem 1 gives

\[
D^tA=D^tP\quad(t\ge1),
\]

while every rank at most `s` occurs literally.  Cut `A` at the safe edge and
append its first `d` entries.  All cyclic derivative cells through depth `d`
remain present; exterior safety preserves the upper ranks.  The resulting
linear word is universal.

## 7. Exact `k=11` audit

The source middle certificate is

```text
scratch/sigma_sat_k11_allcentral_cap2.certificate.json
SHA-256 a23b8d6847dba4350cca8dc8b9da89519e77067e58c866422713115887aaf397
```

For this certificate, translation by one ground coordinate acts as rotation
by 252 positions on the 462-cycle.  The run-alternating core has rank profile

\[
1^{66}2^{231}3^{165}.
\]

All 63 quotient surplus-Hall inequalities hold.  The smallest nonempty
quotient margin is 2.  The same audit was run on two independent complete
shadow certificates:

| certificate | q1 cap | core rank profile | minimum quotient margin |
|---|---:|---|---:|
| final cap-2 | 2 | `1^66 2^231 3^165` | 2 |
| alternate seed 17 | 2 | `1^77 2^231 3^154` | 4 |
| cap-free seed 29 | 3 | `1^77 2^209 3^176` | 3 |

Thus cap 2 is not used by the bulk compiler theorem.

The generated word has entry profile

\[
1^{11}2^{57}3^{397},
\]

and 231 distinct entry values, exactly all masks of ranks 1--3.  Two
independent verifiers report 2,047/2,047 masks:

```text
scratch/sigma_calibration_harness
scratch/sigma_calibration_verify_or_suffix
```

The harness additionally reports the exact lower equality ledger

\[
1392=1023+369,
\]

with all 1,392 short cells below the middle rank and 1,023 distinct lower
masks.

Reproduction:

```sh
python3 scratch/sigma_calibration_bulk_surplus_hall.py \
  scratch/sigma_sat_k11_allcentral_cap2.certificate.json \
  --k 11 --delay 3 \
  --output-word scratch/sigma_calibration_bulk_k11_465.word

scratch/sigma_calibration_harness \
  11 scratch/sigma_calibration_bulk_k11_465.word

scratch/sigma_calibration_verify_or_suffix \
  11 scratch/sigma_calibration_bulk_k11_465.word
```

## 8. Exact scope: the boundary cannot be removed

The file

```text
scratch/sigma_calibration_k7_full_nonsym43.certificate.json
SHA-256 548d93cb92d08c0c3f4f8cb1ce874ad00312d4c3b7da9c11f6abb9636a25d3e9
```

is a `k=7`, delay-2 middle cycle with:

* complete lower and upper shadows through depth 2;
* residence at least 3;
* q1 upper load at most 2;
* 28 exterior-safe cuts.

Nevertheless an exact SAT encoding proves:

* the **cyclic** literal compiler is UNSAT (`210` variables, `518` clauses);
* among the 28 exterior-safe cuts, 24 linear PCSH instances are SAT and 4
  are UNSAT (cuts `0,1,14,29`).

Therefore neither of the following implications is true:

\[
\text{complete shadows + residence + cap 2}
\Longrightarrow \text{cyclic PCSH},
\]

\[
\text{exterior-safe cut}
\Longrightarrow \text{PCSH for that particular cut}.
\]

The boundary reservoir is a real part of the construction, not bookkeeping.
It repairs the cyclic deficiency at suitable cuts.

A bounded portfolio of 121 independently generated `k=7` cycles with the
same structural constraints was checked by the exact SAT auditor.  The
number of PCSH-successful cuts out of 28 had histogram

\[
15^8\;24^{13}\;28^{100}.
\]

Every cycle therefore had a successful safe cut; the worst cycles had 15.
This is finite evidence only, not a theorem.

Reproduction of the exact PCSH audit:

```sh
python3 scratch/sigma_calibration_exact_pcsh.py \
  scratch/sigma_calibration_k7_full_nonsym43.certificate.json \
  --k 7 --delay 2 --cyclic

python3 scratch/sigma_calibration_exact_pcsh.py \
  scratch/sigma_calibration_k7_full_nonsym43.certificate.json \
  --k 7 --delay 2
```

## 9. Remaining implication in the bulk regime

The selected-pin presentation is no longer needed for the final `k=11`
certificate.  Within the literal-bulk regime, the remaining structural
problem is sharper:

> Prove that a complete-shadow, residence-safe middle object has an
> exterior-safe cut whose `d` boundary positions absorb every deficit of the
> cyclic surplus-Hall system.

The `k=7` counterexample shows that quotient expansion alone cannot prove
this statement: the cyclic bulk may genuinely be deficient.  The positive
`k=11` margins show the opposite regime, where the bulk already has room and
the boundary is needed only for upper-shadow linearization.
