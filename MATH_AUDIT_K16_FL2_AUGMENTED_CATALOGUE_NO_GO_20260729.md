# K16 FL2 augmented-catalogue exact no-go

## Result

Let `Q` be the current both-q1-perfect FL2 factor

```text
scratch/k16_q1_endpoint_resume1_failedlit2_20260729.json
SHA-256 276a5eb2e48e5fb25c34ed10ec5d162519b8334ff55259733d638b420eb7115d
```

and let `R` be the fixed resident PBBS factor.  Form the physical Johnson-edge
catalogue `C` from

1. every edge of `Q`;
2. every edge of `R`; and
3. every changed edge named by the radius-two/three packet reports for the
   removed FL3 core and both surviving FL2 cores.

The resulting catalogue has `25,530` edges.  There is **no** subset
`F subset C` satisfying all four conditions

1. every middle vertex has degree two in `F`;
2. every lower q1 colour occurs on an edge of `F`;
3. every upper q1 colour occurs on an edge of `F`;
4. for every one of the `2,221` short runs of `Q`, at least one edge in its
   closed run boundary is absent from `F`.

CP-SAT returned `INFEASIBLE` in the first solve, before dynamic CEGAR, in
`1.62` seconds and under `200 MB` RSS.

Condition 4 is necessary for a resident final factor: if every edge in the
closed boundary of a short coordinate run of `Q` survives, that same run
survives in the final 2-factor.  Consequently the no-go covers every
composition of the enumerated radius-two/three packet edges, not merely the
`17 x 20` pairwise-disjoint compositions currently being enumerated.

This result does **not** exclude a radius-four packet, an edge outside the
finite catalogue, a change of resident parent, or an unrestricted optimal
word.  The CP-SAT infeasibility currently has no retained independent proof
log; extraction of a small solver-free/Farkas core is assigned separately.

## Exact encoding

The model uses one Boolean `x_e` per `e in C`.

```text
sum_{e incident to v} x_e = 2                       for every middle v
sum_{e: lower(e)=L} x_e >= 1                        for every lower q1 L
sum_{e: upper(e)=U} x_e >= 1                        for every upper q1 U
sum_{e in closure(M)} (1-x_e) >= 1                  for every initial motif M
```

The first family makes the selected graph a spanning 2-factor and fixes its
edge count automatically.  The next two families are literal physical
palette coverage, not quotient counts.  The last family is the necessary
closed-boundary residence condition above.  No connectivity constraint is
used.

The reusable solver additionally audits each feasible 2-factor literally and
adds the same sound closure row for every newly created short run.  No such
round was reached in this instance.

## Frozen artifacts

```text
scratch/solve_k16_q1_augmented_catalogue_residence_cegar_20260729.py
SHA-256 a92e7ca4e6a3e53681791aa9d544fa19516f578a4d662ca8bae84db0dc1d7745

scratch/k16_fl2_augmented_allr23_cegar_20260729.json
SHA-256 b310551d3e349763e754e20fe21139cc867cda73339a26afaf49b93f7382aaf4

scratch/k16_fl2_augmented_allr23_cegar_20260729.resource.txt
SHA-256 8476c907cd1001d62800e8e29eed0aa57ed3fe122dcf3d15c2092d0f6468186e
```

The three packet-report hashes are stored inside the result JSON.  The solver
is H100-only outside `--build-only`, validates every input provenance hash,
and labels `INFEASIBLE` only for the supplied finite catalogue.
