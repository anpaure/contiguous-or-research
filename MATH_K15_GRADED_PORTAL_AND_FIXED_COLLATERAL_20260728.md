# The graded Hall-22 portal and its fixed collateral

Date: 2026-07-28

Status: exact H100 census, independently materialized carrier certificate, and
matching/shadow audit.  This note proves that the desired local DM circuit can
be split physically, but every two-braid realization in the complete
neutral-first catalogue creates a larger Hall shore elsewhere.  It does not
prove a length-6438 word.

## 1. Native grading

For a fully interior depth-`d` resident Johnson carrier of rank `r`, let

\[
 P_j=\bigcap_{i=j-d}^{j}T_i.
\]

The deletions in every `d` consecutive transitions are distinct: otherwise
one coordinate would have to re-enter and then leave in an internal positive
run shorter than `d+1`.  Hence

\[
 |P_j|=r-d,
 \qquad |P_j\triangle P_{j+1}|=2.
\]

The same argument makes the controller additions distinct across every
compiler window, so for `0<=s<d`,

\[
 \left|P_j\cup\cdots\cup P_{j+s}\right|=r-d+s.                 \tag{1.1}
\]

At `k=15`, `(r,d)=(8,3)`: interior native traces have ranks `5,6,7`
at depths `0,1,2`.  Thus neither a depth-zero native `2575` nor a
depth-one native `2607` is physically possible.  The grade-compatible split
of the remaining circuit must be

\[
 \boxed{\text{depth one: }2575,qquad\text{depth two: }2607.}   \tag{1.2}
\]

## 2. The complete neutral-first portal census

Start from

```text
scratch/k15_segment_braid_hall22_zero6.json
```

with Hall deficiency `22`, six zero targets, and DM circuit

\[
 \{2575,2607\}\quad\text{versus one depth-two cell}.           \tag{2.1}
\]

There are `682` distinct nontrivial protected-neutral first states.  On the
H100 CPU, their complete second signed-three-cut neighbourhoods contain

```text
375,282,842 Johnson-valid braids
  8,164,534 residence-valid braids
  6,224,656 all-upper-safe braids
         10 grade-compatible portals (1.2).
```

All ten portals have the same controller motif, up to reversal,

\[
 (2567,2574,2604)quad\text{or}\quad(2604,2574,2567),           \tag{2.2}
\]

because

\[
 2567\cup2574=2575,qquad
 2567\cup2574\cup2604=2607.                                   \tag{2.3}
\]

They all preserve the exact middle deck, Johnson chronology, depth-three
residence, and every upper support layer.  They also all have the identical
lower-hole vector

\[
 (6,20,6,1,0,0,0),                                             \tag{2.4}
\]

Hall deficiency `25`, and eight zero targets.

## 3. Exact signed collateral

Relative to the Hall-22 base, every portal loses precisely

\[
 \begin{array}{c|c}
 \text{lower depth one}&719,2667\\
 \text{lower depth two}&591,2603,2665
 \end{array}                                                    \tag{3.1}
\]

and gains the desired lower-depth-two support `2575`.  No upper support is
lost.  Thus the circuit split itself succeeds, but its fixed seam collar
creates two new zero targets and a stronger remote Hall shore.

The representative route is

\[
 H22\xrightarrow{\operatorname{FF}(872,4524,4738)}H22
 \xrightarrow{\operatorname{FF}(378,967,4680)}H25_{\rm portal}.
                                                                    \tag{3.2}
\]

The full common-core audit gives deficiencies

\[
 22\longrightarrow22\longrightarrow25                         \tag{3.3}
\]

and cross-shore gap matrix

\[
 \begin{pmatrix}
 22&22&21\\
 22&22&21\\
 20&20&25
 \end{pmatrix}.                                                  \tag{3.4}
\]

Equation (3.4) is the key diagnosis: the old deficient shore really improves
from gap `22` to `21`, while a new gap-`25` shore appears.  The local splitter
is therefore correct; only compensation is missing.

## 4. Portal-preserving third moves

Across all ten portal carriers, exhaustive enumeration gives

```text
5,484,833 Johnson-valid third braids
  119,994 residence-valid braids
   91,293 all-upper-safe braids
       82 portal-preserving outputs, including identities
       22 nontrivial portal-preserving outputs.
```

Every nontrivial output still has at least six immediate-lower holes.  Their
exact score classes are

```text
Hall 25 / zero 9: 4
Hall 26 / zero 9: 7
Hall 28 / zero 10: 4
Hall 29 / zero 10: 7.
```

None restores any member of the fixed lost sets (3.1).  Their best exact
compiler score is therefore Hall `25`; their best zero count is `9`.
Consequently no single third braid both retains some graded portal (1.2) and
compensates its collar.

In fact the statement is stronger: none of the 22 genuine portal-preserving
braids gains **any** lower support at depths one or two.  Eleven leave both
support sets unchanged; the other eleven delete two depth-one supports and
two or three depth-two supports.  Hence this entire one-braid neighbourhood
is support-nongaining in precisely the layers where compensation is needed.

The unfiltered third-neighbourhood scans also finish negatively.  For each of
the ten portal states there is exactly one Hall-22/zero-six/lower-hole-four
output, and it is the inverse repair which destroys the portal and returns to
the neutral first state.  No third move reaches Hall 21.  Thus the physical
portal is a genuine but uncompensated excursion, not a hidden monotone descent.

This does **not** rule out a third braid which destroys this portal and wins
through a different DM component, nor a longer route which temporarily loses
and later recreates (1.2).  It proves that the next positive move must treat
the portal and the opposite signed shadow vector as one compound object.

## 5. Reproducibility

Representative states and exact audit:

```text
scratch/k15_h22z6_portal_router_0077.json
scratch/k15_h22z6_graded_portal_0077.json
scratch/audit_k15_h22z6_graded_portal_0077.json
scratch/k15_h22z6_graded_portal_census.json
```

Search sources:

```text
scratch/search_k15_segment_braid_native.cpp
scratch/search_k15_graded_portal_native.cpp
scratch/run_k15_h22z6_portal_beam_h100.sh
```

The generic independent auditor is
`scratch/audit_k15_segment_braid_descent.py`.
