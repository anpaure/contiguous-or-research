# K10 common-base matching reflections: exact renewal and proper-cut compilation

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

## 0. Outcome

Put

\[
n=2m+1,\qquad B=\operatorname{Cat}_m=\frac1n\binom nm,
\qquad H=\lceil A\sqrt m\rceil .
\tag{0.1}
\]

This note proves the missing **physical common-base statement** for three
matching reflections.  It is stronger than a construction at one prepared
factor: the three cells exist afresh at every exact-factor endpoint.

Let \(M\) be a near-perfect matching of the coordinate set and let

\[
g_M=\prod_{e\in M}e .
\tag{0.2}
\]

Thus \(g_M\) has cycle type \(1\,2^m\).  At an arbitrary exact middle
wreath factor \(F\), form the owner components for the elementary abelian
coordinate group \(\Gamma_M=\langle M\rangle\).  Each component has a
\(\Gamma_M\)-invariant middle root.  Independently replacing any component
by its \(g_M\)-image gives a literal exact factor.  If the chosen component
set is nonempty and proper, that corner is reached by exactly \(m\)
nonempty proper freshly recomputed transposition cuts, one for each edge of
\(M\).

The associated fair cell has the exact floor-sensitive Haar identity

\[
\boxed{
\mathbb E\bigl[\mathcal Q_H(F_\varepsilon)-\mathcal Q_H(F)\bigr]
=\frac{V_M(F)-A_M(F)}4 .}
\tag{0.3}
\]

It fixes the \(g_M\)-invariant part of the centered load at every corner,
not merely on average.

There is a stronger version.  Give every \(\Gamma_M\)-owner root an
arbitrary, independently chosen phase in the whole group \(\Gamma_M\).
All phases can still be compiled in one common pass of at most \(m\) proper
cuts.  A common global phase is first divided out; it does not change the
energy.  The resulting exact group-Haar identity is

\[
\boxed{
\mathbb E\bigl[\mathcal Q_H(F_{\boldsymbol\gamma})-
\mathcal Q_H(F)\bigr]
=\mathscr V_M(F)-\mathscr A_M(F),
\qquad
\mathscr A_M=\|(I-\Pi_M)f(F)\|_H^2,}
\tag{0.3a}
\]

where \(\Pi_M\) is averaging over \(\Gamma_M\).  This full group cell is
also renewable at every endpoint.

Apply this to the productive matching \(\mathcal R_m\) of K10.  Complete
its product reflection to a conjugate of the audited triple \(s,r,t\).
The first two matching edge sets form a Hamilton path and the third is
\(\mathcal R_m\).  Their union has at most \(2m+1=n\) colours and maximum
degree three.  Hence the K10 \(1/16\)-prepared factor, and every later exact
endpoint, has three simultaneous literal reflection-Haar macro-cells using
only that degree-three menu.  The audited frame gives

\[
\boxed{
\sum_{a\in\{s,r,t\}} A_a(F)
\ge \frac{\mathcal Q_H(F)+\beta_H}{25n^6}.}
\tag{0.4}
\]

Here \(\beta_H\ge0\) is the exact adjacent-integer floor baseline defined
below.  Thus the three coherent displacements span every centered
Gaussian-window direction.

For the full matching-group cells, the two alternating path groups alone
give the sharper self-contained frame

\[
\boxed{
\mathscr A_s(F)+\mathscr A_r(F)+\mathscr A_t(F)
\ge\frac{2}{n^3}
\bigl(\mathcal Q_H(F)+\beta_H\bigr).}
\tag{0.4a}
\]

Thus the state-renewed group atlas has a uniform \(2n^{-3}\) spanning
constant on the exact-factor profile space, without using a diameter bound for the three product
reflections.

What is not proved is the needed upper bound for the **joined-owner
variances** \(V_s,V_r,V_t\).  K10's seam count is taken in the separate
single-transposition overlays and does not by itself bound these three
joined variances.  The common-base/root-persistence problem is therefore
closed; the surviving quantitative statement is exactly

\[
\sum_{a\in\{s,r,t\}}(A_a-V_a)
\ge 12\lambda_m\bigl(\mathcal Q_H-C_AHB\bigr),
\tag{0.5}
\]

with \(\lambda_m=m^{-O(1)}\), uniformly at every renewed endpoint.  Section
5 proves that (0.5) is sufficient, using only proper cuts, to reach
\(O_A(HB)=o(W)\).

No constant-one conclusion is claimed.

## 1. Exact floor notation

At depth \(q\le H\), write

\[
r_q=m-q,\qquad N_q=\binom n{r_q},\qquad
\frac W{N_q}=c_q+\theta_q,
\tag{1.1}
\]

where \(c_q=\lfloor W/N_q\rfloor\) and \(0\le\theta_q<1\).  For an exact
factor \(F\), let

\[
f_q(F)=\mu_q^F-\frac W{N_q}{\bf1},\qquad
\|f(F)\|_H^2=\sum_{q=1}^H\frac{\|f_q(F)\|_2^2}{c_q}.
\tag{1.2}
\]

The unhalved floor energy is

\[
\mathcal Q_H(F)=
\sum_{q=1}^H\frac1{c_q}
\sum_{|S|=r_q}
(\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1).
\tag{1.3}
\]

Because every exact factor has total depth-\(q\) load \(W\), direct
expansion gives

\[
\boxed{
\mathcal Q_H(F)=\|f(F)\|_H^2-\beta_H,\qquad
\beta_H=\sum_{q=1}^H
\frac{N_q\theta_q(1-\theta_q)}{c_q}.}
\tag{1.4}
\]

In particular \(\beta_H\) is independent of \(F\).  All energy identities
below therefore retain the integer floor exactly.

## 2. Group-owner roots

Let \(F\) be any exact middle wreath factor and let \(\Gamma\le S_n\).
For a wreath row \(C\), denote its set of owned middle masks by
\(\mathcal W_m(C)\).  Define a graph on the rows of \(F\) by joining
\(C,D\in F\) whenever there are

\[
X\in\mathcal W_m(C),\qquad \gamma\in\Gamma,
\qquad \gamma X\in\mathcal W_m(D).
\tag{2.1}
\]

Call its connected components the \(\Gamma\)-owner components.  For one
component \(K\), put

\[
U_K=\mathop{\dot\bigcup}_{C\in K}\mathcal W_m(C).
\tag{2.2}
\]

### Lemma 2.1 (invariant disjoint roots)

The sets \(U_K\) partition \(\binom{[n]}m\), and

\[
\gamma U_K=U_K\qquad(\gamma\in\Gamma).
\tag{2.3}
\]

For every \(\gamma\in\Gamma\), the row family \(\gamma K\) is an exact
factor of the same root \(U_K\).  Consequently, choosing independently
either \(K\) or \(\gamma K\) on every root gives a literal exact middle
wreath factor.

#### Proof

Exactness of \(F\) makes the union in (2.2) disjoint, and the roots plainly
partition the middle layer.  If \(X\in U_K\), let \(C\in K\) own \(X\).
For \(\gamma\in\Gamma\), let \(D\in F\) be the unique owner of
\(\gamma X\).  Relation (2.1) puts \(D\) in the same component as \(C\).
Thus \(\gamma X\in U_K\), proving \(\gamma U_K\subseteq U_K\).  Apply the
same argument to \(\gamma^{-1}\) for equality.

The middle masks of \(\gamma K\) are exactly \(\gamma U_K=U_K\), each
once.  Different roots are disjoint, so arbitrary rootwise choices remain
exact.  \(\square\)

This proves the required component/root disjointness without referring to
an overlay computed at an earlier state.

## 3. A matching reflection compiles in one fresh pass

Let

\[
M=\{e_1,\ldots,e_m\}
\tag{3.1}
\]

be a near-perfect matching of coordinate transpositions.  Its edges are
pairwise disjoint, so

\[
\Gamma_M=\langle e_1,\ldots,e_m\rangle\cong(C_2)^m,
\qquad g_M=e_m\cdots e_1
\tag{3.2}
\]

and \(g_M^2=1\).

We use the following elementary fact to certify properness.

### Lemma 3.1 (no transposition-invariant subfactor)

Assume \(m\ge2\).  If \(P\) is a nonempty row subfamily of an exact factor
\(F\), then for every coordinate transposition \(e\),

\[
eP\ne P.
\tag{3.3}
\]

#### Proof

First, every wreath row \(C\) owns an \(e\)-fixed middle mask.  Indeed,
among its \(n=2m+1\) cyclic middle windows, each endpoint of \(e\) occurs
in exactly \(m\) windows.  If every window contained exactly one endpoint,
the total endpoint incidence would be \(n=2m+1\), whereas it is \(2m\).
Thus some window contains both endpoints or neither and is fixed by \(e\).

Suppose \(eP=P\), choose \(C\in P\), and put \(D=eC\in P\).  If \(T\)
is an \(e\)-fixed middle mask owned by \(C\), then \(T=eT\) is also owned
by \(eC=D\).  Exactness forces \(C=D\).  But an unoriented cyclic order on
odd \(n\ge5\) points cannot be fixed by one coordinate transposition: its
stabilizer on labels is dihedral; a nonidentity rotation is not a single
transposition, while an odd-cycle reflection swaps exactly \(m\ge2\)
pairs.  This contradiction proves (3.3).  \(\square\)

### Theorem 3.2 (parallel proper-cut compilation)

Let \(K\) range over the freshly defined \(\Gamma_M\)-owner components of
an arbitrary exact factor \(F\).  Choose a component set \(\mathscr S\) and
put

\[
U=\mathop{\dot\bigcup}_{K\in\mathscr S}U_K.
\tag{3.4}
\]

The exact factor which uses \(g_MK\) for \(K\in\mathscr S\) and \(K\)
otherwise is reachable from \(F\) by at most \(m\) freshly recomputed
complete-component cuts, all using colours of \(M\).

If \(\mathscr S\) is nonempty and proper, then all \(m\) stages are
nonempty proper cuts.

#### Proof

By Lemma 2.1, both \(U\) and its complement are invariant under every
\(e_j\).  Starting from \(F\), at stage \(j\) freshly compute the complete
\(e_j\)-ownership components and select all components whose middle roots
lie in \(U\), and no component outside \(U\).  Invariance prevents an
overlay edge, and hence a connected component, from crossing
\(U/U^c\).  The cut therefore applies \(e_j\) to every current row over
\(U\) and leaves every row over \(U^c\) unchanged.

Induction gives, after stage \(j\),

\[
(e_j\cdots e_1)(F|_U)\ \dot\cup\ F|_{U^c}.
\tag{3.5}
\]

After all \(m\) stages this is the asserted rootwise \(g_M\)-phase child.
This argument recomputes the overlay at every stage; no persistence of an
old component is assumed.

If \(\mathscr S\) is nonempty and proper, then \(U,U^c\) both contain
rows at every stage.  Lemma 3.1, applied to the current exact factor,
shows that neither of the two current row subfamilies is
\(e_j\)-invariant.  Hence the fresh overlay has an active component on
both sides of the root boundary.  The chosen component set at stage \(j\)
is therefore nonempty and is not the whole overlay.  Every stage is a
proper cut.  \(\square\)

The improvement over processing owner roots separately is important: a
single common reflection phase uses \(m\) cuts total, not \(m\) times the
number of chosen roots.

### Theorem 3.3 (all matching-group phases in one pass)

For each \(\Gamma_M\)-owner component \(K\), choose an arbitrary phase
\(\gamma_K\in\Gamma_M\), and choose one reference component \(K_0\).
Put \(\gamma_0=\gamma_{K_0}\) and

\[
\gamma'_K=\gamma_0^{-1}\gamma_K.
\tag{3.6}
\]

Then the normalized exact factor

\[
F_{\boldsymbol\gamma'}=\mathop{\dot\bigcup}_K\gamma'_KK
\tag{3.7}
\]

is reachable from \(F\) by exactly \(r(\boldsymbol\gamma;K_0)\) nonempty
proper freshly recomputed cuts, all in colours of \(M\), where

\[
r(\boldsymbol\gamma;K_0)
=\#\{j:\text{some }K\text{ has a different }e_j\text{-bit from }K_0\}
\le m.
\tag{3.8}
\]

Moreover

\[
F_{\boldsymbol\gamma'}=\gamma_0^{-1}F_{\boldsymbol\gamma},
\qquad
F_{\boldsymbol\gamma}=\mathop{\dot\bigcup}_K\gamma_KK,
\tag{3.9}
\]

so the normalized child is a global coordinate translate of the prescribed
child and has exactly the same floor energy.  If all phases are equal then
\(r=0\).  If they are not all equal then \(1\le r\le m\).

If one prescribed reference component \(K_0\) already has
\(\gamma_{K_0}=1\), then \(F_{\boldsymbol\gamma'}=
F_{\boldsymbol\gamma}\), so the prescribed child itself is reached by
exactly \(r\) proper cuts.

#### Proof

Write uniquely

\[
\gamma_K=\prod_{j=1}^m e_j^{b_{K,j}},
\qquad b_{K,j}\in\{0,1\}.
\tag{3.10}
\]

The \(e_j\)-bit of \(\gamma'_K\) is

\[
b'_{K,j}=b_{K,j}\mathbin\oplus b_{K_0,j}.
\tag{3.11}
\]

At stage \(j\), let \(U_j\) be the union of the owner roots with
\(b'_{K,j}=1\).  Every \(U_j\) is \(\Gamma_M\)-invariant.  If it is empty,
omit the stage.  Otherwise it is not the whole middle layer, because the
reference root \(U_{K_0}\) is excluded by \(b'_{K_0,j}=0\).  The proof of
Theorem 3.2 shows that one fresh \(e_j\)-cut applies \(e_j\) simultaneously
on precisely those roots.  Lemma 3.1 supplies an active fresh component
inside \(U_j\) and another in its nonempty complement.  Thus this stage is
nonempty and proper.

The matching edges commute.  After all nonempty stages, root \(K\) has
accumulated exactly \(\prod_j e_j^{b'_{K,j}}=\gamma'_K\).  The number of
used stages is exactly (3.8).  Finally, abelianness and the
\(\Gamma_M\)-invariance of every owner root give (3.9).  Coordinate
relabeling preserves \(\mathcal Q_H\), completing the proof.  \(\square\)

This parallel bit routing is special to the matching group.  It improves
the general root-by-root word-length compilation bound to one common pass,
even though the root phases are all different.

## 4. Exact matching-reflection Haar identity

For a \(\Gamma_M\)-owner component \(K\), let \(z_K\) be the stacked
lower-load effect of replacing \(K\) by \(g_MK\).  Use the weighted norm
from (1.2), and define

\[
A_M(F)=\left\|\sum_K z_K\right\|_H^2
=\|g_Mf(F)-f(F)\|_H^2,
\qquad
V_M(F)=\sum_K\|z_K\|_H^2.
\tag{4.1}
\]

Since \(g_MU_K=U_K\) and \(g_M^2=1\),

\[
g_Mz_K=-z_K.
\tag{4.2}
\]

Let \(F_\varepsilon\) choose \(g_MK\) when \(\varepsilon_K=+1\) and
\(K\) when \(\varepsilon_K=-1\).  Lemma 2.1 makes every corner literal
and exact.

### Theorem 4.1 (renewable common-base kernel)

For every sign vector,

\[
\boxed{
f(F_\varepsilon)
=P_Mf(F)+\frac12\sum_K\varepsilon_Kz_K,
\qquad P_M=\frac{I+g_M}{2}.}
\tag{4.3}
\]

In particular

\[
P_Mf(F_\varepsilon)=P_Mf(F)
\tag{4.4}
\]

at every corner.  For independent fair signs,

\[
\boxed{
\mathbb E\|(I-P_M)f(F_\varepsilon)\|_H^2
=\frac{V_M(F)}4,\qquad
\|(I-P_M)f(F)\|_H^2=\frac{A_M(F)}4,}
\tag{4.5}
\]

and the exact floor drift is (0.3).

If \(A_M(F)>V_M(F)\), some corner of strictly smaller energy is reached
from \(F\) by exactly \(m\) proper fresh cuts.

#### Proof

On each invariant root, the midpoint of the two row phases is
\((K+g_MK)/2\).  Summing over roots gives \(P_Mf(F)\); centering by
\(W/N_q\) commutes with \(g_M\).  This proves (4.3).  Equation (4.2)
proves (4.4), and independence of the signs kills all cross terms, giving
(4.5).

The original endpoint has anti-invariant squared norm \(A_M/4\), while a
fair corner has expected anti-invariant squared norm \(V_M/4\).  The
invariant norm is unchanged.  Subtracting and using the factor-independent
floor identity (1.4) proves (0.3).

If \(A_M>V_M\), the average energy is strictly smaller.  The empty corner
is \(F\), and the full corner is \(g_MF\); both have energy
\(\mathcal Q_H(F)\).  A strictly decreasing corner is therefore nonempty
and proper.  Theorem 3.2 compiles it into exactly \(m\) proper cuts.
\(\square\)

Nothing in Theorem 4.1 is tied to the initial state.  At an arbitrary child
one simply recomputes the three owner partitions.  This is the endpoint
closure absent from the earlier conjugated-chart construction.

### Theorem 4.2 (full matching-group Haar identity)

Let

\[
\Pi_M=\frac1{|\Gamma_M|}\sum_{\gamma\in\Gamma_M}\gamma
\tag{4.6}
\]

be the orthogonal projection onto the \(\Gamma_M\)-invariant profile
space.  For one owner component \(K\), write \(x_K(\gamma)\) for its
stacked lower-load vector in phase \(\gamma K\), and put

\[
\bar x_K=\mathbb E_{\gamma\in\Gamma_M}x_K(\gamma),
\qquad
\mathscr V_M(F)=
\sum_K\mathbb E_{\gamma\in\Gamma_M}
\|x_K(\gamma)-\bar x_K\|_H^2,
\tag{4.7}
\]

and

\[
\mathscr A_M(F)=\|(I-\Pi_M)f(F)\|_H^2.
\tag{4.8}
\]

If the phases \(\gamma_K\) are independent and uniform in \(\Gamma_M\),
then every child is literal and exact,

\[
\Pi_M f(F_{\boldsymbol\gamma})=\Pi_M f(F)
\tag{4.9}
\]

at every corner, and (0.3a) holds exactly.  Moreover every value of the
energy random variable in (0.3a) has an equal-energy normalized
representative reachable by exactly
\(r(\boldsymbol\gamma;K_0)\le m\) proper cuts.  Here \(r=0\) precisely
when all root phases are the same global phase; every nonglobal phase vector
uses between one and \(m\) nonempty proper cuts.

#### Proof

On the root \(U_K\), group averaging gives

\[
\bar x_K=\Pi_Mx_K(1).
\tag{4.10}
\]

Thus the sum of the component means, after subtracting the invariant
constant baseline, is \(\Pi_Mf(F)\).  Every fluctuation
\(x_K(\gamma)-\bar x_K\) is orthogonal to the invariant subspace, proving
(4.9).  Independence and centering kill cross terms between distinct
owner components, whence

\[
\mathbb E\|f(F_{\boldsymbol\gamma})\|_H^2
=\|\Pi_Mf(F)\|_H^2+\mathscr V_M(F).
\tag{4.11}
\]

Orthogonal projection also gives

\[
\|f(F)\|_H^2
=\|\Pi_Mf(F)\|_H^2+\mathscr A_M(F).
\tag{4.12}
\]

Subtract (4.12) from (4.11) and use (1.4) to obtain (0.3a).  The last
assertion is Theorem 3.3.  \(\square\)

### Lemma 4.3 (exact joined Gram curvature and hypercube bridge)

Put

\[
y_K=(I-\Pi_M)x_K(1).
\tag{4.13}
\]

Then

\[
\boxed{
\mathscr A_M=\left\|\sum_Ky_K\right\|_H^2,
\qquad
\mathscr V_M=\sum_K\|y_K\|_H^2,}
\tag{4.14}
\]

and consequently

\[
\boxed{
\mathscr A_M-\mathscr V_M
=2\sum_{K<L}\langle y_K,y_L\rangle_H.}
\tag{4.15}
\]

Moreover the full group variance obeys the exact hypercube Poincare bound

\[
\boxed{
\mathscr V_M
\le\frac14\sum_K\sum_{e\in M}
\|x_K(1)-x_K(e)\|_H^2.}
\tag{4.16}
\]

#### Proof

The first identity in (4.14) follows by summing the owner-component
contributions to \((I-\Pi_M)f(F)\).  For every \(\gamma\in\Gamma_M\),
commutation and isometry give

\[
x_K(\gamma)-\bar x_K
=\gamma\bigl(x_K(1)-\Pi_Mx_K(1)\bigr)=\gamma y_K.
\tag{4.17}
\]

Its norm is \(\|y_K\|_H\), proving the second identity in (4.14).
Expansion gives (4.15).

For (4.16), expand the Hilbert-valued function
\(\gamma\mapsto x_K(\gamma)\) in the Walsh characters of
\(\Gamma_M\cong\{\pm1\}^m\):

\[
x_K(\gamma)=\sum_{S\subseteq M}\widehat x_K(S)\chi_S(\gamma).
\tag{4.18}
\]

Parseval gives

\[
\|y_K\|_H^2
=\sum_{\varnothing\ne S\subseteq M}\|\widehat x_K(S)\|_H^2.
\tag{4.19}
\]

For \(e\in M\), flipping the \(e\)-bit multiplies \(\chi_S\) by \(-1\)
exactly when \(e\in S\).  Hence

\[
\mathbb E_\gamma
\|x_K(\gamma)-x_K(e\gamma)\|_H^2
=4\sum_{S\ni e}\|\widehat x_K(S)\|_H^2.
\tag{4.20}
\]

The left side of (4.20) is independent of \(\gamma\), because

\[
x_K(\gamma)-x_K(e\gamma)
=\gamma\bigl(x_K(1)-x_K(e)\bigr)
\tag{4.21}
\]

and coordinate permutations are isometries.  Sum (4.20) over \(e\),
divide by four, and use \(|S|\ge1\) in (4.19).  This proves (4.16), and
then summing over \(K\) completes the lemma.  \(\square\)

## 5. Three matching reflections on the K10 prepared factor

Let \(\mathcal R_m\) be the productive near-perfect matching furnished by
K10 at its literal laminar-prepared factor \(F_m^{\rm lam}\), and put

\[
t=\prod_{e\in\mathcal R_m}e.
\tag{5.1}
\]

Recall the audited reference triple on \(\mathbb Z_n\):

\[
s_0(x)=-x,\qquad r_0(x)=1-x,
\qquad t_0=u s_0u,\quad u=(0\ 1).
\tag{5.2}
\]

Every one of \(s_0,r_0,t_0,t\) has cycle type \(1\,2^m\).  Choose a
coordinate bijection \(h\) such that

\[
t=h^{-1}t_0h,
\qquad s=h^{-1}s_0h,qquad r=h^{-1}r_0h.
\tag{5.3}
\]

Let \(M_s,M_r\) be the matching edge sets of \(s,r\).  The union

\[
P=M_s\cup M_r
\tag{5.4}
\]

is a Hamilton path.  Indeed, before conjugation every vertex has degree
two except the distinct fixed points of \(s_0,r_0\), which have degree one;
also \(r_0s_0:x\mapsto x+1\) is an \(n\)-cycle, so the union is connected.
It is therefore one path through all \(n\) vertices.

Consequently

\[
\mathcal O=P\cup\mathcal R_m
\tag{5.5}
\]

in fact has at most \(2m+1=n\) coordinate-transposition colours and maximum
degree at most three.  To see the sharper count, \(t_0=us_0u\) agrees with
\(s_0\) on every matching edge except one: \(s_0\) pairs \(1\) with
\(-1\) and fixes \(0\), whereas \(t_0\) pairs \(0\) with \(-1\) and
fixes \(1\).  Hence

\[
|M_s\cap\mathcal R_m|=m-1,
\qquad |P\cup\mathcal R_m|\le2m+1.
\tag{5.5a}
\]

The path edges alone generate \(S_n\).  More importantly for
the three macro-generators, conjugacy transfers the audited facts

\[
\langle s,r,t\rangle=
\begin{cases}
A_n,&m\text{ even},\\
S_n,&m\text{ odd},
\end{cases}
\tag{5.6}
\]

and word diameter less than \(7n^3\).

Apply Theorem 4.1 separately to \(M_s,M_r,\mathcal R_m\).  These are three
literal common-base cells at \(F_m^{\rm lam}\), all supported on the
degree-three menu (5.5).  The same assertion holds after every corner,
because the group-owner components are recomputed from that corner.

For \(a\in\{s,r,t\}\), abbreviate \(A_a=A_{M_a}\), \(V_a=V_{M_a}\).
The audited three-reflection frame, applied depth by depth and then with
weights \(1/c_q\), says

\[
\sum_a\|(I-P_a)f(F)\|_H^2
\ge\frac1{100n^6}\|f(F)\|_H^2.
\tag{5.7}
\]

Since \(A_a=4\|(I-P_a)f(F)\|_H^2\), equations (1.4) and (5.7) prove
(0.4).

There is an equally literal full-group version.  Let \(\Pi_a\) average
over the matching group \(\Gamma_{M_a}\), and abbreviate

\[
\mathscr A_a=\|(I-\Pi_a)f(F)\|_H^2,
\qquad \mathscr V_a=\mathscr V_{M_a}(F).
\tag{5.7a}
\]

Because \(g_a\in\Gamma_{M_a}\), one has
\(\operatorname{Fix}(\Gamma_{M_a})\subseteq\operatorname{Fix}(g_a)\).
Distance to the smaller invariant subspace is larger, and hence (5.7)
implies

\[
\boxed{
\sum_{a\in\{s,r,t\}}\mathscr A_a
\ge\frac1{100n^6}\|f(F)\|_H^2
=\frac{\mathcal Q_H(F)+\beta_H}{100n^6}.}
\tag{5.7b}
\]

For exact-factor profiles this can be sharpened, self-containedly, from
order \(n^{-6}\) to the explicit constant \(2n^{-3}\).  The zero-point-margin
condition is essential in the sharpening.

### Lemma 5.1 (two alternating matching groups form a \(2n^{-3}\) frame)

On the rank-\(k\) subset layer, let

\[
v\in\bigoplus_{j\ge2}U_j^{(k)}.
\tag{5.7d}
\]

Then

\[
\boxed{
\|(I-\Pi_s)v\|_2^2+\|(I-\Pi_r)v\|_2^2
\ge \frac{2}{n^3}\|v\|_2^2.}
\tag{5.7e}
\]

Every exact-factor centered profile satisfies (5.7d) at every retained
depth.  Consequently

\[
\boxed{
\mathscr A_s+\mathscr A_r+\mathscr A_t
\ge \frac{2}{n^3}
\bigl(\mathcal Q_H(F)+\beta_H\bigr).}
\tag{5.7f}
\]

#### Proof

Order the coordinates as \(1,\ldots,n\) along the Hamilton path
\(P=M_s\cup M_r\), and put

\[
\tau_p=(p\ p+1),\qquad
E_p=\|v-\tau_pv\|_2^2
\quad(1\le p<n).
\tag{5.7g}
\]

For \(1\le a<b\le n\), the endpoint transposition \((a\ b)\) has the
adjacent word

\[
(a\ b)=
\tau_a\tau_{a+1}\cdots\tau_{b-1}
\tau_{b-2}\cdots\tau_a,
\tag{5.7h}
\]

of length \(2(b-a)-1\), in which every path edge occurs at most twice.
Telescoping (5.7h), using unitarity and Cauchy--Schwarz, gives

\[
\|v-(a\ b)v\|_2^2
\le4(b-a)\sum_{p=a}^{b-1}E_p.
\tag{5.7i}
\]

After summing over \(a<b\), the coefficient of a fixed \(E_p\) is at
most

\[
4\sum_{a\le p<b}(b-a)
\le4n\,p(n-p)\le n^3.
\tag{5.7j}
\]

Therefore

\[
\sum_{1\le a<b\le n}\|v-(a\ b)v\|_2^2
\le n^3\sum_{p=1}^{n-1}E_p.
\tag{5.7k}
\]

We now use the exact Johnson spectrum, with all normalization factors
displayed.  On \(U_j^{(k)}\), the unnormalized Johnson Laplacian has
eigenvalue

\[
j(n-j+1).
\tag{5.7l}
\]

Every Johnson edge is generated by a unique coordinate transposition, and
each moved two-cycle is counted from both endpoints in the squared norm.
Hence, on \(U_j^{(k)}\),

\[
\sum_{a<b}\|v-(a\ b)v\|_2^2
=2j(n-j+1)\|v\|_2^2.
\tag{5.7m}
\]

The allowed Johnson indices satisfy \(j\le\min(k,n-k)\le n/2\), so
\(j(n-j+1)\) is increasing in \(j\).  Orthogonality of the Johnson modules
and \(j\ge2\) therefore give

\[
\sum_{a<b}\|v-(a\ b)v\|_2^2
\ge4(n-1)\|v\|_2^2.
\tag{5.7n}
\]

Combining (5.7k) and (5.7n),

\[
\sum_{p=1}^{n-1}E_p
\ge\frac{4(n-1)}{n^3}\|v\|_2^2.
\tag{5.7o}
\]

Put \(d_i=\|(I-\Pi_i)v\|_2\), \(i=s,r\).  If
\(\tau_p\in M_i\), then \(\tau_p\Pi_i=\Pi_i\), and so

\[
E_p
=\|(I-\tau_p)(I-\Pi_i)v\|_2^2
\le4d_i^2.
\tag{5.7p}
\]

Both alternating path matchings have exactly \(m=(n-1)/2\) edges.  Thus

\[
\sum_{p=1}^{n-1}E_p
\le4m(d_s^2+d_r^2)
=2(n-1)(d_s^2+d_r^2).
\tag{5.7q}
\]

Equations (5.7o)--(5.7q) prove (5.7e).

It remains only to verify the admissible module condition for the actual
profile.  At depth \(q\), put \(k=m-q\).  Every one of the \(B\) wreath
rows contributes \(n\) cyclic \(k\)-windows, so
\(\sum_S\mu_q^F(S)=nB=W\); hence \(f_q(F)\) has zero total.  A fixed
coordinate belongs to exactly \(k\) of the \(n\) cyclic \(k\)-windows of
each row, and therefore

\[
\sum_{S\ni x}\mu_q^F(S)=kB.
\tag{5.7r}
\]

The constant mean contributes the same amount because

\[
\frac W{\binom nk}\binom{n-1}{k-1}
=\frac{Wk}{n}=kB.
\tag{5.7s}
\]

Thus every point margin of \(f_q(F)\) is zero.  Equivalently
\(f_q(F)\in\bigoplus_{j\ge2}U_j^{(k)}\).  Apply (5.7e) at each depth,
divide by \(c_q\), sum over \(q\le H\), add the nonnegative \(t\)-term,
and use (1.4).  This proves (5.7f).  \(\square\)

Choosing one of the three groups uniformly and then taking independent
uniform phases on its freshly recomputed owner roots gives

\[
\boxed{
\mathbb E[\mathcal Q_H(F')-\mathcal Q_H(F)]
=-\frac13\sum_a(\mathscr A_a-\mathscr V_a).}
\tag{5.7c}
\]

Every strictly decreasing value in this average has an equal-energy
representative reached in one proper matching pass by Theorem 3.3.  Thus
the full-group alternative has the same endpoint renewal and a stronger
invariant projection; its remaining issue is again quantitative component
variance.

If a reflection is selected uniformly and then its owner components are
signed fairly, Theorem 4.1 gives the exact one-block drift

\[
\boxed{
\mathbb E[\mathcal Q_H(F')-\mathcal Q_H(F)]
=-\frac1{12}\sum_{a\in\{s,r,t\}}(A_a(F)-V_a(F)).}
\tag{5.8}
\]

Thus no invariant or anti-invariant mode is omitted: only the sign of the
joined-owner curvature in (5.8) remains.

### Proposition 5.2 (exact iteration criterion)

Let \(T=C_AHB\).  Suppose that at every exact endpoint with
\(\mathcal Q_H(F)>T\), the renewed common-base cells satisfy (0.5) for some
\(0<\lambda_m\le1\).  Then a finite sequence of proper freshly recomputed
cuts, all using colours of (5.5), reaches an exact factor \(F_*\) with

\[
\mathcal Q_H(F_*)\le2T=O_A(HB)=o(W).
\tag{5.9}
\]

The same conclusion holds for the full group-Haar cells if, at every such
endpoint,

\[
\sum_{a\in\{s,r,t\}}(\mathscr A_a-\mathscr V_a)
\ge3\lambda_m(\mathcal Q_H(F)-T).
\tag{5.9a}
\]

#### Proof

Equations (0.5) and (5.8) show that some reflection and some corner obey

\[
\mathcal Q_H(F')
\le\mathcal Q_H(F)-\lambda_m(\mathcal Q_H(F)-T).
\tag{5.10}
\]

When \(\mathcal Q_H(F)>T\), the decrease is strict.  The empty and full
corners have the same energy as \(F\), so the selected corner is nonempty
and proper.  Theorem 3.2 realizes it by \(m\) proper fresh cuts.

Under (5.9a), equation (5.7c) gives the identical inequality (5.10) for
some group-phase child.  Theorem 3.3 supplies an equal-energy representative
using at most \(m\) proper fresh cuts.  Thus the rest of the iteration is
the same in the binary and full-group cases.

As long as \(\mathcal Q_H(F)>2T\), (5.10) gives

\[
\mathcal Q_H(F')\le(1-\lambda_m/2)\mathcal Q_H(F).
\tag{5.11}
\]

After finitely many blocks this forces (5.9).  Finally,

\[
\frac{HB}{W}=\frac Hn=O_A(m^{-1/2})\longrightarrow0,
\tag{5.12}
\]

so (5.9) is the required fixed-window \(o(W)\) scale.  \(\square\)

## 6. Exact boundary

The report proves the following unconditional facts.

1. Every matching reflection, and indeed its full elementary abelian
   matching group, has a literal Haar cell at every exact factor.
2. Every phase assignment has an equal-energy normalized representative
   which compiles in exactly \(r\le m\) freshly recomputed proper cuts,
   where \(r=0\) exactly for a common global phase and \(1\le r\le m\)
   otherwise.
3. K10's productive matching can be completed by two matchings to the
   audited three-reflection frame while retaining a degree-three,
   at-most-\(n\)-colour menu.
4. The three cells coexist at the K10 prepared factor and renew after every
   endpoint; their coherent displacements satisfy the binary full-window
   frame (0.4), while the full group cells satisfy the sharper admissible
   frame (0.4a).
5. The exact curvature inequality (0.5) would now yield
   \(\mathcal Q_H=O_A(HB)=o(W)\) by proper cuts alone.

The unproved quantities are \(V_s+V_r+V_t\) for the binary reflection
cells and \(\mathscr V_s+\mathscr V_r+\mathscr V_t\) for the full group
cells.  In both cases the rows have first been joined into owner components
of the whole elementary abelian matching group.  The
\((11/128-o(1))W\) K10 seams live in separate single-edge overlays and do
not furnish an upper bound for either joined variance.  Establishing
(0.5), its full-group analogue, or a stronger per-cell inequality whose
additive error is already at the relevant frame scale
(\(n^{-6}HB\) for the audited binary bound, \(n^{-3}HB\) for the full
matching-group bound) is the remaining quantitative theorem.  The older
physical common-base and stale chronology objections no longer apply.

Lemma 4.3 further reduces the variance side to explicit joined
single-edge lower-profile norms through (4.16).  It also shows that the
desired curvature is precisely positive cross-component Gram coherence,
not merely the existence or number of K10 seams.
