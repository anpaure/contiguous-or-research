# The q4 k17 owner descent has a complete three-pair ejection-signature oracle

**Date:** 2026-08-14

**Status:** exact finite-pool algebra and pruning theorem.  It reduces every
three-reflected-pair exchange to 24,804 outgoing faces with exact distinct-
candidate exclusion minima and a complete retained pair/third-candidate
test.  No q4 pool has been searched with this oracle.

## 0. Exact score

Let `ell` be the current 680-row load vector.  For a ten-row candidate `N`
and selected ten-row configuration `P`, put

```text
a(N)=sum_(x in N)(2ell_x-1),
r(P)=sum_(x in P)(3-2ell_x).                                  (0.1)
```

Fix three distinct selected outgoing configurations
`R={P1,P2,P3}` and define

```text
c_R = sum_i r(P_i)+2 sum_(i<j)|P_i intersect P_j|,
h_R(N)=a(N)-2 sum_i |N intersect P_i|.                        (0.2)
```

> **Theorem 0.1 (exact three-pair score).**  For three distinct unselected
> incoming configurations `N1,N2,N3`,
>
> ```text
> Delta_3(R;N1,N2,N3)
>  =c_R+sum_i h_R(N_i)
>       +2 sum_(i<j)|N_i intersect N_j|.                      (0.3)
> ```

There is no triple-intersection correction.  The energy is quadratic, so
all interactions are pairwise; `(0.3)` remains exact on rows lying in all
six configurations.

## 1. Proof

For the signed atom `d_(P,N)=1_N-1_P`, square expansion gives

```text
Phi(ell+d1+d2+d3)-Phi(ell)
 =sum_i [Phi(ell+d_i)-Phi(ell)]
  +2 sum_(i<j)<d_i,d_j>.                                     (1.1)
```

The one-atom score is

```text
             r(P_i)+a(N_i)-2|P_i intersect N_i|.              (1.2)
```

Expanding the three scalar products in `(1.1)` gives all outgoing-
outgoing, incoming-incoming, and cross outgoing-incoming intersections.
Regrouping the first two classes into `c_R` and each incoming cross class
into `h_R` proves `(0.3)`.

Equivalently, the rowwise identity may be checked for arbitrary load `l`
and six membership bits.  The right side is exactly

```text
(l-p1-p2-p3+n1+n2+n3-1)^2-(l-1)^2.                           (1.3)
```

## 2. Exact exclusion minima and pruning

All minima below range over distinct unselected candidate indices.  Let
`m1<=m2<=m3` be the three smallest `h_R` values at distinct candidates.
Since the overlap term in `(0.3)` is nonnegative,

```text
                         c_R+m1+m2+m3>=0                       (2.1)
```

certifies the entire outgoing face nonnegative.

For one candidate `N`, let

```text
mu_2(N)=minimum of h_R(M)+h_R(L)
        over distinct M,L not equal to N.                     (2.2)
```

If `N` occurs in a negative exchange, necessarily

```text
                         c_R+h_R(N)+mu_2(N)<0.                 (2.3)
```

Thus `(2.3)` is a lossless necessary candidate-retention test.  Using
`2m1` instead of `mu_2(N)` is safe but weaker and does not enforce the
three-distinct-candidate requirement sharply.

For two retained distinct candidates define their ejection-pair score

```text
p_R(N,M)=h_R(N)+h_R(M)+2|N intersect M|,                      (2.4)
```

and let

```text
mu_1(N,M)=min {h_R(L):L not in {N,M}}.                        (2.5)
```

A pair belonging to a negative triple must satisfy

```text
                         c_R+p_R(N,M)+mu_1(N,M)<0.             (2.6)
```

Finally, for a retained pair, a third candidate can occur only if

```text
                         h_R(L)<-c_R-p_R(N,M).                 (2.7)
```

For candidates passing `(2.7)`, evaluate the exact remaining interaction

```text
                 2|L intersect N|+2|L intersect M|.            (2.8)
```

Equations `(2.1)`, `(2.3)`, `(2.6)`, and `(2.7)` are all strict where
required.  They discard no negative triple because each replaces only
nonnegative overlaps by zero or the other candidates by exact exclusion
minima.

## 3. Complete finite-pool algorithm

There are

```text
                              binom(54,3)=24,804                 (3.1)
```

outgoing faces.  On one face:

1. compute every `h_R(N)` and the first three distinct score minima;
2. apply the face cut `(2.1)`;
3. retain exactly candidates satisfying `(2.3)`;
4. enumerate retained pairs `N<M`, compute `(2.4)`, and apply `(2.6)`;
5. for each surviving pair `N<M`, scan retained `L>M` satisfying `(2.7)`
   and add `(2.8)`.

Every incoming triple has one canonical ordering `N<M<L`.  If it is
negative, all three candidates pass `(2.3)`, its canonical first pair
passes `(2.6)`, and its third member passes `(2.7)`.  Hence the algorithm
tests it.  Conversely every tested object is a legal triple of distinct
unselected candidates.  This proves completeness.

The exclusion minima are constant-time after sorting candidates by
`(h_R,index)`: inspect the first at most five entries to obtain `mu_2(N)`
or `mu_1(N,M)`.  Exact row overlaps use 680-bit masks.  If the retained
bank is large, bucket pairs by `p_R` and stop once
`c_R+p_R+min h_R>=0`; no arbitrary top-K truncation is justified.

## 4. Streamed and ejection-chain interface

A complete streamed target oracle needs two passes.

1. The first pass freezes the three distinct minima for each outgoing face.
2. The second emits every candidate passing `(2.3)`, tagged by its face
   score.
3. Pair construction and the exact third-candidate scan then run on the
   finite retained banks.

This is also an exact depth-three ejection-chain decomposition: choose the
three outgoing configurations, retain a first incoming candidate by its
two-part exclusion bound, retain its incoming partner by `(2.6)`, then
close with the third configuration and literal interaction `(2.8)`.

## 5. Scope

The theorem covers three distinct reflected-pair replacements while the 35
self lifts are fixed.  Pair+self+self, pair+pair+self, and three-self
exchanges require the same quadratic identity with group-specific incoming
menus, but are not claimed here.  A neutral three-pair pivot, missing
columns, and exchanges of depth at least four remain open even after a
finite-pool no-negative result.

## 6. Independent H100 replay

The synthetic verifier checks all 448 rowwise load/membership cases,
131,040 direct three-exchange scores, exact distinct-candidate exclusion
minima, every negative candidate and pair threshold, and equality between
the retained ejection scan and the complete negative-triple set.  One suite
has 35,690 negative triples; a disjoint exact-cover suite supplies twenty
nonvacuous dead faces.  It performs no q4 pool search.

```text
scratch/verify_q4_k17_exact_three_pair_exchange_ejection_oracle_20260814.py
sha256 610ce65f446e9974e3e16fe3aec1db5d198e2d0aad644afff4b0b3d082dbbc1a

scratch/verify_q4_k17_exact_three_pair_exchange_ejection_oracle_20260814.h100.out
sha256 89716cadfc61692412d94d4e793f9f1148013339c84f90c65f525d6141539310
status PASS
```
