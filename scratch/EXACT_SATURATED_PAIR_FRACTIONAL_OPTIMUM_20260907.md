# Exact fractional optimum for saturated complementary rectangles

Date: 2026-09-07. This is a fractional-cover theorem in a specified
rectangle model. It is not a construction of an integral OR word.

Let the ground set have size `2b`, where `b>=2`, and put
`W=binom(2b,b)`. A column is the ordinary target family

\[
 E_R=(C\times D)\cup(C\times D)^c,
\]

where `C,D` are nonempty saturated set chains on complementary coordinate
supports, of lengths `a,c`. The supports may vary between columns, and
chain centers need not be symmetric. The cost of a column is `a+c`.
One target in both orientations is counted only once in `E_R`.

A fractional cover assigns nonnegative weights to columns such that every
nonempty target has total incident weight at least one. Its cost is the
weighted sum of column costs. Then

\[
 \boxed{\operatorname{OPT}_{\rm frac}(2b)
       =\left(1+\frac1{b(b+1)}\right)W.}             \tag{1}
\]

The same optimum holds if the empty target is also required. The upper
construction uses only two coordinate orbits of columns.

## 1. A feasible three-rank dual

Give each rank-`b` target weight `1/b`, each rank-`b-1` or rank-`b+1`
target weight `1/2`, and all other targets weight zero. The total weight is

\[
 \frac Wb+\binom{2b}{b-1}
 =\left(1+\frac1{b(b+1)}\right)W.                    \tag{2}
\]

We prove that a column has dual weight at most its cost.

Let `H_j` count rank-`b+j` targets in the single orientation `C times D`.
Put `u=(a+c)/2`, `v=|a-c|/2`, and let `z` be its rank center relative to
`b`. The interpolated rank profile is

\[
 H(x)=(u-|x-z|)_+-(v-|x-z|)_+,
 \qquad H_j=H(j).
\]

The outer support endpoints `z-u,z+u` are integers. The profile is
concave between these endpoints and is 1-Lipschitz. Consequently:

* if `H_0>0`, then `H_1+H_(-1)<=2H_0`;
* if `H_0=0`, then `H_1+H_(-1)<=1`.

For the first statement, integer `H_0>=1` puts zero at least one unit
inside the outer support. For the second, at most one adjacent point can
be in the positive support, and its height is at most one.

Ignoring duplicate targets between the two orientations gives the upper
bound

\[
          \text{column dual weight}
          \le \frac{2H_0}{b}+H_1+H_{-1}.             \tag{3}
\]

The support sizes sum to `2b`, so `a+c<=2b+2`. First suppose
`a+c<=2b+1`. If `H_0=0`, (3) is at most one, less than `a+c`.
Otherwise distinguish the following cases.

If `u` is an integer, then `u<=b`. If `H_0=u`, the profile necessarily
has `v=z=0`, and `H_1+H_(-1)=2u-2`; (3) is at most `2u`, with equality
only when `u=b`. If `H_0<=u-1`, then (3) is at most
`2(u-1)(1+1/b)<2u`.

If `u` is a half-integer, then `u<=b+1/2` and `H_0<=u-1/2`.
Equality in the latter forces `v=|z|=1/2`, giving
`H_1+H_(-1)=2H_0-1`. Hence (3) is at most `2u`, with equality only
when `u=b+1/2`. Otherwise `H_0<=u-3/2`, and (3) is strictly less than
`2u`.

It remains to handle `a+c=2b+2`. Both shore chains must then be full
maximal chains. Their rank center is `b`. If the shore sizes are unequal,
`v>=1` and `H_0<=b`, so the occurrence version of (3) is at most
`2b+2`. It can equal that bound only when the shore sizes are `b-1,b+1`;
in that case their full-shore targets are duplicated at the two adjacent
ranks, making the ordinary weight strictly smaller.

For two balanced maximal shore chains, the rectangle and its complement
overlap exactly at the empty set, the two full shores, and the whole
ground set. There are therefore `2b` distinct middle targets and `2b`
targets at each adjacent rank. Their dual weight is `2+2b`, exactly the
cost. This verifies (3) with ordinary incidence in the final case too.

Summing this column inequality with fractional weights proves the lower
bound (2). It applies equally to integral covers.

## 2. An explicit two-orbit cover attaining the dual

Type A is a centered square with both chain lengths `b`. One realization
uses support sizes `b-1,b+1`: take a full maximal chain on the first
support and ranks `1,...,b` of a maximal chain on the second. Its two
orientations are disjoint. At offset `d=|s-b|`, its rank-`s` incidence is

\[
                       n_A(d)=2(b-d)_+,
 \qquad \operatorname{cost}(A)=2b.                  \tag{4}
\]

Type B uses two supports of size `b`. Take a full maximal chain on the
first and ranks `0,...,b-1` of a maximal chain on the second. These
lengths are `b+1,b`; the rectangle and its complement are disjoint. Its
incidence is

\[
 n_B(0)=2b,\qquad n_B(d)=2(b-d)+1\quad(1\le d\le b),
 \qquad \operatorname{cost}(B)=2b+1.                 \tag{5}
\]

Average each type over all coordinate permutations (equivalently, use the
uniform measure on its orbit), and give its entire orbit total weight

\[
 t_A=\frac{W\,(b-1)}{2b(b+1)},\qquad
 t_B=\frac{W}{b(b+1)}.                               \tag{6}
\]

Since coordinate permutations act transitively on every rank, verifying
total incidence at least the rank size verifies each individual target.
The middle incidence is exactly `W`. At offset `1<=d<=b` it is

\[
       W\left(1-\frac db+\frac1{b(b+1)}\right).      \tag{7}
\]

At `d=1`, (7) equals `binom(2b,b+1)`. To check other proper ranks, put

\[
 Q_d=\frac{\binom{2b}{b+d}/W}{1-d/b},\quad 0\le d<b.
\]

Here `Q_0=1`, `Q_1=b^2/(b^2-1)`, and for `1<=d<=b-2`,

\[
 \frac{Q_{d+1}}{Q_d}
 =\frac{(b-d)^2}{b^2-(d+1)^2}<1.
\]

Indeed numerator minus denominator is `1-2d(b-d-1)<0`. Thus, for
`1<=d<b`, the rank size divided by `W` is at most
`(1-d/b)b^2/(b^2-1)`, which is no greater than (7) divided by `W`:
the difference is `(d-1)/(b(b^2-1))`. At `d=b`, (7) is at least one
because `W>=binom(2b,2)=b(2b-1)>=b(b+1)`.

This proves coverage of every target, including both extremes. Its cost is

\[
       2b t_A+(2b+1)t_B=W+\frac{W}{b(b+1)},
\]

which matches (2) and proves (1).

## 3. What exact integral equality would require

The dual proof is tight only for the following shapes:

1. centered sides `b,b`;
2. sides `b+1,b`, with rank center `b+1/2` or `b-1/2`;
3. balanced full maximal sides `b+1,b+1`.

Every such ordinary column contains exactly `2b` distinct middle targets.
If an integral cover attains the fractional optimum exactly, all selected
columns must be tight, and every middle and adjacent target must be
covered exactly once. In particular its number of columns must be
`W/(2b)`, an integer. Writing their type counts as `t_A,t_B,t_C`, the
adjacent-rank equality additionally gives

\[
                   2t_A+t_B=\frac{W}{b+1}.
\]

These are necessary conditions, not a construction or sufficiency theorem.
The full-cube OR coefficient-one objective remains unproved. In particular,
fractional weights cannot be concatenated into one word, and the principal
rectangle charge is not a lower bound on unrestricted OR-word length.

Exact finite checks of all allowed chain rank intervals for `b=2,...,10`
and the two-orbit primal are in
`scripts/check_saturated_pair_dual_20260907.py`. The proof above does not
use the checks as a premise.
