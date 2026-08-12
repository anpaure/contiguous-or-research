# Canonical upper-loss chain in the Type-I `k=11` branch

## Result

Assume the exact Type-I normalization

```text
A[0]=63={0,1,2,3,4,5}
```

and lexicographically sort the five remaining coordinate occurrence columns
as in `K11_RESIDUAL_COORDINATE_LEX_IMPLEMENTATION.md`.  Then every interval
OR using position zero belongs to the single fixed chain

```text
63 < 1087 < 1599 < 1855 < 1983 < 2047.          (1.1)
```

Consequently every target outside this chain has a selected witness wholly
inside the 464-position suffix.  This is an exact WLOG consequence of the
residual coordinate action, not a prescribed central-row ansatz.

## First-occurrence proof

For an outside coordinate `b in {6,7,8,9,10}`, let

```text
f_b=min{p>=1:b in A[p]}.
```

Every `f_b` exists because the suffix core covers the singleton `{b}`.
The lex module orders complete occurrence columns by

```text
column(6)<=lex column(7)<=lex ... <=lex column(10).       (2.1)
```

All five columns are zero at position zero.  If `a<b` but `f_a<f_b`, then
the first row at which columns `a,b` differ is `f_a`, with values `(1,0)`.
This contradicts (2.1).  Hence

```text
f_10<=f_9<=f_8<=f_7<=f_6.                                (2.2)
```

At a prefix endpoint `p`, the outside coordinates already present are

```text
{b:f_b<=p}.
```

Equation (2.2) makes this an upper suffix of the ordered list
`6,7,8,9,10`.  Simultaneous first occurrences may skip a level but cannot
produce another set.  Adding the fixed low six coordinates gives precisely

```text
C_0=63,
C_1=63+2^10=1087,
C_2=C_1+2^9=1599,
C_3=C_2+2^8=1855,
C_4=C_3+2^7=1983,
C_5=C_4+2^6=2047.
```

Any physical interval containing position zero starts at zero and is such a
prefix.  Its OR therefore lies in (1.1).

## Exact SAT consequence

The existing direct upper-target witnesses and compressed rank-seven
witnesses are existential.  For every noncanonical target we may require the
selected witness to avoid position zero:

* for direct ranks eight, nine, and ten, set `Inside(0)=false` unless the
  target is respectively `1599,1855,1983`;
* for a noncanonical rank-seven target, forbid both
  `active AND Inside(0)` and
  `exception_slot_target AND exception_Inside(0)`;
* the unique rank-eleven target is already `2047`; rank six is already
  anchored by the literal `63`.

This takes no new target or interval variables.  Exact-one generic-slot
selection and the existing endpoint absent-bit clauses compress the current
production form to `0 variables / 32 clauses`; see
`K11_TYPE1_PREFIX_CHAIN_SELECTOR_COMPRESSION.md`.  It merely exposes a
consequence already implicit in the array bits and the coordinate quotient.
It should be guarded by both the Type-I and residual-coordinate-lex options.

The reduction proves neither SAT nor UNSAT.  Its purpose is to make the
six-loss upper-core theorem propagate immediately through the existing
target-witness selectors.
