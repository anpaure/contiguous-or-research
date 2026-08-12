# Third-wave lane L: packetized higher-order Hall and short recourse

Date: 2026-07-24

Method: pure mathematics only. No web search, finite search, or solver was used.

## 0. Verdict

This report does **not** prove cyclic alignment, labelled synchronization, MWB, or the final OR theorem. It proves two exact bounded-packet lemmas, characterizes every available fixed-star exact-factor twin packet with explicit universal constants, and constructs sharp recourse obstructions to black-box theorems using only bounded capacities, stagewise Hall feasibility, first-order balance, and ownerwise sibling geometry.

The main positive result is the following conditional lift.

> **Alternating canonical-reservoir lemma.** If, at every rank in one fixed Gaussian window, the required balanced discrepancy can be routed through an owner reservoir disjoint from the preceding reservoir, and every active reservoir component has bounded size, then the rankwise flows glue exactly into one actual ascending adjacent-swap trajectory. If the active components have at most (p_q+1) target vertices, then
> 
> \[
> T_q\le p_q\,\frac12\|b_q-\mu_q\|_1.
> \]

There is no hidden compatibility loss in this statement: adjacent reservoir disjointness exactly neutralizes the carried-state rewiring.

A second theorem isolates the two independent packet requirements. For a connected owner component (C) with (v) vertices, the minimum recourse to an orientable balanced quota is at most (v-1) times its nearest orientable-quota distance. The exact condition that **every** component-compatible balanced quota is orientable is

\[
i_C(U)\le c|U|+\max\{0,k-(v-|U|)\}
\qquad(U\subseteq V(C)),
\]

where (|E(C)|=c|V(C)|+k). Thus bounded component order supplies short recourse, while the displayed higher-order cuts eliminate the Hall surcharge.

Both hypotheses are necessary in substance. A cycle is quota-universal and has overload (1), but may require half of its edges to reverse. More strongly, an explicit two-rank clone automaton with (c_1=c_2=1), (4M+7) owners, overloads (2) and (4), and zero first-order signed defect has exact Bellman cost (2M+4). One literally allowed sibling rewire removes the sole slack edge from (M-1) nested Hall cuts. This refutes any theorem deriving short recourse merely from bounded capacities, stagewise Hall feasibility, point balance, and ownerwise sibling geometry.

Inside a genuine exact-factor fibre, every available fixed-star twin switch is a support-feasible packet. A switch of (k) wreaths has rankwise histogram half-distance at most (2k), pointed owner distance at most (3k), and weighted fixed-window cost (O_A(k\sqrt m)). Since (k\le B=W/n), the diameter of the entire fixed-star fibre is (O_A(W/\sqrt m)=o(W)). A given fibre may contain no nontrivial switch. When a switch exists, transporting a balanced one-pass trajectory across it leaves only an (O(k)) integral quota defect per rank. Repairing that residual by one common short flow is exactly the missing theorem.

No genuine exact-factor counterexample to existential \(\mathrm{CAHR}_A\) is obtained. Conversely, no exact factor with the required bounded dynamic packets is constructed. The lane therefore ends at a strictly narrower and now fully quantified exact-factor packetization problem.

## 1. Fixed-window and one-pass normalization

Put

\[
n=2m+1,
\qquad
W=\binom nm,
\qquad
B=\frac Wn=\operatorname{Cat}_m,
\]

and, for (q\ge1),

\[
N_q=\binom n{m-q},
\qquad
\lambda_q=\frac W{N_q},
\qquad
c_q=\lfloor\lambda_q\rfloor.
\]

Fix (A>0) and set (K=K_A=\lceil A\sqrt m\rceil). Since

\[
\lambda_q
=\prod_{j=0}^{q-1}\frac{m+2+j}{m-j},
\]

uniformly for (q\le K),

\[
\log\lambda_q=\frac{q(q+1)}m+O_A(m^{-1/2}).
\tag{1.1}
\]

Consequently there is a constant (C_A) such that, for all sufficiently large (m),

\[
1\le c_q\le C_A
\qquad(1\le q\le K),
\tag{1.2}
\]

and

\[
S_A(m):=\sum_{q=1}^{K}\frac1{c_q}
=\left(s_A+o_A(1)\right)\sqrt m,
\qquad
s_A=\int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor}.
\tag{1.3}
\]

Only the bound (S_A=O_A(\sqrt m)) is needed below.

For a cyclic order \(\pi=(\pi_0,\ldots,\pi_{n-1})\), with indices modulo
\(n\), write
\[
I_\pi(j,r)=\{\pi_j,\pi_{j+1},\ldots,\pi_{j+r-1}\}.
\]
A wreath is the \(n\)-set support
\(\{I_\pi(j,m):j\in\mathbb Z_n\}\). An exact middle wreath factor is a
family of \(B=W/n\) wreaths whose supports partition
\(\binom{[n]}m\). Thus every middle set has one unique wreath owner.

Fix one oriented exact wreath factor \(F\). For each middle owner
\(X\in\binom{[n]}m\), let

\[
a_1^X,a_2^X,\ldots,a_{K+2}^X
\]

be its canonical deletion word and put

\[
L_q(X)=X\setminus\{a_1^X,\ldots,a_q^X\}.
\]

For fixed \(A\) and all sufficiently large \(m\), \(K+2\le m\), so all displayed letters exist.

The canonical rank-(q) histogram is

\[
\mu_q(S)=\#\{X:L_q(X)=S\},
\qquad S\in\binom{[n]}{m-q}.
\]

Write (W=c_qN_q+\rho_q). A balanced quota is a vector

\[
b_q=c_q\mathbf1+\mathbf1_{H_q},
\qquad |H_q|=\rho_q.
\]

The exact unlabelled overload is

\[
O_q(F)=\max\left\{
\sum_S(c_q-\mu_q(S))_+,
\sum_S(\mu_q(S)-c_q-1)_+
\right\}.
\tag{1.4}
\]

The one-pass carried letter obeys

\[
\kappa_1(X)=a_1^X,
\qquad
\kappa_{q+1}(X)=
\begin{cases}
\kappa_q(X),&X\text{ toggles at }q,\\
a_{q+1}^X,&X\text{ does not toggle at }q.
\end{cases}
\tag{1.5}
\]

At stage (q), the no-toggle endpoint is always

\[
u_{q,X}=L_q(X),
\]

while the actual toggle endpoint is

\[
L_{q+1}(X)\cup\{\kappa_q(X)\}.
\]

If (X) did not toggle at (q-1), then (kappa_q(X)=a_q^X), so its toggle uses the **canonical sibling arc**

\[
e_{q,X}:u_{q,X}=L_q(X)\longrightarrow
v_{q,X}=L_{q+1}(X)\cup\{a_q^X\}.
\tag{1.6}
\]

Toggling (X) adds the incidence column

\[
\mathbf e_{v_{q,X}}-\mathbf e_{u_{q,X}}
\tag{1.7}
\]

to the load vector.

### 1.1 Exact nearest-quota identity

For any integer histogram \(\mu\) of total \(cN+\rho\), define

\[
A(\mu)=\sum_z(c-\mu(z))_+,
\qquad
B(\mu)=\sum_z(\mu(z)-c-1)_+.
\]

Then

\[
\boxed{
\min_{|H|=\rho}
\frac12\|c\mathbf1+\mathbf1_H-\mu\|_1
=\max\{A(\mu),B(\mu)\}.
}
\tag{1.8}
\]

Indeed, clip \(\mu\) into \(\{c,c+1\}\). This costs \(A+B\) in full \(\ell^1\) and produces \(\rho+A-B\) high cells. Correcting the high-cell count costs \(|A-B|\) more. The resulting full distance is

\[
A+B+|A-B|=2\max(A,B).
\]

Conversely every balanced target must pay all mass below (c) and all mass above (c+1), so its half-distance is at least both (A) and (B).

Thus \(O_q(F)\) is exactly the nearest balanced half-\(\ell^1\) distance. For every actual stage-\(q\) balanced reorientation with \(T_q\) toggles and load \(b_q\),

\[
O_q(F)\le \frac12\|b_q-\mu_q\|_1\le T_q.
\tag{1.9}
\]

The second inequality holds because every toggle contributes one head-minus-tail vector. Hence overload is an unavoidable lower bound on labelled recourse.

### 1.2 A rankwise point-regular quota, with its exact loss

Let (r=m-q). Every exact-factor histogram has point degree

\[
\sum_{S\ni x}\mu_q(S)=\frac{rW}{n}=rB
\qquad(x\in[n]).
\tag{1.10}
\]

There is always a point-regular balanced quota within a factor (r+1) of nearest balance.

> **Lemma 1.1.** There is a family (H\subseteq\binom{[n]}r), (|H|=\rho_q), with every point degree equal to
> 
> \[
> d^*=\frac{r\rho_q}{n},
> \]
> 
> such that, for (b=c_q\mathbf1+\mathbf1_H),
> 
> \[
> \frac12\|b-\mu_q\|_1\le(r+1)O_q(F).
> \tag{1.11}
> \]

**Proof.** Choose a nearest quota (b_0=c_q\mathbf1+\mathbf1_{H_0}), so its half-distance is (O_q). If (U_r) is point incidence, then by (1.10)

The number \(d^*\) is integral, because \(rW/n=rB\) and
\(c_qrN_q/n=c_q\binom{n-1}{r-1}\) are integers and their difference is
\(r\rho_q/n\).

\[
\deg_{H_0}(x)-d^*=[U_r(b_0-\mu_q)]_x.
\]

Therefore

\[
P:=\sum_x(\deg_{H_0}(x)-d^*)_+
=\frac12\|U_r(b_0-\mu_q)\|_1
\le rO_q.
\tag{1.12}
\]

If (x) is overfull and (y) underfull, then some (E\in H_0) contains (x), omits (y), and satisfies (E-x+y\notin H_0). Otherwise (E\mapsto E-x+y) would inject all such (x)-sets into the corresponding (y)-sets, contradicting (deg(x)>\deg(y)). Replace (E) by (E-x+y). Simplicity and cardinality are preserved and (P) drops by one. After exactly (P) exchanges the family is point-regular. Its high-cell vector moved half-distance (P), so (1.11) follows from the triangle inequality. \(\square\)

This lemma is only rankwise. The exchanges can move high cells between different owner-graph components and need not preserve their forced high counts. Moreover (r\asymp m), so the loss in (1.11) is too large to convert the bare MWB rate (o(W)) into cyclic alignment.

## 2. The alternating canonical-reservoir packet lemma

For (R_q\subseteq\binom{[n]}m), let (D_q[R_q]) be the directed multigraph consisting of the canonical arcs (1.6) for owners in (R_q), counted with owner multiplicity. For (U\subseteq\binom{[n]}{m-q}), let

\[
\partial^-_{R_q}(U)
=\{e_{q,X}:X\in R_q, u_{q,X}\notin U, v_{q,X}\in U\}.
\]

A weak component of \(D_q[R_q]\) is called active for a discrepancy \(\delta_q\) if it meets \(\operatorname{supp}\delta_q\).

### Theorem 2.1 — alternating canonical-reservoir lift

Fix one oriented exact factor (F) and an integer (K\le m-1). Suppose that for every (1\le q\le K) there are:

- a balanced quota (b_q);
- an owner reservoir (R_q\), with (R_0=\varnothing) and
  
  \[
  R_q\cap R_{q-1}=\varnothing;
  \tag{2.1}
  \]
- an integer (p_q\ge0);

such that, with \(\delta_q=b_q-\mu_q\),

\[
\boxed{
\delta_q(U)\le|\partial^-_{R_q}(U)|
\qquad
\text{for every }U\subseteq\binom{[n]}{m-q},
}
\tag{2.2}
\]

and every active weak component of (D_q[R_q]) has at most (p_q+1) target vertices.

Then there is one actual ascending one-pass trajectory whose rank-(q) load is exactly (b_q). If (T_q) is its number of stage-(q) toggles and

\[
D_q=\frac12\|b_q-\mu_q\|_1,
\]

then

\[
\boxed{
T_q\le p_qD_q,
\qquad
\sum_{q=1}^{K}\frac{T_q}{c_q}
\le
\sum_{q=1}^{K}\frac{p_qD_q}{c_q}.
}
\tag{2.3}
\]

**Proof.** Let (B_q) be the incidence matrix of (D_q[R_q]), with column (mathbf e_v-\mathbf e_u) for an arc (u\to v). The capacitated flow system

\[
B_qx_q=\delta_q,
\qquad
0\le x_q\le1
\tag{2.4}
\]

is feasible if and only if (2.2) holds. Necessity follows by summing (2.4) over (U). Sufficiency is the standard directed cut theorem; the inequality for (V\setminus U) supplies the outgoing half of the cut condition. Incidence total unimodularity gives an integral solution.

Choose an integral feasible (x_q) of minimum cardinality. Its selected arcs contain no directed cycle, because deleting a selected cycle preserves (2.4) and reduces cardinality. Hence the selected integral flow decomposes into exactly

\[
\sum_z(\delta_q(z))_+=D_q
\]

unit source-to-sink paths and no cycles. Every such path lies in an active reservoir component, is simple, and has length at most (p_q). Thus

\[
|x_q|\le p_qD_q.
\tag{2.5}
\]

It remains to check temporal compatibility. Toggle exactly the owners selected by (x_q). If (X) is selected at stage (q), then (X\in R_q) and, by (2.1), (X\notin R_{q-1}). It was therefore not selected at stage (q-1), so the no-toggle reset in (1.5) gives

\[
\kappa_q(X)=a_q^X.
\]

Its actual alternate is exactly the canonical head \(v_{q,X}\). An owner not selected at \(q\) uses \(u_{q,X}=L_q(X)\), independently of its carried letter. Thus the independently chosen rankwise flows are precisely the decisions of one actual recurrence, and their loads are \(\mu_q+B_qx_q=b_q\). An owner may reappear at \(q+2\), because the intervening no-toggle again resets its carried letter. This proves (2.3). \(\square\)

### 2.1 Exact scope and the remaining reservoir theorem

The theorem is conditional but not a signed relaxation. Every selected object is an actual owner of one exact factor, and the conclusion is one integral nested trajectory inside that same factor.

Taking (U) to be a whole weak reservoir component in (2.2), and then taking its complement, gives

\[
\delta_q(U)=0.
\tag{2.6}
\]

Thus each active packet must contain exactly equal positive and negative discrepancy. If opposite signs are at directed distance (d), any supported unit path has length at least (d). Bounded (p_q) is therefore a genuine short-recourse hypothesis, not a consequence of small (|\delta_q\|_1) or Hall feasibility.

If (p_q\le p_A), the (b_q) are nearest quotas, and

\[
\sum_{q\le K}\frac{O_q(F)}{c_q}=o(W),
\]

then (1.8) and (2.3) give \(\mathrm{CAHR}_A\). The unproved content is that the same nearest quotas satisfy (2.2) in adjacent-disjoint bounded reservoirs. Neither nearest balance nor point regularity implies those cuts.

If the (b_q) are additionally point-regular, then the selected coordinate-label arcs are Eulerian. Indeed the point effect of (e_{q,X}) is

\[
\mathbf e_{a_q^X}-\mathbf e_{a_{q+1}^X},
\]

and (U_{m-q}(b_q-\mu_q)=0). Thus the selected label arcs decompose into directed coordinate cycles without adding toggles. This removes first-order point imbalance, but not the higher-order target cuts.

### 2.2 Alternation does not create a first-order shortage

There is always one owner two-colouring which splits every deletion-position/coordinate class almost equally.

> **Lemma 2.2.** Put
> 
> \[
> M_0=n(K+1),
> \qquad
> s=\sqrt{\frac B2\log(4M_0)}.
> \]
> 
> There is a colouring (chi:\binom{[n]}m\to\{0,1\}) such that for every (1\le t\le K+1), every (z\in[n]), and both colours (j),
> 
> \[
> \left|
> \#\{X:a_t^X=z, \chi(X)=j\}-\frac B2
> \right|\le s.
> \tag{2.7}
> \]

**Proof.** In every wreath, each coordinate occurs exactly once at each deletion position, so

\[
\#\{X:a_t^X=z\}=B.
\]

Colour owners independently and fairly. Hoeffding gives failure probability at most

\[
2e^{-2s^2/B}=\frac1{2M_0}
\]

for a fixed ((t,z)). A union bound over the (M_0) classes leaves positive probability that none fails. The estimate for the complementary colour is identical. \(\square\)

Taking (R_q=\chi^{-1}(q\bmod2)) gives (2.1). Arcs entering the point star ({S:z\in S}) are exactly the owners with (a_q^X=z), and arcs leaving it are exactly those with (a_{q+1}^X=z). Thus both parity reservoirs retain (B/2+o(B)) first-order in- and out-supply simultaneously: alternation does not annihilate first-order supply. This does **not** establish even the point-star cut unless the prescribed demand also satisfies the corresponding \(B/2+o(B)\) bound; for a point-regular quota the point-star demand is zero. It says nothing about a general family (U) in (2.2), nor about active component size.

## 3. Mobile quotas: exact Hall surcharge and recourse dilation

The preceding theorem prescribes (b_q). A complementary formulation lets the high quota cells move inside each owner component.

Let (C) be a connected loopless multigraph, let \(c\in\mathbb Z_{\ge0}\), and suppose

\[
v=|V(C)|,
\qquad
e=|E(C)|=cv+k,
\qquad
0\le k\le v,
\tag{3.1}
\]

and fix a baseline orientation of indegree vector \(\mu\). A component-compatible balanced quota is

\[
b_H=c\mathbf1+\mathbf1_H,
\qquad H\subseteq V(C),\quad |H|=k.
\]

Let \(\mathcal B_C\) be the nonempty family of \(H\)'s for which \(b_H\) is orientable, and define

\[
\widehat\omega_C
=\min_{H\in\mathcal B_C}\frac12\|b_H-\mu\|_1.
\tag{3.2}
\]

Let \(\tau_C\) be the minimum number of baseline-edge reversals among all orientations with indegree \(b_H\), \(H\in\mathcal B_C\).

### Theorem 3.1 — component transport theorem

\[
\boxed{
\widehat\omega_C\le\tau_C\le(v-1)\widehat\omega_C.
}
\tag{3.3}
\]

**Proof.** Every reversal contributes one head-minus-tail vector, proving the lower bound. Choose a quota attaining \(\widehat\omega_C\), and among its realizing orientations choose one at minimum Hamming distance from the baseline. Direct every changed edge from its old head to its new head. The divergence of this changed-edge digraph is \(b_H-\mu\). If it contained a directed cycle, restoring all edges of that cycle to their baseline heads would preserve every indegree and reduce Hamming distance. Hence it is acyclic.

Its integral flow decomposes into exactly \(\widehat\omega_C\) unit source-to-sink paths. Each is simple and has length at most \(v-1\). Therefore the total number of changed edges is at most \((v-1)\widehat\omega_C\). \(\square\)

Parallel edges cause no difficulty. If \(\widehat\omega_C=0\), the baseline is already balanced and \(\tau_C=0\).

### 3.1 Exact quota-universality criterion

Call (C) **quota-universal** if every (H\subseteq V(C)) of size (k) gives an orientable (b_H).

> **Theorem 3.2.** The component (C) is quota-universal if and only if
> 
> \[
> \boxed{
> i_C(U)\le c|U|+\max\{0,k-(v-|U|)\}
> \qquad(U\subseteq V(C)),
> }
> \tag{3.4}
> \]
> 
> where (i_C(U)) counts internal edges with multiplicity.

**Proof.** A prescribed indegree vector (b) of total (e) is orientable if and only if

\[
i_C(U)\le b(U)
\qquad(U\subseteq V(C)).
\tag{3.5}
\]

The complementary set supplies the other endpoint-capacity inequality. Among all (k)-sets (H), the least possible value of (|H\cap U|) is

\[
\max\{0,k-|V(C)\setminus U|\}.
\]

Minimizing (b_H(U)) in (3.5) gives exactly (3.4). \(\square\)

For comparison, existence of at least one free-high balanced orientation is equivalent to

\[
i_C(U)\le(c+1)|U|,
\qquad
i_C(U)\le c|U|+k
\qquad(U\subseteq V(C)).
\tag{3.6}
\]

The first inequality is the upper-capacity cut; the second is the complement form of the lower-capacity cut.

Define the unconstrained local nearest distance

\[
O_C=\max\left\{
\sum_{z\in C}(c-\mu(z))_+,
\sum_{z\in C}(\mu(z)-c-1)_+
\right\},
\tag{3.7}
\]

and the **Hall surcharge**

\[
\eta_C=\widehat\omega_C-O_C\ge0.
\tag{3.8}
\]

Then Theorem 3.1 reads

\[
\tau_C\le(v-1)(O_C+\eta_C).
\tag{3.9}
\]

Quota-universality implies (eta_C=0), but is stronger than necessary.

### 3.2 Disconnected packet bound

Let a current stage graph have components (C_j). Put

\[
e_j=c v_j+k_j.
\]

A balanced orientation requires (0\le k_j\le v_j) in every component. If every component with (O_{C_j}>0) has at most (L) vertices and is balanceable, then

\[
T\le(L-1)\left(2O+\sum_j\eta_{C_j}\right),
\tag{3.10}
\]

where (O) is the global overload. Indeed,

\[
\sum_jO_{C_j}
=\sum_j\max(A_j,B_j)
\le A+B
\le2\max(A,B)=2O.
\tag{3.11}
\]

Components with (O_{C_j}=0) retain the baseline orientation at zero cost. In particular, quota-universal bad components of size at most (L) give

\[
\boxed{T\le2(L-1)O.}
\tag{3.12}
\]

The factor (2) cannot be deleted from this aggregation without an additional componentwise sign condition: the (A)-defect and (B)-defect can lie in different components.

There is also a weaker bound requiring only (3.6). Any balanced orientation of a bad component reverses at most

\[
e_j\le(c+1)v_j\le(c+1)L
\]

edges. The number of bad components is at most the number of bad vertices, hence at most (A+B\le2O). Therefore

\[
\boxed{T\le2(c+1)LO.}
\tag{3.13}
\]

On a fixed Gaussian window, (c\le C_A), so this remains a constant-factor lift.

### 3.3 Robust packet CAHR lemma

The multistage quantifier is essential because (G_{q+1}(\kappa_{q+1})) rewires exactly the owners toggled at stage (q).

Call a current component canonically bad if it contains a target \(S\) with
\(\mu_q(S)\notin\{c_q,c_q+1\}\). The all-tail orientation has load
\(\mu_q\) in every carried state, so this definition is state-independent
even though the component partition is not.

> **Theorem 3.3 — robust packet CAHR.** Fix (A>0) and (L_A<\infty). Suppose that for all sufficiently large (m) there is one oriented exact factor (F_m) such that
> 
> \[
> \mathcal U_A(F_m):=
> \sum_{q\le K_A}\frac{O_q(F_m)}{c_q}=o(W),
> \tag{3.14}
> \]
> 
> and, for every (q\le K_A) and every carried state reachable from the initial state by a balanced prefix, each current component containing a canonically bad vertex has at most (L_A) vertices and is quota-universal for
> 
> \[
> k_C=e_C-c_qv_C.
> \]
>
> In particular, \(0\le k_C\le v_C\) for every such component.
> 
> Then one actual one-pass balanced trajectory satisfies
> 
> \[
> \sum_{q\le K_A}\frac{T_q}{c_q}
> \le2(L_A-1)\mathcal U_A(F_m)=o(W).
> \tag{3.15}
> \]

**Proof.** At each reached state, leave every component whose canonical loads already lie in ({c_q,c_q+1}) unchanged. On every bad component choose a Hamming-minimum balanced orientation. Equations (3.3), (3.11), and quota-universality give (T_q\le2(L_A-1)O_q). The chosen orientation generates the next carried state, which remains within the robust quantifier. Induct on (q). \(\square\)

The same conclusion, with constant (2(C_A+1)L_A), follows if “quota-universal” is weakened to “balanceable” throughout. It is not enough to prove the property only for the canonical rankwise graphs.

At (q=1),

\[
c_1=1,
\qquad
\rho_1=W-N_1=\frac{2W}{m+2}=o(W).
\tag{3.16}
\]

Under the stronger hypothesis that **every** current component has at most \(L_A\) vertices, all but \(o(W)\) target vertices would lie in bounded unicyclic components: at most \(\rho_1\) components can have positive surplus \(k_C=e_C-v_C\), and every connected zero-surplus balanceable component is unicyclic. Theorem 3.3 itself bounds only canonically bad components, so it does not imply this stronger structural conclusion. This comparison shows how strong a full component packetization theorem would be.

## 4. Sharp recourse obstructions

### 4.1 A quota-universal long cycle

Let (C_v) be a simple cycle, with (c=1) and (k=0). Its only balanced quota is indegree one at every vertex, and it is quota-universal because

\[
i(U)\le|U|
\qquad(U\subseteq V(C_v)).
\]

Start from a directed cyclic orientation and reverse a contiguous block of (h) edges. The resulting load has one (0), one (2), and all other entries (1). Hence

\[
O=\widehat\omega=1.
\]

The only balanced orientations are the two directed cyclic phases, at Hamming distances (h) and (v-h). Therefore, for (h=\lfloor v/2\rfloor),

\[
\tau=\lfloor v/2\rfloor.
\tag{4.1}
\]

This proves that the factor (v-1) in Theorem 3.1 is correct in order. Perfect Hall feasibility and bounded capacity do not imply short recourse.

### 4.2 Zero point defect on an embedded cube

The obstruction survives the first-order point-margin law. The following cube-cycle fact was proved and audited in the adaptive-Hall lane:

> **Imported proved cube-cycle lemma.** For (d=2), and for every (d\ge4), (Q_d) has a Hamilton cycle of length (M=2^d) with four quarter-spaced vertices (A,B,C,D) satisfying
> 
> \[
> \mathbf1_A+\mathbf1_C=\mathbf1_B+\mathbf1_D
> \tag{4.2}
> \]
> 
> after the standard Boolean-cube embedding in a Johnson layer.

Embed (Q_d) in (J(n,r)) by taking a fixed set and choosing one label from each of (d) disjoint coordinate pairs; this requires
\(d\le\min(r,n-r)\). Start with one directed Hamilton phase and reverse the two opposite quarter arcs (A\to B) and (C\to D). The indegree vector is (2) at (A,C), (0) at (B,D), and (1) elsewhere. Thus

\[
O=2,
\qquad
\sum_{S\in V(Q_d)}(\mu(S)-1)\mathbf1_S
=\mathbf1_A+\mathbf1_C-\mathbf1_B-\mathbf1_D=0,
\tag{4.3}
\]

but either balanced cyclic phase differs on exactly (M/2) edges:

\[
\tau=M/2.
\tag{4.4}
\]

This is a Johnson-supported, zero-point-defect stage obstruction. It is not packetized inside an exact wreath factor.

### 4.3 One sibling rewire can amplify cost (1) to (M)

Let

\[
k=v_0,v_1,\ldots,v_{M-1}=h
\]

be a path, add a vertex (s), and add edges (sk,sh). Orient every path edge toward (k) and both added edges toward (s). The baseline loads are (2) at (s), (0) at (h), and (1) elsewhere. In the canonical cycle, reversing (sh) repairs the load in one move.

Now perform one allowed sibling rewire, replacing (sh) by a second parallel edge (sk), while retaining its baseline head (s). In every all-one orientation, the leaf (h) forces the last path edge toward (h); induction forces all (M-1) path edges away from (k), and exactly one parallel edge must point to (k). Therefore

\[
\tau_{\rm canonical}=1,
\qquad
\tau_{\rm rewired}=M.
\tag{4.5}
\]

For

\[
U_j=\{v_j,v_{j+1},\ldots,v_{M-1}\},
\qquad1\le j\le M-1,
\]

the rewired graph satisfies

\[
i(U_j)=|U_j|-1,
\qquad
|\partial U_j|=1.
\]

Thus all (M-1) upper Hall cuts are tight. Before rewiring, (sh) was a second boundary edge and supplied exactly one unit of slack to every one of these nested cuts. A single sibling rewire deletes all of that slack at once.

This proves that a canonical cheap-repair certificate and one common slack
edge need not survive automatically to the next state. It does not refute a
theorem which assumes bounded component order in both states.

### 4.4 A scalable two-rank clone automaton

The previous cascade can be synchronized with a balanced first rank.

> **Theorem 4.1 — abstract two-rank Bellman obstruction.** For every (d\ge4), (M=2^d), there is an abstract two-rank owner automaton with
> 
> \[
> c_1=c_2=1,
> \qquad
> P=4M+7\text{ owners at each rank},
> \]
> 
> such that both ranks are balanceable, the canonical overloads are
> 
> \[
> O_1=2,
> \qquad
> O_2=4,
> \tag{4.6}
> \]
> 
> all first-order signed defects cancel in a formal cloned point-label ledger, but the exact two-stage Bellman value is
> 
> \[
> R_1=2M+4.
> \tag{4.7}
> \]

**Construction and proof.** Take four rank-two traps indexed by (i=0,1,2,3). Trap (i) has vertices

\[
s_i,v_{i,0},\ldots,v_{i,M-1},
\qquad
k_i=v_{i,0},\quad h_i=v_{i,M-1},
\]

path owners (p_{i,j}=v_{i,j-1}v_{i,j}), an owner (f_i=s_ik_i), and a special owner (g_i). Canonically (g_i=s_ih_i); if its rank-one control toggles, it rewires to a second (s_ik_i). The baseline heads are (v_{i,j-1}) on every path edge and (s_i) on (f_i,g_i). Each trap therefore has load (2) at (s_i), (0) at (h_i), and (1) elsewhere. Its canonical and rewired repair costs are (1) and (M), respectively, by (4.5).

At rank one, the four special owners form a square (AB,BC,CD,DA). Their baseline heads are (A,C,C,A), so their loads are

\[
(2,0,2,0).
\]

Every balanced orientation of this square is one of its two directed phases and toggles exactly one opposite pair of special owners. Hence exactly two rank-two traps rewire.

Freeze the (4M) nonspecial trap owners at rank one as leaf edges attached to a core triangle, with each baseline head at its leaf. Add the three triangle owners as fillers. Every all-one orientation keeps every leaf owner at its baseline head; the filler triangle can retain its phase or reverse all three edges.

At rank two, give the three filler owners a separate three-vertex component
disjoint from all four traps. In the retained filler phase it is the
baseline directed \(3\)-cycle and costs zero. Stipulate in the abstract
automaton that every other filler state remains disjoint from the traps and
is either balanceable at nonnegative cost or infeasible. Hence it can never
lower a trap cost. Every balanced first stage toggles exactly two controls
and no nonspecial trap owner; its minimum cost is \(2\), attained by
retaining the filler phase. At rank two, two traps cost \(M\) and two cost
\(1\), for total \(2M+2\). This proves (4.7) and accounts for all \(4M+7\)
owners and vertices at both ranks.

In the formal cloned point-label ledger, the square defect can be labelled by a Boolean rectangle

\[
A=R+p_0+q_0,
\quad B=R+p_1+q_0,
\quad C=R+p_1+q_1,
\quad D=R+p_0+q_1,
\]

so

\[
\mathbf1_A+\mathbf1_C-\mathbf1_B-\mathbf1_D=0.
\tag{4.8}
\]

The adjacent-swap realization is explicit. In general, an owner
\(X=C_0\cup\{x,y,z\}\) with deletion word \((z,y,x)\) has rank-one
endpoints
\[
C_0\cup\{x,y\},\qquad C_0\cup\{x,z\},
\]
and its canonical/rewired rank-two edges are
\[
C_0\cup\{x\}\ --\ C_0\cup\{y\},
\qquad
C_0\cup\{x\}\ --\ C_0\cup\{z\}.
\tag{4.8a}
\]
Use, around \(AB,BC,CD,DA\), the four words
\[
(p_1,p_0,q_0),\quad
(q_0,q_1,p_1),\quad
(p_0,p_1,q_1),\quad
(q_1,q_0,p_0).
\tag{4.8b}
\]
Their rank-two triples \((s_i,h_i,k_i)\) are
\[
(Rq_0,Rp_0,Rp_1),\quad
(Rp_1,Rq_1,Rq_0),\quad
(Rq_1,Rp_1,Rp_0),\quad
(Rp_0,Rq_0,Rq_1),
\tag{4.8c}
\]
where \(Rt\) abbreviates \(R\cup\{t\}\).

The two possible control-toggle pairs are opposite coordinate arcs and hence Eulerian in that ledger. The four trap defects can likewise be labelled, with multiplicity, so that

\[
\sum_{i=0}^3(\mathbf1_{s_i}-\mathbf1_{h_i})=0.
\tag{4.9}
\]

For one rewired trap the formal incidence effect of the forced path and
parallel-edge toggles telescopes to
\(\mathbf1_{h_i}-\mathbf1_{s_i}\), exactly cancelling that trap's formal
baseline point defect. Thus the long recourse survives the first-order law
inside the clone model. This is not a simultaneously injective point-margin
realization in one Boolean layer.

For (L) disjoint copies, put (W^*=L(4M+7)). Then

\[
O_1+O_2=6L=o(W^*)
\qquad(M\to\infty),
\]

while

\[
\frac{R_1}{W^*}\longrightarrow\frac12.
\tag{4.10}
\]

The local floor capacities \(c_1=c_2=1\) match the fixed-window floors for large \(m\):

\[
c_1=\left\lfloor\frac{m+2}{m}\right\rfloor=1,
\]

and

\[
c_2=\left\lfloor
\frac{(m+2)(m+3)}{m(m-1)}
\right\rfloor=1
\qquad(m\ge8).
\tag{4.11}
\]

For every fixed (A>0), both ranks lie in the Gaussian window for all sufficiently large (m).

The module itself has equal local edge and vertex counts and no high slots;
an actual layer has positive global remainder \(\rho_q\). Abstract surplus
components could be appended, but no exact-factor realization follows.

**Exact scope.** The four control diamonds can be realized by literal adjacent-swap words. A rank-two cube trap is individually Johnson-embeddable when \(d\le\min(r,n-r)\); at the literal \(q=2\) layer this requires \(d\le m-2\). Thus the comparison \(M\to\infty\) uses a joint choice \(d=d(m)\to\infty\), \(d(m)\le m-2\). The embedding and ambient completion may depend on the trap. The full freezing overlay uses cloned target labels and is not proved simultaneously realizable by Boolean sets, cyclic wreath rows, or one exact factor. Theorem 4.1 therefore refutes a black-box owner-graph theorem, not existential \(\mathrm{CAHR}_A\).

This scope is substantive. Trap geometry alone has a cheap natural prefix,
and the following owner-injective construction shows the escape explicitly.
On \(\mathbb Z_n\), write
\(I(j,r)=\{j,j+1,\ldots,j+r-1\}\) modulo \(n\), put
\[
v_j=I(j,m-2)\qquad(0\le j<n),
\]
delete \(v_{n-1}v_0\), set
\[
C=v_{n-1}\cap v_0,\qquad x=m,\qquad s=C\cup\{x\},
\]
and add \(sv_0,sv_{n-1}\). With
\[
U_j=I(j,m-1),\qquad
F=s\cup v_0,\qquad G=s\cup v_{n-1},
\]
the preceding-rank union sequence
\[
F,U_0,\ldots,U_{n-2},G
\]
is a simple Johnson cycle with distinct middle owners. However its
successive no-toggle intersections are
\[
v_0,v_1,\ldots,v_{n-1},s.
\]
Thus the rank-two orientation is already all-one; after rewiring
\(sv_{n-1}\) to a second \(sv_0\), retaining head \(s\), it remains all-one.
This is a literal cheap balanced decoration of the underlying trap graph,
not a realization of the defective \(1\to n\) recourse cascade. An
owner-injective literal realization of that defective two-rank trap, a
four-trap control square, protected isolation, positive-density wreath
packetization, and exact-factor completion all remain unproved.

### 4.5 A genuine exact-factor row-local barrier

At (q=1), the coordinate effects of the owners in one wreath form a directed Hamilton (n)-cycle on the coordinate labels. If a correction packet is required to preserve point margins **inside each row separately**, then the selected subset of this directed cycle must be Eulerian. It is therefore either empty or the whole cycle.

Consequently every nonempty row-separable point-regular packet costs at least (n) owner toggles. A correction active in (R) rows costs at least (nR); since (W=nB), an (o(W)) correction can touch only (o(B)) rows in this architecture. Cross-row coordinate cycles can evade the conclusion. Thus this is a genuine exact-factor obstruction to rowwise packetization, not to general packetization.

There is a related exact sparse law. Every balanced (q=1) orientation has exactly

\[
\rho_1=\frac{2W}{m+2}
\tag{4.12}
\]

high vertices. Delete one incoming edge at each high vertex. The **reduced**
oriented graph has indegree exactly one everywhere, so every weak component
of that reduced graph is unicyclic. For indegree-one orientations of the
reduced graph, all tree edges are forced and only the cycle phase remains
free. Reinserted surplus edges can change this geometry. Hall feasibility
and the edge-count law alone therefore do not supply short recourse; a
positive theorem must control the reduced cycle phases and geometry or
exploit the \(o(W)\) surplus edges.

In wreath units the first two exact surplus ledgers are
\[
\frac{\rho_1}{B}
=\frac{2(2m+1)}{m+2}
=4-\frac6{m+2},
\tag{4.13}
\]
and, when \(m\ge8\) so that \(c_2=1\),
\[
\frac{\rho_2}{W}
=\frac{6(m+1)}{(m+2)(m+3)},
\qquad
\frac{\rho_2}{B}
=\frac{6(2m+1)(m+1)}{(m+2)(m+3)}
\longrightarrow12.
\tag{4.14}
\]
Thus only boundedly many surplus high slots are available per wreath row at
the first two ranks, despite the global \(o(W)\) surplus.

## 5. Classification of support-feasible packets in a fixed-star exact-factor fibre

Fix a coordinate (v\). Write

\[
P_v=\{M:v\in M\},
\qquad
Q_v=\{M:v\notin M\}.
\]

Every (P_v)-trace of a wreath has exactly two unoriented lifts, differing by the swap of two adjacent gap labels (x,y). For a wreath (E), let (R_E) be its two variable (Q_v) middle sets and (A_E) those of its twin. In an exact factor (F), define the partial map

\[
\phi(E)=E'
\quad\Longleftrightarrow\quad
A_E=R_{E'},
\tag{5.1}
\]

leaving it undefined if (A_E) meets the fixed (Q_v)-part.

### Theorem 5.1 — fixed-star exact fibre classification

Assume (m\ge4).

1. Replacing a set \(I\subseteq F\) of wreaths by their twins gives an exact factor if and only if \(I\) is a union of directed \(\phi\)-cycles. Every such cycle has length at least \(4\).

2. Let (F_I,F_J) be two exact states in this fibre and put (k=|I\triangle J|). With coherent orientations, the changed rows have exactly (k) common paths of order (n-2) and (k) common paths of order (2). Exactly (2k) middle owners change rows, and there are exactly (2k) old and (2k) new factor seams.

3. For (1\le q\le m-2), (r=m-q), the rank-(r) histogram difference is a sum of (k) four-cell rectangles

\[
\mathbf1_{S\cup\{y\}}
+\mathbf1_{R\cup\{x\}}
-\mathbf1_{S\cup\{x\}}
-\mathbf1_{R\cup\{y\}}.
\tag{5.2}
\]

Every rectangle has four distinct cells, zero total, and zero point margins. Hence

\[
\frac12\|\mu_q(F_I)-\mu_q(F_J)\|_1\le2k.
\tag{5.3}
\]

At the middle rank the total difference is exactly zero by cycle conservation, and at singleton rank it is also zero.

4. With the same coherent orientations, at every (1\le q\le m-1) the canonical pointed owner mismatch is at most (3k): the (2k) reassigned owners are charged in full, and exactly (k) common owners can change their lower flag. Therefore, for (K\le m-2),

\[
\sum_{q\le K}\frac{
\frac12\|\mu_q(F_I)-\mu_q(F_J)\|_1}{c_q}
\le2kS_A(m),
\tag{5.4}
\]

and the weighted pointed owner mismatch is at most

\[
3kS_A(m).
\tag{5.5}
\]

**Proof.** Exactness after a twin replacement is equivalent to

\[
\{A_E:E\in I\}=\{R_E:E\in I\}
\]

as multisets, which is exactly the assertion that \(\phi|_I\) permutes \(I\). Loops are impossible because \(A_E\cap R_E=\varnothing\), and two-cycles force two traces to share a \(P_v\) endpoint. For a hypothetical three-cycle, choose representatives of the unordered complementary variable pairs recursively along the three Johnson adjacencies. After the third step the representative is either the initial set or its complement. The latter has Johnson distance \(m>3\) from the initial set when \(m\ge4\), so it is impossible. The three representatives therefore form a genuine Johnson triangle. Every Johnson triangle is either a star with a common \((m-1)\)-set or a top inside a common \((m+1)\)-set. In the first case all three traces share the corresponding \(P_v\) endpoint; in the second their complementary side cores give a common \(P_v\) endpoint. Both contradict exactness.

An adjacent gap swap changes exactly two cyclic (r)-intervals, giving (5.2). The path profile follows by cutting at the two variable starts. At lower rank, precisely one common start per changed trace lies outside the two reassigned middle starts; this gives the additional (k) pointed mismatches. Summing the rankwise bounds proves (5.4) and (5.5). \(\square\)

Since (k\le B=W/n), (1.3) gives the full-fibre diameter bounds

\[
2BS_A(m)
=\left(s_A+o_A(1)\right)\frac W{\sqrt m},
\tag{5.6}
\]

and

\[
3BS_A(m)
=\left(\frac32s_A+o_A(1)\right)\frac W{\sqrt m}.
\tag{5.7}
\]

These bounds hold for an arbitrary-length chain inside the same fixed-star fibre, because every state is determined by a subset of the vertex-disjoint \(\phi\)-cycle bits. Repeated switching cannot accumulate more than the fibre diameter.

### 5.1 Exact transport of one-pass decisions across a gap swap

Suppose one common owner's deletion word changes by transposing positions (t,t+1). For (2\le t\le K), transform the old bits ((\varepsilon_{t-1},\varepsilon_t)) by

\[
00\mapsto01,
\qquad
01\mapsto00,
\qquad
10\mapsto01,
\qquad
11\mapsto11.
\tag{5.8}
\]

The carried state after stage \(t\) is unchanged, and every chosen lower set agrees except possibly at depth \(t-1\). Because \(c_q\) is nondecreasing, the weighted cost increase is at most \(1/c_t\). At \(t=1\), flip \(\varepsilon_1\); this preserves both \(P_1\) and \(\kappa_2\) and increases cost by at most \(1/c_1\). At the right boundary \(t=K+1\), keep \(\varepsilon_K\); no cost is added and only the depth-\(K\) target can differ, when \(\varepsilon_K=1\).

Applying this ownerwise gives the following exact approximate-stability statement.

For each changed trace and each \(1\le t\le K+1\), exactly one fixed common
owner sees the gap labels in deletion positions \(t,t+1\). Consequently,
cost can increase on at most \(k\) common owners at each \(t\le K\), while
at rank \(q\) only the \(t=q+1\) common owners can contribute a transported
load discrepancy.

> **Corollary 5.2.** Suppose (F_I) has a balanced one-pass trajectory of weighted cost (C), and switch (k) traces to another exact fibre state (F_J), orienting every new twin coherently with its old row as in Theorem 5.1. Transport every common owner's decisions by (5.8), and choose no toggles on the (2k) reassigned owners. The result is one genuine one-pass trajectory for (F_J) with cost at most
> 
> \[
> C+kS_A(m),
> \tag{5.9}
> \]
> 
> whose rank-\(q\) load differs from the old balanced load by half-\(\ell^1\) at most \(3k\). Hence its total weighted integral quota defect is at most
> 
> \[
> 3kS_A(m).
> \tag{5.10}
> \]

For (k\le B), both errors are (O_A(W/\sqrt m)=o(W)). The corollary preserves an approximate CAHR trajectory, not exact balance. Retracting the (O(k))-supported residual at all ranks by one nested short flow is precisely the missing packetized Hall theorem.

There is a useful cutwise stability bound when the same prescribed quota
\(b_q\) and the same owner reservoir are transported ownerwise between the
coherently oriented states. At a fixed rank, at most \(3k\) fixed-owner
canonical arcs and at most \(2k\) reassigned-owner arcs can change, so every
transported-reservoir cut capacity changes by at most \(5k\). The histogram
demand changes on any target family by at most \(2k\). Therefore every
prescribed cut slack changes by at most

\[
7k.
\tag{5.11}
\]

This is only a fixed-\((b_q,R_q)\) Lipschitz estimate. If the quota is
reselected or reservoir membership is recomputed, their transfer distances
must be added. A single changed arc can merge two weak components, so (5.11)
gives no bound on the packet order \(p_q+1\) and no favourable sign.

### 5.2 Why the exact fibre packets do not close CAHR

The fixed-star theorem is a genuine support-feasible exact-factor packet theorem, but it has four decisive limitations.

1. A given exact factor need not contain any directed \(\phi\)-cycle for the chosen star.
2. The whole fibre has only \(O_A(W/\sqrt m)\) weighted histogram diameter. It cannot repair a \(\Theta(W)\) weighted defect.
3. Repeated switches in the same fibre never escape the same cycle-bit cube. One must change the star or the projected trace family by another exact-factor move.
4. Corollary 5.2 leaves an integral residual. Point and histogram cancellation do not orient that residual through short owner paths.

Thus exact packet availability and short higher-order Hall retraction remain separate theorems.

## 6. Clean final lemma and exact implication scope

The strongest clean theorem target exposed by this lane is the following.

> **Bounded Packet Retraction \(\mathrm{BPR}_A\) — unproved exact-factor lemma.** For every fixed (A>0), all sufficiently large (m) admit one oriented exact factor (F_m), balanced quotas (b_q), and owner reservoirs (R_q) for (1\le q\le K_A), such that:
> 
> 1. \(R_0=\varnothing\) and \(R_q\cap R_{q-1}=\varnothing\);
> 2. for every target family (U),
>    
>    \[
>    (b_q-\mu_q)(U)\le|\partial^-_{R_q}(U)|;
>    \]
> 3. every reservoir component meeting \(\operatorname{supp}(b_q-\mu_q)\) has at most \(p_A+1\) vertices, for a constant \(p_A\) independent of \(m\);
> 4. 
>    \[
>    \sum_{q\le K_A}
>    \frac{\|b_q-\mu_q\|_1}{2c_q}=o(W).
>    \]

Theorem 2.1 proves, with no further hypothesis,

\[
\mathrm{BPR}_A\Longrightarrow\mathrm{CAHR}_A.
\tag{6.1}
\]

The robust mobile-quota alternative is Theorem 3.3: replace prescribed reservoirs by uniformly bounded balanceable bad components in **every** state reachable by any balanced prefix. Quota-universality gives the improved coefficient (2(L_A-1)); ordinary free-high Hall gives (2(C_A+1)L_A).

\(\mathrm{BPR}_A\) alone yields one integral balanced nested flag resolution at weighted mismatch \(o(W)\); its condition 4 already implies weighted overload \(o(W)\) by (1.9). The robust mobile-component alternative yields the same conclusion together with the separate overload hypothesis (3.14). Fixed-\(A\) labelled alignment then diagonalizes to labelled synchronization, which is sufficient for MWB and the final OR construction. The reverse implications are not claimed: labelled synchronization is strictly stronger than MWB, and both packet properties are stronger than the existential conclusion of \(\mathrm{CAHR}_A\).

In the abstract owner-graph and clone-automaton category, the obstructions prove that none of the following replacements is valid:

\[
\text{small overload} + \text{stagewise Hall}
\Longrightarrow \text{short recourse},
\]

\[
\text{small overload} + \text{zero point defect}
\Longrightarrow \text{short recourse},
\]

or

\[
\text{canonical repair cost }1\text{ with common Hall slack}
\Longrightarrow \text{dynamically short repair}.
\]

The last display does not refute a theorem assuming genuinely bounded
component order in both states; the canonical and rewired traps themselves
have growing order.

The exact-factor row theorem additionally rules out independent point-regular packets inside single wreath rows.

Any one of the following concrete positive routes would suffice; they are
not claimed to exhaust all possible proofs:

1. adjacent-disjoint canonical reservoirs satisfying every higher-order cut and having bounded active components;
2. robustly bounded balanceable bad components in every state reachable by any balanced prefix, as quantified in Theorem 3.3;
3. a different exact macrotrade family which transports the residual of Corollary 5.2 through one common nested flow.

No signed-factor argument suffices for any of these. No local Johnson or clone-graph obstruction currently lifts to a protected positive-density packet system inside one exact factor. Therefore the third-wave L lane narrows the conjecture to a genuine positive/support-feasible exact-factor theorem, but neither proves nor disproves that theorem.

## 7. Proved/open ledger

### Proved here

1. The alternating canonical-reservoir lift, including exact cut signs, integral path decomposition, constants, and temporal gluing.
2. The exact nearest balanced-quota identity and the necessary lower bound (O_q\le T_q).
3. Rankwise point-regular quota repair with explicit loss ((m-q+1)O_q).
4. A simultaneous alternating reservoir split retaining (B/2+o(B)) supply in every point-star class.
5. The component transport inequality \(\widehat\omega\le\tau\le(v-1)\widehat\omega\).
6. The exact quota-universality criterion and the Hall-surcharge decomposition.
7. The robust bounded-component CAHR theorem, with constants (2(L_A-1)) and (2(C_A+1)L_A).
8. The order-sharp long-cycle obstruction and the imported audited zero-point cube obstruction.
9. The one-rewire nested-cut cascade and the scalable **abstract** two-rank clone Bellman obstruction.
10. The genuine exact-factor row-local Eulerian barrier and the exact post-deletion depth-one unicyclic law.
11. The fixed-star exact packet-cube theorem, including cycle length at least four, histogram constant (2k), pointed constant (3k), and full-fibre (O_A(W/\sqrt m)) diameter.
12. Exact one-pass transport across a gap swap, approximate-CAHR stability, and the (7k) cut-slack Lipschitz bound.

### Still unproved

1. \(\mathrm{BPR}_A\), robust dynamic packetization, or any other unconditional \(\mathrm{CAHR}_A\) theorem.
2. Existence of enough directed fixed-star lift cycles in a useful exact factor.
3. Exact balanced retraction of the (O(k))-per-rank residual in Corollary 5.2.
4. Positive-density completion of the clone or cube obstruction inside one exact wreath factor.
5. A genuine exact-factor counterexample to existential cyclic alignment or MWB.
