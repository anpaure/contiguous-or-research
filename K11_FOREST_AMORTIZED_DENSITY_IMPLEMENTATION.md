# Amortized six-subcube comparator in the unrestricted `k=11` SAT generator

## Scope

The optional `K11_FOREST_LOCAL_DENSITY_PB=1` module in
`k11_forest_sat.cpp` previously imposed

\[
252n_1+126n_2+56n_3+21n_4+6n_5+n_6\ge12936.
\]

The audited amortized subcube-density theorem strengthens this standalone
comparator to

\[
252n_1+126n_2+56n_3+21n_4+6n_5+n_6\ge14322.
\]

Only the constant and its explanatory comment were changed.  The exact
one-hot popcount, weighted additions, and unsigned comparator are unchanged.
Both constants use fourteen bits, so the guarded variable and clause counts
are unchanged.

## Deterministic build-only regression

The source was compiled against the clause-counting CaDiCaL test double:

```text
/opt/homebrew/bin/g++ -O3 -std=c++20 -Wall -Wextra -Wpedantic \
  -I scratch/cadical_stub k11_forest_sat.cpp \
  -o /tmp/k11_forest_sat_amortized_stub

K11_FOREST_BUILD_ONLY=1 K11_FOREST_LOCAL_DENSITY_PB=1 \
  /tmp/k11_forest_sat_amortized_stub \
  k11_upper549_natural_array.txt /tmp/ignored.txt 1
```

It reports

```text
variables=4951658 clauses=15805044
local_density_pb=1
local_density_pb_variables=59036
local_density_pb_clauses=280226
BUILD_ONLY
```

This test checks deterministic construction and inventory only.  The test
double is not a SAT solver and supplies no satisfiability conclusion.

## Mathematical calibration

At `k=11`, the scalar comparator is already implied by the stronger
cumulative entry-rank truncation theorems, although those cuts are not all
present in this guarded CNF module.  The genuinely new mathematical content
is the distributional inequality

\[
\sum_{U\in\binom{[11]}6}(32-p_U)_+\le462,
\]

which is not encoded by this scalar pseudo-Boolean comparator.

The checked source hash is

```text
fe88bd308e968cd46a5e9be0246f265b0da1fa03935892d4a6ad73446c32e540  k11_forest_sat.cpp
```
