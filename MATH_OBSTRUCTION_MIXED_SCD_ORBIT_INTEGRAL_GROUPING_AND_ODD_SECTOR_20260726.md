# Mixed-SCD orbit incidence does not round: a cyclic lattice obstruction and a macroscopic odd sector

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Verdict

The complete coordinate-conjugacy orbit has the exact endpoint
biregularity and empty-rectangle expansion proved in the mixed-SCD theorem,
but those facts do **not** imply an integral owner-disjoint SCD or path
resolution.

There are two exact obstructions.

1. In the full labelled coordinate orbit of one SCD of \(B_3\), there is a
   \(C_3\)-invariant subcatalogue in which every Boolean vertex has degree
   three, the constant vector \(1/3\) is an exact fractional SCD, and every
   rank projection has normalized Hall with equality. Nevertheless the
   all-rank chain-incidence system has no integral solution. Its Smith
   obstruction is a literal \(\mathbb Z/3\mathbb Z\) character.

2. In the middle Johnson layer, a fixed coordinate triple partitions the
   fraction \(3m/(2(2m-1))\) of all owners into disjoint Johnson triangles. The
   owner-to-edge-option incidence on every triangle is a biregular \(C_6\)
   and has an exact fractional factor, but every owner-disjoint atomic-path
   packing leaves one vertex per triangle. The resulting leave is

   \[
   2\binom{2m-3}{m-1}
   ={m\over2(2m-1)}\binom{2m}{m}
   =\left({1\over4}+o(1)\right)W.                    \tag{0.1}
   \]

The second construction is the ordinary odd-set/blossom obstruction. It
uses only Johnson edges in the full coordinate orbit of one Johnson edge.
The first construction shows that replacing paths by complete symmetric
chains does not remove the integral problem: it moves to the joint
all-rank lattice.

The full **unfiltered** orbit has a trivial exact integral resolution: every
single colour \(\pi\mathscr D\) is already an SCD. The obstructions below
concern history/type-filtered subcatalogues. They do not say that the actual
queue-safe mixed-SCD catalogue has such a cut. They prove the sharp logical
boundary: no group-design or nibble theorem for a filtered catalogue can be
deduced from the presently proved biregular orbit marginals alone. A
positive theorem must additionally control owner conflicts and the joint
all-rank lattice, or prove that the physical queue-safe options cross every
such odd/lattice sector.

## 1. A base SCD and its labelled orbit

Write \(123=\{1,2,3\}\), and similarly for smaller sets. Consider

\[
\begin{array}{rcl}
L_{12}&:&\varnothing\subset1\subset12\subset123,\\
R_{2,23}&:&2\subset23,\\
R_{3,13}&:&3\subset13 .
\end{array}                                                     \tag{1.1}
\]

These are saturated, symmetric, disjoint, and contain all eight vertices
of \(B_3\). Thus (1.1) is an SCD \(\mathscr D\). Retain every
\(\pi\in S_3\) as a label on the conjugate \(\pi\mathscr D\).

For distinct \(a,b,c\), put

\[
L_{a,b}:\quad
\varnothing\subset a\subset ab\subset123.                       \tag{1.2}
\]

There is exactly one labelled occurrence of \(L_{a,b}\): the conjugating
permutation is forced by
\(\pi(1)=a,\pi(2)=b,\pi(3)=c\).

For an incidence \(a\subset ab\), put

\[
R_{a,ab}:\quad a\subset ab.                                     \tag{1.3}
\]

There are exactly two labelled occurrences of (1.3). One comes from
\(2\subset23\), with \(\pi(2)=a,\pi(3)=b\); the other comes from
\(3\subset13\), with \(\pi(3)=a,\pi(1)=b\). The remaining image is forced.
Thus all columns below are literal occurrences in the complete labelled
coordinate orbit.

### Proposition 1.1 (the unrestricted orbit is integrally resolvable)

The multiset of all labelled orbit occurrences has the exact resolution

\[
\{\pi\mathscr D:\pi\in S_3\}.                                  \tag{1.4}
\]

More generally, for any SCD \(\mathscr E\) of \(B_n\), the labelled
coordinate orbit resolves into the \(n!\) SCD colours
\(\pi\mathscr E\), \(\pi\in S_n\).
Likewise, any functorial product-path construction made from a fixed tuple
of SCD colours is already an integral path partition for that global colour
tuple. The difficulty starts only when occurrences from different tuples
are mixed after a state-dependent filter.

#### Proof

For each fixed label \(\pi\), the chains of \(\pi\mathscr E\) partition
\(B_n\). Distinct labels are retained as distinct copies, so sorting all
labelled occurrences by \(\pi\) is the asserted resolution. \(\square\)

Thus the issue is not integrality of the unfiltered orbit. It is whether a
history-dependent subcatalogue, after its endpoint projections have passed
the empty-rectangle tests, still contains a mixed integral resolution.

### Lemma 1.2 (exact two-colour component rigidity)

Let \(\mathcal P,\mathcal Q\) be any two partitions of a finite resource set
\(V\). Form their bipartite overlap multigraph \(\Gamma\): its left vertices
are blocks of \(\mathcal P\), its right vertices are blocks of
\(\mathcal Q\), and every \(v\in V\) is an edge joining its two containing
blocks.

Every exact cover of \(V\) by whole blocks from
\(\mathcal P\cup\mathcal Q\) is obtained by independently choosing, on each
connected component of \(\Gamma\), either all \(\mathcal P\)-blocks or all
\(\mathcal Q\)-blocks. In particular, if \(\Gamma\) is connected, the only
two exact covers are \(\mathcal P\) and \(\mathcal Q\).

#### Proof

Give a selected block value one and an unselected block value zero. For the
edge \(v=PQ\), exact coverage says

\[
                              x_P+x_Q=1.                         \tag{1.5}
\]

Thus values alternate across every edge. On a connected bipartite
component, all left values equal one common bit and all right values equal
its complement. Both choices work, proving the lemma. \(\square\)

The fractional assignment \(x_B=1/2\) always satisfies (1.5), irrespective
of component size. Hence even for two genuine global SCD colours,
fractional averaging says nothing about the number of independently
choosable integral regions. The three-colour catalogue below shows that
passing to one more colour can introduce a lattice obstruction rather than
remove integrality.

## 2. The cyclic mixed catalogue

Use cyclic indices modulo three and define

\[
\begin{array}{lll}
u_1=1,&u_2=2,&u_3=3,\\
v_1=12,&v_2=23,&v_3=13 .
\end{array}                                                     \tag{2.1}
\]

Retain

\[
\begin{array}{lll}
L_1=L_{1,2},&L_2=L_{2,3},&L_3=L_{3,1},\\
S_1=R_{1,13},&S_2=R_{2,12},&S_3=R_{3,23}.
\end{array}                                                     \tag{2.2}
\]

For every \(S_i\), retain both labelled occurrences and denote them by
\(S_i^0,S_i^1\). The coordinate cycle \((1\,2\,3)\) permutes the three
long columns and the three pairs of short columns, so this is a
\(C_3\)-invariant subcatalogue. Its incidence pattern is

\[
\begin{split}
L_i&=\{\varnothing,u_i,v_i,123\},\\
S_i^\epsilon&=\{u_i,v_{i-1}\},
\qquad \epsilon\in\{0,1\}.
\end{split}                                                     \tag{2.3}
\]

### Proposition 2.1 (exact regularity and fractional cover)

Every vertex of \(B_3\) belongs to exactly three labelled columns in
(2.3). Consequently

\[
                         x_C={1\over3}                           \tag{2.4}
\]

for every retained labelled occurrence \(C\) is an exact fractional chain
partition of \(B_3\).

#### Proof

The vertices \(\varnothing,123\) belong to \(L_1,L_2,L_3\). A singleton
\(u_i\) belongs to \(L_i,S_i^0,S_i^1\). A doubleton \(v_i\) belongs to
\(L_i,S_{i+1}^0,S_{i+1}^1\). Thus every row degree is three, and summing
\(1/3\) over incident columns gives one in every row. \(\square\)

### Proposition 2.2 (every rank projection has zero Hall deficiency)

For \(r=0,1,2,3\), form the bipartite incidence graph between rank-\(r\)
vertices and retained labelled chains which cross rank \(r\). For every
family \(\mathcal F\) of rank-\(r\) vertices,

\[
 {|\Gamma(\mathcal F)|\over|\mathcal C_r|}
 ={|\mathcal F|\over|B_3(r)|}.                                 \tag{2.5}
\]

#### Proof

At ranks zero and three there is one left vertex and three right
occurrences. At ranks one and two there are three left vertices and nine
right occurrences. Each right occurrence contains exactly one vertex of
the displayed rank, each left vertex has degree three, and option sets of
distinct left vertices are disjoint. Hence
\(|\Gamma(\mathcal F)|=3|\mathcal F|\), proving (2.5). \(\square\)

Thus exact degree regularity, fractional balance, and the strongest
possible normalized Hall statement in every separate resource--column
rank projection all hold. This is formally analogous to, but not identical
with, the history--active-alphabet Kneser projection in the dynamic
empty-rectangle theorem.

One scope distinction is useful. In this \(B_3\) example every long chain
has the same unordered active alphabet \(\{1,2,3\}\). Therefore a
conservative support filter

\[
                       A(C)\cap Z=\varnothing                   \tag{2.6}
\]

either retains all six long orders or retains none. It cannot itself retain
exactly the three cyclic long orders in (2.2). The displayed obstruction can
arise only after an order/age/type restriction is imposed in addition to
unordered active-alphabet avoidance. Consequently Theorem 3.1 is an
obstruction to rounding from orbit marginals, not a counterexample to the
specific conservative Kneser graph.

## 3. The exact \(\mathbb Z/3\mathbb Z\) obstruction

### Theorem 3.1 (no integral mixed SCD)

No pairwise vertex-disjoint selection of the retained labelled occurrences
covers \(B_3\).

#### Proof

Let \(\ell_i\) be the selected multiplicity of \(L_i\), and put

\[
s_i=x_{S_i^0}+x_{S_i^1}.                                       \tag{3.1}
\]

The bottom vertex, the row \(u_i\), and the row \(v_i\), respectively, give

\[
\ell_1+\ell_2+\ell_3=1,                                        \tag{3.2}
\]

\[
\ell_i+s_i=1,                                                   \tag{3.3}
\]

\[
\ell_i+s_{i+1}=1.                                               \tag{3.4}
\]

Comparing (3.4) at \(i\) with (3.3) at \(i+1\) gives
\(\ell_i=\ell_{i+1}\). Hence all three \(\ell_i\)'s are equal, contradicting
(3.2) over the integers. Over the reals the unique aggregated solution is
\(\ell_i=1/3,s_i=2/3\), exactly (2.4). \(\square\)

There is a literal Smith character. Give the vertices the following
weights modulo three:

\[
\begin{array}{c|cccccccc}
Z&\varnothing&123&u_1&u_2&u_3&v_1&v_2&v_3\\ \hline
\chi(Z)&1&0&0&1&2&2&1&0 .
\end{array}                                                     \tag{3.5}
\]

Every retained chain has total \(\chi\)-weight zero:

\[
\chi(L_1)=1+0+0+2,\quad
\chi(L_2)=1+0+1+1,\quad
\chi(L_3)=1+0+2+0,                                              \tag{3.6}
\]

and the short types have weights \(0+0,1+2,2+1\). On the other hand,

\[
\sum_{Z\in B_3}\chi(Z)=1\pmod3.                                 \tag{3.7}
\]

Therefore the all-one row vector is not in the integer lattice generated
by the retained orbit columns. This is stronger than semigroup
nonnormality: no absorber or multiplicity can repair one copy without
changing the column set or deleting vertices.

### Corollary 3.2 (arbitrarily large Boolean dimensions)

For every \(t\ge0\) there is an SCD \(\mathscr D_{2t+3}\) of
\(B_{2t+3}\) and a subcatalogue of its full labelled coordinate orbit with
an exact fractional chain partition but no integral chain partition.

#### Proof

Take an SCD \(\mathscr E\) of \(B_{2t}\). It has

\[
c_t=\binom{2t}{t}-\binom{2t}{t-1}
={1\over t+1}\binom{2t}{t}                                     \tag{3.8}
\]

singleton chains at rank \(t\). Form the Cartesian product of
\(\mathscr E\) with (1.1), and symmetrically decompose every product of
chains. When the \(\mathscr E\)-factor is a singleton \(\{Y\}\), retain
the three chains \(Y\cup C\), \(C\in\mathscr D\); they are already symmetric
in \(B_{2t+3}\).

Fix one such \(Y\). Keep the identity-colour chains disjoint from

\[
\mathcal Q_Y=\{Y\cup Z:Z\subseteq[3]\},                          \tag{3.9}
\]

and on \(\mathcal Q_Y\) allow only the nine labelled columns of Section 2,
translated by \(Y\). They lie in the coordinate orbit under permutations
of the final three coordinates. Exclude every other orbit chain meeting
\(\mathcal Q_Y\).

The identity chains outside \(\mathcal Q_Y\), with coefficient one, and
the nine translated columns, with coefficient \(1/3\), form an exact
fractional cover. Any integral cover would restrict on \(\mathcal Q_Y\)
to Theorem 3.1's impossible cover. \(\square\)

The replacement may be made simultaneously on all \(c_t\) singleton
product cells. Even an approximate packing leaves at least two vertices
in every copy: without a long chain the three short types cover at most
six vertices, while after choosing one long chain at most one short type
is disjoint from it. Thus the leave is at least \(2c_t\). If
\(W_{2t+3}=\binom{2t+3}{t+1}\), then exactly

\[
{2c_t\over W_{2t+3}}
={t+2\over(2t+1)(2t+3)}
=\left({1\over2(2t+3)}+o(t^{-1})\right).                        \tag{3.10}
\]

This is a genuine asymptotic lattice obstruction of scale
\(\Theta(W/m)\). At \(H=\sqrt m\log\log m\) it is below \(W/H\), so it is
a no-go for the proposed deduction from biregularity, not a coefficient-one
no-go for the full physical catalogue.

## 4. A macroscopic odd-set obstruction for atomic path options

Let

\[
\Omega_m=\binom{[2m]}m,\qquad W=|\Omega_m|,                     \tag{4.1}
\]

and fix \(B=\{1,2,3\}\), with \(R=[2m]\setminus B\). For every
\(Y\in\binom R{m-1}\), define

\[
\mathcal T_Y^{(1)}
=\{Y\cup\{1\},Y\cup\{2\},Y\cup\{3\}\}.                         \tag{4.2}
\]

For every \(Y\in\binom R{m-2}\), define

\[
\mathcal T_Y^{(2)}
=\{Y\cup(B\setminus\{1\}),
Y\cup(B\setminus\{2\}),
Y\cup(B\setminus\{3\})\}.                                      \tag{4.3}
\]

Any two vertices in one triple are Johnson adjacent. The triples are
pairwise disjoint and exhaust the owners \(X\) with
\(|X\cap B|\in\{1,2\}\). Retain the three Johnson edges inside every
triangle as atomic path options. Every option lies in the full
coordinate-conjugacy orbit of one Johnson edge.

### Theorem 4.1 (exact blossom deficit)

On

\[
\Omega_B^\circ=\{X\in\Omega_m:|X\cap B|\in\{1,2\}\},            \tag{4.4}
\]

the owner-to-option incidence is a disjoint union of biregular \(C_6\)'s.
It has the exact fractional cover \(x_e=1/2\), and its bipartite
owner-to-option projection has zero Hall deficiency. Nevertheless every
integral owner-disjoint atomic-path packing leaves at least

\[
2\binom{2m-3}{m-1}                                             \tag{4.5}
\]

owners.

#### Proof

Inside one triangle, every owner is incident with two edge options and
every edge has two owners. Its owner-option incidence graph is \(C_6\).
Giving all three edges weight \(1/2\) covers every owner once. The
bipartite incidence cycle itself has a perfect matching, so its local Hall
deficiency is zero.

An integral owner-disjoint selection is a matching in the triangle and
contains at most one edge. Hence it leaves at least one owner. The number
of triangles is

\[
\binom{2m-3}{m-1}+\binom{2m-3}{m-2}
=2\binom{2m-3}{m-1},                                           \tag{4.6}
\]

which proves (4.5). \(\square\)

The exact active-mass and leave ratios are

\[
{|\Omega_B^\circ|\over W}
={6\binom{2m-3}{m-1}\over\binom{2m}m}
={3m\over2(2m-1)},                                             \tag{4.7}
\]

\[
{2\binom{2m-3}{m-1}\over W}
={m\over2(2m-1)}.                                              \tag{4.8}
\]

For each triangle \(\mathcal T\), an integral matching obeys the blossom
inequality

\[
\sum_{e\subseteq\mathcal T}x_e\le1,                             \tag{4.9}
\]

whereas the fractional degree equations force the left side to be \(3/2\).

This is a typed subcatalogue, not a claim that an unrestricted queue state
forbids every edge leaving \(B\). Its role is exact: an argument which sees
only biregular owner-option incidence cannot distinguish the full orbit
from this macroscopic odd sector.

### Proposition 4.2 (small support avoidance cannot isolate the triangles)

Fix \(X\in\Omega_B^\circ\) and a forbidden coordinate support
\(Z\subseteq[2m]\). Let \(a=|X\cap B|\in\{1,2\}\), and put

\[
z_-=\bigl|Z\cap(X\setminus B)\bigr|,
\qquad
z_+=\bigl|Z\cap(X^c\setminus B)\bigr|.                          \tag{4.10}
\]

The number of Johnson seams from \(X\) whose support avoids \(Z\), and whose
other endpoint lies outside \(X\)'s triangle, is at least

\[
\boxed{(m-a-z_-)\bigl(m-(3-a)-z_+\bigr).}                       \tag{4.11}
\]

In particular, if \(|Z|\le H\le m-4\), this number is at least

\[
                         (m-H-3)^2,                             \tag{4.12}
\]

and it is \((1-o(1))m^2\) when \(H=o(m)\).

#### Proof

Choose a removal coordinate

\[
r\in X\setminus(B\cup Z)
\]

and an insertion coordinate

\[
s\in X^c\setminus(B\cup Z).
\]

There are exactly the two factors in (4.11) choices. The Johnson edge

\[
                         X\longleftrightarrow X-r+s             \tag{4.13}
\]

has support \(\{r,s\}\) disjoint from \(Z\). It does not change the
\(B\)-part of \(X\), but it changes the outside core, so its other endpoint
is not one of the other two vertices in (4.2) or (4.3). Distinct ordered
pairs \((r,s)\) give distinct neighbors. This proves (4.11).

By the two-sided residence criterion, disjointness of the new support pair
from the live support \(Z\) is simultaneously conservative-safe for the
lower and upper signs.

Both factors in (4.11) are at least \(m-3-|Z|\), giving (4.12). \(\square\)

Thus the macroscopic triangle obstruction cannot be the complete seam graph
created by an \(O(H)\)-support avoidance rule in the regime \(H=o(m)\).
The actual conservative safe family has polynomially many transverse
cross-sector seams at every triangle owner. What remains nontrivial is to
select those crossing seams together with whole SCD paths without creating
new owner conflicts or violating the joint rank lattice.

### Proposition 4.3 (a common forbidden support has only cheap parity leave)

Fix one common forbidden support \(Z\subseteq[2m]\), \(|Z|=s\), for every
owner, and retain **all** Johnson edges whose support avoids \(Z\). This
safe graph has an atomic-path matching leaving at most

\[
                              2^s                               \tag{4.14}
\]

owners. Consequently, if \(s\le H=o(m)\), then its parity leave is
\(2^H=W^{o(1)}=o(W/H)\).

#### Proof

An allowed edge never changes \(X\cap Z\). Conversely, after fixing
\(P=X\cap Z\), every one-for-one exchange outside \(Z\) is allowed. Hence
the component indexed by \(P\subseteq Z\) is

\[
J(2m-s,m-|P|),                                                  \tag{4.15}
\]

when the displayed rank is feasible. There are at most \(2^s\) nonempty
components.

For completeness, every Johnson graph \(J(N,k)\) has a Hamilton path.
List the \(k\)-subsets recursively by

\[
\mathcal G(N,k)=
\mathcal G(N-1,k)\ \Vert\
\bigl(N+\operatorname{rev}\mathcal G(N-1,k-1)\bigr),            \tag{4.16}
\]

with the unique lists at \(k=0,N\). Inductively the first and last members
are

\[
\{1,\ldots,k\},
\qquad
\{1,\ldots,k-1,N\}.                                             \tag{4.17}
\]

The last member of the first block in (4.16) is
\(\{1,\ldots,k-1,N-1\}\), while the first member of the second block is

\[
\{1,\ldots,k-2,N-1,N\};
\]

they differ by one exchange. All other consecutive pairs are adjacent by
induction, proving the Hamilton-path assertion. When \(k=1\), the displayed
bridge is simply \(\{N-1\},\{N\}\); this is the same one-exchange check.

Taking alternate edges of a Hamilton path matches every vertex except
possibly one. Apply this separately to the at most \(2^s\) components in
(4.15), proving (4.14). Finally

\[
\log(2^H H)=O(H+\log m)=o(m),
\qquad
\log W=(2\log2)m+O(\log m),
\]

so \(2^H=o(W/H)\). \(\square\)

Thus a common queue support has no coefficient-scale blossom obstruction.
Any physical odd-set obstruction must use owner-dependent histories, or
whole-path/intermediate-owner conflicts which are invisible in the atomic
seam graph.

## 5. The missing condition in a positive theorem

Let \(A\) be the physical-resource incidence matrix of the permitted mixed
chain or path columns. The dynamic empty-rectangle theorem controls
particular endpoint projections \(P_rA\). Sections 2--4 show that even

* normalized Hall for every separately typed endpoint projection;
* exact regular degrees;
* an exact fractional solution \(Ax=\mathbf1\); and
* membership of every column in one coordinate-conjugacy orbit

do not imply an integral solution.

For clarity, the conclusion applies to arbitrary history/type-filtered
subcatalogues. Proposition 1.1 gives an integral resolution before
filtering, while Proposition 4.2 proves that the particular triangle filter
is not generated by small unordered support avoidance. A future positive
theorem may exploit precisely this extra crossing structure; it cannot use
biregularity alone.

At minimum, a theorem for the **actual queue-safe** columns must prove:

1. **Joint lattice primitivity.** For every modulus \(d\ge2\) and every
   resource character \(\chi\) for which every allowed full column has
   \(\chi\)-sum zero modulo \(d\), the demanded resource vector has the
   same congruence. Character (3.5) shows this is not formal from symmetry.

2. **Owner-conflict odd-set expansion.** In every graph projection in
   which a selected path consumes two owner ports, all blossom inequalities
   must hold after the permitted \(o(W/H)\) leave. Endpoint Hall does not
   imply this; (4.9) is the smallest witness.

For longer columns these are only the first members of the full hypergraph
matching dual and lattice. A nibble addresses concentration and codegrees
only after these deterministic barriers are excluded.

## 6. Audited boundary

Proved:

* a literal \(C_3\)-symmetric subcatalogue of the complete labelled SCD
  orbit with exact fractional balance and perfect separate-rank Hall;
* a \(\mathbb Z/3\mathbb Z\) character excluding integral SCD grouping;
* an embedding into arbitrarily large odd Boolean dimensions;
* a macroscopic Johnson-triangle blossom obstruction with exact counts; and
* the precise extra lattice and owner-conflict conditions missing from the
  endpoint empty-rectangle theorem.

Also proved:

* the full unrestricted orbit is trivially resolvable into its global SCD
  colours; and
* neither displayed obstruction is forced by conservative
  \(O(H)\)-support avoidance: the \(B_3\) filter distinguishes equal-support
  orders, while every triangle owner has at least \((m-H-3)^2\) safe seams
  leaving its triangle.

Not proved:

* that the actual coherent-route queue filter realizes either subcatalogue;
* that the unrestricted full mixed-SCD orbit has an odd or lattice deficit;
* that a filter-specific absorber cannot cross these sectors; or
* coefficient one.

The next positive target is a theorem that physical queue-safe options cross
every odd owner sector and generate a primitive joint all-rank lattice,
followed by a codegree estimate for the resulting conflict hypergraph.
