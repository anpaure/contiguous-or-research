# K16 compound short-cycle q1 no-go (2026-07-30)

## Authenticated scope

Source factor:

- `scratch/k16_asymmetric_triangle_orbit_repair_20260729.json`
- SHA-256 `6044bd63b7281c358c6c33399ccf2dd15143f783535cb6fe6b85a797c04affdc`

Candidate catalogue:

- `scratch/k16_asymmetric_signed_compound_cycle_catalogue_20260730.json`
- 1,263 individually deep-safe, gainful rethread cycles of lengths 3--5
  (95 of length 3, 180 of length 4, 988 of length 5).

## Result

No nonempty subset of the 1,263 candidates preserves both q1 shadows.
This remains true after dropping all structural constraints (transition
disjointness and mutual cut separation) and all deep-shadow constraints.
Consequently, compound selection from this complete short-cycle catalogue
cannot repair the source factor.

This is stronger than the exact pair census: the obstruction applies to
subsets of arbitrary cardinality within the catalogue.

## Solver-free certificate

For a q1 target of source multiplicity one, a legal selected family must have
nonnegative total signed delta at that target.  If, among the candidates not
already ruled out, a unit-load target has losses but no gains, every losing
candidate is impossible.

Applying this implication in parallel gives an empty core in two rounds:

| round | candidates killed | candidates left |
|---:|---:|---:|
| 1 | 1,235 | 28 |
| 2 | 28 | 0 |

The first round uses 451 lower-q1 and 784 upper-q1 chosen witnesses.  The
second uses 14 of each.  Every candidate has an explicit unit-load target
witness in the audit JSON.

Verifier and certificate:

- `scratch/audit_k16_asymmetric_compound_q1_peeling_20260730.py`
- `scratch/k16_asymmetric_compound_q1_peeling_20260730.audit.json`
- audit SHA-256
  `d0ff8ab28b4b64e1051f40de9421d18a62d772430f07444d769babf028628f0e`

## Independent exact optimization cross-check

An independent CP-SAT relaxation maximizes the number of selected candidates
subject only to exact signed lower-q1 and upper-q1 load rows.  It has 1,263
binary variables, 6,344 signed rows, no structural constraints, and no deep
constraints.  The certified optimum is zero (`OPTIMAL`, 0.011 seconds on the
H100 CPU host).

- `scratch/audit_k16_asymmetric_compound_q1_global_20260730.py`
- `scratch/k16_asymmetric_compound_q1_global_20260730.audit.json`
- audit SHA-256
  `a4a0426a9902ce3fb2e48761a6e4598818a9a3f99325fd0f4f32393766aebcbe`

The exact-cardinality model also independently returns infeasible for every
tested cardinality 2 through 12; the global optimum-zero result subsumes those
runs.

## Boundary of the result

This closes compound repair only inside the authenticated length-3--5
catalogue whose members are individually deep-safe and gainful.  It does not
rule out:

- longer rethread cycles;
- cycles that temporarily lose deep coverage but compensate jointly;
- cycles that are individually non-gainful but useful in a compound move;
- rebuilding the carrier outside this source-relative rethread family.

The mathematical lesson is nevertheless sharp: q1 failure is not a pairwise
or small-cardinality phenomenon here.  Unit-load q1 rows form a two-round
dependency closure that kills the entire short-cycle move family.
