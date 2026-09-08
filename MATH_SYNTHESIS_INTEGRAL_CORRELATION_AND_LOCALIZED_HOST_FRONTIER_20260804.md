# Integral correlation and the localized-host frontier for `B+O(1)`

**Date:** 2026-08-04  
**Status:** proof-safe synthesis of the pure-mathematical push.  No new
all-dimensional upper bound is claimed.

## 0. Verdict

The unconditional finite statement remains

\[
                    \nu(k)=B(k)\qquad(0\le k\le16),
\]

and `k=17` remains the first unresolved finite dimension.  The present
results do not prove

\[
 \nu(k)=B(k),\qquad \nu(k)\le B(k)+1,
 \qquad\hbox{or}\qquad \nu(k)\le B(k)+O(1)
\]

for all `k`.

They do support one clean global conclusion:

\[
 \boxed{\text{Every remaining obstruction exposed in this push is a
 correlated integral/physical choice, not a scalar or fractional cut.}}
 \tag{0.1}
\]

More precisely:

* the exact triangular endpoint capacities pass every Boolean rank and
  Greene--Kleitman cut and admit an exact fractional named flag factor;
* the canonical two-SCD lower architecture has exact total capacity, and in
  sufficiently large even dimensions it has a strict raw socket-count
  reserve;
* the residual typed router is automatic after one type-legal,
  degree-weighted pair of private occurrence factors is co-instantiated in
  the same residual state;
* the aperture token has a large exact product-Johnson seam reservoir, and
  every nonempty fixed-total-coordinate interface state extends once both
  Johnson-slice margins tend to infinity;
* in even ground dimension, residence at the required `Theta(sqrt(k))`
  scale is available on all but an exponentially small fraction of central
  owners, as a disjoint cycle factor rather than one global carrier.

The failures all concern simultaneous exactness:

* independent lower rounding leaves `Omega(W)` named holes;
* common rank-slab chunkings fail the exact lower socket thresholds;
* a fixed upper factor can have separately feasible target witnesses with
  no common occurrence section;
* bounded scope per seam constraint can still reject every eligible token;
* pairwise module compatibility need not give a common lower/upper/router
  host; and
* the exponentially small nonresident owner family is still exponentially
  large in absolute size and cannot be discarded.

## 1. The lower endpoint factor is fractionally exact

At word length `W+h`, the strict-lower witnesses grouped by right endpoint
have the exact sorted capacities

\[
          (\underbrace{h,\ldots,h}_{W+1},h-1,h-2,\ldots,1).       \tag{1.1}
\]

Their total is

\[
                         hW+{h+1\choose2}.                         \tag{1.2}
\]

For `h>=d(k)` in the nontrivial range `d(k)>=1`, every generalized
Greene--Kleitman capacity inequality and
every exact rank-to-labelled-slot flow cut passes.  There is a fractional
selection of one legal Boolean flag in every labelled slot which covers
every named strict-lower target with total mass one.  Under uniform capacity
`h`, the fractional optimum is exactly

\[
 \kappa_h^*=\max\left\{{k\choose r-1},{\Lambda\over h}\right\}.   \tag{1.3}
\]

At `h=d`, the available `W+d` slots exceed (1.3) by at least `(d-1)/2`.
Thus neither total capacity, the largest rank, nor any generalized
antichain cut explains the missing integral word.

This relaxation is not automatically integral.  A disjoint union of two
`(h+1)`-chains and `n-3` singleton chains has a perfect complete-multipartite
incomparability graph, passes the same triangular capacity norms, and has a
fractional `n`-slot cover, but needs `n+1` integral bounded chains.  Hence a
Boolean-specific rounding theorem is necessary.

The natural product rounding is quantitatively wrong.  In the symmetric
fractional factor, independently sample one flag per slot.  Already at rank
`r-1`, at least a constant fraction of the named targets is uncovered with
probability `1-exp(-Omega(W))`; repairing the outcome needs `Omega(W)` slot
changes.  Any coefficient-one proof must impose global dependence before
rounding, not repair a product sample locally.

## 2. The strongest concrete lower architecture is two correlated SCDs

Fix `t=r-d`.  One collar SCD supplies owner sockets with exact capacity
histogram

\[
 \#\{\text{capacity-}u\text{ owner sockets}\}
 ={k\choose t+u}-{k\choose t+u-1},\qquad1\le u\le d,  \tag{2.1}
\]

including exactly `W-C(k,r-1)` empty full-capacity owner sockets.  The
linear boundary supplies one additional socket of each capacity
`1,...,d`.  For any chunking of a second SCD below rank `t`, completion is
equivalent to one literal containment-and-capacity Hall system.

At the scalar level, total socket capacity minus lower demand is exactly

\[
                  \sigma=dW+{d+1\choose2}-\Lambda\ge0.             \tag{2.2}
\]

For even `k`, the canonical collar has

\[
 \#\text{short sockets}=(1-e^{-\pi/4}+o(1))W>0.544W,               \tag{2.3}
\]

whereas splitting all residual SCD tails into chunks of size at most `d`
requires fewer than `0.501W` chunks.  Thus there is strict raw-count and
capacity reserve.

However, how the second SCD is cut is decisive.  In the symmetrized
rank-density relaxation, if `A_(s,a)` is the mass of chunks of load `a` and
top rank `s`, the exact threshold system is

\[
 \sum_s\sum_{a\ge q}A_{s,a}
 \le W-{k\choose t+q-1}+d-q+1,
 \qquad1\le q\le d.                                  \tag{2.4}
\]

Maximal `d`-slabs already violate the `q=d` cut by `Theta(W)`.  More
strongly, in all sufficiently large even dimensions every decomposition
using one common grid of consecutive rank slabs violates (2.4): its `q=1`
and top-slab threshold inequalities contradict one another in the Gaussian
limit.  Therefore a successful two-SCD proof must choose **chain-dependent
cut ranks**, then prove the stronger literal containment Hall cuts for one
correlated collar SCD.

This is the sharpest current lower construction target:

> **Chain-dependent cross-SCD Hall.**  Choose the cut positions on the
> residual SCD chains nonuniformly so that (2.4) holds, then choose the
> collar and residual SCDs jointly so every literal Hall cut vanishes.

It remains open, as does the stronger countdown-compatible two-endpoint
serialization required by one source word.

## 3. The upper factor must be chosen with its occurrence section

There is no universal abstract fixed-factor theorem.  A directed four-cycle
with colour word `R,A,R,B` and two unique disjoint two-edge interval
witnesses can force the two different `R` occurrences.  Each target is
separately feasible and every occurrence section already breaks the cycle,
yet no section realizes both targets.

The exact positive object is the dual target-choice CSP.  Choose one witness
per higher target; for each q1 colour, one relation requires all chosen
witnesses using that colour to use the same physical occurrence.  On a
running-intersection scope tree, semijoin pruning is exact.  Once a rainbow
witness selector is fixed, an immutable reserve Hall condition makes the
component-breaking forest independent of that selector.  Outside this
acyclic face, a literal colour-scope blocker LLL is sufficient under its
explicit probability/dependency inequalities.

The missing statement is not another marginal count.  It is a Boolean-host
theorem supplying one nonempty dual join (or one verified blocker-LLL
instance) together with reserve Hall and the lower chronology.

## 4. The seam and router are now localized exactly

Let `H` be the incoming rank-`(R-1)` token, `D` the aperture depth, and `F`
forbidden in the outgoing token.  Put

\[
 A=H-F,\qquad B=H^c-F,\qquad
 h=D-1-|F\cap H|,\qquad \ell=D-1.
\]

Eligible outputs avoiding `F` are exactly a product of Johnson slices

\[
                         {A\choose h}\times{B\choose\ell}.         \tag{4.1}
\]

For one complete joined host relation depending on total coordinate
footprint `U,V` with allowed local states `L`, the accepted count is

\[
 \sum_{(S,T)\in L}
 { |A|-|U|\choose h-|S|}
 { |B|-|V|\choose\ell-|T|}.                          \tag{4.2}
\]

Hence every nonempty fixed-total-footprint join extends once the footprint
fits on both sides of the slices.  A fixed physical occurrence-exception
bank costs at most its cardinality from (4.2).  More generally, exact
hypergeometric cylinder weights give a rare-defect DNF criterion and a
defect-transversal container criterion.

This cannot be weakened to “each constraint has bounded scope.”  The unary
events `x is a hole`, with pairwise disjoint coordinate supports, cover the
entire fixed-size slice.  Singleton physical occurrence events can likewise
cover every seam.  The real host must therefore admit a bounded **total**
projection, a small fixed occurrence exception bank, or a subunit total
rare-defect certificate mass.

For the residual common-cap router, full active-port rank is stronger than
necessary.  Let a claim--port factor be left `h`-regular and right degree at
most `h`; let a port--sink factor be left `q`-regular.  If the private
occurrence lifts coexist and every sink `s` satisfies

\[
              \sum_{f=ps}\deg_B(p)\le hq,                          \tag{4.3}
\]

then weight `1/(hq)` on every two-stage incidence chain.  All claim, port,
suffix, and sink loads are at most one, so integral max flow routes every
claim.  At `h=q=2`, two private occurrence-lifted factors suffice.  The
remaining issue is their common-state physical lift, not a hidden flow cut.

## 5. Residence is almost solved, but “almost” is not additive

In even ground dimension, pair the `2r` coordinates.  Fixing which pairs
are double, empty, and
singleton partitions `J(2r,r)` into induced cube cells `Q_m`, where `m` is
the number of singleton pairs.  On every cell with

\[
                  m\ge L+\lceil3\log_2r\rceil,
\]

the Goddyn--Gvozdjak long-bit-run Gray cycle gives a Johnson cycle whose
successive transitions of every varying physical coordinate are separated
by at least `L`; constant coordinates create no within-cell transition.
For
`L=Theta(sqrt(r))`, the uncovered owner fraction is at most

\[
 (2r+1)2^{-r}\left({er\over L+\lceil3\log_2r\rceil}\right)^{
 L+\lceil3\log_2r\rceil}
 =e^{-\Omega(r)}.                                    \tag{5.1}
\]

Thus the required residence scale holds on `1-e^{-Omega(r)}` of the middle
layer.  But small cells are structurally unavoidable: for even `r`, `m=0`
cells are isolated vertices; for odd `r`, `m=1` cells are `Q_1` paths, not
cycles.  Exact completion needs cross-cell edges.  The missing theorem is a
run-transparent cross-cell splice/absorption which also installs the q1 and
upper palettes.

Hamilton compression, one-track structure, and flip balance cannot replace
this theorem.  The maximally `5`-symmetric, one-track, balanced Hamilton
cycle

\[
 12,13,23,24,34,35,45,14,15,25
\]

in `J(5,2)` has a coordinate run of length one.

## 6. The shortest honest all-dimensional target

The current strongest implication remains `PPC(C)`, but the hypotheses can
now be made concrete.  A **Localized Correlated Pivot Host of charge `C`**
would consist of one odd selected spine and terminal even taps such that,
in one materialized state,

1. a chain-dependent two-SCD lower chunking satisfies every literal typed
   socket Hall cut and the residual nonadjacency/countdown rows;
2. a resident q1-exact owner host contains a protected all-width upper
   witness selector with nonempty dual join and a reserve forest/connector;
3. the aperture seam relation has one of the product-Johnson localization
   certificates of Section 4;
4. the residual occurrence bundles satisfy the degree-weighted factor
   cascade in the same cap state; and
5. the final literal replay has repair charge at most `C`, with one-star
   odd regeneration and terminal even taps.

The terminal-charge ledger, together with the private
pushout/running-intersection composition theorem, then gives

\[
                         \nu(k)\le B(k)+C.                            \tag{6.1}
\]

In particular `C=1` gives `B+1`; `C=0` gives equality using the lower bound.
This implication is proved.  Existence of the displayed host is not.

The most leverage now lies in two constructive lemmas, not in another
fractional relaxation:

* **chain-dependent cross-SCD Hall**, including the literal containment
  cuts; and
* **run-transparent decorated cross-cell splicing**, chosen jointly with
  the upper occurrence section and the private router factors.

Solving them separately is still insufficient unless their choices have a
running-intersection/private-footprint co-instantiation or an equivalent
global join theorem.

## 7. Bottom line

The pure-math push materially narrows the conjecture but does not finish it.
It removes the following as possible fundamental barriers:

* scalar endpoint capacity;
* all Boolean rank and generalized Greene--Kleitman cuts;
* fractional named flag feasibility;
* raw two-SCD socket count;
* token-sphere size and fixed coordinate avoidance; and
* max-flow integrality of a coexisting private two-factor router.

The remaining obstruction is exactly the one the finite `k=16` solution
foreshadowed: one globally correlated occurrence-labelled construction.
No known theorem currently supplies that correlation at coefficient one.
