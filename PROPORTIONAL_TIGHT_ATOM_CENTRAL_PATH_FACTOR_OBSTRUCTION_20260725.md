# Proportional tight atoms: the canonical central path-factor obstruction

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, solver, or
computer experiment is used.

## 0. Outcome and exact scope

This note audits the proposed lift from the `b` shortest augmenting paths
in the middle inclusion graph to one more proportional tight atom.

The central conclusion of
`PROPORTIONAL_TIGHT_ATOM_MATCHING_EXPANSION_20260725.md` is an ordinary
inclusion matching of the correct cardinality.  That conclusion is not
enough even to reconstruct the two central ranks of the atoms.  The
pairing-independent missing object is an exact alternating path factor in
the induced middle-incidence graph.

The following statements are proved.

1. A family of `tb` available rank-`m` vertices and `tb` available
   rank-`m+1` vertices is the central projection of `t` tight atoms if and
   only if its induced inclusion graph has a spanning factor of `t`
   alternating `(b,b)` paths satisfying an explicit coordinate-freshness
   condition.
2. Consequently the induced graph must contain at least

   \[
   t(2b-1)=2tb-t
   \]

   inclusion edges.  A perfect matching supplies only `tb` of them.  The
   missing `t(b-1)` incidences are tight-row seams, not bookkeeping.
3. For every polynomial-size packet, there are central resource families
   whose induced inclusion graph is exactly a perfect matching, while
   their addition-label vector and every central star-moment inequality
   proved in the earlier report are exactly valid.  They admit no tight
   atom at all.
4. For every perfect matching `Q` of the middle inclusion graph, and for
   all sufficiently large `m`, the empty atom matching has a legitimate
   choice of `b` equally shortest `Q`-augmenting paths whose induced
   central graph is exactly `b` isolated edges.  Thus those `b` shortest
   paths cannot be lifted even to one central tight row.

The last statement is uniform in `Q`, but its quantifier is important: for
every `Q` there exists a bad choice among the tied shortest paths.  It does
not prove that a deliberately seam-aware choice of `Q` and of the paths is
impossible.  It proves that path length, deletion count, the central
matching property, and the current central moment laws do not imply the
lift.  Any positive continuation must choose in a larger tight-path state
graph or prove the cylinder-fibre expansion condition from the earlier
report.

## 1. Central tight rows and the induced inclusion graph

Let

\[
n=2m+1,
\qquad 2\le b\le m,
\qquad W=\binom{2m+1}{m},
\]

and let `G_m` be the bipartite inclusion graph between
`binom([n],m)` and `binom([n],m+1)`.

For an injective word, the two central target rows are

\[
L_i=\{x_i,x_{i+1},\ldots,x_{i+m-1}\},
\qquad
R_i=\{x_i,x_{i+1},\ldots,x_{i+m}\},
\qquad 0\le i<b.
\tag{1.1}
\]

They obey

\[
L_i\subset R_i,
\qquad
L_{i+1}\subset R_i
\quad(0\le i<b-1).
\tag{1.2}
\]

Thus their incidence graph contains the alternating path

\[
L_0-R_0-L_1-R_1-\cdots-L_{b-1}-R_{b-1}.
\tag{1.3}
\]

The ordinary central flag matching consists only of the `b` edges
`L_iR_i`; it omits the `b-1` seam edges `L_{i+1}R_i`.

Suppose now that

\[
\mathcal L\subseteq\binom{[n]}m,
\qquad
\mathcal R\subseteq\binom{[n]}{m+1},
\qquad
|\mathcal L|=|\mathcal R|=tb.
\tag{1.4}
\]

Write

\[
H(\mathcal L,\mathcal R)=G_m[\mathcal L,\mathcal R]
\tag{1.5}
\]

for the full induced inclusion graph.  This pairing-independent graph is
the correct central object: after an alternating exchange, a new atom is
free to pair an available `m`-set with any available containing
`(m+1)`-set, not only with the partner used by the witness matching.

## 2. Canonical path-factor characterization

### Definition 2.1 — fresh alternating `(b,b)` path

An alternating path in `G_m`, written

\[
L_0-R_0-L_1-R_1-\cdots-L_{b-1}-R_{b-1},
\tag{2.1}
\]

is **fresh** if, on putting

\[
z_i=R_i\setminus L_i
\quad(0\le i<b),
\qquad
d_i=R_i\setminus L_{i+1}
\quad(0\le i<b-1),
\tag{2.2}
\]

the following hold:

\[
z_0,\ldots,z_{b-1}
\text{ are distinct members of }[n]\setminus L_0,
\tag{2.3}
\]

and

\[
d_0,\ldots,d_{b-2}
\text{ are distinct members of }L_0.
\tag{2.4}
\]

The set differences in (2.2) are singletons because every displayed edge
is an inclusion edge between consecutive ranks.  We identify each
singleton with its element.

### Theorem 2.2 — exact central path-factor theorem

The resource pair \((\mathcal L,\mathcal R)\) in (1.4) is the central target
system of `t` pairwise central-disjoint proportional tight atoms with
central start sets \(I_0=I_1=\{0,\ldots,b-1\}\) if and
only if \(H(\mathcal L,\mathcal R)\) contains a spanning union of `t`
vertex-disjoint fresh alternating paths of the form (2.1).

Here “central-disjoint” means that all selected rank-`m` targets are
distinct and all selected rank-`m+1` targets are distinct.  The theorem is
only a central-rank statement; it does not assert disjointness of the
off-central targets of the completed words.

#### Proof

For necessity, take one atom and use its natural order (1.1).  The path
edges are (1.2).  Moreover,

\[
z_i=x_{i+m},
\qquad
d_i=x_i.
\]

Injectivity of the word gives (2.3)--(2.4).  Distinct atoms in the central
resource family give vertex-disjoint paths, and all vertices are used.

For sufficiency, fix one fresh path.  Choose

\[
d_{b-1}\in
L_0\setminus\{d_0,\ldots,d_{b-2}\},
\tag{2.5}
\]

which is possible because \(b\le m\).  Define

\[
x_i=d_i\quad(0\le i<b).
\tag{2.6}
\]

Fill positions `b,...,m-1` with the elements of

\[
L_0\setminus\{d_0,\ldots,d_{b-1}\}
\]

in any order, and put

\[
x_{m+i}=z_i\quad(0\le i<b).
\tag{2.7}
\]

Equations (2.3)--(2.4) show that these `m+b` labels are distinct.  The
path recursion gives, by induction,

\[
L_i=
\left(L_0\setminus\{d_0,\ldots,d_{i-1}\}\right)
\cup\{z_0,\ldots,z_{i-1}\},
\tag{2.8}
\]

and then \(R_i=L_i\cup\{z_i\}\).  Hence the word constructed in
(2.6)--(2.7) realizes the prescribed path exactly as its central target
row.

Perform this construction independently on the `t` paths.  Coordinate
labels may be reused by different words; only injectivity inside one word
is required.  Vertex-disjointness of the paths gives central target
disjointness.

In the proportional Gaussian setup one needs the word through position
`m+b+H-1`.  If

\[
b+H\le m+1,
\tag{2.9}
\]

then exactly `H` further unused labels can be appended, since

\[
n-(m+b)=m+1-b.
\]

The actual parameters satisfy the stronger inequality `b+H<m` for all
sufficiently large `m`.  This completes the proof.  ∎

### Corollary 2.3 — canonical edge-count and seam obstruction

If \((\mathcal L,\mathcal R)\) is centrally realizable by `t` atoms, then

\[
\boxed{
|E(H(\mathcal L,\mathcal R))|
\ge t(2b-1)=2tb-t.}
\tag{2.10}
\]

In particular, a perfect matching in the induced graph accounts for only
`tb` incidences.  A realization needs a further `t(b-1)` incidences in
the induced graph.

#### Proof

Each of the `t` vertex-disjoint paths has exactly `2b-1` edges.  Their
edge sets are disjoint.  ∎

The inequality is necessary and not sufficient: the extra incidences
must form paths of the exact lengths, and the paths must satisfy
(2.3)--(2.4).

## 3. A robust no-seam family satisfying all central moment laws

The next theorem shows that the obstruction is not detected by the
integral endpoint hypersimplex or by any of the central star-moment bounds
proved previously.

### Theorem 3.1 — exact diagonal central resources

Let \(m\ge2\), \(2\le b\le m\), and \(t\ge1\) be integers satisfying

\[
\boxed{
tb\bigl(1+m(m+1)\bigr)<\binom{2m}{m}.}
\tag{3.1}
\]

There are families

\[
\mathcal L\subseteq\binom{[2m+1]}m,
\qquad
\mathcal R\subseteq\binom{[2m+1]}{m+1},
\qquad
|\mathcal L|=|\mathcal R|=tb,
\]

with the following properties.

1. \(H(\mathcal L,\mathcal R)\) is exactly a matching of `tb` isolated
   inclusion edges.
2. Those edges can be written

   \[
   (A_{i,h},A_{i,h}\cup\{z_i\}),
   \qquad 1\le i\le b,
   \quad 1\le h\le t,
   \tag{3.2}
   \]

   for distinct labels `z_1,...,z_b`.
3. If `a_x` is the multiplicity of `x` as an added label in (3.2), then

   \[
   a_x=t\mathbf 1_{\{x\in Z\}},
   \qquad Z=\{z_1,\ldots,z_b\}.
   \tag{3.3}
   \]

   Thus

   \[
   0\le a_x\le t,
   \qquad
   \sum_xa_x=tb,
   \tag{3.4}
   \]

   and, for every \(X\subseteq[n]\),

   \[
   t\bigl(b-(n-|X|)\bigr)_+
   \le a(X)\le t\min(b,|X|).
   \tag{3.5}
   \]
4. For \(1\le j\le m+1\) and \(T\in\binom{[n]}j\), let
   \(z(A,B)\) denote the unique element of \(B\setminus A\), and define

   \[
   g(T)=
   \#\left\{(A,B)\text{ in (3.2)}:
   z(A,B)\in T,
   \ T\setminus\{z(A,B)\}\subseteq A
   \right\}.
   \tag{3.6}
   \]

   Equivalently, if `c_0(T)` and `c_1(T)` count the selected lower and
   upper targets containing `T`, then

   \[
   g(T)=c_1(T)-c_0(T).
   \]

   Then

   \[
   0\le g(T)\le t\min(j,b),
   \tag{3.7}
   \]

   and

   \[
   \sum_{T\in\binom{[n]}j}g(T)
   =tb\binom m{j-1}.
   \tag{3.8}
   \]

   If `r_0(T),r_1(T)` are the corresponding residual star counts in the
   full two middle layers, then, for \(1\le j\le m\),

   \[
   D_j-t\min(j,b)
   \le r_1(T)-r_0(T)\le D_j,
   \tag{3.9}
   \]

   where

   \[
   D_j=
   \binom{n-j}{m+1-j}-\binom{n-j}{m-j}.
   \]
5. Nevertheless these resources do not centrally realize even one tight
   row of length at least two, and in particular do not realize `t`
   atoms of width `b`.

#### Proof

Fix distinct labels `z_1,...,z_b`.  For a prescribed `z_i`, the number of
`m`-sets avoiding it is

\[
\binom{2m}{m}.
\tag{3.10}
\]

Choose the `tb` sets `A_{i,h}` successively, always avoiding their
prescribed `z_i`, and require every two chosen sets to have Johnson
distance at least two.  One previously selected `m`-set forbids at most

\[
1+m((2m+1)-m)=1+m(m+1)
\tag{3.11}
\]

sets: itself and its Johnson-distance-one neighbors.  Condition (3.1)
therefore leaves an admissible choice at every step.

Put

\[
B_{i,h}=A_{i,h}\cup\{z_i\}.
\]

If a distinct selected set `A_{i',h'}` were contained in `B_{i,h}`, then
it would be a distinct `m`-subset of the same `(m+1)`-set and hence would
have Johnson distance one from `A_{i,h}`, a contradiction.  Thus the only
inclusions between the selected left and right families are

\[
A_{i,h}\subset B_{i,h}.
\]

The right sets are also distinct: equality of two right sets would make
their distinct left sets two `m`-subsets of one `(m+1)`-set, again at
Johnson distance one.  This proves item 1.

Equation (3.3) is immediate.  Since

\[
a(X)=t|X\cap Z|,
\]

the upper inequality in (3.5) is immediate, while

\[
|X\cap Z|\ge b-(n-|X|)
\]

gives the lower inequality.

Every flag counted by `g(T)` has its added label in `T`.  Each of the `b`
possible added labels occurs on exactly `t` flags, so

\[
g(T)\le t|T\cap Z|\le t\min(j,b),
\]

proving (3.7).  A fixed flag contributes to (3.6) for exactly

\[
\binom m{j-1}
\]

sets `T`: choose the other `j-1` elements from its lower `m`-set.  Sum
over the `tb` flags to obtain (3.8).

Subtracting the covered difference `g(T)` from the full-layer difference
`D_j` gives (3.9).

Finally, the induced inclusion graph is a union of isolated edges, so it
contains no alternating path with two left vertices and two right
vertices.  Theorem 2.2 proves item 5.  ∎

For the proportional parameters \(b=\lfloor m^{3/4}\rfloor\) and any polynomially
bounded `t`, condition (3.1) holds for all sufficiently large `m`.
More generally it holds throughout a much larger subexponential range.
For example,

\[
\binom{2m}{m}
=\prod_{i=1}^{m}\frac{m+i}{i}
\ge 2^m,
\]

whereas the left side of (3.1) is polynomial under the stated
specialization.  No asymptotic estimate is needed in the theorem itself.

The vector in (3.3) is integrally decomposable into `t` copies of the
same `b`-set `Z`; it lies at a particularly simple integral point of the
hypersimplex.  Thus the failure is not fractional or divisibility-based.
It is exactly the absence of interval seams.

## 4. The exact seam ledger after central alternating augmentation

Let `M` be an atom matching and let \(J\subseteq M\) be the packet of old
atoms touched by selected augmenting paths in `G_m`.  Put

\[
j=|J|,
\qquad t=j+1.
\]

The central exchange deletes some old matching flags and adds one more
flag on each selected augmenting path.  Its resulting inclusion matching
has `tb` edges.

### Lemma 4.1 — the old packet vertices are all retained

The vertex set of the resulting `tb`-edge central matching consists of
all `2jb` central vertices of the atoms in `J`, together with exactly `b`
previously unmatched vertices on each side of `G_m`.

#### Proof

On an alternating augmenting path, every endpoint of a deleted old
matching edge is incident with one of the new matching edges on that same
path.  The path has one more new edge than old edge.  The selected paths
are vertex-disjoint.  Retaining all untouched flags of the atoms in `J`
therefore keeps every old packet vertex and adds one new left endpoint and
one new right endpoint per path.  There are `b` selected paths.  ∎

Let \(\mathcal L'\), \(\mathcal R'\) denote these final central vertex families,
and let

\[
H'=G_m[\mathcal L',\mathcal R'].
\]

All original central path incidences of every atom in `J` remain edges of
`H'`, irrespective of how the final inclusion matching re-pairs their
vertices.  They form `j` disjoint fresh paths and contribute exactly

\[
j(2b-1)
\tag{4.1}
\]

known incidences.

### Corollary 4.2 — exact new-seam requirement

If the enlarged central resource pair is realizable by `j+1` atoms, then
some spanning fresh path factor uses at least

\[
\boxed{2b-1}
\tag{4.2}
\]

incidences outside the union of the `j` original atom paths.

#### Proof

A `(j+1)`-atom path factor contains `(j+1)(2b-1)` distinct edges.  At
most `j(2b-1)` of them can belong to the old path union.  Subtraction
gives (4.2).  ∎

There is a second useful formulation if one insists on using the final
`tb`-edge inclusion matching `P'` as the vertical edges of the new rows.
Make a directed graph on the edges of `P'` by putting

\[
(L,R)\longrightarrow(L',R')
\quad\Longleftrightarrow\quad
L'\subset R\text{ and }L'\ne L.
\tag{4.3}
\]

A decomposition using `P'` vertically needs `t` disjoint directed paths
of `b` vertices and therefore needs `t(b-1)=tb-t` transition arcs.  If
`Gamma(P')` is the bipartite source-target version of (4.3), then a
necessary Hall inequality is

\[
\boxed{
\nu(\Gamma(P'))\ge tb-t,}
\tag{4.4}
\]

or equivalently

\[
\boxed{
\max_{X\subseteq P'}
\bigl(|X|-|N^+(X)|\bigr)\le t.}
\tag{4.5}
\]

Equations (4.4)--(4.5) are necessary only for the fixed-vertical-pairing
route.  The canonical statement allowing arbitrary re-pairing is Theorem
2.2.  In either formulation, minimizing the number of deleted old flags
proves no positive lower bound on the number of required seam incidences.

Indeed, a fixed-vertical path factor uses `t(b-1)` transition arcs.  The
union of all natural seam incidences in the `j` old rows has only
`j(b-1)` edges.  Therefore such a factor must use at least

\[
t(b-1)-j(b-1)=b-1
\tag{4.6}
\]

transition arcs outside the old natural seam set.  This lower bound is
independent of how few old vertical flags the shortest augmenting paths
delete.

## 5. Every perfect `Q` admits a bad shortest-path choice

The preceding construction did not require its diagonal matching to
extend to a perfect matching of `G_m`.  The next theorem gives a literal
shortest-augmenting-path obstruction inside every perfect matching.

### Theorem 5.1 — uniform shortest-`Q` obstruction

Let `Q` be any perfect matching of `G_m`.  Form a graph `C_Q` on the `W`
edges of `Q`, joining distinct

\[
e=(L,R),
\qquad f=(L',R')
\]

when

\[
L\subset R'
\quad\text{or}\quad
L'\subset R.
\tag{5.1}
\]

Then

\[
\Delta(C_Q)\le2m.
\tag{5.2}
\]

Consequently `C_Q` has an independent set of size at least

\[
\left\lceil\frac{W}{2m+1}\right\rceil.
\tag{5.3}
\]

For all sufficiently large `m`, this is larger than

\[
b=\lfloor m^{3/4}\rfloor.
\]

If the current atom matching is empty, one may therefore choose `b` of
the shortest `Q`-augmenting paths such that their `b` lower endpoints and
`b` upper endpoints induce exactly `b` isolated inclusion edges.  Those
central resources are not the central projection of one tight atom.

#### Proof

Fix `e=(L,R)` in `Q`.  The upper set `R` has `m+1` lower neighbors.  One
is `L`; its other `m` lower neighbors are each the lower endpoint of a
unique edge of `Q`.  Hence at most `m` other `Q`-edges satisfy
\(L'\subset R\).

Likewise `L` has `m+1` upper neighbors.  One is `R`; each of the other
`m` upper neighbors is the upper endpoint of a unique edge of `Q`.
Hence at most `m` other `Q`-edges satisfy \(L\subset R'\).  This proves
(5.2).

A greedy independent-set construction in a graph of maximum degree
`2m` selects at least \(\lceil W/(2m+1)\rceil\) vertices, proving (5.3).
Also

\[
W=\binom{2m+1}{m}\ge\binom{2m}{m}\ge2^m,
\]

so (5.3) exceeds \(\lfloor m^{3/4}\rfloor\) for all sufficiently large
`m`.

Against the empty matching, `Q` itself is the disjoint union of `W`
augmenting paths, each consisting of one `Q`-edge and containing zero old
edges.  Thus all have the minimum possible length.  Choose `b` edges from
the independent set.  Independence under (5.1) says that no lower
endpoint of one selected edge is contained in the upper endpoint of
another.  Therefore the full induced inclusion graph on the selected
endpoints is exactly the selected matching of `b` edges.  For \(b\ge2\) it
violates (2.10), which would require at least `2b-1` edges.  ∎

This theorem is not defeated by choosing `Q` strategically: the bad tied
choice exists for every `Q`.  It is, however, defeated in principle by
choosing the tied paths strategically as well.  The theorem therefore
rules out an implication from “the `b` shortest paths” unless the path
selection includes an additional seam-aware condition.

At the empty matching, the global residual contains all other middle
vertices and of course contains full atoms.  Theorem 5.1 is therefore not
a counterexample to the unrestricted augmentation condition (Lift),
which may ignore the displayed path endpoints and choose an atom
elsewhere.  It is an exact counterexample to an **endpoint-preserving
resegmentation** of the central matching delivered by the selected
shortest paths.  This distinction is also why the theorem does not rule
out a larger state-graph augmentation.

## 6. Reversal, boundary fibres, and the exact surviving route

Word reversal does not remove the obstruction.  Reversing an atom still
gives an alternating path in the undirected induced inclusion graph.  A
diagonal graph consisting of isolated edges has no such path in either
orientation.

The boundary fibres from
`PROPORTIONAL_TIGHT_ATOM_MATCHING_EXPANSION_20260725.md` do carry the
missing structure.  For each fixed boundary type and core, the central
targets come with their actual fresh path (1.3), and the off-central
targets are fixed at the same time.  Hence an unblocked boundary-fibre
atom automatically passes the central path-factor test.  This explains
precisely why the fibre expansion condition (FE) is stronger than the
ordinary central matching conclusion.

A larger alternating state graph could also evade the obstruction, but
its states must remember enough information to enforce (2.3)--(2.4) and
must synchronize the off-central targets.  An alternating path in `G_m`
alone remembers neither.

## 7. Proved boundary

### Proved

1. The canonical pairing-independent central lift condition is a fresh
   `(b,b)` path factor in the induced middle-incidence graph.
2. The exact edge-count obstruction is \(|E(H)|\ge2tb-t\).
3. The central endpoint hypersimplex and all central star-moment bounds do
   not imply even one seam; Theorem 3.1 gives exact integral
   counterexamples.
4. For every perfect middle matching `Q`, there is a valid choice of `b`
   tied shortest augmenting paths from the empty matching which fails the
   endpoint-preserving central resegmentation.
5. The shortest-path deletion ledger and the new-seam ledger are distinct:
   bounding the former gives no lower bound for the latter.

### Not proved

1. No theorem here rules out a deliberately seam-aware joint choice of
   `Q` and the `b` augmenting paths.
2. A fresh central path factor is not sufficient for a full proportional
   atom matching: off-central targets of different completed words may
   collide with each other or with the unreleased old matching.
3. The cylinder-fibre expansion condition (FE), and hence the
   proportional tight-atom matching lemma and constant one, remain
   unproved.

Thus the endpoint-preserving resegmentation of the present
`b`-shortest-path conclusion is closed: its conclusion is strictly weaker
than central tight-row realizability.  An unrestricted packet lift could
ignore those endpoints, and remains open.  A viable positive route must
build augmentations in a seam-aware partial-word or boundary-fibre state
space from the outset.
