# Cross-chain packet connectors

## 1. Outcome

Let a word over a finite join-semilattice be **universal** when its nonempty
contiguous joins contain every nonzero target.  The first cross-chain packet
suggested by `THICK_FOUR_BOX_SLICE_FUSION.md` is not an obstruction.  It has
a genuine linear fusion.

Write

\[
 R_c=[0,1]\times[0,1]\times[0,c]
\]

with coordinatewise maximum, and let `g(R_c)` denote the shortest nonzero
universal word.  The first two factors form the Boolean diamond.  Its usual
symmetric-chain decomposition consists of a three-point chain and a
singleton.  Pairing the chains independently with `[0,c]` gives length

\[
                         2c+3.                       \tag{1.1}
\]

The exact answer is substantially shorter.

### Theorem A (exact diamond packet)

For every integer `c>=0`,

\[
 \boxed{
             g(R_c)=c+\left\lceil{c\over2}\right\rceil+2
                   =\left\lceil{3c\over2}\right\rceil+2.}   \tag{1.2}
\]

Thus the two adjacent chain rectangles save

\[
 (2c+3)-g(R_c)=\left\lfloor{c\over2}\right\rfloor+1.        \tag{1.3}
\]

If the local minimum is nonzero in the ambient box and must also be
represented, add one entry to both sides of the comparison.  The saving in
(1.3) is unchanged.

The construction is explicit and search-free.  It also shows that the
simple alternating word of length `2c+2` is universal but is not shortest
once `c>=2`.

There is, however, a sharp warning about generalization.

### Theorem B (two-port obstruction)

Suppose a fused core is to be used as a black box between two external chain
tails: all heights `1,...,c` on the left tail must be obtained by adjoining a
prefix of the core, and all heights on the right tail by adjoining a suffix.
Then the core contains at least

\[
                              2c-1                 \tag{1.4}
\]

positions.  This scalar lower bound is sharp.  Hence the linear saving of
Theorem A cannot be retained by attaching arbitrary chain tails to its two
ends through conventional prefix/suffix portals.  A useful larger packet
must let the tail entries participate nonlocally in the mixed witnesses.

Finally, the terminal adjacent pair in an arbitrary two-chain hook
decomposition is exactly a thin three-box, not merely analogous to one.
For a rectangle `[0,p]x[0,q]`, `p<=q`, its last two hooks form

\[
                  [0,1]\times[0,q-p+1].            \tag{1.5}
\]

Consequently, the next packet theorem is precisely a uniform fusion bound
for `[0,1]x[0,s]x[0,c]`.  The diamond theorem settles `s=1`; no general
`Omega(min(s,c))` saving is proved here.

## 2. Notation for the diamond

Put

\[
 \begin{aligned}
 Z_j&=(0,0,j),\\
 X_j&=(1,0,j),\\
 Y_j&=(0,1,j).
 \end{aligned}                                    \tag{2.1}
\]

The target `(1,1,j)` will be denoted `XY_j`, but no `XY_j` entry is needed
in the construction.

The key economy is to divide the positive heights into two classes.

* A **low** height gets one literal colored pivot `X_j` or `Y_j`.
* A **high** height gets only its forced literal `Z_j`; it is placed between
  two pivots of opposite colors.

There are `ceil(c/2)` low heights and `floor(c/2)` high heights.  The same
positive colored pivot which represents one low target is also an endpoint
of one or two high-height witnesses.

## 3. Explicit optimal word

### 3.1 Even height

Let `c=2m`.  For `1<=i<=m`, choose alternating pivots `P_i` with

\[
 P_i=
 \begin{cases}
 Y_i,&m-i\text{ is even},\\
 X_i,&m-i\text{ is odd}.
 \end{cases}                                      \tag{3.1}
\]

In particular `P_m=Y_m`.  First output

\[
 P_1,Z_{m+1},P_2,Z_{m+2},\ldots,
 P_m,Z_{2m}.                                      \tag{3.2}
\]

Then output, in decreasing order, the `Z_i` for which `P_i=Y_i`; output

\[
                              X_0,Y_0;             \tag{3.3}
\]

and finally output, in increasing order, the `Z_i` for which `P_i=X_i`.

There are `m` pivots, `m` high zero-pivots, `m` low zero-pivots, and two
height-zero pivots.  The length is

\[
                              3m+2.                \tag{3.4}
\]

### 3.2 Odd height

Let `c=2m+1` and put `r=m+1`.  Choose alternating pivots
`P_1,...,P_r`, again ending in `P_r=Y_r`.  First output

\[
 P_1,Z_{r+1},P_2,Z_{r+2},\ldots,
 P_m,Z_{r+m},P_r.                                 \tag{3.5}
\]

The last displayed high pivot is `Z_(2m+1)`.  Follow this by the same low
tail as before:

1. the `Z_i` with `P_i=Y_i`, in decreasing order;
2. `X_0,Y_0`;
3. the `Z_i` with `P_i=X_i`, in increasing order.

The length is

\[
                    (m+1)+m+(m+1)+2=3m+4.         \tag{3.6}
\]

Equations (3.4) and (3.6) equal the right side of (1.2).

A direct exhaustive sanity checker for the displayed construction is
`scratch/diamond_packet_verify.cpp`.  It independently enumerates every
interval and verifies all targets for `0<=c<=100`; this is not used in the
proof.

## 4. Coverage proof

Every positive zero target `Z_j` occurs literally.  The targets `X_0` and
`Y_0` occur literally, and the two-entry interval `X_0,Y_0` represents
`XY_0`.

Consider a high height.  In the odd construction, every high `Z_j` lies
directly between two opposite-colored pivots, both of height below `j`.
The singleton `Z_j`, its two two-entry intervals with the neighboring
pivots, and the three-entry interval through both pivots represent

\[
                         Z_j,X_j,Y_j,XY_j.          \tag{4.1}
\]

The same is true for all but the final high pivot in the even construction.
The final pivot `Z_(2m)` has `P_m=Y_m` on its left and `X_0` on its right;
the intervening low zero-pivots all have height at most `m`.  Hence the same
four witnesses work, with a possibly longer interval on the right.

Now let `1<=i<=ceil(c/2)` be low.

* If `P_i=Y_i`, then `Y_i` is literal.  Its `Z_i` lies in the decreasing
  zero-pivot block immediately to the left of `X_0`.  Every zero-pivot
  between `Z_i` and `X_0` has height at most `i`.  Thus the intervals
  from `Z_i` through `X_0`, and through `X_0,Y_0`, represent `X_i` and
  `XY_i`.
* If `P_i=X_i`, then `X_i` is literal.  Its `Z_i` lies in the increasing
  zero-pivot block immediately to the right of `Y_0`.  Every preceding
  zero-pivot in that block has height at most `i`.  Hence the intervals
  from `Y_0` through `Z_i`, and from `X_0,Y_0` through `Z_i`, represent
  `Y_i` and `XY_i`.

Together with the literal `Z_i`, all four targets at every low height are
represented.  This proves the upper half of Theorem A.

## 5. Exact lower bound

The lower bound is an interval-order argument; it does not assume the form
of the construction.

By coordinatewise closure, every entry of a candidate word may be assumed
to be a point of `R_c`.  For every `1<=j<=c`, representing `Z_j` forces a
literal occurrence of `Z_j`: every entry in such a witness has first two
coordinates zero, and some entry must attain height `j`.  Representing
`X_0` and `Y_0` likewise forces literal occurrences of those two points.

Choose one forced occurrence of each of

\[
                         Z_1,\ldots,Z_c,X_0,Y_0.   \tag{5.1}
\]

If the word has length `n`, call its remaining

\[
                              e=n-(c+2)            \tag{5.2}
\]

positions **extra**.

Call a positive height `j` exceptional if either

1. `Z_j` occurs at least twice, or
2. the word contains `X_j` or `Y_j` as an entry.

Distinct exceptional heights can be charged to distinct extra positions:
use a second `Z_j`, or the displayed pure colored entry.  Therefore

\[
                 \#\{\text{exceptional heights}\}\le e.     \tag{5.3}
\]

Now fix a nonexceptional height `j`.  The unique `Z_j` occurrence must lie
in every witness for `X_j` and in every witness for `Y_j`.  Indeed, neither
pure colored entry at height `j` exists, and no entry carrying the opposite
color may occur in either pure target witness.

The two witnesses must acquire their `X` and `Y` colors on opposite sides
of `Z_j`.  If both colors were acquired on the same side, the farther
colored entry and `Z_j` would enclose the nearer entry of the opposite
color, contaminating one of the two pure witnesses.  Consequently `Z_j`
lies between two consecutive colored positions of the word, one pure `X`
and one pure `Y`.  Every intervening entry is uncolored and has height at
most `j`; otherwise one of the two witnesses would be contaminated.  The
maximum height in this colored gap is therefore exactly `j`.

No two nonexceptional heights can use the same colored gap, since one fixed
gap has only one maximum height.  It remains to count the available gaps.

Let `q` be the number of colored positions, meaning entries with first or
second coordinate nonzero.  Apart from the selected `X_0,Y_0`, all such
positions are extra, so

\[
                              q\le e+2.             \tag{5.4}
\]

There are `q-1` gaps between consecutive colored positions, but at least
one cannot serve a positive nonexceptional height.  To see this, take an
interval witnessing `XY_0`.  It has height zero throughout.  If it contains
an `XY`-colored entry, a gap incident with that entry does not have opposite
pure endpoints.  Otherwise, scanning the colored positions in the witness
finds a consecutive pure-color transition `X|Y` or `Y|X`; its gap has
maximum height zero.  In either case at least one of the `q-1` gaps is
unavailable to a positive height.

It follows that

\[
              \#\{\text{nonexceptional heights}\}
                    \le q-2\le e.                 \tag{5.5}
\]

Combining (5.3) and (5.5) gives

\[
                              c\le2e.              \tag{5.6}
\]

Hence `e>=ceil(c/2)`, and (5.2) proves

\[
                    n\ge c+\left\lceil{c\over2}\right\rceil+2.
\]

This matches the explicit word and completes Theorem A.

## 6. Audit of the simple alternating word

The natural word

\[
 X_0,Y_0,Z_1,X_0,Z_2,Y_0,Z_3,X_0,Z_4,Y_0,\ldots   \tag{6.1}
\]

with the color after `Z_j` chosen opposite to the colored entry immediately
before it has length `2c+2`.  At every positive height, `Z_j` is bracketed
by opposite colors of height zero, so its local one-, two-, and three-entry
intervals give all four targets.  The initial `X_0,Y_0` gives the height-zero
targets.  Thus (6.1) is valid.

Theorem A shows exactly how much it wastes:

\[
 (2c+2)-g(R_c)=\left\lfloor{c\over2}\right\rfloor. \tag{6.2}
\]

The waste comes from assigning a fresh colored pivot to every positive
height.  In the optimal construction one positive pivot simultaneously
serves its own low height and as a boundary for a different high height.

## 7. Why the optimal diamond cannot be used as a two-port black box

The obstruction is already visible after forgetting the first two
coordinates.

### Lemma 1 (two-sided record bound)

Let `h_1,...,h_N` be integers in `[0,c]`.  Suppose that for every
`1<=k<=c` some prefix has maximum exactly `k`, and some suffix has maximum
exactly `k`.  Then

\[
                              N\ge2c-1.             \tag{7.1}
\]

#### Proof

For every `k`, choose the first position at which the prefix maximum becomes
`k`.  These give `c` distinct prefix-record positions.  Reading from the
right gives `c` distinct suffix-record positions.

A position belonging to both sets must itself have height `k` and be a
record from both directions.  Then no entry anywhere in the word exceeds
`k`.  Since the word realizes prefix and suffix maximum `c`, the common
record can only have `k=c`.  Thus the two record sets overlap in at most one
position, proving (7.1).  The mountain

\[
                     1,2,\ldots,c-1,c,c-1,\ldots,2,1
\]

shows sharpness.  \(\square\)

Now suppose a longer first chain is placed immediately to the left of a
mixed core.  If every target at height `k` on that chain is to be obtained
by taking a chain-tail entry followed by a prefix of the core, the core's
height sequence must have every `k` as a prefix maximum.  Attaching a second
chain on the right by suffix witnesses imposes the suffix condition.
Lemma 1 forces `2c-1` core positions.

The two independent chain connectors spend only `2c` positive-height
positions in total.  Therefore a conventional two-port replacement can
save at most one of them.  The `Theta(c)` saving in Theorem A depends on the
fact that the diamond has no external tails: its positive colored pivots are
free to act inside witnesses instead of presenting complete vertical flags
at both ends.

This is a sharp obstruction to the most immediate extension, not a lower
bound on unrestricted mixed words for longer adjacent chains.

## 8. Geometry of the terminal hook pair

For `0<=t<=p<=q`, write the standard symmetric hook in
`[0,p]x[0,q]` as

\[
 H_t=(t,0),(t,1),\ldots,(t,q-t),
     (t+1,q-t),\ldots,(p,q-t).                    \tag{8.1}
\]

Its edge height is `p+q-2t`.  The last two hooks are

\[
 H_{p-1}\quad\text{and}\quad H_p.
\]

A direct inspection gives

\[
 H_{p-1}\sqcup H_p
       =\{p-1,p\}\times[0,q-p+1].                 \tag{8.2}
\]

After translating the first coordinate, their packet with `[0,c]` is

\[
                  [0,1]\times[0,s]\times[0,c],
                  \qquad s=q-p+1.                 \tag{8.3}
\]

The independent connectors, with the local minimum included, have total
length

\[
                  2s+2c+2.                        \tag{8.4}
\]

Indeed, the two hook edge heights are `s+1` and `s-1`.  Thus a terminal-pair
fusion saving `Omega(min(s,c))` is exactly a bound of the form

\[
 g([0,1]\times[0,s]\times[0,c];\text{ local zero included})
 \le2s+2c+2-\Omega(\min(s,c)).                     \tag{8.5}
\]

For `s=1`, Theorem A gives the stronger saving
`floor(c/2)+1`.  For general `s`, (8.5) is already a nontrivial thin
three-box problem.  The two-port lemma explains why merely inserting the
optimal `s=1` word at the turn and leaving the long arms outside cannot
prove it.

Nonterminal adjacent hooks form a two-rail ribbon with one or more changes
in the orientation of its cross-comparabilities.  They are not automatically
isomorphic to the straight strip (8.3).  Any packet theorem used across the
entire three-box SCD must handle these turns rather than silently replacing
the ribbon by a product of two chains.

## 9. Aggregation accounting

The diamond theorem is a genuine local fusion, but isolated diamonds do not
change the equal-four-box leading term.  In the nested-hook SCD, a terminal
square packet occurs only when the corresponding two-chain rectangle is
balanced.  There are too few such isolated packets to remove the
`Theta(m^3)` independent-chain excess found in
`THICK_FOUR_BOX_SLICE_FUSION.md`.

To obtain a cubic total saving, one needs a positive-density family of
adjacent-chain packets, each saving a constant fraction of
`min(c,L_j)`.  The exact next statement is therefore:

> **Ribbon packet lemma (open).**  Pair adjacent hooks in the nested SCD.
> For a pair with characteristic rail length `L`, construct one mixed word
> for both rectangles times `[0,c]` whose length is the sum of the two
> independent connector lengths minus `Omega(min(c,L))`, uniformly through
> all hook turns.

Theorem A proves this phenomenon at the smallest ribbon.  Theorem B rules
out the naive proof which treats that ribbon as a two-port core.  A successful
proof must braid rail entries with the height markers throughout the packet.

## 10. Final ledger

Proved:

* the exact formula `g([0,1]^2 x [0,c])=ceil(3c/2)+2`;
* an explicit optimal word for every `c`;
* an exact lower bound charging positive heights to extra entries and
  opposite-color gaps;
* the sharp `2c-1` two-port record obstruction;
* the exact reduction of the terminal hook pair to
  `[0,1]x[0,q-p+1]x[0,c]`; and
* the exact independent length and saving accounting.

Open:

* the thin-strip packet bound (8.5) for arbitrary `s`;
* a uniform connector for nonterminal two-rail hook ribbons; and
* a packet aggregation with enough total saving to make the thick four-box
  error subcritical.
