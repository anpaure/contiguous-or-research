# ST at the exact two-point gate: all-winding transfer, renewal blocks, and the proved asymptotic boundary

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

## 0. Result

Put

\[
 N=2r+1,\qquad B_r=\operatorname {Cat}_r,
 \qquad H=\lceil A\sqrt r\rceil,
 \qquad G=2H-1,
\]

where \(A>0\) is fixed.  Let \(E_H\) be the genuine PBBS return-start
set on quotient cycles of length greater than \(H+1\), and put

\[
 R_H=|E_H|,
 \qquad
 \mathcal C_H=\sum_{u=1}^{H+1}|E_H\cap\tau^{-u}E_H|.
\]

The global asymptotic of \(\mathcal C_H/R_H\) is **not** determined here.
In particular, neither boundedness nor divergence is claimed for the
long-period Pascal-saddle process.  The following theorem-level advances
are proved and audited in the companion reports cited below.

1. Firstness, duration, and every winding admit one exact killed-transfer
   operator.  Thus positive winding is not an error term.
2. On a reduced core, the predicate \(B_2\le G\) is an exact two-hit
   killed operator.  Orbitwise, its killed operator is a direct sum of
   nilpotent Jordan chains whose lengths are the genuine coordinate
   renewal gaps.  Hence a Perron-eigenvalue computation of this killed
   time operator cannot evaluate the desired ratio.
3. The complete predecessor-active count is a nearest-neighbour
   functional of two aligned renewal blocks.  The ratio \(K_{r,H}/S_{r,H}\)
   is exactly its Pascal-Palm susceptibility.
4. Fixing a terminal inverse occupancy \(z\) fixes the return winding on
   the entire exact inverse fibre.  The two-phase terminal-layer transport
   matrix is an explicit integral stars-and-bars matrix.
5. On the Pascal saddle, every pair contribution involving a positive
   terminal occupancy \(z\ge1\) is bounded by an absolute constant times
   its terminal-zero all-winding companion.  Therefore positive terminal
   occupancy creates no additional total-\(ST_A\) alternative.  The sole
   surviving process is terminal zero, with its winding label retained.
6. A complete genuine mountain inverse fibre has critical \(1/H\) start
   density and bounded susceptibility:

   \[
    H\frac{R_H^{\rm mt}}{|\Omega_{r,h}|}\to2Ac,
    \qquad
    \frac{\mathcal C_H^{\rm mt}}{R_H^{\rm mt}}\to2Ac,
   \]

   and its Palm neighbour count converges to
   \(\operatorname {Poisson}(2Ac)\).  This proves that genuine PBBS
   renewal does not uniformly force divergence.
7. The same mountain transfer can be evaluated with every positive
   winding.  Terminal occupancy \(z\) gives winding exactly \(z\) and a
   bounded two-point ratio.  However every active \(z\ge1\) mountain
   layer lies on a quotient cycle shorter than the ST cutoff and is
   deleted.  A one-generation spectator preserving the mountain core
   cannot change this.

Consequently the proved boundary is

\[
 \boxed{
  \frac{\mathcal C_H}{R_H}\asymp
  \mathbb E_{\rm active}^{\rm Pascal}
   \#\{1\le u\le H+1:\text{the aligned predecessor block at }2u
                         \text{ is active}\},}
\]

at critical saddle mass, with absolute comparison constants inherited
from the exact Pascal lift.  A bounded value, together with
\(R_H=\Omega_A(B_r/H)\), refutes \((ST_A)\).  Divergence is necessary for
\((ST_A)\).  The displayed Palm mean remains uncomputed on the genuine
long-period saddle cores.

## 1. Direct all-winding killed transfer

Let \(\Omega_N=\binom{[N]}r\) be the labelled PBBS state space, let
\({\cal U}\) be the one-step PBBS permutation, and let \(Q_j\) project
onto states whose unique unmatched coordinate is \(j\).  Put

\[
 K_j=(I-Q_j){\cal U},
 \qquad
 {\cal R}_{j,g}=Q_j{\cal U}K_j^{g-1}Q_j.
\]

Reading operators from right to left, \({\cal R}_{j,g}\) updates for
\(g\) steps, kills every proper-prefix visit to \(j\), and retains the
endpoint visit.  Hence

\[
 \Pi_H=\sum_j\sum_{g=1}^{G}{\cal R}_{j,g}^{*}{\cal R}_{j,g}
\]

is exactly the first-return indicator before the short-cycle deletion.
Let \(\Lambda_H\) be the invariant projection onto lifts of quotient
cycles longer than \(H+1\), and set

\[
 {\cal E}_H=\Lambda_H\Pi_H.
\]

Then

\[
 \boxed{
 NR_H=\operatorname {Tr}{\cal E}_H,\qquad
 N\mathcal C_H=
 \sum_{u=1}^{H+1}
 \operatorname {Tr}
  ({\cal E}_H{\cal U}^{-2u}{\cal E}_H{\cal U}^{2u}).}
 \tag{1.1}
\]

To retain winding, replace \({\cal U}\) by the monomial permutation

\[
 {\cal U}(z)e_x=z^{\delta(D(x))}e_{{\cal U}x}.
\]

If a first return has gap \(2s+1\) and winding \(w\), the exponent of
its unique monomial is

\[
 \boxed{(s-w)N.}                                  \tag{1.2}
\]

Indeed

\[
 \delta(D_j)+\delta(\phi D_j)=N-d(D_j)
\]

and the return equation is

\[
 \sum_{j=0}^{s-1}d(D_j)=\delta(D_s)+wN.
\]

Coefficient extraction in (1.2) therefore gives disjoint projections
\({\cal E}_{H,w}\) and the exact mixed-winding trace

\[
 N\mathcal C_H^{w,w'}=
 \sum_{u=1}^{H+1}
 \operatorname {Tr}
  ({\cal E}_{H,w}{\cal U}^{-2u}
   {\cal E}_{H,w'}{\cal U}^{2u}).                \tag{1.3}
\]

## 2. The reduced two-hit operator and renewal-block identity

Work orbitwise with equality particles labelled persistently in their
cyclic order.  This is the particle-labelled augmentation of the reduced
PBBS quotient; the projection \(Q_j^{\rm par}\) now means that persistent
particle \(j\) is selected.  If the current particle is \(j\), its
immediate predecessor is \(b=j-1\).  The same killed-operator construction
gives an exact two-hit projection for the first two future selections of
\(b\).  Summing over hit gaps \(a,b'\ge1\), \(a+b'\le G\), gives exactly

\[
 A_G(F)=\mathbf1_{\{B_2(F)\le G\}}.              \tag{2.1}
\]

With the exact inverse-Pascal weight

\[
 P_r(F)=\binom{r+d-\operatorname {pk}(F)}{2d},
\]

the weighted one- and two-point quantities are literal traces of this
projection and its \(2u\)-step conjugates.  This is the operator form of
the audited predecessor transmission.

There is an exact orbitwise normal form.  Fix a persistent particle
\(b\), list its successive selection times cyclically as

\[
 t_{b,1}<t_{b,2}<\cdots,
 \qquad
 g_{b,i}=t_{b,i+1}-t_{b,i}.
\]

On that orbit,

\[
 (I-Q_b^{\rm par}){\cal U}
 \simeq\bigoplus_i J_{g_{b,i}},                  \tag{2.2}
\]

where \(J_g\) is the nilpotent forward shift on a chain of length \(g\).
All eigenvalues are therefore zero.

The missing datum is visible without operator notation.  Put \(a=b+1\).
A phase \(s\) in the block

\[
 t_{b,i-1}<s<t_{b,i}
\]

is predecessor-active precisely when

\[
 \boxed{
  \kappa_s=a,
  \qquad
  (t_{b,i}-s)+g_{b,i}\le G.}                    \tag{2.3}
\]

Thus one active count needs the placement of successor visits in the
suffix of one \(b\)-block together with the length of the next block.
The two-point count additionally needs the relative alignment of these
renewal decompositions for different persistent particles.

After summing with the Pascal weights,

\[
 \boxed{
 {K_{r,H}\over S_{r,H}}
 =\mathbb E_{\rm active}^{\rm Pascal}
   \#\{1\le u\le H+1:A_G(\tau^uF)=1\}.}          \tag{2.4}
\]

The one-gap histogram, the nilpotent spectrum (2.2), and every one-time
marginal omit the alignments in (2.3)--(2.4).

## 3. Exact terminal-layer transport, with winding

Fix a first-pruned core \(F\in\mathcal D_d\) with \(k\) peaks.  Put

\[
 y=r-d-k,\qquad p=2d+1,\qquad M=r+d-k.
\]

After compulsory leaves are removed, the inverse fibre is the weak
composition simplex of \(y\) into \(p\) slots.  Its total size and its
terminal-\(z\) layer are

\[
 P_r(F)=\binom M{2d},
 \qquad
 K_z(d,k)=\binom{M-z-1}{2d-1}.                  \tag{3.1}
\]

If \(B_{2z+2}(F)\le G<N\), the exact adjacent-particle theorem gives the
same first-return gap to every lift in this layer.  Persistent particle
order also gives the same integer degree of the closed normalized-label
trajectory.  Hence the winding

\[
 \omega_z(F)
\]

is constant on the whole terminal layer.

At phase \(u\), the transported terminal free occupancy is one initial
free coordinate \(q_{\eta_u}\).  The apparent affine shift in the total
gap formula cancels exactly against the transported compulsory occupancy.
Consequently the two-phase layer entry is

\[
 \boxed{
 J_u(F;z,z')=
 \begin{cases}
  \displaystyle\binom{M-z-z'-2}{2d-2},&\eta_u\ne0,\\[2mm]
  K_z(d,k),&\eta_u=0\text{ and }z'=z,\\
  0,&\eta_u=0\text{ and }z'\ne z.
 \end{cases}}                                    \tag{3.2}
\]

This is an integral transportation matrix.  Its row sums are \(K_z\)
and its column sums are \(K_{z'}\).

On the Pascal saddle

\[
 d={r\over2}+O(\sqrt{r\log r}),
 \qquad
 k={r\over6}+O(\sqrt{r\log r}),
\]

uniformly for \(z+z'=O(\log r)\),

\[
 {K_z\over P_r(F)}=left({3\over4}+o(1)\right)4^{-z},
 \tag{3.3}
\]

and, for distinct transported coordinates,

\[
 {J_u(F;z,z')\over P_r(F)}
 =\left({9\over16}+o(1)\right)4^{-(z+z')}.       \tag{3.4}
\]

For terminal zero, two active phase subsets each have density
\(\alpha=3/4+o(1)\), so their intersection has density at least
\(2\alpha-1=1/2+o(1)\).  This remains true after restricting to any
fixed sets of winding labels, because \(\omega_0(F)\) is a core-layer
label.

Positive terminal occupancies have total density

\[
 \beta=1-\alpha={1\over4}+o(1).                  \tag{3.5}
\]

For any reduced active phase pair, let \(S_0\) be the terminal-zero
subset and \(S_+\) the union of all eligible \(z\ge1\) layers.  Then

\[
 |S_+\cap\Sigma^{-u}S_+|
 \le {\beta\over2\alpha-1}
      |S_0\cap\Sigma^{-u}S_0|,                  \tag{3.6}
\]

and the number of common parents with at least one positive terminal
occupancy is at most

\[
 {2\beta\over2\alpha-1}
      |S_0\cap\Sigma^{-u}S_0|.                  \tag{3.7}
\]

The saddle constants in (3.6)--(3.7) are \(1/2+o(1)\) and \(1+o(1)\).
Thus positive terminal occupancy is quantitatively subordinate to the
terminal-zero all-winding correlation.  Positive winding with \(z=0\)
is still present and is retained by the winding-labelled predicate
\(\omega_0(F)>0\).

## 4. A computed genuine bounded-renewal sector

Let \(p=2h-1\) be prime, let \(h/\sqrt r\to c\), and assume

\[
 {A\over2}<c<A.
\]

The complete inverse fibre over the rank-\((h-1)\) mountain is

\[
 \Omega_{r,h}={(n_0,\ldots,n_{p-1})\ge0:
                         \sum_jn_j=r-h\}.
\]

The literal PBBS map rotates the coordinates, and a phase is active
exactly when its current coordinate is zero.  Every active return has
gap \(2h+1\), winding zero, and lies on a quotient cycle longer than
\(H+1\).  Stars and bars gives

\[
 |\Omega_{r,h}|=\binom{r-h+p-1}{p-1},
 \qquad
 R_H^{\rm mt}=\binom{r-h+p-2}{p-2},              \tag{4.1}
\]

\[
 \mathcal C_H^{\rm mt}
 =(H+1)\binom{r-h+p-3}{p-3}.                    \tag{4.2}
\]

Hence

\[
 H{R_H^{\rm mt}\over|\Omega_{r,h}|}\to2Ac,
 \qquad
 {\mathcal C_H^{\rm mt}\over R_H^{\rm mt}}\to2Ac.          \tag{4.3}
\]

Conditioned on an active phase, the factorial moments of the number
\(X\) of future active phases in the ST window are

\[
 \mathbb E(X)_q
 =(H+1)_q{(p-2)_q\over(r-h+p-2)_q}
 \longrightarrow(2Ac)^q,                       \tag{4.4}
\]

so \(X\Rightarrow\operatorname {Poisson}(2Ac)\).

This is a genuine retained PBBS sector with critical fibre density and
bounded susceptibility.  Its total size is only
\(\exp(O(\sqrt r\log r))\), and its first-pruned core has period one.
It therefore does not give critical Catalan mass.

## 5. Exact mountain positive winding and its short-cycle obstruction

In the same mountain fibre, terminal occupancy \(n_0=z\) has

\[
 \boxed{
  g_z=2+(2z+1)p,
  \qquad s_z=h+zp,
  \qquad w_z=z.}                                 \tag{5.1}
\]

For a fixed finite winding set \(S\), put

\[
 R_S=\sum_{a\in S}\binom{y-a+p-2}{p-2},
 \qquad
 J_S=\sum_{a,b\in S}\binom{y-a-b+p-3}{p-3}.
\]

For every \(L\ge1\), coordinate rotation gives the exact cyclic renewal

\[
 \mathcal C_S(L)=left\lfloor{L\over p}\right\rfloor R_S+
 \left(L-left\lfloor{L\over p}\right\rfloor\right)J_S.
 \tag{5.2}
\]

If \(h/\sqrt r\to c\), \(H/\sqrt r\to A\), and \(S\) is fixed, then

\[
 {\mathcal C_S(H+1)\over R_S}
 =\left\lfloor{H+1\over p}\right\rfloor+2Ac|S|+o(1),       \tag{5.3}
\]

which is bounded.

This positive-winding asymptotic does not survive the retained-cycle
cut.  If any \(z\ge1\) is active, then

\[
 3p+2\le2H-1,
 \qquad\text{so}\qquad p<H+1.                  \tag{5.4}
\]

Every mountain-fibre quotient orbit has period dividing \(p\), so all
such positive starts are deleted.  The weak-composition fibre is the
complete one-generation inverse fibre and satisfies \(\tau^p=1\);
there is no deletion-preserving spectator at this inverse level which
can lengthen the period.  A deeper spectator changes the first-pruned
core and its predecessor itinerary, and remains unconstructed.

## 6. Exact implication boundary

The computed formulas prove that finite susceptibility is compatible
with literal PBBS dynamics, firstness, Gaussian residence, and critical
\(1/H\) density inside an exact fibre.  They also prove that positive
terminal layers are not an independent source of divergent correlation.

They do **not** prove either of the two global estimates

\[
 R_H=\Theta_A(B_r/H),
 \qquad
 \mathcal C_H=O_A(R_H),                          \tag{6.1}
\]

and they do not prove \(\mathcal C_H/R_H\to\infty\).  The exact missing
theorem is a limit law for the aligned blocks (2.3), simultaneously over
all persistent particles, on the long-period cores in the Pascal saddle.
It must retain the terminal-zero winding label and the actual identity
\(D_{i+1}=\tau D_i\).

The source theorems are:

* `MATH_THEOREM_N_ST_KILLED_TRANSFER_AND_RENEWAL_BLOCK_GATE_20260726.md`;
* `MATH_THEOREM_N_ST_POSITIVE_WINDING_TWO_POINT_TRANSFER_20260726.md`;
* `MATH_THEOREM_N_ST_ZERO_WINDING_MOUNTAIN_RENEWAL_SUSCEPTIBILITY_20260726.md`;
* `MATH_THEOREM_N_ST_MOUNTAIN_POSITIVE_WINDING_RENEWAL_AND_SHORT_CYCLE_NOGO_20260726.md`.
