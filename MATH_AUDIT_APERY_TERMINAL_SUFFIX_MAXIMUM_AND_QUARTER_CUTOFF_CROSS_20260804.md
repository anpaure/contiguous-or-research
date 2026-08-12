# Cross-audit: terminal suffix maxima and the quarter cutoff

**Date:** 2026-08-04  
**Method:** independent symbolic audit only; no search, numerical experiment,
or computational construction.

**Audited lemma:**
`MATH_LEMMA_APERY_TERMINAL_SUFFIX_MAXIMUM_AND_QUARTER_CUTOFF_20260804.md`,
SHA256
`6ef133e15f8635db9a91fb837ef2df65fadedc6a52ff923b0b5895f215324639`.

## 0. Verdict

The suffix-maximum theorem, reflected envelope, spacing bound, and integer
quarter count are correct for every `h>=2`.  I made three proof-scope
repairs:

1. the spacing statement now carries its necessary range `1<=i<h-1`;
2. the period-two prefix/minimum-gap case is discharged directly rather
   than silently invoking a dependency stated for `h>=3`; and
3. the reflected-ray application now explicitly assumes
   `0<X_i<=Y_i<1/2` and attributes the numerical period-eight and period-nine
   margins to the additional pair/theta estimates in their cited theorems.

No substantive inequality changes.

## 1. Complement duality

Write the cyclic gaps in their distinguished order as

\[
 \gamma_1,\gamma_2,\ldots,\gamma_h,
 \qquad
 \sum_{j=1}^h\gamma_j=P.
\tag{1.1}
\]

Fix `1<=i<h`.  Complementation in the cyclic `h`-set of gap positions maps
every consecutive `(h-i)`-block to the complementary consecutive `i`-block.
It is a bijection, and the two block sums add to `P`.  Therefore a minimum
`(h-i)`-block is sent to a maximum `i`-block.

The distinguished initial block is

\[
 \gamma_1+\cdots+\gamma_{h-i}=s_{h-i}.
\]

Its complement is exactly

\[
 R_i=\gamma_{h-i+1}+\cdots+\gamma_h=P-s_{h-i}.
\tag{1.2}
\]

Prefix minimality therefore proves that `R_i` is a maximum cyclic
`i`-block.  There is no reversal-index ambiguity: on a circle the complement
of one consecutive arc is the other consecutive arc.

## 2. Average and sharp envelope

There are `h` cyclic `i`-blocks.  Each gap belongs to exactly `i` of them,
so the sum of all their sums is `iP`, and their average is `iP/h`.  Hence

\[
                         R_i\ge {iP\over h}.
\tag{2.1}
\]

Under exact first carry, `A=P+a` and `alpha=a/A`, so

\[
 {P\over A}=1-\alpha,
 \qquad
 Y_i={A-s_{h-i}\over A}={a+R_i\over A}.
\tag{2.2}
\]

Substitution in (2.1) gives the claimed universal envelope

\[
 \boxed{
 Y_i\ge\alpha+{i\over h}(1-\alpha)
 }
 \qquad(1\le i<h).
\tag{2.3}
\]

It is sharp: for equal gaps, `P=ha`, exact carry gives
`alpha=1/(h+1)` and equality holds in (2.3) for every `i`.

## 3. Spacing

For `1<=i<h-1`, both endpoints are defined and direct subtraction gives

\[
 Y_{i+1}-Y_i
 ={s_{h-i}-s_{h-i-1}\over A}
 ={\gamma_{h-i}\over A}.
\tag{3.1}
\]

The length-one instance of prefix minimality says that
`gamma_j>=gamma_1=a` for every gap.  Consequently

\[
 \boxed{Y_{i+1}-Y_i\ge\alpha}
 \qquad(1\le i<h-1).
\tag{3.2}
\]

For `h=2` there is only `Y_1`, so (3.2) is correctly vacuous.  The honest
period-two carry inequality is `P>=2a`; it directly gives
`gamma_2=P-a>=a`, which supplies the same minimum-gap premise without using
the `h>=3` version of the general dependency.

## 4. Quarter cutoff and exact integer count

If an allowed integer index satisfies `i>=h/4`, then (2.3) gives

\[
 Y_i\ge\alpha+{1-\alpha\over4}
 ={1\over4}+{3\alpha\over4}>{1\over4},
\tag{4.1}
\]

because `a>0`.  Hence `Y_i<=1/4` is possible only when the positive integer
`i` satisfies `i<h/4`.

For every integer `h>=2`, the number of positive integers strictly below
`h/4` is

\[
 \left\lceil{h\over4}\right\rceil-1.
\tag{4.2}
\]

Indeed, writing `h=4q+r`, `0<=r<=3`, the count is `q-1` when `r=0` and `q`
when `r>0`, exactly as in (4.2).  Thus the formula handles all small periods
and all multiples of four without an endpoint exception:

\[
\begin{array}{c|c}
h&\text{maximum number at or below }1/4\\ \hline
2,3,4&0\\
5,6,7,8&1\\
9,10,11,12&2.
\end{array}
\tag{4.3}
\]

For example, at `h=4` the first valid index already satisfies equality in
the hypothesis `i>=h/4`, and (4.1) is still strict.

The same substitution proves the general cutoff

\[
 {i\over h}\ge {q-\alpha\over1-\alpha}
 \quad\Longrightarrow\quad Y_i\ge q,
\tag{4.4}
\]

for `0<q<1`.  When `q<=alpha`, the right-hand threshold is nonpositive and
the implication simply applies to every allowed positive index.

## 5. Exact scope of the reflected-ray consequence

The quarter classification uses more than (4.1): for the indices retained
in the reflected-ray ledger, the cited exact identity also proves

\[
                         0<X_i\le Y_i<1/2.
\tag{5.1}
\]

If `Y_i>1/4`, then exactly one of the following holds:

* `X_i>=1/4`, so both endpoints lie in `[1/4,1/2)` and decreasingness of
  the compact train gives `f(X_i)>=f(Y_i)`; or
* `X_i<1/4<Y_i`, so the pair crosses the quarter point and separate
  lower/upper train estimates are required.

Thus only indices `i<h/4` can have an entire pair at or below the quarter
point, and their number is bounded by (4.2).  The location lemma alone does
not numerically control the crossing pairs.  In particular:

* the period-eight margin `859/210000` additionally uses its `H=3`, pair,
  theta, and middle-train estimates; and
* the period-nine closure additionally uses the two-ninth monotonicity
  anchor and its own pair/theta estimates.

Therefore the audited lemma is a correct all-period geometric reduction,
not an all-period positivity theorem.  Its remaining early bank has size
`ceil(h/4)-1`, which grows with `h` and still requires a uniform
quadrature/overlap argument.
