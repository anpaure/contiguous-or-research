# Masked core triangles have large loose trees: the remaining ring-state gate

## Status

The masked-core C6 tensor is a genuine zero-charge cross-core connector.
Its local rank, topology, immediate-palette and residence calculations are
correct.  The abstract 3-uniform hypergraph of possible invariant cores is
not merely connected: every maximal loose tree contains at least a fixed
positive fraction of all core vertices.  Hence it contains loose trees far
larger than the `Theta(W/q)` ring count required by a near-maximal schedule.

There is nevertheless one global quantifier left.  A selected ring is not
specified by its core alone: its moving set, unused set, cyclic order and
literal occurrence tickets determine which masked triangles it can expose.
The core/moving/unused partition-state projection is connected and has
explicit elementary moves, but an abstract loose core tree does not
automatically lift to one compatible tree of cyclic, occurrence-labelled
ring states.  This note gives the exact state condition.

No computation or search is used.

## 1. Local audit and one correction

Put

\[
             n=2q-1,\qquad s=q-h.
\]

For an `(s-1)`-set `H` and distinct labels `a,b,c` outside `H`, the masked
triangle has cores

\[
                    H+a,\quad H+b,\quad H+c.           \tag{1.1}
\]

At one cut the old and rejoined cumulative unions are

\[
 \begin{aligned}
 L_i^a&=H+a+b+\Lambda_i,\\
 R_j^a&=H+a+P_j,\\
 R_j^b&=H+b+P_j,
 \end{aligned}
\]

and therefore

\[
              L_i^a\cup R_j^b=L_i^a\cup R_j^a         \tag{1.2}
\]

addresswise.  With the common ordered filler bank included, both sides
have rank `q-h+i+j`.  Thus widths `h-1,h,h+1` are respectively roots,
owners and immediate uppers, all with zero signed current.  The cyclic tail
permutation merges the three components, and the run/gap calculation at
period `ell>=2h` is unchanged.

The only correction to the first frozen statement is that fixed-width row
simplicity holds for

\[
                         1\le w<\ell,                  \tag{1.3}
\]

not for `w=ell`: all `ell` full-cycle windows in one input ring have the
same value.  Since `h+1<ell` in the near-maximal regime, this does not
affect the immediate root/owner/upper theorem.

## 2. The core-triangle hypergraph

Let `mathcal H_(n,s)` have vertex set `binom([n],s)`.  Its hyperedges are
the triples

\[
              \{H+a,H+b,H+c\},                         \tag{2.1}
\]

where `|H|=s-1` and `a,b,c` are distinct outside `H`.

### Proposition 2.1 (exact degrees)

The hypergraph is regular with

\[
 d_1=s\binom{n-s}{2},                                  \tag{2.2}
\]

and its maximum pair-codegree is

\[
 d_2=n-s-1.                                            \tag{2.3}
\]

The two-section of `mathcal H_(n,s)` is exactly the Johnson graph
`J(n,s)`.

#### Proof

For a fixed core `V`, choose the deleted element `x in V`, giving the base
`H=V-x`, and then choose the other two extensions from the `n-s` labels
outside `V`.  This gives (2.2), without overcounting because the common
intersection of a hyperedge is its unique `(s-1)`-base.

Two vertices lie in a common hyperedge exactly when they share `s-1`
elements.  Their common base is then unique, and the third extension can
be any of the `n-s-1` labels not used by the pair, proving (2.3) and the
two-section assertion. \(\square\)

At critical width, `d_1=Theta(q^3)` and `d_2=Theta(q)`, so
`d_2/d_1=Theta(q^-2)`.

## 3. A positive-density loose tree

### Theorem 3.1 (every maximal loose tree is large)

Every maximal loose tree in `mathcal H_(n,s)` has at least

\[
             {n-s\over n}\binom ns                    \tag{3.1}
\]

vertices.  Consequently, for every odd integer `m` with

\[
       3\le m\le {n-s\over n}\binom ns,                \tag{3.2}
\]

the hypergraph contains a loose tree on exactly `m` vertices.

#### Proof

Start from one hyperedge and repeatedly add a hyperedge meeting the current
vertex set `U` in exactly one vertex.  When this process is maximal, fix
`V in U` and one of its `s` bases `H=V-x`.  At most one other extension of
`H` can lie outside `U`; otherwise `V` together with two outside extensions
would be an admissible next loose edge.  Every Johnson neighbor of `V` has
a unique base with `V`, so

\[
                      deg_{U^c}(V)\le s.                \tag{3.3}
\]

Hence the Johnson edge boundary satisfies

\[
                      e(U,U^c)\le s|U|.                 \tag{3.4}
\]

The Johnson graph `J(n,s)` is `d=s(n-s)` regular and has second adjacency
eigenvalue `d-n`.  Its exact spectral boundary inequality is therefore

\[
 e(U,U^c)\ge n|U|\left(1-{|U|\over\binom ns}\right).   \tag{3.5}
\]

Combining (3.4)--(3.5) gives

\[
                   {|U|\over\binom ns}\ge1-{s\over n}
                      ={n-s\over n},
\]

which is (3.1).  The greedy process adds two new vertices at each step, so
one may stop at any odd size before its maximal endpoint. \(\square\)

### Corollary 3.2 (the near-maximal ring count fits easily)

Let `h=O(sqrt(q))`, and let `c` be any scalar ring schedule using periods
`q+h-3,q+h-2`.  Then, for all sufficiently large `q`,

\[
                  c\le {n-s\over n}\binom ns.          \tag{3.6}
\]

Thus `mathcal H_(n,s)` contains a loose tree on `c` vertices when `c` is
odd, and on `c-1` vertices when `c` is even.

#### Proof

Writing `W=binom(2q-1,q)`, the scalar schedule has

\[
                      c\le {W\over q+h-3}.              \tag{3.7}
\]

Also

\[
 {W\over\binom ns}
   =\prod_{j=0}^{h-1}{q+j\over q-j}
   \le \exp\!\left({h(h-1)\over q-h+1}\right),         \tag{3.8}
\]

which is bounded when `h=O(sqrt(q))`.  The right side of (3.6) is
`(1/2+o(1)) binom(n,s)`, whereas (3.7) is only
`O(binom(n,s)/q)` by (3.8).
This proves (3.6). \(\square\)

This closes the *abstract core-label topology*.  It does not yet select
the owner-disjoint rings attached to those labels.

## 4. The exact collar-state action

A literal ring state consists at minimum of

\[
                (V,F,U,pi),                             \tag{4.1}
\]

where `V` is its `s`-element core, `F` is its `ell`-element moving set,
`U=[n]-(V union F)` is unused, and `pi` is the cyclic order on `F` with a
chosen special cut marker.

For a fixed ring `(V,F,U)`, a masked triangle incident with it has the
exact form

\[
       V,qquad V-a+b,qquad V-a+c,                    \tag{4.2}
\]

where

\[
                         a\in V,\quad b\in F,quad c\in U.   \tag{4.3}
\]

Hence the number of oriented local port roles exposed by that ring before
cyclic-order and ticket restrictions is

\[
                         |V||F||U|=s\ell(n-s-\ell).     \tag{4.4}
\]

For periods `ell_+=q+h-2` and `ell_-=q+h-3`, the unused-set sizes are one
and two, respectively, so (4.4) is `s ell_+` and `2s ell_-`.

### Proposition 4.1 (state compatibility is sparse inside the core degree)

Put `D=n-s`.  The fraction of abstract core hyperedges incident with a
fixed ring core which can use one fixed partition `(V,F,U)` in the role
(4.2)--(4.3) is

\[
 {s\ell|U|\over s\binom D2}
       ={2\ell|U|\over D(D-1)}.                        \tag{4.5}
\]

For either near-maximal period this is `Theta(1/q)`.

Moreover, fix a core triangle and choose independently and uniformly an
unused `u`-set at each of its three core vertices, where `u=1` or `2`.
The probability that either cyclic orientation has the required
unused/moving roles is at most

\[
                         2\left({u\over D}\right)^3
                         =O(q^{-3}).                    \tag{4.6}
\]

This estimate does not yet price agreement of the three cyclic filler
orders, which is an additional correlation.

#### Proof

Equation (4.5) divides the exact role count (4.4) by the full core degree
(2.2).  For one cyclic orientation of a fixed triangle, each of its three
rings must place one prescribed outside label in its unused set.  This has
probability `u/D` at each vertex.  Union-bound the two orientations to get
(4.6). \(\square\)

Thus a masked connector tree cannot be expected to appear after an
independently rounded ring factor.  The ring triples and their orders must
be selected in correlation with the one-copy owner/root cover.

### Lemma 4.2 (masked triangle reverses a directed state cycle)

Write a collar state as `(H+u,x)`, where the first entry is the core and
`x` is the special moving marker.  Here the full first-ring partition is

\[
 V=H+u,\qquad F=G+x,\qquad U=Z+y,                     \tag{4.7}
\]

so in particular `u in V`, `x in F`, and `y in U`.  The other two rings
cyclically rotate these three exceptional labels.  The three input states

\[
       (H+u,x),\qquad(H+x,y),\qquad(H+y,u)              \tag{4.8}
\]

are transformed by the masked splice into the three output states

\[
       (H+x,u),\qquad(H+y,x),\qquad(H+u,y).             \tag{4.9}
\]

Thus the port reverses the directed triangle on the three adjacent cores.

#### Proof

At the cut belonging to core `H+u`, its left cumulative profile contains
both `u` and `x`.  After attaching the right profile of the `H+x` ring,
the regenerated collar has core `H+x` and special left marker `u`.  This
is the first state in (4.9).  Cyclic translation gives the other two.
Equation (1.2) is the simultaneous addresswise OR identity. \(\square\)

### Corollary 4.3 (the partition-state projection is connected)

From a full state `(V,F,U)` and choices

\[
                         u\in V,\quad x\in F,\quad y\in U,
\]

one masked port exposes the following three partition states:

\[
 \begin{array}{c|c|c}
 \text{core}&\text{moving}&\text{unused}\\ \hline
 V-u+x&F-x+u&U,\\
 V-u+y&F&U-y+u,\\
 V&F-x+y&U-y+x.
 \end{array}                                           \tag{4.10}
\]

At the collar level it also exposes both

\[
       (H+u,y)\quad\hbox{and}\quad(H+x,u).              \tag{4.11}
\]

Consequently the projection of the masked-port state graph onto ordered
partitions `(V,F,U)` of fixed sizes is connected: the three outputs perform
respectively a core--moving, core--unused, and moving--unused exchange.

#### Proof

The three rows of (4.10) are obtained by reading the moving and unused
sets from the output states in (4.9): the common banks `G,Z` remain fixed
and the exceptional labels are transposed.  Pairwise exchanges between
the three cells of an ordered set partition generate all ordered
partitions with those cell sizes. \(\square\)

This is only connectivity of the category projection.  It does not prove
connectivity with a prescribed cyclic order, occurrence tickets, or capped
ages, nor that the two required fresh companion rings occur in a fixed
one-copy factor.  In particular `y` is not an arbitrary outside label for
one fixed ring: it must lie in that ring's unused set.

## 5. The precise remaining integral gate

The abstract core obstruction and the former six-seam upper-current
obstruction are both gone.  The remaining theorem is an
occurrence-resolved lift of Theorem 3.1:

> **Masked-ring loose-tree cover-down.**  Select exactly one occurrence of
> every owner and root into rings of periods `q+h-3,q+h-2`, and orient a
> loose tree on all but at most one selected ring, so that every incident
> triangle obeys (4.2)--(4.3), its three cyclic filler orders agree, its
> reused output collar is the next literal input collar, all nonlocal
> upper/lower tickets avoid the cuts or are transported, and the final
> capped ages pass.

Serial collar reuse means an original ring need supply only its first
input collar; later appearances of a shared core may use the collar created
by the preceding splice.  This removes the need to plant two independent
collars in every internal original ring.  It does **not** remove the need
to choose the two fresh companion rings with the exact moving/unused and
cyclic-order states required by (4.8).

Theorem 3.1 proves that there is ample abstract core topology, and
Corollary 4.3 removes any invariant at the level of the three category
sets.  The unsolved content is their simultaneous cyclic and
occurrence-resolved realization inside the one-copy decorated ring cover.
