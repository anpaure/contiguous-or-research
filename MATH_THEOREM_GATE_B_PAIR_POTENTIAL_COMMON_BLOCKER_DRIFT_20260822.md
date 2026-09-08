# Gate B pair potential: exact blocker drift and the common-neighbourhood boundary

**Date:** 2026-08-22  
**Status:** exact finite-deletion identities and an unconditional complete-state
reference bound.  The complete-state infinitesimal collision drift is
`O(D_M/r)` before multiplication by the marking probability, uniformly over
the shallow band.  Consequently its accumulated regenerated-reference
**linearized** contribution is `O(log(1/x)/r)`, not
`Theta(log(1/x))`.  The same bound is proved nonlinearly only for the
independent-blocker surrogate in Section 5.  This does **not**
bound the same statistic in the stopped, history-dependent residual
catalogue; that transfer remains open.

## 1. Pair mass and an arbitrary deletion cell

Let `C` be a finite labelled catalogue of `Z>0` rows.  Every row has exactly
`b` distinct windows in a target set `T` of size `N`.  Write

\[
 X(T)=|\{F\in C:T\text{ is a window of }F\}|,
 \qquad
 c(F,G)=|W(F)\cap W(G)|.                              \tag{1.1}
\]

The ordered pair mass and its normalized collision multiplier are

\[
 S=\sum_{F,G\in C}c(F,G)=\sum_TX(T)^2,
 \qquad
 K={NS\over b^2Z^2}.                                  \tag{1.2}
\]

Let `B subseteq C` be any deletion cell.  Put

\[
 m=|B|,\qquad Y(T)=|B\cap\{F:T\in W(F)\}|,             \tag{1.3}
\]

\[
 R_B=\sum_TX(T)Y(T),\qquad Q_B=\sum_TY(T)^2,
 \qquad L_B=2R_B-Q_B.                                 \tag{1.4}
\]

### Theorem 1.1 (exact finite one-cell drift)

If `C'=C-B`, `Z'=Z-m`, and `S',K'` are its pair mass and collision
multiplier, then

\[
 \boxed{S'=S-L_B,\qquad
 {K'\over K}={1-L_B/S\over(1-m/Z)^2}.}               \tag{1.5}
\]

Equivalently,

\[
 \boxed{
 L_B=\sum_{F,G\in C}c(F,G)
       1_{\{F\in B\text{ or }G\in B\}}.}             \tag{1.6}
\]

Thus, whenever `m/Z,L_B/S<=1/2`,

\[
 \log{K'\over K}
 =2{m\over Z}-{L_B\over S}
  +O\left((m/Z)^2+(L_B/S)^2\right).                 \tag{1.7}
\]

#### Proof

The new external degree is `X'(T)=X(T)-Y(T)`.  Squaring and summing gives

\[
 S'=\sum_T(X(T)-Y(T))^2=S-2R_B+Q_B.
\]

Alternatively, an ordered pair is lost exactly when at least one of its
members lies in `B`, which proves (1.6).  Substitute `Z'=Z-m` into (1.2)
to obtain (1.5).  The Taylor estimate in (1.7) follows from
`log(1-u)=-u+O(u^2)` on `[0,1/2]`.  \(\square\)

Now let the catalogue carry a conflict graph, and let `Gamma[H]` denote
the **closed** conflict neighbourhood of `H`, including `H`.  In one
isolated-edge bite, order the accepted isolated rows as
`H_1,...,H_s` and define their first-blocker cells

\[
 B_i=\Gamma[H_i]-\bigcup_{a<i}\Gamma[H_a].           \tag{1.8}
\]

The cells are disjoint and their union is exactly the deleted catalogue.
Applying (1.5) successively is an exact finite one-bite formula.  Notice
that the accepted rows are disjoint but their closed neighbourhoods need
not be; (1.8) is what removes that multiplicity.

## 2. The exact singleton tangent and its nonregular correction

Independently mark every catalogue row with probability `p`, accept the
isolated marks, and delete the closed neighbourhoods of the accepted rows.
Let `z(p)` and `s(p)` be the expected remaining catalogue size and expected
ordered pair mass.  At `p=0`, only singleton mark sets contribute to the
derivative.  For `H in C`, put

\[
 C_H=|\Gamma[H]|,qquad
 L_H=\sum_{F,G}c(F,G)
          1_{\{F\in\Gamma[H]\text{ or }G\in\Gamma[H]\}}.    \tag{2.1}
\]

### Theorem 2.1 (exact isolated-blocker tangent)

\[
 \boxed{
 \left.{d\over dp}\log{Ns(p)\over b^2z(p)^2}\right|_{p=0}
 =-{\sum_HL_H\over S}+{2\sum_HC_H\over Z}.}          \tag{2.2}
\]

For an ordered pair put

\[
 J(F,G)=|\Gamma[F]\cap\Gamma[G]|,qquad
 W_F=\sum_Gc(F,G).                                    \tag{2.3}
\]

Then the same derivative equals

\[
 \boxed{
 {1\over S}\sum_{F,G}c(F,G)J(F,G)
 +2\left\{ {1\over Z}\sum_FC_F
       -{1\over S}\sum_FW_FC_F\right\}.}            \tag{2.4}
\]

In particular, if the conflict graph is closed-neighbourhood regular and
`W_F` is constant, the correction in braces vanishes and the derivative
is precisely the `c`-size-biased mean common closed-neighbourhood size.

#### Proof

A singleton mark at `H` is isolated and deletes `Gamma[H]`.  Hence

\[
 z'(0)=-\sum_HC_H,\qquad s'(0)=-\sum_HL_H,
\]

which gives (2.2).  Next,

\[
 \sum_HL_H
 =\sum_{F,G}c(F,G)|\Gamma[F]\cup\Gamma[G]|.
\]

Use

\[
 |\Gamma[F]\cup\Gamma[G]|=C_F+C_G-J(F,G)
\]

and the symmetry of `c(F,G)` to obtain

\[
 \sum_HL_H=2\sum_FW_FC_F-\sum_{F,G}c(F,G)J(F,G).
\]

Substitution in (2.2) proves (2.4).  \(\square\)

Formula (2.4) is the exact reason a marginal degree calculation is
insufficient in a nonregular stopped catalogue.  There are two possible
sources of positive drift: common blockers of a shallow-colliding pair,
and a covariance between closed-neighbourhood size and the pair-endpoint
weight `W_F`.

## 3. Complete punctured catalogue and exact common-blocker scalar

Put

\[
 n=2r+1,qquad D_M=2r\,r!(r+1)!,qquad
 D_L={r+2\over r}D_M.                                \tag{3.1}
\]

A directed punctured configuration is a permutation of `[n]`; it retains
the `2r` cyclic `r`-windows and `2r` cyclic `(r-1)`-windows whose start is
not zero.  Two configurations conflict when their retained central decks
share a tagged target.  The resulting complete conflict graph is
vertex-transitive.

Fix `2<=q<=sqrt(r)/4`, put

\[
 k=r-q,qquad N_q={n\choose k},qquad
 D_q=n\,k!(n-k)!,                                    \tag{3.2}
\]

and let `Omega_q(T)` be the `D_q` permutations in which a fixed `k`-set
`T` is a full cyclic window.  Every row has `n` such full-row windows, so
the complete pair mass is `N_qD_q^2` and `K=1`.

### Proposition 3.1 (exact complete-state drift)

The derivative in (2.2) is

\[
 \boxed{
 I_q={1\over D_q^2}\sum_{F,G\in\Omega_q(T)}
       |\Gamma[F]\cap\Gamma[G]|
     =\sum_H\theta_H(T)^2,}                         \tag{3.3}
\]

where

\[
 \theta_H(T)={|\Gamma[H]\cap\Omega_q(T)|\over D_q}. \tag{3.4}
\]

#### Proof

In the complete catalogue both `C_F=|Gamma[F]|` and
`W_F=nD_q` are constant, so (2.4) has no nonregular correction.  Split
the pair weight `c_q(F,G)` over its common full-row windows and use target
transitivity.  This gives the first expression in (3.3).  Finally swap
the common blocker `H` with the ordered pair `(F,G)`:

\[
 \sum_{F,G\in\Omega_q(T)}|\Gamma[F]\cap\Gamma[G]|
 =\sum_H|\Gamma[H]\cap\Omega_q(T)|^2.
\]

Divide by `D_q^2`.  \(\square\)

## 4. Boundary envelope for the common-neighbourhood scalar

For a tagged central target `v`, define

\[
 w(v)=\Pr(v\in E(F)\mid F\text{ uniform in }\Omega_q(T)).    \tag{4.1}
\]

If `H` conflicts with `F`, then \(E(H)\cap E(F)\ne\varnothing\).  The union
bound therefore gives

\[
 \theta_H(T)\le g_H(T):=\sum_{v\in E(H)}w(v).        \tag{4.2}
\]

Let `d(v,u)` be the number of punctured configurations containing both
tagged central targets, with `d(v,v)=d(v)`.  Double counting `H` gives the
exact quadratic envelope

\[
 \boxed{
 I_q\le Q_q:=\sum_Hg_H(T)^2
       =\sum_{v,u}d(v,u)w(v)w(u).}                  \tag{4.3}
\]

We now record an entirely finite formula for `Q_q`.  It is useful both for
the proof and for independent verification.  Put `ell=n-k=r+1+q`.  For
`h in {r-1,r}` and `0<=a<=min(k,h)`, define

\[
 m_{k,h}(a)=
 \begin{cases}
 n-k-h+1,&a=0,\\
 2,&0<a<\min(k,h),\\
 |k-h|+1,&a=\min(k,h),
 \end{cases}                                         \tag{4.4}
\]

and use zero outside the feasible range.  The exact one-target weight is

\[
 \boxed{
 w_h(a)={n-1\over n}
 {m_{k,h}(a)\over {k\choose a}{\ell\choose h-a}}.}   \tag{4.5}
\]

Indeed, the full external start has `n` choices, the retained central
start has `n-1` choices, and the four labelled Venn cells give the two
binomial denominators.

For two central target sizes `h,h'` with intersection `s`, their exact
codegree is

\[
d_{h,h'}(s)=
 \left((n-2)m_{h,h'}(s)+1_{s=\min(h,h')}\right)
 s!(h-s)!(h'-s)!(n-h-h'+s)!.                       \tag{4.6}
\]

To verify (4.6), fix the cyclic start of the first target.  There are
`m_(h,h')(s)` relative starts of the second.  For a placement with distinct
starts, exactly `n-2` absolute rotations avoid the two forbidden puncture
origins; the unique same-start placement exists exactly when
`s=min(h,h')` and then has `n-1`, producing the additional indicator.
The four labelled Venn cells may be ordered independently in the displayed
factorial number of ways.  This proves (4.6) without an imported pair table.

Let `Mult(m;a,b,c,d)=m!/(a!b!c!d!)`, interpreted as zero unless its four
arguments are nonnegative and sum to `m`.  Then

\[
\begin{aligned}
 Q_q=\sum_{h,h'\in\{r-1,r\}}\sum_{a,a'}\sum_{t,u}
 &\operatorname {Mult}(k;t,a-t,a'-t,k-a-a'+t)\\
 {}\times&\operatorname {Mult}(\ell;u,h-a-u,h'-a'-u,
                   \ell-h+a-h'+a'+u)\\
 {}\times&w_h(a)w_{h'}(a')d_{h,h'}(t+u).            \tag{4.7}
\end{aligned}
\]

The zero convention makes all four sums finite without separately listing
their feasibility bounds.

### Theorem 4.1 (uniform shallow common-blocker bound)

There is an absolute constant `C` such that, uniformly for

\[
                         2\le q\le\sqrt r/4,
\]

\[
 \boxed{I_q\le Q_q\le {C\over r}D_M.}              \tag{4.8}
\]

For `q=2`, the explicit lower-containment part of the envelope is

\[
 {4\over r}D_M+O(D_M/r^2).                          \tag{4.9}
\]

Thus the order `D_M/r` of the envelope cannot be improved by an argument
which merely replaces conflict by the number of shared central targets.

#### Proof

Equation (4.7) follows by partitioning `T` and its complement into the
four membership cells of two central targets.  Their intersection is
`s=t+u`; multiplication by (4.6) and summation proves the formula.

We prove (4.8) without estimating the fourfold sum term by term.  Regard
`D=(d(v,u))` as a matrix on the disjoint union of the lower and middle
central target layers.  It is a Gram matrix of target--configuration
incidences, hence positive semidefinite.  Its row sum at `v` is

\[
 \sum_ud(v,u)=\sum_{H\ni v}|E(H)|=4r\,d(v)\le4rD_L. \tag{4.10}
\]

Consequently

\[
 \lVert D\rVert_{2\to2}\le4rD_L.                  \tag{4.11}
\]

The exact squared norm of the vector in (4.5) is

\[
 \lVert w\rVert_2^2=\left({n-1\over n}\right)^2
 \sum_{h\in\{r-1,r\}}\sum_a
 {m_{k,h}(a)^2\over {k\choose a}{\ell\choose h-a}}. \tag{4.12}
\]

We use the following elementary reciprocal-binomial estimate:

\[
\begin{array}{ll}
 q=2:&w=w_0+e,\quad \lVert e\rVert_2^2=O(r^{-2}),\\
 q\ge3:&\lVert w\rVert_2^2=O(r^{-2}),             \tag{4.13}
\end{array}
\]

where `w_0` is supported on the `(r+3)` lower targets `L` containing
`T`, and has the constant value

\[
                         c_0={n-1\over n}{2\over r+3}.         \tag{4.14}
\]

For completeness, here are the details.  In the lower layer the
containment term `a=k` in (4.12) is

\[
 {q^2\over {\ell\choose q-1}},                     \tag{4.15}
\]

and in the middle layer it is

\[
 {(q+1)^2\over {\ell\choose q}}.                   \tag{4.16}
\]

At `q=2`, (4.15) is `4/(r+3)` and is exactly the containment
contribution before the common prefactor in (4.12); it is the squared-norm
contribution of `w_0`.  Equation (4.16) is `O(r^-2)`.  At `q>=3`, both
are `O(r^-2)`, uniformly for
`q<=sqrt(r)/4`, by `{m choose j}>=(m/j)^j`.  The disjoint endpoint has
denominator respectively `{ell choose q+2}` or `{ell choose q+1}` and is
smaller.  On the proper-overlap range `m_{k,h}(a)=2`; use
`{k choose a}>=k` and

\[
 \sum_{j=q}^{\ell-q}{1\over{\ell\choose j}}
 \le {\ell\over{\ell\choose q}}.                    \tag{4.17}
\]

This is just binomial unimodality: every denominator in the displayed
range is at least `{ell choose q}`.  The additional factor `1/k` from
`{k choose a}>=k` cancels `ell` up to an absolute factor, since
`ell/k=O(1)` in the stated shallow range.  This proves (4.13), including
the stated uniformity.  Finitely many small `r` are absorbed by increasing
the absolute constant.

For `q>=3`, (4.11)--(4.13) immediately give

\[
 Q_q=w^TDw\le4rD_L\lVert w\rVert_2^2=O(D_M/r).    \tag{4.18}
\]

For `q=2`, positivity and Cauchy--Schwarz in the `D`-seminorm give

\[
 Q_q\le\left(\sqrt{w_0^TDw_0}+\sqrt{e^TDe}\right)^2. \tag{4.19}
\]

The second term is `O(D_M/r)` by (4.11) and (4.13).  For the first, two
distinct lower supersets of `T` have intersection `r-2`; hence (4.6)
gives

\[
 \lambda_{LL}(r-2)=2(2r-1)(r-2)!(r+1)!.
\]

Writing `ell=r+3`, exact summation on the support of `w_0` gives

\[
 w_0^TDw_0
 =c_0^2\left(\ell D_L+\ell(\ell-1)\lambda_{LL}(r-2)\right)
 ={4\over r}D_M+O(D_M/r^2).                         \tag{4.20}
\]

Equations (4.19)--(4.20) prove (4.8), while (4.20) is (4.9).  Finally
\(I_q\le Q_q\) was proved in (4.2)--(4.3).  \(\square\)

## 5. What the scale does and does not rule out

At the standard initial marking scale

\[
                         p={\gamma\over rD_M},       \tag{5.1}
\]

Theorems 2.1 and 4.1 give the complete-state singleton tangent

\[
                         pI_q=O_\gamma(r^{-2}).      \tag{5.2}
\]

A regenerated reference descent uses `O(r log(1/x))` constant-scale
bites.  Its accumulated linear common-blocker contribution is therefore

\[
 \boxed{O\left({\log(1/x)\over r}\right)=o(1),}      \tag{5.3}
\]

whereas a capacity-sized uniform-survivor Gate-B catalogue needs
`log K>=log(1/x)-O(1)`.  Thus the complete/regenerated singleton mechanism
is quantitatively too small by a factor of order `r`.

There is also an exact finite benchmark.  If every potential blocker is
activated independently with probability `p` and **all** activated closed
neighbourhoods are deleted, then in a closed-neighbourhood-regular graph
the ratio of expected pair mass to the square of expected catalogue size
is multiplied by

\[
 \mathbb E_{c\text{-pair}}(1-p)^{-J(F,G)}.           \tag{5.4}
\]

If `p<=1/2` and `pC_0<=beta`, where `C_0=|Gamma[F]|`, convexity on
`0<=J<=C_0` yields

\[
 \mathbb E(1-p)^{-J}
 \le1+\bigl((1-p)^{-C_0}-1\bigr){\mathbb EJ\over C_0}
 =1+O_\beta(r^{-2}),                                \tag{5.5}
\]

because `C_0=Theta(rD_M)` and `mathbb EJ=I_q=O(D_M/r)`.
This confirms (5.3) for the independent-blocker reference surrogate even
without linearizing `pC_0`.

For self-containment, the neighbourhood scale used here follows directly
from (4.6).  If \(t_H(G)=|E(H)\cap E(G)|\), then

\[
 \sum_Gt_H(G)=\sum_{v\in E(H)}d(v)=4(r+1)D_M,
\]

whereas

\[
 \sum_G\binom{t_H(G)}2
 =\sum_{\{v,u\}\subseteq E(H)}d(v,u)=O(D_M).        \tag{5.6}
\]

For the last estimate, identify each central window in the fixed cyclic
deck with its two boundary cuts.  A cut belongs to at most four tagged
central windows, so only `O(r)` unordered target pairs share a boundary
cut; the remaining `O(r^2)` pairs use four distinct cuts.  Substitution in
(4.6) gives respectively

\[
 d(v,u)=O(D_M/r),\qquad d(v,u)=O(D_M/r^2).          \tag{5.6a}
\]

Indeed, in each of the four tagged size combinations the shared-cut cases
are the containment or complementary endpoint terms of (4.6); moving one
step into the proper-overlap range multiplies the factorial quotient by at
most `1/r`, and successive terms form geometric tails.  Hence the first
class contributes `O(D_M)` and the second also contributes `O(D_M)`, which
proves the last estimate in (5.6).  Since
`t-1<=binom(t,2)` for `t>=1`,

\[
 4(r+1)D_M-O(D_M)\le C_0\le4(r+1)D_M,              \tag{5.7}
\]

which is the asserted `Theta(rD_M)` estimate.

The isolated-edge nibble is not that surrogate.  Acceptance makes the
blocker set dependent, and after previous bites neither `C_F` nor `W_F`
is constant.  The exact finite formula (1.5) then contains both the
common-neighbourhood term and the nonregular correction in (2.4), while
later first-blocker cells depend on earlier accepted rows.  Therefore
(5.3) does **not** prove `K_tau=o(1/x)` for the actual stopped process.
It proves the narrower and rigorous conclusion:

> any successful uniform-survivor route must create an adaptive
> common-blocker/nonregular covariance amplification absent from the
> complete-state tangent and the independent-blocker regenerated
> surrogate analyzed here.

The finite algebra and orbit sum are independently checked by
`scratch/verify_gate_b_pair_potential_common_blocker_drift_20260822.py`.
