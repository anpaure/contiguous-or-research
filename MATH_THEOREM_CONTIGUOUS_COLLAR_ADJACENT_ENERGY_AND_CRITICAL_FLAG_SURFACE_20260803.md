# Contiguous-collar adjacent energy and the critical flag surface

**Date:** 2026-08-03  
**Status:** unconditional rank-level theorem, with a label-level corollary for
weighted nested-chain packings.  No computation is used.

## 0. Outcome

Put

\[
 k=2r,\qquad W={2r\choose r},\qquad
 b_j={{2r\choose r-j}\over W}\quad(1\le j<r),
\]

and let

\[
 d=(\delta+o(1))\sqrt r,\qquad \delta={\sqrt\pi\over2}.
\]

Fix a nonnegative integer constant `C`, put `D=d+C`, and choose

\[
 \sqrt{\log2}\le c<\delta,\qquad
 a=\lceil c\sqrt r\rceil .                              \tag{0.1}
\]

Let `(L,R)` be an arbitrary joint law with

\[
 L\in\{0,1,\ldots,a\}
\]

satisfying

\[
 \Pr(L\ge j)=b_j\quad(1\le j\le a),                    \tag{0.2}
\]

\[
 R\subseteq\{a+1,\ldots,r-1\},\qquad
 L+|R|\le D\quad\hbox{pointwise}.                       \tag{0.3}
\]

Thus `L` is the forced length of a contiguous adjacent-rank collar and `R`
is an otherwise unrestricted residual rank set.  In particular, **no
stability, parity, or independence hypothesis is imposed on `R`**.

Write

\[
 q_j=\Pr(j\in R),\qquad
 \theta_j=\Pr(j,j+1\in R).                              \tag{0.4}
\]

If the residual marginals are near complete in the weak sense

\[
 0\le q_j\le b_j,\qquad
 \sum_{j>a}(b_j-q_j)=o(\sqrt r),                         \tag{0.5}
\]

then

\[
 \boxed{
 \sum_{j=a+1}^{a+2t-1}\theta_j
 \ge (2\eta(c)+o(1))\sqrt r,
 }
 \qquad t=\left\lfloor {D\over2}\right\rfloor,         \tag{0.6}
\]

where

\[
 \eta(c)=\int_{\delta/2}^{c+\delta}e^{-x^2}\,dx
              -{\delta\over2}>0.                       \tag{0.7}
\]

Consequently some adjacent residual pair satisfies

\[
 \boxed{
 \theta_j\ge {2\eta(c)\over\delta}+o(1)=\Omega_c(1).
 }                                                       \tag{0.8}
\]

The named-target standard `o(W)` leave implies the much stronger condition
`sum(b_j-q_j)=o(1)`, so (0.6)--(0.8) apply to every such residual packing.

For the symmetric uniform-order owner-flag law, (0.8) implies

\[
 \rho_2\ge
 \left({2\eta(c)\over\delta}+o(1)\right){1\over r}.      \tag{0.9}
\]

Moreover the forced collar law has `Pr(L=a)=b_a>0`.  Hence the maximum
supported atom size `K`, including its owner, satisfies

\[
 a+1\le K\le D+1,
\]

and therefore

\[
 \boxed{
 K=\Theta(\sqrt r),\qquad
 K^2\rho_2\ge
 {2c^2\eta(c)\over\delta}+o(1)=\Omega_c(1).
 }                                                       \tag{0.10}
\]

Thus allowing adjacent residual ranks does not move a near-complete
contiguous-collar law into the subcritical regime.  It merely changes the
old stable-set Hall contradiction into a forced macroscopic amount of
adjacent-rank cooccurrence.

In fact the codegree conclusion does not require uniform order if the
label-sensitive construction is still a weighted packing by nested-chain
atoms with named-target degrees at most one.  A direct averaging argument
then gives the same `Omega(1/r)` normalized codegree.  What rank data alone
do **not** control is a label-sensitive system which is not a target-capacity
packing, or whose adjacent rank obligations are split among different atoms
instead of appearing as one nested flag.

For `c>delta`, (0.2)--(0.3) are already infeasible for all sufficiently
large `r`: the event `L=a` has positive probability while `a>D`.  Hence the
range in (0.1), apart from the boundary `c=delta` whose feasibility depends
on lower-order terms in `d+C-a`, is the only nontrivial macroscopic-collar
range above the decorrelation threshold.

## 1. The path occupancy inequality

Let `P` be a path on `2t` vertices.  For `S subseteq V(P)`, put

\[
 m=|S|,\qquad
 e(S)=|\{xy\in E(P):x,y\in S\}|.
\]

### Lemma 1.1 (path excess is paid by adjacent energy)

For every `S subseteq V(P)`,

\[
 \boxed{
 |S|\le t+{e(S)+1\over2}.
 }                                                       \tag{1.1}
\]

### Proof

Let `h` be the number of nonempty selected runs.  Each selected run of
length `u` contributes `u-1` selected edges, so

\[
 e(S)=m-h.                                               \tag{1.2}
\]

The `2t-m` unselected vertices separate at most `2t-m+1` selected runs.
Thus

\[
 h\le2t-m+1.
\]

Substitution in (1.2) gives

\[
 e(S)\ge2m-2t-1,
\]

which is equivalent to (1.1). `square`

The additive `1/2` is only the linear-path boundary effect.  The scale of
the theorem is `sqrt(r)`, so it is immaterial, but retaining it makes every
finite inequality below exact.

## 2. An exact Hall-energy row

Let

\[
 A_t=\{a+1,a+2,\ldots,a+2t\},
 \qquad t=\left\lfloor{D\over2}\right\rfloor,           \tag{2.1}
\]

and define

\[
 E_t(R)=|\{j:a+1\le j<a+2t,\ j,j+1\in R\}|.            \tag{2.2}
\]

For all sufficiently large `r`, the block lies inside the residual distance
range (equivalently, its corresponding target ranks remain positive), and

\[
 D-a<t<D,
\]

because `c>delta/2`.

Apply Lemma 1.1 to `R cap A_t`.  The pointwise capacity (0.3) gives the
second bound

\[
 |R\cap A_t|\le D-L.
\]

Combining the two bounds yields the pointwise inequality

\[
 \boxed{
 |R\cap A_t|
 \le \min(t,D-L)+{E_t(R)+1\over2}.
 }                                                       \tag{2.3}
\]

Indeed, if `D-L<=t`, the capacity bound alone is stronger; if `D-L>t`, use
Lemma 1.1.

Taking expectations and using the tail-sum formula together with (0.2),

\[
\begin{aligned}
 \sum_{j\in A_t}q_j
 &\le \mathbb E\min(t,D-L)+{\mathbb E E_t(R)+1\over2}\\
 &=t-\mathbb E(L-(D-t))_+
       +{\mathbb E E_t(R)+1\over2}\\
 &=t-\sum_{j=D-t+1}^{a}b_j
       +{\mathbb E E_t(R)+1\over2}.                    \tag{2.4}
\end{aligned}
\]

Define the finite Hall surplus

\[
 \Delta_r(c,C)
 =\sum_{j=D-t+1}^{a+2t}b_j-t.                           \tag{2.5}
\]

Subtracting (2.4) from the target mass on `A_t` gives the exact inequality

\[
 \boxed{
 \mathbb E E_t(R)
 \ge 2\Delta_r(c,C)-1
       -2\sum_{j\in A_t}(b_j-q_j).
 }                                                       \tag{2.6}
\]

This is the desired replacement for the no-adjacent Hall row.  Setting
`E_t=0` recovers, up to the harmless path boundary constant, the stable-set
obstruction.

## 3. The energy is macroscopic

Uniformly for `j=O(sqrt(r))`,

\[
 b_j=\exp(-j^2/r+o(1)).                                  \tag{3.1}
\]

Also

\[
 {D\over\sqrt r}\longrightarrow\delta,
 \qquad {a\over\sqrt r}\longrightarrow c,
 \qquad {t\over\sqrt r}\longrightarrow{\delta\over2}.
\]

The Riemann sum in (2.5) therefore gives

\[
 \Delta_r(c,C)
   =(\eta(c)+o(1))\sqrt r,                               \tag{3.2}
\]

with `eta(c)` as in (0.7).  The positivity

\[
 \eta(c)>0\qquad(c\ge\sqrt{\log2})                     \tag{3.3}
\]

is the elementary Gaussian inequality proved in
`MATH_THEOREM_CONTIGUOUS_COLLAR_STABLE_RESIDUAL_HALL_OBSTRUCTION_20260803.md`.

Under (0.5), equations (2.6)--(3.3) give

\[
 \mathbb E E_t(R)
 \ge(2\eta(c)+o(1))\sqrt r,                             \tag{3.4}
\]

which is (0.6).  On the other hand,

\[
 \mathbb E E_t(R)
 =\sum_{j=a+1}^{a+2t-1}\theta_j.                        \tag{3.5}
\]

There are

\[
 2t-1=(\delta+o(1))\sqrt r
\]

summands.  Equations (3.4)--(3.5) prove (0.8).

The assumption in (0.5) may be weakened further: (3.4) holds whenever the
deficit on the single block `A_t` is `o(sqrt(r))`.  We use the global form
only because it is the natural consequence of a near-complete named-target
packing.

## 4. Uniform-order flag codegrees

Fix an index `j` satisfying (0.8), and put

\[
 u=r-j,\qquad s=u-1.
\]

Under the uniform-order owner-flag law, for every named flag

\[
 S\subset U,\qquad |S|=s,\quad |U|=u,
\]

the exact flag formula is

\[
 {d_x(S,U)\over d_x(U)}
 ={\theta_j\over q_j{u\choose s}}
 ={\theta_j\over q_j u}.                                \tag{4.1}
\]

Since `q_j<=1` and `u<=r`,

\[
 {d_x(S,U)\over d_x(U)}\ge{\theta_j\over r}.            \tag{4.2}
\]

The normalized maximum pair codegree uses the smaller incident degree, so
it is at least the ratio in (4.2).  Equation (0.9) follows.

Finally, (0.2) gives

\[
 \Pr(L=a)=b_a>0.                                        \tag{4.3}
\]

Every atom with `L=a` contains at least `a` target vertices.  The pointwise
capacity gives at most `D` target vertices in every atom.  Hence

\[
 a+1\le K\le D+1,                                       \tag{4.4}
\]

where the extra vertex is the owner.  Combining (4.2)--(4.4) with (0.8)
proves (0.10).

## 5. Label-sensitive orders: exact scope

The uniform-order formula (4.1) is convenient but not essential.  Consider
any weighted atom family satisfying all of the following.

1. There is total atom weight one at each of the `W` rank-`r` owners.
2. The selected targets inside each atom form one inclusion chain.
3. The empirical rank law of the atom family is the joint law `(L,R)` above.
4. Every named strict-lower target has total weighted degree at most one.

For a fixed adjacent distance pair `j,j+1`, every atom containing both
ranks contributes exactly one cover flag between ranks `u-1` and `u`, where
`u=r-j`.  Therefore

\[
 \sum_{\substack{|S|=u-1,\ |U|=u\\S\subset U}}
 d_x(S,U)=W\theta_j.                                    \tag{5.1}
\]

There are

\[
 {2r\choose u}u=Wb_j u                                 \tag{5.2}
\]

such named cover flags.  Some flag consequently has

\[
 d_x(S,U)\ge{\theta_j\over b_j u}
             \ge{\theta_j\over r}.                     \tag{5.3}
\]

Both incident target degrees are at most one.  Thus its normalized
codegree is at least its raw codegree, and (0.9)--(0.10) follow again.

Accordingly, a nonuniform label-sensitive order cannot evade the critical
pair scale while it remains a capacity-one nested-chain packing.  It may
change **which** named flags carry the collision, but cannot remove the
collision mass.

The rank-level argument by itself does not cover either of the following
larger classes.

* A weighted law with no named-target degree cap.  It need not represent a
  fractional target packing, and normalized codegrees can no longer be
  inferred from (5.1) alone.
* A physical representation in which the obligations at adjacent ranks are
  assigned to different atoms or different occurrence roles rather than to
  one nested owner flag.  Then `theta_j` is not the mass of one target-pair
  codegree ledger.

Those are genuine changes of architecture.  Within the owner-plus-flag
atom model, label sensitivity is not an escape.

## 6. Interpretation

The previous stable-residual theorem said that a contiguous collar and a
parity-separated residual law cannot coexist near perfectly.  The present
theorem gives the exact price of deleting parity separation:

\[
 \boxed{
 \text{near-complete residual mass}
 \Longrightarrow
 \Omega(\sqrt r)\text{ adjacent-rank cooccurrences per owner law}.
 }
\]

Since the relevant block has only `Theta(sqrt(r))` adjacent rank pairs,
one pair carries constant joint probability.  In an owner-flag packing
this forces normalized codegree `Omega(1/r)` while atom width remains
`Theta(sqrt(r))`.  Hence

\[
 K^2\rho_2=\Omega(1).
\]

The contiguous-collar route therefore faces a dichotomy:

* suppress adjacent residual ranks and lose `Theta(sqrt(r)W)` target mass;
* retain near-complete target mass and remain at or above the critical flag
  collision surface.

This is a limitation of black-box degree/codegree rounding, not a
nonexistence theorem.  A Boolean-specific laminar absorber may still round
the correlated flag law, and a different physical architecture may bundle
adjacent-rank roles without presenting them as one target-pair atom.
