# Exact third-edge orbit split for the fixed-row `k=11` search

## 1. Statement

Use the canonical prefix from `K11_SECOND_EDGE_ORBITS.md`:

```text
C = {0,1,2,3,4}                         omitted rank-5 colour
E = C union {5} = 63                    first rank-6 vertex
F = E - {3} + {6} = 119                second rank-6 vertex
```

The four certified choices for the next vertex `G` are

```text
q=0: G=126 = F-{0}+{3}
q=1: G=246 = F-{0}+{7}
q=2: G= 95 = F-{5}+{3}
q=3: G=215 = F-{5}+{7}.
```

Assume the required delay-three factorability condition: every internal
coordinate 1-run of the central row has length at least four.  After fixing
`q`, every legal next vertex `H`, modulo the pointwise/setwise stabilizer of
the already fixed data `C,E,F,G`, is represented exactly once in this table:

| `q` | number of orbits | representative masks `H` |
|---:|---:|---|
| 0 | 4 | `125, 252, 95, 222` |
| 1 | 6 | `245, 252, 500, 215, 222, 470` |
| 2 | 2 | `126, 222` |
| 3 | 3 | `222, 246, 470` |

Thus the first four real vertices have only `4+6+2+3=15` exhaustive
symmetry branches after factorability, rather than four branches each with
up to thirty raw Johnson continuations.

## 2. Two exact exclusions

Write the second transition as `F -> G = F-{x}+{y}` and the third as
`G -> H = G-{u}+{v}`.

First, `u` cannot equal `y`.  If it did, then

```text
G intersection H = G-{y} = F-{x} = F intersection G,
```

so the third edge would repeat the rank-five lower colour of the second
edge.  The fixed-row search requires all 461 real edge lower colours to be
distinct.

Second, `u` cannot be bit `6`.  Bit `6` is absent from `E` and was introduced
by the first transition `E -> F`.  It is present in both `F` and `G`.  If it
were removed by `G -> H`, its incidence word at the start of the central row
would contain

```text
E F G H
0 1 1 0.
```

This is an internal 1-run of length two, contradicting the exact
delay-three run condition.  Notice that this is a boundary-safe argument:
the run starts after the left endpoint and ends before the right endpoint.

No other removal is excluded merely by the already fixed prefix.  Addition
always uses a coordinate outside `G`.

## 3. Stabilizer calculation

The stabilizer of a fixed family of masks permutes coordinates precisely
inside equal membership-signature classes.  For each `q`, remove the two
forbidden classes from `G` and cross the remaining removal classes with the
addition classes outside `G`.

### Case `q=0`, `G=126`

The nontrivial signature classes are

```text
{1,2,4},  {7,8,9,10};
```

the other relevant coordinates `0,3,5,6` are distinguished.  The allowed
removal classes are `{1,2,4}` and `{5}`; the addition classes are `{0}` and
`{7,8,9,10}`.  Their four products give

```text
125, 252, 95, 222.
```

### Case `q=1`, `G=246`

The allowed removal classes are `{1,2,4}` and `{5}`.  The addition classes
are `{0}`, `{3}`, and `{8,9,10}`.  The six products give

```text
245, 252, 500, 215, 222, 470.
```

### Case `q=2`, `G=95`

The only allowed removal class is `{0,1,2,4}`.  The addition classes are
`{5}` and `{7,8,9,10}`.  The two products give

```text
126, 222.
```

### Case `q=3`, `G=215`

The only allowed removal class is `{0,1,2,4}`.  The addition classes are
`{3}`, `{5}`, and `{8,9,10}`.  The three products give

```text
222, 246, 470.
```

In each case the stabilizer is independently transitive on the displayed
removal and addition classes.  Conversely, different class pairs have
different membership signatures and cannot be related by that stabilizer.
The table is therefore both complete and irredundant.

The representative vertices are distinct from `E,F,G`; their new edge lower
colour is distinct from both previous lower colours.  Hence no additional
case in the table is spurious.

## 4. Implementation and safe scope

`recombine_paths_sat.cpp` now accepts

```text
RECOMBINE_SECOND_ORBIT=q
RECOMBINE_THIRD_ORBIT=t
```

where `t` lies in the row-specific range from the table.  It fixes the
directed arc `G -> H`.  The option is rejected unless all of the following
hold:

```text
complete Johnson graph (`all...` mode)
ordered connected encoding
k=11, rank=6, delay=3
factorability enforced either up front or by the exact lazy run loop
WLOG canonicalization active
RECOMBINE_SECOND_ORBIT is also supplied.
```

Running all fifteen `(q,t)` pairs is exhaustive for the factorable fixed-row
ansatz.  Like the second-edge split, it is not a theorem about unrestricted
monotone-band arrays.
