# Exact strong-GK transitions and the one-reset macro core

**Status (2026-08-21).**  The transition theorem and the macro-core
reduction below are proved.  They isolate a serious new obstruction to
concatenating the otherwise large family of length-`b` compatible FIFO
paths: after one reset per macro is imposed cyclically, only the directed
cycle support of one explicit finite graph is usable.  Exact H100 data
through `b=6` show that this support is tiny.

The remaining asymptotic step is stated separately as Conjecture 4.1.  It
is not used as a theorem here.  If proved, it would show that this exact
one-reset route has linear source loss.  Nothing below rules out two or
more reset letters per macro, nonperiodic macro lengths, a different SCD,
or a physical compiler which preserves active claims across a seam.

## 1. Prefix-walk notation

Fix a balanced zero--one word of length `2b`, with its `b` one-positions
forming the middle source `S`.  Put

\[
 h(t)=\#\{i\le t:i\in S\}-\#\{i\le t:i\notin S\},
 \qquad k=-\min_t h(t).                              \tag{1.1}
\]

For `1<=j<=k`, let

\[
 z_j=\min\{t:h(t)=-j\}.                              \tag{1.2}
\]

These are exactly the unmatched zero positions, from left to right.  The
upper Greene--Kleitman additions are therefore

\[
 a_i(S)=z_{k-i+1}\quad(1\le i\le k).                 \tag{1.3}
\]

Write

\[
 L(S)=\max\{t:h(t)=-k\}                              \tag{1.4}
\]

for the last return to the global minimum.  If `k>0`, then
`a_1(S)<max S`: after the first global minimum the balanced walk must use
a later one in order to return to height zero.

Given `x in S`, make the forced first-successor exchange

\[
 S'=S-\{x\}+\{a_1(S)\}.                              \tag{1.5}
\]

Call (1.5) **strong** when the complete common surviving GK prefix agrees:

\[
 (a_1(S'),\ldots,a_c(S'))
   =(a_2(S),\ldots,a_{c+1}(S)),
 \quad c=\min\{k(S'),k(S)-1\}.                       \tag{1.6}
\]

For `k=1`, (1.6) is empty and the single claimed addition has already been
emitted.

## 2. Exact strong-transition theorem

### Theorem 2.1

If `k(S)>=2`, (1.5) is strong if and only if exactly one of the following
two extreme conditions holds:

\[
 \begin{array}{lll}
 \text{left/up:}   &x<z_1=a_k(S),& k(S')=k(S)+1,\\
 \text{right/down:}&x>L(S),      & k(S')=k(S)-1.
 \end{array}                                           \tag{2.1}
\]

There is no strong exchange with `z_1<x<=L(S)`.  For `k(S)=1`, every
exchange is strong in the vacuous sense of (1.6); more precisely,

\[
 \begin{array}{c|c}
 x<z_1 & k(S')=2,\quad a_1(S')<a_1(S),\\
 x>z_1,\ x>L(S)& k(S')=0,\\
 x>z_1,\ x<L(S)& k(S')=1,\quad a_1(S')>a_1(S).
 \end{array}                                           \tag{2.2}
\]

#### Proof

Changing `x` from one to zero and `z_k` from zero to one changes the
prefix walk by

\[
 h'(t)-h(t)=
 \begin{cases}
 -2,&x\le t<z_k,\quad x<z_k,\\
 +2,&z_k\le t<x,\quad z_k<x,\\
 0,&\text{otherwise}.
 \end{cases}                                           \tag{2.3}
\]

Suppose first that `x<z_1`.  Before `z_1` the old walk is nonnegative.
Between `x` and `z_1` the shifted walk creates two new negative ladder
levels by the time `z_1` is reached; then every old ladder point `z_j`,
`1<=j<=k-1`, creates the level two below its old one.  Hence the new
minimum is `-(k+1)` and the deepest
`k-1` new ladder positions, in reverse order, are

\[
 z_{k-1},z_{k-2},\ldots,z_1.                         \tag{2.4}
\]

This is exactly the old surviving addition list.

If instead `z_j<x<z_{j+1}` for some `1<=j<k`, the shift in (2.3) starts
inside the old ladder.  The deep new ladder list initially contains
`z_{k-1},...,z_{j+1}`, but it then contains one of the two newly inserted
ladder positions before it reaches `z_j`.  Thus it disagrees with
`z_{k-1},...,z_{j+1},z_j` within the first `k-1` entries.  This proves both
the left implication and the exclusion of every interior `x<z_k`.

Now suppose `x>z_k`.  Before `z_k` the minimum is `-(k-1)`, and on
`[z_k,x)` the shift in (2.3) raises the old walk.  If `x>L(S)`, the suffix
from `x` onward never returns to `-k`; the new minimum is therefore
`-(k-1)`, with ladder positions `z_1,...,z_{k-1}`.  This gives the full
surviving list (2.4).  If `x<L(S)`, the suffix does return to `-k`.
Its first such return becomes the new deepest ladder point, so the new
first addition lies strictly to the right of `z_k` and already disagrees
with `z_{k-1}`.  This proves (2.1).  The same walk calculation with `k=1`
gives the three cases in (2.2).  \(\square\)

### Corollary 2.2 (shape of a strong FIFO path)

Along a strong FIFO path, `k` changes by one at every state with `k>=2`.
The emitted first additions strictly decrease except at a `k=1` to `k=1`
transition.  At such a flat transition, if `x` is the dropped coordinate,

\[
             a_1(S)<x<a_1(S').                       \tag{2.5}
\]

Thus every increase in the emitted coordinate sequence is an already
retired `k=1` seam.  This does not by itself prove the empirical
`3(b-1)` maximum strong-path length.

## 3. Exact length-`b` macro graph

An ordered FIFO state is a tuple of `b` distinct coordinates.  A
**length-`b` macro** has `b` source states and `b-1` consecutive strong
transitions.  Write its start as

\[
 q=(p_1,\ldots,p_{b-1},R)=(P,R).                     \tag{3.1}
\]

If its forced additions are `F=(f_1,...,f_(b-1))`, FIFO gives the exact
endpoint

\[
                   q_{\rm end}=(R,F).                \tag{3.2}
\]

One arbitrary reset transition drops `R` and appends a coordinate `R'`
not in `F`, so the next macro start must be

\[
                        (F,R').                       \tag{3.3}
\]

This defines a finite directed graph `G_b`:

* vertices are ordered starts (3.1) whose next `b-1` transitions are
  strong;
* `(P,R)->(F,R')` is an edge for every legal reset in (3.3) for which
  `(F,R')` is itself a vertex of `G_b`.

If dropping and immediately re-appending `R` is physically forbidden,
also require `R'!=R`.  A cyclic concatenation with exactly one reset after
every length-`b` macro uses only vertices lying in nontrivial strongly
connected components of `G_b` (or vertices with a self-loop).  Conversely,
every directed cycle in `G_b` is exactly such an ordered cyclic
concatenation.  This is an equivalence, not merely a necessary local test.

### Proposition 3.1 (maximum-label sentinel)

Let `m` be the largest coordinate which occurs anywhere in a cyclic macro
concatenation.  At every macro start `(P,R)`,

\[
                         m\notin P.                  \tag{3.4}
\]

Consequently, whenever `m` occurs it is the reset sentinel `R`.

#### Proof

By (3.3), every entry of `P` was a forced first addition during the
preceding macro.  Every such addition is strictly below the maximum of its
source, by the observation after (1.4), and that maximum is at most `m`.
Thus no forced addition equals `m`.  \(\square\)

The point of (3.2)--(3.4) is that a near-perfect set packing of abstract
length-`b` source paths says nothing about reset linkage.  Only the cyclic
support of `G_b` can participate in this exact one-reset compiler.

## 4. The remaining normal-form gate

For an ordered prefix `P=(p_1,...,p_(b-1))`, split it at every index for
which `p_(i+1)!=p_i-1`.  Call the resulting pieces its **descending
coordinate intervals**.

### Conjecture 4.1 (three-interval recurrent normal form)

Every vertex `(P,R)` on a directed cycle of `G_b` has at most three
descending coordinate intervals in `P`.

This statement is deliberately not promoted to a lemma.  It is exact in
the exhaustive range in Section 5.  A proof would immediately give the
desired asymptotic obstruction: a prefix with at most three intervals is
specified by at most six interval endpoints and their order, and the
sentinel has `2b` choices.  Hence the number of recurrent ordered macro
states would be `O(b^7)`, and all their macros together would contain at
most `O(b^8)=o(binomial(2b,b))` middle sources.  An exact one-reset cyclic
compiler would then leave `(1-o(1))W_b`, not merely a positive fraction.

The conjecture concerns fixed length `b` and one reset per macro.  Even its
proof would not imply a no-go for variable macro lengths or two-letter
reset collars.

## 5. Exact finite audit

The script

`scratch/research_gk_length_b_macro_reset_core_20260821.py`

constructs every ordered macro, every reset edge, and the exact SCC cycle
support.  It also verifies (3.4) and records the interval-run histogram.
With same-sentinel reset allowed, the results are

\[
\begin{array}{c|rrrrr}
b&2&3&4&5&6\\ \hline
|V(G_b)|&8&54&526&6496&99516\\
\text{cycle-supported vertices}&5&8&17&33&54\\
\text{sources in their macros}&6&11&33&69&108.
\end{array}                                           \tag{5.1}
\]

The interval-run histograms at `b=5,6` are respectively

\[
       \{1:8,2:21,3:4\},\qquad \{1:9,2:36,3:9\}.     \tag{5.2}
\]

When `R'=R` is forbidden, the exact cycle support is still smaller.  These
finite values motivate Conjecture 4.1; they do not prove it.
