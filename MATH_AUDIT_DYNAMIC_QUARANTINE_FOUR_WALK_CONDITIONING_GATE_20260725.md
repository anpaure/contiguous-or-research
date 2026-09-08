# Dynamic-quarantine four-walk gate: conditioning and denominator audit

Date: 2026-07-25

Method: pure mathematics only. No computation or search is used.

## 0. Verdict

The raw pair-square and bow-tie estimates in
MATH_ATTACK_CATALOGUE_PAIR_SQUARE_AND_BOWTIE_GATE_20260725.md are not
challenged here. The proposed hereditary transfer, however, is not yet a
valid recurrence.

There are four exact conclusions.

1. Equations (6.3), (6.6), and (6.12) use the loss of an **unconditioned**
   target fibre. They therefore charge loss one whenever the tentative
   chunk deliberately consumes that target. Summed through a run ending
   at tag density \(1/\log m\), these diagonal terms have size
   \[
   \Theta(KT)=\Theta(W\sqrt m),
   \]
   not \(o(W)\). Thus (6.6) and (6.12), literally stated, are impossible.
2. The correct parallel-bite kernel must be conditioned on the target
   surviving. This conditioning still factors over tags, but introduces
   the exact denominators \(1-\alpha q_U(x)\). In a sequential
   activated-tag process the denominators are \(1-q_U(x)\), which are not
   controlled by an aggregate target-load estimate.
3. Fixed priority decorations do make codegrees monotone. Together with a
   lower bound \(d_{t+1}(v)\ge \rho_t d_t(v)\), monotonicity gives the exact
   factor \(\rho_t^{-2}\). It does **not** give \(z_t^{-2}\) when \(z_t\)
   is unused-resource density: for fixed \(K\)-resource decorations the
   natural degree density is \(z_t^{K-1}\). The missing link contraction
   is exactly the nontrivial assertion.
4. The new \(s=4\) swap-cube reservoir and the raw two-link factor
   \(\beta=m^{-1/2+o(1)}\) do not close this gap. The \(m^{-4}\) deletion
   bound applies to dynamic quarantine alone. Owner and priority
   conditioning may force a rare face, and conditioning a raw
   \(\beta\)-event on a set of mass \(\theta\) permits inflation to
   \(\min(1,\beta/\theta)\). The face-diffusion or witness-map statement
   isolated in
   MATH_ATTACK_S4_SWAP_CUBE_BOUNDARY_AND_DENOMINATOR_GATE_20260725.md is
   genuinely still necessary.

Hence the present data do not prove hereditary pair-square propagation.
They also do not furnish a counterexample to a correctly
survival-conditioned, PBBS-specific averaged recurrence. The precise
surviving gate is stated in Section 7.

## 1. The consumed-fibre diagonal

Let \(F_x\) be the current fibre of decorated candidates which claim a
currently available protected target \(x\). For a tentative chunk \(E\),
write, as in (6.7) of the pair-square report,

\[
 I_{s,x}(E)=\frac{D_s(F_x)-D_{s+1}(F_x)}{D_s(F_x)}.
 \tag{1.1}
\]

If \(x\in C(E)\), then \(E\) consumes \(x\), and every decorated candidate
in \(F_x\) is deleted. Therefore

\[
 \boxed{I_{s,x}(E)=1\qquad(x\in C(E)).}
 \tag{1.2}
\]

This is independent of quarantine, priorities, and all codegrees.

### Proposition 1.1 (unconditioned sequential gate is impossible)

Suppose every emitted legal chunk has \(K_s(E)\) available protected
claims. Then at every sequential step

\[
 \boxed{
 \sum_{x\ {\rm available}} I_{s,x}(E)^2\ge K_s(E).}
 \tag{1.3}
\]

Consequently, if a run emits \(N\) chunks, each with \(K_s(E)\ge K_-\),

\[
 \sum_x\sum_{s<N}I_{s,x}(E_s)^2\ge K_-N.
 \tag{1.4}
\]

#### Proof

Every one of the \(K_s(E)\) claimed targets contributes one to the left
side of (1.3) by (1.2). Sum over the sequential steps. \(\square\)

For the calibrated geodesic chunks,

\[
 T=(1+o(1))\frac Wg,
 \qquad
 K=g+2\sum_{q=1}^Q\bar c_q^{(g)}.
 \tag{1.5}
\]

Uniformly for \(q\le c\sqrt m\), the local central-binomial estimate gives

\[
 \frac{R_q}{W}=\exp(-q^2/m+o(1))=\Theta_c(1).
 \tag{1.6}
\]

Since \(T=(1+o(1))W/g\), (1.6) implies

\[
 c_q^{(g)}=\Theta_c(g)\qquad(q\le c\sqrt m).
 \tag{1.7}
\]

The deadline enlargement deletes only \(o(g)\) claims in total, so it does
not affect the following order of magnitude. Gaussian summation gives the
matching upper bound. Hence

\[
 \boxed{K=\Theta(g\sqrt m),\qquad KT=\Theta(W\sqrt m).}
 \tag{1.8}
\]

A run down to tag density \(1/\log m\) emits

\[
 N=(1-o(1))T.
 \tag{1.9}
\]

Equations (1.4), (1.8), and (1.9) prove that the left side of (6.12) in
the pair-square report is at least \(\Theta(W\sqrt m)\) before its
nonnegative tag terms are added. It cannot be \(o(W\eta^2)\) for any
\(\eta=o(1)\). If previously declared exceptional target fibres are
omitted from the sum, replace \(K_s(E)\) in (1.3) by the number of good
claims of \(E\). The already assumed \(o(W)\) exceptional-incidence
ledger then subtracts only \(o(W)\) from (1.4), while
\(KT=\Theta(W\sqrt m)\).

The same obstruction occurs in the parallel identity. Let

\[
 I_{t,x}(E)=
 \sum_{P\in F_x}p_{t,F_x}(P)h_t(P,E).
 \tag{1.10}
\]

If \(x\in C(E)\), then \(h_t(P,E)=1\) for every \(P\in F_x\), so
\(I_{t,x}(E)=1\). Therefore

\[
 \sum_x J_t(F_x)
 =\sum_x\sum_U\mathbb E I_{t,x}(E_U)^2
 \ge K T_t.
 \tag{1.11}
\]

After multiplying by the activation probability, a geometric run satisfies

\[
 \alpha\sum_{t<R}\sum_xJ_t(F_x)
 \ge K\alpha\sum_{t<R}T_t
 =(1-o(1))KT.
 \tag{1.12}
\]

Thus the \(\alpha\)-corrected version of (6.6) is also impossible as
written. The point is not excessive covariance: the terms in (1.12) are
fibres which have been intentionally consumed and therefore need no
residual-degree estimate.

## 2. The exact survival-conditioned parallel kernel

The conditioning used in Section 4 of the pair-square report is essential.
For a live tag \(U\), put

\[
 q_U(x)=\Pr_{E\sim\nu_U}(x\in C(E)).
 \tag{2.1}
\]

The tag variable is inactive with probability \(1-\alpha\), and otherwise
chooses \(E\sim\nu_U\). Let \(\mathcal A_x\) be the event that no tag
variable chooses a chunk containing \(x\). Independence over tags gives

\[
 \Pr(\mathcal A_x)=\prod_U(1-\alpha q_U(x)).
 \tag{2.2}
\]

Moreover, conditional on \(\mathcal A_x\), the tag variables remain
independent and their exact laws are

\[
 \Pr(X_U=\varnothing\mid\mathcal A_x)
 =\frac{1-\alpha}{1-\alpha q_U(x)},
 \tag{2.3}
\]

\[
 \Pr(X_U=E\mid\mathcal A_x)
 =\frac{\alpha\nu_U(E)\mathbf1_{\{x\notin C(E)\}}}
 {1-\alpha q_U(x)}.
 \tag{2.4}
\]

Thus, for two residual candidates \(e,f\ni x\), the conditioned
common-killer contribution of tag \(U\) is

\[
 \boxed{
 \widetilde p_U^{\,x}(e,f)
 =\frac{\alpha}{1-\alpha q_U(x)}
 \sum_{E:x\notin C(E)}
 \nu_U(E)\mathbf1_{\{E\sim e,\ E\sim f\}}.}
 \tag{2.5}
\]

This formula removes exactly the diagonal in Section 1. It also includes
same-tag killing: the relation \(E\sim e\) includes use of \(e\)'s tag.
Since \(q_U(x)\le1\), the parallel denominator is at most
\((1-\alpha)^{-1}\), which is harmless for one bite.

For a sequential process in which an activated tag is certainly sampled,
the corresponding conditioned law is

\[
 \boxed{
 \nu_U^x(E)=
 \frac{\nu_U(E)\mathbf1_{\{x\notin C(E)\}}}{1-q_U(x)}.}
 \tag{2.6}
\]

Here no harmless activation factor protects the denominator. An aggregate
bound on \(\sum_Uq_U(x)\) permits \(q_U(x)=1\) for one tag and therefore
does not control (2.6). This is the exact same-tag/max-influence obstruction
to calling the sequential formulation equivalent to the parallel one.

## 3. What fixed-decoration monotonicity actually proves

Priority decorations are fixed globally: a priority order claims a fixed
set of targets, and later history only deletes decorations. Dynamic
quarantine also only deletes. Hence, for every pair of resources,

\[
 d_{t+1}(x,y)\le d_t(x,y).
 \tag{3.1}
\]

This observation gives the following exact, but weaker, recurrence.

### Lemma 3.1 (monotone denominator recurrence)

Fix rank strata \(V_i,V_j\). Suppose every surviving
\(v\in V_i\cup V_j\) satisfies

\[
 d_{t+1}(v)\ge\rho_vd_t(v),
 \qquad \rho_v>0.
 \tag{3.2}
\]

Then for every surviving \(x\in V_i\),

\[
 \boxed{
 \sum_{y\in V_j\ {\rm surviving}}K_{t+1}(x,y)^2
 \le
 \frac1{\rho_x\inf_{y\in V_j}\rho_y}
 \sum_{y\in V_j}K_t(x,y)^2.}
 \tag{3.3}
\]

In particular, if all the ratios in (3.2) are at least \(\rho\), the loss
is at most \(\rho^{-2}\).

#### Proof

For every surviving \(y\), use (3.1) in the numerator and (3.2) in both
denominators:

\[
 \frac{d_{t+1}(x,y)^2}{d_{t+1}(x)d_{t+1}(y)}
 \le
 \frac1{\rho_x\rho_y}
 \frac{d_t(x,y)^2}{d_t(x)d_t(y)}.
\]

Sum over \(y\). \(\square\)

The distinction between \(\rho\) and unused-resource density \(z\) is
decisive. In a fixed \(K\)-uniform decorated hypergraph under independent
resource survival of density \(z\), the ideal scales are

\[
 \frac{d_z(x)}{d_0(x)}\sim z^{K-1},
 \qquad
 \frac{d_z(x,y)}{d_0(x,y)}\sim z^{K-2}.
 \tag{3.4}
\]

The two factors in (3.4) combine to give the desired pair-square inflation
\(z^{-2}\). Monotonicity alone discards the second estimate and gives only

\[
 z^{-2(K-1)}.
 \tag{3.5}
\]

At \(z=1/\log m\) and \(K=m^{1+o(1)}\), (3.5) is astronomically larger
than \((\log m)^2\). Therefore fixed decorations plus good **relative
stratum degrees** do not prove (5.1) unless those degrees are lower-bounded
by \(z\) times their original values, an assertion incompatible with the
ordinary fixed-edge survival scale. The missing assertion is precisely a
relative contraction of links, not mere monotonicity.

## 4. A finite exact concentration gadget

The following construction shows concretely why monotonicity cannot be
upgraded to pointwise link contraction without another hypothesis. It is
an abstract tagged protected-resource system, not an embedding claim for
the PBBS catalogue.

Let \(L\) be a perfect square and put \(D=L^{3/2}\),
\(s=D/\sqrt L=L\), and \(t=(D-s)/L=\sqrt L-1\). Take protected resources

\[
 x,z,b_1,\ldots,b_L,c_1,\ldots,c_L.
\]

There are \(s\) decorations containing \(\{x,z\}\), \(t\) decorations
containing each \(\{x,b_j\}\), and \(t\) decorations containing each
\(\{z,c_j\}\). Add one decoration

\[
 E=\{b_1,\ldots,b_L,c_1,\ldots,c_L\}.
\]

Pad the degree of each \(b_j,c_j\) to \(D\) with decorations containing
no other protected resource. All decorations may be padded by unprotected
private resources. Partition decorations into tags of degree \(D\), using
distinct tags for incident decorations and tag-only fillers. In particular
\(E\)'s tag contains \(E\) and \(D-1\) tag-only fillers. Put \(x\) in rank
\(r\), put \(z,b_1,\ldots,b_L\) in rank \(r+1\), and put the \(c_j\)'s in
rank \(r+2\).

All protected target degrees are \(D\), and

\[
 K(x,z)=\frac1{\sqrt L},
 \qquad
 K(x,b_j)=K(z,c_j)=\frac1L-\frac1{L^{3/2}},
 \qquad
 K(u,v)=\frac1D\quad
 (u\ne v,\ u,v\in\{b_1,\ldots,b_L,c_1,\ldots,c_L\}).
 \tag{4.1}
\]

Consequently

\[
 \sum_{y\ne x}K(x,y)^2\le\frac2L,
 \qquad
 \max_{u\in\{b_j,c_j\}}\sum_{y\ne u}K(u,y)^2
 \le\frac4{L^2}.
 \tag{4.2}
\]

The tag blocks contribute at most \(1/D\) to a target row. Every
intersection of two distinct decorations has width at most two, so the
four-antichain quarantine graph is empty.

For \(L\asymp m\), (4.2) has exactly the raw adjacent-rank
\(O(m^{-1})\) and same-rank \(O(m^{-2})\) scales. Condition on the legal
nibble choice \(E\). The resources \(x,z\) survive, but all their
blocker decorations are deleted. Hence

\[
 d'(x)=d'(z)=d'(x,z)=s,
 \qquad K'(x,z)=1,
 \tag{4.3}
\]

and the \(x\)-row pair-square jumps from at most \(2/L\) to at least one.
This respects the exact tagged kernel, includes same-tag resources, and
uses no quarantine edge. Its probability under uniform choice in \(E\)'s
tag is \(1/D\), so it is not a counterexample to a sufficiently averaged
exception ledger. It is a rigorous counterexample to deterministic
pointwise hereditary propagation and to any argument using only codegree
monotonicity and balanced surviving denominators.

## 5. Why the switch cubes and \(\beta\) do not yet repair conditioning

The \(s=4\) quarantine theorem proves that, outside an \(o(W)\) physical
ledger, quarantine removes at most

\[
 \eta=m^{-4+o(1)}
 \tag{5.1}
\]

of a raw fibre. It follows correctly that almost every raw cube vertex
lies in many quarantine-intact logarithmic faces. This statement concerns
the deletion set

\[
 Z_{\rm quar}=\{P:P\text{ is forbidden by a past four-antichain}\}.
 \tag{5.2}
\]

The actual residual additionally intersects with

\[
 A_t=\{P:\operatorname{owners}(P)\subseteq\mathcal O_t,\
                P\text{ has a feasible priority}\}.
 \tag{5.3}
\]

No lower cube-density or face-diffusion estimate for \(A_t\) is proved by
(5.1). Indeed, the exact forced-face example in the swap-cube report says
that a set of raw density \(2^{-t}\) can be one prescribed face and can lie
entirely inside a quarantine deletion set of the same tiny density.

The raw two-link estimate has the same conditioning limitation. If an
event \(B\) has raw probability at most \(\beta\) and the current residual
law is raw law conditioned on \(A\), where \(\Pr(A)=\theta\), then the only
unconditional conclusion is

\[
 \boxed{
 \Pr(B\mid A)\le\min\left\{1,\frac\beta\theta\right\}.}
 \tag{5.4}
\]

For

\[
 \beta=m^{-1/2+o(1)},
 \tag{5.5}
\]

a forced face of density \(\theta=2^{-t}\) already destroys subcriticality
when \(t\ge(1/2+o(1))\log_2m\). The available cube theorem allows faces up
to nearly \(4\log_2m\), so its raw reservoir does not supply the missing
conditional denominator.

Equations (5.1) and (5.5) would compose if one proved either

\[
 \Pr(\mathsf F_t\in\mathcal A\mid\mathcal F_t)
 \le m^{o(1)}\operatorname{Unif}_t(\mathcal A)
 \tag{5.6}
\]

for forced swap faces, or a direct witness map charging every failure of
(5.6) to a fresh two-link branch. Neither follows from high raw cube degree.
A parity class already shows abstractly that a set of density \(1/2\) in a
cube can contain no one-switch edge.

There is also a fibre issue which must be made explicit in a final proof.
A tag fibre is naturally a union of full arrival-switch cubes. A target
fibre need not be: toggling a switch may change whether that target is
claimed. One needs either a target-preserving subcube decomposition with
the asserted dimension, or an incidence-weighted cube argument. The raw
tag-fibre cube decomposition by itself does not provide target-fibre
denominators.

## 6. Audit of the cover/remainder refinement

The later cover/remainder refinement in Theorem 3.1 of the pair-square
report is valid and removes the former rank-aggregation concern. Write
\(\mathcal C(x)\) for the Boolean covers and cocovers of \(x\). The
leading adjacent-rank vector has norm \(O(m^{-1/2})\); after removing it,
the sum of the remaining block norms is \(O(m^{-1})\). Two distinct
members of \(\mathcal C(x)\) are either same-rank Johnson neighbours or
a nested rank-gap-two pair, so their normalized codegree is \(O(m^{-2})\).
It follows that

\[
 \mathfrak T(x)
 =O\left(\frac1m+\frac g{m^{3/2}}\right)
 =m^{-1+o(1)}.
 \tag{6.1}
\]

The protected Gaussian band has \(\Theta(W\sqrt m)\) targets. Therefore,
even after the \(z^{-2}\) inflation at \(z=1/\log m\) and the effective
\(\log\log m\) time factor, its raw aggregate covariance scale is

\[
 W\sqrt m\,
 m^{-1+o(1)}(\log m)^2\log\log m
 =Wm^{-1/2+o(1)}
 =o(W).
 \tag{6.2}
\]

Thus all scalar and raw rank-aggregation ledgers do close. The surviving
objection is solely hereditary conditioning: one must prove that the
weighted, survival-conditioned physical-label kernel retains the
\(m^{-1+o(1)}z^{-2}\) scale.

## 7. Corrected exact gate

For each protected target \(x\), let \(F_x\) be tracked only on the event
that \(x\) remains unused. Define the parallel conditional common-link
kernel by (2.5), including the tag resource and excluding direct use of
\(x\). Let \(I^\circ_{t,x}(E)\) be the fractional loss of the \(x\)-fibre
from conflicts other than consuming \(x\), under this conditioned law.

A valid positive theorem would have to prove, outside a physical
\(o(W)\) ledger,

\[
 \sum_t\alpha
 \sum_{x\ {\rm surviving}}
 \mathbb E\left[(I^\circ_{t,x}(E))^2
       \mid x\text{ survives the bite}\right]
 =o(W\zeta^2),
 \tag{7.1}
\]

for a tolerance \(\zeta=o(1)\), together with the analogous conditioned
tag term and common mean drift. In a sequential formulation one must add
either

\[
 \max_{U,x}q_U(x)\le1-\gamma_m
 \tag{7.2}
\]

with quantified \(\gamma_m\), or an equivalent truncation of the
denominators in (2.6). To derive (7.1) from the new cube input, one still
needs the face-diffusion/witness-map assertion (5.6), followed by the
physical square-label dispersal bound identified in Section 8.

## 8. Audit of the down-set entropy update

Theorem 4.1 of
DYNAMIC_QUARANTINE_EXCHANGE_AND_DOWNSET_ENTROPY_AUDIT_20260725.md is
correct. For a uniform random member \(X\) of a down-set
\(A\subseteq Q_f\), deletion of coordinate \(i\) injects
\(\{x\in A:x_i=1\}\) into \(\{x\in A:x_i=0\}\), so
\(\Pr(X_i=1)\le1/2\). Entropy subadditivity and concavity then give

\[
 \log_2|A|
 \le\sum_i h_2(\Pr(X_i=1))
 \le f h_2(\mathbb E|X|/f),
\]

and the stated quadratic entropy deficit follows. Every pair of one
coordinates at \(x\) does indeed anchor a full lower square, so the
aggregate square count is valid.

This update removes the parity-class example from the actual lane **if**
the following hypotheses are proved for the physical residual slices:

1. after fixing the priority and outside data, feasibility is a down-set
   (or subcube) in the chosen switch coordinates;
2. size-biased feasible slices have density
   \(\exp(-o(f))\); and
3. their physically effective free dimension satisfies
   \(f\to\infty\) faster than \(\log\log m\).

It does not repair Sections 1--3. Consumed fibres must still be
conditioned away, and aggregate square abundance does not give labelled
pair-square contraction. With the notation of the down-set report,
entropy controls

\[
 \sum_{\omega,x,y}N_\omega(x,y),
\]

whereas the required kernel contains

\[
 \sum_{x,y}
 \frac{\bigl(\sum_\omega N_\omega(x,y)\bigr)^2}
 {d_A(x)d_A(y)}.
\]

The cross-slice terms remain completely unsummed. Thus the new entropy
theorem is a valid denominator advance, but the exact next theorem is
still physical square-label dispersal under the survival-conditioned
law (2.5).

One scale distinction also needs correction before using the coding
estimate in Section 3 of the down-set report. The full carrier has
\(\Theta(M)=\Theta(m)\) commuting adjacent switches. A return-free
geodesic **chunk** has only \(\Theta(g)\) switches whose local diamonds
change its protected physical claims. Switches outside the chunk may
supply multiplicity but not distinct physical augmentations. Therefore
the assertion \(K/k^2=o(1)\) is justified only after proving that
\(k=\Theta(m)\) physically effective switches remain in the chunk
hyperedge. With the presently explicit chunk-local dimension
\(k=\Theta(g)\) and \(K=\Theta(g\sqrt m)\),

\[
 \frac K{k^2}=\Theta\left(\frac{\sqrt m}{g}\right),
\]

which is not known to vanish at the stated scales.

This is the precise proved/conditional boundary. No coefficient-one
conclusion follows yet.
