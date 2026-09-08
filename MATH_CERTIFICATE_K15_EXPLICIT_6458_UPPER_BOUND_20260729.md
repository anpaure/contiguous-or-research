# The explicit `k=15` upper bound improves to 6,458

Date: 2026-07-29

The exact common-word compiler in
`MATH_CERTIFICATE_K15_EXPLICIT_6459_UPPER_BOUND_20260729.md` produces a
6,438-entry prefix whose residual consists of 21 masks.  Three of those masks
satisfy

\[
                         9524\ \mathbin\lor\ 13616=13620.       \tag{1}
\]

Consequently the two-letter suffix `9524,13616` witnesses all three masks:
the two one-letter intervals witness the operands and their two-letter union
witnesses `13620`.  Appending the other 18 residual masks individually gives
a suffix of length 20 and hence an explicit word of length

\[
                              \boxed{6458}.
\]

Together with the general lower bound this proves

\[
                         \boxed{6438\le\nu(15)\le6458}.         \tag{2}
\]

The word is

```text
scratch/k15_h19_exact_compiler_union_suffix_6458.word
```

with SHA-256

```text
c4300f7d6ec4f618ead87bb15ca3b831803f0c3296e3c5274f4ecd91fb029598
```

The deterministic builder and independent exhaustive verifier are

```text
scratch/build_k15_6458_union_suffix.py
scratch/verify_k15_nearoptimal_upper_bound.py
```

and their compact outputs are

```text
scratch/k15_h19_exact_compiler_union_suffix_6458.build.json
scratch/k15_h19_exact_compiler_union_suffix_6458.verify.json.
```

The verifier checks all 32,767 nonempty masks directly, verifies the first
6,438 entries still have the certified `D^3` middle carrier, and reports gap
20 above the lower bound.  No solver claim is needed for the length-6,458
upper bound once the word is stored.

## The 20-letter suffix is optimal for this prefix

Among the 21 residual masks, the only strict containments are

\[
                 9524\subset13620,
                 \qquad13616\subset13620.
\]

Consequently the residual family with `13620` removed is an antichain of
size 20.  Every new witness for one of these 20 masks must end in the
appended suffix.  Two intervals with the same right endpoint are nested, so
their ORs are comparable and cannot be two distinct members of the
antichain.  A suffix of length `s` supplies only `s` new right endpoints.
Therefore every completing suffix has length at least 20, even if intervals
crossing the prefix/suffix seam are allowed.  Equation (1) constructs one of
length 20.

The previously recorded check that the final prefix letter `7682` is a
subset of no residual target remains true, but is not needed for this
stronger endpoint-antichain proof.  Therefore the stored suffix is shortest
possible for this fixed prefix.  The exact OR--Pascal compatibility theorem
and terminal-collar audit are in
`MATH_ATTACK_L_K15_RESIDUAL_OR_PASCAL_AND_TERMINAL_COLLAR_AUDIT_20260729.md`.

This does **not** prove `nu(15)>=6458`: a different carrier or a different
common compiler prefix may have a more compressible residual.  It proves
only that further progress cannot come from reordering or redesigning the
suffix attached to the present prefix.
