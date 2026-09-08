# Exact229 fixed-envelope Hall and endpoint-locality audit

**Date:** 2026-07-30  
**Scope:** independent replay of `exact_229.targets`; no claim about a downstream Boolean compiler or unenumerated exchanges.

## Theorem (audited exact status)

Let (T) be
`scratch/ad_k16_bad2_splitpair_exact_20260730/exact_229.targets`, SHA-256
`cae23cfcedbc9d193ebd9191045edd0e5c14f56af5fc96a802b8cefa7cd7e974`.
Then:

1. (T) has length (12873), with its three flat repetitions at expanded
   positions (6320,12869,12871).  After collapsing those repetitions it has
   (12870) states.
2. Its maximal monotone envelope is everywhere nonempty, has exactly (32063)
   proper-prefix compiler cells, and the arbitrary-width accumulated-union
   upper oracle has zero missing targets.
3. The fixed-envelope lower Hall graph has (26332) left targets, (32063)
   right cells, and (347875) incidences.  An explicit matching of size
   (26307) is valid and vertex-disjoint.  An explicit shore (U) has
   
   \[
   |U|=212,\qquad |N(U)|=187.
   \]
   
   Therefore the maximum matching has size exactly (26307), and the exact
   Hall deficiency is (25).
4. The induced shore graph has exactly (25) connected components, every one
   of deficiency one.  Its component histogram ((|L|,|R|,δ)^{\#}) is
   
   \[
   (1,0,1)^{12},(3,2,1)^2,(4,3,1)^3,(6,5,1),(7,6,1),
   (15,14,1),(18,17,1),(23,22,1),(34,33,1),(35,34,1),(44,43,1).
   \]
   
   The unmatched-rank histogram is (24) rank-seven targets and the isolated
   rank-one target `0x8000`.

The lower bound in item 3 is independently checked edge by edge.  The upper
bound is the literal shore-neighbour census, not a solver status; consequently
the equality and deficiency are certificate-level statements.

## Exact support-five geometry

Relative to
`scratch/root_k16_a_fourtoken_q1hole_direct_moves_20260730/best_upper_complete_bad2.targets`,
the candidate deletes

```text
1265-1266, 1294-1295, 2185-2186, 2216-2217, 3845-3846
```

and inserts

```text
1265-1295, 1266-3846, 1294-2216, 2185-2217, 2186-3845.
```

The collapsed source segments, in candidate order, are

| source interval | length | orientation |
|---|---:|---|
| (0\ldots1265) | 1266 | forward |
| (1295\ldots2185) | 891 | forward |
| (2217\ldots3845) | 1629 | forward |
| (2186\ldots2216) | 31 | forward |
| (1294\ldots1266) | 29 | reverse |
| (3846\ldots12869) | 9024 | forward |

Thus the two advertised inserted blocks are exactly the 31-state forward block
and the 29-state reverse block; the five joins are the complete support-five
macro, not independent local replacements.

## Literal endpoint columns

For each new join, the audit records the six states on either side and their
entire prefix/suffix OR chains.  The compact boundary signatures are:

| expanded boundary | source join | endpoint masks | six-left OR | six-right OR |
|---:|---|---|---|---|
| 1266 | (1265\to1295) | `6b68 -> 636c` | `6ffe` | `7b7d` |
| 2157 | (2185\to2217) | `2d1d -> 2f2c` | `2fbf` | `3fef` |
| 3786 | (3845\to2186) | `6879 -> 691d` | `6efd` | `6dff` |
| 3817 | (2216\to1294) | `3f28 -> 6768` | `7f3b` | `7f7e` |
| 3846 | (1266\to3846) | `6ba8 -> 6b29` | `6fee` | `7bf9` |

All twelve recorded depth entries around every join equal three.  Moreover,
none of the (187) *current* shore-neighbour cells starts in any join's exact
dependency interval ([c-5,c+5]).  This is a statement about the present
shore graph: a future edit can create new neighbours there, but it cannot
claim any already-present local neighbour from this census.

## Occurrence-profile and locality lemma

For a fixed envelope and a proper-prefix cell (J=[s,s+\ell)), let

* (U_J) be the OR of the allowed envelope masks in (J);
* (M_J) be its forced/mandatory mask; and
* (P_p) be the maximal envelope at each (p\in J).

Then a shore target (S) is adjacent to (J) if and only if

\[
M_J\subseteq S\subseteq U_J,
\qquad S\cap P_p\ne\varnothing\quad(p\in J).
\]

For COMP3, the complete profile at start (s) depends only on target/depth
rows ([s-6,s+5]).  Hence:

* changing one row (k) affects only starts ([k-5,k+6]); two such supports
  are disjoint at separation at least (12);
* changing one seam (c) affects only starts ([c-5,c+5]); two seam supports
  are disjoint at separation at least (11).

Consequently, with the flat/depth phase and shore (U) fixed, the signed
neighbour-count currents of separated columns add exactly.  This does **not**
assert that maximum-matching changes add: alternating paths may couple remote
components after the columns are installed.  A safe pre-Hall score is therefore

\[
\Delta_U=|N_{\rm new}(U)\setminus N_{\rm old}(U)|
          -|N_{\rm old}(U)\setminus N_{\rm new}(U)|,
\]

computed from the literal occurrence profiles.  Any exact completion against
this fixed shore must have Δ_U at least (25); only then is reoptimizing the
full matching potentially decisive.

## Reproducibility

Auditor:
`scratch/audit_threadD_k16_exact229_hall25_independent_20260730.py`, SHA-256
`2cc5ab7b770120bcf9e728afb54184b74098c1ede43fcfeaad35f61198c90f63`.

The final capped H100 replay used one CPU, exited zero in 6.33 seconds, and
reached 66664 KiB maximum RSS.  It also checked fail-closed that the Hall shore
lies in the rank-one-through-seven universe and that the stored unmatched list
and rank histogram equal the complement of the explicit matching.  The
principal output hashes are:

```text
165c6cdd19f2ad349b5bc9787f7f1f81a93d301525f84743f149676e64f590ff  exact229.audit.json
b8ec1fcf49cc746c9532e6fd47f55b30559dfa80d07e402892c9c7f61eae49c8  exact229.envelope
4336652e38dc9127b04809cbb1507682d16085b3672b860442f2b72e1fff0e00  exact229.shore_profiles.tsv
```

The audit payload hash (canonical JSON with the hash field removed) is
`82534ab571a3e187333965c4808ce5a8c773926fff36c07d9c6ca7f4490ea5d8`.
