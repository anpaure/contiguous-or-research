# Audit: suffix-kernel endpoint selector and two-mark cylinder

**Date:** 2026-08-05  
**Method:** independent symbolic ledger and scope audit; no computation  
**Audited theorem:**
`MATH_THEOREM_SUFFIX_KERNEL_ENDPOINT_SELECTOR_AND_TWO_MARK_CYLINDER_20260805.md`

## 1. Rank ledger

For a suffix of `d-1` owners `T_2,...,T_d`, there are `d-2` fresh deletions
`x_3,...,x_d`.  Hence

\[
 |P|=|T_2|-(d-2)=r-d+2.
\]

After fixing `b_2`, the endpoint-changing mark aperture has size
`r-d+1`.  Removing both marks leaves `r-d` persistent coordinates, exactly
the sum

\[
                         (r-2d)+d
\]

needed for `C` and `A`.  Thus no hidden coordinate is missing.

The outside set for the first two queue labels has size

\[
 k-|T_2|-(d-2)=k-r-d+2=q-d+1,
\]

which agrees exactly with the `K_y` theorem.

## 2. Owner identity audit

Writing `z=b_1`, the reconstructed suffix is

\[
 T_j=P\cup\{x_{j+1},\ldots,x_d\}
          \cup\{b_3,\ldots,b_j\},\qquad2\le j\le d.
\]

The right side is independent of `z`, of the partition
`\(P-\{z,b_2\}=C\mathbin{\dot\cup}A\)`,
and of the order of `A`.  At `j=2` the two variable sets are respectively
`{x_3,...,x_d}` and empty; at `j=d` they are empty and
`{b_3,...,b_d}`.  This verifies both endpoints and every transition.

Changing `z` does change the full endpoint fibre and generally the lower
path.  The theorem therefore does not invoke the forbidden fixed-fibre
switch.

## 3. Cylinder arithmetic audit

If the one-mark intensity is at most

\[
                         (1+\epsilon_1)H/(Wr),
\]

then occurrence-local independent marking gives two-mark intensity at most

\[
 {1+\epsilon_1\over r-d+1}{H\over Wr}
 = (1+\epsilon_1){r-1\over r-d+1}{H\over W(r)_2}.
\]

Because `d=o(r)`,

\[
                         {r-1\over r-d+1}=1+O(d/r)=1+o(1).
\]

The calculation applies after conditioning on the full suffix history, so
overlapping persistent kernels create no diagonal coupling.  Marks are
keyed by occurrences, not coordinate values.

For any later alteration, `X_alpha<=widetilde X_alpha` pointwise.  Products
of zero-one variables retain this inequality, proving that arbitrary
deletion cannot worsen any cylinder order.

## 4. Scope exclusions

The theorem does **not** prove any of the following.

1. That a previously fixed lower fresh path can change its `b_1` mark.
2. That the existing lower-first macro factor admits the required quantifier
   reversal.
3. That all independently marked suffixes extend simultaneously without
   deleting occurrences.
4. That the required lower named-target cover survives endpoint-fibre
   changes.
5. That a bank-conditioned one-mark cylinder exists beyond the scope of the
   theorem already used as input in the pre-reserved construction.

The exact remaining input is the suffix-first endpoint-extension statement:
realize the marked suffixes in a lower fresh-chain factor after deleting at
most `O(H/d)` occurrences.  Conditional on that statement, `(C2)` and the
bottom Haxell completion are rigorous.

## 5. Verdict

**PASS, with the suffix-first quantifier explicit.**  The stochastic
two-mark kernel and its cylinder calculation are unconditional once the
fresh suffix and one-mark state are fixed.  The theorem is a genuine
positive endpoint-changing result, but not yet an unconditional bottom
completion because the lower-chain extension remains open.
