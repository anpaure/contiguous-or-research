# `k=11` `q19_abstract` portal-branch implementation

## Outcome

`k11_forest_sat.cpp` now accepts

```text
K11_FOREST_PORTAL_BRANCH=q19_abstract
```

This is the exact branch specified in Section 6.2 of
`K11_PORTAL_BRANCH_ENCODING_DESIGN.md`.  It allocates no SAT variable and
adds exactly 922 clauses:

```text
rank-six mixed schedule                         462
12 active rank-seven endpoint macros   12 * 38 = 456
direct target 958 fixed to seam [18,21]          4
                                                ---
                                                922
```

The branch is an extra hypothesis, not a WLOG reduction.  A satisfying
decoded word, after independent OR verification, proves `nu(11)=465`.
UNSAT refutes only this named branch.

## Exact constraints

The selected rank-six schedule is fixed to zero-based states

```text
state6[i] = 02,  i = 0..18;
state6[i] = 03,  i = 19..461.
```

Thus its selected witnesses are the nineteen triple windows `R3(1)..R3(19)`
and the remaining 443 quadruple windows `R4(20)..R4(462)`.

For each target

```text
251 493 607 941 956 1267 1468 1694 1763 1884 1946 1990
```

the implementation sets the existing `RankSevenShadow::active` literal and
applies the zero-variable endpoint macro with `h=17`.  Therefore its selected
crossed witness is exactly one of zero-based

```text
[0,3], [1,4], ..., [17,20],
```

which are the physical portals `R4(1)..R4(18)`.  The direct exact target
`958` is fixed to zero-based `[18,21]`, the seam `R4(19)`.

Every other nonzero target remains encoded by the original exact formula.
The rank-six row and all 465 entry masks remain free.

## Tiny clause/sign audit

The inherited unary endpoint meanings are

```text
L(p) <=> p >= selected left endpoint,
R(p) <=> p <= selected right endpoint.
```

For each named rank-seven target, `L(17)` forces the left endpoint to be at
most 17.  If the unique left transition occurs at `s`, then the emitted
clauses reduce to

```text
 R(s+3), -R(s+4),
```

so the right endpoint is exactly `s+3`.  At `s=0` the two clauses are

```text
-L(0) OR R(3)
-L(0) OR -R(4).
```

At `s>0` they are

```text
-L(s) OR L(s-1) OR R(s+3)
-L(s) OR L(s-1) OR -R(s+4).
```

The signs therefore agree with the endpoint convention.  The count per
target is one `active` unit, one `L(17)` unit, and 36 implications, namely
38 clauses.

The seam units are

```text
 L_958(18), -L_958(17), R_958(21), -R_958(22),
```

and hence fix exactly `[18,21]`.

The base crossed-witness encoding makes an active rank-seven interval exact:
the selected rank-six prefix and suffix are distinct six-subsets of the
target, while the four absent-bit clauses prohibit contamination.  No new
pin variables or detached portal-value variables are introduced.

## Mode guard and proof trace

As for the two earlier portal modes, `q19_abstract` requires exactly

```text
K11_FOREST_ADJACENT_SHADOWS=1
K11_FOREST_RANK3_SHADOWS=1
```

among the structural modules.  Containment caps are optional; all other
structural/symmetry modes are rejected.

The proof-trace ordering fix is preserved.  `solver.trace_proof(...)` is
still called immediately after construction of the solver and before solver
options, variable declaration, or any clause emission.

With the portal environment variable absent, the new clause block is not
entered.  The disabled-mode inventory remains the audited
`2,882,282 / 14,352,124`, and the two older branches also retain their exact
deltas:

```text
q19_fixed_row:    485 clauses, total 14,352,609
q19_factor_prefix:704 clauses, total 14,352,828
```

## Remote build-only regression

The source was copied to the RunPod host

```text
root@157.157.221.29:27423
```

and compiled, with no warnings, using

```text
g++ -O3 -std=c++2a -Wall -Wextra -Wpedantic \
    -I/root/cadical/src k11_forest_sat.cpp \
    /root/cadical/build/libcadical.a -lpthread \
    -o k11_forest_sat_q19_abstract
```

Build-only formula generation reported:

| mode | containment caps | variables | clauses | branch clauses |
|---|---:|---:|---:|---:|
| `q19_abstract` | no | 2,882,282 | 14,353,046 | 922 |
| `q19_abstract` | yes | 2,882,282 | 14,460,414 | 922 |

No SAT solve was launched.

Remote deployment paths and hashes:

```text
/root/q19_abstract_build/k11_forest_sat.cpp
419e073e6e07be901d2b74bf5efaaa6f49f5cbb25164ebc2f7a8e0c0c591d0ac

/root/q19_abstract_build/k11_forest_sat_q19_abstract
2a00fec86c3fe51c268b07c6bf54e77f1b54272d3a0859cf81b1147b7fdc8aa9
```
