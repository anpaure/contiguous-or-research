# Thread D: phase-free carrier to exact `COMP_3` adapter

Date: 2026-07-30

Status: the fail-closed physical adapter is implemented and its new shadow
rows pass independent `K=8`/`K=10` regressions.  The retained fresh `K=10`
phase-free carrier does **not** compile: it is already missing nine cyclic
arbitrary-upper targets, so no cut or source assignment can repair it.

## 1. Executable contract

The executable is
`scratch/threadD_phasefree_comp3_adapter_20260730.py`.  Given a decoded
phase-free result it independently performs the following steps.

1. Recompute and verify the producer payload hash.
2. Rebuild the complete literal two-rail option catalogue.
3. Replay every selected option, the quotient Hamilton circuit, the single
   A/B shore blocks, and voltage one.
4. Materialize all coordinate rotations and require that the resulting
   physical cycle is exactly the full middle layer, with no repeated owner
   and no non-Johnson edge.
5. Recompute every cyclic positive run and enforce the advertised residence.
6. For `q=1,2,3`, enumerate every cyclic `(q+1)`-owner intersection and
   compare its support with the complete rank-`R-q` layer.
7. Compute every arbitrary-width cyclic upper witness by the exact
   accumulated-union recurrence, not a fixed-width proxy.
8. For a requested cut and orientation, repeat the lower and arbitrary-upper
   audits on the literal linear path and verify the maximal erosion core.
9. Only for depth three, and only after those checks, call the retained exact
   `COMP_3` source model.  A returned word is accepted only if
   `full_word_audit` derives exactly the proposed middle path and covers every
   nonempty mask.  At `K=16` it also requires an actual source letter
   `{z}=32768`; consequently a PASS includes a literal census of all 65,535
   nonempty masks.

The exact optimum has depth two at `K=8,10`.  Those dimensions validate the
new carrier rows and reconstruction, but are deliberately not sent to the
depth-three compiler.

For a fixed target rank, the lower row is exact because its witness is by
definition

\[
  T_i\cap T_{i+1}\cap\cdots\cap T_{i+q}.
\]

The upper recurrence keeps precisely all values of interval ORs ending at
the current owner.  Doubling a cyclic chronology adds all wrapped intervals;
intervals longer than one revolution add only the already present full-set
union.  Hence this is an iff oracle for arbitrary-width cyclic upper
coverage.  The regression suite also compares the recurrence with literal
quadratic enumeration on random small words.

## 2. Exact retained regressions

### `K=8`

The 70-owner carrier is independently reconstructed and gives

| gate | holes |
|---|---:|
| lower q1 | 0 |
| lower q2 | 0 |
| lower q3 | 0 |
| arbitrary upper, all ranks | 0 |

Its minimum cyclic positive run is three, as required for depth two.  Cut
zero in forward orientation also has zero q1/q2/q3 and arbitrary-upper holes
and an exact nonempty maximal depth-two envelope.  This is a carrier-row
regression, not a new word certificate.

### `K=10`

The 252-owner carrier has minimum positive run three and complete q1 and q3,
but exact replay gives

\[
 \text{lower-q2 holes}=\{73,146,292\}
\]

and the nine rank-seven arbitrary-upper holes

\[
 \{687,701,757,855,862,890,939,981,1002\}.
\]

These are cyclic holes.  A linear cut can only delete cyclic witnesses, so
no cut can supply any of the nine absent upper targets.  The existing exact
compiler rejects a chronology with an arbitrary-upper hole before creating
source variables.  Thus this fresh `K=10` candidate is unconditionally
ineligible for `COMP_3`/the corresponding depth-two compiler; this is not a
resource-limited or solver-derived conclusion.

## 3. Artifacts and scope

- source: `scratch/threadD_phasefree_comp3_adapter_20260730.py`
- tests: `scratch/test_threadD_phasefree_comp3_adapter_20260730.py`
- `K=8` replay: `scratch/threadD_k8_phasefree_comp3_adapter_20260730.audit.json`
- `K=10` replay: `scratch/threadD_k10_phasefree_comp3_adapter_20260730.audit.json`

All four lightweight tests pass locally.  No H100 job was launched.  No
`K=16` carrier, compiler, SAT, UNSAT, or word claim is made here.  A future
CP-SAT `INFEASIBLE` result remains scoped to the fixed cut and normalized
one-block/unit-voltage carrier class and must retain its exact model and
resource provenance; resource/time termination is `UNKNOWN`.
