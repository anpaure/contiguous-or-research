In this lane write \(W=\binom{2m}{m}\). The verdict is: \(\mathrm{RSCD}_A\) remains unproved, but the full-SCD extension issue is now completely resolved, the path-cover problem has an exact Hall formulation, and two large construction classes are sharply separated:

- cut odd wreaths give an exact \(o(W)\)-toll rotor skeleton, with only a nested shadow-matching theorem missing;
- every construction confined to one fixed coordinate-pair system has toll \(\Omega_A(W)\), so native Bender–Knuth cubes and stationary pair recursion cannot work.

## 1. Exact band-extension theorem

**Theorem.** Every saturated symmetric-chain decomposition of the central band

\[
\bigcup_{j=m-H}^{m+H}\binom{[2m]}j
\]

extends integrally to a full SCD of \(B_{2m}\), preserving every band member and every band chain.

**Proof.** Suppose ranks \(r=m-q,\ldots,2m-r=m+q\) are already decomposed. Let \(Y\) be the chains meeting both boundary ranks, with endpoints

\[
A_y\in\binom{[2m]}r,\qquad B_y\in\binom{[2m]}{2m-r}.
\]

The correlation \(A_y\leftrightarrow B_y\) is arbitrary. Put

\[
X=\binom{[2m]}{r-1},\qquad
Z=\binom{[2m]}{2m-r+1},
\]

and form a bipartite graph with sides \(X\sqcup Y^{-}\) and \(Z\sqcup Y^{+}\). Its edges are

\[
x\sim y^+\iff x\subset A_y,\qquad
y^-\sim z\iff B_y\subset z,
\]

together with the identity edge \(y^-y^+\).

Let

\[
\alpha=m+q+1,\qquad \beta=m-q.
\]

Give comparison edges weight \(1/\alpha\) and identity edges weight

\[
1-\frac{\beta}{\alpha}=\frac{2q+1}{m+q+1}.
\]

Every \(x\) and \(z\) has \(\alpha\) comparison neighbours; every \(y^\pm\) has \(\beta\). Hence every row and column sum is one. The support therefore satisfies Hall and has an integral perfect matching.

An identity-matched \(y\) stops at depth \(q\). Otherwise unique \(x,z\) extend it to

\[
x\subset A_y\subset\cdots\subset B_y\subset z.
\]

All new outer sets occur once and symmetry is preserved. Iterating \(q=H,\ldots,m-1\) proves the theorem. ∎

Consequently, \(\mathrm{RSCD}_A\) is exactly equivalent to its central-band version. Constructing an integral band SCD is enough; no additional outer extendibility lemma is needed.

## 2. Exact ordered-Hall characterization

Fix an exact band SCD \(\mathcal D\). For radius class \(d\), let \(R_d\) be its directed rotor graph. For a total order \(\prec\) on its vertices, retain only forward arcs and let

\[
\operatorname{def}_d(\prec)
=\max_{S}\bigl(|S|-|N_\prec^+(S)|\bigr).
\]

Then the minimum possible number of components in a spanning directed rotor path forest is exactly

\[
\boxed{
p_d^*(\mathcal D)=\min_\prec\operatorname{def}_d(\prec).
}
\]

Indeed, a maximum bipartite matching in the forward arcs gives indegree and outdegree at most one. Strict increase forbids directed cycles; under these degree bounds any undirected cycle would necessarily be directed. Conversely, topologically ordering any path forest makes all its arcs forward.

Thus

\[
\boxed{
\Phi_{\min}(\mathcal D)
=\sum_{d=0}^H(2d+1)
 \min_{\prec_d}\max_S
 \bigl(|S|-|N_{\prec_d}^+(S)|\bigr).
}
\]

There is also an exact multirank deficiency identity. Put

\[
P_q=\sum_{d=q}^H p_d.
\]

Selected rotor arcs from classes \(d\ge q\) induce an inclusion matching between ranks \(m-q\) and \(m+q\) of size \(N_q-P_q\). Moreover,

\[
\boxed{
\Phi=P_0+2\sum_{q=1}^H P_q.
}
\]

The inclusion matchings are necessary but not sufficient by themselves: they must arise coherently from one band SCD and the same rotor arcs.

## 3. Exact odd-cut rotor skeleton

Cut any exact odd wreath factor at a distinguished coordinate \(\infty\). This gives

\[
B=\operatorname{Cat}_m=\frac{W}{m+1}
\]

vertex-disjoint complementary Johnson paths

\[
P=(X_0,\ldots,X_m),\qquad X_m=X_0^c,
\]

partitioning the even middle layer. Their \(mB=N_1\) edge-unions partition rank \(m+1\).

Write

\[
a_t=X_t\setminus X_{t+1},\qquad
b_t=X_{t+1}\setminus X_t,
\]

and

\[
w=(a_0,\ldots,a_{m-1},b_0,\ldots,b_{m-1}).
\]

Then \(X_t=I_w(t,m)\). Define

\[
L_q(t)=I_w(t+q,m-q),\qquad
U_q(t)=I_w(t-q,m+q).
\]

The radius-\(d\) chain at \(X_t\) has state

\[
\left(
I_w(t+d,m-d);
w_{t+d-1},\ldots,w_{t-d};
I_w(t+m,m-d)
\right).
\]

For \(d\ge1\), the transition \(t\to t+1\) is exactly the rotor successor with

\[
x=w_{t+d},\qquad y=w_{t+m};
\]

for \(d=0\) it is the corrected ordinary swap. Hence every constant-radius segment is a literal directed rotor path.

Let

\[
n_d=N_d-N_{d+1}\quad(d<H),\qquad n_H=N_H.
\]

Concatenating the \(B\) paths and assigning the labels \(d\) in contiguous chunks of sizes \(n_d\) gives

\[
p_d\le\frac{n_d}{m+1}+2.
\]

Since

\[
U_H:=\sum_{d=0}^H(2d+1)n_d
=W+2\sum_{q=1}^H N_q,
\]

the formal toll is

\[
\Phi_{\rm cut}
\le \frac{U_H}{m+1}+2(H+1)^2
=O_A(W/\sqrt m)+O_A(m)=o(W).
\]

Thus radius arithmetic, path length, and rotor chronology are solved.

What is not automatic is the band SCD. For \(A_q=\{v:r(v)\ge q\}\), the interval chains partition the band exactly iff, for every \(q\le H\),

\[
v\mapsto L_q(v),\qquad v\mapsto U_q(v)
\]

are bijections onto ranks \(m-q,m+q\). Equivalently, the labelled edges \(L_q(v)U_q(v)\), \(v\in A_q\), form nested perfect matchings.

A convenient exact formulation uses binary variables

\[
x_{v,0}=1,\qquad x_{v,q+1}\le x_{v,q},
\]

with constraints

\[
\sum_{v:L_q(v)=S}x_{v,q}=1,\qquad
\sum_{v:U_q(v)=T}x_{v,q}=1.
\]

Putting \(z_{v,d}=x_{v,d}-x_{v,d+1}\), the same-label path edges determine \(p_d\) exactly. The following is therefore the explicit surviving lemma.

> **Cut-path nested-shadow lemma — UNPROVED.**  
> For every fixed \(A>0\), some exact odd wreath factor admits an integral solution of the displayed nested system with
> \[
> \sum_{d\le H}(2d+1)p_d=o(W),
> \qquad H=\lceil A\sqrt m\rceil.
> \]

The band-extension theorem would then produce the required one integral full SCD.

A useful anchoring puts radius zero at \(X_0\) of every path. The upper depth-one bijection is then automatic:

\[
U_1(X_t)=X_{t-1}\cup X_t,\qquad 1\le t\le m.
\]

The lower depth-one family remains a genuine rainbow requirement; the exact odd factor alone does not supply it.

## 4. Fixed-pair constructions have a Gaussian \(\Omega(W)\) barrier

Fix a perfect coordinate matching \(\mathcal P\), and suppose every selected rotor arc flips one pair of \(\mathcal P\).

For a rank-\((m-q)\) target with \(f\) full pairs, put

\[
T_{f,q}
=\frac{m!}{f!(f+q)!(m-2f-q)!}\,2^{m-2f-q},
\]

while the number of middle starts of source type \(f\) is

\[
V_f
=\frac{m!}{f!^2(m-2f)!}\,2^{m-2f}.
\]

Define the exact type deficit

\[
D_{m,q}=\sum_f(T_{f,q}-V_f)_+.
\]

A path of \(t\) chains reaching depth \(q\) has \((t-q)_+\) starts with \(q\) following rotor arcs. Their lower depth-\(q\) members are \(q\)-face shadows of \(q\) distinct \(\mathcal P\)-pairs. Hence, with \(P_q=\sum_{d\ge q}p_d\),

\[
N_q-qP_q\le\sum_f\min(T_{f,q},V_f)=N_q-D_{m,q},
\]

so

\[
\boxed{qP_q\ge D_{m,q}.}
\]

For \(q=x\sqrt m+o(\sqrt m)\), let \(\Phi_{\rm G}\) be the standard normal CDF and define

\[
\Delta(x)
=\Phi_{\rm G}(x/2)-e^{x^2}\Phi_{\rm G}(-3x/2)>0.
\]

Uniform Stirling/local-CLT expansion gives

\[
\frac{D_{m,q}}W\longrightarrow e^{-x^2}\Delta(x).
\]

The decisive ratio calculation is

\[
\frac{T_{f,q}}{V_f}
=\prod_{i<q}\frac{m-2f-i}{2(f+1+i)},
\]

and, for \(f=m/4+X\sqrt m\),

\[
\log\frac{T_{f,q}}{V_f}
=-8xX-3x^2+o(1),
\qquad
X\Rightarrow N(-x/2,1/16).
\]

Therefore, for every \(0<a<A\),

\[
\boxed{
\liminf_{m\to\infty}\frac{\Phi}{W}
\ge
2\int_a^A
\frac{e^{-x^2}\Delta(x)}x\,dx
>0.
}
\]

So no one-fixed-pair rotor architecture proves \(\mathrm{RSCD}_A\). This includes the native Bender–Knuth cube partition and stationary pair-coordinate product recursion. It also shows that sparse surgery cannot repair them: a linear number of centers must be rebundled through genuinely mixed coordinate systems.

At the local \(C\times B_2\) level, the shuffle automaton does contain noncanonical within-box rotor mergers, but the stationary two-lane lift still leaves at least one radius-\(d\) component per parent-chain vertex. Whether changing phases and mixing pair frames yields a contracting recursion remains **unproved**; the fixed-pair theorem rules out only the unmixed version.

## Final status

Proved and independently audited:

1. every exact central-band SCD extends to one full integral SCD;
2. the exact ordered-Hall formula for \(p_d^*\);
3. the deficiency identity \(\Phi=P_0+2\sum_{q\ge1}P_q\);
4. the exact odd-cut rotor skeleton with formal toll \(o(W)\);
5. the Gaussian \(\Omega(W)\) obstruction for one fixed pair frame.

Still unproved:

\[
\boxed{\text{one integral nested two-sided shadow matching with }o(W)\text{ rotor toll}.}
\]

This remains a direct even-dimensional OR route. It does not prove odd MWB, labelled \(CA_A\), or any overload-to-labelled converse.
