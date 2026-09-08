# Conditional additive-child criterion for the first-moment top strip

Date: 2026-07-27

Scope: constant-one repaired promotion-ring slow-greedy hierarchy.

## 0. Conditional result

Let \(k=(1+o(1))m\) be the owner count of a repaired edge and
\(K=k+1\) its total resource count.  Put

\[
 L=C_1(\log m)^2,\qquad J=C_0\log m,\qquad
 \rho_*=\left\lfloor{L-2\over4}\right\rfloor+1.
\tag{0.1}
\]

Run to survivor density \(z=m^{-1/20}\), and define the common
edge/coin endpoint parameter

\[
 \alpha={CL^4\over m^2z^2}=m^{-19/10+o(1)}.
\tag{0.2}
\]

Assume the following inputs:

1. arbitrary equality-resolved static mixed diagrams by row
   exploration;
2. the graded stochastic moments \(q(2\rho+1)\le L\); and
3. a hereditary stopped one-row edge-column and compensation-resource
   path-mesh maximum/internal census through order \(2L+2\), including
   the non-disjoint column-intersection extension used in Section 2.

Item 3 is not currently proved after endogenous restriction.  It is the
only stopped boundary input used below; no mixed top-strip moment or
relative child/parent estimate is assumed.

For every top-strip type \(\tau\) of excess
\(\rho_*\le\rho\le L\), let \(S_\tau(t)\) be its
owner-incidence-marked count and \(Y_\tau(t)\) its complete
current-density first-moment base, excluding \(\alpha^\rho\).
Precisely, the quotient notation below means

\[
 {S_\tau(t)\over Y_\tau(t)}
 :=
 {1\over kE_{\rm ref}(t)}
 \sum_Xd_t(X){Z_{\tau,X}(t)\over B_{\tau,X}(t)}.
\tag{0.2a}
\]

The root-incidence version replaces \(kE_{\rm ref}\) by
\(E_{\rm ref}\).

Then

\[
 \boxed{
 \mathbb E\,{S_\tau(t)\over Y_\tau(t)}
 \le C_\tau\alpha^\rho
 \qquad(0\le t\le T),}
\tag{0.3}
\]

where

\[
                         C_\tau\le\exp[C\rho\log(\rho+1)].
\tag{0.4}
\]

The exact cross-prefix edge/coin mass obeys the stronger additive
estimate

\[
 \boxed{
 {1\over kE_{\rm ref}(t)}
 \sum_X{d_t(X)\over B_{\tau,X}(t)}
 \left[
 \nu_t\mathsf X_{\tau,X}^E(t)
 +\mathsf X_{\tau,X}^\circ(t)
 \right]
 \le C L^{C_2}\alpha^{\rho+1}.}
\tag{0.5}
\]

Thus the first-moment top strip remains at \(O(\alpha^\rho)\).
No relative child/parent estimate and no all-order ordered tower are
needed.

Stop an owner center when

\[
 \sum_{\rho=\rho_*}^{L}\ \sum_{\tau\in\mathcal T_\rho}
 \alpha^{-3\rho/4}
 {Z_{\tau,X}(t)\over B_{\tau,X}(t)}>1.
\tag{0.6}
\]

With probability \(1-o(1)\), the total normalized stopped incidence is

\[
 \boxed{
 \sum_{X\ {\rm stopped}}
 {d_{\tau_X}(X)\over kE_{\rm ref}(\tau_X)}
 \le\beta,\qquad
 \beta=\exp[-c(\log m)^3].}
\tag{0.7}
\]

The root-centered analogue has \(d_{\tau_R}(R)/E_{\rm ref}(\tau_R)\).
After conversion by current degrees, all analytically quarantined
owners and roots cost \(o(N_H)\) matching roots.  If a literal core is
required, one one-generation cleaning loses at most

\[
                         \eta N_H=o(N_H),\qquad
 \eta=\sqrt{\beta k},
\tag{0.8}
\]

The \(O(m\log m)\) degree-reference slabs are used only to convert the
time-varying normalized charge into current root degrees; their number
does not enter \(\eta\).  Secondary high-loss owners are stopped but
their remaining stars are not removed, so no cascade occurs.

Thus the stated input would close the first-moment part of the graded top
strip.  This note does not prove that hereditary input and therefore is
not an unconditional closure theorem.

## 1. Exact prefix/last-row hazard

Fix an equality-resolved physical prefix \(C\).  Let \(P_C\) be the
union of its distinct protected resources.  For a compatible last row
\(f\), put

\[
                         R_C(f)=V(f)\setminus P_C.
\tag{1.1}
\]

For any active resource set \(A\), write

\[
 \mathcal E_t(A)=\bigcup_{y\in A}\mathcal E_t(y).
\tag{1.2}
\]

Every active edge has rate
\(\nu_t=(k\Delta_t)^{-1}\), while resource \(y\) has compensation rate
\((\Delta_t-d_t(y))/(k\Delta_t)\).  Thus every single resource has
total marginal hazard \(k^{-1}\).

Because \(P_C\cap R_C(f)=\varnothing\), the exact compensated hazard
identity is

\[
\begin{aligned}
 \Lambda_t(P_C\cup R_C(f))
 &=\Lambda_t(P_C)+\Lambda_t(R_C(f))\\
 &\quad-\nu_t
 |\mathcal E_t(P_C)\cap\mathcal E_t(R_C(f))|.
\end{aligned}
\tag{1.3}
\]

The terminal prefix-death term is not discarded.  It cancels the
prefix-survival derivative in \(Y_\tau(t)\).  After the already proved
individual prefix and last-row first-moment errors are removed, the
remaining positive edge term is

\[
 \mathsf X_C^E
 =
 \sum_{f\in\mathcal F_C}
 |\mathcal E_t(P_C)\cap\mathcal E_t(R_C(f))|.
\tag{1.4}
\]

Equivalently,

\[
 \mathsf X_C^E
 \le
 \sum_{f\in\mathcal F_C}
 \sum_{p\in P_C}\sum_{y\in R_C(f)}d_t(p,y).
\tag{1.5}
\]

After equality resolution \(P_C\cap R_C(f)=\varnothing\), so distinct
compensation clocks are exactly additive and there is no physical
cross-prefix coin term.  If the formal expansion is performed before
equality resolution, a resource \(y\) displayed in both the prefix and
last row is counted twice but rings once.  Resolving that equality is
equivalently one shared-resource child; denote this harmless formal
overcount, including its coin rate, by \(\mathsf X_C^\circ\).

Equations (1.3)--(1.5) are the complete first-moment correction.  In
particular, marginal compensation alone would not prove (0.3); the
cross-prefix term must be paid.

## 2. The cross-prefix term is one absolute child

Reverse the pair-degree sum in (1.5).  A choice counted by
\(d_t(p,y)\) is one active catalogue edge \(g\) containing a prefix
resource \(p\) and a genuinely new last-row resource \(y\).  In the
mixed diagram, \(g\) is one new column with two incidences.  Hence

\[
                         \Delta\omega=2-1=1.
\tag{2.1}
\]

Expose the child diagram row by row.  Every old-column condition on the
new last row is supplied by the proved stopped one-row disjoint
path-mesh maximum.  Every column first introduced from that row is
supplied by the proved internal census.  The new cross-prefix column
has one free incidence and one endpoint incidence, so it contributes

\[
                         (K\Delta_t)\alpha
\tag{2.2}
\]

before its clock rate.  Since

\[
                         \nu_tK\Delta_t={K\over k}=1+o(1),
\tag{2.3}
\]

the aggregate edge children satisfy

\[
 {1\over kE_{\rm ref}(t)}
 \sum_X{d_t(X)\over B_{\tau,X}(t)}
 \nu_t\mathsf X_{\tau,X}^E(t)
 \le C L^{C_2}\alpha^{\rho+1}.
\tag{2.4}
\]

The polynomial \(L^{C_2}\) pays the choices of the two displayed
incidences, orientations, and witness positions.  It is independent of
the number of private columns, which have already been summed.

If \(g\) meets an already displayed protected column, merge it into the
column-intersection forest.  Its first incidence then has at most
\(\Delta_t\), rather than \(K\Delta_t\), choices.  The factor \(K^{-1}\)
gained after the clock normalization pays the displayed position.
Further intersections only merge more forest components and do not
worsen (2.4).

For a formal compensation child, one resource is common to the prefix
and last row before equality resolution.  Its first occurrence has at
most \(K\) positions, its second occurrence pays the resource endpoint
factor \(\alpha\), and its clock rate is at most \(k^{-1}\).  Thus

\[
 {1\over kE_{\rm ref}(t)}
 \sum_X{d_t(X)\over B_{\tau,X}(t)}
 \mathsf X_{\tau,X}^\circ(t)
 \le C L^{C_2}\alpha^{\rho+1}.
\tag{2.5}
\]

Equations (2.4)--(2.5) prove (0.5).

In the completely equality-resolved physical-union formulation,
\(\mathsf X^\circ=0\); retaining (2.5) simply makes the theorem
compatible with the formal mixed-diagram bookkeeping.

This is an absolute child bound.  It does not divide by the current
parent mass.  Therefore a tiny parent causes no singular ratio, and the
child level does not need to be propagated recursively.

## 3. Duhamel closure at \(O(\alpha^\rho)\)

Put

\[
                         U_\tau(t)={S_\tau(t)\over Y_\tau(t)}.
\tag{3.1}
\]

The exact prefix cancellation in Section 1, the individual one-row
first-moment comparison, and (0.5) give the stopped pathwise generator
inequality

\[
 \mathcal G U_\tau(t)
 \le
 \epsilon_\tau(t)U_\tau(t)
 +C L^{C_2}\alpha^{\rho+1}.
\tag{3.2}
\]

Consequently

\[
 {d^+\over dt}\mathbb E U_\tau(t)
 \le
 \epsilon_\tau(t)\mathbb E U_\tau(t)
 +C L^{C_2}\alpha^{\rho+1},
\tag{3.2a}
\]

where

\[
                         \int_0^T|\epsilon_\tau(t)|\,dt=o(1)
\tag{3.3}
\]

uniformly over top-strip types.  Static row exploration gives

\[
                         U_\tau(0)\le C_\tau\alpha^\rho.
\tag{3.4}
\]

Variation of constants yields

\[
 \mathbb E U_\tau(t)
 \le e^{o(1)}
 \left[
 C_\tau\alpha^\rho
 +
 CTL^{C_2}\alpha^{\rho+1}
 \right].
\tag{3.5}
\]

But

\[
 TL^{C_2}\alpha
 \le
 m\log m\,(\log m)^{O(1)}m^{-19/10+o(1)}
 =m^{-9/10+o(1)}=o(1).
\tag{3.6}
\]

This proves (0.3).  The only level above the parent appears additively
and is integrable; there is no infinite boundary chain.

## 4. Marked-incidence maximal inequality

For quarantine one needs a maximal, incidence-weighted statement, not
only (3.5).  Realize the owner weight \(d_t(X)\) by marking one actual
live catalogue incidence through \(X\).  Include its deterministic
incidence reference

\[
                         \mathfrak I_O(t)=kE_{\rm ref}(t)
\tag{4.1}
\]

in the base.  Death of the mark is terminal; a common event involving
it is another one-row child already bounded by Section 2.  Thus no
random degree is multiplied into a supermartingale after the fact.

After the harmless integrating factor for \(\epsilon_\tau\), (3.2)
has deterministic source

\[
                         a_\tau(t)\le CL^{C_2}\alpha^{\rho+1}.
\tag{4.2}
\]

Define the backward reserve

\[
 V_\tau(t)=
 e^{-\int_0^t\epsilon_\tau}
 U_\tau(t)
 +
 \int_t^T
 e^{-\int_0^v\epsilon_\tau}a_\tau(v)\,dv.
\tag{4.3}
\]

The stopped generator of \(V_\tau\) is nonpositive, and
\(V_\tau\ge e^{-o(1)}U_\tau\).  Moreover,

\[
 \mathbb EV_\tau(0)
 \le C_\tau\alpha^\rho
 +
 CTL^{C_2}\alpha^{\rho+1}
 \le 2C_\tau\alpha^\rho.
\tag{4.4}
\]

Sum

\[
                         \alpha^{-3\rho/4}V_\tau
\tag{4.5}
\]

over all top-strip types and stop each marked center at its first
crossing of (0.6).  At a crossing, the marked potential contributes at
least

\[
                         {d_{\tau_X}(X)\over
                           \mathfrak I_O(\tau_X)}.
\tag{4.6}
\]

Core compression gives

\[
                         |\mathcal T_\rho|
 \le\exp[C\rho\log(\rho+1)].
\tag{4.7}
\]

Therefore the expected total normalized crossing charge is at most

\[
\begin{aligned}
 \beta_0
 &\le
 C\sum_{\rho=\rho_*}^{L}
 \exp[C\rho\log(\rho+1)]\alpha^{\rho/4}\\
 &\le\exp[-c_0L\log m]
 \le\exp[-c_1(\log m)^3].
\end{aligned}
\tag{4.8}
\]

Markov at level \(\beta_0^{1/2}\), followed by renaming
\(\beta=\beta_0^{1/2}\), proves (0.7).  The root-incidence mark uses

\[
                         \mathfrak I_R(t)=E_{\rm ref}(t)
\tag{4.9}
\]

and gives the identical bound.

On every retained center, adjacent child envelopes have ratio at most

\[
                         \alpha^{3/4}.
\tag{4.10}
\]

Indeed the stopping envelope at excess \(\rho+1\) divided by the one
at excess \(\rho\) is
\(\alpha^{3(\rho+1)/4}/\alpha^{3\rho/4}\).
Its total-time cost is

\[
 TL^{O(1)}\alpha^{3/4}=m^{-17/40+o(1)}=o(1).
\tag{4.11}
\]

Thus the loose local envelopes and the aggregate maximal ledger are
simultaneously compatible.

## 5. Conversion to \(o(N_H)\) roots

The normalized charge in (0.7) occurs at varying degree scales.
Partition time into reference slabs on which \(D_{\rm ref}(t)\) changes
by at most a factor two.  Since

\[
                         \log D_0=O(m\log m),
\tag{5.1}
\]

one may take

\[
                         C_{\rm sl}=O(m\log m).
\tag{5.2}
\]

This subdivision is used only for the leave ledger and requests no new
moment.

Let \(Q_j^O\) be the owners crossing in slab \(j\), and let \(q_j\) be
their contribution to the normalized sum in (0.7).  On the
degree-stopped core,

\[
 d_t(X)\ge cD_j,\qquad
 E_{\rm ref}(t)=(1+o(1))N_tD_j
\tag{5.3}
\]

throughout the slab.  Hence

\[
 |Q_j^O|
 \le {2q_jkE_j\over cD_j}
 \le Cq_jkN_t.
\tag{5.4}
\]

Summing \(q_j\le\sum_jq_j\le\beta\) and using
\(N_t\le N_H\) gives

\[
                         |Q^O|
 \le C\beta kN_H=o(N_H).
\tag{5.5}
\]

The polynomial number of slabs does not enter (5.5), because their
normalized charges sum to \(\beta\).  Directly stopped roots satisfy

\[
                         |Q^R|\le C\beta N_H=o(N_H).
\tag{5.6}
\]

Analytical quarantine removes no catalogue edge.  At the terminal
matching, if selected edges containing a stopped owner are not trusted,
discard each such selected edge once and assign it to one stopped owner
which it contains.  Also discard selected edges at stopped roots.  The
number of lost matching roots is at most

\[
                         |Q^O|+|Q^R|=o(N_H).
\tag{5.7}
\]

The resulting additional owner leave is

\[
 k(|Q^O|+|Q^R|)
 =O(\beta k^2N_H)=o(W),
\tag{5.8}
\]

because \(W=(1+o(1))kN_H\) and \(\beta k=o(1)\).

No incident star was suppressed during the trajectory, so this
terminal operation has no cascade.

## 6. Optional one-generation literal cleaning

If a consumer requires a literal current subcatalogue, suppress the
edges incident with the primary stopped-owner set once.  In slab \(j\),
the number removed satisfies

\[
                         F_j\le 2q_jkE_j.
\tag{6.1}
\]

Let

\[
                         \eta=\sqrt{\beta k}.
\tag{6.2}
\]

The roots losing more than \(\eta D_j\) in slab \(j\) number at most

\[
 {F_j\over\eta D_j}
 \le {Cq_jk\over\eta}N_t.
\tag{6.3}
\]

After summing the normalized charges \(q_j\),

\[
                         |Q_{\rm loss}^R|
 \le {C\beta k\over\eta}N_H
 =C\eta N_H=o(N_H).
\tag{6.4}
\]

The removed edges cause total owner-degree loss \(kF_j\).  Owners losing
more than \(\eta D_j\) therefore have total number at most

\[
                         {Cq_jk^2\over\eta}N_t.
\tag{6.5}
\]

Over all slabs this is at most \(C\eta kN_H=o(W)\).
Add these secondary owners only to the analytical exception list.
Do not suppress their remaining stars.

Every unexceptional root and owner loses at most an \(\eta\)-fraction
of its current degree.  Primary stars are removed once, secondary
exceptions are not expanded, and no further removal wave is generated.
This is the claimed noncascading literal cleaning.

## 7. Interface with the graded core

For \(\rho<\rho_*\), the proved choice

\[
 q(\rho)=\min\left\{J,
          \left\lfloor{L\over2\rho+1}\right\rfloor\right\}
\tag{7.1}
\]

has \(q(\rho)\ge2\), and every replicated moment remains below excess
\(L\).  For \(\rho\ge\rho_*\), Sections 1--4 give the first-moment
envelope and maximal quarantine.

At the entrance to the top strip,

\[
 \alpha^{3\rho/4}
 \le\alpha^{3L/16+O(1)}
 =\exp[-\Omega((\log m)^3)].
\tag{7.2}
\]

This is below the stochastic-core failure budget, the cumulative degree
tolerance, and both leave ledgers.  Thus the graded stochastic core and
the first-moment top strip meet without a missing outer flux.

## 8. Exact status

The proof uses only the stated current inputs.  In particular:

1. prefix terminal death is retained and exactly paired with the
   prefix-survival reference;
2. the surviving cross-prefix edge and coin terms are paid as one
   absolute excess-\((\rho+1)\) child;
3. \(T\alpha=o(1)\) closes that child additively;
4. marked incidences, rather than random external weights, give the
   maximal quarantine; and
5. division by current degree, rather than the false implication
   \(o(E/m)=o(N_H)\), gives the root leave.

The one-row stop in input 3 is bootstrap-compatible.  Stop such a
variable at its first envelope crossing; below the crossing, Section 2
is deterministic.  Its proved graded moments charge the crossing,
while the additive top-strip estimate prevents those moment diagrams
from escaping through the ceiling.  The marked-incidence quarantine
then absorbs the stopped one-row centers in the same \(\beta\) ledger.
Thus input 3 is used as a stopped member of the proved hierarchy, not
as an assertion that no one-row exception occurs.

Hence aggregate stopped compensation/edge-column mass remains
\(O(\alpha^\rho)\), and the top strip can be quarantined at
\(o(N_H)\) root cost without cascade.
