# PBBS promotion sidecars cancel on a flagged-coatom cycle

**Date:** 2026-08-07  
**Status:** unconditional signed-support reduction, with an important
scope limitation.  A directed cycle makes every exported predecessor-q1
*target value* occur literally in another hinge.  It does not make the
owner-edge q1 palette injective: every cycle value colours two owner
edges.  Thus the construction closes named target coverage only in a
compiler that permits those duplicate edge colours.  Existence of the
required packing and the remaining owner-path completion are not asserted.

## 1. Flagged continuation coatoms

Use the odd PBBS parameters

\[
 n=2m+1,\qquad d\ge2,\qquad a=m-d-2.
\]

Let \(I\) be an index set.  For every \(i\in I\), suppose that we are
given a saturated upper flag

\[
 M_i\subset U_i=M_i\cup\{u_i\},
 \qquad |M_i|=a,
 \tag{1.1}
\]

and a rank-\((m-1)\) continuation coatom

\[
 Q_i\supset U_i.
 \tag{1.2}
\]

Assume that the \(Q_i\) are pairwise distinct.  Put

\[
 C_i:=Q_i\setminus U_i.
 \tag{1.3}
\]

Then \(|C_i|=d\), and

\[
 Q_i=M_i\mathbin{\dot\cup}\{u_i\}
       \mathbin{\dot\cup}C_i.
 \tag{1.4}
\]

Define the **flagged-coatom digraph** \(D\) on \(I\) by putting an arc
\(i\to j\), for \(i\ne j\), precisely when

\[
 Q_i\setminus\{u_i\}\subset Q_j.
 \tag{1.5}
\]

Since \(Q_i,Q_j\) have the same rank and are distinct, an arc has a
unique entering label

\[
 b_i(j)\in Q_j\setminus Q_i
 \tag{1.6}
\]

and

\[
 Q_j=(Q_i\setminus\{u_i\})\cup\{b_i(j)\}.
 \tag{1.7}
\]

Thus every arc is a directed Johnson edge whose prescribed deletion is
the distinguished flag label \(u_i\).

## 2. One arc produces one flat hinge

Fix an arc \(i\to j\), abbreviate \(b_i=b_i(j)\), and set

\[
 B_i:=C_i\cup\{b_i\}.
 \tag{2.1}
\]

Then

\[
 M_i\cup B_i=Q_j,
 \qquad
 U_i\cup C_i=Q_i,
 \tag{2.2}
\]

and

\[
 T_i:=U_i\cup B_i=Q_i\cup Q_j
 \tag{2.3}
\]

has rank \(m\).

Choose labels \(b_i^-\) and \(v_i\) outside

\[
 M_i\cup\{u_i\}\cup C_i\cup\{b_i\}
 \tag{2.4}
\]

and distinct from each other.  Put

\[
 B_i^-:=C_i\cup\{b_i^-\}.
 \tag{2.5}
\]

Finally, choose nonempty source letters

\[
 K_{i,1},\ldots,K_{i,d-1}\subseteq M_i,
 \qquad
 \bigcup_{s=1}^{d-1}K_{i,s}=M_i.
 \tag{2.6}
\]

The flat promotion source block

\[
 B_i^-,\ \{u_i\},\ K_{i,1},\ldots,K_{i,d-1},\
 B_i,\ \{v_i\}
 \tag{2.7}
\]

has three consecutive length-\((d+1)\) owner values

\[
 T_i^-:=Q_i\cup\{b_i^-\},\qquad
 T_i=Q_i\cup Q_j,\qquad
 T_i^+:=Q_j\cup\{v_i\}.
 \tag{2.8}
\]

They form a simple two-edge Johnson path.  Its two native length-\(d\)
overlaps have values

\[
 U_i
 \quad\hbox{and}\quad
 Q_j.
 \tag{2.9}
\]

The set-theoretic lower colours of the two owner edges are instead

\[
 Q_i=T_i^-\cap T_i,
 \qquad
 Q_j=T_i\cap T_i^+.
 \tag{2.10}
\]

Consequently the successor lower colour \(Q_j\) is literal in the block,
whereas the predecessor lower colour \(Q_i\) is its single exported q1
sidecar.

### Proof

Equations (2.2)--(2.3) follow from (1.4), (1.7), and the definition of
\(B_i\).  The source calculation is exactly the flat three-owner
promotion hinge: the middle \(d-1\) letters have union \(M_i\), the
left overlap is \(M_i\cup\{u_i\}=U_i\), and the right overlap is
\(M_i\cup C_i\cup\{b_i\}=Q_j\).  Formula (2.8) follows by adding the
one entering source letter on each side.  Taking intersections gives
(2.10). \(\square\)

## 3. Exact cycle cancellation

### Theorem 3.1 (sidecar-cycle cancellation)

Let \(J\subseteq I\), and suppose that \(\pi:J\to J\) is a permutation
such that

\[
 i\to\pi(i)
 \tag{3.1}
\]

is an arc of \(D\) for every \(i\in J\).  Construct the flat hinge
(2.7) from every arc \(i\to\pi(i)\).

Then the multiset of exported predecessor sidecar **values** is exactly
the multiset of literal successor lower-colour values:

\[
 \boxed{
 \{Q_i:i\in J\}
 =
 \{Q_{\pi(i)}:i\in J\}.}
 \tag{3.2}
\]

In particular, every exported named target occurs literally somewhere in
the packet bank.  However, each \(Q_i\) is the set-theoretic lower colour
of two different owner edges: the predecessor edge of hinge \(i\) and the
successor edge of hinge \(\pi^{-1}(i)\).  Therefore the packet bank has
\(|J|\) duplicate q1 edge colours.  It is not a q1-rainbow factor, and a
one-copy edge-palette architecture must price those duplicates.

If, in addition, the undirected Johnson edges

\[
 \{Q_i,Q_{\pi(i)}\}
 \tag{3.3}
\]

have pairwise distinct unions, then the middle owners

\[
 T_i=Q_i\cup Q_{\pi(i)}
 \tag{3.4}
\]

are pairwise distinct.

#### Proof

By (2.10), hinge \(i\) exports precisely \(Q_i\) and literally supplies
precisely \(Q_{\pi(i)}\).  A permutation preserves the multiset of
vertices, proving (3.2).  Equation (2.3) identifies the middle owner with
the union colour of (3.3), so rainbow union colours give distinct owners.
\(\square\)

### Corollary 3.2 (cycles of length at least three)

Suppose \(Q_0,Q_1,\ldots,Q_{h-1}\) is a directed cycle in the rank-
\((m-1)\) Johnson graph, indexed cyclically, and for every \(i\) there is
an eligible flag \((M_i,u_i)\) such that

\[
 u_i=Q_i\setminus Q_{i+1},
 \qquad
 M_i\subseteq Q_i\cap Q_{i+1},
 \qquad |M_i|=m-d-2.
 \tag{3.5}
\]

If the edge unions \(Q_i\cup Q_{i+1}\) are distinct, the corresponding
hinges have zero uncovered predecessor-q1 target values and distinct
middle owners.  They still have one duplicated q1 edge colour per hinge.

The exclusion of two-cycles is substantive: the two orientations of one
Johnson edge have the same rank-\(m\) union and would duplicate the middle
owner.  A simple cycle of length at least three avoids that immediate
degeneracy, although nonadjacent union repetitions must still be excluded.

### Corollary 3.3 (explicit promotion triangle)

Choose

\[
 R\in{[n]\choose m-2}
\]

and three distinct labels \(x,y,z\notin R\).  Put

\[
 Q_x=R\cup\{x\},\qquad
 Q_y=R\cup\{y\},\qquad
 Q_z=R\cup\{z\}.
 \tag{3.6}
\]

Choose three distinct \(d\)-subsets \(C_x,C_y,C_z\subset R\), and set

\[
 M_s=R\setminus C_s,qquad U_s=M_s\cup\{s\}
 \quad(s\in\{x,y,z\}).
 \tag{3.7}
\]

Then the directed triangle

\[
 x\longrightarrow y\longrightarrow z\longrightarrow x
 \tag{3.8}
\]

in the flagged-coatom graph gives three flat promotion hinges with:

* pairwise distinct lower flag targets \(M_s,U_s\);
* zero uncovered predecessor-q1 target values, but three duplicated
  q1 edge colours;
* three distinct literal q1 colours \(Q_x,Q_y,Q_z\); and
* three distinct middle owners

  \[
  R\cup\{x,y\},\qquad
  R\cup\{y,z\},\qquad
  R\cup\{z,x\}.
  \tag{3.9}
  \]

If a common \((d-1)\)-set

\[
 A\subseteq R\setminus(C_x\cup C_y\cup C_z)
 \tag{3.10}
\]

is available, put

\[
 K_s=R\setminus(A\cup C_s),\qquad G=R\setminus A.
 \tag{3.11}
\]

Then

\[
 M_s=K_s\mathbin{\dot\cup}A,qquad
 G=K_s\mathbin{\dot\cup}C_s
 \tag{3.12}
\]

for all three hinges.  Hence all three have the same *candidate* permanent
rail core \(G\).  This is only a common-core interface; it does not by
itself interlace the three literal collars in one chronology.

#### Proof

For the vertex \(s\), the distinguished deletion is \(s\), and the next
coatom in (3.8) is obtained by replacing \(s\) by the next triangle
label.  Thus (1.5) holds.  Distinctness of the \(C_s\) gives distinct
\(M_s\); the labels \(s\) then give distinct \(U_s\).  The sidecar and
owner statements follow from Theorem 3.1.  Equations (3.11)--(3.12) are
set differences inside \(R\). \(\square\)

The optional common-core condition (3.10) is easy locally whenever
\(R\setminus(C_x\cup C_y\cup C_z)\) has at least \(d-1\) elements.  It
does not assert that positive-density triangles can be placed in one
literal rail chronology.

## 4. What this changes globally

### Lemma 4.1 (central endpoint-hole bound)

Let a word of length \(W+d\) contain all \(W\) rank-\(m\) targets, and
choose one witnessing interval for each such target.  Then every chosen
interval has length at most \(d+1\), and the chosen intervals use \(W\)
distinct right endpoints.  Consequently there are only \(d\) unused
right endpoints.

In particular, if the union of the last \(d+1\) letters ending at a
position \(e\) has rank less than \(m\), no selected rank-\(m\) witness
can end at \(e\).  There can be at most \(d\) distinct positions of this
kind.

#### Proof

Distinct rank-\(m\) target values are incomparable.  Hence their selected
witness intervals are noncontaining.  Order them by their left endpoints:

\[
 a_1<\cdots<a_W.
\]

Their right endpoints are then also strictly increasing,

\[
 b_1<\cdots<b_W.
\]

Since \(a_i\ge i\) and the \(i\)-th member of a \(W\)-subset of
\([W+d]\) is at most \(d+i\),

\[
 b_i-a_i+1\le(d+i)-i+1=d+1.
\]

There are \(W+d\) possible right endpoints and the selected witnesses use
\(W\) of them.  Finally, every interval of length at most \(d+1\) ending
at \(e\) is contained in the final length-\((d+1)\) interval ending
there.  If the latter has rank below \(m\), so does the former. \(\square\)

The split one-longer refinement makes one sidecar literal at the cost of
a rank-\((m-1)\) length-\((d+1)\) central-row hole.  At physical length
\(W+d\), the selected rank-\(m\) witness antichain has only \(d\) unused
right endpoints by Lemma 4.1.  Thus a bank of distinct split occurrences
has size at most \(d\), and cannot serve a \(\Theta(W)\)-sized flag bank.

The flat packet (2.7) has no such central-row hole.  Theorem 3.1 shows
that its sidecar target values can be recycled on a flagged-coatom cycle
cover.  It does not remove the duplicate-q1 incidence current.

Accordingly the next global selector is the following concrete object.

> **Flagged-coatom rainbow cycle-packing problem.**  From the eligible
> rephased PBBS flags, choose the required bank and distinct continuation
> coatoms \(Q_i\supset U_i\) so that the flagged digraph (1.5) contains a
> cycle cover with no two-cycles and with all edge-union colours distinct.

After this selector is found, the remaining resources are the duplicate
q1 edge current, the outer owners \(T_i^-,T_i^+\), residence collars,
upper witnesses, and the background common-cap matching.  The predecessor
target values are covered, but the occurrence-labelled palette is not
closed.

This theorem does not prove the cycle packing, the physical path-factor
completion, the common-cap row, \(\nu(k)\le B(k)+O(1)\), or exact
equality.
