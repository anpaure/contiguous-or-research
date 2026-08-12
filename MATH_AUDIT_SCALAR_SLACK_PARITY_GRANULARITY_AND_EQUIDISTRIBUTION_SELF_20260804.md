# Self-audit: scalar slack parity, granularity, and equidistribution

## Audited source

`MATH_THEOREM_SCALAR_SLACK_PARITY_GRANULARITY_AND_EQUIDISTRIBUTION_20260804.md`

This is a proof audit only.  It uses no finite search and makes no claim
about construction of a universal word.

## 1. Definition and parity formulas — PASS

For \(k=2m-1\),

\[
 W=C_m/2,
 \qquad
 \Lambda=2^{2m-2}-1,
\]

and

\[
 (C_m/2)\,4^m/(2C_m)=4^{m-1}.
\]

For \(k=2m\),

\[
 W=C_m,
 \qquad
 \Lambda=2^{2m-1}-C_m/2-1,
\]

and

\[
 C_m\bigl(4^m/(2C_m)-1/2\bigr)
 =2^{2m-1}-C_m/2.
\]

Thus the unified identity \(\Lambda=W(A_m-\eta)-1\) is exact.

## 2. Quotient-remainder dichotomy — PASS with stated asymptotic scope

Writing \(\Lambda=qW+\rho\), the value at \(q\) succeeds exactly when
\(\rho\le T_q\), and \(q+1\) always succeeds.  Excluding \(q-1\) uses
\(T_{q-1}<W\).  Since Stirling gives \(q=O(\sqrt m)\), this holds for all
sufficiently large \(m\).  The theorem does not claim the dichotomy for
uninspected small \(m\).

The step size

\[
 [tW+T_t]-[(t-1)W+T_{t-1}]=W+t
\]

verifies \(0\le\sigma<W+d\).

## 3. Dyadic congruence — PASS

Kummer gives \(v_2(C_m)=s_2(m)=a\).  With \(C_m=2^au\), \(u\) odd:

- odd parity has reduced phase denominator \(u\) and \(W/u=2^{a-1}\);
- even parity has reduced phase denominator \(2u\) and
  \(W/(2u)=2^{a-1}\).

Therefore \(Wy\equiv0\pmod {2^{a-1}}\),
\(\Lambda\equiv-1\), and

\[
 \sigma\equiv T_d+1\pmod {2^{a-1}}.
\]

The positive residue floor is correct.  It is only polynomial in scale and
is not represented as a positive fraction of \(W\).

## 4. Diophantine equations and uniqueness — PASS

Substitution and multiplication by two give

\[
 2^{2m-1}=dC_m+d(d+1)+2-2s
\]

and

\[
 2^{2m}=(2d+1)C_m+d(d+1)+2-2s.
\]

For fixed \((d,s)\) with positive correction, division by \(C_m\) compares
the strictly increasing sequence \(R_m=4^m/C_m\) with a strictly decreasing
sequence.  The recurrence

\[
 R_{m+1}/R_m=2(m+1)/(2m+1)>1
\]

is exact.  The bounded nonpositive-correction depths are finite because
\(d(m)\to\infty\).  Hence the \(O_S(\sqrt K)\) count follows from
\(d=\Theta(\sqrt m)\).

The displayed \(k=6\) and \(k=9\) cases are direct substitutions only; the
source explicitly does not call them an exhaustive list.

## 5. Uniform limiting distribution — PASS

The central-binomial expansion gives

\[
 A_m=(\sqrt{\pi m}/2)(1+1/(8m)+O(m^{-2})).
\]

Van der Corput on dyadic intervals gives an \(O(N^{3/4})\) bound for every
fixed nonzero Weyl frequency of \(\alpha\sqrt m\), enough for uniform
distribution.  The \(O(m^{-1/2})\) perturbation is harmless.

Outside \(\theta\le T_q/W\),

\[
 \sigma/W=1-\theta+O(m/W).
\]

The exceptional set has density zero by fixed-interval uniform
distribution.  This proves the empirical uniform law.  The source now
explicitly notes that isolated values can exceed one by \(O(m/W)\), so it
does not incorrectly assert literal containment in \([0,1]\).

The density-one bound follows because failure puts \(\theta\) in shrinking
endpoint neighbourhoods.  Fixed-interval uniform distribution suffices:
for every fixed \(\varepsilon\), the eventual bad set lies in two intervals
of total length \(2\varepsilon\), then \(\varepsilon\downarrow0\).

## 6. Square-root-scale subsequence — PASS

Squaring the Stirling expansion gives

\[
 A_m^2=\frac\pi4\left(m+\frac14+\frac1{32m}+O(m^{-2})\right).
\]

For target lattice \(n+\eta\), the polynomial

\[
 4(n+\eta)^2/\pi-1/4
\]

has irrational quadratic coefficient and is uniformly distributed modulo
one.  Selecting its fractional part in
\([\varepsilon_j,2\varepsilon_j]\), then taking the floor, places \(A_m\)
below the target lattice by
\(O(\varepsilon_j/\sqrt m)\).  The triangular correction is exponentially
smaller.  This proves

\[
 \liminf\sqrt m\,\sigma/W=0
\]

on both parities.

No quantitative irrationality measure is invoked.  The source correctly
does not infer failure of every \(W/k^a\) lower bound for \(a>1/2\).

## 7. Rounding interpretation — PASS

Under the separately proved zero-leakage identity \(M=D-\sigma\), one has
\(D\ge\sigma\).  Therefore:

- total \(D\) cannot be globally \(o(W/k^c)\), since \(\sigma=\Theta(W)\)
  on a positive-density set;
- an excess bound \(D-\sigma\le E(k)\) gives only \(M\le E(k)\);
- a subpolynomial but unbounded \(E(k)\) is not an additive constant;
- density-one slack lower bounds do not prove an all-dimensional theorem.

These implications are logically scoped to the zero-leakage face and do
not claim a word construction.

## Final audit verdict

**PASS, with explicit limitations.**

The theorem proves exact parity arithmetic, congruential granularity,
near-zero sparsity at fixed absolute threshold, paritywise limiting
distribution, and the square-root-scale liminf.  It does not prove a
positive all-dimensional polynomial lower bound, finiteness of zero slack,
or \(B(k)+O(1)\).
