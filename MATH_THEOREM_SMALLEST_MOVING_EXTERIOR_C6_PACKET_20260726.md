# The smallest literal moving-exterior \(C_6\) router

Date: 2026-07-26

The abstract common-core \(C_6\) can be realized by literal equal-length
Johnson geodesics with a complete \(X/Y\) collar ledger.  The metric
correction is essential: its two states are not “identity versus a
3-cycle.”  They have absolute twists \(\tau^2\) and \(\tau\), respectively.
Both have constant displacement one, so one common moving exterior works.

The construction below is minimal in cycle size, local rank, and exterior
displacement.  It is a genuine local packet.  A separate seam theorem is
still needed to install copies at positive density; Section 6 gives the
exact direct-seam obstruction.

## 1. Coordinates and ports

Fix an ambient middle rank \(m\ge3\).  Choose pairwise disjoint data

\[
 |C|=m-3,\qquad u,v,k,a_0,a_1,a_2,
\]

and use indices modulo three.  Put

\[
 O_L=C\cup\{u\},\qquad O_R=C\cup\{v\},\qquad
 J=\{k,a_0,a_1,a_2\}.                                  \tag{1.1}
\]

Thus \(|O_L|=|O_R|=m-2\), \(|J|=4\), and

\[
                         e=|O_L\setminus O_R|=1.        \tag{1.2}
\]

The three local rank-two ports are

\[
                         P_i=\{k,a_i\},                 \tag{1.3}
\]

and \(\tau(P_i)=P_{i+1}\).

## 2. The two path packets

Define lower \(m\)-sets

\[
\begin{aligned}
 X_0^i&=C\cup\{u,k,a_i\},\\
 X_1^i&=C\cup\{u,a_i,a_{i+1}\},\\
 X_2^i&=C\cup\{v,a_i,a_{i+1}\},
\end{aligned}                                           \tag{2.1}
\]

and upper \((m+1)\)-sets

\[
\begin{aligned}
 Y_0^i&=C\cup\{u,k,a_i,a_{i+1}\},\\
 Y_1^i&=C\cup\{u,v,a_i,a_{i+1}\}.
\end{aligned}                                           \tag{2.2}
\]

The old packet consists of

\[
 \mathcal P^-_i:
 X_0^i-Y_0^i-X_1^i-Y_1^i-X_2^i,
 \qquad i\in\mathbb Z_3.                                \tag{2.3}
\]

The three first incidences in (2.3) are one alternating common-core
\(C_6\):

\[
\begin{aligned}
 X_0^0-Y_0^0-X_0^1-Y_0^1-X_0^2-Y_0^2-X_0^0,            \tag{2.4}
\end{aligned}
\]

whose common \((m-1)\)-core is

\[
                         \widehat K=C\cup\{u,k\}.        \tag{2.5}
\]

Toggle the selected edges \(X_0^iY_0^i\).  The new packet is

\[
 \mathcal P^+_{i+1}:
 X_0^{i+1}-Y_0^i-X_1^i-Y_1^i-X_2^i,
 \qquad i\in\mathbb Z_3.                                \tag{2.6}
\]

### Theorem 2.1 (exact packet)

Both (2.3) and (2.6) are families of three pairwise vertex-disjoint
length-two Johnson geodesics.  They have exactly the same lower and upper
vertex ledgers.

#### Proof

Every displayed adjacency is containment.  In (2.3), the two exchanges
are

\[
                         k\mapsto a_{i+1},\qquad
                         u\mapsto v.                    \tag{2.7}
\]

Both inserted elements occur in the final state and both removed elements
are absent there.  Thus the path has Johnson length and distance two.

For the new path rooted at \(X_0^j\), put \(i=j-1\) in (2.6).  Its
exchanges are

\[
                         k\mapsto a_{j-1},\qquad
                         u\mapsto v,                    \tag{2.8}
\]

again two distinct permanent exchanges.  Hence it is also geodesic.

Within any one displayed layer, the three adjacent pairs

\[
 \{a_0,a_1\},\quad\{a_1,a_2\},\quad\{a_2,a_0\}
\]

are distinct.  Different lower layers are distinguished by the
presence-pattern of \(k,u,v\), and the two upper layers are distinguished
in the same way.  Hence all paths in either packet are vertex-disjoint.

Finally, the toggle changes only incidences.  Equations (2.3) and (2.6)
use literally the same \(X_0^i,X_1^i,X_2^i,Y_0^i,Y_1^i\), once each.
\(\square\)

## 3. Exact monodromy and the metric equation

The right boundary satisfies

\[
 X_2^i
 =O_R\cup\{a_i,a_{i+1}\}
 =O_R\cup(J\setminus P_{i+2}).                          \tag{3.1}
\]

Thus the old packet sends

\[
                         P_i\longmapsto J\setminus P_{i+2},
\]

so its absolute twist is \(\tau^2\).

In the new packet, the path rooted at \(P_j\) uses the suffix with
\(i=j-1\), and therefore ends at

\[
 X_2^{j-1}
 =O_R\cup\{a_{j-1},a_j\}
 =O_R\cup(J\setminus P_{j+1}).                          \tag{3.2}
\]

Its absolute twist is \(\tau\).  The relative router action is the
3-cycle \(\tau^{-1}\).

Both states satisfy the moving-exterior metric gate exactly:

\[
\boxed{
 e=1
 =|P_i\setminus\tau(P_i)|
 =|P_i\setminus\tau^2(P_i)|
 \qquad(i\in\mathbb Z_3).}                              \tag{3.3}
\]

The endpoint distances are therefore two in both settings, exactly the
number of exchanges in Theorem 2.1.

### Proposition 3.1 (why identity versus \(\tau\) is impossible)

No common pair \(O_L,O_R\) can realize, with one fixed equal geodesic
length, an identity state and a nonidentity \(\tau\)-state on these ports.

#### Proof

The moving-exterior equation is

\[
                         e=|P\setminus\sigma(P)|.       \tag{3.4}
\]

For \(\sigma=1\), its right side is zero.  For either nontrivial power of
\(\tau\), it is one.  The same exterior pair cannot have both values of
\(e\). \(\square\)

This is why the physical packet must compare the two nonidentity absolute
twists \(\tau^2\) and \(\tau\).  Abstractly subtracting the identity
matching hides this metric requirement.

## 4. Complete collar ledger

There are no suppressed crossing states.  The two collars are exactly

\[
\begin{array}{c|c|c}
\text{exchange}&\text{upper collar}&\text{next lower state}\\ \hline
k\mapsto a_{i+1}
 &C\cup\{u,k,a_i,a_{i+1}\}
 &C\cup\{u,a_i,a_{i+1}\}\\
u\mapsto v
 &C\cup\{u,v,a_i,a_{i+1}\}
 &C\cup\{v,a_i,a_{i+1}\}.
\end{array}                                             \tag{4.1}
\]

After the switch, only the owner of the first upper collar changes:
\(X_0^{i+1}\) enters \(Y_0^i\) in place of \(X_0^i\).  The second collar
and every lower state are unchanged.  Therefore

\[
\Delta_{\mathcal X}=0,\qquad
\Delta_{\mathcal Y}=0                                  \tag{4.2}
\]

as literal multisets, including the mixed exterior state containing both
\(u\) and \(v\).

Both boundary families are also unchanged as sets:

\[
 \{X_0^i:i\in\mathbb Z_3\},\qquad
 \{X_2^i:i\in\mathbb Z_3\}.                            \tag{4.3}
\]

Hence the packet can replace one setting by the other inside any ambient
path ledger which already contains its old state, with the right tails
permuted by the relative 3-cycle.

## 5. Literal minimum-wreath interpretation and minimality

Each path is not merely an abstract incidence path.  Its ordered
remove/insert pairs are given in (2.7) or (2.8), with no coordinate
repeated.  Complete these two removal and insertion lists by arbitrary
orders of the still unused ambient coordinates.  The standard
omitted-coordinate construction then extends each path to a contiguous
segment of a minimum odd-graph wreath.

The parameters are minimal.

1. \(h\ge3\), because the adjacent-layer Boolean incidence graph is
   \(C_4\)-free.
2. A common-core \(C_{2h}\) at local rank \(r\) needs \(h\le r+1\).
   Thus \(h=3\) forces \(r\ge2\).
3. A nonidentity twist forces \(e\ge1\) by (3.4).

The packet attains

\[
                         (h,r,e)=(3,2,1).               \tag{5.1}
\]

## 6. The remaining direct-seam obstruction

The packet is one-way between two different boundary geometries.  The
left port family has

\[
 \bigcap_i X_0^i=C\cup\{u,k\},
 \qquad \left|\bigcap_i X_0^i\right|=m-1,              \tag{6.1}
\]

whereas the right port family has

\[
 \bigcap_i X_2^i=C\cup\{v\},
 \qquad \left|\bigcap_i X_2^i\right|=m-2.              \tag{6.2}
\]

Thus no coordinate relabelling can identify the right boundary with the
left boundary of another common-core copy: intersection cardinality is a
setwise invariant.  In local language, the input ports form a star
\(\{k,a_i\}\), while the output ports form the complementary triangle
\(\{a_i,a_{i+1}\}\).

This does not negate the packet.  It proves that direct serial repetition
requires an additional collar which changes the boundary geometry.
Such a collar must itself be audited for geodesicity.  For example, simply
reinserting \(k\) to turn the triangle back into a star backtracks a
coordinate already removed in (2.7), so the concatenated path is not
geodesic.

Accordingly the exact proved boundary is:

\[
\boxed{
\begin{gathered}
\text{a smallest literal equal-length moving-exterior \(C_6\) router
exists, with full \(X/Y\) collar ownership;}\\
\text{a positive-density or serial conveyor still needs a
star-to-triangle seam theorem.}
\end{gathered}}                                         \tag{6.3}
\]

No constant-one conclusion follows from the local packet alone.
