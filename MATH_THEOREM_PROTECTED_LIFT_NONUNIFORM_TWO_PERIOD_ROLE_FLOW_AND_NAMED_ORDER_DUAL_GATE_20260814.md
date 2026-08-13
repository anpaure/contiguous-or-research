# Protected lift: a nonuniform two-period role flow and the named-order dual gate

**Date:** 2026-08-14  
**Status:** unconditional asymptotic positive theorem for the exact
owner/lower ground-point role system, under an explicit four-step Gray
direction-gap margin.  The construction breaks cyclic-orbit symmetry on a
lift-sized bank of genuine shells and then pads it to a full exact role
allocation.  It does not solve the fractional or integral named
owner/lower ordering system, upper support, seam chronology, or fusion.

## 0. Parameters and the protected defect

Put

\[
 k=2p+1,\qquad R=p+1,\qquad c=R-q,
 \qquad W={k\choose R},\qquad K={W\over k}.            \tag{0.1}
\]

Partition `[k]-{z}` into pairs `P_i={a_i,b_i}`.  Let `H` be a cyclic
Hamilton Gray code of `Q_p`, let `h_i` be its number of direction-`i`
transitions, and put

\[
                         e=2^p.                       \tag{0.2}
\]

The protected transversal lift has the exact role defect

\[
 u_{a_i}=u_{b_i}={h_i\over2},\qquad u_z=0,            \tag{0.3}
\]

\[
 r_{a_i}=r_{b_i}
 =2^{p-1}-{(q-1)h_i\over2},\qquad r_z=0.             \tag{0.4}
\]

Here `u_x` is the number of shell supports which must be removed at `x`,
and `r_x` is removed weighted core load.  They satisfy

\[
                         \sum_xu_x=e,qquad
                         \sum_xr_x=ce.                \tag{0.5}
\]

We assume the stronger direction-count bound

\[
 \boxed{
                         h_i\le {e\over q+4}
                         \qquad(i\in[p]).}             \tag{0.6}
\]

A repeated-direction separation of at least `q+4` implies `(0.6)`.  The
standard long-run cube theorem supplies this constant margin whenever
`p-3log_2p>=q+4`.

## 1. An exact equal-period shell decomposition

The following lemma is the constructive integrality mechanism.

### Lemma 1.1 (slot-clone decomposition)

Let `m,t,c,N` be nonnegative integers with `c+N<=m`.  For `x in[m]`, let
`alpha_x,beta_x` be nonnegative integers satisfying

\[
 \sum_x\alpha_x=ct,qquad
 \sum_x\beta_x=Nt,qquad
 \alpha_x+\beta_x\le t.                               \tag{1.1}
\]

Then there are `t` labelled pairs

\[
                         (C_j,T_j),qquad
 |C_j|=c,quad |T_j|=N,quad C_j\cap T_j=\varnothing,  \tag{1.2}
\]

such that `x` occurs in exactly `alpha_x` cores and exactly `beta_x`
supports.

The pairs can be found by bipartite edge colouring.

#### Proof

Make `c` core-slot vertices and `N` support-slot vertices.  Distribute
`alpha_x` parallel edges from the core slots to coordinate `x` so that
every core slot has degree `t`; this is possible because the total is
`ct`.  Similarly distribute the `beta_x` support edges so every support
slot has degree `t`.

The resulting bipartite multigraph has degree `t` at every slot and degree
`alpha_x+beta_x<=t` at every coordinate.  Add dummy slot vertices and
dummy edges to make a `t`-regular bipartite multigraph with `m` vertices on
each side.  By Konig's line-colouring theorem it decomposes into `t`
perfect matchings.  In one matching, the genuine core slots meet `c`
distinct coordinates and the genuine support slots meet `N` other distinct
coordinates.  Read these as `(C_j,T_j)`.  Edge multiplicities give the
required column degrees. \(\square\)

Thus the coordinatewise capacity in `(1.1)` is not merely a fractional
condition.  It is an exact integer decomposition theorem.

## 2. A lift-sized nonuniform shadow-shell bank

Take the two shortest consecutive legal periods

\[
                         n=2q+2,qquad n+1=2q+3,       \tag{2.1}
\]

and write

\[
                         m=2p.                        \tag{2.2}
\]

Thus the shadow bank uses only the paired coordinates and omits `z` from
every core and support.

Put

\[
 g=m-(n+2)                                             \tag{2.3}
\]

and assume `g>c`.  Define

\[
 B_0=\max\left\{
 n^2+n-2,
 \left\lceil{m(n-1)\over c}\right\rceil,
 \left\lceil{2gn\over g-c}\right\rceil
 \right\}.                                            \tag{2.4}
\]

Let `b` be the least integer at least `B_0` satisfying

\[
                         b\equiv e\pmod n,             \tag{2.5}
\]

and suppose

\[
 (n+1)b\le {e\over n+6},
 \qquad
 mb<{5e\over n+6}.                                    \tag{2.6}
\]

Finally put

\[
                         a={e-(n+1)b\over n}.          \tag{2.7}
\]

These inequalities hold for all sufficiently large central parameters
`q=o(p)`: `B_0` is polynomial in `p,q`, while `e=2^p`.

### Theorem 2.1 (exact nonuniform defect bank)

Under `(0.6)` and `(2.3)--(2.7)`, there are `a` genuine shells of period
`n` and `b` genuine shells of period `n+1`, all on `[k]-{z}`, such that

\[
 \sum_jN_j=e,qquad
 |C_j|=c,quad |T_j|=N_j,quad C_j\cap T_j=\varnothing, \tag{2.8}
\]

and their exact role degrees are

\[
                         |\{j:x\in T_j\}|=u_x,        \tag{2.9}
\]

\[
                         \sum_{j:x\in C_j}N_j=r_x.    \tag{2.10}

\]

Hence this shell bank has exactly the same owner and lower ground-point
loads as the protected transversal lift.

#### Proof

Work on the `m=2p` paired coordinates.  Equation `(0.6)` gives

\[
                         u_x\le {e\over n+6}.          \tag{2.11}
\]

At least `n+2` coordinates satisfy `u_x>=b`.  Otherwise at most `n+1`
coordinates contribute at the upper bound `(2.11)` and every remaining
coordinate contributes less than `b`, giving

\[
 \sum_xu_x
 <{(n+1)e\over n+6}+mb<e,                            \tag{2.12}
\]

contrary to `(0.5)`.  Fix an `(n+2)`-set `Q` of such coordinates.

For every coordinate, let `rho_x` be the least nonnegative residue of
`r_x` modulo `n`.  We first choose the heavy-core degrees `v_x`.  Start
with `v_x=rho_x` everywhere and keep these values fixed on `Q`.  Since

\[
 \sum_xr_x=ce,qquad b\equiv e\pmod n,                \tag{2.13}
\]

the integer

\[
                         \Delta={cb-\sum_x\rho_x\over n}          \tag{2.14}
\]

is integral.  It is nonnegative by `(2.4)`.  On the `g` coordinates
outside `Q`, the total capacity for adding multiples of `n` is at least

\[
 {g(b-2n)\over n}\ge {cb\over n}\ge\Delta,           \tag{2.15}
\]

again by `(2.4)`.  Distribute `Delta` increments there.  We obtain

\[
 0\le v_x\le b,qquad
 v_x\equiv r_x\pmod n,qquad
 \sum_xv_x=cb,                                        \tag{2.16}

\]

and `v_x=rho_x<=n-1` on `Q`.

Define the light-core degrees

\[
                         ell_x={r_x-(n+1)v_x\over n}.  \tag{2.17}
\]

They are integers with sum `ca`.  They are nonnegative because

\[
 r_x\ge {5e\over n+6}\ge(n+1)b,                      \tag{2.18}
\]

and they are at most `a` because `e-r_x>=e/2>(n+1)b`.

Next select the heavy-support degrees `s_x`, supported on `Q`, with

\[
 0\le s_x\le b-v_x,qquad
                         \sum_xs_x=(n+1)b.            \tag{2.19}

\]

This is possible because `u_x>=b` on `Q` and

\[
 \sum_{x\in Q}(b-v_x)
 \ge(n+2)(b-n+1)\ge(n+1)b                            \tag{2.20}
\]

by `(2.4)`.  Choose the degrees within these intervals.  Put

\[
                         w_x=u_x-s_x.                 \tag{2.21}
\]

Then `w_x>=0` and `sum_xw_x=na`.  The heavy capacity

\[
                         v_x+s_x\le b                 \tag{2.22}
\]

holds by construction.  For the light capacity, direct substitution gives

\[
 \begin{aligned}
 n(a-\ell_x-w_x)
 &= {e\over2}-(q+3)u_x
    -(n+1)(b-v_x)+ns_x\\
 &\ge {e\over n+6}-(n+1)b\ge0.                       \tag{2.23}
 \end{aligned}
\]

Apply Lemma 1.1 to the `b` heavy tokens with core degrees `v_x` and support
degrees `s_x`, and to the `a` light tokens with core degrees `ell_x` and
support degrees `w_x`.  Equations `(2.9)--(2.10)` follow from
`(2.17),(2.21)`. \(\square\)

The construction uses `a+b=Theta(e/q)` shells, not whole cyclic orbit
blocks.  It is a deterministic breaking of orbit symmetry along the Gray
direction counts.

## 3. Padding the defect bank to an exact full role allocation

The defect bank can be embedded in a complete unprotected role allocation.
This makes its deletion, followed by insertion of the transversal lift,
an exact positive role operation.

### Lemma 3.1 (balanced residue allocation)

Let \(S,\rho,k,n\) be integers with \(S\equiv k\rho\pmod n\).  If
`S/k` is sufficiently large, there are nonnegative integers `d_x` such that

\[
 d_x\equiv\rho\pmod n,qquad
 \sum_xd_x=S,qquad
                         |d_x-S/k|<n.                 \tag{3.1}
\]

#### Proof

Write `d_x=rho+n t_x`.  The required sum of the `t_x` is integral; split it
as evenly as possible among the `k` coordinates. \(\square\)

### Theorem 3.2 (exact protected owner/lower role flow)

Assume the hypotheses of Theorem 2.1 and, asymptotically,

\[
                         q=o(p),qquad 2^p=o(W/k).      \tag{3.2}

\]

For all sufficiently large `p`, there is a positive shell collection
\(\mathcal R\) of periods `n,n+1` whose total period is `W-e` and whose roles
are exactly

\[
 |\{j\in\mathcal R:x\in T_j\}|=K-u_x,                \tag{3.3}
\]

\[
 \sum_{j\in\mathcal R:x\in C_j}N_j=cK-r_x.           \tag{3.4}
\]

Therefore \(\mathcal R\) satisfies every owner and lower ground-point equation
after the transversal lift is protected.

#### Proof

Choose nonnegative `A,B=Theta(W/n)` satisfying

\[
                         nA+(n+1)B=W.                 \tag{3.5}

\]

For example, choose \(B\equiv W\pmod n\) nearest \(W/(2n+1)\) and define
`A` by `(3.5)`.  Eventually `A>a` and `B>b`.

We construct a complete uniform role bank which contains the defect bank.
Let `v_x,s_x,ell_x,w_x` be its heavy/light degree splits from Theorem 2.1.
Use Lemma 3.1 to choose total heavy-core degrees `V_x` with

\[
 V_x\equiv cK\pmod n,qquad
 \sum_xV_x=cB,qquad
                         V_x={cB\over k}+O(n).         \tag{3.6}

\]

Put

\[
                         L_x={cK-(n+1)V_x\over n}.     \tag{3.7}

\]

Then `sum_xL_x=cA` and `L_x=cA/k+O(n)`.  Independently choose integers

\[
 \sum_xS_x=(n+1)B,qquad
                         S_x={(n+1)B\over k}+O(1),    \tag{3.8}

\]

and put `Q_x=K-S_x`, so `sum_xQ_x=nA` and
`Q_x=nA/k+O(1)`.

Because `A,B=Theta(W/n)`, while every degree in the defect bank is
`O(e)` and `e=o(W/k)`, the balanced degrees eventually satisfy

\[
 V_x\ge v_x,quad S_x\ge s_x,quad
 L_x\ge\ell_x,quad Q_x\ge w_x.                       \tag{3.9}

\]

Moreover the strict shell-space margins

\[
 k-c-(n+1)=p-q-3>0,qquad
 k-c-n=p-q-2>0                                      \tag{3.10}

\]

give, eventually,

\[
 (V_x-v_x)+(S_x-s_x)\le B-b,                         \tag{3.11}
\]

\[
 (L_x-\ell_x)+(Q_x-w_x)\le A-a.                     \tag{3.12}

\]

Apply Lemma 1.1 to these residual heavy and light degree sequences.  Add
the resulting shells to the defect bank.  The union has support degree `K`
and weighted core degree `cK` at every coordinate.  Delete the defect bank;
the remainder \(\mathcal R\) has `(3.3)--(3.4)`. \(\square\)

This directly constructs cores and core-disjoint supports.  Hence all
capacitated Hall inequalities for the role system pass; no separate
existence invocation is needed.

## 4. Cross-cell count after ordering

For any cyclic order on a period-`N` support, the resulting pure rail has at
least `ceil(N/2)` edges which are cross-cell relative to the fixed pair
structure.  Therefore every eventual ordering of \(\mathcal R\) contains at
least

\[
 \boxed{
                         {W-e\over2}}                 \tag{4.1}

\]

nonlift cross-cell edges.  The macroscopic cross bank required by the
low-pair-cell obstruction is automatic and does not depend on the ordering
rounding.

## 5. The exact protected named-order gates

The role theorem does not choose cyclic orders.  Freeze its labelled shells.
For shell `j`, let `Omega_j^safe` be the cyclic orders of `T_j`, modulo
rotation, whose owner and lower decks avoid the protected lift shores
`Y,Z`.

For `sigma in Omega_j^safe`, write `E^+(j,sigma)` for its `N_j` owners and
`E^-(j,sigma)` for its `N_j` lower colours.

### Theorem 5.1 (exact fractional dual)

There are distributions `lambda_(j,sigma)>=0` which choose one safe order
per token fractionally and give load one to every residual owner and lower
colour if and only if, for every real weight pair

\[
 theta^+:\mathcal O-Y\to\mathbb R,qquad
 theta^-:\mathcal L-Z\to\mathbb R,                   \tag{5.1}

\]

one has

\[
 \boxed{
 \sum_{A\notin Y}\theta_A^+
 +\sum_{L\notin Z}\theta_L^-
 \le
 \sum_j\max_{\sigma\in\Omega_j^{\rm safe}}
 \left(
  \sum_{A\in E^+(j,\sigma)}\theta_A^+
 +\sum_{L\in E^-(j,\sigma)}\theta_L^-
 \right).}                                            \tag{5.2}

\]

An empty `Omega_j^safe` makes the system infeasible.

#### Proof

For one token, the attainable fractional incidence vectors form the convex
hull of its safe order vectors.  The total attainable load set is their
Minkowski sum.  Condition `(5.2)` is exactly membership of the all-ones
residual vector in that sum, by finite-dimensional separating
hyperplanes. \(\square\)

### Integral, simplicity, and chronology boundary

An integral exact factor requires binary variables

\[
 z_{j,\sigma}\in\{0,1\},qquad
 \sum_{\sigma\in\Omega_j^{\rm safe}}z_{j,\sigma}=1,   \tag{5.3}

\]

with every residual owner and lower row equal to one.  Theorem 5.1 is only
the fractional relaxation; it does not round these multiple-choice order
polytopes.

Every individual selected rail is owner-simple and lower-simple because
its toggle labels are distinct and `N_j>2q`.  Thus an integral solution of
the named equations is globally simple automatically.  Each closed rail is
`q`-biresident internally: a toggle trace is `1^q0^(N_j-q)`, while core
coordinates are constant.  Nothing here joins the closed components or
checks the transition collars at future seams.  Immediate-upper support and
source flags are also outside the role and named owner/lower systems.

The complete two-shore order hypergraph retains the forced incident
owner--facet codegree `2/R`; hence the owner-only vanishing-codegree nibble
cannot be imported unchanged.  The next theorem must prove `(5.2)` for the
constructed nonuniform shells and then round it by an incidence-aware
partite/conflict matching or a structured-leave absorber.

## 6. Exact scope

The positive conclusion is

\[
 \boxed{
 \begin{gathered}
 \text{long-run direction margin}\Rightarrow
 \text{exact lift-sized nonuniform defect shells},\\
 \text{slot-clone edge colouring}\Rightarrow
 \text{integral cores and core-disjoint supports},\\
 \text{balanced padding}\Rightarrow
 \text{exact protected owner/lower point roles},\\
 \text{every future ordering}\Rightarrow
 \Omega(W)\text{ cross-cell edges}.
 \end{gathered}}                                      \tag{6.1}

\]

No fractional named-order feasibility, integral named-order rounding,
upper support, source chronology, or component fusion is claimed.
