# Six-slot size-three-efficient clocks: exact three-chamber scalar gate

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It resolves the two
Apéry maxima in the surviving six-slot `h=3` branch, retains all five
availability pulses in proof-safe directions, and reduces the complete
branch to three explicit scalar gates meeting continuously along two
ordered walls.  It does not sign those three gates or prove complete
six-slot positivity.

Put

\[
                         A={\sqrt\pi\over2}.
\]

Consider a normalized six-slot table in the `h=3` branch.  Write

\[
 p=c_3,qquad a=c_4-p,qquad b=c_5-p.
\tag{0.1}
\]

The exact canonical normal form gives

\[
 c_6=2p,qquad {A\over2}\le p<A,
\tag{0.2}
\]

and

\[
 0\le a\le {p\over3},qquad
 a\le b\le {2p\over3},qquad
 a,b<A-p.
\tag{0.3}
\]

The inequality `b>=a` follows from endpoint superadditivity
`c_5>=c_1+c_4`.  The two eventual shifts are

\[
 s_1=\max\{a,2b-p\},
 \qquad
 s_2=\max\{b,2a\}.
\tag{0.4}
\]

The full five-pulse formula is

\[
\begin{aligned}
 \Phi={}&\mathcal L_3(p;s_1,s_2)\\
 &+K(c_1)-K(s_1)
  +K(p+a)-K(p+s_1)\\
 &+K(V_7)-K(2p+s_1)\\
 &+K(c_2)-K(s_2)
  +K(p+b)-K(p+s_2),
\end{aligned}
\tag{0.5}
\]

where

\[
                         V_7=\max\{2p+a,p+b+c_2\}.
\tag{0.6}
\]

Every term in (0.5) is retained until its sign or exact cancellation is
proved below.

## 1. The two walls are ordered

Because `p>=3a`,

\[
                         2a\le {p+a\over2}.
\tag{1.1}
\]

Therefore the projected parameter domain has exactly the three chambers

\[
\begin{array}{ll}
\mathrm I:&a\le b\le2a,\\
\mathrm {II}:&2a\le b\le(p+a)/2,\\
\mathrm {III}:&(p+a)/2\le b<A-p.
\end{array}
\tag{1.2}
\]

Empty chambers are harmless.  On these chambers, respectively,

\[
 (s_1,s_2)=
 (a,2a),\qquad(a,b),\qquad(2b-p,b).
\tag{1.3}
\]

## 2. Chamber I: the prethreshold retained-pulse gate

Define

\[
\boxed{
\begin{aligned}
 \mathcal G_{\rm I}(p,a,b)={}&\mathcal L_3(p;a,2a)\\
 &+K(b-a)-K(a)+K(b)-K(2a)\\
 &+K(p+b)-K(p+2a).
\end{aligned}}
\tag{2.1}
\]

### Proposition 2.1

On chamber I,

\[
                         \boxed{\Phi\ge\mathcal G_{\rm I}(p,a,b).}
\tag{2.2}
\]

#### Proof

Here `(s_1,s_2)=(a,2a)`.  The size-four pulse vanishes.  Moreover,

\[
 p+b+c_2\le p+2b\le p+4a\le2p+a,
\]

using `c_2<=b`, `b<=2a`, and `3a<=p`.  Thus

\[
                         V_7=2p+a=2p+s_1,
\]

so the capacity-seven pulse also vanishes.

Superadditivity gives

\[
 c_1\le b-a\le a,qquad c_2\le b\le2a.
\]

All these arguments are below `3A/4`, where `K` is decreasing.  Hence

\[
 K(c_1)-K(a)\ge K(b-a)-K(a),
\]

and

\[
 K(c_2)-K(2a)\ge K(b)-K(2a).
\]

The size-five pulse remains exactly
`K(p+b)-K(p+2a)`.  Substitution in (0.5) proves (2.2). \(\square\)

This has the same algebraic expression as the retained-pulse gate in the
five-slot proof, but the range is opposite: here `b<A-p`, so the size-five
value is still below threshold.

## 3. Chamber II: one pure ordered-gap lattice

Define

\[
                         \boxed{
 \mathcal G_{\rm II}(p,a,b)=\mathcal L_3(p;a,b).}
\tag{3.1}
\]

### Proposition 3.1

On chamber II,

\[
                         \boxed{\Phi\ge\mathcal G_{\rm II}(p,a,b).}
\tag{3.2}
\]

#### Proof

Here `(s_1,s_2)=(a,b)`, so the size-four and size-five pulses vanish.
Also

\[
 p+b+c_2\le p+2b\le2p+a,
\]

and hence `V_7=2p+a=2p+s_1`; the capacity-seven pulse vanishes.

Finally `c_1<=a` and `c_2<=b`.  Since

\[
 0\le c_1\le a<A-p\le A/2,
 \qquad
 0\le c_2\le b<A-p\le A/2,
\]

the two remaining pulses are nonnegative by compact monotonicity of `K`.
Dropping them proves (3.2). \(\square\)

The cyclic gaps of this lattice satisfy

\[
                         a\le b-a\le p-b.
\tag{3.3}

Indeed `b>=2a` gives the first inequality, and
`b<=(p+a)/2` gives the second.  Thus the middle chamber is one
three-coset lattice with ordered gaps and no adverse finite pulse.

## 4. Chamber III: two exact adverse comparisons

Define

\[
\boxed{
\begin{aligned}
 \mathcal G_{\rm III}(p,a,b)={}&
 \mathcal L_3(p;2b-p,b)\\
 &+K(p+a)-K(2b)\\
 &+K(2p+a)-K(p+2b).
\end{aligned}}
\tag{4.1}
\]

### Proposition 4.1

On chamber III,

\[
                         \boxed{\Phi\ge\mathcal G_{\rm III}(p,a,b).}
\tag{4.2}
\]

#### Proof

Here `(s_1,s_2)=(2b-p,b)`.  The size-five pulse vanishes.  The chamber
inequality gives

\[
 0\le c_1\le a\le2b-p<A/2,
\]

while `c_2<=b<A/2`; hence the size-one and size-two pulses are
nonnegative.

The size-four pulse is exactly

\[
                         K(p+a)-K(2b).
\]

Moreover

\[
 2p+a\le p+2b,qquad p+b+c_2\le p+2b,
\]

so

\[
                         2p+a\le V_7\le p+2b.
\]

Both endpoints lie in \([A,\infty)\), where (K) is increasing.  Therefore

\[
 K(V_7)-K(p+2b)
 \ge K(2p+a)-K(p+2b).
\]

Substitution proves (4.2). \(\square\)

## 5. Continuous three-gate reduction

The gates agree on their shared walls.  At `b=2a`,

\[
 \mathcal G_{\rm I}(p,a,2a)
 =\mathcal G_{\rm II}(p,a,2a)
 =\mathcal L_3(p;a,2a).
\tag{5.1}
\]

At `b=(p+a)/2`, one has `2b-p=a`, and both pulse differences in
`\mathcal G_{\rm III}` vanish.  Hence

\[
 \mathcal G_{\rm II}\left(p,a,{p+a\over2}\right)
 =\mathcal G_{\rm III}\left(p,a,{p+a\over2}\right).
\tag{5.2}
\]

### Theorem 5.1 (exact residual gate)

The three analytic inequalities

\[
 \mathcal G_{\rm I}>0,\qquad
 \mathcal G_{\rm II}>0,
 \qquad
 \mathcal G_{\rm III}>0
\tag{5.3}
\]

on their respective portions of (0.2)--(1.2) are sufficient to close the
complete normalized six-slot `h=3` branch.

No maximum, availability transient, or potentially adverse pulse remains
outside (5.3).  The five-pulse problem has collapsed to a continuous
three-piece scalar function of `(p,a,b)`.

## 6. Scope and dependencies

This theorem is a reduction, not a sign proof for (5.3).  It does not
close the six-slot `h=3` branch, the remaining `h=4,5` branches, complete
grid-six positivity, the all-grid Bellman inequality, or an OR-word upper
bound.

| role | file | SHA-256 |
|---|---|---|
| canonical six-slot normal forms | `MATH_THEOREM_SIX_SLOT_CANONICAL_MAXIMUM_EFFICIENCY_APERY_NORMAL_FORMS_20260804.md` | `3b537980a6f18aae936979335cc6756079ff10b92a80019acf3a97df8be9bede` |
| independent canonical-form audit | `MATH_AUDIT_SIX_SLOT_CANONICAL_MAXIMUM_EFFICIENCY_APERY_NORMAL_FORMS_INDEPENDENT_20260804.md` | `fae9fe02688d666e956619abe40698791a4146004a59a483893d0634ebbe3006` |
| compact monotonicity through `3A/4` | `MATH_THEOREM_FIVE_SLOT_TWO_EFFICIENT_SMALL_PERIOD_WEDGE_CLOSURE_20260804.md` | `a678fc5a33c6457d9d640aa963d902fdb8c7ed932ade6a14fd320caf8d285e43` |
