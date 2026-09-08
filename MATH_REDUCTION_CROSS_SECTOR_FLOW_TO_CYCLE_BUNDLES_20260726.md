# From cross-sector occupancy flow to coherent \(C_{2h}\)-bundles: exact reduction and the first integral obstruction

Date: 2026-07-26

Method: pure mathematics.  No search or solver input is used.

## 0. Outcome

The cross-sector macroprofile flow

\[
 F_{k,\ell}
 ={V_k\over\binom mq}\prod_i\binom{k_i}{\ell_i}                   \tag{0.1}
\]

is a genuine bipartite network flow.  After replacing its target values by
floor/ceiling integers, it has an integral realization.  This is the last
place where ordinary total unimodularity applies.

The smallest exact coherent-rounding problem is the following decorated
cycle exact-cover system.  Let \(\mathscr C\) be the catalogue of allowed
directed isometric \(C_{2h}\)'s across all tensor packets, local-associator
corners, Hamming phases, and permitted direction orders.  For \(C\in
\mathscr C\), let

\[
 a_X(C)=\mathbf1_{\{X\in C\}},                                      \tag{0.2}
\]

and let

\[
 b_{q,k,\ell}(C)
 =\#\{X\in C:\kappa(X)=k,\ \kappa(L_q(C,X))=\ell\}.                  \tag{0.3}
\]

Here \(L_q(C,X)\) is the lower depth-\(q\) target at the start \(X\) of
the directed cycle.  If \(G_{q,k,\ell}\) is an integral rounding of the
desired profile flow, coherent long-cycle rounding is exactly

\[
\boxed{
\begin{aligned}
 \sum_{C\in\mathscr C}a_X(C)x_C&=1
                 &&(X\text{ a middle owner}),\\
 \sum_{C\in\mathscr C}b_{q,k,\ell}(C)x_C&=G_{q,k,\ell}
                 &&(1\le q\le H,\ k,\ell),\\
 x_C&\in\mathbb Z_{\ge0}.&
\end{aligned}}                                                     \tag{CB}
\]

The owner equations automatically make every \(x_C\) binary.  Conversely,
an integral solution is precisely a vertex-disjoint \(C_{2h}\)-factor
whose common cyclic prefixes realize all the prescribed profile flows.
Thus \((CB)\) is the smallest exact profile-level hypergraph formulation;
individual labelled-target coverage is a further refinement, not hidden in
the notation.

Three proposed automatic integrality arguments fail.

1. **Birkhoff--von Neumann stops before bundling.**  It integrally rounds
   owner-to-target assignments at one depth, and a layered network rounds
   nested flags through all depths.  It does not group \(2h\) starts into
   a common cyclic direction word.
2. **The cycle matrix is not a network matrix or totally unimodular.**
   For every \(h\ge3\), three translates of one standard isometric
   \(C_{2h}\) contain the minor
   \[
      \begin{pmatrix}
       1&1&0\\1&0&1\\0&1&1
      \end{pmatrix},
      \qquad\det=-2.                                                \tag{0.4}
   \]
   The three owner equations have the unique fractional solution
   \(x_0=x_1=x_2=1/2\) and no integral solution.
3. **Prefix laminarity is destroyed by cyclic closure.**  Prefixes from
   one fixed start form a chain, but different starts and different cycle
   translates give the crossing triangle (0.4).  There is no common
   laminar family containing the cycle columns.

There are also exact physical congruences:

\[
 \boxed{\sum_\ell G_{q,k,\ell}\equiv0\pmod{2h}}                    \tag{0.5}
\]

for every source profile \(k\), because one selected cycle remains in one
middle macroprofile and contains \(2h\) owners, and

\[
 \boxed{G_{q,k,\ell}\equiv0\pmod2\qquad(1\le q<h)}                  \tag{0.6}
\]

because every direction interval occurs at the two antipodal starts of
the word \(\sigma\sigma\), with the same macroprofile transition.
The network-rounded flow need not obey either congruence.

These are rigorous integral obstructions, but not yet coefficient-one
obstructions.  With eight-coordinate macroblocks, the number of source and
target macroprofiles is at most \(9^{m/4}=\exp(0.5494\ldots m)=o(W)\).
Leaving fewer than \(2h\) owners per source profile and one occurrence per
profile-flow cell costs \(o(W)\) whenever \(h=\exp(o(m))\), in particular
for the intended polynomial \(h\).  Thus the congruences can be quarantined
as a sublinear residual.

The exact remaining theorem is consequently a **semigroup saturation**
statement for the cycle columns after these local congruences are removed:

\[
 \boxed{\text{Does every interior integral point of the profile-flow
 cone, satisfying (0.5)--(0.6), lie in the nonnegative cycle semigroup
 up to }o(W)\text{ residual mass?}}                                  \tag{0.7}
\]

No Birkhoff, network-matrix, or laminar theorem proves (0.7).  The
determinant-\(2\) minor is the first rigorous obstruction, and coherent
cycle-semigroup saturation is the irreducible gate.

The sectorwise order-count bound from the tensor-associator audit remains
explicitly conditional: it applies only if each balanced tensor sector is
required to meet its own target quotas.  Cross-sector flow (0.1) evades
that bound; it does not evade the cycle-semigroup obstruction above.

## 1. The unbundled profile network

Partition \([2m]\) into eight-coordinate macroblocks.  For a middle owner
\(X\) and a lower target \(T\), write

\[
 \kappa(X)=k,\qquad \kappa(T)=\ell.                                  \tag{1.1}
\]

The exact profile counts are

\[
 V_k=\prod_i\binom8{k_i},\qquad
 T_\ell=\prod_i\binom8{\ell_i}.                                     \tag{1.2}
\]

Join \(k\) to \(\ell\) when \(\ell_i\le k_i\) for all \(i\) and
\(\sum_i(k_i-\ell_i)=q\).  Formula (0.1) has row sums \(V_k\) and column
sums

\[
                         {W\over N_q}T_\ell.                         \tag{1.3}
\]

Give each source node integral supply \(V_k\), and each target node lower
and upper capacities

\[
 c_qT_\ell,\qquad(c_q+1)T_\ell,\qquad
 c_q=\lfloor W/N_q\rfloor.                                          \tag{1.4}
\]

The flow (0.1) is feasible.  Since this is a bipartite transport network,
there is an integral feasible flow \(G_q\).  This remains true
simultaneously for nested deletion flags after introducing the usual
layered states

\[
 k^{(0)}\ge k^{(1)}\ge\cdots\ge k^{(H)},\qquad
 |k^{(q-1)}|-|k^{(q)}|=1.                                           \tag{1.5}
\]

The node--arc incidence matrix of this acyclic layered network is totally
unimodular.  Hence one can choose integral nested macroprofile chains.

This theorem says nothing about cyclic bundling.  In (1.5), two flags with
the same initial profile may use unrelated deletion orders.  In a
\(C_{2h}\), all \(2h\) starts are cyclic shifts of one word
\(\sigma\sigma\), and the forward and reverse flags are coupled.

## 2. The exact cycle-bundle hypergraph

Let \(\Omega\) be the set of middle owners surviving any allowed
\(o(W)\) quarantine.  An allowed directed cycle

\[
 C=(X_0,X_1,\ldots,X_{2h-1},X_0)                                   \tag{2.1}
\]

must satisfy:

1. \(X_tX_{t+1}\) is a legal pair-flip Johnson edge;
2. its direction word is \(\sigma\sigma\) for a permutation \(\sigma\)
   of its \(h\) active directions;
3. its local tensor-packet shore is legal; and
4. every required \(q\)-window is geodesic.

For each start \(X_t\), the one cycle simultaneously determines

\[
 L_1(C,X_t)\supset L_2(C,X_t)\supset\cdots\supset L_H(C,X_t)          \tag{2.2}
\]

and the complementary upper chain.  Therefore a cycle is one hyperedge in
the decorated resource set

\[
 \Omega\ \sqcup\
 \{(q,k,\ell,s):1\le q\le H,\ 1\le s\le G_{q,k,\ell}\}.              \tag{2.3}
\]

It consumes its \(2h\) owner vertices and supplies
\(b_{q,k,\ell}(C)\) indistinguishable slots of each profile color.  Writing
only the multiplicity equations yields exactly \((CB)\).  Splitting the
profile slots into labelled copies gives the ordinary hypergraph exact
cover with the same integer points.

### Theorem 2.1 (exactness of \((CB)\))

Integral solutions of \((CB)\) are in bijection with exact middle
\(C_{2h}\)-factors realizing the prescribed simultaneous profile flows.

#### Proof

If \(x\) is integral, an owner equation implies \(x_C\le1\) for every
cycle containing that owner.  The first line of \((CB)\) therefore selects
pairwise owner-disjoint cycles covering every owner exactly once.  The
second line is exactly the profile census of their common depth windows.

Conversely, such a cycle factor has a \(0\)-\(1\) incidence vector.  Exact
middle ownership gives the first equations and its profile census gives
the second. \(\square\)

The formulation is minimal in the following sense.  Deleting the
profile-color equations forgets the desired flow.  Replacing cycle
variables by individual owner-to-target arcs forgets common cyclic
bundling.  No auxiliary variable is needed to express either condition.

## 3. Why Birkhoff--von Neumann does not lift

At one depth, let \(z_{X,T}\) indicate that the occurrence starting at
\(X\) is assigned to \(T\).  The equations

\[
 \sum_Tz_{X,T}=1,\qquad
 c_q\le\sum_Xz_{X,T}\le c_q+1                                      \tag{3.1}
\]

form a capacitated bipartite matching polytope and are integral.  With
the containment arcs \(T\subset X\), this is exactly the Birkhoff/network
part of the problem.

Across depths, refine \(z\) to a unit flow through the subset lattice.
The resulting layered network remains integral and produces nested flags.

To recover a cycle one must additionally assert that the successor map on
owners is a permutation all of whose cycles have length \(2h\), and that
the direction word on each cycle is \(\sigma\sigma\).  Birkhoff's theorem
only produces an arbitrary permutation.  Fixed cycle length is a subtour
condition, and the isometric word is a further global condition.  These
constraints are not represented by node--arc incidence rows.

Equivalently, the projection

\[
 \{\text{cycle factors}\}\longrightarrow
 \{\text{nested integral flag flows}\}                              \tag{3.2}
\]

is not surjective.  The congruences in Section 6 already give explicit
flag flows outside its image.

## 4. A determinant-\(2\) minor inside the actual cube-cycle catalogue

Let \(h\ge3\), write \(e_1,e_2,\ldots,e_h\) for the cube basis, and set

\[
 p_0=0,\qquad p_j=e_1+\cdots+e_j.
                                                                        \tag{4.1}
\]

The standard isometric \(C_{2h}\) has vertex support

\[
 P=\{p_0,\ldots,p_{h-1},
       \mathbf1+p_0,\ldots,\mathbf1+p_{h-1}\}.                       \tag{4.2}
\]

Consider its three translates

\[
 C_0=P,\qquad C_1=P+e_1,\qquad C_2=P+e_2.                            \tag{4.3}
\]

For \(h\ge3\),

\[
 0,e_1,e_1+e_2\in P,\qquad e_2\notin P.                             \tag{4.4}
\]

Consequently the owners

\[
 u_{01}=0,\qquad u_{02}=e_1+e_2,\qquad u_{12}=e_2                    \tag{4.5}
\]

have cycle incidences

\[
\begin{array}{c|ccc}
 &C_0&C_1&C_2\\ \hline
u_{01}&1&1&0\\
u_{02}&1&0&1\\
u_{12}&0&1&1.
\end{array}                                                        \tag{4.6}
\]

Indeed:

* \(0\in P\cap(P+e_1)\) and \(0\notin P+e_2\);
* \(e_1+e_2\in P\cap(P+e_2)\) and
  \(e_1+e_2\notin P+e_1\); and
* \(e_2\notin P\), while
  \(e_2\in(P+e_1)\cap(P+e_2)\).

The determinant in (0.4) is \(-2\).  In the restricted three-owner exact
cover, the equations are

\[
 x_0+x_1=1,\qquad x_0+x_2=1,\qquad x_1+x_2=1,                       \tag{4.7}
\]

whose unique solution is \(x_0=x_1=x_2=1/2\).  No integral solution
exists.

### Corollary 4.1

The owner--\(C_{2h}\) incidence matrix, and hence the matrix of \((CB)\),
is not totally unimodular for any \(h\ge3\).

Adding profile rows cannot turn the displayed owner submatrix into a
network matrix.  Thus neither arbitrary cycle selection nor coherent
profile-flow rounding follows from total unimodularity.

The obstruction is minimal: every \(1\times1\) and \(2\times2\)
\(0\)-\(1\) matrix has determinant in \(\{0,\pm1\}\); the triangle is the
first possible determinant-\(2\) minor.

## 5. Why laminar decomposition also stops

For one fixed start \(X\), the lower targets in (2.2) are nested.  Those
rows form a laminar chain and can be handled by a network flow.  However,
the \(2h\) starts of one cycle are cyclic shifts.  Their direction
intervals cross:

\[
 \{\sigma_1,\sigma_2\},\quad
 \{\sigma_2,\sigma_3\},\quad\ldots                                  \tag{5.1}
\]

are not laminar.  Allowing multiple direction orders contains, on three
directions, the three two-sets

\[
                         \{1,2\},\quad\{1,3\},\quad\{2,3\},          \tag{5.2}
\]

whose incidence matrix is again (0.4).  Thus there is no global laminar
uncrossing that preserves the cycle columns.

One may cut every cycle at one start and obtain a laminar path problem.
Re-gluing the endpoints reintroduces exactly the odd-cycle/subtour
constraint.  Hence a path decomposition is a valid fractional or
leave-producing relaxation, but not an exact coherent-rounding theorem.

## 6. Exact congruence obstructions

An isometric \(C_{2h}\) has direction word \(\sigma\sigma\).  It stays in
one middle macroprofile \(k\), since every transition is internal to one
fixed macroblock.  Therefore a selected cycle consumes exactly \(2h\)
owners from that profile.  This proves (0.5).

Fix \(1\le q<h\).  A direction \(q\)-set \(D\) is a cyclic interval of
\(\sigma\) at exactly two antipodal starts, or at no start.  The two starts
have the same source macroprofile and delete directions in the same
macroblocks, so they have the same target macroprofile.  Every cycle's
contribution \(b_{q,k,\ell}(C)\) is therefore even.  This proves (0.6).

There are finer coordinate-star congruences.  Along one active cube
direction, each endpoint of the corresponding physical coordinate pair
occurs at exactly \(h\) of the \(2h\) middle owners.  A frozen full pair
contributes \(2h\) occurrences of each endpoint and a frozen empty pair
contributes zero.  Hence owner-star totals of any cycle bundle lie in the
lattice generated by \(h\) and \(2h\).  These are the familiar
cycle-resolution divisibilities.

### Proposition 6.1 (the congruence leave is sublinear)

Assume \(h=\exp(o(m))\).  There is a residual set of \(o(W)\) owner and
profile tokens after whose deletion all source-profile totals are
divisible by \(2h\) and all profile-flow cells are even.

#### Proof

There are at most

\[
                         9^{m/4}                                    \tag{6.1}
\]

eight-block occupancy vectors.  First quarantine fewer than \(2h\)
owners from every source profile, making every surviving source total
divisible by \(2h\).  This costs at most \(2h\) times the number of source
profiles.  Restrict an integral profile flow to the surviving supply,
allowing the same amount of target-profile error.

At a fixed depth and source-profile row, the number of odd flow cells is
even because the row sum is even.  Pair the odd cells.  For each pair,
subtract one unit from one (positive) odd cell and add it to the other.
Both become even, the source row sum is unchanged, and the target-column
\(L^1\) error is at most two.  Thus all cell parities can be repaired at
total profile error at most the number of reachable cells.  For
polynomially many depths,
the number of such cells is at most a polynomial factor times
\(9^{m/2}\) under the crude independent source/target count.  This last
crude bound is not \(o(W)\), so one should use the support relation:
\(\ell_i\le k_i\) and \(\sum(k_i-\ell_i)=q=O(\sqrt m)\).
For each \(k\), the number of reachable \(\ell\)'s is at most

\[
 \sum_{j\le q}\binom{m/4}{j}8^j
   =\exp(O(q\log m))=\exp(o(m)).                                     \tag{6.2}
\]

Thus the total number of reachable cells through polynomially many
Gaussian depths is

\[
 9^{m/4}\exp(o(m))
   =\exp\!\left({\log9\over4}m+o(m)\right)
   =\exp(0.5494\ldots m+o(m))=o(W),                                  \tag{6.3}
\]

because \(\log W=(\log4+o(1))m=1.3862\ldots m+o(m)\).
Multiplication by \(2h=\exp(o(m))\) preserves \(o(W)\). \(\square\)

Proposition 6.1 says only that the visible lattice congruences are
asymptotically cheap.  It does not assert that satisfying them is
sufficient for cycle decomposition.  The triangle is an actual hole in
the restricted three-owner system and proves non-unimodularity; by itself
it does not prove that the particular full exact-cover right-hand side is
a hole of the full cycle semigroup.

## 7. The exact remaining saturation theorem

Let \(A\) be the owner/profile incidence matrix in \((CB)\), and write

\[
 \mathsf S(A)=\{Ax:x\in\mathbb Z_{\ge0}^{\mathscr C}\},\qquad
 \mathsf C(A)=\{Ax:x\in\mathbb R_{\ge0}^{\mathscr C}\}.              \tag{7.1}
\]

The profile flow and group averaging give points in the rational cone
\(\mathsf C(A)\).  Coherent rounding asks for membership in the affine
slice of the semigroup \(\mathsf S(A)\).

The determinant-\(2\) minor shows that \(A\) is not unimodular, so
\[
 \mathsf C(A)\cap\mathbb Z^{\rm rows}=\mathsf S(A)                   \tag{7.2}
\]
does not follow from matrix theory.  Proposition 6.1 removes the obvious
local lattice defects at \(o(W)\) cost.  The live statement is:

> **Cycle-semigroup saturation gate.**  After deleting \(o(W)\) owner
> tokens, every balanced cross-sector profile flow lying a fixed relative
> distance inside \(\mathsf C(A)\) and satisfying all cycle lattice
> congruences is realizable by pairwise owner-disjoint allowed
> \(C_{2h}\)'s, with aggregate profile error \(o(W)\).

This is stronger than an ordinary matching theorem because the edge size
\(2h\) grows and every edge carries all depths simultaneously.  It is
weaker than exact normality of \(\mathsf S(A)\), because a sublinear leave
and sublinear profile error are allowed.

No theorem in this note proves the gate.  What is proved is the exact
reduction, the failure of the three automatic integrality mechanisms, and
the fact that the first congruence obstructions are cheap enough that a
genuine saturation/absorber theorem could still yield coefficient one.
