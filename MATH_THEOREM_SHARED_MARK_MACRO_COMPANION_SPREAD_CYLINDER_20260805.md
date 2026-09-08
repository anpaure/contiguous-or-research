# Shared duplicate marks are harmless under companion spread

**Date:** 2026-08-05  
**Method:** macro-cluster exposure, partition expansion, and hypergeometric
orbit tails; no computation or search  
**Status:** exact cylinder theorem plus an unconditional random-bank orbit
lemma.  The `h=2,3` duplicate FIFO macro forces its copies to share `b_1`, so
independent occurrence marking is not physically appropriate for that
architecture.  Nevertheless a common mark still gives the required
two-mark cylinder whenever fixed owner occurrences have superpolynomially
small probability of being companions.  The fresh duplicate geometry has
an `exp(Omega(d log d))` companion orbit, and uniform pre-reserved banks do
not destroy it.  What remains is to retain this companion-spread law in the
integral macro selector after the other upper owners are installed.

## 1. Abstract bounded-macro model

Let `S` be a family of one-mark suffix occurrences `s=(T_2,b_2)`.  A random
selected subfamily is partitioned into macros of size at most a fixed
`h_0`.  Every macro `G` has a common endpoint aperture `A_G` of size

\[
                         a=r-d+1,                            \tag{1.1}
\]

and chooses one common mark `Z_G`, uniformly from `A_G`, independently over
the macros conditional on the complete unmarked macro structure.  Thus all
copies in one literal duplicate block share `b_1=Z_G`, as required by the
fresh duplicate lift.

Let `Y_s` indicate selection of the one-mark occurrence `s`.  Fix already
exposed banks `B_0,B_1`.  Assume the random macro selector has the following
**cluster exposure cylinder**.  There are numbers `eta,kappa` such that, for
every collection of distinct prescribed occurrences indexed by `[m]`, and
every set partition `pi` of `[m]` into blocks of size at most `h_0`,

\[
 \Pr\left(
   \begin{array}{c}
   \text{all prescribed occurrences are selected, and}\\[-2mm]
   \text{their induced common-macro partition is exactly }\pi
   \end{array}
   \ \middle|\ B_0,B_1\right)
 \le \eta^{|\pi|}\kappa^{m-|\pi|}.                         \tag{CE}
\]

For the all-singleton partition this is bounded by the ordinary one-mark
cylinder (the exact-partition event is a subevent of selection).  Requiring
the partition to be exact avoids counting a structure with fewer independent
macro marks under a finer partition.

The following elementary criterion is often easier to verify than `(CE)`.

### Lemma 1.1 (root-and-companion exposure implies `(CE)`)

For every prescribed cluster, root it at any one of its occurrences.
Suppose that

1. any `g` prescribed roots are jointly selected with probability at most
   `eta^g`; and
2. after exposing the roots and any earlier companions, the conditional
   probability that a prescribed further occurrence is in its root's macro
   is at most `kappa`.

Then `(CE)` holds.

#### Proof

For a partition with `g` blocks, expose its `g` roots first and then the
remaining `m-g` occurrences in any block-respecting order.  Apply condition
1 to the roots and condition 2 at every later exposure.  The chain rule
gives `eta^g kappa^(m-g)`.  Requiring the induced partition to be exact only
shrinks the event.  \(\square\)

### Theorem 1.1 (cluster-spread shared-mark cylinder)

Put

\[
                         u={a\kappa\over\eta}.              \tag{1.2}
\]

For every compatible collection of prescribed two-mark states
`alpha_i=(s_i,z_i)`, `1<=i<=m`, one has

\[
 \boxed{
 \Pr(\alpha_1,\ldots,\alpha_m\text{ are selected}\mid B_0,B_1)
 \le \left({\eta\over a}\right)^m
       \sum_{c=0}^{m-1}(m^2u)^c.}                           \tag{1.3}
\]

Consequently, if `m<=M`, `M^2u=o(1)`, then uniformly through those orders

\[
 \Pr(\alpha_1,\ldots,\alpha_m\text{ selected}\mid B_0,B_1)
 \le\left((1+o(1)){\eta\over a}\right)^m.                  \tag{1.4}
\]

#### Proof

Expose the unmarked macro partition.  It induces a partition `pi` of the
prescribed selected occurrences according to common macro membership.  If
two prescribed marks in one block disagree, the conditional probability is
zero.  Otherwise the independent common macro marks contribute

\[
                         a^{-|\pi|}.                         \tag{1.5}
\]

Sum over all possible induced partitions and apply `(CE)`.  A partition
with `c=m-|pi|` mergers may be encoded by choosing, in every nonsingleton
block, a rooted spanning star.  Forgetting acyclicity and the restriction on
block size gives at most `m^{2c}` encodings: choose an ordered pair of
vertices for each of `c` star edges.  Therefore

\[
 \begin{aligned}
 \Pr(\text{prescribed two-mark states})
 &\le\sum_\pi a^{-|\pi|}\eta^{|\pi|}\kappa^{m-|\pi|}\\
 &\le(\eta/a)^m\sum_{c=0}^{m-1}(m^2a\kappa/\eta)^c,
 \end{aligned}                                             \tag{1.6}
\]

which is (1.3).  If `M^2u=o(1)`, the geometric sum is `1+o(1)` uniformly.
Its `m`-th root is also `1+o(1)`, proving (1.4).  \(\square\)

This theorem quantifies the diagonal obstruction exactly.  Shared marks are
not dangerous merely because they exist; they are dangerous only when a
fixed prescribed pair has companion probability comparable to `eta/a`.

## 2. Companion orbit in a fresh duplicate macro

Consider the `h=2,3` punctured duplicate lift.  At level two its copies have

\[
                         T_2^c=P\mathbin{\dot\cup}X_c^+,    \tag{2.1}
\]

where

\[
 |P|=r-d+2,\qquad |X_c^+|=d-2,                              \tag{2.2}
\]

the tails `X_c^+` are pairwise disjoint, and the common one-mark label
`b_2` lies in `P`.  Hence two companion level-two owners have Johnson
distance exactly `d-2` and intersection exactly `P`.

Fix a one-mark occurrence `(T,b_2)`.  Before choosing the remaining copies,
one may choose

* the removed tail `T-P`, in `\(\binom{r-1}{d-2}\)` ways; and
* one companion tail outside `T`, in `\(\binom{k-r}{d-2}\)` ways.

Thus the full prospective companion orbit has size

\[
 N_2=\binom{r-1}{d-2}\binom{k-r}{d-2}.                     \tag{2.3}
\]

After one companion has been installed, every further companion has at
least

\[
 N_*=\binom{k-r-(h_0-2)(d-2)}{d-2}                         \tag{2.4}
\]

fresh tail choices.  In the central regime `r,k-r=Theta(d^2)`,

\[
                         \log N_*=\Theta(d\log d).          \tag{2.5}
\]

An occurrence-local sampler which chooses each companion uniformly from its
remaining prospective tail orbit therefore has point mass at most

\[
                         \kappa\le {h_0-1\over N_*}.        \tag{2.6}
\]

With the natural one-mark scale

\[
                         \eta=\Theta((dr)^{-1})
                              =\Theta(d^{-3})               \tag{2.7}
\]

and `a=Theta(d^2)`, equations (1.2), (2.5), and (2.6) give

\[
                         M^2u=o(1)\qquad(M=O(d)).            \tag{2.8}

Therefore the common mark of a `2/3` duplicate macro costs no asymptotic
cylinder factor under the companion-spread sampler.

The statement is prospective.  An integral selector can concentrate on a
small subset of the orbit; `(CE)` or its sequential companion version must
be retained by the actual macro packing.

## 3. Uniform pre-reserved banks preserve every local orbit

The bank reservation itself does not obstruct companion spread.

### Lemma 3.1 (simultaneous companion-orbit survival)

Let `B=B_0\cup B_1` be a uniform fixed-size bank in the rank-`r` owner
layer, of density

\[
                         p=O(1/d).                            \tag{3.1}
\]

For every prospective companion-tail orbit `O` of size at least `N_*`,

\[
 \Pr\bigl(|O\setminus B|<(1-2p)|O|\bigr)
                         \le \exp(-\Omega(pN_*)).            \tag{3.2}
\]

Simultaneously for every orbit arising from the fresh `h<=h_0` macro,

\[
                         |O\setminus B|=(1-O(1/d))|O|        \tag{3.3}
\]

with probability `1-o(1)`.

#### Proof

For fixed `O`, `|O cap B|` is hypergeometric of mean `p|O|`; the standard
sampling-without-replacement Chernoff bound gives (3.2).

An orbit is specified by `O(d)` coordinate sets and labels.  A crude bound
of `2^{O(k)}k^{O(d)}` on their number has logarithm `O(k+d log k)=O(d^2)`.
By (2.5), `pN_*=exp(Omega(d log d))`, which dominates `d^2`.  A union bound
therefore proves (3.3).  \(\square\)

After conditioning on a bank pair satisfying (3.3), uniform selection from
the surviving local orbit only changes (2.6) by the factor `1+O(1/d)`.

This lemma does not control owners consumed adaptively by the upper macro
packing.  Avoiding concentration caused by those choices is exactly the
remaining companion-spread selector row.

## 4. Exact sufficient selector theorem for the bottom completion

Combine the preceding result with the endpoint aperture theorem.

### Corollary 4.1

Suppose the pre-reserved upper construction is selected as fresh `h=2,3`
duplicate macros and satisfies `(CE)` with

\[
 \eta\le(1+o(1)){H\over Wr},\qquad
 \kappa\le {O(1)\over N_*}.                                \tag{4.1}
\]

Choose the common `b_1` of each macro uniformly from its persistent-kernel
aperture.  Then the retained marked level-two states satisfy the
bank-conditioned cylinder `(C2)` through order `O(d)`.

#### Proof

Theorem 1.1 and (2.8) give the cylinder with intensity

\[
 (1+o(1)){\eta\over r-d+1}
 \le(1+o(1)){H\over W(r)_2},                               \tag{4.2}
\]

using `(r-1)/(r-d+1)=1+O(d/r)`.  This is `(C2)`.  \(\square\)

Thus the exact extra randomness compatible with duplicate lower blocks is
not independent marks on copies.  It is:

1. a common uniform endpoint mark inside each macro; and
2. a companion selector whose maximum local atom is
   `exp(-Omega(d log d))`.

The second condition is far weaker than a full two-mark cylinder and is the
sharp remaining integral selector target on this route.

## 5. Proof-safe conclusion

The theorem closes the apparent conflict between the two requirements:

* duplicate copies may share their lower path and therefore share `b_1`;
* prescribed owner occurrences still have an asymptotically product
  two-mark law, because the chance that they are the copies sharing that
  mark is superpolynomially small.

Uniform random banks preserve the necessary prospective companion orbit.
What remains open is to prove `(CE)` for the actual owner-disjoint integral
macro selector after all upper-owner exclusions.  No further mark
randomness is needed once that companion-spread row is available.
