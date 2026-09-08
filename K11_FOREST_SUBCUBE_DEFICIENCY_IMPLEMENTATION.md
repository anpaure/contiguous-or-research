# Exact six-subcube run-credit encoding for the unrestricted `k=11` solver

## 1. Verdict

The full per-six-set deficiency information is practical to encode.  The
optional environment guard

```text
K11_FOREST_SUBCUBE_DEFICIENCY=1
```

now enables an exact CNF circuit in `k11_forest_sat.cpp`.  The implemented
cut is stronger than the originally requested linear-credit law.

For

\[
 p_U=|\{i:A_i\subseteq U\}|,
 \qquad U\in\binom{[11]}6,
\]

the independently proved exact run envelope gives

\[
 \gamma(28)=7,\quad \gamma(29)=5,\quad
 \gamma(30)=3,\quad \gamma(31)=1,\quad
 \gamma(p)=0\ (p\ge32).
\]

The module imposes both audited inequalities

\[
 \boxed{\sum_U\gamma(p_U)\le462}                         \tag{1.1}
\]

and

\[
 \boxed{\sum_U(\gamma(p_U)-1)_+\le369}.                 \tag{1.2}
\]

Thus it contains, in particular,

\[
 7a_{28}+5a_{29}+3a_{30}+a_{31}\le462,
 \qquad
 6a_{28}+4a_{29}+2a_{30}\le369.
\]

Both strictly dominate the earlier
`4a28+3a29+2a30+a31<=462` law.  The mathematical source is
`EXACT_SUBCUBE_RUN_CREDIT.md`; its independent proof audit is
`EXACT_SUBCUBE_RUN_CREDIT_AUDIT.md`.

## 2. Exact support indicators

For a fixed six-set `U` and position `i`, a fresh variable `x[U][i]` is
defined by

\[
 x_{U,i}\longleftrightarrow
 \bigwedge_{b\notin U}\neg A_{i,b}.                      \tag{2.1}
\]

There are five outside coordinates.  Five binary implications and one
six-literal reverse clause define (2.1) in both directions.  Hence

\[
 p_U=\sum_{i=0}^{464}x_{U,i}                              \tag{2.2}
\]

exactly, rather than by a one-way relaxation.

The direct five-input conjunction is smaller than constructing the entire
subset lattice at every position.  The latter would require indicators for
all coordinate subsets of sizes two through five and would use both more
variables and more clauses.

## 3. Exact population counts

Each 465-input sum (2.2) is computed by a Wallace compressor:

1. three equal-weight literals enter an exact full adder;
2. its sum stays at the same weight and its carry moves one weight upward;
3. compression continues until at most two literals remain at each weight;
4. one exact ripple addition combines the two residual binary rows.

The full-adder CNF has fourteen clauses: eight define parity and six define
majority.  The final carry is retained, so no modular wraparound is possible.

For 465 inputs the compressor uses exactly 453 full adders and the final
ripple uses eight.  Thus one six-set count needs 461 full adders, or 922
variables and 6,454 clauses.

The independently proved marked-run bound `p_U>=28` is encoded by a direct
first-difference comparator against the constant 28.  It uses three clauses
and no auxiliary variable.  Since this lower bound holds for every universal
word represented by the base formula, adjoining it preserves the exact
solution set.

## 4. Exact charge bits

Let `p[j]` denote bit `j` of the exact count.  Define

\[
 g_U=[p_U\le31].
\]

Because `p_U>=28`, the exact three-bit binary expansion of `gamma(p_U)` is

\[
 \gamma_0=g_U,
 \qquad
 \gamma_1=g_U\wedge\neg p[0],
 \qquad
 \gamma_2=g_U\wedge\neg p[1].                            \tag{4.1}
\]

Indeed the four live values are

```text
p_U       28   29   30   31
gamma     111  101  011  001   (binary, high bit first)
```

The variable `g_U` is an exact conjunction saying that count bits 5 and
above are zero.  Two exact AND-NOT gates define the other charge bits.
This costs only three variables and eleven clauses per six-set.

The residual charge in (1.2) reuses the same gates:

\[
 (\gamma-1)_+=2\gamma_1+4\gamma_2.                       \tag{4.2}
\]

No second bank of per-subcube variables is needed.

## 5. Global exact sums

The 462 three-bit charges are summed by a second Wallace circuit.  Its
initial buckets contain 462 literals at each of weights 1, 2, and 4.  It
uses 1,370 compressor adders and an eleven-adder final ripple.  A direct
constant comparator imposes total at most 462.

The residual circuit starts with 462 literals at weights 2 and 4.  It uses
908 compressor adders and an eleven-adder ripple, followed by the comparator
against 369.

All support gates, full adders, charge gates, and comparisons are
bidirectional or exact forbidden-first-difference clauses.  Therefore every
assignment to the array bits has exactly its true support counts and exact
charges; auxiliary choices cannot conceal a violation of (1.1) or (1.2).

## 6. Deterministic inventory

The optional module contributes exactly

| component | variables | clauses |
|---|---:|---:|
| true constant | 1 | 1 |
| `462*465` support indicators | 214,830 | 1,288,980 |
| 462 exact support popcounts | 425,964 | 2,981,748 |
| 462 lower-bound comparators | 0 | 1,386 |
| exact charge bits | 1,386 | 5,082 |
| total-charge Wallace sum/comparator | 2,762 | 19,340 |
| residual-charge Wallace sum/comparator | 1,838 | 12,873 |
| **total** | **646,781** | **4,309,410** |

The flat zero-terminated clause buffer avoids allocating 4.3 million
individual `std::vector` objects.  With the clause-counting test double, the
complete guarded build uses about 87 MB peak resident memory and takes under
one second after compilation on the audit host.

The unguarded base inventory is

```text
variables=4892622 clauses=15524818
```

and the guarded inventory is

```text
variables=5539403 clauses=19834228
subcube_deficiency_variables=646781
subcube_deficiency_clauses=4309410
```

The module also composes additively with the existing local-density PB plan:

```text
variables=5598439 clauses=20114454
local_density_pb_variables=59036
local_density_pb_clauses=280226
subcube_deficiency_variables=646781
subcube_deficiency_clauses=4309410
```

With the adjacent/rank-three reductions and both central band modules, the
current optimized forest inventory is

```text
variables=3536105 clauses=18699861
subcube_deficiency_variables=646781
subcube_deficiency_clauses=4309410
```

These are construction inventories, not SAT or UNSAT conclusions.

## 7. Independent finite circuit audit

The checker

```text
python3 scratch/verify_k11_subcube_run_credit_encoding.py
```

independently verifies:

* every row of the exact full-adder truth table;
* the five-coordinate support equivalence;
* all 512 inputs to the `p_U>=28` comparator;
* all 4,096 inputs to each global constant comparator;
* the exact capacity table `7,5,3,1,0` from `F_3(p,q)`;
* the charge-bit identities for every `28<=p<=465`;
* both Wallace inventories and the final variable/clause totals.

Its output is

```text
full-adder truth table: PASS
five-coordinate support equivalence: PASS
constant comparators: PASS
exact gamma table 7,5,3,1,0: PASS
Wallace/inventory audit: 646781 variables, 4309410 clauses: PASS
```

## 8. Guard-off identity

`SubcubeRunCreditPlan` is allocated only when
`K11_FOREST_SUBCUBE_DEFICIENCY` is nonzero.  Its clauses are emitted only
when that plan exists.  The portal branch rejects the new structural module,
preserving its previously frozen option inventory.

The streaming hash test double in `scratch/cadical_hash_stub/cadical.hpp`
fingerprints every `solver.add()` argument.  The absent guard and an explicit
zero guard both give

```text
CLAUSE_STREAM_FNV64=ad22e261832b9ae2 ADD_CALLS=55261249
```

so the disabled module has exact clause-stream identity, not merely equal
variable and clause counts.  With the module enabled the fingerprint is

```text
CLAUSE_STREAM_FNV64=4a7368896cedd337 ADD_CALLS=73792904
```

The hash stub is a build auditor, not a SAT solver.

## 9. Boundary-core and onion reuse

The exact run envelope has the stronger boundary-core branch

\[
 7a_{28}^C+5a_{29}^C+3a_{30}^C+a_{31}^C\le461
\]

when the canonical endpoint-six-set branch is selected.  This strengthening
is now encoded under the conjunction of

```text
K11_FOREST_SUBCUBE_DEFICIENCY=1
K11_FOREST_RANK_FILTRATION_TYPE1=1.
```

The existing support indicators are reused.  Since Type I fixes `A[0]=63`,
only the support of the six-set `U=63` changes on deleting the endpoint.  An
exact two-bit correction to the existing global charge sum therefore avoids
both a second support bank and a second population counter.  The incremental
inventory is 25 variables and 189 clauses.  The implementation and
independent audit are `K11_TYPE1_CORE_SUBCUBE_ENCODING.md` and
`K11_TYPE1_CORE_SUBCUBE_ENCODING_AUDIT.md`.

Likewise, the proposed onion cuts can reuse `LocalDensityPBPlan`'s exact
entry-rank one-hot layer:

* endpoint rank-six restrictions and the scalar cap of 134 rank-five
  entries become small cardinality comparisons;
* the claim that rank-at-most-four positions form at most two blocks becomes
  a transition counter over the shared one-hot predicates;
* exact rank-five core coverage and rank-five value duplication are not
  consequences of rank counts and need additional value-sensitive clauses.

Those onion claims should be encoded only after their theorem audit.  No
un-audited branch condition was added here.

## 10. Frozen artifacts

At the time of this implementation audit:

```text
3a51bcf5f181d0a31f5cceac1e94f19079355b02aad60516be9bc626c1b5dec8  k11_forest_sat.cpp
466b700aedfccc8e7d06fe289df3daf027426123841537c6926e393e7b651d63  scratch/verify_k11_subcube_run_credit_encoding.py
34284993af22627b273dd3cb27abcc5815f574d45aa81e95dcc074fde5c651a0  scratch/cadical_hash_stub/cadical.hpp
b3b8fa5d614a12abbd0a661596637d619957c597779d232de775f1f5eadd407d  EXACT_SUBCUBE_RUN_CREDIT.md
6b07e3e92dfb308bc5e3eeaa5aedfe8a9d146019346a2d812d8ddf36d7681cb5  scratch/check_exact_subcube_run_credit.py
e5d22ff7bf69ff275f7eb39ba19e30e818bfc1ff8f7f1e041d619450f83317f3  EXACT_SUBCUBE_RUN_CREDIT_AUDIT.md
```

This source hash includes the independently developed Type-II rank-filtration
module and was rebuilt after both guarded modules were integrated.  Any
subsequent shared-worktree edit must be rehashed before a production run.

The later Type-I rank-filtration edit did not alter the subcube-deficiency
module.  The production deployment combining both modules was rebuilt from
the subsequent source hash

```text
ab9a3e1cce0325469adbb57d8c39c9a5b660f194c20b9ff6b099497f0ba9c4ea  k11_forest_sat.cpp
```

and is frozen separately in `K11_ONION_SUBCUBE_DEPLOYMENT_20260723.md`.

The theorem-note hash changed only for the two presentation repairs requested
by the independent audit: unique equation numbering and an explicit
proper-subset credit function in the boundary-core paragraph.  Neither repair
changes the encoded `k=11` charge tables.
