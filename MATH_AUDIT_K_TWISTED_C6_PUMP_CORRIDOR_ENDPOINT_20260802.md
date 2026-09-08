# Independent audit: twisted `C6` pump corridor endpoint calculus

**Date:** 2026-08-02  
**Scope:** independent finite replay of the algebra in
`MATH_THEOREM_K_TWISTED_C6_PUMP_CORRIDOR_ENDPOINT_AND_TERNARY_FUSION_GATE_20260802.md`.
This is not an ambient-host existence computation.

## 1. Replayed rows

The independent script
`scratch/audit_k_twisted_c6_pump_corridor_endpoint_20260802.py` checks:

1. the three-run pump from its binary word, without importing the original
   audit implementation;
2. all physical root transitions and the formulas

   \[
   \alpha_j=p_{j\bmod3}+\lfloor j/3\rfloor,
   \qquad
   \beta_j=q_{j\bmod3}+\lfloor j/3\rfloor;
   \]

3. exact multiplicity three of every coordinate in each of the deletion
   and insertion streams;
4. all four positive/negative endpoint collar formulas after cutting the
   private edge;
5. exhaustive two-edge lower-palette replay for `J(5,2)`, `J(6,3)` and
   `J(7,3)`; every lower-transparent crossed rectangle has equal old lower
   colours, exactly as Theorem 3.1 requires; and
6. the literal six-atom Boolean-hex lower/upper/tail/head identity and zero
   signed charge under independently assigned endpoint phase potentials.

The retained output is

```text
PASS twisted-C6 ambient endpoint audit pump_cases=36 rectangles=21000 hexes=1
```

The 36 pump cases are `1<=d<=12` and slack `0,1,3`.

## 2. Proof audit

The connector condition is exactly the directed-history collar recurrence:
one checks the connector deletion against the predecessor insertion collar,
the connector insertion against the successor deletion collar, and every
old cross pair with index sum at most `d`.  Applying it in both event
polarities is therefore necessary and sufficient at the changed seams.

The two-edge obstruction proof is complete: equality of the lower
multisets has only two pairings.  In the direct pairing both candidate old
facets equal the intersection of the two crossed heads; in the crossed
pairing two distinct rank-`(r-1)` subsets would force the two old tails to
be the same rank-`r` set.  Thus exact lower-rainbow preservation is
impossible on a nondegenerate two-edge splice.

For the corrected Boolean hex, the known four-resource identity preserves
all immediate resource rows.  Three distinct old cycle components are
concatenated into one in the displayed order.  The three positive and
three negative connector tests are exhaustive.  The charge identity is
automatic only for one coherent physical lift; the theorem correctly keeps
it explicit for a quotient catalogue assembled from separately
canonicalized options.

## 3. Scope verdict

**PASS within stated scope.**  The theorem proves an exact endpoint state
and identifies the first palette-transparent topology operation.  It does
not prove:

* completion of the `6k` developed pump incidences into an owner/`q1`
  factor;
* existence of two prepared old Boolean-hex partner edges on distinct host
  components;
* acceptance of their collars by an arbitrary ambient chronology;
* deeper upper, source/envelope, exterior-window, or compiler rows.

The arithmetic `6k>r-2` correctly shows only that the current small
protected-factor theorem is inapplicable.  It is not an impossibility
theorem for every prospective or quotient-aware host.
