# Triangular chain atoms: exact rank rounding, the representative absorber, and a generic Greene--Kleitman no-go

Date: 2026-08-01  
Status: unconditional exact reductions and a sharp generic-poset obstruction.
No zero- or constant-defect Boolean triangular factor is claimed.

## 0. Scope and verdict

Put

\[
 r=\left\lceil\frac{k}{2}\right\rceil,
 \qquad W=\binom{k}{r},
 \qquad \mathcal L=\{S\subseteq[k]:1\le |S|<r\},
 \qquad \Lambda=|\mathcal L|,
\]

and let

\[
 d=\min\left\{q:qW+\binom{q+1}{2}\ge\Lambda\right\},
 \qquad h=(\Lambda-dW)_+.
\]

The exact fractional theorem in
`MATH_THEOREM_OPTIMAL_TRIANGULAR_FRACTIONAL_CHAIN_FACTOR_20260801.md`
uses the physically correct resources:

* one chain of at most `d` strict-lower targets below each rank-`r` owner;
* one unanchored boundary chain of capacity `i` for every `1<=i<=d`.

This note proves the following sharpening of the integral frontier.

1. The Ferrers **rank inventory rounds integrally with zero loss**.  The
   boundary rank rows can even be realized by pairwise-disjoint literal
   Boolean chains.  Therefore rank counts and scalar capacity are not the
   integral obstruction.
2. Every single-family chain-height/Hall inequality is already implied by
   the fractional theorem.  Such cuts cannot prove a positive integral
   defect.
3. Greene--Kleitman saturation cannot supply the missing rounding.  For
   every `d>=2` there is a finite poset with the same triangular resource
   vector which has an exact fractional factor and a chain partition
   simultaneously saturated for **every** Greene--Kleitman norm, but whose
   exact integral triangular defect is

   \[
                         \binom{d+1}{2}-d
                         =\frac{d(d-1)}2.
   \]

4. Starting from a stronger anchored `(d+1)`-factor, the exact absorber
   needed at the true geometry is a transversal of the long owner chains
   which is itself packable into boundary chains of capacities `1,...,d`.
   This is a correlation condition, not a cardinality condition.

The surviving Boolean theorem is therefore a flag-exchange/representative
absorber.  The stronger anchored `D=ceil(Lambda/W)` factor remains a useful
uniform-chain starting point, but is not substituted for the triangular
target: it directly suffices when `D=d`, while for `D=d+1` it must also pass
the representative absorber of Theorem 4.1.

## 1. Exact integral triangular object

For each rank-`r` owner `T`, choose an inclusion chain

\[
 C_T\subseteq\{S:\varnothing\ne S\subsetneq T\},
 \qquad |C_T|\le d.
\]

For each boundary address `i in [d]`, choose an arbitrary inclusion chain

\[
                         B_i\subseteq\mathcal L,
                         \qquad |B_i|\le i.
\]

All selected target sets must be pairwise disjoint.  The triangular
deficiency is

\[
 \Gamma_d^\triangle
 =\Lambda-\max\left|\bigcup_T C_T\;\cup\;\bigcup_{i=1}^d B_i\right|.
                                                               \tag{1.1}
\]

The new fractional theorem says exactly that the LP relaxation of (1.1)
has value zero.  This is sharper than the anchored-only depth-`D` model.

## 2. The Ferrers rank ledger rounds exactly

Write `a_s=binom(k,s)` for `1<=s<r`.  Choose the `h` cells of the triangular
Ferrers board used in the fractional theorem.  Let

\[
 R_i\subseteq[i],\qquad |R_i|\le i,
 \qquad b_s=|\{i:s\in R_i\}|.                       \tag{2.1}
\]

Thus the boundary bank asks for one target of rank `s` at each address
with `s in R_i`, and the anchored owners must carry

\[
                         a'_s=a_s-b_s               \tag{2.2}
\]

rank-`s` targets.

### Theorem 2.1 (zero-defect rank scheduling)

There is a `0`--`1` matrix `M=(M_(T,s))`, indexed by rank-`r` owners and
strict-lower ranks, such that

\[
 \sum_T M_{T,s}=a'_s,
 \qquad \sum_s M_{T,s}\le d.                        \tag{2.3}
\]

Moreover, the boundary rank sets `R_i` have pairwise target-disjoint
literal Boolean-chain representatives.

#### Proof

For every `s<r`, binomial unimodality gives

\[
                         0\le a'_s\le a_s\le W.
\]

Also

\[
 \sum_s a'_s=\Lambda-h=\min(\Lambda,dW)\le dW.      \tag{2.4}
\]

Consider the complete bipartite flow network from rank labels `s` to the
`W` owner addresses, with unit capacity on every rank--owner edge and owner
capacity `d`.  For a set `J` of rank labels,

\[
 \sum_{s\in J}a'_s
 \le
 \begin{cases}
     |J|W,&|J|<d,\\
     dW,&|J|\ge d.
   \end{cases}                                      \tag{2.5}
\]

These are precisely the max-flow cuts.  Integral max flow gives (2.3).

For the boundary rows, choose one ordering
`pi=(pi_1,...,pi_k)`.  At address `i` and rank `s in R_i`, use the suffix

\[
                         \{\pi_{i-s+1},\ldots,\pi_i\}.
\]

For fixed `i` these sets form one chain.  Two selected sets of different
ranks have different cardinalities; two of the same rank have distinct
right endpoints and hence are distinct.  Thus all boundary targets are
distinct.  In fact these `d` chains are suffix rows of one literal source
prefix and already satisfy the sliding cocycle.  \(\square\)

The theorem deliberately stops at rank labels.  For every owner `T`, the
selected ranks in (2.3) must still be realized by one flag inside `T`, and
all those flags must partition the particular residual target sets left by
the boundary chains.  This is an ordered-slice hypergraph matching, not the
flow used above.

There is a complementary target-level strengthening of the same TU
relaxation.

### Theorem 2.2 (zero-defect rank-separated containment assignment)

Every target in `mathcal L` can be assigned either to a containing owner or
to one boundary address so that:

* an owner receives at most `d` targets and no two have the same rank;
* address `i` receives at most `i` targets and only ranks in `R_i`, again at
  most one of each rank.

#### Proof

Use a flow network with one unit at every target `S`.  A rank-`s` target is
adjacent to slot `(T,s)` whenever `S subset T`, and to boundary slot
`(partial_i,s)` whenever `s in R_i`.  Every slot has capacity one; the slots
at one owner feed a capacity-`d` node, and those at address `i` feed a
capacity-`i` node.

There is a fractional full flow.  Send `1/a_s` from each rank-`s` target to
each of its `b_s` boundary slots.  Distribute its remaining
`1-b_s/a_s` uniformly among its containing rank-`r` owners.  The load at a
boundary slot is one.  The load at every owner-rank slot is

\[
 \binom rs\frac{1-b_s/a_s}{\binom{k-s}{r-s}}
 =\frac{a_s-b_s}{W}\le1,                            \tag{2.6}
\]

using
`a_s binom(k-s,r-s)=W binom(r,s)`.  The total owner load is
`(Lambda-h)/W<=d`.  Integral max flow now gives the claimed assignment.
\(\square\)

Theorems 2.1 and 2.2 are two exact projections, not a hidden solution.
Theorem 2.1 makes the boundary selections into literal chains but only
rounds rank counts.  Theorem 2.2 assigns the actual targets with containment
but does not make the different ranks at one address comparable.  Coupling
those two properties is precisely the chain-atom correlation gate.

An exact local move is available: swapping positions `s,s+1` in an owner
ordering changes only its rank-`s` prefix and preserves every other prefix.
Thus Boolean sibling/Johnson-square moves are rank-pure potential absorber
edges.  What is not proved is a system of disjoint alternating routes which
uses those moves to remove every collision except `O(1)`.

## 3. The complete fractional dual passes; integer ceilings remain

For a family `F` in a poset, write `ht(F)` for the largest size of a chain
contained in `F`.  More generally, for nonnegative target weights `w`, put

\[
 H_c(w;X)=\max\left\{\sum_{S\in C}w_S:
      C\subseteq X\text{ is a chain},\ |C|\le c\right\}.        \tag{3.1}
\]

### Theorem 3.1 (exact weighted dual of the static marginal atom system)

The fractional triangular factor exists if and only if, for every
`w in R_+^mathcal L`,

\[
 \sum_{S\in\mathcal L}w_S
 \le \sum_T H_d(w;\mathcal L\cap2^T)
       +\sum_{i=1}^d H_i(w;\mathcal L).                         \tag{3.2}
\]

#### Proof

At each address take the convex hull of the incidence vectors of its legal
chains, including the empty chain.  The Minkowski sum `K` of these local
chain polytopes is exactly the set of total fractional coverage vectors.
Its support function at a nonnegative `w` is the right side of (3.2).
Therefore separation gives `1_mathcal L in K` exactly when (3.2) holds.

It is enough to use `w>=0`: every local polytope and hence `K` is
coordinatewise down-closed.  A separating vector with a negative entry may
have that entry replaced by zero; the support function is unchanged while
its value on `1_mathcal L` only increases.  \(\square\)

This is the complete dual after the boundary addresses are projected to
their individual chain marginals.  It does not characterize the smaller
physical polytope in which all addresses and owner traces must come from one
common source chronology.  The authoritative fractional construction does
belong to that correlated face, and Theorem 2.1 preserves its boundary
prefix, but integral owner coupling/serialization remains separate.

Taking `w=1_F` gives the ordinary family-height row.  Namely, for every
`F subseteq mathcal L`, every integral triangular selection satisfies

\[
 |F\cap\text{covered}|
 \le
 \sum_{T\in\binom{[k]}r}
   \min\!\left(d,\operatorname{ht}(F\cap 2^T)\right)
 +\sum_{i=1}^d\min\!\left(i,\operatorname{ht}(F)\right).       \tag{3.3}
\]

### Corollary 3.2 (fractional domination of every height cut)

For every `F subseteq mathcal L`,

\[
 |F|\le
 \sum_T\min\!\left(d,\operatorname{ht}(F\cap2^T)\right)
 +\sum_{i=1}^d\min\!\left(i,\operatorname{ht}(F)\right).       \tag{3.4}
\]

#### Proof

Use Theorem 3.1 with `w=1_F`; then
`H_c(1_F;X)=min(c,ht(F cap X))`.  \(\square\)

Consequently no positive defect can be certified by any ordinary weighted
fractional/Farkas row, not merely by rank counts or indicator heights.  An
integral strengthening does survive.  If the induced comparability graph
of a target family `F` has components `F_1,...,F_m`, then every selected
chain meets at most one component, so exact integral coverage necessarily
satisfies

\[
             \sum_{j=1}^m\left\lceil\frac{|F_j|}{d}\right\rceil
             \le W+d.                                           \tag{3.5}
\]

One may replace each ceiling by the exact minimum number of chains of size
at most `d` covering `F_j`.  These are configuration/component-ceiling
cuts; they are nonlinear integer strengthenings invisible to the exact LP.

## 4. Exact representative-absorber reduction

Let `D=ceil(Lambda/W)`.  The only nontrivial comparison with the stronger
uniform subclass is `D=d+1`; if `D=d`, an exact anchored `D`-factor is
already a zero-defect triangular selection with empty boundary chains.

Assume `D=d+1` and suppose an exact anchored `(d+1)`-factor
`A={A_T}` is supplied.  Put

\[
                         \mathcal H=\{T:|A_T|=d+1\}.             \tag{4.1}
\]

### Theorem 4.1 (long-chain representative absorber)

Choose one representative `x_T in A_T` for every `T in mathcal H`.  If all
but `c` of these representatives can be partitioned into chains

\[
                         X_1,\ldots,X_d,
                         \qquad |X_i|\le i,                      \tag{4.2}
\]

then

\[
                         \Gamma_d^\triangle\le c.               \tag{4.3}
\]

#### Proof

Delete `x_T` from every long owner chain.  The anchored chains now all have
size at most `d`.  Install the chains `X_i` at the boundary addresses, and
leave the `c` unused representatives uncovered.  All other targets retain
their old, disjoint owner assignment.  \(\square\)

This gives the exact bounded-absorber target.  It is not enough that the
boundary bank has enough scalar cells.  Indeed, when
`Lambda=dW+h`, define the underfill

\[
 z=\sum_{T\notin\mathcal H}(d-|A_T|).
\]

Counting the factor gives

\[
                         |\mathcal H|=h+z.                       \tag{4.4}
\]

The scalar condition for (4.2) is only

\[
 h+z-c\le\binom{d+1}{2}.                           \tag{4.5}
\]

It says nothing about comparability among the chosen representatives.  The
next section shows that this missing correlation can cost order `d^2` even
when (4.5) is an equality.

## 5. A sharp generic-poset no-go

### Theorem 5.1 (fractional exactness plus all-norm saturation does not round)

For every `d>=2`, there is a finite anchored poset instance with

\[
 W=\binom{d+1}{2}
\]

owners, anchored capacity `d`, and boundary capacities `1,...,d` such that:

1. its triangular LP has deficiency zero;
2. its natural chain partition is Greene--Kleitman `t`-saturated for every
   `t` simultaneously;
3. its exact integral triangular deficiency is

   \[
                         W-d=\frac{d(d-1)}2.                      \tag{5.1}
   \]

#### Construction and proof

Let the lower poset be the disjoint union of `W` chains

\[
 L_j=(\ell_{j,1}<\cdots<\ell_{j,d+1}),\qquad 1\le j\le W,
\]

with elements from different `L_j` incomparable.  Add `W` incomparable
owner elements, each above every lower element.  Thus every lower chain is
legal at every owner.

For the fractional factor, an anchored address chooses `j` uniformly and
then a uniformly random `d`-subset of `L_j`.  A boundary address of capacity
`i` chooses `j` uniformly and a uniformly random `i`-subset of `L_j`.  A
fixed lower target receives load

\[
 W\frac{d}{W(d+1)}
 +\sum_{i=1}^d\frac{i}{W(d+1)}
 =\frac d{d+1}+\frac{\binom{d+1}{2}}{W(d+1)}=1.       \tag{5.2}
\]

Hence the triangular LP is exact.

Integrally, one selected atom lies in only one component `L_j`.  Covering
all `d+1` targets of one component needs at least two atoms.  There are only
`W+d` addresses, rather than `2W`.  More precisely, assign one anchored
`d`-chain to every component; the `d` boundary atoms can cover the one
remaining target in only `d` components.  This attains defect `W-d`.
Conversely, distributing `W+d` atoms among `W` components covers at most
`dW+d` targets.  If component `j` receives `n_j` atoms, then its coverage is
at most

\[
 \min(dn_j,d+1)
 \le d\,\mathbf 1_{n_j\ge1}+\mathbf 1_{n_j\ge2}.
\]

If `n_1` is the number of nonempty components and `n_2` the number receiving
at least two atoms, then `n_1<=W` and
`n_2<=(W+d)-n_1`.  Therefore total coverage is at most

\[
 dn_1+n_2\le(d-1)n_1+W+d\le dW+d.
\]

Thus (5.1) is exact.

Finally, the lower poset is graded into `d+1` antichains of size `W`, and
its partition into the `W` chains `L_j` has

\[
 \sum_j\min(t,|L_j|)=W\min(t,d+1).
\]

This equals the maximum size of a union of `t` antichains, so the same
partition is `t`-saturated for every `t`.  Adding one distinct owner to each
chain preserves the statement with `d+2` in place of `d+1`.  \(\square\)

This is not a Boolean-lattice counterexample: its comparability graph has
`W` separated lower components, while the Boolean lower ideal has abundant
cross-rank exchanges.  Its purpose is exact.  No theorem using only
fractional triangular feasibility, the capacity vector, and generic
Greene--Kleitman saturation can imply an `O(1)` rounding.  It does not rule
out a theorem exploiting the specific binomial rank profile.  Such a
positive proof must use that profile or, more structurally, the Boolean
exchange geometry to route representatives between the separated
long-chain roles.

## 6. Consequence and surviving gate

The strongest statements established here are

\[
\boxed{
\begin{array}{c}
\text{triangular fractional target: exact;}\\
\text{rank/Ferrers schedule: exact integrally;}\\
\text{one-family height cuts: all satisfied;}\\
\text{general-poset integral rounding: false by }\Theta(d^2);\\
\text{Boolean flag/representative absorber: open.}
\end{array}}
\]

An `O(1)` Boolean theorem can be pursued in either of two working forms; the
second is a stronger sufficient subclass, not an equivalent reformulation:

* choose the owner flags jointly so that only `O(1)` residual targets remain
  after the triangular boundary chains; or
* in the stronger `(d+1)` subclass, rechain until representatives of all
  but `O(1)` long owner chains satisfy (4.2).

The adjacent-prefix swap is the smallest Boolean actuator, but a disjoint
alternating-route/absorber theorem for it is not presently proved.  Even a
static success would still precede the independent sliding-OR
serialization, upper-shadow, residence, and common-cap gates.

## References used for scope

* C. Greene and D. J. Kleitman, the saturation/min--max theory for unions of
  antichains and chain norms.
* H. Shum and L. E. Trotter, *Cardinality-restricted chains and antichains
  in partially ordered sets*, Discrete Applied Mathematics 65 (1996),
  421--439.  The general cardinality-restricted chain-cover problem is
  NP-complete.
* B. Sudakov, I. Tomon and A. Z. Wagner, *Uniform chain decompositions and
  applications*, Random Structures & Algorithms 60 (2022), 261--286.  Its
  upper-half construction yields the sublinear-defect Boolean rounding
  recorded separately in
  `MATH_THEOREM_TRIANGULAR_CHAIN_DEFICIENCY_STW_ROUNDING_AND_GK_BARRIER_20260801.md`.
