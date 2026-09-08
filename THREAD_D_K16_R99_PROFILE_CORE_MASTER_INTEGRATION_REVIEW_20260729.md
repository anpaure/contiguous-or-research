# Thread D: r99 profile-core master integration review (2026-07-29)

## Verdict

The 21-feature row in
`scratch/threadD_k16_r99_retain_r105_fixed_recourse_minimal_core_20260729.json`
has an exact, small master encoding.  The minimal encoding adds **18 Boolean
variables and 37 constraints** to either branch.  No q1-loss variable is
needed.  The row is branch-independent and is compatible with existing v4
Hall/core resumes because it changes only the master; the exact recourse
subproblem and its scope digest remain unchanged.

The core artifact has file SHA-256
`ba56f188ec49c8a30c867623470aad6c1b3f8541c311a9cd4715fc1ef7d8c2bf`
and embedded payload SHA-256
`c8d65e5c8a8e3766a87a5b8cbbcd238d36d8a4c8d48346d5f2849437b804ceb4`.
Its final replay is `INFEASIBLE`; all 21 one-feature deletions have feasible
witnesses.  The independent solver-free semantic audit is
`scratch/threadD_k16_r99_retain_r105_state_core_and_hall_20260729.audit.json`
(file SHA-256
`0ff37f35db85155f97f064c189bb86e25876f4224f52cfd78bc40510041df4e4`).

## Exact row

Let

\[
 b_v(x)=\sum_{e\in F:\,v\in e}x_e,
\]

where `x_e=master_cut[e]`.  The frozen source is loopless degree two, hence
`b_v` is always in `{0,1,2}`.  Define `z_v=[b_v=0]` for

```
397,399,465,476,501,544,590,592,
661,713,728,772,777,821,843,851
```

and `u_v=[b_v<=1]` for `v=823,845`.  The three lost-colour indicators are
exactly

```
lost_lower(1,693) = x_17223
lost_upper(1,5805) = x_20660
lost_upper(1,5813) = x_20691.
```

Each displayed colour has exactly the shown singleton source-provider set;
all three edge IDs lie in the 858-edge source.  Therefore the generalized
Benders row is

\[
 \sum_{v\in Z}z_v+u_{823}+u_{845}
 +x_{17223}+x_{20660}+x_{20691}\le 20. \tag{P21}
\]

Do not replace the final three terms by aggregate lower/upper loss counts:
the certificate depends on these literal colours.

## Minimal exact Boolean channels

For each zero node introduce one Boolean `z_v` and add

\[
 b_v\le 2(1-z_v),\qquad b_v\ge 1-z_v.
\]

If `z_v=1`, these force `b_v=0`; if `z_v=0`, they force
`b_v in {1,2}`.  Thus `z_v` is equivalent to, rather than merely implied by,
`b_v=0`.

For each threshold-one node introduce one Boolean `u_v` and add

\[
 b_v\le 2-u_v,\qquad b_v\ge 2(1-u_v).
\]

If `u_v=1`, these force `b_v<=1`; if `u_v=0`, they force `b_v=2`.
Thus `u_v` is exactly `[b_v<=1]`.

This uses 18 Booleans, 36 channel constraints, and the one P21 constraint.
The artifact's three-way one-hot endpoint channel is also correct, but would
use 54 Booleans for the same 36 channel constraints.  Unless several future
profile rows reuse the same endpoint states, the 18-variable encoding is the
strictly smaller exact encoding.

Suggested insertion immediately after `master_cut_incident` is built:

```python
require(all(len(master_cut_incident[v]) == 2 for v in range(len(cat.nodes))),
        "profile channels require the loopless degree-two source")
profile_terms = []
for node in PROFILE_ZERO_NODES:
    z = master.new_bool_var(f"profile_b{node}_eq0")
    b = sum(master_cut_incident[node])
    master.add(b <= 2 * (1 - z))
    master.add(b >= 1 - z)
    profile_terms.append(z)
for node in PROFILE_LE1_NODES:
    u = master.new_bool_var(f"profile_b{node}_le1")
    b = sum(master_cut_incident[node])
    master.add(b <= 2 - u)
    master.add(b >= 2 * (1 - u))
    profile_terms.append(u)
profile_terms.extend(master_cut[e] for e in (17223, 20660, 20691))
master.add(sum(profile_terms) <= 20)
```

The endpoint expression must use `master_cut_incident`, not incident
`master_y`: `y` records only selected double-repair seams and is not the exact
endpoint demand of the recourse problem.

## Exact model deltas

The current static master census is 21,645 variables and 3,691 retain / 3,692
delete constraints.  After P21 it must be

| branch | variables | static constraints |
|---|---:|---:|
| retain | 21,663 | 3,728 |
| delete | 21,663 | 3,729 |

With `H` imported dynamic portal-Hall rows and `C` replayed positive cores,
the resumed constraint census is respectively `3728+H+C` or `3729+H+C`.
In particular, the authenticated retain-r103 v4 bootstrap contains `H=140`
and `C=0`, so its exact new initial census is **21,663 variables / 3,868
constraints**.

The objective is unchanged.  The 18 profile variables should be created
after all existing `master_cut` and `master_y` variables so their existing
indices remain stable, although resumes use edge IDs rather than master
literal indices.

## Resume compatibility

The subproblem remains 27,428 variables / 2,387 constraints and its scope
SHA-256 remains
`3a86d00e6c2ecd496b1ad0026328881db2aa3d9600aa32ff0179dccaf2be9e79`.
Consequently:

1. Existing v4 `learned_portal_hall_rows` remain valid and are replayed
   semantically as before.
2. Existing positive edge cores remain valid; the current driver already
   replays each against the unchanged exact subproblem before adding it.
3. The P21 row must **not** be inserted into `learned_cores`: that field is a
   list of positive source-edge subsets and `add_no_good` would encode a
   different inequality.
4. Legacy `k16-r99-joint-cover-cegar-search-v1` files are still not direct
   resumes.  Their Hall rows require the existing authenticated bootstrap
   conversion; historical joint rows remain omitted.

A new uniquely named driver may accept v4 resumes as migration inputs, add
P21 eagerly, and emit v5 outputs carrying a `master_static_scope_sha256` that
binds the profile artifact, semantic row, and channel version.  If the v4
schema is retained, add equivalent mandatory metadata; otherwise old and new
master checkpoints are indistinguishable by schema even though importing an
old v4 resume is logically safe.

## Required fail-closed checks

Before adding P21, check all of the following:

- core file and embedded payload hashes;
- source, catalogue, radius 99, final replay `INFEASIBLE`, and
  `generalized_master_cut.valid=true`;
- exactly 21 distinct feature IDs: 16 `deg_le:*:0`, two `deg_le:*:1`, and
  the three listed q1 rows;
- all 18 endpoint nodes are distinct and every source incidence list has
  length two;
- for each q1 feature, the current catalogue's source-provider set and
  loopless off-source addable-provider set exactly equal the stored lists;
- the generalized conditions and RHS 20 agree with `final_core_rows`.

The evidence scope remains the artifact's stated one: trusted CP-SAT
infeasibility plus exact semantic replay, not a formal UNSAT proof.  The row
is global across retain/delete because the recourse model is branch-free, but
it says nothing about connectivity, voltage, top residence, or deeper
shadows.

## Code-review checklist

The current driver needs coordinated edits at these sites:

- master construction/census near lines 909--960: validate the profile,
  create the 18 channels, add P21, and update both censuses;
- hint auditing: report `profile_core_row` when a proposed cut has 21 true
  features, otherwise a hint can be labelled accepted although the new
  master rejects it;
- decoded-candidate assertions near lines 1418--1436: assert P21 directly,
  alongside learned core/Hall checks;
- resumed census near lines 1323--1329: use the new static baseline;
- output metadata near lines 1754--1810: record the 18 variables, 37 rows,
  core/model/audit hashes, semantic row, and trusted-evidence scope.

No model was built and no solver was run for this review.
