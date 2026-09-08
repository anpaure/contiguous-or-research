# The canonical MSW product bank has a macroscopic local two-step defect

**Status (2026-08-21).**  This note gives an unconditional obstruction to
using the canonical Mütze--Standke--Wiechert (MSW) central wreath factor,
unchanged or after a sparse row perturbation, as a two-block physical lift
of the alternating Greene--Kleitman (GK) chains.  Even if every physical
phase had the desired GK orientation, the targets after the first two
alternating emissions omit a positive fraction of their split profile.

The obstruction is local to one central split profile.  That profile has
only `Theta(b^(-1/2))` of the full middle-layer mass on two `b`-blocks, so
the result is **not** by itself an `Omega(W_b)` global no-go.  It also does
not apply to a genuinely noncanonical shadow-surjective wreath factor.

## 1. Hole order versus contiguous-window order

Put

\[
                 b=2r+1,\qquad N=\binom br .                 \tag{1.1}
\]

For a Dyck word `x` of semilength `r`, let `pi(x)` be the MSW flip-position
permutation and put

\[
                 q(x)=(\pi(x),b).                            \tag{1.2}
\]

The word `q(x)` is the **hole word** of the corresponding minimum odd-graph
cycle.  If the cycle vertices are `A_i`, then

\[
        A_i=\{q_{i+1},q_{i+3},\ldots,q_{i+2r-1}\}.           \tag{1.3}
\]

Consequently a contiguous-window cyclic order for the wreath is the
step-two decimation

\[
                    \alpha_x(j)=q(x)_{2j},                    \tag{1.4}
\]

up to cyclic rotation and reversal.  The settled minimum-cycle--wreath
equivalence proves that the `r`-window decks of the `Cat_r` orders
`alpha_x` partition `binom([b],r)`.

This indexing distinction matters.  Starting at `r=3`, using `q(x)` itself
as a contiguous-window order is false: the resulting union has repeated
and missing middle windows.  The checker records the exact finite counts.

## 2. The product two-step support identity

For a central wreath factor `F`, let

\[
 \mathcal I_s(F)=
 \{I_i^s(\sigma):\sigma\in F,\ i\in\mathbb Z_b\}             \tag{2.1}
\]

denote the **set** of distinct length-`s` windows.  Multiplicity is erased
in (2.1).  Since complements of `(r+1)`-windows are `r`-windows in the
same cyclic order, every exact central factor satisfies

\[
          |\mathcal I_{r+1}(F)|=\binom b{r+1}=N.              \tag{2.2}
\]

Take disjoint copies `A,B` of `[b]`, an exact central factor `F_A` on `A`,
and an exact central factor `F_B` on `B`.  Pair all their wreath orders and
start from the split `(r,r+1)`.  During the first two persistent steps the
type word is either `AB` or `BA`.  In either case exactly one new `A`
coordinate and one new `B` coordinate have been emitted.  Thus the local
window sizes after two steps are `(r+1,r+2)`.

### Theorem 2.1 (exact Cartesian support after two alternating steps)

The distinct split-profile targets supplied by the complete product bank
after two alternating steps are exactly

\[
       \mathcal I_{r+1}(F_A)\times\mathcal I_{r+2}(F_B).      \tag{2.3}
\]

In particular their number is

\[
             N\,|\mathcal I_{r+2}(F_B)|.                     \tag{2.4}
\]

The identity is independent of whether the physical word begins `AB` or
`BA`, of the phase origins, and of the GK orientations assigned to the
sources.

#### Proof

Inside one product block, its `b^2` counter pairs run through
`Z_b^2`.  Advancing each stream once translates the two counters, so the
resulting occurrences are precisely the Cartesian product of the
`(r+1)`-window deck of the first order and the `(r+2)`-window deck of the
second.  Taking every pair of factor rows gives (2.3).  Equation (2.2)
gives (2.4).  The order of the two advances only changes the intermediate
target, not the two-step target.  \(\square\)

Define the first-shadow hole count

\[
 h_1(F)=\binom b{r-1}-|\mathcal I_{r-1}(F)|.                 \tag{2.5}
\]

Complementation identifies `(r+2)`-windows with `(r-1)`-windows, so

\[
 |\mathcal I_{r+2}(F)|=\binom b{r+2}-h_1(F).                \tag{2.6}
\]

It follows from Theorem 2.1 that the product bank misses exactly

\[
                         N h_1(F_B)                           \tag{2.7}
\]

members of the complete `(r+1,r+2)` split profile.  Selecting or retiring
some occurrences cannot enlarge this support.

## 3. Canonical MSW loss and sparse-switch stability

Let `F_r^can` be the canonical MSW factor.  The already audited marked-gap
theorem gives

\[
 h_1(F_r^{\rm can})\ge
 \left[(2r-3)\operatorname {Cat}_{r-2}
             -{2N\over r+2}\right]_+.                       \tag{3.1}
\]

Moreover, if an exact factor `F'` replaces exactly `s` canonical rows, it
gives the stability estimate

\[
 h_1(F')\ge
 \left[(2r-3)\operatorname {Cat}_{r-2}
       -(r-1)s-{2N\over r+2}\right]_+.                       \tag{3.2}
\]

These are Theorem 2.2 and Proposition 4.1 of
`MATH_ATTACK_A_PHASE_ONE_MULTIDEPTH_SHADOW_BARRIER_20260725.md`; their
insertion--erasure proof is not duplicated here.

### Corollary 3.1 (canonical product obstruction)

Even under a hypothetically perfect GK phase alignment, the canonical
product bank misses at least

\[
 \boxed{
 N\left[(2r-3)\operatorname {Cat}_{r-2}
             -{2N\over r+2}\right]_+
       =\left({1\over16}-o(1)\right)N^2}                    \tag{3.3}
\]

two-step targets in the `(r+1,r+2)` profile.  Since

\[
 \binom b{r+2}={r\over r+2}N,                               \tag{3.4}
\]

the missed fraction of that profile is at least `1/16-o(1)`.  No matching
upper bound on the canonical defect is asserted.

If `F_B` is obtained by replacing `s` canonical rows, then (2.7) and
(3.2) apply.  In particular, making the two-step product deficit `o(N^2)`
requires

\[
                  s\ge(1/8-o(1))\operatorname {Cat}_r.      \tag{3.5}
\]

Global coordinate conjugation, cyclic row rotation, and row reversal do
not change any window support and therefore do not reduce (3.3).  Any
successful canonical switch strategy must replace a positive density of
the rows.  The row-distance bound (3.5) alone does not rule out the known
`1100`/`1010` inverse-triple packet, because that packet changes a positive
density of the canonical rows.  Its **locality**, however, gives a stronger
obstruction.

### Theorem 3.2 (Catalan-many separated-double-swap trades are insufficient)

Suppose an adaptive sequence of `T` exact support-matched trades is made,
where each trade applies one separated double swap to each of two current
wreath rows.  If the final object is a spanning odd-graph two-factor, then

\[
 h_1(F_T)\ge
 \left[(2r-3)\operatorname {Cat}_{r-2}
       -18T-{2N\over r+2}\right]_+.                         \tag{3.6}
\]

Consequently every `T=O(Cat_r)` such bank, including the aligned
`1100`/`1010` packet, leaves

\[
                         h_1(F_T)\ge(1/16-o(1))N,            \tag{3.7}
\]

and hence still misses `(1/16-o(1))N^2` two-step product targets.  Repair by
this bounded local trade family needs `T=Omega(N)=Omega(r Cat_r)`.

#### Proof

In one cyclic order, a separated double swap changes exactly three central
window sets.  Index the old odd cycle by window starts.  Its factor edges
join starts differing by `r` modulo `b`.  Therefore the first-shadow slot at
start `i` is certainly unchanged unless one of

\[
                         i-r,\quad i,\quad i+r               \tag{3.8}
\]

is one of the three changed starts.  At most nine old slot centers are
touched in one row and at most eighteen in the two rows of a support-matched
trade.

Use the original canonical marked-gap certificates as a static cover
system.  Their occurrence slots are pairwise disjoint.  During an adaptive
sequence, one trade can newly touch at most eighteen original slot centers,
so at least `K_r-18T` original certificates have neither slot touched.  Both
incident factor edges at each untouched center remain their canonical
edges, hence those certificates remain equal pairs in the final
first-shadow histogram.  The exact duplicate ledger

\[
 \sum_S(\mu(S)-1)_+={2N\over r+2}+h_1(F_T)                  \tag{3.9}
\]

now gives (3.6), exactly as in the marked-gap stability proof.  Since
`Cat_r=N/b`, (3.7) follows.  Finally apply (2.7).  \(\square\)

The constant `18` is deliberately conservative.  It is enough to separate
the `O(Cat_r)` supply of known inverse-triple trades from the
`Theta(r Cat_r)` repair demand.  A related sharp `3/6`-slot statement for
incidence/direct odd-graph hexagons is proved independently in
`MATH_OBSTRUCTION_CATALAN_C6_MARKED_GAP_REPAIR_CAPACITY_20260821.md`.

## 4. Exact finite phase census

For orientation diagnostics, replace a `(r+1)`-window on `B` by its
complementary `r`-window.  For two corrected MSW orders `alpha,beta`, form
the GK parity matrix on their two `r`-window decks.  A physical phase is an
antidiagonal.  Independently reversing one stream changes antidiagonals to
diagonals, so there are only two distinct relative-direction choices.

For each factor-row pair, the checker maximizes first over those two
directions.  `mono` is the number of GK-monochromatic phases; `correct` is
the number which can also be matched to a cyclic shift and global color
choice of the one-defect-alternating persistent word.

\[
\begin{array}{c|r|r|r|r}
b&\operatorname {Cat}_r^2&\max\mathrm{mono}
 &\max\mathrm{correct}&\text{pairs with zero mono}\\ \hline
5&4&3&2&0\\
7&25&4&3&10\\
9&196&5&3&115\\
11&1764&5&4&1240\\
13&17424&6&4&13527
\end{array}                                                \tag{4.1}
\]

The complete histograms, not only the maxima, are frozen in the checker.
They show no finite sign of alignment, but (4.1) is **not** promoted to an
asymptotic theorem.  Corollary 3.1 is the rigorous obstruction.

## 5. Global scope

Write

\[
                         W_b=\binom{2b}{b}.                   \tag{5.1}
\]

The central product profile has

\[
              N\binom b{r+2}=\Theta(N^2)
                         =\Theta(W_b/\sqrt b).                \tag{5.2}
\]

Therefore (3.3) is `Theta(W_b/sqrt(b))=o(W_b)`.  It rules out a
near-perfect lift **relative to this local profile**, but it is not an
aggregate coefficient-one obstruction on the full two-block middle layer.
To obtain an `Omega(W_b)` global obstruction one would have to prove that
the same constant loss persists on `Theta(sqrt(b))` profiles carrying a
constant fraction of the squared-binomial mass.  The central MSW factor
alone gives no such multirank statement.

Conversely, the result does not rule out:

1. a positive-density exact trade transforming the canonical factor;
2. a different shadow-surjective central wreath factor;
3. non-product atoms which rebundle the duplicate local shadows; or
4. accepting the entire central-profile loss as an `o(W_b)` global seam.

Thus the exact verdict is negative for the unchanged canonical product
bank, open for a dense switch/conjugation family, and neutral at the full
`W_b` scale.

## 6. H100 checker

`scratch/audit_canonical_msw_product_two_step_gk_phase_gate_20260821.py`
reconstructs the MSW flip recursion, verifies the hole-word decimation and
the exact central factor through `r=7`, checks the Cartesian support identity
literally through `r=5`, verifies the canonical shadow counts and the
marked-gap lower bound, and reproduces every histogram behind (4.1) through
`b=13`.
