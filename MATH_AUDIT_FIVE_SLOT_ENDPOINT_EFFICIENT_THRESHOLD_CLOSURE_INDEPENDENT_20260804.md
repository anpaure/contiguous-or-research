# Independent audit: five-slot endpoint-efficient threshold closure

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_FIVE_SLOT_ENDPOINT_EFFICIENT_THRESHOLD_CLOSURE_20260804.md`  
**Method:** independent endpoint-period comparison, derivative audit, and
exact rational Gaussian bounds.  No search or floating-point sign test is
used.  
**Verdict:** **PASS**.

## 1. Endpoint normalization and scope

After first-crossing deletion and endpoint saturation, assigning ties to
the least maximum-density index has an exact consequence: a genuine
`h=5` table has `c_5=A`.  If saturation produced `c_5>A`, an attaining
lower partition would contain a denomination of at least the endpoint
density, so the table would be assigned to `h<5` instead.

Thus the theorem analyzes exactly the genuine endpoint branch, not all
tables for which size five happens to tie before normalization.

## 2. Exact train identity

For `0<=t<=1`, the `q=0` train term is

\[
 1-e^{-a(1-t)^2}-e^{-a(1+t)^2},
\]

and every `q>=1` term is `-e^{-a(1+t+q)^2}`.  Their sum is precisely

\[
 F_A(At)=1-E(1-t)-\sum_{n\ge0}E(1+t+n).
\]

Differentiating produces the theorem's formula with `h(x)=xE(x)`.  There
is no missing compact term at `t=0` or `t=1`; the kernel and its first
derivative match at the threshold.

## 3. Monotonicity audit

For `u=1-t in [1/5,1/2]`, the derivative tail starts at `2-u>=3/2`, where
`h` decreases.  The two-term integral majorant has the correct direction:

\[
 \sum_{n\ge0}h(2-u+n)
 \le h(2-u)+h(3-u)+{e^{-a(3-u)^2}\over2a}.
\]

The resulting difference is `J(u)`.  Its second derivative is

\[
 h''(u)-h''(2-u)-h''(3-u)+h'(3-u).
\]

On the stated interval every summand is negative.  Hence `J` is concave,
and endpoint checking is sufficient.  Direct substitution gives exactly
the two expressions in the theorem.  The `Q_9` bounds occur only on
positive terms; reciprocal `P_8` bounds occur only on subtracted terms.
The rational signs `J(1/5)>1/25` and `J(1/2)>1/10` therefore have the
correct direction.  This proves strict decrease of `F_A` on
`[A/2,4A/5]`.

## 4. Endpoint Gaussian bounds

For decreasing `E`,

\[
 \sum_{m\ge0}E(z+m)
 \le E(z)+\int_z^\infty E(x)dx
 \le E(z)(1+(2az)^{-1}).
\]

At `3A/5`, the residual tail really begins at `18/5`; at `4A/5`, it
begins at `19/5`.  The exponents and coefficients audit as follows:

\[
\begin{array}{c|c|c}
t&\text{three explicit exponents}&\text{residual exponent/coefficient}\\ \hline
3/5&\pi/25,16\pi/25,169\pi/100
   &81\pi/25,\ 1+5/(9\pi)\\
4/5&\pi/100,81\pi/100,49\pi/25
   &361\pi/100,\ 1+10/(19\pi).
\end{array}
\]

Replacing every subtracted exponential by its reciprocal-`P_8` upper
bound gives exactly `B_3` and `B_4`.  Their rational expansions establish

\[
 F_A(3A/5)>-1/40,
 \qquad F_A(4A/5)>-21/400.
\]

Monotonicity plus the previously proved positivity on `[0,A/2]` extends
these to the complete intervals claimed.

## 5. Endpoint-period and availability audit

For capacity `5q+r`, the actual Bellman clock contains the configuration
of `q` endpoint generators and one size-`r` generator.  Since `c_5=A`,

\[
 V_{5q+r}\ge qA+c_r.
\]

For `q>=1`, both arguments are at least `A`, where `K` increases.  For
`q=0`, internal superadditivity gives `V_r=c_r`.  Summing proves

\[
 \Phi\ge C(A)+\sum_{r=1}^{4}F_A(c_r)
\]

on the literal clock.  Thus none of the sixteen endpoint Apéry witnesses
or their finite availability corrections is silently deleted.

Maximum density gives `c_i<=iA/5`.  Applying the train bounds yields the
strict margin

\[
 {1\over25}+{1\over25}-{1\over40}-{21\over400}
 ={1\over400}.
\]

**Final verdict: PASS.**  The genuine five-slot endpoint-efficient branch
is positive.  Combined with the size-two closure, only `h=3,4` remain at
five slots; no all-slot conclusion is asserted.
