# Thread D: complement-dual odd-graph lattice, voltage, and the one-splice gate

Date: 2026-08-01  
Status: exact algebraic theorem.  The occurrence duality, square topology,
cycle-lattice ranks, and voltage images are proved.  Alternating matching
circuits are complete for the unrestricted complement-dual matching fibre,
but rank-ten coverage is a nonlinear turn constraint and a palette-safe
one-splice certificate is not proved here.

## 0. Outcome

Let `O` be the 1,430 rank-nine `Z_17` owner orbits, let `L` be the 1,430
rank-eight facet orbits, and let `C:O<->L` be complementation.  Choose an
incidence perfect matching `D:O->L` and put

\[
                  H=CD^{-1}C,\qquad A=CD:O\longrightarrow O.       \tag{0.1}
\]

Then the following statements are exact.

1. `A` is a directed one-factor of the 9-regular quotient odd graph: in a
   physical alignment, `|a intersect A(a)|=1`.  Conversely every such
   directed one-factor determines `D`.
2. If `p(a)` and `n(a)` are the labels of the incoming and outgoing
   `A`-arcs at `a`, then

   \[
   U(Ca)=Ca\cup\{p(a),n(a)\},\qquad
   L(a)=a\setminus\{p(a),n(a)\}.                    \tag{0.2}
   \]

   Hence `C(L(a))=U(Ca)` occurrence by occurrence, with identical
   multiplicities after complementing target labels.
3. The owner successor of `D union H` is `A^2`.  A Hamilton `A` therefore
   gives exactly two 715-owner quotient factor cycles, never one.
4. The ordinary directed odd-graph cycle lattice has rank 5,006 and full
   voltage image `Z_17`.  The complement-even support-change lattice has
   rank 5,005 and voltage zero.  The oriented `D`-versus-`H` change lattice
   has rank 5,006, one universal `Z/2` defect, and still has full voltage
   image because its voltage is twice the unrestricted incidence-cycle
   voltage.
5. Alternating circuits of `D` generate every endpoint perfect matching in
   this restricted family.  They do **not** linearly generate the rank-ten
   coverage vector: (0.2) couples an incoming and an outgoing arc.  Safe
   serial reachability is governed by the exact provider inequalities in
   Section 6.
6. If a Hamilton `A` is turn-surjective, its 1,430 turns on 1,144 colours
   have exactly 286 **repeat units**.  This is not necessarily 286 distinct
   repeated colours and does not by itself furnish the required cross
   rectangle.  One non-dual rectangle can join the two parity cycles iff it
   passes the local incidence, voltage, and four-ticket palette test of
   Section 7.

Thus the complement-dual face retains all mod-17 voltage freedom, but it
cannot be the final connected factor without one symmetry-breaking splice.

## 1. Direct odd-graph normal form

For `a in O`, `D(a)` is a rank-eight facet contained in `a`.  Therefore

\[
       A(a)=C(D(a))=C(a)\cup\{n(a)\}                 \tag{1.1}
\]

for a unique physical label `n(a) in a`.  Equivalently

\[
                         |a\cap A(a)|=1.             \tag{1.2}
\]

Perfectness of `D` on the facet shore is exactly injectivity, hence
bijectivity, of `A`.  Conversely (1.1) recovers the incidence matching as
`D=CA`.  Thus `D`-matchings are precisely directed cycle covers in the
voltage-labelled quotient of `KG(17,8)`, written on complementary rank-nine
vertices.

Write

\[
 A^{-1}(a)=C(a)\cup\{p(a)\},\qquad
 A(a)=C(a)\cup\{n(a)\}.                              \tag{1.3}
\]

At the facet `C(a)`, the two selected owners are `A^{-1}(a)` and `A(a)`.
At owner `a`, the selected facets are their complements.  Hence

\[
\begin{aligned}
 U(Ca)&=A^{-1}(a)\cup A(a)=C(a)\cup\{p(a),n(a)\},\\
 L(a)&=C(A^{-1}(a))\cap C(A(a))=a\setminus\{p(a),n(a)\}.
                                                               \tag{1.4}
\end{aligned}
\]

The two labels are distinct exactly when the two factor incidences at the
corresponding occurrence are distinct.  In particular they are distinct on
a Hamilton `A`.

### Corollary 1.1 (literal occurrence duality)

For every owner occurrence,

\[
                         C(L(a))=U(C(a)).             \tag{1.5}
\]

Consequently the rank-seven and rank-ten load vectors satisfy

\[
             \mu_7(Q)=\mu_{10}(C(Q))                 \tag{1.6}
\]

for every physical target and for every quotient target orbit.  Thus one
of the two immediate-palette ALO families is redundant.  This says nothing
about ranks eleven and above.

## 2. The square-permutation topology

Since `H=CA^{-1}`, its inverse is `H^{-1}=AC`.  Following a `D` incidence
and then the inverse `H` incidence gives

\[
                      H^{-1}D=A^2.                   \tag{2.1}
\]

If an `A`-cycle has length `ell`, its contribution to the factor is

\[
                   \gcd(\ell,2)                       \tag{2.2}
\]

cycles.  In particular

\[
 c(A^2)=\#\{\text{odd }A\text{-cycles}\}
       +2\#\{\text{even }A\text{-cycles}\}.         \tag{2.3}
\]

Because `|O|=1430` is even, the number of odd `A`-cycles is even, so
`c(A^2)` is a positive even integer.  A connected quotient factor is
therefore impossible inside the exact dual face.  The minimum is two,
attained by one 1,430-cycle `A`; the two components are its even and odd
positions and each has 715 owners.

This is an algebraic separator: an ordinary one-component subtour CEGAR
must not be run on the exact complement-dual master.

## 3. Component voltage directly from `A`

Let the selected physical lift of the arc `a->A(a)` have voltage
`alpha_a in Z_17`.  On an `A`-cycle `Z` put

\[
                         u(Z)=\sum_{a\in Z}\alpha_a.  \tag{3.1}
\]

The factor dart `a->A^2(a)` has voltage

\[
                         \alpha_a+\alpha_{A(a)}.      \tag{3.2}
\]

Therefore:

* if `|Z|` is odd, `A^2` has one quotient component of voltage `2u(Z)`;
* if `|Z|` is even, `A^2` has two quotient components and each has voltage
  `u(Z)`.

For the prime-17 cover, a quotient component of voltage `v` lifts to
`gcd(17,v)` physical components.  Hence a Hamilton `A` of voltage `u!=0`
gives exactly two physical factor cycles; `u=0` gives 34.  Only one
primitive-voltage row on `A` is needed—the two parity voltages are equal.

### Theorem 3.1 (full raw voltage image)

The ordinary integral cycle lattice of the quotient odd graph maps onto
`Z_17` under (3.1).

#### Proof

The physical odd graph is the connected regular `Z_17` cover of the
quotient graph.  Given any deck displacement `g`, connectedness supplies a
physical path from a chosen lift `(a,0)` to `(a,g)`.  Its projection is a
closed quotient walk of voltage `g`.  Decomposing that walk into integral
cycles proves surjectivity.  \(\square\)

This is a cycle-lattice theorem.  It does not by itself prove that the
subset of Hamilton `A`-cycles realizes every voltage class.

## 4. The two restricted lattices

Let `G` be the rank-eight/rank-nine quotient incidence multigraph, orient
all its edges from facets to owners, let

\[
                         \mathcal Z=\ker_{\mathbb Z}B              \tag{4.1}
\]

be its rank-10,011 circulation lattice, and let `c` be edge complement.
There are no fixed edge occurrences: the 12,870 edges form 6,435
complement pairs.  Identifying a pair gives the connected nonbipartite
9-regular odd-graph quotient `Q` with

\[
                 |V(Q)|=1430,\qquad |E(Q)|=6435.    \tag{4.2}
\]

The exact finite census contains eight undirected quotient loops.

A matching change `z=D'-D` induces two different objects:

\[
 \Delta_{\rm supp}=(I+c)z,
 \qquad
 \Delta_{\rm or}=(I-c)z.                            \tag{4.3}
\]

The first is the change of the unoriented factor support
`D union C(D)`.  The second orients `D` against `H` and is the object whose
voltage is factor monodromy.

### Theorem 4.1 (integral lattice split)

1. The support lattice is

   \[
        (I+c)\mathcal Z=\mathcal Z^c
          \cong\ker_{\mathbb Z}Q_{+},               \tag{4.4}
   \]

   where `Q_+` is the signless vertex-edge incidence matrix of the quotient
   odd graph.  It is saturated and has rank

   \[
                         6435-1430=5005.             \tag{4.5}
   \]

2. The oriented anti-invariant space has rank

   \[
                         6435-1430+1=5006.           \tag{4.6}
   \]

   The norm image `(I-c)\mathcal Z` has index two in it.  This is the only
   universal extra integral defect of the complement restriction.

3. Complement reverses quotient voltage, up to the vertex-gauge
   coboundary:

   \[
                         \omega(cz)=-\omega(z).       \tag{4.7}
   \]

   Consequently

   \[
   \omega(\Delta_{\rm supp})=0,
   \qquad
   \omega(\Delta_{\rm or})=2\omega(z).              \tag{4.8}
   \]

   Since the unrestricted incidence-cycle voltage image is `Z_17` and 2
   is a unit modulo 17, the oriented complement-dual lattice still has full
   voltage image `Z_17`.

#### Proof

An invariant circulation assigns one integer to each complement-paired
edge.  Its balance equations are exactly `Q_+w=0`.  Since `Q` is connected
and nonbipartite, `Q_+` has rational rank 1,430, giving (4.5).  The kernel
is saturated.  Conversely, reduce an integral `w in ker Q_+` modulo two.
Its mod-two support is Eulerian.  Orient a cycle decomposition of that
support to obtain an antisymmetric circulation `r` with `r=w (mod 2)`.
Then `(w+r)/2` is an integral circulation whose complement norm is `w`.
This proves equality in (4.4).

The usual directed incidence matrix of connected `Q` has rank 1,429,
giving (4.6).  The connected bipartite double cover `G->Q` has the standard
transfer exact sequence.  Relative to one odd base loop, every invariant
topological cycle is a transfer after its odd-winding parity is removed;
twice the remaining primitive odd class is a transfer.  Hence the quotient
by `(I-c)\mathcal Z` is exactly `Z/2`.

Finally the audited complement shift is a negated edge shift plus one
potential at each endpoint.  Potentials cancel on a circulation, proving
(4.7); (4.8) and the prime-17 conclusion follow.  \(\square\)

An explicit support-lattice basis is obtained from a spanning tree and one
odd base loop: use alternating vectors on even fundamental cycles, and for
each odd fundamental cycle use the signed handcuff joining it to the base
loop, with coefficient two along the joining tree path.

The phrase “full voltage image” must therefore name the lattice: it is
false for complement-even **support deltas**, and true for the oriented
`D`-versus-`H` circulation and for the direct `A` cycle lattice.

## 5. `D`-alternating circuits in `A` language

Split the vertex set of the directed odd graph into a tail copy and a head
copy.  A cycle cover `A` is a perfect matching between these copies.  Let
`A'` be another cycle cover.  Their symmetric difference is a disjoint
union of alternating assignment cycles.  On one such cycle, with changed
tails `x_1,...,x_t`, the switch has the form

\[
       x_i\longmapsto A(x_i)
       \quad\rightsquigarrow\quad
       x_i\longmapsto A(x_{i+1})                    \tag{5.1}
\]

after cyclic reindexing, and every displayed new arc must belong to the
odd-graph quotient.

Thus ordinary `D`-alternating cycles generate all endpoint perfect
matchings.  With arbitrary compound switches, any two complement-dual
endpoint configurations are connected in one step by toggling all
components of their symmetric difference.

Three caveats are exact.

1. Toggling one component at a time can create a forbidden dual collision
   or a two-cycle even when both endpoints are collision-free.
2. It can split a Hamilton `A`; Hamilton-preserving reachability is a
   smaller, unproved Markov problem.
3. The rank-ten turn at `a` uses both the incoming and outgoing selected
   arcs.  It is not a linear image of the matching cycle lattice.

## 6. Exact rank-ten switch ledger

For a matching-cycle switch (5.1), put

\[
                  X=\{x_1,\ldots,x_t\},\qquad Y=A(X).             \tag{6.1}
\]

Only centers in `X union Y` can change their turn colour: an outgoing arc
changes only at `X`, and an incoming arc changes only at `Y`.

For every rank-ten target orbit `T`, let

* `mu_T` be its old occurrence load;
* `loss_T` be the number of changed centers whose old turn is `T`;
* `gain_T` be the number of changed centers whose new turn is `T`.

Then the switched cover remains rank-ten-surjective if and only if

\[
                    \mu_T-\operatorname{loss}_T
                           +\operatorname{gain}_T\ge1
                    \qquad(\text{every }T).          \tag{6.2}
\]

By (1.5), the complementary rank-seven ledger is then automatic.  Equation
(6.2) is the exact cut family consumable by an alternating-cycle master.
It also proves the scope boundary:

> `D`-cycles generate the whole restricted matching fibre, but no linear
> cycle-lattice theorem alone generates rank-ten coverage.

The remaining existence problem is precisely a collision-free Hamilton
cycle `A` of primitive voltage whose 1,430 local label pairs cover all
1,144 target orbits.

## 7. The 286 repeat units and one non-dual splice

Assume the remaining existence problem in Section 6 has a solution.  Its
turn loads obey

\[
          \sum_T\mu_T=1430,qquad
          \sum_T(\mu_T-1)=1430-1144=286.            \tag{7.1}
\]

These are 286 repeat **occurrence units**.  The number of distinct targets
with load at least two need not be 286.

The factor `A^2` has two parity cycles.  Keep `D`, delete one `H` edge from
each cycle, and reconnect the two owner/facet endpoint pairs crosswise.
This is the unique two-edge perfect-matching move that can merge the two
cycles.  If the old `H` shifts are `h_p,h_q`, the new shifts are
`h'_p,h'_q`, and the Hamilton `A` has voltage `u`, the joined quotient
factor has voltage

\[
                 V'=2u+h_p+h_q-h'_p-h'_q\pmod {17}.               \tag{7.2}
\]

It has one physical lift exactly when `V'!=0`.

The switch changes two upper occurrences, at its two facet endpoints, and
two lower occurrences, at its two owner endpoints.  Before the splice, the
two lower tickets correspond by (1.5) to two further upper tickets.  Thus
the exact deletion screen can be written on one palette as four old upper
occurrences.  For each target `T`, let `d_T` and `a_T` count the deleted and
added occurrences across the appropriate upper/lower ledgers.  Palette
survival is exactly

\[
                         \mu_T-d_T+a_T\ge1.           \tag{7.3}

\]

The scalar 286 proves ample total excess for four deletions, but it does
not place those excess tickets on a legal cross rectangle.  The exact live
splice gate is therefore:

1. one old `H` edge on each parity cycle;
2. both crossed quotient incidences exist and avoid `D`;
3. (7.2) is nonzero;
4. the four-ticket inequalities (7.3) hold;
5. the boundary pins, residence halos, and deeper opening survive.

This is the sharp use of the repeat budget.  It is an `O(1)` coloured
incidence problem, not a consequence of the number 286 alone.

## 8. Audited finite geometry and scope

The repository audits used by this note establish:

* 1,430 owner and 1,430 facet orbits;
* 12,870 directed incidence/odd-graph arcs;
* 6,435 fixed-point-free complement pairs;
* 51,480 local turns and all 1,144 upper and lower target orbits available;
* 218,790 physical phase arcs replayed;
* 16 directed quotient loop arcs, i.e. eight undirected loops;
* the forced cycle sizes `[715,715]` under an exact Hamilton `A`.

Relevant frozen files are:

* `MATH_THEOREM_K17_COMPLEMENT_DUAL_ONE_MATCHING_PALETTE_REDUCTION_20260801.md`;
* `MATH_AUDIT_K_K17_COMPLEMENT_DUAL_ONE_MATCHING_PALETTE_AND_TOPOLOGY_20260801.md`;
* `scratch/k17_age_direct_A_cycle_master_20260801.audit.json`;
* `scratch/k17_age_complement_dual_matching_master_20260801.audit.json`;
* `MATH_THEOREM_THREAD_D_K17_INCIDENCE_PATH_LATTICE_AND_RANK7_RUN4_CUTS_20260801.md`.

No SAT solve and no `k=17` word is claimed.  Full voltage is a formal
cycle-lattice result; rank-ten Hamilton existence and the coloured external
splice remain the exact finite gates.
