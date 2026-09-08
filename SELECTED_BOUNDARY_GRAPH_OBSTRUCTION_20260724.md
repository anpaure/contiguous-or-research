# The selected boundary graph: exact depth-one law and the multidepth lift

## Result and scope

Section 9 of `MULTIDEPTH_SAFE_SPLICE_THEOREM_20260724.md` reduces the
independent-cut loss to a directed path forest in a boundary graph.  This
note identifies that graph exactly at depth one and proves a rigorous
obstruction to obtaining its degree from the presently known marginals.

The main points are:

1. a mixed-flag arc is not an arbitrary adjacency of two used lower
   colours; the target edge must carry one prescribed exchange coordinate;
2. there are exponentially large, vertex-disjoint, two-sided-rainbow edge
   families with no mixed-flag arc at all; and
3. the natural pointwise lift through every depth `q<=H` is equivalent to
   equality of a `2H-1`-coordinate removal word around the two cuts.

Thus neither exact middle ownership nor depth-one lower/upper rainbowness
implies a long selected boundary forest.  The cyclic-strip matching must be
chosen with an additional transition-word correlation, or the soft ledger
must exploit arcs which add many but not all boundary colours.

---

## 1. Directed flags of selected Johnson edges

Let `mathcal P` be any vertex-disjoint collection of Johnson cycles or
paths in `J(2m,m)` whose edge intersections and edge unions are globally
distinct.  An undirected selected edge has a unique flag

\[
 L\subset U,
 \qquad |L|=m-1,\quad |U|=m+1,
\tag{1.1}
\]

and

\[
 U\setminus L=\{a,b\}.
\]

It gives two directed cut occurrences:

\[
 e_a(L,b):L+a\longrightarrow L+b
\tag{1.2}
\]

removes `a` and inserts `b`, while `e_b(L,a)` has the opposite orientation.

For a coordinate `a`, define

\[
 \mathcal F_a
 =\{(L,b):e_a(L,b)\text{ is a directed selected occurrence}\},
\tag{1.3}
\]

and let `mathcal S_a` be its projection to the lower colours `L`.  Global
lower rainbowness makes this projection injective.  If the selected family
has `E` undirected edges, then

\[
 \sum_{a\in[2m]}|\mathcal S_a|=2E.
\tag{1.4}
\]

---

## 2. Exact selected mixed-flag arc criterion

Take two directed occurrences

\[
 e_a(L,b):L+a\longrightarrow L+b,
\]

and

\[
e_a(M,c):M+a\longrightarrow M+c
\]

which remove the same coordinate `a` and come from distinct selected
undirected edges.  This is automatic for occurrences on distinct current
components.  In particular, global lower rainbowness gives `L!=M`.

### Theorem 2.1 -- selected depth-one boundary law

The one-edge path splice from the tail `L+a` of the first cut to the head
`M+c` of the second owns the mixed flag

\[
 (L,\ M+a+c)
\tag{2.1}
\]

if and only if there is a coordinate `d` such that

\[
 \boxed{
 c\in L,\qquad d\notin L\cup\{a\},
 \qquad M=L-c+d.}
\tag{2.2}
\]

Equivalently, `L` and `M` are adjacent in
`J([2m] setminus {a},m-1)`, and the target's inserted coordinate is exactly

\[
 c=L\setminus M.
\tag{2.3}
\]

If the two cut occurrences belong to vertex-disjoint components, then
automatically `d!=b`, so the new head is not the old head of the source.

#### Proof

The mixed-flag requirement is

\[
 (L+a)\cap(M+c)=L,
 \qquad
 (L+a)\cup(M+c)=M+a+c.
\tag{2.4}
\]

The first identity gives `M+c=L+d` for a unique
`d notin L union {a}`.  Since `c notin M`, there are a priori two cases:
either `c=d` and `M=L`, or `c in L` and `M=L-c+d`.  The first case is
excluded by the distinct-edge premise and global lower rainbowness.
Therefore `c in L` and `M=L-c+d`.  The union identity then follows
automatically:

\[
 M+a+c=L+a+d.
\]

Conversely these equations directly give (2.4).  If `d=b`, the target head
`L+d` equals the source head `L+b`, contradicting vertex-disjointness of the
two components. ∎

For a fixed `a`, the selected boundary graph is therefore a directed,
coordinate-labelled subgraph of the Johnson graph on `mathcal S_a`.  An
adjacency `L-M` is usable toward `M` only when the selected flag over `M`
has other exchange coordinate `L setminus M`.  Ordinary induced-edge counts
in `J(mathcal S_a)` overcount the selected boundary graph.

The exact number of selected directed depth-one arcs is

\[
 \boxed{
 A_1=
 \sum_{a}
 \sum_{(M,c)\in\mathcal F_a}
 \left|
 \{d\in M:M-d+c\in\mathcal S_a\}
 \right|,}
\tag{2.5}
\]

after deleting the terms whose two occurrences belong to the same current
component.  Formula (2.5), rather than only the cardinalities
`|mathcal S_a|`, is the selected degree ledger.

---

## 3. A zero-arc rainbow obstruction

The coordinate label in (2.3) is indispensable.

### Theorem 3.1 -- large two-sided-rainbow family with no mixed arc

Fix two coordinates `a!=x`.  For every

\[
 L\in\binom{[2m]\setminus\{a,x\}}{m-1},
\]

take the Johnson edge

\[
 (L+a,\ L+x).
\tag{3.1}
\]

This is a vertex-disjoint family of

\[
 \boxed{\binom{2m-2}{m-1}}
\tag{3.2}
\]

edges.  All lower colours `L` are distinct, all upper colours `L+a+x` are
distinct, yet its selected boundary graph has no arc in either orientation.

#### Proof

Distinct `L` give distinct lower and upper colours.  They also give disjoint
middle endpoints as graph vertices.  Equalities of the form
`L+a=M+x` are impossible because the left set contains `a` but not `x`,
whereas the right contains `x` but not `a`; same-side endpoint equalities
force `L=M`.  Thus the Johnson edges are vertex-disjoint.

In the orientation removing `a`, every selected target flag has inserted
coordinate `x`, while every selected lower colour omits `x`.  Condition
(2.3) would require `x in L`, a contradiction.  The orientation removing
`x` is symmetric.  Hence there is no mixed-flag arc. ∎

The size in (3.2) is asymptotic to one half of
`binom(2m-1,m-1)` and to one quarter of the middle width.  Therefore even a
very large vertex-disjoint, two-sided-rainbow partial ownership system can
have selected boundary degree zero.

This example is not itself a union of cyclic strips.  It proves the precise
scope obstruction: the properties currently exported by the strip matching
(vertex ownership plus signed depth-one rainbowness) do not logically imply
the desired boundary graph.  A theorem for the selected strip cycles must
use their transition-pair distribution, not only their row marginals.

There is also a zero-arc obstruction inside the cyclic-strip class itself.

### Proposition 3.2 -- a common antipodal pairing kills every boundary arc

Fix a fixed-point-free involution `pi` on `[2m]`.  Consider any family of
cyclic-strip cycles for which

* the moving coordinate set `R` is `pi`-invariant; and
* the cyclic order satisfies

  \[
  z_{t+\ell}=\pi(z_t).
  \tag{3.3}
  \]

Then the selected depth-one boundary graph of every subfamily is empty.
This remains true after restricting to pairwise vertex-disjoint cycles and
globally rainbow edge colours.

#### Proof

Every strip transition has exchange pair

\[
 \{z_t,z_{t+\ell}\}=\{z_t,\pi(z_t)\}.
\]

Hence a directed occurrence removing `a` always inserts `pi(a)`.  Its lower
colour omits both `a` and `pi(a)`.  If it were the target of a mixed-flag arc
from another occurrence removing `a`, Theorem 2.1 would require its inserted
coordinate `pi(a)` to equal `L setminus M` and therefore to belong to the
source lower colour `L`.  But every source occurrence removing `a` also has
exchange pair `{a,pi(a)}`, so its lower colour omits `pi(a)`.  This is a
contradiction. ∎

Proposition 3.2 does not assert that the restricted fixed-`pi` strip family
has a near-perfect multidepth matching.  It proves the exact structural
lesson needed here: cyclic-strip geometry alone supplies no positive
selected boundary degree.  Any successful matching theorem must enforce
diversity or expansion of the antipodal exchange pairings across cycles.

---

## 4. What random cut selection can certify

Suppose the selected strip matching has `p` cycles, each with `2ell` edges.
There are `4ell` directed cut occurrences per cycle.  Let `A_1` be the
number of ordered compatible occurrence arcs from (2.5) between distinct
cycles.

Choose one directed cut occurrence independently and uniformly on every
cycle.  Let `D_cut` be the resulting directed boundary graph.

### Proposition 4.1 -- exact random-cut first moment

\[
 \boxed{
 \mathbb E|E(D_{\rm cut})|
 =\frac{A_1}{16\ell^2}.}
\tag{4.1}
\]

#### Proof

Each ordered compatible occurrence arc specifies one cut occurrence on
each of two distinct cycles.  Both are selected with probability
`(4ell)^(-2)`.  Sum the indicators. ∎

There is no long-forest conclusion from (4.1) without a distributional
bound on `A_1` and on its cycle-level degrees/codegrees.  Theorem 3.1 shows
why `A_1` cannot be bounded below using only middle coverage and depth-one
rainbowness.

---

## 5. The exact pointwise multidepth lift

The signature condition (9.3) in the safe-splice note is stated as equality
of unordered sets of windows.  Internal window injectivity makes it just as
rigid as pointwise equality.

For cycle `i`, write

\[
 T^i_{t+1}=T^i_t-r^i_t+a^i_t,
\tag{5.1}
\]

with the cut transition indexed by `t=-1`.  Let `r_*` be the coordinate
removed by the new cross edge from `T^i_{-1}` to `T^j_0`.  Assume the old
and new transition blocks are `H`-separated.

Write `B_(i,q)^pm(r)` and `X_(ij,q)^pm(r)` for the individual windows in
(9.1)--(9.2), indexed by `1<=r<=q`.

### Theorem 5.1 -- ordered signature compatibility is a common removal word

The pointwise identities

\[
 \mathcal X_{ij,q}^-(r)=\mathcal B_{i,q}^-(r),
 \qquad
 \mathcal X_{ij,q}^+(r)=\mathcal B_{j,q}^+(r)
\tag{5.2}
\]

for every `1<=r<=q<=H` hold if and only if

\[
 \boxed{
 r_*=r^i_{-1}=r^j_{-1},
 \qquad
 r^i_t=r^j_t
 \quad(-H\le t\le H-2).}
\tag{5.3}
\]

#### Proof

For a lower crossing window with parameters `(q,r)`, the old source window
and the new cross window start at the same set `T^i_{-r}`.  In an
`H`-separated block, their intersections are that starting set minus their
respective removed coordinates.  The removals before the cut are common,
so equality is equivalent to

\[
 \{r_*,r^j_0,\ldots,r^j_{q-r-1}\}
 =
 \{r^i_{-1},r^i_0,\ldots,r^i_{q-r-1}\}.
\tag{5.4}
\]

Taking `r=q` first gives `r_*=r^i_{-1}`.  Taking `r=1` and successively
`q=2,...,H` then gives

\[
 r^j_t=r^i_t\qquad(0\le t\le H-2).
\tag{5.5}
\]

For an upper crossing window, the old target window and the cross window
end at the same set `T^j_{q-r}`.  Their unions are that endpoint plus the
coordinates removed on the respective preceding transitions.  The
post-cut target transitions are common, so equality is equivalent to

\[
 \{r^i_{-r},\ldots,r^i_{-2},r_*\}
 =
 \{r^j_{-r},\ldots,r^j_{-1}\}.
\tag{5.6}
\]

Taking `r=1,2,...,H` successively yields

\[
 r_*=r^j_{-1},
 \qquad
 r^i_{-s}=r^j_{-s}\quad(2\le s\le H).
\tag{5.7}
\]

Equations (5.5) and (5.7) give (5.3).  Conversely, substituting (5.3) into
(5.4) and (5.6) proves every identity in (5.2). ∎

For a cyclic strip, the removed coordinate on transition `t` is exactly the
`t`-th coordinate in its cyclic order.  Therefore the ordered multidepth
lift requires the two cut orders to share the same ordered coordinate block

\[
 (z_{-H},z_{-H+1},\ldots,z_{H-2})
\tag{5.8}
\]

of length `2H-1`, with the cross edge removing their common cut coordinate.
This is the exact failure of a naive depth-one lift: matching one lower and
one upper flag does not correlate the surrounding transition word.

### Corollary 5.2 -- setwise compatibility is equally rigid

Assume the old and cross boundary signatures are internally injective at
every depth, as supplied by the strong seam condition.  Then the unordered
set equalities

\[
 \mathcal X_{ij,q}^-=\mathcal B_{i,q}^-,
 \qquad
 \mathcal X_{ij,q}^+=\mathcal B_{j,q}^+
 \quad(1\le q\le H)
\tag{5.9}
\]

hold if and only if (5.3) holds.

#### Proof

At depth one there is only one window, so setwise and pointwise equality
coincide.  Induct on `q`.

For the lower signatures at depth `q`, every window with `r>=2` uses at
most the post-cut removal indices `0,...,q-3`.  The induction hypothesis and
the proof of Theorem 5.1 therefore show that these `q-1` cross windows equal
their old source windows with the same `r`.  The old depth-`q` windows are
distinct.  Equality of the two `q`-element sets forces the only remaining
cross window, `r=1`, to equal the only remaining old window.  Formula (5.4)
then yields `r^j_(q-2)=r^i_(q-2)`.

Dually, for the upper signatures, every window with `r<=q-1` uses only the
already matched pre-cut removal indices.  Those `q-1` windows agree
pointwise; injectivity and set equality force the remaining `r=q` windows
to agree, and (5.6) yields `r^j_(-q)=r^i_(-q)`.  This completes the induction
and proves (5.3).  The converse is Theorem 5.1. ∎

Thus exact multidepth signature compatibility, even in its original setwise
form, forces the common transition block (5.8).  Corollary 5.2 does not rule
out profitable **soft** arcs under (9.6), which need only add many new
colours rather than inherit every boundary signature exactly.

---

## 6. Exact remaining selected-graph gate

The next sufficient statement is now finite and explicit.

> Choose one directed cut occurrence on almost every selected strip cycle
> and a directed path forest on the cycles so that each arc satisfies the
> exact selected law (2.2), the seam-run condition, and has total soft
> new-colour gain
> \[
> \sum_{e=i\to j}\sum_{q\le H,\pm}
> |\mathcal X_{ij,q}^\pm\setminus R_{q,e}^\pm|
> =pH(H+1)-o(W).
> \]

Exact signature inheritance can be substituted for the soft gain, but
Theorem 5.1 and Corollary 5.2 then demand a common removal word of length
`2H-1` on every arc.  Theorems 3.1 and 3.2 prove that no such path forest
follows from the existing ownership/rainbow marginals or from cyclic-strip
geometry alone.
