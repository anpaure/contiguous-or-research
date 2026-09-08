# The Catalan linearization problem

This note isolates the first genuinely global obstruction in the proposed
middle-layer recursion.  Everything through Section 6 is proved.  Section 7
states the exact remaining lemma.

Fix `m>=1`, put `Omega=[2m]`, and write

\[
 \mathcal A=\binom{\Omega}{m-1},\qquad
 \mathcal B=\binom{\Omega}{m+1},\qquad
 \mathcal M=\binom{\Omega}{m}.
\]

Their sizes are

\[
 |\mathcal M|=W=\binom{2m}{m},\qquad
 |\mathcal A|=|\mathcal B|=N=\binom{2m}{m+1}=W-K,
 \tag{0.1}
\]

where

\[
 K=\operatorname{Cat}_m=\frac{W}{m+1},\qquad N=mK.          \tag{0.2}
\]

Let `H_m` be the bipartite inclusion graph between `mathcal A` and
`mathcal B`.  Every edge `(S,U)` of `H_m` has `|U minus S|=2` and determines
one edge of the Johnson graph `J(2m,m)`: its endpoints are the two middle
sets strictly between `S` and `U`.

A perfect matching of `H_m` therefore produces `N` Johnson edges on the `W`
middle vertices.  Every rank-`m-1` intersection colour and every
rank-`m+1` union colour occurs exactly once.  The question is whether the
matching can be chosen so that these Johnson edges form a linear forest.

## 1. Kneser-permutation normal form

Complementation identifies the upper colour layer with another copy of the
lower colour layer.

### Proposition 1 (disjointness-permutation equivalence)

Perfect matchings of `H_m` are in bijection with permutations

\[
 g:\mathcal A\longrightarrow\mathcal A                 \tag{1.1}
\]

satisfying

\[
 S\cap g(S)=\varnothing\qquad(S\in\mathcal A).          \tag{1.2}
\]

For a middle set `P`, the degree of `P` in the induced Johnson graph is

\[
 d_g(P)=
 \#\{S\in\binom{P}{m-1}:g(S)\subseteq P^c\}.            \tag{1.3}
\]

Equivalently,

\[
 d_g(P)=
 \#\{a\in P:g(P\setminus\{a\})\subseteq P^c\}.         \tag{1.4}
\]

#### Proof

Given a perfect matching `h:mathcal A -> mathcal B`, define

\[
 g(S)=\Omega\setminus h(S).
\]

Since complementation is a bijection from `mathcal B` to `mathcal A`, `g` is
a permutation.  The matching condition `S subset h(S)` is exactly
`S cap g(S)=emptyset`.  The construction reverses by putting
`h(S)=Omega minus g(S)`.

The matched pair belonging to `S` is incident with `P in mathcal M` exactly
when

\[
 S\subset P\subset h(S).
\]

After complementation, the second containment says `g(S) subset P^c`.
There are precisely `m` possible `(m-1)`-sets contained in `P`, namely
`P minus {a}`.  This proves (1.3)--(1.4).  QED.

Thus the maximum-degree-two part of the problem has an exact formulation:

> Find a permutation of all `(m-1)`-sets to disjoint `(m-1)`-sets such that
> no middle cut `(P,P^c)` is crossed by more than two assigned pairs.

This is stronger than finding an arbitrary perfect matching or an arbitrary
Hamilton cycle in the Kneser graph on `mathcal A`.

## 2. Two balance laws forced by every matching

The Catalan number is not only the component defect.  It is also the exact
coordinate frequency of every selected transition.

For a matched pair `(S,U)`, call the two-element set

\[
 \lambda(S,U)=U\setminus S                                  \tag{2.1}
\]

its transition label.  This is also the symmetric difference of the two
induced middle endpoints.

### Proposition 2 (uniform transition labels)

For every perfect matching of `H_m` and every coordinate `x in Omega`,

\[
 \#\{(S,U):x\in U\setminus S\}=K.                          \tag{2.2}
\]

#### Proof

Every upper set and every lower set occurs exactly once, and `S subset U`.
Consequently the number in (2.2) is

\[
 \#\{U\in\mathcal B:x\in U\}
 -\#\{S\in\mathcal A:x\in S\}
 =\binom{2m-1}{m}-\binom{2m-1}{m-2}.
\]

Using

\[
 \binom{2m-1}{m}=\frac W2,\qquad
 \binom{2m-1}{m-2}=\frac W2\frac{m-1}{m+1},
\]

the difference is `W/(m+1)=K`.  QED.

In particular, all `2m` coordinates occur equally often among the `2N`
coordinate appearances in the transition labels.  This balance is automatic;
it does not distinguish a good matching from a bad one.

### Proposition 3 (balanced endpoint-defect identity)

For every perfect matching, define the formal defect

\[
 \delta(P)=2-d(P)\qquad(P\in\mathcal M).                  \tag{2.3}
\]

Then

\[
 \sum_{P\in\mathcal M}\delta(P)=2K,                       \tag{2.4}
\]

and, for every coordinate `x`,

\[
 \sum_{P\ni x}\delta(P)=K.                                \tag{2.5}
\]

#### Proof

The induced graph has `N` edges, so its degree sum is `2N`.  Equation (2.4)
is therefore `2W-2N=2K`.

For (2.5), consider the contribution of one matched interval `[S,U]` to the
degrees of middle sets containing `x`.  If `x in S`, both middle endpoints
contain `x`; if `x in U minus S`, exactly one does; otherwise neither does.
Hence

\[
 \sum_{P\ni x}d(P)
 =2\binom{2m-1}{m-2}+K.                                    \tag{2.6}
\]

There are `binom(2m-1,m-1)=W/2` middle sets containing `x`.  Subtracting
(2.6) from twice this number and using the identities in Proposition 2 gives
(2.5).  QED.

If `d(P)<=2` everywhere, the defects are nonnegative.  A degree-one path
endpoint contributes one token and an isolated vertex contributes two.  Thus
(2.4)--(2.5) say:

> The `2K` endpoint tokens of any maximum-degree-two matching are perfectly
> balanced: every coordinate belongs to exactly `K` endpoint tokens.

This is a necessary global boundary condition for any recursive splice.

## 3. Exact geometry of alternating 2-switches

Let `(S_1,U_1)` and `(S_2,U_2)` be two edges of a perfect matching.  They
admit an alternating 2-switch when

\[
 S_1\subset U_2,qquad S_2\subset U_1,                     \tag{3.1}
\]

in which case they may be replaced by `(S_1,U_2)` and `(S_2,U_1)`.

### Theorem 4 (every 2-switch is a pivot switch)

Two matched pairs admit a 2-switch if and only if their induced Johnson edges
share a middle endpoint `P`.

More explicitly, every switch has a unique representation

\[
 S_i=P\setminus\{a_i\},\qquad U_i=P\cup\{b_i\}\quad(i=1,2), \tag{3.2}
\]

where

\[
 a_1\ne a_2\in P,qquad b_1\ne b_2\notin P.                \tag{3.3}
\]

Writing

\[
 Q_{ij}=P\setminus\{a_i\}\cup\{b_j\},                    \tag{3.4}
\]

the switch replaces the Johnson edges

\[
 PQ_{11},\ PQ_{22}\quad\hbox{by}\quad PQ_{12},\ PQ_{21}. \tag{3.5}
\]

#### Proof

Assume (3.1).  Both `S_1,S_2` lie in both `U_1,U_2`, so

\[
 S_1\cup S_2\subseteq U_1\cap U_2.                         \tag{3.6}
\]

The lower sets are distinct, hence their union has size at least `m`.  The
upper sets are distinct, hence their intersection has size at most `m`.
Thus equality holds throughout (3.6), and

\[
 P:=S_1\cup S_2=U_1\cap U_2
\]

is a middle set.  This gives (3.2)--(3.3), and every one of the four matched
pairs in the alternating square has `P` as one intermediate middle set.

Conversely, if two induced Johnson edges share `P`, their lower colours are
subsets of `P` and their upper colours contain `P`.  The cross containments
(3.1) follow immediately.  Formula (3.5) is then the direct expansion of the
four intervals.  QED.

This theorem has two important consequences.

1. A 2-switch is exactly a transposition of two columns in a partial rook
   placement at one middle pivot: rows are removed coordinates `a`, columns
   are inserted coordinates `b`.
2. The degree of the pivot `P` is unchanged by the switch.  Therefore no
   argument that repeatedly switches *at* a high-degree vertex can lower that
   vertex's degree.

The four opposite vertices in (3.4) are distinct.  Their degree changes are

\[
 d(Q_{11}),d(Q_{22})\mapsto d(Q_{11})-1,d(Q_{22})-1,
\]

\[
 d(Q_{12}),d(Q_{21})\mapsto d(Q_{12})+1,d(Q_{21})+1.       \tag{3.7}
\]

For the convex energy

\[
 \mathcal E=\sum_{P\in\mathcal M}\binom{d(P)}2,           \tag{3.8}
\]

the exact change is

\[
 \Delta\mathcal E=
 d(Q_{12})+d(Q_{21})-d(Q_{11})-d(Q_{22})+2.                \tag{3.9}
\]

Hence an energy-minimal matching under 2-switches only satisfies the local
rectangle inequalities

\[
 d(Q_{11})+d(Q_{22})
 \le d(Q_{12})+d(Q_{21})+2.                                \tag{3.10}
\]

The inequality controls the four opposite corners, not the pivot degree.
It therefore gives no direct bound on `d(P)`.  Section 5 exhibits natural
matchings with unbounded pivot degree, but does not assert that they are
global or local minima of the energy.

## 4. Two safe conditional switches

The pivot description gives exact sufficient conditions for useful local
moves.  These are not existence theorems, but they identify what a global
absorber must supply.

### Lemma 5 (safe degree transport)

In the switch (3.5), suppose one old opposite endpoint, say `Q_11`, has degree
at least three, and

\[
 d(Q_{12})\le1,\qquad d(Q_{21})\le1.                       \tag{4.1}
\]

Then the switch lowers `d(Q_11)` by one, creates no degree greater than two at
either new opposite endpoint, and leaves the pivot degree unchanged.

This is immediate from (3.7).  Notice that the switch is performed at the
*other endpoint* `P` of the edge `P Q_11`, not at the overloaded endpoint
itself.

### Lemma 6 (safe cycle opening)

Suppose the induced graph has maximum degree two and `P` lies on a cycle,
with incident selected edges `P Q_11,P Q_22`.  If the cross vertices
`Q_12,Q_21` are degree-zero or degree-one endpoints in two distinct path
components, then the pivot switch (3.5):

* preserves maximum degree two;
* turns the old cycle minus `P` into a path; and
* joins the two indicated path components through `P` into one path.

Consequently it reduces the number of cycle components by one and preserves
the number of path components.

#### Proof

Deleting the two edges incident with `P` opens the old cycle into the path
from `Q_11` to `Q_22`.  The two inserted edges attach `P` to endpoints of two
different path components.  Those two paths and `P` therefore concatenate
to one path.  The degree assumptions and (3.7) prove the maximum-degree
claim.  One path is created from the cycle and two paths are replaced by one,
so the number of path components is unchanged.  QED.

The missing global step is precisely to guarantee low-degree cross vertices
of the required kind.  The average degree alone does not do this locally.

## 5. A symbolic obstruction to the natural cyclic matching

There is a canonical rotation-equivariant perfect matching which looks at
first like it should remove the branching of the linear Greene--Kleitman
matching.  It does not.

For a lower binary word, perform the standard circular parenthesis matching,
canceling cyclic `01` pairs.  Since the word has two more zeros than ones,
exactly two zeros remain unmatched.  Flip those two zeros to ones.  If the
unmatched zeros are used as cuts, the word has the form

\[
 0D_1\,0D_2
\]

with `D_1,D_2` Dyck words.  After the flip it is `1D_1 1D_2`; the reverse
matching leaves exactly those two ones unmatched.  Thus this operation is a
bijection between the lower and upper adjacent layers and defines a perfect
matching of `H_m`.

### Proposition 7 (an unbounded-degree star)

For every `m>=1`, the alternating middle word

\[
 P=(01)^m                                                   \tag{5.1}
\]

has degree exactly `m` in the Johnson graph induced by the cyclic-parenthesis
matching.

#### Proof

For `j=1,...,m`, change the `1` at position `2j` of `P` to zero, obtaining a
lower word `S_j`.  Every unmodified adjacent `01` pair cancels, and the two
unmatched zeros of `S_j` are exactly positions `2j-1,2j`.  Flipping them gives

\[
 U_j=P\cup\{2j-1\}.                                        \tag{5.2}
\]

The two middle sets in `[S_j,U_j]` are `P` and

\[
 Q_j=P\setminus\{2j\}\cup\{2j-1\}.                        \tag{5.3}
\]

The `Q_j` are distinct, so these are `m` distinct selected edges incident
with `P`.  Formula (1.4) also shows there can be no additional incident edge,
because `P` has only `m` lower facets.  QED.

Every 2-switch involving two of these star edges and pivoted at `P` merely
permutes their inserted coordinates, by Theorem 4.  It leaves `d(P)=m`.
Reducing this star requires switches pivoted at its neighbours after the
matching has been globally rearranged.

This gives a symbolic obstruction family, not just a small counterexample:
the most natural cyclic incidence bijection is arbitrarily far from the
desired degree bound, and direct pivot-greedy switching cannot repair its
central overload.

## 6. Exact accounting once maximum degree two is reached

Suppose a perfect matching induces a graph `F` of maximum degree at most two.
Every component is a path (isolated vertices included) or a cycle.  Let `p`
and `q` be the numbers of path and cycle components.

### Proposition 8 (the path count is automatically Catalan)

\[
 p=K.                                                        \tag{6.1}
\]

In particular, `F` is an acyclic linear forest if and only if it consists of
exactly `K` path components and no cycle components.

#### Proof

Every path component contributes one more vertex than edge, while every
cycle contributes equally many.  Hence

\[
 W-N=p.
\]

Equation (0.1) gives `W-N=K`.  QED.

Thus there are three logically separate gates:

1. **degree gate:** find a perfect matching inducing maximum degree two;
2. **cycle gate:** eliminate all cycle components while preserving the
   perfect colour matching and the degree bound;
3. **bridge gate:** orient the resulting `K` paths so their endpoints can be
   joined by exactly `K-1` Johnson edges.

The endpoint tokens at the end of gate 2 automatically satisfy the perfect
coordinate balance of Proposition 3.

## 7. Exact remaining lemma

The strongest clean statement needed for the central recursion is the
following.

### Catalan switch-linearization lemma (open)

For every `m`, the inclusion graph `H_m` has a perfect matching whose induced
Johnson graph is an endpoint-connectable linear forest.  Equivalently, it has
maximum degree at most two, has no cycle component, and its `K` path
components admit orientations and an ordering in which consecutive terminal
endpoints are Johnson-adjacent.

A stronger switch form would say that the Greene--Kleitman perfect matching
can be transformed into such a matching by alternating switches.  Theorem 4
shows that 2-switches alone are highly constrained pivot operations; longer
alternating-cycle switches may be necessary.

If the lemma holds, retaining the `N` matched edges and adding the `K-1`
bridges gives a Hamilton path through all `W` middle sets with every lower and
upper adjacent colour represented.  The edge count is exact:

\[
 N+(K-1)=W-1.                                               \tag{7.1}
\]

This would settle the purely central two-sided rainbow skeleton.  It would
still not, by itself, prove a universal contiguous-OR array: deeper
consecutive shadows, coordinate-run factorability, and pin-surviving lower
labels remain separate all-rank requirements.

No proof of the Catalan switch-linearization lemma is claimed here.  The
proved contribution is the exact Kneser normal form, the coordinate and
endpoint balance laws, the complete classification of 2-switches, safe local
switch criteria, and an unbounded symbolic obstruction to the naive cyclic
matching.
