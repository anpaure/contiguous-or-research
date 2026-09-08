# Independent audit of multidepth-safe cyclic-strip splicing

This note audits `MULTIDEPTH_SAFE_SPLICE_THEOREM_20260724.md`.  The local
switch classification, the rectangular depth-one colour table, the exact
ambient multigraph degree, the `4\ell` parallel-multiplicity bound, and the
`1-O(H^2/m)` transition-separation estimate are correct as statements about
the complete ambient strip family.  There is one necessary correction:
ambient partner cycles counted by that multigraph need not be vertex
disjoint.  A separate orbit estimate below restores the intended conclusion
in the parameter range `\ell^2=o(m)`.

## 1. Complete switch classification

Let the deleted edges be `AA'` and `BB'`, and reconnect them as `AB'` and
`BA'`.  Write

\[
 A'=A-a+b,\qquad B'=A-c+d,
\]

where `a,c\in A` and `b,d\notin A`.  The fourth vertex `B` is a common
neighbour of `A'` and `B'`.

If `a\ne c` and `b\ne d`, put `K=A-\{a,c\}`.  The four common neighbours of
`A'` and `B'` are

\[
 A=K+a+c,\qquad K+b+d,\qquad K+c+d,\qquad K+a+b.
\]

Thus the three possible choices for `B` are exactly the rectangular choice
`K+b+d` and the two chorded/diamond choices.  If `a=c` or `b=d`, the two
fixed vertices `A',B'` are adjacent; their common neighbours are the union
of the lower clique on `A'\cap B'` and the upper clique inside
`A'\cup B'`.  This exhausts all cases.

For the induced rectangular case one may write, cyclically,

\[
 V_i=K\cup\{r_i,r_{i+1}\},\qquad i\pmod 4.
\]

The old edges are `V_0V_1,V_2V_3`, and the new ones are
`V_0V_3,V_1V_2`.  Their lower colours are respectively

\[
 K+r_1,\ K+r_3;\qquad K+r_0,\ K+r_2,
\]

and their upper colours are

\[
 K+(Q-r_3),\ K+(Q-r_1);\qquad
 K+(Q-r_2),\ K+(Q-r_0),
\]

where `Q=\{r_0,r_1,r_2,r_3\}`.  The four colours in either rank are
pairwise distinct.  In a chorded case exactly one new lower colour and one
new upper colour recycle destroyed old colours; the other colour on each
side is new.  Old two-sided rainbowness excludes the common-lower and
common-upper clique choices, but it does **not** exclude the chorded cases.

## 2. Exact local transition criterion

Assume the retained pieces of the two old cycles are already
`H`-separated.  At one new seam let `\sigma` be the new transition label,
let `\alpha_i` be the label of the `i`-th old transition before the seam,
and let `\beta_j` be the label of the `j`-th old transition after it.
Provided the two new seams are more than `H` transitions apart, the merged
cycle is `H`-separated if and only if, at both seams,

\[
 \sigma\cap\alpha_i=\sigma\cap\beta_i=\varnothing
 \quad(1\le i\le H),
\]

and

\[
 \alpha_i\cap\beta_j=\varnothing
 \quad\text{whenever }i+j\le H.
\]

Necessity and sufficiency follow simply by classifying every pair of new
transition positions at cyclic distance at most `H`: a pair is either
wholly inside an old retained piece, contains the new seam, or straddles
the seam.  This is the exact run condition for both zero-runs and one-runs.

The stronger `H`-seam condition in the main note—pairwise disjointness of
all `H` labels before the seam, the seam label, and all `H` labels after
it—is therefore sufficient but not necessary.

For depth `q`, the `q` windows crossing a seam use only the transition
positions from `-q+1` through `q-1`.  If these `2q-1` labels are pairwise
disjoint, the crossing lower shadows are pairwise distinct: for two starts
`u<v`, the coordinate inserted on transition `u` is absent from the first
vertex of the earlier window but persists throughout the later window.
The dual argument with the coordinate removed on transition `u` separates
the upper shadows.  Hence the strong `H`-seam condition really does imply
crossing-window injectivity for every `q\le H`.  Ordinary `H`-separation
alone is weaker and does not supply this particular injectivity proof.

## 3. Ambient degree and multiplicity

The number of cyclic-strip cycles is

\[
 |\mathfrak C_{m,\ell}|=
 \frac{(2m)!}{4\ell(m-\ell)!^2}.
\]

Since each has `2\ell` Johnson edges and `J(2m,m)` has
`Wm^2/2` edges, every fixed Johnson edge is contained in

\[
 D_E=\left(\frac{(m-1)!}{(m-\ell)!}\right)^2
\]

strip cycles.  A fixed edge `(L,\{a,b\})` has exactly `(m-1)^2`
rectangular opposite edges: choose `c\in L` and
`d\notin L\cup\{a,b\}`.  Therefore the ambient rectangular incidence
multigraph is regular of degree

\[
 2\ell(m-1)^2D_E.
\]

There are no loops for `\ell\ge3`: the other strip edge with the same
antipodal exchange pair has lower colour at Johnson distance `\ell-1`,
not one.  Two cycles share at most `\ell` antipodal exchange pairs, and
each pair occurs on two edges in either cycle.  Their parallel incidence
multiplicity is consequently at most `4\ell`.

## 4. Strongly run-safe fraction

For a fixed strip edge, its `H` transitions before and `H` transitions
after it have `4H` distinct coordinate labels when `\ell>2H`.  Rejecting
`(c,d)` when either coordinate lies in this neighbourhood loses at most
`8H/(m-1)` of the rectangular choices (a deliberately loose bound).

Conditional on an opposite edge `f`, a uniformly chosen strip cycle through
`f` has exactly `2H` neighbourhood coordinates in the lower colour of `f`
and `2H` in the complement of its upper colour.  The stabilizer of `f` is
transitive on either `(m-1)`-element class.  Thus a fixed eligible coordinate
appears with probability `2H/(m-1)`.  Requiring its neighbourhood to avoid
the first `4H`-set and `\{c,d\}` loses at most

\[
 \frac{(4H+2)2H}{m-1}.
\]

This proves the claimed ambient fraction `1-O(H^2/m)`.

## 5. Vertex-disjointness correction

The complete ambient incidence multigraph also counts partner cycles which
meet the fixed cycle away from the switched edges.  Such an incidence does
not merge two vertex-disjoint cycles into a simple cycle.  The following
uniform estimate repairs this omission.

Fix a Johnson edge

\[
 f=\{L+a,L+b\},
\]

put `O=[2m]\setminus(L\cup\{a,b\})`, and choose uniformly among the `D_E`
strip cycles through `f`.  Its edge stabilizer is

\[
 (\mathfrak S_L\times\mathfrak S_O)\rtimes\langle(a\ b)\rangle.
\]

For an `m`-set `X`, every stabilizer orbit other than

\[
 \{L+a,L+b\},\qquad \{O+a,O+b\}
\]

has size at least `m-1`.  Indeed, its orbit size is a product of binomial
coefficients from the two `(m-1)`-element classes, with an optional factor
two; the only smaller cases are the displayed endpoint and complementary
endpoint orbits.

For any such orbit `\mathcal O`, let `c_f(X)` count strip cycles containing
both `f` and `X`.  It is constant on `\mathcal O`, and double counting gives

\[
 |\mathcal O|c_f(X)
 =\sum_{\Gamma'\ni f}|V(\Gamma')\cap\mathcal O|
 \le 2\ell D_E.
\]

Hence

\[
 \Pr(X\in V(\Gamma')\mid f\subset\Gamma')
 \le\frac{2\ell}{m-1}.
\]

Under the strong run-safety condition, neither endpoint of `f` belongs to
the fixed strip cycle `\Gamma`: either endpoint would have to be the other
cycle-neighbour of one switched endpoint, forcing the new label `\{c,d\}`
into the first old transition neighbourhood.  A complement of an endpoint
cannot occur in a strip cycle through `f`, because `\ell<m` gives that cycle
a nonempty core contained in every one of its vertices.  A union bound over
the `2\ell` vertices of `\Gamma` now yields

\[
 \Pr(V(\Gamma')\cap V(\Gamma)\ne\varnothing
      \mid f\subset\Gamma')
 \le\frac{4\ell^2}{m-1}.
\]

Consequently the vertex-disjoint, strongly `H`-run-safe incidence degree is
at least

\[
 \left(1-O\left(\frac{H^2+\ell^2}{m}\right)\right)
 2\ell(m-1)^2D_E.
\]

In the polylogarithmic strip regime used by the project,
`H^2+\ell^2=o(m)`, so the corrected graph remains asymptotically dense.
Without `\ell^2=o(m)`, the original ambient theorem remains true, but it
does not by itself assert that its incidences splice vertex-disjoint cycles.

## 6. Chorded rotor audit

For compatible holes `F` of rank `m-1` and `G` of rank `m+1` with
`|F\cap G|=m-2`, the data

\[
 K=F\cap G,\qquad Q=(F\cup G)\setminus K
\]

are unique, `|Q|=4`, and there is a unique `x\in Q` with

\[
 (F,G)=(K+x,K+(Q-x)).
\]

A chorded switch changes `x` to any other `y\in Q` while preserving
`(K,Q)`.  For fixed `x\ne y`, either of the two remaining elements of `Q`
may be the recycled lower colour, and these give exactly two witnesses.
Thus the ambient transport graph is indeed the disjoint union of

\[
 \binom{2m}{m-2}\binom{m+2}{4}
\]

copies of `K_4`, with witness multiplicity two on every graph edge.  This is
only an ambient classification; it supplies no selected-cycle lift or
multidepth colour safety by itself.
