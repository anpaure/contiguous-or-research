# K16 S4 two-interacting-local-block census

Date: 2026-07-30  
Lane: AD  
Status: **source frozen and syntax-audited; census not executed**

## Frozen source and provenance

Enumerator:

`scratch/search_ad_k16_s4_two_interacting_local_blocks_20260730.cpp`

SHA-256:

`62b4dec55394daa1fca0014271d687e15c87e28c3bc5b4721b34d947ba37ad9e`.

Input manifest:

`scratch/ad_k16_s4_two_interacting_local_blocks_20260730.INPUTS.sha256`

SHA-256:

`d055557d75e871c5cf8215e277b823dabcaab484b76c568fe6512465fa5b2240`.

The source passes a warning-clean C++20 syntax audit.  It was not executed.

The frozen antecedent is

`scratch/s4_exact229_swap6608_12714_l3_20260730.targets`

with SHA-256

`955dc2fb350cd399f050e4dafb481925633e0024eaa438ee3cf4f984e0acb995`.

It is middle-exact with capacity 32063, has no zero maximal envelope, and has
the single unrestricted upper hole `4e79`.  Its generalized lower Hall graph
has matching 26308 and deficiency 24.

## Exact source lineage

Starting from exact229, S4 changes precisely six positions:

```text
[6608,6611): ce38 cc3c cc2e  -> 4e78 4e3c 4c3e
[12714,12717): 4e78 4e3c 4c3e -> ce38 cc3c cc2e
```

Thus it is exactly the forward exchange of two length-three blocks.  The
exact229 `A+B` relocation has net zero length before both sites, so their
origin labels are respectively bad2 rows `6608..6610` and `12714..12716`.
The binary reconstructs bad2 -> exact229 -> S4 row-for-row before searching.

## Complete bounded face

On S4 choose two disjoint equal-length intervals

\[
I=[i,i+\ell),\qquad
J=[j,j+\ell),
\]

where

\[
3\le\ell\le16,qquad 0\le j-(i+\ell)\le6.
\]

Exchange their contents without moving an intervening row.  The block placed
at either slot may independently be forward or reversed.  The gap bound is
exactly the complement of the earlier strict-halo separation: the two
depth-three dependency halos interact.

An operation is admitted only when its actual changed-position support is at
least six.  This excludes all support-at-most-four cases and, conservatively,
the entire support-five layer rather than attempting to distinguish a
possibly broader unprotected support-five subclass.  The resulting exact
labelled catalogue size is

\[
5,037,984.
\]

This is complete for equal-length exchanges with lengths 3--16, gap 0--6,
four orientations, and support at least six.  It does not cover unequal
blocks, length at least 17, gap at least seven, overlapping blocks, arbitrary
row substitutions, or any long interval shift.

## Local-to-global middle theorem

### Lemma

Suppose a proposed block exchange leaves the equality indicator

\[
[T_r=T_{r+1}]
\]

unchanged at every affected adjacency.  Let (d_r) be the frozen S4 dynamic
depth.  It is enough to replay rows from three positions before the first
changed row through the largest source position touched by a changed row.
If every maximal envelope in this range is nonzero and every replayed row is
exact, then the complete middle chronology is exact.

### Proof

Unchanged equality indicators give the identical global depth sequence
((d_r)).  A changed target row (r) can alter only source envelopes at
positions (r,ldots,r+d_r).  Hence the program takes the union of these
positions over both blocks.  A row can see this union only if its start lies
at most three positions before its first point and no later than its last
point.  The stated replay range contains exactly this safe superset.

For every source position (p) in the range, the program recomputes

\[
P_p=\bigcap_{r\le p\le r+d_r}T_r
\]

directly from the proposed word, and then checks

\[
T_r=\bigcup_{p=r}^{r+d_r}P_p.
\]

Every envelope and row outside the range has exactly its old defining target
set, hence is unchanged from S4.  This proves global exactness.  The emitted
candidate is nevertheless subjected to a second full middle replay; any
disagreement aborts the run rather than being classified as a negative.
□

Every middle survivor receives unrestricted upper interval-OR replay.  Only
upper-complete words are emitted.  Deduplication uses a compact disk bucket
but compares all 12,873 rows on every equal digest, so a hash collision cannot
discard a distinct word.  Each emitted file is ready for independent full
Hall replay; the enumerator itself makes no Hall claim.

The current outcome is UNKNOWN because the H100-only census has not run.

