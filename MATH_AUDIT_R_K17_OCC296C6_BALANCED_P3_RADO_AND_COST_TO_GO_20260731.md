# Independent audit: occurrence296+C6 guarded cut and balanced P3 cost-to-go

Date: 2026-07-31  
Verdict: **PASS with explicit scope corrections**

This audit checks
`MATH_THEOREM_R_K17_OCC296C6_BALANCED_P3_RADO_AND_COST_TO_GO_20260731.md`.
It uses independent literal reconstruction where available and proves the
structural statements separately from the finite census.

## 1. Source authentication — PASS

The frozen owner cycle has 24,310 distinct rank-nine owners and SHA-256

```text
a47aa9d7c8b86ca3912c8c82262969332727d27bf427ee8783ccb1a8ce664b49.
```

The H2 and H4 independent payloads agree on one cycle, exact lower q1,
marked size 4,108, D2/D3 503/503, replay rows/bits 748/776 and upper holes
1585/824/116 in ranks 10--12.  Their audit SHAs are respectively
`fc6716d...` and `0bca08d7...` as listed in the theorem.

## 2. Old-cut survival — PASS, fibre-specific

The 1,160-C6 history changes the residual lift but not the occurrence base
or ordered macro interiors.  Therefore the 296 component-interior strict
runs are literal invariants of every subsequent residual-\(U\) circuit.
The 177 target set was computed in a support superset of all such residual
circuits; all 177 remain holes at the new checkpoint.  Thus the empty
neighbourhood proof is valid for arbitrary compound length inside that
fibre.

The proof does **not** extend the 296 run rows to complement exchanges.
This correction is essential: those packets rethread physical owner edges.

## 3. P1/P2/P3 structure — PASS

For a primitive column \(e\to f\), zero owner boundary is equivalent to
equality of the old and new endpoint multisets, hence to a trivial column.
So P1 is empty.

For P2, colour the two old edges red and the two new edges blue.  Opposite
boundaries give equal red/blue degrees.  After common-edge cancellation the
nontrivial case is an alternating C4.  If its red edges are \(AB,CD\) and
blue edges \(AC,BD\), the two incidences of the first exchange imply
\(B\cap C=L_p\), while those of the second imply \(B\cap C=L_q\).
Thus the lower colours agree, contradicting uniqueness of the old edge in a
lower-rainbow factor.  The empty/reverse case forces the same equality
directly.  This independently proves the no-P2 lemma.  The exact catalogue
confirms 545,721 distinct boundaries and zero opposite pairs.

For support-two columns, boundary is the incidence boundary of a directed
endpoint arc.  A loopless Eulerian digraph with exactly three arcs and no
balanced two-arc subgraph is a directed triangle.  The P3 normal form is
therefore correct.  The binary catalogue header and records independently
give 28,114 triangles, 14,243 disconnected reconnections and 13,871
one-path packets.

## 4. Rank-ten Rado audit — PASS with hyperpacket warning

Independent script:

```text
scratch/audit_k17_occ296c6_balanced_p2_p3_rank10_independent_20260731.py
SHA  a625d6fc8f41fecfc52213dbf12f755313eb1d8c271e77ad67274fee7066b2d3
```

Output:

```text
scratch/k17_occ296c6_balanced_p2_p3_rank10_independent_20260731.audit.json
SHA  de1e812ce472954a9875b787ecec00dc6117af77a3dca02aeeb4804c2098ff2e
```

It reconstructs all packet gain/loss sets and verifies:

| row | exact value |
|---|---:|
| P3 packets | 13,871 |
| direct-service packets | 4,074 |
| service incidences | 4,599 |
| covered / zero rank-ten rows | 1,462 / 123 |
| one-credit matching rank | 1,459 |
| loss-free positive packets | 1,292 |
| old-177 covered / zero | 151 / 26 |

The 123 and 26 zero-row sets are the exact empty-neighbourhood sets in the
relevant unguarded frozen **atomic candidate relations**, and lower bounds
after any guard pruning.  The exact guarded zero sets may be larger.  They
are not no-gos for
synergistic compounds with nonlinear target effects.  Likewise the matching
deficiency 126 is **not** a physical packet no-go: the nonzero 6/3 core
consists of three packets which each serve two targets.  The theorem
correctly labels it a unit-credit serialization obstruction only.

The 26-row decimal list has 26 distinct entries and its canonical JSON hash
is `1b41458e...`.  Direct hexadecimal conversion agrees with the theorem.

## 5. Packet 584 literal replay — PASS

The independent checker was strengthened to difference the literal upper
target sets and test membership in the old 177-set:

```text
scratch/audit_k17_opt28_balanced_p3_best_independent_20260731.py
SHA  059a8f6973b97df05b2ce6b62aad132c40982ebe284e3f260727b54d4490d4e8

scratch/k17_opt28_occ296_c6_balanced_p3_exact_20260731.independent.audit.json
SHA  641cf08a1557e11f8a5792ace7362beefd1f11085f0f9ebb745180c8d3dbccb0
payload 18956dd3879040a37a56ca9955dff3273dc99eed757f3e3344d8d682a318a7c8
```

It verifies the declared three cuts, three removed and three added edges,
owner-degree balance, one cycle, exact lower palette and literal marked
path.  Aggregate run/envelope/replay metrics agree before and after.
Literal target differences through rank 12 are exactly

```text
rank10 gained: b73a,1173b,1333e; lost: none
rank11 gained: b73b,1333f;       lost: none
rank12 gained: none;             lost: b73f
```

The old-177 intersection is exactly `{0x1173b}`.  This corrects an earlier
informal subagent statement that all three rank-ten gains belonged to the
old cut.  The theorem uses the independently checked value.

The signed potential derivative
\(-3w_{10}-2w_{11}+w_{12}\) follows immediately and has no hidden
probabilistic or independence assumption.  It is not a physical action
cost.  For physical cost \(a\), the corresponding reduced Bellman cost is
\(a+\Delta\Phi\), exactly as stated in the corrected theorem.

## 6. Common-cap and sequential scope — PASS fail-closed

The numerical host and envelope values are exact, but they are not an exact
common-cap matching.  The checkpoint still has 776 missing inverse row
bits, so the common guard family is empty upstream.  The theorem never
promotes the proxy to common-cap feasibility.

The packet audit enumerates upper targets only through rank 12.  Therefore
it does not establish preservation of ranks 13+ protected witnesses; the
theorem now states this fail-closed.

Likewise, all Rado cuts are for a frozen atomic candidate relation.  Applying
one P3 packet changes chronology and may change the provider catalogue, and
two atoms can have a synergistic target effect absent from either singleton.
The 123 and 26 zero sets therefore do not exclude such compounds,
regenerated P3, mixed support-four triples, P4 packets, or longer circuits.
The final scope statement is correct.

## 7. Final verdict

The decisive statements are valid:

1. rank zero on 473 obligations survives exactly in the fixed pure
   residual-\(U\) fibre;
2. arity three is the first possible and actual balanced packet layer;
3. its unguarded frozen support-two atomic service projection has exact
   rank-zero sets 123 globally and 26 from the old target cut, giving lower
   bounds under guard pruning;
4. packet 584 is a literal scalar-threshold-preserving signed provider arc
   through rank 12 with projected-potential derivative
   \(-3w_{10}-2w_{11}+w_{12}\).

No accepting K17 state, common cap, compatible packet covering theorem, or
dimension-uniform contraction is established.
