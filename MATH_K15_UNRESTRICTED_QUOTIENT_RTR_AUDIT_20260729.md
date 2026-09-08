# Odd turn selector in the cyclic quotient: RTR audit and K15 launch

Date: 2026-07-29  
Status: exact quotient model implemented and small cases audited; capped K15
lane running on H100 CPU.

## 0. Scope

For odd `n=2r+1`, choose exactly one Johnson edge from every rank-`r+1`
upper set.  The selected edges must form a degree-two factor on rank `r`,
cover every rank-`r-1` turn colour, and have all positive and negative
coordinate runs (and all components) of length at least `s`.

The implementation restricts to factors invariant under cyclic rotation.
This is much broader than the now-refuted source-relative FRR lane, but it
is not an unrestricted nonequivariant RTR theorem.

The cyclic action is free on ranks `r` and `r+1`: a stabilizer order dividing
`n` would force it to divide the rank difference `2r-n=-1` or
`2(r+1)-n=1`.  Therefore one quotient choice has exactly `n` physical
rotates and materializes without phase ambiguity.

## 1. Exact quotient model

For every rank-`r+1` necklace representative `U`, choose one of its
`C(r+1,2)` facet-pair edge orbits.  The model enforces:

1. exactly one pair choice per upper orbit;
2. exact physical degree two on every rank-`r` vertex, after quotient-
   identical rows are deduplicated.  A quotient loop contributes coefficient
   two and is retained correctly;
3. physical coverage of every rank-`r-1` lower colour.  Shorter exceptional
   lower orbits are built physically before OR-row deduplication;
4. every length-one `1`-run and `0`-run exclusion;
5. longer short runs and short components by universal physical path CEGAR
   clauses.

A CEGAR path cut is expanded under every unit multiplier of `Z_n`.  Rotation
is already absorbed into one quotient variable.  Every SAT assignment is
rebuilt as a literal physical edge set before cuts are accepted.

On a residence-clean factor the materializer also runs the canonical
all-depth compiler audit: fixed consecutive intersections below rank `r`,
and every strictly new cumulative union above it.  A q1-perfect bi-resident
factor with deeper holes is retained under a distinct nonfinal status.

## 2. K15 size

For `n=15`, `r=7`, `s=4`:

| item | count |
|---|---:|
| upper necklace orbits | 429 |
| pair choices per orbit | 28 |
| primary variables | 12,012 |
| total CNF variables | 112,398 |
| clauses before CEGAR | 294,629 |
| literals before CEGAR | 1,907,763 |
| degree rows | 429 |
| lower rows | 335 |
| lower orbit sizes | `15^333 5^2` |
| static one-run/gap rows | 6,435 |

This is safely below the 16 GiB launch threshold and roughly fifteen times
smaller in primary variables than the 180,180-variable physical fallback.

## 3. Small-case validation

### n=7, residence 3

The quotient CNF has 30 primary variables and is UNSAT after 39 sound cuts.
An independent exhaustive enumeration of all `6^5=7,776` quotient choices
finds 234 static q1 factors and zero positive-resident factors.  Thus this
is a genuine empty equivariant class, not an encoder failure.  The existing
physical nonequivariant n=7 PASS remains the decoder regression.

### n=9, residence 3

The quotient CNF has 140 primary variables.  After 40 rounds and 1,176
sound affine cuts it first finds a q1-perfect factor with no short positive
or negative run, but three upper rank-six holes.  Continuing while blocking
only each exact all-depth-incomplete factor reaches a literal all-depth PASS
after 3,639 accumulated cuts.  Its physical component lengths are
`99+18+9`, and every rank has zero holes.  This validates the quotient
degree/lower weights, exceptional rank-three orbit, materialization,
residence cuts, and final all-depth replay end to end.

## 4. K15 live lane

The K15 lane runs on one low-priority H100 CPU core with a 4 GiB address-
space cap and a six-hour outer timeout.  Its first two base candidates were
found in 13.2 and 6.7 seconds.  They had about 3,500 physical short-run
violations each, collapsing under rotation and unit multipliers to about
1,750 fresh sound clauses per round.

Paths:

* implementation:
  `scratch/solve_odd_turn_selector_quotient_cegar_20260729.py`;
* H100 work directory: `/dev/shm/k15_frr_h60/qrtr15`;
* append-only ledger: `/dev/shm/k15_frr_h60/qrtr15/rounds.jsonl`.

A resource limit or timed-out round is `UNKNOWN`, never UNSAT.  SAT at the
q1/bi-residence level is not called final until the physical all-depth audit
also has zero holes.
