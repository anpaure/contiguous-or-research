# Balanced affine Beatty clocks: uniform omitted-residue closure

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves every member
of the balanced affine setup-cost no-descent family strictly positive, in
every grid size.  It does not prove positivity of the full affine family,
all finite Bellman tables, or an OR-word upper bound.

Put

\[
 A={\sqrt\pi\over2}.
\]

For an integer `h>=2`, define

\[
 d={A\over2h},\qquad L=2h-1,\qquad \tau=Ld=A-d.
\tag{0.1}
\]

The balanced affine setup-cost clock at grid `n=h+1` is

\[
 V_m=d\left\lfloor{Lm\over h}\right\rfloor.
\tag{0.2}
\]

Its selected residues modulo `L` are

\[
 S_h=\{0,1,3,\ldots,2h-3\},
\]

and the omitted residues are

\[
 E_h=\{2,4,\ldots,2h-2\}.
\]

Write

\[
 \Phi_h=\sum_{q\ge0}\sum_{r\in S_h}K((qL+r)d),
\tag{0.3}
\]

and

\[
 \Omega_h=\sum_{q\ge0}\sum_{r\in E_h}K((qL+r)d).
\tag{0.4}
\]

The residue partition gives

\[
                         C(d)=\Phi_h+\Omega_h,
\tag{0.5}
\]

where the arithmetic all-ceiling theorem gives `C(d)>0`.

## Theorem

For every integer `h>=2`,

\[
 \boxed{
 \Omega_h<-{4271\over29160000}<0.}
\tag{0.6}
\]

Consequently

\[
 \boxed{
 \Phi_h>C(d)+{4271\over29160000}
          >{4271\over29160000}>0.}
\tag{0.7}
\]

Thus the balanced affine no-descent clock is never a Bellman separator.

## 1. The omitted train as a subthreshold-period grid

For a period `sigma` put

\[
 F_\sigma(w)=\sum_{q\ge0}K(q\sigma+w).
\tag{1.1}
\]

Since the omitted residues are `2j`, `1<=j<h`, equation (0.4) becomes

\[
 \boxed{
 \Omega_h=\sum_{j=1}^{h-1}F_\tau(w_j),
 \qquad
 w_j=2jd={jA\over h}.}
\tag{1.2}
\]

Every `w_j` lies in `[2d,A-2d]`.  In particular

\[
                         \tau+w_j>A.
\tag{1.3}
\]

Thus all terms after the compact `q=0` term lie in the strictly increasing
Gaussian tail of `K`.

## 2. Exact threshold-period root-of-unity sum

For the threshold train `F_A`, the exact Jacobi reflection identity is

\[
 F_A(w)+F_A(A-w)=\rho(w),
\tag{2.1}
\]

where

\[
 \rho(At)=-4\sum_{m\ge1}e^{-4\pi m^2}\cos(2\pi mt),
\tag{2.2}
\]

and

\[
 4\sum_{m\ge1}e^{-4\pi m^2}<{1\over20000}.
\tag{2.3}
\]

Let

\[
                         S_h=\sum_{j=1}^{h-1}F_A(jA/h).
\tag{2.4}
\]

The map `j -> h-j` permutes the summands, so (2.1) gives

\[
 2S_h=\sum_{j=1}^{h-1}\rho(jA/h).
\tag{2.5}
\]

For every integer `m>=1`, the roots-of-unity identity gives

\[
 \sum_{j=1}^{h-1}\cos(2\pi mj/h)
 =\begin{cases}
   h-1,&h\mid m,\\
   -1,&h\nmid m.
  \end{cases}
\tag{2.6}
\]

Substitution into (2.2)--(2.5) yields the exact expression

\[
 S_h
 =2\sum_{m\ge1}e^{-4\pi m^2}
  -2h\sum_{\ell\ge1}e^{-4\pi h^2\ell^2}.
\tag{2.7}
\]

Therefore (2.3) implies

\[
                         \boxed{S_h<{1\over40000}.}
\tag{2.8}
\]

No factor depending on `h` is lost: the complete root-of-unity sum is
taken before the theta tail is bounded.

## 3. Uniform negative drift from shortening the period

For each `j`, compare the subthreshold and threshold trains term by term.
The compact terms agree.  For every `q>=1`, (1.3) puts both arguments in
the increasing tail and

\[
 q\tau+w_j<qA+w_j,
\]

so

\[
 F_\tau(w_j)-F_A(w_j)
 <K(\tau+w_j)-K(A+w_j)<0.
\tag{3.1}
\]

On `[A,infinity)`,

\[
 K'(x)=2(A+x)e^{-(A+x)^2}.
\tag{3.2}
\]

For

\[
 x\in[\tau+w_j,A+w_j],
\]

one has

\[
                         2A<A+x<3A.
\tag{3.3}
\]

The function `u -> u e^{-u^2}` is decreasing for `u>=1/sqrt(2)`, and
`2A>1/sqrt(2)`.  Hence throughout (3.3),

\[
                         K'(x)>6Ae^{-9A^2}.
\tag{3.4}
\]

The interval in (3.1) has length `d`, so integration gives

\[
 F_\tau(w_j)-F_A(w_j)
 <-6Ad\,e^{-9A^2}.
\tag{3.5}
\]

Summing (3.5) over `j=1,...,h-1` and using
`d=A/(2h)`, `A^2=pi/4`, gives

\[
\begin{aligned}
 \sum_{j=1}^{h-1}\bigl(F_\tau(w_j)-F_A(w_j)\bigr)
 &<-3A^2{h-1\over h}e^{-9A^2}\\
 &\le-{3\pi\over8}e^{-9\pi/4}.
\end{aligned}
\tag{3.6}
\]

The last inequality uses `(h-1)/h>=1/2`.

For a completely rational comparison, use `pi>3`, `pi<22/7`, and `e<3`:

\[
 {3\pi\over8}e^{-9\pi/4}
 >{9\over8}e^{-8}
 >{9\over8\cdot3^8}
 ={1\over5832}.
\tag{3.7}
\]

Thus

\[
 \boxed{
 \sum_{j=1}^{h-1}\bigl(F_\tau(w_j)-F_A(w_j)\bigr)
 <-{1\over5832}.}
\tag{3.8}
\]

## 4. Completion

Equations (1.2), (2.4), (2.8), and (3.8) give

\[
 \Omega_h
 <{1\over40000}-{1\over5832}
 =-{4271\over29160000}<0.
\tag{4.1}
\]

Now (0.5) and `C(d)>0` prove (0.7). \(\square\)

## 5. Scope and dependencies

The theorem closes the balanced specialization

\[
 \alpha={A\over h},\qquad\beta={A\over2h}
\]

of the affine setup-cost family.  The more general parameter interval
`0<beta<A/(h-1)` remains open, as do arbitrary subthreshold Apéry carry
tables and the all-grid Bellman inequality.

| role | file | SHA-256 |
|---|---|---|
| affine setup-cost clock | `MATH_THEOREM_AFFINE_SETUP_COST_FIRST_CROSSING_AND_APERY_NO_DESCENT_20260804.md` | `408aacd10f2e20bf26364f6464d06a7d0fb9c4d179e93e21b8a26482ce7405ce` |
| selected/omitted residue identity | `MATH_THEOREM_SIX_SLOT_AFFINE_BEATTY_OMITTED_RESIDUE_CLOSURE_20260804.md` | `0bfc91a873e559234f89231abeb6f14ef30ef43c7b727e8a8c391e7e0e0b5c46` |
| exact Jacobi reflection identity | `MATH_THEOREM_FIVE_SLOT_REPEATED_GAP_EXACT_THETA_ENDPOINT_DESCENT_20260804.md` | `0bed69bf36b52abb5eab3022f2a06f3eabe7f05cdd299d232d9fd0a7b90094ff` |
| arithmetic all-ceiling positivity | `MATH_THEOREM_SMOOTH_BINOMIAL_CONFIGURATION_DUAL_AND_CEILING_PRICE_CLASSES_20260804.md` | `c3a2c1858f59fa32e61d2f9a9252085ad7fb01f3521ab5cb46998705123e103d` |
