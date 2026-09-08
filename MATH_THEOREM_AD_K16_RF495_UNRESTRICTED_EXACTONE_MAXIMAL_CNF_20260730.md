# AD theorem: unrestricted exact-one RF495 maximal-provider CNF

Date: 2026-07-30  
Scope: the complete frozen seed5/self RF495 `4/9/5` fibre.

## 1. Construction

The saturated atlas has 70 residual targets and exactly 70 nonempty free-run
sets `Q`.  In every `(target,Q)` class there is a unique greatest fixed OR,
giving 4,900 exact physical maximal providers.  The new formula uses:

```text
288   cell-bit variables       (18 cells times 16 coordinates)
4900  provider selectors       (70 targets times 70 choices)
4830  sequential auxiliaries   (70 blocks times 69)
-----
10018 variables.
```

For a provider `(T,F,Q)` with selector `y`, it includes:

1. `(-y OR -x[p,b])` for every `p in Q` and `b notin T`;
2. `(-y OR OR_(p in Q) x[p,b])` for every `b in T minus F`.

Each free cell has one 16-literal nonzero clause.  Each target block has one
70-selector at-least-one clause and a 69-auxiliary Sinz at-most-one chain.
For selectors `x_1,...,x_70` and auxiliaries `s_1,...,s_69`, the chain is

```text
(-x_1 OR s_1),
(-x_i OR s_i), (-s_(i-1) OR s_i), (-x_i OR -s_(i-1))  for 2<=i<=69,
(-x_70 OR -s_69).
```

If two selectors `x_i,x_j`, `i<j`, were true, `x_i` would propagate the
prefix state through `s_(j-1)`, contradicting the clause for `x_j`.  Together
with the positive block clause this is exact-one.

The exact clause ledger is

```text
18       nonzero-cell clauses
160954   provider-semantic clauses
70       target at-least-one clauses
14420    sequential at-most-one clauses
------
175462 clauses.
```

The CNF has SHA-256

```text
0d0adb8078b412ee4602382222bdbb907f2bf6274f5fc2715578fe07079038f8.
```

## 2. Exactness theorem

**Theorem.** The exact-one CNF is satisfiable if and only if the frozen
seed5/self RF495 fibre contains a literal universal word of length 12,873.

*Proof.* Suppose first that the CNF is satisfiable.  Every free cell is
nonzero.  Exactly one authenticated physical representative is selected for
each residual target.  The forbidden-bit clauses make every selected
interval's variable-cell contribution a subset of its target; the needed-bit
clauses supply every target bit absent from its fixed OR.  Hence that literal
interval has OR exactly the target.  The two fixed bodies cover every
nonresidual mask, so the materialized word is universal.

Conversely, let a literal completion exist.  For every residual target choose
one realizing raw interval.  Within its same-`(target,Q)` class replace the
row by the unique greatest fixed-OR representative.  The free support and all
forbidden bits are unchanged, while `T minus F` can only shrink, so the same
cell assignment realizes the maximal representative.  Select exactly this
row for each target.  All provider, nonzero, and exact-one clauses follow.
QED.

This is the unrestricted 4,900-choice frozen-fibre model: it has no privileged
hole root, rehost budget, sharp/nonsharp unit, or derivative-row condition.

## 3. Independent audit and acceptance

The independent verifier reconstructs every one of the 175,462 clauses in
deterministic order from the mapping and checks the complete variable ranges,
all 70 exact-one blocks, and the semantic exactness theorem.  It reports
`PASS` with payload

```text
1da731b42b5e9d68d68da92645e048d294c51661c9963182053bbd693eaafce4.
```

A separate fail-closed SAT decoder checks exactly one selector per target,
replays every selected physical representative, reconstructs all eighteen
cells, and then literally replays all 65,535 masks.  Its `D^3` histogram is
diagnostic only.  A SAT output passing this decoder proves
`nu(16)=12,873`; an UNSAT claim requires a checked proof and excludes this
frozen RF495 fibre only.

## 4. Execution status

The formula is the next exact computational priority after the sharp roots
were structurally closed through rehost budget ten.  No solve was launched in
this lane because H100 was effectively saturated and swap-full.  The package
is staged under

```text
/home/amodo/or15/work/ad_rf495_exactone_0d0adb80_20260730
```

for a later one-CPU proof-retaining run.  Restrictive-first nonsharp choices
may be used as branching or polarity hints only; adding them as hard units
would shrink the theorem's unrestricted scope.

After core 7 was proposed for the run, the mandatory health check found PID
`1073042`, a live Kissat process using 95.6% CPU on that core; `mpstat -P 7`
reported 0% idle.  Swap was also full.  Therefore the conditional launch was
not authorized by the health criterion and no process was started.  The
remote package hashes match the local CNF/map/audit exactly.
