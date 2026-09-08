# Exact CNF encoding of the unrestricted `k=11` local-density cuts

## 1. Scope and switch

`k11_forest_sat.cpp` now recognizes the optional environment variable

```text
K11_FOREST_LOCAL_DENSITY_PB=1
```

When enabled, it adds the two independently audited necessary inequalities

\[
 210n_1+84n_2+28n_3+7n_4+n_5\ge7392,
 \tag{1}
\]

\[
 252n_1+126n_2+56n_3+21n_4+6n_5+n_6\ge12936,
 \tag{2}
\]

where `n_s` is the number of literal array entries of Hamming weight `s`.
The first inequality is audited in `K11_LOCAL_DENSITY_INDEPENDENT_AUDIT.md`.
The second was subsequently strengthened by the simultaneous-cap marked-run
theorem in `K11_NESTED_LOCAL_DENSITY_NEXT.md`; its independent source and
solver audit is `CONTAINMENT_CAPS_SOLVERS_INDEPENDENT_AUDIT.md`.

The module is disabled by default.  In disabled mode its plan is not
constructed, so it allocates no variables and emits no clauses.

## 2. Exact entry-rank layer

For each physical position `p`, the module derives one-hot literals

```text
rank[p][s]  <=>  popcount(A[p]) = s,       0 <= s <= 11.
```

After the first input bit, the two prefix-count literals are simply
`!A[p][0]` and `A[p][0]`.  Suppose the exact prefix-count literals after some
prefix are `c_s`, and let `x` be the next array bit.  The next count literal
`z_s` is defined by the exact mux

\[
 z_s\iff (\neg x\land c_s)\lor(x\land c_{s-1}),
\]

with an out-of-range predecessor represented by the constant-false literal.
The four clauses are

```text
x  -z   c_s
x   z  -c_s
-x -z   c_(s-1)
-x  z  -c_(s-1)
```

For `x=0` they reduce to `z <=> c_s`; for `x=1` they reduce to
`z <=> c_(s-1)`.  Induction on the eleven bits proves that the final twelve
literals have their stated meanings and exactly one is true.  No independent
or guessable rank variable exists.

This rank circuit is shared by both inequalities.

## 3. Exact weighted terms

For each inequality and position, eight binary literals encode that entry's
weight.  For a bit position `b`, its output `w_b` is defined as the OR of
exactly those `rank[p][s]` whose coefficient has bit `b` set:

```text
rank[p][s] -> w_b                         for every supporting s
w_b -> OR_s rank[p][s].
```

Because the rank layer is exact one-hot, these eight outputs are exactly the
ordinary binary expansion of the coefficient contributed by that entry.

The first coefficient table has 14 set-bit incidences and the second has 21.
Including one reverse-OR clause for each of the eight output bits, this costs
`22+29=51` clauses per physical position.

## 4. Exact arithmetic

The 465 eight-bit terms are summed by a balanced tree of ripple adders.  A
full adder uses eight truth-table clauses for

\[
 s=a\mathbin\oplus b\mathbin\oplus c
\]

and the following six clauses for

\[
 c'=\operatorname{majority}(a,b,c):
\]

```text
-a -b  c'       -c' a b
-a -c  c'       -c' a c
-b -c  c'       -c' b c
```

Both outputs are therefore bidirectionally defined.  Every ripple addition
retains its final carry, so no addition is modular.  The balanced tree uses
4,172 bit stages per inequality and ends at width 17.  This is sufficient
because

\[
 465\cdot252=117180<2^{17}.
\]

Finally, an exact most-significant-bit-first comparator enforces

```text
7392  <= total_five
12936 <= total_six.
```

At each bit it forbids `x=1,y=0` while all higher bits are equal.  Its
`equal_above` literals are defined in both directions.  Thus auxiliary choices
cannot conceal the first unequal bit.

It follows that every assignment of the original array bits has a unique
extension through the rank, weight, and addition gates.  That extension
satisfies the comparator clauses if and only if (1) and (2) hold.  The module
is therefore sound and complete for the two pseudo-Boolean inequalities.

## 5. Exact inventory

The enabled module has the following inventory.

| part | variables | clauses |
|---|---:|---:|
| constant one | 1 | 1 |
| 465 exact rank circuits | 34,875 | 139,500 |
| two weighted terms per entry | 7,440 | 23,715 |
| two balanced adder trees | 16,688 | 116,816 |
| two exact comparators | 32 | 194 |
| **total** | **59,036** | **280,226** |

The inventory agrees with all six production build-only regressions.

## 6. Independent gate checker

`k11_local_density_pb_unit.cpp` is a standalone checker with no CaDiCaL
dependency.  It exhaustively verifies:

* all 16 assignments of the mux truth table;
* all 32 assignments of the full-adder truth table;
* every input and every auxiliary assignment of ripple adders of widths 1--4,
  proving exactly one extension and the exact nonmodular sum;
* every input and every auxiliary assignment of unsigned comparators of
  widths 1--5, proving exactly one extension for `x<=y` and no extension for
  `x>y`.

The checked output is

```text
PASS: mux, full-adder, ripple-adder, and unsigned-comparator truth tables
```

## 7. Build-only regressions

All builds used the full production option set (adjacent shadows, rank-three
shadows, band cuts, joint-band cuts, endpoint alignment, canonical/boundary
rank-six entry cuts, singleton-pool cut, and the indicated exact rank-six
branch).  No SAT solve was launched.

| portfolio | PB off variables/clauses | PB on variables/clauses |
|---|---:|---:|
| branch 0, no min-component schedule | 2,924,697 / 14,732,380 | 2,983,733 / 15,012,606 |
| branch 0, `e0c1` | 2,924,697 / 14,772,036 | 2,983,733 / 15,052,262 |
| branch 1, `e1c2` | 2,924,938 / 14,811,758 | 2,983,974 / 15,091,984 |

Each difference is exactly `+59,036` variables and `+280,226` clauses.

For a stronger absent-mode regression, the frozen pre-change source

```text
c16750771e78912f427d472d845cf952e30e4909eea97b474b6fccc0d9676017
```

and the new source were compiled against the same deterministic clause-stream
hashing solver stub.  With the density variable absent, their complete literal
streams were identical in all three portfolios:

| portfolio | variables | clauses | literal calls | hash1 | hash2 |
|---|---:|---:|---:|---|---|
| branch 0 | 2,924,697 | 14,732,380 | 65,118,464 | `508f5b599ffa2587` | `ce4ebfb80b9d4243` |
| `e0c1` | 2,924,697 | 14,772,036 | 65,261,404 | `1ba2f6438525dabf` | `08e01def7963e234` |
| `e1c2` | 2,924,938 | 14,811,758 | 65,383,266 | `a90ec30698cb6056` | `b12d755236aaccbd` |

Therefore the optional implementation preserves the disabled CNF literal for
literal, not merely its variable and clause counts.

## 8. Reproduction

```bash
g++ -O3 -std=c++20 -Wall -Wextra -Wpedantic \
    k11_local_density_pb_unit.cpp -o k11_local_density_pb_unit
./k11_local_density_pb_unit

g++ -O3 -std=c++20 k11_forest_sat.cpp -lcadical -o k11_forest_sat

K11_FOREST_LOCAL_DENSITY_PB=1 \
K11_FOREST_BUILD_ONLY=1 \
./k11_forest_sat k11_upper549_natural_array.txt ignored.txt 1
```

The usual production portfolio variables should be supplied alongside the
last command when reproducing the table above.
