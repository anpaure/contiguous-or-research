# Any fixed-factor companion cylinder suffices for the bottom Haxell step

**Date:** 2026-08-05  
**Method:** rescaling the exact option/load ledger and the separator
reservation constants; no computation or search  
**Status:** unconditional reduction.  The bottom completion does not need a
`1+o(1)` cylinder constant.  For every absolute `C>=1`, a two-mark cylinder
with intensity at most `C H/[W(r)_2]` through order `O(d)` is sufficient.
The two bank densities and the separator sacrifice may be enlarged by
constants depending on `C`.  Consequently the companion-selector target
may lose a fixed factor per prescribed macro; only dimension-dependent
loss is forbidden.

## 1. Fixed-factor marked cylinder

Retain the notation of
`MATH_THEOREM_PRE_RESERVED_KY_OPTION_TAIL_AND_TWO_MARK_CYLINDER_GATE_20260805.md`.
Replace `(C2)` by

\[
 \boxed{
 \mathbb E\!\left[\prod_{a=1}^mX_{\alpha_a}\mid B_0,B_1\right]
 \le\left({C H\over W(r)_2}\right)^m}
 \qquad(m\le C_0d),                                      \tag{1.1}
\]

where `C` is fixed independently of `k`.

The Laplace expansion in that theorem is linear in the cylinder intensity.
Thus the natural resource-load means become

\[
                         C\rho_0,
 \qquad                  C\rho_1,                         \tag{1.2}
\]

while the one-task option degree remains

\[
                         \bar D
 =(1+o(1))p_0p_1^2{y\choose2}.                             \tag{1.3}
\]

The environment tails are properties of the pre-reserved uniform banks and
are unchanged.

## 2. Rescaled Haxell margin

The bounded-degree option pruning has type-zero multiplicity one and a
fixed type-one multiplicity.  Repeating the proof of equation (5.12) in the
pre-reserved theorem, with (1.2), gives the sufficient asymptotic margin

\[
 \boxed{
 1>2C\left({1\over\beta_0}+{4\over\beta_1}\right).}        \tag{2.1}
\]

For example, take

\[
                         \beta_0=\beta_1=20C.              \tag{2.2}
\]

Then the right side of (2.1) is `1/2`.

Choose the separator-sacrifice constant `c` so that

\[
                         c>\beta_0+\beta_1-2;              \tag{2.3}
\]

for instance `c=40C`.  The upper-level scalar ratio after both banks are
pre-reserved is

\[
                         2+c-\beta_0-\beta_1+o(1)=2+o(1),  \tag{2.4}
\]

so every level `j>=2` retains fixed positive slack.  Since `C,c,beta_0,
beta_1` are absolute constants and `W/H=d+1+o(1)`, the two banks fit for
all sufficiently large `d`, and the sacrificed copy count

\[
                         \lceil cH/d\rceil                 \tag{2.5}
\]

remains exactly on the permitted `O(H/d)` scale.

The option mean in (1.3) is still `Theta(d)`—only its fixed leading
constant changes—so every Chernoff and size-biased exponential tail remains
`exp[-Omega_C(d)]`.

## 3. Shared duplicate marks

Suppose the unmarked macro partition has

\[
 \Pr(\Pi=\pi\mid B_0,B_1)
 \le (C\eta_*)^{|\pi|}\kappa^{m-|\pi|},
 \qquad
                         \eta_*={H\over Wr},               \tag{3.1}
\]

where `kappa=exp[-Omega(d log d)]`.  Give every macro its common uniform
mark from an aperture of size `a=r-d+1`.

The partition expansion now has merger parameter

\[
                         {a\kappa\over C\eta_*},            \tag{3.2}
\]

which is even smaller than in the unit-constant theorem.  Uniformly for
`m=O(d)`, it yields

\[
 \Pr(\text{prescribed two-mark states})
 \le\left((1+o(1)){C\eta_*\over a}\right)^m
 \le\left((1+o(1)){C H\over W(r)_2}\right)^m.             \tag{3.3}
\]

Thus (1.1) follows.

## 4. Consequence for the stopped-hazard target

It is enough to prove the macro cylinder with **some absolute root cost**:

\[
 \boxed{
 \Pr(\Pi=\pi\mid B_0,B_1)
 \le (C\eta_*)^{|\pi|}\kappa^{m-|\pi|}}
\tag{4.1}

for one fixed `C` and every `m=O(d)`.

In particular, an across-round shared-competitor calculation may spend
`exp(O(|pi|))`; it need not achieve `exp(o(|pi|))`.  A loss such as
`(log d)^|pi|` is still fatal, because no fixed choice of bank and sacrifice
constants absorbs it.

This changes the quantitative target for the regenerative macro selector:
prove constant cost per stopped root, exponentially small cost per
same-macro merger, and separator-small cleanup.  Exact asymptotic product
measure is unnecessary.

