# Exact bridges and cyclic closure for the tail move-to-front walk

**Status (2026-08-21).**  The bridge, padding, rigidity, and cyclic-closure
statements below are proved.  They remove endpoint return and cyclic seam
closure as obstructions for the eligible-walk program.  They do **not** prove
that the available fixed-endpoint trajectory palette can be selected to cover
a `1-o(1)` fraction of any rank, let alone all ranks in the central band.

## 1. Model

Let a state be a permutation

\[
\pi=(\pi_1,\ldots,\pi_n),
\]

listed from most to least recent.  Fix an eligibility floor `f` with
`1<=f<=n-1`, and put `d=n-f+1>=2`.  For `f<=j<=n`, let

\[
T_j(\pi_1,\ldots,\pi_n)
 = (\pi_j,\pi_1,\ldots,\pi_{j-1},
    \pi_{j+1},\ldots,\pi_n).
\]

Thus `T_j` records the letter currently in position `j` and moves it to the
front.  A legal tail-MTF trajectory is a word in the operators
`T_f,T_{f+1},...,T_n`.  Function composition below is read right to left, so
`T_{i+1}^i compose T_i` means that chronologically one first applies `T_i`
and then applies `T_{i+1}` exactly `i` times.

If a letter is recorded at times `s<t`, then

\[
t-s\ge f. \tag{1.1}
\]

Indeed it is moved to position one at time `s`; every intervening legal move
pushes it down by exactly one position until it can first reach position `f`.

## 2. Polynomial directed diameter

### Theorem 2.1 (explicit directed connector)

For any two states `pi,tau`, there is a legal directed tail-MTF trajectory
from `pi` to `tau` of length strictly less than `n^3`.

#### Proof

Each `T_j` is a `j`-cycle on the first `j` positions, hence

\[
T_j^j=I,\qquad T_j^{-1}=T_j^{j-1}. \tag{2.1}
\]

For every `f<=i<n`, define

\[
S_i:=T_{i+1}^{i}\circ T_i.
\]

The first move takes the entry in position `i` to the front; the following
`i` copies of `T_{i+1}` apply `T_{i+1}^{-1}` and put that entry into position
`i+1`.  Directly,

\[
S_i(x_1,\ldots,x_n)
=(x_1,\ldots,x_{i-1},x_{i+1},x_i,x_{i+2},\ldots,x_n). \tag{2.2}
\]

So `S_i` is the adjacent transposition of positions `i,i+1`, expressed by a
legal directed word of length `i+1<=n`.

Put `h=f+1` and `C=T_f`.  The operator `C` cyclically permutes the first `f`
positions.  The conjugates

\[
C^{-a}\circ S_f\circ C^a,\qquad 0\le a<f, \tag{2.3}
\]

are exactly the star transpositions `(j,h)`, `1<=j<=f`.  When `a>0`, replace
`C^{-a}` by the legal positive word `C^{f-a}`.  Hence every star
transposition has a legal directed realization of length at most
`2f+1<=2n-1`.

Consider the tree on the position set `[n]` with edges

\[
\{(j,h):1\le j\le f\}
\quad\text{and}\quad
\{(i,i+1):h\le i<n\}. \tag{2.4}
\]

Every edge transposition of this tree therefore has a legal realization of
length at most `2n-1`.  Edge transpositions of a tree generate `S_n`.
More quantitatively, the usual leaf-fixing procedure transforms any
permutation into any other using at most

\[
(n-1)+(n-2)+\cdots+1=\frac{n(n-1)}2
\]

tree-edge transpositions: bring the correct token to a leaf along the unique
path in the remaining tree, fix that leaf, and continue.  The resulting
legal word has length at most

\[
(2n-1)\frac{n(n-1)}2<n^3.
\]

This word acts on the positions of `pi` by the unique permutation carrying
it to `tau`.  Therefore it is the required directed connector.  ∎

### Theorem 2.2 (one common exact bridge length)

Set

\[
R(n,f):=n^3+f^2. \tag{2.5}
\]

Every ordered pair of states `pi,tau` is joined by a legal tail-MTF
trajectory of **exactly** `R(n,f)` steps.

#### Proof

Take a connector of length `ell<n^3` from Theorem 2.1.  Both
`T_f^f` and `T_{f+1}^{f+1}` are legal identity words, of lengths `f` and
`f+1`.  Every integer `q>=f(f-1)` has the form

\[
q=af+b(f+1),\qquad a,b\ge0. \tag{2.6}
\]

For completeness, write `q=sf+r`, `0<=r<f`; the hypothesis gives
`s>=f-1>=r`, and then `q=(s-r)f+r(f+1)`.

Here `R(n,f)-ell>f^2`, so append the corresponding number of the two
identity loops at `tau`.  The padded connector has exactly `R(n,f)` steps.
∎

### Corollary 2.3 (full fixed-endpoint free-prefix palette)

Fix states `pi,tau` and an integer `a>=0`.  Every legal `a`-step prefix from
`pi` extends to an `(a+R(n,f))`-step trajectory from `pi` to `tau`.
Consequently there are at least `d^a` distinct access words of this common
length and with these common endpoints.

#### Proof

After the arbitrary prefix, apply Theorem 2.2 from its terminal state to
`tau`.  There are exactly `d` legal position choices at every prefix step,
and the first different position choice records a different letter, so the
`d^a` prefix access words are distinct.  ∎

Thus prescribed endpoints cost only the polynomial terminal budget `R`; if
`a/R -> infinity`, an asymptotic fraction `1-o(1)` of a bridge can be chosen
as an entirely unrestricted eligible trajectory.  This is an entropy and
localization statement, not a coverage-selection theorem.

## 3. Endpoint rigidity and the first diamond

### Proposition 3.1 (rigid terminal collar)

Let two legal trajectories have the same initial state, the same terminal
state, and the same length `b`.

1. If `b<=f`, their access words are identical.
2. If `b>=f`, their last `f` recorded letters are identical.
3. For any `k<=f`, among the `b` post-move top-`k` observations, at most

   \[
   \max\{0,b-f+k-1\} \tag{3.1}
   \]

   positions can differ between the two trajectories.

#### Proof

By (1.1), any `f` consecutive recorded letters are distinct.  Therefore the
last `min(b,f)` recorded letters occur, in reverse chronological order, in
the first `min(b,f)` positions of the terminal recency permutation.  The
terminal state fixes those letters.  This proves the first two claims.

If `b<=f`, the first claim and the common initial state make the two
trajectories identical, so no observation differs.  When `b>=f`, the common
suffix begins at time `b-f+1`.  After `k` letters of
that suffix have been recorded, the top `k` positions depend only on those
common letters.  Thus every observation from time `b-f+k` onward is fixed,
leaving at most (3.1) potentially variable observations.  ∎

In particular, sub-`f` fixed-endpoint blocks have no resampling entropy.
The first nontrivial fixed-endpoint switch occurs at length `f+1`.

### Proposition 3.2 (universal length-`f+1` diamond)

Write an arbitrary state as

\[
\pi=(p_1,\ldots,p_{f-1},q_1,q_2,\ldots,q_d).
\]

The two access words

\[
q_1,p_{f-1},\ldots,p_1,q_1
\quad\text{and}\quad
q_2,p_{f-1},\ldots,p_1,q_1 \tag{3.2}
\]

are legal, have length `f+1`, and have the same terminal state

\[
(q_1,p_1,\ldots,p_{f-1},q_2,\ldots,q_d). \tag{3.3}
\]

#### Proof

The first letter in either word starts in the eligible tail.  After that
move, `p_{f-1}` is in position `f`; moving it to the front puts
`p_{f-2}` in position `f`, and so on.  The final `q_1` is eligible in both
branches.  Formula (3.3) follows either by direct replay or by ordering the
accessed letters by their last occurrence.  ∎

This diamond changes only its first recorded letter.  Consequently it can
alter at most `k` rank-`k` observations.  The proposition is useful as a
minimal absorber, but a tiling by such diamonds exposes only `O(1)` offers
per target on average at total length `Theta(M)`; by itself it does not
establish a vanishing covering defect.

There is also a `d`-way version of length `f+d=n+1`: for any `1<=j<=d`,

\[
q_j,p_{f-1},\ldots,p_1,q_1,q_2,\ldots,q_d \tag{3.4}
\]

is legal, and all `d` choices have the same endpoint
`(q_d,\ldots,q_1,p_1,\ldots,p_{f-1})`.  It offers `d` alternatives for the
first `k` affected observations, but the remaining observations in the
gadget are common.  Hence this explicit palette controls at most a
`k/(n+1)` fraction of its window positions (about one half at central
rank).  Long bridges from Corollary 2.3 are needed to make the controllable
fraction tend to one.

## 4. Cyclic closure is no longer an open endpoint gate

### Theorem 4.1 (polynomial cyclic closure)

Let `pi_0 -> pi_1 -> ... -> pi_L` be any legal tail-MTF trajectory.  There is
a legal continuation of fewer than `n^3` steps from `pi_L` back to `pi_0`.
The resulting closed trajectory gives a cyclic singleton word of length

\[
L+O(n^3) \tag{4.1}
\]

whose equal cyclic letters have separation at least `f`.

For every `k<=f`, all rank-`k` windows lying wholly inside the original
trajectory are retained; only the usual first `k-1` linear boundary
observations need be discarded before comparing a state observation with a
literal word window.

#### Proof

Apply Theorem 2.1 to `(pi_L,pi_0)` and append that connector.  Repeating the
closed operator word periodically is a legal bi-infinite tail-MTF
trajectory.  Inequality (1.1), applied to this periodic trajectory, gives
the cyclic equal-letter separation, including across the seam.  When
`k<=f`, every `k` consecutive recorded letters are distinct and form the
top-`k` recency set.  Appending a connector cannot destroy any original
internal window.  ∎

Because the middle-layer scale is exponential, `n^3=o(binom(n,floor(n/2)))`.
Thus, for ranks `k<=f`, any linear eligible trajectory giving a
coefficient-one or plateau statement can be made genuinely cyclic at
asymptotically zero length cost.
What remains open is finding the trajectory with summed central-band defect
`o(W)`; return to the starting recency state and the cyclic gap condition no
longer add an asymptotic obstruction.

## 5. What the bridge theorem does and does not give

The exact bridge theorem supports the following rigorous block reduction.
Partition a desired cyclic trajectory into blocks of length `a+R`, prescribe
the skeleton state at every block boundary, choose an arbitrary eligible
`a`-step prefix in every block, and close it to the next skeleton state.
The blocks then compose exactly, while the connector fraction is
`R/(a+R)`.  Taking `a/R -> infinity` makes this loss `o(1)`.

The unresolved selection problem is now clean: from the `d^a` prefix paths
in each block, select one per block so that their rank-window sets cover a
`1-o(1)` fraction of the relevant layers.  A direct invocation of a generic
hypergraph nibble is not yet justified.  A candidate path has at most `a`
distinct targets at one rank and at most order `a H` incidences across a band
of width `H`; only a useful low-repeat candidate would have matching lower
bounds.  Even in that regime, small pair codegrees alone do not imply an
almost-perfect matching when edge size grows (finite-projective-plane type
examples are the standard warning).  Moreover all candidates at one time
lie in a common Johnson fan, so their target labels are highly correlated
rather than independent uniform coupons.

Accordingly, the proved advance is:

1. exact polynomial connectivity and aperiodic padding;
2. asymptotically free fixed-endpoint localization;
3. genuine cyclic closure with the required gap floor;
4. a precise residual palette-selection/expansion problem.

It is **not** yet a proof of `1-o(1)` coverage.

## 6. Finite verification (H100 only)

An independent exhaustive replay on H100 checked:

- `T_j^j=I` and the adjacent-swap identity (2.2) on every permutation for
  all `2<=n<=7` and every `1<=f<n`;
- reachability of all `n!` states from the identity and the actual directed
  Cayley diameter for every `2<=n<=9` and every `1<=f<n`.
- legality and the common endpoint in the `d`-way gadget (3.4) on every
  permutation for all `2<=n<=8` and every `1<=f<n`.

The largest observed diameter was 30 (`n=9,f=8`), versus the proved bound
`n^3=729`.  These computations are sanity checks only; the theorems above
are established by the explicit words and do not rely on finite evidence.
