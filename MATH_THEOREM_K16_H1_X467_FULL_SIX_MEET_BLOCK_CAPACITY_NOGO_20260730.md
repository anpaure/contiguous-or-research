# K16 H1 joint13: full six-meet block-capacity no-go for `x467`

Date: 2026-07-30  
Status: **GO, exact conditional learned unit**

## Theorem

In the frozen explicit-witness joint13 fibre, choice `x467`—the flat-1
singleton chart for the residual hole `0x2c6d`—is impossible.

This is a conditional statement about one chart in the thirteen-position
fibre.  It is not an UNSAT result for joint13, does not say that `x467` was
forced, and is not an unrestricted K16 no-go.

## Proof

Conditional on `x467`, the authenticated physical-meet quotient is exhaustive:
the canonical flat-1 value is one of

```text
0x2849, 0x2869, 0x286d, 0x2c49, 0x2c69, 0x2c6d.
```

For each fixed flat-1 state, exhaust all 65,535 nonzero physical flat-0
values and evaluate the three original collar-0 charts `[0,0]`, `[0,1]`, and
`[1,1]` directly.  The maximum numbers of residual targets simultaneously
coverable in collar 0 are

| flat-1 state | collar-0 capacity |
|---|---:|
| `0x2849` | 4 |
| `0x2869` | 5 |
| `0x286d` | 5 |
| `0x2c49` | 4 |
| `0x2c69` | 5 |
| `0x2c6d` | 3 |

Independently, canonical-intersection enumeration over the other three safe
blocks gives exact target capacities 23, 14, and 12.  Their sum is 49.

Choose one valid chart for every one of the 55 residual targets and assign
the target to its chart's safe block.  The assigned target sets form a
partition, so their total size is bounded by the sum of the four block
capacities.  In the six meet states these sums are respectively

```text
53, 54, 54, 53, 54, 52,
```

all strictly below 55.  Hence every physical meet state under `x467` is
impossible, proving the conditional unit `not x467`.

The per-block upper bounds are safe because canonical normalization replaces
each editable cell by an intersection of selected target labels crossing it.
This preserves every selected chart and puts every cell in the 216-state meet
closure.  For interval OR `V`, target `T`, and residual need `N`, chart
validity is exactly `V subseteq T` and `N subseteq V`.

## Exact learned clauses

In the 1,790-variable explicit-witness CNF, the derived clause is the unit

```text
(-467).
```

In the exact 469-variable proxy/supply-code composition, the five code bits
for target `H=0x2c6d` are variables `81,82,83,84,85`.  Old chart 2 has
little-endian code pattern `0,1,0,0,0`, so its exact exclusion clause is

```text
(81 OR -82 OR 83 OR 84 OR 85).
```

No other chart of `H` is excluded by this theorem.  In original
chart-indicator form (with the sixteen contracted actions treated as zero in
the 469-variable composition), the proof adds the unconditional other-collar
cuts

```text
sum A[T,j], j=3..12  <= 23,
sum A[T,j], j=13..18 <= 14,
sum A[T,j], j=19..28 <= 12,
```

and, conditional on `x467`, collar 0 has capacity at most 5.  Summing with
the exact one-chart-per-target equality gives `55 <= 54`, the shortest form
of the contradiction.  The state-specific rows strengthen this to totals
`53,54,54,53,54,52`.

## Authentication

```text
physical six-state meet audit
  SHA-256 e8a4e58cea9fafb93a4fd97e28a5e665b4f698cc486ab52d2687cbba2a934be3

independent 23+14+12 block-capacity audit
  SHA-256 f9c262957c8eb2800484f39fa7387525da4031c3a8b50f043211216372dd1850

all-six collar-capacity audit
  SHA-256 b4859efd53d41126a6167792e7a269fe7d1b8fe9db079265af154dd03bb14507

all-six audit driver
  SHA-256 5ef093fdae8bca39069f07b0aa05b59f2d97d657016cce257321dd7d1dbd2a96

second all-six clause audit
  SHA-256 88858fdda57e1993f8f5129ea8507905401e604e0be267817139923e844da878

zero-state/action-mode Hall parent
  SHA-256 a50992c88efe63d6981f639e1208cf6f9c31676821def50a80e61330b1063c44

all-six H100 byte-replay manifest
  SHA-256 ee35ec9f83ef56696f07d9cd08add9d12bd6ccfb06b86cf4a034859084a75c57
```

The block-capacity enumeration was independently replayed on H100 under a
60-second/512-MiB cap, reproducing every structural result field.  No SAT
solver verdict is used.  The all-six extension was separately replayed on
H100 core 13 under the same wall/address caps; it finished in 5.50 seconds,
used 17,920 KiB RSS, and reproduced its audit byte-for-byte.  All heavy
artifacts were written under unique `/home/amodo/or15/work` directories;
none was written to `/dev/shm`.
