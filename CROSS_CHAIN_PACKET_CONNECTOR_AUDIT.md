# Independent audit of `CROSS_CHAIN_PACKET_CONNECTOR.md`

## 1. Verdict

The diamond-packet theorem is correct without computational assistance:

\[
 \boxed{g([0,1]^2\times[0,c])
       =c+\lceil c/2\rceil+2
       =\lceil3c/2\rceil+2}                         \tag{1.1}
\]

for every integer `c>=0`.  The displayed words have the asserted lengths
and cover every nonzero point.  The lower bound correctly handles arbitrary
words, including entries of type `XY_j`, duplicate literals, and both
parities.  The boundary cases are

\[
 g(R_0)=2,qquad g(R_1)=4,qquad g(R_2)=5.           \tag{1.2}

The scalar two-sided-record lemma is also correct and sharp for `c>=1`:

\[
                              N\ge2c-1.             \tag{1.3}

For `c=0` its printed right side is negative and “sharpness” is not
meaningful; the uniform nonnegative statement is

\[
                              N\ge\max(0,2c-1).     \tag{1.4}

Theorem B needs its portal hypothesis stated literally.  The record lower
bound applies when

* every left-tail target uses an external part whose vertical height is
  zero and then terminates in a **prefix** of the core; and
* every right-tail target begins in a **suffix** of the core and then uses
  an external height-zero part.

If an external tail already supplies vertical height `k`, or a witness is
allowed to cross the entire core and enter the opposite tail, the prefix or
suffix maximum need not equal `k`, so Lemma 1 no longer applies.  The source
does ultimately describe the result as an obstruction to “conventional
prefix/suffix portals”; it is not an unrestricted lower bound for every
possible attachment of two tails.

## 2. The explicit construction

Use

\[
 Z_j=(0,0,j),\quad X_j=(1,0,j),\quad Y_j=(0,1,j),
 \quad XY_j=(1,1,j).                                \tag{2.1}
\]

Every target at height `j` is one of these four points, except that `Z_0`
is the excluded zero target.

### 2.1 Even case

Let `c=2m`.  There are `m` low pivots `P_i`, alternating colors and ending
with `P_m=Y_m`.  The first part is

\[
 P_1,Z_{m+1},P_2,Z_{m+2},\ldots,P_m,Z_{2m}.        \tag{2.2}
\]

It contains `m` colored low pivots and `m` high `Z` pivots.  The tail
contains every low `Z_i` once, followed by `X_0,Y_0`, so it has `m+2`
positions.  Total length is

\[
                              3m+2.                 \tag{2.3}

For `m=0`, all patterned portions are empty and the construction is simply
`X_0,Y_0`, correctly covering the three nonzero points of `R_0`.

### 2.2 Odd case

Let `c=2m+1` and `r=m+1`.  There are `r` low pivots, alternating and ending
at `P_r=Y_r`.  The first part is

\[
 P_1,Z_{r+1},P_2,Z_{r+2},\ldots,
 P_m,Z_{r+m},P_r.                                  \tag{2.4}
\]

It has `m+1` colored pivots and `m` high `Z` pivots.  The low-zero tail has
`m+1` entries plus `X_0,Y_0`.  Thus the total is

\[
                         3m+4.                      \tag{2.5}

For `m=0`, the word is explicitly

\[
                         Y_1,Z_1,X_0,Y_0,           \tag{2.6}

which covers `R_1` and has length four.

Equations (2.3) and (2.5) are respectively

\[
 c+\lceil c/2\rceil+2
 =\lceil3c/2\rceil+2.                               \tag{2.7}

## 3. Coverage, reconstructed without search

Every `Z_j`, `j>=1`, is literal.  The entries `X_0,Y_0` are literal, and
their two-entry interval has join `XY_0`.

### 3.1 High heights

In the odd word, each high `Z_j` is immediately bracketed by two low pivots
of opposite colors and lower height.  Therefore

* `Z_j` alone gives `Z_j`;
* either adjacent two-entry interval gives `X_j` or `Y_j`; and
* the three-entry interval gives `XY_j`.

In the even word the same applies except at `Z_(2m)`.  Its left neighbor is
`P_m=Y_m`.  To its right lie only low zero-pivots, all of height at most
`m`, until `X_0`.  Hence

\[
 Y_m\;|\;Z_{2m}\;|\;(\text{low }Z\text{'s})\;|\;X_0 \tag{3.1}

provides the same four joins at height `2m`.  No intervening entry carries
a contaminating color or greater height.

### 3.2 Low heights

If `P_i=Y_i`, then `Y_i` is literal.  The low `Z` entries of `Y` color are
listed in decreasing index order immediately before `X_0`.  Starting at
`Z_i`, every later zero-pivot has height at most `i`; consequently

\[
 Z_i\leadsto X_0=X_i,qquad
 Z_i\leadsto X_0,Y_0=XY_i.                          \tag{3.2}

Together with literal `Z_i,Y_i`, this covers all four targets.

If `P_i=X_i`, its `Z_i` lies in the increasing block immediately after
`Y_0`.  All earlier zero-pivots in that block have height at most `i`, so

\[
 Y_0\leadsto Z_i=Y_i,qquad
 X_0,Y_0\leadsto Z_i=XY_i.                          \tag{3.3}

Together with literal `Z_i,X_i`, this again covers all four.

This proves universality for every `c`; no property checked by the C++ file
is needed.

## 4. Forced entries and the extra-position ledger

Let an arbitrary universal nonzero word have length `n`.

### 4.1 Forced literals

For `1<=j<=c`, a witness for `Z_j` may contain only entries with first two
coordinates zero and height at most `j`.  Some entry must attain height
`j`, and the only possibility is literal `Z_j`.  Thus all `c` positive
`Z` points occur.

A witness for `X_0` may contain only height-zero entries with second
coordinate zero, and must attain first coordinate one.  It therefore
contains literal `X_0`; similarly `Y_0` is forced.

Choose one occurrence of every forced point and put

\[
                         e=n-(c+2).                 \tag{4.1}

Every other word position is extra.  This remains valid at `c=0`, where
only `X_0,Y_0` are forced.

### 4.2 Exceptional heights

Call positive height `j` exceptional when either `Z_j` is duplicated or a
literal `X_j` or `Y_j` occurs.  Every exceptional height can be charged to
a distinct extra position:

* choose a second `Z_j` in the first case;
* otherwise choose the displayed positive pure-color entry.

Entries at different heights are distinct, so these charges do not
collide.  Therefore

\[
                         E_{\rm exc}\le e.          \tag{4.2}

An `XY_j` entry is not omitted from the accounting.  It is colored and
extra, but it cannot appear in a pure `X_j` or `Y_j` witness, so it does not
make height `j` exceptional and is handled by the colored-gap count below.

## 5. Nonexceptional heights and opposite-color gaps

Fix a nonexceptional positive height `j`.

### 5.1 The unique `Z_j` is compulsory

A witness for `X_j` contains no entry with second coordinate one.  At
height exactly `j`, its only possible entries are `Z_j` and `X_j`; the
latter is absent.  Since the interval must attain height `j`, it contains
the unique `Z_j`.  The same argument puts that occurrence in every witness
for `Y_j`.

Each pure witness must also contain a colored entry of its own color and no
entry of the opposite color.  Its colored entry has height below `j`, since
`X_j,Y_j` are absent.

### 5.2 The colors lie on opposite sides

Suppose chosen `X` and `Y` color occurrences both lay to the left of the
unique `Z_j`.  The farther one and `Z_j` enclose the nearer one.  Thus one
of the pure witnesses contains the opposite color, a contradiction.  The
same argument excludes both being on the right.  Hence `Z_j` has an `X`
color on one side and a `Y` color on the other.

Take the nearest colored position on each side of `Z_j`.  They are
consecutive in the global sequence of colored positions.  Every colored
entry between the originally chosen pure-color entry and `Z_j` must have
the same pure color—an opposite or `XY` entry would contaminate that
witness.  Consequently the two nearest endpoints are opposite **pure**
colors.

All entries strictly between them are uncolored `Z` entries.  The two pure
witnesses show that their heights are at most `j`, while the gap contains
the unique literal `Z_j`.  Thus this colored gap has maximum height exactly
`j`.

One colored gap has only one maximum, so distinct nonexceptional heights use
distinct gaps.

## 6. Counting the colored gaps

Let `q` be the number of colored positions, i.e. entries whose first or
second coordinate is one.  Besides the selected occurrences of `X_0,Y_0`,
all colored positions are extra.  Hence

\[
                              q\le e+2.             \tag{6.1}

There are `q-1` gaps between consecutive colored positions.  At least one
cannot serve a positive nonexceptional height.

Choose a witness for `XY_0`.  Every entry in it has height zero.

* If it contains an `XY`-colored entry, at least one gap incident with that
  entry has a non-pure endpoint and is unavailable.  Such an incident gap
  exists because the forced `X_0,Y_0` are two distinct additional colored
  positions, so the `XY` position has a neighbor in the global colored
  order.
* If it contains no `XY` entry, it contains at least one pure `X` and one
  pure `Y`.  Two consecutive colored entries along that witness have
  opposite colors.  They are consecutive in the global colored order, and
  every intervening entry has height zero.  Their gap therefore has maximum
  zero.

Thus at most `q-2` gaps serve positive heights.  By Section 5,

\[
                         E_{\rm nonexc}\le q-2\le e. \tag{6.2}

Together with (4.2),

\[
 c=E_{\rm exc}+E_{\rm nonexc}\le2e.                \tag{6.3}

Since `e` is an integer,

\[
 e\ge\lceil c/2\rceil,qquad
 n\ge c+\lceil c/2\rceil+2.                        \tag{6.4}

For `c=0`, the exceptional/nonexceptional sets are empty and (6.4) reduces
to the already forced `n>=2`.  For odd `c`, integrality supplies exactly the
required ceiling.  This completes the noncomputational lower bound.

## 7. The two-sided record lemma

Let `c>=1`, and suppose `h_1,...,h_N in [0,c]` has every value
`1,...,c` as both a prefix maximum and a suffix maximum.

For each `k`, let `p_k` be the first index at which the prefix maximum is
`k`.  Then `h_(p_k)=k`, and the `c` positions `p_k` are distinct.  Reading
from the right, let `s_k` be the first position at which the suffix maximum
becomes `k`; these are another `c` distinct positions.

If one position lies in both sets, its value shows that it is `p_k=s_k` for
the same `k`.  Prefix-record status makes every entry to its left at most
`k`, and suffix-record status makes every entry to its right at most `k`.
Thus the global maximum is `k`.  Since the hypotheses realize maximum `c`,
one must have `k=c`.  The two record sets intersect in at most one position,
so

\[
                              N\ge2c-1.             \tag{7.1}

The mountain

\[
                      1,2,\ldots,c-1,c,c-1,\ldots,2,1 \tag{7.2}

has length `2c-1` and realizes every required prefix and suffix maximum.
This proves sharpness for all `c>=1`, including the one-element mountain at
`c=1`.

For `c=0`, there are no record requirements.  If an empty core is allowed,
the optimum is zero; if a core is required to be nonempty, it is one.  The
formula `2c-1` should not be asserted as a sharp cardinality in that case.

## 8. Scope of the two-port obstruction

The record lemma yields Theorem B only after the portal model implies its
hypothesis.  A sufficient formal portal model is:

* a left-tail witness consists of a prescribed external segment whose
  vertical maximum is zero, followed by a prefix of the core, and stops
  inside the core;
* for every target vertical height `k`, some such core prefix must raise the
  maximum to exactly `k`;
* symmetrically, a right-tail witness begins in a core suffix, exits to an
  external segment of vertical maximum zero, and every `k` is supplied by
  a suffix maximum.

Then the core height word satisfies Section 7 and has at least `2c-1`
positions.  Two independent conventional connectors use `2c`
positive-height core positions, so this portal architecture can save at
most one.

The conclusion does **not** follow without those restrictions.  In
particular:

1. if a tail entry or external segment itself has height `k`, the included
   core prefix may have maximum below `k`;
2. if a left-tail witness crosses the entire core and continues into the
   right tail, it is not represented by a core prefix maximum; and
3. if different target heights use different external vertical markers,
   the record sets need not exist at all.

Thus Theorem B is a sharp scalar obstruction to the explicitly conventional
two-port black box, exactly as the final paragraphs of the source intend.
It is not an obstruction to nonlocal mixed witnesses, and it should not be
quoted without the portal hypotheses.

## 9. Corrected ledger

**Proved:**

* the explicit construction for every `c>=0`;
* exact universality by the interval witnesses in Section 3;
* the arbitrary-word lower bound and parity rounding;
* the exact formula (1.1), including `c=0,1`;
* the record bound `2c-1` and its sharp mountain for `c>=1`.

**Qualification:** for `c=0`, replace the two-port lower bound by the
appropriate zero/one convention for an empty/nonempty core.

**Scope:** the two-port application requires pure prefix and suffix portals
whose external pieces do not supply positive vertical height and whose
witnesses do not cross both ports.

No C++ enumeration is used anywhere in this audit.
