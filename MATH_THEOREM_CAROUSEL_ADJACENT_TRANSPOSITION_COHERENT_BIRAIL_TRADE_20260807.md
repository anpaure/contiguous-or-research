# Adjacent carousel transpositions are coherent two-ray trades at every width

**Date:** 2026-08-07  
**Status:** unconditional local trade theorem.  Global availability of a
sequence of collision-free trades is not asserted.

## 1. Setup

Let \(Y\) be a cyclically ordered set of size \(M\).  Fix adjacent positions
containing labels \(x,y\), in that order, and let \(\sigma'\) be obtained from
\(\sigma\) by interchanging \(x,y\).

For \(1\le\ell<M\), let \(\mathcal I_\ell(\sigma)\) be the family of
\(\ell\)-element cyclic intervals in \(\sigma\).  If a fixed core \(C\) is
adjoined, put

\[
 \mathcal D_\ell(C,\sigma)
 =\{C\cup I:I\in\mathcal I_\ell(\sigma)\}.
\tag{1.1}
\]

Write \(L_{\ell-1}\) for the \(\ell-1\) labels immediately preceding \(x\),
and \(R_{\ell-1}\) for the \(\ell-1\) labels immediately following \(y\), in
the old order.  Since \(\ell<M\), neither ray contains the opposite active
label.

## 2. Exact all-width trade

### Theorem 2.1

For every \(1\le\ell<M\), the following is the exact signed
**occurrence-current** identity:

\[
 \begin{aligned}
 \mathcal D_\ell(C,\sigma)-\mathcal D_\ell(C,\sigma')
 ={}&
 [C\cup L_{\ell-1}\cup\{x\}]
 +[C\cup\{y\}\cup R_{\ell-1}]\\
 &-[C\cup L_{\ell-1}\cup\{y\}]
 -[C\cup\{x\}\cup R_{\ell-1}].
 \end{aligned}
\tag{2.1}
\]

For

\[
 2\le\ell\le M-2,
\tag{2.2}
\]

all four displayed values are distinct.  In that range the two positive
terms are precisely the old-only deck values and the two negative terms are
the new-only deck values.  At \(\ell=1\) and \(\ell=M-1\), the old values are
merely permuted into the new positions and the named deck is invariant,
although the signed occurrence identity still holds.

#### Proof

A cyclic interval changes as an occurrence only if it contains exactly one
of the two adjacent positions.  There are exactly two such intervals: the
interval of length \(\ell\) ending at \(x\), and the interval of length
\(\ell\) beginning at \(y\).  Their old and new label sets are exactly the
four terms in (2.1).  Every other interval contains both active positions or
neither, hence is unchanged.  Adjoining the same core \(C\) preserves the
identity.

For \(2\le\ell\le M-2\), a cross-equality would force the cyclic
\((\ell-1)\)-interval immediately before \(x\) to equal the cyclic
\((\ell-1)\)-interval immediately after \(y\).  Equal proper cyclic
intervals have the same initial position, which here occurs only at the
excluded co-singleton endpoint.  At the singleton endpoint both exterior
rays are empty and the two singleton values are visibly only permuted.
\(\square\)

### Corollary 2.2 (owner and immediate palettes)

For the pure-rail carousel with

\[
 q=d+1,\qquad |C|=R-q,
\]

the owner row is the \(\ell=q\) deck.  An adjacent transposition replaces
exactly the two owners

\[
 C\cup L_d\cup\{x\},\qquad C\cup\{y\}\cup R_d
\]

by

\[
 C\cup L_d\cup\{y\},\qquad C\cup\{x\}\cup R_d.
\tag{2.3}
\]

The selected immediate lower and upper palettes undergo the same coherent
trade at lengths \(d\) and \(d+2\), respectively.  Every other owner and
every other immediate-palette value is fixed.

### Corollary 2.3 (all lower and upper widths move coherently)

At every proper interval width, the two changed occurrences undergo the
same switch

\[
 \begin{array}{c|cc}
 &L_{\ell-1}&R_{\ell-1}\\ \hline
 \text{old}&x&y\\
 \text{new}&y&x.
 \end{array}
\tag{2.4}
\]

Thus the signed current has two old and two new occurrences **per width**,
not a number proportional to the component length at a fixed width.  It is
a literal named-value trade for \(2\le\ell\le M-2\); the singleton and
co-singleton named decks are fixed.  This is the all-width analogue of the
terminal birail interchange.

## 3. Hole-routing interpretation

Suppose a selected carousel edge is disjoint from the other selected owner
edges.  Replacing it by the transposed carousel is an admissible owner-matching
move exactly when the two new owners in (2.3) are currently uncovered (or are
the next vertices on an alternating augmentation), after which the two old
owners become the routed holes.

Because adjacent transpositions generate every permutation of the toggle
order, Theorem 2.1 supplies a complete local generating set on an isolated
carousel.  The unresolved global statement is not algebraic generation; it
is the simultaneous availability of a sequence whose two entering owners are
free and whose designated lower/upper/compiler witnesses can be rerouted.

In particular, the theorem proves the following exact reduction:

> A carousel absorber may be built from alternating paths of adjacent-toggle
> trades.  Each step has two owner ports and two coherent witness ports at
> every nonextreme interval width.

It does **not** prove that the alternating-path network expands, that all
component divisibility defects are absorbable, or that the final common cap
has a matching.
