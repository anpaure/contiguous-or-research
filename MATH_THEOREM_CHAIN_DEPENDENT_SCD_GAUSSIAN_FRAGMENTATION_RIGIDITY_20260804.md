# Chain-dependent SCD cutting: Gaussian fragmentation rigidity and the minimum-chunk obstruction

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  The theorem identifies
the unique possible scaling limit of any chain-dependent cut profile which
passes the exact socket threshold inequalities.  It rules out every
minimum-number-of-chunks rule, independently of where its cuts are placed,
and gives a sharper top-threshold obstruction for balanced equal-part cuts.
It also proves that any successful literal attachment is asymptotically
capacity-diagonal.  It does **not** construct the required fragmentation or
the named containment matching.

## 0. Setup

Work first in the even Boolean lattice `B_(2r)`.  Put

\[
 C_s={2r\choose s},\qquad W=C_r,
\]

and let `d=d(2r)` be the coefficient-one depth.  Thus, with

\[
 A={\sqrt\pi\over2},\qquad t=r-d,
\]

we have

\[
 {d\over\sqrt r}\longrightarrow A.                 \tag{0.1}
\]

Write

\[
 H_b=C_b-C_{b-1}\qquad(C_{-1}=0).                   \tag{0.2}
\]

There are exactly `H_b` chains of bottom rank `b` in every symmetric-chain
decomposition.  Below the collar bottom `t`, such a chain has residual
length `t-b`.  The unique chain beginning at the empty set loses one cell
when the empty set is deleted; that `O(1)` discrepancy is immaterial below.

The owner sockets of capacity `u` have multiplicity `H_(t+u)`, and the
endpoint triangle supplies one further socket of every capacity
`u=1,...,d`.

Given an arbitrary chain-dependent cutting of all residual SCD chains into
nonempty consecutive chunks of lengths at most `d`, let `n_q` be the number
of chunks of length at least `q`.  The exact rank-density threshold theorem
requires

\[
 n_q\le W-C_{t+q-1}+d-q+1\qquad(1\le q\le d).       \tag{0.3}
\]

The point of this note is that (0.3), although only one-dimensional, is
asymptotically rigid.

## 1. The two Gaussian measures

Define the augmented residual-row measure and socket-capacity measure by

\[
 \nu_r={1\over W}\sum_{b=0}^{t-1}H_b
       \delta_{(t-b)/\sqrt r},                       \tag{1.1}
\]

and

\[
 \mu_r={1\over W}\sum_{u=1}^d(H_{t+u}+1)
       \delta_{u/\sqrt r}.                           \tag{1.2}
\]

Replacing the augmented bottom chain in (1.1) by the actual punctured one
changes one atom by `1/sqrt(r)` and has no limiting effect.

### Theorem 1.1 (Gaussian row and socket limits)

The measures in (1.1)--(1.2) converge weakly to

\[
 \boxed{
 d\nu(x)=2(A+x)e^{-(A+x)^2}\,dx\quad(x>0),
 }
                                                               \tag{1.3}
\]

and

\[
 \boxed{
 d\mu(y)=2(A-y)e^{-(A-y)^2}\,dy\quad(0<y<A).
 }
                                                               \tag{1.4}
\]

Their count masses are

\[
 \nu((0,\infty))=e^{-A^2},\qquad
 \mu((0,A))=1-e^{-A^2}.                              \tag{1.5}
\]

Their first moments are equal:

\[
 \boxed{
 \int_0^\infty x\,d\nu(x)
 =\int_0^A y\,d\mu(y)
 =\int_A^\infty e^{-z^2}\,dz.
 }                                                     \tag{1.6}
\]

#### Proof

For fixed `x>=0`, telescoping (0.2) gives

\[
 \nu_r([x,\infty))
 ={C_{t-\lceil x\sqrt r\rceil}\over W}+o(1).
                                                               \tag{1.7}
\]

The local central-binomial estimate, uniformly on compact `x`-ranges,
is

\[
 {C_{r-z\sqrt r}\over W}\longrightarrow e^{-z^2}.
                                                               \tag{1.8}
\]

Equations (0.1), (1.7), and (1.8) give

\[
 \nu_r([x,\infty))\longrightarrow e^{-(A+x)^2},       \tag{1.9}
\]

whose negative derivative is (1.3).  Gaussian tail domination supplies
tightness and justifies passage beyond compact sets.

Likewise, for `0<y<A`,

\[
 \mu_r([y,A+o(1)])
 ={W-C_{t+\lceil y\sqrt r\rceil-1}\over W}+o(1)
 \longrightarrow 1-e^{-(A-y)^2}.                     \tag{1.10}
\]

The `d` boundary atoms have total mass `d/W=o(1)`.  Differentiating
(1.10) gives (1.4), and setting `x=y=0` gives (1.5).

For the first moment of (1.3), substitute `z=A+x` and integrate by parts:

\[
 \begin{aligned}
 \int_0^\infty 2x(A+x)e^{-(A+x)^2}\,dx
 &=\int_A^\infty 2(z-A)z e^{-z^2}\,dz\\
 &=\int_A^\infty e^{-z^2}\,dz.
 \end{aligned}                                        \tag{1.11}
\]

For (1.4), substitute `z=A-y`:

\[
 \int_0^A2y(A-y)e^{-(A-y)^2}\,dy
 =A-\int_0^A e^{-z^2}\,dz.                           \tag{1.12}
\]

Finally

\[
 A={\sqrt\pi\over2}=\int_0^\infty e^{-z^2}\,dz,
\]

so (1.11) and (1.12) agree and give (1.6).  \(\square\)

The equality of moments is the continuum form of the coefficient-one
scalar ledger.  In probabilistic language, if `Z` has Rayleigh density
`2z e^(-z^2)`, then `A=E Z`; residual rows are the positive deviations
`Z-A`, while sockets are the negative deviations `A-Z`.

## 2. Zero-waste rigidity

For a declared cutting, define its chunk measure

\[
 \eta_r={1\over W}\sum_F\delta_{|F|/\sqrt r},         \tag{2.1}
\]

where the sum is over all residual chunks.

### Theorem 2.1 (unique feasible fragmentation limit)

Suppose the cut profile satisfies every threshold inequality (0.3).
Then

\[
 \boxed{\eta_r\Longrightarrow\mu.}                   \tag{2.2}
\]

More generally, (2.2) still follows if the largest positive threshold
violation is `o(W)`.

Thus the Gaussian fragmentation problem is not merely a convenient model:
it is forced.  Any asymptotically feasible chain-dependent rule must
fragment the row measure `nu` into **exactly** the capacity measure `mu`.

#### Proof

The `q=1` inequality bounds the total mass of `eta_r`, and all its atoms lie
in `[0,d/sqrt(r)]`, a fixed compact interval asymptotically.  Take an
arbitrary weakly convergent subsequence, with limit `eta` on `[0,A]`.

For every fixed `y>0`, put `q=ceil(y sqrt(r))` in (0.3).  Equations
(1.10) and (2.1) give, at every continuity point,

\[
 \eta([y,A])\le\mu([y,A]).                            \tag{2.3}
\]

The sum of all chunk lengths is the residual target count `D_r`.  The sum
of all socket capacities is `D_r+sigma_r`, where

\[
 0\le\sigma_r<W+d                                      \tag{2.4}
\]

by minimality of `d`.  Therefore

\[
 \int x\,d\eta_r(x)
 =\int y\,d\mu_r(y)-{\sigma_r\over W\sqrt r}.
                                                               \tag{2.5}
\]

The last term tends to zero.  Theorem 1.1 and bounded support imply

\[
 \int_0^A\eta([y,A])\,dy
 =\int x\,d\eta(x)
 =\int y\,d\mu(y)
 =\int_0^A\mu([y,A])\,dy.                             \tag{2.6}
\]

The nonnegative difference between the two tail functions in (2.3) has
integral zero, hence vanishes almost everywhere.  Right continuity then
gives equality for every `y>0`; consequently `eta` and `mu` agree on
`(0,A]`.

The `q=1` inequality also gives

\[
 \eta([0,A])\le\mu([0,A]).                            \tag{2.7}
\]

Since the two measures already agree on `(0,A]`, (2.7) forbids an atom of
`eta` at zero.  Thus `eta=mu`.  Every subsequential limit is the same, so
the whole sequence converges.  An `o(W)` additive violation changes
(2.3) by `o(1)` and the same proof applies.  \(\square\)

### Corollary 2.2 (macroscopic failure is unavoidable off `mu`)

If a family of cutting rules has a weak chunk limit different from `mu`,
then along some subsequence

\[
 \max_{1\le q\le d}
 \left(n_q-W+C_{t+q-1}-d+q-1\right)_+=\Omega(W).
                                                               \tag{2.8}
\]

This follows by contraposition and compactness from Theorem 2.1.

## 3. Minimum-chunk cutting is impossible

The minimum possible number of pieces in a residual chain of length `L`
is `ceil(L/d)`.  This number is independent of the cut locations.

### Theorem 3.1 (all minimum-piece rules fail)

Every cutting which uses exactly `ceil(L/d)` chunks on every residual
chain violates the socket thresholds by `Omega(W)` in all sufficiently
large even dimensions.

#### Proof

By the tail-sum formula for the ceiling, the limiting number of chunks per
`W` is

\[
 p_{\min}
 =\sum_{j\ge0}\nu((jA,\infty))
 =\sum_{m\ge1}e^{-m^2A^2}
 =\sum_{m\ge1}e^{-\pi m^2/4}.                         \tag{3.1}
\]

On the other hand, Theorem 2.1 forces every feasible chunk measure to have
count mass

\[
 p_{\rm sock}=\mu((0,A))=1-e^{-\pi/4}.               \tag{3.2}
\]

These constants are strictly separated.  For example,

\[
 \sum_{m\ge2}e^{-\pi m^2/4}
 \le {e^{-\pi}\over1-e^{-5\pi/4}},                  \tag{3.3}
\]

while the elementary bounds

\[
 e^{-\pi/4}<0.456,\qquad e^{-\pi}<0.044,
 \qquad e^{-5\pi/4}<0.020
\]

give

\[
 p_{\min}<0.501<0.544<p_{\rm sock}.                  \tag{3.4}
\]

Thus a minimum-piece rule cannot have the forced limit `mu`.  Corollary
2.2 gives the stated linear violation.  \(\square\)

This theorem is stronger than the common-slab obstruction: changing the
phase, moving every cut separately, or balancing the pieces inside each
chain cannot help while the number of pieces remains minimal.  A successful
rule must make a positive-density bank of additional cuts.

## 4. Balanced equal-part cutting fails at the top

Consider the canonical balanced minimum-piece rule: a chain of length `L`
uses `m=ceil(L/d)` chunks, whose lengths differ by at most one.

### Theorem 4.1 (balanced top-tail obstruction)

The limiting chunk measure of the balanced rule is

\[
 \eta_{\rm bal}(B)
 =\sum_{m\ge1}\int_{(m-1)A}^{mA}
 m\,\mathbf 1_{\{x/m\in B\}}\,d\nu(x).              \tag{4.1}
\]

It violates a threshold `q=(A-epsilon+o(1))sqrt(r)` by `Omega(W)` for
every sufficiently small fixed `epsilon>0`.

#### Proof

Rounding the nearly equal integer parts changes their scaled lengths by
`o(1)`, so (4.1) follows directly from (1.3).  The `m=1` rows alone give

\[
 \eta_{\rm bal}([A-\epsilon,A])
 \ge\int_{A-\epsilon}^A2(A+x)e^{-(A+x)^2}\,dx.        \tag{4.2}
\]

The right side is `nu(A) epsilon+O(epsilon^2)`, with

\[
 \nu(A)=4Ae^{-4A^2}=4Ae^{-\pi}>0.                    \tag{4.3}
\]

But the available socket tail is exactly

\[
 \mu([A-\epsilon,A])=1-e^{-\epsilon^2}
 =\epsilon^2+O(\epsilon^4).                          \tag{4.4}
\]

For all sufficiently small fixed `epsilon`, (4.2) exceeds (4.4) by a
positive constant.  Taking
`q=ceil((A-epsilon)sqrt(r))` proves the linear threshold violation.
\(\square\)

The failure mechanism is sharp: equal balancing leaves a linear density of
chunks just below the maximal size `d`, whereas the SCD supplies only a
quadratically thin capacity tail there.

## 5. Consequence for literal containment matching

Suppose a declared chunk bank is actually matched into the literal owner
and boundary sockets.  If chunk `F` of length `a_F` is assigned to capacity
`u_F`, define its waste to be `u_F-a_F`; an unused socket has waste equal
to its full capacity.

### Theorem 5.1 (capacity-diagonal rigidity)

The total waste of every exact attachment is exactly

\[
 \boxed{
 \sum_{F\ \mathrm{matched}}(u_F-a_F)
 +\sum_{R\ \mathrm{unused}}u_R=\sigma_r.
 }                                                     \tag{5.1}
\]

Consequently, for every fixed `epsilon>0`, only `o(W)` sockets can be
either

* unused with capacity at least `epsilon sqrt(r)`, or
* matched to a chunk shorter than their capacity by at least
  `epsilon sqrt(r)`.

Equivalently, every subsequential joint scaling limit of

\[
 {1\over W}\sum_{F\ \mathrm{matched}}
 \delta_{(|F|/\sqrt r,\,u_F/\sqrt r)}                \tag{5.2}
\]

is supported on the diagonal `x=y` and has both macroscopic marginals
equal to `mu`.

#### Proof

The chunks partition the residual targets, so their total length is
`D_r`.  The sockets have total capacity `D_r+sigma_r`.  Subtraction gives
(5.1).  By (2.4), the number of terms of size at least
`epsilon sqrt(r)` is at most

\[
 {\sigma_r\over\epsilon\sqrt r}=O(W/\sqrt r)=o(W).
\]

The joint-limit statement follows from Theorem 2.1 and the fact that the
mean nonnegative displacement `(u_F-|F|)/sqrt(r)` tends to zero.  \(\square\)

Thus there is no positive-density capacity reserve available to repair a
poorly correlated pair of SCDs after the cutting is chosen.  At
coefficient one, the literal containment theorem must correlate the two
SCDs while constructing the fragmentation: almost every macroscopic
capacity-`u` root must receive a chunk of asymptotically the same load.

## 6. Odd dimensions and exact frontier

For `k=2r-1`, use either widest middle rank and the analogous collar.  The
central-binomial ratios and `d/sqrt(r)` have the same limits; the missing
endpoint capacity and all parity corrections have mass `o(W)` after the
normalization above.  Therefore Theorems 1.1--5.1, with the same `nu` and
`mu`, hold verbatim asymptotically.

The lower cross-SCD route has therefore reached the following exact
frontier.

1. Common slabs fail, and now every minimum-number-of-pieces adaptive rule
   fails as well.
2. A successful chain-dependent rule must create a positive-density bank
   of additional cuts and realize the unique Rayleigh fragmentation
   `nu -> mu`.
3. Any literal attachment realizing it has zero leading waste and is
   capacity-diagonal.
4. What remains is a genuine fragmentation theorem, followed by a
   correlated choice of the residual and collar SCDs satisfying the named
   containment Hall cuts.  Independent or post-hoc correlation has no
   macroscopic capacity cushion.

No coefficient-one or bounded-deficiency construction is claimed here.
