# Neighborhood regularity by Bonferroni and one-sided quarantine

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Let \({\cal H}\) be a residual catalogue hypergraph.  For a catalogue
edge \(f\), let

\[
 N(f)=|\{e\in E({\cal H}):e\cap f\ne\varnothing\}|
 \tag{0.1}
\]

be its conflict-neighborhood size.  Uniform edge sampling gives common
degree contraction if \(N(f)\) is nearly constant over almost all
candidate edges in every protected fibre.

There are two possible routes.

1. A direct variance expansion of \(N(f)\) requires codegrees of up to
   five resources.  The existing pair-square/triangle statistic does
   not contain these terms.
2. A one-sided Bonferroni estimate avoids that hierarchy.  Put

\[
 L(f)=\sum_{v\in f}d(v),\qquad
 B(f)=\sum_{\{u,v\}\subseteq f}d(u,v).
 \tag{0.2}
\]

Then exactly

\[
 \boxed{L(f)-B(f)\le N(f)\le L(f).}
 \tag{0.3}
\]

Consequently, if \(L(f)=(1+o(1))L_0\) and merely

\[
 \mathbb E_f B(f)=o(L_0),
 \tag{0.4}
\]

then deleting an \(o(1)\) fraction of candidate edges makes
\(N(f)=(1+o(1))L_0\) pointwise on the rest.  No variance estimate is
needed.

For the uniform anchored fibre \(E_x=\{f:x\in f\}\), the mean in
(0.4) has the exact form

\[
 \boxed{
 \mathbb E_{f\in E_x}B(f)
 ={1\over d(x)}
 \sum_{\{u,v\}}d(u,v)d(x,u,v).}
 \tag{0.5}
\]

The part with \(x\in\{u,v\}\) is exactly the diagonal anchored
pair-square \(d(x)^{-1}\sum_ud(x,u)^2\), already controlled by the raw
catalogue theorem.  The only new scalar input is

\[
 \boxed{
 \Theta(x)={1\over d(x)L_0}
 \sum_{u<v,\ u,v\ne x}d(u,v)d(x,u,v)=o(1).}
 \tag{0.6}

This is a weighted three-resource overlap, strictly lower-order than
the five-resource kernel arising from direct variance.  If (0.6) can
be proved under the current tilted law in weighted average, uniform
legal sampling supplies the common contraction for all but a
coefficient-safe quarantine.

No proof of (0.6) for the physical residual catalogue is given here.
The advance is the exact reduction from neighborhood variance to the
one-sided third-order kernel (0.6).

## 1. Exact inclusion--exclusion

For a resource \(v\), let

\[
 E_v=\{e\in E({\cal H}):v\in e\}.
 \tag{1.1}
\]

Then

\[
 N(f)=\left|\bigcup_{v\in f}E_v\right|.
 \tag{1.2}
\]

The first two Bonferroni inequalities give

\[
 \sum_{v\in f}|E_v|
 -\sum_{\{u,v\}\subseteq f}|E_u\cap E_v|
 \le N(f)\le
 \sum_{v\in f}|E_v|.
 \tag{1.3}
\]

Since \(|E_v|=d(v)\) and \(|E_u\cap E_v|=d(u,v)\), this is (0.3).
No assumption on uniformity is used.

If every catalogue edge has a fixed number \(k_i\) of resources from
stratum \(V_i\), and

\[
 d(v)=(1+O(\epsilon))D_i\qquad(v\in V_i),
 \tag{1.4}
\]

then

\[
 L(f)=(1+O(\epsilon))L_0,qquad
 L_0=\sum_i k_iD_i,
 \tag{1.5}
\]

uniformly in \(f\).  Thus all variation not already paid by the degree
corridor is one-sided and bounded by \(B(f)\).

## 2. Mean control is enough

### Theorem 2.1 (Bonferroni quarantine)

Let \(\nu\) be any probability law on a candidate-edge fibre
\({\cal F}\).  Suppose

\[
 |L(f)-L_0|\le\epsilon L_0
 \quad(f\in{\cal F}),
 \tag{2.1}
\]

and

\[
 \mathbb E_{f\sim\nu}B(f)\le\delta L_0.
 \tag{2.2}
\]

For every \(0<\eta<1\), outside a set of \(\nu\)-mass at most
\(\delta/\eta\),

\[
 \boxed{
 N(f)=L_0\bigl(1+O(\epsilon+\eta)\bigr).}
 \tag{2.3}
\]

In particular, taking \(\eta=\sqrt\delta\), the exceptional mass is at
most \(\sqrt\delta\) and the relative neighborhood error is
\(O(\epsilon+\sqrt\delta)\).

#### Proof

Markov's inequality applied to (2.2) gives

\[
 \nu\{f:B(f)>\eta L_0\}\le\delta/\eta.
 \tag{2.4}
\]

For every remaining \(f\), insert (2.1) and
\(B(f)\le\eta L_0\) into (0.3). \(\square\)

This is precisely the type of deletion already allowed by dynamic
quarantine: if the weighted sum of the \(\delta\)'s over fibres and
times is \(o(1)\), the discarded physical accounting weight is
\(o(W)\).

## 3. Exact anchored mean

Fix a resource \(x\), and sample \(f\) uniformly from

\[
 E_x=\{f:x\in f\}.
 \tag{3.1}
\]

For a resource pair \(A=\{u,v\}\),

\[
 \Pr(A\subseteq f)={d(x,u,v)\over d(x)},
 \tag{3.2}
\]

where repeated elements are removed from the argument of \(d\).  Hence

\[
\begin{aligned}
 \mathbb E_{f\in E_x}B(f)
 &=\sum_{\{u,v\}}d(u,v)\Pr(\{u,v\}\subseteq f)\\
 &={1\over d(x)}
   \sum_{\{u,v\}}d(u,v)d(x,u,v).
\end{aligned}
 \tag{3.3}
\]

This proves (0.5).  Splitting according to whether the pair contains
\(x\) gives

\[
 \boxed{
 \mathbb E_{f\in E_x}B(f)
 ={1\over d(x)}\sum_{u\ne x}d(x,u)^2
 +{1\over d(x)}
  \sum_{u<v,\ u,v\ne x}d(u,v)d(x,u,v).}
 \tag{3.4}
\]

The first term is the diagonal pair-square row.  In a regular catalogue
with normalized kernel \(K(x,u)=d(x,u)/D\), it is

\[
 D\sum_uK(x,u)^2,
 \tag{3.5}
\]

which is \(O(D/m)\) under the audited raw pair-square bound.  Relative
to \(L_0\asymp KD\), this part is already negligible.

The second term in (3.4) is (0.6).  It is not the raw triangle

\[
 \sum_{u,v}K(x,u)K(u,v)K(v,x).
 \tag{3.6}
\]

Indeed, (3.4) contains the actual conditional triple codegree
\(d(x,u,v)\).  A sufficient bridge would be the conditional
decorrelation inequality

\[
 {d(x,u,v)\over d(x)}
 \le(1+o(1))
 {d(x,u)d(x,v)\over d(x)^2}
 +r_x(u,v),
 \tag{3.7}
\]

with

\[
 {1\over L_0}\sum_{u<v}d(u,v)r_x(u,v)=o(1).
 \tag{3.8}
\]

Under (3.7)--(3.8), the nonanchor part of (3.4) is bounded by the raw
triangle form plus \(o(L_0)\).  Dense down-set two-bit inequalities are
of exactly the sign required by (3.7), but identifying physical
resource inclusion with those switch bits under the outer tilted law
is still required.

There is a quantitative local form of this observation.

### Proposition 3.1 (dense-downset conditional decorrelation)

Let \(X\) be uniform on a downset
\(A\subseteq\{0,1\}^f\) of density \(2^{-b}\).  Put

\[
 p_i=\Pr(X_i=1),\qquad p_{ij}=\Pr(X_i=X_j=1),
 \tag{3.9}
\]

and

\[
 R=\sqrt{(\log2)fb/2}.
 \tag{3.10}
\]

Then

\[
 p_{ij}\le{1\over4},qquad
 \sum_i(1/2-p_i)\le R.
 \tag{3.11}
\]

Let \(w_{ij}\ge0\) be pair weights satisfying

\[
 w_{ij}\le w_{\max},qquad
 \sum_{i<j}w_{ij}\ge c f^2w_{\max}
 \tag{3.12}
\]

for a fixed \(c>0\).  If \(b=o(f)\), then outside pairs of total
\(w\)-weight

\[
 O_c((b/f)^{1/4})\sum_{i<j}w_{ij},
 \tag{3.13}
\]

one has

\[
 \boxed{
 p_{ij}\le
 \bigl(1+O((b/f)^{1/4})\bigr)p_ip_j.}
 \tag{3.14}
\]

#### Proof

The two inequalities in (3.11) are the downset Harris inequality and
the entropy-deficit bound, respectively.  Put

\[
 \tau=\sqrt{R/f}=O((b/f)^{1/4})
 \tag{3.15}
\]

and call coordinate \(i\) bad when \(1/2-p_i>\tau\).  By (3.11), the
number of bad coordinates is at most \(R/\tau\).  The total weight of
pairs incident with one of them is at most

\[
 f(R/\tau)w_{\max}
 \le {R\over c\tau f}\sum_{i<j}w_{ij}
 =O_c(\tau)\sum_{i<j}w_{ij}.
 \tag{3.16}
\]

If neither coordinate is bad, then

\[
 p_ip_j\ge(1/2-\tau)^2,
 \tag{3.17}
\]

while \(p_{ij}\le1/4\).  Therefore

\[
 {p_{ij}\over p_ip_j}
 \le{1/4\over(1/2-\tau)^2}=1+O(\tau).
 \tag{3.18}
\]

Equations (3.15)--(3.18) prove the proposition. \(\square\)

Thus the within-slice part of (3.7) follows from density plus diffuse
pair weights.  The remaining physical issue is to prove that the
weighted triple kernel in (3.4), after aggregating outer schedule
slices and physical labels, has the diffuseness (3.12).  The affine
two-moment cross-slice theorem is aimed exactly at this last step.

## 4. What a direct variance calculation demands

The literal second moment of the Bonferroni correction is

\[
 \boxed{
 \mathbb E_{f\in E_x}B(f)^2
 ={1\over d(x)}
 \sum_{A,B\in\binom V2}
 d(A)d(B)d(x\cup A\cup B).}
 \tag{4.1}
\]

This follows by expanding

\[
 B(f)^2=\sum_{A,B\subseteq f,\ |A|=|B|=2}d(A)d(B)
 \tag{4.2}
\]

and averaging the indicator of \(x\cup A\cup B\subseteq f\).

The terms in (4.1) split as follows:

* \(A=B\): weighted triple-codegree terms;
* \(|A\cap B|=1\): weighted four-resource codegrees;
* \(A\cap B=\varnothing\): weighted five-resource codegrees.

Therefore raw degree, pair-codegree, and triangle data do not by
themselves evaluate (4.1).  A direct variance proof needs a new
four/five-resource decorrelation statement.

There is also a purely linear-algebraic reason the existing bow-tie
second moment does not automatically control neighborhood variance.
For the conflict incidence matrix

\[
 M_{f,e}=\mathbf1_{\{f\cap e\ne\varnothing\}},
 \tag{4.3}
\]

the shared-killer/bow-tie identity controls the squared column sums

\[
 \|M^T\mathbf1\|_2^2,
 \tag{4.4}
\]

whereas neighborhood variance is the centered squared row-sum norm

\[
 \|M\mathbf1-\overline N\mathbf1\|_2^2.
 \tag{4.5}
\]

There is no inequality from (4.4) to (4.5) for a general binary
matrix.  For example, matrices can have every column sum equal to one
while all ones lie in one row, or while they form a permutation matrix;
the column statistic is identical and the row variance is radically
different.  Catalogue geometry must supply the missing correlation.

## 5. Consequence for common contraction

Consider a microstep which samples a killer edge uniformly from a legal
residual family of size \(M\).  A candidate decoration \(f\) survives
the microstep with probability

\[
 1-{N(f)\over M}.
 \tag{5.1}
\]

Under Theorem 2.1, all nonquarantined candidates in the fibre therefore
have the common survival factor

\[
 1-{L_0\over M}
 +O\left((\epsilon+\sqrt\delta){L_0\over M}\right).
 \tag{5.2}
\]

The same statement exponentiates over a sparse independent bite, with
the usual quadratic collision error.  Thus a weighted aggregate form
of (0.6), together with the already proved degree corridor and diagonal
pair-square bound, would construct the common scalar compensator
directly from uniform legal sampling.  It would avoid solving a signed
LP for degree means.

The exact remaining input for this route is therefore not the full
variance of \(N(f)\), but the survival-conditioned third-order bound

\[
 \boxed{
 \sum_x\operatorname {wt}(x)
 {1\over d(x)L_0(x)}
 \sum_{u<v,\ u,v\ne x}d(u,v)d(x,u,v)=o(1),}
 \tag{5.3}
\]

with the weights interpreted under the current priority-tilted law.
Raw triangle plus a physical version of the conditional decorrelation
(3.7) would prove (5.3).  Without that bridge, neither the raw
pair-square nor the raw triangle alone proves common contraction.
