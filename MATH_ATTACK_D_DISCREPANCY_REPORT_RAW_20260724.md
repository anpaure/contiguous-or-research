## Verdict

This route does **not** prove the contiguous-OR conjecture. It does, however, isolate the failure precisely:

- averaging or concentrating whole coordinate relabelings is exactly inert;
- legal wreath recombination is controlled by ownership-overlay components, not arbitrary signs;
- the common nested resolution introduces a genuine labeled coupling absent from overload MWB;
- adjacent owner-word swaps give an exact rank-isolated repair mechanism, but its evolving sparse graphs need a new Hall-plus-short-transport theorem.

The conjecture is reduced to one explicit support-feasible lemma stated below.

## 1. Fixed-window logic

For fixed \(A>0\), put

\[
K_A=\lceil A\sqrt m\rceil,\qquad
\lambda_q=\frac{W}{N_q},\qquad c_q=\lfloor\lambda_q\rfloor .
\]

Uniformly for \(q\le K_A\),

\[
\log\lambda_q
=\sum_{i=0}^{q-1}
 \log\!\left(1+\frac{2(i+1)}{m-i}\right)
=\frac{q(q+1)}m+O_A(m^{-1/2}).
\]

Hence

\[
1\le c_q\le C_A,\qquad
e^{-A^2-o(1)}W\le N_q\le W,
\]

and therefore

\[
\sum_{q\le K_A}N_q=\Theta_A(W\sqrt m).
\tag{1}
\]

Define

\[
\beta_m(A)=\frac1W\min_F
 \sum_{q\le K_A}\frac{O_q(F)}{c_q},
\]

and

\[
\gamma_m(A)=\frac1W\min_{F,P}
 \sum_{q\le K_A}\frac{e_q(F,P)}{c_q}.
\]

The exact logical relations are

\[
\boxed{\beta_m(A)\le\gamma_m(A).}
\tag{2}
\]

Thus labeled \(CA_A\) implies fixed-window overload MWB, but the converse is unproved.

The two separate diagonalization statements are valid:

- \(\beta_m(A)\to0\) for every fixed \(A\) is equivalent to overload MWB on some window \(H=\sqrt m\,\omega(m)\), with \(\omega\to\infty\) and \(H=o(m)\).
- \(\gamma_m(A)\to0\) for every fixed \(A\) is equivalent to labeled SYNC on such a window.

For the reverse diagonal direction, choose \(M_j\ge j^4\) so that \(m\ge M_j\) implies \(\gamma_m(j)\le1/j\). If \(j(m)\) is the largest \(j\) with \(M_j\le m\), then

\[
j(m)\to\infty,\qquad j(m)\le m^{1/4},
\]

so \(H=j(m)\sqrt m=o(m)\), while the normalized labeled cost is at most \(1/j(m)\).

Because \(c_q\le C_A\), labeled \(CA_A\) is equivalent to

\[
\sum_{q\le K_A}e_q(F,P)=o(W).
\tag{3}
\]

This allows only an \(o(m^{-1/2})\) fraction of the \(\Theta_A(W\sqrt m)\) owner-depth incidences to mismatch.

## 2. Orbit averaging is integrally inert

For every coordinate permutation \(\sigma\),

\[
L_q^{\sigma F}(X)
=\sigma L_q^F(\sigma^{-1}X),
\]

and consequently

\[
\mu_q^{\sigma F}(S)=\mu_q^F(\sigma^{-1}S).
\tag{4}
\]

Therefore every symmetric statistic of the load histogram is constant on the orbit:

\[
O_q(\sigma F)=O_q(F),\qquad
Q_q(\sigma F)=Q_q(F),
\]

as are holes and every symmetric norm.

More strongly, if

\[
J_A(F)=\min_P\sum_{q\le K_A}\frac{e_q(F,P)}{c_q},
\]

then

\[
J_A(\sigma F)=J_A(F).
\tag{5}
\]

Indeed, \(P\mapsto\sigma P\), where

\[
(\sigma P)_q(X)=\sigma P_q(\sigma^{-1}X),
\]

is a bijection of balanced nested resolutions and preserves every mismatch count.

Nevertheless, transitivity gives the exact fractional barycenter

\[
\frac1{n!}\sum_{\sigma}\mu_q^{\sigma F}
=\lambda_q\mathbf1.
\tag{6}
\]

Thus the orbit barycenter is perfectly balanced while every orbit atom has exactly the original discrepancy.

This also rules out recursive coloring of whole-factor atoms. In the weighted Hilbert space

\[
\|z\|_A^2=\sum_{q\le K_A}\frac{\|z_q\|_2^2}{c_q},
\]

let \(Z_\sigma=(\mu_q^{\sigma F}-\lambda_q\mathbf1)_q\). These vectors have mean zero and common norm. If a partial-coloring tree is refined until one orbit factor remains, the conditional barycenters \(M_j\) satisfy the exact martingale identity

\[
\sum_j\mathbb E\|M_j-M_{j-1}\|_A^2
=\mathbb E\|Z_\sigma\|_A^2.
\tag{7}
\]

Hence variance hidden during early averaging returns completely at the singleton leaf. Wreath-level refactorization is indispensable.

For a fixed resolution \(P\), uniform relabeling is worse still. The stabilizer of \(X\) acts transitively on its \((m-q)\)-subsets, so

\[
\Pr_\sigma[L_q^{\sigma F}(X)=P_q(X)]
=\binom mq^{-1}.
\tag{8}
\]

Consequently the expected weighted number of matches through \(K_A\) is

\[
W\sum_{q\le K_A}\frac1{c_q\binom mq}
=\frac{1+o(1)}m\,W.
\tag{9}
\]

The available weighted owner-depth mass is \(\Theta_A(W\sqrt m)\). Uniform orbit averaging therefore cannot supply labeled descent relative to a fixed common \(P\).

## 3. Exact factor recombination theorem

Let \(F,G\) be exact factors. Form their bipartite ownership multigraph:

- left vertices are wreaths of \(F\);
- right vertices are wreaths of \(G\);
- each middle set \(X\) gives one edge joining its unique owners.

Every vertex has degree \(n\).

### Overlay theorem

Every exact factor supported on the colored union \(F\sqcup G\) is obtained by independently choosing, in each connected component, either the complete \(F\)-side or the complete \(G\)-side.

Indeed, if \(x_C,y_D\in\{0,1\}\) indicate selection, exact ownership on the edge \(CD\) gives

\[
x_C+y_D=1.
\]

Along every two-edge path all left variables agree. Connectivity leaves exactly one bit per component. Conversely, those equations cover every middle set exactly once.

Thus partial coloring may act on ownership components, but not on individual wreaths.

For one fixed balanced nested resolution \(P\), let \(a_C(P)\) and \(b_C(P)\) be the weighted mismatch costs contributed by component \(C\) on the \(F\)- and \(G\)-sides. Then

\[
\boxed{
\min_{\substack{J\subseteq F\cup G\\J\text{ exact}}}
E_A(J,P)
=\sum_C\min\{a_C(P),b_C(P)\}.
}
\tag{10}
\]

The exact gain from \(F\) is

\[
\sum_C(a_C(P)-b_C(P))_+.
\tag{11}
\]

This is scalar component selection, not an unconstrained vector-balancing problem. The hard coupling is that the same \(P\) must satisfy all components and depths.

If the overlay is connected, the only supported factors are \(F\) and \(G\). For coordinate relabelings they have identical symmetric energy. No concentration theorem can create a third outcome.

## 4. Exact Gaussian component ledger

Write \(W=c_qN_q+r_q\) and

\[
d_q(F)=\mu_q^F-\lambda_q\mathbf1.
\]

The exact quantization identity is

\[
Q_q(F)
=\frac12\left(
\|d_q(F)\|_2^2-\frac{r_q(N_q-r_q)}{N_q}
\right).
\tag{12}
\]

Hence, with

\[
\Phi_A=
\sum_{q\le K_A}
\frac{r_q(N_q-r_q)}{N_qc_q},
\]

one has

\[
\|d(F)\|_A^2=\Phi_A+2\sum_{q\le K_A}\frac{Q_q(F)}{c_q}.
\tag{13}
\]

For every fixed \(A>0\),

\[
\Phi_A=\Theta_A(W\sqrt m).
\tag{14}
\]

The upper bound follows from \(K_A=O_A(\sqrt m)\) and each term being \(O(W)\). For the lower bound, choose a fixed subinterval of \(0<q/\sqrt m<\min(A,\sqrt{\log2})\) on which \(\lambda_q-1\) stays bounded away from both zero and one; then \(c_q=1\), \(N_q=\Theta_A(W)\), and each of \(\Theta_A(\sqrt m)\) depths contributes \(\Theta_A(W)\).

Thus the correct quadratic target is not \(o(W)\) raw norm. It is

\[
\boxed{\|d(F)\|_A^2\le\Phi_A+o(W).}
\tag{15}
\]

For an overlay component containing \(s_C\) wreaths on each side, let \(\Delta_C\) be its all-depth load difference. Then

\[
\|\Delta_{C,q}\|_1\le2ns_C,\qquad
\|\Delta_{C,q}\|_\infty\le s_C,
\]

and so

\[
\|\Delta_C\|_A^2
\le2ns_C^2\sum_{q\le K_A}\frac1{c_q}
=O_A(ns_C^2\sqrt m).
\tag{16}
\]

Random component signs give the exact identity

\[
\mathbb E\left\|
\frac{d(F)+d(G)}2+\frac12\sum_C\varepsilon_C\Delta_C
\right\|_A^2
=
\left\|\frac{d(F)+d(G)}2\right\|_A^2
+\frac14\sum_C\|\Delta_C\|_A^2.
\tag{17}
\]

Even bounded component sizes give only the raw \(O(W\sqrt m)\) scale. The required result is additive \(o(W)\) above the floor (14). Ordinary vector balancing or matrix concentration does not supply that precision.

## 5. Common nested flow can be rounded alone

There is one positive integral theorem.

Let \(f\) be the integral \(T\)-fold nested flow obtained from all coordinate relabelings of a factor. Then:

- every middle set has outflow \(T\);
- every rank-\((m-q)\) node has flow \(T\lambda_q\).

Split every lower node into an in-node and out-node with capacity interval \([c_q,c_q+1]\), retain each transition edge with capacity \(f_e\), and require unit flow from every middle set.

The fractional flow \(f/T\) is feasible. All bounds are integral and the network matrix is totally unimodular, so there is an integral subflow \(g\le f\). Unit-path decomposition gives one balanced nested resolution.

Thus:

\[
\boxed{\text{the common nested flow alone has no orbit integrality obstruction.}}
\]

But \(g\) may exchange owner identities and suffixes when paths meet. It need not remain close to the actual flags of any one selected wreath factor. That missing coupling is exactly the labeled problem.

Equivalently, \(CA_A\) is an integral exact-cover problem on decorated wreath atoms: one wreath, together with one alternative deletion chain for each of its \(n\) owners. The orbit barycenter is a zero-cost fractional solution. Rounding either the wreath constraints or the flow constraints separately is known; rounding their coupling is not.

## 6. Exact rank-isolated adjacent-swap theorem

Extend each owner’s factor deletion word to \(K_A+1\):

\[
d_X=(d_X(1),\dots,d_X(K_A+1),\dots),
\]

so that

\[
L_q^F(X)=X\setminus\{d_X(1),\dots,d_X(q)\}.
\]

Swapping positions \(q,q+1\) changes the deleted prefix set at exactly depth \(q\), and at no other depth.

Process boundaries sequentially. At stage \(q\), for every owner \(X\), the two possible depth-\(q\) sets form an edge of a multigraph \(G_q\) on \(\binom{[n]}{m-q}\). Orienting the edge toward one endpoint chooses that owner’s depth-\(q\) value.

If \(b_q\) is a prescribed target load vector with total \(W\), then an orientation with indegree vector \(b_q\) exists iff, for every \(U\),

\[
\boxed{
e_{G_q}(U)\le b_q(U)
\le e_{G_q}(U)+|\delta_{G_q}(U)|.
}
\tag{18}
\]

Proof: assign every edge to one endpoint with endpoint demand \(b_q\). Capacitated Hall gives the left inequality; applying it to the complement gives the right one.

Allowing any balanced vector \(c_q\le b_q(v)\le c_q+1\), the equivalent Hoffman cuts are

\[
e_{G_q}(U)\le(c_q+1)|U|,
\tag{19}
\]

\[
c_q|U|\le e_{G_q}(U)+|\delta_{G_q}(U)|.
\tag{20}
\]

Giving the original endpoint cost zero and the swapped endpoint cost one produces an integral min-cost orientation. If \(T_q\) edges are reversed at stage \(q\), later stages do not alter depth \(q\), and the resulting common resolution satisfies exactly

\[
e_q(F,P)=T_q
\]

for the one-pass construction. More generally \(e_q\le T_q\) for arbitrary adjacent-swap sequences.

Therefore:

> If every fixed \(A\) admits an exact factor and a sequential family of feasible orientations with
> \[
> \sum_{q\le K_A}\frac{T_q}{c_q}=o(W),
> \]
> then \(CA_A\), SYNC, and the final OR bound follow.

This operation preserves one exact factor and one common nested resolution throughout. It is stronger than overload MWB.

The graphs are sparse:

\[
|E(G_q)|=W,\qquad
|V(G_q)|=N_q,\qquad
\overline d(G_q)=2\lambda_q=O_A(1).
\tag{21}
\]

Thus their Hall and transport properties cannot be inferred from density of the ambient Boolean inclusion graph.

## 7. Sharp obstruction to short swap repair

Small overload plus Hall feasibility does not imply a short repair.

Take an even cycle \(C_{2\ell}\), with desired indegree one at every vertex. Choose antipodes \(u,v\) and orient both \(u\)-to-\(v\) arcs toward \(v\). Then

\[
\deg^-(u)=0,\qquad
\deg^-(v)=2,
\]

and every other indegree is one. The overload is exactly one.

The only indegree-one orientations of a cycle are its two directed cyclic orientations. Reaching either requires reversing one entire \(u\)-\(v\) arc, hence exactly

\[
\ell=\frac{|V|}{2}
\]

toggles.

Therefore Hall feasibility and overload \(1\) can coexist with linear labeled repair cost. This obstruction can be realized locally by Johnson edges, but it has **not** been shown to occur as the full \(G_q\) of an exact wreath factor. A positive proof must establish a wreath-specific exclusion or expansion theorem.

This also proves why fixed-window overload \(GW\) is not generically equivalent to labeled \(CA_A\): histogram correction may be cheap while every supported labeled correction is far away.

## 8. Exact remaining lemmas

The concrete missing statement for the rank-isolated route is:

> **UNPROVED Short Dynamic Hall Lemma \((SDH_A)\).**  
> For every fixed \(A>0\), there is an exact middle wreath factor \(F\) for which the evolving graphs \(G_1,\dots,G_{K_A}\) admit sequential balanced orientations satisfying (19)–(20) and
> \[
> \sum_{q\le K_A}T_q=o(W).
> \]

This is stronger than \(CA_A\), but it is exact, support-feasible, and checkable.

For the orbit-component route, the logically weakest local replacement is:

> **UNPROVED Labeled Component Descent Lemma \((LCD_A)\).**  
> Let
> \[
> \phi_A(F)=\min_P E_A(F,P).
> \]
> There is \(\eta_m(A)\to0\) such that whenever
> \(\phi_A(F)>\eta_m(A)W\), a coordinate relabeling \(\sigma\) and legal ownership-component switches between \(F\) and \(\sigma F\) produce an exact factor \(F'\) with
> \[
> E_A(F',P_F)<\phi_A(F),
> \]
> where \(P_F\) is one minimizing common resolution for \(F\).

Finite descent would then yield \(\phi_A(F)\le\eta_mW=o(W)\).

Neither lemma is presently proved. Uniform orbit averaging cannot prove \(LCD_A\), because its expected available match gain relative to a fixed \(P_F\) is only \(O(W/m)\).

## 9. Implication for the OR bound

For integer loads, let

\[
D^-=\sum_S(c_q-\mu_q(S))_+,\qquad
D^+=\sum_S(\mu_q(S)-c_q-1)_+.
\]

The exact overload is \(O_q=\max(D^-,D^+)\), and pointwise

\[
\frac12d(d-1)\ge(-d)_+ +(d-1)_+,
\]

so

\[
O_q\le Q_q.
\]

Every hole consumes at least \(c_q\) underload units, hence

\[
M_q\le\frac{O_q}{c_q}
\le\frac{e_q}{c_q}.
\tag{22}
\]

Thus labeled SYNC gives \(\sum_qM_q=o(W)\). The audited word bound becomes

\[
\nu(2m+1)
\le W+O(HW/m)+2\sum_{q\le H}M_q+o(W)
=W+o(W),
\]

because \(H=o(m)\) and \(H/\sqrt m\to\infty\). The standard trimmed lift gives both parities.

The deep tail is independently automatic. If

\[
\frac{Q^2}{m}\ge
\frac12\log m-\frac12\log\log m+\omega(1),
\]

then, for any quantities \(D_q\le W\),

\[
\sum_{q\ge Q}\frac{D_q}{c_q}
=O\!\left(
W\frac mQ e^{-Q^2/m}
\right)
=o(W).
\]

Any fixed \(Q=\alpha\sqrt{m\log m}\) with \(\alpha>1/\sqrt2\) is safe. The boundary notation
\((1/\sqrt2+o(1))\sqrt{m\log m}\) is insufficient unless its second-order approach is explicitly one-sided.

## Adversarial audit

The strongest claims were checked against the following failure modes:

- The fixed-window overload and labeled statements are not conflated: only \(CA_A\Rightarrow GW\) is proved.
- Orbit invariance covers single relabelings and whole-factor coloring only; it does not exclude rare structured wreath-level trades.
- The overlay theorem concerns the colored union of two factors; larger supports may have additional circuits.
- Gaussian component balancing controls histograms, not a common labeled resolution.
- The nested subflow theorem allows owner paths to exchange tails, so it does not solve synchronization.
- \(SDH_A\) is sufficient but not equivalent to \(CA_A\); arbitrary nearby resolutions may require operations outside the one-pass adjacent-swap class.
- The even-cycle obstruction is an exact local orientation counterexample, not an exact-wreath-factor counterexample.
- Bounded capacities do not give bounded repair: the evolving \(G_q\) have only constant average degree.
- All final OR estimates use one exact factor and one common integral nested resolution.

So the stable conclusion is: the orbit/partial-coloring route is exhausted at a precise dynamic sparse-orientation or component-descent theorem. Fractional balance, ordinary discrepancy, entropy averaging, independent quotas, and generic Hall feasibility do not cross that gate.

## Audit corrections and scope clarifications

The following corrections govern the statements and formulas above.

1. **Fixed-window sums start at depth one.** Every fixed-window sum in the discrepancy, matching, energy, and synchronization statements is over
   \[
   1\le q\le K_A.
   \]
   In particular, the estimate
   \[
   W\sum_{q=1}^{K_A}\frac1{c_q\binom mq}
   =\frac{1+o(1)}mW
   \]
   excludes \(q=0\). Including \(q=0\) would add the deterministic \(W\) middle-layer matches and invalidate that estimate.

2. **Scope of the martingale identity.** Equation (7) applies when \(\sigma\) is uniform on the coordinate orbit and \((M_j)\) is the conditional-expectation martingale associated with a filtration generated by successive partitions/refinements of that uniform sample space. It is not a statement about an arbitrary reweighted partial coloring or an arbitrary nonuniform distribution on orbit factors.

3. **Scope of the overlay theorem.** The component characterization applies to the colored union of exactly two factors \(F\sqcup G\). It does not characterize exact factors supported on three or more colored factors, on the whole orbit multicover, or on an uncolored support where additional integral circuits may exist.

4. **Energy convention.** Throughout the report,
   \[
   Q_q=\sum_S\binom{\mu_q(S)}2-\left(N_q\binom{c_q}2+r_qc_q\right)
   =\frac12\sum_S(\mu_q(S)-c_q)(\mu_q(S)-c_q-1)
   \]
   is the collision excess itself. Thus
   \[
   Q_q=\frac12\left(\|d_q\|_2^2-\frac{r_q(N_q-r_q)}{N_q}\right).
   \]
   If instead one calls the full squared-discrepancy excess an “energy,” that quantity is \(2Q_q\), and every associated energy-update coefficient changes by the corresponding factor of two.

5. **Meaning of the random-sign bound.** The \(O(W\sqrt m)\) random-component-sign estimate shows only that the elementary independent-sign/second-moment argument does not reach additive \(o(W)\) accuracy above the quantization floor. It is not an impossibility theorem for correlated partial coloring, entropy methods using additional wreath structure, or a specially constructed legal trade system.

6. **Range for adjacent swaps.** The adjacent-swap construction uses deletion positions \(q,q+1\), so it requires
   \[
   K_A+1\le m.
   \]
   This holds for every fixed \(A\) and all sufficiently large \(m\), but it is part of the theorem's range.

7. **Status of the even-cycle obstruction.** The even-cycle example is an abstract endpoint-orientation obstruction, locally compatible with Johnson edges. It is not a construction of such a cycle as the complete evolving graph \(G_q\) of an actual exact wreath factor. It rules out a black-box Hall-to-proximity implication, not the desired wreath-specific theorem.

8. **Status of the replacement lemmas.** \((SDH_A)\) and \((LCD_A)\) are sufficient method-specific lemmas. Neither is claimed to be necessary, equivalent to \(CA_A\), or logically weakest among all possible routes.

9. **Quantifiers in \((LCD_A)\).** Its intended statement is: for every fixed \(A\), there is \(\eta_m(A)\to0\) such that **for every** exact factor \(F\) satisfying
   \[
   \phi_A(F)>\eta_m(A)W,
   \]
   and for a chosen minimizing common resolution
   \[
   P_F\in\operatorname*{argmin}_P E_A(F,P),
   \]
   there exist a coordinate relabeling and legal two-factor ownership-component switches producing \(F'\) with
   \[
   E_A(F',P_F)<\phi_A(F).
   \]
   Reoptimization afterward gives \(\phi_A(F')\le E_A(F',P_F)\).

10. **Average gain versus qualitative descent.** The \(O(W/m)\) expected component-gain bound for a uniform relabeling shows that uniform averaging cannot establish a useful quantitative or multiplicative drift at the required scale. It does not rule out a rare structured relabeling giving a strictly positive gain, and therefore does not by itself refute the qualitative strict-descent assertion in \((LCD_A)\).

11. **Precise deep-tail threshold.** The controlling sufficient condition is
    \[
    \frac{Q^2}{m}\ge
    \frac12\log m-\frac12\log\log m+\omega(1).
    \]
    In particular, the exact leading choice
    \[
    Q=\frac1{\sqrt2}\sqrt{m\log m}
    \]
    is safe, since it exceeds the displayed threshold by \(\tfrac12\log\log m\). Some one-sided approaches from below are also safe when they still satisfy the precise second-order inequality. The bare notation
    \[
    Q=(1/\sqrt2+o(1))\sqrt{m\log m}
    \]
    is ambiguous because it does not specify the sign or magnitude of the second-order deviation.
