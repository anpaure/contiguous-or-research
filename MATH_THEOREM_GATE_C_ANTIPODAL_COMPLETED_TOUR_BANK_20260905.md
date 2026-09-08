# Gate C: antipodal completed-tour banks

**Status (2026-09-05).**  Every assertion below is proved.  For one fixed
pairing and cyclic pair order, completed coherent tours can be grouped into
balanced linear banks containing antipodal state pairs.  Inside such a bank:

* all completed middle supports are disjoint;
* all rank-`b+1` supports are disjoint; and
* the only rank-`b-1` collisions are the antipodal ones, with exact total
  repetition fraction `1/b`.

One such bank can be transported to every factor of a coordinate
one-factorization while preserving cross-bank disjointness.  This is a
strictly stronger local atom for the adjacent-rank selector.  It does not
select enough packets to cover the global layers, so the global
matching-correlated rounding problem remains open.

Let `b>=5` be odd.  Fix a perfect pairing

\[
 \mathcal P=\{P_0,\ldots,P_{b-1}\}                    \tag{0.1}
\]

and a directed cyclic order of its pairs.  Identify a transversal state
with `x in F_2^b`, and write `T(x)` for its completed coherent FIFO tour.
Its cyclic word has length `b^2`.  For `h in {-1,0,1}`, let

\[
 S_h(x)=\{I_{b+h}^{w_x}(a):a\in\mathbb Z_{b^2}\}.    \tag{0.2}
\]

Every support in (0.2) has size `b^2`.  Let `1` denote the all-one vector
of `F_2^b`, and let `tau` exchange the two ground labels in every pair.

## 1. Exact antipodal intersections

Changing the initial state from `x` to `x+1` exchanges the chosen and
unchosen member of every pair at every time.  Hence, position by position,

\[
                         w_{x+\mathbf1}=\tau w_x.      \tag{1.1}
\]

### Lemma 1.1 (antipodal collision inventory)

For every state `x`,

\[
 \boxed{
 |S_{-1}(x)\cap S_{-1}(x+\mathbf1)|=2b,
 \quad S_0(x)\cap S_0(x+\mathbf1)=\varnothing,
 \quad S_1(x)\cap S_1(x+\mathbf1)=\varnothing.}      \tag{1.2}
\]

#### Proof

At rank `b-1`, a target has one empty coordinate pair and splits every
other pair.  Fix the empty pair `e`, and list the other pair indices in the
order in which the relevant FIFO passage flips them:

\[
                         a_1,a_2,\ldots,a_{b-1}.       \tag{1.3}
\]

For some base split vector `v`, the `b` targets with empty pair `e` have
split vectors

\[
 v+\mathbf1_{\{a_1,\ldots,a_i\}},
                         \qquad0\le i\le b-1.          \tag{1.4}
\]

By (1.1), the corresponding family for `x+1` is the coordinatewise
complement of (1.4).  Equality between one prefix vector and one
complemented prefix vector is equivalent to

\[
 \{a_1,\ldots,a_i\}=\{a_{j+1},\ldots,a_{b-1}\}.       \tag{1.5}
\]

An initial and a terminal segment of the linear list (1.3) are equal only
when both are empty or both are the whole list.  Thus there are exactly two
common lower targets for each of the `b` choices of `e`, proving the first
formula in (1.2).

At middle rank, an internal target has a unique occupancy signature
`(empty pair, doubled pair)`.  Applying `tau` preserves that signature and
complements all `b-2>0` split choices, so the unique target of that
signature in `S_0(x)` cannot be its `tau`-mate.  The other `b` middle
targets are transversals.  If the boundary transversal at phase `s` is
written in the fixed pair order, its bit vector is

\[
 v_s=x+s\mathbf1+\mathbf1_{\{0,\ldots,s-1\}}.         \tag{1.6}
\]

For `0<=s<t<b`, the difference `v_s+v_t` is either the nonempty proper
interval indicator `1_{[s,t)}` or its complement.  It is never `1`.
Therefore no two boundary transversals are `tau`-mates.  Internal and
boundary occupancy signatures differ, proving the middle assertion.

At upper rank there are two occupancy types.  A target with one empty and
two doubled pairs has a signature occurring only once, and it has
`b-3>0` split pairs; the preceding uniqueness argument applies.  A target
with no empty pair and one doubled pair has exactly two possible starts.
By cyclic relabelling, take the doubled pair to be `2`, the first start to
be the beginning of packet `0`, and the second to be the special output of
packet `2`.  Outside pair `2`, their split bits are respectively

\[
 (0,1,1,\ldots,1),qquad
 (1,1,1,0,\ldots,0),                                 \tag{1.7}
\]

where the displayed coordinates are pairs
`0,1,3,4,...,b-1`.  They differ in exactly `b-3`, rather than `b-1`,
coordinates.  Hence they are not `tau`-mates.  This exhausts the upper
signatures and proves (1.2). \(\square\)

## 2. A balanced linear bank containing the antipode

Let \(\mathcal B_\circ\subseteq\mathbb F_2^b\setminus\{0\}\) be the set of state
differences for which two completed tours share a target at one of the
three ranks in (0.2).  Equality of two target forms fixes the state
difference on every pair split in both forms.  Each form has at most three
nonsplit pairs, so an ordered pair of forms gives at most `2^6` candidate
differences.  There are `3b^2` forms, whence

\[
                         |\mathcal B_\circ|\le576b^4. \tag{2.1}
\]

Lemma 1.1 says

\[
 \mathbf1\in\mathcal B_\circ,
 \quad\text{but it causes collisions only at rank }b-1.            \tag{2.2}
\]

Let

\[
 2\le H=o(b/\log b),\qquad
 V_H=\sum_{j=1}^{H}{b\choose j},\qquad
 s=\left\lceil\log_2(4V_H)\right\rceil.             \tag{2.3}
\]

### Theorem 2.1 (antipodal balanced subcode)

For all sufficiently large `b`, there is an `(s+1)`-dimensional code
`C <= F_2^b` such that

\[
 \boxed{
 \mathbf1\in C,\qquad
 C\cap\mathcal B_\circ=\{\mathbf1\},\qquad
 d(C^\perp)>H.}                                      \tag{2.4}
\]

#### Proof

Choose independent uniform `X_1,...,X_s in F_2^b` and put

\[
                         C=\langle\mathbf1,X_1,\ldots,X_s\rangle.   \tag{2.5}
\]

The probability that their images in
\(\mathbb F_2^b/\langle\mathbf1\rangle\) are dependent is at most
`2^(s+1-b)=o(1)`.

For every nonempty coefficient vector `u`, the sum `X_u` is uniform in
`F_2^b`.  Taking both `X_u` and `1+X_u`, a union bound gives

\[
 \Pr\bigl((C\setminus\{0,\mathbf1\})
             \cap\mathcal B_\circ\ne\varnothing\bigr)
 \le {2(2^s-1)|\mathcal B_\circ|\over2^b}=o(1),      \tag{2.6}
\]

because `s=o(b)` and (2.1) is polynomial.

Now fix a nonzero vector `y` of weight at most `H`.  If `wt(y)` is odd,
then \(y\mathbin\cdot\mathbf1=1\), so `y` cannot lie in \(C^\perp\).  If
`wt(y)` is even, the
probability that `y dot X_i=0` for every `i` is `2^(-s)`.  Therefore

\[
 \Pr(d(C^\perp)\le H)\le V_H2^{-s}\le {1\over4}.     \tag{2.7}
\]

For large `b`, the two `o(1)` errors in (2.6) and the dependence estimate,
together with (2.7), sum to less than one.  A choice satisfying all three
requirements exists. \(\square\)

Every coset of `C` is exactly `H`-wise uniform in the state coordinates,
by the dual-distance condition.

### Theorem 2.2 (exact bank support sizes)

Put `c=|C|=2^(s+1)`.  In every coset `z+C`, the `c` completed tours have
union sizes

\[
 \boxed{
 \left|\bigcup_{x\in z+C}S_0(x)\right|=b^2c,
 \quad
 \left|\bigcup_{x\in z+C}S_1(x)\right|=b^2c,
 \quad
 \left|\bigcup_{x\in z+C}S_{-1}(x)\right|=b(b-1)c=qc.}             \tag{2.8}
\]

In particular, its `qc` internal middle targets are all distinct.

#### Proof

Two different states of the coset have difference in
\(C\setminus\{0\}\).  By (2.4), every difference other than `1` causes no
collision at any of the three ranks.  Lemma 1.1 shows that difference `1`
also causes no middle or upper collision, proving the first two formulas.

The coset is partitioned into `c/2` antipodal pairs.  Each pair has exactly
`2b` repeated lower targets by Lemma 1.1.  No lower target can occur in two
different antipodal pairs, since that would create a collision whose state
difference is neither `0` nor `1`.  Inclusion--exclusion is therefore
exact:

\[
 b^2c-{c\over2}(2b)=b(b-1)c.
\]

The internal middle supports are subsets of the mutually disjoint full
middle supports. \(\square\)

Thus the deliberate admission of one collision difference loses exactly
one `b`th of the lower occurrence capacity and nothing at middle or upper
rank.

## 3. One antipodal bank on every factor

Fix the standard one-factorization of `K_(2b)` into pairings

\[
                         \mathcal P_0,\ldots,\mathcal P_{2b-2}.      \tag{3.1}
\]

Transport an independent copy of the template in Theorem 2.2 by a uniform
automorphism of each pairing, carrying its cyclic order, state coordinates,
and code with it.

For two different factors `P,Q`, the graph `P union Q` is a disjoint union
of even cycles and has at most `b/2` components.  A target accessible to a
completed tour at one of ranks `b-1,b,b+1` has at most three monochromatic
edges of its pairing.  If it is accessible for both `P` and `Q`, delete the
at most six exceptional edges.  After choosing those edges and their
types, the remaining zero--one colouring is constant up to reversal on at
most `b/2+6` components.  Hence the common accessible support at a fixed
rank is at most

\[
                         C_0b^6 2^{b/2}               \tag{3.2}
\]

for an absolute constant `C_0`.

Every occupancy-signature orbit has at least `2^(b-3)` members, whereas a
bank has at most `b^2c` targets in it.  Pairing automorphisms are transitive
on each such orbit.  Thus a fixed accessible target belongs to a random
transported bank with probability at most

\[
                         C_1b^2c\,2^{-b}.              \tag{3.3}
\]

For two factors, independence, (3.2), and (3.3) bound the probability of a
cross-bank collision at any fixed rank by

\[
 C_2b^{10}c^2\,2^{-3b/2}=2^{-3b/2+o(b)}.             \tag{3.4}
\]

There are fewer than `2b^2` factor pairs and three ranks.  The union bound
in (3.4) is `o(1)`, so a simultaneous collision-free transport exists.

### Theorem 3.1 (antipodal one-factorization packet)

For every sufficiently large odd `b`, there are `2b-1` antipodal balanced
banks, one on every factor in (3.1), such that different banks have
disjoint supports separately at ranks `b-1,b,b+1`.  With

\[
                         R=(2b-1)c                    \tag{3.5}
\]

the number of constituent tours, their packet supports have exact sizes

\[
 \boxed{
 K_{\rm int}=Rq,qquad
 K_0=K_1=Rb^2,qquad
 K_{-1}=Rq.}                                         \tag{3.6}
\]

The internal middle targets are pairwise distinct.  At lower rank the only
repetitions before taking the support are the intrinsic antipodal ones
already charged in (2.8); there are no cross-bank repetitions.  There are
`R/2` antipodal state pairs and `2b` repeated lower targets per pair, hence
the total lower repetition excess is exactly `Rb`.

#### Proof

Choose the simultaneous transports just established.  Apply Theorem 2.2
inside every bank and cross-bank disjointness between different factors,
then sum the exact support sizes. \(\square\)

Equivalently, the exact ledger is

\[
 \begin{array}{c|c|c}
 \text{rank}&\text{raw occurrences}&\text{distinct packet targets}\\ \hline
 b-1&Rb^2&Rq\\
 b&Rb^2&Rb^2\\
 b+1&Rb^2&Rb^2.
 \end{array}                                          \tag{3.7}
\]

## 4. Consequence and remaining obstruction

At the global internal matching scale `W/K_int`, the packet has scalar
capacities

\[
 {W\over K_{\rm int}}K_{-1}=W,qquad
 {W\over K_{\rm int}}K_1={b\over b-1}W.             \tag{4.1}
\]

Both exceed

\[
                         W_1={b\over b+1}W           \tag{4.2}
\]

by only `O(W/b)` at the nearest lower rank and by `O(W/b)` relative to the
coefficient-one budget.  Thus the antipodal packet loses no asymptotic
adjacent capacity, while its intrinsic lower repetitions already fit in
the allowed `o(W)` ledger.

This does not prove that different packet images can be chosen with
disjoint internal targets and `o(W)` adjacent holes.  It proves that the
current coset machinery can be made locally compatible with exactly the
right three-layer scalar profile.  The first unresolved step is now a
global matching/coverage theorem for the coordinate orbit of the packets
in Theorem 3.1; no repair internal to one bank or one one-factorization is
still needed.
