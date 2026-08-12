# Self-audit: dense-hook unique promoted port

**Date:** 2026-08-05  
**Object:**
`MATH_THEOREM_PBBS_DENSE_HOOK_UNIQUE_PROMOTED_PORT_TWO_C6_NOGO_20260805.md`

## 1. Port inverse

The promoted-parent theorem identifies ports with marked adjacent
zero-entry pairs, not merely with zero entries and not merely with the
unmarked parent component.  Inserting `00` into a strictly positive cyclic
vector creates exactly one such pair; the outer overlaps are `positive,0`
and `0,positive`.

## 2. Density quantifier

If `x_i>=2`, then removing one chip at any slot leaves `y_i>=1`, while all
other entries remain positive.  Thus the unique-port lemma applies to
every leaf-plucking C6 incident with `x`, not only to one selected cut.

The existence condition `b>=2q` is sufficient: start with two chips in
each of the `q` slots.  It is not claimed necessary.

## 3. Scope

The theorem excludes only:

1. one nonadjacent clean leaf-plucking C6;
2. a two-C6 jump using two distinct ports of one promoted parent;
3. a two-adjacent-step simulation of transport distance greater than two.

It does not exclude a long adjacent walk, a non-leaf C6 family, or a
higher q2-neutral circuit.

**Verdict: PASS.**

