# Two enriched positions are necessary and sufficient for the split-pivot four-deficit repair

Date: 2026-08-01  
Lane: Thread D / split-pivot literal lower-`q1` repair  
Status: exact linear-source theorem.  Owner and pre-insertion depth rows are
fixed; source positions may only be enlarged, not moved, duplicated, or
inserted.  Full old-deck transparency is not claimed.

## 0. Result

Use the sparse split-pivot source of Section 4 of
`MATH_THEOREM_A_SPLIT_PIVOT_PHYSICAL_COLLAR_AND_BPLUS1_TERMINAL_PATH_20260801.md`,
with

\[
 B=C\mathbin{\dot\cup}X_L\mathbin{\dot\cup}X_R,\qquad
 X=X_L\mathbin{\dot\cup}X_R,\qquad
 x_L\in X_L,\quad x_R\in X_R.                        \tag{0.1}
\]

Allow an existing source letter to be replaced only by a superset, while
requiring both the post-insertion owner row and the pre-insertion depth row
to remain fixed.  Then:

1. no one-position enrichment repairs all four lower-`q1` deficits;
2. two positions suffice; and
3. every two-position repair has one position in each of the banks

   \[
   \begin{aligned}
    H_L&=[h,2h-2]\cup
       \begin{cases}\{h-1\},&|X_R|=1,\\\varnothing,&|X_R|>1,
       \end{cases}\\
    H_R&=[2h+2,3h]\cup
       \begin{cases}\{3h+1\},&|X_L|=1,\\\varnothing,&|X_L|>1.
       \end{cases}                                      \tag{0.2}
   \end{aligned}
   \]

For the always-available interior choices

\[
 p_L=h+j-1\quad(1\le j\le h-1),\qquad
 p_R=2h+s\quad(2\le s\le h),                           \tag{0.3}
\]

the inclusion-minimal replacements are

   \[
   \{\lambda_j\}\longmapsto(B-\{x_R\})\cup\{\lambda_j\},
   \qquad
   \{\rho_s\}\longmapsto(B-\{x_L\})\cup\{\rho_s\}. \tag{0.4}
   \]

If `|X_R|=1`, the additional left choice replaces the seam singleton at
`h-1` by `B^-`; if `|X_L|=1`, the additional right choice replaces the seam
singleton at `3h+1` by `B^+`.  Thus the number of minimum position pairs is

\[
 (h-1+\mathbf 1_{|X_R|=1})(h-1+\mathbf 1_{|X_L|=1}).   \tag{0.5}
\]

In the generic case `|X_L|,|X_R|>1` this is `(h-1)^2`.  For `h=2` the
interior pair is `lambda_1,rho_2`, with the displayed seam alternatives
available exactly on singleton shores.

The repair preserves all owners, the complete pre-insertion depth row,
both immediate palettes, the pivot rays, and the owner residence ledger.
It is not transparent relative to the old sparse source deck: already the
one-letter intervals in (0.4) change value.

## 1. Position convention and four deficit intervals

Index the `4h+1` post-insertion source positions by `0,...,4h`, with the
inserted letter `X` at position `2h`.  The owner windows have length `h+1`
and start at `0,...,3h`.

The four deficient shared length-`h` intervals are

\[
\begin{aligned}
 I_1&=[h-1,2h-2], &D_1&=C\cup X_L,\\
 I_2&=[h,2h-1],   &D_2&=X_R-\{x_R\},\\
 I_3&=[2h+1,3h],  &D_3&=X_L-\{x_L\},\\
 I_4&=[2h+2,3h+1],&D_4&=C\cup X_R.                  \tag{1.1}
\end{aligned}
\]

Here `D_i` is the difference between the corresponding owner intersection
and the old shared source union.  The common left and right position banks
are

\[
 I_1\cap I_2=[h,2h-2],\qquad
 I_3\cap I_4=[2h+2,3h].                               \tag{1.2}
\]

They are disjoint.  In the sparse source, the first bank consists exactly
of the singleton positions `lambda_1,...,lambda_(h-1)`, and the second of
`rho_2,...,rho_h`.

## 2. Necessity of two positions

An enrichment can change a shared cell only if its position belongs to that
cell's interval.  Therefore any repair-position set is a hitting set for
`I_1,I_2,I_3,I_4`.

No source position belongs to both a left interval and a right interval:

\[
             \max(I_1\cup I_2)=2h-1
                <2h+1=\min(I_3\cup I_4).              \tag{2.1}
\]

In particular

\[
                         I_1\cap I_2\cap I_3\cap I_4
                             =\varnothing.              \tag{2.2}
\]

Hence one position cannot repair all four deficits.  The deficits
`D_1,D_4` are always nonempty, whereas

\[
 D_2=\varnothing\iff |X_R|=1,
 \qquad D_3=\varnothing\iff |X_L|=1.                   \tag{2.3}
\]

With exactly two positions, one must service all nonempty left deficits
and the other all nonempty right deficits.  Consequently every minimum
hitting set has the form

\[
 \{p_L,p_R\},\qquad
 p_L\in H_L,\quad p_R\in H_R,                          \tag{2.4}
\]

where `H_L,H_R` are given in (0.2).  If `D_2` is nonempty, the left position
must lie in `I_1` intersect `I_2`; if it is empty, any position of `I_1` is
allowed.
The right statement is symmetric.  This proves the lower bound and the
asserted position classification.  A
single physical position could hit all four only after cyclic
identification, copying one occurrence to two addresses, or another change
outside the stated linear fixed-position model.

## 3. Exact simultaneous pre/post caps

For an interior left choice write

\[
 p_L=h+j-1\quad(1\le j\le h-1).                        \tag{3.1}
\]

The post-insertion owner windows containing `p_L` are

\[
 L_{j-1},L_j,\ldots,L_{h-1},M_0,M_1,\ldots,M_{j-1}.
\]

Their exact intersection is

\[
             (B-\{x_R\})\cup\{\lambda_j\}.            \tag{3.2}
\]

After deleting `X`, the pre-insertion windows containing the same position
are

\[
 L_{j-1},\ldots,L_{h-1},U_0,\ldots,U_{j-1}.
\]
They have the same intersection (3.2).  Thus (3.2) is the exact common cap
at `p_L`.  Moreover

\[
 D_1\cup D_2
   =(C\cup X_L)\cup(X_R-\{x_R\})=B-\{x_R\}.            \tag{3.3}
\]

So a one-position repair of both left deficits is possible and forces the
first replacement in (0.4).

When `|X_R|=1`, the only additional candidate is `p_L=h-1`.  Its containing
post and pre cells are all `L_0,...,L_(h-1)`, whose intersection is

\[
                         B^-\cup\{\lambda_1\}.          \tag{3.4}
\]

The old seam letter is `{q^-}` and the only nonempty left deficit is
`D_1=B-{x_R}`.  Hence the inclusion-minimal endpoint replacement is `B^-`;
the extra cap coordinate `lambda_1` is optional but unnecessary.

For an interior right choice write

\[
 p_R=2h+s\quad(2\le s\le h).                           \tag{3.5}
\]

The post-insertion containing owners are

\[
 M_s,M_{s+1},\ldots,M_h,R_0,R_1,\ldots,R_{s-1},
\]

and the pre-insertion containing cells are

\[
 U_{s-1},U_s,\ldots,U_{h-1},R_0,\ldots,R_{s-1}.
\]

Both intersections equal

\[
             (B-\{x_L\})\cup\{\rho_s\}.               \tag{3.6}
\]

Since

\[
 D_3\cup D_4
   =(X_L-\{x_L\})\cup(C\cup X_R)=B-\{x_L\},           \tag{3.7}
\]

the second replacement in (0.4) is possible and forced.

When `|X_L|=1`, the additional candidate `p_R=3h+1` has exact common cap

\[
                         B^+\cup\{\rho_h\}.             \tag{3.8}
\]

Its old seam letter is `{q^+}` and the only nonempty right deficit is
`D_4=B-{x_L}`.  The inclusion-minimal endpoint replacement is therefore
`B^+`; `rho_h` is optional.

Equations (3.2), (3.4), (3.6), and (3.8) prove more than owner legality:
each enriched letter lies below every containing post owner and every
containing pre-insertion depth cell.  Hence both complete depth rows remain
unchanged.

## 4. Exact lower-`q1` repair

Every `p_L` in `H_L` lies in each left interval having a nonempty deficit,
so its new core supplies all required left coordinates.  Every `p_R` in `H_R`
does the same on the right.

No other shared cell overshoots.  Indeed every added coordinate lies in the
intersection of all owner windows containing its position.  If another
shared cell was already tight, that coordinate was already present in its
shared union; otherwise tightness would have failed before the repair.  At
the four exceptional cells, (3.3) and (3.7) supply exactly the displayed
deficits.  Thus every shared cell becomes its owner intersection.

The owner row is unchanged, so its set-valued upper transitions and both
palette-injectivity statements are unchanged.  Every upper transition is
still literal as the union of its two owner windows.

## 5. Rays, old-deck scope, and residence

Delete `X` from the repaired word.  The two letters adjacent to its old cut
are unchanged from the sparse serialization and have union containing
`B`, hence containing `X`.  Reinserting `X` therefore transports every
interval OR of this **repaired preword** exactly.  The insertion-born cells
remain

\[
 X,\qquad B\cup\lambda[h-i+1,h],\qquad
 B\cup\rho[1,i]\quad(1\le i<h),                       \tag{5.1}
\]

because every such interval already contains `X`, and the new core pieces
in (0.4), or their endpoint variants, are subsets of `B` apart from the
already present seam labels.

The owner chronology is unchanged, so the residence/run statement is also
unchanged, including its clipped endpoint qualifications.

There is no transparency from the old sparse source to the repaired source.
For example, at an interior choice the one-letter occurrence at `p_L`
changes from `{lambda_j}` to `(B-{x_R}) union {lambda_j}`; at the optional
endpoint it changes from `{q^-}` to `B^-`.  Thus an incumbent matching
or occurrence ledger on the sparse word must be transported or recomputed.
Likewise, the common caps in Section 3 are only the owner/pre-depth caps;
any additional ambient compiler, boundary, phase, or mixed-exterior row can
shrink them and must be checked separately.

For a label having only one singleton source occurrence, this loss is
structural, not merely an occurrence relabelling.  In a nonempty-letter OR
word, an interval can have value `{alpha}` only if every letter in it is a
nonempty subset of `{alpha}`; hence at least one source letter in that
interval is literally `{alpha}`.  Thus enriching the unique `{alpha}`
letter makes that singleton target impossible unless another literal host
is planted.  The same argument applies to the selected right label.

The canonical Pascal deadline jump is an important exception.  With fresh
labels `lambda'_1=alpha` and `rho'_H=gamma`, its exact block identities are

\[
 E_H^-=(\gamma)E_h^-,\qquad A_H^-=(\alpha)A_h^-,
 \qquad A_H^+=A_h^+(\gamma),\qquad E_H^+=E_h^+(\alpha). \tag{5.2a}
\]

The two-address repair enriches the `alpha` occurrence in `A_H^-` and the
`gamma` occurrence in `A_H^+`, but the far-right block `E_H^+` still
contains a literal singleton `{alpha}` and the far-left block `E_H^-`
still contains `{gamma}`.  Hence the two newborn singleton targets survive
the jump exactly.  No additional singleton host is needed on that step.
On a plateau, or when an old `lambda/rho` label has no second singleton
occurrence, the multiplicity-one obstruction above remains active and must
be checked literally.

### 5.1 Exact cap and guard load

For an interior choice, both new singleton letters have rank

\[
                              |B|=r-h.                 \tag{5.2}
\]

Each is contained in exactly `h+1` post-owner windows and `h+1`
pre-insertion depth windows, and its exact simultaneous cap is the new
letter itself, as proved in (3.2) and (3.6).  Each address belongs to `h`
native lower-`q1` intervals.  Two of those intervals are the formerly
deficient cells; every other one was already tight and therefore absorbs
the enrichment without changing value.  No source position or unit of
physical length is added.

There is also an exact audit rule for every other interval guard.  Put

\[
 \Delta_L=B-\{x_R\},\qquad \Delta_R=B-\{x_L\}.        \tag{5.3}
\]

For every nonempty source interval `I`,

\[
 \operatorname {OR}_{\rm repaired}(I)
 =\operatorname {OR}_{\rm sparse}(I)
  \cup\mathbf1_{p_L\in I}\Delta_L
  \cup\mathbf1_{p_R\in I}\Delta_R.                  \tag{5.4}
\]

Thus only intervals containing one of the two selected addresses need be
replayed, and (5.4) is a necessary-and-sufficient pointwise test for whether
their set value changes.  With `N=4h+1` source positions, the number of
candidate interval addresses is

\[
\begin{aligned}
 G(j,s)={}&(h+j)(3h-j+2)
 +(2h+s+1)(2h-s+1)\\
 &-(h+j)(2h-s+1),                                    \tag{5.5}
\end{aligned}
\]

where the last term removes intervals containing both addresses.  This is
an address count, not a claim that all those OR values change; exact changes
are selected by (5.4).  In particular the two one-letter cells always
change, so a frozen occurrence-labelled compiler has at least two literal
guard obligations.

For a singleton-shore seam choice, use the same formula with
`p_L=h-1`, `Delta_L=C union X_L`, or with `p_R=3h+1`,
`Delta_R=C union X_R`.  Its inclusion-minimal new letter still has rank
`r-h`; the extra `lambda_1` or `rho_h` in the exact cap is optional and is
not charged by the minimal repair.

### 5.2 Three exact repair interfaces

The repair choices form a compiler Pareto menu rather than a strict
address-count ordering.

| interface | enriched positions | selected singleton occurrences lost | unhosted singleton obligations |
|---|---:|---:|---:|
| four-site | the two original non-singleton seam addresses on each shore | 0 | 0 |
| two-site | one `lambda_j` and one `rho_s` address | 2 | 0--2, according to alternate literal hosts |
| hybrid three-site | one singleton address on one shore, two seam addresses on the other | 1 | 0--1, according to an alternate literal host |

The four-site row is the repair of equation (3.1) in the companion theorem:
it never enriches a `lambda` or `rho` singleton, although its four existing
non-singleton cell values and their ambient guards still change.  A hybrid
uses (0.4) on exactly one shore and the corresponding pair of four-site
seam enrichments on the other.  The same cap and shared-block proofs apply
shore by shore, so every row in the table has exact native lower `q1`, the
same owner/pre rows, rays, and residence.  Without literal alternate hosts
for the exported singleton targets, none of the three rows dominates the
others for the terminal compiler.  On the canonical deadline jump, (5.2a)
sets the two-site row's last column to zero; this advantage is not automatic
on plateau steps.

## 6. Conclusion

Within the fixed-position sparse-source model, the minimum number of
enriched positions is exactly two.  The complete minimum family is (0.2)--
(0.4), with the inclusion-minimal endpoint variants of Section 3.  This
minimizes the number of changed addresses for the local lower-`q1` repair.
It is not strictly better than the four-position interface: in a Pascal
jump it deletes two selected singleton occurrences, although the canonical
jump supplies remote copies and therefore loses no newborn singleton
target.  Plateau and old-label uses still require a literal multiplicity
audit.  The global address-transport, singleton-host, and common-cap gates
remain separate.

## 7. Independent replay

The uniform proof is accompanied by an exact finite audit.  It reconstructs
the sparse source for four different split-size profiles, tries every
interior pair `(j,s)`, and verifies the post row, pre row, native lower and
upper `q1`, both rays, local pre/post caps, and residence:

```text
scratch/audit_threadD_split_core_two_address_repair_20260801.py
  SHA-256 c9832e18bbe946112ee6737dc41ea85b1bed6e4522c6d23481ed527d135c22f5
scratch/threadD_split_core_two_address_repair_20260801.audit.json
  SHA-256 23768d4abd3a1e33f95c4517512f83a383fb9333656716c5c68b956ee516a490
  payload  94684b0d0faae135aeb1b852e622703a48efccc9fdb9ddeca7bfa7918309ac07
```

The stored run covers `2<=h<=64`, `252` split-core fixtures, and all
`341376` interior `(j,s)` choices.  It has zero native-`q1` and residence
defects.  The singleton-shore seam alternatives are proved directly by the
cap identities (3.4) and (3.8); they are not silently inferred from the
interior census.
