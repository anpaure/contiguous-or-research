# Independent audit of the adjacent-depth zero-defect residual-collar synthesis

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, code, search, or solver  
**Audited file:**
`MATH_SYNTHESIS_FRACTIONAL_CONFIGURATION_TO_ZERO_DEFECT_ADJACENT_COLLAR_20260805.md`  
**Verdict after correction:** **PASS, with residual/even-dimensional scope.**

## 1. Corrections required by the audit

The pre-audit draft contained five material overstatements.

1. It called the result a theorem for the complete nonempty lower ideal.
   The MLD/configuration argument directly covers the canonical residual
   histogram.  A triangular or other separately priced boundary bank remains
   separate until the protected serialization theorem includes it.
2. It moved from depth `D` to `D+1` without applying terminal deletion.
   The old rank-`t-1` singleton jobs disappear, and all other jobs lose their
   last cell.  The new MLD cutoff is `b-1=t-2`, not `t-1`.
3. It asserted named attachment for every tail-feasible reserve vector, but
   the pointwise Hall union bound additionally needs the spread inequalities
   involving `d_g`.
4. It did not define `d_g` in the synthesis theorem.
5. It stated an all-`k` `B+1` corollary although the argument was carried out
   only in `B_(2r)`.

All five points are corrected in the audited file.

## 2. Parameter and index audit

Put

\[
 C_s={2r\choose s},\quad H_s=C_s-C_{s-1},\quad W=C_r,
 \quad t=r-D,\quad b=t-1.
\]

At old depth `D`, exact capacity `g` has multiplicity `H_(t+g)`.  Hence

\[
 K_q=\sum_{g=q}^D H_{t+g}
     =C_r-C_{t+q-1}=W-C_{t+q-1}.
\]

At new depth `D+1`, exact capacity `g` has multiplicity `H_(b+g)`, so

\[
 K_q^+=\sum_{g=q}^{D+1}H_{b+g}
      =C_r-C_{b+q-1}=W-C_{b+q-1}.
\]

Since `b=t-1`, for `q<=D`,

\[
 K_q^+-K_q=C_{t+q-1}-C_{t+q-2}=H_{t+q-1},
\]

and

\[
 K_{D+1}^+=W-C_{r-1}=H_r.
\]

Thus every tail index in the corrected theorem is exact.  In particular,
the first adjacent margin is `H_t`, not `H_(t-1)`, and the last old-tail
margin is `H_(r-1)`.

## 3. Residual cutoff and exceptional-bank audit

The old residual ranks are `1,...,t-1`.  A job born at rank `a` has length
`t-a`.  After deleting the terminal cell, its descendant has length
`t-a-1`; the old `a=t-1` jobs disappear.  Therefore the new residual ranks
are exactly

\[
                         1,\ldots,t-2=b-1,
\]

and `L_max<=t-2` (with the harmless convention `L_max=0` when no job
survives).

With at most `D` exceptional old jobs, consecutive fragmentation of their
surviving descendants into pieces of length at most `D` uses at most

\[
 h=D\left\lceil {L_{\max}\over D}\right\rceil.
\]

Moreover,

\[
 h<L_{\max}+D\le t-2+D=r-2<r.
\]

The corrected `h` is therefore valid and slightly sharper than the earlier
safe but untransported bound `D ceil(t/D)`.

Deleting `h` maximum-capacity occurrences subtracts `h` from every new
tail.  Deleting another `Delta_g` occurrences of exact capacity `g`
subtracts `sum_(g>=q) Delta_g` from tail `q`.  Hence the inequalities

\[
 h+\sum_{g=q}^{D+1}\Delta_g\le H_{t+q-1}
\]

are exactly the finite conditions needed to preserve every transported old
tail.  The separate last-row inequality is exactly

\[
 h+\Delta_{D+1}\le H_r.
\]

No scalar capacity is counted twice.

## 4. Extreme-point and MLD quantifier audit

The valid order of choices is:

1. choose an extreme point of the deterministic old configuration LP;
2. identify configuration counts and at most `D` exceptional abstract jobs;
3. apply terminal deletion and perform the sorted capacity-type assignment;
4. uniformly refine each deterministic new-depth birth cohort by the
   resulting complete configuration/exception/capacity-mark vectors;
5. only then expose the independent augmented Boolean matchings;
6. after the named fragment tops are known, choose the collar matching.

This is exactly the order used in the corrected proof.  The mark fixed before
the random path cover is a capacity type, not a named Boolean bottom chosen
from realized geometry.  Uniform fixed-count refinement therefore falls
inside the cohort-stable MLD theorem.  The final named bottom is selected
afterward by an integral matching, which is permitted.

The path process must be run only to cutoff `b-1`.  The corrected text says
so explicitly.  Consequently every ordinary and exceptional top has rank at
most `b-1`; the minimum containment degree for a capacity-`g` start is

\[
 d_g={2r-(b-1)\choose (b+g)-(b-1)}
     ={2r-b+1\choose g+1},
\]

which verifies the corrected spread parameter.

## 5. Reserve asymptotics

For `D=O(sqrt(r))`, all ranks `u_g=b+g` lie within `O(sqrt(r))` of the
middle.  Uniformly there,

\[
 C_{u_g}=\Theta(W),\qquad H_{u_g}\ge cW/r.
\]

Taking

\[
 \Delta_g=\left\lceil
 A\sqrt{rC_{u_g}H_{u_g}/d_g}\right\rceil
\]

gives the required pointwise exponent.  Also

\[
 {d_{g+1}\over d_g}={r+D+1-g\over g+2},
\]

so reserve tails are geometrically dominated on the square-root collar.  In
the coefficient-one regime `D=Theta(sqrt(r))`, at the weakest first row,

\[
 \Delta_1=O(Wr^{-3/4}),\qquad H_t=\Theta(Wr^{-1/2}),
\]

and at every later row the reserve tail is `o(H_(t+q-1))`.  The exceptional
charge `h<r` is polynomial.  Thus the tail-reserve conditions hold for all
sufficiently large `r`.  The same comparison only needs `D->infinity` and
`D=O(sqrt(r))`; the weaker assumption `D=O(sqrt(r))` alone would not suffice
(for bounded `D`, the first reserve can be of the same order as `H_t`).  The
corrected corollary now states the necessary coefficient-one hypothesis.

## 6. Exact word-length scope

For even `k=2r`, if `D=d(2r)`, then by definition

\[
 B(2r)=W+D,
 \qquad W+D+1=B(2r)+1.
\]

This identity is arithmetically exact.  What is conditional is its physical
interpretation: the lower forest must still be serialized as actual suffix
cells of the same resident, upper-complete owner chronology.  The corrected
corollary therefore assumes protected serialization and any separately
priced boundary bank.  It is now scope-safe and makes no odd-dimensional
claim.  At new depth `h=D+1`, each owner window contains `h+1=D+2` source
letters; on a flat owner chronology the corresponding run-residence floor is
therefore `D+2`, not `D+1`.  The corrected serialization interface uses the
depth parameter rather than conflating these two quantities.

## 7. Can the absorber be internalized at depth `D`?

Not by the adjacent-bank argument.  If an ordinary integral selection
saturates a tail `A_q=K_q`, then reserving any old socket of capacity at least
`q` violates the sorted-tail inequality immediately.  A same-depth proof
must instead establish the joint integer augmentation

\[
 \sum_a(p_a-p_a^0)+\sum_{f\in F}q_f\le
 K-\sum_a p_a^0.
\]

This is a normality/exchange theorem for the actual Boolean configuration
semigroup.  Neither fractional feasibility nor MLD implies it.

The complete-even-pair-slice parity theorem is a genuine no-go for a
different shortcut: no universal serializer can repair every exact
fractional slice with only bounded external **support**.  It is not a no-go
for `C=0`.  A full carrier can use linearly many internal cross-slice
transitions without adding word positions, and the theorem does not show
that the actual triangular carrier contains an isolated even slice.

The proof-safe conclusion is therefore:

\[
 \boxed{
 \begin{array}{c}
 \text{the adjacent absorber cannot simply be reserved at depth }D;\\
 \text{same-depth }C=0\text{ needs joint semigroup augmentation and}\\
 \text{parity-aware protected serialization;}\\
 \text{no current parity or integrality result disproves }C=0.
 \end{array}}
\]

## 8. Final verdict

After the corrections above, the synthesis is a valid finite implication
for the canonical residual lower system and a valid asymptotic conditional
reduction to `B(2r)+1`.  It must not be cited as an unconditional `B+1`, as
an odd-dimensional theorem, as a proof of a separately removed boundary
bank, or as a proof of protected serialization.
