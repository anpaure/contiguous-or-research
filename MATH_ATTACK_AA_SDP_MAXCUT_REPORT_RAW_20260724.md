The SDP/vector-balancing route does not prove \(LM_A\). It yields several exact lower bounds, but also a new obstruction showing that factor energy need not produce even ideal transposition gain from the presently known scalar invariants.

## 1. Exact three-floor decomposition

Fix a transposition \(\tau\). For every moved orbit \(p=\{S,\tau S\}\) at depth \(q\), and genuine ownership component \(K\), put

\[
z_{pK}=a_K(S)-a_K(\tau S),\qquad \alpha_p=\frac2{c_q}.
\]

Then

\[
A_\tau=\sum_p\alpha_p\Big(\sum_Kz_{pK}\Big)^2,
\]

\[
\beta_\tau=
\min_{\varepsilon_K=\pm1}
\sum_p\alpha_p\Big(\sum_K\varepsilon_Kz_{pK}\Big)^2.
\]

The exact Max-Cut identity is

\[
\boxed{
C_\tau^*:=\max_I\langle d_I,d_{I^c}\rangle_H
=\frac{A_\tau-\beta_\tau}{4}.
}
\tag{1}
\]

Let \(\ell_p\) be the componentwise-preserved total load on \(p\), set

\[
\pi_p=\ell_p\bmod2,\qquad
\Pi_\tau=\sum_p\alpha_p\pi_p.
\]

Every integral signing has the same row parity, so \(\beta_\tau\ge\Pi_\tau\). Hence

\[
\boxed{
C_\tau^*
=
\underbrace{\frac{A_\tau-\Pi_\tau}{4}}_{G_\tau\text{: ideal pair-orbit gain}}
-
\underbrace{\frac{\beta_\tau-\Pi_\tau}{4}}_{\text{ownership bundling loss}}.
}
\tag{2}
\]

This separation is decisive: one must prove both \(G_\tau\) is large and the bundling loss is small.

At one rank \(r=m-q\), averaging ideal gain over the \(\binom n2\) transpositions gives the exact nonlinear Johnson energy

\[
\boxed{
\mathbb E_\tau G_{\tau,q}
=
\frac{2}{\binom n2\,c_q}
\sum_{\{S,T\}\in E(J(n,r))}
\left\lfloor\frac{(\mu_q(S)-\mu_q(T))^2}{4}\right\rfloor .
}
\tag{3}
\]

Its kernel is exactly the cone of integer \(1\)-Lipschitz loads:

\[
|\mu_q(S)-\mu_q(T)|\le1
\quad\text{for every Johnson edge }ST.
\tag{4}
\]

## 2. Strongest unconditional genuine-component bounds

Write

\[
w_{KL}=\langle d_K,d_L\rangle_H,\qquad
W_+=\sum w_{KL}^{+},\qquad
W_-=\sum(-w_{KL})^{+},
\]

and \(V_\tau=\sum_K\|d_K\|_H^2\).

The signed frustration identity is

\[
C_\tau^*=W_+-\operatorname{fr}_{\min}.
\tag{5}
\]

If \(\mathfrak M_\tau\) is the maximum \(|w|\)-weight matching in the component Gram graph, forcing every matched positive edge to cross and every matched negative edge not to cross gives

\[
\boxed{
C_\tau^*
\ge
\frac{W_+-W_-}{2}+\frac{\mathfrak M_\tau}{2}
=
\frac{A_\tau-V_\tau}{4}+\frac{\mathfrak M_\tau}{2}.
}
\tag{6}
\]

A dense-graph Rademacher-chaos bound is

\[
\boxed{
C_\tau^*
\ge
\frac{A_\tau-V_\tau}{4}
+\frac1{36}
\left(\sum_{K<L}w_{KL}^2\right)^{1/2}.
}
\tag{7}
\]

For (7), degree-two Bonami gives \(\|Z\|_4\le3\|Z\|_2\); interpolation gives \(\mathbb E|Z|\ge\|Z\|_2/9\), so some signing has \(Z\le-\|Z\|_2/18\).

Thus a cut-local minimum necessarily satisfies, for every \(\tau\),

\[
W_--W_+\ge\mathfrak M_\tau,
\qquad
W_--W_+\ge
\frac1{18}\left(\sum_{K<L}w_{KL}^2\right)^{1/2}.
\tag{8}
\]

These are genuine new structural consequences of local minimality.

## 3. Exact sparsity/forest theorem

Let \(\mathcal I_\tau\) be the bipartite incidence graph between orbit rows \(p\) and components \(K\), with \(pK\) present iff \(z_{pK}\ne0\). Define the rowwise optimum

\[
b_p=\min_{\eta_K=\pm1}
\left(\sum_{K\in N(p)}\eta_Kz_{pK}\right)^2.
\]

If \(\mathcal I_\tau\) is a forest, one common signing simultaneously attains every rowwise minimum:

\[
\boxed{\beta_\tau=\sum_p\alpha_pb_p.}
\tag{9}
\]

Proof: root every tree. At a row reached through one assigned parent variable, choose a local minimizing pattern and reverse all its signs if needed to match the parent. Acyclicity prevents conflicts.

More generally, if deleting rows \(\mathcal R\) leaves a forest, and

\[
L_p=\sum_K|z_{pK}|,
\]

then

\[
\beta_\tau
\le
\sum_{p\notin\mathcal R}\alpha_pb_p
+\sum_{p\in\mathcal R}\alpha_pL_p^2.
\]

Consequently,

\[
\boxed{
C_\tau^*\ge
G_\tau-\frac14\left[
\sum_{p\notin\mathcal R}\alpha_p(b_p-\pi_p)
+\sum_{p\in\mathcal R}\alpha_p(L_p^2-\pi_p)
\right].
}
\tag{10}
\]

This is the cleanest sparsity-based lower bound obtained. It isolates two independent errors:

- local amplitude locking \(b_p-\pi_p\);
- global cycle/holonomy frustration, represented by the feedback rows.

Both must be Catalan-small. Forest structure alone is insufficient: coefficients \(2,2,-2\) already give \(b_p>\pi_p\). Conversely, unit coefficients can have \(b_p=\pi_p\) on every row while a six-cycle of inconsistent constraints forces a positive global loss.

## 4. A high-energy exact-total obstruction before bundling

For all \(m\ge13122\), set

\[
n=2m+1,\qquad r=m-1,\qquad N=\binom nr,\qquad
R=W-N=\frac{2N}{m}.
\]

Choose eight labels \(U=\{a_i,b_i:1\le i\le4\}\), and define \(x\) by

\[
x(S)=
\begin{cases}
+1,&S\cap U\in
\{\{a_1,a_2,a_3,a_4\},\{b_1,b_2,b_3,b_4\}\},\\
-1,&S\cap U\in
\{\{a_1,a_2,b_3,b_4\},\{b_1,b_2,a_3,a_4\}\},\\
0,&\text{otherwise}.
\end{cases}
\tag{11}
\]

Then \(x\) has zero total and every point margin zero. Opposite-sign local patterns have Johnson distance two, so \(x\) is \(1\)-Lipschitz.

Put \(d=rR/n\). On \(V=[n]\setminus U\), choose simple families

\[
\mathcal E_0\subseteq\binom Vr,\quad |\mathcal E_0|=R-d,
\]

\[
\mathcal E_8\subseteq\binom V{r-8},\quad |\mathcal E_8|=d,
\]

whose combined degree at every \(v\in V\) is \(d\). They exist by minimizing the sum of squared degrees: any degree gap at least two permits a same-color high-to-low exchange decreasing the objective. The capacity inequalities follow from both ambient strata having density at least \(3^{-8}\), while \(R/N\le3^{-8}\).

Let

\[
\mathcal H=\mathcal E_0\cup\{U\cup E:E\in\mathcal E_8\},
\qquad
\mu=1+x+\mathbf1_{\mathcal H}.
\tag{12}
\]

Then

\[
\sum_S\mu(S)=W,\qquad
\sum_{S\ni i}\mu(S)=\frac{rW}{n},
\qquad
\mu(S)\in\{0,1,2\}.
\]

Every member of \(\mathcal H\) is Johnson distance at least four from \(\operatorname{supp}x\), so \(\mu\) remains \(1\)-Lipschitz.

Writing \(T=\binom{n-8}{r-4}\), one has

\[
\boxed{
Q_1(\mu)=4T,\qquad O_1(\mu)=2T,
}
\tag{13}
\]

and

\[
\frac{Q_1}{W}\to\frac1{64},
\qquad
\frac{O_1}{W}\to\frac1{128}.
\tag{14}
\]

Yet (4) holds, so

\[
G_{\tau,1}=0
\quad\text{for every transposition }\tau.
\tag{15}
\]

Thus \(A_\tau=\Pi_\tau\); any pair-total-preserving integral decomposition would have \(\beta_\tau=A_\tau\) and \(C_\tau^*=0\).

This construction was independently rederived and audited twice, including the degree-exchange existence argument, integrality of \(d\), capacities, margins, and distance claims.

Crucial scope: \(\mu\) is not proved realizable by an exact wreath factor. It proves that exact total, point regularity, nonnegativity, maximum load two, parity, and Johnson geometry do not imply ideal gain.

Moreover, choosing point-regular balanced quota vectors at every other lower rank and applying simultaneous integral selector surjectivity produces one signed cyclic-order vector with exact middle incidence, all lower loads \(1\)-Lipschitz, and \(Q_1=\Theta(W)\). Hence even the full signed exact-middle relaxation has a high-energy ideal-cut local minimum. Only nonnegative squarefree support-feasible factor geometry is missing.

## 5. SDP/Grothendieck obstruction

The formal component pattern

\[
d_1=2u,\qquad d_2=2u,\qquad d_3=-2u
\]

has

\[
A=4\|u\|^2,\qquad \Pi=0,\qquad \beta=A,\qquad C^*=0.
\]

The vector SDP sets its residual to zero: choose unit vectors \(a,b\) at angle \(120^\circ\) and \(c=a+b\). Every integral coefficient \(\varepsilon_1+\varepsilon_2-\varepsilon_3\) is odd, so integral residual remains \(A\).

Thus the relaxed cut value is \(A/4\) while the integral value is zero. The gap scales arbitrarily and survives parity-only SDP constraints. Hyperplane/Grothendieck rounding necessarily retains an additive term proportional to

\[
\sum_{K<L}|w_{KL}|,
\]

which can be \(\Theta(A)\). There is no Catalan-error consequence without a new ownership-geometry estimate.

Elementary zonotope rounding likewise gives only

\[
\beta\le
\left\|r+\sum_{K\in J}x_Kd_K\right\|^2+
\sum_{K\in J}(1-x_K^2)\|d_K\|^2,
\]

and the number of fractional boundary components can equal the full component rank.

## 6. Genuine MSW components: a positive theorem and a sparsity no-go

For the canonical MSW factor and \(\tau=(2\,3)\), let \(J\) be its \(\operatorname{Cat}_{m-2}\) genuine two-for-two components. Put

\[
d_J=\sum_{K\in J}d_K,\qquad
V_J=\sum_{K\in J}\|d_K\|_H^2.
\]

Selecting every \(K\in J\) independently with probability \(p\) gives exactly

\[
\boxed{
C_\tau^*\ge
p\bigl(\langle d_J,d\rangle-V_J\bigr)
-p^2\bigl(\|d_J\|^2-V_J\bigr).
}
\tag{16}
\]

At \(p=\tfrac12\),

\[
\boxed{
C_\tau^*
\ge
\frac14\left(
\|d\|^2-\|d-d_J\|^2-V_J
\right).
}
\tag{17}
\]

The exact variance is

\[
V_J=
\operatorname{Cat}_{m-2}
\left(
\frac4{c_1}+8\sum_{q=2}^H\frac1{c_q}
\right)
\le(8H-4)\operatorname{Cat}_{m-2}.
\tag{18}
\]

Hence

\[
C_\tau^*
\ge
\frac14\bigl(\|d\|^2-\|d-d_J\|^2\bigr)
-(2H-1)\operatorname{Cat}_{m-2}.
\tag{19}
\]

This is a genuine Catalan-error partial-cut theorem. The missing quantity is the aggregate alignment with the larger components.

The hoped-for bounded-overlap proof fails. Put \(M=m-2\). At depth \(q\), the exact Dyck four-arm formula gives

\[
\boxed{
\|d_{J,q}\|_2^2
\ge
2\operatorname{Cat}_{M-q}\operatorname{Cat}_q^2.
}
\tag{20}
\]

Indeed, for every decomposition \(R=UV\) with
\(U\in\mathcal D_q\), \(V\in\mathcal D_{M-q}\), all \(\operatorname{Cat}_q\) choices of \(U\) yield the same positive \(E\)-suffix dipole; its core contains \(n\), while no opposite-sign arm does, so cancellation is impossible.

Since \(V_{J,q}=8\operatorname{Cat}_M\),

\[
\|d_J\|_H^2-V_J
\ge
\frac{2\operatorname{Cat}_{M-q}\operatorname{Cat}_q^2}{c_q}
-O(H\operatorname{Cat}_M).
\tag{21}
\]

For \(q=H=\lceil A\sqrt m\rceil\),

\[
\frac{\|d_J\|^2-V_J}{V_J}
\ge
\Omega_A\!\left(\frac{4^H}{H^4}\right).
\tag{22}
\]

Therefore the complete MSW local family does not have \(O(n)\) positive-Gram degree. Sparse Bernoulli thinning at \(p=1/n\) cannot be justified by overlap alone; an equally large favorable alignment, or a carefully pruned multiscale family, would be required.

## Final status

Lane AA is exhausted at two distinct, explicitly isolated exact-factor lemmas:

1. **UNPROVED ideal-gain geometry.** Exact wreath-factor chronology must exclude high-energy lower histograms that are Johnson \(1\)-Lipschitz, quantitatively giving
   \[
   \max_\tau G_\tau
   \gtrsim_A \frac{\mathcal Q_A-C_AH_A\operatorname{Cat}_m}{n}.
   \]

2. **UNPROVED bundling geometry.** For the same transposition, the local amplitude plus feedback/holonomy loss in (10) must be \(O_A(H_A\operatorname{Cat}_m/n)\), or an equivalent genuine derivative-frame estimate must hold.

Together they would yield

\[
\max_{\tau,I}\langle d_I,d_{I^c}\rangle_H
\ge
\frac{\eta_A}{n}\mathcal Q_A(F)
-\frac{C_A}{n}H_A\operatorname{Cat}_m,
\]

and therefore \(LM_A\), fixed-window MWB, and the asymptotic contiguous-OR theorem.

Neither statement follows from SDP, Grothendieck, vector balancing, signed-lattice surjectivity, pair parity, bounded component size, row sparsity, or the known MSW local atlas. Any proof must use literal cyclic-prefix chronology and genuine ownership components inside one exact factor.
