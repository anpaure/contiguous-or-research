# The first-exit boundary diamond and the sharp depth barrier for folded cross conversion

**Date:** 2026-08-03  
**Status:** unconditional native value-and-phase converter for the
codimension-one cross type, and a sharp support/depth no-go for bounded
cap-preserving Hasse/diamond converters of the full folded-\(C_8\) type.
The general protected fan host remains conditional. No computation is used.

## 0. Result

Let \(R_i\subset V_i\) be a first-exit pair and let
\(h_i\) be its exit distance. At every upper-run boundary
\(R_i\ne R_{i+1}\), one has \(h_i=2\), and four already existing interval
occurrences form the exact rectangle

\[
\begin{array}{ccc}
&&v_i=[i,i+d+2]\\
&q_i=[i,i+d+1]&&q_{i+1}=[i+1,i+d+2]\\
&&o_{i+1}=[i+1,i+d+1].
\end{array}
\tag{0.1}
\]

Their Boolean values form the diamond

\[
\begin{array}{ccc}
&&V_i=R_i\cup R_{i+1}\\
&R_i&&R_{i+1}\\
&&T_{i+1}=R_i\cap R_{i+1}.
\end{array}
\tag{0.2}
\]

Thus the nested first-exit terminal pair \((q_i,v_i)\) converts to the
incomparable pair \((q_i,q_{i+1})\), preserving the cap value \(V_i\),
using no new word position and no new interval address. Since each q1
upper occurrence is present in either q1 phase record, the two middle
addresses may be given opposite phase tags. Protected use still requires
one common cap state to admit those phase-labelled records and their
guards.

This is the smallest possible Boolean converter: one diamond, four values,
two terminal cells, and threshold requirement two. It converts a folded
cross ticket exactly only when both arms are coatoms of their cap. For the
canonical ticket

\[
 P=C\cup F[1,j],\qquad S=C\cup F[j+1,d],\qquad
 V=C\cup F[1,d],
\tag{0.3}
\]

the cap deficits are

\[
 |V-P|=d-j,\qquad |V-S|=j.
\tag{0.4}
\]

Hence a one-diamond conversion exists if and only if
\(d=2,j=1\).

More generally, every cap-preserving Hasse/diamond fan producing
\((P,S)\) has at least

\[
 \boxed{d\text{ Hasse edges and }d+1\text{ distinct Boolean values}.}
\tag{0.5}
\]

Its longest cap-to-terminal branch has length

\[
 \ell_j=\max\{j,d-j\}.
\tag{0.6}
\]

If the native first-exit coatom \(R=V-\{x\}\) is to be reused, the sharp
local value condition is

\[
 x\in(P\triangle S)=V-C.
\tag{0.7}
\]

Then one arm lies below \(R\), and a minimal fan needs exactly \(d-1\)
additional addressed values beyond \(R,V\). If \(x\in C\), neither arm is
below \(R\), so the native nested edge is not on a minimal fan and \(d\)
additional values are needed beyond the cap.

Consequently no \(O(1)\)-support cap-preserving Hasse/diamond converter
exists as \(d\to\infty\). In a serial first-exit realization which exposes
one Hasse level per exit-distance unit, ticket \(j\) has the sharp
threshold requirement

\[
 \boxed{a_j=1+\max\{j,d-j\}.}
\tag{0.8}
\]

Thus the missing converter cannot automatically have requirement two,
except in the codimension-one case.

## 1. The native boundary diamond

Suppose \(R_i\ne R_{i+1}\). The upper run containing \(i\) ends at \(i\),
so the first owner outside \(R_i\) is \(T_{i+2}\), and \(h_i=2\). The
first-exit definitions give

\[
 w_i=[i,i+d+1]=q_i,\qquad
 v_i=[i,i+d+2].
\tag{1.1}
\]

The next native q1 upper cell and intervening owner are

\[
 q_{i+1}=[i+1,i+d+2],\qquad
 o_{i+1}=[i+1,i+d+1].
\tag{1.2}
\]

As address sets,

\[
 q_i\cap q_{i+1}=o_{i+1},\qquad
 q_i\cup q_{i+1}=v_i.
\tag{1.3}
\]

Their values are \(R_i,R_{i+1},T_{i+1},V_i\). Both upper values contain
the rank-\(r\) owner \(T_{i+1}\). They are distinct rank-\((r+1)\) sets,
so their intersection is exactly \(T_{i+1}\). Their union has rank
\(r+2\) and equals the first-exit cap \(V_i\). This proves (0.2).

The middle addresses are distinct and incomparable: \(q_i\) contains the
left endpoint \(i\), while \(q_{i+1}\) contains the right endpoint
\(i+d+2\). The conversion consumes those two unit-capacity terminal cells;
\(o_{i+1}\) and \(v_i\) are the bottom and cap certificates.

Both q1 phase records contain the q1 upper address at their seam. Therefore
one may use \(q_i\) with phase zero and \(q_{i+1}\) with phase one, or the
reverse, without identifying the two physical cells. This is a raw
opposite-phase occurrence statement. It does not by itself prove
background compatibility, common-cap product closure, or guard
admissibility.

### Capacity of the native socket bank

Let \(E_\partial=\{i:R_i\ne R_{i+1}\}\), and form the subgraph of the
cycle on q1 addresses whose edge at \(i\) is \(q_iq_{i+1}\). Selecting
native converters with disjoint terminal cells is exactly selecting a
matching in this graph.

If the upper word has \(J\) maximal constant runs, then
\(|E_\partial|=J\). A subgraph of a cycle with \(J\) edges has a matching
of size at least \(\lfloor J/2\rfloor\). Upper surjectivity gives

\[
 J\ge\binom{2r-1}{r+1}
 ={r-1\over r+1}W.
\tag{1.4}
\]

Hence the raw native converter bank contains at least

\[
 \left\lfloor {r-1\over2(r+1)}W\right\rfloor
\tag{1.5}
\]

pairwise terminal-disjoint sockets. Named cap, core, phase, and guard
acceptance remain explicit filters. After fixing any terminal-disjoint
socket matching \(M_\partial\), the exact deficiency for a logical ticket
set \(I\) is the ordinary Hall value

\[
 \delta=\max_{X\subseteq I}
 \bigl(|X|-|N_{M_\partial}(X)|\bigr)_+.
\tag{1.6}
\]

## 2. Sharp one-diamond criterion

Let \(P,S\) be incomparable and \(P\cup S=V\). They are the two middle
vertices of a Boolean Hasse diamond with top \(V\) if and only if

\[
 |V-P|=|V-S|=1.
\tag{2.1}
\]

Necessity is the definition of a Hasse diamond. Conversely, under (2.1),
\(P\cap S\) has rank \(|V|-2\), and

\[
 P\cap S\lessdot P,S\lessdot V
\]

is the required diamond.

For (0.3), equation (2.1) is \(d-j=j=1\), equivalently \(d=2,j=1\).
Thus the native boundary diamond is an exact folded converter only in this
case. For \(d>2\), its equal-coatom cross type is not the canonical folded
ticket.

## 3. Minimal cap-preserving fan

Consider any Hasse circuit which contains a descending path from \(V\) to
\(P\) and another from \(V\) to \(S\). Their lengths are at least
\(|V-P|=d-j\) and \(|V-S|=j\), with equality for saturated paths.

The two paths cannot share a vertex below \(V\). Indeed, a shared vertex
\(U\) must contain both terminals, hence

\[
 U\supseteq P\cup S=V,
\]

so \(U=V\). Therefore the two branches are internally vertex-disjoint.
They contain at least

\[
 (d-j+1)+(j+1)-1=d+1
\]

vertices and \(d\) edges in total. Choosing arbitrary deletion orders on
the two arms attains these numbers, proving (0.5).

Let \(R=V-\{x\}\) be the native first-exit coatom. A terminal, say \(P\),
lies below \(R\) exactly when \(x\notin P\). Since
\(P\cap S=C\) and \(P\cup S=V\), at least one arm lies below \(R\) exactly
when \(x\notin C\), which is (0.7). In that case choose the saturated path
to that arm with first edge \(V\gtrdot R\); the lower bound is attained
with \(R,V\) as the two native values and \(d-1\) further fan vertices.
If \(x\in C\), both terminals contain \(x\), so neither branch can pass
through \(R\).

The longest branch has length (0.6). In a serial host where distance two
exposes one cap-to-coatom edge and every extra exit-distance unit exposes
one further Hasse level, a fan exists only if

\[
 h_i\ge1+\ell_j.
\tag{3.1}
\]

A host supplying private addressed occurrences at every level of the two
saturated branches, with opposite phase tags on their terminal addresses
and a common cap anchor, attains (3.1). This proves the sharp conditional
threshold (0.8). The native first-exit theorem alone supplies no such
value-changing fan beyond the boundary diamond.

## 4. Exact threshold demand of the folded bank

There are two canonical tickets for every \(1\le j<d\), one for each
folded base. Under the serial fan condition, both have requirement
\(a_j=1+\max(j,d-j)\). Put

\[
 A(t)=|\{\text{folded tickets }x:a_x\ge t\}|.
\]

Then

\[
 A(t)=
\begin{cases}
 2(d-1),&
 2\le t\le1+\lceil d/2\rceil,\\
 4(d-t+1),&
 1+\lceil d/2\rceil<t\le d,\\
 0,&t\ge d+1.
\end{cases}
\tag{4.1}
\]

Indeed, for \(m=t-1>\lceil d/2\rceil\), the indices failing
\(\max(j,d-j)\ge m\) are

\[
 d-m<j<m,
\]

of which there are \(2m-d-1\). Thus one folded base has
\((d-1)-(2m-d-1)=2(d-m)\) surviving indices, and the two bases give
\(4(d-m)=4(d-t+1)\).

If a protected private fan host has threshold acceptance
\(x\sim i\) exactly when \(h_i\ge a_x\), after deleting unavailable seams
\(Z\), the exact terminal deficiency is therefore

\[
 \boxed{
 \delta=
 \max_{t\ge2}\bigl(A(t)-H_Z(t)\bigr)_+,
 }
\tag{4.2}
\]

with \(A(t)\) given by (4.1). This is the exact Hall/min-cut accounting
conditional on the private fan host. The first-exit geometry supplies the
histogram \(H_Z\), but upper surjectivity gives no lower bound on its
long-exit tail.

## 5. Consequence

The value-and-phase problem has a complete sharp boundary.

* At a run boundary, the native four-cell interval diamond gives a
  zero-length-charge, opposite-phase, cap-preserving converter for the
  codimension-one cross type.
* A general folded-\(C_8\) ticket has total cap deficit \(d\). Any
  cap-preserving Hasse/diamond converter has support and serial threshold
  growing linearly with \(d\); no bounded protected converter of this type
  exists.
* A general positive theorem must plant the \(d+1\)-vertex private fan and
  pass the threshold cuts (4.2), or abandon this conversion architecture
  for the pivot/direct-literal branch.

This is a no-go for bounded Hasse/diamond conversion, not for arbitrary
nonlocal compiler recoding.
