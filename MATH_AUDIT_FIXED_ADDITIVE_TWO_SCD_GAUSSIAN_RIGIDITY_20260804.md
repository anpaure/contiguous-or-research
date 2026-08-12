# Audit of fixed-additive two-SCD Gaussian rigidity

**Date:** 2026-08-04  
**Verdict:** PASS after one exact correction and two proof-scope
clarifications were incorporated into the theorem.

Audited theorem:

MATH_THEOREM_FIXED_ADDITIVE_TWO_SCD_GAUSSIAN_RIGIDITY_20260804.md

Frozen SHA-256:

53491d7ed7703bd09bbdb1d5dc676f980d2583d37dd5cd12d6227d71353393e4.

## 1. Exact correction

The original residual length \(t_C-b\) at every SCD start counted the empty
set on the unique chain beginning at rank zero. The strict-lower bank is
nonempty, so the exact length is

\[
 L_b=t_C-b-\mathbf 1_{\{b=0\}}.
\]

The original convention changed no weak limit, minimum-piece density, or
\(\Omega(W)\) conclusion, because it affected one target. It did make the
claimed exact vacancy equation off by one. The frozen theorem now removes
the empty set explicitly.

Indeed,

\[
 \sum_F|F|=\sum_{s=1}^{t_C-1}{2r\choose s},
\]

whereas summation by parts gives

\[
 \sum_{u=1}^{h}u(H_{t_C+u}+1)
 =hW-\sum_{s=t_C}^{r-1}{2r\choose s}+{h+1\choose2}.
\]

Their difference is exactly

\[
 hW+{h+1\choose2}-\Lambda=\sigma_C.
\]

## 2. Gaussian limits

Since \(h=d+C\) and \(C\) is fixed,

\[
 {h\over\sqrt r}\to A={\sqrt\pi\over2}.
\]

Telescoping the start counts gives the residual tail

\[
 {\nu_{r,C}}([x,\infty))\to e^{-(A+x)^2}.
\]

The socket tail is

\[
 {\mu_{r,C}}([y,A])\to1-e^{-(A-y)^2}.
\]

Differentiation gives the stated densities

\[
 2(A+x)e^{-(A+x)^2}\,dx
\quad\hbox{and}\quad
 2(A-y)e^{-(A-y)^2}\,dy.
\]

The boundary contributes \(h/W=o(1)\) mass. The fixed shift \(C\) and the
single rank-zero correction disappear after \(\sqrt r\)-scaling.

## 3. Scalar shift

Expanding \(h=d+C\) gives

\[
 \sigma_C
 =\sigma_0+CW+Cd+{C(C+1)\over2}.
\]

Minimality of \(d\) gives \(0\le\sigma_0<W+d\). Hence
\(\sigma_C=O(W)\) for fixed \(C\), while the leading job/socket first
moment has scale \(W\sqrt r\). Therefore

\[
 {\sigma_C\over W\sqrt r}\to0.
\]

## 4. Rigidity argument

The phrase “threshold cuts with additive error \(o(W)\)” has been replaced
by the uniform statement

\[
 \#\{F:|F|\ge q\}
 \le\#\{\text{sockets of capacity at least }q\}+\epsilon_rW
\]

for all \(1\le q\le h\), with one \(\epsilon_r\to0\).

Every subsequential chunk limit is supported in \([0,A]\), is bounded in
total mass by the \(q=1\) cut, and obeys every positive tail domination.
Exact scalar vacancy and bounded support give equality of first moments.
The integral of the nonnegative tail difference is therefore zero.
Equality first holds away from atoms and then at every positive threshold
by one-sided approximation. The \(q=1\) inequality forbids extra mass at
zero. Thus the limiting chunk measure is exactly \(\mu\).

The original reference to right continuity was imprecise for closed tails;
the frozen proof now uses continuity at non-atoms and one-sided
approximation.

## 5. Consequences

The minimum-piece density is

\[
 p_{\min}=\sum_{m\ge1}e^{-\pi m^2/4}<0.501,
\]

whereas the forced socket/chunk mass is

\[
 1-e^{-\pi/4}>0.544.
\]

The gap is a positive constant, so every minimum-piece cutting misses some
threshold by \(\Omega(W)\), uniformly for each fixed \(C\).

For a literal matching, matched slack plus unused socket capacity equals
\(\sigma_C=O(W)\). Therefore only \(o(W)\) matched or unused sockets can
have macroscopic slack at least \(\epsilon\sqrt r\). Together with the
rigidity theorem, this gives the stated capacity-diagonal macroscopic
limit.

## 6. Scope

The theorem is a necessary asymptotic rigidity result for the two-SCD
route. It does not:

* construct a chain-dependent cutting with the required limiting measure;
* prove the finite configuration-price inequalities;
* prove literal containment Hall;
* serialize the chunks into one source word; or
* co-instantiate residence, upper witnesses, seam, and common cap.

The conclusion applies for every fixed additive \(C\). It does not address
\(C=C(r)\) growing with dimension. No finite computation or solver result
is used.
