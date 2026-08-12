# Audit of the GJM middle-four-level lexical factor

> **Sharpening notice (2026-07-26).**  The Catalan lower bound in
> Theorem 3 is valid but very far from sharp.  The first-global-minimum
> construction in
> `MATH_OBSTRUCTION_THREE_LEVEL_OPPOSITE_COLOR_AND_GJM_LINEAR_COLLISIONS_20260726.md`
> gives pairwise disjoint lexical collision pairs indexed by every word of
> length (2r-1) and weight (r-2), and therefore
> \[
> \delta_r\ge\binom{2r-1}{r-2}
>   =\left(\frac14-o(1)\right)\binom{2r+1}{r}.
> \]
> Consequently the later Catalan-scale rainbow-pruning target for the
> unflagged lower contraction is impossible: retaining that contraction
> requires a linear-size pruning.  The exact forest construction and the
> structural non-identification of the two central layers proved below are
> unaffected.

This note checks whether the cycle factor from Gregor--Jäger--Mütze--Sawada--
Wille, *Gray codes and symmetric chains* (JCTB 2022;
[arXiv:1802.06021](https://arxiv.org/abs/1802.06021)), supplies the missing
two-sided central-diamond factor for the contiguous-OR problem.

The answer is precise:

* contracting its **lower** outer vertices gives a spanning Johnson linear
  forest with every lower colour exactly once and only `O(Cat_m)` components;
* this contraction has too few edges to cover the upper layer;
* the upper and lower contractions live on different central layers, and the
  paper's central edge set is not a matching that identifies those layers;
* with the paper's distinguished last coordinate used as the new coordinate
  `z`, the factor contains **no** six-cycle of the required `z`-lifted
  central-diamond form.

Thus the paper supplies a strong one-sided atom, but not the simultaneous
two-sided factor.

## 1. The desired six-cycle lift

Let the old ground set be `Omega=[2m]`, and let `z` be a new coordinate.  A
matched Boolean interval

\[
 S\subset U,\qquad |S|=m-1,\quad |U|=m+1,
\]

has `U minus S={a,b}`.  Orient the induced middle Johnson edge from

\[
 X=S\cup\{a\}
 \quad\hbox{to}\quad
 Y=S\cup\{b\}.                                           \tag{1.1}
\]

The associated lifted six-cycle in the middle four levels of `Q_(2m+1)` is

\[
 S, X, U, U\cup\{z\}, Y\cup\{z\}, S\cup\{z\}, S.
\tag{1.2}
\]

It uses every one of the following two edges that flips `z`:

\[
                         U--(U\cup\{z\}),
 \qquad                   S--(S\cup\{z\}).              \tag{1.3}
\]

### Lemma 1 (exact packing criterion)

Let `h` be a perfect matching between the rank-`m-1` and rank-`m+1` layers
of `B_(2m)`, with `S subset h(S)`.  Let `H_h` be the graph on the middle
`m`-sets whose edge for `S` is the two-element interval between `S` and
`h(S)`.

The six-cycles (1.2) can be oriented so that they are pairwise vertex-
disjoint if and only if `H_h` has an orientation with indegree and outdegree
at most one.  Equivalently,

\[
                          \Delta(H_h)\le2.               \tag{1.4}
\]

#### Proof

All outer vertices `S` and `h(S) union {z}` are already distinct because
`h` is a perfect matching.  The other automatically distinct central
vertices are `S union {z}` and `h(S)`.  The only possible collisions are:

* two cycles using the same unmarked tail `X`; or
* two cycles using the same marked head `Y union {z}`.

These are exactly outdegree and indegree collisions in the oriented graph
`H_h`.  A graph admits an orientation with both degrees at most one exactly
when every component is a path or a cycle, i.e. when its maximum degree is at
most two.  QED.

If `H_h` is a linear forest, it has

\[
 \binom{2m}{m}-\binom{2m}{m-1}=\operatorname {Cat}_m   \tag{1.5}
\]

components, including isolated vertices.  This is precisely the Catalan
linearization problem in `CATALAN_LINEARIZATION.md`.

## 2. What the GJM lexical factor actually uses

To avoid a collision of notation, write the paper's dimension as `2r+1`.
Its four central levels are

\[
                         r-1,r,r+1,r+2.                  \tag{2.1}
\]

The explicit cycle factor is

\[
 \mathcal C_{2r+1}=
 (M_{2r+1,r-1}^{r}\cup M_{2r+1,r-1}^{r+1})
 \cup
 (M_{2r+1,r+1}^{r}\cup M_{2r+1,r+1}^{r+1})
 \cup E,                                                  \tag{2.2}
\]

where `E` consists of selected `r`, `r-1`, and `r-2` lexical edges between
the two inner levels.  This is equations (17) and (20) in the paper's
middle-four-level construction.

The union of the two lexical matchings between either pair of outer levels
contains paths but no cycles.  This is an explicit theorem used in the paper
to analyze its factor.

## 3. The lower contraction is a colour-perfect linear forest

Suppress every rank-`r-1` vertex in the lower part of (2.2).  Such a vertex
has exactly two neighbors in rank `r`, one in each lexical matching.  The
suppression produces one Johnson edge on rank-`r` sets whose intersection is
the suppressed vertex.

### Theorem 2 (one-sided lexical forest)

The lower contraction is a spanning linear forest `F_-` on

\[
 W'=\binom{2r+1}{r}                                      \tag{3.1}
\]

rank-`r` vertices.  It has

\[
 N'=\binom{2r+1}{r-1}                                   \tag{3.2}
\]

edges, and every rank-`r-1` intersection colour occurs exactly once.
Including isolated rank-`r` vertices, its number of components is

\[
 \begin{aligned}
 D_r&=W'-N'\\
    &=\frac{2}{r+2}\binom{2r+1}{r}\\
    &=\frac{2(2r+1)}{r+2}\operatorname {Cat}_r
      =O(\operatorname {Cat}_r).                         \tag{3.3}
 \end{aligned}
\]

#### Proof

There is one suppressed edge for every rank-`r-1` set, giving (3.2) and the
rainbow intersection statement.  Suppressing one bipartition class in a
collection of paths again gives a collection of paths; adding the unused
rank-`r` vertices as isolated vertices makes it spanning.  A spanning forest
has `vertices minus edges` components, giving (3.3).  QED.

This is a useful exact global atom.  It is not, however, two-sided.  There
are `W'` possible rank-`r+1` union colours but only `N'<W'` edges in `F_-`.
Consequently

\[
 \boxed{F_-\text{ cannot cover all upper colours, by cardinality alone}.}
\tag{3.4}
\]

At least `D_r` further Johnson edges are necessary.  If they could join the
`D_r` components while supplying exactly the missing union colours, this
would indeed give the desired kind of two-sided factor.  The published
four-level factor does not provide that identification automatically.

There is a stronger obstruction: the `N'` union colours already present in
`F_-` are not distinct.

### Theorem 3 (symbolic lexical-colour collisions)

For every `r>=2`, the lower lexical forest `F_-` contains at least

\[
                         \operatorname {Cat}_{r-1}       \tag{3.5}
\]

pairwise edge-disjoint pairs of edges having the same upper union colour.
The common colours of these pairs are themselves distinct.

Consequently, if `delta_r` denotes the duplicate excess

\[
 \delta_r=|E(F_-)|-
   |\{X\cup Y:XY\in E(F_-)\}|,                           \tag{3.6}
\]

then

\[
 \delta_r\ge \operatorname {Cat}_{r-1},                 \tag{3.7}
\]

and the number of missing upper colours is

\[
                         D_r+\delta_r.                   \tag{3.8}
\]

#### Proof

Use the paper's convention in which the lower forest is formed from the
`r`- and `(r+1)`-lexical matchings.  A lower vertex is a bitstring with
`r-1` up-steps and `r+2` down-steps.  The two incident matching edges flip
the down-steps with scan indices `r` and `r+1`, where down-steps are scanned
row by row from top to bottom and from right to left within a row.  The union
colour of the contracted edge is obtained by flipping **both** of these
positions to up-steps.

Let `w` and `v` be Dyck words whose semilengths add to `r-2`, and consider
the two lower words

\[
                         x=w\,00010\,v,
 \qquad                  x'=w\,00001\,v.                \tag{3.9}
\]

The first Dyck word stays weakly above height zero.  After either five-step
gadget the path is at height `-3`, and the final Dyck word stays weakly above
that height.  In `00010`, the two lexically last down-steps are gadget
positions

\[
                         5,3,                            \tag{3.10}
\]

whereas in `00001` they are gadget positions

\[
                         3,4.                            \tag{3.11}
\]

All other down-steps start above height `-2`.  Down-steps of `v` starting at
height `-2` lie to the right and are scanned earlier.  In the first gadget,
positions `5,3` are therefore last on the bottom row.  In the second,
position `4` is the unique down-step starting at height `-3`, and position
`3` is last on the row above it.  Since there are `r+2` down-steps in total,
these are exactly global scan indices `r,r+1`.

The pre-existing gadget up-step is respectively at position `4` and position
`5`.  In both cases the resulting union colour has up-step set

\[
 \{\hbox{up-steps of }w\}\cup
 \{\hbox{the three final gadget positions}\}\cup
 \{\hbox{up-steps of }v\}.                               \tag{3.12}
\]

Thus `x` and `x'` give distinct forest edges with the same union colour.  The
decomposition is unique: `w` is the maximal initial Dyck prefix before the
first step below height zero, the next five positions form the gadget, and
the remainder is `v`.  Hence distinct pairs `(w,v)` give distinct collision
pairs and distinct common colours.  Their number is the Catalan convolution

\[
 \sum_{a+b=r-2}\operatorname {Cat}_a\operatorname {Cat}_b
 =\operatorname {Cat}_{r-1}.                            \tag{3.13}
\]

This proves (3.5)--(3.7).
Equation (3.8) is the identity

\[
 W'-\#\{\hbox{present upper colours}\}
 =(W'-N')+(N'-\#\{\hbox{present upper colours}\}).
\]

QED.

The lower bound has a clean scale.  Exactly,

\[
 \frac{\operatorname {Cat}_{r-1}}{\operatorname {Cat}_r}
 =\frac{r+1}{2(2r-1)}
 =\frac14+O(r^{-1}),                                     \tag{3.14}
\]

and, using (3.3),

\[
 \frac{\operatorname {Cat}_{r-1}}{D_r}
 =\frac{(r+1)(r+2)}{4(2r-1)(2r+1)}
 =\frac1{16}+O(r^{-1}).                                  \tag{3.15}
\]

Relative to the full middle width,

\[
 \frac{\operatorname {Cat}_{r-1}}{W'}
 =\frac{r+1}{2(2r-1)(2r+1)}
 =\frac1{8r}+O(r^{-2}).                                  \tag{3.16}
\]

So the proved defect is a positive constant fraction of the Catalan repair
scale, but only an `O(1/r)` fraction of the middle layer.  It is compatible
with a width-plus-`O(Cat_r)` theorem, while ruling out a zero-repair theorem.

### Corollary 4 (endpoint completion cannot retain the forest)

No Hamilton cycle obtained only by adding `D_r` edges between the components
of `F_-` can cover every upper colour.

More generally, before a completion can be upper-rainbow, at least
`delta_r>=Cat_(r-1)` forest edges must be deleted.  After deleting the minimum
possible number of edges, the number of path components rises from `D_r` to
at least

\[
                         D_r+\operatorname {Cat}_{r-1}.  \tag{3.17}
\]

#### Proof

Joining `D_r` path components cyclically adds exactly `D_r` edges, but by
(3.8) there are `D_r+delta_r` absent upper colours.  More generally, suppose
`q` forest edges are deleted.  The retained forest has `D_r+q` components,
so a cyclic completion has exactly `D_r+q` connector slots.  If the retained
forest still has duplicate union colours, the number of absent upper colours
is strictly larger than `D_r+q`; completion is impossible.  Hence the
retained union colours must be distinct, requiring deletion of at least one
edge for every unit of duplicate excess.  Apply (3.7).  QED.

This is still Catalan-scale, so it does not kill the route asymptotically.
It does show that the GJM forest needs a genuine `Omega(Cat_r)` rainbow
repair; merely connecting its existing endpoints cannot work.

### The exact rainbow-pruning and endpoint target

For any choice of one retained edge from every upper colour already present
in `F_-`, delete all other occurrences of those colours.  The number deleted
is exactly `delta_r`; this is the minimum possible rainbow pruning.  The
resulting spanning linear forest `F_0` has

\[
                         c=D_r+\delta_r                  \tag{3.18}
\]

components and pairwise distinct upper colours.  It is missing exactly `c`
upper colours and exactly `delta_r` lower colours (the intersection colours
of the deleted edges).

Give every nontrivial path component its two endpoint ports; an isolated
vertex has two formal ports at the same vertex.  Form the endpoint multigraph
whose candidate edge between two ports `x,y` is the Johnson edge `xy`, with
the ordered colour pair

\[
                       (x\cap y,\ x\cup y).              \tag{3.19}
\]

Then the pruned forest extends to a two-sided-colour-complete Hamilton cycle
if and only if one can choose `c` candidate edges such that:

1. every endpoint port is used exactly once;
2. after contracting every component of `F_0`, the chosen edges form one
   connected `2`-regular multigraph;
3. their upper colours are exactly the `c` missing upper colours; and
4. their lower colours contain all `delta_r` deleted lower colours.

Necessity follows by deleting the forest edges from a completion.  For
sufficiency, orient every path component consistently and splice it with the
chosen endpoint edges.  Conditions 1--2 give one Hamilton cycle, while 3--4
restore both colour layers.

This is the clean repaired global target:

\[
 \boxed{
 \begin{array}{c}
 \delta_r=O(\operatorname {Cat}_r),\\[2mm]
 \text{rainbow pruning of }\delta_r\text{ edges},\\[1mm]
 \text{a rainbow endpoint cycle on }D_r+\delta_r
       \text{ components}.
 \end{array}}
\tag{3.20}
\]

The GJM lexical analysis proves neither the `O(Cat_r)` upper bound on
`delta_r` nor the endpoint-cycle condition.  The only unconditional general
upper bound currently obtained directly from the forest is the trivial
`delta_r<=N'`, which is too large.  Establishing a Catalan-scale upper bound
on all lexical colour collisions is therefore the first quantitative gate of
this repaired route.

The upper outer contraction gives the dual path forest on rank-`r+1` sets.
After complementing its vertices, it is another lower-colour-perfect forest
on a copy of the rank-`r` layer.  It is not a set of connector edges for
`F_-` on the same vertex copies.

## 4. The central lexical edges cannot simply be contracted

The set `E` in (2.2) is deliberately not a perfect matching between the two
central levels.  In the notation of the paper, endpoints of upper lexical
paths receive one edge of `E`, isolated upper vertices receive two, and other
vertices receive none; the complementary statement holds on the lower
central level.  These degrees are what close the upper and lower paths into
a cycle factor.

Therefore contracting `E` does not give a bijection between rank-`r` and
rank-`r+1` vertices.  Without such a bijection there is no well-defined
single rank-`r` Johnson graph on which both outer contractions become edges.
The full GJM cycle factor is a cycle system in four cube levels, not the lift
of one two-coloured Johnson factor.

This is a structural failure, not merely an omitted verification.

## 5. The fixed-`z` six-cycle packing is absent

The GJM construction distinguishes the last bit.  Its upper path collection

\[
 \mathcal P=M_{2r+1,r+1}^{r}\cup M_{2r+1,r+1}^{r+1}
\tag{5.1}
\]

splits as `mathcal P_0 dotcup mathcal P_1` because, as the paper states
explicitly, neither lexical matching in (5.1) uses an edge along which the
last bit is flipped.

Take that last coordinate as the appended coordinate `z`, exactly as in the
dimension lift (1.2).

### Theorem 5 (no lifted diamond cycles in the lexical factor)

The GJM cycle factor `mathcal C_(2r+1)` contains no six-cycle of the form
(1.2) with the last coordinate as `z`.

#### Proof

Every cycle (1.2) contains the upper outer edge

\[
                         U--(U\cup\{z\}),                \tag{5.2}
\]

which flips the last bit.  All upper outer edges of the GJM factor belong to
`mathcal P`, and no edge of `mathcal P` flips the last bit.  Hence (5.2), and
therefore (1.2), is absent.  QED.

So the factor does not even give a near-perfect subpacking of the **exact**
fixed-`z` cycles: it gives zero of them.  Choosing a different distinguished
coordinate changes the sectioning and is not a consequence of the published
construction.

The later local six-cycle switches used by GJM to join the factor cycles do
not change this audit of the starting lexical factor, and the paper makes no
claim that the resulting Hamilton cycle decomposes into the fixed-`z` lifts
(1.2).

## 6. Conclusion

The middle-four-level construction contributes one rigorous object relevant
to the OR problem:

\[
 \boxed{
 \text{a lower-colour-perfect spanning Johnson forest with }
 O(\operatorname {Cat}_r)\text{ components}.}
\tag{6.1}
\]

What it does **not** contribute is the needed simultaneous pairing of lower
and upper colours on those same Johnson edges.  The exact missing operation
would have to add `D_r` carefully coloured connectors to `F_-`, or construct
the perfect interval matching of Lemma 1 directly.  The explicit GJM central
lexical edges and its fixed-last-bit outer paths do neither.
