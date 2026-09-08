# Short-interval pool refinement from an upper singleton

## Status

Let

```text
k=2r+1,
M=C(k,r)=C(k,r+1),
n=M+d,
L=sum_(s=1)^(r-1) C(k,s).
```

Choose one witness for every rank-`r` and rank-`r+1` mask.  Let `x_j` count
selected upper witnesses of width `j`.  In every regime where the independently
proved cross-layer theorem gives `x0<=1`, the following additional necessary
inequality holds:

\[
 \boxed{x_d\ge L+2M-\left(dn-\binom d2\right)+(d-1)x_0.}
 \tag{1}
\]

This is unrestricted.  It uses only physical interval counts and the selected
witness bands; it does not assume a fixed derivative row, Johnson adjacency,
or a connected endpoint forest.

## 1. Every lower target uses a short interval

The selected rank-`r` witness family has `M` intervals in `M+d` positions.
After sorting by left endpoint, its `i`th interval is contained in `[i,i+d]`.
Consequently every physical interval of length at least `d+1` contains a
selected rank-`r` witness and has OR rank at least `r`.

Every target of rank at most `r-1` therefore has a witness of length at most
`d`.  There are exactly

\[
 L=\sum_{s=1}^{r-1}\binom{k}{s}
\]

such targets.

The independently selected rank-`r` witnesses themselves all have length at
most `d`: a length-`d+1` interval contains a selected rank-`r+1` witness.
Finally, exactly `M-x_d` selected rank-`r+1` witnesses have width at most
`d-1`, hence length at most `d`.

All these intervals represent different masks (their target ranks or masks
differ), so they are physically distinct.  The short pool must therefore
contain at least

\[
 L+M+(M-x_d)=L+2M-x_d                         \tag{2}
\]

occupied intervals.

## 2. A selected upper singleton deletes pool slots

The number of nonempty physical intervals of length at most `d` is

\[
 P_d(n)=\sum_{ell=1}^{d}(n-ell+1)
       =dn-\binom d2.                           \tag{3}
\]

Suppose `x0=1` and the selected singleton is `[p,p]`, with OR mask `C` of rank
`r+1`.  For every length `ell=2,...,d`, at least one interval of length `ell`
contains `p`; this remains true when `p` is either boundary position.  Thus
there are at least `d-1` short intervals containing `p` other than the selected
singleton.

Every such interval has OR containing `C`.  It cannot represent a target of
rank at most `r`.  If its OR has rank `r+1`, it equals `C`, so it also cannot
be the selected witness of a different upper target.  Hence none of these
`d-1` intervals can occur among the distinct intervals counted in (2).

Because `x0` is zero or one, the usable short pool has size at most

\[
 P_d(n)-(d-1)x_0.                              \tag{4}
\]

Combining (2)--(4) proves (1).

## 3. Exact values at the conjectural odd lengths below 20

At `n=B(k)=M+d`, equation (1) gives:

| `k` | `M` | `d` | `L` | base lower bound on `x_d` | singleton refinement |
|---:|---:|---:|---:|---:|---:|
| 7  | 35 | 2 | 28 | 25 | `x2>=25+x0` |
| 9  | 126 | 2 | 129 | 126 | `x2>=126+x0` |
| 11 | 462 | 3 | 561 | 93 | `x3>=93+2*x0` |
| 13 | 1,716 | 3 | 2,379 | 657 | `x3>=657+2*x0` |
| 15 | 6,435 | 3 | 9,948 | 3,507 | `x3>=3507+2*x0` |
| 17 | 24,310 | 3 | 41,225 | 16,909 | `x3>=16909+2*x0` |
| 19 | 92,378 | 3 | 169,765 | 77,381 | `x3>=77381+2*x0` |

The `k=9` row is rigid: since `x2<=M=126`, it forces

```text
x0=0,
x2=126.
```

Thus every selected upper-middle witness in an optimal nine-bit array has
physical length three.  For `k=11`, (1) strengthens the currently encoded
`x3>=93` row exactly in the `x0=1` branch.

## 4. Scope

Equation (1) is a necessary inequality, not a profile characterization or an
existence theorem.  The additive deletion term is proved here only under
`x0<=1`; with several upper singleton positions, their families of containing
short intervals can overlap and require separate inclusion--exclusion.

Any SAT implementation may add the `k=11` comparison

```text
x3 >= 93+2*x0
```

without choosing a fixed row.  A candidate still requires independent OR
verification, and an UNSAT claim still requires a checked proof trace.
