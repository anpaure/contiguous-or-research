# The common geodesic tail is not a bounded-distance cyclic context

## Status

This note reconciles two statements which otherwise look contradictory.

* `MATH_ATTACK_AC2_GRAVER_SUSPENSION_20260724.md`, Theorem 9.2, proves
  that a recursively packed pair of same-sign wreath rows must acquire
  linearly growing cyclic adjacent-swap distance.  In particular a
  distance-preserving common cyclic context cannot persist.
* `MATH_THEOREM_TENSORED_FOUR_ROW_TAMARI_WREATH_TRANSPORT_20260806.md`
  tensors the four-row packet by appending the same complement-geodesic
  tail to every row in path time.

There is no contradiction.  A common tail in **exchange-path time** is
not a common contiguous context in the cyclic-window coordinate order.
It splits into two banks, at row-dependent deletion/insertion cuts, and
automatically creates the dispersion required by Theorem 9.2.

No computation is used.

## 1. The two orderings

Let a base complement geodesic in one row `R` have deletion and insertion
orders

\[
 D_R=(d^R_1,\ldots,d^R_b),\qquad
 E_R=(e^R_1,\ldots,e^R_b).                            \tag{1.1}
\]

Its shortest-wreath cyclic-window order is

\[
                   C_R=(D_R,E_R,\infty).              \tag{1.2}
\]

Now append a common complement-geodesic tail on fresh coordinates, with
deletion and insertion banks

\[
 D_F=(\delta_1,\ldots,\delta_t),\qquad
 E_F=(\epsilon_1,\ldots,\epsilon_t).                  \tag{1.3}
\]

Path time performs all base exchanges and then all fresh exchanges.  The
deletion and insertion orders of the extended geodesic are consequently
`(D_R,D_F)` and `(E_R,E_F)`.  Therefore the extended cyclic-window order is

\[
             \widehat C_R=(D_R,D_F,E_R,E_F,\infty).   \tag{1.4}
\]

Equation (1.4) is the order used in the residence proof of the tensor
theorem.  The common exchange tail appears as **two separated blocks** in
cyclic-window order.  These blocks straddle the row-dependent old
insertion bank `E_R`.  Thus (1.4) is not obtained by adjoining one fixed
contiguous prefix or suffix to (1.2) at a row-independent cyclic cut.

This distinction is especially important when two rows have different
start endpoints.  An old coordinate may lie in `D_R` for one row and in
`E_S` for another.  The fresh banks then lie on different sides of that
coordinate in the two lifted orders, so a common exchange tail can create
linearly many adjacent-swap crossings.

Deleting the fresh coordinates from (1.4) recovers (1.2), but deletion is
only a projection; it does not imply equality of the two cyclic distances.

## 2. Dispersion is automatic from disjointness

Let two extended rows `R,S` belong to the same sign of one packet phase.
The tensor theorem proves that their shortest-wreath supports remain
simple and disjoint.  The interval-overlap inequality of Theorem 9.2
therefore applies at the new semilength `b+t` and gives

\[
       d_\circ(\widehat C_R,\widehat C_S)\ge b+t+1.   \tag{2.1}
\]

If

\[
                         d_0=d_\circ(C_R,C_S),        \tag{2.2}
\]

then the tensor has produced distance growth at least

\[
       d_\circ(\widehat C_R,\widehat C_S)-d_0
                        \ge b+t+1-d_0.                \tag{2.3}
\]

Thus the tensor does not evade the linear-dispersion theorem.  Its proved
disjointness forces it to realize exactly the kind of growing dispersion
that theorem demands.  No separate calculation of an optimal adjacent-
swap path is needed for this consistency conclusion.

## 3. Correct scope of the common-context no-go

Theorem 9.2 rules out a lift family satisfying a bounded-growth estimate

\[
 d_\circ(\Phi_t(C),\Phi_t(D))
       \le d_\circ(C,D)+e_t                            \tag{3.1}
\]

with `e_t=o(t)`; in particular it rules out a genuinely distance-
preserving (`e_t=0`) common cyclic context.  It does not say that every
construction informally described as "append the same tail" has `e_t=0`.

The tensor theorem uses common **path data**, while Theorem 9.2 measures
commonality in the induced **cyclic-window order**.  Formula (1.4) is the
conversion between them and is the precise reason both theorems can hold.

Accordingly, the sentence "a literal common context fails" should always
be read as "a bounded-distance common cyclic-window context fails."  It
must not be applied to the two-bank exchange-word tensor without first
proving a bounded value of `e_t`; (2.1)--(2.3) show that such a bound is
false for the packed tensor rows.

## 4. Consequence for phase-switched companion work

The all-dimensional Tamari tensor is therefore a valid local candidate
for a phase transport and is not refuted by the 2026-07-24 dispersion
theorem.  This consistency result supplies no companion connectivity:
the audited base tensor still preserves only the companion edge `A--L`.
Nor does it prove all-width/provider-safe serial closure.  Those remain the
exact premises in
`MATH_THEOREM_PHASE_SWITCHED_COMPANION_MATCHINGS_SUFFICE_20260806.md`.
