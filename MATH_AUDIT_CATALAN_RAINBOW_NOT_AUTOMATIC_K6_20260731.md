# Cap-two plus the lower integrality floor does not force a rainbow switch

Date: 2026-07-31  
Status: exact finite counterexample to an *automatic implication*; it does
not contradict the conditional switch theorem

## 1. Scope

The local switch theorem in
`MATH_THEOREM_CATALAN_TWO_RAIL_RAINBOW_SWITCH_REDUCTION_20260731.md`
is correct under its explicit rainbow hypothesis (2.2).  What is not true
is the tempting strengthening

\[
 \text{cap-two Catalan compression + lower profile }1^{N-K}2^K
 \quad\Longrightarrow\quad
 \text{a rainbow switch choice exists}.
\]

The implication already fails for (m=3), on the six-element ground set.

## 2. Exact instance

Use bit masks on ([6]).  A saturating cycle through all fifteen rank-four
sets is

\[
 (15,43,45,46,39,51,23,54,58,27,57,60,53,29,30).
\]

Its cyclic rank-three seam facets (C_i=U_{i-1}\cap U_i) are

\[
 (14,11,41,44,38,35,19,22,50,26,25,56,52,21,28).
\]

The omitted facets are hosted injectively as follows:

\[
 7\mapsto U_0,qquad
 37\mapsto U_4,qquad
 49\mapsto U_5,qquad
 42\mapsto U_8,qquad
 13\mapsto U_{13}.
\]

Splitting those five blocks gives a Hamilton cycle on all twenty
rank-three sets.  Its fifteen rank-two lower colours have exact floor
profile

\[
                         1^{10}2^5,
\]

and the duplicated colours are

\[
                         \mathcal D=\{12,18,24,33,36\}.
\]

Nevertheless the inserted facet (X=7) has incident lower colours
(6,3), and (X=42) has incident lower colours (34,10).  Neither pair
meets (mathcal D).  Hence no choice of one incident edge at every
inserted facet can run through (mathcal D), even before imposing the
distinct-seam condition.

The companion audit exhausts all (2^5) endpoint choices and verifies the
claim:

```text
python3 scratch/audit_catalan_rainbow_floor_counterexample_k6_20260731.py
```

## 3. Correct conclusion

Theorem 3.1 remains an exact conditional theorem.  Its proof has three
sound ingredients:

1. distinct selected seam facets give distinct cuts on the unmarked rail;
2. distinct inserted facets and seam facets give distinct cuts on the
   marked rail; and
3. each switch replaces colours
   (J,z+(X\cap J)) by (J,X), so a rainbow choice deletes precisely one
   copy of every duplicated marked colour while filling every omitted
   unmarked colour.

What remains is a genuinely stronger **oriented split-repair matching**:
the Catalan injection must be chosen together with one incident side per
insertion so that the chosen split colours are the duplicate set and the
chosen seam facets are distinct.  Neither cap two, lower completeness, nor
the integrality-floor profile implies that matching for an arbitrary
saturating cycle or arbitrary injection.

This sharpens the reduction's status without weakening its utility: the
new target is still Catalan-sized, but it must be built into the
split-repair choice rather than inferred afterward.
