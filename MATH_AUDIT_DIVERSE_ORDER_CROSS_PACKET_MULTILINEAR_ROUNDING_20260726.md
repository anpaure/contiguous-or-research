# Audit of diverse-order cross-packet multilinear rounding

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Verdict

The exact load, hole, repeat, product-uncovered, and pair-covariance
formulas in
`MATH_REDUCTION_DIVERSE_ORDER_CROSS_PACKET_MULTILINEAR_ROUNDING_20260726.md`
are correct for the atomic packet model.  The conditional-expectation
rounding theorem is also correct, simultaneously for all depths and both
signs, because one applies it to their single nonnegative aggregate cost.
Theorem 5.1 correctly converts covariance excess (o(W)) above the
balanced integer baseline into (o(W)) total holes.

The phrase “zero integrality gap” needs a precise reading.  It is true
because the multilinear extension is **defined** to be the expectation of
the integral objective under a product distribution.  It is therefore an
average of integral costs, and its global minimum over the product of
simplices is attained at an integral vertex.  This is not a convex
relaxation, an LP theorem, or an algorithmic rounding gain.  The functions

\[
 \widetilde{\cal H}(x)
   =\sum_{c,T}\prod_P(1-p_{P,c}(T))
\]

and

\[
 \widetilde{\cal C}(x)
   =\sum_c\sum_{P<Q}\sum_{\omega,\eta}
      x_{P,\omega}x_{Q,\eta}
      |I_{P,c}^{\omega}\cap I_{Q,c}^{\eta}|
\]

are multi-affine but generally nonconvex jointly.  Finding a fractional
point with low multilinear cost is, without additional structure,
logically as hard as finding the integral point: delta distributions are
already included, and conditional expectation gives the converse.

Accordingly, the exact remaining conditions are:

1. **Hole form, necessary and sufficient at packet level:** construct one
   common product distribution (x) such that

   \[
        \sum_{c,T}\prod_P(1-p_{P,c}(T))=o(W).
   \]

   This is equivalent to the existence of an integral packet-option
   selection with (o(W)) holes.
2. **Covariance form, stronger sufficient condition:** construct one
   common product distribution satisfying

   \[
    \sum_c\left(\widetilde{\cal C}_c(x)
                    -{\cal C}_{c,\min}\right)=o(W).
   \]

   This is equivalent, by the same averaging argument, to the existence
   of an integral choice with covariance excess (o(W)), and it implies
   the desired hole bound.  It is not equivalent to small holes because
   a sublinear repeat mass may be highly concentrated and have large
   factorial energy.

Thus the note correctly removes any **separate objective-level rounding
obstruction**, but it does not turn the surviving grouped theorem into a
linear or convex fractional problem.  The substantive open theorem is the
construction or structural analysis of a low-cost product distribution.

Three scope qualifications should be recorded.

* If several packets are put in one coupled choice group, all no-diagonal
  formulas remain literal only when their image sets are pairwise disjoint
  within every group.  This is true for sibling parallel fibres of one
  parent (Q_S), by frozen-spectator separation, but not for an arbitrary
  grouping.
* The near-polarization conclusion following (4.8) is immediate under a
  uniform targetwise bound
  \(\sum_Pp_{P,c}(T)\le\Lambda=O(1)\).  A bounded **average** load at each
  depth alone does not give a global “outside (o(W)) target-depth pairs”
  statement when the number of depths grows.
* The source note inherits the interface qualification from the diverse
  packet theorem: component count makes an external (O(H))-per-component
  interface cost negligible, but that interface operation is not proved
  by the packet theorem itself.

## 1. Atomic packet load ledger

Fix a signed depth (c=(\sigma,q)).  Packet injectivity gives a set

\[
                         I_{P,c}^{\omega}
\]

of size (s=2^R), so

\[
 v_{P,\omega}^{c}(T)=\mathbf1_{\{T\in I_{P,c}^{\omega}\}}
 \in\{0,1\},
 \qquad
 \sum_Tv_{P,\omega}^{c}(T)=s.
\]

Choosing one option per packet gives

\[
                         L_c(T)=\sum_Pv_{P,\omega_P}^{c}(T).
\]

Since there are (G/s) packets,

\[
                         \sum_TL_c(T)=G.
\]

Let (U_c=\{T:L_c(T)>0\}).  Then

\[
 \begin{aligned}
 {\cal E}_c
   &=\sum_T(L_c(T)-1)_+
     =\sum_{T\in U_c}(L_c(T)-1)
     =G-|U_c|,\\
 {\cal H}_c
   &=N_q-|U_c|.
 \end{aligned}
\]

Subtracting proves

\[
 \boxed{{\cal H}_c=N_q-G+{\cal E}_c.}
\]

There is no missing diagonal term because one packet contributes at most
one occurrence to a target.  This is exactly the cross-packet identity
audited independently in
`MATH_AUDIT_DIVERSE_ORDER_COMPILER_PACKET_FACTOR_20260726.md`.

## 2. Multi-affinity and conditional expectation

For arbitrary packet distributions (x_P\in\Delta(\Omega_P)), one has

\[
 \widetilde J(x)
 =\sum_{(\omega_P)_P}
    J((\omega_P)_P)\prod_Px_{P,\omega_P}.            \tag{2.1}
\]

Holding all (x_Q), (Q\ne P), fixed, (2.1) is affine in (x_P).
Thus it is multi-affine.  This conclusion does not require (J) itself
to be additive, convex, or even nonnegative; finiteness is enough.
Nonnegativity matters later when a small aggregate is used to control all
its summands.

Equation (2.1) is an average of integral costs.  Hence at least one
configuration has cost no larger than the average.  The sequential proof
is equally exact: after some packets have been fixed, the current
conditional expectation is

\[
 \sum_{\omega\in\Omega_P}x_{P,\omega}
       \mathbb E[J\mid\omega_P=\omega,\text{ previous choices}],
\]

so one option is at most this average.  Fix it and continue.

If

\[
                         J=\sum_{c}J_c
\]

uses every depth and both signs, the same packet option remains fixed in
all summands.  There is no depth-by-depth choice.  This verifies the
claimed simultaneous rounding.

Because delta distributions belong to every simplex,

\[
 \min_x\widetilde J(x)\le\min_{\boldsymbol\omega}J(\boldsymbol\omega).
\]

The averaging inequality gives the reverse inequality, proving equality.
This is the exact content of the “zero gap” assertion.

### What the equality does not say

Multi-affine does not mean convex.  For instance, the two-packet term
(a_{\omega\eta}x_{P,\omega}x_{Q,\eta}) has an indefinite joint Hessian
in general.  Conditional expectation derandomizes a **given** product
distribution; it does not construct a useful distribution, solve its
global minimization, or turn first-marginal feasibility into low cost.

Thus Theorem 3.1 is elementary and exact, but it is formally an averaging
identity rather than an independent structural rounding theorem.

## 3. Exact uncovered functional

For fixed (T,c), define

\[
 p_{P,c}(T)=\Pr_x[T\in I_{P,c}^{\omega_P}].
\]

The packet choices are independent, so the events indexed by different
packets are independent.  Therefore

\[
 \Pr_x[L_c(T)=0]=\prod_P(1-p_{P,c}(T)).
\]

Summing indicators gives exactly

\[
 \boxed{
 \widetilde{\cal H}(x)
   =\sum_{c,T}\prod_P(1-p_{P,c}(T)).}
\]

Applying Section 2 to (J=\sum_c{\cal H}_c) proves that
(\widetilde{\cal H}(x)=o(W)) is sufficient for one integral common
choice.  Conversely, any integral choice with (o(W)) holes gives such
an (x) by taking every (x_P) to be a delta mass.  Hence this condition
is exactly equivalent to the integral packet-selection target.

The mean inequalities

\[
                         \sum_Pp_{P,c}(T)\ge1
\]

do not imply it.  If (max_Pp_P=o(1)) and
(sum_Pp_P=\lambda+o(1)), then

\[
 \sum_P\log(1-p_P)
   =-\lambda+o(1),
\]

so the uncovered probability is (e^{-\lambda+o(1)}).

## 4. Audit of the polarization bound

Assume

\[
 0\le p_i\le1-\varepsilon,
 \qquad
 \sum_ip_i\le\Lambda.
\]

Since (p\mapsto\log(1-p)) is concave, the product is minimized at an
extreme allocation: as many (p_i)'s as possible equal
(1-\varepsilon), at most one is intermediate, and the rest vanish.
Writing (k=\lfloor\Lambda/(1-\varepsilon)\rfloor), this gives the
slightly sharper bound

\[
 \prod_i(1-p_i)\ge\varepsilon^{k+1}.
\]

The source's bound

\[
 \prod_i(1-p_i)
 \ge\varepsilon^{\lceil\Lambda/(1-\varepsilon)\rceil+1}
\]

is weaker but valid.

Consequently, under a uniform constant targetwise bound on
(sum_Pp_{P,c}(T)), every target with
(max_Pp_{P,c}(T)\le1-\varepsilon) pays a fixed positive uncovered
probability.  An aggregate uncovered cost (o(W)) then permits only
(o(W)) such target-depth pairs.

This last conclusion cannot be inferred from a bounded mean over targets
without an additional tail argument.  At one depth, total mass (G=O(W))
allows (O(W/K)) targets to have expected load at least (K).  Across a
growing (H)-window, one may have (O(W/H)) high-load diffuse targets at
each depth, hence (O(W)) such target-depth pairs in total, while their
uncovered probabilities are exponentially small in (H).  The exact
formulas remain correct; only the informal global polarization sentence
needs the targetwise bounded-load qualification.

## 5. Exact covariance formula

For integral packet choices,

\[
 \begin{aligned}
 {\cal C}_c(L)
   &=\sum_T\binom{\sum_Pv_P^c(T)}2\\
   &=\sum_T\sum_{P<Q}v_P^c(T)v_Q^c(T)\\
   &=\sum_{P<Q}|I_{P,c}^{\omega_P}\cap I_{Q,c}^{\omega_Q}|.
 \end{aligned}
\]

There is no (P=Q) term because (v_P^c(T)\in\{0,1\}).  Taking
expectations and using independence yields

\[
 \boxed{
 \widetilde{\cal C}_c(x)
 =\sum_{P<Q}\sum_{\omega,\eta}
    x_{P,\omega}x_{Q,\eta}
    |I_{P,c}^{\omega}\cap I_{Q,c}^{\eta}|.}
\]

This is a bilinear cross-packet energy, not a conventional covariance
with means subtracted; the terminology is harmless provided (5.3) is
kept as the definition.

## 6. Balanced collision baseline

Write

\[
                         G=aN_q+r_q,\qquad0\le r_q<N_q.
\]

Discrete convexity of (z\mapsto\binom z2) shows that the minimum over
all nonnegative integer load vectors of mass (G) has (r_q) entries
(a+1) and (N_q-r_q) entries (a).  Its energy is

\[
 \begin{aligned}
 {\cal C}_{c,\min}
  &=(N_q-r_q)\binom a2+r_q\binom{a+1}2\\
  &=N_q\binom a2+r_qa.
 \end{aligned}
\]

This is a universal lower bound.  It need not be attainable by the
packet-option catalogue, so calling it the “convex minimum” should not be
read as a feasible fractional packet optimum.

## 7. Covariance excess implies holes

Suppose first that (G\ge N_q), so (a\ge1).  Repeatedly move one unit
from a load (x) to a load (y) whenever (x\ge y+2).  The collision
energy decreases by

\[
 \binom x2+\binom y2-\binom{x-1}2-\binom{y+1}2
 =x-y-1\ge1.
\]

The procedure ends at a balanced vector and decreases energy by exactly
the initial excess over ({\cal C}_{c,\min}).  Since the balanced vector
has no zero coordinate, every initial hole must receive a unit during the
procedure.  Thus

\[
 {\cal H}_c
 \le {\cal C}_c-{\cal C}_{c,\min}.                 \tag{7.1}
\]

If (G<N_q), then (a=0) and the baseline is zero.  Put

\[
                         E=\sum_T(L_c(T)-1)_+.
\]

One has

\[
 {\cal H}_c=N_q-G+E,
 \qquad
 E\le\sum_T\binom{L_c(T)}2={\cal C}_c.
\]

Therefore in both cases

\[
 {\cal H}_c
 \le (N_q-G)_+
       +\bigl({\cal C}_c-{\cal C}_{c,\min}\bigr).  \tag{7.2}
\]

Apply conditional-expectation rounding to
(J=\sum_c{\cal C}_c).  Since every integral configuration is at least
the baseline at every (c), condition (5.5) yields an integral choice
whose total excess is (o(W)).  In the (G<N_q) case,

\[
                         N_q-G\le W-G=o(W/H).
\]

There are (O(H)) signed depths, so the sum of the forced terms is
(o(W)).  Summing (7.2) proves Theorem 5.1.

The proof is sound.

### Strength of the covariance condition

Small holes control the linear repeat mass
(sum_T(L(T)-1)_+), but not its concentration.  For example, a repeat
mass (r=o(W)) placed on one target has factorial cost
(\binom{r+1}{2}), which need not be (o(W)).  Hence covariance excess
(o(W)) is a genuinely stronger sufficient target than hole count
(o(W)), not merely a different notation for it.

## 8. Coupled choice groups

The multi-affine averaging theorem remains valid verbatim if one replaces
packets by arbitrary choice groups: sample one group option independently
per group and average the resulting total cost.

The simplified load and covariance formulas require more.  If a group
(B) contains several packets, its combined column is

\[
                         v_B^c(T)=\sum_{P\in B}v_P^c(T).
\]

It is (0/1), and contributes no diagonal collision term, only when the
constituent image sets are pairwise disjoint for that signed depth.

For the intended coupling of parallel sibling fibres cut from one parent
(Q_S), this disjointness is automatic: two fibres differ on a frozen
spectator axis, and every lower or upper target retains exactly one frozen
endpoint on that axis.  This was proved in
`MATH_AUDIT_DIVERSE_ORDER_COMPILER_PACKET_FACTOR_20260726.md`.

If a later construction couples packets from different parent cells, the
note must either retain the atomic packet variables or add the exact
within-group term

\[
 \sum_B\sum_{\{P,Q\}\subseteq B}
       |I_{P,c}\cap I_{Q,c}|
\]

to the collision ledger.  “Every assertion below” is not automatic for
an arbitrary grouping.

## 9. Exact surviving fractional condition

The first-marginal Gaussian profile flow supplies numbers resembling

\[
                         \sum_Pp_{P,c}(T).
\]

That is only the first moment.  Neither the product hole functional nor
the pair-intersection functional is determined by it.

The precise surviving alternatives are:

### Exact hole condition

Find packet distributions, common to all (c), with

\[
 \boxed{
 \sum_{c,T}\prod_P(1-p_{P,c}(T))=o(W).}
\]

This condition is necessary and sufficient for the packet-option problem
because integral delta distributions are permitted and conditional
expectation rounds any feasible product distribution.

### Strong covariance condition

Find packet distributions, common to all (c), with

\[
 \boxed{
 \sum_c\left[
   \sum_{P<Q}\sum_{\omega,\eta}
      x_{P,\omega}x_{Q,\eta}
      |I_{P,c}^{\omega}\cap I_{Q,c}^{\eta}|
   -\left(N_q\binom{a_q}{2}+r_qa_q\right)
 \right]=o(W),}
\]

where (G=a_qN_q+r_q).  This is sufficient and strictly stronger in
general.

Neither boxed condition is a linear feasibility theorem.  They are
nonconvex product-distribution design statements.  A future positive
result must exploit geometry of the packet option sets, polarization,
negative dependence, or an explicit covariance cancellation; ordinary
mean-profile Hall is not enough.

## 10. Interface inheritance

The source note says that seams and the interface toll have already been
closed.  What has been proved unconditionally is the component count

\[
                         G/(2R)=o(W/H).
\]

This makes any separately proved (O(H))-per-component interface cost
(o(W)).  The diverse packet theorem itself does not construct that
interface, and a naive deletion of every cycle-closure window costs
(Theta(H^2)) trace occurrences per component.  This qualification is
orthogonal to multilinear rounding but should remain visible in the
global theorem ledger.

## 11. Audited boundary

Proved:

* exact hole/repeat identity;
* exact product-uncovered functional;
* multi-affinity in every packet distribution;
* simultaneous whole-packet conditional-expectation rounding;
* exact pair-intersection covariance formula;
* exact balanced collision baseline; and
* covariance excess (o(W)\Rightarrow o(W)) total holes.

Qualified:

* “zero integrality gap” is a tautological global-minimum identity for a
  nonconvex multilinear extension, not an LP relaxation result;
* polarization outside (o(W)) target-depth pairs needs a uniform
  targetwise load bound or a quantitative tail estimate;
* coupled groups need within-group disjointness; and
* interface cost remains conditional on a separate transfer lemma.

Still open:

* construct a common all-depth product distribution satisfying the exact
  hole functional; or
* prove the stronger covariance baseline estimate.

That nonconvex distribution-design theorem, rather than integral
rounding, is the surviving cross-packet gate.
