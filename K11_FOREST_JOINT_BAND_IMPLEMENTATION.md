# Implemented exact joint-band circuit for unrestricted `k=11,n=465`

## Frozen status

The globally necessary cuts proved and independently audited in
`K11_FOREST_JOINT_SHORT_BAND_CUTS.md` are now implemented behind the new guard

```text
K11_FOREST_JOINT_BAND_CUTS=1
```

in `k11_forest_sat.cpp`.

Frozen source:

```text
SHA-256 8e0c04ae927ecff09b1ffbbeab5f8d719963788151d317cab05b78613e47fd8d
```

The guard requires

```text
K11_FOREST_BAND_CUTS=1
```

and exits with an explicit error otherwise.  It makes no fixed-row,
Hamilton-path, Johnson-adjacency, or connected-forest assumption.

A real remote `-O3` CaDiCaL build reproduced:

```text
all previous guards, joint guard off:
  variables = 2,885,308
  clauses   = 14,360,485

all previous guards, joint guard on:
  variables = 2,889,324
  clauses   = 14,390,451

joint delta:
  variables = 4,016
  clauses   = 29,966.
```

Thus the guard-off formula inventory is unchanged.

## 1. Source anchors

In frozen source `k11_forest_sat.cpp`:

```text
lines 278--519   JointBandCutPlan
lines 613--629   environment guard and dependency check
lines 781--787   plan allocation after BandCutPlan
lines 810--815   guarded clauses added to CaDiCaL
lines 1283--1298 exact inventory logging
```

The strengthened `x0<=1` comparator begins at line 466, the exact derivation
of `e=x0` at line 469, and the three rank-five chain cases at lines 488, 498,
and 508.

## 2. Why three rank-five chains are exact

Rank-five state `03` is already forbidden by the proved rank-six witness-length
bound.  Every coordinatewise monotone rank-five schedule therefore extends to
one of four maximal state chains:

```text
A = 00 01 02 12 13 23 33
B = 00 01 02 12 22 23 33
C = 00 01 11 12 13 23 33
D = 00 01 11 12 22 23 33.
```

Chain D contains no width-two state.  The proved inequality

\[
 y_2\ge y_0+87+4x_0
\]

excludes it.  The circuit chooses exactly one of A,B,C and conditionally
forbids states outside that chain.  A schedule that is a subchain of more than
one may choose any extension; all three cases compute its physical width
counts identically.

For the selected chain, six exact transition positions `h1,...,h6` are encoded
by 463 one-hot selectors each and converted to nine-bit unsigned integers.
The pre-existing schedule monotonicity makes the transition selector unique;
no quadratic at-most-one clauses are needed.

## 3. Exact derivation of `e=x0`

The existing rank-six boundary identities give

\[
 x_0=g_1+462-g_6.
\]

The new unguarded comparison is

\[
 g_1+461\le g_6,
\]

so `x0<=1`.  Rank-six width zero occurs only in states `00` and `33` on the
already-forced rank-six chain.  The implementation defines `e` bidirectionally
as the OR of all 924 such slot-state literals.  Since at most one can occur,

\[
 e=x_0\in\{0,1\}.
\]

This is an exact derived value, not a free phase selector.

## 4. Four guarded inequalities per chain

The rank-five boundaries give exact formulas for `y0,y2` in each of A,B,C.
The implementation substitutes them into:

\[
 y_0+x_0\le135,
\]

\[
 y_2\ge y_0+87+4x_0,
\]

\[
 x_0+x_1\le y_0+3,
\]

\[
 y_2\le x_3+3.
\]

All negative terms are moved to the opposite side, so every constraint is an
ordinary unsigned addition/comparison.  `4e` is represented by a two-bit
shift.  The ripple adders retain their final carry, and the guarded
most-significant-first comparators define all prefix-equality auxiliaries when
their chain selector is active.

The independent checker

```text
scratch/verify_k11_forest_joint_short_cuts.cpp
```

validates the direct profile identities and every transformed comparison on
300,000 deterministic boundary cases.  Its frozen SHA-256 is

```text
108c15dfa835cb958c2bd1260636eb61e14619cc52ef5b9461e991ba1c1570a2
```

and it reports `PASS`.

## 5. Exact joint inventory

The 4,016 variables are:

| category | variables |
|---|---:|
| three chain selectors | 3 |
| six rank-five boundary one-hots, `6*463` | 2,778 |
| six nine-bit boundary values | 54 |
| exact `e=x0` bit | 1 |
| ripple-adder and comparator auxiliaries | 1,180 |
| **total** | **4,016** |

The 29,966 clauses are:

| category | clauses |
|---|---:|
| exact-one chain selector | 4 |
| conditional chain membership, `3*462*3` | 4,158 |
| six boundary positive clauses | 6 |
| guarded boundary transition implications | 16,632 |
| binary boundary extraction, `6*9*2` | 108 |
| exact `e` definition | 925 |
| all adders and thirteen comparisons | 8,133 |
| **total** | **29,966** |

“Thirteen comparisons” means the one unguarded strengthening of `x0` plus
four inequalities in each of the three rank-five chain cases.

## 6. Reproduction

Build and reconstruct the complete guarded formula with:

```bash
g++ -O3 -std=c++20 k11_forest_sat.cpp -lcadical -o k11_forest_sat

K11_FOREST_BUILD_ONLY=1 \
K11_FOREST_ADJACENT_SHADOWS=1 \
K11_FOREST_RANK3_SHADOWS=1 \
K11_FOREST_BAND_CUTS=1 \
K11_FOREST_JOINT_BAND_CUTS=1 \
./k11_forest_sat k11_upper549_natural_array.txt ignored.txt 1
```

Expected inventory suffix:

```text
band_cut_variables=3026 band_cut_clauses=8361
joint_band_cut_variables=4016 joint_band_cut_clauses=29966
BUILD_ONLY
```

## 7. Scope

This is a globally valid search reduction, not a SAT or UNSAT result.  A SAT
candidate still requires both independent contiguous-OR verifiers.  An UNSAT
claim still requires an archived DIMACS/proof pair and independent proof
checking.  The upper-layer endpoint and residual-pin designs remain separate
and are not enabled by this guard.
