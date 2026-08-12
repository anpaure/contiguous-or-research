# AD audit: exact 507-seam C=105 basis, one-dimensional Graver face, and 42-column escape parity

Date: 2026-07-30

## 1. Verdict

The exported 507-seam feasible GLOP support for the C=105,
slack-one, two-extra-weight-one aggregate branch has now been reconstructed
exactly from the raw seam binary.  It is a nondegenerate rational basic point,
not a numerical artefact.

More importantly, removing its one accidentally tight weight-one service row
leaves a one-dimensional rational face.  The integral kernel of that face has
one primitive generator, hence Graver basis `{+g,-g}`.  Eight seam coordinates
are zero in `g`, and every one of those eight coordinates is identically
`1/2` along the entire face.  Therefore no integral flow satisfying the
aggregate branch equations can be supported wholly on these 507 seams.

For the smallest witness, seam 95845, the obstruction reduces to the
coefficientwise identity

```text
2 [e=95845]
  = [56439 in H(e)] + [tail(e)=5298] - [head(e)=5298]       (e in S).   (1)
```

Target 56439 has price two.  In either labeled weight-one-repeat branch it is
therefore serviced exactly once, while port 5298 is balanced.  Extending (1)
to the complete slack-at-most-one cyclic seam layer gives an exact parity cut
on only 42 seams:

```text
sum_{e in O} x_e = 1 (mod 2),       |O|=42.                (2)
```

Thus every integer solution of either branch must use an odd, in particular
positive, number of these 42 escape seams.  This is a proved search reduction,
not global infeasibility of either branch.

## 2. Frozen inputs and branch semantics

The raw inputs are:

```text
scratch/k16_len8_source_seam_ledger_20260730.bin
  SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657

scratch/k16_direct_cycle_dual_exact_20260730.audit.json
  SHA-256 29b4aae4bc889e07261725b275455a58583d949932a0eeabf65eae33eb7c460d

scratch/k16_floor105_s1_repeat1_same_lp_support_20260730.audit.json
  SHA-256 f897a52feef096a8429097f02a5beb22cde9c2598a466f98e91fce9ce02121f6

scratch/k16_floor105_s1_repeat1_distinct_lp_support_20260730.audit.json
  SHA-256 98ad094849753c1df2c7b86422f27682a6a875e7da12d4517a6e02ad138d4aa6

scratch/k16_floor105_s1_repeat1_q2_lp_support_20260730.tsv
  SHA-256 1949605e913cc4e5f6c4d7f660225ca5a7218d8219f88b378902b0400d2997e6
```

The two named LP reports have the same positive support because the LP stage
imposed only the aggregate weight-one occurrence total.  It did **not** impose
the labeled distinction between one target occurring three times and two
targets occurring twice.  Consequently every theorem below is stated for the
common aggregate face and applies to both labeled shapes.

Let `b_t in {1,2,4}` be the exact scale-two target weights.  Their census is
15, 60, and 18 respectively.  In the branch at issue,

```text
total seam count                 = 105,
total dual slack                = 1,
weight-one service total        = 17,
weight-two service total        = 60,
weight-four service total       = 18.
```

Because every target must be serviced at least once, all 60 weight-two and all
18 weight-four targets are forced to service exactly one.  These 78 equations,
the weight-one aggregate equation, the slack equation, and endpoint balance
are the base equalities used below.  Count 105 follows from the scale-two
telescoping identity, so adding it does not change the face.

## 3. Exact cycle reconstruction and denominators

### Theorem 3.1 (exact cycle basis)

Let `S` be the 507 positive seams in the exported support.  Its directed
support graph has

```text
E = 507 edges,
V = 433 vertices,
c = 7 weak components = 7 directed SCCs,
rank(incidence) = V-c = 426,
cycle dimension = E-V+c = 81.
```

A deterministic minimum-residual decomposition yields exactly 81 simple
directed cycles.  Their incidence vectors have rank 81 modulo each of

```text
998244353, 1000000007, 1000000009,
```

and therefore form a rational basis of the complete circulation space on
`S`.  The canonical JSON hash of the ordered cycle lists is

```text
eacb0be64faf5d917390e3d1ec804bc61efb3601699dc5162742453b38311a33.
```

The cycle lengths range from 2 through 100.  The full length histogram and
all 81 ordered seam lists are frozen in the exact audit artifact.

### Proof

The checker streams the binary seam records named by the exported TSV, without
materializing or optimizing over the remaining seam variables.  Exact endpoint
pairs give the displayed graph census.  The incidence-rank formula on each
weak component gives `433-7=426`, hence cycle dimension 81.

At each decomposition step the checker takes a positive minimum-residual arc,
finds a simple directed return path, and subtracts their minimum residual.
It obtains 81 cycles, reconstructs all 507 floating values to error below
`1e-13`, and verifies their rank over the three prime fields.  Rank 81 over
even one field supplies a nonzero 81-minor over the integers; as the ambient
cycle space has dimension 81, the cycles are a rational basis.  QED.

### Theorem 3.2 (exact basic point)

In the 81 cycle coordinates, impose the 78 forced target rows, the weight-one
aggregate row, the slack row, and the one tight weight-one target row
`service(58385)=1`.  The resulting 81 by 81 integer matrix has

```text
determinant = -5447939798827891712
            = -256 * 21281014839171452.
```

The unique exact cycle coefficients and all 507 reconstructed seam values are
positive and strictly below one.  Their common denominator is

```text
D = 21281014839171452.
```

The seam-denominator histogram is:

| reduced denominator | seam count |
|---:|---:|
| 2 | 8 |
| 4,135,447,889,462 | 2 |
| 64,099,442,286,661 | 3 |
| 74,933,150,842,153 | 17 |
| 149,866,301,684,306 | 3 |
| 171,621,087,412,673 | 3 |
| 343,242,174,825,346 | 2 |
| 5,320,253,709,792,863 | 239 |
| 10,640,507,419,585,726 | 208 |
| 21,281,014,839,171,452 | 22 |

Exact replay gives endpoint balance zero, count 105, slack one, every target
covered, weight-one service total 17, and maximum outgoing port mass

```text
74499315280525 / 74933150842153 < 1.
```

The maximum difference from the exported GLOP values is below `9.82e-14`.

### Proof

All entries of the 81 by 81 system are integer cycle service or slack counts.
The checker solves it over `ZZ` by fraction-free exact linear algebra, records
the displayed nonzero determinant, and substitutes every resulting rational
coefficient back into the raw seam incidence, service, slack, and port rows.
No floating value is used in this substitution.  The denominator and replay
claims follow by reducing the exact fractions.  QED.

## 4. One-dimensional Graver and proximity theorem

Let `A_S x=b` denote endpoint balance on `S`, service one for the 78
weight-two/four targets, weight-one aggregate 17, and slack one.  Do not impose
the active row `service(58385)=1`.

### Theorem 4.1 (rank-one integer kernel)

The matrix `A_S` has rank 506 and rational nullity one.  Its integer kernel is

```text
ker_Z(A_S) = Z g
```

for the primitive vector `g` frozen in the audit.  Consequently the Graver
basis of `A_S` is exactly `{g,-g}`.  Every rational point of the base face is

```text
x* + theta g,       theta in Q.                           (3)
```

The vector `g` is nonzero on 499 seams and zero on exactly the following eight:

```text
95845, 132215, 139492, 175996,
178709, 207222, 207270, 207722.
```

Every one of these eight coordinates equals `1/2` in `x*`; hence it equals
`1/2` at every point (3).  The base face contains no integral point.

### Proof

After endpoint balance, the circulation space has dimension 81.  The 78
forced service rows, the weight-one aggregate row, and the slack row have
exact rank 80 in the cycle basis.  Thus `rank(A_S)=426+80=506` and its rational
kernel is one-dimensional.  The checker computes an integer null vector,
maps it from cycle to seam coordinates, divides by the gcd of all seam
coordinates, and substitutes it exactly into every base row.  The result is
the displayed primitive `g`.

Any integer vector in a one-dimensional rational kernel is an integer multiple
of its primitive generator: Bezout applied to the coordinates of `g` makes
the scalar integral.  Hence the lattice is `Zg`.  In a rank-one lattice every
multiple `ng` with `|n|>1` conformally decomposes, whereas `+g` and `-g` do
not; this proves the Graver assertion.  Finally, (3) fixes every coordinate
where `g_e=0`, and exact reconstruction gives value `1/2` at the eight listed
seams.  QED.

### Corollary 4.2 (support escape)

No Graver augmentation confined to `S` can round this face.  Every integral
solution of either labeled branch in the full catalogue selects at least one
seam outside `S`:

```text
sum_{e notin S} x_e >= 1.                                 (4)
```

This is a support-face obstruction only; it does not exclude an integer point
after outside columns are admitted.

### Theorem 4.3 (exact unconstrained count-105 proximity)

Among all binary vectors `z` on the 507 coordinates with `sum z=105`, the
unique nearest vector to `x*` in `L1` selects the 105 largest exact coordinates.
Their sum is

```text
1338905670549408795 / 21281014839171452
  = 62.9154991276505...
```

and the exact minimum distance is

```text
895600887563593665 / 10640507419585726
  = 84.1690017446990....                                  (5)
```

The 105th and 106th coordinates are respectively

```text
seam 194278: 2352568568789348 / 5320253709792863,
seam  85895: 2233607126073906 / 5320253709792863,
```

with strict gap

```text
118961442715442 / 5320253709792863.
```

### Proof

For binary `z` of cardinality 105 and `sum x*=105`,

```text
||z-x*||_1 = 210 - 2 sum_{e:z_e=1} x*_e.
```

An exchange argument therefore selects the 105 largest coordinates.  The
strict boundary gap proves uniqueness, and exact fraction summation gives
(5).  This ignores balance, service, and capacity, so it is a lower bound on
the distance to any more constrained binary point, not a rounded witness.
QED.

## 5. The compact row-span identity and global 42-column cut

The row-span certificate for seam 95845 has only two nonzero multipliers:

```text
(1/2) * service row for target 56439,
(1/2) * balance row for port 5298.
```

Raw coefficient replay on every seam in `S` is exactly (1).  Define on the
complete catalogue

```text
r_e = 2[e=95845]
      - [56439 in H(e)]
      - [tail(e)=5298] + [head(e)=5298].                  (6)
```

Then `r_e=0` for every `e in S`.  For any balanced integral selection in
either repeat-weight-one/slack-one branch, target 56439 is one of the forced
weight-two targets and has service exactly one.  Summing (6) therefore gives

```text
sum_e r_e x_e = 2 x_95845 - 1,                            (7)
```

which is odd.

Every positive edge of a balanced finite directed selection lies on a
directed cycle, so it is sound to restrict to the slack-at-most-one cyclic
layer.  That layer contains 15,340 seams.  The exact signed census is

```text
r=-2:      1 seam,
r=-1:     38 seams,
r= 0: 15,297 seams,
r=+1:      4 seams.
```

The unique `r=-2` seam is 95839.  The four `r=+1` seams are

```text
81516, 131269, 173135, 207263.
```

The 38 `r=-1` seams are

```text
12124, 56358, 63372, 67162, 67173, 67174, 77656, 81145,
82793, 106693, 118202, 118209, 118220, 123700, 136745,
136762, 153850, 153861, 153885, 160394, 167281, 167287,
167308, 167312, 178694, 178717, 181240, 189617, 190923,
197304, 205060, 205584, 205594, 205605, 206554, 207273,
207494, 211181.
```

Let `O` be the union of the `r=-1` and `r=+1` lists.  Reducing (7) modulo two
proves (2).  Thus the branch master may add either the parity row or its valid
linear consequence

```text
sum_{e in O} x_e >= 1.                                   (8)
```

This is strictly sharper than the generic 507-support no-good: it identifies
only 42 possible odd escape columns among all 15,340 cycle-eligible columns.

## 6. Audit artifacts and resource bounds

The exact basis builder and artifact are:

```text
scratch/exactify_ad_k16_c105_repeat1_basis507_20260730.py
  SHA-256 1a45b2bec73af64d76df8d0fb41aa8e00e1fe2eb4c4645d1461ab39130dea1a0

scratch/ad_k16_c105_repeat1_basis507_exact_20260730.audit.json
  SHA-256 bf772d4515728b9d2ff77684b500687beb1610662b3f721ccad30e908b4468f2
  payload e1b774f2f1ad62c9a52d5a355cf079acc469c054c21786d8a46047b6612e803a
```

The independent full-catalogue escape replay is:

```text
scratch/audit_ad_k16_c105_repeat1_escape_parity_20260730.py
  SHA-256 6f7a86bc098cb8334cbb32abdc784d1007b9780bbb452de155ff61482a0bd553

scratch/ad_k16_c105_repeat1_escape_parity_20260730.audit.json
  SHA-256 9918f1a0c8d9514edb964857083864883cf69db97c83b7dd6cd606d3935fbd1c
  payload 6018202faaa36843d2b92d82bc83c552c72903f9ce3e90eb2286354a592c75c4
```

The exact nearest-binary audit is:

```text
scratch/audit_ad_k16_c105_basis507_exact_l1_20260730.py
  SHA-256 d26203f5f5fa0911ac4a295929d6e630506768aefb00d8400a465f9d4d120378

scratch/ad_k16_c105_basis507_exact_l1_20260730.audit.json
  SHA-256 3a870759354d71340d06579e4efd40d5d43d53c6a9deb03ed92906299d3f7050
  payload 8f6142e6048661cb01f4f3aa0e7d56a9042aba3af06902550b96768aefcfeac9
```

The fraction-free exactification ran on one H100 CPU in 0.93 seconds with
58,028 KiB maximum RSS under a 2 GiB address-space cap.  The independent
full-catalogue parity scan ran on one H100 CPU in 0.82 seconds with 61,772 KiB
maximum RSS under a 512 MiB cap.  No SAT, CP-SAT, CNF emission, or integer
search was run.

## 7. Exact boundary

Proved:

1. the 507-seam GLOP support is an exact full-rank rational basic point;
2. its exact 81-cycle decomposition, determinant, denominators, and values;
3. the aggregate support face has rank-one integer kernel and Graver basis
   `{+g,-g}`;
4. the entire support face is integer-infeasible because eight coordinates
   are frozen at `1/2`;
5. the exact nearest count-105 binary `L1` distance;
6. every full-catalogue integer solution in either labeled branch uses an odd
   number of the explicit 42 escape seams.

Not proved:

1. global infeasibility of either labeled repeat-weight-one branch;
2. any assertion about the separate 622-seam weight-two LP basis;
3. compatibility of an escape seam with port capacity or any omitted physical
   row;
4. a floor 106 theorem or a K16 repaired carrier.

