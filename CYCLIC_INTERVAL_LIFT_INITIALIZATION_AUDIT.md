# Cyclic-interval resolutions: lifting no-go and initialization theorem

## 1. Outcome

Put

\[
 n=2m+1,\qquad W=\binom n m,\qquad B=\frac Wn=\operatorname {Cat}_m.
\]

Three statements which are easy to conflate are now separated exactly.

1.  An SCD of the necklace quotient `B_n/C_n` lifts, after deleting a
    negligible periodic family, to an ordinary near-complete SCD of `B_n`.
    It does **not** lift to a cyclic-interval resolution.  For all but
    `o(W)` middle sets, the coordinate-rotation orbit contains no Johnson
    edge at all, whereas every wreath contains a cyclic Johnson path.
2.  The Mütze--Standke--Wiechert factor supplies the complementary object:
    an exact decomposition of the middle layer into `B` wreaths.  Extending
    it vertically is exactly a tower of nested perfect matchings.  A
    pre-existing SCD cannot simply be matched to the wreath starts: the
    middle set already forces the assignment.
3.  Initialization is **not** an additional asymptotic obstruction.  In any
    exact cyclic-interval SCD resolution, even one with adversarially placed
    radii, all wreaths can be linearized in

    \[
       W+O\!\left(W\sqrt{\frac{\log n}{n}}\right)
    \]

    entries.  The same holds with an additional `o(W)` term for an
    `o(W)`-defect resolution.

Thus the remaining theorem is genuinely the horizontal--vertical
compatibility theorem.  Neither quotient-SCD existence nor middle-wreath
existence implies it, but once it is proved there is no hidden reset cost.

The primary external inputs are:

* P. Hersh and A. Schilling, *Symmetric Chain Decomposition for Cyclic
  Quotients of Boolean Algebras and Relation to Cyclic Crystals*,
  arXiv:1107.4073;
* V. Dhand, *Symmetric chain decomposition of necklace posets*,
  arXiv:1104.4147; and
* T. Mütze, C. Standke and V. Wiechert, *A minimum-change version of the
  Chung--Feller theorem for Dyck paths*, arXiv:1603.02525.

## 2. Per-wreath linearization

For a cyclic order

\[
 \pi=(x_0,x_1,\ldots,x_{n-1})
\]

write

\[
 I_\pi(j,r)=\{x_j,x_{j+1},\ldots,x_{j+r-1}\}.
\]

The symmetric interval chain of radius `d` at start `j` is

\[
 \mathcal C_{\pi,j}^{(d)}
   =\bigl(I_\pi(j,r):m-d\le r\le m+1+d\bigr).
\tag{2.1}
\]

### Lemma 1 (one wreath with nonuniform radii)

Suppose starts of one order `pi` are assigned arbitrary radii
`d_j<=H<m`.  Put

\[
 E_j=I_\pi(j,m-H).
\tag{2.2}
\]

Then the linear word

\[
 E_0,E_1,\ldots,E_{n-1},E_0,E_1,\ldots,E_{2H}
\tag{2.3}
\]

contains every member of every chain
`C_(pi,j)^(d_j)` as a contiguous OR.  Its length is

\[
 n+2H+1.
\tag{2.4}
\]

If `H=m`, the singleton word

\[
 \{x_0\},\ldots,\{x_{n-1}\},
 \{x_0\},\ldots,\{x_{n-2}\}
\tag{2.5}
\]

has length `2n-1` and covers every nonempty cyclic interval, hence again
covers every nonempty member of all the assigned chains.

#### Proof

For `H<m`, the base intervals in (2.2) are nonempty and overlap.  Therefore

\[
 \bigcup_{s=0}^{r}E_{j+s}=I_\pi(j,m-H+r)
\tag{2.6}
\]

whenever `0<=r<=2H+1`.  If `m-d_j<=t<=m+1+d_j`, take

\[
 r=t-(m-H).
\]

Then

\[
 H-d_j\le r\le H+d_j+1\le2H+1,
\]

and (2.6) gives `I_pi(j,t)`.  The repeated prefix in (2.3) turns every
cyclic window of at most `2H+2` terms into an ordinary linear window.

When `H=m`, every nonempty interval is the union of its consecutive
singleton coordinates, and (2.5) linearizes every cyclic window of length
at most `n`.  This also handles the unique radius-`m` chain after its empty
member is omitted.  QED.

The lemma is stronger than a uniform-depth erosion block: a wreath pays only
for the largest radius actually assigned to one of its starts.

## 3. The radius ledger automatically makes initialization negligible

Consider an exact cyclic-interval SCD resolution.  For every selected order
`pi`, let

\[
 H_\pi=\max_j d_{\pi,j}.
\tag{3.1}
\]

For `q>=0`, put

\[
 N_q=\binom n{m-q}.
\tag{3.2}
\]

Exactly `N_q` chains of an SCD have radius at least `q`: they are in
bijection with their rank-`m-q` members.

### Theorem 2 (maximum-radius ledger)

For every placement of the SCD radii among the `B` wreaths,

\[
 \sum_\pi H_\pi
   \le \sum_{q=1}^{m}\min\{B,N_q\}
   =O\!\left(W\sqrt{\frac{\log n}{n}}\right).
\tag{3.3}
\]

Consequently an exact cyclic-interval SCD resolution gives

\[
 \boxed{
 \nu(n)\le
 W+O\!\left(W\sqrt{\frac{\log n}{n}}\right).}
\tag{3.4}
\]

#### Proof

For each `q`, an order with `H_pi>=q` contains at least one chain of radius
at least `q`.  Hence

\[
 \#\{\pi:H_\pi\ge q\}\le\min\{B,N_q\}.
\tag{3.5}
\]

Summing (3.5) over `q` gives the first inequality in (3.3).

For the asymptotic estimate, the exact central ratio is

\[
 \frac{N_q}{W}
  =\prod_{i=0}^{q-1}\frac{m-i}{m+2+i}.
\tag{3.6}
\]

Since `log(1-x)<=-x` and `m+2+i<=n`,

\[
 \frac{N_q}{W}
   \le \exp\!\left(-\frac{q(q+1)}n\right).
\tag{3.7}
\]

Take `Q=ceil(2 sqrt(n log n))`.  The first `Q` summands in (3.3) contribute

\[
 BQ=O\!\left(W\sqrt{\frac{\log n}{n}}\right).
\]

The Gaussian tail from (3.7) is

\[
 \sum_{q>Q}N_q
 \le W\sum_{q>Q}e^{-q^2/n}
 \le W\,O\!\left(\frac nQe^{-Q^2/n}\right)
 =o(W/n),
\]

which proves (3.3).

Apply Lemma 1 independently to every wreath and concatenate the resulting
words.  Extra ORs crossing two words are harmless.  The total length is at
most

\[
 \sum_\pi(n+2H_\pi+1)
  =nB+2\sum_\pi H_\pi+B
  =W+O\!\left(W\sqrt{\frac{\log n}{n}}\right).
\]

The special radius-`m` word (2.5) is no longer than the bound
`n+2H_pi+1` used in this sum.  QED.

### Corollary 3 (defective version)

Suppose at most `B` complete cyclic-order bundles contain pairwise-disjoint
symmetric interval chains and their union misses `Q_0` nonempty Boolean
sets.  Then the bundles can be linearized in

\[
 W+O\!\left(W\sqrt{\frac{\log n}{n}}\right)+Q_0
\tag{3.8}
\]

entries.  In particular, `Q_0=o(W)` implies length `W+o(W)`.

#### Proof

Disjointness implies that the number of retained chains of radius at least
`q` is at most `N_q`, so (3.5)--(3.7) remain valid.  Linearize every bundle
and append each missing set literally.  QED.

This explicitly closes the reset/seam ledger.  A proposed resolution should
be judged on compatibility and coverage, not rejected merely because a few
wreaths contain long chains.

## 4. Why a necklace SCD does not give the required bundles

Let `sigma` be a fixed `n`-cycle on the coordinates.  A literal lift of a
quotient chain uses all coordinate rotations of one nested representative.
Its lower-middle members therefore form

\[
 \operatorname {Orb}_\sigma(X)
   =\{\sigma^tX:t\in\mathbb Z_n\}
\tag{4.1}
\]

for some `m`-set `X`.

### Theorem 4 (rotation-orbit wreath obstruction)

Let `X` be aperiodic.  If the `n` lifted chains above (4.1) can be the `n`
starts of one cyclic-interval bundle, even after the rotations are reordered
arbitrarily, then

\[
 |X\mathbin\triangle\sigma^aX|=2
\tag{4.2}
\]

for some nonzero `a in Z_n`.

The number of subsets of `[n]` satisfying (4.2) for at least one nonzero
`a` is at most

\[
 O(n^4 2^{n/2})=o(W).
\tag{4.3}
\]

Consequently only `o(W)` chains in a literal rotation-lifted necklace SCD
can belong to such bundles.  Deleting the periodic necklaces does not
change this conclusion.

#### Proof

Consecutive lower-middle intervals of one cyclic order differ by deleting
one coordinate and inserting one coordinate.  Thus any wreath contains a
Johnson edge.  If its vertices are the rotations of `X`, some two distinct
rotations are Johnson adjacent.  Translating one of them back to `X` gives
(4.2).

Fix `a\ne0`, put `g=gcd(n,a)` and `L=n/g`.  The permutation `sigma^a`
has `g` cycles of length `L`.  For a binary incidence word, the Hamming
distance in (4.2) is the total number of bit transitions around these
coordinate cycles.  Exactly two transitions means:

* one of the `g` cycles is chosen;
* two of its `L` cyclic gaps are transition gaps; and
* every other coordinate cycle is constant.

Hence the number of binary words satisfying (4.2) for this `a` is at most

\[
 g\binom L2 2^g.
\tag{4.4}
\]

For a nonidentity rotation, `g<=n/2`.  Summing the crude bound (4.4) over
fewer than `n` choices of `a` gives (4.3).  The middle-rank restriction can
only reduce the count.  Since `W=Theta(2^n/sqrt n)`, (4.3) is `o(W)`.

Periodic words themselves number at most `n2^(n/2)=o(W)`.  Every remaining
rotation orbit has size `n`, so the exceptional orbit bundles account for
only `o(W)` lifted chains.  QED.

The obstruction is earlier than move-to-front threading: almost every
literal rotation bundle fails to be a wreath even as an unordered family of
middle sets.  A successful use of necklace chains must globally **re-bundle**
chains from different quotient orbits; the quotient theorem supplies no such
re-bundling.

## 5. Exact wreath factors and the correct two-stage matching

Let `F` be any exact wreath factor of the lower middle layer.  Let `Omega`
be its `W` pointed starts.  For `v=(pi,j)` define

\[
 L_q(v)=I_\pi(j,m-q),\qquad
 U_q(v)=I_\pi(j,m+1+q).
\tag{5.1}
\]

Make the labelled bipartite graph `G_q` whose edge at `v` joins
`L_q(v)` to `U_q(v)`.

### Theorem 5 (nested-matching criterion)

The factor `F` extends to a cyclic-interval SCD resolution if and only if
there are nested start sets

\[
 \Omega=A_0\supseteq A_1\supseteq\cdots\supseteq A_m
\tag{5.2}
\]

such that `G_q[A_q]` is a perfect matching for every `q`.  The radius of a
start is the largest `q` for which it lies in `A_q`.

This is the exact two-stage theorem, but its second stage is additional
mathematics; it is not a consequence of the first-stage wreath factor.

#### Proof

At rank `m-q`, the selected chains contain precisely the values `L_q(v)`
with `v in A_q`; at the complementary rank they contain precisely the
values `U_q(v)`.  Both ranks are partitioned exactly when the corresponding
labelled edges form a perfect matching.  Nesting says exactly that a chain
which reaches depth `q+1` also reaches depth `q`.  QED.

### Lemma 6 (there is no black-box SCD-to-wreath matching)

Fix an ordinary SCD `D` and an exact wreath factor `F`.  If a chain
`C in D` is to become an interval chain at a pointed start of `F`, that start
is uniquely forced by the lower-middle member of `C`.

#### Proof

Every chain of an odd-dimensional SCD has a unique rank-`m` member `S_C`.
Because `F` partitions the lower middle layer, there is exactly one pointed
start `v` with `L_0(v)=S_C`.  Any compatible assignment must use this `v`.
QED.

In fact the central rank-`m+1` member of `C` must already equal `U_0(v)`.
There is therefore no Hall-type freedom obtained by first constructing an
arbitrary SCD and then matching its chains to a fixed wreath factor.  The
nested matchings in Theorem 5 must construct the vertical chains **inside**
the chosen factor.

The MSW theorem gives an exact `F`, hence solves `G_0` in every dimension.
It does not solve Theorem 5.  The explicit MSW factor already has isolated
depth-one targets in dimension nine (the four missing rank-three intervals
recorded in `ODD_GRAPH_EXACT_WREATH_FACTOR.md`), so its `G_1` has no perfect
matching there.  This is a symbolic counterexample to the implication

\[
 \text{exact wreath factor}\quad\Longrightarrow\quad
 \text{vertical cyclic-interval resolution}.
\]

Likewise, a Baranyai/tight-cycle decomposition supplies only `G_0`.
Separate wreath decompositions at other ranks do not supply the nested use
of the same pointed starts required by (5.2).

## 6. Exact frontier

The two known global theorems solve orthogonal halves of the desired object:

\[
\begin{array}{c|c|c}
\text{input}&\text{solved}&\text{missing}\\ \hline
\text{necklace-poset SCD}&\text{vertical chains}
  &\text{horizontal wreath re-bundling}\\
\text{MSW odd-graph factor}&\text{horizontal wreaths}
  &\text{nested vertical matchings}.
\end{array}
\]

The correct next theorem is therefore one of the following equivalent
compatibility statements.

* Construct an exact wreath factor whose graphs `G_q` have nested perfect
  matchings.
* For asymptotic optimality, construct a factor and nested partial matchings
  whose total number of uncovered lower and upper targets is `o(W)`.
* Starting from a lifted quotient SCD, globally re-bundle chains from
  different rotation orbits into `B-o(B)` cyclic orders; literal orbit
  bundles are ruled out by Theorem 4.

Theorem 2 and Corollary 3 show that any one of these compatibility results
has the correct OR-array cost automatically.  The hard problem is not
initialization, periodicity, or the numerical radius histogram.  It is the
integral coupling of the horizontal wreath factor with the vertical chain
flags.
