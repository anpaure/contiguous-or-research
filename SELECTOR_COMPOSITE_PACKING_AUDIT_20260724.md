# Selector composites: a legal isolated trade, a parity obstruction, and a small-support no-go

Date: 2026-07-24

## 1. Summary

The elementary Petr--Turek square is rank-isolated but neither of its two
signs is a middle packing.  A natural next question is whether several such
squares can be combined so that the surviving positive orders and surviving
negative orders are separately middle-disjoint.

The finite answer at (n=9,m=4) has two layers.

1. Packing compatibility and rank isolation *can* coexist: there is an
   explicit (3)-for-(3) legal wreath trade which preserves ranks (2)
   and (4) and changes only rank (3).
2. That trade is not an integral sum of rank-(3) Petr--Turek squares.  A
   cyclic-order parity functional gives a one-line mod-(2) certificate.
   In fact, every rank-isolated alternative replacing at most six rows of
   the archived (Q_9) factor reduces to this same obstructed core trade.

An independent connected-composite search also proves that, for either
selector rank (2) or (3), no sum of at most six *distinct*,
unit-coefficient selector squares has middle-disjoint positive and negative
supports.

Thus merely summing a handful of selectors does not bridge the integral
gap.  On the other hand, the legal (3)-trade shows that the obstruction is
specifically the selector lattice, not rank isolation or packing geometry
by themselves.

No asymptotic wreath decomposition or coefficient-one OR theorem is claimed.

## 2. Audit of the elementary obstruction

The proof in `RANK_ISOLATED_SELECTOR_INTEGRAL_OBSTRUCTION_20260724.md` is
correct after two presentational repairs:

* the corrupted symbols for \(\tau\) and \(\sigma\) were restored;
* the proof only establishes the required lower bound of (n-4) common
  middle intervals.  Distinct affected starts alone would not rule out an
  accidental additional coincidence, so the unnecessary assertion of exact
  equality was removed.

The finite checker

```text
python3 scratch/analyze_rank_isolated_wreath_squares.py \
  m4_vertical_wreath_factor.txt
```

still returns

```text
factor=m4_vertical_wreath_factor.txt n=9 m=4 rows=14
distinct PT squares=80640 applicable=0
rank-isolation identities checked=80640
rank=2 holes=0 energy=28 applicable=0 isolated_ok=0 delta_hist={}
  diagonal occupancy census={(0, 0): 40208, (0, 1): 56, (1, 0): 56}
rank=3 holes=0 energy=2 applicable=0 isolated_ok=0 delta_hist={}
  diagonal occupancy census={(0, 0): 40208, (0, 1): 56, (1, 0): 56}
```

For (n=9), a direct all-square census also gives exactly five common
middle intervals on each diagonal, but this exact finite value is not used.

## 3. An explicit legal rank-(3)-isolated trade

Write a cyclic order by its representative beginning with (1), modulo
reversal.  Let the old side be

\[
\begin{aligned}
O_1&=(1,2,4,7,6,9,3,8,5),\\
O_2&=(1,3,7,9,2,6,5,8,4),\\
O_3&=(1,4,7,6,3,2,5,8,9),
\end{aligned}
\tag{3.1}
\]

and let the new side be

\[
\begin{aligned}
N_1&=(1,2,4,7,6,3,9,8,5),\\
N_2&=(1,3,8,5,2,9,6,7,4),\\
N_3&=(1,4,8,5,6,2,3,7,9).
\end{aligned}
\tag{3.2}
\]

### Proposition 3.1

Each side of (3.1)--(3.2) is a middle packing, the two sides cover exactly
the same (27) middle (4)-sets, and their rank-(2) incidence vectors are
equal.  Their rank-(3) difference is nonzero.  More precisely, the old-only
rank-(3) targets are

\[
137,\quad 189,\quad 235,\quad 279,
\tag{3.3}
\]

whereas the new-only targets are

\[
138,\quad 179,\quad 237,\quad 259.
\tag{3.4}
\]

#### Proof

List the nine cyclic intervals at ranks (2,3,4) in each displayed order.
Exact multiset comparison gives

\[
 A_2(O_1+O_2+O_3)=A_2(N_1+N_2+N_3),
\]

\[
 A_4(O_1+O_2+O_3)=A_4(N_1+N_2+N_3),
\]

and (3.3)--(3.4) give the nonzero (A_3)-difference.  On each side the
(27) middle intervals are distinct, so both signs are genuine partial
wreath packings.  Rank (1) is automatic because every cyclic order contains
each singleton exactly once.  The executable audit performs these comparisons
directly.
\(\square\)

This is already a useful correction to the heuristic suggested by a single
selector square: legal rank-isolated factor trades exist in the smallest
defective odd dimension, just not as one elementary square.

## 4. The cyclic-order parity obstruction

For an unoriented cyclic order on ([9]), rotate it to begin with (1) and
take the parity of the resulting permutation.  Reversing the orientation
reverses the remaining eight entries and changes parity by

\[
 (-1)^{\binom 82}=1.
\]

Thus this parity is well-defined on an unoriented wreath column.  Let

\[
 \chi(C)=1
 \quad\Longleftrightarrow\quad
 C\text{ is odd}.
\tag{4.1}
\]

### Lemma 4.1

For every Petr--Turek selector square (z),

\[
 \sum_C \chi(C)z_C=0\pmod 2.
\tag{4.2}
\]

#### Proof

The two adjacent transpositions defining a square each reverse permutation
parity.  Its four orders therefore consist of two even and two odd orders.
Modulo two the signs of the square disappear, so its scalar product with
\(\chi\) is zero.  The same is true for every integral sum of squares.
\(\square\)

All three old orders in (3.1) are even and all three new orders in (3.2)
are odd.  Therefore their signed difference has

\[
 \sum_C\chi(C)z_C=3=1\pmod2.
\tag{4.3}
\]

### Corollary 4.2

The legal rank-(3)-isolated trade (3.1)--(3.2) is not an integral signed
sum of rank-(3) Petr--Turek selector squares.

This is stronger than a failure to find a short decomposition: (4.3)
excludes an integral decomposition of every length and with arbitrary
integer coefficients.

More generally, for (n=2m+1) with even (m), reversal of an unoriented
cyclic order preserves permutation parity, so the same mod-(2) selector
invariant is available.  For odd (m), reversal flips parity and this
particular functional does not descend to unoriented columns.

## 5. Exact factor-relative census through six rows

The script

```text
python3 scratch/search_rank_isolated_packing_trades.py \
  m4_vertical_wreath_factor.txt --max-k 6
```

enumerates every alternative decomposition of the middle masks belonging to
each (k)-subset of the archived (14)-row factor, for (2\le k\le6).
It checks exact middle packing, every lower shadow, and membership modulo two
in the corresponding selector-square span.  The isolated census is

\[
\begin{array}{c|ccccc}
k&2&3&4&5&6\\ \hline
\text{rank-isolated alternatives}&0&1&11&55&165\\
\text{passing the selector GF(2) test}&0&0&0&0&0.
\end{array}
\tag{5.1}
\]

The numbers in the first row after (k=3) are

\[
 1,\binom{11}{1},\binom{11}{2},\binom{11}{3}.
\]

Direct inspection confirms what these counts suggest: every isolated entry
in this range is the same core trade (3.1)--(3.2), with (k-3) unchanged
factor rows adjoined to both sides.  After common rows cancel, (4.3) remains,
so every case fails the selector-lattice test.

This census is relative to the archived factor; it is not an enumeration of
all partial packings on nine points.

## 6. A direct six-square no-go

The second script searches sums of selector squares themselves:

```text
python3 scratch/search_packing_selector_composites.py \
  --m 4 --rank 3 --max-squares 6
```

and analogously with `--rank 2`.  For both ranks it returns

```text
depth=1 nodes=1 states=0 found=False
depth=2 nodes=21 states=1 found=False
depth=3 nodes=629 states=21 found=False
depth=4 nodes=17917 states=445 found=False
depth=5 nodes=176065 states=3842 found=False
depth=6 nodes=1222517 states=24588 found=False
```

### Proposition 6.1

At (m=4), for selector rank (2) or (3), no nonzero sum of at most six
distinct selector-square vectors with coefficients in \(\{-1,1\}\) has all
surviving coefficients in \(\{-1,1\}\) and has separately middle-disjoint
positive and negative supports.

#### Exhaustiveness of the finite search

All selector squares of a fixed rank form one orbit under coordinate
relabeling, so the first square and its sign may be fixed.  If the
square--order incidence graph of a composite has several components, then
each component's surviving sign supports are subsets of the corresponding
global sign supports.  A nonzero minimal composite therefore has a nonzero
connected component which is itself packing-compatible.

At an intermediate state, call a row bad if its coefficient is not
\(\pm1\), or if it shares a middle interval with another row having the same
sign.  Every completion with a bad state must contain a remaining square
incident with at least one bad row.  Since summation is commutative, such a
square may be chosen next.  The depth-first search branches over every unused
incident square and both signs; its memoization key contains the full
coefficient state, remaining depth, and exact used-square set.  Its only
depth pruning is the maximum of two sound touch bounds: coefficient-bad rows
and the size of a greedily chosen matching in the same-sign conflict graph,
each divided by the four orders available in one square.  These observations
prove that the printed search is exhaustive for the stated distinct,
unit-coefficient scope.

The proposition does not exclude a composite using seven or more squares,
or one having a square coefficient of magnitude greater than one.

## 7. Consequence for the program

There are now three sharply separated facts.

* Petr--Turek squares give exact real-linear rank selectors.
* Legal rank-isolated partial wreath trades already exist at (m=4).
* The first legal isolated trade lies outside the integral selector lattice,
  and no genuine unit-selector composite exists through seven squares.

The next constructive target should therefore not be phrased merely as
"sum a few selector squares."  One needs either

1. a larger selector composite which also defeats the mod-(2) invariants;
2. a different family of integral rank-local generators; or
3. packing-compatible balanced switches with quantitatively small, rather
   than identically zero, leakage into the other Gaussian-weighted ranks.

The third option remains the most directly aligned with the established
balanced-(C_8) switching and weighted-overload framework.
