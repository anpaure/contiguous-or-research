# Short unlocked gaps localize the maximal-antecedent compiler to mandatory-core positive hits

**Date:** 2026-08-05  
**Method:** coordinate-run erosion, exact-value interval pins, and central
binomial asymptotics; no computation or search  
**Status:** unconditional reduction on the canonical maximal-antecedent
face.  If a prescribed free bank is a union of gaps of length at most the
deadline, then retaining the mandatory erosion endpoints inside those gaps
automatically preserves the complete owner row.  The remaining ordinary
compiler test is purely local: mandatory-core containment and positive
hits for the chosen exact-value intervals.  A uniform depth-sized block
template has enough scalar interval capacity asymptotically.  This note does
not prove that the PBBS depth-`d` occurrence fibres avoid that template, nor
that the local positive-hit atlas exists.

## 1. Set-up and the mandatory core

Let

\[
                         T=(T_i)_{i\in\mathbb Z_W}
\]

be a cyclic simple rank-`r` Johnson trace.  Assume every positive
coordinate run has length at least `d+1`, and put

\[
 P_p=\bigcap_{h=0}^{d}T_{p-h}.
 \tag{1.1}
\]

Then `P` is the maximal depth-`d` antecedent and

\[
                         T_i=\bigcup_{p=i}^{i+d}P_p.
 \tag{1.2}
\]

For each source position define

\[
 F_p=(P_p\setminus P_{p-1})\cup(P_p\setminus P_{p+1}).
 \tag{1.3}
\]

The set `F_p` consists exactly of the coordinates whose eroded positive
run begins or ends at `p`.

### Lemma 1.1 (mandatory erosion endpoints)

If `A_p\subseteq P_p` and `D^d A=T`, then

\[
                         F_p\subseteq A_p
                         \qquad(p\in\mathbb Z_W).
 \tag{1.4}
\]

#### Proof

Unwrap one nonconstant positive run of a coordinate `x` in the owner word
as `[a,b]`.  Its support in `P` is exactly

\[
                         [a+d,b].
 \tag{1.5}
\]

In the source window `[a,a+d]` representing `T_a`, the only envelope
position containing `x` is `a+d`.  Hence `x\in A_{a+d}`.  Likewise the
only envelope position containing `x` in the source window `[b,b+d]`
representing `T_b` is `b`, so `x\in A_b`.  These are precisely the two
finite endpoints in (1.3).  A coordinate constant on the whole cyclic
component contributes no endpoint.  Taking all coordinate runs proves
(1.4).  \(\square\)

Thus any interval `I` assigned the exact target value `S` must obey the
necessary aperture condition

\[
                         \bigcup_{p\in I}F_p\subseteq S.
 \tag{1.6}
\]

This is stronger than the envelope condition
\(S\subseteq\bigcup_{p\in I}P_p\) and is the first literal constraint that
an owner-intersection witness does not see.

## 2. Short-gap localization

Let `R\subseteq\mathbb Z_W` be a union of disjoint maximal cyclic intervals

\[
                         G_1,\ldots,G_c,
 \qquad                  |G_a|\le d.
 \tag{2.1}
\]

Think of `R` as the free bank.  Every position outside `R` will retain its
maximal letter.

### Theorem 2.1 (mandatory cores make every short gap owner-safe)

Suppose

\[
 A_p=P_p\quad(p\notin R),
 \qquad
 F_p\subseteq A_p\subseteq P_p\quad(p\in R).
 \tag{2.2}
\]

Then

\[
                         D^dA=T.
 \tag{2.3}
\]

#### Proof

Fix a coordinate `x`.  First unwrap a nonconstant component `E=[u,v]` of
its support in `P`.  By Lemma 1.1, both endpoints `u,v` are retained in
`A`.  Every omitted position of `E` lies in `R`.  Inside one free gap, a
consecutive omitted block has length at most `d`; two different free gaps
are separated either by a retained occurrence of `x` or by a point outside
`E`.  Consequently the first and last points of `E` are retained and every
gap between successive retained points of `E` has at most `d` omitted
positions.

If instead `x` is constant on the whole cyclic component, its `P`-support
is the whole cycle.  Since every free gap is proper and has length at most
`d`, the retained complement of `R` again breaks every omitted block at
length at most `d`; the same window argument below applies without
endpoints.

The source window `[i,i+d]` for an owner occurrence `x\in T_i` meets
`E`.  At either clipped end it contains the retained endpoint of `E`; in
the interior, a window of `d+1` consecutive positions cannot lie inside an
omitted block of length at most `d`.  Hence it contains some `p` with
`x\in A_p`.  This proves
\(T_i\subseteq\bigcup_{p=i}^{i+d}A_p\).  The reverse inclusion follows
from `A_p\subseteq P_p` and (1.2).  Apply this to every coordinate and
owner.  \(\square\)

The theorem is deliberately stronger than a one-target statement.  Inside
one short gap, arbitrarily many overlapping negative pins may be imposed;
as long as their joint deletion leaves every mandatory core, no owner cut
can fail.

## 3. Exact local atlas criterion

For every target `S` of rank below `r-d`, choose a nonempty interval

\[
                         I_S\subseteq G_a
 \tag{3.1}
\]

inside one free gap.  Different target intervals may overlap.  Define the
maximal letter compatible with all selected negative equalities by

\[
 A_p^*=P_p\cap
       \bigcap_{S:\,p\in I_S}S
       \quad(p\in R),
 \qquad
 A_p^*=P_p\quad(p\notin R),
 \tag{3.2}
\]

where an empty intersection of target labels is the whole ground set.

### Theorem 3.1 (short-gap exact-value atlas)

There is a nonzero antecedent which retains `P` outside `R`, realizes every
selected equality

\[
                         \bigcup_{p\in I_S}A_p=S,
 \tag{3.3}
\]

and has derivative `T` if and only if

\[
                         F_p\subseteq A_p^*\ne\varnothing
                         \quad(p\in R),
 \tag{3.4}
\]

and

\[
 \forall S\ \forall x\in S\quad
 \exists p\in I_S\quad x\in A_p^*.
 \tag{3.5}
\]

When these conditions hold, the word `A^*` itself is a solution.

#### Proof

For necessity, every equality (3.3) forbids `x` at every position of
`I_S` when `x\notin S`.  Hence any realizing word is contained in
`A^*`.  Lemma 1.1 gives the first containment in (3.4), nonzero letters
give the second, and the positive side of (3.3) gives (3.5).

Conversely, (3.2) gives `A_p^*\subseteq S` throughout `I_S`; therefore
its union there is contained in `S`.  Condition (3.5) supplies every
member of `S`, proving equality.  Condition (3.4) and Theorem 2.1 give
`D^dA^*=T`, and (3.4) also gives nonzero letters.  \(\square\)

Thus, on a depth-sized block face, all central-window cuts and all
nonzero-letter cuts disappear.  The complete ordinary compiler obstruction
is the explicitly local family (3.4)--(3.5).  A typed external cap, if
required, remains separate.

## 4. Adding the canonical depth-`d` locks

Put `t=r-d`.  For each rank-`t` target let

\[
                         O_S=\{p:P_p=S\}.
 \tag{4.1}
\]

Assume

\[
                         O_S\not\subseteq R
                         \qquad(|S|=t).
 \tag{4.2}
\]

Choose one `p(S)\in O_S\setminus R`.  The fibres are disjoint, so these
positions are automatically distinct.  Since `A^*=P` outside `R`,

\[
                         A^*_{p(S)}=P_{p(S)}=S.
 \tag{4.3}
\]

### Corollary 4.1 (exact block-lock reduction)

Under (2.1), (3.4)--(3.5), and (4.2), one word simultaneously realizes

1. every rank-`r` owner;
2. one canonical singleton occurrence of every rank-`r-d` target; and
3. every selected deeper target interval.

There is no matching left after `R` and the intervals have been selected.
The two genuine choices are exactly:

* find a short-block bank `R` satisfying the fibre-transversal condition
  (4.2); and
* choose a complete interval atlas in `R` satisfying the local coordinate
  conditions (3.4)--(3.5).

## 5. A depth-sized block template has enough scalar capacity

Specialize to the odd PBBS parameters

\[
 n=2m+1,
 \qquad r=m,
 \qquad W={n\choose m},
 \qquad t=m-d.
 \tag{5.1}
\]

Put

\[
 M={n\choose t},
 \qquad U=W-M,
 \qquad L_< =\sum_{s=1}^{t-1}{n\choose s},
 \qquad q=\left\lfloor{U\over d+1}\right\rfloor.
 \tag{5.2}
\]

Consider any cyclic template consisting of `q` free blocks of length `d`,
each separated from the next by at least one nonfree position.  The unused
nonfree reservoir has exact size

\[
 W-qd
 =M+q+\bigl(U-q(d+1)\bigr)
 \ge M+q.
 \tag{5.3}
\]

Thus it has room for all `M` canonical locks and for one separator per free
block.  Its number of short physical intervals is

\[
                         q{d(d+1)\over2}.
 \tag{5.4}
\]

### Theorem 5.1 (strict asymptotic scalar surplus)

For the optimal deadline, for all sufficiently large `m`,

\[
                         q{d(d+1)\over2}>L_<.
 \tag{5.5}
\]

#### Proof

The central local limit and binomial-tail estimates give

\[
 {M\over W}\longrightarrow e^{-\pi/4},
 \qquad
 {L_<\over dW}\longrightarrow
 2\Phi\!\left(-\sqrt{\pi/2}\right).
 \tag{5.6}
\]

Since `d` tends to infinity,

\[
 {q d(d+1)/2\over dW}
 \longrightarrow {1-e^{-\pi/4}\over2}.
 \tag{5.7}
\]

The limiting constants satisfy the strict inequality

\[
 2\Phi\!\left(-\sqrt{\pi/2}\right)
 <{1-e^{-\pi/4}\over2};
 \tag{5.8}
\]

the two sides are approximately `0.210` and `0.272`.  One proof without
decimal evaluation uses the standard two-step Mills bound

\[
 \Phi(-x)<{4\phi(x)\over3x+\sqrt{x^2+8}}
 \qquad(x>0).
 \tag{5.9}
\]

At `x=sqrt(pi/2)`, one has
`phi(x)=e^(-pi/4)/(2x)`; substitution in (5.9) gives (5.8) by direct
algebra (already the elementary bounds `3<pi<22/7` leave strict slack).
The positive limiting gap proves (5.5).
\(\square\)

Therefore the canonical-lock obstruction is not scalar.  A bank made of
deadline-sized blocks can reserve one separator per block, discard
`O(W/d)` additional positions beyond the canonical lock count, and still
have a positive `Theta(dW)` interval surplus.

## 6. Why multiplicity totals cannot produce the blocks

The fibre condition needs genuine PBBS positional information.  Aggregate
support and the identity

\[
                         \sum_S|O_S|=W
 \tag{6.1}
\]

do not suffice.

### Proposition 6.1 (abstract evenly forced counterexample)

Let `M=Theta(W)`.  There is a partition of a cyclic `W`-set into `M`
nonempty fibres such that every transversal has maximum complementary gap
`O(W/M)=O(1)`.

#### Proof

Take `M-1` singleton fibres and place their points as evenly as possible
around the cycle.  Put all remaining positions in the last fibre.  Every
transversal must contain every singleton point.  Consecutive forced points
are at cyclic distance at most `ceil(W/(M-1))`, so every complementary gap
has the asserted bounded length.  \(\square\)

When `d` tends to infinity, such a layout has only `O(W)` short-interval
capacity, not the required `Theta(dW)`.  Hence neither average multiplicity,
complete support, nor zero floor-correct repeat excess can prove (4.2) for
the block template.  The missing positive theorem must use PBBS component
ordering or another literal occurrence geometry.

## 7. Forced-transition interpretation and the singleton aperture

Assume now that the maximal antecedent itself is a simple Johnson trace,
and write

\[
 P_{p+1}=P_p-\{\delta_p\}+\{\iota_{p+1}\}.
 \tag{7.1}
\]

For a biresident owner trace this follows directly from erosion: `delta_p`
is the coordinate deleted at the owner transition `T_p -> T_(p+1)`, while
`iota_p` is the coordinate whose owner run begins at `T_(p-d)`.  Equation
(1.3) becomes

\[
                         F_p=\{\iota_p,\delta_p\}.
 \tag{7.2}
\]

The two labels may coincide; this happens exactly when their coordinate has
an owner run of the minimum allowed length `d+1`.

### Proposition 7.1 (an exact target interval is transition-confined)

If an interval `I=[a,b]` has exact value `S` in any antecedent of `T`, then

\[
 \{\iota_a,\delta_a,\iota_{a+1},\delta_{a+1},
       \ldots,\iota_b,\delta_b\}\subseteq S.
 \tag{7.3}
\]

Consequently every internal transition

\[
                         P_p\longrightarrow P_{p+1}
                         \qquad(a\le p<b)
 \tag{7.4}
\]

exchanges two labels belonging to `S`.  Equivalently, the projection
`P_p setminus S` is constant for `a<=p<=b`.  The entrance transition may
delete a label outside `S`, and the exit transition may insert one; their
labels not belonging to the interval letters are not constrained.

#### Proof

Equation (7.3) is (1.6) together with (7.2).  For an internal transition,
its deleted label is `delta_p in F_p` and its inserted label is
`iota_(p+1) in F_(p+1)`, so both lie in `S`.  Removing and inserting only
members of `S` leaves the projection outside `S` unchanged.  `square`

### Proposition 7.2 (biresidence gives the rank-width aperture)

Assume every zero gap of the owner trace also has length at least `d+1`.
If a target `S` is realized on an interval `I` of width at most `d`, then

\[
                         |I|\le |S|.
 \tag{7.5}
\]

#### Proof

If a coordinate has an owner zero gap of length `G`, its zero gap in the
eroded word `P` has length `G+d`.  Hence the same coordinate cannot be
inserted into `P` twice within `d` consecutive source positions.  For
`I=[a,b]`, the labels

\[
                         \iota_a,\iota_{a+1},\ldots,\iota_b
 \tag{7.6}
\]

are therefore `|I|` distinct coordinates.  Proposition 7.1 puts all of
them in `S`, proving (7.5).  `square`

### Corollary 7.3 (singleton targets force minimum owner runs)

If the singleton target `{x}` occurs in a depth-`d` antecedent, then its
only possible interval is a singleton position `p`, and

\[
                         F_p=\{x\}.
 \tag{7.7}
\]

Equivalently, `x` has a positive owner run of length exactly `d+1` whose
eroded support is the one point `p`.  Hence a complete strict-lower compiler
requires at least one minimum-length positive run for every ground
coordinate.

#### Proof

Every nonempty letter in an interval with union `{x}` equals `{x}`.  Thus
`F_p subseteq {x}` at every position of the interval.  If two consecutive
positions occurred, Proposition 7.1 would force the Johnson transition
between them to delete and insert the same label `x`, contradicting
simplicity.  The interval therefore has one position and its nonempty
mandatory core is `{x}`.

The support of `x` in `P` is the erosion of its owner run.  It is a singleton
exactly when the owner run has length `d+1`.  `square`

This exposes a concrete low-rank requirement hidden by all scalar interval
counts.  In particular, a terminal component whose owner runs are all
strictly longer than `d+1` contributes no singleton compiler cell on its
maximal antecedent, however many unused physical intervals it contains.
For the rigid braid this follows from its exact run lengths `m-1,m+1` once
`d<=m-3`; for a residual rigid component it follows from the run floor
`m-2` whenever `d<=m-4`.  Singleton tickets must then come from other
components or from a nonmaximal/component-joining construction.

### Corollary 7.4 (all rank-threshold width counts pass in the block template)

Let `R` be the `q` depth-sized blocks of Section 5.  For `1<=s<t`, the
number of its intervals whose width is at most `min(s,d)` is

\[
 C_s=q\sum_{\ell=1}^{\min(s,d)}(d-\ell+1).
 \tag{7.8}
\]

For all sufficiently large `m`, simultaneously for every `1<=s<t`,

\[
                         \sum_{j=1}^{s}{n\choose j}<C_s.
 \tag{7.9}
\]

#### Proof

If `s>=d`, equation (7.8) is the complete capacity (5.4), and (7.9)
follows from Theorem 5.1.  If `s<d`, then `C_s>=qd=Theta(W)`.  Uniformly
for `s<=d=Theta(sqrt(m))`,

\[
 \sum_{j=1}^{s}{n\choose j}
 \le (s+1)n^s
 =\exp(O(\sqrt m\log m))
 =o(W).
 \tag{7.10}
\]

This proves every remaining threshold at once.  `square`

Thus even the stronger biresident width aperture has ample scalar room.
What it does not count is the literal inclusion `F(I) subseteq S`; at rank
one that inclusion is exactly the minimum-run condition of Corollary 7.3.

## 8. Explicit core-plus-marker triangular charts

The mandatory cores also give a positive literal chart whenever a free
block avoids short runs of the eroded word.

Let `G=[a,b]` have length `g<=d`.  Assume no coordinate is inserted into
`P` twice across `G`, and no positive `P`-run has both endpoints in `G`.
Equivalently, in the notation (7.1), the labels

\[
                         U_G=\{\iota_p:p\in G\}
 \tag{8.1}
\]

are distinct and

\[
                         F_p\cap U_G=\{\iota_p\}
                         \qquad(p\in G).
 \tag{8.2}
\]

Both conditions follow, for example, if every positive and zero run of `P`
meeting the block has length greater than `g`.

Put

\[
 C_G=\left(\bigcap_{p\in G}P_p\right)
       \setminus\bigcup_{p\in G}F_p.
 \tag{8.3}
\]

Choose any `K subseteq C_G`, and define

\[
 A_p=K\cup F_p\quad(p\in G),
 \qquad
 A_p=P_p\quad(p\notin G).
 \tag{8.4}
\]

### Theorem 8.1 (literal triangular chart)

The word (8.4) has derivative `T`.  Its intervals inside `G` have the exact
values

\[
                         V(I)=K\cup\bigcup_{p\in I}F_p.
 \tag{8.5}

All `g(g+1)/2` values (8.5) are distinct.  More precisely,

\[
                         V(I)\cap U_G
                         =\{\iota_p:p\in I\}.
 \tag{8.6}

If `P` is rank `t` and its transitions across `G` have distinct deletion
labels, then

\[
                         |C_G|\ge t-g-1.
 \tag{8.7}

Consequently, whenever `t>=2g+1`, choosing

\[
                         |K|\le t-2g-1
 \tag{8.8}

makes every value in the chart have rank below `t`.

#### Proof

The inclusions `K subseteq P_p` and `F_p subseteq P_p` make (8.4) a valid
subword of the maximal envelope.  Theorem 2.1 gives `D^dA=T`.  Equation
(8.5) is immediate from taking the union of its letters.

By (8.2), the only member of the private marker bank `U_G` in `F_p` is
`iota_p`; by (8.3), `K` is disjoint from that bank.  This proves (8.6).
Two cyclic intervals of length at most `g<W` have different sets of
positions and hence different private-marker subsets, proving injectivity.

The intersection of `g` consecutive rank-`t` Johnson states loses at most
`g-1` coordinates.  Among the mandatory labels, only the entering label at
the left boundary and the departing label at the right boundary can remain
in every state of the block.  Deleting those two possible labels gives
(8.7).  Finally

\[
 |V(I)|\le |K|+\sum_{p\in I}|F_p|
          \le |K|+2g\le t-1,
 \tag{8.9}
\]

which proves the last assertion.  `square`

Thus a good free block is not merely a reservoir of formal addresses.  It
carries a literal owner-compatible triangular chart with a private address
signature.  The remaining global value problem is to choose the blocks and
their cores so that the union of these explicit chart families contains
every target below rank `t`; internal occurrence collisions within one
chart are already impossible.

For the rigid braid and residual components, the proved owner run/gap
lengths imply the local hypothesis of Theorem 8.1 for `g=d` once
`m` is sufficiently large compared with `d`.  Those altered components
have only polynomially many positions, so this observation is a local
chart supply theorem, not the required exponentially large global atlas.

## 9. Exact remaining theorem

On the canonical maximal-antecedent route, the next proof can now be stated
without hidden Hall language.

> **PBBS block-atlas theorem.**  Choose a union `R` of deadline-sized
> cyclic blocks with the scalar size in Section 5 such that no depth-`d`
> fibre `O_S` is contained in `R`; then assign every lower target of rank
> below `r-d` to an interval in `R` so that (3.4)--(3.5) hold.

The first clause is a positional fibre-hitting statement.  The second is a
coordinate-value interval-chart statement.  Once they hold, Corollary 4.1
constructs the ordinary word automatically.  A typed common-cap router and
component opening, if demanded by the surrounding architecture, remain
additional gates.

## 10. Dependencies and scope

The maximal row identity and the top-row singleton cells are in

`MATH_THEOREM_PBBS_MAXIMAL_ANTECEDENT_INTERSECTION_SOURCE_ROW_IDENTITY_20260805.md`.

The fibre-transversal criterion and deep scalar gap count are in

`MATH_THEOREM_PBBS_CANONICAL_DEPTH_D_LOCK_AND_DEEP_GAP_CAPACITY_20260805.md`.

The unrestricted fixed-atlas coordinate cuts are in

`MATH_THEOREM_PBBS_RIGID_ROTATION_FIXED_ANTECEDENT_COMPILER_AND_EXACT_CAP_CUT_20260805.md`.

This note proves no PBBS block placement, no complete local interval chart,
no typed suffix routing, and no `B(k)+O(1)` upper bound.
