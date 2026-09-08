## Verdict

Lane L remains open. I found neither a proof of \(LM_A\) nor a genuine exact-factor counterexample. The route is exhausted at a precise support-feasible dichotomy:

- prove that high energy forces a positive weighted component cut for some transposition; or
- realize a high-energy exact factor whose transposition overlays are all connected, which would disprove \(LM_A\).

The signed lattice cannot decide between them.

### 1. Exact parity-floor form of the Gram problem

Fix a transposition \(\tau\). For each moved pair \(p=\{S,\tau S\}\) at depth \(q\), orient the pair and, for every ownership component \(K\), put

\[
x_K=a_K(S),\qquad y_K=a_K(\tau S),\qquad z_K=x_K-y_K.
\]

Let

\[
z=\sum_K z_K=\mu_q(S)-\mu_q(\tau S),\quad
\ell=\mu_q(S)+\mu_q(\tau S),\quad
\pi=\ell\bmod2.
\]

For a component signing \(\varepsilon\), write

\[
u_p(\varepsilon)=\sum_K\varepsilon_Kz_K.
\]

Every signing preserves \(\ell\), so \(u_p(\varepsilon)\equiv\ell\pmod2\), hence \(u_p(\varepsilon)^2\ge\pi\).

Define

\[
\mathfrak G_\tau
=\frac12\sum_{q,p}\frac{z^2-\pi}{c_q},
\qquad
\mathfrak R_\tau(\varepsilon)
=\frac12\sum_{q,p}\frac{u_p(\varepsilon)^2-\pi}{c_q}.
\]

A direct expansion of the quadratic energy gives the exact integral identity

\[
\boxed{
\mathcal Q_A(F_\varepsilon)-\mathcal Q_A(F)
=
\mathfrak R_\tau(\varepsilon)-\mathfrak G_\tau.
}
\]

Thus \(\mathfrak G_\tau\) is the ideal integral gain from balancing every \(\tau\)-pair independently, while \(\mathfrak R_\tau\ge0\) is the restitution forced by bundling occurrences into entire ownership components.

Since the all-\(+\) signing is \(F\) itself,

\[
\boxed{
F\text{ is }\tau\text{-cut-local}
\iff
\mathfrak G_\tau=\min_\varepsilon\mathfrak R_\tau(\varepsilon).
}
\]

At a local minimum, all ideal pair-balancing gain is therefore lost exactly to component bundling.

The pairwise occurrence expansion is

\[
\frac{z^2-\pi}{2}
=
\left\lfloor\frac\ell2\right\rfloor
+\binom{\mu(S)}2+\binom{\mu(\tau S)}2
-\mu(S)\mu(\tau S),
\]

and

\[
\frac{\sum_Kz_K^2-\pi}{2}
=
\left\lfloor\frac\ell2\right\rfloor+
\sum_K\left[
\binom{x_K}2+\binom{y_K}2-x_Ky_K
\right].
\]

Their difference is exactly

\[
P_S^{\rm sep}+P_{\tau S}^{\rm sep}
-C_{S,\tau S}^{\rm sep}.
\]

This confirms the audited interpretation: separated duplicates help, while separated opposite-target occurrences lock the current signing.

### 2. Strongest consequence of the weighted cut cone

Let

\[
w_{KL}=\langle\Delta_K,\Delta_L\rangle_A.
\]

Switching a component set \(I\) changes energy by

\[
\mathcal Q_A(F_I)-\mathcal Q_A(F)
=-\sum_{\substack{K\in I\\L\notin I}}w_{KL}.
\]

Hence cut-locality is precisely

\[
w^+(\delta I)\le w^-(\delta I)\qquad\text{for every }I.
\]

By the layer-cake/coarea identity, this implies

\[
\boxed{
\sum_{K<L}w_{KL}|t_K-t_L|\le0
}
\]

for every real labelling \(t_K\), and therefore for every \(L^1\) cut semimetric. Moreover, every positive Gram edge of weight \(p\) has negative-network min-cut at least \(p\), so that single demand can be fractionally routed through negative edges.

This is the full automatic cut-cone conclusion. It supplies no Euclidean norm bound and no simultaneous bounded-congestion routing theorem. Connected overlays have one component and an empty Gram graph, so all these inequalities are vacuous at arbitrary energy.

Balanced target pairs are the principal lock. If

\[
|\mu(S)-\mu(\tau S)|\le1,
\]

then \(z^2=\pi\), so their ideal gain is zero, although separated component occurrences can impose positive restitution on every altered signing. Raw cyclic positivity bounds this locking at only \(O_A(W)\) per rank, hence \(O_A(H_AW)\) over the window. The desired terminal energy is

\[
H_A\operatorname{Cat}_m=\frac{H_AW}{n}
=\Theta_A(W/\sqrt m).
\]

Thus raw locking estimates lose a factor \(n\). In a transposition-scale spectral proof, the required floor-restituted error would be

\[
O_A\!\left(\frac{H_A\operatorname{Cat}_m}{n}\right)
=
O_A\!\left(\frac{H_AW}{n^2}\right),
\]

so absolute occurrence bounds miss by \(n^2\) at the terminal scale.

### 3. Exact extension-fan geometry does not close the gap

Let \(r=m-q\), and let \(K\) contain \(k\) old wreaths. Its \(nk\) owned middle roots form a \(\tau\)-invariant set \(E_K\). For each \(X\in E_K\), let \(\partial_q^-(X)\) and \(\partial_q^+(X)\) be its \(q+1\) cyclic \(r\)-subintervals under the old and new owners. Then integrally inside this one component,

\[
\boxed{
(q+1)\Delta_{K,q}
=
\sum_{X\in E_K}
\left(
\mathbf1_{\partial_q^+(X)}
-\mathbf1_{\partial_q^-(X)}
\right).
}
\]

If \(d_C\in\{1,\ldots,m\}\) is the cyclic distance between the transposed labels in wreath \(C\), fixed-root overlap gives

\[
\|\Delta_{K,q}\|_1
\le
\sum_{C\in K}
\begin{cases}
2(q+2d_C),&d_C\le m-q,\\
2(m+d_C),&d_C>m-q.
\end{cases}
\]

Since cyclic distance is uniform on \(1,\ldots,m\),

\[
\boxed{
\mathbb E_\tau\sum_K\|\Delta_{K,q}\|_1
\le
\operatorname{Cat}_m
\left(
2m+2q+2-\frac{q(q+1)}m
\right).
}
\]

Every depth-\(q\) occurrence consumes \(q+1\) distinct owned middle extensions, so

\[
\mu_q(S)\le
\left\lfloor
\frac1{q+1}\binom{m+q+1}{q}
\right\rfloor.
\]

These bounds are exact but much too large. The diagonal variance alone satisfies, for \(2\le r\le m\),

\[
\mathbb E_\tau
\|\tau\mathbf1_{\mathcal I_r(C)}
-\mathbf1_{\mathcal I_r(C)}\|_2^2
=
\frac{4(r(n-r)-2)}{n-1}.
\]

Summed over all wreaths, this is \(\Theta(W)\) per rank. Catalan-scale control therefore requires order-\(W\) signed cancellation inside components. Triangle inequalities and extension capacities discard precisely that cancellation.

### 4. Explicit obstruction blueprint—and the missing realization

There is an explicit nonnegative first-shadow histogram with macroscopic energy that passes the known marginal constraints.

Let \(r=m-1\), \(N=N_1\), and

\[
R=W-N=\frac{2W}{m+2}.
\]

For all sufficiently large \(m\), one can choose a point-regular family \(\mathcal H\subseteq\binom{[n]}r\) of size \(R\). A self-contained construction uses orbits of the cyclic \(n\)-cycle: since

\[
\gcd(n,r)\in\{1,3\},\qquad n/\gcd(n,r)\mid R,
\]

the required size is assembled from full orbits and, when necessary, at most two \(n/3\)-orbits. Their union is point-regular. Put

\[
b_0=1+\mathbf1_{\mathcal H}.
\]

For four distinct labels \(a,b,c,d\), define

\[
v(S)=
(\mathbf1_{a\in S}-\mathbf1_{b\in S})
(\mathbf1_{c\in S}-\mathbf1_{d\in S}),
\qquad
\mu=b_0+v.
\]

Then \(U_rv=0\), and each sign of \(v\) occurs on exactly

\[
2C,\qquad C=\binom{2m-3}{m-3}
\]

targets. Consequently \(\mu\) has total \(W\), the exact point margins, and

\[
0\le\mu(S)\le3
\le\left\lfloor\frac{m+2}{2}\right\rfloor.
\]

Since at most \(R\) negative cells of \(v\) can receive the high baseline value,

\[
Q_1(\mu)\ge4C-2R.
\]

Exactly,

\[
\boxed{
\frac{Q_1(\mu)}W
\ge
\frac{(m+1)(m-2)}{(2m+1)(2m-1)}
-\frac4{m+2}
=
\frac14-o(1).
}
\]

Rank-isolated selector surjectivity produces an integral signed exact-middle solution with histogram \(\mu\). It does not produce a Boolean exact factor.

The precise unproved obstruction lemma is:

> Infinitely many \(m\) admit an exact factor \(F_m\) with first-shadow histogram \(\mu\) above and
> \[
> U_{F_m}\cap\tau U_{F_m}=\langle\mathbf1\rangle
> \]
> for every transposition \(\tau\).

The intersection condition is exactly connectedness of every ownership overlay. If realized, every legal move would merely relabel \(F_m\), making it cut-local, while

\[
\frac{\mathcal Q_A(F_m)}
{H_A\operatorname{Cat}_m}
\ge
\left(\frac1{2A}+o(1)\right)\sqrt m\to\infty.
\]

That would genuinely disprove \(LM_A\). No proved construction realizes it.

The canonical MSW factor does not: its \((2\,3)\)-overlay has
\(\sum_{j=0}^{m-2}\operatorname{Cat}_j>1\) components, and its proved all-dimensional hole family has only \(\operatorname{Cat}_{m-4}\) members, below the \(H_A\operatorname{Cat}_m\) scale.

### Final status

The decisive identities and constants were independently rederived and sign-audited. They confirm:

\[
\boxed{\text{\(LM_A\) is neither proved nor refuted.}}
\]

A proof now requires a genuinely exact-factor fragmentation/locking theorem excluding simultaneous high-energy component restitution. A counterexample requires the Boolean rigid-realization lemma above. Signed selectors, raw extension geometry, cut-cone inequalities, and the currently proved MSW structure supply neither.

If \(LM_A\) is eventually proved, it yields fixed-window unlabelled overload and hence MWB; it does not by itself yield labelled common-owner synchronization.
