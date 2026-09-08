# k=13 phase-trade Hamiltonian: certificate and compiler audit

## Result

The six translated 3-owner trades at shifts

\[
\{0,1,2,3,6,7\}
\]

turn the thirteen 132-cycles of the zero-voltage `b=11` factor into one
Hamilton cycle on all
\(\binom{13}{7}=1716\) middle masks.  The resulting cycle retains complete
lower and upper shadow coverage at every possible depth \(q=1,\ldots,6\).
It is not, however, resident through depth 3, so neither the canonical nor
the flexible depth-3 compiler can consume it.

This separates two genuinely different finite gates:

1. this certificate has Hamiltonicity and all-depth shadow coverage, but
   fails residence;
2. the previously found resident rotor has perfect depth-3 residence, but
   its flexible compiler has the one-orbit rank-5 MUS represented by 597.

## Materialized certificate

The standalone certificate is
`scratch/k13_b11_phase_hamilton.certificate.json`.  It contains:

- the complete 1716-vertex middle cycle;
- all 1716 selected Johnson edges as explicit
  `(lower, endpoints, upper)` records;
- all 18 changed owners, including their old and new endpoint pairs;
- the six selected translate shifts and provenance paths.

Digests:

| artifact | SHA-256 |
|---|---|
| `scratch/k13_b11_phase_hamilton_cycle.txt` | `72f4e6aa5e752826b3fd4962575cee99de32940ac5bfb034b280bd720e4f19b5` |
| `scratch/k13_b11_phase_hamilton.certificate.json` | `0c6a914868356867bfad79f1f282eef33f353a0e7664044f5f990f201542f46a` |
| `scratch/k13_b11_phase_hamilton_audit.json` | `b45da3a7f6ed8cb9a8fd25d73e9ea390e43bae7d8c4e91151ff516a17a688867` |
| `scratch/k13_b11_phase_hamilton.compiler_audit.json` | `0198ea3aba076d51d5608152406ec5d6ccf523e622e1584fc06cc62825b8aeb5` |

The materializer and independent verifier are respectively
`scratch/materialize_k13_b11_phase_hamilton.py` and
`scratch/verify_k13_b11_phase_hamilton.py`.

## Full shadow audit

For every cyclic window of \(q+1\) middle masks, the lower shadow is its
intersection and the upper shadow is its union.  A window is valid when these
have ranks \(7-q\) and \(7+q\), respectively.

| \(q\) | lower holes | upper holes | invalid lower windows | invalid upper windows |
|---:|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 | 78 |
| 3 | 0 | 0 | 6 | 396 |
| 4 | 0 | 0 | 149 | 1012 |
| 5 | 0 | 0 | 559 | 1389 |
| 6 | 0 | 0 | 1144 | 1683 |

Thus the trades preserve more than the search objective: not only \(q\le3\),
but every lower and upper rank is covered.  The invalid-window counts show
that deep coverage is highly redundant rather than wreath-like.

## Exact residence residue

There are exactly 143 inserted coordinates deleted within the next three
edges:

| residence lag | count |
|---:|---:|
| 2 | 6 |
| 3 | 137 |

Normalizing each local defect by the cyclic coordinate action gives 24 exact
local signatures.  Their multiplicities are:

| signature multiplicity | number of signatures |
|---:|---:|
| 2 | 1 |
| 3 | 1 |
| 4 | 2 |
| 6 | 10 |
| 7 | 10 |

The complete 143 positions, their deletion positions, coordinates, lags,
position-mod-132 histogram, and normalized signatures are recorded in
`scratch/k13_b11_phase_hamilton_audit.json`.

The maximal cyclic depth-3 erosion consists of 1710 rank-4 masks and 6 rank-5
masks.  Its third derivative disagrees with the requested middle cycle at 332
positions; 241 disagreements miss one coordinate and 91 miss two.  Therefore the
residence failure is a necessary structural failure, not a weakness of the
SAT encoding.

## Canonical compiler

Running

```text
python3 scratch/sigma_multirow_compiler.py \
  scratch/k13_b11_phase_hamilton.certificate.json --k 13 --depth 3
```

stops at

```text
middle certificate is not resident through requested depth
```

before constructing the SAT instance.  The canonical core itself has rank
histogram

```text
0:12, 1:310, 2:1079, 3:283, 4:32,
```

but its maximal envelope fails to reconstruct 332 middle positions.

If one ignores that prior structural failure and only counts geometrically
core-compatible windows, every rank at most 4 has a candidate.  At rank 5,
18 masks have no canonical-core window; their cyclic-orbit representatives
are

```text
121, 213, 271, 841.
```

This is a sparse-core obstruction, not the rotor's representative-597
obstruction.

## Flexible compiler and the best cut

All 1716 cyclic cuts were audited.  The minimum number of linear depth-3
reconstruction failures is 326, attained by exactly 13 cuts, at starts

```text
52, 221, 316, 396, 580, 801, 970, 1065, 1234, 1329, 1409, 1504, 1584.
```

The first is materialized as
`scratch/k13_b11_phase_hamilton.best_cut.certificate.json`, SHA-256
`39a142c2b9913945a2b474ad510b7c5239761c55389e596f443b633b6b329375`.
The flexible compiler reports `STRUCTURAL_UNSAT` with 326 failures.

The maximal linear rows at that best cut have the following main-rank
coverage:

| row | dominant rank | distinct at that rank | holes at that rank |
|---:|---:|---:|---:|
| 0 | 4 | 715 | 0 |
| 1 | 5 | 1209 | 78 |
| 2 | 6 | 1479 | 237 |
| 3 | 7 | 1390 | 326 |

These are diagnostics of the maximal envelope, not optimized SAT rows.  At
the more permissive geometric-candidate level, every rank-5 target has at
least 4 and at most 16 flexible windows.  Thus rank 5 does not fail locally;
the flexible compiler is blocked earlier by residence.

## Comparison with the residence-perfect rotor

The resident certificate
`scratch/sigma_sat_k13_compilerrelax_h3_knob819_lns80.certificate.json` has
zero depth-3 residence violations.  Its exact single-target scan finds 98 of
99 cyclic rank-5 orbits satisfiable.  The only exception is the orbit

```text
597, 1194, 1361, 2197, 2388, 2597, 2697,
2722, 4394, 4776, 5194, 5394, 5444.
```

That orbit is an `UNSAT_1_MINIMAL_BY_ORBIT` MUS, even though representative
597 has 8 local candidate windows.

For the new phase-trade Hamiltonian, each of these thirteen masks has exactly
3 canonical-core candidates and 9 flexible best-cut candidates.  It never
reaches the corresponding SAT question because residence has already failed.

The comparison is therefore sharp:

\[
\begin{array}{c|c|c|c}
&\text{Hamilton/all shadows}&\text{depth-3 residence}&\text{rank-5 gate}\\
\hline
\text{phase-trade cycle}&\text{yes}&\text{143 defects}&\text{not reached}\\
\text{resident rotor}&\text{resident seed}&\text{perfect}&\text{orbit 597 UNSAT}
\end{array}
\]

The next search should combine these two properties directly; neither a
different cut nor a more flexible lower compiler can repair the 143
residence defects in this Hamilton cycle.
