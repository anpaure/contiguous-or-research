# Six-slot `h=4`: a certified outer-gate interval, endpoint obstruction, and the residual KKT locus

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical sign theorem and exact residual
reduction.  It proves both scalar gates left by the redundant-endpoint
reduction on an explicit initial interval, proves that both relaxed gates
are strictly negative at the opposite endpoint, and isolates every
remaining smooth, boundary, and nonsmooth KKT branch.  Consequently the
two relaxed gates cannot close the complete six-slot `h=4` branch.  No
search or sampled numerical estimate is used.

Put

\[
 A={\sqrt\pi\over2},
 \qquad
 F_\tau(w)=\sum_{q\ge0}K(q\tau+w),
 \qquad C(\tau)=F_\tau(0),
\tag{0.1}
\]

and write `F=F_A`, `C=C(A)`.  The preceding exact reduction defines, for

\[
 0\le\delta\le {A\over2},
 \qquad \tau=A+\delta,
 \qquad B_\delta={A-2\delta\over3},
\tag{0.2}
\]

\[
 \mathcal H(\delta)
 =\min_{0\le b\le B_\delta}
 \left[C(\tau)+F_\tau(b+\delta)+F_\tau(A-b)\right],
\tag{0.3}
\]

\[
 \mathcal I(\delta)
 =\min_{0\le b\le A/3}
 \left[F_\tau(A-b)
 +\min\{C(\tau),F_\tau(m_\delta(b))\}\right],
\quad
 m_\delta(b)=\min\{A/2,b+\delta\},
\tag{0.4}
\]

and

\[
 \mathcal S(\delta)=\min_{0\le w\le\tau/2}F_\tau(w).
\tag{0.5}
\]

The two gates are

\[
 \mathfrak G_{XY}=\mathcal H+\mathcal I+\mathcal S,
 \qquad
 \mathfrak G_Z=C(\tau/2)+2\mathcal I.
\tag{0.6}
\]

The physical inert range is `0<delta<A/2`.

## 1. A full-half compact slope bound

The five-slot compact theorem proves

\[
 0<-K'(w)<{3\over10}
 \qquad(A/4\le w\le A/2).
\tag{1.1}
\]

The same estimate in fact holds on the omitted first quarter.

### Lemma 1.1

For every `0<=w<=A/2`,

\[
 \boxed{0\le-K'(w)<{3\over10},}
\tag{1.2}
\]

with strict positivity when `0<w<=A/2`.

Consequently, if `0<=s<=t<=A/2`, then

\[
 \boxed{
 F(s)-F(t)\le {3(t-s)\over10},
 \qquad
 F(s)-F(t)<{61\over1000}.}
\tag{1.3}
\]

Equivalently, the minimum of the two displayed upper bounds is a weak
upper bound; the displacement bound is strict whenever `s<t`.

#### Proof

It remains only to treat `0<=w<=A/4`.  Put `t=w/A`.  The exact
factorization used in the five-slot proof is

\[
 {-K'(At)\over2A}
 =\left(e^{-A^2(1-t)^2}+e^{-A^2(1+t)^2}\right)
   \left(\tanh {\pi t\over2}-t\right).
\tag{1.4}
\]

The first factor is `1-K(At)<1`.  Nonnegativity follows from
`arctanh(t)<=4t/3<=pi t/2` on `0<=t<=1/2`; the final comparison is strict
for `t>0`, so equality occurs only at `t=0`.
On `0<=t<=1/4`,

\[
 \tanh {\pi t\over2}-t
 <\left({\pi\over2}-1\right)t
 <{4\over7}{1\over4}={1\over7}<{1\over6}.
\tag{1.5}
\]

Since `A<8/9`, (1.4) gives

\[
 -K'(At)<{2A\over6}<{8\over27}<{3\over10}.
\]

Together with (1.1), this proves (1.2).

For `q>=1`, the argument `qA+w` lies on the increasing Gaussian-tail
branch, so its derivative is positive.  Hence, whenever `F'(w)<0`,

\[
                         -F'(w)<-K'(w)<3/10.
\]

Integrating only the negative part of `F'` proves the first bound in
(1.3).  The authenticated estimates `F(s)<61/1000` and `F(t)>0` on the
half band prove the second. \(\square\)

## 2. One common minorant for both gates

Use the exact constants

\[
 \varepsilon={1\over20000},
 \qquad
 C_0={5503\over125000},
 \qquad
 M={61\over1000},
 \qquad
 \eta=M-C_0={2122\over125000}.
\tag{2.1}
\]

Jacobi reflection gives

\[
 F(w)+F(A-w)=\rho(w),
 \qquad |\rho(w)|<\varepsilon.
\tag{2.2}
\]

At the half shift,

\[
 F(A/2)={\rho(A/2)\over2}
 =2\sum_{m\ge1}(-1)^{m+1}e^{-4\pi m^2},
\]

so

\[
                         0<F(A/2)<{1\over40000}.
\tag{2.3}
\]

Define

\[
 D(\delta)=\min\left\{{3\delta\over10},M\right\},
\tag{2.4}
\]

and

\[
 E(\delta)=
 \min\left\{{3\delta\over20},F(A/4)-F(A/2)\right\}.
\tag{2.5}
\]

### Lemma 2.1 (the three envelope bounds)

For every `0<=delta<=A/2`,

\[
 \boxed{
 \mathcal H(\delta)>C(A+\delta)-D(\delta)-\varepsilon,}
\tag{2.6}
\]

\[
 \boxed{
 \mathcal I(\delta)>-\varepsilon-max\{\eta,D(\delta)\},}
\tag{2.7}
\]

and

\[
 \boxed{
 \mathcal S(\delta)>-\varepsilon-F(A/2)-E(\delta).}
\tag{2.8}
\]

Moreover,

\[
 \boxed{
 C((A+\delta)/2)
 >C(A+\delta)-\varepsilon-F(A/2)-E(\delta).}
\tag{2.9}
\]

#### Proof

Increasing the period from `A` to `A+delta` removes negative Gaussian
tail mass at every fixed shift below `A`.  For an admissible `b` in
`mathcal H`, both `b` and `b+delta` lie in `[0,A/2]`.  Reflection and
Lemma 1.1 therefore give

\[
\begin{aligned}
 F_\tau(b+\delta)+F_\tau(A-b)
 &\ge F(b+\delta)+F(A-b)\\
 &>F(b+\delta)-F(b)-\varepsilon\\
 &\ge-D(\delta)-\varepsilon.
\end{aligned}
\]

The reflection comparison in the preceding line is strict, so the final
bound remains strict.  This proves (2.6).

For the inactive envelope, period monotonicity gives

\[
\begin{aligned}
 &F_\tau(A-b)+\min\{C(\tau),F_\tau(m_\delta(b))\}\\
 &\quad\ge
 F(A-b)+\min\{C,F(m_\delta(b))\}\\
 &\quad>
 -\varepsilon-
 \left[F(b)-\min\{C,F(m_\delta(b))\}\right].
\end{aligned}
\tag{2.10}
\]

The bracket is

\[
 \max\{F(b)-C,F(b)-F(m_\delta(b))\}.
\]

Its first member is smaller than `M-C_0=eta`; its second is at most
`D(delta)` by (1.3), because `m_delta(b)-b<=delta`.  The strict reflection
comparison in (2.10) preserves the strict inequality in (2.7).

For `w<=A/2`, `F_tau(w)>=F(w)>0`.  If
`A/2<w<=tau/2`, put `v=A-w`.  Then

\[
 {A-\delta\over2}\le v<{A\over2}.
\]

This interval lies in `[A/4,A/2]`.  Reflection, monotone decrease there,
and (1.3) give

\[
 F_\tau(w)\ge F(w)>-\varepsilon-F(v)
 >-\varepsilon-F(A/2)-E(\delta).
\]

This proves (2.8).  Finally use the exact interlacing identity

\[
 C(\tau/2)=C(\tau)+F_\tau(\tau/2)
\]

and apply the same last estimate at `w=tau/2`, proving (2.9). \(\square\)

### Corollary 2.2 (common gate minorant)

For both `star in {XY,Z}`,

\[
 \boxed{
 \mathfrak G_\star(\delta)
 >C(A+\delta)-2\max\{\eta,D(\delta)\}
   -F(A/2)-E(\delta)-3\varepsilon.}
\tag{2.11}
\]

#### Proof

For `Z`, add (2.9) to twice (2.7).  For `XY`, add
(2.6)--(2.8) and use `D<=max{eta,D}`. \(\square\)

## 3. An explicit positive interval

The ceiling train is strictly increasing and strictly concave on
`[A,infinity)`, and the authenticated endpoint bounds are

\[
 C(A)>C_0,
 \qquad
 C(6A/5)>{63\over1000}.
\tag{3.1}
\]

Concavity and `A<8/9` imply, for `0<=delta<=A/5`,

\[
 \boxed{
 C(A+\delta)>C_0+{5337\over50000}\delta.}
\tag{3.2}
\]

Indeed, with `t=5delta/A`, concavity gives

\[
 C(A+\delta)
 \ge(1-t)C(A)+tC(6A/5)
 >(1-t)C_0+t{63\over1000}.
\]

The certified endpoint difference is `2372/125000`.  Since it is positive
and `5/A>45/8`, the coefficient of `delta` is larger than

\[
 {45\over8}{2372\over125000}={5337\over50000}.
\]

Put

\[
 \delta_0={1061\over18750},
 \qquad
 \boxed{\delta_*={43849\over643260}}.
\tag{3.3}
\]

Thus `3 delta_0/10=eta`, and

\[
 0<\delta_0<{3\over50}<\delta_*<{7\over100}<{A\over5}.
\tag{3.4}
\]

### Theorem 3.1 (certified local signing)

For both gates,

\[
 \boxed{
 \mathfrak G_{XY}(\delta)>0,
 \qquad
 \mathfrak G_Z(\delta)>0
 \quad(0\le\delta\le\delta_*).}
\tag{3.5}
\]

#### Proof

First take `0<=delta<=delta_0`.  Then
`max{eta,D(delta)}=eta`, while `E(delta)<=3delta/20`.  Equations
(2.3), (2.11), and (3.2) give

\[
 \mathfrak G_\star(\delta)
 >{9897\over1000000}-{2163\over50000}\delta.
\tag{3.6}
\]

Since `delta_0<3/50`, the right side is larger than

\[
 {9897\over1000000}
 -{2163\over50000}{3\over50}
 ={36507\over5000000}>0.
\tag{3.7}
\]

Now take `delta_0<=delta<=delta_*`.  Here
`D(delta)=3delta/10>=eta`; the range cap in (2.4) is inactive because
`delta_*<7/100<61/300`.  Hence

\[
 \mathfrak G_\star(\delta)
 >{43849\over1000000}-{32163\over50000}\delta.
\tag{3.8}
\]

The right side is nonnegative precisely through

\[
 \delta={43849/1000000\over32163/50000}
 ={43849\over643260}=\delta_*.
\]

All preceding inequalities are strict, so the gate is strictly positive
also at `delta=delta_*`. \(\square\)

## 4. Both relaxed gates fail at the far endpoint

The following rational Gaussian bounds are exact.  The first and the
`e^{-pi}` bound are already authenticated; the remaining rows follow from
`pi<22/7` and the degree-24 Taylor majorant

\[
 U_{24}(x)=\sum_{n=0}^{24}{x^n\over n!}
 +{x^{25}\over25!}\,{1\over1-x/26}
\tag{4.1}
\]

for `e^x`.  Direct rational cross multiplication gives

\[
\begin{array}{c|c}
\text{Gaussian}&\text{strict lower bound}\\ \hline
e^{-\pi/4}&4559/10000\\
e^{-\pi}&27/625\\
e^{-\pi/64}&119/125\\
e^{-49\pi/64}&901/10000\\
e^{-\pi/16}&1027/1250\\
e^{-9\pi/16}&853/5000\\
e^{-\pi/36}&9163/10000\\
e^{-25\pi/36}&1127/10000\\
e^{-25\pi/16}&73/10000.
\end{array}
\tag{4.2}
\]

For example the rational exponent majorants used in the new rows are

\[
 {11\over224},\ {539\over224},\ {11\over56},\ {99\over56},\
 {11\over126},\ {275\over126},\ {275\over56},
\]

respectively.  Formula (4.1) bounds the positive Taylor tail because all
successive ratios after degree 25 are at most `x/26`.

### Theorem 4.1 (endpoint obstruction)

At the formal endpoint `delta=A/2`,

\[
 \boxed{
 \mathfrak G_{XY}(A/2)<-{21\over2000},
 \qquad
 \mathfrak G_Z(A/2)<-{9\over2500}.}
\tag{4.3}
\]

#### Proof

Put `tau=3A/2`.  Since `B_{A/2}=0`, and since `b=A/3` is admissible in
`mathcal I`,

\[
\begin{aligned}
 \mathfrak G_{XY}(A/2)
 \le{}&C(\tau)+2F_\tau(A/2)+F_\tau(A)\\
     &+F_\tau(2A/3)+F_\tau(3A/4).
\end{aligned}
\tag{4.4}
\]

Discarding only negative Gaussian tails on the right gives

\[
\begin{aligned}
 \mathfrak G_{XY}(A/2)
 <5-&\bigl(
 2e^{-\pi/4}+2e^{-\pi/16}+2e^{-9\pi/16}+e^{-\pi}\\
 &\qquad+e^{-\pi/36}+e^{-25\pi/36}
 +e^{-\pi/64}+e^{-49\pi/64}\bigr).
\end{aligned}
\tag{4.5}
\]

The parenthesis is larger, by (4.2), than

\[
 {50105\over10000}.
\]

This proves the first inequality in (4.3).

For the `Z` gate, use `b=A/3` in both copies of `mathcal I` and use
the low endpoint `F_tau(A/2)` inside the minimum.  Thus

\[
 \mathfrak G_Z(A/2)
 \le C(3A/4)+2F_\tau(2A/3)+2F_\tau(A/2).
\tag{4.6}
\]

Keeping the first negative tail of `C(3A/4)` and discarding all later
negative tails gives

\[
\begin{aligned}
 \mathfrak G_Z(A/2)
 <6-&\bigl(
 2e^{-\pi/4}+e^{-\pi/64}+e^{-49\pi/64}+e^{-25\pi/16}\\
 &\qquad+2e^{-\pi/16}+2e^{-9\pi/16}
 +2e^{-\pi/36}+2e^{-25\pi/36}\bigr).
\end{aligned}
\tag{4.7}
\]

The parenthesis is larger than

\[
 {60036\over10000},
\]

which proves the second inequality in (4.3). \(\square\)

### Corollary 4.2 (the relaxed scalar route is intrinsically incomplete)

Both gates are continuous on `[0,A/2]`.  Indeed, parameterize the moving
domains in `mathcal H` and `mathcal S` by fixed unit intervals and apply
continuity of a minimum over a compact set.  Hence each gate has at least
one zero in

\[
                         (\delta_*,A/2),
\tag{4.8}
\]

and is strictly negative on some one-sided neighborhood of `A/2`.

Therefore no proof of complete six-slot `h=4` positivity can proceed by
signing the relaxed gates (0.6) on their full formal range.  The negative
gate values do **not** exhibit nonpositive physical Bellman tables: the
separate envelope minima need not be simultaneously attainable.  They
prove only that the present decoupled scalar relaxation loses essential
correlation.

## 5. Exact residual KKT and Chamber-II subtraction ledger

The unresolved parameter interval is now bounded explicitly:

\[
                         \delta_*<\delta<A/2.
\tag{5.1}
\]

Write

\[
 T_\tau(w)=F_\tau'(w),
 \qquad
 R_\tau(w)=\partial_\tau F_\tau(w)
 =\sum_{q\ge1}qK'(q\tau+w).
\tag{5.2}
\]

Every term in `R_tau(w)` is strictly positive.  The exact Chamber-II
residual subtraction identity is

\[
 \boxed{
 R_\tau(w)-T_\tau(w)
 =-K'(w)+\sum_{q\ge1}(q-1)K'(q\tau+w).}
\tag{5.3}
\]

In particular,

\[
T_\tau(w)=0\quad\Longrightarrow\quad R_\tau(w)>0.
\tag{5.4}
\]

Also, when `0<=w<=A/2`, Lemma 1.1 and (5.3) give

\[
                         R_\tau(w)-T_\tau(w)>0.
\tag{5.4a}
\]

For a smooth complementary-pair branch satisfying
`T_tau(r)=T_tau(s)=t`, one has the exact coefficient ledger

\[
 R_\tau(r)+R_\tau(s)+T_\tau(r)
 =[R_\tau(r)-T_\tau(r)]
  +[R_\tau(s)-T_\tau(s)]+3t.
\tag{5.5}
\]

Thus the period residual is strictly positive at every isolated
one-shift critical train.  Formula (5.5) is the precise analogue of the
Chamber-II shift-stationarity subtraction on a complementary-pair branch;
no sign is asserted for its full right side when one shift lies above
`A/2`.  Those pair branches therefore remain in the residual KKT locus.

For completeness, the residual candidate list is as follows.

* A minimizer of `mathcal H` has `b=0`, `b=B_delta`, or
  `T_tau(b+delta)=T_tau(A-b)`.
* A minimizer of `mathcal I` has `b=0`, `b=A/3`, a clip or cap switch
  `b+delta=A/2` or `F_tau(m_delta(b))=C(tau)`, or obeys
  `T_tau(A-b)=0` on a constant-low branch or
  `T_tau(b+delta)=T_tau(A-b)` on the moving branch.
* A minimizer of `mathcal S` is `0`, `tau/2`, or obeys
  `T_tau(w)=0` with `A/2<=w<=tau/2`.

On every smooth branch, an outer stationary point satisfies

\[
 \boxed{\mathcal H'+\mathcal I'+\mathcal S'=0}
 \quad\text{or}\quad
 \boxed{{1\over2}\sum_{q\ge1}qK'(q\tau/2)+2\mathcal I'=0},
\tag{5.6}
\]

with the exact envelope derivatives from the redundant-endpoint theorem.
At a branch tie, clip, cap switch, or changing active minimizer, the exact
one-sided local-minimum condition is

\[
                         \partial_-\mathfrak G\le0
                         \le\partial_+\mathfrak G.
\tag{5.7}
\]

At a multiway tie this implies, but is stronger than merely writing, the
Clarke necessary condition that zero lie in the convex hull of the active
branch derivatives.  Outer endpoints
`delta=delta_*`, `delta=A/2`, and all inner domain endpoints remain
separate candidates.  A gate zero itself additionally satisfies
`mathfrak G=0`; it need not be outer-stationary.

Equations (5.1)--(5.7), together with the finite inner list, are the exact
bounded KKT locus.  There is no omitted smooth branch and no appeal to a
sampled minimizer.

## 6. Exact scope

This theorem proves:

1. both outer gates are strictly positive through the explicit rational
   displacement `delta_*`;
2. both gates are strictly negative at the far formal endpoint and hence
   the relaxation necessarily crosses zero;
3. every remaining analytic candidate lies in the bounded interval
   (5.1) and obeys the exact smooth or nonsmooth ledger above.

It does **not** prove complete six-slot `h=4` positivity or negativity of
any physical table.  The next proof must restore correlation between the
two reflected pairs and the singleton, or return to the literal
endpoint-period train; further optimization of the already decoupled
gates cannot make them positive on the full range.

## 7. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| exact two-gate/KKT reduction | `MATH_THEOREM_SIX_SLOT_H4_REDUNDANT_ENDPOINT_THREE_BLOCK_SCALAR_KKT_REDUCTION_20260804.md` | `f410d86f5d544755c08f269ece1d47910f2d3c055be91c7a391bb548090f53d3` |
| independent audit of that reduction | `MATH_AUDIT_SIX_SLOT_H4_REDUNDANT_ENDPOINT_THREE_BLOCK_SCALAR_KKT_REDUCTION_INDEPENDENT_20260804.md` | `f92d2d444c23cbc7366820d367935a9db5bbd304faafcd73e53f445963a5ee0e` |
| compact Gaussian slope and ceiling bounds | `MATH_THEOREM_H4_INERT_COMPACT_GAUSSIAN_GATE_CLOSURE_20260804.md` | `f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b` |
| Jacobi reflection and residual bound | `MATH_THEOREM_APERY_LONG_WRAP_EUCLIDEAN_SHIFT_AND_THETA_RESIDUAL_20260804.md` | `7540343eab8e110d950c7e19a6dea33aefc2e17a89f7c90b93966a4ed653b738` |
| half-band positivity and upper bound | `MATH_THEOREM_SIX_SLOT_ENDPOINT_EFFICIENT_SUBCOMPLEMENTARY_PAIR_CLOSURE_20260804.md` | `4929d9e074816be68ece5a97203c5ea1696fd2f79f8445da9cc746ad205209e0` |
| Chamber-II residual-subtraction model | `MATH_THEOREM_CHAMBER_II_PERIOD_RESIDUAL_INCOMPATIBILITY_AND_COMPLETE_CLOSURE_20260804.md` | `52ec7f4ac4dbe9f0a32e5eed063cf5bf8419c535575a631b16d8c98d31e40a68` |
