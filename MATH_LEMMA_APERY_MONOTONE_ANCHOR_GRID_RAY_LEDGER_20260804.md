# Monotone anchor grids for all-period reflected-ray ledgers

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It packages the
period-eight through period-twenty-one proofs into one exact finite-grid
inequality and isolates the one-dimensional analytic input needed to push
arbitrary periods.  It does not by itself prove all-period positivity.

## 0. Setup

Let an honest exact-first-carry period-`h` table have reflected pairs

\[
                         0<X_i\le Y_i<1/2,
 \qquad                  1\le i\le u,
\]

and endpoint lower comparison

\[
\begin{aligned}
 E(s)={}&C+g(\alpha)
 +\sum_{i=1}^u\bigl(f(X_i)-f(Y_i)+g(Y_i)\bigr)\\
 &+\sum_{r=u+2}^{h-u-1}f(s_r/A),
 \qquad \Phi(W)\ge E(s).                              \tag{0.1}
\end{aligned}
\]

Terminal-suffix maximality gives

\[
                         Y_i>{i\over h}.               \tag{0.2}
\]

Assume the certified analytic rows

\[
 C>L,\qquad f(x)>L\quad(0\le x\le1/4),               \tag{0.3}
\]

\[
 |g(x)|<\varepsilon,qquad g(x)>0\quad(1/4\le x\le1/2).
                                                                  \tag{0.4}
\]

Assume also the certified quarter-interval monotonicity

\[
                         f'(x)<0\qquad(1/4\le x\le1/2).          \tag{0.4a}
\]

Let

\[
 0\le t_0<t_1<\cdots<t_s<1/2                         \tag{0.5}
\]

be analytic anchors such that `f` is decreasing on every
`[t_j,1/2]` and

\[
                         f(t_j)<V_j.                   \tag{0.6}
\]

One may also include a global anchor `t_* =0` with any certified bound
`f<V_*` on the whole half interval; no monotonicity is needed for that
special row.

## 1. One anchored reflected pair

### Lemma 1.1

Suppose `Y>t_j`.  Then

\[
 f(X)-f(Y)+g(Y)>
 \begin{cases}
 \min\{0,L-V_j-\varepsilon\},&t_j<1/4,\\
 \min\{0,L-V_j\},&t_j\ge1/4,
 \end{cases}                                          \tag{1.1}
\]

for every `0<X<=Y<1/2`.

For the global anchor, the valid price is

\[
                         \min\{0,L-V_*-\varepsilon\}. \tag{1.2}
\]

#### Proof

First assume `t_j<1/4`.  If `X<t_j`, then `X<1/4`, so (0.3), (0.4),
(0.6), and monotonicity give

\[
 f(X)-f(Y)+g(Y)>L-V_j-\varepsilon.
\]

If `X>=t_j`, monotonicity on `[t_j,1/2]` gives
`f(X)-f(Y)>=0`, while `g(Y)>-epsilon`.  Moreover
`f(t_j)>L` and `f(t_j)<V_j`, so
`L-V_j-epsilon<-epsilon`.  Hence the pair is strictly larger than the
first clipped price in (1.1).

Now let `t_j>=1/4`.  If `X<1/4`, use the floor, `f(Y)<V_j`, and positive
`g(Y)`.  If `X>=1/4`, monotonicity on the quarter interval gives a
nonnegative compact difference and `g(Y)>0`.  This proves the second row.

For the global anchor, if `X<1/4` use the global upper bound and (0.3)--
(0.4); if `X>=1/4`, quarter-interval decrease and positive theta give the
clipped zero branch. \(\square\)

## 2. Exact finite-grid ledger

For every `i`, choose either the global anchor or any indexed anchor
satisfying

\[
                         t_{j(i)}\le {i\over h}.        \tag{2.1}
\]

Because (0.2) is strict, that anchor is legal even when equality holds in
(2.1).  Among all eligible anchors choose one with the largest clipped
price (equivalently, the smallest theta-priced upper value), and let `p_i`
be that price from (1.1) or (1.2).  No monotonicity of the numerical
sequence `V_j` is assumed.

### Theorem 2.1 (anchor-grid ledger)

Every honest exact-first-carry table satisfies

\[
 \boxed{
 E(s)>L-\varepsilon+\sum_{i=1}^u p_i
       +\sum_{r=u+2}^{h-u-1}f(s_r/A).}                \tag{2.2}
\]

Consequently, if

\[
 \boxed{L-\varepsilon+\sum_{i=1}^u p_i>0}            \tag{2.3}
\]

for every geometrically possible `u` not already closed by the overlap-
depth theorem, then every period-`h` exact-first-carry clock is positive.
Any retained positive middle train or any joint overlap/theta credit may be
added to the left side of (2.3).

#### Proof

Use `C>L`, `g(alpha)>-epsilon`, and Lemma 1.1 on each reflected pair in
(0.1).  Every middle train is positive.  This gives (2.2), and (2.3)
implies `Phi(W)>=E(s)>0`. \(\square\)

## 3. Exact relation to the finite closures

The audited finite-period proofs are instances of Theorem 2.1 with the
anchors

\[
 \begin{array}{c|c}
 \text{anchor}&\text{certified upper value}\\ \hline
 \text{global}&1079/20000\\
 4/21&5127/100000\\
 1/5&101/2000\\
 1/4&1129/25000\\
 2/7&4083/100000.
 \end{array}                                           \tag{3.1}
\]

The common floor and theta allowance are

\[
                         L={5503\over125000},
 \qquad                  \varepsilon={1\over20000}.   \tag{3.2}
\]

Theorem 2.1 reproduces the independent-pair portions of all closures through
period twenty-one.  The `2/7` anchor has positive raw price
`L-4083/100000`, so its unconditional grid price is correctly clipped to
zero.  The period-twenty-one last chamber extracts that positive raw credit
only under the additional case `X_6<1/4`; if `X_6>=1/4`, ordered early rays
put every later pair in the decreasing quarter interval.  Thus the grid
theorem is a common ledger, not a claim that every finite proof is a blind
scalar substitution.

## 4. All-period analytic target

Define the **priced** decreasing majorant on the half interval by

\[
 B(t)=\min\left(
 V_*+\varepsilon,
 \inf_{j:t_j\le t}
   \{V_j+\varepsilon\mathbf1_{t_j<1/4}\}
 \right),                                             \tag{4.1}
\]

where an empty indexed infimum is ignored.  This incorporates the theta
allowance of the chosen anchor rather than assuming that the anchor grid
contains the quarter point.  Then the ray-only all-period problem is the
one-dimensional discrete quadrature

\[
 L-\varepsilon+
 \sum_{i=1}^u
 \min\{0,L-B(i/h)\}>0,
                                                               \tag{4.2}
\]

Equation (4.2), or the same inequality augmented by the
middle-train and overlap-depth credits in (2.2), is a sufficient all-period
theorem.

This is the shortest analytic frontier produced by the finite closures:
construct one certified majorant `B` with a uniform Riemann-sum inequality,
rather than proving a new isolated rational anchor at every period.

## 5. Scope

This lemma concerns only honest exact-first-carry **formal** cyclic Apéry
clocks.  It does not address overshoot, later first crossing, finite physical
shoulders, integral carrier rounding, common-cap compilation, or an OR-word
upper bound.
