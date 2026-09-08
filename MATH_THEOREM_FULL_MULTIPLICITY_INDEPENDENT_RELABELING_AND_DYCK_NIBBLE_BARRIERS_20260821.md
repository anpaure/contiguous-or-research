# Full multiplicity does not rescue independent rank relabeling, and the raw Dyck palette is not a small-codegree nibble

**Status (2026-08-21).**  Every assertion below is proved.  There are two
separate conclusions.

1.  In the clustered two-block product bank, using all `q+1` payload
    sources at upper offset `q` does not rescue independent rank-by-rank and
    side-by-side relabeling.  Uniformly for every `1<=q<=Q=o(sqrt b)`,
    at least a `(1/4-o(1))` fraction of rank-`(b+q)` targets remains
    uncovered in expectation.  If `Q->infinity`, the expected aggregate
    miss over these ranks is at least `(1/4-o(1))QW_b`.
2.  The Petr--Turek Dyck-typed wreath palette is an exact regular
    `(2k+2)`-uniform slot--target multihypergraph of degree `k!^2`, but its
    maximum pair codegree is also `k!^2`.  More robustly, a positive-density
    family of complementary target pairs has normalized codegree
    `Theta(1/k)`, so merely projecting away the coverage constraints of
    `o(binom(2k,k))` target vertices cannot produce the stronger
    `k Delta_2/Delta=o(1)` scale.

Neither statement rules out correlated cross-rank conjugations, a trimmed
Dyck palette, augmentation, or a theorem exploiting global interval
geometry.  They rule out two direct probabilistic shortcuts.

## 1. Full-multiplicity clustered bank

Let `b` tend to infinity through odd primes.  Put

\[
 W_b={2b\choose b}.
\]

Conditionally fix tight-cycle factors on each of two disjoint `b`-sets
`A,B` at every payload rank in a central interval containing all ranks used
below.  At local rank `t`, independently conjugate the factor on `A` by a
uniform permutation of `A`, and independently conjugate the factor on `B`
by a uniform permutation of `B`.  All conjugations belonging to distinct
rank-and-side pairs are mutually independent.  At payload rank `r`, product
all orders in the rank-`r` factor on `A` with all orders in the
rank-`(b-r)` factor on `B`, using the clustered schedule

\[
 \tau_r=A^rB^{b-r}.
\]

Fix an upper offset `q` and a target `Y` of rank `b+q`.  Write

\[
 s=|Y\cap A|,
 \qquad P_{q,s}={b\choose s}{b\choose s-q},
 \qquad c_j={b\choose j}.
\]

For `0<=z<=q`, the source with exactly `z` new `A`-letters has payload
`r=s-z`.  Let `N_z(Y)` be its occurrence multiplicity at `Y`, across every
order pair, phase, and counter point at that payload.  The exact source
means are

\[
 \lambda_0={b-s-q+1\over b}{c_s^2\over c_sc_{s-q}},
 \qquad
 \lambda_q={s-2q+1\over b}{c_{s-q}^2\over c_sc_{s-q}},               \tag{1.1}
\]

and, for `1<=z<=q-1`,

\[
 \lambda_z={2\over b}{c_{s-z}^2\over c_sc_{s-q}}.                   \tag{1.2}
\]

Indeed the phase multiplicities are respectively
`b-s-q+1`, `s-2q+1`, and `2`.  There are `c_(s-z)^2/b^2` order pairs and
`b` counter points on each contributing phase diagonal.  Independent label
conjugation is transitive on the `P_(q,s)` targets of the profile, so total
source occurrence divided by `P_(q,s)` gives (1.1)--(1.2).

Most importantly, the random variables

\[
 N_0(Y),N_1(Y),\ldots,N_q(Y)                                      \tag{1.3}
\]

are mutually independent.  Source `z` depends only on the rank-and-side
conjugations

\[
 (s-z,A),\qquad (b-s+z,B),
\]

and these two coordinates are disjoint for different `z`.

### Lemma 1.1 (uniform central source means)

Let `Q=Q(b)=o(sqrt b)`.  There is a sequence `L=L(b)->infinity` such that,
uniformly for `1<=q<=Q` and

\[
 x=s-{b+q\over2},\qquad |x|<=L\sqrt b,                         \tag{1.4}
\]

the two endpoint means in (1.1) are `1/2+o(1)`, while every interior mean
in (1.2) is `(2+o(1))/b`.

#### Proof

Take

\[
 L=\left({\sqrt b\over\max(Q,1)}\right)^{1/2}.
\]

Then `L->infinity`, `L sqrt(b)=o(b)`, and `QL/sqrt(b)=o(1)`.  Put

\[
 u=\log{c_s\over c_{s-q}},\qquad d={b+1\over2}.
\]

The exact product formula is

\[
 u(x)=\sum_{j=0}^{q-1}
 \log {d-(x+j-(q-1)/2)\over d+(x+j-(q-1)/2)}.                    \tag{1.5}
\]

The offsets are symmetric, so `u(0)=0`.  On (1.4), the derivative of each
summand has absolute value `(4+o(1))/b`; hence

\[
 |u|<= (4+o(1)){q|x|\over b}=o(1).                              \tag{1.6}
\]

Also, uniformly for `0<=z<=q`, bounded adjacent second differences of
`log c_j` on this central range give

\[
 \log {c_{s-z}^2\over c_sc_{s-q}}
  =(1-2z/q)u+O(q^2/b)=o(1).                                    \tag{1.7}
\]

For completeness, the error in (1.7) follows by writing
`log(c_(t-1)/c_t)=log(t/(b-t+1))`; this adjacent slope changes by `O(1/b)`
per unit throughout the range in (1.4), and the chord has length `q`.
Finally

\[
 {b-s-q+1\over b}={1\over2}+o(1),\qquad
 {s-2q+1\over b}={1\over2}+o(1).
\]

Equations (1.1)--(1.2), (1.6), and (1.7) prove the lemma.  \(\square\)

### Theorem 1.2 (full-multiplicity independent coupon barrier)

Uniformly for every `1<=q<=Q=o(sqrt b)`, if `Z_q` is the number of
uncovered rank-`(b+q)` targets, then

\[
 \boxed{\mathbb E Z_q\ge(1/4-o(1)){2b\choose b+q}.}               \tag{1.8}
\]

If in addition `Q->infinity`, then

\[
 \boxed{\mathbb E\sum_{q=1}^QZ_q
       \ge(1/4-o(1))QW_b.}                                      \tag{1.9}
\]

#### Proof

For a uniformly random rank-`(b+q)` target, its split coordinate has mean
`(b+q)/2` and variance `Theta(b)`.  Chebyshev's inequality and `L->infinity`
show that (1.4) contains a `1-o(1)` fraction of all targets, uniformly for
`q<=Q`.

Fix one such target.  Markov's inequality gives

\[
 \Pr(N_z(Y)>0)\le\lambda_z.
\]

By Lemma 1.1 the two endpoint means are below one for large `b`, every
interior mean is at most `3/b`, and the source events are independent by
(1.3).  Therefore

\[
 \begin{aligned}
 \Pr(Y\hbox{ is uncovered})
 &=\prod_{z=0}^q\Pr(N_z(Y)=0)\\
 &\ge\prod_{z=0}^q(1-\lambda_z)\\
 &=(1/4-o(1))\prod_{z=1}^{q-1}(1-O(1/b))
  =1/4-o(1),
 \end{aligned}                                                    \tag{1.10}
\]

uniformly for `q<=Q`.  Summing (1.10) over the `1-o(1)` fraction of central
targets proves (1.8).

Uniformly for `q<=Q=o(sqrt b)`, the exact layer ratio gives

\[
 { {2b\choose b+q}\over W_b}=1-o(1).
\]

Summing (1.8) over `q<=Q` proves (1.9).  \(\square\)

The conclusion is an expectation theorem for independent rank-and-side
conjugations.  It does not say that every outcome fails, and it does not
apply to deliberately correlated cross-rank order banks.

There is nevertheless a sharp necessary condition on any such correlated
replacement.

### Theorem 1.3 (successful correlated marginals must be maximally anti-aligned)

Allow arbitrary correlations between different payload ranks, but require
that for every payload `r` the conjugation pair consisting of rank `r` on
`A` and rank `b-r` on `B` retain its product-uniform marginal.  Fix
`q=o(sqrt b)`, choose a uniform rank-`(b+q)` target `Y`, and let `E_0,E_q`
be the events that the two endpoint payload sources cover `Y`.  If the
expected uncovered fraction at this rank is `o(1)`, then

\[
 \Pr(E_0)=\Pr(E_q)=1/2+o(1),\qquad
 \Pr(E_0\cap E_q)=o(1),                              \tag{1.11}
\]

and hence

\[
 \operatorname{Cov}(1_{E_0},1_{E_q})=-1/4+o(1).     \tag{1.12}
\]

Thus a successful correlated construction cannot merely perturb the
independent law: on a random target its two dominant source ranks must be
almost perfectly complementary.

#### Proof

Product-uniform source marginals preserve all means (1.1)--(1.2).  On the
`1-o(1)` central set from Lemma 1.1, the probability that any interior source
covers `Y` is, without any independence assumption, at most

\[
 \sum_{z=1}^{q-1}\Pr(N_z(Y)>0)
 \le\sum_{z=1}^{q-1}\lambda_z=o(1).                 \tag{1.13}
\]

Also `Pr(E_0),Pr(E_q)<=1/2+o(1)` by Markov and the endpoint means.  If the
total uncovered probability is `o(1)`, (1.13) forces
`Pr(E_0 union E_q)=1-o(1)`.  The two upper bounds then force each endpoint
probability to equal `1/2+o(1)`, and inclusion--exclusion forces their
intersection to be `o(1)`.  Equation (1.12) follows.  \(\square\)

## 2. The Dyck-typed wreath hypergraph

Put `n=2k+1`, let

\[
 A=\{1,\ldots,k\},\qquad B=\{k+1,\ldots,2k\},
\]

and let `D_k` be the set of Dyck paths of semilength `k`.  Define a
slot--target multihypergraph `H_k` as follows.  Its vertices are one slot for
each `D in D_k` together with all `k`-subsets of `Z_n`.  For every
permutation `pi` fixing `0` whose positions `1,...,2k` have `A/B` pattern
`D`, include the edge

\[
 \{D\}\cup\mathcal F_\pi,
\]

where `F_pi` is the wreath of the `n` cyclic length-`k` windows of `pi`.
Every edge has size `n+1=2k+2`.

We use the Petr--Turek identities

\[
 \iota_k(k,l)={k\choose l}^2,
 \qquad
 \iota_k(k+1,l)={k\choose l-1}{k\choose l},                    \tag{2.1}
\]

with the second identity extended to the complementary values of `l` by
reflection.  Here `iota_k(m,l)` is the total number of length-`m` intervals
with `l` falls over all Dyck `k`-paths.

### Theorem 2.1 (exact regularity, but maximal pair codegree)

The multihypergraph `H_k` is exactly `k!^2`-regular.  Nevertheless

\[
 \boxed{\Delta_2(H_k)=k!^2.}                                  \tag{2.2}
\]

In particular its normalized maximum pair codegree is one, so the raw
Dyck-slot hypergraph cannot be fed directly to a small-codegree
growing-rank nibble.

#### Proof

A slot has degree `k!^2`, because the `A` labels and `B` labels may be
assigned independently to their prescribed positions.

First let `S` be a target not containing `0`, and put `l=|S cap B|`.  A
window realizing `S` corresponds to a length-`k` Dyck interval with `l`
falls.  Once the interval is fixed, the number of compatible labelings is

\[
 [l!(k-l)!]^2.
\]

The first identity in (2.1) therefore gives degree

\[
 {k\choose l}^2[l!(k-l)!]^2=k!^2.                              \tag{2.3}
\]

Now suppose `0 in S` and put `a=|S cap A|`.  The complementary cyclic
interval has length `k+1` and contains `a+1` `B`-positions.  Its compatible
label count is

\[
 a!(k-a)!(a+1)!(k-a-1)!.
\]

The second identity in (2.1) gives degree

\[
 {k\choose a}{k\choose a+1}
 a!(k-a)!(a+1)!(k-a-1)!=k!^2.                                  \tag{2.4}
\]

Thus every vertex has degree `k!^2`.

Finally take the mountain path `D_star=R^kF^k`.  Every pattern-respecting
permutation in this slot has the target `A` as its all-rise window and the
target `B` as its all-fall window.  Hence

\[
 \operatorname{codeg}(D_star,A)
 =\operatorname{codeg}(A,B)=k!^2.                              \tag{2.5}
\]

No codegree can exceed the common degree, proving (2.2).  \(\square\)

This obstruction is deliberately scoped to the raw hypergraph.  The
exceptional mountain slot and extreme targets form a negligible set.  The
next result shows, however, that merely projecting away those extreme target
constraints does not reach the `o(1/k)` normalized pair scale.

### Theorem 2.2 (a robust complementary-pair codegree band)

Let `S,T` be disjoint `k`-subsets which partition `A union B`, so that `0`
is the unique unused label.  Put `a=|S cap A|` and assume `a>k/2`.  Then

\[
 {\operatorname{codeg}_{\mathcal H_k}(S,T)\over k!^2}
 =\left({2a+1-k\over a+1}\right)^2.                         \tag{2.6}
\]

Consequently, for any fixed `0<c_1<c_2`, a positive fraction of the
nonzero target vertices belong to disjoint complementary pairs with

\[
 {\operatorname{codeg}(S,T)\over k!^2}>={4c_1^2+o(1)\over k}. \tag{2.7}
\]

Projecting away (that is, ignoring the coverage constraints of)
`o(binom(2k,k))` target vertices leaves at least one such pair.  Thus this
form of asymptotically negligible target trimming cannot make

\[
 k{\Delta_2\over\Delta}=o(1).                              \tag{2.8}
\]

#### Proof

If a cyclic wreath contains the two disjoint targets, their positional
windows leave only the position of `0` uncovered.  Since `pi(0)=0`, the two
windows are therefore the position blocks `1,...,k` and `k+1,...,2k`.
Because a Dyck prefix of length `k` has at least `k/2` rises and `a>k/2`,
`S` must occupy the first block.

Let

\[
 B_{k,a}={k\choose a}-{k\choose a+1}
 ={k\choose a}{2a+1-k\over a+1}.                         \tag{2.9}
\]

The ballot/reflection formula says that `B_(k,a)` is the number of
nonnegative length-`k` prefixes with `a` rises.  Reversing and exchanging
rises with falls gives the same count for the suffix from height `2a-k`
back to zero.  Hence exactly `B_(k,a)^2` Dyck paths have `a` rises in their
first `k` positions.

For each such path, assigning the fixed labels of `S` and `T` to the two
blocks gives

\[
 [a!(k-a)!]^2
\]

permutations.  Division by `k!^2` proves (2.6).

Now restrict to

\[
 c_1\sqrt k<=a-k/2<=c_2\sqrt k.                         \tag{2.10}
\]

Equation (2.6) gives (2.7).  Under the weights
`binom(k,a)^2/binom(2k,k)`, the centered variable `a-k/2` has a
nondegenerate Gaussian limit, so (2.10) contains a fixed positive fraction
of all nonzero targets.  Complementation pairs these targets with the
corresponding symmetric band below `k/2`, and the pairs are vertex-disjoint.
Hitting every such pair therefore requires projecting away a fixed positive
fraction of the target constraints.  This proves (2.8).  \(\square\)

This does not prove that a Dyck-typed approximate decomposition is
impossible.  It proves that the raw or negligibly target-trimmed palette does
not have the `Delta_2/Delta=O(1/k^2)` profile suggested by a direct
growing-rank one-bite argument.  A successful use of the Dyck structure
would need to absorb these complementary pairs, thin edges or slots in a
correlated way, or use a matching theorem tolerant of the `Theta(1/k)`
band.

Reference: Jan Petr and Pavel Turek, *Intervals in Dyck paths and the wreath
conjecture*, arXiv:2501.07277 (2025), Corollary 1.2 and Conjecture 2.2.
