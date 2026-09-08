# Every period-eight depth-three Apéry clock is positive

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical closure of the complete
exact-first-carry period-eight `H=3` formal branch.  It bypasses the false
same-marginal two-spike functional compression.  It does not address
periods above eight, threshold overshoot, later first crossing, or the
finite physical shoulder.

## 0. Result

Let

\[
 0=s_0<s_1<\cdots<s_7<P,
 \qquad P+s_1=A={\sqrt\pi\over2},                     \tag{0.1}
\]

be an honest cyclic Apéry table of period eight.  Write `a=s_1`, let its
cyclic gaps be \(\gamma_1=a,\gamma_2,\ldots,\gamma_8\), and suppose its
two reflected ray systems have overlap depth \(H=3\).  Then

\[
                         \boxed{\Phi(W)>{859\over210000}>0.}       \tag{0.2}
\]

Thus the first possible triple-overlap geometry is completely positive.

The proof uses no compression.  Prefix-minimality makes every terminal
gap suffix a maximum cyclic block.  This forces the second and third
reflected endpoints beyond the quarter point, where the compact train is
decreasing and has the sharp quarter upper bound.  Only the first pair can
remain wholly before the quarter point, and one ceiling train pays for
that single expensive pair and the other two cheap pairs.

## 1. Reflected-ray formula at period eight

For `H=3` at period eight, necessarily the number of shifts above the
midpoint is `u=3`.  Define

\[
 X_i={s_{i+1}\over A},
 \qquad
 Y_i={A-s_{8-i}\over A},
 \qquad 1\le i\le3.                                  \tag{1.1}
\]

The carry inequalities and the midpoint split give

\[
 0<X_1<X_2<X_3< {1\over2},
 \qquad
 0<Y_1<Y_2<Y_3<{1\over2},
 \qquad
 X_i\le Y_i.                                          \tag{1.2}
\]

Put

\[
 F(w)=\sum_{q\ge0}K(qA+w),
 \qquad f(x)=F(Ax),
 \qquad g(x)=\rho(Ax),
 \qquad C=F(0),
 \qquad \alpha={a\over A}.                           \tag{1.3}
\]

The exact reflected-ray identity is

\[
 \boxed{
 E(s)=C+g(\alpha)
      +\sum_{i=1}^3\{f(X_i)-f(Y_i)+g(Y_i)\},}
                                                               \tag{1.4}
\]

and the literal exact-first-carry comparison gives

\[
                         \Phi(W)\ge E(s).             \tag{1.5}
\]

## 2. Terminal suffixes are maximum cyclic blocks

### Lemma 2.1

For every `1<=i<=7`, the terminal `i`-gap block

\[
                         \gamma_{9-i}+\cdots+\gamma_8 \tag{2.1}
\]

has maximum sum among all cyclic `i`-gap blocks.

#### Proof

The prefix-minimum theorem says that the initial `(8-i)`-gap block has
minimum sum among all cyclic blocks of that length.  Complementation in
the cyclic period turns `(8-i)`-blocks into `i`-blocks and reverses the
order of their sums.  The complement of the initial block is precisely
the terminal block in (2.1). \(\square\)

The average cyclic `i`-block sum is `iP/8`.  Hence Lemma 2.1 gives

\[
 \gamma_7+\gamma_8\ge {P\over4},
 \qquad
 \gamma_6+\gamma_7+\gamma_8\ge {3P\over8}.           \tag{2.2}
\]

Since

\[
 Y_2={a+\gamma_7+\gamma_8\over A},
 \qquad
 Y_3={a+\gamma_6+\gamma_7+\gamma_8\over A},
 \qquad A=P+a,                                        \tag{2.3}
\]

we obtain the strict quarter locations

\[
 \boxed{
 Y_2>{1\over4},
 \qquad
 Y_3>{3\over8}>{1\over4}.}                           \tag{2.4}
\]

Indeed, for example

\[
 a+{P\over4}-{P+a\over4}={3a\over4}>0.
\]

The second strict comparison is

\[
 a+{3P\over8}-{3(P+a)\over8}={5a\over8}>0.
\]

## 3. Pairwise compact-train bounds

The authenticated train and theta bounds used below are

\[
 C>{57\over1400},
 \qquad
 f(x)>{57\over1400}\quad(0\le x\le1/4),             \tag{3.1}
\]

\[
 f(1/4)<{293\over6000},
 \qquad
 f\text{ decreases on }[1/4,1/2],                    \tag{3.2}
\]

\[
 f(x)<{61\over1000}\quad(0\le x\le1/2),             \tag{3.3}
\]

and

\[
 |g(x)|<{1\over20000}\quad(0\le x\le1/2),
 \qquad g(x)>0\quad(1/4\le x\le1/2).                \tag{3.4}
\]

### Lemma 3.1 (a pair ending after the quarter)

If

\[
                         0<X\le Y<1/2,
 \qquad                  Y\ge1/4,
\]

then

\[
 f(X)-f(Y)+g(Y)>-{341\over42000}.                     \tag{3.5}
\]

#### Proof

If `X>=1/4`, monotone decrease gives `f(X)>=f(Y)`, and `g(Y)>0`.
If `X<1/4`, equations (3.1)--(3.2) give

\[
 f(X)-f(Y)>{57\over1400}-{293\over6000}
            =-{341\over42000},
\]

while again `g(Y)>0`. \(\square\)

### Lemma 3.2 (the unrestricted first pair)

If

\[
                         0<X\le Y<1/2,
\]

then

\[
 f(X)-f(Y)+g(Y)>-{71\over3500}-{1\over20000}.         \tag{3.6}
\]

#### Proof

If `Y<1/4`, equations (3.1), (3.3), and (3.4) give

\[
 f(X)-f(Y)+g(Y)
 >{57\over1400}-{61\over1000}-{1\over20000}
 =-{71\over3500}-{1\over20000}.
\]

If `Y>=1/4`, Lemma 3.1 is strictly stronger than (3.6). \(\square\)

## 4. Complete closure

### Theorem 4.1

Every table in Section 0 obeys (0.2).

#### Proof

Apply Lemma 3.2 to the first pair in (1.4).  By (2.4), apply Lemma 3.1
to the second and third pairs.  The minimum-gap theorem gives
`P>=8a`, and therefore

\[
                         0<\alpha={a\over P+a}\le{1\over9}<{1\over2}.
\]

The theta bound is therefore applicable and gives

\[
                         g(\alpha)>-{1\over20000}.
\]

Then

\[
\begin{aligned}
 E(s)
 &>{57\over1400}
   -{71\over3500}
   -2{341\over42000}
   -{2\over20000}\\
 &={859\over210000}>0.
\end{aligned}                                         \tag{4.1}
\]

Equation (1.5) proves the same lower bound for \(\Phi(W)\). \(\square\)

## 5. Scope and consequence

The same-marginal two-spike functional compression is false, but it is no
longer needed at period eight.  The exact logical status is now:

* `H<=2` is closed by the general reflected-ray-depth theorem;
* `H=3` first becomes possible at period eight;
* every period-eight `H=3` formal clock is positive by Theorem 4.1.

The next multidefect analytic target therefore begins at period nine (or
at later first crossing/finite shoulder), not in a residual period-eight
face.

This theorem does not imply universal Bellman positivity or an OR-word
upper bound.

| role | file |
|---|---|
| prefix-minimum and reflected-ray identity | `MATH_THEOREM_APERY_MULTIDEFECT_PREFIX_MINIMUM_AND_REFLECTED_RAY_DEPTH_REDUCTION_20260804.md` |
| period-eight `H=3` classification | `MATH_THEOREM_APERY_FIRST_H3_EIGHT_PERIOD_TWO_SPIKE_SCALAR_20260804.md` |
| compact quarter bounds | `MATH_THEOREM_COMPLEMENTARY_PAIR_TRAIN_AND_H4_INERT_SCALAR_REDUCTION_20260804.md` |
| theta monotonicity and positivity | `MATH_LEMMA_THETA_HALF_INTERVAL_MONOTONICITY_AND_HALF_ROOT_SUMS_20260804.md` |
