# Capacitated flag Hall, orbit barycentres, and the exact depth-one common-refinement gate

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input is
used.

## 0. Verdict

Let

\[
 \mathcal L=\binom{[n]}{m-1},\qquad
 \mathcal M=\binom{[n]}m,\qquad
 \mathcal U=\binom{[n]}{m+1},
 \qquad n\in\{2m,2m+1\}.
\]

Every Johnson edge is the middle lift of a unique flag

\[
             R\subset U,\qquad |R|=m-1,\quad |U|=m+1.       \tag{0.1}
\]

There are three successively stronger problems, and they must not be
identified.

1. Prescribed lower and upper colour loads alone form an ordinary bipartite
   `b`-factor problem on the flag graph.  The exact capacitated Hall cuts are
   proved below.  They imply, integrally, both an exact two-sided rainbow
   colour core and a full floor/ceiling colour allocation.
2. Adding middle-owner degree at most two turns the same columns into a
   four-resource hypergraph packing.  Its exact *fractional* weighted Hall
   dual is elementary, and the symmetric optimum has zero loss.  Ordinary
   Hall integrality is lost.  The Catalan parity obstruction is an actual
   obstruction to restoring it in the strongest exact core.
3. Requiring middle degree two and few components is still stronger.  The
   uniform fractional point is an orbit barycentre of connected GMM cycles
   (and, in the spanning normalization, of Hamilton cycles), so neither the
   fractional Hall inequalities nor the standalone cycle subtour
   inequalities nor the displayed marginal capacities separate it.
   Mixed rank inequalities valid only for integral common objects are not
   excluded.  Selecting one integral common object with a quantitative
   component bound is the remaining rounding problem.

On the odd ground there is one useful asymmetric exception.  If lower
colours need only be hole-free, rather than floor/ceiling bounded, then a
fixed exact lower core can be completed by an ordinary incidence flow.  Its
exact Hall cuts are (6.3) below, and a forest core automatically gives at
most

\[
                   {2W\over m+2}=o(W/H)                    \tag{0.2}
\]

cycles for every `H=o(m)`.  Imposing the lower ceiling two reintroduces the
four-resource hypergraph gate.

Thus the component count is automatic after a forest core has been
completed: by the ordinary flow in the coverage normalization, or by an
integral solution of the stronger residual system in the balanced
normalization.  What is not automatic for floor/ceiling balance is the
integral completion itself.  None of the results below proves constant one.

## 1. The flag graph and its exact degrees

Let `Gamma=Gamma_(n,m)` be the bipartite graph on
`mathcal L dotcup mathcal U`, with `R U` an edge when `R subset U`.  If

\[
                         U\setminus R=\{a,b\},
\]

its middle lift is

\[
 \lambda(R,U)=\{R\cup\{a\},R\cup\{b\}\}\in E(J(n,m)).       \tag{1.1}
\]

This is a bijection from `E(Gamma)` to the Johnson edges.  Put

\[
 W=|\mathcal M|,\quad N_-=|\mathcal L|,\quad N_+=|\mathcal U|,
\]

\[
 d_-={n-m+1\choose2},\qquad d_+={m+1\choose2},\qquad
 D_J=m(n-m).                                                \tag{1.2}
\]

Thus every lower vertex has degree `d_-`, every upper vertex has degree
`d_+`, every middle owner has Johnson degree `D_J`, and

\[
 N_-d_-=N_+d_+={WD_J\over2}.                                \tag{1.3}
\]

For a flag family `F`, write `d_F^-(R),d_F^+(U)` for its two colour
degrees and

\[
 d_F^0(X)=|\{(R,U)\in F:X\in\lambda(R,U)\}|                 \tag{1.4}
\]

for the degree of `X` in the middle lift.

## 2. Exact capacitated Hall for the two colour shores

The following is the complete integral statement when middle degrees are
not prescribed.

### Theorem 2.1 (flag `b`-factor Hall theorem)

Let `a_R,b_U` be nonnegative integers satisfying

\[
                    \sum_Ra_R=\sum_Ub_U=:B.                 \tag{2.1}
\]

There is a simple flag family `F subset E(Gamma)` with

\[
                  d_F^-(R)=a_R,\qquad d_F^+(U)=b_U           \tag{2.2}
\]

if and only if, for every `A subset mathcal L` and
`B' subset mathcal U`,

\[
 \boxed{
 a(A)\le b(B')+e_\Gamma(A,\mathcal U\setminus B').}         \tag{2.3}
\]

#### Proof

Use the network with an arc of capacity `a_R` from the source to `R`, an
arc of capacity one from `R` to `U` for every flag, and an arc of capacity
`b_U` from `U` to the sink.  A cut whose source side is
`{s} union A union B'` has capacity

\[
 a(\mathcal L\setminus A)+e_\Gamma(A,\mathcal U\setminus B')+b(B').
\]

It has capacity at least `B=a(mathcal L)` exactly when (2.3) holds.
Max-flow/min-cut and integral capacities prove the theorem. `square`

For upper capacities rather than equalities, one deletes the equality of
the total upper mass and uses the same network.  In the unit-demand case
(2.3) reduces to the usual Hall theorem.

## 3. Integral colour allocations with the exact central quotas

### Theorem 3.1 (the exact rainbow core exists on the colour shores)

There is a matching in `Gamma` saturating `mathcal L`.  Consequently there
is a flag family of size `N_-` whose lower colours are all used exactly once
and whose upper colours are pairwise distinct.  For `n=2m` this is a
perfect matching of `Gamma`.

#### Proof

For `A subset mathcal L`, biregularity gives

\[
 d_-|A|\le d_+|N_\Gamma(A)|.
\]

In both central cases `d_- >= d_+`, so
`|N_Gamma(A)|>=|A|`.  Hall's theorem applies.  On the even ground the two
shores have the same size. `square`

The lift supplied by Theorem 3.1 need not have middle degree at most two.
In particular this theorem is not a two-factor theorem.

### Theorem 3.2 (full floor/ceiling colour allocation)

Assume `m>=2`.

1. If `n=2m`, there is a simple flag family of size `W` for which every
   lower and upper colour has load one or two.  Exactly

   \[
                         K={W\over m+1}=W-N_-               \tag{3.1}
   \]

   colours on each shore have load two.
2. If `n=2m+1`, there is a simple flag family of size `W` for which every
   upper colour has load one and every lower colour has load one or two.
   Exactly

   \[
                         d={2W\over m+2}=W-N_-               \tag{3.2}
   \]

   lower colours have load two.

#### Proof

On the even ground `Gamma` is regular.  Decompose it into edge-disjoint
perfect matchings.  Take one whole perfect matching and any `K` edges of a
second one.  Their endpoints are distinct within the second matching, so
the asserted degrees follow.

On the odd ground let every `U in mathcal U` choose one adjacent lower
vertex, with capacity two at each lower vertex.  The capacitated Hall
condition holds, because for `S subset mathcal U`,

\[
 d_+|S|\le d_-|N_\Gamma(S)|,
 \qquad {d_-\over d_+}={m+2\over m}\le2.                    \tag{3.3}
\]

Thus an integral assignment of all upper vertices with lower loads at most
two exists.

It remains to remove empty lower vertices.  Direct an auxiliary arc
`R to R'` if some upper vertex adjacent to `R` is currently assigned to
`R'`.  Start from an empty lower vertex `R_0`, and let `S` be its reachable
set.  If `S` contained no vertex of load two, then every upper neighbour of
`S` would be assigned inside `S`, and hence

\[
 |N_\Gamma(S)|=\sum_{R\in S}d_F^-(R)\le |S|-1.              \tag{3.4}
\]

But biregularity gives

\[
 |N_\Gamma(S)|\ge {d_-\over d_+}|S|>|S|,                   \tag{3.5}
\]

a contradiction.  Therefore there is an alternating path from `R_0` to a
lower vertex of load two.  Reassign each upper vertex along that path one
step backwards.  The initial load becomes one, the final load becomes one,
and all intermediate loads are unchanged.  Repetition removes every empty
lower vertex.  Since the total load is `W=N_-+d`, exactly `d` lower
vertices then have load two. `square`

Again, Theorem 3.2 controls only the two colour ledgers.  Its lift can have
arbitrary middle degrees up to the local flag-matching bound, and may have
no two-factor interpretation.

## 4. The augmented owner-capacitated Hall dual

For clarity, the exact integral common-refinement systems are as follows.
The near-spanning rainbow-core system has Boolean variables `x_e,z_X` and

\[
 \begin{aligned}
  &\sum_{e:\ell(e)=R}x_e\le1,\qquad
    \sum_{e:u(e)=U}x_e\le1,\\
  &\sum_{e\ni X}x_e=2z_X,\qquad
    x_e,z_X\in\{0,1\}.                                    \tag{4.0a}
 \end{aligned}
\]

Its support is `sum_X z_X=sum_e x_e`.  The ideal exact core has this value
`N_-`; allowing `o(W/H)` additional loss asks for
`sum_X z_X=N_--o(W/H)`.

The spanning floor/ceiling system has `x_e in {0,1}` and

\[
 \sum_{e\ni X}x_e=2,qquad
 1\le\sum_{e:\ell(e)=R}x_e\le2,\qquad
 1\le\sum_{e:u(e)=U}x_e\le2.                               \tag{4.0b}
\]

On the odd ground the upper equations in (4.0b) are automatically equal
to one, because `|mathcal U|=W=sum_e x_e`; on the even ground exactly
`W-N_-` colours on each shore have load two.  Equations (4.0a)--(4.0b)
impose no component bound: their middle lifts may be unions of many cycles.

For nonnegative capacities `a_R,b_U,c_X`, consider the fractional common
packing

\[
 \begin{aligned}
  \max\quad&\sum_{e\in E(J)}x_e,\\
  \text{subject to}\quad&
   \sum_{e:\ell(e)=R}x_e\le a_R &&(R\in\mathcal L),\\
  &\sum_{e:u(e)=U}x_e\le b_U &&(U\in\mathcal U),\\
  &\sum_{e\ni X}x_e\le c_X &&(X\in\mathcal M),\\
  &x_e\ge0.                                                \tag{4.1}
 \end{aligned}
\]

### Theorem 4.1 (weighted four-shore Hall dual)

The value of (4.1) equals

\[
 \boxed{
 \min\left\{
  \sum_Ra_R\alpha_R+\sum_Ub_U\beta_U+\sum_Xc_X\gamma_X:
  \alpha_{\ell(e)}+\beta_{u(e)}+\gamma_X+\gamma_Y\ge1
  \text{ for }e=XY
 \right\},}                                               \tag{4.2}
\]

where all dual variables are nonnegative.

#### Proof

This is finite-dimensional linear-programming duality applied to (4.1).
Each Johnson edge uses exactly its lower colour, its upper colour, and its
two middle endpoints, which gives the four terms in (4.2). `square`

Theorem 4.1 is an exact fractional Hall theorem, not an integral matching
theorem.  The constraint matrix has four ones in each column and is not a
network matrix.  The exact Catalan parity obstruction on `n=2m`,
`m=2^a-1`, supplies an actual Boolean-lattice witness to the integrality
failure: the fractional exact core below exists, while an integral
two-sided rainbow cycle factor does not.

### Theorem 4.2 (zero fractional loss, core and spanning forms)

Let `e` range over all Johnson edges.

1. Put

   \[
                         \bar x_e={1\over d_-}.              \tag{4.3}
   \]

   Then every lower load is one, every upper load is

   \[
                         {d_+\over d_-}={N_-\over N_+}\le1, \tag{4.4}
   \]

   and every middle degree is

   \[
                         {D_J\over d_-}={2N_-\over W}.       \tag{4.5}
   \]

   Thus, on putting `z_X=N_-/W`, one has the exact fractional owner
   equations

   \[
                         \sum_{e\ni X}\bar x_e=2z_X,
   \qquad \sum_Xz_X=N_-.                                   \tag{4.6}
   \]

   The fractional owner-capacitated core optimum is exactly `N_-`.
2. Put

   \[
                         \widetilde x_e={2\over D_J}.        \tag{4.7}
   \]

   Then every middle degree is two and the two colour loads are

   \[
                         {W\over N_-},\qquad {W\over N_+}.  \tag{4.8}
   \]

   In particular, on `n=2m` both loads are `(m+1)/m`; on
   `n=2m+1` the lower load is `(m+2)/m` and the upper load is one.
   Hence (4.7) obeys the exact fractional floor/ceiling interval
   `1<=load<=2` and has total mass `W`.

#### Proof

Equations (4.3)--(4.8) follow from the degree census (1.2)--(1.3).  The
core mass is `|E(J)|/d_-=N_-`; no packing with lower capacity one can have
larger mass.  The spanning mass is `2|E(J)|/D_J=W`; no packing with middle
capacity two can have larger mass. `square`

## 5. GMM and Middle Levels meet exactly at the fractional point

The preceding symmetric points are not merely feasible LP solutions.
They are orbit barycentres of connected one-sided solutions.

### Theorem 5.1 (cycle-orbit common barycentre)

1. Let `P` be any GMM two-level saturating cycle projected to
   `J(n,m)`.  It has `N_-` Johnson edges and is lower-rainbow.  Averaging
   its edge indicator over all coordinate permutations gives exactly
   `bar x` in (4.3).
2. Let `C` be any Hamilton cycle of `J(n,m)`, for example the contraction
   supplied by a GMM tight enumeration.  Averaging its edge indicator over
   all coordinate permutations gives exactly `widetilde x` in (4.7).
3. On `n=2m+1`, contraction of a Middle-Levels Hamilton cycle gives a
   Hamilton cycle of `J(n,m)` whose upper colours are used exactly once.
   Its coordinate-orbit average is again `widetilde x`.

Consequently, in the odd-ground spanning normalization, the convex hull of
the lower-complete Hamilton cycles obtained from GMM tight enumerations and
the convex hull of the upper-complete Hamilton cycles obtained from Middle
Levels meet at `widetilde x`.  Separately, the orbit hull of the connected
GMM core cycles contains `bar x`.  Thus the standalone cycle-polytope
inequalities and the explicit fractional capacity inequalities are all
satisfied at the corresponding symmetric point.  This does not rule out a
mixed rank inequality for the convex hull of integral common refinements.

#### Proof

The symmetric group is transitive on Johnson edges.  Therefore the orbit
average of any `t`-edge object assigns the common value
`t/|E(J)|` to every Johnson edge.  For `t=N_-`, (1.3) gives
`N_-/|E(J)|=1/d_-`; for `t=W`, it gives `W/|E(J)|=2/D_J`.

For the last assertion, a Middle-Levels Hamilton cycle alternates all
rank-`m` sets with all rank-`m+1` sets.  Suppressing the latter makes its
two adjacent rank-`m` facets into a Johnson edge of union equal to the
suppressed set.  Every upper set occurs once. `square`

This theorem explains the exact limitation of convex Hall arguments.  A
linear separation cannot choose one integral cycle from two orbit
barycentres.  The missing assertion is a discrepancy/rounding theorem for
one common member, not another marginal count.

## 6. The strongest ordinary-flow completion: hole-free, not quota-safe

This section specializes to the odd ground `n=2m+1`.  Put

\[
 N=N_-={m\over m+2}W,\qquad d=W-N={2W\over m+2}.             \tag{6.1}
\]

Let `F` be a flag family of size `N` such that every lower colour occurs
once, its upper colours are distinct, and `d_F^0(X)<=2`.  Define

\[
 \delta_F(X)=2-d_F^0(X),\qquad
 \mathcal U_0=\mathcal U\setminus u(F).                     \tag{6.2}
\]

Then `sum_X delta_F(X)=2d` and `|mathcal U_0|=d`.

### Theorem 6.1 (exact residual owner--upper Hall theorem)

The lift of `F` extends to a spanning two-factor using every upper colour
exactly once if and only if, for every `A subset mathcal M`,

\[
 \boxed{
 \sum_{X\in A}\delta_F(X)
 \le \sum_{U\in\mathcal U_0}\min\{2,|\{X\in A:X\subset U\}|\}.} \tag{6.3}
\]

Every completion adds exactly `d` Johnson edges.  All lower colours remain
hole-free.  If the middle lift of `F` is a forest, every such completion
has at most `d=o(W/H)` components for `H=o(m)`.

#### Proof

Use the bipartite incidence network from `mathcal U_0` to `mathcal M`.
Each `U` supplies two units, each incidence `U-X` has capacity one, and
`X` demands `delta_F(X)` units.  The total masses agree.  The
max-flow/min-cut criterion for satisfying all middle demands is exactly
(6.3).  An integral flow chooses two distinct middle facets `X_U,Y_U` of
each `U`; they form the Johnson edge of union `U`.  Conversely, every
completion supplies this flow.

Every cycle component of the completed two-factor either was already a
cycle component of the core or contains an added edge.  If the core is a
forest, distinct completed components therefore consume distinct added
edges, so there are at most `d` components.  Finally
`d/(W/H)=2H/(m+2)->0`. `square`

### Proposition 6.2 (why the floor ceiling destroys the flow)

Prescribe lower residual capacities

\[
 \kappa_R=b_R-d_F^-(R),\qquad b_R\in\{1,2\}.                \tag{6.4}
\]

For each unused `U`, the completion must choose a *pair* of facets
`X,Y subset U`; this pair simultaneously determines the lower colour
`R=X cap Y`.  The exact integer variables are therefore indexed by flags
`(R,U)`, and obey

\[
 \begin{aligned}
  &\sum_{R\subset U}y_{R,U}=1 &&(U\in\mathcal U_0),\\
  &\sum_{(R,U):X\in\lambda(R,U)}y_{R,U}=\delta_F(X)
       &&(X\in\mathcal M),\\
  &\sum_{U\supset R}y_{R,U}\le\kappa_R &&(R\in\mathcal L),\\
  &y_{R,U}\in\{0,1\}.                                     \tag{6.5}
 \end{aligned}
\]

Unlike (6.3), (6.5) cannot be obtained by independently sending the two
units out of `U`: their pairing determines `R`.  It is a hypergraph
matching/degree problem.  Thus Theorem 6.1 proves exact hole-free
completion but not exact floor/ceiling completion.

If (6.5) does have an integral solution, the component proof of Theorem
6.1 applies without change: a forest core is completed using exactly `d`
new edges and therefore yields at most `d=o(W/H)` cycle components for
`H=o(m)`.

Its fractional obstruction can nevertheless be written exactly.  Assume
the prescribed residual lower mass is `sum_R kappa_R=d`.  The fractional
relaxation of (6.5) is feasible if and only if every nonnegative family
`alpha_U,beta_R,gamma_X` satisfying

\[
 \alpha_U+\beta_R+\gamma_X+\gamma_Y\ge1
 \quad\text{whenever }U\in\mathcal U_0, R\subset U,
 \ \lambda(R,U)=XY                                      \tag{6.6}
\]

obeys

\[
 \boxed{
 \sum_{U\in\mathcal U_0}\alpha_U+
 \sum_R\kappa_R\beta_R+
 \sum_X\delta_F(X)\gamma_X\ge d.}                       \tag{6.7}
\]

Indeed, maximize `sum_(R,U)y_(R,U)` subject to the three capacity families
in (6.5).  Its packing dual is (6.6)--(6.7).  A packing of value `d`
saturates all `d` upper slots, all `d` lower slots, and all `2d` owner
deficit slots, so it satisfies the equalities in (6.5).  This proves the
fractional equivalence by LP duality.  It does not supply an integral
packing.

## 7. Endpoint completion and the exact component-rate gate

Let `F` be a linear forest on all `W` middle owners, with `t` internal
edges and `p=W-t` path components, isolated owners included.  Prescribe
full colour quotas `b_R^-,b_U^+` of total `W`, and suppose the internal
loads do not exceed them.  The residual colour capacities have total `p`
on each shore.

Orient the paths and call their terminal and initial ports `T_i,H_i`.
A candidate seam `T_i H_j` is a Johnson edge not already in `F` and
consumes its lower and upper residual colour slots.  (In particular, a
one-edge path may not be closed by selecting its own retained edge a second
time.)  Give every underlying physical Johnson edge one additional
unit-capacity resource; this prevents the two orientations of the same
edge from both being selected (which matters especially for two isolated
owners).  The resulting five-resource seam hypergraph has vertex classes

\[
 \{T_i\},\quad\{H_j\},\quad\mathcal L,\quad\mathcal U,
 \quad E(J(n,m)).                                      \tag{7.1}
\]

### Theorem 7.1 (exact fractional seam Hall dual)

There is a fractional seam packing of size `p` if and only if every
nonnegative family `alpha_i,beta_j,lambda_R,mu_U,eta_g` satisfying

\[
 \alpha_i+\beta_j+\lambda_{\ell(g)}+\mu_{u(g)}+\eta_g\ge1
                                                               \tag{7.2}
\]

for every oriented candidate seam from `T_i` to `H_j` whose underlying
physical edge is `g`, obeys

\[
 \boxed{
 \sum_i\alpha_i+\sum_j\beta_j
 +\sum_R\kappa_R^-\lambda_R+\sum_U\kappa_U^+\mu_U
 +\sum_{g\in E(J)}\eta_g\ge p.}                         \tag{7.3}
\]

Here `kappa^-`, `kappa^+` are the residual capacities.  An integral
packing of size `p` closes the paths to a spanning two-factor with at most
`p` components and exactly the prescribed colour quotas.

#### Proof

The fractional seam-packing LP has capacity one at every terminal and
initial port, capacities `kappa^-`, `kappa^+` at the colour vertices,
and capacity one at each physical-edge resource.
Its vertex-cover dual is (7.2)--(7.3).  Since `p` is the total capacity of
each port shore and of each colour-slot shore, a size-`p` integral packing
saturates every port and every residual colour slot.  Contracting each old
path, the selected seams form a directed permutation of the path
components.  Physical-edge capacity makes its expansion simple, giving a
simple two-factor with at most `p` cycles.
`square`

Theorem 7.1 is deliberately fractional.  Five-resource hypergraph matching
does not inherit bipartite matching integrality.  The exact integral gate is
that this seam hypergraph have matching number `p`; ordinary Hall cuts or
their fractional weighted form do not prove it.

There is a second, quantitative formulation relevant to the known
two-sided pseudoforest.  Suppose a common flag packing has `t` edges,
middle degree at most two, and projected girth at least `L`.  Deleting one
edge from every projected cycle gives a spanning linear forest with

\[
 c(F)\le (W-N_-)+(N_--t)+{W\over L}.                         \tag{7.4}
\]

Therefore, for `H=o(m)`, the two estimates

\[
              N_--t=o(W/H),\qquad {L\over H}\longrightarrow\infty \tag{7.5}
\]

would give `c(F)=o(W/H)`.  The audited fixed-girth conflict-free matching
theorem proves only `N_--t=o(W)` after a diagonal in fixed `L`; it supplies
neither quantitative estimate in (7.5).

## 8. Exact proved/conditional boundary

The following statements are unconditional.

1. Every prescribed two-shore flag `b`-factor is governed exactly by the
   cut inequalities (2.3).
2. Both the rainbow core colour allocation and the full floor/ceiling
   colour allocation exist integrally.
3. The core and spanning common-refinement LPs have zero fractional loss;
   their symmetric solutions are orbit barycentres of connected GMM and
   Middle-Levels objects.
4. A fixed odd-ground exact lower forest core satisfying (6.3) completes
   to a spanning upper-bijective, lower-hole-free two-factor with
   `o(W/H)` components whenever `H=o(m)`.
5. The known common two-sided pseudoforest gives only unparameterized
   `o(W)` owner/colour loss and components.

The smallest remaining floor/ceiling statement over a fixed forest core is
an integral solution of (6.5); its component bound is then automatic.  A
full common flag family with the prescribed colour quotas and middle degree
two is equivalent to such a core/completion decomposition, but without a
forest or small-cycle condition it need not have few components.  For the
pseudoforest route one additionally
needs the quantitative estimates (7.5) and an integral seam matching of
size `p`.  The component quotient need not be connected: once
`p=o(W/H)`, any cycle cover of the paths already has the required number of
components.

## 9. Adversarial audit

* Theorems 2.1, 3.1, and 3.2 say nothing about middle degrees.  Calling
  their lifts factors would be false.
* Theorem 4.1 is fractional.  The orbit barycentre in Theorem 5.1 does not
  imply that one orbit member has the two-sided quotas.
* The GMM saturating cycle and tight enumeration are distinct existential
  objects.  Only their separately audited projection properties are used.
* Theorem 6.1 permits arbitrarily repeated lower colours after the core.
  It proves hole-freeness, not the ceiling two in (6.5).
* Theorem 7.1 gives fractional seam Hall.  An integral seam matching and a
  connected quotient are stronger; only the former is needed for an
  `o(W/H)` component count once `p=o(W/H)`.
* In (7.4), the intrinsic owner excess `W-N_-=O(W/m)` is negligible only
  because `H=o(m)`.  The fixed-girth diagonal does not provide the two
  rates in (7.5).

Accordingly ordinary Hall, GMM connectivity, and Middle-Levels connectivity
are each individually exact, but their required integral common refinement
remains open.
