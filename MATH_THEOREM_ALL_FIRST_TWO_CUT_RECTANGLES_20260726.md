# All two-row/two-cut rectangles in the Chung--Feller layered factor

Date: 2026-07-26

This note classifies every move which keeps two row endpoints fixed,
swaps their states at one intermediate layer, and uses cancellation across
the two adjacent `Y` cuts.  There are two answers.

1. Abstractly, every nontrivial move is an affine four-coordinate
   octahedral rectangle.  This gives necessary and sufficient set
   conditions, not merely the known leaf example.
2. At the **first two cuts of the canonical Chung--Feller factor**, the
   recursion forces the two roots to be

   \[
                         1100R\longleftrightarrow1010R,
                         \qquad R\in\mathcal D_{r-2}.   \tag{0.1}
   \]

   There are no further two-row rectangles.

Consequently the first-two-cut root graph is a disjoint matching with
`Cat_(r-2)` edges.  Its components have size at most two, and it moves only

\[
            {2\operatorname {Cat}_{r-2}\over\operatorname {Cat}_r}
                    \longrightarrow {1\over8}          \tag{0.2}
\]

of the roots.  It cannot support a balanced first-layer permutation on
the whole Catalan layer.

## 1. The abstract rectangle problem

Let all sets below have size `r`.  Consider two length-two Johnson paths

\[
                       A-B-C,\qquad D-E-F,             \tag{1.1}
\]

lying in complementary geodesics, so `d_J(A,C)=d_J(D,F)=2`.  Swap the
two middle states:

\[
                       A-E-C,\qquad D-B-F.             \tag{1.2}
\]

The state multiset is automatically preserved.  The exact two-cut
conditions are

\[
 A\sim_JE\sim_JC,qquad D\sim_JB\sim_JF,              \tag{1.3}
\]

and

\[
 \boxed{
 \{A\cup B,B\cup C,D\cup E,E\cup F\}_{\rm multi}
 =
 \{A\cup E,E\cup C,D\cup B,B\cup F\}_{\rm multi}.}   \tag{1.4}
\]

Equation (1.4) is aggregate across both cuts.  Equality cut by cut is not
required.

### Theorem 1.1 (necessary and sufficient octahedral form)

A nonidentity swap (1.2) satisfies (1.3)--(1.4), without reusing an
`X`-state, if and only if there are an `(r-2)`-set `K` and four distinct
coordinates `x,y,z,w` outside `K` for which, after possibly exchanging
the two rows, the old and new paths are

\[
\begin{array}{c|ccc}
 &X_t&X_{t+1}&X_{t+2}\\ \hline
\text{old row }P&Kxy&Kxw&Kzw\\
\text{old row }Q&Kxz&Kyz&Kyw
\end{array}
\quad\longmapsto\quad
\begin{array}{c|ccc}
\text{new row }P&Kxy&Kyz&Kzw\\
\text{new row }Q&Kxz&Kxw&Kyw.
\end{array}                                                   \tag{1.5}
\]

Here `Kxy` abbreviates `K union {x,y}`.  On either shore the four union
colours are exactly

\[
                    Kxyz,\quad Kxyw,\quad Kxzw,\quad Kyzw.      \tag{1.6}
\]

#### Proof

Since `d_J(A,C)=2`, write

\[
                         A=Kab,qquad C=Kcd              \tag{1.7}
\]

with `a,b,c,d` distinct.  Their common Johnson neighbours are precisely

\[
                         Kac,Kad,Kbc,Kbd.               \tag{1.8}
\]

Both `B` and `E` belong to this list.  If they are adjacent rather than
opposite in the four-cycle (1.8), changing `B` to `E` on the first row
removes one three-set colour and inserts another while leaving the other
first-row colour fixed.  To cancel this on the second row, one of its
boundary states must equal `A` or `C`; that repeats an already owned
`X`-state.  Hence `B,E` are opposite members of (1.8).

Now `D,F` must be common neighbours of these opposite middle states.
Their four common neighbours are `A,C` and the remaining opposite pair
of two-subsets.  Exact state ownership excludes `A,C`, so `D,F` are that
remaining pair, in one of the two orders.  Renaming the four coordinates
gives (1.5).  Direct union gives (1.6), proving sufficiency as well.
\(\square\)

Equivalently, the six affected states are the six two-subsets of one
four-set, with a common core `K`.  The three path endpoint pairs are the
three antipodal pairs of the octahedron `J(4,2)`.

## 2. Exchange-prefix form

For a rooted complementary path write

\[
 X_{i+1}=X_i-\{a_{i+1}\}+\{b_{i+1}\}.                \tag{2.1}
\]

In the orientation (1.5), the first two exchange pairs are

\[
\begin{array}{c|cc}
 &\text{first exchange}&\text{second exchange}\\ \hline
P&y\mapsto w&x\mapsto z\\
Q&x\mapsto y&z\mapsto w.
\end{array}                                                   \tag{2.2}
\]

Thus, if `rho(R)` is the Chung--Feller flip-position word in the convention
that an exchange inserts `rho_(2i-1)` and deletes `rho_(2i)`, every edge
of the first-two-cut graph can be oriented so that

\[
             \rho(P)=(w,y,z,x,\ldots),\qquad
             \rho(Q)=(y,x,w,z,\ldots).                \tag{2.3}
\]

The root sets satisfy

\[
                         Q=P-\{y\}+\{z\}.              \tag{2.4}
\]

Conversely, (2.3)--(2.4) imply the octahedron (1.5) and hence give a legal
rectangle.  These are therefore another set of necessary and sufficient
conditions.

## 3. Chung--Feller recursion forces the prefix leaf pair

We use the exact MSW recursion.  If the first primitive component of a
Dyck word is `1u0` of semilength `j`, followed by `v`, then

\[
 \rho(1u0v)=
 \bigl(2j, 2j-\rho(\operatorname {rev}u), 1,
                     2j+\rho(v)\bigr),                \tag{3.1}
\]

where subtraction and addition act entrywise.  In particular the first
inserted coordinate is twice the first-return semilength.

### Theorem 3.1 (complete first-two-cut root graph)

For `r>=2`, two canonical Dyck rows form a nontrivial rectangle at cuts
zero and one if and only if they are the pair (0.1).

#### Proof

Let an edge be oriented as in (2.3).  Let the first primitive components
of `P,Q` have semilengths `j,k`.  Equation (3.1) gives

\[
                              w=2j,qquad y=2k.          \tag{3.2}
\]

The roots differ by changing position `y` from an up-step in `P` to a
down-step in `Q`, and a later position `z` in the opposite direction.
Since `Q` first returns at `y`, the path `P` is two units above `Q`
immediately after `y`; hence `P` returns later and

\[
                              j>k,qquad w>y.            \tag{3.3}
\]

If `k>=2`, the first primitive flip block of `Q` has at least four
entries, all coordinates at most `2k=y`.  In particular its third entry
is at most `y`.  But (2.3) says that the third entry is `w>y`, a
contradiction.  Therefore

\[
                              k=1,qquad y=2,quad x=1.  \tag{3.4}
\]

Now inspect `P`.  If `j>=3`, then after the initial entry `2j`, the next
at least three entries belong to the block
`2j-rho(rev u)`.  Every entry of this block is at least two, because
`rho(rev u)` uses only coordinates at most `2j-2`.  This contradicts the
fourth entry `x=1` in (2.3).  Hence `j=2`.  Formula (3.1), using
`rho(10)=(2,1)`, gives

\[
                         \rho(P)=(4,2,3,1,\ldots).      \tag{3.5}
\]

The first primitive component of `P` is therefore `1100`.  Equation
(2.4) changes its second bit to zero and its third bit to one, so

\[
                         P=1100R,qquad Q=1010R         \tag{3.6}
\]

for one common Dyck suffix `R`.  Conversely the concatenation law gives

\[
 \rho(1100R)=(4,2,3,1,4+\rho(R)),\qquad
 \rho(1010R)=(2,1,4,3,4+\rho(R)),                    \tag{3.7}
\]

which is exactly (2.3).  Theorem 1.1 proves legality.  \(\square\)

This proof uses neither an even-pair ansatz nor a coordinate-conjugation
restriction.  It begins with an arbitrary pair of canonical rows and an
arbitrary aggregate two-cut colour cancellation.

## 4. Components and the first-layer permutation obstruction

Let `G_r^(2)` be the graph on `D_r` whose edges are all legal nontrivial
two-row rectangles at the first two cuts.  Theorem 3.1 gives

\[
 E(G_r^{(2)})=
 \bigl\{\{1100R,1010R\}:R\in\mathcal D_{r-2}\bigr\}. \tag{4.1}
\]

These edges are pairwise vertex-disjoint.  Hence `G_r^(2)` has

\[
 \operatorname {Cat}_{r-2}\text{ components of size two},
 \qquad
 \operatorname {Cat}_r-2\operatorname {Cat}_{r-2}
       \text{ singleton components}.                 \tag{4.2}
\]

The group of first-layer row permutations generated by all such moves is

\[
                     \boxed{(C_2)^{\operatorname {Cat}_{r-2}}.} \tag{4.3}
\]

It independently swaps the two middle states on each edge and fixes every
other root.  Equivalently, the unordered pair

\[
                         \{1100R,1010R\}               \tag{4.4}
\]

and every singleton root are complete component invariants.

The active root proportion is

\[
 {2C_{r-2}\over C_r}
 ={r(r+1)\over2(2r-1)(2r-3)}
 \longrightarrow{1\over8}.                           \tag{4.5}
\]

Thus no choice of these rectangles gives a balanced permutation of the
whole first Chung--Feller layer: at least

\[
                         C_r-2C_{r-2}
                 =\left({7\over8}+o(1)\right)C_r      \tag{4.6}
\]

root labels are fixed.  Even on the active support, every orbit has only
two states.

For reference, on one active pair the canonical first inserted labels are
`4` and `2`; after the swap they are `3` and `4`.  Hence each selected
rectangle moves one aggregate unit from label `2` to label `3`, but no
selection can turn this sparse matching into an all-root conveyor.

## 5. Scope

At an arbitrary pair of adjacent cuts inside a complementary geodesic,
Theorem 1.1 remains the complete set-theoretic classification: every
two-row move is octahedral.  Contextual copies later in the flip word give
the familiar `P1100R <-> P1010R` rectangles at their own two cuts.

The matching theorem (4.1) is specifically for the **first two global
cuts of the canonical layered factor**.  Enlarging the library by
coordinate conjugation, by longer alternating cycles, or by factors which
leave the canonical flaw layer at an intermediate phase is a different
graph.  Those extensions are not ruled out here.
