# Independent audit of the nested vertical-wreath flag

## Verdict

`NESTED_VERTICAL_WREATH_FLAG.md` is correct within its stated scope.

The explicit `Q_5 < Q_7 < Q_9` Catalan flag is valid.  Exhaustion confirms
that the fourteen-row `Q_9` certificate has exactly two projected exact
`Q_7` factors and that each has exactly 35 projected exact `Q_5` subflags.
All reported projected factors are fully vertical, not merely exact in their
middle rank.

The two-coordinate sector formulas are exact.  They prove that a lift made
only from maximum-separation insertions is impossible and that a saturated
recursive lift with `C_{m-1}` inherited maximum-type rows requires new rows
of mean type `(m+1)/3`.  The `Q_9 -> Q_11` schedule with fourteen type-five
rows and twenty-eight type-two rows has the correct sector counts.

No `Q_11` factor has been constructed here; satisfiability of the finite
exact-cover formulation remains open.

## 1. Independence of the finite verification

The checker

```text
scratch/check_nested_vertical_wreath_flag.py
```

reads only `m4_fully_vertical_wreath_factor.txt`.  It does not import the SAT
generator, the original `Q_9` verifier, or any claimed projected rows.

For an order on `2t+1` points it constructs every cyclic interval literally.
It recognizes an exact factor only when the complete occurrence list at
rank `t` has the same size and support as the entire target rank.  It then
checks every other proper rank separately.

Its exhaustive search spaces are:

* `binom(9,2) binom(14,5)=72072` projected `Q_7` candidates;
* `binom(7,2) binom(5,2)=210` projected `Q_5` candidates inside each
  discovered `Q_7` core.

The output is

```text
projected_Q7_factors [((2, 9), (2, 3, 5, 6, 11)), ((5, 6), (1, 5, 7, 9, 14))]
Q7_core (2, 9) (2, 3, 5, 6, 11) projected_Q5_flags 35
Q7_core (5, 6) (1, 5, 7, 9, 14) projected_Q5_flags 35
distinguished_flag_Q9_rows (2, 3, 5, 6, 11)
distinguished_flag_Q7_rows (2, 3)
Q9_pair_type_hist {1: 4, 2: 4, 3: 1, 4: 5}
Q7_pair_type_hist {1: 2, 2: 1, 3: 2}
Q5_rows ((4, 7, 6, 8, 5), (5, 7, 8, 4, 6))
Q9_to_Q11_type_ledger {5: 14, 2: 28} sectors (126, 252, 84)
PASS
```

## 2. Audit of the type formula

Put the two marked symbols at cyclic distance `h<=m` in a cycle of length
`2m+1`.

* A length-`m` window contains both symbols for exactly `m-h` starts.
* The total marked-symbol incidence over all windows is `2m`, so exactly
  `2m-2(m-h)=2h` windows contain one symbol.
* The remaining count is `2m+1-(m-h)-2h=m+1-h`.

This independently recovers (3.1).  Summing the one-symbol count over an
exact factor gives

\[
 2\sum_h h r_h=2\binom{2m-1}{m-1},
\]

which is (3.3).  Subtracting `C_{m-1}` type-`m` rows and using

\[
 C_m/C_{m-1}=2(2m-1)/(m+1)
\]

gives both equations in (4.1).  The checker evaluates all resulting integer
identities for `2<=m<=12`.

For `m=5`, a type-five row contributes `(1,10,0)` and a type-two row
contributes `(4,4,3)`.  Therefore

\[
 14(1,10,0)+28(4,4,3)=(126,252,84),
\]

which equals

\[
 \left(\binom95,,2\binom94,,\binom93\right).
\]

## 3. Audit of the insertion candidate counts

For a fixed unoriented old nine-cycle, a type-five extension has four old
symbols on the short arc between the two new symbols.  Choosing the cut gives
nine possibilities; choosing which new symbol starts that short arc gives
two.  Hence there are 18 extensions per inherited row and `14*18=252`
inherited candidates.

For a type-two eleven-cycle, orient the cycle uniquely so that `a` is the
origin and `b` is two steps clockwise.  Choose the one old symbol between
them and order the remaining eight symbols: `9*8!=9!=362880` candidates.

The coverage-constraint counts are also correct:

\[
 \binom{11}{5}=462,
 \qquad
 \sum_{r=1}^4\binom{11}{r}=11+55+165+330=561.
\]

## 4. Scope and remaining risk

The sector ledger is necessary for exact middle coverage but not sufficient.
The candidate rows must still be selected so that:

1. every middle target occurs exactly once;
2. every lower target occurs at least once;
3. the fourteen inherited choices remain compatible with the twenty-eight
   new choices.

No assertion in the note treats the numerical ledger as a proof of those
conditions.  Conversely, failure of the one-type `r_2=28` restriction would
not refute the general lift: equation (5.3) lists all other admissible type
profiles.  The unrestricted two-coordinate recursion therefore remains an
open construction problem.

