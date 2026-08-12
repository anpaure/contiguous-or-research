# Audit of the rank-twisted macroblock tiling and its physical Hall gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Outcome

The owner-packing part of
`MATH_THEOREM_RANK_TWISTED_MACROBLOCK_PACKET_TILING_20260726.md`
is correct.  There is, however, an essential target-side datum which that
theorem deliberately leaves unspecified: in every product cell of dimension
`S >= r`, one must choose the `r` physical axes retained in the parallel
`Q_r` splitting.  Literal source-to-target incidence depends on this choice,
not merely on the fact that the union of the rank-dependent local frames is
`K_(d,d)`.

This note proves four precise statements.

1. It gives exact lower and upper physical candidate-degree formulae for an
   arbitrary choice of the retained axis sets.
2. After adjoining the full order/phase catalogue
   `Aut(Q_r)=C_2^r semidirect S_r`, it computes the exact factor-label multiplicity of
   every candidate source--target pair and every candidate physical face.
3. It states the exact weighted outer Hall dual.  Pointwise reachability and
   positive candidate degree test only singleton weights and are not this
   dual.
4. It gives a legal retained-axis choice, including the natural
   lexicographic choice, for which at every fixed Gaussian depth

   \[
                    q=A\sqrt m+O(1)
   \]

   both the lower and upper factors miss `(1-o(1))N_q` targets.  The exact
   profile Hall ratio in the offending cut is

   \[
    {\binom n{t+q}\over\binom nt}\quad\hbox{or}\quad
    {\binom n{u-q}\over\binom nu},                    \tag{0.1}
   \]

   and is `exp(-Omega(q^2/r))=o(1)` on a target set of mass `1-o(1)`.

Thus the owner theorem is verified, but the rank twist and dense-cross count
alone do not imply any Gaussian Hall theorem.  A dispersed choice of retained
axes satisfying the weighted dual below remains a genuine open requirement.

## 1. Audit of the owner theorem

Write

\[
 [2m]=R_0\mathbin{\dot\cup}\bigdotcup_{j=1}^b B_j,
 \qquad B_j=A_j\mathbin{\dot\cup}C_j,
 \qquad |A_j|=|C_j|=d,                               \tag{1.1}
\]

where `|R_0|<2d`.  At local rank `k`, the matching is

\[
 M_k=\{a_i c_{i+k}:i\in\mathbb Z_d\}.                \tag{1.2}
\]

For a fixed local-rank vector, these are `db` disjoint physical pairs.
Under an unconditioned uniform subset, their number `S` of one-endpoint
pairs is exactly `Bin(db,1/2)`.  Hence, for `r=o(m)`,

\[
 4^{db}\Pr(S<r)=2^{db+o(m)}=2^{m+o(m)}.              \tag{1.3}
\]

There are at most

\[
 (2d+1)^b=\exp\!\left(O\!\left({m\log d\over d}\right)\right)
             =2^{o(m)}                               \tag{1.4}
\]

local-rank vectors.  Although the estimate (1.3) overcounts a subset once
for every rank vector, this is a valid upper bound.  The residual factor is
at most `2^(2d)=2^o(m)`.  This proves the stated

\[
                         L\le 2^{m+o(m)}.             \tag{1.5}
\]

Every cell of dimension `S >= r` is partitioned into parallel `Q_r` cells
by choosing an `r`-subset of its flexible axes and freezing all other
orientations.  This is an exact physical partition, and all retained axes
join an `A_j` coordinate to a `C_j` coordinate.  These owner claims pass.

There is one qualification to the compiler sentence.  The cited recursive
factor `F_r` is proved for `r` a power of two, and its simultaneous literal
trace injectivity is proved through `q <= r/2`.  Consequently statements
about compiled windows must either assume these hypotheses or cite a
different compiler.  This does not affect the owner tiling itself; in the
intended scale one may replace `r` by a neighboring power of two.

## 2. Exact local status statistics

For a local set `Z subseteq B_j`, define relative to `M_k`

\[
\begin{aligned}
 z_k(Z)&=\#\{e\in M_k:e\cap Z=\varnothing\},\\
 f_k(Z)&=\#\{e\in M_k:e\subseteq Z\},\\
 s_k(Z)&=\#\{e\in M_k:|e\cap Z|=1\}.
\end{aligned}                                         \tag{2.1}
\]

If

\[
 \rho_k(Z)=|\{i:a_i\in Z,\ c_{i+k}\in Z\}|,
\]

then exactly

\[
 f_k(Z)=\rho_k(Z),\qquad
 z_k(Z)=d-|Z|+\rho_k(Z),\qquad
 s_k(Z)=|Z|-2\rho_k(Z).                              \tag{2.2}
\]

These identities retain all dependence on the rank twist.  In particular,
replacing `M_(t+a)` by `M_t`, even when `a` is small, is not an exact
operation.

## 3. Exact lower candidate degree

Fix a lower physical target

\[
                         T\in\binom{[2m]}{m-q}        \tag{3.1}
\]

and put `T_j=T cap B_j`, `t_j=|T_j|`.  A source middle owner has local
ranks

\[
                         k_j=t_j+a_j,
 \qquad a_j\ge0,\qquad \sum_j a_j=q.                 \tag{3.2}
\]

The residual coordinates cannot change in a packet, so the source and
target have the same intersection with `R_0`.

For a fixed allocation `a=(a_j)`, a lower face is obtained by choosing

\[
 D_j\subseteq\{e\in M_{t_j+a_j}:e\cap T_j=\varnothing\},
 \qquad |D_j|=a_j.                                   \tag{3.3}
\]

The edges in `D_j` are changed from zero status in `T` to flexible status
in the source cell.  All remaining statuses are forced by `T`.  Therefore
`(a,D)` determines one and only one product status cell, of dimension

\[
 S^-(T;a,D)=q+\sum_j s_{t_j+a_j}(T_j).               \tag{3.4}
\]

The right side is independent of the particular chosen sets `D_j`.
Before the parallel `Q_r` splitting, the exact number of compatible product
cells is

\[
 C_q^-(T)=
 \sum_{\substack{a_j\ge0\\\sum a_j=q}}
       \prod_j\binom{z_{t_j+a_j}(T_j)}{a_j}.          \tag{3.5}
\]

Each such cell contains exactly `2^q` middle sources above this face, one
for every choice of an endpoint on each edge in `D=dotcup_j D_j`.

Now let `I(C)` be the retained `r`-axis set selected in a product cell
`C` with `S(C)>=r`.  Splitting `C` along `I(C)` creates exactly one packet
having `T` as the face indexed by `D` if and only if

\[
                              D\subseteq I(C).         \tag{3.6}
\]

Indeed the orientations of every flexible edge outside `D` are then fixed
by `T`; in particular there is a unique choice of the frozen orientations
outside `I(C)`.  Hence the exact number of selected physical packets for
which `T` is a lower `q`-face is

\[
 p_q^-(T)=
 \sum_{\substack{a_j\ge0\\\sum a_j=q}}
 \ \sum_{\substack{D_j\subseteq Z_{t_j+a_j}(T_j)\\|D_j|=a_j}}
 \mathbf 1\{S^-(T;a,D)\ge r\}\,
 \mathbf 1\{D\subseteq I(C^-(T;a,D))\}.             \tag{3.7}
\]

Here `Z_k(Z)` denotes the zero-edge set, not merely its cardinality.
Formula (3.7), rather than (3.5), is the literal packet compatibility
degree.

## 4. Exact upper candidate degree

Fix

\[
                         U\in\binom{[2m]}{m+q},        \tag{4.1}
\]

put `U_j=U cap B_j`, and write `u_j=|U_j|`.  An underlying source has

\[
                         k_j=u_j-a_j,
 \qquad a_j\ge0,\qquad \sum_j a_j=q.                 \tag{4.2}
\]

The touched axes must be full edges of `U_j` in the actual source frame
`M_(u_j-a_j)`.  Thus

\[
 D_j\subseteq\{e\in M_{u_j-a_j}:e\subseteq U_j\},
 \qquad |D_j|=a_j.                                   \tag{4.3}
\]

Changing these full statuses to flexible ones gives the unique product
cell of dimension

\[
 S^+(U;a,D)=q+\sum_j s_{u_j-a_j}(U_j).               \tag{4.4}
\]

Consequently the pre-splitting cell count and the literal selected-packet
degree are respectively

\[
 C_q^+(U)=
 \sum_{\substack{a_j\ge0\\\sum a_j=q}}
       \prod_j\binom{f_{u_j-a_j}(U_j)}{a_j},          \tag{4.5}
\]

and

\[
 p_q^+(U)=
 \sum_{\substack{a_j\ge0\\\sum a_j=q}}
 \ \sum_{\substack{D_j\subseteq F_{u_j-a_j}(U_j)\\|D_j|=a_j}}
 \mathbf 1\{S^+(U;a,D)\ge r\}\,
 \mathbf 1\{D\subseteq I(C^+(U;a,D))\}.            \tag{4.6}
\]

Here `F_k(U)` is the full-edge set.  Equations (3.7) and (4.6) are not
formally interchangeable by complementation because complementation sends
local rank `k` to `2d-k`, and the prescribed frame changes from `M_k` to
`M_(2d-k)`.  Both signs therefore had to be counted separately.

## 5. Exact order/phase multiplicities

Assume `r` is a power of two and `q<=r/2`.  Let `F_r` be the audited
return-free successor factor on `Q_r`.  On each physical packet include
the complete labelled order/phase catalogue

\[
             G_r=\operatorname{Aut}(Q_r)=C_2^r\rtimes S_r,
             \qquad |G_r|=2^r r!.                    \tag{5.1}
\]

A phase is a bit translation and an order is a direction permutation.
For `g in G_r`, install the conjugate `gF_rg^(-1)`.

### Lemma 5.1 (fixed-source multiplicity)

Let `x` be a fixed source vertex of a packet and let `Q` be a fixed set of
`q` packet axes.  Exactly

\[
                         {|G_r|\over\binom rq}         \tag{5.2}
\]

labels have `Q` as the direction set of the forward `q`-window from `x`.
The identical statement holds for reverse windows.

#### Proof

For a uniform `g`, the preimage of `x` is uniform on `Q_r`.  Conditional
on that preimage, the direction permutation is uniform in `S_r`, and hence
sends the base `q`-set of distinct directions uniformly to the
`binom(r,q)` possible `q`-sets.  This is exact, not asymptotic.  Reversal
does not alter the argument.  \(\square\)

Since the lower or upper face of a fixed source is determined by its
`q`-set of touched axes, (5.2) is also the exact labelled degree of a
fixed compatible source--target pair.

### Lemma 5.2 (fixed-face multiplicity)

A fixed physical `q`-face of one packet is produced by exactly

\[
             \Lambda_{r,q}={2^q|G_r|\over\binom rq}   \tag{5.3}
\]

labels.  This holds for both signs.

#### Proof

There are `2^q` packet vertices above a lower face, or below an upper face.
Each has the multiplicity (5.2).  For a fixed label, packet-wide trace
injectivity says that at most one of those vertices produces the given
physical target, so these label sets are disjoint.  \(\square\)

Combining Sections 3--5 gives the exact labelled physical target degrees

\[
 d_q^-(T)=\Lambda_{r,q}p_q^-(T),\qquad
 d_q^+(U)=\Lambda_{r,q}p_q^+(U).                     \tag{5.4}
\]

If `mathcal P` is the selected packet family and its owner leave is `L`,
then every packet has `binom(r,q)2^(r-q)` physical `q`-faces.  Therefore

\[
 \sum_Tp_q^-(T)=\sum_Up_q^+(U)
 ={W-L\over2^r}\binom rq2^{r-q}
 =(W-L){\binom rq\over2^q},                          \tag{5.5}
\]

and, writing `N_q=binom(2m,m-q)=binom(2m,m+q)`,

\[
 {1\over N_q}\sum_Td_q^-(T)
 ={1\over N_q}\sum_Ud_q^+(U)
 =|G_r|{W-L\over N_q}.                               \tag{5.6}
\]

Equation (5.6) verifies the average degree but says nothing about its
lower tail or Hall cuts.

## 6. The exact weighted outer Hall condition

For every packet `P` and label `g`, let

\[
 \tau_{P,g,q}^\epsilon
   \subseteq\binom{[2m]}{m+\epsilon q}                \tag{6.1}
\]

be its `2^r` distinct literal traces.  A fractional choice of at most one
label per packet covers every target at every protected signed depth if
and only if there are numbers `x_(P,g)>=0` such that

\[
 \sum_gx_{P,g}\le1,
 \qquad
 \sum_{P,g:T\in\tau_{P,g,q}^\epsilon}x_{P,g}\ge1
 \quad\hbox{for every }(q,\epsilon,T).                \tag{6.2}
\]

By separation of the product of the packet simplices, (6.2) is equivalent
to the following weighted outer Hall inequalities: for every nonnegative
array `y=(y_(q,epsilon,T))`,

\[
 \boxed{
 \sum_{q,\epsilon,T}y_{q,\epsilon,T}
 \ \le\
 \sum_{P\in\mathcal P}\max_{g\in G_r}
       \sum_{q,\epsilon}
       \sum_{T\in\tau_{P,g,q}^\epsilon}y_{q,\epsilon,T}.}
                                                               \tag{6.3}
\]

Indeed the right side is the support function of the product of packet
simplices.  Downward closure of its image permits the separating vector
to be taken nonnegative.  Filling unused packet mass by an arbitrary label
changes `<=1` to `=1` without damaging coverage.

The singleton choices of `y` recover pointwise candidate degree.  General
`y` couple all factors, orders, phases, depths, and signs.  Thus neither
`C_q^epsilon(T)>0` nor `p_q^epsilon(T)>0` is a Hall theorem.

## 7. A legal retained-axis choice with a Gaussian Hall catastrophe

The following theorem shows quantitatively why the retained-axis rule
cannot remain unspecified.

### Theorem 7.1 (localized-axis Hall cut)

Assume

\[
 d\to\infty,\qquad d=m^{o(1)},\qquad
 {r\over d\log m}\longrightarrow\infty,
 \qquad \sqrt m\ll r=o(m),                           \tag{7.1}
\]

and take `r` to be a power of two.  Let

\[
                         q=A\sqrt m+O(1),\qquad A>0.  \tag{7.2}
\]

There is a legal parallel-`Q_r` splitting of all good product cells for
which, regardless of the factor/order/phase label selected in each packet,

\[
 \#\{\hbox{distinct lower depth-}q\hbox{ targets covered}\}
                         =o(N_q),                     \tag{7.3}
\]

and the same assertion holds for upper targets.  Hence both signs have
`(1-o(1))N_q` holes.

#### Proof: localized owner packets

Let `E` be the union of the first `ell` complete macroblocks, where

\[
 p=d\ell\in[8r,8r+d),\qquad n=|E|=2p=\Theta(r).       \tag{7.4}
\]

For a product cell having at least `r` flexible axes in `E`, retain `r`
of those axes.  In every other good product cell choose an arbitrary
`r`-set.  This is a legal exact parallel-cube splitting.  Lexicographically
choosing the first `r` flexible axes is a special case on the first class.

It remains to show that the second class contains only `o(W)` middle
owners.  Under the unconditioned Bernoulli-`1/2` law, let `K_j` be the
local rank and let

\[
 Y_j=s_{K_j}(X\cap B_j).                              \tag{7.5}
\]

The variables `Y_j` are independent across macroblocks and lie in `[0,d]`.
Conditional on `K_j=k`, the matching `M_k` is fixed and

\[
 \mathbb E(Y_j\mid K_j=k)
 ={k(2d-k)\over2d-1}.                                \tag{7.6}
\]

Since `K_j` has distribution `Bin(2d,1/2)`, direct evaluation gives

\[
                         \mathbb EY_j={d\over2}.       \tag{7.7}
\]

Hoeffding's inequality and `p<9r` therefore give

\[
 \Pr\!\left(\sum_{j\le\ell}Y_j<r\right)
 \le
 \exp\!\left(-{2(3r)^2\over\ell d^2}\right)
 \le \exp(-2r/d).                                    \tag{7.8}
\]

Conditioning on the global event `|X|=m` multiplies this probability by at
most `O(sqrt(m))`.  Assumption (7.1) makes the result `o(1)`.  Thus all but
`o(W)` middle owners belong to packets whose every axis lies in `E`.

#### Proof: the exact lower profile ratio

Put

\[
 \mu_-={n(m-q)\over2m}
       ={n\over2}-{nq\over2m},                        \tag{7.9}
\]

and let `mathcal A_q^-` consist of lower targets with

\[
                    \bigl||T\cap E|-\mu_-\bigr|\le q/10. \tag{7.10}
\]

For a uniform rank-`m-q` target, `|T cap E|` is hypergeometric with
variance at most `n/4`.  Since `n/q^2=Theta(r/m)=o(1)`, Chebyshev gives

\[
                         |\mathcal A_q^-|=(1-o(1))N_q. \tag{7.11}
\]

Fix `t` in (7.10) and one exterior set

\[
 Y\subseteq[2m]\setminus E,
 \qquad |Y|=m-q-t.                                    \tag{7.12}
\]

There are exactly `binom(n,t)` targets in this fibre.  A localized packet
does not change the exterior set.  Every middle source capable of supplying
one of these targets therefore has the same `Y` and has exactly `t+q`
coordinates in `E`.  There are only `binom(n,t+q)` such sources.  Since one
source contributes one depth-`q` occurrence, the exact fibre capacity ratio
is

\[
                         R_q^-(t)={\binom n{t+q}\over\binom nt}. \tag{7.13}
\]

Now `n=o(m)` and (7.10) imply

\[
 |t-n/2|\le q/5,
 \qquad |t+q-n/2|\ge4q/5                             \tag{7.14}
\]

for all large `m`.  Also `q=o(n)`.  The elementary product formula for
binomial coefficients, or strict log concavity about `n/2`, yields

\[
 R_q^-(t)\le\exp(-c q^2/n)=o(1)                      \tag{7.15}
\]

uniformly in this window.  For completeness, if `0<=u<v<=n/4`,

\[
 {\binom n{\lfloor n/2\rfloor+v}
  \over
  \binom n{\lfloor n/2\rfloor+u}}
 =\prod_{j=u+1}^v
   {\lfloor n/2\rfloor-j+1\over\lceil n/2\rceil+j}
 \le \exp\!\left(-{v^2-u^2\over n}\right),          \tag{7.16}
\]

and symmetry handles either sign of `t-n/2`.

Summing (7.13)--(7.15) over all exterior fibres and all `t` in (7.10)
shows that localized packets cover only `o(N_q)` members of
`mathcal A_q^-`.  Exceptional packets contribute at most one target per
exceptional middle source, hence `o(W)=o(N_q)`, because

\[
                         {N_q\over W}\longrightarrow e^{-A^2}>0. \tag{7.17}
\]

This proves (7.3).

#### Proof: the upper sign

For upper targets use

\[
 \mu_+={n(m+q)\over2m}={n\over2}+{nq\over2m}         \tag{7.18}
\]

and the window `||U cap E|-mu_+|<=q/10`.  It again has mass `1-o(1)`.
For fixed inside size `u` and fixed exterior set, the source has inside
size `u-q`, so the exact capacity ratio is

\[
                         R_q^+(u)={\binom n{u-q}\over\binom nu}. \tag{7.19}
\]

Equations (7.14)--(7.16), reflected about `n/2`, give
`R_q^+(u)<=exp(-cq^2/n)=o(1)`.  Exceptional sources again contribute only
`o(N_q)`.  This proves the upper assertion.  \(\square\)

## 8. Adversarial audit and exact remaining boundary

Theorem 7.1 does **not** prove that every rank-twisted retained-axis rule
fails.  It proves the sharper statement actually justified by the present
data: owner packing, complete frame union, and `s(P)=r` do not imply target
Hall, because a fully legal realization of all three properties violates a
single explicit physical cut on almost the whole Gaussian target layer.

The counterexample uses no weakness of the local compiler.  It survives
the full order/phase catalogue and even an arbitrary factor on each packet,
because every such factor preserves the exterior coordinate set.

Conversely, the exact degree formula (5.4) is not itself a positive Hall
result.  Large or nearly regular singleton degrees can coexist with a
failure of (6.3), and an integral packet choice is stronger still than the
fractional condition (6.3).

The minimum surviving hypothesis for this architecture is therefore:

> choose the retained axis sets `I(C)` and one common packet compiler label
> per selected packet so that the literal trace sets satisfy the weighted
> inequalities (6.3), with an aggregate `o(W)` relaxation over all protected
> signed depths.

Any useful sufficient version must in particular rule out localization in
every coordinate carrier `E` with

\[
                         q^2\gg |E|,qquad |E|=o(m),   \tag{8.1}
\]

because the exterior-profile cut above then has exponentially vanishing
Hall ratio.  Proving such dispersion together with (6.3), rather than mere
potential reachability under the union `K_(d,d)`, is the unresolved
Gaussian source/target gate.
