# Two-sided trace injectivity forbids a mixed-frame cycle in the minimal
# quartet associator

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

The 24-owner trade in
`MATH_THEOREM_LOCAL_PAIR_FRAME_ASSOCIATOR_20260726.md` is a genuine exact
exchange between the pair frames

\[
                         ab\mid cd
 \qquad\text{and}\qquad ac\mid bd.
\]

It cannot be reorganized into actual cycles which change between the two
frames while retaining injective lower **and** upper depth-one traces.

More precisely, consider the union of all edges on the two sides of that
trade.  Every 2-factor of this union whose edge intersections are all
distinct and whose edge unions are all distinct splits into two frame
sectors.  No component contains a frame-specific edge from each sector.

The obstruction is local and sharp.  At either shared hub, choosing one
incident edge from each transverse frame repeats either the lower
intersection or the upper union.  Thus a literal two-sided frame-changing
primitive must be larger than the minimal four-coordinate recoupling, or
must tolerate and later absorb a depth-one collision.

This explains the exact boundary between the two current positive facts:

* the six-for-six quartet switch changes frame integrally but only between
  whole cycles; and
* the phase-synchronized `Q_8` cycle changes its adjacent-pair frame, but
  has not supplied a literal physical target decoder.

## 1. The union graph

Use the notation of the local associator theorem.  The special-coordinate
states are

\[
 \begin{aligned}
 U&=bc,&V&=ad,\\
 A&=ac,&B&=bd,&C&=ab,&D&=cd.
 \end{aligned}                                             \tag{1.1}
\]

The first frame has local square

\[
                         U-A-V-B-U,                           \tag{1.2}
\]

and the second has

\[
                         U-C-V-D-U.                           \tag{1.3}
\]

For every reservoir orientation `Y in mathcal Y`, their union on the
special coordinate is the complete bipartite graph

\[
                         K_{\{U,V\},\{A,B,C,D\}}.             \tag{1.4}
\]

The remaining edges are reservoir-square edges at each leaf
`A,B,C,D`.  They preserve the leaf and hence preserve the sector

\[
                         \{A,B\}\quad\text{or}\quad\{C,D\}.   \tag{1.5}
\]

Call an edge in (1.2) genuinely frame zero and an edge in (1.3) genuinely
frame one.  Reservoir edges are frame-neutral for the argument.

## 2. The hub collision table

Fix one reservoir orientation `Y`; it is adjoined unchanged to every
special set below.  At the hub `U=bc`, the four possible neighbours have
the following lower special intersection and upper special union:

\[
\begin{array}{c|cc}
\text{edge}&\text{intersection}&\text{union}\\ \hline
U A&c&abc\\
U B&b&bcd\\
U C&b&abc\\
U D&c&bcd.
\end{array}                                               \tag{2.1}
\]

Thus every cross-sector pair, one neighbour from `{A,B}` and one from
`{C,D}`, repeats one trace:

\[
 \begin{array}{c|c}
 A,C&\text{same upper union }abc\\
 A,D&\text{same lower intersection }c\\
 B,C&\text{same lower intersection }b\\
 B,D&\text{same upper union }bcd.
 \end{array}                                               \tag{2.2}
\]

At `V=ad` the analogous table is

\[
\begin{array}{c|cc}
\text{edge}&\text{intersection}&\text{union}\\ \hline
V A&a&acd\\
V B&d&abd\\
V C&a&abd\\
V D&d&acd,
\end{array}                                               \tag{2.3}
\]

and again every cross-sector pair repeats either its lower or upper trace.
Adjoining the same `Y` does not change any equality.

## 3. Sector theorem

### Theorem 3.1 (no literal mixed-frame 2-factor)

Let `mathcal H` be a 2-factor of the union graph of the two exact
24-owner factors.  Suppose the maps

\[
 e=XY\longmapsto X\cap Y,
 \qquad
 e=XY\longmapsto X\cup Y                              \tag{3.1}
\]

are both injective on `E(mathcal H)`.  Then every cycle of `mathcal H`
is contained in one of the two sector subgraphs

\[
 \{U,V,A,B\}\times\mathcal Y
 \qquad\text{or}\qquad
 \{U,V,C,D\}\times\mathcal Y,                        \tag{3.2}
\]

with the reservoir edges at the displayed leaves.  In particular, no
cycle contains a genuinely frame-zero edge and a genuinely frame-one edge.

#### Proof

At a hub vertex `(U,Y)` or `(V,Y)`, the 2-factor chooses exactly two
incident edges.  By (2.2)--(2.3), injectivity of both maps in (3.1) forbids
choosing one neighbour from each sector.  Hence both selected neighbours
belong to `{A,B}` or both belong to `{C,D}`.

After leaving a hub, the only non-hub edges are reservoir edges.  Such an
edge fixes its leaf and therefore cannot change the sector (1.5).  At the
next hub, the same argument forces the cycle to leave in the sector in
which it arrived.  Induction around the cycle proves (3.2). \(\square\)

### Corollary 3.2

No switching, splicing, or successor reassignment confined to the minimal
24-owner support can simultaneously have:

1. exact middle ownership;
2. one actual cycle using both quartet frames; and
3. injective lower and upper depth-one physical traces.

The theorem permits a frame-changing cycle if one sign is allowed to
collide.  It also permits the original exact six-for-six trade, because its
cycles individually remain in one sector.  Hence the obstruction is
exactly two-sided literal trace injectivity, not owner exactness alone.

There is a quantitative form.  Call a hub **mixed** when its two selected
2-factor edges go to different sectors, and let `M` be the number of mixed
hubs.  If `L` and `U` are the multisets of lower intersections and upper
unions of all selected edges, then

\[
 (|E|-|\operatorname{supp}L|)
 +( |E|-|\operatorname{supp}U| )\ \ge\ M.             \tag{3.3}
\]

Indeed, (2.2)--(2.3) assign one repeated lower or upper target to every
mixed hub.  Targets assigned at different hubs are distinct: their
reservoir orientation `Y` or their special singleton/triple differs.
Moreover, different hubs use disjoint incident edge pairs.  Thus the
duplicate charges add.  Every cycle which enters and later leaves the other
frame sector has at least two mixed hubs, so each genuine frame excursion
costs at least two units of combined signed collision excess.
