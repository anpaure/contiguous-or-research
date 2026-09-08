# The survival-conditioned pair-square recurrence

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

There is a closed one-bite recurrence for the dynamic-quarantine
pair-square profile.  It identifies exactly what the new
\(\eta=m^{-4}\) swap-cube reservoir and the raw two-link branching factor
\(\beta=m^{-1/2+o(1)}\) would have to prove.

The recurrence must be written under the law conditioned on both anchor
resources surviving the bite.  Under that law, if

1. one-resource degrees contract by
   \(a_t=q_t^{k-1}\);
2. two-resource links have conditional mean contraction
   \(b_t=q_t^{k-2}\); and
3. the survival-conditioned link variance is at most
   \(O(\alpha_t\beta)\) times the current pair-square block,

then, in survival-conditioned weighted expectation,

\[
 \boxed{
 \mathbb E^\circ S_{t+1,h}(x)
 \le q_t^{-2}
 \bigl(1+O(e_t+\alpha_t\beta)\bigr)S_{t,h}(x)
 +q_t^{-2}E_{t,h}(x).}
 \tag{0.1}
\]

Here \(e_t\) contains the scalar mean/degree error and the harmless
quarantine erosion, while \(E_{t,h}\) is an explicitly normalized
exceptional link-variance term.

Writing

\[
 z_t=\prod_{j<t}q_j,
 \tag{0.2}
\]

equation (0.1) iterates to

\[
 \mathbb E^\circ S_{t,h}(x)
 \le(1+o(1))z_t^{-2}B_h
 \tag{0.3}
\]

through \(z_t=1/\log m\), provided

\[
 \sum_t e_t=o(1),\qquad
 \beta\sum_t\alpha_t=o(1),\qquad
 \sum_t{z_t^2E_{t,h}(x)\over B_h}=o(1).
 \tag{0.4}
\]

The numerical input is sufficient:

\[
 \beta\sum_t\alpha_t
 =m^{-1/2+o(1)}O(\log\log m)=o(1),
 \tag{0.5}
\]

and even \(O(m)\) bites lose only
\(O(m\sqrt\eta)=O(m^{-1})\) to the cube-boundary error.

What is not proved by the two raw inputs is hypothesis 3.  Quarantine
retains almost all of the ambient switch cube, but the owner/priority
history may condition on a very rare face.  A raw event of mass
\(\beta\) can have conditional mass one on such a face.  The down-set
entropy theorem guarantees many unlabelled switch squares inside dense
slices, but the kernel in hypothesis 3 is a labelled second moment and
contains unsummed cross-slice terms.

Thus the exact new theorem still needed is a
**survival-conditioned physical square-label dispersal inequality**.
The raw \(\beta\)-census is not that theorem.  No coefficient-one
conclusion is claimed.

## 1. Direct hits must be conditioned away

Let \(X_U\) be the tentative variable at tag \(U\): it is inactive with
probability \(1-\alpha_t\), and otherwise samples
\(E\sim\nu_{t,U}\).  For two currently unused resources \(x,y\), put

\[
 q_{t,U}(x,y)
 =
 \Pr_{E\sim\nu_{t,U}}
 \bigl(E\cap\{x,y\}\ne\varnothing\bigr).
 \tag{1.1}
\]

Let \(\mathcal A_{xy}\) be the event that no tentative chunk directly
uses \(x\) or \(y\).  Since this event factors over tags, the variables
remain independent after conditioning, with exact laws

\[
 \Pr(X_U=\varnothing\mid\mathcal A_{xy})
 =
 {1-\alpha_t\over1-\alpha_tq_{t,U}(x,y)}
 \tag{1.2}
\]

and

\[
 \Pr(X_U=E\mid\mathcal A_{xy})
 =
 {\alpha_t\nu_{t,U}(E)
  \mathbf1_{\{E\cap\{x,y\}=\varnothing\}}
  \over
  1-\alpha_tq_{t,U}(x,y)}.
 \tag{1.3}
\]

The denominators in (1.2)--(1.3) lie in
\([1-\alpha_t,1]\), so they cost only \(1+O(\alpha_t)\) in one parallel
bite.

This conditioning is essential.  If a tentative chunk contains \(x\),
the entire \(x\)-fibre is intentionally consumed and its fractional loss
equals one.  Summing those diagonal losses through the run gives
\(\Theta(KT)=\Theta(W\sqrt m)\), not \(o(W)\).  Consumed fibres leave the
residual problem and must not enter its variance kernel.

## 2. Pair links and their exact ideal contractions

In the current decorated catalogue write

\[
 D_t(x)=\#\{P:x\in P\},\qquad
 C_t(x,y)=\#\{P:x,y\in P\},
 \tag{2.1}
\]

with the same definitions for integer priority weights.  For \(x\) in
rank \(r\), set

\[
 S_{t,h}(x)
 =
 \sum_{\substack{|y|=r+h\\y\ {\rm currently\ tracked}}}
 {C_t(x,y)^2\over D_t(x)D_t(y)}.
 \tag{2.2}
\]

If one bite leaves each resource independently available with factor
\(q_t\), then, conditional on the anchors surviving, the ideal scales of
a \(k\)-resource decoration are

\[
 a_t=q_t^{k-1}
 \quad\hbox{for }D_t(x),
 \qquad
 b_t=q_t^{k-2}
 \quad\hbox{for }C_t(x,y).
 \tag{2.3}
\]

Their quotient is the whole reason for the desired inflation:

\[
 {b_t^2\over a_t^2}=q_t^{-2}.
 \tag{2.4}
\]

Codegree monotonicity alone does not recover (2.3).  It would replace
\(b_t\) by one and give the useless factor \(a_t^{-2}\).

## 3. The exact fresh-branching hypothesis

Fix a rank block \(h\).  The following is the minimal second-moment
statement used in the recurrence.

### Definition 3.1 (survival-conditioned fresh branching)

At bite \(t\), write \({\rm FBL}_t(h)\) for the conjunction of:

\[
 D_{t+1}(v)
 \ge (1-e_t)a_tD_t(v)
 \tag{3.1}
\]

for every retained resource \(v\) in the two relevant strata;

\[
 \left|
 \mathbb E\!\left[
 C_{t+1}(x,y)\mid\mathcal F_t,\mathcal A_{xy}
 \right]
 -b_tC_t(x,y)
 \right|
 \le e_tb_tC_t(x,y);
 \tag{3.2}
\]

and

\[
\begin{aligned}
 &\sum_{|y|=r+h}
 {\operatorname {Var}\!\left(
 C_{t+1}(x,y)\mid\mathcal F_t,\mathcal A_{xy}
 \right)
 \over D_t(x)D_t(y)}
 \\
 &\hspace{18mm}\le
 C\alpha_t\beta\,b_t^2S_{t,h}(x)
 +b_t^2E_{t,h}(x).
\end{aligned}
 \tag{3.3}
\]

All direct-use diagonals are absent because of \(\mathcal A_{xy}\).
Equation (3.3) is the residual two-link/four-walk statement.  It is a
weighted assertion under the current tilted laws, not a raw catalogue
count.

## 4. One-bite theorem

### Theorem 4.1 (conditioned pair-square recurrence)

Assume \({\rm FBL}_t(h)\), and discard the fibres failing (3.1) to their
separate exceptional ledger.  Then, conditional on the two anchors
remaining unused,

\[
\begin{aligned}
 \mathbb E S_{t+1,h}(x)
 &\le
 q_t^{-2}
 \bigl(1+C(e_t+\alpha_t\beta)\bigr)S_{t,h}(x)
 \\
 &\qquad
 +q_t^{-2}(1+Ce_t)E_{t,h}(x).
\end{aligned}
 \tag{4.1}
\]

#### Proof

By (3.1),

\[
 S_{t+1,h}(x)
 \le
 {(1-e_t)^{-2}a_t^{-2}}
 \sum_{|y|=r+h}
 {C_{t+1}(x,y)^2\over D_t(x)D_t(y)}.
 \tag{4.2}
\]

For each \(y\), conditional second-moment decomposition gives

\[
 \mathbb E C_{t+1}(x,y)^2
 =
 \bigl(\mathbb E C_{t+1}(x,y)\bigr)^2
 +
 \operatorname {Var}C_{t+1}(x,y).
 \tag{4.3}
\]

Equation (3.2) bounds the first term by

\[
 (1+Ce_t)b_t^2C_t(x,y)^2.
 \tag{4.4}
\]

For the pair-square conditioned only on \(x\) surviving, a consumed
\(y\) contributes zero.  Its surviving contribution is its
\(\mathcal A_{xy}\)-conditional expectation multiplied by a probability
at most one.  Thus summing the separate two-anchor conditional bounds is
a valid upper bound.

Sum (4.3), use (3.2)--(3.3), substitute into (4.2), and use
\(b_t^2/a_t^2=q_t^{-2}\).  Since
\((1-e_t)^{-2}=1+O(e_t)\), this is (4.1).
\(\square\)

The same proof works blockwise for the mixed exposed/claimed kernels in
the exact priority influence majorant.

## 5. Iteration through density \(1/\log m\)

Let

\[
 B_0=Cm^{-2},
 \qquad
 B_h=C(|h|+1)^2|h|!(C/m)^{|h|}
 \quad(h\ne0)
 \tag{5.1}
\]

be the raw block bounds, and define

\[
 R_{t,h}(x)={z_t^2S_{t,h}(x)\over B_h}.
 \tag{5.2}
\]

Because \(z_{t+1}=q_tz_t\), Theorem 4.1 gives

\[
 \mathbb E R_{t+1,h}(x)
 \le
 \bigl(1+C(e_t+\alpha_t\beta)\bigr)R_{t,h}(x)
 +(1+Ce_t){z_t^2E_{t,h}(x)\over B_h}.
 \tag{5.3}
\]

Iterating (5.3) and using \(1+u\le e^u\) proves:

### Corollary 5.1 (closed conditional iteration)

If (0.4) holds uniformly before \(z_t=1/\log m\), then

\[
 \boxed{
 \mathbb E^\circ S_{t,h}(x)
 \le(1+o(1))z_t^{-2}B_h.}
 \tag{5.4}
\]

At the stated scales,

\[
 \beta\sum_t\alpha_t
 =
 m^{-1/2+o(1)}O(\log\log m)=o(1).
 \tag{5.5}
\]

If a cube-boundary error \(O(\sqrt\eta)\) is paid in each of at most
\(O(m)\) macroscopic bites, then

\[
 \sum_tO(\sqrt\eta)
 =O(m\cdot m^{-2})=O(m^{-1})=o(1).
 \tag{5.6}
\]

Thus every numerical error in the proposed composition is summable.

Combining (5.4) with the audited cover/remainder Schur split gives

\[
 \mathfrak T_t(x)
 \le
 C\left[
 {1\over z_t^2m}
 +{g\over z_t^2m^{3/2}}
 +{1\over z_t^3m^{3/2}}
 \right].
 \tag{5.7}
\]

At \(z_t=1/\log m\), this is \(m^{-1+o(1)}\).  Multiplication by the
\(\Theta(W\sqrt m)\) physical target count therefore gives \(o(W)\);
the improved cover/remainder split is strong enough for the global
ledger once (5.4) is available.

## 6. What the cube and raw \(\beta\) do prove

Four-antichain quarantine has raw relative degree

\[
 \xi_4=m^{-5+o(1)}.
 \tag{6.1}
\]

Taking the exceptional-fibre threshold

\[
 \eta=m^{-4}
 \tag{6.2}
\]

costs only \(o(W)\).  If \(Z\) is the deleted part of a
\(d=\Theta(m)\) adjacent-switch cube, directed boundary counting gives

\[
 \#\left\{
 x\notin Z:
 |N(x)\cap Z|>\sqrt\eta\,d
 \right\}
 \le\sqrt\eta\,2^d.
 \tag{6.3}
\]

Thus all but \(m^{-2}\) of the ambient schedules retain
\((1-m^{-2})d\) swap neighbours.

The width-three two-link shape expansion has raw branching ratio

\[
 \beta={g\over m}(C\log m)^6=m^{-1/2+o(1)}.
 \tag{6.4}
\]

These statements prove the raw inputs and explain the factors in
(5.5)--(5.6).  They do not prove (3.2)--(3.3) under the current
survival-conditioned law.

## 7. Why the raw composition fails

Let \(A_t\) be the current owner/priority-feasible schedules before
quarantine.  Its raw density inside a switch cube can be exponentially
small.  If \(B\) is any raw two-link event of probability at most
\(\beta\), then the only unconditional estimate is

\[
 \Pr(B\mid A_t)
 \le\min\left\{1,{\beta\over\Pr(A_t)}\right\}.
 \tag{7.1}
\]

At resource density \(z\), a fixed \(g\)-resource schedule naturally has
raw survival mass comparable to \(z^g\), and

\[
 (1/\log m)^g\ll m^{-4}\ll\beta.
 \tag{7.2}
\]

Therefore \(A_t\) may, from the two raw estimates alone, lie entirely in
the boundary-atypical set or in the two-link event.

The same issue remains after using the valid down-set entropy theorem.
For a feasible slice \(\omega\), let \(N_\omega(x,y)\) count its switch
squares bearing physical target-pair label \((x,y)\).  Entropy controls

\[
 \sum_{\omega,x,y}N_\omega(x,y),
 \tag{7.3}
\]

but (3.3) contains

\[
 \sum_{x,y}
 {\left(\sum_\omega N_\omega(x,y)\right)^2
  \over D_t(x)D_t(y)}.
 \tag{7.4}
\]

The unsummed cross-slice part is

\[
 \sum_{x,y}\sum_{\omega\ne\omega'}
 {N_\omega(x,y)N_{\omega'}(x,y)
  \over D_t(x)D_t(y)}.
 \tag{7.5}
\]

Neither ambient cube boundary nor aggregate down-set square entropy
bounds (7.5).

There is also a physical-dimension caveat.  A full carrier has
\(\Theta(m)\) commuting arrival switches, but a length-\(g\) chunk has
only \(\Theta(g)\) explicitly verified switches which change its
protected physical claims.  Any coding estimate using
\(K/d^2=o(1)\) must first prove a physically effective
\(d=\Theta(m)\); with \(d=\Theta(g)\),

\[
 {K\over d^2}
 =\Theta\!\left({\sqrt m\over g}\right),
 \tag{7.6}
\]

which is not known to vanish.

## 8. Exact remaining statement

The raw four-walk lane is now exhausted.  The sufficient and
coefficient-scale exact next statement is (3.3), with its mean companion
(3.2), under the conditioned law (1.3).  Equivalently, one may prove the
physical square-label dispersal bound

\[
 \boxed{
 \sum_{x,y}\sum_{\omega\ne\omega'}
 {N_\omega(x,y)N_{\omega'}(x,y)
  \over D_t(x)D_t(y)}
 \le
 C\alpha_t\beta\,
 \mathcal S_t
 +o_t(1),}
 \tag{8.1}
\]

where \(\mathcal S_t\) is the current block pair-square energy and the
normalized errors sum as in (0.4).

Proving (8.1) would make Theorem 4.1 unconditional for the actual
catalogue and close hereditary propagation through \(1/\log m\).
Without (8.1), the ambient \((1-\eta)\)-cube retention and raw
\(\beta\)-branching estimates do not compose.
