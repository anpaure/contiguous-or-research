# K16 state2 buffered facet-star closure-graph no-go

Date: 2026-07-30

## 1. Scope and verdict

Consider either authenticated length-12,873 state2 chronology

| case | target SHA-256 | blocker \(H\) | first flat | capacity |
|---:|---|---:|---:|---:|
| 0 | `762a6361c571f4e182aa03340399d3a1c07f25755c689362da173f04bd1cc407` | `0x1639` | 1,102 | 26,845 |
| 1 | `1e75cfb4c8e610a4ea2bf1095e44d3236f655aabc3efe65e8532912b7c0572a8` | `0x1879` | 2,031 | 27,774 |

Both sources are exact G0 carriers, have the prescribed tail flats at
12,869 and 12,871, and have no upper hole.  Their independent source audit is

`scratch/k16_state2_hostseam_5opt_survivors_20260730/independent.audit.json`,
SHA-256 `a189324d549d1e4caa6f6cb2b070ee30dd62df578177b76b9962180ee1f2d233`.

For either source, choose three distinct rank-eight rows of the form
\(H\cup\{x\}\).  Remove each complete source collar of radius three, retain
the residual core in source order, and insert all twenty-one removed rows as
one contiguous block at one residual-core gap.  The order in that block is
arbitrary.  In particular, this contains every radius-three three-strand
braid obtained by independently orienting the collars and interleaving them
layer by layer.

The nine centres are exactly the nine distinct cofacets
\(H\cup\{x\}\), one for each coordinate outside \(H\).  Hence any three
distinct chosen centres have meet exactly \(H\).  In the intended
layer-interleaved braid their centre layer is three consecutive rows, so in
a flat-free depth-two neighbourhood the envelope of the third centre cell is
exactly that meet.  This is therefore the advertised physical \(H\)-host
mechanism; the obstruction below occurs earlier, at the carrier
reconstruction gate.

**Theorem.** No word in this fibre is an exact tail-fixed G0 carrier.  Thus no
member reaches the host, upper-completeness, or full static lower-atlas gates.

This is a solver-free, source-relative theorem.  It says nothing about two or
more insertion gaps, edited row values, larger atoms, other source words, or
unrestricted K16.

## 2. Exact local reconstruction

Away from a flat, let the current depth be \(d\in\{2,3\}\).  For a target row
sequence \(q\), the maximal envelope and reconstructed row are

\[
 E_c=\bigwedge_{j=\max(0,c-d)}^c q_j,
 \qquad
 R_d(q)_i=\bigvee_{c=i}^{i+d}E_c.
\]

An exact carrier requires

\[
 R_d(q)_i=q_i                                                     \tag{1}
\]

for every row.  If a radius-three collar centred at \(p\) is removed, write
\(b=p-3\) for the new directed seam, from the last retained row on its left
to the first retained row on its right.  Only rows

\[
 b-d\le i\le b+d-1
\]

have a reconstruction window crossing this seam.  Their combined target
support lies in

\[
 [b-2d,b+2d-1]\subseteq[b-6,b+5].                               \tag{2}
\]

Equation (2) is the six-row port bound.  It is also why a change at a
residual-core insertion gap farther than six from \(b\) cannot repair a
failed seam equation.  Moving the first flat can only change the constant
local phase between \(d=3\) and \(d=2\), so the audit deliberately tests both
phases at every seam.  This is a relaxation of the actual chronology.

## 3. Directed seam graph

For every cofacet centre \(p\) and phase \(d\), form a directed edge

\[
 L_{p,d}\longrightarrow R_{p,d}
\]

whose ports are the retained source rows on the two sides of the deleted
collar.  The edge is admitted exactly when every crossing row satisfies
(1).  All rejected edges have an explicit row and a nonzero lost-bit mask;
the reconstructed mask is always a strict submask of the requested row.

The complete compatibility table is remarkably small.  A two-character
signature records admission at depths \((2,3)\):

| case | cofacet centres | signatures |
|---:|---|---|
| `H=0x1639` | 6, 1058, 2167, 4387, 10966, 11032, 11287, 11366, 12199 | `00` at all nine centres |
| `H=0x1879` | 617 | `10` |
| `H=0x1879` | 1987, 4025, 5316, 6061, 10681, 11190, 12387, 12768 | `00` at all eight centres |

The literal 36-edge catalogue is

`scratch/k16_state2_buffered_star_closure_graph_20260730.tsv`, SHA-256
`dfd84e12080b37b1f07983a7b5e25fdeaee9885e5955171a08f9d9de65bbeb59`.

For example, the exceptional case-1 centre 617 passes only the relaxed
depth-two edge.  Its actual source phase is depth three, where row 611 asks
for `0x5b26` but reconstructs only `0x5326`, losing `0x0800`.  Every actual
source-phase edge in both cases is rejected.

## 4. The one-gap patch bound

The nine source collars are pairwise disjoint.  After any three are removed,
their directed closure gaps remain far apart:

| case | minimum centre separation | minimum compacted closure separation |
|---:|---:|---:|
| 0 | 66 | \(66-7=59\) |
| 1 | 381 | \(381-7=374\) |

The radius-six influence zones from (2) are therefore disjoint.  Inserting
one contiguous block at one residual-core gap can replace or locally affect
at most one of the three closure edges.  The orientation and internal order
of that block do not alter either of the two other core adjacencies.

In case 0, every selected triple has three phase-relaxed forbidden closure
edges.  One insertion patch leaves at least two failures.  In case 1, at most
one of the selected centres can be the lone relaxed edge at 617.  Every
triple therefore has at least two forbidden closure edges, and one insertion
patch leaves at least one failure.  Equation (1) then rules out an exact
carrier.

There is also a stronger actual-phase form.  A separate audit verifies that
every row in each of the eighteen possible source collars is unique within
its root, every collar is disjoint from the three source flats, and every
removal-closure endpoint pair is unequal.  Consequently neither a removal
closure nor any
internal or external weave join can create a new flat.  If the insertion
splits an original flat, the candidate has only two flats and fails G0;
otherwise the original flat ledger and every closure's actual phase are
preserved.  All eighteen actual-phase closure edges fail.  Hence one
insertion patch leaves at least two literal carrier failures in **both**
cases.  The phase-relaxed argument above is retained as an independent
over-approximation.

Equivalently, among all \(9P3=504\) ordered centre triples in each case, zero
have the two compatible unpatched edges required after one possible patch.
The eight independent strand orientations give 4,032 layer-interleaved
representations per case, all eliminated before their internal weave is even
examined.

## 5. Audit and relation to the fixed-host runs

The byte-reproducible audit

`scratch/audit_k16_state2_buffered_star_closure_graph_20260730.py`

has SHA-256
`d8f9a9b75a3504d6aee9317fe0704af3f22c3bbf7d5fac0ce599903003b3a4fb`.

It authenticates both targets and stored envelopes, reconstructs every maximal
envelope and target row, checks the capacities and upper coverage, extracts
the exact nine cofacets, evaluates all 36 directed phase edges, enumerates all
84 unordered and 504 ordered triples per case, and independently checks the
radius-six patch-zone overlap at every residual-core gap.

Its output is

`scratch/k16_state2_buffered_star_closure_graph_20260730.audit.json`, SHA-256
`1bd7ea59ee6fbdb81559bad4f592479bb86c65ba8246bbb2149d27118d4e69b0`,
payload SHA-256
`6f8339fa6ff01f27e8bfb6bc9207b8738e3bd158bb3994577c48b50eb3c42f95`.

The earlier H100 runs used the exact layer-interleaved implementation
`scratch/search_k16_buffered_facet_star_braid_20260730.cpp`, SHA-256
`12d8b4d704f2c0ee1dcb5db0eafb8b3b9c0ef0b2a02ba305342108ed7ef97587`,
at only the nominated cells 4,930 and 2,036.  They found `carrier=0` in 4,032
jobs per source.  Those finite runs are consistent with, but are not needed
for, the host-position-independent closure-graph proof above.

A structurally separate streaming-port implementation proves that six rows
on each side are both sufficient and sharp, derives all removal, insertion,
and twenty internal weave seams from the literal origin path, and matches
direct full replay on authenticated representative paths.  Its theorem,
verifier, and output are respectively

- `scratch/k16_state2_buffered_star_graph_independent_20260730/THEOREM_DIRECTED_RADIUS3_SEAM_GRAPH.md`, SHA-256 `71a9c7b43120285171a523d088530e256aaeffb64ac98b7f3d3239ab40b19753`;
- `scratch/k16_state2_buffered_star_graph_independent_20260730/audit_directed_radius3_graph.py`, SHA-256 `49dda85fa30ff5d6b74983dc077241f1461605ef93392c8c941ab8459cb39251`;
- `scratch/k16_state2_buffered_star_graph_independent_20260730/audit.json`, SHA-256 `ac9fc8b9f8f5408dd8fca669d0116a5a54abc42c1b03cc6dda2639f25bc9b1cc`, payload SHA-256 `08d9201f1dd0c9c7a69ae04d2a1549791d2bed7301b64bfbbdf59bf34c116ad0`.

The same independent implementation then cross-checks every one of the 36
phase-edge records and both complete 84-triple ledgers from the primary
audit, with zero mismatch:

- `scratch/k16_state2_buffered_star_graph_independent_20260730/cross_audit_closure_graph.py`, SHA-256 `ccefca7d86c414313ee71f1a4a129937690a00c67ab2b52ad96368c5662edb0b`;
- `scratch/k16_state2_buffered_star_graph_independent_20260730/closure_graph_cross_audit.json`, SHA-256 `078235cdf6a9c76c701971512b0aa9a07ffd4c2ca27bbafe8340ae0524901816`, payload SHA-256 `ff8afd90109507962bfd4357d837b528386f90b02355cbff8b44f5014df11a73`.

Finally, a second independent closure implementation performs the stronger
actual-phase census and enumerates the exact directed repair-gap set of every
canonical failure in all 168 unordered triples.  It obtains 2,240 directed
repair incidences, maximum one affected closure at any insertion gap, and
minimum two untouched failures for either root:

- `scratch/k16_state2_layer_interleaved_closure_obstruction_20260730/audit_k16_state2_layer_interleaved_closure_obstruction_20260730.py`, SHA-256 `fa9a0d2b81930756cc79ace0dcfba4a7fa9b4c975dd2ab31765bac0cfda34ea4`;
- `scratch/k16_state2_layer_interleaved_closure_obstruction_20260730/independent.audit.json`, SHA-256 `332a9cb257ea4a80ffaf40097f851a22eeb787775976783af86ba9c3e3cfbd4d`, payload SHA-256 `32d196d894bb8818b67ba9593e45dfdb496100ae9b2645c33b53cd075114da6d`;
- `scratch/k16_state2_layer_interleaved_closure_obstruction_20260730/closure_catalogue.tsv`, SHA-256 `b3c24ae420775250fe2e1d001a2ee86e38ac4c2fb3ff50da5492e91059e7751b`;
- `scratch/k16_state2_layer_interleaved_closure_obstruction_20260730/triple_port_catalogue.tsv`, SHA-256 `333e320875547ece1112bfdd4b5b305268cff946b140dbabbdbe5bb614ebd7fb`;
- `scratch/k16_state2_layer_interleaved_closure_obstruction_20260730/directed_repair_ports.tsv`, SHA-256 `017e5f50c984e2c7ac3e66df8ba3f1793dbecf7678676b03863112d07ba55f04`.
