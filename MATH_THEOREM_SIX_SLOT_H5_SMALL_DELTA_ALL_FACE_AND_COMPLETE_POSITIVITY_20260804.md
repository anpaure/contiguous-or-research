# Six-slot `h=5`: all-face small-excess closure and complete positivity

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical sign theorem.  It strengthens
the face-`Z` argument to the entire compact union of the three inert
endpoint faces.  Together with the frozen threshold and large-excess
theorems, it proves complete positivity of the canonical six-slot
least-maximum-density branch `h=5`.  No search or sampled computation is
used.

Put

\[
 A={\sqrt\pi\over2},
 \qquad F(w)=F_A(w),
 \qquad C=F(0),
 \qquad \varepsilon={1\over20000}.
\tag{0.1}
\]

Use the reflected coordinates

\[
 (c_1,c_2,c_3,c_4,c_5)=(x,y,A-m,A-v,A-u).
\tag{0.2}
\]

The exact compact physical polytope satisfies

\[
 0\le u<{A\over6},
 \qquad 0\le x\le {A\over5},
 \qquad 0\le y\le {2A\over5},
\tag{0.3}
\]

\[
 v\ge {A+4u\over5},
 \qquad A-2m\le\delta,
 \qquad 0<\delta<{A\over15}.
\tag{0.4}
\]

No endpoint equality is fixed: one only assumes the physical saturation

\[
 \max\{x-u,y-v,A-2m\}=\delta.
\tag{0.5}
\]

The compact train is

\[
 T_5=C-F(u)+F(x)-F(v)+F(y)-F(m).
\tag{0.6}
\]

The exact endpoint-period expression is

\[
 \mathscr E_5
 =T_5+\sum_{j=1}^{6}D_j
 +\Theta(u)+\Theta(v)+\Theta(m),
\tag{0.7}
\]

where every period gain `D_j` is nonnegative and

\[
                         \Theta(w)>-\varepsilon
 \qquad(0\le w\le A).
\tag{0.8}
\]

## 1. The third ray is uniformly positive on all three faces

The endpoint inequality in (0.4) gives

\[
 m\ge {A-\delta\over2}>{7A\over15}.
\tag{1.1}
\]

The previously frozen point anchors are

\[
 F(2A/5)>{18879\over1000000},
 \qquad
 F(7A/15)<{7121\over1000000}.
\tag{1.2}
\]

The period-uniform no-interior-minimum theorem on `[0,2A/5]`, together
with `F(2A/5)<C`, gives

\[
                         F(y)\ge F(2A/5).
\tag{1.3}
\]

If `m<=A/2`, strict decrease from `4A/25` and (1.1) give

\[
 F(m)\le F(7A/15)<{7121\over1000000}.
\]

If instead `m>A/2`, then `0<=A-m<A/2`; positivity on the lower half and
Jacobi reflection give

\[
 F(m)=\Theta(m)-F(A-m)<\varepsilon
 <{7121\over1000000}.
\]

Thus, on **every** endpoint face,

\[
\boxed{
 F(y)-F(m)>{11758\over1000000}.}
\tag{1.4}
\]

This is the key globalization: equality `A-2m=delta` is unnecessary.

## 2. The first two rays

The quarter anchor and the no-interior-minimum theorem give

\[
                         F(x)\ge C
 \qquad(0\le x\le A/5).
\tag{2.1}
\]

Hence

\[
 C-F(u)+F(x)-F(v)\ge2C-F(u)-F(v).
\tag{2.2}
\]

Retain

\[
 C>{44024\over1000000},
\tag{2.3}
\]

and the frozen compact prices

\[
 F(u)<{49000\over1000000}\quad(0\le u\le A/32),
\tag{2.4}
\]

\[
 F(u)<{51000\over1000000}\quad(0\le u\le A/16),
\tag{2.5}
\]

\[
 F(u)<{53300\over1000000}quad(0\le u\le A/2),
\tag{2.6}
\]

together with

\[
 F(A/5)<{49730\over1000000},
 \quad
 F(9A/40)<{48000\over1000000},
 \quad
 F(A/4)<{45160\over1000000}.
\tag{2.7}
\]

Whenever a lower bound `v>=b` in (2.7) has `v<=A/2`, monotonicity gives
`F(v)<=F(b)`.  If `v>A/2`, reflection and lower-half positivity instead
give

\[
                         F(v)<\varepsilon,
\tag{2.8}
\]

which is stronger than every price in (2.7).  Thus none of the following
cases requires `v<=A/2`.

### Case I: `0<=u<=A/32`

Here `v>=A/5`.  Equations (2.2)--(2.4) and (2.7)--(2.8) give

\[
 C-F(u)+F(x)-F(v)>-{10682\over1000000}.
\tag{2.9}
\]

### Case II: `A/32<=u<=A/16`

Now

\[
 v\ge {A+4(A/32)\over5}={9A\over40},
\]

and

\[
 C-F(u)+F(x)-F(v)>-{10952\over1000000}.
\tag{2.10}
\]

### Case III: `A/16<=u<A/6`

Here `v>=A/4`, and

\[
 C-F(u)+F(x)-F(v)>-{10412\over1000000}.
\tag{2.11}
\]

These are exactly the rational subtractions

\[
 88048-49000-49730=-10682,
\]

\[
 88048-51000-48000=-10952,
\]

\[
 88048-53300-45160=-10412.
\]

## 3. Complete small-excess closure

All six period gains in (0.7) are nonnegative.  Without using any theta
sign, (0.8) prices the three reflection errors by `3epsilon=150/10^6`.
Combining (1.4) with Cases I--III yields respectively

\[
 \mathscr E_5>{11758-10682-150\over1000000}
 ={926\over1000000},
\tag{3.1}
\]

\[
 \mathscr E_5>{11758-10952-150\over1000000}
 ={656\over1000000},
\tag{3.2}
\]

and

\[
 \mathscr E_5>{11758-10412-150\over1000000}
 ={1196\over1000000}.
\tag{3.3}
\]

### Theorem 3.1 (all-face small-excess closure)

Every point of the compact physical `h=5` endpoint-face union with

\[
                         0<\delta<{A\over15}
\]

has strictly positive Bellman functional.  Uniformly,

\[
                         \boxed{\Phi>{656\over1000000}.}
\tag{3.4}
\]

### Proof

The endpoint-period theorem gives `Phi>=mathscr E_5`.  The three cases
cover the full possible `u` interval, and (3.2) is the smallest margin.
No use was made of which one of the three equalities in (0.5) is active.
\(\square\)

## 4. Complete `h=5` theorem

### Theorem 4.1

Every canonical first-crossing, endpoint-saturated six-slot table assigned
to the least maximum-density branch `h=5` has strictly positive Bellman
functional.

### Proof

There are three ranges:

1. `delta=0`: the frozen threshold theorem gives
   `Phi>163/70000`;
2. `0<delta<A/15`: Theorem 3.1 gives
   `Phi>656/1000000`;
3. `A/15<=delta<A/5`: the frozen large-excess theorem gives
   `Phi>59573/132500000`.

These exhaust the exact endpoint normalization of the canonical `h=5`
branch.  \(\square\)

## 5. Exact scope

This theorem proves complete positivity of the canonical six-slot
`h=5` branch.  It does not by itself prove complete six-slot positivity
unless all other least-density branches are separately cited; nor does it
prove an arbitrary-grid Bellman theorem, a general Apéry theorem, or an
OR-word result.

## 6. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| exact reflected `h=5` polytope and decomposition | `MATH_THEOREM_SIX_SLOT_H5_REFLECTED_THREE_RAY_SCALAR_GATE_20260804.md` | `2f26836e6c46974153136e45247ae10c3f5ff44a8bd9f55d60e511b98d091aef` |
| large-excess closure and two-fifths anchor | `MATH_THEOREM_SIX_SLOT_H5_NESTED_RAY_TRANSPORT_AND_LARGE_DELTA_CLOSURE_20260804.md` | `34dfb968b14876fdd190183eef29723475ca2c6c537faac8b807c641dd4fba1a` |
| local compact bounds and new point anchors | `MATH_THEOREM_SIX_SLOT_H5_FACE_Z_SMALL_DELTA_COMPLETE_POSITIVITY_20260804.md` | `5b9fc5880b0b8717036b744c2639928cfd84d27f57d0b4d5aca125afec0243d5` |
| exact threshold theorem | `MATH_THEOREM_SIX_SLOT_H5_ENDPOINT_DEFECT_POLYTOPE_AND_CORRELATED_GATE_20260804.md` | `4a751598067165d88cd1e01e0406c3dce09c941cbba7fa0dd95487d0ff3e4b59` |
| no-interior-minimum theorem | `MATH_THEOREM_SIX_SLOT_H4_REDUNDANT_ENDPOINT_THREE_BLOCK_SCALAR_KKT_REDUCTION_20260804.md` | `f410d86f5d544755c08f269ece1d47910f2d3c055be91c7a391bb548090f53d3` |
| quarter anchor | `MATH_THEOREM_H4_INERT_COMPACT_GAUSSIAN_GATE_CLOSURE_20260804.md` | `f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b` |
