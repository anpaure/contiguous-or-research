# Exact bi-residence CNF in the fixed-`M0` `k=15` factor fibre

Date: 2026-07-29  
Lane: H  
Status: exact finite reduction proved and independently audited; H100 CPU
search in progress.  No SAT or UNSAT verdict is asserted in this note.

## 1. Setup

Let

\[
 \mathcal L=\binom{[15]}7,
 \qquad
 \mathcal V=\binom{[15]}8,
\]

and fix the equivariant perfect matching

\[
 M_0:\mathcal L\longrightarrow\mathcal V
\]

stored in

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/seed0.mapping.json.
```

Choose a second equivariant perfect matching `P` in the same incidence
graph, with no physical edge common to `M0`, and put

\[
 \tau=M_0^{-1}P.
\]

On a physical cycle of `tau`, write

\[
 L_{i+1}=\tau(L_i),
 \qquad
 T_{i+1}=M_0(L_{i+1})=L_i\cup L_{i+1}.
\tag{1.1}
\]

For the directed lower arc `e_i=(L_i,L_(i+1))`, put

\[
 \delta_i=L_i\setminus L_{i+1},
 \qquad
 \iota_i=L_{i+1}\setminus L_i.
\tag{1.2}
\]

On the rank-exact face both are singleton coordinates.  The desired
**bi-residence** condition is that, on every cyclic physical component and
for every coordinate, every nonconstant one-run and every nonconstant
zero-run in `(T_i)` has length at least four.  Constant traces have the
component length.  The simultaneous clauses below already exclude every
nonconstant component of length below four.

## 2. Exact dual run theorem

### Theorem 2.1

On the non-common-edge face, the carrier `(T_i)` is bi-resident if and only
if, cyclically for every `i`,

\[
 \boxed{
 \iota_i\ne\delta_{i+1},\quad
 \iota_i\ne\delta_{i+2},\quad
 \delta_i\ne\iota_{i+2},\quad
 \delta_i\ne\iota_{i+3},\quad
 \delta_i\ne\iota_{i+4}.}
\tag{2.1}
\]

#### Proof

For one coordinate, let `b_i=1[x in L_i]` and `t_i=1[x in T_i]`.
Equation (1.1) gives

\[
 t_{i+1}=b_i\vee b_{i+1}.
\tag{2.2}
\]

A lower zero-gap of length one would have trace `101`.  At its central
lower state the deleted and immediately reinserted coordinate is the unique
coordinate completing that state under both matchings, so `P=M0` there,
contrary to the face assumption.  Hence lower one-runs cannot coalesce under
the dilation (2.2).

A lower one-run of length `ell` therefore becomes a carrier one-run of
length `ell+1`.  The forbidden lower lengths one and two are exactly

\[
 \iota_i=\delta_{i+1}
 \quad\hbox{or}\quad
 \iota_i=\delta_{i+2}.
\]

A lower zero-gap has length `g>=2` and becomes a carrier zero-run of length
`g-1`.  The forbidden carrier lengths one, two and three are therefore the
lower gaps `g=2,3,4`, exactly

\[
 \delta_i=\iota_{i+2},\quad
 \delta_i=\iota_{i+3},\quad
 \delta_i=\iota_{i+4}.
\]

These implications are reversible by reading the two boundary events of
each run.  This proves (2.1).  If a physical component had length below four
and were nonconstant, some coordinate would have a nonconstant positive run
shorter than four and would violate the first two conditions.  Thus treating
a constant-zero trace vacuously in the dual enumerator does not admit a
false bi-resident model after the positive clauses are imposed.  ∎

## 3. Exact quotient CNF

There is one Boolean variable `x_e` for each retained equivariant orbit of
second-matching incidences.  Perfect-matching equations impose exactly one
selected variable at every lower and middle quotient vertex.

For every compatible physical selected path `e_i,...,e_(i+s)`, append the
negative clause

\[
 \bigvee_{j=0}^{s}\neg x_{e_{i+j}}
\tag{3.1}
\]

when its endpoint labels realize one of the equalities in (2.1).  Repeated
quotient variables on the path are collapsed.  Paths using inconsistent
choices at a lower or middle quotient vertex are discarded.  Thus:

- positive-run clauses have physical arity two and three;
- zero-run clauses have physical arity three, four and five;
- after quotient collapse, the actual widths can be smaller.

Every clause is sound because selecting all its variables selects that
entire physical path.  Conversely every short physical run supplies its
boundary path and hence one clause.  Subsumption among all-negative clauses
is exact.

For the frozen seed-0 matching the independent counts are

```text
retained matching variables              2999
base upper-q1/lower-q2 clauses           19498
positive-residence clauses               20943
  widths                            2:2995, 3:17948
zero-residence clauses                  761235
  widths          2:7, 3:20353, 4:124646, 5:616229
complete bi-resident core clauses       801676
```

The corrected core DIMACS on H100 is

```text
/dev/shm/laneH_k16_sixpiece_20260729/seed0.biresident.cnf
```

with SHA-256

```text
4f4974700f7f9621831a71207889d23d3c31de50249454b4a041b83613599238.
```

The earlier files named `*.dualresident.cnf` contained only the zero-run
clauses.  They are valid relaxations but are not bi-residence models.

## 4. The four quotient-parallel incidences do not weaken the test

The stable mapping omits four non-`M0` incidences whose upper quotient
vertex equals that of the corresponding `M0` edge.  Selecting any one of
them closes an autonomous physical component.  Direct equivariant
reconstruction gives:

| lower orbit / added coordinate | forced carrier cycle | length | minimum one-run | minimum zero-run |
|---|---|---:|---:|---:|
| `315 / 12` | `7271,7395,3303` | 3 | 2 | 1 |
| `384 / 8` | `4973,7017,23369,23117,21101` | 5 | 3 | 2 |
| `406 / 11` | `6989,6765,23145,21353,21325` | 5 | 3 | 2 |
| `416 / 14` | `21685,22181,5813` | 3 | 2 | 1 |

Each is incompatible with bi-residence before any shadow condition is used.
Consequently their omission is equivalent, for this decision problem, to
four proved unit clauses.  UNSAT of the 2,999-variable model therefore
excludes the full non-`M0` seed-0 matching fibre, not merely an unexplained
subface.

## 5. Why the `q<=3` geodesic rows are exact under bi-residence

### Theorem 5.1

Assume `(T_i)` is bi-resident.  For `q=1,2,3`, a rank-`8+q` target is the
union of some contiguous interval if and only if it is the union of `q+1`
consecutive carrier states.  Dually, a rank-`8-q` target is the intersection
of some contiguous interval if and only if it is the intersection of `q+1`
consecutive carrier states.

#### Proof

In at most three consecutive transitions, no inserted coordinate can have
appeared earlier: such a return would create a zero-gap shorter than four.
Hence the union of any `q+1` consecutive states has rank exactly `8+q`.
If a longer interval has union `Y` of that same rank, its initial `q+1`
subwindow already has rank `8+q` and is contained in `Y`, hence equals `Y`.

Dually, in at most three transitions no newly present coordinate can be
deleted and no original coordinate can be deleted twice.  Otherwise a
one-run shorter than four occurs.  Thus every `q+1` subwindow has
intersection rank exactly `8-q`.  If a longer interval has intersection
`S` of that rank, its initial `q+1` intersection has rank `8-q` and contains
`S`, hence equals `S`.  ∎

Therefore the existing minimum-geodesic witness extension for upper `q2`,
upper `q3`, and lower `q3` is necessary as well as sufficient after the two
run theories are imposed.  The corrected protected DIMACS is

```text
/dev/shm/laneH_k16_sixpiece_20260729/u2u3l3.biresident.cnf
```

with

```text
variables     1072002
clauses       4952989
SHA-256       e7ad59ba08729a5e9af98e37807b7d8a3b0040468e9bc7697ec1d14736c69d2b.
```

It protects all lower and upper ranks through distance three.  It does not
encode upper distances four through seven.  Hence:

- `UNSAT` excludes every all-depth bi-resident factor in this fixed fibre;
- `SAT` proves only the protected `q<=3` statement until an independent
  physical all-depth replay passes.

For calibration, the retained all-depth resident factor
`u2u3l3_s801.engine.json` violates the new dual theory in exactly 127
quotient clauses.  Physically it has 2,040 short zero-runs:

```text
length 1: 330
length 2: 585
length 3: 1125.
```

Thus the dual condition is not inherited from the known all-depth factor.

## 6. Fail-closed SAT/UNSAT protocol

A SAT output is accepted only after all of the following are independently
reconstructed from the first 2,999 model variables:

1. the exact equivariant perfect matching and all physical components;
2. every cyclic one-run and zero-run, including constant traces;
3. complete upper-`q1` and lower-`q2` coverage;
4. complete bilateral physical shadow coverage at every required depth;
5. the explicit 429-row factor and hashes of every input.

An UNSAT transcript alone is not a certificate.  The proof-grade route is:

1. rerun the frozen DIMACS with a Kissat proof file;
2. verify the proof independently with `drat-trim`;
3. retain the DIMACS, proof, verification log, builder hashes, mapping hash,
   and the four forced-cycle unit consequences of Section 4.

No connectivity claim is needed for this factor test.  Complement-doubling
and the segmented-ladder splice remain separate consumers of a positive
factor.

## 7. Exact terminal status of the retained searches

Neither retained search decided the fixed fibre.

First, the eager 801,676-clause core was translated literally to CP-SAT and
seeded by the known all-depth resident model.  It terminated `UNKNOWN` after
1,801.60 solver seconds, with 16,306,046 branches and 6,197,594 conflicts.
This is a search transcript, not evidence of infeasibility.  The preserved
files are

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/seed0.biresident.cpsat.report.json
SHA-256 61e95b08f2f471a9a4963f92189c379125ad918cbd96c5ce088218617df265bc

scratch/k15_fixed_matching_pbbs_resident_20260729/seed0.biresident.cpsat.out
SHA-256 660c9342751f1d0cfadb62a1ea0edc609409289986cfa663a32eefe7b598c403
```

Second, the exact lazy zero-gap CEGAR resumed from a 46,610-clause frozen
formula and appended 52,296 further catalogue clauses.  Its last frozen
formula therefore has 2,999 variables and 98,906 clauses.  The round-494
SAT assignment violated exactly 71 further minimal zero-gap clauses; after
adding those clauses, the round-495 Kissat call reached its 600-second cap.
The driver consequently terminated `UNKNOWN`, after 496 recorded rounds and
10,279.46 elapsed seconds.  It did not reach the scripted 500-round limit.

The preserved exact checkpoint is

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/seed0.biresident.cegar.result.json
SHA-256 3598b0b3a878ab495a1c2860712145bcab654ff739199ae7b3980fe02183e7a7

scratch/k15_fixed_matching_pbbs_resident_20260729/seed0.biresident.cegar.round495.cnf
SHA-256 9867d66d4a5377d580a824cfe05b0b8e69c215fc12c89036f89736b156cf0c19

scratch/k15_fixed_matching_pbbs_resident_20260729/seed0.biresident.cegar.round495.kissat.out
SHA-256 fb76b39e924d2946ea420522cb5a1719877a6d9360ff7a0f5f90d8633828e9f2
```

Thus the proved boundary is exact: the CNF/CEGAR formulation is sound and
the checkpoint is reproducible, but there is presently neither a
bi-resident factor nor a proof-certified no-go for this fixed matching
fibre.
