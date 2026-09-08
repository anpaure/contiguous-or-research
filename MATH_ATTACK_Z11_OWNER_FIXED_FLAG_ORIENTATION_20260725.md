# Owner-fixed flag rerouting: the exact orientation split, local dual, and run price

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or certificate is used.

## 0. Verdict

Fix a family of lower-owner incidences and give every incidence two literal
flag realizations. There are two different discrete-convex objects, and they
must not be conflated.

1. At one fixed depth, after forgetting owner labels, the possible load
   vectors are indegree vectors of a multigraph orientation. This load set is
   (M)-convex. The floor energy is (M)-convex on it, directed-path reversal
   is an exact local/global test, and residual reachability gives exact
   deficit and surplus cut certificates.
2. On the genuine owner-decorated choice fibre, the same binary owner choice
   controls every depth. On this partition-base domain an (M)-convex
   function must be modular across distinct owners. For the half floor
   energy the mixed coefficient of owners (i,j) is exactly

   \[
   \langle d_i,d_j\rangle_w.
   \]

   Therefore the synchronized floor energy is (M)-convex if and only if
   all distinct owner innovations are weighted-orthogonal. Genuine
   owner-fixed common-target spikes have

   \[
   \langle d_i,d_j\rangle_w\ge w_q>0,
   \]

   and give a strict literal obstruction.
3. The physical run term is not a harmless linear regularizer. If (J) is
   the number of labelled source-row runs, a run of (s) owners has exact
   literal length (s+2H), so the exact scalarized defect is

   \[
   \mathscr F_H=\Psi_H+2HJ.
   \]

   The row-boundary functional (J) itself violates (M)-exchange on a
   genuine four-owner chart even when the floor energy is modular.
4. There is nevertheless an exact local-minimum dual. For every legal packet
   (T), with total flag displacement (D_T),

   \[
   \Delta_T\Psi_H
   =\left\langle D_T,\mu-c-\frac12\mathbf1\right\rangle_w
    \frac12\|D_T\|_w^2,
   \]

   and a local minimum of \(\mathscr F_H\) satisfies

   \[
   -\Delta_T\Psi_H\le 2H B_x(T),
   \]

   where (B_x(T)) is the exact carrier-boundary charge and
   (B_x(T)\le2|T|).
5. Consequently, a packet cover which corrects (D) distinct simple
   diffuse surplus units, has weighted cross-depth restitution (R), and
   total carrier charge (B), obeys

   \[
   \frac{D}{C_A}\le R+2HB,
   \qquad
   C_A=\max_{|q|\le A\sqrt m}c_q=O_A(1).
   \]

   Thus (R=o(W)) and (B=o(W/H)) would force (D=o(W)). This is a
   quantitatively strong certificate, but its antecedent is precisely a
   collar-clean diffuse packet theorem.
6. The generic owner-incidence and row-boundary axioms do not imply that
   antecedent. An exact integral orientation/run catalogue can have
   \(\Theta(W)\) floor energy and (J=O(W/m)), while every correcting atom
   creates exactly two runs. This catalogue is not asserted to be the flag
   atlas of one positive wreath factor; it proves that a wreath-specific
   crossing-seam theorem is indispensable.

The strongest concrete enlarged neighbourhood left by this analysis is an
order-coherent paired-row interval move. A whole paired run has zero run
increase, and an interval has carrier charge at most two. No theorem is
proved which packs the actual diffuse wreath collisions into
(o(W/H)) such boundaries with (o(W)) cross-depth restitution. Hence no
constant-one conclusion is claimed.

---

## 1. Exact owner-decorated orientation model

Let \(\mathcal A\) be a finite set of signed depths. For each
\(a\in\mathcal A\), let \(V_a\) be its target layer, let (c_a\) be its
integer floor, and let (w_a>0). In the fixed-Gaussian wreath application
one takes (w_a=1/c_a); throughout the full-word application all the
relevant (c_a)'s are positive. If an autonomous partial token core has
some (c_a=0), the identities below remain valid with an arbitrary positive
weight, but statements which divide by (c_a) are omitted.

Let (I) be a set of fixed lower-owner incidences. Owner (i\in I) has
two support-feasible literal realizations. At depth (a), their targets are

\[
p_{i,a}^0,p_{i,a}^1\in V_a.
\]

Both realizations have exactly the same designated lower target and middle
owner. This is the legality condition which makes arbitrary simultaneous
choices a central matching. Put

\[
a_i^\epsilon
=\bigoplus_{a\in\mathcal A}\delta_{p_{i,a}^\epsilon},
\qquad
d_i=a_i^1-a_i^0.
\tag{1.1}
\]

Every (d_i) has coordinate sum zero separately in each depth block. With
a fixed background load (b), a corner (x\in\{0,1\}^I) has load

\[
\mu(x)
=b+\sum_{i\in I}\bigl((1-x_i)a_i^0+x_i a_i^1\bigr)
=\mu(0)+\sum_{i\in I}x_i d_i.
\tag{1.2}
\]

Define the half floor polynomial

\[
\phi_c(t)=\frac12(t-c)(t-c-1)
\tag{1.3}
\]

and the weighted energy

\[
\boxed{
\Psi(x)
=\sum_{a\in\mathcal A}w_a
  \sum_{v\in V_a}\phi_{c_a}(\mu_{a,v}(x)).
}
\tag{1.4}
\]

The half normalization is used throughout this report. Doubling every
formula gives the doubled factorial-floor convention.

### Lemma 1.1 -- exact quadratic expansion

Put

\[
\langle u,v\rangle_w
=\sum_{a\in\mathcal A}w_a\langle u_a,v_a\rangle_2.
\tag{1.5}
\]

Then

\[
\boxed{
\Psi(x)
=\Psi(0)+\sum_i h_i x_i
  \sum_{i<j}\langle d_i,d_j\rangle_w x_i x_j,
}
\tag{1.6}
\]

where

\[
h_i
=\left\langle\mu(0)-c-\frac12\mathbf1,d_i\right\rangle_w
 +\frac12\|d_i\|_w^2.
\tag{1.7}
\]

For a packet (T\subseteq I), orient every (d_i), (i\in T), from
its current realization to its alternate realization and put

\[
D_T=\sum_{i\in T}d_i.
\]

Then

\[
\boxed{
\Delta_T\Psi
=\left\langle\mu-c-\frac12\mathbf1,D_T\right\rangle_w
 +\frac12\|D_T\|_w^2.
}
\tag{1.8}
\]

Because every depth block of (D_T) has sum zero, the (c+\frac12)
term in (1.8) may equivalently be suppressed.

#### Proof

The scalar identity

\[
\phi_c(t+s)-\phi_c(t)
=(t-c-\tfrac12)s+\tfrac12s^2
\]

gives (1.8) after summing coordinates. Taking
(D_T=\sum_{i\in T}d_i), expanding its square, and using (x_i^2=x_i)
gives (1.6)--(1.7). \(\square\)

### Exact integral run formulation

Label every physical source-row piece and linearly order its positions after
the initialization cut. Let (y_{r,s}(x)\in\{0,1\}) indicate whether
position (s) of row (r) is used by corner (x). A candidate position is
fixed, equals (x_i), or equals (1-x_i). Put (y_{r,0}=0), and introduce
binary run-start variables (z_{r,s}) satisfying

\[
\begin{aligned}
z_{r,s}&\ge y_{r,s}-y_{r,s-1},\\
z_{r,s}&\le y_{r,s},\\
z_{r,s}&\le1-y_{r,s-1}.
\end{aligned}
\tag{1.9}
\]

Then

\[
\boxed{J(x)=\sum_{r,s}z_{r,s}}
\tag{1.10}
\]

is exactly the number of selected labelled row runs. Together,
(1.2), (1.9), the binary owner equations, and the fixed matching
incidences form an exact integral orientation formulation. No fractional
owner or flag is introduced.

The audited two-sided literalizer writes a run of (s) principal owners in
exact length (s+2H). Thus a corner with (M) principal owners has literal
length

\[
\boxed{M+2HJ(x).}
\tag{1.11}

The relevant scalarized local objective is therefore

\[
\boxed{\mathscr F_H(x)=\Psi(x)+2HJ(x).}
\tag{1.12}

---

## 2. Exact (M)-convexity criterion on owner choices

Encode the two choices of owner (i) by

\[
y_{i,0}+y_{i,1}=1,
\qquad y_{i,\epsilon}\in\{0,1\}.
\tag{2.1}
\]

The domain

\[
\mathcal B_I
=\left\{y\in\{0,1\}^{I\times\{0,1\}}:
 y_{i,0}+y_{i,1}=1\ (i\in I)\right\}
\tag{2.2}
\]

is the base family of a partition matroid. Extend \,\(\Psi\) by
(+\infty) off \(\mathcal B_I\).

### Theorem 2.1 -- owner-decorated (M)-convexity is exactly modularity

The weighted half floor energy is (M)-convex on \(\mathcal B_I\) if and
only if

\[
\boxed{
\langle d_i,d_j\rangle_w=0
\qquad(i\ne j).
}
\tag{2.3}
\]

Equivalently, on the full owner-decorated domain, an (M)-convex route
objective has no interaction between distinct owners.

#### Proof

Fix distinct owners (i,j) and fix all other choices. Write
(\Psi_{\alpha\beta}\) for the four corners on these two bits. Lemma 1.1
gives the rectangle identity

\[
\boxed{
\Psi_{00}+\Psi_{11}-\Psi_{10}-\Psi_{01}
=\langle d_i,d_j\rangle_w.
}
\tag{2.4}
\]

Apply the (M)-exchange axiom to the two bases (00,11). If the selected
atom of owner (i) is exchanged, feasibility forces the receiving atom to
be the other atom of the same owner: using an atom from a different
partition block would leave one block empty and another doubled. Hence

\[
\Psi_{00}+\Psi_{11}\ge\Psi_{10}+\Psi_{01},
\]

so the right side of (2.4) is nonnegative.

Apply the same axiom to (01,10). It gives the reverse inequality, so the
right side is nonpositive. Thus every mixed Gram coefficient vanishes.

Conversely, if all mixed Gram coefficients vanish, (1.6) is a sum of
one-owner functions. The forced paired exchange merely swaps the two
one-owner values between the compared bases, and the exchange inequality
holds with equality. \(\square\)

### Corollary 2.2 -- genuine owner-fixed spike obstruction

Suppose two owner-fixed upper spikes share their old depth-(q) target.
The spike construction fixes the designated lower-owner incidences and all
lower flags. Every old upper target avoids the omitted source pair, every
nonzero image meets it, and the two old depth-(q) targets coincide.
Therefore

\[
\langle d_i,d_j\rangle_w
\ge w_q>0.
\tag{2.5}
\]

The synchronized weighted floor energy is not (M)-convex on this literal
four-corner fibre. The same conclusion holds for the lower owner-fixed
spike at every depth where that chart is defined.

This obstruction survives any nonnegative physical run coefficient if the
two route options are treated as separately labelled singleton row pieces:
every corner then has the same number of runs. This is a literal
post-selection chart, not a switch inside one preassigned exact factor.

#### Proof

At the common target, both innovations contain the same negative unit.
No old target can equal a nonzero image target because the former avoids
the omitted pair and the latter meets it. Hence the depth-(q) inner
product is at least one; all weights are nonnegative. Theorem 2.1 applies.
Singleton labelling makes (J=|I|) on every corner, so it adds only a
constant. \(\square\)

### A second domain obstruction

If one owner rerouting changes flags at two or more depths, then the two
joint load vectors differ in \(\ell^1\)-distance at least four. The
two-point joint-load image is not an (M)-convex set: a required unit
exchange produces an intermediate vector which is neither endpoint. Thus
even projecting away owner labels does not restore (M)-convexity when the
depths remain diagonally synchronized.

---

## 3. The positive one-depth quotient

The preceding failure does not contradict the following exact theorem.
Fix one depth, suppress its index, and let (G=(V,E)) be the multigraph in
which owner (i) is the edge joining (p_i^0,p_i^1). Orient every edge
from its unchosen target to its chosen target. With fixed background load
(b\in\mathbb Z_+^V),

\[
\mu_v=b_v+\operatorname{indeg}_G(v).
\tag{3.1}
\]

Write (E(S)) for the multiset of edges with both endpoints in (S), and
\(\delta(S)\) for the crossing multiset.

### Theorem 3.1 -- graphical loads form an (M)-convex set

The feasible one-depth load set is exactly

\[
\boxed{
\begin{aligned}
\mathcal D_G=\{\mu\in\mathbb Z^V:\quad
&\mu(V)=b(V)+|E|,\\
&\mu(S)\ge b(S)+|E(S)|\quad(S\subseteq V)\}.
\end{aligned}}
\tag{3.2}
\]

It is (M)-convex. If every \(\varphi_v:\mathbb Z\to\mathbb R\) is
discrete convex, then

\[
\sum_v\varphi_v(\mu_v)+\delta_{\mathcal D_G}(\mu)
\tag{3.3}
\]

is an (M)-convex function. In particular this holds for the one-depth
floor energy.

#### Proof

Every internal edge of (S) contributes one chosen endpoint in (S),
which proves necessity of the lower cut inequalities. Conversely, these
are the standard orientation cuts; a direct max-flow construction sends
one unit from each edge-node to one of its two endpoint nodes with demands
\(\mu_v-b_v\). The only finite cuts are exactly (3.2), so integral max-flow
gives an orientation.

For the exchange axiom, take orientations with loads \(\mu,\nu\). Direct
every edge on which they differ from its chosen endpoint in the
\(\nu\)-orientation to its chosen endpoint in the \(\mu\)-orientation.
The divergence of this difference digraph is \(\mu-\nu\). If
\(\mu_u>\nu_u\), a directed path ends at (u) and begins at some (v)
with \(\mu_v<\nu_v\). Reversing the choices on this path in both
orientations, in opposite directions, realizes

\[
\mu-e_u+e_v,
\qquad
\nu+e_u-e_v.
\]

Discrete convexity at coordinates (u,v), using
\(\mu_u>\nu_u\) and \(\mu_v<\nu_v\), gives the (M)-exchange inequality
for (3.3). \(\square\)

### Theorem 3.2 -- residual-path and exact cut dual

Fix an orientation and direct each residual edge from its unchosen target
to its chosen target. Reversing a directed path (u\leadsto v) transfers
one load unit from (v) to (u). For constant floor (c) and weight
(w>0), its half-floor change is

\[
\boxed{w(\mu_u-\mu_v+1).}
\tag{3.4}
\]

Therefore the orientation globally minimizes the one-depth floor energy if
and only if there is no directed path (u\leadsto v) with

\[
\mu_v\ge\mu_u+2.
\tag{3.5}
\]

At such an optimum define

\[
L_- =\{v:\mu_v\le c-1\},
\qquad
R_-=\operatorname{Reach}(L_-).
\tag{3.6}
\]

Then (R_-) is forward closed, contains every deficit vertex, contains
only vertices of load at most (c), and

\[
\boxed{
D^-
:=\sum_v(c-\mu_v)_+
=c|R_-|-b(R_-)-|E(R_-)|-|\delta(R_-)|.
}
\tag{3.7}
\]

Similarly put

\[
R_0=\operatorname{Reach}\{v:\mu_v\le c\},
\qquad
C_+=V\setminus R_0.
\tag{3.8}
\]

Then (C_+) contains every vertex of load at least (c+2), contains only
vertices of load at least (c+1), receives no chosen boundary edge, and

\[
\boxed{
D^+
:=\sum_v(\mu_v-c-1)_+
=b(C_+)+|E(C_+)|-(c+1)|C_+|.
}
\tag{3.9}
\]

#### Proof

On a path, every internal load change cancels. The initial vertex gains one
and the terminal vertex loses one. Since

\[
\phi_c(t+1)-\phi_c(t)=t-c,
\qquad
\phi_c(t-1)-\phi_c(t)=c+1-t,
\]

their sum is (3.4). The local/global equivalence follows from Theorem 3.1.

If a vertex reachable from (L_-) had load at least (c+1), a suffix of
the path from a deficit vertex to it would violate (3.5). Hence
\(\mu\le c\) on (R_-). Forward closure says every crossing edge points
into (R_-), so

\[
\mu(R_-)=b(R_-)+|E(R_-)|+|\delta(R_-)|.
\]

All and only deficit mass lies in (R_-), proving (3.7).

The same argument shows that (R_0) contains no load at least (c+2).
Every load at most (c) is a seed, so (C_+) contains only loads at least
(c+1). No crossing edge has its chosen endpoint in (C_+), whence

\[
\mu(C_+)=b(C_+)+|E(C_+)|.
\]

Subtracting ((c+1)|C_+|) proves (3.9). \(\square\)

### Corollary 3.3 -- bounded diffuse energy is a cut-slack question

Assume every positive deficit depth and surplus height is at most (K):

\[
(c-\mu_v)_+\le K,
\qquad
(\mu_v-c-1)_+\le K.
\]

For weight (1/c),

\[
\boxed{
\frac{D^-+D^+}{c}
\le\Psi_q
\le\frac{K+1}{2c}(D^-+D^+).
}
\tag{3.10}
\]

Thus one-depth cut slacks (o(W/K)) imply (o(W)) floor energy, and cut
slacks (o(W)) already imply (o(W)) mobile overload. What is missing in
the synchronized problem is not this duality: a real owner rerouting uses
the same bit at several depths, and the projection graphs need not share
their directed paths or even their connected components.

---

## 4. Exact physical run calculus and a second exchange obstruction

For a selected vertex set (S) in a labelled row path,

\[
J_r(S)=|S|-e_r(S),
\tag{4.1}
\]

where (e_r(S)) is the number of row adjacencies induced by (S). For a
cyclic source row the same formula holds for a proper nonempty subset, and
a full selected cycle contributes one run; after the literal initialization
cut it is one linear run.

### Lemma 4.1 -- carrier-boundary inequality

Let (x^T) be obtained by toggling a support-feasible packet (T). For
each labelled row (r), let (S_r(x)) be its selected positions and put

\[
B_x(T)
=\sum_r J_r\bigl(S_r(x)\mathbin\triangle S_r(x^T)\bigr).
\tag{4.2}
\]

Then

\[
\boxed{
|J(x^T)-J(x)|\le B_x(T)\le2|T|.
}
\tag{4.3}
\]

For one owner flip, if (d_{\rm old}) is the selected-neighbour degree of
the deleted old position and (d_{\rm new}) is the selected-neighbour
degree at the new position just before insertion, then, apart from the
explicit full-cycle correction,

\[
\Delta J=d_{\rm old}-d_{\rm new},
\qquad |\Delta J|\le2.
\tag{4.4}
\]

#### Proof

On the zero-extended linear row, twice the run count is the total variation
of its selection word. The boundary word of (S\triangle T) is the XOR of
the boundary words, so the triangle inequality gives

\[
|J_r(S)-J_r(T)|\le J_r(S\triangle T).
\]

Sum over rows. A toggled owner contributes one deleted and one inserted
carrier vertex, so the carrier contains at most (2|T|) vertices and hence
at most (2|T|) runs. Formula (4.4) follows directly from (4.1): deletion
changes the run count by (d_{\rm old}-1), while insertion changes it by
(1-d_{\rm new}). \(\square\)

### Proposition 4.2 -- the run penalty itself violates (M)-exchange

Fix (1\le H\le m-2). Take four consecutive owner occurrences in one
omitted-pair source row. For occurrence (i), use the owner-fixed upper
spike distinguished at depth (H), map its entering coordinate to one
common omitted-pair marker, and place its alternate occurrence in a private
conjugate labelled row.

All lower flags and all upper flags at depths below (H) are fixed. At
depth (H), the four old targets are distinct, the four image targets are
distinct, and an old target avoids the omitted pair while an image contains
the marker. Hence all pairwise weighted Gram products vanish and the floor
energy is modular on these four bits.

Restrict to corners switching exactly two owners. With (x=1100) and
(y=0011),

\[
J(x)+J(y)=3+3=6.
\]

For the (M)-exchange requested at the second coordinate, the only two
receiving choices give respectively

\[
(1010,0101):\quad J=4+4,
\]

and

\[
(1001,0110):\quad J=3+4.
\]

Both violate the (M)-exchange inequality. Therefore

\[
\boxed{\Psi+\lambda J\text{ is not (M)-convex for any }\lambda>0}
\tag{4.5}

on this genuine owner-fixed literal chart.

#### Proof

If (U_H(i)) is the old upper flag and (b_i) its entering coordinate,
the image flag is

\[
V_i=U_H(i)-b_i+a_1=U_{H-1}(i)+a_1.
\]

Proper cyclic windows at distinct starts are distinct, so both the old
family and image family are injective. The omitted-pair marker separates
the two families. Thus every mixed floor coefficient is zero.

For the run count, every switched owner is a private singleton run. The
unswitched owners among the four old consecutive positions contribute one
run when consecutive and two when separated. The displayed values follow.
The floor's modular terms cancel in every paired exchange, leaving the
strict run inequalities. \(\square\)

Each route in Proposition 4.2 is integral in its own exact-factor row copy,
and the final concatenation is literal. The proposition is not an
exact-factor-fibre switch theorem; it is a theorem about the owner-fixed
post-selection rerouting model posed here.

---

## 5. The exact packet-local dual

Let \(\mathcal N(x)\) be any family of support-feasible owner packets at a
corner (x). No closure under arbitrary subsets is assumed.

### Theorem 5.1 -- penalized reduced-cost certificate

If (x) is a local minimum of \(\mathscr F_H=\Psi+2HJ\) under
\(\mathcal N(x)\), then every (T\in\mathcal N(x)) satisfies

\[
\boxed{
\left\langle\mu-c-\frac12\mathbf1,D_T\right\rangle_w
 +\frac12\|D_T\|_w^2
 +2H\bigl(J(x^T)-J(x)\bigr)\ge0.
}
\tag{5.1}
\]

In particular,

\[
\boxed{-\Delta_T\Psi\le2H B_x(T).}
\tag{5.2}
\]

#### Proof

Equation (5.1) is Lemma 1.1 plus local minimality. Rearranging and applying
Lemma 4.1 gives

\[
-\Delta_T\Psi
\le2H\bigl(J(x^T)-J(x)\bigr)
\le2HB_x(T).
\]

\(\square\)

### Corollary 5.2 -- one simple restitution packet

Fix a depth (q) with weight (1/c_q). Suppose a legal packet transfers
(D) distinct units from (D) distinct targets of load (c_q+2) to
(D) distinct targets of load (c_q), leaving both at load (c_q+1).
Suppose its total weighted floor increase at all other depths is at most
(R). Then a local minimum obeys

\[
\boxed{
\frac{D}{c_q}\le R+2H B_x(T).
}
\tag{5.3}

#### Proof

At one corrected pair,

\[
\phi_{c_q}(c_q+2)+\phi_{c_q}(c_q)
-2\phi_{c_q}(c_q+1)=1.
\]

Thus the selected depth improves by exactly (D/c_q), while the other
depths cost at most (R). Apply (5.2). \(\square\)

### Theorem 5.3 -- fractional packet-cover certificate

Let \(T_s\in\mathcal N(x)\), let \(\lambda_s\ge0\), and suppose packet
(T_s) services (L_s) simple diffuse units. Assume

\[
-\Delta_{T_s}\Psi\ge\frac{L_s}{C_A}-R_s,
\tag{5.4}
\]

where (R_s\ge0) is its restitution/collateral charge, and

\[
\sum_s\lambda_sL_s\ge D.
\tag{5.5}
\]

Then every packet-local minimum satisfies

\[
\boxed{
\frac{D}{C_A}
\le\sum_s\lambda_sR_s
 +2H\sum_s\lambda_sB_x(T_s).
}
\tag{5.6}
\]

For a fixed Gaussian window, (C_A=O_A(1)). Hence

\[
\sum_s\lambda_sR_s=o(W),
\qquad
\sum_s\lambda_sB_x(T_s)=o(W/H)
\tag{5.7}
\]

force (D=o(W)).

#### Proof

Apply (5.2) to every packet, combine it with (5.4), multiply by
\(\lambda_s\), and sum. For \(|q|\le A\sqrt m\), the exact binomial ratio
(W/N_q) is a product of (O_A(\sqrt m)) factors whose logarithms sum to
(O_A(q^2/m)=O_A(1)). Thus all floors (c_q\) are bounded by a constant
depending only on (A). \(\square\)

Theorem 5.3 is not tautological full-Graver closure. Its packets are concrete
support-feasible reroutings, and it requires only a fractional cover by
them. Its unproved antecedent is a geometric packet construction with both
small row boundary and small synchronized spill.

---

## 6. What the dual proves and what it cannot prove

### Proposition 6.1 -- exact deepest-fibre threshold

At the deepest selected upper depth (q=H), take a complete old collision
fibre of (t) owner-fixed spike occurrences at a target (U), assume
\(\mu_H(U)=t\), and choose distinct image targets (V_1,\ldots,V_t\).
There is no deeper spill. Switching the whole fibre has exact half-floor
change

\[
\boxed{
\Delta\Psi_H
=\frac{\sum_{i=1}^t\mu_H(V_i)-\binom t2}{c_H}.
}
\tag{6.1}

At a local minimum,

\[
\boxed{
\binom t2
\le\sum_{i=1}^t\mu_H(V_i)+2Hc_HB_x(T)
\le\sum_{i=1}^t\mu_H(V_i)+4Hc_Ht.
}
\tag{6.2}

If every image load is at most (b), this yields only

\[
\boxed{t\le2b+8Hc_H+1.}
\tag{6.3}

Thus the physical price rules out very concentrated fibres, but it gives no
control on multiplicities (2,\ldots,O(Hc_H)), exactly the diffuse sector.

#### Proof

Removing all (t) units from (U), and adding one to each distinct image,
changes the unweighted half floor by

\[
\sum_i\mu_H(V_i)-t\mu_H(U)+\binom{t+1}{2}
=\sum_i\mu_H(V_i)-\binom t2.
\]

Divide by (c_H), apply (5.2), and use (B_x(T)\le2t). Dividing (6.2)
by (t>0) proves (6.3). \(\square\)

### Proposition 6.2 -- incidence-only diffuse trap

Fix integers (c,H\ge1). For every sufficiently large (N) and every
(D<N/2), there is an integral two-route orientation/run catalogue with
floor (c), total mass (cN+D), and (D) independent correcting owners
such that, for a switched set (A\),

\[
\boxed{
\Psi(A)=\Psi(\varnothing)-\frac{2|A|}{c},
\qquad
J(A)=J(\varnothing)+2|A|.
}
\tag{6.4}

Consequently

\[
\mathscr F_H(A)-\mathscr F_H(\varnothing)
=|A|\left(4H-\frac2c\right)>0
\tag{6.5}

for every nonempty (A). If (D=\Theta(N)), then
\(\Psi(\varnothing)=\Theta(N)). The old occurrences and their fixed
background can be packed into (O(N/m)) long labelled rows, so

\[
J(\varnothing)=O(N/m)=o(N/H)
\]

whenever (H=o(m)). Nevertheless every corner with only (o(N/H)) new
runs corrects only (o(N/H)) atoms and retains \(\Theta(N)\) floor energy.

#### Proof

Choose disjoint target pairs \((u_i,v_i)\), (1\le i\le D), with initial
loads

\[
\mu(u_i)=c+2,
\qquad
\mu(v_i)=c-1.
\]

Put every other target at load (c). The total load is

\[
D(2c+1)+c(N-2D)=cN+D.
\]

Owner (i) moves one occurrence from (u_i) to (v_i), changing the pair
to \((c+1,c)\). Its weighted half-floor improvement is

\[
\frac1c\left(phi_c(c+2)+\phi_c(c-1)ight)=\frac2c.
\]

Place every movable old occurrence at a pairwise nonadjacent interior
position of a long selected old row, with immutable selected positions on
both sides, and put its alternate at a private empty labelled row position.
Deleting the old occurrence splits one run into two; inserting the alternate
creates one singleton run. Nonadjacency makes these changes additive, so
(6.4) holds. The remaining statements follow immediately. \(\square\)

Proposition 6.2 is an exact integral counterexample to any theorem using
only fixed incidences, target loads, and the generic row-boundary ledger.
It is **not** claimed to embed into one exact wreath factor, or even into a
coordinate-window flag atlas. It therefore does not refute MWB or the
contiguous-OR conjecture. It proves that a successful dual argument must use
additional wreath geometry which creates shared crossing seams.

---

## 7. A concrete stronger move set

The run obstruction identifies the correct enlargement. Suppose owners
\(1,\ldots,\ell\) occur consecutively in one old labelled row and their
alternate occurrences occur consecutively, in the same order, in one
alternate labelled row. Let (x_i=1) choose the alternate. Apart from fixed
outside endpoint terms, the two-row run count is exactly

\[
\boxed{
J(x)=1+\sum_{i=1}^{\ell-1}\mathbf1_{\{x_i\ne x_{i+1}\}}.
}
\tag{7.1}

Hence:

1. flipping a contiguous owner interval has carrier charge at most two;
2. its run change has absolute value at most two; and
3. flipping the whole paired run has \(\Delta J=0\).

These moves are not the tautological full-Graver closure. They are literal
order-coherent paired-row interval reversals. Combining (7.1) with Theorem
5.3 gives the following exact sufficient statement.

> **Paired-row packet gate.** If the fixed-Gaussian diffuse surplus units
> admit a fractional cover by support-feasible order-coherent paired-row
> intervals whose total cross-depth restitution is (o(W)) and whose total
> carrier boundary is (o(W/H)), then every local minimum under those
> interval moves has (o(W)) serviced diffuse floor defect. Together with
> an (o(W)) bound for the unserviced remainder, it yields the required
> floor estimate while adding only (o(W)) literal run overhead.

The proof is exactly Theorem 5.3. The missing content is existence of the
paired rows with common order, support feasibility, and a cover of the
actual upper and lower collision atoms. Fixed lower-owner incidences alone
do not provide any of those three properties.

---

## 8. Exact proved/conditional boundary

### Proved

1. The single-depth indegree-load quotient is (M)-convex, with exact
   residual-path optimality and the cut certificates (3.7), (3.9).
2. The synchronized owner-decorated weighted floor is (M)-convex only in
   the pairwise-orthogonal, hence modular, case.
3. Genuine owner-fixed common-target spike atoms violate that criterion.
4. The exact physical objective is \(\Psi+2HJ\), the carrier inequality is
   \(|\Delta J|\le B\le2|T|\), and the packet dual (5.1)--(5.2) is exact.
5. A low-restitution, low-boundary packet cover gives the quantitative
   diffuse bound (5.6).
6. The universal physical price alone sees only load gaps of order (Hc_q),
   as quantified by (6.2)--(6.3).
7. Fixed-incidence orientation data alone admit the macroscopic diffuse trap
   of Proposition 6.2.
8. Order-coherent paired-row interval moves have (O(1)) carrier boundary,
   and whole paired-run reversal has zero run increase.

### Not proved

1. No exact wreath counterexample with macroscopic diffuse floor energy is
   constructed.
2. No theorem supplies the necessary paired-row packet cover inside the
   positive pair-omission or exact-factor geometry.
3. No (o(W)) restitution estimate is proved for a positive-density family
   of such packets.
4. Therefore neither fixed-window MWB nor the constant-one contiguous-OR
   theorem follows here.

The lane is decisively closed for generic owner-decorated (M)-convexity.
Its non-tautological surviving form is the paired-row packet gate, not a
standard discrete-exchange axiom.
