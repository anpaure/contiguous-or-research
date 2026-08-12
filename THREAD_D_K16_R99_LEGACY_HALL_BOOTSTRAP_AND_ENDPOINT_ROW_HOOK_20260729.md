# Thread D: exact r99 legacy-Hall bootstrap and arbitrary endpoint-row hook

Date: 2026-07-29  
Status: proved source-level adapter; syntax audited only; no model was built and
no local or H100 solver was launched.

## 1. Authenticated branch endpoints

The latest complete guarded checkpoints are

```text
retain  scratch/k16_r99_joint_guarded_upper4_retain_r43_20260729.json
        SHA-256 0a7984a9c7fe4210a87cdd3762cdf2109ae89f8af6a2561a03065e0f5323c599
        43 rounds, 86 same-palette Hall rows, 44 joint-cover rows

delete  scratch/k16_r99_joint_guarded_upper4_delete_r43_20260729.json
        SHA-256 37d82f1950a2b9f17e3fa156c74c4d5c316063c982ad8a93806d0778796c23f1
        43 rounds, 70 same-palette Hall rows, 45 joint-cover rows
```

Both embedded payload hashes replay.  The later retain `r103` path has only a
log and is not a resumable certificate.

The last retained cuts are not feasibility certificates.  Retain ends at cut
hash `a3233585...`, with upper Hall deficit one and joint-cover deficit two.
Delete ends at `fc5013da...`, with lower Hall deficit five and joint-cover
deficit thirteen.  The best Hall-feasible recorded cuts are retain round 39,
hash `0443bea1...`, joint cover `40<41`, and delete round 9, hash
`dc4cc068...`, joint cover `38<42`.

## 2. What may be transported

Every one of the 86/70 historical Hall rows is a canonical portal-union row.
It can therefore be reconstructed from its palette, colours, unique source
providers and portal union, after which all of the following are recomputed
from the current catalogue:

1. source uniqueness of every colour;
2. completeness of the off-source provider family;
3. equality of the portal union with the union of the audited colour portals;
4. every coefficient
   `|ends(source edge) intersect portal union|`.

The two branch checkpoints each already contain two of the three current eager
Hall rows.  After semantic deduplication, the exact production bootstraps have

```text
retain: 84 imported rows, hence 3,691+84 = 3,775 master constraints;
delete: 68 imported rows, hence 3,692+68 = 3,760 master constraints.
```

Both retain the same 21,645 master variables.  The complete branch-free q1
recourse remains 27,428 variables and 2,387 constraints.

Historical joint-cover rows are not transported.  The production master has
one Boolean column for each of the 20,787 double-repair seams with exact two
colour and endpoint capacities, so every such projected joint-cover row is
already implied by the lifted `y` layer.

## 3. Upper-four provenance correction

The current certified arbitrary endpoint-cover row is reconstructed from

```text
scratch/k16_r99_6c98_fourcolour_endpoint_cover_cut_20260729.audit.json
SHA-256 aacf3b7960201815404596a4fc124e99173d38b757b347ede0b240142ecbbd3d
```

It has upper colours

```text
(1,1883), (1,1907), (1,3255), (1,5939),
```

source providers `4742,22511,23229,24034`, and a 26-node endpoint cover.
Neither r43 checkpoint contains it as a Hall row.  The delete checkpoint does
contain one older *joint/signed* encoding of the same inequality, SHA
`0a17ba4a...`; retain contains no equivalent legacy encoding.  Thus the safe
normal form is:

* reconstruct the current row eagerly from the current audit in both branches;
* import no old joint rows;
* never infer that the r43 files by themselves contain the current eager row.

For a palette, a source-unique colour family `C`, and a node set `P` meeting
every loopless off-source provider of every colour in `C`, the reusable row is

```text
sum_h |ends(h) intersect P| x_h >= sum_{c in C} x[e(c)].
```

This follows from distinct-colour seam injection and exact degree restitution.
It is branch independent.

## 4. Fail-closed adapter and generalized row schema

The standalone adapter is

```text
scratch/threadD_prepare_k16_r99_legacy_hall_bootstrap_20260729.py
```

It imports neither OR-Tools nor any solver, requires the exact current driver,
catalogue and input hashes, semantically replays every transported row, and
writes a minimal `k16-r99-cut-add-benders-cegar-checkpoint-v4` resume.  The
runtime production driver recomputes the branch-free subproblem scope hash and
rejects any mismatch before accepting it.

The output also contains a dormant
`k16-r99-arbitrary-endpoint-cover-row-family-v1` hook.  A row has fields

```text
palette
colours
source_provider_edge_ids
endpoint_cover_nodes
source_cut_coefficients
row_sha256
```

and is accepted only after complete provider coverage and every endpoint
coefficient are recomputed.  The current production driver does **not** consume
that resume array.  Its single upper-four row remains the separate eager input.
Future dynamic arbitrary-cover separation must explicitly install validated
rows and persist them under a new driver schema; placing bytes in the dormant
hook is not enough.

## 5. Next exact branch gate

The transported rows avoid rediscovering 84/68 exact Hall cuts.  They do not
close either branch.  The next branch-exact operation is the existing
branch-free both-q1 recourse oracle:

* SAT yields an exact 99-cut/99-add q1 repair, still subject to later fresh
  residence/connectivity/shadow audit;
* replayed UNSAT under positive cut assumptions yields the portable Benders
  row `sum_{e in K} x_e <= |K|-1`;
* a solver-derived row is never learned from `UNKNOWN`.

An assumption core may subsequently be projected into an arbitrary
endpoint-cover row using the schema above, but no such new projection is
claimed in this source-only iteration.

## 6. Resource-safe launch contract

No launch occurred.  A future H100-CPU launch must use exactly one worker and
both of the following limits:

```text
ulimit -v 2097152
--workers 1 --max-memory-mb 1536
```

The 2 GiB address-space limit is the hard bound; the CP-SAT parameter is only
cooperative.  Use an exclusive branch lock, a fresh output namespace and at
most one round initially.  Do not use the older frozen low-memory launcher's
3/4 GiB probe/chunk modes for this lane.  A build-only size replay and current
H100 headroom confirmation are prerequisites.

