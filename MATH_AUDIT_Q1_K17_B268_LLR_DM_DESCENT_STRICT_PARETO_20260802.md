# Q1 audit: authoritative `b268` LLR transfer and DM-descent strict Pareto table

**Date:** 2026-08-02  
**Status:** exact finite positive theorem on the authoritative `b268` target
parent.  A protected `437`-transfer table strictly improves the parent in
both measured socket phases, their intersection and union, and exact supplier
rank.  This is not a common occurrence-labelled state, chronology, compiler,
or `k=17` word.

## 1. Parent and scope correction

The parent in this audit is

```text
scratch/k17_phase0_retained_witness_private_basis_20260802/
  private_h_outer_materialized.tsv
SHA-256 b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
```

This is the same parent on which the `1,748` private phase-0 tickets were
authenticated.  The transfer catalogue excludes the deduplicated union of
all ticket short, predecessor-host, successor-host, nonnegative
predecessor-token, and nonnegative successor-token row IDs: `7,213` physical
rows in total.  Hence every selected-ticket row retains its exact `b268`
value.

This corrects the earlier warm47 experiment.  There, the same `7,213` row IDs
had been transplanted from the `original.res1972.tsv` private-ticket artifact
onto a different target table.  Its numerical supplier/price measurements
remain exact warm47 calibrations, but it is not a common-parent private-ticket
construction and must not be called `full-private`.

## 2. Exact structural supply on `b268`

The literal phase-0 socket summary has `4,708` zero short roles.  Of these,
`4,013` are low-rank `LR` rows eligible for the exchange

\[
 (L<M<R)+(U<Q)\longmapsto(M<R)+(L<U<Q),\qquad L\subset U.
\]

Before ticket-row protection there are `116,384` containment edges and the
maximum row-disjoint matching has size `2,983`.  After excluding all `7,213`
native ticket rows, the exact catalogue has

\[
 93,234\text{ edges},\qquad
 \nu_{\rm structural}=2,831.
\]

Its structural Hall shore is `1,461/279`, of deficiency `1,182`.  This is a
matching obstruction to transferring all `4,013` roles at once, not an
obstruction to a large useful protected subfamily.

The protected catalogue is

```text
scratch/root_k17_b268_llr_transfer_matching_20260802/protected.all_edges.tsv
SHA-256 30fac2b299c353446024a83fb93525d66e6b6720eacbd1895db68c5544598c89
```

## 3. Two marginal phases and a `464`-edge common matching

Every protected structural edge was priced exactly after its paired
`LR+LMR -> LLR+MR` replacement.

The first phase is literal: it uses the `b268` owner masks themselves.  The
second uses the root-aligned `round047.s7.phase1` owner table.  The latter is a
transported-opening marginal; a carrier-opening transport theorem is not
asserted.

The exact marginal census is

```text
protected structural edges                           93,234
native b268 phase-0 positive                         23,342
transported phase-1 positive                         25,173
positive in both phases                              11,893
maximum row-disjoint matching in the intersection       464
```

Materializing that `464`-matching and then repricing the complete table, not
merely summing marginal edge scores, gives

```text
table                phase0   phase1   both   either   supplier rank/16898
b268 baseline          2687     1891   1422     3156        16796
common464              3119     2274   1864     3529        16767
```

Thus the raw `464` table gains `442` common-positive short roles but initially
costs `29` supplier ranks.

## 4. Exact DM-guided descent

The supplier graph of `common464` has `105` zero heads and deficiency `131`.
Exactly `19` of those zero heads are newly created selected `LLR` heads.
Undoing their transfers produces a `445`-transfer table:

```text
selected   phase0   phase1   both   either   supplier deficiency
445          3104     2260   1848     3516          107
```

Its recomputed maximum-deficiency shore is `135/28`.  Exactly eight selected
new `LLR` heads lie in that shore.  Undoing those eight produces the final
`437`-transfer table:

```text
selected   phase0   phase1   both   either   supplier rank   deficiency
437          3097     2252   1838     3511        16801           97
```

The new supplier shore is `111/14` and contains no selected new `LLR` head,
so the rule "undo every selected transfer whose new head lies in the current
maximum shore" has reached a local fixed point.

For comparison, the broader deletion of the three selected right-hand `MR`
supplier rows in the preceding neighbor shore gives deficiency `99`, worse
than the head-only table.  It is not the retained incumbent.

## 5. Strict Pareto theorem

### Theorem

On the authoritative `b268` target parent, there is a row-disjoint set of
`437` protected `LLR` transfers whose materialized table has

\[
 (P_0,P_1,P_{\cap},P_{\cup},r_{\rm supplier})
   =(3097,2252,1838,3511,16801).
\]

The baseline tuple is

\[
 (2687,1891,1422,3156,16796).
\]

Therefore the new table strictly improves every displayed coordinate, by

\[
 (+410,+361,+416,+355,+5).
\]

Every one of the `7,213` physical row identities named by the authenticated
private ticket bank is unchanged.

#### Proof

The `437` selected exchanges form a row-disjoint matching in the protected
`11,893`-edge two-phase intersection.  Each exchange preserves the global
target partition and changes only its two named rows, so materialization is
literal and the excluded ticket rows are unchanged.

The two complete DNF replays independently enumerate all `7,395` short rows
of the materialized table, giving the first four coordinates.  The generalized
supplier replay constructs every admissible row-pair edge, computes a maximum
matching of size `16,801`, and independently returns the exact shore
`111/14`; this gives the fifth coordinate.  Comparing with the same three
replays on `b268` proves the coordinatewise strict inequalities.  No marginal
additivity assumption is used.  \(\square\)

## 6. Zero-head anatomy

The baseline has `94` zero supplier heads.  The final table has `82`, all of
which are surviving `LMR` heads:

```text
inherited baseline-zero LMR heads       66
newly zero surviving LMR heads           16
new selected LLR zero heads               0
total                                    82
```

Thus `28` baseline zero heads have either been activated or removed, while
only `16` previously nonzero surviving heads become zero.

A transfer changes the flag menus of exactly its left and right rows.  It
also replaces the old right-row hard-head requirement by the new left-row
requirement whenever those bottoms are hard.  Consequently its direct
supplier effect is confined to two outgoing supplier rows and two head
columns, although the maximum matching and DM shore respond globally.

## 7. Frozen artifacts

The final artifact folder is

```text
scratch/q1_k17_b268_llr_dm_descent_20260802/
```

Key files and hashes are

```text
b268_llr.protected.common464_undo27dm.selected.tsv
  e9704b820222d93f56bcbf348d202651f2ace1082e1fb65eb6c21fce88d2db25
b268_llr.protected.common464_undo27dm.table.tsv
  b6a51766dd8c7632a79f1f60abea26deced8cc5f40aec952bc8b704a3600c2b6
b268_llr.protected.common464_undo27dm.native_phase0.dnf.tsv
  9a872ae53f11289beee64388c2425e7257bdbf0a0e00a77cbd2cce6f10915e61
b268_llr.protected.common464_undo27dm.transported_phase1.dnf.tsv
  2449d317e8efc2c461551ed32a224194575ed6c9f2de90587fdde36d5d5b9e47
b268_llr.protected.common464_undo27dm.projection.audit.json
  2a5a5263c41d5b8fada2b26e8a97a6cccc4ae05ce70a579d71ced8e6dd6ef1e4
audit.json
  recorded in MANIFEST.sha256
```

Relevant source hashes are

```text
scratch/audit_root_k17_b268_llr_transfer_matching_20260802.cpp
  6d635776bb5efa913b084ab61590a9a4a02062c6399fa56b009355ce63c973f6
scratch/price_k17_llr_transfer_new_mr_20260802.cpp
  282d4784318e42fc82969825cd6acf3045815aab8e6508b8121b91cc081f59b3
scratch/match_k17_priced_llr_edges_20260802.cpp
  0d48e2b9d81d4a55f09648918161adfc19dabf979bf6c6909ce022ad0e49d124
scratch/materialize_k17_llr_socket_matching_20260802.cpp
  3df48c73246f34a0b76674365e4d9a08c537cea8793557f713325c59fc720d25
scratch/audit_k17_arbitrary_table_supplier_projection_20260802.cpp
  7a10575d892737120c06641bd405fdfd0fe20a5907615ed2c528d5a4ab836914
```

## 8. Exact remaining scope

This theorem closes a real same-parent correlation row: one protected table
simultaneously improves both measured socket palettes and the supplier
matching.  It does **not** yet provide:

* an exact replay of the residual complete outer matching after target-row
  exchanges;
* one occurrence-labelled state shared by the two marginal phase prices;
* a proof that the transported phase-1 opening belongs to the same carrier;
* chronology, residence, complete upper shadows, common cap, lower compiler,
  or a universal `k=17` word.

Those are the gates that separate this strict Pareto table from an improved
upper bound for `nu(17)`.
