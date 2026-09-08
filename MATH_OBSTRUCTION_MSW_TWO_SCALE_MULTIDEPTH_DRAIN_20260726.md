# A persistent-suffix dual obstruction for high Catalan overshoot

Date: 2026-07-26

## 0. Outcome

The compatible two-adjacent-scale cube has an explicit coherent dual
witness. It rules out the full cube whenever the Catalan overshoot
`Cat_r/p` exceeds `64/11+o(1)`. Below that threshold the witness is not
strong enough: switches beyond the deliberately cardinality-tuned
subcube may compensate for the dead suffix arm.

For every scale-`s` rectangle and every depth `q>=s`, one of its four
isolated arms transports mass between two targets which are already above
the row-power cap `p` in the canonical MSW factor.  That arm has zero
signed action on the canonical overloaded-set cut.  Hence an isolated
rectangle can drain at most three units, not four.

The only possible escape is a nonlinear window having switches at both
boundaries.  Such interactions are sparse.  A two-hole Catalan count gives,
uniformly for the phase-critical depths,

\[
             J_q=O(W/r^3)                                \tag{0.1}
\]

double-boundary windows among the complete scale-`r`/`r+1` catalogues.
If `B` bits of the compatible cube are available, every state satisfies

\[
 \boxed{
  \bigl(K_{q,p}-(W-N_q)\bigr)_+
  \ge D_r-(W-N_q)-3B-O(W/r^3).}                         \tag{0.2}
\]

For the full compatible cube,

\[
 B=C_r=M_r+M_{r+1}-E_r,
 \qquad {B\over H_{m,r}\Cat_r}
 =\rho_{m,r}{C_r\over M_r}.                             \tag{0.3}
\]

The leading term in (0.2) is positive precisely when

\[
 {\Cat_r\over p}>t^{\ddagger}_{m,r}
 :=\left[{1\over2}-3\rho_{m,r}{C_r\over M_r}\right]^{-1}
 ={64\over11}+O(r^{-1}+r/m).                            \tag{0.4}
\]

Above this threshold, summing through `H=Theta(p^(1/4))` gives

\[
 \boxed{
  \operatorname {PCap}_{[r+1,H]}
  =\Omega\left({Wp^{1/4}\over(\log p)^{3/2}}\right)
  \gg W.}                                                \tag{0.5}
\]

Thus the literal two-scale lane is closed on every overshoot subsequence
bounded below by `64/11+epsilon`, even after:

* combining the two adjacent scales;
* deleting every physical cross-scale conflict;
* choosing the remaining bits adversarially and coherently across depths.

The obstruction is the persistent saturated suffix arm, witnessed by the
canonical overloaded-set potentials. It also proves that the deliberately
tuned `L=floor((D_r-c_H)/4)` subcube cannot work. That latter fact alone
does not close the full lane, because the compatible cube has additional
exact variables. For overshoot at or below `64/11`, and for a menu with a
third scale, a new dual or a positive construction remains open.

---

## 1. Persistent saturation of one suffix arm

Fix a scale `s` parent context `C`.  At its matched depth, the elementary
rectangle indexed by `R in D_(s-1)` has the form

\[
 a_{s,C,R}
 =\partial_C(A_{C,s}+B_{C,s})
  -\partial_C(P^E_{C,R,s}+P^O_{C,R,s}).                  \tag{1.1}
\]

The distinguished suffix arm `partial_C A_(C,s)` moves one occurrence
from a source target of canonical load at least

\[
                         d_s=\Cat_s                      \tag{1.2}
\]

to a destination target of canonical load at least

\[
                         e_s=\Cat_{s-1}.                 \tag{1.3}
\]

If `r` is minimal with `Cat_r>=4p` and `s in {r,r+1}`, then

\[
                         d_s>p,\qquad e_s>p.             \tag{1.4}
\]

For `s=r`, this uses

\[
 {\Cat_{r-1}\over\Cat_r}
 ={r+1\over2(2r-1)}>{1\over4};                           \tag{1.5}
\]

for `s=r+1` it is immediate from `e_(r+1)=Cat_r>=4p`.

### Lemma 1.1 (suffix saturation persists at every larger depth)

For every `q>=s`, the isolated depth-`q` column of the same rectangle has
a suffix arm whose source and destination both belong to

\[
              \Omega_q:=\{S:\mu_q^{MSW}(S)>p\}.         \tag{1.6}
\]

#### Proof

At depth `s`, the two targets in (1.2)--(1.3) are obtained from a fixed
suffix of the common parity tail.  Increasing the depth from `s` to `q`
shortens that suffix by deleting exterior coordinates; it does not inspect
the Catalan filling `R`.  Every canonical occurrence counted in
(1.2)--(1.3) therefore projects to the corresponding shortened suffix
target.  Several old targets may coalesce under this projection, but an
occurrence is never lost.  The new source and destination loads are hence
at least `d_s` and `e_s`.  Equation (1.4) puts both in `Omega_q`.
\(\square\)

Here are the endpoints without shorthand. Let

\[
 \ell_q=m-q-1,
 \qquad A_{C,q}=\operatorname {suf}_{\ell_q}(\mathsf O_C)              \tag{1.7}
\]

for the parity tail carrying the marked `2 -> 4` arm (interchanging
`mathsf O` and `mathsf E` only changes the chosen normalization). If the
local transposed labels are `beta_C,gamma_C`, the two endpoints are

\[
 S_{C,q}=A_{C,q}\cup\{\beta_C\},
 \qquad T_{C,q}=A_{C,q}\cup\{\gamma_C\}.                \tag{1.8}
\]

At `q=s`, the source occurrences are the boundary-rooted windows in the
`Cat_s` rows `10v`, `v in D_s`; the destination occurrences include the
`Cat_(s-1)` rows `1100R`, `R in D_(s-1)`. Keeping the same boundary and
shortening its suffix sends these distinct row occurrences respectively
to `S_(C,q)` and `T_(C,q)`. Thus the literal bounds are

\[
 \mu_q^{MSW}(S_{C,q})\ge\Cat_s,
 \qquad
 \mu_q^{MSW}(T_{C,q})\ge\Cat_{s-1}
 \qquad(q\ge s).                                        \tag{1.9}
\]

These are occurrence injections, not estimates obtained by averaging.

### Why the second self-depth arm does not propagate

At the matched depth there is a second occurrence-level neutral move.  In
the notation of Lemma 15.2A of the plateau audit, the two switched rows
have

\[
 B_R:\quad O_C\cup\{2\}\longrightarrow O_C\cup\{4\},
 \qquad
 A_R:\quad O_C\cup\{4\}\longrightarrow O_C\cup\{3\}.   \tag{1.10}
\]

All three displayed canonical loads are above the cap at `q=s`.  This is
the source of the self-depth two-arm estimate.  It is important, however,
that the canonical preload at `O_C union {3}` is supplied by the rows

\[
                         D_R=101R0                      \tag{1.11}
\]

on the *opposite* boundary window: `A_R` uses phases `1,...,s`, whereas
`D_R` supplies its preload on phases `0,...,s-1`.  On increasing the depth,
these two windows acquire different exterior states.  Equivalently, their
cores peel along the two opposite parity flags of the omitted-label word.
They agree at `q=s`, but there is no occurrence-preserving map from the
`D_R` windows to the new `A_R` endpoint for `q>s`.

By contrast, the target `O_C union {4}` in the first move of (1.10) is
preloaded by `A_R` on the *same* boundary alignment as the `B_R` window.
That is exactly the same-alignment injection used in (1.9).  Consequently
only this first neutral arm is certified at every larger depth.  The
self-depth estimate of two useful opposite arms must not be substituted
for the persistent estimate below.

Let `alpha_q=1_(Omega_q)`.  The isolated column has four unit arms.  The
arm in Lemma 1.1 contributes zero to

\[
        \alpha_q(N_{q,e})-\alpha_q(P_{q,e}),             \tag{1.12}
\]

so

\[
\boxed{
        \alpha_q(N_{q,e})-\alpha_q(P_{q,e})\le3.}        \tag{1.13}
\]

This holds for every retained scale-`r` and scale-`r+1` bit once
`q>=r+1`.

At the zero state,

\[
 \langle\alpha_q,\mu_q^{MSW}-p\mathbf1\rangle
 =K_{q,p}(F_{MSW}).                                      \tag{1.14}
\]

Thus `alpha_q` is the promised explicit fractional-potential witness.

---

## 2. Exact form of the nonlinear interaction remainder

Let `x` be any state of the compatible two-scale cube, and write

\[
 \mu_q^x
 =\mu_q^0+\sum_ex_ea_{q,e}+\mathcal R_q(x),            \tag{2.1}
\]

where `a_(q,e)` is the isolated column.

Boundary locality implies that the target of a depth-`q` window can be
nonadditive only if both of its boundary phases are selected switches.
Interior switched phases do not affect its intersection.  For one such
double-boundary window, the mixed second difference is

\[
 \mathbf e_{T_{11}}-\mathbf e_{T_{10}}
 -\mathbf e_{T_{01}}+\mathbf e_{T_{00}}.                 \tag{2.2}
\]

Its positive and negative masses are at most two.  Consequently, if
`J_q(x)` is the number of selected double-boundary windows, then

\[
 \boxed{
 |\langle\alpha_q,\mathcal R_q(x)\rangle|
  \le2J_q(x).}                                           \tag{2.3}
\]

This statement is fully statewise, not a first-order expansion at the
zero state. To see this, consider a selected switch whose phase is
strictly inside a window. Its two unchanged neighboring states `L,R` are
also inside the window, and the old and new middle states `M,M'` satisfy

\[
                         L\cap M\cap R=L\cap M'\cap R.   \tag{2.4}
\]

The compatible-cube construction makes affected phase-edge slabs
disjoint, so `L,R` are not changed by another retained switch. If `Z` is
the intersection of all other states of the window, then
`Z\subseteq L\cap R`, and (2.4) gives `Z\cap M=Z\cap M'`.
This remains true with arbitrarily many other interior switches. Hence a
window target is a function only of the two switch bits at its boundary
phases. Its complete Boolean expansion stops at the mixed second
difference (2.2); there are no higher-order rescues in the all-on state.

It remains to count such windows.

---

## 3. The two-hole Catalan count

For `s in {r,r+1}`, one switch incidence in a row is an aligned
size-`s+1` block whose local filling is one of

\[
                   1100R,\ 1010R,\qquad R\in D_{s-1}.   \tag{3.1}
\]

Thus there are `2Cat_(s-1)` admissible fillings of one marked block.

Fix `s,u in {r,r+1}` and a displacement `q>=r+1`.  After the incompatible
nested adjacent-scale pairs have been deleted, two switch incidences at
the two boundaries of a depth-`q` window lie in disjoint recursion blocks.
This includes the mixed pairs `s!=u`: nodes whose sizes differ by one are
either disjoint or in the unique direct-child configuration removed by the
interlacing matching. Thus no overlapping-scale pair is omitted below.

Put

\[
 C(z)=1+zC(z)^2,\qquad A(z)=zC(z),\qquad
 U(z)={1\over1-2A(z)}=A'(z).                            \tag{3.2}
\]

For one LCA-to-marked-node branch, mark by `x` the root nodes and sibling
subtrees on the complementary cyclic arc, and by `y` those on the phase
arc between the two marked blocks.  One context frame contributes either
`A(x)` or `A(y)`, so the exact bivariate branch series is

\[
                         V(x,y)={1\over1-A(x)-A(y)}.     \tag{3.3}
\]

For two incomparable marked blocks, the root-to-LCA context contributes
`U(x)` and the two LCA branches contribute `V(x,y)^2`.  The LCA,
boundary orientations, and fixed offsets inside the switch blocks change
this by only finitely many monomials.  It suffices to bound

\[
                         [x^a y^j]U(x)V(x,y)^2,          \tag{3.4}
\]

where the prescribed phase displacement fixes `j` up to `O(1)` and

\[
                         a=m-s-u-j+O(1).                \tag{3.5}
\]

For `q<=m/2`, one has `a=Omega(m)` and `j<=a+O(1)`.
Expanding the two branch frames gives

\[
 V(x,y)^2
 =\sum_{b\ge0}(b+1)A(y)^bC(x)^{b+2}.                   \tag{3.6}
\]

The exact coefficient formulas are

\[
\begin{aligned}
 X_{a,b}:=[x^a]U(x)C(x)^{b+2}
 &= {a+1\over2a+b+3}\binom{2a+b+3}{a+1},\\
 Y_{j,b}:=[y^j]A(y)^b
 &= {b\over j}\binom{2j-b-1}{j-b}\qquad(b\ge1).
                                                               \tag{3.7}
\end{aligned}
\]

The first follows from

\[
 UC^{b+2}=A'C^{b+2}={1\over b+1}(C^{b+1})',             \tag{3.8}
\]

and the second from Lagrange inversion for `A=z/(1-A)`. Uniform binomial
estimates, for `1<=b<=j<=a`, give

\[
\begin{aligned}
 X_{a,b}&\le C{4^a2^b\over\sqrt a}e^{-cb^2/a},\\
 Y_{j,b}&\le C{4^j2^{-b}b\over j^{3/2}}e^{-cb^2/j}.
                                                               \tag{3.9}
\end{aligned}
\]

Therefore

\[
\begin{aligned}
 [x^a y^j]UV^2
 &\le C{4^{a+j}\over\sqrt a\,j^{3/2}}
          \sum_{b\ge1}b^2e^{-cb^2/j}\\
 &\le C{4^{a+j}\over\sqrt a}.                          \tag{3.10}
\end{aligned}
\]

The case `j=0` satisfies the same bound directly. Multiplying by the two
internal filling counts in (3.1) yields

\[
 J_q^{s,u}
 \le C{4^{m-s-u}\over\sqrt m}\Cat_{s-1}\Cat_{u-1}
 \le {C'W\over(su)^{3/2}}.                              \tag{3.11}
\]

Since `s,u` differ from `r` by at most one, summing the four ordered scale
pairs gives

\[
 \boxed{J_q(x)\le J_q^{all}\le {CW\over r^3}}           \tag{3.12}
\]

uniformly for `r+1<=q<=m/2`.  Fixing `q` is essential: summing over all
displacements would free the `y`-degree and restore an extra factor of
order `m`.

---

## 4. The coherent dual lower bound

Let a compatible subcube have `B` available bits. For an arbitrary state
`x`, combine
(1.13), (1.14), (2.1), and (2.3):

\[
\begin{aligned}
 K_{q,p}(\mu_q^x)
 &\ge\langle\alpha_q,\mu_q^x-p\mathbf1\rangle\\
 &\ge K_{q,p}(F_{MSW})-3|x|-2J_q(x)\\
 &\ge K_{q,p}(F_{MSW})-3B-{2CW\over r^3}.               \tag{4.1}
\end{aligned}

Subtract `W-N_q` and take a positive part:

\[
\boxed{
 \bigl(K_{q,p}(\mu_q^x)-(W-N_q)\bigr)_+
 \ge
 \left[D_r-(W-N_q)-3B-{2CW\over r^3}\right]_+.}         \tag{4.2}
\]

For the deliberately tuned subcube

\[
 L=\left\lfloor{D_r-(W-N_H)\over4}\right\rfloor
 =\Theta(W/r^{3/2}),                                    \tag{4.3}
\]

equation (4.2) gives `L-o(L)` per depth, as previously claimed. This
closes that tuned subcube, but does not close a larger cube with `B>L`.

The argument is coherent across depths: it uses the family of exact dual
weights

\[
                         \alpha_q=\mathbf1_{\Omega_q}.   \tag{4.4}
\]

and the same physical state `x` at every depth.  No separate optimization
is taken.

---

## 5. Aggregate obstruction

Let

\[
        H\in[p^{1/4}/8,p^{1/4}/4].                       \tag{5.1}
\]

There are `Theta(p^(1/4))` depths between `r+1` and `H`, because
`r=Theta(log p)`. For the full compatible cube, put

\[
 B=C_r,
 \qquad
 \zeta_{m,r}:={B\over H_{m,r}\Cat_r}
 =\rho_{m,r}{C_r\over M_r}.                             \tag{5.2}
\]

Ignoring the uniformly negligible `(W-N_q)` and `O(W/r^3)` terms, the
normalized right side of (4.2) is

\[
             {1\over2}-{1\over t}-3\zeta_{m,r},
 \qquad t={\Cat_r\over p}.                              \tag{5.3}
\]

It is positive when

\[
 t>t^{\ddagger}_{m,r}
 :=\left({1\over2}-3\zeta_{m,r}\right)^{-1}
 ={64\over11}+O(r^{-1}+r/m).                            \tag{5.4}
\]

For every fixed `epsilon>0`, if
`t>=64/11+epsilon`, summing (4.2) gives

\[
\begin{aligned}
 \operatorname {PCap}_{[r+1,H]}(F_x)
 &\ge\Omega_\varepsilon\left(
    {Wp^{1/4}\over(\log p)^{3/2}}
             \right).                                   \tag{5.5}
\end{aligned}

This is larger than `W` by the factor
`p^(1/4)/(log p)^(3/2)->infinity`.  In particular no state, no product
mean followed by rounding, and no adversarial coherent selection inside
the full two-scale cube can have `PCap=o(W)` on such an overshoot
subsequence.

For a product mean, average (4.1) over states; the same lower bound holds
with `|x|` replaced by its expectation and `J_q(x)` by its expectation,
which is no larger than (3.12).  Thus the obstruction also directly
refutes the fractional/product gate.

### What a third scale changes

For any bounded scale menu, every column still loses one isolated drain
unit after the largest scale, and the two-hole nonlinear correction remains
`O(W/r^3)` per ordered scale pair. But a third catalogue also contributes
another `Theta(M_r)` bits. The simple cut (4.2) then has too much nominal
three-arm capacity and need not remain positive. Hence this note does not
rule out a physically compatible three-scale construction. To close it one
needs either a second saturated arm, a stronger weighted potential, or an
exact three-scale compatibility/capacity audit.

---

## 6. Scope

This theorem is specific to the literal interior recursive rectangles.
It does not rule out:

1. a parent-boundary-changing packet whose positive endpoint is genuinely
   below the cap;
2. a larger trade with more than four useful arms;
3. a different exact middle factor without the Catalan suffix plateau;
4. a nonlocal multi-parent atom whose double-boundary interactions occur
   at density `Theta(L)` at every protected depth.

It does rule out obtaining constant one by adding more independent copies
of the same interior leaf rectangle at the two adjacent Catalan scales.
The fixed saturated suffix arm costs one quarter of every column, while
nonlinear boundary interactions are smaller by the factor `r^(-3/2)`.
