# Terminal suffix maxima and the universal quarter cutoff

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical lemma for every honest cyclic
Apéry table.  It extracts the all-period mechanism used in the direct
period-eight and period-nine closures.  It does not by itself prove
positivity for arbitrary period.

## 0. Setup

Let

\[
 0=s_0<s_1<\cdots<s_{h-1}<P,
 \qquad h\ge2,                                         \tag{0.1}
\]

be an honest cyclic Apéry table, with cyclic gaps

\[
 \gamma_1=s_1,
 \quad
 \gamma_j=s_j-s_{j-1}\ (2\le j<h),
 \quad
 \gamma_h=P-s_{h-1}.                                  \tag{0.2}
\]

The prefix-minimum theorem says that for every length `t`, the initial
`t`-gap block has minimum sum among all cyclic blocks of that length.
For `h=2` this statement and the minimum-gap conclusion used below follow
directly from the sole nontrivial honesty inequality `P>=2s_1`; thus the
smallest allowed period does not rely on an `h>=3` dependency convention.

Assume additionally the exact-first-carry normalization

\[
                         P+s_1=A,                      \tag{0.3}
\]

put

\[
                         a=s_1,
 \qquad                  \alpha={a\over A},            \tag{0.4}
\]

and define the reflected late-ray endpoints

\[
 Y_i={A-s_{h-i}\over A}
     ={a+\gamma_{h-i+1}+\cdots+\gamma_h\over A},
 \qquad 1\le i<h.                                     \tag{0.5}
\]

## 1. Complementary block duality

### Theorem 1.1 (terminal suffix maximum)

For every `1<=i<h`, the terminal `i`-gap suffix

\[
                         R_i=\gamma_{h-i+1}+\cdots+\gamma_h        \tag{1.1}
\]

has maximum sum among all cyclic `i`-gap blocks.  Consequently

\[
                         \boxed{R_i\ge{iP\over h}.}     \tag{1.2}
\]

#### Proof

Every cyclic `i`-block is the complement, inside the full period, of one
cyclic `(h-i)`-block.  Complementation reverses their sums.  The initial
`(h-i)`-block is minimum by prefix-minimality, and its complement is exactly
the terminal suffix `R_i`.  Thus `R_i` is maximum.

The average of all `h` cyclic `i`-block sums is `iP/h`, because every gap
occurs in exactly `i` of those blocks.  A maximum is at least the average,
proving (1.2). \(\square\)

This is the max-side dual of the prefix-average inequality

\[
                         s_i\le{iP\over h}.             \tag{1.3}
\]

Both inequalities come from the same honest cyclic block order.

## 2. Exact reflected-ray lower envelope

### Corollary 2.1

Under exact first carry,

\[
 \boxed{
 Y_i\ge
 \alpha+{i\over h}(1-\alpha).}                        \tag{2.1}
\]

Moreover the reflected endpoints have the spacing floor

\[
 \boxed{Y_{i+1}-Y_i\ge\alpha\qquad(1\le i<h-1).}     \tag{2.2}
\]

#### Proof

Since `P/A=1-alpha`, equations (0.5) and (1.2) give

\[
 Y_i={a+R_i\over A}
 \ge\alpha+{iP\over hA}
 =\alpha+{i\over h}(1-\alpha).
\]

Also

\[
 Y_{i+1}-Y_i={\gamma_{h-i}\over A}\ge{a\over A}=\alpha
\]

by the minimum-gap theorem. \(\square\)

### Corollary 2.2 (quarter cutoff)

Every reflected endpoint with

\[
                         i\ge {h\over4}                 \tag{2.3}
\]

satisfies

\[
                         \boxed{Y_i>{1\over4}.}         \tag{2.4}
\]

Hence, for any integer `0<=u<h`, among `Y_1,...,Y_u` at most

\[
                         \boxed{\left\lceil{h\over4}\right\rceil-1} \tag{2.5}
\]

can lie at or below the quarter point.

#### Proof

If `i/h>=1/4`, (2.1) gives

\[
 Y_i\ge\alpha+{1-\alpha\over4}
       ={1\over4}+{3\alpha\over4}>{1\over4}.
\]

The positive integers strictly smaller than `h/4` number
`ceil(h/4)-1`, proving (2.5). \(\square\)

In particular, the bound is zero for `h=2,3,4`, one for `5<=h<=8`,
and two for `9<=h<=12`; no exceptional rounding convention is needed at a
multiple of four because the cutoff in (2.3) is inclusive and the conclusion
in (2.4) is strict.

More generally, for any `0<q<1`,

\[
 {i\over h}\ge{q-\alpha\over1-\alpha}
 \quad\Longrightarrow\quad
 Y_i\ge q.                                             \tag{2.6}
\]

This permits analytic cutoffs other than the quarter point whenever a
train monotonicity anchor is available.

## 3. Consequence for the reflected-ray ledger

Assume now the additional reflected-ray notation and hypotheses of the
cited exact-first-carry identity.  Thus `0<=u<h` and, for `1<=i<=u`,

\[
                         0<X_i\le Y_i<1/2.             \tag{3.0}
\]

In that exact reflected-ray identity

\[
 E(s)=C+\Theta+
       \sum_{i=1}^u\{f(X_i)-f(Y_i)\}
       +\text{nonnegative middle trains},              \tag{3.1}
\]

the compact train decreases on `[1/4,1/2]`.  Corollary 2.2, together with
(3.0), therefore separates the indexed pairs `1<=i<=u` into:

1. at most `ceil(h/4)-1` early reflected pairs which can lie wholly before
   the quarter point; and
2. all remaining pairs, for which either both endpoints lie in the
   decreasing interval or the pair crosses the quarter point.  Turning the
   latter alternative into a numerical lower bound additionally uses the
   sharp compact-train estimates from the cited finite-period theorems.

For `h=8`, only the first pair can be pre-quarter.  Under the additional
`H=3` hypotheses and pair/theta estimates of the cited period-eight theorem,
this location statement is the input yielding the complete margin
`859/210000`.  For `h=9`, only the first two can be pre-quarter; under the
corresponding cited hypotheses, the additional two-ninth monotonicity anchor
closes the second one.  For larger periods, (2.1) gives the exact grid of
analytic anchors which a finite-period proof must supplement with suitable
train estimates.

The number in (2.5) grows with `h`, so this lemma is a structural reduction,
not an all-period positivity proof.  A uniform theorem still requires a
quadrature/overlap argument for the growing early-ray bank.

## 4. Dependencies

| role | file |
|---|---|
| prefix-minimum theorem and reflected-ray identity | `MATH_THEOREM_APERY_MULTIDEFECT_PREFIX_MINIMUM_AND_REFLECTED_RAY_DEPTH_REDUCTION_20260804.md` |
| period-eight direct closure | `MATH_THEOREM_APERY_PERIOD8_ALL_H3_DIRECT_QUARTER_CLOSURE_20260804.md` |
| period-nine two-ninth closure | `MATH_THEOREM_APERY_PERIOD9_H3_TWO_NINTH_TRAIN_AND_COMPLETE_POSITIVITY_20260804.md` |
