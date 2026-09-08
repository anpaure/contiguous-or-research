# Pair CHD: exact bias audit, PSF reduction, and the surviving fourth kernel

Date: 2026-07-27

Scope: the pair-parent centered Hilbert diagonal in the actual
selected-edge plus compensation generator.  This note audits only CHD;
it does not assert a near-factor theorem.

## 0. Verdict

There is a useful exact reduction, but CHD is not yet proved.

1.  After the child-specific predictable integrating factors of Lemma
    3.1 in
    `MATH_AUDIT_HILBERT_TWO_SHORE_PROFILE_ENERGY_AND_FINITE_CUTOFF_20260727.md`,
    the coordinatewise predictable bias is zero.  There is nevertheless
    a centering mismatch when one event deletes some shore coordinates
    and decrements the survivors.  Exact weighted ANOVA turns it into a
    positive scalar term, and Lemma 4.0 plus PFS\(_3\) bounds that term by
    \(o(L^C/(r(r-2)))\).  Thus the bias half of CHD closes, but it is not
    identically zero.

2.  Expanding one selected-edge square over the two killed rows and
    resolving their common physical resources separates the diagonal
    into two pieces.  The piece in which the selected edge meets the two
    exclusive shores is bounded by the already proved whole-arm PSF and
    has the required scale

    \[
       O\!\left({L^C\over r(r-2)}\right).
       \tag{0.1}
    \]

3.  The remaining piece is not a compensation artefact.  It is the
    conditional co-occurrence kernel

    \[
       d_t(S\cup\{a,y\}),
       \tag{0.2}
    \]

    with one common physical resource \(y\).  Selected edges containing
    \(y\) and the compensation clock of \(y\) have combined rate exactly

    \[
       \nu_t d_t(y)+\chi_t(y)={1\over r}.
       \tag{0.3}
    \]

    Thus deleting the compensation clocks only replaces \(1/r\) by
    \(\nu_t d_t(y)\); on degree-flat resources this is only a constant
    factor.

4.  PPS, PFS\(_3\), Lemma 4.0, and whole-arm PSF do not by themselves
    bound this last kernel.  A completely explicit block-design link
    below satisfies the corresponding marginal and pair/triple scales
    but has centered common-resource diagonal \(\Theta(u/r)\), a factor
    \(\Theta((r-2)u)\) above CHD.  It may be realized either through
    compensation clocks on deficient children or through selected-edge
    clocks on degree-flat children.  It is an abstract induced
    \(r\)-uniform stopped state, not a proved reachable state of the
    promotion-frame catalogue.  Consequently it is a logical obstruction
    to deriving CHD from the currently listed stops, not a refutation of a
    trajectory-specific promotion-frame theorem.

The exact remaining theorem is therefore an incidence-weighted,
trajectory-specific conditional spectral estimate for (0.2).  It is
strictly weaker than pointwise PFS\(_4\), but it is genuinely fourth
profile information.

## 1. Notation and the exact normalized kernel

Fix an active pair parent \(S\), put

\[
                         b=r-2,
\]

and write

\[
 \mu_a=d_0(Sa)u^{b-1},\qquad
 p_a={d_0(Sa)\over b\,d_0(S)},\qquad
 C_S=b\,d_0(S)u^{b-1}.
 \tag{1.1}
\]

Then

\[
                         \mu_a=C_Sp_a.                    \tag{1.2}
\]

Let

\[
 A_a=d_t(Sa),\qquad D_{ay}=d_t(Say),\qquad X_a={A_a\over\mu_a}.
 \tag{1.3}
\]

On the current live extension shore \({\cal A}_t\),

\[
 \sum_{a\in{\cal A}_t}p_aX_a=uX_S.                       \tag{1.4}
\]

Before PPS and PFS\(_3\), corridor constants give

\[
 X_S\le CL^C A_2,\qquad 0\le X_a\le CL^C A_3.            \tag{1.5}
\]

For a selected edge \(g\) avoiding the protected parent and a surviving
coordinate \(a\notin g\), define

\[
 K_g(a)=\#\{F\in{\cal H}_t:Sa\subseteq F,
                         (F\setminus Sa)\cap g\ne\varnothing\}.
 \tag{1.6}
\]

For a compensation resource \(y\ne a\), the decrement is exactly

\[
                         K_y(a)=D_{ay}.                    \tag{1.7}
\]

If \(c_a(t)=\exp[-\int_0^t\beta_{Sa}(s)\,ds]\), then
\(c_a=1+o(1)\) before the stated stops, and the actual jump vector is

\[
 h_{g,a}=c_a{K_g(a)\over\mu_a},\qquad
 h_{y,a}=c_a{D_{ay}\over\mu_a}.                          \tag{1.8}
\]

Coordinates physically deleted by the event are first removed from the
shore.  This contributes the nonpositive weighted-ANOVA deletion term
and is never included in (1.8).

## 2. Exact deletion-centroid bias and its bound

Put \(Z_a=c_aX_a\), and on the current shore center at

\[
 \bar Z={\sum_ap_aZ_a\over P},\qquad P=\sum_ap_a,
 \qquad V_S=\sum_ap_a(Z_a-\bar Z)^2.                    \tag{2.1}
\]

By definition of the exact coordinate compensator \(\beta_{Sa}\), the
nonterminal coordinate drift is zero:

\[
                  (\partial_t+{\cal L}_t)Z_a=0           \tag{2.2}
\]

up to the terminal death of the coordinate, which removes it from
(2.1).  This does not make the centered bias identically zero.  The
reason is that the coordinatewise cancellation uses the old shore,
whereas the decrement vector is centered on the shore left after the
event.

Here is the exact correction.  For one event \(e\), let \(D_e\) be the
deleted coordinates, \(B_e={\cal A}_t\setminus D_e\), and put

\[
 q_e=\sum_{a\in D_e}p_a,\qquad P_e=P-q_e,\qquad
 H_e=\sum_{a\in B_e}p_ah_{e,a}.                          \tag{2.3}
\]

Write \(\bar Z\) and \(\bar Z_{B_e}\) for the old- and new-shore
means, and \(\delta_e=\bar Z_{B_e}-\bar Z\).  Weighted ANOVA gives

\[
 V({\cal A}_t,Z)-V(B_e,Z)
 \ge {PP_e\over q_e}\,\delta_e^2.                        \tag{2.4}
\]

After the coordinatewise linear drifts cancel, the sole mismatch is
\(2\delta_eH_e\).  Consequently

\[
 2\delta_eH_e-{PP_e\over q_e}\delta_e^2
 \le {q_eH_e^2\over PP_e}.                              \tag{2.5}
\]

Thus the exact generator inequality is

\[
 \boxed{
 (\partial_t+{\cal L}_t)V_S
 \le Q_S+R_S^{\rm shore},
 \qquad
 Q_S=\sum_e\lambda_e
       \|h_e-\bar h_e\mathbf1\|_{L^2(p;B_e)}^2,}
 \tag{2.6}
\]

where

\[
 \boxed{
 R_S^{\rm shore}
 \le\sum_e\lambda_e{q_eH_e^2\over P(P-q_e)}.}           \tag{2.7}
\]

This term is smaller than the CHD scale.  Lemma 4.0 gives

\[
 q_g\le {L^C\over bm},\qquad
 q_y=p_y\le {L^C\over bm^2}.                            \tag{2.8}
\]

For a selected edge, reverse the child-row sum.  Every killed parent-link
row contributes at most \(b\) surviving child incidences, and PFS\(_3\)
plus the one-frame child sum give

\[
 H_g\le {CL^CA_3\over m}.                               \tag{2.9}
\]

For a compensation coin,

\[
 H_y={b-1\over b\,d_0(S)u^{b-1}}d_t(Sy)
     =(b-1)p_yX_y
 \le {CL^CA_3\over m^2}.                               \tag{2.10}
\]

Finally, reversing all nonterminal row-deletion incidences gives

\[
 \sum_e\lambda_eH_e
 \le C\sum_ap_aX_a
 \le CL^CA_2u.                                         \tag{2.11}
\]

On the active-shore stop \(P\ge c_0u\), equations
(2.7)--(2.11) imply

\[
 \boxed{
 R_S^{\rm shore}
 \le {L^C\over b m^2u}
 =o\!\left({1\over rb}\right)}                         \tag{2.12}
\]

uniformly for \(u\ge m^{-1/2}(\log m)^B\).  The last equality uses
\(r,b=(1+o(1))m\), with polylogarithms absorbed into \(L^C\).

Thus the bias half of (4.2) is closed.  The important point is that it is
paid jointly by the favorable deletion term and the small static shore
mass, not erased by coordinatewise compensation alone.

The same calculation holds in the edge-only process with the edge-only
child compensator.  It does not improve the bracket in Section 4.

## 3. Row-pair expansion and the PSF-paid part

For fixed \(a\), expand

\[
 K_g(a)^2
 =\sum_{F,F'\in{\cal H}_t(Sa)}
   \mathbf1\{g\hbox{ kills }F\}
   \mathbf1\{g\hbox{ kills }F'\}.                       \tag{3.1}
\]

Resolve the common physical prefix of \(F,F'\).  An event counted in
(3.1) has one of two certificates.

* It contains a common resource
  \(y\in(F\cap F')\setminus Sa\).
* Avoiding the common prefix, it meets both exclusive shores
  \(F\setminus F'\) and \(F'\setminus F\).

The second class has clock mass at most

\[
                         \beta_*
 \le {CL^CA_H\over m^2u}                                 \tag{3.2}
\]

by the stopped whole-arm PSF theorem.  Dropping centering only enlarges
the square, so its contribution to (2.3) is at most

\[
 \begin{aligned}
 Q_S^{\rm excl}
 &\le \beta_*\sum_ap_aX_a^2\\
 &\le \beta_*\,(CL^CA_3)\sum_ap_aX_a\\
 &\le {CL^CA_HA_2A_3\over m^2}.
 \end{aligned}                                           \tag{3.3}
\]

Here (1.4)--(1.5) supply the factor \(u\) which cancels the
\(u^{-1}\) in (3.2).  Since \(r,b=(1+o(1))m\), (3.3) is exactly
the desired \(L^C/(rb)\) scale.  This calculation includes all
exclusive-shore equality shapes already covered by PSF; no PFS\(_4\)
is used.

## 4. The surviving common-resource kernel

For a fixed resource \(y\), the selected-edge clocks containing \(y\)
have total rate \(\nu_td_t(y)\), while its compensation clock has rate
\(\chi_t(y)\).  Hence (0.3) is exact.  In the edge-only process the
coefficient is \(\nu_td_t(y)\).

At the uncentered second-moment level, reversing the common-resource
certificate gives the exact sufficient remainder

\[
 \boxed{
 {\cal R}_S(t)
 ={1\over r}\sum_{a,y}
       p_a\left({D_{ay}\over\mu_a}\right)^2.}
 \tag{4.1}
\]

Indeed,

\[
 \sum_{F,F'\in{\cal H}_t(Sa)}
 |(F\cap F')\setminus Sa|
 =\sum_yD_{ay}^2.                                       \tag{4.2}
\]

The genuinely centered version for singleton clocks is

\[
 \boxed{
 {\cal T}_S(t)
 ={1\over r}\sum_y
  \operatorname {Var}_{p;\,{\cal A}_t\setminus\{y\}}
   \left(a\longmapsto {D_{ay}\over\mu_a}\right).}
 \tag{4.3}
\]

For selected edges containing several common resources, (4.3) must be
augmented by their equality-resolved joint version; (4.1) is a valid
upper bound for all of them.  Equations (3.3)--(4.3) show that the
remaining CHD statement is precisely

\[
 \boxed{
 \text{the incidence aggregate of the common-resource centered
 kernel is }O\!\left({L^C\over rb}\right).}
 \tag{4.4}
\]

This is a conditional Hilbert--Schmidt estimate.  To display it, use
(1.2) and put

\[
 L_S(a,y)={D_{ay}\over C_S\sqrt{p_ap_y}}.                \tag{4.5}
\]

The matrix \(L_S\) is symmetric.  Its row sums satisfy

\[
 \sum_yD_{ay}=(b-1)A_a,                                  \tag{4.6}
\]

but (4.6) controls only its Perron mode.  The expression (4.3) is the
weighted Hilbert--Schmidt mass off the corresponding rank-one mode.
PFS\(_3\) bounds the row sums through \(X_a\); it does not bound that
off-rank-one mass.

Thus CHD has not reduced to a scalar fourth maximum, but neither has
fourth-profile information disappeared.  It survives as the averaged
spectral statement (4.4).

## 5. Why PPS and PFS\(_3\) alone cannot prove (4.4)

The following finite construction is a calibration obstruction.  Put
\(v=b^2\), take \(N=b^3\) child resources, and split them into
\(N/v=b\) groups of size \(v\).  In the current \(S\)-link, take every
set

\[
                         S\cup B,
 \qquad B\in\binom{G}{b},                                \tag{5.1}
\]

inside each group \(G\), and no cross-group row.  This is a simple
\(r\)-uniform link.  Every child has degree

\[
 A=\binom{v-1}{b-1},                                     \tag{5.2}
\]

and two distinct children in the same group have joint degree

\[
 D=\binom{v-2}{b-2}
   =A{b-1\over v-1};                                     \tag{5.3}
\]

children in different groups have joint degree zero.

Fix any density \(u\in(0,1)\).  Add inactive time-zero rows so that on
the active shore

\[
 p_a={u\over N},\qquad \mu_a=A,qquad X_a=1,\qquad P=u.
 \tag{5.4}
\]

The missing mass \(1-u\) is assigned to inactive child resources.
There are two equivalent ways to complete the current catalogue.

* Pad with a disjoint regular component of maximum degree
  \(\Delta\gg A\).  Then every active child in (5.1) has

\[
                         \chi_t(a)=(1-o(1))/r.            \tag{5.5}
\]

* Alternatively, for every active child \(a\), add \(\Delta-A\)
  active background edges through \(a\), using fresh private resources
  and avoiding \(S\).  Then \(d_t(a)=\Delta\), \(\chi_t(a)=0\), and
  the total selected-edge clock rate through \(a\) is
  \(\nu_td_t(a)=1/r\).  Such a background edge deletes \(a\) and has
  exactly the same decrement vector on the surviving child shore as the
  singleton clock of \(a\).

The time-zero degrees may be padded, using edges carrying deleted private
markers, so that

\[
 \Delta=D_0u^{r-1},\quad
 d_0(Sa)u^{b-1}=A,\quad
 d_0(ay)u^{r-2}=D.                                      \tag{5.6}
\]

All quantities can be made integral by a common blow-up.  Equations
(5.4)--(5.6) put the parent at its neutral reference, put every child
strictly below any polylogarithmic PFS\(_3\) threshold, and put every
active pair below its density-corrected PPS threshold.  The one-child
ratio is \(\Theta(b^{-2})\); one event-row sum has scale
\(\Theta(b^{-1})\).  Taking \(N=b^3\) also makes the usual static theta
sum at most the required \(O(b^{-2})\) scale after normalization.

For a fixed \(y\), however,

\[
 {D_{ay}\over\mu_a}
 =\begin{cases}
   (b-1)/(v-1),&a\ne y\hbox{ in the same group},\\
   0,&\hbox{otherwise}.
  \end{cases}                                            \tag{5.7}
\]

Therefore

\[
 \operatorname {Var}_{p}
  \left({D_{ay}\over\mu_a}:a\ne y\right)
 =(1+o(1)){u\over N}.                                   \tag{5.8}
\]

Summing (5.8) over the \(N\) active choices of \(y\), and using either
completion above, gives

\[
 \boxed{
 Q_S^{\rm common}=(1+o(1)){u\over r}.}                  \tag{5.9}
\]

For constant \(u\), this exceeds \(L^C/(rb)\) by
\(b/L^C\); even at \(u=m^{-1/2}\) it exceeds it by
\(m^{1/2}/L^C\).

This construction is vertex-induced: the padded rows excluded from the
current state contain deleted private markers.  It is not asserted to be
an induced subcatalogue of the ordinary promotion-frame design, nor to be
reached with nonnegligible probability by its random process.  It proves
the exact logical point:

\[
 \boxed{
 \text{marginal degree, PPS, PFS\(_3\), and static theta data do not
 imply CHD for a general induced stopped state}.}
 \tag{5.10}
\]

## 6. Edge-only clocks do not change the boundary

Remove the singleton compensation clocks and give every child its exact
edge-only Doléans normalizer.  The proof of (2.3) is unchanged, with

\[
 Q_S^{\rm edge}=\nu_t\sum_g\|h_g^\circ\|_p^2.           \tag{6.1}
\]

The exclusive-shore part is still (3.3).  For a common resource \(y\),
the coefficient in (4.3) becomes

\[
                         \nu_td_t(y)\le {1\over r}.       \tag{6.2}
\]

On a degree-flat resource \(d_t(y)=(1-o(1))\Delta_t\), this is
\((1-o(1))/r\).  A predictable normalizer cancels linear drift; it
cannot cancel the bracket of an event which simultaneously kills the
same common-resource sublink in many child coordinates.  Hence the
edge-only reformulation gives no asymptotic gain for (4.4).

## 7. Exact next theorem

The pair CHD route now needs only the following catalogue-specific
statement.

> **Trajectory conditional-kernel theorem.**  In the actual
> promotion-frame induced process, before the degree, PPS, PFS\(_3\),
> whole-arm, and active-shore stops, the marked-pair incidence aggregate
> of the equality-resolved common-resource kernel (4.3), including the
> joint selected-edge equality classes, is
> \(O(L^C/(r(r-2)))\).

Together with (2.3) and (3.3), this theorem is exactly CHD and hence,
by Proposition 4.1 of the Hilbert note, would close PFS\(_3\).

What has been eliminated is the predictable-bias problem and every
exclusive-shore event.  What remains is a single state-specific
conditional spectral theorem.  It cannot be replaced by maximum
PFS\(_4\), but neither can it be inferred from the existing pair and
triple stops alone.
