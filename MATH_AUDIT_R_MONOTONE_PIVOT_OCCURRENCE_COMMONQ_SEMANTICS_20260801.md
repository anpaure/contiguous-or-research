# Independent audit: monotone pivot occurrence and common-Q semantics

Date: 2026-08-01  
Verdict: `VALID WITH EXPLICIT RELEASE/STATE HYPOTHESES`  
Scope: local monotone insertion and compiler rows only; no physical
Pascal/PBBS host-existence claim.

## 1. Valid core

For an insertion

\[
        \cdots,Q_L\mid Q_R,\cdots
        \longmapsto
        \cdots,Q_L,X,Q_R,\cdots,
        \qquad X\subseteq Q_L\cup Q_R,
\]

the monotone convex-hull map `Phi` is a literal injection on all old
interval addresses and preserves every OR.  In the width-`h` band, exactly
the `h-1` maximal crossing cells escape to width `h+1`; the complement of
the retained image is exactly the singleton pivot and two rays, of total
size `2h-1`.

Let `M_0` be the old target-to-cell matching.  If `U` is the set of actual
old target vertices moved to ray cells, `D` is the set of genuinely new
target vertices, and \(\psi:U\mathbin{\dot\cup}D\to F_X\) is an injective literal ray
assignment, then

\[
       \psi\ \dot\cup\
       \Phi\bigl(M_0|_{L\setminus U}\bigr)
\]

is one exact matching iff every retained old edge remains band/guard
admissible.  No background Hall theorem remains because `F_X` is the exact
cell complement.

For the prepared common-core packet \(X\subseteq Q\), every non-singleton ray
mask is an old one-sided target.  All `2h-2` such logical vertices must be
released, not counted as fresh.  The singleton `X` is released if old and is
otherwise the sole fresh target.

## 2. Common-Q verdict

The combined matching is one exact common-`Q` matching, not merely a set of
separately legal edges, precisely when one fixed state exports:

* the complete inserted word and pivot owner windows;
* the old/new interval map, escaped cells and fan addresses;
* target IDs/values, old matching addresses, release set and ray assignment;
* pointwise lower bounds and caps;
* every row's target, live address interval and frozen exterior; and
* every non-value occurrence guard after transport.

If that literal inserted word realizes the complete row family between the
declared lower bounds and caps, the componentwise maximal intersections are
nonempty and reconstruct every row.  This is a direct sufficient
certificate for one common-`Q` state.  The displayed maximal-intersection
criterion in the main theorem is also necessary.

Two marginal phase matchings are not enough.  Common addresses must use the
intersection of both phase row families; private addresses need an exported
common/private partition and separate phase maximal letters under one cap.

## 3. Corrections made during audit

1. Both rays are private under monotone `Phi`, not under one canonical
   full-block grouping.  Grouping `X` with the left old letter puts the left
   ray in the full-block image; grouping right is symmetric.  Such cells are
   usable only after their old matching edges are released.
2. Logical target identities are explicit.  In the ordinary compiler there
   is one vertex per mask; repeated equal-mask ray rows are redundant
   equations, not extra matching edges.  A genuine occurrence multiset must
   export distinct IDs and enough equal-valued cells.
3. Rank saturation is sufficient to make all `h-1` escaped cells unusable by
   any strict-lower matching.  For one fixed matching the exact condition is
   merely avoidance/admissibility of those cells.
4. The singleton collision is included: if `X` is already an old target, it
   belongs to the release set.
5. Exact-width/address/trace guards are not implied by OR preservation.  A
   retained crossing cell grows by one position and needs an explicit guard
   transition or rehosting.
6. The complete owner-window list, including endpoints and rank/adjacency
   data, is exported.  Interior rank saturation alone does not certify it.

## 4. Sharp failures

Omitting any of the following breaks the claim:

* omission of \(X\subseteq Q_L\cup Q_R\): the adjacent crossing OR changes;
* release: one target vertex receives both its old and packet matching edge;
* escaped-cell avoidance: a retained width-`h` edge exits the band;
* target IDs: equal-mask multiplicities are miscounted;
* cap/lower/row state: a cap can omit a required element of `X`;
* guard map: value survives while width/address chronology fails; or
* owner state: a new `(h+1)`-window can have rank below the middle layer.

## 5. Independent replay

The independent formula replay checks all depths `2<=h<=64` and directly
enumerates every interval address.  It verifies the exact complement,
release/recombination matching, and one simultaneous maximal common-`Q` row
family on generic tagged words.

```text
scratch/audit_r_monotone_pivot_occurrence_commonq_20260801.py
scratch/r_monotone_pivot_occurrence_commonq_20260801.audit.json
```

The older `audit_monotone_pivot_insertion_ray_repair` is not evidence for
this stronger semantic statement: it checks only a particular support/ray
instance and lies on a rank-obstruction face.  The new replay was written
specifically to audit occurrence transport, releases, both fan shores and
maximal common-`Q` reconstruction.
