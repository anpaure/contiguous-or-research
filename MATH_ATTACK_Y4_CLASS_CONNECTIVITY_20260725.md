# Fourth-wave Y: exact-factor class connectivity by nonlocal Haar packets

## 0. Verdict

Let

\[
n=2m+1,\qquad
W=\binom nm,\qquad
B=\operatorname{Cat}_m=\frac Wn,
\]

and let \(\mathfrak F_m\) be the finite nonempty fibre of exact middle
wreath factors.  Fix \(A>0\).  Throughout the fixed-window statements,
\(m\) is sufficiently large (depending on \(A\)) that

\[
H=H_A=\lceil A\sqrt m\rceil\le m-2.
\]

The exact structural statements through Section 7, and the occurrence-cap
bound in Section 8.1, in fact hold for every \(m\ge2\) and every defined
depth stack \(1\le H\le m-1\).  Statements involving no lower-shadow
profile hold for every \(m\ge2\).  Let \(\mathcal Q_H\) be the full weighted
floor-corrected energy.

The fourth-wave class question has an exact answer after one explicitly
defined nonlocal augmentation.

### Main positive theorem

Adjoin all applicable **Gram-antagonistic comparison-Haar packets**.  Such a
packet is a union of connected old/new ownership circuits whose retained
lower-shadow effects have strictly negative Gram correlation across every
nontrivial cut.  Single connected ownership circuits are included by
definition.

This one family has four exact properties.

1. Every move remains inside the integral exact-factor fibre.

2. The augmented graph is connected, with

   \[
   \boxed{
   \operatorname{diam}\Gamma_{m,H}^{\rm GA}
   \le \left\lfloor\frac{B}{2}\right\rfloor.
   }
   \]

   Under controlled fair binary Haar resampling, any prescribed target is
   hit in expected time at most \(B\).

3. If an exact comparator \(G\) improves \(F\) by

   \[
   g=\mathcal Q_H(F)-\mathcal Q_H(G)>0,
   \]

   then one applicable Gram-antagonistic packet improves \(F\) by at least

   \[
   \boxed{
   \frac{g}{|\mathcal K(F,G)|}
   \ge \frac{g}{\lfloor B/2\rfloor}
   \ge \frac{2g}{B}.
   }
   \]

   This sharpens the previously recorded \(g/B\) comparison constant by a
   factor two.  Repeated comparison with a global minimizer reaches some
   global minimizer in at most \(\lfloor B/2\rfloor\) strict exact moves.
   Replacing each chosen move by its fair binary Haar projector gives an
   almost-sure, pathwise nonincreasing stopping policy with expected hitting
   time at most \(B\).

4. Every Gram-antagonistic packet is a feasible primitive of the augmented
   load matrix

   \[
   \widehat A_H=
   \begin{pmatrix}
   A_m&0\\
   D_H&-I
   \end{pmatrix}.
   \]

   A connected one-component member is already an ordinary
   packing-compatible circuit of \(A_m\); a multicomponent member is an
   ownership-disconnected augmented-Haar macro-packet.  It may in a special
   case coincide with an already legal simultaneous transposition-cell
   signing.  The converse primitivity implication is not proved.

There is also a cardinality-minimal sparse connectivity theorem.  Fix one
canonical exact hub \(F^\circ\).  From every other factor, switch one
canonically selected connected component of its comparison overlay with
\(F^\circ\).  The resulting \(|\mathfrak F_m|-1\) binary Haar edges form a
spanning tree.  Adding only those parent edges not already present in the
original transposition-cell graph makes the augmented chain irreducible.  Thus
the connectivity theorem does not require adjoining every Graver edge,
although the sparse family is still global and oracle-scale.

### Exact energy conclusion

Put

\[
M_{m,H}=\min_{F\in\mathfrak F_m}\mathcal Q_H(F).
\]

The augmented graph has one class, and

\[
\boxed{
\min_{G\in\mathscr C_{\rm aug}(F)}\mathcal Q_H(G)=M_{m,H}
\qquad(F\in\mathfrak F_m).
}
\]

For every real \(L\), the following are equivalent:

\[
\boxed{
M_{m,H}\le L;
}
\]

\[
\boxed{
\text{every }F\text{ with }\mathcal Q_H(F)>L
\text{ has an improving Gram-antagonistic move};
}
\]

\[
\boxed{
\text{every start reaches }\{\mathcal Q_H\le L\}
\text{ in at most }\lfloor B/2\rfloor
\text{ strict augmented moves}.
}
\]

Consequently, for \(H=H_A\), the unique class contains a factor of energy
\(O_A(H_AB)\) if and only if

\[
\boxed{
M_{m,H_A}=O_A(H_AB).
}
\]

This global quadratic fixed-window bound remains **unproved**.  It is a
sufficient route to the frozen unlabelled overload target, but it is
stronger than that target and is not equivalent to MWB.  Connectivity
removes the class obstruction; it cannot bound the value of a cost function
on the resulting single class.

No augmented class invariant survives: nonlinear, parity, modular,
homological, holonomy, and oriented-matroid state invariants are all
constant once the comparison-Haar tree is adjoined.  No new invariant
forcing a positive Catalan-scale energy floor was found.

Every theorem below stays inside literal \(0/1\) exact factors.  No signed
relation, partial packing, or alternating edge cycle is treated as an exact
factor unless its common completion is part of the construction.

---

## 1. Exact factors, loads, and floor energy

Let \(\Omega_m\) be the set of unoriented cyclic orders on \([n]\), modulo
rotation and reversal.  Let

\[
A_m:\mathbb Z^{\Omega_m}\longrightarrow
\mathbb Z^{\binom{[n]}m}
\]

be the middle cyclic-interval incidence map.  The exact factor fibre is

\[
\mathfrak F_m
=
\left\{
x\in\{0,1\}^{\Omega_m}:A_mx=\mathbf1
\right\}.
\tag{Y4.1}
\]

Every factor has exactly \(B=W/n\) wreaths.

For \(1\le q\le H\), put

\[
r_q=m-q,\qquad
N_q=\binom n{r_q},\qquad
\lambda_q=\frac W{N_q}=c_q+\theta_q,
\]

where

\[
c_q=\lfloor\lambda_q\rfloor,\qquad
0\le\theta_q<1.
\]

Let \(B_q\) be the rank-\(r_q\) cyclic-interval incidence map and define

\[
D_Hx=(B_1x,\ldots,B_Hx).
\tag{Y4.2}
\]

For an exact factor \(F\), write

\[
\mu_q^F=B_q\mathbf1_F,\qquad
f_q^F=\mu_q^F-\lambda_q\mathbf1,
\]

and

\[
\beta_q=N_q\theta_q(1-\theta_q).
\]

Every one of the \(B\) wreaths contributes \(n\) rank-\(r_q\) cyclic
intervals, so

\[
\sum_S\mu_q^F(S)=nB=W,
\]

and \(\lambda_q=W/N_q\) is the exact mean load.

Use the weighted inner product

\[
\langle u,v\rangle_H
=\sum_{q=1}^{H}\frac{\langle u_q,v_q\rangle_2}{c_q},
\qquad
\|u\|_H^2=\langle u,u\rangle_H.
\tag{Y4.3}
\]

Put

\[
Q_q(F)
=
\sum_{S\in\binom{[n]}{r_q}}
(\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1)
=\|f_q^F\|_2^2-\beta_q.
\]

The full weighted floor energy is

\[
\begin{aligned}
\mathcal Q_H(F)
&=
\sum_{q=1}^{H}\frac1{c_q}
\sum_{S\in\binom{[n]}{r_q}}
(\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1)\\
&=
\|f^F\|_H^2-\mathfrak B_H,
\end{aligned}
\tag{Y4.4}
\]

where

\[
\mathfrak B_H=\sum_{q=1}^{H}\frac{\beta_q}{c_q}.
\]

Every numerator product

\[
(\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1)
\]

is a nonnegative integer.  After division by \(c_q\), the weighted energy
\(\mathcal Q_H\) is nonnegative but need not be integral.

If \(z\in\ker A_m\) is an applicable exact-factor move and

\[
v=D_Hz,
\]

then every rank block of \(v\) has coordinate sum zero and

\[
\boxed{
\mathcal Q_H(F+z)-\mathcal Q_H(F)
=2\langle f^F,v\rangle_H+\|v\|_H^2.
}
\tag{Y4.5}
\]

This is the full-energy normalization.  The corresponding half energy has
all terms divided by two.

---

## 2. Connected comparison circuits

### 2.1 Reduced packing bitrades

A **reduced packing bitrade** is a vector

\[
z=\mathbf1_P-\mathbf1_N
\tag{Y4.6}
\]

such that:

1. \(P,N\subseteq\Omega_m\) are disjoint;
2. each of \(P,N\) is a middle-wreath packing, so its selected wreaths have
   pairwise disjoint middle interval families; and
3.

   \[
   A_m\mathbf1_P=A_m\mathbf1_N.
   \tag{Y4.7}
   \]

The common vector in (Y4.7) is a \(0/1\) indicator of a set of middle
masks.

The **ownership overlay** \(\Gamma(z)\) is the bipartite multigraph with
vertex classes \(N\) and \(P\).  For each middle mask in the common support,
put one edge between its unique owner in \(N\) and its unique owner in
\(P\).  Every overlay vertex has degree \(n\), because every wreath has
exactly \(n\) middle intervals.  Hence every connected component has equal
numbers of old and new wreaths.

Call \(z\) an **ownership-connected comparison circuit** when
\(\Gamma(z)\) is connected.

### Theorem 2.1: exact applicability and circuit primitivity

Assume \(m\ge2\).  Let \(z=\mathbf1_P-\mathbf1_N\) be a reduced packing
bitrade.

1. If \(N\subseteq F\) for an exact factor \(F\), then

   \[
   F'=(F\setminus N)\,\dot\cup\,P
   \tag{Y4.8}
   \]

   is a literal integral exact factor.

2. If \(\Gamma(z)\) is connected, then

   \[
   \ker_{\mathbb R}
   \left(A_m\big|_{\operatorname{supp}z}\right)
   =\mathbb Rz.
   \tag{Y4.9}
   \]

   Thus \(z\) is a support-minimal linear circuit and a squarefree Graver
   element of \(A_m\).

#### Proof

The residual factor \(F\setminus N\) covers exactly the complement of the
middle support in (Y4.7), and \(P\) covers that support exactly once.
Therefore (Y4.8) covers every middle mask exactly once.  A wreath of \(P\)
cannot already lie in \(F\setminus N\): all its middle masks lie in the
support of \(N\), whereas every residual wreath has middle masks in the
complement.  Hence the union is disjoint and \(F'\) is a \(0/1\) exact
factor.

For the second claim, let \(u\) be any real kernel vector supported on
\(P\cup N\).  The equation at a middle mask whose owners are
\(C\in N\) and \(D\in P\) is

\[
u_C+u_D=0.
\tag{Y4.10}
\]

Along a connected bipartite overlay, (Y4.10) forces one common scalar on
all vertices of \(N\) and its negative on all vertices of \(P\).  Thus
\(u\) is a scalar multiple of \(z\).  This proves (Y4.9), and both circuit
and Graver primitivity follow. \(\square\)

The term “circuit” in this report is therefore literal on
packing-compatible support.  No classification of arbitrary circuits or
the unrestricted Graver basis of \(A_m\) is asserted.

### 2.2 No nontrivial one-for-one component

The middle-incidence column of one wreath determines its unoriented cyclic
order.  Indeed, let \(d_C(a,b)\in\{1,\ldots,m\}\) be the shorter cyclic
distance between two labels in a wreath \(C\).  Exactly

\[
m-d_C(a,b)
\]

middle \(m\)-windows of \(C\) contain both labels.  Hence equality of
middle-incidence columns gives every pairwise cyclic distance.  In
particular, the pairs occurring together \(m-1\) times are exactly the
distance-one pairs, which recover the unoriented cycle.

Consequently, if two wreath columns are equal, the wreaths are equal.

### Lemma 2.2: minimum side size

Every nonzero connected component of a reduced exact-factor comparison
overlay contains at least two old and two new wreaths.

#### Proof

The two side sizes are equal because the component is \(n\)-regular
bipartite.  If each side had size one, its two wreath columns would be
equal.  Column injectivity would make the two wreaths identical, contrary
to cancellation and reducedness. \(\square\)

This elementary lemma is responsible for the factor-two improvement in all
diameter and energy-gap constants below.

---

## 3. The exact comparison-Haar cube

Let \(F,G\in\mathfrak F_m\).  Cancel their common wreaths and form the
ownership overlay between

\[
N=F\setminus G,\qquad P=G\setminus F.
\]

Let its connected components be

\[
K_1,\ldots,K_k.
\]

Write

\[
z_i=\mathbf1_{P_i}-\mathbf1_{N_i},
\qquad
v_i=D_Hz_i.
\tag{Y4.11}
\]

For \(I\subseteq[k]\), put

\[
F_I=F+\sum_{i\in I}z_i.
\tag{Y4.12}
\]

### Theorem 3.1: exact cube and restricted-support classification

Every \(F_I\) is an exact factor.  Moreover, after the common wreaths
\(F\cap G\) are fixed, the exact factors using only columns in \(F\cup G\)
are precisely the \(2^k\) factors \(F_I\).

At the lattice level,

\[
\boxed{
\ker_{\mathbb Z}
\left(
A_m\big|_{(F\triangle G)}
\right)
=\bigoplus_{i=1}^{k}\mathbb Zz_i.
}
\tag{Y4.13}
\]

#### Proof

Each \(z_i\) is an applicable connected comparison circuit, and distinct
components have disjoint middle supports.  Theorem 2.1 proves exactness of
every subset switch.

For (Y4.13), a kernel coefficient vector supported on \(F\triangle G\)
obeys (Y4.10) on every ownership edge.  Its coefficient is therefore
constant, with opposite signs on the two sides, inside each connected
component.  Different components have disjoint row equations, so their
coefficients are independent.

For completeness, let \(H'\) be an exact factor using only columns in
\(F\cup G\).  Every common wreath is forced, because no column of
\(F\triangle G\) meets a middle mask owned by a common wreath.  Thus

\[
y=\mathbf1_{H'}-\mathbf1_F
\]

is supported on \(F\triangle G\), and (Y4.13) writes it uniquely as

\[
y=\sum_i a_i z_i,qquad a_i\in\mathbb Z.
\]

On \(N_i\), the coefficient of \(H'\) is \(1-a_i\), and on \(P_i\) it is
\(a_i\).  Binarity forces \(a_i\in\{0,1\}\).  Hence \(H'=F_I\) for a
unique \(I\subseteq[k]\), proving both the classification and the count
\(2^k\). \(\square\)

Thus every pair of exact factors determines an exact comparison-Haar cube.
Its first Walsh/Haar directions are the connected circuits \(z_i\).

By Lemma 2.2,

\[
\boxed{
k\le
\left\lfloor\frac{|F\setminus G|}{2}\right\rfloor
\le
\left\lfloor\frac B2\right\rfloor.
}
\tag{Y4.14}
\]

### Corollary 3.2: full connected-circuit graph

If every applicable ownership-connected comparison circuit is allowed, then
the exact-factor graph is connected and

\[
\boxed{
d_{\rm circ}(F,G)
\le
\left\lfloor\frac{|F\setminus G|}{2}\right\rfloor
\le\left\lfloor\frac B2\right\rfloor.
}
\tag{Y4.15}
\]

Switching components one at a time gives the path.

This is a fibrewise Markov/test family for the single exact right-hand side
\(A_mx=\mathbf1\).  It is not claimed to be a Markov basis for every
nonnegative right-hand side of \(A_m\).

### 3.1 Binary Haar kernels

For one circuit edge \(e=\{U,V\}\), define \(K_e\) on functions on
\(\mathfrak F_m\) by

\[
(K_eh)(U)=(K_eh)(V)=\frac{h(U)+h(V)}2,
\]

and let \(K_eh=h\) away from \(\{U,V\}\).  Then

\[
K_e^2=K_e,\qquad K_e^*=K_e.
\tag{Y4.16}
\]

It is the two-state Haar projector for that exact circuit.

Under controlled fair resampling, repeat the current binary projector until
the desired endpoint is sampled.  The stage time is geometric of mean two.
Combining this with (Y4.15) gives

\[
\boxed{
\mathbb E_FT_G
\le
2d_{\rm circ}(F,G)
\le |F\setminus G|
\le B.
}
\tag{Y4.17}
\]

This is a controlled chain using the newly adjoined circuit kernels, not the
original transposition heat.

### 3.2 Exact comparison-cube energy ledger

For \(I\subseteq[k]\), (Y4.5) gives

\[
\boxed{
\mathcal Q_H(F_I)-\mathcal Q_H(F)
=
2\left\langle f^F,\sum_{i\in I}v_i\right\rangle_H
+\left\|\sum_{i\in I}v_i\right\|_H^2.
}
\tag{Y4.18}
\]

Let

\[
f_c=\frac{f^F+f^G}{2}.
\]

Writing the cube vertices by signs \(\varepsilon_i\in\{\pm1\}\),

\[
f_\varepsilon
=f_c+\frac12\sum_i\varepsilon_iv_i.
\tag{Y4.19}
\]

Uniform cube averaging gives

\[
\boxed{
\mathbb E_\varepsilon\mathcal Q_H(F_\varepsilon)
=\|f_c\|_H^2
+\frac14\sum_i\|v_i\|_H^2
-\mathfrak B_H.
}
\tag{Y4.20}
\]

The endpoint average is

\[
\boxed{
\frac{\mathcal Q_H(F)+\mathcal Q_H(G)}2
=\|f_c\|_H^2
+\frac14\left\|\sum_iv_i\right\|_H^2
-\mathfrak B_H.
}
\tag{Y4.21}
\]

Therefore

\[
\mathbb E_\varepsilon\mathcal Q_H(F_\varepsilon)
-\frac{\mathcal Q_H(F)+\mathcal Q_H(G)}2
=
\frac14
\left(
\sum_i\|v_i\|_H^2-\left\|\sum_iv_i\right\|_H^2
\right).
\tag{Y4.22}
\]

The right side has no fixed sign.  Also, \(f_c\) need not be orthogonal to
the individual \(v_i\)'s for an arbitrary comparison pair.  Hence there is
no general best-sign formula depending only on
\(\|\sum_i\varepsilon_iv_i\|^2\).  Connectivity and exact cube structure
alone do not supply monotone energy descent.

Along any ordering of the \(k\) component switches, the energy increments
only telescope to

\[
\mathcal Q_H(G)-\mathcal Q_H(F).
\]

If \(G\) is better, at least one step in that ordering improves by at least
\((\mathcal Q_H(F)-\mathcal Q_H(G))/k\), but it may occur only after uphill
preparation.

---

## 4. One explicit augmented family: Gram-antagonistic Haar packets

Let \(z=\mathbf1_P-\mathbf1_N\) be any reduced support-feasible packing
bitrade, not necessarily connected.  Let

\[
\mathcal K(z)=\{K_1,\ldots,K_s\}
\]

be its ownership components, and orient

\[
z_K=\mathbf1_{P_K}-\mathbf1_{N_K},
\qquad
v_K=D_Hz_K.
\tag{Y4.23}
\]

For \(J\subseteq\mathcal K(z)\), put

\[
v_J=\sum_{K\in J}v_K.
\]

### Definition 4.1: Gram-antagonistic packet

A nonempty packet \(J\subseteq\mathcal K(z)\) is
**Gram-antagonistic** when either \(|J|=1\), or

\[
\boxed{
\langle v_I,v_{J\setminus I}\rangle_H<0
\quad
\text{for every }
\varnothing\ne I\subsetneq J.
}
\tag{Y4.24}
\]

Let \(\mathscr{GA}_{m,H}\) be the family of all applicable moves obtained
from Gram-antagonistic packets of all reduced packing bitrades.  This is one
finite, explicitly defined family depending only on \(m,H\).

The family is reversal-closed.  Swapping the two trade sides sends every
\(v_K\) to \(-v_K\), leaves all Gram products in (Y4.24) unchanged, and is
applicable at the switched endpoint.  Hence it defines an undirected exact
switch graph.  Each such macro-edge carries the same two-state Haar
projector (Y4.16), now applied to its two exact endpoints.

Its singleton members are ordinary ownership-connected alternating
circuits.  Its multicomponent members bundle several such circuits because
their lower-shadow effects cancel antagonistically.  These are the nonlocal
augmented-Haar moves.

Every **one-component** switch in a transposition cell is a singleton member
of \(\mathscr{GA}_{m,H}\).  A simultaneous switch of several transposition
components need not itself be Gram-antagonistic, so the augmented graph is
understood to retain all original transposition-cell edges and adjoin the
Gram-antagonistic ones.  Single-component switches generate the same
original communicating classes as arbitrary cell signings.  The new family
is therefore a valid augmentation; strict edge-set enlargement for every
\(m\) is not asserted.

---

## 5. Connectivity, a sparse hub tree, and invariant collapse

### Theorem 5.1: augmented connectivity and diameter

For \(m\ge2\), the graph generated by \(\mathscr{GA}_{m,H}\) alone is
connected, and hence so is its union with the original transposition-cell
graph.  Moreover,

\[
\boxed{
\operatorname{diam}\Gamma_{m,H}^{\rm GA}
\le\left\lfloor\frac B2\right\rfloor.
}
\tag{Y4.25}
\]

Under controlled fair binary resampling of singleton circuit edges,

\[
\boxed{
\mathbb E_FT_G\le B
\qquad(F,G\in\mathfrak F_m).
}
\tag{Y4.26}
\]

#### Proof

Every connected comparison circuit is a singleton Gram-antagonistic packet.
Apply Corollary 3.2 and (Y4.17). \(\square\)

The family is canonical but huge.  It contains factor-scale packets and
quantifies over all support-feasible exact comparisons.  The next theorem
shows that such maximality is not needed merely for connectivity.

Connectivity here is a fibre-completion theorem: the family declares every
support-feasible connected comparison circuit available.  It is not a
connectivity theorem for a bounded circuit template, one \(S_n\)-orbit, or
a permutation-generated library, and it supplies no efficient separation
oracle.

### 5.1 Canonical sparse parent circuits

Fix:

1. one named exact factor \(F^\circ\), for example a canonical MSW factor;
   and
2. a total order on the middle masks.

For \(F\ne F^\circ\), form the reduced \(F/F^\circ\) ownership overlay.
Let \(S(F)\) be the least middle mask whose owners in \(F\) and
\(F^\circ\) differ.  Let \(K(F)\) be the overlay component containing the
edge labelled \(S(F)\).  Define \(p(F)\) by switching precisely \(K(F)\)
toward \(F^\circ\).

Put

\[
\rho(F)=|F\setminus F^\circ|.
\tag{Y4.27}
\]

### Theorem 5.2: cardinality-minimal comparison-Haar tree

The undirected edge set

\[
\mathcal T(F^\circ)
=
\left\{
\{F,p(F)\}:F\in\mathfrak F_m,\ F\ne F^\circ
\right\}
\tag{Y4.28}
\]

is a spanning tree of the exact-factor fibre.  Every edge is an
ownership-connected comparison circuit and hence a singleton member of
\(\mathscr{GA}_{m,H}\).  Moreover,

\[
\boxed{
d_{\mathcal T}(F,F^\circ)
\le
\left\lfloor\frac{\rho(F)}2\right\rfloor
\le\left\lfloor\frac B2\right\rfloor,
}
\tag{Y4.29}
\]

and

\[
\boxed{
\operatorname{diam}\mathcal T(F^\circ)\le B.
}
\tag{Y4.30}
\]

#### Proof

If the selected component has \(s\) old and \(s\) new wreaths, then all new
wreaths lie in \(F^\circ\setminus F\), while all removed wreaths lie in
\(F\setminus F^\circ\).  Therefore

\[
\rho(p(F))=\rho(F)-s.
\tag{Y4.31}
\]

Lemma 2.2 gives \(s\ge2\).  Iterating \(p\) reaches \(F^\circ\) within the
bound (Y4.29).

Orient every edge \(F\to p(F)\).  Along it \(\rho\) strictly decreases, so
the same undirected edge cannot arise from two different children.  Thus
there are exactly \(|\mathfrak F_m|-1\) edges, and every vertex reaches the
hub.  To see undirected acyclicity directly, a vertex of maximal \(\rho\)
on an undirected cycle would have both cycle edges oriented away from it,
contradicting its unique parent edge.  Hence the connected graph is a tree.
Routing through the hub gives

\[
\operatorname{diam}\mathcal T(F^\circ)
\le2\left\lfloor\frac B2\right\rfloor\le B.
\]

This proves (Y4.30). \(\square\)

Among simple edge families that connect all \(|\mathfrak F_m|\) states, the
tree cardinality \(|\mathfrak F_m|-1\) is minimal.

Let \(E_{\rm tr}\) be the original Y3 edge set: \(\{F,G\}\in E_{\rm tr}\)
when \(F,G\) lie in one intrinsic coordinate-transposition cell.  This
allows an arbitrary simultaneous component signing; using only the
one-component edges gives the same communicating classes.  Define the
literally adjoined nonlocal family

\[
\mathcal T_{\rm add}(F^\circ)
=
\mathcal T(F^\circ)\setminus E_{\rm tr}.
\tag{Y4.32}
\]

Then

\[
E_{\rm tr}\cup\mathcal T_{\rm add}(F^\circ)
\]

contains the whole tree and is connected.  Every genuinely added edge is,
by definition, absent from the original transposition chain.

### 5.2 Haar projector and invariant theorem

Choose positive weights \(w_e\) on the tree edges with

\[
\sum_{e\in\mathcal T}w_e=1,
\]

and put

\[
K_{\mathcal T}=\sum_{e\in\mathcal T}w_eK_e.
\tag{Y4.33}
\]

This is a symmetric Markov kernel.  For every real function \(h\) on
\(\mathfrak F_m\),

\[
\boxed{
\langle h,(I-K_{\mathcal T})h\rangle
=
\frac12\sum_{\{U,V\}=e\in\mathcal T}
w_e(h(U)-h(V))^2.
}
\tag{Y4.34}
\]

Hence

\[
\boxed{
\ker(I-K_{\mathcal T})
=\{\text{constant functions on }\mathfrak F_m\}.
}
\tag{Y4.35}
\]

The chain is irreducible and aperiodic and has the uniform law on the whole
exact fibre as its unique stationary distribution.

At the integer-column level, let

\[
\mathcal L_{\mathcal T}
=
\operatorname{span}_{\mathbb Z}
\left\{
\mathbf1_{p(F)}-\mathbf1_F:F\ne F^\circ
\right\}.
\tag{Y4.36}
\]

Telescoping along tree paths gives

\[
\boxed{
\mathcal L_{\mathcal T}
=
\operatorname{span}_{\mathbb Z}
\left\{
\mathbf1_G-\mathbf1_F:F,G\in\mathfrak F_m
\right\}.
}
\tag{Y4.37}
\]

Therefore:

* every additive or modular character annihilating the adjoined circuits is
  constant on the exact fibre;
* every arbitrary state invariant is constant by graph connectivity; and
* odd-graph homology or voltage holonomy can remain only as path
  decomposition data, not as a class-separating \(H^0\) invariant.

This conclusion concerns the augmented graph.  It does not prove that the
original transposition-cell graph was connected.

---

## 6. Odd-graph alternating-cycle interpretation

Under the standard multiplier-two correspondence, the \(n\) middle windows
of one wreath form a \(C_n\) in the odd graph

\[
O_m=KG(2m+1,m).
\]

Explicitly, if

\[
M_i=\{c_i,c_{i+1},\ldots,c_{i+m-1}\}
\qquad(i\bmod n),
\]

then \(M_i\cap M_{i+m}=\varnothing\).  Since
\(\gcd(m,2m+1)=1\), the step \(i\mapsto i+m\) visits all \(n\) windows
and gives the claimed odd-graph cycle.

An exact wreath factor is therefore a spanning \(C_n\)-factor of \(O_m\).

For two exact factors \(F,G\), color their odd-graph edges red and blue.
After common edges are cancelled, each middle-mask vertex has equal red and
blue degree.  The symmetric edge difference decomposes into edge-disjoint
red/blue alternating even closed trails, equivalently alternating Euler
circuits in its balanced pieces.  These circuits need not be simple cycles.

An ownership component from Section 3 is a packet consisting of whole old
wreath \(C_n\)'s and whole new wreath \(C_n\)'s on one common middle-mask
block.  Its odd-graph symmetric difference is consequently a packet of
alternating cycles.  Switching the whole ownership packet is exactly the
legal circuit move of Theorem 2.1.

Switching one constituent alternating closed trail is not automatically
legal.  It preserves 2-factorhood, but the resulting cycles need not all
have length \(n\), so the endpoint need not be a wreath factor.  The
restricted-support theorem (Y4.13) sharpens this:

> Among exact factors using only the old and new wreath columns, a legal
> toggle is necessarily a union of whole ownership components.

A toggle not corresponding to a union of whole ownership components can be
exact only if its resulting wreath decomposition introduces hybrid columns
outside \(F\cup G\).  Thus ordinary edge-cycle generation is a graph or
signed-lattice statement.  Whole ownership-connected packets are the first
level at which exact-factor connectivity is proved.

---

## 7. Gram-antagonistic descent

Let \(F,G\in\mathfrak F_m\) and orient their comparison components
\(K_1,\ldots,K_k\) toward \(G\), with effects \(v_i\) as in (Y4.11).
For \(J\subseteq[k]\), define

\[
\Delta_F(J)
=\mathcal Q_H(F_J)-\mathcal Q_H(F).
\tag{Y4.38}
\]

For a nontrivial cut \(J=I\dot\cup L\), equation (Y4.5) gives the exact mixed
identity

\[
\boxed{
\Delta_F(J)
=\Delta_F(I)+\Delta_F(L)
+2\langle v_I,v_L\rangle_H.
}
\tag{Y4.39}
\]

### Theorem 7.1: comparison descent with the \(2/B\) constant

Suppose

\[
g=\mathcal Q_H(F)-\mathcal Q_H(G)>0.
\]

Then there is an applicable Gram-antagonistic packet
\(J\subseteq[k]\) such that

\[
\boxed{
\mathcal Q_H(F)-\mathcal Q_H(F_J)
\ge
\frac{g}{k}
\ge
\frac{g}{\lfloor B/2\rfloor}
\ge\frac{2g}{B}.
}
\tag{Y4.40}
\]

#### Proof

Start with the full packet \([k]\).  Whenever a current packet \(J\) is not
Gram-antagonistic, choose a nontrivial cut

\[
J=I\dot\cup L
\]

with

\[
\langle v_I,v_L\rangle_H\ge0,
\]

and replace \(J\) by \(I,L\).  The recursion terminates in
Gram-antagonistic leaves \(P_1,\ldots,P_t\), with \(t\le k\).

By (Y4.39), every split satisfies

\[
\Delta_F(J)\ge\Delta_F(I)+\Delta_F(L).
\]

Iteration gives

\[
-g=\Delta_F([k])
\ge\sum_{a=1}^{t}\Delta_F(P_a).
\]

Some leaf therefore has

\[
\Delta_F(P_a)\le-\frac gt\le-\frac gk.
\]

Use (Y4.14) for the remaining inequalities. \(\square\)

### Theorem 7.2: exact local/global and threshold equivalence

Let

\[
M_{m,H}=\min_{F\in\mathfrak F_m}\mathcal Q_H(F).
\tag{Y4.41}
\]

Then:

1.

   \[
   \boxed{
   F\text{ is a global minimizer}
   \iff
   F\text{ has no improving }\mathscr{GA}_{m,H}\text{ move}.
   }
   \tag{Y4.42}
   \]

2. Fix a global minimizer \(G^*\).  Starting from any \(F_0\), repeated
   application of Theorem 7.1 toward the remaining
   \(F_t/G^*\) overlay reaches some global minimizer in at most

   \[
   \boxed{
   |\mathcal K(F_0,G^*)|
   \le\left\lfloor\frac{|F_0\setminus G^*|}{2}\right\rfloor
   \le\left\lfloor\frac B2\right\rfloor
   }
   \tag{Y4.43}
   \]

   strict exact moves.  Until a minimum is reached,

   \[
   \boxed{
   \mathcal Q_H(F_{t+1})-M_{m,H}
   \le
   \left(1-\frac2B\right)
   \bigl(\mathcal Q_H(F_t)-M_{m,H}\bigr).
   }
   \tag{Y4.44}
   \]

3. For every real \(L\), the following are equivalent:

   \[
   M_{m,H}\le L;
   \tag{Y4.45}
   \]

   \[
   \text{every }F\text{ with }\mathcal Q_H(F)>L
   \text{ has an improving Gram-antagonistic move};
   \tag{Y4.46}
   \]

   \[
   \text{every }F
   \text{ reaches }\{\mathcal Q_H\le L\}
   \text{ within }\lfloor B/2\rfloor
   \text{ strict augmented moves}.
   \tag{Y4.47}
   \]

   Here a start already satisfying \(\mathcal Q_H(F)\le L\) uses zero
   moves.

#### Proof

If \(F\) is not globally minimal, compare it with \(G^*\) in Theorem 7.1.
This proves (Y4.42).

After switching a packet toward \(G^*\), all of its ownership components
become common with \(G^*\); the unswitched components are unchanged.
Every strict step removes at least one remaining component.  The process
therefore stops within (Y4.43), either at \(G^*\) or earlier at another
global minimizer.  Equation (Y4.40), with \(G=G^*\), proves (Y4.44).

If (Y4.45) holds and \(\mathcal Q_H(F)>L\), then \(G^*\) is a better
comparator, so Theorem 7.1 gives (Y4.46), and the preceding iteration gives
(Y4.47).  Conversely, if \(M_{m,H}>L\), a global minimizer itself has energy
above \(L\) and has no improving move.  This contradicts either (Y4.46) or
(Y4.47). \(\square\)

### Corollary 7.3: monotone fair stopping time

Fix a global minimizer \(G^*\).  At a nonminimal current state, select the
improving Gram-antagonistic packet supplied by Theorem 7.1 and repeatedly
apply the fair binary Haar projector on that macro-edge until its switched
endpoint is sampled.  Then the process reaches some global minimizer almost
surely, its energy never increases at any trial, and

\[
\boxed{
\mathbb E_F T_{\min}
\le
2|\mathcal K(F,G^*)|
\le |F\setminus G^*|
\le B.
}
\]

Indeed, a failed fair trial leaves the state unchanged, while a successful
trial makes the strict improvement and removes at least one remaining
comparison component.  Each successful stage has geometric waiting time of
mean two, and there are at most the initial
\(|\mathcal K(F,G^*)|\) stages.  This is a stopped process for the newly
adjoined binary macro-projectors, not for the original fixed transposition
heat.

### Augmented-Haar primitivity

Recall

\[
\widehat A_H
=
\begin{pmatrix}
A_m&0\\
D_H&-I
\end{pmatrix}.
\tag{Y4.48}
\]

For a legal packet \(J\), put

\[
\widehat z_J=(z_J,v_J)\in\ker_{\mathbb Z}\widehat A_H.
\]

### Theorem 7.4: antagonistic packets are feasible augmented primitives

Every Gram-antagonistic packet satisfies

\[
\boxed{
\widehat z_J\in\operatorname{Gr}(\widehat A_H).
}
\tag{Y4.49}
\]

#### Proof

Because \(z_J\) is squarefree and support feasible, any conformal
\(A_m\)-kernel submove supported inside it is a union \(z_I\) of complete
ownership components.  The lifted lower block forces its auxiliary part to
be \(v_I\).

Suppose a nonempty proper conformal lifted submove existed.  Then

\[
v_I\sqsubseteq v_J.
\]

Consequently \(v_I\) and

\[
v_{J\setminus I}=v_J-v_I
\]

are coordinatewise sign-compatible.  Their weighted inner product is
nonnegative, contradicting (Y4.24).  Thus no proper conformal kernel
submove exists. \(\square\)

The converse is not proved.  A feasible augmented-Graver packet can be
primitive for a reason not detected by strict Gram antagonism.

---

## 8. What the unique class says about Catalan-scale energy

For \(H=H_A\), define the normalized global minimum

\[
\kappa_A(m)
=
\frac{M_{m,H_A}}{H_AB}.
\tag{Y4.50}
\]

Since the augmented graph is connected,

\[
\boxed{
\min_{G\in\mathscr C_{\rm aug}(F)}
\mathcal Q_{H_A}(G)
=M_{m,H_A}
=\kappa_A(m)H_AB
}
\tag{Y4.51}
\]

for every start \(F\).

Therefore

\[
\boxed{
\text{the augmented class contains }
\mathcal Q_{H_A}=O_A(H_AB)
\iff
\sup_{m\ge m_0(A)}\kappa_A(m)<\infty.
}
\tag{Y4.52}
\]

This is an exact reduction, not a new estimate on the minimum.  The right
side is **unproved**.

If (Y4.52) holds, every start reaches a target factor in at most
\(\lfloor B/2\rfloor\) strictly energy-decreasing Gram-antagonistic moves.
Conversely, failure of (Y4.52) means that even the single universal
augmented class has no such quadratic-energy target on an asymptotic
subsequence.

The exact overload inequality is

\[
\mathcal O_H(F)\le\frac12\mathcal Q_H(F).
\tag{Y4.53}
\]

Moreover,

\[
\frac{H_AB}{W}=\frac{H_A}{n}=O_A(m^{-1/2}).
\]

Hence \(\mathcal Q_{H_A}=O_A(H_AB)\) gives
\(\mathcal O_{H_A}=o_A(W)\).

Thus (Y4.52), for every fixed \(A\), is a sufficient fixed-window
unlabelled balancing theorem and has the frozen diagonal implication to
MWB.  The converse is not proved: low mobile overload need not force
Catalan-scale quadratic energy.

### 8.1 A universal but far-too-weak upper bound

The class does have an unconditional quantitative energy bound, but it is
far above the desired scale.

Fix \(S\in\binom{[n]}{m-q}\).  Each occurrence of \(S\) as a cyclic
\((m-q)\)-interval lies in exactly \(q+1\) middle intervals of the same
wreath.  Across distinct occurrences in an exact factor, these middle
supersets are disjoint, because every middle set has one owner.  Since the
number of middle supersets of \(S\) is

\[
\binom{m+q+1}{q},
\]

we have

\[
\boxed{
\mu_q^F(S)
\le
L_{m,q}:=
\left\lfloor
\frac1{q+1}\binom{m+q+1}{q}
\right\rfloor.
}
\tag{Y4.54}
\]

Therefore

\[
\sum_S\mu_q^F(S)^2
\le L_{m,q}\sum_S\mu_q^F(S)
=L_{m,q}W.
\]

Since

\[
Q_q(F)
=\|f_q^F\|_2^2-\beta_q
\le\sum_S\mu_q^F(S)^2,
\]

every exact factor satisfies

\[
\boxed{
\mathcal Q_H(F)
\le
W\sum_{q=1}^{H}\frac{L_{m,q}}{c_q}.
}
\tag{Y4.55}
\]

In particular,

\[
\boxed{
M_{m,H}
\le
W\sum_{q=1}^{H}\frac{L_{m,q}}{c_q}.
}
\tag{Y4.56}
\]

For \(H=H_A=\lceil A\sqrt m\rceil\le(A+1)\sqrt m\), the binomial estimate

\[
\binom{m+q+1}{q}
\le
\left(\frac{e(m+q+1)}q\right)^q
\]

and \(c_q\ge1\) give

\[
\begin{aligned}
\frac{M_{m,H_A}}{H_AB}
&\le \frac n{H_A}
\sum_{q=1}^{H_A}L_{m,q}\\
&\le n\binom{m+H_A+1}{H_A}\\
&\le
n\left(\frac{e(m+H_A+1)}{H_A}\right)^{H_A}.
\end{aligned}
\]

Taking logarithms therefore gives

\[
\boxed{
\frac{M_{m,H_A}}{H_AB}
\le
\exp\!\bigl(O_A(\sqrt m\log m)\bigr).
}
\tag{Y4.57}
\]

This is an honest class bound, but it is asymptotically useless for
(Y4.52).

### 8.2 Boolean-\(E_2\) compatibility

The proved Boolean-\(E_2\) stability theorem does not lower-bound
\(M_{m,H_A}\).  If (Y4.52) is true and \(F^*\) is a low global minimizer,
then the Y3 theorem forces

\[
\Xi_{H_A}(F^*)=\Omega_A(nW\sqrt m).
\tag{Y4.58}
\]

Thus a successful Gram-antagonistic descent must terminate at a
floor-balanced factor with large higher-harmonic surplus.  Nothing in
(Y4.24), (Y4.39), or the augmented-Graver proof suppresses that surplus.
The present class theorem is therefore compatible with the Boolean-\(E_2\)
no-go.

---

## 9. A narrower permutation-defined nonlocal Haar family

The comparison-Haar family is exact but global.  A more concrete
coordinate-defined family gives strong coherent displacement, although its
class connectivity and correlated residual remain open.

Let \(\mathcal I_m\) be the conjugacy class in \(S_n\) of involutions of
cycle type

\[
1\,2^m.
\]

Fix \(\sigma\in\mathcal I_m\), cancel the common wreaths of \(F\) and
\(\sigma F\), and form their reduced ownership overlay.  The involution
\(\sigma\) side-swaps the overlay and permutes its connected components in
orbits of size one or two.  Common wreaths remain fixed.  For each component
orbit \(\mathcal O\), bundle all of its old sides into
\(N_{\mathcal O}\) and put

\[
p_{\mathcal O}
=\mathbf1_{\sigma N_{\mathcal O}}
-\mathbf1_{N_{\mathcal O}},
\qquad
\delta_{\mathcal O}=D_Hp_{\mathcal O}.
\tag{Y4.59}
\]

Then

\[
\sigma p_{\mathcal O}=-p_{\mathcal O},
\qquad
\sigma\delta_{\mathcal O}=-\delta_{\mathcal O}.
\tag{Y4.60}
\]

For signs \(\varepsilon_{\mathcal O}\in\{\pm1\}\), define

\[
F_\varepsilon
=
(F\cap\sigma F)
\,\dot\cup\!
\bigcup_{\mathcal O}
\begin{cases}
\sigma N_{\mathcal O},&\varepsilon_{\mathcal O}=+1,\\
N_{\mathcal O},&\varepsilon_{\mathcal O}=-1.
\end{cases}
\]

Every \(F_\varepsilon\) is an exact factor, because this chooses complete
sides of the direct \(F/\sigma F\) ownership components and retains the
common wreaths.

Put

\[
h_\sigma=\frac{f^F+\sigma f^F}{2},
\qquad
A_\sigma=\|\sigma f^F-f^F\|_H^2.
\]

The midpoint is \(\sigma\)-invariant and every
\(\delta_{\mathcal O}\) is anti-invariant, so they are orthogonal.

### Theorem 9.1: exact involution-Haar signing identity

For every packet signing
\(\varepsilon_{\mathcal O}\in\{\pm1\}\),

\[
\boxed{
\mathcal Q_H(F_\varepsilon)-\mathcal Q_H(F)
=
\frac{
\left\|
\sum_{\mathcal O}
\varepsilon_{\mathcal O}\delta_{\mathcal O}
\right\|_H^2
-A_\sigma
}{4}.
}
\tag{Y4.61}
\]

Thus the best gain in the \(\sigma\)-bundle cell is

\[
\boxed{
\gamma_\sigma(F)
=
\frac14
\left(
A_\sigma
-
\min_\varepsilon
\left\|
\sum_{\mathcal O}
\varepsilon_{\mathcal O}\delta_{\mathcal O}
\right\|_H^2
\right).
}
\tag{Y4.62}
\]

#### Proof

The signed profile is

\[
f^{F_\varepsilon}
=h_\sigma+\frac12
\sum_{\mathcal O}\varepsilon_{\mathcal O}\delta_{\mathcal O},
\]

whereas the all-old factor has

\[
f^F=h_\sigma-\frac12\sum_{\mathcal O}\delta_{\mathcal O}.
\]

The invariant midpoint is orthogonal to every anti-invariant summand, and

\[
\sum_{\mathcal O}\delta_{\mathcal O}=\sigma f^F-f^F.
\]

Subtract the two squared norms and cancel \(\mathfrak B_H\) to obtain
(Y4.61).  Optimizing the displayed difference gives (Y4.62). \(\square\)

For an arbitrary noninvolutive comparison permutation, (Y4.61) is false
without extra linear midpoint fields.  The anti-invariance in (Y4.60) is
essential.

### 9.1 Exact coherent spectrum

Let \(\sigma\) be uniform in \(\mathcal I_m\).  The conjugacy-class average
acts on Johnson degree \(j\) by a scalar \(\rho_j\).  The number of
\(\sigma\)-fixed \(j\)-subsets is

\[
\operatorname{Fix}_{2a}(\sigma)=\binom ma,
\qquad
\operatorname{Fix}_{2a+1}(\sigma)=\binom ma.
\]

The character ratio on the two-row Johnson module is therefore

\[
\boxed{
\rho_0=1,\qquad
\rho_{2a+1}=0,\qquad
\rho_{2a}
=\frac{\binom ma}{\binom{2m+1}{2a}}.
}
\tag{Y4.63}
\]

For \(1\le a\le\lfloor m/2\rfloor\), these nonconstant even ratios decrease
with \(a\), and

\[
0\le\rho_{2a}\le\rho_2=\frac1n.
\tag{Y4.64}
\]

Every exact centered load has Johnson degrees \(j\ge2\).  Indeed, centering
kills degree zero, while for every label \(x\)

\[
\sum_{S\ni x}\mu_q^F(S)=r_qB
\]

because each of the \(B\) wreaths has exactly \(r_q\) cyclic
\(r_q\)-intervals containing \(x\).  Thus all point margins are constant,
which kills degree one.  Hence

\[
\boxed{
2\left(1-\frac1n\right)
\bigl(\mathcal Q_H(F)+\mathfrak B_H\bigr)
\le
\mathbb E_{\sigma\in\mathcal I_m}A_\sigma
\le
2\bigl(\mathcal Q_H(F)+\mathfrak B_H\bigr).
}
\tag{Y4.65}
\]

#### Proof

Centrality of the conjugacy-class average makes it scalar on each Johnson
irreducible.  The degree-\(j\) character is

\[
\operatorname{Fix}_j-\operatorname{Fix}_{j-1},
\]

and its dimension is

\[
\binom nj-\binom n{j-1}.
\]

Substitution of the fixed-set counts gives (Y4.63).  Whenever
\(2a+2\le m\), the ratio of the \(a+1\) and \(a\) nonconstant even values
simplifies to

\[
\frac{2a+1}{2m+1-2a}\le1
\qquad(2a+2\le m),
\]

which proves (Y4.64).  Finally,

\[
\mathbb E_\sigma\|f-\sigma f\|_2^2
=2\sum_{j\ge2}(1-\rho_j)\|f_j\|_2^2
\]

rank by rank.  Weight and sum in \(q\). \(\square\)

The coherent displacement is therefore of constant order, not the
\(1/n\)-order contraction of one random transposition.

Now take \(H=H_A\).  Admit every simultaneous involution-orbit signing from
Theorem 9.1 as one exact Haar-cell macro-transition.  One concrete
sufficient residual gate for this narrower family would be the following:
there exist constants
\(0<\eta_A\le1\) and \(C_A>0\) such that, for every sufficiently large
\(m\) and every exact factor \(F\),

\[
\boxed{
\mathbb E_{\sigma\in\mathcal I_m}\gamma_\sigma(F)
\ge
\eta_A\mathcal Q_H(F)-C_AH_AB
}
\tag{IHG_A}
\]

This gate is **unproved**, and it is not claimed necessary for a low class
minimum.  If it were true, every class minimum for the involution-bundle
macro-augmentation would have

\[
\mathcal Q_H(F)\le\frac{C_A}{\eta_A}H_AB,
\]

because at a class minimum every signed endpoint has no smaller energy, so
\(\gamma_\sigma(F)=0\) for every \(\sigma\).  If instead

\[
\mathcal Q_H(F)\ge\frac{2C_A}{\eta_A}H_AB,
\]

then the gate gives \(\mathbb E_\sigma\gamma_\sigma(F)\ge
\eta_A\mathcal Q_H(F)/2\).  Hence some involution and best simultaneous
signing contract the energy by at least the factor \(1-\eta_A/2\).  If only
one orbit packet at a time were admitted, the same
endpoint would remain exactly reachable, but this one-step contraction
statement would no longer follow because intermediate energies could rise.

The gate is compatible with Boolean-\(E_2\): it is thresholded,
state-dependent, and retains correlated nonlocal packet signs.  It does not
require \(R_H\) to lie near the absolute \(4(n-1)\mathfrak B_H\) baseline.

No connectivity theorem for the involution-bundle subfamily is proved.
Equation (Y4.65) controls coherent displacement only; the signing residual
in (Y4.62) may restore all of it.

---

## 10. Invariant audit

### 10.1 Full augmented family

The spanning-tree theorem gives the complete answer:

\[
\boxed{
\text{every state invariant of the augmented chain is constant.}
}
\tag{Y4.66}
\]

Consequently, any proposed invariant built from the following data is
either changed by some allowed tree edge or has one common value on the
whole fibre:

* integer and modular linear functionals;
* wreath-parity or chirality counts;
* support and ownership-component statistics;
* odd-graph homology classes modulo allowed alternating packets;
* voltage and holonomy state labels; and
* nonlinear invariants.

For homology explicitly, encode a factor by its odd-graph
\(\mathbb F_2\)-edge cycle \(e(F)\).  Every tree edge difference

\[
e(p(F))+e(F)
\]

is a sum of its alternating cycles.  Telescoping along the unique tree path
shows that

\[
e(G)+e(F)
\]

lies in the span of allowed packet differences for every \(F,G\).
Therefore a remaining holonomy can describe how a path was decomposed, but
cannot separate vertices or communicating classes.

### 10.2 Narrow coordinate-group families

If one permits only component translations from coordinate groups
\(\Gamma_a\) and lets

\[
L=\langle\Gamma_a:a\rangle,
\]

then the exact \(L\)-orbit totals at every lower rank remain invariant.  The
associated integral convex orbit floors are the profile floors from Y3.
When \(L=S_n\), there is one orbit at every rank and those floors vanish.

When \(m\) is even, \(A_n\)-only coordinate Haar can preserve the two
unoriented-wreath chirality counts.  However, \(A_n\) is transitive on each
relevant target rank, so chirality gives no positive lower-shadow
orbit-profile floor.  An odd transposition exchanges the two chirality
orbits, and switching a component \(K\) changes the even-wreath count by the
difference between the two chirality populations in \(K\).  Thus
\(A_n\)-orbit invariance supplies no invariant once odd moves are admitted;
the previously audited \(m=4\) odd-component trade is an explicit parity
change.  No all-\(m\) parity-change theorem is needed here.

Thus the narrower invariant search produces no obstruction to the intended
completed chain and no Catalan-scale energy floor.

---

## 11. Scope, caveats, and independent audit ledger

Three independent proof audits separately rederived (i) the ownership
circuit, restricted cube, diameter, and hub tree; (ii) the
Gram-antagonistic split recursion, \(2/B\) constant, augmented-Graver
argument, occurrence cap, and involution spectrum; and (iii) the invariant,
alternating-trail, and MWB implication scopes.  Each audit returned the core
theorems valid.  Its quantifier and wording corrections have been
incorporated above.  The following qualifications are essential.

1. **Exact positivity.**  Every circuit used for connectivity comes from the
   ownership overlay of two completed exact factors, or is explicitly
   assumed applicable at its negative endpoint.  Arbitrary partial trades,
   including the known six-for-six shallow-neutral packet, are not promoted
   without a common completion.

2. **Circuit constant.**  Overlay regularity gives equal side sizes.
   Injectivity of wreath middle columns excludes side size one for \(m\ge2\).
   Therefore the number of components is at most
   \(\lfloor|F\setminus G|/2\rfloor\), not merely
   \(|F\setminus G|\).  This is the sole source of the factor two in
   (Y4.40).

3. **Full versus half energy.**  The report uses the full energy
   \(\mathcal Q_H\).  Consequently the mixed identity (Y4.39) has
   \(2\langle v_I,v_L\rangle_H\).  The selected gain remains \(g/t\);
   no extra factor two enters there.

4. **Ordinary versus augmented circuits.**  A singleton comparison component
   is a support-minimal ordinary \(A_m\)-circuit.  A multicomponent
   Gram-antagonistic packet can be disconnected in the middle ownership
   overlay and is primitive only in the augmented load lift.  It must be
   admitted as one macro-move to obtain one-step monotone descent.  If only
   its connected components are admitted, the same endpoint is reachable,
   but intermediate energies may increase.

5. **Graver direction.**  Gram antagonism implies feasible augmented-Graver
   primitivity.  The converse is not asserted.

6. **Markov scope.**  Connected comparison circuits form a Markov/test family
   for the exact right-hand side \(A_mx=\mathbf1\).  No claim is made that
   this squarefree subfamily connects every nonnegative fibre of \(A_m\).

7. **Alternating-cycle scope.**  Edgewise alternating-cycle decomposition
   preserves a spanning 2-factor, not necessarily a decomposition into
   \(C_n\) wreath cycles.  Exactness begins with the whole ownership packet.

8. **Midpoint fields.**  For a general comparison cube,
   \(f_c=(f^F+f^G)/2\) need not be orthogonal to individual component effects.
   Pure sign-norm formulas are invalid there.  They become valid in
   Section 9 only after involution component orbits are bundled so that each
   effect is anti-invariant.

9. **Sparse family scope.**  The hub tree is an explicit, cardinality-minimal
   state-edge family, but it is not a bounded local circuit library.  It
   requires comparison with a globally fixed exact factor and may contain
   factor-scale packets.

10. **Energy conclusion.**  Connectivity proves that the class minimum is
    \(M_{m,H}\), not that \(M_{m,H}=O_A(H_AB)\).  The latter remains the exact
    unproved quadratic target.  Likewise, Theorem 7.2 excludes nonglobal
    local minima only in the comparator-defined Gram-antagonistic
    macro-neighborhood.

11. **MWB scope.**  Catalan-scale quadratic energy is sufficient for small
    unlabelled overload.  It is stronger than the frozen overload target and
    supplies no labelled common-owner synchronization.

12. **Original graph.**  Nothing here proves that the unaugmented
    transposition-cell graph is connected or rules out a
    transposition-rigid class.  The new circuits deliberately bridge any
    such classes.

---

## 12. Final theorem-level status

The fourth-wave class attack proves:

* literal ownership-connected packing circuits and their exact
  comparison-Haar cubes;
* connectivity of the exact-factor fibre after one explicit
  Gram-antagonistic Haar augmentation;
* the diameter bound \(\lfloor\operatorname{Cat}_m/2\rfloor\) and controlled
  fair hitting bound \(\operatorname{Cat}_m\);
* a canonical cardinality-minimal comparison-Haar spanning tree;
* collapse of every state, modular, lattice, homological, and holonomy
  class invariant;
* exact Gram-antagonistic comparison descent with gain at least
  \(2/\operatorname{Cat}_m\) of the comparator gap;
* arrival at a global floor-energy minimizer in at most
  \(\lfloor\operatorname{Cat}_m/2\rfloor\) strict macro-moves;
* an almost-sure monotone fair macro-projector policy with expected
  minimizer hitting time at most \(\operatorname{Cat}_m\);
* equivalence of every augmented low-class statement to the global minimum
  bound \(M_{m,H_A}=O_A(H_A\operatorname{Cat}_m)\);
* the universal occurrence-cap bound (Y4.56), which remains far too weak;
  and
* a narrower involution-Haar family with exact constant coherent spectrum
  and the explicit unproved residual gate \((\mathrm{IHG}_A)\).

Thus the communicating-class obstruction can be removed completely by a
precise integral nonlocal circuit family.  For this oracle-scale
fibre-completion neighborhood, what remains is not communicating-class
topology but the positive global optimization statement

\[
\boxed{
\min_{F\in\mathfrak F_m}\mathcal Q_{H_A}(F)
=O_A\!\left(
H_A\operatorname{Cat}_m
\right).
}
\]

No proof or disproof of this bound is obtained.  No exact-factor invariant
forcing its failure is found.  The sparse comparison-Haar tree shows that
the failure cannot be blamed on communicating classes once nonlocal
ownership circuits are admitted; the Gram-antagonistic theorem shows that
it cannot be blamed on nonglobal local minima in that augmented
neighborhood.  For this completed neighborhood, the remaining obstruction
is exactly the value of the global integral optimum.
