# Two-endpoint star packets: exact collision law, large fractional margin, and the short-rank gate

**Date:** 2026-08-06  
**Method:** two shifted suffix chains, exact exchange counting, and local
central-binomial asymptotics  
**Status:** unconditional reduction.  Replacing maximal star cycles by the
shortest packet which actually saves one reset reduces packet rank from
`Theta(nd)` to `2d=Theta(sqrt(n))`.  The resulting packet hypergraph has
more than three orders of magnitude of fractional capacity beyond the theta
deficit.  Independent random packets nevertheless have `Theta(d)` conflict
degree, so an integral short-packet matching theorem is still required.

## 1. The shortest useful packet

Use the odd merged-PBBS parameters

\[
 n=2m+1,\qquad s=m-2d,\qquad q=s-1,\qquad
 v=n-q=n-s+1,
\]

and write

\[
                         W={n\choose m}.
\]

Fix a core `Q in binom([n],q)` and an ordered injective tuple

\[
             \mathbf z=(z_0,z_1,\ldots,z_d)\in([n]\setminus Q)_{d+1}.
\]

For `1<=j<=d`, define the two shifted targets

\[
 \begin{aligned}
 T_{0,j}(Q,\mathbf z)
   &=Q\cup\{z_{d-j},\ldots,z_{d-1}\},\\
 T_{1,j}(Q,\mathbf z)
   &=Q\cup\{z_{d-j+1},\ldots,z_d\}.
 \end{aligned}                                                     \tag{1.1}
\]

### Lemma 1.1 (two full endpoints)

The `2d` targets in (1.1) are distinct.  For each `i in {0,1}`, the row

\[
 T_{i,1}\subset T_{i,2}\subset\cdots\subset T_{i,d}
\]

is one saturated full PBBS piece.  The two rows are consecutive endpoint
chains of the literal word

\[
                     Q+z_0,\ldots,Q+z_d.
\]

Hence one such packet serializes two full pieces while spending no private
reset between them.

#### Proof

At fixed `j`, the two private windows differ by `z_{d-j}` versus `z_d`, so
they are distinct.  Different values of `j` give different ranks.  Each
row grows by one new tuple element at every step, and (1.1) is exactly the
sliding-union normal form for the last two endpoints of the displayed word.
\(\square\)

Thus the packet hypergraph has one vertex for every target in the rank band

\[
                         s,s+1,\ldots,s+d-1
\]

and one `2d`-edge for every pair `(Q,mathbf z)`.

## 2. Exact core-pair collision probability

Fix two cores `P,Q` and put

\[
 A=P\setminus Q,\qquad B=Q\setminus P,\qquad |A|=|B|=h.
\]

Choose the two ordered tuples independently and uniformly.  Equal targets
can occur only at a common depth `j>=h`.  They then have the unique form

\[
 P\cup(B\cup C)=Q\cup(A\cup C),
 \qquad C\in{[n]\setminus(P\cup Q)\choose j-h}.                    \tag{2.1}
\]

Each of the two designated `j`-windows of a random tuple is a uniform
`j`-subset of a `v`-set.  Therefore a union bound over the four ordered
window pairs gives

\[
 \boxed{
 p_h\le
 4\sum_{j=h}^{d}
 { {v-h\choose j-h}\over {v\choose j}^{,2}}.}                    \tag{2.2}
\]

The first designated window pair gives the matching lower bound

\[
                         p_h\ge {1\over{v\choose h}^{,2}}.          \tag{2.3}
\]

### Lemma 2.1 (first-depth domination)

Fix any constant `lambda` with

\[
                         \pi/4<\lambda<1.
\]

For all sufficiently large parameters and every `1<=h<=d`,

\[
 \boxed{
 {1\over{v\choose h}^{,2}}
 \le p_h\le
 {4\over1-\lambda}{1\over{v\choose h}^{,2}}.}                    \tag{2.4}
\]

#### Proof

Let the `j`-th summand in (2.2), without the factor four, be `a_j`.  Direct
cancellation gives

\[
 {a_{j+1}\over a_j}
  ={(j+1)^2\over(j+1-h)(v-j)}.                                     \tag{2.5}
\]

The right side is maximized, over `h<=j<=d`, when `h=j`, and is then at
most

\[
                         {(d+1)^2\over v-d}.
\]

At the optimal deadline, `d^2/n -> pi/8` and `v/n ->1/2`, so this ratio
tends to `pi/4`.  It is therefore at most `lambda` eventually.  Summing the
geometric majorant and using `a_h=1/binom(v,h)^2` proves the upper bound;
(2.3) proves the lower bound. \(\square\)

## 3. Independent packets have a growing conflict degree

A fixed `q`-core has exactly

\[
                         {q\choose h}{v\choose h}                    \tag{3.1}
\]

other cores at Johnson distance `h`.  Combining (2.4) with (3.1), the
expected number of conflicting independently randomized packets, when one
packet is put on every core, is between

\[
 \sum_{h=1}^d {q\choose h}/{v\choose h}
 \quad\hbox{and}\quad
 {4\over1-\lambda}
 \sum_{h=1}^d {q\choose h}/{v\choose h}.                            \tag{3.2}
\]

For `h<=d`,

\[
 {q\choose h}/{v\choose h}
   =\prod_{i=0}^{h-1}{q-i\over v-i}.
\]

Here `q/v=1-Theta(d/n)`.  Hence the product is bounded below by a positive
constant for `h<=c d`, for any sufficiently small fixed `c>0`, and is at
most one.  Consequently

\[
 \boxed{\mathbb E\deg_{\rm conflict}=\Theta(d).}                    \tag{3.3}
\]

Selecting a fixed positive density of cores independently still leaves
`Theta(d)` conflicts per selected packet.  Thus one-shot random selection
plus deletion cannot prove the required constant-density matching.

## 4. Exact target load and fractional matching

Fix a target `X` of rank `q+j`.  It contains exactly

\[
                         {q+j\choose j}
\]

possible cores.  For any one of those cores, the two shifted `j`-windows
are different and each is uniform.  Therefore a random packet on that core
contains `X` with exact probability

\[
                         {2\over{v\choose j}}.                        \tag{4.1}
\]

If every core is activated with probability `rho`, the expected load at
`X` is

\[
 2\rho,{{q+j\choose j}\over{v\choose j}}le2\rho,                 \tag{4.2}
\]

because `q+j<=v` throughout the top slab.

More invariantly, average uniformly over all packets and give them total
fractional mass `T`.  Symmetry inside each rank gives load

\[
                         {2T\over {n\choose s+j-1}}                  \tag{4.3}
\]

at every rank-`(s+j-1)` target.  The band is increasing, so its smallest
layer is rank `s`.  Consequently every

\[
                         T\le {1\over2}{n\choose s}                  \tag{4.4}
\]

is a fractional matching size.

At the optimal deadline,

\[
 {{n\choose s}\over W}\longrightarrow e^{-\pi}.                   \tag{4.5}
\]

The reset deficit is

\[
 \theta W+o(W),\qquad
 \theta=2\sigma-1
       =4\sum_{a\ge1}e^{-4\pi a^2}
       =0.0000139\ldots .                                           \tag{4.6}
\]

Since

\[
 {e^{-\pi}/2\over\theta}>1500,                                    \tag{4.7}
\]

the two-endpoint packet hypergraph has over three orders of magnitude more
fractional matching capacity than is needed to absorb every missing reset.

## 5. What this changes

The maximal-cycle route sought a constant-density family of edges having
rank `Theta(nd)`.  The shortest useful packet has:

\[
 \boxed{
 \text{edge rank }2d=\Theta(\sqrt n),\qquad
 \text{fractional margin }>1500,\qquad
 \text{random conflict degree }\Theta(d).}
\]

Thus the exact alternative star theorem is:

> **Two-endpoint theta matching.**  The packet hypergraph above has a
> matching of size `(theta+o(1))W`.

Such a matching would pair every full piece responsible for the theta reset
deficit.  It would close the *target-disjoint shared-reset* row without any
all-depth maximal-star packing or nested-suffix maximum-link invariant.

The theorem does not follow from the fractional point alone: growing-rank
projective decorations show that regularity and pair-codegree bounds can
hide an integral obstruction.  Existing nibble theorems are stated with a
hierarchy in which the uniformity is fixed before the error constants, so
they cannot simply be cited with `2d -> infinity`.  What is now required is
either

1. a packet-specific expansion/switching proof of the two-endpoint theta
   matching; or
2. a quantitatively uniform small-density nibble theorem whose hypotheses
   include the complete higher-codegree sequence of this packet system.

Even after that matching, placement in the varying PBBS owner envelopes and
the common compiler remain separate global rows.  The result here is a
strict reduction of the all-depth star-factor gate, not a proof of
`nu(k)<=B(k)+O(1)`.
