# Fixed-decoration deletion and the stopped variance bootstrap

Date: 2026-07-25

Method: pure mathematics only.

## 0. Verdict

Expanding every base grid into its fixed priority orders does give a
literal decreasing family of decorated candidates for the sequential
exact-priority nibble.  Owner consumption, target consumption, deadline
failure, tag retirement, exceptional discard, and permanent dynamic
quarantine only delete fixed decorations.  The factorial priority weight
is exactly the number of surviving decorations; it is not a changing
weight on a surviving decoration.

This gives two sharp deterministic facts.  If

\[
 d_t(v)\ge a_t d_0(v)\qquad\hbox{for every relevant live fibre }v,
 \tag{0.1}
\]

then every normalized pair-square is at most \(a_t^{-2}\) times its raw
value, and every fixed-conflict common-link square is at most
\(a_t^{-3}\) times its raw value.  Consequently, **if** the stopped lower
bound in the question were

\[
 a_t\ge (1-\eta)z_t,\qquad z_t\ge1/\log m,
 \tag{0.2}
\]

the raw \(m^{-1+o(1)}\) triangle would indeed give the global weighted
quadratic-variation budget

\[
 B_mW=m^{-1/2+o(1)}W,
 \tag{0.3}
\]

and the global stopped Doob theorem would close variance.

However, (0.2) is not the stopped degree lower bound recorded for the
current geodesic-chunk nibble.  In the established notation

\[
 z_t=\prod_{s<t}q_s
 \tag{0.4}
\]

is the surviving resource density, whereas a one-root decorated degree
has ideal contraction

\[
 d_t(v)=(1+o(1))z_t^{\,g-1}d_0(v),
 \qquad g=m^{1/2+o(1)}.
 \tag{0.5}
\]

This is exactly the exponent in Corollary 3.2 of
`MATH_ATTACK_DYNAMIC_QUARANTINE_CONDITIONED_PAIR_SQUARE_RECURRENCE_20260725.md`.
Deletion monotonicity alone therefore gives only

\[
 S_t\le (1+o(1))z_t^{-2(g-1)}S_0,
 \qquad
 J_t\le (1+o(1))z_t^{-3(g-1)}J_0.
 \tag{0.6}
\]

At \(z_t=1/\log m\), the second multiplier is

\[
 (\log m)^{3(g-1)},
 \tag{0.7}
\]

which is superpolynomial and destroys (0.3).  Thus the fixed-decoration
observation proves a useful conditional variance theorem, but it does not
close the current hereditary recurrence.  The remaining statement is
still a numerator-contraction or predictable pair-link mean-spread
theorem, for example

\[
 d_t(x,y)\lesssim z_t^{\,g-2}d_0(x,y)
 \tag{0.8}
\]

in the weighted form needed by the process.  Binary deletion by itself
cannot supply (0.8).

There is one genuine structural exception.  The later donor operation
which deletes phase columns and then chooses a new priority on the
shortened trajectory is not a subhypergraph operation on the original
full decorated catalogue.  It is not used in the sequential hereditary
nibble.  If it is inserted into that nibble, all phase-deletion masks and
their resulting priorities must be frozen in the initial catalogue and
the raw degree and common-link estimates must be reproved.

## 1. Fixed priority orders really are fixed decorations

Fix a base grid \(P\), with phases \([g]\), and a priority permutation
\(\sigma\).  For every phase \(i\) and protected depth \(q\), the grid has
a fixed target \(T_{i,q}(P)\).  With the fixed deadline allowances used
by the construction, the order \(\sigma\) claims \(T_{i,q}(P)\) according
to the fixed comparison between the position of \(i\) in \(\sigma\) and
the cutoff \(c_q\).  Equivalently, if that target has become unavailable,
the same comparison says whether \(\sigma\) violates the resulting
deadline.

Thus \((P,\sigma)\) has a fixed owner set and a fixed claimed-target set.
At a history \({\cal H}_t\), it is feasible precisely when all its owners
are unused, all targets which it claims are available, its tag is live,
and its base grid has not been permanently quarantined.  Each of these
conditions is monotone under the committed process.

The familiar quantities \(B_{t,q}(P)\), \(n_{t,q}(P)\), and
\(\sigma_{t,q}(P)\) do change with time, but they are only statistics used
to count the fixed permutations which remain.  The exact factorial
formula says

\[
 \Pi_t(P)=\#\{\sigma:(P,\sigma)\hbox{ is feasible at time }t\}.
 \tag{1.1}
\]

As unavailable targets accumulate,

\[
 \Pi_{t+1}(P)\le\Pi_t(P).
 \tag{1.2}
\]

The multiplicative deadline update is the quotient of the two integer
counts in (1.1); it does not modify a surviving copy.

Consequently, after including the fixed initial pruning in the definition
of \(\Omega_0\), there are sets

\[
 \Omega_{t+1}\subseteq\Omega_t\subseteq\Omega_0
 \tag{1.3}
\]

of live decorated candidates.  Sampling a base grid with probability
proportional to \(\Pi_t(P)\), followed by a uniform feasible priority, is
exactly uniform sampling from the corresponding decorated tag fibre of
\(\Omega_t\).

### Operations in the recorded process

The following are all deletions from \(\Omega_t\).

1. Consuming a middle owner deletes every decoration containing it.
2. Consuming a protected target deletes every decoration which claims it.
3. A deadline failure deletes the fixed orders which claim an unavailable
   target too early; it does not move a phase inside a surviving order.
4. The \(B_4\) quarantine relation is fixed by the two full grids.
   Quarantining against an accepted grid permanently deletes its fixed
   neighbours.
5. Retiring a tag, discarding an exceptional fibre, and the auxiliary
   wasteful restriction against tentative choices only delete copies.
6. Conditioning on one- or two-root survival changes the probability
   law on \(\Omega_t\); it does not add a candidate.

The deadline allowance \(\bar d_q\) must be fixed before \(\Omega_0\) is
defined.  The recorded construction does this.  An adaptive enlargement
which revives formerly infeasible orders would violate (1.3), but no such
revival is part of the audited nibble.

Temporary tentative choices which are later rejected cause no problem.
At completed histories only committed deletions enter \(\Omega_t\); for
the within-bite variance calculation the auxiliary wasteful restriction
is itself a deletion from the current \(\Omega_t\).

## 2. Deterministic normalized pair-square domination

Let \(\mathcal H_0\) be a finite multihypergraph and let
\(\mathcal H\subseteq\mathcal H_0\) be obtained by reducing edge
multiplicities.  Write

\[
 d(x)=\#\{e\in\mathcal H:x\in e\},\qquad
 d(x,y)=\#\{e\in\mathcal H:x,y\in e\},
 \tag{2.1}
\]

and use a subscript zero for \(\mathcal H_0\).  Suppose

\[
 d(v)\ge a_vd_0(v),\qquad 0<a_v\le1.
 \tag{2.2}
\]

Define

\[
 K(x,y)={d(x,y)\over\sqrt{d(x)d(y)}}.
 \tag{2.3}
\]

Since \(d(x,y)\le d_0(x,y)\),

\[
 \boxed{
 K(x,y)\le(a_xa_y)^{-1/2}K_0(x,y).}
 \tag{2.4}
\]

For any block \(B\) of possible second vertices,

\[
\begin{aligned}
 S(x;B)&:=\sum_{y\in B}K(x,y)^2\\
 &\le a_x^{-1}\sum_{y\in B}a_y^{-1}K_0(x,y)^2.
\end{aligned}
 \tag{2.5}
\]

In particular, if every displayed \(a_v\ge a\), then

\[
 \boxed{S(x;B)\le a^{-2}S_0(x;B).}
 \tag{2.6}
\]

For the normalized triangle,

\[
 {d(x,y)d(y,z)d(z,x)\over d(x)d(y)d(z)}
 \le
 {1\over a_xa_ya_z}
 {d_0(x,y)d_0(y,z)d_0(z,x)
  \over d_0(x)d_0(y)d_0(z)}.
 \tag{2.7}
\]

Summing gives

\[
 \boxed{{\mathfrak T}_{\cal H}(x)\le a^{-3}
              {\mathfrak T}_{{\cal H}_0}(x).}
 \tag{2.8}
\]

These inequalities are pathwise and require no independence,
conditioning, exchange structure, or martingale argument.

## 3. Direct domination of the exact priority common-link square

The same conclusion can be proved without representing every conflict as
a shared physical vertex.  It therefore also applies to fixed full-grid
quarantine edges whenever their own raw \(J_0\) is inserted.  In the
current accounting those quarantine losses may instead be paid by the
separate \(m^{-4+o(1)}\) pathwise loss ledger.

Let \(\Omega_0\) be the decorated candidate multiset, let
\(\Omega_t\subseteq\Omega_0\), and let \({\cal C}_F\) be the fixed set of
decorations belonging to fibre \(F\).  Tags form a partition of
\(\Omega_0\).  Let \(e\to f\) be any fixed relation meaning that choosing
\(e\) deletes \(f\).  Put

\[
 D_t(F)=|\Omega_t\cap\mathcal C_F|,
 \qquad
 L_t(F,e)=|\{f\in\Omega_t\cap\mathcal C_F:e\to f\}|.
 \tag{3.1}
\]

The exact binary common-link square for fibre \(F\) is

\[
 J_t(F)=
 \sum_U{1\over D_t(U)}
 \sum_{e\in\Omega_t\cap\mathcal C_U}
 \left({L_t(F,e)\over D_t(F)}\right)^2.
 \tag{3.2}
\]

Here a base grid with \(a_t(P)\) feasible orders simply occurs with that
many fixed decorated copies, so (3.2) is exactly the weighted priority
kernel after expansion.

Assume

\[
 D_t(F)\ge aD_0(F),\qquad D_t(U)\ge aD_0(U)
 \tag{3.3}
\]

for the displayed fibre and every live tag.  Since
\(L_t(F,e)\le L_0(F,e)\) and the outer summation in (3.2) is over a subset
of the initial candidates,

\[
\begin{aligned}
 J_t(F)
 &\le {1\over a^3}
 \sum_U{1\over D_0(U)}
 \sum_{e\in\Omega_0\cap\mathcal C_U}
 \left({L_0(F,e)\over D_0(F)}\right)^2\\
 &=a^{-3}J_0(F).
\end{aligned}
 \tag{3.4}
\]

Thus

\[
 \boxed{J_t(F)\le a^{-3}J_0(F).}
 \tag{3.5}
\]

This is the exact aggregate four-walk domination sought by the proposed
argument.  It is stronger than first bounding physical pair codegrees,
and it shows that cross-slice repetition is harmless **provided the
linear lower bound (3.3) holds**.  It also shows why deletion alone is not
enough: the three normalizing degrees in (3.2) are the whole issue.

If parallel activation is used under a root-survival conditioning, the
per-tag law has denominator \(1-\alpha q_U\ge1-\alpha\).  This inserts
only the already recorded factor \((1-\alpha)^{-1}=1+O(\alpha)\) in one
bite.  The cleanest exact form of (3.5) is the sequential formulation,
where no such denominator occurs.

## 4. Conditional stopped-Doob closure

Assume now, only up to each fibre's stopping time, that

\[
 D_t(F)\ge(1-\eta)z_tD_0(F),
 \qquad z_t\ge1/\log m.
 \tag{4.1}
\]

The stopping time here is strictly before direct consumption of the
fibre's root (and, for a tag fibre, before retirement of that tag).
Equivalently one works under the exact root-survival law.  Including the
terminal consuming jump would insert a loss of one and recover the
already-audited \(\Theta(KT)=\Theta(W\sqrt m)\) diagonal obstruction.
All estimates below concern the pre-hit stopped increments.

By (3.5),

\[
 J_t(F)\le(1-\eta)^{-3}z_t^{-3}J_0(F)
 \le(1+O(\eta))\log^3m\,J_0(F).
 \tag{4.2}
\]

For the ordinary owner/target/deadline relation, the proved mixed raw
bound is

\[
 J_0(F)\le m^{-1+o(1)}
 \tag{4.3}
\]

in the aggregate mixed target/tag normalization.  There are

\[
 Q=m^{1/2+o(1)}
 \tag{4.4}
\]

protected strata, and the effective time factor is
\(O(\log\log m)=m^{o(1)}\).  Hence the stopped weighted predictable
quadratic variation is

\[
\begin{aligned}
 \sum_F\operatorname{wt}(F)
 \mathbb E\langle M_F\rangle_{\tau_F}
 &\le
 W\,Q\,m^{-1+o(1)}\log^3m\log\log m\\
 &=m^{-1/2+o(1)}W.
\end{aligned}
 \tag{4.5}
\]

Permanent \(B_4\)-quarantine deletions are structurally covered by
Section 3 but need not be folded into (4.3): outside weighted \(o(W)\)
fibres their already proved cumulative fractional loss is
\(m^{-4+o(1)}\).  Since \(0\le I\le1\), their sum of squared increments is
at most their total fractional loss, and after the
\(Q=m^{1/2+o(1)}\) fibre ledger it is still \(o(W)\).

Put \(B_m=m^{-1/2+o(1)}\) and choose

\[
 \eta=B_m^{1/4}=m^{-1/8+o(1)}.
 \tag{4.6}
\]

The weighted stopped Doob lemma charges corridor exits by

\[
 O(B_m/\eta^2)W=O(B_m^{1/2})W
   =m^{-1/4+o(1)}W=o(W),
 \tag{4.7}
\]

while the logarithmic remainder or bounded predictable drift budget
contributes at most

\[
 O(B_m/\eta)W=O(B_m^{3/4})W
   =m^{-3/8+o(1)}W=o(W).
 \tag{4.8}
\]

Therefore (4.1) would close the variance part of hereditary propagation,
leaving only the predictable mean-spread comparison.

## 5. Why the premise is not the current stopped lower bound

In the current nibble, one bite retains an individual resource with
factor \(q_t\).  Conditional on one root surviving, a decorated candidate
still has \(g-1\) other required resource coordinates.  The recorded
one-root reference contraction is therefore

\[
 \rho_{1,t}=q_t^{\,g-1}(1+o(1)).
 \tag{5.1}
\]

After several bites,

\[
 \prod_{s<t}\rho_{1,s}
 =(1+o(1))\left(\prod_{s<t}q_s\right)^{g-1}
 =(1+o(1))z_t^{\,g-1}.
 \tag{5.2}
\]

The stopped scalar martingale controls the ratio of \(D_t(F)\) to the
reference in (5.2), conditional on the still-required scalar predictable
mean-spread statement.  It does not replace (5.2) by \(z_t\).  Thus even
after that mean-spread statement is supplied, the resulting lower bound
would be

\[
 D_t(F)\ge(1-o(1))z_t^{\,g-1}D_0(F),
 \tag{5.3}
\]

not (4.1).

Substitution of (5.3) into the deletion theorem gives

\[
 J_t(F)\le(1+o(1))z_t^{-3(g-1)}J_0(F).
 \tag{5.4}
\]

At the required resource density \(z_t=1/\log m\),

\[
 z_t^{-3(g-1)}
 =\exp(3(g-1)\log\log m).
 \tag{5.5}
\]

Since \(g=m^{1/2+o(1)}\), (5.5) dominates every fixed power of \(m\).
It cannot be absorbed into the raw \(m^{-1+o(1)}\) triangle, even before
the factor \(Q\) is paid.

Stopping instead when the **catalogue-degree** density first reaches
\(1/\log m\) would make Section 4 applicable, but by (5.2) this occurs
when

\[
 z_t=(1/\log m)^{1/(g-1)}
 =1-\Theta\left({\log\log m\over g}\right).
 \tag{5.6}
\]

Only an \(O((\log\log m)/g)=o(1)\) fraction of resources has then been
consumed.  The residual middle antichain still has weight \((1-o(1))W\),
so this stopping point is useless for coefficient one.

## 6. Sharpness and the exact surviving gate

The losses in (2.6), (2.8), and (3.5) are sharp for arbitrary deletion.
For example, start with three vertices \(x,y,z\), retain a fixed family of
edges common to each relevant pair, and pad each one-vertex degree with
private edges.  Delete only private edges until every one-vertex degree
is \(a\) times its initial value.  All retained pair codegrees stay
unchanged, so each normalized pair kernel grows by \(a^{-1}\), its square
by \(a^{-2}\), and the triangle by \(a^{-3}\).

Hence no theorem using only

\[
 {\cal H}_t\subseteq{\cal H}_0
 \quad\hbox{and one-root degree lower bounds}
 \tag{6.1}
\]

can improve these exponents.  To recover the desired resource-density
inflation one needs numerator contraction.  A sufficient pointwise form
is

\[
 d_t(x,y)\le(1+o(1))z_t^{\,g-2}d_0(x,y),
 \tag{6.2}
\]

together with (5.3).  Then

\[
 {d_t(x,y)^2\over d_t(x)d_t(y)}
 \le(1+o(1))z_t^{-2}
 {d_0(x,y)^2\over d_0(x)d_0(y)}.
 \tag{6.3}
\]

The weighted conditioned form of (6.2) is precisely the surviving
pair-link predictable mean-contraction gate (CM).  An aggregate version
sufficient for (3.2) would also suffice.  What the present audit removes
is any doubt about factorial priority reweighting: it is ordinary
deletion.  What it does not remove is the need to prove that the surviving
decorations are not concentrated on the initially rare common-link core.

No coefficient-one conclusion follows from deletion monotonicity alone.
