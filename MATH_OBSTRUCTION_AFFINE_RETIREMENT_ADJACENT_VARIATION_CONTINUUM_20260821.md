# The affine proportional prefix envelope has a positive adjacent-variation continuum obstruction

**Status (2026-08-21).**  The theorem below is proved.  It disproves the
proposed estimate

\[
 \mathcal A_1=O(HW_b/b)
\]

for the proportional densities of the half-step affine schedule.  In fact,
already for `H>=1.51 sqrt(b)`,

\[
 \liminf_{b\to\infty}{\mathcal A_1\over W_b}>0.              \tag{0.1}
\]

Consequently the explicit prefix-envelope retirement point
`x_i(q)=a_i min_(j<=q) rho_(j,s_i(j))` loses `Omega(W_b)` mass.  This is an
obstruction to that witness, **not** an obstruction to the retirement LP:
a different fractional retirement point may still have `o(W_b)` deficit.

The mechanism is a parity-scale lattice term in the exact affine window
histogram.  It survives on a positive two-dimensional continuum of
completely ordinary alternating transitions; it is not caused by the rare
equal-letter defect pairs.

## 1. Notation and the selected transition class

Write

\[
 b=2h+1,\qquad c_j={b\choose h+1+j},\qquad L_j=c_j^2,
 \qquad W_b={2b\choose b}.                           \tag{1.1}
\]

We use the half-step affine schedule

\[
 R(x)=hx\pmod b,\qquad P_r=\{x:R(x)<r\}.             \tag{1.2}
\]

The source of upper distance `k` has split `r=h+1+k`, and one phase path
has weight `L_k/b`.  At even offset `q=2u`, write an upper target profile as

\[
 s=h+1+u+K.                                          \tag{1.3}
\]

Thus its centered displacement is `K+1/2`.  At odd offset `2u+1`, the
upper profile with the same integer parameter `K` is

\[
 s=h+1+u+K.                                          \tag{1.4}
\]

Let `T_e(u,K),T_o(u,K)` denote the corresponding affine profile
capacities, and let

\[
 P_e(u,K)=c_{K+u}c_{K-u},\qquad
 P_o(u,K)=c_{K+u}c_{K-u-1}.                          \tag{1.5}
\]

Put

\[
 \rho_e(u,K)=\min(1,P_e/T_e),\qquad
 \rho_o(u,K)=\min(1,P_o/T_o).                        \tag{1.6}
\]

In this notation the adjacent ledger being tested is

\[
 \mathcal A_1=
 \sum_{r,p}{{b\choose r}^2\over b}
 \sum_{q=2}^H
 [\rho_{q,s_{r,p}(q)}-\rho_{q-1,s_{r,p}(q-1)}]_+ .   \tag{1.6a}
\]

We select even integers `K` with `2<=K<=2u`.  Set `v=K/2` and

\[
 A_e=h+1-u-K,\qquad A_o=h-u-K.                       \tag{1.7}
\]

The exact half-step window histogram gives

\[
\begin{aligned}
 bT_e(u,K)
 &=2A_eL_K+4\sum_{j=v+1}^{K-1}L_j+(u-v+3)L_v,\\
 bT_o(u,K)
 &=A_oL_K+(A_o+4)L_{K-1}+4\sum_{j=v}^{K-2}L_j.
                                                               \tag{1.8}
\end{aligned}
\]

These identities can also be read directly from the two defect intervals
of lengths `k,k+1`: the overlap histogram of a moving `u`-interval with an
interval of length `ell` is `2` below `min(u,ell)` and
`|u-ell|+1` at its top value.

Now specialize the source distance to `k=K`.  Exactly `A_o` upper phases
have the even profile `K`, append a `0`, and have the odd profile `K`.
Indeed, the odd `d=0` histogram cell has size `A_o`, and it can only be
entered from the even `d=0` cell by appending `0`.  Complement-reflection
gives another `A_o` lower phases with the same density increment.  Hence
this one transition class contributes exactly

\[
 {2A_oL_K\over b}
 [\rho_o(u,K)-\rho_e(u,K)]_+                         \tag{1.9}
\]

to `mathcal A_1`.

## 2. Uniform continuum expansion

Let

\[
 u=\alpha\sqrt b+O(1),\qquad K=\beta\sqrt b+O(1),    \tag{2.1}
\]

where `(alpha,beta)` ranges over a fixed compact subset of
`0<beta<2alpha`.  Stirling's formula, uniformly on such compact sets,
gives

\[
 {L_{y\sqrt b+O(1)}\over L_K}
 =\exp\{4(\beta^2-y^2)\}+o(1),                       \tag{2.2}
\]

and

\[
 \sqrt b\,{L_K\over W_b}
 \longrightarrow {2\over\sqrt\pi}e^{-4\beta^2}.    \tag{2.3}
\]

Define

\[
 I(\beta)=\int_{\beta/2}^{\beta}
              e^{4(\beta^2-y^2)}\,dy,
 \qquad E(\beta)=e^{3\beta^2}.                      \tag{2.4}
\]

Dividing (1.8) by `bL_K` and applying (2.2) as a Riemann sum yields,
uniformly on compact sets,

\[
 {bT_e\over bL_K}
 =1+{f_e(\alpha,\beta)\over\sqrt b}+o(b^{-1/2}),    \tag{2.5}
\]

\[
 f_e=-2\alpha-2\beta+4I(\beta)
       +(\alpha-\beta/2)E(\beta),                   \tag{2.6}
\]

and

\[
 {bT_o\over bL_K}
 =1+{f_o(\alpha,\beta)\over\sqrt b}+o(b^{-1/2}),    \tag{2.7}
\]

\[
 f_o=-2\alpha+2\beta+4I(\beta).                    \tag{2.8}
\]

For (2.8), use

\[
 {L_{K-1}\over L_K}
 =1+{8\beta\over\sqrt b}+O(b^{-1}).                 \tag{2.9}
\]

The quota ratio is even simpler:

\[
 {P_o\over P_e}
 ={c_{K-u-1}\over c_{K-u}}
 =1+{4(\beta-\alpha)\over\sqrt b}+O(b^{-1}).        \tag{2.10}
\]

Also

\[
 {P_e\over L_K}\longrightarrow e^{-4\alpha^2}.     \tag{2.11}
\]

On every compact set with `alpha>0`, the cap in (1.6) is therefore
inactive for all sufficiently large `b`.  Combining (2.5)--(2.11) proves
the uniform limit

\[
 \boxed{
 \sqrt b\,[\rho_o(u,K)-\rho_e(u,K)]
 \longrightarrow e^{-4\alpha^2}g(\alpha,\beta),}
                                                               \tag{2.12}
\]

where

\[
 g(\alpha,\beta)
 =(\alpha-\beta/2)e^{3\beta^2}-4\alpha.             \tag{2.13}
\]

The integral term cancels.  The surviving term is precisely the parity
endpoint coefficient in (1.8).

## 3. A fixed positive rectangle

Take

\[
 \mathcal R=[0.70,0.75]\times[1.10,1.20].            \tag{3.1}
\]

Throughout `mathcal R`, `beta<2alpha`, and

\[
 \alpha-\beta/2\ge0.10,qquad
 e^{3\beta^2}\ge e^{3.63}>32,qquad 4\alpha\le3.
\]

Thus

\[
 g(\alpha,\beta)>0.2.                                \tag{3.2}
\]

Uniformity in Section 2 implies that, for all sufficiently large `b`,
every integer `u` and even integer `K` satisfying

\[
 0.70\sqrt b\le u\le0.75\sqrt b,qquad
 1.10\sqrt b\le K\le1.20\sqrt b                    \tag{3.3}
\]

obeys

\[
 \rho_o(u,K)-\rho_e(u,K)\ge {c_0\over\sqrt b}       \tag{3.4}
\]

for an absolute `c_0>0`.  Equations (2.3) and (1.7) also give, uniformly
on (3.3),

\[
 {L_K\over W_b}\ge {c_1\over\sqrt b},qquad
 {2A_o\over b}\ge c_2                                \tag{3.5}
\]

with absolute positive constants.  There are `Theta(sqrt(b))` permitted
values of `u` and `Theta(sqrt(b))` even values of `K`.  Summing (1.9) over
the rectangle proves

\[
 \boxed{\mathcal A_1\ge cW_b}                        \tag{3.6}
\]

for one absolute `c>0`, whenever `H>=1.51 sqrt(b)` and `b` is sufficiently
large.  This proves (0.1).  The selected source ranks and every contributor
in (1.8) lie in `[b/4,3b/4]`, so central source truncation does not alter
the argument.

## 4. Consequence for the prefix envelope and exact scope

For any scalar sequence `u(1),...,u(H)` with running minimum
`v(q)=min_(j<=q)u(j)`,

\[
 u(q)-v(q)\ge[u(q)-u(q-1)]_+.                       \tag{4.1}
\]

After multiplying by the path capacities and summing,

\[
 \sum_{i,q}a_i[u_i(q)-\min_{j\le q}u_i(j)]
 \ge\mathcal A_1.                                    \tag{4.2}
\]

Therefore (3.6) proves an `Omega(W_b)` loss for the proportional prefix
envelope itself.  In particular, neither the originally proposed
`O(HW_b/b)` estimate for `mathcal A_1` nor an `o(W_b)` analysis of that
witness can be true.

This theorem does **not** lower-bound the optimum of the affine retirement
LP.  The LP may use path-dependent thinning which is not the running
minimum of the layerwise proportional optima.  It also says nothing about
integral chain rounding or labelled cyclic-order coinstantiation.

## 5. H100 audit

The checker
`scratch/audit_affine_adjacent_variation_continuum_obstruction_20260821.py`
verifies the exact formulas against literal affine words at small sizes,
checks the exact joint transition count in (1.9), and prints the convergence
in (2.12) at a fixed interior point.  These finite rows are diagnostics;
the asymptotic proof is Sections 2--3.
