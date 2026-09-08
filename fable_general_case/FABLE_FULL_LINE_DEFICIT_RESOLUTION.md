# Resolution of the full-line edge-deficit regime: joint charge, sharp frontier, and the minimal missing lemma

## 1. Scope and outcome

This note treats the full-line branch with bottom-threshold edge deficit
`delta >= delta_0 = (sqrt(29)-5)^2/24`. All work is in the subquadratic-defect
branch `D_word = o(a^2)` (the complementary branch is already closed by
Theorem B of `LARGE_DEFECT_DICHOTOMY_NEXT.md`).

Neither Outcome A nor Outcome B is fully reached. What is proved:

1. **Budget saturation identity** (Lemma 3.1): the gap budget
   `int z drho <= delta` is in fact an identity up to the terminal gap.
2. **Cover-gap transfer identity** (Lemma 4.1): the uncovered density equals
   the word mass residing at uncovered points, `D/a^2 = gamma_des + o(1)`.
   The wedge error and the gap correction are charged to the *same* word
   mass; the double charge of the two seals is thereby localized.
3. **Refined seal** (Theorem 5.1):
   `U(1+) <= 15/4 + (5/4)sqrt(6 gamma_des) + 3 gamma_int - (3/2) delta`.
   Corollary 5.2 excludes every full-line process with
   `gamma_des < (1-6delta)^2/150`, for all `delta < 1/6`. At
   `gamma_des = delta` this reproduces `delta_0` exactly; at
   `gamma_des = 0` it excludes the entire range `delta < 1/6`, a 27-fold
   extension.
4. **Level-tension bounds** (Lemma 6.1): unconditional lower bounds
   `tau_A >= sum_d A_d^2/2`, `iota_A >= sum_{d<e}((A_d+A_e-1)_+)^2/2`,
   `A_d <= 1`, against the budget `tau_A + iota_A <= 2f - 3 + delta`.
5. **Bottom-threshold optimality** (Theorem 7.1): both `delta(c)` and
   `gamma_des(c)` are nondecreasing in `c`, so the local joint charge is
   strongest at `c = 1+`; no threshold sweep of the same charge can help.
6. A **scalar dual near-extremizer** (Section 8) satisfying all six audited
   constraint families at the bottom threshold with value exactly
   `15/4 + (5/4)sqrt(6delta) + (3/2)delta`, proving that the missing lemma
   cannot be a rearrangement of the existing families.
7. The **minimal missing lemma** (Lemma M, Section 9), strictly narrower
   than threshold coupling: a desert-occupancy discount with an explicit
   sufficient constant `mu > 75/(8(1-6delta_1))`. The reduction
   Lemma M => full closure below `delta_1` is proved.

## 2. Notation

Fix the bottom threshold `c -> 1+`. `ell = 3 - delta` is selected plateau
edge mass; `f` the selected count; `P, N` selected positive/negative level
counts; `A` absorbed seam mass with level measures `nu_d^A <= Leb[0,1]`,
masses `A_d`, `tau_A = sum_d int t dnu_d^A`,
`iota_A = sum_{d<e} intint 1_{t+u<=1} dnu_d^A dnu_e^A`. `rho` is the seam
measure with marks `(p,s,z)`, `alpha <= rho` the absorbed part,
`C = int_alpha (p+s-1)`. Selected lines `L_a`, uncovered set
`D_a = |H_a \ L_a|`. Word positions are vertex-convention; all conventions
differ by `O(a) = o(a^2)`.

New masses. `gamma_int = int z drho` (internal predecessor-gap mass),
`gamma_term` the terminal/boundary gap mass of a linear word, and

```text
gamma_des = (1/a^2) #{word positions at points of H_a not covered by L_a},
gamma_cov = the internal-gap part of gamma_des.
```

## 3. Budget saturation

### Lemma 3.1 (gap budget is an identity)

For every full-line limiting process at the bottom threshold,

```text
delta = gamma_int + gamma_term + o(1),   hence   int z drho <= delta,
```

and equality `int z drho = delta` holds iff `gamma_term = 0`.

#### Proof

The middle word traverses `3a^2 + O(a)` positions. Selected plateau edges
occupy `ell a^2` of them; every remaining position lies either in some
internal predecessor gap of the bottom tail (counted by `int z drho` after
normalization, by the exact contraction law (2.3) of
`MULTISCALE_DIRECTION_COUPLING_NEXT.md`: at the bottom threshold every
non-plateau position lies in exactly one predecessor gap) or in the one
terminal gap of the linear word. Normalizing by `a^2` gives the identity.
QED.

Thus the hypothesis `int z drho <= delta` of `SMALL_DEFICIT_WEDGE_SEAL.md`
is not an assumption but a theorem, and any slack in it is exactly the
terminal-gap mass, which produces no seam charge (audit 8.3 of
`MULTISCALE_DIRECTION_COUPLING_NEXT.md`).

## 4. The cover-gap transfer identity

### Lemma 4.1 (uncovered density = word mass in the desert)

```text
D_a/a^2 = gamma_des + o(1),   and   gamma_des <= delta.
```

#### Proof

Both bounds refine (2.1) of `SMALL_DEFICIT_WEDGE_SEAL.md`. The middle word
visits every point of `H_a` exactly once (it is a Hamilton path of the
middle layer under the audited encoding). A point of `H_a \ L_a` is visited
by a word position that cannot lie on any selected plateau edge, since
plateau vertex sets lie in `L_a`. Hence uncovered points inject into
non-plateau word positions, giving `D_a/a^2 <= delta + o(1)`, which is
(2.1). Conversely every uncovered point is visited, and the visiting
position is a gap position; counting gives the identity
`D_a/a^2 = gamma_des`, where `gamma_des` is by definition the gap mass
sitting at uncovered points. Since total gap mass is `delta` (Lemma 3.1),
`gamma_des <= delta`. QED.

### Consequence: the two errors charge one mass

The wedge error of `SMALL_DEFICIT_WEDGE_SEAL.md` is driven by `D_a/a^2`,
i.e. by `gamma_des`. The gap correction `3 int z drho` is driven by total
gap mass `delta = gamma_des + (delta - gamma_des)`. The prompt's suspected
double charge is now an exact decomposition: only the sub-mass `gamma_des`
is charged twice (once as missing wedge points, once as gap capacity), and
the complementary mass `delta - gamma_des` consists of gap positions that
lie ON selected lines — positions where a plateau line passes through the
gap. This is the mass the joint inequality of Section 5 discounts.

## 5. The joint weighted wedge-gap inequality

### Theorem 5.1 (joint charge)

For every full-line-realizable limiting ledger with edge deficit `delta`
and desert gap mass `gamma_des`,

```text
U(1+) <= 15/4 + (5/4) sqrt(6 gamma_des) + 3 gamma_int - (3/2) delta
      <= 15/4 + (5/4) sqrt(6 gamma_des) + (3/2) delta.        (5.1)
```

#### Proof

Rerun the wedge argument of `SMALL_DEFICIT_WEDGE_SEAL.md` Section 2 with
`D_a/a^2 = gamma_des + o(1)` (Lemma 4.1) in place of the crude bound
`delta`. Convexity of the slice count gives

```text
P + 2N >= 3 - sqrt(6 gamma_des),   hence
A <= P <= 2f - 3 + eps_d,   eps_d = sqrt(6 gamma_des).       (5.2)
```

The two absorbed-base bounds become

```text
C <= 4f - 6 + 2 eps_d,
C <= A + 2(3 - delta - f) <= 3 - 2 delta + eps_d.            (5.3)
```

The exact gap correction (Lemma 4.1 of `SMALL_DEFICIT_WEDGE_SEAL.md`,
coefficient 3, pointwise sharp) charges only internal gap mass:

```text
U(1+) <= 3 - f + C + 3 gamma_int.                            (5.4)
```

Optimizing (5.3) in `f` at the crossing `f_0 = (9 - 2delta - eps_d)/4`,

```text
U(1+) <= 15/4 + (5/4) eps_d - (3/2) delta + 3 gamma_int,
```

and `gamma_int <= delta` (Lemma 3.1) gives (5.1). QED.

### Corollary 5.2 (extended exclusion frontier)

`U(1+) < 4` holds whenever

```text
(5/4) sqrt(6 gamma_des) < 1/4 - (3/2) delta,
i.e.   gamma_des < (1 - 6 delta)^2 / 150,   delta < 1/6.     (5.5)
```

In particular:

* at the diagonal `gamma_des = delta` (every gap position uncovered),
  (5.5) reads `150 delta < (1-6delta)^2`, whose root is exactly
  `delta_0 = (sqrt(29)-5)^2/24 = 0.0061813...` — the seal's constant is
  recovered as the worst case of the joint charge, confirming consistency;
* at `gamma_des = 0` (all gap positions covered), every deficit
  `delta < 1/6 = 0.1666...` is excluded — a 27-fold extension of the
  closed range along this axis;
* the surviving region is the open set

```text
S = { (delta, gamma_des) : delta >= delta_0 - style boundary,
      (1-6delta)^2/150 <= gamma_des <= delta,  delta < 1/6 } 
    union { delta >= 1/6 },                                    (5.6)
```

  a thin parabolic sliver plus the large-deficit tail.

### Remark 5.3 (why this is the prompt's joint charge)

The double-charged mass identified in Section 4 is `gamma_des`. Inequality
(5.1) charges the wedge error to `gamma_des` alone and rebates the covered
gap mass `delta - gamma_des` from the gap correction at rate 3 against the
moment relief rate 2 in (5.3) (net rebate 3/2 per unit of `delta` after
optimization). No pointwise improvement of the coefficient 3 is used or
needed; the prompt's sharpness warning is respected.

## 6. Level tension in the surviving sliver

In `S`, absorbed mass must be large (else the nonabsorbed saving closes the
value; see the ledger file, row L5). The absorbed successor lines then pay
`tau_A + iota_A` by (4.5) of `ABSORBED_FLOW_COAREA.md`.

### Lemma 6.1 (unconditional level tension)

With `A_d` the absorbed successor mass in direction `d` and
`nu_d^A <= Leb` on `[0,1]` (bottom threshold),

```text
A_d <= 1,
tau_A >= sum_d A_d^2 / 2,                                     (6.1)
iota_A >= sum_{d<e} ((A_d + A_e - 1)_+)^2 / 2,                (6.2)
ell <= 2f - tau_A - iota_A   =>   tau_A + iota_A <= 2f - 3 + delta.
```

#### Proof

(6.1): `nu_d^A <= Leb[0,1]` forces the first moment of a mass-`A_d`
submeasure to be at least that of `Leb[0,A_d]`, namely `A_d^2/2`; also
`A_d <= 1`. (6.2): for directions `d != e`, the pair set
`{t + u <= 1}` receives, under any pair of Lebesgue-dominated measures of
masses `A_d, A_e`, at least the mass of the corner square
`[0,x] x [0,x]` triangle with `x = (A_d + A_e - 1)_+` shifted to the
extremes: pushing both measures upward to `Leb[1-A_d,1] x Leb[1-A_e,1]`
minimizes the pair integral, and that minimum is `((A_d+A_e-1)_+)^2/2` by
direct integration of `1_{t+u<=1}`. The last line is (4.5) of
`ABSORBED_FLOW_COAREA.md` with `ell = 3 - delta`. QED.

### Remark 6.2 (what Lemma 6.1 does and does not close)

If absorption were direction-balanced with `A_d = A/3` and `A -> 3` (the
naive extreme), then `tau_A >= 3/2` and `iota_A >= 3/2` while the budget is
`2f - 3 + delta <= 3 + delta`: tight but not contradictory. The scalar dual
extremizer of Section 8 selects `A = 2f - 3 + eps_d`, `A_d = A/3`, level
measures `Leb[0, A/3]` packed at the bottom — which meets (6.1)-(6.2) with
slack. Level tension alone therefore does not empty `S`; it constrains the
extremizer's line geometry and is used by Lemma M below.

## 7. No threshold sweep of the same charge can help

### Theorem 7.1 (bottom-threshold optimality of the joint charge)

Let `delta(c) = 3 - ell(c)` and `gamma_des(c)` be the deficit and desert
mass of the threshold-`c` selected family. Then both are nondecreasing in
`c`, and the exclusion region (5.5) applied at threshold `c` is contained
in the region applied at `1+` after the audited value shift
`3c - 3 + 2e(c)`; the shift is nonnegative and vanishes at `c = 1+`.

#### Proof

Raising `c` deletes plateaux, so `ell(c)` is nonincreasing: `delta(c)`
nondecreasing. Deleting plateaux deletes lines, so `L_a(c)` shrinks and
`D_a(c)` grows: `gamma_des(c)` nondecreasing (monotone under contraction by
Theorem 2.1 of `MULTISCALE_DIRECTION_COUPLING_NEXT.md`: deleted plateau
positions become gap positions, and a deleted plateau's own line leaves the
cover). The seam identity at threshold `c` carries the additive term `3c`
in place of 3 and the secant term `2e(c) >= 0`, so the sub-four test only
tightens while both error drivers grow. Hence any threshold at which (5.5)
excludes also excludes at the bottom. QED.

This proves the prompt's "integrate one common weight over the actual
contraction lifetimes" cannot succeed with the *present* joint charge as
integrand: the charge is pointwise weakest-binding exactly at `c = 1+`, so
every lifetime-weighted average of it is dominated by its bottom value.
Any successful weighting must use a *different* quantity that improves
under contraction — the absorbed-flow matrices of
`ABSORBED_FLOW_COAREA.md` Section 3 remain the only audited candidate.

## 8. Scalar dual near-extremizer on the frontier

Take any `delta in [delta_0, 1/6)` and set `eps = sqrt(6 delta)`.

**Ledger X(delta).** Bottom threshold only. `f = (9 - 2delta - eps)/4`;
seam marks concentrated near `p = s = 1 + (3 - delta - f)/f` with
`z`-marginal: mass `delta` of gaps placed pointwise as `z = delta/f` per
seam on the double-charge extremal profile `(p,s,z) -> (2,2,1)` direction,
scaled to respect `p + s - 1 <= 2`; absorbed submass `A = 2f - 3 + eps`
split `A_d = A/3`, absorbed levels `nu_d^A = Leb[0, A/3]`; uncovered set a
union of three symmetric wedge triangles of total density `delta`
(`gamma_des = delta`, `gamma_int = delta`, `gamma_term = 0`).

**Checked constraints** (rows L1-L9 of the ledger file): mass and moment
identities, `P + 2N >= 3 - eps` with equality, `A <= P` with equality,
absorption legality `p - 1 <= t <= 2 - s` on the support, the level-tension
inequalities (6.1)-(6.2) with slack, the coarea inequality (5.1) of
`ABSORBED_FLOW_COAREA.md` for every admissible weight (verified in the
ledger by the wedge-triangle line count), and the seam identity value

```text
U_X(1+) = 15/4 + (5/4) eps + (3/2) delta > 4.
```

**What X(delta) is not.** X is a scalar ledger, not a marked word process:
it does not exhibit an actual middle order, and it does not satisfy any
constraint outside the six audited families (none is claimed). Its role is
dual: every inequality among the six families is tight or slack on X
exactly as listed, so no reweighting of those families alone can push the
bound below `15/4 + (5/4)eps + (3/2)delta`. The joint charge of Theorem
5.1 escapes X only through `gamma_des < delta`; X pins `gamma_des = delta`
by putting every gap position in the desert. Hence the exact remaining
question is whether a real word can keep its gap positions off its own
selected lines — which is Lemma M.

## 9. The minimal missing lemma

### Lemma M (desert-occupancy discount) — STATEMENT, NOT PROVED

There exist constants `mu > 0` and `delta_1 in (delta_0, 1/6]` such that
every full-line-realizable limiting process with `delta < delta_1` obeys

```text
U(1+) <= 15/4 + (5/4) sqrt(6 gamma_des) + (3/2) delta - mu (delta - gamma_cov)
```

with `gamma_cov = delta - gamma_des` the covered gap mass — equivalently,
any strengthening of the pair `(5.2)-(5.4)` in which desert gap positions
`gamma_des` themselves produce a seam rebate at linear rate `mu`.

### Theorem 9.1 (reduction: Lemma M closes the regime below delta_1)

If Lemma M holds with `mu >= 75/(8(1 - 6 delta_1))`, then every full-line
process with `delta < delta_1` has `U(1+) < 4`.

#### Proof

Write `g = gamma_des <= delta`. By Lemma M (second form),
`U <= 15/4 + (5/4)sqrt(6g) + (3/2)delta - mu g`. The right side is concave
in `sqrt g`; its maximum over `g >= 0` is at `sqrt(6g*) = 15/(8mu)`, value
`15/4 + (3/2)delta + 75/(32 mu)`. This is `< 4` iff
`75/(32 mu) < 1/4 - (3/2)delta`, i.e. `mu > 75/(8(1 - 6 delta))`, which
holds for all `delta < delta_1` by hypothesis. QED.

### Why Lemma M is minimal and strictly narrower than threshold coupling

1. **Single threshold.** Lemma M is a statement at `c = 1+` only; no
   lifetimes, no contraction, no coupling. Theorem 7.1 shows the present
   charge cannot be improved by sweeping `c`, so a bottom-threshold
   strengthening is the narrowest possible locus.
2. **Sharpness witness.** The dual ledger X(delta) shows the six audited
   families cannot yield any positive `mu` by rearrangement: X satisfies
   all of them with `gamma_des = delta` and value above four. Lemma M is
   exactly the assertion that X's desert configuration is not
   word-realizable at zero cost — the only gap between the audited
   relaxation and the truth in this regime.
3. **Physical content.** A desert gap position is a word position at an
   uncovered point of `H_a`. The word must travel through the desert;
   every desert excursion must enter and leave through covered territory,
   and the excursion boundary edges are threshold runs available to the
   saving functional but not charged by `phi`. Lemma M asserts this
   travel cost is linear in desert mass. It is false for arbitrary scalar
   ledgers (X), so any proof must use the Hamilton-path locality of the
   word — but only through the bottom-threshold desert, not through any
   cross-threshold object.
4. **Explicit target constant.** `mu = 12` suffices for
   `delta_1 = 1/24`: then `75/(8(1-6/24)) = 75/6 = 12.5`; take
   `mu >= 12.5` for `delta_1 = 1/24`, or `mu >= 75/8 = 9.375` for the
   pure frontier `delta_1 -> 0+` (already >= any previously closed range).

## 10. Honest status

* Closed here: all `(delta, gamma_des)` with `gamma_des < (1-6delta)^2/150`,
  `delta < 1/6` — a strict superset of the previous `delta < delta_0`.
* Open: the sliver `S` of (5.6), i.e. processes that place at least
  `(1-6delta)^2/150` of gap mass in their own line desert, and all
  `delta >= 1/6`.
* Outcome A is not claimed: no universal `U(c) < 4` for the sliver.
* Outcome B is not claimed: X(delta) is a dual ledger, not a process.
* The one missing lemma is Lemma M; Theorem 9.1 is the complete reduction.
