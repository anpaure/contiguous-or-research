# A common-intersection alternating circuit has an exact source lift

**Date:** 2026-08-13  
**Status:** unconditional prospective local theorem.  It reduces protected
resident switching to finite owner/immediate-palette algebra whenever the
changed owners have a sufficiently large common intersection.  It does not
assert that a required circuit exists in a given frozen factor.

## 1. Data

Let `A_0,...,A_(s-1)` and `B_0,...,B_(s-1)` be distinct rank-`R` owners.
Let `pi` be a permutation of `Z_s`.  Suppose

\[
             H\subseteq\bigcap_{i=0}^{s-1}(A_i\cap B_i),
             \qquad |H|\ge d\ge1.                 \tag{1.1}
\]

Assume the old and new pairs

\[
             A_iB_i,
             \qquad A_iB_{\pi(i)}                 \tag{1.2}
\]

are all Johnson edges and that their immediate colour multisets agree:

\[
 \left\{\!\left\{A_i\cap B_i:i\in\mathbb Z_s\right\}\!\right\}
 =\left\{\!\left\{A_i\cap B_{\pi(i)}:i\in\mathbb Z_s\right\}\!\right\},
                                                               \tag{1.3}
\]

\[
 \left\{\!\left\{A_i\cup B_i:i\in\mathbb Z_s\right\}\!\right\}
 =\left\{\!\left\{A_i\cup B_{\pi(i)}:i\in\mathbb Z_s\right\}\!\right\}.
                                                               \tag{1.4}
\]

The permutation need not be one cycle.  When the symmetric difference of
the two matchings is one alternating circuit, it is the usual cyclic
rethread; allowing general `pi` permits several disjoint circuits at once.

Partition `H` into nonempty sets

\[
             H=C_1\mathbin{\dot\cup}\cdots
               \mathbin{\dot\cup}C_d.             \tag{1.5}
\]

Put

\[
             X_i=A_i\setminus H,
             \qquad Y_i=B_i\setminus H.            \tag{1.6}
\]

The old and new source fragments are

\[
 W_i=(X_i,C_1,\ldots,C_d,Y_i),
 \qquad
 \widehat W_i=(X_i,C_1,\ldots,C_d,Y_{\pi(i)}).    \tag{1.7}
\]

At source level, cut immediately before every tagged `Y_j` occurrence and
move its complete residual path to the role that receives `Y_j`.  This is
well-defined even when several cuts lie on one old component.  Require the
displayed fragment occurrences to be **cut-separated**: no tagged `Y` cut
lies strictly inside another displayed left block
`X_h,C_1,...,C_d`.  Occurrence-disjoint protected fragments are a sufficient
way to ensure this premise.

## 2. The lift theorem

### Theorem 2.1 (common-intersection circuit lift)

Under `(1.1)--(1.4)` and the cut-separation premise, the rethread `(1.7)`:

1. realizes exactly the old and new owner edges in `(1.2)`;
2. preserves the complete owner, immediate-lower, and immediate-upper
   occurrence multisets;
3. gives a literal occurrence-, width-, and value-preserving bijection on
   every interval OR of rank strictly below `R`;
4. therefore transports every source-derivative lower row and every
   cell-based strict-lower compiler assignment exactly;
5. preserves the complete internal fragment deck at every width;
6. has zero source-length charge; and
7. on a cyclic carrier, every nonconstant positive owner run created by a
   source occurrence has length at least `d+1`.

No assertion about zero-run length, exterior upper intervals, selected
q2 companions, socket state, or cap routes is implicit in this theorem.

#### Proof

The two length-`d+1` windows in `W_i` have values

\[
              H\cup X_i=A_i,
       \qquad H\cup Y_i=B_i,                       \tag{2.1}
\]

and the corresponding windows in `\widehat W_i` have values
`A_i,B_(pi(i))`.  Hence the owner row is precisely `(1.2)`.  The owner
multiset is unchanged because the `A` roles are fixed and the `B` roles are
permuted.  Equations `(1.3)--(1.4)` give the two immediate palettes.

Cut all affected source components just before the tagged `Y` occurrences.
This creates disjoint tagged residual paths, each beginning with one `Y_j`.
The rethread only permutes these complete paths.  Consider an interval
crossing one new seam.  If it reaches the left screen `X_i`, it contains all
history letters and therefore contains

\[
                         H\cup X_i=A_i,             \tag{2.2}
\]

of rank `R`.  Thus a strict-lower interval crossing a changed seam uses only
a suffix of the common history followed by a prefix of the transported
`Y_j` path.  Map it to the old seam before that same tagged path.  Its
history suffix, transported path prefix, width, and OR value are literal
copies.  A strict-lower interval cannot cross a second changed seam, since
between two cuts it then contains one complete `X_h,C_1,...,C_d` block and
hence the owner `A_h`.  Intervals avoiding cuts stay fixed inside their
tagged residual paths.  The reverse rethread supplies the inverse map,
proving the strict-lower occurrence bijection.

The internal fragment has length `d+2`.  Widths at most `d` are one-sided
and are covered by the same bijection.  Width `d+1` is the owner row.
Width `d+2` consists of the values `A_i\cup B_i` before the move and
`A_i\cup B_(pi(i))` after it, whose multisets agree by `(1.4)`.  Hence the
complete internal deck is exact.

Finally, every occurrence of a coordinate in a cyclic source word belongs
to `d+1` consecutive owner windows.  Each occurrence therefore contributes
a positive interval of length `d+1`; unions of such intervals have no
shorter nonempty component.  The operation only permutes existing source
blocks, so its length charge is zero.  This proves all claims.  `square`

## 3. Immediate consequence for short Johnson collars

### Corollary 3.1 (short-support criterion)

Suppose every changed owner lies in a Johnson walk segment of `ell` edges
starting at one rank-`R` owner, and all auxiliary owners retain the
intersection of that segment.  Then the common intersection has size at
least `R-ell`.  Consequently every palette-neutral alternating trade on
that support has the lift of Theorem 2.1 whenever

\[
                         ell\le R-d.                \tag{3.1}
\]

#### Proof

At most one coordinate is deleted at each Johnson transition, so the
intersection of the walk owners has size at least `R-ell`.  The rest is
Theorem 2.1.  `square`

For the universal-word scale `R=Theta(k)` and `d=Theta(sqrt(k))`, every
`O(d)`-edge local Boolean trade has abundant common-history room.  Thus the
local source/residence problem for a short PBBS collar reduces to finding a
palette-neutral alternating trade whose auxiliary owners stay inside the
collar's large common-intersection slice.  Global disjoint planting and
fresh exterior witness assignment remain separate problems.

This theorem generalizes the rank-three, five-head common-history argument
in
`MATH_THEOREM_PBBS_PENTAGON_THREE_SCREEN_COMMON_HISTORY_AND_UPPER_CURRENT_GATE_20260805.md`.
Section 6 of that note gives the corresponding complete exterior-current
tensor.  The present abstraction does not make that exterior current vanish.
