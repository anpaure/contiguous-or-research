# K17 complement-dual support-ten residence hyperedge correction

Date: 2026-08-01  
Lane: H2 independent literal replay  
Status: **support ten remains source-relative UNSAT, but the published 219
boundary-pair proof is invalid and must not be cited.**

## Scope

The frozen source is
`scratch/threadD_k17_complement_dual_splice_20260801/seed.best.tsv`, SHA-256
`a3f9eac037ae66a460349b12d578a31222afe1a7d168da641e77967a44ddbab3`.
Support means changed quotient successor tails; a same-head phase change counts
as changed.  This note does not enumerate support ten and says nothing about
another seed or unrestricted K17.

## Correction

The boundary-pair claim in
`MATH_AUDIT_H2_K17_COMPLEMENT_DUAL_SUPPORT10_CONNECTOR_AND_RESIDENCE_GATE_20260801.md`
is not sound.  A changed successor tail strictly inside a physical
`0 1^ell 0` run can destroy the run even when its entering and leaving tails
are unchanged.  Hence pairwise-disjoint *boundary pairs* do not give a
hitting-set lower bound, and the number 219 is withdrawn.

For a short run beginning at physical position `s`, define instead

\[
 E_{s,\ell}=\{\tau_{s-1},\tau_s,\ldots,\tau_{s+\ell-1}\},
\]

where `tau_i` is the quotient tail owning the physical successor arc out of
position `i`.  These are exactly the arcs of
`0 -> 1^ell -> 0`.  If support misses `E_{s,ell}`, the complete literal
subpath remains, possibly under one common deck rotation, and therefore some
coordinate still has a positive run of length `ell<4`.

For an even more conservative certificate, add the following-zero tail:

\[
 \bar E_{s,\ell}=E_{s,\ell}\cup\{\tau_{s+\ell}\}.
\]

Every residence repair must hit `E_{s,ell}` and hence also
`bar E_{s,ell}`.  Thus pairwise-disjoint closed spans still certify distinct
required support tails.

## Independent replay

The reconstructed primitive large lift has 24,293 distinct physical owners
and voltage 4 modulo 17.  Its short positive runs are exactly

```text
length 2: 1190
length 3: 3128
```

After quotient-tail deduplication:

| hypergraph | distinct edges | edge sizes | deterministic disjoint packing |
|---|---:|---|---:|
| minimal outgoing-arc spans `E` | 254 | `3^70 4^184` | 173 |
| closed vertex spans `bar E` | 254 | `4^70 5^184` | 151 |

The packing algorithm repeatedly takes a minimum-size, minimum-current-
conflict edge with lexicographic tie-breaking.  No optimality is asserted.
The audit JSON freezes eleven pairwise-disjoint closed spans, each replayed as
the literal bit-0 pattern `0,1,1,0`.  Eleven already imply that no support of
size at most ten can repair residence.  The larger counts are reproducible
diagnostics, not exact transversal numbers.

Therefore the corrected scoped theorem is:

> Every floor-four residence repair of this frozen complement-dual seed that
> is expressed by changed quotient successor tails has support at least 11
> (indeed the frozen packing certifies at least 151).  Consequently the exact
> support-ten face is residence-UNSAT before topology, voltage, J7, or palette
> rows.

## Artifacts

```text
scratch/audit_h2_k17_complement_dual_support10_residence_hyperedges_20260801.py
scratch/h2_k17_complement_dual_support10_residence_hyperedges_20260801.audit.json
```

The checker independently reconstructs the atlas, complement dual, successor
permutation, physical lift, every cyclic short run, both corrected
hypergraphs, and both deterministic packings.  It does not invoke the
support-ten DFS.
