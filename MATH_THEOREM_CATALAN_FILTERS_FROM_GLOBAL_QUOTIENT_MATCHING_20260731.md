# Catalan filters can be chosen from a global quotient matching

Date: 2026-07-31  
Status: exact theorem; removes the residual-palette Hall gate for the
existential construction.  It does **not** assert that every previously
prescribed complement-paired filter extends.

## 1. The diamond graph is a bipartite Kneser graph

Let \(|\Omega|=2m\), put \(k=m-1\), and let

\[
\mathcal L=\binom{\Omega}{k},\qquad
\mathcal U=\binom{\Omega}{k+2}.
\]

The lower--upper diamond graph \(\mathcal B_m\) has shores
\(\mathcal L,\mathcal U\), with \(L\sim U\) iff \(L\subset U\).
Both shores have size \(\binom{2m}{m-1}\), and every vertex has degree

\[
\Delta=\binom{m+1}{2}.                                      \tag{1}
\]

After identifying \(U\in\mathcal U\) with
\(U^c\in\binom{\Omega}{k}\), adjacency becomes disjointness.  Thus
\(\mathcal B_m\) is the bipartite double cover of
\(KG(2m,m-1)\).

## 2. Free quotient matching lemma

### Lemma 1

Let a finite group \(H\) act freely on both shores of a balanced
\(\Delta\)-regular bipartite multigraph \(G\), preserving its shores and
edges.  Then \(G\) has an \(H\)-invariant perfect matching.

#### Proof

Because the action on vertices is free, every edge orbit incident with a
fixed vertex orbit contains exactly one edge incident with each physical
vertex in that orbit.  Consequently the quotient multigraph \(G/H\) is
balanced and \(\Delta\)-regular, with degrees counted with multiplicity.
For any set \(X\) of left quotient vertices, counting its incident edges
gives

\[
\Delta |X|\le \Delta |N(X)|,
\]

so Hall's condition holds.  Lift a quotient perfect matching by taking
the complete \(H\)-orbit of every selected quotient edge.  Freeness makes
the lift a physical perfect matching. \(\square\)

## 3. Application to the three-primary Catalan filters

Write

\[
q=2m-1,\qquad s=3^{v_3(q)},\qquad h=q/s,
\]

and identify \(\Omega=\mathbb Z_q\sqcup\{\infty\}\).  The clean subgroup

\[
H=\langle s\rangle\cong\mathbb Z_h
\]

acts freely on ranks \(m-1,m,m+1\), by the theorem in
`MATH_THEOREM_CATALAN_THREE_PRIMARY_QUOTIENT_REDUCTION_20260731.md`.
Apply Lemma 1 to \(\mathcal B_m\).

### Theorem 2 (globally extendable filter selection)

There is an \(H\)-invariant perfect matching \(M\) of the complete
lower--upper diamond graph.  Therefore any \(H\)-stable distinguished
banks on the two shores can be serviced by taking the edges of \(M\)
incident with those banks, and these selected edges are extendable by
construction: their extension is \(M\) itself.

Suppose in particular that

\[
q=6a+3,\qquad m=3a+2,qquad v_3(q)=1.
\]

Let the exceptional lower bank and, after complementing the upper shore,
the exceptional upper bank be the two copies of

\[
E_A=\{\infty\}\cup\pi^{-1}(A),qquad
A\in\binom{\mathbb Z_{2a+1}}a.                           \tag{2}
\]

The restriction of \(M\) to edges incident with these two exceptional
banks has all of the following properties.

1. It contains exactly \(2\operatorname{Cat}_a\) clean-subgroup edge
   orbits: one for every exceptional quotient vertex on each shore.
2. Every exceptional lower and upper colour is serviced exactly once.
3. On each typed opposite shore, every nonexceptional colour used by a
   filter is distinct, because \(M\) is a matching.  After complement-
   identifying the two shores as one Kneser label set, a lower-family
   opposite label may equal an upper-family opposite label; no cross-family
   distinctness in that auxiliary label space is claimed.
4. The two filter families are disjoint.  In complemented coordinates an
   exceptional vertex on either shore contains \(\infty\), so two such
   vertices are not disjoint and cannot form a diamond edge.
5. Every selected clean-subgroup edge orbit occupies exactly one third of
   a free full-\(\mathbb Z_q\) edge orbit.  Hence the exceptional-filter
   restriction attains the sharp \(2\operatorname{Cat}_a\) floor.
   The completed matching may contain additional partial full-rotation
   orbits away from the exceptional banks.
6. All rank-\(m\) middle endpoints of the selected filter diamonds are
   pairwise distinct.

#### Proof of the last two assertions

An edge incident with an exceptional vertex cannot have an exceptional
vertex at its other end, by item 4.  The other endpoint is therefore free
under full rotation.  The edge orbit is free as well, so its selected
\(H\)-orbit has \(h=q/3\) of the \(q\) physical edges.  No second phase
from that full orbit can belong to \(M\): the shortened full colour orbit
also has size \(h\), and freeness makes \(H\) transitive on it, so every
phase lies over the same
exceptional colour orbit, and an additional selected phase would repeat an
already matched exceptional vertex.  Hence the intersection with the full
orbit is exactly \(h\), not merely at least \(h\).

For middle endpoints, first consider two lower-exceptional diamonds.  Two
different sets (2) differ by complete order-three cosets, so their symmetric
difference has size at least six.  Two distinct rank-\((m-1)\) sets that
are both contained in one rank-\(m\) set can differ in only one element on
each side.  Thus two lower filters cannot share a middle endpoint.  The
upper statement follows by complementation.  A lower-filter middle endpoint
contains \(\infty\), whereas an upper-filter middle endpoint does not, so
there is no cross-family collision. \(\square\)

The important point is logical: the exceptional phase sections should be
chosen **after** a quotient perfect matching, as its restriction.  Then
extension through the nonexceptional palettes is not a new theorem.

The typed-shore qualification in item 3 is necessary.  A matching may contain
both \(E_LD_R\) and \(D_LE_R\), so both filter families can display the same
complemented Kneser label \(D\) while using different physical-shore vertices.
This does not affect outer-palette exactness or the middle-endpoint argument.

At higher 3-primary valuation, the same global matching theorem remains
valid. Each shortened full colour orbit splits into \(s/3\) clean-
\(H\) quotient vertices, so the exceptional restriction contains exactly
\(2\operatorname{Cat}_a(s/3)\) clean-\(H\) edge orbits. Each such orbit is
\(1/s\) of a full edge orbit. The \(s/3\) choices belonging to one Catalan
necklace may lie in different full edge orbits; no sharp
\(2\operatorname{Cat}_a\) full-orbit packet theorem is claimed there.

The middle-endpoint privacy just proved is internal to the exceptional
restriction. A nonexceptional edge of the completing matching may reuse one
of those middle endpoints, and the full physical lift may have arbitrary
middle degrees or cycles.

## 4. What remains true for a preassigned complement-paired filter

Let \(P\) be a fixed complement-paired partial diamond matching.  Under
the disjointness identification its endpoint set is the same set
\(D\subseteq\binom{\Omega}{k}\) on both shores.  The prescribed matching
extends iff the residual bipartite graph

\[
KG(2m,m-1)^{\mathrm{bip}}[V\setminus D,V\setminus D]     \tag{3}
\]

has a perfect matching.

Equivalently, it fails iff there are cross-intersecting families
\(\mathcal A,\mathcal C\subseteq V\setminus D\) such that

\[
|\mathcal A|+|\mathcal C|>|V|-|D|.                      \tag{4}
\]

Indeed, a Hall violator \(\mathcal A\) gives
\(\mathcal C=(V\setminus D)\setminus N(\mathcal A)\), and conversely.
Condition (4) is the exact Hall obstruction for a fixed filter.

For the explicit filters of
`MATH_THEOREM_CATALAN_PERIOD3_FILTER_RECURSION_20260731.md`, the deleted
set \(D=E\sqcup F\) induces precisely a matching in the ordinary Kneser
graph.  Indeed, all \(E_A\)'s contain \(\infty\).  Further,
\(E_A\cap F_{A'}=\varnothing\) iff \(A=A'\): if a quotient coset belongs
to \(A\setminus A'\), then \(E_A\) contains all three of its points while
\(F_{A'}\) deletes at most one.  Finally, two \(F\)'s intersect because
their \((a+1)\)-element quotient supports in a \((2a+1)\)-set intersect,
and each retains at least two of the three points in any common coset.

There is also a uniform local bound.

### Lemma 3 (three-neighbour deletion bound)

Every vertex outside \(D\) has at most three neighbours in \(D\).  If it
does not contain \(\infty\), it has at most two.

#### Proof

The case \(a=0\) is a direct finite check. Assume \(a\ge1\).

A set disjoint from some \(E_A\) avoids \(\infty\).  Its \(3a+1\) finite
points occupy at least \(a+1\) quotient cosets, leaving at most one possible
\(a\)-set \(A\).  Thus it has at most one \(E\)-neighbour.

Write

\[
C_A=\Omega\setminus F_A
   =E_A\cup\{x_A,y_A\}.
\]

A vertex \(S\) is adjacent to \(F_A\) precisely when \(S\subset C_A\).
If \(\infty\notin S\), then \(S\) omits one point from the finite part of
\(C_A\).  The full and two-point quotient cosets in \(S\) recover \(A\)
uniquely, so there is at most one \(F\)-neighbour.

If \(\infty\in S\), its finite part omits two points from the finite part
of \(C_A\).  Usually the cosets occupied at least twice recover \(A\)
uniquely.  The only ambiguous pattern has \(a-1\) full cosets and three
one-point cosets; exactly one of those three can be the remaining member of
\(A\).  Hence there are at most three \(F\)-neighbours. \(\square\)

Thus the residual graph has minimum degree at least
\(\binom{m+1}{2}-3\).  This useful rigidity does not by itself prove (3):
near-regular balanced bipartite graphs can still violate Hall.  No claim
that every arbitrary choice of the pairs \(\{b_A,c_A\}\) extends is made
here.

## 5. Consequence for the all-\(k\) route

The palette-extension gate separates from the physical one as follows.

* Exact two-sided outer-colour matching, including service of every
  period-three exceptional quotient vertex, is unconditional by Theorem 2.
  At higher 3-primary valuation this is not a fixed-full-orbit packet
  coupling statement.
* What remains is to choose the quotient perfect matching so that its
  entire physical diamond lift is a spanning \(K\)-path forest; its
  nonexceptional diamonds avoid forbidden collisions at filter endpoints
  and private sockets; its mixed Pascal squares, retained incidences and
  wedge/pivot ledgers are compatible; and its endpoint closure has
  generating \(H\)-voltage and trivial residual stabilizer.

Thus a residual Kneser Hall theorem is not the missing existence lemma.
The missing condition is Hamilton-compatible **structure inside the set of
quotient perfect matchings**.
