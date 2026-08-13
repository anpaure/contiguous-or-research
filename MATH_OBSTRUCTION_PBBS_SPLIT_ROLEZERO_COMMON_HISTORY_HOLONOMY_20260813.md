# The direct split role-zero chain has an exact history holonomy obstruction

**Date:** 2026-08-13  
**Status:** unconditional source-level no-go for the direct all-height
concatenation of the same-history split macros.  The local palette split at
one height remains valid.  What fails is using one ordered common history
on both halves of every macro while concatenating the macros through the
literal shared spine owners.

## 1. Adjacent height cores

Use the high-height PBBS notation

\[
 G_h=\{h+2,\ldots,2h\}\mathbin{\dot\cup}
     \{2h+4,2h+6,\ldots,2r\},
 \qquad H_h=G_h\cup\{0\}.
\tag{1.1}
\]

The role-zero owner is represented at height `h` by

\[
 U_h=H_h\cup X_h=H_{h-1}\cup Y_{h-1},
\tag{1.2}
\]

where direct subtraction in `(1.1)` gives

\[
 X_h=H_{h-1}\setminus H_h=\{h+1,2h+2\},
 \qquad
 Y_{h-1}=H_h\setminus H_{h-1}=\{2h-1,2h\}.
\tag{1.3}
\]

In particular

\[
 H_{h-1}\cap H_h
 =H_{h-1}\setminus X_h
 =H_h\setminus Y_{h-1}.
\tag{1.4}
\]

## 2. The forced shift recurrence

Let

\[
 \mathcal C_h=(C_{h,1},\ldots,C_{h,d})
\tag{2.1}
\]

be the ordered nonempty partition of `H_h` used on **both** source
half-blocks of the split macro at height `h`.  Its terminal half-block is

\[
 (W_h,C_{h,1},\ldots,C_{h,d},Y_h),
\tag{2.2}
\]

and the next macro's initial half-block is

\[
 (X_{h+1},C_{h+1,1},\ldots,C_{h+1,d},Z_{h+1}).
\tag{2.3}
\]

The two owner edges meet at `U_(h+1)`.  If they are consecutive edges of
one depth-`d` source chronology, their length-`d+2` source blocks start one
position apart.  Literal overlap therefore forces

\[
 C_{h,1}=X_{h+1},
\tag{2.4}
\]

\[
 C_{h+1,j}=C_{h,j+1}\quad(1\le j<d),
 \qquad
 C_{h+1,d}=Y_h.
\tag{2.5}
\]

These equations are not merely set-union constraints.  They follow from
equality of the actual source letters in the overlap.

Conversely, `(2.4)--(2.5)` is locally compatible with the core change:
after deleting the first block `X_(h+1)` from the partition of `H_h`, the
remaining blocks partition `H_h\cap H_(h+1)`, and appending `Y_h` produces
a partition of `H_(h+1)`.

## 3. Holonomy after `d+1` junctions

Apply `(2.4)--(2.5)` at the consecutive junctions

\[
 h-1,h,\ldots,h+d-1.
\]

The first `d` junctions force

\[
 \mathcal C_{h-1}
   =(X_h,X_{h+1},\ldots,X_{h+d-1}),
\tag{3.1}
\]

up to the harmless corresponding shift of the starting index.  After
`d` shifts, the next required first block is the block appended at the
first junction.  Equivalently, the `d+1` junction equations imply

\[
                         X_{h+d}=Y_{h-1}.             \tag{3.2}
\]

But `(1.3)` gives

\[
 X_{h+d}=\{h+d+1,2h+2d+2\},
 \qquad
 Y_{h-1}=\{2h-1,2h\}.
\tag{3.3}
\]

For `d\ge1` these sets are unequal; their largest elements already satisfy

\[
                         2h+2d+2>2h.                 \tag{3.4}
\]

### Theorem 3.1 (direct common-history chain no-go)

No depth-`d` source word can contain `d+1` consecutive junctions of the
literal PBBS role-zero split macros if, at every height, the two halves use
the same ordered history partition of `H_h`.

Thus the local same-history split cannot be concatenated through the full
deadline-scale height ladder.  This is a source-letter obstruction even
though every individual half-edge, owner, lower palette and upper palette
is legal.

## 4. Exact scope and escape routes

The theorem does **not** obstruct:

1. one isolated split macro;
2. a bounded run of at most `d` junctions;
3. different input and output histories separated by a genuine
   history-changing detour; or
4. moving the strict-lower occurrence transport to auxiliary source rails,
   thereby freeing the two palette half-edges to use different histories.

The fourth route is particularly concrete.  If the old history is
`(O_1,...,O_d)`, then three physically disjoint rails can preserve,
respectively, every strict-lower interval meeting the left screen, every
one meeting the right screen, and every history-only interval.  Replacing
`O_d` on the first rail and `O_1` on the second by equal-size fresh blocks
keeps those visible intervals literal while avoiding the old spine owners;
the third rail retains the complete old history between fresh screens.
That decoupling construction requires its own resource and antecedent
audit and is not asserted here.

The sharp conclusion is

\[
 \boxed{
 \text{same history on both halves}
 +\text{ literal all-height concatenation}
 \Longrightarrow\text{ impossible shift holonomy}.}
\]
