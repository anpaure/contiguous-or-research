# Every linearization of the reset--return cycle has quadratic short-OR collateral

**Date:** 2026-08-01  
**Status:** unconditional uniform lower-bound theorem plus exact H100 census
through `d=30`.  No cut of the complete-reversal reset cycle preserves its
internal cyclic OR deck.  Every cut loses at least

\[
                              d(2d-1)                       \tag{0.1}
\]

distinct values which have no other cyclic witness at all.  The sharper
full-loss formulas reported in Section 6 are exact finite census results,
not yet promoted to an all-`d` theorem.

This does not show that those targets are globally absent: an ambient
carrier may provide duplicate witnesses.  It shows that a safe cut cannot
be obtained from the packet's internal deck alone.

## 1. The maximal antecedent has a four-block normal form

Use the sharp-coordinate version of the resident complete-reversal cycle:

\[
                   r=2d+1,\qquad k=4d+2.                   \tag{1.1}
\]

Let

\[
 X=\{x_1,\ldots,x_d\},\qquad
 C=\{c_1,\ldots,c_d\},                                   \tag{1.2}
\]

and use two medium labels `delta,alpha` and two singleton banks

\[
 U=\{u_1,\ldots,u_d\},\qquad
 Y=\{y_1,\ldots,y_d\}.                                   \tag{1.3}
\]

For the construction in
`MATH_THEOREM_RESET_RETURN_RAIL_COMPLETE_REVERSAL_GUARDED_CYCLE_20260801.md`,
these labels are, explicitly,

\[
 c_j=z_{j-1},\quad \delta=z_d,\quad
 u_j=z_{d+j},\quad \alpha=z_{2d+1},                       \tag{1.4}
\]

while `x_j` are the selected reset-core labels and `y_j` are the fresh
return labels.

### Theorem 1.1 (source normal form)

The maximal cyclic depth-`d` antecedent `A=(A_0,...,A_(4d+1))` is

\[
 A_t=\{\delta\}\cup\{x_1,\ldots,x_t\}
                  \cup\{c_{t+1},\ldots,c_d\}
                  \qquad(0\le t\le d),                   \tag{1.5}
\]

\[
 A_{d+j}=X\cup\{u_j\}
                  \qquad(1\le j\le d),                   \tag{1.6}
\]

\[
 A_{2d+1+s}=\{\alpha\}\cup\{x_{s+1},\ldots,x_d\}
                         \cup\{c_1,\ldots,c_s\}
                  \qquad(0\le s\le d),                   \tag{1.7}
\]

and

\[
 A_{3d+1+j}=C\cup\{y_j\}
                  \qquad(1\le j\le d).                   \tag{1.8}
\]

Every `A_i` has rank `d+1`, and successive terms differ by one exchange.
Every ground coordinate enters exactly once around the cycle.

#### Proof

Intersect the `d+1` consecutive root sets ending at each position in the
explicit reset path and return rail.  During the first block the retained
reset seam is changed successively from `C` to `X`, giving (1.5).  The
first singleton bank gives (1.6).  The return half changes `X` back to `C`,
giving (1.7), and the second singleton bank gives (1.8).

The displayed sets all have rank `d+1`.  Their transitions are

\[
 c_j\mapsto x_j,quad
 \delta\mapsto u_1\mapsto\cdots\mapsto u_d\mapsto\alpha,
\]

\[
 x_j\mapsto c_j,quad
 \alpha\mapsto y_1\mapsto\cdots\mapsto y_d\mapsto\delta.
\]

Thus every transition is Johnson and every coordinate is inserted once.
Direct substitution in the maximal-erosion definition proves that these
are exactly its cells. \(\square\)

If the reset core has `h>=0` additional permanent coordinates, the same
formulas hold with one common `h`-set added to every `A_i`.  This changes
all ranks by `h` but changes no equality, witness, or loss count below.

## 2. Positive and zero runs in the source word

From (1.5)--(1.8):

* each `x_j` and `c_j` has one positive run of length `2d+1`;
* `delta` and `alpha` have positive runs of length `d+1`; and
* every `u_j` and `y_j` has a singleton positive run.

Since the cycle length is

\[
                              M=4d+2,                       \tag{2.1}
\]

every coordinate has a zero run of length at least

\[
                              2d+1.                         \tag{2.2}
\]

This separation is the source of the unavoidable cut collateral.

## 3. Short cyclic intervals have globally unique OR-values

### Lemma 3.1 (short-interval injectivity)

Let

\[
 I(s,w)=A_s,A_{s+1},\ldots,A_{s+w-1}
\]

be a cyclic source interval.  For every

\[
                              1\le w\le2d,                 \tag{3.1}
\]

its union has rank

\[
                              d+w,                          \tag{3.2}
\]

and the map

\[
                    (s,w)\longmapsto\bigcup I(s,w)         \tag{3.3}
\]

is injective.  Its value has no witness of any other width either.

#### Proof

Let `e_i` be the coordinate inserted when passing from `A_(i-1)` to
`A_i`.  By Theorem 1.1 the `e_i` are all distinct.  By (2.2), `e_i` is
absent from the preceding `2d+1` source cells.

Starting with `A_s`, each extension to `A_(s+j)`, `1<=j<w`, therefore
adds the new coordinate `e_(s+j)`, which was absent from every earlier
cell of the interval.  This proves (3.2).  In particular equal unions must
have equal widths.

Now suppose two width-`w` intervals have distinct starts.  Rotate the
indices, and if necessary exchange the two intervals, so their starts are
`0` and `h` with

\[
                         1\le h\le M/2=2d+1.               \tag{3.4}
\]

Because `w<=2d`, neither displayed interval wraps in this indexing.

If `h>=w`, the coordinate `e_h` belongs to the second interval and is
absent from the first by its preceding zero run.  If `h<w`, the coordinate
`e_w` belongs to the second interval and is absent from the first.  The
unions are different in either case.  This proves injectivity.

Finally (3.2) distinguishes all other widths up to `2d`; a wider interval
contains its first `2d` cells plus at least one further entering coordinate,
so it has rank greater than `3d` and cannot equal a short value. \(\square\)

## 4. Every cut loses a closed-form quadratic family

Fix any cut between `A_(c-1)` and `A_c`, and linearize the word there.  For
a fixed width `w`, exactly `w-1` cyclic intervals of width `w` cross the
cut.  When `2<=w<=2d`, Lemma 3.1 says that all these values are globally
unique in the cyclic word.  Therefore none has a noncrossing internal
witness after the cut.

### Theorem 4.1 (uniform cut collateral)

Every linearization loses at least

\[
 \sum_{w=2}^{2d}(w-1)
       =\binom{2d}{2}
       =d(2d-1)                                            \tag{4.1}
\]

distinct cyclic interval-OR values.  Each lost value in this family had
exactly one cyclic witness.

If the owner rank is `r=2d+1+h`, the guaranteed family has rank histogram

\[
 \begin{array}{c|c}
 \text{rank}&\text{number of forced losses}\\ \hline
 r-d+t&t
 \end{array}
 \qquad(1\le t\le2d-1).                                  \tag{4.2}
\]

#### Proof

The count and nonrecoverability are the preceding paragraph.  Every source
cell has rank `r-d`; putting `w=t+1` in (3.2) gives rank `r-d+t`, proving
(4.2). \(\square\)

Since `d=Theta(sqrt(k))`, (4.1) is `Theta(k)`.  Thus no choice of a single
cut can leave only `O(1)` internally unsupported values.

## 5. What the theorem rules out

The complete-reversal construction remains an exact cyclic two-phase
packet.  Theorem 4.1 rules out the stronger hope that one could simply cut
that packet at a favourable boundary and rely on duplicate witnesses
elsewhere inside the same packet.

A successful global host must do at least one of the following:

1. reserve ambient witnesses for the forced family (4.2);
2. reverse a compatible exterior socket together with the packet;
3. splice through a second packet whose crossing deck supplies the missing
   values; or
4. use a non-linear component contraction in which the cyclic cells remain
   available.

The theorem does not say that the target values in (4.2) are globally
unique in a spanning carrier, so it is not an impossibility theorem for a
protected host or for `nu(k)<=B(k)+O(1)`.

## 6. Exact finite census through depth 30

The independent H100 audit

```text
scratch/audit_reset_return_rail_linearization_20260801.cpp
```

enumerates every cyclic interval value, every possible cut, and every
noncrossing linear witness for the sharp source word.  It proves the
uniform short-family assertions directly and, for every `1<=d<=30`, finds
the stronger exact pattern

\[
 |\operatorname{Deck}_{\rm cyc}(A)|=10d^2+10d+3,           \tag{6.1}
\]

\[
 \min_c\operatorname{lost}(c)=\frac{d(7d+1)}2,
 \qquad
 \max_c\operatorname{lost}(c)=\frac{d(7d+3)}2.            \tag{6.2}
\]

There are `2d` minimum-loss cuts and `2d+2` maximum-loss cuts; no other
loss class occurs.  With the indexing of (1.5)--(1.8), the minimum cuts are

\[
 \{1,\ldots,d\}\cup\{2d+2,\ldots,3d+1\}.                 \tag{6.3}
\]

For one minimum cut the complete loss histogram is

\[
 \#\text{losses of rank }s=
 \begin{cases}
 s-d-1,&d+2\le s\le3d+1,\\
 s-2d-2,&3d+2\le s\le4d+1,\\
 0,&\text{otherwise}.
 \end{cases}                                               \tag{6.4}
\]

The program asserts all formulas (6.1)--(6.4), but the present note uses
them only as an exact finite census.  A uniform proof of the additional
long-interval contribution in (6.2) would require a full four-block deck
classification and is not needed for Theorem 4.1.

Compiled and run on H100 with `g++ -std=c++20 -O3`, the retained verdict is

```text
PASS_RESET_RETURN_RAIL_LINEARIZATION d=1..30 sharp_core cyclic=10d^2+10d+3 short_unique=M(2d) every_cut_short_collateral=d(2d-1) observed_min=d(7d+1)/2 observed_max=d(7d+3)/2 best_cut_count=2d worst_cut_count=2d+2 no_safe_cut
```

The transcript is retained at

```text
scratch/audit_reset_return_rail_linearization_20260801.out
```

## 7. Updated frontier

The local reset packet now has a clean dichotomy.

* **Cyclic phase trade:** exact, resident, all-depth, and literal.
* **Bare linear opening:** necessarily loses at least `d(2d-1)` internally
  unique short-interval values.

Therefore the next gate is not “find the right cut.”  It is a
**duplicate-witness protected host** or a **phase-reflected exterior socket**
for the explicit rank-graded family (4.2), together with the already-open
common residual compiler and coefficient-one owner planting.

