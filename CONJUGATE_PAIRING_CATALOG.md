# A polynomial catalog removes pointwise fixed-pair type rigidity

## 1. Scope

Let `P` be a perfect matching of `[2m]`.  For a set `S subset [2m]`, put

\[
 \phi_P(S)=|\{e\in P:e\subseteq S\}|.
\tag{1.1}
\]

This is the full-pair statistic used by the fixed-pair shadow-capacity
theorem.  One fixed matching has the wrong source/target type balance at
depth `q=Theta(sqrt(m))`.  The result below shows that no individual target
has to remain trapped in one fixed type: a polynomial-size multiset of
coordinate matchings simultaneously approximates the random-matching
one-set type law for **every** subset of `[2m]`.

This does not by itself balance source and target capacities jointly.  If
all catalog members are regarded as independent full copies, the aggregate
numbers of source and target occurrences of type `f` are still `K V_f` and
`K T_(f,q)`.  A nonuniform allocation of actual middle vertices among the
catalog members remains to be found.

This is not a cube partition, a cycle factor, or a shadow theorem.  It says
that mixing conjugate pair systems has scalar type diversity.  The remaining
problem is to realize a compatible mixture while preserving the required
radius labels, disjointness, and shift overlap.

## 2. Exact type law under a random matching

For `0<=t<=2m`, define

\[
 A_{m,t}(f)=
 \binom mf\binom{m-f}{t-2f}2^{t-2f},
\tag{2.1}
\]

with the convention that an invalid binomial coefficient is zero.

### Lemma 1

If `P` is fixed, exactly `A_(m,t)(f)` of the `t`-subsets `S` satisfy
`phi_P(S)=f`.  Consequently, if `P` is a uniformly random perfect matching,
then for every fixed `t`-set `S`,

\[
 \Pr\{\phi_P(S)=f\}
   ={A_{m,t}(f)\over\binom{2m}t}.
\tag{2.2}
\]

#### Proof

For a fixed matching, choose the `f` pairs lying wholly in `S`, then choose
the `t-2f` pairs contributing one endpoint, and finally choose that endpoint
in each of the latter pairs.  This gives (2.1).

The symmetric group is transitive on `t`-subsets and on perfect matchings.
Double-counting pairs `(P,S)` with `phi_P(S)=f` therefore makes the type law
of a fixed set under random `P` equal to the type law of a random set under
a fixed `P`, which is (2.2).  QED.

For `t=m`, (2.1) is the source count

\[
 V_f={m!\over f!f!(m-2f)!}2^{m-2f}.
\tag{2.3}
\]

For `t=m-q`, it is the target count

\[
 T_{f,q}={m!\over f!(f+q)!(m-2f-q)!}2^{m-2f-q}.
\tag{2.4}
\]

Thus the exact distributions appearing in the fixed-pair obstruction are
precisely the one-set marginals obtained by conjugating the matching.

## 3. Uniform polynomial catalog theorem

### Theorem 2

For every `0<epsilon<1`, there is a multiset

\[
 \mathcal P=(P_1,\ldots,P_K)
\tag{3.1}
\]

of perfect matchings of `[2m]`, with

\[
 K\le
 \left\lceil {4(m+\log(m+1)+1)\over\epsilon^2}\right\rceil,
\tag{3.2}
\]

such that simultaneously for every `S subseteq [2m]` and every integer
`0<=f<=m`,

\[
 \left|
 {1\over K}|\{j:\phi_{P_j}(S)=f\}|
 -{A_{m,|S|}(f)\over\binom{2m}{|S|}}
 \right|\le\epsilon.
\tag{3.3}
\]

#### Proof

Choose `P_1,...,P_K` independently and uniformly from all perfect
matchings.  For fixed `(S,f)`, the summands

\[
 1_{\{\phi_{P_j}(S)=f\}}
\]

are independent Bernoulli variables with mean (2.2).  Hoeffding's
inequality bounds failure of (3.3) by

\[
 2\exp(-2K\epsilon^2).
\tag{3.4}
\]

There are at most `2^(2m)(m+1)` relevant pairs `(S,f)`.  Taking `log` in
(3.2) to mean the natural logarithm, the union bound is strictly below one
for that value (with considerable slack).
Hence some catalog satisfies every inequality simultaneously.  QED.

### Corollary 3

For `m>=2`, there is a catalog of size `O(m^5)` for which, uniformly over
every subset `S`, the empirical law of `phi_P(S)` has total-variation
distance `O(1/m)` from the exact random-matching law.

#### Proof

Take `epsilon=m^(-2)` in Theorem 2.  Summing the coordinatewise errors over
the at most `m+1` possible values of `f` gives at most `(m+1)/m^2` in
`l_1`, hence at most `(m+1)/(2m^2)` in total variation.  QED.

The exponent five is not optimized.  The important point is polynomial,
uniform simultaneous control over all exponentially many target sets.

## 4. Fractional conjugation identity

There is a complementary exact statement which does not discretize the
matching distribution.

Take any middle block system whose depth-`q` starts produce exactly
`N_q=binom(2m,m-q)` lower-shadow occurrences and the same number of
upper-shadow occurrences, counted with multiplicity.  Conjugate every
ground coordinate by a uniformly random permutation.  The statement below
concerns these occurrence multisets; repeated shadows remain repeated.

### Lemma 4

For every fixed lower target `S` of rank `m-q`, its expected multiplicity in
the conjugated system is one.  The same holds for every upper target of rank
`m+q`.

#### Proof

Coordinate permutations act transitively on either target layer.  Hence all
targets have the same expected multiplicity.  The total multiplicity is
always `N_q`, equal to the number of targets in the layer.  The common
expectation is therefore one.  QED.

Thus the group average over all `(2m)!` coordinate permutations, counted
with multiplicity, gives exact fractional occurrence degree one at every
shadow target, even if the original block system has severe collisions.
This identity is only fractional: choosing one global conjugate merely
renames the collisions, while choosing different conjugates block by block
can destroy the middle partition.

The lemma is independent of binary RSK radius.  An arbitrary coordinate
permutation preserves ranks, inclusion, physical OR relations, and the
lengths of any already constructed symmetric chains, but it need not
preserve the standard binary-RSK shape of a middle set or the RSK-radius
purity of a BK cell.  Therefore the lemma may transport an abstract radius
label attached to a completed block, but it does not turn coordinate
conjugates into new standard-RSK-radius-pure BK cells.

## 5. Consequence for the construction program

The native Bender--Knuth partition fails at `q=c sqrt(m)` because all of its
cells use one coordinate matching.  Theorem 2 proves that only polynomially
many matchings are needed to give every individual target the correct
random-matching type marginal, uniformly over all targets.  It does **not**
prove a simultaneous allocation of sources to targets, nor does it imply
that a polynomial catalog of arbitrarily chosen conjugating permutations
approximates the shadow multiplicities of a given block system: those
multiplicities depend on more than the matching statistic `phi_P`.

Lemma 4 separately gives exact fractional shadow balance over the full
permutation-group average.

What remains is the following integral resolution problem.

> Select vertex-disjoint coordinate-conjugated cells or cycle blocks from a
> suitably resolved catalog so that they cover
> `W-o(W)` middle vertices and, through every required depth, their lower
> and upper shadow maps have total collision defect `o(W)`.

Neither theorem here supplies that selection.  In particular:

* cells from different conjugate partitions overlap on middle vertices;
* coordinate conjugation does not preserve standard binary-RSK radius
  purity, so radius certificates must be transported with completed blocks
  or rebuilt in the selected resolution;
* a separate matching at each depth need not stitch into one shifted word;
* independent block choices retain the Poisson collision barrier;
* current generic hypergraph matching theorems leave `Theta(W)` rather than
  `o(W)` at the relevant nested pair-codegree scale.

The proved gain is a clean separation.  Pointwise fixed-type rigidity
disappears in a polynomial matching catalog, and the full conjugation
average has exact fractional shadow degrees.  Neither fact removes the
joint capacity constraints of a polynomial integral catalog.  The missing
mathematics is still an integral, radius-compatible, shift-compatible
resolution theorem.
