# Adjacent necklaces: the five-skeleton is an odd capacity-two token sector

**Date:** 2026-08-05  
**Method:** exact residue coordinates, local path matching, and hub-fibre
classification; no computation  
**Status:** unconditional reduction.  It corrects two overly strong
hub-rainbow claims and isolates the remaining problem as a coloured
matching/ear problem.  It does not prove the all-odd-`q` matching theorem.

## 1. Critical macro parts have a unique capacity-two coordinate

Let `q` be odd.  After the canonical three-run macro matching, every
ordinary critical macro part belongs to

\[
 \mathcal S=\{H\ge4:H\equiv0,4,5\pmod6\}.
\]

Every `H in S` has a unique expression

\[
                         H=6a+4+t,
 \qquad a\in\mathbb Z_{\ge0},\quad t\in\{0,1,2\}.       \tag{1.1}
\]

Thus a critical cyclic macro composition of length `k` is a cyclic pair

\[
              (a,t)=((a_1,t_1),\ldots,(a_k,t_k)),       \tag{1.2}
\]

with

\[
 q=6\sum_i a_i+4k+R,\qquad R:=\sum_i t_i.              \tag{1.3}
\]

Since `q` is odd, `R` is odd.

### Theorem 1.1 (capacity-two sector decomposition)

An adjacent unit transfer between two macro parts remains inside the
critical family if and only if it fixes the background `a` and performs
one legal nearest-neighbour hop in

\[
 \mathcal T_{k,R}
 =\{t\in\{0,1,2\}^{\mathbb Z_k}:\sum_i t_i=R\}.        \tag{1.4}
\]

The local edges are exactly

\[
  01\leftrightarrow10,\qquad
  12\leftrightarrow21,\qquad
  02\leftrightarrow11\leftrightarrow20.               \tag{1.5}
\]

For a background necklace `[a]`, the ordinary critical necklace graph is
the quotient of the capacity-two token graph (1.4) by the cyclic
stabilizer of `a`.

#### Proof

Changing a cut by one transfers one unit between two adjacent parts.
Writing the two parts in (1.1), a transfer stays in `S` precisely when
neither local digit leaves `{0,1,2}`.  This gives (1.5), preserves each
`a_i`, and conversely every edge in (1.5) is a legal critical transfer.
Rotation acts simultaneously on `a` and `t`, so after fixing `[a]` the
remaining quotient group is exactly its stabilizer. \(\square\)

The odd five-skeleton is the parity shadow of this stronger statement:
the number of digits equal to one has the same parity as `R`, hence is
odd.

## 2. Exact hub colour fibres

Delete the moved cut.  If the two parts adjacent to it are `A,B`, the hub
remembers their merged value

\[
                              M=A+B.                  \tag{2.1}
\]

Fix a literal hub, a particular merged-gap site in that hub, and all
parts outside that site.  The critical expansions at the site are the
splits

\[
                         M=A+(M-A),\qquad A,M-A\in S. \tag{2.2}
\]

Order these splits by the integer `A`.

### Theorem 2.1 (split-fibre classification)

The adjacency graph on (2.2) is a disjoint union of the following blocks:

\[
\begin{array}{c|c|c}
M\pmod6&\text{residue sequence in a block}&\text{block}\\ \hline
3&(4,5)-(5,4)&P_2,\\
4&(4,0)-(5,5)-(0,4)&P_3,\\
5&(5,0)-(0,5)&P_2.
\end{array}                                            \tag{2.3}
\]

For the other residues there is no critical horizontal edge.  Distinct
blocks in one split fibre are separated by at least one forbidden split.

#### Proof

The allowed residues for a part are `4,5,0` in increasing integer order.
Two splits are adjacent precisely when the first summand rises by one and
the second falls by one.  Enumerating the possible residue sums gives
exactly (2.3).  Passing from a terminal residue zero to the next residue
four changes the first summand by four, so different blocks do not meet.
\(\square\)

This theorem gives the exact hub capacity.  A hub colour can contain many
vertex-disjoint edges: it can have several split blocks at one site and
several eligible merged-gap sites.  Therefore

\[
 \boxed{\text{edge matching does not imply hub-rainbow matching}.}       \tag{2.4}
\]

The hub condition is a partition-matroid constraint on selected edge
occurrences: at most one selected edge from the entire colour fibre of
each unpointed hub orbit.

For example, the rooted hub `(21,4,6)` supports the two disjoint edges

\[
 (4,17,4,6)-(5,16,4,6),\qquad
 (10,11,4,6)-(11,10,4,6),                            \tag{2.5}
\]

which have the same deleted-cut hub `(21,4,6)`.  The two split blocks in
the merged part of size twenty-one are separated by forbidden splits.
This corrects the former assertion
that an arbitrary matching in a rooted `4/5` token path is automatically
hub-rainbow.

## 3. A complete rooted matching when the macro length is even

Before taking rotations, suppose `k=2m` and choose an origin.  Pair the
positions as

\[
                   (1,2),(3,4),\ldots,(2m-1,2m).      \tag{3.1}
\]

On one ordered pair use the local matching

\[
 01-10,\qquad02-11,\qquad12-21,                       \tag{3.2}
\]

leaving the three local states

\[
                              00,20,22                 \tag{3.3}
\]

unmatched.  For a global state, scan the pairs in (3.1) and apply (3.2)
at the first pair not in (3.3).

### Theorem 3.1 (even-length rooted token matching)

For odd `R`, this is a fixed-point-free involution of the labelled sector
`T_(2m,R)`.  Hence every labelled even-length capacity-two sector has a
perfect matching by legal critical transfers.

#### Proof

Within a fixed pair sum, the local graphs are respectively

\[
 P_1,\ P_2,\ P_3,\ P_2,\ P_1
\]

for sums zero through four.  Formula (3.2) is an involution away from the
chosen critical endpoint of each odd local path.  It does not change any
earlier pair, so rescanning chooses the same active pair and reverses the
move.

If a global state were unmatched, every pair would belong to (3.3).
Each state in (3.3) has even local mass, forcing the total `R` to be even,
a contradiction. \(\square\)

This is a genuine matching theorem, but it is rooted and it does not yet
satisfy the unpointed hub partition constraint (2.4).

## 4. Exact rooted residue for odd macro length

For `k=2m+1`, protect position one and apply the same matching to

\[
                   (2,3),(4,5),\ldots,(2m,2m+1).      \tag{4.1}
\]

### Proposition 4.1

At odd total mass `R`, the unmatched labelled states are exactly

\[
 t_1=1,\qquad (t_2,t_3),\ldots,(t_{2m},t_{2m+1})
                       \in\{00,20,22\},               \tag{4.2}
\]

subject to the total-mass equation.

#### Proof

The product matching leaves precisely the local critical states (3.3).
Their combined mass is even.  Therefore the protected digit must be odd,
and the only odd digit in `{0,1,2}` is one.  The converse is immediate.
\(\square\)

Thus the rooted odd-length obstruction has been reduced from a full
capacity-two sector to a three-letter product with one forced singleton.
Forgetting the root, enforcing the hub partition, and routing these
residues by odd circulation ears remain open.

## 5. The special divisible-by-three fibre is phase-locked

Now let `q=3a`, with `q` odd.  The enlarged special macro fibre is the odd
path

\[
 S_0-S_1-\cdots-S_{a-2}-S_{a-1},                     \tag{5.1}
\]

where

\[
 S_r=(3^r,q-3r)\quad(0\le r\le a-2),\qquad
 S_{a-1}=(3^a).                                      \tag{5.2}

Only a boundary between a gap three and the terminal gap can be shifted
while keeping every gap at least three.  For `r>=1`, the valid shift has
gap word

\[
                       (3^{r-1},4,q-3r-1).            \tag{5.3}

Its macro base is

\[
                         (3r+1,q-3r-1).               \tag{5.4}

### Theorem 5.1 (wrong-shore exit obstruction)

The base (5.4) is ordinary critical if and only if `r` is odd.  Therefore
every direct horizontal exit from the special path to an ordinary
critical macro fibre lies at an odd-indexed vertex `S_r`.

No matching consisting of special-path edges and such direct exits can
cover the special path while using any number of external critical
partners.  In particular the special critical monomer cannot be removed
by a direct critical-to-critical hub-rainbow matching.

#### Proof

Modulo six, `q=3`.  If `r` is odd, (5.4) has residues `(4,5)`; if `r` is
even, its first part has residue one and its second part residue two.
This proves the first assertion.

Remove from the odd path (5.1) the vertices matched externally.  For the
remaining path components to have perfect matchings, the least removed
index must be even: the initial component has that many vertices.  But
every available direct critical exit has odd index.  If no vertex is
removed, the odd path itself is not perfectly matchable.  Either way a
perfect cover is impossible. \(\square\)

The obstruction is already visible at `q=9`: the critical macro orbits
are the special `(9)` and the ordinary `(4,5)`.  The transfer
`45<->54` folds to a quotient self-loop, while `(9)` has no horizontal
edge.  At `q=11`, the critical bases `(11)` and `(5,6)` give the analogous
warning.  Hence the simple critical graph is not the final matching
object even in the first small cases.

### Theorem 5.2 (one-product-ear parity lock)

Write `q=6b+3` and choose an even special index `r=2s`; put `c=b-s`.
The direct shift out of `S_r` enters the noncritical macro base

\[
             (A,B)=(6s+1,6c+2)                       \tag{5.5}
\]

at the vertex `x=(2s-1,0)` of its product fibre

\[
                         P_{2s}\square P_{2c}.        \tag{5.6}
\]

Suppose a two-tail ear enters (5.6) at `x`, traverses this one product
fibre, and exits by one horizontal transfer to a critical macro fibre.
If deleting its two product-fibre endpoints leaves that product fibre
perfectly matchable, then its critical exit vertex lies on the minority
shore of the target odd product fibre.  Consequently that target fibre
cannot be completed after only this one external deletion.

#### Proof

Write a product-fibre vertex as

\[
 (3^i,A-3i,3^j,B-3j),\quad
 0\le i<2s,\quad0\le j<2c.                           \tag{5.7}

The entry `x=(2s-1,0)` has odd grid parity.  The even-by-even product has
equal bipartition shores, so an exit `y=(i,j)` whose removal together with
`x` permits a perfect matching must have even parity `i+j`.

The only one-step boundary move from (5.7) which changes both noncritical
base residues `(1,2)` into allowed residues is

\[
 (A-3i)\mid3\longmapsto(A-3i-1)\mid4.                \tag{5.8}

It produces the critical base

\[
                         (A-1,4,B-3),                 \tag{5.9}

\]

with expansion coordinates `(i,0,j-1)`.  The other possible boundary
moves leave at least one of the base residues one or two.  The three path
orders in (5.9) are `2s-1,1,2c-1`, all odd.  Its even coordinate-parity
shore is therefore larger by one.  But the exit vertex has parity

\[
                            i+j-1,                    \tag{5.10}

\]

which is odd because `i+j` is even.  It lies on the minority shore.
Deleting it makes the shore imbalance two, so no internal perfect
matching remains. \(\square\)

Thus the first plausible higher ear is itself parity-locked.  A repair
must use an odd circulation blossom, at least a three-tail network, or a
second gradient fibre which changes this parity accounting.

## 6. Correct remaining theorem

The remaining object is the following coloured ear problem.

1. On every ordinary background sector `(a,R)`, match the capacity-two
   token configurations modulo rotation.
2. Regard deleted-cut hub orbits as colours and use each colour at most
   once across all background sectors.
3. Admit orbit-folded odd circulation blossoms and alternating gradient
   paths through noncritical macro fibres.
4. When `q=3 mod 6`, include an odd blossom, a three-tail network, or at
   least two gradient fibres leaving the wrong-shore special path; a
   direct critical exit and a one-product two-tail ear cannot suffice.
5. Preserve at most one prescribed radial socket.

Equivalently, selected horizontal edges form a matching in the critical
state graph and an independent set in the partition matroid of hub
colours, augmented by the explicitly permitted folded/gradient ears.
This is strictly sharper than the former “five-skeleton hub-rainbow
matching” statement and explains why edge matching alone repeatedly
stalls.

## 7. Scope

Proved here:

1. exact reduction of every ordinary critical macro sector to an odd
   capacity-two token sector;
2. exact `P2/P3` structure of every pointed hub split fibre;
3. a perfect rooted matching for every even macro length;
4. the exact rooted critical residue for odd macro length; and
5. the wrong-shore obstruction for the special `q=3 mod 6` fibre and the
   one-product-ear parity lock.

Not proved:

1. cyclic descent of the rooted token matching;
2. the global partition-matroid/hub-rainbow constraint;
3. the necessary higher alternating ear out of the special fibre;
4. protected packing of circulation interiors; or
5. the complete adjacent-necklace theorem.
