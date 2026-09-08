The mesoscopic lane closes with a rigorous capacity ceiling, not a cover-down theorem. The decisive result is that any packet capable of repairing arbitrary linear first-shadow defects must touch a positive density of all owners and must rewire \(\Theta(m)\) productive undirected wreath edges per \(O(1)\)-wreath packet. Bundling or globally reoptimizing the common nested Hall flow cannot evade this bound.

## 1. Universal exact-packet locality theorem

Let \(F_0,F_1\) be exact wreath factors agreeing outside the same middle support \(U\), with \(L=|U|\). Orient their affected wreaths compatibly with their pointed cyclic orders and write their successor permutations as \(\sigma_0,\sigma_1\). Define

\[
t_{\rm und}=|E(F_0[U])\setminus E(F_1[U])|,
\]

and

\[
t_{\rm dir}
=
\bigl|
\{(X,\sigma_0X):X\in U\}
\setminus
\{(X,\sigma_1X):X\in U\}
\bigr|.
\]

For \(X=I_\pi(s,m)\), choose the odd-cycle orientation satisfying

\[
\sigma I_\pi(s,m)=I_\pi(s+m,m).
\]

Since \(2m\equiv-1\pmod{2m+1}\),

\[
\boxed{
L_q^F(X)=\bigcap_{j=0}^{q}\sigma_F^{2j}(X).
}
\tag{1}
\]

Thus the pointed depth-\(q\) flag depends on one directed \(2q\)-edge history.

Define

\[
D_q^{\rm hist}
=\frac12\|\mu_q(F_1)-\mu_q(F_0)\|_1
\]

and

\[
D_q^{\rm point}
=
|\{X\in U:L_q^{F_0}(X)\ne L_q^{F_1}(X)\}|.
\]

Then, for every \(1\le q\le m-1\),

\[
\boxed{
D_q^{\rm hist}\le \min(L,2qt_{\rm und}),
\qquad
D_q^{\rm point}\le \min(L,2qt_{\rm dir}).
}
\tag{2}
\]

At \(q=0,m\), both distances vanish.

For the histogram statement, use the centered, orientation-independent colour

\[
C_q^F(X)
=
\bigcap_{j=0}^{q}\sigma_F^{-q+2j}(X).
\]

Its multiset is exactly the depth-\(q\) cyclic-interval histogram. A centered colour is unchanged whenever its radius-\(q\) path contains no old-only undirected edge. Each such edge lies in exactly \(2q\) radius paths. The directed proof follows identically from (1).

More sharply, if deleting the old-only edges leaves maximal common paths of vertex-orders \(\ell_i\), then

\[
D_q^{\rm hist}
\le
\sum_i\min(\ell_i,2q).
\tag{3}
\]

This is a coupling/removal-mass bound, not necessarily the actual half-\(\ell_1\) distance after cancellations. For profile-3 \(C_8\) trades, \(\ell_i=3,n-3,3,n-3\), recovering exactly the audited potential masses

\[
r_1=8,\qquad r_q=4q+6\quad(2\le q\le m-1).
\]

## 2. Overload and common-Hall objectives are Lipschitz

Balanced quota vectors have the same total mass as \(\mu_q\), so

\[
O_q(F)
=
\min_{b\ {\rm balanced}}
\frac12\|\mu_q(F)-b\|_1.
\]

Hence

\[
\boxed{
|O_q(F_1)-O_q(F_0)|\le D_q^{\rm hist}.
}
\tag{4}
\]

Let \(\mathscr R\) be the factor-independent finite family of all integral balanced nested resolutions and put

\[
\mathcal J_A(F)
=
\min_{P\in\mathscr R}
\sum_{q\le K_A}\frac{e_q(F,P)}{c_q}.
\]

For every fixed \(P\), the two mismatch indicators differ only on owners counted by \(D_q^{\rm point}\). Applying this first to a minimizer for \(F_0\), then symmetrically to one for \(F_1\), gives

\[
\boxed{
|\mathcal J_A(F_1)-\mathcal J_A(F_0)|
\le
\sum_{q\le K_A}\frac{D_q^{\rm point}}{c_q}.
}
\tag{5}
\]

Thus even wholesale reoptimization of one integral common nested Hall flow cannot amplify a packet beyond its pointed-slot support.

## 3. Sharp fixed-window capacity curve

For fixed \(A>0\), define

\[
d(x)=\lfloor e^{x^2}\rfloor,
\quad
\kappa_A=\int_0^A\frac{dx}{d(x)},
\quad
J_A=\int_0^A\frac{x\,dx}{d(x)},
\]

and

\[
F_A(\lambda)=\int_0^A\frac{\min(\lambda,x)}{d(x)}\,dx.
\]

For a packet of owner-volume \(L\) and seam count \(t>0\), put

\[
C_A(L,t)
=
\sum_{q\le K_A}\frac{\min(L,2qt)}{c_q},
\qquad
\lambda=\frac{L}{2t\sqrt m}.
\]

Uniformly for fixed \(A\),

\[
\boxed{
C_A(L,t)
=
2tmF_A(\lambda)
+
O_A\!\bigl(\min\{L,t\sqrt m\}\bigr).
}
\tag{6}
\]

Indeed,

\[
\log\frac W{N_q}
=
\frac{q(q+1)}m+O_A(m^{-1})
=
\frac{q^2}{m}+O_A(m^{-1/2}),
\]

so \(c_q\) differs from \(d(q/\sqrt m)\) at only \(O_A(1)\) indices. A bounded-variation Riemann sum proves (6). In particular,

\[
\sum_{q\le K_A}\frac1{c_q}
=
\kappa_A\sqrt m+O_A(1),
\qquad
\sum_{q\le K_A}\frac q{c_q}
=
J_A m+O_A(\sqrt m).
\tag{7}
\]

Consequently,

\[
|\Phi_A(F_1)-\Phi_A(F_0)|
\le C_A(L,t_{\rm und}),
\]

and

\[
|\mathcal J_A(F_1)-\mathcal J_A(F_0)|
\le C_A(L,t_{\rm dir}).
\]

These constants are fixed-window constants only; no uniformity in an unspecified growing \(A(m)\) is asserted.

For owner-disjoint packets \((L_i,t_i)\), let

\[
V=\sum_iL_i,\qquad T=\sum_it_i.
\]

Since

\[
\sum_i\min(L_i,2qt_i)\le\min(V,2qT),
\]

any rank-\(q\) correction of size \(D_q\) must satisfy

\[
\boxed{
V\ge D_q,\qquad T\ge\frac{D_q}{2q}.
}
\tag{8}
\]

This is the clean capacity ceiling.

For packets with \(L=\Theta(m)\) occupying owner density \(\rho=pL/W\):

- Repairing \(D_1\ge\delta W\) requires average
  \[
  t_i\ge\frac{\delta L}{2\rho}=\Theta(m).
  \]
- At \(q\sim x\sqrt m\), it requires average \(t_i=\Omega(\sqrt m)\).
- A \(t=\Theta(\sqrt m)\) packet is therefore Gaussian-dense but cannot repair an arbitrary linear defect at any fixed shallow depth.
- If \(D_q\ge\delta W\) at every \(q\le K_A\), then
  \[
  \frac{T}{B}
  \ge
  \left(\frac{\delta\kappa_A}{J_A}+o(1)\right)\sqrt m,
  \qquad B=\frac Wn.
  \]

For the audited profile-3 \(C_8\),

\[
\sum_{q\le K_A}\frac{r_q}{c_q}
=
4J_A m+O_A(\sqrt m).
\]

Thus \(B\) such switches have \(\Theta(W)\) aggregate weighted capacity, but only \(O(W/\sqrt m)\) capacity at any individual Gaussian rank and \(O(W/m)\) at depth one. A linear depth-one overload needs at least \(\delta W/8\) switch uses; the pointed bound \(9\) gives \(\delta W/9\). Aggregate capacity therefore cannot be promoted to bundled multidepth correction.

## 4. Two-wreath mesoscopic normal form

There is also an architecture-specific ceiling beyond profile-3 counting.

Let \(C,D\) be two middle-disjoint wreath supports, \(m\ge3\).

First, cross odd-graph edges between \(C\) and \(D\) form a matching. If \(X\in C\) had two cross-neighbours \(Y,Z\in D\), then \(Y,Z\subset X^c\), so \(|Y\cap Z|=m-1\). They are adjacent cyclic \(m\)-intervals of \(D\), and

\[
[n]\setminus(Y\cup Z)=X
\]

is another \(D\)-interval, contradicting \(C\cap D=\varnothing\).

Moreover, the cross-incident vertices on either old wreath contain no three consecutive cycle vertices. For adjacent matched vertices of \(D\), their cross preimages in \(C\) intersect in at most one point. Intersection zero would create a forbidden \(4\)-cycle, so their intersection is one, which in a wreath means cycle-distance \(3\). Three consecutive matched \(D\)-vertices would therefore have preimages \(C_{-3},C_0,C_3\). In an omitted-label word \(z\),

\[
C_0^c\cap C_3^c=\{z_0,z_2\},
\qquad
C_0^c\cap C_{-3}^c=\{z_{-3},z_{-1}\}.
\]

The single coordinate omitted by the cross-neighbour of \(C_0\) would have to lie in both disjoint pairs, impossible.

Hence

\[
\boxed{
e_{\rm cross}(C,D)\le\left\lfloor\frac{2n}{3}\right\rfloor.
}
\tag{9}
\]

Now replace the two old cycles by any other 2-factor on \(C\cup D\). Since each wreath is induced and cross edges form a matching, every vertex retains at least one old edge. The removed edges form matchings of equal cardinality \(r\) on \(C\) and \(D\), and the new cross matching has \(2r\) edges. Therefore

\[
r\le\left\lfloor\frac n3\right\rfloor,
\qquad
t_{\rm und}=2r\le2\left\lfloor\frac n3\right\rfloor.
\tag{10}
\]

The common path pieces have at least three vertices each. Consequently the depth-one removal/addition capacity of any two-wreath packet is at most

\[
4\left\lfloor\frac n3\right\rfloor
=
\left(\frac23+o(1)\right)|C\cup D|.
\tag{11}
\]

Thus a two-wreath packet can be genuinely mesoscopic only by installing a linear cross matching. The existing profile-3 \(C_8\) is the \(r=2\) local instance. No all-\(m\) construction of a coordinate-compatible linear cross matching which resews into two exact \(n\)-cycles was proved.

## 5. Dense pointed motion can be pure gauge

Reversing one wreath is a legal one-wreath packet preserving exactly the same middle owners. If

\[
X_j=I_\pi(j,m),
\]

then its two states have

\[
L_q^+(X_j)=I_\pi(j,m-q),
\qquad
L_q^-(X_j)=I_\pi(j+q,m-q).
\]

These are distinct for every \(1\le q\le m-1\), so reversal changes exactly \(n=\Theta(m)\) pointed slots at every shallow depth. Nevertheless,

\[
\{L_q^+(X_j):j\in\mathbb Z_n\}
=
\{L_q^-(X_j):j\in\mathbb Z_n\},
\]

so every histogram and every \(O_q\) is unchanged. Here

\[
t_{\rm und}=0,\qquad t_{\rm dir}=n.
\]

For a fixed balanced nested resolution \(P\), let \(U_C\) be the weighted incidences matching neither orientation, and \(A_C,B_C\) those matching only \(+\) or only \(-\). The exact best bundled orientation cost is

\[
\boxed{
U_C+\min(A_C,B_C).
}
\tag{12}
\]

The same orientation bit controls every owner and every depth. This is a genuine integral, positive-density pointed packet, but it has zero overload capacity and supplies no Hall expansion theorem. It proves that \(\Theta(m)\) pointed changes alone are insufficient; productive undirected transport and correct signs are essential.

## 6. Hall-cut ceiling

Fix stopping depths and a final quota vector \(b\). If two packet states change \(r_q\) frozen depth-\(q\) owner values, then for every target family \(\mathcal A\),

\[
\|g_q'-g_q\|_1\le2r_q,
\qquad
|g_q'(\mathcal A)-g_q(\mathcal A)|\le r_q.
\]

Therefore the adjacent residual clone-Hall slack changes by at most

\[
\boxed{r_{q-1}+r_q.}
\tag{13}
\]

If stopping depths themselves change, every changed frozen-status incidence and release source must also be charged; a bound using only changed labels is then false.

Equations (5) and (13) are ceilings only. They do not provide the needed sign, preserve all tight cuts, or guarantee that one packet state works simultaneously at every depth. A sparse graph edit can still force a linear alternating reroute.

## Exact remaining status

Proved:

- the universal two-resource packet locality theorem;
- the exact fixed-window capacity curve and constants;
- robustness under global reoptimization of one integral common nested resolution;
- positive-density and seam-density lower bounds;
- the two-wreath cross-matching/no-three-consecutive ceiling;
- the dense-reversal gauge obstruction.

Unproved:

1. A positive-density family of legal exact packets with \(\Theta(m)\) **productive undirected** shallow transport per \(O(1)\)-wreath packet.
2. A choice of their bundled states whose effects have the correct signs after histogram cancellations.
3. Survival of every residual Hoffman/Hall cut under the same state vector at every depth.
4. A cover-down theorem producing \(o(W)\) weighted overload, or the stronger labelled \(o(W)\) mismatch.

Accordingly, this lane proves a rigorous capacity ceiling but neither MWB nor labelled synchronization. The conjecture remains open. The decisive \(2q\) locality constants, half-\(\ell_1\) normalization, reversal caveat, fixed-window asymptotics, and minimization over integral common flows were independently audited.
