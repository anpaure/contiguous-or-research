# Eighth-wave AB: adaptive multibridge cages and an exact escape-depth obstruction

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, computer
algebra, or numerical experiment is used. Every state below is a literal
integral exact middle wreath factor, and every transition is a complete cut of
freshly recomputed ownership components.

Status: theorem-level obstruction. The unrestricted theorem with quantifiers

\[
\forall F\ \exists\text{ a productive unrestricted adaptive multibridge
schedule}
\]

is not proved or disproved. What is proved is a strict strengthening of the
one-prescribed-overlay obstruction: one exact factor can lock a
Gaussian-sized forest of distinct bridges, and indeed all full cells from a
quadratic-size bridge menu, against arbitrary adaptive histories. There is
also an exact lower bound on the number of arbitrary overlay cuts needed to
disperse the protected collision pile after leaving that menu.

---

## 0. Verdict

Fix \(A>0\), and put

\[
n=2m+1,\qquad W=\binom nm,\qquad B=\operatorname{Cat}_m=\frac Wn,
\qquad H=\lceil A\sqrt m\rceil .
\tag{0.1}
\]

At depth \(q\), let

\[
N_q=\binom n{m-q},\qquad
c_q=\left\lfloor\frac W{N_q}\right\rfloor,
\qquad b_q=\binom{c_q+1}{2}.
\tag{0.2}
\]

For an exact factor \(F\), let \(\Phi_q(F)\) be its undoubled factorial
collision excess above the exact adjacent-integer floor, and put

\[
\mathfrak F_A(F)=\sum_{q=1}^{H}\frac{\Phi_q(F)}{b_q}.
\tag{0.3}
\]

For every integer

\[
2\le s\le m-H-2,
\tag{0.4}
\]

the shifted MSW packet of colour \(s\) determines three disjoint coordinate
classes

\[
\mathcal I_s,\qquad \mathcal Z_s,\qquad
\{\beta_s,\gamma_s\},
\tag{0.5}
\]

with

\[
|\mathcal I_s|=s+1,\qquad
|\mathcal Z_s|=s+2H+2,
\qquad
(\beta_s\ \gamma_s)=\tau_s.
\tag{0.6}
\]

Define the bridge menu

\[
\mathcal M_s
=\binom{\mathcal I_s}{2}
 \cup\binom{\mathcal Z_s}{2}
 \cup\{\tau_s\}.
\tag{0.7}
\]

The main theorem constructs an exact factor \(G_{m,s}\) with the following
properties.

1. **Full-cell adaptive lock.** For every finite deterministic, randomized,
   or history-dependent sequence starting at \(G_{m,s}\), if every step is a
   cut of an arbitrary subset of all freshly recomputed components for some
   transposition in \(\mathcal M_s\), then the endpoint \(F_T\) satisfies

   \[
   \boxed{
   \mathfrak F_A(F_T)\ge \mathfrak F_A(G_{m,s}).
   }
   \tag{0.8}
   \]

   In particular, at the starting factor, every complete cell in the menu has
   best gain exactly zero.

2. **Many distinct fresh bridges.** The menu contains a coordinate forest of

   \[
   \boxed{2s+2H+2}
   \tag{0.9}
   \]

   distinct edges. In any ordering of those forest edges, every edge is a
   genuinely fresh bridge when first used. The whole menu has exactly

   \[
   \boxed{
   \binom{s+1}{2}+\binom{s+2H+2}{2}+1
   }
   \tag{0.10}
   \]

   transpositions.

3. **High exact floor.** With

   \[
   K_A=
   \binom{\left\lceil e^{\,2(A+1)(A+2)}\right\rceil+1}{2},
   \tag{0.11}
   \]

   one has, for all sufficiently large \(m\),

   \[
   \boxed{
   \mathfrak F_A(G_{m,s})
   >W\left(
   \frac{4^{H-s}}{2048K_A\,nH^4}-1
   \right).
   }
   \tag{0.12}
   \]

4. **Arbitrary-bridge escape depth.** Now allow the schedule to leave
   \(\mathcal M_s\) and use arbitrary transpositions. If \(F_D\) is the
   endpoint after \(D\) complete, freshly recomputed transposition-cell cuts,
   then

   \[
   \boxed{
   \frac{\mathfrak F_A(F_D)}W
   >
   \frac{2^{\,2(H-s)-D-10}}{K_A\,nH^4}
   -1-\frac1{2n}.
   }
   \tag{0.13}
   \]

   Thus an endpoint satisfying \(\mathfrak F_A(F_D)\le CW\) must obey the
   exact lower bound

   \[
   \boxed{
   D\ge
   2(H-s)-10-
   \log_2\!\left(
   K_A nH^4\left(C+1+\frac1{2n}\right)
   \right).
   }
   \tag{0.14}
   \]

Taking \(s=\lfloor H/2\rfloor\), after changing \(s\) by at most one to
ensure \(s\ge2\), gives one exact factor with all of the following
simultaneously:

\[
2s+2H+2=3H+O(1)
\tag{0.15}
\]

distinct forest-fresh locked bridges,

\[
|\mathcal M_s|=\Theta_A(m),
\tag{0.16}
\]

\[
\frac{\mathfrak F_A(G_{m,s})}{W}\longrightarrow\infty,
\qquad
\frac{\mathfrak F_A(G_{m,s})}{nW}\longrightarrow\infty,
\tag{0.17}
\]

and, for each fixed \(C<\infty\),

\[
D\ge H-3\log_2m-O_{A,C}(1)
=\Omega_A(\sqrt m)
\tag{0.18}
\]

before an arbitrary adaptive schedule can reach \(\mathfrak F_A\le CW\).

This is a genuine adaptive obstruction. It allows full recomputation and
arbitrary component subsets at every step; it is not a packet-coordinate-only
lock. It does not lock a transposition outside \(\mathcal M_s\), including
one internal to the variable region \(\mathcal R_s\) or one crossing the
displayed membership classes, and it does not rule out a spanning-tree-length
schedule with \(\Theta(m)\) stages. Selecting and controlling such an
outside-menu bridge is the precise surviving gate.

---

## 1. Exact factorial baseline and legal component cuts

Let \(F\) be an exact middle wreath factor. Its depth-\(q\) load is

\[
\mu_q^F(S)
=\#\{C\in F:S\text{ is a cyclic }(m-q)\text{-interval of }C\}.
\tag{1.1}
\]

Every factor has total depth-\(q\) load \(W\). Write

\[
W=c_qN_q+\rho_q,
\qquad 0\le\rho_q<N_q.
\tag{1.2}
\]

The exact minimum second factorial moment among all nonnegative integral
vectors of this mass is

\[
P_q^{\min}
=(N_q-\rho_q)\binom{c_q}{2}
 +\rho_q\binom{c_q+1}{2}.
\tag{1.3}
\]

Thus

\[
\Phi_q(F)
=\sum_S\binom{\mu_q^F(S)}2-P_q^{\min}\ge0.
\tag{1.4}
\]

The baseline in (1.3), rather than a fractional mean-square baseline, is
used in every estimate below.

Fix a transposition \(\sigma\). The ownership overlay of \(F\) and
\(\sigma F\) decomposes into connected components \(K\). If \(a_K\) is
the complete lower-load contribution of the old rows in \(K\), then the
new rows contribute exactly \(\sigma a_K\). Switching any collection of
complete components produces another literal integral exact factor.

### Lemma 1.1 (target-orbit invariance under full component cuts)

Let a group \(G\le S_n\) act on rank-\(r\) targets, let \(\sigma\in G\),
and let \(\mathcal O\) be a \(G\)-orbit of targets. Every complete cut of
freshly recomputed components in the \(F\)-versus-\(\sigma F\) overlay
preserves

\[
\sum_{S\in\mathcal O}\mu_r^F(S).
\tag{1.5}
\]

More particularly:

* if \(\sigma\) fixes targets \(S,T\) individually, their two loads are
  individually preserved;
* if \(\sigma\) interchanges \(S,T\), the pair total
  \(\mu(S)+\mu(T)\) is preserved.

#### Proof

For a switched component, the load change is

\[
(\sigma-I)a_K.
\tag{1.6}
\]

Because \(\sigma\mathcal O=\mathcal O\), summing (1.6) over
\(\mathcal O\) gives zero. Unswitched components contribute zero change.
The two special cases are the singleton- and two-point-orbit instances.
The argument uses the actual full component contribution; it is unaffected
by how the overlay was obtained or by earlier moves. \(\square\)

### Lemma 1.2 (rowwise transport through one arbitrary cut)

For every complete component cut from \(F\) to \(F'\) in a
\(\sigma\)-cell, there is a bijection from the rows of \(F\) to the rows
of \(F'\) under which each row \(C\) is sent either to \(C\) or to
\(\sigma C\). Consequently every selected cyclic-interval occurrence token
is sent either from target \(S\) to \(S\), or from \(S\) to
\(\sigma S\).

#### Proof

On an unswitched ownership component use the identity bijection. On a
switched component use \(C\mapsto\sigma C\) between its complete old and
new row sides. The component root supports are disjoint, so the union of
these maps is a bijection onto the child factor. Coordinate relabelling sends
each cyclic interval of \(C\) to the corresponding cyclic interval of
\(\sigma C\). \(\square\)

---

## 2. The shifted private pile and its membership atoms

Let \(F_m^{\rm MSW}\) be the canonical MSW exact factor. For an integer
\(s\) satisfying (0.4), put

\[
P_s=1^s0^s,\qquad M_s=m-s-2,
\qquad \tau_s=(2s+2\ \ 2s+3).
\tag{2.1}
\]

The audited size-two packet family is

\[
J_s=
\bigl\{\{P_s1100R,P_s1010R\}:R\in\mathcal D_{M_s}\bigr\}.
\tag{2.2}
\]

For a Dyck word \(V\), let \(\mathsf A(V)\) be its down-step position
list, and let \(\mathsf B(P_s)\) be the complementary prefix list appearing
in the exact four-arm formula. At depth \(H\), restrict (2.2) to

\[
R=UV,\qquad
U\in\mathcal D_H,
\quad V\in\mathcal D_{M_s-H}.
\tag{2.3}
\]

Define

\[
\beta_s=2s+2,\qquad \gamma_s=2s+3,
\tag{2.4}
\]

\[
\mathcal C_{s,V}
=\mathsf B(P_s)\cup\{n\}
 \cup\bigl(2s+4+2H+\mathsf A(V)\bigr),
\tag{2.5}
\]

and

\[
S_{s,V}=\mathcal C_{s,V}\cup\{\beta_s\},
\qquad
T_{s,V}=\mathcal C_{s,V}\cup\{\gamma_s\}.
\tag{2.6}
\]

These are rank-\((m-H)\) targets. There are

\[
L_s=\operatorname{Cat}_{M_s-H}
=\operatorname{Cat}_{m-s-H-2}
\tag{2.7}
\]

distinct pairs in (2.6).

### Lemma 2.1 (shifted Catalan pair-total pile)

For every \(V\in\mathcal D_{M_s-H}\), the canonical factor satisfies

\[
\boxed{
\mu_H^{F_m^{\rm MSW}}(S_{s,V})
+\mu_H^{F_m^{\rm MSW}}(T_{s,V})
\ge \operatorname{Cat}_H.
}
\tag{2.8}
\]

The pairs in (2.6) are pairwise target-disjoint: all \(2L_s\) displayed
targets are distinct.

#### Proof

The exact shifted four-arm formula gives the positive suffix core

\[
(2s+4+2H+\mathsf A(V))
\cup\{n\}\cup\mathsf B(P_s),
\tag{2.9}
\]

independently of the first Dyck factor \(U\). All
\(\operatorname{Cat}_H\) choices of \(U\) contribute with the same
orientation to the dipole (2.6). The audited marker argument shows that no
negative arm from these packet rows cancels that private dipole. Therefore
the absolute difference between the two packet-subfamily loads on the pair
is at least \(\operatorname{Cat}_H\). The sum of two nonnegative loads is
at least their absolute difference, and all remaining factor rows only add
nonnegative occurrences. This proves (2.8).

The down-step set determines the Dyck word, so
\(V\mapsto\mathsf A(V)\) is injective. Removing the unique member of
\(\{\beta_s,\gamma_s\}\) from either target recovers
\(\mathcal C_{s,V}\). Two targets with different distinguished coordinates
cannot agree, and two with the same distinguished coordinate agree only when
their cores, hence their Dyck words \(V\), agree. Thus all displayed targets
are distinct. \(\square\)

We now expose the fixed membership atoms. Put

\[
\mathcal I_s=\mathsf B(P_s)\cup\{n\}.
\tag{2.10}
\]

For \(P_s=1^s0^s\), the underlying set of
\(\mathsf B(P_s)\) is \([s]\). In particular it has size \(s\), so

\[
|\mathcal I_s|=s+1.
\tag{2.11}
\]

Let

\[
r_s=M_s-H=m-s-H-2.
\tag{2.12}
\]

Every shifted set in (2.5) lies in the coordinate interval

\[
\mathcal R_s
=2s+4+2H+[2r_s],
\qquad |\mathcal R_s|=2r_s.
\tag{2.13}
\]

Equivalently,

\[
\mathcal R_s=\{2s+2H+5,\ldots,2m\},
\tag{2.13a}
\]

with the interval empty when \(r_s=0\).

Finally define

\[
\mathcal Z_s
=[n]\setminus
\left(
\mathcal I_s\cup\{\beta_s,\gamma_s\}\cup\mathcal R_s
\right).
\tag{2.14}
\]

The four displayed sets are disjoint in the four-arm coordinate frame, and

\[
\begin{aligned}
|\mathcal Z_s|
&=n-(s+1)-2-2(m-s-H-2)\\
&=s+2H+2.
\end{aligned}
\tag{2.15}
\]

Every target in (2.6) contains every coordinate of \(\mathcal I_s\), no
coordinate of \(\mathcal Z_s\), and exactly one of
\(\beta_s,\gamma_s\). Its membership inside \(\mathcal R_s\) may depend
on \(V\).

Consequently, every transposition internal to \(\mathcal I_s\) or internal
to \(\mathcal Z_s\) fixes both targets in each private pair individually,
whereas \(\tau_s=(\beta_s\ \gamma_s)\) interchanges them.

---

## 3. The adaptive full-cell cage

For each \(V\in\mathcal D_{r_s}\), let

\[
t_V
=\mu_H^{F_m^{\rm MSW}}(S_{s,V})
 +\mu_H^{F_m^{\rm MSW}}(T_{s,V}).
\tag{3.1}
\]

By Lemma 2.1,

\[
t_V\ge \operatorname{Cat}_H.
\tag{3.2}
\]

Let \(\mathscr I_{m,s}\) be the set of all literal exact middle wreath
factors \(F\) such that

\[
\mu_H^F(S_{s,V})+\mu_H^F(T_{s,V})=t_V
\quad\text{for every }V\in\mathcal D_{r_s}.
\tag{3.3}
\]

This set is finite and nonempty because it contains
\(F_m^{\rm MSW}\).

### Theorem 3.1 (adaptive menu lock with the correct internal quantifiers)

Choose

\[
G_{m,s}\in\operatorname*{argmin}_{F\in\mathscr I_{m,s}}
\mathfrak F_A(F).
\tag{3.4}
\]

Then the following statement holds:

\[
\boxed{
\begin{gathered}
\forall T\ge0\ \forall\text{ realized adaptive histories}
\ (F_0,\sigma_1,I_1,F_1,\ldots,\sigma_T,I_T,F_T),\\
F_0=G_{m,s},\quad \sigma_j\in\mathcal M_s,\quad
I_j\text{ any subset of all freshly recomputed }\sigma_j
\text{-components},\\
\mathfrak F_A(F_T)\ge\mathfrak F_A(G_{m,s}).
\end{gathered}
}
\tag{3.5}
\]

The assertion is pathwise, so it also holds for randomized choices and
finite or almost-surely finite stopping times.

At time zero, for every \(\sigma\in\mathcal M_s\),

\[
\boxed{
\max_I
\bigl(
\mathfrak F_A(G_{m,s})-
\mathfrak F_A(G_{m,s}^{\,I,\sigma})
\bigr)=0.
}
\tag{3.6}
\]

#### Proof

If \(\sigma\) is internal to \(\mathcal I_s\) or to
\(\mathcal Z_s\), it fixes every private target individually. If
\(\sigma=\tau_s\), it swaps the two targets of every private pair. Lemma
1.1 therefore shows that every allowed complete component cut preserves all
equalities (3.3). This remains true after arbitrary earlier moves because
Lemma 1.1 applies to the freshly recomputed current overlay. Hence every
endpoint in (3.5) belongs to \(\mathscr I_{m,s}\). Minimality in (3.4)
proves (3.5).

For (3.6), every child lies in \(\mathscr I_{m,s}\), so its gain is at
most zero. The empty cut has gain zero. \(\square\)

### Corollary 3.2 (distinct forest-fresh locked bridges)

Take any spanning tree on \(\mathcal I_s\), any spanning tree on
\(\mathcal Z_s\), and the edge \(\{\beta_s,\gamma_s\}\). Their union is
a coordinate forest contained in \(\mathcal M_s\), with

\[
(|\mathcal I_s|-1)+(|\mathcal Z_s|-1)+1
=2s+2H+2
\tag{3.7}
\]

edges. Every edge is distinct, and every ordering of the edges of a forest
makes each edge a fresh bridge when it first appears. All their complete
cells are simultaneously locked at \(G_{m,s}\), and every adaptive history
using any menu edges has the net lock (3.5).

The exact menu cardinality is (0.10).

#### Proof

The two trees and the isolated edge have disjoint vertex sets, so their
union is a forest. Equation (3.7) follows from (2.11) and (2.15). A forest
edge cannot have its endpoints connected by earlier forest edges, since
that would create a cycle. The lock is Theorem 3.1. \(\square\)

---

## 4. Exact factorial floor inside the cage

For an integer \(t\ge0\), define

\[
\psi(t)=\min_{x+y=t}\left[\binom x2+\binom y2\right]
=\left\lfloor\frac{(t-1)^2}{4}\right\rfloor.
\tag{4.1}
\]

### Theorem 4.1 (exact private-pair floor)

Every \(F\in\mathscr I_{m,s}\) satisfies

\[
\boxed{
\Phi_H(F)
\ge
L_s\,\psi(\operatorname{Cat}_H)-P_H^{\min}.
}
\tag{4.2}
\]

Consequently, for fixed \(A>0\), all sufficiently large \(m\), and every
\(s\) satisfying (0.4),

\[
\boxed{
\mathfrak F_A(F)
>
W\left(
\frac{4^{H-s}}{2048K_A\,nH^4}-1
\right).
}
\tag{4.3}
\]

#### Proof

For each private pair, its integral total is \(t_V\ge\operatorname{Cat}_H\).
The function \(\psi\) is nondecreasing, so the pair contributes at least
\(\psi(\operatorname{Cat}_H)\) to the second factorial moment. The pairs
are distinct. Summing their contributions and subtracting the exact global
floor (1.3) proves (4.2).

For \(H\ge3\),

\[
\psi(\operatorname{Cat}_H)
\ge\frac{\operatorname{Cat}_H^2}{8},
\tag{4.4}
\]

and

\[
\operatorname{Cat}_H
\ge\frac{4^H}{(H+1)(2H+1)}
\ge\frac{4^H}{4H^2}.
\tag{4.5}
\]

Every successive Catalan ratio is less than four. Since
\(L_s=\operatorname{Cat}_{m-s-H-2}\),

\[
L_s>
\frac{\operatorname{Cat}_m}{4^{s+H+2}}
=\frac{W}{n4^{s+H+2}}.
\tag{4.6}
\]

Combining (4.4)--(4.6) gives

\[
L_s\psi(\operatorname{Cat}_H)
>
\frac{W4^{H-s}}{2048\,nH^4}.
\tag{4.7}
\]

Moreover,

\[
\frac W{N_H}
=\prod_{j=0}^{H-1}\frac{m+2+j}{m-j}
\le e^{2(A+1)(A+2)}
\tag{4.8}
\]

for all sufficiently large \(m\). Therefore \(b_H\le K_A\). Also

\[
P_H^{\min}\le N_Hb_H\le Wb_H.
\tag{4.9}
\]

Divide (4.2) by \(b_H\), discard the other nonnegative depths in
\(\mathfrak F_A\), and use (4.7)--(4.9). This proves (4.3). \(\square\)

### Corollary 4.2 (two useful parameter regimes)

1. If \(s=\lfloor H/2\rfloor\), then the cage has \(3H+O(1)\)
   forest-fresh edges and \(\Theta_A(m)\) menu edges, while both ratios in
   (0.17) tend to infinity.

2. If

   \[
   \ell_m=\left\lceil10\log_4m\right\rceil,
   \qquad s=H-\ell_m,
   \tag{4.10}
   \]

   then, for large \(m\), the cage has

   \[
   4H-2\ell_m+2=(4-o(1))H
   \tag{4.11}
   \]

   forest-fresh edges and still satisfies both divergent ratios in (0.17).

#### Proof

In the first regime, \(4^{H-s}\ge4^{H/2}\), which dominates every
polynomial in \(m\). Equation (3.7) gives the edge count. In the second,
\(4^{H-s}=4^{\ell_m}\ge m^{10}\), while
\(n^2H^4=O_A(m^4)\). Equations (3.7) and (4.3) give the claims. \(\square\)

---

## 5. Arbitrary adaptive escape requires many counted cuts

The menu lock is permanent only while bridges remain in \(\mathcal M_s\).
The next theorem permits every transposition and quantifies how quickly an
arbitrary adaptive history can disperse the protected occurrences.

### Lemma 5.1 (binary token-support growth)

Suppose an exact factor \(F_0\) contains \(L\) pairwise disjoint labelled
groups of selected rank-\(r\) occurrence tokens. Assume that each group has
exactly \(T\) tokens and is initially supported on at most \(a\) target
values. After any
realized sequence of \(D\) complete transposition-component cuts, with
arbitrary adaptive transpositions, component subsets, and recomputation, the
tokens from one group are supported on at most

\[
a2^D
\tag{5.1}
\]

target values.

If \(\mu_D\) is the complete endpoint load, then

\[
\boxed{
\sum_X\binom{\mu_D(X)}2
\ge
L\left(
\frac{T^2}{2a2^D}-\frac T2
\right).
}
\tag{5.2}
\]

#### Proof

Fix the realized bridge word
\(\sigma_1,\ldots,\sigma_D\). Lemma 1.2 shows that a token is acted on at
step \(j\) by either \(I\) or \(\sigma_j\). From any one initial target,
there are at most \(2^D\) possible resulting words and hence at most
\(2^D\) possible endpoint targets. This proves (5.1).

For a fixed token group, let \(a_X\) be its endpoint multiplicities. By
Cauchy--Schwarz,

\[
\sum_Xa_X^2\ge\frac{T^2}{a2^D}.
\tag{5.3}
\]

Therefore

\[
\sum_X\binom{a_X}{2}
\ge\frac{T^2}{2a2^D}-\frac T2.
\tag{5.4}
\]

Occurrence tokens remain distinct under the row bijections in Lemma 1.2.
Different labelled groups may land on the same targets, but
\(\binom{x+y}{2}\ge\binom x2+\binom y2\). Unselected endpoint occurrences
only add further nonnegative terms. Summing (5.4) over the groups proves
(5.2). \(\square\)

### Theorem 5.2 (exact unrestricted escape-depth inequality)

Start at the cage minimizer \(G_{m,s}\). Let

\[
G_{m,s}=F_0\longrightarrow F_1\longrightarrow\cdots
\longrightarrow F_D
\tag{5.5}
\]

be any realized adaptive sequence of \(D\) complete component cuts for
arbitrary transpositions. At each step the ownership components are the
freshly recomputed current components. Then

\[
\boxed{
\mathfrak F_A(F_D)
\ge
\frac1{b_H}
\left(
\frac{L_s\operatorname{Cat}_H^2}{2^{D+2}}
-\frac{L_s\operatorname{Cat}_H}{2}
-P_H^{\min}
\right).
}
\tag{5.6}
\]

In particular, (0.13) and (0.14) hold.

#### Proof

At \(G_{m,s}\), private pair \(V\) has total load
\(t_V\ge\operatorname{Cat}_H\). Select exactly
\(\operatorname{Cat}_H\) literal occurrence tokens from each pair and
colour them by \(V\). The groups are disjoint because the private pairs are
pairwise target-disjoint. The initial support of each colour has size at most
two. Apply Lemma 5.1 with

\[
L=L_s,\qquad T=\operatorname{Cat}_H,\qquad a=2.
\tag{5.7}
\]

Subtracting the exact floor \(P_H^{\min}\) from (5.2) proves the
depth-\(H\) bound in (5.6). Dividing by \(b_H\) and discarding every other
nonnegative depth proves (5.6).

The Catalan concatenation map

\[
\mathcal D_{m-s-H-2}\times\mathcal D_H
\hookrightarrow\mathcal D_{m-s-2}
\tag{5.8}
\]

gives

\[
L_s\operatorname{Cat}_H
\le\operatorname{Cat}_{m-s-2}
<\operatorname{Cat}_m=\frac Wn.
\tag{5.9}
\]

Equations (4.5)--(4.6) give

\[
\frac{L_s\operatorname{Cat}_H^2}{2^{D+2}}
>
\frac{W\,2^{\,2(H-s)-D-10}}{nH^4}.
\tag{5.10}
\]

Use \(b_H\le K_A\), \(b_H\ge1\), (4.9), and (5.9) in
(5.6), then divide by \(W\). This gives (0.13).

If \(\mathfrak F_A(F_D)\le CW\), rearranging (0.13) gives

\[
2^{\,2(H-s)-D-10}
<K_A nH^4\left(C+1+\frac1{2n}\right),
\tag{5.11}
\]

which is (0.14), with an immaterial strict/non-strict endpoint adjustment
obtainable by a ceiling. \(\square\)

### Corollary 5.3 (balanced cage and escape tradeoff)

Take \(s=\lfloor H/2\rfloor\). For each fixed \(C<\infty\), every
adaptive path from \(G_{m,s}\) to an endpoint with
\(\mathfrak F_A\le CW\) uses at least

\[
H-3\log_2m-O_{A,C}(1)
\tag{5.12}
\]

complete overlay cuts. In particular, any path to

\[
\mathfrak F_A=O_A(HB)=O_A\left(\frac{HW}{n}\right)
\tag{5.13}
\]

uses \(\Omega_A(\sqrt m)\) counted cuts.

#### Proof

Here \(2(H-s)=H+O(1)\), while

\[
\log_2(K_AnH^4)=3\log_2m+O_A(1).
\tag{5.14}
\]

Substitute in (0.14). The threshold in (5.13) is at most \(CW\) for a
fixed \(C\) and all sufficiently large \(m\). \(\square\)

The number \(D\) counts actual complete component cuts. A macro-stage which
hides several preparatory, bridge, or cleanup cuts must charge each of them
to \(D\). One cut may switch any subset of all components in its current
cell; the theorem does not count individual components separately.

---

## 6. Exact quantifier boundary

The proved quantifier order is

\[
\boxed{
\begin{gathered}
\forall A>0\ \exists m_0(A)\ \forall m\ge m_0(A)\\
\forall s\in[2,m-H-2]\cap\mathbb Z\ \exists G_{m,s}\\
\forall\text{ finite adaptive schedules supported on }\mathcal M_s:\quad
\mathfrak F_A(F_{\rm end})\ge\mathfrak F_A(G_{m,s}).
\end{gathered}
}
\tag{6.1}
\]

For unrestricted schedules, the proved statement is not a lock but the
escape-depth inequality (5.6).

The requested positive order would be

\[
\boxed{
\forall F\ \exists\text{ an unrestricted legal adaptive schedule with a
quantitative release-capture or descent guarantee}.
}
\tag{6.2}
\]

Statement (6.2) remains unproved. The present theorem shows exactly what a
proof of (6.2) must add.

1. At \(G_{m,s}\), it cannot obtain a net improvement using only bridges
   internal to the always-in class, internal to the always-out class, or the
   private-pair bridge. It must use a transposition outside
   \(\mathcal M_s\), which may be internal to or incident with the variable
   region \(\mathcal R_s\), or use a permutation move not generated by one
   counted transposition cut.

2. Merely leaving the cage does not rapidly remove the obstruction. Even
   with arbitrary future bridge labels, an \(O(W)\)-energy endpoint needs
   the number of actual cuts in (0.14). For \(s=\lfloor H/2\rfloor\), this
   is \(\Omega_A(\sqrt m)\).

3. A spanning-tree-length schedule has \(n-1=\Theta(m)\) stages, which is
   longer than this lower bound. Therefore the theorem does not refute a
   fully renewed spanning-tree schedule.

4. The all-transposition duplicate--mixing ledger still gives a positive
   selector only under the unproved shielding bound on
   \(X_A^{\rm fac}\). The present cage supplies no such bound for an
   outside-menu bridge.

5. The subgroup-profile telescope supplies release, but it does not provide
   a common component signing which captures that release after the
   outside-menu bridge. Opposite-target mixing and within-component
   multiplicity can still restore the entire coherent gain.

Thus the surviving theorem is more specific than “adapt somehow.” It must
select a bridge outside \(\mathcal M_s\) from every such invariant-fibre
minimizer, prove favorable duplicate separation minus opposite-target mixing
in that fresh full overlay, and renew this capture through the number of
layers forced by (0.14), with total residue \(O_A(HB)\).

No such outside-menu bridge theorem is proved here. No claim of MWB, labelled
common-owner synchronization, a literal OR word, or the constant-one theorem
is made.

---

## 7. Independent audit and rejected overstatements

The decisive argument was independently checked in the following places.

1. **Full components, not packet coordinates.** Equation (1.6) uses the
   complete current ownership component. Therefore Theorem 3.1 allows every
   subset of all freshly recomputed components, including components much
   larger than the original size-two packet.

2. **Membership atoms.** The private core consists only of the fixed prefix
   list \(\mathsf B(P_s)\), the coordinate \(n\), and a down-step subset of
   the \(2r_s\)-coordinate shifted interval. This gives the exact sizes in
   (2.11) and (2.15). Transpositions internal to an included or excluded atom
   fix the target as a set.

3. **Integral floor.** The collision deduction subtracts
   \(P_H^{\min}\) from (1.3). It does not replace the floor by a fractional
   variance. The normalizer is exactly
   \(b_H=\binom{c_H+1}{2}\).

4. **Constant \(2048\).** It is the product of the factor eight in
   \(\psi(C_H)\ge C_H^2/8\), the factor sixteen in
   \(C_H^2\ge16^H/(16H^4)\), and the factor sixteen from the extra two
   Catalan-ratio steps in \(4^{s+H+2}\).

5. **Token exponent.** Starting from two targets gives at most
   \(2^{D+1}\) target values after \(D\) cuts. The factorial collision
   contribution is therefore
   \(C_H^2/2^{D+2}-C_H/2\), producing the exponent
   \(2(H-s)-D-10\) in (0.13).

6. **No stagewise overclaim.** From the invariant-fibre minimizer, every
   first menu cut is nonimproving and every menu-only endpoint has
   nonpositive net gain. After an uphill step, a later individual stage may
   descend relative to the immediately preceding state. Only the net claim
   (3.5) is asserted.

7. **Rejected full-cube inference.** It is false that the lowest-colour
   private-pair totals are invariant throughout the entire positive-density
   AB6 heterogeneous cube merely because packet root supports are disjoint.
   Later packet blocks can overlap those lower-target supports. The present
   proof avoids that error by protecting the highest selected pile with
   literal membership atoms. No claim locks all \(m-H-3\) native matching
   bridges from AB6.

8. **Unrestricted scope.** A bridge outside \(\mathcal M_s\), including one
   internal to the variable region or crossing membership atoms, is not
   covered by the permanent lock and can change protected pair totals.
   Theorem 5.2 then gives only a depth lower bound, not permanent locking.
   This is why (6.2) remains open.

The report therefore supplies a theorem-level, fully integral adaptive
obstruction with exact constants and floors, while preserving the precise
conditional boundary of the unrestricted selector problem.
