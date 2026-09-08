# The q4 k17 owner descent has a complete four-pair oracle and a general exclusion recurrence

**Date:** 2026-08-14

**Status:** exact finite-pool algebra and pruning theorem.  It reduces the
`binom(54,4)=316,251` outgoing four-reflected-pair faces to a lossless
layered search with exact distinct-candidate exclusion minima.  The same
recurrence applies to every fixed exchange depth.  No q4 pool verdict is
claimed here.

## 0. Exact score at arbitrary depth

Let `ell` be the current row-load vector.  For a candidate configuration
`N` and selected configuration `P`, put

```text
a(N)=sum_(x in N)(2ell_x-1),
r(P)=sum_(x in P)(3-2ell_x).                                  (0.1)
```

Fix `k` distinct selected outgoing configurations
`R={P1,...,Pk}` and define

```text
c_R = sum_i r(P_i)+2 sum_(i<j)|P_i intersect P_j|,
h_R(N)=a(N)-2 sum_i |N intersect P_i|.                        (0.2)
```

> **Theorem 0.1 (exact k-exchange score).**  For distinct unselected
> incoming configurations `N1,...,Nk`,
>
> ```text
> Delta_k(R;N1,...,Nk)
>   =c_R+sum_i h_R(N_i)
>        +2 sum_(i<j)|N_i intersect N_j|.                    (0.3)
> ```

There are no intersections of order at least three in `(0.3)`: the
energy is quadratic, so all interactions are pairwise.

For a distinct incoming prefix `S`, define

```text
q_R(empty)=0,
q_R(S)=sum_(N in S)h_R(N)
       +2 sum_({N,M} subset S)|N intersect M|.                (0.4)
```

Then adjoining a new candidate has the exact recurrence

```text
q_R(S union {N})
 =q_R(S)+h_R(N)+2 sum_(M in S)|N intersect M|.                (0.5)
```

## 1. Proof of the score

For `d_i=1_(N_i)-1_(P_i)`, square expansion gives

```text
Phi(ell+sum_i d_i)-Phi(ell)
 =sum_i [Phi(ell+d_i)-Phi(ell)]
  +2 sum_(i<j)<d_i,d_j>.                                     (1.1)
```

The one-atom term is

```text
r(P_i)+a(N_i)-2|P_i intersect N_i|.                          (1.2)
```

Expanding the scalar products in `(1.1)` and grouping outgoing-outgoing
terms into `c_R`, all incoming-outgoing terms into the corresponding
`h_R`, and incoming-incoming terms last proves `(0.3)`.  Formula `(0.5)`
is the difference between `(0.4)` on `S union {N}` and on `S`.

## 2. General lossless exclusion recurrence

Let the finite incoming bank consist of distinct unselected candidate
indices.  For a prefix `S` and integer `t`, let

```text
mu_t(S)=minimum sum_(N in T) h_R(N)                           (2.1)
```

over all `t`-subsets `T` of the candidate bank disjoint from `S`.
Equivalently, `mu_t(S)` is the sum of the `t` smallest `h_R` values at
distinct indices outside `S`.

> **Theorem 2.1 (lossless prefix cut).**  If `|S|=j<k` and `S` is
> contained in a negative `k`-exchange, then
>
> ```text
>                   c_R+q_R(S)+mu_(k-j)(S)<0.                 (2.2)
> ```

Indeed, the remaining `k-j` candidates contribute at least
`mu_(k-j)(S)` through their `h_R` scores, while every omitted overlap with
the prefix or among the remaining candidates is nonnegative.  Thus the
left side of `(2.2)` is a lower bound for that completion.  This proves
necessity.  It is not a sufficient negativity test.

Sort candidates once by `(h_R,index)`.  To compute `mu_(k-j)(S)`, scan
only the first at most `(k-j)+j=k` sorted entries: at worst all `j`
excluded prefix indices occur first.  Hence every exclusion minimum is
constant-time for fixed `k`.

## 3. Complete four-pair oracle

For `k=4`, abbreviate `h=h_R`.  The face cut is

```text
c_R+mu_4(empty)>=0.                                          (3.1)
```

For a candidate `N`, a pair `N,M`, and a triple `N,M,L`, respectively,
the lossless necessary retention tests are

```text
c_R+h(N)+mu_3({N})<0,                                        (3.2)
c_R+q_R({N,M})+mu_2({N,M})<0,                                (3.3)
c_R+q_R({N,M,L})+mu_1({N,M,L})<0.                            (3.4)
```

For a surviving triple, a fourth candidate `K` can close negatively only
if

```text
                         h(K)<-c_R-q_R({N,M,L}).              (3.5)
```

Every candidate passing `(3.5)` is evaluated with the exact missing term

```text
            2|K intersect N|+2|K intersect M|+2|K intersect L|. (3.6)
```

The complete finite-pool algorithm is therefore:

1. compute `c_R`, every `h_R`, and `mu_4(empty)`;
2. apply `(3.1)` and retain candidates satisfying `(3.2)`;
3. enumerate retained canonical pairs `N<M` and apply `(3.3)`;
4. enumerate retained canonical triples `N<M<L` and apply `(3.4)`;
5. scan retained `K>L` satisfying `(3.5)` and add `(3.6)` exactly.

Every incoming four-set has one canonical ordering.  If it is negative,
each of its singleton, pair, and triple prefixes passes Theorem 2.1, and
its last candidate passes `(3.5)`.  Hence the algorithm tests it.
Conversely every tested object consists of four distinct unselected
candidates.  This proves completeness.

The scan may be streamed in two passes per outgoing face: the first pass
freezes its first four `(h_R,index)` entries (score ties are allowed); the second emits every
candidate passing `(3.2)`.  All later exclusion minima inspect the same
first four sorted entries.  Bitset intersections evaluate `(0.5)`.
Arbitrary top-K truncation is not lossless.

## 4. General fixed-depth oracle

For arbitrary fixed `k`, impose an index order on the incoming bank and
grow canonical prefixes.  At every prefix `S` of size `j<k`, apply
`(2.2)`; append only candidates with index larger than the last prefix
index and update `q_R` by `(0.5)`.  At size `k`, test the exact value
`c_R+q_R(S)`.  Induction on prefix length and Theorem 2.1 prove that the
resulting search finds exactly all negative `k`-exchanges.

This is an exact ejection-tree recurrence, not a polynomial-time claim:
the surviving prefix bank can still be large.  Its value is that every
cut is rigorous, distinct-candidate exclusions cost `O(k)` after sorting,
and the remaining combinatorial work is explicit rather than hidden by a
heuristic cap.

## 5. Scope

The four-pair specialization covers four distinct reflected-pair
replacements while the 35 self lifts are fixed.  Mixed pair/self moves
need the same quadratic recurrence with a type-specific menu and self-
group constraints; they are not claimed here.  A finite-pool no-negative
result would not rule out missing columns, neutral pivots, changing the
fixed matching, or exchanges at a different depth.

## 6. Independent H100 replay

The verifier exhausts the scalar four-out/four-in square identity, compares
the score to direct row-load changes on synthetic banks, checks every
prefix exclusion implication, and proves that the layered oracle returns
exactly the complete set of negative four-exchanges.  It also replays the
general recurrence at depths one through four.  It performs no q4 pool
search.

Verifier and output hashes are frozen in the accompanying audit.
