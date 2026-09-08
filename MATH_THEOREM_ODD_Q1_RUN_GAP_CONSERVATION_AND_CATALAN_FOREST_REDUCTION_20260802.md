# Odd near-rainbow owners: exact run conservation and the balanced Catalan-forest gate

**Date:** 2026-08-02  
**Status:** unconditional identities and an exact localization theorem. They
do not prove a long-run Middle Levels Hamilton cycle, a `K17` carrier, an
upper-shadow theorem, a source factor, or a compiler.

## 0. Result

Put

\[
 k=2r-1,\qquad W={k\choose r},\qquad
 C=\operatorname {Cat}_{r-1}={1\over r}{2r-2\choose r-1}.
\]

Let `T_0,...,T_(W-1)` be a cyclic order of all rank-`r` sets. Suppose a set
`G` of cyclic adjacencies are Johnson edges and their rank-`(r-1)`
intersections are all different. Let `B` be the other adjacencies and put
`b=|B|`. The positive-staircase rigidity theorem gives such a decomposition
with

\[
 b\le 2d                                                     \tag{0.1}
\]

for the selected owner order of any hypothetical odd tight word; the
artificial last-to-first seam is included in `B`.

This note proves seven facts.

1. In the exact-rainbow Hamilton case (`B` empty), every coordinate has
   exactly `C` positive runs and `C` zero gaps. Their exact average lengths
   are `r` and `r-1`.
2. For a near-rainbow order there is an exact coordinatewise correction law,
   and the total correction is the sum of the Johnson-distance excess at the
   `b` exceptional seams.
3. Deleting one coordinate turns its positive runs into an exact
   lower-rainbow Catalan linear forest. Complementing the zero gaps turns
   them into an upper-completed Catalan linear forest. Long residence is
   exactly a simultaneous balanced-component problem in these `2k` forests.
4. All residence difficulty outside an `O(kd)` endpoint bank is already
   visible as component size. The at-most-`2d` q1 exceptions cannot hide a
   bulk family of short components.
5. Complementing the minimum odd-graph wreath factor gives, in every odd
   dimension, an exact-q1 two-factor whose positive runs all have length
   `r` and whose zero gaps all have length `r-1`.
6. A clean Boolean incidence-hexagon fusion of three wreath components has
   an exact finite aperture test.  The test shows precisely why abstract
   plane-tree connectivity is weaker than resident fusion.
7. Once the MSW factor is frozen, the supported hex list through an
   incidence is only a degree-two graph of order at most `2(r-2)`, and a
   canonical selected incidence has no supported hex at all.  Thus the
   prospective quadratic raw atlas does not survive literal freezing.

The arithmetic does **not** force a short run. In the exact-rainbow case,
the run/gap marginals permit a common floor `h` exactly when `h<=r-1`.
For the OR depth `h=d(k)+1`, this scalar condition holds for every odd
`k>=7`.  The balanced q1 factor itself is supplied in Section 5.  The
missing theorem is resident, upper-decorated component fusion, not another
q1 count.

## 1. Exact near-rainbow run identity

Fix a coordinate `x`. Define

\[
 P={2r-2\choose r-1}=rC,\qquad
 Z={2r-2\choose r}=(r-1)C.                             \tag{1.1}
\]

There are `P` owners containing `x` and `Z` owners omitting `x`.

Let `M` be the set of q1 colours not represented by `G`. Since `G` has
`W-b` distinct colours and the q1 layer has size `W`, `|M|=b`. Put

\[
\begin{aligned}
 m_x^0&=|\{S\in M:x\notin S\}|,
 &m_x^1&=|\{S\in M:x\in S\}|,\\
 b_x^0&=|\{i\in B:x\notin T_i\cap T_{i+1}\}|,
 &b_x^1&=|\{i\in B:x\in T_i\cap T_{i+1}\}|.
\end{aligned}                                             \tag{1.2}
\]

Thus `m_x^0+m_x^1=b_x^0+b_x^1=b`.

### Theorem 1.1 (exact exceptional-seam correction)

Let `R_x` be the number of cyclic positive `x`-runs (equivalently, zero
gaps). Then

\[
 \boxed{R_x=C-m_x^0+b_x^0=C+m_x^1-b_x^1.}             \tag{1.3}
\]

In particular, `|R_x-C|<=b`. Moreover,

\[
 \boxed{
 \sum_{x=1}^kR_x
   =W+\sum_{i\in B}\bigl(r-1-|T_i\cap T_{i+1}|\bigr).}
                                                               \tag{1.4}
\]

Every summand in (1.4) is nonnegative. It is zero precisely when that
exceptional seam is still a Johnson edge, for example a duplicate-colour
Johnson seam.

#### Proof

For an arbitrary cyclic binary word with `Z` zero positions and `R`
nonconstant positive runs, the number of edges whose endpoint intersection
omits the bit is

\[
 (Z-R)+2R=Z+R.                                          \tag{1.5}
\]

The first term counts zero--zero edges, and the second the two boundary
edges of every run.

There are `P` rank-`(r-1)` q1 colours omitting `x`. The good edges use
exactly `P-m_x^0` of them. Adding the `b_x^0` exceptional adjacencies whose
two endpoints are not both `x`-owners, (1.5) gives

\[
 Z+R_x=P-m_x^0+b_x^0.
\]

Since `P-Z=C`, this is (1.3); the second expression follows by subtracting
both sides from `b`.

Every missing q1 colour has rank `r-1` and hence omits exactly `r`
coordinates, so \(\sum_xm_x^0=rb\). An exceptional adjacency
\(T_iT_{i+1}\) omits from its intersection exactly
\(k-|T_i\cap T_{i+1}|\) coordinates.
Finally `kC=W` and `k-r=r-1`. Summing (1.3) proves (1.4). Distinct rank-`r`
owners intersect in at most `r-1` points, proving nonnegativity. \(\square\)

### Corollary 1.2 (exact rainbow)

If every cyclic adjacency is Johnson and every q1 colour occurs once, then

\[
 R_x=C,\qquad
 \sum\text{positive lengths}=rC,\qquad
 \sum\text{zero lengths}=(r-1)C.                    \tag{1.6}
\]

Hence the average positive and zero lengths are exactly `r` and `r-1`.
Equation (1.3) also handles all `2d` missing, duplicate, or non-Johnson
exceptions of a tight arbitrary-start schedule.

## 2. Coordinate deletion exposes a Catalan forest

Assume first that the owner cycle is exactly q1-rainbow.

### Theorem 2.1 (positive deletion forest)

Fix `x`. On the ground set `[k]-{x}`, form a graph `F_x^+` whose vertices
are all rank-`(r-1)` sets

\[
 A=T-\{x\},\qquad x\in T,                              \tag{2.1}
\]

and whose edges are the consecutive owner pairs which both contain `x`.
Then:

1. `F_x^+` is a spanning linear forest;
2. its edge intersections use every rank-`(r-2)` set exactly once;
3. it has exactly `C` components; and
4. its component orders are exactly the positive `x`-run lengths.

#### Proof

The containing-`x` vertices occur in maximal consecutive blocks of the
owner cycle, so the induced graph is a disjoint union of paths, with orders
equal to the run lengths. A q1 edge internal to such a block has colour `S`
containing `x`; after deleting `x`, its edge colour is the rank-`(r-2)` set
`S-{x}`. Exact q1 rainbowness uses all of these colours exactly once. There
are

\[
 {2r-2\choose r-1}=rC\quad\hbox{vertices and}\quad
 {2r-2\choose r-2}=(r-1)C\quad\hbox{edges},          \tag{2.2}
\]

so the forest has `C` components. \(\square\)

### Theorem 2.2 (zero-gap complement forest)

For each owner `T` omitting `x`, put

\[
 A=([k]-\{x\})-T,\qquad |A|=r-2.                      \tag{2.3}
\]

Internal zero-gap adjacencies give a spanning linear forest `F_x^-` on all
rank-`(r-2)` sets. It has exactly `C` components, whose orders are exactly
the zero-gap lengths. Its internal edge unions are distinct rank-`(r-1)`
sets. The unused `2C` rank-`(r-1)` colours occur once each as the two
endpoint caps of the `C` paths.

#### Proof

Complementation preserves Johnson adjacency and converts the intersection
colour of two zero owners into the union colour of their complements. The
zero blocks are paths of the asserted orders. They have

\[
 (r-1)C\text{ vertices},\qquad (r-2)C\text{ internal edges}, \tag{2.4}
\]

and hence `C` components. Exact q1 use makes the internal and boundary
colours distinct. Every path has two boundary q1 colours, accounting for
the remaining `2C` of the total `rC` rank-`(r-1)` colours. \(\square\)

### Corollary 2.3 (balanced Catalan-forest equivalence)

An exact-rainbow Hamilton owner cycle is positively depth-`d` resident iff
every component of every `F_x^+` has order at least `d+1`. It is
simultaneously positive/negative resident iff the same lower bound also
holds in every `F_x^-`.

Thus the long-run Middle Levels problem is equivalently a simultaneous
balanced Catalan-forest problem for these `2k` coordinate sections. A
separate forest for each coordinate is insufficient: all of them must be
sections of one owner cycle.

## 3. Near-rainbow localization

Return to `G,B` from Section 1 and keep only good edges.

### Theorem 3.1 (all bulk short runs are visible)

For a coordinate `x`, the good containing-`x` graph is a spanning linear
forest with exactly

\[
 C+m_x^1                                                    \tag{3.1}
\]

components. Every component not incident to an endpoint of an exceptional
seam is one complete positive run of the full cyclic order. Consequently,
if the full order has positive run floor `h`, every such unexposed component
has order at least `h`.

Across all coordinates, at most `2rb` positive components are incident to
exceptional-seam endpoints. Dually, at most `2(r-1)b` zero-gap components
are incident to those endpoints.

#### Proof

Good internal positive edges are exactly the represented q1 colours
containing `x`. There are `(r-1)C-m_x^1` of them on `rC` vertices, proving
(3.1). Removing `B` cuts the cyclic owner order only at exceptional seams;
an unexposed component therefore cannot be joined or split by restoring
those seams and is a complete run.

Each endpoint owner lies in exactly `r` positive coordinate sections and
`r-1` zero sections. There are at most two endpoints per exceptional seam,
which proves the two bounds. \(\square\)

### Consequence 3.2 (tight-word structural target)

With `b<=2d`, every tight odd word must induce a good q1 forest in which all
but at most

\[
 4rd=O(kd)
\]

positive components, and all but at most `4(r-1)d` zero components, already
meet the residence floor. The residual question on the exposed components
is a finite capped-age composition across the `b` seams and the linear cut.

This is stronger than the average-run calculation and weaker than a
construction. It rules out using the positive staircase merely as a large
scalar hiding place for a bulk residence defect.

## 4. No scalar impossibility

For one coordinate on an exact q1 cycle, specifying positive and zero run
lengths only requires two compositions

\[
 rC=\ell_1+\cdots+\ell_C,\qquad
 (r-1)C=g_1+\cdots+g_C.                               \tag{4.1}
\]

Compositions with all `ell_i,g_i>=h` exist iff `h<=r-1`. This proves only
marginal feasibility; it does not couple the `k` coordinates into one
sequence of all owners.

For odd `k>=7`, the definition of the optimal deadline gives

\[
 d(k)\le r-2.                                           \tag{4.2}
\]

One direct verification is as follows. The lower half has size
`2^(2r-2)-1`, while `W=binom(2r-1,r)`. At `r=4`,
`2^(2r-2)/W=64/35<2=r-2`. This ratio is multiplied from `r` to `r+1` by
`2(r+1)/(2r+1)`, so induction keeps it below `r-2`. Hence `(r-2)W` already
dominates the lower-half demand, and (4.2) follows.

Thus `h=d+1<=r-1`: exact q1 arithmetic is compatible with simultaneous
positive and zero residence in every nontrivial odd dimension from `k=7`
onward.

For the near-rainbow case, a sufficient marginal condition uniform over all
`b<=2d` exception patterns is

\[
 (C+2d)(d+1)\le(r-1)C.                                \tag{4.3}
\]

At `K17`, `(r,d,C)=(9,3,1430)`, and (4.3) reads

\[
 1436\cdot4=5744<11440.                                \tag{4.4}
\]

So even the worst coordinate correction allowed by q1 rigidity leaves
`5696` units of zero-gap length beyond the floor. There is no run-count or
gap-count obstruction to a `K17` long-run owner order.

## 5. An unconditional perfectly balanced q1 two-factor

The balanced component system whose marginal existence was left open above
already follows from the minimum-cycle factor of the odd graph.

Mütze, Standke, and Wiechert proved that

\[
                    KG(2r-1,r-1)                         \tag{5.1}
\]

has a spanning factor of `C` cycles, each of length `k=2r-1`.  The repository
records the result and the elementary fact that every such minimum odd cycle
is a wreath in `ODD_GRAPH_EXACT_WREATH_FACTOR.md`.

### Theorem 5.1 (complemented wreath factor)

For every odd `k=2r-1`, there is an exact-q1 owner two-factor on all rank-`r`
sets with the following properties:

1. it has exactly `C=Cat_(r-1)` components, each with `k` owners;
2. every coordinate has one positive run of length `r` and one zero gap of
   length `r-1` on each component; and
3. every rank-`(r-1)` q1 colour occurs exactly once.

Consequently this factor is simultaneously positive/negative depth-`d(k)`
resident for every odd `k>=7`.

#### Proof

Take one length-`k` odd-graph cycle

\[
                  A_0,A_1,\ldots,A_{k-1},A_k=A_0,       \tag{5.2}
\]

where the `A_i` are rank-`(r-1)` sets and consecutive sets are disjoint.
Since multiplication by two permutes `Z_k`, define

\[
                         T_i=[k]\setminus A_{2i}.        \tag{5.3}
\]

These are all complements of the owners of the odd cycle.  The two sets
`A_(2i)` and `A_(2i+2)` are distinct rank-`(r-1)` subsets of the rank-`r`
complement of `A_(2i+1)`, so their union is exactly that complement. Hence

\[
 T_i\cap T_{i+1}
  =[k]\setminus(A_{2i}\cup A_{2i+2})=A_{2i+1}.        \tag{5.4}
\]

The odd residues `2i+1` also run through `Z_k`. Thus this projected owner
cycle uses every `A_i` once as a q1 colour. Over the spanning odd-graph
factor, every rank-`r` owner and every rank-`(r-1)` colour occurs once.

Every minimum odd cycle has an omitted-label order `z_0,...,z_(k-1)` in
which

\[
 A_j=\{z_{j+1},z_{j+3},\ldots,z_{j+2r-3}\}.          \tag{5.5}
\]

Putting `w_i=z_(2i)`, (5.3) becomes

\[
                         T_i=\{w_i,w_{i+1},\ldots,w_{i+r-1}\}. \tag{5.6}
\]

Thus every coordinate occupies exactly `r` consecutive owners and is absent
from the other `r-1`. Finally `d(k)+1<=r-1` by (4.2). \(\square\)

Theorem 5.1 closes residence, q1, and owner coverage at the **two-factor**
level. It does not fuse the `C` wreaths into one chronology. Nor does it
give the rank-`(r+1)` upper palette: on the complemented factor that row is
the complement of the original wreath factor's lower-turn palette, whose
canonical MSW instance has a growing defect. The remaining theorem is a
resident, upper-decorated fusion, not construction of balanced components
from scratch.

## 6. Exact aperture obstruction for a wreath-hexagon fusion

Theorem 5.1 solves the balanced-factor problem but leaves a Catalan number
of components.  The smallest q1-preserving component move is a Boolean
incidence hexagon.  Its residence effect admits an exact description.

Let `S` have size `r-2`, and let `a,b,c` be distinct points outside `S`.
Write

\[
\begin{array}{lll}
 L_a=S+a,&L_b=S+b,&L_c=S+c,\\
 U_{ab}=S+a+b,&U_{bc}=S+b+c,&U_{ca}=S+c+a.
\end{array}                                               \tag{6.1}
\]

Suppose a wreath two-factor in the Middle Levels incidence graph contains
the alternating matching

\[
 O=\{L_aU_{ab},L_bU_{bc},L_cU_{ca}\}                     \tag{6.2}
\]

and not the other matching

\[
 N=\{L_aU_{ca},L_cU_{bc},L_bU_{ab}\}.                    \tag{6.3}
\]

Assume the three edges in `O` lie in three different wreath components.
Deleting them opens owner paths

\[
 P_a:U_{ab}\leadsto V_a,
 \qquad P_b:U_{bc}\leadsto V_b,
 \qquad P_c:U_{ca}\leadsto V_c,                         \tag{6.4}
\]

where `V_i` is the other owner incident with `L_i`.  Toggling the hexagon
reconnects these paths in the cyclic order

\[
                         P_aP_cP_b.                       \tag{6.5}
\]

For a coordinate `x`, a path `P`, and a bit `epsilon in {0,1}`, let
`p_P^epsilon(x)` and `s_P^epsilon(x)` be the lengths of the initial and
terminal `epsilon`-blocks in the owner-bit trace of `P`; they are zero when
the corresponding endpoint bit is not `epsilon`.

### Theorem 6.1 (exact one-hex aperture criterion)

Let `h<=r-1`.  The merged owner cycle in (6.5) has every positive run and
every zero gap of length at least `h` if and only if the following port test
holds at each of its three new seams `P -> Q`, for every coordinate `x`.

* If the terminal bit of `P` and initial bit of `Q` are both `epsilon`, then

  \[
                  s_P^\epsilon(x)+p_Q^\epsilon(x)\ge h. \tag{6.6}
  \]

* If those two bits are different, then both exposed blocks terminate at
  the seam and

  \[
        s_P^{\operatorname{last}_P(x)}(x)\ge h,
        \qquad
        p_Q^{\operatorname{first}_Q(x)}(x)\ge h.        \tag{6.7}
  \]

#### Proof

In a wreath component the cyclic `x`-trace is `1^r0^(r-1)`, up to
rotation.  Cutting one incidence therefore leaves either one full internal
block and two endpoint fragments, or two full endpoint blocks when the cut
is at a transition.  All internal blocks already have order at least `h`.

After (6.3), an endpoint fragment is maximal by itself exactly when the new
seam changes bit, giving (6.7).  When the bit agrees, precisely the terminal
fragment on the left and initial fragment on the right coalesce, giving
(6.6).  Every new maximal block is of exactly one of these forms, and every
form occurs.  This proves necessity and sufficiency. \(\square\)

The port data themselves are rigid.

### Lemma 6.2 (wreath aperture permutations)

At an old cut `L subset U,V`, orient the opened owner path from `U` to `V`.
Then

\[
 \{p_P^1(x):x\in L\}=\{1,2,\ldots,r-1\},              \tag{6.8}
\]

and `s_P^1(x)=r-p_P^1(x)` on `L`.  On the coordinates outside `U union V`,

\[
 \{p_P^0(x):x\notin U\cup V\}=\{1,2,\ldots,r-2\},    \tag{6.9}
\]

and `s_P^0(x)=r-1-p_P^0(x)`.  If `u=U-L` and `v=V-L`,
then the path begins with the full `u`-run of order `r` and the full
`v`-gap of order `r-1`, and ends with the full `u`-gap and full `v`-run.

#### Proof

Use the sliding-window form (5.6) and place the cut between the last and
first windows.  The `r-1` coordinates in their intersection disappear from
the successive windows after respectively `1,2,...,r-1` steps.  The
coordinates absent from both endpoint windows enter the complementary
zero window after respectively `1,2,...,r-2` steps.  The two symmetric
difference coordinates are exactly the two transition cases. \(\square\)

The raw `m^2` Boolean-hex count through an oriented incidence is prospective.
Once a literal factor is frozen, most of those circuits need not alternate.

### Theorem 6.3 (frozen support is a degree-two graph)

Fix a selected incidence `e=(L,U)` of any exact q1 two-factor, with
`|L|=r-1`, `U=L+b`.  An alternating Boolean hexagon containing `e` is
indexed by a pair

\[
                         a\in L,\qquad c\notin U.       \tag{6.10}
\]

Make the bipartite **support graph** `G_e` on these two label shores, joining
`a` to `c` when the corresponding hexagon alternates with the frozen factor.
Then

\[
                         \Delta(G_e)\le2,
              \qquad |E(G_e)|\le2(r-2).                \tag{6.11}
\]

Moreover, if the opened path at `e` is a wreath and positive-run floor `h`
is required, every accepting edge `ac` satisfies

\[
 p_e^1(a)\ge h,
 \qquad s_e^0(c)\ge h.                                \tag{6.12}
\]

The first admissible set in (6.12) has order `r-h`; the second has order
`r-h-1`.

#### Proof

For fixed `a`, another old edge of the hexagon has lower endpoint `U-a`.
That lower vertex has only two selected owner neighbours, so there are at
most two possible extension labels `c`.  For fixed `c`, the other old edge
at owner `L+c` must delete `a`; that owner has only two selected lower
neighbours, so there are at most two possible `a`.  Thus `G_e` has maximum
degree two.

At `U`, besides `L=U-b`, exactly one other selected lower neighbour has the
form `U-a_0`, with `a_0 in L`.  Taking `a=a_0` would put an edge of the
opposite hex matching in the factor, so it cannot be alternating.  Only
`r-2` left labels remain, proving (6.11).

In the toggled hex, the seam immediately before the fixed path introduces
the label `a`; its positive prefix is therefore exposed and gives the first
condition in (6.12).  The seam immediately after the fixed path introduces
`c`; the terminal zero fragment of `c` is exposed and gives the second.
Lemma 6.2 makes the positive prefix values on `L` the permutation
`1,...,r-1`, and makes the zero suffix values outside the two endpoint
owners the permutation `1,...,r-2`.  The asserted cardinalities follow.
\(\square\)

The linear upper bound is sharp in scale for arbitrary factors, but there is
no positive lower bound, even in the canonical complemented MSW factor.

### Theorem 6.4 (an MSW incidence with zero supported hexes)

Put `n=r-1`, use finite coordinates `0,...,2n-1` and the point `infinity`,
and let

\[
                         X=\{0,1,\ldots,n-1\}.          \tag{6.13}
\]

In the complemented MSW factor, the selected incidence

\[
                         X\subset X+\infty             \tag{6.14}
\]

lies in no alternating incidence hexagon, for every `n>=3`.

#### Proof

The mountain Dyck word `1^n0^n` generates one MSW odd cycle.  Its special
closing q1 colour is `X`, and the two complemented owners at that colour are
`X+infinity` and `X+(2n-1)`, so (6.14) is selected.

Write `Y={n,...,2n-1}`.  A possible hex through (6.14) chooses
`a in X` and `c in Y`.  The other two edges of the same alternating matching
would be

\[
 (X-a+\infty)\subset(X-a+c+\infty),
 \qquad
 (X-a+c)\subset(X+c).                                  \tag{6.15}
\]

Apply the defining MSW `g` and `h` scans to these two incidences.  The first
word is the complement-with-`infinity` of `Y+a`, and the second is the
finite word `X-a+c`.  There are only the two monotone blocks on either side
of the displaced steps, so the height scan gives

\[
\begin{array}{c|c}
\text{first incidence in (6.15)}&
 c=2n-2\ \text{or}\ (c=2n-1\ \text{and}\ a\ne0),\\
\text{second incidence in (6.15)}&
 a=1\ \text{or}\ (a=0\ \text{and}\ c\le2n-2).
\end{array}                                             \tag{6.16}
\]

Indeed, these are respectively the last down-step touching height zero in
`Y-c+a` (or the corresponding `h` deletion in `Y+a`) and the first up-step
touching height one in `X+c` (or the corresponding `g` insertion in
`X-a+c`).  Intersecting the two rows of (6.16), both incidences are selected
simultaneously exactly for

\[
 (a,c)=(0,2n-2),\quad(1,2n-2),\quad(1,2n-1).          \tag{6.17}
\]

For completeness, the three scans respectively select the following edge
of the opposite hex matching:

\[
\begin{array}{c|c}
(0,2n-2)&(X-0+\infty)\subset(X+\infty),\\
(1,2n-2)&(X-1+(2n-2))\subset
              (X-1+(2n-2)+\infty),\\
(1,2n-1)&X\subset X+(2n-1).
\end{array}                                             \tag{6.18}
\]

Thus every completion of the old three-edge matching already contains an
opposite edge and is not alternating.  All other pairs fail at least one
edge of (6.15). \(\square\)

Theorem 6.4 rules out `Omega(r)`, and even one, as a uniform supported-list
lower bound through a fixed MSW incidence.  Conjugating (6.14) by an
automorphism which preserves the factor cannot help.  Any abundance theorem
must choose its anchors globally, first modify the factor, or use compound
alternating circuits rather than demand a menu at every incumbent edge.

A bounded exact census of the whole complemented MSW factor gives the
following additional calibration.  `positive` means the one-hex output has
positive run floor `h=d+1`; `biresident` imposes the same floor on zero gaps.

\[
\begin{array}{c|r|r|r|r|r|r}
k&C&h&\text{alternating hexes}&\text{positive}&
 \max_e\deg_{\rm supp}(e)&\max_e\deg_{+}(e)\\ \hline
7&5&3&28&0&3&0\\
9&14&3&142&10&5&1\\
11&42&4&606&10&7&1\\
13&132&4&2464&40&9&1\\
15&429&4&9828&164&11&1\\
17&1430&4&38842&700&13&2
\end{array}                                               \tag{6.20}
\]

Every alternating hex in these rows is a clean three-wreath merge, but no
one-hex output is biresident.  At `K17`, `46,552` of the `48,620` selected
incidences lie in no positive-accepting hex at all.  Even ignoring every
support collision, the `700` initially accepting hexes can lower the
component count by at most `1400`, leaving at least `30` components.  A
tight near-rainbow chronology with at most six exceptional seams can join
at most seven such components.  Therefore the route

\[
 \text{MSW factor}+\text{one simultaneous bank of initially supported,
 positive-resident raw hexes}                           \tag{6.21}
\]

cannot solve `K17`.  Sequentially created hexes, expanded resident macros,
or longer alternating circuits are not covered by this finite no-go.

One useful quantitative consequence is that a new same-one seam can violate
(6.6) for at most `h-2` coordinates, and the same is true for a same-zero
seam.  At most three further nonautomatic endpoint-fragment inequalities
in (6.7) can fail.  Hence one new seam has at most

\[
                              2h-1                    \tag{6.22}
\]

failed aperture inequalities, and one hexagon has at most `6h-3`.  This is
a localization bound, not an existence proof: zero failures are required
for an unguarded resident fusion.

For a family of pairwise vertex-disjoint hexagons, delete all old
three-edge matchings and call the retained owner fragments **atoms**.  The
exact multi-hex residence test is obtained by recording, for every atom and
coordinate, its internal short-block flag, its two endpoint bits, and its
prefix/suffix lengths capped at `h`; concatenate these records in the final
transition cycles using (6.6)--(6.7).  Thus resident Hamiltonization of the
wreath factor is exactly the following correlated selection problem:

> choose a strict component-spanning incidence hypertree of alternating
> hexagons whose final capped-aperture automaton is accepting.

The known plane-tree leaf-pull or coherent-ECO two-section connectivity
forgets the aperture record and therefore does not imply this statement.
Conversely, an accepting strict hypertree fuses the Catalan wreaths while
preserving the full positive/negative residence floor.  This is the exact
residence obstruction before upper witnesses are imposed.

## 7. An unconditional q1-only actuator

Let `H` be the `r`-regular Middle Levels incidence graph, and let an exact
q1 two-factor be written as the union of two edge-disjoint perfect matchings

\[
 F=M_0\cup M_1.                                         \tag{7.1}
\]

### Theorem 7.1 (every selected incidence is movable in the q1 fibre)

For `r>=3`, every edge \(e\in M_0\) lies on an alternating circuit which can
be switched while preserving every owner degree and every q1 row exactly,
and while remaining disjoint from `M_1`.

#### Proof

Delete \(M_0\cup M_1\) from `H`. The residual graph is `(r-2)`-regular and
bipartite, so it has a perfect matching `N`. The graph \(M_0\cup N\) is a
disjoint union of alternating even cycles, and `e` lies on one of them.
Switch `M_0` along that component. The result is another perfect matching,
still disjoint from `M_1`; hence (7.1) remains an exact q1 two-factor and
`e` has been removed. \(\square\)

Every literal short run contains selected incidence edges, so Theorem 7.1
can destroy any chosen old blocker on the owner/q1 face. It does **not** say
that the switched factor stays Hamiltonian, that fewer short runs are born,
or that the upper palette and deeper shadows survive. Those simultaneous
acceptance rows, rather than q1 immobility, are the switching theorem still
missing.

### Corollary 7.2 (complete q1 reset)

With `N` as in the proof, replacing all of `M_0` by `N` gives the exact q1
factor

\[
                              F'=N\cup M_1.              \tag{7.2}
\]

No projected owner edge of `F` survives in `F'`. Consequently every old
short-run segment is broken simultaneously.

Indeed, the projected edge in a q1 row `S` joins its `M_0`-owner to its
`M_1`-owner. The residual matching `N` uses neither incidence, so the new
row joins a different owner to the old `M_1`-owner. Two rank-`r` owners have
at most one rank-`(r-1)` intersection, so the same projected edge cannot
reappear in another row.

Corollary 7.2 is a reset, not a descent theorem: it may replace the old debt
by equally large new debt and may split the factor. Its value is to rule out
an invariant-blocker explanation on the unrestricted q1 face and to expose
the honest target: choose the residual perfect matching in correlation with
history, topology, and upper-provider rows.

## 8. `K17` and finite calibration

The current authenticated equivariant factor at

```text
/home/amodo/or15/work/root_k17_c68b_c6xc6_20260802/
  promoted_depth8_res1241/factor.tsv
```

is exact q1, owner-once, upper-q1-complete, and one-cycle. Its positive
short-run histogram is

```text
length 1       0
length 2     663
length 3     578
total       1241 = 73 * 17
```

and its zero-gap short total is `8415`. The `73` is an orbit count, not a
word-length gap.

A single linear cut can make at most one positive run per coordinate a
boundary run, so merely opening this cycle leaves at least

\[
 1241-17=1224                                             \tag{7.1}
\]

positive blockers. More generally, changing only six seam locations while
freezing every other adjacency can touch at most `2*r*6=108` positive
good-forest components by Theorem 3.1. Hence the q1-exception allowance is
not a shortcut for this incumbent. Bulk q1-preserving rethreading is still
required.

This is not a global `K17` no-go. A non-equivariant factor or a long
q1-preserving alternating circuit can alter many bulk adjacencies while
keeping `b=0`; Theorem 7.1 confirms that the unrestricted q1 fibre has such
mobility.

There is also a useful positive calibration. Applying the exact depth-three
derivative to `answers/k11.word` gives a cyclic owner order with

```text
owners              462 / 462
q1 facets           462 / 462
positive runs       42 per coordinate
minimum positive     4
short positive       0
minimum zero         1
short zero          19 per coordinate
```

Thus an exact-q1 Hamilton cycle can genuinely attain the required positive
residence floor; q1 rainbowness does not force a short positive run. The
same witness shows that positive residence does not imply dual gap
residence.

The bounded audit was compiled with `g++ -O3 -march=native` and run on the
H100 CPU under two roots,

```text
/home/amodo/or15/work/root_odd_q1_run_gap_identity_20260802
/home/amodo/or15/work/root_wreath_hex_aperture_20260802
/home/amodo/or15/work/root_msw_supported_resident_hex_supply_20260802
```

with hashes

```text
ff0df67024b080e6fd1324ebad7f0640c450794691418093724e5b91db4fb62f
  audit_odd_q1_run_gap_identity_20260802.cpp
ad3d769260b4c7be9498b755133bb0e21c06befec15b109ee892271e9cb91f88
  k11.out
746b469af108558b14e7f6af0e3f76f9b6f39f70b3561e0258cc976650761850
  k11.word
a15c5ab774f8aba90944dd77c1804b428a9d5207ca6b8658696c66a7ee28fb00
  audit_wreath_hex_aperture_identity_20260802.cpp
6369f89689ccff31e95c5a46c6922475f4fbe7c0bf4817aea2d204fd07e85275
  audit.out
8126f0a8fdeccae7c87e0bfae9634b4729c54f86298b4e3759b2d515e599a806
  audit_msw_supported_resident_hex_supply_20260802.cpp
23a1b0e06b83d89876ddd8877f914e7eeb982f52c0890f57cc45690117477c3c
  audit.out (complete MSW supported/accepting census)
```

The second audit checks the aperture-permutation identities and compares
the port criterion with a direct cyclic run scan in `660,000` deterministic
trials on ground sizes `7,9,11,13,15,17`.
The third audit reconstructs the MSW factor from the Chung--Feller `g,h`
maps, verifies the wreath components, exhausts every Boolean incidence
hexagon through `K17`, and directly replays the positive/biresident aperture
tests used in (6.20).

## 9. Exact surviving theorem

The residence row of an odd tight word has now been reduced to:

> **Resident upper-decorated Catalan fusion.** Starting from the complemented
> wreath factor of Theorem 5.1 (or another balanced q1 factor), fuse its
> `Cat_(r-1)` components to `O(d)` paths and finally one chronology while
> retaining the run/gap floor and installing the complete upper witness
> bank. On a merely near-rainbow endpoint, solve the `O(kd)`
> occurrence-labelled boundary states across the at-most-`2d` seams.

The q1 count, balanced two-factor supply, and fixed-incidence mobility are
settled. What remains is accepted topology/upper transport without losing
that balance.
Neither the `73` equivariant `K17` defect orbits nor the poor dual gaps of
the `K11` witness imply a global obstruction.
