# Audit AD: the two radius-99 max-slack cuts fail cut-only portal rows

Date: 2026-07-29

## 1. Exact scope and frozen inputs

This is a solver-free evaluation of the two dynamic double-capacity witnesses
against the complete family of 1,328 unique-colour portal inequalities.  It
does not invoke CP-SAT and does not use the dynamic capacity variables `y`.

The frozen source factor is
`scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json`, SHA-256
`d1662b09981bbfe3fbd25e46bad045c628407eda9d1c52936ca39c721151a7c8`.
The reconstructed quotient catalogue has digest
`e5ffa02199834c476f45b314b2eacfbaa1866a74895cc0aa4e12744c8d157ff3`.

The two cut witnesses are:

| branch | witness artifact SHA-256 | cut-value SHA-256 |
|---|---|---|
| retain | `92b06f1b6850fd7865cc20e49c9e5280f3231e57ec06eb92b8293f78dc2df606` | `4190aac9363d88fbb327bec88340e1ea9ed9e5dbd517dd12d0b77afaedd27b38` |
| delete | `7be03bb4696679ed270bec70001f09a5b300690a1cf20f7d21147f9272a1bf9a` | `41202dbc0b2932965f996558974c6d0a53980516570b16f2d6601924ac2560dc` |

The portal family reconstructs as 667 lower rows and 661 upper rows, with 20
parallel-provider cases correctly skipped.  Its complete row-key hash is
`5b94a68de77a1a230dd345b8803baf32c633483b18e266cd4c9e4ff8ea546335`.
This equals the family declared by both fixed full-seam models.

## 2. Portal inequality and proof

Let `C` be the set of cut source edges.  Let a q1 colour have unique source
provider `e=uv`, and suppose it has no off-source loopless provider parallel
to `{u,v}`.  Let `Q_e` be the set of nodes outside `{u,v}` occurring on an
off-source provider of that colour, and let

`H_e = {h in source : h has an endpoint in Q_e}`.

Every exact degree-balanced completion covering the colour satisfies

`sum_{h in H_e} cut[h] >= cut[e]`.                                      (P_e)

Indeed, if `cut[e]=0` the inequality is automatic.  If `cut[e]=1`, q1
coverage requires an added replacement provider.  By the nonparallel
hypothesis this added edge has an endpoint `q in Q_e`.  Its positive added
degree at `q`, together with exact degree restoration, forces positive cut
degree at `q`.  Hence at least one source edge of `H_e` is cut.  This is an
integer implication; it uses neither the double-repair relaxation nor its
matching variables.

## 3. Exact evaluation

For the retain witness, 121 portal rows have their unique provider cut: 62
lower and 59 upper.  Seven are violated: six lower and one upper.  For the
delete witness, 119 portal rows are active: 61 lower and 58 upper.  Six are
violated: five lower and one upper.  The corresponding dynamic-capacity
matching/demand/slack triples were `49/24/+25` and `46/22/+24`; these values do
not enter the portal evaluation.

Every listed violation has `cut[e]=1` and `C intersect H_e = empty`, so its
left side is zero and its right side is one.

| branch | palette | colour | sole source provider `e` | `C intersect H_e` |
|---|---|---:|---:|---|
| retain | lower | `(0,995)` | 9215 | empty |
| retain | lower | `(0,1715)` | 3782 | empty |
| retain | lower | `(0,3429)` | 10492 | empty |
| retain | lower | `(1,483)` | 21021 | empty |
| retain | lower | `(1,573)` | 19213 | empty |
| retain | lower | `(1,1369)` | 20402 | empty |
| retain | upper | `(0,3311)` | 3536 | empty |
| delete | lower | `(0,995)` | 9215 | empty |
| delete | lower | `(0,1715)` | 3782 | empty |
| delete | lower | `(0,3253)` | 9539 | empty |
| delete | lower | `(0,3429)` | 10492 | empty |
| delete | lower | `(1,1369)` | 20402 | empty |
| delete | upper | `(1,1907)` | 22511 | empty |

There is a single common one-row certificate for both witnesses.  For lower
colour `(0,995)`, the sole source provider is edge 9215, and

`H_9215 = {1240,1689,1720,1737,1808,1815,2632,5497,5503,5719,5726,9086,18893,18903}`.

Both cuts contain 9215 and contain none of these fourteen support edges.
Thus the same inequality

`cut[1240]+cut[1689]+cut[1720]+cut[1737]+cut[1808]+cut[1815]`
`+cut[2632]+cut[5497]+cut[5503]+cut[5719]+cut[5726]+cut[9086]`
`+cut[18893]+cut[18903] >= cut[9215]`

evaluates to `0 >= 1` for both.

The machine-readable audit records the exact portal-node and full support sets
for all thirteen branch-labelled violations.  The retain violated-row-key hash
is `9bb97e09e002700520c28470eecdd5c35f5fd67aea720a51efc6d59ad4b84cfa`;
the delete hash is
`4557b59810b430edf894b007253603cb334bdf48f2b51dc030098fb854479b03`.

## 4. Consequences and exact caveat

Each fixed full-seam instance is infeasible from the fixed cut equalities and
any one of its violated portal inequalities alone.  Therefore the reported
presolve UNSAT has a solver-free portal-only certificate; degree, explicit q1
rows, motif rows, Pareto rows, and the dynamic double-capacity witness are not
needed once the portal row is present.  Since `(P_e)` is itself a theorem from
exact degree restoration and q1 coverage, the same cuts cannot have a genuine
degree-balanced q1 completion even if the redundant explicit portal rows are
removed from the implementation.

What is not proved from the result JSON is which internal presolve rule CP-SAT
used first.  The mathematical claim is only that the portal contradiction is
already sufficient.  The positive dynamic-capacity slack `+25` and `+24`
therefore has no bearing on feasibility: it belongs to a weaker master that
omitted these cut-only consequences.

Consequently, all 1,328 portal rows must be imposed before reoptimizing the
dynamic cut-capacity master.  Neither old max-slack cut is an admissible hint
for the portal-complete master or for a downstream seam subproblem.

## 5. Reproduction

Run the lightweight, solver-free script
`scratch/audit_ad_maxslack_portal_witnesses_20260729.py`.  It writes
`scratch/ad_maxslack_portal_witnesses_20260729.audit.json` and fails closed on
the source, catalogue, portal-family, witness, fixed-result, branch, and cut
hashes.
