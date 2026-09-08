# Endpoint-hole feasibility has an exact degree-fibre law and a minimal
# phase-aligned two-stratum repair

Date: 2026-08-01  
Lane: controlled-leave coordinate cocycle / multi-stratum repair  
Status: exact hole-degree characterization, exact two-stratum normal form,
bounded fractional feasibility from `m>=7`, and an integral coordinate/
lower-avoidance construction for all sufficiently large `m`.  The common-
`M_0` extension, coloured exit SDR, residual forest, and compiler remain open.

## 0. Outcome

Let

\[
 C=\operatorname {Cat}_m,qquad c=\operatorname {Cat}_{m-1},
 \qquad I_m=C-2c.                                                \tag{0.1}
\]

For any packet interface, let `E_t` be

\[
 E_t=(\text{reserved owner-slot incidence at }t)
     -(\text{reserved lower incidence at }t)
     -(\text{reserved upper incidence at }t).                    \tag{0.2}
\]

The full odd host contributes `-2c` at every coordinate.  Therefore exact
upper/slot saturation with a `C`-set unused lower family `H` is possible at
the coordinate layer only if

\[
                         \boxed{E=2c\,\mathbf1+d_H}.              \tag{0.3}
\]

This note gives an exact characterization of the possible degree vectors
`d_H` and the smallest stratum repair of the frozen one-stratum failure.

One controlled mixed-head packet in ordered stratum `(a,z)` contributes

\[
                         2e_a+e_z+\chi_S+\chi_L.                  \tag{0.4}
\]

This signature is unchanged if the anonymous controlled target is replaced
by the four-row canonical rooted phase.  A single stratum has `E_a=2C` and
is impossible because `d_H(a)<=C` while `C>2c`.

Two **swapped** strata `(a,z)` and `(z,a)` are minimal and remove this
singleton obstruction.  If the first contains `q` packets and the second
`C-q`, then

\[
 d_H(a)=C+q-2c,qquad d_H(z)=2C-q-2c,                             \tag{0.5}
\]

and both lie in `[0,C]` exactly when

\[
                         C-2c\le q\le2c.                         \tag{0.6}
\]

The interval is nonempty because `C<4c`.

There is an exact two-stratum normal form for the remaining coordinates.
It has a bounded rational solution from `m>=7`, and a Kneser-circulation
construction realizes it integrally in the full lower layer for all
sufficiently large `m`.  The hole family may be chosen first and the packet
cores then chosen to avoid its one-special-coordinate members.  Thus the
one-stratum failure is repaired at the endpoint layer with the minimum two
strata.  The unresolved rows are the common-`M_0` extension, one coloured
exit SDR, and the residual physical forest/compiler.

## 1. Exact feasible endpoint-hole degree vectors

Let `A` be the allowed residual lower family, a subfamily of
`binom(Omega,m-1)`.  Define

\[
 \mathfrak D_C(A)=
 \left\{d_H:\ H\subseteq A,\ |H|=C\right\}.                      \tag{1.1}
\]

### Theorem 1.1 (exact coefficient/fibre characterization)

For an integer vector `h in Z^Omega`, the following are equivalent.

1. `h in mathfrak D_C(A)`.
2. The binary system

\[
 \sum_{K\in A}x_K=C,qquad
 \sum_{K\in A:t\in K}x_K=h_t\quad(t\in\Omega),qquad
 x_K\in\{0,1\}                                                    \tag{1.2}
\]

   is feasible.
3. In the multivariate polynomial

\[
 \Phi_A(y,\mathbf x)=
       \prod_{K\in A}\left(1+y\prod_{t\in K}x_t\right),         \tag{1.3}
\]

   the coefficient `[y^C product_t x_t^(h_t)]` is positive.

#### Proof

Choosing the `y product_(t in K)x_t` term records selecting the distinct
lower resource `K`.  Its `y`-degree is the family size and its exponent at
`x_t` is the coordinate degree.  This proves all equivalences. \(\square\)

In particular every feasible vector satisfies

\[
 0\le h_t\le C,qquad \sum_t h_t=(m-1)C.                          \tag{1.4}
\]

There are sharper support inequalities.  For any weight vector `lambda`,
order the allowed lower sets by

\[
                         w_\lambda(K)=\sum_{t\in K}\lambda_t.    \tag{1.5}
\]

If `w_(1)>=...` are these weights in decreasing order, then

\[
                         \lambda\cdot h\le\sum_{i=1}^Cw_{(i)}.   \tag{1.6}
\]

The inequalities (1.6), for all `lambda`, characterize the convex hull of
`mathfrak D_C(A)`.  They do not by themselves certify an integral fibre in
(1.2); the binary coefficient in (1.3) is the exact integral condition.

Combining Theorem 1.1 with the coordinate cocycle gives the promised
positive law:

### Corollary 1.2 (endpoint-hole law)

A packet deletion vector `E` passes the complete coordinate layer if and
only if

\[
                         E-2c\mathbf1\in\mathfrak D_C(A).         \tag{1.7}
\]

This is necessary for a residual matching.  It is not sufficient for the
upper/lower/slot matching or graphic rows.

## 2. The packet excess signature is phase-invariant

Fix distinct coordinates `a,z`, put `G=Omega-{a,z}`, and let

\[
                         S<L,qquad |S|=m-2,quad |L|=m-1         \tag{2.1}
\]

be a central SCD edge in `G`.

For the anonymous controlled packet, reserve uppers `azL,azV`, lowers
`aS,L`, and slot multiset

\[
                         2[aL]+2[azS]+[aV]+[zL].                  \tag{2.2}
\]

Direct cancellation gives

\[
 \delta_{a,z}(S,L)=2e_a+e_z+\chi_S+\chi_L.                       \tag{2.3}
\]

The four-row rooted packet instead reserves target `aU`, rerouted lower
`zS`, and the same slot multiset, where

\[
                         U=L+b,qquad V=S+b.                      \tag{2.4}
\]

Its excess is

\[
\begin{aligned}
 &2\chi_{aL}+2\chi_{azS}+\chi_{aV}+\chi_{zL}
 -\chi_{aS}-\chi_{zS}-\chi_{azL}-\chi_{aU}\\
 &=2e_a+e_z+2\chi_L+\chi_V-\chi_U\\
 &=2e_a+e_z+\chi_S+\chi_L,                                      \tag{2.5}
\end{aligned}
\]

because `U=L+b`, `V=S+b`, and `L=S+u`.  Hence (2.3) is independent of
which of these two packet realizations is used.

For the rooted realization, deletion of the fixed letter `a` gives the
C-phase on a short SCD chain and the clean D-phase on a long chain.  Thus
every first-stratum provider has a canonical four-row phase.  The joint
two-stratum phase/resource rows are considered in Section 6.

## 3. Minimality and the swapped two-stratum interval

Take `C` packets in one `(a,z)` stratum.  Since all `S,L` lie in `G`,
(2.3) gives

\[
                         E_a=2C,qquad E_z=C.                     \tag{3.1}
\]

Equation (1.7) would require `h_a=2C-2c>C`, proving that one stratum is
impossible.

Now take `q` packets in stratum `(a,z)` and `C-q` in the swapped stratum
`(z,a)`.  Their distinguished-coordinate excess is

\[
                         E_a=C+q,qquad E_z=2C-q.                 \tag{3.2}
\]

The singleton conditions `0<=E_a-2c,E_z-2c<=C` reduce exactly to (0.6).
Indeed the only nontrivial inequalities are

\[
                         q\le2c,qquad q\ge C-2c.                \tag{3.3}
\]

The interval has integer points because

\[
                         4c-C={6c\over m+1}>0.                   \tag{3.4}
\]

Thus two coordinate strata are necessary and sufficient for the
distinguished singleton cuts.

## 4. Exact two-stratum hole normal form

Put

\[
 r_a=2c-q,qquad r_z=q-(C-2c),qquad
 s=r_a+r_z=4c-C.                                                  \tag{4.1}
\]

All three numbers are nonnegative under (0.6).  An exact lower-hole family
with the distinguished degrees in (0.5) may be put in the following normal
form:

* `C-s` holes contain both `a,z` and an `(m-3)`-set from `G`;
* `r_z` holes contain `a` but not `z` and an `(m-2)`-set from `G`;
* `r_a` holes contain `z` but not `a` and an `(m-2)`-set from `G`;
* no hole omits both distinguished coordinates.

Indeed `r_a=C-h_a` and `r_z=C-h_z` are exactly the numbers omitting `a`
and `z`.

Let `P_1,P_2` be the selected central-pair banks in the two strata and put

\[
 e_G(t)=
 \#\{(S,L)\in P_1\cup P_2:t\in S\}
 +\#\{(S,L)\in P_1\cup P_2:t\in L\}.                             \tag{4.2}
\]

Let `X_11,X_10,X_01` denote the three `G`-families in the normal form.
Then the complete endpoint-hole law is exactly

\[
 \boxed{
 e_G(t)=2c+d_{X_{11}}(t)+d_{X_{10}}(t)+d_{X_{01}}(t)
 \quad(t\in G).}                                                  \tag{4.3}
\]

Together with distinctness and avoidance of the reserved lower resources,
(4.3) is equivalent to (1.7).  It is the smallest integral correlation
left after the distinguished coordinates are repaired.

## 5. Fractional and integral realizations

Let

\[
                         n=|G|=2m-3,qquad
 N={n\choose m-2}.                                                \tag{5.1}
\]

Across the complete central-pair bank, the `S` shore is all rank-`m-2`
sets and the `L` shore is all rank-`m-1` sets.  Therefore every coordinate
of `G` has total load

\[
 {n-1\choose m-3}+{n-1\choose m-2}
 ={n\choose m-2}=N.                                              \tag{5.2}
\]

Give every central pair total weight `C/N` and split this weight between
the two strata so their total masses are `q,C-q`.  Then

\[
                              e_G(t)=C\qquad(t\in G).             \tag{5.3}
\]

On the hole side, distribute the three category masses from Section 4
uniformly over their respective Boolean ranks.  Every coordinate of `G`
then has load

\[
 { (C-s)(m-3)+s(m-2)\over2m-3}=C-2c.                            \tag{5.4}
\]

The equality follows from `s=4c-C` and

\[
                         (m+1)C=2(2m-1)c.                        \tag{5.5}
\]

Equations (5.3)--(5.4) prove (4.3) exactly over the rationals.

### Theorem 5.1 (minimal bounded fractional repair)

For every `m>=7` and every rational `q` in (0.6), the swapped two-stratum
system has an exact fractional packet/hole solution of (0.3) with every
individual resource used with weight at most one.  No one-stratum
fractional solution satisfies even the singleton cap at its add coordinate.

The threshold in this uniform construction is real: the category containing
both `a,z` has mass `C-s=2(C-2c)`, but only
`binom(2m-3,m-3)` resources.  The capacity inequality first holds at
`m=7` (with equality there); it fails for `m=3,4,5,6`.

There is also an exact integral realization in the full lower layer.

### Theorem 5.2 (integral Kneser-circulation realization)

For all sufficiently large `m`, there are `C` distinct central pairs
`S<L`, split between the two swapped strata in any integer sizes
`q,C-q` satisfying (0.6), and `C` distinct rank-`(m-1)` holes such that
(0.3) holds exactly.  Moreover the holes may be chosen first and the
central pairs chosen so that no one-special-coordinate hole is a reserved
packet lower.

#### Proof

Put `r=m-2` and consider the odd Kneser graph `KG(2r+1,r)` on the
rank-`r` subsets of `G`.  For a directed edge `S->J`, set

\[
                         L=G-J.                                  \tag{5.6}
\]

Then `S subset L`, and a directed cycle union `P` of order `C` obeys

\[
 \sum_{S\in P}(\chi_S+\chi_{L(S)})
 =\sum_{S\in P}(\mathbf1_G+\chi_S-\chi_{J(S)})
 =C\mathbf1_G.                                                   \tag{5.7}
\]

The odd Kneser graph has a cycle cover: take an incidence bijection from
rank `r` to rank `r+1` and complement its images.  Taking alternating edges
in its cycles gives a matching of order at least `N/3`.  Since

\[
 {C\over N}={4(2m-1)\over m(m+1)}=O(m^{-1}),                    \tag{5.8}
\]

`C/2` disjoint matching edges are available for all sufficiently large
`m`; use them as directed two-cycles.  If `C` is odd, use one standard odd
cycle of length `2m-3` and fill the remaining even number of vertices by
two-cycles.  Deleting the polynomial-size odd cycle does not affect (5.8).

Write

\[
 I=C-2c,\qquad J_0=4c-C={3C\over2m-1},\qquad
 q=I+t,\quad 0\le t\le J_0.                                    \tag{5.9}
\]

Choose holes in the three classes

\[
 2I\text{ of type }az{G\choose m-3},\qquad
 t\text{ of type }a{G\choose m-2},\qquad
 (J_0-t)\text{ of type }z{G\choose m-2}.                       \tag{5.10}
\]

Among all simple choices with these class sizes, minimize the sum of
squares of the `G`-degrees.  If two degrees differ by at least two, in one
class a selected set containing the larger-degree coordinate has an
unselected one-coordinate swap toward the smaller-degree coordinate.
That swap preserves its class and simplicity and decreases the square sum.
Hence all `G`-degrees differ by at most one.  Their average is the integer
`I`, so every one equals `I`.  Equations (3.2), (5.7), and (5.10) now give
the exact vector in (0.3).

For lower avoidance, choose (5.10) first and let `F` be the union of the
ordinary cores of the one-special-coordinate holes.  Then

\[
                         |F|=J_0={6c\over m+1}.                  \tag{5.11}
\]

Removing all matching edges incident with `F` loses at most `|F|` edges,
and

\[
                         {N\over3}-|F|>{C\over2}                 \tag{5.12}
\]

for all sufficiently large `m`.  In the odd case a random coordinate
translate of the standard odd cycle avoids `F`, because its expected
intersection is `(2m-3)|F|/N<1`; the remaining matching still supplies the
two-cycles.  Thus take `P cap F=emptyset`.  The reserved lowers are `aS`
and `zS`, while the only holes with these signatures have cores in `F`, so
they are disjoint.  \(\square\)

Theorem 5.2 proves an integral endpoint/lower-avoidance theorem.  It does
not say that its central pairs extend to one fixed SCD or that the exit
labels can be chosen without typed collisions.

## 6. Resource and four-row phase interface

There are two different physical realizations and they must not be
conflated.  The anonymous packet below puts both auxiliary and target
uppers in one `az`-signature bank, so resource disjointness requires

\[
                              2C\le N.                            \tag{6.0}
\]

This first holds at `m=15`; in particular the anonymous finite
`m=6,7,8,9` instances are pigeonhole-UNSAT.  The corrected four-row packet
uses separate `aU` and `zU` target banks.  The paired flagged-Kneser theorem
in
`MATH_THEOREM_CATALAN_PHASE_COMPATIBLE_PAIRED_KNESER_BLOCK_BANK_20260801.md`
constructs its complete typed resource bank asymptotically.  Its remaining
owner-basis condition is the residual Hall row recorded below.

The anonymous controlled packet cube can use a common pair of incidence
bijections `sigma,beta`.  If

\[
                         \tau=\sigma^{-1}\beta                    \tag{6.1}
\]

and `P` is independent in the cycle graph of `tau`, then partitioning `P`
as `P_1 dotcup P_2` between the swapped strata preserves all resource rows:

* `sigma(P)` and `beta(P)` are disjoint, separating all upper banks;
* `P_1,P_2` and `sigma(P_1),sigma(P_2)` separate the lower banks; and
* the `{a,z}` signatures separate the physical owner banks, with the only
  repeated signatures again reduced to `sigma(P) cap beta(P)=emptyset`.

Hence the exact anonymous two-stratum packet cube is available for every
integer `q` in (0.6), once an independent set of order `C` has been chosen.
What is not automatic is the hole-degree fibre (4.3).

For the canonical four-row rooted realization, the same excess law holds,
but replacing the `beta` target by `U=L+b` introduces the joint injectivity
rows

\[
                         U=L+b,qquad V=S+b.                      \tag{6.2}
\]

Each first-stratum provider has a canonical short-C/long-D phase.  A
simultaneous swapped-stratum bank must additionally reconcile the two
phase orientations and all cross-stratum `U,V` collisions.  Thus the
anonymous independent-set construction cannot be cited as a fixed-`M_0`
rooted packet theorem.

For the corrected packet, a core `S->J`, `L=G-J`, and `b in J` plants

\[
 aS\mapsto aL,\qquad zS\mapsto azS,\qquad L\mapsto zL.          \tag{6.3}
\]

Across a resource-disjoint bank these are `3C` distinct incidence rows.
If `D_P` and `I_P` are their domain and image banks, extension to one
perfect owner basis is equivalent to

\[
 |N(X)\setminus I_P|\ge |X|
 \quad\text{for every }X\subseteq
 {\Omega\choose m-1}\setminus D_P.                             \tag{6.4}
\]

This exact Hall row, rather than the finite same-signature pigeonhole, is
the first open phase gate for the corrected asymptotic construction.

## 7. Exact remaining positive target

The coordinate obstruction is repaired at the smallest possible stratum
count, but exact odd synchronization still needs one integral object:

> Choose a resource-disjoint two-stratum packet bank, an allowed `C`-set
> lower-hole family, and—on the rooted route—a joint `U,V` phase assignment,
> so that the coefficient condition (1.3) and the coupling equation (4.3)
> hold while the induced residual host retains its local-load bounds.

After this degree fibre is solved, upper/slot saturation and graphic
independence are still separate.  The present theorem proves that a
two-stratum repair is the minimal viable interface and identifies its exact
integral correlation; it does not overclaim a completed residual forest.
