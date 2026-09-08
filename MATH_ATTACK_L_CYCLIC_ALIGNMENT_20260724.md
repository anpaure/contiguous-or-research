# Lane L: cyclic alignment inside one exact wreath factor

Date: 2026-07-24

Method: pure mathematics only. No web search, finite search, or solver was used.

## 0. Outcome

The lane does not prove \(\mathrm{CA}_A\), labelled synchronization, or MWB. It does produce four principal structural advances, two combinatorial obstructions, and one closed heat proposal.

The advances are:

1. the fixed-factor one-pass alignment problem has an exact integral Hall–Bellman formulation, with no independent per-depth choice;
2. for every fixed Gaussian window, balanced quota vectors can be chosen point-regular at every rank;
3. along a point-regular adaptive trajectory, all owner toggles are forced into directed coordinate cycles;
4. orbit averaging admits exact integral arcwise rounding, but the orbit projection is universal and erases all owner/factor correlations.

The two geometric obstructions are:

1. a cyclic flow that remains perfect inside each individual wreath row is rigid: it can only apply a common phase to the whole row and cannot rebalance its histogram;
2. every nontrivial exact-factor \(C_8\) trade, in the asymptotic range \(m\ge3\), has the universal path profile
   \[
   3,n-3,3,n-3.
   \]
   Hence repair of a fixed positive density of depth-one defect by \(C_8\) moves requires \(\Omega(W)\) steps and \(\Theta(m)\) average reuse of a fixed set of \(B\) bookkeeping slots. This is not a claim that the same wreath supports recur, since a chain can introduce new wreaths. Factorially many rooted partners do not form a simultaneously applicable packing reservoir.

The corrected heat-switch ledger is also incorporated. Exact wreath histograms have zero point margins, so the applicable transposition coefficient is \(4(n-1)\), not \(2n\). The old \(2nB_H\) gate is impossible on a fixed Gaussian window. The corrected \(4(n-1)B_H\) target is compatible with the ambient Johnson spectrum, but Boolean-\(E_2\) stability forces an additional \(\Omega_A(nW\sqrt m)\) gap at every same-window global minimizer. Thus that corrected near-baseline gate is also impossible. This closes the heat near-equality route without refuting MWB.

The exact remaining positive gate is a packetized higher-order Hall plus short-recourse theorem along one common adaptive trajectory. A second possible gate is a dense macrotrade cover-down with either low direct orientation frustration or a controlled reoptimization of the nested resolution. Neither is proved here, and no genuine exact-factor obstruction to either one is constructed.

## 1. Fixed-window normalization and the strength of alignment

Put

\[
n=2m+1,\qquad
W=\binom nm,\qquad
B=\frac Wn=\operatorname{Cat}_m,
\]

For a cyclic order \(\pi=(\pi_0,\ldots,\pi_{n-1})\), with indices modulo \(n\), write

\[
I_\pi(j,r)=\{\pi_j,\pi_{j+1},\ldots,\pi_{j+r-1}\}.
\]

A wreath is the row of its \(n\) length-\(m\) cyclic intervals. An exact middle wreath factor consists of \(B=W/n\) such rows whose length-\(m\) intervals partition \(\binom{[n]}m\). Thus every middle set has one unique pointed occurrence \(X=I_\pi(j,m)\).

\[
N_q=\binom n{m-q},\qquad
\lambda_q=\frac W{N_q},\qquad
c_q=\lfloor\lambda_q\rfloor,
\]

and, for fixed \(A>0\),

\[
K=K_A=\lceil A\sqrt m\rceil.
\]

Uniformly for \(1\le q\le K\),

\[
\log\lambda_q
=\frac{q(q+1)}m+O_A(m^{-1/2}),
\]

so, after enlarging \(C_A\) if necessary, for all sufficiently large \(m\),

\[
1\le c_q\le\lambda_q\le C_A
\]

for a constant depending only on \(A\). Moreover,

\[
S_A(m):=\sum_{q=1}^{K}\frac1{c_q}
=\left(s_A+o_A(1)\right)\sqrt m,
\qquad
s_A=\int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor},
\tag{1.1}
\]

and

\[
T_A(m):=\sum_{q=1}^{K}\frac q{c_q}
=\left(t_A+o_A(1)\right)m,
\qquad
t_A=\int_0^A\frac{x\,dx}{\lfloor e^{x^2}\rfloor}.
\tag{1.2}
\]

An orientation of every wreath in an exact factor \(F\) gives each middle owner \(X\in\binom{[n]}m\) a canonical deletion word and hence a canonical lower flag \(L_q^F(X)\in\binom{[n]}{m-q}\). Define its depth histogram by

\[
\mu_q^F(S)=\#\{X:L_q^F(X)=S\}.
\]

Writing \(d_{q,S}=\mu_q^F(S)-c_q\), define the exact balanced overload

\[
O_q(F)=\max\left\{
\sum_S(-d_{q,S})_+,
\sum_S(d_{q,S}-1)_+
\right\}.
\tag{1.3}
\]

An integral balanced nested resolution assigns to every owner a flag

\[
X=P_0(X)\supset P_1(X)\supset\cdots\supset P_K(X),
\qquad |P_q(X)|=m-q,
\]

such that every rank-\((m-q)\) set is used either \(c_q\) or \(c_q+1\) times. For such a resolution \(P\), put

\[
e_q(F,P)=\#\{X:P_q(X)\ne L_q^F(X)\}.
\]

For an oriented exact factor \(F\) and one balanced nested resolution \(P\), define

\[
E_A(F,P)
=\sum_{q=1}^{K}\frac{e_q(F,P)}{c_q},
\qquad
J_A(F)=\min_P E_A(F,P).
\tag{1.4}
\]

Since the capacities are bounded,

\[
E_A(F,P)=o(W)
\quad\Longleftrightarrow\quad
\sum_{q=1}^{K}e_q(F,P)=o(W).
\tag{1.5}
\]

This is stronger than an average owner-depth statement. Let

\[
\mathcal E(F,P)
=\{X:\text{there is some }1\le q\le K
\text{ with }P_q(X)\ne L_q^F(X)\}.
\]

Then

\[
|\mathcal E(F,P)|
\le\sum_{q=1}^{K}e_q(F,P).
\tag{1.6}
\]

Thus a successful aligned pair has a common canonical owner core of size

\[
W-o(W)
\]

through the entire Gaussian window. It is not enough to choose good factors or good quotas separately at each depth.

### 1.1 A necessary deletion-margin invariant

Let \(a_t^F(X)\) be the \(t\)-th canonical deletion letter of owner \(X\), and let

\[
d_t^P(X)=P_{t-1}(X)\setminus P_t(X).
\]

Define its deletion histogram by

\[
D_t^P(z)=\#\{X:d_t^P(X)=z\}.
\]

For every coordinate \(z\), a wreath row uses \(z\) exactly once at every fixed deletion position. Therefore

\[
\#\{X:a_t^F(X)=z\}=B.
\tag{1.7}
\]

If \(P\) agrees with \(F\) at depths \(t-1\) and \(t\), it also agrees on the \(t\)-th deleted coordinate. Changing one owner's deletion coordinate changes the deletion histogram in \(\ell^1\) by at most two. With \(e_0=0\),

\[
\boxed{
\left\|
\bigl(\#\{X:d_t^P(X)=z\}\bigr)_{z\in[n]}
-B\mathbf1
\right\|_1
\le2(e_{t-1}+e_t).
}
\tag{1.8}
\]

Consequently,

\[
E_A(F,P)=o(W)
\quad\Longrightarrow\quad
\sum_{t=1}^{K}
\left\|D_t^P-B\mathbf1\right\|_1=o(W).
\tag{1.9}
\]

Ordinary balanced-node flow does not impose (1.9). It is a colored, owner-step invariant that any genuine alignment theorem must recover.

## 2. Exact one-pass owner state

Fix one oriented exact factor \(F\) throughout this section. For owner \(X\), extend its canonical deletion word to

\[
a_1^X,\ldots,a_{K+1}^X,
\qquad
L_q(X)=X\setminus\{a_1^X,\ldots,a_q^X\}.
\]

Assume \(K+1\le m\), which holds for fixed \(A\) and large \(m\).

Process stages \(q=1,\ldots,K\) once in ascending order. At stage \(q\), either retain or transpose the current letters in positions \(q,q+1\). Write
\(\varepsilon_q(X)=1\) for a toggle and define the carried letter by

\[
\kappa_1(X)=a_1^X,
\]

\[
\kappa_{q+1}(X)=
\begin{cases}
\kappa_q(X),&\varepsilon_q(X)=1,\\
a_{q+1}^X,&\varepsilon_q(X)=0.
\end{cases}
\tag{2.1}
\]

Then the chosen depth-\(q\) target is exactly

\[
\boxed{
P_q(X)=L_{q+1}(X)\cup\{\kappa_{q+1}(X)\}.
}
\tag{2.2}
\]

Immediately before stage \(q\), the two legal endpoints are

\[
u_X=L_q(X)
=L_{q+1}(X)\cup\{a_{q+1}^X\},
\]

\[
v_X=L_{q+1}(X)\cup\{\kappa_q(X)\}.
\tag{2.3}
\]

They are distinct because
\(\kappa_q(X)\in\{a_1^X,\ldots,a_q^X\}\).
Their intersection and union are

\[
u_X\cap v_X=L_{q+1}(X),
\qquad
u_X\cup v_X=P_{q-1}(X).
\tag{2.4}
\]

Later stages do not change the chosen depth-\(q\) set, and therefore

\[
\boxed{
e_q(F,P)=T_q
:=\#\{X:\varepsilon_q(X)=1\}.
}
\tag{2.5}
\]

All chosen sets come from one final deletion word per owner, so they form one integral common nested resolution. No rankwise gluing is hidden here.

Consecutive toggled stages \(s,\ldots,t-1\) rotate deletion-word positions
\([s,t]\). This is the correct run/block indexing.

## 3. Exact Hall–Bellman formulation

For a reachable carried-letter state \(\kappa=(\kappa_X)_X\), so that

\[
\kappa_X\in\{a_1^X,\ldots,a_q^X\}
\qquad\text{for every }X,
\]

let \(G_q(\kappa)\) be the owner-labelled loopless multigraph on
\(\binom{[n]}{m-q}\) containing the edge \(u_Xv_X\) from (2.3) for every owner.

Orienting toward \(u_X\) means no toggle; orienting toward \(v_X\) means toggle. The indegrees are exactly the depth-\(q\) loads.

### 3.1 Prescribed and mobile Hall cuts

For a prescribed integral quota \(b_q\) of total \(W\), an orientation with indegree vector \(b_q\) exists if and only if, for every vertex family \(U\),

\[
\boxed{
i_q(U)\le b_q(U)
\le i_q(U)+|\partial_q(U)|.
}
\tag{3.1}
\]

Here \(i_q(U)\) counts internal owner edges with multiplicity, while \(|\partial_q(U)|\) counts, with multiplicity, owner edges having exactly one endpoint in \(U\). This is the integral owner-edge-to-endpoint flow theorem.

Writing

\[
W=c_qN_q+\rho_q,
\]

an orientation with every load in
\(\{c_q,c_q+1\}\), with the high vertices free, exists if and only if

\[
\boxed{
i_q(U)\le(c_q+1)|U|,
\qquad
i_q(U)\le c_q|U|+\rho_q
}
\tag{3.2}
\]

for every \(U\). The second inequality is the complement form of the lower-capacity cut.

For a fixed prescribed \(b_q\), the minimum immediate toggle cost is obtained from the directed incidence matrix \(B_D\) whose owner-\(X\) column is \(\mathbf e_{v_X}-\mathbf e_{u_X}\):

\[
\tau_q(\kappa,b_q)
=
\min\left\{
\mathbf1^\top x:
B_Dx=b_q-\mu_q^F,\quad
0\le x\le1
\right\}.
\tag{3.3}
\]

The optimum is integral. It is not valid to minimize (3.3) greedily at every stage: two orientations having the same current cost and load can create different carried-letter states and different future graphs.

### 3.2 Exact Bellman recursion

Let \(\mathcal B_q(\kappa)\) be the set of balanced orientations of
\(G_q(\kappa)\), decided exactly by (3.2). An orientation \(\mathcal O\) has toggle count \(T(\mathcal O)\) and produces a next state \(\kappa'\) through (2.1).

Put

\[
R_{K+1}^F(\kappa)=0
\]

and recursively define

\[
\boxed{
R_q^F(\kappa)
=
\min_{\mathcal O\in\mathcal B_q(\kappa)}
\left[
\frac{T(\mathcal O)}{c_q}
+R_{q+1}^F(\kappa')
\right],
}
\tag{3.4}
\]

with value \(+\infty\) when the Hall family is empty. It is defined only on reachable states as above; equivalently, assign value \(+\infty\) to every invalid state.

Then

\[
\boxed{
R_1^F\bigl((a_1^X)_X\bigr)
=
\min_{\substack{P\text{ reachable by}\\
\text{one ascending swap pass}}}
\sum_{q=1}^{K}\frac{e_q(F,P)}{c_q}.
}
\tag{3.5}
\]

This is an exact integral characterization. It makes no separate per-depth choice.

Equivalently, one may choose one binary word
\(\varepsilon\in\{0,1\}^K\) for every owner, use the induced interval-composition path, impose all rank capacities simultaneously, and minimize
\(\sum_q\varepsilon_q/c_q\). The resulting configuration ILP is exactly equivalent to (3.4). It is only the one-pass class, not the unrestricted class of all downward flags. Already at \(K=2\), the natural generic configuration matrix can contain a determinant-\(2\) minor; no generic TU claim is available.

## 4. Point-regular balanced quota families

The point-margin obstruction can be removed rankwise.

### Theorem 4.1 — cyclic point-regular quotas

For every fixed \(A>0\), all sufficiently large \(m\), and every
\(0\le q\le K_A\), there is a cyclically invariant family

\[
\mathcal H_q\subseteq\binom{[n]}{r},
\qquad r=m-q,
\]

of size

\[
|\mathcal H_q|=\rho_q=W-c_qN_q.
\]

Consequently

\[
b_q(S)=c_q+\mathbf1_{\mathcal H_q}(S)
\tag{4.1}
\]

is balanced and has the exact point margins

\[
\boxed{
\sum_{S\ni x}b_q(S)=\frac{rW}{n}=rB
\qquad(x\in[n]).
}
\tag{4.2}
\]

#### Proof

Let

\[
g=\gcd(n,r).
\]

Since \(n\) is odd,

\[
g=\gcd(n,2r)
=\gcd(n,2q+1),
\tag{4.3}
\]

so \(g\le2q+1=O_A(\sqrt m)\). Let \(C_n\) act on \(r\)-sets by cyclic coordinate rotation.

If a set has stabilizer order \(h\), then \(h\mid n\) and \(h\mid r\), hence \(h\mid g\). Every orbit length is therefore a multiple of

\[
L:=\frac ng.
\]

In particular \(L\mid N_q\). Also \(n\mid W\), so \(L\mid W\) and hence

\[
L\mid\rho_q,\qquad L\mid(N_q-\rho_q).
\tag{4.4}
\]

Put

\[
e=\min(\rho_q,N_q-\rho_q)
\]

and write uniquely

\[
e=an+bL,\qquad a\ge0,\quad0\le b<g.
\tag{4.5}
\]

There are enough full length-\(n\) orbits. A nontrivially stabilized \(r\)-set is invariant under the unique subgroup of some order
\(h>1\) dividing \(g\), and is determined by \(r/h\) of the \(n/h\) subgroup-orbits. Because \(n\) is odd, \(h\ge3\), so

\[
\#\{\text{nonfull-orbit }r\text{-sets}\}
\le
\sum_{\substack{h\mid g\\h>1}}
\binom{n/h}{r/h}
\le\tau(g)2^{n/3}
=o_A(N_q).
\tag{4.6}
\]

Here \(N_q=W/\lambda_q\ge W/C_A\ge2^n/[C_A(n+1)]\). Thus more than \(N_q/2\) sets lie in full orbits for large \(m\), while
\(an\le e\le N_q/2\).

There are also enough exact length-\(L\) orbits. Put

\[
k=\frac rg.
\]

Then \(\gcd(L,k)=1\). Every binary word of length \(L\) and weight \(k\) is primitive: a proper repetition number would divide both \(L\) and \(k\). Repeating it \(g\) times gives an \(r\)-set with stabilizer exactly \(g\). Thus the number of length-\(L\) orbits is

\[
\frac1L\binom Lk.
\tag{4.7}
\]

Uniformly in the fixed window,

\[
L=\Omega_A(\sqrt m),
\qquad
\frac{k}{L}=\frac rn\in[1/3,1/2)
\]

for large \(m\), so (4.7) exceeds \(g\). Select \(a\) full orbits and \(b\) length-\(L\) orbits. Their union \(\mathcal E\) is invariant and has size \(e\). If \(\rho_q\le N_q/2\), take
\(\mathcal H_q=\mathcal E\); otherwise take its complement in the full \(r\)-layer.

Cyclic invariance makes every point degree equal. Double counting gives degree

\[
\frac{r\rho_q}{n}.
\]

Finally,

\[
c_q\binom{n-1}{r-1}
+\frac{r\rho_q}{n}
=\frac{r(c_qN_q+\rho_q)}n
=\frac{rW}{n},
\]

which proves (4.2). \(\square\)

### Scope

The theorem is rankwise. It does not show that the independently constructed
\(\mathcal H_q\) satisfy adjacent-rank clone Hall conditions, arise from one nested resolution, or are orientable in the owner graphs of one factor.

It does show that exact point regularity is not the missing rankwise obstruction.

## 5. The coordinate-cycle synchronization law

At stage \(q\), attach to owner \(X\) the directed label arc

\[
a_{q+1}^X\longrightarrow\kappa_q(X).
\tag{5.1}
\]

Toggling that owner changes its point-incidence vector by

\[
\mathbf e_{\kappa_q(X)}
-\mathbf e_{a_{q+1}^X}.
\tag{5.2}
\]

Let \(\mathscr D_q\) be the directed owner-labelled multigraph on the \(n\) coordinates consisting of all arcs (5.1), and let
\(\mathscr T_q\) be the subgraph of toggled arcs.

The canonical deletion-position histogram is uniform:

\[
\#\{X:a_{q+1}^X=x\}=B.
\tag{5.3}
\]

If

\[
\Delta_{q-1,x}
=
\#\{X:x\in P_{q-1}(X)\}
-(m-q+1)B,
\]

then the carried-letter recurrence gives

\[
\#\{X:\kappa_q(X)=x\}=B+\Delta_{q-1,x}.
\tag{5.4}
\]

Thus, whenever the preceding load has exact point margins,
\(\mathscr D_q\) is \(B\)-regular in both indegree and outdegree.

For the new chosen load,

\[
\boxed{
\Delta_q
=
\sum_{X:\varepsilon_q(X)=1}
\left(
\mathbf e_{\kappa_q(X)}
-\mathbf e_{a_{q+1}^X}
\right).
}
\tag{5.5}
\]

This proves the following exact characterization.

### Theorem 5.1 — cycle-bundled point correction

Assume that the preceding depth-\((q-1)\) load has exact point margins. If the attained balanced depth-\(q\) quota also has exact point margins, then every feasible stage-\(q\) toggle set is an Eulerian directed subgraph of
\(\mathscr D_q\), and hence decomposes into directed coordinate cycles. Conversely, every union of directed cycles preserves the exact point margins.

More generally, an arbitrary toggle set decomposes into edge-disjoint directed trails and cycles; splitting repeated vertices turns the trails into directed paths whose terminal and initial endpoint multiplicities are precisely the positive and negative parts of \(\Delta_q\).

At \(q=1\), the \(n\) arcs contributed by each wreath row form one directed Hamilton cycle on the coordinates. At later stages, carried letters can destroy this rowwise Hamilton identity, but under point-regular preceding loads the global label multigraph remains Eulerian.

Thus a point-regular version of the adaptive Hall theorem is automatically synchronized around coordinate cycles at each stage. This statement supplies neither one common cycle packet across different depths nor higher-order set-load feasibility. The remaining obstruction is higher-order set load and cross-depth synchronization, not point flow.

### Corollary 5.2 — exact deletion margins

If point-regular quotas at every adjacent pair of ranks are attained by the same nested trajectory \(P\), then

\[
\#\{X:d_q^P(X)=x\}
=
(m-q+1)B-(m-q)B
=B
\tag{5.6}
\]

for every coordinate \(x\). Hence the necessary deletion invariant (1.9) holds with zero error.

## 6. Rigidity of perfect flow inside one wreath row

The preceding global cycles should not be confused with independent flow around each wreath.

Fix one cyclic row \(\pi\), write

\[
X_j=I_\pi(j,m),
\]

and suppose every owner is constrained to follow cyclic subintervals

\[
P_q(X_j)
=I_\pi(\phi_q(j),m-q)
\subseteq P_{q-1}(X_j).
\tag{6.1}
\]

Assume that at every depth the row uses every cyclic interval exactly once, so \(\phi_q\) is a permutation of \(\mathbb Z_n\).

Nestedness implies

\[
\phi_{q+1}(j)\in
\{\phi_q(j),\phi_q(j)+1\}.
\tag{6.2}
\]

Relabel owners by the permutation \(\phi_q\). The transition from level \(q\) to \(q+1\) is then a perfect matching in the bipartite cycle with edges

\[
t\longrightarrow t,
\qquad
t\longrightarrow t+1.
\]

This bipartite \(2n\)-cycle has exactly two perfect matchings. If one vertex advances, its successor cannot stay and is forced to advance; propagation around the cyclic index set forces every vertex to advance. Otherwise every vertex stays. Oddness of \(n\) is not needed for this rigidity step.

Therefore there is one common bit \(\delta_q\in\{0,1\}\) such that

\[
\phi_{q+1}(j)=\phi_q(j)+\delta_q
\quad\text{for every }j.
\tag{6.3}
\]

Starting with \(\phi_0(j)=j\), one obtains

\[
\boxed{
\phi_q(j)=j+s_q
\quad\text{for one common phase }s_q.
}
\tag{6.4}
\]

The depth histogram of the row is unchanged by this phase. If \(s_q\ne0\), all \(n\) owners of the row disagree with the canonical prefix at depth \(q\).

### Consequence

A rowwise perfect cyclic flow either does nothing useful to the histogram or pays a whole-row labelled cost. Nontrivial rebalancing must permit collisions/holes within rows, exchange flow across rows, or leave the cyclic-subinterval class. This rules out a naive proof that balances each wreath independently and then concatenates the answers.

## 7. Orbit rebalancing: exact positive theorem and exact erasure

Fix an oriented exact factor \(F\) and average all \(T=n!\) coordinate relabelings with multiplicity.

### 7.1 Universal owner flow

For a fixed middle owner \(X\), every permutation of the \(m\) deletion letters of \(X\) occurs exactly \(T/m!\) times among the canonical flags of the orbit factors. Hence, for every
\(S\subset X\) of size \(m-q\),

\[
\#\{\sigma:L_q^{\sigma F}(X)=S\}
=\frac{T}{\binom mq}.
\tag{7.1}
\]

For a directed Boolean cover \(U\to V\) at deletion step \(q\) with

\[
V\subset U\subseteq X,
\qquad |U|=m-q+1,
\qquad |V|=m-q,
\]

\[
\#\{\sigma:
(L_{q-1}^{\sigma F}(X),L_q^{\sigma F}(X))
=(U,V)\}
=\frac{T}{q\binom mq}.
\tag{7.2}
\]

For a cover not contained in \(X\), this count is zero.

After summing over middle owners, every rank-\((m-q)\) target carries

\[
T\lambda_q,
\]

and every cover edge between ranks \(m-q+1\) and \(m-q\) carries

\[
\frac{T\lambda_q}{m+q+1}
=\frac{T\lambda_{q-1}}{m-q+1}.
\tag{7.3}
\]

Thus the projected coordinate-orbit flow is the universal uniform Boolean deletion flow. It is independent of the starting factor.

### 7.2 Integral arcwise rounding

Normalize the flow by \(T\). Give every middle source supply one; split each lower node with throughput interval

\[
[c_q,c_q+1];
\]

and give each cover edge at step \(q\) the integral capacity interval

\[
\left[
\left\lfloor\frac{\lambda_q}{m+q+1}\right\rfloor,
\left\lceil\frac{\lambda_q}{m+q+1}\right\rceil
\right].
\tag{7.4}
\]

The universal fractional flow is feasible. The constraint matrix is a network matrix with integral lower and upper bounds, so it has an integral feasible flow. Unit-path decomposition yields one balanced nested resolution.

On a fixed Gaussian window,

\[
\frac{\lambda_q}{m+q+1}<1
\]

for large \(m\), so every Boolean cover edge can be used at most once in this aggregate projected flow.

This is a genuine positive integral theorem: balanced nesting and even arcwise rounding have no ordinary flow obstruction.

### 7.3 Why it does not align a factor

The theorem has erased precisely the needed information. Whenever two owner paths meet at a lower node, aggregate flow permits their suffixes to be exchanged. The reconnected paths remain nested, but their source-specific canonical mismatch costs can change at every later rank.

For any fixed balanced \(P\) and uniform \(\sigma\),

\[
\Pr[L_q^{\sigma F}(X)=P_q(X)]
=\binom mq^{-1},
\tag{7.5}
\]

so

\[
\mathbb E_\sigma E_A(\sigma F,P)
=
W\sum_{q=1}^{K}
\frac{1-\binom mq^{-1}}{c_q}.
\tag{7.6}
\]

The expected weighted matches are only

\[
W\sum_{q=1}^{K}
\frac{1}{c_q\binom mq}
=\frac{1+o_A(1)}m\,W,
\tag{7.7}
\]

whereas the total weighted owner-depth mass is
\(\Theta_A(W\sqrt m)\).

Whole-factor selection is exactly inert:

\[
J_A(\sigma F)=J_A(F).
\tag{7.8}
\]

At wreath level the erasure is total. Across the full coordinate orbit, each oriented wreath occurs \(nB\) times, and each unoriented support occurs \(2nB\) times. The uncolored union is the entire wreath hypergraph. Arbitrary refactorization of the full orbit is therefore the original exact-factor choice problem, not a restricted rounding theorem.

Orbit averaging changes per-factor, or quenched, balanced constraints into averaged, or annealed, constraints. TU rounding of the projection does not reverse that relaxation.

## 8. Exact odd-graph \(C_8\) trade classification

Regard a wreath as an induced \(n\)-cycle in
\(O_m=KG(2m+1,m)\).

### Theorem 8.1 — universal profile \(3,n-3\)

Assume \(m\ge3\), so \(n\ge7\). Let \(F,F'\) be exact wreath factors whose symmetric difference is one nontrivial simple \(F\)-alternating \(C_8\). Then:

1. the switch cuts exactly two old wreaths twice each and creates exactly two new wreaths from two inherited paths each;
2. the four inherited path vertex-orders are
   \[
   \boxed{\{3,n-3,3,n-3\};}
   \tag{8.1}
   \]
3. after choosing orientations optimally, exactly one short three-vertex inherited path must reverse.

#### Proof

Every wreath support is induced: among its \(n\) middle intervals, the only disjoint pairs are consecutive cycle vertices.

If a touched old wreath lost only one factor edge, it would remain an \(n\)-vertex path. It cannot join a positive second path inside a new \(n\)-cycle, while closing its own endpoints uses the removed edge. Thus every touched old wreath is cut at least twice. The four removed factor edges cannot all lie in one old wreath: then every affected middle vertex would lie in its \(n\)-vertex support, so the new factor would have to place one \(n\)-vertex wreath on exactly that support; because the support induces only the original wreath cycle, no different replacement edges exist. Hence the old cut shape is \(2+2\). Applying the same argument to the reverse move gives new shape \(2+2\).

We need one cross-neighbour fact. Let \(C,D\) be middle-disjoint wreath supports, let \(Y,Y'\) be adjacent vertices of \(D\), and suppose

\[
X\cap Y=\varnothing,\qquad
X'\cap Y'=\varnothing
\]

for \(X,X'\in C\). If \(p\) is the unique point outside
\(Y\cup Y'\), then

\[
X=(Y'\setminus\{y'\})\cup\{p\},
\qquad
X'=(Y\setminus\{y\})\cup\{p\},
\]

because middle-disjointness excludes \(X=Y'\) and \(X'=Y\). Hence

\[
X\cap X'=\{p\}.
\]

In a wreath, two vertices have intersection one exactly when their cycle distance is three. Indeed, from

\[
C_i=\{z_{i+1},z_{i+3},\ldots,z_{i+2m-1}\},
\]

separation \(2s\) gives intersection \(m-s\), and separation \(2s+1\) gives intersection \(s\).

Index one old wreath so its removed edges are
\(C_0C_1\) and \(C_aC_{a+1}\), with
\(2\le a\le m\). The two endpoints of either removed edge of the other old wreath have cross preimages in \(C\) at distance three. Those preimages cannot be the two endpoints of one removed \(C\)-edge, so they pair one endpoint from each cut.

The pairing

\[
\{C_0,C_a\},\quad\{C_1,C_{a+1}\}
\]

forces \(a=3\). The crossed pairing would force
\(a-1=3\) and simultaneously
\(\min(a+1,n-a-1)=3\), impossible for odd \(n\ge7\). Thus each old cut has profile \(3,n-3\), and symmetry gives the same profile on the new side.

Every new seam joins the two distinct old supports. Indeed, an edge internal to one old support is, by inducedness, an old cycle edge and cannot be a new edge of the nontrivial symmetric difference. Moreover, a new wreath cannot inherit both paths of one old wreath: their union is the entire old \(n\)-vertex support, so inducedness would force the new cycle to be the old cycle. Hence each new wreath inherits one path from each old wreath. The inherited-path incidence multigraph between the two old and two new wreaths is therefore the simple \(K_{2,2}=C_4\), rather than two double edges.

Give this \(C_4\) the signs recording agreement of path orientations. Its sign product is negative. If it were positive, one could orient all inherited paths consistently, and the old and new seam edges would split into two alternating \(C_4\)'s. The odd graph is \(C_4\)-free, since two distinct middle sets cannot have two distinct common disjoint middle neighbours. Therefore the signed \(C_4\) is negative. Orient each new wreath along its long inherited path; both long paths agree, and parity forces exactly one short path to reverse. \(\square\)

### 8.2 Universal multidepth ceilings

For an inherited path of vertex-order \(\ell\), a depth-\(q\) orientation-independent cyclic color can change only within \(q\) centres of either seam. The old changed-slot ceiling is

\[
\min(\ell,2q).
\]

Using (8.1),

\[
R_1=8,
\]

\[
\boxed{
R_q=4q+6
\qquad(2\le q\le m-1).
}
\tag{8.2}
\]

Thus

\[
\frac12\|\mu_q(F')-\mu_q(F)\|_1\le R_q
\tag{8.3}
\]

and

\[
|O_q(F')-O_q(F)|\le R_q.
\tag{8.4}
\]

These are coupling ceilings, not actual changed histogram support or guaranteed improvement. At the singleton rank the actual histogram is factor-independent even though the coupling ceiling is positive.

For pointed flags, preserved paths have the same seam ceiling, while the unique reversed short path is charged in full. Hence

\[
\widetilde R_1=9,
\]

\[
\boxed{
\widetilde R_q=4q+6
\qquad(2\le q\le m-1).
}
\tag{8.5}
\]

For every fixed balanced nested \(P\),

\[
|e_q(F',P)-e_q(F,P)|\le\widetilde R_q.
\tag{8.6}
\]

Summing (8.6) with weights and using
\(|\min_P f(P)-\min_P g(P)|\le\sup_P|f(P)-g(P)|\)
gives (8.8).

With \(S_A,T_A\) from (1.1)–(1.2),

\[
\boxed{
|\Phi_A(F')-\Phi_A(F)|
\le4T_A+6S_A-2,
}
\tag{8.7}
\]

\[
\boxed{
|J_A(F')-J_A(F)|
\le4T_A+6S_A-1,
}
\tag{8.8}
\]

where

\[
\Phi_A(F)=\sum_{q=1}^{K}\frac{O_q(F)}{c_q}.
\]

### 8.3 Chain and packing obstruction

At depth one, every exact \(C_8\) move changes overload by at most eight. For fixed \(\delta>0\), a chain changing depth-one overload by \(\delta W\) therefore needs at least

\[
\frac{\delta W}{8}
\tag{8.9}
\]

steps. If the evolving factor's \(B\) wreath positions are tracked as persistent bookkeeping slots, every step updates two such slots. Their average update count is at least

\[
\frac{2(\delta W/8)}B
=\frac{\delta n}{4}
=\Theta(m).
\tag{8.10}
\]

A family of pairwise middle-support-disjoint \(C_8\) switches simultaneously applicable to one factor has at most \(B/2\) members and changes depth-one overload by at most

\[
4B=o(W).
\tag{8.11}
\]

For the full Gaussian objective, one step has capacity

\[
(4t_A+o_A(1))m,
\]

so a \(\delta W\) change needs

\[
\left(\frac{\delta}{2t_A}+o_A(1)\right)B
\tag{8.12}
\]

steps. Thus the weighted estimate rules out only \(o(B)\)-length chains for a fixed positive weighted change. It does not rule out a support-disjoint family of linear size in \(B\), nor \(O(1)\) updates per persistent slot, for the weighted aggregate. The stronger \(\Theta(m)\) slot-reuse obstruction belongs specifically to fixed-positive-density depth-one repair. Moreover, persistent-slot reuse is not reuse of actual wreath supports: a chain may continually introduce new supports.

The factorial rooted-partner count is not a reservoir. For a fixed directed root, every partner contains the same two middle vertices, independently of its factorial parameters. Hence at most one partner for that root can lie in an exact factor. The universal profile theorem gives at most \(2n\) directed roots incident to one wreath and at most \(W\) candidate exact \(C_8\) moves incident to one factor.

No theorem says that any of these moves improves the relevant objective. Neutral plateau chains may be necessary, and bad \(C_8\)-local minima are not excluded asymptotically.

## 9. General macrotrades and signed orientation frustration

The correct larger-move invariant is not merely seam count.

Let \(F_0,F_1\) be exact factors and let

\[
P_1,\ldots,P_s
\]

be the maximal common undirected odd-factor paths in the changed owner support, with vertex-orders \(\ell_i\). Form the bipartite incidence graph
\(\Gamma\) between old and new wreaths, with one signed edge for each inherited path, recording whether fixed reference orientations traverse it in the same or opposite direction.

Define

\[
g_A(\ell)
=\sum_{q=1}^{K}\frac{\min(\ell,2q)}{c_q},
\tag{9.1}
\]

\[
h_A(\ell)
=\ell S_A-g_A(\ell)
=\sum_{q=1}^{K}\frac{(\ell-2q)_+}{c_q}.
\tag{9.2}
\]

Let
\(\operatorname{frust}_{h_A}(\Gamma)\) be the minimum total \(h_A\)-weight of unsatisfied signed edges after independently reversing old and new wreath orientations.

For fixed orientations, define the direct canonical-owner distance

\[
d_A^{\rm dir}(F_0,F_1)
=\sum_{q=1}^{K}\frac1{c_q}
\#\{X:L_q^{F_0}(X)\ne L_q^{F_1}(X)\},
\]

and let \(d_A^{\rm dir,*}\) be its minimum over all old and new wreath orientations.

### Theorem 9.1 — macrotrade locality/frustration ledger

\[
\boxed{
\sum_{q=1}^{K}
\frac{\|\mu_q(F_1)-\mu_q(F_0)\|_1}{2c_q}
\le
\sum_i g_A(\ell_i).
}
\tag{9.3}
\]

After choosing orientations optimally, the direct pointed distance obeys

\[
\boxed{
d_A^{\rm dir,*}(F_0,F_1)
\le
\sum_i g_A(\ell_i)
+\operatorname{frust}_{h_A}(\Gamma).
}
\tag{9.4}
\]

#### Proof

On an aligned inherited path, every centre more than \(q\) positions from both seams has the same radius-\(q\) cyclic color and the same pointed flag before and after the trade. At most
\(\min(\ell,2q)\) old slots remain. This proves (9.3) and the \(g_A\) contribution in (9.4).

If a path is traversed in the opposite direction, charge every one of its
\(\ell\) owner slots at every depth. Relative to its seam charge, the extra surrogate charge is exactly \(h_A(\ell)\). Reversing one wreath switches all signs incident to the corresponding vertex of \(\Gamma\), so the minimum extra charge in this surrogate ledger is precisely the signed frustration. The actual mismatch is no larger than that charge, proving (9.4). \(\square\)

There is also a direct-distance lower bound: a reversed path has at least

\[
(\ell-4q)_+
\]

interior owners whose old and new depth-\(q\) cyclic intervals are distinct. To see this, discard the first and last \(2q\) centres of the inherited path. For every remaining owner, both oriented depth-\(q\) flags are determined entirely inside the inherited path. Reversal deletes the two opposite endpoint \(q\)-blocks of its middle interval; these blocks are disjoint for the fixed-window range \(2q<m\), so the two lower sets differ. Therefore a negative signed incidence cycle whose paths all have order
\(\Theta(m)\) forces direct pointed displacement
\(\Omega_A(m^{3/2})\): every signing leaves at least one long path reversed. A single forced reversed path contributes \(\Theta_A(m^{3/2})\), while the total can be larger if the signed cycle has growing length.

This is not a lower bound on the reoptimized \(J_A\) objective, because the balanced resolution may also change. It proves that a dense unlabelled macrotrade needs a low-frustration theorem if it is to align the inherited canonical owner flags directly. A reoptimized common nested resolution could in principle bypass this direct-distance obstruction.

## 10. Exact factor-fibre switch chains

For any two exact factors \(F,F'\), cancel common wreaths and form the bipartite ownership multigraph:

- left vertices are \(F\setminus F'\);
- right vertices are \(F'\setminus F\);
- every middle set joins its old and new owning wreath.

The graph is \(n\)-regular. Every connected component \(C\) contains equally many old and new wreaths and defines a squarefree support-feasible trade. Switching its complete side preserves exact middle ownership. Switching the components one at a time connects \(F\) to \(F'\) through exact factors.

Thus the exact factor fibre is connected by macrotrades. But:

- a component can contain a factor-scale number of wreaths;
- a connected overlay gives only one binary switch;
- the decomposition gives no favorable seam count or sign;
- an alternating-cycle decomposition of factor edges need not preserve \(n\)-cycle components at intermediate states;
- the direct pointed cost is upper-controlled by the surrogate frustration ledger (9.4), not just by the number of changed wreaths.

This is an exact local-to-global chain theorem without a quantitative alignment theorem.

## 11. Corrected heat-switch route

Fix \(1\le H\le m-1\). For an exact factor let

\[
a_q=\frac W{N_q}=c_q+\theta_q,
\]

\[
V_q(F)=\sum_S(\mu_q(S)-a_q)^2,
\qquad
V_q^{\min}=N_q\theta_q(1-\theta_q),
\]

\[
Q_q(F)=V_q(F)-V_q^{\min}
=\sum_S
(\mu_q(S)-c_q)(\mu_q(S)-c_q-1).
\tag{11.1}
\]

Put

\[
E_H(F)=\sum_{q=1}^{H}\frac{Q_q(F)}{c_q},
\qquad
B_H=\sum_{q=1}^{H}\frac{V_q^{\min}}{c_q},
\]

\[
P_H(F)=\sum_{q=1}^{H}\frac{O_q(F)}{c_q}.
\tag{11.2}
\]

Let \(F\) be a global minimizer of \(E_H\) on the same window \(H\). For an unordered coordinate transposition \(\tau\), overlay \(F\) and \(\tau F\) by middle ownership. If \(C\) is an overlay component, let \(u_{q,C}\) and \(w_{q,C}\) be the complete-side depth-\(q\) histograms. Define

\[
A_{\tau,H}=\sum_{q=1}^{H}
\frac{\|\mu_q-\tau\mu_q\|_2^2}{c_q},
\qquad
N_{\tau,H}=\sum_C\sum_{q=1}^{H}
\frac{\|u_{q,C}-w_{q,C}\|_2^2}{c_q},
\]

\[
D_H=\sum_{\tau}A_{\tau,H},
\qquad
R_H=\sum_{\tau}N_{\tau,H},
\tag{11.2a}
\]

where every unordered transposition is counted once. Fair independent resampling of complete component sides gives \(A_{\tau,H}\le N_{\tau,H}\) at the global minimizer.

Indeed, if \(F'\) is the fair switched child, then rankwise

\[
\begin{aligned}
\mathbb E V_q(F')
&=\left\|\frac{\mu_q+\tau\mu_q}{2}-a_q\mathbf1\right\|_2^2
+\frac14\sum_C\|u_{q,C}-w_{q,C}\|_2^2,\\
V_q(F)
&=\left\|\frac{\mu_q+\tau\mu_q}{2}-a_q\mathbf1\right\|_2^2
+\frac14\|\mu_q-\tau\mu_q\|_2^2.
\end{aligned}
\tag{11.2b}
\]

Every child is an exact factor. Weighted same-window global minimality, followed by multiplication by four, is exactly \(A_{\tau,H}\le N_{\tau,H}\).

Exact wreath centered histograms have zero total and zero point-star margins. Their Johnson degrees zero and one vanish. Hence the sharp ambient coefficient in the applicable Johnson spectral inequality is

\[
\boxed{4(n-1),}
\tag{11.3}
\]

not the generic \(2n\). Global minimality and the integer floor identity give

\[
\boxed{
R_H\ge D_H
\ge4(n-1)(B_H+E_H(F)),
}
\tag{11.4}
\]

and

\[
\boxed{
P_H(F)
\le\frac{E_H(F)}2
\le
\frac{R_H-4(n-1)B_H}{8(n-1)}.
}
\tag{11.5}
\]

There is an exact nonnegative decomposition

\[
\begin{aligned}
R_H-4(n-1)B_H
={}&(R_H-D_H)\\
&+\bigl(D_H-4(n-1)(B_H+E_H)\bigr)\\
&+4(n-1)E_H.
\end{aligned}
\tag{11.6}
\]

On \(H=K_A\),

\[
B_H\sim\beta_AW\sqrt m,
\]

\[
\beta_A=
\int_0^A
\frac{\{e^{x^2}\}(1-\{e^{x^2}\})}
{e^{x^2}\lfloor e^{x^2}\rfloor}\,dx
>0.
\tag{11.7}
\]

Therefore the old proposed gate

\[
R_H\le2nB_H+o(nW)
\]

is formally sufficient but impossible: its baseline is below the forced
\(4(n-1)B_H\) floor by \(\Theta_A(nW\sqrt m)\).

The coefficient \(4(n-1)\) is the sharp ambient Johnson coefficient after degrees zero and one are removed. Thus the corrected near-baseline target

\[
R_H\le4(n-1)B_H+o(nW)
\tag{11.8}
\]

is spectrally compatible and, by (11.5), would imply

\[
E_H=o(W),
\qquad
P_H=o(W).
\]

It is nevertheless impossible at every same-window global minimizer on every nontrivial fixed Gaussian window. The additional obstruction is Boolean degree-two stability.

### Theorem 11.1 — Boolean stability closes the corrected heat gate

For every fixed \(A>0\), there is \(\kappa_A>0\) such that, for all sufficiently large \(m\), every global minimizer of the same-window objective with \(H=K_A\) satisfies

\[
\boxed{
R_H-4(n-1)B_H
\ge \kappa_A nW\sqrt m.
}
\tag{11.9}
\]

Consequently (11.8) is false, not merely unproved.

#### Proof

We record the decisive stability input. Put

\[
\theta_*:=\frac{3-\sqrt6}{6}.
\]

For every compact \(I\subset(0,\theta_*)\) and every fixed central-slice window, there is \(\varepsilon_I>0\) such that every Boolean family \(\mathcal B\subseteq\binom{[n]}r\) of density \(\theta\in I\) obeys

\[
\left\|
P_{E_1\oplus E_{\ge3}}
(\mathbf1_{\mathcal B}-\theta\mathbf1)
\right\|_2^2
\ge\varepsilon_I\binom nr.
\tag{11.10}
\]

This is an imported proved lemma: Theorem 7.1 of
`MATH_ATTACK_D_BOOLEAN_E2_STABILITY_20260724.md`. For completeness, its decisive invariant is the third moment. Every \(h\in E_2\) has the harmonic-matrix representation

\[
h(S)=\sum_{i<j}a_{ij}\mathbf1_{\{i,j\}\subseteq S},
\qquad A\mathbf1=0,
\]

with \(A\) symmetric and zero diagonal. Put

\[
\pi_t=\frac{(r)_t}{(n)_t},\quad
S_2=\sum_{i<j}a_{ij}^2,\quad
C_3=\sum_{i<j}a_{ij}^3,\quad
T_3=\operatorname{tr}(A^3).
\]

Direct expansion on the slice gives

\[
\mathbb Eh^2=\alpha_{n,r}S_2,
\qquad
\mathbb Eh^3=a_{n,r}C_3+b_{n,r}T_3,
\]

where

\[
\begin{aligned}
\alpha_{n,r}&=\pi_2-2\pi_3+\pi_4,\\
a_{n,r}&=\pi_2-6\pi_3+13\pi_4-12\pi_5+4\pi_6,\\
b_{n,r}&=\pi_3-3\pi_4+3\pi_5-\pi_6.
\end{aligned}
\]

On a central slice,

\[
\alpha_{n,r}=\frac1{16}+O_A(n^{-1}),
\qquad
a_{n,r}=O_A(n^{-1}),
\qquad
b_{n,r}=\frac1{64}+O_A(n^{-1}).
\]

The elementary bounds

\[
|C_3|\le S_2^{3/2},
\qquad
|T_3|\le(2S_2)^{3/2}
\]

therefore give, uniformly on a central slice,

\[
|\mathbb Eh^3|
\le(2\sqrt2+O_A(n^{-1}))(\mathbb Eh^2)^{3/2},
\qquad
\mathbb Eh^4\le C(\mathbb Eh^2)^2.
\]

The fourth-moment estimate follows by expanding four edge monomials: the row-sum identities kill every endpoint pattern with a degree-one vertex, while each remaining four-edge pattern is bounded by \((\sum_{i,j}a_{ij}^2)^2\). The central-slice lower bound on \(\alpha_{n,r}\) makes \(C\) absolute.

For \(g=\mathbf1_{\mathcal B}-\theta\), its standardized third moment is

\[
\frac{\mathbb Eg^3}{(\mathbb Eg^2)^{3/2}}
=\frac{1-2\theta}{\sqrt{\theta(1-\theta)}}.
\]

This exceeds \(2\sqrt2\) exactly when \(0<\theta<\theta_*\). The fourth-moment bound makes the third moment continuous under \(L^2\) approximation by \(E_2\); compactness of \(I\) therefore yields the uniform positive gap (11.10).

Now choose

\[
0<u<v<\min\{A,\sqrt{\log(17/16)}\}.
\]

For every integer depth \(u\sqrt m\le q\le v\sqrt m\), after shrinking \([u,v]\) once if necessary,

\[
c_q=1,
\qquad
\theta_q=\lambda_q-1\in I\Subset(0,1/16),
\qquad
N_q=\Theta_{u,v}(W).
\tag{11.11}
\]

Write

\[
f_q=\mu_q-\lambda_q\mathbf1,
\qquad
\mathcal H_q=\sum_{j\ge3}\|f_q^{(j)}\|_2^2,
\qquad
\mathcal E_q=Q_q(F).
\]

The exact wreath margins give \(f_q^{(0)}=f_q^{(1)}=0\). Round the integer vector \(\mu_q\) to a vector

\[
b_q=\mathbf1+\mathbf1_{\mathcal B_q}
\]

of the same mass. Pointwise nearest-integer rounding followed by correcting the mass gives the exact estimate

\[
\|\mu_q-b_q\|_2^2
\le2\mathcal E_q+2\sqrt{N_q\mathcal E_q}.
\tag{11.12}
\]

Here is the rounding proof. First put \(\widetilde b_q(S)=1\) when \(\mu_q(S)\le1\), and \(\widetilde b_q(S)=2\) when \(\mu_q(S)\ge2\). Pointwise,

\[
(\mu_q(S)-\widetilde b_q(S))^2
\le(\mu_q(S)-1)(\mu_q(S)-2),
\]

so \(\|\mu_q-\widetilde b_q\|_2^2\le\mathcal E_q\). Its mass discrepancy from \(W\) is at most

\[
\sqrt{N_q}\,\|\mu_q-\widetilde b_q\|_2
\le\sqrt{N_q\mathcal E_q}.
\]

Flip exactly that many entries of \(\widetilde b_q\) between one and two in the required direction. The resulting \(b_q=\mathbf1+\mathbf1_{\mathcal B_q}\) has mass \(W\), and the squared triangle inequality gives (11.12).

Applying (11.10), orthogonal projection, and (11.12) yields

\[
\varepsilon_I N_q
\le2\mathcal H_q+4\mathcal E_q
+4\sqrt{N_q\mathcal E_q}.
\]

Replace \(\varepsilon_I\) by \(\min\{\varepsilon_I,1\}\), which preserves (11.10). Then the displayed inequality implies the following exact dichotomy.

\[
\boxed{
\mathcal H_q\ge\frac{\varepsilon_I}{4}N_q
\quad\text{or}\quad
\mathcal E_q\ge\frac{\varepsilon_I^2}{256}N_q.
}
\tag{11.13}
\]

At a same-window global minimizer, the nonnegative slack decomposition refines to

\[
\begin{aligned}
R_H-4(n-1)B_H
\ge{}&4(n-1)\sum_{q=1}^{H}\frac{\mathcal E_q}{c_q}\\
&+2\sum_{q=1}^{H}\frac1{c_q}
\sum_{j\ge3}(j-2)(n-j-1)\|f_q^{(j)}\|_2^2.
\end{aligned}
\tag{11.14}
\]

Since \(j\le m-q\le m\),

\[
(j-2)(n-j-1)\ge n-4
\qquad(j\ge3).
\]

By (11.11)--(11.13), every one of the \(\Theta_{u,v}(\sqrt m)\) selected depths contributes at least

\[
\min\left\{
\frac{(n-4)\varepsilon_I}{2}N_q,
\frac{(n-1)\varepsilon_I^2}{64}N_q
\right\}
=\Omega_{u,v,I}(nW)
\]

to (11.14). Summing proves (11.9). \(\square\)

The exact overload inequality (11.5) remains valid, but the lower bound (11.9) does not force \(E_H\) or \(P_H\) to be large: the unavoidable gap may be paid by Johnson degrees at least three. It proves only that component-noise near-equality cannot certify small overload.

Even an independent proof of \(P_H=o(W)\) would still be unlabelled. There is no proved implication

\[
P_H=o(W)\Longrightarrow J_A(F)=o(W).
\tag{11.15}
\]

Abstract cycle and cube examples show that Hall feasibility and tiny overload can coexist with long supported recourse. A successful overload route would therefore require both a different small-overload mechanism and an exact-factor nested retraction theorem.

## 12. Two live gates and one closed heat proposal

### 12.1 Direct packetized Hall–recourse gate

The logically clean sufficient statement within the one-pass class is:

> **Cyclic Adaptive Hall–Recourse Lemma \(\mathrm{CAHR}_A\) — unproved.**  
> For every fixed \(A>0\) and all sufficiently large \(m\), there are one oriented exact factor \(F_{m,A}\), reachable state vectors \(\kappa_q=(\kappa_q(X))_X\), and orientations
> \[
> \mathcal O_q\in\mathcal B_q(\kappa_q)
> \qquad(1\le q\le K_A),
> \]
> such that \(\kappa_1=(a_1^X)_X\), the same orientation \(\mathcal O_q\) generates \(\kappa_{q+1}\) through (2.1), and \(T_q=T(\mathcal O_q)\). Thus the actually chosen trajectory is balanced at every rank and satisfies every cut in (3.2). Moreover,
> \[
> \boxed{
> \sum_{q=1}^{K_A}\frac{T_q}{c_q}=o(W)
> }
> \tag{12.1}
> \]
> as \(m\to\infty\) with \(A\) fixed.

Equivalently,

\[
\boxed{
\min_F
R_1^F\bigl((a_1^X)_X\bigr)
=o(W)
\quad\text{for each fixed }A\text{ as }m\to\infty.
}
\tag{12.2}
\]

Only one trajectory is required. Requiring every reachable graph or every factor to work is unnecessarily stronger.

By (2.5), this proves fixed-window labelled alignment. Diagonalizing fixed \(A\) proves labelled synchronization and hence MWB and the final OR theorem.

A stronger cycle-synchronized version requires the same reachable nested trajectory to attain, at every rank, point-regular quotas of the type supplied rankwise by Theorem 4.1. Then every stage correction is automatically a union of coordinate cycles by Theorem 5.1, and all deletion-position margins are exactly canonical. What remains is still the simultaneous quota compatibility, higher-order Hall, and short-recourse theorem.

### 12.2 The corrected heat-plus-retraction proposal is closed

The formerly proposed route was to prove (11.8) at a same-window global minimizer and then prove the wreath-specific retraction

\[
\boxed{
J_A(F)
\le C_A'\,P_H(F)+o(W).
}
\tag{12.3}
\]

Theorem 11.1 disproves its first step, so this is not a remaining heat route. A retraction of the displayed form could still be useful if a different theorem supplied \(P_H=o(W)\). No generic retraction of this kind is true; it would have to use exact packet geometry and one common nested flow.

A logically different plateau proposal could allow macrotrades from the global minimizer to a factor \(F'\) with

\[
E_H(F')=E_H(F)+o(W)
\]

and \(J_A(F')=o(W)\). This does not follow from heat near-equality. If the plateau theorem must correct a fixed positive depth-one defect using only \(C_8\) moves, (8.9)--(8.11) force \(\Omega(W)\) moves and rule out a single simultaneously support-disjoint reservoir; the weighted aggregate alone has no bounded-reuse obstruction.

### 12.3 Dense decorated macrotrade cover-down

The second live route is a positive-density macrotrade theorem supplying simultaneously:

1. \(\Theta(m)\) productive depth-one seams per \(O(1)\)-wreath packet, or an equivalent linear-scale correction;
2. either low signed orientation frustration in the sense of (9.4) for a direct inherited-owner coupling, or a proof that reoptimization of the common nested resolution bypasses that direct-distance ledger;
3. preservation of every hard Hall quota in one common window;
4. an exact factor after every selected bundle, or one exact endpoint with a support-feasible global switch;
5. weighted owner recourse \(o(W)\).

No such packet is currently constructed. For fixed-positive-density depth-one repair, the universal \(C_8\) theorem proves that a single disjoint family of bounded-seam local absorbers cannot substitute for it.

## 13. Additional exact Hall flow for irreversible release

There is a rigorous hybrid between adaptive diamonds and arbitrary residual flow.

Let

\[
V_q=\binom{[n]}{m-q}\qquad(0\le q\le K).
\]

Let an owner follow a chosen one-pass cyclic prefix \(\widehat P_q(X)\) through a stopping depth
\(a(X)\in\{0,1,\ldots,K\}\), then release it permanently into a common suffix flow. Here \(\widehat P_0(X)=X\). Precisely, let

\[
g_q(S)=\#\{X:a(X)\ge q,\ \widehat P_q(X)=S\},
\qquad
\sigma_q(S)=\#\{X:a(X)=q,\ \widehat P_q(X)=S\}.
\]

Thus \(g_q(S)\) is the active load at depth \(q\), while \(\sigma_q(S)\) is the number released at \(S\) immediately after depth \(q\). Put

\[
\ell_q(S)=(c_q-g_q(S))_+,
\qquad
u_q(S)=c_q+1-g_q(S).
\]

Assume \(g_q(S)\le c_q+1\) for every \(q,S\). Put

\[
R_K=\#\{X:a(X)<K\}.
\]

For arbitrary families
\(B_q\subseteq V_q\) for \(0\le q<K\), put

\[
C_q=\partial B_{q-1}\qquad(1\le q\le K).
\]

Here \(\partial B_{q-1}\subseteq V_q\) is the lower Boolean shadow. For a function \(h_q\) on \(V_q\), notation \(h_q(B)\) means \(\sum_{S\in B}h_q(S)\).

Hoffman's theorem on the split layered Boolean network, closed to a circulation by the fixed terminal return arc with lower and upper capacity \([R_K,R_K]\), gives an integral residual suffix flow if and only if both staircase systems hold:

\[
\boxed{
\sum_{q=0}^{K-1}\sigma_q(B_q)
+\sum_{q=1}^{K-1}\ell_q(B_q\setminus C_q)
\le
\sum_{q=1}^{K-1}u_q(C_q\setminus B_q)
+u_K(C_K),
}
\tag{13.1}
\]

\[
\boxed{
\begin{aligned}
\sum_{q=0}^{K-1}\sigma_q(B_q)
&+\sum_{q=1}^{K-1}\ell_q(B_q\setminus C_q)
+\ell_K(V_K\setminus C_K)\\
&\le
R_K
+\sum_{q=1}^{K-1}u_q(C_q\setminus B_q).
\end{aligned}
}
\tag{13.2}
\]

Integral capacities give an integral common suffix resolution. Define the number of active toggles by

\[
T_q^{\rm act}
=\#\{X:a(X)\ge q,\ \varepsilon_q(X)=1\}.
\]

Its total alignment cost is at most

\[
\boxed{
\sum_{q=1}^{K}\frac{T_q^{\rm act}}{c_q}
+\sum_X
\Psi_{m,K}(a(X)),
}
\tag{13.3}
\]

where

\[
\Psi_{m,K}(a)=\sum_{q=a+1}^{K}\frac1{c_q}.
\]

This is an exact sufficient theorem, not an independent rankwise selection. Its weakness is irreversible release: it can charge an entire suffix where a later adjacent swap would have rejoined immediately.

## 14. Final proved/open ledger

### Proved here, or explicitly imported and applied

1. The exact Hall–Bellman recursion (3.4) for one common adjacent-swap trajectory.
2. Cyclically invariant point-regular balanced quotas at every fixed-window rank.
3. The coordinate-cycle decomposition of every point-regular adaptive correction.
4. Exact deletion-position regularity along a point-regular trajectory.
5. Rigidity of per-wreath perfect cyclic flow.
6. Universal orbit-flow formulas and integral arcwise rounding.
7. Exact erasure of factor-dependent owner correlations from the projected orbit flow.
8. Universal profile-\(3\) classification of every exact-factor \(C_8\) move.
9. Exact \(C_8\) multidepth ceilings, chain lower bounds, and rooted-reservoir packing obstruction.
10. The signed seam/frustration ledger for arbitrary exact macrotrades.
11. Exact factor-fibre connectivity by ownership-component macrotrades.
12. The corrected \(4(n-1)\) heat-switch ledger and the impossibility of the \(2nB_H\) gate.
13. The imported proved Boolean-\(E_2\) stability lemma, applied here to show the stronger impossibility of the corrected \(4(n-1)B_H+o(nW)\) near-baseline gate.
14. The Hoffman staircase criterion for adaptive-prefix/residual-flow hybrids.

### Still unproved

1. Any exact factor and trajectory satisfying \(\mathrm{CAHR}_A\).
2. Simultaneous nested compatibility of the point-regular quota families.
3. Higher-order Hall expansion for the evolving packetized owner graphs.
4. A short supported-recourse theorem beyond first-order point constraints.
5. Any nested retraction such as (12.3), should a different argument provide small overload.
6. A positive-density macrotrade cover-down with either low direct frustration or controlled nested reoptimization.
7. A theorem that neutral \(C_8\) plateau chains reach a good basin.
8. A genuine exact-factor counterexample to cyclic alignment or MWB.

## 15. Final verdict

The new point-regular and cycle-decomposition theorems show that first-order margins can be synchronized integrally around coordinate cycles. The row-rigidity theorem shows why this cannot be done one wreath at a time. For fixed-positive-density depth-one repair, the universal \(C_8\) theorem rules out a single disjoint bounded-seam reservoir. The macrotrade frustration ledger identifies the extra signed condition needed by a direct inherited-owner coupling, while leaving open a bypass through reoptimization of the nested resolution.

The remaining obstruction is therefore not ordinary flow integrality, point balance, exact-factor connectivity, or a shortage of formal local partners. It is the simultaneous positive statement

\[
\boxed{
\text{one exact packetized factor}
+\text{ higher-order Hall feasibility}
+\text{ short cycle-bundled recourse}
+\text{ one common nested owner coupling}.
}
\]

That statement is precisely \(\mathrm{CAHR}_A\) within the one-pass class. A dense macrotrade theorem coupled to a common nested reoptimization is the other live route. The corrected heat near-equality route is now rigorously closed.
