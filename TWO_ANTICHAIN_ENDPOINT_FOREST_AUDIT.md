# Independent audit of the two-antichain endpoint-forest theorem

## Verdict

**PASS.**  The shared-endpoint matchings, the claim that their union is
acyclic, and the rounded lower bound

```text
n>=|F|+|G|-floor(lambda(F,G)/2)
```

are valid.  No alternating-cycle counterexample exists: the cyclic shift
would have to preserve the strict endpoint order induced independently by
both antichains.

The exact computational claims through `k=5` pass.  The theorem is a genuine
non-scalar endpoint consequence, but its optimized value is smaller than the
rank-count bound at `k=4,5`.  Full rank-layer pairs give only width (even) or
width plus one (odd), now proved in every dimension.

## 1. Endpoint matching audit

Within one antichain, two selected intervals cannot contain each other.
Hence their left and right endpoints are separately distinct, and sorting by
one endpoint sorts by the other.  Intersection of two endpoint sets of sizes
`|F|,|G|` in `[n]` has size at least `|F|+|G|-n`.  A shared endpoint nests the
two intervals and therefore gives a cross-comparability edge.  Since endpoint
sets are injective within each family, the shared-left and shared-right edges
are matchings.

A pair cannot share both endpoints: it would assign two distinct target ORs
to one physical interval.  Thus the two matchings are edge-disjoint.

## 2. Acyclicity audit

On a putative alternating cycle, the interval identities are

```text
G_i=[ell_i,r_i],  F_i=[ell_i,r_(i-1)].
```

The `G` antichain says the order of `(ell_i)` equals the order of `(r_i)`.
The `F` antichain says the order of `(ell_i)` equals the order of
`(r_(i-1))`.  Hence cyclic shift preserves a finite strict total order.  A
nontrivial cycle shift cannot do this.  This rules out every cycle length,
not merely four-cycles.

The checker independently enumerates all noncontaining interval-family pairs
through five positions, constructs both endpoint matchings, and tests the
resulting graph directly for cycles and degree violations.

## 3. Rounding and definition of `lambda`

The actual endpoint graph is a linear-forest subgraph of `C(F,G)`, so

```text
lambda>=2(V-n).
```

Rearrangement gives `n>=V-lambda/2`.  Since `V,n,lambda` are integral,

```text
ceil(V-lambda/2)=V-floor(lambda/2).
```

The maximum in the definition of `lambda` is essential.  Replacing it by a
maximum matching or by the number of all comparable pairs would not justify
the same inequality.

## 4. Computational audit

For `k<=4`, every disjoint antichain pair is enumerated and `lambda` is
computed exactly by an include/exclude search that maintains degree at most
two and a rollback disjoint-set forest.

At `k=5`, pairs of combined size at most eleven are automatically bounded by
eleven.  For all 704,639 larger disjoint pairs, the checker constructs a
specific acyclic degree-two subgraph with at least `2(V-11)` edges.  This
proves their endpoint value is at most eleven without assuming that the
constructed forest is maximum.  The complete rank-two/rank-three pair has a
19-edge forest, the absolute `V-1` cap, and attains eleven.  Hence the stated
value is exact.

For full layers through `k=8`, every computed forest reaches the elementary
part-size cap (4.1), proving exactness.  Through `k=12`, explicit deterministic
forests bound every noncentral pair by the displayed maximum, while the odd
central case uses the established middle-levels Hamilton cycle.  Claims
beyond that range are deliberately not made.

## 5. Full rank layers and scope

The later all-dimensional evaluation of complete rank-layer pairs also
passes.  Mütze--Su Lemma 12 supplies a cycle through the whole smaller layer
and vertex-disjoint monotone lifts of its opposite cycle vertices.  Taking
the lift vertex at the desired second rank gives a smaller-side-saturating
cycle in any two-layer inclusion graph (complementation handles the reversed
rank regime).  Deleting one edge proves the equal-size cap; when the larger
side has an unused vertex, breaking the cycle at one of its neighbors and
reattaching to that vertex proves the unequal-size cap.  Therefore

```text
lambda=min(2 min(f,g),f+g-1)
```

for all complete rank-layer pairs, not merely those checked computationally.
Their maximum is width in even dimensions and width plus one in odd
dimensions `k>=3`.

This theorem does not imply that `B_forest(k)` improves `B(k)`, and the finite
data point the other way.  Exhaustive arbitrary-antichain optimization beyond
`k=5` remains open.  A random or greedy forest supplies a lower bound on
`lambda` and hence an upper bound on one candidate's endpoint expression; it
must not be mistaken for an exact maximum unless it reaches an independent
upper cap.
