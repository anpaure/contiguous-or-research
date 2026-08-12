# Buffered slow bites: the column-energy obstruction and the exact sufficient hierarchy

Date: 2026-07-27

Scope: repaired promotion-ring owner packing and the claimed direct
growing-rank slow-greedy trajectory.

## 0. Verdict

The moving order buffer in
`MATH_THEOREM_REPAIRED_RING_GROWING_UNIFORMITY_SLOW_BITE_TRAJECTORY_20260726.md`
does repair the *old* formal error that an order-
\(L-1\) generator term can leave an order-\(L\) hierarchy in one step.
It does **not** prove Lemma 5.1 of that note.

The remaining failure is orthogonal to order depth.  If an aggregate mesh
energy is

\[
                  Y=\sum_{C}w_C A_C^h,
\tag{0.1}
\]

and selection of \(g\) decreases \(A_C\) by \(B_C(g)\), then the
quadratic variation and the large-jump compensator depend on the
**column sums**

\[
             Z_Y(g):=\sum_Cw_CA_C^{h-1}B_C(g).
\tag{0.2}
\]

The catalogue estimates (3.11)--(3.12) in the claimed proof control
rowwise powers such as

\[
                 \sum_{C,g} B_C(g)^\ell .
\tag{0.3}
\]

They do not control

\[
                 \sum_g Z_Y(g)^2
        \quad\hbox{or}\quad
                 \sum_g Z_Y(g)^J .
\tag{0.4}
\]

Expanding (0.4) creates mixed diagrams in which one selected edge \(g\)
meets several *different* protected clusters.  Those diagrams are not
the powers of one cluster recorded by (3.12).  The spanning-forest
paragraph in the proof asserts their bound but supplies no inequality
which implies it.  In fact the implication from (0.3) to (0.4) is false,
as the explicit breadth model in Section 2 shows.

The exact repaired statement is:

\[
\boxed{
 \text{the buffered trajectory follows from aggregate column-link
 energies (ACLE), but ACLE is not proved by the current mesh catalogue.}
}
\tag{0.5}
\]

Consequently Theorem 0.1 and the claimed matching
\(|Q|\ge(1-m^{-1/20}-o(1))N_H\) are **not presently proved**.  They remain
valid conditional consequences of ACLE together with the already stated
drift and weighted-cleaning estimates.

## 1. The exact generator quantity

Fix a stopped protected-cluster family \(\mathcal C\).  For every
\(C\in\mathcal C\), let \(A_C\ge0\) be its current link count and let

\[
 B_C(g)=\#\{\text{options counted by }A_C
                   \text{ which are killed by selecting }g\}.
\tag{1.1}
\]

Thus \(0\le B_C(g)\le A_C\).  With \(Y\) as in (0.1), one jump has

\[
\begin{aligned}
 D_Y(g)&:=Y-Y^{(g)}\\
 &=\sum_Cw_C\bigl(A_C^h-(A_C-B_C(g))^h\bigr).
\end{aligned}
\tag{1.2}
\]

For \(h\ge1\),

\[
 0\le D_Y(g)
 \le h\sum_Cw_CA_C^{h-1}B_C(g)
 =hZ_Y(g).
\tag{1.3}
\]

At edge rate \(\nu_t=(K\mathcal D_R(t))^{-1}\), the predictable
quadratic variation is therefore

\[
 {d\langle M_Y\rangle_t\over dt}
 =\nu_t\sum_gD_Y(g)^2
 \le h^2\nu_t\sum_gZ_Y(g)^2.
\tag{1.4}
\]

Likewise, for every \(b>0\) and integer \(J\ge2\), the compensator of
jumps larger than \(bY\) is at most

\[
 {h^J\over b^JY^J}\,
             \nu_t\sum_g Z_Y(g)^J.
\tag{1.5}
\]

Equations (1.4)--(1.5) are exact.  They identify the least information a
Freedman argument must supply.  Notice that it is a statement about
columns indexed by the *same* \(g\), not separate power sums for each
protected cluster.

### The missing mixed diagram

Already for

\[
                  Y=\sum_e a_X(e)^2,
\tag{1.6}
\]

one has, to first order,

\[
 Z_Y(g)=\sum_e a_X(e)b_X(e,g).
\tag{1.7}
\]

The square in (1.4) contains

\[
 \sum_{e\ne e'}a_X(e)a_X(e')b_X(e,g)b_X(e',g).
\tag{1.8}
\]

This counts two different link options/protected clusters coupled by one
common next edge.  A power
\((B_X^{\boldsymbol c}(e_1,\ldots,e_j))^\ell\) instead makes every one of
its \(\ell\) link copies meet the *same whole protected tuple*.  It does
not equal (1.8), and (1.8) is not obtained by binomial inversion inside
one tuple.

Thus the assertion in the proof of Lemma 5.1 that every quadratic or
higher jump term is already an energy from (3.13) is false.

## 2. Explicit breadth obstruction to the scalar implication

The logical failure can be seen without any asymptotics.  Let there be
\(P\) protected clusters and \(Q\) possible next edges.  Put

\[
                         A_C=1\qquad(C=1,\ldots,P).
\tag{2.1}
\]

Choose a biregular bipartite incidence graph between clusters and next
edges in which every next edge has degree

\[
                         a=\lceil\eta P\rceil
\tag{2.2}
\]

and put

\[
 B_C(g)=\mathbf1_{\{C\sim g\}}.
\tag{2.3}
\]

For every \(\ell\ge1\), all scalar row powers are identical:

\[
                 \sum_{C,g}B_C(g)^\ell=Qa.
\tag{2.4}
\]

In particular, increasing \(\ell\) produces no extra protection.  On
the other hand, with \(Y=P\), every possible jump has

\[
                 D_Y(g)=a\ge\eta Y,
\qquad
                 \sum_gD_Y(g)^\ell=Qa^\ell.
\tag{2.5}
\]

Thus the large-jump column moment is larger than the scalar row moment by
the factor \(a^{\ell-1}\).  The discrepancy can be arbitrarily large.

This model is directly relevant to the claimed use of (3.12).  The
dynamic mesh clusters can be heavily depleted, so that \(A_C=1\), while
the right sides of (3.11)--(3.12) are normalized by the factorial-scale
owner degree rather than by the current \(A_C\).  Hence those inequalities
allow (2.4) for polynomial \(P,Q\).  One next edge may then move a positive
fraction of the depleted clusters at once.  This is a one-step breadth
event: it advances each individual cluster by only one witness level, so
an \(L_i-J\) versus \(L_i\) order buffer does not attach \(J\) small
factors to it.

The model is an obstruction to the *proof implication*, not a
counterexample asserted to occur inside the repaired promotion-ring
catalogue.  Ruling it out in that catalogue is precisely the missing
aggregate column-link theorem.

## 3. The exact weakest stopped-generator condition

The following formulation avoids any ambiguity about which mesh diagrams
are required.

### Definition 3.1 (ACLE on an interval)

Let \(I=[t_0,t_1]\), and let \(Y\) be a stopped nonnegative aggregate
observable with positive deterministic reference \(y(t)\).  Fix
\(0<\eta<1\), \(b>0\), and an integer \(J\ge2\).  ACLE for \(Y\) on
\(I\) consists of:

1. **drift:** after applying the integrating factor defined by \(y\),
   the total normalized predictable drift error is at most \(o(\eta)\);

2. **column quadratic energy:** before the stopping time,

   \[
    \int_I {h^2\over y(t)^2}
       {1\over K\mathcal D_R(t)}
       \sum_g Z_Y(g,t)^2\,dt\le v;
   \tag{3.1}
   \]

3. **column large-jump energy:**

   \[
    \int_I {h^J\over b^Jy(t)^J}
       {1\over K\mathcal D_R(t)}
       \sum_g Z_Y(g,t)^J\,dt\le\delta.
   \tag{3.2}
   \]

The same definition is used incidence-weightedly: (3.1)--(3.2) may fail
on owners whose current degree mass is \(o(E_t)\).

This condition is weaker than the pointwise dynamic ratio estimate

\[
            B_C(g)/A_C\le C(j+1)^4/(m^2u_t),
\tag{3.3}
\]

and stronger than the scalar row-power catalogue.  It asks for exactly
the predictable quantities appearing in Freedman's inequality, no more.

There is a clean intermediate sufficient condition which identifies the
precise missing normalization.  Suppose that, for \(\ell=2,J\), every
nonexceptional current cluster satisfies the **relative row estimate**

\[
 {1\over K\mathcal D_R}
       \sum_g\left({B_C(g)\over A_C}\right)^\ell
 \le \epsilon_\ell
 \qquad(A_C>0).
\tag{3.3a}
\]

Then ACLE follows automatically, with no separate expansion of cross
terms.  Indeed, put

\[
 p_C={w_CA_C^h\over Y},\qquad
 r_C(g)={B_C(g)\over A_C}.
\]

The \(p_C\)'s form a probability distribution and

\[
 {Z_Y(g)\over Y}=\sum_Cp_Cr_C(g).
\]

Jensen therefore gives, for every \(\ell\ge1\),

\[
 {1\over K\mathcal D_R}\sum_g
       \left({Z_Y(g)\over Y}\right)^\ell
 \le
 \sum_Cp_C,{1\over K\mathcal D_R}
       \sum_g r_C(g)^\ell
 \le\epsilon_\ell.
\tag{3.3b}
\]

Thus the diagonal link-energy condition (4.1) from the weighted-RPRN
note really is sufficient.  What (3.11)--(3.12) fail to provide after
restriction is the factor \(A_C^\ell\) on the right of (3.3a): their
normalization remains a factorial-scale catalogue envelope.  The breadth
model in Section 2 exploits exactly this gap.

### Theorem 3.2 (stopped ACLE trajectory lemma)

Suppose that at every one of \(O(\log m)\) checkpoints, all degree,
internal-pair, and core bridge observables needed for a fresh slow-greedy
interval satisfy ACLE after weighted quarantine.  Suppose uniformly

\[
 \eta=m^{-1/10},qquad
 v\le C T\varepsilon_*,qquad
 b={T\varepsilon_*\over\eta},qquad
 \delta\le e^{-c(\log m)^2},
\tag{3.4}
\]

where

\[
 T={K\over20}\log m,qquad
 \varepsilon_*={C(\log m)^8\over m^2z^2},qquad
 z=m^{-1/20}.
\tag{3.5}
\]

Assume also that the total normalized quarantine loss is \(o(1)\).
Then the direct slow-greedy process reaches root density
\(z(1+o(1))\), and its matching leaves \(o(W)\) owners.

#### Proof

Normalize by the integrating factor \(y(t)\) and stop at the first
\(\eta\)-deviation.  By (1.4) and (3.1), the clipped martingale has total
quadratic variation at most \(v\).  Formula (1.5) and (3.2) show that the
compensator of a jump larger than \(b\) is at most \(\delta\).  Freedman's
inequality therefore gives

\[
 \Pr\left(\sup_{t\in I}|Y(t)/y(t)-1|>2\eta\right)
 \le
 2\exp\left[-{c\eta^2\over v+b\eta}\right]+\delta.
\tag{3.6}
\]

Here the drift contribution is absorbed by item 1 of ACLE.  From
(3.4),

\[
 v+b\eta=O(T\varepsilon_*),
\qquad
 {\eta^2\over T\varepsilon_*}
 \ge {c m^{7/10}\over(\log m)^9}.
\tag{3.7}
\]

Consequently (3.6) is at most \(e^{-c'(\log m)^2}\).  Average the stopped
failure indicator over roots and incidence-weightedly over owners.
Markov's inequality gives, simultaneously at all \(O(\log m)\)
checkpoints, bad root mass and bad owner incidence

\[
                 e^{-c''(\log m)^2}=o(1/m)
\tag{3.8}
\]

of their respective totals.  The weighted quarantine lemma then removes
only \(o(E_t)\) active edges and \(o(N)\) roots in total.

On the remaining core, the degree and drift estimates give

\[
                    {dx\over dt}=-{x\over K}(1+o(1)).
\tag{3.9}
\]

Since \(T=(K/20)\log m\), integration yields

\[
                    x(T)=m^{-1/20}(1+o(1)).
\tag{3.10}
\]

If \(s=(z+o(1))N\) roots are missed, the exact repaired-ring ledger is

\[
 W-r(N-s)=W-rN+rs
 =O\left(\left({H+\kappa\over m}+z\right)W\right)=o(W).
\tag{3.11}
\]

This proves the assertion. \(\square\)

## 4. What a genuine buffer must contain

A sufficient combinatorial implementation of ACLE is a **full mixed
column-diagram hierarchy**.  A diagram has:

* several link-option rows, all through the same base resource;
* several protected/selected edge columns;
* every prescribed owner-intersection witness between a row and a
  column; and
* the equality partition of coincident link rows.

If a column has \(t\) witness incidences, one incidence is the ordinary
first-order deletion hazard and the other \(t-1\) incidences are the
small transverse constraints.  Thus the correct excess order is

\[
             \omega(\Gamma)=
             \#\{\text{witness incidences}\}
             -\#\{\text{nonempty columns}\}.
\tag{4.1}
\]

The static endpoint exposure suggests the bound

\[
 Z_\Gamma(0)
 \le D_X^{,a}(K D)^{,b}
       \left({C|\Gamma|^4\over m^2}\right)^{\omega(\Gamma)},
\tag{4.2}
\]

where \(a\) and \(b\) are the numbers of link rows and edge columns.
Unlike (3.12), this includes diagrams with one common column attached to
different protected tuples, hence includes (1.8).

For a moving buffer to be valid, one must prove the stopped dynamic
version of (4.2), incidence-weightedly, through

\[
 J=C_0\log m,qquad L=C_1(\log m)^2,
\tag{4.3}
\]

with the following rule: the centered generator may add a new column;
a one-incidence column is absorbed into the reference drift, while a
column of size \(t\ge2\) raises \(\omega\) by \(t-1\).  A term crossing
from a core at distance \(J\) to the outer boundary then really does
carry at least \(J\) factors of

\[
                    {CL^4\over m^2u_t^2}.
\tag{4.4}
\]

This full diagram assertion implies (3.1)--(3.2) by expanding the powers
of (0.2), and hence implies Theorem 3.2.  It is the correct buffered
hierarchy.  Establishing (4.2) dynamically is still a theorem: the
one-row endpoint catalogue in the claimed proof does not establish it.

## 5. Audit of the claimed owner packing theorem

The following parts of the slow-greedy note survive this audit:

1. the exact root/owner leave ledger;
2. the reference trajectory and time change;
3. the time-zero one-row multiplicity mesh estimates, subject to their
   separate combinatorial audit;
4. the numerical smallness
   \(T\varepsilon_*=O(m^{-9/10}(\log m)^9)\); and
5. weighted quarantine once a stopped failure estimate is available.

The following implication does not survive:

\[
 \text{(3.11)--(3.12) + an additive order buffer}
 \quad\Longrightarrow\quad
 \text{Lemma 5.1's failure probability (5.2)}.
\tag{5.1}
\]

It fails because a large aggregate jump can be broad rather than deep.
The order buffer prices depth; ACLE prices breadth.  Both are necessary.

Therefore the rigorous current statement is

\[
\boxed{
 \text{ACLE (or the full mixed column-diagram buffer) implies the
 desired owner matching; ACLE remains unproved.}
}
\tag{5.2}

No counterexample to the existence of a near-perfect owner matching is
proved here.  What is proved is that the advertised direct trajectory
proof has not established one.

## 6. Addendum: the first literal column term is a tree

The abstract breadth obstruction does not occur at the first literal
column term once the stopped influence maximum

\[
                         a_X(e)\le A
\]

is available.  The companion note
`MATH_THEOREM_FIRST_COLUMN_BREADTH_ENERGY_REPAIRED_RING_20260727.md`
proves, with \(L=K\Delta_t\),

\[
 \sum_g\left(\sum_ea_X(e)b_X(e,g)\right)^2
 \le d_t(X)L^3A^3.
\]

The proof is an exact tree-homomorphism count in the bipartite conflict
incidence graph.  More generally every column moment of
\(\sum_ea_X(e)^h\) has the factor
\((A/d_t(X))^{\ell-1}\).

Thus the first ACLE breadth observable is now proved **conditionally on
the stopped relative influence scale**.  This sharpens, but does not
reverse, the audit verdict: the unresolved step is regeneration (or a
high-moment substitute) for
\(A/d_t(X)=O(\operatorname{polylog}(m)/m^2)\).  The scalar buffer note did
not prove that step.
