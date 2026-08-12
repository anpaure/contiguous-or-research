# Adjacent pair-omission intervals: exact legality, global flatness, and floor descent

Date: 2026-07-25

Method: pure mathematics only.  No computation, search, solver, or
long-running job is used.

## 0. Outcome

This note audits the common-base adjacent-priority chart against
`PAIR_PRIORITY_SWAP_EXACT_FLOOR_ENERGY_AUDIT_20260725.md`.
There is no contradiction between the two conclusions.

Let

\[
 n=2m+1,
 \qquad A=P_j,
 \qquad B=P_{j+1},
\]

and let

\[
 \theta=(a_1\ b_1)(a_2\ b_2)
\]

exchange the two coordinates of \(A=\{a_1,a_2\}\) with those of
\(B=\{b_1,b_2\}\).  Choose the two local factors with

\[
 F_B=\theta F_A.
\tag{0.1}
\]

The coherent first-avoided matchings for the orders

\[
 \cdots,A,B,\cdots
 \quad\hbox{and}\quad
 \cdots,B,A,\cdots
\]

are denoted by \(M^-\) and \(M^+\).  They differ exactly on

\[
 \mathcal D_j=\left\{S\in\binom{[n]}{m-1}:
 S\cap(A\cup B)=\varnothing,
 \ S\cap P_h\ne\varnothing\ (h<j)\right\}.
\tag{0.2}
\]

Break the occurrences of \(\mathcal D_j\) in every row of \(F_A\) into
maximal cyclic intervals.  Independently choosing phase \(A\) or phase
\(B\) on each such interval gives a full lower-saturating,
middle-injective token matching.  If \(r_j\) is the number of interval
bits, then

\[
 \boxed{
 r_j\le \min\{2j\operatorname{Cat}_{m-1},|\mathcal D_j|\},
 \qquad
 J(M_\varepsilon)-J(M^-)\le2r_j.}
\tag{0.3}
\]

For arbitrary finite nonnegative signed-depth weights \(w_q^\pm\), put

\[
 \mathcal C_j=
 \sum_{q=1}^H w_q^+
 \sum_{U:\,U\cap B\ne\varnothing}
 \binom{\mu_{q,U}}2,
\tag{0.4}
\]

where \(\mu_{q,U}\) is the number of changed phase-\(A\) tokens whose
upper depth-\(q\) flag is \(U\).  For \(H\le m-2\), the doubled,
floor-corrected energy satisfies the exact identity

\[
 \boxed{
 \mathbb E_\varepsilon\mathcal Q_w(M_\varepsilon)
 =\mathcal Q_w(M^-)-\mathcal C_j
 =\mathcal Q_w(M^+)-\mathcal C_j.}
\tag{0.5}
\]

Hence some literal interval corner obeys

\[
 \boxed{
 \mathcal Q_w(M_\varepsilon)
 \le \mathcal Q_w(M^-)-\mathcal C_j,\qquad
 J(M_\varepsilon)\le J(M^-)+2r_j.}
\tag{0.6}
\]

This is floor-corrected descent, not merely a positive raw Gram form.
Every activated unordered duplicate contributes exactly its weight to the
guaranteed descent, while one interval bit creates at most two new physical
runs.

The global pair swap remains rankwise energy-flat.  In the global cube all
interval bits are forced to be equal, so its variance is the full coherent
square and its Haar gap is zero.  Independent interval bits have smaller
variance; the missing cross terms are exactly (0.4).  A mixed interval
corner is not the image of \(M^-\) under one global coordinate
permutation, so the global flatness theorem does not apply to it.

No constant-one conclusion is claimed.  The chart fixes every lower flag
and every upper flag avoiding \(B\); charged coverage of those invariant
sectors, and compatibility of different adjacent charts in one joint
cube, remain open.

## 1. The exact changed domain

Let \(\kappa^-\) and \(\kappa^+\) be the first-avoided maps in the two
orders.  A lower set which fails an earlier pair is decided before the
swap.  A lower set which avoids \(A\) but meets \(B\) is assigned to
\(A\) in both orders, and the symmetric statement holds with \(A,B\)
interchanged.  A set meeting both is assigned to neither.  Thus a set
changes phase if and only if it meets every earlier pair and avoids both
\(A,B\), proving (0.2).

The exact carrier size is

\[
 |\mathcal D_j|
 =\sum_{h=0}^{j-1}(-1)^h\binom{j-1}{h}
   \binom{2m-3-2h}{m-1},
\tag{1.1}
\]

with the usual convention that an impossible binomial coefficient is
zero.  This is inclusion-exclusion over the earlier pairs missed by an
\((m-1)\)-set in the \((2m-3)\)-point complement of \(A\cup B\).

Use the predecessor token convention in a row
\(\pi=(x_0,\ldots,x_{2m-2})\):

\[
 S_i=I_\pi(i,m-1),
 \qquad Y_i=I_\pi(i-1,m).
\tag{1.2}
\]

If \(S_i\) has first avoided pair \(P\), then \(Y_i\) still meets all
earlier pairs because it contains \(S_i\), and it still avoids \(P\)
because the entire row lies in \([n]\setminus P\).  Thus \(S_i\) and
\(Y_i\) have the same category.  Within one category the length-\(m\)
windows of the exact local factor are all distinct.  Therefore both
\(M^-\) and \(M^+\) saturate every lower target once and have distinct
middle owners.

For \(S\in\mathcal D_j\), \(\theta S=S\) pointwise.  If \(e_A(S)\)
is its token in \(F_A\), then the conjugate row in \(F_B\) gives

\[
 \boxed{e_B(S)=\theta e_A(S).}
\tag{1.3}
\]

All tokens outside \(\mathcal D_j\) are identical in the two coherent
endpoints.

## 2. Every independent interval corner is a full matching

Write \(Y_A(S)\) for the middle owner of \(e_A(S)\), so that

\[
 Y_B(S)=\theta Y_A(S).
\tag{2.1}
\]

First consider two changed lower targets.  Suppose an \(A\)-choice at
\(S\) and a \(B\)-choice at \(T\) have the same owner:

\[
 Y_A(S)=Y_B(T)=\theta Y_A(T).
\tag{2.2}
\]

The left member avoids \(A\), while the right member avoids \(B\).
Their common value therefore avoids \(A\cup B\), so it is fixed by
\(\theta\).  Equation (2.2) now gives

\[
 Y_A(S)=Y_A(T).
\]

The predecessor-owner map in \(F_A\) is injective, hence \(S=T\).
A corner never chooses both tokens over the same lower target, so no mixed
collision occurs.  Same-phase changed owners are distinct by exactness of
\(F_A\) or \(F_B\).

It remains to check the unchanged background.  Every \(A\)-choice occurs
together with the full common background in the coherent matching
\(M^-\); every \(B\)-choice occurs with that same background in
\(M^+\).  Hence neither can collide with a background owner.  Two
background owners are distinct because they occur in both endpoint
matchings.

Finally, every lower target outside \(\mathcal D_j\) retains its one
background token, and every lower target in \(\mathcal D_j\) receives
exactly one of \(e_A(S),e_B(S)\).  Thus every tokenwise choice, and in
particular every interval-correlated choice, preserves both lower
saturation and distinct middle ownership.  The changed overlay consists
of one-lower-vertex alternating paths, or parallel two-cycles when
\(Y_A(S)=Y_B(S)\).

## 3. Exact physical interval and run accounting

In an \(F_A\)-row, the predicate \(S_i\in\mathcal D_j\) is

\[
 \bigl[S_i\cap B=\varnothing\bigr]
 \ \wedge\ 
 \bigwedge_{h<j}\bigl[S_i\cap P_h\ne\varnothing\bigr].
\tag{3.1}
\]

For one coordinate pair \(P\), the starts at which a length-\((m-1)\)
cyclic window avoids \(P\) form at most two circular intervals.  Their
indicator has at most four boundary edges.  The boundary of the Boolean
combination (3.1) is contained in the union of the boundary sets of its
\(j\) predicates.  It therefore has at most \(4j\) boundary edges and at
most \(2j\) cyclic components.

One local factor has exactly

\[
 R_m=\frac1{2m-1}\binom{2m-1}{m-1}
 =\operatorname{Cat}_{m-1}
\tag{3.2}
\]

rows.  Hence

\[
 r_j\le\min\{2jR_m,|\mathcal D_j|\}.
\tag{3.3}
\]

The conjugate row \(\theta\pi\in F_B\) has the same carrier starts,
because every \(S_i\in\mathcal D_j\) is fixed by \(\theta\).  Relative
to \(M^-\), changing one interval bit removes an all-selected interval
from its \(F_A\)-row and inserts the paired all-unselected interval in its
\(F_B\)-row.  Removing one contiguous all-one interval can increase the
cyclic run count by at most one, and inserting one contiguous all-zero
interval can increase it by at most one.  Therefore every corner obeys

\[
 J(M_\varepsilon)-J(M^-)\le2r_j.
\tag{3.4}
\]

The exact ratio

\[
 \frac{R_m}{W}
 =\frac{m(m+1)}{(2m-1)(2m)(2m+1)}
\tag{3.5}
\]

gives

\[
 \frac{H[J(M_\varepsilon)-J(M^-)]}{W}
 \le
 \frac{4jHm(m+1)}{(2m-1)(2m)(2m+1)}
 =O(jH/m).
\tag{3.6}
\]

There is also a uniform-in-\(j\) bound.  If \(N_j\) is the number of
first-avoided category-\(j\) lower targets, then

\[
 |\mathcal D_j|\le N_j
 \le C\sqrt m\binom{2m-1}{m-1}(3/4)^{j-1}.
\tag{3.7}
\]

Splitting at \(20\log m\) in (3.3) gives, uniformly in \(j\),

\[
 r_j=O(W\log m/m),
 \qquad
 J(M_\varepsilon)-J(M^-)=O(W\log m/m).
\tag{3.8}
\]

Thus the new runs are \(o(W/H)\) whenever \(H=o(m/\log m)\).  The
coherent first-avoided endpoint already has

\[
 J(M^-)=O(W\log^2m/m),
\tag{3.9}
\]

so every interval corner has \(J=o(W/H)\) whenever
\(H=o(m/\log^2m)\), in particular for
\(H=O(\sqrt{m\log m})\).  If a selected token is sampled uniformly,
the probability that its physical predecessor is absent is at most
\(J/T\), where

\[
 T=\binom n{m-1}=\frac{m}{m+2}W.
\tag{3.10}
\]

Consequently

\[
 \Pr(\text{predecessor selected}\mid\text{token selected})
 \ge1-J/T=1-o(1/H).
\tag{3.11}
\]

## 4. Exact positive joined Gram and lossless packetization

For \(1\le q\le H\le m-2\), let \(L_q(S),U_q(S)\) be the lower and
upper flags of the phase-\(A\) token.  Stack signed-rank load vectors in
the Hilbert norm

\[
 \|v\|_w^2
 =\sum_{q=1}^H
 \left(w_q^-\|v_q^-\|_2^2+w_q^+\|v_q^+\|_2^2\right),
\tag{4.1}
\]

where all \(w_q^\pm\) are finite and nonnegative.  Put

\[
 d_S=\phi(e_B(S))-\phi(e_A(S)).
\]

Because \(L_q(S)\subseteq S\) and \(\theta S=S\),

\[
 (d_S)_q^-=0,
 \qquad
 (d_S)_q^+=\delta_{\theta U_q(S)}-\delta_{U_q(S)}.
\tag{4.2}
\]

If \(U,V\subseteq[n]\setminus A\), expansion gives

\[
 \left\langle
 \delta_{\theta U}-\delta_U,
 \delta_{\theta V}-\delta_V
 \right\rangle
 =2\mathbf1_{\{U=V,\ U\cap B\ne\varnothing\}}.
\tag{4.3}
\]

Indeed, a cross equality \(U=\theta V\) forces the common set to avoid
both \(A,B\), hence to be fixed by \(\theta\), and therefore reduces to
the cancelling case \(U=V\) with \(U\cap B=\varnothing\).  It follows
that

\[
 \boxed{
 \langle d_S,d_T\rangle_w
 =2\sum_{q=1}^H w_q^+
 \mathbf1_{\{U_q(S)=U_q(T),\ U_q(S)\cap B\ne\varnothing\}}
 \ge0.}
\tag{4.4}
\]

For a maximal carrier interval \(I\), put

\[
 z_I=\sum_{S\in I}d_S.
\]

At depth \(q\le m-2\), the upper flags along one physical row are proper
cyclic windows of length \(m+q<2m-1\).  Distinct starts give distinct
sets.  Hence (4.4) makes the token innovations inside one interval
pairwise orthogonal:

\[
 \boxed{
 \|z_I\|_w^2=\sum_{S\in I}\|d_S\|_w^2.}
\tag{4.5}
\]

Thus the positive correlation needed for physical long blocks loses no
Gram curvature.

Let

\[
 \mu_{q,U}=|\{S\in\mathcal D_j:U_q(S)=U\}|,
\]

and define

\[
 A_j=\left\|\sum_Iz_I\right\|_w^2,
 \qquad
 V_j=\sum_I\|z_I\|_w^2.
\]

Equations (4.4)--(4.5) give, exactly,

\[
 \boxed{
 \begin{aligned}
 A_j&=2\sum_{q=1}^H w_q^+
       \sum_{U:\,U\cap B\ne\varnothing}\mu_{q,U}^2,\\
 V_j&=2\sum_{q=1}^H w_q^+
       \sum_{U:\,U\cap B\ne\varnothing}\mu_{q,U},\\
 A_j-V_j&=2\sum_{q=1}^H w_q^+
       \sum_{U:\,U\cap B\ne\varnothing}
       \mu_{q,U}(\mu_{q,U}-1)=4\mathcal C_j.
 \end{aligned}}
\tag{4.6}
\]

Every duplicate counted in (4.6) lies in two different interval blocks,
because one physical row has no repeated proper cyclic window.

## 5. Why the coherent global cube is flat

Every upper flag of a phase-\(P\) token contains its lower endpoint and
lies inside \([n]\setminus P\).  It therefore meets every pair earlier
than \(P\) and avoids \(P\): its first avoided category is again \(P\).
Thus upper target coordinates split into disjoint first-avoided strata.

On the union of the \(A\)- and \(B\)-strata, \(\theta\) bijects all
phase-\(A/B\) tokens used by \(M^-\) with all phase-\(A/B\) tokens used
by \(M^+\), and (0.1) carries every upper flag to its \(\theta\)-image.
The loads outside this stratum are identical in the two endpoints.
Consequently, at every upper depth, the endpoint load vectors differ only
by a permutation inside a disjoint target block.  Their factorial floor
energies are equal.

For lower flags, only \(S\in\mathcal D_j\) changes token, and every such
lower flag is a subset of the pointwise fixed set \(S\).  Hence the lower
load vectors are identical.  Every middle load is \(0/1\), by Section 2,
and therefore has zero factorial floor excess.  We have proved the exact
rankwise identity

\[
 \boxed{\mathcal Q_{w,q}^\pm(M^-)=
        \mathcal Q_{w,q}^\pm(M^+)\quad\text{for every signed depth}.}
\tag{5.1}
\]

This is precisely the global pair-symmetric flatness theorem.  It says
nothing about a corner which applies \(\theta\) to some physical intervals
and not to others.  In Gram language, forcing all interval signs to be one
global sign gives

\[
 V_{\mathrm{global}}
 =\left\|\sum_Iz_I\right\|_w^2=A_j,
\tag{5.2}
\]

so its Haar gap is zero.  Independent interval signs instead give

\[
 V_{\mathrm{interval}}=\sum_I\|z_I\|_w^2=V_j,
\tag{5.3}
\]

and the removed cross-interval coherence is

\[
 A_j-V_j=4\mathcal C_j.
\]

This is why the finer chart evades, rather than contradicts, global
rankwise flatness.

## 6. Exact floor-corrected descent

Every interval corner has exactly \(T=\binom n{m-1}\) flags at every
signed depth.  For a target rank of size \(K\), write

\[
 T=cK+\delta,
 \qquad0\le\delta<K,
 \qquad\lambda=T/K,
 \qquad B=\frac{\delta(K-\delta)}K.
\tag{6.1}
\]

For an integral load vector \(x\) of mass \(T\), use the doubled
factorial floor excess

\[
 Q(x)=\sum_Z(x_Z-c)(x_Z-c-1)
 =\|x-\lambda\mathbf1\|_2^2-B.
\tag{6.2}
\]

The floor term \(B\) is identical at every corner.  With fair independent
Rademacher interval signs \(\varepsilon_I\in\{-1,+1\}\),

\[
 f_\varepsilon
 =\frac{f^-+f^+}{2}+\frac12\sum_I\varepsilon_Iz_I,
\]

so

\[
 \mathbb E\mathcal Q_w(M_\varepsilon)
 =\frac{\mathcal Q_w(M^-)+\mathcal Q_w(M^+)}2
  -\frac{A_j-V_j}{4}.
\tag{6.3}
\]

Substituting (5.1) and (4.6) proves (0.5):

\[
 \boxed{
 \mathbb E\mathcal Q_w(M_\varepsilon)
 =\mathcal Q_w(M^-)
  -\sum_{q=1}^H w_q^+
    \sum_{U:\,U\cap B\ne\varnothing}\binom{\mu_{q,U}}2.}
\tag{6.4}
\]

Because every corner satisfies the deterministic run bound (0.3), at
least one corner simultaneously satisfies both inequalities in (0.6).
If the half floor excess \(\Phi=Q/2\) is used, the guaranteed descent in
(6.4) is divided by two.

There is also an exact consistency inequality.  Applying (6.4) at one
upper depth and using nonnegativity of the integral floor excess gives

\[
 w_q^+\sum_{U:\,U\cap B\ne\varnothing}
       \binom{\mu_{q,U}}2
 \le \mathcal Q_{w,q}^+(M^-).
\tag{6.4a}
\]

Thus the refined chart never promises more descent than the coherent
endpoint actually contains.  In the globally correlated cube the same
collision reservoir is hidden because all cross-interval terms remain in
the variance; independent interval bits expose it.

The exceptional first upper rank is nonsingular in this formulation.  Its
target count is \(K=W\), while

\[
 T=\frac{m}{m+2}W,
 \qquad c_1^+=0,
 \qquad B_1=\frac{2m}{(m+2)^2}W.
\tag{6.5}
\]

Thus

\[
 Q_1^+(x)=\sum_Ux_U(x_U-1),
\]

and (6.4) remains exact with any finite \(w_1^+\).  One must not write
\(1/c_1^+\) for the autonomous token-core floor.

## 7. Certified boundary

The interval theorem closes four points with the exact quantifiers needed
by the block-rounding gate:

1. every independent interval corner is a genuine lower-saturating,
   middle-injective matching;
2. predecessor failure is \(o(1/H)\) and the added run count is at most
   \(2r_j=O(W\log m/m)\) uniformly in \(j\);
3. global pair-symmetric flatness is retained at the two coherent
   endpoints but does not extend to mixed interval corners;
4. the guaranteed integral descent is the floor-corrected collision count
   (0.4), not merely the raw Gram gap.

What remains is equally exact.  The chart has no lower-flag innovation,
and its upper innovation vanishes on targets avoiding \(B\).  Moreover,
the recursively conjugate adjacent charts form separate cubes sharing one
base; mutual owner-disjointness for simultaneous bits from different
adjacent positions is not proved.  Finally, if a later completion adds a
common load which is not \(\theta\)-symmetric on the affected stratum,
the average-versus-endpoints identity (6.3) survives, but equality of the
two completed endpoint energies need not.  More exactly, if \(r_q\) is
the common completion and

\[
 z_q=\mu_q(M^+)-\mu_q(M^-),
\]

then their completed-energy difference is

\[
 2\sum_qw_q^+\langle r_q,z_q\rangle.
\]

The interval gain remains \(\mathcal C_j\) below their average, and hence
lies below both completed endpoints whenever

\[
 \mathcal C_j\ge
 \left|\sum_qw_q^+\langle r_q,z_q\rangle\right|.
\]

A \(\theta\)-invariant completion makes this cross term zero.  Charged
all-sector coverage and a low-run completion with this compatibility are
the remaining constant-one statements.
