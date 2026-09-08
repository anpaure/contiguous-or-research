# The p6440 unshielded O2 + I0 + one-return OR-convolution theorem

**Date:** 2026-07-30

**Lane:** D, exact finite K16

**Status:** proved, solver-free finite exhaustion in the stated fibre

## 1. Result

Let `w` be the authenticated reorganized-H1 word

```text
scratch/k16_h2_to_h1_p0.h1.word
SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a
```

of length 12,873.  Its unique uncovered nonzero mask is

```text
H = 0x2c6d.
```

Consider exactly the following four-cell family.

1. At `u=6439`, choose one of all 16 retained unshielded outer-only
   debt-two (`O2`) values.
2. At the adjacent portal `v=6440`, choose one of all 16 portal values.
3. Choose one of all 25 retained shielded zero-export inner-only (`I0`)
   rows.
4. Choose one arbitrary nonzero one-cell return that supplies every current
   positive deficit.

The adjacent cells `u,v` are one packet.  That packet, the `I0` cell, and
the return cell must be three distinct clusters, with every consecutive
inter-cluster open gap having source OR `0xffff`.  No additive assumption is
made inside the adjacent packet.

**Theorem.** None of the resulting words is universal.  There are

```text
16 * 16 * 25 = 6,400
```

packet-plus-`I0` states and exactly 521,088 geometrically admissible,
integral one-return joins.  Exhaustive exact signed-multiplicity replay finds
zero completions.  The minimum final number of holes is nine.

This is the first retained broken-shield split stratum above the shielded
`I0+O2+return` theorem.  It is a four-site `[2,1,1]` atomic-cluster result,
so it is disjoint by cardinality from the unrestricted radius-three lane.
Every `I0` site is outside the frozen joint13 support, so every member of
this family is also outside that fixed joint13 fibre.

## 2. Exact adjacent-packet identity

For a word `w`, write `m_w(T)` for the number of consecutive intervals whose
bitwise OR is `T`.  A rewrite has signed incidence column

```text
beta(T) = m_w(T) - m_w'(T).
```

Put

```text
a = w_u = 0x206d,
b = w_v = 0x806d,
```

and let `x,y` be the new values at `u,v`.  Let `L(lambda)` be the
multiplicity of the empty or source suffix context ending at `u-1`, and let
`R(rho)` be the multiplicity of the empty or source prefix context beginning
at `v+1`.  Define the exact endpoint transforms

```text
Theta_u(c) = sum_lambda L(lambda) e_(lambda OR c),
Theta_v(c) = sum_rho    R(rho)    e_(c OR rho),
Phi(q)     = sum_(lambda,rho) L(lambda)R(rho)
             e_(lambda OR q OR rho).
```

Affected intervals use only `u`, only `v`, or both.  Partitioning them into
these three disjoint classes gives the exact packet column

```text
B_(x,y)
  = Theta_u(a) - Theta_u(x)
  + Theta_v(b) - Theta_v(y)
  + Phi(a OR b) - Phi(x OR y).                 (2.1)
```

Let `beta_u(x)` and `beta_v(y)` instead denote the two source-relative
single-cell columns, with the other adjacent cell frozen.  Expanding those
two columns gives the equivalent mixed-rectangle identity

```text
B_(x,y) = beta_u(x) + beta_v(y)
          - [Phi(x OR y) - Phi(x OR b)
             - Phi(a OR y) + Phi(a OR b)].     (2.2)
```

Equations (2.1) and (2.2) were evaluated independently and agreed for all
256 packet pairs.  The 256 full signed packet profiles are all distinct,
even though `x OR y` takes only eight values, with multiplicities

```text
0xa444:4,   0xa445:12,  0xa44c:12,  0xa44d:36,
0xa464:12,  0xa465:36,  0xa46c:36,  0xa46d:108.
```

Consequently the joint OR is not a sound packet quotient.  Separately,
Section 5 exhibits 6,400 distinct signed partial profiles but only four
positive deficit supports, so the positive hole set is not a sound state
quotient either.

## 3. Additivity outside the packet

If an open source gap between two edit clusters has OR `0xffff`, every
interval crossing that gap already has full OR.  Its target is unchanged by
either cluster.  Hence all mixed differences across that gap vanish.  For a
packet choice `(x,y)`, an `I0` column `beta_I`, and a geometrically separated
return column `beta_R`, the exact total column is therefore

```text
beta_total = B_(x,y) + beta_I + beta_R.         (3.1)
```

This is the only additivity used by the census.

Let

```text
kappa(T) = m_w(T) - 1,
r(T) = B_(x,y)(T) + beta_I(T) - kappa(T).
```

The packet-plus-`I0` state is completed by a return exactly when

```text
beta_R(T) <= -r(T) for every nonzero T.         (3.2)
```

Thus the completion test is an integral coordinatewise capacity test, not a
fractional or hole-only test.

## 4. Complete return interval

Fix a return position `t`.  For a target `T`, let `C_t(T)` be the OR of the
maximal source context around `t` whose cells are all submasks of `T`, with
the cell at `t` omitted.  Replacing `w_t` by `z` creates an interval through
`t` with OR `T` exactly when

```text
T minus C_t(T) subseteq z subseteq T.
```

Therefore a single return is a common-provider candidate for every target in
a positive-deficit set `D` if and only if

```text
L_t(D) := OR_(T in D) (T minus C_t(T))
          subseteq z
          subseteq
U(D) := AND_(T in D) T.                        (4.1)
```

Enumerating every submask between `L_t(D)` and `U(D)` at every physical
position is complete for a one-cell common-provider return.  The census then
recomputes the whole signed column and applies (3.2), so (4.1) is only a
candidate generator and cannot hide collateral losses.

All positive demands in this stratum are one.  Moreover every equal-length
replacement has zero total signed mass.  Thus coordinatewise dominance
between two complete columns with the same total mass is possible only when
the columns are equal.  No strict full-profile dominance pruning is
available.

## 5. Census

The retained primitive atlas is exactly:

```text
unshielded outer debt 2: 16 rows, all at p6439;
unshielded outer debt 3:  8 rows, all at p6438;
unshielded outer debt 4: 24 rows, at p6437/p6438;
unshielded inner or joint debt <=4: 0 rows;
shielded I0: 25 rows, at p6606^16, p7984^8, p9726^1.
```

In particular the present `O2` family is the smallest retained unshielded
outer family, and no retained unshielded inner/joint row of debt at most four
precedes it.

The 6,400 packet-plus-`I0` states have 6,400 distinct exact signed profiles.
Their positive deficit supports are:

```text
{0x286d,0x287d,0x2c6d}                         3,776 states;
{0x286d,0x287d,0x2c6d,0x846d}                 1,024 states;
{0x286d,0x287d,0x2c6d,0x846d,0xa46d}          1,024 states;
{0x286d,0x287d,0x2c6d,0xa46d}                   576 states.
```

Only the first support has a common-provider bank, containing 138 literal
rows.  Across its three `I0` physical bases, all

```text
3,776 * 138 = 521,088
```

joins pass the inter-cluster geometry and unit-demand filters.  Every one is
then tested against the complete signed profile.  The final hole histogram
is

```text
9:241664, 10:30208, 11:3776, 12:101952,
13:37760, 14:101952, 17:3776.
```

The retained nine-hole witness uses

```text
p556 : 0x0063 -> 0x286d,
p6439: 0x206d -> 0xa004,
p6440: 0x806d -> 0x0441,
p6606: 0x840c -> 0x0004,
```

and leaves exactly

```text
{0x2463,0x2467,0x2867,0x2877,0x2c67,
 0x3463,0x3467,0x3663,0x367b}.
```

Literal interval recount of the saved word reproduces this set.

## 6. Independent audit and resources

The native C++ producer rebuilt the retained atlas, asserted both packet
formulas for every pair, generated every common-provider interval, checked
cluster geometry, and ran all 521,088 exact capacity tests.  It used one H100
CPU in the exclusive directory

```text
/home/amodo/or15/work/threadD_k16_p6440_unshielded_o2_i0_return_orconv_20260730
```

with a 512 MiB address-space cap, no `/dev/shm` writes, and no swap.  Compile:
5.76 seconds and 287,740 KiB maximum RSS.  Census: 3.60 seconds and 24,064
KiB maximum RSS.

A cross-language replay, independent of the native C++ but using the frozen
Python precheck helper library, rebuilt the endpoint convolution and mixed
rectangle, rebuilt all return banks, repeated all 521,088 signed joins,
reproduced the complete histogram and minimum, and literally replayed the
saved word.  It passed in 20.57 seconds at 87,552 KiB maximum RSS, with no
swap.

Authoritative artifacts:

```text
scratch/threadD_k16_p6440_unshielded_o2_i0_return_orconv_mitm_20260730.cpp
  d23967921eb233d86400c01df8c4cd93164d73ad690c51a545266ab1b4cd2002
scratch/audit_threadD_k16_p6440_unshielded_o2_i0_return_precheck_20260730.py
  954b62acece9b1672fe078ae3851c1272a3edb45619a80e72dd386ed842e57e7
scratch/threadD_k16_p6440_unshielded_o2_i0_return_precheck_20260730.audit.json
  e1940462f771606705ca0b75473b17586cbda7af35c800da5afa02e9572e7c73
scratch/threadD_k16_p6440_unshielded_o2_i0_return_orconv_mitm_20260730/
  threadD_k16_p6440_unshielded_o2_i0_return_orconv_mitm_20260730.raw.audit.json
  2d803927db1be68a45bfac73fb88e243ed624618e1da50ff6b19d2dcfad99846
scratch/audit_threadD_k16_p6440_unshielded_o2_i0_return_independent_20260730.py
  40b6c9d82e6aa25cafac9629686a8c3a166b54031cacbe9f3ac43d436b337b54
scratch/threadD_k16_p6440_unshielded_o2_i0_return_orconv_mitm_20260730/
  threadD_k16_p6440_unshielded_o2_i0_return_orconv_mitm_20260730.independent.audit.json
  fbaa5238c6a62e9762dfe3bd8ee38488ecf7bb5492a44a6b85fd4d8258e8e49b
  payload fec319d129677ad88cb16e58426d42f8185e51f259d5cc7bb939b81414cf0c35
scratch/threadD_k16_p6440_unshielded_o2_i0_return_orconv_mitm_20260730/
  threadD_k16_p6440_unshielded_o2_i0_return_orconv_mitm_20260730.best.word
  00a5bfb12a838e8d76e42a7fa1e06e1dbc3f16a3a814a309003f44331dfd57fa
scratch/threadD_k16_p6440_unshielded_o2_i0_return_orconv_mitm_20260730.provenance.txt
  c9f8f258c983cebadcf6844009a82b848525dafa466ac836c73bb518b8e35be5
```

## 7. Exact scope boundary

The theorem closes only

```text
unshielded p6439 O2 + adjacent p6440 portal
  + one shielded I0 + one separated arbitrary return.
```

It does **not** close p6438 `O3`, p6437/p6438 `O4`, an unshielded inner or
joint service column, a same-cluster return, more than one broken source-FULL
gap, a compound or multi-cell return, multiple returns, another portal or
basin, the active unrestricted radius-three campaign, or the frozen joint13
campaign.  In particular, the high-debt/joint-service branch remains open.

The global finite bracket is unchanged:

```text
12873 <= nu(16) <= 12874.
```
