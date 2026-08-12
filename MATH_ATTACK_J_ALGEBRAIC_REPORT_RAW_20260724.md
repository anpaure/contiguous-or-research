# Verdict

This algebraic/representation-theoretic route does **not** prove the contiguous-OR width conjecture.

It does yield three rigorous advances:

1. The common lower-rank incidence map is surjective over \(\mathbb Z\), not merely over \(\mathbb R\). There is no denominator, Smith-index, congruence, or cross-rank lattice obstruction in the unrestricted signed wreath lattice.
2. Legal component switching admits exact one-step and multistep heat identities, separately on every Johnson/Specht isotype.
3. Those identities expose a definitive obstruction: representation theory controls the coherent displacement, but the component variance lies in the support-feasible exact-factor geometry and cannot be bounded by association-scheme spectra or the signed integer lattice alone.

The smallest clean remaining statement is a legal positive-cut/local-minimum lemma stated below. It remains **UNPROVED**.

## 1. Fixed-window energy

Put \(n=2m+1\), \(W=\binom nm\), \(N_q=\binom n{m-q}\), and write

\[
W=c_qN_q+b_q,\qquad 0\le b_q<N_q.
\]

For fixed \(A>0\), let \(H_A=\lceil A\sqrt m\rceil\). Uniformly for \(q\le H_A\),

\[
\log\frac{W}{N_q}
=\frac{q(q+1)}m+O_A(m^{-1/2}),
\]

so

\[
1\le c_q\le C_A
\]

for a constant depending only on \(A\).

For an exact factor \(F\), let \(\mu_q(F)\) be its depth-\(q\) histogram and define

\[
f_q=\mu_q-\frac{W}{N_q}\mathbf1.
\]

The floor-corrected collision excess is

\[
\Phi_q(F)=
\sum_S\binom{\mu_q(S)}2-
\left[
(N_q-b_q)\binom{c_q}2+
b_q\binom{c_q+1}2
\right].
\]

Exactly,

\[
2\Phi_q
=\|f_q\|_2^2-\frac{b_q(N_q-b_q)}{N_q}
=\sum_S(\mu_q(S)-c_q)(\mu_q(S)-c_q-1).
\tag{1}
\]

If

\[
D_q=\sum_S(c_q-\mu_q(S))_+,\qquad
E_q=\sum_S(\mu_q(S)-c_q-1)_+,
\]

then the balanced overload is \(O_q=\max(D_q,E_q)\). A deficit \(d\) contributes \(d(d+1)\ge2d\) to (1), and a surplus \(e\) contributes \(e(e+1)\ge2e\). Hence

\[
\boxed{O_q\le\Phi_q.}
\tag{2}
\]

Define

\[
\Psi_A(F)=\sum_{q\le H_A}\frac{\Phi_q(F)}{c_q}.
\]

Thus \(\Psi_A=o(W)\) implies fixed-window overload MWB.

## 2. Exact integer-lattice theorem

Let \(\Omega_n\) be the oriented cyclic orders modulo rotation, and let

\[
\mathsf A_r:\mathbb Z^{\Omega_n}\to
\mathbb Z^{\binom{[n]}r}
\]

record all cyclic \(r\)-intervals. Let \(U_r\) be point-versus-\(r\)-set incidence.

### Theorem 1 — octahedral generation

For \(2\le r\le n-2\),

\[
\boxed{
\ker_{\mathbb Z}U_r
=
\left\langle
\omega(K;a,b,c,d)
\right\rangle_{\mathbb Z},
}
\tag{3}
\]

where \(|K|=r-2\), the four displayed points are distinct outside \(K\), and

\[
\omega(K;a,b,c,d)
=e_{Kbc}-e_{Kac}-e_{Kbd}+e_{Kad}.
\]

#### Proof

Induct on \(n\). At \(n=r+1\), the \(r\)-sets are complements of points and \(U_{r+1,r}=J-I\), which is nonsingular.

For \(n\ge r+2\), split \(y\in\ker_{\mathbb Z}U_r\) into its \(n\)-free and \(n\)-containing parts:

\[
y=a+\sum_{T\in\binom{[n-1]}{r-1}}b_Te_{T\cup\{n\}}.
\]

The \(n\)-margin gives \(\sum_Tb_T=0\). Since the Johnson graph \(J(n-1,r-1)\) is connected, its oriented edge differences generate this augmentation lattice integrally.

For adjacent \(T=K\cup\{a\}\) and \(T'=K\cup\{b\}\), choose

\[
c\notin K\cup\{a,b,n\},
\]

which is possible because \(r\le n-2\). The \(n\)-containing part of \(\omega(K;a,b,c,n)\) is \(e_T-e_{T'}\), up to sign. Integral combinations of these octahedra kill the entire \(n\)-containing part. The remainder lies in \(\ker_{\mathbb Z}U_{n-1,r}\), so induction finishes. ∎

### Theorem 2 — simultaneous integral cyclic selectors

For \(n=2m+1\),

\[
\boxed{
(\mathsf A_2,\ldots,\mathsf A_{m-1}):
\ker_{\mathbb Z}\mathsf A_m
\longrightarrow
\bigoplus_{r=2}^{m-1}\ker_{\mathbb Z}U_r
\text{ is onto}.
}
\tag{4}
\]

#### Proof

Every octahedron in (3) is, after relabelling, the rank-\(r\) image of a Petr–Turek four-order selector \(z\), while

\[
\mathsf A_sz=0\qquad(1\le s\le m,\ s\ne r).
\]

Decompose the prescribed target vectors into octahedra and lift them rank by rank. ∎

### Consequence

Given an exact factor indicator \(x_F\) and separately chosen point-regular floor/ceiling quota vectors \(b_r\), Theorem 2 produces

\[
x^\sharp\in\mathbb Z^{\Omega_n}
\]

such that

\[
\mathsf A_mx^\sharp=\mathbf1,\qquad
\mathsf A_rx^\sharp=b_r\quad(2\le r<m).
\tag{5}
\]

Thus one common integral **signed** solution can have perfect balance at every lower rank simultaneously.

This is not an exact factor: \(x^\sharp\) may have negative coefficients. Moreover, the rankwise quota vectors in (5) need not form one nested deletion flow.

The elementary selectors themselves are never applicable factor trades. The two orders on either sign share at least \(n-4>0\) middle intervals, whereas two wreaths in an exact factor must have disjoint middle supports.

Hence:

\[
\boxed{\text{the unrestricted signed lattice is saturated; positivity/support is the gate.}}
\]

## 3. Exact component heat identity

Let \(G=\sigma F\). Overlay the middle-set ownership partitions of \(F\) and \(G\). This is an \(n\)-regular bipartite graph. For a component \(K\), write \(L_K\subset F\), \(R_K\subset G\), and

\[
\delta_{K,q}
=\mu_q(R_K)-\mu_q(L_K).
\]

Choosing either complete side in every component produces one integral exact factor \(F_\varepsilon\).

Because \(|L_K|=|R_K|\), every component effect satisfies

\[
\sum_S\delta_{K,q}(S)=0,\qquad
U_{m-q}\delta_{K,q}=0.
\tag{6}
\]

Thus it lies entirely in the Johnson modules \(E_j\), \(j\ge2\).

Define

\[
A_H=\sum_{q\le H}\frac{
\|\mu_q(F)-\mu_q(\sigma F)\|_2^2}{c_q},
\]

\[
R_H(\varepsilon)=
\sum_{q\le H}\frac{
\|\sum_K\varepsilon_K\delta_{K,q}\|_2^2}{c_q},
\]

and

\[
V_H=\sum_{q\le H}\frac1{c_q}
\sum_K\|\delta_{K,q}\|_2^2.
\]

The floor in (1) is factor-independent, so the parallelogram identity gives exactly

\[
\boxed{
\Psi_H(F_\varepsilon)+\Psi_H(F_{-\varepsilon})
=
2\Psi_H(F)+\frac14(R_H(\varepsilon)-A_H).
}
\tag{7}
\]

For independent fair signs,

\[
\boxed{
\mathbb E_\varepsilon\Psi_H(F_\varepsilon)
=
\Psi_H(F)-\frac18(A_H-V_H).
}
\tag{8}
\]

No \(O(H\operatorname{Cat}_m)\) error occurs in this identity.

Projecting (8) onto \(E_j\) gives

\[
A_H-V_H
=
\sum_{q,j}\frac1{c_q}
\left[
\left\|\sum_K\delta_{K,q}^{(j)}\right\|_2^2
-\sum_K\|\delta_{K,q}^{(j)}\|_2^2
\right].
\tag{9}
\]

Thus the heat gap is exactly the sum of cross-component inner products. Schur orthogonality does not determine their signs.

## 4. What representation theory does and does not control

For uniform \(\sigma\in S_n\),

\[
\mathbb E_\sigma A_H
=
2\sum_{q\le H}\frac{\|f_q\|_2^2}{c_q}
=
4\Psi_H+2B_H^{\mathrm{fl}},
\tag{10}
\]

where

\[
B_H^{\mathrm{fl}}
=
\sum_{q\le H}
\frac{b_q(N_q-b_q)}{N_qc_q}.
\]

For a uniform transposition \(\tau\), its averaging eigenvalue on
\(E_j\cong S^{(n-j,j)}\) is

\[
1-\frac{2j(n-j+1)}{n(n-1)}.
\]

Therefore

\[
\mathbb E_\tau\|f_q-\tau f_q\|_2^2
=
\sum_{j\ge2}
\frac{4j(n-j+1)}{n(n-1)}
\|f_q^{(j)}\|_2^2.
\tag{11}
\]

The smallest coefficient is \(8/n\), attained at \(j=2\). This proves coherent contraction only at scale \(1/n\) per transposition.

It gives no bound on \(V_H\). Indeed, even within one fixed \(E_2\), component effects \(u,-u\) have

\[
A=0,\qquad V=2\|u\|^2,
\]

whereas \(u,u\) have

\[
A=4\|u\|^2,\qquad V=2\|u\|^2.
\]

The isotypic norms are identical; only their cross-component alignment differs.

### Exact signed-lattice obstruction

For distinct \(a,b,c,d\), define

\[
v(S)=
(\mathbf1_{a\in S}-\mathbf1_{b\in S})
(\mathbf1_{c\in S}-\mathbf1_{d\in S}).
\]

Then \(v\) is an integral pure-\(E_2\) vector and

\[
\|v\|_2^2=4\binom{n-4}{r-2}.
\]

Taking \(\tau=(a\,b)\) gives \(\tau v=-v\). Formal component effects \(v,-v\) therefore satisfy the transposition-anti-invariance constraint but give

\[
A=0,\qquad
V=\frac8{c_q}\binom{n-4}{r-2}
=\Theta_A(W)
\]

for \(r=m-q\), \(q\le A\sqrt m\). In contrast,

\[
H_A\operatorname{Cat}_m
=\frac{H_AW}{n}
=\Theta_A(W/\sqrt m).
\]

Moreover, \(v\) is a sum of octahedra and has an integral rank-isolated preimage by Theorem 2.

This is not an exact-factor counterexample: those preimages are not packing-compatible. It proves that spectra plus the full integer target lattice cannot yield the required \(O(H\operatorname{Cat}_m)\) comparison.

## 5. Ownership components are an exact intersection invariant

Let \(\mathcal P_F\) be the partition of the middle layer into wreath blocks, and let \(U_F\) be the space of functions constant on every block.

### Lemma 3

The number of ownership components of \(F\) versus \(\sigma F\) is

\[
\boxed{
k(F,\sigma)=\dim(U_F\cap\sigma U_F).
}
\tag{12}
\]

#### Proof

A vector in the intersection assigns a constant to every \(F\)-block and every \(\sigma F\)-block. Along every ownership edge those constants agree, so there is one free value per connected component. The converse is immediate. ∎

Thus connectedness is the exact condition

\[
U_F\cap\sigma U_F=\operatorname{span}\{\mathbf1\}.
\]

Association-scheme traces measure principal angles, not the multiplicity of exact angle zero. In particular, if \(P_F\) is projection onto \(U_F\), \(E_j\) are the middle Johnson projections, \(d_j=\dim E_j\), and \(t_j=\operatorname{Tr}(P_FE_j)\), then

\[
\mathbb E_\sigma
\operatorname{Tr}(P_F\sigma P_F\sigma^{-1})
=
\sum_j\frac{t_j^2}{d_j}.
\tag{13}
\]

This does not determine (12). Hence spectral overlap cannot substitute for a component-connectivity theorem.

## 6. Exact transposition cubes and the Markov obstruction

Fix a transposition \(\tau\). Its component selections form genuine Boolean-cube equivalence classes of exact factors. The child has the same \(\tau\)-components, with some sides reversed. Consequently the fair heat kernel \(K_\tau\) is an orthogonal projection:

\[
K_\tau^2=K_\tau,\qquad K_\tau^*=K_\tau.
\tag{14}
\]

For \(m\ge2\), the cube vertices are distinct. A transposition cannot stabilize an unoriented odd cyclic order: an odd-cycle reflection has cycle type \(1\,2^m\), not one transposition.

Thus

\[
K=\binom n2^{-1}\sum_\tau K_\tau
\]

is self-adjoint, positive semidefinite, and reversible for counting measure on exact factors.

Let

\[
Q_q=\|f_q\|_2^2-\frac{b_q(N_q-b_q)}{N_q}=2\Phi_q,
\qquad
\mathcal Q_A=\sum_{q\le H_A}\frac{Q_q}{c_q}.
\]

Set \(\rho=1-2/n\),

\[
R_q(F,\tau)=\frac14\sum_K\|\delta_{K,q}\|_2^2,
\]

\[
s_q=
\frac14\mathbb E_\tau\|f_q-\tau f_q\|_2^2
-\frac2n\|f_q\|_2^2\ge0,
\]

and

\[
\gamma_q=
\mathbb E_\tau R_q
-\frac2n\frac{b_q(N_q-b_q)}{N_q}.
\]

Then exactly

\[
\boxed{
K\mathcal Q_A
=
\rho\mathcal Q_A+\Gamma_A-S_A,
}
\tag{15}
\]

or

\[
\boxed{
\Gamma_A-S_A
=
\frac2n\mathcal Q_A+(K-I)\mathcal Q_A.
}
\tag{16}
\]

Therefore the proposed \(MHG_A\) inequality is precisely the Foster–Lyapunov estimate

\[
K\mathcal Q_A
\le
\left(1-\frac{\eta_A}{n}\right)\mathcal Q_A
+\frac{C_A}{n}H_A\operatorname{Cat}_m.
\tag{17}
\]

It is not a consequence of (11); it is already the desired integral-chain contraction.

For every stationary law \(\pi\),

\[
\mathbb E_\pi(\Gamma_A-S_A)
=
\frac2n\mathbb E_\pi\mathcal Q_A.
\]

Hence (17), if pointwise, forces every stationary communicating class to have

\[
\mathbb E_\pi\mathcal Q_A
\le\frac{C_A}{\eta_A}H_A\operatorname{Cat}_m.
\tag{18}
\]

This is much stronger than exhibiting one good factor.

Any Poisson/coboundary rewrite retains this obstruction. If

\[
(I-K)u=\mathcal Q_A-\overline{\mathcal Q}_{\mathscr C}
\]

on a communicating class, then

\[
\Gamma_A-S_A-\frac{2-\eta}{n}\mathcal Q_A
=
\frac{\eta}{n}\overline{\mathcal Q}_{\mathscr C}
+
(I-K)\left(\frac{\eta}{n}u-\mathcal Q_A\right).
\tag{19}
\]

Without a bound on the class mean or the Poisson potential, (19) is tautological.

## 7. Exact \(O(n)\)-step identity

For a fixed transposition word \(\tau_1,\ldots,\tau_T\), let

\[
P_t=\frac{I+\tau_t}{2},\qquad
M=P_T\cdots P_1,\qquad
Q_t=P_T\cdots P_{t+1}.
\]

If \(\xi_t\) is the centered component-switching noise, then

\[
x_T=Mx_0+\sum_{t=1}^TQ_t\xi_t.
\]

Because the word is fixed before the component signs are sampled, the \(\xi_t\) are martingale differences. Thus

\[
\boxed{
\mathbb E\Psi_A(F_T)
=
\frac12\|Mx_0\|_A^2-B_A
+\frac18\mathcal N_T,
}
\tag{20}
\]

where

\[
\mathcal N_T=
\sum_{t=1}^T
\mathbb E\sum_K\|Q_t\delta_{t,K}\|_A^2.
\]

The future projections filter early component noise.

Let

\[
d_T=\frac12\|Mx_0\|_A^2-B_A.
\]

Integrality of every final leaf forces

\[
\mathcal N_T\ge8(-d_T)_+.
\]

Defining

\[
\mathcal R_T=\mathcal N_T-8(-d_T)_+\ge0
\]

gives the exact restitution identity

\[
\boxed{
\mathbb E\Psi_A(F_T)
=(d_T)_++\frac18\mathcal R_T.
}
\tag{21}
\]

Thus total noise cannot be made small: some is forced to restore the integer floor. Only \(\mathcal R_T\) is harmful.

For independent uniform transpositions, the projection contraction on \(E_j\) is

\[
\alpha_j=1-\frac{j(n-j+1)}{n(n-1)}
\le1-\frac2n.
\]

Hence for

\[
T_0=\lceil n\log2\rceil
\]

some fixed word satisfies

\[
\|Mx_0\|_A^2\le\frac14\|x_0\|_A^2.
\tag{22}
\]

The coherent \(O(n)\)-step contraction is therefore complete. The sole missing estimate is on \(\mathcal R_{T_0}\).

The \(O(n)\) scale is sharp in the signed \(E_2\) relaxation. A circulant zero-row-sum edge array gives a pure \(E_2\) vector for which every sequence of \(o(n)\) transposition projections leaves \(1-o(1)\) of its norm: after \(t\) steps, all edges between the at least \(n-2t\) untouched coordinates retain their coefficients.

## 8. Smallest remaining legal selector lemma

For fixed \(\tau\), let \(\Delta_K\) be the weighted all-depth component effects and let \(\Delta_T=\sum_{K\in T}\Delta_K\). Since \(\tau\Delta_K=-\Delta_K\), switching precisely \(T\) gives

\[
\boxed{
\mathcal Q_A(F_T)-\mathcal Q_A(F)
=
-\langle\Delta_T,\Delta_{T^c}\rangle_A.
}
\tag{23}
\]

Therefore a strict legal descent exists exactly when the signed component Gram graph has a positive cut.

The smallest clean route-specific lemma is:

> **UNPROVED positive-cut/local-minimum lemma.**  
> For every fixed \(A\), if
> \[
> \mathcal Q_A(F)>C_AH_A\operatorname{Cat}_m,
> \]
> then some coordinate transposition and some subset of its ownership components satisfy
> \[
> \langle\Delta_T,\Delta_{T^c}\rangle_A>0.
> \tag{LM\(_A\)}
> \]

Equivalently, every local minimum under legal transposition-component switches has energy \(O_A(H_A\operatorname{Cat}_m)\).

This is strictly weaker than one-step \(HG_L\), uniform \(MHG_A\), or a quantitative drift rate. It is still unproved and is exactly support-feasible.

A representation-aligned stronger alternative is the **UNPROVED** excess-noise bound

\[
\mathcal R_{T_0}
\le4\Psi_A(F)+C_AH_A\operatorname{Cat}_m.
\tag{FEN\(_A\)}
\]

## 9. Why the missing lemma finishes MWB and the OR bound

Assume \(LM_A\). Repeated strict legal descent terminates because the exact-factor space is finite. At termination,

\[
\mathcal Q_A(F)=O_A(H_A\operatorname{Cat}_m).
\]

Since \(W=n\operatorname{Cat}_m\),

\[
\frac{H_A\operatorname{Cat}_m}{W}
=\frac{H_A}{n}
=O_A(m^{-1/2})=o(1).
\]

Therefore

\[
\sum_{q\le H_A}\frac{O_q(F)}{c_q}
\le
\Psi_A(F)
=\frac12\mathcal Q_A(F)
=o(W).
\]

Doing this for every fixed integer \(A\), then choosing a sufficiently slowly growing diagonal \(A=A(m)\), gives

\[
H=\sqrt m\,\omega(m),\qquad
\omega(m)\to\infty,\qquad H=o(m),
\]

and one exact factor with

\[
\sum_{q\le H}\frac{O_q}{c_q}=o(W).
\]

Every hole contributes at least \(c_q\) deficit units, so

\[
M_q\le\frac{O_q}{c_q},
\qquad
\sum_{q\le H}M_q=o(W).
\]

The audited literal wreath word then has length

\[
W+O(HW/m)+2\sum_{q\le H}M_q=W+o(W).
\]

The symmetric-chain product word covers both outer tails in \(o(W)\) because \(H/\sqrt m\to\infty\) and \(H=o(m)\). Hence

\[
\nu(2m+1)\le W+o(W),
\]

and the standard trimmed lift gives

\[
\nu(k)=(1+o(1))
\binom{k}{\lfloor k/2\rfloor}.
\]

Every estimate after \(LM_A\) is therefore rigorous.

## 10. Labelled common ownership remains stronger

The heat route always keeps one exact factor and uses one common component choice across every depth. It proves overload MWB, not the stronger labelled statement involving a balanced nested resolution \(P\).

For \(r=m-q\), if \(b_q\) is the fibre histogram of \(P_q\), then

\[
e_q(F,P)\ge
\frac1{2r}
\left\|
U_rb_q-r\frac Wn\mathbf1
\right\|_1.
\tag{24}
\]

Indeed, each mismatch changes the point-incidence vector by \(\ell_1\)-norm at most \(2r\).

The known lower-bounded flow constructs balanced nested \(P\), but does not ensure proximity to the wreath flags. Independent point-regular quota vectors need not nest. Thus

\[
\sum_q O_q/c_q=o(W)
\]

does **not presently imply**

\[
\sum_q e_q/c_q=o(W).
\]

A costed common-flow proximity theorem would be an additional **UNPROVED** lemma. This does not affect overload MWB’s direct implication to the OR bound.

For the alternative deep-tail cutoff, the precise safe condition is

\[
\frac{Q^2}{m}
\ge
\frac12\log m-\frac12\log\log m+\omega(1).
\]

Any fixed \(Q=\alpha\sqrt{m\log m}\) with \(\alpha>1/\sqrt2\) is safe. Writing only
\((1/\sqrt2+o(1))\sqrt{m\log m}\) is ambiguous without a one-sided second-order condition.

## Adversarial audit

The main claims were independently audited. The surviving limitations are:

- Theorem 2 produces a signed integer vector, not a Boolean exact factor.
- Rankwise point-regular quotas do not produce one common nested resolution.
- The pure-\(E_2\) examples are counterexamples only to spectral/lattice relaxations, not to \(LM_A\) for actual factor components.
- One-shot constant-\(\eta\) \(HG_L\) is not disproved for exact factors; it is merely stronger than the natural transposition scale.
- Formula (20) requires the transposition word to be fixed before future component signs are exposed. For adaptive words, only the one-step martingale identity is valid.
- Fixed transposition heat kernels are reversible, so no state-independent spectral frame can contract every exact factor.
- The observed pentadiagonal inverse and growing-\(j\) harmonic ordering remain unproved and, even if proved, would not control component correlations.
- No finite or computational search was used in these arguments.

Accordingly, the strongest rigorous conclusion is:

\[
\boxed{
\begin{gathered}
\text{all real and integer target-lattice obstructions vanish;}\\
\text{the correct coherent heat scale is } \Theta(n)\text{ transpositions;}\\
\text{the sole remaining gate is a support-feasible positive-cut}\\
\text{or excess-component-noise theorem inside the exact-factor fibre.}
\end{gathered}}
\]

The common baselines are [the fixed-window synchronization brief](/Users/amir.nuriyev/Documents/problem/EXACT_REMAINING_SYNC_THEOREM_BRIEF_20260724.md) and [the frozen heat-gap audit](/Users/amir.nuriyev/Documents/problem/MESOSCOPIC_COMPONENT_HEAT_GAP_AUDIT_20260724.md).

## Independent audit corrections

The octahedral kernel proof and the coefficient-one simultaneous selector
map are correct.  The selector identity itself is an imported Petr--Turek
input, and the conclusion concerns only the unrestricted signed map
\[
\ker_{\mathbb Z}A_m\longrightarrow
\bigoplus_{r=2}^{m-1}\ker_{\mathbb Z}U_r.
\]
It removes no positivity, packing-support, regular-quota, or nesting
obstruction.  Oriented columns and unoriented factor columns must be kept
explicitly distinguished.

For a transposition \(\tau\), the cube-average operator is indeed an
orthogonal projection.  The missing structural justification is that if the
two swapped labels have cyclic distance \(d\le m\), then every wreath \(C\)
shares at least \(n-2d\ge1\) middle intervals with \(\tau C\).  Consequently
each ownership component is \(\tau\)-invariant and its two sides are
exchanged by \(\tau\).  Non-stabilization of one wreath alone would not prove
this.

In equations (20)--(21), define
\[
x_t=(f_{t,q})_q,\qquad
\|x\|_A^2=\sum_q\|x_q\|_2^2/c_q,\qquad
\xi_t=\frac12\sum_K\varepsilon_{t,K}\delta_{t,K},
\]
and
\[
B_A=\frac12\sum_q
\frac{b_q(N_q-b_q)}{N_qc_q}.
\]
The contracting transposition word depends on the current \(F,x_0,A\) and
must be fixed before its component signs are sampled; it is not universal.
\((\mathrm{FEN}_A)\) is sufficient only with the joint quantifier that this
same word satisfies both coherent contraction and the excess-noise bound.
Then one obtains
\[
d_T^+\le\Psi_A(F)/4,\qquad
\mathbb E\Psi_A(F_T)\le
\frac34\Psi_A(F)+O_A(H_A\operatorname{Cat}_m).
\]

\((\mathrm{LM}_A)\) and \((\mathrm{FEN}_A)\) are route-specific sufficient
lemmas, not necessary gates.  Nor is \(\mathrm{LM}_A\) generally comparable
with an \(HG_L\) statement that may use an arbitrary permutation rather than
a transposition.  The final overload-to-OR implication is valid relative to
the imported exact-factor existence, literal wreath transfer, product-tail,
and trimmed-lift theorems.
