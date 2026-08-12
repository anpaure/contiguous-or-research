# Lane C: the reflection-even companion Haar block

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or probabilistic experiment is used. Random signs below average a
finite family of literal integral exact factors.

## 0. Result

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad B=\operatorname{Cat}_m=\frac Wn,
\qquad H=\lceil A\sqrt m\rceil,
\]

and let \(\mathcal Q_H\), \(c_q\), the canonical MSW factor \(F^0\), the
reflection \(\sigma\), the transpositions

\[
\tau=(2\ 3),\qquad \tau'=\sigma\tau\sigma,
\]

the terminal-chart-free set \(\mathcal I\), and the size-two packet trades
\(z_R\), \(R\in\mathcal I\), be exactly as in
`MATH_ATTACK_C_REFLECTED_CHART_HAAR_CONTRACTION_20260725.md`.  Thus the
root packets

\[
\{U_R,\sigma U_R:R\in\mathcal I\}
\tag{0.1}
\]

are pairwise disjoint, \(U_R\) is \(\tau\)-invariant, and \(\sigma U_R\)
is \(\tau'\)-invariant.

Switch both members of every reflected pair and put

\[
F^{++}=F^0+\sum_{R\in\mathcal I}(z_R+\sigma z_R).
\tag{0.2}
\]

For \(\varepsilon\in\{\pm1\}^{\mathcal I}\), define \(F_\varepsilon^+\)
by choosing coherently on each reflected root pair:

\[
\begin{array}{c|cc}
&U_R&\sigma U_R\\ \hline
\varepsilon_R=-1&K_R&\sigma K_R\\
\varepsilon_R=+1&\tau K_R&\sigma\tau K_R.
\end{array}
\tag{0.3}
\]

All roots outside (0.1) retain their rows from \(F^0\).

### Theorem 0.1 (reflection-even Haar contraction)

For every fixed \(A>0\) and all sufficiently large \(m\):

1. every \(F_\varepsilon^+\) is a literal exact factor and is fixed by
   \(\sigma\);
2. from either endpoint \(F^0\) or \(F^{++}\), every corner is reachable
   by at most two freshly recomputed complete component cuts, in colours
   \(\tau\) and \(\tau'\);
3. if the signs are independent and fair, then

   \[
   \boxed{
   \mathbb E\mathcal Q_H(F_\varepsilon^+)
   \le
   \max\{\mathcal Q_H(F^0),\mathcal Q_H(F^{++})\}
   -\frac{B4^H}{512M_AH^4}+8HB,}
   \tag{0.4}
   \]

   where

   \[
   M_A=\left\lceil e^{2(A+1)(A+2)}\right\rceil;
   \]

4. consequently one corner satisfies

   \[
   \boxed{
   \mathcal Q_H(F_\varepsilon^+)
   \le
   \max\{\mathcal Q_H(F^0),\mathcal Q_H(F^{++})\}
   -\frac{B4^H}{1024M_AH^4}.}
   \tag{0.5}
   \]

Moreover a corner satisfying the weaker bound with denominator \(2048\)
may be required to have both signs.  It is then reached from the higher
endpoint by two nonempty proper freshly recomputed cuts.

All profiles in (0.3) are reflection-invariant.  If \(c\) is the midpoint
of the two endpoint profiles, then

\[
\boxed{
\frac{\mathbb E\|f(F_\varepsilon^+)-c\|_H^2}
{\|f(F^{++})-c\|_H^2}
\le \frac{4096M_AH^5}{4^H}=o_A(1).}
\tag{0.6}
\]

Thus the reflected chart has an even as well as an odd Haar mode.  The odd
mode in the source report burns a reflection-anti-invariant coherent
profile; (0.6) burns a genuine reflection-invariant coherent profile with
the same quantitative ratio.

This does not contract an arbitrary reflection-invariant residue.  The
midpoint \(c\) is left fixed, and no iteration theorem placing a new chart
signal through every invariant direction is proved.

## 1. Exactness and two-cut realization

The two-row families in (0.1) are pairwise root-disjoint.  On each
\(U_R\), either \(K_R\) or \(\tau K_R\) partitions the same roots.  On
\(\sigma U_R\), either \(\sigma K_R\) or \(\sigma\tau K_R\) partitions
the same roots.  Independent choices in (0.3) therefore preserve every
middle root exactly once.  Hence every corner is an integral exact factor.

Reflection interchanges the two root packets in each row of (0.3):

\[
\sigma(K_R\cup\sigma K_R)=K_R\cup\sigma K_R,
\qquad
\sigma(\tau K_R\cup\sigma\tau K_R)
=\tau K_R\cup\sigma\tau K_R.
\]

The complement of (0.1) is reflection-invariant and retains the
reflection-invariant factor \(F^0\).  Thus

\[
\boxed{\sigma F_\varepsilon^+=F_\varepsilon^+.}
\tag{1.1}
\]

Starting at \(F^0\), let

\[
S=\{R:\varepsilon_R=+1\}.
\]

In the fresh \(\tau\)-overlay switch the complete components on \(U_R\),
\(R\in S\).  Then, in the freshly recomputed \(\tau'\)-overlay, switch
the complete components on \(\sigma U_R\), \(R\in S\).  Root invariance
seals each displayed packet from all other roots.  The first cut changes no
row on a reflected packet, so every component used by the second cut
persists exactly.

Starting at \(F^{++}\), perform the same two cuts for
\(S=\{R:\varepsilon_R=-1\}\), now returning those pairs to their old
shores.  This proves the claimed reachability.  If both signs occur, both
cuts are nonempty; because a nonempty complementary family of displayed
components remains unswitched, both cuts are proper even before counting
the other components of the two overlays.

More generally, even selecting all of \(\mathcal I\) is proper.  The union

\[
U=\mathop{\dot\bigcup}_{R\in\mathcal I}U_R
\]

is \(\tau\)-invariant and has

\[
|U|=2n|\mathcal I|<2n\operatorname{Cat}_{m-2}<nB=W
\]

for all sufficiently large \(m\).  Hence its nonempty complement is also
\(\tau\)-invariant and contains at least one unswitched fresh component.
The reflected union has the same strict size bound and gives the identical
argument for \(\tau'\).  Thus any corner different from the chosen starting
endpoint is reached from it by two nonempty proper cuts, including when the
corner is the opposite coherent endpoint.

## 2. Exact even-Haar identity

Let

\[
d_R=(B_{m-q}z_R)_{q\le H},\qquad
k_R=d_R+\sigma d_R,
\]

\[
K=\sum_{R\in\mathcal I}k_R,\qquad
A_+=\|K\|_H^2,\qquad
V_+=\sum_{R\in\mathcal I}\|k_R\|_H^2.
\tag{2.1}
\]

Write \(f^0=f(F^0)\).  The endpoint profiles are

\[
f(F^0)=f^0,\qquad f(F^{++})=f^0+K.
\]

Their midpoint is

\[
c=f^0+\frac K2,
\tag{2.2}
\]

and every corner has the exact profile

\[
\boxed{
f(F_\varepsilon^+)
=c+\frac12\sum_{R\in\mathcal I}\varepsilon_Rk_R.}
\tag{2.3}
\]

Every vector in (2.2)--(2.3) is \(\sigma\)-invariant.

Fair signs kill all cross terms between distinct bundles, giving

\[
\mathbb E\|f(F_\varepsilon^+)-c\|_H^2=\frac{V_+}{4},
\qquad
\|f(F^{++})-c\|_H^2=\frac{A_+}{4}.
\tag{2.4}
\]

The adjacent-integer floor subtraction is factor-independent.  Applying
the parallelogram identity to the two endpoint profiles gives the exact
energy identity

\[
\boxed{
\mathbb E\mathcal Q_H(F_\varepsilon^+)
=\frac{\mathcal Q_H(F^0)+\mathcal Q_H(F^{++})}{2}
+\frac{V_+-A_+}{4}.}
\tag{2.5}
\]

In particular,

\[
\mathbb E\mathcal Q_H(F_\varepsilon^+)
\le
\max\{\mathcal Q_H(F^0),\mathcal Q_H(F^{++})\}
-\frac{A_+-V_+}{4}.
\tag{2.6}
\]

## 3. Coherent signal and variance

At depth \(H\), for each terminal-chart-free
\(V\in\mathcal D_{m-H-2}\), the packets

\[
R=UV,\qquad U\in\mathcal D_H,
\]

give one coherently oriented dipole of coefficient
\(\operatorname{Cat}_H\) on the private target pair.  The original private
targets contain \(2m,n\) and omit \(1\); the reflected targets contain
\(1,n\) and omit \(2m\).  The two private families are disjoint, and every
nonprivate arm in either family omits \(n\).  Therefore the same private
coordinate argument used for the odd Haar mode gives

\[
A_+
\ge
\frac{4(\operatorname{Cat}_{m-H-2}-2\operatorname{Cat}_{m-H-4})
\operatorname{Cat}_H^2}{c_H}
>
\frac{B4^H}{128M_AH^4}.
\tag{3.1}
\]

The exact four-arm profile obeys

\[
\|d_R\|_H^2
=\frac4{c_1}+8\sum_{q=2}^H\frac1{c_q}<8H.
\]

Since \(\sigma\) is an isometry,

\[
\|k_R\|_H^2
=\|d_R+\sigma d_R\|_H^2
\le4\|d_R\|_H^2<32H.
\]

There are fewer than \(B\) bundles, so

\[
\boxed{V_+<32HB.}
\tag{3.2}
\]

Substitution of (3.1)--(3.2) into (2.6) proves (0.4).  Since
\(4^H/(M_AH^5)\to\infty\), for all sufficiently large \(m\),

\[
\frac{A_+-V_+}{4}
>\frac{B4^H}{1024M_AH^4}.
\tag{3.3}
\]

Some corner has energy no greater than the average, proving (0.5).
Equations (2.4), (3.1), and (3.2) prove (0.6).

## 4. Extraction of a genuinely mixed corner

It remains only to justify the optional mixed-corner assertion, because in
the even mode the two coherent endpoints need not have equal energy.

Let \(L=|\mathcal I|\) and \(N=2^L\).  The exact terminal count is

\[
L=\operatorname{Cat}_{m-2}-2\operatorname{Cat}_{m-4}
\ge\frac12\operatorname{Cat}_{m-2}
\tag{4.1}
\]

for all sufficiently large \(m\).  At each depth, the centered quadratic
identity gives \(0\le Q_q(F)\le W^2\); hence

\[
0\le\mathcal Q_H(F)\le HW^2
\tag{4.2}
\]

for every exact factor.

Put

\[
C=\frac{B4^H}{1024M_AH^4},\qquad
Q_{\rm hi}=\max\{\mathcal Q_H(F^0),\mathcal Q_H(F^{++})\}.
\]

By (0.4)--(3.3), the average over all \(N\) corners is at most
\(Q_{\rm hi}-C\).  Removing the two coherent endpoints and using only
nonnegativity, the average over the remaining \(N-2\) mixed corners is at
most

\[
\frac{N(Q_{\rm hi}-C)}{N-2}.
\tag{4.3}
\]

Equations (4.1)--(4.2) imply

\[
NC>4Q_{\rm hi}
\tag{4.4}
\]

for all sufficiently large \(m\): \(L\) is exponential in \(m\), so
\(N=2^L\) dominates \(HW^2/C\).  From (4.3)--(4.4),

\[
\frac{N(Q_{\rm hi}-C)}{N-2}
\le Q_{\rm hi}-\frac C2.
\]

Thus some genuinely mixed corner has

\[
\boxed{
\mathcal Q_H(F_\varepsilon^+)
\le Q_{\rm hi}-\frac{B4^H}{2048M_AH^4}.}
\tag{4.5}
\]

Section 1 reaches it from the higher endpoint by two nonempty proper fresh
component cuts.

## 5. High-harmonic form and exact boundary

For

\[
J=\left\lfloor\frac{\gamma H}{\log(108m)}\right\rfloor,
\qquad0<\gamma<\log4,
\]

the universal run cap bounds the low-degree energy of both exact endpoints
by

\[
U=\frac{BH^3}{n}e^{\gamma H}.
\]

Their low-degree squared displacement is at most \(4U\).  Hence

\[
A_+^{>J}
>\frac{B4^H}{128M_AH^4}-4U,
\qquad
V_+^{>J}<32HB,
\tag{5.1}
\]

and therefore

\[
\boxed{\frac{V_+^{>J}}{A_+^{>J}}=o_{A,\gamma}(1).}
\tag{5.2}
\]

This is a literal reflection-invariant shield-burning block.  It closes the
formal concern that the reflected chart can act only on an odd symmetry
sector.  What remains open is coverage: neither (0.6) nor (5.2) says that
the fixed midpoint \(c\), or an arbitrary reflection-invariant residual of
a previous odd block, has small energy.  A constant-one iteration still
requires overlapping reflected reservoirs or a state-adaptive sequence of
involutions with a uniform spectral gap on those successive midpoints.
