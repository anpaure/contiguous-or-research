# The first legal nonlocal Haar circuit

## 1. Statement

Let `n=9`, so the middle rank is `m=4`.  For an omitted-label cyclic
order `q=(q_0,...,q_8)`, put

\[
 I_i^{(r)}(q)=\{q_i,q_{i+2},\ldots,q_{i+2r-2}\},
 \qquad
 B_re_q=\sum_{i\in\mathbb Z_9}e_{I_i^{(r)}(q)}.
\]

There is a support-feasible four-for-four trade `w` with

\[
                 B_4w=B_3w=0,
        \qquad   B_2w\ne0.                            \tag{1.1}
\]

Thus the exact wreath-factor fibre really does contain a nonlocal Haar
direction: it preserves the middle layer and the first lower shadow while
changing the second lower shadow.  This is the first rank for which such a
direction can exist, since at `m=3` the second lower shadow is rank one and
is constant for every collection of the same number of cyclic orders.

## 2. The eight orders

The negative orders are

```text
1 8 6 7 4 5 3 9 2
1 9 8 6 7 4 5 2 3
1 5 3 9 8 6 7 2 4
1 7 3 9 4 5 8 2 6
```

and the positive orders are

```text
1 9 3 5 4 7 6 8 2
1 5 4 7 6 8 9 2 3
1 7 6 8 9 3 5 2 4
1 8 5 4 9 3 7 2 6
```

Write `N` and `P` for these two four-order families and put

\[
                         w={\bf1}_P-{\bf1}_N.          \tag{2.1}
\]

The four middle wreaths on each side are pairwise disjoint.  Direct
enumeration of the `4*9` intervals on each side gives

\[
                         B_4{\bf1}_P=B_4{\bf1}_N,      \tag{2.2}
\]

so (2.1) is a legal exact-middle trade.

At the first lower rank, direct cancellation of the `4*9` triples gives

\[
                         B_3w=0.                       \tag{2.3}
\]

At rank two the surviving effect is

\[
\begin{aligned}
B_2w={}&-e_{13}+e_{23}+e_{14}-e_{24}
        +e_{15}-e_{25}-e_{19}+e_{29}.                 \tag{2.4}
\end{aligned}
\]

In particular the deeper effect is nonzero.  Formula (2.4) can also be
read as two elementary square effects sharing the coordinate pair
`{1,2}`.

## 3. Exact-factor completion

The following ten orders are common to two exact factors containing the
two sides of the trade:

```text
1 4 6 9 7 8 5 3 2
1 6 5 7 3 9 8 4 2
1 3 8 6 7 5 9 4 2
1 4 6 2 8 9 5 7 3
1 4 6 5 2 9 7 8 3
1 5 4 2 6 9 7 8 3
1 8 6 7 5 9 2 3 4
1 8 7 9 4 2 5 3 6
1 7 2 3 5 9 8 4 6
1 8 7 9 2 3 4 5 6
```

Appending `N` gives one exact factor and appending `P` gives another: in
each case their fourteen wreaths enumerate all

\[
                         \binom94=126
\]

middle sets exactly once.  Therefore the trade is not merely a signed
kernel relation; it is the difference of two actual `0/1` exact factors.

The factor was reached from the MSW factor by three component switches,
using coordinate transpositions

\[
                     (1\ 3),\quad(2\ 4),\quad(1\ 5),  \tag{3.1}
\]

and `N -> P` is one connected interaction-component switch for the final
transposition `(1 2)`.  The reachability information explains why this
circuit is absent from the component cube at the original MSW factor: the
three preparatory switches create it.

## 4. Verification

The standalone verifier

[verify_nonlocal_haar_m4.cpp](./verify_nonlocal_haar_m4.cpp)

checks, independently:

1. pairwise middle-wreath disjointness on each four-order side;
2. exact completion of both fourteen-order factors;
3. `B_4w=0`;
4. `B_3w=0`; and
5. the eight-term nonzero effect (2.4).

The discovery search was run remotely in the visible `tmux` session
`nonlocal_haar`; the certificate itself is a direct finite proof and does
not depend on the search.

## 5. What this does and does not prove

This settles the existence question at the first nontrivial dimension and
invalidates any proposed theorem that the first-shadow map is injective on
the entire exact-factor fibre.  It does **not** yet give an all-`m` family.

Two naive suspensions were tested and fail already from `m=4` to `m=5`:

* inserting one common adjacent pair at a common gap of all eight orders;
* inserting two new labels antipodally while preserving each old cyclic
  order.

The remaining all-dimensional target is therefore a genuine commutator
lift: reproduce the three preparatory component switches and the final
four-for-four component inside a Dyck prefix/suffix context, rather than
padding the finished eight-order identity after the fact.
