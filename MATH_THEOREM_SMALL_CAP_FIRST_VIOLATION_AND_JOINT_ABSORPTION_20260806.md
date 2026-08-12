# Small-cap first violation and joint J/GDIR/HDIR absorption

**Date:** 2026-08-06  
**Method:** stopped drift, small-constant absorption, and optional stopping;
no computation or search  
**Status:** proof-safe closure of the scalar PCAP bootstrap once the
already-stated joint signed decomposition is available.  The cap need only
hold on a constant-probability terminal event; the annealed
quarantine--Haxell composition can retain that event at constant cost.

## 1. Abstract simultaneous absorption

Let \(\tau\) be the first violation of PCAP, the good-load bounds, the
total-rate lower bound, the owner-mixture bounds, or any individual-root
hypothesis used below, or the ordinary terminal density if none fails.
In particular, stop at the first violation of

\[
 \mathcal P_i\le\varepsilon_P{N_T(i)\over d^3}
\tag{PCAP}
\]

within that common stopped interval.  Let

\[
 \begin{aligned}
 \mathsf D&=\mathbb E\sum_{i<\tau}\mathcal J_i,\\
 \mathsf H&=\text{the stopped GDIR + HDIR + root-carre budget},\\
 \mathsf I&=\text{the shared-insertion Bellman budget},\\
 \mathsf A&=\mathcal P_0+\text{ROc + FE3 + owner/slot/endpoint budgets}.
 \end{aligned}
\tag{1.1}
\]

All four quantities are nonnegative.  The exact FP9/root-contraction
decomposition and the local-order/endpoint rows have the following
algebraic form, with absolute constants:

\[
 \boxed{\mathsf D+\mathsf H\le C_0\mathsf A+C_1\mathsf I.}
\tag{1.2}
\]

The future-service affine theorem and its adapted-mark expansion give,
under PCAP,

\[
 \boxed{
 \mathsf I\le
 C_2\varepsilon_P
  (\mathsf A+\mathsf D+\mathsf H).}
\tag{1.3}
\]

Here the \(\mathsf H\) term is exactly the moving-mark
GDIR/HDIR/root-carre term, while \(\mathsf D\) is the unweighted
future-hazard defect.  No weighted copy of either quantity remains.

### Theorem 1.1 (small-constant closure)

If

\[
 C_1C_2\varepsilon_P\le{1\over2},
\tag{1.4}
\]

then

\[
 \boxed{
 \mathsf D+\mathsf H+\mathsf I\le C\mathsf A}
\tag{1.5}
\]

for an absolute \(C\).

#### Proof

Insert (1.3) into (1.2):

\[
 \mathsf D+\mathsf H
 \le (C_0+C_1C_2\varepsilon_P)\mathsf A
   +C_1C_2\varepsilon_P(\mathsf D+\mathsf H).
\]

Move the last term to the left and use (1.4).  This bounds
\(\mathsf D+\mathsf H\) by \(C\mathsf A\); substitute back in (1.3) to
bound \(\mathsf I\).  \(\square\)

Thus the hazard defect is not assumed previously controlled.  It and the
insertion row close simultaneously.

## 2. First-violation control of PCAP

The exact future-potential drift is

\[
 \mathbb E_i(\mathcal P_{i+1}-\mathcal P_i)
 \le-(1-\rho_i^2)\mathcal P_i+\mathcal J_i.
\tag{2.1}
\]

Discarding the negative service term, stopping at \(\tau\), and applying
Theorem 1.1 gives

\[
 \boxed{
 \mathbb E\mathcal P_\tau
 \le\mathcal P_0+\mathsf D
 \le C\mathsf A.}
\tag{2.2}
\]

The authenticated initial/static scale is

\[
 \mathsf A\le C_A{M\over d^4}.
\tag{2.3}
\]

If PCAP fails before terminal density \(p_*=c/d\), then

\[
 \mathcal P_\tau>
 \varepsilon_P{N_T(\tau)\over d^3}
 \ge c_T\varepsilon_Pc\,{M\over d^4},
\tag{2.4}
\]

where \(c_T>0\) is the fixed lower/owner layer comparison constant.
Therefore

\[
 \boxed{
 \Pr(\text{PCAP fails})
 \le {CC_A\over c_T\varepsilon_Pc}.}
\tag{2.5}
\]

Choose \(\varepsilon_P\) first to satisfy (1.4), and then choose the fixed
separator constant \(c\) so large that the right side of (2.5) is at most,
say, \(1/4\).  The initial cap also has margin, since at \(p_*=c/d\) its
minimum threshold is

\[
 c_T\varepsilon_Pc\,{M\over d^4}
\]

while \(\mathcal P_0\le C_AM/d^4\).

Hence PCAP itself fails before the common stopping time with probability
at most \(1/4\).  Reaching terminal density additionally requires the
separate good-load/rate/root bootstrap events in the definition of
\(\tau\).  Their failure probabilities must be combined before claiming
a terminal success probability.  On PCAP failure, kill the analytical
branch; on joint survival, all estimates above hold through the full run.

## 3. Interface with the annealed construction

The joint cap/load/rate/root-survival event is terminal.  If it has
absolute positive probability under the same raw packing law, and the
downstream completion theorem is pointwise valid on every output in that
event, the annealed quarantine--Haxell composition permits imposing it at
the reciprocal constant cost.  The PCAP estimate alone establishes only
its own part of that joint event.

If a later argument insists on retaining the unconditioned raw law, (2.5)
alone does not give the sharper \(O(1/d)\) cap-failure probability needed
to delete every selected block on failure.  The proof-safe route supplied
here is the killed terminal-event route, not an expected full-erasure
claim.

## 4. Exact remaining premise

Theorem 1.1 is algebra, not a new assertion of (1.2).  To invoke it, the
joint local proof must verify (1.2) with \(\mathsf I\) containing all
shared-insertion pieces and \(\mathsf H\) containing the exact adapted mark
innovation terms.  The affine and adapted-mark notes establish (1.3).

Accordingly:

* PCAP is no longer an independent probabilistic obstruction;
* the mutual J/IPH feedback is no longer circular;
* the sole remaining analytic content is the coefficient-faithful joint
  signed decomposition (1.2), including the occurrence-preserving
  identification of the adapted innovation with the type-resolved
  GDIR/HDIR/root-carre families.
