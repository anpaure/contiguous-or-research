# Floor-corrected heat route: final theorem-level report

The floor-corrected heat route is now genuinely isolated, but it does not prove the conjecture. The remaining fair-heat condition is exactly a drift statement for the desired energy, not a consequence of \(S_n\) smoothing. A strictly weaker signed-component condition and an exact \(O(n)\)-step circuit formulation survive.

## 1. Fixed-window energy

Fix \(A>0\), set \(H_A=\lceil A\sqrt m\rceil\), and write

\[
W=c_qN_q+r_q,\qquad
N_q=\binom{2m+1}{m-q},\qquad
c_q=\left\lfloor\frac W{N_q}\right\rfloor .
\]

For an exact factor \(F\), let

\[
f_q=\mu_q-\frac W{N_q}\mathbf1,\qquad
B_q^{\rm fl}=\frac{r_q(N_q-r_q)}{N_q},
\]

and define the full floor-corrected energy

\[
Q_q(F)=\|f_q\|_2^2-B_q^{\rm fl}
=\sum_S(\mu_q(S)-c_q)(\mu_q(S)-c_q-1).
\]

Thus \(Q_q\ge0\) and is twice the balanced pair-collision excess. Put

\[
\mathcal Q_A(F)=\sum_{q\le H_A}\frac{Q_q(F)}{c_q}.
\]

The exact overload decomposition gives

\[
2O_q(F)\le Q_q(F),
\qquad
\sum_{q\le H_A}\frac{O_q(F)}{c_q}
\le\frac12\mathcal Q_A(F).
\tag{1}
\]

Hence \(\mathcal Q_A(F)=o(W)\) for every fixed \(A\), followed by diagonalization, proves overload MWB and the final OR bound.

For the factor-independent deep tail, the safe statement is

\[
\frac{Q^2}{m}\ge
\frac12\log m-\frac12\log\log m+\omega(1)
\quad\Longrightarrow\quad
\sum_{q\ge Q}\frac{O_q(F)}{c_q}=o(W)
\]

for every exact factor. In particular, \(Q=\alpha\sqrt{m\log m}\) is safe for fixed \(\alpha>1/\sqrt2\).

## 2. The master \(MHG_A\) quantity is an exact coboundary

Let \(\mathsf K\) be the uniform-transposition, fair-component heat kernel. With

\[
\rho=1-\frac2n,\qquad n=2m+1,
\]

the audited recurrence is

\[
\mathsf K\mathcal Q_A
=\rho\mathcal Q_A+\widehat\Gamma_A,
\qquad
\widehat\Gamma_A=\Gamma_A-S_A.
\]

Therefore

\[
\boxed{
\widehat\Gamma_A
=(\mathsf K-I)\mathcal Q_A+\frac2n\mathcal Q_A
=(\mathsf K-\rho I)\mathcal Q_A.
}
\tag{2}
\]

This has three consequences.

First, the discounted sum is an identity:

\[
\boxed{
\sum_{t<T}\rho^{T-1-t}\mathsf K^t\widehat\Gamma_A
=
\mathsf K^T\mathcal Q_A-\rho^T\mathcal Q_A.
}
\tag{3}
\]

Thus a discounted bound on \(\widehat\Gamma_A\) is exactly a terminal-energy bound in different notation.

Second, on every stationary communicating class \(\pi\),

\[
\boxed{
\mathbb E_\pi\widehat\Gamma_A
=\frac2n\mathbb E_\pi\mathcal Q_A.
}
\tag{4}
\]

Consequently the proposed estimate

\[
\widehat\Gamma_A(F)
\le
\frac{2-\eta_A}{n}\mathcal Q_A(F)
+\frac{C_A}{n}H_A\operatorname{Cat}_m
\tag{MHG\(_A\)}
\]

already forces

\[
\mathbb E_\pi\mathcal Q_A
\le
\frac{C_A}{\eta_A}H_A\operatorname{Cat}_m=o(W)
\]

in every stationary class.

Third, adding an arbitrary coboundary does not weaken the problem. If

\[
\widehat\Gamma_A
\le
\frac{2-\eta_A}{n}\mathcal Q_A+r_A+(I-\mathsf K)h,
\]

then

\[
(\mathsf K-I)(\mathcal Q_A+h)
\le-\frac{\eta_A}{n}\mathcal Q_A+r_A.
\]

Stationary averaging again gives \(\mathbb E_\pi\mathcal Q_A\le nr_A/\eta_A\). Conversely, on a finite irreducible class, this stationary bound is sufficient to manufacture such an \(h\) by solving the Poisson equation. Thus an unrestricted coboundary formulation is equivalent to the desired low stationary energy.

This rigorously answers the filtered-\(\gamma\) question: there is no purely spectral or generic coboundary shortcut.

## 3. Exact integral signed-component theorem

For a transposition \(\tau\), define

\[
A_\tau
=\sum_{q\le H_A}\frac{\|f_q-\tau f_q\|_2^2}{c_q},
\]

\[
R_\tau(\varepsilon)
=\sum_{q\le H_A}\frac{
\left\|\sum_K\varepsilon_K\Delta_{K,q}\right\|_2^2}{c_q},
\]

\[
V_\tau=\mathbb E_\varepsilon R_\tau(\varepsilon),
\qquad
\beta_\tau^{\rm sgn}=\min_\varepsilon R_\tau(\varepsilon).
\]

Every signing produces an actual integral exact factor. The antipodal identity is

\[
\boxed{
\mathcal Q_A(F_\varepsilon)+\mathcal Q_A(F_{-\varepsilon})
=
2\mathcal Q_A(F)+\frac12\bigl(R_\tau(\varepsilon)-A_\tau\bigr).
}
\tag{5}
\]

Therefore some antipodal child satisfies

\[
\boxed{
\mathcal Q_A(G)
\le
\mathcal Q_A(F)-\frac14
\bigl(A_\tau-\beta_\tau^{\rm sgn}\bigr).
}
\tag{6}
\]

Fair \(MHG_A\) is exactly equivalent to

\[
\mathbb E_\tau(A_\tau-V_\tau)
\ge
\frac{4\eta_A}{n}\mathcal Q_A
-\frac{4C_A}{n}H_A\operatorname{Cat}_m.
\tag{7}
\]

Since \(\beta_\tau^{\rm sgn}\le V_\tau\), the strictly weaker, scale-correct integral target is

\[
\boxed{
\mathbb E_\tau(A_\tau-\beta_\tau^{\rm sgn})
\ge
\frac{4\eta_A}{n}\mathcal Q_A
-\frac{4C_A}{n}H_A\operatorname{Cat}_m.
}
\tag{SMHG\(_A\)}
\]

It yields a deterministic exact child with

\[
\mathcal Q_A(G)
\le
\left(1-\frac{\eta_A}{n}\right)\mathcal Q_A(F)
+\frac{C_A}{n}H_A\operatorname{Cat}_m.
\]

Iteration for \(O_A(n)\) steps reaches \(O_A(H_A\operatorname{Cat}_m)=O_A(W/\sqrt m)=o(W)\).

### Genuine-factor obstruction

Let \(F_*\) globally minimize \(\mathcal Q_A\). Both antipodal children in (5) have energy at least \(\mathcal Q_A(F_*)\). Hence

\[
R_\tau(\varepsilon)\ge A_\tau
\quad\text{for every }\tau,\varepsilon.
\]

The all-positive signing has \(R_\tau=A_\tau\), so

\[
\boxed{
\beta_\tau^{\rm sgn}=A_\tau,\qquad V_\tau\ge A_\tau
}
\tag{8}
\]

at every global minimizer.

Thus either fair \(MHG_A\) or signed \(SMHG_A\), when applied at the minimizer, already forces the desired \(\mathcal Q_A(F_*)=O_A(H_A\operatorname{Cat}_m)\) conclusion. Neither is a softer consequence of continuous smoothing.

If the ownership overlay is connected, there is one component and

\[
\beta_\tau^{\rm sgn}=V_\tau=A_\tau.
\]

The only children are \(F\) and \(\tau F\), so covariance cancels the entire midpoint smoothing. Large \(A_\tau\) alone gives zero integral progress.

## 4. Exact occurrence-pair form of \(MHG_A\)

For a moved target pair \(\{S,T=\tau S\}\), let \(x_K,y_K\) be the left-side occurrence counts of \(S,T\) inside component \(K\). Define

\[
P_S^{\rm sep}=\sum_{K<J}x_Kx_J,\qquad
P_T^{\rm sep}=\sum_{K<J}y_Ky_J,
\]

\[
C_{ST}^{\rm sep}=\sum_{K\ne J}x_Ky_J.
\]

A direct calculation gives

\[
\boxed{
A_{\{S,T\}}-V_{\{S,T\}}
=
4\bigl(P_S^{\rm sep}+P_T^{\rm sep}-C_{ST}^{\rm sep}\bigr).
}
\tag{9}
\]

Consequently fair \(MHG_A\) is precisely

\[
\boxed{
\begin{aligned}
\mathbb E_\tau\sum_{q\le H_A}\frac1{c_q}
\sum_{\{S,\tau S\}}
\bigl(
P_S^{\rm sep}+P_{\tau S}^{\rm sep}
-C_{S,\tau S}^{\rm sep}
\bigr)
\ge{}&
\frac{\eta_A}{n}\mathcal Q_A(F)\\
&-\frac{C_A}{n}H_A\operatorname{Cat}_m .
\end{aligned}}
\tag{10}
\]

This identifies the missing geometry exactly:

- same-target duplicate pairs in different components are the positive term;
- opposite-target occurrences in different components are the negative term;
- duplicates concentrated in one component supply no repair energy;
- fragmentation alone is insufficient.

For example, with \(c_q=1\), a load pair \((0,2)\) has positive floor excess but contributes zero if the two duplicate occurrences lie in one component. Conversely, \((1,1)\) has zero floor excess but contributes \(-1\) if its two occurrences lie in different components.

Thus bounded capacities, load histograms, target robustness, and the \(S_n\) decomposition do not imply (10).

## 5. Exact \(O(n)\)-step ledger

Let

\[
\lambda_j=1-\frac{j(n-j+1)}{n(n-1)}
\]

on the Johnson module \(S^{(n-j,j)}\). For the uniform-transposition fair heat chain,

\[
\boxed{
\begin{aligned}
\mathbb E\|f_{T,q,j}\|_2^2
={}&\lambda_j^T\|f_{0,q,j}\|_2^2\\
&+\frac14\sum_{t<T}\lambda_j^{T-1-t}
\mathbb E\sum_K\|\Delta_{t,K,q,j}\|_2^2.
\end{aligned}}
\tag{11}
\]

This is the sharp multistep identity: random-transposition sampling belongs to the signal, and only component rounding remains as propagated noise.

Since \(\lambda_j\le\lambda_2=1-2/n\), \(T=\Theta(n)\) gives constant continuous contraction. A sufficient multistep component-noise lemma is

\[
\mathcal C_T
\le
\gamma_TB_A+2r_{m,A},
\qquad
\gamma_T=1-\left(1-\frac2n\right)^T,
\qquad
r_{m,A}=o(W),
\]

where \(\mathcal C_T\) is the discounted component term from (11) and \(B_A\) is the exact integer floor. This produces an integral endpoint satisfying

\[
\mathcal Q_A(G)
\le(1-\gamma_T)\mathcal Q_A(F)+2r_{m,A}.
\]

The weakest direct nonreversible replacement is a legal circuit of \(T=O_A(n)\) actual factors satisfying

\[
\sum_{t<T}(A_t-R_t)
\ge
4\eta_A\mathcal Q_A(F_0)-4r_{m,A},
\qquad r_{m,A}=o(W).
\tag{12}
\]

No such circuit theorem is proved. It is, however, correctly scaled; the earlier constant-\(\eta\) one-permutation \(HG_L\) was not.

## 6. Common ownership: what is and is not proved

The corrected logical relation is

\[
(\mathrm{CA}_A)\Longrightarrow(\mathrm{GW}),
\]

not equivalence. Small overload already proves the OR bound directly, but does not currently produce a nearby common balanced nested resolution.

### Prefix-freezing theorem

Let \(L_q(X)\) be the factor-induced deletion paths and choose stopping depths \(a(X)\). Freeze every owner through \(a(X)\), and let \(g_q(S)\) be the frozen load. Assume

\[
g_q(S)\le c_q+1.
\]

Give the residual layered inclusion flow node capacities

\[
\ell_q(S)=\max\{0,c_q-g_q(S)\},
\qquad
u_q(S)=c_q+1-g_q(S).
\]

If this single residual lower-bounded network satisfies all Hoffman cuts, total unimodularity gives an integral residual flow and hence one balanced nested resolution \(P\) with

\[
\boxed{
\sum_{q\le H_A}\frac{e_q(L,P)}{c_q}
\le
\sum_X\sum_{q>a(X)}\frac1{c_q}.
}
\tag{13}
\]

This is an exact positive common-owner lemma. The missing part is selecting stopping depths with small tail charge while retaining every residual Hoffman inequality.

### Generic stability is false

There are one-layer owner networks with capacities \(\{1,2\}\), overload \(1\), and constant floor energy for which the unique balanced assignment changes \(N-1\) of \(N+o(N)\) owners. Thus total unimodularity, bounded quotas, and small histogram distance alone cannot imply labelled proximity.

### Full Boolean one-rank repair is better

For a \((d_{\mathcal X},d_{\mathcal S})\)-biregular owner-target graph, let

\[
\lambda=\frac{|\mathcal X|}{|\mathcal S|}
=\frac{d_{\mathcal S}}{d_{\mathcal X}},
\qquad c=\lfloor\lambda\rfloor,
\qquad c<\lambda<c+1.
\]

Every assignment \(f\) has a balanced assignment \(g\) satisfying

\[
\boxed{
|\{X:f(X)\ne g(X)\}|
\le
O(f)\left[
2+
\frac{\log N}{\log(\lambda/c)}
+
\frac{\log N}{\log((c+1)/\lambda)}
\right].
}
\tag{14}
\]

The proof uses two alternating BFS phases. Lower-deficit reachable target sets grow by \(\lambda/c\) until meeting a donor; after upper excess is removed, capacity-augmentation owner sets grow by \((c+1)/\lambda\) until reaching a vacancy.

For the Boolean first shadow,

\[
\lambda=\frac{m+2}{m}=1+\frac2m,
\]

so

\[
\boxed{e_1=O(m^2O_1).}
\tag{15}
\]

Therefore overload \(1\) cannot force \(\Theta(W)\) first-shadow changes in the full Boolean inclusion graph.

This theorem remains single-rank, depends on the distance of \(\lambda\) from an integer, and supplies no common nesting. It does not prove that \(O_q=o(W)\) implies \(e_q=o(W)\) without a quantitative rate.

## Final status

The heat route is exhausted at the following exact gate:

> **UNPROVED fragmentation/circuit lemma.** Prove signed \(SMHG_A\), fair \(MHG_A\), or the \(O(n)\)-step circuit inequality (12) for every fixed \(A\).

The targetwise content is exactly (10): cross-component same-target duplicate dispersion must dominate cross-component opposite-target mixing at scale \(\mathcal Q_A/n\).

For the stronger labelled theorem, one additionally needs:

> **UNPROVED common-owner stability.** Select frozen prefixes satisfying every residual Hoffman cut and having \(o(W)\) tail charge.

No genuine exact-factor counterexample to \(MHG_A\) or \(SMHG_A\) was obtained. What is rigorously refuted is the idea that \(S_n\) smoothing, bounded capacities, a generic coboundary, or marginal flow integrality can supply the missing contraction.

## Audit corrections

The following corrections delimit the preceding statements without changing the remaining theorem.

1. The \(SMHG_A\) recurrence contracts by only \(1-\eta_A/n\) per step. From a worst-case starting factor, reaching the \(H_A\operatorname{Cat}_m\) scale therefore requires
   \[
   O_A(n\log W)=O_A(n^2)
   \]
   steps, not merely \(O_A(n)\). A block of \(O_A(n)\) steps gives only a constant-factor contraction. Alternatively, applying the one-step inequality directly at a global minimizer yields the desired bound without iteration.

2. Equation (12) is a sufficient fixed-path circuit condition, not the logically weakest replacement. Its telescoping form requires choosing at each step the lower-energy antipodal child associated with the displayed component signing. For an arbitrary legal sequence, the energy update has an additional midpoint cross term, so the displayed sum does not telescope as written. Even under the sufficient antipodal choice, \(O_A(n)\) steps give only constant contraction; reaching the terminal scale from the worst initial energy again requires repeated blocks, totaling \(O_A(n\log W)\) steps.

3. The abstract moved-pair patterns in Section 4 show that bounded loads, histogram data, and representation-theoretic constraints alone do not imply the desired heat gap. They do not disprove any implication restricted to genuine exact-factor interaction components.

4. The prefix-freezing theorem is conditional on every Hoffman cut of the residual lower-bounded network. It proves integrality and the stated mismatch bound once feasible stopping prefixes are supplied; it does not construct or select prefixes satisfying those cuts.

5. In the biregular repair theorem, \(N\) denotes the number of target vertices, \(N=|\mathcal S|\), and the statement assumes
   \[
   c=\lfloor\lambda\rfloor\ge1.
   \]
   The lower-shadow application has \(c\ge1\); the \(c=0\) case is outside that theorem.
