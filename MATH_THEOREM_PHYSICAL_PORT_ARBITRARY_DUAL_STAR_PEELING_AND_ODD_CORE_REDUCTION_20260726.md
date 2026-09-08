# Arbitrary physical port duals: owner-star synchronization and the residual odd-holonomy core

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input is
used.

> **Independent audits.** The owner-star randomization, all \(D,\Lambda\),
> \(B_X\) factors, pair-codegree charging, and the two cover-number scales
> were checked independently. A second audit checked the matching LP,
> \(D+\mu\) pair-core constant, clique-sum identity, balanced reduction,
> local-ratio peeling, and Theorem B after the explicit scope corrections
> now incorporated below. No theorem-falsifying defect remains; the two
> fixed-rank and balanced-matrix inputs are identified as imported results.

## 0. Result and exact boundary

Let \(\mathcal H_m^\#=(V,\mathscr C)\) be the independently selected
physical strip-port hypergraph from the localized Boolean-envelope theorem.
Write

\[
 D=D_1,
 \qquad
 \mu=\Delta _2(\mathcal H_m^\#),
 \tag{0.1}
\]

so every nonmiddle target has degree exactly \(D\), every middle target has
degree at most \(D\), and

\[
 \mu\le (4+o(1)){D\over m}.
 \tag{0.2}
\]

The same selected outcome has the off-edge-star bound

\[
 \Lambda:=
 \max_{\substack{v\notin e_E^\#}}
 \bigl|\{C:v\in e_C^\#,\ e_C^\#\cap e_E^\#\ne\varnothing\}\bigr|
 \le 2\widehat\rho_mD,
 \tag{0.3}
\]

where

\[
 \widehat\rho_m
 =O\!\left({1\over m}+{h\over m^{3/2}}\right)+o(m^{-A})
 \tag{0.4}
\]

for every fixed \(A\), at the stated physical strip scales. Finally, the
independently audited Boolean-envelope theorem supplies a uniform number

\[
 \beta_m=o(D/\sqrt m)
 \tag{0.5}
\]

such that every non-star intersecting physical family obeys

\[
 |\mathcal F|\le\beta_m.
 \tag{0.5a}
\]

Consequently, for every nonnegative weight field \(z\) on
\(\mathcal F\),

\[
 z(\mathcal F)\le \beta_m\max_{C\in\mathcal F}z_C.
 \tag{0.6}
\]

The main new theorem is not restricted to intersecting supports.

### Theorem A (weighted owner-star synchronization)

Let \(y_C\ge0\), and put

\[
 \nu_y=\max_{M\text{ a matching}}\sum_{C\in M}y_C.
 \tag{0.7}
\]

Choose a set \(X\subseteq V\) of \(q\) targets, and let \(\mathcal S\) be
any set of positive-weight strips meeting \(X\). Define the exact
multi-owner energy

\[
 B_X(y;\mathcal S)
 =\sum_{C\in\mathcal S}y_C\bigl(|e_C^\#\cap X|-1\bigr).
 \tag{0.8}
\]

If \((q-1)\Lambda<D\), then

\[
 \boxed{
 y(\mathcal S)
 \le
 {D\nu_y+B_X(y;\mathcal S)
  \over 1-(q-1)\Lambda/D}.}
 \tag{0.9}
\]

Moreover,

\[
 B_X(y;\mathcal S)
 \le {q\choose2}\mu\nu_y,
 \tag{0.10}
\]

and consequently

\[
 \boxed{
 y(\mathcal S)
 \le
 D\nu_y\,
 {1+{q\choose2}\mu/D
  \over 1-(q-1)\Lambda/D}.}
 \tag{0.11}
\]

In particular, if \(X\) covers the whole support of \(y\), then

\[
 {y(\mathscr C)\over\nu_y}
 \le
 D\,
 {1+(2+o(1))q(q-1)/m
  \over 1-2(q-1)\widehat\rho_m}.
 \tag{0.12}
\]

Thus every arbitrary, possibly non-clique dual support satisfies

\[
 y(\mathscr C)\le(1+o(1))D\nu_y
 \tag{0.13}
\]

whenever its target-cover number is \(o(\sqrt m)\). At both audited strip
choices, target-cover \(o(m^{1/4})\) gives the stronger estimate

\[
 y(\mathscr C)
 \le\bigl(D+o(D/\sqrt m)\bigr)\nu_y.
 \tag{0.14}
\]

This proves a genuine arbitrary-support portion of the fractional
edge-colouring gate. It does not prove the result for supports with
Gaussian-or-larger target-cover number.

The remaining reduction is also rigorous. Classical projective planes are
non-star cliques and are eliminated by (0.6). Coherent graph odd sets are
pair-core supports and have fractional chromatic index at most

\[
 D+\mu=D+O(D/m).
 \tag{0.15}
\]

Every support admitting a conflict-preserving generator of sufficiently
slowly growing rank \(r_*(m)\to\infty\) has

\[
 \chi'\le(1+o(1))D.
 \tag{0.16}
\]

Every support admitting a balanced conflict representation has the exact
bound

\[
 \chi_f'\le D.
 \tag{0.17}
\]

Therefore a constant-factor counterexample, if one exists, is necessarily
a high-cover, non-clique, non-pair-core, unbalanced, rank-diverging
matching-dual atom. Its strong odd Berge cycles must be interlocked so
that every star or bounded-rank peel is blocked by the rest of the
support. No such physical atom is constructed here.

## 1. The exact fractional-colouring LP

Let \(\mathfrak M\) be the set of physical matchings. Then

\[
 \chi_f'(\mathcal H_m^\#)
 =\min\left\{
   \sum_{M\in\mathfrak M}\lambda_M:
   \sum_{M\ni C}\lambda_M\ge1\ (C\in\mathscr C),\quad
   \lambda_M\ge0
   \right\}.
 \tag{1.1}
\]

Its dual is

\[
 \chi_f'(\mathcal H_m^\#)
 =\max\left\{
   \sum_Cy_C:
   y_C\ge0,\quad
   \sum_{C\in M}y_C\le1\ (M\in\mathfrak M)
   \right\}.
 \tag{1.2}
\]

Equivalently,

\[
 \boxed{
 \chi_f'(\mathcal H_m^\#)
 =\sup_{0\ne y\ge0}{y(\mathscr C)\over\nu_y}.}
 \tag{1.3}
\]

If

\[
 P_M=\operatorname {conv}\{\mathbf1_M:M\in\mathfrak M\},
 \tag{1.4}
\]

then

\[
 \boxed{
 \chi_f'(\mathcal H_m^\#)\le L
 \quad\Longleftrightarrow\quad
 L^{-1}\mathbf1_{\mathscr C}\in P_M.}
 \tag{1.5}
\]

For the forward direction, normalize a fractional colouring to a
probability distribution on matchings. Its marginal vector dominates
\(L^{-1}\mathbf1\); independently thinning selected edges, or using the
downward closure of \(P_M\), gives equality. The reverse direction is
immediate by rescaling a convex decomposition.

Let \(A\) be the target-by-strip incidence matrix. Exact target regularity
gives

\[
 D^{-1}\mathbf1_{\mathscr C}
 \in P^*:=\{x\ge0:Ax\le\mathbf1\}.
 \tag{1.6}
\]

The gate is precisely the passage from the fractional packing polytope
\(P^*\) to the integral matching polytope \(P_M\).

For later use, the weighted fractional matching value is

\[
 \nu_y^*
 =\max\{y^Tx:x\ge0,\ Ax\le\mathbf1\}
 =\min\{\mathbf1^Tz:z\ge0,\ A^Tz\ge y\}.
 \tag{1.7}
\]

It has the following exact star-decomposition form:

\[
 \boxed{
 \nu_y^*
 =\min
 \left\{
  \sum_{v\in V}\|y^{(v)}\|_\infty:
  y=\sum_vy^{(v)},\quad
  y^{(v)}\ge0,\quad
  \operatorname {supp}y^{(v)}\subseteq\operatorname {Star}(v)
 \right\}.}
 \tag{1.8}
\]

Indeed, a dual cover \(z\) gives each edge \(C\) total capacity
\(\sum_{v\in C}z_v\ge y_C\); distribute \(y_C\) among those capacities
and obtain \(\|y^{(v)}\|_\infty\le z_v\). Conversely, any displayed
decomposition gives the feasible cover
\(z_v=\|y^{(v)}\|_\infty\).

Equation (1.8) is the exact sense in which every fractional obstruction is
a collection of target-star fields. The missing fact is not a star
decomposition; it is the synchronization of those fields into common
physical matchings. Theorem A proves that synchronization when the number
of relevant owner stars is small enough.

## 2. Proof of the owner-star synchronization theorem

Assign every \(C\in\mathcal S\) one owner

\[
 \phi(C)\in e_C^\#\cap X.
 \tag{2.1}
\]

Writing \(X=\{v_1,\ldots,v_q\}\), put

\[
 \mathcal F_i=\{C\in\mathcal S:\phi(C)=v_i\}.
 \tag{2.2}
\]

The families \(\mathcal F_i\) partition \(\mathcal S\), and
\(|\mathcal F_i|\le D\). Pad each \(\mathcal F_i\) with null slots until it
has exactly \(D\) slots. Independently and uniformly choose one slot from
each \(\mathcal F_i\). Delete every chosen physical strip which conflicts
with another chosen physical strip. The survivors form a matching.

The expected raw chosen weight is

\[
 {y(\mathcal S)\over D}.
 \tag{2.3}
\]

For ordered \(i\ne j\), the expected weight from \(\mathcal F_i\) lost to
a collision with the chosen member of \(\mathcal F_j\) is at most

\[
 {1\over D^2}
 \sum_{C\in\mathcal F_i}y_C
 \bigl|\{E\in\mathcal F_j:e_C^\#\cap e_E^\#\ne\varnothing\}\bigr|.
 \tag{2.4}
\]

If \(v_j\notin e_C^\#\), the cardinality in (2.4) is at most \(\Lambda\)
by (0.3). If \(v_j\in e_C^\#\), use only the trivial bound \(D\).
Summing (2.4) over all ordered pairs gives total expected deleted weight
at most

\[
 {(q-1)\Lambda\over D^2}y(\mathcal S)
 +{1\over D}
 \sum_{i=1}^q\sum_{C\in\mathcal F_i}
 y_C\,\bigl|(e_C^\#\cap X)\setminus\{v_i\}\bigr|.
 \tag{2.5}
\]

The last sum is exactly \(B_X(y;\mathcal S)\), independently of the
choice of owner map. Hence some realized matching has weight at least

\[
 {y(\mathcal S)\over D}
 \left(1-{(q-1)\Lambda\over D}\right)
 -{B_X(y;\mathcal S)\over D}.
 \tag{2.6}
\]

It cannot exceed \(\nu_y\). Rearranging (2.6) proves (0.9).

For \(t\ge1\), \(t-1\le\binom t2\). Therefore

\[
\begin{aligned}
 B_X(y;\mathcal S)
 &\le
 \sum_{C\in\mathcal S}y_C
   { |e_C^\#\cap X|\choose2}\\
 &=
 \sum_{\{u,v\}\in\binom X2}
 \sum_{C\in\mathcal S:\{u,v\}\subseteq e_C^\#}y_C.
\end{aligned}
 \tag{2.7}
\]

Every inner family has at most \(\mu\) strips, while

\[
 y_C\le\nu_y
 \tag{2.8}
\]

because a singleton strip is a matching. Thus (2.7) is at most
\(\binom q2\mu\nu_y\), proving (0.10), (0.11), and (0.12).

The proof permits arbitrary weights, arbitrary conflicts inside and
between the owner stars, and arbitrary multi-owner strips. The two losses
have distinct meanings:

* \((q-1)\Lambda/D\) is the ordinary cross-star collision probability;
* \(B_X\) is the exact repeated-owner incidence which cannot be charged by
  the off-edge estimate because the second owner already lies in the
  strip.

No independence of physical target ownership is asserted; the only
randomness is an averaging device applied after the exact selected port
outcome has been fixed.

## 3. Quantitative consequences and residual intersecting clusters

From (0.2), (0.3), and (0.11),

\[
 {y(\mathcal S)\over D\nu_y}
 \le
 {1+(2+o(1))q(q-1)/m
  \over1-2(q-1)\widehat\rho_m}.
 \tag{3.1}
\]

Consequently the sufficient conditions are exactly

\[
 q\widehat\rho_m+{q^2\over m}=o(1)
 \tag{3.2}
\]

for \((1+o(1))D\), and

\[
 q\widehat\rho_m+{q^2\over m}=o(m^{-1/2})
 \tag{3.3}
\]

for \(D+o(D/\sqrt m)\).

At the default choice \(h=m^{2/3+o(1)}\),

\[
 \widehat\rho_m=m^{-5/6+o(1)}.
 \tag{3.4}
\]

At the optimized choice

\[
 h=\sqrt m\log m\,L_m,
 \qquad L_m\to\infty,\quad L_m=m^{o(1)},
 \tag{3.5}
\]

one has

\[
 \widehat\rho_m=O(\log m\,L_m/m).
 \tag{3.6}
\]

At either choice, \(q=o(\sqrt m)\) implies (3.2), while
\(q=o(m^{1/4})\) implies (3.3).

There is a useful partial-cover version. Suppose

\[
 y=y^0+z^1+\cdots+z^r
 \tag{3.7}
\]

coordinatewise, where \(\operatorname {supp}y^0\) is covered by \(X\)
and every \(\operatorname {supp}z^j\) is intersecting but not contained
in one target star. Then Theorem A and (0.6) give

\[
 \boxed{
 y(\mathscr C)
 \le
 D\nu_y
 {1+{q\choose2}\mu/D
  \over1-(q-1)\Lambda/D}
 +\beta_m\sum_{j=1}^r\max_Cz_C^j.}
 \tag{3.8}
\]

Here each matching value for a component field is at most \(\nu_y\)
because the decomposition is coordinatewise nonnegative. In particular,
if the residual families form an ordinary cover rather than a weight
decomposition, assign each residual strip to one ambient family and extend
the assigned weight by zero on the other members of that ambient
non-star family. Applying (0.6) to the ambient families gives

\[
 y(\mathscr C)
 \le
 D\nu_y
 {1+(2+o(1))q(q-1)/m
  \over1-2(q-1)\widehat\rho_m}
 +r\beta_m\nu_y.
 \tag{3.9}
\]

This is a precise stars-plus-non-star-clusters theorem. It shows what a
decomposition must preserve: not merely shore cardinality, but the common
matching normalization \(\nu_y\).

There is an alternative pair-core atlas criterion which does not require
one small target cover. If

\[
 y=\sum_{j=1}^su^j+\sum_{i=1}^rz^i
 \tag{3.10}
\]

coordinatewise, every \(u^j\) has pair-core support, and every \(z^i\)
has non-star intersecting support, then (0.6) and (4.4) below give

\[
 \boxed{
 y(\mathscr C)
 \le
 (D+\mu)\sum_{j=1}^s\nu_{u^j}
 +\beta_m\sum_{i=1}^r\max_Cz_C^i.}
 \tag{3.11}
\]

Consequently, for nonnegative \(\eta_m,\kappa_m\),

\[
 \sum_j\nu_{u^j}\le(1+\eta_m)\nu_y,
 \qquad
 \sum_i\max_Cz_C^i\le\kappa_m\nu_y
 \tag{3.12}
\]

imply

\[
 y(\mathscr C)
 \le\bigl((D+\mu)(1+\eta_m)+\beta_m\kappa_m\bigr)\nu_y.
 \tag{3.13}
\]

Thus \(\eta_m=o(1)\) and \(\beta_m\kappa_m=o(D)\) suffice for the
qualitative coefficient-one bound. The sharper compiler scale requires
\(\eta_m=o(m^{-1/2})\) and
\(\beta_m\kappa_m=o(D/\sqrt m)\). This formulation isolates the exact
matching-value additivity which a many-star decomposition must retain.

## 4. Pair cores and all bounded physical conflict templates

### 4.1 The exact pair-core constant

Suppose \(\mathcal Q\subseteq\mathscr C\) has a pair-core representation:
each strip \(C\) is assigned an unordered target pair \(\pi(C)\subseteq
e_C^\#\), and

\[
 e_C^\#\cap e_E^\#\ne\varnothing
 \quad\Longleftrightarrow\quad
 \pi(C)\cap\pi(E)\ne\varnothing.
 \tag{4.1}
\]

The representing loopless multigraph has maximum degree at most \(D\) and
maximum edge multiplicity at most \(\mu\). The fractional multigraph
edge-colouring formula gives

\[
 \chi_f'
 =\max\left\{
 \Delta,
 \max_{\substack{U\subseteq V\\|U|\text{ odd},\ |U|\ge3}}
 {2|E(U)|\over|U|-1}
 \right\}.
 \tag{4.2}
\]

For \(s=|U|\),

\[
 {2|E(U)|\over s-1}
 \le
 \min\left\{{Ds\over s-1},\ \mu s\right\}.
 \tag{4.3}
\]

If \(\mu(s-1)\le D\), the second term is at most \(D+\mu\). If
\(\mu(s-1)>D\), the first term is strictly less than \(D+\mu\). Hence

\[
 \boxed{
 \chi_f'(\mathcal Q)\le D+\mu.}
 \tag{4.4}
\]

This sharpens the previous \(D+2\mu\) ledger. It eliminates every coherent
odd cycle, odd set, and graph blow-up at the stronger
\(D+o(D/\sqrt m)\) scale.

### 4.2 Conflict-generator rank

For \(\mathcal Q\subseteq\mathscr C\), define
\(\operatorname {cgr}(\mathcal Q)\) to be the least \(r\) for which one
can choose

\[
 \varnothing\ne g_C\subseteq e_C^\#,
 \qquad 1\le |g_C|\le r,
 \tag{4.5}
\]

such that

\[
 e_C^\#\cap e_E^\#\ne\varnothing
 \quad\Longleftrightarrow\quad
 g_C\cap g_E\ne\varnothing
 \qquad(C\ne E\in\mathcal Q).
 \tag{4.6}
\]

Thus \(g_C\) retains literal physical targets and preserves the complete
conflict graph. Target stars have generator rank one, and pair-core
supports have generator rank at most two. Requiring \(g_C\ne\varnothing\)
loses nothing: if an empty generator were allowed, its strip would be
isolated in \(\mathcal Q\); retaining any one of its physical targets adds
a target used by no other strip of \(\mathcal Q\), hence creates no new
conflict.

We use the following standard theorem as an imported result.

> **Imported fixed-rank sparse-codegree edge-colouring theorem.** For
> every fixed \(r\) and \(\varepsilon>0\), there are
> \(\delta(r,\varepsilon)>0\) and \(\Delta_0(r,\varepsilon)\) such that
> every finite simple \(r\)-uniform hypergraph of maximum degree \(\Delta\ge
> \Delta_0\) and maximum pair-codegree at most \(\delta\Delta\) has
> chromatic index at most \((1+\varepsilon)\Delta\).

This theorem is not reproved here.

### Theorem 4.1 (slow-rank diagonal)

There are functions

\[
 r_*(m)\longrightarrow\infty,
 \qquad
 \varepsilon_m\longrightarrow0,
 \tag{4.7}
\]

such that every physical subfamily \(\mathcal Q\) with
\(\operatorname {cgr}(\mathcal Q)\le r_*(m)\) satisfies

\[
 \boxed{
 \chi'(\mathcal Q)\le(1+\varepsilon_m)D.}
 \tag{4.8}
\]

#### Proof

Fix an integer \(j\). Choose the imported theorem with rank \(j+1\) and
error \(1/j\). Before applying it, adjoin at least one edge-private
auxiliary target to every generator and then pad every generator to common
rank \(j+1\). The resulting hypergraph is simple and uniform, has the same
conflict graph, has maximum degree \(\max\{\Delta_g,1\}\), and has
pair-codegree at most \(\max\{\mu,1\}\). Since
\(j\max\{\mu,1\}/D\to0\) and \(D/j\to\infty\), there is
\(M_j\) such that its codegree and degree thresholds hold for all
\(m\ge M_j\). Choose \(M_j\ge j\), make the sequence strictly
increasing, and put

\[
 r_*(m)=\max\bigl(\{j:m\ge M_j\}\cup\{0\}\bigr).
 \tag{4.9}
\]

This tends to infinity, deliberately with no claimed rate.

Let generators of rank at most \(j=r_*(m)\) have maximum target degree
\(\Delta_g\). If \(\Delta_g<D/j\), greedy colouring of their line graph
gives

\[
 \chi'\le j(\Delta_g-1)+1<D.
 \tag{4.10}
\]

If \(\Delta_g\ge D/j\), the padded pair-codegree obeys

\[
 {\Delta_2(g_{\rm pad})\over\Delta_g}
 \le {j\max\{\mu,1\}\over D}.
 \tag{4.11}
\]

The imported theorem gives

\[
 \chi'\le(1+1/j)\Delta_g\le(1+1/j)D.
 \tag{4.12}
\]

For the finitely many \(m<M_1\), take \(r_*(m)=0\); the assertion is
vacuous for nonempty supports because generators are nonempty. The
edge-private padding creates neither physical conflicts nor a
pair-codegree larger than one on any new target pair. Diagonalizing the
finitely many initial \(m\)'s into \(\varepsilon_m\) proves (4.8).
\(\square\)

Theorem 4.1 is qualitative. Since \(r_*(m)\) may grow arbitrarily slowly,
it does not supply the additive \(o(D/\sqrt m)\) rate. It must not be
applied with the full growing physical edge rank \(K\).

An exact integer formulation of \(\operatorname {cgr}(\mathcal Q)\le r\)
uses variables \(z_{C,v}\in\{0,1\}\) and \(w_{CE,v}\in\{0,1\}\):

\[
 1\le\sum_{v\in e_C^\#}z_{C,v}\le r,
 \tag{4.13}
\]

\[
 w_{CE,v}\le z_{C,v},\qquad
 w_{CE,v}\le z_{E,v},
 \tag{4.14}
\]

and, for every conflicting pair \(C,E\),

\[
 \sum_{v\in e_C^\#\cap e_E^\#}w_{CE,v}\ge1.
 \tag{4.15}
\]

Thus failure of every slowly growing generator is an exact, literal
port-holonomy obstruction rather than an abstract set representation.

## 5. Balanced representations and the precise odd obstruction

A \(0\)-\(1\) matrix is balanced if it has no square submatrix of odd
order with exactly two ones in each row and each column. Equivalently, its
incidence hypergraph has no strong odd Berge cycle.

We use the standard balanced-matrix integrality theorem: if \(A\) is
balanced, then

\[
 \{x\ge0:Ax\le\mathbf1\}
 \tag{5.1}
\]

is integral. This imported theorem is not reproved here.

### Theorem 5.1 (balanced coefficient one)

If a physical support \(\mathcal Q\) admits a conflict-preserving target
generator with every generator edge nonempty, as in (4.5), and whose
incidence matrix is balanced, then

\[
 \boxed{\chi_f'(\mathcal Q)\le D.}
 \tag{5.2}
\]

#### Proof

The generator has maximum target degree at most \(D\), so
\(D^{-1}\mathbf1_{\mathcal Q}\) belongs to (5.1). By integrality, it lies
in the convex hull of incidence vectors of generator matchings. Since the
generator preserves all conflicts, these are exactly physical matchings.
Now apply (1.5). \(\square\)

There is also a self-contained edge-colouring proof after accepting
balanced integrality. At maximum degree \(\Delta\), the uniform point
\(1/\Delta\) lies in the matching polytope. On every target of degree
\(\Delta\), its constraint is tight. In a convex decomposition, every
matching of positive coefficient therefore covers every such target.
Delete one of those matchings; the maximum degree drops to
\(\Delta-1\), balancedness is inherited, and induction gives exactly
\(\Delta\) colours.

For \(\mathcal Q\subseteq\mathscr C\), define its balanced-transversal
cost

\[
 \operatorname {bct}(\mathcal Q)
 =\min\{\chi_f'(Z):Z\subseteq\mathcal Q,\
       A_{\mathcal Q\setminus Z}\text{ is balanced}\}.
 \tag{5.3}
\]

Here \(A\) is the full physical target incidence; using a balanced
subgenerator could only improve the bound. Colouring \(Z\) and
\(\mathcal Q\setminus Z\) with disjoint palettes gives

\[
 \boxed{
 \chi_f'(\mathcal Q)\le D+\operatorname {bct}(\mathcal Q).}
 \tag{5.4}
\]

Consequently, for every weight field and every fixed such \(Z\),

\[
 y(\mathcal Q)\le D\nu_y+y(Z)
 \tag{5.5}
\]

whenever deleting \(Z\) leaves a balanced incidence matrix.

Hence, if

\[
 \chi_f'(\mathcal Q)>(1+\varepsilon)D,
 \tag{5.6}
\]

then every strip set meeting all strong odd Berge cycles of this full
physical incidence matrix has fractional chromatic cost greater than
\(\varepsilon D\). In particular, if such a
transversal \(Z\) has a rank-\(r\) conflict generator of maximum degree
\(\Delta_Z\), greedy colouring implies

\[
 r(\Delta_Z-1)+1>\varepsilon D.
 \tag{5.7}
\]

Thus a surviving odd obstruction is not one finite determinant-two
minor. It is a family of odd minors whose every bounded-generator edge
transversal has linear local load.

Physical chronology does permit the audited holonomy triangle

\[
 \begin{pmatrix}
 0&1&1\\
 1&0&1\\
 1&1&0
 \end{pmatrix},
 \qquad \det=2.
 \tag{5.8}
\]

That triangle has generator rank two and is covered by (4.4). A strong
odd cycle with no collateral conflicts is likewise a pair-core odd hole.
Therefore neither local determinant two nor an ordinary odd cycle is the
survivor; the necessary object is a rank-at-least-three interlocking of
many such cycles.

## 6. Clique separators and why projective obstructions do not survive

Let \(G\) be the conflict graph on physical strips. If

\[
 G=G_1\cup G_2,
 \tag{6.1}
\]

there are no edges between \(V(G_1)\setminus V(G_2)\) and
\(V(G_2)\setminus V(G_1)\), and \(G_1\cap G_2\) is a clique, then

\[
 \boxed{
 \chi_f(G)=\max\{\chi_f(G_1),\chi_f(G_2)\}.}
 \tag{6.2}
\]

To prove the upper bound, take rational \(a/b\) above both fractional
chromatic numbers and choose \(b\)-fold \(a\)-colourings. The vertices of
the common clique receive pairwise-disjoint \(b\)-sets of colours in both
colourings. A permutation of the \(a\) colours aligns these sets, after
which the two colourings glue. Let \(a/b\) decrease to the maximum.

Repeated clique-separator decomposition therefore reduces the problem
exactly to clique-cutset-free atoms. Target-star separators are legitimate
clique separators. Every atom which is itself a clique is already safe:

* if it is contained in one target star, it has at most \(D\) vertices;
* otherwise the verified Boolean-envelope theorem gives weighted ratio at
  most \(\beta_m=o(D/\sqrt m)\).

A literal projective plane is a non-star clique and is therefore in the
second class. A fixed projective or odd template also has bounded
conflict-generator rank and is covered by Theorem 4.1. Thus no ordinary
projective obstruction survives the physical chronology estimates.

What may survive is not a clique sum of those pieces. It must be a
clique-prime mesh whose different conflicts use different target stars
and whose odd minors cannot be removed at sublinear chromatic cost.

## 7. Exact matching-gain peeling

The remaining difficulty is not expressed by piecewise chromatic bounds
alone: different pieces may block one another's maximum matchings. The
following lemma records the exact missing compatibility.

For a weight field \(y\) and \(Q\subseteq\operatorname {supp}y\), put

\[
 y_Q=y\mathbf1_Q,
 \qquad
 \Delta_y(Q)=\nu_y-\nu_{y-y_Q}.
 \tag{7.1}
\]

Suppose a class of certified pieces has constants \(b(Q)\) such that,
for every \(w\) supported on \(Q\),

\[
 w(Q)\le b(Q)\nu_w.
 \tag{7.2}
\]

### Lemma 7.1 (local-ratio support peeling)

Fix \(L>0\). If every nonzero \(y\) has a nonempty certified
\(Q\subseteq\operatorname {supp}y\) satisfying

\[
 \boxed{
 \Delta_y(Q)\ge {b(Q)\over L}\nu_{y_Q},}
 \tag{7.3}
\]

then

\[
 \chi_f'(\mathcal H_m^\#)\le L.
 \tag{7.4}
\]

#### Proof

Induct on the number of positive coordinates of \(y\). The induction
hypothesis for \(y-y_Q\), (7.2), and (7.3) give

\[
\begin{aligned}
 y(\mathscr C)
 &=y(Q)+(y-y_Q)(\mathscr C)\\
 &\le b(Q)\nu_{y_Q}+L\nu_{y-y_Q}\\
 &\le L\Delta_y(Q)+L\nu_{y-y_Q}
 =L\nu_y.
\end{aligned}
 \tag{7.5}
\]

Apply (1.3). \(\square\)

For the present physical hypergraph one may take

\[
 b(Q)=
 \begin{cases}
 1,&Q\text{ is a singleton},\\
 D,&Q\text{ is contained in a target star},\\
 \mu,&Q\text{ is contained in the common link of two distinct targets},\\
 \beta_m,&Q\text{ is intersecting and non-star},\\
 D+\mu,&Q\text{ is pair-core},\\
 D,&Q\text{ has a balanced conflict representation},\\
 (1+\varepsilon_m)D,
   &\operatorname {cgr}(Q)\le r_*(m).
 \end{cases}
 \tag{7.6}
\]

This gives a clean sufficient theorem: it is enough to peel the support
by pieces in (7.6) while preserving the matching gain (7.3). It also
gives the exact obstruction.

### Corollary 7.2 (support-minimal obstruction certificate)

If \(\chi_f'>L\), there is a nonnegative weight field \(y\), with
support minimal among violating fields and normalized by \(\nu_y=1\),
such that

\[
 y(\mathscr C)>L
 \tag{7.7}
\]

and every nonempty proper certified piece satisfies

\[
 \boxed{
 \Delta_y(Q)<{b(Q)\over L}\nu_{y_Q}.}
 \tag{7.8}
\]

Indeed, the restriction \(y-y_Q\) has smaller support and hence total
weight at most \(L\nu_{y-y_Q}\). If (7.8) failed, adding (7.2) would
contradict (7.7).

For a non-star intersecting \(Q\), (7.8) becomes

\[
 \Delta_y(Q)=o(m^{-1/2})\max_{C\in Q}y_C.
 \tag{7.9}
\]

Thus every verified non-star clique is almost completely blocked by the
outside support. For a singleton \(Q=\{C\}\), it gives the sharper exact
condition

\[
 \nu_y-\nu_{y-y_C}< {y_C\over L}.
 \tag{7.10}
\]

For stars, pair links, pair cores, balanced pieces, and slowly
growing generators, (7.8) says that nearly all of the piece's optimal
matching weight is already redundant with the exterior. This is the
precise cross-piece monodromy which a decomposition theorem still has to
overcome.

There is a complementary global statement. If

\[
 \chi_f'>(1+\varepsilon)D
 \tag{7.11}
\]

and \(y\) is normalized as above, then deleting any subfamily whose
conflict components are all intersecting, balanced, or of generator rank
at most \(r_*(m)\) leaves at least

\[
 (\varepsilon-o(1))D
 \tag{7.12}
\]

of total dual weight. Otherwise the deleted part has weighted ratio at
most \((1+o(1))D\), and the total cannot exceed \((1+\varepsilon)D\).

## 8. The sharp residual theorem

Combining the preceding sections gives the following precise reduction.

### Theorem B (necessary form of a physical counterexample)

If, for some fixed \(\varepsilon>0\) and infinitely many \(m\),

\[
 \chi_f'(\mathcal H_m^\#)>(1+\varepsilon)D,
 \tag{8.1}
\]

then for each such \(m\) there is a nonnegative dual certificate \(y\),
normalized by \(\nu_y=1\), whose support may be chosen conflict-connected
and clique-cutset-free, and which has all of the following properties.

1. **High owner-cover complexity.** It is not covered by
   \(o(\sqrt m)\) physical targets. More quantitatively, every target set
   \(X\) with \((|X|-1)\Lambda<D\) obeys the exact restriction (0.9), so
   either its covered weight is small or its multi-owner energy \(B_X\)
   is large.

2. **No clique or projective core.** It is not intersecting. Every
   non-star intersecting subfamily has the negligible marginal gain
   (7.9).

3. **No global pair-core representation.** The whole support is not pair-core
   representable, since every such support has ratio at most \(D+\mu\).
   Proper pair-core subfamilies may occur, but (7.8) says they are
   matching-gain blocked by the exterior.

4. **Unbounded literal conflict rank.** Its conflict-generator rank is
   greater than \(r_*(m)\to\infty\).

5. **Strong odd-cycle mesh.** It admits no balanced conflict
   representation. Its full physical incidence matrix is unbalanced and
   therefore contains a strong odd Berge-cycle submatrix. Every edge
   transversal of all strong odd cycles of this full incidence matrix has
   fractional chromatic cost more than \(\varepsilon D\).

6. **Matching interlock.** Every proper certified star, intersecting,
   pair-core, balanced, or bounded-generator piece obeys (7.8). Thus no
   such piece can be peeled while retaining its natural share of the
   optimum matching.

Conversely, if for every fixed \(\varepsilon>0\) no certificates with
properties 1--6 exist for all sufficiently large \(m\), then
\(\chi_f'\le(1+o(1))D\). At the sharper annulus precision, it is enough to
exclude them with \(o(D/\sqrt m)\) in place of \(o(D)\), but Theorem 4.1
does not currently provide that rate.

#### Proof

Equations (1.2)--(1.3) give a dual certificate. Among all violating weight
fields, choose one with globally minimum support cardinality and normalize
it by \(\nu_y=1\). Its support is connected: otherwise fractional
chromatic number is the maximum over its conflict components, and a
proper component would itself admit a violating weight field. Its support
is also clique-cutset-free. Indeed, if it were a proper clique sum, (6.2)
would put fractional chromatic number greater than \((1+\varepsilon)D\)
on one proper summand, which would again admit a violating field of
smaller support. Thus global support minimality gives both structural
properties before Corollary 7.2 is applied.

Property 1 is Theorem A. Property 2 is (0.6) and (7.9). Property 3 is
(4.4). Property 4 is Theorem 4.1. If a balanced conflict representation
existed, Theorem 5.1 would contradict (8.1), proving the first part of
Property 5; (5.4) proves its transversal-cost statement. Property 6 is
Corollary 7.2. \(\square\)

The separating form is especially concise:

\[
 {1\over D}\mathbf1\in\{x\ge0:Ax\le\mathbf1\},
 \tag{8.2}
\]

but the residual weight satisfies

\[
 y(M)\le1\quad(M\in\mathfrak M),
 \qquad
 \left\langle y,{1\over D}\mathbf1\right\rangle>1+\varepsilon.
 \tag{8.3}
\]

Unlike a projective plane, the support of (8.3) is not intersecting.
Unlike an ordinary blossom, it cannot be encoded by target pairs. Unlike
a finite holonomy minor, it cannot be removed at sublinear chromatic cost.
This rank-diverging, matching-interlocked odd mesh is the precise surviving
physical obstruction.

## 9. Role and limitation of the Boolean-envelope kernel

For a feasible target label \(A\) of bounded span and a physical packet
\(P\) avoiding its Boolean envelope, the audited selected kernel gives

\[
 \Lambda_{\rm conc}=C_1(\log M+hH),
 \tag{9.0}
\]

where \(M\) is the number of raw physical strips, and

\[
 \sum_{T\in P}d^\#(A,T)
 \le4\eta_s(|P|)d^\#(A)+|P|\Lambda_{\rm conc},
 \qquad
 \eta_s(|P|)=O_s\!\left({1\over m}+{|P|\over m^2}\right)
 +\text{active-disjoint tail}.
 \tag{9.1}
\]

Its three adaptive contractions prove (0.6). This note uses that result as
a black box and does not redo its clique audit.

The kernel cannot simply be iterated on an arbitrary matching-dual
support. In a clique, every next witness must still meet every previous
witness, so the adaptive history remains in one common conditional link.
In a non-clique support, successive conflicts may be routed through
different strips and different target stars. Summing (9.1) over those
choices loses precisely the matching gain measured by \(\Delta_y(Q)\), or
equivalently the representative-collision terms in (0.9).

Thus the smallest remaining hypothesis is not another clique estimate.
It is either

* a general owner-star representative theorem extending (0.9) beyond
  \(q=o(\sqrt m)\), with multi-owner energy controlled by physical
  chronology; or
* the local-ratio matching-gain condition (7.3) for one of the certified
  physical pieces in every dual support.

Either statement would compose directly into \((1+o(1))D\). At the
constant-one compiler precision, the same statement needs additive error
\(o(D/\sqrt m)\).

## 10. Audited boundary

Proved here:

1. the exact LP and star-decomposition identities (1.3), (1.5), and
   (1.8);
2. the arbitrary-support owner-star synchronization inequalities
   (0.9)--(0.12), including the exact multi-owner energy;
3. \((1+o(1))D\) for every dual support of target-cover
   \(o(\sqrt m)\), and \(D+o(D/\sqrt m)\) for target-cover
   \(o(m^{1/4})\) at both audited strip scales;
4. the residual stars-plus-non-star-clusters estimate (3.8);
5. the sharpened pair-core bound \(D+\mu\);
6. the slow conflict-generator-rank reduction, conditional only on the
   explicitly stated imported fixed-rank edge-colouring theorem;
7. exact coefficient one for balanced conflict representations,
   conditional only on the explicitly stated imported balanced-matrix
   theorem;
8. the clique-sum identity, matching-gain peeling lemma, balanced
   transversal criterion, and the complete necessary certificate in
   Theorem B.

Not proved:

1. the owner-star synchronization inequality for Gaussian-or-larger
   target covers;
2. an \(o(D/\sqrt m)\) quantitative version of the slowly growing
   conflict-generator theorem;
3. the absence of the rank-diverging, matching-interlocked odd core in
   Theorem B; or
4. the full inequality
   \(\chi_f'(\mathcal H_m^\#)\le(1+o(1))D\) for arbitrary physical
   supports.

No classical odd-set or projective configuration remains as a standalone
or global obstruction. Such configurations may occur as proper pieces,
but then they obey the matching-gain interlock (7.8). The exact open object
is the higher-rank physical representative-packing/holonomy core described
above.
