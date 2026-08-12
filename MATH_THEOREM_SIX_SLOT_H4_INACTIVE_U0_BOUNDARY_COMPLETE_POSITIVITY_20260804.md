# Six-slot `h=4`: complete positivity of the inactive `u=0` rectangle boundary

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical sign theorem.  It proves the
literal correlated rectangle gate strictly positive on the complete
inactive `u=0` boundary, including the subface `P=A`.  Together with the
active-`Gamma` theorem, the whole `u=0` face is closed.  It does not sign
the other inactive boundary strata.  No search or sampled computation is
used.

Put

\[
 A={\sqrt\pi\over2},
 \qquad
 \delta_*={43849\over643260},
 \qquad
 \tau_0=A+\delta_*,
\tag{0.1}
\]

and

\[
 F_\tau(w)=\sum_{q\ge0}K(q\tau+w),
 \qquad
 C(\tau)=F_\tau(0).
\tag{0.2}
\]

On `u=0`, the correlated rectangle gate is

\[
 \mathfrak R(\delta,P,0)
 =2\{C(\tau)+F_\tau(P)\}-\Gamma(\delta),
 \qquad
 {2\tau\over3}\le P\le A.
\tag{0.3}
\]

The closed active side was already proved positive.  We therefore work
on the inactive side, where

\[
                         \Gamma(\delta)={1\over20000}.
\tag{0.4}
\]

It is enough to prove a uniform positive lower bound for the brace in
(0.3).

## 1. Reduction to the first residual period

For every fixed `w`,

\[
 \partial_\tau F_\tau(w)
 =\sum_{q\ge1}qK'(q\tau+w)>0,
\tag{1.1}
\]

because all shifted terms lie on the increasing Gaussian tail.  Hence

\[
 H(\tau,P):=C(\tau)+F_\tau(P)
\tag{1.2}
\]

is strictly increasing in `tau` for fixed `P`.

If `(tau,P)` is admissible and `tau>=tau_0`, then

\[
 P\ge {2\tau\over3}\ge {2\tau_0\over3},
\]

so the same `P` is admissible at `tau_0`.  Therefore

\[
 \boxed{H(\tau,P)\ge H(\tau_0,P).}
\tag{1.3}
\]

Write

\[
 M=1-2e^{-\pi/4}>{881\over10000}.
\tag{1.4}
\]

Then

\[
 H(\tau_0,P)
 =M+K(P)-\mathcal T_0-\mathcal T_P,
\tag{1.5}
\]

where

\[
 \mathcal T_0=\sum_{q\ge1}e^{-(A+q\tau_0)^2},
 \qquad
 \mathcal T_P=\sum_{q\ge1}e^{-(A+q\tau_0+P)^2}.
\tag{1.6}
\]

## 2. The ceiling tail

The rational bounds

\[
 A>{4431\over5000},
 \qquad
 \delta_*>{1363\over20000}
\tag{2.1}
\]

follow respectively by squaring against `\pi>333/106` and by direct
cross multiplication.

The first ceiling-tail argument satisfies

\[
 A+\tau_0=2A+\delta_*
 >{36811\over20000},
\]

and therefore

\[
 (A+\tau_0)^2>{271\over80}.
\tag{2.2}
\]

The finite positive Taylor comparison

\[
 \sum_{j=0}^{12}{(271/80)^j\over j!}>{5000\over169}
\tag{2.3}
\]

gives

\[
                         e^{-(A+\tau_0)^2}<{169\over5000}.
\tag{2.4}
\]

For the remaining tail,

\[
 A+2\tau_0=3A+2\delta_*>{27949\over10000},
\]

so its first exponent exceeds `39/5`.  Direct positive Taylor
comparisons give

\[
 e^{39/5}>2400,
 \qquad
 e^{7\pi/4}>200.
\tag{2.5}
\]

The second inequality prices every successive ratio, since the squared
argument gaps from `q=2` onward are at least `7\pi/4`.  Hence

\[
 \sum_{q\ge2}e^{-(A+q\tau_0)^2}
 <{1/2400\over1-1/200}<{1\over2000}.
\]

Combining with (2.4),

\[
 \boxed{\mathcal T_0<{169\over5000}+{1\over2000}
 ={343\over10000}.}
\tag{2.6}
\]

## 3. Two compact-kernel ranges

Write `P=At`.  The admissible lower endpoint satisfies `t>7/10`.
Indeed `delta_*>A/20`, using `A<8/9` and
`delta_*>17/250>2/45`.

### Lemma 3.1 (lower range)

For

\[
 {2\tau_0\over3A}\le t\le {17\over20},
\]

one has

\[
                         \boxed{K(At)>-{51\over1000}.}
\tag{3.1}
\]

#### Proof

The ratio of the positive to the adverse term in `K'(At)/(2A)` is

\[
 r(t)={1+t\over1-t}e^{-\pi t}.
\]

On `t>=7/10`,

\[
 {d\over dt}\log r(t)
 ={2\over1-t^2}-\pi
 \ge{200\over51}-{22\over7}>0.
\]

At `t=17/20`,

\[
 r(17/20)={37\over3}e^{-17\pi/20}<1,
\]

because `17\pi/20>2669/1000` and the degree-eight positive Taylor
polynomial at `2669/1000` exceeds `37/3`.  Thus `K'<0` throughout this
range, and its minimum there is at `17A/20`.

At that endpoint,

\[
 K(17A/20)
 =1-e^{-9\pi/1600}-e^{-1369\pi/1600}.
\]

Put `x=9\pi/1600`.  The bounds on `\pi` give

\[
 {1413\over80000}<x<{1\over50},
\]

and hence

\[
 1-e^{-x}>x-{x^2\over2}
 >{99\over100}{1413\over80000}>{87\over5000}.
\tag{3.2}
\]

Also `1369\pi/1600>214933/80000`, and the degree-nine positive
Taylor polynomial at `214933/80000` exceeds `2500/171`.  Therefore

\[
 e^{-1369\pi/1600}<{171\over2500}.
\tag{3.3}
\]

Equations (3.2)--(3.3) give

\[
 K(17A/20)>{87\over5000}-{171\over2500}
 =-{51\over1000}.
\]

This proves (3.1). \(\square\)

### Lemma 3.2 (upper range)

For

\[
                         {17\over20}\le t\le1,
\]

one has

\[
                         \boxed{K(At)>-{13\over250}.}
\tag{3.4}
\]

#### Proof

Put `s=1-t`, so `0<=s<=3/20`.  The endpoints already satisfy the
claim: `s=3/20` follows from Lemma 3.1, while at `s=0`,

\[
                         K(A)=-e^{-\pi}>-{13\over250}.
\]

Consider an interior minimum.  Its critical equation is

\[
 (2-s)e^{-\pi(2-s)^2/4}
 =s e^{-\pi s^2/4}.
\tag{3.5}
\]

The quotient of the left side by the right side is

\[
 q(s)={2-s\over s}e^{-\pi(1-s)}.
\]

Its logarithmic derivative is negative on `(0,3/20]`.  At `s=3/25`,

\[
 q(3/25)={47\over3}e^{-22\pi/25}<1,
\]

because `22\pi/25>1727/625` and the degree-eight positive Taylor
polynomial there exceeds `47/3`.  Hence every critical point has
`s<3/25`.

At a critical point, (3.5) gives

\[
 K=1-{2\over2-s}e^{-\pi s^2/4}.
\tag{3.6}
\]

The subtracted expression is increasing on `[0,3/25]`, since its
logarithmic derivative is

\[
 {1\over2-s}-{\pi s\over2}>0.
\]

Finally, if `x_0=1413/125000`, then

\[
 e^{-9\pi/2500}
 <1-x_0+{x_0^2\over2}<{12361\over12500}.
\tag{3.7}
\]

Therefore (3.6) yields

\[
 {2\over2-s}e^{-\pi s^2/4}
 <{50\over47}{12361\over12500}={263\over250},
\]

and hence `K>-13/250`.  This proves (3.4). \(\square\)

## 4. Two shifted-tail ranges

The first shifted-tail argument always satisfies

\[
 A+\tau_0+P
 \ge A+{5\tau_0\over3}
 >{148607\over60000}.
\]

Its square exceeds `613/100`, and the positive Taylor polynomial gives
`e^(613/100)>450`.  Every successive exponent gap is at least

\[
                         {19\pi\over12},
\]

whose exponential exceeds `100`.  Consequently

\[
 \boxed{
 \mathcal T_P<{1/450\over1-1/100}
 ={2\over891}<{9\over4000}.}
\tag{4.1}
\]

If `t>=17/20`, the stronger first-argument bound is

\[
 A+\tau_0+P
 \ge {57A\over20}+\delta_*
 >{129691\over50000}.
\]

Its square exceeds `6727/1000`, and the positive Taylor polynomial gives
`e^(6727/1000)>810`.  With the same ratio bound,

\[
 \boxed{
 \mathcal T_P<{1/810\over1-1/100}<{1\over800}.}
\tag{4.2}
\]

## 5. Complete `u=0` positivity

### Theorem 5.1

For every admissible `tau,P` with `tau>=tau_0`,

\[
                         \boxed{C(\tau)+F_\tau(P)>{11\over20000}.}
\tag{5.1}
\]

#### Proof

Use (1.3)--(1.6) and split at `P=17A/20`.

In the lower range, Lemma 3.1 and (4.1) give

\[
 H>{881\over10000}-{343\over10000}
     -{51\over1000}-{9\over4000}
 ={11\over20000}.
\]

In the upper range, Lemma 3.2 and (4.2) give the same bound:

\[
 H>{881\over10000}-{343\over10000}
     -{13\over250}-{1\over800}
 ={11\over20000}.
\]

This proves (5.1). \(\square\)

### Corollary 5.2 (inactive `u=0` face)

On the complete inactive `u=0` boundary,

\[
 \boxed{
 \mathfrak R(\delta,P,0)>{21\over20000}>0.}
\tag{5.2}
\]

#### Proof

Use (0.3)--(0.4) and Theorem 5.1:

\[
 \mathfrak R
 =2H-{1\over20000}
 >{22\over20000}-{1\over20000}
 ={21\over20000}.
\]

This proves (5.2). \(\square\)

The subface `P=A` has `u=0` because `u<=A-P`, and is therefore closed as
well.  The active side and its switch were already closed by the active
`Gamma` theorem, so the entire `u=0` face is positive.

## 6. Exact scope

This theorem closes:

1. the whole inactive `u=0` boundary with margin `21/20000`;
2. the full `P=A` subface;
3. together with the active theorem, the complete `u=0` face.

It does not sign `u=A-P`, `u=P/4`, `P=2tau/3`, the low-branch switch,
or their intersections.

## 7. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| correlated literal rectangle | `MATH_THEOREM_SIX_SLOT_H4_LITERAL_RECTANGLE_CORRELATED_GATE_20260804.md` | `533f194ed727b2c15d26ca2007131a3bfc22f08f401097f74d021d40cf5dd5cd` |
| active-`Gamma` positivity | `MATH_THEOREM_SIX_SLOT_H4_ACTIVE_GAMMA_COMPLETE_POSITIVITY_AND_BOUNDARY_COLLAPSE_20260804.md` | `3259e9c0c8a3f74839f5ed1cf73646395b8bebb17ea871d1d7e95e74360e2953` |
| corrected upper convexity | `MATH_THEOREM_SIX_SLOT_H4_RECTANGLE_UPPER_CONVEXITY_AND_KKT_PRUNING_20260804.md` | `6f8daaba40de9d40c17d429fa4925d4d985d3374fa00d89a5d05651b2529aa11` |
| compact Gaussian bounds | `MATH_THEOREM_H4_INERT_COMPACT_GAUSSIAN_GATE_CLOSURE_20260804.md` | `f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b` |
