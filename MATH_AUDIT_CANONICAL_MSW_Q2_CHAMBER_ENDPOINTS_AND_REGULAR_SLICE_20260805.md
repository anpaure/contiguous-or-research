# Focused audit of the MSW q2 chamber endpoint scope and regular slice

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_CANONICAL_MSW_Q2_CHAMBER_LANGUAGE_AND_RENEWAL_GRAMMAR_20260805.md`,
SHA prefix `b677cbfc`  
**Scope:** endpoint flaw types and the family
`T_(a,b)=(1100)^a 111 (10)^b 1` only  
**Verdict:** PASS

## 1. Endpoint flaw classes

Let `x=T-{p,q}` with `p<q` satisfy the raw height/corridor/ordinal inverse
conditions.

If `x` is Dyck, the down-step created at `p` cannot start at height zero in
`x`.  Hence its target height is `H_T(p)=1`, not zero.  Between `p` and
`q`, `x` is two units below `T`; the down-step created at `q` can remain
nonnegative only when `H_T(q)=3`, not two.  Therefore flaw zero forces type
`(1,3)`.

Reflecting the path-height argument gives the terminal flaw class: its
first changed step must have target height zero and its second target height
two.  Thus flaw `r` forces type `(0,2)`.

Lemma 9.1 of
`MATH_THEOREM_MSW_Q1_INVERSE_AND_SQRT_BOUND_20260725.md` proves that a fixed
target has at most one raw pair of either type.  Hence there are at most two
endpoint-decorated labels in total, exactly as claimed.

## 2. The regular slice

For

```text
T_(a,b) = (1100)^a 111 (10)^b 1,
```

each `1100` block ends with a `D_2` barrier.  The sole productive chamber
after the final such barrier has low labels

```text
I = {a,a+1}
```

and high labels

```text
J = {0,1,...,b+1}.
```

Therefore `I` and `J` are disjoint exactly when `a>b+1`.  If `a=b+1`, the
central `U_0` and central `U_2` have the same ordinal label.  If `a<=b`,
the central `U_0` pairs with the unique chamber `U_3` having exactly `a`
later `U_3` steps.

For `a,b>=2`, either balanced predecessor visits both positive and negative
heights: the initial `1100` blocks supply positive visits, while the changed
central steps supply a negative visit.  Thus neither witness is removed by
the endpoint-flaw decoration.

Consequently

```text
T_(a,b) is internally missing  iff  a>b+1,
```

as stated.  No correction is required in the audited scope.
