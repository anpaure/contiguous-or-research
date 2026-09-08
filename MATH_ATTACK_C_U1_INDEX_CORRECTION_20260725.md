# The Johnson \(U_1\) mode is absent from exact wreath-component noise

Date: 2026-07-25

## Verdict

Use the standard Johnson indexing

\[
\mathbb R^{\binom{[n]}r}
=U_0^{(r)}\oplus U_1^{(r)}\oplus\cdots\oplus U_r^{(r)},
\qquad U_j^{(r)}\cong S^{(n-j,j)}.
\]

For every ownership component in the overlay of two exact wreath factors,
its rank-\(r\) histogram innovation has both its \(U_0\) and \(U_1\)
projections equal to zero. Thus there is no \(U_1\) component-noise
baseline to isolate. The first possible and unique slow module is \(U_2\).

For a uniformly random coordinate transposition, the exact slow rate in the
normalization \(\frac14\mathbb E\|g-\tau g\|_2^2\) is

\[
\kappa_2=\frac2n.
\]

Equivalently, after summing over all unordered coordinate transpositions,
the sharp ambient coefficient is \(4(n-1)\). The coefficient \(2n\) is the
\(U_1\) coefficient and is inapplicable. If one reindexes the quotient by
the forced point-margin constraints and calls its first module
\(\widetilde U_1\), then \(\widetilde U_1=U_2\); its eigenvalue and all
floor terms must still be those of \(U_2\).

This closes the proposed **\(U_1\)-baseline harmonic lane**. It does not
disprove a heat-gap theorem using physical ownership components. The exact
remaining one-step statement is the \(U_2\)-relative inequality (8.2)
below.

## 1. Component point margins

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad
t=\frac Wn=\operatorname{Cat}_m.
\]

At depth \(q\), write \(r=m-q\). For a collection \(\mathcal A\) of
wreath rows, let \(\mu_q(\mathcal A)\) be the histogram of all cyclic
\(r\)-intervals in its rows.

Overlay any two exact middle wreath factors \(F,G\). The ownership graph is
an \(n\)-regular bipartite multigraph: its row vertices are the wreaths of
\(F\) and \(G\), and its edges are the middle sets. Let \(K\) be a connected
component, with row sides \(L_K,R_K\), and define

\[
\Delta_{K,q}=\mu_q(L_K)-\mu_q(R_K).
\tag{1.1}
\]

### Theorem 1.1

For every \(K,q\),

\[
\boxed{
\operatorname{proj}_{U_0^{(r)}}\Delta_{K,q}
=\operatorname{proj}_{U_1^{(r)}}\Delta_{K,q}=0.}
\tag{1.2}
\]

#### Proof

Since the ownership component is \(n\)-regular on both sides,

\[
n|L_K|=|E(K)|=n|R_K|,
\]

so \(s_K:=|L_K|=|R_K|\). One wreath has exactly \(n\) cyclic
\(r\)-intervals, and every coordinate lies in exactly \(r\) of them.
Consequently both side histograms have total mass \(ns_K\), and, for every
coordinate \(x\), both have point margin \(rs_K\). Hence

\[
\sum_S\Delta_{K,q}(S)=0,
\qquad
\sum_{S\ni x}\Delta_{K,q}(S)=0\quad(x\in[n]).
\tag{1.3}
\]

The span of the constant function and the coordinate-incidence functions
\(S\mapsto\mathbf1_{\{x\in S\}}\) is exactly
\(U_0^{(r)}\oplus U_1^{(r)}\). Equations (1.3) say that
\(\Delta_{K,q}\) is orthogonal to that span. \(\square\)

The theorem applies to every overlay, not only to coordinate-transposition
overlays. When \(r=1\), \(U_0^{(1)}\oplus U_1^{(1)}\) is the whole slice,
so every component innovation is identically zero.

## 2. Extra symmetry for a transposition overlay

Let \(G=\tau F\), where \(\tau=(ab)\) is a coordinate transposition.

### Lemma 2.1

For each ownership component,

\[
R_K=\tau L_K,
\qquad
\tau\Delta_{K,q}=-\Delta_{K,q}.
\tag{2.1}
\]

#### Proof

In one wreath, the total number of incidences of \(a,b\) among the \(n\)
middle intervals is \(2m=n-1\). If every middle interval contained exactly
one of \(a,b\), that total would be \(n\). Therefore every wreath owns a
middle set containing both of \(a,b\), or neither; that set is fixed by
\(\tau\). Its ownership edge joins a left row \(C\) to the right row
\(\tau C\). Thus a component contains \(C\) on the left if and only if it
contains \(\tau C\) on the right, proving \(R_K=\tau L_K\). Applying
\(\tau\) to (1.1) reverses its two terms. \(\square\)

Let \(\Delta_{K,q,j}\) denote the \(U_j^{(r)}\) projection, and define

\[
A_{\tau,q,j}
=\left\|\sum_K\Delta_{K,q,j}\right\|_2^2,
\qquad
V_{\tau,q,j}=\sum_K\|\Delta_{K,q,j}\|_2^2.
\tag{2.2}
\]

Orthogonality and Theorem 1.1 give

\[
A_{\tau,q}=\sum_{j\ge2}A_{\tau,q,j},
\qquad
V_{\tau,q}=\sum_{j\ge2}V_{\tau,q,j}.
\tag{2.3}
\]

For a depth window, use the floor-compatible weights

\[
A_{\tau,H}=\sum_{q\le H}\frac{A_{\tau,q}}{c_q},
\qquad
V_{\tau,H}=\sum_{q\le H}\frac{V_{\tau,q}}{c_q}.
\tag{2.4}
\]

In particular,
\(A_{\tau,q,1}=V_{\tau,q,1}=0\) component by component, not merely on
average.

## 3. The sharp slow mode

On \(U_j^{(r)}\), the Johnson Laplacian has eigenvalue \(j(n-j+1)\).
Therefore, for a uniform unordered coordinate transposition,

\[
\frac14\mathbb E_\tau\|g-\tau g\|_2^2
=\kappa_j\|g\|_2^2,
\qquad
\kappa_j=\frac{j(n-j+1)}{n(n-1)}.
\tag{3.1}
\]

For \(2\le j\le r\le m\), \(j(n-j+1)\) is strictly increasing in \(j\).
Hence

\[
\kappa_2=\frac2n,
\qquad
\kappa_j-\kappa_2
=\frac{(j-2)(n-j-1)}{n(n-1)}\ge0.
\tag{3.2}
\]

Equivalently,

\[
\sum_{\tau}\|g-\tau g\|_2^2
\ge4(n-1)\|g\|_2^2
\tag{3.3}
\]

whenever \(g\perp U_0\oplus U_1\). Equality holds throughout the ambient
\(U_2\) module.

This sharpness cannot be improved using only integrality, zero total, zero
point margins, and transposition anti-invariance. For four distinct
coordinates \(a,b,c,d\), set

\[
v(S)=
(\mathbf1_{\{a\in S\}}-\mathbf1_{\{b\in S\}})
(\mathbf1_{\{c\in S\}}-\mathbf1_{\{d\in S\}}),
\tag{3.4}
\]

where the two parenthesized factors are multiplied. It is integral and
nonzero for \(2\le r\le n-2\). It has degree at most two in the slice
coordinates. Direct cancellation among the four choices of one point from
each pair shows that its total and every point margin are zero. Thus it lies
in \(U_2^{(r)}\). For \(\tau=(ab)\), it is \(\tau\)-anti-invariant.

Even nonnegativity of the two abstract side histograms adds nothing: with
\(b(S)\equiv n\), the vectors \(u=b+v\) and \(w=b-v=\tau u\) are
nonnegative integral, each has total \(nN_q\), each point margin is
\(rN_q\), and their difference is \(2v\). Thus they even have the exact
row-count/point-margin ratio for \(N_q\) abstract rows. This is not an
assertion that \(u,w\) are realizable by actual wreath rows. It proves the
exact marginal-only no-go: the physical ownership structure is
indispensable for any improvement over (3.3).

## 4. Integer floor and its mesoscopic size

For the full factor histogram, put

\[
N_q=\binom n{m-q},\qquad
\lambda_q=\frac W{N_q}=c_q+\theta_q,\qquad
\beta_q=N_q\theta_q(1-\theta_q).
\tag{4.1}
\]

Let

\[
f_q=\mu_q-\lambda_q\mathbf1,
\qquad
Q_q=\sum_S(\mu_q(S)-c_q)(\mu_q(S)-c_q-1).
\]

Expansion gives the exact floor identity

\[
\boxed{Q_q=\|f_q\|_2^2-\beta_q\ge0.}
\tag{4.2}
\]

In the pair-collision convention
\(\Phi_q=\sum_S\binom{\mu_q(S)}2-\min\sum_S\binom{\mu_q(S)}2\),
one has \(Q_q=2\Phi_q\), and the balanced overload obeys
\(2O_q\le Q_q\).

Every full exact-factor histogram has zero centered point margins, so
\(f_q\in\bigoplus_{j\ge2}U_j^{(r)}\).

For \(H=\lceil L\sqrt m\rceil\), define

\[
\mathcal Q_H=\sum_{q\le H}\frac{Q_q}{c_q},
\qquad
B_H=\sum_{q\le H}\frac{\beta_q}{c_q}.
\tag{4.3}
\]

The exact load ratio is

\[
\lambda_q=\prod_{i=0}^{q-1}\frac{m+2+i}{m-i},
\]

and uniformly for \(q\le L\sqrt m\),

\[
\log\lambda_q=\frac{q(q+1)}m+O_L(m^{-1/2}),
\qquad
\lambda_q=e^{(q/\sqrt m)^2}+o_L(1).
\tag{4.4}
\]

Since

\[
\frac{\beta_q}{c_qW}
=\frac{\{\lambda_q\}(1-\{\lambda_q\})}
{\lambda_q\lfloor\lambda_q\rfloor},
\]

a Riemann sum yields

\[
\boxed{
\frac{B_H}{W\sqrt m}\longrightarrow
\kappa_L:=
\int_0^L
\frac{\{e^{x^2}\}(1-\{e^{x^2}\})}
{e^{x^2}\lfloor e^{x^2}\rfloor}\,dx>0.}
\tag{4.5}
\]

Indeed, the integrand, defined as zero when \(e^{x^2}\) is an integer, is
continuous on every compact interval; the apparent jumps of the floor are
killed by the numerator. It is positive away from finitely many points.

The forced transposition-scale floor is therefore

\[
\boxed{
\frac2nB_H
=\left(\frac{2\kappa_L}{L}+o(1)\right)H\,t.}
\tag{4.6}
\]

It is exactly on the allowed \(H\operatorname{Cat}_m\) scale.

## 5. At floor balance, the baseline is exactly the pair-parity floor

Suppose \(Q_q(F)=0\). Then

\[
\mu_q=c_q+\mathbf1_{\mathcal B_q},
\qquad
|\mathcal B_q|=N_q\theta_q,
\]

for a Boolean bonus family \(\mathcal B_q\), and
\(f_q=\mathbf1_{\mathcal B_q}-\theta_q\mathbf1\). In particular,
\(\|f_q\|_2^2=\beta_q\), and its \(U_0,U_1\) parts vanish.

For a transposition \(\tau\), let

\[
b_q(F,\tau)
=\frac12\#\bigl\{p=\{S,\tau S\}:S\ne\tau S,
\mathbf1_{\mathcal B_q}(S)\ne
\mathbf1_{\mathcal B_q}(\tau S)\bigr\}.
\tag{5.1}
\]

This is exactly the odd-pair floor: a moved pair has odd total load if and
only if precisely one endpoint is a bonus target.

### Theorem 5.1

At exact floor balance,

\[
\boxed{
\frac14\|f_q-\tau f_q\|_2^2=b_q(F,\tau)}
\tag{5.2}
\]

for every \(\tau\), and

\[
\boxed{
\mathbb E_\tau b_q(F,\tau)
=\frac2n\beta_q
+\sum_{j\ge3}
\frac{(j-2)(n-j-1)}{n(n-1)}
\|f_{q,j}\|_2^2.}
\tag{5.3}
\]

#### Proof

On a moved pair, the two Boolean values are either equal, contributing
zero to both sides of (5.2), or differ by one. In the latter case the pair
contributes \(2/4=1/2\) to the squared-norm side and \(1/2\) to (5.1).
This proves (5.2).

Every Johnson edge \(\{S,T\}\) is \(T=\tau S\) for a unique coordinate
transposition \(\tau\). Hence

\[
\sum_\tau b_q(F,\tau)
=\frac12|\partial_J\mathcal B_q|
=\frac12\langle f_q,L_Jf_q\rangle.
\]

The Johnson eigenvalue on \(U_j\) is \(j(n-j+1)\). Separate its value
\(2(n-1)\) at \(j=2\), use \(\|f_q\|_2^2=\beta_q\), and divide by
\(\binom n2\). This gives (5.3). \(\square\)

Thus, at floor balance, the term \(2\beta_q/n\) is not merely an algebraic
subtraction. It is the \(U_2\)-rate part of the exact local transposition
parity floor. The higher-harmonic part of the same parity floor is the
surplus in (5.3). There is no \(U_1\) contribution.

## 6. Exact floor-corrected harmonic ledger

Put \(f_{q,j}=\operatorname{proj}_{U_j}f_q\), and define

\[
\mathcal S_H=
\sum_{q\le H}\frac1{c_q}
\sum_{j\ge3}
\frac{(j-2)(n-j-1)}{n(n-1)}
\|f_{q,j}\|_2^2.
\tag{6.1}
\]

Equations (3.1), (3.2), and (4.2) give the identity

\[
\boxed{
\frac14\mathbb E_\tau A_{\tau,H}
=\frac2n(\mathcal Q_H+B_H)+\mathcal S_H.}
\tag{6.2}
\]

Let

\[
\mathcal R_H=\frac14\mathbb E_\tau V_{\tau,H}.
\]

Fair independent component-side choices produce an actual exact factor and
obey

\[
\boxed{
\mathbb E\mathcal Q_H(F')
=\mathcal Q_H(F)
-\frac14\mathbb E_\tau(A_{\tau,H}-V_{\tau,H})}
\tag{6.3}
\]

and hence

\[
\boxed{
\mathbb E\mathcal Q_H(F')
=\left(1-\frac2n\right)\mathcal Q_H(F)
+\mathcal R_H-\frac2nB_H-\mathcal S_H.}
\tag{6.4}
\]

Thus the floor term is the \(U_2\) rate \(2/n\) applied to the unavoidable
integer norm \(B_H\). It is not a \(U_1\) contribution, and it is not the
actual \(U_2\) projection of a balanced histogram; higher-harmonic mass is
accounted for exactly by \(\mathcal S_H\).

## 7. The indexing no-go

Had \(U_1\) been allowed, its rate in (3.1) would be \(1/(n-1)\), and the
all-transposition coefficient would be \(2n\). The true floor coefficient
is \(4(n-1)\). Their difference is

\[
[4(n-1)-2n]B_H=(2n-4)B_H,
\tag{7.1}
\]

which is \(\Theta_L(nW\sqrt m)\), not \(o(nW)\). Per random
transposition, the omitted floor is

\[
\left(\frac2n-\frac1{n-1}\right)B_H
=\left(\frac{\kappa_L}{L}+o(1)\right)H\,t.
\tag{7.2}
\]

Therefore a \(U_1\)-calibrated floor correction is asymptotically wrong by
one full Catalan mesoscopic error term.

There is a second normalization trap. A transposition removes only a
\(\Theta(1/n)\) fraction of a \(U_2\) norm. Thus a constant-coefficient
one-transposition gap cannot be obtained from harmonic smoothing; the
coefficient and the additive error must both be on the transposition scale.
A uniform full coordinate permutation instead satisfies

\[
\frac14\mathbb E_\sigma A_{\sigma,H}
=\frac12(\mathcal Q_H+B_H),
\]

which is the constant-scale mesoscopic normalization. It must not be mixed
with the \(U_1\) or \(U_2\) transposition eigenvalues.

## 8. The next exact statement

The correctly normalized one-step statement sufficient for fixed-window
MWB is: for some \(\eta_L>0,C_L<\infty\), every exact factor satisfies

\[
\boxed{
\frac14\mathbb E_\tau
(A_{\tau,H}-V_{\tau,H})
\ge
\frac{\eta_L}{n}\mathcal Q_H(F)
-\frac{C_L}{n}H\,t.}
\tag{8.1}
\]

Equivalently, by (6.2),

\[
\boxed{
\mathcal R_H-\mathcal S_H
\le
\frac2nB_H
+\frac{2-\eta_L}{n}\mathcal Q_H(F)
+\frac{C_L}{n}H\,t.}
\tag{8.2}
\]

To verify sufficiency, take a global minimizer \(F_*\) of
\(\mathcal Q_H\). Every component-switch child is an exact factor, so the
left side of (8.1) is at most zero at \(F_*\). Hence

\[
\mathcal Q_H(F_*)
\le\frac{C_L}{\eta_L}H\,t=o(W).
\]

Since \(2O_q\le Q_q\), this gives the fixed-window MWB estimate.

No \(U_1\) term can help prove (8.1): it is identically zero. The slow term
is the physical \(U_2\) component covariance, while all \(j\ge3\) coherent
gain is represented by the exact rebate \(\mathcal S_H\).

## Exact scope

The proved no-go is:

1. component innovations have no Johnson \(U_1\) part;
2. \(U_2\) is the sharp first possible mode;
3. the \(U_1\)-based floor is wrong by
   \(\Theta_L(H\operatorname{Cat}_m)\) per transposition; and
4. standard representation theory plus the forced marginal identities
   cannot improve the \(U_2\) rate.

This does not prove (8.1). Any proof of (8.1) must use additional physical
information about exact ownership components, beyond their integrality,
equal row counts, point margins, and transposition anti-invariance.
