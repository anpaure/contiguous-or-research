# Active-row no-recycling across transpositions

Date: 2026-07-25

Status: theorem-level pure mathematics. No search, solver, finite
computation, or signed-factor surrogate is used. Every child below is
obtained by one common signing of the freshly recomputed genuine ownership
components of one coordinate transposition. Hence every child is a literal
integral exact wreath factor.

---

## 0. Outcome

Put

\[
n=2m+1,\qquad t=\operatorname{Cat}_m,\qquad
W=nt=\binom nm,
\]

\[
H=\lceil A\sqrt m\rceil,\qquad
r_q=m-q,\qquad
N_q=\binom n{r_q},\qquad
c_q=\left\lfloor\frac W{N_q}\right\rfloor,
\]

\[
d_q=r_q(n-r_q)=(m-q)(m+q+1),\qquad
T_n=\binom n2.
\]

Here \(A>0\) is fixed, and \(m\) is sufficiently large that
\(H\le m-2\).

This report proves an exact active-row comparison across distinct
transpositions.

First, if \(V_{\tau,q}\) is the genuine component variance at depth \(q\),
then

\[
\boxed{
\sum_\tau V_{\tau,q}
\le 2W(d_q-2)+4d_q\Pi_q(F),
\qquad
\Pi_q(F)=\sum_S\binom{\mu_q(S)}2.
}
\tag{0.1}
\]

The collision coefficient is \(d_q\), not \(T_n\): one duplicated literal
target can be reused only by the \(d_q\) transpositions which actually move
that target. No component-size or connectivity assumption occurs.

Second, depth one admits a sharper star-matching identity. For every
Johnson edge \(e=ST\), transport the occurrence matching at \(T\) by the
unique transposition taking \(S\) to \(T\), and superpose it on the
occurrence matching at \(S\). Let \(p_e^+,p_e^-\) count the two orientations
of imbalanced alternating paths, and let \(d_{e,K}\) be their signed count
inside the genuine component \(K\). Define

\[
\Delta_e=(p_e^+)^2+(p_e^-)^2-\sum_Kd_{e,K}^2\ge0.
\]

Then the full two-coordinate contribution is exactly

\[
\boxed{
A_{e,1}-V_{e,1}=2\Delta_e-4p_e^+p_e^-.
}
\tag{0.2}
\]

Thus \(\Delta_e\) is the positive active-path dispersion across freshly
recomputed components, while \(p_e^+p_e^-\) is the exact
opposite-orientation recycling.

Third, these identities give a literal averaged reduced descent:

\[
\boxed{
G^{\rm red}(F)\ge
\max\left\{0,
\frac{\mathfrak D_1(F)+\mathfrak A_{\ge2}(F)
      -\mathfrak C_{\ge2}(F)}{4T_n}
-\delta_m\right\},
}
\tag{0.3}
\]

where all three numerator terms are explicit in Theorem 4.1 and

\[
\delta_m=\Gamma_AQ_0^4\frac tn,\qquad
Q_0=\lfloor m^{1/8}\rfloor,\qquad
\Gamma_A=81e^{2(A+3)^2}.
\tag{0.4}
\]

Consequently one actual component signing has reduced gain
\(>D_AHt/n\) whenever

\[
\mathfrak D_1+\mathfrak A_{\ge2}-\mathfrak C_{\ge2}
>
4T_n\left(\delta_m+D_A\frac{Ht}{n}\right).
\tag{0.5}
\]

There is a clean fixed-\(A\) positive branch. Suppose the first-shadow load
is maximally saturated:

\[
\mu_1=M\mathbf1_{\mathcal A},
\qquad
M=\left\lfloor\frac{m+2}{2}\right\rfloor.
\tag{0.6}
\]

For a boundary edge \(e=ST\), \(S\in\mathcal A\),
\(T\notin\mathcal A\), let \(x_{e,K}\) be the number of the \(M\) owner rows
of \(S\) lying in the fresh \(\tau_e\)-component \(K\), and put

\[
\operatorname{sep}(e)
=\sum_{K<L}x_{e,K}x_{e,L}.
\tag{0.7}
\]

Then

\[
\boxed{
\sum_\tau(A_{\tau,1}-V_{\tau,1})
=4\sum_{e\in\partial_J\mathcal A}\operatorname{sep}(e).
}
\tag{0.8}
\]

There is no internal high--high restitution: two maximum matchings have
only balanced alternating cycles and balanced alternating paths, for both
parities of \(m+2\).

Exact point margins make \(\mathcal A\) a Johnson \(1\)-design and force

\[
\boxed{
|\partial_J\mathcal A|
\ge 2(n-1)\frac WM(1-\alpha),
\qquad
\alpha=\frac{|\mathcal A|}{N_1}
=\frac{m+2}{mM}.
}
\tag{0.9}
\]

If a fraction \(\varphi\) of this boundary splits its \(M\)-packet among
at least two fresh components, and a fraction \(\vartheta\) of the
resulting fair depth-one gain survives the exact deeper restitution, then

\[
\boxed{
G^{\rm red}(F)
\ge
4\vartheta\varphi
\left(1-\frac1M\right)(1-\alpha)t-\delta_m.
}
\tag{0.10}
\]

Thus the target \(D_AHt/n\) follows whenever

\[
4\vartheta\varphi
\left(1-\frac1M\right)(1-\alpha)
>
D_A\frac Hn+\Gamma_A\frac{Q_0^4}{n}.
\tag{0.11}
\]

The right side is \(O_A(m^{-1/2})\). In particular,

\[
\vartheta\varphi\gg_A m^{-1/2}
\tag{0.12}
\]

is already sufficient. This is a constructive escape, not a new
obstruction. What remains unproved is the unconditional implication from
high reduced energy to (0.5), or to the split-and-survival condition
(0.11). No claim of \(LM_A\) or constant one is made.

---

## 1. Exact heat normalization

For a row \(C\in F\), let

\[
w_{C,q}=\mathbf1_{\mathcal W_{r_q}(C)},
\qquad
\mu_q=\sum_{C\in F}w_{C,q}.
\tag{1.1}
\]

For an exact factor \(F\), define

\[
Q_q(F)
=\sum_{|S|=r_q}
(\mu_q(S)-c_q)(\mu_q(S)-c_q-1),
\qquad
\mathcal Q_A(F)=\sum_{q\le H}\frac{Q_q(F)}{c_q}.
\tag{1.0}
\]

Let

\[
\mathcal S_2(F)
=\sum_{q\le Q_0}\frac{\|P_{q,2}f_q\|_2^2}{c_q},
\qquad
f_q=\mu_q-\frac W{N_q}\mathbf1,
\]

where \(P_{q,2}\) is orthogonal projection to Johnson degree \(2\). Put

\[
\mathcal Q_A^{\rm red}(F)=\mathcal Q_A(F)-\mathcal S_2(F).
\]

For a genuine component signing \(I\) in the fresh \(\tau\)-cell, write

\[
G_\tau^{\rm red}(F)
=\max_I\left[
\mathcal Q_A^{\rm red}(F)
-\mathcal Q_A^{\rm red}(F^{\tau,I})\right],
\qquad
G^{\rm red}(F)=\max_\tau G_\tau^{\rm red}(F),
\]

where the empty signing is included.

Fix an unordered coordinate transposition \(\tau\). Let \(K\) range over
the genuine ownership components of \(F\) against \(\tau F\). We identify
the two shores by their old row labels. This is legitimate: among the
\(n\) middle windows of any row, some window contains both transposed
coordinates or neither of them, since otherwise their total incidence
would be \(n\), whereas it is \(2m=n-1\). That middle root is fixed by
\(\tau\), and joins the old row \(C\) to the new row \(\tau C\) in the
same overlay component. Define

\[
d_{K,q}=\sum_{C\in K}(w_{C,q}-\tau w_{C,q}),
\tag{1.2}
\]

\[
A_{\tau,q}
=\left\|\sum_Kd_{K,q}\right\|_2^2
=\|\mu_q-\tau\mu_q\|_2^2,
\qquad
V_{\tau,q}=\sum_K\|d_{K,q}\|_2^2.
\tag{1.3}
\]

Set

\[
A_\tau=\sum_{q\le H}\frac{A_{\tau,q}}{c_q},
\qquad
V_\tau=\sum_{q\le H}\frac{V_{\tau,q}}{c_q}.
\tag{1.4}
\]

Fair independent signs on the complete components use one common sign at
all depths. The exact antipodal identity gives

\[
\mathbb E_\varepsilon
\bigl[\mathcal Q_A(F)-\mathcal Q_A(F_\varepsilon)\bigr]
=\frac{A_\tau-V_\tau}{4}.
\tag{1.5}
\]

Every \(F_\varepsilon\) is a literal exact factor. The verified shallow
\(E_2\) chronology comparison gives

\[
|\mathcal S_2(F)-\mathcal S_2(F_\varepsilon)|
\le\delta_m.
\tag{1.6}
\]

Therefore

\[
\boxed{
G_\tau^{\rm red}(F)
\ge\frac{A_\tau-V_\tau}{4}-\delta_m,
}
\tag{1.7}
\]

and the empty signing gives \(G_\tau^{\rm red}\ge0\). The target-pair
arguments below are applied only to the full unprojected norm; reduction is
made once, through (1.6).

---

## 2. Literal row budget across distinct transpositions

For rows \(C,D\), put

\[
h_q(C,D)=\langle w_{C,q},w_{D,q}\rangle,
\qquad
\Pi_q(F)=\sum_{C<D}h_q(C,D)
=\sum_{|S|=r_q}\binom{\mu_q(S)}2.
\tag{2.1}
\]

### Lemma 2.1 (one-row transposition boundary)

Let \(w_C\) be the indicator of the cyclic \(r\)-intervals of one row,
where \(2\le r\le m-1\). If the transposed coordinates have shorter cyclic
distance \(\ell\in\{1,\ldots,m\}\) in \(C\), then

\[
\boxed{
\|w_C-\tau w_C\|_2^2
=4\left(\min\{r,\ell\}-\mathbf1_{\{\ell=r\}}\right).
}
\tag{2.2}
\]

Consequently

\[
\boxed{
\sum_\tau\|w_C-\tau w_C\|_2^2
=2n\bigl(r(n-r)-2\bigr).
}
\tag{2.3}
\]

#### Proof

Exactly \(2\min\{r,\ell\}\) supported intervals contain one transposed
coordinate and not the other. Normally all leave the support. If
\(\ell=r\), exactly one internal Johnson edge of the cyclic interval cycle
has colour \(\tau\); its two endpoints are exchanged and must be removed
from the leaving count. The symmetric difference counts each leaving
interval twice, proving (2.2).

There are \(n\) coordinate pairs at each distance \(1,\ldots,m\), and

\[
\sum_{\ell=1}^m\min\{r,\ell\}=\frac{r(n-r)}2.
\]

Summation proves (2.3). \(\square\)

For \(r=r_q\), summing over the \(t=W/n\) rows gives

\[
\boxed{
\sum_\tau R_{\tau,q}=2W(d_q-2),
\qquad
R_{\tau,q}
=\sum_C\|w_{C,q}-\tau w_{C,q}\|_2^2.
}
\tag{2.4}
\]

### Lemma 2.2 (one duplicated target has \(d_q\) moving colours)

For distinct rows \(C,D\), set

\[
a_C^\tau=w_{C,q}-\tau w_{C,q}.
\]

Then

\[
\boxed{
\sum_\tau
\bigl(\langle a_C^\tau,a_D^\tau\rangle\bigr)_+
\le2d_qh_q(C,D).
}
\tag{2.5}
\]

#### Proof

Since \(a_C^\tau(S)\in\{-1,0,1\}\),

\[
\bigl(\langle a_C^\tau,a_D^\tau\rangle\bigr)_+
\le
\sum_S\bigl(a_C^\tau(S)a_D^\tau(S)\bigr)_+.
\]

A positive coordinate product is either \(++\), charged to the common old
target \(S\), or \(--\), charged to the common old target \(\tau S\).
In either case the charged target is moved. A fixed rank-\(r_q\) target is
moved by exactly \(d_q=r_q(n-r_q)\) unordered transpositions, and each can
supply at most these two charges. Summing over the \(h_q(C,D)\) common
targets proves (2.5). \(\square\)

### Theorem 2.3 (active-row no-recycling)

For every exact factor, every \(q\le H\), and arbitrary component sizes,

\[
\boxed{
\sum_\tau V_{\tau,q}
\le2W(d_q-2)+4d_q\Pi_q(F).
}
\tag{2.6}
\]

More strongly, with

\[
R_{\tau,H}=\sum_{q\le H}\frac{R_{\tau,q}}{c_q},
\qquad
V_{\tau,H}=\sum_{q\le H}\frac{V_{\tau,q}}{c_q},
\]

\[
\boxed{
\sum_\tau(V_{\tau,H}-R_{\tau,H})_+
\le4\sum_{q\le H}\frac{d_q\Pi_q(F)}{c_q}.
}
\tag{2.7}
\]

#### Proof

Expanding inside the actual component partition gives

\[
V_{\tau,q}-R_{\tau,q}
=2\sum_K\sum_{\substack{C<D\\C,D\in K}}
\langle a_C^\tau,a_D^\tau\rangle.
\tag{2.8}
\]

Take the positive part, discard negative terms, and then discard the
same-component restriction. Lemma 2.2 yields

\[
\sum_\tau(V_{\tau,q}-R_{\tau,q})_+
\le4d_q\Pi_q(F).
\tag{2.9}
\]

Combine this with (2.4) to obtain (2.6). For the weighted form, first use

\[
\left(\sum_q\frac{x_q}{c_q}\right)_+
\le\sum_q\frac{(x_q)_+}{c_q},
\]

then apply (2.9). \(\square\)

The exact floor conversion is

\[
\boxed{
\Pi_q(F)=P_q^{\min}+\frac{Q_q(F)}2,
\qquad
P_q^{\min}
=c_qW-\binom{c_q+1}{2}N_q.
}
\tag{2.10}
\]

This follows by expanding both sides.

There is also a pointwise size-free cap:

\[
\boxed{
V_{\tau,q}\le R_{\tau,q}+4\Pi_q(F)
\le
\left(1+\frac{\Pi_q(F)}t\right)R_{\tau,q}.
}
\tag{2.11}
\]

Indeed,

\[
\langle a_C^\tau,a_D^\tau\rangle
=2\bigl(h_q(C,D)-\langle w_{C,q},\tau w_{D,q}\rangle\bigr)
\le2h_q(C,D),
\]

which proves the first inequality from (2.8); the second uses
\(R_{\tau,q}\ge4t\), a consequence of (2.2).

At \(q=1\),

\[
c_1=1,\qquad
P_1^{\min}=W-N_1=\frac{2W}{m+2},
\]

so the factor in (2.11) is exactly

\[
1+\frac{\Pi_1}t
=1+\frac{2n}{m+2}+\frac{Q_1}{2t}.
\tag{2.12}
\]

At terminal energy \(\mathcal Q_A=O_A(Ht)\), this is
\(O_A(\sqrt m)\), independently of component size.

For completeness, (2.7) also bounds the growing-harmonic effective shield
count. Put

\[
R^-_{m,H}=2t\sum_{q\le H}\frac{m-q-1}{c_q}.
\tag{2.13}
\]

For every real \(s>1\),

\[
\boxed{
k_s^{\rm eff}
\le
\left\lfloor
\frac{4\sum_{q\le H}d_q\Pi_q/c_q}
{(s-1)R^-_{m,H}}
\right\rfloor.
}
\tag{2.14}
\]

To prove the denominator, for fixed \(\tau=(ab)\) let
\(\ell_C\) be the shorter cyclic distance between \(a,b\) in row \(C\),
and set \(s_C=m-\ell_C\). Counting middle roots containing both \(a,b\)
gives

\[
\sum_Cs_C=\binom{2m-1}{m-2}=\frac{m-1}{2}t.
\tag{2.15}
\]

The chord bound

\[
(q-s)_+\le q\left(1-\frac{s}{m-1}\right)
\qquad(0\le s\le m-1)
\]

implies

\[
\sum_C(q-s_C)_+\le\frac{qt}{2}.
\]

Insert this in (2.2), losing at most \(4t\) at
\(\ell_C=m-q\), to obtain

\[
R_{\tau,q}\ge2(m-q-1)t.
\tag{2.16}
\]

Thus \(R_{\tau,H}\ge R^-_{m,H}\). If
\(V_\tau^{>J}>sR_{\tau,H}\), then

\[
(V_{\tau,H}-R_{\tau,H})_+>(s-1)R^-_{m,H},
\]

because \(V_\tau^{>J}\le V_{\tau,H}\). Summing and applying (2.7) proves
(2.14).

---

## 3. Exact depth-one star paths

For an \((m-1)\)-set \(S\), let

\[
\mathcal X_S
=\left\{X\in\binom{[n]}m:S\subset X\right\}.
\]

This star has \(m+2\) middle roots. If a row \(C\) owns \(S\) as a cyclic
\((m-1)\)-interval, exactly two consecutive middle windows of \(C\)
contain \(S\). Join them and label the edge by \(C\). Since exact-factor
rows have disjoint middle roots, these edges form a matching
\(\mathcal M_S\) of size \(\mu_1(S)\). Hence

\[
\boxed{
0\le\mu_1(S)\le
M:=\left\lfloor\frac{m+2}{2}\right\rfloor.
}
\tag{3.1}
\]

Fix an edge \(e=\{S,T\}\) of \(J(n,m-1)\), and let \(\tau_e\) be the
unique transposition with \(\tau_eS=T\). Transport
\(\mathcal M_T\) to a matching on \(\mathcal X_S\), and superpose it on
\(\mathcal M_S\).

The union is a two-coloured multigraph of alternating paths and even
cycles. Common matching edges must be retained as red--blue parallel
\(2\)-cycles, or cancelled in matched pairs; collapsing one to a single
uncoloured edge would create a false imbalance.

For an alternating component \(L\), set

\[
\epsilon(L)
=|E(L)\cap\mathcal M_S|
-|E(L)\cap\tau_e\mathcal M_T|
\in\{-1,0,1\}.
\tag{3.2}
\]

Let \(p_e^+\) and \(p_e^-\) count the components with signs \(+1\) and
\(-1\).

### Lemma 3.1 (star components are globally component-feasible)

Every alternating star component lies in one genuine
\(F/\tau_eF\) ownership component.

#### Proof

At a shared star root \(X\), the red edge is labelled by the old row
owning \(X\). The blue edge is transported from the old row owning
\(\tau_eX\), and hence is labelled on the new shore by its
\(\tau_e\)-image. The middle root \(X\) is exactly an overlay edge joining
these row vertices. By the shore identification proved in Section 1, both
old row labels lie in that same genuine component. Propagation along an
alternating component proves the claim. A one-colour one-edge path is
assigned to the component containing its single row label. \(\square\)

For a genuine component \(K\), let \(a_{e,K}\) and \(b_{e,K}\) count its
\(+1\) and \(-1\) star paths. Then

\[
d_{e,K}:=a_{e,K}-b_{e,K}=d_{K,1}(S),
\qquad
d_{K,1}(T)=-d_{e,K},
\tag{3.3}
\]

and

\[
\mu_1(S)-\mu_1(T)=p_e^+-p_e^-.
\tag{3.4}
\]

### Theorem 3.2 (exact star-path dispersion)

Define

\[
\Delta_e
=(p_e^+)^2+(p_e^-)^2-\sum_Kd_{e,K}^2.
\tag{3.5}
\]

Then

\[
\boxed{\Delta_e\ge0,}
\tag{3.6}
\]

\[
\boxed{
A_{e,1}-V_{e,1}
=2\Delta_e-4p_e^+p_e^-,
}
\tag{3.7}
\]

and, for both parities of \(m+2\),

\[
\boxed{
p_e^+\le\min\{\mu_1(S),M-\mu_1(T)\},
\qquad
p_e^-\le\min\{\mu_1(T),M-\mu_1(S)\}.
}
\tag{3.8}
\]

#### Proof

Writing \(a_K=a_{e,K}\), \(b_K=b_{e,K}\),

\[
\sum_K(a_K-b_K)^2
\le\sum_Ka_K^2+\sum_Kb_K^2
\le\left(\sum_Ka_K\right)^2
 +\left(\sum_Kb_K\right)^2,
\]

which proves (3.6).

The two target coordinates give

\[
A_{e,1}=2(p_e^+-p_e^-)^2,
\qquad
V_{e,1}=2\sum_Kd_{e,K}^2.
\]

Subtracting proves (3.7).

Every \(+\)-path uses a red edge and has two distinct endpoints unmatched
by the blue matching. Therefore

\[
p_e^+\le\mu_1(S),
\qquad
2p_e^+\le m+2-2\mu_1(T).
\]

Taking the integer floor gives
\(p_e^+\le M-\mu_1(T)\), including odd \(m+2\). The other inequality is
symmetric. \(\square\)

Define the clipped collision

\[
\psi_M(x,y)=
\begin{cases}
xy,&x+y\le M,\\
(M-x)(M-y),&x+y\ge M.
\end{cases}
\tag{3.9}
\]

Equation (3.8) gives the exact support-feasible dichotomy

\[
\boxed{
p_e^+p_e^-\le
\psi_M(\mu_1(S),\mu_1(T)).
}
\tag{3.10}
\]

In the low half, opposite recycling consumes one occurrence from each
target; in the high half, it consumes one unused star slot from each
target. The expression vanishes on every edge for loads in \(\{0,M\}\).

### Corollary 3.3 (uniform first-shadow component cap)

For every component \(K\), target \(S\), and transposition \(\tau\),

\[
|d_{K,1}(S)|\le M.
\tag{3.10a}
\]

Moreover,

\[
\boxed{
V_{\tau,1}\le M R_{\tau,1}
\le2M(m+1)t<2MW.
}
\tag{3.10b}
\]

Indeed, (3.10a) follows from the star matching. Therefore

\[
V_{\tau,1}
\le M\sum_{K,S}|d_{K,1}(S)|
\le M\sum_{C,S}|w_{C,1}(S)-w_{C,1}(\tau S)|
=MR_{\tau,1}.
\]

For the last bound, let \(\ell_C\) be the shorter cyclic distance of the
transposed pair in row \(C\). Counting middle windows containing both
coordinates gives

\[
\sum_C(m-\ell_C)=\frac{m-1}{2}t,
\qquad
\sum_C\ell_C=\frac{m+1}{2}t.
\]

If \(z_\tau^{\rm far}\) is the number of rows with
\(\ell_C\in\{m-1,m\}\), the exact row formula (2.2) gives

\[
\boxed{
R_{\tau,1}=2(m+1)t-4z_\tau^{\rm far},
\qquad
2(m-1)t\le R_{\tau,1}\le2(m+1)t.
}
\tag{3.10c}
\]

Each unordered Johnson edge belongs to one unique unordered coordinate
transposition, and its two target coordinates are already included in
(3.7). Therefore there is no extra ordering factor:

\[
\boxed{
\mathfrak D_1(F)
:=\sum_\tau(A_{\tau,1}-V_{\tau,1})
=\sum_{e\in E(J(n,m-1))}
\left(2\Delta_e-4p_e^+p_e^-\right).
}
\tag{3.11}
\]

There is a robust hard-core lower bound which does not require all loads to
belong to \(\{0,M\}\). Let

\[
\mathcal B_{M0}
=\left\{e=\{S,T\}\in E(J(n,m-1)):
\{\mu_1(S),\mu_1(T)\}=\{M,0\}\right\}.
\tag{3.12}
\]

Orient \(e\in\mathcal B_{M0}\) from its load-\(M\) endpoint. Its \(M\)
one-edge paths are the active owner rows of that endpoint. Define
\(\operatorname{sep}(e)\) as the number of their unordered pairs lying in
different fresh \(\tau_e\)-components, and put

\[
\operatorname{Sep}_{M0}(F)
=\sum_{e\in\mathcal B_{M0}}\operatorname{sep}(e),
\qquad
\Psi_1(F)
=\sum_{e\in E(J(n,m-1))}
\psi_M(\mu_1(S),\mu_1(T)).
\tag{3.13}
\]

On an \(M\)--\(0\) edge, (3.7) is exactly
\(4\operatorname{sep}(e)\). On every other edge, (3.6), (3.7), and
(3.10) give a lower bound \(-4\psi_M\). Hence

\[
\boxed{
\mathfrak D_1(F)
\ge4\operatorname{Sep}_{M0}(F)-4\Psi_1(F).
}
\tag{3.14}
\]

---

## 4. Averaged negative reduced gain

Let

\[
f_q=\mu_q-\frac W{N_q}\mathbf1,
\]

and let \(P_{q,j}\) be Johnson degree \(j\). Define the exact full deeper
coherent heat

\[
\mathfrak A_{\ge2}(F)
=2\sum_{q=2}^H\sum_{j\ge2}
\frac{j(n-j+1)}{c_q}\|P_{q,j}f_q\|_2^2.
\tag{4.1}
\]

The transposition spectral identity gives

\[
\mathfrak A_{\ge2}
=\sum_\tau\sum_{q=2}^H\frac{A_{\tau,q}}{c_q}.
\tag{4.2}
\]

Define the active-row capacity

\[
\mathfrak C_{\ge2}(F)
=2W\sum_{q=2}^H\frac{d_q-2}{c_q}
 +4\sum_{q=2}^H\frac{d_q\Pi_q(F)}{c_q}.
\tag{4.3}
\]

Theorem 2.3 gives

\[
\sum_\tau\sum_{q=2}^H\frac{V_{\tau,q}}{c_q}
\le\mathfrak C_{\ge2}(F).
\tag{4.4}
\]

### Theorem 4.1 (constructive averaged reduced descent)

For every fixed \(A>0\), all sufficiently large \(m\), and every exact
factor \(F\),

\[
\boxed{
G^{\rm red}(F)\ge
\max\left\{0,
\frac{\mathfrak D_1(F)+\mathfrak A_{\ge2}(F)
      -\mathfrak C_{\ge2}(F)}{4T_n}
-\delta_m\right\}.
}
\tag{4.5}
\]

In particular, a literal component signing with reduced gain
\(>D_AHt/n\) exists whenever

\[
\boxed{
\mathfrak D_1+\mathfrak A_{\ge2}-\mathfrak C_{\ge2}
>
4T_n\left(\delta_m+D_A\frac{Ht}{n}\right).
}
\tag{4.6}
\]

#### Proof

Sum (1.7) over all \(T_n\) transpositions. The depth-one sum is exactly
\(\mathfrak D_1\) by (3.11). Equations (4.2) and (4.4) lower-bound the
sum of the deeper \(A-V\) terms by
\(\mathfrak A_{\ge2}-\mathfrak C_{\ge2}\). Hence

\[
\sum_\tau G_\tau^{\rm red}
\ge
\frac{\mathfrak D_1+\mathfrak A_{\ge2}
      -\mathfrak C_{\ge2}}4
-T_n\delta_m.
\]

The maximum is at least the average, and the empty cut gives gain zero.
This proves (4.5); (4.6) follows. \(\square\)

The full spectrum in (4.1) is intentional. The one payment \(\delta_m\)
already converts the complete full-objective gain to reduced gain.
Replacing (4.1) by the retained spectrum while retaining \(\delta_m\)
would be valid but would discard shallow \(E_2\) twice.

### Corollary 4.2 (robust nonsaturated hard-core escape)

Every exact factor obeys

\[
\boxed{
G^{\rm red}(F)\ge
\max\left\{0,
\frac{
4\operatorname{Sep}_{M0}(F)-4\Psi_1(F)
+\mathfrak A_{\ge2}(F)-\mathfrak C_{\ge2}(F)}
{4T_n}
-\delta_m\right\}.
}
\tag{4.7}
\]

Thus a literal reduced gain \(>D_AHt/n\) exists whenever

\[
\boxed{
4\operatorname{Sep}_{M0}-4\Psi_1
+\mathfrak A_{\ge2}-\mathfrak C_{\ge2}
>
4T_n\left(\delta_m+D_A\frac{Ht}{n}\right).
}
\tag{4.8}
\]

This follows by substituting (3.14) in Theorem 4.1. It is useful when the
first-shadow histogram has a large saturated \(M\)--\(0\) boundary but a
nonempty residual family of intermediate loads: the latter is charged
exactly by the clipped collision \(\Psi_1\), rather than being discarded.

---

## 5. Saturated first-shadow packets

Assume

\[
\mu_1=M\mathbf1_{\mathcal A},
\qquad
M=\left\lfloor\frac{m+2}{2}\right\rfloor.
\tag{5.1}
\]

Then

\[
|\mathcal A|=\frac WM,
\qquad
\alpha:=\frac{|\mathcal A|}{N_1}
=\frac{m+2}{mM}.
\tag{5.2}
\]

The exact depth-one floor energy is

\[
\boxed{
Q_1(F)=2N_1+(M-3)W.
}
\tag{5.3}
\]

Indeed, a zero target contributes \(2\), and a load-\(M\) target
contributes \((M-1)(M-2)\).

### Lemma 5.1 (forced Johnson boundary)

The family \(\mathcal A\) is an exact \(1\)-design, and

\[
\boxed{
|\partial_J\mathcal A|
\ge2(n-1)\frac WM(1-\alpha).
}
\tag{5.4}
\]

#### Proof

Every physical row contains each coordinate in exactly \(m-1\) of its
first-shadow intervals. Thus

\[
\sum_{S\ni v}\mu_1(S)=(m-1)t
\qquad(v\in[n]).
\]

Under (5.1), every point belongs to exactly \((m-1)t/M\) members of
\(\mathcal A\). Hence
\(\mathbf1_{\mathcal A}-\alpha\mathbf1\) has Johnson degrees \(0,1\)
equal to zero. The first available Laplacian eigenvalue is \(2(n-1)\), so

\[
|\partial_J\mathcal A|
=\langle\mathbf1_{\mathcal A},
L_J\mathbf1_{\mathcal A}\rangle
\ge2(n-1)N_1\alpha(1-\alpha),
\]

which is (5.4). \(\square\)

For \(e=ST\in\partial_J\mathcal A\), orient the edge with
\(S\in\mathcal A\). The red star matching has \(M\) edges and the blue
matching is empty. Its \(M\) one-edge alternating paths are precisely the
\(M\) active owner rows of \(S\). Put

\[
x_{e,K}
=\#\{\text{these rows in the fresh }\tau_e\text{-component }K\}.
\tag{5.5}
\]

Then

\[
\sum_Kx_{e,K}=M,\qquad
\Delta_e=M^2-\sum_Kx_{e,K}^2.
\tag{5.6}
\]

Define

\[
\operatorname{sep}(e)=\sum_{K<L}x_{e,K}x_{e,L}.
\tag{5.7}
\]

Therefore

\[
\boxed{\Delta_e=2\operatorname{sep}(e).}
\tag{5.8}
\]

If both endpoints of a Johnson edge lie in \(\mathcal A\), both star
matchings have maximum size \(M\). For even \(m+2\), their union consists
of alternating cycles. For odd \(m+2\), each matching leaves one vertex
unmatched: equal unmatched vertices again give cycles, while distinct
unmatched vertices give one even alternating path which begins in one
colour and ends in the other. Thus every star component has equal red and
blue edge counts, and

\[
d_{e,K}=0\qquad\text{for every }K.
\tag{5.9}
\]

Low--low edges are trivial. Equations (3.7)--(3.8) now give

\[
\boxed{
\sum_\tau(A_{\tau,1}-V_{\tau,1})
=4\operatorname{Sep}(F),
\qquad
\operatorname{Sep}(F)
:=\sum_{e\in\partial_J\mathcal A}\operatorname{sep}(e).
}
\tag{5.10}
\]

This is the sharp active-row no-recycling identity: every unordered pair
of active owners separated by its fresh boundary component partition
contributes exactly one unit to the summed fair depth-one gain.

If the \(M\) owners meet \(h_e\) components, then

\[
\boxed{
\Delta_e\ge(h_e-1)(2M-h_e).
}
\tag{5.11}
\]

Indeed, among \(h_e\) positive integer parts summing to \(M\), the sum of
squares is maximized by
\(M-h_e+1,1,\ldots,1\). In particular,

\[
h_e\ge2
\quad\Longrightarrow\quad
\operatorname{sep}(e)\ge M-1.
\tag{5.12}
\]

### Theorem 5.2 (hard-quota constructive escape)

Define the exact signed deeper restitution

\[
\mathfrak J_{\ge2}(F)
=\sum_\tau\sum_{q=2}^H
\frac{V_{\tau,q}-A_{\tau,q}}{c_q}.
\tag{5.13}
\]

Then every exact factor satisfying (5.1) obeys

\[
\boxed{
G^{\rm red}(F)
\ge
\max\left\{0,
\frac{\operatorname{Sep}(F)}{T_n}
-\frac{\mathfrak J_{\ge2}(F)}{4T_n}
-\delta_m\right\}.
}
\tag{5.14}
\]

If \(Q_q(F)=0\) for \(2\le q\le H\), then
\(\mathfrak J_{\ge2}\ge0\): at each such rank the starting floor energy is
zero and every literal child has nonnegative floor energy. The identity
(5.14) itself does not require \(Q_q=0\).

Suppose that, for some \(0<\vartheta\le1\),

\[
\boxed{
\mathfrak J_{\ge2}(F)
\le4(1-\vartheta)\operatorname{Sep}(F).
}
\tag{5.15}
\]

If a fraction \(\varphi\) of the boundary edges in (5.4) have
\(h_e\ge2\), then

\[
\boxed{
G^{\rm red}(F)
\ge
4\vartheta\varphi
\left(1-\frac1M\right)(1-\alpha)t
-\delta_m.
}
\tag{5.16}
\]

#### Proof

Insert (5.10) and the exact deeper term
\(-\mathfrak J_{\ge2}\) into (1.7), sum over \(\tau\), and average.
This proves (5.14). Under (5.15), its affine term is at least

\[
\vartheta\frac{\operatorname{Sep}(F)}{T_n}-\delta_m.
\]

Equations (5.4) and (5.12) give

\[
\operatorname{Sep}(F)
\ge
2\varphi(M-1)(n-1)\frac WM(1-\alpha).
\]

Use \(W=nt\) and \(T_n=n(n-1)/2\) to obtain (5.16).
\(\square\)

### Corollary 5.3 (fixed-\(A\) target scale)

Under the hypotheses of Theorem 5.2, a literal component signing with

\[
G^{\rm red}(F)>D_A\frac{Ht}{n}
\]

exists whenever

\[
\boxed{
4\vartheta\varphi
\left(1-\frac1M\right)(1-\alpha)
>
D_A\frac Hn+\Gamma_A\frac{Q_0^4}{n}.
}
\tag{5.17}
\]

For fixed \(A,D_A\), the right side is \(O_A(m^{-1/2})\), while
\(M\to\infty\) and \(\alpha\to0\). Thus

\[
\vartheta\varphi\gg_A m^{-1/2}
\tag{5.18}
\]

is sufficient. This is an integral fixed-window escape at exactly the
reduced-gain scale needed by the constant-one route.

---

## 6. Independent audit and precise boundary

The decisive steps were independently checked.

1. Equation (2.5) was checked both by coordinate charging and by

   \[
   \langle a_C^\tau,a_D^\tau\rangle
   =2\bigl(h_q(C,D)-\langle w_{C,q},\tau w_{D,q}\rangle\bigr).
   \]

2. The factor \(2\) in (3.7) comes from retaining both target coordinates
   \(S,T\). The Johnson edge is unordered and belongs to one unique
   transposition, so (3.11) has no further factor.

3. Common star-matching edges are parallel two-coloured \(2\)-cycles.

4. A \(\tau\)-fixed middle root in the star is an ordinary star vertex and
   creates no exception to the alternating-path decomposition.

5. In odd star size, a heavy path needs two endpoints unmatched by the
   opposite matching, proving the same integer cap \(M-\mu\).

6. In the saturated high--high case, every alternating component is
   balanced, so there is no internal restitution term.

7. The star identity is unprojected. The reduced conclusion uses the
   separate uniform comparison (1.6), avoiding an invalid pairwise
   decomposition after Johnson projection.

### Proved

* The component-size-free cross-transposition bounds
  (2.6), (2.7), (2.11), and (2.14).
* The exact star-path dispersion identity (3.7), its parity-safe caps
  (3.8), the clipped dichotomy (3.9)--(3.10), the uniform cap
  (3.10a)--(3.10c), and the robust hard-core bound (3.14).
* The general constructive averaged descent (4.5)--(4.6) and its
  nonsaturated specialization (4.7)--(4.8).
* The hard-quota separation identity (5.10), forced Johnson boundary
  (5.4), and fixed-\(A\) escape (5.14)--(5.18).

### Not proved

* A universal lower bound on the split fraction \(\varphi\).
* A universal strict survival bound (5.15) on deeper restitution.
* An implication from arbitrary high reduced energy to (4.6) or (5.17).
* A high-energy exact factor local for every transposition.

The lane has therefore advanced from a giant-component obstruction to a
literal constructive comparison. In the saturated branch, after deeper
restitution is accounted for, more than an \(O_A(m^{-1/2})\) fraction of
the forced Johnson boundary must avoid complete active-row recycling.
Proving that cross-transposition dispersion statement, or its nonsaturated
clipped analogue from (3.9), would supply the required adaptive reduced cut
and close this branch of \(LM_A\).
