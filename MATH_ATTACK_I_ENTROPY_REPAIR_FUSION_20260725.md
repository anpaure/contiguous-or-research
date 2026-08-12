# Signed-subcube entropy repair inside a principal MTF trajectory

Date: 2026-07-25

## 0. Verdict

This route does **not** prove the contiguous-OR width conjecture. It does
settle what entropy repair can and cannot do for the presently available
principal-MTF architectures.

1. A canonical signed-face repair packet can be inserted immediately
   before a full reverse MTF initialization. The initialization erases the
   incoming state, so the packet and the principal trajectory coexist in
   one literal word with no second reset charge. Its length remains
   additive. This is state-compatible seam fusion, not free overlap with
   the \(W\) principal positions.
2. The exact entropy dual permits cumulative defect much larger than
   \(W\) when actual holes reuse a growing complementary trace through
   many depths. An exact sufficient trace-condensation theorem is proved
   below.
3. The entropy functional is not the cost of arbitrary in-place MTF
   fusion. One endpoint can expose a chain through \(H\) ranks even though
   the signed-face functional of that chain is exactly \(2H\). Endpoint
   chains and signed-face cylinders are different geometries.
4. This caveat does not save the stationary fixed-pair principal
   trajectory. Its canonical lower holes have positive density at every
   rank in a compact Gaussian interval. After allowing arbitrary
   seam-crossing intervals, \(R\) nonprincipal positions, and \(E\)
   surrendered principal endpoint--rank flags, the residual entropy obeys

   \[
   \Psi_{\rm res}
   \ge
   (1+\log(2K))
   \left[
   (\bar\delta_{a,b}-o(1))W-R-\frac EK
   \right]_+ .
   \tag{0.1}
   \]

   Here \(K\asymp\sqrt m\) and \(\bar\delta_{a,b}>0\) is explicit below.
   Preserving all but \(o(W)\) principal endpoints and using only \(o(W)\)
   other positions therefore leaves Poisson cost
   \(\Omega(W\log m)\). Even an unrestricted literal completion has
   length \(\Omega(W)\).

The exact deterministic seam-repair gate is
\(\mathfrak P_H+D_{\rm det}=o(W)\). The route-specific entropy condition
\(\mathrm{EMTF}_A\) in Section 2 is a sufficient, but not necessary,
surrogate because Poissonization can carry a logarithmic tax. A concrete
structural lemma which would prove it is the **actual
principal-trajectory trace-condensation lemma** in Section 8: for one
exact middle-owner chronology and one common adaptive-MTF lift, its actual
holes, after every incidental interval is counted, must have signed-face
cluster cost \(o(W)\). Separate factors at separate depths, fractional
ownership, and abstract hole families do not supply it.

All logarithms are natural. No finite search or occupancy heuristic is
used.

---

## 1. Exact signed-face entropy dual

Put

\[
n=2m,\qquad W=\binom{2m}{m},\qquad
H=\lceil A\sqrt m\rceil
\]

for fixed \(A>0\). Let \(\mathcal H\) be a family of nonempty proper
targets in the central band; its members may lie on both sides of the
middle layer.

For disjoint anchors \(P,N\subseteq[n]\), with
\(P\cup N\ne\varnothing\), put

\[
U=[n]\setminus(P\cup N),\qquad s=|U|,
\]

and define the proper opposite signed face

\[
C(P,N)
=\{P\cup T:T\subseteq U\}
 \cup
 \{N\cup T:T\subseteq U\}.
\tag{1.1}
\]

Its canonical two-branch OR block has length

\[
\gamma_C
=2\nu(s)+\mathbf 1_{P\ne\varnothing}
             +\mathbf 1_{N\ne\varnothing}.
\tag{1.2}
\]

Here \(\nu(0)=0\).

This is the exact length of the stated block; it is not asserted to be the
minimum length of an arbitrary word covering the same face. The
empty-anchor full cube is excluded. At \(s=0\), a face with two nonempty
anchors has cost two. The one-anchor-empty face
\(\{\varnothing,[n]\}\) has cost one but meets no nonempty proper target.

Let \(\mathsf A_{S,C}=\mathbf1_{S\in C}\). Define

\[
\Psi(\mathcal H)
=\inf_{\lambda\ge0}
\left[
\sum_C\gamma_C\lambda_C
+2\sum_{S\in\mathcal H}e^{-(\mathsf A\lambda)_S}
\right].
\tag{1.3}
\]

### Theorem 1.1 — exact Fenchel dual

For every finite \(\mathcal H\),

\[
\boxed{
\Psi(\mathcal H)
=
\max_{\substack{0\le y_S\le2\\
                 \mathsf A^Ty\le\gamma}}
\sum_{S\in\mathcal H}
y_S\left(1+\log\frac2{y_S}\right).}
\tag{1.4}
\]

The summand at \(y_S=0\) is interpreted by continuity.

#### Proof

For \(x\ge0\), direct differentiation gives

\[
2e^{-x}
=\max_{0\le y\le2}
\left[y\left(1+\log\frac2y\right)-xy\right],
\tag{1.5}
\]

with maximizer \(y=2e^{-x}\). Substitute (1.5) in (1.3).
Finite-dimensional Fenchel duality interchanges the minimum in
\(\lambda\ge0\) and the maximum in \(0\le y\le2\). The coefficient of
\(\lambda_C\) becomes

\[
\gamma_C-\sum_{S\in C}y_S.
\]

The infimum over \(\lambda_C\ge0\) is zero when this coefficient is
nonnegative and is \(-\infty\) otherwise. The surviving constraints are
exactly \(\mathsf A^Ty\le\gamma\), proving (1.4). \(\square\)

### Rank-profile consequences

Let

\[
\mathcal H=\bigsqcup_{q\in Q}\mathcal H_q,\qquad
\mathcal H_q\subseteq\binom{[n]}{r_q},\qquad
M_q=|\mathcal H_q|,
\]

where the ranks \(r_q\) are distinct. If a proper face has free dimension
\(s\ge1\), then at one fixed rank

\[
|C(P,N)\cap\tbinom{[n]}r|
\le
2\binom{s}{\lfloor s/2\rfloor}
\le2\nu(s)\le\gamma_C.
\tag{1.6}
\]

The \(s=0\) cases satisfy the same inequality directly. Therefore, for
nonnegative \(\alpha_q\) with \(\sum_q\alpha_q\le1\), the assignment

\[
y_S=\alpha_q\qquad(S\in\mathcal H_q)
\]

is feasible in (1.4). Hence

\[
\boxed{
\Psi(\mathcal H)
\ge
\sum_{q\in Q}M_q\alpha_q
\left(1+\log\frac2{\alpha_q}\right).}
\tag{1.7}
\]

In particular, if \(K=|Q|\), then

\[
\boxed{\Psi(\mathcal H)\ge(1+\log2)M_q}
\tag{1.8}
\]

and

\[
\boxed{
\Psi(\mathcal H)
\ge
\frac{1+\log(2K)}K\sum_{q\in Q}M_q.}
\tag{1.9}
\]

Thus \(\Psi=o(W)\) forces \(M_q=o(W)\) at every rank. Across a Gaussian
window \(K=\Theta(\sqrt m)\), it only forces

\[
\sum_{q\in Q}M_q
=o\!\left(\frac{W\sqrt m}{\log m}\right),
\tag{1.10}
\]

so a nonsummable cumulative defect is not excluded.

For later comparison define

\[
D_{\rm frac}
=\min_{\substack{x_C,z_S\ge0\\
                  \mathsf Ax+z\ge\mathbf1}}
\left(\sum_C\gamma_Cx_C+2\sum_Sz_S\right).
\tag{1.11}
\]

Linear-programming duality gives

\[
D_{\rm frac}
=\max_{\substack{0\le y\le2\\
                  \mathsf A^Ty\le\gamma}}\sum_Sy_S.
\tag{1.12}
\]

Taking \(y_S=1/K\) on \(K\) ranks yields

\[
\boxed{D_{\rm frac}\ge K^{-1}\sum_qM_q.}
\tag{1.13}
\]

Let \(D_{\rm det}\) be the minimum cost obtained by taking an integral
collection of canonical face blocks and paying two entries for every
uncovered target through its charged literal column. Then
\(D_{\rm det}\ge D_{\rm frac}\). This is a symmetric canonical-repair
value, not the minimum length of an unrestricted word on the targets.

---

## 2. Exact state-compatible seam fusion

An ordered-partition MTF state is written

\[
\Pi=(B_1,\ldots,B_b),
\]

where the \(B_i\) are nonempty, pairwise disjoint, and partition \([n]\).
The full reverse initialization is

\[
B_b,B_{b-1},\ldots,B_1.
\tag{2.1}
\]

After (2.1), the MTF state is \(\Pi\), independently of the incoming
state: the last occurrences of the blocks are in reverse chronological
order, and their union deletes every older residual block.

Let \(\mathcal A\) be one physical principal adaptive-MTF word covering all
middle sets at \(W\) designated state endpoints and exposing its certified
central flags. Write

\[
|\mathcal A|=W+\mathfrak P_H,
\tag{2.2}
\]

where \(\mathfrak P_H\) is its actual portal/reset excess. With \(C\)
independently initialized canonical radius-\(H\) components,

\[
\mathfrak P_H=(2H+1)C.
\tag{2.3}
\]

Let \(\mathcal H(\mathcal A)\) denote the targets in the chosen central
band which are not represented anywhere in this one physical word. Thus
incidental and seam-crossing witnesses are removed before the repair
functional is formed.

### Theorem 2.1 — entropy-compressed MTF seam insertion

There is one literal central-band word of length

\[
\boxed{
L_{\rm band}
\le W+\mathfrak P_H+D_{\rm det}(\mathcal H)
\le W+\mathfrak P_H+\lceil\Psi(\mathcal H)\rceil.}
\tag{2.4}
\]

The repair packet can be placed before the first full reverse
initialization of \(\mathcal A\); it need not be appended after the
principal trajectory.

#### Proof

Fix \(\varepsilon>0\) and choose intensities \(\lambda_C\) whose objective
in (1.3) is at most \(\Psi+\varepsilon\). Independently select the
canonical block for \(C\) with probability \(1-e^{-\lambda_C}\). A hole
\(S\) is left uncovered with probability

\[
\prod_{C\ni S}e^{-\lambda_C}
=e^{-(\mathsf A\lambda)_S}.
\]

After the selected blocks, repair every uncovered target by its charged
two-letter literal column. The expected length is at most

\[
\sum_C\gamma_C(1-e^{-\lambda_C})
+2\sum_Se^{-(\mathsf A\lambda)_S}
\le\Psi+\varepsilon.
\tag{2.5}
\]

For every \(\varepsilon>0\), some deterministic packet therefore covers
\(\mathcal H\) with length at most \(\Psi+\varepsilon\). Since
\(D_{\rm det}\) is an attained integer minimum, letting
\(\varepsilon\downarrow0\) gives \(D_{\rm det}\le\Psi\), and hence
\(D_{\rm det}\le\lceil\Psi\rceil\). Choose an optimal packet
\(\mathcal Q\).

Place \(\mathcal Q\) immediately before (2.1). Every repair witness is
internal to \(\mathcal Q\). Whatever ordered partition the packet leaves
behind, (2.1) restores \(\Pi\) exactly. The old principal word is an
unchanged contiguous suffix, so all its states and witnesses survive. No
additional reset is needed, and the total length is
\(|\mathcal A|+|\mathcal Q|\). \(\square\)

### Corollary 2.2 — route-specific sufficient condition

For every fixed \(A\), the condition

\[
\boxed{
\mathfrak P_H+\Psi(\mathcal H(\mathcal A))=o(W)}
\tag{\mathrm{EMTF}_A}
\]

gives a central-band word of length \(W+o(W)\). If
\(\mathrm{EMTF}_A\) holds for every fixed \(A\), the audited
symmetric-chain tail word contributes

\[
O\bigl((1+A^2)e^{-A^2+o(1)}W\bigr).
\tag{2.6}
\]

Taking \(m\to\infty\) for fixed \(A\), and then \(A\to\infty\), gives the
coefficient-one OR bound in even dimension; the standard trimmed one-bit
lift gives the other parity.

The theorem proves state compatibility, not \(\mathrm{EMTF}_A\). In
particular, it does not hide a linear repair packet in the \(W\)
productive endpoints.

---

## 3. A rigorous correlated-hole certificate

The next theorem applies to the **actual** holes of any specified
principal word. It remains unproved that a useful principal word satisfies
its hypotheses.

For \(M\ge0\) and \(\gamma>0\), put

\[
\phi(M,\gamma)
=\min_{\lambda\ge0}(\gamma\lambda+2Me^{-\lambda}).
\tag{3.1}
\]

Direct differentiation gives

\[
\phi(M,\gamma)
=
\begin{cases}
2M,&2M\le\gamma,\\[1mm]
\gamma\left(1+\log\dfrac{2M}{\gamma}\right),&2M\ge\gamma.
\end{cases}
\tag{3.2}
\]

### Theorem 3.1 — actual trace-corridor compression

Suppose

\[
\mathcal H
=\mathcal H_0\mathbin{\dot\cup}
 \mathcal G_1\mathbin{\dot\cup}\cdots
 \mathbin{\dot\cup}\mathcal G_J,\qquad
\mathcal G_i\subseteq C_i,
\tag{3.3}
\]

where \(C_i\) is a proper signed face of cost \(\gamma_i\). Then

\[
\boxed{
\Psi(\mathcal H)
\le2|\mathcal H_0|+
\sum_{i=1}^J\phi(|\mathcal G_i|,\gamma_i).}
\tag{3.4}
\]

If each \(\mathcal G_i\) occupies at most \(R_*\) distinct ranks, then

\[
\boxed{
\Psi(\mathcal H)
\le2|\mathcal H_0|+
(1+\log(2R_*))\sum_{i=1}^J\gamma_i.}
\tag{3.5}
\]

#### Proof

Use only the columns \(C_i\), with each intensity chosen to attain (3.1),
and pay \(\mathcal H_0\) literally. This gives (3.4). By (1.6), one face
contains at most \(\gamma_i\) holes at one rank, so

\[
|\mathcal G_i|\le R_*\gamma_i.
\]

Equation (3.2), including its \(2M\le\gamma\) branch, gives

\[
\phi(|\mathcal G_i|,\gamma_i)
\le\gamma_i(1+\log(2R_*)),
\]

proving (3.5). \(\square\)

Fix a marker set \(D\), \(|D|=d\ge1\). The complementary trace cells

\[
\{S:S\cap D\in\{R,D\setminus R\}\}
\tag{3.6}
\]

are precisely the signed faces \(C(R,D\setminus R)\), of costs

\[
\gamma_R
=2\nu(2m-d)
+\mathbf1_{R\ne\varnothing}
+\mathbf1_{D\setminus R\ne\varnothing}.
\tag{3.7}
\]

The known constant-factor universal-word bound and Stirling's formula give,
uniformly for \(d=o(m)\),

\[
\begin{aligned}
\gamma_R
&=O\!\left(\binom{2m-d}{\lfloor(2m-d)/2\rfloor}\right)\\
&=O\!\left(
2^{-d}\sqrt{\frac{2m}{2m-d}}\,W
\right)
=O(2^{-d}W).
\end{aligned}
\tag{3.8}
\]

Thus, when \(R_*\le2H=O_A(\sqrt m)\),

\[
\boxed{
|\mathcal H_0|=o(W),\qquad
J2^{-d}\log m=o(1)
\quad\Longrightarrow\quad
\Psi(\mathcal H)=o(W).}
\tag{3.9}
\]

This permits genuinely large cumulative defect. In the abstract saturated
one-cell model, take even
\(d=\frac14\log_2m+O(1)\) and a trace \(R\subseteq D\) with
\(|R|=d/2\). At lower depth \(q\le A\sqrt m\), the cell slice has exact
size

\[
2\binom{2m-d}{m-q-d/2}.
\]

The central-binomial product expansion, uniformly for
\(q=O_A(\sqrt m)\) and \(d=o(\sqrt m)\), is

\[
\frac{\binom{2m-d}{m-q-d/2}}W
=(1+o(1))2^{-d}
\sqrt{\frac{2m}{2m-d}}\,
\exp\!\left(-\frac{2q^2}{2m-d}\right).
\]

It is therefore \(\Theta_A(2^{-d})\). Thus every one of
\(\Theta(\sqrt m)\) ranks has \(\Theta_A(2^{-d}W)\) holes, and

\[
M=\Theta_A(Wm^{1/4}),\qquad
\Psi=\Theta_A\!\left(\frac{W\log m}{m^{1/4}}\right)=o(W),
\tag{3.10}
\]

where (1.9) gives the matching lower order. This is only a sharp scale
example; it is not asserted to be the hole family of an exact factor or an
MTF trajectory.

---

## 4. Why \(\Psi\) is not the cost of arbitrary MTF overlap

Choose pairwise disjoint nonempty blocks

\[
|D_0|=m-H,\qquad |D_i|=1\quad(1\le i<H).
\]

Start with

\[
\mathcal B=(D_{H-1},D_{H-2},\ldots,D_1)
\]

and append the single letter \(D_0\). At its right endpoint the suffix
unions are

\[
S_j=D_0\cup D_1\cup\cdots\cup D_j,\qquad 0\le j<H.
\tag{4.1}
\]

They give one new target in every rank \(m-H,\ldots,m-1\), and none was
represented by \(\mathcal B\), because every \(S_j\) contains \(D_0\).
Thus one added endpoint fuses \(H\) new targets.

### Proposition 4.1 — one chain is signed-face incompressible

For every strict inclusion chain \(\Gamma\) of nonempty proper sets,

\[
\boxed{
\Psi(\Gamma)=D_{\rm frac}(\Gamma)
=D_{\rm det}(\Gamma)=2|\Gamma|.}
\tag{4.2}
\]

#### Proof

Fix a proper face \(C(P,N)\) of free dimension \(s\). If both anchors are
nonempty, its two branches are mutually incomparable, so a chain meets at
most one branch and has at most \(s+1\) members there. Since

\[
\gamma_C\ge2\binom{s}{\lfloor s/2\rfloor}+2\ge2s+2,
\]

the intersection has density at most \(1/2\). The \(s=0\) case is direct.

If exactly one anchor is empty and \(s\ge1\), the two branches together are
a Boolean lattice on \(s+1\) atoms. The empty and full endpoints do not
belong to \(\Gamma\), so the intersection has at most \(s\) members. Now

\[
\gamma_C\ge2\binom{s}{\lfloor s/2\rfloor}+1\ge2s+1.
\]

When \(s=0\), the face is \(\{\varnothing,[n]\}\) and misses \(\Gamma\).

Thus \(2|\Gamma\cap C|\le\gamma_C\) for every face. Taking \(y_S=2\) on
\(\Gamma\) is feasible in (1.4) and (1.12), and gives the lower bound
\(2|\Gamma|\). Literal two-letter columns, or \(\lambda=0\) in (1.3),
give the matching upper bound. \(\square\)

Applied to (4.1), this says \(\Psi=2H\) although the incremental fused
length is one. Thus a lower bound on \(\Psi\) rules out the Poisson
signed-face certificate, not arbitrary stateful overlap. A general no-go
must also use endpoint throughput.

---

## 5. Exact endpoint-loss ledger

For intervals ending at a fixed right endpoint \(j\), moving the left
endpoint leftward can only enlarge the union. Thus all represented sets
ending at \(j\) form an inclusion chain and there is at most one distinct
represented set of each rank.

In particular, in a word of length \(W+R\) covering every middle set,
choose one right endpoint for each middle-set witness. These \(W\)
endpoints are distinct, because two distinct equal-rank sets cannot lie in
one chain. Every target not represented at these \(W\) principal endpoints
must end at one of the remaining \(R\) positions. The off-principal
targets are therefore covered by at most \(R\) chains, contain at most
\(R\) members of each rank, and at most \(KR\) members on \(K\) ranks.

For a prescribed principal MTF trajectory, let its \(W\) designated
saturated endpoints expose lower flags

\[
F_{v,q}\in\binom{[2m]}{m-q},\qquad q\in Q,
\]

and put

\[
\widetilde{\mathcal H}_q
=\binom{[2m]}{m-q}
 \setminus\{F_{v,q}:v\text{ principal}\},
\quad
\widetilde M_q=|\widetilde{\mathcal H}_q|,
\quad
X_Q=\sum_{q\in Q}\widetilde M_q.
\tag{5.1}
\]

Consider any fused modification. Let

* \(R\) be the number of physical positions which are not designated
  principal endpoints;
* \(E_q\) be the number of principal rank-\((m-q)\) certificates
  surrendered, and \(E=\sum_{q\in Q}E_q\);
* \(\mathcal H_q^{\rm res}\) be the old canonical holes still not
  represented anywhere after the fusion.

All reset, bridge, face-packet, and seam positions are counted in \(R\).

### Theorem 5.1 — exact fused endpoint ledger

With \(K=|Q|\),

\[
\boxed{
M_{\rm res}:=\sum_{q\in Q}|\mathcal H_q^{\rm res}|
\ge X_Q-KR-E.}
\tag{5.2}
\]

Consequently,

\[
\boxed{
\Psi(\mathcal H^{\rm res})
\ge
\frac{1+\log(2K)}K[X_Q-KR-E]_+,}
\tag{5.3}
\]

and

\[
\boxed{
R+\frac EK+D_{\rm frac}(\mathcal H^{\rm res})
\ge\frac{X_Q}K.}
\tag{5.4}
\]

The same lower bound holds with \(D_{\rm frac}\) replaced by
\(D_{\rm det}\), or by the length of an arbitrary literal completion.
If \(e\) principal endpoints surrender at least one \(Q\)-flag, then
\(E\le Ke\), and

\[
\boxed{
R+e+\text{remaining literal completion length}
\ge\frac{X_Q}K.}
\tag{5.5}
\]

#### Proof

At a nonsurrendered principal endpoint \(v\), the canonical suffix
\(F_{v,q}\) is the unique represented set of its rank ending there. An old
canonical hole is unequal to every such flag. If it becomes represented,
its witness must end either at one of the \(R\) nonprincipal positions or
at a principal endpoint whose \(q\)-certificate was surrendered. At one
fixed rank, these endpoints can gain at most \(R+E_q\) old holes. Summing
over \(q\in Q\) proves (5.2). Because the proof uses right endpoints, it
includes every seam-crossing interval.

Equation (5.3) follows from (1.9). Equations (1.13) and (5.2) give

\[
D_{\rm frac}\ge K^{-1}[X_Q-KR-E]_+.
\]

If \(X_Q\le KR+E\), then \(R+E/K\ge X_Q/K\); otherwise adding the last
display proves (5.4). The deterministic value dominates its fractional
relaxation. Finally, each endpoint in an arbitrary completion covers at
most one residual target at each of the \(K\) ranks, so its length is at
least \(M_{\rm res}/K\). This proves the unrestricted statement and
(5.5). \(\square\)

The theorem closes the incidental-interval loophole whenever the
designated states are retained. It does not claim that changing \(e\)
states needs \(e\) letter edits: one early edit can perturb many later MTF
states.

---

## 6. Gaussian fixed-frame obstruction

Fix a perfect matching \(\mathcal P\) of the \(2m\) coordinates. Consider a
canonical \(H\)-saturated lower-MTF forest with \(p\) post-cut components.
Suppose \(s_{\rm ex}\) selected arcs do not flip one pair of
\(\mathcal P\), while every other selected arc does.

For a middle source having \(f\) full matched pairs, the number of possible
sources is

\[
V_f
=\frac{m!}{f!^2(m-2f)!}\,2^{m-2f}.
\tag{6.1}
\]

For a rank-\((m-q)\) target having \(f\) full pairs, \(f+q\) empty pairs,
and \(m-2f-q\) split pairs, the number of targets is

\[
T_{f,q}
=\frac{m!}{f!(f+q)!(m-2f-q)!}\,2^{m-2f-q}.
\tag{6.2}
\]

Put \(T_{f,q}=0\) outside its natural range and define

\[
D_{m,q}=\sum_f(T_{f,q}-V_f)_+.
\tag{6.3}
\]

### Lemma 6.1 — exact type-capacity deficit

For every \(q\le H\),

\[
\boxed{
\widetilde M_q
\ge[D_{m,q}-q(s_{\rm ex}+p)]_+.}
\tag{6.4}
\]

#### Proof

A pure length-\(q\) path window flips \(q\) distinct pairs of
\(\mathcal P\). Its lower flag empties those split pairs and preserves the
number \(f\) of full pairs. Hence sources of type \(f\) can hit at most
\(\min(V_f,T_{f,q})\) distinct targets of that type.

Every exceptional arc belongs to at most \(q\) length-\(q\) windows, and a
component boundary destroys at most \(q\) possible windows. The pure
windows contribute at most

\[
\sum_f\min(V_f,T_{f,q})
=\sum_fT_{f,q}-\sum_f(T_{f,q}-V_f)_+
=\binom{2m}{m-q}-D_{m,q}.
\]

The at most \(q(s_{\rm ex}+p)\) contaminated starts contribute at most one
new target each. Thus at least \(D_{m,q}-q(s_{\rm ex}+p)\) targets are
absent, proving (6.4). \(\square\)

### Lemma 6.2 — uniform Gaussian capacity limit

For fixed \(0<a<b<\infty\), uniformly when
\(a\le q/\sqrt m\le b\),

\[
\boxed{
\frac{D_{m,q}}W
=\delta(q/\sqrt m)+o(1),}
\tag{6.5}
\]

where

\[
\boxed{
\delta(x)
=e^{-x^2}\Phi_{\rm G}(x/2)
-\Phi_{\rm G}(-3x/2)>0.}
\tag{6.6}
\]

#### Proof

Write

\[
q=x\sqrt m+O(1),\qquad f=\frac m4+X\sqrt m.
\]

Uniform Stirling expansion on bounded \(X\) and compact positive
\(x\)-intervals gives

\[
\frac{V_f}{W}
=\frac4{\sqrt{2\pi m}}e^{-8X^2}(1+o(1))
\tag{6.7}
\]

and

\[
\frac{T_{f,q}}W
=\frac4{\sqrt{2\pi m}}
e^{-8(X+x/2)^2-x^2}(1+o(1)).
\tag{6.8}
\]

The ratio of the limiting target and source densities is
\(e^{-8xX-3x^2}\), so the target exceeds the source exactly for
\(X<-3x/8\). The exact adjacent ratios are

\[
\frac{V_{f+1}}{V_f}
=\frac{(m-2f)(m-2f-1)}{4(f+1)^2}
\tag{6.9}
\]

and

\[
\frac{T_{f+1,q}}{T_{f,q}}
=
\frac{(m-2f-q)(m-2f-q-1)}
{4(f+1)(f+q+1)}.
\tag{6.10}
\]

These ratios are decreasing through their respective saddles. Uniformly
for \(q/\sqrt m\in[a,b]\), comparison of successive ratios on the two
sides of the saddle gives constants \(c,C>0\) such that the normalized
mass outside

\[
|f-m/4|\le M\sqrt m
\]

for \(V\), or outside

\[
|f-(m/4-q/2)|\le M\sqrt m
\]

for \(T\), is at most \(Ce^{-cM^2}\). The portions with distance
\(\Omega(m)\) are smaller geometrically. Thus both discrete laws have
uniform Gaussian tails, which justifies summing the positive difference
and passing uniformly to the integral on \([a,b]\).

Under the source law, \(X\) converges to \(N(0,1/16)\), so its mass below
\(-3x/8\) tends to \(\Phi_{\rm G}(-3x/2)\). The target law has total mass

\[
\frac{\binom{2m}{m-q}}W\longrightarrow e^{-x^2}
\]

and conditional limit \(N(-x/2,1/16)\); its mass below the crossing is
\(e^{-x^2}\Phi_{\rm G}(x/2)\). Their difference is (6.6). It is positive
because the target density is strictly larger on the nonempty region
\(X<-3x/8\). \(\square\)

Choose

\[
Q_m=\{q:\lceil a\sqrt m\rceil\le q\le\lfloor b\sqrt m\rfloor\},
\qquad K_m=|Q_m|,
\tag{6.11}
\]

where \(0<a<b\le A\), and put

\[
\bar\delta_{a,b}
=\frac1{b-a}\int_a^b\delta(x)\,dx>0.
\tag{6.12}
\]

If

\[
s_{\rm ex}+p=o(W/\sqrt m),
\tag{6.13}
\]

then (6.4), (6.5), and a Riemann sum give

\[
\boxed{
\frac1{K_m}\sum_{q\in Q_m}\widetilde M_q
\ge(\bar\delta_{a,b}-o(1))W.}
\tag{6.14}
\]

Indeed, \([u-v]_+\ge u-v\), while

\[
\frac{(s_{\rm ex}+p)\sum_{q\in Q_m}q}{WK_m}
=O\!\left(\frac{\sqrt m(s_{\rm ex}+p)}W\right)=o(1).
\tag{6.15}
\]

### Theorem 6.3 — Gaussian entropy-fusion no-go

Apply an arbitrary fused modification to the fixed-frame principal word.
Let \(R\) count all nonprincipal physical positions and let \(E\) count
all surrendered principal endpoint--rank incidences on \(Q_m\). Under
(6.13),

\[
\boxed{
\Psi(\mathcal H^{\rm res})
\ge
(1+\log(2K_m))
\left[
(\bar\delta_{a,b}-o(1))W
-R-\frac E{K_m}
\right]_+.}
\tag{6.16}
\]

Moreover, for an arbitrary remaining literal completion of length \(L\),

\[
\boxed{
R+\frac E{K_m}+L
\ge(\bar\delta_{a,b}-o(1))W.}
\tag{6.17}
\]

If only \(e\) principal endpoints are altered, so \(E\le K_me\), then

\[
\boxed{
R+e+L\ge(\bar\delta_{a,b}-o(1))W.}
\tag{6.18}
\]

#### Proof

Substitute (6.14) into Theorem 5.1. Equations (5.3), (5.4), and the
arbitrary-completion version of (5.4) give (6.16)--(6.18). \(\square\)

Consequently:

* if all principal flags are retained and \(R=o(W)\), then
  \(\Psi_{\rm res}=\Omega(W\log m)\), because
  \(\log K_m=\frac12\log m+O(1)\);
* if \(R=o(W)\) and \(\Psi_{\rm res}=o(W)\), then

  \[
  E\ge(\bar\delta_{a,b}-o(1))WK_m,
  \qquad
  e\ge(\bar\delta_{a,b}-o(1))W;
  \]

* even outside the signed-face architecture, preserving all but \(o(W)\)
  principal endpoints and using only \(o(W)\) other positions leaves an
  \(\Omega(W)\) physical completion cost.

Thus entropy repair cannot be fused sparsely into the fixed-frame
Gaussian trajectory. Its escapes lie outside the hypotheses:
positive-density principal reflagging, exceptional arcs or component
boundaries at the \(\Omega(W/\sqrt m)\) scale, or a wholesale
non-fixed-frame trajectory.

---

## 7. Canonical MSW one-rank specialization

For this section only, switch to the odd-factor notation

\[
n_{\rm o}=2m+1,\qquad
W_{\rm o}=\binom{2m+1}{m},\qquad
\operatorname{Cat}_m=\frac{W_{\rm o}}{2m+1}.
\]

Theorem 5.1 is ambient-dimension independent. Here it is applied on
\([n_{\rm o}]\), with
\(F_{v,1}\in\binom{[n_{\rm o}]}{m-1}\).

The audited canonical-MSW marked-gap collision family gives

\[
M_1(F_m^{\rm MSW})\ge(1/16-o(1))W_{\rm o}.
\tag{7.1}
\]

For an MTF realization whose designated first-shadow flags are those of
this factor, Theorem 5.1 with \(K=1\) gives

\[
R+e_1+L\ge(1/16-o(1))W_{\rm o}
\tag{7.2}
\]

and

\[
\Psi_{\rm res}
\ge(1+\log2)
[(1/16-o(1))W_{\rm o}-R-e_1]_+.
\tag{7.3}
\]

Thus the canonical MSW endpoint flags cannot be repaired by an
\(o(W_{\rm o})\)
state-preserving fusion. The independently audited marked-gap stability
theorem is stronger at the factor level: any exact factor with
\(o(W_{\rm o})\)
first-shadow holes must replace at least

\[
(1/8-o(1))\operatorname{Cat}_m
\]

canonical MSW wreaths and change at least
\((1/16-o(1))W_{\rm o}\) centered first-shadow owner flags. This is an
edit-volume
obstruction, not a construction of a distant good factor.

---

## 8. Exact remaining lemma and implication scope

The weakest exact statement for the deterministic canonical seam-repair
architecture is

\[
\mathfrak P_H+D_{\rm det}(\mathcal H(\mathcal A))=o(W).
\]

The entropy condition \(\mathrm{EMTF}_A\) is a convenient sufficient
surrogate, not an equivalent condition. The following concrete
trace-condensation statement would prove it.

> **UNPROVED actual principal trace-condensation lemma
> \(\mathrm{APTC}_A\).** For every fixed \(A>0\), choose one exact
> middle-owner chronology (for example, the complementary-geodesic cut of
> one exact odd factor), one common radius-\(H\) adaptive-MTF lift, all its
> boundary states, and one physical bridge/reset system. Let
> \(\mathcal A_{m,A}\) be the resulting single word and let
> \(\mathcal H(\mathcal A_{m,A})\) be the targets in ranks
> \(m-H,\ldots,m-1,m+1,\ldots,m+H\) not represented anywhere in that
> word. Prove jointly that
>
> \[
> \mathfrak P_H=o(W)
> \]
>
> and that the actual holes admit a disjoint partition
>
> \[
> \mathcal H
> =\mathcal H_0\mathbin{\dot\cup}
>  \mathcal G_1\mathbin{\dot\cup}\cdots
>  \mathbin{\dot\cup}\mathcal G_J,\qquad
>  \mathcal G_i\subseteq C_i,
> \]
>
> satisfying
>
> \[
> \boxed{
> 2|\mathcal H_0|
> +\sum_i\phi(|\mathcal G_i|,\gamma_i)=o(W).}
> \tag{\mathrm{APTC}_A}
> \]

By Theorems 2.1 and 3.1, \(\mathrm{APTC}_A\) gives one literal
central-band word of length \(W+o(W)\). If it holds for every fixed \(A\),
Corollary 2.2 gives the coefficient-one OR bound. Every object in the
lemma is common: there is no separate depthwise factor, fractional owner,
or unextendible almost-matching.

The currently known exact odd-factor MTF word already has independent
reset excess

\[
(2H+1)\frac{W}{m+1}=O_A(W/\sqrt m)=o(W).
\tag{8.1}
\]

What is missing is its deep distinct support and the trace-condensation
estimate. Occurrence-level nested flags and box-rainbow portals do not
prove that the masks are globally distinct. The fixed-frame theorem shows
that a stationary pair frame cannot supply the missing support by sparse
repair.

If signed faces are abandoned, a possible alternative escape is a
positive-density joint reflagging theorem: construct a legal one-update
trajectory which changes \(\Omega(W)\) Gaussian principal flags while
preserving exact middle ownership, together with an explicit compatible
endpoint-chain completion of its remaining holes using \(o(W)\) new
positions. Merely proving that the remaining hole poset has chain width
\(o(W)\) would be necessary for such a completion, but not sufficient:
the required reverse-difference letters and endpoint states must also fit
the physical word. This alternative is unproved.

---

## 9. Adversarial audit

The main steps were independently rederived and audited. The following
scope restrictions are essential.

1. **Poisson cost versus physical cost.** \(\Psi\) is the exact convex
   value for canonical proper signed-face blocks. It is not a lower bound
   on arbitrary MTF fusion; Proposition 4.1 gives an explicit unbounded
   gap.
2. **No incidental-witness omission.** In Theorems 5.1 and 6.3, \(R\)
   counts every nondesignated physical position, including reset, bridge,
   seam, and already-fused face positions. The proof uses right endpoints,
   so cross-seam witnesses are included.
3. **No double charging.** A face-packet position already placed inside
   the fused word belongs to \(R\); it is not charged again in the
   residual \(\Psi\). The functional is evaluated only on holes left after
   that fusion.
4. **Rank convention.** The Gaussian fixed-frame theorem uses lower ranks
   only. There is no hidden factor two. A two-sided application must count
   both signed rank sets in \(Q\).
5. **State distance is not update distance.** The variable \(e\) counts
   principal endpoints whose flags change. It is not a lower bound on
   edited letters, because one edit can alter many subsequent MTF states.
6. **Uniform Gaussian range.** Lemma 6.2 is used only on a compact interval
   \(0<a<b\le A\), avoiding an unjustified nonuniform passage through
   \(x=0\).
7. **Fixed-frame scope.** Theorem 6.3 assumes
   \(s_{\rm ex}+p=o(W/\sqrt m)\) and retained labelled principal states. A
   mixed-frame construction at the \(W/\sqrt m\) scale or a wholesale new
   trajectory is not ruled out.
8. **Reset scope.** Theorem 2.1 inserts the packet before a genuine full
   reverse initialization. It does not automatically absorb a packet at a
   shared one-update portal. The gain is the absence of an additional
   reset, not disappearance of packet length.
9. **Actual-hole quantifier.** The structural example (3.10) is not used
   as evidence about an exact factor. The obstruction in Section 6 is the
   theorem about an actual fixed-frame canonical support; the positive
   route remains conditional on \(\mathrm{APTC}_A\).

Accordingly, the route is exhausted at the dichotomy

\[
\boxed{
\begin{array}{c}
\text{actual trace condensation}\Rightarrow
\text{state-compatible }o(W)\text{ seam repair},\\[1mm]
\text{stationary fixed frame}+\text{sparse reflagging}\Rightarrow
\Omega(W)\text{ physical cost}.
\end{array}}
\]

No theorem presently places the principal exact-owner MTF trajectory on
the positive side of this dichotomy.
