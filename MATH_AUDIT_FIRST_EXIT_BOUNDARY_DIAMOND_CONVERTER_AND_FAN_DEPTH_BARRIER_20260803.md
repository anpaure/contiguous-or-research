# Independent audit: first-exit boundary converter and fan-depth barrier

**Date:** 2026-08-03  
**Audited theorem:**  
MATH_THEOREM_FIRST_EXIT_BOUNDARY_DIAMOND_CONVERTER_AND_FAN_DEPTH_BARRIER_20260803.md  
**Theorem SHA256:**  
0524a427210c5e8c92b6ff550a8f88025a57fb5cbf390b4d7f68a028efd41412

**Verdict:** PASS in its stated Hasse/diamond scope. The native converter
is exact only for the codimension-one folded type. General folded tickets
require support and exit threshold growing with \(d\).

## 1. Native interval rectangle

At an upper-run boundary \(R_i\ne R_{i+1}\), \(T_{i+2}\) cannot remain
inside \(R_i\); otherwise the two distinct facets \(T_{i+1},T_{i+2}\)
would have union \(R_i\), forcing \(R_{i+1}=R_i\). Hence \(h_i=2\).

The four interval addresses are

\[
 q_i=[i,i+d+1],\quad q_{i+1}=[i+1,i+d+2],
\]

\[
 o_{i+1}=[i+1,i+d+1],\quad v_i=[i,i+d+2].
\]

They satisfy

\[
 q_i\cap q_{i+1}=o_{i+1},\qquad
 q_i\cup q_{i+1}=v_i.
\]

Their OR values are \(R_i,R_{i+1},T_{i+1},V_i\). The two distinct
rank-\((r+1)\) upper values both contain \(T_{i+1}\), so their intersection
is exactly \(T_{i+1}\); their union is the rank-\((r+2)\) first-exit cap.
Thus the address and value diamonds agree literally.

No new address or source position is introduced. The two terminal q1
addresses are distinct. Their opposite phase tags are available at the raw
q1-record level, but protected simultaneous use remains conditional on one
cap/guard/background state, as stated.

## 2. Native socket capacity

Boundary converters correspond to edges \(q_iq_{i+1}\) in the transition
subgraph of a cycle. Terminal-disjoint converters are exactly a matching.
If there are \(J\) constant upper runs, there are \(J\) boundary edges.
Every subgraph of a cycle with \(J\) edges has matching number at least
\(\lfloor J/2\rfloor\). Upper surjectivity gives

\[
 J\ge\binom{2r-1}{r+1}={r-1\over r+1}W.
\]

The raw socket lower bound follows. After a disjoint socket matching is
fixed, named type acceptance is an ordinary ticket-to-socket bipartite
graph, with the displayed Hall deficiency. No unproved type acceptance is
deduced from the count.

## 3. One-diamond criterion

Two incomparable sets \(P,S\) with union \(V\) are middle vertices of one
Boolean Hasse diamond exactly when both are coatoms of \(V\). For the
folded ticket,

\[
 |V-P|=d-j,\qquad |V-S|=j.
\]

Both deficits equal one exactly for \(d=2,j=1\). Thus the theorem correctly
does not identify the native equal-coatom diamond with a general folded
ticket.

## 4. Fan support lower bound

Any descending Hasse path from \(V\) to \(P\) has at least \(d-j\) edges;
one to \(S\) has at least \(j\). A vertex shared below \(V\) would contain
both terminals and therefore their union \(V\), an impossibility. The
branches share only \(V\).

Consequently their union contains at least

\[
 (d-j+1)+(j+1)-1=d+1
\]

vertices and \(d\) edges. Two saturated deletion chains attain equality.
The longest branch has length \(\max(j,d-j)\).

For \(R=V-\{x\}\), one terminal is below \(R\) exactly when \(x\) lies in
the other terminal's exclusive arm. This occurs exactly when
\(x\notin P\cap S=C\). Hence the reuse condition
\(x\in V-C=P\triangle S\) is necessary and sufficient. Reusing \(R,V\)
leaves exactly \(d-1\) further fan vertices to expose; if \(x\in C\), the
native coatom lies on neither branch.

This proves the claimed no-go for bounded-support cap-preserving
Hasse/diamond conversion as \(d\to\infty\). It is deliberately not a
no-go for arbitrary nonlocal compiler recoding.

## 5. Serial threshold and demand histogram

Under the explicitly stated serial host convention—distance two exposes
the first coatom level and every additional distance unit exposes one
further Hasse level—the sharp requirement is

\[
 a_j=1+\max(j,d-j).
\]

For two tickets at every \(j=1,\ldots,d-1\), all tickets survive thresholds
through \(1+\lceil d/2\rceil\). Above that, writing \(m=t-1\), one folded
base has \(2(d-m)\) indices with \(\max(j,d-j)\ge m\), so both bases give

\[
 A(t)=4(d-t+1).
\]

The piecewise formula in the theorem is exact. Substitution into the
already proved threshold-Hall theorem gives

\[
 \delta=\max_t(A(t)-H_Z(t))_+.
\]

This remains conditional on a private addressed fan host; first-exit
geometry alone does not supply the value-changing internal vertices or a
lower bound on long-exit supply.

## 6. Final scope

Certified:

1. a zero-length-charge native converter at upper-run boundaries;
2. exact opposite-phase raw terminal addresses and preserved cap value;
3. exact codimension-one criterion;
4. sharp \(d+1\)-vertex, \(d\)-edge fan lower bound;
5. sharp serial threshold and its Hall demand histogram.

Not claimed:

1. a protected general fan already exists in the carrier;
2. native first-exit plateaux realize its internal values;
3. cap/core names and guards accept every raw boundary socket;
4. the no-go covers arbitrary nonlocal compiler recoding.

Within this boundary, the theorem is proof-safe.
