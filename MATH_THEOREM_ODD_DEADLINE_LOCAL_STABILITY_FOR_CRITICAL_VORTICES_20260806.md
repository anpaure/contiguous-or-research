# Odd deadlines are locally stable across a critical balanced vortex

## Status

For the odd ground set of size `2r-1`, let `d_r` be the exact triangular
deadline in the lower bound.  This note proves that reducing the semirank
from `r` to `r-a` changes the deadline by at most one whenever
`a=o(sqrt r)` with an explicit inequality.  In particular this holds for
the critical balanced-vortex choice

\[
                         a=\left\lfloor{\log_2 r\over4}\right\rfloor.
\]

Thus a critical vortex needs the intrinsic smaller-depth construction, or
at worst one additional derivative layer, to match the ambient depth.  The
theorem does not construct that one-layer extension or its splice ports.

## 1. Exact odd-layer recurrence

Put

\[
 W_r=\binom{2r-1}r={1\over2}\binom{2r}r,
 \qquad
 \Lambda_r=\sum_{s=1}^{r-1}\binom{2r-1}s=4^{r-1}-1.       \tag{1.1}
\]

Define

\[
 d_r=\min\left\{t\ge0:
       tW_r+\binom{t+1}2\ge\Lambda_r\right\},
 \qquad x_r={\Lambda_r\over W_r}.                         \tag{1.2}
\]

The exact recurrences are

\[
 {W_r\over W_{r-1}}=4-{2\over r},
 \qquad
 \Lambda_r=4\Lambda_{r-1}+3,                             \tag{1.3}
\]

and hence

\[
 \boxed{
 x_r-x_{r-1}={x_{r-1}\over2r-1}+{3\over W_r}.}           \tag{1.4}
\]

### Lemma 1.1 (monotonicity of the exact deadline)

For every `r>=2`,

\[
                              d_r\ge d_{r-1}.              \tag{1.5}
\]

#### Proof

Let `t<d_(r-1)`.  Then

\[
 tW_{r-1}+\binom{t+1}2<\Lambda_{r-1}.                    \tag{1.6}
\]

Multiplication by four, followed by (1.3), gives

\[
 4tW_{r-1}+4\binom{t+1}2<\Lambda_r-3.                   \tag{1.7}
\]

Since `W_r<4W_(r-1)` and
`binom(t+1,2)<=4binom(t+1,2)`, the left side of the deadline
test at semirank `r` is strictly smaller than the left side of (1.7),
unless `t=0`; the case `t=0` is immediate.  Thus `t` is still infeasible
at semirank `r`.  Every integer below `d_(r-1)` is infeasible, proving
(1.5).  \(\square\)

## 2. Quantitative variation of the scalar deadline

For `s>=2`, the elementary central-binomial estimate

\[
                         \binom{2s}s\ge {4^s\over2\sqrt s}              \tag{2.1}
\]

implies

\[
                              0<x_s<\sqrt s.              \tag{2.2}
\]

Consequently (1.4) gives, for `1<=a<r-1`,

\[
 0<x_r-x_{r-a}
   <{a\over2\sqrt{r-a-1}}+{3a\over W_{r-a+1}}.           \tag{2.3}
\]

Indeed, each of the `a` first terms in (1.4) is at most
`1/(2sqrt(r-a-1))`, and the central binomial coefficients increase with
the semirank.

## 3. One-step stability

### Theorem 3.1 (local deadline stability)

Assume `r-a>=4` and

\[
 {a\over2\sqrt{r-a-1}}+{3a\over W_{r-a+1}}\le {1\over2}. \tag{3.1}
\]

Then

\[
                         \boxed{d_r-d_{r-a}\in\{0,1\}.}   \tag{3.2}
\]

#### Proof

Monotonicity gives `d_r>=d_(r-a)`.  Put `m=d_(r-a)`.  By feasibility of
`m`,

\[
 x_{r-a}\le m+{\binom{m+1}2\over W_{r-a}}.               \tag{3.3}
\]

For `r-a>=4`, one has `m<=r-a-1` and therefore

\[
 {\binom{m+1}2\over W_{r-a}}<{1\over2}.                  \tag{3.4}
\]

Indeed `m<=r-a-1` follows by bounding each of the `r-a-1`
strict-lower binomial coefficients by `W_(r-a)`.  The remaining strict
inequality follows from
`W_s=binom(2s-1,s)>s(s-1)` for `s>=4` (check `s=4`, then use
`W_(s+1)/W_s=4-2/(s+1)`).

If `d_r>=m+2`, then `m+1` is infeasible at semirank `r`, whence

\[
 x_r>m+1+{\binom{m+2}2\over W_r}>m+1.                    \tag{3.5}
\]

Equations (3.3)--(3.5) give

\[
 x_r-x_{r-a}>1-{\binom{m+1}2\over W_{r-a}}>{1\over2},    \tag{3.6}
\]

contradicting (2.3) and (3.1).  Hence `d_r<=m+1`, which together with
monotonicity proves (3.2).  \(\square\)

### Corollary 3.2 (critical balanced vortex)

For

\[
                         a=\left\lfloor{\log_2 r\over4}\right\rfloor,
                                                                    \tag{3.7}
\]

condition (3.1) holds for all sufficiently large `r`.  Thus the ambient
owner width

\[
                         D_r=d_r+1                         \tag{3.8}
\]

and the intrinsic vortex width `D_(r-a)=d_(r-a)+1` are equal or differ by
exactly one.

#### Proof

Here `a=O(log r)=o(sqrt r)`.  The first term in (3.1) tends to zero and the
second is exponentially small.  Apply Theorem 3.1.  \(\square\)

## 4. Exact functorial lift at a fixed ambient owner width

Let `A,B,R,q` be the balanced-slice data, and fix any owner-window width
`D<=q`.  Thus the derivative depth is `D-1`.  For a source chronology
`C=(C_t)` on `R`, define

\[
                              \widehat C_t=A\cup C_t.       \tag{4.1}
\]

### Proposition 4.1 (interval-deck and state lift)

For every source interval `I`,

\[
                  \bigcup_{t\in I}\widehat C_t
                     =A\cup\bigcup_{t\in I}C_t.           \tag{4.2}
\]

Consequently:

1. rank-`q` length-`D` source-window owners on `R` lift to rank-`r`
   ambient owners in
   `mathcal O_(A,B)`;
2. every marked lower or upper interval target lifts by adjoining `A`;
3. the order-`D-1` de Bruijn entrance and exit states (the `D-1`
   overlapping source letters) lift componentwise by adjoining `A` to
   every source letter;
4. every coordinate of `A` has one full positive run through the lifted
   block, every coordinate of `B` has one full gap, and the run/gap data on
   `R` are unchanged.

#### Proof

Equation (4.2) is distributivity of union and the fact that `A` is present
in every lifted source letter.  Each listed assertion follows directly.
\(\square\)

Thus there is no *algebraic* ambient-depth penalty: a decorated chronology
constructed on the vortex directly at depth `D_r` lifts literally and has
the correct state interface.  The open row is existence of that
deadline-flexible decorated chronology.  Corollary 3.2 shows it asks for
only the intrinsic depth or one extra derivative layer, rather than a
growing depth discrepancy.
