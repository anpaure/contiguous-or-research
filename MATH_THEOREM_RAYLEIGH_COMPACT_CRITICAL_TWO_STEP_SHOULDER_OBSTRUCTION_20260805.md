# A genuine adverse two-step shoulder layer in the compact critical regime

**Date:** 2026-08-05  
**Method:** pure mathematics; an explicit saturated Bellman family and
continuity at the Rayleigh minimum; no computation, enumeration, search,
or solver  
**Status:** unconditional sharp obstruction to a termwise extension of the
small-critical-value shoulder theorem.  Saturated first-minimum Bellman
tables with least-critical value tending to \(\zeta\) from below can have
an actual positive-measure shoulder layer whose derivative-prefix train is
strictly positive.  Thus the remaining compact regime cannot be closed by
proving every critical-chain prefix slope nonpositive; compensation across
other layers or the strict formal reserve is essential.  The construction
does not give a nonpositive total Rayleigh clock.

## 1. The family

Let \(K\) be the Rayleigh kernel and \(\zeta\) its unique minimum.  Hence

\[
                         K'(\zeta)=0,
 \qquad                 K'(2\zeta)>0.              \tag{1.1}
\]

For an integer \(H\ge5\), put

\[
 N=2H,
 \qquad
 L_H=\zeta\left(1-{2\over H}\right),
 \qquad
 \lambda_H={L_H\over H}.                          \tag{1.2}
\]

Define a table \(c_0,\ldots,c_N\) by

\[
 c_j=
 \begin{cases}
 0,&0\le j<H,\\
 L_H,&j=H,\\
 \lambda_H(H+1),&H+1\le j<2H,\\
 2L_H,&j=2H.
 \end{cases}                                      \tag{1.3}
\]

### Lemma 1.1 (exact Bellman normalization)

For every \(H\ge5\), the table (1.3) is nonnegative, nondecreasing, and
internally superadditive.  Its first \(\zeta\)-crossing is at \(N=2H\),
and the endpoint is already saturated.  Its maximum density is
\(\lambda_H\), its least critical denomination is \(H\), and its complete
critical set is

\[
                         \{H,H+1,2H\}.             \tag{1.4}
\]

In particular its critical gcd is one and its formal clock is arithmetic:

\[
                         U_m=\lambda_Hm.            \tag{1.5}
\]

#### Proof

Monotonicity follows from

\[
 L_H<\lambda_H(H+1)<2L_H.
\]

Consider \(i+j\le2H\).  If \(i+j<H\), all values are zero.  If exactly
one input is at least \(H\), monotonicity and the constant middle plateau
give \(c_{i+j}\ge c_i+c_j\), because the other input has value zero.  If
both inputs are at least \(H\), then necessarily \(i=j=H\) and

\[
                         c_{2H}=2c_H.
\]

Thus the table is internally superadditive.

Every proper value is below \(\zeta\).  Indeed

\[
 \lambda_H(H+1)
 =\zeta\left(1-{2\over H}\right)left(1+{1\over H}\right)
 =\zeta\left(1-{1\over H}-{2\over H^2}\right)<\zeta. \tag{1.6}
\]

On the other hand

\[
 c_{2H}=2\zeta(1-2/H)\ge\zeta
\]

for \(H\ge4\).  The proper partition \(2H=H+H\) has value \(2L_H\),
so the endpoint is saturated exactly.

The ratios at \(H,H+1,2H\) all equal \(\lambda_H\).  Every plateau index
strictly larger than \(H+1\) has smaller ratio, and every lower index has
zero ratio.  This proves (1.4).  Consecutive critical indices have gcd one,
so the formal clock is (1.5). \(\square\)

## 2. An actual positive shoulder prefix

Put

\[
                         r=H-1.                    \tag{2.1}
\]

Since \(r<H\), the displayed physical value is zero.  At the next point
of its \(H\)-critical chain one has

\[
 \begin{aligned}
 \Delta_r
   &=U_r-V_r=\lambda_H(H-1),\\
 \Delta_{r+H}
   &=\lambda_H(2H-1)-\lambda_H(H+1)
     =\lambda_H(H-2)>0.                            \tag{2.2}
 \end{aligned}
\]

Thus, for every

\[
                         0<t<\lambda_H(H-2),        \tag{2.3}
\]

the active derivative prefix on this chain has length at least two.  Its
start is

\[
                         y_H(t)=\lambda_H(H-1)-t.   \tag{2.4}
\]

### Theorem 2.1 (positive two-step layer)

For every sufficiently large \(H\), there is an \(\epsilon_H>0\) such
that, for all \(0<t<\epsilon_H\),

\[
 \boxed{
 K'(y_H(t))+K'(y_H(t)+L_H)>0.}                    \tag{2.5}
\]

Consequently the actual active prefix satisfies

\[
 \boxed{
 J_{L_H,N_r(t)}(y_H(t))>0}                        \tag{2.6}
\]

on a positive-measure set of layers.

#### Proof

As \(H\to\infty\),

\[
 L_H\longrightarrow\zeta,
 \qquad
 \lambda_H(H-1)=L_H(1-1/H)\longrightarrow\zeta.  \tag{2.7}
\]

Therefore, at \(t=0\), the left side of (2.5) tends to

\[
                         K'(\zeta)+K'(2\zeta)
                         =K'(2\zeta)>0.            \tag{2.8}
\]

Continuity of \(K'\) gives (2.5) for all sufficiently large \(H\) and
all sufficiently small positive \(t\).  Shrink \(\epsilon_H\), if
necessary, so that (2.3) also holds.

The first two terms of the active prefix have the positive sum (2.5).
Every possible later term has argument

\[
 y_H(t)+qL_H>\zeta\qquad(q\ge2)
\]

after one further harmless shrinking of \(\epsilon_H\), because both
\(y_H(0)\) and \(L_H\) tend to \(\zeta\).  By the one-well sign law
these later terms are strictly positive.  Since (2.2)--(2.3) ensure that
the actual prefix has at least two terms, its full sum is positive.  This
proves (2.6). \(\square\)

## 3. Exact implication

The critical-chain layer-cake formula is

\[
 \Phi(V)-\Phi(U)
 =-\sum_s\int J_{L_H,N_s(t)}(U_s-t)\,dt.           \tag{3.1}
\]

Theorem 2.1 exhibits a genuine positive-measure region where one integrand
on the right is negative after the leading minus sign.  Therefore neither
of the following can hold throughout the compact critical band:

1. every active derivative prefix is nonpositive;
2. every critical chain has nonnegative shoulder correction termwise.

This is stronger than the earlier abstract one-chain no-go: the present
positive prefix occurs in an exact nonnegative, internally superadditive,
saturated first-\(\zeta\) Bellman table, and its start remains strictly
below \(\zeta\).

The theorem does **not** sum all layers of (3.1).  Other residues and
heights may provide larger favorable credit, and the formal clock has a
strict positive reserve.  Hence no nonpositive physical clock or failure
of the all-price conjecture is claimed.

The proof-safe remaining compact target is now necessarily global:

> charge the positive derivative-prefix layers to negative layers in other
> residues/heights, or directly to the strict formal inverse-circle reserve,
> using the exact Bellman/Pareto coupling.  A one-chain sign theorem is
> impossible.

## 4. Dependencies

1. `MATH_THEOREM_APERY_FINITE_SHOULDER_CRITICAL_CHAIN_LAYER_CAKE_REDUCTION_20260804.md`;
2. `MATH_THEOREM_RAYLEIGH_SMALL_CRITICAL_VALUE_SHOULDER_POSITIVITY_20260805.md`;
3. the one-well sign and continuity properties of the Rayleigh kernel.

