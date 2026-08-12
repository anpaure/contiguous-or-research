# Audit of the three-top/two-base promotion conveyor

Date: 2026-07-27

## 0. Verdict

The complete-frame conveyor in the three-top/two-base promotion note is
mathematically valid. Its exact direct-deck derivative is

\[
 \Delta_h=d_h(\omega;x,y)+d_h(\omega';x,y),
\]

so

\[
 \Delta_h=0\quad(1\le h\le H),
\qquad
 |\operatorname{supp}\Delta_{H+q}|=
 \|\Delta_{H+q}\|_2^2=16q
\quad(1\le q\le H).
\]

Both shores have the same squarefree set of \(3M\) middle owners, and
the floor self-toll cancellation is exact.

Two qualifications are needed.

1. At the opposite-side endpoint \(q=H\), the cited identity
   \(\Delta_{H-q}=0\) would read \(\Delta_0=0\), outside the deck
   notation. The claim is nevertheless true separately: the direct
   rank-\(M\) deck consists only of the unchanged top, once on both
   shores.
2. Complementation of the two path edges occurs inside different tops.
   It is valid because of the common-core identity in Lemma 2.1 below,
   not merely because one may “complement inside the virtual endpoint
   top.”

The ordered-core verdict has two different scopes.

* The conveyor fixes the order induced on its own common
  \((M-2)\)-core \(C\).
* Its three tops form a triangle in the Johnson graph, whereas every
  maximal Boolean top cell is bipartite.  Thus it can never be supported
  wholly inside one such cell.
* In the global one-top-at-every-root table, the third top can act as an
  exterior catalyst.  Choosing a cell core which contains one endpoint
  placeholder makes the conveyor genuinely change that cell's
  ordered-core histogram.

So the maximal-face invariant remains an exact obstruction on the
isolated face, but the conveyor is a literal bounded-support
core-reordering catalyst once cross-face tops are available.

There is also a positive density result. The abstract
three-top supports form a regular 3-uniform hypergraph with negligible
pair codegree and hence admit an almost-perfect top matching. Thus
top-disjoint core-changing conveyor supports are dense. This does not
control overlap of their \(3M\) middle owners or their all-depth target
supports.

## 1. Endpoint telescope and literal support

For a core context \(K\subseteq C\), write

\[
 g_K(u,v)=e_{K\cup\{v\}}-e_{K\cup\{u\}}.
\]

Every term in the placeholder derivative is of this form, with a sign
determined by whether it lies at \(A\) or \(B\). Consequently

\[
 g_K(x,a)+g_K(a,y)=g_K(x,y)
\tag{1.1}
\]

phase by phase. This proves the three-top telescope without any
separate phase choices.

For \(h\le H\), the \(A\)-contexts of \(\omega'\) are exactly the
\(B\)-contexts of \(\omega\), and conversely. Their signs are opposite,
so the derivative vanishes.

At \(h=H+q\), cancellation remains exactly on
\(q\le t\le H-1\). The boundary set has \(2q\) indices. For each
index there are four signed context families:

\[
 A_\omega,\ B_\omega,\ A_{\omega'},\ B_{\omega'}.
\]

The inner arm type and the number of predecessor labels recover the
family and \(t\); the two copies of a fixed inner type enter disjoint
outer collars. Hence all \(8q\) core contexts are distinct. Each
contributes \(g_K(x,y)\), whose two coordinates are also distinct from
all others. Thus there are exactly \(8q\) positive and \(8q\) negative
coordinates.

A literal enumeration at \((H,M)=(2,16)\) and \((3,24)\) independently
reproduces support/norm values \(16q\), zero derivatives through \(H\),
and squarefree equal middle decks of sizes \(3M\).

## 2. Complementation across different tops

### Lemma 2.1 (common-core complement transport)

For \(K\subseteq C\) and the top \(U_{uv}=C\cup\{u,v\}\),
complementation inside \(U_{uv}\) sends

\[
 g_K(u,v)\longmapsto-g_{C\setminus K}(u,v).
\tag{2.1}
\]

Therefore it commutes with the endpoint telescope:

\[
 \mathcal C_{xa}g_K(x,a)+\mathcal C_{ay}g_K(a,y)
 =\mathcal C_{xy}g_K(x,y).
\tag{2.2}
\]

#### Proof

\[
 U_{uv}\setminus(K\cup\{v\})=(C\setminus K)\cup\{u\},
\quad
 U_{uv}\setminus(K\cup\{u\})=(C\setminus K)\cup\{v\}.
\]

This proves (2.1), and (2.2) is (1.1) with the common context
\(C\setminus K\) and an overall minus sign. \(\square\)

This lemma rigorously justifies every complementary derivative in the
conveyor theorem even though its three frames live on different tops.
It also shows that there is no hidden choice of a different phase on
the two path edges.

For \(1\le q<H\), complementing the \(H+q\) derivative gives the direct
rank-\((m-q)\) derivative, and complementing the zero
\((H-q)\)-derivative gives the zero direct rank-\((m+q)\) derivative.
At \(q=H\), the latter is zero because every complete frame has the same
single rank-\(M\) top target on both shores. Global complementation in
\([2m]\) gives the two root-form assertions.

## 3. Middle support and floor identity

The middle-squarefreeness proof is sound. A common middle owner on two
different packet tops must lie in their intersection. Equivalently,
the complementary \(H\)-window on each top contains its exclusive
placeholder. At each shared endpoint this compares an \(A\)-context
with a \(B\)-context of the same base after the prescribed inner-arm
interchange. Those context families use disjoint arms. The same
argument survives reversal of all placeholder roles on the new shore.

Lemma 2.1 and \(\Delta_H=0\) give equality of the aggregate middle
decks. Since both are squarefree, they have literally the same support
of \(3M\) owners.

The coordinate involution \(x\leftrightarrow y\), \(a\mapsto a\),
\(C\) fixed, maps the old three-frame load to the new one. Therefore
their squared norms agree in every layer. If
\(\Delta=\Gamma^1-\Gamma^0\), then

\[
 2\langle\Gamma^0,\Delta\rangle+\|\Delta\|_2^2=0.
\]

Substitution into the integer floor-energy expansion leaves exactly
\(\langle R,\Delta\rangle\). No baseline or quadratic term is hidden.

The fresh-frame descent witness is also valid under \(M\ge8H\): the
ambient complement of \(C\cup\{x,a,y\}\) has \(m-H-1\) labels, while
the witness needs \(H+q\le2H\). Its \(H+1\) fresh \(Z\)-labels force
every middle window to use \(Z\), but exactly one rank-\((m-q)\) window
avoids \(Z\).

## 4. Exact ordered-core boundary

For a top \(U_i\), let

\[
 \operatorname{ord}_C(\pi)
\]

be the cyclic order induced on the common core \(C\) after deleting the
two placeholders. On each of the three tops separately, the old and
new frames use the same positional base:

\[
\begin{array}{c|c|c}
U_0&\omega^+(x,y)&\omega^-(x,y)\\
U_1&(\omega')^+(x,a)&(\omega')^-(x,a)\\
U_2&(\omega')^+(a,y)&(\omega')^-(a,y).
\end{array}
\]

Only the two labels in the placeholder positions are interchanged.
Every label of \(C\) remains in its literal old position. Hence

\[
 \boxed{
 \operatorname{ord}_C(\pi_i^{\rm old})
 =\operatorname{ord}_C(\pi_i^{\rm new})
 \quad(i=0,1,2).}
\tag{4.1}
\]

Thus every ordered-core histogram induced by a subset of the packet's
own common core is fixed.

### Proposition 4.1 (a packet cannot be internal to a Boolean cell)

The three packet tops form a triangle: every pair intersects in
\(M-1\) labels.  The top graph of a maximal Boolean cell is a hypercube,
and is therefore bipartite.  Consequently no maximal Boolean cell
contains all three packet tops.

In particular, the packet cannot be applied to a table on the isolated
cell face, because its top margin is zero at the necessary third,
exterior top.  The ordered-core invariant theorem for that face remains
valid.

### Proposition 4.2 (one exterior top changes an ordered core)

In the global table, fix the packet endpoint \(x\).  Choose a
\(2H\)-set

\[
 D\subseteq C\cup\{x\},\qquad x\in D,
\]

with asymmetric anchor labels from \(C\) around the two placeholder
positions, and with \(y\notin D\).  There is a maximal Boolean cell with
fixed core \(D\) containing \(U_0=C\cup\{x,y\}\): pair every label of
\(U_0\setminus D\) with a distinct label of \([2m]\setminus U_0\).

The top \(U_1=C\cup\{x,a\}\) also lies in this cell after choosing the
pair containing \(y\) to be \(\{y,a\}\), while
\(U_2=C\cup\{a,y\}\) does not contain \(x\) and lies outside the cell.
On \(U_0\), the move sends \(x\) from placeholder position \(A\) to
position \(B\); on \(U_1\) it makes the analogous swap in \(\omega'\).
After deleting labels outside \(D\), the asymmetric anchors distinguish
the two positions, so

\[
 \operatorname{ord}_D(\pi_i^{\rm old})
 \ne \operatorname{ord}_D(\pi_i^{\rm new})
 \quad(i=0,1).
\tag{4.2}
\]

Therefore the conveyor changes the cornerwise \(D\)-ordered-core
histogram, with \(U_2\) serving as one exterior catalyst.  This is an
exact statewise core-reordering move, not a counting inference.

## 5. Dense top supports, but no owner packing theorem

Ignore the frame decoration and retain only the three touched tops.
Let \(\mathcal P\) be the 3-uniform hypergraph whose vertices are
rank-\(M\) tops and whose edges are triples

\[
 C\cup\{x,y\},\quad C\cup\{x,a\},\quad C\cup\{a,y\}.
\]

Put \(s=2m-M=m-H\). Then \(\mathcal P\) is regular with

\[
 d_{\mathcal P}(U)=s\binom M2.
\tag{5.1}
\]

Indeed, choose the unique \((M+1)\)-set \(S\supset U\) in \(s\) ways
and then choose the other two \(M\)-subsets of \(S\) in
\(\binom M2\) ways.

Two distinct tops have codegree

\[
 d_{\mathcal P}(U,V)=
 \begin{cases}
 M-1,&|U\cap V|=M-1,\\
 0,&\text{otherwise}.
 \end{cases}
\tag{5.2}
\]

Thus

\[
 \frac{\Delta_2(\mathcal P)}{d_{\mathcal P}}
 =\frac{2}{sM}=o(1).
\tag{5.3}
\]

Since the uniformity here is the fixed value three, the ordinary
Pippenger--Spencer theorem applies and gives a matching covering all
but \(o(\binom{2m}M)\) top vertices. Therefore an almost-spanning
family of pairwise top-disjoint abstract conveyor supports exists.

For every support, the common core has size \(M-2\) and admits the arm
partition because \(M\ge8H\), so every selected support can be decorated
as an actual conveyor.  Proposition 4.2 then chooses a local Boolean
chart in which it is core-changing.  This produces a dense,
zero-top-overlap library of literal port-changing catalysts.

It does **not** prove that the \(3M\)-owner supports of distinct packets
are disjoint, nor that their old shores occur in a prescribed exact
frame table. Those are growing-uniformity owner-packing and charged
coverage conditions.  It also does not bound overlap of the
\(16q\)-coordinate derivatives at different packets.  Thus “bounded
overlap” is proved exactly for top variables, but not for middle owners
or all-depth load coordinates.

## 6. Final boundary

Verified:

1. the exact three-top telescope;
2. all support and norm counts \(16q\);
3. literal squarefree equality of middle support;
4. complement transport across the two path tops;
5. exact floor self-toll cancellation;
6. the fresh-frame one-depth descent witness;
7. a dense almost-perfect packing of abstract top supports.

Verified about ports:

1. the packet fixes its own common-core order;
2. it cannot occur wholly inside a maximal Boolean cell;
3. with one exterior top it changes a chosen cell's ordered-core
   histogram;
4. an almost-spanning family of these catalysts can be made
   pairwise top-disjoint.

Still open:

1. owner-disjoint packing of decorated packets;
2. favorable simultaneous all-depth charging;
3. bounded overlap on middle-owner and derivative coordinates;
4. coefficient one.
