# The equivariant source-relative `FRR(7,4)` lane is closed: `60>41`

## 0. The verdict

Let `B_0` be the rank-seven facet derivative of the saved `6390+45`
`k=15` factor.  There is **no** `Z_15`-equivariant rethread of `B_0`
satisfying Theorem 4B.1, at any cut budget.

The obstruction is quantitative and occurs before lower-colour restoration:

\[
\boxed{
 \begin{array}{c}
 \text{cut orbits required to hit every length-three collar}\ge60,\\[2mm]
 \text{four-separated cut orbits supportable by an exact compatible}\
 \text{endpoint matching with the same upper colours}\le41.
 \end{array}}
                                                               \tag{0.1}
\]

Thus the source-relative equivariant endpoint-matching architecture has a
deficit of at least 19 cut orbits.  The 12 forced unique lower-colour orbits
never become the binding constraint.

This does **not** refute nonequivariant `FRR(7,4)`, a rethread not obtained by
cutting and perfectly matching retained source paths, or an unrelated
`RTR(7,4)` factor.

## 1. Why the endpoint catalogue is valid for every budget

Index the large source edge orbits by `h in Z_426`.  The two endpoints made
by cutting `h` are

\[
                  L_h=X_h,\qquad R_h=X_{h+1}.          \tag{1.1}
\]

Hypothesis 2 of Theorem 4B.1 requires every retained path to have at least
four vertices.  On the source cycle this is exactly

\[
             z_h+z_{h+j}\le1
       \qquad(1\le j\le3).                            \tag{1.2}
\]

Under (1.2), the first four inward states at every exposed endpoint are
unchanged by all other cuts.  Hence the capped trace vector

\[
 \big(\tau_x(L_h)\big)_{x\in[15]},\qquad
 \big(\tau_x(R_h)\big)_{x\in[15]}                     \tag{1.3}
\]

is source-fixed.  It does not depend on the cut budget or on the rest of the
cut set.

Therefore one may enumerate once and for all every triple

\[
          (e,f,\delta),\qquad e,f\in\{L_h,R_h:h\in Z_{426}\},
          \quad\delta\in Z_{15},                       \tag{1.4}
\]

whose rotated endpoint facets are Johnson adjacent, have a large-component
upper colour, and satisfy the exact residence compatibility inequalities
(4.8).  The deterministic enumeration contains 2,000 seam orbits.

For cut bits `z_h` and seam bits `y_s`, the equations

\[
 \sum_{s:e\in\partial s}y_s=z_{o(e)}                  \tag{1.5}
\]

for all 852 endpoint types, and

\[
 \sum_{s:u(s)=h}y_s=z_h                               \tag{1.6}
\]

for all 426 upper colours, are exactly the endpoint perfect matching and
upper-rainbow conditions.  They include same-owner seams and re-addition of
an old cut edge whenever that old edge itself passes (4.8).  A seam variable
represents all 15 physical rotations, so (1.5) is also exact at physical
phase level.

The catalogue and the full lower-row extension are independently generated
by

```text
scratch/audit_k15_frr_static_endpoint_exact_cover_20260729.py
scratch/k15_frr_static_endpoint_exact_cover_20260729.audit.json
scratch/k15_frr_static_endpoint_exact_cover_20260729.opb
```

The general exact formulation is proved in
`MATH_THEOREM_K15_FRR_STATIC_ENDPOINT_EXACT_COVER_20260729.md`.

## 2. The lower side: 60 cut orbits are necessary

The 1,425 physical positive runs of length three give 95 quotient closed
collars, each a four-subset of `Z_426`.  Every repair must cut at least one
edge in every collar.

The width-three cyclic DP in

```text
scratch/audit_k15_facet_rail_q1_rethread_frontier_20260729.py
```

proves that the minimum collar transversal is 60.  Re-running the DP with
(1.2) imposed still gives minimum 60.  Thus the retained-path condition does
not raise the minimum, but it does not lower it either:

\[
               |H|\ge60.                              \tag{2.1}
\]

This half is solver-free and keeps a canonical witness.

## 3. The upper side: at most 41 cut orbits can close

Forget the collars and every lower-colour row.  Retain only

* the 2,000 compatible seam orbits;
* cut spacing (1.2);
* endpoint equations (1.5); and
* upper-colour equations (1.6).

Maximizing `sum_h z_h` in this relaxation gives exactly

\[
                   \max\sum_hz_h=41.                  \tag{3.1}
\]

### Lower witness

The selected 41-orbit solution is independently replayed by

```text
scratch/audit_k15_frr_max41_certificate_20260729.py
scratch/k15_frr_max41_certificate_20260729.audit.json
```

with SHA-256 values

```text
c47e4e97fc6724817ea1556d104b2a33eeaf1129d14fde58fb9c50e2fc05b2c0  script
023066803707df4355bd35382c332ca3bdb5d39c4532ae54740f0134c6faa54e  output
```

It consists of 34 compatible old seams and one nontrivial seven-owner packet
on

\[
                 \{32,39,73,90,143,336,373\}.          \tag{3.2}
\]

The audit checks all 852 endpoint equations, all 426 upper equations, and
cyclic spacing four.  It hits only eight of the 95 bad-run collars, so it is
a closure witness, not an `FRR` repair.

### Formal upper certificate

The negation of the upper bound, `sum z_h>=42`, has a direct CNF encoding:

```text
scratch/generate_k15_frr_max41_drat_cnf_20260729.py
scratch/k15_frr_max42_endpoint_spacing_20260729.cnf.audit.json
scratch/k15_frr_max42_endpoint_spacing_20260729.cnf
```

The CNF has

\[
 19457\text{ variables},\qquad91638\text{ clauses},\qquad238155
 \text{ literals}.                                    \tag{3.3}
\]

Its first 2,426 variables are precisely the 426 cut bits and 2,000 seam
bits.  The remaining 17,031 variables implement an exact sequential
`>=42` threshold.  That threshold encoding was exhaustively projected for
all sizes at most four before the large CNF was emitted.

Kissat returned UNSAT (exit code 20) in 0.12 CPU seconds and emitted a DRAT
proof.  `drat-trim` independently returned

```text
s VERIFIED
```

after a 1.287-second backward check.  The proof artifacts are

```text
scratch/k15_frr_max42_endpoint_spacing_20260729.drat
scratch/k15_frr_max42_endpoint_spacing_20260729.kissat.log
scratch/k15_frr_max42_endpoint_spacing_20260729.dratcheck.log
```

with SHA-256 values

```text
651f7e955cda17466b3e5cac50350b47376d50a86a9d3067dc85b76dea6df785  DRAT
15f576f392ab392ebdabefa1424706e59cfb215bbaec68fd9878d6031d1ef8df  Kissat log
79e6a4df2706b243db26f948705df5e363f4f0e69e21165246adb89f19eb73eb  drat-trim log
```

The CNF SHA-256 is

```text
a067eb35fc5b01c9b2f12595309737bbcdf11c2ead824c8b09930fd6eddc66c2
```

so the formal certificate proves the upper half of (3.1) independently of
CP-SAT.  The CP-SAT optimization artifact is retained as
`scratch/diag_max_spaced_closed.json`; its `OPTIMAL` value is 41 and its
selected solution is the independently replayed lower witness above.

## 4. Conclusion

Combining (2.1) and (3.1), every equivariant Theorem-4B.1 repair would have
to satisfy

\[
                    60\le |H|\le41,                   \tag{4.1}
\]

a contradiction.  In particular, adding more than 60 cut orbits cannot
rescue this architecture: the obstruction is a hard endpoint/upper closure
ceiling, not a minimum-budget artefact.

The earlier 60-orbit CP-SAT model correspondingly closes in presolve as
INFEASIBLE in 0.0117 seconds:

```text
scratch/k15_frr_static_endpoint_stage_20260729.json
scratch/k15_frr_static_endpoint_stage_20260729.log
```

with hashes

```text
b842f9721004f297729a255aa21441d1075b14c6a192d4486b0b5ac915d70029  result
4cd30923e91b42023293490d7e84d1be44d49bcb314c7d1adc0986db041c8b5d  log
```

Those solver files are now only a cross-check; the `60>41` conclusion rests
on the solver-free collar DP, the audited 41 witness, and the verified DRAT
upper certificate.

## 5. All-depth and compiler scope

The SAT materializer now replays the exact canonical all-depth convention:

* rank seven: every factor vertex once;
* lower rank `7-q`: intersections of exactly `q+1` consecutive cyclic
  states;
* upper fixed-window rank `7+q`: unions of exactly `q+1` consecutive states;
* upper canonical: from each cyclic start extend until full and record every
  strictly new union once.

On the old `B_0`, both fixed-window sides and the canonical upper side have
zero holes at every rank.  The canonical load-one census is

\[
\begin{array}{c|rrrrrrrr}
r&4&5&6&7&8&9&10&11\\ \hline
\#\{\text{load }1\}&90&900&3630&6435&6435&3675&1095&30.
\end{array}                                           \tag{5.1}
\]

Because the source-relative equivariant repair is impossible, there is no
new factor to replay.  Had a full repair passed and retained zero holes in
this audit, it would have preserved the source-side factor shadows needed by
the complement-double lane.  It still would not alone prove
`nu(16)=12873`: the physical `K=16` carrier, its mixed/deeper shadows, and
the lower compiler would require materialization and independent audit.

The live consequence is architectural: abandon minimum-collar equivariant
rethreading of this fixed `B_0`.  The remaining routes are nonequivariant
source repair, a rethread which changes more than exposed endpoint matching,
or a direct unrelated resident turn-rainbow factor.
