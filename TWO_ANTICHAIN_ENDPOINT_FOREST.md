# The two-antichain endpoint-forest bound

## 1. Theorem

Let `F,G` be disjoint antichains in the punctured Boolean lattice.  Their
cross-comparability graph `C(F,G)` has vertex set `F union G` and joins
`S in F` to `T in G` exactly when `S,T` are comparable.

Let

```text
lambda(F,G)=maximum number of edges in a linear-forest subgraph of C(F,G).
```

A linear forest is an acyclic graph of maximum degree at most two.  Put
`V=|F|+|G|`.

### Theorem 1 (endpoint forest)

Every universal contiguous-OR word of length `n` satisfies

```text
n >= V-floor(lambda(F,G)/2).                       (1.1)
```

Consequently

```text
B_forest(k):=max_(F,G) [|F|+|G|-floor(lambda(F,G)/2)]
```

is a valid lower bound for `nu(k)`.

## 2. Proof

Choose one witness interval for every member of `F union G`.  Within one
antichain, selected witnesses have distinct left endpoints, distinct right
endpoints, and increasing left order agrees with increasing right order.

The two left-endpoint sets have sizes `|F|,|G|` inside `[n]`, so at least

```text
|F|+|G|-n=V-n
```

positions are common.  Each common position pairs one `F` witness and one
`G` witness.  Their intervals share a left endpoint and are nested, so their
labels are comparable.  These pairs form a matching `L` in `C(F,G)` with

```text
|L|>=V-n.                                           (2.1)
```

Common right endpoints analogously give a matching `R` with

```text
|R|>=V-n.                                           (2.2)
```

No cross-pair belongs to both matchings: two distinct targets cannot use the
same physical interval.  Thus `L union R` has maximum degree at most two.

### Lemma 2.1 (no alternating endpoint cycle)

`L union R` is acyclic.

### Proof

Suppose it has an alternating cycle.  Index it so that `F_i-G_i` is an `L`
edge and `G_i-F_(i+1)` is an `R` edge, cyclically.  Write their common left
and right endpoints as `ell_i,r_i`.  Then

```text
I(G_i)=[ell_i,r_i],
I(F_i)=[ell_i,r_(i-1)].                              (2.3)
```

Noncontainment within `G` gives, for every `i,j`,

```text
ell_i<ell_j iff r_i<r_j.                             (2.4)
```

Noncontainment within `F` gives

```text
ell_i<ell_j iff r_(i-1)<r_(j-1).                    (2.5)
```

Combining (2.4)--(2.5) says that the nontrivial cyclic shift
`i -> i-1` preserves a strict total order on the cycle vertices.  A finite
strict total order has no nonidentity order-preserving cyclic permutation.
Contradiction.  ∎

Therefore `L union R` is a linear forest in `C(F,G)`, so

```text
lambda(F,G)>=|L|+|R|>=2(V-n).
```

Rearranging and using integrality gives

```text
n>=ceil(V-lambda/2)=V-floor(lambda/2),
```

proving (1.1).  The argument remains valid when `V<=n`; the endpoint
intersection lower bounds may then be nonpositive, but the same algebraic
inequality is still valid.

## 3. Exact finite optimization

The checker `scratch/check_two_antichain_endpoint_forest.py` performs three
independent computations.

1. It exhausts pairs of noncontaining interval families through five
   physical positions and confirms that their shared-left/shared-right graph
   is always a forest.
2. It exhausts every disjoint pair of antichains in the punctured cubes
   through `k=4`, computing `lambda` exactly by branch-and-bound.
3. At `k=5`, it exhausts all `7,580` punctured-cube antichains and all
   `704,639` disjoint pairs with combined size at least twelve.  For every
   such pair it explicitly constructs a linear forest large enough to prove
   the value at most eleven.  The two full middle layers have a 19-edge
   Hamilton path and attain eleven.

The exact results are

| `k` | Boolean width `W(k)` | rank-count `B(k)` | `B_forest(k)` |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 2 | 2 | 2 | 2 |
| 3 | 3 | 4 | 4 |
| 4 | 6 | 7 | 6 |
| 5 | 10 | 12 | 11 |

Thus the new theorem is correct, but it does not dominate the rank-count
bound even in the first nontrivial dimensions.

## 4. Full rank-layer pairs: exact in every dimension

For two complete distinct rank layers, the comparability graph is the usual
Boolean inclusion graph.  If their sizes are `f,g`, then exactly

```text
lambda=min(2 min(f,g), f+g-1).                      (4.1)
```

The upper bound is elementary: degrees are at most two and a forest on
`f+g` vertices has at most `f+g-1` edges.  For the matching lower bound use
[Mütze--Su, Lemma 12](https://arxiv.org/abs/1503.09175).  If the smaller
layer has rank `p` and the larger one rank `q`, after complementing both
layers if necessary we have

```text
p<q and p+q<=k.
```

Lemma 12 gives a cycle alternating through every `p`-set and selected
`(p+1)`-sets, together with vertex-disjoint monotone paths from those
selected vertices through every rank up to `k-p`.  Replace each selected
`(p+1)`-vertex on the cycle by the rank-`q` vertex of its own path.  The
replacement vertices are distinct, contain the old vertices, and remain
comparable to both neighboring `p`-sets.  This produces a cycle saturating
the entire smaller layer.

If `f=g`, delete one cycle edge and obtain `f+g-1` edges.  If, say, `f<g`,
choose an unused larger-side vertex and one of its smaller-side neighbors;
delete one cycle edge at that neighbor and attach the unused vertex there.
The result is a linear forest with `2f` edges.  This proves (4.1).

The resulting endpoint-forest value is the larger layer size when `f!=g`,
and `f+1` when `f=g`.  Maximizing over complete layers therefore gives

```text
W(k)       for even k,
W(k)+1     for odd k>=3,
1          for k=1.                                (4.2)
```

In particular, the previously checked finite values are

| `k` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| max full-layer bound | 1 | 2 | 4 | 6 | 11 | 20 | 36 | 70 | 127 | 252 | 463 | 924 |

At the first open cube this gives only `463`, below `B(11)=465`.  Formula
(4.2) now certifies every complete rank-layer pair through `k<20`, and in
fact in every dimension.  Arbitrary-antichain optimization is still
exhausted only through `k=5`; the number of antichains makes direct
enumeration infeasible beyond that point.

## 5. Interpretation

The theorem uses genuine joint left/right endpoint information and therefore
lies outside the scalar blocker barrier.  Its acyclicity mechanism is real.
The finite optimization nevertheless shows that two antichains alone do not
automatically recover the additive rank slack.

The next plausible strengthening would have to retain three or more witness
families simultaneously, or remember which comparable edges are demanded by
several endpoint forests.  Simply optimizing a pair of complete rank layers
does not improve the current lower bound.
