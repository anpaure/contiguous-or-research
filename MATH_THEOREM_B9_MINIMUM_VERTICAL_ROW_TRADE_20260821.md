# The minimum static row trade to a fully vertical b=9 wreath factor

**Date:** 2026-08-21  
**Method:** exact finite exhaustion; the search space and pruning argument
are explicit below  
**Status:** exact b=9 theorem; no asymptotic claim

## 0. Result

Put \(b=9,r=4\), and let \(F_0\) be the canonical fourteen-row MSW exact
middle-wreath factor.  For an exact factor \(F\), let \(h_q(F)\) be the
number of rank-\((4-q)\) sets which do not occur as cyclic windows in its
rows.

### Theorem 0.1

Among all exact middle-wreath factors \(F\) on \([9]\) with
\(h_1(F)=0\), the maximum possible overlap with \(F_0\) is nine rows.
Equivalently, the minimum static row-replacement distance from \(F_0\) to
q=1 completeness is exactly five.

The same optimum holds after requiring simultaneous completeness at every
lower depth:

\[
                  (h_1(F),h_2(F),h_3(F))=(0,0,0).       \tag{0.1}
\]

Consequently the coordinatewise Pareto minimum of the b=9 all-depth hole
profile is feasible and equals \((0,0,0)\).  In particular, there is no
finite-dimensional invariant obstruction to the multidepth target.

This is a theorem about the number of canonical rows replaced in one static
trade.  It is not a claim about the minimum number of balanced \(C_8\)
switches.  A separate audited construction reaches an all-depth-complete
factor from \(F_0\) in six general balanced \(C_8\) switches, but minimality
of that path length is not asserted here.

## 1. The five-row witness

Delete the following five unoriented cyclic orders from \(F_0\):

\[
\begin{array}{l}
1\ 3\ 4\ 2\ 9\ 7\ 5\ 6\ 8,\\
1\ 4\ 3\ 7\ 2\ 6\ 5\ 8\ 9,\\
1\ 4\ 5\ 3\ 2\ 8\ 6\ 7\ 9,\\
1\ 5\ 3\ 2\ 9\ 7\ 6\ 4\ 8,\\
1\ 6\ 4\ 3\ 2\ 8\ 7\ 5\ 9,
\end{array}                                                \tag{1.1}
\]

and insert

\[
\begin{array}{l}
1\ 3\ 5\ 2\ 9\ 7\ 4\ 6\ 8,\\
1\ 4\ 3\ 2\ 5\ 8\ 6\ 9\ 7,\\
1\ 4\ 3\ 8\ 2\ 6\ 7\ 9\ 5,\\
1\ 4\ 9\ 3\ 2\ 7\ 6\ 5\ 8,\\
1\ 6\ 4\ 3\ 2\ 7\ 8\ 5\ 9.
\end{array}                                                \tag{1.2}
\]

The rank-four window multisets of (1.1) and (1.2) agree.  Thus the
replacement preserves the exact middle factor.  Direct enumeration of the
cyclic windows of the resulting fourteen rows gives (0.1).  Rank one is in
fact automatic: every cyclic order contains every singleton.

## 2. Why four rows cannot suffice

There are exactly

\[
                         {(9-1)!\over2}=20160              \tag{2.1}
\]

unoriented cyclic orders on \([9]\).  Represent each by its unique rotation
beginning with 1 whose second entry is smaller than its last.

Suppose an exact factor \(F\) retains all canonical rows outside a set
\(R\subseteq F_0\), with \(|R|=t\).  Let \(U_R\) be the union of the
rank-four windows in the rows of \(R\).  Exactness of \(F_0\) gives
\(|U_R|=9t\).  Every retained canonical row already owns every rank-four
target outside \(U_R\).  Hence every inserted row must have all nine of its
rank-four windows inside \(U_R\), and the inserted rows must partition
\(U_R\).

This turns the lower bound into a finite exact-cover exhaustion.  For every
\(R\) with \(1\le |R|\le4\):

1. list every one of the 20160 rows whose rank-four window set is contained
   in \(U_R\);
2. recursively choose the least uncovered target of \(U_R\), and branch
   over rows containing it whose other windows are still uncovered; and
3. at every completed exact cover of \(U_R\), restore the retained rows and
   test the rank-three support.

There are

\[
 \sum_{t=1}^4\binom{14}{t}=1470                         \tag{2.2}
\]

sets \(R\).  The exhaustion reaches 3218 completed exact replacement covers,
and none covers all 84 rank-three targets.  Thus every q=1-complete exact
factor replaces at least five canonical rows.  The witness in Section 1
attains five and is complete also at q=2 and q=3, proving Theorem 0.1.

The branch rule is exhaustive rather than heuristic: in any exact cover,
the least currently uncovered target belongs to exactly one selected row,
and selecting that row leaves another instance of the same subproblem.

## 3. Scope

The theorem proves exact b=9 feasibility, the complete Pareto profile, and
minimum static row-replacement distance from the canonical factor.  It does
not prove uniqueness of the five-row trade, minimum balanced-switch distance,
or an infinite family with \(\sum_{q\le H}h_q=o\!\left(\binom{2r+1}r\right)\).

## 4. Checker

The exact audit is

```text
scratch/audit_b9_minimum_vertical_row_trade_20260821.py
```

It constructs all 20160 rows, constructs the canonical MSW factor, performs
the complete search in Section 2, and checks every rank of the five-row
witness.  Its H100 output is

```text
B9_MINIMUM_VERTICAL_ROW_TRADE_AUDIT_PASS {
  'canonical_removed_sets_checked': 1470,
  'exact_replacement_covers_checked': 3218,
  'minimum_row_replacements': 5,
  'final_holes_q1_q2_q3': (0, 0, 0)
}
```

The independent CP-SAT model
`scratch/research_b9_minimum_row_trade_to_vertical_20260821.py` returns the
same optimum for q=1 alone and for the joint q=1,q=2 constraints; it is
corroboration, not part of the proof above.
