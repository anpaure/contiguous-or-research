# The `k=17` 6,281-piece SCD bank fails integrated seam Hall

**Date:** 2026-08-01  
**Status:** authenticated finite theorem for the frozen canonical
`resident_pieces.json` segmentation.  Both the raw and deliberately relaxed
necessary-residence seam atlases are audited with the missing lower palette
and the complete rank-10--15 upper-hole bank in the same atoms.  This does not
rule out alternative minimum cuts, interior splitting/rethreading, or a
different SCD factor.

## 0. Outcome

The authenticated SCD construction partitions all 24,310 rank-nine owners
into 6,281 internally depth-three-factorable paths.  Their interiors use
18,029 distinct rank-eight lower colours and leave exactly

\[
                             6281                               \tag{0.1}
\]

missing lower colours.  Their complete internal interval-OR deck leaves
6,273 upper targets of ranks 10 through 15:

\[
\begin{array}{c|rrrrrr}
\text{rank}&10&11&12&13&14&15\\ \hline
\text{holes}&1419&2454&1655&608&122&15.
\end{array}                                                    \tag{0.2}
\]

The 1,419 rank-ten holes are exactly the distinct q1 values killed by the
1,419 residence cuts.

There are 6,280 joins in a linear ordering of the 6,281 pieces, hence the
upper count has apparent scalar spare seven.  The exact incidence audit
shows that this spare is illusory.

* Even before residence, after requiring the seam intersection to be one of
  the 6,281 missing lower colours, 70 rank-eleven and two rank-twelve holes
  have no seam provider.
* Under a relaxed **necessary** residence predicate, 1,749 lower colours,
  453 tail blocks, 453 head blocks, and 2,052 upper targets have no candidate.
* In particular, 720 of the 1,419 cut-killed rank-ten tickets are zero.
* The necessary-residence block tail--head matching has size only
  `5747/6281`, whereas a linear braid needs 6,280 joins.
* The near-square upper-target--seam projection has matching size only
  `4141/6273`.

Thus the frozen 6,281-piece SCD bank cannot be completed by choosing an order
and orientation of its existing pieces.  Different cuts, further interior
splits, a global rethread, or whole seam gadgets are required.

## 1. Exact integrated seam atlas

For every physical piece `B`, retain both orientations `B^+` and `B^-`, even
when they coincide on a singleton.  An oriented raw seam

\[
                         e=(B^\sigma,D^\tau)                   \tag{1.1}
\]

is admitted exactly when:

1. `B` and `D` are different physical pieces;
2. the final owner of \(B^\sigma\) and first owner of \(D^\tau\) are distinct
   Johnson neighbours; and
3. their rank-eight intersection is one of the 6,281 colours absent from the
   piece interiors.

Condition 3 is essential.  A seam using an already consumed lower colour
cannot participate in a coefficient-one q1 reassembly.

For every admitted seam, enumerate all unions

\[
 \left(\bigcup\text{a suffix of }B^\sigma\right)
 \cup
 \left(\bigcup\text{a prefix of }D^\tau\right).               \tag{1.2}
\]

Every value in the upper-hole bank supplied by (1.2) is attached to the same
seam atom.  This is the exact two-piece crossing-interval support; no bounded
ray truncation is used.

### 1.1 Necessary residence filter

For an oriented block `B` and coordinate `x`, let `pre_B(x)` and `suf_B(x)`
be its positive prefix and suffix lengths, truncated at four, and let
`all_B(x)` mean that the block is all-one in `x`.

For a seam `B|D`, if neither block is all-one in `x`, impose

\[
\begin{array}{c|c|c}
x\in\operatorname{last}(B)&x\in\operatorname{first}(D)&
\text{necessary condition}\\ \hline
1&1&\operatorname{suf}_B(x)+\operatorname{pre}_D(x)\ge4,\\
1&0&\operatorname{suf}_B(x)\ge4,\\
0&1&\operatorname{pre}_D(x)\ge4.
\end{array}                                                    \tag{1.3}
\]

If either block is all-one, impose no condition: an arbitrarily chosen future
or previous block is allowed to rescue the run.  Hence every seam in any
globally depth-three-resident assembly belongs to this filtered atlas.  Empty
rows after this relaxation are genuine obstructions, not artifacts of a
greedy local closure rule.

## 2. Raw projection census

The integrated raw atlas contains

\[
                            243998                              \tag{2.1}
\]

oriented seam atoms.  All 6,281 missing lower colours have positive degree,
and every physical piece has some incoming and outgoing orientation.  Exact
maximum matchings are

\[
\begin{array}{c|r}
\text{projection}&\text{matching size}\\ \hline
\text{tail piece--head piece}&6281\\
\text{tail piece--lower colour}&6281\\
\text{lower colour--head piece}&6281\\
\text{tail state--head state}&11284/12562\\
\text{tail state--lower colour}&6281\\
\text{lower colour--head state}&6281.
\end{array}                                                    \tag{2.2}
\]

So the owner/lower layer is projection-perfect before residence.

The upper rows are not.  Their singleton census is

\[
\begin{array}{c|rrrrrr}
\text{rank}&10&11&12&13&14&15\\ \hline
\text{zero targets}&0&70&2&0&0&0\\
\text{minimum positive degree}&2&2&2&8&42&230\\
\text{maximum degree}&108&110&200&356&444&702.
\end{array}                                                    \tag{2.3}
\]

The upper-target--seam matching has size `6197/6273`; the additional four
units beyond the 72 zero rows are ordinary projected Hall deficiency.  The
tail-piece--upper and upper--head-piece matchings are each `6191/6273`.
Most sharply, the lower-colour--upper-target projection has size only

\[
                             4986/6273.                         \tag{2.4}
\]

Therefore the exact lower palette and complete upper bank are already
incompatible on this atomic piece face, even with residence ignored.

## 3. Necessary-residence projection census

The relaxed residence filter leaves 85,080 atoms.  Its lower and block
singleton failures are

\[
\begin{array}{c|r}
\text{quantity}&\text{value}\\ \hline
\text{zero lower colours}&1749\\
\text{zero outgoing physical pieces}&453\\
\text{zero incoming physical pieces}&453\\
\text{zero outgoing oriented states}&3522\\
\text{zero incoming oriented states}&3522.
\end{array}                                                    \tag{3.1}
\]

The exact projection matchings collapse to

\[
\begin{array}{c|r}
\text{projection}&\text{matching size}\\ \hline
\text{tail piece--head piece}&5747/6281\\
\text{tail piece--lower colour}&4532/6281\\
\text{lower colour--head piece}&4532/6281\\
\text{tail state--head state}&8091/12562\\
\text{tail state--lower colour}&4532/6281\\
\text{lower colour--head state}&4532/6281.
\end{array}                                                    \tag{3.2}
\]

The lower matching values equal the number of nonzero lower rows, but the
piece tail--head projection has a further Hall deficiency: `6281-5747=534`.
A linear braid may omit only one tail and one head, so its required 6,280
joins are impossible on this atlas by 533 units.

The upper singleton census is

\[
\begin{array}{c|rrrrrr}
\text{rank}&10&11&12&13&14&15\\ \hline
\text{zero targets}&720&990&307&35&0&0\\
\text{minimum positive degree}&2&2&2&2&2&38\\
\text{maximum degree}&86&72&80&104&118&174.
\end{array}                                                    \tag{3.3}
\]

There are therefore

\[
                       720+990+307+35=2052                    \tag{3.4}
\]

upper holes with no direct provider even in the necessary relaxation.  The
upper-target--seam matching is only

\[
                             4141/6273,                         \tag{3.5}
\]

80 below the 4,221 nonzero rows.  The tail-piece--upper and
upper--head-piece matchings are both `4003/6273`, and the correlated
lower-colour--upper matching is `3272/6273`.

### 3.1 The cut-killed rank-ten bank

Raw q1-compatible seams support all 1,419 rank-ten tickets, with degrees from
two to 108.  Necessary residence leaves only

\[
                             699/1419                           \tag{3.6}
\]

supported, with positive degrees from two to 86.

An earlier audit which ignored whether the seam intersection was a missing
lower colour found 322 necessary-residence-zero rank-ten targets.  The
integrated number 720 therefore contains an additional

\[
                             720-322=398                        \tag{3.7}
\]

targets whose only resident providers reuse an already consumed lower
colour.  This quantifies the exact lower/upper correlation missed by the
separate marginal atlases.

## 4. Verdict on the seven-spare identity

The identity

\[
                 6280\text{ joins}-6273\text{ upper holes}=7 \tag{4.1}
\]

is scalar only.

It fails on this fixed bank in two independent ways:

1. even raw q1-compatible seams leave 72 upper rows empty; and
2. necessary residence leaves 2,052 upper rows empty and cannot even form a
   6,280-edge path on the physical pieces.

The injection matching `upper target -> seam atom` is a useful near-square
projection but is not itself necessary, because one physical seam can deliver
several upper targets.  The singleton zeros in (2.3) and (3.3), however, are
unconditional within the frozen atomic-bank model.  No sharing of seams and
no allocation of the seven scalar spare joins can serve a target with no
provider.

## 5. Reproducible artifacts and scope

The standalone C++20 audit is

```text
scratch/audit_k17_scd_6281_oriented_seam_hall_20260801.cpp
SHA256 9b82d76c77cdc88e8467557c8f6928b24aaae7623dc47c2239058f721e312998
```

The retained output, including every zero lower and upper mask, is

```text
scratch/k17_scd_6281_oriented_seam_hall_20260801.out
SHA256 6963a23790a958b55bc98d395ead5de84b402b243b9908dff8320c68ff71e356
```

The authenticated input is

```text
scratch/ad_k17_scd_multicomponent_20260801/resident_pieces.json
SHA256 f1e8ca31601e5e4af4430a33b453faa78133701da374f4d73dbe3c405791913b
```

The audit was compiled and run on H100 with
`g++ -std=c++20 -O3 -DNDEBUG` and ends in

```text
PASS_K17_SCD_6281_ORIENTED_SEAM_HALL
```

This theorem closes only the frozen canonical 1,419-cut atomic-piece basin.
It leaves alternative minimum transversals, additional splits, changes of the
SCD forest, non-atomic seam/socket gadgets, and a global protected rethread
open.  In particular, it is not a lower bound on `nu(17)`.
