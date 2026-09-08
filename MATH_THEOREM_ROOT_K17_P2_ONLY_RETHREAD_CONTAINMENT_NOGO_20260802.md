# K17 P2-only rethread containment obstruction

Date: 2026-08-02

## Verdict

The fixed-P2-only role-moving face is impossible before any endpoint-state
packing is considered.  Across the two authenticated owner phases, 1,641 of
the 3,899 immutable length-two roles fail the complete relaxed-nine socket
overapproximation in at least one phase.  Of their bottom labels, 230 are
strictly contained in exactly one of the 3,899 fixed P2 roots.  That unique
root is the label's current failing role.  Consequently no permutation of
the existing P2 bottoms among the existing P2 roots can make every P2 role
socketable.

This is a scoped no-go.  It does not rule out a P2/H prefix exchange, a
carrier rethread that changes the P2 root bank, a longer compound relay, or a
K17 optimum.

## Exact formulation

Let the fixed length-two rows be

\[
  (S_i,R_i,O_i),\qquad i=1,\ldots,3899,
\]

where \(S_i\subsetneq R_i\subsetneq O_i\), the root has rank eight, and the
owner has rank nine.  A P2-only rethread assigns the same multiset of bottom
targets to the same fixed root/owner roles by a permutation \(\pi\), subject
to

\[
  S_{\pi(i)}\subsetneq R_i.
\]

For a bottom label \(S\), define its P2 containment degree

\[
  d_{P2}(S)=\bigl|\{i:S\subsetneq R_i\}\bigr|.
\]

If the current role of \(S\) has no common-phase socket and
\(d_{P2}(S)=1\), then every valid P2-only permutation fixes \(S\) on that
same role.  The role remains socketless.  One such label is enough to rule
out a full P2-only repair.

## Frozen census

The complete producer and independent replays agree on:

| item | count |
|---|---:|
| phase-0 zero roles | 1,412 |
| phase-1 zero roles | 1,413 |
| zero in both phases | 1,184 |
| phase-0 only | 228 |
| phase-1 only | 229 |
| union of phase-zero sets | 1,641 |

The union-zero bottoms have ranks

\[
  17,277,724,623
\]

at ranks four through seven.  Exactly 230 have P2 containment degree one:
four have rank six and 226 have rank seven.  A further 251 have containment
degree two, so 481 union-zero bottoms have degree at most two.

Therefore a valid repair must move at least those 230 forced labels across
the P2 boundary, or change the root bank itself.  The smallest currently
identified exact escape is the P2/H prefix exchange

\[
  (S,R)+(B,M,U)\longmapsto(B,R)+(S,M,U),
\]

with both cross-containments and a common-phase socket on the new P2 role.

## Evidence and scope

Inputs:

- `scratch/k17_fixed_p2_role_moving_escape_20260802/phase0.p2_global_union.metrics.tsv`, SHA-256 `b45713072b1d54d315c9d6de3512741aaa8c143966316bece76b80d0ec5ae137`;
- `scratch/k17_fixed_p2_role_moving_escape_20260802/phase1.p2_global_union.metrics.tsv`, SHA-256 `b7d7d70c559ae4279f366283160fa56fcb538fbe01409124981f6b9f853b882f`.

Audit source:

- `scratch/audit_root_k17_p2_only_rethread_containment_obstruction_20260802.cpp`, SHA-256 `c8fb1a7c5f762ce4131853faf6108c43085ed70d8bf3c841479054225fba1ea2`;
- `scratch/k17_fixed_p2_role_moving_escape_20260802/p2_only_rethread_containment_nogo.audit.json`, SHA-256 `814135eb5d475dc7a7a3d3a0d305c1ccb844783b3306ea7b870ccffc16aacd20`.

The independent H100 replay is frozen under
`/home/amodo/or15/work/root_k17_p2_only_rethread_containment_nogo_20260802/`.
Its manifest reproduces both input hashes and the audit hash above.

The metric inputs already range over all 2,129,483 dynamic potential long
modes, the 17 fixed soft modes, nine short addresses, and every allowed flag
pair in each phase.  Their positive rows are only an overapproximation, but
their zero rows are exact for the declared frozen P2 role.  The new argument
uses only those exact zeros and strict containment, so it does not assume
that independently positive sockets compose.

No supplier, residual cycle-cover, residence, upper-shadow, compiler, source,
or universal-word claim is made.
