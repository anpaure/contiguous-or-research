# Independent audit of the unsaturated one-copy hinge

**Date:** 2026-08-02  
**Audited theorem:**
`MATH_THEOREM_A_UNSATURATED_ONECOPY_HINGE_AND_PROTECTED_COMPLETION_GATE_20260802.md`,
SHA-256
`24561cd24c7b2e8e401d3c06601c370a05c171f19bac19399293421e3bfc0c2e`.

## Verdict

PASS, with the literal-state scope made explicit.  The menu cardinality is
the number of distinct order-`d` tail **tuples**, not necessarily the number
of distinct tail-union masks.

The strengthened lightweight verifier
`scratch/audit_a_unsaturated_onecopy_hinge_20260802.py`, SHA-256
`3d360701dcc5811b870dd8e70e997497dfbf1414b0f7ed393929f0f6bf5a4a60`,
returns

```text
PASS
nonempty_chains=8212 nonempty_traces=14692
empty_traces=42
rank2_words_checked=3267
tuple_union_collision_example=PASS
fixed_q1_one_step_tails_checked=360
```

## What was checked

For every `r=3,...,6`, `d=1,...,4`, and every strict nonempty chain of
admissible length, the replay checks:

1. every source letter is nonempty and the full `(d+1)`-letter union is the
   prescribed owner `T`;
2. every requested terminal suffix union is exactly `S_q`;
3. the two endpoint-state unions are exactly (2.3) and (2.4), both proper;
4. the missing guard `y` is absent from the tail union;
5. the literal tail tuples have cardinality `2^(|S_1|-1)` and the literal
   head tuple is fixed.

The empty-chain formula was replayed for `r=3,...,8`, `d=1,...,7`, including
its exact endpoint unions.  Exhaustion of all nonempty-letter words over a
rank-two owner proves the claimed impossibility for `d=2,...,6`; the positive
depth-one word is checked separately.

Finally, 360 small literal de Bruijn tail systems confirm Proposition 4.1:
after the last letter (the depth-one suffix target) is fixed, every literal
tail has exactly one compatible head.  Hence no single-transition relation
with that fixed payload can contain a nontrivial two-sided endpoint product;
a completed two-sided hinge must be a longer macro or a correlated relation.

The collision example

```text
T={1,2,3}, S_1={1,2}, y=1, x=2, d=2, ell=1
```

has two different literal tails (from `A=empty` and `A={2}`) but the same
tail-union mask.  It validates the theorem's corrected warning: a downstream
flow may use the full de Bruijn tuples, but may not count these as distinct
after quotienting only by union.

## Scope

This audit proves local owner legality, suffix payloads, and endpoint
unsaturation.  It does not prove residence of the repeated filler, protected
upper witnesses, exterior interval transparency, the shifted Hoffman cuts,
a connected spanning skeleton, or bounded reset cost.  Those are precisely
the protected-completion rows retained as open in Sections 4--5.
