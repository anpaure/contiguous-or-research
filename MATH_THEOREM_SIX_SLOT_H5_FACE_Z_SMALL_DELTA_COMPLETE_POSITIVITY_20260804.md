# Six-slot `h=5`: complete positivity of face `Z`

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical sign theorem.  It closes the
entire repeated-middle endpoint face `Z` in the canonical inert `h=5`
branch.  The only interval not covered by the preceding large-excess
theorem is `0<delta<A/15`.  On that interval, exact face geometry turns
the third compact ray into a fixed positive bank, while three elementary
subinterval bounds in the smallest reflected coordinate control the first
two rays.  No search or sampled computation is used.

Put

\[
 A={\sqrt\pi\over2},
 \qquad F(w)=F_A(w),
 \qquad C=F(0),
 \qquad \Theta(w)=F(w)+F(A-w),
\tag{0.1}
\]

and retain the authenticated constants

\[
 L={5503\over125000},
 \qquad G={533\over10000},
 \qquad V_5={4973\over100000},
 \qquad Q={1129\over25000},
 \qquad \varepsilon={1\over20000}.
\tag{0.2}
\]

Thus

\[
 C>L,
 \qquad F(w)<G\quad(0\le w\le A/2),
 \qquad F(A/5)<V_5,
 \qquad C<F(A/4)<Q,
\tag{0.3}
\]

\[
 F'(w)<0\quad(4A/25\le w\le A/2),
 \qquad |\Theta(w)|<\varepsilon\quad(0\le w\le A),
\tag{0.4}
\]

and

\[
 \Theta(w)>0\qquad(A/4\le w\le A/2).
\tag{0.5}
\]

We also use the period-uniform fact that `F` has no interior local
minimum on `[0,A/2]`.  In particular, the minimum on every compact
subinterval is attained at an endpoint.  Finally, the already frozen
two-fifths anchor is

\[
 {18879\over1000000}<F(2A/5)<{107\over5000}<C.
\tag{0.6}
\]

## 1. Two local compact bounds near zero

Write

\[
 f(t)=F(At).
\]

Jacobi completion gives, for `0<=t<=1/2`,

\[
 f(t)=1-\vartheta(t)+H(t)+R(t),
\tag{1.1}
\]

where

\[
 H(t)=e^{-\pi t^2/4}+e^{-\pi(2-t)^2/4},
 \qquad
 R(t)=\sum_{j\ge3}e^{-\pi(j-t)^2/4},
\tag{1.2}
\]

and `|vartheta(t)-2|<epsilon`.

### Lemma 1.1

\[
 \boxed{F(w)<{49\over1000}\qquad(0\le w\le A/32),}
\tag{1.3}
\]

and

\[
 \boxed{F(w)<{51\over1000}\qquad(0\le w\le A/16).}
\tag{1.4}
\]

### Proof

The function `H` is increasing on `[0,1/16]`.  Indeed, `H'(t)>0` is
equivalent to

\[
 {2-t\over t}>e^{\pi(1-t)}.
\tag{1.5}
\]

The logarithm of the quotient of the two sides has derivative

\[
 \pi-{2\over t(2-t)}<0
 \qquad(0<t\le1/16),
\]

and (1.5) holds at `t=1/16`, since its left side is `31` while the
right side is below `e^3<31`.  Every summand of `R` is also increasing
on this interval.

At `t=1/32`, positive Taylor-polynomial comparisons, using
`333/106<pi`, give

\[
 e^{-\pi/4096}<{9993\over10000},
 \qquad
 e^{-3969\pi/4096}<{6\over125},
 \qquad
 e^{-9025\pi/4096}<{99\over100000}.
\tag{1.6}
\]

The ratio of every consecutive term in `R` is below `1/200`; it is
enough to check the first ratio, whose exponent gap is `111*pi/64`.
Consequently

\[
 R(1/32)<{99/100000\over1-1/200}<{1\over1000}.
\tag{1.7}
\]

Equations (1.1), (1.6), (1.7), and
`1-vartheta< -1+epsilon` give

\[
 f(t)<{9993\over10000}+{6\over125}+{1\over1000}
       -1+{1\over20000}
     ={967\over20000}<{49\over1000}
\]

for `0<=t<=1/32`.

At `t=1/16`, the corresponding exact comparisons are

\[
 e^{-\pi/1024}<{99695\over100000},
 \qquad
 e^{-961\pi/1024}<{21\over400},
 \qquad
 e^{-2209\pi/1024}<{23\over20000}.
\tag{1.8}
\]

Now the first tail-ratio exponent gap is `55*pi/32`, and the same
positive-polynomial check makes every ratio smaller than `1/200`.
Hence

\[
 R(1/16)<{23/20000\over1-1/200}<{29\over25000}.
\tag{1.9}
\]

Therefore, for `0<=t<=1/16`,

\[
 f(t)<{99695\over100000}+{21\over400}+{29\over25000}
       -1+{1\over20000}
     ={2533\over50000}<{51\over1000}.
\]

All exponential comparisons in (1.6)--(1.9) are finite rational
certificates: after substituting `pi>333/106`, the positive Taylor sums
of degrees respectively `1,8,15,8` and `1,9,14,9` exceed the required
reciprocals.  This proves the lemma.  \(\square\)

## 2. Two new fixed anchors

For `0<z<25`, put

\[
 U_{24}(z)=\sum_{j=0}^{23}{z^j\over j!}
 +{z^{24}\over24!(1-z/25)}.
\tag{2.1}
\]

Then `e^z<U_24(z)`.

### Lemma 2.1

\[
 \boxed{F(9A/40)<{48\over1000}.}
\tag{2.2}
\]

### Proof

The first four adverse Gaussian exponents are

\[
 {961\pi\over6400},
 \qquad {2401\pi\over6400},
 \qquad {7921\pi\over6400},
 \qquad {16641\pi\over6400}.
\tag{2.3}
\]

Using `pi<355/113`, direct positive-denominator substitution in
`U_24` gives the strict lower bounds

\[
 {6238\over10000},
 \qquad {3076\over10000},
 \qquad {204\over10000},
 \qquad {27\over100000}.
\tag{2.4}
\]

Their sum is `95207/100000`.  Discarding the remaining adverse tail,

\[
 F(9A/40)<1-{95207\over100000}
 ={4793\over100000}<{48\over1000}.
\]

\(\square\)

### Lemma 2.2

\[
 \boxed{F(7A/15)<{7121\over1000000}.}
\tag{2.5}
\]

### Proof

The first four adverse Gaussian exponents are

\[
 {16\pi\over225},
 \qquad {121\pi\over225},
 \qquad {1369\pi\over900},
 \qquad {676\pi\over225}.
\tag{2.6}
\]

The same `U_24` comparison gives strict lower bounds

\[
 {799790\over1000000},
 \qquad {184610\over1000000},
 \qquad {8400\over1000000},
 \qquad {79\over1000000}.
\tag{2.7}
\]

They sum to `992879/1000000`.  Hence

\[
 F(7A/15)<1-{992879\over1000000}
 ={7121\over1000000}.
\]

\(\square\)

## 3. Exact geometry on face `Z`

Use the reflected physical coordinates

\[
 (c_1,c_2,c_3,c_4,c_5)=(x,y,A-m,A-v,A-u).
\tag{3.1}
\]

The compact train is

\[
 \boxed{
 T_5=C-F(u)+F(x)-F(v)+F(y)-F(m).}
\tag{3.2}
\]

On face `Z`,

\[
 m={A-\delta\over2}.
\tag{3.3}
\]

Assume for the rest of the proof that

\[
 0<\delta<{A\over15}.
\tag{3.4}
\]

Then the exact physical inequalities give

\[
 {7A\over15}<m<{A\over2},
 \qquad v\le m-x\le m<{A\over2},
\tag{3.5}
\]

\[
 0\le u<{A\over6},
 \qquad 0\le x\le {A\over5},
 \qquad 0\le y\le {2A\over5},
 \qquad v\ge {A+4u\over5}.
\tag{3.6}
\]

The no-interior-minimum theorem on `[0,A/4]`, together with
`F(A/4)>C`, yields

\[
                         F(x)\ge C.
\tag{3.7}
\]

Similarly, on `[0,2A/5]` its two endpoint values are `C` and
`F(2A/5)<C`; hence

\[
                         F(y)\ge F(2A/5).
\tag{3.8}
\]

Finally, strict decrease on `[4A/25,A/2]`, (3.5), Lemma 2.2, and
(0.6) give the fixed third-ray bank

\[
\boxed{
 F(y)-F(m)
 >{18879-7121\over1000000}
 ={11758\over1000000}.}
\tag{3.9}
\]

Also `Theta(m)>0` by (0.5).

## 4. Three intervals in the smallest reflected coordinate

The exact reflected decomposition writes the literal endpoint expression
as

\[
 \mathscr E_5
 =T_5+\sum_{j=1}^{6}D_j
  +\Theta(u)+\Theta(v)+\Theta(m),
\tag{4.1}
\]

where the six period gains `D_j` are nonnegative.  It therefore suffices
to sign the compact train plus the three theta terms.

By (3.7), the first two compact rays satisfy

\[
 C-F(u)+F(x)-F(v)\ge2C-F(u)-F(v).
\tag{4.2}
\]

We now split only according to `u`.

### Case I: `0<=u<=A/32`

Lemma 1.1 gives `F(u)<49000/1000000`.  Since `v>=A/5` and
`v<A/2`, monotonicity and (0.3) give

\[
 F(v)\le F(A/5)<{49730\over1000000}.
\]

Hence

\[
 2C-F(u)-F(v)
 >{88048-49000-49730\over1000000}
 =-{10682\over1000000}.
\tag{4.3}
\]

The midpoint theta term is positive, while the other two theta terms
are each larger than `-epsilon`.  Combining (3.9) and (4.3),

\[
 \mathscr E_5
 >{11758-10682-100\over1000000}
 ={976\over1000000}>0.
\tag{4.4}
\]

### Case II: `A/32<=u<=A/16`

Now Lemma 1.1 gives `F(u)<51000/1000000`, while

\[
 v\ge {A+4(A/32)\over5}={9A\over40}.
\]

By monotonicity and Lemma 2.1,

\[
 F(v)\le F(9A/40)<{48000\over1000000}.
\]

Therefore

\[
 2C-F(u)-F(v)
 >{88048-51000-48000\over1000000}
 =-{10952\over1000000}.
\tag{4.5}
\]

Again only two theta terms can be negative.  Thus

\[
 \mathscr E_5
 >{11758-10952-100\over1000000}
 ={706\over1000000}>0.
\tag{4.6}
\]

### Case III: `A/16<=u<A/6`

The global compact price gives

\[
 F(u)<G={53300\over1000000}.
\]

Here

\[
 v\ge {A+4(A/16)\over5}={A\over4}.
\]

Thus monotonicity and (0.3) give

\[
 F(v)\le F(A/4)<Q={45160\over1000000}.
\]

It follows that

\[
 2C-F(u)-F(v)
 >{88048-53300-45160\over1000000}
 =-{10412\over1000000}.
\tag{4.7}
\]

Both `Theta(v)` and `Theta(m)` are positive; only `Theta(u)` can cost
`epsilon`.  Hence

\[
 \mathscr E_5
 >{11758-10412-50\over1000000}
 ={1296\over1000000}>0.
\tag{4.8}
\]

## 5. Complete face theorem

### Theorem 5.1 (small-excess face `Z`)

Every canonical inert size-five-efficient six-slot table on face `Z`
with

\[
                         0<\delta<{A\over15}
\]

has strictly positive Bellman functional.  Uniformly on this open face,

\[
                         \boxed{\Phi>{706\over1000000}.}
\tag{5.1}
\]

### Proof

The endpoint-period comparison gives `Phi>=mathscr E_5`.  Cases I--III
cover the full interval `0<=u<A/6`; their smallest lower margin is the
Case-II value in (4.6).  \(\square\)

### Corollary 5.2 (complete repeated-middle face)

The entire physical face `Z` is strictly positive.  Indeed:

* the threshold `delta=0` is already positive;
* Theorem 5.1 covers `0<delta<A/15`;
* the frozen large-excess theorem covers `A/15<=delta<A/5`.

Thus the repeated-middle endpoint face contributes no zero or negative
point to the unsigned `Gamma_5` gate.

## 6. Exact scope

This theorem closes one of the three endpoint faces of the compact
reflected `h=5` chamber.  It does **not** close faces `X` or `Y`, their
interior union, the full unsigned `Gamma_5`, any larger grid size, or an
OR-word construction.

## 7. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| exact reflected `h=5` polytope and face `Z` | `MATH_THEOREM_SIX_SLOT_H5_REFLECTED_THREE_RAY_SCALAR_GATE_20260804.md` | `2f26836e6c46974153136e45247ae10c3f5ff44a8bd9f55d60e511b98d091aef` |
| nested-ray train and large-excess closure | `MATH_THEOREM_SIX_SLOT_H5_NESTED_RAY_TRANSPORT_AND_LARGE_DELTA_CLOSURE_20260804.md` | `34dfb968b14876fdd190183eef29723475ca2c6c537faac8b807c641dd4fba1a` |
| global compact price, monotonicity, one-fifth anchor | `MATH_THEOREM_APERY_PERIOD25_SHARP_GLOBAL_PRICE_AND_THRESHOLD_RAY_COMPLETE_POSITIVITY_20260804.md` | `61265fdf0e355aae0c6c786f9725ee639a427a1efb866fa21191ccb7b575653a` |
| no-interior-minimum theorem | `MATH_THEOREM_SIX_SLOT_H4_REDUNDANT_ENDPOINT_THREE_BLOCK_SCALAR_KKT_REDUCTION_20260804.md` | `f410d86f5d544755c08f269ece1d47910f2d3c055be91c7a391bb548090f53d3` |
| quarter anchor | `MATH_THEOREM_H4_INERT_COMPACT_GAUSSIAN_GATE_CLOSURE_20260804.md` | `f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b` |
| theta positivity on the upper half interval | `MATH_LEMMA_THETA_HALF_INTERVAL_MONOTONICITY_AND_HALF_ROOT_SUMS_20260804.md` | `f974aeda114df4c933a396c06de51596bccd2fea18066412d45f7a18df62a0e3` |
