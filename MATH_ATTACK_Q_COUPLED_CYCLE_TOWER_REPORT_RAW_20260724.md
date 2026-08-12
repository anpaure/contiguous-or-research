The depth-one lane reduces exactly to one colored \(C_{2m+1}\)-factor problem, but the proved two-sided rainbow forest does not supply the required exact factor. The fixed-Gaussian extension is a coupled cycle-tower problem and does not follow from depth one.

## 1. Exact depth-one colored-factor theorem

Let \(F\) be an exact \(C_{2m+1}\)-factor of \(KG(2m+1,m)\). Every component is a wreath. If \(Y_F(X),Z_F(X)\) are the two factor-neighbors of a middle set \(X\), define its angle color

\[
\chi_F(X)=Y_F(X)\cap Z_F(X)\in\binom{[2m+1]}{m-1}.
\]

Reindexing each odd cycle by step two gives its Johnson \(n\)-cycle; the corresponding Johnson edge has

\[
\text{lower color }Y_F(X)\cap Z_F(X)=\chi_F(X),
\]

while

\[
Y_F(X)\cup Z_F(X)=X^c.
\]

Therefore every rank-\((m+1)\) adjacent upper union occurs exactly once in every exact factor. The upper side of the depth-one edge-color problem is automatic.

Let \(\mu_1(S)=|\{X:\chi_F(X)=S\}|\), and let \(M_1\) be the number of missing lower colors. For \(m\ge3\),

\[
c_1=1,\qquad
r_1=W-\binom{2m+1}{m-1}=\frac{2W}{m+2}.
\]

If \(t_1=|\{S:\mu_1(S)\ge2\}|\), the exact overload is

\[
\boxed{O_1=M_1+(r_1-t_1)_+.}
\]

Consequently

\[
M_1\le O_1\le M_1+\frac{2W}{m+2},
\]

and hence

\[
\boxed{O_1=o(W)\iff M_1=o(W).}
\]

Thus lane Q’s depth-one target is precisely:

> Find an exact \(C_{2m+1}\)-factor whose angle colors cover all but \(o(W)\) rank-\((m-1)\) sets.

The symmetric rank-\((m+2)\) triple-union histogram is then automatically its complement. This is unlabelled overload only; it does not yield labelled common-owner synchronization.

## 2. Exact fixed-coordinate normal form

Fix \(z\) and put \(Q=[2m]\),

\[
V=\binom{2m}{m},\qquad B=\frac{V}{m+1}=\operatorname{Cat}_m.
\]

Exact wreath factors are in bijection with \(B\) Johnson paths

\[
X_0,X_1,\ldots ,X_m\subseteq Q
\]

such that:

1. all \(X_i\) partition \(\binom Qm\);
2. \(X_m=Q\setminus X_0\);
3. the edge unions \(U_i=X_i\cup X_{i+1}\) partition \(\binom Q{m+1}\).

The corresponding odd cycle is

\[
X_0,A_0,X_1,A_1,\ldots ,A_{m-1},X_m,X_0,
\qquad
A_i=\{z\}\cup(Q\setminus U_i).
\]

Its depth-one lower colors split exactly into

\[
X_i\cap X_{i+1}\quad(0\le i<m),
\]

the two caps

\[
Q\setminus U_0,\qquad Q\setminus U_{m-1},
\]

and the turn colors

\[
\{z\}\cup\bigl(Q\setminus(U_{i-1}\cup U_i)\bigr),
\qquad 1\le i<m.
\]

The sector counts are exact:

\[
\begin{array}{c|c|c}
\text{sector}&\text{slots}&\text{targets}\\ \hline
z\text{-free}&(m+2)B&mB\\
z\text{-containing}&(m-1)B&
\frac{m(m-1)}{m+2}B .
\end{array}
\]

Both sectors have mean load \((m+2)/m\).

The proved two-sided rainbow forest controls the internal intersections and makes the \(U_i\) distinct. It does not control the turn statistic

\[
\kappa_X=U_e\cup U_f
\]

at a degree-two pivot \(X\). These \(\kappa_X\) are exactly the complements of the \(z\)-containing lower colors.

A sharp sufficient lemma is therefore:

> **Colored complementary-completion lemma — unproved.**  
> There exists an exact complementary \(m\)-path factor whose edge unions partition \(\binom Q{m+1}\), with all but \(o(V)\) internal intersections and all but \(o(V)\) turn colors distinct.

Equivalently, in the inclusion graph between ranks \(m-1\) and \(m+1\), one needs a perfect matching whose induced Johnson graph consists of complement-ended paths and whose consecutive upper-color unions are near-surjective. This would prove \(O_1=o(W)\).

## 3. Why the rainbow forest cannot be completed as a black box

There are two independent missing properties: turn-color control and wreath-compatible geometry.

For a positive-density geometric obstruction, fix five coordinates \(a,b,c,d,e\). For every \(R\in\binom{[2m]\setminus\{a,b,c,d,e\}}{m-2}\), take

\[
Rac,\ Rbc,\ Rbd,\ Rde.
\]

Across all \(R\), the vertices, lower edge colors, upper edge colors, and both turn colors are injective. Nevertheless \(b\) is inserted and later removed, so no complementary geodesic path can contain all three edges. Any wreath-compatible completion must delete at least one edge per gadget:

\[
\binom{2m-5}{m-2}
=\left(\frac1{32}+o(1)\right)V.
\]

This is a positive-density partial obstruction, not a near-spanning counterexample. It proves that local two-sided rainbowness—even with turn rainbowness—does not imply \(o(V)\)-edit wreath completion. A theorem specialized to the particular near-spanning forest remains logically possible but unproved.

Likewise, a separate positive-density path family can have all adjacent lower and upper colors distinct while two consecutive triple intersections coincide. Thus generic depth-one rainbowness does not control depth two. The audited \(m=4\) exact-factor certificate also shows that one perfect depth-one coordinate cut can miss depth-two colors globally; this refutes one-cut propagation, not the stronger global implication \(O_1=o(W)\Rightarrow O_2=o(W)\), which remains open.

## 4. The exact Gaussian-depth cycle tower

For one exact factor define

\[
V^q_{\pi,j}=I_\pi(j,m-q),\qquad
\mu_q(S)=|\{(\pi,j):V^q_{\pi,j}=S\}|.
\]

The \(B\) cyclic rows \(V^q_{\pi,0},\ldots,V^q_{\pi,n-1}\) form an exact occurrence-level cycle tower satisfying

\[
V^q_{\pi,j}\cap V^q_{\pi,j+1}
   =V^{q+1}_{\pi,j+1},
\qquad
V^q_{\pi,j}\cup V^q_{\pi,j+1}
   =V^{q-1}_{\pi,j}.
\]

Hence

\[
\boxed{
\begin{aligned}
\text{vertex loads at level }q&=\mu_q,\\
\text{lower edge-color loads}&=\mu_{q+1},\\
\text{upper edge-color loads}&=\mu_{q-1}.
\end{aligned}}
\]

Depth-one balancing therefore merely balances the vertices of the next colored-cycle problem. It supplies no bound on its lower edge colors.

For general \(q\), writing \(W=c_qN_q+r_q\),

\[
D_q=\sum_S(c_q-\mu_q(S))_+,\qquad
t_q=|\{S:\mu_q(S)\ge c_q+1\}|,
\]

gives the exact formula

\[
\boxed{O_q=D_q+(r_q-t_q)_+.}
\]

Uniformly for \(q\le A\sqrt m\),

\[
\log\frac{W}{N_q}
=\frac{q(q+1)}m+O_A(m^{-1/2}),
\]

so \(c_q\le C_A\). Thus fixed-window MWB requires one exact factor with

\[
\sum_{q\le A\sqrt m}\frac{O_q}{c_q}=o(W).
\]

Independent cycle factors or forests at successive levels do not establish this.

There is also a sharp seam barrier. Cutting all wreaths at \(z\) and simply discarding the \(2q\) fringe windows at depth \(q\) costs

\[
2B\sum_{q=1}^{K_A}q
=B K_A(K_A+1),
\]

and therefore

\[
\frac{B K_A(K_A+1)}W\longrightarrow\frac{A^2}{2}.
\]

Since \(c_q\) is bounded, this remains \(\Theta_A(W)\) after weighting. Cross-seam synchronization is indispensable at Gaussian depth.

Finally, the audited profile-3 \(C_8\) switches cost \(O_A(m)\) per switch. Any \(o(B)\) sparse absorber changes the fixed-window objective by only \(o(W)\), so it cannot repair a linear initial defect.

## Verdict

- The depth-one upper edge colors are automatically perfect.
- Depth-one overload is asymptotically equivalent to lower-color near-surjectivity.
- The proved two-sided rainbow forest supplies the correct positive-density skeleton but lacks turn colors, complementary geodesic completion, and exact factor extendibility.
- No valid depth-one-to-Gaussian bootstrap exists.
- The fixed-Gaussian problem is exactly a coupled, integral colored-cycle tower inside one wreath factor.

The smallest new theorem for this lane is the colored complementary-completion lemma above. Its Gaussian analogue must control every level of the cycle tower jointly; that is essentially the remaining unlabelled MWB theorem, not a consequence of the depth-one forest.
