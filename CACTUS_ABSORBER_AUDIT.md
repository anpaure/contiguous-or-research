# Cactus/Berenstein--Kirillov relations as possible decorated absorbers

## 0. Verdict

No local cactus relation currently supplies the three-conjugate absorber
required by `MIXED_CONJUGATE_RESOLUTION.md`.

The sharp binary/two-row conclusions are:

1. Every nontrivial elementary Bender--Knuth microstep is a radius-preserving
   physical Johnson edge.
2. The smallest relation with two distinct all-active factorizations is a
   distant-generator commuting square.  Its two paths have the same
   endpoints, but different middle interiors.  Reinterpreting the square as
   two resolutions covering the same four middle vertices still fails:
   no Johnson four-cycle has the same lower **and** upper shadow multisets in
   its two perfect matchings.
3. The adjacent-generator relation produces no nondegenerate physical cycle
   in the two-row specialization.  The three occupied boxes have width at
   most two, so their toggle graph is a path; every closed adjacent-toggle
   word reduces by fixed steps and immediate backtracks.
4. General cactus interval relations do give equal endpoint operators, but
   endpoint equality does not imply a decorated trade.  Exhaustive binary
   tests through `m=6` find no nested cactus factorization whose two reduced
   physical paths have both the same middle multiset and the same separate
   lower/upper shadow multisets.

Thus the cactus relations are useful as a source of homotopies between
toggle paths, not as ready-made absorbers.  A larger composite of several
relation cells might still cancel their signed shadow discrepancies; that
possibility remains open and is stated precisely in Section 8.

The only external input used as background is Chmutov--Glick--Pylyavskyy,
[The Berenstein--Kirillov group and cactus groups](https://arxiv.org/abs/1609.02046).
Their paper proves that the cactus interval operators are represented in the
BK group and records the involution, disjoint-interval commutation, and
nested-interval conjugation relations.  All physical Johnson and shadow
claims below are proved separately in the binary standard-tableau
specialization.

## 1. What counts as an absorber here

Let a physical Johnson edge `XY` have typed decorations

\[
 L(XY)=X\cap Y,\qquad U(XY)=X\cup Y.                 \tag{1.1}
\]

Two collections `mathcal A,mathcal B` of radius-pure Johnson paths or blocks
form a **depth-one decorated trade** when

* they cover the same multiset of middle vertices;
* their multisets of lower decorations are equal; and
* their multisets of upper decorations are equal.

For a depth-`H` trade, the analogous equality is required separately for
every lower and upper depth through `H`.

Equality of path endpoints is much weaker than this definition.  It fixes
neither the internal middle vertices nor any shadow color.  This distinction
is the central audit guardrail.

## 2. Binary standard tableaux and physical microsteps

Encode a two-row standard tableau `Q` by its ballot word
`q_1...q_(2m)`, with `U` and `D` recording its two rows.  The elementary
standard-tableau Bender--Knuth move `tau_i` swaps the consecutive labels
`i,i+1` exactly when their boxes are incomparable.  In the ballot word this
is the adjacent swap

\[
 UD\longleftrightarrow DU                              \tag{2.1}
\]

whenever the swapped word remains ballot.

The inverse binary-RSK carrier calculation in
`BENDER_KNUTH_ISOMETRIC_CUBES.md` applies to every `i`, not only odd `i`:
whenever (2.1) is nontrivial, the two balanced inverse-RSK words differ in
exactly one selected and one unselected coordinate.  Tableau shape is
unchanged.  Hence:

### Theorem 1 (microstep admissibility)

Every nontrivial `tau_i` step on a two-row standard tableau is a physical
radius-preserving Johnson edge.

Fixed `tau_i` steps are identities, not length-one physical moves.  They may
be deleted from a state-specific path, but their deletion changes the word
length and prevents a formal group word from being treated automatically as
a uniform Johnson block.

## 3. The smallest relation: a commuting square

For `|i-j|>1`, the operators `tau_i,tau_j` act on disjoint labels and
commute.  When both are active throughout the square, the two words

\[
 \tau_i\tau_j,qquad \tau_j\tau_i                    \tag{3.1}
\]

give distinct radius-pure Johnson paths with the same endpoints.

This occurs already at `m=3`.  Take the ballot word

\[
 Q=UDUDUU
\]

and the one-based generators `tau_2,tau_4`.  The four inverse-RSK middle
sets are

\[
 \begin{array}{c|c}
 Q&\{1,3,6\}\\
 \tau_2Q&\{1,2,6\}\\
 \tau_4Q&\{1,4,6\}\\
 \tau_2\tau_4Q&\{2,4,6\}.
 \end{array}                                          \tag{3.2}
\]

The paths through `tau_2Q` and `tau_4Q` have different internal middle
vertices, so (3.1) is not itself a middle-balanced trade.

There is a natural stronger attempt: use the two parallel-edge perfect
matchings of the square.  Both resolutions then cover all four middle
vertices.  In (3.2), the first resolution has decorated edges

\[
 \begin{array}{c|c}
 L&U\\ \hline
 \{1,6\}&\{1,2,3,6\}\\
 \{4,6\}&\{1,2,4,6\},
 \end{array}                                          \tag{3.3}
\]

whereas the second has

\[
 \begin{array}{c|c}
 L&U\\ \hline
 \{1,6\}&\{1,3,4,6\}\\
 \{2,6\}&\{1,2,4,6\}.
 \end{array}                                          \tag{3.4}
\]

Both typed shadow multisets differ.

This is not an accident of the example.

### Theorem 2 (no decorated Johnson-square trade)

Let `A-B-D-C-A` be a four-cycle of four distinct vertices in `J(n,m)`.
The two perfect matchings

\[
 \{AB,CD\},\qquad\{AC,BD\}                           \tag{3.5}
\]

cannot have simultaneously equal lower-shadow multisets and equal
upper-shadow multisets.

### Proof

Write two neighbours of `A` as

\[
 B=A-a+b,qquad C=A-c+d.                              \tag{3.6}
\]

There are three possible four-cycle geometries.

* If `a=c`, all four vertices share one rank-`m-1` set.  Every edge has the
  same lower shadow, but the two perfect matchings pair four distinct added
  elements in two different ways, so their upper-shadow multisets differ.
* If `b=d`, dually all four vertices lie in one rank-`m+1` set.  Their upper
  shadows agree and their lower-shadow multisets differ.
* If `a!=c` and `b!=d`, the fourth vertex is

  \[
   D=A-\{a,c\}+\{b,d\}.
  \]

  This is the ordinary coordinate rectangle.  Directly, the first matching
  deletes/fills the `{a,b}` direction and the second the `{c,d}` direction;
  both their lower and upper type families differ.

The cases exhaust (3.6), proving the theorem.  QED.

Consequently the smallest cactus/BK relation with two physical
factorizations is not even a depth-one absorber.

## 4. Adjacent BK relations collapse in two rows

The BK group has the relation `(t_1t_2)^6=I`; the cited paper records it as
the one classical known BK relation not arising from cactus relations.  One
might hope that a shifted pair `tau_i,tau_(i+1)` produces an alternating
hexagon or dodecagon of radius-pure Johnson moves.

It does not in the binary/two-row standard specialization.

### Theorem 3 (no adjacent-toggle cycle)

Fix the three boxes occupied by labels `i,i+1,i+2` in a two-row standard
tableau.  The graph of their possible labelings under `tau_i,tau_(i+1)` is
a path.  In particular it contains no nontrivial all-active alternating
cycle.

### Proof

The three boxes inherit a poset of width at most two from the Ferrers
diagram.  They cannot be a three-element antichain.  Their possible
standard labelings are precisely the linear extensions of this induced
three-element poset, and `tau_i,tau_(i+1)` are its adjacent swaps.

For a three-element poset with at least one comparison, the adjacent-swap
graph of its linear extensions is a path: it has respectively one, two, or
three vertices according to the comparison pattern.  The six-cycle occurs
only for a three-element antichain, which width two excludes.  QED.

Thus every realization of an adjacent BK power relation contains a fixed
move or an immediate reversal.  After deleting identities and cancelling
spurs `X-Y-X`, nothing remains that could serve as a physical cycle block.

At the bottom indices the obstruction is even more elementary: label `1`
occupies the northwest box and label `2` is comparable with it, so `tau_1`
is always fixed on a standard tableau.

## 5. General cactus interval relations

Using the notation of Chmutov--Glick--Pylyavskyy, interval operators satisfy

\[
 q_{[i,j]}^2=I,                                       \tag{5.1}
\]

commute on disjoint intervals, and obey the nested conjugation law

\[
 q_{[i,l]}q_{[j,k]}q_{[i,l]}
   =q_{[i+l-k,\,i+l-j]}
 \qquad(i\le j<k\le l).                              \tag{5.2}

They expand into Bender--Knuth generators via

\[
 q_{[i,j]}=q_{j-1}q_{j-i}q_{j-1},
 \qquad
 q_r=t_1(t_2t_1)\cdots(t_r\cdots t_1).               \tag{5.3}

In a standard tableau the displayed word (5.3) always contains fixed
`tau_1` steps.  Deleting every fixed step state by state leaves a physical
radius-pure Johnson path by Theorem 1, but generally with a variable length.
The two sides of (5.2) then have the same endpoint and no further automatic
incidence equality.

There is a useful structural interpretation.  Two-row tableaux are ballot
paths, and active toggles exchange adjacent `UD,DU` steps.  Their toggle
graph is the cover graph of the corresponding distributive lattice of
lattice paths.  Its elementary two-cells are distant-toggle commuting
squares.  Thus cactus homotopies in the binary specialization are built
from the square cells already rejected by Theorem 2, together with
backtracks.

This does not prove that signed discrepancies from many squares can never
cancel.  It proves that cancellation is additional absorber structure, not
a consequence of the cactus relation itself.

## 6. Fixed-coordinate cube obstruction

The square failure extends to complete direction matchings in one genuine
fixed-coordinate cube.  Let its free pairs be `P_1,...,P_s` and its fixed
included core be `C`.  The lower shadows of the full direction-`i` matching
are exactly the sets which

* contain `C`;
* contain neither member of `P_i`; and
* contain one member of every other free pair.

Therefore the lower-shadow families belonging to different directions are
disjoint: the unique empty free pair identifies the direction.  Dually, the
upper families are disjoint because the unique full free pair identifies
the direction.

### Proposition 4 (direction-count rigidity)

Two unions, with multiplicity, of complete direction matchings in one
fixed-coordinate cube have equal lower-shadow multisets (or equal upper
shadow multisets) only when they use every direction with the same
multiplicity.  They then contain the same edge multiset.

Hence cactus commutations confined to one isometric cube generate no
nontrivial decorated matching trade.  This proposition does not cover
partial direction matchings spread across several coordinate conjugates;
those are exactly the configurations an eventual absorber must exploit.

## 7. Promotion and evacuation words

Promotion and interval evacuation can be expanded into elementary toggles.
After fixed microsteps are removed, every remaining microstep is admissible
by Theorem 1.  Their macro endpoints, however, are not local Johnson moves:
`TABLEAU_CRYSTAL_AUDIT.md` gives a two-row promotion family changing
`2m-2` ground coordinates, and evacuation induces reverse-complement, which
is either fixed or changes at least four coordinates.

Accordingly these operators provide long radius-pure **walks**, not one
absorber edge.  Their standard words have length growing with the interval
and contain state-dependent identities and backtracks.  No second
factorization with the same complete decorated incidence has been found.
Treating the macro operator itself as a Johnson step would be invalid.

## 8. Exhaustive audit and the remaining search target

The checker

```text
scratch/check_cactus_absorbers.py
```

enumerates all two-row tableaux, computes inverse binary RSK, expands
(5.2)--(5.3), deletes fixed microsteps, cancels immediate path spurs, and
compares middle, lower, and upper multisets separately.  Through `m=6` it
finds:

```text
m   active distant squares   reduced distinct cactus paths
2             0                          0
3            16                        265
4           180                       1996
5          1344                       6866
6          8400                      24350
```

There are zero equal-middle or equal-decorated pairs in every row.  The
adjacent two-generator graphs contain no cycles, as Theorem 3 predicts.

The auxiliary search

```text
scratch/search_three_bk_squares.py
```

looks for two or three vertex-disjoint active BK squares whose signed
depth-one lower and upper discrepancies cancel.  It finds none through
`m=5` (3, 36, and 280 distinct positive-radius squares for `m=3,4,5`).
This is finite evidence, not an impossibility theorem.

The first still-credible cactus-inspired target is therefore:

> Find a bounded connected complex of at least three coordinate-conjugated
> commuting squares whose two resolutions cover exactly the same middle
> vertices and whose signed lower and upper discrepancies cancel; then test
> the same equality simultaneously at every depth carried by the blocks.

Theorem 2 rules out one square, Proposition 4 rules out merely cycling whole
directions inside one fixed cube, and Theorem 3 removes the adjacent-toggle
hexagon.  Any successful complex must mix genuinely different coordinate
pair systems or nonlocal carrier supports.

## 9. Final ledger

| statement | status |
|---|---|
| nontrivial standard BK microstep is a radius-pure Johnson edge | proved |
| distant commutation is the smallest two-path relation | proved |
| a Johnson square is a decorated absorber | false |
| adjacent BK power relation gives a physical two-row cycle | false |
| complete direction factors inside one isometric cube trade nontrivially | false |
| tested nested cactus relations give a decorated trade through `m=6` | false computationally |
| no composite cactus complex can ever absorb | not proved |
| a bounded three-conjugate decorated absorber exists | open |

The cactus/BK relations therefore clarify the local topology but do not
close the integral resolution conjecture.  The missing object must be a
new decorated relation among several conjugated physical blocks, not a
standard cactus identity read only at its endpoints.
