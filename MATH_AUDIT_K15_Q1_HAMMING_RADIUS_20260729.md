# Exact `k=15` upper-`q=1` Hamming-radius audit

Date: 2026-07-29

## Result

Let `F_0` be the strict equivariant, degree-two, residence-clean `k=15`
selector in
`scratch/fixtures/k15_residence_hint_explicit_v1.json`.  It misses 67
upper-`q=1` orbit colours.

Every degree-two selector covering all upper-`q=1` colours differs from
`F_0` in at least **68** lower-orbit choices, according to two independent
exact CP-SAT formulations of the sharp radius-67 case.  Connectivity,
voltage, residence, and deeper shadows were omitted, so this is a lower bound
for every valid carrier in the strict quotient catalogue.

The current status is computer-audited rather than a published formal UNSAT
certificate.  A human cut/parity proof or checked CNF proof remains desirable.

## Why 67 is the first possible radius

There are exactly 67 missing upper colours.  One changed lower-orbit choice
can introduce at most one colour.  Therefore any covering selector has
Hamming distance at least 67 from `F_0`.

At distance exactly 67, every changed choice must introduce a different one
of the 67 missing colours.  In particular:

1. no new choice can restore an old colour;
2. an old colour of initial load `ell` can be removed at most `ell-1` times;
3. exactly one action is selected for each missing colour;
4. at most one action is selected at each lower orbit.

These observations make the radius-67 action model complete, not a heuristic
neighbourhood.

## Endpoint-balance formulation

A choice is an edge between two central necklace vertices.  Replacing the
old choice `e_0(L)` at lower orbit `L` by `e(L)` changes the quotient degree
vector by

\[
                 \partial(e-e_0).
\]

Because `F_0` is degree two, the repaired selector is degree two if and only
if the sum of these action vectors is zero at every one of the 429 central
vertices.

The exact Boolean model therefore consists of:

- one variable for every q1-safe action adding a missing colour;
- exactly one action per missing colour;
- at most one action per lower orbit;
- removal capacity `load(c)-1` for every old colour;
- zero total endpoint-degree delta at every central vertex.

No orientation or Hamiltonicity assumption appears.

## Two exhaustive tests

### One-end circulation

Restrict to replacements whose old and new edges share one endpoint.  Such
an action moves one degree unit along a directed arc.  All 67 missing colours
have candidates; there are 828 actions total.  The exact circulation model is
`INFEASIBLE`.

### Complete radius-67 action model

Allow both one-end and two-end replacements.  There are 1646 q1-safe actions.
The complete endpoint-balance model is also `INFEASIBLE`.

Thus the two-end moves are necessary in general (they occur in the relaxed
67-change q1 scaffold), but even their full family cannot close degree at the
sharp radius.

## Reproducers and outputs

- `scratch/audit_k15_q1_circulation_repair.py`
- `scratch/k15_q1_circulation_repair.audit.json`
- `scratch/k15_q1_allactions_r67.audit.json`
- `scratch/audit_k15_degree_upper1_radius.py` (the general exact-radius model)

The radius-68 exact test is the next computation.  If it is feasible, its
selector becomes a much stronger carrier hint; if it is infeasible, the same
argument raises the structural lower bound again.

