# Audit of directed clean-C6 halo telescoping and the sibling return

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_DIRECTED_CLEAN_C6_HALO_TELESCOPING_AND_SIBLING_RETURN_20260805.md`  
**Method:** independent symbolic row and permutation replay; no search  
**Verdict:** **PASS**, with the contour scope explicitly conditional on
physical monotone third-shore order.

## 1. Clean-C6 orientation replay

The old edges are `u_i -> v_i`; the new edges are
`u_i -> v_(i+1)`.  If the old row on `u_i -> v_i` is `R_i`, the new row
on `u_i -> v_(i+1)` is `R_(i+1)`.  At `v_i`, the replacement incoming
edge is therefore `u_(i-1) -> v_i`, and its row is `R_i`.  Hence the
incoming row at every head is pointwise unchanged.  This verifies the
orientation-sensitive identity on which the theorem depends.

At a shared head/tail `w`, write the incoming row `L` and the old/new
outgoing rows `R,R'`.  The final turn is `L intersection R'`: exactly the
isolated tail change of the second packet.  There is no cross term and no
condition relating the two packets' deleted pivots.  Summing isolated
q2-neutral identities is therefore valid.

## 2. PBBS velocity replay

For hook height `H`, the vacancy-circle length is `q_H=2H-1`, while

\[
 2(1-H)=1-q_H\equiv1\pmod {q_H}.
\]

For promoted height `H+1`, the length is `2H+1` and

\[
 2(1-(H+1))=1-(2H+1)\equiv1\pmod {2H+1}.
\]

Thus the sign is positive in both rows.  This proves consecutive factor
time on a fixed necklace; it does not identify different necklaces.

## 3. Return-permutation replay

For path-edge labels `1,...,E`, put

\[
 \alpha=(2\ 3)(4\ 5)\cdots,
 \qquad
 \beta=(1\ 2)(3\ 4)\cdots,
 \qquad
 \gamma=(1\ 2\ \cdots\ E).
\]

With rightmost action first, `pi=beta alpha` maps:

* `1 -> 2`;
* a nonterminal even label to the next even label;
* an odd label at least three to the preceding odd label;
* the terminal even label to `E` if `E` is odd, and `E` to `E-1` if
  `E` is even.

Left composition by `gamma` gives

\[
 (1,3,2,5,4,\ldots,E,E-1)
\]

when `E` is odd, and

\[
 (1,3,2,5,4,\ldots,E-1,E-2)(E)
\]

when `E` is even.  Directly, `E=1` gives one fixed label and `E=2` gives
two fixed labels.  The one/two count is correct.

## 4. Scope audit

The theorem proves unconditionally:

1. compound q1/q2 neutrality across the canonical sibling halo overlap;
2. the positive PBBS velocity sign; and
3. the algebraic return count under `gamma=(1 ... E)`.

It does **not** prove that the recursively spliced promoted components
present their marked ports in that physical order.  The triple-zero rail
is an angle-graph path, generally between distinct factor components.
Accordingly, the one-or-two-contour conclusion is conditional, exactly as
stated in the theorem.
