# `k=17`: occurrence-labelled mobile fan / bounded-Hall separator on the 3,664 q1 residuals

**Date:** 2026-08-02  
**Lane:** D, proof-safe finite audit  
**Status:** frozen exact q1-only separator; independent structural replay and full/core DRAT cross-check pass

## Frozen input and contract

The input is the 3,664 visible/clean-9923 `EXACT_BUILD` banks in the authenticated round02 semantic-filter union.  For each fixed one-recut anchor, the audit reconstructs the complete selected q1 atom atlas and applies the second recut by an exact occurrence-coordinate delta.  The final atom count is checked against an independent complete bank evaluation for every row.

An atom records its immutable ordered tail and head owner traces, endpoint orientations, and literal rank-eight colour.  The positive resources are the complete outgoing-piece, incoming-piece, and selected-colour rows.  Two different atoms are blocked only by one of the native q1 reasons:

1. a common outgoing resource;
2. a common incoming resource;
3. a common selected-colour resource; or
4. contradictory orientations of one physical occurrence-labelled piece.

The fourth blocker is the one-resolution consequence of the two literal atom-to-orientation implications.  No degree equality, mask equality as occurrence identity, sampled exterior compatibility, or mutable rebuilt-piece identity is used.

## Separator searched

For each final bank the audit includes every provider row in its exact changed/interface region, every row named by the decoded primary and alternate stored semantic cores, and the registered bow-tie/dual-fan colour rows.  Within each of the outgoing, incoming, and colour shores it exhausts every two-row subset; on banks not already rejected by a pair, it then exhausts every three-row subset.

A two-row rejection exports both complete provider rows and one literal blocker provenance record for every Cartesian provider pair.  A three-row rejection would analogously export a blocker for every provider triple.  This is a direct finite certificate for Theorems 5.1 and 7.1 of `MATH_THEOREM_A_K17_FINAL_PROVIDER_BOUNDARY_LANGUAGE_AND_FUNCTIONAL_HALL_SEPARATOR_20260802.md`.

## Exact result

The separator gives

\[
3664 = 61\ \texttt{MOBILE\_FAN\_UNSAT} + 0\ \texttt{HALL3\_UNSAT}
       + 3603\ \texttt{UNDECIDED}.
\]

All 61 certificates are selected-colour fans.  They are exactly the 30 residuals at anchor 6 and the 31 residuals at anchor 8.  Each maps the alternate stored fan to the final occurrence-labelled colour rows

\[
  6964\leftrightarrow 35786,\qquad 6830\leftrightarrow 35275,
\]

whose complete final provider degrees are respectively 4 and 8.  Thus each certificate contains 12 providers and all (4\cdot8=32) blocked pairs.  Frozen totals are:

| item | exact count |
|---|---:|
| occurrence-labelled provider records | 732 |
| blocked provider pairs | 1,952 |
| outgoing AMO blockers | 488 |
| incoming AMO blockers | 488 |
| orientation-resolution blockers | 976 |
| selected-colour AMO blockers | 0 |

The independent replay checks all 1,952 Cartesian entries, the resource/orientation provenance of each entry, the rank-eight mask represented by each colour-row identifier, and the case/job/anchor/bank-key bijection.  It also checks the retained production full-proof and trimmed-core DRAT logs for all 61 banks; all 122 logs contain `s VERIFIED`.

## Why one common exterior language is not useful here

The exact union of objects changed across the 3,664-bank family meets:

| shared interface component | union size | fraction of the 7,612-row shore |
|---|---:|---:|
| outgoing rows | 6,892 | 90.54% |
| incoming rows | 6,892 | 90.54% |
| orientation pieces | 6,892 | 90.54% |
| selected-colour rows | 4,925 | 64.70% |

It spans 470 partner bases, 33,582 removed atom coordinates, and 89,266 added atom coordinates.  Therefore a single exact exterior boundary language shared by all 3,664 banks is not materially smaller than the q1 formula.  Materializing it would be a near-full decision computation, so it was correctly not placed in front of the already-running exact portfolio.  The 61 rejections instead need no exterior approximation: their complete final rows are blocked by native literal clauses alone.

## Scope boundary

`MOBILE_FAN_UNSAT` is an exact UNSAT statement for the native q1 orientation/outgoing/incoming/selected-colour formula.  `UNDECIDED` has no positive meaning.  The scan found no three-row Hall certificate in its stated interface/core region.  No claim is made here about rank-ten rows, connectivity, exact global residence, ranks 11--17, rooted state, topology, or the compiler.

The frozen artifact root is:

`/home/amodo/or15/work/threadD_k17_mobile_hall3664_20260802`

See `INDEX.tsv` and `SHA256SUMS` there for the replay entry points and adopted hashes.
