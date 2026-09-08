# Independent audit: balanced affine Beatty uniform omitted-residue closure

**Date:** 2026-08-04  
**Verdict:** **GO.**  Every balanced affine setup-cost clock has strictly
positive Bellman functional.  The omitted-train identity, root-of-unity
sum, period-shortening direction, derivative lower bound, rational drift,
and final uniform margin all check for every integer `h>=2`.

## 1. Exact binding and dependencies

Audited theorem:

`MATH_THEOREM_BALANCED_AFFINE_BEATTY_UNIFORM_OMITTED_RESIDUE_CLOSURE_20260804.md`

SHA-256:

`fda0267a9d09b6876ec761cfd5665e2da6c56bdcfc4fc1a05e954765bdffca2c`

The frozen dependency hashes all match the current workspace:

| role | SHA-256 |
|---|---|
| affine setup-cost clock | `408aacd10f2e20bf26364f6464d06a7d0fb9c4d179e93e21b8a26482ce7405ce` |
| selected/omitted residue identity | `0bfc91a873e559234f89231abeb6f14ef30ef43c7b727e8a8c391e7e0e0b5c46` |
| exact Jacobi reflection identity | `0bed69bf36b52abb5eab3022f2a06f3eabe7f05cdd299d232d9fd0a7b90094ff` |
| arithmetic all-ceiling positivity | `c3a2c1858f59fa32e61d2f9a9252085ad7fb01f3521ab5cb46998705123e103d` |

No theorem byte was changed during this audit.

## 2. Omitted train and threshold geometry

With

\[
 d={A\over2h},\qquad L=2h-1,
 \qquad \tau=Ld=A-d,
\]

the omitted residue `2j` contributes the train with shift

\[
 w_j=2jd={jA\over h}\qquad(1\le j<h).
\]

Therefore

\[
 \Omega_h=\sum_{j=1}^{h-1}F_\tau(w_j)
\]

exactly.  Its smallest shift is `2d`, so

\[
 \tau+w_j\ge A-d+2d=A+d>A.
\]

Thus every positive-period term lies strictly in the increasing Gaussian
tail; this verifies the range needed later for every `h>=2`.

## 3. Root-of-unity threshold sum

Put

\[
 S_h=\sum_{j=1}^{h-1}F_A(jA/h).
\]

The involution `j -> h-j`, including its possible fixed point, and the
exact reflection identity give

\[
 2S_h=\sum_{j=1}^{h-1}\rho(jA/h).
\]

For every positive integer `m`,

\[
 \sum_{j=1}^{h-1}\cos(2\pi mj/h)
 =\begin{cases}h-1,&h\mid m,\\-1,&h\nmid m.
 \end{cases}
\]

Substituting the complete cosine sum before estimating its tail yields

\[
 S_h=2\sum_{m\ge1}e^{-4\pi m^2}
      -2h\sum_{\ell\ge1}e^{-4\pi h^2\ell^2}.
\]

The second term is nonnegative before its minus sign.  Since the frozen
theta estimate says

\[
 4\sum_{m\ge1}e^{-4\pi m^2}<{1\over20000},
\]

one gets the uniform, strict upper bound

\[
                         S_h<{1\over40000}.
\]

There is no hidden factor of `h` in this step.

## 4. Period-shortening drift

The compact `q=0` entries of `F_tau(w_j)` and `F_A(w_j)` agree.  For
`q>=1`,

\[
 q\tau+w_j<qA+w_j,
\]

and both arguments exceed `A`.  Because `K` is strictly increasing on
that tail, every difference is negative.  Retaining only the first such
difference therefore has the correct strict direction:

\[
 F_\tau(w_j)-F_A(w_j)
 <K(\tau+w_j)-K(A+w_j)<0.
\]

For `x in [tau+w_j,A+w_j]`, the shift range gives

\[
                         2A<A+x<3A.
\]

Since `u e^{-u^2}` is decreasing above `1/sqrt(2)` and
`2A=sqrt(pi)>1/sqrt(2)`,

\[
 K'(x)=2(A+x)e^{-(A+x)^2}>6Ae^{-9A^2}.
\]

The comparison interval has length `d`; integration and summation over
the `h-1` shifts give

\[
 \sum_j(F_\tau(w_j)-F_A(w_j))
 <-3A^2{h-1\over h}e^{-9A^2}
 \le-{3\pi\over8}e^{-9\pi/4}.
\]

The negative-inequality direction is correct because `(h-1)/h>=1/2`.

Finally, `pi>3`, `pi<22/7`, and `e<3` imply

\[
 {3\pi\over8}e^{-9\pi/4}
 >{9\over8}e^{-8}
 >{9\over8\cdot3^8}
 ={1\over5832}.
\]

Here `pi<22/7` gives `9pi/4<8`, so the exponential comparison also has
the stated direction.  Hence the total drift is strictly below
`-1/5832`.

## 5. Final exact margin and scope

Combining the threshold sum and drift,

\[
 \Omega_h<{1\over40000}-{1\over5832}
 =-{4271\over29160000}<0.
\]

The arithmetic residue partition is exact and `C(d)>0`, so

\[
 \Phi_h=C(d)-\Omega_h
 >C(d)+{4271\over29160000}
 >{4271\over29160000}.
\]

This closes the balanced choice

\[
 \alpha=A/h,\qquad\beta=A/(2h)
\]

for every grid `n=h+1`.  It does not sign the entire affine parameter
interval, arbitrary subthreshold Apéry carries, all Bellman tables, or an
OR-word upper bound.
