# k=15 joint-cut and cycle1/P12 braid search (2026-07-28)

This note records exact SAT results obtained after the step19 PBBS factor was
segmented.  Every UNSAT below is before the depth-three linear compiler; all
models preserve the 6,435 middle masks exactly.

## 1. Joint defect-cut model

`scratch/k15_joint_cut_splice_sat.py` simultaneously chooses:

- in each of the fifteen 9-edge blocks of physical cycle12, either the shared
  central residence cut or one left/right cut pair (all `7^15` choices);
- an arbitrary residence-hitting cut set on physical cycle14 (all 45 edge
  positions are allowed);
- one cut and orientation of every clean cycle;
- an orientation of every resulting segment and a residence-safe directed
  seam path;
- at most two q1-lower colours absent from the seam palette.

The dynamic segment decomposition is encoded rather than enumerated: a
selected pair `(a,b)` means that `a,b` are consecutive selected cuts, and it
implies that no intermediate cut is selected.  Segment orientations and seam
degrees are conditional on these pair variables.

Result: **UNSAT** at q1 lower alone (no upper-shadow clauses and no endpoint
flag clauses), including all cycle14 cut positions.  The largest instance has
13,650 options, 135,030 residence-safe directed seams, 852,640 variables, and
1,794,378 clauses; kissat proves UNSAT in 1.87 seconds.

Thus the entire local two-defect-cycle resegmentation class is closed.  The
earlier fixed minimum-cut obstruction (at least 22 unportalable removed
colours) was not the whole issue: alternative cuts make every colour
individually portalable, but the simultaneous path/colour degree system still
has no h<=2 solution.

## 2. Budget-13 replacement path

`scratch/k15_global_trade_splice_sat.py` replaces cycle12 by the resident
budget-13 path and cuts the 13 native owners of its foreign colours in cycle1.
If the replacement path is kept as one item, all fourteen of its intrinsic
missing q1 colours have **zero** residence-safe seam portals.  Therefore this
fixed-item global trade is immediately UNSAT.  It must braid/resegment cycle1
and P12 rather than splice them as intact items.

## 3. General cycle1/P12 braid

`scratch/k15_cycle1_p12_braid_undirected_sat.py` uses an undirected degree-two
path encoding.  For each vertex,

`degree(v) + endpoint(v) = 2`,

and the number of endpoints is constrained to one or two.  The degree sum has
even parity, hence there are exactly two endpoints and exactly `N-1` selected
edges.  At-most-one selected edge per lower colour then implies automatically
that exactly one of the `N=5295` original cycle1/cycle12 lower colours is
missing.

Upper-q1 coverage is imposed only on the 3,960 masks not supplied by the other
fifteen cycles.  Connectivity is lazy.  Residence can be imposed lazily or by
the exact orientation-invariant clauses

`outside x -- (1,2,or 3 vertices containing x) -- outside x`.

Every selected such path is a forbidden coordinate run of length at most
three; conversely every internal depth-three residence violation has this
form.

### Staged results

- Current cycle1 edges + current P12 edges + all 4,365 cross palette edges,
  upper on, residence off: **SAT**.  After 45 connectivity cuts it gives a
  Hamilton path, one missing lower colour, and no upper-q1 hole:
  `scratch/k15_cycle1_p12_braid_current_u_upper_nor.json`.
- The same catalogue with exact eager residence: **UNSAT**.
- Adding all 420 P12-induced edges: **UNSAT**.
- Also adding all cycle1-induced edges incident to the foreign-owner
  neighbourhood: radius 0 and radius 1 are **UNSAT**; radius 2 is UNKNOWN at
  300 seconds; radius 4 has SAT degree-two selections but connectivity remains
  under search.
- On the phase-aligned P12 seed, adding every cycle1 chord whose union is in
  `rot(3957) union {28330}` is **UNSAT**; additionally inducing P12 is still
  **UNSAT**.

The no-residence Hamilton certificate's sole lower miss does not fit either
endpoint flag.  In contrast, the explicit phase braid
`scratch/k15_phasealigned_braid_5049.json` misses only 25258, and 25258 is a
valid left endpoint flag (it is contained in the first middle mask 26282 and
contains its first deleted coordinate 8192).  That braid's remaining ledger is
exactly 15 periodic residence violations and 16 upper-q1 holes.

## 4. Reproduction files

- `scratch/audit_k15_step19_q1_portal_floor.py`
- `scratch/k15_joint_cut_splice_sat.py`
- `scratch/k15_global_trade_splice_sat.py`
- `scratch/k15_cycle1_p12_braid_sat.py` (older directed formulation)
- `scratch/k15_cycle1_p12_braid_undirected_sat.py` (current formulation)
- `scratch/k15_allcut_portal_census.py`

The authoritative phase replacement is a cycle/path file (`*.cycle.txt`) or
`scratch/k15_cycle12_phasealigned_3413.json`; an older dotted-prefix command
overwrote one budget-13 JSON report, so its `.cycle.txt` is authoritative.
