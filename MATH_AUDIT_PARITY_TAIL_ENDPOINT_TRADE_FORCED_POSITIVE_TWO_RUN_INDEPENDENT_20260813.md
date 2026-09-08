# Independent audit: forced positive two-run in the parity-tail trade

**Date:** 2026-08-13  
**Verdict:** **PASS.**  
**Frozen source:** `MATH_OBSTRUCTION_PARITY_TAIL_ENDPOINT_TRADE_HAS_FORCED_POSITIVE_TWO_RUN_20260813.md`  
**Source SHA-256:** `642052a1b0e0a9e38490fe586c8836e57b90674abfc15d54362bd98f9f12b7fe`  
**Verifier SHA-256:** `63a55309ab9bb709e6fa1aeb835b932ed657ed1560932015319da14caf6c0d8c`  
**Frozen H100 artifact SHA-256:** `daefdac139bd3f6423010b234a4dd680726e8e10312ff6ce0c4655fe7b47200e`

The verifier was independently rerun on H100 for every \(10\le m\le80\); all 71
instances passed.  This supplements the frozen artifact's mixed-parity large values.

## 1. Core and owner ranks

The even interval \(\{12,14,\ldots,2m-2\}\) has \(m-6\) elements.  It is disjoint
from \(\{0,6,9,10,2m-3\}\), so

\[
                         |K_m|=(m-6)+5=m-1.
\]

The two displayed extras in each \(D_i\) are distinct and outside \(K_m\), hence
every \(D_i\) has the required owner rank \(m+1\).  Direct intersections give exactly
the three rank-\(m\) facets in (1.3).

## 2. Literal full-factor adjacency

The two repair hosts are unchanged canonical MSW rows.  Applying the same root-local
construction audited for the parity-tail theorem gives their complete cyclic owner
windows.  In the first host, \(D_0D_1\) is the old edge flanking repair step 4; in
the second, \(D_2D_3\) is the old edge flanking repair step 5.  The relative repair
changes the step-4 colour \(K_m+2\) to the edge \(D_1D_2\) and does not list either
boundary colour among the changed labels.

The replay applies every endpoint rotation, then verifies degree two on every owner
appearing in the touched full rows.  It checks

\[
 D_0-D_1-D_2-D_3
\]

as literal factor edges, not merely pairwise Johnson adjacencies.  All moving endpoints
belong to the reconstructed touched rows, and the relative trade preserves their
global degrees, so no unexamined row can add a third edge at \(D_1\) or \(D_2\).
This validates the full-factor scope.

## 3. Residence obstruction

Coordinate \(2\) is absent from \(K_m\), hence its word on the quartet is exactly

\[
                         0,1,1,0.
\]

Both flanking zero owners are adjacent to the two one owners.  The positive run is
therefore maximal in the global cyclic chronology and has length exactly two.  The
factor fails positive \(q\)-residence for every \(q\ge3\), independently of all
other components or source choices.

## 4. Boundary-touch and conjugation

If the three **coloured edges** in (1.3)—meaning their endpoint pairs at those facet
colours—remain unchanged, the degree-two condition forces the same four-owner path and
the same two-run.  This is now stated explicitly in Corollary 3.  A colour by itself
always remains present under an endpoint rotation, so the endpoint-pair condition is
the necessary local invariant.

Coordinate conjugation transports set membership, intersections, adjacency, and run
lengths.  Thus a conjugate packet has the same `0110` witness on
\(\gamma(2)\).  If packet interfaces are mutually edge-disjoint, each packet retains
its own three-edge witness; fusions supported elsewhere cannot change it.  Hence any
such family retains at least one positive two-run per packet and cannot be positive
\(q\)-resident for \(q\ge3\).

This does not obstruct an overlapping multi-terminal trade which deliberately changes
a boundary edge or the repair splice.  The source states that escape exactly and does
not overclaim a universal residence impossibility.
