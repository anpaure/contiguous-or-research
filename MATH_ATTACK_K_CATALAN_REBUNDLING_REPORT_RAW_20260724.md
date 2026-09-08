The fixed Catalan hierarchy cannot perform the required repair. It admits an exact positive-density rebundling that changes \(3/8+o(1)\) of all wreaths while changing only \(o(W)\) first-shadow coordinates. Noncommuting preparations create \(\Theta(\operatorname{Cat}_m)\) seams, but no theorem forces those seams to disperse among recomputed components or to correlate with hole–duplicate pairs. Thus the route stops at a precise new component-dispersion/NAE lemma, not at synchronization.

Put \(C_j=\operatorname{Cat}_j\), \(B=C_m=W/n\), and \(\tau=(2\,3)\).

## 1. Catalan-tail obstruction

The canonical components are

\[
K_{j,R}=\{AR:A\in\mathcal A_j\},\qquad
|K_{j,R}|=C_j+C_{j+1},
\]

with suffix depth \(r=m-j-2\). Let \(\Delta_{j,R}\) be the rank-\((m-1)\) histogram effect of switching \(K_{j,R}\).

### Theorem 1

For every \(j,R\),

\[
\boxed{
\|\Delta_{j,R}\|_1,\,
|\operatorname{supp}\Delta_{j,R}|
\le (4j+10)(C_j+C_{j+1}).
}
\]

Consequently, for all components with suffix depth \(r\ge L\),

\[
\boxed{
A_{m,L}:=
\sum_{r=L}^{m-2}
(4m-4r+2)
(C_{m-r-2}+C_{m-r-1})C_r
=O\!\left(\frac{W}{\sqrt L}\right).
}
\]

Proof. In the correct step-two cyclic order, the rank-\((m-1)\) windows of \(q(AR)\) are read in blocks

\[
(n,X_A,U_R,Y_A,D_R)
\]

of lengths \(1,a,r,a,r\), where \(a=j+2\). The multisets of \(X_A=\operatorname{Up}(A)\) and \(Y_A=\operatorname{Down}(A)\), over \(A\in\mathcal A_j\), are \(\tau\)-invariant.

Among the \(n\) window slots, \(r+1\) slots avoiding \(n\) and \(r-1\) slots containing \(n\) depend on \(A\) only through the whole of \(X_A\) or \(Y_A\), so their component sums cancel under \(\tau\). Only

\[
n-2r=2a+1=2j+5
\]

old occurrences per root remain as candidates. Removal and addition give the factor \(2\), proving the component bound. Standard estimates

\[
C_s\asymp \frac{4^s}{(s+1)^{3/2}}
\]

then give the displayed Catalan sum.

Now switch every component with \(r\ge L\). The number of replaced wreaths is

\[
M_{m,L}=
\sum_{r=L}^{m-2}
C_r(C_{m-r-2}+C_{m-r-1}).
\]

If \(L\to\infty\) and \(m-L\to\infty\), then

\[
\boxed{\frac{M_{m,L}}{B}\longrightarrow\frac38.}
\]

Indeed, the mass with both \(j,r\) large is \(o(B)\), while the fixed-\(j\) endpoint contributes

\[
\sum_{j\ge0}\frac{C_j+C_{j+1}}{4^{j+2}}=\frac38.
\]

Taking \(L=\lfloor m/2\rfloor\) therefore produces one integral exact factor which:

\[
\begin{aligned}
&\text{replaces }(3/8+o(1))B\text{ wreaths},\\
&\text{reassigns }(3/8+o(1))W\text{ middle owners},\\
&\text{changes the first-shadow histogram by only }
O(W/\sqrt m)=o(W).
\end{aligned}
\]

Moreover, any two vertices of this static tail cube satisfy

\[
\|\mu_{m-1}(F_I)-\mu_{m-1}(F_J)\|_1\le A_{m,L}.
\]

Hence, under the assignment’s frozen premise that the canonical factor has \(\delta W\) first-shadow holes, every tail-cube vertex still has

\[
(\delta-o(1))W
\]

holes. Positive-density root replacement is therefore not enough: most Catalan components are first-shadow seam-sparse.

This conclusion is unconditional as a diameter theorem. The repository itself proves only large finite canonical miss fractions, not an all-\(m\) positive lower limit; the macroscopic-hole corollary uses the premise supplied in the assignment.

## 2. Exact nonlocal seam creation

There is nevertheless a genuine preparatory switch.

Switch every size-two component

\[
K_{0,R}=\{1100R,1010R\}.
\]

For \(\sigma=(4\,5)\), write \(R=1u0v\), \(u\in\mathcal D_t\). Then

\[
\begin{aligned}
\sigma(1100R)&=11010u0v\in K_{t+1,v},\\
\sigma(1010R)&=10110u0v\in K_{t+1,v}.
\end{aligned}
\]

Thus the \(2C_{m-2}\) middle-target orbits represented by these roots cross from a switched \(K_{0,R}\) block to an unswitched block. This exact factor preparation:

\[
\boxed{
\text{replaces }(1/8+o(1))B\text{ wreaths and creates }
(1/8+o(1))B\text{ disjoint target seams}.
}
\]

A general spectral version is stronger. Let

\[
E_K=\bigsqcup_{C\in K}\mathcal W_m(C),
\qquad p_K=\frac{|E_K|}{W}=\frac{|K|}{B}.
\]

Every \(E_K\) is a \(1\)-design:

\[
|E_K|=n|K|,\qquad
|\{X\in E_K:i\in X\}|=m|K|.
\]

Hence its centred indicator has no Johnson harmonics of degrees \(0,1\). Using the degree-two Laplacian eigenvalue \(2(n-1)\),

\[
e_\times\ge(n-1)W\chi_m,\qquad
\chi_m=1-\sum_Kp_K^2.
\]

Every Johnson edge belongs to one transposition, and \(\tau\) contributes none because every \(E_K\) is \(\tau\)-invariant. A max-cut among the block labels therefore gives some \(\sigma\ne\tau\) and an exact \(\tau\)-component switch with at least

\[
\boxed{
\frac{(n-1)W\chi_m}{2(\binom n2-1)}
=
\frac{n(n-1)}{n(n-1)-2}\chi_m B
}
\]

unordered seams.

For the Catalan hierarchy,

\[
\sum_Kp_K^2
\longrightarrow
\frac{25(2-\sqrt3)}{64},
\]

so

\[
\boxed{
\chi_m\longrightarrow
\gamma=\frac{14+25\sqrt3}{64}
=0.895332\ldots
}
\]

A weighted random-cut argument can simultaneously keep both sides between \(B/4\) and \(3B/4\), while retaining

\[
(\beta-o(1))B,\qquad
\beta=\frac{1287-700\sqrt3}{512}=0.1456\ldots
\]

seams. Thus the preparation can be genuinely positive-density on both sides.

## 3. Exact commutator law—and the obstruction

Let \(\kappa(X)\) be the canonical \(\tau\)-block containing the middle target \(X\), and let \(\varepsilon_K\) be the chosen block sign. In the prepared factor \(H\),

\[
o_H(X)=
\tau^{\varepsilon_{\kappa(X)}}
o_F\!\left(\tau^{\varepsilon_{\kappa(X)}}X\right).
\]

Across \(X\mapsto\sigma X\), put

\[
a=\varepsilon_{\kappa(X)},\qquad
b=\varepsilon_{\kappa(\sigma X)}.
\]

After pulling back to the original factor, the transition is

\[
c(X;\sigma)=\tau^b\sigma\tau^a.
\]

Thus

\[
\begin{array}{c|c}
(a,b)&c(X;\sigma)\\ \hline
(0,0)&\sigma\\
(1,1)&\tau\sigma\tau\\
(0,1)&\tau\sigma\\
(1,0)&\sigma\tau.
\end{array}
\]

A seam is therefore exactly a mixed-cocycle location. If \(\tau,\sigma\) overlap, its two orientations carry the opposite \(3\)-cycles \(\tau\sigma\) and \(\sigma\tau\).

This proves noncommutative action, but not useful component splitting. The seams are middle-target orbits, not components of the recomputed \(H\)-versus-\(\sigma H\) overlay. All \(\Theta(B)\) seams may lie in one recomputed component, in which case the only choices are \(H\) and \(\sigma H\), with identical missing counts.

There is an exact warning already at the original factor. For \(\sigma_0=(1\,2)\), the canonical overlay is connected. Contracting it by the \(\tau\)-blocks remains connected on

\[
K_m=\sum_{r=0}^{m-2}C_r=(1/12+o(1))B
\]

vertices, so a max-cut supplies \((1/24+o(1))B\) noncommuting seams—all initially concentrated in one component.

A tempting stronger assertion was independently rejected: the original sealed components

\[
\{101100v,101010v\}
\]

for \(\sigma=(4\,5)\) prove transversality of the two original component partitions, but after the \(K_0\)-preparation the second root has been replaced by its \(\tau\)-image. Those components are not proved to survive in the recomputed overlay.

## 4. Three further rigorous barriers

### Local-chart speed limit

If round \(t\) consists of \(R_t\) disjoint four-letter two-for-two switches, each switch has only two positive first-shadow cells. Hence

\[
M(F_{t-1})-M(F_t)\le2R_t,\qquad R_t\le B/2.
\]

Therefore

\[
M(F_0)-M(F_T)\le BT.
\]

A defect \(M(F_0)\ge\delta W\) cannot be reduced to \(o(W)\) in this architecture unless

\[
\boxed{T\ge(\delta-o(1))n.}
\]

This remains true when the legal four-letter charts are recomputed after every round. Nonlocal components can evade it.

### Finite-energy random signs

In one component cube, let \(\mathcal H\) be the original holes and let \(h_S\) count components carrying occurrences of \(\tau S\). If both conditional bit probabilities are at least a fixed \(\eta>0\), then

\[
\Pr(S\text{ remains a hole})\ge\eta^{h_S}.
\]

Since

\[
\sum_{S\in\mathcal H}h_S\le W,
\]

Jensen gives

\[
\boxed{
\mathbb E M(F_\varepsilon)
\ge |\mathcal H|\,\eta^{W/|\mathcal H|}.
}
\]

Thus \(|\mathcal H|\ge\delta W\) implies

\[
\mathbb E M(F_\varepsilon)
\ge\delta\eta^{1/\delta}W.
\]

Finite-temperature random or hierarchical sampling cannot solve the one-cube problem. An exceptional deterministic correlated assignment is not excluded.

### Multistep group-orbit invariant

For any dynamically recomputed sequence under transpositions \(\tau_t\),

\[
\mu_t-\mu_{t-1}=(\tau_t-I)a_t.
\]

If \(G=\langle\tau_1,\ldots,\tau_T\rangle\), then the total multiplicity on every \(G\)-orbit \(\mathcal O\) is invariant:

\[
\sum_{S\in\mathcal O}\mu_T(S)
=
\sum_{S\in\mathcal O}\mu_0(S).
\]

If the used-transposition graph has coordinate components \(V_i\), these orbits are the profiles \((|S\cap V_i|)_i\). Writing \(T_{\mathcal O}\) for the invariant mass,

\[
\boxed{
M_r(F_T)\ge
\sum_{\mathcal O}(|\mathcal O|-T_{\mathcal O})_+.
}
\]

Hence a fixed finite-coordinate commutator cannot be a general global repair. A viable schedule must make its transposition graph connected, or prove every residual profile deficit negligible.

## 5. Exact theorem still missing

For a recomputed \(\sigma\)-cube, first-shadow optimization is a signed NAE instance. A hole–duplicate orbit contributes useful gain only if the duplicate occurrences lie in at least two recomputed components. A separated covered pair contributes risk.

If \(\ell\) seam-certified orbits are split hole–duplicate pairs, their fair expected gain is at least \(\ell/2\). If the separated-covered risk is at most \(\theta\ell\), \(\theta<1/2\), conditional expectation gives one legal switch with

\[
M(G')\le M(G)-\left(\frac12-\theta\right)\ell.
\]

Thus the precise successor theorem is:

\[
\boxed{
\begin{gathered}
\text{Disperse }\Omega(B)\text{ mixed seams among recomputed components;}\\
\text{map }\Omega(B)\text{ of them injectively to split hole–duplicate pairs;}\\
\text{keep the weighted separated-covered NAE risk below half the gain.}
\end{gathered}
}
\]

Renewing this for \(O(n)\) adaptive rounds would repair a macroscopic first-shadow defect. For MWB it must hold simultaneously through every fixed Gaussian window with the same component signs. Labelled synchronization would still require the separate common nested-owner theorem.

So the lane reaches a rigorous obstruction for the **exhibited
`3/8`-mass tail subcube**: that tail is macroscopically active on owners but
asymptotically inert on the first shadow.  This does not establish
first-shadow inertness of the complete fixed `(2 3)` Catalan hierarchy; the
remaining large-atom head has only a coefficient-scale triangle bound and
may still admit a productive cut.  Nonlocal preparations create many exact
mixed seams, but seam dispersion and targetwise NAE correlation remain
completely unproved.  No current result establishes MWB or labelled
synchronization.  See the independent scope correction in
`MATH_ATTACK_K_CATALAN_REBUNDLING_AUDIT_20260724.md` and the full-cube audit
`MATH_AUDIT_FULL_CANONICAL_23_CUBE_Q1_20260725.md`.
