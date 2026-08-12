# Independent audit: four-slot Apéry scalar-gate closure

**Date:** 2026-08-04  
**Verdict:** **PASS after one proof-scope completion in Corollary 3.2.**  
**Method:** symbolic Gaussian calculus and exact rational arithmetic only;
no search, SAT/CP solver, H100, or floating-point sign decision was used.

## 1. Frozen sources and repair

The submitted theorem was

`MATH_THEOREM_FOUR_SLOT_APERY_SCALAR_GATE_CLOSURE_20260804.md`

at SHA-256

`ab18e79c4f209e1d2ab34b8c04161b14debea64e4bd81d1338f49961a536b3de`.

The scalar inequality was correct as submitted.  The proof of Corollary
3.2, however, silently used the `x,y,z<A` hypothesis from Section 7 of the
parent Apéry theorem while stating the corollary for every four-efficient
table.  The proof now explicitly applies the all-grid first-crossing
deletion theorem:

* if the first displayed crossing has capacity at most three, the positive
  prefix functional is a lower bound for the original functional;
* otherwise the crossing is the endpoint `T`, so `x,y,z<A` and the parent
  Section 7 reduction applies literally.

The repaired theorem SHA-256 is

`2b334fc6670ec73d4eba0f9de7a211b5e64f38a77f205ee822bebc4f3a79e776`.

The independent exact-rational replay is

`scratch/n4_apery_scalar_gate_independent_audit_20260804/exact_rational_replay.py`

at SHA-256

`656fd01a69cc921488472a85c1a4725747865ac5d61524b244041eae4814d50e`.

It prints `PASS: exact rational replay`.

## 2. Identification of `C(a)` with the ceiling margin

Let `sigma` be socket measure minus job measure.  Since

\[
 K(v)=\sigma([v,\infty)),
\]

layer cake for the ceiling price gives

\[
 C(a)=\sum_{m\ge0}K(ma)=S(a)-J(a),
\]

where `S(a)` and `J(a)` are exactly the socket and job sums in the
all-ceiling theorem.  The possible term at `ma=A` has socket contribution
`1-exp(0)=0`, so the endpoint convention does not affect the equality.

The Fourier estimate therefore transfers verbatim:

\[
 \left|C(a)-{M\over2}\right|
 \le {C_0a^2\zeta(3)\over4\pi^3},
 \qquad M=1-2e^{-\pi/4},
 \quad C_0=4+8e^{-3/2}.
\]

The constant comes from

\[
 |p'(0)|+\lVert p''\rVert_1=4+8e^{-3/2}
\]

for `p(z)=2z exp(-z^2)`.  The elementary Taylor bound
`e^(3/2)>4` gives `C_0<6` in the asserted strict direction.

## 3. Uniform small-step lower bound

The exact source bounds are

\[
 M>{3\over35},\qquad \zeta(3)<{5\over4},
 \qquad\pi^2>9.
\]

The first follows from

\[
 \sum_{j=0}^4{(333/424)^j\over j!}>{35\over16},
\]

so `e^(-pi/4)<16/35`.  The replayed rational excess is

\[
 {744100411\over258555281408}>0.
\]

For `a<=A/3`, one has `a^2<=pi/36`.  Consequently

\[
 {C_0a^2\zeta(3)\over4\pi^3}
 <{6(5/4)(\pi/36)\over4\pi^3}
 <{5\over864}.
\]

Thus

\[
 C(a)>{3\over70}-{5\over864}
 ={1121\over30240}.
\]

All factors and inequality directions in Lemma 1.1 are correct.

## 4. Monotonicity of the adverse decrement

Write

\[
 D(\alpha)=e^{-(A+4\alpha)^2}-e^{-(A+5\alpha)^2}
\]

and `t=alpha/A`.  Direct differentiation shows

\[
 D'(\alpha)<0
\]

if and only if

\[
 \log {5(1+5t)\over4(1+4t)}
 <{\pi\over4}t(2+9t).
\]

The rational function on the left is increasing in `t`; on
`[1/4,1/3]` it is at most `10/7<3/2`.  Since

\[
 e^{1/2}>1+{1\over2}+{1\over8}>{3\over2},
\]

its logarithm is below `1/2`.  The right side is increasing and at the
left endpoint equals `17pi/64>51/64>1/2`.  Hence `D` is strictly
decreasing, with no omitted critical point or reversed logarithmic
comparison.

Its maximum is therefore

\[
 D(A/4)=e^{-\pi}-e^{-81\pi/64}.
\]

The two exact Gaussian bounds were replayed independently:

* the degree-eight positive Taylor polynomial at `333/106` is larger than
  `160/7`, proving `e^(-pi)<7/160`; its exact polynomial margin is

  \[
  {11696223954514882761\over71404393738981703680}>0;
  \]

* with `pi<355/113`, the degree-six positive Taylor polynomial for
  `exp(81pi/64)` plus its exact geometric remainder is below `2000/37`,
  proving `e^(-81pi/64)>37/2000`; the exact margin below `2000/37` is

  \[
  {5468934762851735834586721954429
   \over17253537991099247881972514553856}>0.
  \]

Therefore

\[
 D(\alpha)<{7\over160}-{37\over2000}
 ={101\over4000}.
\]

## 5. Scalar margin

Both `4alpha` and `5alpha` lie in the Gaussian tail, so

\[
 K(4\alpha)-K(5\alpha)=-D(\alpha).
\]

Combining the two strict bounds gives

\[
\begin{aligned}
 J(\alpha)
 &>{1121\over30240}-{101\over4000}\\
 &={8936\over756000}
 ={1117\over94500}>0.
\end{aligned}
\]

The common-denominator arithmetic is exact.

## 6. Use of the parent Apéry reduction

After the repaired first-crossing split, assume `x,y,z<A`.  The exact
parent theorem makes the four-efficient functional nondecreasing in the
endpoint and reduces it to

\[
 T_0=\max\{A,2y,4z/3\}.
\]

The first face is the already-proved threshold theorem and the second is
the complete two-efficient branch.  On the third face set

\[
 \alpha=z/3\in(A/4,A/3).
\]

The exact Apéry shifts are `alpha,2alpha,3alpha`, and the parent functional
formula is

\[
 C(\alpha)+K(x)-K(\alpha)+K(y)-K(2\alpha)
 +K(4\alpha+b_1)-K(5\alpha).
\]

The first two corrections are nonnegative because `K` decreases on
`[0,2A/3]`.  Since `b_1>=0` and `K` increases on the tail,

\[
 K(4\alpha+b_1)-K(5\alpha)
 \ge K(4\alpha)-K(5\alpha).
\]

The functional is therefore at least `J(alpha)>0`.  The parent reduction
contains every capacity below nine, including its delayed capacity-five
correction; no finite Apéry head was silently discarded.

## 7. Verdict and scope

The scalar Fourier bound, decrement monotonicity, all rational Gaussian
certificates, and the repaired corollary are valid.

**Final verdict: PASS.**  Together with the separately audited exact Apéry
normal form, this closes the complete four-slot-efficient branch.

It does not close the three-slot-efficient branch, all `n=4` tables, the
universal Bellman inequality, or `nu(k)<=B(k)+O(1)`.
