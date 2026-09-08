# Exact certificate: the `k=15` joint scaffold is 61 choices from degree two

Date: 2026-07-29

## Certified result

Let `S_0` be the explicit selector

`scratch/fixtures/k15_joint_q1_q3_scaffold_hint_v1.json`.

It chooses one strict quotient-catalogue edge at every one of the 429 lower
orbits.  Among all selectors obtained by changing its choice at some lower
orbits, the minimum number of changes required to make every central quotient
vertex have degree two is exactly

\[
                               \boxed{61}.
\]

The lower bound holds for the continuous relaxation, not merely for Boolean
selectors.  Therefore the entire Hamming ball of radius at most 60 is
infeasible.  No exact-shell monotonicity argument and no collection of
separate radius-40 through radius-60 solver statuses is needed.

An explicit selector at distance 61 attains the bound.  Hence this is an exact
projection distance, not just a lower bound.

This statement concerns **degree two only**.  The attaining selector is not a
valid final carrier: it is disconnected, violates residence, and loses upper
shadows.

## Initial imbalance

Including the four zero-degree vertices omitted by an ordinary `Counter`
histogram, the scaffold degrees are

| degree | number of quotient vertices |
|---:|---:|
| 0 | 4 |
| 1 | 71 |
| 2 | 283 |
| 3 | 64 |
| 4 | 6 |
| 5 | 1 |

The total absolute degree discrepancy is 158, giving the elementary bound
`ceil(158/4)=40`.  The exact certificate below accounts for the extra 21
changes forced by the catalogue incidence geometry.

## Continuous projection LP

There are 11,569 possible replacement actions.  For action `a`, let

- `L(a)` be its lower orbit;
- `delta_a(v)` be its endpoint-degree change at central orbit vertex `v`;
- `x_a` be its selection variable.

The continuous relaxation is

\[
\begin{aligned}
\min\quad &\sum_a x_a,\\
\text{subject to}\quad
&\sum_{a:L(a)=L}x_a\le 1 &&\text{for every lower orbit }L,\\
&\sum_a\delta_a(v)x_a=2-d_0(v) &&\text{for every central vertex }v,\\
&x_a\ge0.
\end{aligned}
\]

Upper bounds `x_a<=1` are redundant because every action belongs to one
lower-orbit at-most-one constraint.

GLOP, CLP, and SCIP/SoPlex independently returned objective 61.  More
importantly, the optimum has the following exact arithmetic certificate.

## The exact `1/8`-integral dual certificate

The certificate assigns:

- a free potential `q_v` to 175 central vertices (zero elsewhere);
- a nonpositive penalty `r_L` to four lower-orbit constraints (zero
  elsewhere).

Every value is an integer multiple of `1/8`.  The four nonzero lower
penalties are

\[
r_{319}=-1,qquad r_{1269}=-\tfrac14,qquad
r_{1679}=-1,qquad r_{1893}=-1.
\]

The complete 175-entry potential table is stored in
`scratch/k15_joint_scaffold_degree_dual.certificate.json`.

The verifier checks, with exact integer arithmetic, all 11,569 inequalities

\[
             \sum_v q_v\delta_a(v)+r_{L(a)}\le1.       \tag{1}
\]

There are 2,585 tight action inequalities.  It also checks the exact dual
objective identity

\[
 \sum_v q_v(2-d_0(v))+\sum_Lr_L=\frac{488}{8}=61.      \tag{2}
\]

For any fractional degree-two projection `x`, multiply (1) by `x_a` and sum:

\[
\begin{aligned}
\sum_a x_a
&\ge \sum_vq_v\sum_a\delta_a(v)x_a
   +\sum_Lr_L\sum_{a:L(a)=L}x_a\\
&=\sum_vq_v(2-d_0(v))
   +\sum_Lr_L z_L\\
&\ge\sum_vq_v(2-d_0(v))+\sum_Lr_L\\
&=61.
\end{aligned}
\]

The second inequality uses `r_L<=0` and `z_L<=1`.  This proves the whole
radius-60 ball infeasible in one calculation.

## Independent audit of the radius-61 witness

The witness is

`scratch/k15_joint_scaffold_degreeonly_r61.json`.

The standalone verifier reconstructs both selectors from explicit choice
triples and checks:

- one choice occurs at every lower orbit;
- exactly 61 lower-orbit choices differ from the scaffold;
- every one of the 429 quotient central vertices has degree exactly two;
- the physical lift covers all 6,435 central sets with degree two.

The physical lift is a 21-component 2-factor with component lengths

```text
3660,
141 (five times),
138 (fifteen times).
```

The independent negative audit is equally important:

- 795 residence violations;
- 46 missing upper-`q=1` orbit colours;
- 55 missing lower-`q=2` orbit colours;
- 20 missing lower-`q=3` orbit colours;
- 77 missing upper colours over the full audited tower.

Thus the witness proves only that the degree projection distance is 61.  It is
a search hint, not a `k=15` solution.

## Reproducer and verification

Discovery/generation:

- `scratch/audit_k15_joint_scaffold_degree_lp.py`
- `scratch/generate_k15_joint_scaffold_degree_dual_certificate.py`

Exact solver-free verification of the stored certificate and witness:

```bash
PYTHONPATH=scratch python3 \
  scratch/verify_k15_joint_scaffold_degree_projection.py \
  scratch/fixtures/k15_joint_q1_q3_scaffold_hint_v1.json \
  scratch/k15_joint_scaffold_degree_dual.certificate.json \
  scratch/k15_joint_scaffold_degreeonly_r61.json
```

Verified output:

```json
{"continuous_lower_bound": 61.0, "dual_nonzero_degree_multipliers": 175, "dual_nonzero_lower_multipliers": 4, "dual_tight_actions": 2585, "exact_degree_projection_distance": 61, "minimum_dual_slack_numerator": 0, "physical_cycle_count": 21, "physical_cycle_lengths": [3660, 141, 141, 141, 141, 141, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138, 138], "quotient_degree_histogram": {"2": 429}, "status": "VERIFIED", "witness_hamming_distance": 61}
```

Artifact hashes:

| artifact | SHA-256 |
|---|---|
| joint scaffold | `8e48bff3328b3440c479f4dd659f5350f4f17917160766612b968e5361a70fdb` |
| exact dual certificate | `1b131a34658feab6f09146e0c7f46bcfa709b34cad1ba245de84a1285d8b14d2` |
| radius-61 witness | `5ad877cfa8f599d28fdddbcc0154c1bd4e73f850313ff3f8df59a5fd1f6089ac` |

## Relation to a DRAT proof

The exact dual is a stronger and much smaller certificate than a Boolean
DRAT trace: it proves infeasibility of the fractional relaxation and is only
3.5 KB.  A deterministic CNF encoding of the relaxed dual support was also
constructed, but its sequential-counter encoding produced a 53 MB formula
and a rapidly growing proof trace.  That redundant trace was stopped and
deleted; retaining it would add no mathematical assurance beyond the exact
integer verifier above.

## Search consequence

Any degree-reconciliation search centred on this joint scaffold should begin
at radius 61.  Radius 61 is already saturated merely by restoring degree;
requiring upper-`q=1`, residence, connectivity, or deeper shadows can only
increase the required distance or make that shell infeasible.

