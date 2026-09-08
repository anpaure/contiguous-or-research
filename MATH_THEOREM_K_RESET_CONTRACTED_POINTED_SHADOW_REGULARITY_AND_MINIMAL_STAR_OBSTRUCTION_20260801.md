# Reset-contracted pointed shadows: an exact regular Hall face and the minimal star obstruction

**Date:** 2026-08-01  
**Lane:** K, functional attachment after a protected rolling reset  
**Status:** unconditional all-parameter sufficient theorem and a smallest
literal obstruction.  The theorem verifies the complete predecessor-Hall
row once a high-target table and a functional owner alignment satisfy two
explicit Boolean closure conditions.  It does not prove that such a table
exists in every dimension, or that the authenticated `k=17` table satisfies
the conditions.

## 0. Result

Fix one phase of an opened reset bank and contract its used tails, heads,
and owners.  Fix a selected depth-three high-target flag table, a bijection
from residual heads to residual owners, and a physical alignment label at
each head.  The functional predecessor graph splits by alignment label
`z` into the pointed-shadow graphs

\[
 S\sim(H,\gamma)
 \quad\Longleftrightarrow\quad
 S=H-\{\beta\}\text{ for some }\beta\in H-\{\gamma\}.
 \tag{0.1}
\]

For any balanced block, Hall follows from the elementary but useful
degree condition

\[
 \min_{(H,\gamma)}d(H,\gamma)
       \ \ge\ \max_S d(S)>0.                              \tag{0.2}
\]

In the Boolean host, (0.2) has a literal integral realization.  It is
enough that

1. every selected pointed head retains its complete punctured-facet fibre;
2. for every selected tail `S` and every pointer `gamma in S`, at most one
   selected head extends the pointed facet `(S,gamma)`.

Then every head has degree `m-2`, every tail has degree at most `m-2`, and
equal shore sizes force the graph to be `(m-2)`-regular.  Consequently it
has a perfect matching.  This supplies the exact owner/tail/head chronology,
and owner bijectivity automatically excludes the closed directed
two-cycles classified in the overlap-core theorem.

The condition is genuinely restrictive.  At `(k,m,d)=(7,3,3)`, two
distinct pointed heads with the same pointer can have the same unique
predecessor.  Together with one unused tail they form a balanced literal
two-by-two block of matching size one.  This is the smallest pointed-shadow
Hall obstruction compatible with complete individual predecessor fibres.

Thus the remaining all-dimensional construction problem is not an
unstructured three-matroid intersection.  A sufficient exact target is a
reset-compatible high-target table and functional alignment whose pointed
shadow incidence is a disjoint union of the regular blocks proved below.
Whether the Boolean/Pascal selector can always be chosen on this face is
open.

## 1. Functional blocks after protected contraction

Assume throughout that `m>=3`.  Use the depth-three normalized notation.
A tail flag with aligned exterior
label `z` has the form

\[
                         (S,z),\qquad |S|=m-2,               \tag{1.1}
\]

and a head flag has signature

\[
                         (H,\gamma),\qquad |H|=m-1,
                         \quad\gamma\in H.                  \tag{1.2}
\]

The complete literal turn law for fixed `z` is

\[
 (S,z)\longrightarrow(H,\gamma)
 \quad\Longleftrightarrow\quad
 S\subset H,\quad\gamma\in S,\quad z\notin H.             \tag{1.3}
\]

Equivalently, the possible predecessors of `(H,gamma)` are

\[
 (H-\{\beta\},z),\qquad \beta\in H-\{\gamma\}.             \tag{1.4}
\]

The owner is `H union {0,z}`.  These are literal, occurrence-aligned
statements; quotient equality by itself is not being used.

Let `L_z` be the selected residual tail flags carrying label `z`, and let
`R_z` be the residual head flags whose chosen functional owner alignment is
`z`.  The label-flux equations require

\[
                         |L_z|=|R_z|.                         \tag{1.5}
\]

Delete every tail, head, and owner used by the protected reset.  Let
`G_z` be the residual bipartite graph defined by (1.3).  A perfect matching
in every `G_z`, together with the protected reset turns, is exactly a
perfect matching of the functional predecessor graph.

## 2. The degree-dominance Hall lemma

### Lemma 2.1 (balanced degree dominance)

Let `G=(L,R;E)` be a finite bipartite graph with `|L|=|R|`.  If

\[
 \delta:=\min_{v\in R}d(v),\qquad
 \Delta:=\max_{u\in L}d(u),\qquad
                         \delta\ge\Delta>0,                  \tag{2.1}
\]

then `G` has a perfect matching.

#### Proof

For any `Y subseteq R`, every edge incident with `Y` ends in `N(Y)`, so

\[
 \delta|Y|\le e(Y,N(Y))\le\Delta|N(Y)|.                    \tag{2.2}
\]

As `delta>=Delta>0`, this gives `|N(Y)|>=|Y|`.  Hall's theorem gives a
matching saturating `R`, and (1.5) makes it perfect.  \(\square\)

This lemma is deliberately stronger than a scalar average-degree bound.
It proves every Hall cut simultaneously.

## 3. Boolean full-fibre regularity

Call a balanced block `(L_z,R_z)` **full-fibre closed** if

\[
 (H,\gamma)\in R_z,\ \beta\in H-\{\gamma\}
 \quad\Longrightarrow\quad
                         (H-\{\beta\},z)\in L_z.             \tag{3.1}
\]

Thus every residual head retains all of its `m-2` literal predecessors.
For a protected contraction, (3.1) includes the requirement that no such
predecessor is one of the deleted reset tails.

Call the block **pointed-simple** if for every `S in L_z` and every
`gamma in S`,

\[
 \left|\{\beta:(S+\{\beta\},\gamma)\in R_z\}\right|\le1,   \tag{3.2}
\]

where only legal external `beta` satisfying (1.3) are counted.  This is a
local condition on pointed facets; it does **not** require `gamma` to be
globally injective in the whole block.

### Theorem 3.1 (pointed-shadow regularity, `m>=3`)

Every balanced, nonempty, full-fibre-closed, pointed-simple block `G_z` is
`(m-2)`-regular and has a perfect matching.

#### Proof

By (3.1), each head `(H,gamma)` has exactly the `m-2` neighbours in
(1.4).  Hence

\[
                         d_R(H,\gamma)=m-2.                  \tag{3.3}
\]

For a fixed tail `S`, every adjacent head has a pointer `gamma in S`.
Condition (3.2) permits at most one adjacent head for each of the `m-2`
choices of `gamma`, so

\[
                         d_L(S)\le m-2.                      \tag{3.4}
\]

Lemma 2.1 already gives a perfect matching.  Moreover, the sum of the head
degrees is `(m-2)|R_z|=(m-2)|L_z|`.  Since every tail degree is at most
`m-2`, equality of the degree sums forces every tail degree to be exactly
`m-2`.  \(\square\)

### Corollary 3.2 (exact pointed-Latin form)

Under Theorem 3.1, for every `S in L_z` and every `gamma in S` there is
exactly one legal `beta` such that

\[
                         (S+\{\beta\},\gamma)\in R_z.        \tag{3.5}
\]

Conversely, (3.5) together with full-fibre closure implies the hypotheses
of Theorem 3.1.

Thus the sufficient face may be specified as a pointed Boolean Latin rule:
each pointed tail facet has one selected extension, and selecting a pointed
head selects its complete family of punctured facets.

## 4. Reset-conditioned functional attachment

### Theorem 4.1 (protected functional completion)

Fix a depth-three selected flag table, meaning exactly one flag per root
orbit, which already supplies the required rank-`(m-1)` and rank-`(m-2)`
high-target flags.  Fix one phase of an opened reset bank, contract its used
resources, and choose a bijective residual
head-to-owner attachment together with physical alignment labels.  Suppose
that:

1. the alignment flux is balanced as in (1.5);
2. every nonempty residual label block is full-fibre closed and
   pointed-simple.

Then the residual functional predecessor graph has a perfect matching.
Adding back the protected reset turns gives an owner-exact literal directed
cycle cover retaining the opened reset bank and the selected high targets.

#### Proof

Theorem 3.1 gives a perfect matching independently in each label block.
Their disjoint union uses every residual tail and head once.  The fixed
functional attachment uses every residual owner once.  Add the contracted
reset matching.  All turns are literal by (1.3), and the flag table and its
marked targets were fixed before the matching was chosen.  \(\square\)

The selected root permutation cannot contain a **literal reciprocal**
directed two-cycle.  If the physical turns `p -> q` and `q -> p` occurred
with inverse phases, their common owner would be `p union q`, contradicting
injectivity of the functional owner attachment.  Thus the closed-doubleton
obstruction is already excluded.  This does not rule out an abstract
two-node quotient cycle whose lifted turns have noninverse phases or
nontrivial voltage.

At `k=17,m=8`, the regular degree in Theorem 3.1 is six.  A prospective
certificate therefore needs six retained predecessors at every residual
head and pointed load at most six at every residual tail, in addition to
the exact high-target and alignment-flux rows.  These properties have not
been verified for an authenticated `k=17` table.  The independently chosen
reset-compatible table has residual predecessor matching only `850/1423`
and `406` dead tails, so it is far outside this sufficient face.  That is
evidence about one table, not an all-face obstruction.

## 5. The smallest literal pointed-star obstruction

Take `(k,m,d)=(7,3,3)`.  Choose pairwise distinct physical coordinates

\[
                         0,z,\gamma,\beta_1,\beta_2,\delta.  \tag{5.1}
\]

Put

\[
 \begin{aligned}
 L_z&=\{(\{\gamma\},z),(\{\delta\},z)\},\\
 R_z&=\{(\{\gamma,\beta_1\},\gamma),
         (\{\gamma,\beta_2\},\gamma)\}.
 \end{aligned}                                               \tag{5.2}
\]

Each head has `m-2=1` possible predecessor, and both have the same one:

\[
 N(R_z)=\{(\{\gamma\},z)\}.                                \tag{5.3}
\]

Thus `|R_z|=|L_z|=2`, every head retains its complete predecessor fibre,
but the matching number is one.  Pointed simplicity fails at
`(S,gamma)=({gamma},gamma)`.

This obstruction is smallest on the full-fibre face for `m>=3`.  A one-head
block has a predecessor by full-fibre closure.  At depth three, `m=3` is the first
case and every head fibre has size one, so two heads sharing that fibre are
the first possible Hall set.  The displayed roots and turns are literal
and pairwise distinct.  The block is not asserted to extend to a complete
high-target selector; it is a sharp local warning against deriving Hall
from complete individual lists or uniform fractional marginals.

## 6. Relation to Rado and the bidirectional reset

For a fixed flag table and fixed functional attachment, the protected
aligned-column theorem identifies completion with one Rado transversal.
Theorem 3.1 supplies a Boolean-specific certificate for all of those Rado
rank inequalities at once.  It is stronger than mere list nonemptiness and
does not invoke a generic three-matroid intersection theorem.

This sparse selected-table face must not be confused with the stronger
complete-host complement-list colouring.  The latter assigns **every**
pointed head option to an exterior label; its proper-colour condition forces
each colour class to be a full Steiner system and is impossible, for
example, at `m=8`.  Here, for fixed `(gamma,z)`, (3.1)--(3.2) require only a
partial Steiner packing on the heads actually selected by the high-target
table: their `(m-3)`-shadows are disjoint, but need not cover every
`(m-3)`-set.  Therefore the complete-host divisibility obstruction neither
proves nor refutes Theorem 4.1's prospective sparse face.

The bidirectional rolling reset gives two static-equivalent functional
attachments.  On the closed bank their overlay is one alternating cycle;
after opening one seam it exports one head-owner alternating path and two
predecessor parity paths.  Therefore switching reset phase does not by
itself improve Theorem 4.1.  To use the switch while preserving the
functional completion, the ambient selected blocks must supply one owner
return and two predecessor returns which are projections of one common
literal turn-triple lift.  Separate projection paths are not sufficient.
Direct seam closure merely recreates the isolated reset cycle, while
edgewise phase mixing creates an owner-repeating closed doubleton.

The strongest exact conclusion is therefore:

> High-target selection and functional attachment are jointly sufficient
> after reset contraction if their aligned pointed-shadow blocks obey
> full-fibre closure and pointed simplicity.  The remaining prospective
> construction problem is to choose the high-target table and attachment on
> this regular face, or to realize the three external returns while moving
> between its two reset phases.

This does not prove connectedness, quotient voltage, residence outside the
reset, arbitrary-width upper shadows, the terminal compiler, or any bound
on `nu(k)`.

## 7. Dependencies and scope

This note uses the exact normal form and protected contraction from:

```text
MATH_THEOREM_D3_QUOTIENT_FLAG_NORMAL_FORM_FUNCTIONAL_HALL_AND_COMPACT_CODESIGN_20260801.md
MATH_THEOREM_K17_RESET_CONDITIONED_THREE_MATROID_AND_FUNCTIONAL_FLOW_GATE_20260801.md
MATH_THEOREM_K_OVERLAP_CORE_FLOW_AND_ROOT_COLOURED_CIRCULATION_GATE_20260801.md
MATH_THEOREM_K_PROTECTED_FUNCTIONAL_RADO_FACE_AND_LITERAL_TRIANGLE_EXCHANGE_OBSTRUCTION_20260801.md
MATH_THEOREM_K_BIDIRECTIONAL_ROLLING_RESET_FUNCTIONAL_ATTACHMENT_AND_DOUBLETON_GATE_20260801.md
MATH_THEOREM_D3_COMPLEMENT_LIST_COLOURING_STEINER_NECESSITY_AND_ODD_M_NOGO_20260801.md
```

No computation is used.  The positive theorem is uniform in `m>=3` at
depth three.  The obstruction is a literal local block, not a global
`k=7` no-go.  The complete-host joint-selection projection remains
nonmatroidal already at `k=5`; consequently Theorem 4.1 is a genuine
structured sufficient face rather than a hidden proof of the unrestricted
functional-attachment theorem.
