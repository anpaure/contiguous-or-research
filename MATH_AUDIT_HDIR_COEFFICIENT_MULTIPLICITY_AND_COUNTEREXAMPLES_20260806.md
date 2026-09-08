# Internal audit of the corrected HDIR reduction

**Date:** 2026-08-06  
**Audited source:**
`MATH_THEOREM_HDIR_FROM_GDIR_SMALL_CAP_AND_FE3_20260806.md`  
**Method:** coefficient replay plus adversarial finite examples; no search  
**Verdict:** **PASS AS A CONDITIONAL REDUCTION FOR THE ROOT-OMITTED BASE
PAIR FAMILY.**  Every factor depending on `d` is explicit.  The theorem
does not cover marked/rooted occurrence conventions, and it assumes the
already authenticated dynamic `FP9 -> FE3` coefficient identity.

## 1. The deterministic product remainder is necessary

Take `V={x,y}`, let the active edge measure be zero on both resources, and
let both ideal hazards equal `u>0`.  Then

\[
 Y_x=Y_y=\Lambda(V)=\mathcal B(V)=0,
 \qquad q(V)=2u-u^2.
\]

Thus

\[
 X\mathcal H(V)-\sum_{z\in V}(Xu-Y_z)=-Xu^2\ne0.
\]

Any absolute estimate using only `B(V)` is false.  The corrected theorem
adds `D^{prod}=Xu^2`, making (2.5) exact.

## 2. Distinguished roots must be removed

Take a row with distinguished root set `Q={q_1,q_2}` and empty
root-omitted face.  Then `g_x^circ=0` for every resource, whereas including
`Q` in the first-order sum can give

\[
 (a_{q_1}+a_{q_2})^2>0.
\]

Hence no estimate of that square by the root-omitted `g^circ` is possible.
The corrected face `(E\cup F)-Q` is necessary, and the two omitted roots
must stay in the two-root service ledger.

## 3. Occurrence coalescing is necessary and sufficient

Suppose the same physical resource `x` appears in both `E` and `F`, and a
deleting edge `G` contains `x,y`.  On the occurrence multiset
`{x_E,x_F,y}`, an occurrence-pair count can count three pairs, including
the meaningless pair `{x_E,x_F}`.  The hit event has only the two physical
vertices `{x,y}` and contributes

\[
 {|G\cap\{x,y\}|\choose2}=1.
\]

After coalescing to physical resource vertices, Tonelli gives exactly

\[
 \sum_{\{x,y\}\subseteq V}Y_{x,y}
 =\sum_G a_G{|G\cap V|\choose2}.
\]

Thus there is no hidden occurrence factor.  The only remaining
multiplicities are orientation of `(E,F)` (at most two) and choice of
left/right/union face (at most three).

## 4. The pair square spends exactly one factor `d`

For the non-slot face there are `O(d^2)` resource pairs and each has load
`O(1/d)`, so `B_ns<=Cd`.  With constantly many slots, there are `O(d)`
slot--non-slot pairs of bounded load and `O(1)` slot--slot pairs, so
`B_slot<=Cd`.  Hence

\[
 B^2\le Cd B.
\]

The dynamic first-two-hit identity supplies `sum cR B/X<=C A/d`; the
product is exactly `C A`.  No other `d`-dependent multiplicity occurs.

This assumption is sharp at the scale used.  If one allowed `Theta(d^2)`
non-slot pairs each of constant load, then `B=Theta(d^2)` and
`B^2=Theta(d^4)`; the `1/d` FE3 spare would not close the square.  Likewise,
`Theta(d)` slot vertices would invalidate the slot estimate.  These are
correctly excluded by the good-relation stop and fixed-template slot
count.

## 5. The beta-zero convention is sound

The incidence coefficients satisfy `g_x^circ>=0`.  Therefore

\[
 \beta_T={\sum_xg_x^\circ\over\sum_xY_x}=0
\]

implies every `g_x^circ=0`; both the first-order row and `Gfrak_T` vanish.
No division-by-zero limit is being assumed.

## 6. Normalization replay

Let `D(V)=X H(V)`.  Since `h=1-\rho^2\asymp X^{-1}`,

\[
 {H(V)^2\over h}={D(V)^2\over hX^2}\asymp {D(V)^2\over X}.
\]

This is exactly the coefficient used in the first-order and Bonferroni
square estimates.  There is neither an extra `X` nor a missing `X^{-1}`.

For the deterministic product remainder, `Dprod<=Cd^2/X`,
`sum_A mu_A<=CX/d^2`, at most `CM` transitions occur, and
`X>=cM/d`.  Therefore its entire contribution is at most

\[
 CM\,{1\over X}{X\over d^2}{d^4\over X^2}
 \le {Cd^4\over M},
\]

exponentially smaller than the static scale.

## 7. Exact scope boundary

The proof establishes only

\[
 HDIR_{base}^{circ}
 \lesssim theta\,GDIR
   +(\varepsilon_P/\theta)ROOT+A.
\]

It does not prove `GDIR`, does not infer exceptional owner/slot classes
from the ordinary pair-ratio bound, and does not silently identify
marked/rooted occurrence conventions with the base family.  Those are
explicit theorem inputs or finite replay obligations.  Subject to that
scope, no counterexample above survives the corrected statement.
