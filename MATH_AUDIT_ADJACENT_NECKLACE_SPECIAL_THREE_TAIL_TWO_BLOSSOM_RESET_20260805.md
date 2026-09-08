# Audit: the special `q=3 mod 6` three-tail reset

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_ADJACENT_NECKLACE_SPECIAL_THREE_TAIL_TWO_BLOSSOM_RESET_20260805.md`  
**Method:** symbolic gap, path-order, parity, and collision replay; no search  
**Verdict:** PASS as a local reset.  The two reset hub colours remain a
contracted input to the global ordinary-sector selector.

## 1. Parameter and path-order replay

Let `q=6b+3`, choose `2<=s<=b-1`, and put `c=b-s`.  Then `s>=2` and
`c>=1`, so every coordinate used in the theorem is nonnegative.

The five macro bases and their path orders are:

\[
\begin{array}{c|c|c}
\text{base}&\text{residues mod }6&\text{orders}\\ \hline
(6s+1,6c+2)&(1,2)&(2s,2c)\\
(6s,4,6c-1)&(0,4,5)&(2s-1,1,2c-1)\\
(6s-1,5,6c-1)&(5,5,5)&(2s-1,1,2c-1)\\
(6s+4,6c-1)&(4,5)&(2s+1,2c-1).
\end{array}
\tag{1.1}
\]

These follow directly from

\[
 L(H)+1=\left\lfloor{H-4\over3}\right\rfloor+1.
\tag{1.2}
\]

The special path has order `2b+1`.  Removing index `2s` leaves components
of orders `2s` and `2b-2s`, both even.

## 2. Noncritical gradient replay

The one-product theorem gives entry

\[
                         x=(2s-1,0)
\]

in the even-by-even grid.  The chosen exit

\[
                         y=(2s-3,1)
\]

is valid, has even parity, and maps under the unique residue-repair move to

\[
                         z=(2s-3,0,0)
\]

in `(6s,4,6c-1)`.  The coordinate sum of `z` is odd, so it lies on the
minority shore of the odd product.  The theorem does not evade or
contradict the one-product-ear no-go; it pays that minority deletion with
two additional majority tails.

For `F-{x,y}`, the displayed matching covers all columns at least two.
On columns zero and one, all rows through `2s-4` use vertical pairs, and
the two horizontal pairs

\[
 (2s-3,0)(2s-2,0),
 \qquad
 (2s-2,1)(2s-1,1)
\]

cover the remaining four vertices.  This is exact also at the boundary
values `s=2` and `c=1`.

## 3. Three-tail and blossom replay

In `T`, the three deleted boundary vertices have first coordinates

\[
                         2s-4, 2s-3, 2s-2.
\]

They are an even--odd--even triple and are the final three positions of
the first factor.  The remaining boundary segment has even order
`2s-4`; every other column belongs to one of `c-1` consecutive column
pairs.  Hence the stated product matching is complete.

At the two majority vertices, the exact gap moves are

\[
                         12\mid4\longleftrightarrow11\mid5,
 \qquad                  6\mid4\longleftrightarrow5\mid5.
\tag{3.1}
\]

Their target macro sums are both `(6s-1,5,6c-1)`.  Deleting the moved cuts
instead gives

\[
 (3^{2s-4},16,6c-1),
 \qquad
 (3^{2s-2},10,6c-1),
\tag{3.2}
\]

both in `(6s+4,6c-1)`.  The values sixteen and ten distinguish the two
hub necklaces under every rotation because `6c-1` is odd.  The two
blossoms therefore satisfy the one-use hub rule relative to one another.

The blossom endpoint levels are `2s-1` and `2s+1`.  Internal circulation
states from a `k`-gap endpoint have `k` or `k-1` zeroes, so the two
interior zero-count sets are

\[
 \{2s-1,2s-2\},
 \qquad
 \{2s+1,2s\},
\]

which are disjoint.  This repairs the precise cross-level gap left by the
fixed-level injectivity theorem.

## 4. Socket cancellation replay

The midpoint in `U` has literal gap word

\[
                         (3^{2s-3},8,5,6c-1),
\]

while the midpoint in `D` is

\[
                         (3^{2s-3},13,6c-1).
\]

Thus they differ by exactly one cut insertion/deletion, splitting thirteen
as `8+5`.  This is a literal ambient adjacent-transfer edge.

In `U`, deleting the two blossom endpoints and the midpoint removes the
final three cells of boundary column zero.  In `D`, the analogous triple
leaves boundary-column segments of orders `2s-4` and two.  All are even,
and every nonboundary column is paired with its neighbour.  The two
claimed perfect matchings and the final socket edge are therefore exact.

## 5. Quotient and scope replay

The bases with residue patterns `(1,2)`, `(0,4,5)`, and `(4,5)` have
trivial stabilizer.  The `(5,5,5)` base could have order-three stabilizer
only if its three literal values were equal, impossible because `s>=2`
gives `6s-1>5`.  Thus none of the path matchings is merely a pointed
construction.

The proof consumes the two hub colour classes (3.2).  A different split
block over either unpointed hub can still exist.  Therefore the theorem
correctly stops at a local reset and requires the global ordinary-sector
selector to contract both colours.  No claim of automatic cross-background
hub disjointness is made.

For the small values, `q=3` is the permitted singleton socket, `q=9` uses
the path edge `S_1S_2` and the cut edge `(9)-(4,5)`, and `q=15` is exactly
the previously audited two-blossom closure.  These cases cover all values
not admitting `2<=s<=b-1`.
