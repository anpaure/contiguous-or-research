# Exact failure of threshold-period relaxation at the common repeated-gap corner

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical obstruction.  It proves that
replacing the true composite endpoint period by the threshold period `A`
is strictly lossy at the common uniform boundary of both repeated-gap
orientations: the resulting five-train lower bound is negative even though
the actual train, and the first descent retaining its composite period,
are positive.  Hence this threshold-period relaxation cannot by itself
close either gate on its full closed domain.

Put

\[
 A={\sqrt\pi\over2},
 \qquad
 F(v)=F_A(v)=\sum_{q\ge0}K(qA+v),
 \qquad C=F(0).
\]

The exact reflected-train identity is

\[
 F(v)+F(A-v)=R(v),
\tag{0.1}
\]

where

\[
 R(v)=-4\sum_{m\ge1}e^{-4\pi m^2}
             \cos\left({2\pi m v\over A}\right).
\tag{0.2}
\]

The long-singleton gate is

\[
 \mathcal P(p,a)=\mathcal L_3(p;a,2a).
\]

At its common boundary

\[
 a={A\over4},
 \qquad p=A-a={3A\over4}=3a,
\tag{0.3}
\]

the actual three-residue train interlaces into the arithmetic clock of
step `A/4`, and therefore

\[
\mathcal P(3A/4,A/4)=C(A/4)>0.
\tag{0.4}
\]

The short-singleton gate

\[
 \mathcal R(a,\beta)=\mathcal L_3(a+2\beta;a,a+\beta)
\]

has the same limiting uniform point at

\[
 a=\beta={A\over4}.
\tag{0.5}
\]

Indeed its first six clock values are then again

\[
 0,{A\over4},{A\over2},{3A\over4},A,{5A\over4},
\]

and its actual value is the same positive ceiling `C(A/4)`.

## Theorem 1.1

The five-residue train obtained after replacing the true composite period
`E=5A/4` by `A` is strictly negative:

\[
\boxed{
 S:=C+F(A/4)+F(A/2)+F(3A/4)+F(A)<0.
}
\tag{1.1}
\]

Consequently no argument which performs this threshold-period replacement
can prove positivity on the complete closed domain without retaining
additional phase information.

### Proof

Apply (0.1) at `v=0`, `A/4`, and `A/2`.  Then

\[
 C+F(A)=R(0),
 \qquad
 F(A/4)+F(3A/4)=R(A/4),
 \qquad
 F(A/2)={1\over2}R(A/2).
\]

Hence

\[
 S=R(0)+R(A/4)+{1\over2}R(A/2).
\tag{1.2}
\]

Put `q=e^{-4pi}`.  The coefficient of `q^{m^2}` in (1.2) is

\[
 -4-4\cos(\pi m/2)-2(-1)^m.
\tag{1.3}
\]

It equals

\[
 \begin{cases}
 -2,&m\text{ odd},\\
 -2,&m\equiv2\pmod4,\\
 -10,&m\equiv0\pmod4.
 \end{cases}
\tag{1.4}
\]

Every coefficient is strictly negative and every `q^{m^2}` is positive.
Thus `S<0`, proving (1.1). \(\square\)

## 2. Scope

The obstruction is to the threshold-period relaxation, not to the Bellman
claim.  In fact (0.4) is strictly positive.  At the corner, the first
five-point descent with its true period `E=5A/4` is exact: its five residue
classes interlace into the same positive clock `C(A/4)`.  The negative
train appears only in the second monotone step `F_E -> F_A`; that
replacement discards precisely the period structure that makes the uniform
boundary an arithmetic ceiling.

Therefore a successful proof of the long-singleton gate must retain at
least one of:

1. the true period-three derivative;
2. the true composite period `E` or an exact comparison to the arithmetic
   ceiling before the replacement `E -> A`; or
3. a boundary-stable interpolation that keeps the period-three phase.

The same obstruction occurs in both orientations because they meet at
the same uniform arithmetic train.  This note is an obstruction to the
threshold-period replacement `F_E -> F_A`, not to composite endpoint
descent itself and not a counterexample to either gate or to the full
five-slot Bellman problem.
