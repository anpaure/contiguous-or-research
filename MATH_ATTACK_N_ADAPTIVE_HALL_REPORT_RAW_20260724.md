Outcome: \(\mathrm{SDH}_A/\mathrm{AO}_A\) remains open. I found neither a proof of simultaneous Hall feasibility and \(o(W)\) recourse nor an exact-wreath counterexample. The lane is now sharply localized: all first-order marginals and generic network-flow arguments can be eliminated, while the surviving obstruction is exact locally but lacks linear packetization into one exact factor.

## 1. Exact adaptive-state theorem

For owner \(X\), let \(a_1,\ldots,a_{K+1}\) be its canonical deletion word and

\[
L_q(X)=X\setminus\{a_1,\ldots,a_q\}.
\]

Let \(\varepsilon_q(X)=1\) denote a stage-\(q\) toggle. Define the carried letter

\[
\kappa_1=a_1,\qquad
\kappa_{q+1}=
\begin{cases}
\kappa_q,&\varepsilon_q=1,\\
a_{q+1},&\varepsilon_q=0.
\end{cases}
\]

Then, exactly,

\[
\boxed{P_q(X)=L_{q+1}(X)\cup\{\kappa_{q+1}(X)\}.}
\]

Before deciding at depth \(q\), the owner edge is

\[
\boxed{
L_q(X)\;-\;\bigl(L_{q+1}(X)\cup\{\kappa_q(X)\}\bigr).
}
\]

Its intersection and union are

\[
\boxed{
u_X\cap v_X=L_{q+1}(X),\qquad
u_X\cup v_X=P_{q-1}(X).
}
\]

Thus \(P_q=L_q\) iff \(\varepsilon_q=0\), proving again

\[
\boxed{e_q=T_q.}
\]

Maximal toggle runs correspond exactly to consecutive blocks \([s,t]\) on which

\[
(a_s,\ldots,a_t)\mapsto(a_{s+1},\ldots,a_t,a_s),
\]

and, for \(s\le q<t\),

\[
P_q=L_{q+1}\cup\{a_s\}.
\]

Hence the adaptive problem is equivalently one static integer selection of an interval composition for every owner. There is no residual online ambiguity.

For fixed \(A\), one may take \(C_A=\lceil e^{A^2+2}\rceil\) for all sufficiently large \(m\), so

\[
1\le c_q\le C_A\qquad(q\le K_A).
\]

Therefore

\[
C_A^{-1}\sum_qT_q
\le\sum_q\frac{T_q}{c_q}
\le\sum_qT_q.
\]

Consequently \(\mathrm{SDH}_A\) and \(\mathrm{AO}_A\) are equivalent formulations of the same fixed-window missing theorem.

## 2. Earlier choices alter exactly the preceding toggle set

Let \(H_q\) be the canonical sibling graph with edge

\[
L_q(X)\;-\;\bigl(L_{q+1}(X)\cup\{a_q(X)\}\bigr).
\]

For \(q\ge2\),

\[
\kappa_q=a_q\iff\varepsilon_{q-1}=0.
\]

Hence \(G_q\) is obtained from \(H_q\) by rewiring exactly the \(T_{q-1}\) labelled owner edges toggled at depth \(q-1\). Only their alternate endpoints change; anchors and intersections remain fixed. Thus, for every vertex family \(U\),

\[
|e_{G_q}(U)-e_{H_q}(U)|\le T_{q-1}.
\]

The exact evolving invariants are:

\[
\text{intersection histogram}=\mu_{q+1},
\]

\[
\text{union histogram}=b_{q-1},
\]

\[
\text{canonical-endpoint histogram}=\mu_q.
\]

In particular, the unions are already balanced:

\[
b_{q-1}(T)\in\{c_{q-1},c_{q-1}+1\}.
\]

The history is therefore sparse in support but not in effect: a changed head may remember an arbitrarily old carry.

## 3. Every one-coordinate Hall cut is automatically safe

Put \(r=m-q\), \(B=W/n\), and

\[
\Delta_{q,x}
=\#\{X:x\in P_q(X)\}-rB.
\]

If \(C_q(x)=\#\{X:\kappa_q(X)=x\}\), then

\[
C_q(x)=B+\Delta_{q-1,x},
\]

and

\[
\Delta_q
=\sum_{X:\varepsilon_q(X)=1}
\bigl(\mathbf e_{\kappa_q(X)}-\mathbf e_{a_{q+1}(X)}\bigr).
\]

Therefore

\[
\|\Delta_q\|_1\le2T_q,\qquad
\|\Delta_q\|_\infty\le T_q.
\]

If \(U_x=\{S:x\in S\}\), direct edge counting gives

\[
e_{G_q}(U_x)=(r-1)B,
\]

\[
|\partial_{G_q}(U_x)|=B+C_q(x),
\]

\[
e_{G_q}(U_x^c)=(n-r)B-C_q(x).
\]

Writing \(W=c_qN_q+\rho_q\), balanced orientation is equivalent to

\[
e_G(U)\le(c_q+1)|U|,
\qquad
e_G(U)\le c_q|U|+\rho_q
\]

for every \(U\). Substituting the displayed counts and using

\[
c_qN_q\le W<(c_q+1)N_q
\]

shows both cuts for \(U_x\) and \(U_x^c\) have nonnegative slack for every history.

Thus:

\[
\boxed{\text{Any Hall obstruction is genuinely higher-order; point stars can never witness it.}}
\]

A useful necessary static condition follows. Define

\[
\mathfrak d_q(F)=
\max_U\left\{
\bigl(e_{H_q}(U)-(c_q+1)|U|\bigr)_+,\,
\bigl(e_{H_q}(U)-c_q|U|-\rho_q\bigr)_+
\right\}.
\]

Dynamic feasibility implies

\[
\mathfrak d_q(F)\le T_{q-1}.
\]

Therefore every \(\mathrm{SDH}_A\) solution must satisfy

\[
\boxed{\mathfrak d_1(F)=0,\qquad
\sum_{q\le K_A}\mathfrak d_q(F)=o(W).}
\]

This is necessary but not sufficient: it says nothing about toggle distance.

## 4. The simultaneous owner system is not generically integral

The static formulation chooses one interval composition per owner, subject to target capacities at every depth. For \(K=1\) this is ordinary bipartite matching. For \(K\ge2\), it is an intersection of at least three partition systems.

Already at \(K=2\), the genuine configuration matrix can contain a determinant-\(2\) minor. Let \(|R|=m-3\) and take distinct \(a,b,c,d\), with owners

\[
X=R\cup\{a,b,c\},\quad(a_1,a_2,a_3)=(a,b,c),
\]

\[
Y=R\cup\{d,b,c\},\quad(a_1,a_2,a_3)=(d,b,c).
\]

They share canonical targets

\[
A=R\cup\{b,c\},\qquad C=R\cup\{c\}.
\]

Using configurations \(X:(0,1)\), \(X:(1,0)\), and \(Y:(0,0)\), and rows “owner \(X\), target \(A\), target \(C\),” gives

\[
\begin{pmatrix}
1&1&0\\
1&0&1\\
0&1&1
\end{pmatrix},
\qquad \det=-2.
\]

The direct time-expanded owner-flow matrix also contains an independently audited determinant-\(2\) minor. Hence ordinary total unimodularity, single-commodity flow, or two-matroid intersection cannot prove simultaneous feasibility.

These local words are individually wreath-realizable, but their co-occurrence inside one exact factor is not proved. This is an integrality obstruction to the generic architecture, not an exact-factor counterexample.

## 5. A point-balanced Johnson obstruction with exponential transport

For every \(d=2\) or \(d\ge4\), there is a Hamilton cycle of \(Q_d\), of length \(M=2^d\), with quarter vertices \(A,B,C,D\) satisfying

\[
\mathbf1_A+\mathbf1_C=\mathbf1_B+\mathbf1_D.
\]

For \(d\ge4\), construct it in \(Q_2\times Q_{d-2}\) by traversing four Hamilton paths between the checkpoints

\[
0,\ e_1,\ e_1+e_2,\ e_2.
\]

Reverse two opposite quarter-arcs. The resulting endpoint loads are

\[
2\text{ at }A,C,\qquad
0\text{ at }B,D,\qquad
1\text{ elsewhere}.
\]

The only all-one endpoint orientations of a cycle are its two directed cyclic orientations, and either requires exactly

\[
\boxed{M/2=2^{d-1}}
\]

toggles. Yet the signed point defect is exactly zero.

Embed \(Q_d\) into \(J(n,r)\) by choosing disjoint coordinate pairs and setting

\[
\phi(x)=C_0\cup\{u_i^{x_i}:1\le i\le d\}.
\]

Every cube edge has a distinct union and distinct intersection: the flipped pair is uniquely the pair occurring twice in the union and zero times in the intersection.

At \(q=1\), these unions are distinct middle owners and the intersections are distinct canonical depth-two targets. Moreover, the cube can be isolated in the bare one-edge-per-middle-owner selector: an \(m\)-set has at most two cube facets, since the induced cube is triangle-free, so every noncycle owner can choose two facets outside the cube.

If such a block were an isolated component of an actual \(G_1\), then \(c_1=1\), its overload would be only \(2\), but its minimum toggle repair would be \(2^{d-1}\). The block also has equal adjacent deletion-position marginals and satisfies the exact canonical resource inequality

\[
(q+1)\mu_q(S)+q\nu_q^{\rm can}(S)
\le\binom{m+q+1}{q}.
\]

Thus it survives Johnson locality, unique tops and cores, point homomesy, adjacent deletion-label homomesy, and the known row-resource cap.

This decisively refutes any black-box implication

\[
\text{Hall feasibility + Johnson geometry + point balance}
\Longrightarrow
\text{short supported transport}.
\]

## 6. One allowed sibling rewire can amplify cost from \(1\) to \(2^d\)

There is also a genuinely adaptive local trap. Let

\[
s=C+x,\qquad h=C+y,\qquad k=C+z.
\]

Embed a \(Q_d\) containing adjacent \(h,k\) but excluding \(s\). Delete \(hk\) from a Hamilton cycle, obtaining a Hamilton path from \(k\) to \(h\), and add edges \(sk\) and the special edge \(sh\).

Choose baseline endpoints along the path from \(s\) toward \(h\), and choose \(s\) on \(sh\). The loads are \(2\) at \(s\), \(0\) at \(h\), and \(1\) elsewhere. In the canonical graph, toggling \(sh\) to \(h\) repairs the component in one move.

If a previous owner toggle carries \(z\), the special edge is rewired from \(sh\) to \(sk\), exactly the allowed same-core adjacent-deletion change. There are then two parallel \(sk\) edges. Leaf-forcing along the remaining path shows that every balanced orientation must reverse all \(2^d-1\) cube-path edges and one \(sk\) edge:

\[
\boxed{\tau_{\rm canonical}=1,\qquad
\tau_{\rm rewired}=2^d.}
\]

This is an abstract Johnson-supported residual component. External exact-factor edges could provide shortcuts, so it is not an exact-wreath counterexample. It proves, however, that the exact allowed rewiring has no generic Lipschitz recourse bound.

## 7. Why this still does not refute \(\mathrm{SDH}_A\)

An actual wreath factor imposes further packet constraints:

- Each wreath contributes \(n\) sibling edges forming a matching.
- Their ordered difference labels form one directed Hamilton cycle on coordinates.
- The ordered-pair multiset is identical at every adjacent deletion position.
- Edge unions and intersections are the cyclic \((r+1)\)- and \((r-1)\)-windows of the same row.
- The \(B=W/n\) packets’ middle windows partition all \(W\) owners.

There is also the exact pair-distance ledger. For every coordinate pair \(\{x,y\}\),

\[
\sum_{\pi\in\mathcal F}d_\pi(x,y)=\frac{B(m+1)}2,
\]

so at most \(B/2\) packet cycles can make \(\{x,y\}\) adjacent.

The cube passes every known local constraint, and each decorated edge is individually extendible to a wreath and hence to some conjugate exact factor. What is not proved is simultaneous packetization of linearly many such edges, isolation of the resulting components, and exact completion of the remaining owners.

A single largest cube has at most \(2^{m-1}=o(B)\) edges, hence is asymptotically negligible. Linear toggle cost would require \(\Omega(W/2^d)\) protected copies and roughly \(\Theta(n)\) compatible prescribed edges in typical wreath packets.

Cardinality alone cannot guarantee completion: a sparse partial packing may consume all \(m+1\) odd-graph neighbors of an uncovered middle set, leaving no wreath through it.

## Final lane status

The following remain unproved:

1. **Packetized higher-order Hall expansion:** choose one exact factor for which all reachable \(G_q\) satisfy every non-coordinate Hall cut.

2. **Packetized short transport:** exclude point-balanced long cycles and same-core recourse cascades at positive density, or prove a global amortized correction theorem.

3. **Exact simultaneous owner integrality:** exploit special packet structure to overcome the determinant-\(2\) local automaton obstruction.

4. **Counterexample packetization:** replicate the cube/trap blocks at linear scale inside one exact factor with a Hall-feasible complement.

Even proving item 4 would only produce a bad exact factor; because \(\mathrm{SDH}_A\) is existential, it would not refute the lemma unless every possible jointly chosen factor were obstructed.

So the honest conclusion is:

\[
\boxed{\mathrm{SDH}_A/\mathrm{AO}_A\text{ is not proved and not disproved.}}
\]

The route is genuinely exhausted at exact cyclic packetization plus higher-order Hall/short-transport control. All decisive local calculations above were independently rederived and audited.
