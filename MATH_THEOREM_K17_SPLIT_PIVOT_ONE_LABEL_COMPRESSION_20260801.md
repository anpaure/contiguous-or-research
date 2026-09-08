# One-label compression of the tight split-pivot collar

Date: 2026-08-01

## Theorem

In Theorem 4.2 of
`MATH_THEOREM_A_SPLIT_PIVOT_PHYSICAL_COLLAR_AND_BPLUS1_TERMINAL_PATH_20260801.md`,
the two fresh labels `q^-` and `q^+` need not be distinct.  They may be
identified with one fresh coordinate `q`:

```text
B^- = (B - {x_R}) + q,
B^+ = (B - {x_L}) + q.
```

All of the following local conclusions of Theorem 4.2 remain valid:

- the displayed source has `4h+1` letters;
- its depth-`h` row is the same `3h+1`-owner Johnson path;
- every owner has rank `r` and the owners are distinct;
- every native shared depth-`h-1` cell is the exact adjacent-owner
  intersection;
- every spanning depth-`h+1` cell is the exact adjacent-owner union;
- both immediate palettes are injective;
- every internal positive run and internal zero gap has length at least
  `h+1`;
- the pre/post insertion old-deck transport remains literal.

The labelled support drops from

```text
r + 3h
```

to

```text
r + 3h - 1.
```

Thus for `r=9,h=3` the source uses exactly 17 coordinates.  The earlier
two-label sufficient hypothesis missed `k=17` by one coordinate; the
compressed source fits it exactly.

## Proof

The source-row computation in Theorem 4.2 uses only the two set identities

```text
B^- cap X = X - {x_R},
B^+ cap X = X - {x_L}.
```

They remain true when the fresh coordinates are identified, because `q` is
outside `B` and `X`.  Hence the owner row and the tightness identity

```text
O_t cap O_(t+1) = C_t union (a_t cap a_(t+h+1))
```

are unchanged.  The literal lower and upper q1 rows therefore remain exact.

Owner simplicity also survives.  Every left-collar owner contains `q` and
`x_L` but not `x_R`; every right-collar owner contains `q` and `x_R` but not
`x_L`; and every central owner contains both `x_L,x_R` but not `q`.
Consequently the three blocks are disjoint as owner families.  Within each
block the moving `lambda/rho/D` prefix or suffix still determines the owner.

For lower q1 colours, after identification the five edge-class signatures
on `{x_L,x_R,q}` are

```text
{x_L,q}, {x_L}, {x_L,x_R}, {x_R}, {x_R,q},
```

which remain pairwise distinct.  For upper q1 colours the left and right
seams now share the distinguished signature `{x_L,x_R,q}`, but their full
values are respectively

```text
B union L union {q},
B union R union {q}.
```

They are distinct because the fresh nonempty banks `L` and `R` are
disjoint.  Every other cross-class collision is still excluded by its
distinguished-coordinate signature, and within-class injectivity is
unchanged.

The only changed residence trace is that of `q`.  It has a left endpoint
positive run of length `h`, an internal zero gap of length `h+1`, and a
right endpoint positive run of length `h`.  Both short positive runs are
clipped at path endpoints; the internal gap meets the exact floor.  All
other traces are those of Theorem 4.2.

Finally the distinct coordinate ledger is

```text
|B| + |L| + |R| + |D^-| + |D^+| + 1
= (r-h) + h + h + (h-1) + (h-1) + 1
= r + 3h - 1.
```

This proves the compression.

## Exhaustive `k=17` literal audit

The C++ checker fixes a six-coordinate `B`, the three-label `L,R` banks,
the two-label `D^-,D^+` banks, and one shared `q`.  It exhausts all 2430
choices obtained by:

1. assigning every element of `B` to `C`, `X_L`, or `X_R`, with both split
   shores nonempty;
2. choosing distinguished `x_L in X_L` and `x_R in X_R`.

For every case it reconstructs the 13-letter source and verifies:

- all ten literal depth-3 owners against their formulas;
- rank 9 and owner simplicity;
- the nine native rank-8 intersections and nine rank-10 unions;
- injectivity of both palettes;
- positive-run and zero-gap floor 4, with endpoint clipping;
- all 17 coordinates used, exactly `r+3h-1`;
- every old pre-insertion interval OR transports to the post-insertion word.

Artifacts:

```text
scratch/audit_k17_split_pivot_one_q_compression_20260801.cpp
scratch/k17_split_pivot_one_q_compression_20260801.audit.json
```

Audit status:

```text
PASS_K17_SPLIT_PIVOT_ONE_Q_COMPRESSION
```

## Scope

This closes the local coordinate-shortage row only.  It does not plant the
source in the finite SCD chronology, select an upper-exact Catalan connector,
verify all higher OR rows, or solve the lower common compiler.  In
particular it is not a `k=17` universal word and not by itself a proof of
`nu(17)=B(17)` or `B(k)+O(1)`.
