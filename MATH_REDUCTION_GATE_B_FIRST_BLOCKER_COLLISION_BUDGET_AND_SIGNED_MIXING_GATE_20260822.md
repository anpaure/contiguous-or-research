# Gate B: exact first-blocker collision budget and the signed mixing gate

**Date:** 2026-08-22

**Status:** unconditional pathwise theorem for the actual stopped
isolated-edge process, plus a sharp obstruction.  The theorem proves that a
capacity-sized full-survivor cover forces logarithmic mass in one of two
first-blocker statistics: a signed endpoint-mixing deficit or a quadratic
common-blocker mass.  The complete punctured geometry makes the latter only
`O(r^-2)` at the singleton-bite scale, but it does not control the former
after adaptive deletions.  Therefore this note neither proves the positive
Gate-B alignment nor proves `K_tau=o(1/x)`.  It identifies the exact extra
stopped statistic needed for either conclusion and proves that
common-neighbour bounds alone cannot supply it.

The note also gives the exact balanced-rate linear program and dual for an
adaptive reinforcement bite, a canonical entropy-regularized switching
law, a finite `r=4` obstruction to obtaining a compensated shallow current
inside one natural `C_8`-switch orbit, and a punctured two-edge obstruction
showing that no such balanced rate law exists on every induced residual.

## 1. Catalogue, Palm law, and pair potential

Let `C` be a finite nonempty labelled row catalogue, `Z=|C|`.  Every row
has exactly `b` distinct windows in a target set `T` of size `N`.  Write

\[
 X(T)=|\{F\in C:T\in W(F)\}|,
 \qquad \pi(T)={X(T)\over bZ}.                       \tag{1.1}
\]

Then `pi` is a probability law.  For two rows put

\[
 c(F,G)=|W(F)\cap W(G)|,
 \qquad W_C(F)=\sum_{G\in C}c(F,G)
              =\sum_{T\in W(F)}X(T).               \tag{1.2}
\]

The ordered pair mass and collision multiplier are

\[
 S(C)=\sum_TX(T)^2=\sum_{F,G\in C}c(F,G),
 \qquad {\cal K}(C)={NS(C)\over b^2Z^2}
                   =N\sum_T\pi(T)^2.               \tag{1.3}
\]

Thus `K>=1`, with equality precisely when the external-window Palm law is
uniform.

## 2. One deletion cell: the exact signed recursion

Let `B` be a nonempty subset of `C`, put

\[
 m=|B|,\qquad \delta={m\over Z},\qquad
 Y(T)=|\{F\in B:T\in W(F)\}|.                       \tag{2.1}
\]

Define

\[
 R_B=\sum_TX(T)Y(T)=\sum_{F\in B}W_C(F),
 \qquad Q_B=\sum_TY(T)^2=\sum_{F,G\in B}c(F,G),    \tag{2.2}
\]

and the signed endpoint-mixing deficit

\[
 E_B={m\over Z}S(C)-R_B
    =m\left({1\over Z}\sum_{F\in C}W_C(F)
             -{1\over m}\sum_{F\in B}W_C(F)\right).            \tag{2.3}
\]

Positive `E_B` means that the cell deletes rows carrying less
external-pair mass than a uniform `m`-set would carry.  Equivalently, for
a uniform row `F` of `C`,

\[
 E_B=-Z\,\operatorname {Cov}
       \bigl(W_C(F),\mathbf1_{\{F\in B\}}\bigr).    \tag{2.4}
\]

### Theorem 2.1 (exact cell recursion)

Let `C'=C-B`.  Then

\[
 \boxed{S(C')=S(C)(1-2\delta)+2E_B+Q_B,}            \tag{2.5}
\]

and

\[
 \boxed{
 {{\cal K}(C')\over{\cal K}(C)}
 ={1-2\delta+(2E_B+Q_B)/S(C)\over(1-\delta)^2}
 =1+{2E_B+Q_B-\delta^2S(C)
        \over(1-\delta)^2S(C)}.}                   \tag{2.6}
\]

If `delta<=delta_0<1`, then

\[
 \boxed{
 \log{{\cal K}(C')\over{\cal K}(C)}
 \le {2(E_B)_++Q_B\over(1-\delta_0)^2S(C)}.}       \tag{2.7}
\]

#### Proof

The new external degree is `X'(T)=X(T)-Y(T)`.  Squaring and summing gives

\[
 S(C')=S(C)-2R_B+Q_B.
\]

Substitute `R_B=delta S(C)-E_B` to obtain (2.5), and use
`|C'|=Z(1-delta)` in (1.3) to obtain (2.6).  If the last fraction in
(2.6) is nonpositive, its logarithm is nonpositive.  Otherwise use
`log(1+u)<=u`, discard `-delta^2 S(C)`, replace `E_B` by its positive
part, and use `delta<=delta_0`.  This proves (2.7).  `square`

There is also an exact Palm form.  Give the deleted cell its own window
law

\[
 \nu_B(T)={Y(T)\over bm}.                            \tag{2.8}
\]

Then

\[
 \boxed{\pi'(T)={\pi(T)-\delta\nu_B(T)\over1-\delta}.}        \tag{2.9}
\]

Equations (2.6) and (2.9) are the same recursion, written respectively in
second-moment and transport form.

## 3. First-blocker cells in the actual bite

Now let `C_j` be the actual residual catalogue just before bite `j`.
Conditionally on the past, mark its rows independently, accept the isolated
marks, and delete their closed conflict neighbourhoods.  Order the accepted
rows deterministically as

\[
 G_{j,1},\ldots,G_{j,s_j}.
\]

Put `C_{j,0}=C_j` and define

\[
 B_{j,i}=\Gamma_{C_j}[G_{j,i}]
          -\bigcup_{a<i}\Gamma_{C_j}[G_{j,a}],
 \qquad C_{j,i}=C_{j,i-1}-B_{j,i}.                 \tag{3.1}
\]

Accepted rows are pairwise nonconflicting, so `G_{j,i}` is still present
in `C_{j,i-1}` and

\[
 B_{j,i}=\Gamma_{C_{j,i-1}}[G_{j,i}].              \tag{3.2}
\]

The cells are disjoint and partition `C_j-C_{j+1}`.  Apply the notation of
Section 2 to the current catalogue `C_{j,i-1}` and its cell `B_{j,i}`;
write the resulting quantities as

\[
 S_{j,i},\quad E_{j,i},\quad Q_{j,i},\quad
 \delta_{j,i}={|B_{j,i}|\over|C_{j,i-1}|}.          \tag{3.3}
\]

### Theorem 3.1 (stopped first-blocker collision budget)

Suppose every complete bite deletes at most one eighth of its starting
catalogue.  For every bounded stopping time `tau`, pathwise,

\[
 \boxed{
 \log{{\cal K}_\tau\over{\cal K}_0}
 \le {64\over49}\sum_{j<\tau}\sum_{i=1}^{s_j}
 {2(E_{j,i})_++Q_{j,i}\over S_{j,i}}.}             \tag{3.4}
\]

In particular, if `K_0=1` and the right side is
`o(log(1/x))`, then

\[
                         {\cal K}_\tau=x^{-o(1)}=o(1/x).       \tag{3.5}
\]

#### Proof

Fix one bite, let `Z_0` be its starting catalogue size, let `D<=Z_0/8`
be its total deletion, and let `P_i` be the number of rows removed before
cell `i`.  Because the remaining cells partition the as-yet-unremoved part
of the total deletion, their current cell size satisfies

\[
 |B_{j,i}|\le D-P_i\le {Z_0\over8}-P_i
              \le {1\over8}(Z_0-P_i).
\]

Since `Z_0-P_i=|C_{j,i-1}|`, this proves the sharper normalization

\[
                         \delta_{j,i}\le {1\over8}.           \tag{3.6}
\]

Apply (2.7) with `delta_0=1/8` to every cell and telescope first within
each bite and then through the bounded stopping time.  Since
`(1-1/8)^-2=64/49`, this is (3.4).  Equation (3.5) follows by
exponentiation because `x->0`.  `square`

Thus there are exactly two pathwise sources of large external collision:

1. the **signed term** `(E_{j,i})_+`, meaning that an actual blocker cell
   preferentially removes rows of below-average external-pair weight; and
2. the **quadratic term** `Q_{j,i}`, meaning that two rows in one blocker
   cell already have many common external windows.

No independence or regenerated snapshot has been used.

## 4. Capacity forcing and terminal-hole alignment

Let `H` be any target set of size `aN` and put

\[
 R_C(H)=\pi_C(H).                                   \tag{4.1}
\]

Cauchy--Schwarz on `H` and its complement gives the sharp inequality

\[
 \boxed{
 {\cal K}(C)\ge {R_C(H)^2\over a}
                  +{(1-R_C(H))^2\over1-a}.}        \tag{4.2}
\]

Equality holds exactly when `pi_C` is constant on each of the two cells.

Now fix a realized stopped trajectory and let `H` be its terminal hole
set at the tagged rank.  No accepted row has a window in `H`.  For every
first-blocker cell define its deleted Palm law `nu_{j,i}` by (2.8), and
put `R_{j,i}=pi_{j,i}(H)`.  Equation (2.9) gives the exact aggregate
hole transport

\[
 \boxed{
 R_{j,i+1}={R_{j,i}-\delta_{j,i}\nu_{j,i}(H)
                    \over1-\delta_{j,i}}.}          \tag{4.3}
\]

Whenever the terminal hole mass is positive, every preceding `R_{j,i}` is
positive, and hence

\[
 \boxed{
 \log{R_\tau(H)\over |H|/N}
 =\sum_{j<\tau}\sum_i
 \log{1-\delta_{j,i}\nu_{j,i}(H)/R_{j,i}
       \over1-\delta_{j,i}}.}                      \tag{4.4}
\]

This is the aggregate first-blocker version of the pointwise protection
identity.  It says that constant terminal Palm mass on an `x`-density hole
set requires `log(1/x)-O(1)` cumulative underexposure of that set in the
actual deletion cells.

For the punctured application, `N=B_q=(1-o(1))A` in the capacity band.  If
`g>=c_0xA` terminal holes satisfy the uniform-survivor floor

\[
                         \pi_\tau(T)\ge {1\over KxA},          \tag{4.5}
\]

then their Palm mass is at least `c_0/K+o(1)`.  Equations (4.2) and (3.4)
therefore imply

\[
 \boxed{
 \sum_{j<\tau}\sum_i{2(E_{j,i})_++Q_{j,i}\over S_{j,i}}
 \ge {49\over64}\bigl(\log(1/x)-O_{K,c_0}(1)\bigr).}         \tag{4.6}
\]

#### Proof

For (4.2), split `N sum pi(T)^2` over `H,H^c` and apply
Cauchy--Schwarz separately.  Equation (4.3) is (2.9) summed over the fixed
terminal set; telescoping its logarithm proves (4.4).  Under (4.5), the
hole Palm mass is at least

\[
                         {g\over KxA}\ge {c_0\over K}.
\]

Also `g<=KxA`, because the total Palm mass is at most one.  Hence
`a=g/N=Theta(x)`, and (4.2) gives `K_tau>=c/x` for a fixed positive
constant `c`.  Combine this with (3.4) and `K_0=1` to obtain (4.6).
`square`

The cell law also yields a useful exact `L^2` audit.  Put

\[
 \chi_{j,i}^2=N\sum_T(\pi_{j,i}(T)-\nu_{j,i}(T))^2.           \tag{4.7}
\]

Then

\[
 |R_{j,i}-\nu_{j,i}(H)|
 \le\sqrt{a\,\chi_{j,i}^2}.                         \tag{4.8}
\]

Indeed `|H|=aN`, so this is Cauchy--Schwarz.  Thus a proof of positive
alignment must create a large signed Palm--cell discrepancy; a proof of
small cumulative discrepancy rules it out.

## 5. Where punctured common-neighbour geometry enters

For a catalogue with conflict graph, define the `c`-weighted common closed
neighbourhood mass rooted at `G` by

\[
 J_C(G)=\sum_{F,H\in C}c(F,H)
       \mathbf1_{\{G\in\Gamma_C[F]\cap\Gamma_C[H]\}},         \tag{5.1}
\]

and its pair-biased mean common-blocker count by

\[
 I(C)={1\over S(C)}\sum_{G\in C}J_C(G)
 ={1\over S(C)}\sum_{F,H\in C}c(F,H)
                    |\Gamma_C[F]\cap\Gamma_C[H]|.             \tag{5.2}
\]

Because a first-blocker cell satisfies `B_{j,i} subseteq
Gamma_{C_{j,i-1}}[G_{j,i}]`, its quadratic charge obeys the exact
hereditary bound

\[
 \boxed{Q_{j,i}\le J_{C_{j,i-1}}(G_{j,i}).}         \tag{5.3}
\]

This is the promised use of common-neighbour geometry: it controls the
quadratic term in (3.4), with no independence assumption.  It says nothing
about the sign of `E_{j,i}`.

For completeness, consider the complete directed punctured catalogue on
`b=2r+1` labels and a shallow rank `2<=q<=sqrt(r)/4`.  Put

\[
 k=r-q,\quad N_q={b\choose k},\quad
 D_q=b\,k!(b-k)!,\quad D_M=2r\,r!(r+1)!.            \tag{5.4}
\]

For a fixed shallow target `T`, let `Omega_q(T)` be its `D_q`-row external
star.  Target and row transitivity give

\[
 I(C_0)=I_q={1\over D_q^2}\sum_{F,H\in\Omega_q(T)}
                 |\Gamma[F]\cap\Gamma[H]|.         \tag{5.5}
\]

The punctured boundary calculation gives the uniform estimate

\[
 \boxed{I_q\le {C\over r}D_M.}                     \tag{5.6}
\]

Here is a compact self-contained proof of the scale.  For a central target
`v`, let

\[
 w(v)=\Pr(v\in E(F)\mid F\hbox{ uniform in }\Omega_q(T)).     \tag{5.7}
\]

If a row `G` conflicts with `F`, their central decks meet, so the union
bound gives

\[
 {|\Gamma[G]\cap\Omega_q(T)|\over D_q}
 \le\sum_{v\in E(G)}w(v).                           \tag{5.8}
\]

Let `D=(d(v,u))` be the Gram matrix of central-target incidence, where
`d(v,u)` is the number of punctured rows containing both targets.  Swapping
the common blocker and the two external-star rows in (5.5) gives

\[
 I_q\le w^{\mathsf T}Dw.                            \tag{5.9}
\]

Every row has `4r` central targets, and every central target has degree at
most

\[
 D_L={r+2\over r}D_M.
\]

Thus every row sum of the positive semidefinite matrix `D` is at most
`4rD_L`, so `||D||<=4rD_L`.  If a central target has size
`h in {r-1,r}` and meets `T` in `a` points, exact cyclic interval counting
gives

\[
 w_h(a)={b-1\over b}
 {m_{k,h}(a)\over {k\choose a}{b-k\choose h-a}},    \tag{5.10}
\]

where

\[
 m_{k,h}(a)=
 \begin{cases}
 b-k-h+1,&a=0,\\
 2,&0<a<\min(k,h),\\
 |k-h|+1,&a=\min(k,h).
 \end{cases}                                        \tag{5.11}
\]

Consequently

\[
 ||w||_2^2=\left({b-1\over b}\right)^2
 \sum_{h\in\{r-1,r\}}\sum_a
 {m_{k,h}(a)^2\over {k\choose a}{b-k\choose h-a}}.            \tag{5.12}
\]

For `q>=3`, the two containment terms are respectively
`q^2/{r+1+q choose q-1}` and
`(q+1)^2/{r+1+q choose q}`, hence `O(r^-2)` uniformly in the stated
range.  The disjoint endpoints are smaller.  On the proper-overlap range,
use `{k choose a}>=k`, binomial unimodality, and

\[
 \sum_{j=q}^{r+1}{1\over{r+1+q\choose j}}
 \le {r+2+q\over{r+1+q\choose q}}                  \tag{5.13}
\]

to obtain another `O(r^-2)`.  Hence `||w||_2^2=O(r^-2)` and (5.6)
follows from (5.9).

For `q=2`, split off the lower containment vector `w_0`, supported on the
`r+3` lower supersets of `T` and constant there with value

\[
                         c_0={b-1\over b}{2\over r+3}.
\]

The remainder has squared norm `O(r^-2)`.  Two distinct such lower
supersets have punctured codegree

\[
                         2(2r-1)(r-2)!(r+1)!.
\]

Direct summation therefore gives

\[
 w_0^{\mathsf T}Dw_0={4\over r}D_M+O(D_M/r^2).      \tag{5.14}
\]

Positive-semidefinite Cauchy--Schwarz, together with
`||D||<=4rD_L`, bounds the remainder and cross term by `O(D_M/r)`, again
proving (5.6).

In the complete catalogue `W_C(F)=bD_q` is constant, so every deletion
cell has `E_B=0` before any earlier deletion has broken transitivity.  At
the standard singleton marking scale

\[
                         p={\gamma\over rD_M},
\]

the complete-state common-blocker forcing is therefore

\[
                         pI_q=O_\gamma(r^{-2}).      \tag{5.15}
\]

This is an actual infinitesimal statement about the first stopped state.
It must not be iterated through adaptive residuals: neither (5.6) at the
current average scale nor the vanishing of the signed term is hereditary.

## 6. A sharp obstruction to a common-neighbour-only proof

The signed term in (3.4) is indispensable, even when every closed
neighbourhood is a singleton.

Fix integers `N,L` and a set `H` of `h=xN` targets.  Take `b=1` and make
`L` labelled rows for every target, each row having that target as its sole
window.  Give the rows the empty conflict graph.  Initially

\[
                         X(T)=L,\qquad {\cal K}_0=1.            \tag{6.1}
\]

Delete, one singleton cell at a time, every row whose target is outside
`H`, and delete no row whose target lies in `H`.  This is a possible
realization of an isolated-mark process: in an empty graph every marked row
is accepted.  The deletions may be spread over as many rounds as necessary
so that every bite removes at most one eighth of its starting catalogue.

At the end,

\[
 \pi_\tau(T)={\mathbf1_H(T)\over h},\qquad
 {\cal K}_\tau={N\over h}={1\over x}.               \tag{6.2}
\]

The accepted rows hit every target outside `H` and none inside it, so `H`
is exactly the terminal hole set and `R_\tau(H)=1`.

Every cell has `Q_B=1`.  Throughout the deletion sequence

\[
 S(C)\ge hL^2=xNL^2.
\]

There are at most `NL` cells, and hence

\[
 \sum_B{Q_B\over S(C)}\le {1\over xL}.             \tag{6.3}
\]

Taking `L>>1/(x log(1/x))` makes the entire quadratic/common-blocker
budget `o(log(1/x))`, while (4.6) forces the signed budget to be
`Omega(log(1/x))`.  Thus even the strongest possible off-diagonal
common-neighbour bound cannot control Gate B without a stopped theorem for
the sign bias.  The example is not punctured geometry and is not claimed
to describe a typical punctured trajectory; it is a logical obstruction
to deleting the signed term from the proof.

## 7. Balanced adaptive reinforcement: exact LP and dual

The signed term suggests a deliberate modification of the bite: give larger
marking rates to rows whose closed neighbourhood has below-average
pair-endpoint weight.  This section gives the exact scalar-level switching
theorem and its obstruction.

Let `H` be a nonempty punctured residual.  Every configuration has
`k=2r` targets in each of the two central shores `V_M,V_L`.  Put

\[
 Z=|E(H)|,\qquad n_\sigma=|V_\sigma|,
 \qquad d(v)=|\{F:v\in F\}|.                       \tag{7.1}
\]

Give each surviving configuration `G` a rate `lambda_G>=0`, normalized by

\[
                         \sum_G\lambda_G=1.         \tag{7.2}
\]

Its target load is

\[
                         q_v=\sum_{G\ni v}\lambda_G.           \tag{7.3}
\]

Exact shorewise balance forces and is expressed by

\[
                         q_v={k\over n_\sigma}
                  \quad(v\in V_\sigma).            \tag{7.4}
\]

For rooted degree erosion define

\[
 P_{vG}={1\over d(v)}\sum_{F\ni v}(|F\cap G|-1)_+.             \tag{7.5}
\]

Let `M_v(t)` be the expected residual degree at `v`, conditional on `v`
surviving a singleton-rate bite of size `t`, and define the conditional
rooted erosion by

\[
                         e_v=-{d\over dt}\log M_v(t)\bigg|_{t=0}.
\]

The direct singleton-mark incidence expansion gives, under (7.4),

\[
 e_v=kq_M+kq_L-q_\sigma-\sum_GP_{vG}\lambda_G,
                         \qquad v\in V_\sigma.       \tag{7.6}
\]

Indeed `1_(|F cap G|>0)=|F cap G|-(|F cap G|-1)_+`.  Average this
identity first over `F ni v` and then over the mark `G`.  The first term
is `kq_M+kq_L`, and the duplicate term is (7.5).  Dividing the
unconditional expected degree by the survival probability of `v` adds
the conditional correction `-q_sigma`.  Thus rooted erosion is constant
on each shore precisely
when there are free numbers `rho_M,rho_L` such that

\[
 \sum_GP_{vG}\lambda_G=\rho_\sigma
                         \quad(v\in V_\sigma).       \tag{7.7}
\]

Let `Gamma[G]` be the current closed conflict neighbourhood and define

\[
 C_G=|\Gamma[G]|,qquad
 Y_G(T)=|\Gamma[G]\cap\mathcal S(T)|,               \tag{7.8}
\]

\[
 R_G=\sum_TX(T)Y_G(T),\qquad Q_G=\sum_TY_G(T)^2.    \tag{7.9}
\]

The singleton collision-gain coefficient is

\[
 \boxed{
 g_G={2C_G\over Z}-{2R_G-Q_G\over S}
 =2\left({C_G\over Z}-{R_G\over S}\right)+{Q_G\over S}.}     \tag{7.10}
\]

The first signed summand is positive exactly when

\[
                         {R_G\over C_G}<{S\over Z},            \tag{7.11}
\]

so (7.10) formalizes the proposed bias toward a closed neighbourhood of
below-average pair-endpoint weight.

### Theorem 7.1 (balanced collision-reinforcement LP)

Mark `G` independently with probability `t lambda_G`, accept isolated
marks, and delete their closed neighbourhoods.  Let `z(t)` and `s(t)` be
the expected residual catalogue size and expected residual pair mass, and
put `overline K(t)=Ns(t)/(b^2z(t)^2)`.  Then

\[
 \boxed{
 {d\over dt}\log\overline{\cal K}(t)
 \bigg|_{t=0}=\sum_Gg_G\lambda_G.}                 \tag{7.12}
\]

At `t=0` every nonempty marking pattern of first order is a singleton.  The
optimal
simultaneously load-balanced and erosion-balanced reinforcement is the
finite linear program

\[
 \boxed{
 \begin{aligned}
 \mathfrak G(H)=\max\quad&\sum_Gg_G\lambda_G,\\
 \text{subject to}\quad
 &\lambda_G\ge0,\\
 &\sum_{G\ni v}\lambda_G={k\over n_\sigma}
                                  &&(v\in V_\sigma),\\
 &\sum_GP_{vG}\lambda_G=\rho_\sigma
                                  &&(v\in V_\sigma),
 \end{aligned}}                                                   \tag{7.13}
\]

where `rho_M,rho_L` are free.  If the feasible set is nonempty, strong LP
duality gives

\[
 \boxed{
 \mathfrak G(H)=\min_{y,z}
 \sum_{\sigma\in\{M,L\}}{k\over n_\sigma}
                         \sum_{v\in V_\sigma}y_v,}              \tag{7.14}
\]

where the minimum is over real `y_v,z_v` satisfying

\[
 \sum_{v\in V_\sigma}z_v=0\quad(\sigma=M,L),       \tag{7.15}
\]

\[
 \sum_{v\in G}y_v+\sum_vz_vP_{vG}\ge g_G
                         \quad(G\in E(H)).          \tag{7.16}
\]

#### Proof

With one marked row `G`, the catalogue loses `C_G` rows and pair mass
`2R_G-Q_G`, by Theorem 2.1.  Therefore

\[
 Z'(0)=-\sum_G\lambda_GC_G,qquad
 S'(0)=-\sum_G\lambda_G(2R_G-Q_G).
\]

Logarithmically differentiate `K=NS/(b^2Z^2)` to obtain (7.12) and
(7.10).  Equations (7.4) and (7.7) give (7.13).

For the dual, attach `y` to the load equations and `z` to the erosion
equations.  The free shore variables `rho_sigma` force (7.15).  Boundedness
of the maximization over every nonnegative `lambda_G` forces (7.16), and
the remaining dual objective is the right side of (7.14).  Finite
linear-programming duality proves equality.  `square`

The quantity in (7.12) is deliberately a ratio of first moments, not the
expectation of a random ratio.  For a finite bite,
simultaneous marks and overlapping neighbourhoods create the nonlinear
first-blocker terms of Sections 2--3; a positive LP value cannot simply be
multiplied by a finite step without bounding those errors.

The dual gives an exact switching test.  For any threshold `eta`, either a
feasible rate law has collision derivative at least `eta`, or a pair
`(y,z)` satisfying (7.15)--(7.16) has objective below `eta`.  This is
checkable on the current residual and uses no reference snapshot.

### Proposition 7.1a (row-hazard compensation forces quadratic drift)

There is a particularly transparent sufficient system.  Suppose a rate
law `lambda` and a number `c in [0,1)` satisfy

\[
 \boxed{
 \sum_{G:F\in\Gamma[G]}\lambda_G=c
                         \qquad(F\in C).}           \tag{7.17a}
\]

Thus a row sampled uniformly from the current catalogue has the same
probability `c` of belonging to the selected blocker's cell, regardless of
the row.  Select one blocker `G` with law `lambda` and delete `Gamma[G]`.
For the resulting random `Z',S'`,

\[
 \boxed{
 \mathbb EZ'=Z(1-c),\qquad
 \mathbb ES'=S(1-c)^2+\sum_T
                 \operatorname {Var}_\lambda Y_G(T).}         \tag{7.17b}
\]

Consequently

\[
 \boxed{
 {N\mathbb ES'\over b^2(\mathbb EZ')^2}
 =\mathcal K+
 {N\sum_T\operatorname {Var}_\lambda Y_G(T)
       \over b^2Z^2(1-c)^2}\ge\mathcal K.}          \tag{7.17c}
\]

#### Proof

Summing (7.17a) over `F` gives
`sum_G lambda_G C_G=cZ`.  For every target,

\[
 \mathbb E_\lambda Y_G(T)
 =\sum_{F\in\mathcal S(T)}
        \sum_{G:F\in\Gamma[G]}\lambda_G=cX(T).     \tag{7.17d}
\]

Therefore `E R_G=cS`, while

\[
 \mathbb E Q_G=\sum_T\mathbb EY_G(T)^2
 =c^2S+\sum_T\operatorname {Var}Y_G(T).
\]

Insert these identities into `Z'=Z-C_G` and
`S'=S-2R_G+Q_G`.  This proves (7.17b)--(7.17c).  `square`

Equation (7.17a) is itself a finite linear feasibility problem and can be
intersected with either the exact balance constraints (7.13) or the
compensated constraints (7.23a).  It kills the signed endpoint bias
identically in first moments; all remaining collision gain is the explicit
common-blocker variance in (7.17b).  Uniform rates satisfy it whenever the
current conflict graph is closed-neighbourhood regular.  No hereditary
feasibility claim is made for adaptive punctured residuals.

### Theorem 7.2 (canonical balanced Gibbs switching)

Assume the feasible polytope in (7.13) contains a rate law
`lambda^0` which is positive on every edge not forced to zero.  For
`theta>=0`, let `lambda^theta` be the unique maximizer over that polytope
of

\[
 \theta\sum_Gg_G\lambda_G
 -D(\lambda\Vert\lambda^0),
 \qquad
 D(\lambda\Vert\lambda^0)
 =\sum_G\lambda_G\log{\lambda_G\over\lambda_G^0}.             \tag{7.18}
\]

Then `lambda^theta=lambda^0` at `theta=0`, every `lambda^theta` preserves
the central load and rooted-erosion constraints, and

\[
                         \theta\longmapsto
 \sum_Gg_G\lambda_G^\theta                         \tag{7.19}
\]

is nondecreasing.  As `theta->infinity`, every limit point is an optimizer
of (7.13).  Hence if `mathfrak G(H)>0`, a sufficiently strong balanced
Gibbs tilt gives rigorously positive singleton collision drift.

#### Proof

Relative entropy is strictly convex on the support of `lambda^0`, so the
objective in (7.18) is strictly concave on the compact feasible polytope
and has a unique maximizer.  At `theta=0`, relative entropy is uniquely
minimized by `lambda^0`.  If `theta_2>theta_1`, optimality at the two
parameters gives

\[
 \theta_2g\mathbin\cdot\lambda^{\theta_2}
 -D(\lambda^{\theta_2}\Vert\lambda^0)
 \ge\theta_2g\mathbin\cdot\lambda^{\theta_1}
 -D(\lambda^{\theta_1}\Vert\lambda^0),
\]

and the reverse inequality with `theta_1` and its optimizer.  Adding them
gives

\[
 (\theta_2-\theta_1)
 g\mathbin\cdot(\lambda^{\theta_2}-\lambda^{\theta_1})\ge0,
\]

which proves (7.19).  Divide the optimality inequality by `theta` and let
`theta` tend to infinity.  Compactness shows that every limit point
maximizes `g dot lambda`.  `square`

There is an exact hole-support version.  For a current candidate hole set
\(\mathcal H\) with \(X_{\mathcal H}>0\), put

\[
 X_{\mathcal H}=\sum_{T\in\mathcal H}X(T),
 \qquad
 M_G(\mathcal H)=\sum_{F\in\Gamma[G]}|W(F)\cap\mathcal H|,    \tag{7.20}
\]

and

\[
 h_G(\mathcal H)={C_G\over Z}
                 -{M_G(\mathcal H)\over X_{\mathcal H}}.     \tag{7.21}
\]

Restrict (7.13) further by

\[
 \lambda_G=0\quad\hbox{whenever }W(G)\cap\mathcal H\ne\varnothing.    \tag{7.22}
\]

Thus no marked singleton directly hits \(\mathcal H\).  If the restricted
polytope is nonempty, then

\[
 \boxed{
 {d\over dt}\log {\mathbb E X_{\mathcal H}(t)
                         \over b\,\mathbb E Z(t)}\bigg|_{t=0}
 =\sum_Gh_G(\mathcal H)\lambda_G.}                 \tag{7.23}
\]

Indeed a singleton `G` removes `C_G` rows and exactly
\(M_G(\mathcal H)\) incidences with the candidate support.  The same LP-dual
and Gibbs-tilt proof, with objective \(h_G(\mathcal H)\) and support
restriction (7.22), gives a canonical balanced rate law maximizing
first-order Palm protection while creating no direct hit.  This is a
genuine positive scalar-level switching theorem.  It does not assert that
the restricted polytope is nonempty or that the finite-bite errors are
summable.

### Proposition 7.2a (balanced hole protection is exactly duplicate bias)

The target-load equations cancel the entire marginal part of the
hole-support objective.  Put

\[
 s_{\mathcal H}(F)=|W(F)\cap\mathcal H|,
 \qquad
 D(F,G)=(|F\cap G|-1)_+,                            \tag{7.23f}
\]

\[
 D_0(G)=\sum_FD(F,G),
 \qquad
 D_{\mathcal H}(G)=\sum_Fs_{\mathcal H}(F)D(F,G).  \tag{7.23g}
\]

If `lambda` satisfies the shorewise target loads (7.4), then

\[
 \boxed{
 \sum_G\lambda_Gh_G(\mathcal H)
 =\sum_G\lambda_G\left{
 {D_{\mathcal H}(G)\over X_{\mathcal H}}
 -{D_0(G)\over Z}\right}.}                       \tag{7.23h}
\]

Consequently, if every row allowed by the no-hit restriction (7.22)
satisfies

\[
                         {D_{\mathcal H}(G)\over X_{\mathcal H}}
 \le {D_0(G)\over Z},                              \tag{7.23i}
\]

then no target-load-balanced independent-rate law supported on those rows
has positive first-order Palm-protection drift.

#### Proof

For `t=|F cap G|`, the identity
`1_(t>0)=t-(t-1)_+` gives

\[
 C_G=\sum_{v\in G}d(v)-D_0(G),                     \tag{7.23j}
\]

and, after weighting row `F` by `s_mathcal H(F)`,

\[
 M_G(\mathcal H)=\sum_{v\in G}a_v(\mathcal H)
                         -D_{\mathcal H}(G),
 \qquad
 a_v(\mathcal H)=\sum_{F\ni v}s_{\mathcal H}(F).  \tag{7.23k}
\]

Average the first identity under `lambda`.  Since every shore has edge
uniformity `k` and load `k/n_sigma`,

\[
 {1\over Z}\sum_vq_vd(v)
 =k^2\left({1\over n_M}+{1\over n_L}\right).       \tag{7.23l}
\]

For the second identity, each row contributes its score to exactly `k`
targets per shore, so

\[
 \sum_{v\in V_\sigma}a_v(\mathcal H)=kX_{\mathcal H}.
\]

Therefore

\[
 {1\over X_{\mathcal H}}\sum_vq_va_v(\mathcal H)
 =k^2\left({1\over n_M}+{1\over n_L}\right).       \tag{7.23m}
\]

The two marginal terms (7.23l)--(7.23m) cancel in
`sum_G lambda_G(C_G/Z-M_G/X_mathcal H)`, leaving (7.23h).  Equation
(7.23i) then makes every remaining summand nonpositive.  `square`

This is the exact obstruction faced by a balanced reserve/vortex rule.
Pair-endpoint inverse weighting is useful only if the actual punctured
residual develops positive **hole-weighted duplicate bias**.  Static
central-load balance, marginal external degrees, and the first-blocker
common-neighbour count do not create that sign.

### Theorem 7.3 (compensated pair-endpoint inverse weighting)

Exact shorewise balance is stronger than necessary for perturbing the
existing uniform bite.  There is an always-feasible compensated version
which preserves *all* singleton target loads and rooted duplicate exposures
of a chosen baseline law.

Let `lambda^0` be any positive baseline rate law; in particular one may
take the uniform law `lambda_G^0=1/Z`.  Let `A_(vG)=1_(v in G)`, and form
the matrix `B` by stacking the target-incidence matrix `A` and the rooted
exposure matrix `P` from (7.5).  Define

\[
 \Lambda_{\rm comp}(\lambda^0)
 =\{\lambda\ge0:B\lambda=B\lambda^0\}.             \tag{7.23a}
\]

Normalization is automatic from the incidence rows, because every column
of `A` has the same total `2k`.  Thus (7.23a) is a nonempty compact
probability polytope.  Every one of its laws has exactly the same target
loads and the same values `sum_G P_(vG)lambda_G` as the baseline.

For either the singleton tangent objective `f_G=g_G`, the exact cell
objective `f_G=ell_G`, or any other current scalar, let

\[
 \lambda^\theta
 =\arg\max_{\lambda\in\Lambda_{\rm comp}(\lambda^0)}
 \left\{\theta\sum_Gf_G\lambda_G
              -D(\lambda\Vert\lambda^0)\right\}.   \tag{7.23b}
\]

Then `lambda^theta=lambda^0` at `theta=0`, and

\[
                         \theta\longmapsto
                         \sum_Gf_G\lambda_G^\theta             \tag{7.23c}
\]

is nondecreasing.  It is strictly increasing at zero unless `f` belongs
to the row space of `B`.  More exactly, if
`dot lambda=(d/dtheta)lambda^theta|_(theta=0)`, then

\[
 \boxed{
 {d\over d\theta}\sum_Gf_G\lambda_G^\theta\bigg|_{\theta=0}
 =\sum_G{(\dot\lambda_G)^2\over\lambda_G^0}\ge0.}             \tag{7.23d}
\]

The limiting compensated optimum has the exact dual

\[
 \boxed{
 \max_{\lambda\in\Lambda_{\rm comp}(\lambda^0)}f\mathbin\cdot\lambda
 =\min_{y:B^{\mathsf T}y\ge f}(B\lambda^0)\mathbin\cdot y.}   \tag{7.23e}
\]

#### Proof

The monotonicity proof is the same two-optima argument as in Theorem 7.2.
For the strict statement, differentiate the Lagrange equations for
(7.23b) at zero.  This differentiation is legitimate because
`lambda^0_G>0` for every column: it lies in the relative interior of the
affine feasible polytope, so the nonnegativity constraints remain inactive
for all sufficiently small `theta`.  For some multiplier vector `xi`,

\[
 {\dot\lambda_G\over\lambda_G^0}=f_G+(B^{\mathsf T}\xi)_G,
 \qquad B\dot\lambda=0.
\]

Multiply by `dot lambda_G` and sum.  The multiplier term vanishes, giving
(7.23d).  It is zero exactly when `dot lambda=0`, equivalently when `f`
is in the row space of `B` (a constant is already in that row space by
the equal column sums of `A`).  Finally (7.23e) is the ordinary finite LP
dual of (7.23a).  `square`

Thus compensated pair-endpoint inverse weighting has an exact dichotomy:
it gives a strict improvement over the uniform stopped-law drift whenever
the desired scalar has a component invisible to the central load/exposure
constraints, and it is provably powerless precisely when the scalar lies
in their dual row space.  Unlike (7.13), this compensated polytope is never
empty.

For a preselected hole support, use any positive baseline law supported on
rows avoiding that support and apply the same construction inside those
columns.  This preserves that baseline's central loads and cannot create a
direct hit.  The missing existence statement is now sharper: construct
such a supported baseline with acceptable Gate-A loads, then prove that
the exact hole-protection scalar (7.26) has a cumulatively large component
outside the corresponding row space.

### Proposition 7.3a (the puncture-averaged `C_8` seed is exposure-detected)

There is a useful exact warning about how Theorem 7.3 must be used.  Put
`n=2r+1`, choose distinct labels `a,b,c,d`, and let

\[
 P=(p_1,\ldots,p_{r-1}),\qquad Q=(q_1,\ldots,q_{r-2})
\]

be disjoint ordered words on the other labels.  Regard

\[
\begin{array}{ll}
 R_0=a\,b\,P\,c\,d\,Q,&R_1=c\,a\,P\,d\,b\,Q,\\
 S_0=a\,c\,P\,b\,d\,Q,&S_1=b\,a\,P\,d\,c\,Q
\end{array}                                                   \tag{7.23n}
\]

as cyclic words, and write
`t=[S_0]+[S_1]-[R_0]-[R_1]`.  Let `tau_P` reverse the labels of `P`,
so `tau_P(p_i)=p_(r-i)`, and fix every other label.  Then

\[
                         t^*=t+\tau_Pt                         \tag{7.23o}
\]

has zero complete rank-`r` and rank-`(r-1)` window ledgers.  For `r>=4`
its complete rank-`(r-2)` ledger is nonzero; explicitly it is twice

\[
 -[\{b\}\cup\operatorname {pre}_{r-3}Q]
 -[\{c\}\cup\operatorname {suf}_{r-3}Q]
 +[\{c\}\cup\operatorname {pre}_{r-3}Q]
 +[\{b\}\cup\operatorname {suf}_{r-3}Q].          \tag{7.23p}
\]

For each cyclic word in `t^*`, now sum its directed punctured
configuration over all `n` possible puncture origins; call the resulting
signed configuration vector `delta`.  Then

\[
                         A\delta=0,                 \tag{7.23q}
\]

while its full-row rank-`(r-2)` current is `n` times (7.23p).

At `r=4`, however, this direction is not in `ker P`.  More sharply, work
in the complete directed punctured catalogue on nine labels and use the
unnormalized exposure

\[
 \widetilde P_{vG}=d(v)P_{vG}
   =\sum_{F\ni v}(|F\cap G|-1)_+.                  \tag{7.23r}
\]

Every full-catalogue degree `d(v)` is positive, so row scaling from `P`
to `widetilde P` changes neither its kernel nor any compensated
feasibility statement.

For a function `z` on `k`-sets define

\[
 (\partial_{k\to2}z)(U)=
       \sum_{\substack{v\supseteq U\\|v|=k}}z(v).             \tag{7.23s}
\]

Take, without loss of generality,

\[
 (a,b,c,d)=(0,1,2,3),\quad P=(4,5,6),\quad Q=(7,8),
\]

and let `J` be the unpunctured rank-two current of `t^*`.  Thus

\[
                         J=2(-[17]+[18]+[27]-[28]).            \tag{7.23t}
\]

Here, for example, `[17]` denotes the basis vector of the unordered pair
`{1,7}`.

The exact complete-catalogue identities are

\[
 \boxed{
 \partial_{4\to2}(\widetilde P\delta)_M=425J,
 \qquad
 \partial_{3\to2}(\widetilde P\delta)_L=8832J.}              \tag{7.23u}
\]

Equivalently, if `Q_2 delta=9J` denotes its full-row rank-two current,
the two factors in (7.23u) are `425/9` and `2944/3` relative to
`Q_2 delta`.  Consequently every rational combination of label translates

\[
                         \Delta=\sum_{g\in S_9}c_g\,g\delta    \tag{7.23v}
\]

satisfies

\[
                         P\Delta=0\quad\Longrightarrow\quad
                         Q_2\Delta=0.                          \tag{7.23w}
\]

This is an obstruction only to this single orbit module, not to the full
compensated polytope.

#### Proof

Index starts by `0,...,2r`.  The rank-`r` windows of `R_0` have the
following literal partners:

\[
\begin{array}{c|c}
\text{start in }R_0&\text{equal window in the positive shore}\\ \hline
0&S_1/0\\
1&S_0/2\\
2&S_0/1\\
3\le i\le r+1&S_1/i\\
r+2&S_0/(r+2)\\
r+3\le i\le2r&S_1/i.
\end{array}                                                   \tag{7.23aa}
\]

The table for `R_1` is obtained by interchanging `S_0,S_1`; its starts
are again disjoint and exhaustive.  This proves the zero rank-`r` ledger.
At rank `r-1`, cancellation of all internal windows leaves

\[
 -[\{b\}\cup(P-\{p_{r-1}\})]
 -[\{c\}\cup(P-\{p_1\})]
 +[\{c\}\cup(P-\{p_{r-1}\})]
 +[\{b\}\cup(P-\{p_1\})].                         \tag{7.23x}
\]

Reversing `P` negates (7.23x), proving rank-`(r-1)` cancellation in
`t^*`; it does not affect the already zero rank-`r` ledger.  At rank
`r-2`, the same boundary enumeration has one square on the `P` boundaries
and the square (7.23p) on the `Q` boundaries.  Reversal negates the first
and fixes the second, leaving twice (7.23p).  Its four sets are distinct
for `r>=4`, so it is nonzero.

Across all `n` puncture origins, every complete rank-`r` or rank-`(r-1)`
window is omitted once and retained `n-1` times.  This proves (7.23q).
The full-row external deck is independent of the puncture origin and is
therefore multiplied by `n`.

It remains only to audit the finite constants in (7.23u).  They admit the
following complete four-entry certificate; every unlisted pair has value
zero:

\[
\begin{array}{c|rrrr}
 U&17&18&27&28\\ \hline
 J(U)&-2&2&2&-2\\
 \partial_{4\to2}(\widetilde P\delta)_M(U)
      &-850&850&850&-850\\
 \partial_{3\to2}(\widetilde P\delta)_L(U)
      &-17664&17664&17664&-17664.
\end{array}                                                   \tag{7.23y}
\]

For completeness, (7.23y) is obtained directly from (7.23r): enumerate
the `9!` labelled configurations `F`, form the retained eight rank-four
and eight rank-three targets of each, add
`(|F cap G|-1)_+` at every retained root `v`, and sum with the `72`
signed coefficients of `delta`.  This is an exhaustive finite sum, not a
sampling calculation; the companion verifier performs these integer
operations and checks all `36` pair coordinates.  Equation (7.23u)
follows from the table.  Both `partial` and `widetilde P` commute with
label permutations, so applying (7.23u) to (7.23v) proves (7.23w).
`square`

There is an even more local certified obstruction at the complete state.
Restrict the support of a signed perturbation to the `72` distinct directed
configurations underlying this one seed (eight words and nine origins),
while retaining the complete-catalogue exposure matrix (7.23r).  Modular
Gaussian elimination over the prime `1000003` gives

\[
 \operatorname {rank}_{\mathbb F_{1000003}}A=35,
 \qquad
 \operatorname {rank}_{\mathbb F_{1000003}}
                  \binom A{\widetilde P}=72.                 \tag{7.23z}
\]

The second rank equals the number of columns; a nonzero minor modulo a
prime is a nonzero integer minor.  Hence no nonzero signed perturbation
supported on this local bank preserves both central incidences and rooted
exposures.  The exact verifier for (7.23y)--(7.23z) is
`scratch/verify_gate_b_first_blocker_collision_budget_20260822.py`.

### Theorem 7.4 (exact single-cell compensators)

The finite-bite error disappears completely if the weighted process is run
as an adaptive single-cell process.  At state `C_n`, choose one current row
`G_n` from an `F_n`-measurable law `lambda_n`, accept it, and delete its
closed neighbourhood.  This is the zero-simultaneity limit of independent
exponential marking clocks; every selected mark is isolated, and the
accepted rows form a matching.

For a candidate row `G`, compute `u_G,omega_G,chi_G` from its full current
cell `Gamma[G]` by

\[
 u_G={C_G\over Z},\qquad
 \omega_G={R_G\over S},\qquad
 \chi_G={Q_G\over S},
\]

and put

\[
 \ell_G=\log\left(
 1+{\chi_G+2(u_G-\omega_G)-u_G^2\over(1-u_G)^2}
              \right).                              \tag{7.24}
\]

Stop before a cell empties the catalogue.  Then

\[
 \boxed{
 \log{{\cal K}_n\over{\cal K}_0}
 -\sum_{a<n}\sum_G\lambda_a(G)\ell_{a,G}}          \tag{7.25}
\]

is a martingale.  This is an exact finite compensator, not a tangent.

For a fixed candidate hole set \(\mathcal H\), restrict every `lambda_n` to
rows having no window in \(\mathcal H\).  Put

\[
 a_G(\mathcal H)={M_G(\mathcal H)\over X_{\mathcal H}},
 \qquad
 \ell_G(\mathcal H)=\log{1-a_G(\mathcal H)\over1-u_G}.        \tag{7.26}
\]

Stop before \(X_{\mathcal H}\) becomes zero.  If
\(R_n(\mathcal H)=\pi_n(\mathcal H)\), then

\[
 \boxed{
 \log{R_n(\mathcal H)\over R_0(\mathcal H)}
 -\sum_{a<n}\sum_G\lambda_a(G)\ell_{a,G}(\mathcal H)}        \tag{7.27}
\]

is also a martingale.  Moreover every member of \(\mathcal H\) is unhit
throughout the process.

#### Proof

Conditional on `F_n`, the only randomness is `G_n`.  Theorem 2.1 says its
literal increment of `log K` is (7.24), so subtracting its conditional
mean proves (7.25).  For the fixed support, one cell changes its total
window incidence and catalogue size by

\[
 X_{\mathcal H}'=X_{\mathcal H}-M_G(\mathcal H),
 \qquad Z'=Z-C_G.
\]

Since \(R=X_{\mathcal H}/(bZ)\), its literal logarithmic increment is
(7.26),
which proves (7.27).  The support restriction prevents every accepted row
from containing a member of \(\mathcal H\).  `square`

There is a useful high-probability form requiring no general martingale
black box.  Suppose a selected objective `Y_n` is either `ell_(n,G_n)` or
`ell_(n,G_n)(mathcal H)`, and the rate law is supported where

\[
                         0\le Y_n\le c.             \tag{7.28}
\]

Put `mu_n=E(Y_n|F_n)`.  For every bounded stopping time and
`0<delta<1`, on any event where `sum_(n<tau)mu_n>=L`,

\[
 \boxed{
 \Pr\left(\sum_{n<\tau}Y_n\le(1-\delta)L,
           \ \sum_{n<\tau}\mu_n\ge L\right)
 \le\exp\left[-{L\over c}
 \{\delta+(1-\delta)\log(1-\delta)\}\right].}     \tag{7.29}
\]

Indeed convexity of `exp(-theta y)` on `[0,c]` gives

\[
 \mathbb E(e^{-\theta Y_n}\mid\mathcal F_n)
 \le1-{1-e^{-\theta c}\over c}\mu_n
 \le\exp\left(-{1-e^{-\theta c}\over c}\mu_n\right).
\]

Multiply these conditional inequalities, stop, and optimize at
`theta=c^{-1}log(1/(1-delta))` to obtain (7.29).
Formally, replace `Y_n,mu_n` by
`1_(n<tau)Y_n,1_(n<tau)mu_n`; since `{n<tau}` is `F_n`-measurable for a
stopping time, the same conditional inequality applies and makes the
stopped product argument literal.

For collision gain, deletion can only decrease `S`, so every nonnegative
increment satisfies

\[
                         0\le\ell_G\le-2\log(1-u_G).            \tag{7.30}
\]

For hole protection, \(a_G(\mathcal H)\ge0\), so the same argument gives
\(0\le\ell_G(\mathcal H)\le-\log(1-u_G)\) on its nonnegative support.  Hence a
uniform current cell bound `u_G<=epsilon<1/2` allows `c=4epsilon` in
(7.29).

This yields a literal positive switching criterion.  If at every state one
of the balanced polytopes is nonempty after restricting to nonnegative
exact increments, use its Gibbs tilt or exact LP optimizer.  If the
resulting predictable gain before the stopping density is
`(1+Omega(1))log(1/x)` and `epsilon=o(log(1/x))`, then (7.29) forces the
realized gain above `log(1/x)-O(1)` with probability `1-o(1)`.  For the
hole-support objective, an initial `Theta(x)` Palm mass therefore becomes
`Omega(1)` while all of its targets remain holes.  What is not proved is
that these positive-support balanced polytopes remain nonempty or have the
required cumulative objective in the punctured trajectory.

### Proposition 7.5 (no hereditary balanced-reinforcement theorem)

For every `r>=3` there is an induced punctured residual for which the
feasible set in (7.13) is empty.

#### Proof

On `Omega={0,1,...,2r}`, read subscripts modulo `b=2r+1` and define

\[
 I_h^u(s)=\{u_s,u_{s+1},\ldots,u_{s+h-1}\},
\]

\[
 E(u)=\{(M,I_r^u(s)):1\le s\le2r\}
 \mathbin{\dot\cup}
 \{(L,I_{r-1}^u(s)):1\le s\le2r\}.
\]

Let

\[
 w=(0,1,\ldots,2r-2,2r-1,2r),
 \qquad
 w'=(0,1,\ldots,2r-2,2r,2r-1).                    \tag{7.31}
\]

Retain exactly the central targets in `U=E(w) union E(w')`.  Write
`M_s=I_r^w(s)` and `L_s=I_(r-1)^w(s)`, with primes for `w'`.
Swapping the adjacent letters `2r-1,2r` changes a cyclic interval exactly
when it contains one but not the other.  Reading its two boundary cuts
shows that the only changed targets are

\[
                         M_r,M_{2r},L_{r+1},L_{2r},             \tag{7.32}
\]

and their four primed replacements.  Thus the two configurations have
`2r-2` common targets and two private targets on each shore.

It remains to check that `U` induces no third configuration.  The
containment graph of every punctured configuration is the canonically
oriented alternating path

\[
 L_1-M_1-L_2-M_2-\cdots-L_{2r}-M_{2r}.             \tag{7.33}
\]

Direct deletion of one point from the sets in (7.32) shows that the
containment graph induced by `U` has the common initial path through
`L_r`, two internally disjoint length-two branches

\[
                         L_r-M_r-L_{r+1}-M_{r+1},
 \qquad
                         L_r-M'_r-L'_{r+1}-M_{r+1},             \tag{7.34}
\]

then the common path through `M_(2r-1)`, and the two terminal tails

\[
                         M_{2r-1}-L_{2r}-M_{2r},
 \qquad
                         M_{2r-1}-L'_{2r}-M'_{2r}.              \tag{7.35}
\]

There are no other containment edges: compare each exceptional lower set
in (7.32) with the listed middle sets; every unlisted comparison differs in
at least two labels.  A candidate (7.33) uses `2r` targets on each shore,
so it omits four vertices of the `4r+4`-vertex union graph.  That graph has
leaves `L_1,M_(2r),M'_(2r)`, degree-three vertices
`L_r,M_(r+1),M_(2r-1)`, and degree two everywhere else.  Propagate the
degree-two requirement of an induced spanning path inward from the three
leaves.  At each of the three degree-three junctions exactly one of the two
parallel continuations must be discarded; the shore counts then force the
omitted four vertices to be one complete two-vertex branch of (7.34) and
one complete two-vertex tail of (7.35).  Conversely each of the four
branch--tail choices leaves an induced alternating path.

Only the two unmixed choices are genuine cyclic-window paths.  For a word
`u`, the oriented same-start pairs satisfy

\[
                         M_s\setminus L_s=\{u_{s+r-1}\}
                         \qquad(1\le s\le2r).        \tag{7.36}
\]

The common pairs plus the chosen branch reconstruct every word position
except `r-1`, and the unique unused label reconstructs that position.  The
unprimed branch reconstructs `w`, whereas the primed branch reconstructs
`w'`; their required terminal tails are respectively unprimed and primed.
The two mixed choices therefore contradict their reconstructed word.
Hence the residual induced by `U` has exactly the two edges `E(w),E(w')`.

In each central shore the two edges have `2r-2` common targets and two
private targets apiece.  If their rates are `lambda,mu`, the loads on a
common, `w`-private, and `w'`-private target are respectively

\[
                         \lambda+\mu,\qquad\lambda,\qquad\mu.
\]

Shorewise equality forces `lambda=mu=0`, contradicting normalization.
Thus even the load equations in (7.13) are infeasible.  `square`

Proposition 7.5 does not say that the actual descent reaches this residual:
choosing either edge covers all but four of its targets.  It proves the
precise limitation of the reinforcement proposal.  A successful switching
algorithm must prove a history invariant excluding such dual obstructions,
or use their support as a priority-cleanup family with negligible global
cost.  There is no rate-selection theorem valid for every induced
punctured residual.

## 8. Exact remaining adaptive theorem

Define on the actual stopped punctured trajectory

\[
 \Phi_{\rm sign}=\sum_{j<\tau}\sum_i{(E_{j,i})_+\over S_{j,i}},
 \qquad
 \Phi_{\rm cb}=\sum_{j<\tau}\sum_i{Q_{j,i}\over S_{j,i}}.     \tag{8.1}
\]

The proved conclusions are now exact:

* `Phi_sign+Phi_cb=o(log(1/x))` implies
  `K_tau=o(1/x)`, ruling out the full-survivor Gate-B route;
* a capacity-sized successful full-survivor cover forces
  `2Phi_sign+Phi_cb=Omega(log(1/x))`; and
* the punctured complete-state common-neighbour calculation supplies only
  the initial scale `pI_q=O(r^-2)`.  It does not bound either stopped sum.

The smallest missing negative theorem is therefore stopped summability of
both quantities in (8.1), or a direct current-scale estimate implying it.
The smallest missing positive theorem is the opposite: prove that the
signed deletion bias builds logarithmic mass and that its high-Palm tail is
the terminal hole set.  The accepted-hit likelihood remains an additional
constraint on that positive alternative.

Accordingly, the new pair-potential identities do not yet select the
full-survivor route or the hole-biased/long-arc route.  They do prove that
static punctured common-neighbour geometry alone cannot make the
selection: the adaptive signed endpoint-mixing term is a genuinely
separate stopped statistic.
