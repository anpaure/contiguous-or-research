# A syndrome-suspended `Q_4` braid bank: exponentially many independent packet-order switches

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Outcome

The antipodally repaired finite braid in
`MATH_THEOREM_Q4_COMMON_PHASE_BLOCK_TRANSPOSITION_20260726.md` is valid:
its two shores are exact isometric `C_8`-factors of `Q_4`, their direction
words are

\[
                         1234\,1234,
             \qquad      1432\,1432,                 \tag{0.1}
\]

and the displayed column index is one common cyclic phase colouring.
The move is an antipodally doubled nonconstant packet-order braid.  It is
not, by itself, a proof of equality of a protected multi-depth collar, and
the packet-colour word change is not literally one isolated consecutive
`AB -> BA` swap.

The finite braid does globalize cleanly inside the standard syndrome
factor.  Let `h=2^a>=4`.  The standard parity-alternating syndrome map has
many repeated coordinate columns.  Choose two repeated columns at cyclic
distance two and transpose the corresponding cube directions.  If `F` is
one standard syndrome `C_{2h}`-factor and `tau F` its coordinate-conjugate,
then their ownership overlap graph has exactly

\[
                         {2^h\over4h}                 \tag{0.2}
\]

connected components.  Every component contains two cycles of `F` and two
cycles of `tau F`; the two shores partition the same `4h` owners.  The
components may therefore be switched independently, producing

\[
                         2^{,2^h/(4h)}               \tag{0.3}
\]

exact owner factors.  In each switched component exactly two cycles change
their direction order by the prescribed transposition.  Only four phase
owners per cycle move to the partner cycle.

Thus the desired scale is achieved:

\[
 \boxed{
   \Theta(2^h/h)\text{ independent components, each with two cycles per
   shore and a bounded phase-local payload}.}         \tag{0.4}
\]

The exact granularity is a pair of cycles, not one cycle.  The equal-syndrome
condition is the algebraic reason the overlap stays local; an arbitrary
direction transposition need not have this component structure.

## 1. Audit of the repaired `Q_4` table

Use the two rows

\[
\begin{array}{c|cccccccc}
j&0&1&2&3&4&5&6&7\\ \hline
a_j&0000&1000&1100&1110&1111&0111&0011&0001\\
b_j&0101&1101&1001&1011&1010&0010&0110&0100.
\end{array}                                           \tag{1.1}
\]

They are disjoint and exhaust `Q_4`.  The first factor consists of the two
rows and has direction word `1234 1234`.  The repaired second factor is

\[
\begin{aligned}
 &(a_0,a_1,b_2,b_3,a_4,a_5,b_6,b_7),\\
 &(b_0,b_1,a_2,a_3,b_4,b_5,a_6,a_7).
\end{aligned}                                         \tag{1.2}
\]

Both rows in (1.2) have direction word `1432 1432`.  For example, the
first row has successive directions

\[
                         1,4,3,2,1,4,3,2.             \tag{1.3}
\]

The second row has the same word.  Hence all four cycles are isometric.
Every row takes one vertex from each column `j`, so

\[
                         c(a_j)=c(b_j)=j\pmod8         \tag{1.4}
\]

is cyclic on both shores.

If directions `1,2` have packet colour `A` and `3,4` colour `B`, the two
words are `AABBAABB` and `ABBAABBA`.  Four antipodally paired phase
positions change.  Thus the finite theorem proves nonzero block-order
holonomy with common ownership and phase.  Calling it one isolated
adjacent packet transposition would be stronger than the table proves.

The ownership-overlap graph of the two old cycles and the two new cycles
is `K_{2,2}`, with multiplicity four on every incidence, so the finite
trade is one connected component.  Its edge symmetric difference is four
small square faces, but the faces are not independently switchable: among
the sixteen partial shore choices, only switching none or switching all
four gives an isometric `C_8`-factor.

Common phase is also strictly weaker than a common protected collar.  At
depth one the two shores have sixteen distinct targets each but only eight
in common.  Their aggregate depth-two and depth-three target multisets do
coincide, while their phase-resolved versions do not.  Hence the finite
table is a valid closed braid and suspension seed, but a ported use still
requires an explicit collar calculation.

## 2. The standard syndrome factor with a repeated pair

Let

\[
                         V=\mathbb F_2^h,
             \qquad     A=\mathbb F_2^a,
             \qquad     |A|=h.                       \tag{2.1}
\]

Choose a nonzero linear functional `lambda:A -> F_2`, put
`A_0=ker(lambda)`, and choose `z` with `lambda(z)=1`.  Enumerate

\[
                         A_0=\{a_0,\ldots,a_{h/2-1}\}
\]

and define

\[
 u_{2j}=a_j,
 \qquad
 u_{2j+1}=a_j+z,
 \qquad
 w_i=u_i+u_{i+1}.                                    \tag{2.2}
\]

Subscripts on `u` are cyclic modulo `h`.  Define the syndrome map

\[
                         \Psi(e_i)=w_i.               \tag{2.3}
\]

The standard telescoping argument gives `Psi(1)=0` and makes the prefix
syndromes a complete transversal of `A`.  The feature needed here is even
simpler:

\[
                         w_{2j}=z
                 \qquad(0\le j<h/2).                 \tag{2.4}
\]

In particular

\[
                         \Psi(e_0)=\Psi(e_2).         \tag{2.5}
\]

Put

\[
 K=\ker\Psi,
 \qquad
 \delta=e_0+e_2,
 \qquad
 \tau=(0\ 2).                                        \tag{2.6}
\]

Then `delta in K`, `tau K=K`, and `tau(1)=1`.

### Lemma 2.1 (an invariant phase complement)

There is a `tau`-invariant direct-sum decomposition

\[
                         K=K_0\oplus\langle\mathbf1\rangle        \tag{2.7}
\]

with `delta in K_0`.

#### Proof

For every `x in K`,

\[
                         \tau x+x\in\langle\delta\rangle.        \tag{2.8}
\]

Because `h>=4`, the vectors `1` and `delta` are independent.  Choose a
linear functional `eta:K -> F_2` such that

\[
                         \eta(\mathbf1)=1,
             \qquad     \eta(\delta)=0.              \tag{2.9}
\]

Equation (2.8) implies `eta(tau x)=eta(x)`.  Hence
`K_0=ker(eta)` is `tau`-invariant, contains `delta`, and is a complement
to `1`.  \(\square\)

Let

\[
 p_i=e_0+\cdots+e_{i-1}\quad(0\le i<h),              \tag{2.10}
\]

and let `P` be the isometric cycle with vertex order

\[
 p_0,p_1,\ldots,p_{h-1},
 \mathbf1+p_0,\mathbf1+p_1,\ldots,\mathbf1+p_{h-1}.  \tag{2.11}
\]

Its direction word is

\[
                 0,1,\ldots,h-1,0,1,\ldots,h-1.      \tag{2.12}
\]

The standard syndrome factor is

\[
                         \mathcal F^0
                  =\{P+k:k\in K_0\}.                 \tag{2.13}
\]

It contains

\[
                         |K_0|={2^h\over2h}            \tag{2.14}
\]

vertex-disjoint isometric `C_{2h}`'s and partitions `Q_h`.

Now put

\[
                         \mathcal F^1=\tau\mathcal F^0
                    =\{\tau P+k:k\in K_0\}.          \tag{2.15}
\]

The equality uses `tau K_0=K_0`.  This is again an exact isometric factor,
and every cycle has direction word

\[
                         2,1,0,3,4,\ldots,h-1
\]

repeated twice.  Up to a cyclic phase rotation and a relabelling of the
four displayed directions, this is exactly the packet-order change in
(0.1).

## 3. One common cyclic phase colouring

For every `x in V`, its syndrome uniquely determines an index
`i in {0,...,h-1}` through

\[
                         \Psi(x)=\Psi(p_i).           \tag{3.1}
\]

Then `x+p_i in K`.  Define

\[
 c(x)=i+h\eta(x+p_i)\pmod{2h}.                       \tag{3.2}
\]

### Theorem 3.1 (global common phase)

The map (3.2) increases by one around every oriented cycle of both
`F^0` and `F^1`.

#### Proof

On `P+k`, with `k in K_0`, the two vertices of syndrome `Psi(p_i)` are
`p_i+k` and `1+p_i+k`.  Equation (3.2) gives them colours `i` and `i+h`,
respectively, which is exactly their cyclic position in (2.11).

For the second factor, put

\[
                         d_i=\tau p_i+p_i.            \tag{3.3}
\]

Directly from the prefix order,

\[
 d_i=
 \begin{cases}
  \delta,&i=1,2,\\
  0,&\text{otherwise}.
 \end{cases}                                         \tag{3.4}
\]

Thus `eta(d_i)=0`.  The right-shore phase-`i` vertex `tau p_i+k` has,
relative to the left prefix `p_i`, kernel displacement `d_i+k`, on which
`eta` is zero.  Its complement has `eta`-value one.  Hence (3.2) again
gives phases `i` and `i+h`.  \(\square\)

This is stronger than merely assigning phases separately on the two
factors: it is one owner colouring of all of `Q_h` compatible with both.

## 4. Exact ownership-overlap components

For `k in K_0`, write

\[
                         L_k=P+k,
             \qquad     R_k=\tau P+k.                \tag{4.1}
\]

Regard `L_k,R_k` as cycle vertices in the bipartite ownership-overlap
multigraph; every cube owner supplies one overlap edge.

### Theorem 4.1 (two-by-two component classification)

For every `k in K_0`,

\[
 \begin{aligned}
 |R_k\cap L_k|&=2h-4,\\
 |R_k\cap L_{k+\delta}|&=4,
 \end{aligned}                                       \tag{4.2}
\]

and `R_k` meets no other left cycle.  Consequently the connected
components are indexed by the cosets of `<delta>` in `K_0` and have the
form

\[
 \{L_k,L_{k+\delta}\}
       \quad\hbox{versus}\quad
 \{R_k,R_{k+\delta}\}.                               \tag{4.3}
\]

There are exactly

\[
                         {|K_0|\over2}={2^h\over4h}   \tag{4.4}
\]

such components.

#### Proof

Equations (3.3)--(3.4) say that `tau P` agrees with `P` at every phase
except `1,2,1+h,2+h`.  At those four phases it equals the corresponding
vertex of `P+delta`.  Translation by `k` proves (4.2).  Since the left
cycles partition the cube, there are no other intersections.

Both multiplicities in (4.2) are positive.  Hence `R_k` joins the left
labels `k` and `k+delta`, and the same is true with those labels reversed
for `R_{k+delta}`.  This gives exactly (4.3).  Distinct cosets are
disconnected, proving (4.4).  \(\square\)

### Corollary 4.2 (literal independent braid switches)

For every coset `k+<delta>`,

\[
             L_k\mathbin{\dot\cup}L_{k+\delta}
             =R_k\mathbin{\dot\cup}R_{k+\delta}      \tag{4.5}
\]

as owner sets.  Choosing either shore independently in every component
always gives another exact isometric `C_{2h}`-factor of `Q_h`.

Thus the two syndrome factors span an explicit Boolean cube of exact
factors of dimension `2^h/(4h)`.  A switch changes the direction order on
exactly two cycles.  It cannot change only one of them: the overlap
component (4.3) is connected and each right cycle imports four owners from
its partner.

The modification is phase-local.  A right cycle retains `2h-4` owners of
its same-labelled left cycle and moves exactly four phase owners to the
partner.  The component support has `4h` owners, so “bounded component”
means a bounded number of long cycles and a bounded number of rerouted
phases, not a bounded number of cube vertices.

## 5. Exact row-specific routing inside equal-column classes

The preceding binary bank is the rank-one case of an exact routing
criterion.  Let `G` be any group of coordinate permutations which preserves
every syndrome column:

\[
                         \Psi\sigma=\Psi
                 \qquad(\sigma\in G).                \tag{5.1}
\]

Put

\[
 D_G=\sum_{\sigma\in G}\operatorname {im}(\sigma-I). \tag{5.2}
\]

Then `D_G subseteq K`.  Assume `1 notin D_G`.  Choose the functional
`eta` in Lemma 2.1 to vanish on `D_G`; then `K_0=ker(eta)` is invariant
under every member of `G`.

For `sigma in G` and phase `i`, define the phase displacement

\[
                         d_i(\sigma)=\sigma p_i+p_i\in D_G.       \tag{5.3}
\]

Choose a possibly different permutation `sigma_k in G` for every row
label `k in K_0`, and form the oriented cycles

\[
                         C_k=\sigma_kP+k.             \tag{5.4}
\]

### Theorem 5.1 (phasewise Latin criterion)

The cycles in (5.4) form an exact `C_{2h}`-factor of `Q_h` if and only if,
for every phase `i`, the map

\[
 T_i:K_0\longrightarrow K_0,
 \qquad
 T_i(k)=k+d_i(\sigma_k)                               \tag{5.5}
\]

is a permutation.  Whenever this holds, the cycles have the one common
phase colouring (3.2).

#### Proof

At phase `i`, the first-half owner in row `k` is

\[
 \sigma_kp_i+k=p_i+T_i(k).                            \tag{5.6}
\]

The left factor has exactly one phase-`i` owner `p_i+l` for every
`l in K_0`.  Hence the new rows cover that phase class exactly once if and
only if `T_i` is bijective.  The antipodal phase `i+h` is obtained by adding
`1`, so it imposes the identical condition.  The `2h` phase classes
partition the cube, proving necessity and sufficiency.

Every displacement in (5.3) lies in `D_G`, on which `eta` vanishes.
Therefore (3.2) assigns colour `i` to (5.6) and colour `i+h` to its
complement.  This proves the common-phase assertion.  \(\square\)

For one transposition `tau=(a b)` of equal-syndrome coordinates, put
`delta=e_a+e_b`.  The displacement `d_i(tau)` is `delta` exactly when the
prefix `p_i` contains one of `a,b`, and is zero otherwise.  A binary
row-specific field has the form

\[
                         \sigma_k=\tau^{\varepsilon(k)},
             \qquad     \varepsilon:K_0\to\mathbb F_2.           \tag{5.7}
\]

At every affected phase, (5.5) is

\[
                         k\longmapsto k+\varepsilon(k)\delta.     \tag{5.8}
\]

### Corollary 5.2 (complete classification for one transposition)

The row-specific field (5.7) is an exact factor if and only if

\[
                         \varepsilon(k)=\varepsilon(k+\delta)
                  \qquad(k\in K_0).                  \tag{5.9}
\]

Thus one may choose the transposed order independently on every pair
`{k,k+delta}`, but not independently on the two rows inside that pair.

#### Proof

On a `delta`-pair, (5.8) is a permutation precisely in the two cases
`(epsilon(k),epsilon(k+delta))=(0,0)` and `(1,1)`: it respectively fixes
or swaps the two labels.  The mixed choices identify two inputs and omit
one output.  Apply Theorem 5.1.  \(\square\)

This recovers the overlap components of Theorem 4.1 and proves that their
two-cycle granularity is not an artefact of that proof; it is the exact
owner-partition constraint.

More generally, suppose an equal-column class has `s` coordinates and `G`
is its full symmetric group, fixing all other coordinates.  Then

\[
                         D_G=
 \{x:\operatorname {supp}(x)\text{ lies in the class and }|x|\text{ is even}\},
                                                               \tag{5.10}
\]

which has dimension `s-1`.  Since coordinates outside the class are fixed,
`1 notin D_G`, so zero midpoint holonomy and a common phase colouring are
available for every such permutation.  Arbitrary row-by-row choices are
not automatically legal: their exact and complete constraint is the
simultaneous family of Latin conditions (5.5).

The parity-alternating standard syndrome used in Section 2 already has the
equal-column class

\[
                         \{0,2,4,\ldots,h-2\}          \tag{5.11}
\]

of size `h/2`.  A Gray-code syndrome enumeration may provide other repeated
classes, but is not needed for the existence or scale of the present bank.

## 6. Scope and the next gate

The theorem gives precisely the requested ownership globalization for one
packet transposition:

* common middle support;
* one common cyclic owner phase;
* `Theta(2^h/h)` independent owner-trade components;
* a prescribed cycle-order transposition selected separately on every
  two-cycle packet; and
* no loss of physical isometry.

The repeated-syndrome hypothesis is load-bearing.  If directions `a,b`
have different syndrome columns, then `e_a+e_b` is not in `K`; the two
changed prefix arcs do not merely move to a fixed partner cycle, and neither
the two-by-two component theorem nor the common phase formula follows.

The remaining global question is no longer whether bounded/local braid
components exist.  They do, at the optimal exponential count.  It is
whether choices from this Boolean bank can be coordinated across many
different repeated-column transpositions so that their cycle-specific
direction orders satisfy the simultaneous lower/upper Gaussian shadow
Hall inequalities.  One fixed transposition supplies only one binary order
bit per two-cycle component.
