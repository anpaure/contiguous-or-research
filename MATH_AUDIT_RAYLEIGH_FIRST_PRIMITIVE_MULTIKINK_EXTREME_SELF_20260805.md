# Self-audit of the first primitive multi-kink Apéry extreme

**Date:** 2026-08-05  
**Method:** independent algebraic replay; pure mathematics; no computation,
search, or solver  
**Audited source:**
`MATH_THEOREM_RAYLEIGH_FIRST_PRIMITIVE_MULTIKINK_EXTREME_AND_POSITIVE_RESERVE_20260805.md`  
**Verdict:** **PASS.**  The period-four cone classification, period-five
extremality and primitivity, phase regrouping, Fourier coefficients, and
strict rational reserve all check.

## 1. Cyclic-block equivalence

For increments `x_i=s_i-s_(i-1)`, a nonwrapping block has value

\[
 B_a(j)=s_{a+j}-s_a,
\]

while a wrapping block has value

\[
 B_a(j)=P+s_{a+j-g}-s_a.
\]

In the two cases, `B_a(j)>=s_j=B_0(j)` is exactly the ordinary or carry
superadditivity inequality.  Thus Lemma 1.1 is an iff, not merely a
necessary condition.

## 2. Small-period cone classification

For `g=3`, length one makes `x_1` minimum and length two makes `x_3`
maximum, yielding `x_1<=x_2<=x_3`.

For `g=4`, the length-one and length-three constraints are

\[
 x_1\le x_i\le x_4\qquad(1\le i\le4).
\]

They imply all length-two comparisons termwise.  After subtracting the
constant vector, an inversion `y_2>y_3` is removed by

\[
 (y_2-y_3)(0,1,0,1),
\]

and the residual last coordinate remains at least `y_3` because
`y_4>=y_2`.  The exceptional vector has period two and a zero defect at
residue two.  Hence the claimed “one-kink or proper-period” classification
through `g=4` is exact.

## 3. Period-five extreme ray

For `x^*=(0,1,0,1,1)`, the cyclic block rows are

\[
\begin{array}{c|ccccc}
1&0&1&0&1&1\\
2&1&1&1&2&1\\
3&1&2&2&2&2\\
4&2&3&2&3&2.
\end{array}
\]

The first entry is minimal in every row.  If `x^*=y+z` inside the cone,
the zero coordinates force `y_1=y_3=0` and `z_1=z_3=0`.  The active
length-two comparisons with starts two and four then force

\[
 y_2=y_4=y_5,
 \qquad
 z_2=z_4=z_5.
\]

Both summands lie on the original ray, proving extremality.

At scale `eta`, the proper shift/density comparisons are

\[
 0<{3\eta\over5},
 \quad
 \eta<{6\eta\over5},
 \quad
 \eta<{9\eta\over5},
 \quad
 2\eta<{12\eta\over5}.
\]

Thus all proper defects are strictly positive.  Since five is prime, the
only proper-period lift is constant; nonmonotonicity excludes the
one-kink cone.  The “first genuinely primitive new extreme” conclusion is
therefore valid.

## 4. Phase regrouping

The five phases are

\[
 0,0,\eta,\eta,2\eta
\]

in period `P=3eta`.  Hence

\[
 \Phi_5^*
 =\bigl(F_P(0)+F_P(\eta)+F_P(2\eta)\bigr)
  +F_P(0)+F_P(\eta)
 =C(\eta)+\Psi(\eta).
\]

This is an exact partition of the terms, with no finite-head correction.

## 5. Two-phase Fourier replay

For the point train at residues `0,eta` modulo `P=3eta`, the periodic
counting discrepancy has derivative

\[
 D'=\delta_0+\delta_\eta-{2\over P}.
\]

Its mean is

\[
 {1\over P}
 \left(
 \int_0^\eta\left(1-{2x\over P}\right)dx
 +\int_\eta^P\left(2-{2x\over P}\right)dx
 \right)
 ={2\over3}.
\]

For `n!=0`,

\[
 |\widehat D_n|
 ={|1+e^{-2\pi i n/3}|\over2\pi|n|}.
\]

The numerator has magnitude two on multiples of three and one otherwise,
so

\[
 \sum_{n\ge1}{|1+e^{-2\pi i n/3}|\over n^3}
 =\zeta(3)+{1\over27}\zeta(3)
 ={28\over27}\zeta(3).
\]

Combining this with the audited transform bound

\[
 |\widehat q(2\pi n/P)|
 <{BP^2\over4\pi^2n^2}
\]

and pairing signs gives exactly

\[
 |\text{nonzero modes}|
 <{7B\eta^2\over3\pi^3}\zeta(3).
\]

There is no lost factor of `P`, two, or `pi`.

## 6. Rational reserve

The normalized period condition gives

\[
 \eta^2={P^2\over9}\le{\zeta^2\over9}<{2\over27}.
\]

Thus, with `B=5324/875`, `zeta(3)<5/4`, and `pi^3>27`,

\[
 |\text{nonzero modes}|
 <{7\over3}{5324\over875}{2\over27}{5\over4}{1\over27}
 ={2662\over54675}.
\]

The zeroth mode obeys

\[
 {2M\over3}>{22\over375}.
\]

Their difference is

\[
 {22\over375}-{2662\over54675}
 ={2728\over273375}>0.
\]

Hence `Psi` is strictly positive, and adding the independently proved
arithmetic reserve `C(eta)>377/108000` proves the displayed bound for
`Phi_5^*`.

## 7. Scope

This result refutes only the proposed structural generation by one-kink
and collapsed-period rays; it does not refute positivity.  It signs the
smallest new primitive extreme, but does not classify higher-period
extremes or justify minimizing a nonlinear phase functional solely on
cone extreme rays.  The source states those limitations explicitly.

**Final verdict: PASS.**
