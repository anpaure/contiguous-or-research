# Complete reconciliation of Claude's 2026-07-30 ledger

Date: 2026-07-30

## Scope and authentication

The complete 2,371-line ledger was read, not merely its latest tail:

```text
/Users/amir.nuriyev/Downloads/opusproblem/work/LEDGER.md
SHA-256 ae69fc2f037b1d40705500b434597fbc116188406df12c376c2dc01fc5fe5fc6
```

The accompanying synthesis was also read:

```text
/Users/amir.nuriyev/Downloads/opusproblem/work/THEORY_SYNTHESIS_20260730.md
SHA-256 dcd0c4d0899e8610994dd6d5154ee02265cd30f88fb87c0c0e3f6684a60cb6ee
```

This note reconciles those files with the later project state.  It does not
promote a measured pattern to a theorem or a bounded solver run to a verdict.

## 1. Decisive separation of the two current K16 routes

The ledger's raw-splice route and the project's carrier/compiler route are
different search spaces and must remain separate.

* A raw-splice candidate is already a literal word.  A SAT completion of an
  18-cell length-12,873 fibre ends K16 immediately after exhaustive replay.
  Residence, a flat middle carrier, and COMP3 are not prerequisites.
* An exact carrier is only the middle/upper input to a lower compiler.  The
  current `exact_229` carrier is all-upper but has generalized-Hall deficiency
  25.  The shifted-eight near-carrier has one middle bit defect and two
  conditional Hall-gain cells; repairing that bit is not itself a universal
  word.

Consequently the next free H100 CPU was reassigned from the secondary
matching-protected shifted-eight model to the exact seed1/self raw-splice
fibre.  The latter has direct finishing value; the former would still leave a
lower Hall problem even on SAT.

## 2. What today's later results supersede

The ledger treated the seed5/self `4/9/5` RF495 fibre as likely empty but not
closed.  Item 2035 now closes that entire authenticated fixed fibre without
SAT: 21 mandatory rank-eight targets inject into only 20 typed physical
anchors.  This is a source/layout theorem, not a global K16 lower bound.

The restricted-shore `211/212` score of collar 5960 is also superseded as a
production signal.  Final literal replay gives 18 arbitrary-upper holes and
full generalized-Hall deficiency 427.  Every current candidate must pass the
full 26,332-target matching, not a fixed U20 or old-shore score.

The shifted-eight separated-cycle search repaired middle exactness and upper
coverage many times, but the first fourteen full-Hall deficiencies were
45--60.  Thus those candidates confirm, rather than evade, the global
compiler coupling.

## 3. Highest-value direct finite lane from the ledger

The frozen seed1/self `4/9/5` fibre is genuinely unclassified.  Its exact
maximal-provider quotient has:

```text
73 residual targets
70 contiguous free-position classes
6,128 literal semantic rows
5,110 exact same-Q maximal rows
18 nonzero free cells
```

The maximal-core criterion is necessary and sufficient for this frozen
catalogue, and the independent verifier reconstructs all 18 cells and replays
all 65,535 nonzero masks on SAT.  The package is authenticated at

```text
/home/amodo/or15/work/ad_s1s1_495_maxcore_c8fda289_20260730
```

with source SHA
`42383ef4e862763d47090712688806d47fb2bf36e846419df5776a3352985c37`
and atlas SHA
`c8fda28998f9d2b5128bd9360b13e9aaa3858c00ee34af0ac5018af9c37a6bd4`.
It is queued on H100 core 62 after the active shifted-eight census.  SAT would
prove `nu(16)=12873`; a replayed exhaustive UNSAT would close only this
seed1/self `4/9/5` fibre.

The matching-protected shifted-eight CP-SAT model remains staged at

```text
/home/amodo/or15/work/root_k16_shifted8_matchprotected_20260730
```

as a secondary carrier lane.

## 4. Corrected status of the all-odd wedge/SPILL route

The elementary wedge identity is substantive: an absence run of length one
gives the same rank-`r+1` adjacent-union colour on its two flanking edges, so
those flanks avoid the multiplicity-one adjacent-union obstruction.

However, the ledger's stronger kill-shape assertion is **not** a theorem.
`MATH_AUDIT_WEDGE_KILL_SHAPE_COUNTEREXAMPLE_20260730.md` gives an explicit
odd-middle cycle in `J(9,5)` where a rank-`r+3` fragile target has a kernel
containing a wedge flank; the construction suspends to every `J(2r-1,r)`,
`r>=5`.  Consequently neither

```text
every wedge killer is a one-sided rank-(r+2) three-OR
```

nor the resulting two-three-OR `O(nk)` test is valid for unrestricted
Johnson cycles.

The authoritative replacement is
`MATH_THEOREM_R_PROTECTED_WEDGE_RAYS_AND_PRODUCT_SPILL_20260730.md`:

1. under fixed-width all-depth support `(FW)`, a rank-`(r+q)` killer of a
   wedge flank is the unique corresponding outward `q`-ray;
2. one fixed-width target cannot kill both flanks;
3. the exact product-wedge incidence criterion `(PWI)` and its weighted
   `(SPILL)` potential are rigorous;
4. opening `b` components at wedge flanks loses at most
   `b(k-r-1)=O(bk)` old upper targets by the assigned-geodesic injection.

This is useful but does not give zero spill.  The missing all-odd inputs are
now explicitly:

```text
a strict locked-ray/product-dispersion inequality (or a seam absorber for
the O(k) ray list), a jointly admissible opening/seam atlas, and the lower
compiler-Hall theorem.
```

The observed good wedges remain design evidence and may be imposed as an
instance-side condition, but they are not a universal consequence of local
wedge algebra or residence.  Positive-slack COMP_d automaticity is likewise
supported by finite compile censuses, not proved by them.

## 5. Even-K structural lesson retained from the ledger

The h=1 doubled splice is not representative of known even optima.  The
verified `k=8,10,12,14` words are heavily interleaved.  Therefore:

* UNSAT of every fixed 18-cell splice fibre would not prove
  `nu(16)=12874` without an architecture classification;
* SAT in any raw-splice fibre is nevertheless sufficient and should be
  pursued because it finishes immediately;
* the interleaved/equivariant carrier route remains necessary as the
  architecture-diverse alternative.

The ledger's supply-law observation explains why small-even splice failures
do not transfer cleanly to K16: the K15 parents have dramatically more
low-rank letter supply.  Thus K10/K12 calibration is useful but not a K16
no-go.

## 6. Current authoritative status

```text
12873 <= nu(16) <= 12874.
```

There is no verified length-12,873 universal word and no global lower bound
of 12,874.  The direct seed1/self raw-splice decision, the full-matching-
protected shifted-eight repair, and the interleaved carrier search are the
three non-equivalent finite routes.  The all-odd wedge/factor/compiler
implication is the leading general mathematical route.
