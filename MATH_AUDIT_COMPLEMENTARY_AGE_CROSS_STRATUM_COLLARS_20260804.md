# Independent proof audit: complementary-age cross-stratum collars

**Date:** 2026-08-04  
**Audited file:**
`MATH_THEOREM_COMPLEMENTARY_AGE_CROSS_STRATUM_COLLARS_20260804.md`

## 1. Off-by-one convention

Put a new seam transition in slot zero.  The `i`-th retained transition on
one inward side occupies slot `-i`, and the `j`-th retained transition on the
other occupies slot `j`.  Their transition-slot separation through the seam
is therefore `i+j`.  Since consecutive transition slots have separation one
(the triangle pulse), the correct safety inequality is

\[
                              i+j\ge L.
\]

Thus the reversal `i -> L-i` is exactly tight.  No extra `+1` may be inserted
if ages start at one as they do in the theorem.

## 2. One-seam and two-seam checks

An `L`-resident transition word has no repeated direction among the first
`L-1` inward slots, and its cut direction cannot occur there.  Therefore the
one-seam prescription uses `L-1` distinct collar labels plus one cut label;
`m>=L` is the exact elementary room condition.

For two seams, capping absence by the value `L` is safe: if either direction
is absent, its inequality is automatic.  Once `p,q` are excluded from the
large collars, every possible new short repetition is represented by one
edge missing from `G_sigma`.  A perfect matching plus the fixed cut direction
is consequently both necessary and sufficient for common-direction
relabeling.  The long-arc and exceptional-direction hypotheses are still
needed and are stated explicitly.

## 3. Balanced-support check

With equal two-end support, each direction contributes at least `L` to the
sum of its two endpoint ages.  There are `L-1` directions, while the total of
both age permutations is exactly

\[
              2(1+\cdots+(L-1))=L(L-1).
\]

Hence every contribution equals `L`.  Complementing the endpoint-zero age
therefore also complements endpoint one.  The claimed matching is valid at
both seams simultaneously.

## 4. Automatic-range check

For a direction present at both ends, its two forbidden degrees sum to at
most `L-2`; for a direction present at only one end, its forbidden degree is
at most `L-2`.  The bound is symmetric.  On `n=m-1` non-cut directions,
minimum degree is at least `n-(L-2)`, which reaches `n/2` at
`m>=2L-3`.  The standard half-minimum-degree Hall argument is correct.

Choosing `p,q` afterward needs three directions outside the union of the two
large collars: the common cut direction and the two exceptional directions.
The union has size at most `2L-2` inside a set of size `m+2`; this yields the
slightly stronger worst-case bound `m>=2L-1`.

## 5. Scope verdict

**PASS.**  The theorem rigorously improves the crude `4L` relabelling range
and gives a critical-scale certificate, but it correctly does not claim:

1. that balanced-support cuts exist in every long-run cube cycle;
2. that many such cuts coexist in one global splice;
3. that `Q_0` or `Q_1` is absorbed without a pulse;
4. any lower/upper palette or compiler property.

The remaining critical residence gate is now a phase-coherent cut-pattern
construction, not raw collar cardinality.
