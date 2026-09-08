# Conditional cross-prefix \(q=1\) additive-child criterion

Date: 2026-07-27

Scope: the last formal boundary in the repaired-ring excess hierarchy.

## 0. Conditional status

This note proves an implication, not an unconditional closure theorem.
It assumes a hereditary stopped one-row edge/coin path-mesh maximum and
internal census through order \(2L+2\), including the non-disjoint
column-intersection extension used in Section 2.  Those stopped inputs
have not been proved after endogenous restriction.  Accordingly, every
closure claim below is conditional on that input.

Let (\tau) be a fully equality-resolved mixed type.  After collapsing
equal formal rows and equal owner witnesses, let (b(\tau)) be its number
of physical rows, let (\widetilde s(\tau)) be its number of distinct
physical witness incidences, and define its **physical excess**

\[
                       \rho=\widetilde s(\tau)-c(\tau).
\tag{0.0}
\]

All references below use \(d_t(X)^{b(\tau)}\), not the number of formal
row copies.  Let

\[
             S_\tau(t)=\sum_Xw_X(t)Z_{\tau,X}(t)
\tag{0.1}
\]

be its owner-incidence weighted count.  Write (Y_\tau(t)) for its
natural current-density base reference, including
\(d_t(X)^{b(\tau)}\) and without the excess factor, and
put

\[
       \alpha={CL^4\over m^2z^2}=m^{-19/10+o(1)},
 \qquad L=C_1(\log m)^2,qquad z=m^{-1/20}.
\tag{0.2}
\]

Assume the hereditary stopped one-row edge/coin path-mesh maximum and
internal census through order \(2L+2\), including the non-disjoint
column-intersection extension.  Their \(q=1\) drift would then have only
the already audited internal overlap term.

Conditional on that input, the cross-prefix overlap from the audit
satisfies the **absolute**
aggregate bound

\[
 \boxed{
 {\nu_t\sum_Xw_X\mathsf X_{\tau,X}\over Y_\tau(t)}
 \le C L^{C_0}\alpha^{\rho+1}.}
\tag{0.3}
\]

Consequently the normalized first moment obeys

\[
 {d^+\over dt}\mathbb E{S_\tau(t)\over Y_\tau(t)}
 \le
 \epsilon_m(t)\mathbb E{S_\tau(t)\over Y_\tau(t)}
 +CL^{C_0}\alpha^{\rho+1},
\tag{0.4}
\]

where \(\int_0^T|\epsilon_m|=o(1)\).  Since

\[
                         T L^{C_0}\alpha=o(1),
\tag{0.5}
\]

the static scale propagates:

\[
 \boxed{
       \mathbb E S_\tau(t)
       \le C\alpha^\rho Y_\tau(t)
       \qquad(0\le t\le T).}
\tag{0.6}
\]

This is the key point: one does **not** need a relative bound
\(\mathsf X_\tau\ll Z_\tau\).  When the parent happens to be tiny, the
child is still controlled by its absolute reference scale.  Thus the
one-level larger first-moment term does not recursively reopen the top.

Combining (0.6) with the top-strip threshold
\(\alpha^{3\rho/4}\) yields bad incidence

\[
 \exp[-\Omega((\log m)^3)]
\tag{0.7}
\]

after all diagram types and checkpoints are summed.  The exponent
\(3/4\), rather than (1/2), also makes the adjacent-level drift factor
(T\alpha^{3/4}=o(1)).

## 1. Exact cross-prefix term

Expose all but the last physical row.  Let (P_C) be the distinct
protected prefix resources and (S_C(f)) the unprotected resources of a
last-row option.  The exact terminal prefix contribution is

\[
                         \mathsf K_C=-\Lambda_t(P_C)A_C.
\tag{1.1}
\]

The exact last-row loss away from terminal prefix events is

\[
 \mathsf D_1(C;f)
 ={|S_C(f)|\over r}
  -\nu_t\bigl[J_t(P_C\cup S_C(f))-J_t(P_C)\bigr].
\tag{1.2}
\]

After removing the internal terms (J_t(P_C)) and (J_t(S_C(f))), the
only new contribution is

\[
 \mathsf X_C=
 \sum_{f\in\mathcal F_C}
 \bigl[J_t(P_C\cup S_C(f))-J_t(P_C)-J_t(S_C(f))\bigr].
\tag{1.3}
\]

It is bounded by

\[
 \mathsf X_C
 \le
 \sum_{f\in\mathcal F_C}
 \sum_{p\in P_C}\sum_{s\in S_C(f)}d_t(p,s).
\tag{1.4}
\]

This verifies that the missing term is neither an equality diagonal nor
an internal path overlap.  It is a common killing event between a prefix
resource and the last row.

## 2. Child-column representation

Reverse the pair-degree sum in (1.4).  A choice counted by (d_t(p,s))
is an active catalogue edge (g) containing (p) and (s).  In the
mixed diagram, (g) is one new column with one incidence in the prefix
and one incidence in the last row.  Hence

\[
                         \Delta\omega=2-1=1.
\tag{2.1}
\]

There are at most (L^{C_0}) choices of the two displayed incidences,
their orientations, and their witness positions.  Apply the current
row-exploration bound to the child diagram.  Before multiplication by
the edge-clock rate its new free column contributes (K\Delta_t) and
its second incidence contributes \(\alpha\).  Since

\[
                       \nu_tK\Delta_t={K\over r}=1+o(1),
\tag{2.2}
\]

summing all children gives

\[
 \nu_t\sum_Xw_X\mathsf X_{\tau,X}
 \le
 C L^{C_0}\alpha^{\rho+1}Y_\tau(t),
\tag{2.3}
\]

which is (0.3).

There is one disjointness qualification.  If the common future edge
\(g\) meets an already displayed protected column, merge \(g\) with that
column in the column-intersection forest.  Choosing \(g\) through the
fixed common resource costs at most \(\Delta_t\), rather than the free
\(K\Delta_t\), and its incidence with the last row still pays the one-row
path-mesh factor \(\alpha\).  After multiplication by
\(\nu_t=(r\Delta_t)^{-1}\), the lost factor \(K\) pays the displayed
position choices; multiple overlaps only improve the bound after the
usual forest partition.  Thus non-disjoint terminal children obey the
same polynomial-\(L\) version of (2.3).

A compensation clock common to the prefix and last row is the analogous
shared-resource child.  After resolving already displayed resource
equalities, a new common resource is one additional row--row owner
witness, costs the same factor \(\alpha\) by the one-row path-mesh
maximum, and has clock rate at most \(1/r\).  Its aggregate contribution
is therefore no larger than the edge-column term in (2.3).

The assumption at the start of the theorem is exactly what is needed in
this step.  It is a one-row stopped input, not the mixed top-strip
conclusion: when the child is exposed row by row, every old-column
condition on one new row is supplied by the one-row disjoint path-mesh
maximum, and every newly introduced column is supplied by the internal
census.  No relative child/parent estimate is used.

## 3. Duhamel closure

The product/current-density reference drift contains the marginal
hazards of all distinct physical resources.  The already audited internal
overlap terms contribute the multiplicative error \(\epsilon_m(t)\), with

\[
                         \int_0^T|\epsilon_m(t)|dt=o(1).
\tag{3.1}
\]

The cross-prefix term has the favorable sign for growth and is bounded by
(2.3).  Variation of constants gives

\[
 \mathbb E{S_\tau(t)\over Y_\tau(t)}
 \le e^{o(1)}
 \left[
 {S_\tau(0)\over Y_\tau(0)}
 +CTL^{C_0}\alpha^{\rho+1}
 \right].
\tag{3.2}
\]

The static row-exploration theorem gives the first term
(O(\alpha^\rho)).  Moreover

\[
 TL^{C_0}\alpha
 \le m\log m\,(\log m)^{O(1)}m^{-19/10+o(1)}
 =m^{-9/10+o(1)}.
\tag{3.3}
\]

Equations (3.2)--(3.3) prove (0.6).

## 4. Top-strip quarantine

Core compression gives at most

\[
                       \exp[O(\rho\log(\rho+1))]
\tag{4.1}
\]

types at excess \(\rho\).  Quarantine at the first crossing of

\[
                         \widehat Z_{\tau,X}
                         >\alpha^{3\rho/4}.
\tag{4.2}
\]

Stopped weighted Markov/Doob applied to (0.6) gives bad incidence at one
type at most (C\alpha^{\rho/4}) of the owner incidence.  For
\(\rho\ge L/4\), summing types and (O(\log m)) checkpoints yields

\[
\begin{aligned}
 \log\beta_m
 &\le O(\rho\log\rho)-{\rho\over4}\log(1/\alpha)\\
 &=-\Omega(L\log m)
 =-\Omega((\log m)^3).
\end{aligned}
\tag{4.3}
\]

On the retained top strip an adjacent one-child contribution has relative
size at most \(\alpha^{3/4}\).  Its total-time cost is

\[
                  T(\log m)^{O(1)}\alpha^{3/4}
                  =m^{-17/40+o(1)}=o(1).
\tag{4.4}
\]

Thus both the aggregate bad mass and the retained drift close.

## 5. Exact status

Conditional on the stated hereditary stopped input, the cross-prefix
\(q=1\) term is not a counterexample and does not require an infinite
recursion.  It is one absolute child level and closes by Duhamel because
\(T\alpha=o(1)\).

The stated hereditary stopped **one-row** edge/coin path-mesh maximum,
internal census, and non-disjoint extension through order \(2L+2\) are
not re-proved here and are not currently established.  They form a
strictly smaller target than mixed MDLE, but they are still a genuine
open boundary.  If they are proved, (0.3)--(0.7) close the mixed
first-moment top strip.

The proposed bootstrap is formally compatible if the hereditary stopped
input is supplied: stop each one-row variable at its first envelope
crossing, apply the deterministic row-exploration estimate before that
time, and quarantine the stopped exceptions.  This paragraph is a
conditional closure scheme, not a proof that the one-row stop rarely
fires.
