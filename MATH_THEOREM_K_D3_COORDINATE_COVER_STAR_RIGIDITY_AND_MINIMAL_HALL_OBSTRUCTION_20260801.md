# Depth-three coordinate-cover hosts: star rigidity, the minimal Hall obstruction, and the fibre-closed escape

**Date:** 2026-08-01  
**Lane:** K, functional attachment after the opened rolling reset  
**Status:** unconditional Boolean-specific theorems and one independently
replayed finite witness.  The note refutes ordinary two-sided
coordinate-cover and bounded universal-rectangle hosts as automatic sources
of the missing functional attachment.  It gives a sufficient
fibre-closed degree condition and the exact support-three augmentation row
which remains live.  It does not refute a prospectively correlated flag
table, and it does not construct the global high-target selector.

## 0. Outcome

At depth three a tail-normalized flag and a head-normalized flag have the
forms

\[
 f=(S,z),\qquad g=(H,\gamma),qquad
 |S|=m-2,\quad |H|=m-1,
\]

and, after a functional head--owner attachment fixes the exterior label
`z`, the exact predecessor law is

\[
 f\longrightarrow g
 \quad\Longleftrightarrow\quad
 S\subset H,\quad \gamma\in S,
 \tag{0.1}
\]

with owner `H+{0,z}`.  Equivalently the possible predecessors of
`(H,gamma)` are

\[
       (H-\{\beta\},z),\qquad \beta\in H-\{\gamma\}.
 \tag{0.2}
\]

This geometry has two consequences.

1. A literal complete Cartesian matrix cell is necessarily a star.  A
   bounded number of such cells cannot cover the Catalan-sized quotient
   table.
2. If "two-sided coordinate cover" means only that every row and column is
   nonempty, it does not imply Hall.  There is a root-simple,
   owner-simple, separated-point `3 by 3` obstruction already at `m=4`.

Thus the Ramsey/separated-palette idea can be useful only if its entries
carry a correlated predecessor matching, not merely coordinate margins or
homogeneous rectangles.  A proof-safe positive face is full predecessor
fibre closure together with a left-load bound.  The rolling-reset phase
trade transports the resulting boundary defect but does not create Hall
gain; the Boolean support-three hexagon is the first possible local
augmenter.

## 1. Functional blocks and literal Cartesian cells

Fix a nonzero exterior label `z`.  Let `L_z` be a selected family of tails
`(S,z)` and let `R_z` be selected head records `(H,gamma)` whose functional
owner attachment uses `z`.  Write `B_z` for the bipartite graph given by
(0.1).

A pair of nonempty subfamilies

\[
                         (L,R),\qquad L\subseteq L_z,
                         \quad R\subseteq R_z,
\]

is a **literal Cartesian cell** if every pair in `L times R` is an edge of
`B_z`.  It is **root-simple** when no two records of `R` use the same head
support `H`; this is forced in a selected quotient flag table because the
head root is `[H+{0}]` and only one flag is chosen per root orbit.  The
stronger quotient-root-simple condition only strengthens the hypothesis.

### Theorem 1.1 (Cartesian cells are stars)

Let `(L,R)` be a root-simple literal Cartesian cell.  Then

\[
                     \min\{|L|,|R|\}=1.                    \tag{1.1}
\]

More precisely,

\[
                     |L|\le m-2,
             \qquad |R|\le m+1.                            \tag{1.2}
\]

#### Proof

Suppose `L` contains distinct sets `S_1,S_2`.  Every head support in `R`
contains their union.  Since both `S_i` have size `m-2`, either their union
has size at least `m`, in which case no `(m-1)`-set contains it, or they
differ in one element and their union is the unique possible head support
of size `m-1`.  Root simplicity then gives `|R|=1`.

Conversely, suppose `R` contains two records with distinct supports
`H_1,H_2`.  Any tail in `L` is an `(m-2)`-subset of `H_1 intersect H_2`.
Distinct `(m-1)`-sets have intersection of size at most `m-2`; if such a
tail exists, it is unique.  Hence `|L|=1`.  This proves (1.1).

For a fixed head `(H,gamma)`, (0.2) gives exactly `m-2` possible tails,
proving the first bound in (1.2).  For a fixed tail `S`, the head support
must be `S+{beta}`.  Outside `S union {0,z}` there are

\[
                 (2m+1)-|S|-2=m+1
\]

choices of `beta`; root simplicity permits at most one pointed head record
on each support.  This proves the second bound.  \(\square\)

### Corollary 1.2 (no bounded universal-cell cover)

Let `N` selected tails and `N` selected heads be covered on both shores by
`t` literal Cartesian cells.  Then

\[
                         t\ge \left\lceil{N\over m-2}\right\rceil.
 \tag{1.3}
\]

In the cyclic quotient table `N=Cat_m`.  After contracting a protected
bank of `h` turns, the same argument gives

\[
                 t\ge \left\lceil{{\rm Cat}_m-h\over m-2}\right\rceil.
 \tag{1.4}
\]

For the opened `k=17` reset, `(m,h,N)=(8,7,1430)`, so at least

\[
                              \lceil1423/6\rceil=238
 \tag{1.5}
\]

actual Cartesian cells are required.

This rules out a constant number of literal homogeneous cells.  It does
not rule out a bounded number of **cell types** instantiated at Catalan
many different roots; such an instantiation must still prove the global
matching between the instances.

This is distinct from the state-product bound in
`MATH_THEOREM_K_RAMSEY_COORDINATE_COVER_OWNER_C4_AND_SUPPORT3_ESCAPE_20260801.md`.
That theorem assumes partitions into `a` row states and `b` column states
and proves `N<=ab`.  Corollary 1.2 assumes no partition--the cells may
overlap--and instead bounds the number `t` of actual offered Cartesian
cells using the exact Boolean star degrees.  Neither statement bounds a
finite catalogue of abstract cell types which is instantiated separately
at occurrence level.

## 2. Two-sided margins are not Hall

The alternative meaning of coordinate cover is weaker: every selected
head has at least one selected predecessor and every selected tail is used
by at least one selected head.  These are exactly the singleton Hall cuts.
They do not imply the non-singleton cuts.

### Theorem 2.1 (smallest literal Boolean obstruction)

At `m=4`, on `Z_9`, fix `z=8` and put

\[
\begin{array}{c|c}
\text{tail}&S\\ \hline
f_1&\{2,3\}\\
f_2&\{4,7\}\\
f_3&\{5,7\}
\end{array}
\qquad
\begin{array}{c|c|c}
\text{head}&H&\gamma\\ \hline
g_1&\{1,2,3\}&2\\
g_2&\{2,3,6\}&3\\
g_3&\{4,5,7\}&7.
\end{array}                                                   \tag{2.1}
\]

The induced predecessor graph has neighbourhoods

\[
              N(g_1)=\{f_1\},\qquad
              N(g_2)=\{f_1\},\qquad
              N(g_3)=\{f_2,f_3\}.                           \tag{2.2}
\]

Consequently every row and column is nonempty, and the three pointed
labels are distinct, but

\[
                         |N(\{g_1,g_2\})|=1<2.              \tag{2.3}
\]

The six flags in (2.1) occupy six distinct cyclic root orbits; the three
owners `H_i+{0,8}` occupy three distinct cyclic owner orbits.  The three
tail `T` colours `[S_i]` and the three tail `P` colours `[S_i+{0}]` are
also separately distinct.

#### Proof

For `g_1`, deleting an element other than `gamma=2` gives the facets
`{2,3}` and `{1,2}`, only the first of which is selected.  For `g_2` the
corresponding facets are `{2,3}` and `{3,6}`.  For `g_3` they are
`{4,7}` and `{5,7}`.  This proves (2.2)--(2.3).

The orbit assertions are a finite literal check.  In bit-mask notation the
three tail roots are

\[
                   269,401,417
\]

with canonical cyclic representatives `27,57,29`.  The three selected
flags giving the displayed head records have tail-normalized roots

\[
                   387,329,197
\]

with canonical representatives `15,77,43`.  The owner representatives are
`31,109,59`.  The `T` representatives are `3,9,5`, and the `P`
representatives are `13,41,21`.  All claimed families are therefore
injective.  \(\square\)

The order three is minimal as an abstract two-sided-cover obstruction:
every balanced bipartite graph of order at most two with no isolated
vertex has a perfect matching.  It is also the first Boolean depth at which
this pattern can occur.  At `m=3`, every pointed head has exactly one
possible predecessor.  On equal shores, nonempty columns make that
functional map surjective and hence bijective.

Theorem 2.1 is a local/partial-table obstruction.  It does not assert that
the six prescribed flag options extend to a complete high-target selector,
and therefore is not a `k=9` or all-parameter no-go.  It proves exactly
that root, owner, and local high-colour injectivity plus separated point
palettes do not upgrade coordinate cover to functional Hall.

## 3. The fibre-closed positive face

There is a sharp Boolean-specific condition under which elementary degree
counting does prove Hall.

### Theorem 3.1 (fibre-closed degree criterion)

Assume `|L_z|=|R_z|`.  Suppose

1. every selected head retains its complete predecessor fibre:

   \[
      \{(H-\{\beta\},z):\beta\in H-\{\gamma\}\}
                     \subseteq L_z;                          \tag{3.1}
   \]

2. every selected tail has degree at most `m-2` in `B_z`.

Then `B_z` is `(m-2)`-regular and has a perfect matching.

#### Proof

Condition (3.1) gives every right vertex degree exactly `m-2`.  Hence

\[
                         |E(B_z)|=(m-2)|R_z|.
\]

The left degree bound and `|L_z|=|R_z|` give the reverse inequality with
the same total.  Equality is forced at every left vertex, so the graph is
regular.  Every positive regular balanced bipartite graph has a perfect
matching.  \(\square\)

One sufficient way to get the left degree bound is to make the pointed
labels `gamma` injective on `R_z`: a neighbour of a fixed `S` is determined
by a point `gamma in S` and its selected head, so there are at most
`|S|=m-2` neighbours.

This last sufficient condition has a capacity cost which must not be
hidden.  If the whole selected table is split into `b` genuine subpalettes
such that, for every `z`, `gamma` is globally injective inside each
subpalette, then one subpalette contains at most

\[
                         (2m)(2m-1)                           \tag{3.2}
\]

heads.  Therefore

\[
                         b\ge
 \left\lceil{{\rm Cat}_m-h\over 2m(2m-1)}\right\rceil       \tag{3.3}
\]

after a protected bank of size `h` is contracted.  No constant number of
globally point-injective subpalettes works uniformly in `m`.  Equation
(3.3) applies only under this explicit global injectivity assumption; it
does not apply to reusable palette types whose literal point labels may
repeat.

The pointed-Steiner construction is one attempt to make the complete host
regular.  Its known divisibility failure at `m=8` does not contradict
Theorem 3.1: the latter concerns a prospectively selected, possibly
nonregular subtable.  It says precisely what the Ramsey host would need to
deliver in place of the impossible global regularization.

## 4. Interaction with the rolling reset and the support-three packet

Open and contract the seven protected `k=17` reset turns before applying
Theorem 3.1.  The theorem remains valid verbatim on the residual blocks if
complete fibre closure is interpreted **after** deleting the protected
tails.  In particular, a residual head whose old fibre met a protected tail
must either be contracted too or receive a literal replacement predecessor;
ordinary coordinate cover does not supply that replacement.

The bidirectional rolling-reset trade does not repair this row by itself.
Its two phases exchange one head--owner attachment path and two predecessor
parity paths.  On the closed ring any mixed local orientation creates the
owner doubleton, while on the opened ring the phase switch merely transports
the three endpoint defects.  It needs one external owner return and two
external predecessor returns and has no intrinsic positive Hall gain.

The owner two-cycle classification also explains why a nontrivial
support-two repair cannot be assumed.  The first owner-simple local
possibility is the typed Boolean support-three hexagon.  Its exact useful
form at this gate is the following standard augmentation criterion.

### Proposition 4.1 (disjoint literal-hex augmentation)

Let `M` be a matching in the reset-contracted predecessor graph with
deficiency `r`.  Suppose there are `r` vertex-disjoint `M`-augmenting paths,
each realized by one literal support-three Boolean hex packet, and suppose
their non-predecessor root, owner, target, and reset resources are mutually
disjoint and palette preserving.  Then toggling all packets gives a perfect
functional predecessor matching while retaining the opened reset bank.

This is immediate from the ordinary disjoint augmenting-path theorem; the
physical hypotheses make the graph toggles simultaneous legal flag-table
moves.

The missing assertion is the supply of those packets from a jointly chosen
high-target table.  Theorem 2.1 shows why a Ramsey coordinate cover cannot
replace it: the first deficient core already has order three even when all
singleton coordinate margins and local injections pass.

## 5. Exact boundary

The following are proved.

* Universal Cartesian coordinate cells are star-rigid and require
  Catalan-many actual cells.
* Two-sided row/column cover, separated pointed palettes, root/owner
  injectivity, and distinct `P/T` colours on the covered tail block do not
  imply Hall.
* Complete predecessor-fibre closure plus the exact left-load bound does
  imply Hall.
* A reset-conditioned family of disjoint literal support-three augmenters
  would close the remaining functional matching row.

What remains open is an all-root construction choosing the high-target
flags and functional owner bijection so that either the fibre-closed degree
criterion holds or the required support-three augmenting bank exists.  The
ordinary Ramsey coordinate-cover hypotheses are strictly too weak, while
the stronger universal-cell interpretation is quantitatively impossible.

## 6. Audit artifacts

The independently written bounded `-O3` audit was compiled and run on the
H100 CPU:

* `scratch/audit_k_d3_coordinate_cover_minimal_hall_obstruction_20260801.cpp`;
* `scratch/audit_k_d3_coordinate_cover_minimal_hall_obstruction_20260801.txt`.

SHA-256:

* source: `8c1f544605e94802a20fb5380c20ac6212cd9be4edf4670b59573f0541f4fb64`;
* output: `f7c8fb032e00b76ff5341a11f4a568e6513205fac6d0589a9c396a3facf6a3b5`.

The audit enumerates all `7!` labelings of the displayed `3 by 3` pattern,
checks the exact punctured-containment adjacency, and requires six distinct
root orbits, three distinct owner orbits, and separately distinct `P` and
`T` orbit families on the three covered tails.
