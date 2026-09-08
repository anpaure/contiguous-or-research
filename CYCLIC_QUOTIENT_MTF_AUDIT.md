# Cyclic-quotient SCDs versus exact move-to-front dynamics

This note audits the following tempting route to

\[
  \nu(n)=(1+o(1))W(n),\qquad
  W(n)=\binom{n}{\lfloor n/2\rfloor}.
\]

Hersh and Schilling give an explicit symmetric-chain decomposition of the
necklace quotient `B_n/C_n` (equivalently, of binary necklaces ordered by
inclusion up to rotation):

> P. Hersh and A. Schilling, *Symmetric Chain Decomposition for Cyclic
> Quotients of Boolean Algebras and Relation to Cyclic Crystals*, IMRN 2013,
> 463--473, arXiv:1107.4073.

The attractive plan is to lift each quotient chain to `n` rotated chains in
`B_n`, thread those rotations by one move-to-front update apiece, and pay one
reset per quotient chain.  Since there are about `W(n)/n` quotient chains and
a typical first state has `O(sqrt(n))` blocks, this would have the ideal reset
ledger `O(W/sqrt(n))=o(W)`.

The first, lifting, part really does work after an `o(W)` deletion.  The
second, MTF-threading, part fails on `1-o(1)` of the lifted chains.  The
obstruction is independent of the particular Hersh--Schilling SCD: it applies
to every SCD lifted in parallel by coordinate rotations.

## 1. A quotient SCD lifts after negligible periodic loss

Let `sigma` be the cyclic permutation of `[n]`.  Call a subset *aperiodic* if
its `sigma`-orbit has size `n`.

### Lemma 1 (periodic words are negligible)

The number of periodic binary words of length `n` is at most

\[
  n2^{n/2}=o(W(n)).                                      \tag{1.1}
\]

#### Proof

A periodic word has a proper period `d|n`, hence `d<=n/2`, and is determined
by its first `d` letters.  Summing the crude bound `2^d` over proper divisors
gives at most `n2^(n/2)`.  Since `W(n)=Theta(2^n/sqrt(n))`, this is `o(W)`.
QED.

### Lemma 2 (aperiodic quotient-chain lift)

Let

\[
  [S_0]<[S_1]<\cdots<[S_h]                         \tag{1.2}
\]

be a saturated chain in `B_n/C_n`, and suppose every necklace in it is
aperiodic.  One can choose representatives

\[
  S_0'\subset S_1'\subset\cdots\subset S_h'          \tag{1.3}
\]

such that the `n` chains

\[
  \sigma^tS_0'\subset\sigma^tS_1'\subset\cdots
       \subset\sigma^tS_h',\qquad t\in\mathbb Z_n,   \tag{1.4}
\]

are pairwise disjoint.

#### Proof

Choose `S_0'` arbitrarily.  A quotient cover `[S_i]<[S_(i+1)]` means that
some representatives are related by an ordinary cover.  Rotating that pair
so that its lower member is the already chosen `S_i'` chooses `S_(i+1)'` and
gives (1.3).  If two chains or two ranks in (1.4) met, equality of ranks first
forces the same `i`, and then aperiodicity forces the same rotation `t`.
QED.

### Corollary 3 (near-complete rotation-bundled SCD)

From any SCD of `B_n/C_n`, in particular the Hersh--Schilling SCD, delete
every quotient chain containing a periodic necklace and lift all remaining
chains as in Lemma 2.  The result is a disjoint symmetric-chain cover of all
but `o(W(n))` Boolean masks, containing `W(n)-o(W(n))` chains.

#### Proof

The number of bad quotient chains is at most the number of periodic
necklaces, hence at most `n2^(n/2)`.  A quotient chain has at most `n+1`
necklaces and each necklace has at most `n` representatives, so deleting all
bad chains loses at most `O(n^3 2^(n/2))=o(W)` masks.  Every SCD chain has one
member in the lower middle rank, so the surviving lifted cover has
`W-o(W)` chains.  QED.

This establishes that periodic stabilizers are not the real obstruction.

## 2. A three-minimum obstruction for exact MTF composition

A saturated symmetric chain is written

\[
 C=(B,\ B+e_1,\ldots,B+e_1+\cdots+e_h),             \tag{2.1}
\]

where `B` is its minimum.  An ordered partition `Pi` *exposes* `C` when all
members of `C` are prefix unions of `Pi`.  For a nonempty update mask `X`,

\[
 M_X(R_1,\ldots,R_s)
   =(X,R_1-X,\ldots,R_s-X),                          \tag{2.2}
\]

after empty blocks are deleted.

The following lemma uses only the exact MTF rule.  It does not assume
singleton states, full-minimum updates, or a particular SCD.

### Theorem 4 (three-minimum obstruction)

Let `C_0,C_1,C_2` be three nontrivial saturated chains with distinct minima
`B_0,B_1,B_2` of the same cardinality.  Suppose there are exposing states
`Pi_i` and nonempty masks `X_1,X_2` with

\[
  \Pi_1=M_{X_1}(\Pi_0),\qquad
  \Pi_2=M_{X_2}(\Pi_1).                              \tag{2.3}
\]

Then

\[
  \boxed{|B_1\setminus(B_0\cup B_2)|\le1.}           \tag{2.4}
\]

#### Proof

Because `Pi_1` exposes `C_1`, its new first block satisfies
`X_1 subseteq B_1`.  Delete `X_1` from `Pi_0`.  Both `B_0-X_1` and
`B_1-X_1` are prefix unions of the same residual ordered partition: the
first because `Pi_0` exposes `C_0`, and the second because `Pi_1` exposes
`C_1`.  They are therefore comparable.

The inclusion `B_0-X_1 subseteq B_1-X_1` would imply `B_0 subseteq B_1`,
because `X_1 subseteq B_1`; equal cardinalities would then give `B_0=B_1`,
contrary to the hypothesis.  Hence

\[
  B_1-X_1\subseteq B_0-X_1,
  \qquad	ext{so}qquad B_1\setminus B_0\subseteq X_1. \tag{2.5}
\]

Now perform the second update.  Its new block satisfies
`X_2 subseteq B_2`.  The old first block becomes `X_1-X_2` and is the first
surviving residual block.

If `X_2` is a proper subset of `B_2`, the remaining minimum
`B_2-X_2` must be completed before any element outside `B_2` appears.
Consequently `X_1-X_2 subseteq B_2`, and hence `X_1 subseteq B_2`.

If `X_2=B_2`, the target minimum is complete in the new first block.  Since
`C_2` is nontrivial, the next prescribed prefix differs from `B_2` by one
singleton increment.  Therefore the first residual block `X_1-B_2` is
either empty or that singleton.  In both cases

\[
  |X_1\setminus B_2|\le1.                            \tag{2.6}
\]

Combining (2.5) and (2.6) gives (2.4).  QED.

The point is block coalescence.  The first transition must update every new
element of the middle minimum `B_1`; those elements become one tied block.
The next transition can lose at most one element of that block outside its
new minimum, because the next chain grows by singleton increments.

## 3. Almost no set satisfies the necessary rotation condition

For distinct nonzero residues `a,b in Z_n`, define

\[
 \mathcal E_{a,b}
   =\{B\subseteq\mathbb Z_n:
       |B\setminus(\sigma^aB\cup\sigma^bB)|\le1\}.   \tag{3.1}
\]

### Theorem 5 (exponential rarity)

Uniformly over all distinct nonzero `a,b`, the union of these exceptional
families satisfies

\[
 \left|\bigcup_{a,b}\mathcal E_{a,b}\right|
 \le n^2 2^n\left(1+\frac n7\right)
             \left(\frac78\right)^{n/27}
 =o(W(n)).                                           \tag{3.2}
\]

#### Proof

Fix `a,b`.  For each `i`, consider the three-set

\[
  Q_i=\{i,i-a,i-b\}.                                 \tag{3.3}
\]

Its three vertices are distinct.  An underlying three-set can occur as at
most three of the `Q_i`, so there are at least `n/3` distinct triples.  Each
coordinate lies in at most three triples.  Greedily choosing a triple and
deleting every intersecting triple therefore gives a disjoint subfamily of
size

\[
  L\ge n/27.                                         \tag{3.4}
\]

For the distinguished index `i` of one selected triple, the event

\[
  i\in B,\qquad i-a\notin B,\qquad i-b\notin B       \tag{3.5}
\]

is exactly one of the eight assignments on that triple.  The selected
triples are disjoint, so requiring at most one event (3.5) among them leaves
at most

\[
  2^{n-3L}\bigl(7^L+L7^{L-1}\bigr)
  =2^n(7/8)^L(1+L/7)                                 \tag{3.6}
\]

binary words.  Use `L>=n/27` and `L<=n`, and sum over fewer
than `n^2` ordered choices `(a,b)`.  The exponential factor dominates the
polynomial, while `W(n)=Theta(2^n/sqrt(n))`.  QED.

### Corollary 6 (rotation bundles have linearly many MTF components)

Consider any rotation-lifted SCD cover with `W-o(W)` nontrivial chains, and
require every genuine MTF state path to remain inside one rotation bundle.
Then every such path cover has at least

\[
  (1/2-o(1))W(n)                                     \tag{3.7}
\]

components.

#### Proof

In a path containing three distinct rotations, translate the middle
rotation to zero.  Theorem 4 says its minimum belongs to some
`E_(a,b)`.  By Theorem 5, only `o(W)` of the distinct chain minima are
exceptional.  Every nonexceptional chain can therefore occur only as an
endpoint of its path.  A path has two endpoints, giving (3.7).  The
radius-zero chains in even dimension and the unique chain with empty
minimum together number only `o(W)` and do not affect the estimate.  QED.

Every ordered partition exposing a chain other than the one-set chain
`{[n]}` has at least two blocks.  Hence the exact reset ledger

\[
  N-p+\sum_{j=1}^p s_j
\]

has excess at least `p-O(1)=Omega(W)` on this path cover.  Thus the literal
quotient-chain/rotation-bundle route cannot prove a constant-one upper bound.

## 4. A small explicit Hersh--Schilling obstruction

The first useful example already occurs for six coordinates.  In the
Hersh--Schilling cyclic bracketing, the Lyndon word

\[
  110110
\]

has unmatched `1` positions `2,5`.  Their lowering map gives the quotient
chain

\[
 [100100]\ <\ [110100]\ <\ [110110].                \tag{4.1}
\]

A nested representative has flag

\[
 B=\{1,4\},\qquad (e_1,e_2)=(2,5),\qquad
 Z=\{3,6\}.                                         \tag{4.2}
\]

It has three distinct coordinate rotations.  Their minima are

\[
  \{1,4\},\qquad\{2,5\},\qquad\{3,6\}.              \tag{4.3}
\]

For any ordering of these three chains, the middle minimum has two elements
outside the union of the other two minima.  Theorem 4 therefore forbids a
genuine three-state MTF path through all three rotations.  At least two MTF
components are necessary even though the quotient chain itself is perfectly
valid.

This example also displays why an existential quotient-chain arc is not
composable.  A transition into one rotated chain must coalesce both new
minimum elements; the next rotated chain needs those two elements separated
as its two singleton increments.

## 5. What survives

The cyclic quotient remains useful in exactly one sense: Corollary 3 gives a
canonical near-complete SCD whose chains are organized into only `W/n`
rotation bundles.  But the coordinate rotations cannot themselves be used
as the one-step MTF threading.

Any successful use of the quotient must add genuinely new information.  For
example, it could use the quotient chains merely as indices and connect
states belonging to *different* rotation bundles, or assign unrelated
ground-set orders to the rotation indices.  Such a construction is no
longer supplied by the Hersh--Schilling quotient theorem.  The necessary
three-minimum condition for any proposed state path is always

\[
  |B_i\setminus(B_{i-1}\cup B_{i+1})|\le1,           \tag{5.1}
\]

apart from trivial target chains.  Thus a global MTF construction must order
chain minima so that almost every minimum is nearly covered by its two
neighbors.  This is a concrete new design constraint, and not a property of
literal coordinate-rotation orbits.
