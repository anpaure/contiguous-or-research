The adjacent-deletion swap lane is a genuine improvement over the prefix-release route: it preserves labelled ownership, isolates one rank exactly, and charges rejoining chains only once. It still does not prove MWB, because the evolving orientation graphs need a new adaptive Hall-and-cost theorem.

## 1. Exact rank-isolation theorem

Fix an oriented exact factor \(F\). Extend each owner’s cyclic deletion word to
\[
a^X=(a_1,\ldots,a_{K+1}).
\]
Process stages \(q=1,\ldots,K\). At stage \(q\), optionally transpose the current letters in positions \(q,q+1\).

Before stage \(q\), earlier swaps occurred wholly inside positions \(1,\ldots,q\). Hence
\[
\{w_1,\ldots,w_q\}=\{a_1,\ldots,a_q\}, \tag{1}
\]
while position \(q+1\) is still \(a_{q+1}\).

Therefore the two possible depth-\(q\) sets are
\[
S_X=L_q^F(X)
=X\setminus\{a_1,\ldots,a_q\}, \tag{2}
\]
and, writing \(u=w_q\),
\[
S'_X=S_X-\{a_{q+1}\}+\{u\}. \tag{3}
\]
They are distinct.

A stage-\(q\) swap changes only the set of the first \(q\) deleted letters:

- shallower prefixes omit both positions;
- deeper prefixes contain both positions;
- later stages touch only positions after \(q\).

Thus all final maps come from one deletion word per owner and form one common nested resolution. If \(T_q\) owners toggle at stage \(q\), then exactly
\[
\boxed{e_q(F,P)=T_q.} \tag{4}
\]

This is sharper than the marked-run or owner-tail bounds because the chains diverge at depth \(q\) and automatically rejoin at \(q+1\).

## 2. Exact stagewise orientation theorem

Let \(G_q\) be the multigraph on \(\binom{[n]}{m-q}\) having the owner edge
\[
S_XS'_X
\]
for each \(X\). Orienting the edge toward \(S_X\) means no toggle; orienting it toward \(S'_X\) means toggle. Vertex indegrees are precisely the depth-\(q\) fiber loads.

For \(U\subseteq V(G_q)\), let:

- \(i_q(U)\) be the number of internal edges;
- \(\partial_q(U)\) be the number of edges with exactly one endpoint in \(U\);
- \(b(U)=\sum_{S\in U}b(S)\).

### Prescribed quotas

A prescribed load vector \(b\) is orientable exactly when
\[
b(V)=W
\]
and
\[
\boxed{
i_q(U)\le b(U)\le i_q(U)+|\partial_q(U)|
\quad\text{for every }U.
} \tag{5}
\]

Every internal edge must contribute one unit to \(U\), while every boundary edge may contribute zero or one. Sufficiency follows from the integral flow connecting each unit-supply owner edge to its two possible endpoints.

### Unprescribed balanced quotas

An orientation with every load in \(\{c_q,c_q+1\}\) exists exactly when
\[
\boxed{
i_q(U)\le(c_q+1)|U|,
\qquad
c_q|U|\le i_q(U)+|\partial_q(U)|
} \tag{6}
\]
for every \(U\). Since \(W=c_qN_q+\rho_q\), feasibility automatically gives exactly \(\rho_q\) high-load vertices.

On a fixed window \(q\le A\sqrt m\),
\[
\frac{2|E(G_q)|}{|V(G_q)|}
=\frac{2W}{N_q}=O_A(1).
\]
Thus these are genuinely sparse orientation problems; their Hall cuts cannot be replaced by dense expansion heuristics.

## 3. Exact toggle cost

Direct every edge from its no-toggle endpoint to its alternate endpoint. Let \(\mu_q\) be the original factor histogram and let \(b\) be the chosen balanced load. If \(B_D\) is the directed incidence matrix, then
\[
\boxed{
\tau_q(b)=
\min\left\{
\sum_ex_e:
B_Dx=b-\mu_q,\ 0\le x_e\le1
\right\}.
} \tag{7}
\]
The optimum is integral by total unimodularity and equals the minimum number of owner toggles.

Every toggle moves one unit between two histogram cells, so
\[
\tau_q(b)\ge\frac12\|b-\mu_q\|_1. \tag{8}
\]
Consequently
\[
\boxed{O_q(F)\le\tau_q(b)=e_q.} \tag{9}
\]

The inequality can be strict. In the abstract directed graph with two arcs \(u\to v\) and one arc \(v\to w\),
\[
\mu=(2,1,0),\qquad b=(1,1,1).
\]
The histogram distance is one, but realizing \(b\) requires one \(u\to v\) toggle and the \(v\to w\) toggle, so \(\tau=2\).

This exhibits the precise distinction from overload: histogram mass may need to travel through several supported owner edges.

## 4. The dynamic obstruction

Although each operation is rank-isolated in the final resolution, the graphs are not independent. A stage-\(q\) toggle changes the letter carried into position \(q+1\), hence changes the alternate endpoints in \(G_{q+1}\).

Therefore:

- \(G_q\) must be rebuilt after all earlier choices;
- a minimum-cost orientation of \(G_q\) may destroy Hall feasibility at later stages;
- separate feasible or optimal orientations do not prove one common resolution.

The exact missing statement is:

> **UNPROVED — adaptive owner-orientation lemma.**  
> For every fixed \(A>0\), there exist one exact oriented wreath factor and sequential balanced orientations of the evolving graphs
> \[
> G_1,\ldots,G_{\lceil A\sqrt m\rceil}
> \]
> satisfying all cuts (6) and
> \[
> \boxed{
> \sum_{q\le A\sqrt m}\frac{T_q}{c_q}=o(W).
> }
> \tag{AO\(_A\)}

By (4), \((\mathrm{AO}_A)\) implies the labelled fixed-window theorem. Diagonalization then gives labelled SYNC.

The implication hierarchy is
\[
\boxed{
\text{adaptive swaps}
\Longrightarrow
\text{labelled SYNC}
\Longrightarrow
\text{overload MWB}
\Longrightarrow
\text{final OR bound}.
}
\]
No reverse implication is known.

In particular, fixed-window
\[
\min_F\sum_q O_q(F)/c_q=o(W)
\]
is equivalent to overload MWB by diagonalization, but it does not provide a nearby nested labelled flow or feasible orientations of the \(G_q\).

## 5. Comparison with the cyclic-flow reductions

- **Versus variable release:** release flow fixes an initial cyclic prefix and charges every later depth after release. A rank-isolated swap rejoins immediately, so release flow may overcharge one toggle by an entire \(\Psi\)-tail.

- **Versus marked runs:** marked-run control rewards cyclic clustering of successor-law violations. Adjacent swaps can be scattered and create many marks while still having the exact small cost \(\sum_qT_q/c_q\). Conversely, marked-run constructions allow changes not reachable by one ascending adjacent-swap pass.

- **Versus ordinary stable matching:** the orientation theorem retains the actual owner edge \(S_XS'_X\). It therefore includes the geometric Hall constraints missing from matching based only on point or tuple margins.

- **Point margins:** if exact point-compatible quotas are desired, prescribe regular high-quota families in (5). Without imposing them, every toggle changes two point incidences, so
  \[
  \|\delta_q\|_1\le2T_q,\qquad
  \|\delta_q\|_\infty\le T_q.
  \]

A useful hybrid could perform supported swaps for active owners and release a small exceptional set into the residual Hall flow, with total charge
\[
\sum_q\frac{T_q^{\rm active}}{c_q}
+\sum_X\Psi_{m,H}(\alpha(X)).
\]
That hybrid also remains unproved.

## Audit corrections

The rank-isolated construction requires
\[
K+1\le m,
\]
and every owner word \((a_1,\ldots,a_{K+1})\) consists of distinct deletion letters.

For each \(q\), the **final** depth-\(q\) mismatch is exactly the stage-\(q\) toggle: earlier swaps preserve the unordered first-\(q\) deletion set, and later swaps do not touch it. Thus
\[
e_q=T_q.
\]
The separate balanced loads selected at the stages constitute one common nested balanced resolution only after all stages have been completed and the final owner words are read simultaneously.

Every graph \(G_q\) is a loopless multigraph. Parallel owner edges are retained and counted with multiplicity. There are no loops because the current position-\(q\) and position-\((q+1)\) deletion letters are distinct, so the two possible intermediate rank-\((m-q)\) sets are distinct.

Equation (9) must be read as the chain
\[
\boxed{
O_q(F)
\le \frac12\|b-\mu_q\|_1
\le \tau_q(b)
\le T_q
=e_q.
} \tag{9'}
\]
Here \(T_q\) is the number of toggles in the orientation actually selected at stage \(q\). Equality \(\tau_q(b)=e_q\) holds only when that selected orientation is a minimum-toggle orientation for the prescribed load vector \(b\).

The dynamic dependence of \(G_{q+1}\) is ownerwise: its alternate endpoint for owner \(X\) depends on the particular deletion letter carried into position \(q+1\) by the earlier decisions for that same owner. Aggregate stage histograms do not determine the future graph.

The adaptive statement \((\mathrm{AO}_A)\) is a sufficient labelled theorem. It is strictly stronger than overload MWB and is not claimed to be equivalent to it. In particular, overload MWB does not supply supported owner edges, dynamically feasible orientations, or one common nested labelled resolution.

For the point-margin comparison, the deviation used above is
\[
\delta_{q,x}
=\#\{X:x\in P_q(X)\}
-\frac{(m-q)W}{n}.
\]
A stage-\(q\) toggle exchanges one retained coordinate for another, giving
\[
\|\delta_q\|_1\le2T_q,
\qquad
\|\delta_q\|_\infty\le T_q.
\]

In the hybrid formulation, \(\alpha(X)\) denotes the last depth through which owner \(X\) remains in the cyclic/swap-controlled system before it is permanently released to the residual nested flow, and
\[
\Psi_{m,H}(\alpha(X))
=\sum_{q=\alpha(X)+1}^{H}\frac1{c_q}.
\]
After release, no later owner-specific swap agreement is claimed; its remaining depths are charged by this finite tail.
