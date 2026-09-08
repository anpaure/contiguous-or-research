# MSW gives the mixed monotone-block factor; only cross-component seams remain

**Date:** 2026-08-13  
**Status:** unconditional asymptotic theorem for odd ground size.  It solves
the owner-perfect, globally lower-injective, mixed-(q,q+1) monotone-block
packing problem without a hypergraph nibble.  Within every MSW component,
the omitted lower tickets reconnect the blocks in a (q)-biresident cycle.
It does not join different MSW components or repair the known noncanonical
upper-deck defect.

## 1. Parameters and the exact MSW factor

Put

\[
 k=2R-1,\qquad W={k\choose R},\qquad
 \Lambda=\sum_{j<R}{k\choose j}=2^{k-1},              \tag{1.1}
\]

and let

\[
 d=\min\left\{t\in\mathbb Z_{\ge0}:
        tW+{t+1\choose2}\ge\Lambda\right\},\qquad q=d+1. \tag{1.2}
\]

[The Mütze--Standke--Wiechert (MSW) cycle factor](https://arxiv.org/abs/1603.02525)
partitions the rank-`(R-1)`
layer into cyclic `(R-1)`-window decks on cyclic orders of `[k]`.
Complementing each
deck gives the corresponding cyclic rank-`R` owner deck.  Equivalently,
on one cyclic order `x_0,\ldots,x_{k-1}`, write

\[
 T_i=\{x_i,x_{i+1},\ldots,x_{i+R-1}\},
 \qquad i\in\mathbb Z_k.                              \tag{1.3}
\]

Across all wreaths, the `T_i` partition every rank-`R` owner and the
edge intersections

\[
 T_i\cap T_{i+1}
   =\{x_{i+1},\ldots,x_{i+R-1}\}                     \tag{1.4}
\]

partition every rank-`(R-1)` lower colour.

## 2. Eventual arithmetic

### Lemma 2.1

For every `R>=16`,

\[
 2\le q\le R-1,
 \qquad k=2R-1\ge q(q-1).                             \tag{2.1}
\]

Consequently there are nonnegative integers `a,b` with

\[
                         k=aq+b(q+1).                 \tag{2.2}
\]

#### Proof

The standard central-binomial bound

\[
 {2R\choose R}\ge{4^R\over2\sqrt R}
\]

and `W=\frac12{2R\choose R}` give

\[
 {\Lambda\over W}\le\sqrt R.                       \tag{2.3}
\]

Since the nonnegative triangular term in (1.2) can only lower the first
successful integer,

\[
 d\le\left\lceil{\Lambda\over W}\right\rceil,
 \qquad q\le\sqrt R+2.                               \tag{2.4}
\]

For `R>=16`,

\[
 q(q-1)\le(\sqrt R+2)(\sqrt R+1)
          =R+3\sqrt R+2\le2R-1,                     \tag{2.5}
\]

and `q<=R-1`; also `q>=2` directly from (1.2).  Finally, `q` and `q+1` are
coprime and their Frobenius number is

\[
 q(q+1)-q-(q+1)=q(q-1)-1.                            \tag{2.6}
\]

Thus (2.2) follows from (2.1).  \(\square\)

The theorem below also holds for any particular parameters satisfying
`q\le R-1` and (2.2), independently of how `q` was chosen.

## 3. Exact mixed block factor

### Theorem 3.1

Cut every cyclic owner deck (1.3) into `a` consecutive blocks of `q`
owners and `b` consecutive blocks of `q+1` owners, in any cyclic order
realizing (2.2).  Then:

1. every block is a monotone exchange path;
2. the blocks partition the owner layer;
3. all internal lower colours of all blocks are globally distinct;
4. the unused lower colours are exactly the original MSW edges at the
   block cuts;
5. reconnecting each block to its cyclic successor with that original
   cut edge recovers the MSW cycle, and every resulting component is
   `q`-biresident.

#### Proof

The transition `T_i\to T_{i+1}` deletes `x_i` and inserts
`x_{i+R}`.  In a block of `s\in\{q,q+1\}` owners there are `s-1\le q`
transitions.  Because `q\le R-1`, the deletion labels

\[
 x_i,\ldots,x_{i+s-2}
\]

and insertion labels

\[
 x_{i+R},\ldots,x_{i+R+s-2}
\]

are separately distinct and mutually disjoint on the cycle of length
(2R-1).  Hence the block has exactly the monotone form obtained by
successively deleting pairwise distinct old labels and inserting
pairwise distinct new labels.

The blocks are a vertex partition of each MSW cycle, and the wreaths
partition the owner layer, proving Item 2.  Their internal edges are a
subset of the globally exact MSW lower ledger (1.4), proving Item 3.
Deleting the cut edges from disjoint cycles leaves precisely those lower
colours unused, proving Item 4.  Restoring each deleted edge recovers the
original factor.

Finally, a coordinate occurs in exactly `R` consecutive owners of
(1.3) and is absent for the other `R-1`.  Both cyclic run lengths are at
least `q`, so the recovered components are `q`-biresident.  \(\square\)

## 4. Exact consequence for the monotone-block programme

Let a mixed augmented hypergraph have one resource edge for every
monotone block, consisting of its owner support together with its internal
lower colours.  Theorem 3.1 gives explicitly an owner-perfect matching in
this mixed `q/(q+1)` host, and the original MSW cut edges give a rainbow
legal seam cycle on the blocks belonging to each wreath.

Therefore none of the following is an open problem in the odd case:

* owner-perfect mixed monotone-block packing;
* global injectivity of internal lower colours;
* the one-missing-colour-per-block ledger; or
* residence-compatible joining of blocks inside one wreath.

The remaining seam problem is strictly the **cross-wreath** problem:
replace a collection of original cut edges by palette-compatible seams
which join the wreath cycles, while retaining (q)-residence and the
required upper/source occurrence bank.  The canonical MSW factor's known
upper-deck holes remain unchanged by merely cutting and restoring its own
edges.  Thus the theorem removes the generic hypergraph matching gate but
does not solve the global compiler or one-cycle construction.
