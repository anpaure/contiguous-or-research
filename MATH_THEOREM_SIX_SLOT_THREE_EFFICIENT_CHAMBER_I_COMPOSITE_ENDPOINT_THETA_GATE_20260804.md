# Six-slot `h=3` chamber I: exact composite-endpoint theta gate

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It replaces the
complete chamber-I retained-pulse expression by one exact compact theta
gate after descending at its first composite threshold endpoint.  It does
not sign that gate or prove chamber-I positivity.

Put

\[
 A={\sqrt\pi\over2},
 \qquad F(w)=\sum_{q\ge0}K(qA+w),
 \qquad C=F(0).
\]

For `0<=w<=A`, define

\[
 \rho(w)=-4\sum_{m\ge1}e^{-4\pi m^2}
                 \cos\left({2\pi m w\over A}\right).
\tag{0.1}
\]

The exact Jacobi reflection identity is

\[
                         F(w)+F(A-w)=\rho(w).
\tag{0.2}
\]

Consider the chamber-I gate

\[
\begin{aligned}
 \mathcal G_{\rm I}(p,a,b)={}&\mathcal L_3(p;a,2a)\\
 &+K(b-a)-K(a)+K(b)-K(2a)\\
 &+K(p+b)-K(p+2a),
\end{aligned}
\tag{0.3}
\]

on its exact domain

\[
 {A\over2}\le p<A,qquad 0\le a\le {p\over3},qquad
 a\le b\le2a,qquad b<A-p.
\tag{0.4}
\]

## 1. The literal six-point prefix

The three differences in (0.3) replace exactly the eventual values
`a`, `2a`, and `p+2a`.  Hence the clock summed by (0.3) begins

\[
 W_0,\ldots,W_6=
 0,\ b-a,\ b,\ p,\ p+a,\ p+b,\ 2p,
\tag{1.1}
\]

and from capacity six onward agrees with the three-residue Apéry clock.
Equivalently, it is the Bellman clock of the internally superadditive
table

\[
                         (0,b-a,b,p,p+a,p+b,2p).
\tag{1.2}
\]

The inequalities needed for (1.2) are consequences of `b<=2a` and
`p>=3a`; this is also the extremal table attaining every lower replacement
used in the chamber-I reduction.  In particular, `W` is superadditive.

By (0.4),

\[
 W_i<A\quad(0\le i\le5),
 \qquad W_6=2p\ge A.
\tag{1.3}
\]

Thus the first threshold point is the composite endpoint at capacity six.

## 2. Six-point composite-endpoint descent

Superadditivity gives

\[
 W_{6q+i}\ge qW_6+W_i\ge qA+W_i
 \qquad(q\ge1,\ 0\le i<6).
\tag{2.1}
\]

Both sides of (2.1) lie in the increasing Gaussian tail of `K`.
Consequently

\[
\boxed{
 \mathcal G_{\rm I}(p,a,b)
 \ge\sum_{i=0}^{5}F(W_i).
}
\tag{2.2}
\]

This proof also covers the boundary `2p=A`; no strict endpoint crossing is
required.

## 3. Exact compact coordinates

Set

\[
                         x=b-a,
 \qquad d=A-p-b.
\tag{3.1}
\]

Then

\[
\begin{aligned}
 W_1&=x,&W_2&=b,\\
 W_3&=A-(d+b),&W_4&=A-(d+x),&W_5&=A-d.
\end{aligned}
\tag{3.2}
\]

The projected domain (0.4) is equivalently

\[
\boxed{
 0\le x\le {b\over2},qquad d>0,qquad
 b+d\le {A\over2},qquad d+4b-3x\le A.
}
\tag{3.3}
\]

Indeed `a=b-x` and `p=A-b-d`; the four inequalities in (3.3) are,
respectively, `a<=b<=2a`, `b<A-p`, `p>=A/2`, and `p>=3a`.

Apply (0.2) to the last three entries in (3.2).  Equation (2.2) becomes

\[
\boxed{
 \mathcal G_{\rm I}(p,a,b)\ge \mathcal Q_{\rm I}(x,b,d),
}
\tag{3.4}
\]

where

\[
\boxed{
\begin{aligned}
 \mathcal Q_{\rm I}(x,b,d)={}&C+F(x)+F(b)\\
 &-F(d)-F(d+x)-F(d+b)\\
 &+\rho(d)+\rho(d+x)+\rho(d+b).
\end{aligned}}
\tag{3.5}
\]

Every argument in (3.5) lies in `[0,A/2]`.  No uniform reflection error,
finite availability pulse, or infinite tail remains outside this gate.

### Theorem (exact residual chamber-I gate)

The compact inequality

\[
 \boxed{\mathcal Q_{\rm I}(x,b,d)>0}
\tag{3.6}
\]

on (3.3) is sufficient to prove

\[
                         \mathcal G_{\rm I}(p,a,b)>0
\]

throughout chamber I.

Since

\[
 |\rho(w)|\le
 4\sum_{m\ge1}e^{-4\pi m^2}< {1\over20000},
\]

the stronger but phase-free inequality

\[
 C+F(x)+F(b)-F(d)-F(d+x)-F(d+b)>{3\over20000}
\tag{3.7}
\]

also suffices.

## 4. Scope

This theorem is a reduction only.  It does not assert (3.6), complete
chamber-I positivity, complete six-slot positivity, the all-grid Bellman
inequality, or an OR-word upper bound.  In particular it does not reuse
the delayed five-slot `b`-concavity theorem across the opposite
prethreshold inequality `p+b<A`.

## 5. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| exact chamber-I normal form | `MATH_THEOREM_SIX_SLOT_THREE_EFFICIENT_EXACT_THREE_CHAMBER_GATE_20260804.md` | `a3a79b92148b1b4b415c7795473b70f50bd6d0b84f20f6899a3275f62af9b0dd` |
| exact Jacobi reflection identity | `MATH_THEOREM_FIVE_SLOT_REPEATED_GAP_EXACT_THETA_ENDPOINT_DESCENT_20260804.md` | `0bed69bf36b52abb5eab3022f2a06f3eabe7f05cdd299d232d9fd0a7b90094ff` |

