# Adjacent necklaces: shifted-quiet full-merge fibres and the exact cross-fibre obstruction

**Date:** 2026-08-05  
**Method:** a rotation-equivariant defect-erasing normal form, cyclic
segmentation, and an exact orbit count; no computation  
**Status:** unconditional reduction and no-go theorem.  The full-merge map
does partition the shifted-quiet critical domain, but its fibres cannot in
general be matched independently with deficiency at most one.  The first
explicit obstruction occurs at the all-one merged base of length fifteen.

## 1. Input: the shifted-quiet critical domain

Fix an odd coordinate length `q`.  After terminal-fracture fibres and the
internal allocation path products are matched, every surviving long
positive run has one of the forms

\[
 (o_1,1,o_2,1,\ldots,o_h,2),                       \tag{1.1}
\]

or

\[
 (a,o_1,1,\ldots,o_h,2),                           \tag{1.2}
\]

where every \(o_i\) is positive and odd, while `a` is an arbitrary
positive free coordinate.  The run is followed by one zero.  Unit blocks
\((1,0^g)\) may also occur.

Call the necklaces with this property the **shifted-quiet critical
domain**.  This note studies only the literal exit edges

\[
                  (o,2,0)\longleftrightarrow(o,1,1),
                  \qquad o\text{ odd}.              \tag{1.3}
\]

It does not discard the other adjacent transfers of the ambient graph.

## 2. The full-merge normal form

For a shifted-quiet critical composition `x`, apply (1.3) in the forward
direction at the terminal defect of every long block, simultaneously.
Denote the result by \(M(x)\).

### Lemma 2.1 (well-defined normal form)

The map `M` is well defined, preserves coordinate length and total mass,
commutes with rotation, and is injectively labelled by its terminal cut
set once its value is fixed.

#### Proof

Distinct long positive runs have distinct terminal coordinates and
distinct following zeroes.  Thus the supports of their forward exits are
disjoint.  Each operation replaces `2,0` by `1,1`, preserving both length
and mass.  The set of maximal positive runs and their terminal coordinates
is defined cyclically, so the construction commutes with rotation.

If `B=M(x)`, record the former terminal coordinates in a set `S`.  Recover
`x` by replacing `B_j,B_(j+1)=1,1` with `2,0` for every `j in S`.
Therefore `B` together with `S` recovers `x` uniquely. \(\square\)

For a merged word `B`, define \(\operatorname{Adm}(B)\) to be the family
of cut sets `S` for which the simultaneous reverse replacements

\[
              (B_j,B_{j+1})=(1,1)\longmapsto(2,0),
              \qquad j\in S,                        \tag{2.1}
\]

are disjoint and produce a shifted-quiet critical composition.  This is a
local cyclic segmentation condition: consecutive selected cuts delimit
exactly the run words (1.1)--(1.2), while the unselected fixed zeroes of
`B` delimit the untouched unit blocks.

### Theorem 2.2 (exact fibre and toggle subgraph)

For every merged necklace `[B]`, its shifted-quiet preimage is

\[
       \{[x_S]:S\in\operatorname{Adm}(B)\}/\operatorname{Stab}(B),
                                                        \tag{2.2}
\]

where `x_S` is obtained from (2.1).  Different merged necklaces have
disjoint preimages.  The literal exit edges inside this fibre contain the
simple toggle graph

\[
 S\longleftrightarrow S\triangle\{j\}
 \quad\text{whenever both cut sets are admissible}.    \tag{2.3}
\]

#### Proof

Lemma 2.1 gives the labelled statement.  If rotations carry `x_S` to
`x_T`, applying `M` shows that the same rotation stabilizes `B` and carries
`S` to `T`; the converse is immediate.  Since `M` is a function, distinct
values of `[B]` have disjoint preimages.  Adding or deleting one admissible
cut is exactly one application of (1.3), proving (2.3). \(\square\)

The word “contain” in the last sentence is deliberate.  Other ambient
adjacent transfers may leave the full-merge fibre or may join two
segmentations by a longer alternating Schur path.  They are precisely the
resources needed after the obstruction below.

## 3. The all-one fibre is a sparse-subset toggle graph

Take

\[
                              B=1^q.                 \tag{3.1}
\]

There are no fixed zeroes and every possible reverse cut has the local
form `1,1,1 -> 1,2,0`.

### Theorem 3.1 (exact all-one segmentation)

The admissible cut sets for (3.1) are exactly the nonempty cyclic subsets
\(S\subseteq\mathbb Z_q\) whose distinct elements have cyclic distance at
least three.  Consequently the exit subgraph of this fibre is the Hasse
toggle graph of nonempty `2`-independent subsets of the cycle, modulo
rotation.

#### Proof

A selected centre `j` creates the terminal `2` at `j` and its following
zero at `j+1`.  If the next selected centre is `k`, the positive run between
these zeroes is

\[
                    (1,1,\ldots,1,2).               \tag{3.2}
\]

It has length `k-j-1` cyclically.  It belongs to (1.1) or (1.2) exactly
when that length is at least two.  Since all displayed entries before the
terminal two are one, every required odd/one alternation is automatic.
Thus consecutive cyclic cuts must, and may, be separated by at least
three coordinates.

The cut set cannot be empty because `1^q` itself has no zero and hence is
not a boundary composition in the shifted-quiet domain.  Toggling one cut
is exactly (1.3). \(\square\)

## 4. Every cut-cardinality layer is a smaller necklace set

Let `S` have `k` cuts, in cyclic order, and let

\[
                   g_1,\ldots,g_k\ge3,
                   \qquad \sum_i g_i=q               \tag{4.1}
\]

be their cyclic gaps.  Put \(e_i=g_i-3\).

### Corollary 4.1 (smaller-necklace layer)

The rotation orbits of admissible `k`-cut sets are in canonical bijection
with

\[
                     \mathcal N_{k,q-3k},            \tag{4.2}
\]

the weak-composition necklaces of mass \(q-3k\) on `k` cyclic slots.

#### Proof

Equation (4.1) is equivalent to a weak composition

\[
                   (e_1,\ldots,e_k),
                   \qquad e_i\ge0,quad\sum e_i=q-3k.
\]

Changing the first named cut cyclically rotates this composition, and no
other identification occurs. \(\square\)

Thus the Schur-critical all-one fibre is not an opaque family.  Its levels
are the explicit smaller adjacent-necklace state sets

\[
  \mathcal N_{1,q-3},\mathcal N_{2,q-6},\ldots,
  \mathcal N_{\lfloor q/3\rfloor,q-3\lfloor q/3\rfloor},
                                                        \tag{4.3}
\]

and an exit toggle moves between consecutive levels by splitting or
coalescing cyclic gaps.

## 5. A sharp fibrewise obstruction at q=15

The toggle graph is bipartite by the parity of `|S|`.  We now count its
two orbit shores exactly when `q=15`.

### Theorem 5.1 (deficiency two in the all-one merge fibre)

For \(q=15\), the numbers of rotation-orbit vertices with
\(|S|=1,2,3,4,5\) are respectively

\[
                              1,5,10,5,1.            \tag{5.1}
\]

Hence the odd shore has size twelve and the even shore size ten.  Every
matching using only the exit-toggle edges leaves at least two vertices
unmatched.

#### Proof

Use Corollary 4.1.

* `k=1`: there is one weak composition of mass twelve on one slot.
* `k=2`: weak compositions of nine on two cyclic slots are unordered pairs
  \((a,9-a)\), giving five orbits.
* `k=3`: Burnside on weak compositions of six gives

  \[
  {1\over3}\left({8\choose2}+2\right)=10,            \tag{5.2}
  \]

  since each nontrivial rotation fixes only `(2,2,2)`.
* `k=4`: the identity fixes \({6\choose3}=20\) weak compositions of
  mass three.  No nonidentity rotation fixes one, since an orbit-constant
  four-tuple has total divisible by two or four.  Hence there are five
  orbits.
* `k=5`: mass zero gives one orbit.

The odd levels `k=1,3,5` contain `1+10+1=12` vertices; the even levels
contain `5+5=10`.  Every toggle changes `k` by one, so a matching covers
at most ten vertices on each shore and has deficiency at least two.
\(\square\)

This is not a counterexample to near-perfect matching in the full
adjacent-necklace graph.  It is a counterexample to the proposed strategy
of matching every fully merged exit fibre independently.

## 6. Schur-complement meaning

The terminal-fracture and path-product stages leave one critical vector
per exceptional allocation fibre.  Applying only the literal exit matrix
on those vectors gives the toggle operator (2.3).  Theorem 5.1 says that
this first-order critical operator has nullity at least two at `q=15`.

Therefore a successful interacting skew operator must retain at least one
of the following before taking its Schur complement:

1. allocation edges whose alternating paths join different merged bases;
2. unit-block slide edges, which change `B`;
3. higher alternating paths through already matched path-product fibres;
   or
4. a coupled normalization which groups several merged bases at once.

Equivalently, the effective critical graph cannot be merely the disjoint
union of the full-merge fibres.  Cross-base terms are forced by an exact
parity count, not only by a concern about overlapping local moves.

Corollary 4.1 supplies a useful target for those terms: at fixed `k`, the
critical vertices are already a smaller necklace layer.  The missing
Schur edges should be sought as literal adjacent transfers inducing the
smaller graph's mass moves, together with vertical edges between `k` and
`k+1`.

## 7. Scope

Proved:

1. a rotation-equivariant full-merge normal form on the shifted-quiet
   critical domain;
2. its exact occurrence-labelled cut-set fibres;
3. the exact all-one fibre as a sparse cyclic-subset toggle graph;
4. identification of every cut-cardinality layer with
   \(\mathcal N_{k,q-3k}\); and
5. an exact deficiency-at-least-two obstruction to fibrewise matching at
   `q=15`.

Not proved or disproved:

1. near-perfect matching after cross-base Schur edges are restored;
2. a collision-free choice of those alternating paths;
3. protected radial socket compatibility; or
4. any universal-word upper bound.

