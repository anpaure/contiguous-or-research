# Hilbert/two-shore profile energy: exact centering, the remaining diagonal, and the finite-cutoff audit

Date: 2026-07-27

Scope: the stopped profile hierarchy in the genuine compensated
vertex-induced ordinary-promotion-frame process.

## 0. Verdict

There are three different statements which must not be conflated.

1.  The observation

    \[
       \sum_{i=1}^{b}p_i^2\asymp b^{-1},\qquad b=m-k,
    \]

    for the exact post-collar continuation spine is correct.  It does
    **not** by itself repair the scalar hierarchy.  In the Hilbert norm
    which charges stopped child incidence, the averaging operator has
    norm one.  Equivalently, the apparent (b^{-1}) gain in an
    unweighted square is cancelled by the (b) child multiplicity in
    initialization and stop charging.

2.  There is nevertheless a genuinely different Hilbert object.  After
    conditioning on the live extension shore and subtracting its exact
    weighted mean, marginal deaths are favorable and the coherent child
    mode vanishes identically.  Its generator is an exact centered
    repeated-event diagonal.  If that diagonal has rate

    \[
                         O\!\left({L^C\over rb}\right),
                                                        \tag{CHD}
    \]

    in incidence aggregate, then the total PFS\(_3\)-stopped incidence is
    (O(L^C\log(1/z)/A_3^2)W=o(W)).  Thus a two-shore theorem of the
    correct strength really would close PFS\(_3\), with no propagation
    past the collar.

3.  CHD is not currently proved dynamically.  It is the centered form of
    the repeated selected-edge/compensation-coin diagonal.  The static
    theta calculation is consistent with it, and the exact consecutive
    spine has precisely the required (b^{-1}) square scale, but neither
    fact gives the hereditary stopped estimate.

There is also an important correction to the proposed compensated
``\(+2\)'' finite cutoff.  A degree-two common event is the second Taylor
term, but it raises the natural mixed-diagram excess by **one**, not two.
A shared compensation coin is one new physical resource.  Therefore
marginal compensation does not prove that the physical profile/excess
generator has no coherent (+1) term.  If one grades by Taylor incidence
multiplicity so that it is called (+2), the terminal initialization must
include repeated-edge and repeated-coin power diagrams; distinct-owner
higher codegrees alone do not pay it.

The net result is a viable, sharply isolated Hilbert target, not a completed
trajectory theorem and not a new impossibility theorem.

## 1. Why the raw square does not gain (1/b)

Let a parent have (b) children and let (p_i\ge0),
\(\sum_i p_i=1\), be their normalized static masses.  Along the exact
post-(H) spine,

\[
                         p_i=(1+o(1))/b.                 \tag{1.1}
\]

The scalar child operator is

\[
                         Ty=\sum_i p_i y_i.              \tag{1.2}
\]

As a map from unweighted \(\ell_2^b\) to \(\mathbb R\),

\[
                         \|T\|^2=\sum_i p_i^2\asymp b^{-1}.
                                                               \tag{1.3}
\]

But stopped child incidence is weighted by (p_i), so its natural
Hilbert space is (L^2(p)).  In that space

\[
 |Ty|^2\le\sum_i p_i y_i^2,
 \qquad \|T:L^2(p)\to\mathbb R\|=1.                    \tag{1.4}
\]

The constant vector realizes equality.  The same issue appears directly
in a square-generator estimate:

\[
 2x\sum_i p_i y_i
 \le \eta x^2+\eta^{-1}\sum_i p_i y_i^2.                \tag{1.5}
\]

There is no (b^{-1}) on the right.  Alternatively, using the unweighted
norm gives a (b^{-1}) transfer coefficient, but the constant initial
vector has squared norm (b), and a stopped (p)-mass is
(b^{-1}) times the unweighted stopped count.  The two factors cancel.

Consequently a raw squared-profile energy is subject to the same constant
child mode as the scalar energy.  A successful Hilbert argument must
remove that mode, not merely square the scalar recurrence.

## 2. Exact live-shore centering

Fix a live physical (k)-profile (S), put (b=r-k), and sum over all
physical extension resources (a\notin S) for which
(d_0(S\cup\{a\})>0).  Every row through (S) contains exactly (b)
such resources, hence at every live state

\[
 \boxed{
   \sum_a d_t(S\cup\{a\})=b\,d_t(S).}                  \tag{2.1}
\]

The same identity at time zero gives weights

\[
 p_a={d_0(S\cup\{a\})\over b,d_0(S)},
 \qquad \sum_a p_a=1.                                  \tag{2.2}
\]

Let \({\cal A}_t\) be the extension resources still alive and define

\[
\begin{aligned}
 P_S(t)&=\sum_{a\in{\cal A}_t}p_a,\\
 X_S(t)&={d_t(S)\over d_0(S)u_t^b},\\
 X_{S,a}(t)&={d_t(S\cup\{a\})
                 \over d_0(S\cup\{a\})u_t^{b-1}}.
\end{aligned}                                           \tag{2.3}
\]

Dead extension resources have zero child degree.  Dividing (2.1) by the
references in (2.3) yields the exact mean identity

\[
 \boxed{
   \sum_{a\in{\cal A}_t}p_aX_{S,a}(t)=u_tX_S(t).}       \tag{2.4}
\]

When (P_S(t)>0), put

\[
 \bar X_S(t)={u_tX_S(t)\over P_S(t)},\qquad
 V_S(t)=\sum_{a\in{\cal A}_t}p_a
          \bigl(X_{S,a}(t)-\bar X_S(t)\bigr)^2.         \tag{2.5}
\]

Thus (V_S(0)=0).  More importantly, deletion of an extension resource
cannot increase (V_S).  Indeed, for weights of total mass (P), deleting
one coordinate of weight (p) changes the weighted centered sum of
squares by

\[
 V_{\rm old}-V_{\rm new}
 ={pP\over P-p}(x-\bar x)^2\ge0.                         \tag{2.6}
\]

Iterating proves the same assertion for simultaneous deletion of any set
of extension coordinates.  This removes the Bernoulli shore-survival
noise which makes the unconditioned variance order one.

## 3. The exact centered generator

Consider an event (e), either a selected catalogue edge or a
compensation resource.  First delete from the extension shore every
coordinate physically contained in (e); this is favorable by (2.6).
On the remaining coordinate set (B_e\subseteq{\cal A}_t), let

\[
 h_{e,a}=
 {\#\{\hbox{rows in the }(S,a)\hbox{-link killed by }e\}
  \over d_0(S\cup\{a\})u_t^{b-1}}.                       \tag{3.1}
\]

Write (h_e^\circ=h_e-\bar h_e\mathbf1), with the mean taken using the
weights (p_a) on (B_e).  If
(Y_a=X_{S,a}-\bar X_S), the nonterminal jump identity is

\[
 \Delta_eV_S
 \le -2\langle Y,h_e^\circ\rangle_p
       +\|h_e^\circ\|_{L^2(p)}^2.                       \tag{3.2}
\]

There is no estimate in (3.2): it is the polarization identity after the
favorable coordinate deletion.  In particular a constant child decrement
has (h_e^\circ=0).  This is the exact cancellation missing from every
one-index scalar profile.

Let \(\lambda_e(t)\) denote the actual event rate
((\nu_t\) for selected edges and \(\chi_t(y)\) for a coin).  After adding
the deterministic derivatives of the references in (2.3), define the
centered predictable bias (B_S(t)) so that all homogeneous first-order
loss is removed.  Then

\[
 (\partial_t+{\cal L}_t)V_S
 \le 2\langle Y,B_S\rangle_p+Q_S,                         \tag{3.3}
\]

where the exact centered diagonal is

\[
 \boxed{
 Q_S(t)=\sum_e\lambda_e(t)
           \|h_e^\circ\|_{L^2(p;B_e)}^2.}                \tag{3.4}
\]

Formula (3.4) includes both same-selected-edge powers and
same-compensation-coin powers.  It is the Hilbert form of the diagonal
\(\mathsf D_2\) in the exact stopped generator.  Bounding only distinct
next resources does not bound (3.4).

### Lemma 3.1 (coordinatewise drift compensation)

For a child (T=S\cup\{a\}), stopped when (T) dies, put

\[
 \beta_T(t)=\nu_t
 {\sum_{F\in{\cal F}_T(t)}
   \bigl[J_t(V(F))-J_t(T)\bigr]\over d_t(T)},
                                                               \tag{3.5}
\]

with value zero for an empty link.  This is the exact deficit in the
nonterminal loss hazard
\(\Lambda_t(V(F))-\Lambda_t(T)\).  Terminal events meeting \(T\) remove
the coordinate and are favorable.  The compensated union identity gives

\[
             (\partial_t+{\cal L}_t)X_T=\beta_TX_T.       \tag{3.6}
\]

Before PPS, the edge-local pair census gives

\[
 0\le\beta_T(t)\le {L^CA_2\over rmu_t},\qquad
 \int_0^T\beta_T(t)dt\le {L^CA_2\over mz}=o(1).          \tag{3.7}
\]

Consequently

\[
 Z_T(t)=X_T(t)\exp\!\left[-\int_0^t\beta_T(s)ds\right]   \tag{3.8}
\]

has zero predictable first-order drift before terminal death.  Replace
(X_{S,a}) by (Z_{S,a}) in (2.5), and center at its current weighted
mean.  Coordinate deletion remains favorable, and

\[
                         (\partial_t+{\cal L}_t)V_S\le Q_S,
                                                               \tag{3.9}
\]

where the jump vectors in (Q_S) only acquire factors
(e^{-\int\beta_T}=1+o(1)).  Moreover

\[
 e^{-o(1)}X_{S,a}\le Z_{S,a}\le X_{S,a},\qquad
 {\sum_{a\in{\cal A}_t}p_aZ_{S,a}\over P_S}
 \le {u_tX_S\over P_S}.                                  \tag{3.10}
\]

Thus a child crossing still has centered displacement
((1-o(1))A_3-A_2/c_0\).  The bias in (3.3) is removable; the sole
Hilbert gate is the centered carre-du-champ (3.4).

## 4. A precise sufficient theorem for PFS\(_3\)

The following proposition records exactly what the Hilbert idea would buy.

### Lemma 4.0 (the active-shore mass stop is cheap)

For a pair parent (S), assume the already proved static one-frame child
bound

\[
 \sum_{a\in V(g)}q_3(S\cup\{a\})\le {L^C\over m}q_2(S)  \tag{4.0a}
\]

for every physical event edge (g), and the one-child bound

\[
 q_3(S\cup\{a\})\le {L^C\over m^2}q_2(S).               \tag{4.0b}
\]

Then, for (b=r-2\sim m),

\[
 \Pr\left(\inf_{u_t\ge z}{P_S(t)\over u_t}<c_0\right)
 \le \exp[-m^{1+o(1)}]                                   \tag{4.0c}
\]

for any fixed (c_0<1), uniformly at
(z=m^{-1/2}(\log m)^B).  The same bound holds for the upper crossing
(P_S/u>c_0^{-1}).  Hence (4.1) costs (o(W)) marked incidence.

#### Proof

Every active extension resource has exact marginal deletion rate (1/r)
in the compensated process.  Thus (P_S/u), stopped when (S) dies, is a
martingale.  A selected edge deletes extension-shore weight at most

\[
 w_g\le {1\over bq_2(S)}{L^C\over m}q_2(S)
       ={L^C\over bm},                                    \tag{4.0d}
\]

and a compensation coin deletes weight at most

\[
 p_a\le {L^C\over bm^2}.                                  \tag{4.0e}
\]

Before (P_S\le2u), reverse the event sum and use the exact marginal
loss rate:

\[
\begin{aligned}
 {d\langle P_S/u\rangle_t\over dt}
 &\le {\max\{\max_gw_g,\max_ap_a\}\over u^2}
       {P_S\over r}\\
 &\le {L^C\over rbmu_t}.
\end{aligned}                                             \tag{4.0f}
\]

Since (dt=-r,du/u), the integrated quadratic variation is at most

\[
 {L^C\over bm}\int_z^1{du\over u^2}
 \le {L^C\over bmz}=m^{-3/2+o(1)}.                       \tag{4.0g}
\]

The normalized jump envelope has the same order
(L^C/(bmz)=o(1)).  Two-sided Freedman at a fixed positive deviation
therefore proves (4.0c).  Marked-incidence weighting avoids any union over
ambient pairs.  \(\square\)

### Proposition 4.1 (centered-diagonal criterion)

Fix a marked pair profile (S), so (b=r-2\sim m).  Stop at the ordinary
degree and PPS boundaries, and also at

\[
 P_S(t)<c_0u_t                                                   \tag{4.1}
\]

for a fixed (c_0>0).  Suppose, before these stops, that

\[
 2\langle Y,B_S\rangle_p
 \le \epsilon_tV_S+{L^C\over rb},qquad
 Q_S(t)\le {L^C\over rb},                                  \tag{4.2}
\]

with \(\int_0^T\epsilon_tdt=o(1)\), in the required
owner-incidence aggregate.  Quarantine and remove a child coordinate at
its first PFS\(_3\) crossing.  If

\[
                         A_3\ge {4A_2\over c_0},           \tag{4.3}
\]

then

\[
 \boxed{
  \mathbb E\sum_{a\ \mathrm{crossing}}p_a
  \le {CL^C\log(1/z)\over bA_3^2}.}                       \tag{4.4}
\]

Consequently the time-zero triple-profile mass stopped above one pair is
at most

\[
 \boxed{
  CL^C{\log(1/z)\over A_3^2}\,q_2(S).}                   \tag{4.5}
\]

In particular a sufficiently large polylogarithmic (A_3) makes the
aggregate PFS\(_3\) incidence (o(W)).  Lemma 4.0 pays the auxiliary
stop (4.1).

#### Proof

Equations (3.3)--(4.2), Gronwall, and
(T/r=\log(1/z)) give a total expected centered-energy budget

\[
             {CL^C\log(1/z)\over b}.                     \tag{4.6}
\]

This budget includes the energy removed when a crossing coordinate is
quarantined, by (2.6).  At such a crossing, PPS, (4.1), and (2.4) give

\[
 \bar X_S\le A_2/c_0\le A_3/4.
\]

Hence the removed coordinate contributes at least
(p_a(A_3/2)^2) after harmless corridor constants.  Summing these drops
and using (4.6) proves (4.4).  Finally

\[
 q_3(S\cup\{a\})=bq_2(S)p_a,                              \tag{4.7}
\]

so multiplying (4.4) by (bq_2(S)) proves (4.5).  \(\square\)

The factor (b^{-1}) in (4.2) is exactly the factor needed: it cancels
the (b) in (4.7).  This is why centering, rather than a raw square, is
the meaningful Hilbert proposal.

## 5. Calibration on the exact consecutive spine

On the post-(H) consecutive spine there are (b=m-k) continuation
directions and their normalized weights are

\[
                         p_i=(1+o(1))/b.                   \tag{5.1}
\]

A coherent decrement is constant in (i), hence disappears from
(h^\circ).  A unit decrement supported on one continuation direction has

\[
                         \|h^\circ\|_{L^2(p)}^2=O(1/b).   \tag{5.2}
\]

After the physical event clock (1/r), (5.2) is exactly the scale in
(4.2).  Thus the consecutive spine which refutes every positive scalar
all-order norm is **not** an obstruction to the centered Hilbert norm.

This is only a calibration.  A live residual event may hit many child
links with unequal normalized decrements.  Proving (4.2) means controlling
the incidence-weighted centered version of

\[
 \nu_t\sum_g A_{S,a}(g)A_{S,a'}(g)
 \quad\hbox{and}\quad
 \sum_y\chi_t(y)P_{S,a}(y)P_{S,a'}(y),                    \tag{5.3}
\]

including the diagonal (a=a').  The time-zero theta kernel controls the
first nontrivial static instance of (5.3); it does not regenerate (5.3)
along the stopped trajectory.

### 5.1 Equivalent conditional-influence scale

For a surviving child \(T=S\cup\{a\}\), let

\[
 \rho_T(t)=\sup_e
 {\,\#\{\hbox{\(T\)-link rows killed nonterminally by \(e\)}\}\over
   d_t(T)},                                                \tag{5.4}
\]

where selected-edge and coin events are both included.  Since a
decrement \(K\) satisfies \(K^2\le\rho_Td_t(T)K\), and the total
nonterminal loss rate of one link row is at most one,

\[
 Q_S(t)\le (1+o(1))
       \sum_{a\in{\cal A}_t}p_a\,\rho_{S,a}(t)\,
       X_{S,a}(t)^2,                                      \tag{5.5}
\]

up to the harmless centering subtraction and reference factors.  Thus
CHD follows, for example, from the incidence-weighted conditional
influence bound

\[
 \sum_ap_a\rho_{S,a}X_{S,a}^2
 \le {L^C\over rb}.                                      \tag{5.6}
\]

At time zero the ordinary-frame \(m^{-2}\) pair scale is exactly
\((rb)^{-1}\).  In a concentrated child residual, however,
\(\rho_T\) can be order one.  Formula (5.6) makes precise why the static
theta theorem is the correct calibration but not a hereditary proof:
the missing assertion is that the actual vertex-induced trajectory does
not put appreciable \(p_aX_{S,a}^2\)-mass on high-influence child links.
This is a size-biased, centered statement, weaker than pointwise PFS4.

## 6. Audit of the compensated \(+2\) cutoff

The exact stopped power generator is

\[
 {\cal L}A_C^2=-2A_C\mathsf D_1(C)+\mathsf D_2(C)+\mathsf K_C,
 \qquad \mathsf K_C\le0,                                  \tag{6.1}
\]

where

\[
 \mathsf D_2(C)
 =\nu_t\sum_gA_C(g)^2+\sum_y\chi_t(y)P_C(y)^2.             \tag{6.2}
\]

Marginal compensation correctly subtracts the first-order degree-one
reference.  It does not erase (6.2).

There are two possible gradings.

* In **Taylor-incidence degree**, (6.2) is the \(\ell=2\) term.
* In the natural mixed row--column excess

  \[
     \omega=|E|-|C|=\sum_{c\in C}(d(c)-1),                \tag{6.3}
  \]

  adjoining one degree-two common event raises \(\omega\) by one.
  A compensation coin common to two displayed rows is one new physical
  resource, hence one physical-profile extension.

Thus the assertion that the *physical profile/excess* generator starts at
\(+2\) is false without an additional cancellation.  If the finite score
is instead graded by Taylor-incidence degree, then the terminal term at
degree (J) contains repeated copies of the same selected edge and the
same coin.  The bound

\[
                         (CJ^2/m)^J                         \tag{6.4}
\]

obtained from distinct-owner higher codegrees does not bound those power
diagrams.  One needs the dynamic exponential/mixed-diagonal estimate
(EMDLE/MDLE), which is precisely the boundary already isolated in the
buffered-generator audit.

There is, however, a useful pathwise estimate for this surviving (+1)
orbit.  If (A_a=d_t(S\cup\{a\})), then for arbitrary nonnegative
weights (w_a), reverse summation gives

\[
 \nu_t\sum_g\sum_{a\in g}w_aA_a^2
 +\sum_a\chi_t(a)w_aA_a^2
 \le {2\over r}\sum_aw_aA_a^2.                         \tag{6.5}
\]

Indeed (d_t(a)\le\Delta_t),
(\nu_t=(r\Delta_t)^{-1}), and \(\chi_t(a)\le r^{-1}\).
This is exact in every induced residual.  Thus the repeated-child (+1)
has coefficient (2/r) in an **inherited-denominator flag norm**, and a
geometric cutoff with
\(\theta\asymp\sqrt{{\cal T}}\) pays it because

\[
              {{\cal T}\over\theta}{2\over r}
              =O\!\left(\sqrt{\log m/m}\right).          \tag{6.6}
\]

The normalization qualification is essential.  If the child square is
rebased to its own natural reference
\(\mu_{S,a}=d_0(Sa)u^{b-1}\), then

\[
 {A_a^2\over\mu_S^2}
 =\left({\mu_{S,a}\over\mu_S}\right)^2
   {A_a^2\over\mu_{S,a}^2},\qquad
 {\mu_{S,a}\over\mu_S}
 ={d_0(Sa)\over d_0(S)}{1\over u}.                       \tag{6.7}
\]

Consequently (6.5) is not automatically the coefficient (2/r) in a
natural child-normalized score.  It becomes one after retaining inherited
denominators, or after proving the equality-resolved conditional fibre
bound

\[
 {d_0(Sa)\over d_0(S)}\le {CJ^2\over m^2}qquad(k\le J), \tag{6.8}
\]

in the incidence range being monitored.  At
\(u\ge m^{-1/2}(\log m)^B\), (6.8) makes the rebasing factor in
(6.7) harmless.  Global maximum higher-codegree estimates do not by
themselves imply the conditional ratio (6.8) when (d_0(S)) is tiny;
forced common resources must first be equality-resolved and rare fibres
charged separately.

Therefore
`MATH_REDUCTION_COMPENSATED_PLUS_TWO_LOGSQUARED_CUTOFF_20260727.md`
is a correct conditional operator calculation **if** CG\(_J\) is supplied,
but marginal compensation is not a proof of CG\(_J\), and its displayed
terminal initialization does not by itself cover the diagonal grading.

## 7. The finite cutoff which remains legitimate

Stopping at (J=(\log m)^2\ll H) is still strategically sound.  The
time-zero mass of distinct physical terminal profiles is

\[
 \exp[-(1-o(1))J\log m],                                    \tag{7.1}
\]

and a fixed terminal link is paid by a stopped first-moment
supermartingale after the already audited physical-union integrating
factor.  This genuinely avoids the post-(H) scalar spine.

What it does **not** avoid is the dynamic centered diagonal below (J).
There are now two equivalent-looking ways to state the remaining theorem:

1. prove the active-shore centered bounds (4.1)--(4.2) uniformly through
   (J), or
2. prove the incidence-weighted mixed diagonal/exponential remainder
   through (J), including repeated edge and coin columns.

The first formulation has an advantage: it quotients out the exact
constant child mode and asks only for the fluctuation which can actually
create a new profile stop.  It is therefore strictly better targeted than
an absolute-value all-order scalar majorant.

In view of (6.5), the finite cutoff can be sharpened further.  The repeated
single-child part is already pathwise controlled.  Its unresolved pieces
are now precisely:

1. transport from the inherited flag norm in (6.5) to the natural
   stop-charging norm, equivalently (6.8) plus a rare-fibre quarantine;
2. distinct-child cross terms, including their equality partitions; and
3. the terminal mixed-power mass at order (J).

This is strictly smaller than an arbitrary MDLE theorem, but it is not
empty bookkeeping: item 1 is where a missing survival/reference factor can
turn (2/r) into (2/(ru^2)).

## 8. Exact next theorem

The most economical positive target is:

> **Centered Hilbert diagonal theorem.**  In the genuine compensated
> vertex-induced process, outside owner incidence (o(W)), every marked
> pair profile satisfies the active-shore mass lower bound (4.1) and the
> two inequalities (4.2), down to
> (z=m^{-1/2}(\log m)^B).

It is enough first to prove this only for pair parents; Proposition 4.1 then
closes PFS\(_3\), which is the sole profile-order boundary needed by the
already completed pair/whole-arm argument.  No all-order scalar weights and
no post-(H) propagation appear.

The theorem is not a consequence of maximum codegrees or of marginal
compensation.  Its source is the centered repeated-event kernel (3.4), so
any proof must be trajectory-specific or incidence-averaged.
