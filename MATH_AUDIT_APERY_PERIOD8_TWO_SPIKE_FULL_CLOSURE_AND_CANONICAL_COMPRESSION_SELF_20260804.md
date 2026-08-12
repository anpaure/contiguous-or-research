# Self-audit: full period-eight two-spike closure and canonical compression

**Date:** 2026-08-04  
**Target:** MATH_THEOREM_APERY_PERIOD8_TWO_SPIKE_FULL_CLOSURE_AND_CANONICAL_COMPRESSION_20260804.md  
**Target SHA-256:** 76f1ced69d953d0ed0d6f1b4dd20566fcf5d6a657158c4b6de5b349e155e8e27  
**Verdict:** **PASS / GO in the stated two-spike and combinatorial-compression scope.**

This is a self-audit, not an independent-authorship audit. No enumeration,
solver, numerical search, Python, or H100 computation was used.

## 1. Residual scalar geometry

On the residual chamber

\[
 v>{9+\eta\over2},
\]

the denominator \(D=7+2v-\eta\) is greater than sixteen. Hence all three
early points \(2/D,3/D,4/D\) are below \(1/4\).

The first reflected point is above \(1/4\) because

\[
 4(v+1)>7+2v-\eta
 \quad\Longleftrightarrow\quad
 2v>3-\eta,
\]

which follows from \(v>3\). The final reflected point is below \(1/2\)
because

\[
 2(v+3)<7+2v-\eta
 \quad\Longleftrightarrow\quad
 \eta<1.
\]

Thus the three adverse compact points and their theta terms all lie in the
authenticated quarter-to-half interval.

## 2. Rational margin

The imported bounds are

\[
 C>{57\over1400},\qquad
 f(x)>{57\over1400}\quad(0\le x\le1/4),
\]

\[
 f(x)<f(1/4)<{293\over6000}\quad(1/4<x<1/2).
\]

The three reflected theta terms are positive, and the remaining singleton
theta term is greater than \(-1/20000\). Therefore

\[
 \mathcal E
 >4{57\over1400}
  -3{293\over6000}
  -{1\over20000}.
\]

On denominator 140000 the numerator is

\[
                         22800-20510-7=2283.
\]

This verifies both the sign and exact margin. Combined with the previously
proved \(D\le16\) chamber, the entire honest two-spike domain is closed.

## 3. Total-excess inequality

For an arbitrary period-eight depth-three word, write

\[
\begin{aligned}
 \gamma_2+\gamma_3+\gamma_4&=3a+\ell,\\
 \gamma_5&=a+\beta,\\
 \gamma_6+\gamma_7&=2a+r,\\
 \gamma_8&=a+\tau.
\end{aligned}
\]

The exact depth-three inequalities give

\[
 \tau>2a+\ell,\qquad
 \beta>\tau+r-\ell-a.
\]

Therefore the total excess \(\delta=\ell+\beta+r+\tau\) satisfies

\[
 \delta>2\tau+2r-a>3a.
\]

All inequality directions are strict, as required for the open
depth-three overlap.

## 4. Canonical representative

Because \(\delta>3a\), the interval

\[
 \max\{2a,\delta/2\}<z<(\delta+a)/2
\]

is nonempty. Setting

\[
 t'=a+z,\qquad b'=a+\delta-z
\]

gives

\[
 t'>3a,\qquad t'>b',\qquad b'>t'-a.
\]

The sum of the eight new gaps is

\[
 6a+b'+t'=8a+\delta=P.
\]

Hence the canonical word is honest and depth three by the exact two-spike
classification, while preserving \(a\), \(P\), and \(A=P+a\).

## 5. Scope

The construction does not compare the original and canonical Bellman
functionals. The theorem explicitly leaves that variational compression
gate open. It also makes no claim about larger periods, higher overlap
depth, overshoot, later crossing, or finite physical shoulders.

Within those exclusions, every claimed identity and inequality checks.
