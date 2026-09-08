# Monotone geodesic chunks are literal two-chain grid strips

Date: 2026-07-25

Method: pure mathematics only.

## 0. Result

The monotone Johnson geodesics used in
`MATH_ATTACK_GEODESIC_ORBIT_TRP_OVERLAP_PRUNING_20260725.md` have a stronger
deterministic flag structure than an arbitrary rotor chunk.

Write \(g=\ell+2Q-1\), and parameterize one **buffered** geodesic by

\[
 U=C\ \dot\cup\ \{a_1,\ldots,a_g\}\ \dot\cup\
   \{b_1,\ldots,b_g\}\ \dot\cup\ R,
\]

where \(|C|=m-g\).  Define the full two-chain grid

\[
 G_{i,j}
 =C\cup\{a_{i+1},\ldots,a_g\}
    \cup\{b_1,\ldots,b_j\},
 \qquad 0\le i,j\le g.
 \tag{0.1}
\]

Then the full certificate walk is the diagonal

\[
 X_t=G_{t,t}\qquad(0\le t\le g),
 \tag{0.2}
\]

and every controlled flag at an interior phase is exactly a point of the
diagonal strip:

\[
 \boxed{L_q(t)=G_{t+q,t},\qquad U_q(t)=G_{t-q,t}}
 \tag{0.3}
\]

whenever \(0\le q\le Q\) and \(Q\le t\le g-Q\).  The \(\ell\)
physical central starts are precisely

\[
 t=Q,Q+1,\ldots,Q+\ell-1.
\]

Thus the \(2Q\) boundary phases are only the usual past/future certificate
buffer; they are not selected owner occurrences and need not be repaired.
Every controlled flag of every physical central start is uniquely
determined by the buffered owner geodesic; no hidden rotor realization
remains.  The reset cost is

\[
 O(QW/\ell)=o(W)
\]

for \(Q\ll\ell\ll m\).  Consequently the surviving simultaneous-flag
problem for the geodesic catalogue is exactly a packing problem for
diagonal strips in products of two chains.

This does not prove the strip packing.  It removes a spurious hidden-state
gate and supplies the correct object whose full overlap hierarchy must be
estimated.

## 1. Exact grid identities

The geodesic owner sequence is

\[
 X_t
 =C\cup\{a_{t+1},\ldots,a_g\}
    \cup\{b_1,\ldots,b_t\}.
 \tag{1.1}
\]

This is (0.2).  For \(t+q\le g\), the future owners

\[
 X_t,X_{t+1},\ldots,X_{t+q}
\]

have decreasing \(a\)-suffixes and increasing \(b\)-prefixes.  Their
intersection therefore keeps the smallest \(a\)-suffix and the smallest
\(b\)-prefix:

\[
\begin{aligned}
 \bigcap_{h=0}^qX_{t+h}
 &=C\cup\{a_{t+q+1},\ldots,a_g\}
      \cup\{b_1,\ldots,b_t\}\\
 &=G_{t+q,t}.
\end{aligned}
\tag{1.2}
\]

For \(t-q\ge0\), the past owners

\[
 X_t,X_{t-1},\ldots,X_{t-q}
\]

have largest \(a\)-suffix at time \(t-q\) and largest \(b\)-prefix at
time \(t\).  Hence

\[
\begin{aligned}
 \bigcup_{h=0}^qX_{t-h}
 &=C\cup\{a_{t-q+1},\ldots,a_g\}
      \cup\{b_1,\ldots,b_t\}\\
 &=G_{t-q,t}.
\end{aligned}
\tag{1.3}
\]

The path-hitting identities for a radius-\(Q\) rotor give

\[
 L_q(t)=\bigcap_{h=0}^qX_{t+h},
 \qquad
 U_q(t)=\bigcup_{h=0}^qX_{t-h},
\]

which proves (0.3).

The rank check is automatic:

\[
 |G_{i,j}|=(m-g)+(g-i)+j=m-i+j.
 \tag{1.4}
\]

Thus \(G_{t+q,t}\) has rank \(m-q\) and \(G_{t-q,t}\) has rank
\(m+q\).

## 2. Exact buffering ledger

Use as physical owner starts exactly the \(\ell\) diagonal points

\[
 t=Q,Q+1,\ldots,Q+\ell-1=g-Q.
\]

There are therefore exactly \(\ell\) claimed flags in every signed
controlled row.  The earlier and later \(Q\) diagonal points supply only
the history certificate needed for the path-hitting intersections and
unions.  This is the ordinary buffered-chunk convention: the first
physical state is initialized directly from its ordered partition, and
the future buffer is a certificate, not an emitted continuation.

The literal reset cost of the chunks is

\[
 O(QW/\ell)=o(W),
 \tag{2.1}
\]

and the omitted carrier remainder is \(O(\ell W/m)=o(W)\).  Neither term
changes when the interior flags are viewed as the grid strip (0.3).

## 3. Revised exact gate

For each geodesic chunk, let

\[
 \mathcal G_Q(C,A,B)
 =\{G_{t,t}:Q\le t\le Q+\ell-1\}
  \cup
  \{G_{t+q,t},G_{t-q,t}:
       1\le q\le Q,\ Q\le t\le Q+\ell-1\}.
\]

The simultaneous-flag extraction problem for the trimmed geodesic orbit
is:

> Select almost all carrier-copy tags so that the corresponding sets
> \(\mathcal G_Q(C,A,B)\) have total duplicate excess \(o(W)\), with the
> usual \(O(QW/\ell)\) initialization ledger.

The owner-only hierarchy in the source note controls intersections of the
diagonal points \(G_{t,t}\).  What remains is the weighted overlap
enumerator for the complete diagonal strips.  Because (0.3) is exact,
that is now a purely two-chain-grid incidence problem rather than a hidden
rotor-decoration problem.
