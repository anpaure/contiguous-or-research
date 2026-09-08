# Six-slot `h=4`: upper-band convexity and elimination of the first rectangle KKT branch

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves strict
convexity of every periodized train on the complete upper band used by the
literal rectangle gate.  Consequently the constant-low smooth KKT branch
has no interior point.  Every remaining smooth interior obstruction lies
on the moving-low branch, on the active `Gamma` side, and obeys one signed
three-train stationarity system.  The last period-residual equation is not
excluded here, so complete `h=4` positivity is not claimed.  No
computation or search is used.

Put

\[
 A={\sqrt\pi\over2},
 \qquad
 F_\tau(w)=\sum_{q\ge0}K(q\tau+w),
\tag{0.1}
\]

and

\[
 T_\tau(w)=F_\tau'(w),
 \qquad
 R_\tau(w)=\partial_\tau F_\tau(w).
\tag{0.2}
\]

The correlated rectangle gate has

\[
 A\le\tau\le {3A\over2},
 \qquad
 {2\tau\over3}\le P\le A,
 \qquad
 0\le u\le\min\{A-P,P/4\}.
\tag{0.3}
\]

Its two smooth low branches are

\[
 \mathrm C:\quad F_\tau(u)\ge C(\tau),
 \qquad
 \mathrm U:\quad F_\tau(u)\le C(\tau).
\tag{0.4}
\]

## 1. A uniform upper-band curvature bound

Write

\[
                         h(r)=re^{-r^2}.
\tag{1.1}
\]

For `0<=w<=A`, direct differentiation gives

\[
 {1\over2}F_\tau''(w)
 =h'(A-w)+h'(A+w)
  +\sum_{q\ge1}h'(A+q\tau+w),
\tag{1.2}
\]

where

\[
                         h'(r)=(1-2r^2)e^{-r^2}.
\tag{1.3}
\]

### Lemma 1.1 (near reflection)

If `2tau/3<=w<=A`, then

\[
                         \boxed{h'(A-w)>{3\over4}.}
\tag{1.4}
\]

#### Proof

Here `0<=A-w<=A/3`.  Since

\[
 h''(r)=2r(2r^2-3)e^{-r^2}<0
 \qquad(0<r\le A/3),
\]

the minimum is at `r=A/3`.  The exact Gaussian estimate

\[
 e^{-\pi/36}>{9163\over10000}>{115\over126}
\]

and `pi<22/7` give

\[
 h'(A/3)
 =\left(1-{\pi\over18}\right)e^{-\pi/36}
 >{52\over63}{115\over126}
 ={5980\over7938}>{3\over4}.
\]

This proves (1.4). \(\square\)

### Lemma 1.2 (far compact reflection)

On the same band,

\[
                         \boxed{h'(A+w)>-{2\over5}.}
\tag{1.5}
\]

#### Proof

Now `A+w>=5A/3`.  The function

\[
                         (2r^2-1)e^{-r^2}
\]

is decreasing for `r^2>=3/2`; hence the worst point is `r=5A/3`.
The authenticated bound

\[
                         e^{-25\pi/36}<{23\over200}
\]

and `pi<22/7` give

\[
 (2(5A/3)^2-1)e^{-(5A/3)^2}
 <{212\over63}{23\over200}<{2\over5}.
\]

Since `h'` is the negative of this quantity, (1.5) follows. \(\square\)

### Lemma 1.3 (complete period tail)

Uniformly on (0.3),

\[
 \boxed{
 \sum_{q\ge1}h'(A+q\tau+w)>-{1\over25}.}
\tag{1.6}
\]

#### Proof

All terms are negative.  The first argument satisfies

\[
 A+\tau+w\ge A+{5\tau\over3}\ge {8A\over3}.
\]

At `r_0=8A/3`,

\[
 2r_0^2-1={32\pi\over9}-1<{641\over63}.
\]

Also `pi>333/106` gives

\[
 {16\pi\over9}>{296\over53},
\]

and the positive exponential series gives

\[
                         e^{296/53}>260.
\]

Thus the first adverse magnitude is smaller than

\[
                         {641\over63\cdot260}.
\tag{1.7}
\]

It remains to control successive ratios.  Put `t=tau/A`.  If
`1<=t<=6/5`, then

\[
 {\tau\over r}\le {2\over5},
 \qquad
 r^2>{16\over3},
\]

so

\[
 {2(r+\tau)^2-1\over2r^2-1}
 <{49\over25}{32\over29}<{11\over5}.
\tag{1.8}
\]

If `6/5<t<=3/2`, then

\[
 {\tau\over r}\le {3\over7},
 \qquad
 r^2>{9\pi\over4}>{2997\over424},
\]

and therefore

\[
 {2(r+\tau)^2-1\over2r^2-1}
 <{100\over49}{2997\over2785}<{11\over5}.
\tag{1.9}
\]

The exponent gap satisfies

\[
 (r+\tau)^2-r^2
 =2r\tau+\tau^2
 \ge {19\pi\over12}>{19\over4}.
\]

The positive exponential series gives `e^(19/4)>110`.  Hence every
successive adverse magnitude is less than `1/50` of its predecessor.
Equations (1.7)--(1.9) yield

\[
 -\sum_{q\ge1}h'(A+q\tau+w)
 <{641\over63\cdot260}{1\over1-1/50}<{1\over25}.
\]

This proves (1.6). \(\square\)

### Theorem 1.4 (strict upper-band convexity)

For every `tau` in `[A,3A/2]`,

\[
 \boxed{
 F_\tau''(w)>{31\over50}>0
 \qquad(2\tau/3\le w\le A).}
\tag{1.10}
\]

In particular, `T_tau` is strictly increasing on this complete band and
has at most one zero there.

#### Proof

Add Lemmas 1.1--1.3 in (1.2):

\[
 {1\over2}F_\tau''(w)
 >{3\over4}-{2\over5}-{1\over25}
 ={31\over100}.
\]

Multiply by two. \(\square\)

## 2. Elimination of branch `C`

The correlated rectangle theorem proves that an interior stationary point
on branch `C` must satisfy

\[
 T_\tau(P)=0,
 \qquad
 T_\tau(P+u)=0.
\tag{2.1}
\]

### Theorem 2.1

Branch `C` has no smooth interior stationary point.

#### Proof

At an interior point, `u>0`, so

\[
 {2\tau\over3}<P<P+u<A.
\]

Both shifts lie in the strict-convexity band.  Theorem 1.4 makes
`T_tau` strictly increasing, so it cannot vanish at both distinct shifts.
This contradicts (2.1). \(\square\)

Thus every minimum on branch `C` lies on the finite boundary/switch list
already recorded by the rectangle theorem.

## 3. The unique possible smooth interior pattern

On branch `U`, the two shift equations are

\[
 T_\tau(P)+T_\tau(P+u)=0,
 \qquad
 T_\tau(u)+T_\tau(P+u)=0.
\tag{3.1}
\]

### Theorem 3.1 (signed three-train stationarity)

Every smooth interior stationary point of the complete rectangle gate
must lie on branch `U`, must have active `Gamma`, and must satisfy

\[
\boxed{
 T_\tau(P)=T_\tau(u)=-T_\tau(P+u)<0,}
\tag{3.2}
\]

together with

\[
\boxed{
 R_\tau(0)+R_\tau(u)+R_\tau(P)+R_\tau(P+u)
 =-{1\over2}T_A((A-\delta)/2).}
\tag{3.3}
\]

#### Proof

Theorem 2.1 removes branch `C`.  On branch `U`, equation (3.1) gives

\[
                         T_\tau(P)=T_\tau(u).
\]

Because `u>0`, one has `P+u>P`.  Strict increase of `T_tau` on the upper
band gives

\[
                         T_\tau(P+u)>T_\tau(P).
\]

Their sum is zero, so their only possible sign order is

\[
                         T_\tau(P)<0<T_\tau(P+u),
\]

which is exactly the orientation displayed in (3.2).

Every term `R_tau(w)` is strictly positive.  Therefore the outer period
equation cannot hold on the inactive `Gamma` branch, where `Gamma'=0`.
On the active branch,

\[
 \Gamma'(\delta)=-{1\over2}T_A((A-\delta)/2),
\]

and the outer equation is exactly (3.3). \(\square\)

Equation (3.3) is now the sole smooth interior obstruction.  It is a
four-train positive period residual equated to one compact threshold
slope.  This is the precise analogue of the final Chamber-II residual
before shift-stationarity subtraction.

## 4. Exact scope

The theorem proves:

1. a uniform strict curvature margin `31/50` on the entire physical upper
   band;
2. complete removal of the constant-low smooth interior branch;
3. removal of every moving-low interior point on the inactive `Gamma`
   side;
4. reduction of all remaining smooth interior points to the signed system
   (3.2)--(3.3).

It does not eliminate boundary/switch minima or prove that (3.2)--(3.3)
is empty.  Hence it does not yet close the rectangle gate or six-slot
`h=4` positivity.

## 5. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| corrected literal rectangle gate | `MATH_THEOREM_SIX_SLOT_H4_LITERAL_RECTANGLE_CORRELATED_GATE_20260804.md` | `533f194ed727b2c15d26ca2007131a3bfc22f08f401097f74d021d40cf5dd5cd` |
| compact Gaussian bound `e^{-25pi/36}<23/200` | `MATH_THEOREM_SIX_SLOT_TWO_EFFICIENT_COMPLETE_THREE_COMPACT_ROW_CLOSURE_20260804.md` | `53a65d72f9f6a22ccef91f43c5759c61fc0a0ea831294b71b56a46d1cae95d3a` |
| Gaussian and half-band train bounds | `MATH_THEOREM_H4_INERT_COMPACT_GAUSSIAN_GATE_CLOSURE_20260804.md` | `f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b` |
