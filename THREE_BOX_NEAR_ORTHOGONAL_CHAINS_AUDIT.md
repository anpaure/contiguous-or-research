# Audit of the near-minimum orthogonal chain partitions

## 1. Verdict

The theorem in `THREE_BOX_NEAR_ORTHOGONAL_CHAINS.md` is correct:

\[
                    |\mathcal L|=W_m,
             \qquad |\mathcal R'|=W_m+m,
\]

and the two displayed families are orthogonal chain partitions of
`[0,m]^3`.  The inner-label rechaining covers every original right-chain
piece exactly once, every new `Q_(i,j)` is a chain, and the count is exactly
`+m`.

The proof of Lemma 1 in the source is too compressed to be independently
checkable as written: “separate four minima” suppresses the essential label
calculation.  Section 3 below supplies a direct complete derivation and
confirms the claim.

Non-saturation of the new `Q` chains is harmless.  Endpoint classes of
witness intervals need only be chains under inclusion; arbitrary-mask array
entries naturally allow skipped ranks.

This theorem clears a necessary orthogonal-chain-count gate, not the OR-word
problem.  A converse to the endpoint-chain theorem is false without ordered
triangular support, within-chain precedence, and coordinatewise label
realization.  None of those three properties follows from the present
rechain.

## 2. Hook-chain formulas

For the `xz` square, define the standard hook path of inner label `i` by

\[
 K_i(t)=
 \begin{cases}
   (t,i),&0\leq t\leq m-i,\\
   (m-i,t-m+2i),&m-i\leq t\leq2(m-i).
 \end{cases}                                                \tag{2.1}
\]

The coordinates here are `(x,z)`.  The right chain `R_(i,j)` is

\[
\begin{split}
 &\{(K_i(j)_x,y,K_i(j)_z):0\leq y\leq m-j\}\\
 &\quad\cup
 \{(K_i(t)_x,m-j,K_i(t)_z):j<t\leq2(m-i)\}.          \tag{2.2}
\end{split}
\]

It is nonempty exactly for

\[
                         0\leq j\leq\min(m,2(m-i)).  \tag{2.3}
\]

Equations (2.1)--(2.2) follow immediately from

\[
 i_R=\min(z,m-x),\qquad j_R=\min(t_R,m-y).
\]

They also prove that every fiber is a saturated symmetric chain.  Swapping
`y` and `z` gives the left fibers.  The number of nonempty labels is

\[
 \sum_{i=0}^m\bigl(\min(m,2(m-i))+1\bigr)=W_m,
\]

so both original hook families are SCDs of minimum size.

## 3. Complete double-intersection calculation

An intersection of `R_(i,j)` with a left chain is exactly an occurrence of
that left label along the right chain.  We now list those labels.

### 3.1 Triangular labels

Suppose `i+j<=m`.  Then `j<=m-i`, so `K_i(j)=(j,i)`.  The first segment of
`R_(i,j)` consists of

\[
                         (j,y,i),\qquad0\leq y\leq m-j.
\]

Its left labels are

\[
                         (y,j),qquad0\leq y\leq m-j. \tag{3.1}
\]

On the horizontal part of the second segment,

\[
 (x,y,z)=(t,m-j,i),qquad j<t\leq m-i,
\]

the first left label is `m-t`, which decreases strictly, and the second is

\[
                         \min(2t-j,m-i).              \tag{3.2}
\]

These labels cannot repeat one another, cannot meet (3.1) because their
second coordinate is strictly greater than `j`, and can meet the following
vertical part only at first coordinate `i`; at that endpoint their second
coordinate is `m-i`.

On the vertical inner part,

\[
 (x,y,z)=(m-i,m-j,z),qquad i<z\leq m,
\]

the left labels are

\[
                         (i,m-z),qquad i<z\leq m.    \tag{3.3}
\]

They are distinct.  The only possible intersection between (3.1) and (3.3)
is the label `(i,j)`.  It occurs at

\[
 u_{i,j}=(j,i,i)
\]

in (3.1), and at

\[
 v_{i,j}=(m-i,m-j,m-j)
\]

in (3.3), precisely when `i+j<m`.  If `i+j=m`, these formulas describe the
same hook corner and there is only one occurrence.

### 3.2 Labels outside the triangle

If `i+j>m`, then `j>m-i`, so the inner point `K_i(j)` lies on its vertical
part.  Put

\[
                         k_0=2m-j-2i.
\]

The first segment has left labels

\[
                         (y,k_0),qquad0\leq y\leq m-j,
\]

and the second has labels

\[
                         (m-j,k),qquad0\leq k<k_0.
\]

The two ranges are disjoint and internally injective.  Thus there is no
repeated left label outside the triangle.

Combining the two cases proves:

* every `L`/`R` pair intersects at most twice;
* the only double has identical label `(i,j)` with `i+j<m`; and
* its two points are exactly `u_(i,j)` and `v_(i,j)`.

This is Lemma 1 with all cases exposed.  An independent exact evaluation of
the label maps for `1<=m<=40` agrees with the formulas; it is only a sanity
check.

## 4. Prefix and suffix labels

For `i+j<=m`, the cut point `u_(i,j)` lies on the first segment (3.1).  The
prefix through it consists exactly of

\[
                         (j,h,i),qquad0\leq h\leq i,
\]

and hence has the left labels

\[
                         \{(h,j):0\leq h\leq i\}.     \tag{4.1}
\]

Every remaining point on the first segment has first left label at least
`i+1`; the horizontal inner segment has first label `m-t>=i`; and the final
vertical segment has first label exactly `i`.  Therefore every suffix label
has first coordinate at least `i`.  Section 3 shows that neither piece has an
internal repeated label.  Lemma 2 is correct.

## 5. Rechaining formulas and coverage

For `Q_(i,j)=P_(i,j) union S_(i+1,j)`, the lower prefix ends at

\[
                         u_{i,j}=(j,i,i).
\]

If `j<m-i-1`, the cut in `R_(i+1,j)` occurs before the outer hook corner, so
the first suffix point increments its `y` coordinate:

\[
                         (j,i+2,i+1).
\]

If `j=m-i-1`, the cut is the outer corner and the next step increments `z`:

\[
                         (j,i+1,i+2).
\]

Both dominate `(j,i,i)`, proving `Q_(i,j)` is a chain.  It may skip one rank,
which is allowed.

The pairing range

\[
 0\leq i\leq m-2,qquad0\leq j\leq m-i-1
\]

uses every listed prefix and suffix at most once: prefixes have inner label
`i`, while suffixes have inner label `i+1`.  The special reunion at `(0,m)`
uses neither a listed prefix nor suffix.  All remaining pieces are explicitly
left unpaired, so the construction is a partition—no point is lost or
duplicated.

For orthogonality, (4.1) gives first left-label coordinate at most `i` on the
prefix, while Lemma 2 applied to `S_(i+1,j)` gives first coordinate at least
`i+1` on the suffix.  Their label sets are disjoint.  Every label is already
internally unique on each piece, so no new chain meets a left chain twice.

## 6. Exact count

The triangular family has

\[
                         T={ (m+1)(m+2)\over2}
\]

right chains.  Cutting produces `2T-1` nonempty pieces: every prefix is
nonempty, and the only empty suffix is `S_(m,0)`.

The number of `Q` pairings is

\[
 \sum_{i=0}^{m-2}(m-i)=2+3+\cdots+m
                      ={m(m+1)\over2}-1.
\]

The reunion at `(0,m)` makes one additional merge, so the total number of
merges is `m(m+1)/2`.  The net increase over the original `T` chains is

\[
 (2T-1)-{m(m+1)\over2}-T=m.
\]

Every chain outside the triangle is unchanged, proving exactly

\[
                         |\mathcal R'|=W_m+m.
\]

The formulas also hold in the boundary case `m=1`, where the `Q` range is
empty and the special reunion supplies the only merge.

## 7. Relevance to contiguous OR words

Given one selected witness per target, grouping by common left and right
physical endpoints produces two orthogonal chain partitions.  Thus the new
pair has the correct necessary chain counts for a prospective word of length
`W_m+O(m)`.

The converse needs three additional theorems:

1. order the left and right chains so every occupied incidence cell lies in
   the physical triangle `left<=right` with only `O(m)` padding;
2. make target inclusion along every chain agree with the required endpoint
   precedence in both directions; and
3. realize every occupied cell by coordinatewise OR labels without
   contaminating other cells.

Orthogonality alone proves none of these.  The non-saturated `Q` chains are
acceptable—the endpoint-chain normal form never requires saturation—but the
claim that their triangular label geometry has `O(m)` bandwidth remains a
conjectural next step.

