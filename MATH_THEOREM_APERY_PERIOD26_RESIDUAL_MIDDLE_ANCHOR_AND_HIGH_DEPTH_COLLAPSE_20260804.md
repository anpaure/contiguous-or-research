# Period twenty-six residuals: a middle anchor and collapse to depths eleven and twelve

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It closes both
authenticated period-twenty-six residual chambers whenever their reflected
ray depth is at most ten.  It leaves only depths eleven and twelve, and on
depth eleven records the exact two-point central-rail credit.  It does not
claim complete period-twenty-six positivity.  No search, solver, sampled
computation, or numerical optimization is used.

Retain

\[
A={\sqrt\pi\over2},
\qquad
f(x)=F_A(Ax),
\qquad
C=f(0),
\tag{0.1}
\]

and the exact period-twenty-six residual identities

\[
E(s)=-{1882\over1000000}+\mathcal S_6
\tag{0.2}
\]

on `R_6`, and

\[
E(s)=-{1648\over1000000}+\mathcal S_7
\tag{0.3}
\]

on `R_7`.  In both identities the discarded middle train is one
nonnegative summand of `mathcal S_j`.

## 1. A uniform middle anchor through six thirteenths

### Lemma 1.1

One has

\[
\boxed{f(x)>{1\over250}\qquad(0\le x\le6/13).}
\tag{1.1}
\]

#### Proof

Every interior critical point of `f` on `[0,1/2]` is a strict maximum.
Therefore the minimum of `f` on `[0,6/13]` occurs at one of its two
endpoints.

At zero, the frozen compact estimate gives

\[
C>{5503\over125000}>{1\over250}.
\tag{1.2}
\]

At `x=6/13`, the literal train is

\[
\begin{aligned}
f(6/13)=1
&-e^{-49\pi/676}-e^{-361\pi/676}
-e^{-256\pi/169}-e^{-2025\pi/676}\\
&-\sum_{j\ge4}e^{-\pi(j+6/13)^2/4}.
\end{aligned}
\tag{1.3}
\]

Using `pi>333/106`, finite positive Taylor lower bounds for the reciprocal
exponentials give

\[
e^{-49\pi/676}<{797\over1000},
\qquad
e^{-361\pi/676}<{47\over250},
\tag{1.4}
\]

\[
e^{-256\pi/169}<{1\over100},
\qquad
e^{-2025\pi/676}<{1\over10000}.
\tag{1.5}
\]

For transparency, it is enough to apply positive Taylor polynomials to

\[
{16317\over71656},
\quad {120213\over71656},
\quad {85248\over17914},
\quad {674325\over71656},
\]

and compare with `1000/797`, `250/47`, `100`, and `10000`, respectively.
Degrees three, seven, seven, and sixteen, respectively, already suffice.

The first omitted term has exponent greater than

\[
{280053\over17914}>15,
\]

and every successor ratio is below `1/100`.  A finite positive Taylor
bound (degree ten for the first term and degree five for the ratio) therefore
gives

\[
\sum_{j\ge4}e^{-\pi(j+6/13)^2/4}<{1\over10000}.
\tag{1.6}
\]

Substitution in (1.3) yields

\[
f(6/13)>
1-{797\over1000}-{47\over250}-{1\over100}
-{1\over10000}-{1\over10000}
={3\over625}>{1\over250}.
\tag{1.7}
\]

Together with (1.2) and the strict-maximum classification, this proves
(1.1). \(\square\)

## 2. Prefix-average placement of the first middle shift

Normalize the exact first carry by

\[
s_1=\alpha A,
\qquad
P=(1-\alpha)A.
\tag{2.1}
\]

The cyclic prefix-minimum theorem gives, for every `r`,

\[
{s_r\over A}\le {rP\over26A}
={r(1-\alpha)\over26}<{r\over26}.
\tag{2.2}
\]

At reflected depth `u`, the middle train is

\[
\mathcal M=
\sum_{r=u+2}^{25-u}f(s_r/A).
\tag{2.3}
\]

If `6<=u<=10`, its first index `r=u+2` lies between eight and twelve.
Hence (2.2) gives

\[
0<{s_{u+2}\over A}<{u+2\over26}\le {6\over13}.
\tag{2.4}
\]

Lemma 1.1 now gives the uniform literal credit

\[
\boxed{\mathcal M>{1\over250}={4000\over1000000}.}
\tag{2.5}
\]

## 3. Simultaneous closure of `R_6` and `R_7` through depth ten

Every other summand in `mathcal S_6` and `mathcal S_7` is nonnegative.
Therefore, for `6<=u<=10`, chamber `R_6` satisfies

\[
E(s)>
-{1882\over1000000}+{4000\over1000000}
={2118\over1000000}>0,
\tag{3.1}
\]

while chamber `R_7` satisfies

\[
E(s)>
-{1648\over1000000}+{4000\over1000000}
={2352\over1000000}>0.
\tag{3.2}
\]

Thus neither residual chamber survives below depth eleven.

## 4. The exact depth-eleven central rail

At `u=11`, the middle train consists exactly of

\[
\mathcal M_{11}=f(s_{13}/A)+f(s_{14}/A).
\tag{4.1}
\]

Put

\[
z={s_{13}\over A},
\qquad
w={s_{14}\over A}.
\]

Minimum-gap spacing, prefix averaging, and the definition of depth eleven
give

\[
0<z<w\le{1\over2},
\qquad
w-z\ge\alpha,
\qquad
z\le{1-\alpha\over2}.
\tag{4.2}
\]

In particular `z<=1/2-alpha`.  Both residual chambers have
`X_6>=7alpha` and `X_6<2/13`, hence

\[
\alpha<{2\over91},
\qquad
{1\over2}-\alpha>{1\over3}.
\tag{4.3}
\]

The inherited one-third anchor gives

\[
f(1/2-\alpha)<f(1/3)<{29\over750}<L<C.
\tag{4.4}
\]

Since every interior critical point of `f` is a strict maximum, the
minimum on every compact subinterval occurs at an endpoint.  At the second
endpoint, Jacobi reflection and the authenticated half-interval theta sign
and absolute bound give

\[
 2f(1/2)=g(1/2),
 \qquad 0<f(1/2)<{\varepsilon\over2}<C,
\]

Consequently

\[
\boxed{
\mathcal M_{11}
\ge
\min_{0\le t\le1/2-\alpha} f(t)
+\min_{0\le t\le1/2}f(t)
=f(1/2-\alpha)+f(1/2).}
\tag{4.5}
\]

Thus the remaining depth-eleven gates sharpen to

\[
\widehat{\mathcal S}_6
+f(1/2-\alpha)+f(1/2)
>{1882\over1000000},
\tag{4.6}
\]

or

\[
\widehat{\mathcal S}_7
+f(1/2-\alpha)+f(1/2)
>{1648\over1000000},
\tag{4.7}
\]

where `widehat mathcal S_j` is the corresponding nonnegative slack with
the middle train removed.

At `u=12`, the middle train is empty, so the exact residual gates remain
those already authenticated.

## 5. The sharpened frontier

### Theorem 5.1

Every honest exact-first-carry period-twenty-six clock is strictly positive
unless all of the following hold:

1. its overlap depth satisfies `H>=5`;
2. its reflected ray depth is `u=11` or `u=12`;
3. it lies in residual chamber `R_6` or `R_7`;
4. at depth eleven, the appropriate central-rail gate (4.6) or (4.7)
   remains unsigned; at depth twelve, the original exact residual slack
   remains unsigned.

The new ingredient is shared by both chambers: one forced middle shift
below `6/13` pays more than twice either residual debt.  The remaining
obstruction is therefore genuinely a near-half, high-depth geometry, not
an arbitrary short ray.

This theorem does not sign the depth-eleven or depth-twelve gates, prove
complete period-twenty-six positivity, treat finite shoulders, or make an
OR-word claim.

## 6. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| authenticated period-26 residual identities | `MATH_THEOREM_APERY_PERIOD26_SHARP_DEPTH_AND_TWO_RESIDUAL_THRESHOLD_CHAMBERS_20260804.md` | `15777eb5978671af4ce685f9760fc1c2a1cef25e424cafe7deda8bc004cdee2f` |
| cyclic prefix minimum and terminal average | `MATH_LEMMA_APERY_TERMINAL_SUFFIX_MAXIMUM_AND_QUARTER_CUTOFF_20260804.md` | `6ef133e15f8635db9a91fb837ef2df65fadedc6a52ff923b0b5895f215324639` |
| critical-point classification | `MATH_THEOREM_COMPLEMENTARY_PAIR_TRAIN_AND_H4_INERT_SCALAR_REDUCTION_20260804.md` | `fc8b2dee92dd3bb9afab390c8507db51fec05c6ca4e9d46ac4948c7422d042a7` |
| compact endpoint value `C>L` | `MATH_THEOREM_H4_INERT_COMPACT_GAUSSIAN_GATE_CLOSURE_20260804.md` | `f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b` |
| one-third compact anchor | `MATH_THEOREM_SIX_SLOT_H4_ACTIVE_GAMMA_COMPLETE_POSITIVITY_AND_BOUNDARY_COLLAPSE_20260804.md` | `3259e9c0c8a3f74839f5ed1cf73646395b8bebb17ea871d1d7e95e74360e2953` |
| theta sign and absolute bound | `MATH_LEMMA_THETA_HALF_INTERVAL_MONOTONICITY_AND_HALF_ROOT_SUMS_20260804.md` | `f974aeda114df4c933a396c06de51596bccd2fea18066412d45f7a18df62a0e3` |
