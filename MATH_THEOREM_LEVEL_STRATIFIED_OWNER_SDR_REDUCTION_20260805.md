# The owner-bundle packing is a backward sequence of ordinary SDRs

**Date:** 2026-08-05  
**Method:** exact FIFO inversion and Hall's theorem; no computation or search  
**Status:** unconditional structural reduction.  After the penultimate and
terminal owners of the selected copies are fixed, the remaining owner-bundle
problem is not a growing-uniformity hypergraph matching.  It is exactly a
sequence of `d-1` bipartite left-perfect matchings.  The last backward level
is the unique balanced bottleneck; every earlier level has linearly growing
right-side slack.  What remains open is to construct the last-two assignment
so that all these ordinary Hall systems hold simultaneously.

## 1. One copy, read backward

Fix a fresh lower block

\[
 S_j=C\cup\{a_{j+1},\ldots,a_d\}
          \cup\{b_1,\ldots,b_j\},\qquad 0\le j<d,     \tag{1.1}
\]

and put

\[
 R=S_0\cup\{b_1,\ldots,b_{d-1}\},\qquad |R|=r-1.    \tag{1.2}
\]

For one punctured copy, choose distinct coordinates

\[
                         x_1,\ldots,x_d,u\in[k]\setminus R.  \tag{1.3}
\]

Its owners are

\[
 \begin{aligned}
 T_j&=S_0\cup\{b_1,\ldots,b_j\}
              \cup\{x_{j+1},\ldots,x_d\},&&0\le j<d,\\
 T_d&=R\cup\{u\}.                                            \tag{1.4}
 \end{aligned}
\]

In particular,

\[
                         T_{d-1}=R\cup\{x_d\}.               \tag{1.5}
\]

For \(0\le j\le d-2\), equation (1.4) is equivalent to the backward
recurrence

\[
 \boxed{
                         T_j=T_{j+1}-\{b_{j+1}\}+\{x_{j+1}\}.}
 \tag{1.6}
\]

Once `T_(j+1)` is known, the new coordinate `x_(j+1)` is the unique element
of `T_j-T_(j+1)`.

## 2. The level graph

Let `I` be a labelled family of requested copies.  Several copies may come
from the same lower block.  Assume their owners at levels `j+1,...,d` have
already been chosen and are pairwise distinct globally.

For a copy `i`, write `R_i` for its hull, write `u_i` for its already fixed
terminal coordinate, and put

\[
 Z_i^{>j+1}=\{u_i,x_{j+2}^i,\ldots,x_d^i\}.                   \tag{2.1}
\]

These coordinates are already determined by the later owner levels.  Let

\[
 F_j=\{T_\ell^i:i\in I, j+1\le\ell\le d\}                   \tag{2.2}
\]

be the owners already occupied.

Define the bipartite **level graph** `G_j` as follows.  Its left shore is
`I`; its right shore is \(\mathcal R-F_j\), where
\(\mathcal R={ [k]\choose r}\).  Join copy `i` to owner `T` when

\[
 T=T_{j+1}^i-\{b_{j+1}^i\}+\{x\}                             \tag{2.3}
\]

for some

\[
 x\in[k]\setminus\bigl(R_i\cup Z_i^{>j+1}\bigr).            \tag{2.4}
\]

Before deleting `F_j`, every left degree is exactly

\[
                         q-(d-j),\qquad q=k-r+1.              \tag{2.5}
\]

Indeed `[k]-R_i` has size `q`, and precisely `d-j-1` later queue labels plus
the terminal coordinate have already been used.

## 3. Exact sequential-SDR theorem

### Theorem 3.1 (backward owner factorization)

Fix the lower blocks, their multiplicities, and pairwise distinct owners at
levels `d-1` and `d`.  The following are equivalent.

1. All copies extend to complete FIFO owner paths (1.4), and every owner
   used by every copy is globally distinct.
2. Starting with `j=d-2` and descending to `j=0`, the level graph `G_j`
   has a matching saturating its left shore after the choices at later
   levels have been fixed.

Equivalently, at every level one needs exactly the ordinary Hall system

\[
 \boxed{
                         |N_{G_j}(J)|\ge|J|
                         \qquad(J\subseteq I).}              \tag{3.1}
\]

#### Proof

Suppose first that the complete owner paths exist.  At level `j`, match copy
`i` to its owner `T_j^i`.  Formula (1.6) and freshness (1.3) put this edge
in `G_j`.  Global owner distinctness makes it a left-perfect matching.

Conversely, begin with the fixed last two levels.  Let a left-perfect
matching of `G_(d-2)` choose `T_(d-2)^i` for every copy.  Equation (2.3)
defines one new coordinate `x_(d-1)^i`; (2.4) makes it fresh relative to the
hull and the later queue labels.  The right shore excludes `F_(d-2)`, so
the new owners are distinct from every later owner, and the matching makes
them distinct from one another.

Repeat at levels `d-3,...,0`.  Inductively, each step chooses the next fresh
queue coordinate, preserves (1.4), and introduces no owner collision.  At
the end all queue labels in (1.3) are distinct and every owner is unique.
Hall's theorem gives the equivalence with (3.1).  \(\square\)

This theorem retains all copy labels, so the terminal `Sym(h)` action within
each macro remains available after the SDRs have been installed.

## 4. A useful deterministic sufficient condition

For a level graph, put

\[
 \delta_j=\min_{i\in I}d_{G_j}(i),\qquad
 \Delta_j^R=\max_{T\in\mathcal R-F_j}d_{G_j}(T).             \tag{4.1}
\]

### Corollary 4.1 (degree-ratio Hall certificate)

If

\[
                         \delta_j\ge\Delta_j^R,              \tag{4.2}
\]

then `G_j` has a matching saturating `I`.

#### Proof

For every \(J\subseteq I\), count the edges from `J` to its neighbourhood in
two ways:

\[
 \delta_j|J|\le e(J,N(J))\le\Delta_j^R|N(J)|.               \tag{4.3}
\]

Condition (4.2) gives `|N(J)|>=|J|`, and Hall applies.  \(\square\)

The condition is only sufficient.  A pseudorandom sparse level graph may
have a perfect matching even when its maximum right degree is larger than
its minimum left degree.

## 5. The exact slack ledger

Let

\[
                         H=|I|,\qquad W=|\mathcal R|.       \tag{5.1}
\]

In the optimal scalar ledger,

\[
                         H=\left\lfloor{W\over d+1}\right\rfloor
                         +O(W/d^2),                           \tag{5.2}
\]

where the error allows the already budgeted discarded copies.  Immediately
before level `j` is assigned, the `d-j` later levels occupy `(d-j)H` owners.
Therefore the available right shore has size

\[
 \begin{aligned}
 |\mathcal R-F_j|
   &=W-(d-j)H\\
   &=(j+1)H+O(W/d).                                         \tag{5.3}
 \end{aligned}
\]

Thus the right-to-left size ratio at level `j` is

\[
                         j+1+O(1).                           \tag{5.4}
\]

More precisely, under a product-like distribution of the later owner
levels, a raw menu of size `q-O(d)` sees expected surviving degree

\[
 { |\mathcal R-F_j|\over W}\,(q-O(d))
                         =\Theta((j+1)d),                    \tag{5.5}
\]

because \(q=\Theta(d^2)\).

Consequently:

* `j=0` is the unique balanced SDR: both shores have size `H+O(W/d)` and
  the natural degree scale is \(\Theta(d)\);
* level `j` has expansion slack about `j+1` and natural degree
  \(\Theta((j+1)d)\); and
* no growing edge remains.  The required objects are ordinary bipartite
  matchings of diverging degree.

## 6. The sharpened open theorem

The internal-owner part of the connected macro-factor theorem is now
equivalent to the following statement.

> **Regenerating level-Hall theorem.**  Choose the last two owner slots of
> the punctured copies so that, after each backward matching is selected,
> all subsequent level graphs satisfy (3.1).  It is enough to prove this
> with `O(W/d^2)` discarded copies.

The hull alteration theorem supplies the last-two slots with the correct
capacity and loss provided its quadratic adjacency energy is controlled.
The remaining correlation is therefore precise: those injections must be
chosen so that the balanced graph `G_0`, and then the successively slacker
graphs `G_1,...,G_(d-2)`, retain Hall.

A proof may use random injections plus switchings, an all-cut expansion
estimate, or a small absorber.  What is no longer necessary is a black-box
matching theorem for hyperedges of size \(\Theta(d)\).

## 7. Dependencies

The punctured-copy formula and terminal `Sym(h)` switch are in

`MATH_THEOREM_FRESH_FIFO_BLOCK_CHAIN_KERNEL_AND_PAYLOAD_ATLAS_GATE_20260805.md`.

The last-two hull alteration is in

`MATH_THEOREM_OWNER_HULL_OBSTRUCTION_AND_TERMINAL_ALTERATION_20260805.md`.
