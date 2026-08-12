# Lane Z7: clipped restitution, cyclic synchronization support, and the parity-slice obstruction

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, computer
algebra, or long computation is used. Every object called an exact factor or an
exact child below is a literal positive integral middle-wreath factor. Formal
coefficient examples are explicitly labelled as non-wreath examples.

---

## 0. Verdict

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad
B=\frac Wn=\operatorname{Cat}_m,\qquad
H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed. The Z5 restitution-gap estimate

\[
I_\sigma(F)-\operatorname{Frag}_\sigma(F)
-\sqrt{S_\sigma(F)\delta_\sigma(F)}
\ge \eta_A\mathcal C_H(F)-K_AHB
\tag{Z5.8.6}
\]

is **not proved** in this report. No genuine high-corridor wreath factor
violating it for every adaptively selected fixed-point involution is
constructed. The report proves four exact advances which sharply change the
form of the surviving gate.

All fixed-window statements are for sufficiently large \(m\), depending on
\(A\), so that \(H\le m-1\). The parity-slice statements impose the further
explicit condition that \(m\) is even.

1. The Z5 maximum-coefficient fragmentation surrogate must be clipped by the
   ideal gain already present at the original corner. There are exact
   quantities \(\operatorname{Coh}_\sigma,\operatorname{Osc}_\sigma\ge0\)
   such that

   \[
   I_\sigma-\operatorname{Frag}_\sigma
   =\operatorname{Coh}_\sigma-\operatorname{Osc}_\sigma,
   \]

   while the true legal gain satisfies the strictly stronger bound

   \[
   \boxed{
   \Gamma_\sigma
   \ge \operatorname{Coh}_\sigma-\operatorname{Sync}_\sigma.}
   \]

   Thus \(\operatorname{Osc}_\sigma\) is not restitution. It is overshoot of
   the untrimmed surrogate.

2. Synchronization is supported only on cyclic incidence edges. If
   \(S_\sigma^\circ\) is the total weight of target--bundle edges which lie
   on an undirected cycle, then

   \[
   \boxed{
   \operatorname{Sync}_\sigma
   \le \operatorname{Fr}_\sigma
   \le \sqrt{S_\sigma^\circ\delta_\sigma}.}
   \]

   Bridge mass, including arbitrarily large tree appendages, creates no
   synchronization residue.

3. Combining the two improvements gives the genuine positive-fibre estimate

   \[
   \boxed{
   \Gamma_\sigma(F)
   \ge
   \operatorname{Coh}_\sigma(F)
   -\sqrt{S_\sigma^\circ(F)\delta_\sigma(F)}.}
   \tag{0.1}
   \]

   The corresponding coherence gate, stated exactly in Section 5, is
   strictly weaker than (Z5.8.6) and gives the same logarithmic
   macro-descent if proved.

4. There is a genuine simultaneous obstruction to the original move family.
   When \(m\) is even, every involution of type \(1\,2^m\) is even and every
   bundled Z5 child preserves the cyclic-order parity census \(N_-\). For
   each realized census value, a corridor minimizer in that slice is therefore
   locally minimal for **every** Z5 fixed-point-involution bundle cell. The
   genuine MSW size-three components realize at least

   \[
   \operatorname{Cat}_{m-3}+1
   =\left(\frac1{64}+o(1)\right)B
   \]

   different slices. Hence (Z5.8.6), if true, forces an \(O_A(HB)\) factor
   separately in each of these \(\Theta(B)\) slices. A high minimum in any
   one slice would be a genuine counterexample to (Z5.8.6), but that lower
   bound is unproved.

The preserved-census mechanism can be escaped in concrete states without
full-Graver closure. Raw two-component orbits may be unbundled, retaining
positive exact component switches but losing conserved target-pair totals;
this changes the census exactly when the two old shores have different
censuses. Alternatively, for even \(m\), odd involutions of type
\(1^3\,2^{m-1}\) preserve the complete binary bundle formalism, are
transitive on every controlled target rank, and have nonconstant Johnson
eigenvalues at most \(1/n\) on every exact-load degree \(j\ge2\). Their
full-flip endpoint has a different census unless \(N_-=B/2\). Neither
enlargement is proved to cross every slice from every factor.

No claim of MWB, constant one, labelled synchronization, or a literal
contiguous-OR word is made.

---

## 1. Imported exact Z5 notation

At depth \(q\le H\), write

\[
r_q=m-q,\qquad N_q=\binom n{r_q},\qquad
c_q=\left\lfloor\frac W{N_q}\right\rfloor.
\]

For an exact factor \(F\), the floor-corrected corridor is

\[
\mathcal C_H(F)
=\sum_{q\le H}\frac1{c_q}
\sum_{S\in\binom{[n]}{r_q}}
\chi_{c_q}(\mu_q^F(S)),
\qquad
\chi_c(t)=(c-t)_+ +(t-c-1)_+.
\tag{1.1}
\]

Fix an involution \(\sigma\) of type \(1\,2^m\). Cancel common rows of
\(F\) and \(\sigma F\), form the middle-ownership overlay, and bundle its
components in \(\sigma\)-orbits. For a bundle \(K\), its two shores are
\(K^+\subset F\) and \(K^-=\sigma K^+\). Choosing one shore of every bundle
gives a positive integral exact factor \(F^\sigma_\varepsilon\).

For a moved target pair

\[
p=(q,\{S,\sigma S\}),
\]

orient it as \(S,\sigma S\) and put

\[
z_{pK}
=\#\{C\in K^+:C\text{ owns }S\}
-\#\{C\in K^+:C\text{ owns }\sigma S\},
\tag{1.2}
\]

\[
M_p=\mu_q^F(S)+\mu_q^F(\sigma S),
\qquad
D_p(\varepsilon)=\sum_K\varepsilon_Kz_{pK}.
\tag{1.3}
\]

The child loads on the pair are

\[
\frac{M_p+D_p(\varepsilon)}2,
\qquad
\frac{M_p-D_p(\varepsilon)}2.
\tag{1.4}
\]

For

\[
b_p=b_{c_q}(M_p)
=(2c_q-M_p)_+ +(M_p-2c_q-2)_+,
\tag{1.5}
\]

the exact two-target cost is

\[
h_{c_q,M_p}(D)=\max\{b_p,|D|-1\}.
\tag{1.6}
\]

Let

\[
r_p=\min_{\eta\in\{\pm1\}^{\mathscr K_\sigma(F)}}
\left|\sum_K\eta_Kz_{pK}\right|.
\tag{1.7}
\]

Z5 proves the exact restitution identity

\[
\Gamma_\sigma(F)
=I_\sigma(F)-\operatorname{Lock}_\sigma(F)
-\operatorname{Sync}_\sigma(F)\ge0,
\tag{1.8}
\]

where

\[
\operatorname{Lock}_\sigma
=\sum_p\frac{(r_p-1-b_p)_+}{c_q}.
\tag{1.9}
\]

The old fragmentation surrogate uses

\[
Z_p=\max_K|z_{pK}|,
\qquad
\operatorname{Frag}_\sigma
=\sum_p\frac{(Z_p-1-b_p)_+}{c_q}.
\tag{1.10}
\]

All sums over \(p\) below range over moved pairs at all controlled depths.

---

## 2. Clipped fragmentation is the correct row restitution

Put

\[
t_p=1+b_p,
\qquad
d_p=|D_p(\mathbf1)|
=|\mu_q^F(S)-\mu_q^F(\sigma S)|.
\tag{2.1}
\]

Define the unweighted pair quantities

\[
i_p=(d_p-t_p)_+,
\qquad
f_p=(Z_p-t_p)_+,
\qquad
\ell_p=(r_p-t_p)_+.
\tag{2.2}
\]

Thus

\[
I_\sigma=\sum_p\frac{i_p}{c_q},\qquad
\operatorname{Frag}_\sigma=\sum_p\frac{f_p}{c_q},\qquad
\operatorname{Lock}_\sigma=\sum_p\frac{\ell_p}{c_q}.
\tag{2.3}
\]

The formula for \(I_\sigma\) follows directly from (1.6): the original
pair cost exceeds its real midpoint floor by
\((d_p-1-b_p)_+\).

### Theorem 2.1 -- clipped fragmentation and coherent gain

For every moved pair,

\[
\boxed{r_p\le\min\{d_p,Z_p\}.}
\tag{2.4}
\]

Consequently,

\[
\boxed{
\ell_p\le
(\min\{d_p,Z_p\}-t_p)_+
=\min\{i_p,f_p\}.}
\tag{2.5}
\]

Define

\[
g_p=(d_p-\max\{Z_p,t_p\})_+,
\qquad
o_p=(Z_p-\max\{d_p,t_p\})_+,
\tag{2.6}
\]

and

\[
\operatorname{Coh}_\sigma
=\sum_p\frac{g_p}{c_q},
\qquad
\operatorname{Osc}_\sigma
=\sum_p\frac{o_p}{c_q}.
\tag{2.7}
\]

Then

\[
\boxed{
I_\sigma-\operatorname{Frag}_\sigma
=\operatorname{Coh}_\sigma-\operatorname{Osc}_\sigma,}
\tag{2.8}
\]

whereas the clipped surrogate

\[
\widehat{\operatorname{Frag}}_\sigma
=\sum_p\frac{\min\{i_p,f_p\}}{c_q}
\tag{2.9}
\]

satisfies

\[
\boxed{
\operatorname{Lock}_\sigma
\le\widehat{\operatorname{Frag}}_\sigma
=I_\sigma-\operatorname{Coh}_\sigma.}
\tag{2.10}
\]

In particular,

\[
\boxed{
\Gamma_\sigma(F)
\ge\operatorname{Coh}_\sigma(F)
-\operatorname{Sync}_\sigma(F).}
\tag{2.11}
\]

#### Proof

The all-plus signing is the original factor, so it is one admissible signing
in (1.7) and gives \(r_p\le d_p\). The Z5 greedy signing argument gives
\(r_p\le Z_p\). This proves (2.4). Since \(u\mapsto(u-t_p)_+\) is
nondecreasing,

\[
\ell_p\le(\min\{d_p,Z_p\}-t_p)_+.
\]

For nonnegative \(d,Z,t\), direct separation into the cases
\(d,Z\le t\), \(d\ge Z\), and \(Z\ge d\) gives

\[
(d-t)_+-(Z-t)_+
=(d-\max\{Z,t\})_+-(Z-\max\{d,t\})_+,
\tag{2.12}
\]

and

\[
(d-t)_+-\min\{(d-t)_+,(Z-t)_+\}
=(d-\max\{Z,t\})_+.
\tag{2.13}
\]

Apply these with \((d,Z,t)=(d_p,Z_p,t_p)\), divide by \(c_q\), and
sum to obtain (2.8)--(2.10). Finally combine (2.10) with the exact identity
(1.8). \(\square\)

The distinction is structural. The old expression subtracts
\(\operatorname{Osc}_\sigma\), even when the original pair has no ideal
gain which that oscillation could restore. The true locking residue cannot
exceed the ideal pair gain.

### Formal sharpness example, not a wreath construction

Take one abstract pair with

\[
c=2,\qquad M=4,\qquad b=0,\qquad t=1,
\]

and two bundle coefficients \(z_1=2,z_2=-2\). The all-plus loads are
\((2,2)\), and the four signings give

\[
(2,2),\quad(0,4),\quad(4,0),\quad(2,2).
\]

Thus every signing has nonnegative integral loads and the pair total is
fixed. Here

\[
d=r=0,\qquad I=\operatorname{Lock}
=\operatorname{Sync}=0,
\]

but \(Z=2\) and the old fragmentation is \(1/c=1/2\). Disjoint
replication makes \(\operatorname{Osc}\) macroscopic while exact restitution
remains zero. This proves that positivity, integrality, pair-total
conservation, and the greedy max bound alone cannot control the untrimmed
surrogate. It is **not** a cyclic-wreath realization and is not used as a
counterexample to (Z5.8.6).

---

## 3. Literal cyclic geometry of bundle fragmentation

For a wreath \(C\), let \(\operatorname{Int}_s(C)\) be its family of \(n\) cyclic
\(s\)-intervals. For an \((m-q)\)-set \(S\), define

\[
a_{q,S}(C)
=\#\{X\in\operatorname{Int}_m(C):S\subseteq X\},
\tag{3.1}
\]

\[
\rho_{q,S}(C)
=a_{q,S}(C)
-(q+1)\mathbf1_{\{S\in\operatorname{Int}_{m-q}(C)\}}.
\tag{3.2}
\]

### Lemma 3.1 -- cyclic containment spill

For every \(1\le q\le m-1\),

\[
\boxed{0\le\rho_{q,S}(C)\le q.}
\tag{3.3}
\]

#### Proof

Complementation sends a cyclic \(m\)-interval \(X\) to a cyclic
\((m+1)\)-interval \(X^c\). Therefore \(X\supseteq S\) is equivalent to
\(X^c\subseteq S^c\). Now

\[
|S^c|=m+q+1<2(m+1).
\]

Hence at most one cyclic run of \(S^c\) can have length at least \(m+1\).
If \(S\) is a cyclic \((m-q)\)-interval, then \(S^c\) is one run of
length \(m+q+1\), containing exactly

\[
(m+q+1)-(m+1)+1=q+1
\]

cyclic \((m+1)\)-intervals. In this case \(\rho=0\). If \(S\) is not a
cyclic interval, then \(S^c\) is not one run. Its unique possible
contributing run has length at most \(m+q\), so it contains at most \(q\)
cyclic \((m+1)\)-intervals. This proves (3.3). \(\square\)

For a bundle \(K\), put

\[
s_K=|K^+|,
\qquad
R_{K,q}(S)=\sum_{C\in K^+}\rho_{q,S}(C).
\tag{3.4}
\]

### Theorem 3.2 -- exact bundle-spill identity

For every moved pair \(p=(q,\{S,\sigma S\})\),

\[
\boxed{
(q+1)z_{pK}
=R_{K,q}(\sigma S)-R_{K,q}(S).}
\tag{3.5}
\]

Consequently,

\[
\boxed{
|z_{pK}|
\le\left\lfloor\frac{q s_K}{q+1}\right\rfloor
=s_K-\left\lceil\frac{s_K}{q+1}\right\rceil.}
\tag{3.6}
\]

#### Proof

Let

\[
U_K=\mathbin{\dot\bigcup}_{C\in K^+}\operatorname{Int}_m(C).
\]

The union is disjoint because \(K^+\) lies in an exact factor. The two
shores of each ownership component partition the same middle-root set.
Since \(K\) is a complete \(\sigma\)-orbit bundle and
\(K^-=\sigma K^+\),

\[
U_K
=\mathbin{\dot\bigcup}_{C\in K^-}\operatorname{Int}_m(C)
=\sigma U_K.
\tag{3.7}
\]

If \(\alpha_K(S)\) counts rows of \(K^+\) owning \(S\), then Lemma 3.1
gives

\[
\#\{X\in U_K:S\subseteq X\}
=(q+1)\alpha_K(S)+R_{K,q}(S).
\tag{3.8}
\]

The left side is unchanged when \(S\) is replaced by \(\sigma S\), by
(3.7). Since

\[
z_{pK}=\alpha_K(S)-\alpha_K(\sigma S),
\]

subtraction proves (3.5). By (3.3), each of
\(R_{K,q}(S),R_{K,q}(\sigma S)\) lies in \([0,qs_K]\). Their difference
therefore has absolute value at most \(qs_K\). It is divisible by
\(q+1\), which proves (3.6). \(\square\)

In particular,

\[
Z_p
=\frac1{q+1}
\max_K|R_{K,q}(\sigma S)-R_{K,q}(S)|.
\tag{3.9}
\]

Thus \(\operatorname{Coh}\) and \(\operatorname{Osc}\) are literal
thresholded spill oscillations, not abstract discrepancy parameters.

### Corollary 3.3 -- exact small-bundle immunity

Every side-size-two bundle has \(|z_{pK}|\le1\) at every controlled depth
and therefore contributes no positive fragmentation. At depth \(q=1\),
the same holds for every side-size-three bundle.

More generally, positive fragmentation at \(p\) forces some maximizing
bundle to satisfy

\[
\boxed{
s_K\ge
\left\lceil\frac{(q+1)(b_p+2)}q\right\rceil.}
\tag{3.10}
\]

#### Proof

For \(s_K=2\), the right side of (3.6) is one for every \(q\ge1\). For
\(q=1,s_K=3\), it is also one. Since \(b_p\ge0\), fragmentation requires
\(Z_p>b_p+1\), hence the integer inequality \(Z_p\ge b_p+2\). Combine
this with (3.6). \(\square\)

---

## 4. Synchronization lives only on cyclic incidence support

For a fixed joint choice of pair-optimal preferred signings
\(\xi^p\in\Sigma_p^{\rm opt}\), form the signed bipartite graph with bundle
vertices \(K\), pair vertices \(p\), and an edge \(pK\) whenever
\(z_{pK}\ne0\). Its edge sign is \(\xi_K^p\), and its weight is

\[
a_{pK}=\frac{2|z_{pK}|}{c_q}.
\tag{4.1}
\]

The support graph itself is independent of the preferred signs. Let
\(E_\sigma^\circ\) be the set of edges which lie on an undirected cycle,
equivalently the non-bridge edges, and put

\[
S_\sigma^\circ
=\sum_{pK\in E_\sigma^\circ}a_{pK}.
\tag{4.2}
\]

Recall that \(\delta_\sigma\) minimizes

\[
\sum_{p,K}a_{pK}
\frac{1-\xi_K^p\langle u_K,v_p\rangle}{2}
\tag{4.3}
\]

over preferred signings and unit vectors, while
\(\operatorname{Fr}_\sigma\) is the minimum signed mismatch mass over one
common family of discrete bundle and target signs.

### Theorem 4.1 -- cyclic-support synchronization bound

\[
\boxed{
\operatorname{Sync}_\sigma
\le\operatorname{Fr}_\sigma
\le\sqrt{S_\sigma^\circ\delta_\sigma}.}
\tag{4.4}
\]

This improves the Z5 bound
\(\operatorname{Fr}_\sigma\le\sqrt{S_\sigma\delta_\sigma}\), since
\(S_\sigma^\circ\le S_\sigma\). In particular, a forest has
\(S_\sigma^\circ=0\) and zero synchronization residue.

#### Proof

Choose preferred signs and unit vectors attaining \(\delta_\sigma\).
Hyperplane-round with a standard Gaussian vector \(g\):

\[
\varepsilon_K=\operatorname{sgn}\langle g,u_K\rangle,
\qquad
t_p=\operatorname{sgn}\langle g,v_p\rangle.
\]

For an edge \(pK\), the violation probability is

\[
\frac{\arccos(\xi_K^p\langle u_K,v_p\rangle)}\pi
\le
\sqrt{
\frac{1-\xi_K^p\langle u_K,v_p\rangle}{2}}.
\]

Count only non-bridge edges and apply weighted Cauchy--Schwarz. The expected
violated non-bridge mass is at most

\[
\sqrt{
S_\sigma^\circ
\sum_{pK\in E_\sigma^\circ}a_{pK}
\frac{1-\xi_K^p\langle u_K,v_p\rangle}{2}}
\le\sqrt{S_\sigma^\circ\delta_\sigma}.
\tag{4.5}
\]

Choose an outcome no worse than this expectation. Delete all bridges of the
support graph and contract each remaining connected component. The bridges
form a forest on the contracted vertices. Multiplying all discrete vertex
signs inside one contracted component by \(-1\) does not change the status
of any internal non-bridge edge. Root each bridge-tree and flip its child
components recursively so that every bridge is satisfied. The final signing
therefore has total mismatch mass equal to its non-bridge mismatch mass,
which is bounded by (4.5). Minimizing proves the second inequality in
(4.4); the first is the exact Z5 Lipschitz comparison. \(\square\)

Combining Theorems 2.1 and 4.1 proves (0.1).

The square-root loss is still a real issue on unbalanced signed cycles. For
example, a uniform unbalanced cycle of length \(L\) and edge weight \(w\)
has vector defect

\[
\delta_C
=\frac{wL}{2}\left(1-\cos\frac\pi L\right).
\tag{4.6}
\]

Indeed, gauge the cycle to one negative edge and write the vector objective
as \(w/4\) times the antiperiodic cycle Dirichlet energy. Its smallest
eigenvalue is \(2-2\cos(\pi/L)\), attained by planar vectors rotating by
\(\pi/L\) per edge. Formula (4.6) is an audit tool for any future claim that
genuine wreath holonomy has small \(\delta_\sigma\); it is not by itself a
wreath realization theorem. In the bipartite target--bundle graph, every
such cycle has even \(L\).

---

## 5. The repaired restitution gate

### Theorem 5.1 -- conditional coherent macro-descent

Fix \(A>0\). Suppose that constants

\[
0<\eta_A\le1,\qquad K_A>0,
\]

and \(m_0(A)\) exist, with \(H\le m-1\) for \(m\ge m_0(A)\), such that,
for every \(m\ge m_0(A)\) and every exact
factor \(F\), some \(\sigma\in\mathcal I_m\) satisfies

\[
\boxed{
\operatorname{Coh}_\sigma(F)
-\sqrt{S_\sigma^\circ(F)\delta_\sigma(F)}
\ge\eta_A\mathcal C_H(F)-K_AHB.}
\tag{R_A^{\rm coh}}
\]

Then steepest positive involution-bundle descent reaches an exact factor
with

\[
\mathcal C_H(F)
\le\frac{2K_A}{\eta_A}HB=o(W)
\tag{5.1}
\]

after at most

\[
1+\left\lceil
\frac2{\eta_A}
\log^+\!\left(
\frac{\mathcal C_H(F_0)}{(2K_A/\eta_A)HB}
\right)
\right\rceil
\tag{5.2}
\]

macrosteps.

#### Proof

By (0.1), the selected cell has a legal child whose gain is at least the
left side of \((R_A^{\rm coh})\). If

\[
\mathcal C_H(F)>\frac{2K_A}{\eta_A}HB,
\]

the gain is greater than \(\eta_A\mathcal C_H(F)/2\). Thus every
macrostep contracts the corridor by at least the factor
\(1-\eta_A/2\). Since
\(-\log(1-\eta_A/2)\ge\eta_A/2\), iteration proves (5.2). Finally,

\[
\frac{HB}{W}=\frac Hn=O_A(m^{-1/2}),
\]

so (5.1) is \(o(W)\). \(\square\)

The original (Z5.8.6) is exactly the stronger condition

\[
\operatorname{Coh}_\sigma
-\operatorname{Osc}_\sigma
-\sqrt{S_\sigma\delta_\sigma}
\ge\eta_A\mathcal C_H-K_AHB.
\tag{5.3}
\]

Thus (Z5.8.6) simultaneously pays for two avoidable proof losses:
max-coefficient overshoot and acyclic synchronization mass. Neither is part
of exact restitution. The genuinely surviving quantitative gate is
\((R_A^{\rm coh})\), or a still sharper version using exact
\(\operatorname{Sync}_\sigma\). This gate remains unproved.

---

## 6. A genuine simultaneous obstruction: cyclic-order parity slices

Assume throughout this section that \(m\ge4\) is even.

Fix one unoriented cyclic order \(C_0\). If \(C=\pi C_0\), define

\[
\epsilon(C)=\operatorname{sgn}(\pi)\in\{\pm1\}.
\tag{6.1}
\]

This is well-defined: rotations of odd length \(n\) are even, and a
reflection has cycle type \(1\,2^m\), hence sign \((-1)^m=1\). For an
exact factor \(F\), put

\[
N_-(F)=\#\{C\in F:\epsilon(C)=-1\}.
\tag{6.2}
\]

### Theorem 6.1 -- every Z5 bundle cell preserves the census

For even \(m\), every \(\sigma\in\mathcal I_m\) is even, and every bundle
child satisfies

\[
\boxed{N_-(F^\sigma_\varepsilon)=N_-(F).}
\tag{6.3}
\]

#### Proof

An involution of type \(1\,2^m\) has sign \((-1)^m=1\). Therefore
\(\epsilon(\sigma C)=\epsilon(C)\) for every wreath row. On each bundle,
\(K^-=\sigma K^+\), so the two shores contain exactly the same number of
negative rows. Replacing any collection of complete bundle shores preserves
their total census. \(\square\)

Let

\[
\mathcal E_m
=\{e:\text{some exact factor }F\text{ has }N_-(F)=e\},
\tag{6.4}
\]

and define the slice minimum

\[
\omega_{A,e}(m)
=\min\{\mathcal C_H(F):F\text{ exact},\ N_-(F)=e\}.
\tag{6.5}
\]

The minimum exists because the exact fibre is finite.

### Theorem 6.2 -- simultaneous local minima in every realized slice

Choose a minimizer \(F_e\) in (6.5). Then, for every
\(\sigma\in\mathcal I_m\),

\[
\boxed{\Gamma_\sigma(F_e)=0,}
\tag{6.6}
\]

and

\[
\boxed{
I_\sigma(F_e)-\operatorname{Frag}_\sigma(F_e)
-\sqrt{S_\sigma(F_e)\delta_\sigma(F_e)}\le0.}
\tag{6.7}
\]

The repaired coherent surrogate is also nonpositive:

\[
\boxed{
\operatorname{Coh}_\sigma(F_e)
-\sqrt{S_\sigma^\circ(F_e)\delta_\sigma(F_e)}\le0.}
\tag{6.7a}
\]

#### Proof

By Theorem 6.1, every vertex of every bundle cell through \(F_e\) remains
in census slice \(e\). Slice minimality makes every child corridor at least
\(\mathcal C_H(F_e)\), while \(F_e\) itself is a cell vertex. Hence the
best cell gain is zero, proving (6.6). The exact restitution identity gives

\[
I_\sigma=\operatorname{Lock}_\sigma+\operatorname{Sync}_\sigma.
\]

Now use
\(\operatorname{Lock}_\sigma\le\operatorname{Frag}_\sigma\) and
\(\operatorname{Sync}_\sigma\le\sqrt{S_\sigma\delta_\sigma}\) to obtain
(6.7). Theorem 2.1 and \(\Gamma_\sigma=0\) give
\(\operatorname{Coh}_\sigma\le\operatorname{Sync}_\sigma\); Theorem 4.1
then proves (6.7a). \(\square\)

### Theorem 6.3 -- linearly many genuine slices

The set of realized census values obeys

\[
\boxed{
|\mathcal E_m|\ge\operatorname{Cat}_{m-3}+1
=\left(\frac1{64}+o(1)\right)B.}
\tag{6.8}
\]

#### Proof

Use the audited canonical MSW ownership overlay for the transposition
\(\tau=(2\ 3)\). Its \(j=1\) stratum contains
\(L=\operatorname{Cat}_{m-3}\) independently switchable components with
three old and three new wreath rows. Since \(\tau\) is odd, it flips the
sign of every row. If one shore of such a component contains \(a\) negative
rows, its other shore contains \(3-a\); switching changes the census by

\[
3-2a\in\{-3,-1,1,3\},
\]

which is never zero. Choose the lower-census shore in every one of the
\(L\) components, then toggle the components one at a time toward their
higher-census shores. The resulting \(L+1\) exact factors have strictly
increasing census values. Finally,

\[
\frac{\operatorname{Cat}_{m-3}}{\operatorname{Cat}_m}
=\frac{m(m-1)(m+1)}
{8(2m-1)(2m-3)(2m-5)}
\longrightarrow\frac1{64}.
\]

\(\square\)

### Corollary 6.4 -- exact consequence and counterexample criterion

If (Z5.8.6) holds with constants \(\eta_A,K_A\), then every sufficiently
large even \(m\) and every \(e\in\mathcal E_m\) satisfy

\[
\boxed{
\omega_{A,e}(m)\le\frac{K_A}{\eta_A}HB.}
\tag{6.9}
\]

The identical conclusion follows if the revised gate
\((R_A^{\rm coh})\) holds with those constants.

Consequently,

\[
\boxed{
\limsup_{\substack{m\to\infty\\m\text{ even}}}
\frac{\max_{e\in\mathcal E_m}\omega_{A,e}(m)}{HB}=\infty
\quad\Longrightarrow\quad
\text{(Z5.8.6) is false}.}
\tag{6.10}
\]

The counterexample furnished by (6.10) would be a genuine exact wreath
factor and would be bad for every adaptively selected
\(\sigma\in\mathcal I_m\).

#### Proof

Apply (Z5.8.6) to \(F_e\). Its left side is nonpositive for every
\(\sigma\), by (6.7), while the asserted selected \(\sigma\) has left side
at least \(\eta_A\omega_{A,e}-K_AHB\). This proves (6.9), and (6.10) is
its contrapositive along a sequence. For \((R_A^{\rm coh})\), use (6.7a)
in exactly the same argument. \(\square\)

The lower bound in (6.10) is **unproved**. Thus Theorem 6.2 is a genuine
simultaneous move-family obstruction, but not yet a counterexample to
(Z5.8.6).

There is also a precise reason that linear shadow arguments do not supply
the missing lower bound. If \(B_r\) is cyclic \(r\)-interval incidence and
\(\epsilon\) is the full sign vector on wreaths, then

\[
\boxed{B_r\epsilon=0\qquad(0\le r\le n).}
\tag{6.11}
\]

For \(1\le r\le n-1\), fix an \(r\)-set \(S\), transpose two coordinates
inside \(S\) or inside \(S^c\), and pair all cyclic orders in which \(S\)
is an interval. The transposition fixes \(S\), reverses \(\epsilon\), and
has no fixed cyclic order because a single transposition is not a
nonidentity element of an odd dihedral stabilizer. The cases \(r=0,n\)
follow from equality of the two sign classes. This proves (6.11). It shows
that census is invisible to the entire linear shadow tower; it does not
show that a low integral factor exists in every census slice.

---

## 7. Concrete stronger positive move sets

The preservation proof in Section 6 is caused by the bundled
anti-invariant restriction, not by positivity of ownership-component
switches. Unbundling exposes a possible census-changing axis; it does not
prove that this axis is nonzero at every factor.

### 7.1 Raw unbundling inside the same involution overlay

Let \(C=(L_C,R_C)\) be one raw connected component of the reduced
\(F/\sigma F\) overlay, with \(L_C\subset F\) and
\(R_C\subset\sigma F\). Let \(\bar C=\sigma C\). Then

\[
\sigma L_C=R_{\bar C},
\qquad
\sigma R_C=L_{\bar C}.
\tag{7.1}
\]

Assume \(m\) is even and \(\{C,\bar C\}\) is a two-component orbit. Put

\[
a=N_-(L_C),\qquad a'=N_-(L_{\bar C}).
\]

Since \(\sigma\) is even,

\[
N_-(R_C)=a',\qquad N_-(R_{\bar C})=a.
\tag{7.2}
\]

Switching neither or both components preserves the census, while switching
only \(C\) changes it by \(a'-a\), and switching only \(\bar C\) changes
it by \(a-a'\). Every one of these four choices is a positive integral
exact factor because it switches complete ownership components.

At the signed profile level, put

\[
e_C=\mathbf1_{L_C}-\mathbf1_{R_C}.
\]

Then

\[
\sigma e_C=-e_{\bar C}.
\tag{7.3}
\]

For raw signs \(s_C,s_{\bar C}\in\{\pm1\}\), define

\[
u=\frac{s_C+s_{\bar C}}2,
\qquad
v=\frac{s_C-s_{\bar C}}2.
\]

The signed deviation from the four-corner midpoint is

\[
\frac12\left[
u(e_C+e_{\bar C})+v(e_C-e_{\bar C})
\right].
\tag{7.4}
\]

The first axis is \(\sigma\)-anti-invariant and the second is
\(\sigma\)-invariant. Z5 bundling keeps only \(v=0\). Raw unbundling
admits the missing invariant axis and changes the parity census precisely
when \(a\ne a'\). Existence of such an orbit at every factor is unproved. Its
price is that the total load on a target pair \(\{S,\sigma S\}\) is no
longer fixed, so the scalar normal form (1.6) does not apply unchanged.

This is a concrete positive enlargement, not full-Graver closure.

### 7.2 Odd three-fixed involutions retain the binary normal form

For even \(m\), let \(\mathcal J_m\) be the conjugacy class of involutions
of type

\[
1^3\,2^{m-1}.
\tag{7.5}
\]

Every member is odd. Cancellation, ownership-component orbit bundling, and
complete-shore signing work verbatim for this class because those arguments
use only \(\sigma^2=1\). In particular, all children remain positive
integral exact factors and every moved target pair retains a conserved total.

### Theorem 7.1 -- controlled-rank transitivity

For every integer \(0\le r\le m-1\) and all
\(S,T\in\binom{[n]}r\), some \(\sigma\in\mathcal J_m\) satisfies
\(\sigma S=T\).

#### Proof

Pair \(S\setminus T\) bijectively with \(T\setminus S\). Put

\[
a=|S\cap T|,
\qquad
b=|[n]\setminus(S\cup T)|.
\]

Then

\[
a+b=n-2|S\setminus T|\ge n-2r\ge3
\]

is odd. If \(a\) is odd and \(b>0\), leave one point fixed in the first
region and two in the second; since positive even \(b\) is at least two,
this is possible. If \(b=0\), then \(a\ge3\), so leave three points fixed
in the first region. Use the symmetric choices when \(b\) is odd. Pair all
remaining points internally within the two invariant regions. Together with
the cross-pairs, this produces exactly three fixed points and \(m-1\)
transpositions, and maps \(S\) to \(T\). \(\square\)

### Theorem 7.2 -- exact Johnson spectrum

Let \(P_r^{(3)}\) average the action of \(\mathcal J_m\) on the rank-
\(r\) slice. For every occurring Johnson degree
\(0\le j\le\min\{r,n-r\}\), its eigenvalue is

\[
\boxed{
\rho_{2a}=\frac{\binom ma}{\binom n{2a}},
\qquad
\rho_{2a+1}=\frac{2a+1}{m}\rho_{2a}.}
\tag{7.6}
\]

Consequently,

\[
\boxed{
0\le\rho_j\le\frac1n
\qquad(2\le j\le m-1),}
\tag{7.7}
\]

while \(\rho_1=1/m\).

#### Proof

The fixed-subset generating polynomial of an involution of type
\(1^3\,2^{m-1}\) is

\[
P(x)=(1+x)^3(1+x^2)^{m-1}.
\]

The degree-\(j\) two-row Johnson character is the fixed-\(j\)-set
character minus the fixed-\((j-1)\)-set character. Its numerator is thus
the coefficient of \(x^j\) in

\[
(1-x)P(x)
=(1+2x-2x^3-x^4)(1+x^2)^{m-1}.
\tag{7.8}
\]

Divide this coefficient by the Johnson-module dimension

\[
d_j=\binom nj-\binom n{j-1}.
\]

With the convention that out-of-range binomial coefficients vanish, the
two coefficient numerators are

\[
A_{2a}=\binom{m-1}{a}-\binom{m-1}{a-2},
\qquad
A_{2a+1}=2\left(\binom{m-1}{a}-\binom{m-1}{a-1}\right).
\tag{7.8a}
\]

Direct substitution of the factorial formulas gives

\[
A_{2a}
=d_{2a}\frac{\binom ma}{\binom n{2a}},
\qquad
A_{2a+1}
=d_{2a+1}\frac{2a+1}{m}
\frac{\binom ma}{\binom n{2a}}.
\tag{7.8b}
\]

This proves (7.6). The even eigenvalues decrease, because

\[
\frac{\rho_{2a+2}}{\rho_{2a}}
=\frac{2a+1}{2(m-a)+1}\le1,
\]

and

\[
\rho_2=\frac m{\binom n2}=\frac1n.
\]

For odd \(j=2a+1\le m-1\) with \(j\ge3\), the factor
\((2a+1)/m\) is less than one, proving (7.7). Formula (7.6) at \(a=0\)
gives \(\rho_1=1/m\). \(\square\)

Every centered exact-factor rank load has Johnson degree zero and degree
one equal to zero: centering kills degree zero, and for every coordinate
\(x\),

\[
\sum_{S\ni x}\mu_q^F(S)=r_qB,
\]

because each wreath has exactly \(r_q\) cyclic \(r_q\)-intervals containing
\(x\). Therefore the coherent exact-load spectrum of \(\mathcal J_m\) is
as strong as the spectrum used in Z5. For arbitrary level-set indicators,
the spectral mixing error changes from \(1/n\) to \(1/m\), only a factor
less than three for all \(m\ge2\).

Finally, because every \(\sigma\in\mathcal J_m\) is odd,

\[
\boxed{N_-(\sigma F)=B-N_-(F).}
\tag{7.9}
\]

The full-flip vertex of the bundle cell is \(\sigma F\). Hence the census
obstruction disappears whenever \(N_-(F)\ne B/2\). The difficult
fragmentation and synchronization estimates do not disappear; no analogue
of \((R_A^{\rm coh})\) is proved for \(\mathcal J_m\).

For odd \(m\), the original class \(1\,2^m\) is already odd. Thus one may
use the parity-unified non-Graver family

\[
\begin{cases}
1\,2^m,&m\text{ odd},\\
1^3\,2^{m-1},&m\text{ even},
\end{cases}
\]

without losing controlled-rank transitivity or the \(1/n\) coherent
spectral ceiling on exact-load degrees.

---

## 8. Independent audit and exact boundary

### Proved in this report

1. The pairwise clipped locking inequality (2.5).
2. The exact decomposition
   \(I-\operatorname{Frag}=\operatorname{Coh}-\operatorname{Osc}\).
3. The genuine gain bound
   \(\Gamma\ge\operatorname{Coh}-\operatorname{Sync}\).
4. The cyclic containment-spill identity (3.5) and the exact bundle-size
   coefficient bound (3.6).
5. Complete immunity of side-size-two bundles, and of depth-one
   side-size-three bundles, from positive fragmentation.
6. The cyclic-support synchronization estimate (4.4).
7. Conditional logarithmic macro-descent under
   \((R_A^{\rm coh})\), with the same constants and terminal scale as Z5.
8. Preservation of cyclic-order parity census by every bundled
   \(1\,2^m\) cell when \(m\) is even.
9. Simultaneous nonpositivity of the complete Z5 restitution surrogate at
   every parity-slice minimizer, for every permitted involution.
10. Existence of at least \(\operatorname{Cat}_{m-3}+1\) realized genuine
    census slices.
11. The exact implication (6.9) and genuine counterexample criterion
    (6.10).
12. Positive raw-component unbundling and its anti-invariant/invariant axis
    decomposition.
13. Controlled-rank transitivity, exact spectrum, positive legality, and
    census escape for odd \(1^3\,2^{m-1}\) involution bundles.

### Decisive-step audits

- **No hidden pair factor.** The quantities \(i_p,f_p,\ell_p\) are
  unweighted pair costs and are divided by exactly one \(c_q\). Equation
  (1.6) makes \(i_p=(d_p-1-b_p)_+\) with no factor two.
- **No false two-sided spill bound.** Both spill sums lie in
  \([0,qs_K]\), so their difference is at most \(qs_K\), not
  \(2qs_K\). Divisibility by \(q+1\) gives (3.6).
- **No bridge rounding debt.** After hyperplane rounding, contracted
  non-bridge components form a forest under the bridge edges. Recursive
  whole-component flips satisfy every bridge without altering any
  non-bridge edge status.
- **No parity claim for odd \(m\).** The slice obstruction uses even \(m\)
  essentially. The stronger three-fixed class is introduced only there.
- **No fixed-target transitivity error.** In Theorem 7.1,
  \(r\le m-1\) ensures at least three points remain after cross-pairing;
  exactly three fixed points can therefore be placed with the required
  parities.
- **No degree-one spectral import.** The three-fixed class has
  \(\rho_1=1/m>1/n\). The \(1/n\) claim is made only for degrees
  \(j\ge2\), and exact centered loads have no degree-one component.
- **No abstract model promoted to a wreath.** The example after Theorem 2.1
  is used only to audit the max surrogate. The genuine obstruction is
  Theorems 6.1--6.3, which uses literal exact factors.

### Unproved and not claimed

1. Z5 equation (8.6).
2. The revised coherence gate \((R_A^{\rm coh})\).
3. A bound of \(O_A(HB)\) for synchronization, cyclic support, spill
   oscillation, or their sum on an adaptive involution.
4. The high-slice lower bound (6.10).
5. A genuine high-corridor wreath counterexample to (8.6).
6. Connectivity or low slice minima for either raw-unbundled or
   three-fixed-involution moves.
7. MWB, labelled common-owner synchronization, constant one, or a literal
   contiguous-OR construction.

The exact proved/conditional boundary is therefore:

\[
\boxed{
\text{actual bundled descent is controlled by distributed coherence and
cyclic holonomy, not by untrimmed fragmentation or tree mass};}
\]

\[
\boxed{
\text{the original }1\,2^m\text{ bundled family has }\Theta(B)
\text{ genuine simultaneous parity-slice traps for even }m;}
\]

\[
\boxed{
\text{proving (8.6) requires }O_A(HB)\text{ minima in every such slice,
or a stronger move family must cross them}.}
\]

The odd three-fixed involution family supplies one explicit positive,
non-Graver way to leave a noncentral parity slice while retaining the exact
pair formalism. No crossing statement is proved from the central slice
\(N_-=B/2\), and restitution for the enlarged family remains open.
