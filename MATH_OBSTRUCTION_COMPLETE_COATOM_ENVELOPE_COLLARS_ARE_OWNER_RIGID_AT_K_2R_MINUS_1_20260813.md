# Complete coatom-envelope collars are positive-resident but owner-rigid at `k=2R-1`

**Date:** 2026-08-13  
**Status:** unconditional local collar theorem and exact owner-incidence
no-go for trades made only from complete collars.  Partial/open coatom
paths are not ruled out.

## 1. The complete collar

Let `Omega` have size `k`, let `T subseteq Omega` have size `R+1`, and
choose a cyclic order

\[
                         x_0,x_1,\ldots,x_R
\]

of the elements of `T`.  Put

\[
                         O_i=T\setminus\{x_i\}.
\]

Then

\[
                         O_0,O_1,\ldots,O_R,O_0       \tag{1.1}
\]

is a simple Johnson cycle on rank-`R` owners.  Every adjacent union is
exactly `T`, while its immediate-lower tickets are

\[
                         T\setminus\{x_i,x_{i+1}\}.  \tag{1.2}
\]

Thus the missing-label order identifies the lower ledger with the edge
set of a Hamilton cycle on `T`.

Every coordinate `x in T` is absent at exactly the one owner `T-x` and
present at all other `R` owners.  Its unique cyclic positive run therefore
has length `R` and its zero gap has length one.  Consequently a complete
coatom collar is positively `q`-resident for every `q<=R`, and every one
of its `R+1` upper-edge occurrences witnesses the same envelope target
`T`.

The repeated upper value means that this collar has upper **support**, not
a simple upper occurrence palette.  Its owner and lower palettes are
simple.

## 2. Owner-incidence rigidity

For each `(R+1)`-set `T`, let

\[
 c_T=\sum_{x\in T}\mathbf e_{T\setminus\{x\}}
       \in\mathbb Z^{\binom{\Omega}{R}}             \tag{2.1}
\]

be the owner vector of its complete collar.

### Theorem 2.1

Assume

\[
                         k=2R-1.                    \tag{2.2}
\]

Then the vectors `c_T`, over all `(R+1)`-sets `T`, are linearly
independent over `Q`.  Hence an old/new bank of complete coatom collars is
owner-exact,

\[
             \sum_T n_T^-c_T=\sum_T n_T^+c_T,       \tag{2.3}
\]

if and only if

\[
                         n_T^-=n_T^+\quad\hbox{for every }T. \tag{2.4}
\]

In particular, a nontrivial support trade that replaces one multiset of
envelope targets by another cannot be built solely from complete collars.

#### Proof

Let `W` be the matrix whose rows are rank-`R` owners, whose columns are
rank-`R+1` targets, and whose entry is one when the row owner is a coatom
of the column target.  Its column at `T` is `c_T`.

Complement rows and columns.  A row owner `O` becomes an `(R-1)`-set
`O^c`, a column target `T` becomes an `(R-2)`-set `T^c`, and

\[
                         O\subset T
       \quad\Longleftrightarrow\quad T^c\subset O^c. \tag{2.5}
\]

Thus `W`, up to row and column relabelling, is the inclusion matrix from
`(R-2)`-sets to `(R-1)`-sets on a `(2R-1)`-set.  The characteristic-zero
rank theorem for subset-inclusion matrices gives

\[
 \operatorname{rank}_{\mathbb Q}W
   =\min\left\{\binom{2R-1}{R-2},
                \binom{2R-1}{R-1}\right\}
   =\binom{2R-1}{R-2},                              \tag{2.6}
\]

which is the number of columns.  Hence the columns are independent.
Applying this to (2.3) proves (2.4).  \(\square\)

## 3. Exact remaining escape

One may reorder a fixed target's missing labels, changing its lower
Hamilton cycle while keeping its owner vector and upper support `T`.
Such reorders can be useful for topology or lower-ticket trades, but they
cannot change the envelope-target multiset.

To repair a genuinely missing target while retaining exact owners, one
must therefore use at least one ingredient outside the complete-collar
column family: for example partial/open coatom paths together with a
separate owner-balancing trade.  Positive residence is then no longer an
automatic consequence of the closed collar, because the two exterior
cuts can split the long positive arcs.  Those boundary runs and the exact
lower-ticket complement ledger are the next gates.
