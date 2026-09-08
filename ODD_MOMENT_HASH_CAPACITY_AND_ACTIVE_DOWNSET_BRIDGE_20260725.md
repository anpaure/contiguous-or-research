# Odd-characteristic moment hashes, physical capacity, and the active-downset bridge

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

There are three conclusions.

1. Over an odd prime field, the pair consisting of the first subset sum
   and the second elementary symmetric sum is exactly equivalent to the
   previously used first and second power sums.  It has a particularly
   clean one-exchange formula and introduces no second hash entropy.
2. Hash labels must remain analysis indices, not matching resources.  With
   that convention the original floor-calibrated augmented coordinate
   orbit keeps its exact physical fractional capacity.  Restricting to one
   fixed global affine hash is a different, non-edge-transitive catalogue;
   its target-fibre theorem is still required.
3. The previously open effective-dimension and nonuniform pair-weight
   bridges follow from one elementary support bound plus the proved
   down-set entropy theorem.  On every size-biased dense slice, all but
   `O(log log m)` of the geometrically effective switch coordinates remain
   active, and its direction-pair weights satisfy the needed pointwise
   `O(S/f^2)` bound.

The remaining affine gate is therefore the fixed-hash physical target
degree/denominator theorem, not effective switch dimension.

## 1. A characteristic-safe two-moment hash

Let `p` be an odd prime and let

\[
 h:[n]\longrightarrow\mathbb F_p.
\]

For a Boolean target `S`, put

\[
 s(S)=\sum_{x\in S}h(x),
 \qquad
 e(S)=\sum_{\{x,y\}\subseteq S}h(x)h(y),
 \qquad
 q(S)=\sum_{x\in S}h(x)^2.
 \tag{1.1}
\]

Then

\[
 \boxed{e(S)={s(S)^2-q(S)\over2}.}
 \tag{1.2}
\]

Hence `(s,e)` and `(s,q)` determine one another by an invertible linear-
quadratic change of coordinates.  Every affine-row parabola formula and
every nonidentical-curve collision bound proved for `(s,q)` transfers
verbatim to `(s,e)`.

### Proposition 1.1 (one-exchange recovery)

Suppose

\[
 S'=S-a+b
\]

where the displayed letters denote the corresponding field labels and
`delta=b-a ne 0`.  Then

\[
 \boxed{
 s(S')-s(S)=\delta,
 \qquad
 e(S')-e(S)=\delta\bigl(s(S)-a\bigr).}
 \tag{1.3}
\]

Consequently the data

\[
 s(S),\quad s(S')-s(S),\quad e(S')-e(S)
\]

recover the ordered exchanged labels exactly:

\[
 \boxed{
 a=s(S)-{e(S')-e(S)\over s(S')-s(S)},
 \qquad b=a+s(S')-s(S).}
 \tag{1.4}
\]

#### Proof

Write `H=S\setminus{a}`.  Then

\[
 e(S)=e(H)+a s(H),
 \qquad
 e(S')=e(H)+b s(H),
\]

and `s(H)=s(S)-a`. \(\square\)

The identity (1.3) is valid in every characteristic.  In characteristic
two it avoids the collapse `q=s^2`.  Nevertheless, a literal nonzero
constant-step arithmetic progression still has period two in every
characteristic-two field.  The present affine-row construction therefore
continues to use odd `p`; `e` is a robustness correction, not permission to
reuse the same long-AP proof over `F_{2^k}`.

The unit-shell warning also remains: one exchanged label pair does not
determine the common affine slope of an entire coordinate string.  Formula
(1.4) recovers the local exchange, while slope dispersal still needs two
physical columns or an outer-slice argument.

## 2. Hash labels are indices, not matching vertices

Let a physical augmented edge contain

* one carrier-copy tag;
* `g` middle owners; and
* `c_q` physical targets in each signed depth-`q` row.

No vertex representing a hash value is added.  The moment pair `(s,e)` is
only an index attached to each physical target for the collision audit.

For the full coordinate orbit, let `T` be the tag count, let

\[
 W=\binom nm,
 \qquad R_q=\binom n{r_q^-}=\binom n{r_q^+}
\]

in the parity-appropriate complementary-row convention.  Thus
`(r_q^-,r_q^+)=(m-q,m+q)` when `n=2m`, while
`(r_q^-,r_q^+)=(m-q,m+1+q)` when `n=2m+1`.  Take

\[
 c_q=\min\left\{g,\left\lfloor{R_q\over T}\right\rfloor\right\}.
 \tag{2.1}
\]

The physical degree ratios are exactly

\[
 \boxed{
 {D_m\over D_{\rm tag}}={Tg\over W}\le1,
 \qquad
 {D_{r_q^-}\over D_{\rm tag}}
 ={D_{r_q^+}\over D_{\rm tag}}
 ={Tc_q\over R_q}\le1.}
 \tag{2.2}
\]

Therefore, if `gT<=W`, the full physical orbit has

\[
 \boxed{\nu^*=T.}
 \tag{2.3}
\]

The floor leaves satisfy

\[
 0\le R_q-Tc_q<T
\]

when the cap does not bind, while capped rows have the already audited
crossing-height deficit.  Hence the scalar floor/cap sum is `o(W)` under
`QT=o(W)` and the crossing ledger.  Moment stratification changes none of
these statements because it has added no capacity vertices.

By contrast, if the `p^2` moment labels are inserted as matching vertices,
their small orbit can become the dominant capacity and destroy (2.3).

### The fixed-hash symmetry boundary

There are two different catalogues which must not be conflated.

1. Orbiting a decorated pair `(h,e)` under the full coordinate group gives
   an edge-transitive labelled multihypergraph and the exact capacity
   (2.3), but different orbit edges generally carry different conjugate
   hashes.  Their moment labels are not one common physical partition.
2. Freezing one global balanced hash `h` gives the common moment partition
   needed for cross-slice comparison, but its literal symmetry group is
   the product of permutations inside the hash fibres (possibly enlarged
   by genuine colour-class symmetries).  Its tag and target orbits refine
   into hash histograms, and rank-level calibration alone no longer proves
   their individual degree bounds.

Thus the fixed-hash target-load theorem, such as equation (7.10) in the
affine-fibre audit, remains necessary.  Averaging over conjugate hashes
cannot replace it: physical equality of targets lying in two different
hash frames does not imply equality of their two moment labels.

## 3. Active dimension from slice density

The first missing switch-orbit bridge has a direct solution.

Let `J_0` be `f_0` geometrically effective, pairwise disjoint switch
directions in one outer slice.  Let

\[
 A\subseteq\{0,1\}^{J_0}
\]

be its nonempty feasible assignment family.  Define the active support

\[
 J(A)=\{i\in J_0:\text{ some }x\in A\text{ has }x_i=1\},
 \qquad f(A)=|J(A)|.
 \tag{3.1}
\]

### Lemma 3.1 (support-entropy bound)

If

\[
 \rho={|A|\over2^{f_0}},
 \qquad b=\log_2(1/\rho),
\]

then

\[
 \boxed{f(A)\ge f_0-b.}
 \tag{3.2}
\]

#### Proof

Every member of `A` is zero outside `J(A)`, so

\[
 |A|\le2^{f(A)}.
\]

Compare with `|A|=2^{f_0-b}`. \(\square\)

Downward closure is not needed for Lemma 3.1.  It is needed below to turn
active support into many anchored switch squares.

### Proposition 3.2 (size-biased active-slice theorem)

Let slices `omega` have base effective dimensions `f_{0,omega}` and
feasible families `A_omega`.  Suppose

\[
 \sum_\omega|A_\omega|
 \ge z\sum_\omega2^{f_{0,\omega}}.
 \tag{3.3}
\]

For `L>1`, slices with

\[
 {|A_\omega|\over2^{f_{0,\omega}}}<{z\over L}
\]

carry at most `1/L` of the total feasible assignment mass.  Every other
slice satisfies

\[
 \boxed{
 f(A_\omega)
 \ge f_{0,\omega}-\log_2(L/z).}
 \tag{3.4}
\]

#### Proof

The bad mass is at most

\[
 {z\over L}\sum_\omega2^{f_{0,\omega}}
 \le {1\over L}\sum_\omega|A_\omega|.
\]

Apply Lemma 3.1 to every good slice. \(\square\)

In the affine application take

\[
 z\ge1/\log m,
 \qquad L=\log m,
 \qquad f_{0,\omega}\ge c p,
 \qquad p=m^{1/2+o(1)}.
\]

Then, outside `o(1)` size-biased feasible mass,

\[
 \boxed{
 f(A_\omega)=f_{0,\omega}-O(\log\log m)
             =p\,m^{-o(1)}.}
 \tag{3.5}
\]

If the base directions have an injective affected-phase map, their active
subfamily retains it.  This proves the effective-`f` hypothesis used by
the affine cross-slice collision theorem, conditional only on the common
density inequality (3.3) and the geometric lower bound on `f_0`.

## 4. Dense down-sets give the required pointwise pair weights

Assume now that `A subseteq Q_f` is a down-set on its active coordinates,
and let `X` be uniform on `A`.  For ordered distinct directions put

\[
 w_A(i,j)=|\{x\in A:x_i=x_j=1\}|,
\]

and

\[
 S_A=\sum_{i\ne j}w_A(i,j)
    =\sum_{x\in A}|x|(|x|-1).
 \tag{4.1}
\]

Let `b=log_2(2^f/|A|)`.  The proved down-set entropy theorem gives

\[
 \mu:=\mathbb E|X|
 \ge {f\over2}-\sqrt{{(\ln2)fb\over2}}.
\]

By convexity,

\[
 S_A\ge|A|\mu(\mu-1).
 \tag{4.2}
\]

On the other hand, trivially `w_A(i,j)<=|A|`.  Hence, when `b=o(f)`,

\[
 \boxed{
 \max_{i\ne j}w_A(i,j)
 \le(4+o(1)){S_A\over f^2}.}
 \tag{4.3}
\]

This is exactly the pointwise direction-pair condition required in the
nonuniform version of the affine cross-slice theorem.  It is stronger than
aggregate `ell_1` closeness and uses no replacement of the down-set by a
uniform full cube.

If every feasible decorated edge in a slice carries the same scalar
weight, (4.3) applies verbatim after multiplying all counts by that weight.

There is a weighted strengthening which identifies exactly what is needed
for genuinely nonuniform assignment weights.  Let `pi` be any probability
law on `Q_f`, put

\[
 b_\pi=f-H_2(\pi),
 \qquad p_i=\Pr_\pi(X_i=1),
 \]

and define

\[
 w_\pi(i,j)=\Pr_\pi(X_i=X_j=1),
 \qquad S_\pi=\sum_{i\ne j}w_\pi(i,j).
\]

Entropy subadditivity gives

\[
 f-b_\pi=H_2(X)\le\sum_i h_2(p_i).
\]

The binary-entropy quadratic bound, followed by Cauchy--Schwarz, yields

\[
 \sum_i p_i
 \ge {f\over2}-\sqrt{{(\ln2)fb_\pi\over2}}.
 \tag{4.4}
\]

Therefore, if `b_pi=o(f)`, convexity gives

\[
 S_\pi
 =\mathbb E_\pi |X|(|X|-1)
 \ge(1-o(1)){f^2\over4}.
\]

Since `w_pi(i,j)<=1`,

\[
 \boxed{
 \max_{i\ne j}w_\pi(i,j)
 \le(4+o(1)){S_\pi\over f^2}.}
 \tag{4.5}
\]

Thus arbitrary assignment weights are harmless whenever their normalized
law has entropy deficiency `o(f)`.  No down-set hypothesis is needed for
the inequality itself.  Downward closure is still what certifies that a
top assignment with bits `i=j=1` anchors the corresponding complete lower
switch square.  Without either high weighted entropy or a separate
max-to-average hypothesis, support alone cannot prevent all weight from
being placed on one assignment.

## 5. Exact fixed-hash target-column formula

The remaining target-fibre problem admits a useful exact product formula.
It explains both the cancellation available from affine symmetry and the
part which still needs a theorem.

Let the fixed hash fibres have sizes `n_s=|h^{-1}(s)|`.  A trimmed
transversal step chooses one departure coordinate `a_s` from the carrier
in every residue and one arrival coordinate `b_s` from its complement in
every residue.  Fix two residue sets `A,B subseteq F_p`.  At the phase in
question, coordinates `a_s` with `s in A` are deleted and coordinates
`b_s` with `s in B` are inserted.  Conditional on a carrier `U`, choose
all `a_s,b_s` uniformly from their available fibres.

For a target `S`, write

\[
 x_s=|S\cap h^{-1}(s)|.
\]

### Proposition 5.1 (transversal-kernel column sum)

Assume the target histogram is interior for this toggle pattern: every
compatible source carrier has at least one available departure and one
available arrival coordinate in each fibre.  The simpler sufficient
condition `2<=x_s<=n_s-2` for every `s` is more than enough and fails on
only an exponentially small central-rank target family at the present
scales.

The sum, over all source carriers of the forced rank, of the conditional
transition probabilities into `S` is

\[
 \boxed{
 K_{A,B}(S)=
 \prod_{s\in A\setminus B}{n_s-x_s\over x_s+1}
 \prod_{s\in B\setminus A}{x_s\over n_s-x_s+1}.}
 \tag{5.1}
\]

Residues in `A cap B` and outside `A union B` contribute exactly one.

#### Proof

The choices factor over the hash fibres.  If `s in A setminus B`, the
source occupancy is `x_s+1`.  There are `n_s-x_s` possible deleted
coordinates, and, for each source, the selected departure coordinate has
probability `1/(x_s+1)`; the unused arrival choice cancels from numerator
and denominator.  This gives `(n_s-x_s)/(x_s+1)`.  The case
`s in B setminus A` is dual and gives `x_s/(n_s-x_s+1)`.

If `s in A cap B`, a source is obtained from `S` by choosing one of its
`x_s` coordinates to be the arrival and one of its `n_s-x_s` outside
coordinates to be the departure.  There are `x_s(n_s-x_s)` such sources,
and each forced ordered pair has probability
`1/[x_s(n_s-x_s)]`, so the contribution is one.  If neither toggle is
used, the source is uniquely `S` in that fibre and again contributes one.
Multiplication over the fibres proves (5.1). \(\square\)

At boundary histograms the same argument holds after deleting the
ineligible source terms; formula (5.1) must not be read with a cancelled
zero availability factor.  The intended target-regularity application
first discards these exponentially rare boundary fibres.

The affine catalogue averages (5.1) over the interval pairs `(A,B)`
generated by phase, offsets and a common nonzero slope.  This average is
the exact fixed-hash membership-atom partition function hidden in the
time-zero target-load condition.

There is an exact first-order cancellation.  At the balanced histogram
`x_s=x_*` (in the equal-fibre idealization), the family of affine interval
pairs is transitive on residues.  Hence the gradient of its averaged
column sum has all coordinates equal.  On the fixed-rank tangent space

\[
 \sum_s (x_s-x_*)=0,
\]

the linear term vanishes.  Because the affine group is two-transitive,
the Hessian has one diagonal and one off-diagonal value, and its
restriction to the same tangent space is a scalar multiple of
`sum_s(x_s-x_*)^2`.

This reduces the fixed-hash theorem to controlling the third and higher
terms of the affine-interval average on typical multivariate
hypergeometric histograms.  It is not legitimate to control those terms
by one interval product: an individual logarithmic linear form can have
order-one fluctuation when `p asymp sqrt(m)`.  The averaging over affine
offsets and slopes must be used.  Proposition 5.1 therefore sharpens, but
does not by itself prove, the target-fibre theorem.

## 6. Updated remaining gate

Sections 3--4 close two of the three bridges listed in the affine
cross-slice dispersal note:

* dense size-biased slices have `f=p m^{-o(1)}`;
* their actual direction-pair counts satisfy the required pointwise
  `O(S/f^2)` bound, also for any weighted law of entropy deficiency
  `o(f)`.

What remains is physical denominator control.  One still needs, for one
fixed global balanced hash,

1. time-zero target-fibre loads at most `1+o(1)` outside physical
   `o(W)` weight (or the stronger literal `o(1/Q)` version); and
2. a stopped lower-degree theorem ensuring
   \[
   d_t(x)\ge(1-o(1))z_t d_0(x)
   \]
   on the retained physical targets.

Under such a lower bound, the denominator inflation through
`z_t>=1/log m` is only `z_t^{-2}<=log^2 m=m^{o(1)}`, so the proved
`m^{-1+o(1)}` cross-slice label factor remains at the required scale.
Proposition 5.1 identifies the fixed-hash target load as an explicit
affine-interval average and proves cancellation of its degree-one
histogram mode.  The fixed-hash higher-order partition-function theorem
and the stopped predictable-mean-spread theorem, rather than the
effective-downset bridge, are now the exact unresolved affine gates.
