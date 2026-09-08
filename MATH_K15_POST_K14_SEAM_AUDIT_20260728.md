# k=15 seam audit after the exact k=14 construction

## Carrier

The audited source is
`scratch/k15_dual_descent_a4_step19.segments.json`.  Its middle factor has:

- 6,435 rank-8 vertices;
- 17 physical cycles;
- zero lower or upper shadow holes at every depth;
- 45 depth-three residence violations, concentrated in two cycles.

The defective cycles have lengths 135 and 45.  Their exact minimum residence
cut systems have sizes 15 and 8:

- the length-135 cycle becomes (9^{15});
- the length-45 cycle becomes (6^7+3).

Thus 23 forced defect cuts plus one variable cut on each of the 15 clean
cycles yield 38 resident pieces.

## Correct carrier/compiler interface

Lower middle shadows are not carrier constraints.  They are variables of the
depth-three lower compiler, exactly as in the k=14 proof.  The splice model
was therefore extended with `--upper-only`, which:

- retains depth-three residence and upper q1/q2 coverage;
- drops lower q1/q2 carrier coverage;
- leaves the lower ideal for the exact Hall/SAT compiler.

The minimum defect cuts themselves preserve all upper shadows.  Their only
native losses are 23 lower-q1 and 16 lower-q2 colours.

## Exact finite results

1. The upper-only necessary provider precheck passes.
2. With all colour constraints removed, the 38-piece resident path model is
   **UNSAT**.  Hence the immediate obstruction is endpoint compatibility,
   not shadow coverage.
3. With upper q1 coverage restored, all three cyclic-translation classes of
   the 45 minimum cut systems on the length-45 defective cycle are **UNSAT**.
4. Full upper q1/q2 is consequently also UNSAT for the minimum segmentation.
5. Splitting the clean length-5,160 carrier at one additional fixed pair was
   tested at 512 calibrated pairs with a fixed anchor; every resulting
   resident path instance was UNSAT.  This is a finite search result for that
   slice, not a general impossibility theorem.

Therefore the current construction does **not** yet attain

\[
B(15)=\binom{15}{8}+3=6438.
\]

## What must change

The k=14 seam lesson survives in sharpened form: cuts must be selected jointly
with the portals they expose.  At k=15 the minimum residence segmentation is
itself incompatible, before colours.  One of the following is necessary:

1. a jointly variable second cut on a clean cycle (not a fixed-pair scan);
2. two or more coordinated extra splits;
3. a local carrier trade that changes the rigid (9^{15}) / (6^7+3)
   endpoint packets while preserving the all-shadow property.

Only after a resident upper-exact path exists should the combined depth-three
Hall audit and compiler be run.

## Code/results

- corrected splice model: `scratch/k15_segment_splice_sat.py`
- minimum segmentation: `scratch/k15_dual_descent_a4_step19.segments.json`
- upper-only full result: `scratch/k15_step19_upperonly.json` (UNSAT)
- relaxed path result: `scratch/k15_step19_path_relaxed.json` (UNSAT)
