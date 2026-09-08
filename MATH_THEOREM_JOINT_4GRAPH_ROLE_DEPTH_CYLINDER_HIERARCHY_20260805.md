# The joint 4-graph has an exact role-depth cylinder hierarchy

**Date:** 2026-08-05  
**Method:** exact FIFO core counting and weighted cylinder Laplace bounds;
no computation or search  
**Status:** sharp conditional theorem and necessity audit.  In the joint
level-two/bottom 4-graph, the load of role `B_2` is controlled by the
one-mark state `(T_3,b_3)`, the load of `B_1` by the two-mark state
`(T_3,b_3,b_2)`, and the load of `B_0` by the three-mark state
`(T_3,b_3,b_2,b_1)`.  The existing one-mark cylinder closes the first load
only.  Uniform bottom banks do not manufacture either missing mark.

## 1. The three nested cores

For one task after level three, write

\[
 \begin{aligned}
 C_2&=T_3-\{b_3\},             &&|C_2|=r-1,\\
 C_1&=T_3-\{b_3,b_2\},         &&|C_1|=r-2,\\
 C_0&=T_3-\{b_3,b_2,b_1\},     &&|C_0|=r-3.               \tag{1.1}
 \end{aligned}
\]

Then the three final owners are

\[
 \begin{aligned}
 T_2&=C_2+x_3,\\
 T_1&=C_1+x_3+x_2,\\
 T_0&=C_0+x_3+x_2+x_1.                                  \tag{1.2}
 \end{aligned}
\]

Thus fixing a role-`j` owner exposes exactly a codimension `3-j` core.  This
already predicts the required number of marked deletion coordinates.

Put

\[
                         h={H\over W}=\Theta(1/d),
 \qquad q_0=k-r=\Theta(d^2),                               \tag{1.3}
\]

and pre-reserve role banks of densities

\[
                         p_j={\beta_jH\over W}=\Theta(1/d).
                                                                    \tag{1.4}
\]

The fresh reservoir size `y` satisfies `y=(1+o(1))q_0`.

## 2. Marked-cylinder hypotheses

For `a=1,2,3`, let `X_alpha^(a)` indicate that one prescribed compatible
state

\[
 \alpha=(T_3,b_3,b_2,\ldots,b_{4-a})                       \tag{2.1}
\]

is selected.  The bank-conditioned `a`-mark cylinder is

\[
 \boxed{
 \mathbb E\left[\prod_{t=1}^mX_{\alpha_t}^{(a)}
                    \mid B_0,B_1,B_2\right]
 \le\vartheta_a^m,
 \qquad
 \vartheta_a={(1+o(1))H\over W(r)_a}.}                    \tag{C_a}
\]

Only compatible collections with distinct level-three owners occur, and
only `m=O(d)` is needed for the weakest tail below.

Condition `(C_(a+1))` is genuinely stronger than `(C_a)`: after sampling
an `a`-mark state, choosing the next mark as a deterministic function of
the old state preserves every `C_a` cylinder and may violate `C_(a+1)` by
a factor `Theta(r)`.

## 3. Exact candidate counts through one fixed owner

Fix `U_j in B_j`.  Before testing the other role banks, the number of
marked states whose depth-appropriate core can produce `U_j` is

\[
 \begin{array}{c|c|c}
 j&a=3-j&\text{number of marked states}\\ \hline
 2&1&r q_0,\\
 1&2&{r\choose2}(q_0)_2,\\
 0&3&{r\choose3}(q_0)_3.
 \end{array}                                               \tag{3.1}
\]

Indeed, choose the codimension-`a` core inside `U_j`, and then choose the
ordered `a` deleted marks outside `U_j`.  The fresh labels in
`U_j-core` are then determined up to `a!` orders, which are counted in the
downstream extension multiplicity below.

For one such marked state, the mean number of extensions using the fixed
owner and hitting all remaining banks is

\[
 \begin{array}{c|c}
 j&\text{mean extension multiplicity}\\ \hline
 2&(y-1)(y-2)p_1p_0,\\
 1&2(y-2)p_2p_0,\\
 0&6p_2p_1.
 \end{array}                                               \tag{3.2}
\]

Multiplying (3.1), (3.2), and the appropriate `vartheta_a` gives

\[
 \begin{aligned}
 \rho_2
 &= (1+o(1))h q_0y^2p_1p_0,\\
 \rho_1
 &= (1+o(1))h q_0^2y p_2p_0,\\
 \rho_0
 &= (1+o(1))h q_0^3p_2p_1.                               \tag{3.3}
 \end{aligned}
\]

All three are `Theta(d^3)`.  If

\[
                         D=(y)_3p_2p_1p_0,                 \tag{3.4}
\]

then

\[
                         \rho_j=(1+o(1)){D\over\beta_j},  \tag{3.5}
\]

as required by global incidence double counting.

## 4. Conditional load theorem

The extension multiplicity of one marked state has a product-binomial
tail under the uniform role banks.  By the same bounded-degree pruning used
for `K_y`, one may retain `(1-o(1))D` options per good task while imposing
the deterministic per-state caps

\[
                         w_2\le A d^2,
 \qquad                  w_1\le A d,
 \qquad                  w_0\le 6                         \tag{4.1}
\]

for a fixed `A`; the bad-task probability is `exp(-Omega(d))`.  Equivalently,
one may keep all options and use their product-binomial exponential moments.
The caps make the argument transparent.

### Theorem 4.1 (role-depth load tails)

For each `j=0,1,2`, assume `(C_(3-j))`.  Then, after deleting
`exp(-Omega(d))H` bad tasks, the size-biased high-load tail satisfies

\[
 \boxed{
 \mathbb E\left[
  \ell_j(U)1_{\{\ell_j(U)>(1+\eta)\rho_j\}}
        \mid U\in B_j\right]
 \le \rho_j e^{-c_jd}}                                   \tag{4.2}
\]

for fixed suitable `eta,c_j>0`.

#### Proof

Fix the banks and `U_j`.  Write the load as

\[
                         \ell_j(U)=\sum_\alpha w_\alpha X_\alpha,
                                                                    \tag{4.3}
\]

where `alpha` ranges over the depth-appropriate marked states in (3.1).
Uniform-bank Chernoff bounds give a size-biased exponential tail for the
sum of the prospective extension weights around its mean in (3.2); this is
the same quadratic-block argument for `j=2`, its two-stage analogue for
`j=1`, and an ordinary binomial-pair argument for `j=0`.

On the good environment, expand

\[
 e^{t\ell_j}=\prod_\alpha
       \left(1+(e^{tw_\alpha}-1)X_\alpha\right).           \tag{4.4}
\]

Condition `(C_(3-j))` bounds each distinct-state term by the corresponding
power of `vartheta_(3-j)`.  Convexity on the intervals in (4.1) gives the
Laplace transform of a compound Poisson variable with mean `O(rho_j)` and
jump cap respectively `O(d^2),O(d),O(1)`.  Its constant-factor tail
exponents are

\[
                         \Omega(\rho_2/d^2)=\Omega(d),
 \quad                    \Omega(\rho_1/d)=\Omega(d^2),
 \quad                    \Omega(\rho_0)=\Omega(d^3).     \tag{4.5}
\]

The differentiated expansion of (4.4) gives the same exponents for the
size-biased tail.  Add the exponentially small bad-environment contribution.
\(\square\)

The theorem shows in particular that the one-mark cylinder does close the
`B_2` resource row with the exact exponent needed by exceptional-core
cleanup.

## 5. Why one mark does not close `B_1`

Fix a prospective `B_1` owner `U_1`.  A two-mark core capable of producing
it is any

\[
                         C_1\in{U_1\choose r-2}.           \tag{5.1}
\]

There are `Theta(r^2)=Theta(d^4)` choices.  For each, the two deleted marks
`b_2,b_3` may be chosen outside `U_1` in `Theta(q_0^2)=Theta(d^4)` ordered
ways.  Thus there are `Theta(d^8)` compatible two-mark states, and `(C_2)`
selects their correct `Theta(d^3)` mass.

In contrast, `(C_1)` does not constrain `b_2`.  One may choose it
deterministically as part of the task label while leaving the law of
`(T_3,b_3)` unchanged.  At the one-mark intensity

\[
                         \vartheta_1=Theta(d^{-3}),         \tag{5.2}
\]

the same codimension-two atlas can carry `Theta(d^5)` selected one-mark
states compatible with `U_1`.  The remaining random-bank extension has
constant mean, so the resulting `B_1` load can be `Theta(d^5)`, two powers
of `d` above the nominal `Theta(d^3)` load, while every one-mark cylinder
remains unchanged.

Equivalently, the explicit cluster in
`MATH_THEOREM_LEVEL2_BOTTOM_JOINT_4GRAPH_DEGREES_AND_MARK_DEPTH_BARRIER_20260805.md`
is the simplest finite face of this phenomenon.  Capping identical
one-mark skeletons alone handles that face but not the whole codimension-two
atlas (5.1).

Therefore

\[
 \boxed{(C_1)+\text{uniform banks does not imply the }B_1
        \text{ resource tail}.}                           \tag{5.3}
\]

The minimal natural extra datum is the mark `b_2`, i.e. `(C_2)`.  No
information about `b_1` is needed for the `B_1` row.

## 6. Why two marks do not close `B_0`

Fix `U_0`.  Its relevant core is

\[
                         C_0\in{U_0\choose r-3},           \tag{6.1}
\]

and there are `Theta(r^3)=Theta(d^6)` such cores.  The three deleted marks
have `Theta(q_0^3)=Theta(d^6)` ordered choices.  Hence the full three-mark
atlas has `Theta(d^12)` states; intensity

\[
                         \vartheta_3=Theta(d^{-7})         \tag{6.2}
\]

selects `Theta(d^5)`, and the two remaining bank hits contribute
`Theta(d^{-2})`, giving the correct `Theta(d^3)` load.

Condition `(C_2)` leaves `b_1` uncontrolled.  Choosing `b_1` as a
deterministic function of the two-mark state preserves every `(C_2)`
cylinder but may concentrate the rank-`r-3` cores in (6.1).  The candidate
mass can then be larger by `Theta(r)`, and the uniform `B_2,B_1` tests do
not restore the missing marked-coordinate factor in a bank-conditioned
selection law.

Thus

\[
 \boxed{(C_2)+\text{uniform banks does not imply the }B_0
        \text{ resource tail};}                           \tag{6.3}
\]

the minimal natural extra datum is `b_1`, i.e. `(C_3)`.

## 7. Exact Haxell consequence and current frontier

If all three cylinder rows `(C_1),(C_2),(C_3)` hold, Theorem 4.1 and the
one-task lower tail give, after `exp(-Omega(d))H=o(H/d)` cleanup,

\[
 \min_i d(i)\ge(1-\eta)D,
 \qquad
 \max_{U\in B_j}d(U)\le(1+\eta){D\over\beta_j}.           \tag{7.1}
\]

Therefore Haxell gives an exact joint-band matching whenever

\[
 {2(1+\eta)\over1-\eta}
       \left({1\over\beta_0}+{1\over\beta_1}
                         +{1\over\beta_2}\right)<1.       \tag{7.2}
\]

All constants are fixed and the separator can reserve banks this large.

The role-by-role audit is consequently

\[
 \boxed{
 \begin{array}{c|c|c}
 \text{resource}&\text{needed cylinder}&\text{status from one mark}\\ \hline
 B_2&(T_3,b_3)&\text{closed},\\
 B_1&(T_3,b_3,b_2)&\text{open},\\
 B_0&(T_3,b_3,b_2,b_1)&\text{open}.
 \end{array}}                                             \tag{7.3}
\]

Hence the joint-band route does not yield an unconditional Haxell theorem
from the existing one-mark spread.  It does sharpen the missing theorem:
one additional mark closes `B_1`, and exactly one further mark closes
`B_0`; neither row requires a global Hall-cut invariant.

