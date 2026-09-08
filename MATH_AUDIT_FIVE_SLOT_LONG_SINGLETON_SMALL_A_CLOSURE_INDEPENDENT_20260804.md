# Independent audit: five-slot long-singleton closure for `a<=A/8`

**Date:** 2026-08-04  
**Audited source:**
`MATH_THEOREM_FIVE_SLOT_LONG_SINGLETON_SMALL_A_CLOSURE_20260804.md`  
**Verdict:** **PASS.**

## 1. Domain and endpoint descent

With

\[
 t=A-p-a,
\]

the long-singleton domain gives

\[
 0<t<a,
 \qquad 4a+t<A.
\]

The compact quadrilateral reduction applies with exactly this coordinate
and gives

\[
 \mathcal P(p,a)
 >C+F(a)+F(2a)-F(t)-F(a+t)-2\varepsilon.
\tag{1.1}
\]

No reversed no-interior-minimum comparison is used in (1.1).

## 2. Range check

If `0<a<=A/8`, then

\[
 0<t<a\le A/8,
 \qquad 0<a+t<2a\le A/4.
\]

Thus all four shifted arguments in (1.1) lie in `[0,A/4]`; in
particular they also lie in the larger interval `[0,A/2]` on which the
audited upper bound is valid.

The critical-point theorem says that every interior critical point of
`F` on `[0,A/4]` is a strict local maximum.  Hence the minimum on that
compact interval is an endpoint.  The two endpoint bounds

\[
 C>{43\over1000},
 \qquad F(A/4)>{44739\over1000000}>{43\over1000}
\]

therefore imply

\[
 F(w)>{43\over1000}\qquad(0\le w\le A/4).
\tag{2.1}
\]

The separate half-period estimate gives

\[
 F(w)<{64\over1000}\qquad(0\le w\le A/2).
\tag{2.2}
\]

## 3. Margin arithmetic

Substitution of (2.1)--(2.2) into (1.1), together with
`epsilon<1/20000`, gives

\[
\begin{aligned}
 \mathcal P(p,a)
 &>3{43\over1000}-2{64\over1000}-{2\over20000}\\
 &= {9\over10000}>0.
\end{aligned}
\]

The coefficient count is correct: the positive terms are `C,F(a),F(2a)`
and the adverse terms are `F(t),F(a+t)` plus two reflection errors.

## 4. Scope

The proof closes exactly `0<a<=A/8`.  It does not sign the compact
endpoint-descent bound on `A/8<a<A/4`, where that bound can be negative,
and makes no assertion about the full long-singleton gate or all five-slot
tables.
