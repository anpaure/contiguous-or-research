# Resolvable isometric \(C_{2h}\)-decomposition of \(Q_h\)

Date: 2026-07-26

Status: independent folded-quotient proof of the theorem audited in
`MATH_THEOREM_RESOLVABLE_ISOMETRIC_HYPERCUBE_CYCLES_20260726.md`.

## 0. Audited conclusion

Let \(h=2^t\) with \(t\geq 1\).  The edge set of the binary cube
\(Q_h\) has a resolution

\[
 E(Q_h)=\mathop{\dot\bigcup}_{a\in A_0}E(\mathcal R_a),
 \qquad |A_0|=h/2,
 \tag{0.1}
\]

in which every \(\mathcal R_a\) is a vertex partition into
\(2^{h-t-1}\) graph-isometric cycles of length \(2h\).  Every cycle has
the same transition-direction word

\[
 0,1,\ldots,h-1,0,1,\ldots,h-1.
 \tag{0.2}
\]

Consequently the complete decomposition contains exactly

\[
 {h\over2}\,2^{h-t-1}=2^{h-2}
 \tag{0.3}
\]

cycles, as the edge count forces.

There are two corrections to the informal ``Hamming-code theorem'' label.

1. A code-translate partition of the vertices supplies only **one**
   resolution class, not an edge decomposition.  The \(h/2\) translated
   classes in (0.1) are an additional step.
2. The code used below is not the ordinary perfect Hamming code (nor the
   ordinary extended Hamming code).  Its check columns lie in one affine
   parity hyperplane and necessarily repeat.  Thus ``Hamming-code'' is at
   best a loose description of the syndrome construction.

The assertion is false at the power \(h=1\) if cycles are simple: \(Q_1\)
has one edge and no \(C_2\).  Thus \(t\geq1\), equivalently \(h\geq2\), is
necessary.

Conversely, the power-of-two restriction is forced by resolvability.  A
vertex-partition class would contain \(2^h/(2h)\) cycles, so \(h\mid
2^{h-1}\).  Hence \(h\) has no odd prime divisor and is a power of two.
Thus, apart from the degenerate \(h=1\) case, the theorem gives the exact
arithmetic range for a resolvable \(C_{2h}\)-decomposition.

## 1. A parity-alternating syndrome cycle

Put

\[
 A=\mathbb F_2^t
\]

and choose a nonzero linear functional

\[
 \lambda:A\longrightarrow\mathbb F_2.
\]

Write \(A_0=\ker\lambda\) and choose \(z\in A\) with
\(\lambda(z)=1\).  If

\[
 A_0=\{a_0,a_1,\ldots,a_{h/2-1}\},
\]

define a cyclic listing of all elements of \(A\) by

\[
 u_{2j}=a_j,
 \qquad
 u_{2j+1}=a_j+z
 \qquad(0\leq j<h/2).
 \tag{1.1}
\]

All subscripts on the \(u_i\)'s will be read modulo \(h\).  Put

\[
 w_i=u_i+u_{i+1}\qquad(0\leq i<h).
 \tag{1.2}
\]

Then

\[
 \lambda(w_i)=1\quad\hbox{for every }i,
 \qquad
 \sum_{i=0}^{h-1}w_i=0.
 \tag{1.3}
\]

The first identity follows because consecutive terms in (1.1) have
opposite \(\lambda\)-parity, including the cyclic last-first pair.  The
second telescopes.

Let \(V=\mathbb F_2^h\), with standard basis
\(e_0,\ldots,e_{h-1}\), and define the syndrome map

\[
 \Psi:V\longrightarrow A,
 \qquad
 \Psi(e_i)=w_i.
 \tag{1.4}
\]

Let \({\bf1}=e_0+\cdots+e_{h-1}\).  By (1.3),

\[
 {\bf1}\in\ker\Psi.
 \tag{1.5}
\]

For \(0\leq i\leq h\), set

\[
 p_i=e_0+e_1+\cdots+e_{i-1};
 \qquad p_0=0,\qquad p_h={\bf1}.
 \tag{1.6}
\]

Telescoping (1.2) gives

\[
 \Psi(p_i)=\sum_{j<i}(u_j+u_{j+1})=u_0+u_i
 \qquad(0\leq i<h).
 \tag{1.7}
\]

The right sides run through all of \(A\).  Hence \(\Psi\) is surjective,
and

\[
 \dim\ker\Psi=h-t.
 \tag{1.8}
\]

Moreover,

\[
 \lambda(\Psi(x))=\sum_{i=0}^{h-1}x_i
 \quad (x\in V),
 \tag{1.9}
\]

because both sides take the value one on every basis vector.

## 2. The base isometric cycle and one vertex resolution

Let \(P\) be the cycle whose cyclic vertex list is

\[
 p_0,p_1,\ldots,p_{h-1},
 {\bf1}+p_0,{\bf1}+p_1,\ldots,{\bf1}+p_{h-1}.
 \tag{2.1}
\]

Its transition word is (0.2).  The vertices \(p_i\), \(0\leq i<h\), are
distinct.  If \(i\leq j<h\), then \(p_i+p_j\) is supported on the proper
coordinate interval \(\{i,\ldots,j-1\}\), so it cannot equal
\({\bf1}\).  Thus no \(p_i\) equals \({\bf1}+p_j\), and the \(2h\)
vertices in (2.1) are distinct.  Hence \(P\cong C_{2h}\).

### Lemma 2.1 (strong isometry)

The cycle \(P\) is an isometric subgraph of \(Q_h\).

#### Proof

Let two cycle vertices have cyclic distance \(r\leq h\).  The corresponding
shorter arc uses \(r\) consecutive terms of the periodic transition word
(0.2).  Every block of at most \(h\) consecutive terms contains no repeated
direction.  The endpoints therefore differ in exactly \(r\) coordinates,
so their distance in \(Q_h\) is \(r\), equal to their distance on the
cycle.  This holds for every pair of cycle vertices.  \(\square\)

By (1.5) and (1.7), the two vertices \(p_i\) and
\({\bf1}+p_i\) have the same syndrome, and these are exactly the two
vertices of \(P\) with syndrome \(u_0+u_i\).  Thus \(P\) meets every fibre
of \(\Psi\) in one antipodal pair.

Choose a linear complement \(K_0\) to \(\langle{\bf1}\rangle\) in
\(\ker\Psi\):

\[
 \ker\Psi=K_0\oplus\langle{\bf1}\rangle.
 \tag{2.2}
\]

Then

\[
 |K_0|=2^{h-t-1}.
 \tag{2.3}
\]

### Lemma 2.2 (one resolution class)

The cycles

\[
 \mathcal R_0=\{P+k:k\in K_0\}
 \tag{2.4}
\]

partition \(V(Q_h)\).

#### Proof

Suppose \(x+k=y+k'\), where \(x,y\in V(P)\) and
\(k,k'\in K_0\).  Applying \(\Psi\) shows that \(x,y\) have the same
syndrome.  By the preceding paragraph, either \(x=y\) or
\(x=y+{\bf1}\).  Accordingly, \(k+k'\) is either zero or \({\bf1}\).
The direct sum (2.2) forces the first alternative and \(k=k'\).  Hence the
cycles are vertex-disjoint.  Their total number of vertices is

\[
 |K_0|\,2h=2^{h-t-1}2^{t+1}=2^h,
\]

so they cover the cube.  \(\square\)

## 3. The full set of resolution classes

For each \(a\in A\), choose any \(r_a\in V\) satisfying

\[
 \Psi(r_a)=a.
 \tag{3.1}
\]

Define

\[
 \boxed{\displaystyle
 \mathcal R_a=\{P+r_a+k:k\in K_0\}.}
 \tag{3.2}
\]

Changing \(r_a\) by an element of \(\ker\Psi\) only permutes the cycles
in (3.2) (translation by \({\bf1}\) fixes the vertex set of \(P\)).
Lemma 2.2, after translation by \(r_a\), proves that every
\(\mathcal R_a\) is a vertex partition and hence a spanning \(2\)-factor.

It remains to prove that the \(h/2\) factors indexed by \(A_0\) partition
the edges.

Fix a coordinate direction \(i\).  In \(P\), the two direction-\(i\)
edges have initial vertices \(p_i\) and \({\bf1}+p_i\).  Therefore all
direction-\(i\) edges in \(\mathcal R_a\) have their distinguished initial
vertices in

\[
 p_i+r_a+K_0+\{0,{\bf1}\}
 =p_i+r_a+\ker\Psi
 =\Psi^{-1}(u_0+u_i+a).
 \tag{3.3}
\]

As \(a\) runs through \(A_0\), the fibres in (3.3) run through all
syndromes in the affine hyperplane

\[
 u_0+u_i+A_0.
 \tag{3.4}
\]

On the other hand, traversing a direction-\(i\) edge adds
\(w_i\) to the syndrome, and \(\lambda(w_i)=1\).  Hence every undirected
direction-\(i\) edge has exactly one endpoint whose syndrome lies in
(3.4).  Formula (3.3) therefore selects every direction-\(i\) edge exactly
once as \(a\) ranges over \(A_0\).  This is true independently for every
\(i\), proving (0.1).

The variation of the classes is therefore completely explicit: cycles
inside one class differ by translations in \(K_0\), while distinct classes
differ by translations whose \(\Psi\)-syndromes run through \(A_0\).
More generally, for either affine half \(b+A_0\) of \(A\), the family
\(\{\mathcal R_a:a\in b+A_0\}\) is a resolution by the same proof; in
(3.4), one merely replaces \(A_0\) by \(b+A_0\).  Thus the \(h\) syndrome
translates of the base \(2\)-factor split naturally into two full
resolutions, either one of which proves the theorem.  Different
parity-alternating cyclic listings \(u_0,\ldots,u_{h-1}\) give further
syndrome maps and hence further resolutions, while leaving the transition
word (0.2) unchanged.

## 4. Exact ledgers and the edge/vertex distinction

There are

\[
 |A_0|=2^{t-1}=h/2
\]

resolution classes.  Each contains

\[
 |K_0|=2^{h-t-1}={2^h\over2h}
\]

cycles, exactly the number required to partition the \(2^h\) vertices.
Thus the complete decomposition has

\[
 {h\over2}{2^h\over2h}=2^{h-2}
\]

cycles.  Multiplication by \(2h\) gives

\[
 2^{h-2}(2h)=h2^{h-1}=|E(Q_h)|.
\]

So the precise hierarchy is:

* one member of \(\mathcal R_a\) is a graph-isometric \(C_{2h}\);
* one \(\mathcal R_a\) is a vertex partition, equivalently a spanning
  \(2\)-factor;
* the \(h/2\) classes \(\mathcal R_a\) partition all cube edges.

## 5. Why the ordinary Hamming-code slogan is insufficient

The perfect binary Hamming code of length \(h-1\) has a parity-check matrix
whose columns are the distinct nonzero elements of \(\mathbb F_2^t\).
That fact by itself neither produces (3.2) nor partitions the cube edges.
The present proof instead requires

\[
 \lambda(\Psi(e_i))=1\quad\hbox{for all }i,
 \tag{5.1}
\]

because (5.1) makes one affine syndrome half a canonical choice of one
endpoint from every edge in every direction.  There are only \(h/2\)
vectors in \(\lambda^{-1}(1)\), whereas there are \(h\) coordinate
directions, so the check columns \(w_i\) necessarily repeat.  In
particular this is not a Hamming parity-check matrix.

The power-of-two input is used exactly to make the quotient syndrome set
have size \(h\), so that the \(h\) antipodal pairs of one \(C_{2h}\) form
a complete syndrome transversal.  The parity-alternating cyclic ordering
(1.1), rather than perfect-code minimum distance, is the decisive
resolvability property.
