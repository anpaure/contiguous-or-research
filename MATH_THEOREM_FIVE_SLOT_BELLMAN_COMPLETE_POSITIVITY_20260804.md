# Complete positivity of Bellman clocks through grid size five

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem assembled from the
independently audited branch theorems listed below.  It proves every finite
Bellman table with at most five active slots strictly positive.  It does not
prove the all-grid Bellman inequality or `nu(k)<=B(k)+O(1)`.

Put

\[
 A={\sqrt\pi\over2},
\]

and let `K` be the Rayleigh signed-tail kernel.  Let

\[
 0=c_0\le c_1\le\cdots\le c_n,
 \qquad c_{i+j}\ge c_i+c_j\quad(i+j\le n),
 \qquad c_n\ge A,
\tag{0.1}
\]

where `n<=5`, and define the exact carry-aware Bellman clock

\[
 V_0=0,
 \qquad
 V_m=\max_{1\le j\le\min(m,n)}(c_j+V_{m-j}).
\tag{0.2}
\]

## Theorem

Every table (0.1) satisfies

\[
                         \boxed{\sum_{m\ge0}K(V_m)>0.}
\tag{0.3}
\]

Consequently, if a finite internally superadditive Bellman table has
nonpositive functional, then its grid size is at least six.

## Proof

The complete four-slot theorem covers `n<=4`.  Take `n=5`.

Argue contrapositively and suppose the functional is nonpositive.  First
apply the proof-safe first-crossing deletion and then the monotone endpoint
saturation from the complete five-slot structural reduction.  A shorter
first-crossing prefix belongs to the already-positive `n<=4` theorem, so
the surviving table first crosses the threshold at slot five and lies on
its appropriate active or inert saturated endpoint face.  These
normalizations are performed **before** the efficiency branch is chosen;
this order is essential because endpoint saturation can change which
denomination maximizes density.

Assign the table to its least maximum-density denomination among sizes
`2,3,4,5`.  This is exhaustive: if size one is maximally efficient, then
`c_2>=2c_1` forces size two to be maximally efficient as well.  The exact
five-slot maximum-efficiency normal forms now give four branches.

1. **Size two.**  The complete small-period wedge theorem proves the
   two-efficient branch positive, retaining both finite pulses.

2. **Size five.**  If size five is the least maximizer among `2,3,4,5`,
   then it is the global least maximizer by the preceding size-one
   observation.  Least-critical endpoint normalization therefore forces
   `c_5=A`.  The endpoint-period train theorem proves this branch positive
   with margin `1/400`.

3. **Size four.**  Monotone endpoint normalization gives the active face
   `T=A` and the two inert composites `T=P+x`, `T=y+z`.  The active face is
   positive with margin `199/2310000`.  On the inert faces, the exact
   complementary-pair reduction removes the shifted trains, the compact
   kernel loss obeys the audited slope/range bound, and concavity of
   `C(A+delta)` reduces the remaining gate to rational endpoint checks.
   Hence both inert faces and the complete size-four branch are positive.

4. **Size three.**  Every active endpoint `c_5=A` is positive with margin
   `69/10000`.  On the inert endpoint, the exact five-pulse normal form
   collapses to two repeated-gap orientations.  The short-singleton gate

   \[
    \mathcal R(a,\beta)
    =\mathcal L_3(a+2\beta;a,a+\beta)
   \]

   is strictly increasing in its repeated gap: retaining the complete
   `q=1,2` derivative blocks reduces both parameter strips to one convex
   worst corner, which is positive by exact rational Gaussian
   certificates.  Its two lower boundaries are positive.

   The remaining retained-pulse face is strictly concave in its endpoint
   increment.  Its threshold endpoint is already positive, and its other
   endpoint is the long-singleton lattice

   \[
    \mathcal P(p,a)=\mathcal L_3(p;a,2a).
   \]

   For this lattice, the complete `q=1,2` period-derivative block is a
   jointly convex function `B(r,s)`.  An exact rational tangent at
   `(r,s)=(12/35,1/7)` gives

   \[
                         B(r,s)>{79\over1750}>0
   \]

   on a rectangle containing the full physical domain.  Thus
   \(\partial\mathcal P/\partial p>0\); the already-positive density and
   threshold lower-period boundaries transport positivity through the
   entire long-singleton interval.  Strict endpoint concavity then closes
   the retained-pulse face as well.

These branches exhaust the least-maximizer partition, so every five-slot
table is strictly positive.  Together with the complete `n<=4` theorem,
this proves (0.3). \(\square\)

## Frozen proof dependencies

| role | file | SHA-256 |
|---|---|---|
| `n<=4` closure | `MATH_THEOREM_FOUR_SLOT_BELLMAN_COMPLETE_POSITIVITY_20260804.md` | `1624cff37c4f6b45edd16234e054d43c99ceb722d7dac4b57d058a40465b68b9` |
| five-slot normal forms | `MATH_THEOREM_FIVE_SLOT_MAXIMUM_EFFICIENCY_APERY_NORMAL_FORMS_20260804.md` | `2ba2be5a52e4761790f031fcc63955c8066fd032fc3afaa81de866b50abd9b9e` |
| size-two closure | `MATH_THEOREM_FIVE_SLOT_TWO_EFFICIENT_SMALL_PERIOD_WEDGE_CLOSURE_20260804.md` | `a678fc5a33c6457d9d640aa963d902fdb8c7ed932ade6a14fd320caf8d285e43` |
| least-endpoint normalization | `MATH_THEOREM_LEAST_CRITICAL_ENDPOINT_THRESHOLD_NORMALIZATION_20260804.md` | `7d897ac0600f9331f821fb1ca3a5d47483c67caf412b009d172fe8b365580f7f` |
| size-five closure | `MATH_THEOREM_FIVE_SLOT_ENDPOINT_EFFICIENT_THRESHOLD_CLOSURE_20260804.md` | `db22119a59eae766e51c9461111f207342280309a3144fe43d0caf214c704027` |
| size-four boundary split | `MATH_THEOREM_FIVE_SLOT_FOUR_EFFICIENT_THREE_FACE_BOUNDARY_REDUCTION_20260804.md` | `332debcb96ff54fa47d9c85e153d9a36c01460ccbf9552ee20a2e73baee90c5b` |
| size-four active face | `MATH_THEOREM_FIVE_SLOT_FOUR_EFFICIENT_THRESHOLD_FACE_CLOSURE_20260804.md` | `9cee07d666ae51411550cfad13b8cb8f0ac8006e8968c5983583353dacb10722` |
| size-four inert faces | `MATH_THEOREM_H4_INERT_COMPACT_GAUSSIAN_GATE_CLOSURE_20260804.md` | `f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b` |
| size-three endpoint split | `MATH_THEOREM_FIVE_SLOT_THREE_EFFICIENT_THRESHOLD_ENDPOINT_AND_DELAYED_CROSSING_REDUCTION_20260804.md` | `1e15d736592bce3103786fb965f62fe6f028436c0d35b763b195157a2cf3d0b6` |
| delayed endpoint concavity | `MATH_THEOREM_FIVE_SLOT_THREE_EFFICIENT_DELAYED_B_CONCAVITY_AND_PURE_LATTICE_GATE_20260804.md` | `b494371c790ed20f14e29bd4beba67b27aa30f7f5b1447e4ef8da4e74db8ea14` |
| short-singleton closure | `MATH_THEOREM_FIVE_SLOT_SHORT_SINGLETON_REPEATED_GAP_COMPLETE_CLOSURE_20260804.md` | `8f7e7caecfbf873d7992e34349e3d3c3cc7968ae8e8691615d193d4afa8ef992` |
| long-singleton closure | `MATH_THEOREM_FIVE_SLOT_LONG_SINGLETON_COMPLETE_Q12_TANGENT_CLOSURE_20260804.md` | `19f8a5a23cca1963e1914da28f609a56c9247f89422ee407e8e3aaa696654927` |

The branch theorems have independent audits.  In particular, the current
short-singleton bytes are bound by audit SHA
`c0427eb680265563ffb85448a0a538d89a63c6421d668a847d9d09f05e6e3760`,
and the long-singleton tangent theorem is bound by audit SHA
`d2c148f0f7c32ffcfb95a412f831877db8b2b4c29aa3472598a13fecab58f538`.

## Scope

This is a complete finite-grid theorem through five, not the universal
clock theorem.  It moves the first possible mixed-denomination separator
to grid size six.  It does not by itself supply an integral smooth
configuration, a resident carrier, a common-cap router, or a proof of
`nu(k)<=B(k)+O(1)`.
