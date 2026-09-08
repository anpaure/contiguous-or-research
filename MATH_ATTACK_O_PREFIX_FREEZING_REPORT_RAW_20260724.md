Lane O has an exact negative resolution at the Boolean-flow level: all residual Hoffman cuts can be satisfied while permanent prefix freezing still costs \(\Theta(W)\). The obstruction is irreversible release, not flow infeasibility.

## 1. Exact residual Hoffman theorem

Let \(V_q=\binom{[n]}{m-q}\), \(0\le q\le K\), and choose stopping depths \(a(X)\in\{0,\ldots,K\}\). Define

\[
g_q(S)=\#\{X:a(X)\ge q,\ L_q(X)=S\},
\]

and, for \(q<K\),

\[
\sigma_q(S)=\#\{X:a(X)=q,\ L_q(X)=S\}.
\]

Thus \(\sigma_q\) is the supply released immediately after layer \(q\). Put

\[
R_K=\sum_{q<K}\sigma_q(V_q),
\qquad
\ell_q(S)=(c_q-g_q(S))_+,
\qquad
u_q(S)=c_q+1-g_q(S),
\]

assuming \(g_q(S)\le c_q+1\).

For \(B_q\subseteq V_q\), let \(C_q=\partial B_{q-1}\subseteq V_q\) be its immediate lower Boolean shadow. Extend \(\ell_q,u_q\) additively to families.

**Theorem.** An integral residual suffix flow exists if and only if, for every sequence \(B_0,\ldots,B_{K-1}\), both

\[
\begin{aligned}
\sum_{q<K}\sigma_q(B_q)
+\sum_{q=1}^{K-1}\ell_q(B_q\setminus C_q)
\le{}&
\sum_{q=1}^{K-1}u_q(C_q\setminus B_q)
+u_K(C_K),
\tag{U}
\end{aligned}
\]

and

\[
\begin{aligned}
\sum_{q<K}\sigma_q(B_q)
+\sum_{q=1}^{K-1}\ell_q(B_q\setminus C_q)
+\ell_K(V_K\setminus C_K)
\le{}&
R_K+\sum_{q=1}^{K-1}u_q(C_q\setminus B_q).
\tag{L}
\end{aligned}
\]

Proof: split every residual node into a pre-node and post-node joined by an arc with bounds \([\ell_q,u_q]\); use unbounded Boolean-inclusion arcs between layers, inject \(\sigma_q\) at post-nodes, and drain layer \(K\) to one sink. Hoffman’s circulation theorem gives the cuts. Finite cuts must be closed under Boolean transition arcs; minimizing over pre-node membership yields exactly (U) and (L). Integer capacities and total unimodularity give an integral flow.

For \(K=1\), these reduce to the ordinary two-sided Hall conditions

\[
\sigma_0(B)\le u_1(\partial B),
\qquad
\ell_1(V_1\setminus\partial B)
\le \sigma_0(V_0\setminus B),
\]

which independently checks the signs.

In particular, adjacent-layer support cuts such as

\[
\ell_{q+1}(\mathcal B)
\le u_q(N(\mathcal B))+\sigma_q(N(\mathcal B))
\]

are necessary, but independently feasible adjacent pairs do not replace the multilevel staircase cuts.

## 2. Permanent-release lower bound

Let

\[
R_q=\#\{X:a(X)<q\}.
\]

Then \(R_q\) is nondecreasing and

\[
\sum_X\Psi_{m,K}(a(X))
=\sum_{q=1}^K\frac{R_q}{c_q}.
\]

For every balanced completion \(Q\),

\[
O_q(L)\le e_q(L,Q)\le R_q.
\]

Hence, writing \(M_q=\max_{s\le q}O_s(L)\),

\[
\boxed{
\sum_X\Psi_{m,K}(a(X))
\ge
\sum_{q=1}^K\frac{M_q}{c_q}.
}
\tag{RM}
\]

Equivalently,

\[
\sum_{q=1}^K\frac{M_q}{c_q}
=
\sum_{s=1}^K(M_s-M_{s-1})
\sum_{q=s}^K\frac1{c_q}.
\]

Every new overload record is therefore charged through the entire remaining window. In particular, for \(q\le K/2\),

\[
O_q(L)=o(W/\sqrt m)
\]

is necessary for \(o(W)\) prefix cost. Fixed-window MWB only requires \(O_q=o(W)\), so it does not supply this rate.

## 3. Exact Boolean obstruction

Fix \(A>0\) and \(K=\lceil A\sqrt m\rceil\). For all sufficiently large \(m\), there exist integral nested owner paths \(L\) and a balanced nested resolution \(P\) such that

\[
O_1(L)=R:=\left\lfloor\frac{N_1}{\sqrt m}\right\rfloor,
\qquad
O_q(L)=0\quad(2\le q\le K),
\]

and

\[
e_1(L,P)=R,\qquad e_q(L,P)=0\quad(q\ge2).
\]

Thus both the overload and labelled objectives equal \(R=o(W)\), but the minimum prefix-release cost is

\[
\boxed{
R\sum_{q=1}^K\frac1{c_q}=\Theta_A(W).
}
\]

Construction: take any balanced nested resolution \(P\). At rank one,

\[
c_1=1,\qquad \frac{W}{N_1}=\frac{m+2}{m},
\]

so every target has \(P\)-load \(1\) or \(2\). The number of low targets is

\[
|\mathcal L|
=N_1\left(1-\frac2m\right).
\]

For each low target \(S\), let \(X_S\) be its unique owner. Swapping the first two deletion letters of \(X_S\) gives another intermediate target \(A_S\).

Make a simple graph on \(\mathcal L\), joining \(S\) to \(A_S\) whenever \(A_S\) is also low. It has at most \(|\mathcal L|\) edges, so Caro–Wei gives an independent set of size at least \(|\mathcal L|/3\). Choose \(I\) of size \(R\) inside it and swap the first two deletion letters for the owners \(X_S\), \(S\in I\).

The paths rejoin at depth two, so \(L_q=P_q\) for every \(q\ge2\). At depth one every selected \(S\) loses its unique owner and, by independence, receives none. Hence

\[
D_1^-=R.
\]

All unselected targets only gain load, with total gain \(R\), so \(D_1^+\le R\). Therefore the exact overload identity gives \(O_1=R\).

For the constant, uniformly for \(q\le K\),

\[
\log\frac{W}{N_q}
\le\frac{q(q+1)}{m-q+1}
\le2(A+1)(A+2)
\]

for large \(m\). Thus, with

\[
C_A=\exp(2(A+1)(A+2)),
\]

we have \(c_q\le C_A\). Also \(R\ge W/(2\sqrt m)\), so every prefix completion costs at least

\[
R\frac{K}{C_A}
\ge\frac{A}{2C_A}W.
\]

Conversely, stop exactly the selected owners at depth \(0\), freeze all others through \(K\), and let the released owners follow their \(P\)-paths. This is an explicit integral residual flow satisfying every Hoffman cut and attaining exactly

\[
R\sum_{q\le K}\frac1{c_q}.
\]

Thus the obstruction persists even when the residual network is completely feasible.

## Exact scope

The constructed \(L\) is an integral nested Boolean owner system, but it is not proved to come from one exact wreath factor: independent ownerwise swaps generally destroy cyclic bundling. Therefore this is not an exact-factor counterexample to SYNC or MWB.

It does prove:

- No theorem using only Boolean inclusion, bounded quotas, small overload, and Hoffman integrality can establish \(o(W)\) permanent-prefix cost.
- Prefix freezing is strictly stronger than labelled synchronization because it cannot charge rank-isolated repairs only once.
- Any positive exact-wreath version must prove the genuinely wreath-specific necessary condition

\[
\sum_{q\le K}
\frac{\max_{s\le q}O_s(F)}{c_q}=o(W),
\]

and then select stops satisfying all staircase cuts. Both statements remain unproved.
- Realizing the obstruction inside one exact wreath factor also remains unproved.

The decisive Hoffman signs, independent-set construction, overload calculation, constants, and exact residual-flow witness were independently rederived. No finite search or nonintegral factor argument was used.
