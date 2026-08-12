# K16 fixed75 C106: exact R2/R3 portal-partition no-go

Date: 2026-07-30

## 0. Verdict and scope

On the authenticated fixed-`F75` residual-31 face:

* all 270 R2 five-lock signatures are infeasible for both portal
  partitions `2` and `1+1`;
* all 90 R3 signatures are infeasible for all three portal partitions
  `3`, `2+1`, and `1+1+1`.

The proof is solver-free and shared across the partitions.  It is a corollary
of the authenticated marked price-four closed-walk theorem.  No reduced
candidate exists, so
`scratch/replay_k16_floor106_candidate_20260730.py` is not invoked.

This statement remains integral, fixed-`F75` conditioned, and source-relative
to the frozen 211,604-seam bank.  It is not a global or fractional C106
claim.

## 1. Exact profile and partition censuses

The count-106 equality identity is

\[
                              Q+R=5.                  \tag{1.1}
\]

The five-lock normal form has 1,024 integral signatures.  At total slack
`R`, its signature count is

\[
                         \binom5R3^{5-R}.             \tag{1.2}
\]

Thus R2 has 270 signatures and R3 has 90.  Every one services each
of the residual price-four targets

\[
                    T=\{46811,56173,60854\}           \tag{1.3}
\]

exactly once.

Because every positive seam slack is a positive integer, the positive-slack
multisets are exactly the integer partitions of `R`:

```text
R=2 : 2, 1+1
R=3 : 3, 2+1, 1+1+1.
```

These lists classify every portal partition; their order around residual
cycles is unrestricted and does not need separate enumeration for the shared
obstruction below.

## 2. Shared marked-cycle lemma

After deleting seams touching an `F75` port, seams hitting an
`F75`-serviced target, and seams of slack greater than five, the exact clean
graph has 205,694 arcs.  The authoritative state-expanded audit prices every
marked directed closed walk of slack at most five by its union of targets in
`T`.  Its table is

```text
mask  000 001 010 011 100 101 110 111
cost    6   3   3   6   3   6   6   6
```

Here 6 is a truncation sentinel: no closed walk of total slack at most five
has the specified mask.  Consequently:

1. every directed cycle meeting one specified member of `T` has slack at
   least three;
2. no directed cycle of slack at most five meets two members of `T`.

The audit checks all 180 marked provider occurrences and all eight return
masks, including pair supersets containing the third target.

## 3. R2 classification

### Theorem 3.1

Neither portal partition `2` nor `1+1` supports an integral balanced
residual-31 block for any of the 270 R2 signatures.

#### Proof

Any selected residual block decomposes into directed cycles.  Servicing even
one member of `T` requires a marked cycle, whose slack is at least three by
Section 2.  The entire packet has slack two.  Hence it cannot service any
member of `T`, whereas every signature demands all three.  This argument
does not depend on whether the two slack units lie on one portal or two.
QED.

Explicitly, partition `2` puts its sole portal on a cycle of slack two, which
is unmarked.  For partition `1+1`, placing both portals on one cycle again
gives an unmarked slack-two cycle, while splitting them gives two unmarked
slack-one cycles.  These are upper bounds and do not assert that every listed
portal arrangement exists.

Thus the exact conditioned feasibility list for both R2 partitions is empty.

Quantitatively this is a universal no-go over

```text
270 signatures x 2 partitions = 540 signature-partition branches.
```

For each marked target, the exact provider-return histogram over its sixty
providers is `cost3^5 cost4^20 sentinel>5^35`; hence zero marked provider can
close within the R2 budget.

## 4. Advance through R3

### Theorem 4.1

None of the portal partitions `3`, `2+1`, or `1+1+1` supports an
integral balanced residual-31 block for any of the 90 R3 signatures.

#### Proof

No slack-at-most-five cycle can service a pair from `T`.  Therefore three
distinct marked cycles are required.  Each has slack at least three, so the
packet would have total slack at least nine, contradicting R3.  This is
independent of the distribution of the three portal-slack units.  QED.

The component allocation is exhaustive:

```text
portal multiset   allocation among cycles    marked targets possible
3                 3                          at most 1
2+1               3, or 2 | 1                at most 1, or 0
1+1+1             3, 2 | 1, or 1 | 1 | 1    at most 1, or 0
```

Again these are upper bounds, not existence claims for every allocation.

The R3 conditioned feasibility list is therefore also empty.  In fact the
same marked-cycle theorem already eliminates R4 and R5, yielding the
previously frozen fixed-`F75` conditioned floor 107.

## 5. Exact replay

The focused corollary verifier is

```text
scratch/audit_l_k16_fixed75_c106_r2_r3_partition_corollary_20260730.py
SHA-256 57d4847f54fac6abd1ee38b4f40788756515f5503da047e24a8889313f0dc9b6

scratch/l_k16_fixed75_c106_r2_r3_partition_corollary_20260730.audit.json
SHA-256 c89966f57bdf226d595344c0274f3c2c5e25dae685f356c49461b42484a48625
payload 6b6850ad8949b586a4c80d76f32587d6a21f34038a8b4fe84a95af3b0382b2f0
```

It pins and verifies:

```text
scratch/l_k16_fixed75_residual31_c106_atlas_20260730.audit.json
SHA-256 a08a6d8f42b9e9e70b0e7278edfd5492032eb7733a3710c53e821101597a7125
payload b892695f00b0bc1120c3d9dd0c920b573cf36954e5aac0c236c4685f566b2ce0

scratch/l_k16_fixed75_c106_price4_closed_walk_floor107_v2_20260730.audit.json
SHA-256 58915e7da037ebba28e230dcd71e3084d1c4aacbfec80c5fc024128943550d7f
payload 6451cab631029429efb2548cd63ccbd3ec3417f6bf5aa0d383946aed413399b9
```

The output stores every one of the 270+90 signatures, the exhaustive portal
partitions, empty feasible lists, and the exact reason for rejection.  The
full marked-cycle theorem remains
`MATH_THEOREM_L_K16_FIXED75_CONDITIONED_FLOOR107_PRICE4_CLOSED_WALK_20260730.md`.

## 6. Candidate-checker boundary

The required candidate checker is authoritative for a positive seam list:

```text
scratch/replay_k16_floor106_candidate_20260730.py
```

No seam list is emitted here because the structural theorem excludes every
R2 and R3 residual block before physical separation, q1, residence,
all-depth, or compiler checks.  Therefore no reduced or physical PASS is
claimed.
