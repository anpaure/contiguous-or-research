# Audit of the quiet-source clock minor

**Date:** 2026-08-06  \
**Method:** literal row replay and reverse decoding; no computation  \
**Verdict:** the labelled first-scan statements pass.  Quotient descent
and terminal boundary pairing remain explicitly outside scope.

## 1. Local directed rows

The scan rows are

\[
01\leftrightarrow10,\qquad
02\leftrightarrow11,\qquad
12\leftrightarrow21,
\]

and the source is on the majority shore.  Therefore, after any first
physical nonwrap transfer, its endpoint is on the minority shore and the
selected scan row is oriented from that endpoint back to the majority
shore.

The source entrances replay as

\[
\begin{array}{rcl}
20&\to&11\to02,\\
22\mid00&\to&21\mid10\to12\mid10,\\
00\mid22&\to&01\mid12\to10\mid12.
\end{array}
\]

Across the boundary-to-\(p_1\) connector they replay as

\[
\begin{array}{rcl}
22_{\partial}\mid00&\to&21_{\partial}\mid10
                         \to21_{\partial}\mid01,\\
00_{\partial}\mid22&\to&01_{\partial}\mid12
                         \to01_{\partial}\mid21.
\end{array}
\]

In each row the scan pair is nonboundary and precedes the boundary pair,
so no displayed vertex is deleted with \(V(P)\).

## 2. Zipper replay

For \(b,c\in\{0,2\}\), put \(q(b)=(b,b)\) and \(c(b)=(1,b)\).
Then

\[
\begin{array}{rcl}
00\mid(1,c)&\to&01\mid(0,c)\to10\mid(0,c),\\
22\mid(1,c)&\to&21\mid(2,c)\to12\mid(2,c).
\end{array}
\]

This is exactly

\[
                         q(b)c(c)\leadsto c(b)(b,c).
\]

The right marker stores both binary labels.  Hence the rewrite is
injective and reverses uniquely once the current clock position is known.
The least nonquiet scan pair is that clock position.

The two activation endings are

\[
q(b)q(1)\leadsto c(b)c(b)
\]

and

\[
q(b)q(2-b)\leadsto c(b)c(2-b).
\]

Equality versus inequality of the two \(c\)-labels distinguishes the
activation types.  The untouched suffix and boundary marker then recover
the original source.  Thus no two selected majority-shore paths meet.
Every minority intermediate is the \(N\)-mate of its next majority
vertex, so minority collisions are also impossible.

## 3. Source exhaustion

At central compressed mass, \(u\in\{0,1,2\}^m\) has sum \(m\).

* An internal digit one gives the first entrance.
* If there is no internal one, the internal digits are zero/two.  They
  cannot all be zero, since then \(u_m=m>2\), and cannot all be two,
  since then \(u_m=2-m<0\).  Hence an internal zero/two change exists.

Therefore every central source is covered for \(m\ge3\).  The cases
\(m<3\) are finite base sectors and are not asserted by the theorem.

## 4. Strict-gammoid conclusion

The paths link every source in \(Q\) to a distinct terminal.  By the
already-proved source-contraction representation of \(S/V(P)\), their
terminal set is a basis.  This inference uses no boundary occurrence and
no Pfaffian cancellation claim.

## 5. Boundary-aperture replay

At a promoted root clock \(p_1=c(b)=(1,b)\), let the current
coordinate-zero value be \(d\in\{0,2\}\).  The unique transfer making it
one gives

\[
                         (p_1,t_0)=(1,b;d)
          \longrightarrow (d,b;1).
\]

The four post-transfer \(p_1\)-states are

\[
\begin{array}{c|cccc}
(d,b)&(0,0)&(0,2)&(2,0)&(2,2)\\ \hline
p_1&00&02&20&22.
\end{array}
\]

Only \(02\) is nonquiet.  It toggles to \(11\); in the other three cases
the next nonquiet zipper marker toggles.  Thus every branch is a directed
two-arc extension and the displayed local state reverse-decodes \(d,b\).

The direct \(u_1=1\) branches end at

\[
 (p_1,\partial)=(01,01\text{ or }21),\qquad(21,21).
\]

These signatures are pairwise disjoint and disjoint from the four generic
states.  No boundary-activation route is used in the canonical bank; the
binary core always activates at its first internal zero/two change.

Every final aperture state has \(t_0=1\).  Its merged boundary hub recovers
the other boundary digit by subtracting one from the merged value, so the
hub map is injective on the entire terminal bank.

## 6. Exact remaining scope

The audit does **not** establish:

1. a physical boundary matching on the terminal basis;
2. an \(H\)-equivariant phase-cube clock matching for nontrivial
   stabilizer \(H\);
3. orbit-injectivity of the terminal hub signatures;
4. hub safety of the complementary nonwrap matching; or
5. the odd-current theorem.

The one-component obstruction is literal: transfers in the clock-tail
minor avoid \(p_1\), so coordinate zero never changes, while the two
endpoints of every boundary edge have different coordinate-zero values.
The aperture now reaches one endpoint of a distinct-colour boundary edge
from every source.  Since the central source rank \(|Q|\) is odd, the next
step is the one-socket paired-basis problem: choose \((|Q|-1)/2\) of those
hub-distinct edges together with one allowed socket endpoint so that the
resulting \(|Q|\) endpoints form one surplus basis.  Individual
reachability and hub separation no longer remain open in the labelled
sector.

After normalizing the aperture basis to the identity and writing the
partner columns as \(C\), a socket \(k\) and a set
\(I\subseteq[|Q|]\setminus\{k\}\), \(|I|=(|Q|-1)/2\), work exactly when

\[
 \det C\bigl[[|Q|]\setminus(I\cup\{k\}),I\bigr]\ne0.
\]

Equivalently its generating skew matrix is

\[
                         D_xC^{\mathsf T}-CD_x.
\]

A disjoint counterflow whose last-intersection map is a permutation
\(\pi\) can close the actual odd-rank gate by a deterministic socket
selection exactly when the cycle containing the socket is odd and every
other cycle of \(\pi\) is even.  This parity statement is a condition on
the counterflow construction, not a proof that the required counterflow
exists.

If the socket is freely selectable, this is equivalent to saying that
\(\pi\) has exactly one odd cycle.  The central source rank is odd because
the complement involution \(u\mapsto2-u\) pairs every source except
\(1^m\).  Hence a single Hamilton cycle on the quiet sources would be a
sufficient deterministic predecessor map, but its physical realization
remains unproved.
