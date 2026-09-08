# Chamber II closes: the long-wrap shift and period equations are incompatible

**Date:** 2026-08-04

**Status:** unconditional pure-mathematical sign theorem.  It proves that
the bounded long-wrap KKT locus is empty, completes positivity of the
long-wrap train for every admissible period, and therefore closes all of
six-slot Chamber II through the frozen boundary reduction.  It does not
close Chamber I, the other six-slot efficiency branches, arbitrary-grid
Bellman positivity, or an OR-word upper bound.

Put

\[
 A={\sqrt\pi\over2},
 \qquad
 F_P(w)=\sum_{q\ge0}K(qP+w),
 \qquad
 C(P)=F_P(0),
\tag{0.1}
\]

and

\[
 Q_P(a)=C(P)+F_P(a)+F_P(2a).
\tag{0.2}
\]

The preceding outer-period theorem proves `Q_P>0` for

\[
 {A\over2}\le P\le{4A\over5},
 \qquad
 {11A\over12}\le P<A.
\tag{0.3}
\]

Every possible nonpositive value left by that theorem would therefore have

\[
 {4\over5}<\rho:={P\over A}<{11\over12},
 \qquad
 0<x:={a\over A}<{1-\rho\over2},
\tag{0.4}
\]

and, at a global minimum, would satisfy both the shift and period equations

\[
 T_\rho(x)+2T_\rho(2x)=0,
 \qquad
 \mathcal R(\rho,x)=0.
\tag{0.5}
\]

We prove that the first equation forces the left side of the second to be
strictly positive.

## 1. One normalized kernel contains every train

Put

\[
 h(z)=ze^{-\pi z^2/4}
\]

and define

\[
 \kappa(u)={K'(Au)\over2A}
 =\begin{cases}
 h(1+u)-h(1-u),&0\le u\le1,\\
 h(1+u),&u\ge1.
 \end{cases}
\tag{1.1}
\]

For `0<=s<=1-rho`, the exact shift derivative is

\[
 \boxed{
 T_\rho(s)=\sum_{q\ge0}\kappa(q\rho+s).}
\tag{1.2}
\]

Indeed the `q=0,1` terms give the two compact reflections, while every
`q>=2` term lies on the Gaussian tail.  The normalized period residual is

\[
 \boxed{
 \mathcal R(\rho,x)
 =\sum_{q\ge1}q\{
 \kappa(q\rho)+\kappa(q\rho+x)+\kappa(q\rho+2x)\}.}
\tag{1.3}
\]

All series and their differentiated series converge absolutely and
uniformly on the closed parameter rectangles used below.

## 2. The compact slope separation

### Lemma 2.1

For

\[
                         0\le t\le{1\over5},
\]

one has

\[
                         \boxed{\kappa'(t)<-{2\over5}.}
\tag{2.1}
\]

For

\[
                         {4\over5}<u<1,
\]

one has

\[
                         \boxed{\kappa'(u)<1.}
\tag{2.2}
\]

### Proof

On `[0,1]`,

\[
                         \kappa'(t)=h'(1+t)+h'(1-t).
\tag{2.3}
\]

The reflected-curvature theorem gives

\[
 h''(1+t)-h''(1-t)\ge0
 \qquad(0\le t\le1/2).
\tag{2.4}
\]

Thus `kappa'` is nondecreasing on this interval.  At `t=1/5`, the corrected
rational Gaussian certificate gives

\[
                         h'(6/5)<-{2\over5}.
\tag{2.5}
\]

Also

\[
 h'(4/5)<0,
\tag{2.6}
\]

because `8pi/25>1`.  Hence

\[
 \kappa'(1/5)=h'(6/5)+h'(4/5)<-{2\over5},
\]

and monotonicity proves (2.1).

For (2.2), write

\[
 \kappa'(u)=h'(1+u)+h'(1-u).
\]

The first term is negative because `1+u>9/5>sqrt(2/pi)`.  The second is
strictly smaller than one: for `z=1-u>0`,

\[
 h'(z)=e^{-\pi z^2/4}left(1-{\pi z^2\over2}\right)<1.
\]

This proves (2.2). \(\square\)

### Corollary 2.2 (compact exchange dominates the first carry)

On the domain (0.4),

\[
 \boxed{
 -\kappa(x)-2\kappa(2x)
 >\kappa(\rho+2x)-\kappa(\rho).}
\tag{2.7}
\]

### Proof

Here

\[
                         0<x<2x<1-\rho<{1\over5}.
\]

Since `kappa(0)=0`, (2.1) gives

\[
 -\kappa(x)>{2x\over5},
 \qquad
 -2\kappa(2x)>{8x\over5}.
\]

Their sum is strictly larger than `2x`.  On the other hand,

\[
 [\rho,\rho+2x]\subset(4/5,1),
\]

so (2.2) gives

\[
 \kappa(\rho+2x)-\kappa(\rho)
 =\int_\rho^{\rho+2x}\kappa'(u)\,du<2x.
\]

Combining the two inequalities proves (2.7). \(\square\)

## 3. Exact elimination of the period equation

Put

\[
                         G(\rho,x)=T_\rho(x)+2T_\rho(2x).
\tag{3.1}
\]

### Theorem 3.1 (period residual is positive on the shift-stationary set)

For every point satisfying (0.4),

\[
 \boxed{
 G(\rho,x)=0
 \quad\Longrightarrow\quad
 \mathcal R(\rho,x)>0.}
\tag{3.2}
\]

### Proof

Expand `G` using (1.2) and subtract it from (1.3).  On the set `G=0`,

\[
\begin{aligned}
 \mathcal R(\rho,x)
={}&-\kappa(x)-2\kappa(2x)
       +\kappa(\rho)-\kappa(\rho+2x)\\
 &+\sum_{q\ge2}q\kappa(q\rho)\\
 &+\sum_{q\ge2}(q-1)\kappa(q\rho+x)\\
 &+\sum_{q\ge3}(q-2)\kappa(q\rho+2x).
\end{aligned}
\tag{3.3}
\]

The coefficient ledger is exact:

* the unshifted period train contributes `q kappa(q rho)`;
* subtracting the first shifted train changes its coefficient to `q-1`
  and removes the `q=0` term `kappa(x)`;
* subtracting twice the second shifted train changes its coefficient to
  `q-2`, removes `2kappa(2x)`, and leaves the `q=1` term
  `-kappa(rho+2x)`.

Every term in the three displayed sums is nonnegative, and the first sum
is strictly positive, because each of their arguments exceeds one and

\[
                         \kappa(u)=h(1+u)>0\qquad(u>1).
\]

The first line of (3.3) is strictly positive by Corollary 2.2.  Therefore
`mathcal R(rho,x)>0`. \(\square\)

### Corollary 3.2 (empty KKT locus)

There is no point in (0.4) satisfying simultaneously

\[
 \begin{gathered}
 T_\rho(x)+2T_\rho(2x)=0,\\
 T_\rho'(x)+4T_\rho'(2x)\ge0,\\
 T_\rho(x)\le0\le T_\rho(2x),\\
 \mathcal R(\rho,x)=0.
 \end{gathered}
\tag{3.4}
\]

Indeed the first and last equations alone are incompatible.  The curvature
and one-sided derivative signs are therefore redundant for exclusion.

## 4. Complete long-wrap and Chamber-II closure

### Theorem 4.1

For every

\[
 {A\over2}<P<A,
 \qquad
 0<a<\min\left\{{P\over3},{A-P\over2}\right\},
\]

one has

\[
                         \boxed{Q_P(a)>0.}
\tag{4.1}
\]

Consequently the long-wrap family is positive on its complete closed
admissible domain, and all of six-slot Chamber II is positive.

### Proof

The outer-period theorem proves the claim outside the band (0.4), and all
boundary faces of the closed `(P,a)` domain are strictly positive by the
frozen Chamber-II reduction.

Suppose a nonpositive value existed.  By continuity, `Q` would attain a
nonpositive global minimum on the compact closure of the admissible domain.
Strict boundary positivity and the outer-period theorem place that minimum
in (0.4).  Its two free first derivatives give

\[
                         G(\rho,x)=0,
 \qquad \mathcal R(\rho,x)=0,
\]

contradicting Theorem 3.1.  Hence `Q_P(a)>0` everywhere.

The frozen stationary-strip elimination theorem states that positivity of
this long-wrap boundary implies positivity of the whole Chamber-II polygon.
This proves the final assertion. \(\square\)

## 5. Exact scope and dependencies

The theorem closes the long-wrap residual and Chamber II.  It makes no
claim about Chamber I's retained pulse, the remaining six-slot efficiency
branches, arbitrary-grid Bellman positivity, integral carrier
construction, or `nu(k)<=B(k)+O(1)`.

| role | file | SHA-256 |
|---|---|---|
| corrected outer-period closure and KKT core | `MATH_THEOREM_LONG_WRAP_OUTER_PERIOD_CLOSURE_AND_COMPACT_THETA_CORE_20260804.md` | `c60b69aadd89815605be134162ade2c2355008ae9f34ee39d45bb3c5cef139b3` |
| independent audit of that closure | `MATH_AUDIT_LONG_WRAP_OUTER_PERIOD_CLOSURE_AND_COMPACT_THETA_CORE_INDEPENDENT_20260804.md` | `4f230c0615122794d71e65523d4b55a8bbe9f2b6c63de66b9b6bed48c41bc4da` |
| stationary-strip elimination and long-wrap KKT reduction | `MATH_THEOREM_SIX_SLOT_CHAMBER_II_STATIONARY_STRIP_ELIMINATION_AND_LONG_WRAP_CURVE_20260804.md` | `f5dbde2a817c6ab23ade7de5c0f0d691d80db4d4bb23865f9643959efa79c91b` |
| independent audit of the KKT reduction | `MATH_AUDIT_SIX_SLOT_CHAMBER_II_STATIONARY_STRIP_AND_LONG_WRAP_CURVE_INDEPENDENT_20260804.md` | `3900b98672355272cf866659b4a5046f60b581604e18c91282e78e29d5f53d65` |
