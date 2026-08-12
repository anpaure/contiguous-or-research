# Audit of the capacitated peak-deletion induction

Date: 2026-07-25

Method: pure mathematics only.

## Verdict

The main formulas in Theorem 5.1, Corollary 5.2, and the conditional
constant (7.2) are correct. The required corrections are definitional,
one moderate-deviation proof insertion, and two scope qualifications.

## 1. Theorem 5.1

For the inverse step

\[
 D_{j+1}\longmapsto D_j,
\]

the core rank, core peak count, and free-leaf count are respectively

\[
 r_{j+1},\qquad r_{j+1}-r_{j+2},\qquad
 y_j=r_j-2r_{j+1}+r_{j+2}.
\]

Therefore the factors

\[
 \binom{r_j+r_{j+2}}{2r_{j+1}},
 \qquad
 \binom{r_j+r_{j+2}-z_j-1}{2r_{j+1}-1}
\]

and the product range \(0\le j\le L-1\) are correct. Add the exact
admissibility convention

\[
 0\le z_j\le y_j;
\]

the prescribed-slot factor is zero otherwise.

Fixing \(D_L\) correctly fixes
\[
 r_{L+1}=r_L-\operatorname{pk}(D_L).
\]
There is no index shift in (5.3)--(5.6).

## 2. Corollary 5.2

The harmonic profile is realizable. Divisibility by
\(\operatorname{lcm}(1,\ldots,L+2)\) makes all \(r_j\) integral. It also
makes

\[
 r_L-r_{L+1}=\frac{R}{(L+1)(L+2)}
\]

integral because \(L+1\) and \(L+2\) are coprime. Moreover,

\[
 y_j=\frac{2R}{(j+1)(j+2)(j+3)}>0.
\]

The displayed bottom Dyck word has the prescribed rank and number of peaks,
and successive inverse fibres are nonempty. The telescoping product is
indeed

\[
 \prod_{j=0}^{L-1}\frac{(j+1)(j+3)}{(j+2)^2}
 =\frac{L+2}{2(L+1)}.
\]

Scope correction: this is a conditional fibre fraction inside one exact
rank profile and one fixed bottom root. No lower bound is proved for that
profile's proportion of the global Catalan/Pascal mass. Thus Corollary 5.2
rules out pointwise multiplication of seam losses; it is not by itself an
aggregate obstruction at the \(B_r/r\) scale.

## 3. Saddle tail (4.9)

The conclusion is valid, but it cannot be deduced solely from (4.5), whose
stated uniformity covers bounded \(u,v\), while (4.9) reaches
\(\Theta(\sqrt{\log r})\).

Insert a uniform moderate-deviation Stirling estimate for

\[
 |u|+|v|=O(\sqrt{\log r}).
\]

The least eigenvalue of the negative Hessian is

\[
 \lambda_{\min}
 =\frac{57-3\sqrt{73}}4.
\]

Within a fixed interior neighbourhood, one may use

\[
 \frac{\mathsf M_r(d,k)}{B_r}
 \le
 \frac Cr
 \exp\!\left[-\frac{\lambda_{\min}}4(u^2+v^2)\right].
\]

Together with the fixed entropy gap outside that neighbourhood, this proves
(4.9). A conservative explicit choice is any

\[
 C_0>\frac4{\sqrt{\lambda_{\min}}},
\]

so \(C_0=2\) suffices.

## 4. Conditional constant (7.2)

The constant is correct. The saddle-curve mass is

\[
 \frac{9\sqrt2}{2\pi\sqrt r}
 \left(\int_{-a}^{a}e^{-33v^2/8}\,dv\right)B_r.
\]

A slot bounded by \(z_0\) retains

\[
 \frac34\,4^{-z_0}+o(1),
\]

and variable-length interval greedy packing divides by

\[
 2H_A+1=2A\sqrt r+o(\sqrt r).
\]

Their product is exactly the coefficient in (7.2). Replace the phrase
“equal-length subdivision” by “variable-length conflict greedy”; no
subdivision is needed.

## 5. Two-child capacity

The two children are correctly indexed:

\[
 [0,h],\qquad [t_-,g].
\]

Same-label parity makes their step-two residence traces subtraces of the
parent projected trace. A parent edge occurrence can appear in both, so
the universal child load is at most \(2F\). For the gap-seven passage, the
two child traces are

\[
 \{-1,1,3,5\},\qquad \{1,3,5,7\},
\]

and multiplicity two is attained on their three-edge overlap.

Add the qualification that another deletion step is applied to a child
only while that child's gap is smaller than its current circumference.
The result rules out contraction for the raw two-child charge; it does not
rule out a further decorrelation statistic.

## 6. Minor exact-definition corrections

In (1.8), the phrase “\((E,g)\) satisfies (1.5)” is ill-typed because
(1.5) contains \(z_*(D)\). Define a reduced passage by

\[
 \kappa_g(E)=-1,\qquad
 \kappa_h(E)=0\text{ for some }0<h<g,\qquad
 n_{-1}(g)\text{ odd},
\]

and only then set

\[
 z_E(g)=\frac{n_{-1}(g)-1}{2}.
\]

When asserting

\[
 \sum_eF_r(e)=B_r,
\]

include the \(d=0\) fully-pruned star boundary explicitly.
