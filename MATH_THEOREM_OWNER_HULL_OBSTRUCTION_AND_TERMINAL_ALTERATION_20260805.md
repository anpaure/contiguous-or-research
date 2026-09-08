# Owner hulls: the exact terminal obstruction and a sparse-collision completion

**Date:** 2026-08-05  
**Method:** literal FIFO endpoint algebra, incidence double counting, an
adaptive binomial tail, and a random terminal alteration; no computation or
search  
**Status:** proof-safe reduction for the connected `2/3` macro-factor
programme.  An arbitrary fresh lower-path packing need not admit any owner
lift.  The obstruction is already visible in the last two owners of every
copy.  For a regenerative random nibble, however, the repeated-hull
obstruction has a superexponentially small tail.  Moreover, a single
quadratic adjacency-energy bound gives an injective assignment of both the
penultimate and terminal owners after deleting only `O(W/d^2)` copies.  The
still-open row is the simultaneous disjoint packing of the first `d-1`
internal owners of every retained copy.

## 1. The hull of a fresh lower block

Put

\[
 t=r-d,qquad \mathcal L={ [k]\choose t},qquad
 M=|\mathcal L|,qquad \mathcal R={ [k]\choose r}.
 \tag{1.1}
\]

Let

\[
 P=(S_0,S_1,\ldots,S_{d-1})                         \tag{1.2}
\]

be a fresh lower path.  Thus

\[
 S_j=S_{j-1}-a_j+b_j\qquad(1\le j<d),                \tag{1.3}
\]

and the `2(d-1)` event labels are distinct.  Its **hull** is

\[
 R(P)=\bigcup_{j=0}^{d-1}S_j
     =S_0\cup\{b_1,\ldots,b_{d-1}\}.                  \tag{1.4}
\]

It has rank `r-1`.

In the punctured duplicate lift, every copy of `P` has terminal owner

\[
                         R(P)\cup\{u\},qquad u\notin R(P).   \tag{1.5}
\]

Consequently the complete terminal menu of one block is the upper star of
its hull and has size

\[
                         q=k-r+1.                            \tag{1.6}
\]

This observation is independent of the queue bank and of its ordering.

The penultimate owner belongs to the same star:

\[
                         T_{d-1}=R(P)\cup\{x_d\}.             \tag{1.7}
\]

Thus one copy ultimately needs two distinct points of the hull star, one
for `x_d` and one for `u`.

## 2. Exact terminal Hall theorem

Let \(\mathcal B\) be any family of pairwise lower-vertex-disjoint fresh
blocks.  Assign a desired multiplicity \(h_P\in\{2,3\}\) to every block.
Make `h_P` labelled terminal clones of its hull.  Join a clone of `R` to the
rank-`r` owner `T` precisely when \(R\subset T\).

### Theorem 2.1 (terminal Hall criterion)

The terminal owners of all requested copies can be chosen pairwise distinct
if and only if, for every subfamily `F` of hulls,

\[
 \boxed{
 \sum_{R\in F}h_R
       \le\left|\bigcup_{R\in F}\{T\in\mathcal R:R\subset T\}\right|.}
 \tag{2.1}
\]

Here repeated occurrences of the same hull are combined in `h_R`.

#### Proof

This is Hall's theorem applied to the bipartite graph of terminal clones and
rank-`r` owners.  Clones of the same hull have the same neighbourhood, so a
Hall shore may be enlarged to contain either all or none of those clones.
The resulting inequalities are exactly (2.1).  \(\square\)

In particular,

\[
                         h_R\le q                            \tag{2.2}
\]

is necessary for every single hull.  It is not sufficient: distinct
rank-`r-1` hulls may have overlapping upper stars.  Thus a maximum hull-load
bound is a local prerequisite, not a substitute for (2.1).

## 3. Why an arbitrary lower packing is not enough

### Proposition 3.1 (one-hull obstruction)

For all sufficiently large central parameters, there is a family of more
than `q/2` pairwise vertex-disjoint fresh `d`-paths having one common hull
`R`.  No `2/3` lift of that family exists, because its terminal demand is
larger than `q`.

#### Proof

Fix a rank-`r-1` set `R`.  The number of oriented fresh paths with hull `R`
is

\[
                         N_R=(r-1)_{d-1}(t)_{d-1}.            \tag{3.1}
\]

Indeed, first order the `d-1` elements of `R-S_0`, and then order the
`d-1` deleted elements of `S_0`.  Conversely these two orders reconstruct
the path.

The number of rank-`t` vertices inside `R` is

\[
                         K_R={r-1\choose t}={r-1\choose d-1}. \tag{3.2}
\]

By symmetry, a fixed such vertex belongs to exactly `d N_R/K_R` oriented
paths.  Hence a forbidden set of `f` lower vertices meets at most

\[
                         {f d\over K_R}N_R                   \tag{3.3}
\]

paths.  Greedily select paths.  Before selecting the `(m+1)`-st path, fewer
than `md` lower vertices are forbidden.  A new path therefore exists while

\[
                         {m d^2\over K_R}<1.                 \tag{3.4}
\]

In the central range, `K_R` grows faster than every polynomial in `k`, while
\(q=\Theta(k)\) and \(d=\Theta(\sqrt{k})\).  Thus (3.4) holds for
`m=q/2+1` once `k` is large.  This gives more than `q/2` vertex-disjoint
blocks with hull `R`.

Every block requests at least two copies, but (1.6) supplies only `q`
different terminal owners.  Inequality (2.2), or directly the pigeonhole
principle, rules out the lift.  \(\square\)

Therefore the uncoloured fresh-path packing theorem must be strengthened by
a hull-balanced nibble, or lower blocks and owner bundles must be selected
jointly.  This is a real quantifier issue, not a cosmetic choice of queues.

## 4. Exact path degree per hull

Let \(\mathcal H\) be the labelled fresh-path hypergraph on the rank-`t`
layer.
Its vertex degree is

\[
                         D=d(t)_{d-1}(k-t)_{d-1}.             \tag{4.1}
\]

Let

\[
                         H_-={k\choose r-1}                  \tag{4.2}
\]

be the number of hulls.  Every hull supports the same number `P` of labelled
paths.  Double counting path--lower-vertex and path--hull incidences gives

\[
 \boxed{
                         {P\over D}={M\over dH_-}.}           \tag{4.3}
\]

For the optimal central parameters \(H_-/M=\Theta(1)\), so

\[
                         P/D=Theta(1/d).                     \tag{4.4}
\]

Equation (4.3), rather than only a maximum-codegree estimate, is the scale
which makes repeated hulls harmless in a balanced nibble.

## 5. Hull loads in a regenerative nibble

The next lemma is deliberately conditional only on the exact one-step
tracking rows which a direct nibble must prove anyway.  It shows that hull
capacity is not an additional asymptotic obstruction.

Consider nibble rounds indexed by `i`.  Let `rho_i` be the current lower
vertex density.  Assume

\[
 1/d\le\rho_i\le1,qquad
 D_i\ge(1-\eta)D\rho_i^{d-1},qquad
 P_i(R)\le(1+\eta)P\rho_i^d                         \tag{5.1}
\]

for every surviving lower vertex and every hull `R`, where `eta=o(1)`.
In round `i`, independently mark each surviving labelled path with
probability at most

\[
                         p_i={\gamma\over dD_i},              \tag{5.2}
\]

where `gamma>0` is fixed.  Suppose also that

\[
                         \rho_{i+1}\le(1-c/d)\rho_i           \tag{5.3}
\]

until density `1/d`, for a fixed `c>0`.

### Lemma 5.1 (superexponential hull-cap tail)

Let `Y_R` be the total number of marked paths with hull `R` over all rounds.
Then its predictable mean is at most `C/d`, and for every integer \(L\ge1\),

\[
                         Pr(Y_R\ge L)
             \le\left({eC\over dL}\right)^L.                \tag{5.4}
\]

Consequently, with

\[
                         L=\left\lfloor {q\over6}\right\rfloor,
 \tag{5.5}
\]

the probability that any of the `H_-` hulls reaches load `L` is `o(1)`.

#### Proof

Conditional on the past, (4.3), (5.1), and (5.2) give

\[
 \begin{aligned}
 E(\hbox{new marks of hull }R\mid\mathcal F_i)
 &\le { (1+\eta)P\rho_i^d\gamma
          \over d(1-\eta)D\rho_i^{d-1}}\\
 &\le {C\rho_i\over d^2}.                                  \tag{5.6}
 \end{aligned}
\]

The geometric decay (5.3) gives

\[
                         \sum_i\rho_i\le C'd,                \tag{5.7}
\]

so the total predictable mean is at most `C/d`.

For completeness, the adaptive binomial bound follows from the exponential
supermartingale.  If \(X_s\in\{0,1\}\) are the successive mark indicators and
their conditional probabilities have sum at most `mu`, then

\[
 E\exp\!\left(\theta\sum_sX_s\right)
 \le\exp(\mu(e^\theta-1)).                                  \tag{5.8}
\]

Markov's inequality, optimized at `e^theta=L/mu`, gives
\(\Pr(\sum_sX_s\ge L)\le(e\mu/L)^L\).  This proves (5.4).

Now \(q=\Theta(k)=\Theta(d^2)\).  Hence the logarithm of the right side of
(5.4) at (5.5) is \(-\Theta(d^2\log d)\), whereas

\[
                         \log H_-=Theta(k)=Theta(d^2).        \tag{5.9}
\]

A union bound over all hulls tends to zero.  Accepted paths are a subset of
marked paths, so the same cap holds for the actual packing.  \(\square\)

Thus any successful regenerative nibble may impose the hull cap (5.5)
without changing its asymptotic bite rate.  Since every block has at most
three copies, this cap guarantees at most `q/2` copies and hence at most `q`
last-two owner slots in one hull star.

## 6. Sparse-collision completion of the last two owner levels

After assigning multiplicities, let \(c_R\in\{0,2,3,4,\ldots\}\) be the
number of requested copies whose block hull is `R`.  Assume \(2c_R\le q\).
For a rank-`r`
owner `T`, its `r` facets are the rank-`r-1` sets contained in `T`.  Define
the **cross-hull adjacency energy**

\[
 \mathcal A(c)=
   \sum_{T\in\mathcal R}
   \sum_{\substack{R,R'\subset T\\ |R|=|R'|=r-1,\ R<R'}}
                         c_Rc_{R'}.                           \tag{6.1}
\]

Two distinct hulls have a common terminal owner if and only if they are two
facets of one rank-`r` set, and then that common owner is unique.

### Theorem 6.1 (penultimate--terminal alteration)

There are pairwise distinct penultimate and terminal owners for all but at
most

\[
                         {4\mathcal A(c)\over q^2}            \tag{6.2}
\]

requested copies.  In particular, if

\[
                         \mathcal A(c)=O(Wd^2),               \tag{6.3}
\]

then only `O(W/d^2)` copies need be discarded.

#### Proof

For each hull `R`, make two labelled slots for every copy, called its
penultimate and terminal slots.  Choose a uniformly random injection from
these `2c_R` slots into the `q` upper neighbours of `R`.  Make these
injections independently for distinct hulls.  Slots belonging to the same
hull never collide, and the two slots of one copy are automatically
different.  Interpret their two added coordinates as `x_d` and `u`.

Slots belonging to two distinct hulls can collide only when the hulls are
facets of one common owner `T`.  For each ordered pair of slots on such a
pair of hulls, the probability that both choose `T` is `1/q^2`.  There are
`4c_Rc_(R')` cross-slot pairs over hulls `R,R'`.  Therefore the expected
number of colliding unordered slot pairs is exactly

\[
                         4\mathcal A(c)/q^2.                  \tag{6.4}
\]

Choose an outcome no worse than its expectation.  From every colliding pair
delete the copy owning one endpoint, continuing until no collision remains.
The number of deleted copies is at most the original number of colliding
slot pairs, proving (6.2).

Under central scaling, \(q=\Theta(d^2)\).  Substitution of (6.3) into (6.2)
gives `O(W/d^2)`.  \(\square\)

Deleting `O(W/d^2)` copies loses only `O(W/d)` duplicate lower positions,
because one copy carries `d` such positions.  This is exactly the separator
scale already present in the scalar ledger.

For a product-density \(\Theta(1/d)\) sample of hull copies, a fixed owner
sees \(\Theta(r/d)=\Theta(d)\) selected facets, so (6.3) is the natural quadratic
scale.  Proving that the actual macro nibble retains this energy is a
tracking problem, not a new Hall or capacity phenomenon.

## 7. Sharpened remaining theorem

The owner-bundle gate can now be stated without hiding the terminal issue.
It is enough to construct a regenerative joint nibble which:

1. covers all but `O(M/d)` lower vertices by fresh blocks;
2. assigns multiplicity two or three with the scalar total from the
   `2/3` ledger;
3. chooses the `d` internal owners of every retained copy pairwise
   distinctly;
4. satisfies the degree and hull-count tracking (5.1)--(5.3); and
5. leaves cross-hull energy \(\mathcal A=O(Wd^2)\).

Lemma 5.1 then supplies the exact per-hull capacity, and Theorem 6.1 installs
the last two owners of all but `O(W/d^2)` copies.  The terminal `Sym(h)`
switches remain available afterward to merge components whenever the macro
component graph is connected.

The only substantive integral row not reduced here is the disjoint selection
of levels `0,...,d-2` in item 3, together with the regenerative tracking
needed to iterate its isolated bites.  In particular, neither a maximum
hull-load estimate nor ordinary terminal Hall alone proves the connected
integral macro factor.

## 8. Dependencies

The punctured duplicate lift and terminal switches are in

`MATH_THEOREM_FRESH_FIFO_BLOCK_CHAIN_KERNEL_AND_PAYLOAD_ATLAS_GATE_20260805.md`.

The uncoloured `O(M/d)` fresh-path packing and the product-residual
all-order codegrees are in

`MATH_THEOREM_FRESH_JOHNSON_PATH_PACKING_AND_ALL_ORDER_RESIDUAL_20260805.md`.
