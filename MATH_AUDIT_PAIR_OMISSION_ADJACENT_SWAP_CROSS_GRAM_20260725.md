# Audit of the adjacent-priority conjugate-factor cross-Gram theorem

Date: 2026-07-25

Method: pure mathematics only.  No computation, search, solver, or
long-running job is used.

## 0. Scope and verdict

This note audits only Sections 0--6 of
`MATH_ATTACK_PAIR_OMISSION_ADJACENT_SWAP_CROSS_GRAM_20260725.md`.
Proposition 7.2 and every conclusion depending on it are outside the scope
of this audit and are not certified here.

The conjugate-factor theorem has a correct core:

* after an adjacent priority swap, arbitrary runwise choices between the
  two conjugate tokens do extend to a full lower-saturating,
  middle-injective matching;
* the upper-flag Gram is entrywise nonnegative and has exactly the factor
  stated below;
* packetizing a maximal physical interval loses no variance for
  (H\le m-2);
* the number of packets and the added physical runs have the required
  (o(W/H)) bounds in the stated ranges.

Two corrections/quantifier restrictions are essential.

1. The symbols (c_q\ge1) in the attack note cannot be the actual token
   floor capacities.  Here the total flag mass is
   (T=\binom{2m+1}{m-1}), and the first upper floor is exactly
   (c_1^+=0).  Every occurrence of (1/c_q) in Sections 0--5 must be
   read instead as an arbitrary finite nonnegative upper-rank weight
   (w_q^+).  With that replacement the floor-corrected identity is
   exact, including (q=1,+).
2. The successive choice
   (F_{P_{j+1}}=\theta_jF_{P_j}) supplies a menu of individually legal
   adjacent charts sharing one endpoint.  It does **not** prove that bits
   from distinct adjacent charts may be chosen simultaneously.  Thus
   (0.10) and (6.5) are certified as cumulative menu-size bounds, not as
   the boundary count of one joint hypercube of matchings.

The proof of Lemma 2.1 in the attack note also omitted collisions with the
unchanged background.  Section 2 below supplies the missing argument; it
does not require a new hypothesis.

## 1. Exact carrier and endpoint matchings

Put

\[
 n=2m+1,\qquad A=P_j,\qquad B=P_{j+1},
\]

and let

\[
 \theta=(a_1\ b_1)(a_2\ b_2)
\]

for fixed labellings (A=\{a_1,a_2\}),
(B=\{b_1,b_2\}).  Assume (F_B=\theta F_A).  The two priority orders
differ at precisely

\[
 \mathcal D_j=\left\{S\in\binom{[n]}{m-1}:
 S\cap(A\cup B)=\varnothing,
 \ S\cap P_h\ne\varnothing\ (h<j)\right\}.
\tag{1.1}
\]

Indeed, a set failing an earlier pair is decided earlier; a set avoiding
exactly one of (A,B) is assigned to that same pair in both orders; and a
set meeting both is assigned to neither.  A set meeting every earlier pair
and avoiding both moves from (A) to (B), proving (1.1).

The predecessor token convention also gives genuine endpoint matchings.
If (S=I_\pi(i,m-1)) has first avoided pair (P), then

\[
 Y=I_\pi(i-1,m)=S\cup\{x_{i-1}\}
\]

still meets every earlier pair and still avoids (P).  Hence (S) and
(Y) have the same first-avoided category.  The length-(m) windows in
one exact local factor are globally distinct, and different categories
are disjoint.  Thus the predecessor owners are distinct.  This proves that
both coherent endpoints (M^-,M^+) are lower-saturating matchings.

For (S\in\mathcal D_j), one has (\theta S=S).  Therefore its two
tokens satisfy

\[
 e_B(S)=\theta e_A(S).
\tag{1.2}
\]

Outside (\mathcal D_j), the selected token is literally the same in the
two endpoints.

## 2. Full-matching legality, including the unchanged background

Let (Y_A(S)) and (Y_B(S)=\theta Y_A(S)) be the two possible middle
owners for (S\in\mathcal D_j).  If

\[
 Y_A(S)=Y_B(T)=\theta Y_A(T),
\tag{2.1}
\]

then the common set avoids (A), because the left member lies in (F_A),
and avoids (B), because the right member lies in (F_B).  It is therefore
fixed by (\theta).  Applying (\theta) to (2.1) gives
(Y_A(S)=Y_A(T)), and exactness of (F_A) gives (S=T).  The same proof
handles the reverse mixed equality.  Thus differently oriented changed
tokens can collide only when they belong to the same lower target, in
which case a corner chooses only one of them.

It remains to include the common background, which the submitted proof did
not discuss.  Let (b(R)) be the common token at a lower target
(R\notin\mathcal D_j).  Then:

* (b(R)) cannot collide with (e_A(S)), because both occur in the
  matching (M^-);
* (b(R)) cannot collide with (e_B(S)), because both occur in the
  matching (M^+);
* two background tokens cannot collide, because they occur in both
  endpoints.

Together with the mixed-orientation argument, this exhausts all pairs of
selected edges.  Consequently every independent tokenwise choice on
\(\mathcal D_j\), and hence every runwise-correlated choice, is a full
lower-saturating, middle-injective matching.  The changed symmetric
difference consists exactly of length-two alternating paths with one lower
vertex, together with parallel two-cycles when the two owners coincide.

## 3. Correct floor ledger

Every corner has exactly

\[
 T=\binom n{m-1}
\tag{3.1}
\]

flags at each signed depth.  For

\[
 N_q^\pm=\binom n{m\pm q},\qquad
 \frac{T}{N_q^\pm}=c_q^\pm+\vartheta_q^\pm,
 \qquad
 c_q^\pm=\left\lfloor\frac{T}{N_q^\pm}\right\rfloor,
\tag{3.2}
\]

one has, exactly,

\[
 \frac TW=\frac{m}{m+2},\qquad
 c_1^+=0,\qquad c_1^-=1,\qquad c_2^+=1.
\tag{3.3}
\]

In particular the displayed (1/c_q) weights in the attack note are
undefined if (c_q) denotes the actual upper floor.  Let instead
(w_q^\pm\ge0) be arbitrary finite weights and define the unhalved floor
energy

\[
 \mathcal Q_w(M)=
 \sum_{q\le H}\sum_{\epsilon\in\{-,+\}}w_q^\epsilon
 \sum_{|R|=m+\epsilon q}
 (\mu_{q,R}^\epsilon-c_q^\epsilon)
 (\mu_{q,R}^\epsilon-c_q^\epsilon-1).
\tag{3.4}
\]

Here (m+(-)q) means (m-q).  If

\[
 f_{q,R}^\epsilon=mu_{q,R}^\epsilon-T/N_q^\epsilon,
\]

then fixed total mass gives the exact identity

\[
 \mathcal Q_w(M)=\|f(M)\|_w^2-
 \sum_{q,\epsilon}w_q^\epsilon N_q^\epsilon
 \vartheta_q^\epsilon(1-\vartheta_q^\epsilon).
\tag{3.5}
\]

At (q=1,+), (3.4) is simply
(w_1^+\sum_R\mu_R(\mu_R-1)); there is no singularity.  Thus every
quadratic Gram identity below transfers exactly to floor-energy
differences.  If the half floor polynomial is used instead, all energy
drifts below are divided by two.

## 4. Exact Gram factors and lossless physical packetization

For (S\in\mathcal D_j), let (U_q(S)) be the upper flag of its
(F_A)-token and put (d_S=\phi_B(S)-\phi_A(S)).  Every lower flag is a
subset of (S), so

\[
 (d_S)_q^-=0,
 \qquad
 (d_S)_q^+=\delta_{\theta U_q(S)}-\delta_{U_q(S)}.
\tag{4.1}
\]

For (U,V\subseteq[n]\setminus A), expansion of the four unit-vector
terms gives

\[
 \left\langle\delta_{\theta U}-\delta_U,
 \delta_{\theta V}-\delta_V\right\rangle
 =2\mathbf1_{\{U=V,\ U\cap B\ne\varnothing\}}.
\tag{4.2}
\]

To justify the absence of negative cross terms, an equality
(U=\theta V) would make the common set avoid both (A) and (B), hence
fix it under (\theta), and therefore force (U=V).  Consequently

\[
 \boxed{
 \langle d_S,d_T\rangle_w
 =2\sum_{q=1}^H w_q^+
 \mathbf1_{\{U_q(S)=U_q(T),\ U_q(S)\cap B\ne\varnothing\}}
 \ge0.}
\tag{4.3}
\]

This certifies the factor (2) in (0.2).

Break the starts of (\mathcal D_j) in every (F_A)-row into maximal
cyclic intervals (I), and put (z_I=\sum_{S\in I}d_S).  For
(H\le m-2), every (U_q(S)) is a proper cyclic window of length
(m+q<2m-1).  Distinct starts in one row therefore give distinct upper
sets.  Equation (4.3) makes the corresponding innovations orthogonal, so

\[
 \|z_I\|_w^2=\sum_{S\in I}\|d_S\|_w^2.
\tag{4.4}
\]

Writing

\[
 \mu_{q,U}=|\{S\in\mathcal D_j:U_q(S)=U\}|,
\]

and

\[
 \mathfrak A_j=\left\|\sum_Iz_I\right\|_w^2,
 \qquad
 \mathfrak V_j=\sum_I\|z_I\|_w^2,
\]

one obtains exactly

\[
 \boxed{
 \begin{aligned}
 \mathfrak A_j
 &=2\sum_{q\le H}w_q^+
   \sum_{U:U\cap B\ne\varnothing}\mu_{q,U}^2,\\
 \mathfrak V_j
 &=2\sum_{q\le H}w_q^+
   \sum_{U:U\cap B\ne\varnothing}\mu_{q,U},\\
 \mathfrak A_j-\mathfrak V_j
 &=2\sum_{q\le H}w_q^+
   \sum_{U:U\cap B\ne\varnothing}
       \mu_{q,U}(\mu_{q,U}-1).
 \end{aligned}}
\tag{4.5}
\]

Thus the gap is nonnegative, and it is strictly positive exactly when an
activated upper target occurs at least twice at a depth having positive
weight.

For fair independent interval signs,

\[
 \boxed{
 \mathbb E\mathcal Q_w(M_\varepsilon)
 =\frac{\mathcal Q_w(M^-)+\mathcal Q_w(M^+)}2
 -\frac{\mathfrak A_j-\mathfrak V_j}{4}.}
\tag{4.6}
\]

Equivalently, the exact unhalved-energy gain below the endpoint average is

\[
 \frac12\sum_{q\le H}w_q^+
 \sum_{U:U\cap B\ne\varnothing}
 \mu_{q,U}(\mu_{q,U}-1).
\tag{4.7}
\]

This certifies the factors in (0.5)--(0.6), after the required weight
correction.

## 5. Exact interval and run accounting

One local factor has

\[
 R_m=\frac1{2m-1}\binom{2m-1}{m-1}
 =\operatorname{Cat}_{m-1}
\tag{5.1}
\]

rows, and

\[
 \frac{R_m}{W}
 =\frac{m(m+1)}{(2m-1)(2m)(2m+1)}
 =\frac{m+1}{2(2m-1)(2m+1)}.
\tag{5.2}
\]

For one coordinate pair (C), the starts whose length-((m-1)) window
avoids (C) form at most two circular intervals and hence have at most
four boundary edges.  Membership in (\mathcal D_j) inside an (F_A)-row
is a Boolean combination of the (j) avoidance predicates belonging to
(B,P_1,\ldots,P_{j-1}).  Its boundary is contained in the union of their
boundaries, so it has at most (4j) boundary edges and at most (2j)
cyclic components.  Therefore the number (r_j) of run bits obeys the
slightly sharper bound

\[
 \boxed{r_j\le\min\{2jR_m,\ |\mathcal D_j|\}.}
\tag{5.3}
\]

The attack note's (4jR_m) bound is consequently valid but not sharp.

Switching one maximal interval can increase the run count in its old
(F_A)-row by at most one and in its new paired (F_B)-row by at most one.
For every corner,

\[
 \boxed{J(M_\varepsilon)\le J(M^-)+2r_j
 \le J(M^-)+4jR_m.}
\tag{5.4}
\]

Since (J(M^-)=O(W\log^2m/m)), the base cost remains (o(W/H)) for
(H=o(m/\log^2m)).  The added cost from the elementary bound is

\[
 \frac{4jHR_m}{W}
 =\frac{4jHm(m+1)}{(2m-1)(2m)(2m+1)}
 =O(jH/m),
\tag{5.5}
\]

which is (o(1)) under (jH=o(m)).

Let (N_j) be the number of lower sets whose first avoided pair is
(P_j).  The first-avoided tail estimate gives

\[
 N_j\le C\sqrt m\binom{2m-1}{m-1}(3/4)^{j-1},
\tag{5.6}
\]

and (\mathcal D_j\subseteq\{S:\kappa(S)=j\}).  Taking
(t=\lceil20\log m\rceil) in (5.3) yields

\[
 \sum_{j=1}^{m-1}r_j
 \le\sum_{j\le t}2jR_m+\sum_{j>t}N_j
 =O(W\log^2m/m).
\tag{5.7}
\]

Hence the cumulative number of run variables in the entire menu is
(o(W/H)) whenever (H=o(m/\log^2m)).  All constants and powers in the
attack note's weaker (6.2)--(6.6) bounds are therefore certified.

## 6. Common-base adjacent menu: exact quantifiers

Choose (F_{P_1}) arbitrarily and define inductively

\[
 F_{P_{j+1}}=\theta_jF_{P_j}\qquad(1\le j<m).
\tag{6.1}
\]

Because (\theta_j) maps ([n]\setminus P_j) bijectively to
([n]\setminus P_{j+1}), every (F_{P_{j+1}}) is an exact local factor.
Let (M^0) be the first-avoided matching in the order
(P_1,\ldots,P_m).  For each fixed (j), let (M^{(j)}) use the order
with only (P_j,P_{j+1}) interchanged.  Sections 1--5 apply to the pair
((M^0,M^{(j)})).  Thus all (m-1) charts exist with one common endpoint,
and the catalog bounds (0.10) and (5.7) are valid.

What has not been proved is that alternative tokens belonging to
different (j)'s are mutually middle-disjoint.  The singleton-component
argument in Section 2 compares only the two phases of one fixed adjacent
swap.  Therefore no product of the (m-1) run cubes, and no simultaneous
choice of bits from different adjacent charts, follows from (6.1).

In particular (Ht^2=o(m)) correctly says that the first (t) **separate
charts** have cumulative catalog size (o(W/H)); it is not yet a boundary
theorem for one matching using all (t) charts.

## 7. Precise proved boundary

The audited theorem gives a literal low-run interpolation and a computed
nonnegative cross-Gram.  The first version of this audit left an unnecessary
endpoint-skew condition here.  The exact first-avoided stratum argument in
`PAIR_PRIORITY_SWAP_EXACT_FLOOR_ENERGY_AUDIT_20260725.md` removes it for
the pair-symmetric token core: at every signed rank,

\[
 \mathcal Q_{w,q}^\pm(M^-)=\mathcal Q_{w,q}^\pm(M^+).
\tag{7.1}
\]

Indeed the two upper endpoint profiles differ by the coordinate
permutation (\theta) on the disjoint union of their (A/B) first-avoided
strata; lower profiles are identical and middle profiles are injective.
Consequently (4.6) gives the exact floor-corrected descent

\[
 \mathbb E\mathcal Q_w(M_\varepsilon)
 =\mathcal Q_w(M^-)
 -\frac{\mathfrak A_j-\mathfrak V_j}{4}.
\tag{7.2}
\]

Thus a positive duplicate census does put a runwise corner strictly below
both coherent endpoints.  The global pair-symmetric swap remains flat
because forcing all interval signs equal changes the variance from
(\mathfrak V_j) to (\mathfrak A_j), making the gap zero.  Independent
interval signs are not induced by one global coordinate permutation.

The surviving gates are charged coverage of the lower and fixed-upper
sectors, and cross-(j) middle-disjointness (or another legal recombination
theorem) for a joint atlas.  A later common completion must also preserve
the affected-stratum symmetry if descent below both *completed* endpoints
is to follow directly.  No constant-one conclusion is certified.
