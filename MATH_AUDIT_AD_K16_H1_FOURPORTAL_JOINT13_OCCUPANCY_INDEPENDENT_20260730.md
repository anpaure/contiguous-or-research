# Independent audit: K16 H1 joint13 occupancy CNF

Date: 2026-07-30  
Auditor: lane AD geometry sublane  
Verdict: **PASS for exact ordered encoding and stated support scope; UNSOLVED/UNKNOWN**

## Audited objects

```text
scratch/ad_k16_h1_fourportal_joint13_occupancy_20260730/model.cnf
SHA-256 251229383ec319a744fea37bd2f3f89bdf59e638727677166f0eaa7751ecd9bb

scratch/ad_k16_h1_fourportal_joint13_occupancy_20260730/model.map.json
SHA-256 f624e5684fe58c122d43371c16fbd4e1c8db9b9ae8a84930d3b9cf59a4758f31
payload SHA-256 4f163a37546364532807ef1767b33e3706e921587099d841954d262fe9974e08

scratch/build_ad_k16_h1_fourportal_joint13_occupancy_20260730.py
SHA-256 c3f7946a6fffd919c17fa0b7a059d651e0cd2a8102417cb1a0e0ab4aa4d2f2a9
```

I did not execute or import the builder and did not invoke a SAT solver.  The
independent audit starts from the separately frozen source-geometry ledger

```text
scratch/ad_k16_h1_four_portal_geometry_20260730.audit.json
SHA-256 3263ab64f540e5552f810f2dbf919d6b18da89310162ff8746c0f099e9b4a9d0.
```

## Independent reconstruction

The reconstruction confirms:

* the thirteen physical positions
  `[0,1]`, `[4486,4489]`, `[6438,6440]`, `[12869,12872]`;
* the exact 55 residual targets and their common coordinate 6;
* 29 one-block interval signatures per target, hence 1,595 signatures;
* the 1,130-variable allocation:
  715 occupancies, 220 block controls, and 195 noncommon-coordinate
  availability bits;
* every chart need from the independently maximal fixed context, matching all
  1,595 ordered map rows.

For each target, the occupancy ALO plus occupancy-to-control rows and the four
control AMO rows force use of one block.  The start-pair clauses forbid two
distinct `0->1` starts within that block, so the nonempty occupancy set is
exactly one interval.  Conversely every one-block interval satisfies those
rows.

For cell `i` and noncommon coordinate `q`, the forward omission rows and one
reverse row give exactly

```text
a[i,q] = 1  iff every selected target using i contains q.
```

Every residual target contains coordinate 6, so the omitted coordinate is
always present and the canonical intersection at every cell is nonzero.

Under the one-run constraints, the endpoint/exterior-neighbour signature in
each durable clause is false in all its guard literals exactly for its named
interval and for no other interval.  The remaining availability disjunction
therefore enforces precisely each noncommon bit of the independently rebuilt
need.  A needed common bit is automatic on a nonempty selected interval.

The independent clause generator matched the DIMACS rows **in order**, not
just as a multiset.  The final exact dimensions are

```text
variables  1130
clauses   17558
literals  67482
```

with clause-family census

```text
target ALO                 55
occupancy-to-control      715
control AMO               330
run-start AMO             385
omission forward         5577
availability reverse      195
durable                  10301
```

## Theorem-scope audit

The encoded equivalence is valid for arbitrary nonzero substitutions on the
named thirteen cells because there is no change-cardinality budget.  Choosing
one actual witness per residual target is WLOG, and canonical expansion to
selected-target intersections preserves those witnesses.  Every other target
retains a fixed-only witness.

The model does **not** establish that a global length-12,873 solution can be
moved into this support.  It does not force a portal to use one of the 153
minimum-debt values.  It is not a fixed-radius model.  The parent theorem and
map state these boundaries correctly.

No satisfying assignment, UNSAT proof, or solver transcript was produced.
The disposition remains `UNSOLVED_UNKNOWN`, and the global K16 bracket is
unchanged.

## Reproducible independent audit

```text
scratch/audit_ad_k16_h1_fourportal_joint13_occupancy_independent_20260730.py
SHA-256 314f1741dfffad7fa5ea98ae797b5ca03385442967ddcc1694fc25cb603e7b6f

scratch/ad_k16_h1_fourportal_joint13_occupancy_20260730/model.independent_audit.json
SHA-256 5605a1a32e7c0f1b588579d82fc81cc7dbe2892878971321bebcb405fc9843f1
payload SHA-256 59847d9bdeccfb5c4618c714e12226da4884d3622cd23f4c2eeb293e7804afea
```
