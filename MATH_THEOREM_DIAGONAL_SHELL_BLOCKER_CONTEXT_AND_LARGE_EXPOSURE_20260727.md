# Diagonal-shell blocker contexts: exponential local repair and a literal large-exposure construction

Date: 2026-07-27

Method: pure mathematics only. No computation, solver, search, or web
input is used.

## 0. Decision

Use the fixed good common cores and one fixed admissible nested phase
profile in every root. Retain the notation

\[
 W=\binom{2m}{m},\qquad N=N_H,\qquad M=m+H,\qquad
 s=m-H,\qquad L=m-3H+1,
\tag{0.1}
\]

\[
 k=L+2\sum_{q=1}^{H-1}b_q=\Theta(m^{3/2}),
\qquad D=s!,
\tag{0.2}
\]

and let \(p_*\) be the maximum single-target exposure in one literal
tail-order fibre. At the calibrated height,

\[
 kp_*\le
 \exp\left\{-\left({\log2\over4}-o(1)\right)
                         \sqrt{m\log m}\right\}.
\tag{0.3}
\]

For a root \(U\), target \(T\), and a uniform literal history in \(U\),
write \(p_{U,T}\) for the probability that the history contains \(T\).
Thus \(p_{U,T}=0\) when \(T\) is incompatible with \(U\), and otherwise
it is the exact rank exposure from the port-count theorem.

For one selected literal history \(e_V\), define its exposure to the
complete fibre of \(U\) by

\[
 \omega_U(e_V)=\sum_{T\in e_V}p_{U,T}.
\tag{0.4}
\]

This note proves four statements.

1. There is an exact diagonal-shell classification of all terms in
   (0.4). If \(B=V\setminus U\), a target \(V\setminus I\) from
   \(e_V\) is compatible with \(U\) if and only if

   \[
   Q_V\subseteq U,\qquad Q_U\subseteq V,\qquad
   B\subseteq I,\qquad I\cap Q_U=\varnothing.
   \tag{0.5}
   \]

2. If \(a\) is the linear span of \(B\) in the tail order of \(e_V\),
   then at deletion length \(\ell\) there are at most

   \[
   (\ell-a+1)_+
   \tag{0.6}
   \]

   compatible phase contexts. Consequently, for distinct roots,

   \[
   \boxed{
   \omega_U(e_V)\le h_*p_*,
   \qquad h_*:=H(2H-1)<2H^2.}
   \tag{0.7}
   \]

3. No one selected history fully blocks another complete fibre. More
   generally, fewer than \(1/(h_*p_*)\) selected histories cannot fully
   block a fibre. Hence every root set of size

   \[
   r<1+{1\over h_*p_*}
   \tag{0.8}
   \]

   has a target-simple literal full-history selection. This improves the
   earlier local repair denominator \(kp_*\) to \(h_*p_*\).
4. The pairwise improvement does not sum to a global
   \(\iota(V)=o(m)\) theorem. For every fixed good-core fractional atlas
   there is a literal one-history-per-root selection and a selected
   history \(e_V\) for which

   \[
   \boxed{
   \iota(V):=
    \sum_{\substack{U:\,c_U>0\\U\ne V}}\omega_U(e_V)
    \ge c k=\Omega(m^{3/2})}
   \tag{0.9}
   \]

   for an absolute constant \(c>0\). Here \(c_U>0\) means that the
   selected history of \(U\) has an actual collision in the displayed
   global selection.

Thus diagonal nesting completely rules out bounded, polynomial, and
subexponential fully blocking port systems, but it does not give the
desired incoming-exposure bound uniformly over literal selections.
There are physical selections with \(\iota(V)\gg m\).

This does not refute the collision theorem. The selection in (0.9) is
not asserted to minimize collision excess. The exact surviving positive
gate is minimizer-specific:

> prove that some global collision minimizer has
> \(\max_V\iota(V)=o(m)\).

No theorem depending only on pairwise diagonal contexts, fixed-core
degree caps, or local odd-port repairability can establish that statement
for every selection.

## 1. Literal histories and per-depth exposures

Fix a root top \(V\), its core \(Q_V\), and a tail order

\[
 w=(w_1,\ldots,w_s)
\tag{1.1}
\]

of \(S_V=V\setminus Q_V\). At phase \(j\) and deletion length
\(\ell\), put

\[
 I_{j,\ell}
 =\{w_{j+2H-\ell},\ldots,w_{j+2H-1}\},
\qquad
 T_{j,\ell}=V\setminus I_{j,\ell}.
\tag{1.2}
\]

The protected lengths are:

- \(\ell=H\) at all \(L\) middle phases;
- \(\ell=H-q\) at the \(b_q\) active upper phases; and
- \(\ell=H+q\) at the same \(b_q\) active lower phases,

for \(1\le q<H\). Empty quota lengths are omitted.

For a compatible target at length \(\ell\), define

\[
 p_\ell=
 \begin{cases}
 \displaystyle {L\over\binom{s}{H}},&\ell=H,\\[3mm]
 \displaystyle {b_q\over\binom{s}{H-q}},
       &\ell=H-q,\ 1\le q<H,\\[3mm]
 \displaystyle {b_q\over\binom{s}{H+q}},
       &\ell=H+q,\ 1\le q<H.
 \end{cases}
\tag{1.3}
\]

Then \(p_{U,T}=p_\ell\) for a compatible rank-\((M-\ell)\) target and
\(p_{U,T}=0\) otherwise. In particular,

\[
 p_\ell\le p_*.
\tag{1.4}
\]

## 2. Exact cross-root context classification

Fix another top \(U\ne V\), with core \(Q_U\), and put

\[
 A=U\setminus V,\qquad B=V\setminus U,\qquad
 |A|=|B|=\delta.
\tag{2.1}
\]

### Theorem 2.1 (reciprocal-core diagonal criterion)

For a protected cell \((j,\ell)\) of the selected history \(e_V\), the
target \(T_{j,\ell}\) is compatible with the complete history fibre of
\(U\) if and only if

\[
 Q_V\subseteq U,\qquad Q_U\subseteq V,
\tag{2.2}
\]

\[
 B\subseteq I_{j,\ell},\qquad
 I_{j,\ell}\cap Q_U=\varnothing.
\tag{2.3}
\]

When these conditions hold,

\[
 U\setminus T_{j,\ell}
 =A\mathbin{\dot\cup}(I_{j,\ell}\setminus B),
\tag{2.4}
\]

an \(\ell\)-set, so the target has the correct physical context in
\(U\).

#### Proof

Compatibility with \(U\) is exactly

\[
 Q_U\subseteq T_{j,\ell}\subseteq U.
\tag{2.5}
\]

The second inclusion holds if and only if every point of
\(B=V\setminus U\) was deleted, namely \(B\subseteq I_{j,\ell}\).
Since every deletion interval lies in \(V\setminus Q_V\), this forces
\(B\cap Q_V=\varnothing\), equivalently \(Q_V\subseteq U\).

The first inclusion in (2.5) is equivalent to
\(Q_U\subseteq V\) and \(I_{j,\ell}\cap Q_U=\varnothing\).
This proves necessity and sufficiency of (2.2)--(2.3). Formula (2.4)
follows by subtracting \(V\setminus I_{j,\ell}\) from
\((V\setminus B)\dot\cup A\). \(\square\)

Several immediate restrictions are worth recording:

\[
 \delta\le\ell\le2H-1,
\tag{2.6}
\]

the exchanged set \(B\) lies entirely in the displayed tail of \(V\),
and no deletion interval witnessing compatibility may cross a tail
coordinate belonging to \(Q_U\setminus Q_V\).

## 3. Span bound and exact exposure formula

If \(B\subseteq S_V\), let

\[
 a=\operatorname{span}_w(B)
 =\max\{t:w_t\in B\}-\min\{t:w_t\in B\}+1.
\tag{3.1}
\]

Put \(a=+\infty\) when \(B\nsubseteq S_V\). For every protected length
\(\ell\), let \(n_\ell(U,V;e_V)\) be the number of its active phases
whose deletion intervals satisfy (2.3).

### Theorem 3.1 (diagonal-shell exposure formula)

\[
 \boxed{
 \omega_U(e_V)
 =\sum_{\ell=1}^{2H-1}
      n_\ell(U,V;e_V)\,p_\ell,}
\tag{3.2}
\]

where terms at inactive lengths are zero, and

\[
 \boxed{
 n_\ell(U,V;e_V)\le(\ell-a+1)_+.}
\tag{3.3}
\]

Consequently,

\[
 \omega_U(e_V)
 \le p_*\sum_{\ell=1}^{2H-1}\ell
 =H(2H-1)p_*.
\tag{3.4}
\]

#### Proof

Theorem 2.1 classifies exactly which targets in \(e_V\) have nonzero
exposure to \(U\); each such target has the per-depth exposure
\(p_\ell\), proving (3.2).

Every witnessing length-\(\ell\) interval contains \(B\). A set of
linear span \(a\) is contained in at most
\(\ell-a+1\) length-\(\ell\) intervals. Restricting to eligible phases,
to the nested active phase set, and to intervals avoiding \(Q_U\) can
only decrease this number. This proves (3.3). Summing its crude upper
bound \(\ell\) proves (3.4). \(\square\)

This is the exact diagonal-shell improvement over the bound
\(\omega_U(e_V)\le kp_*\). Although one history has
\(k=\Theta(m^{3/2})\) targets, only \(O(H^2)\) of its phase-depth cells
can even be compatible with one other root.

## 4. Full blocking and the improved local repair radius

Say that a target family \(\mathcal F\) fully blocks the fibre
\(\Omega_U\) if every history \(f\in\Omega_U\) intersects
\(\mathcal F\).

### Corollary 4.1 (one history never fully blocks a fibre)

For sufficiently large \(m\), no selected history \(e_V\), \(V\ne U\),
fully blocks \(\Omega_U\).

#### Proof

By (0.3),

\[
 h_*p_*\le2H^2p_*=o(1).
\tag{4.1}
\]

The average value of \(|f\cap e_V|\) over
\(f\in\Omega_U\) is \(\omega_U(e_V)<1\). Since the intersection size is
a nonnegative integer, some \(f\) has intersection zero. \(\square\)

### Theorem 4.2 (diagonal-shell greedy repair)

Let \(U_1,\ldots,U_r\) be distinct roots with arbitrary fixed good
cores and admissible nested phase sets. If

\[
 (r-1)h_*p_*<1,
\tag{4.2}
\]

then there is one literal full history in every root and all selected
protected targets are pairwise distinct.

#### Proof

Choose roots sequentially. After histories have been chosen in
\(U_1,\ldots,U_{i-1}\), their union has exposure to \(U_i\) at most

\[
 \sum_{j<i}\omega_{U_i}(e_{U_j})
 \le(i-1)h_*p_*<1
\tag{4.3}
\]

by Theorem 3.1. Therefore some history in \(\Omega_{U_i}\) avoids the
whole previous union. Continue. \(\square\)

### Corollary 4.3 (improved closed-obstruction size)

Every inclusion-minimal closed root subsystem without a target-simple
transversal has at least

\[
 1+{1\over h_*p_*}
\tag{4.4}
\]

roots, with the evident ceiling convention.

In particular, all bounded, polynomial, and
\(\exp(o(H))\)-sized odd-port systems repair inside the literal
all-depth catalogue.

## 5. Why pairwise nesting cannot bound total incoming exposure

For every root \(U\) and target \(v\), retain

\[
 p_{U,v}={|\{e\in\Omega_U:v\in e\}|\over D},
\qquad
 \rho_v=\sum_U p_{U,v}\le1.
\tag{5.1}
\]

The fixed-core fractional atlas has

\[
 \sum_v\rho_v=kN=B-\Delta,
\qquad \Delta=o(W)=o(B).
\tag{5.2}
\]

For one literal history \(e_V\), define its unrestricted incoming
exposure

\[
 J(e_V)=\sum_{U\ne V}\omega_U(e_V).
\tag{5.3}
\]

### Proposition 5.1 (large total exposure is unavoidable)

There is a root \(V\) and a literal history \(e_V\) such that

\[
 J(e_V)\ge(1-o(1))k.
\tag{5.4}
\]

#### Proof

Average over a uniform history in every root:

\[
 \sum_V {1\over D}\sum_{e_V\in\Omega_V}J(e_V)
 =\sum_v\left(\rho_v^2-\sum_U p_{U,v}^2\right).
\tag{5.5}
\]

By Cauchy--Schwarz,

\[
 \sum_v\rho_v^2
 \ge{(B-\Delta)^2\over B}
 =B-o(B).
\tag{5.6}
\]

Also

\[
 \sum_{U,v}p_{U,v}^2
 \le p_*\sum_{U,v}p_{U,v}
 =p_*kN=o(B).
\tag{5.7}
\]

Thus the left side of (5.5) is
\((1-o(1))B=(1-o(1))kN\). Divide by \(N\). \(\square\)

So the separate capacity rows and diagonal-shell nesting permit one
history to receive total exposure \(\Theta(k)\). The restriction to
collided source roots in \(\iota(V)\) is essential.

## 6. A literal selection with \(\iota(V)=\Omega(k)\)

We now show that even the collided-source restriction does not give a
uniform \(o(m)\) bound over all selections.

For two distinct roots define

\[
 q_{U,R}=\sum_v p_{U,v}p_{R,v}.
\tag{6.1}
\]

This is the expected exposure \(\omega_U(e_R)\) of a uniform history
in \(R\). By Theorem 3.1,

\[
 q_{U,R}\le h_*p_*.
\tag{6.2}
\]

Put

\[
 a_U=\sum_{R\ne U}q_{U,R}.
\tag{6.3}
\]

Then

\[
 \sum_Ua_U
 =\sum_v\left(\rho_v^2-\sum_Up_{U,v}^2\right)
 =(1-o(1))kN
\tag{6.4}
\]

by (5.5)--(5.7).

### Theorem 6.1 (large incoming exposure in a literal selection)

There is a literal one-history-per-root selection \(e\) and a selected
history \(e_V\) such that

\[
 \boxed{
 \sum_{\substack{U:\,c_U(e)>0\\U\ne V}}\omega_U(e_V)
 \ge c k}
\tag{6.5}
\]

for an absolute constant \(c>0\).

#### Proof

Randomly and independently assign every root to one of three classes
\(\mathsf S,\mathsf C,\mathsf B\), each with probability \(1/3\).
Then choose one uniform literal history independently in every root.

For \(U\in\mathsf S\), let \(I_U\) be the indicator that its selected
history shares at least one target with a selected history belonging to
\(\mathsf C\). Such a root has \(c_U(e)>0\) in the full selection.
For a fixed class partition, put

\[
 a_U^{\mathsf C}=\sum_{R\in\mathsf C}q_{U,R},
\qquad
 a_U^{\mathsf B}=\sum_{R\in\mathsf B}q_{U,R}.
\tag{6.6}
\]

Let \(X_U\) count the targets of the selected history of \(U\) which
are used by at least one selected \(\mathsf C\)-history. Since
\(0\le X_U\le k\),

\[
 \Pr(I_U=1)\ge{\mathbb E X_U\over k}.
\tag{6.7}
\]

For a target \(v\), the probability that no \(\mathsf C\)-root selects
it is

\[
 \prod_{R\in\mathsf C}(1-p_{R,v})
 \le\exp\left(-\sum_{R\in\mathsf C}p_{R,v}\right).
\tag{6.8}
\]

The sum in the exponent is at most \(\rho_v\le1\), and

\[
 1-e^{-x}\ge(1-e^{-1})x\qquad(0\le x\le1).
\tag{6.9}
\]

Therefore

\[
 \mathbb E X_U
 \ge(1-e^{-1})a_U^{\mathsf C}.
\tag{6.10}
\]

The histories selected in \(\mathsf B\) are independent of \(I_U\).
Conditional on the class partition,

\[
 \mathbb E\left[
 I_U\sum_{V\in\mathsf B}\omega_U(e_V)\right]
 \ge {1-e^{-1}\over k}\,
      a_U^{\mathsf C}a_U^{\mathsf B}.
\tag{6.11}
\]

Conditional on \(U\in\mathsf S\), averaging the random classes of the
other roots gives

\[
 \mathbb E[
 a_U^{\mathsf C}a_U^{\mathsf B}]
 ={1\over9}
 \left(a_U^2-\sum_{R\ne U}q_{U,R}^2\right).
\tag{6.12}
\]

Now Cauchy--Schwarz and (6.4) give

\[
 \sum_Ua_U^2
 \ge {(\sum_Ua_U)^2\over N}
 =(1-o(1))k^2N.
\tag{6.13}
\]

By (6.2),

\[
 \sum_U\sum_{R\ne U}q_{U,R}^2
 \le h_*p_*\sum_Ua_U
 =o(k^2N).
\tag{6.14}
\]

Multiply (6.11)--(6.12) by
\(\Pr(U\in\mathsf S)=1/3\), sum over \(U\), and use
(6.13)--(6.14). The expected value of

\[
 \sum_{V\in\mathsf B}
 \sum_{\substack{U\in\mathsf S\\I_U=1}}\omega_U(e_V)
\tag{6.15}
\]

is at least \(c_0kN\) for an absolute \(c_0>0\). Hence some literal
realization has value at least \(c_0kN\). There are at most \(N\)
selected histories in \(\mathsf B\), so one of them has incoming
exposure at least \(c_0k\) from roots with \(c_U(e)>0\). This is
(6.5). \(\square\)

The construction uses actual complete histories at every root and
actual physical target collisions. It is not a profile or entropy
example.

## 7. Consequences for the minimizer-specific blocker theorem

Theorem 6.1 proves that the proposed uniform estimate

\[
 \iota(V)=o(m)\qquad\hbox{for every selection and every selected }V
\tag{7.1}
\]

is false by a factor of order \(\sqrt m\). Diagonal-shell nesting gives
the sharp pairwise sparsity (3.4), but exponentially many pairwise-small
contexts can accumulate on one literal history.

At a collision minimizer, the one-switch blocker identity still gives

\[
 K^*\le N\max_V\iota(V).
\tag{7.2}
\]

Thus a minimizer-specific estimate

\[
 \max_V\iota(V)=o(m)
\tag{7.3}
\]

would prove \(K^*=o(W)\). Theorem 6.1 does not refute (7.3), because
its selection is not asserted to minimize \(K\).

The improved pairwise bound strengthens the obstruction forced by a
linear-collision minimizer. If \(K^*\ge\varepsilon W\), then some
selected history has \(\iota(V)=\Omega(m)\); since every incoming root
contributes at most \(h_*p_*\), that history participates in the
blocking sets of at least

\[
 \boxed{
 {\varepsilon m\over(1+o(1))h_*p_*}
 =\exp(\Omega(H))}
\tag{7.4}
\]

distinct collided roots.

Therefore the exact surviving gate is not pairwise context
classification. It is an optimization theorem showing that multi-root
switches can transform a collision minimizer until no history receives
\(\Omega(m)\) total blocker exposure. Bounded odd-port switches are
already covered by Theorem 4.2; a successful move must act on the
globally shared blocker mesh.

## 8. Final theorem-grade statement

### Theorem 8.1 (diagonal blocker dichotomy)

For the physical all-depth common-core history catalogue:

1. cross-root compatible cells obey the reciprocal-core criterion
   (2.2)--(2.3);
2. one root pair shares at most \((\ell-a+1)_+\) contexts at length
   \(\ell\);
3. one selected history exposes at most \(H(2H-1)p_*\) mass to any
   other complete fibre;
4. fewer than \(1/(H(2H-1)p_*)\) histories cannot fully block one
   fibre, so every smaller odd-port system repairs integrally;
5. nevertheless there is a literal global selection and selected
   history with collided-source incoming exposure
   \(\Omega(k)=\Omega(m^{3/2})\);
6. hence diagonal nesting and exact per-depth contexts cannot prove a
   uniform \(o(m)\) blocker-congestion bound; and
7. failure of the minimizer-specific \(o(m)\) bound requires a literal
   exponentially large shared blocker mesh as quantified in (7.4).

The local odd-port lane is therefore closed for collision excess. The
remaining constant-one problem is a global multi-root improvement
theorem for collision minimizers, not a further single-history
context count.

## 9. Dependency ledger

This note uses:

- MATH_THEOREM_FULL_HISTORY_COLLISION_DUAL_AND_GLOBAL_BLOCKER_20260727.md
  for the collision minimizer, blocker exposure, and the implication
  \(K^*\le N\max_V\iota(V)\);
- MATH_ATTACK_O_CCTPF_FULL_HISTORY_ODD_PORT_AND_REPAIR_20260726.md for
  the exact per-depth exposure \(p_\ell\), the forbidden-port lemma, and
  the exponential estimate (0.3);
- MATH_THEOREM_S_COMMON_CORE_TRACE_FUSION_OBSTRUCTION_20260726.md for
  the underlying span principle.

No perfect-matching theorem, entropy lower bound, or computational
experiment is used.
