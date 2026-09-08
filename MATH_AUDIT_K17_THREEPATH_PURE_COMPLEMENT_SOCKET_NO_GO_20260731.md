# K17 three-path pure-complement socket no-go (2026-07-31)

## Scope

This note audits the frozen three-path phase witness
`scratch/k17_marked_atom_phase_path_frozen_20260731.json` and closes only the
two endpoint-specific **shore-preserving pure-complement geodesic** socket
families.  It does not exclude mixed-tag circuits, splitting or rephasing one
of the six endpoint atoms, or choosing a different path cover.

The deterministic verifier is
`scratch/audit_k17_threepath_pure_complement_socket_no_go_20260731.py`.
It reconstructs the three literal paths through the independent H2 decoder;
it does not import the abandoned C6/C10 residual-bfactor solver.

## What the 192 fixed U connectors prove

In the rank-8 port multigraph, every selected U connector uses two distinct
ports at which the fixed macro degree is exactly one.  Adding that U edge
therefore saturates both ports.  Every unsplit macro seam inside an atom is
already saturated by its two incident macro edges.  Consequently, in any
connected degree-two completion, each of the three decoded owner words occurs
as one cyclic interval, up to reversing the whole interval.

This does **not** join the three intervals.  The six path-end ports have fixed
macro degree two and residual demand zero, so each path end continues into its
fixed complementary macro.  Thus “two sockets” is initially only the linear
component ledger (3-1=2), not a certificate that two particular physical
facet circuits exist.

## Pure-complement bracketing lemma

Fix a binary coordinate (c).  Let a left word end in the pattern

\[
0,1,1
\]

and a right word begin in the pattern

\[
1,1,0.
\]

Insert between them a bridge of at least two owners on which (c=0)
identically.  Then the concatenation has two bounded one-runs of length two in
coordinate (c).  Hence it violates D2 residence.  In the adjacent-OR trace,
each pattern (0,1,1,0) becomes a bounded one-run of length three.  The two
zero bridge owners supply a zero OR-edge between the two sides, so these runs
remain distinct; hence D3 residence also fails twice.

The statement is independent of the bridge length and its old-coordinate
geodesic ordering.  Its hypotheses deliberately do not cover a bridge that
carries (c), or a circuit that changes either endpoint word.

## Exact application

The abstract concatenation order is path 0, path 2, path 1, with literal path
lengths 898, 4834, and 78 in that order.

1. **C6 interface (path 0 to path 2).**  The phase endpoints are 76515 and
   77365.  The complementary tails are the X-shore owners 43747 and 44597,
   at Johnson distance three.  Every shortest tail geodesic is all-X.  The
   endpoint words have forced Y profiles (0,1,1) and (1,1,0).  After the
   phase-owner/facet-disjoint and local-residence filters, exactly 20 rows
   remain.  All 20 have exactly two D2 length-two and two D3 length-three
   defects in tag bit 16.  Full-context pass count: zero.

2. **C10 interface (path 2 to path 1).**  The phase endpoints are 59846 and
   40045.  The complementary tails are the Y-shore owners 92614 and 72813,
   at Johnson distance five.  Every shortest tail geodesic is all-Y.  The
   endpoint words have forced X profiles (0,1,1) and (1,1,0).  After the
   same filters, exactly 2207 rows remain.  All 2207 have exactly two D2
   length-two and two D3 length-three defects in tag bit 15.  Full-context
   pass count: zero.

Therefore neither the literal C6 nor literal C10 pure-complement family can
realize the two abstract joins while retaining the frozen phase endpoints.
The next socket catalogue must change the immediate endpoint geometry: use a
mixed-tag packet, split/rephase an endpoint atom, or change the three-path
cover.  A residual U-to-port b-flow can preserve the three intervals but
cannot remove this endpoint obstruction.

## Reproduction and hashes

Run:

```text
python3 scratch/audit_k17_threepath_pure_complement_socket_no_go_20260731.py
```

The output is byte-identical to
`scratch/k17_threepath_pure_complement_socket_no_go_20260731.audit.json`.

- verifier SHA-256: `ba7629bbdf7b772a240504c955d7ec048345f26cddbea4c9a1a0d01bb212e8e7`
- JSON SHA-256: `df272bbeeaef7faf0965410711124b2e366d4dae02db3c87913893c8338ecb65`
- JSON payload SHA-256: `86d0510ac2ade8709a9ee1f14b0422bab5c88b9ed33493f978e27ef75dcd5103`
- frozen witness SHA-256: `234a34703cdef66722d6df54b936361048565915f4bf9ab523e13368d828bdec`
- independent decoder SHA-256: `805dee17d08d00a60b819f495f44a0b87c256fdfdc47ff6e0a30b3bebcc120ec`

The candidate-list payload hashes are
`3e7a374ca8da01a851574027336bad09c894ad49eefafe5fc9e939db4c7c238e`
for C6 and
`4d61af557b72231afbc98a2a0e6330c8cbc25a8e61c7c267b65097a4a3f1bd8a`
for C10.
