# Independent audit: diagonal dual-role two-boundary capacity dichotomy

**Date:** 2026-08-03  
**Audited theorem:**
`MATH_THEOREM_DIAGONAL_DUAL_ROLE_TWO_BOUNDARY_CAPACITY_DICHOTOMY_20260803.md`  
**Audited theorem SHA-256:**
`7a913cb0aee28ff716e16747eb08643eb90c57b340bfedc6c1339875cfdd2049`  
**Verdict:** **GO after one necessary scope correction.**  No finite search
or computer-assisted mathematical claim is used.

## 1. Necessary correction

The first draft defined

\[
 P_i=\bigcup_{j=i+1}^{i+d}A_j=T_i\cap T_{i+1}
\]

for arbitrary nonempty source letters.  The equality is false without a
q1-exact overlap hypothesis: a coordinate in a boundary letter can recur on
the opposite side of the cut and enlarge the intersection beyond the
interior union.

The theorem has been corrected to assume explicitly that the row is on the
flat q1-exact face:

\[
 |T_i|=r,qquad |P_i|=r-1,qquad P_i=T_i\cap T_{i+1}.
\]

The literal addresses

\[
 p_i=[i+1,i+d]_W,quad o_i=[i,i+d]_W,quad q_i=[i,i+d+1]_W
\]

are now also stated explicitly.  This correction is load-bearing for the
interpretation of `p_i`, `o_i`, and `q_i` as consecutive q1 port, owner, and
upper-turn roles.  The later capacity count itself uses only these fixed
literal chains and their occurrence labels.

## 2. Audit of the four literal chains

Put

\[
 T_i=\bigcup_{h=i}^{i+d}A_h,qquad
 P_i=\bigcup_{h=i+1}^{i+d}A_h,qquad
 R_i=T_i\cup T_{i+1}.
\]

The four chronological chains and their two newly exposed boundary
occurrences are:

\[
\begin{array}{c|c|c}
\text{chain}&\text{first extension}&\text{second extension}\\
\hline
p_i-o_i-q_i
 &P_i\cup A_i=T_i
 &T_i\cup A_{i+d+1}=R_i\\
p_i-o_i-q_{i-1}
 &P_i\cup A_i=T_i
 &T_i\cup A_{i-1}=R_{i-1}\\
p_i-o_{i+1}-q_i
 &P_i\cup A_{i+d+1}=T_{i+1}
 &T_{i+1}\cup A_i=R_i\\
p_i-o_{i+1}-q_{i+1}
 &P_i\cup A_{i+d+1}=T_{i+1}
 &T_{i+1}\cup A_{i+d+2}=R_{i+1}.
\end{array}
\]

Hence the theorem's source-label table is exact:

\[
 (a_i,a_{i+d+1}),\quad
 (a_i,a_{i-1}),\quad
 (a_{i+d+1},a_i),\quad
 (a_{i+d+1},a_{i+d+2}).
\]

The q1 hypothesis also makes each semantic step proper: adjacent owners
have rank `r`, intersection rank `r-1`, and union rank `r+1`.

## 3. Distinctness and alias audit

The range

\[
                         2\le d<W-2
\]

implies `W>=5`, `1<=d+1<=W-2`, and all of `d`, `d+1`, `d+2` are strictly
less than `W`.  Therefore:

* the two source indices in each row above are distinct modulo `W`;
* `i` and `i-d-1` are distinct modulo `W`;
* the fixed-length cyclic addresses `p_i`, `o_i`, and `q_i` are separately
  injective in `i`;
* the port intervals have length at least two, so none aliases a one-cell
  source occurrence; and
* the owner and upper-turn intervals have different lengths from ports and
  sources.

Equal set values at different addresses do not coalesce physical occurrence
capacity.  The theorem consistently works with occurrence addresses rather
than value vertices.

## 4. Unit-source cut

Every admitted length-two chain uses two distinct unit source occurrences.
If a family is pairwise capacity-disjoint, its source-occurrence pairs are
pairwise disjoint.  A family of size `x` therefore consumes `2x` members of
the `W`-element source bank, so

\[
                         x\le\left\lfloor W/2\right\rfloor.
\]

This is an exact resource cut for the four-chain literal model.  It is not
a semantic Hall obstruction, and it does not apply if source labels are
declared unpriced.  The theorem states both limitations.

## 5. Capacity-two load and occurrence disjointness

For the canonical family

\[
                         p_i-o_i-q_i,qquad i\in\mathbb Z_W,
\]

path `i` uses source occurrences `a_i` and `a_(i+d+1)`.  A fixed `a_h`
therefore appears exactly on paths

\[
                         i=h,qquad i=h-d-1.
\]

Section 3 shows these path indices are distinct.  Thus every source has
load exactly two.  The port, owner, and upper-turn addresses are each
injective in `i`, so every one of those occurrence resources has load
exactly one.  Giving source occurrences capacity two and all other
displayed occurrence resources capacity one therefore makes the complete
family feasible.

This verifies exact capacity, not just average capacity or a fractional
relaxation.

## 6. Private-attachment corollary

After the correction, the compressed attachment is explicitly required to
consume **no** source occurrence.  The lower step of path `i` then uses only
`a_i`; these are injective across `i`.  If the attachments are pairwise
private and each owner remains an available transit vertex, all source,
port, owner, attachment, and upper-token capacities are unit-disjoint.

The corollary is conditional on a literal attachment.  It does not infer
such an attachment from the abstract owner-to-upper perfect matching.

## 7. Scope of the positive conclusion

The capacity-two and private-attachment constructions are valid only on the
declared dual-service face:

* an owner occurrence may simultaneously retain its owner role and serve as
  the unique transit vertex of its route; and
* an upper-turn occurrence may retain its declarative upper-witness role
  while serving as that route's terminal.

If the common-cap convention reserves or deletes owner capacity, these
positive linkages fail unless a private owner bypass is supplied.  Likewise,
the theorem does not prove transported background compatibility, product
closure for two occurrence coordinates, guards, regeneration, or an
all-dimensional dual-role ticket.  It proves exactly the following local
dichotomy:

\[
\begin{array}{c}
\text{canonical literal two-boundary lift with unit sources}
\Longrightarrow \operatorname{rank}\le\lfloor W/2\rfloor,\\[2mm]
\text{the same lift with source capacity two}
\Longrightarrow \text{full rank on the dual-service face},\\[2mm]
\text{private source-free owner attachments}
\Longrightarrow \text{full rank with unit sources}.
\end{array}
\]

Within this corrected scope, every stated identity and capacity claim is
valid.
