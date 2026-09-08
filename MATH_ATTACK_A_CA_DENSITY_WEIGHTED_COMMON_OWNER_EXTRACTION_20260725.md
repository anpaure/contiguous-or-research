# Density-weighted common-owner extraction

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, solver, or
long-running computation is used.

## 0. Result

The audited pointed cyclic-flag theorem and the exact directed residual
Hall theorem combine more sharply than the global-spill estimate suggests.
Fix one exact factor, one **common** balanced quota flow, and a monotone
packet-compatible release profile

\[
 \varnothing=E_0\subseteq E_1\subseteq\cdots\subseteq E_K.
\]

For a signed prescribed target family \(\mathcal T_a\), let

\[
 \alpha_a=
 \frac{|\mathcal T_a|}
      {\binom{2m+1}{m-\tau(a)}}.
\]

If \(J_q^\uparrow\) denotes the number of released depth-\(q\) canonical
occurrences lying in overloaded common-quota fibres, then one joint
coordinate relabelling and the audited parent pruning leave at least

\[
 \boxed{
 L\ge
 \sum_{a\in\mathcal A}
       \alpha_a\bigl(W-J_{\tau(a)}^\uparrow\bigr)
       -P_{\mathcal A}^{\#}.}
 \tag{0.1}
\]

Here \(P_{\mathcal A}^{\#}=o(W)\) is the exact audited collision bound.
Thus the single finite inequality

\[
 \boxed{
 \sum_{a\in\mathcal A}\alpha_aJ_{\tau(a)}^\uparrow
 \le
 W\sum_{a\in\mathcal A}\alpha_a
 -P_{\mathcal A}^{\#}-\varepsilon_AKW}
 \tag{WCOI}
\]

implies the full integral pointed extraction conclusion on the unchanged
literal word of the same exact factor.

The exact common-quota loss term in this argument is the density-weighted
deficit \(\sum_a\alpha_aD_{\tau(a)}^b\), defined below.  Packet feasibility
proves

\[
 D_q^b\le J_q^\uparrow,
\]

so (WCOI) is the common-owner incidence form of the gate.  It is strictly
sharper than subtracting \(J_q^\uparrow\) once in full at every signed slot:
for each slot the exact improvement is

\[
 \alpha_a\rho_q+(1-\alpha_a)J_q^\uparrow\ge0.
\]

All floor baselines, high-quota sets, common-depth compatibility, and owner
labels are retained.

## 1. Exact common-quota notation

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad
 K=\lceil A\sqrt m\rceil,
 \qquad V_q=\binom{[n]}{m-q}.
 \tag{1.1}
\]

At depth \(q\), write the exact division

\[
 W=c_q|V_q|+\rho_q,
 \qquad
 c_q=\left\lfloor\frac W{|V_q|}\right\rfloor,
 \qquad 0\le\rho_q<|V_q|,
 \tag{1.2}
\]

and put \(u_q=c_q+\mathbf1_{\{\rho_q>0\}}\).  Fix one oriented exact
wreath factor \(F\), with canonical flags \(\Gamma_q(X)\), and let

\[
 \ell_q(S)=|\{X:\Gamma_q(X)=S\}|.
 \tag{1.3}
\]

Fix balanced vectors belonging to one common integral nested flow:

\[
 b_q(S)=c_q+\mathbf1_{H_q}(S),
 \qquad |H_q|=\rho_q.
 \tag{1.4}
\]

In particular, the high sets \(H_q\) are not optimized independently.
Define the exact fixed-common-quota deficit

\[
 D_q^b(F)
 =\sum_{S\in V_q}(b_q(S)-\ell_q(S))_+.
 \tag{1.5}
\]

Since both vectors have total mass \(W\),

\[
 \boxed{
 D_q^b(F)
 =\sum_{S\in V_q}(\ell_q(S)-b_q(S))_+.}
 \tag{1.6}
\]

Assume that the monotone release profile satisfies all exact survival and
directed crossing inequalities at transition \(q\), with \(E_q\).  Thus it
is not merely a collection of rankwise marginals: by the monotone-release
Hall theorem it realizes one integral common nested resolution.  Put

\[
 a_q^{E_q}(S)=|\{X\in E_q:\Gamma_q(X)=S\}|,
 \tag{1.7}
\]

\[
 J_q^\uparrow(F,b;E_q)
 =\sum_{\ell_q(S)>b_q(S)}a_q^{E_q}(S).
 \tag{1.8}
\]

The survival inequalities give, fibre by fibre,

\[
 a_q^{E_q}(S)\ge \ell_q(S)-b_q(S)
 \qquad\text{when }\ell_q(S)>b_q(S).
\]

Together with (1.6), this proves the exact sandwich

\[
 \boxed{D_q^b(F)\le J_q^\uparrow(F,b;E_q)\le |E_q|.}
 \tag{1.9}
\]

The crossing inequalities are what certify that these same released owners
extend integrally through the actual adjacent Boolean transitions.  No
independently chosen quota vector is used below.

## 2. Density-weighted relabelling theorem

Let \(\mathcal A\subseteq\{-K,\ldots,K+1\}\) be signed slots and let
\(\mathcal T_a\) be prescribed targets at signed rank \(m+a\).  Put

\[
 \tau(a)=
 \begin{cases}
  -a,&a\le0,\\
  a-1,&a\ge1,
 \end{cases}
 \qquad
 N_q=|V_q|,
 \qquad
 \alpha_a=\frac{|\mathcal T_a|}{N_{\tau(a)}}.
 \tag{2.1}
\]

For an upper signed slot, targets are transported to \(V_{\tau(a)}\) by
complementation.  Complementation commutes with every coordinate
permutation and preserves cardinality, so the same \(\alpha_a\) applies.

Assume the prescribed targets are partitioned into fixed-dimensional
product parents satisfying the audited extension bound

\[
 \#\{\text{rank-}g\text{ extensions in one parent}\}
 \le \binom{g+d-1}{d-1}
 \tag{2.2}
\]

for a fixed \(d\).  Define the exact full-incidence collision bound

\[
 P_{\mathcal A}^{\#}
 =W\sum_{\substack{a<a'\\a,a'\in\mathcal A}}
 \frac{\binom{a'-a+d-1}{d-1}}
      {\binom{m+1-a}{a'-a}}.
 \tag{2.3}
\]

The audited estimate gives

\[
 P_{\mathcal A}^{\#}=O_{A,d}(KW/m)=o(W).
 \tag{2.4}
\]

### Theorem 2.1 — one relabelling pays only density-weighted deficit

There is one coordinate relabelling of \(F,b\), and of the compatible
release certificate, followed by a choice of at most \(u_{\tau(a)}\)
literal occurrences in each signed target fibre and the audited
one-edge-per-start--parent pruning, for which the resulting occurrence
graph has target degree at most

\[
 \Delta_A=\max_{q\le K}u_q=O_A(1)
\]

and edge count

\[
 \boxed{
 L\ge
 \sum_{a\in\mathcal A}
 \alpha_a\bigl(W-D_{\tau(a)}^b(F)\bigr)
 -P_{\mathcal A}^{\#}.}
 \tag{2.5}
\]

Consequently (0.1) holds.

#### Proof

Choose a uniformly random coordinate permutation \(\sigma\).  Transport
the factor and the one common quota flow together.  At a lower slot of
depth \(q\), let \(\mu_\sigma(T)\) and \(b_\sigma(T)\) be the transported
canonical load and quota.  At an upper slot use their complemented
transports.  In both cases

\[
 b_\sigma(T)\in\{c_q,u_q\}.
\]

Put

\[
 \widehat\mu_\sigma(T)=\min\{\mu_\sigma(T),u_q\},
 \qquad
 d_\sigma(T)=(b_\sigma(T)-\mu_\sigma(T))_+.
\]

Pointwise,

\[
 \widehat\mu_\sigma(T)
 \ge b_\sigma(T)-d_\sigma(T).
 \tag{2.6}
\]

The symmetric group is transitive on every signed target rank.  The quota
and deficit vectors have exact total masses

\[
 \sum_Tb_\sigma(T)=W,
 \qquad
 \sum_Td_\sigma(T)=D_q^b(F).
\]

Therefore, for every prescribed family \(\mathcal T_a\),

\[
 \mathbb E_\sigma
 \sum_{T\in\mathcal T_a}b_\sigma(T)
 =\alpha_aW,
 \tag{2.7}
\]

\[
 \mathbb E_\sigma
 \sum_{T\in\mathcal T_a}d_\sigma(T)
 =\alpha_aD_q^b(F).
 \tag{2.8}
\]

Let \(R(\sigma)\) be the total number of designated capped prescribed
occurrences over all signed slots.  Summing (2.6)--(2.8) gives

\[
 \mathbb E R(\sigma)
 \ge
 \sum_{a\in\mathcal A}
 \alpha_a\bigl(W-D_{\tau(a)}^b(F)\bigr).
 \tag{2.9}
\]

Let \(Y(\sigma)\) be the number of same-parent pairs in the **full,
uncapped** prescribed occurrence graph.  The audited conditional-extension
calculation gives

\[
 \mathbb EY(\sigma)\le P_{\mathcal A}^{\#}.
 \tag{2.10}
\]

Choose one \(\sigma\) for which

\[
 R(\sigma)-Y(\sigma)
 \ge \mathbb E(R-Y).
\]

Only after this choice, designate exactly
\(\widehat\mu_\sigma(T)\) occurrences in every prescribed fibre.  Every
same-parent pair in the capped graph was already counted by \(Y(\sigma)\).
Keeping one edge in a start--parent cell of size \(r\) deletes

\[
 r-1\le\binom r2
\]

edges.  Hence the total pruning loss is at most \(Y(\sigma)\).  Equations
(2.9)--(2.10) prove (2.5).  The fibre cap proves the target-degree bound.
Finally use (1.9) with the nonnegative coefficients \(\alpha_a\) to obtain
(0.1). \(\square\)

## 3. The single construction-enabling inequality

The exact finite density-weighted deficit gate is

\[
 \boxed{
 \sum_{a\in\mathcal A}
 \alpha_aD_{\tau(a)}^b(F)
 \le
 W\sum_{a\in\mathcal A}\alpha_a
 -P_{\mathcal A}^{\#}-\varepsilon_AKW.}
 \tag{3.1}
\]

Under (3.1), Theorem 2.1 gives \(L\ge\varepsilon_AKW\).  The audited
finite floor-capped extraction theorem may therefore be applied with

\[
 s=\left\lfloor\frac{\varepsilon_AK}{2}\right\rfloor.
\]

Indeed, the pruned left degree is at most \(|\mathcal A|\), so
\(L\le |\mathcal A|W\) and hence
\(|\mathcal A|\ge\varepsilon_AK\).  Thus \(s\le|\mathcal A|\); moreover
\(s/\Delta_A=\Theta_{A,\varepsilon_A}(K)\), and the audited degree-count
bound leaves \(\Omega_{A,\varepsilon_A}(W)\) starts of degree at least
\(s\).

It yields, for every fixed \(\delta>0\) and all sufficiently large \(m\),
at least \(\delta W\) globally distinct prescribed shoulder targets on

\[
 O_{A,\varepsilon_A,\delta}(W/K)
\]

literal pointed starts, with targets at each start lying in distinct
product parents and with sharing excess \((\delta-o(1))W\).  No target is
created, no seam is added, and the exact factor is unchanged.

By (1.9), the single common-owner inequality (WCOI) implies (3.1).  It is
therefore a direct sufficient construction gate using owners already
certified by all survival and directed Hall packets.

For comparison, the earlier slotwise estimate subtracts
\(J_q^\uparrow\) in full from the floor supply
\(c_q|\mathcal T_a|\).  Since

\[
 c_q|\mathcal T_a|
 =\alpha_a c_qN_q
 =\alpha_a(W-\rho_q),
\]

the improvement of the new contribution over the old one is exactly

\[
 \begin{aligned}
 &\alpha_a(W-J_q^\uparrow)
   -\bigl(c_q|\mathcal T_a|-J_q^\uparrow\bigr)\\
 &\qquad
 =\alpha_a\rho_q+(1-\alpha_a)J_q^\uparrow\ge0.
 \end{aligned}
 \tag{3.2}
\]

Thus (WCOI) retains every floor correction and is never weaker; it can be
strictly stronger by a linear amount.

## 4. Precise boundary

Theorem 2.1 and the implication (WCOI) \(\Rightarrow\) integral pointed
extraction are proved.  The remaining construction statement addressed by
this extraction sublane is to choose one exact factor, one common balanced
quota flow, and one monotone family satisfying every survival and directed
crossing inequality for which (WCOI) has a fixed positive margin.  This
statement gives the audited pointed endpoint construction; by itself it is
not asserted to finish the other fusion steps of the constant-one theorem.

This is weaker than the tail-area condition

\[
 \sum_{q\le K}\frac{|E_q|}{c_q}=o(W)
\]

that proves the full labelled theorem \((\mathrm{CA}_A)\): (WCOI) only
charges released owners in overloaded canonical fibres, and charges each
signed slot by its exact prescribed-target density.  It is nevertheless
strong enough for the audited pointed endpoint construction, with no
rankwise quota substitution and no loss of cyclic packet compatibility.
