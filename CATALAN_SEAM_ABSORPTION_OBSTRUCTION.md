# The exact obstruction to pointwise Catalan seam absorption

> **Correction (2026-08-06).**  Section 3's claim that a common inserted
> context has zero cyclic adjacent-swap cost is false: a shortest old swap
> word may cross the insertion cut, and after insertion that crossing pays
> the full block length.  The audited all-dimensional Tamari tensor is an
> explicit counterexample.  See
> `MATH_CORRECTION_TAMARI_TENSOR_REFUTES_ZERO_COST_COMMON_CONTEXT_20260806.md`.
> Section 3 and conclusions relying on its `e_t=0` assertion are retracted.
> The full-orbit pointing obstruction and fixed-hierarchy independence
> arguments are separate and are not retracted by this correction.

## 1. Outcome

The proved Catalan component hierarchy does **not** by itself give an
absorber for the integral Haar suspension.  Two independent obstructions
survive the correction above: a successful suspension cannot be pointwise
and cannot select components from one fixed MSW interaction cube.  The
formerly claimed obstruction to a literal common-context lift is false.

The surviving conclusions are unconditional.

1. A phase-oblivious antipodal extension of one old wreath must use every
   one of its `2m+1` pointings with equal multiplicity.  Two distinct such
   pointings already overlap in the new middle layer, so no nonempty
   phase-oblivious orderwise gadget is a partial factor.
2. **Retracted.** Inserting a common Dyck prefix/suffix context need not
   preserve cyclic adjacent-swap distance.  A swap path crossing the marked
   insertion cut pays the whole inserted block; the common Tamari tensor can
   create linearly growing distance by precisely this mechanism.
3. For the complete `(2 3)` MSW component hierarchy, the first-lower shadow
   effects of all components are linearly independent.  Hence no nonempty
   selection of components from that fixed cube preserves the first-lower
   shadow.  At the outer boundary the situation is even more rigid: the
   interaction quotient is connected, so the only boundary switch is the
   global transposition of the entire factor.

Consequently any proof built only from the fixed MSW interaction cube must
use a **noncommutative component-splitting theorem**: preparatory switches
must change the factor before later components are recomputed.  The
four-step `m=4` Haar circuit is of exactly this form.  The corrected Tamari
tensor shows, however, that common-tail suspension itself is not excluded;
its remaining issue is exact global factor completion.

## 2. Full-orbit cost of universal phase erasure

Put

\[
                         n=2m+1.
\]

For one old cyclic order `C`, let `E_a C` denote the antipodal extension in
which the first new coordinate is put at gap `a` and the second at gap
`a+m`.  If an old middle interval starts at `s`, its complete new top-row
incidence is determined by

\[
 \kappa(a-s)\in\{X_0,X_1,Y_1,Y_0,B\},
\]

where the fibres of `kappa` are

\[
 [0,m-2],\quad\{m-1\},\quad\{m\},\quad
 [m+1,2m-1],\quad\{2m\}.                            \tag{2.1}
\]

These are the exact five states from Theorem 6.1 of
`HAAR_ANTIPODAL_SUSPENSION.md`.

Let `D` be a multiset of pointing offsets.  Define the middle signature seen
at phase `s` by

\[
               K_D(s)=\{\!\{\kappa(a-s):a\in D\}\!\}. \tag{2.2}
\]

### Theorem 1 (universal phase erasure is the full orbit)

The multiset `K_D(s)` is independent of `s` if and only if

\[
                   D=c\,\mathbb Z_n                 \tag{2.3}
\]

for some nonnegative integer `c`.  In particular, every nonempty universal
phase-erasing gadget has at least `n` extensions of each old wreath.

### Proof

The number of occurrences of the state `B` in `K_D(s)` is

\[
       \#\{a\in D:a-s=2m\}=\operatorname{mult}_D(s-1). \tag{2.4}
\]

If `K_D(s)` is independent of `s`, then (2.4) is constant as `s` runs
through `Z_n`.  Thus every residue has the same multiplicity in `D`, which
is (2.3).  Conversely, the uniform multiset (2.3) is invariant under every
translation, so (2.2) is independent of `s`.  QED.

The singleton boundary state `B` is decisive: no Fourier analysis and no
assumption on the other four fibres is needed.

### Corollary 2 (orderwise phase erasure is incompatible with packing)

No nonempty universal phase-erasing family of antipodal extensions of one
old wreath is a new middle-wreath packing.

### Proof

For `a != b`, the two extensions `E_a C` and `E_b C` share a new middle
target.  One direct proof is to take an old middle interval `S_s`.  Relative
to its start, the `n` pointings split into `m` pointings exposing
`S_s union {x}`, `m` pointings exposing `S_s union {y}`, and one boundary
pointing.  Rotating `s` puts any prescribed pair `a,b` in one common class
(with the boundary point used in the antipodal case).  Hence both extensions
contain the same new middle target.

Theorem 1 requires at least two distinct pointings, so the resulting family
is not a partial factor.  QED.

The lower bound remains true if both antipodal orientations are allowed.
For each orientation the boundary state is attained at one affine translate
of the pointing.  Hence, if its total count is phase-independent, summing
that count over all `n` phases gives `|D|=nc`; a nonempty gadget has
`c>=1` and therefore still uses at least `n` extensions.  With two
orientations this argument need not make the two pointing multisets
separately uniform, so only the cardinality conclusion is asserted.

This proves that the translate sum in the linear suspension cannot be
desingularized one old order at a time.  Different old owners and genuinely
different Dyck sectors must be mixed.

## 3. Conditional distance bound and the retracted zero-cost specialization

For unoriented cyclic orders `C,D` of length `2m+1`, let
`d_circ(C,D)` be their cyclic adjacent-swap distance, allowing a final
rotation or reversal.  The elementary overlap bound is

\[
 |W_m(C)\cap W_m(D)|\ge 2m+1-2d_\circ(C,D).          \tag{3.1}
\]

In particular, two orders in one partial factor satisfy

\[
                         d_\circ(C,D)\ge m+1.         \tag{3.2}
\]

### Theorem 3 (conditional context-dispersion lower bound)

Let `C,D` be two distinct orders on one side of a support-feasible trade in
dimension `m_0`.  Suppose a proposed lift to dimension `m_0+t` produces
orders `Phi_t(C),Phi_t(D)` and

\[
 d_\circ(\Phi_t(C),\Phi_t(D))
       \le d_\circ(C,D)+e_t.                         \tag{3.3}
\]

If the lifted side is a partial middle-wreath factor, then necessarily

\[
 e_t\ge m_0+t+1-d_\circ(C,D).                        \tag{3.4}
\]

### Proof

Apply (3.2) in the new dimension and combine it with (3.3):

\[
 m_0+t+1
 \le d_\circ(\Phi_t(C),\Phi_t(D))
 \le d_\circ(C,D)+e_t.
\]

This is (3.4).  QED.

The old specialization asserted that a common inserted context has `e_t=0`.
That assertion and the resulting `m>=7` Haar no-go are retracted.  For fixed
linear cuts, the exact corrected identity is

\[
 d_{\rm inv}(C_LBC_R,D_LBD_R)
 =d_{\rm inv}(C,D)+|B|\,|A_C\mathbin\triangle A_D|,
\]

where `A_C,A_D` are the old labels lying before the two insertion cuts.
Thus a common block may itself provide the necessary linear dispersion.
See the correction note cited at the top of this file.

The conditional inequality still says that every support-feasible lift must
have the required new minimum distance.  It no longer attributes that gain
to order-dependent context; a common tail can supply it through cut
crossings.

## 4. Why the Catalan hierarchy is not a flow network

Let `F_m` be the MSW factor and compare it with `(2 3)F_m`.  Its interaction
components are

\[
 K_{j,R}=\{AR:A\in\mathcal A_j\},
 \qquad 0\le j\le m-2,\quad R\in\mathcal D_{m-j-2}, \tag{4.1}
\]

with sizes `Cat_j+Cat_(j+1)`.  Let `Delta_(j,R)` be the rank-`m-1`
effect of switching that component.

### Theorem 4 (fixed-hierarchy no-absorption theorem)

For arbitrary coefficients over any field,

\[
             \sum_{j,R}c_{j,R}\Delta_{j,R}=0
       \quad\Longrightarrow\quad c_{j,R}=0
       \text{ for every }(j,R).                     \tag{4.2}
\]

Consequently no nonempty selection of the fixed Catalan components preserves
the first-lower shadow.

### Proof

`MSW_COLEX_PIVOT.md` gives every column `Delta_(j,R)` a colex-smallest
nonzero target `P_(j,R)` of coefficient `+1`.  These pivots are pairwise
distinct, and every other target in a column is later than its pivot.  Order
the columns by their pivots and eliminate in increasing colex order.  This
is triangular with diagonal one, proving (4.2) over every field.  QED.

Thus the exact Catalan count of components is not a dimension count for
first-shadow-preserving routing.  In a fixed interaction cube every
component choice leaves its own uncancellable pivot.

There is a complementary boundary obstruction.  For the transposition of
the first two path coordinates, `MSW_BOUNDARY_CONNECTIVITY.md` proves that
the quotient on all Dyck roots is connected in every dimension.  Therefore
the factor interaction graph has one component: every root also has a
middle target fixed by the transposition, giving a vertical edge which
identifies its left and right copies, and the connected quotient then lifts
to the full bipartite interaction graph.  Hence the only nontrivial
boundary switch replaces the entire MSW factor by its global transposed
copy.  In particular, the connected capped-root theorem supplies no local
boundary absorbers: connectivity means fusion, not independent routing.

## 5. The exact theorem still needed

Combine Theorem 5.1 of `HAAR_HOLONOMY_CLASSIFICATION.md` with the results
above.  A legal suspension must do all of the following.

1. **Cycle hitting.**  It must change the middle owner of at least one target
   on every nonzero-gain cycle of the old owner-transfer graph.
2. **Order mixing.**  It cannot erase pointing phase independently on each
   old wreath; Theorem 1 forces the forbidden full translate orbit.
3. **Metric dispersion.**  Its same-sign cyclic orders must acquire the
   distance required by the packing bound.  A common tail may itself supply
   this through the corrected cut-crossing term.
4. **State dependence.**  It cannot select a kernel combination from one
   fixed Catalan hierarchy; Theorem 4 says there is none.
5. **Completion.**  After rerouting, the negative and positive partial
   packings must have a common residual middle-factor completion, and their
   rank-`m-1` phase buckets must balance.

The minimal honest successor statement is therefore the following.

> **Noncommutative Catalan component-splitting theorem.**  Starting from a
> marked top-two-shadow-invisible factor edge in dimension `m`, construct in
> dimension `m+1` a bounded-depth sequence of preparatory component switches
> under at least two transpositions.  Components are recomputed after every
> switch.  In the final state, the marked interaction component must (i) hit
> every lifted unbalanced owner cycle, (ii) be a partial-factor code of
> distance at least `m+2`, (iii) have zero rank-`m` effect, and (iv) carry an
> injective image of the old deeper effect.

This is stronger than a flow or matching statement on the original Catalan
tree: the required degrees of freedom are created by changing the factor
state itself.  It is exactly what happens in the certified `m=4` circuit,
where three preparatory switches create the final four-for-four Haar edge.

The surviving obstruction results above sharply delimit a proof based on
the fixed component hierarchy.  Such a recursion must be noncommutative and
state-level; a pointwise cap, a boundary switch, or a fixed-cube component
combination is mathematically incapable of doing the job.  Common-tail
suspension is no longer on this no-go list.
