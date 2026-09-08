# Independent audit: endpoint-blocker barrier and containment spectrum

## Verdict

**PASS, with two proof-completion notes and one scope clarification.**

The fractional containment cap, the targetwise Dilworth optimum, the formula

```text
omega(k,s)=C(k,ceil(k/2))-C(s,ceil(k/2))
```

for `s<k`, and the collapse of the complete targetwise containment-spectrum
Hall hierarchy to `B(k)` are valid.  In particular, the argument really does
prove the previously useful but apparently unrecorded fact that the upper
central rank always maximizes the rank-count lower bound:

```text
B(k)=C(k,ceil(k/2))+tau(k,ceil(k/2)).
```

The arbitrary-antichain barrier is also valid in the stated ranges.  In fact,
it follows immediately from the complete targetwise hierarchy and therefore
holds for every `k`, without the range restrictions in Theorem 5.  The
displayed LYM proof is nevertheless correct in its advertised ranges.

The two missing proof sentences are:

1. to justify `H(k)>=B(k)`, observe that for every `q` and every target
   `T` of rank below `q`, the complete rank-`q` layer is an antichain in
   `P_T`; hence `omega(T)>=C(k,q)` and the Hall row at
   `t=n-C(k,q)` contains the rank-`q` rank-count inequality;
2. the broad fractional conclusion should be grounded in pointwise
   domination by the optimal caps, not merely in the final support-antichain
   paragraph.  For every chain-feasible weighting `x`,

   ```text
   sum_(S not subseteq T) x_S <= omega(T),
   ```

   so its cap for every target is no stronger than `lambda_n(k,|T|)`.
   Therefore the complete optimal-cap Hall hierarchy dominates the entire
   Hall hierarchy of every fixed fractional blocker, including targets with
   intermediate (not just zero) contained weight.

These are short completions, not changes to the theorem.  The standard
normal-poset product theorem used to identify the width of `P_T` should be
cited in a publication version.  The result rules out scalar endpoint-fibre
blocker/Hall arguments; it does not rule out nonnested competition for named
cells, joint left/right order, precedence cycles, or coordinate pins.

The independent checker
`scratch/check_blocker_barrier.py` passes.  It verifies exact poset widths by
Dilworth matching through `k=7`, central maximization and the Hall collapse
through `k=200`, every antichain of the punctured cube through `k=5`, and
deterministic non-level random antichains for every `9<=k<20`.

## 1. Fractional containment cap

At one left endpoint, the selected witness labels form an inclusion chain;
the chain constraint therefore gives total starting weight at most one.
The analogous statement holds at one right endpoint.  If `J=[a,b]`, the
total weight of witnesses not contained in `J` is at most

```text
(a-1)+(n-b)=n-|J|.
```

A witness contained in `J` has target contained in `U(J)`.  Rearrangement
gives exactly

```text
|J| <= n-Theta+sum_(S subseteq U(J)) x_S.
```

Double-counting witnesses that both begin before `a` and end after `b` only
makes the outside-weight upper bound weaker, so there is no hidden
multiplicity error.

## 2. Optimal blocker for one target

For fixed `T`, unit weight on a maximum antichain of

```text
P_T={nonempty S:S not subseteq T}
```

gives the cap `n-width(P_T)`.  Conversely, Dilworth partitions `P_T` into
`width(P_T)` chains, and any chain-feasible weighting has total weight at
most one on each chain.  Thus fractionalization cannot beat the ordinary
maximum antichain for that target.

If `|T|=s`, then

```text
P_T isomorphic to B_s x (B_(k-s) minus {empty}).
```

The two factors are normal with log-concave rank numbers, so the standard
product-normality theorem makes the product Sperner.  Its rank-`j` number is

```text
D_j=C(k,j)-C(s,j).
```

The rank sequence is unimodal.  A symmetric-chain injection below the middle
shows `D_(r-1)<=D_r` for `r=ceil(k/2)`.  The displayed even/odd ratio
calculations correctly show `D_(r+1)<=D_r`; when `s<r`, the conclusion is
immediate from `D_r=W`.  Hence

```text
width(P_T)=D_r=W-C(s,r).
```

The matching-based checker independently computes the width of the actual
comparability poset, rather than assuming the rank formula, for all targets
through `k=7`.

## 3. Complete Hall hierarchy and central maximization

At `n_0=W+d`, where `d` is the central rank slack, the optimal caps are

```text
d                         for 1<=s<r,
d+C(s,r)                  for r<=s<k,
n_0                       for s=k.
```

At `t=d`, Hall is exactly the central rank-count inequality.  At the next
breakpoint `t=d+u`, where `u=C(s,r)` and `h=s-r+1`, the extra interval
capacity is

```text
uW-C(u,2).
```

For `s=r` this is exactly `W`.  For `s>r` and `r>=3`, the elementary bounds
`u>=2h` and `u<=W` give

```text
uW-C(u,2) >= hW,
```

which covers all targets in ranks `r,...,s`.  The remaining small dimensions
check directly, as does the final full-set breakpoint.  Since no target set
changes between breakpoints, this proves every Hall row at `n_0`.

For completeness, `H(k)>=B(k)` follows as follows.  If `|T|<q`, the entire
rank-`q` layer lies in `P_T`, and is an antichain.  Hence

```text
lambda_n(T)=n-omega(T) <= n-C(k,q).
```

The Hall inequality at the latter length includes every target below rank
`q`, and is precisely the rank-`q` scalar inequality.  Taking all `q` gives
`H(k)>=B(k)`.  Combining this with feasibility at `n_0` proves

```text
H(k)=B(k)=n_0.
```

The checker confirms this identity, central maximization, Hall feasibility
at `B(k)`, and Hall failure at `B(k)-1` for every `1<=k<=200`.

## 4. Arbitrary antichains

The separate LYM proof is arithmetically sound.  Writing
`|A|=W-delta` and splitting below/at/above the upper central rank gives a
family of at most `delta+z` surviving central sets.  Every avoiding target
at or above the middle can be charged to one of them, with multiplicity at
most `2^(k-r)`.  LYM yields

```text
z<=delta*m                 for k=2m,
z<=delta*m/2               for k=2m+1.
```

This produces the stated avoidance bounds.  The interval-capacity increment

```text
I(n_0,d+delta)-I(n_0,d)=delta*W-C(delta,2)
```

is at least `delta(W+1)/2`.  The two displayed central-binomial comparisons
hold from `m=6` (even) and `m=4` (odd), respectively, and their ratios are
strictly increasing thereafter.

There is also a shorter and stronger deduction.  If `T` avoids an antichain
`A` of size `q`, then `A subseteq P_T`, so `omega(T)>=q` and
`lambda_n(T)<=n-q`.  The complete Hall row at `t=n-q` therefore gives

```text
|Av(A)| <= I(n,n-q)
```

for every `k`.  Thus Theorem 5's conclusion needs no dimension threshold
once Theorem 4 is available.

## 5. Bounded-height and fractional scope

Mirsky partitions a height-`h` family into `h` antichains, so its uniform
weight `1/h` is chain-feasible.  More generally, for every chain-feasible
weighting and every target `T`, Dilworth gives

```text
excluded_weight(T)<=width(P_T)=omega(T).
```

Thus every resulting target cap is pointwise at least the optimal cap
already used in the complete Hall hierarchy.  This proves the intended
barrier for all scalar arguments of the form

```text
endpoint chain capacity -> targetwise maximum length -> nested interval Hall.
```

It does **not** apply once an argument remembers which particular interval
cells are demanded by different targets, couples two nonnested witness
families, uses both endpoint orders simultaneously, or enforces coordinate
pin survival.  Those are exactly the surviving directions identified in the
project handoff.

