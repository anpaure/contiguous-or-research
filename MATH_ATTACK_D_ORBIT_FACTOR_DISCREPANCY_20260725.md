# Attack D: orbit-factor discrepancy and exact reblocking

Date: 2026-07-25

Method: pure mathematics only. No finite search, solver, or web search is
used.

## 0. Verdict

This route does not presently prove MWB, labelled synchronization, or the
contiguous-OR conjecture.

It does give one exact invariant obstruction and two restricted positive
theorems.

1. The permutation-indexed multicover of all coordinate relabelings of an
   exact factor is independent of the factor that generated it. Therefore,
   for every relabeling-invariant notion of Catalan-goodness,

   \[
   \boxed{
   \begin{array}{c}
   \text{the orbit multicover can be decomposed entirely into}\\
   \text{Catalan-good exact factor blocks}
   \end{array}
   \iff
   \text{one Catalan-good exact factor exists}.}
   \tag{0.1}
   \]

   Thus unrestricted orbit reblocking is exactly the original one-factor
   problem. Perfect balance of the orbit barycenter supplies no additional
   discrepancy leverage.

2. There is nevertheless a genuine exact-factor discrepancy theorem inside
   the ownership-component cube of two colored factors. For one common
   component signing at every depth, the mean and variance of the
   floor-subtracted collision excess have closed formulas. If the component
   means are Catalan-small and their aggregate Rademacher coherence is
   sub-Catalan, one signing gives Catalan error simultaneously at every
   depth. Taking the full coordinate orbit of that signed factor then
   reblocks the original orbit multicover entirely into good exact factors.

3. A deterministic antipodal-component theorem locally replaces two
   colored factor blocks by two exact blocks. If all but
   \(O(\operatorname{Cat}_m/n)\) wreaths per side occur in simultaneous
   opposite-effect component pairs and the pair midpoint is Catalan-close
   to a balanced quota, both output factors have Catalan overload at every
   depth.

The smallest method-specific missing statement is now explicit: produce one
actual orbit pair whose genuine ownership components satisfy the Catalan
mean and sub-Catalan aggregate-coherence estimates of Theorem 8.2. Generic
Steinitz or Banaszczyk balancing of whole orbit factors does not establish
this, because its blocks are multifactor covers rather than single exact
factors.

## 1. Exact model and the Catalan target

Put

\[
n=2m+1,\qquad
W=\binom{n}{m},\qquad
B=\operatorname{Cat}_m=\frac Wn.
\tag{1.1}
\]

Let \(\Omega_m\) be the set of unoriented cyclic orders on \([n]\), with
rotation and reversal identified. For \(C\in\Omega_m\), let
\(\mathcal W_r(C)\) be its \(n\) cyclic intervals of size \(r\), and write

\[
\ell_{r,C}\in\{0,1\}^{\binom{[n]}r}
\tag{1.2}
\]

for their incidence vector.

An exact middle wreath factor is a set \(F\subseteq\Omega_m\) such that

\[
\sum_{C\in F}\ell_{m,C}=\mathbf1_{\binom{[n]}m}.
\tag{1.3}
\]

Summing (1.3) over the middle layer gives

\[
n|F|=W,
\qquad
|F|=B.
\tag{1.4}
\]

At depth \(q\), put

\[
r=m-q,\qquad
N_q=\binom nr,\qquad
\lambda_q=\frac W{N_q},\qquad
c_q=\lfloor\lambda_q\rfloor,
\tag{1.5}
\]

and define the lower load of \(F\) by

\[
\mu_q^F=\sum_{C\in F}\ell_{m-q,C}.
\tag{1.6}
\]

Every cyclic order contributes \(n\) intervals, so

\[
\sum_S\mu_q^F(S)=nB=W.
\tag{1.7}
\]

Write

\[
W=c_qN_q+s_q,\qquad0\le s_q<N_q,
\tag{1.8}
\]

and let \(\mathcal B_q\) be the set of all vectors

\[
b\in\{c_q,c_q+1\}^{N_q},
\qquad
\sum_Sb(S)=W.
\tag{1.9}
\]

The balanced-quota overload distance is

\[
O_q(F)
=
\min_{b\in\mathcal B_q}
\sum_S(\mu_q^F(S)-b(S))_+
=
\frac12\min_{b\in\mathcal B_q}
\|\mu_q^F-b\|_1.
\tag{1.10}
\]

The equality follows because \(\mu_q^F\) and every \(b\in\mathcal B_q\)
have the same total mass.

To identify (1.10) with the standard overload ledger, put

\[
D_q^-=\sum_S(c_q-\mu_q^F(S))_+,
\qquad
D_q^+=\sum_S(\mu_q^F(S)-c_q-1)_+.
\tag{1.11}
\]

If

\[
h_q=|\{S:\mu_q^F(S)\ge c_q+1\}|,
\]

then summing \(\mu_q^F-c_q\) gives

\[
s_q=h_q+D_q^+-D_q^-.
\tag{1.12}
\]

If \(h_q\ge s_q\), place the \(s_q\) high quotas on overloaded cells; the
minimum positive transport is \(D_q^-\). If \(h_q<s_q\), place high quotas
on all \(h_q\) such cells and arbitrarily on another \(s_q-h_q\) cells; the
minimum positive transport is \(D_q^+\). Equation (1.12) shows that the
larger of \(D_q^-,D_q^+\) is the applicable value in the two cases. Hence

\[
\boxed{O_q(F)=\max\{D_q^-,D_q^+\}.}
\tag{1.13}
\]

The collision excess, with the half-energy convention, is

\[
\begin{aligned}
Q_q(F)
&=
\sum_S\binom{\mu_q^F(S)}2
-
\left(
N_q\binom{c_q}2+s_qc_q
\right)\\
&=
\frac12\left(
\|\mu_q^F-\lambda_q\mathbf1\|_2^2
-
\phi_q
\right),
\end{aligned}
\tag{1.14}
\]

where

\[
\phi_q=\frac{s_q(N_q-s_q)}{N_q}.
\tag{1.15}
\]

The floor/ceiling histogram minimizes both collisions and squared distance
among integer histograms of mass \(W\). Hence \(Q_q(F)\ge0\). The elementary
integer inequality

\[
\frac12d(d-1)\ge(-d)_+ +(d-1)_+
\qquad(d\in\mathbb Z)
\tag{1.16}
\]

also gives, after summing over \(S\),

\[
Q_q(F)\ge D_q^-+D_q^+\ge O_q(F).
\tag{1.17}
\]

For a fixed \(A>0\), put

\[
K_A=\lceil A\sqrt m\rceil.
\tag{1.18}
\]

The meaningful Catalan per-depth target is

\[
O_q(F)=O_A(B)
\quad\text{or the stronger}\quad
Q_q(F)=O_A(B)
\qquad(1\le q\le K_A).
\tag{1.19}
\]

Indeed, since \(c_q\ge1\),

\[
\sum_{q=1}^{K_A}\frac{O_q(F)}{c_q}
=O_A(K_AB)
=O_A\left(\frac W{\sqrt m}\right)
=o(W).
\tag{1.20}
\]

Thus (1.19) proves the fixed-window unlabelled overload theorem. It does not
by itself produce one common labelled nested resolution.

## 2. The full-orbit erasure theorem

Let \(G=S_n\) act on \(\Omega_m\) by coordinate relabeling. For an exact
factor \(F\), retain all permutation indices, including repetitions, and
form the wreath-copy multiset

\[
\mathcal U(F)
=
\biguplus_{\sigma\in G}\sigma F.
\tag{2.1}
\]

Equivalently, its multiplicity vector is

\[
u_F=\sum_{\sigma\in G}\mathbf1_{\sigma F}
\in\mathbb Z_{\ge0}^{\Omega_m}.
\tag{2.2}
\]

### Theorem 2.1 (full-orbit erasure)

For every exact factor \(F\),

\[
\boxed{u_F=2W\,\mathbf1_{\Omega_m}.}
\tag{2.3}
\]

In particular, \(\mathcal U(F)\) is independent of \(F\).

Under the oriented-mod-rotation convention the corresponding coefficient
is \(W\); every conclusion below is unchanged.

### Proof

The \(S_n\)-action on unoriented cyclic orders is transitive. The stabilizer
of one order is its dihedral group and has size \(2n\). Fix
\(C,D\in\Omega_m\). Exactly \(2n\) coordinate permutations send \(D\) to
\(C\). Therefore

\[
u_F(C)
=
\sum_{D\in F}
|\{\sigma:\sigma D=C\}|
=2n|F|
=2nB
=2W.
\]

This proves (2.3). \(\square\)

The same multicover is exactly balanced at every lower depth:

\[
\boxed{
\sum_{\sigma\in S_n}\mu_q^{\sigma F}
=
n!\lambda_q\,\mathbf1_{\binom{[n]}{m-q}}.
}
\tag{2.4}
\]

Indeed, the left side is coordinate-invariant and hence constant; its total
mass is \(n!W\), giving (2.4).

At the middle layer, every set is covered once by every orbit factor, so
\(\mathcal U(F)\) is an \(n!\)-fold exact middle cover. Consequently every
decomposition of \(\mathcal U(F)\) into exact factors has exactly \(n!\)
blocks.

## 3. Universal exact-reblocking equivalence

An exact-factor decomposition of \(\mathcal U(F)\) is a multiset

\[
\mathscr D=(F_1,\ldots,F_{n!})
\tag{3.1}
\]

of exact factors such that, as uncolored wreath-copy multisets,

\[
\sum_{i=1}^{n!}\mathbf1_{F_i}=u_F.
\tag{3.2}
\]

Identical wreath copies may be bijected between the old and new color
classes. No wreath is discarded or fractionally divided.

### Theorem 3.1 (orbit-reblocking equivalence)

Let \(\mathcal P\) be any property of exact factors invariant under
coordinate relabeling. The following are equivalent.

1. Some exact factor has property \(\mathcal P\).
2. For every exact factor \(F\), the multicover \(\mathcal U(F)\) has an
   exact-factor decomposition all of whose blocks have \(\mathcal P\).
3. For some exact factor \(F\), an exact-factor decomposition of
   \(\mathcal U(F)\) contains one block with \(\mathcal P\).

### Proof

The implication \(2\Rightarrow3\Rightarrow1\) is immediate. Conversely,
let \(H\) be an exact factor with \(\mathcal P\). By Theorem 2.1,

\[
\mathcal U(F)=\mathcal U(H)
=\biguplus_{\sigma\in S_n}\sigma H.
\tag{3.3}
\]

Every block \(\sigma H\) is exact and has \(\mathcal P\). This proves
\(1\Rightarrow2\). \(\square\)

The theorem applies simultaneously to coordinate-invariant threshold
conditions on all \(O_q\), all \(Q_q\), and weighted sums of them. It also
applies to minimized labelled costs after passing to the
orientation-decorated atom convention, in which the owner deletion
direction is part of the atom data and the full-orbit coefficient is \(W\).

### Corollary 3.2 (optimization identity)

Let \(\Phi\) be any relabeling-invariant real functional on exact factors.
Then

\[
\boxed{
\min_{\mathscr D}
\max_{J\in\mathscr D}\Phi(J)
=
\min_{H\text{ exact}}\Phi(H),
}
\tag{3.4}
\]

and

\[
\boxed{
\min_{\mathscr D}
\frac1{n!}\sum_{J\in\mathscr D}\Phi(J)
=
\min_{H\text{ exact}}\Phi(H).
}
\tag{3.5}
\]

### Proof

Every block in every decomposition is an exact factor, so both left sides
are at least the right side. Take the orbit decomposition of a minimizing
factor \(H\); every block then has value \(\Phi(H)\). \(\square\)

Equations (3.4)--(3.5) are the invariant obstruction. A theorem deriving a
Catalan-good exact-factor decomposition from the balanced full orbit is
neither weaker nor more general than a theorem producing one Catalan-good
factor.

This is not a counterexample to Catalan-good factors. It says that full
orbit balance, considered without its intermediate colored trade structure,
cannot distinguish a good factor from a bad one.

## 4. Complete subgroup orbit-profile invariant

The full symmetric group erases every factor profile because it is
transitive on \(\Omega_m\). For a restricted family of coordinate frames,
an exact profile survives.

Let \(\Gamma\le S_n\), and put

\[
\mathcal U_\Gamma(F)=\biguplus_{\gamma\in\Gamma}\gamma F.
\tag{4.1}
\]

### Theorem 4.1 (subgroup profile)

For a \(\Gamma\)-orbit \(\mathcal O\subseteq\Omega_m\) and
\(C\in\mathcal O\),

\[
\boxed{
\operatorname{mult}_C\mathcal U_\Gamma(F)
=
|\Gamma_C|\,|F\cap\mathcal O|.
}
\tag{4.2}
\]

Consequently,

\[
\boxed{
\mathcal U_\Gamma(F)=\mathcal U_\Gamma(H)
\iff
|F\cap\mathcal O|=|H\cap\mathcal O|
\text{ for every }\Gamma\text{-orbit }\mathcal O.
}
\tag{4.3}
\]

### Proof

Fix \(D,C\in\mathcal O\). The set of \(\gamma\in\Gamma\) with
\(\gamma D=C\) is a coset of \(\Gamma_D\), and all stabilizers in
\(\mathcal O\) have the same order. Thus every \(D\in F\cap\mathcal O\)
contributes exactly \(|\Gamma_C|\) copies of \(C\), proving (4.2).
Equality of the multicover multiplicities on every orbit is then
equivalent to equality of the orbit counts, proving (4.3). \(\square\)

This is both a restricted positive theorem and a complete obstruction for
**single-orbit subgroup reblocking**:

\[
\{\gamma F:\gamma\in\Gamma\}
\longrightarrow
\{\gamma H:\gamma\in\Gamma\}.
\tag{4.4}
\]

Finding a good exact factor with the same subgroup orbit-count profile
gives such a legal reblocking, and (4.3) shows that every such
single-orbit replacement preserves the profile.

For an arbitrary exact-factor decomposition

\[
\mathcal U_\Gamma(F)
=
\biguplus_{j=1}^{|\Gamma|}H_j,
\]

only the aggregate identity

\[
\boxed{
\sum_{j=1}^{|\Gamma|}
|H_j\cap\mathcal O|
=
|\Gamma|\,|F\cap\mathcal O|
}
\tag{4.5}
\]

is forced for every \(\Gamma\)-orbit \(\mathcal O\). Individual blocks need
not have the profile of \(F\).

For example, use oriented cyclic orders modulo rotation and
\(\Gamma=A_n\). Because \(n\) is odd, the cyclic stabilizer consists of
even permutations, so the \(S_n\)-orbit splits into two \(A_n\)-orbits
\(\Omega^+,\Omega^-\). The chirality

\[
h(F)=|F\cap\Omega^+|-|F\cap\Omega^-|
\tag{4.6}
\]

is preserved blockwise by a single-orbit \(A_n\)-reblocking and changes
sign under every odd coordinate permutation. Under an arbitrary exact
reblocking, only total chirality is preserved:

\[
\sum_jh(H_j)=|A_n|h(F).
\tag{4.7}
\]

If \(B\) is odd, then \(h(F)\equiv B\pmod2\), so \(h(F)\ne0\), and no odd
permutation stabilizes \(F\).

This chirality statement requires fixed oriented decorations. If reversal
is identified or may be changed freely, the \(A_n\)-orbit structure changes
and (4.6) need not be an invariant.

## 5. Why whole-factor Steinitz balancing does not descend

Let \(x_F\in\{0,1\}^{\Omega_m}\) be the wreath-incidence vector of an exact
factor.

### Lemma 5.1 (zero-one barycentric rigidity)

If

\[
x_H=\sum_{i=1}^t\alpha_i x_{F_i},
\qquad
\alpha_i>0,\qquad
\sum_i\alpha_i=1,
\tag{5.1}
\]

and \(H,F_i\) are exact factors, then

\[
F_i=H\qquad(1\le i\le t).
\tag{5.2}
\]

### Proof

For a coordinate \(C\in H\), the left side of (5.1) is one. It is a convex
combination of zero-one numbers, so every \(x_{F_i}(C)=1\). For
\(C\notin H\), the same argument at value zero gives
\(x_{F_i}(C)=0\). Thus every incidence vector equals \(x_H\). \(\square\)

Hence the average of several whole exact factors cannot itself be a new
exact factor. It can only be a fractional factor or a multifactor cover.
Any rounding back to one factor is precisely the missing integral fibre
problem.

There is also an exact variance ledger. Stack any chosen collection of
lower-load deviations through a coordinate-equivariant map \(L\) into a
Hilbert space whose norm is coordinate-invariant, and write

\[
z_\sigma=L(\sigma F)-\overline L,
\qquad
\overline L=\frac1{|G|}\sum_{\sigma\in G}L(\sigma F).
\tag{5.3}
\]

Then

\[
\sum_{\sigma\in G}z_\sigma=0,
\qquad
\|z_\sigma\|=R
\tag{5.4}
\]

for a common \(R\). Therefore

\[
\frac1{|G|(|G|-1)}
\sum_{\sigma\ne\tau}
\langle z_\sigma,z_\tau\rangle
=-\frac{R^2}{|G|-1}.
\tag{5.5}
\]

For every subset \(I\subseteq G\), with

\[
\bar z_I=\frac1{|I|}\sum_{\sigma\in I}z_\sigma,
\]

one has

\[
\boxed{
\sum_{\sigma\in I}\|z_\sigma-\bar z_I\|^2
=
|I|\bigl(R^2-\|\bar z_I\|^2\bigr).
}
\tag{5.6}
\]

Thus a small block average hides almost all singleton discrepancy as
within-block variance.

Finally, for any ordering \(\sigma_1,\ldots,\sigma_{|G|}\) and partial sums

\[
S_j=\sum_{i=1}^jz_{\sigma_i},
\]

\[
\boxed{\max_{1\le j\le|G|}\|S_j\|\ge\|S_1\|=R.}
\tag{5.7}
\]

Steinitz ordering can control sums of many factor vectors; Banaszczyk
signing can control signed multifactor differences. But a group containing
\(t>1\) orbit factors is an exact \(t\)-fold cover, not one exact factor,
and a singleton group retains the original orbit discrepancy. Lemma 5.1
rules out replacing a group by its barycenter. A support-feasible
wreath-level recoloring is indispensable.

## 6. Quantization and the one-design lattice

A Catalan raw centered-\(\ell_2^2\) target is impossible even for an
arbitrary integer histogram, before exact-factor constraints are imposed.

### Theorem 6.1 (quantization-floor obstruction)

Fix \(A>0\). There is \(x\in(0,A)\) and a sequence

\[
q_m=x\sqrt m+O(1)
\tag{6.1}
\]

such that every integer vector
\(\nu\in\mathbb Z_{\ge0}^{N_{q_m}}\) with total mass \(W\) satisfies

\[
\boxed{
\left\|\nu-\lambda_{q_m}\mathbf1\right\|_2^2
\ge\kappa_AW
}
\tag{6.2}
\]

for some \(\kappa_A>0\) and all sufficiently large \(m\).

In particular, the left side cannot be \(O_A(B)\).

### Proof

Choose \(x\in(0,A)\) such that \(e^{x^2}\notin\mathbb Z\). The fixed-window
expansion gives

\[
\lambda_{q_m}
=
\exp\left(\frac{q_m(q_m+1)}m+O_A(m^{-1/2})\right)
\longrightarrow e^{x^2}.
\tag{6.3}
\]

Write \(e^{x^2}=c+\theta\), where \(c\in\mathbb Z_{\ge1}\) and
\(0<\theta<1\). Among integer vectors of total \(W\), squared distance from
the constant mean is minimized by a floor/ceiling vector. Hence

\[
\left\|\nu-\lambda_{q_m}\mathbf1\right\|_2^2
\ge
\frac{s_{q_m}(N_{q_m}-s_{q_m})}{N_{q_m}}.
\tag{6.4}
\]

Now \(N_{q_m}\sim e^{-x^2}W\) and
\(s_{q_m}/N_{q_m}\to\theta\). The right side of (6.4) is therefore

\[
\left(e^{-x^2}\theta(1-\theta)+o(1)\right)W,
\]

which proves (6.2). Since \(B=W/n=o(W)\), the Catalan raw-energy target is
impossible. \(\square\)

For the concrete choice

\[
x=\sqrt{\log(3/2)},
\tag{6.5}
\]

when it lies in the chosen window, the lower bound is

\[
\left(\frac16+o(1)\right)W.
\tag{6.6}
\]

This is why the meaningful quadratic quantity is the excess \(Q_q\) after
subtracting \(\phi_q\), not the raw norm.

Exact factors satisfy an additional one-design lattice constraint. Put
\(r=m-q\). Every point belongs to exactly \(r\) cyclic \(r\)-intervals of
one cyclic order, so

\[
\sum_{S\ni i}\mu_q^F(S)=rB
\qquad(i\in[n]).
\tag{6.7}
\]

If a floor/ceiling histogram has the form

\[
\mu_q^F=c_q\mathbf1+\mathbf1_{\mathcal H},
\tag{6.8}
\]

then its high-cell family must be regular:

\[
\boxed{
\deg_{\mathcal H}(i)
=
\frac{r\,s_q}{n}
\qquad(i\in[n]).
}
\tag{6.9}
\]

Indeed,

\[
c_q\binom{n-1}{r-1}+\deg_{\mathcal H}(i)=rB,
\]

and using \(W=c_qN_q+s_q\) gives (6.9). Arbitrary coordinatewise vector
rounding need not respect this exact design lattice.

## 7. The legal two-factor signing domain

Let \(F,G\) be two colored exact factors. Form their ownership overlay:

* left vertices are the colored wreaths of \(F\);
* right vertices are the colored wreaths of \(G\);
* every middle set gives one edge joining its unique two owners.

Every vertex has degree \(n\). In each connected component \(K\), the two
sides have the same number \(s_K\) of wreaths.

### Lemma 7.1 (two-factor component cube)

Every exact factor supported on the colored union \(F\sqcup G\) is obtained
by choosing, independently in every ownership component, its complete
\(F\)-side or its complete \(G\)-side.

The complementary side choices form a second exact factor, so every
component signing replaces the two input colors by two literal exact
factors and uses every colored wreath occurrence exactly once.

### Proof

Let \(x_C,y_D\in\{0,1\}\) indicate selection of a left or right wreath. On
the ownership edge for a middle set, exact coverage gives

\[
x_C+y_D=1.
\tag{7.1}
\]

Along every two-edge path all left variables agree, and all right variables
are their complements. Connectivity leaves one binary choice per component.
Conversely, choosing one complete side in every component covers each
ownership edge exactly once. Taking the opposite choices gives the
complementary factor. \(\square\)

For every component \(K\), depth \(q\), and target \(S\), let

\[
u_{K,q}(S)
=
\#\{C\in F\cap K:S\in\mathcal W_{m-q}(C)\},
\]

\[
v_{K,q}(S)
=
\#\{C\in G\cap K:S\in\mathcal W_{m-q}(C)\},
\]

and put

\[
\Delta_{K,q}=u_{K,q}-v_{K,q}.
\tag{7.2}
\]

If \(\varepsilon_K=+1\) selects the \(F\)-side and
\(\varepsilon_K=-1\) the \(G\)-side, Lemma 7.1 gives the exact identity

\[
\boxed{
\mu_q^{H_\varepsilon}
=
\frac{\mu_q^F+\mu_q^G}{2}
+
\frac12\sum_K\varepsilon_K\Delta_{K,q}.
}
\tag{7.3}
\]

The same signs occur at every depth. Moreover,

\[
\|\Delta_{K,q}\|_1\le2ns_K,
\qquad
\|\Delta_{K,q}\|_\infty\le s_K,
\qquad
\|\Delta_{K,q}\|_2^2\le2ns_K^2.
\tag{7.4}
\]

The first bound uses
\(\|u_{K,q}\|_1=\|v_{K,q}\|_1=ns_K\); the other two follow immediately.

Lemma 7.1 is the exact domain in which discrepancy signs preserve
factorhood. Arbitrary signs on wreaths, targets, depths, or three-factor
supports are not justified by this lemma.

## 8. Exact simultaneous component-discrepancy theorem

Fix \(F,G\), and abbreviate

\[
a_q
=
\frac{\mu_q^F+\mu_q^G}{2}
-
\lambda_q\mathbf1,
\qquad
d_{K,q}=\Delta_{K,q}.
\tag{8.1}
\]

For uniformly independent Rademacher component signs, define

\[
M_q
=
\frac12\left(
\|a_q\|_2^2
+
\frac14\sum_K\|d_{K,q}\|_2^2
-
\phi_q
\right),
\tag{8.2}
\]

and

\[
V_q
=
\frac14\sum_K\langle a_q,d_{K,q}\rangle^2
+
\frac1{16}\sum_{K<L}
\langle d_{K,q},d_{L,q}\rangle^2.
\tag{8.3}
\]

### Lemma 8.1 (exact Rademacher ledger)

For the exact factor \(H_\varepsilon\) of Lemma 7.1,

\[
\boxed{\mathbb E_\varepsilon Q_q(H_\varepsilon)=M_q,}
\tag{8.4}
\]

\[
\boxed{\operatorname{Var}_\varepsilon Q_q(H_\varepsilon)=V_q.}
\tag{8.5}
\]

### Proof

By (7.3),

\[
\mu_q^{H_\varepsilon}-\lambda_q\mathbf1
=
a_q+\frac12\sum_K\varepsilon_Kd_{K,q}.
\tag{8.6}
\]

Taking the expected squared norm and using
\(\mathbb E\varepsilon_K\varepsilon_L=0\) for \(K\ne L\) gives (8.4).

More precisely, expansion of (1.14) and (8.6) gives the Rademacher-Walsh
decomposition

\[
\begin{aligned}
Q_q(H_\varepsilon)-M_q
&=
\frac12\sum_K
\varepsilon_K\langle a_q,d_{K,q}\rangle\\
&\quad+
\frac14\sum_{K<L}
\varepsilon_K\varepsilon_L
\langle d_{K,q},d_{L,q}\rangle.
\end{aligned}
\tag{8.7}
\]

Distinct degree-one and degree-two Rademacher characters are orthogonal.
Squaring (8.7) and taking expectation proves (8.5). \(\square\)

### Theorem 8.2 (restricted simultaneous exact-factor rebalancing)

Let \(t_q>0\) for \(1\le q\le K_A\). If

\[
\boxed{
\sum_{q=1}^{K_A}\frac{V_q}{t_q^2}<1,
}
\tag{8.8}
\]

then one common component signing produces a literal exact factor
\(H_\varepsilon\) satisfying

\[
\boxed{
|Q_q(H_\varepsilon)-M_q|<t_q
\qquad(1\le q\le K_A).
}
\tag{8.9}
\]

If \(G=\sigma F\) is an orbit factor, the original full orbit multicover
\(\mathcal U(F)\) consequently has a decomposition into exact factors all
obeying (8.9).

### Proof

Consider the nonnegative potential

\[
\mathcal P(\varepsilon)
=
\sum_{q=1}^{K_A}
\frac{(Q_q(H_\varepsilon)-M_q)^2}{t_q^2}.
\tag{8.10}
\]

Lemmas 8.1 and linearity of expectation give

\[
\mathbb E\mathcal P
=
\sum_{q=1}^{K_A}\frac{V_q}{t_q^2}<1.
\]

Hence some signing has \(\mathcal P(\varepsilon)<1\). Every summand is
nonnegative, so each is below one, proving (8.9). Lemma 7.1 makes
\(H_\varepsilon\) one exact factor.

If \(G=\sigma F\), then Theorem 2.1 gives

\[
\mathcal U(F)=\mathcal U(H_\varepsilon).
\]

The orbit decomposition
\(\biguplus_{\tau\in S_n}\tau H_\varepsilon\) consists of exact factors.
Since \(Q_q\) is relabeling-invariant, every block obeys (8.9).
\(\square\)

### Corollary 8.3 (Catalan certificate)

Suppose an actual orbit pair \(F,\sigma F\) has

\[
M_q\le C_A B
\qquad(1\le q\le K_A)
\tag{8.11}
\]

and

\[
\sum_{q=1}^{K_A}V_q=o(B^2).
\tag{8.12}
\]

Then, for all sufficiently large \(m\), the original full orbit multicover
has an exact-factor decomposition every block \(H\) of which satisfies

\[
\boxed{
Q_q(H)\le(C_A+1)B
\qquad(1\le q\le K_A).
}
\tag{8.13}
\]

Thus every block has Catalan per-depth overload and proves the fixed-window
unlabelled overload theorem.

### Proof

Take \(t_q=B\) in Theorem 8.2. Condition (8.12) implies (8.8) for all
sufficiently large \(m\), and (8.11) plus (8.9) gives (8.13). Finally use
\(O_q\le Q_q\) from (1.17) and then (1.20). \(\square\)

The exact contrapositive is also useful. Fix one actual orbit pair and its
pair-dependent values \(M_q\). If no exact factor satisfies
\(Q_q\le M_q+t_q\) at every depth, then that pair obeys

\[
\boxed{
\sum_{q=1}^{K_A}\frac{V_q}{t_q^2}\ge1.
}
\tag{8.14}
\]

Thus failure of the restricted theorem forces a quantitative aggregate
component-coherence obstruction. It is not enough to say merely that
partial coloring failed.

The elementary independent-sign mean is still expensive in general. From
(7.4),

\[
\frac18\sum_K\|\Delta_{K,q}\|_2^2
\le
\frac n4\sum_Ks_K^2.
\tag{8.15}
\]

In the all-singleton case, \(\sum_Ks_K^2=B\), so the right side is already
of factor order \(W\), while \(B=W/n\). Therefore component-size bounds
alone miss the Catalan scale by a factor \(n\); cancellation of actual
component effects is essential. This is a limitation of the elementary
estimate, not an impossibility theorem for correlated component signs.

## 9. Deterministic antipodal-component rebalancing

The next theorem is a stronger local conclusion under a more structured
hypothesis: both colors, not just one globally re-orbited factor, become
good.

Let \(\mathscr K\) be the ownership components of \(F\sqcup G\). Choose
\(\mathscr R\subseteq\mathscr K\), and suppose
\(\mathscr K\setminus\mathscr R\) has a fixed-point-free involution
\(K\mapsto K^*\) such that

\[
\boxed{
\Delta_{K^*,q}=-\Delta_{K,q}
\quad\text{for every }q\le K_A.
}
\tag{9.1}
\]

The pairing is simultaneous across all depths.

Put

\[
S_{\mathscr R}=\sum_{K\in\mathscr R}s_K,
\qquad
\bar\mu_q=\frac{\mu_q^F+\mu_q^G}{2}.
\tag{9.2}
\]

### Theorem 9.1 (antipodal cancellation)

For arbitrary balanced quotas \(b_q\in\mathcal B_q\), there is a
component signing such that the two complementary exact factors
\(H_\varepsilon,H_{-\varepsilon}\) satisfy

\[
\boxed{
O_q(H_{\pm\varepsilon})
\le
\frac12\left(
\|\bar\mu_q-b_q\|_1+nS_{\mathscr R}
\right)
\qquad(1\le q\le K_A).
}
\tag{9.3}
\]

In particular, if

\[
\|\bar\mu_q-b_q\|_1=O_A(B)
\quad(q\le K_A),
\qquad
S_{\mathscr R}=O_A(B/n),
\tag{9.4}
\]

then both output color blocks are exact factors with Catalan per-depth
overload.

If \(\mathscr R=\varnothing\) and every \(\bar\mu_q=b_q\), both output
factors are exactly balanced at every observed depth.

### Proof

Give paired components equal signs:

\[
\varepsilon_{K^*}=\varepsilon_K.
\]

Their effects cancel by (9.1). Give residual components arbitrary signs.
Equation (7.3) becomes

\[
\mu_q^{H_\varepsilon}
=
\bar\mu_q+h_q,
\qquad
h_q=\frac12
\sum_{K\in\mathscr R}\varepsilon_K\Delta_{K,q}.
\tag{9.5}
\]

By (7.4),

\[
\|h_q\|_1
\le
\frac12\sum_{K\in\mathscr R}\|\Delta_{K,q}\|_1
\le nS_{\mathscr R}.
\tag{9.6}
\]

Both \(\mu_q^{H_\varepsilon}\) and \(b_q\) have total \(W\), so transport
to the particular balanced quota \(b_q\) costs

\[
\frac12
\|\mu_q^{H_\varepsilon}-b_q\|_1
\le
\frac12\left(
\|\bar\mu_q-b_q\|_1+nS_{\mathscr R}
\right).
\]

Minimizing over balanced quotas gives (9.3). The complementary factor has
load \(\bar\mu_q-h_q\) and obeys the identical estimate. Exact factorhood
of both colors follows from Lemma 7.1. \(\square\)

The residual scale \(B/n=W/n^2\) is stringent. The theorem proves that this
scale is sufficient for the antipodal-pair method; it does not claim it is
necessary.

## 10. Exact remaining lemma and implication scope

The clean method-specific target exposed by Theorem 8.2 is:

> **PAIR-COHERENCE LEMMA \(\mathrm{PC}_A\) -- UNPROVED.**  
> For every fixed \(A>0\) and all sufficiently large \(m\), there are an
> exact middle wreath factor \(F\) and a coordinate permutation \(\sigma\)
> such that the ownership components of \(F\sqcup\sigma F\) satisfy
> \[
> M_q=O_A(B)\qquad(1\le q\le K_A)
> \]
> and
> \[
> \sum_{q=1}^{K_A}V_q=o(B^2),
> \]
> with \(M_q,V_q\) defined by (8.2)--(8.3).

This lemma is sufficient, exact, and support-feasible. It uses one common
component signing across the entire depth window. It is not claimed to be
necessary or equivalent to MWB.

A more structured alternative is:

> **ANTIPODAL ORBIT-PAIR LEMMA \(\mathrm{AP}_A\) -- UNPROVED.**  
> Find one orbit pair satisfying (9.1) outside components of total side
> size \(O_A(B/n)\), with a pair midpoint satisfying the first estimate in
> (9.4) at every depth.

Either lemma gives an exact factor with Catalan per-depth overload, hence

\[
\sum_{q=1}^{K_A}\frac{O_q}{c_q}
=O_A(K_AB)
=O_A(W/\sqrt m)
=o(W).
\tag{10.1}
\]

Proving this for every fixed \(A\) gives fixed-window overload MWB and the
already-audited diagonal route to the asymptotic contiguous-OR bound.

It does not prove the stronger labelled statement

\[
\sum_{q\le K_A}\frac{e_q(F,P)}{c_q}=o(W),
\]

because no common nested owner resolution \(P\) is constructed here.

The universal reblocking theorem explains why \(\mathrm{PC}_A\) cannot be
deduced merely from the exact barycenter (2.4): the same barycenter is the
full orbit of every exact factor, good or bad. A proof must use genuine
intermediate colored component structure, cyclic chronology, or another
support-feasible exact-factor mechanism.

## 11. Adversarial audit

1. **Permutation-indexed multicover.** Theorems 2.1 and 3.1 use all
   \(\sigma\in S_n\) with multiplicity. The set of distinct orbit factors
   may have a factor-dependent stabilizer and is not substituted silently.

2. **Uncolored reblocking.** Equality
   \(\mathcal U(F)=\mathcal U(H)\) is equality of uncolored wreath-copy
   multisets. It permits identical copies to be reassigned among block
   colors. If source colors or a prescribed sequence of local trades must
   be retained, Theorem 3.1 alone does not supply that stronger conclusion.

3. **Exact blocks throughout.** Every output block in Theorems 3.1, 8.2,
   and 9.1 is one literal exact middle wreath factor. No vector average,
   fractional factor, or independently balanced rank histogram is called a
   factor.

4. **Coordinate-invariant objective.** The universal equivalence applies
   to relabeling-invariant properties such as overload, collision excess,
   or a minimized labelled cost. It does not preserve closeness to one
   externally frozen, non-equivariant quota vector.

5. **Two-factor scope.** Lemma 7.1 characterizes supported factors in the
   colored union of exactly two factors. Three or more colored factors may
   have additional integral circuits and are not characterized here.

6. **Common signs across depth.** The same component sign is used in every
   \(q\)-coordinate of (7.3). No depthwise sign choice is optimized
   independently.

7. **One good color versus two.** Theorem 8.2 guarantees one good signed
   factor; its complementary two-color output need not satisfy the same
   bounds. The full good-block decomposition there uses the uncolored
   universal reblocking theorem. Theorem 9.1, under its stronger antipodal
   hypothesis, makes both local output colors good.

8. **Quantization convention.** Raw centered squared discrepancy has an
   unavoidable \(\Theta_A(W)\) floor at suitable Gaussian depths.
   Catalan-scale quadratic claims concern the collision excess \(Q_q\)
   after subtracting \(\phi_q\). The factor \(1/2\) in (1.14) is retained
   in every mean and variance formula.

9. **One-design lattice.** Coordinate transitivity of the fractional orbit
   does not remove the exact point-margin constraint (6.7). A rounded high
   family must satisfy (6.9).

10. **Independent-sign limitation.** Estimate (8.15) shows only that the
    elementary independent-sign size bound misses Catalan scale. It does
    not rule out correlated partial coloring, entropy methods, or
    wreath-specific cancellation.

11. **No counterexample to MWB.** Full-orbit erasure proves equivalence of
    unrestricted reblocking and one-factor existence; it does not prove
    that a Catalan-good factor is absent. The subgroup chirality invariant
    is likewise not an overload lower bound.

12. **Unlabelled conclusion only.** Catalan overload or collision excess
    proves fixed-window unlabelled MWB. Small unlabelled histogram error is
    not promoted to a nearby common nested labelled flow.

The stable conclusion is that the balanced full orbit is a universal
reservoir, not a rounding certificate. The nontrivial mathematical content
must enter before the final uncolored reblocking, through genuine
ownership-component cancellation or another exact support-feasible
factor-trade theorem.
