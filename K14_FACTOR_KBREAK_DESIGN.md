# Exact factor-word k-break search for the pinnable k=14 checkpoint

## 1. Certified starting point

Let

```
A = k14_pinnable_factor_16093.txt
T = k14_pinnable_central_1938.txt.
```

Then `|A|=3434`, `|T|=3432`, and

\[
T_i=A_i\mathbin\lor A_{i+1}\mathbin\lor A_{i+2}.
\]

The factor `A` covers 16093 of the 16383 nonzero masks.  It covers every
mask of ranks 1 through 8 and 12 through 14.  Its exact remaining deficit is

\[
249\quad\text{rank-9 masks},\qquad
40\quad\text{rank-10 masks},\qquad
1\quad\text{rank-11 mask}.
\]

Every currently covered mask has a witness of length at most 10.  More
specifically, every mask of rank at most 8 has a witness of length at most 4,
and the shortest-witness distribution has maximum length 10.  This makes it
possible to abandon repeated global factor SAT calls and work directly on the
already valid factor word.

## 2. Window-color k-break lemma

For a word `A=(A_1,...,A_n)`, write

\[
W_h(A,i)=A_i\lor\cdots\lor A_{i+h-1}
\]

and, for a fixed horizon `H`,

\[
c_A(S)=\#\{(i,h):1\le h\le H,\ W_h(A,i)=S\}.
\]

Cut `A` into blocks, optionally reverse some blocks, and permute the signed
blocks to obtain `A'`.  Assume every block has length at least `H`.  Let
`R(S)` be the number of old length-at-most-`H` windows of color `S` crossing
an old cut, and let `N(S)` be the corresponding number crossing a new join.

**Lemma (exact local update).**

\[
c_{A'}(S)=c_A(S)-R(S)+N(S).
\]

In particular, if

\[
c_A(S)>0\Longrightarrow c_A(S)-R(S)+N(S)>0,
\]

then every mask having a length-at-most-`H` witness before the move still has
one afterward.  If `c_A(Q)=0` and `N(Q)>0`, the move additionally gains `Q`.

**Proof.**  A window of length at most `H` is either contained in one block or
crosses exactly one join.  Signed block permutation bijects the first class;
reversal does not change an OR.  The second class is precisely the old/new
crossing-window multisets counted by `R` and `N`.

For the present factor take `H=10`.  If every accepted move satisfies the
strict positivity condition for all currently covered colors and creates at
least one missing color, coverage grows monotonically.  Factorability is
automatic because the object being changed is the actual array `A`, rather
than a proposed central row.

This is stronger and simpler than separately preserving the rank-6/rank-8
edge colors.  If one only wants to preserve universality through rank 8, it is
enough to use `H=4`: ranks 1--6 already occur in singleton/pair windows, rank
7 in triple windows, and rank 8 in four-entry windows.  Using `H=10` preserves
all 16093 currently covered masks, including the upper ranks, and should be
the default.

For clarity, the weakest length-sensitive sufficient test is:

* preserve every pair-only mask of rank at most 6 in the singleton/pair pool;
* preserve every rank-7 color in the length-3 pool;
* preserve every rank-8 color in the length-4 pool.

The old complete rank-6 *intersection colors between central vertices* are
not required for universality once the actual factor word is being searched:
rank 6 is already complete among adjacent pairs of `A`.  Johnson adjacency is
also optional.  It is useful only if one deliberately retains the central-row
normal form.  The aggregate `H=10` positivity test is easier to implement and
strictly more protective than the three bullets.

## 3. Constant-time seam evaluation

For every oriented block end `u`, precompute

\[
\operatorname{suf}_u(a)=\bigvee\text{(last `a` entries)},\qquad 1\le a<H,
\]

and for every oriented block start `v`, precompute

\[
\operatorname{pre}_v(b)=\bigvee\text{(first `b` entries)},\qquad 1\le b<H.
\]

The color multiset contributed at the join `u|v` is

\[
J(u,v)=\left\{
  \operatorname{suf}_u(a)\lor\operatorname{pre}_v(b):
  a,b\ge1,\ a+b\le H
\right\},
\]

with multiplicity.  It contains only

\[
\sum_{h=2}^{H}(h-1)=\binom H2=45
\]

windows when `H=10`.  Thus an `s`-join k-break changes at most `45s` old and
`45s` new colors.  Maintain `c_A` globally and evaluate a move with a small
sparse delta table; no full interval enumeration is required.

After acceptance, update only the seam deltas and the port profiles of the
new block ends.  To avoid windows crossing two joins, require every block
created by the cuts to have length at least 10.  This loses negligible search
freedom and makes the lemma and implementation exact.

## 4. Target-indexed joins

A new seam can witness a missing target `Q` exactly when, for some `a,b`,

\[
X=\operatorname{suf}_u(a)\subseteq Q,
\qquad
Y=\operatorname{pre}_v(b)\subseteq Q,
\qquad
X\lor Y=Q,
\qquad a+b\le H.
\]

Do not enumerate all pairs of cuts.  Bucket oriented prefixes and suffixes by
`(length,mask)`.  For each suffix mask `X subseteq Q`, the compatible prefix
masks are exactly

\[
Y=(Q\setminus X)\cup Z,\qquad Z\subseteq X.
\]

Looking up these buckets directly gives every seam that creates `Q`.  Rank-9,
rank-10, and rank-11 targets should first be sought at their natural minimum
factor-window lengths 5, 6, and 7, respectively, while the preservation
horizon remains 10.

For each target-producing seam, complete it to one of the following signed
linear reconnections:

1. a prefix or suffix reversal (only one old and one new internal join);
2. a two-cut internal segment reversal;
3. a three-cut block relocation, in either orientation;
4. a four-cut double-bridge exchange if the first three neighborhoods fail.

The endpoint reversals are worth testing first.  Reversing a prefix preserves
every internal window of that prefix and changes only its join to the suffix;
the new oriented port is the old beginning of the word.  The analogous
statement holds for a suffix reversal.  Hence only 45 old and 45 new colors
are involved, making a zero-loss move much more likely than for an internal
reversal.

Test the exact sparse color delta.  The acceptance order should be:

```
number of previously covered colors lost (must be 0),
-number of currently missing colors gained,
number of protected colors reduced to multiplicity 1,
number of cuts / total moved boundary mass.
```

The third term keeps multiplicity slack for later rounds.

## 5. Optional preservation of the central skeleton

The monotone-coverage search does not need to preserve `T=D^2 A` as a
permutation of the seventh layer: preserving all covered colors already keeps
every rank-7 and rank-8 mask represented.  If retaining the successful
central skeleton is desired, it is still a local condition.

At each old/new join, record the crossing triple ORs.  Internal triple windows
are preserved under signed block permutation.  Since the current triple row
contains every rank-7 mask exactly once, the new triple row is the same
permutation precisely when the multiset of new crossing triple ORs equals the
multiset of removed crossing triple ORs.  Johnson adjacency and the
rank-6/rank-8 edge-color counters then require inspection only of the few
triple-row edges touching the joins.

This stronger mode is useful as a fallback but is likely unnecessarily rigid.
The recommended first search preserves the whole 16093-color set at horizon
10 and allows the central skeleton to deform.

## 6. Why this differs from the previous path search

Changing `T` first can destroy exact lower labelability, so every candidate
needed another global SAT call.  A signed k-break changes the already labeled
factor `A` itself.  Its validity is never in question, and the exact colors
that can be lost are confined to the cut seams.  The 290-mask completion has
therefore become a monotone colored-word reconnection problem rather than a
central-path-plus-pinning problem.

If zero-loss single moves stop existing, retain the same exact framework and
use a beam of depth two: permit the first move to lose at most `d` protected
colors, then require the second move to restore all of them and gain the
target.  The state carried by the beam is only the sparse color-defect set,
not a SAT core.
