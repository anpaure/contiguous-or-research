# Gate C: direct miss-set tail for pivot flips

**Status (2026-08-22).** This is a proved strengthening of the pivot-flip
factorial-moment theorem.  If `G` is the number of two-sided-ballot cuts of
an order on `K=2e+1>=3` blocks, then for every `0<=R<K`,

\[
 \boxed{
 |\{\tau\in S_K:G(\tau)\ge K-R\}|
 \le \binom K{e+1}2^{K-R}e_R(n_0,...,n_{K-1}),}         \tag{0.1}
\]

where `e_R` is the elementary symmetric polynomial and

\[
 n_{2r}=e+1-r\ (0\le r\le e),\qquad
 n_{2r+1}=e-r\ (0\le r<e).                             \tag{0.2}
\]

Consequently

\[
 \boxed{
 |\{G\ge K-R\}|
 \le 4^K{((e+1)^2/2)^R\over R!}.}                     \tag{0.3}
\]

In particular there are fewer than `4^K` all-good linear orders.  At the
equal-block Gate-C scale, (0.3) improves the entropy exponent to
`O(b/log b)`.

## 1. The only input from the pivot filtration

For completeness, recall the exact filtration statement.  Color each
value by

\[
                         c_v=(-1)^{v+\sigma(v)},        \tag{1.1}
\]

where `sigma=tau^{-1}`.  Conditional on a realizable color vector, reveal
the values in position order.  Before position `p`, the threshold walk has
increments

\[
                 X_p(v)=c_v(-1)^{\mathbf1_{\sigma(v)<p}}.             \tag{1.2}
\]

The value selected at `p` is uniform among `n_p` unrevealed values
eligible for that position parity.  A good cut must select one of at most
two pivot increments of this walk: at most one up-step whose two endpoints
are the minima of their respective left and right halves, and at most one
analogous down-step at the two maxima.  Thus, if `I_p` is the pivot-hit
indicator,

\[
 G\le\sum_p I_p,
 \qquad
 \Pr(I_p=1\mid c,\tau(0),...,\tau(p-1))\le {2\over n_p}.             \tag{1.3}
\]

No conditioning on future goodness occurs in (1.3).

## 2. Prescribing the miss set

Fix a realizable color vector and a set `T` of `R` positions.  Iterated
conditioning in increasing position order gives

\[
 \Pr(I_p=1\text{ for every }p\notin T\mid c)
 \le\prod_{p\notin T}{2\over n_p}.                     \tag{2.1}
\]

If `sum I_p>=K-R`, its actual miss set has size at most `R`; enlarge it to
some `T` of size exactly `R`.  A union bound over `T` therefore gives

\[
 \Pr\left(\sum_pI_p\ge K-R\mid c\right)
 \le {2^{K-R}\over\prod_pn_p}
      e_R(n_0,...,n_{K-1}).                            \tag{2.2}
\]

Each nonempty color fiber contains exactly

\[
                         \prod_pn_p=(e+1)!e!            \tag{2.3}
\]

orders.  A realizable color vector is equivalent to choosing the `e+1`
values assigned to even positions, so there are exactly `binom(K,e+1)`
such vectors.  Multiplying (2.2) by (2.3), summing the fibers, and using
`G<=sum I_p` proves (0.1).

## 3. Closed upper bound and the live scale

The pool sizes have the exact sum

\[
 \sum_{p=0}^{K-1}n_p
 ={(e+1)(e+2)\over2}+{e(e+1)\over2}
 =(e+1)^2.                                             \tag{3.1}
\]

The multinomial expansion gives

\[
 e_R(n_0,...,n_{K-1})\le{(\sum_p n_p)^R\over R!}.      \tag{3.2}
\]

Together with `binom(K,e+1)<=2^K`, equations (0.1) and (3.1)--(3.2)
prove (0.3).

Now take

\[
 K=\Theta(b/\log b),\qquad R=O(b/\log^2b)=O(K/\log b).               \tag{3.3}
\]

Using `R!>=(R/\mathrm e)^R`, where `\mathrm e` is Euler's number, the
logarithm of (0.3) is at most

\[
 K\log4+R\log\left({\mathrm e(e+1)^2\over2R}\right)
 =O(b/\log b)=o(b).                                   \tag{3.4}
\]

Thus the equal-block route fails with a quantitative
`exp(O(b/log b))` candidate bound.  This conclusion remains confined to
equal blocks; unequal or multiscale block systems are not counted here.

The companion checker
`scratch/verify_gate_c_pivot_miss_set_tail_20260822.py` compares (0.1)
against the exact order census through `K=9` and verifies every algebraic
identity above.
