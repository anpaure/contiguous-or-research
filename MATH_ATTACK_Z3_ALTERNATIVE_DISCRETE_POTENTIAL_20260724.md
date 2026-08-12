# Third-wave lane Z: alternative discrete potentials and exchange neighborhoods

## Verdict

There is a useful alternative potential, and there is a strictly more
structured exchange theorem than “use the entire augmented Graver basis.”

The alternative potential is the **free-quota corridor**

\[
\mathcal C_H(F)
=
\sum_{q\le H}\frac1{c_q}
\sum_S
\operatorname{dist}\!\left(\mu_q(F,S),\{c_q,c_q+1\}\right).
\]

It has four decisive properties.

1. It is factorwise equivalent to true mobile-quota overload within the
   universal factor two (sharp for unrestricted fixed-mass histograms;
   exact-factor sharpness is not claimed):
   \[
   \sum_{q\le H}\frac{O_q(F)}{c_q}
   \le \mathcal C_H(F)
   \le
   2\sum_{q\le H}\frac{O_q(F)}{c_q}.
   \]
   Thus its fixed-window \(o(W)\) theorem is equivalent to the unlabelled
   MWB target.

2. It is separable discrete convex in the load variables.  Unlike the exact
   mobile-overload linearization, it needs no high-quota selector variables:
   the ordinary load lift
   \[
   \widehat A_H=
   \begin{pmatrix}
   A_m&0\\
   B_H&-I
   \end{pmatrix}
   \]
   suffices.

3. Full augmented-Graver locality is exact global locality, with the usual
   \(1/\operatorname{Cat}_m\) comparison improvement.  More strongly, an
   objective-specific **atomic packet** subset of the feasible augmented
   Gravers is already an exact test set.

4. There is a simpler, matrix-free enlargement of the ownership-component
   neighborhood.  Join two ownership components when their retained load
   effects cancel in some coordinate.  Local minima under unions connected
   in this sign-cancellation graph are exactly global minima for every
   separable discrete-convex load potential, including both corridor and
   floor energy.

For quadratic floor energy the atomic condition becomes completely
explicit and base-independent: a packet \(J\) is **Gram-antagonistic** when

\[
\langle v_I,v_{J\setminus I}\rangle_H<0
\qquad
\text{for every nonempty proper }I\subset J.
\]

Every better comparator contains an improving Gram-antagonistic legal
packet.  Hence local optimality under these packets is exactly global
floor-energy optimality.  Every such packet is a feasible augmented-Graver
primitive.  The fixed-window Z2 MSW pair gives a genuine two-component
example, so this neighborhood strictly enlarges single ownership-component
moves.

Two limitations are exact.

- Atomic packets need not be small.  An integral nonnegative fixed-mass
  two-coordinate model has an arbitrarily large Gram-antagonistic packet
  whose full union is the only improving subpacket.  This is not proved
  wreath-realizable, so it is a structural warning rather than an
  exact-factor lower bound.
- These descent theorems reach the positive global corridor minimum but do
  not bound it.  The missing statement remains
  \[
  \min_F\mathcal C_{H_A}(F)=o(W)
  \qquad\text{for every fixed }A.
  \]

Thus Z3 restores a genuine exchange descent theorem and replaces quadratic
component noise by an exact \(L^1\) cancellation residue.  It does not prove
MWB, a literal OR word, or labelled common-owner synchronization.

## 1. Exact-factor and load notation

Put

\[
n=2m+1,
\qquad
W=\binom nm,
\qquad
B=\frac Wn=\operatorname{Cat}_m.
\]

Let \(\mathscr W_m\) be the unoriented wreath columns and

\[
\mathcal X_m
=
\{x\in\mathbb Z_{\ge0}^{\mathscr W_m}:A_mx=\mathbf1\}
\]

the nonempty finite exact-factor fibre.  Every \(x\in\mathcal X_m\) is
binary and has \(B\) selected wreaths.

Fix

\[
1\le H\le m-1.
\]

At depth \(q\), let

\[
r_q=m-q,
\qquad
N_q=\binom n{r_q},
\qquad
B_qx=\mu_q(x),
\]

where \(B_q\) is the actual rank-\(r_q\) load map.  Every row has total
mass \(W\).  Write

\[
W=c_qN_q+\rho_q,
\qquad
c_q=\left\lfloor\frac W{N_q}\right\rfloor\ge1,
\qquad
0\le\rho_q<N_q.
\tag{1.1}
\]

Let

\[
B_Hx=(B_1x,\ldots,B_Hx)
\]

be the vertically stacked load map.

For exact factors \(F,G\), cancel common wreaths and form their
middle-ownership overlay.  Its connected components are denoted
\(\mathcal K(F,G)\).  Orient every component from \(F\) to \(G\), and put

\[
z_K=\mathbf1_{G\cap K}-\mathbf1_{F\cap K},
\qquad
v_K=B_Hz_K.
\tag{1.2}
\]

For every \(J\subseteq\mathcal K(F,G)\),

\[
z_J=\sum_{K\in J}z_K,
\qquad
v_J=\sum_{K\in J}v_K,
\qquad
F_J=F+z_J
\tag{1.3}
\]

is a genuine integral exact factor.  Moreover,

\[
|\mathcal K(F,G)|
\le |F\setminus G|
\le B.
\tag{1.4}
\]

All exchanges below are unions of these complete ownership components.
No signed, fractional, or depthwise independently chosen factor is used.

## 2. The free-quota corridor potential

For one load row \(\mu\) of total \(W=cN+\rho\), put

\[
D^-(\mu)=\sum_i(c-\mu_i)_+,
\qquad
D^+(\mu)=\sum_i(\mu_i-c-1)_+.
\tag{2.1}
\]

The mobile balanced overload is

\[
O(\mu)=\max(D^-(\mu),D^+(\mu)).
\tag{2.2}
\]

For depth \(q\), abbreviate

\[
O_q(F)=O(B_qF),
\qquad
C_q(F)=C(B_qF).
\tag{2.2a}
\]

Define the corridor defect

\[
C(\mu)
=D^-(\mu)+D^+(\mu)
=\sum_i\chi_c(\mu_i),
\tag{2.3}
\]

where

\[
\chi_c(t)
=
\operatorname{dist}\!\left(t,\{c,c+1\}\right)
=
(c-t)_++(t-c-1)_+.
\tag{2.4}
\]

For an exact factor define

\[
\boxed{
\mathcal C_H(F)
=
\sum_{q\le H}\frac{C(B_qF)}{c_q}.
}
\tag{2.5}
\]

### Theorem Z3.1 — exact equivalence with mobile overload

Let

\[
p(\mu)=|\{i:\mu_i\ge c+1\}|.
\]

Then

\[
\boxed{
2O(\mu)=C(\mu)+|p(\mu)-\rho|.
}
\tag{2.6}
\]

Consequently, factorwise,

\[
\boxed{
O(\mu)\le C(\mu)\le2O(\mu),
}
\tag{2.7}
\]

and

\[
\boxed{
\sum_{q\le H}\frac{O_q(F)}{c_q}
\le\mathcal C_H(F)
\le
2\sum_{q\le H}\frac{O_q(F)}{c_q}.
}
\tag{2.8}
\]

If

\[
J_H^*
=
\min_{F\in\mathcal X_m}
\sum_{q\le H}\frac{O_q(F)}{c_q},
\qquad
C_H^*=\min_{F\in\mathcal X_m}\mathcal C_H(F),
\]

then

\[
\boxed{
J_H^*\le C_H^*\le2J_H^*.
}
\tag{2.9}
\]

#### Proof

Let

\[
T=\sum_{\mu_i\ge c+1}(\mu_i-c).
\]

Since \(\sum_i(\mu_i-c)=\rho\),

\[
D^-=T-\rho,
\qquad
D^+=T-p.
\]

Thus

\[
D^--D^+=p-\rho.
\]

For two nonnegative numbers \(a,b\),

\[
2\max(a,b)=a+b+|a-b|.
\]

This proves (2.6).  Equations (2.7)--(2.8) follow immediately.  Taking
minima, and evaluating \(C_H\) at a minimizer of \(J_H\), gives (2.9).
\(\square\)

The factor two is sharp on the unrestricted fixed-mass histogram lattice:
for \(N=2,c=1,\rho=1\) and \(\mu=(3,0)\), one has
\(D^-=D^+=1\), hence \(C=2\) and \(O=1\).  This example is not asserted to
be the load row of an exact wreath factor; sharpness inside the exact-factor
image is unproved.

Therefore, for every fixed \(A>0\) and
\(H_A=\lceil A\sqrt m\rceil\le m-1\),

\[
C_{H_A}^*=o(W)
\iff
J_{H_A}^*=o(W).
\tag{2.10}
\]

This equivalence is unlabelled.  It does not select one common nested owner
resolution.

### Theorem Z3.2 — discrete convexity and Lipschitzness

The scalar corridor function has forward differences

\[
\chi_c(t+1)-\chi_c(t)
=
\begin{cases}
-1,&t\le c-1,\\
0,&t=c,\\
+1,&t\ge c+1.
\end{cases}
\tag{2.11}
\]

Hence \(\chi_c\) is discrete convex and \(1\)-Lipschitz.  Consequently
\(\mathcal C_H\) is a separable discrete-convex function of the stacked
load \(B_HF\).

It also lies below the half floor-collision energy:

\[
\mathcal C_H(F)
\le
\Psi_H(F)
:=
\frac12\sum_{q\le H}\frac1{c_q}
\sum_S
(\mu_q(S)-c_q)(\mu_q(S)-c_q-1).
\tag{2.12}
\]

#### Proof

The three cases in (2.11) follow directly from (2.4), and their values are
nondecreasing.  A deficit \(d=c-t>0\) contributes \(d\) to \(\chi_c\) and
\(d(d+1)/2\ge d\) to the floor energy.  A ceiling surplus
\(e=t-c-1>0\) contributes \(e\) and \(e(e+1)/2\ge e\), respectively.
Summing proves (2.12).  \(\square\)

The corridor is therefore quantitatively closer to overload than the
quadratic energy: it is never more than twice overload, whereas the
quadratic penalty can be arbitrarily larger.

## 3. Atomic packets: an objective-specific exact test set

The next theorem is not special to the corridor.  Let

\[
\Theta(u)=\sum_{a\in\mathcal A}\phi_a(u_a)
\tag{3.1}
\]

be any separable discrete-convex function on the retained load coordinates.
Thus every forward-difference sequence

\[
d_a(t)=\phi_a(t+1)-\phi_a(t)
\tag{3.2}
\]

is nondecreasing.  Positive rank weights, such as \(1/c_q\), are absorbed
into the functions \(\phi_a\).

For an \(F/G\) ownership overlay and a component packet
\(J\subseteq\mathcal K(F,G)\), define

\[
\Delta_F(J)
=
\Theta(B_HF+v_J)-\Theta(B_HF).
\tag{3.3}
\]

For a nontrivial cut \(J=I\mathbin{\dot\cup}L\), put

\[
\eta_F(I,L)
=
\Delta_F(J)-\Delta_F(I)-\Delta_F(L).
\tag{3.4}
\]

### Definition 3.1 — atomic legal packet

A nonempty component packet \(J\) is **\(\Theta\)-atomic at \(F\)** if
either \(|J|=1\), or

\[
\boxed{
\eta_F(I,J\setminus I)<0
\quad
\text{for every nonempty proper }I\subset J.
}
\tag{3.5}
\]

This is objective- and base-dependent.  It is nevertheless a property of a
genuine positive-fibre move: every endpoint \(F_J\) in (3.5) is the exact
factor (1.3).

In every local/global assertion below, the allowed macro-neighbors range
over all exact comparators \(G\) and all packets of their \(F/G\) overlays,
not over one fixed overlay chosen in advance.

### Lemma Z3.3 — conformal superadditivity

If \(a,b\ge0\), then for every discrete-convex scalar function \(\phi\),

\[
\phi(x+a+b)-\phi(x+a)
\ge
\phi(x+b)-\phi(x).
\tag{3.6}
\]

The same assertion holds when \(a,b\le0\).  Consequently, if two vectors
\(v,w\) are coordinatewise sign-compatible, then

\[
\Theta(u+v+w)-\Theta(u)
\ge
[\Theta(u+v)-\Theta(u)]
+[\Theta(u+w)-\Theta(u)].
\tag{3.7}
\]

#### Proof

For \(a,b\ge0\), the left increment in (3.6) is the sum of \(b\) forward
differences starting at \(x+a\), while the right increment is the sum of
the corresponding \(b\) forward differences starting at \(x\).  Monotonicity
of (3.2) proves the inequality.  Reverse the direction for two negative
increments.  Apply the scalar assertion coordinatewise and sum to obtain
(3.7).  \(\square\)

### Theorem Z3.4 — atomic-packet descent

Let \(F,G\in\mathcal X_m\), and suppose

\[
g=\Theta(B_HF)-\Theta(B_HG)>0.
\tag{3.8}
\]

Then there is a \(\Theta\)-atomic packet
\(J\subseteq\mathcal K(F,G)\) such that

\[
\boxed{
\Theta(B_HF)-\Theta(B_HF_J)
\ge
\frac{g}{|\mathcal K(F,G)|}
\ge
\frac gB.
}
\tag{3.9}
\]

Therefore

\[
\boxed{
F\text{ globally minimizes }\Theta\circ B_H\text{ on }\mathcal X_m
\iff
F\text{ has no improving }\Theta\text{-atomic legal packet.}
}
\tag{3.10}
\]

Starting from any \(F\), and fixing a global minimizer \(G^*\), repeated
atomic moves chosen inside the remaining \(F/G^*\) overlay reach a global
minimizer in at most

\[
|\mathcal K(F,G^*)|\le B
\tag{3.11}
\]

strict moves.

#### Proof

Start with the full packet \(J_0=\mathcal K(F,G)\).  Whenever a current
packet \(J\) is not atomic, choose a nontrivial cut
\(J=I\mathbin{\dot\cup}L\) for which \(\eta_F(I,L)\ge0\), and replace
\(J\) by its two parts.  By (3.4),

\[
\Delta_F(J)
\ge
\Delta_F(I)+\Delta_F(L).
\tag{3.12}
\]

The recursion terminates because packet cardinality strictly decreases.
Its terminal leaves \(P_1,\ldots,P_t\) partition \(J_0\), every leaf is
atomic, and iterating (3.12) gives

\[
-g
=\Delta_F(J_0)
\ge
\sum_{j=1}^t\Delta_F(P_j).
\tag{3.13}
\]

Since \(t\le|\mathcal K(F,G)|\), some leaf has
\(\Delta_F(P_j)\le-g/t\le-g/|\mathcal K(F,G)|\).  This proves (3.9).
The equivalence (3.10) follows by taking \(G\) to be a global minimizer.

After switching a leaf toward a fixed \(G^*\), the unswitched original
components remain a legal overlay with \(G^*\).  Every strict step removes
at least one such component.  The process either reaches \(G^*\), or stops
earlier at another factor having the same global value.  This proves
(3.11).  \(\square\)

The theorem is an exact descent statement, not merely a certificate that
some signed kernel direction exists.  All intermediate points stay in one
integral exact-factor fibre.

### Theorem Z3.5 — every atomic packet is augmented primitive

Consider the ordinary load lift

\[
\widehat A_H
=
\begin{pmatrix}
A_m&0\\
B_H&-I
\end{pmatrix}.
\tag{3.14}
\]

Its genuine positive fibre is

\[
\widehat{\mathcal X}_{m,H}
=
\left\{
(x,u):
\widehat A_H(x,u)=
\binom{\mathbf1}{0},
\quad
0\le x\le1,
\quad
0\le u\le W\mathbf1,
\quad
(x,u)\text{ integral}
\right\}.
\tag{3.14a}
\]

The map \(F\mapsto(F,B_HF)\) is a bijection from \(\mathcal X_m\) to
\(\widehat{\mathcal X}_{m,H}\).  Thus all feasibility statements below
refer to this boxed positive fibre, even though Graver primitivity itself is
a property of the unrestricted integer kernel.

For a legal packet \(J\), the lifted difference is

\[
\widehat z_J=(z_J,v_J)\in\ker_{\mathbb Z}\widehat A_H.
\tag{3.15}
\]

If \(J\) is \(\Theta\)-atomic at \(F\), then

\[
\boxed{
\widehat z_J\in\mathcal G(\widehat A_H).
}
\tag{3.16}
\]

Here (3.16) means a Graver element feasible between the two positive-fibre
vertices \((F,B_HF)\) and \((F_J,B_HF_J)\).  It does not purport to list
the entire unrestricted Graver basis of \(\widehat A_H\).

#### Proof

For exact-factor vertices, a squarefree conformal kernel submove of
\(z_J\) must be a union \(z_I\) of complete ownership components.  Indeed,
the middle-set equations force the two endpoint choices on each ownership
edge to agree, hence they are constant on every connected ownership
component.  The lower block of (3.14) then forces the lifted part to be
\(v_I\).

Suppose a nonempty proper conformal submove existed.  Then for some
\(\varnothing\ne I\subsetneq J\),

\[
v_I\sqsubseteq v_J,
\tag{3.17}
\]

where \(a\sqsubseteq b\) denotes coordinatewise sign compatibility and
\(|a_i|\le|b_i|\).  Thus \(v_I\) and
\(v_{J\setminus I}=v_J-v_I\) are coordinatewise sign-compatible.  Lemma
Z3.3 gives

\[
\eta_F(I,J\setminus I)\ge0,
\]

contrary to atomicity.  Hence no proper nonzero conformal kernel subvector
exists, which is precisely Graver primitivity.  \(\square\)

Combining Theorems Z3.4 and Z3.5 gives a sharper formulation than the
generic augmented-Graver augmentation theorem:

\[
\boxed{
\text{The objective-dependent atomic packets form an exact test set.}
}
\tag{3.18}
\]

They lie inside the feasible augmented-Graver neighborhood.  No claim is
made that this inclusion is always proper.

For the corridor, (3.14) is all that is required.  In particular, the
high-quota selector variables needed for an exact linearization of mobile
overload are absent.

## 4. A structural enlargement: cancellation-connected packets

Atomicity still quantifies over every cut.  There is a coarser but more
visible neighborhood with the same local/global conclusion.

For an oriented ownership overlay, form the **sign-cancellation graph** on
\(\mathcal K(F,G)\) by joining two distinct components when

\[
K\sim L
\iff
v_K(a)v_L(a)<0
\quad\text{for at least one retained load coordinate }a.
\tag{4.1}
\]

A component packet is cancellation-connected if its induced graph is
connected; a singleton is connected by convention.

### Theorem Z3.6 — cancellation-connected descent

For every separable discrete-convex load potential \(\Theta\), every better
comparator \(G\) for \(F\) contains a cancellation-connected packet \(J\)
such that

\[
\boxed{
\Theta(B_HF)-\Theta(B_HF_J)
\ge
\frac{\Theta(B_HF)-\Theta(B_HG)}
{|\mathcal K(F,G)|}
\ge
\frac{\Theta(B_HF)-\Theta(B_HG)}B.
}
\tag{4.2}
\]

Consequently,

\[
\boxed{
F\text{ is globally optimal}
\iff
F\text{ has no improving cancellation-connected macro-neighbor.}
}
\tag{4.3}
\]

Repeated moves toward a fixed global comparator take at most \(B\) strict
steps.

#### Proof

Let \(J_1,\ldots,J_t\) be the connected components of the graph (4.1),
and set \(w_j=v_{J_j}\).  For two distinct graph components, \(w_i,w_j\)
are coordinatewise sign-compatible.  Otherwise, at a coordinate where the
two aggregate signs were opposite, one individual summand from \(J_i\)
and one from \(J_j\) would have opposite nonzero signs, creating an edge
between the graph components.

Repeated use of Lemma Z3.3 gives

\[
\Theta\!\left(B_HF+\sum_{j=1}^tw_j\right)-\Theta(B_HF)
\ge
\sum_{j=1}^t
[\Theta(B_HF+w_j)-\Theta(B_HF)].
\tag{4.4}
\]

If the left side equals \(-g<0\), one summand is at most \(-g/t\).
Because \(t\le|\mathcal K(F,G)|\le B\), this proves (4.2).  The rest is
identical to the last part of Theorem Z3.4.  \(\square\)

### Corollary Z3.7 — relation to the augmented Graver neighborhood

Every feasible augmented-Graver packet for (3.14) is
cancellation-connected.  Therefore the three neighborhoods obey

\[
\{\Theta\text{-atomic packets}\}
\subseteq
\{\text{feasible augmented Graver packets}\}
\subseteq
\{\text{cancellation-connected packets}\}.
\tag{4.5}
\]

#### Proof

The first inclusion is Theorem Z3.5.  If an augmented-Graver packet had a
disconnected cancellation graph, take one graph component \(J_1\).  The
aggregate effects of \(J_1\) and its complement are sign-compatible, so
\(v_{J_1}\sqsubseteq v_J\).  The nonzero wreath move \(z_{J_1}\), together
with \(v_{J_1}\), would be a proper conformal lifted kernel submove,
contradicting primitivity.  \(\square\)

Graph connectivity forbids a conformal decomposition across the graph
partition, but by itself does not prove primitivity against every component
subunion.  Equality in the second inclusion of (4.5) is not established or
claimed on the genuine exact-factor fibre.

Applied to \(\mathcal C_H\), Theorem Z3.6 restores an exact exchange descent
theorem for a potential equivalent to overload within factor two.  Applied
to discrete entropy, exponential-tail, power-sum, or other separable convex
functions, it gives the same local/global mechanism, but those alternatives
have no proved comparison with mobile overload stronger than (2.8).

## 5. Quadratic refinement: Gram-antagonistic packets

Equip retained load space with

\[
\langle a,b\rangle_H
=
\sum_{q\le H}\frac1{c_q}\langle a_q,b_q\rangle_2,
\qquad
\|a\|_H^2=\langle a,a\rangle_H.
\tag{5.1}
\]

For an exact factor \(F\), center each rank block at its mean:

\[
f_{F,q}=B_qF-\frac W{N_q}\mathbf1.
\tag{5.2}
\]

Every feasible effect has zero coordinate sum in each rank block.  Expanding
the half floor energy (2.12) therefore gives, for every legal packet \(J\),

\[
\Delta_F(J)
=
\langle f_F,v_J\rangle_H+\frac12\|v_J\|_H^2.
\tag{5.3}
\]

The constant discrepancy between \(W/N_q\) and \(c_q+1/2\) disappears
because \(\sum_Sv_{J,q}(S)=0\).

For a cut \(J=I\mathbin{\dot\cup}L\), (5.3) yields the exact mixed term

\[
\boxed{
\eta_F(I,L)=\langle v_I,v_L\rangle_H.
}
\tag{5.4}
\]

### Definition 5.1 — Gram-antagonistic packet

A nonempty packet \(J\) is Gram-antagonistic if it is a singleton, or

\[
\boxed{
\langle v_I,v_{J\setminus I}\rangle_H<0
\quad
\text{for every nonempty proper }I\subset J.
}
\tag{5.5}
\]

Unlike general atomicity, (5.5) is independent of the base load \(f_F\).

### Theorem Z3.8 — exact floor-energy locality

If \(G\) improves the half floor energy of \(F\) by \(g>0\), then some
Gram-antagonistic packet \(J\subseteq\mathcal K(F,G)\) satisfies

\[
\boxed{
\Psi_H(F)-\Psi_H(F_J)
\ge
\frac g{|\mathcal K(F,G)|}
\ge
\frac gB.
}
\tag{5.6}
\]

Hence a factor is a global floor-energy minimizer if and only if it has no
improving Gram-antagonistic legal packet.  Every Gram-antagonistic packet is
a feasible Graver element of the augmented matrix (3.14).

Every inclusion-minimal improving floor-energy packet is
Gram-antagonistic.

#### Proof

By (5.4), Gram-antagonistic is exactly \(\Psi_H\)-atomic, so the first two
claims are Theorems Z3.4 and Z3.5.  If \(J\) is inclusion-minimal improving,
then \(\Delta_F(J)<0\), while for every nontrivial cut both proper parts
have nonnegative change.  Therefore

\[
\eta_F(I,J\setminus I)
=
\Delta_F(J)-\Delta_F(I)-\Delta_F(J\setminus I)<0,
\]

which proves the last assertion.  \(\square\)

There is also a still smaller floor-specific graph test.  Join \(K,L\) if

\[
\langle v_K,v_L\rangle_H<0.
\tag{5.7}
\]

Across distinct connected components of this graph all pairwise Gram terms
are nonnegative.  Decomposing (5.3) by graph components therefore shows
that every improving comparator contains an improving cluster connected
under (5.7), with the same bound (5.6).  A negative Gram edge necessarily
contains coordinatewise cancellation, so (5.7) is a subgraph of (4.1).

At the level of packet neighborhoods this gives

\[
\{\text{Gram-antagonistic packets}\}
\subseteq
\{\text{negative-Gram-graph-connected packets}\}
\subseteq
\{\text{sign-cancellation-connected packets}\}.
\tag{5.7a}
\]

The first inclusion follows because a disconnected negative-Gram graph
would give a cut whose every pairwise cross term is nonnegative, contrary
to (5.5).  Neither inclusion in (5.7a) is asserted strict in the genuine
fibre.

### Proposition Z3.9 — the enlargement is genuine in the exact fibre

For every \(m\ge4\), at \(H=2\) there exist exact factors

\[
F=X+z_1,
\qquad
G=X+z_0,
\tag{5.8}
\]

whose \(F/G\) overlay has the two oriented ownership components
\(z_0,-z_1\), with

\[
\boxed{
\langle B_Hz_0,-B_Hz_1\rangle_H=-\frac2{c_2}<0.
}
\tag{5.9}
\]

Thus their two-component union is both Gram-antagonistic and
cancellation-connected, although its ownership projection is disconnected.

#### Proof

In the audited Z2 construction, take

\[
R_0=(10)^{m-2},
\qquad
R_1=1100(10)^{m-4}.
\tag{5.10}
\]

The proved MSW component formula assigns to these Dyck words two connected,
independently switchable \(2\)-for-\(2\) ownership moves \(z_0,z_1\).
Its signed-core calculation gives

\[
\langle B_1z_0,B_1z_1\rangle_2=0,
\qquad
\langle B_2z_0,B_2z_1\rangle_2=2.
\tag{5.11}
\]

Thus reversing the second orientation changes the retained weighted inner
product to \(-2/c_2\), proving (5.9).  The endpoints (5.8) are obtained by
independently choosing the two component sides while fixing all other
ownership components.  The MSW component realization and the signed-core
calculation are previously proved exact inputs, not computational
certificates.  \(\square\)

Proposition Z3.9 proves strict structural enlargement beyond single
ownership-component moves.  It does **not** prove that the direction
\(F\to G\) improves \(\Psi_2\), nor does it exhibit a component-local but
nonglobal exact factor.  For \(H>2\), deeper-rank terms may change the total
Gram sign, so (5.9) is asserted only for \(H=2\).

## 6. What remains under single ownership-component locality

The corridor has bounded slope, so failure of ordinary component descent
can be measured by an exact linear cancellation residue rather than by a
quadratic variance term.

### Lemma Z3.10 — scalar cancellation inequality

Let \(\phi:\mathbb Z\to\mathbb R\) be discrete convex and
\(1\)-Lipschitz.  For arbitrary integers \(a_1,\ldots,a_s\),

\[
\boxed{
\sum_{i=1}^s[\phi(x+a_i)-\phi(x)]
\le
\phi\!\left(x+\sum_i a_i\right)-\phi(x)
+\sum_i|a_i|-\left|\sum_i a_i\right|.
}
\tag{6.1}
\]

#### Proof

Let

\[
P=\sum_{a_i>0}a_i,
\qquad
N=\sum_{a_i<0}(-a_i).
\]

Repeated same-sign superadditivity from Lemma Z3.3 gives

\[
\sum_i[\phi(x+a_i)-\phi(x)]
\le
[\phi(x+P)-\phi(x)]+[\phi(x-N)-\phi(x)].
\tag{6.2}
\]

Suppose \(P\ge N\).  Lipschitzness gives

\[
\phi(x+P)-\phi(x+P-N)\le N,
\qquad
\phi(x-N)-\phi(x)\le N.
\]

Substituting into (6.2) bounds its right side by

\[
\phi(x+P-N)-\phi(x)+2N.
\]

But \(2N=P+N-|P-N|=\sum_i|a_i|-|\sum_i a_i|\).  The case \(N\ge P\)
is symmetric.  \(\square\)

For exact factors \(F,G\), define the retained cancellation budget

\[
\boxed{
\operatorname{Can}_H(F,G)
=
\sum_{q\le H}\frac1{c_q}\sum_S
\left(
\sum_{K\in\mathcal K(F,G)}|v_{K,q}(S)|
-\left|\sum_{K\in\mathcal K(F,G)}v_{K,q}(S)\right|
\right).
}
\tag{6.3}
\]

It is nonnegative, symmetric in \(F,G\), and vanishes precisely when, in
each retained coordinate, all nonzero component effects have the same sign.

### Theorem Z3.11 — component-local near-global corridor bound

Suppose every individual ownership component in the \(F/G\) overlay is
nonimproving from \(F\):

\[
\mathcal C_H(F_K)\ge\mathcal C_H(F)
\qquad(K\in\mathcal K(F,G)).
\tag{6.4}
\]

Then

\[
\boxed{
\mathcal C_H(F)-\mathcal C_H(G)
\le
\operatorname{Can}_H(F,G).
}
\tag{6.5}
\]

In particular, if the overlay is coordinatewise sign-coherent, so that
\(\operatorname{Can}_H(F,G)=0\), component locality against \(G\) implies
\(\mathcal C_H(F)\le\mathcal C_H(G)\).

#### Proof

Apply Lemma Z3.10 to \(\chi_{c_q}\), with
\(x=\mu_q(F,S)\) and increments \(a_K=v_{K,q}(S)\).  Sum over all retained
coordinates and multiply each depth block by \(1/c_q\).  The result is

\[
\sum_K[\mathcal C_H(F_K)-\mathcal C_H(F)]
\le
\mathcal C_H(G)-\mathcal C_H(F)
+\operatorname{Can}_H(F,G).
\tag{6.6}
\]

The left side is nonnegative by (6.4), proving (6.5).  \(\square\)

### Proposition Z3.12 — universal size of the residue

Let \(d=|F\setminus G|\).  Then

\[
\boxed{
\operatorname{Can}_H(F,G)
\le
2nd\sum_{q\le H}\frac1{c_q}
\le
2W\sum_{q\le H}\frac1{c_q}
\le
2HW.
}
\tag{6.7}
\]

#### Proof

Every rank-shadow column of a wreath contains exactly \(n\) cyclic
intervals.  Hence, by the triangle inequality,

\[
\sum_K\|v_{K,q}\|_1
\le
n\sum_K\|z_K\|_1
=n\|G-F\|_1
=2nd.
\tag{6.8}
\]

Dropping the nonnegative term \(\left|\sum_Kv_{K,q}(S)\right|\) from
(6.3) proves the first bound.  Use \(d\le B=W/n\) for the second and
\(c_q\ge1\) for the third.  \(\square\)

The estimate (6.7) is only \(O(HW)\), not \(o(W)\).  The genuinely new
residual gate for upgrading single-component locality to near-globality is
therefore:

> **Unproved cancellation gate.**  Control
> \(\operatorname{Can}_{H_A}(F,G^*)=o(W)\) for a component-local factor
> \(F\) and a global corridor minimizer \(G^*\), or prove a comparably strong
> averaged version.

No such bound is proved here.  Theorem Z3.11 identifies exactly what would
be sufficient to show
\(\mathcal C_{H_A}(F)=C_{H_A}^*+o(W)\) for such a local \(F\); it does not
assert the gate.  Even that conclusion would not by itself prove
\(C_{H_A}^*=o(W)\).  An absolute bound on the global value remains a
separate necessity for MWB.

## 7. Tangent potentials: exact separation but not a Lyapunov function

Every separable discrete-convex objective has a one-component linear
separation certificate.

Choose a supporting slope \(s_a\) of \(\phi_a\) at \(u_a=B_HF(a)\), so
that

\[
\phi_a(y)\ge\phi_a(u_a)+s_a(y-u_a)
\qquad(y\in\mathbb Z).
\tag{7.1}
\]

Such a slope may be chosen between the backward and forward differences at
\(u_a\).

### Theorem Z3.13 — tangent component descent

If \(G\) improves \(F\) for \(\Theta\) by \(g>0\), then some single
ownership component \(K\in\mathcal K(F,G)\) satisfies

\[
\boxed{
\langle s,v_K\rangle
\le
-\frac g{|\mathcal K(F,G)|}
\le
-\frac gB.
}
\tag{7.2}
\]

#### Proof

Summing (7.1) over coordinates gives

\[
-g
=\Theta(B_HG)-\Theta(B_HF)
\ge
\langle s,B_H(G-F)\rangle
=
\sum_{K\in\mathcal K(F,G)}\langle s,v_K\rangle.
\tag{7.3}
\]

At least one summand is at most the average, proving (7.2).  \(\square\)

For half floor energy, the natural tangent functional is

\[
T_F(X)=\langle f_F,B_HX\rangle_H.
\tag{7.4}
\]

If \(G\) improves \(F\) by \(g>0\), and
\(d=B_H(G-F)\), then (5.3) gives the stronger identity

\[
T_F(G)-T_F(F)
=-g-\frac12\|d\|_H^2.
\tag{7.5}
\]

Thus one ownership component obeys

\[
T_F(F_K)-T_F(F)
\le
-\frac{g+\frac12\|d\|_H^2}{|\mathcal K(F,G)|}
\le-\frac gB.
\tag{7.6}
\]

This restores ordinary one-component descent only for the **base-dependent
linearization**.  The true floor-energy change is

\[
\Psi_H(F_K)-\Psi_H(F)
=
[T_F(F_K)-T_F(F)]+\frac12\|v_K\|_H^2,
\tag{7.7}
\]

so the component certified by (7.6) can increase \(\Psi_H\).  Therefore
\(T_F\) is a separation oracle, not an autonomous discrete potential whose
strict descent proves balancing.

There is also no useful symmetric affine substitute hidden here.  If the
coefficient array of an affine load functional is itself invariant under
all coordinate relabellings, transitivity of \(S_n\) on each rank forces
that coefficient to be constant within every rank.  Since
\(\sum_S\mu_q(S)=W\), the functional is then constant on \(\mathcal X_m\).
Any nonconstant tangent necessarily depends on the current factor or on an
arbitrary labelling.

## 8. A universal connected-move potential, and why it is circular

For completeness, one can force single-component descent by replacing the
objective with a nonlocal graph envelope.  This is an exact existence
result but supplies no method for bounding the objective optimum.

Let \(\mathfrak G_m\) be the graph whose vertices are exact factors and
whose edges are legal switches of one connected ownership component.  For
any \(F,G\), switching the components of their overlay one at a time gives

\[
d_{\mathfrak G}(F,G)
\le|\mathcal K(F,G)|
\le B.
\tag{8.1}
\]

For the corridor or half floor energy, put

\[
L_H=\operatorname{lcm}(c_1,\ldots,c_H).
\tag{8.2}
\]

All objective values lie in \(L_H^{-1}\mathbb Z\).  Set

\[
\varepsilon_H=\frac1{L_H(B+1)}
\tag{8.3}
\]

and define the graph envelope of either objective \(\Theta\) by

\[
\boxed{
\mathcal E_\Theta(F)
=
\min_{G\in\mathcal X_m}
\{\Theta(G)+\varepsilon_Hd_{\mathfrak G}(F,G)\}.
}
\tag{8.4}
\]

### Theorem Z3.14 — envelope descent

The single-component local minima of \(\mathcal E_\Theta\) are exactly the
global minimizers of \(\Theta\).  More precisely, if \(F\) is not a global
minimizer, then it has a graph neighbor \(F'\) with

\[
\boxed{
\mathcal E_\Theta(F')
\le
\mathcal E_\Theta(F)-\varepsilon_H.
}
\tag{8.5}
\]

A sequence choosing such a neighbor terminates after at most

\[
L_H(B+1)[\Theta(F)-\Theta^*]
\tag{8.6}
\]

steps, where \(\Theta^*=\min_G\Theta(G)\).

#### Proof

If \(F\) is nonglobal, discreteness gives

\[
\Theta(F)\ge\Theta^*+\frac1{L_H}.
\tag{8.7}
\]

For a global minimizer \(G^*\), (8.1)--(8.3) give

\[
\Theta(G^*)+\varepsilon_Hd_{\mathfrak G}(F,G^*)
\le
\Theta^*+\frac{B}{L_H(B+1)}
<\Theta(F).
\tag{8.8}
\]

Thus a minimizer \(G\) in (8.4) is not \(F\).  Let \(F'\) be the first
neighbor of \(F\) on a shortest path to \(G\).  Then

\[
\begin{aligned}
\mathcal E_\Theta(F')
&\le \Theta(G)+\varepsilon_Hd_{\mathfrak G}(F',G)\\
&=\Theta(G)+\varepsilon_H[d_{\mathfrak G}(F,G)-1]\\
&=\mathcal E_\Theta(F)-\varepsilon_H.
\end{aligned}
\]

If \(F\) is global, every term in (8.4) is at least \(\Theta^*\), and the
choice \(G=F\) shows \(\mathcal E_\Theta(F)=\Theta^*\); no neighbor is
lower.  This proves the local/global statement.  Finally
\(\mathcal E_\Theta(F)\le\Theta(F)\) and
\(\mathcal E_\Theta\ge\Theta^*\), so repeated decreases of size
\(\varepsilon_H\) give (8.6).  \(\square\)

The construction is mathematically exact but circular for the conjecture:
evaluating (8.4) already minimizes \(\Theta\) over all exact factors, and
an envelope-decreasing move need not decrease \(\Theta\) itself.  Likewise,
for any nonempty target set \(\mathcal T\), the graph distance

\[
d_{\mathcal T}(F)=\min_{G\in\mathcal T}d_{\mathfrak G}(F,G)
\tag{8.9}
\]

has one-component descent to \(\mathcal T\).  Taking \(\mathcal T\) to be
the set of factors with the desired \(o(W)\) overload assumes precisely the
missing nonemptiness statement.

## 9. No bounded packet theorem from abstract load convexity

The atomic and cancellation-connected neighborhoods can contain large
packets.  This is not a defect of the proof: abstract convex load data do
not imply any uniform packet-size bound.

### Proposition Z3.15 — arbitrarily large uniquely improving packets

For every integer \(r\ge1\), there is a two-coordinate, integral,
nonnegative, fixed-mass floor-energy instance with \(r+1\) abstract
load-feasible subset-switch effects such that:

1. the full packet is Gram-antagonistic;
2. the full packet strictly improves the base load; and
3. every nonempty proper subpacket strictly worsens the base load.

#### Construction and proof

Put

\[
C=3r+1,
\qquad
N=2,
\qquad
W=2C,
\qquad
c=C,
\tag{9.1}
\]

and take the base load and effects

\[
\mu=(C+1,C-1),
\qquad
v_0=(-C,C),
\qquad
v_i=(3,-3)\quad(1\le i\le r).
\tag{9.2}
\]

Every subset endpoint is integral, nonnegative, and has total \(2C\).
Indeed, a subset omitting \(v_0\) has scalar effect
\((w,-w)\) with \(0\le w\le3r=C-1\).  A subset containing \(v_0\) has
\(-C\le w\le-C+3r=-1\), and direct substitution in (9.2) gives
nonnegative coordinates in both cases.

Define the unweighted one-row half floor energy by

\[
\Phi(\lambda)
=
\frac12\sum_{i=1}^2(\lambda_i-C)(\lambda_i-C-1).
\tag{9.2a}
\]

For an arbitrary scalar effect \((w,-w)\), it is

\[
\begin{aligned}
\Phi(\mu+(w,-w))
&=\frac12(1+w)w
+\frac12(-1-w)(-2-w)\\
&=(w+1)^2.
\end{aligned}
\tag{9.3}
\]

Thus \(\Phi(\mu)=1\).  The full packet has

\[
w=-C+3r=-1,
\]

and hence energy \(0\).  A nonempty packet omitting \(v_0\) has
\(w\ge3\), so its energy is at least \(16\).  A proper packet containing
\(v_0\) uses at most \(r-1\) of the other effects, hence \(w\le-4\) and
its energy is at least \(9\).  This proves the unique-improvement claims.

Finally consider any nontrivial cut of the full packet.  Exactly one side
contains \(v_0\).  If the other side contains \(t\ge1\) of the positive
effects, its scalar sum is \(3t>0\), while the complementary scalar sum is

\[
-C+3(r-t)=-1-3t<0.
\]

Their Euclidean inner product is

\[
2(3t)(-1-3t)<0.
\tag{9.4}
\]

Hence every cut has negative Gram interaction, proving
Gram-antagonism.  \(\square\)

Multiplying \(\Phi\) and its Gram form by the standard positive rank weight
\(1/C\) changes none of the improvement or antagonism conclusions.

This construction is **not** claimed to be realized by wreath ownership
components.  It proves the precise negative statement that no bound on
packet size follows merely from separable convexity, integrality,
nonnegativity, fixed total mass, or even load dimension two.  Any bounded
packet theorem in the genuine fibre must use additional wreath-specific
structure.

## 10. Exhaustion of nearby discrete-potential routes

### 10.1 Standard \(M/L\)-convexity cannot be recovered by changing only
the scalar penalty

The obstruction lies in the exact-factor domain, not merely in the floor
quadratic.

### Proposition Z3.16 — domain-level exchange failure

For every \(m\ge2\), the exact-factor indicator set \(\mathcal X_m\) is
neither an \(M\)-convex nor an \(M^\natural\)-convex domain, and it is not
\(L^\natural\)-midpoint closed.

#### Proof

Every factor indicator has fixed cardinality \(B\).  Distinct unoriented
wreath columns have distinct middle-incidence columns: for a cyclic order
\(C\), the number of middle intervals containing two points \(u,v\) is

\[
m-d_C(u,v),
\tag{10.1}
\]

where \(d_C(u,v)\in\{1,\ldots,m\}\) is their unoriented cyclic distance.
Thus the middle-interval family determines all cyclic adjacencies and hence
the unoriented cycle.

Consequently, a one-wreath exchange would satisfy

\[
A_m(x-e_C+e_D)=\mathbf1
\quad\Longrightarrow\quad
A_me_C=A_me_D
\quad\Longrightarrow\quad
C=D.
\tag{10.2}
\]

The fibre contains distinct factors: take one exact factor and relabel it.
If every relabelling fixed it, transitivity on wreaths would force its
support to be either empty or all wreaths, whereas it has exactly \(B\)
members.  It is a proper nonempty subset because the total number of
unoriented wreaths is \((2m)!/2\), and

\[
\frac{(2m)!/2}{B}
=\frac{(m+1)(m!)^2}{2}>1
\qquad(m\ge2).
\tag{10.2a}
\]

For two distinct indicators \(x,y\), the \(M\)-exchange axiom demands a
nontrivial exchange (10.2), which is impossible.  In the
\(M^\natural\) axiom, the unpaired alternative changes the fixed
cardinality, while the paired alternative is again (10.2).  Finally, if

\[
k=|\operatorname{supp}x\setminus\operatorname{supp}y|\ge1,
\]

then

\[
\left\lfloor\frac{x+y}2\right\rfloor=x\wedge y,
\qquad
\left\lceil\frac{x+y}2\right\rceil=x\vee y
\]

have cardinalities \(B-k\) and \(B+k\), so neither is an exact factor.
This violates \(L^\natural\)-midpoint closure.  \(\square\)

Therefore replacing the quadratic by corridor, discrete entropy, an
exponential tail, a power sum, or another scalar convex function cannot make the
extended exact-factor objective conventionally \(M\)- or
\(L\)-convex.  The successful replacement must enlarge the moves, as in
Sections 3--5, or enlarge the state space with a Graver lift.

The independently proved Z2 transport theorem shows that, on the
unrestricted fixed-total load lattice, balanced \(L^1\) transport to a
mobile \(c/c+1\) quota is \(M\)-convex.  Pulling that objective back through
\(B_H\) to \(\mathcal X_m\) destroys the unit-exchange domain.  The corridor
avoids explicit quota selectors, but it cannot repair this domain
obstruction.

### 10.2 Other separable potentials do not improve the known target scale

Theorems Z3.4 and Z3.6 apply verbatim to every separable discrete-convex
potential.  This includes discrete-entropy penalties, exponentials of load,
power sums, and finite lexicographic tail encodings.  Their exchange theorem
is therefore no stronger than the general theorem already proved.  More
importantly, no inequality analogous to

\[
O\le C\le2O
\tag{10.3}
\]

is known for them with constants uniform in the load magnitude.  The
quadratic penalty can be arbitrarily larger than overload: with
\(N=2,\rho=0,\mu=(2c,0)\), one has \(O=c\) but unweighted half floor energy
\(c^2\).  Thus among the tested separable choices, the corridor has the closest
proved quantitative relation to the required target.

This paragraph makes no uniqueness claim: an as-yet undiscovered potential
could have additional wreath-specific structure.  It records only the
scope of the established comparisons.

### 10.3 Finite-state drift cannot manufacture a low class

Changing from a deterministic potential to expected drift does not remove
the global-selection issue.

### Proposition Z3.17 — stationary obstruction to strict drift

Let \(K\) be a Markov kernel on a finite state space, let \(\pi\) be a
stationary law, and let \(V\) be any real function.  Then

\[
\boxed{
\sum_x\pi(x)[KV(x)-V(x)]=0.
}
\tag{10.4}
\]

In particular, \(KV<V\) cannot hold at every state in the support of
\(\pi\).

#### Proof

Stationarity gives

\[
\sum_x\pi(x)KV(x)
=\sum_y(\pi K)(y)V(y)
=\sum_y\pi(y)V(y).
\]

Subtracting proves (10.4).  \(\square\)

Thus a scalar potential with strict expected descent outside a proposed
low set already forces every closed stationary class to meet that set.
Adding a Poisson coboundary \((I-K)h\) cannot evade the condition, because
its stationary mean is zero.  In the exact-factor heat route, this is the
same unresolved class-selection content in different notation; it is not a
new proof of a low-overload factor.

### 10.4 Group-component products give a different macro-neighborhood,
not an unconditional potential

The independently audited finite-group construction has the following
relevant scope.  A coordinate group \(\Gamma\le S_n\) partitions an exact
factor into ownership components, and independently translating complete
components by group elements always produces another exact factor.  The
exact group-Haar identity says that optimal floor-energy descent in this
product is governed by the difference between the removable Haar energy
and the optimal correlated residual.  No theorem presently forces that
difference to be positive above the required scale.  If \(\Gamma\) is
transitive on middle sets, the ownership graph is one block and the product
contains only whole-factor relabellings.  Static two-transposition
rectangles also collapse, for \(n\ge5\), to ordinary one-transposition
partial-support trades.

These are previously audited exact statements.  The missing positive
Haar-versus-residual inequality is **unproved**.  Hence group products do
not supersede the atomic/cancellation theorem, and the latter does not prove
the missing group inequality.

## 11. Exact implication scope

Fix \(A>0\) and let

\[
H_A=\min\{m-1,\lceil A\sqrt m\rceil\}.
\tag{11.1}
\]

The proved implication chain is

\[
\boxed{
\min_{F\in\mathcal X_m}\mathcal C_{H_A}(F)=o(W)
\iff
\min_{F\in\mathcal X_m}
\sum_{q\le H_A}\frac{O_q(F)}{c_q}=o(W).
}
\tag{11.2}
\]

For every fixed \(A\), the right side is the small unlabelled overload
statement which, under the frozen diagonalization theorem, is equivalent to
MWB.  Equation (11.2) is therefore a valid replacement target for that
unlabelled route.

The exchange results prove only

\[
\begin{aligned}
&\text{atomic/cancellation-connected local optimum of }\mathcal C_{H_A}\\
&\hspace{35mm}=
\text{global optimum of }\mathcal C_{H_A}.
\end{aligned}
\tag{11.3}
\]

They do not estimate the common value in (11.3).  In particular, none of
the following is proved:

1. \(C_{H_A}^*=o(W)\);
2. an \(o(W)\) cancellation budget in Theorem Z3.11;
3. an \(o(B)\), bounded, or polynomially recognizable atomic packet in the
   genuine wreath fibre;
4. a genuine exact-factor example of a nonglobal single-component local
   minimum for corridor or the fixed-window floor energy;
5. labelled common-owner synchronization; or
6. a literal contiguous-OR word.

The neighbourhood theorem is unlabelled and remains wholly inside a single
exact middle factor at every step.  It neither changes owner resolutions
independently across depths nor invokes the stronger labelled
synchronization statement.

## 12. Independent audit of the decisive step

The atomic-packet argument and its constants were checked independently
against the positive-fibre overlay criterion.  The audit points are
recorded explicitly.

1. **Cut inequality direction.**  Non-atomic means that some cut has
   \(\eta_F\ge0\), hence
   \(\Delta_F(J)\ge\Delta_F(I)+\Delta_F(J\setminus I)\).  Starting from
   \(\Delta_F(\mathcal K)=-g\) therefore gives
   \(\sum_P\Delta_F(P)\le-g\), so an atomic leaf has change at most
   \(-g/t\).  The sign in (3.9) is correct.

2. **Gap divisor.**  Recursive leaves partition the original ownership
   components, so \(t\le|\mathcal K(F,G)|\).  Every nonempty component
   contains at least one wreath of \(F\setminus G\), giving
   \(|\mathcal K(F,G)|\le|F\setminus G|\le B\).  No unbounded general
   Graver-decomposition length enters the constant.

3. **Positive-fibre legality.**  Every recursive leaf is a union of complete
   ownership components.  Equation (1.3), not a signed relaxation, proves
   that all asserted endpoints are integral exact factors.

4. **Primitive implication.**  A proper conformal lifted submove must have
   wreath projection equal to a proper component union \(I\).  The condition
   \(v_I\sqsubseteq v_J\) makes \(v_I\) and \(v_J-v_I\) same-sign in each
   coordinate, so discrete convexity forces \(\eta_F\ge0\), contradicting
   atomicity.  This proves atomic \(\Rightarrow\) augmented primitive; the
   converse was nowhere used or asserted.

5. **Floor specialization.**  The only linear-term subtlety is the shift
   from \(c_q+1/2\) to \(W/N_q\).  Every feasible rank effect has coordinate
   sum zero, so the shift contributes zero.  The mixed term is exactly
   \(\langle v_I,v_L\rangle_H\), with no missing factor \(1/2\).

6. **Corridor constants.**  Conservation gives
   \(D^-=T-\rho\) and \(D^+=T-p\), whence
   \(2O=C+|p-\rho|\).  Thus the constants \(1\) and \(2\) in (2.7) are
   correct and survive summation and minimization.

7. **Scope audit.**  The abstract large-packet construction is not labelled
   wreath-realizable; the Z2 two-component packet proves structural
   strictness but not improvement; and the envelope potential is nonlocal
   and circular.  None is used to claim MWB.

No finite search, certificate data, or fractional-factor surrogate is used
in any proof in this report.

## 13. Final theorem-level verdict

The strongest noncircular conclusion of lane Z3 is:

> The free-quota corridor is a separable discrete-convex exact-factor
> potential equivalent to mobile overload within factor two.  Its
> objective-atomic feasible augmented Graver packets form an exact test set.
> Equivalently, the more explicit cancellation-connected macro-neighborhood
> has no nonglobal local minima.  For floor energy, atomicity reduces to the
> cutwise negative Gram condition (5.5).  Every better endpoint yields such
> an improving packet with at least a \(1/\operatorname{Cat}_m\) fraction of
> the endpoint gap.

This is a genuine enlarged-neighborhood exchange descent theorem on the
positive exact-factor fibre.  The route is nevertheless macro-local:
packet size is uncontrolled, and the global corridor minimum is
unestimated.  A wreath-specific small-packet theorem or an \(o(W)\)
cancellation-residue bound would make the descent/locality statement more
effective, but neither alone would bound the optimum.  For MWB the decisive
remaining assertion is still
\(C_{H_A}^*=o(W)\) for every fixed \(A\).  All of these possible
strengthenings remain unproved.
