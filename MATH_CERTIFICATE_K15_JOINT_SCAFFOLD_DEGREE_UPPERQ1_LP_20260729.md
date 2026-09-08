# Exact LP certificate for the `k=15` joint scaffold: degree two plus upper `q=1`

Date: 2026-07-29

## Result

Let `S_0` be

`scratch/fixtures/k15_joint_q1_q3_scaffold_hint_v1.json`.

Among fractional replacements of its quotient choices satisfying

1. at most one replacement at each lower orbit;
2. quotient degree exactly two at all 429 central vertices; and
3. coverage of all 335 upper-`q=1` orbit colours,

the exact minimum Hamming mass is

\[
 \boxed{
 \frac{1277131056929583148784443}
      {17012931595358722031549}
 =75.06825321498359\ldots }                       \tag{1}
\]

The optimum is certified by matching exact rational primal and dual
solutions.  Consequently every integral selector satisfying degree two and
all upper-`q=1` colours changes at least

\[
                              \boxed{76}
\]

lower-orbit choices.

In particular, every radius-64 carrier search centred on this joint scaffold
is infeasible before residence, connectivity, voltage, or deeper shadows are
considered.

## LP formulation

There are 11,569 replacement actions.  For an action `a`, write

- `L(a)` for its lower orbit;
- `delta_a(v)` for its endpoint-degree change at central vertex `v`;
- `old(a),new(a)` for its old and new upper-`q=1` colours;
- `x_a>=0` for its fractional selection.

Let `d_0(v)` and `ell_0(c)` be the scaffold's initial degree and colour load.
The LP is

\[
\begin{aligned}
\min\quad &\sum_a x_a,\\
\text{subject to}\quad
&\sum_{a:L(a)=L}x_a\le1 &&\forall L,\\
&\sum_a\delta_a(v)x_a=2-d_0(v) &&\forall v,\\
&\ell_0(c)+\sum_a
  \bigl(\mathbf1_{new(a)=c}-\mathbf1_{old(a)=c}\bigr)x_a\ge1
  &&\forall c,\\
&x_a\ge0.
\end{aligned}                                      \tag{2}
\]

The per-action upper bounds are redundant because each action belongs to one
lower-orbit at-most-one constraint.

The scaffold already covers every upper-`q=1` colour, with load histogram

| load | colours |
|---:|---:|
| 1 | 266 |
| 2 | 48 |
| 3 | 17 |
| 4 | 4 |

Thus the colour constraints are survival constraints: the projection must
repair degree without deleting the last copy of any existing colour.

## Exact dual proof

The dual certificate consists of

- four nonzero lower-orbit multipliers `r_L<=0`;
- 428 nonzero free degree potentials `q_v`;
- 184 nonzero colour multipliers `s_c>=0`.

All multipliers share the common denominator

```text
170129315953587220315490
```

and are listed exactly in

`scratch/k15_joint_scaffold_degree_upper1_exact_dual_primal.certificate.json`.

For every one of the 11,569 actions, the verifier checks

\[
 q\!\cdot\!\delta_a+r_{L(a)}+s_{new(a)}-s_{old(a)}\le1.       \tag{3}
\]

There are 620 tight action inequalities.  Multiplying (3) by a feasible
`x_a` and summing gives

\[
\begin{aligned}
\sum_a x_a
&\ge q\!\cdot\!(2-d_0)
 +\sum_L r_L z_L
 +\sum_c s_c(\ell(c)-\ell_0(c))\\
&\ge q\!\cdot\!(2-d_0)
 +\sum_Lr_L
 +\sum_cs_c(1-\ell_0(c))\\
&=\frac{1277131056929583148784443}
        {17012931595358722031549}.
\end{aligned}
\]

Here `z_L<=1`, `r_L<=0`, `ell(c)>=1`, and `s_c>=0` give the second
inequality.

## Exact primal proof and optimality

GLOP's optimal basis has size 616:

- 428 active degree rows;
- 184 active colour rows;
- four active lower-orbit rows.

The same 616-by-616 integer basis was solved over `QQ` using SymPy's
fraction-free `DomainMatrix.solve_den`.  Solving the transposed basis gives an
exact feasible primal solution with 442 nonzero actions and common denominator

```text
17012931595358722031549
```

The verifier checks exactly:

- nonnegativity of all 442 stored action values;
- all 429 lower-orbit capacities;
- all 429 degree equalities;
- all 335 upper-colour inequalities;
- equality of the primal and dual objectives.

This proves (1) as the exact LP optimum, rather than merely a numerical lower
bound.  Numerical solves independently agreed:

| backend | objective |
|---|---:|
| GLOP | `75.06825321498359` |
| CLP | `75.06825321498373` |

## Integer status: `76 <= optimum <= 85`

The current best stored integral selector is the live-optimizer snapshot

`scratch/k15_joint_q1factor_d85_snapshot.json`

with SHA-256

```text
9b00309d55723be62530f9420e458b885bba1386ca4bd699c67ba41f22a19447
```

and Hamming distance 85.  Independent local reconstruction verifies

- one choice per lower orbit;
- quotient degree histogram `2^429`;
- zero missing upper-`q=1` colours.

Therefore the present rigorous interval for the integer degree-plus-`q=1`
projection problem is

\[
                              76\le I\le85.
\]

The incumbent is not a full carrier.  Its physical lift has five components
of lengths

```text
3705, 1725, 615, 270, 120
```

and it has 1,140 residence violations, 52 lower-`q=2` holes, 27
lower-`q=3` holes, and 20 missing upper colours beyond `q=1` over the full
audited tower.

## Relation to exact-shell searches

The earlier exact CP-SAT shell runs returned infeasible through radius 61 for
degree plus upper `q=1`.  They were correct but far weaker than the LP
certificate: the fractional bound alone excludes every integral shell through
radius 75 simultaneously.

The live radius-64 jobs were therefore searching an empty region.  Searches
at radius 76 and above remain logically possible; the best known integral
point is currently at radius 85.

## Artifacts and verification

Authoritative artifacts:

| artifact | SHA-256 |
|---|---|
| exact primal/dual certificate | `31251f4d44b0a05d073283bac59c6d85010d67e683c98774b3527b91e41d5cee` |
| GLOP basis record | `42245a0dfdb66c75e0ec0ac78c0ca4073eb88f27a2988b3a0b522481d35b7fab` |
| distance-85 incumbent | `9b00309d55723be62530f9420e458b885bba1386ca4bd699c67ba41f22a19447` |
| joint scaffold | `8e48bff3328b3440c479f4dd659f5350f4f17917160766612b968e5361a70fdb` |

Discovery and exactification:

- `scratch/audit_k15_joint_scaffold_degree_upper1_lp.py`
- `scratch/exactify_k15_joint_scaffold_degree_upper1_basis.py`

Solver-free exact verification:

```bash
PYTHONPATH=scratch python3 \
  scratch/verify_k15_joint_scaffold_degree_upper1_dual.py \
  scratch/fixtures/k15_joint_q1_q3_scaffold_hint_v1.json \
  scratch/k15_joint_scaffold_degree_upper1_exact_dual_primal.certificate.json \
  --incumbent scratch/k15_joint_q1factor_d85_snapshot.json
```

Verified output includes

```json
{
  "status": "VERIFIED",
  "exact_lp_optimum_certified": true,
  "certified_lower_bound": 75.06825321498359,
  "certified_integer_minimum": 76,
  "incumbent_hamming_distance": 85,
  "radius64_feasible": false,
  "actions_checked": 11569,
  "primal_nonzero_actions": 442
}
```
