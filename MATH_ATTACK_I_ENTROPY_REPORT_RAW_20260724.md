# Raw lead report: signed-subcube entropy repair

## Verdict

This route does **not** prove the contiguous-OR width conjecture. The signed-subcube functional can repair ordinary set holes directly, but it does not control multiplicities, owner labels, or extendibility to one common balanced nested resolution. The fixed-window reduction makes this gap exact.

The strongest outcome is:

1. sharp entropy and Fourier obstructions for signed-subcube repair;
2. a theorem-level analysis of the only known asymptotic MSW hole family;
3. an exact reduction of common-owner synchronization to sequential sparse graph-orientation problems;
4. a precise smallest unresolved rank-local obstruction and a precise sufficient common-flow lemma.

### 1. Signed-subcube entropy theorem

Let \(\mathcal H=\bigsqcup_q\mathcal H_q\) be the lower holes of an exact factor, and \(M_q=|\mathcal H_q|\).

For disjoint anchors \(P,N\), put
\[
U=[n]\setminus(P\cup N),\qquad s=|U|,
\]
and define the opposite faces
\[
\mathcal C(P,N)=
\{P\cup T:T\subseteq U\}\cup
\{N\cup T:T\subseteq U\}.
\]
Complementation exchanges them. Their literal OR-block cost is
\[
\gamma(P,N)=2\nu(s)+\mathbf1_{P\ne\varnothing}
+\mathbf1_{N\ne\varnothing}.
\]

Let \(A\) be hole-versus-face incidence. The Poisson functional is
\[
\Psi(\mathcal H)=
\inf_{\lambda\ge0}
\left[
\gamma^T\lambda+
2\sum_{S\in\mathcal H}e^{-(A\lambda)_S}
\right].
\]

Its exact entropy dual is
\[
\Psi=
\max_{\substack{0\le y\le2\\A^Ty\le\gamma}}
\sum_{S\in\mathcal H}
y_S\left(1+\log\frac2{y_S}\right).
\tag{1}
\]

For arbitrary \(\alpha_q\ge0\) with \(\sum_q\alpha_q\le1\), assigning
\(y_S=\alpha_q\) on \(\mathcal H_q\) is feasible. Indeed, a free-\(s\) face pair meets one rank in at most
\[
2\binom{s}{\lfloor s/2\rfloor}
\le2\nu(s)\le\gamma(P,N)
\]
sets. Therefore
\[
\boxed{
\Psi\ge
\sum_q M_q\alpha_q
\left(1+\log\frac2{\alpha_q}\right).
}
\tag{2}
\]

In particular,
\[
\boxed{\Psi\ge(1+\log2)\max_qM_q}
\tag{3}
\]
and, on \(K\) ranks,
\[
\boxed{
\Psi\ge
\frac{1+\log(2K)}K\sum_{q\le K}M_q.
}
\tag{4}
\]

There is also a rank-free certificate. The elementary bound
\[
\binom{s}{\lfloor s/2\rfloor}
\ge\frac{2^s}{\sqrt{2(s+1)}}
\]
shows that
\[
y_S=\frac1{\sqrt{2(n+1)}}
\]
is simultaneously feasible. Hence
\[
\boxed{
\Psi\ge
\frac{1+\log\!\bigl(2\sqrt{2(n+1)}\bigr)}
{\sqrt{2(n+1)}}\sum_qM_q.
}
\tag{5}
\]

For \(n=2m+1\), this implies
\[
\Psi=o(W)
\Longrightarrow
M_q=o(W)\quad\text{for every }q,
\]
and
\[
\sum_qM_q=o\!\left(\frac{W\sqrt m}{\log m}\right).
\tag{6}
\]

Thus cross-depth reuse cannot conceal a linear defect in even one rank.

### 2. No useful Fourier kernel

Writing \(D=P\cup N\), the face-pair indicator has Walsh expansion
\[
\mathbf1_{\mathcal C(P,N)}(x)
=
2^{1-|D|}
\sum_{\substack{T\subseteq D\\|T|\text{ even}}}
(-1)^{|P\cap T|}\chi_T(x).
\tag{7}
\]

Only complement-even modes occur. Conversely, the zero-free-dimension columns
\[
\mathcal C(S,S^c)=\{S,S^c\}
\]
span every complement-even function. Restricting to the lower representative of each complementary pair gives an identity submatrix.

Therefore
\[
\boxed{\ker A^T=\{0\}}
\tag{8}
\]
on the relevant lower-hole space. There is no redundant Fourier direction available for automatic repair; any saving must come from genuinely economical positive-dimensional face covers.

### 3. Actual canonical MSW holes

The only proved asymptotic canonical family is
\[
T(V)=11101101\,V,\qquad V\in\mathcal D_{m-4}.
\]
Every \(T(V)\) is absent from the MSW second-upper map, so
\[
S(V)=\{\infty\}\cup([2m]\setminus T(V))
\]
is an actual depth-one lower hole. Consequently
\[
M_1^{\rm MSW}\ge\operatorname{Cat}_{m-4}
=\left(\frac1{512m}+o(m^{-1})\right)W.
\tag{9}
\]

This family is Catalan-sparse, not Boolean-cube dense. Fixing the forced prefix and the first/last bits of \(V\) places it inside one face pair with free dimension \(2m-10\). That block costs at least
\[
2\binom{2m-10}{m-5}
=\left(\frac1{1024}+o(1)\right)W,
\tag{10}
\]
whereas literal complementary repair costs only
\[
2\operatorname{Cat}_{m-4}
=\left(\frac1{256m}+o(m^{-1})\right)W.
\tag{11}
\]

Thus treating the Dyck suffix as a free Boolean cube loses a factor \(\Theta(m)\). The known hereditary MSW geometry supplies no useful subcube compression.

The first unavoidable canonical lemma is therefore:

> **UNPROVED rank-one lemma**
> \[
> \boxed{M_1(F_m^{\rm MSW})=o(W).}
> \tag{12}
> \]

It is necessary by (3). No theorem currently proves either (12) or the opposite assertion \(M_1^{\rm MSW}=\Omega(W)\). Finite positive-density data cannot decide this asymptotic question.

### 4. Fixed-window exact-ownership obstruction

Fix \(A>0\) and \(K=\lceil A\sqrt m\rceil\). Uniformly for \(q\le K\),
\[
\log\frac W{N_q}
=\frac{q(q+1)}m+O_A(m^{-1/2}),
\]
so
\[
1\le c_q\le C_A.
\tag{13}
\]

Therefore
\[
\boxed{
\sum_{q\le K}\frac{e_q}{c_q}=o(W)
\iff
\sum_{q\le K}e_q=o(W).
}
\tag{14}
\]

For any common balanced nested resolution \(P\), let
\(b_q(S)=|P_q^{-1}(S)|\). At most
\(\min\{b_q(S),\mu_q(S)\}\) owners assigned to \(S\) can agree, so
\[
e_q(F,P)\ge
\sum_S(b_q(S)-\mu_q(S))_+
=\frac12\|b_q-\mu_q\|_1
\ge c_qM_q.
\tag{15}
\]

Consequently
\[
(\mathrm{CA}_A)
\Longrightarrow
\sum_{q\le K}M_q=o(W)
\Longrightarrow
\Psi\le2\sum_{q\le K}M_q=o(W).
\tag{16}
\]

The converse fails. Signed-subcube repair sees only whether \(\mu_q(S)=0\); it sees neither positive-load quota deficits nor owner identities. Hence it is downstream of synchronization, not a bridge to it.

There is an additional necessary owner constraint. Let \(D_t^P(z)\) count owners whose \(t\)-th deletion under \(P\) is coordinate \(z\). The canonical wreath deletion order deletes every coordinate exactly \(W/n\) times at every position. Agreement at depths \(t-1,t\) forces agreement of the \(t\)-th deletion label, giving
\[
\boxed{
\left\|D_t^P-\frac Wn\mathbf1\right\|_1
\le2(e_{t-1}+e_t).
}
\tag{17}
\]
Thus \((\mathrm{CA}_A)\) also forces
\[
\sum_{t\le K}
\left\|D_t^P-\frac Wn\mathbf1\right\|_1=o(W).
\tag{18}
\]
Balanced node fibers alone do not enforce these stepwise coordinate margins.

### 5. Exact common-flow reduction by deletion diamonds

There is nevertheless an exact rank-isolated operation.

Extend every owner chain through depth \(K+1\). Process \(q=1,\ldots,K\). At stage \(q\), each owner has
\[
P_{q+1}(X)\subset P_{q-1}(X),\qquad
|P_{q-1}(X)\setminus P_{q+1}(X)|=2.
\]
There are exactly two possible intermediate \(q\)-sets. Make them the endpoints of an edge \(e_X\) in a multigraph \(G_q\) on
\(\binom{[n]}{m-q}\).

Choosing the other endpoint is exactly an adjacent swap of the \(q\)-th and \((q+1)\)-st deletion positions. It changes depth \(q\) and no other depth.

For a prescribed load vector \(b_q\), an endpoint assignment exists exactly when
\[
b_q(V(G_q))=W
\]
and, for every vertex family \(U\),
\[
\boxed{
e_{G_q}(U)\le b_q(U)
\le e_{G_q}(U)+|\delta_{G_q}(U)|.
}
\tag{19}
\]
This is the capacitated edge-to-endpoint Hall theorem; the second inequality is the first applied to the complement.

Earlier swaps leave the unprocessed \(q\)-set canonical, and later swaps never alter depth \(q\). Hence if \(f_q\) edges are toggled at stage \(q\), then exactly
\[
e_q=f_q.
\tag{20}
\]

Sequential feasible orientations therefore automatically produce one common integral nested resolution—never independent rank quotas.

This gives the smallest concrete sufficient replacement exposed by the route:

> **UNPROVED dynamic diamond-orientation lemma.**  
> For every fixed \(A\), jointly choose one exact factor \(F_m\) and sequential balanced loads
> \[
> b_q(S)\in\{c_q,c_q+1\},\qquad q\le A\sqrt m,
> \]
> satisfying every dynamic cut condition (19), such that their minimum total toggle cost obeys
> \[
> \boxed{\sum_{q\le A\sqrt m}\frac{f_q}{c_q}=o(W).}
> \tag{21}
> \]

By (20), this proves \((\mathrm{CA}_A)\); fixed-window diagonalization then proves SYNC and the final asymptotic OR bound.

The remaining obstruction is real. Each \(G_q\) has only
\[
|E(G_q)|=W,\qquad
\frac{2|E(G_q)|}{|V(G_q)|}
=\frac{2W}{N_q}=O_A(1),
\]
so it is sparse. At \(q=1\), \(c_1=1\). Taking \(U\) to be a connected component in (19) shows
\[
|E(U)|\ge|U|.
\tag{22}
\]
Every tree or isolated component is therefore fatal to one-stage balancing. Even when all Hall cuts hold, they do not bound the minimum toggle cost; moving one unit along a long alternating path may cost many flips. Moreover \(G_q\) depends on all earlier choices.

Canonical MSW hole recursion currently proves neither these Hall inequalities nor the \(o(W)\) min-cost estimate.

### Adversarial audit

The strongest claims were independently rederived by separate audits. The following qualifications are essential:

- The entropy lower bounds concern the Poisson surrogate \(\Psi\), not the unrestricted deterministic repair optimum.
- A large lower bound on \(\Psi\) therefore does not prove that every deterministic OR repair is expensive.
- The positive-density finite MSW ledgers were not used as asymptotic evidence.
- Hole support alone cannot determine overload; any abstract histogram demonstrating this is not claimed to be exact-factor realizable.
- The diamond construction requires the canonical \(K+1\)-st layer.
- Hall feasibility and low toggle cost are separate requirements.
- The evolving graphs depend on previous orientations.
- No independently chosen adjacent-rank quota vector is used.
- The factor-independent deep overload tail does not remove the fixed-window Hall/min-cost obstruction.

So the route is genuinely exhausted at two precise points: the canonical rank-one condition (12), and—if exact ownership is retained—the dynamic common-flow lemma (21).

