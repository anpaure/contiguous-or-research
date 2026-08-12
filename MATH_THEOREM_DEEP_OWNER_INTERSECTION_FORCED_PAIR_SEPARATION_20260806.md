# Deep owner intersections are separated from their literal source cells

**Date:** 2026-08-06  
**Method:** exact event-index algebra for resident Johnson traces; no
computation or search  
**Status:** unconditional local obstruction and necessary design criterion.
A consecutive owner intersection of depth greater than the antecedent depth
cannot be realized on any source position in the owner interval or its
full depth-`d` forward collar.  Therefore the deep PBBS gap-section SDR must
be rerouted to remote source occurrences.  Singleton targets exist exactly
at coordinate runs of minimum permitted length.

## 1. Event and source notation

Let

\[
 T_{j+1}=T_j-\{D_j\}+\{I_j\}
\tag{1.1}
\]

be a cyclic simple rank-`r` Johnson trace with antecedent depth `d`.  For a
source position `j`, the exact forced-letter theorem gives

\[
 F_j=\{D_j,I_{j-d-1}\}\subseteq A_j
\tag{1.2}
\]

in every antecedent `A` of `T`.

Fix an unwrapped interval of owners and put

\[
 S(i,q)=\bigcap_{h=0}^{q}T_{i+h}.
\tag{1.3}
\]

The statements below concern a nonwrapping representative.  The cyclic
form follows after choosing the cut outside the displayed owner interval.

## 2. Forced-pair separation

### Theorem 2.1

If `q>d`, then

\[
 \boxed{F_j\not\subseteq S(i,q)
 \quad\hbox{for every }j\in[i,i+q+d].}
\tag{2.1}
\]

Consequently no nonempty source block `J` meeting this exclusion interval
can have union `S(i,q)` in an antecedent of this fixed trace.

#### Proof

If

\[
                         i\le j\le i+q-1,
\tag{2.2}
\]

then the transition (1.1) makes `D_j` absent from `T_(j+1)`, one of the
owners in (1.3).  Therefore `D_j notin S(i,q)`.

If instead

\[
                         i+d+1\le j\le i+q+d,
\tag{2.3}
\]

put `e=j-d-1`.  Then `i<=e<=i+q-1`.  Immediately before its insertion on
edge `e`, the coordinate `I_e` is absent from `T_e`, again one of the
owners in (1.3).  Hence `I_(j-d-1) notin S(i,q)`.

Because `q>d`, the intervals in (2.2)--(2.3) overlap or are adjacent, and
their union is `[i,i+q+d]`.  At every position in that union at least one
member of `F_j` is absent from `S(i,q)`, proving (2.1).

If a nonempty source block `J` meeting the exclusion interval had union
`S(i,q)`, choose `j in J cap [i,i+q+d]`.  Then
`A_j subseteq S(i,q)`, while (1.2) gives `F_j subseteq A_j`, contradicting
(2.1).  \(\square\)

### Corollary 2.2 (the deep owner SDR is necessarily nonlocal)

An occurrence-labelled matching which assigns the value `S(i,q)`, `q>d`,
to its owner-intersection address cannot be transported to an ordinary
source interval in the entire local zone `[i,i+q+d]`.  Any literal compiler
using the same target value must find a remote position block `J` satisfying

\[
 \bigcup_{j\in J}F_j\subseteq S(i,q)
 \subseteq\bigcup_{j\in J}P_j.
\tag{2.4}
\]

Thus the deep block-selection lemma is a global occurrence-rerouting
problem, not a local inverse-envelope problem.

## 3. Exact singleton criterion

### Theorem 3.1

For a coordinate `x`, the singleton target `\{x\}` occurs as a source
letter in some antecedent of `T` if and only if `x` has a positive owner
run of length exactly `d+1`.

#### Proof

If `A_j=\{x\}`, then (1.2) gives

\[
                         D_j=I_{j-d-1}=x.
\tag{3.1}
\]

The insertion edge is `j-d-1`, so the run begins at owner `j-d`; the
deletion edge is `j`, so it ends at owner `j`.  Its length is exactly
`d+1`.

Conversely, suppose a run of `x` begins at owner `j-d` and ends at owner
`j`.  Then its insertion and deletion labels satisfy (3.1), and hence
`F_j=\{x\}`.  Also `x in P_j`, because it lies in all owners
`T_(j-d),...,T_j`.  The short-block freedom theorem applied to the
one-position block `J=\{j\}` permits the choice `A_j=\{x\}` while retaining
maximal letters elsewhere.  \(\square\)

### Corollary 3.2 (minimum-run necessity)

Any fixed resident trace intended to support a literal compiler for every
nonempty strict-lower target must give every coordinate at least one run of
length exactly `d+1`.

This is stronger than the usual residence inequality, which only requires
runs to have length at least `d+1`.

## 4. General forced-pair cover condition

Let

\[
                         \mathcal F(T)=\{F_j:j\in\mathbb Z_W\}.
\tag{4.1}
\]

Every target `S` represented by a nonempty source interval of length at
most `d` must contain at least one member of `mathcal F(T)`:

\[
 \boxed{\exists j\quad F_j\subseteq S.}
\tag{4.2}
\]

Indeed every position of its representing interval has its forced set
inside the interval union.  For a block of length `ell<=d`, all `ell`
forced sets must lie in `S`.  Its deletion labels are pairwise distinct:
if one coordinate were deleted twice inside this block, it would have to be
reinserted between the two deletions and its intervening positive owner run
would have length at most `ell<=d`, contradicting `d`-residence.  Therefore

\[
                         \ell\le |S|.
\tag{4.3}
\]

Equation (4.3) is compatible with the deadline triangle, but it is an
occurrence constraint rather than a scalar count.

## 5. PBBS consequence

The top `d` gap-section rows may use the maximal-antecedent row identity.
Theorem 2.1 proves that the deeper rows cannot use the owner-intersection
occurrence or any position in its full local collar.  A proof of the
one-copy PBBS antecedent therefore needs both:

1. a resident trace satisfying the minimum-run condition of Corollary 3.2;
   and
2. a global injection from every deep target to a remote short block obeying
   (2.4), together with the pinned-envelope equalities on overlapping
   blocks.

No aggregate owner-occurrence SDR proves either item.  Conversely, once
such a remote block injection is found, the exact short-block target-pin
theorem materializes it and the terminal compiler-transport theorem carries
it through the PBBS rethreads.
