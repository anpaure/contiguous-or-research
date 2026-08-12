# One-depth shift: vanished singleton jobs expose a capacity-faithful absorber

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional conditional implication for the anonymous two-SCD
fragmentation system.  Fractional feasibility at coefficient-one depth `D`
implies an integral fragmentation at depth `D+1` for every sufficiently
large even dimension.  The absorber consists of actual distinct collar
socket occurrences freed by the vanished length-one jobs.  The theorem does
not prove fractional feasibility at depth `D`, named Boolean containment,
or literal carrier serialization.

## 0. The two adjacent depth systems

Work in `B_(2r)`.  Put

\[
 C_s={2r\choose s},\qquad
 H_s=C_s-C_{s-1},\qquad
 W=C_r,
\tag{0.1}
\]

and let `D=d(2r)`, `t=r-D`.  Fix one residual SCD and one collar SCD.
For the exact finite statement below assume `D>=1` and `t>=2`; both hold
throughout the sufficiently-large regime of Corollary 2.2.  This restriction
avoids the degenerate bottom-zero case in which deleting the empty set
changes the nominal count `H_(t-1)` of length-one jobs.

At depth `D`, a residual chain with bottom rank `b<t` gives a job of
length

\[
                              L_D(b)=t-b,
\tag{0.2}
\]

apart from the usual deletion of the empty set in the unique bottom-zero
chain.  A collar chain with bottom rank `t+u` gives one socket occurrence of
capacity

\[
                              c_D(t+u)=u.
\tag{0.3}
\]

At depth `D+1`, the collar bottom is `t-1`.  On the same two SCDs,

\[
                         L_{D+1}(b)=L_D(b)-1
                         \qquad(b<t-1),
\tag{0.4}
\]

and every old socket occurrence gains one unit of capacity:

\[
                         c_{D+1}(t+u)=u+1.
\tag{0.5}
\]

The old jobs of length one, namely the `H_(t-1)` chains with bottom
`t-1`, disappear completely.  New capacity-one collar sockets also appear
at bottom `t`; they will not be needed below.

Deleting the empty set commutes with (0.4): the punctured bottom-zero job
also loses its terminal cell.  Hence no finite convention is hidden in the
shift.

## 1. Configuration transport through the shift

### Lemma 1.1 (terminal-cell deletion)

Let an old job of length `L>=2` have any integer fragmentation into pieces
of lengths at most `D`, assigned injectively to old collar sockets.  There
is a fragmentation of the corresponding new job of length `L-1` on a
subset of the same socket occurrences.

#### Proof

Order the pieces consecutively along the canonical suffix job.  Remove the
newly deleted terminal cell from the last piece.  If that piece had length
at least two, shorten it by one.  If it had length one, delete the piece and
free its socket.  Every retained piece remains positive and no longer than
before, while every retained socket has gained one unit by (0.5).  Thus all
old assignments remain valid. `square`

The construction is affine on configuration mixtures: apply it separately
to every configuration in the support of a fractional job.

### Lemma 1.2 (singletons free distinct positive sockets)

Every integrally packed old length-one job occupies exactly one socket.
After the shift the job disappears and that same occurrence is free with
new capacity at least two.

#### Proof

A positive fragmentation of total length one has exactly one piece, of
length one.  Distinct jobs use distinct sockets.  Every old positive socket
had capacity at least one and therefore has new capacity at least two by
(0.5). `square`

## 2. Exact `+1` integer-rounding theorem

Use the fractional whole-job configuration LP at depth `D`, either in
exact socket-type coordinates or in the equivalent conjugate-tail form of
`MATH_THEOREM_FRAGMENTATION_FERRERS_SEMIGROUP_BASIC_ROUNDING_AND_ABSORBER_20260805.md`.

### Theorem 2.1 (freed-singleton absorber)

Assume the depth-`D` fractional configuration LP is feasible.  If

\[
 H_{t-1}-2D
 \ \ge\ 
 2D\left\lceil{t-2\over2}\right\rceil,
\tag{2.1}
\]

then the complete nonempty residual job histogram has an integral
fragmentation into the actual depth-`D+1` collar socket occurrences.

#### Proof

Choose a feasible extreme point of the old fractional configuration LP.
By the basic-support theorem, at most `D` old jobs have more than one
positive configuration.  Call this family `F`.  Every other old job has one
integer configuration, and all those configurations together can be
injected into distinct old socket occurrences.

The endpoint triangle contains only `D` old socket occurrences.  Let `G`
be the family of integral jobs whose chosen configurations touch at least
one of them.  Since socket use is injective,

\[
                              |G|\le D.
\tag{2.2}
\]

Discard the jobs in `F union G` temporarily.  Every retained piece is now
assigned to a genuine collar-SCD occurrence, so (0.5) applies literally.

Apply Lemma 1.1 to every integrally packed job of length at least two.  The
corresponding new jobs are now packed integrally into the same, pairwise
distinct, lifted socket occurrences.

There are `H_(t-1)` old length-one jobs.  At most `D` of them belong to
`F` and at most `D` belong to `G`, so Lemma 1.2 frees at least

\[
                              H_{t-1}-2D
\tag{2.3}
\]

distinct lifted socket occurrences of capacity at least two.

The only new jobs not yet packed are those corresponding to members of
`F union G` having old length at least two.  There are at most `2D` of
them, and
each has new length at most `t-2`.  Fragment each into pieces of length two
and at most one final piece of length one.  Each job therefore needs at
most `ceil((t-2)/2)` of the freed occurrences.  Inequality (2.1) supplies
enough pairwise distinct sockets for all of them.  Every new job is now
packed integrally. `square`

### Corollary 2.2 (all sufficiently large even dimensions)

For all sufficiently large `r`, fractional feasibility of the depth-`D`
configuration LP implies integral feasibility at depth `D+1`.

#### Proof

The coefficient-one asymptotic gives

\[
                         D=\Theta(\sqrt r),
 \qquad t=\Theta(r).
\tag{2.4}
\]

The local central-binomial estimate at
`t-1=r-D-1` gives

\[
                         H_{t-1}=\Theta(W/\sqrt r).
\tag{2.5}
\]

The right side of (2.1) is `O(r^(3/2))`, whereas (2.5) is exponential in
`r`.  Hence (2.1) holds for every sufficiently large `r`. `square`

## 3. Interval and boundary variants

The proof is compatible with canonical suffix fragmentation, not merely
with an unordered length list.  In Lemma 1.1 the rightmost cell is removed
from the rightmost fragment, so all remaining fragments are still
consecutive pieces of the shortened suffix.  Thus the result also gives an
anonymous interval-row decomposition at depth `D+1`.

The same proof works for a punctured or triangularly corrected histogram
under the following explicit coherence hypotheses:

1. every new job is obtained from a surviving old job by deleting its
   terminal cell;
2. at least
   `2D ceil((t-2)/2)+2D` old length-one jobs survive; and
3. the old fractional configuration uses the same labelled collar socket
   occurrences which lift by (0.5).

Arbitrary independently chosen old and new boundary deletions need not
satisfy item 1, so no unconditional punctured claim is made.

## 4. Exact scope boundary

This theorem supplies a genuine capacity-faithful **occurrence** bank: the
absorber sockets are the distinct old socket occurrences vacated by
specific integral singleton jobs.  It is stronger than a scalar statement
that the extra depth adds `W` units of capacity.

It is still anonymous with respect to Boolean names.  The proof knows the
length of a residual fragment and the capacity of a collar occurrence, but
does not prove that the collar bottom contains the named top of that
fragment.  It also does not provide a central owner chronology, future-
intersection flags, residence, upper shadows, or a safe opening.

The exact implication established here is

\[
 \boxed{
 \text{fractional exact-}B\text{ two-SCD fragmentation}
 \quad\Longrightarrow\quad
 \text{integral anonymous }(B+1)\text{ fragmentation}
 }
\tag{4.1}
\]

for all sufficiently large even dimensions.  Therefore the integer
semigroup residue is not an independent obstruction to an additive-one
anonymous theorem.  The remaining rank-only premise is the all-price
fractional Rayleigh/binomial inequality; the remaining physical premise is
named containment and serialization on the same lifted occurrences.

## 5. Dependencies

1. `MATH_THEOREM_BOOLEAN_ENDPOINT_PRODUCT_ROUNDING_NOGO_AND_TWO_SCD_SOCKET_LEDGER_20260804.md`;
2. `MATH_THEOREM_MONOTONE_INTERVAL_CANONICAL_FRAGMENTATION_EQUIVALENCE_20260804.md`;
3. `MATH_THEOREM_FRAGMENTATION_FERRERS_SEMIGROUP_BASIC_ROUNDING_AND_ABSORBER_20260805.md`.
