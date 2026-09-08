# Compensated consecutive spine: exact centering, transfer spectrum, and the surviving variance gate

Date: 2026-07-27

Scope: the post-\(H\) consecutive profile from
`MATH_NOGO_ALL_ORDER_PROFILE_ENERGY_CONSECUTIVE_SPINE_20260727.md`,
inside the genuine compensated ordinary-frame process.

## 0. Verdict

The order-one kernel in the scalar no-go is not the kernel seen by the
compensated generator.  For every active protected prefix \(S\),

\[
 \sum_{a}d_t(S\cup\{a\})=(r-|S|)d_t(S).                 \tag{0.1}
\]

Consequently the full one-child mean is a deterministic function of the
parent, pathwise.  After the survival normalization used by the profile
stops it is canceled by the marginal drift/compensation term.  The
quantity denoted \(c_k^{\rm spine}\simeq1\) in the scalar note is an
*unnormalized* child sum.  The child probability in the compensated
calculation has an additional divisor \(r-k\).

For \(H\le k<m\), put

\[
                         R=r-k,\qquad g=m-k.              \tag{0.2}
\]

The complete consecutive-spine mass in the normalized child law is

\[
             A_k={R-1\over R^2}.                         \tag{0.3}
\]

Thus the exact two-orientation transfer matrix is

\[
             \boxed{\mathsf T_k=A_k I_2},                \tag{0.4}
\]

and

\[
             \boxed{\|\mathsf T_k\|_{2\to2}
                    ={R-1\over R^2}\le {1\over R}.}      \tag{0.5}
\]

In particular, throughout the entire post-\(H\) spine,

\[
             \|\mathsf T_k\|\le {1\over H+1}=o(1),      \tag{0.6}
\]

not \(\Theta(1)\).  The positive-scalar weight obstruction (0.8)--(0.11)
of the baseline note therefore does **not** apply to the exactly
compensated process.

Compensation does not make the process deterministic.  After centering,
the spine-versus-complement choice has a nonzero covariance eigenvalue

\[
                       2A_k(1-A_k)=\Theta(1/R).           \tag{0.7}
\]

This is genuine predictable variation: independent compensation clocks
cannot cancel a carré-du-champ term.  But it is an order-
\(1/R\) variance mode, not an order-one first-moment transport.  In
polynomial degree it is second order.  In *physical support order* it can
be either a repeated-child \(+1\) diagonal or a distinct-child \(+2\)
common-event term.

There remains one precise charging issue.  With the same threshold at
orders \(k\) and \(k+1\), a child crossing while the parent is safe forces
only an \(A_0(1-u)\) centered deviation.  This degenerates near time zero.
A fixed threshold separation repairs the deviation, but converting the
conditional variance back to the literal child incidence costs a factor
\(R\).  Thus the next theorem is a staggered-threshold or incidence-weighted
variance estimate; it is not the scalar all-order recurrence refuted here.

## 1. The exact parent-child identity

Let \({\cal H}_t={\cal H}_0[A_t]\) be any current vertex-induced residual
of an \(r\)-uniform hypergraph.  For an active set \(S\), every current
edge through \(S\) contains exactly \(r-|S|\) further resources.  Double
counting pairs \((e,a)\), with \(e\supseteq S\) and
\(a\in e\setminus S\), gives (0.1).  The same identity holds at time
zero.

Put

\[
 q_k(S)={d_0(S)\over D_0},\qquad
 p_{S,a}={q_{k+1}(S\cup\{a\})
                \over (r-k)q_k(S)}.                     \tag{1.1}
\]

Then

\[
                         p_{S,a}\ge0,qquad
                         \sum_a p_{S,a}=1.               \tag{1.2}
\]

For the survival-normalized profile

\[
 X_S(t)={d_t(S)\over d_0(S)u^{r-k}},                     \tag{1.3}
\]

declare \(X_{S\cup\{a\}}=0\) when the child is inactive.  Another use of
(0.1) gives the pathwise identity

\[
 \boxed{
       \sum_a p_{S,a}X_{S\cup\{a\}}=uX_S.}              \tag{1.4}
\]

Hence, with

\[
       Z_{S,a}=X_{S\cup\{a\}}-uX_S,                     \tag{1.5}
\]

one has

\[
                         \sum_a p_{S,a}Z_{S,a}=0.        \tag{1.6}
\]

Equation (1.6) is the exact compensation/coboundary identity.  It holds
for each prefix \(S\) separately.  Compensation therefore removes the
whole parentwise one-child mean, not merely the global constant vector
obtained after summing the two orientations.

The natural residual energy is the conditional variance

\[
 V_S=\sum_a p_{S,a}Z_{S,a}^2
     =\sum_a p_{S,a}X_{S\cup\{a\}}^2-u^2X_S^2.           \tag{1.7}
\]

Thus a positive term left after the exact one-child cancellation is
quadratic.  It may repeat the same child (one new physical resource), or
expose two distinct children.

## 2. Exact normalization of the post-\(H\) spine

Use the exact masses from the baseline note:

\[
 \Gamma_k={2(r-k)(m-k)!(m-H)!\over r(m!)^2},
                  \qquad H\le k\le m.                   \tag{2.1}
\]

For any one of the \(g=m-k\) prescribed consecutive continuations,

\[
 {\Gamma_{k+1}\over\Gamma_k}
       ={R-1\over R}{1\over g}.                          \tag{2.2}
\]

The scalar note sums (2.2) over the \(g\) continuations and obtains

\[
                         {R-1\over R}.                   \tag{2.3}
\]

But (1.1), rather than the raw degree ratio, is the child probability.
Each prescribed continuation therefore has weight

\[
 p_k^{\rm one}
 ={1\over R}{\Gamma_{k+1}\over\Gamma_k}
 ={R-1\over R^2g}.                                      \tag{2.4}
\]

Their total weight is exactly

\[
 g p_k^{\rm one}={R-1\over R^2}=A_k,                    \tag{2.5}
\]

which proves (0.3).

There are two monotone orientations in (2.1).  A consecutive
continuation preserves its orientation: reversing from the prefix shore
to the suffix shore breaks the prescribed nested order.  Consequently,
after aggregating the \(g\) coordinate labels but retaining the two
orientations, the restricted transfer is (0.4).  Its spectrum is

\[
                         \operatorname{spec}(\mathsf T_k)
                         =\{A_k,A_k\},                   \tag{2.6}
\]

which proves (0.5).

The raw scalar kernel and the compensated kernel are related by

\[
 c_k^{\rm spine}=R A_k.                                 \tag{2.7}
\]

The missing factor \(R\) is exactly the number of remaining slots in
each edge, i.e. the averaging factor in (1.1).  This is why iterating
\(c_k^{\rm spine}\) as a positive compensated-generator coefficient
creates a spurious order-one post-\(H\) mode.

For comparison, a path which remains in the consecutive spine at every
post-\(H\) order has weight

\[
 \prod_{k=H}^{m-1}A_k
 =\prod_{R=r-m+1}^{r-H}{R-1\over R^2},                  \tag{2.8}
\]

whose logarithm is \(-\Theta(m\log m)\).  There is no near-unit
one-child spine after the exact normalization.

## 3. The smallest variance transfer matrix

For one fixed orientation, collapse all \(g\) consecutive continuations
to the state \(C\), and all other children to the state \(G\).  Their
probabilities are

\[
                         \Pr(C)=A_k,qquad
                         \Pr(G)=1-A_k.                   \tag{3.1}
\]

The centered two-state covariance matrix is

\[
 \boxed{
 \mathsf C_k
 =A_k(1-A_k)
   \begin{pmatrix}1&-1\\-1&1\end{pmatrix}.}             \tag{3.2}
\]

Therefore

\[
 \operatorname{spec}(\mathsf C_k)
 =\{0,\,2A_k(1-A_k)\},
 \qquad
 \|\mathsf C_k\|=2A_k(1-A_k)\le {2\over R}.            \tag{3.3}
\]

This is the smallest shore/gap matrix: the two orientations give two
identical copies, while the \(C/G\) coordinate records whether the next
resource stays in the consecutive shore or enters the complementary gap
geometry.

Equivalently, on the literal four states
\((C_+,G_+,C_-,G_-)\), the two-shore/gap covariance is

\[
 \mathsf C_k^{\pm}
 =I_2\otimes\mathsf C_k,
 \qquad
 \operatorname{spec}(\mathsf C_k^{\pm})
 =\{0,0,2A_k(1-A_k),2A_k(1-A_k)\}.                      \tag{3.3a}
\]

Thus neither the symmetric nor antisymmetric shore sector has a hidden
unit eigenvalue after parentwise centering.

If the \(g\) individual consecutive labels are retained, their
conditional law inside \(C\) is uniform.  The \((g-1)\)-dimensional
label-contrast covariance has eigenvalue

\[
 {A_k\over g}={R-1\over R^2g}.                           \tag{3.4}
\]

Thus no refinement of the consecutive labels restores the unit scalar
mode.  The only unexamined covariance lies wholly inside the complementary
child geometry; it is not the consecutive spine of the no-go note.

Equation (3.3) also answers the deterministic-versus-random question.
The eigenvalue zero is the deterministic mean killed by compensation.
The second eigenvalue is strictly positive for every \(H\le k<m\), so
there is genuine variance.  For a jump process the predictable bracket
is a sum of squared jumps,

\[
 {d\langle M\rangle_t\over dt}
 =\sum_e\lambda_e(t)(\Delta_e Z)^2
  +\sum_x\chi_x(t)(\Delta_x Z)^2\ge0.                    \tag{3.5}
\]

The compensation clocks are independent positive-rate events.  They can
cancel a predictable first-moment drift, but cannot subtract (3.5).
Accordingly the nonzero eigenvalue in (3.3) is a real variance mode.
Its scale is \(1/R\).  Its generator expansion begins with the
repeated-child diagonal and then the distinct two-child/common-event
terms.

### 3.1 Exact generator cancellation

The preceding distinction can be made directly at generator level.  Let
\(\mathscr G=\partial_t+\mathcal L_t\), and for a pure-jump observable
\(Y\) write

\[
 \boldsymbol\Gamma_t(Y)
 =\mathcal L_t(Y^2)-2Y\mathcal L_tY
 =\sum_h\lambda_h(t)(\Delta_hY)^2.                       \tag{3.6}
\]

The weights \(p_{S,a}\) are static.  Since \(\dot u=-u/r\),

\[
 \mathscr G Z_{S,a}
 =\mathscr G X_{S\cup\{a\}}-u\mathscr G X_S
   +{u\over r}X_S.                                      \tag{3.7}
\]

Applying the jump square identity and then (1.6) gives

\[
\begin{aligned}
 \mathscr G V_S
 &=2\sum_a p_{S,a}Z_{S,a}\mathscr GZ_{S,a}
   +\sum_a p_{S,a}\boldsymbol\Gamma_t(Z_{S,a})\\
 &=2\sum_a p_{S,a}Z_{S,a}
       \mathscr G X_{S\cup\{a\}}
   +\sum_a p_{S,a}\boldsymbol\Gamma_t(Z_{S,a}).          \tag{3.8}
\end{aligned}
\]

Both the parent drift \(-u\mathscr GX_S\) and the derivative of the
survival normalization cancel **exactly**.  Equation (3.8) is the
generator answer to the scalar no-go: there is no positive uncentered
\(+1\) parent-to-child term left.  The first summand contains only
centered variation of the child drifts.  The second summand is a genuine
nonnegative bracket.  If one compensation coin at \(a\), or one selected
edge meeting the displayed link only through \(a\), changes a link by
\(B_a=d_t(S\cup\{a\})\), its contribution contains

\[
                         \lambda_a B_a^2.                \tag{3.9}
\]

This repeats \(a\) twice algebraically but has only one new physical
resource.  It is therefore a physical \(+1\) diagonal, not a \(+2\)
profile.  Terms using two different resources are genuine \(+2\)
column energies.  Bounding (3.8) consequently requires an
\(L^2\)-weighted \(+1\) diagonal estimate together with the distinct
\(+2\) estimate; it does not require the raw \(L^1\) \(+1\) recurrence
of the scalar no-go.

No claim is made here that (3.8) is already summable.  In particular,
the complementary child sector can have large column breadth.  What is
proved is that the post-\(H\) consecutive spine cannot furnish the
order-one \(+1\) coefficient asserted in the baseline obstruction.

## 4. What variance does and does not charge

Suppose the order-\(k+1\) threshold is \(A_+\), the order-\(k\) parent
threshold is \(A_-\), and child \(a\) is the first crossing while its
parent is safe.  From (1.5),

\[
 Z_{S,a}\ge A_+-uA_-.                                  \tag{4.1}
\]

Since

\[
 q_{k+1}(S\cup\{a\})=R p_{S,a}q_k(S),                  \tag{4.2}
\]

the contribution of this child to the incidence-weighted variance is

\[
 q_k(S)V_S
 \ge {q_{k+1}(S\cup\{a\})\over R}
       (A_+-uA_-)^2.                                    \tag{4.3}
\]

With equal thresholds \(A_+=A_-=A_0\), (4.3) contains only
\(A_0^2(1-u)^2/R\), which degenerates as \(u\uparrow1\).  Hence the
variance observable alone does not give a uniform incidence charge for
the unmodified equal-threshold tower.

If, instead, \(A_-\le(1-\delta)A_+\) for fixed \(\delta>0\), then

\[
 q_k(S)V_S
 \ge {\delta^2A_+^2\over R}
       q_{k+1}(S\cup\{a\}).                              \tag{4.4}
\]

Thus a staggered threshold gives a valid charge, but it loses the factor
\(R\).  Equivalently, the literal child incidence is charged by the
rescaled energy \(R q_kV_S\).  Proving that this rescaled energy has
summable generator and initial mass is the exact successor problem.

## 5. Corrected boundary

The following points are proved.

1. The exact one-child mean is a parentwise coboundary, (1.4)--(1.6),
   and is canceled by the compensated survival normalization.
2. The post-\(H\) consecutive spine occupies only \(A_k=(R-1)/R^2\)
   of the normalized child law.
3. Its two-orientation transfer has norm \(A_k\le1/R\), not order one.
4. The associated centered variance is nonzero but has norm at most
   \(2/R\).  Its first physical boundary is the repeated-child \(+1\)
   diagonal; distinct-child terms begin at \(+2\).
5. Equal profile thresholds are not automatically charged by this
   variance near \(u=1\); staggered thresholds work with an exact factor
   \(R\) loss.

Therefore the consecutive-spine note is a valid obstruction to an
*uncentered raw positive-child sum*, but not to the genuine compensated
profile process.  The next defensible gate is

\[
 \boxed{
 \text{a generator/initialization bound for }
 \sum_S (r-|S|)q_k(S)V_S,
 \text{ including its repeated-child diagonal, or an equivalent
 staggered-threshold tower}.}                            \tag{5.1}
\]

That gate may still fail because of complementary child geometries or
two-child column breadth.  The consecutive spine itself supplies no
post-\(H\) unit eigenmode after exact compensation.
