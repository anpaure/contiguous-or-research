# Audit of the twelve-top recharge: squarefree repair and abstract top packing

Date: 2026-07-27

## 0. Verdict

The filler-column Koenig argument, the cyclic histogram cancellation,
and the physical trace telescope are correct.  The original
vertex-indexed choice

\[
                         F_i=F^{(z_i)}
\]

does **not** give squarefree shores: it creates six duplicate middle
owners on each shore.  The construction is repaired, without changing
any other part of the argument, by assigning the `F` palettes with the
proper edge-colouring already used for the `G` palettes:

\[
 e_i=\{z_{i-1},z_i\},
 \qquad
                         F_i=F^{(\gamma(e_i))}.
\tag{0.1}
\]

With (0.1), both shores are squarefree and the theorem is valid.  The
main theorem file has been patched accordingly.

There is also a fixed-uniformity, small-codegree **top-packet**
hypergraph.  It has a near-perfect matching by the fixed-uniformity
Pippenger--Spencer theorem.  This proves positive-density abstract
packing on the top resource.  It does not prove an owner-aware packing:
middle owners belonging to different packets can still collide.

## 1. Filler-column alignment is valid

Every word uses two outside placeholders, two disjoint `F` palettes,
and one `G` palette.  Hence the number of filler positions is

\[
 M-\bigl(2+2(2H-1)+(H-1)\bigr)=M-5H+1.
\]

For a core label `c`, its number of available rows on either six-row
table is `6`, `4`, or `5` according as it lies in no palette, one
`F` palette, or one `G` palette.  Matching the available P-rows to the
available Q-rows label by label gives a regular bipartite multigraph of
degree `M-5H+1`.  Koenig edge-colouring decomposes it into that many
perfect matchings, one for each filler column.  This simultaneously
uses each required label once in every row and makes the two column
multisets identical.

The edge-coloured replacement (0.1) does not change these counts:
each cycle still uses every `F` colour exactly once.

## 2. Histogram and trace checks

For cyclic column indices, left rotation has

\[
 (rp)(j)=p(j+1),\qquad p(M+1):=p(1).
\]

Thus the old and new column multisets are respectively

\[
 P_j+Q_{j+1},\qquad P_{j+1}+Q_j,
\]

and equality `P_j=Q_j` proves coefficientwise histogram cancellation,
including the wrap at `j=M`.

For the word on `U_i=C+{z_{i-1},z_i}`, the two endpoint blocks are

\[
 (z_{i-1},F_i),\qquad(z_i,F_{i-1}).
\]

The left-rotation derivative at deleted length `h` is

\[
 e_{(C\setminus(F_{i-1})^{h-1})+z_{i-1}}
 -e_{(C\setminus F_i^{h-1})+z_i}.
\]

The positive term at `i` is literally the negative term at `i-1`.
This remains true for arbitrary choices of the palettes `F_i`, so
(0.1) preserves the telescope at every `0<=h<=2H`.

The `G` block occupies positions `d-H+2,...,d`, which are disjoint from
both endpoint blocks under the stated size assumption.  It therefore
does not alter the telescope.

## 3. The collision in the original statement

Fix an outside vertex `v`.  In the unrotated P-table, the P-edge
entering `v` has a middle window deleting its near placeholder and the
first `H-1` entries of `F^(v)`.  The resulting owner is

\[
                         X_v=(C\setminus(F^{(v)})^{H-1})+v.
\]

In the rotated Q-table, the Q-edge leaving `v` has a middle window
deleting its shifted far placeholder and exactly the same first
`H-1` entries of `F^(v)`.  It gives the same owner `X_v`.  Hence the
old shore contains six repeated owners.  The new shore has the
symmetric six repetitions.  The `G` palettes do not help because these
two windows are pure `F` contexts.

## 4. Squarefreeness after the repair

Orient each cycle and write `e_Z^-(v),e_Z^+(v)` for the incoming and
outgoing edges at `v`.  The displayed edge-colouring has the four
colours

\[
 \gamma(e_P^-(v)),\ \gamma(e_P^+(v)),\
 \gamma(e_Q^-(v)),\ \gamma(e_Q^+(v))
\]

pairwise distinct.

In an unrotated word on `e_i=z_{i-1}z_i`, a middle window which deletes
the near placeholder has the pure core context

\[
                         \operatorname{pre}_{H-1}F_i.
\]

A window which deletes the far placeholder has context

\[
 \operatorname{suf}_tG^{(\gamma(e_i))}
 \cup
 \operatorname{pre}_{H-1-t}F_{i-1},
 \qquad 1\le t\le H-1.
\tag{4.1}
\]

After left rotation, the near placeholder is invisible and (4.1)
holds with `0<=t<=H-1`.  Therefore, at a retained outside label `v`,
the old shore has one pure P-incoming context, the P-outgoing mixed
contexts, and the rotated-Q-outgoing mixed contexts.  Equality of two
genuinely mixed contexts forces equality of their `G` colour, their
`F` colour, and `t`, because all palettes are disjoint.  The proper
edge-colouring excludes this across different top occurrences.  The
only cross-family pure/pure comparison is P-incoming against
Q-incoming, whose colours are also distinct.  A pure context cannot
equal a genuinely mixed context because the `F` and `G` families are
globally disjoint.  The new shore is symmetric.

Owners whose deleted window meets neither placeholder retain both
outside labels, so their outside pair identifies the top.  Owners whose
window meets exactly one placeholder were covered above.  These are
all cases.  Thus both repaired shores are squarefree.

## 5. Fixed-uniformity abstract top packing

Let the vertices be all rank-`M` tops.  The union of the two carrier
cycles is `K_6` minus a perfect matching.  Thus a simple packet is
specified by an `(M-2)`-set `C`, a six-set `S` outside `C`, and a
perfect matching `J` on `S`; its twelve vertices are

\[
                         C+e,
 \qquad e\in\binom S2\setminus J.
\]

Every such packet is isomorphic to the displayed carrier and hence
admits its two-cycle decomposition and proper palette colouring.  This
is a simple 12-uniform regular hypergraph.  Put `s=n-M`.  Its top
degree is

\[
                         D=12\binom M2\binom s4.
\tag{5.1}
\]

Indeed, after choosing the two elements of the fixed top outside `C`
and the other four elements of `S`, exactly 12 of the 15 perfect
matchings of `K_6` avoid the fixed top-edge.

Two distinct tops can lie in one packet only when their intersection
has size `M-1` or `M-2`.  For an adjacent pair (`|U cap V|=M-1`), the
the two graph edges share one endpoint.  Choose the common outside
label in `M-1` ways and the remaining three elements of `S` in
`binom(s-1,3)` ways.  Exactly 9 perfect matchings avoid the two
adjacent required edges, and hence

\[
 D_2^{\rm adj}=9(M-1)\binom{s-1}3,
 \qquad
 \frac{D_2^{\rm adj}}D=\frac6{Ms}.
\tag{5.2}
\]

For `|U cap V|=M-2`, the graph edges are disjoint.  There are
`binom(s-2,2)` choices for the two unused elements of `S`, and exactly
10 perfect matchings avoid both required disjoint edges, giving

\[
 D_2^{\rm disj}=10\binom{s-2}2,
 \qquad
 \frac{D_2^{\rm disj}}D
 =\frac{20}{M(M-1)s(s-1)}.
\tag{5.3}
\]

All other pair codegrees vanish.  Thus

\[
                         \Delta_2/D=O(m^{-2}).
\]

Uniformity is the fixed number 12 and `D -> infinity`.  The classical
fixed-uniformity near-matching theorem therefore gives a matching of
packets covering all but `o(1)` of the tops.

The stronger fixed-uniformity chromatic-index form gives

\[
                         \chi'=(1+o(1))D.
\]

Since the catalogue has `ND/12` packet edges, all but `o(D)` of its
colour classes have `(1-o(1))N/12` packets.  Choosing any
`L=Theta(m)` such classes gives `L` top-disjoint layers and

\[
                         (1-o(1))LN/12=\Theta(W)
\]

abstract packet occurrences.  Thus the required volume and average
`Theta(m)` top reuse are available at the undecorated top-incidence
level.

This last statement is deliberately only a top-packing theorem.  If
the hypergraph vertices are enlarged to include the `12d` middle
owners used by a packet, the uniformity grows with `m` and the needed
owner codegrees have not been bounded.  Consequently coefficient-one
global installation and chronology remain open.  In particular the
edge-colouring does not ensure that the target word produced on a top
in one layer is the exact source word required by that top's packet in
the next layer.  It solves abstract multi-layer supply, not physical
state compatibility.
