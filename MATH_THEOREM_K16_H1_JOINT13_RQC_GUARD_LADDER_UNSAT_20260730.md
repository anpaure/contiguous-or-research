# K16 H1 joint13: solver-independent R/Q/C guard-ladder UNSAT

Date: 2026-07-30  
Status: **GO, exact only for the frozen thirteen-cell joint13 fibre**

## Scope

Fix the authenticated length-12,873 H1 source and allow arbitrary nonzero
values only at

```text
0,1 | 4486,4487,4488,4489 | 6438,6439,6440 |
12869,12870,12871,12872.
```

The complement is frozen.  There are 55 residual targets and the source hole
is `H=0x2c6d`.  This theorem eliminates the seven H charts left by the
all-29 capacity theorem, hence proves this **support-restricted fibre** UNSAT.
It uses no SAT verdict and no Cartesian coverage-family join.

It is not a normalization of arbitrary length-12,873 words into this support
and is not an unrestricted K16 no-go.

## 1. Owner-capacity lemma

For collar `b` and canonical meet tuple `s`, let `Gamma_b(s)` be the residual
targets having at least one valid local chart.  Canonicalization to target
intersections preserves every selected chart and gives exactly 216 possible
cell states.  A direct exhaustive census covers all

```text
216^2, 216^4, 216^3, 216^4
```

tuples in the four collars.

Let

```text
R = 0x4879,   Q = 0x6879,   C = 0xcc61.
```

The ordinary maxima `max |Gamma_b minus {H}|` and the same maxima excluding
both `H,R` are

```text
M(-H)    = 7,23,14,12
M(-H,-R) = 7,23,14,12.                              (1.1)
```

When displayed targets must be available in the collar, the exact maxima of
`|Gamma_b minus {H}|` are

```text
owner R       5,14, 9,11
owner Q       5,14, 9,12
owner C       5,15, 8,12
owner R,C     2,12, 7,11
owner R,Q     5,14, 9,11
owner R,Q,C   0,12, 6,10.                           (1.2)
```

These are availability maxima, so using (for example) an `owner Q` bound in
a block where `R` is assigned elsewhere can only overestimate that block's
assigned capacity.  Every inequality below is therefore a sound upper bound.

If H chooses chart `j` in collar `b` and R is assigned to collar `c`, put

```text
K_j(-R) = max |Gamma_b minus {R}| with chart j valid for H,
K_j(R)  = max |Gamma_b| with chart j valid for H and R available.
```

The exact target-owner partition gives

```text
c=b:  K_j(R)  + sum_{d != b} M_d(-H,-R),
c!=b: K_j(-R) + G_c(R) + sum_{d notin {b,c}} M_d(-H,-R).   (1.3)
```

Any value below 55 excludes that owner case.

## 2. First guard eliminates five charts

For the seven surviving charts, (1.3), in R-owner order `0,1,2,3`, is

| H chart | explicit variable | four owner totals |
|---:|---:|---|
| 6  | 471 | `54,33,51,55` |
| 15 | 480 | `54,47,42,55` |
| 20 | 485 | `54,47,51,54` |
| 21 | 486 | `53,46,50,53` |
| 24 | 489 | `53,46,50,53` |
| 27 | 492 | `53,46,50,51` |
| 28 | 493 | `53,46,50,53` |

Thus charts `20,21,24,27,28` are immediately impossible.  Charts 6 and 15
can survive this first bound only with R assigned to collar 3 and every term
of the total 55 tight.  In both charts `K_j(R)=0`, so R cannot be assigned to
the H collar itself.

## 3. The two equality rows collapse by Q and C

Charts 6 and 15 are the full intervals of their respective width-four and
width-three H collars.  Validity for H forces the full collar OR inside H,
and every subinterval OR is consequently inside H.

Every need of Q has outside-H part `0x4000` or `0x4010`; every need of C is
the full label `0xcc61`, whose outside-H part is `0xc000`.  Therefore neither
Q nor C can be assigned to the H collar under chart 6 or chart 15.

Starting from the R-owner-3 total 55, assigning Q gives these bounds:

```text
chart 6:  Q owner 0 -> 53; owner 1 -> impossible H collar;
          Q owner 2 -> 50; owner 3 -> 55.

chart15:  Q owner 0 -> 53; owner 1 -> 46;
          Q owner 2 -> impossible H collar; owner 3 -> 55.
```

Hence equality forces Q to collar 3 with R.  From that remaining total 55,
assigning C gives

```text
chart 6:  C owner 0 -> 53; owner 1 -> impossible H collar;
          C owner 2 -> 49; owner 3 -> 54.

chart15:  C owner 0 -> 53; owner 1 -> 47;
          C owner 2 -> impossible H collar; owner 3 -> 54.
```

Every case is now strict or physically impossible.  Thus charts 6 and 15 are
also excluded.

## 4. Exact units and fibre conclusion

The seven learned explicit-witness units are

```text
-x471, -x480, -x485, -x486, -x489, -x492, -x493.
```

In the compact five-bit H code `[81,82,83,84,85]` (least-significant bit
first), their clauses are

```text
chart  6: ( 81 OR -82 OR -83 OR  84 OR  85)
chart 15: (-81 OR -82 OR -83 OR -84 OR  85)
chart 20: ( 81 OR  82 OR -83 OR  84 OR -85)
chart 21: (-81 OR  82 OR -83 OR  84 OR -85)
chart 24: ( 81 OR  82 OR  83 OR -84 OR -85)
chart 27: (-81 OR -82 OR  83 OR -84 OR -85)
chart 28: ( 81 OR  82 OR -83 OR -84 OR -85).
```

The earlier all-29 theorem excluded the other 22 H charts.  Since the H row
must choose exactly one of its 29 charts, all choices are now impossible.
Therefore the frozen arbitrary-value joint13 fibre is UNSAT.

## 5. Authentication and independent audit

The exhaustive program ran on one H100 CPU core in

```text
/home/amodo/or15/work/root_k16_h1_r4879_q6879_cc61_guard_71f15208
```

under a 240-second wall cap and 1-GiB address-space cap.  It finished in
96.67 seconds with 9,092 KiB maximum RSS, exit 0, and wrote nothing to
`/dev/shm`.

Frozen hashes:

```text
enumerator source
  71f1520846a078558dcf76c98b61eeb013e73df662d6a6f83c6c3ff73aaa9232
Linux binary
  6f73465014c00548ad908fad569d04f39d742316497481b2be79bda1885075f9
result
  11a019088c1e1825e7033a8fb318ad535778e73ee708afec6ef74bfebab9700c
resource log
  eb49061e3b1fcb598ca6aeacda1efd67e2413e9e1c28cfef4392bc452e50d864
witness map
  146f81f628148b2fd904bb5e030236135b00cd502aa2d58051ebb32d6e82638a
```

The first independent checker reconstructs the target ledger, chart geometry,
216-state closure, every stored maximizing coverage set directly from its
physical cell tuple, all H/R/Q/C presence and exclusion semantics, all 29 by
four R-owner totals, and every compact clause.  The second checker reconstructs
the full-span physical obstruction and every Q/C owner-ladder inequality.

```text
owner-formula checker
  a3c67584b15bb617d726c62b454cb110bdeaa275c01fa7ea59d068daef09431e
owner-formula audit
  3ca2a730c1889d922d172157e91d2e5f7bee74753821f9d5426cd44a58855940
guard-ladder checker
  c5727d1d11c571827a439b5791a01608616b71e28c67cbda91333152614a7a19
guard-ladder audit
  d20f49e93f912b92d75a65186ab10108446c8d94ac03df7f2f5dfd24d7b8ea0b
```

The prior 22-unit theorem is
`MATH_THEOREM_K16_H1_H29_CONDITIONED_COLLAR_CAPACITY_UNITS_20260730.md`,
SHA-256
`230742fb4f6a28da91eb2a0020c10114f549b9692966c1d456afe4eb48bdc9ee`.

The global bracket remains

```text
12873 <= nu(16) <= 12874.
```
