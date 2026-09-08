# Three consecutive sensitive windows obstruct every pair-shared K2,2 tag weave

Date: 2026-08-01  
Lane: AD, owner-disjoint physicalization of the V4 four-octagon relation  
Status: exact arbitrary-support no-go for the four pair-shared tag rails.  It
does not exclude private tags or a nonlocal tagged ambient embedding.

## 0. Result

Let the four duplicate block occurrences be the vertices of

\[
 K_{2,2},\qquad E=\{02,03,12,13\},                     \tag{0.1}
\]

and let tag `t_e` occur only in the two endpoint blocks of edge `e`.  The
support of each rail along its two endpoint source words may be completely
arbitrary; no periodicity or one-residue ansatz is imposed.

For every `d>=5`, the guarded sharp octagon relation contains three
consecutive phase-sensitive source intervals of width `d`, with starts

\[
                           d+3,d+4,d+5.                  \tag{0.2}
\]

It is impossible that

1. every phase-sensitive interval of width at most `d` retains a matching
   tagged occurrence on the opposite signed shore, and
2. every aligned depth-`d` owner window of width `d+1` has four distinct
   block tag signatures.

Thus staggering the four pair-shared rails cannot remove the V4 owner
multiplicities while preserving the exact short residual deck.  The
obstruction is local and applies to arbitrary rail supports.

## 1. The finite K2,2 tag lemma

For a source interval `I`, let

\[
 H(I)=\{e\in E:S_e\cap I\ne\varnothing\},              \tag{1.1}
\]

where `S_e` is the position support of rail `t_e`.  The tag set seen in block
`v` is

\[
                 \sigma_H(v)=\{e\in H:v\in e\}.        \tag{1.2}
\]

### Lemma 1.1 (cancellation versus distinction)

For `H subseteq E`:

* the positive- and negative-shore tag multisets agree,

  \[
   \{\sigma_H(0),\sigma_H(1)\}_{\rm multi}
       =\{\sigma_H(2),\sigma_H(3)\}_{\rm multi},        \tag{1.3}
  \]

  if and only if `H` is a matching in `K_(2,2)`;
* the four signatures `sigma_H(0),...,sigma_H(3)` are pairwise distinct if
  and only if `H` is **not** a matching.

#### Proof

If `H` is a matching, every selected edge contributes its singleton label
once on each shore, and unmatched vertices contribute the empty set.  This
proves (1.3).  It also gives two equal endpoint signatures for every chosen
edge, or two empty signatures if `H` has fewer than two edges, so the four
signatures are not distinct.

If `H` is not a matching, it contains two adjacent edges.  Their common
endpoint has a tag set of size at least two, while no vertex on the opposite
shore is incident with both; hence (1.3) fails.  Conversely, a direct
two-by-two check (or deletion of the common adjacent pair) shows that no two
vertex incidence sets in a nonmatching subgraph of `K_(2,2)` agree.  Thus the
four signatures are distinct.  \(\square\)

The last converse has only nine cases: the nonmatching edge sets are the
four adjacent pairs, the four three-edge sets, and the full four-edge set.

## 2. The three-window contradiction

Put

\[
 I_j=[s+j,s+j+d-1]\quad(j=0,1,2),\qquad s=d+3.          \tag{2.1}
\]

These are the three consecutive phase-sensitive rows from (0.2).  Let
`H_j=H(I_j)`.  Condition 1 and Lemma 1.1 force every `H_j` to be a matching.

The owner window

\[
 W_j=I_j\cup I_{j+1}=[s+j,s+j+d]                       \tag{2.2}

has tag graph `H_j union H_(j+1)`.  Condition 2 and Lemma 1.1 force this
union to be a nonmatching.

Consider `j=0`.  Since `H_0,H_1` are matchings but their union is not, there
are adjacent edges `e,f` such that `e` occurs only in `I_0` and `f` only in
`I_1`.  The two intervals differ only at their exposed endpoints, so `e`
occurs at position `s` and `f` at position `s+d`.  Every tag occurring in
their common overlap `[s+1,s+d-1]` would have to be disjoint from both `e`
and `f`.  No edge of `K_(2,2)` is disjoint from two adjacent edges.  Hence
the overlap is tag-free.

Apply the same argument to `I_1,I_2`.  Their common overlap
`[s+2,s+d]` must be tag-free.  But the first pair forced `f` to occur at
`s+d`, a contradiction.  This proves the theorem.

## 3. Exact occurrence strengthening in the sharp relation

The actual three rows in (0.2) are even more rigid than the shore-multiset
relaxation used above.  At each row the old-to-new singleton occurrence map
on the four blocks is

\[
             0\mapsto1\mapsto3\mapsto2\mapsto0.        \tag{3.1}
\]

After relabelling the two shores, these are the four edges of (0.1).  Exact
tagged equality along (3.1) requires all four vertex signatures to agree.
Since an edge label occurs at exactly two vertices, this forces

\[
                              H(I_j)=\varnothing.        \tag{3.2}
\]

Thus strict addressed cancellation already makes the two overlapping owner
windows tag-free.  Section 2 proves the stronger result that even arbitrary
matching of equal tagged occurrences cannot rescue the weave.

The three-row identity follows by direct substitution in the guarded sharp
inverse: at starts `d+3,d+4,d+5`, the width-`d` interval meets the first
phase-changing address and no saturating later active corridor, and the four
Klein relabellings send its active value around exactly the cycle (3.1).
The filler union is positionwise common and therefore does not change that
occurrence permutation.

## 4. Scope

The no-go assumes the four globally named tags in (0.1), pairwise-shared
support at aligned source positions, and literal equality of the tag set on
matched residual occurrences.  It does not cover:

* private block tags later cancelled by a separate nonlocal gadget;
* extra buffer labels which alter the four-resource relation;
* a tagged embedding into four nonaligned ambient occurrences; or
* abandoning exact short-deck preservation in favor of a compiler Hall
  repair.

Those are genuine changes of architecture, not staggerings of the proposed
four rails.

## 5. Replay

Run

```text
python3 scratch/audit_ad_k22_staggered_tag_weave_obstruction_20260801.py --write
```

The replay exhausts all 16 edge subsets, verifies Lemma 1.1, and checks for
every `5<=d<=64` that the intervals starting at `d+3,d+4,d+5` have width
`d` and the singleton permutation (3.1).
