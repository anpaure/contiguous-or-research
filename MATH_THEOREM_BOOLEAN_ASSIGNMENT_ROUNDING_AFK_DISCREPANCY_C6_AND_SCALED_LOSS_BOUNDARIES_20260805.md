# Boolean assignment rounding: exact scope of AFK, discrepancy, `C6`, and scaled-loss routes

**Date:** 2026-08-05  
**Method:** pure mathematics and primary-source theorem-scope audit; no
finite search, solver, or H100 computation  
**Status:** four proof shortcuts are sharply delimited.  None currently
proves the full coloured Boolean one-step oracle.  The surviving
constructive target is an exact Boolean-specific assignment theorem after
the old-image occupancy projection has been separated off.

## 0. Required oracle and scaling

Use the augmented Boolean interface `J_q` of
`MATH_THEOREM_COLORED_BOOLEAN_ONE_STEP_UNIFORM_FLOW_CONTRACTION_AND_EXACT_ROUNDING_GAP_20260805.md`.
Its two shores have size

\[
                         N=\binom{2r}{q+1},
\tag{0.1}
\]

so `log N=Theta(r)` throughout the central collar.  There are
`exp(O(r))=N^(O(1))` prescribed colour-by-future-owner tests.  At the
critical interface their smallest relevant fractional mean has scale

\[
                         \mu=\Theta(rD)=\Theta(r^{3/2}),
 \qquad D=\Theta(\sqrt r).
\tag{0.2}
\]

The desired one-step theorem is an exact perfect matching with the uniform
edge marginals and Bernstein/Chernoff deviations for all those tests.

## 1. Arora--Frieze--Kaplan is almost assignment, not exact assignment

Theorem 1.3 of Arora--Frieze--Kaplan starts from a fractional perfect
matching on an `N by N` bipartite graph and returns a matching with at
least

\[
                         N-o(N)
\tag{1.1}
\]

edges.  For a nonnegative linear statistic with maximum coefficient `A`,
its displayed guarantee is

\[
 aM\ge(1-o(1)),a x-\widetilde O(A).
\tag{1.2}
\]

Their Section 5 makes the parameters more explicit.  With

\[
 \delta=O\!\left({\log\log N\over\log N}\right),
 \qquad
 k=\Theta(\log N),
 \qquad
 \Delta=O(\log^3 N),
\tag{1.3}
\]

equations (27), (30), and (31) give a nonnegative weight error of the form

\[
 \delta,a x+\widetilde O(kA\Delta).
\tag{1.4}
\]

The tilde hides further logarithmic/failure-probability factors.  Thus the
published bound is polylogarithmic in `N`, not a Bernstein bound in the
mean `mu`.  In the Boolean scaling the proof controls the explicitly
displayed `k Delta` contribution only at `O(r^4)` before hidden logarithms,
while the
independent-style deviation needed at (0.2) is on the order of
`sqrt(mu r)=Theta(r^(5/4))`.

More fundamentally, (1.1) is not a perfect matching.  Applying (1.2) to
the all-ones statistic gives a loss on the order allowed by the theorem,
not exact preservation of every Boolean chain continuation.

### Conclusion 1.1

The AFK theorem does not prove the one-step oracle.  This is a theorem-
scope conclusion, not a lower bound against a sharper analysis of their
algorithm: a Boolean-specific refinement could conceivably improve both
the additive term and the unmatched residue.

## 2. Exact discrepancy rounding needs rank slack which assignment faces can lose

Bansal's sub-isotropic rounding theorem has an exceptionally relevant
form.  If an iterated rounding process on `f` fractional variables can at
every step preserve a constraint matrix of rank at most

\[
                         (1-\delta)f
\tag{2.1}
\]

for one fixed `delta>0`, then it outputs a reachable integral point with
the exact starting marginals and Bernstein concentration weakened only by

\[
                         \beta={20\over\delta}.
\tag{2.2}
\]

This would solve the required concentration if an exact-assignment
rounding trajectory with constant rank slack were available.

### Proposition 2.1 (long-cycle rank obstruction)

On a face of a bipartite perfect-matching polytope whose fractional support
is one even cycle with `f` edges, the exact degree equations have rank

\[
                         f-1.
\tag{2.3}
\]

Consequently any sub-isotropic application which preserves that assignment
face has

\[
                         \delta\le {1\over f},
 \qquad
                         \beta\ge20f.
\tag{2.4}
\]

#### Proof

The unoriented vertex-edge incidence matrix of a connected bipartite graph
with `f` vertices and `f` edges has rank `f-1`.  Equivalently, the even
cycle perfect-matching face is one-dimensional, so its affine hull has
codimension `f-1`.  Exact movement within that face must retain this affine
hull.  Substitution in (2.1)--(2.2) gives (2.4). `square`

This does not prove that every rounding trajectory must end on one long
cycle.  It proves that the generic theorem cannot be invoked merely from
assignment integrality.  A successful application needs an additional
Boolean theorem that decomposes the evolution into bounded alternating
circuits, or otherwise keeps a constant-dimensional fraction free at every
step.

The earlier Bansal--Nagarajan approximation-friendly discrepancy theorem
does not fill this gap.  Its exact combinatorial extension preserves one
matroid polytope.  Perfect matchings are the common bases of two partition
matroids, and a nontrivial family of graph-perfect-matchings is not itself
the base family of a matroid.  Its general linear-system version allows
violations of the assignment equalities rather than preserving a perfect
matching.

## 3. Exact sensitivity of old-only Boolean `C6` switches

Let `A subset binom([n],q)` be a colour class and let `U subset [n]` have
size `v`.  A Boolean incidence hexagon has core
`C in binom([n],q-1)` and distinct active labels `a,b,c notin C`.  It
toggles the two alternating matchings between

\[
 C+a,C+b,C+c
 \quad\hbox{and}\quad
 C+ab,C+bc,C+ca.
\tag{3.1}
\]

### Theorem 3.1 (`C6` sensitivity identity)

The number of unoriented old-only hexagons which change the number of
`A`-coloured images inside `binom(U,q+1)` is

\[
 (n-v)\,
 \left|\partial_{J(v,q)}
       \left(A\cap\binom Uq\right)\right|.
\tag{3.2}
\]

#### Proof

A toggle can change the statistic only when `C subset U` and exactly two
active labels lie in `U`.  If these are `a,b`, the unique upper hexagon
vertex in `U` is `C+ab`, and its provider toggles between `C+a` and `C+b`.
This changes the colour count exactly when that Johnson edge crosses the
boundary of `A cap binom(U,q)`.  Every boundary edge has `n-v` choices for
the third active label outside `U`. `square`

### Corollary 3.2 (sharp old-only switch obstruction)

Take `A=binom(U,q)`.  Then the right side of (3.2) is zero, while the
fractional mean of the statistic is

\[
 {v-q\over n-q}\binom vq>0.
\tag{3.3}
\]

Hence no packing, repeated round, or spectral analysis using only old-only
`C6` toggles can prove concentration for all colourings.  Such switches
randomize colours only when the induced Johnson boundary is large.  The
complete oracle must also vary old-versus-dummy occupation, for example
through old--dummy `C4`s or longer mixed alternating circuits.

The companion theorem
`MATH_THEOREM_BOOLEAN_MATCHING_IMAGE_STRONG_RAYLEIGH_AND_COLORED_ASSIGNMENT_GATE_20260805.md`
shows that the actual uniform perfect matching nevertheless concentrates
the statistic (3.3): its old image set is Strong Rayleigh.  Thus the
failure is in the restricted `C6` mechanism, not in the desired law.

## 4. Exact tail cost of one dropped continuation

Suppose one scheduled interval piece of length `L=a+b` is split at a
dropped continuation into pieces of lengths `a,b>=1`.  Let `K_s` denote
the number of pieces of length at least `s`.  The change caused by this one
split is exactly

\[
 \Delta K_s=
 \begin{cases}
  +1,&1\le s\le\min(a,b),\\
   0,&\min(a,b)<s\le\max(a,b),\\
  -1,&\max(a,b)<s\le a+b,\\
   0,&s>a+b.
 \end{cases}
\tag{4.1}
\]

#### Proof

The old piece contributes `1_(a+b>=s)`, while the two new pieces contribute
`1_(a>=s)+1_(b>=s)`.  Comparing these three indicators gives (4.1).
`square`

Thus every loss creates one extra chunk, but its capacity-tail cost is not
determined by the chunk count.  An endpoint-adjacent break with
`min(a,b)=1` costs only the first tail.  A central break costs one unit in
many consecutive tails.

## 5. Why the raw linear socket reserve does not yet pay scaled losses

The general scaled matching theorem used in the one-step note has a tail
exponent proportional to `gamma mu`, where `(1-gamma)x` is rounded.  To
union-bound `exp(O(r))` tests with (0.2), one needs

\[
                         \gamma=\Omega(1/D)
                         =\Omega(r^{-1/2}).
\tag{5.1}
\]

At one interface this drops `Theta(gamma W)=Theta(W/sqrt r)` old
continuations.  Across `D=Theta(sqrt r)` interfaces, without
nonaccumulation, it creates

\[
                         \Theta(\gamma WD)=\Theta(W)
\tag{5.2}
\]

breaks.

The two-SCD socket ledger proves a raw count reserve `S-P>=eta W`.  It does
not prove the typed containment/capacity Hall matching, and raw count does
not control the conjugate tails in (4.1).  The proved one-depth-shift
reserve is tail-faithful but vanishing: its first adjacent-depth margin is
only

\[
                         H_t=\Theta(WD/r)
                         =\Theta(W/\sqrt r),
\tag{5.3}
\]

and the deeper comparison is performed at `W/r` scale.  Arbitrary interior
breaks from (5.2) can charge `Theta(W)` units to several tails, far beyond
those proven margins.

Conversely, even at one interface, choosing `gamma=O(1/r)` so that the
loss is at most the deeper `W/r` tail scale gives

\[
                         \gamma\mu=O(\sqrt r),
\tag{5.4}
\]

which cannot beat an `exp(O(r))` union bound.

### Conclusion 5.1

Scaled loss remains viable only with an additional structural theorem,
such as:

1. losses occur within `O(1)` of already scheduled endpoints, so (4.1)
   charges only `O(1)` low tails;
2. a typed, capacity-tail-faithful reserve of constant linear scale exists;
   or
3. losses are regenerated/merged so the number of live breaks contracts
   between interfaces.

The raw `eta W` socket count alone is not such a theorem.

## 6. Exact surviving constructive target

The companion Strong Rayleigh image theorem now controls:

* which upper vertices are occupied by old rather than dummy continuations;
* all future-owner sums after aggregating over the old colours; and
* the complementary aggregate dummy occupancy.

The remaining exact one-step problem is narrower:

> Conditional on, or jointly with, the concentrated old image set, assign
> the coloured old vertices to those images so that every persistent
> colour-by-future-owner statistic has Bernstein deviation, while keeping
> the exact uniform edge marginals.

Any successful proof must exploit mixed old--dummy circuits, a bounded-
circuit exact iterated trajectory, or permanent-ratio control for the
conditional coloured assignment.  Generic Strong Rayleigh, AFK, an
unqualified exact-discrepancy theorem, old-only `C6`s, and raw socket count
have now been removed as standalone solutions.

## 7. Primary theorem references

* S. Arora, A. Frieze and H. Kaplan,
  *A new rounding procedure for the assignment problem with applications
  to dense graph arrangement problems*, Mathematical Programming 92
  (2002), <https://www.aladdin.cs.cmu.edu/papers/pdfs/y2002/qap.pdf>.
* N. Bansal, *On a Generalization of Iterated and Randomized Rounding*,
  Theory of Computing 20(6), 2024,
  <https://theoryofcomputing.org/articles/v020a006/>.
* N. Bansal and V. Nagarajan,
  *Approximation-Friendly Discrepancy Rounding*,
  <https://arxiv.org/abs/1512.02254>.

The `C6` identity, fragmentation-tail identity, and all Boolean scaling
conclusions are proved directly above.
